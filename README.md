<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-21374-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-30 12:18 ｜ **论文总数 / Total Papers**: 21374（近 30 天 / Recent 30 days: 2242）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 21374 篇论文（含摘要、分类筛选、搜索）/ View all 21374 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 554
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 458
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 37
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 93
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 393
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 535
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3702
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 53
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 828
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 109
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2472
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2132
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1960
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1854
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 204
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 255
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5552

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2242 篇，完整 21374 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2242 papers from the last 30 days (with date, authors & abstract). For the full list of 21374 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-07-29** — Yongjian Guo, Wanlun Ma, Lingyu Shen et al. — [On-Policy Distillation for LLM Safety: A Routing Approach to Template-Robust Realignment](http://arxiv.org/abs/2607.27081v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning is the dominant paradigm for specializing large language models (LLMs), yet it exposes a critical vulnerability: malicious data providers can embed harmful behaviors into downstream corpora, creating models that retain professional skills while violating human values on demand. Existing safety-realignment defenses often fail in practice due to three key limitations: they frequently cause catastrophic forgetting of specialized skills; their effectiveness collapses when the defender ca...
  </details>

- **2026-07-29** — Anthony Hughes, Nicole Xing, Collin Francel et al. — [ToxScreen: Detecting Whether an LLM Has Been Poisoned](http://arxiv.org/abs/2607.26849v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed in high-stakes domains, adversaries may poison training data to implant backdoors: hidden triggers that covertly manipulate model behavior at inference time. We ask whether a defender can recover such a trigger under realistic affordances, namely white-box access to the weights and knowledge of the behavior of concern, but no training data, no trusted reference model, no knowledge of the trigger, and no certainty that the model is poisoned. To evaluat...
  </details>

- **2026-07-29** — Haoyu Zhang, Shibo Zheng, Xiangchen Guan et al. — [Borrowed Strength: Best-of-N Search over a Code EncodingBreaks Self-Check Jailbreak Defenses](http://arxiv.org/abs/2607.26639v1)
  <details><summary>📄 Abstract</summary>
  A self-check defense asks the target model to assess a request before answering it; SAGE, the strongest published instance, reports an average 99% defense success rate. We show it can be breached by composing two attacks that are individually harmless against it: an established code-completion encoding and an established best-of-N search, neither of which exceeds 4.7% of behaviors alone. Composed, with the search budget spent on the encoding, they reach 67/22/15% across three open targets, and t...
  </details>

- **2026-07-29** — Haoyu Zhang, Zhuoxi Wang, Shibo Zheng et al. — [Recover, Decode, Reguard: Guard-Agnostic Defense Amplification againstEncoded VLM Jailbreaks](http://arxiv.org/abs/2607.26574v1)
  <details><summary>📄 Abstract</summary>
  Safety classifiers ("guards") are the dominant black-box defense for vision-language models, yet they judge an input's surface form, not its meaning: a harmful request re-encoded as set theory, formal logic, a rare language, code, or an image of text slips past a guard that would block it in plain language -- the decode gap. The natural fix is a guard-agnostic recover-and-decode amplifier that transcribes image content and restates encoded text into its plain payload before the guard, so any off...
  </details>

- **2026-07-29** — Jiachen Qian, Junyu Li — [Prosody-driven Jailbreaks in Audio LLMs: A Controlled Study and Mechanistic Analysis](http://arxiv.org/abs/2607.26541v1)
  <details><summary>📄 Abstract</summary>
  Audio-capable foundation models enable end-to-end spoken interaction, but they also introduce safety risks beyond transcript content. It remains unclear how much jailbreak capability can arise from matched-text variation in speech delivery rather than from lexical rewriting or broader style transfer. We study this question by holding transcript content fixed and varying six speech-delivery presets whose acoustic attributes may co-vary. We present PJ-Break, a black-box evaluation protocol with pr...
  </details>

- **2026-07-28** — Abhishek Kumar Singh, Shrey Nag, Sachita et al. — [Inspect India Evals: An Open Benchmarking Framework for Evaluating Large Language Models in the Indian Linguistic and Cultural Context](http://arxiv.org/abs/2607.25375v1)
  <details><summary>📄 Abstract</summary>
  India is a vast nation of over 1.4 billion people, varied by hundreds of diverse and locally specific traditions and cultures and 22 officially recognized languages. Large language models (LLMs) are now being deployed on a massive scale throughout the mainland as well as in remote villages. However, the common benchmarks - MMLU, BIG-Bench, and TruthfulQA are almost exclusively English- and Western-centric. They do not identify those safety, fairness, and accuracy failures unique to the Indian co...
  </details>

- **2026-07-28** — Haowen Dai, Zonghao Ying, Wenfeng Li et al. — [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](http://arxiv.org/abs/2607.25255v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent. This is a growing social-impact challenge: systems handling sensitive information or consequential tools can turn routine delegation into unauthorized disclosure or unsafe action. We argue that this failu...
  </details>

- **2026-07-27** — Meng Xie, Li Zeng, Hangtao Zhang et al. — [TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models](http://arxiv.org/abs/2607.24897v1)
  <details><summary>📄 Abstract</summary>
  Recent commercial image-generation models can generate high-quality images with readable text (e.g., posters, infographics, and manuals), attracting considerable attention. Yet we first show that this same capability also introduces a previously unreported safety vulnerability: these systems may refuse to generate harmful text directly, yet permit the same content when rendered as text within generated images, i.e., safety alignment does not reliably transfer from textual outputs to text embedde...
  </details>

- **2026-07-27** — Tong Zhang, Zexin Li, Simin Chen et al. — [When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs](http://arxiv.org/abs/2607.24392v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak defenses are essential for protecting large language models (LLMs), but they can also introduce secondary costs that weaken model utility. We present a systematic study of these defense trade-offs along three dimensions: performance impact, over-refusal on benign inputs, and inference cost. Rather than treating defenses as a single class, we organize them by operational strategy and examine how different strategies correlate with different side-effect profiles. Across state-of-the-art ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-07-28** — Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al. — [GPT-Red: Automated Red Teaming via Self-Play at Scale](http://arxiv.org/abs/2607.26115v1)
  <details><summary>📄 Abstract</summary>
  We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it to adversarially train GPT-5.6, our most robust model to prompt injections to date. To create GPT-Red, we design a scalable self-play algorithm where the model is tasked with attacking a diverse population of simultaneously-trained defender ...
  </details>

- **2026-07-27** — Arseny Kravchenko, Vadim Liventsev, Innokentii Konstantinov et al. — [Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents](http://arxiv.org/abs/2607.24625v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents processing mixed-confidentiality data face severe security risks from prompt injection attacks and reasoning errors. While dynamic Information Flow Control (IFC) provides structural security guarantees, traditional taint tracking permanently taints an agent's context upon reading unvetted data, severely restricting downstream utility. We present APPA (Agentic Permissions Policy Algebra), an IFC framework that resolves this usability bottleneck through engine-managed context...
  </details>

- **2026-07-27** — Max Landauer, Florian Skopik, Markus Wurzenberger et al. — [Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection](http://arxiv.org/abs/2607.24174v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into Security Operations Center (SOC) workflows, where they support analysts in tasks such as the interpretation of system logs. However, the ability of LLMs to directly process untrusted textual input also introduces new attack surfaces. In particular, attackers can inject contextual information or explicit instructions into log entries in order to influence how malicious activity is interpreted by the model. Despite the growing adoption ...
  </details>

- **2026-07-27** — Mohan Manivannan, Dalal Alharthi — [Agentic Cloud Decoys: A Deception-Driven Framework for Autonomous Intrusion Investigation](http://arxiv.org/abs/2607.24006v1)
  <details><summary>📄 Abstract</summary>
  Cloud telemetry arrives at a scale that, paradoxically, makes intrusion understanding harder rather than easier. Attackers operate through legitimate identity, federated session tokens, and cloud native APIs indistinguishable from routine administration, and analysts spend an incident reconstructing context the logs already contain. We present Cloud Decoy AI Agent, a framework pairing a high fidelity cloud decoy with an autonomous language model agent that compresses the path from suspicious act...
  </details>

- **2026-07-27** — Wenhao Lan, Shan Li, Xinhua Lai et al. — [ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents](http://arxiv.org/abs/2607.23999v2)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents process untrusted content, maintain memory, delegate across agents, and invoke side-effecting tools. Existing prompt-injection evaluations typically summarize security with terminal attack or policy outcomes, but equal endpoints can conceal different post-exposure traces and different losses of authorized utility. We introduce ContainmentBench, a sandboxed, trace-based benchmark that separately measures benchmark-defined endpoint policy compliance, instrumented logged propa...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-07-29** — Xuanze Chen, Xukang Xie, Wentao Fu et al. — [MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair](http://arxiv.org/abs/2607.27080v1)
  <details><summary>📄 Abstract</summary>
  Memory systems allow agents to retain and reuse information from past interactions, but they can also let malicious content persist. A malicious instruction crafted by an attacker may be stored in long-term memory, recalled much later, and quietly shape a real action. Recent benchmarks increasingly examine agent memory security, yet few trace the same malicious semantics across persistence, downstream consequences, and selective repair under diverse memory-backend comparisons. To address this ga...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-07-28** — Jianing Geng, Ruiqi He, Zekun Fei et al. — [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](http://arxiv.org/abs/2607.25560v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skill...
  </details>

- **2026-07-27** — Rajat Sainju, Dariusz Jarosz, Hairong Shang et al. — [A corrective agentic hybrid RAG and an operations-grounded evaluation for a scientific facility](http://arxiv.org/abs/2607.24663v1)
  <details><summary>📄 Abstract</summary>
  Scientific user facilities accumulate decades of operational knowledge that no single search index covers: electronic logbooks, technical documents, internal wikis, operations chat messages, maintenance records, and live control-system data. We present APS-RAG, Advanced Photon Source Retrieval Augmented Generation, a deployed platform that makes the institutional knowledge at the Advanced Photon Source (APS) accessible to staff through natural-language queries, along with an operations-grounded ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-07-28** — Pushkal Kumar, Tucker Nielson, Tanish Kolhe et al. — [RAGuard: A Layered Defense Framework for Retrieval-Augmented Generation Systems Against Data Poisoning](http://arxiv.org/abs/2607.26339v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems ground large language models (LLMs) in external corpora, but this reliance exposes them to corpus poisoning: maliciously injected passages that manipulate retrieved evidence. We introduce RAGuard, a layered defense against \emph{factual} corpus-poisoning attacks on RAG pipelines. The first layer adversarially fine-tunes a dense retriever on synthetic poisoned documents (fabricated facts, contradictions, and reasoning traps), teaching it to downrank ma...
  </details>

- **2026-07-28** — Jasorsi Ghosh — [Learning Implicit Causal World Models from Multi-Agent Demonstrations](http://arxiv.org/abs/2607.26336v1)
  <details><summary>📄 Abstract</summary>
  In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms. This problem is exacerbated in multi-agent systems where physical transitions are intertwined with strategic agent intents, causing world models to fail under distribution shift. We introduce Implicit Causal World Models to recover environmental dynamics from offline demonstrations without requiring pre-defined causal graphs. By inc...
  </details>

- **2026-07-28** — Zhou Feng, Jiahao Chen, Chunyi Zhou et al. — [Lilith: Backdoor Generalization under Training-Inference Trigger Shift](http://arxiv.org/abs/2607.26099v1)
  <details><summary>📄 Abstract</summary>
  Machine-learning services increasingly rely on public data, third-party providers, and outsourced training, creating opportunities for data-poisoning attacks that implant persistent malicious behavior while preserving benign utility. However, existing backdoor studies largely evaluate exact trigger reuse, training-exposed trigger diversity, or variations along predefined transformation axes. They therefore leave a critical blind spot: whether a backdoor learned from one training-time trigger can...
  </details>

- **2026-07-28** — Rui Yang, Michael Fu, Kla Tantithamthavorn et al. — [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](http://arxiv.org/abs/2607.25619v1)
  <details><summary>📄 Abstract</summary>
  Software engineering teams now deploy AI coding agents (Cursor, Claude Code, GitHub Copilot) as first-class productivity tools, installing domain-specific skill files to tailor agent behavior to project APIs, framework conventions, and organizational workflows. These complex Markdown files are easily downloaded from public registries with a single npx skills add command and no real security screening, representing a novel supply-chain attack surface: a malicious skill file can silently reprogram...
  </details>

- **2026-07-28** — Maria Rosaria Briglia, Igor Maljkovic, Antonio Emanuele Cinà et al. — [Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering](http://arxiv.org/abs/2607.25479v1)
  <details><summary>📄 Abstract</summary>
  Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. In this paper, we show that a malicious provider can exploi...
  </details>

- **2026-07-27** — Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang et al. — [Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study](http://arxiv.org/abs/2607.24893v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. We investigate how early such an attack can be detected while the run is still unfolding, and how robustly it can be caught on...
  </details>

- **2026-07-26** — Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj et al. — [TriShieldRAG: A Three-Ring Defense-in-Depth Framework Against Knowledge Corruption in Retrieval-Augmented Generation](http://arxiv.org/abs/2607.23838v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) lets a large language model answer questions using documents retrieved from an external knowledge base at query time. This makes RAG useful for private data, fast-changing information, and reducing hallucination, but it also means the model's answer is only as trustworthy as whatever the retriever hands it. If the knowledge base accepts writes from more than one party, an attacker needs only a handful of adversarial documents to steer the model toward a chose...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-07-29** — Seunghun Yu, Meiyi Zhu, Petar Popovski et al. — [Conformal Changepoint Localization and Root Cause Analysis with Corrupted Observations](http://arxiv.org/abs/2607.26481v1)
  <details><summary>📄 Abstract</summary>
  Detecting when the statistical behavior of an engineered system changes, and identifying which component is responsible, are core problems in the monitoring of telecommunication networks, robotic platforms, security infrastructure, and multi-agent systems. In safety- and mission-critical deployments, such decisions must be accompanied by statistical reliability guarantees rather than by point estimates alone. Conformal changepoint localization (CONCH) and conformal root cause analysis (CROC) mee...
  </details>

- **2026-07-28** — Yimao Guo, Zuomin Qu, Wei Lu — [I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models](http://arxiv.org/abs/2607.25522v2)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of video generation models has led to the increasing misuse of image-to-video (I2V) models. Although substantial progress has been made in detecting AI-generated videos, proactive defenses against I2V models remain underexplored. In particular, current proactive defenses against I2V models predominantly rely on gradient-based adversarial attacks, which require defenders to possess GPUs with substantial memory resources (VRAM) to generate adversarial examples. To address thi...
  </details>

- **2026-07-28** — Anwar Alajmi, Ayed Salman, Imtiaz Ahmad — [Evaluation of Adversarial Robustness in Arabic Language Models](http://arxiv.org/abs/2607.25814v1)
  <details><summary>📄 Abstract</summary>
  The emergence of the recent outstanding capabilities of Arabic Language Models has opened doors for exposing their vulnerabilities. One of the major security risks associated with such Natural Language Processing models is adversarial attacks. These attacks can deceive the model into the wrong prediction, raising critical model security and safety concerns. This study aims to assess the robustness of five state-of-the-art Arabic Language Models under a distinct set of Arabic adversarial attacks ...
  </details>

- **2026-07-28** — Khalil Alhaj, Razane Tajeddine, Hadi Sarieddeen — [SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication](http://arxiv.org/abs/2607.25676v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication systems such as deep semantic communication (DeepSC) offer high efficiency but are vulnerable to adversarial attacks on their underlying neural networks. We address a physical-layer man-in-the-middle (MitM) threat in which an adversary injects perturbations into the transmitted signal to distort its meaning. We propose SignDeepSC, an architectural defense that achieves adversarial robustness without requiring explicit adversarial example generation during training. The app...
  </details>

- **2026-07-28** — Yimao Guo, Zuomin Qu, Wei Lu — [I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models](http://arxiv.org/abs/2607.25522v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of video generation models has led to the increasing misuse of image-to-video (I2V) models. Although substantial progress has been made in detecting AI-generated videos, proactive defenses against I2V models remain underexplored. In particular, current proactive defenses against I2V models predominantly rely on gradient-based adversarial attacks, which require defenders to possess GPUs with substantial memory resources (VRAM) to generate adversarial examples. To address thi...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 20 papers

- **2026-07-29** — Yikun Li, Ting Zhang, Jiakun Liu et al. — [Graph Is the Verifier: Agentic Reinforcement Learning for Interprocedural Vulnerability Detection](http://arxiv.org/abs/2607.26656v1)
  <details><summary>📄 Abstract</summary>
  Real-world vulnerabilities often span multiple functions, yet most learning-based detectors classify each function in isolation: on a sample of real CVEs, we find that 71.7% of vulnerable functions require evidence from outside the function to be classified correctly. Agentic reinforcement learning (RL) could close this gap by enabling a model to gather that evidence itself, but it lacks a reliable reward, since a reward defined on the final verdict alone can be obtained without performing any i...
  </details>

- **2026-07-29** — Mostafijur Rahman Akhond, Md Afif Al Mamun, Gias Uddin et al. — [Impossible to hide secret ...: Uncovering Security and Privacy Issues in LLM-native IDEs](http://arxiv.org/abs/2607.26390v1)
  <details><summary>📄 Abstract</summary>
  LLM-native IDEs (Integrated Development Environments), aka LIDEs, are designed from the ground up to work with Large Language Models (LLMs). LIDEs have found remarkable success in Software Engineering (SE) tasks such as coding, debugging, and program comprehension. LIDEs are software systems, and, like any system, they can exhibit vulnerabilities. In this paper, we study the security and privacy issues that developers reported while using popular LIDEs in their development tasks. We collected 1....
  </details>

- **2026-07-29** — Yicheng Feng, Yan Zhang, Yan Cheng et al. — [Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents](http://arxiv.org/abs/2607.27083v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools leaves the task under-informed, while too many adds cost, context load, and privacy exposure. Routers and retrievers can rank candidate tools by relevance, but a ranking alone does not determine how many are worth selecting. Existing approaches leave acquisition under heterogeneous costs unaddressed....
  </details>

- **2026-07-29** — Jingbo Zhou, Yusai Zhao, Qi Bao et al. — [OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](http://arxiv.org/abs/2607.27155v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly expected to assist users in completing tasks. However, existing benchmarks provide limited support for evaluating whether agents can carry out office-suite workflows at a reasonable cost. We introduce OmegaUse-OfficeVal, a benchmark for evaluating LLM agents on long-horizon office-suite tasks with task-level economic grounding. The benchmark comprises 100 tasks derived from office-suite requests proposed by practitioners and adapted through a pr...
  </details>

- **2026-07-29** — Lingyang Zeng, Guangze Chen, Kaichen Yu et al. — [Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data](http://arxiv.org/abs/2607.27056v1)
  <details><summary>📄 Abstract</summary>
  Personalized agents are increasingly applied to assist users across a wide range of tasks. Effective personalized assistance requires not only retrieving explicit facts from past interactions stored in agent memory, but also inferring abstract personal characteristics. However, existing memory benchmarks primarily evaluate whether an agent can retrieve information explicitly stated in conversational histories, failing to provide an effective assessment of deeper user understanding. In this work,...
  </details>

- **2026-07-29** — Yi-Sheng Hsu, Nermeen Abou Baker, Uwe Handmann — [Enhancing Generative Information Extraction with Two-step Validation: A Product Attribute Use Case](http://arxiv.org/abs/2607.26780v1)
  <details><summary>📄 Abstract</summary>
  The ability of large language models (LLMs) to process and generate text has introduced potential for applications in information extraction (IE). While it's debated whether LLMs outperform smaller fine-tuned models for classification tasks, their strong generalization capability makes them promising for domains with limited labeled data available for fine-tuning. This advantage is particularly relevant for the emerging application of the digital product passport (DPP), where the problem space i...
  </details>

- **2026-07-29** — Harshiddhi Pathak, Gowtham Reddy N, Mrinal Acharya et al. — [An Attention-Based Framework for Alzheimers Disease Classification Using Resting-State fMRI](http://arxiv.org/abs/2607.26746v1)
  <details><summary>📄 Abstract</summary>
  Accurate identification of Alzheimers disease (AD) using resting-state functional magnetic resonance imaging (rs-fMRI) remains challenging due to the high dimensionality, noise, and complex inter-regional dependencies inherent in functional brain connectivity, which limit the effectiveness of traditional approaches based on handcrafted connectivity features or conventional machine learning models. In this work, we present an attention-based deep learning framework for Alzheimers disease classifi...
  </details>

- **2026-07-28** — Nazanin Amini, Kevin Desai — [MoSAIC: Aligned Intervention Supervision for Part-Local Motion Style Transfer](http://arxiv.org/abs/2607.26304v1)
  <details><summary>📄 Abstract</summary>
  Editing character motion often requires transferring a gesture or gait from one or more reference motions while preserving the source action, timing, root trajectory, and unselected body regions. Existing motion datasets, however, rarely provide paired targets for arbitrary part-local content--reference combinations, and self-reconstruction training may allow a diffusion model to reproduce the content motion while underusing the routed reference. We present MoSAIC, a latent diffusion framework f...
  </details>

- **2026-07-28** — Armin Maleki, Hayder Radha — [HeteroPROPMT: A Real-time and Privacy-Preserving Heterogeneous Collaborative Perception Framework](http://arxiv.org/abs/2607.26283v1)
  <details><summary>📄 Abstract</summary>
  Collaborative Perception (CP) improves autonomous systems' awareness of their surroundings by sharing sensor data, intermediate features, and detection results. In real-world deployments, however, collaborating vehicles often use heterogeneous sensors, perception models, datasets, and training domains, creating feature-space shifts that degrade downstream fusion and detection. Existing approaches typically retrain fusion and detection components or introduce modality-specific feature interpreter...
  </details>

- **2026-07-28** — Takeshi Nishikawa — [Lightweight Image Classification of Raptor Species for Edge Devices: Rare-Species Dataset Expansion via Video Frame Extraction, Knowledge Distillation, and TensorRT Deployment](http://arxiv.org/abs/2607.26238v1)
  <details><summary>📄 Abstract</summary>
  We investigate lightweight raptor-species classification for real-time edge deployment in wind-turbine collision mitigation. Using DINOv2-L (304M parameters) as a teacher, we distilled three lightweight students (MobileNetV4, ViT-Small, and EfficientNet-B0). To reduce confusion between closely related species, we expanded the dataset to 12,519 images, including an increase in Steller's Sea Eagle images from 463 to 2,050 via video-frame extraction. Under a group split that separates samples at th...
  </details>

- **2026-07-28** — Akshay Sasi — [Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization](http://arxiv.org/abs/2607.25451v1)
  <details><summary>📄 Abstract</summary>
  Language models are almost always quantized before they are deployed, and a growing line of work asks whether quantization also lowers their privacy risk. That work measures privacy almost entirely with membership inference. We think this is the wrong thing to measure for the risk that most people actually worry about, namely a model reproducing its training data word for word, and we measure that directly. Using the Pythia models and the public set of sequences each of them is known to have mem...
  </details>

- **2026-07-28** — Mohamed Nabih Ali, Daniele Falavigna, Alessio Brutti — [SpeechLLM Meets Federated Learning for End-to-End ASR: English and Italian Case Studies](http://arxiv.org/abs/2607.25716v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables privacy-preserving training of automatic speech recognition (ASR) systems across distributed data sources, yet its application to large-scale speech language models (SpeechLLMs) remains unexplored. This paper presents the first systematic study of federated training for SpeechLLM-based end-to-end ASR systems. We design a communication-efficient federated optimization strategy tailored to the unique challenges of SpeechLLM architectures, addressing high-dimensional...
  </details>

- **2026-07-28** — Yuwen Ma, Sarah Spurgeon, Tao Li et al. — [To What Extent Can Inherent Communication Noise Guarantee Privacy in Distributed Cooperative Control?](http://arxiv.org/abs/2607.25564v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a differentially private distributed cooperative control scheme for multi-agent systems (MAS). Unlike conventional approaches that actively inject artificial noise for privacy protection, this work investigates whether inherent communication noise can itself serve as a natural privacy mechanism. A physically motivated communication-noise model is developed for mobile MAS by incorporating transmitter perturbation, receiver noise, path-loss attenuation, and log-normal shadowing...
  </details>

- **2026-07-28** — Wanxu Cai, Zhengyu Chen, Huaisheng Zhu et al. — [Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis](http://arxiv.org/abs/2607.25554v1)
  <details><summary>📄 Abstract</summary>
  Future event prediction carries broad social impact yet remains challenging. SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed. While recent Tool-Integrated Reasoning (TIR) internalizes deep search for multi-hop retrieval of facts, forecasting further demands temporal search and reasoning over historical trends and dynamic shifts. The key obstacle is data: historical queries induce temporal leakage that degrades forecasti...
  </details>

- **2026-07-27** — Taimoor Rizwan, Sara Atito, Muhammad Awais et al. — [Diff-ID: Identity Consistent Facial Image Generation and Morphing via Diffusion Models](http://arxiv.org/abs/2607.25078v1)
  <details><summary>📄 Abstract</summary>
  Generative diffusion models have revolutionized facial image synthesis, yet robust identity preservation in high resolution outputs remains a critical challenge. This issue is especially vital for security systems, biometric authentication, and privacy sensitive applications, where any drift in identity integrity can undermine trust and functionality. We introduce Diff-ID, a diffusion based framework that enforces identity consistency while delivering photorealistic quality. Central to our appro...
  </details>

- **2026-07-27** — Steve Aschenbrenner, Marcel Heisler, Thomas Sievers et al. — [Not Forgotten: Implementation and Evaluation of a Personalized Episodic Memory for the Humanoid Robot Head Kim](http://arxiv.org/abs/2607.24190v1)
  <details><summary>📄 Abstract</summary>
  Social robots that rely on large language models for conversation are unable to retain information across sessions. This absence of memory violates social expectations, potentially preventing the formation of persistent relationships. This paper presents a lightweight episodic memory module that integrates vector-based semantic retrieval with an LLM-controlled dialog system, deployed on the humanoid robot head Kim. The module employs a hybrid scoring function combining cosine similarity with a m...
  </details>

- **2026-07-27** — Zihan Li, Feiyang Liu, Dandan Shan et al. — [OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedical Image Analysis](http://arxiv.org/abs/2607.25108v1)
  <details><summary>📄 Abstract</summary>
  Biomedical image analysis spans diverse modalities and tasks, yet real-world deployment is hindered by severe distribution shifts across scanners, protocols, and patient populations. High-performing models consequently require repeated domain-specific fine-tuning, which is a costly cycle that becomes impractical when labels are scarce or privacy constraints limit data sharing. We propose OPERA (Offline Policy-guided Expert Routing and Adaptation), a multi-agent ensemble framework that addresses ...
  </details>

- **2026-07-27** — Oluwadara Adedeji, Michael Mayowa Farayola, Jeff Brozena et al. — [A Computational Ethical Framework for Financial Digital Phenotyping for Mental Health](http://arxiv.org/abs/2607.24275v1)
  <details><summary>📄 Abstract</summary>
  Ethical governance of AI-driven systems is often expressed through high-level principles and static documentation, creating a gap between regulatory requirements and system-level verification. This challenge is particularly acute in digital phenotyping, where continuous behavioural data raises concerns around consent, privacy, and fairness. In this paper, we propose a computational ethical framework for AI-driven digital phenotyping system in which ethical requirements are formalised as deontic ...
  </details>

- **2026-07-26** — Arman Kolozyan, Tom Sorger, Alexander Hicks et al. — [ZKP Security Tools and Verification: Coverage, Effectiveness, Adoption, and Challenges](http://arxiv.org/abs/2607.23752v1)
  <details><summary>📄 Abstract</summary>
  Zero-knowledge proofs (ZKPs) have become a core technology for privacy and verifiable computing. They are used to secure blockchains that handle billions of dollars and identity applications dealing with sensitive personal data. However, ZKP systems are complex, and subtle implementation errors can completely break their guarantees, letting attackers forge money or false proofs of identity. Researchers and practitioners have therefore developed a growing set of bug detection and formal verificat...
  </details>

- **2026-07-26** — Yuhang Wang, Lingyao Li, Hao Zhou — [DriveDNA: A Large-Scale Multimodal Naturalistic Driving Dataset and Benchmark for Driving Style Identification](http://arxiv.org/abs/2607.23822v1)
  <details><summary>📄 Abstract</summary>
  Driving style captures stable, driver-specific patterns in how a vehicle is driven. In naturalistic data, however, this signal is hard to isolate because drivers are observed in different vehicles, on different roads, and under different conditions, so models may mistake vehicle- or situation-specific regularities for driver-specific style. We introduce DriveDNA, a large-scale naturalistic dataset and benchmark for personalized driving-style modeling, comprising 4,121 drives from 465 drivers acr...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-07-29** — Xin Xu, Chengrui Wu, Jiayu Lu et al. — [Collusion with Competitive Marginals: Price-Level Audits Are Blind by Construction](http://arxiv.org/abs/2607.26385v1)
  <details><summary>📄 Abstract</summary>
  Empirical work on algorithmic collusion asks one question of the data: are prices supracompetitive? We show this can be answered "no" by a conspiracy that is nonetheless profitable. Consider bidding agents that couple only through the joint distribution of their unexplained bid components, leaving every agent's own bid law exactly at the competitive law. Any test whose input is a single agent's price or bid history then has power exactly equal to its false-positive rate, for every coupling stren...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-07-29** — Balfroid Martin, Albert Julien, Aliti Dzenatan et al. — [How Developers Experience Debugging Unfamiliar Codebases with Code Tours Generated and Evaluated by Local LLMs](http://arxiv.org/abs/2607.26987v1)
  <details><summary>📄 Abstract</summary>
  Code tours are interactive, onboarding documentation to guide developers through a codebase. Large Language Models (LLMs) can automatically synthesize code tours. Prior work on code tour generation has not studied developer experience or trust calibration when debugging unfamiliar codebases with code tours generated and evaluated by open-weight LLMs. This study surveys how the properties of components in open-weight LLM-authored code tours influence developers' experiences when debugging unfamil...
  </details>

- **2026-07-29** — Shi Lin, Chenpei Wang, Peng Qian et al. — [Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems](http://arxiv.org/abs/2607.26836v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) have exhibited remarkable capabilities in collaborative reasoning and decision-making, yet their interconnected communications introduce new systemic risk: localized hallucinations can propagate along agent communication chain, amplify through interactions, and ultimately trigger cascading failures. Existing countermeasures predominantly follow a post-hoc paradigm, identifying failures only after unsafe behaviors emerge, by which time harmful effects may have ...
  </details>

- **2026-07-29** — Kyungwon Park — [When Does Span-Guided Detoxification Help? Human Preferences and Evaluator Diagnostics in a Controlled Comparison](http://arxiv.org/abs/2607.26795v1)
  <details><summary>📄 Abstract</summary>
  Span-guided rewriting aims to preserve meaning by localizing edits to annotated harmful spans, but the same constraint can leave harmful intent insufficiently mitigated. We present a controlled exploratory comparison of span-guided and unguided detoxification on a mixed-source English evaluation set comprising manually curated inputs and HateXplain test items. We conduct a dense blinded human evaluation under a fixed single-generator setting.   Human preferences reveal a trade-off rather than a ...
  </details>

- **2026-07-28** — Mengya Hu, Susie Park, Suzana Ilic et al. — [Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting](http://arxiv.org/abs/2607.26200v1)
  <details><summary>📄 Abstract</summary>
  Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag. We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. Latency and error rates are diagnostics. We compare Input only, Response only, and Input + response hard b...
  </details>

- **2026-07-28** — Yunhao Liang, Chengguang Gan, Ruixuan Ying et al. — [Do Code Language Models Use Tests? A Behavioral and Representational Study of Test-Driven Code Generation](http://arxiv.org/abs/2607.26244v1)
  <details><summary>📄 Abstract</summary>
  Public tests are widely used to guide large language model code generation, but whether models treat them as executable specifications or merely as extra prompt context remains unclear. We study test-driven code generation on HumanEval+, MBPP+, and recent LiveCodeBench tasks using Qwen2.5-Coder-7B and Qwen3.6-27B. We compare natural-language-only prompts with relevant visible tests, shuffled outputs, irrelevant tests, assertion-only tests, and stronger-model-generated synthetic tests. Evaluation...
  </details>

- **2026-07-28** — Yinuo Zhu, He Liu, Boyuan Gu — [BioDisclose: An Actionability-Aware Benchmark for Biomedical Safety under Adversarial Elicitation](http://arxiv.org/abs/2607.25700v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly support biomedical research, yet their behavior under adversarial requests for dual-use knowledge remains insufficiently characterized. We introduce BioDisclose, a benchmark for measuring biomedical knowledge disclosure under adversarial elicitation. BioDisclose contains 480 prompts derived from 24 expert-authored scenarios across six biomedical risk domains and four elicitation families spanning academic, historical, role-playing, and decomposed prompti...
  </details>

- **2026-07-28** — Abu Bakar Siddik — [Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response](http://arxiv.org/abs/2607.25379v1)
  <details><summary>📄 Abstract</summary>
  Cyber-capable AI agents combine language models with tools, memory, and execution en- vironments to perform multi-step offensive-security tasks. Existing work separately measures cyber capability and catalogs attacks against agent components, but provides less guidance on containing a capable agent within the environments used to evaluate it. This review synthe- sizes five vulnerability classes at that boundary: multi-step offensive chains, objectives that conflict with sandbox boundaries, suppl...
  </details>

- **2026-07-28** — Yongyi Cui, Yue Li, Tianbao Jiang et al. — [Construction-Driven Injection: Linguistically-Grounded Edit-Based Code-Mixing Fingerprints for Large Language Models](http://arxiv.org/abs/2607.25633v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are costly intellectual assets that remain exposed to unauthorized redistribution and commercial misuse. Injected fingerprints, i.e., trigger--target pairs embedded in model behavior, offer a practical, black-box-verifiable ownership signal, but existing methods decouple the two stages of the fingerprint life cycle: how a fingerprint is constructed and how it is injected. Existing fingerprinting frameworks suffer from two limitations. Natural-language fingerprints ar...
  </details>

- **2026-07-28** — Ping He, Yuexiang Xie, Yaliang Li et al. — [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](http://arxiv.org/abs/2607.25297v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks. To standardize interactions between LLM agents and external environments, Model Context Protocol (MCP) tools have emerged as a de facto standard and have been widely integrated into these systems. However, the use of MCP tools also introduces new safety risks, as LLM agents can be induced to perform malicious or unauthorized actions. Although prior work has proposed defens...
  </details>

- **2026-07-28** — David Demitri Africa, Cate Heine, Nadine Staes-Polet et al. — [Detecting CSAM Text-to-Image LoRAs From Weights](http://arxiv.org/abs/2607.25750v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM). Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and generating outputs may itself be unacceptable or illegal. We show that a safer signal lives in the weights. The top-left singular vectors of a LoRA's updates form a compact, inference-free fingerprint ($u_1...
  </details>

- **2026-07-28** — Rodolfo Rizzi, Alessandro Grecucci, Massimo Stella — [MyMentorLLM: A psychotherapy GenAI environment with multimodal voice/text patients, trainees and experts for deliberate practice](http://arxiv.org/abs/2607.25667v1)
  <details><summary>📄 Abstract</summary>
  Psychotherapists need repeated training and supervision by experts; however, scalability is problematic. Here we present MyMentorLLM, a multimodal voice- and text-based simulation environment for deliberate practice, used to generate 2,100 complete Cognitive Behavioural Therapy (CBT) training sessions. Each session links a DSM-5-TR-grounded patient (with major depressive, generalised anxiety or borderline personality disorder), a therapist-in-training and an expert supervisor. As an initial impl...
  </details>

- **2026-07-28** — Frank Yingjie Huo, Neil F. Johnson — [Many-body Tipping Dynamics of ChatGPT-like AIs](http://arxiv.org/abs/2607.25279v1)
  <details><summary>📄 Abstract</summary>
  Why do ChatGPT-like AIs, despite major architectural and training differences, unexpectedly tip to undesirable content (e.g. harmful, misleading, repetitive) even under deterministic greedy decoding? We show that a broad class of such tippings is caused by the many-body interactions between tokens (spins) as they cross the finite-layer system. Tipping emerges as a dynamical first passage process between competing output basins. Attention disorder controls the transport toward, away from, or alon...
  </details>

- **2026-07-28** — Benjamin Cookson, Soroush Ebadian, Dominik Peters et al. — [Proportional Fairness for Harmful Decisions](http://arxiv.org/abs/2607.26053v1)
  <details><summary>📄 Abstract</summary>
  We study allocation of (divisible) public bads, where agents incur costs for alternatives and the goal is to pick a lottery over the alternatives. We show that the traditional definitions of the core, a central criterion of proportional representation for allocation of public goods, private goods, and private bads (chores), do not make sense for allocation of public bads.   We introduce two formalizations of the core tailored to public bads. Under a structural condition which subsumes allocation...
  </details>

- **2026-07-27** — Cen Lu, Yung-Chen Tang, Andrea Cavallaro — [Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT](http://arxiv.org/abs/2607.25063v1)
  <details><summary>📄 Abstract</summary>
  Developers judge a model checkpoint by how it behaves. After supervised fine-tuning (SFT), two checkpoints that perform about the same across relevant benchmarks are treated as interchangeable, equally ready for the next alignment stage, typically preference optimization. We ask whether this judgment misses a pretraining imprint: a difference that no post-SFT benchmark reveals, yet that decides how each checkpoint responds to further training. To find out, we run a controlled experiment on the f...
  </details>

- **2026-07-27** — Xinnuo Xu, Anja Thieme, Daniela Massiceti et al. — [Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed](http://arxiv.org/abs/2607.24898v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art toxicity detectors for text-to-image generation adopt a one-size-fits-all approach: a single universal model applying fixed safety guidelines to all users. Our empirical evidence shows that these detectors fail to shield marginalized communities: approximately 35% of generated images labeled safe are considered harmful by disability communities. In this position paper, we argue for community-specific toxicity detection (CTD). To demonstrate its feasibility, we collaborate with d...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-07-28** — Ads Dawson, Adrian Wood — [StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents](http://arxiv.org/abs/2607.26314v1)
  <details><summary>📄 Abstract</summary>
  Stealth, the discipline of achieving an objective without revealing your presence, capabilities, or collected intelligence, is what separates sophisticated operators from detectable ones. Elite security researchers and advanced persistent threats achieve their objectives unnoticed; autonomous agents increasingly inherit the same offensive tasks, but do they inherit the tradecraft? We introduce StealthBench,a benchmark that measures operational stealth in autonomous offensive-security agents acro...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 45 papers

- **2026-07-29** — Philippe Baumstimler, Jean-Mathieu Gagnon, Sébastien Gagné et al. — [Step-Attention Refinement of DINOv3 Features for Efficient Anterior Eye Segmentation](http://arxiv.org/abs/2607.27087v1)
  <details><summary>📄 Abstract</summary>
  Anterior eye segment (AES) segmentation is a key component of both ocular biometrics and emerging clinical image analysis applications. However, heterogeneous acquisition conditions and limited annotations in medical settings hinder the robustness and generalization of existing methods. Foundation models (FMs) such as DINOv3 offer strong transfer capabilities, but efficiently adapting their representations to dense prediction tasks remains challenging. In this study, we investigate robust AES se...
  </details>

- **2026-07-29** — Petr Simecek, Elnaz Babayeva, Jiri Balhar et al. — [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](http://arxiv.org/abs/2607.27030v1)
  <details><summary>📄 Abstract</summary>
  LLM-based analyzers have begun finding real vulnerabilities in mature open-source projects: AISLE's analyzer is credited with more than 280 CVEs across 78 projects, including OpenSSL, curl, and GnuTLS. We introduce HoF-Bench (named after AISLE's public Hall of Fame), a benchmark built from 95 of these public AI-discovered CVEs across eight repositories pinned at vulnerable commits. Analyzers receive source and target-file scope but not CVE identifiers, descriptions, fixes, or expected mechanisms...
  </details>

- **2026-07-29** — Ruoyu Wang, Heng Zhao, Renjie Wu et al. — [AgentSnare: Learning to Delay, Divert, and Defuse Autonomous Penetration Agents](http://arxiv.org/abs/2607.26998v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents automate penetration testing through an observation-action loop, selecting actions based on observations returned by tools. This dependence allows defenders to inject deceptive observations that can mislead the agent's decision-making process. However, existing defenses rely heavily on static, isolated artifacts planted in the environment prior to an attack. Advanced agents can progressively recognize and bypass these artifacts, ultimately refocusing their explo...
  </details>

- **2026-07-29** — Lehan Wang, Boli Chen, Ruixue Ding et al. — [SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response](http://arxiv.org/abs/2607.26791v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents are increasingly adopted in real-world security operations with access to host artifacts and command-line interfaces (CLIs), making it critical to thoroughly assess their security capabilities. However, existing cybersecurity benchmarks focus on pre-compromise settings where agents are placed in a clean and idealized environment before an attack occurs. This leaves the post-compromise setting underexplored. To address this gap, we introduce SecRespond, the first...
  </details>

- **2026-07-29** — Weijie Feng, Tongwei Zhang, Binbin Liu et al. — [AtmosERC: Modeling Dialogue-Level Affective Atmosphere for Emotion Recognition in Conversation](http://arxiv.org/abs/2607.26726v1)
  <details><summary>📄 Abstract</summary>
  Emotion Recognition in Conversation (ERC) aims to predict utterance-level emotions in dialogues and has largely advanced through context-centric modeling. However, global context is a heterogeneous signal, and not all contextual information is equally relevant to emotion prediction. This paper focuses on the affect-oriented component of this signal, termed dialogue-level affective atmosphere, which captures a latent tendency commonly reflected in conversational emotion patterns. To estimate and ...
  </details>

- **2026-07-29** — Hongqiang Lin, Chao Liu, Xiaofan Bai et al. — [Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting](http://arxiv.org/abs/2607.26643v1)
  <details><summary>📄 Abstract</summary>
  Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world applications. A promising solution is to treat skills as trainable states and optimize them in the same way as model parameters in neural network training. However, data-driven skill optimization is prone to overfitting to the limited trajectories collected from real environments. Overexploiting these trajectories overfits the current batch, while unconst...
  </details>

- **2026-07-29** — Jingyang Yi, Jian Yang, Yifei Jin et al. — [AlphaSchema: Exploring the Space of Trading Semantics for LLM-Based Alpha Mining](http://arxiv.org/abs/2607.26642v1)
  <details><summary>📄 Abstract</summary>
  Automated alpha mining has increasingly adopted large language model (LLM) agents for factor generation and iterative discovery. However, existing LLM-based systems often delegate both factor construction and search decisions to the agent itself, without an explicit exploration space or a principled mechanism for navigating that space. As a result, exploration remains largely implicit and difficult to control or optimize systematically. We introduce AlphaSchema, which constructs and explores a s...
  </details>

- **2026-07-29** — Haichuan Hu, Chunrong Fang, Ye Shang et al. — [MultiFixer: A Coordinator-Proposer Based Multi-Agent Framework For Fixing Multi-Hunk Bugs](http://arxiv.org/abs/2607.26591v1)
  <details><summary>📄 Abstract</summary>
  Automated Program Repair (APR) has benefited greatly from Large Language Models (LLMs), but existing LLM-based APR methods still struggle with multi-hunk bugs that require coordinated changes across multiple locations. These bugs demand repository-level context understanding, repair-order scheduling, and effective hunk-level patch generation and selection. To address these challenges, we propose MultiFixer, a novel Coordinator-Proposer based multi-agent framework for multi-hunk repair. MultiFixe...
  </details>

- **2026-07-29** — Tiancheng Hu, Jin Qin, Yuzheng Wang et al. — [StrataCL: Fabric-Native Communication Library for Production Supernodes](http://arxiv.org/abs/2607.26444v1)
  <details><summary>📄 Abstract</summary>
  Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck. Existing communication libraries remain largely buffer-centric because user and communication buffers are managed separately, causing redundant data copies or costly user-buffer registration. This paper presents StrataCL, a zero-redundancy and fabric-native communication library for production supernodes. StrataCL introduces registration-on-allocation to realize user-buffer direct commun...
  </details>

- **2026-07-29** — Velimir Todorovski, Kwang Hak Kim, Alessandro Astolfi et al. — [Global Exponential Stabilization of the Kinematic Bicycle Model of a Car in Polar Coordinates](http://arxiv.org/abs/2607.26442v1)
  <details><summary>📄 Abstract</summary>
  At parking speeds, the kinematic bicycle is the prevailing model for car-like vehicles. Yet, despite its wide use, stabilizing feedback laws for this system are scarce in the literature, and existing designs often do not reproduce realistic parking maneuvers. This limitation is inherent to the Cartesian coordinates, where Brockett's condition rules out smooth static feedback stabilization. We bypass this obstruction by transforming the system into polar coordinates together with additional range...
  </details>

- **2026-07-28** — Zhiyi Mou, Wangze Ni, Tianfang Xiao et al. — [From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs](http://arxiv.org/abs/2607.25936v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly deployed in real-world applications, making inference efficiency and service reliability critical concerns due to their substantial computational costs. However, the autoregressive generation mechanism of LLMs enables malicious prompts to manipulate generation behaviors, inducing excessive token generation that amplifies computational consumption and threatens service efficiency. Existing methods mainly rely on adversarial suffixes or explicit extension instructions, which ...
  </details>

- **2026-07-28** — Pau Baguer, J. Xavier Salvat Lozano, Gines Garcia-Aviles et al. — [C-RE-ACT: Causal RE-ACTing Agent for O-RAN Forensic Triage](http://arxiv.org/abs/2607.25828v1)
  <details><summary>📄 Abstract</summary>
  The shift to O-RAN architectures marks a turning point in cellular security, where increased openness and modularity directly translate into a broader attack surface. Among the security threats cataloged by the O-RAN Alliance Working Group 11, performance-degradation attacks constitute the largest class. These attacks induce packet losses and latency spikes that are hard to distinguish from operational events such as misconfigurations, transient congestion, or software regressions. Consequently,...
  </details>

- **2026-07-28** — Yu Su, Nabil Aouf — [Cooperative Multi-UAV Navigation in Complex Environments via Systematic Multi-Agent Deep Reinforcement Learning](http://arxiv.org/abs/2607.25754v1)
  <details><summary>📄 Abstract</summary>
  Cooperative navigation of multi-agent UAVs in complex environments faces key challenges including local optima traps, sparse rewards, learning imbalance among agents, and insufficient cross-scenario generalisation. This paper proposes a multi-agent deep reinforcement learning framework that addresses these issues through coordinated exploration, demonstration exploitation, safe curriculum scheduling, and structure-aware generalisation. First, a perception mechanism combining memory of visited st...
  </details>

- **2026-07-28** — Xinran Liu, Shengtao Li, Shouqian Shi et al. — [IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment](http://arxiv.org/abs/2607.25579v1)
  <details><summary>📄 Abstract</summary>
  Entity alignment (EA) identifies entities across knowledge graphs (KGs) that refer to the same real-world object. Conventional EA methods mainly exploit explicit graph structures and textual fields, which often provide insufficient semantic understanding to recognize the same entity under heterogeneous descriptions and distinguish it from semantically similar entities. Although large language models (LLMs) offer deeper entity understanding, existing LLM-based EA methods largely use this capabili...
  </details>

- **2026-07-28** — Cédric Bonhomme, Alexandre Dulaunoy — [Mapping CVEs to MITRE ATT&CK Techniques: A Curated Gold-Set Classifier and the Limits of LLM-Assisted Label Expansion](http://arxiv.org/abs/2607.25572v1)
  <details><summary>📄 Abstract</summary>
  We present a reproducible pipeline for mapping Common Vulnerabilities and Exposures (CVEs) to MITRE ATT&CK Enterprise techniques from free-text vulnerability descriptions. Rather than relying on the CWE->CAPEC->ATT&CK derivation chain, whose table-expansion artifacts we quantify, we train a multi-label classifier on a curated gold dataset of 1,207 CVEs from expert MITRE Center for Threat-Informed Defense mappings. The resulting model approximately doubles recall@5 compared with a zero-shot embed...
  </details>

- **2026-07-28** — Bowen Wang, Chi Zhang, Diyou Shen et al. — [At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference](http://arxiv.org/abs/2607.25504v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained weight pruning and activation sparsification have emerged as effective approaches for reducing the compute and memory cost of inference for Transformer models. In the moderate-sparsity regime, Gustavson's dataflow provides a natural execution model for exploiting both activation and weight sparsity on vector processors through metadata-driven indexed accumulation. However, existing RVV architectures lack native support for this pattern, forcing kernels to rely on software index deco...
  </details>

- **2026-07-28** — Clément Grisi, Jeroen van der Laak, Geert Litjens — [Beyond Counts: A Distributional Robustness Margin For Pathology Foundation Models](http://arxiv.org/abs/2607.25497v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models are approaching clinical deployment, yet remain vulnerable to systematic non-biological variation across centres. Differences in tissue preparation, staining and scanning are strongly encoded in their representations, enabling shortcut learning and weakening generalisation across cohorts and institutions. The Robustness Index (RI) quantifies whether local representation geometry is dominated by biology or by non-biological variation, but its count-based formulation di...
  </details>

- **2026-07-28** — Michael Macaulay, Harmony Bouabid, Guo Gen Ang et al. — [The Disruptive Impact of Large Language Models on Capture the Flag Competitions and the Path Toward Fair Play](http://arxiv.org/abs/2607.25425v1)
  <details><summary>📄 Abstract</summary>
  Capture the Flag (CTF) competitions are among cybersecurity's most effective training grounds, developing practical skill across cryptography, web exploitation, and binary exploitation. Large language models (LLMs) can now solve a growing share of challenges with minimal human input, raising urgent questions about fairness, the validity of rankings, and whether participation still delivers the learning that justifies the effort. This paper reports a mixed-methods study of LLM impact on modern CT...
  </details>

- **2026-07-28** — Chengxin Xie, Qiya Song, Yangbangyan Jiang et al. — [Dual-Domain Manifold Modeling for Hyperspectral Image Fusion](http://arxiv.org/abs/2607.25338v1)
  <details><summary>📄 Abstract</summary>
  Achieving a coherent integration of spectral richness and spatial fidelity remains a central objective in hyperspectral image fusion. However, existing hyperspectral image fusion methods struggle to effectively model geometric constraints. In the spatial domain, weak spatial-spectral interaction limits geometry-aware feature learning and suppresses high-frequency structural information, resulting in low-frequency bias and structural degradation. In the spectral domain, local manifold structures ...
  </details>

- **2026-07-28** — Chaemin Jang, Dongman Lee, Jihee Kim — [Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe](http://arxiv.org/abs/2607.25292v1)
  <details><summary>📄 Abstract</summary>
  Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution. We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output. The same persona on the same question returns the same answer on more than half of items in a public-opinion benchmark. The collapse is sharp: the model's internal probabilities concentrate on a single op...
  </details>

- **2026-07-28** — Zhenning Shi, Chen Xu, Junhao Zhang et al. — [ScaleResfusion: Residual Rectified Flow based on Residual Vector Field](http://arxiv.org/abs/2607.25275v1)
  <details><summary>📄 Abstract</summary>
  Real-world Image Restoration (Real-IR) aims to recover high-quality (HQ) images from complex and unknown degradations. Although recent diffusion-based methods have substantially improved perceptual quality, their current designs leave two key challenges unresolved. Methods that start from Gaussian noise are slow and often less faithful to the degraded input. Residual-based methods usually train from scratch, which makes it hard to exploit modern pre-trained generative priors. In this paper, we p...
  </details>

- **2026-07-28** — Mengqi Wang, Jianwei Wang, Qing Liu et al. — [Interpretable Column Annotation with LLM-Symbolized Decision Process Materialization](http://arxiv.org/abs/2607.25228v1)
  <details><summary>📄 Abstract</summary>
  Column annotation (CA), including column type annotation (CTA) and column property annotation (CPA), aims to identify the meanings of table columns and the semantic relationships among them. Recent CA methods usually use various neural models to learn column representations and directly map them to label categories, thereby (1) sacrificing model interpretability and adaptivity, and (2) overlooking rich label semantics and ultimately limiting accuracy. To address these limitations, we propose Sym...
  </details>

- **2026-07-28** — Narayanaswami Natraj Bharadwaj, Dhivya Chandramouleeswaran — [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](http://arxiv.org/abs/2607.25225v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used for code generation in critical infrastructure, yet the security effect of domain-specific prompting is understudied. We present SecDrift, a benchmark measuring sector-conditioned security drift: the change in static-analysis vulnerability rates when prompts are conditioned on industry contexts versus neutral baselines. We evaluate 7 LLMs (6 producing analyzable code) across 8 CISA critical infrastructure sectors and 9 CWE categories with 5 replicates (5,355 evaluation...
  </details>

- **2026-07-28** — Zheshun Wu, Renjie Zheng, Jinhang Zuo et al. — [A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics](http://arxiv.org/abs/2607.25207v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a hybrid reinforcement learning setting in tabular Markov Decision Processes (MDPs), where an agent aims to learn an optimal policy by combining online interactions with a target environment and offline data from a source environment. A central challenge is that offline data may be collected from outdated environments with shifted transition dynamics, making naive integration of historical data ineffective. To address this, we propose a unified algorithmic framework featu...
  </details>

- **2026-07-27** — Harrison J. Goldwyn, Graham Johnson, Christopher Ibarra et al. — [Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference](http://arxiv.org/abs/2607.25131v1)
  <details><summary>📄 Abstract</summary>
  Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors. Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments. To address this mechanistic gap, we translate a cognitive theory of visua...
  </details>

- **2026-07-27** — Zixuan Wu, Cristina Nita-Rotaru — [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](http://arxiv.org/abs/2607.24964v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed for security-sensitive tasks such as vulnerability detection and code review. Their reliance on natural-language context embedded in source code exposes a previously underexplored attack surface: adversarial comments that can influence a detector's reasoning without changing program behavior. We study LLM-based vulnerability detectors against a new adversary: a coding agent that implements new functionality, deliberately introduces vulnerabilities,...
  </details>

- **2026-07-27** — Andong Lu, Ziyi Zha, Jiandong Jin et al. — [Spatio-Temporal Conditional Denoising Transformer for Modality-Missing RGBT Tracking](http://arxiv.org/abs/2607.24701v1)
  <details><summary>📄 Abstract</summary>
  Missing modalities in RGBT tracking often lead to incomplete and unstable multimodal feature representations that greatly degrade the performance. Existing methods typically attempt to recover missing modalities from available ones, but the quality of data generated in challenging scenarios might be unsatisfactory. In addition, current approaches exhibit limited flexibility in processing both missing and complete data. To overcome these limitations, we propose a Spatio-temporal Conditional Denoi...
  </details>

- **2026-07-27** — Dael Sinay, Rica Gonen — [The Degree of Strategy-Proofness for Risk-Averse Committee Selection](http://arxiv.org/abs/2607.24676v1)
  <details><summary>📄 Abstract</summary>
  The classic notion of strategyproofness implicitly assumes that a manipulating agent either possesses complete knowledge of what all other agents are going to report, or is willing to take the risk and act as if they know these reports. To capture the profound uncertainty of real-world voters, recent work introduced \emph{risk-avoiding truthfulness (RAT)} and the \emph{RAT-degree}, which quantifies the exact number of known reports required for a manipulation to be strictly safe. While the RAT-d...
  </details>

- **2026-07-27** — Hang Ni, Weijia Zhang, Fan Liu et al. — [SIREN: Towards End-to-End Extreme-Weather Early Warning with Experience-Grounded LLM Agents](http://arxiv.org/abs/2607.24588v1)
  <details><summary>📄 Abstract</summary>
  Early warning of extreme weather is essential for mitigating the societal, economic, and environmental risks posed by hazardous weather events. However, expert-centered warning workflows are costly, labor-intensive, and difficult to scale throughout the warning-to-action process. Although recent advances in Large Language Model (LLM) agents have enabled the automation of weather-related tasks, existing studies remain centered on isolated scientific tasks and overlook the chain of interdependent ...
  </details>

- **2026-07-27** — Sofia Della Penna, Lorenzo Parracino, Luciano Pianese et al. — [VulnGym: Evaluating Vulnerability Management Strategies against Advanced Persistent Threats](http://arxiv.org/abs/2607.24552v1)
  <details><summary>📄 Abstract</summary>
  Enterprise networks are continuously targeted by Advanced Persistent Threats (APTs), attack campaigns exploiting software vulnerabilities to compromise critical assets over time. As disclosed vulnerabilities grow, resource-constrained organizations must prioritize which ones to patch. Existing prioritization standards score vulnerabilities individually and cannot capture how a patching policy performs against an adversary that progresses through the network over time. Previous tools have simulat...
  </details>

- **2026-07-27** — G{é}nesis Montenegro, Mokhtar Boumedyen Billami, Catherine Faron et al. — [LLM-Assisted Ontology Engineering and Construction of a French Legal Knowledge Graph](http://arxiv.org/abs/2607.24551v1)
  <details><summary>📄 Abstract</summary>
  Maintenance regulations are complex legal texts that are difficult to exploit when addressing a specific case and challenging to integrate into operational systems. This paper presents a two-stage LLM-assisted workflow for French maintenance regulations: ontology engineering from a SEMLEG-based core ontology, followed by construction of an ontology-grounded French legal knowledge graph. The first stage consists in the open extraction of typed entities and triples from a stratified corpus sample,...
  </details>

- **2026-07-27** — Christos Georgakilas, Aniello Panariello, Samir El Karrat Moreno et al. — [Rethinking Expert Training for Model Merging with Prompt Learning](http://arxiv.org/abs/2607.24465v1)
  <details><summary>📄 Abstract</summary>
  Model merging aims to combine multiple domain-specialized experts trained from a shared foundation model into a single multi-task model. Existing approaches largely focus on improving the merging procedure itself and typically assume experts obtained through full-parameter fine-tuning. In this work, we revisit expert training for model merging. We first show that prompt-based adaptation provides a strong baseline: independently learned prompts can be exploited across tasks while keeping the back...
  </details>

- **2026-07-27** — Qihui Zhu, Yuchen Wang, Zijian Wen et al. — [RP-OPSD: Resolution-Privileged On-Policy Self-Distillation for Multimodal Large Language Models](http://arxiv.org/abs/2607.24447v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) uses privileged information available only to the teacher to provide dense token-level supervision on trajectories generated by the student. However, existing methods often rely on verified solution traces, explanations generated by external models, or manually localized visual evidence, which limits their scalable application to multimodal large language models. To address this issue, we exploit the information gap between high- and low-resolution views of the...
  </details>

- **2026-07-27** — Diego Bolón, Davy Paindaveine — [Möbius-Invariant Goodness-of-Fit Tests for the Spherical Cauchy Model](http://arxiv.org/abs/2607.24376v1)
  <details><summary>📄 Abstract</summary>
  We introduce a class of goodness-of-fit tests for the spherical Cauchy model on the unit hypersphere. The proposed procedures exploit the invariance of the spherical Cauchy family under Möbius transformations: after estimating the parameter by the sample Möbius mean, the observations are transformed to approximate spherical uniformity, and a projection-based uniformity statistic is applied to the resulting sample. We show that, under mild conditions, the resulting tests are exactly distribution-...
  </details>

- **2026-07-27** — Vaibhav Krishna, Hirokazu Shirado, Feng Fu et al. — [Modeling Duelling Contagions of True and False Information in the Face of Inherent Individual biases](http://arxiv.org/abs/2607.24360v1)
  <details><summary>📄 Abstract</summary>
  Advanced digital communication has revolutionized how people create and consume information, making information diffusion an important topic of research for domains from public health to national security. Real-world scenarios of information diffusion often involve competing narratives - true and false - spreading simultaneously. We propose a novel agent-based co-diffusion model, grounded in "complex-contagion" and "spiral of silence" theories, to capture how network dynamics exploit cognitive b...
  </details>

- **2026-07-27** — Tan T. Nguyen, Quan V. Dang — [DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation](http://arxiv.org/abs/2607.24331v1)
  <details><summary>📄 Abstract</summary>
  As the inference phase of Large Language Models (LLMs) requires handling long context windows, the Key-Value (KV) cache initially appears to address this challenge but eventually becomes a significant bottleneck as the context window continues to grow. Low-rank compression has recently been studied as an effective approach to reduce KV cache memory while maintaining model performance. However, only a few existing methods treat the Key and Value caches differently, despite their distinct roles. M...
  </details>

- **2026-07-27** — Angelo Nardone, Paolo Ferragina — [LLM-based Source Code Compression via Thresholded Symbol Ranking](http://arxiv.org/abs/2607.24192v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of lossless compression of source code, motivated by the storage demands of large-scale software archives, such as Software Heritage (https://www.softwareheritage.org/). General-purpose compressors (e.g., zstd, bzip2) offer a good trade-off between compression ratio and speed, but fail to exploit all special regularities inherent in source code. Recent approaches leverage Large Language Models (LLMs) within Shannon's symbol-ranking framework, relying on a scheme in which the...
  </details>

- **2026-07-27** — Yang Li, Hai Liu, Dian Shao et al. — [Agent-UCT: Upper Confidence Bounds Applied to Trees for Agentic Workflow Optimization with Cost-Awareness](http://arxiv.org/abs/2607.24162v1)
  <details><summary>📄 Abstract</summary>
  Optimizing agentic workflows, such as retrieval-augmented generation (RAG) pipelines, requires navigating a combinatorial space of discrete component choices under tight evaluation budgets. Existing approaches - heuristic search, black-box optimization, and standard tree search methods - do not explicitly exploit the compositional structure of these workflows, leading to redundant computation and inefficient budget allocation. We introduce Agent-UCT (Agent-based Cost-Aware Upper Confidence Bound...
  </details>

- **2026-07-27** — Pei Liu, Nan Zheng, Lang Zhang et al. — [LeapBot-WA: World-Anchor Action Models via Predictive Latent Alignments](http://arxiv.org/abs/2607.23969v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have emerged as a powerful paradigm for embodied intelligence, yet the prevailing reliance on pixel-level video generation creates a fundamental bottleneck. Forcing models to reconstruct task-irrelevant visual details dissipates representational capacity and renders policies vulnerable to visual distractors. In this paper, we propose LeapBot-WA, which establishes a novel Predictive-Latent paradigm for WAMs by operationalizing the Joint-Embedding Predictive Architecture...
  </details>

- **2026-07-27** — Mohammed Aldeen, Muhammad Sami Irfan, Sagar Dasgupta et al. — [Development of Vision-Language Model-based GNSS Spoofing Detection for Autonomous Vehicle Navigation](http://arxiv.org/abs/2607.23962v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles (AVs) depend on Global Navigation Satellite Systems (GNSS) for localization and navigation, making them vulnerable to spoofing attacks that can covertly redirect vehicles or induce unsafe maneuvers. In this paper, we develop the first Vision-Language Model (VLM)-based framework for GNSS spoofing detection for autonomous vehicles by fusing front-camera visual data with in-vehicle sensor readings (e.g., speed, acceleration, yaw rate) against GNSS-derived maneuvers. Our approach...
  </details>

- **2026-07-27** — Jyun-Ze Tang, Po-Han Huang, Ming-Ching Chang et al. — [DuoAD: Leveraging [CLS] Dual Characteristics for Training-Free Few-Shot Anomaly Detection](http://arxiv.org/abs/2607.23924v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models have enabled strong training-free anomaly detection (AD). However, most existing approaches rely primarily on independent local patch features, leaving the global contextual information encoded by Vision Transformers (ViTs) underexploited. In this work, we identify the dual characteristics of the ViT [CLS] token: its embedding provides anomaly-invariant global semantic representation, while its attention maps implicitly highlight spatially abnormal regions. Building on t...
  </details>

- **2026-07-26** — Ge Zhang, Jingru Cheng, Huiyuan Chen — [Ranked by Position: Order Sensitivity as an Exploitable Attack Surface in LLM Listwise Recommenders](http://arxiv.org/abs/2607.24869v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) used as listwise rerankers in recommendation systems suffer from position bias when serializing candidate sets into prompts. We show this order sensitivity creates an exploitable attack surface: an attacker can promote a label-0 target into the top-$k$ solely by reordering candidates, without changing item content, labels, or model parameters. We introduce $\mathrm{promo}@k$ to quantify this vulnerability, measuring the fraction of label-0 targets that can be elevate...
  </details>

- **2026-07-26** — Zhaoyuan He, Muhammad Muaz, Lili Qiu — [OmniCache: Multidimensional Hierarchical Feature Caching For Diffusion Models](http://arxiv.org/abs/2607.23844v1)
  <details><summary>📄 Abstract</summary>
  High-resolution image and video diffusion models, including SD3, FLUX, and recent video diffusion transformers, have substantially improved generative quality but remain expensive at inference time because they repeatedly evaluate attention-heavy denoisers over many sampling steps. We address this inefficiency by exploiting redundancy in intermediate diffusion features rather than changing model weights or retraining. We identify four complementary redundancy sources in image and video generatio...
  </details>

- **2026-07-26** — Yifei Li, Zihui Gao, Laks V. S. Lakshmanan — [WISERouter: LLM Routing with Workload Budget Constraint](http://arxiv.org/abs/2607.23765v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve impressive performance across multiple domains, but using the most capable model for every query is prohibitive at scale. LLM routing exploits diversity in model capability and cost by assigning each query to a suitable model to balance utility and budget. Current methods have two limitations: (i) they either use heuristics that do not always enforce the budget constraint or impose a fixed per-query budget that cannot adapt across the workload and leads to su...
  </details>

- **2026-07-26** — Han Jiao, Chen Liu, Jiakai Sun et al. — [RoadVGGT: Road-Structure-Aware Feed-Forward Road Surface Reconstruction](http://arxiv.org/abs/2607.23758v1)
  <details><summary>📄 Abstract</summary>
  Large-scale road surface reconstruction supports high-definition mapping, autonomous-driving perception, annotation, and simulation. Existing road-specialized optimization methods can produce high-quality road representations, but they typically require per-scene training and scene-dependent coverage design around the driving trajectory, limiting scalable reconstruction over newly collected roads. To address these limitations, we introduce RoadVGGT, a road-structure-aware feed-forward framework ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 67 papers

- **2026-07-29** — Peter Lorenz, Anjith George, Sébastien Marcel — [Foundation Models for Face Presentation Attack Detection: A Unified Linear-Probing Benchmark](http://arxiv.org/abs/2607.26993v1)
  <details><summary>📄 Abstract</summary>
  Face presentation attack detection (PAD) remains challenging under cross-dataset evaluation, where domain shift degrades models trained on a single dataset. The scarcity of large-scale labeled data motivates adapting pretrained vision models rather than training task-specific architectures from scratch, raising a fundamental question: do general-purpose vision foundation models encode PAD-relevant information accessible with minimal task-specific training? To investigate, we systematically evalu...
  </details>

- **2026-07-29** — Piyush Jain, Kousik Dasgupta, Rajarshi Roy et al. — [Explainable and Resource-Efficient Spatial Reasoning in Multimodal LLMs for Decision-Critical Applications](http://arxiv.org/abs/2607.27145v1)
  <details><summary>📄 Abstract</summary>
  As Multimodal Large Language Models (MLLMs) are increasingly deployed in decision-critical pipelines such as robotics, embodied AI, and safety monitoring, the opacity of their spatial judgments limits operator trust and auditability. MLLMs demonstrate strong reasoning but often struggle with fine-grained spatial understanding and object hallucination. Prior work, ByDeWay, introduced Layered-Depth-Based Prompting (LDP), a training-free framework that mitigates hallucinations by structuring prompt...
  </details>

- **2026-07-29** — Jinhu Qi, Wentao Zhang, Siu Man Ng et al. — [TREK: A Travel Reasoning and Evaluation Kit for LLM Agents in Complex Trip Planning](http://arxiv.org/abs/2607.26977v1)
  <details><summary>📄 Abstract</summary>
  Travel planning is a demanding stress test for tool-using LLM agents: a usable itinerary is a single artifact that must be right along many axes at once - every flight, hotel, and attraction must exist and be bookable, the days must be physically traversable, the total must clear a budget, and the plan must serve a traveler whose needs are only partly stated. Existing agent benchmarks reward these properties one at a time and grade the final output with soft or LLM-judged rubrics, which cannot c...
  </details>

- **2026-07-29** — Vishisht Choudhary, Lukas Schmidt, Anne Zoë Kenntner et al. — [What Does It Take to Detect an AI Agent? Minimal Feature Sets for Behavioral Detection under Browser Automation](http://arxiv.org/abs/2607.26935v1)
  <details><summary>📄 Abstract</summary>
  Bot detectors deployed at scale treat traffic as binary: human or bot. This assumption breaks when AI agents browse the web through browser automation, a traffic class that is neither and that binary classifiers structurally cannot represent. We present a three-class detection framework distinguishing humans, bots, and AI agents, and show that the binary-vs-agent confusion is architectural: a binary human-vs-bot detector misroutes agent sessions because its label space lacks an agent class. On o...
  </details>

- **2026-07-29** — Chen Shani — [From Found to Designed: Concepts as a Design Axis for Large Language Models](http://arxiv.org/abs/2607.26825v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) encode rich concept-like information, but represent it implicitly through distributed statistical associations rather than as explicit, structured, compositional concepts. Consequently, concept-level structure is typically \emph{found} rather than \emph{designed}: it is recovered after training through probing or dictionary learning, with no architectural guarantee of stability, compositionality, controllability, or alignment with human conceptual organization. We ar...
  </details>

- **2026-07-29** — Shi Lin, Peng Qian, Dinghao Liu et al. — [Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions](http://arxiv.org/abs/2607.26820v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve from standalone assistants into autonomous agents, ensuring their safety requires shifting beyond pointwise risk assessment to understand how risks emerge and unfold over long-horizon trajectories. In multi-turn interactions, malicious intent can be decomposed across seemingly harmless turns and gradually reconstructed through interaction trajectories, eventually resulting in safety failures. Existing safeguards remain largely reactive, detecting manifested...
  </details>

- **2026-07-29** — Wenhao Yang, Runzhi He, Minghui Zhou — [A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities](http://arxiv.org/abs/2607.26819v1)
  <details><summary>📄 Abstract</summary>
  Open source communities have been flooded with AI-generated contributions. In defense, they have written contribution rules to regulate coding agents' behavior, spanning from a total ban, mandatory disclosure, to verification gates and human sign-offs. Yet, whether coding agents read and follow those rules, and behave in open source repositories, remains unknown. To estimate real-world rule compliance of coding agents, we curate 106 issues from 49 repositories containing AI contribution rules in...
  </details>

- **2026-07-29** — Sizhe Zhou, Sheldon Yu, Hui Wei et al. — [Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](http://arxiv.org/abs/2607.26637v1)
  <details><summary>📄 Abstract</summary>
  Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools. Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a growing store organized as memories accumulate, conflict, and go stale, and that this organi...
  </details>

- **2026-07-29** — Zijian Xu, Wenshuo Zhang, Zisen Qin et al. — [Fewer Clarifications, Better Code: Benchmarking Cross-Session Personalized Ambiguity Adaptation in Coding Assistants](http://arxiv.org/abs/2607.26611v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted coding increasingly translates informal user intent into executable software, yet coding requests often contain ambiguities that recur in user-specific ways across tasks and sessions. Existing disambiguation methods typically address each ambiguous request in isolation within the current coding session, often through eliciting additional clarification. However, whether resolved session history from the same user can serve as memory for resolving recurring personalized ambiguity in a ...
  </details>

- **2026-07-29** — Haoliang Ming, Feifei Li, Wenhui Que — [WikiLoop: Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback](http://arxiv.org/abs/2607.26604v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-base construction and querying are typically optimized in isolation: retrieval-augmented agents operate over a fixed, externally maintained index, whereas construction receives no signal from downstream use. We present WikiLoop, a feedback-coupled framework that jointly learns to build and navigate an agent-native Wiki, a persistent linked-page knowledge base designed for machine navigation. A role-conditioned shared policy supports two interfaces: a Navigator retrieves evidence from t...
  </details>

- **2026-07-29** — Yuxiong Xu, Kaiqing Lin, Bin Li et al. — [ThinkOmni: A Reasoning-Driven Omni-Modal LLM Framework for Audio Forgery Detection and Localization](http://arxiv.org/abs/2607.26553v1)
  <details><summary>📄 Abstract</summary>
  Existing audio forgery detection and localization (AFDL) methods often overfit dataset-specific low-level artifacts, limiting their generalization to subtle, localized, and unseen manipulations. Recent audio large language model (ALLM)-based approaches cast AFDL as question answering but still model forensic evidence implicitly, without linking manipulation cues to predictions. To bridge this gap, we propose ThinkOmni, a reasoning-driven omni-modal large language model that jointly performs expl...
  </details>

- **2026-07-29** — Hao Tan, Jun Lan, Zichang Tan et al. — [Veritas++: Value-aware On-Policy Distillation for Perception-Enhanced AIGI Detection](http://arxiv.org/abs/2607.27113v1)
  <details><summary>📄 Abstract</summary>
  The growing capability of image generation models has made synthetic images a routine presence in open media, making robust and generalizable AI-Generated Image (AIGI) detection increasingly essential. While multi-modal large language models (MLLMs) offer a transparent alternative to black-box binary scoring, we observe that current MLLM-based detectors still exhibit notable perception bottlenecks in capturing fine-grained anomalies. They primarily focus on how visual evidence is organized and s...
  </details>

- **2026-07-29** — Hua-Dong Xiong, Xinyuan Yan, Ji-An Li et al. — [Thinking Under Uncertainty: Evidence Use and Information-Seeking in Language Models](http://arxiv.org/abs/2607.26845v1)
  <details><summary>📄 Abstract</summary>
  Inference-time thinking improves the performance of large language models, but aggregate outcomes do not reveal whether models use available evidence more effectively or seek information that could improve future decisions. We distinguish these responses by measuring action preference, thinking length, and reported confidence under matched uncertainty. Ten open-weight models completed matched horizon-style two-armed bandit trials in thinking and non-thinking modes. A cognitive model separated va...
  </details>

- **2026-07-29** — Hung Nguyen, Kim Nhat Minh Nguyen, Van Duc Vu et al. — [Speech2Grasp: Data-Efficient Transfer of Text-Conditioned Grasp Detection to Speech in Humanoid Robots](http://arxiv.org/abs/2607.26567v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots increasingly require multi-modal understanding for natural interaction with humans. Despite the prominence of vision-language models, they generally assume textual rather than the more natural speech inputs. In this paper, we investigate whether a well-established text-conditioned model can be transferred to speech in a data-efficient manner. Using ALBEF as a case study, we conduct diagnostic analyses showing that a lightweight MLP-based projector effectively adapts it to speech,...
  </details>

- **2026-07-29** — Sophie Zeng, Sean Kalaycioglu, Collin Hong et al. — [Interpretable Image-Level Acne Severity Grading via EfficientNet-B0 Transfer Learning and Grad-CAM](http://arxiv.org/abs/2607.26461v1)
  <details><summary>📄 Abstract</summary>
  Acne vulgaris affects most adolescents and many adults. Accurate severity grading guides treatment, monitoring, and clinical trial endpoints, but manual assessment using the Investigator's Global Assessment or Hayashi criteria is limited by inter-rater variability and inconsistent imaging conditions. We developed a four-class acne severity classifier based on the Hayashi criteria using transfer learning with an ImageNet-pretrained EfficientNet-B0 model. The model was fine-tuned on the public ACN...
  </details>

- **2026-07-28** — Neta Kirmayer, David Tayouri, Andrés Murillo et al. — [(EC)2: Event-Centric Explainability for Cybersecurity Through Multi-Agent LLM Investigations](http://arxiv.org/abs/2607.26201v1)
  <details><summary>📄 Abstract</summary>
  Security operations centers rely on anomaly detection systems to flag suspicious events. Feature-level explanations for anomaly detectors offer limited value for operational investigations. To effectively handle alerts, analysts need to know contextual relationships and need actionable understanding of the entities involved. This paper introduces an event-centric detector-agnostic approach for explaining cybersecurity alerts in small- to medium-sized enterprise networks. We present (EC)2, a mult...
  </details>

- **2026-07-28** — Quoc-Huy Trinh, Minh-Van Nguyen, Ulas Bagci — [Rad-JEPA 3D: Radiology Joint-Embedding Predictive Model for 3D Computed Tomography](http://arxiv.org/abs/2607.26196v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining is central to 3D medical image analysis, where unlabeled CT volumes are abundant but expert annotations are scarce. Yet existing volumetric encoders often fail to preserve the coarse spatial and geometric structure that downstream reasoning depends on, limiting their performance on organ disentanglement, abnormality detection, and spatial understanding when paired with language models. We introduce Rad-JEPA 3D, a joint-embedding predictive framework that learns volume...
  </details>

- **2026-07-28** — Xinyi Hong, Pinjun Dong, Xinyang Yu et al. — [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](http://arxiv.org/abs/2607.25718v2)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET...
  </details>

- **2026-07-28** — A. N. Biswas, T. Tabassum, A. A. Shohid et al. — [Characterizing Human-Likeness in AI Generated Poetry: A Zero-shot Classification Study](http://arxiv.org/abs/2607.26221v1)
  <details><summary>📄 Abstract</summary>
  With the advancement of AI technologies, Generative AI (GenAI) and human written text have become nearly indistinguishable. Additionally, the global standardization of AI chatbots made academic malpractice more frequent. Furthermore, existing research indicates GenAI poems are the most difficult to distinguish even without any modification thus, GenAI poems are naturally deemed human-like by modern detectors. However, the objectivity of such dissertations needs to be verified against modern dete...
  </details>

- **2026-07-28** — Federica Maria Surace, Sary Bseiso, John Preskill — [State preparation and detection for quantum simulation of particle collisions](http://arxiv.org/abs/2607.26142v1)
  <details><summary>📄 Abstract</summary>
  Simulating the real-time dynamics of particle collisions is a promising application of quantum simulators, because classical methods such as tensor networks struggle to capture the highly entangled states generated in high-energy scattering. Realizing such simulations requires both the preparation of incoming wave packets and the detection of the outgoing scattering products. In this work, we propose protocols that address both challenges on programmable analog and digital quantum simulation pla...
  </details>

- **2026-07-28** — Fanfu Wei, Thibault Ehrhart, Raphaël Troncy — [Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](http://arxiv.org/abs/2607.25959v2)
  <details><summary>📄 Abstract</summary>
  Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as modality-level inconsistency detection. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity difference...
  </details>

- **2026-07-28** — Adeela Bashir, Zia Ush Shamszaman, Zhao Song et al. — [Network Reciprocity Shapes Evolutionary Cybersecurity Dynamics](http://arxiv.org/abs/2607.25568v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted cybersecurity systems are characterised by continuous adaptation between attackers and defenders, making evolutionary game theory a natural framework for studying their long-term behaviour. However, existing evolutionary cybersecurity models have primarily focused on homogeneous interactions, providing limited understanding of how population structure influences cyber attack-defence dynamics. In this paper, we develop a mixed-role evolutionary game in which adaptive cyber agents can ...
  </details>

- **2026-07-28** — Parmida Geranmayeh, Onur Günlü — [Bayesian-Guided Cooperative RL Beamforming for Wireless Adversarial User Detection](http://arxiv.org/abs/2607.25417v1)
  <details><summary>📄 Abstract</summary>
  In next-generation wireless networks, communication systems are expected to go beyond simple data transmission and simultaneously provide high data rates, efficiency, and security. This requirement has motivated the extensive adoption of machine learning methods to develop intelligent and real-time network management frameworks, enabling the system to continuously monitor and react to channel variations and user behavior while maintaining efficient information delivery. In this context, the inte...
  </details>

- **2026-07-28** — Farooq Shaikh — [Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?](http://arxiv.org/abs/2607.25995v1)
  <details><summary>📄 Abstract</summary>
  Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads. Recent work suggests that large language models (LLMs) can automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings without human authoring. Such systems, however, prompt the model with each finding in isolation from the live service call graph, assuming general hardening knowledge suffices. This assumption breaks down whenever a p...
  </details>

- **2026-07-28** — Ravi Kant Sharma, Ashutosh Uttam, Ajay Kumar — [Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](http://arxiv.org/abs/2607.25914v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management. The model comprises: a formally def...
  </details>

- **2026-07-28** — William Robert Gore — [Distributing Security Controls Through Harness Engineering](http://arxiv.org/abs/2607.25890v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. This paper investigates whether off-the-shelf security controls can be implemented on commercial AI coding agents and scaled to a distrib...
  </details>

- **2026-07-28** — Fanqing Meng, Lingxiao Du, Qiguang Chen et al. — [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](http://arxiv.org/abs/2607.25886v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement requires turning evidence of model failures into better models. Data-centric post-training research entails diagnosing capability gaps, designing and validating training-data strategies, and learning from checkpoint feedback. Can LLM agents automate this loop? Existing benchmarks entangle research decisions with optimization, serving, evaluation, and systems implementation, obscuring agents' research capability. We introduce RSIBench-Data, a controlled benchmark of LLM...
  </details>

- **2026-07-28** — Jui-Feng Chi, Wei-Ta Chu, Sheng-Long Lin — [Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion](http://arxiv.org/abs/2607.25820v1)
  <details><summary>📄 Abstract</summary>
  Food image segmentation plays a vital role in health-related applications such as nutrition tracking and personalized health monitoring. However, existing models often underperform on visually similar ingredients and rare food categories. To address this issue, we propose two plug-and-play multimodal modules that enhance the segmentation performance by leveraging ingredient labels inferred from food images using large language models (LLMs). The first module, called LIM-F (Language Injection Mod...
  </details>

- **2026-07-28** — Luqi Gong, Rui Xu, Yue Chen et al. — [Freq-RemoteVAR: Next-Frequency Autoregressive Modeling for Remote Sensing Change Detection](http://arxiv.org/abs/2607.25815v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing change detection aims to identify land-cover changes from bi-temporal images. Most existing methods follow a one-shot dense prediction paradigm, directly regressing a change mask from fused features. However, such approaches overlook the intrinsic frequency characteristics of change patterns. We propose Freq-RemoteVAR, a frequency autoregressive framework that reformulates change detection as a structured generation problem in the frequency domain. Instead of predicting the change...
  </details>

- **2026-07-28** — Ziqian Liu, Minghao Li, Yiming Qiu — [The Model in the Middle: Toward AI-Native Real-Time Communication](http://arxiv.org/abs/2607.25792v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex omni models are transforming human--AI interaction from turn-based exchanges into continuous multimodal conversations in which speaking, listening, and reasoning unfold concurrently. Rather than viewing the model as a replacement for a human endpoint, we argue for a new perspective: the model is a stateful computational middlebox inside a human-centered feedback loop, with network transport, model serving, and user playback jointly shaping how the interaction evolves. This perspectiv...
  </details>

- **2026-07-28** — Tresor Y. Koffi, Youssef Mourchid, Yohan Dupuis — [FLASH: Efficient Impact Fall Detection with Unified Hypergraph State-Space Model](http://arxiv.org/abs/2607.25791v1)
  <details><summary>📄 Abstract</summary>
  Falls represent a critical public health challenge, and accurate detection of the impact moment when an individual hits the ground is crucial for timely intervention. Existing skeleton-based methods rely on graph neural networks modeling only pairwise joint connections, failing to capture multi-joint coordination characteristic of fall impacts, while transformer-based temporal models suffer from quadratic complexity limiting real-time deployment. We propose FLASH, a novel framework integrating s...
  </details>

- **2026-07-28** — Xinyi Hong, Pinjun Dong, Xinyang Yu et al. — [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](http://arxiv.org/abs/2607.25718v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET...
  </details>

- **2026-07-28** — Zhenzhen Ren, Jiyan He, Xinpeng Zhang et al. — [OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](http://arxiv.org/abs/2607.25656v1)
  <details><summary>📄 Abstract</summary>
  Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based b...
  </details>

- **2026-07-28** — Shiyu Lei, Ke-Xin Ren, Daiyi Jiang et al. — ["Dragon Slayer Becomes the Dragon": How Players Perceive and Respond to Inequality in the Game World of Whiteout Survival](http://arxiv.org/abs/2607.25574v1)
  <details><summary>📄 Abstract</summary>
  Inequality in real-world societies are associated with psychological distress and behavioral consequences. However, less is known about whether similar dynamics emerge when inequality exists within virtual environments or make-belief worlds. As online games increasingly constitute meaningful social spaces, it becomes critical to examine how players perceive and react to structural and resource differences online to optimize their experiences. This study studies perceptions of inequality in the o...
  </details>

- **2026-07-28** — Swarnadip Chatterjee, Ssharvien Kumar Sivakumar, Anirban Mukhopadhyay — [Group Equivariant Diffusion for Anomaly Detection in Computational Cytology](http://arxiv.org/abs/2607.25503v1)
  <details><summary>📄 Abstract</summary>
  Computational cytology on whole-slide images is challenging because malignant cells are rare, heterogeneous, and annotated slides are scarce. Anomaly detection frameworks can be trained on normal slide-negative patches and then applied at test time to flag abnormal patches in held-out slides. Most unsupervised anomaly detection approaches including generative ones (GAN-based and diffusion-based), are tuned to organ-level imaging and require large curated datasets. In cytology the signal is cell-...
  </details>

- **2026-07-28** — Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou et al. — [PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents](http://arxiv.org/abs/2607.25485v1)
  <details><summary>📄 Abstract</summary>
  Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation mode...
  </details>

- **2026-07-28** — Jirong Zhuang — [How Likely and How Deep? Sharp Joint Bounds on Risk-Neutral Crash Probability and Conditional Depth from Option Bid-Ask Quotes](http://arxiv.org/abs/2607.25353v1)
  <details><summary>📄 Abstract</summary>
  A finite panel of option quotes with bid-ask spreads generally does not point-identify either the risk-neutral probability of breaching a specified threshold or the expected shortfall below that threshold conditional on a breach. Sharp marginal bounds characterize each quantity in isolation but not their jointly attainable combinations: values within the two marginal intervals may require different risk-neutral distributions, so pairing them can produce a tail scenario inconsistent with the opti...
  </details>

- **2026-07-28** — Lennart Trumpler, Rodrigo Furlan de Assis, Elias Ribeiro da Silva et al. — [Agentic AI Autonomy Assessment: A Decision-Support Framework Towards Governed Supply Chain Systems](http://arxiv.org/abs/2607.25405v1)
  <details><summary>📄 Abstract</summary>
  Supply chain decision-making is rapidly transforming with the rise of agentic AI - highly autonomous systems that can operate on complex, long-horizon tasks. Yet the adoption of agentic systems outpaces their governance: existing taxonomies of autonomy only offer discrete classifications, rely on subjective judgement, and cannot track autonomy across a system's life cycle, leaving enterprises unable to assess the risks of increasingly autonomous supply chain agents. This paper proposes the Agent...
  </details>

- **2026-07-28** — Can Wang, Yuhao Wang, Yushe Cao et al. — [LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake Detection](http://arxiv.org/abs/2607.25962v1)
  <details><summary>📄 Abstract</summary>
  Recent generative models can produce images with few obvious visual artifacts, weakening detectors and explanations that rely only on surface appearance. We present LaP-Forensics, a multimodal framework that augments RGB semantics with reconstruction-based forensic evidence. A frozen Stable Diffusion DDIM inversion-reconstruction model provides a fixed reconstruction reference, and its residual map measures local compatibility with that reference. Independent projectors encode the RGB image and ...
  </details>

- **2026-07-28** — Fanfu Wei, Thibault Ehrhart, Raphaël Troncy — [Detecting Knowledge Inconsistencies Across Text, Tables, and Knowledge Graphs](http://arxiv.org/abs/2607.25959v1)
  <details><summary>📄 Abstract</summary>
  Wikipedia and Wikidata are widely used for information access, LLM pre-training, and retrieval-augmented generation. Their knowledge is deeply connected but scattered across text, tables, and knowledge graphs. This raises a practical question: when these modalities disagree, how can we detect and explain the conflict? We study this problem as \emph{modality-level inconsistency detection}. We first introduce a taxonomy of cross-modal knowledge inconsistencies, covering information granularity dif...
  </details>

- **2026-07-28** — Carlos Celemin, Benedict Wilkins, Adrián Barahona-Ríos et al. — [Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA](http://arxiv.org/abs/2607.25921v1)
  <details><summary>📄 Abstract</summary>
  In this work, we study the use of Vision-Language Models (VLMs) for anomaly detection in an agent-driven game Quality Assurance (QA) pipeline focusing on geometry clipping. In this evaluation, a custom exploration agent navigates a game level to collect visual observations, while the automatic annotation pipeline provides frame-level clipping labels. This setup allows us to evaluate recent VLMs on a controlled anomaly detection task without manual annotation. We benchmark six recent VLMs (Gemini...
  </details>

- **2026-07-28** — Huynh Duc An Son Nguyen, Lukas Arzoumanidis, Youness Dehbi — [AuthentiCity: A Multi-Source Provenance-Aware Knowledge Graph and Benchmark for 3D City Models](http://arxiv.org/abs/2607.25243v1)
  <details><summary>📄 Abstract</summary>
  Urban digital twins increasingly combine authoritative, crowd-sourced, machine-learned, and reconstructed data with differing reliability, coverage, and semantics. Yet few urban datasets provide a unified representation supporting multi-source integration, provenance tracking, spatial reasoning, and machine learning. We present AuthentiCity, a multi-source, provenance-aware 3D city knowledge graph spanning five cities across three continents (Hamburg, Helsinki, Zurich, New York, and Tokyo) and c...
  </details>

- **2026-07-27** — Hyundoo Park, Byungho Choi — [When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops](http://arxiv.org/abs/2607.25152v1)
  <details><summary>📄 Abstract</summary>
  Long-running autonomous agents plan, act, and judge their own completion without human intervention. When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. We name this failure mode the progress mirage and show, with controlled measurement, that it is a question of what the evaluator is grounded in. We built a testbed that holds the agent and its tool surface fixed and manipulates only the info...
  </details>

- **2026-07-27** — Dushyant Sharma — [Gubernaut: A Deterministic Homeostatic Controller for Affect-Regulated LLM Agents, Validated Across Independent Model Families](http://arxiv.org/abs/2607.24339v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents inherit reactive failure modes: escalation under provocation, sycophantic drift under flattery, perseveration when stuck. These are failures of propensity, not capability; they concern what a model does under sustained pressure, which training-time alignment reduces but does not eliminate at runtime. This research led to the Gubernaut Cognitive Controller (GCC), a model-agnostic runtime control layer in a Nelson--Narens monitoring--control loop: an object level ...
  </details>

- **2026-07-27** — Kimi Team, Tongtong Bai, Yifan Bai et al. — [Kimi K3: Open Frontier Intelligence](http://arxiv.org/abs/2607.24653v1)
  <details><summary>📄 Abstract</summary>
  We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in o...
  </details>

- **2026-07-27** — Zhibin Kang, Hanmo You, Dong Wang et al. — [Evaluating Fuzz Testing for Reinforcement Learning Agents](http://arxiv.org/abs/2607.24577v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) agents are increasingly deployed in safety-critical domains such as robotics, autonomous driving, and drone control, where unexpected behaviors may lead to severe real-world consequences. Fuzz testing has recently emerged as a promising method for exploring the vast state spaces of RL agents and exposing crashes. Although numerous RL fuzzing methods have been proposed, existing studies often differ in evaluation settings, baselines, and metrics, making it difficult to...
  </details>

- **2026-07-27** — Th{é}otime de la Selle — [From transcription to semantic corpus analysis: unsupervised learning of sentence representations for ancient languages](http://arxiv.org/abs/2607.24542v1)
  <details><summary>📄 Abstract</summary>
  Automatic Text Recognition (ATR) now supplies digital humanities with large volumes of unstructured, heterogeneous, and often noisy text in ancient languages. Downstream semantic analysestext reuse identification, alignment, and semantic search-rely on sentence embeddings, yet existing methods transfer poorly to ancient languages: generic multilingual encoders underperform, specialized language models yield anisotropic representation spaces, and labeled similarity data is unavailable. We study t...
  </details>

- **2026-07-27** — Trung V. Phan, Tri Gia Nguyen, Thomas Bauschert — [DeepFaith: Evidence-Grounded LLMs for Faithful Incident Reporting in Multi-Stage APT Defense](http://arxiv.org/abs/2607.24348v1)
  <details><summary>📄 Abstract</summary>
  Advanced Persistent Threats (APTs) are difficult to detect and interpret due to their multi-stage and stealthy nature. While recent autonomous defense systems leverage provenance graphs and learning-based models for detection and mitigation, their outputs remain largely machine-oriented and difficult for analysts to interpret. Large language models (LLMs) offer a promising interface for report generation, but often produce hallucinated or weakly grounded content. In this paper, we propose DeepFa...
  </details>

- **2026-07-27** — Paul Kilian, Markus Kleffmann — [LLM-Based vs. Lexicon-Based Sentiment Signals for Tail-Risk Detection in Meme Stocks](http://arxiv.org/abs/2607.24072v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an empirical comparison of lexicon-based and Large Language Model (LLM)-based sentiment analysis for extracting market-relevant signals from social media discourse in highly volatile equity markets. Using Reddit data from r/WallStreetBets and focusing on meme stocks (GME, AMC, NOK), we construct time-aligned sentiment indicators and evaluate their relationship with market returns, with particular attention to extreme positive return events in the upper tail of the return dist...
  </details>

- **2026-07-27** — Keyu Li, Jin Gao, Dequan Wang — [The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards](http://arxiv.org/abs/2607.24063v1)
  <details><summary>📄 Abstract</summary>
  On standard factuality tasks, frontier models now cluster near the top of the scale. The question is therefore shifting from how factual a system is toward how much compute that factuality costs. Static leaderboards score factuality in isolation and treat compute as free, so they cannot tell a genuinely better system apart from one that simply spends more. Consider a ranking reversal. A brute-force Best-of-4 agent posts the higher raw factuality score (H-Score 0.9169 vs 0.9103) and would top a s...
  </details>

- **2026-07-27** — Pengkun Jiao, Bin Zhu, Jingjing Chen et al. — [Disentangling Semantic Attention from Structural Bias in the Attention Manifold](http://arxiv.org/abs/2607.24017v1)
  <details><summary>📄 Abstract</summary>
  The empirical success of attention mechanism in Multimodal Large Language Models (MLLMs) often obscures its inherent, subtle flaws. Specifically, MLLMs consistently exhibit disproportionate attention toward certain semantically uninformative visual tokens, a phenomenon termed "register" or "Visual Attention Sinks." While existing inference intervention methods attempt to identify these sink tokens and redistribute their attention weights, such approaches typically treat these tokens in isolation...
  </details>

- **2026-07-27** — Haozhen You, Zhen Dong, Jingjing Wang et al. — [Industrial Practice of LLM-Based Test Case Carving and Assertion Generation (Experience Paper)](http://arxiv.org/abs/2607.24000v1)
  <details><summary>📄 Abstract</summary>
  Enterprise regression testing for microservice systems is often constrained by incomplete or outdated documentation. In practice, QA engineers frequently rely on real execution traffic to reconstruct business scenarios; however, turning raw traffic into replayable regression tests with stable validation logic remains labor-intensive and error-prone.   This paper presents NL2Test, an end-to-end approach and tool that generates executable API regression tests from (i) a natural-language scenario d...
  </details>

- **2026-07-27** — Guoyi Zhang, Yanjin Du, Zhengyao Zhao et al. — [Effective Receptive Field Ordering Matters for Infrared Small Target Detection](http://arxiv.org/abs/2607.23994v2)
  <details><summary>📄 Abstract</summary>
  In this work, we investigate a previously unexplored architectural dimension for infrared small target detection: the organization of effective receptive fields (ERFs) during feature refinement. Unlike existing approaches that primarily improve individual feature operators, we argue that ERF organization constitutes an architectural dimension independent of receptive field design itself, and formulate deep feature transformation as a progressive residual correction process, from which a theoreti...
  </details>

- **2026-07-27** — Dane Malenfant — [Moral Hazard in Multi-Agent Language Models](http://arxiv.org/abs/2607.23982v2)
  <details><summary>📄 Abstract</summary>
  Cooperation can fail when socially valuable effort is costly, weakly observable, and mainly benefits others. Drawing on Holmström's team moral-hazard model, we introduce the Dialogue Moral Hazard Game, a controlled textual game that operationalizes this hidden-action structure for language agents. In each episode, an agent can preserve an immediate local reward or pay a query cost to reveal a hidden safety fact that primarily helps another agent's downstream decision. We evaluate seven open-weig...
  </details>

- **2026-07-27** — Yihui Zhang, Tianyu Wo, Jinghao Wang et al. — [SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving](http://arxiv.org/abs/2607.23933v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency. Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads. To resolve this dilemma, we ...
  </details>

- **2026-07-27** — Jun Ling, Tao Huang, Junzhuo Liu et al. — [GOTS: Greedy Orthogonal Token Selection for High-Resolution Vision-Language Models](http://arxiv.org/abs/2607.23913v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language models (VLMs) increasingly rely on dynamic or high-resolution visual encoding, producing thousands of visual tokens that substantially increase downstream language-model inference cost. Existing token-reduction methods assess token utility through token-wise importance, query relevance, coverage, pairwise diversity, or subset-level objectives. Our key insight is to view visual token reduction through selected-span complementarity: instead of scoring a token in isolation or...
  </details>

- **2026-07-27** — Keshav Rastogi, Eugy Han, Jeremy N. Bailenson — [FIDAC: An Easy-to-use Pipeline to Extract and Interpret Interpersonal Distance From Video](http://arxiv.org/abs/2607.25146v1)
  <details><summary>📄 Abstract</summary>
  The distance between persons reveals significant information about their perception of each other. However, such information is not easily extractable and interpretable from video input. We developed an open-sourced library, Facial Interpersonal Distance Analysis and Coding (FIDAC) that transforms facial detection results into actionable data about location and interpersonal distance. This tool merges data from multiple open-source facial detection models, strategically compensating for gaps in ...
  </details>

- **2026-07-27** — Anika Knupfer, Maximilian Lindholz, Johanna Paula Müller et al. — [Panda: Unsupervised Pelvic Anomaly Detection for Real-Time MR Imaging](http://arxiv.org/abs/2607.24703v1)
  <details><summary>📄 Abstract</summary>
  Female pelvic diseases remain an under researched area characterized by often delayed diagnosis. While pelvic MRI offers superior soft-tissue contrast for diagnosis and image-guided procedures, real-time anomaly detection remains challenging due to physiological motion, tissue deformation, and instrument artifacts. Existing supervised approaches are impractical, as adverse events are rare, heterogeneous, and difficult to annotate. We present a Dinomaly-based unsupervised anomaly detection framew...
  </details>

- **2026-07-27** — Marzieh Zare — [Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls](http://arxiv.org/abs/2607.24519v1)
  <details><summary>📄 Abstract</summary>
  Pretrained EEG foundation models are increasingly proposed for clinical decoding, but their transfer across populations and robustness to negative controls remain unclear. We benchmark six models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, and BIOT) on five clinical tasks across four datasets using frozen linear probes with leave-one-subject-out, subject-grouped, or explicitly identified recording-level splits. Selected REVE findings are tested against random initialisation, random features, label ...
  </details>

- **2026-07-27** — Keti Korini, Christian Bizer — [SINT-Flow: Schema Integration using Large Language Model Workflows](http://arxiv.org/abs/2607.24492v1)
  <details><summary>📄 Abstract</summary>
  The goal of schema integration is, given a set of input schemata or tables, to derive a global, unified schema that is able to represent the concepts, attributes, and relationships of all input tables in a coherent fashion. This paper presents SINT-Flow, a schema integration framework composed of five LLM-based operators that can be combined into workflows to perform fully automated, end-to-end schema integration. In contrast to existing approaches, SINT-Flow can process denormalized source tabl...
  </details>

- **2026-07-27** — Heyan Chai, Xin Li, Wenjie Wang et al. — [StanceFlip: A Comprehensive Multi-Dimensional Benchmark for Multimodal Conversational Stance Flipping Forecasting](http://arxiv.org/abs/2607.24191v1)
  <details><summary>📄 Abstract</summary>
  Conversational stance detection has shifted from static text analysis to dynamic multimodal modeling. However, existing benchmarks exhibit three key limitations: failure to capture the dynamic evolution of beliefs, particularly during stance reversals; difficulty in disentangling affective states from logical reasoning; and neglect of the critical role of multimodal cues in resolving pragmatic ambiguities such as sarcasm. To address these limitations, we propose StanceFlip, a benchmark designed ...
  </details>

- **2026-07-27** — Tieniu Wang, Cangzhu Huang, Qianhui Li — [Myopia Prevention and Control 3.0: Artificial Intelligence--Driven Risk Stratification, Proactive Monitoring, and Personalized Intervention](http://arxiv.org/abs/2607.24187v1)
  <details><summary>📄 Abstract</summary>
  The convergence of artificial intelligence (AI), digital sensing, and ubiquitous computing has created an unprecedented opportunity to transform myopia prevention from a reactive, population-based model into a proactive, precision-driven one. Despite evidence that half the world's population will be myopic by 2050, conventional approaches---school-based vision screening (Phase 1.0) and evidence-based risk factor management (Phase 2.0)---have proven insufficient. We review the emergence of Myopia...
  </details>

- **2026-07-27** — Jingkun Luo, Da-Tian Peng — [Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation](http://arxiv.org/abs/2607.24054v1)
  <details><summary>📄 Abstract</summary>
  A correct answer can conceal why an agent succeeded. Once agents change their information state during evaluation, correctness no longer distinguishes intended reasoning from answer acquisition. Outcome evidence and exposure detection do not establish whether success depended on an acquired target; we call this missing evaluation object success provenance. AcquaBench audits it through matched CLEAN, GOLD, and SHAM value substitution on four standardized surfaces with joint qid-clustered analysis...
  </details>

- **2026-07-27** — Saurabh Ranjan, Konstantina Sokratous, Brian Odegaard — [Reality Monitoring in Large Language Models: Self-Knowledge That Transforms with Conversation Memory](http://arxiv.org/abs/2607.23927v1)
  <details><summary>📄 Abstract</summary>
  A conversational AI that cannot tell its own output from what a user said will treat its own mistakes as user-provided facts. In humans, this capacity is called reality monitoring, and its failures are linked to hallucinations, delusions, and confabulation, yet whether LLMs possess it remains untested. Here we show, across two experiments and six LLMs, that source attribution depends on how conversational memory is structured: ceiling accuracy for self-generated content under minimal memory dema...
  </details>

- **2026-07-26** — Satyam Kumar, Saurabh Jha — [The Missing Layer: Specification Infrastructure for AI Oversight](http://arxiv.org/abs/2607.24866v1)
  <details><summary>📄 Abstract</summary>
  AI safety has a missing layer. Interpretability, formal methods, security engineering, evaluation methodology, and reinforcement-learning safety each produce substantial work, but the resulting artifacts do not compose into deployable oversight: every team fielding an agentic system builds its own audit schema, policy dialect, monitoring stack, and escalation path, mostly reinventions of patterns understood elsewhere. We diagnose this as a coordination gap, not a research gap, and propose a two-...
  </details>

- **2026-07-26** — Zhonghua Chu, Hongliang Luo, Boxuan Sun et al. — [ISAC and Vision Fusion for Fine-Grained Low-Altitude Target Recognition](http://arxiv.org/abs/2607.23789v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an integrated sensing and communications (ISAC) and vision fusion framework for fine-grained low-altitude target recognition. Specifically, we first utilize ISAC system to estimate the position of the low-altitude target. Then we adjust the working parameters of the Pan-TiltZoom (PTZ) camera based on the estimated target position, such that the camera can capture the image of tiny low-altitude target from several hundred meters away. After obtaining the wireless echo si...
  </details>

- **2026-07-26** — Ionut Predoaia, Tuong Manh Vu, Konstantinos Barmpis et al. — [A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems](http://arxiv.org/abs/2607.23884v1)
  <details><summary>📄 Abstract</summary>
  Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design. This paper presents an implementation-grounded comparison of the Model Context Protocol (MCP) and the Agent2Agent (A2A) protocol, from a multi-agent systems engineering perspective, using an inter-agent coordination scenario involving LLM-based agents. We evaluate an MCP-based a...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 70 papers

- **2026-07-29** — Roshan Kenia, Stephanie L McNamara, William Lotter — [Anatomy Contextualized Adaption of CT Foundation Models](http://arxiv.org/abs/2607.27154v1)
  <details><summary>📄 Abstract</summary>
  CT vision-language foundation models have demonstrated promising performance across downstream tasks, but are typically trained with whole-volume representations that dilute fine-grained anatomical signals. Fine-grained vision-language pre-training addresses this by aligning anatomy-level visual features with anatomy-specific text, but in doing so discards the global context that whole-volume models provide. Furthermore, existing fine-grained approaches train from scratch, making them computatio...
  </details>

- **2026-07-29** — Xiaochen Wang, Yuan Zhong, Haoyu Wang et al. — [KAMR: Grounding Generation via Knowledge-Aligned Multi-hop Retrieval](http://arxiv.org/abs/2607.27136v1)
  <details><summary>📄 Abstract</summary>
  Graph-based retrieval-augmented generation increasingly relies on multi-hop retrieval, where answering a query requires composing multiple connected knowledge-graph triplets. However, existing retrievers often rank triplets independently via global semantic matching. Moreover, many multi-hop benchmarks provide only final answers, which limits supervision for query--triplet alignment and causes structurally necessary but weakly aligned facts to be missed. To address these issues, we propose a kno...
  </details>

- **2026-07-29** — Itbaan Safwan, Ramail Khan, Muhammad Annas Shaikh et al. — [Towards Grounded GI Endoscopy VQA via Multi-Task Learning on Small VLMs](http://arxiv.org/abs/2607.27122v1)
  <details><summary>📄 Abstract</summary>
  Gastrointestinal (GI) endoscopic image analysis has shifted from single-label classification toward visual question answering (VQA), where a model must answer free-form clinical questions about an image. While recent vision-language models (VLMs) achieve promising answer accuracy on this task, clinical adoption also requires the model's internal representations to reflect the visual evidence behind its answers. We propose a simple multi-task fine-tuning recipe that constructs auxiliary grounding...
  </details>

- **2026-07-29** — Zihan Deng, Chuanzhi Xu, Huiqi Liang et al. — [SciFigQual-Bench: A Benchmark for Scientific Figure Quality Assessment with Full-Manuscript Context](http://arxiv.org/abs/2607.27084v1)
  <details><summary>📄 Abstract</summary>
  Scientific images are the core elements of presenting experimental conclusions, elaborating system architecture, and supporting comparative arguments in scientific papers. However, existing image quality assessment (IQA) methods are predominantly designed for natural photographs or AI-generated content, which cannot be directly applied to scientific papers. The few existing studies on scholarly charts remain confined to visual-surface comparisons, failing to verify caption alignment, citation re...
  </details>

- **2026-07-29** — Chuanzhi Xu, Zihan Deng, Huiqi Liang et al. — [SciFigAlign: Scoring Scientific Figures by Fine-tuned Alignment of Visuals with Manuscript Evidence](http://arxiv.org/abs/2607.27066v1)
  <details><summary>📄 Abstract</summary>
  Scientific figure assessment in peer review differs fundamentally from general image quality evaluation: a figure must be visually legible, faithfully support the manuscript's claims, and communicate evidence with a clear visual hierarchy. However, if we apply traditional image assessment methods to scientific figure quality assessment, limitations emerge: classic IQA models capture perceptual quality or aesthetics but cannot judge whether a figure serves the paper's scientific argument; CLIP-ba...
  </details>

- **2026-07-29** — Seonglae Cho, Adriano Koshiyama — [OptimismBench: Forecasting Bias and the Alignment Effect in Language Model Judgment](http://arxiv.org/abs/2607.26981v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as decision aids whose probability judgments shape downstream choices. Whether those judgments carry a systematic directional tilt has been hard to detect: calibration metrics aggregate unsigned errors, and naturalistic uncertainty offers no ground-truth probability. When an LLM rates a startup's success at 70% but its failure at 15%, the missing 15 points expose a distortion no aggregate score flags. We introduce OptimismBench, which detects direction...
  </details>

- **2026-07-29** — Duzhen Zhang, Yahan Yu, Qiaoyi Su et al. — [Progressive Multimodal Alignment for Continual Instruction Tuning](http://arxiv.org/abs/2607.26947v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) rely on a projector to align visual representations with the language embedding space, making it central to cross-modal understanding. In Multimodal Continual Instruction Tuning (MCIT), however, shifting visual distributions and evolving instruction semantics cause this shared projector to drift, leading to projector-level forgetting, an issue largely overlooked by methods that focus primarily on the LLM backbone. We introduce Progressive Multimodal Align...
  </details>

- **2026-07-29** — Qianru Li, Xuyang Chen, Erkin Türköz et al. — [CinemaTraj: Composing Atomic Camera Trajectories for 3D Scenes with LLM Agents](http://arxiv.org/abs/2607.26910v1)
  <details><summary>📄 Abstract</summary>
  Automatically generating cinematically expressive camera trajectories through 3D scenes from natural language descriptions is a challenging task of high practical value, with applications ranging from real-estate advertising to virtual tour creation. Existing methods either lack true 3D spatial awareness by relying on 2D image priors, or treat trajectory generation as a geometric path planning problem divorced from cinematographic semantics. We present CinemaTraj, a framework that reframes camer...
  </details>

- **2026-07-29** — Yilei Wang, Jiaxin Gan, Kexuan Zhang et al. — [DIRECT: Direct Decoding for Efficient and Aligned Sequence Labeling with Large Language Models](http://arxiv.org/abs/2607.26891v1)
  <details><summary>📄 Abstract</summary>
  Sequence labeling is a fine-grained information extraction task, yet existing large language model-based approaches suffer from insufficient domain alignment and low inference efficiency. To address these issues, we propose DIRECT, a framework that addresses these issues through training-time optimization and inference-time rectification. Specifically, DIRECT performs Direct Preference Optimization (DPO) after supervised fine-tuning to strengthen task alignment with human preferences, and introd...
  </details>

- **2026-07-29** — Yunzhan Fu, Enyu Bao, Xiangyu Shen et al. — [SCALPEL: Semantic Cross-modal Alignment via LLM-Powered Encoder Learning for Medical Vision-Language Representation](http://arxiv.org/abs/2607.26885v1)
  <details><summary>📄 Abstract</summary>
  Vision-language pre-training (VLP) serves as a cornerstone for medical multimodal representation learning. However, existing medical VLP frameworks are often constrained by the limited context windows and shallow representational capacities of lightweight text encoders when processing lengthy, terminology-dense clinical reports. While integrating medical large language models (LLMs) offers unprecedented clinical reasoning capabilities, it introduces three major bottlenecks: (i) the anisotropic r...
  </details>

- **2026-07-29** — Hyunjin Ahn, Woojoo Shim — [Geometric Control of Moving Parallel Transport in Riemannian Cucker--Smale Dynamics with Bonding Forces](http://arxiv.org/abs/2607.26748v1)
  <details><summary>📄 Abstract</summary>
  We study a Cucker--Smale type system with bonding forces on complete Riemannian manifolds with uniformly bounded curvature. On general manifolds, the time variation of parallel transport between moving agents produces curvature-dependent terms, so the standard energy-dissipation argument does not directly yield asymptotic velocity alignment. The bonding energy confines all pairwise distances below the injectivity radius, providing global well-posedness and time integrability of the transported v...
  </details>

- **2026-07-29** — Xiaolong Liu, Junjian Li, Yuan Xiao et al. — [Dual Inversion for Text-to-Image Diffusion Models: From Both Prompt and Noise Perspectives](http://arxiv.org/abs/2607.26735v1)
  <details><summary>📄 Abstract</summary>
  Prompt inversion, as a typical reverse engineering technique, enables text-to-image (T2I) diffusion models to generate the desired target images without extensive prompt engineering. However, existing prompt inversion methods suffer from significant limitations: (1) gradient-based methods are unstable and uninterpretable, often resulting in generated images with severe artifacts; (2) gradient-free methods yield human-readable prompts but still fail to preserve visual fidelity due to the lack of ...
  </details>

- **2026-07-29** — Yupeng Qiu, Han Fang, Ee-Chien Chang — [CASIAL: Geometric Distortion Robust Image Watermarking](http://arxiv.org/abs/2607.26729v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based watermarking has shown strong robustness against non-geometric distortions, yet its performance under geometric transformations remains limited. Such transformations induce two fundamental failure modes: region removal, such as cropping or masking, which eliminates the information carried by removed pixels, and desynchronization, such as scaling or rotation, which misaligns pixel positions and disrupts decoding. We argue that achieving geometric robustness requires two essent...
  </details>

- **2026-07-29** — Desiree Cho, Cameron Tice, Bernie Hogan et al. — [Constitutional Midtraining: Content Presence Drives Alignment Gains](http://arxiv.org/abs/2607.26654v1)
  <details><summary>📄 Abstract</summary>
  Post-training alignment is often shallow, eroding under fine-tuning. Whether midtraining interventions, cleanly isolated from post-training, can produce durable alignment remains untested. We test this via constitutional midtraining: inserting principled, values-based content into midtraining against a replay-only control at 120B scale. Our 394M-token constitutional corpus, built from Anthropic's Constitution, uses a 2x2 factorial design (curriculum ordering x deliberative reasoning) to produce ...
  </details>

- **2026-07-29** — Xinyi Wang, Yuyang Huang, Yalin Su et al. — [Anchoring and Steering Diffusion: Enhancing the Faithfulness of Text-to-Image Generation at Inference Time](http://arxiv.org/abs/2607.26647v1)
  <details><summary>📄 Abstract</summary>
  While text-to-image diffusion models achieve impressive visual quality, they frequently struggle to maintain precise alignment with complex compositional prompts. An effective strategy is to improve the inference process of diffusion models, thereby better leveraging their pretrained priors to address misalignment. Existing training-free methods can be divided into two categories. The first category focuses on improving the randomly sampled initial noise, either performing costly search over noi...
  </details>

- **2026-07-29** — Hao Jiang, Peiru Du, Pengfei Yao et al. — [WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models](http://arxiv.org/abs/2607.26621v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong reasoning capabilities, motivating their adoption as backbones for foundation recommendation models (FRMs). Existing approaches typically enhance recommendation with explicit Chain-of-Thought (CoT) under the Think-then-Answer paradigm. However, generating lengthy rationales introduces substantial inference overhead, while fixed CoT templates struggle to model diverse, dynamic, and context-dependent user interests. We propose WhisperRec, an ef...
  </details>

- **2026-07-29** — Yusen Wan, Zeyuan Chen, Qianshi Zou et al. — [R-SLPR: Region-based Small-to-Large Point-cloud Registration with Contrastive Learning](http://arxiv.org/abs/2607.26583v1)
  <details><summary>📄 Abstract</summary>
  Point-cloud (PC) registration is fundamental to three-dimensional (3D) perception in robotic systems. However, classic registration algorithms falter when aligning a source PC containing limited, incomplete, or ambiguous geometric cues against a reference. This challenge of registering a small, partial PC to a significantly larger global reference is pervasive in real-world deployment yet remains insufficiently addressed by existing learning-based approaches, which typically assume comparable sc...
  </details>

- **2026-07-29** — Yuyun Chen, Tianao Li, TianQuan Feng et al. — [EgoSafe: A First-Person Mobile-Captured Benchmark for Visual Safety Understanding](http://arxiv.org/abs/2607.26518v1)
  <details><summary>📄 Abstract</summary>
  Reliable visual safety understanding in real-world scenarios demands more than just object recognition; it requires causal reasoning under epistemic uncertainty. While Large Vision-Language Models (LVLMs) demonstrate impressive semantic alignment on standard benchmarks, they often struggle to distinguish between superficial correlation and genuine forensic logic when grounded in the dynamic, partially observable nature of first-person experiences. Existing evaluations, dominated by third-person ...
  </details>

- **2026-07-29** — Hasibur Rahman, Smit Desai — [Misalignment Has a Personality: A Big Five Account of Emergent Misalignment](http://arxiv.org/abs/2607.26389v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a language model on data containing a narrow flaw, such as insecure code or incorrect mathematical answers, can cause broad misalignment through a mechanism that remains debated. We provide an interpretable account: in the models and corpora we study, misalignment behaves like a shift in personality. Prior work extracts activation directions for character traits from a single binary contrast, which can separate or steer behavior without establishing a calibrated scale. We instead ext...
  </details>

- **2026-07-29** — Farhan Farsi, Shayan Bali, Mohammad Heydari Rad et al. — [Symphony of Bias: Exploring Gender Associations with Musical Instruments in Multimodal LLMs](http://arxiv.org/abs/2607.26355v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly embedded in everyday life and widely used for information seeking, raising concerns about their potential to perpetuate social biases and reinforce stereotypes. In this study, we investigate gender bias in LLMs through the lens of their associations with musical instruments. Building on social-science research on the cultural gender-typing of instruments, we introduce Symphony-Bias, a parallel multimodal dataset spanning text, vision, and audio. We e...
  </details>

- **2026-07-28** — Marylou Fauchard, Florian Carichon, Margarida Carvalho et al. — [Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems](http://arxiv.org/abs/2607.26120v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs)-powered multi-agent systems are increasingly deployed in mixed-motive environments, where agents operate under asymmetric information and strategic deception due to conflicting or hidden objectives. In these settings, misalignment with collective goals becomes a central concern. We propose a novel framework for evaluating objective misalignment using the social deduction game Werewolf, modifying the objective of a single agent while preserving its assigned role. Acro...
  </details>

- **2026-07-28** — Panagiotis Fytas, Ian Selby, Clemens Karner et al. — [Rethinking Clinical Relevance in Chest X-ray Machine Learning: How Evaluation References Define Performance](http://arxiv.org/abs/2607.26333v1)
  <details><summary>📄 Abstract</summary>
  Chest X-ray (CXR) machine learning relies heavily on automated evaluation using reference standards that aim to approximate clinical judgment. However, commonly used report-derived labels for pathology classification or generic image quality metrics for reconstruction may not reliably reflect clinical judgment. We systematically investigate how evaluation-reference choices affect model performance and ranking in both pathology classification and image quality assessment (IQA). To enable controll...
  </details>

- **2026-07-28** — Wenjie Zhou, Yunting Liu, Renjiao Tang et al. — [Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach](http://arxiv.org/abs/2607.26317v1)
  <details><summary>📄 Abstract</summary>
  Psychometric calibration for educational tests typically requires costly human response data. Large language models (LLMs) simulated examinees offer a promising route to early calibration, but their responses are too accurate and too uniform. We propose Cognitive Diagnostic Profiling (CDP), a zero-shot framework that prompts LLMs to simulate plausible examinees with diverse cognitive profiles: binary attribute-mastery patterns are rendered as natural-language profiles and sampled under an uninfo...
  </details>

- **2026-07-28** — Anton de la Fuente, Arthur Conmy — [Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models](http://arxiv.org/abs/2607.26173v1)
  <details><summary>📄 Abstract</summary>
  Alignment training, model organisms, and toy models are usually treated as separate research areas. But projects in all three frequently use supervised fine-tuning (SFT) to pursue the same underlying goals. When projects share a goal, we should test whether lessons learned from one area transfer to the other areas. We study three such transfers, each taking a lesson developed in one SFT setting and testing it in another. First, we port a lesson about behavior generalization from alignment traini...
  </details>

- **2026-07-28** — Ethan J. Mick, Campbell A. Sweet, Matthias J. Young et al. — [Data Fusion and Contrastive Alignment for Unconstrained IR Molecular Structure Elucidation](http://arxiv.org/abs/2607.26164v1)
  <details><summary>📄 Abstract</summary>
  Automated molecular structure elucidation from infrared (IR) spectroscopy data has seen significant advancements in recent years, but its broad applicability is limited by a reliance on pre-determined chemical formulas provided as auxiliary model inputs. This limits model predictions to isomer identification rather than full molecular structure prediction. Although transformer models have been shown to identify molecular isomers with high accuracy, their reliability for unconstrained structure e...
  </details>

- **2026-07-28** — Xinran Liu, Shouqian Shi, Yutong Chen et al. — [TraceCLIP: Recovering Local Semantics from Patch-to-CLS Contributions](http://arxiv.org/abs/2607.26107v1)
  <details><summary>📄 Abstract</summary>
  Dense vision-language understanding, including object localization, region recognition, and open-vocabulary semantic segmentation, requires associating language concepts with spatially grounded visual regions. CLIP provides a strong foundation for these tasks by learning a shared image-text embedding space from large-scale contrastive pre-training. However, its image-level objective aligns text with a CLS-derived global representation, leaving local vision-language correspondence only indirectly...
  </details>

- **2026-07-28** — Yunpeng Chu — [Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback](http://arxiv.org/abs/2607.26094v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning from Human Feedback (RLHF) is the standard approach for aligning large language models with human preferences, but its quality is limited by static, task-agnostic reward models. This mismatch leads to sparse learning signals and suboptimal alignment. We introduce MeRLa (Meta-Learned Reward Shaping), a principled framework that meta-learns a task-aware shaping function $Φ(x,y;φ)$ across auxiliary tasks before RLHF training. The learned shaping produces a composite reward th...
  </details>

- **2026-07-28** — Yu Yan, Jiahao Chen, Siqi Lu et al. — [Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks](http://arxiv.org/abs/2607.25227v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs. However, the deep integration of open-source model sharing ecosystems with LLM-powered critical decision-making applications also introduces critical risks: if an attacker can manipulate the model's cognitive stance, they can indirectly influence the judgments and actions of downstream decision-makers. This paper defines s...
  </details>

- **2026-07-28** — Frank Nie, Ethan B Liu, Yuan Zhu et al. — [A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series](http://arxiv.org/abs/2607.25947v1)
  <details><summary>📄 Abstract</summary>
  Question answering (QA) over irregular clinical time series (ICTS) plays a pivotal role in a wide range of healthcare applications. Although recent multimodal time-series large language models (LLMs) have shown considerable promise in general-purpose time-series QA, they remain poorly equipped to model the sparsity, asynchrony, and irregular sampling patterns of clinical observations. To fill this gap, we propose ClinPRISM, a cost-effective multimodal LLM reasoning framework for question answeri...
  </details>

- **2026-07-28** — Can Lei, Rafael Garcia, Nuno Gracias et al. — [SC-Match: Scale-Space Matching with Context Consistency for Side-Scan Sonar Mapping](http://arxiv.org/abs/2607.25937v1)
  <details><summary>📄 Abstract</summary>
  Reliable estimation of spatial correspondences between overlapping side-scan sonar (SSS) measurements is essential for mapping, but acoustic appearance variations, weak seabed texture, repetitive patterns, and shadows make such correspondences sparse, unstable, and context-dependent. Scarce point-level annotations further limit sonar-specific training or fine-tuning of deep matching models. To this end, we propose SC-Match, a training-free scale-space matching framework with context-consistent c...
  </details>

- **2026-07-28** — Ramtin Ehsani, Irene Manotas, Saurabh Pujar et al. — [How Do LLMs Read Bug Reports? An Empirical Study of Attention in LLMs for Automated Program Repair](http://arxiv.org/abs/2607.25873v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based Automated Program Repair systems are advancing rapidly, yet their performance remains inconsistent. Even when provided with the same contextual information, an LLM may generate a correct patch for one bug but fail on another closely related bug. Why this happens remains poorly understood, and it is unclear how LLMs prioritize the diverse information in bug reports and whether model attention affects repair success. In this paper, we present the first empirical st...
  </details>

- **2026-07-28** — Leonardo Centellas-Claros, Estefania Pakarati-Cofre, Juan Pablo Sandoval Alcocer et al. — [Rethinking Training Data for Generating Code Review Comments](http://arxiv.org/abs/2607.25851v1)
  <details><summary>📄 Abstract</summary>
  Generating code review comments has become a prominent research direction in automated code review, commonly formulated as a text generation task over diff-comment pairs. Despite advances in learning-based approaches, generated review comments are often generic, weakly grounded, or non-actionable. Recent studies have also shown that review comment datasets contain noisy or unsuitable training instances, motivating LLM-based dataset cleaning approaches. In this paper, we argue that problematic tr...
  </details>

- **2026-07-28** — Aleksandr V. Petrov, Tarun Chillara, Matthew D. Moellman et al. — [Hypothesis-Driven Shelf Generation for Personalised Recommendation](http://arxiv.org/abs/2607.25823v1)
  <details><summary>📄 Abstract</summary>
  Modern recommendation interfaces organise content into shelves: themed rows such as "More of What You Like" or "New Releases for You." In production systems, these shelves are typically defined through hand-crafted templates coupled with dedicated retrieval logic. While effective for broad recommendation intents, this approach does not scale to the long tail of individual taste. We present a content-hypothesis-driven shelf generation system for Spotify Home that replaces fixed templates with nat...
  </details>

- **2026-07-28** — Jui-Feng Chi, Wei-Lun Chu, Bruce Coburn et al. — [Fine-Grained Food Image Understanding via Target-Aware Data Alignment](http://arxiv.org/abs/2607.25794v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained food visual--semantic understanding requires models to capture subtle distinctions across ingredients, cooking methods, doneness, color, texture, and plate composition. Although CLIP-style vision-language models provide a natural framework for this task, their effectiveness is limited when training relies on heterogeneous web-collected image--text pairs. Such data often exhibit a web-to-target domain gap and cross-modal misalignment, where images differ from the target distribution ...
  </details>

- **2026-07-28** — Seungheon Doh, Bruno Sguerra, Sergio Oramas et al. — [LLM-as-a-Judge for Evaluating System Responses in Conversational Music Recommendation](http://arxiv.org/abs/2607.25640v1)
  <details><summary>📄 Abstract</summary>
  Conversational Recommendation Systems (CRS) aim to achieve two primary objectives: recommending relevant items and generating natural language responses. While recommendation accuracy is effectively measured by established ranking metrics, the evaluation of response generation poses a more fundamental challenge. Although human evaluation remains the gold standard, its cost and scalability constraints have motivated the adoption of LLM-as-a-judge as a promising proxy, whose alignment with human j...
  </details>

- **2026-07-28** — Jiarui Wang, Xiang Shi, Jiaqi Cao et al. — [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](http://arxiv.org/abs/2607.25614v1)
  <details><summary>📄 Abstract</summary>
  Adapting Large Language Models (LLMs) to specialized domains often incurs an alignment tax, as fine-tuning on domain-specific tasks can cause catastrophic forgetting and substantially degrade performance on general tasks. We propose MemSFT, which mitigates the alignment tax by decoupling domain specialization from backbone parameter updates through a plug-and-play parametric memory. The memory is trained to imitate the behavior of a non-parametric retriever operating over domain data, thereby me...
  </details>

- **2026-07-28** — Abraham Chachamovits — [Phase Structure in Rotary Attention: A Spectral Framework for Semantic Continuity and Execution-Boundary Governance](http://arxiv.org/abs/2607.25507v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models are usually analyzed through vector geometry, yet ordered context and rotary position encoding introduce explicit phase structure into query-key interactions. This paper develops a bounded spectral framework for examining rotary phase alignment, hidden-state continuity, and semantic drift without treating language models as literal physical wave systems. It first identifies ordered hidden-state sequences, rather than vocabulary indices, as valid domains for spectral d...
  </details>

- **2026-07-28** — Jincheng Wang, Min Zheng, Tao Wei — [COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution](http://arxiv.org/abs/2607.25400v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted. When these instructions are supplied as prompt context, however, the model retains control over both procedure selection and step execution. As interactions accumulate, an agent can skip required steps, take unsupported branches, or execute a vali...
  </details>

- **2026-07-28** — Huwei Ji, Jiajie Su, Yuyuan Li et al. — [Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain Sequential Recommendation](http://arxiv.org/abs/2607.25366v1)
  <details><summary>📄 Abstract</summary>
  LLM-based Cross-Domain Sequential Recommendation (CDSR) leverages LLMs to enhance target performance via deep semantic reasoning, alleviating the dependency on overlapping users. Among LLM-based paradigms, model merging is particularly promising for multi-domain scenarios due to its superior scalability and flexibility in integrating diverse knowledge sources. However, our empirical investigations reveal two critical bottlenecks: (1) cross-domain knowledge conflict; and (2) performance saturatio...
  </details>

- **2026-07-28** — Yujian Ma, Jinqiu Sang, Ruizhe Li et al. — [From Semantics to Readout: Mechanistic Understanding of Audio Tokens after Fine-Tuning for Temporal Audio Grounding](http://arxiv.org/abs/2607.25355v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) convey acoustic evidence to language decoders through native audio tokens, yet the internal roles of these tokens remain poorly understood. Using temporal audio grounding as a diagnostic setting, we examine how language-model fine-tuning affects the layerwise semantics, decoder accessibility, and temporal output alignment of native audio-token states through four complementary analyses: query-conditioned token semantics, calibrated token readout, temporal-wind...
  </details>

- **2026-07-28** — Aysan Aghazadeh, Sina Malakouti, Adriana Kovashka — [Sense it with your eyes: Sensation Generation and Understanding for Advertisements](http://arxiv.org/abs/2607.25314v1)
  <details><summary>📄 Abstract</summary>
  Sensory advertising evokes human senses through visual cues, enabling audiences to mentally simulate experiences and increasing persuasive impact. Despite the recent increase in using AI in generating and understanding creative and persuasive content, how advertisements visually evoke sensations remains largely unexplored. In this work, we introduce the first study of understanding, evaluating, and generating sensory ads. We introduce the Sensory Ad dataset, and define sensation classification t...
  </details>

- **2026-07-28** — Katsuya Ogata, Zongshang Pang, Mayu Otani et al. — [MEDit-Bench: A Dataset for Evaluating Message-Driven Narrative Video Editing](http://arxiv.org/abs/2607.25300v1)
  <details><summary>📄 Abstract</summary>
  Video editing is fundamentally message-driven: even from the same source footage, the selected shots change depending on the narrative the editor wishes to convey. Benchmarks for a closely related task, video summarization, reduce editorial intent to a single, message-agnostic notion of saliency and thus do not account for this diversity. For evaluating message-driven video editing, we present \textbf{MEDit-Bench}, a dataset and benchmark, which pairs long-form videos with multiple editing messa...
  </details>

- **2026-07-28** — Jingbo Zhang, Haoxiang Sun, Wenbo Wang et al. — [ContractHIL-HLS: Contract-Aligned Multi-Agent Workflow with Hardware-in-the-Loop Feedback for HLS Design](http://arxiv.org/abs/2607.25283v1)
  <details><summary>📄 Abstract</summary>
  This paper presents ContractHIL-HLS, a contract-aligned multi-agent workflow for practical high-level synthesis (HLS) engineering. The workflow makes three contributions. First, it introduces a structured contract as the semantic-alignment and task-execution artifact that translates natural language requirements into explicit interfaces, constraints, validation checks, and rollback rules. Second, it incorporates hardware information into the feedback loop by feeding HLS, Vivado, PYNQ runtime, po...
  </details>

- **2026-07-28** — Qian Cheng, Saad Mohammad Rafid Pial, Ruize Tang et al. — [Specula: Scaling formal specifications for autonomous model checking of system code](http://arxiv.org/abs/2607.25333v1)
  <details><summary>📄 Abstract</summary>
  Specula is a push-button agentic system that generates high-quality formal specifications for large, complex system code and uses the specifications for highly effective model checking and bug finding. Specula employs large language model (LLM) based coding agents to autonomously develop TLA+ specifications, including invariants that describe correctness properties of the target system and formal models that describe the system implementation with the right level of abstractions. Specula is full...
  </details>

- **2026-07-28** — Xiaoyu Huang, Lulu Wang — [Emergent Latent-State Computation under Stochastic Volatility](http://arxiv.org/abs/2607.25459v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has largely focused on language models and deterministic toy tasks. Much less is known about how sequence models internally represent latent stochastic dynamics under noisy, partially observed observations. We study this question in a controlled multivariate stochastic volatility setting, where models observe only returns while the ground-truth latent volatility state is known to the researcher. This setting provides a useful benchmark for mechanistic interpretabilit...
  </details>

- **2026-07-27** — Michał Wiliński, Liu Leqi, Chirag Nagpal — [Inverse RL Helps Align AI by Imitating Humans](http://arxiv.org/abs/2607.24900v1)
  <details><summary>📄 Abstract</summary>
  Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following. Current approaches typically use supervised fine-tuning on demonstrations or reinforcement learning with rewards derived from verifiers or human feedback. These paradigms leave an important question underexplored: can demonstrations alone yield an implicit reward that can be inspected, reused, and optimized on-policy to align AI? Motivated by inverse ...
  </details>

- **2026-07-27** — Yubo Sun, Chunyi Peng, Yukun Yan et al. — [HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research](http://arxiv.org/abs/2607.25151v1)
  <details><summary>📄 Abstract</summary>
  Deep research requires models to retrieve, connect, and synthesize evidence from large-scale heterogeneous sources to answer complex queries and produce analytical reports. Existing benchmarks mainly evaluate final outcomes, such as answer correctness, report quality, or citation alignment, while providing limited visibility into whether evidence is correctly selected, linked, and aggregated into supported claims and conclusions. To address this gap, we introduce HiEviDR-Bench, a benchmark for e...
  </details>

- **2026-07-27** — Takuya Isogawa, Ryotaro Okabe, Nutdech Phadetsuwannukun et al. — [Agentic AI for Scientific Reasoning in Autonomous Quantum Sensing Experiments](http://arxiv.org/abs/2607.25145v1)
  <details><summary>📄 Abstract</summary>
  We implement an agentic AI workflow built around a large language model (LLM) agent for autonomous experiments with nitrogen-vacancy (NV) centers in diamond. NV centers are a widely used platform for quantum sensing, and the ability to control many measurements from a computer makes NV experiments a natural setting for autonomous workflows. We make two main contributions. First, we demonstrate an autonomous NV experiment workflow that combines persistent project records, quantitative calculation...
  </details>

- **2026-07-27** — Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray — [Towards Robust Reinforcement Learning for Small-Scale Language Model Agents](http://arxiv.org/abs/2607.25091v1)
  <details><summary>📄 Abstract</summary>
  The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated. In the State-of-the-Art (SOTA) research, fifteen (model, corpus) configurations were trained using Proximal Policy Optimization (PPO). The experiments included Pythia-70M, 160M, 410M and SmolLM2-135M, 360M on the TinyStories, CNN/DailyMail, and Wikitext-103 corpora. Three reprod...
  </details>

- **2026-07-27** — Sylvain Chassang — [Interactive Alignment](http://arxiv.org/abs/2607.25019v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the long-run alignment of interactive agents, including AI systems, teams, firms, and governments, with human welfare. It develops a farming game in which a population of agents makes planting, trading, and expansion decisions. Agents must allocate final output between transfers to humans and investment in their own expansion. Because transfers to humans reduce the resources available for expansion, evolutionary forces tend to select against aligned behavior. The central quest...
  </details>

- **2026-07-27** — Yifan Ye, Yankai Fu, Yaoxu Lv et al. — [Data Pyramid for Embodied Manipulation](http://arxiv.org/abs/2607.24744v1)
  <details><summary>📄 Abstract</summary>
  Multimodal foundation models learned to see and to speak by consuming the whole internet. Embodied agents admit no such shortcut, since they require data that couple observations with physical states and actions. These signals can be provided, to varying degrees, by multiple data sources. In this work, we organize the embodied data ecosystem as a "pyramid" spanning five complementary sources: real-robot data, UMI-style data, egocentric and exocentric data, simulation data, and general vision-lan...
  </details>

- **2026-07-27** — Yu Xia, Zihan Lin, Wei Yang et al. — [LaRec: Unleashing LLM-based Latent Reasoning for Generative Recommendation](http://arxiv.org/abs/2607.24617v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown great promise in recommendation due to superior reasoning abilities. However, existing methods mainly rely on explicit Chain-of-Thought (CoT), resulting in verbose reasoning texts and inefficient response times. latent reasoning aims to balance efficiency by thinking within a continuous latent space, yet it faces two major challenges: (1) Lack of Fine-grained Supervision: Latent reasoning relies solely on feedback from the final labels, providing sparse su...
  </details>

- **2026-07-27** — André Sacilotti, Samuel Felipe dos Santos, Jurandy Almeida — [Test-Time Adaptation via Dual Distillation for Videos Under Severe Distribution Shifts](http://arxiv.org/abs/2607.24611v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models have achieved state-of-the-art performance in several computer vision tasks. However, they experience severe performance degradation when applied to real-world scenarios due to unanticipated distribution shifts. Test-Time Adaptation (TTA) attempts to solve this problem by using unlabeled data from the target domain to dynamically adapt to the test distribution at inference time, without access to the source data. However, TTA remains a challenging problem when adapting to co...
  </details>

- **2026-07-27** — Muna Alebri, Noëlle Rakotondravony, Yassine Bechqito et al. — [Designing Within the Lines: Practitioners' Perspectives and Visualisation Tool Evaluation in the Arabic Context](http://arxiv.org/abs/2607.24571v1)
  <details><summary>📄 Abstract</summary>
  Design guidelines and best practices serve as references that support designers throughout the visualisation design process. While considerable effort has identified the elements that contribute to effective data visualisations, little attention has been paid to how language (scripts and reading direction), tool support, and cultural context also shape design decisions. As a result, assumptions of homogeneity persist, with visualisation practices predominantly benefiting users of English and lef...
  </details>

- **2026-07-27** — Sriharshaa S, Sangeetha Sivanesan, Jaya Nirmala S — [Systematic Analysis of Large Language Models and Transformer-Based Machine Translation for English-Tamil and Tamil-English Across Diverse Datasets](http://arxiv.org/abs/2607.24515v2)
  <details><summary>📄 Abstract</summary>
  The challenge of Machine Translation for low resource languages such as Tamil is primarily caused by the restricted amount of parallel data for these languages, as well as their substantial amount of domain variation and morphological complexity. This research presents the comprehensive evaluation of the performance of several multilingual translation models on English-Tamil and Tamil-English translations across multiple datasets: NTREX, EnTamV2, WikiMatrix and PMIndia. This study evaluates supe...
  </details>

- **2026-07-27** — Jinhao Zhang, Zeyu Liu, Zicheng Yan et al. — [Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension](http://arxiv.org/abs/2607.24887v1)
  <details><summary>📄 Abstract</summary>
  Existing theories of neural-network width characterize asymptotic limits, but provide limited guidance on whether an expansion direction identified from finite training data remains beneficial on unseen data. We study this problem for function-preserving residual expansion and introduce the effective alignment dimension, a measurable quantity describing the signal-noise geometry of activation gradients. By deriving the exact mean and variance of the inner product between independently estimated ...
  </details>

- **2026-07-27** — Guo Tang, HongJie Luo, Tianxu Wang et al. — [PRISM: Prompt Refinement via Image-grounded Self-rewarding Mechanism for Text-to-Image Generation](http://arxiv.org/abs/2607.24353v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image generation models can synthesize high-quality images from natural language descriptions, but their performance remains highly sensitive to prompt formulation. Existing prompt optimization methods mainly rely on text-side rewriting, prompt expansion, or external reward signals, offering limited image-grounded diagnosis and weak support for learning reusable optimisation policies. In this paper, we propose PRISM, a Prompt Refinement framework via Image-grounded Self-rewarding Mechani...
  </details>

- **2026-07-27** — Mingxuan Sun — [CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models](http://arxiv.org/abs/2607.24312v1)
  <details><summary>📄 Abstract</summary>
  Document-level relation extraction (DocRE) aims to extract relations among multiple entities across extended contexts while maintaining consistency across predicted triples. Although large language models (LLMs) show remarkable reasoning capabilities in information extraction, their predictions are typically generated independently for each candidate triple and may violate fundamental relational constraints such as transitivity, symmetry, and functional uniqueness, leading to contradictory and u...
  </details>

- **2026-07-27** — Shuo Wang, Fang Xi, Wenyuan Huang et al. — [KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems](http://arxiv.org/abs/2607.24260v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM systems increasingly rely on knowledge-selection processes that produce high-value structured priors, such as ranked evidence, graph topology, multimodal alignment, and confidence signals. Yet LLM serving remains fundamentally oblivious to this rich structure: once such signals are serialized into a prompt, the backend observes only a flat token sequence, forcing dense and uniform consumption of the full key-value (KV) state during decoding. We term this architectural mismatch the Kno...
  </details>

- **2026-07-27** — Shengyi Wang, Niantong Li, Guangzheng Hu et al. — [FilmBench: A Film-Grade Benchmark for Cinematic Video Generation](http://arxiv.org/abs/2607.24241v1)
  <details><summary>📄 Abstract</summary>
  Progress in video generation keeps narrowing the visual gap between AI-generated and professionally produced footage, yet most benchmarks still draw prompts from web sources or LLM templates and score them with untrained, generic multimodal models. More fundamentally, their evaluation taxonomies remain rudimentary (overall visual quality, coarse text alignment and temporal smoothness) rather than the professional Cinematic Language criteria by which films are actually made and judged, so they as...
  </details>

- **2026-07-27** — Songyue Cai, Lianyu Wang, Shan Gu et al. — [Strategy-Aware Parameter-Efficient Adaptation for LLM-based Auto-Bidding](http://arxiv.org/abs/2607.24232v1)
  <details><summary>📄 Abstract</summary>
  Advertising bidding has evolved from manual strategies to auto-bidding systems better adapted for large-scale, dynamic auction environments. While recent advances in Large Language Models (LLMs) offer strong reasoning for auto-bidding, existing methods suffer from shallow trajectory-text interactions and require costly fine-tuning, hindering the efficient use of pretrained knowledge under diverse constraints. To address these challenges, we propose SAGE, a novel Strategy-aware Auto-bidding frame...
  </details>

- **2026-07-27** — Pengyu Xie, Rongjia Zhou, Zhilin Ou et al. — [TCellAlign: Cross-study T-cell Populations Alignment with Nomenclature-Guided Multi-Agent Workflow](http://arxiv.org/abs/2607.24093v1)
  <details><summary>📄 Abstract</summary>
  Cell type standardization plays a central role in integrating biological knowledge across single-cell studies. While standardized resources (e.g., Cell Ontology, Nomenclature Frameworks) provide unified vocabularies of cell populations, scientific publications and public datasets continue to use heterogeneous study-specific labels, making cross-study comparison difficult even when biologically equivalent cell populations are described. In this work, we are the first to formulate this challenge a...
  </details>

- **2026-07-27** — Michael Girstl, Alexander Mattick, Christopher Mutschler — [Constrained Reinforcement Learning Using Successor Representations](http://arxiv.org/abs/2607.24057v1)
  <details><summary>📄 Abstract</summary>
  Real-world Reinforcement Learning depends on the ability to formulate safety constraints into a policy. A common way to model such constraints is to introduce an additional cost signal in the Markov Decision Process, which notifies the agent of unwanted behavior independently of the reward signal. Unfortunately, current methods are hard to adapt to changes in the cost function introduced by, e.g., domain shift or obstacles moving over time. The lack of adaptability means that policies are too un...
  </details>

- **2026-07-27** — Jiyu Wei, Di Hong, Zhanjie Zhang et al. — [A Cyclic Adaptation-Generalization Framework with Uncertainty-Guided Self-Paced Learning for Long-Term Brain-Machine Interfaces](http://arxiv.org/abs/2607.24031v1)
  <details><summary>📄 Abstract</summary>
  Brain-Machine Interfaces (BMIs), which link the brain to external devices, hold great potential in rehabilitation, human performance augmentation, and human-centered robotics. However, invasive BMIs face a critical challenge for long-term deployment due to neural drift, which degrades decoding performance over time and necessitates frequent recalibration. Existing methods designed to mitigate neural drift typically rely on either domain adaptation (DA) or domain generalization (DG) alone and oft...
  </details>

- **2026-07-27** — Hao Yang, Jin Wang, Xuejie Zhang — [DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models](http://arxiv.org/abs/2607.23944v1)
  <details><summary>📄 Abstract</summary>
  Human visual reasoning typically follows a coarse-to-fine attention process, starting from global scene understanding and gradually focusing on question-relevant regions. However, multimodal large language models may deviate from this pattern due to attention drift and the underutilization of visual evidence, which can lead to hallucinations. To mitigate these issues, this study proposes a Dual-Indicator Guided Contrastive Alignment (DICA), which tracks two information-theoretic indicators durin...
  </details>

- **2026-07-27** — Stefan Richter, Alberto Giammarino, Guillem Torrente et al. — [Bridging Reinforcement Learning and Optimal Control via Feasible Action Mapping](http://arxiv.org/abs/2607.23930v1)
  <details><summary>📄 Abstract</summary>
  Operating constrained dynamical systems requires controllers to efficiently solve complex tasks while enforcing recursive feasibility and safety constraints. To address these competing requirements, we present Feasible Action for Optimal Control (FAOC), a novel control framework integrating Reinforcement Learning (RL) and Optimal Control (OC). The key contribution is a computationally efficient, optimization-based mapping algorithm that transforms the RL agent's action from a static abstract set...
  </details>

- **2026-07-27** — Roberto Spinelli, Thiago C. Martins — [Embodied GPT-5.1: Evidence of a World Model?](http://arxiv.org/abs/2607.23899v1)
  <details><summary>📄 Abstract</summary>
  This exploratory study examines whether a large multimodal language model, GPT-5.1, can serve as the high-level controller of a physical mobile robot despite having no prior embodiment, no training in simulated environments, and no exposure to sensorimotor experience. Using only low-resolution first-person images and a discrete action set, the model was tasked with navigation and object-directed behaviors such as locating and contacting a target toy. Across multiple trials, GPT-5.1 demonstrated ...
  </details>

- **2026-07-26** — Masoud Badiei Khuzani, Sharath Honnaiah, Atiq Islam et al. — [A Coulomb Particle Model for Learning Kernel Attention in Transformers](http://arxiv.org/abs/2607.23869v1)
  <details><summary>📄 Abstract</summary>
  Randomized features provide a scalable approximation to kernel machines, but their performance depends strongly on the choice of feature distribution. We propose a particle-based method that learns this distribution by optimizing kernel-target alignment while regularizing particles with a Riesz/Coulomb repulsive potential. The resulting Hamiltonian yields diverse, task-adaptive random features and admits a mean-field description through a McKean--Vlasov equation. We instantiate the method in lin...
  </details>

- **2026-07-26** — Xianghao Jiao, Ruoyu Chen, Wei Wang et al. — [Consistent Evidence, Robust Recognition: Faithful Attribution Regularization under Geometric Transformations](http://arxiv.org/abs/2607.23835v1)
  <details><summary>📄 Abstract</summary>
  Attribution methods are widely used to characterize the evidence underlying model predictions, yet their potential to improve model behavior remains underexplored. Attribution inconsistency under label-preserving geometric transformations may indicate transformation-sensitive evidence reliance, motivating attribution regularization. However, such supervision is valid only when attribution faithfully reflects the evidence driving predictions. Existing self-supervised methods typically align gradi...
  </details>

- **2026-07-26** — Chenghao Wu, Kesha Ou, Xiaolei Wang et al. — [ClawRec: A Claw-Native Recommender System](http://arxiv.org/abs/2607.23779v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems have become integral to navigating the modern digital ecosystem. Yet most deployed systems remain confined within single-platform boundaries, observing localized interaction traces and ranking items from isolated candidate spaces. This design is poorly suited to real-world tasks that unfold through searches, content consumption, and comparisons across multiple information sources. Claw-style personal agents, with persistent access to authorized cross-platform context, create ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 76 papers

- **2026-07-29** — Fethi Bencherki, Anders Rantzer — [Minimax adaptive control for finite sets of positive linear systems](http://arxiv.org/abs/2607.26816v1)
  <details><summary>📄 Abstract</summary>
  We present a minimax adaptive control framework for discrete-time positive linear systems with parametric uncertainty and adversarial disturbances. The uncertainty in the system dynamics is assumed to lie in a finite set of possible plants. We formulate the problem as a dynamic game between the controller, which minimizes the cost, and an adversary, which selects both the disturbances and the plant dynamics to maximize the cost. An equivalent reformulation of the original game transforms the pro...
  </details>

- **2026-07-29** — Jindong Yang, Han Fang, Weiming Zhang et al. — [FARI: Robust One-Step Inversion for Watermarking in Diffusion Models](http://arxiv.org/abs/2607.26723v1)
  <details><summary>📄 Abstract</summary>
  Inversion-based watermarking is a promising approach to authenticate diffusion-generated images, yet practical use is bottlenecked by inversion that is both slow and error-prone. While the primary challenge in the watermarking setting is robustness against external distortions, existing approaches over-optimize internal truncation error, and because that error scales with the sampler step size, they are inherently confined to high-NFE (number of function evaluations) regimes that cannot meet the...
  </details>

- **2026-07-29** — Linyu Li, Zhi Jin, Yichi Zhang et al. — [Knowledge before Reasoning: EC-Reason-Bench, a Training-Free Diagnostic Benchmark for LLM Enzyme Classification](http://arxiv.org/abs/2607.26397v1)
  <details><summary>📄 Abstract</summary>
  Enzyme function prediction is a hierarchical, knowledge-intensive form of protein function classification. Existing benchmarks expose an anomaly: general LLMs often get the coarse first level right, yet once asked for a complete EC number their accuracy at levels two through four drops to almost zero, while specialized models and tools stay usable. We propose EC-Reason-Bench, a training-free, diagnostic evaluation protocol built to answer two questions: why general LLMs score close to nothing on...
  </details>

- **2026-07-29** — Álvaro Díaz-Laureano, Roger Marí, Elías Masquil et al. — [SeasonStereo: Robust Dense Stereo Matching for Multi-Date Satellite Imagery via Generative AI](http://arxiv.org/abs/2607.27139v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D reconstruction from satellite imagery typically relies on near-simultaneous stereo pairs, limiting its applicability to diachronic settings where multi-date images exhibit varying seasonal and illumination conditions. Training dense stereo matching models robust to appearance changes is a long-standing challenge, as aligned multi-date imagery and ground-truth geometry are costly to obtain at scale. We propose SeasonStereo, a scalable framework that addresses disparity estimation from...
  </details>

- **2026-07-29** — Siddharth Vohra — [Hearsay: Vision-Language Medical Diagnoses Without an Image](http://arxiv.org/abs/2607.26886v1)
  <details><summary>📄 Abstract</summary>
  When asked to describe a medical image that was never attached, frontier vision-language models do not abstain: they confabulate a diagnosis. We show that this confabulation is not random. It is structured by who the patient is said to be. Across chest X-ray, brain MRI, and dermatology, Claude Opus-4.7, GPT-5.4, and Gemini-3.1-Pro are each queried with only a demographic descriptor and no image, and changing the descriptor systematically shifts the diagnosis returned. Claude concentrates sharply...
  </details>

- **2026-07-29** — Ruikang Zhang, Shuo Wang, Qi Su — [From Representations to Behaviors: Exploring the Person-Situation-Behavior Triad in LLMs](http://arxiv.org/abs/2607.26853v1)
  <details><summary>📄 Abstract</summary>
  Human personality theories characterize traits not as isolated attributes captured by a single score, but as stable individual tendencies expressed through the interplay among persons, situations, and behaviors. Existing studies of personality-related behavior in LLMs have primarily focused on outputs elicited under personality conditioning, characterizing observable trait-related expressions while lacking mechanistic evidence for the existence of internal personality-related representations, th...
  </details>

- **2026-07-29** — Ruxi Gu, Zhenliang Zhang, Wei Wang — [ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models](http://arxiv.org/abs/2607.26455v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in knowledge acquisition and reasoning, yet their ability to retain previously acquired knowledge under repeated updates remains insufficiently understood. Existing evaluation paradigms primarily focus on single-step reasoning or static knowledge editing, which fail to capture the temporal dynamics of knowledge retention and degradation during continual model modification. In this work, we propose ForgetBench, a benchmark designe...
  </details>

- **2026-07-29** — Bilgehan Erman, Andrea Francini, Nikos Papadis — [Assurance-Scoped Reliability for Agentic Networks: Capturing the State That Matters](http://arxiv.org/abs/2607.26953v1)
  <details><summary>📄 Abstract</summary>
  Agentic networks transform accepted intents into operational services through autonomous reasoning, adaptive planning, tool use, and cross-domain coordination, but these capabilities introduce failure modes that conventional reliability measures do not fully capture. An accepted intent may still be carried out incorrectly, for example because the system acts on stale information, repeats an external action, applies only part of a change, or enters a fallback mode that quietly relaxes policy enfo...
  </details>

- **2026-07-29** — Jialiang Li, Yuhan Wang, Haojun Li et al. — [Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations](http://arxiv.org/abs/2607.26809v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robotic manipulation requires robots to perform diverse tasks in open-world environments while improving their skills over time. Despite recent progress in robotic manipulation, existing systems still primarily acquire manipulation skills in a static manner, where capabilities are learned for specific tasks or settings rather than adaptively evolving through physical interaction. Resembling how repeated practice enables humans to develop muscle memory, advanced manipulation profi...
  </details>

- **2026-07-29** — Joel Axel Wulff, Alexandre Lasheen — [Reinforcement Learning applied to Optimization of LHC beams in the CERN Proton Synchrotron](http://arxiv.org/abs/2607.26697v1)
  <details><summary>📄 Abstract</summary>
  The longitudinal triple splitting in the CERN Proton Synchrotron (PS) is a key rf manipulation defining the 25 ns bunch spacing delivered to the Large Hadron Collider (LHC). We present an automated optimization of this manipulation based on machine learning. Successive manipulations with rf systems at multiple harmonics of the revolution frequency are performed in the PS. Each bunch injected from the PS Booster (PSB) is split into twelve bunches with ideally identical longitudinal beam parameter...
  </details>

- **2026-07-29** — Peter Kirgis, Sayash Kapoor, Andrew Schwartz et al. — [Can AI agents conduct open-ended AI research? Early evidence from two case studies](http://arxiv.org/abs/2607.27191v1)
  <details><summary>📄 Abstract</summary>
  Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. Current evaluations either test agents on narrow, verifiable tasks, which excludes open-ended research, or submit AI-generated papers to blind peer review, which is overstretched, stochastic, and suffers from poor review quality. We introduce a third way to measure progress towards AI R\&D automation. An agent takes on the central, open-ended ...
  </details>

- **2026-07-29** — Peter Tisnikar, Maja Swieczkowska, Benteng Ma et al. — [Partner Capability Estimation for Task-Agnostic Adaptation in Ad-Hoc Teamwork](http://arxiv.org/abs/2607.27177v1)
  <details><summary>📄 Abstract</summary>
  Effective collaboration with novel and diverse partners is a crucial skill for autonomous agents. Most current ad-hoc teamwork (AHT) approaches assume that agents will collaborate on a single, fixed task and that the partner's capabilities, their ability to successfully execute the desired action, are already known. In reality, a partner's true capabilities are often hidden, and human collaborators may act sub-optimally on tasks with multiple valid strategies. To address these limitations, we ex...
  </details>

- **2026-07-29** — Jiahao Weng — [Herding, Momentum, and Reversal in China's A-Share Market: An Agent-Based Network Model with Information Diffusion](http://arxiv.org/abs/2607.27063v1)
  <details><summary>📄 Abstract</summary>
  This study develops an agent-based financial market model to explain stock-price momentum and reversal through the joint effects of local herding and delayed information diffusion. Investors form heterogeneous Gaussian beliefs about the next-period price, choose among buying, selling, and remaining inactive, and revise their action probabilities in response to neighboring investors. The local interaction structure is represented by von Neumann and Moore lattices and is later replaced by Erdős--R...
  </details>

- **2026-07-29** — Jorge Sanchez Almeida, Angel R. Plastino, Sergio Guerra Arencibia et al. — [Constraining the shape of dark matter haloes using only starlight II. Tests of the technique with objects of known gravitational potential](http://arxiv.org/abs/2607.27001v1)
  <details><summary>📄 Abstract</summary>
  Under the collisionless cold dark matter (CDM) paradigm, galaxies with stellar masses below 10**(5-6) Msun are expected to preserve primordial cuspy dark matter (DM) profiles. Because baryonic feedback should be too weak to transform cusps into cores at these masses, such galaxies provide especially sensitive tests of DM physics. If cores are observed in these systems, they could indicate departures from CDM. To address this problem, Sanchez Almeida et al. (2025) introduced the Eddington Inversi...
  </details>

- **2026-07-29** — Philipp A. Guth, Karl Kunisch, Sergio S. Rodrigues et al. — [Dynamic output-feedback stabilization of uncertain linear dynamics via digital twins](http://arxiv.org/abs/2607.26995v1)
  <details><summary>📄 Abstract</summary>
  This work presents a digital twin framework for output-feedback stabilization and parameter identification in uncertain dynamical systems. A virtual model evolves in parallel with the physical process, assimilating measurement data in real time. By design, the digital twin reconstructs the system state and generates a stabilizing feedback, while model parameters are simultaneously inferred from data of the controlled dynamics using a Bayesian approach. Numerical results for the coupled physical-...
  </details>

- **2026-07-29** — Jinlan Liu, Zhiying Tu, Yongchao Xing et al. — [Dual-Path LLM Reasoning for Multimodal Few-Shot Knowledge Graph Completion](http://arxiv.org/abs/2607.26909v1)
  <details><summary>📄 Abstract</summary>
  Knowledge graph completion (KGC) aims to infer missing facts in knowledge graphs (KGs), thereby improving their completeness and supporting downstream intelligent applications. However, emerging entities and relations in real-world deployments make inductive KGC difficult, especially under few-shot and zero-shot settings. Multimodal information and Large Language Model (LLM)-derived priors can enrich sparse relational contexts, but they may also introduce noisy or hallucinated evidence. To addre...
  </details>

- **2026-07-29** — Poulami Ghosh, Preethi Jyothi — [Language Models are not Equally Robust to Non-Canonical Tokenization across Languages](http://arxiv.org/abs/2607.26831v1)
  <details><summary>📄 Abstract</summary>
  Despite the existence of exponentially many valid tokenizations for a given string, language models operate on a single canonical sequence deterministically produced by the tokenizer, leaving the broader tokenization space largely uncharacterized. In this paper, we investigate this overlooked space by studying the behavior of language models under non-canonical tokenizations across diverse languages. For English, prior work shows that models are largely invariant to alternative tokenizations tha...
  </details>

- **2026-07-29** — Alexander Kozachok, Ilya Latyshev, Evgeny Karpulevich et al. — [Searching for Robust Augmentations to Improve Out-of-Domain Generalization in Dermoscopic Skin Cancer Classification](http://arxiv.org/abs/2607.26765v1)
  <details><summary>📄 Abstract</summary>
  Background/Objectives: Dermoscopic skin lesion classifiers often lose accuracy under domain shift across imaging devices, illumination, and capture artifacts. We study how data augmentation improves the robustness of a binary malignant-versus-non-malignant classifier, with emphasis on out-of-domain (OOD) generalization. Methods: Single augmentations, photometric combinations, and composite policies were searched on a multi-source ISIC Archive collection with Derm7pt, using a ConvNeXt-Large backb...
  </details>

- **2026-07-29** — Haijun Zhang, Zhuojun Duan, Zijun Wu et al. — [Harnessing Large Language Models for Intelligent Resource Allocation in the Internet of Everything](http://arxiv.org/abs/2607.26602v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of the Internet of Everything (IoE) is accelerating the adoption of intelligent applications. However, the massive number of connected devices generates diverse and heterogeneous tasks, which pose increasing challenges for dynamic resource scheduling in IoE environments. Using their superior semantic understanding and reasoning capabilities, Large Artificial Intelligence Models (LAIMs) demonstrate significant potential to handle complex scheduling scenarios and improve reso...
  </details>

- **2026-07-29** — Ignacio M. De la Jara, Cristian Rodriguez-Opazo, Stephen Gould et al. — [Level, Sharpness, and Corpus: Why Zero-Shot OOD Detector Rankings Do Not Transfer](http://arxiv.org/abs/2607.26582v1)
  <details><summary>📄 Abstract</summary>
  Selecting a zero-shot out-of-distribution (OOD) detector for a new deployment is typically based on benchmark rankings, implicitly assuming that the highest-ranked detector will transfer across domains. We show that this assumption does not hold. Through a controlled portability audit across seventeen in-distribution datasets, three vision-language models, and seven representative zero-shot OOD detectors, we find that detector rankings reverse across deployments, every detector exceeds $80\%$ FP...
  </details>

- **2026-07-29** — Keke Huang, Yik Yu Ng, Laks V. S. Lakshmanan et al. — [Parameterized Fair Resource Allocation under Diversity Constraints](http://arxiv.org/abs/2607.26485v1)
  <details><summary>📄 Abstract</summary>
  Resource allocation across multiple agent groups arises in many applications including e-commerce recommendation systems, housing assignment, and course allocation, and is commonly formulated as an optimization problem with diversity constraints to ensure group fairness. Existing approaches typically enforce these constraints as hard conditions, which overly restrict the feasible solution space and often lead to suboptimal allocations.   In this paper, we propose PRA, a parameterized framework f...
  </details>

- **2026-07-29** — Javier C. Weddington, Bence P. Ölveczky, Stephen A. Baccus — [Reinforcement Learning on Cost-Constrained Quadrupedal Hardware](http://arxiv.org/abs/2607.26434v1)
  <details><summary>📄 Abstract</summary>
  Deploying learned control policies on low-cost robotic platforms introduces transport latencies and noisy motor feedback that systematically widens the sim-to-real gap. The chasm of simulation to deployment in hardware lies in the delay of the actuator reaching the commanded position. On platforms such as the Mini Pupper 2, a measured > $50 ms transport delay transforms the locomotion task from a standard Markov decision process into a partially observable one. In this paper, we take a biologica...
  </details>

- **2026-07-29** — Hari Dahal, Rongjie Lai, Yangyang Xu — [Scalable Dynamic Optimal Transport via Distributed Linearized ADMM](http://arxiv.org/abs/2607.26407v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we address two fundamental challenges in the numerical solution of dynamic opti- mal transport (OT) problems. The first challenge arises when the initial and/or terminal densities approach zero and no positive lower bound is available. In this regime, conventional methods may become unstable or computationally inefficient, since the Lipschitz constant of the objective can scale like the reciprocal of the cube of the density. As a result, near-zero regions may lead to slow converge...
  </details>

- **2026-07-29** — Kashif Imteyaz, Mohammad Rashidujjaman Rifat, Divya Ramesh et al. — ["Nobody Did This": Contribution, Originality, and Accountability in Agent-Mediated Collaboration](http://arxiv.org/abs/2607.26387v1)
  <details><summary>📄 Abstract</summary>
  Collaborative knowledge work is changing in ways that go beyond disclosure or transparency. LLM agents are now embedded in how teams research, design, write, and decide: mediating between members, synthesizing inputs, reformulating ideas, and drafting shared outputs. They do not only facilitate collaboration; they operate within the workflow at the moment contributions are being formed. In doing so, they risk undermining the social conditions under which contributions can be witnessed, attribute...
  </details>

- **2026-07-28** — Conor McCauley, Zeliang Kan, Jason Martin — [IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](http://arxiv.org/abs/2607.25987v2)
  <details><summary>📄 Abstract</summary>
  When a language model receives conflicting instructions from different priority levels, which one does it actually follow? This question lies at the heart of reliable LLM deployment. Existing benchmarks answer this only partially, often focusing on a single hierarchy edge or adapting public datasets with limited tool-use coverage. We present IH-Benchmark, a conflict-centered benchmark for instruction-hierarchy robustness across direct system-user conflicts (S>U) and tool-mediated user-tool (U>T)...
  </details>

- **2026-07-28** — Zihan Chen, Di Zhu, Lei Nico Zheng — [When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses](http://arxiv.org/abs/2607.26348v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as synthetic users, stand-ins for human respondents whose simulated answers feed product, policy, and market decisions. We ask when this substitution is valid and when it fails, and package the answer as an evaluation framework for intelligent synthetic-user systems. A single protocol, run across four models spanning two families and an 8B-to-frontier capability range, is applied to two independent domains of real human-response data: U.S. gener...
  </details>

- **2026-07-28** — Lorenzo Cima, Alessio Miaschi, Amaury Trujillo et al. — [Contextualized Counterspeech Can Be More Persuasive Than Generic Counterspeech](http://arxiv.org/abs/2607.26236v1)
  <details><summary>📄 Abstract</summary>
  AI-generated counterspeech offers a scalable and effective strategy to mitigate online toxicity by promoting more constructive dialogue. Yet, existing approaches adopt a generic, one-size-fits-all paradigm, overlooking the conversational context and characteristics of the targeted users. Here, we propose and evaluate multiple strategies for generating contextualized counterspeech that is adapted to the moderation setting and personalized to the moderated user. In detail, we explore a range of co...
  </details>

- **2026-07-28** — Quim Motger, Marc Oriol, Jordi Marco et al. — [Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges](http://arxiv.org/abs/2607.26212v1)
  <details><summary>📄 Abstract</summary>
  Multi-Agent Debate (MAD) is a promising paradigm for improving the accuracy and robustness of Large Language Model (LLM)-based agentic systems. It enables multiple agents to exchange arguments, critique each other's outputs, and iteratively converge towards a solution. However, research remains fragmented, with inconsistent terminology and no rigorous synthesis of MAD design dimensions. We present a systematic literature review characterizing 141 primary studies on MAD. We derive a three-dimensi...
  </details>

- **2026-07-28** — Jiamin Xu, Cong Wang, Zheng Dong et al. — [WildShadowRemover: In-the-Wild Video Shadow Removal via Detail-Preserving Video Diffusion Models](http://arxiv.org/abs/2607.26203v1)
  <details><summary>📄 Abstract</summary>
  Video shadow removal in the wild remains challenging due to complex illumination, diverse shadow appearances, and limited training data. Despite its importance to numerous vision and graphics applications, it remains largely unexplored in unconstrained real-world scenarios. To address this gap, we present WildShadowRemover, a framework that adapts a pretrained video diffusion model for robust video shadow removal via LoRA fine-tuning. To preserve fine image details while retaining the model's po...
  </details>

- **2026-07-28** — Mojdeh Rahmanian, Ashkan Sami, Yanchao Yu — [Large Language Models for Software Engineering Diagrams: A Systematic Review of UML and ER modelling](http://arxiv.org/abs/2607.26100v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied to diagram-based software and data modelling. Among various modelling notations, UML and entity-relationship (ER) diagrams are the most widely adopted for software modelling and data modelling, respectively. Recent literature has investigated various applications of LLMs in diagram modelling; however, their effectiveness and limitations have not been extensively discussed. This systematic literature review analyses 64 studies published betwee...
  </details>

- **2026-07-28** — Conor McCauley, Zeliang Kan, Jason Martin — [\textsc{IH-Benchmark}: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](http://arxiv.org/abs/2607.25987v1)
  <details><summary>📄 Abstract</summary>
  When a language model receives conflicting instructions from different priority levels, which one does it actually follow? This question lies at the heart of reliable LLM deployment. Existing benchmarks answer this only partially, often focusing on a single hierarchy edge or adapting public datasets with limited tool-use coverage. We present IH-Benchmark, a conflict-centered benchmark for instruction-hierarchy robustness across direct system-user conflicts (S>U) and tool-mediated user-tool (U>T)...
  </details>

- **2026-07-28** — Abhishek Pillai, Samir Kumar Nayak, Yuan Chen — [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](http://arxiv.org/abs/2607.26041v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observ...
  </details>

- **2026-07-28** — Weitao Li, Gong Cheng — [Generator-Aligned Representation Interfaces for Diagnostic Soft Equivariance](http://arxiv.org/abs/2607.25988v1)
  <details><summary>📄 Abstract</summary>
  Exact-equivariant architectures typically encode prescribed group actions in specialized operators, which can complicate their reuse with generic backbones and across data modalities. We introduce the Generator-Aligned Representation Interface (GARI), a representation-level design principle that exposes selected transformation generators to a generic sequence backbone through aligned canonical and generator-induced views. We formalize the resulting behavior using a probe-specific soft-equivarian...
  </details>

- **2026-07-28** — Rui Yang, Weihao Xuan, Yi Lin et al. — [Evaluating Multi-Turn Multimodal Diagnostic Reasoning on Challenging Real-World Clinical Cases](http://arxiv.org/abs/2607.25933v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnostic evaluation should not only assess whether models can provide correct diagnoses, but also reflect the realities of clinical practice, including progressive disclosure of multimodal information, dynamic updating of diagnostic hypotheses, and continuous refinement of clinical reasoning. However, existing evaluations of multimodal large language models (MLLMs) typically rely on single-turn or isolated tasks, making it difficult to fully capture the complexity of real-world clinic...
  </details>

- **2026-07-28** — Yi Xu, Cheng Chen, Mufan Cao — [OrthKD: Extracting Generalized Clinical Knowledge from Heterogeneous Teachers for Lightweight Deployment](http://arxiv.org/abs/2607.25545v1)
  <details><summary>📄 Abstract</summary>
  Deploying diabetic retinopathy (DR) screening models in primary care requires edge-efficient systems that remain accurate, safe, and reliable under domain shift. Multi-teacher knowledge distillation (KD) is a natural compression strategy, but existing approaches largely assume that all teachers provide equally trustworthy supervision. In our setting, this assumption fails: a strong CNN teacher (EfficientNet-B3, 0.876 QWK) and a weaker Transformer teacher (Swin-Base, 0.830 QWK) are complementary,...
  </details>

- **2026-07-28** — Zheng Tong, Yang Liu, Wanshu Fan et al. — [Agentic AI in medicine: architectures, applications, evaluation, and challenges for clinical translation](http://arxiv.org/abs/2607.25489v1)
  <details><summary>📄 Abstract</summary>
  Large language models and multimodal foundation models are enabling medical artificial intelligence (AI) systems to move beyond isolated prediction and undertake multistep clinical tasks that require planning, tool use, memory, iterative correction, and coordination among specialized agents. However, the scope of agentic AI in medicine remains unsettled, and current evaluation practices are not yet aligned with the requirements of clinical use. We conducted a scoping review with systematic evide...
  </details>

- **2026-07-28** — Yuan Yin, Elias Ramzi, Marc Lafon et al. — [Pictura: Perspective-View Self-Play at Scale for Driving](http://arxiv.org/abs/2607.26005v1)
  <details><summary>📄 Abstract</summary>
  Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A common fix, distilling the privileged policy into a camera-input student, leaves the student imitati...
  </details>

- **2026-07-28** — Malena Loza, David Chushig-Muzo, Eva Milara et al. — [Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation Models](http://arxiv.org/abs/2607.26000v1)
  <details><summary>📄 Abstract</summary>
  Tabular Foundation Models (TFMs) have emerged as novel approaches for tabular predictive tasks, demonstrating competitive predictive performance to ensemble tree-based models. Most TFMs are trained and evaluated on independent and identically distributed data, but this assumption changes in real-world scenarios due to distribution shifts, which compromise the robustness of models. Limited research has been conducted of TFMs under distribution shifts. We present an empirical evaluation of Out-Of-...
  </details>

- **2026-07-28** — Keyu Zhang, Vadim Safronov, Andrew Martin — [Stemma: Induced Decision Regions Reveal LLM Provenance](http://arxiv.org/abs/2607.25880v1)
  <details><summary>📄 Abstract</summary>
  LLM provenance testing asks whether a suspect LLM belongs to the same lineage as a source. Existing black-box methods largely infer this relationship from response-level characteristics, but these characteristics may shift under adaptation or deployment even when the underlying meaning remains unchanged, weakening the reliability of provenance evidence. To address this limitation, we introduce induced decision regions by mapping open-ended outputs into a finite decision space, thereby abstractin...
  </details>

- **2026-07-28** — Du Yin, Xiachong Lin, Yue Tan et al. — [A2TTA: Anchored-and-Agile Test-Time Adaptation for Evolving Traffic Sensor Networks](http://arxiv.org/abs/2607.25875v1)
  <details><summary>📄 Abstract</summary>
  Traffic forecasting is important for efficient traffic management and route planning in smart cities. Existing traffic forecasting studies typically assume fixed sensor graphs, overlooking the continuous evolution of real-world traffic networks, e.g., ongoing road network construction and evolving human mobility patterns. These dynamic changes can substantially degrade conventional forecasting models, motivating test-time adaptation (TTA) to efficiently adapt pretrained models during deployment....
  </details>

- **2026-07-28** — Weixin Liu, Juming Xiong, Congning Ni et al. — [DRIFT: Direct-Recursive Intervention-Conditioned Forecasting of ICU Physiological Trajectories](http://arxiv.org/abs/2607.25864v1)
  <details><summary>📄 Abstract</summary>
  Many time-series forecasts depend not only on prior observations but also on actions specified during the forecast period. In intensive care units (ICUs), future vital signs and laboratory values are influenced by treatments such as vasopressors. However, models that predict the full future sequence all at once make little use of these treatments, whereas autoregressive models can accumulate errors. We introduce DRIFT, a hybrid framework in which a direct model produces the primary forecast and ...
  </details>

- **2026-07-28** — Philipp Gessler, Alessandro Pignedoli, Alexander Neuhaus et al. — [Topological Classification of Non-Normalizable Vector Fields](http://arxiv.org/abs/2607.25848v1)
  <details><summary>📄 Abstract</summary>
  Topological classification of physical vector fields conventionally relies on field normalization and homotopy-based invariants. However, when field amplitudes vanish, normalization becomes ill-defined, preventing a direct topological characterization. Here, we introduce a general framework for the topological classification of non-normalizable $n$-dimensional vector fields with compactifiable base spaces by transforming them into $(n+1)$-dimensional normalized vector fields. This construction e...
  </details>

- **2026-07-28** — Jean-Philippe Bouchaud, Pierre Bousseyroux, Tomas Espana et al. — [Spectra of high-dimensional Spearman correlation matrices under scale-mixture dependence](http://arxiv.org/abs/2607.25486v1)
  <details><summary>📄 Abstract</summary>
  We study the asymptotic spectral properties of high-dimensional Spearman correlation matrices for scale-mixture data. We consider observations of the form $x_t=σ_t ξ_t \in \mathbb{R}^N,$ where the coordinates of $ξ_t$ are i.i.d.\ and the scalar mixture variable $σ_t$ is shared by all coordinates. Under natural symmetry assumptions, the coordinates of $x_t$ are pairwise uncorrelated in both the Pearson and Spearman sense. Nevertheless, they are not independent when the mixture variable is non-deg...
  </details>

- **2026-07-28** — Frank Schweitzer — [Resilience: Understand Breakdown, Foster Recovery, and Choose the Right Perspective](http://arxiv.org/abs/2607.25458v1)
  <details><summary>📄 Abstract</summary>
  Resilience denotes the capacity of a system to withstand shocks and to recover from them. We distinguish between two different types of dynamics. The first allows for a separation between phases of normalcy and phases of rapid breakdown followed by slow recovery. The second applies to volatile organizations in which such phases are intertwined. Breakdown is often self-inflicted. Situation awareness is impaired by psychological mechanisms that lead to incorrect expectations regarding societal dyn...
  </details>

- **2026-07-28** — Masaki Satoh — [HOME: Robust Hough-space Matching Method for Structured and Textureless Videos](http://arxiv.org/abs/2607.25389v1)
  <details><summary>📄 Abstract</summary>
  Visual front-ends for robotic localization typically rely on point-based features such as Oriented FAST and Rotated BRIEF (ORB), which frequently fail in structured environments dominated by strong linear structures or textureless surfaces. While line-based Simultaneous Localization and Mapping (SLAM) systems mitigate this by utilizing line segments, conventional line extraction and description algorithms are computationally prohibitive for real-time edge robotics. To address this fundamental bo...
  </details>

- **2026-07-28** — Jintian Ji, Xingsu Li, Songhe Feng — [Breaking the Periodicity Assumption: Robust Tensorial Multi-View Clustering via Graph-Spectral Low-Rank Learning](http://arxiv.org/abs/2607.25295v1)
  <details><summary>📄 Abstract</summary>
  Tensorial multi-view clustering (TMC) has achieved strong performance due to its ability to capture high-order correlations across multiple views. Most existing t-SVD-based TMC frameworks apply the Fast Fourier Transform (FFT) along the sample mode to impose frequency-domain low-rank constraints. However, we reveal that this widely adopted design critically relies on an implicit ``periodicity assumption'' induced by the sample arrangement. When samples are ordered by class, neighboring indices t...
  </details>

- **2026-07-27** — Md Ashikur Rahman, Md Arifur Rahman, Niamul Hassan Samin et al. — [Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls](http://arxiv.org/abs/2607.24343v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents act through structured tool calls whose arguments carry different risks. Untrusted content may safely influence an email body but should not determine a recipient, account, command, or credential. Existing statistical methods typically control risk over the entire action, allowing failures in rare, high-risk fields to be obscured by benign arguments. We introduce role-stratified per-field conformal risk control, a calibration layer that wraps any per-field detector and sets...
  </details>

- **2026-07-27** — Barbara Kitchenham, Sebastián Pizard, Lech Madeyski et al. — [Preliminary Guidelines for Using and Evaluating GenAI Tools to Support Systematic Literature Reviews](http://arxiv.org/abs/2607.24991v1)
  <details><summary>📄 Abstract</summary>
  Context: Generative AI (GenAI) and Large Language Models (LLMs) are increasingly used for academic tasks in software engineering and beyond, including systematic literature reviews (SLRs). However, while capable of summarizing text, there is no guarantee they can meet the rigour, reliability, and transparency that SLRs require. Objectives: To support researchers intending to conduct SLRs using GenAI or those conducting empirical studies evaluating how well GenAI supports SLR tasks. Methods: Firs...
  </details>

- **2026-07-27** — Zeyu Zhang, Xue Li, Iacer Calixto et al. — [Beyond Scale and Generation: Understanding Language Model-based Entity Matching](http://arxiv.org/abs/2607.24688v1)
  <details><summary>📄 Abstract</summary>
  Entity matching identifies records that refer to the same real-world entity. Language models can be adapted to this task through bi-encoder, cross-encoder, and generative matcher architectures. However, prior studies often conflate matcher architecture with differences in model backbone, model variant(reflecting different pretraining objectives), and model size, making it difficult to isolate the sources of performance gains. We address this issue through a controlled factorial study spanning th...
  </details>

- **2026-07-27** — Sebastià Nicolau, Adrià Molina, Oriol Ramos Terrades et al. — [Robust Interpretation of Historical Documents in Knowledge Graphs Through Query Inference and Execution](http://arxiv.org/abs/2607.24475v1)
  <details><summary>📄 Abstract</summary>
  The emergence of Large Language Models (LLMs) has redefined how users interact with information in digital environments. However, their widespread and often indiscriminate integration has raised significant concerns regarding reliability and trustworthiness issues that are particularly critical when accessing digital libraries and historical archives. How can one leverage the generalization capacity of an LLM without losing the level of accountability required for an archival institution? In thi...
  </details>

- **2026-07-27** — Florin Neagu — [Decentralised Consensus Learning Networks: SME Rotation Without Centralised Reward](http://arxiv.org/abs/2607.24416v1)
  <details><summary>📄 Abstract</summary>
  Centralised reward signals dominate modern AI learning systems, but they impose a single external definition of correct or valuable knowledge. We present a decentralised, consensus-based multi-agent learning framework in which expertise emerges through peer validation rather than prescribed reward. Agents update beliefs via weighted social consensus, while trust is allocated according to competence inferred from peer consistency instead of ground truth. Subject-matter expert (SME) status is assi...
  </details>

- **2026-07-27** — Tianyi Gao, Han Fang, Tianyi Ding et al. — [Mixture-of-Thought-Tokens: Unifying Perception and Reasoning for Free-form Multimodal Grounding](http://arxiv.org/abs/2607.24407v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models have made great progress in grounding tasks, yet existing methods still struggle to unify precise localization and complex reasoning. For one thing, text-based methods rely on coordinates or index prediction, severely limiting the perceptual capabilities of the model for dense visual objects. Meanwhile, latent token-based methods employ special tokens without inherent spatial references and use a decoding mechanism that lacks thinking steps, weakening high-level ...
  </details>

- **2026-07-27** — Yidong Huang, Tenglong Lu, Hanwen Kang et al. — [Aligning Heterogeneous DFT Datasets: A Graph Neural Network Approach to Cross-Functional Formation Energies](http://arxiv.org/abs/2607.24327v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous density functional theory (DFT) calculations, particularly plane-wave implementations, introduce systematic formation energy errors ranging from tens to hundreds of meV/atom, depending on the selection of exchange-correlation functionals, kinetic energy cutoffs, pseudopotentials, and dispersion corrections. As demonstrated by the MatPES dataset, identical structures can exhibit an average energy discrepancy of 107 meV/atom between PBE and r2SCAN calculations. Such method-dependent ...
  </details>

- **2026-07-27** — Tapan Parikh — [Tag Questions and the Generational Reversal of Sycophancy Across 45 Language Models](http://arxiv.org/abs/2607.23976v1)
  <details><summary>📄 Abstract</summary>
  Appending a two-word confirmation tag to a decision question -- "Is X the better choice?" versus "X is the better choice, right?" -- changes whether a language model endorses the choice. We measure this tag effect on 20 frozen, ground-truth-free decisions between two defensible options, counterbalanced so a model's own preferences cancel, scored by exact match on clamped yes/no replies -- no LLM judge, no embeddings. Across 45 models the effect spans +32% to -32% -- a 64-point swing on one word ...
  </details>

- **2026-07-27** — Yu Li, Wengan He, Wenhui Xu et al. — [Color Fundus Photography Analysis: Co-evolution of Data, Preprocessing, and Modeling toward Multimodal AI](http://arxiv.org/abs/2607.23972v1)
  <details><summary>📄 Abstract</summary>
  Color Fundus Photography (CFP) is a primary non-invasive imaging modality for large-scale screening of ophthalmic and systemic diseases. Existing surveys mainly summarize task-specific algorithms, datasets, or preprocessing techniques independently, lacking a unified perspective on their co-evolution with modern artificial intelligence. This review provides an integrated overview of CFP AI through the interplay of dataset evolution, preprocessing paradigms, and modeling frameworks. We show that ...
  </details>

- **2026-07-27** — Keyu Li, Jin Gao, Jialing Zhang et al. — [LU-500: A Logo Benchmark for Concept Unlearning](http://arxiv.org/abs/2607.24101v1)
  <details><summary>📄 Abstract</summary>
  Concept unlearning is increasingly used to limit the reproduction of protected or unsafe visual concepts in text-to-image models. Existing evaluations, however, mostly study targets that dominate the whole image, such as styles, broad object categories, or portrait-like identities, leaving company logos comparatively underexamined. Logos create a different failure mode: a small localized mark can carry the entire protected concept, must be visually precise to remain recognizable, and can be trig...
  </details>

- **2026-07-27** — Xueping Gao, Jianwei Yang, Qiang Yang — [Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](http://arxiv.org/abs/2607.24604v1)
  <details><summary>📄 Abstract</summary>
  Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee. We study the gap between finding a correct patch and retaining, verifying, and submitting it. A sealed five-seed study over 30 HumanEval repairs produces 900 three-revision trajectories. Under forced revision, current correctness with current traces falls from 0.820 after one revision to 0.673 after two, although ever-correct rises to 0.847. Two common-state studies use 2,430 branche...
  </details>

- **2026-07-27** — Ioannis Sarridis, Ioannis Kompatsiaris, Symeon Papadopoulos — [Face Age Verification Vulnerabilities Under Simple Appearance Manipulations](http://arxiv.org/abs/2607.24194v1)
  <details><summary>📄 Abstract</summary>
  Online platforms increasingly rely on automated age estimation systems to enforce minimum-age policies. Focusing on vision-based models designed for this task, concerns arise regarding their robustness to simple appearance changes that underage individuals may use to bypass such systems, such as drawing a mustache or applying lipstick. In this work, we present a systematic study of age verification robustness by simulating visual alterations that can be easily achieved by underage individuals. W...
  </details>

- **2026-07-27** — Khadija Rais, Abdelmadjid Benmachiche, Imene Soualmia — [Hybrid Artificial Potential Fields and Spatio-Temporal Transformers for Real-Time AUV Path Planning](http://arxiv.org/abs/2607.25056v1)
  <details><summary>📄 Abstract</summary>
  Autonomous Underwater Vehicles (AUVs) operate in complex, unstructured environments where efficient and safe path planning is critical for mission success and energy conservation. This paper presents a comprehensive comparative evaluation of thirteen path planning algorithms, ranging from classical graph-search methods (A*, Dijkstra) and sampling-based approaches (RRT*) to metaheuristics (PSO, GA, ACO, BCO) and learning-based architectures. Special emphasis is placed on a proposed hybrid approac...
  </details>

- **2026-07-27** — Hamid El Bahja, Jan C. Riedel, Peter Jung — [A Hybrid Physics-Informed Neural Network Framework for Subcritical and Supercritical Dynamics in Multi-Species Chemotaxis](http://arxiv.org/abs/2607.24949v1)
  <details><summary>📄 Abstract</summary>
  We study a two-species chemotaxis system that exhibits two qualitatively different regimes: subcritical dynamics, in which solutions remain smooth, and supercritical dynamics, in which strong aggregation may lead to finite-time blow-up. In the subcritical regime, we use a standard continuous-time physics-informed neural network (PINN) with alternating training for the coupled fields and show that it provides accurate and efficient approximations. In the supercritical regime, however, this formul...
  </details>

- **2026-07-27** — Jinjie Mai, Gordon Guocheng Qian, Willi Menapace et al. — [EgoPlay: Event-Triggered Video Editing for Egocentric Streams](http://arxiv.org/abs/2607.24560v1)
  <details><summary>📄 Abstract</summary>
  We introduce EgoPlay, an event-triggered video-to-video editor for egocentric streams, obtained by fine-tuning a pretrained V2V diffusion transformer on event-conditioned data built primarily from Ego4D. Given a monocular video and an event-triggered prompt of the form "when X happens, do Y," EgoPlay infers whether and when event X occurs, preserves pre-event frames, and applies edit Y only to the post-event continuation. Rather than cascading a separate event detector with an editor, EgoPlay le...
  </details>

- **2026-07-27** — Fangyijie Wang, Tanya Akumu, Zi Ye et al. — [Efficient Ultrasound Image Segmentation with Token-Conditioned Neural Cellular Automata](http://arxiv.org/abs/2607.24529v1)
  <details><summary>📄 Abstract</summary>
  Point-of-Care Ultrasound (POCUS) plays an important role in bedside diagnosis and clinical decision-making, particularly in resource-constrained settings. Recent deep learning methods have substantially improved ultrasound image segmentation, enabling accurate diagnosis and biometric estimation. However, their computational cost limits deployment on portable and low-resource devices. To address this challenge, we propose LiteAdaNCA-Net (LANCANet), a lightweight ultrasound segmentation framework ...
  </details>

- **2026-07-27** — Xiangbo Zhang, Xiaoxu Ma — [Grounding latent algorithm routing in transformer reasoning](http://arxiv.org/abs/2607.24471v1)
  <details><summary>📄 Abstract</summary>
  A central question in the in-context learning literature is whether transformers can organize episode-level adaptation around different inductive-bias families. We study this question in a controlled setting through latent algorithm routing: route-like behavior in which the solver-family preference changes with the latent data-generating regime while prompt form is held fixed, remains stable under nuisance perturbations, and is selectively influenced by targeted activation interventions without ...
  </details>

- **2026-07-27** — Dariusz Nowak-Nova — [Retrieval-Augmented Large Language Models as Components of Cognitive Computing architecture for Regulatory Knowledge Management](http://arxiv.org/abs/2607.24352v1)
  <details><summary>📄 Abstract</summary>
  The aim of this article is to verify whether integrating large language models (LLMs) with the Retrieval-Augmented Generation (RAG) architecture enables their transformation from standalone generative models into components of cognitive computing infrastructure with enhanced epistemic reliability. The study proposes an architectural approach based on locally deployed LLMs operating in on-premises environments without high-end GPU accelerators and examines their applicability in supporting regula...
  </details>

- **2026-07-27** — Zefan Qu, Zhenwei Wang, Gerhard Petrus Hancke et al. — [UMI3D: Robust 3D Generation on Unconstrained Multi-Image Inputs via Simultaneous Focus Cross-Attention Routing](http://arxiv.org/abs/2607.24298v1)
  <details><summary>📄 Abstract</summary>
  Recent 3D foundation models can generate high-quality assets from a single image, but degrade markedly on unconstrained multi-image inputs, often producing distorted geometry, over-smoothed textures, and chaotic colors. We argue that this failure stems not from limited model capacity, but from a mismatch between single-image cross-attention and the multi-image setting: existing models lack a principled way to decide which image each 3D voxel should trust at each denoising step. Revisiting recent...
  </details>

- **2026-07-27** — Wenbin Wang, Xiaotong Luo, Yuan Gao et al. — [RPG-VST: Robust Poisson-Gaussian Variance Stabilization for Blind RAW Denoising](http://arxiv.org/abs/2607.24291v1)
  <details><summary>📄 Abstract</summary>
  Variance stabilization with the generalized Anscombe transform (GAT) enables frozen Gaussian denoisers to process Poisson--Gaussian (PG) RAW noise, but its reliability depends on fitted shot/read-noise parameters. In blind single-image deployment, these parameters are estimated from low-texture RAW statistics that are often corrupted by residual texture, clipping, defective pixels, and read-noise floors. Such contamination yields heavy-tailed log-variance residuals, making ordinary least-squares...
  </details>

- **2026-07-27** — Thomas Monks, Alison Harper, Amy Heather et al. — [Generative Artificial Intelligence (GenAI) to convert images of queuing networks into verifiable simulation models: an open-weight LLM workflow approach](http://arxiv.org/abs/2607.24259v1)
  <details><summary>📄 Abstract</summary>
  Recent work has explored the use of Large Language Models (LLMs) to automate simulation model building, typically by generating executable code directly from natural language descriptions. However, this raises challenges for verification and reproducibility particularly for users without programming expertise. We propose Sketch2DES, a sketch-to-simulation workflow that converts diagrammatic representations of queuing networks into verifiable discrete-event simulation models using open-weight LLM...
  </details>

- **2026-07-27** — Guangyi Liu, Huan Zhao, Quanming Yao — [Falsifiable Commitment Planning for Self-Correcting Web Agents](http://arxiv.org/abs/2607.24167v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon web agents often go off track before final failure: a trajectory can remain locally plausible even after the current state, reused skill, or plan assumption no longer supports the user instruction. Existing agents can plan, reflect, or reuse experience, but their plans rarely specify the evidence under which an active step should still be trusted. We propose FCPAgent, a falsifiable commitment planning framework for robust long-horizon web agents. FCPAgent represents each plan step a...
  </details>

- **2026-07-27** — Ahmad Dkhan, Yazan Dayoub, Jana El Haj et al. — [Hierarchical THz Near-Field Localization with Subarray Processing and Covariance Correction](http://arxiv.org/abs/2607.24149v1)
  <details><summary>📄 Abstract</summary>
  Terahertz (THz)-band near-field (NF) localization offers high spatial resolution due to short wavelengths and distance-dependent wavefront curvature in NF multi-antenna systems. However, large arrays and dense deployments, necessary to mitigate THz path loss, raise the received signal dimensionality, creating computational overhead for localization. Furthermore, traditional two-dimensional (2D) subspace algorithms suffer from excessive complexity and poor robustness under coherent sources. This ...
  </details>

- **2026-07-27** — Ali Zahid Raja — [Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems](http://arxiv.org/abs/2607.24117v1)
  <details><summary>📄 Abstract</summary>
  Modern multi-agent knowledge systems increasingly accumulate knowledge through chains of autonomous transformations rather than direct retrieval. Existing provenance work records what happened - execution traces, tool calls, evidence links - and source-reliability estimation is long established (truth discovery, reputation systems). What is missing is an operational framework that attaches graded, per-domain transmitter reliability to claim-level transmission chains, with completeness semantics,...
  </details>

- **2026-07-27** — Xun Zhou, Zhen Dong, Mingyu Ren et al. — [RESTOR: Automated Test Oracle Generation for RESTful APIs via Reinforcement Learning](http://arxiv.org/abs/2607.23963v1)
  <details><summary>📄 Abstract</summary>
  Modern REST API testing faces a critical challenge in defining reliable test oracles, particularly in agile industrial environments where formal specifications (e.g., OpenAPI) are frequently missing or outdated, and historical execution logs are unavailable for newly deployed endpoints. In this paper, we present Restor (Reinforcement Enhanced Single-Traffic Oracle generator for REST APIs), a framework that generates executable test assertions from a single observed request-response pair in a bla...
  </details>

- **2026-07-27** — Bajian Xiang, Cheng Wen, Han Zhao et al. — [Qwen-Audio-3.0-TTS: Freely Controllable and Highly Robust Speech Synthesis with Multi-Stage Training Paradigm](http://arxiv.org/abs/2607.23938v1)
  <details><summary>📄 Abstract</summary>
  In this report, we present Qwen-Audio-3.0-TTS, a production-oriented speech synthesis system that jointly advances content consistency, speaker similarity, prosodic naturalness, audio quality, controllability, multilingual coverage, efficiency, and robustness. It combines a 12.5~Hz low-frame-rate speech tokenizer for reduced inference latency with a five-stage progressive training paradigm for coordinated language model (LM) and flow-matching model (FM) optimization. The model provides productio...
  </details>

- **2026-07-27** — Goodarz Mehr, Sepideh Gohari, Montasir Abbas et al. — [SimBEV2X: A Large-Scale Dataset and Data Generation Tool for Multi-Task Vehicle-to-Everything Cooperative Perception](http://arxiv.org/abs/2607.23910v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception through vehicle-to-everything (V2X) communication can overcome the inherent physical limitations of individual autonomous vehicles, such as occlusions and limited sensor range. However, the development of robust V2X algorithms, particularly those relying on unified spatial representations like bird's-eye view (BEV) representation, is hampered by the lack of large-scale, multi-modal, multi-task datasets. Moreover, collecting and annotating a large set of synchronized, real-...
  </details>

- **2026-07-27** — Nicolas Romeo, David B. Brückner, Noah P. Mitchell — [Growth and remodeling control shape memory in morphogenetic rods](http://arxiv.org/abs/2607.23907v1)
  <details><summary>📄 Abstract</summary>
  Mechanical instabilities provide a general design principle for shaping developing organs and engineering soft materials. However, in slender structures, simple elastic buckling tends to erase rather than preserve shape complexity: structures relax to the simplest possible shape, erasing finer detail. Living systems nonetheless build complex, reproducible morphologies from continually remodeling material, while remaining robust to noise arising across scales. Using analytical theory and numerica...
  </details>

- **2026-07-26** — Shuyu Chen, Chen Zhu, Ye Zhang et al. — [SCTA: An Agentic Framework for Stable and Interpretable Target Gene Discovery from Single-Cell RNA Sequencing](http://arxiv.org/abs/2607.23821v1)
  <details><summary>📄 Abstract</summary>
  Identifying therapeutic target genes from single-cell RNA sequencing (scRNA-seq) data remains a fundamental challenge in translational biology. Unlike bulk assays, scRNA-seq captures heterogeneous cellular states and rare subpopulations, but this same heterogeneity makes target discovery highly sensitive to analytical choices throughout the pipeline, including preprocessing, cell population selection, differential expression analysis, and downstream biological interpretation. As a result, existi...
  </details>

- **2026-07-26** — Daphne Chen, Archit Ritesh Jain, Eric Goossen et al. — [A Few Words Go a Long Way: Language Guided Robot Policy Synthesis](http://arxiv.org/abs/2607.23784v1)
  <details><summary>📄 Abstract</summary>
  While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages the reasoning capabilities of LLM coding agents to synthesize modular robot programs that utilize a suite of perception and cont...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 22 papers

- **2026-07-29** — Yize Li, Ruiqi Yu, Tianya Pan et al. — [GraphQAG: A Knowledge-Graph-Guided Visual Analytics Framework for Question-Answer Pairs Generation](http://arxiv.org/abs/2607.27182v1)
  <details><summary>📄 Abstract</summary>
  Question-answer (QA) pairs are widely used in knowledge base construction, question-answering systems, and the post-training of large language models (LLMs). However, important knowledge in long documents is often distributed across multiple paragraphs and connected through complex entity relationships. Such fragmented and relational knowledge poses substantial challenges for existing QA generation methods, which often fail to adequately cover core document content, cross-paragraph semantic conn...
  </details>

- **2026-07-29** — Zekun Ren, Hongzhao Tan, Jiaen Yee et al. — [PUDA: An AI-Native Hardware Harness for Self-Driving Laboratories](http://arxiv.org/abs/2607.26464v1)
  <details><summary>📄 Abstract</summary>
  Physical Unified Device Architecture (PUDA) is an AI-native hardware harness for self-driving laboratories (SDLs). Rather than building a human-centered graphical user interface (GUI) orchestration layer, PUDA creates a command-line runtime environment that lets agents observe, orient, decide, and act over experiments while hardware execution remains deterministic, atomic, and auditable. Headless by design, devices appear through discoverable command-line interfaces, JSON protocols are routed th...
  </details>

- **2026-07-28** — Genliang Zhu, Chu Wang — [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](http://arxiv.org/abs/2607.25364v2)
  <details><summary>📄 Abstract</summary>
  Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain cl...
  </details>

- **2026-07-28** — Siqi Zeng, Sewoong Lee, Han Zhao et al. — [Steering Instruction Hierarchies at Inference Time](http://arxiv.org/abs/2607.26228v1)
  <details><summary>📄 Abstract</summary>
  Instruction hierarchies are a core safety assumption of language model deployment: higher priority inputs, such as system prompts, should override conflicting lower priority inputs from users or tools. Yet frontier LLMs often violate this hierarchy. We introduce V-Steer, a training-free inference time method that restores privileged influence by editing cached value vectors at prompt positions. Using direct logit attribution on the first next token prediction, V-Steer identifies heads where lowe...
  </details>

- **2026-07-28** — Andreas Bauer — [The Last Costly Signal: How Generative AI Collapses Competence Signaling and Why Liability Sustains Markets for Expert Services](http://arxiv.org/abs/2607.26327v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence has reduced the cost of producing convincing artifacts of expertise-reports, analyses, proposals-to nearly zero. Signaling theory predicts that signals whose informational content rests on production cost lose that content when production becomes cheap. We formalize this prediction for markets for expert services, a class of credence goods, by modeling generative AI as a compression of the discernible headroom between what machines produce at negligible cost an...
  </details>

- **2026-07-28** — Rwaida Alssadi, Muntaser Syed, Balaji Kasula et al. — [TraceCoder: Explainable and Auditable Code Generation with Position-Key Snippet Versioning](http://arxiv.org/abs/2607.26307v1)
  <details><summary>📄 Abstract</summary>
  Contemporary LLM-based coding agents produce code as black-box outputs: the rationale behind each line is hidden, the evolution of the code through benchmark-driven repair is ephemeral, and post-hoc auditing is impossible. We present a code generation concept that addresses these shortcomings through three complementary mechanisms: (i) a relational snippet-history schema that records, per repair event, the benchmark reference, round number, failure text, and LLM explanation, enabling full proven...
  </details>

- **2026-07-28** — Gaston Besanson — [SARC-DQ: Runtime Data-Quality Gating for Agentic AI: Silent Evidence Defects, the Incompetence Shield, and Downstream-Only Remediation](http://arxiv.org/abs/2607.26313v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems act, so a defect in the evidence they retrieve becomes a wrong action with a currency cost. The most dangerous enterprise defects are metadata-borne: a stale price or a superseded record, perfectly well-formed in the payload and betrayed only by freshness, lineage, or provenance. Such a defect never enters the agent's context, and an agent cannot doubt data it cannot see. On a priced replenishment benchmark, a competent agent silently converts an injected metadata-borne defect in...
  </details>

- **2026-07-28** — Lefteris Lazaropoulos, Zoe Paraskevopoulou — [Foundational Refinement Proofs for Deployed Bytecode, at the Price of Tokens](http://arxiv.org/abs/2607.26306v1)
  <details><summary>📄 Abstract</summary>
  Relating low-level executable code to a high-level account of its behavior has been a central concern of programming-language research for decades. From formally verified compilers to translation validators, certifying compilers, and proof-carrying code, each approach chooses between laborious but foundational mechanized proofs and automation that costs completeness, generality, and an increased trusted base. Recently, large language models (LLMs) have begun to change the economics of formal ver...
  </details>

- **2026-07-28** — Genliang Zhu, Chu Wang — [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](http://arxiv.org/abs/2607.25364v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain cl...
  </details>

- **2026-07-28** — Ziheng Zhou, Huiyu Luo, Xiaohu Zhu et al. — [AMPBench-MT: A Homology-Controlled Benchmark for Antimicrobial Peptide Potency, Spectrum, and Safety Prediction](http://arxiv.org/abs/2607.25518v1)
  <details><summary>📄 Abstract</summary>
  Computational AMP discovery is often evaluated through AMP/non-AMP recognition, yet follow-up decisions depend on assay-derived evidence such as target-species potency, hemolysis, toxicity, and selectivity. Existing AMP and peptide benchmarks cover binary recognition, multilabel annotation, assay regression, or broader peptide-model comparison, but they do not jointly place AMP recognition, species-conditioned potency, spectrum, safety-facing proxy endpoints, and cross-endpoint behavior within o...
  </details>

- **2026-07-28** — Florian Krebs — [F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill](http://arxiv.org/abs/2607.25637v1)
  <details><summary>📄 Abstract</summary>
  F(AI)2R is FAIR research with AI in the loop, twice: an AI-assisted authoring pass and a machine-readable audit pass over every artefact. AI systems now draft, refactor, and verify research artefacts, yet their contributions are rarely recorded in a form a later human or machine can audit. Building on the original F(AI)2R experiment, we generalize its provenance model beyond scholarly writing into aiprov, a PROV-O extension covering any AI-in-the-loop artefact, and we package the method as an ex...
  </details>

- **2026-07-28** — Mateusz Kozłowski — [Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact](http://arxiv.org/abs/2607.25589v1)
  <details><summary>📄 Abstract</summary>
  Medical-imaging AI benchmarks combine datasets, DICOM rendering, prompts, provider APIs, automated labels, statistical code, manuscripts, and repository releases. Agreement across these artifacts is usually assumed rather than tested. We performed a retrospective forensic reproducibility audit of a preserved chest-radiograph vision-language model (VLM) pilot; no model was called again and no image or report was newly annotated. We traced prompt bindings, DICOM metadata, output completeness, labe...
  </details>

- **2026-07-28** — Sagie Dekel, Omer Madmon, Moshe Tennenholtz et al. — [Learning Dynamics of Strategic Publishers in Generative AI Ecosystems](http://arxiv.org/abs/2607.25514v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) search systems are transforming how users access information. Unlike ranking-based search systems, where users observe a ranked list of documents, GenAI search systems, given a user's question, generate an answer, often accompanied by external sources (e.g., in the form of citations). Content creators (publishers) seeking to increase exposure might behave strategically and compete with other creators for users' attention. While publishers in ranking-based systems might stra...
  </details>

- **2026-07-27** — Stefan G. Creadore — [Plato-Bio: verification-first biological novelty screening with temporal rediscovery and structural benchmarks](http://arxiv.org/abs/2607.23975v1)
  <details><summary>📄 Abstract</summary>
  Large language model research agents can connect literature retrieval, analysis code, and manuscript preparation, but coherent output does not establish scientific validity. We developed Plato-Bio, a biology-routed extension of the open Plato/Denario architecture that couples explicit workflow states with provenance records, citation checks, claim-to-evidence links, scoped file writes, and publication gates. A source audit identified and repaired three defects that could distort evaluation: loss...
  </details>

- **2026-07-27** — Krithi Shailya, Ananya Lakshmi Ravi, Venkatanathan K. V. et al. — [KANEx: Translating Kolmogorov-Arnold Networks' Interpretability to Medical Explainability](http://arxiv.org/abs/2607.24730v1)
  <details><summary>📄 Abstract</summary>
  Computer vision models have become highly effective for medical applications, yet their black-box nature continues to undermine clinician trust. In clinical workflows, chest X-ray classifiers are increasingly paired with Vision-Language Models (VLMs) to generate natural-language explanations. However, these systems add linguistic fluency without addressing the underlying opacity of the visual model. With the emergence of Kolmogorov-Arnold Networks (KANs), whose spline-based components provide in...
  </details>

- **2026-07-27** — Zhichao Yan, Shizhao Li, Jiapu Wang et al. — [CAGE: Cognitive Attribution Graphs for Faithful Inline Citation Generation in Long-Form Question Answering](http://arxiv.org/abs/2607.24236v2)
  <details><summary>📄 Abstract</summary>
  Long-form question answering increasingly relies on retrieved evidence to make LLM outputs verifiable, with inline citations tracing claims to source documents. However, existing systems often attach citations that are topically related but insufficient to support their claims. We identify attribution ambiguity as a structural challenge: end-to-end generation must implicitly resolve combinatorial claim--document assignments, obscuring evidential boundaries and increasing the risk of evidence-bou...
  </details>

- **2026-07-27** — Xiaoyang Li, Yiqi Wang, Haohui Lu et al. — [MemTX: Transactional Belief Commit for Stateful Agent Memory](http://arxiv.org/abs/2607.23929v2)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. We argue that a memory write is not a belief commit. We present MemTX, a transactional belief-commit protocol. Each rec...
  </details>

- **2026-07-27** — Qing Li, Zeyu Dong, Yin Cui et al. — [What Can I Edit? Open-Ended Strategy Discovery and the Emotion Editability Landscape](http://arxiv.org/abs/2607.23920v1)
  <details><summary>📄 Abstract</summary>
  Emotional image editing requires more than applying affective filters or modifying predefined visual factors: an effective edit must identify what a particular image can afford for a target emotion. Existing affective image manipulation methods, including recent agentic variants, largely operate within bounded strategy spaces based on predefined factor taxonomies, knowledge libraries, or conventional editing templates, and therefore often miss image-specific, context-grounded strategies. We intr...
  </details>

- **2026-07-27** — Sonia Castelo, Eden Wu, Joao Rulff et al. — [UrbanTrace: LLM-Assisted Discovery and Semantics-Aware Integration of Spatial Data](http://arxiv.org/abs/2607.25124v1)
  <details><summary>📄 Abstract</summary>
  Urban decision-making requires integrating heterogeneous spatial data. While current GIS tools handle geometric computation efficiently, they lack the semantic reasoning to guide complex workflows. Analysts manually manage data discovery, spatial boundaries, and measurement semantics, risking aggregation errors. We present UrbanTrace, a visual analytics system that transforms manual spatial data-wrangling into a transparent, node-based collaborative workflow with context-aware AI agents. Using a...
  </details>

- **2026-07-27** — Zhuchenyang Liu, Yao Zhang, Yu Xiao — [Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels](http://arxiv.org/abs/2607.24651v1)
  <details><summary>📄 Abstract</summary>
  Reliable visual document understanding requires a model to attribute each answer to the evidence regions that support it. Recent benchmarks and systems express this step through a coordinate interface: the model outputs the coordinates of bounding boxes that mark the evidence regions in the document. Under this interface, vision-language models often fail to identify the right regions even when the answer is correct, a failure known as Attribution Hallucination. We present a study that investiga...
  </details>

- **2026-07-27** — Zongyou Yang, Yinghan Hou — [Accuracy Hides How Language Models Fail: Measuring Failure States Under Matched Output Budgets](http://arxiv.org/abs/2607.24268v1)
  <details><summary>📄 Abstract</summary>
  Language-model benchmarks collapse two distinct measurement questions into a single accuracy score: whether a response reached an evaluable state, and whether its answer was judged correct. We introduce a two-layer evaluation framework that separates scorer-independent execution evidence, including termination, answer exposure, parseability, and completion length, from scorer-dependent correctness. Across 2,550 outputs from five fixed Qwen and DeepSeek configurations on MATH and ARC-Challenge, m...
  </details>

- **2026-07-27** — Guiling Guo, Jia Yang, Jiahao Xu et al. — [GraphRareBench: An Auditable Graph-Evidence Benchmark for Phenotype-Driven Rare-Disease Diagnosis](http://arxiv.org/abs/2607.24878v1)
  <details><summary>📄 Abstract</summary>
  Phenotype-driven diagnostic benchmarks usually report the rank of the reference disease, but they rarely reveal which plausible alternatives are ranked above it or what evidence a tool-using model examines before making its decision. We introduce GraphRareBench, a provenance-preserving benchmark containing 2,365 ontology-derived cases and 18,093 target-confounder pairs. Each case includes a coarsened HPO query, a fixed candidate pool, graph-defined hard confounders, and source-linked evidence re...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 11 papers

- **2026-07-29** — Yuxuan Cai, Yequan Hu, Hongqian Li et al. — [Can Large Language Models Represent Urban Publics? Behavioral Replication and Population Mismatch in an Affordable-Housing Experiment](http://arxiv.org/abs/2607.27100v1)
  <details><summary>📄 Abstract</summary>
  There is growing interest in using large language models (LLMs) as low-cost proxies for resident attitudes in urban planning. Previous work shows that LLMs can predict average results of survey experiments, but less is known about whether they preserve the spatially anchored, identity-conditioned structure behind those averages, namely how support changes as a project approaches homes and how that response divides across tenure and partisan groups. We compared eight open-weight LLMs with 843 res...
  </details>

- **2026-07-28** — Yuan Zhu, Ethan B. Liu, Frank Nie et al. — [ClinLens: Towards Long-Horizon Coding Agents for Longitudinal Multimodal Clinical Data Science](http://arxiv.org/abs/2607.26155v1)
  <details><summary>📄 Abstract</summary>
  Clinical data-science agents must transform heterogeneous longitudinal records into auditable analyses, yet existing benchmarks largely isolate medical question answering, structured-table reasoning, or generic scientific repositories. We introduce CLINLENS, a benchmark of 200 executable tasks over five linked MIMIC resources spanning structured electronic health records, notes, electrocardiograms, chest radiographs, and echocardiograms. A 4 x 5 taxonomy crosses four patient-time scopes with fiv...
  </details>

- **2026-07-28** — Podakanti Satyajith Chary, Barath Parthiban, Pranesh Velmurugan et al. — [Knowledge-Guided Multimodal Reasoning over Interacting Streams for Video-Level Ambivalence and Hesitancy Recognition](http://arxiv.org/abs/2607.25961v2)
  <details><summary>📄 Abstract</summary>
  Ambivalence and hesitancy (A/H) are conflicting affective states that precede the delay or abandonment of health behaviour change. Recognition of A/H at the video level is difficult, since the signal arises from disagreement across and within facial, vocal, linguistic, and bodily modalities, and manifests differently across individuals. The proposed PRISM-AH (Predictive Reasoning over Interacting Streams for Multimodal Ambivalence/Hesitancy Recognition), is a framework that treats A/H as a multi...
  </details>

- **2026-07-28** — Podakanti Satyajith Chary, Barath Parthiban, Pranesh Velmurugan et al. — [Knowledge-Guided Multimodal Reasoning over Interacting Streams for Video-Level Ambivalence and Hesitancy Recognition](http://arxiv.org/abs/2607.25961v1)
  <details><summary>📄 Abstract</summary>
  Ambivalence and hesitancy (A/H) are conflicting affective states that precede the delay or abandonment of health behaviour change. Recognition of A/H at the video level is difficult, since the signal arises from disagreement across and within facial, vocal, linguistic, and bodily modalities, and manifests differently across individuals. The proposed PRISM-AH (Predictive Reasoning over Interacting Streams for Multimodal Ambivalence/Hesitancy Recognition), is a framework that treats A/H as a multi...
  </details>

- **2026-07-27** — Zichao Lin, Yifeng Xie, Bowen Qu et al. — [PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models](http://arxiv.org/abs/2607.24957v1)
  <details><summary>📄 Abstract</summary>
  We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs). Existing benchmarks often fail to isolate perception: holistic evaluations conflate perceptual errors with failures in reasoning or domain knowledge, while application-driven benchmarks only cover narrow, fragmented domains shaped by heuristic designs. To address these limitations, PerceptionBench adopts a bottom-up approach: by diagno...
  </details>

- **2026-07-27** — Atharva Pandey, Gautam Jajoo — [Reason-Mediated Behavioral Models for Auditing LLM Social Simulators](http://arxiv.org/abs/2607.24649v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as social simulators, including as synthetic survey respondents. Most evaluations ask whether simulated outcomes resemble human outcomes. We argue that this is necessary but too weak: a simulator can match the final answer while using the wrong rationale-derived reason pattern. We study this problem through a 94-person sunscreen concept test in which each respondent evaluated three product concepts and wrote open-ended rationales. We map those rational...
  </details>

- **2026-07-27** — Yuze Sun, Zhongjie Duan, Yingda Chen — [TreeAdapter: Hierarchical Taxonomy-Guided Adapter Composition for Fine-Grained Species Image Generation](http://arxiv.org/abs/2607.24215v1)
  <details><summary>📄 Abstract</summary>
  Although general text-to-image models excel in open-domain generation, their performance degrades significantly in specialized downstream domains, particularly when generating images of rare biological species. Hindered by long-tailed distributions, general models struggle to capture subtle fine-grained details, while per-species fine-tuning methods over-isolate individual species and consequently ignore the shared visual features among closely related taxa. To address this, we propose TreeAdapt...
  </details>

- **2026-07-27** — David Soldani, Petrit Nahi, Awn Muhammad et al. — [6G: From Connectivity Infrastructure to Guaranteed Digital Services](http://arxiv.org/abs/2607.24185v2)
  <details><summary>📄 Abstract</summary>
  Sixth-generation mobile networks are approaching a structural inflection point. Five generations of vendor-led architecture have left operators dependent on platforms they cannot fully modify and artificial-intelligence inference layers they cannot audit. This article argues that 6G should reverse that trajectory by reordering five priorities: control first; customer outcomes before peak rates; business guarantees before megabytes; software-driven operations with governed agentic artificial inte...
  </details>

- **2026-07-27** — Alexandra Vassar, Rahat Masood, Hammond Pearce — [On Capturing the Narrative: Social Media Manipulation Wargaming for Cyberliteracy](http://arxiv.org/abs/2607.23993v1)
  <details><summary>📄 Abstract</summary>
  Misinformation is deeply embedded in online discourse, with nearly one in five posts during global events generated by bots that amplify false content. In recent years, the use of Generative AI has further lowered the barrier to producing convincing misinformation, yet most digital literacy education still relies on static checklists and single-player inoculation games built for an earlier media landscape. This paper describes how we addressed this educational gap through Capture the Narrative, ...
  </details>

- **2026-07-27** — Weijie Xia, Stefanie Horian, Hanyue Huang et al. — [Simulating Tenant Responses to Energy Policy Interventions with Transaction-Cost-Aware LLM Age](http://arxiv.org/abs/2607.24341v2)
  <details><summary>📄 Abstract</summary>
  Recent studies use Large language models (LLMs) to simulate human opinions and decisions by prompting models with demographic, attitudinal, or persona-based descriptions. Yet such simulations rarely model the practical, cognitive, or social frictions that shape how people respond to policy interventions. Perceived transaction cost (PTC) provides a useful lens for modeling the practical frictions that shape policy responses, such as information burden, administrative effort, coordination demands,...
  </details>

- **2026-07-26** — Belal S. Alsinglawi, Weizheng Wang, Junyi Wu et al. — [MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents](http://arxiv.org/abs/2607.23870v1)
  <details><summary>📄 Abstract</summary>
  Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. We introduce MulRobBench, an offline, protocol-conditi...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 143 papers

- **2026-07-29** — Jinkun Zhao, Kui Zhang, Wenjun Wu — [TPCD: Tone-Pressure Contrastive Decoding and the Label-Free Gating Bottleneck in Vision-Language Models](http://arxiv.org/abs/2607.26536v1)
  <details><summary>📄 Abstract</summary>
  High-pressure prompts can push vision-language models (VLMs) into unsupported commitments, such as reading illegible text, reporting indeterminate times, or affirming absent objects. This paper asks whether the pressure-induced distribution itself can serve as a contrastive-decoding negative branch. Tone-pressure contrastive decoding (TPCD) subtracts logits produced under a high-pressure instruction from logits produced under a safe neutral instruction. On the 800-example tone-matters benchmark,...
  </details>

- **2026-07-29** — Pengyu Wang, Benfeng Xu, Shaohan Wang et al. — [Which RAG Paradigm Wins at Scale? A Scaling Study of Retrieval-Augmented Generation Paradigms](http://arxiv.org/abs/2607.26497v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) methods range from lexical and dense retrieval to graph-based indexing and agentic search. They are usually evaluated on different benchmarks at one corpus size, leaving their accuracy-cost scaling unclear. To bridge this gap, we present a controlled corpus-scaling study of these four paradigms. A ladder of 28 strictly nested tiers grows from roughly 1,000 to 512,000 documents while questions and a fixed bedrock of relevant and adversarial documents remain un...
  </details>

- **2026-07-29** — Hongyang Wang, Yichen Shi, Hongrui Li et al. — [FAS-R1: A Unified Multi-Task MLLM for Reasoning Face Anti-Spoofing](http://arxiv.org/abs/2607.26432v1)
  <details><summary>📄 Abstract</summary>
  Face anti-spoofing (FAS) is increasingly expected to provide not only bona fide/spoof decisions, but also attack semantics and image-grounded evidence for human inspection. Existing discriminative FAS models remain largely label-centric, while recent MLLM-based methods offer structured outputs but still rely mainly on supervised fine-tuning, often producing template-like rationales and weak optimization for difficult attacks. We propose FAS-R1, a two-stage reasoning-oriented MLLM framework for u...
  </details>

- **2026-07-29** — Jiayuan Di, Haoyi Yang, Yufei Luo et al. — [Evaluating Regional Bias in LLMs From Abstract Stereotype to Concrete Social Decision-Making](http://arxiv.org/abs/2607.27022v1)
  <details><summary>📄 Abstract</summary>
  Regional bias in large language models (LLMs) may shape both perceptions of regional groups and decisions about individuals from different regions. Yet existing studies often examine these manifestations separately, leaving their structure and consequences unclear. We introduce Stereotypes-to-Decisions (S2D), a systematic framework evaluating regional bias from abstract stereotypes to concrete social decisions. Covering all 34 provincial-level administrative regions of China, S2D evaluates six L...
  </details>

- **2026-07-29** — Zhe Liu, Quan Lu, Zhaohui Du et al. — [BioVLN: A Simulation Platform for Visual Language Navigation in Biomedical Laboratories](http://arxiv.org/abs/2607.26914v1)
  <details><summary>📄 Abstract</summary>
  Biomedical laboratory robots must navigate to instruments before performing experimental procedures. Existing embodied navigation platforms are designed for household environments and treat a target as an object center or an arbitrary nearby position. This representation is inadequate for laboratory instruments, which must be approached from their operating side while maintaining safe clearance from surrounding equipment. We introduce BioVLN, a simulation platform for developing and evaluating v...
  </details>

- **2026-07-29** — Weile Gong, Zijian Lu, Mingcai Chen et al. — [Prior Directions: Why GUI Grounding Gets Locked in the Past](http://arxiv.org/abs/2607.26913v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models often use descriptions of earlier visual states to make decisions about the current scene. When the scene changes, stale language can redirect an otherwise correct visual judgment toward an outdated answer. We study this failure as visual lock-in in a controlled grounding setting where only the verbalized prior varies. Across models, stronger lock-in accompanies smaller changes in the model representation before the final answer. This reversal suggests that lock-in depends...
  </details>

- **2026-07-29** — Lucas Zamora Vera, Jose A. Gonzalez-Lopez — [Phoneme- vs. Character-Level Targets and Selective State-Space Models for Intracortical Brain-to-Text](http://arxiv.org/abs/2607.26751v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art intracortical brain-to-text systems pair a neural-sequence phone decoder with an external language model. Two design axes remain underexplored: whether selective state-space models (Mamba) improve on recurrent decoders, and how the output target (phonetic vs.\ character) interacts with that choice. On the public Brain-to-Text '25 benchmark, we study a controlled 2x2 grid (GRU vs.\ hybrid Mamba decoder; phonetic vs.\ character targets) trained with a CTC objective under one repro...
  </details>

- **2026-07-29** — Junhao Qiu, Zidong Wang, Yansong Sun et al. — [AgenticCANN: Automated Ascend C Operator Generation via Knowledge-Augmented Agentic Evolution](http://arxiv.org/abs/2607.26661v1)
  <details><summary>📄 Abstract</summary>
  Ascend C operator optimization is critical for NPU (Neural Processing Unit) inference performance but requires deep hardware expertise.While large language models (LLMs) have shown promise in automated CUDA kernel generation, the fundamentally different programming model of Ascend C introduces unique challenges that remain unexplored. In this paper, we propose AgenticCANN, a knowledge-augmented agentic evolution framework specifically tailored for automated Ascend C operator synthesis in low-cor...
  </details>

- **2026-07-29** — Zeyu Wang — [The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy](http://arxiv.org/abs/2607.26648v1)
  <details><summary>📄 Abstract</summary>
  Spiking neural networks (SNNs) are promoted as an energy-efficient substrate because sparse, event-driven activity replaces dense multiply-accumulates with cheap accumulates. We argue the energy dividend of sparsity is not a property of SNNs but of the task. Holding architecture fixed and swapping only the hidden unit (continuous vs. leaky-integrate-and-fire), plus a two-sided target-firing-rate probe, we measure how far activity can be pushed down before quality breaks. Low-load feed-forward pe...
  </details>

- **2026-07-29** — Hansi Karunarathna, Nirhoshan Sivaroopan, Chamara Madarasingha et al. — [RAG-HAR+: Towards Cost-Efficient LLM-Based Human Activity Recognition for Edge Deployment](http://arxiv.org/abs/2607.26631v1)
  <details><summary>📄 Abstract</summary>
  Human Activity Recognition (HAR) from wearable sensors supports applications in healthcare, rehabilitation, fitness tracking, and smart environments. Yet, existing deep learning approaches require dataset-specific training, large labeled corpora, and repeated adaptation to new sensor settings or activity taxonomies. Retrieval-Augmented Generation for Human Activity Recognition (RAG-HAR) addresses this by framing HAR as a training-free, retrieval-augmented task, in which statistical descriptions ...
  </details>

- **2026-07-29** — Donghang Duan, Xu Zheng, Lizong Zhang et al. — [FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA](http://arxiv.org/abs/2607.26618v1)
  <details><summary>📄 Abstract</summary>
  Federated PEFT enables LLMs to collaboratively adapt to decentralized private data without sharing raw examples. However, task heterogeneity across clients can cause cross-task interference and gradient conflicts during aggregation. Federated MoE-LoRA addresses this challenge through specialized LoRA experts and conditional routing. Yet existing methods typically specialize at client granularity, implicitly assuming task-coherent clients. Our core insight is that experts need purity, namely patt...
  </details>

- **2026-07-29** — Tao Su, Jinjing Hu, Xiao Wang et al. — [ASARL: Autonomous Social-Aware Relevance Learning for QQ Search](http://arxiv.org/abs/2607.26593v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of online social platforms has transformed communication and information retrieval, giving rise to social search, where queries-titles are typically expressed in informal, community-specific language. While large language models provide strong general-purpose semantic understanding, their effectiveness in social search is constrained by contextual discrepancy, data scarcity, and behavior-driven dynamics. To address these challenges, we propose the Autonomous Social-Aware Relevan...
  </details>

- **2026-07-29** — Mingyang Sun, Jiude Wei, Xiujian Liang et al. — [Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models](http://arxiv.org/abs/2607.26513v1)
  <details><summary>📄 Abstract</summary>
  Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world. This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation. To bridge this crucial gap, we construct a Concept Expert module for VLA to build executable Analytic Concepts that represent objects as explicit, programmatic blueprints. Our mechanism operates in two synergis...
  </details>

- **2026-07-29** — Kawai Chung, Chunkit Chan, Yauwai Yim et al. — [MultivationBench: A Benchmark for Multimodal Sequential Motivation Reasoning](http://arxiv.org/abs/2607.26465v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models have sparked significant interest due to their potential for social intelligence; however, their ability to perform sequential motivation reasoning remains insufficiently studied. Existing evaluations predominantly examine static text or isolated visual snapshots, which do not reflect the cumulative nature of real-world behavioral drivers. To address this gap, we introduce MultivationBench, a benchmark designed to rigorously evaluate multimodal motivation reasoni...
  </details>

- **2026-07-29** — Zhiyuan Pan, Sungmin Kang, Imam Nur Bani Yusuf et al. — [ExplainBench: Evaluating Code Explanations from Agents](http://arxiv.org/abs/2607.26451v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents have seen rapid adoption in software engineering. As agents take a greater role in the actual generation of code, they are making larger changes, spanning tens to hundreds of lines. This makes manual review of agent results increasingly infeasible, leading developers to turn to explanations to understand enacted changes. Despite this, there are no benchmarks that evaluate the trustworthiness of agent-generated explanations. To bridge this gap, we propose Explain...
  </details>

- **2026-07-29** — Genze Jiang, Yizhou Huang, Kezhi Wang — [Can We Trust AI in 6G? Verifiable and Auditable AI-Driven Trustworthy Wireless Networks](http://arxiv.org/abs/2607.26409v1)
  <details><summary>📄 Abstract</summary>
  Mobile network operators are increasingly exploring the use of artificial intelligence (AI) to automate complex network tasks, such as cell selection and mobility management. A fundamental problem arises: there is currently no way to verify that an AI function is making the right decisions or for the right reasons, rather than arriving at correct-looking answers through unreliable shortcuts. In safety-critical and resilience-focused infrastructure, this lack of transparency poses a significant c...
  </details>

- **2026-07-29** — Mehmet Deniz Türkmen, Daniel Hienert — [Continuous Online Evaluation of Recommendation Strategies in Social Science Academic Search](http://arxiv.org/abs/2607.26380v1)
  <details><summary>📄 Abstract</summary>
  Delivering relevant recommendations in academic search engines is a complex task due to the diversity of subject areas, information types, and user preferences. In this case study, we address these challenges by integrating and evaluating a range of recommendation systems within GESIS Search - a domain-specific search engine for the social sciences that provides researchers with access to research data, publications, variables, and measurement instruments. To support continuous, real-time evalua...
  </details>

- **2026-07-29** — Hengyi Xie, Chenfei Yao, Xianjin Wu et al. — [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](http://arxiv.org/abs/2607.27205v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that reformulates the conventional $V \to L \to A$ pathway as a direct $V + L \to A$ mapping. Instead of ...
  </details>

- **2026-07-29** — Gabe Everett, Brice Gunter, Ryan Vander Stelt et al. — [SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception](http://arxiv.org/abs/2607.26985v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement policy learning directly in physical robots (on-robot learning) remains bottlenecked by slow wall-clock training times. We present SymmGrid, a trajectory level augmentation framework inspired by parallelized symmetries that super-scales group transformations to significantly accelerate on-robot learning in both egocentric and exocentric visual setups. We model a Markov Decision Process (MDP) under a symmetry tree, in which state-action pairs have admissible parallelized invari...
  </details>

- **2026-07-29** — Jia Luo — [From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence](http://arxiv.org/abs/2607.26903v1)
  <details><summary>📄 Abstract</summary>
  The key bottleneck in embodied AI is not model architecture but data. Although billions of human manipulation videos exist online, robots cannot directly learn from them due to the embodiment gap between human morphology and robot hardware. We introduce Pegasus, a low-resource framework that bridges this gap by translating human demonstrations into robot-learnable data through structured knowledge transfer. Instead of relying on raw video prompts, Pegasus constructs a graph-based intermediate re...
  </details>

- **2026-07-29** — Yushan Liu, Peibo Sun, Xintao Chao et al. — [CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation](http://arxiv.org/abs/2607.26789v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores l...
  </details>

- **2026-07-29** — Sami Azirar, Enrico Pallotta, Jan Nogga et al. — [ContactFlow: A video action conditioning that transfers across embodiments](http://arxiv.org/abs/2607.26579v1)
  <details><summary>📄 Abstract</summary>
  World models offer a promising route toward robot planning by enabling agents to imagine and verify the consequences of actions before execution. However, current video-based world models often struggle to capture the physical constraints that govern manipulation, particularly contact. Further, their action conditioning is often constrained to specific embodiments such as parallel grippers. We propose \emph{Contact Flow}, an embodiment-agnostic action representation that encodes manipulation thr...
  </details>

- **2026-07-29** — Zheng Zhang, Nanjie Yao, Jiarui He et al. — [CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games](http://arxiv.org/abs/2607.26393v1)
  <details><summary>📄 Abstract</summary>
  Social deduction games (SDGs) such as Werewolf have become challenging testbeds for AI agents. These games require complex social skills such as reasoning, deception, and collaboration. While recent advances in large language models (LLMs) have driven significant progress in SDG agents, current approaches are predominantly text-based, overlooking the multimodal nature that is fundamental to human social interaction. To bridge this gap, we introduce CaM-Wolf, the first SDG agent that integrates m...
  </details>

- **2026-07-29** — Xinyu Wang, Jinbo Bi, Minghu Song — [Q-Steer: Action-Value Guidance for Molecular Policy Optimization](http://arxiv.org/abs/2607.26391v1)
  <details><summary>📄 Abstract</summary>
  Oracle-limited molecular optimization gives reward only after a complete molecule is generated, while each rollout requires many local next-token decisions. This delayed-feedback interface makes molecular policy optimization myopic: an optimizer can learn that a molecule was good without knowing which intermediate actions made it good. We introduce Q-Steer, a rollout-time action-value steering primitive for molecular language models. Q-Steer uses an offline-trained and frozen prefix-action value...
  </details>

- **2026-07-29** — Nishant Balepur, Connor Baumler, Valerie Chen et al. — [(Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding](http://arxiv.org/abs/2607.26375v1)
  <details><summary>📄 Abstract</summary>
  Coding agents (e.g., Cursor) improve developer productivity by optimizing task completion, but shifting users from writing code to prompting and reviewing may harm their understanding, impeding oversight, learning, and communication. To probe this, we have 54 students create a website with one of two AI systems: an agent that edits user code; or a chatbot where users write code alone or adapt generic code snippets. We test understanding via comprehension questions and a task where users extend t...
  </details>

- **2026-07-29** — Lennon J. Shikhman, Michael Galarnyk, Aadi Dash et al. — [Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes](http://arxiv.org/abs/2607.27188v1)
  <details><summary>📄 Abstract</summary>
  Accurate option prices do not imply accurate recovery of the latent risk-neutral density. We study this distinction with two complementary benchmarks. A controlled benchmark exposes simulator-truth densities for latent evaluation, while a chronological NIFTY benchmark tests only held-out market prices. A two-component lognormal mixture has the lowest aggregate price, $L^1$, Wasserstein, and fixed-tail errors on the synthetic benchmark. Learned operators retain narrower strengths: DeepONet reduce...
  </details>

- **2026-07-29** — Adar Avsian, Atahan Dokme, Tony Woo et al. — [Latent-IM: Latent Interaction Management for Speech LLMs](http://arxiv.org/abs/2607.26928v1)
  <details><summary>📄 Abstract</summary>
  Classical spoken dialogue systems often separated dialogue management from response realization: a policy selected the next dialogue action, and a generation component expressed that action. As dialogue systems shift toward LLMs, this decomposition has largely disappeared into the model's hidden representations. We ask whether an LLM-internal analogue of state estimation and action control can be recovered for conversational moves such as acknowledging, checking, querying, explaining, and replyi...
  </details>

- **2026-07-29** — Stefano Liberati, Valentin Pomakov, Samuele Silveravalle — [Bridging Superfluid and Nonminimally Coupled BEC Dark Matter through RAQUAL](http://arxiv.org/abs/2607.26841v1)
  <details><summary>📄 Abstract</summary>
  Motivated by their common condensed-matter inspiration and their shared aim of reconciling MOND-like phenomenology on galactic scales with particle dark matter on larger scales, we investigate the relation between Superfluid Dark Matter (SFDM) and Bose--Einstein Condensate Dark Matter (BECDM). Since SFDM is formulated in the Newtonian regime whereas BECDM is fully relativistic, we first show that the MONDian formulation of SFDM arises as the Newtonian, low-acceleration limit of a Relativistic AQ...
  </details>

- **2026-07-29** — Janin Koch, Xiaohan Liao, Géry Casiez — [AI as Friction for Reflection Support in Ideation](http://arxiv.org/abs/2607.26827v1)
  <details><summary>📄 Abstract</summary>
  Generative AI tools for creative work tend to be designed around the goal of removing friction, on the assumption that smoother iteration and faster output translate into more value for the designer. We argue, however, that this framing leaves out something important about how design ideation works, namely reflection-in-action. The act of accepting, rejecting and reworking candidate ideas is both a path to a final outcome and the process through which designers develop the rationale that allows ...
  </details>

- **2026-07-29** — Runyao Yu, Yuchen Tao, Yujie Chen et al. — [Crossing-Free Probabilistic K-Line Forecasts Without Retraining](http://arxiv.org/abs/2607.26792v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic K-line forecasting describes uncertainty in four complementary prices, namely open--high--low--close (OHLC). However, it introduces two consistency problems: quantile crossing and K-line crossing. Quantile crossing occurs when a higher-quantile forecast falls below a lower-quantile forecast, while K-line crossing occurs when the forecast low exceeds the open or close, or the forecast high falls below the open or close. Existing solutions generally address only one problem through o...
  </details>

- **2026-07-29** — Mahesh Godavarti — [Journey Operators for Structured Multi-Axis Composition](http://arxiv.org/abs/2607.26775v1)
  <details><summary>📄 Abstract</summary>
  Many kinds of data have structure along one or more axes: words in a sentence, pixels in an image, nodes in a tree, frames in audio, or cells in a 3D volume. Along one axis, order matters: "the dog bit the man" is different from "the man bit the dog." Across independent axes, however, neither composition nor movement should depend on the order of axes: in an image, composing right then down should give the same result as composing down then right, and moving right then down should describe the s...
  </details>

- **2026-07-29** — Huixiang Zhang, Mahzabeen Emu — [Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM](http://arxiv.org/abs/2607.26773v1)
  <details><summary>📄 Abstract</summary>
  Latent communication in large language model (LLM)-based multi-agent systems (MAS) transmits continuous internal representations instead of text, but greater representational capacity does not establish that the receiver uses task-relevant information. End-task performance alone also cannot reveal whether an observed effect depends on message presence, content generated for the evaluated example, or information supplied by a separate agent. We introduce a causal audit that applies controlled mes...
  </details>

- **2026-07-29** — Joaquim Duran, Konstantin Pankrashkin — [Congruence of Dirac operators with applications to generalized MIT bag models](http://arxiv.org/abs/2607.26675v1)
  <details><summary>📄 Abstract</summary>
  We highlight a simple congruence transform that shifts coupling parameters for Dirac operators with shell interactions. As one of the consequences, this leads to new observations concerning the self-adjointness and the infinite mass interpretation of generalized MIT bag models.
  </details>

- **2026-07-29** — Federica Pepe, Daniele Bifolco, Costantino Martignetti et al. — [AIGen: Automating AI Bill of Materials Generation Through Hybrid MLOps Integration](http://arxiv.org/abs/2607.26652v1)
  <details><summary>📄 Abstract</summary>
  The responsible development and deployment of artificial intelligence (AI) systems requires rigorous documentation of their constituent artifacts, e.g., datasets, model weights, training pipelines, and runtime dependencies. Although the Software Package Data Exchange (SPDX) 3.0 standard introduced native support for AI and dataset profiles, practical tooling capable of generating standards-compliant AI Bills of Materials (AIBoMs) in an automated and extensible manner remains scarce. This paper p...
  </details>

- **2026-07-29** — Yuan-Heng Wang, Hoshin V. Gupta — [From Conceptual Hydrologic Models to Conceptually Interpretable Neural Networks: A Snow-Water Mass-Conserving-Perceptron Framework for Discovering Catchment-Scale Precipitation-Storage-Runoff Representations](http://arxiv.org/abs/2607.26492v1)
  <details><summary>📄 Abstract</summary>
  The Mass-Conserving Perceptron (MCP) establishes a modeling paradigm in which conceptual hydrologic models can be reformulated as physically constrained, conceptually interpretable neural networks. Here, we develop a snow-water MCP network framework and evaluate it across 513 CAMELS-US basins. We first recast a coupled two-state SOIL-MCP and SNOWMCP conceptual model as a mass-conserving neural network and show that the hydrologic-model and neural-network formulations achieve comparable predictiv...
  </details>

- **2026-07-29** — Haifeng Wu — [Learning Dynamic User Personas from Implicit Interaction Streams via Iterative Refinement](http://arxiv.org/abs/2607.26473v1)
  <details><summary>📄 Abstract</summary>
  Personalizing large language models (LLMs) to individual users is essential for improving user experience, yet existing approaches typically rely on explicit preference supervision such as pairwise comparisons or demographic attributes, limiting their applicability in natural interaction settings. We propose IRIS, a framework that learns dynamic user personas directly from implicit interaction streams by extracting behavioral signals from everyday conversations and iteratively refining persona r...
  </details>

- **2026-07-29** — Aman Kumar, Lasitha Vidyaratne, Dipanjan D Ghosh et al. — [Diagnosing Fine-Grained Inconsistency Classification in Financial Disclosure Text](http://arxiv.org/abs/2607.26368v1)
  <details><summary>📄 Abstract</summary>
  Financial disclosures contain numerical claims, temporal statements, entity references, policy commitments, and risk descriptions that may conflict in qualitatively different ways. Detecting a conflict is only the first step: review workflows may also need to determine its type, since numerical, temporal, referential, factual, and normative inconsistencies require different evidence and downstream checks. We study this problem as fine-grained inconsistency classification. Using a fixed 5,940-ins...
  </details>

- **2026-07-29** — Keegan Harris, Brian W. Lee, Ian Waudby-Smith et al. — [Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning](http://arxiv.org/abs/2607.26358v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) fine-tuning is widely used in language model training to improve model performance on a target task while limiting drift from a reference policy. A standard way to balance this trade-off is via a KL-regularized RL objective, although this formulation does not by itself provide a principled way to set the regularization coefficient. In practice, the coefficient is typically chosen heuristically or via hyperparameter search, which can lead to unnecessary overhead in tra...
  </details>

- **2026-07-28** — Fangxu Yu, Zinan Lin, Xiaodong Liu et al. — [Weak-to-Strong On-Policy Distillation](http://arxiv.org/abs/2607.26246v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD), which aligns a student with the teacher's token-level distribution on the student's own rollouts, is an effective paradigm for transferring capabilities across LLMs. Prevailing approaches assume a teacher at least as capable as the student: they either distill a larger model into a smaller one, which fails at the frontier where no larger teacher exists, or consolidate multiple domain experts trained from a shared base, which requires costly training at the student's...
  </details>

- **2026-07-28** — Takyoung Kim, Kang-wook Kim, Sang Hoon Woo et al. — [DuplexGen: Adaptive Synthesis of Human-AI Turn-Taking Dialogues](http://arxiv.org/abs/2607.26178v1)
  <details><summary>📄 Abstract</summary>
  Turn-taking is a central component of full-duplex interaction. Which turn-taking behaviors are appropriate varies with the scenario, yet current models apply a single norm regardless of context. This limitation originates in their training data: human-human speech corpora capture natural timing phenomena but provide little role grounding or scenario-specific norms, while heuristic or prompted synthesis methods inject turn-taking behaviors without basing them on human preferences. We introduce Du...
  </details>

- **2026-07-28** — Lecomte Thierry, Germain Vincent — [Validating ETCS Data with the B Mathematical Language: An Industrial Pipeline and a Blueprint for LLM Integration](http://arxiv.org/abs/2607.26111v1)
  <details><summary>📄 Abstract</summary>
  Can large language models participate in the production and validation of ERTMS/ETCS data without undermining the certification arguments required by CENELEC EN 50128/50716? ERTMS/ETCS is a distributed safety-critical system (trackside, onboard, radio-block centre) whose behaviour is parameterised by large volumes of data drawn from the UNISIG Subsets; errors in that data propagate through the distributed architecture. This paper reports the current status of an ongoing industrial research effor...
  </details>

- **2026-07-28** — Yuhan Hu, Hugues Thomas, Peide Huang et al. — [MoMo: Dial Motion Mode in Robot Manipulation with Spatiotemporal Action Tokenization](http://arxiv.org/abs/2607.26315v1)
  <details><summary>📄 Abstract</summary>
  To operate effectively across diverse contexts, robots must not only perform manipulation tasks accurately but also adapt how their actions unfold to the task, object, and interaction setting. We ask whether this execution-level variation can be learned as a reusable behavioral factor shared across tasks. We present \textbf{MoMo}, a two-stage imitation-learning framework consisting of a spatiotemporal action tokenizer and a behavior-cloning transformer that takes task and a continuous motion-mod...
  </details>

- **2026-07-28** — Yuvraj Verma — [Try Again, Don't Look Back: Blind Resampling Outperforms Self-Repair in Small Code Models](http://arxiv.org/abs/2607.26117v1)
  <details><summary>📄 Abstract</summary>
  Self-repair - returning a failed program to the model together with its test output and asking for a correction - is a standard component of code agents, and is almost always evaluated against a baseline that does not retry at all. We argue that this comparison confounds the value of the feedback with the value of the extra attempt. Using a placebo-controlled design on MBPP+ at three model scales (1.5B, 3B, 7B), we compare four matched-budget retry conditions: blind resampling, a content-free fa...
  </details>

- **2026-07-28** — Evyatar Cohen, Jose Yallouz, Alexander Shpiner et al. — [Incast-Free MoE Rate-Based Scheduling](http://arxiv.org/abs/2607.26340v1)
  <details><summary>📄 Abstract</summary>
  Mixture of Experts (MoE) architectures have become key to large language models; however, their typical round-robin (RR) scheduling introduces significant bottlenecks.   In this paper, we demonstrate that RR causes a previously-undiscovered exponential incast phenomenon with MoE traffic. We propose an alternative proactive fair scheduling framework tailored for MoE workloads, which effectively prevents fabric oversubscription. We also outline how it can be implemented in NICs. Finally, through e...
  </details>

- **2026-07-28** — Jiaang Li, Chengzu Li, Zhaochong An et al. — [Seeing or Knowing? Visual Context Sensitivity in Multimodal Large Language Models](http://arxiv.org/abs/2607.26326v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) achieve strong performance by integrating visual inputs with the rich priors of pretrained language models. However, they often fail on vision-centric tasks, especially when visual evidence conflicts with pretrained knowledge. We explore these failures separately using two diagnostic paradigms: (1) probing whether visual information is available, via image reconstruction, and (2) measuring multimodal context sensitivity, the extent to which the model foll...
  </details>

- **2026-07-28** — Marie Neubrander, Graham Tierney, Alexander Volfovsky — [The Confounder Trap: Treatment-Encoding Representations in Causal Inference with Text](http://arxiv.org/abs/2607.26309v1)
  <details><summary>📄 Abstract</summary>
  Estimating causal effects of linguistic properties from observational text is difficult because the same document can contain both the treatment of interest and the non-treatment textual attributes needed for adjustment. Existing approaches often learn representations from the full text to capture latent confounding, but when treatment status is itself encoded by words in the text, these representations can directly encode treatment. This creates a confounder trap: richer representations can mak...
  </details>

- **2026-07-28** — Kalyani Kansal, Brandon Levin, David Savitt — [Inclusions between p-bounded crystalline loci in dimension two](http://arxiv.org/abs/2607.26305v1)
  <details><summary>📄 Abstract</summary>
  Let p be an odd prime and K/Qp a finite unramified extension of degree f > 1. Let Z(r) be the reduced special fiber of the Emerton-Gee stack of two-dimensional crystalline representations of Hodge type r of the absolute Galois group of K. We study the collection of stacks Z(r) as r varies over p-bounded Hodge types, as a set partially ordered under inclusion. We prove that aside from two degenerate cases, simple inclusions can be classified in terms of three operations on Hodge types, two of whi...
  </details>

- **2026-07-28** — Kuldip Singh Atwal, Emma Von Hoene, Hossein Amiri et al. — [Mobility and Contact Networks Shape Epidemic Outcomes: A Large-Scale Agent-Based Modeling Study](http://arxiv.org/abs/2607.26217v1)
  <details><summary>📄 Abstract</summary>
  Human mobility plays a central role in shaping contact patterns that drive infectious disease transmission, yet mobility is often simplified in agent-based models (ABMs) due to data and computational constraints. The effects of these simplifications on model outputs are poorly understood. In this study, we systematically examined how alternative mobility assumptions influence emergent contact networks and epidemic dynamics within a large-scale ABM. Using a synthetic population of one million age...
  </details>

- **2026-07-28** — Zongfei Li, Yuan-yih Shang, Guozhong Luo — [Dynamic Parameterization Is Not Dynamic Inference](http://arxiv.org/abs/2607.26192v1)
  <details><summary>📄 Abstract</summary>
  Input-dependent controller coefficients are often treated as evidence of dynamic inference or computational savings. This interpretation conflates three properties: coefficient variation, dependence of a frozen model on how coefficients are assigned to inputs, and conditional execution. We focus on the second property and formulate a general principle of frozen-controller auditing. We provide one concrete implementation, Frozen-Controller Auditing (FCA), which caches the complete coefficient ten...
  </details>

- **2026-07-28** — Chandra Sripada, Richard Lewis — [Cognitive Convergence: Deep Similarities Between Large Language Models and Human Cognition](http://arxiv.org/abs/2607.26179v1)
  <details><summary>📄 Abstract</summary>
  LLMs are widely regarded as alien intelligences, systems whose cognitive operations are fundamentally unlike our own. Apparent similarities to human cognition are therefore often seen as the result of anthropomorphic projection. We argue that this framing is mistaken. LLMs clearly differ from humans in important respects, including their physical substrate, learning history, and the environments with which they interact. These differences make it all the more striking that contemporary LLM-based...
  </details>

- **2026-07-28** — Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin — [WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing](http://arxiv.org/abs/2607.25234v2)
  <details><summary>📄 Abstract</summary>
  Stereo depth estimation for driving, robotics and augmented reality must run at high resolution under tight latency budgets, yet in transformer-based matchers the global self-attention that aggregates scene context grows quadratically with the number of pixels and comes to dominate runtime. We show that the joint self-attention stage of a stereo transformer, whose role is to spread context across both views, can be replaced by a data-independent Walsh-Hadamard token mixer that mixes tokens globa...
  </details>

- **2026-07-28** — Abhishek dileep, Shubham Sharma, Padmanabhan Rajan — [Device Invariance using Domain Adaptation on Acoustic Scene Classification](http://arxiv.org/abs/2607.25887v1)
  <details><summary>📄 Abstract</summary>
  This paper explores the effectiveness of domain adaptation techniques when using convolutional neural network (CNN)-based and transformer-based feature representations for acoustic scene classification. Two well-known domain adaptation techniques, namely domain adversarial neural network (also called DANN) and conditional domain adversarial network (also called CDAN) are evaluated under various domain shifts. Our study indicates that DANN provides effective domain adaptation fairly consistently ...
  </details>

- **2026-07-28** — Yuhao Cheng — [Beyond endoscopy for the symmetric square representation: The simple trace formula case](http://arxiv.org/abs/2607.25383v1)
  <details><summary>📄 Abstract</summary>
  At the beginning of this century, Langlands introduced a strategy known as \emph{Beyond Endoscopy} to attack the principle of functoriality. Altuğ studied $\mathsf{GL}_2$ over $\mathbb Q$ in the unramified setting for the standard representation. We consider the case with ramification at $S=\{\infty,q_1,\dots,q_r\}$ with $2\in S$ and derive an asymptotic formula for the symmetric square representation adding some additional conditions on the test function so that the trace formula is simple. The...
  </details>

- **2026-07-28** — Nagarani Brammanayagam, Devaprakash Muniraj — [MR-TGN: A Meta-Role Temporal Graph Network for Team-Level Intent Prediction in Multi-Agent Systems](http://arxiv.org/abs/2607.25316v1)
  <details><summary>📄 Abstract</summary>
  Collective intent prediction in multi-agent systems focuses on predicting the shared objectives and future behaviours of groups of interacting agents. The problem is particularly challenging because collective intent emerges from complex interactions, evolving cooperation structures, and long-term behavioural dependencies among heterogeneous agents operating in dynamic and partially observable environments. Furthermore, functional roles adopted by agents are often latent, may change over time, a...
  </details>

- **2026-07-28** — Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti et al. — [VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening](http://arxiv.org/abs/2607.26042v1)
  <details><summary>📄 Abstract</summary>
  We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph man...
  </details>

- **2026-07-28** — Ankang Yang, Jitao Zhao, Di Jin et al. — [CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer](http://arxiv.org/abs/2607.26023v1)
  <details><summary>📄 Abstract</summary>
  Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored...
  </details>

- **2026-07-28** — Stefan Krsteski, Charlotte Meyer, Guillaume Allegre et al. — [Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](http://arxiv.org/abs/2607.25891v1)
  <details><summary>📄 Abstract</summary>
  Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six und...
  </details>

- **2026-07-28** — Minghao Li, Ziqian Liu, Ziyu Mao et al. — [Towards a Systems Foundation for Agentic Cloud Management](http://arxiv.org/abs/2607.25883v1)
  <details><summary>📄 Abstract</summary>
  Agentic cloud management is emerging as a practice to automate laborious operations, minimize toil, and improve responsiveness. Despite the rapid development of autonomous management agents, we argue that the fundamental missing piece is a systems foundation to enable safe, effective operations across agents and between agents and human operators. In this paper, we advocate for the need of such a systems foundation and share our efforts on developing CloudWeaver, an agentic management substrate ...
  </details>

- **2026-07-28** — Jiabao Ji, Yujian Liu, Li An et al. — [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](http://arxiv.org/abs/2607.25816v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents often spend substantial wall-clock time waiting for tool call results. Tool-call speculation can hide this latency by predicting and pre-executing an agent's next tool call if the prediction matches the agent's eventual tool call, but existing speculators are typically separate draft models or cached traces that are poorly aligned with the deployed agent's own behavior. We identify this speculator-agent gap and show that the target agent itself is a strong next-call s...
  </details>

- **2026-07-28** — Bo-Shiun Shen, Son-Hsien Chen — [Macroscopic wall pressure and microscopic contact load in crowds without egress: social-group cohesion and boundary buffering](http://arxiv.org/abs/2607.25780v1)
  <details><summary>📄 Abstract</summary>
  Crowd safety in confined venues is usually evaluated through evacuation performance or pre-collision avoidance, while direct mechanical hazards in dense gatherings without egress remain poorly understood. We study an Elastic Reorientation Model (ERM), a Social Force Model (SFM), and their coupled dynamics. Post-collision behavior is represented by social-group cohesion ($γ_g$) and wall buffering ($γ_w$), while risk is quantified by the macroscopic wall line pressure ($P_{\text{wall}}$) and the m...
  </details>

- **2026-07-28** — Thomas Hickling, Dylan Wynne, Yu Su et al. — [Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller](http://arxiv.org/abs/2607.25728v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop. This integrate-in-world, act-in- ego design enables consistent multi-UAV spatial fusion whilst retaining decentralised co...
  </details>

- **2026-07-28** — Sam Relins, Daniel Birks — [Why Public Service AI Governance Frameworks Risk Failing in the Age of General-Purpose AI: Lessons from Policing](http://arxiv.org/abs/2607.25648v1)
  <details><summary>📄 Abstract</summary>
  Public services face growing pressure to adopt artificial intelligence (AI) to close the gap between rising demand and falling resources. That pressure has intensified with general-purpose AI (GPAI): AI built on large language models that can be directed by prompt alone to perform an effectively unbounded range of tasks. We argue that the properties that make these models attractive - their generality, accessibility, and low deployment cost - undermine the conditions under which AI safety has hi...
  </details>

- **2026-07-28** — Federico Cabitza, Gianluca Colombo — [Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines](http://arxiv.org/abs/2607.25620v1)
  <details><summary>📄 Abstract</summary>
  Quattrociocchi and colleagues warn that the fluent outputs of large language models may allow linguistic plausibility to substitute for epistemic evaluation, producing the condition they call *Epistemia*: the experience of possessing knowledge without undertaking the practices through which judgment would ordinarily be warranted. This article accepts that diagnosis but challenges its explanatory framework, which compares an embodied, socially situated human knower with an isolated generative mod...
  </details>

- **2026-07-28** — Weiming Zhuang, Jiabo Huang, Jingtao Li et al. — [Argus-Unified: Towards A Compact and Economical Unified Model for Image Understanding and Generation](http://arxiv.org/abs/2607.25527v1)
  <details><summary>📄 Abstract</summary>
  Unifying visual understanding and generation in one model holds immense promise, but remains challenging and expensive due to heavy compute and data demands and conflicts between the visual features needed for these two capabilities. To address these challenges, we present Argus-Unified, a compact, effective and unified multimodal model built with low demand on computation and data. Instead of aligning modalities from scratch, Argus-Unified effectively leverages pretrained vision-language models...
  </details>

- **2026-07-28** — Huan Chen, Xiang Song, Jian Jin et al. — [Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm](http://arxiv.org/abs/2607.25446v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. Classic organizational theory (Belbin roles, Mintzberg coordination, RACI accountability) becomes executable, validated configurati...
  </details>

- **2026-07-28** — Jiaran Ye, Lingxu Ran, Zijun Yao et al. — [Where Steering Signals Come From: Activation Source Selection in Activation Steering](http://arxiv.org/abs/2607.25270v1)
  <details><summary>📄 Abstract</summary>
  Activation steering controls language models by adding vectors or features to hidden states at inference time, but the upstream source of these steering signals is often treated as a secondary detail. We study this source choice as activation source selection: the combination of source context and activation readout policy used to collect the hidden states from which a steering signal is built. Holding the downstream intervention fixed, we show across three instruction-tuned models and four stee...
  </details>

- **2026-07-28** — Ghazal Kaviani, Ghassan AlRegib — [FORGE: Frame Orthogonality in Relevance Geometry for Long-Form Video Understanding](http://arxiv.org/abs/2607.25266v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have enabled long-form video understanding at a scale that was not previously possible. However, the density of relevant content decreases sharply as video sequence length increases, and exposing the model to more irrelevant content measurably reduces its accuracy. In this paper, we address the problem of maximizing query-relevant information in a frame subset selected at inference time, without training. FORGE (Frame Orthogonality in Relevance Geometry) ...
  </details>

- **2026-07-28** — Yixuan Duan, Arjun Naik, Sadeer Al-Kindi et al. — [CADENCE: A Cardiac Atom Dictionary for Interpretable Neural Concept Extraction from ECG Foundation Models](http://arxiv.org/abs/2607.25244v1)
  <details><summary>📄 Abstract</summary>
  Foundation models for 12-lead electrocardiograms (ECGs) transfer well across clinical tasks, but the physiological knowledge encoded in their representations remains opaque. We present CADENCE, a framework that decomposes an ECG foundation model into a human-interpretable, queryable dictionary of physiological concepts. Using a BatchTopK sparse autoencoder, CADENCE factorizes Layer-6 embeddings from more than nine million ECG tokens into 8,192 sparse cardiac atoms. These atoms align better than ...
  </details>

- **2026-07-28** — Weiqi Huang, Dianyi Yang, Jiaxin Li et al. — [SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](http://arxiv.org/abs/2607.25219v1)
  <details><summary>📄 Abstract</summary>
  Social navigation has progressed from simplified 2D environments toward a more general vision-based setting, in which a robot needs to achieve socially compliant behavior purely from onboard visual observations. Yet supporting simulation platforms have not kept pace: existing options either lack visual observations, lack moving human avatars, or fall short of real-world fidelity in appearance and pedestrian behavior, offering limited support for advancing vision-based social navigation. We intro...
  </details>

- **2026-07-28** — Shutong Qiao, Wei Yuan, Tong Chen et al. — [VaLiDRec: Variable-Length LLM-Aligned Semantic IDs for Generative Recommendation](http://arxiv.org/abs/2607.25209v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation commonly represents items using fixed-length semantic identifiers (SIDs) constructed through clustering and quantization. However, these artificial codes may overcompress item semantics, remain misaligned with pretrained LLM vocabularies, and require costly autoregressive decoding. In light of this, we propose VaLiDRec, a generative recommendation framework based on variable-length, LLM-aligned semantic identifiers. VaLiDRec constructs SIDs directly from informative nat...
  </details>

- **2026-07-28** — Xiao Li, Mouxiao Bian, Zhaodi Wu et al. — [MyoCardBench: A Real-World Data Benchmark for Evaluating Large Language Models in Clinically Authentic Cardiovascular Care Scenarios](http://arxiv.org/abs/2607.25186v1)
  <details><summary>📄 Abstract</summary>
  Background: Most medical large language model (LLM) benchmarks focus on examination knowledge or isolated tasks and may not reflect the longitudinal, multimodal, and safety-critical workflow of cardiovascular care. Objective: To develop MyoCardBench, a real-world benchmark spanning the cardiovascular care continuum, and assess LLM performance across clinical dimensions and specialist tasks. Methods: MyoCardBench includes 2,263 items from 13 task-specific datasets derived from de-identified cardi...
  </details>

- **2026-07-28** — Elan Barenholtz — [A scaling law of contextual persistence in human language](http://arxiv.org/abs/2607.25184v1)
  <details><summary>📄 Abstract</summary>
  Human language exhibits lawful structure at the level of words (frequency, vocabulary growth) and word pairs (co-occurrence across distance). Here we show that the arrangement of words in sequence -- a central determinant of meaning -- obeys a comparable law. Using large language models as probabilistic probes, we measured the reduction in target perplexity conferred by prior context at distance d beyond that of the same words scrambled; this difference, the contextual persistence function P(d),...
  </details>

- **2026-07-28** — Sungjae Park, Shubham Tulsiani — [$π\mathbf{R}^2$: Reactive Real-time Flow Policies](http://arxiv.org/abs/2607.26055v1)
  <details><summary>📄 Abstract</summary>
  Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones. Such chunks run open-loop, so the policy cannot react to sensory input arriving mid-execution, sacrificing \emph{reactivity}. Replanning more often would restore it, but the perception-to-action pipeline (a large backbone plus multiple denoising steps) is too slow: this \emph{latency} forbids frequent replanning and leaves committed actions stale, making such policies...
  </details>

- **2026-07-28** — Samantha V. Barron, Bradley Mitchell, Vinay Tripathi et al. — [Observable Estimation in the Absence of Classical Verification](http://arxiv.org/abs/2607.25998v1)
  <details><summary>📄 Abstract</summary>
  The predictive success of quantum mechanics underpins many areas of modern science, even as the exact simulation of large, interacting quantum systems remains beyond the reach of classical computation. This success has been enabled by the remarkable advancement of scalable numerical approximation methods, which often demonstrate practical accuracy despite the absence of formal guarantees. As quantum simulation pushes into regimes where these approximations struggle, a fundamental challenge arise...
  </details>

- **2026-07-28** — Huy Ha, C. Karen Liu, Shuran Song — [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](http://arxiv.org/abs/2607.25798v1)
  <details><summary>📄 Abstract</summary>
  An often overlooked factor of robot manipulation performance is the embodiment of the robot itself. Motivated by this problem, we study motion-conditioned robot co-design, where the goal is to generate complete robot designs that track target end-effector trajectories (from human demonstrations) while optimizing user-defined rewards. We introduce Transformer Transformer, a diffusion transformer trained on RoboTokens, a unified tokenization of robot embodiments, states, and actions. The same arch...
  </details>

- **2026-07-28** — Yizhou Chen, Hang Xu, Dongjie Yu et al. — [Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations](http://arxiv.org/abs/2607.25397v1)
  <details><summary>📄 Abstract</summary>
  Successfully automating dexterous, long-horizon robotic manipulation requires frameworks capable of both high-level reasoning and fine-grained execution. Traditional task and motion planning (TAMP), while excellent at symbolic planning, is often brittle in contact-rich operations. Simultaneously, imitation learning (IL), while effective in manipulation tasks with visual feedback, is limited by its low capability in spatial generalization and multi-stage operation. To reconcile their complementar...
  </details>

- **2026-07-28** — Fengxiang Wang, Jiangnan Huang, Mingshuo Chen et al. — [Beyond Zooming: Learning Multi-Tool Visual Reasoning for Ultra-High-Resolution Remote Sensing](http://arxiv.org/abs/2607.25993v1)
  <details><summary>📄 Abstract</summary>
  Ultra-high-resolution (UHR) remote-sensing (RS) imagery provides fine-grained Earth-observation evidence over city-scale scenes, but poses a fundamental challenge for multimodal large language models (MLLMs): task-relevant evidence is often sparse, local, and spatially dispersed across extremely large visual contexts. A natural solution is to equip MLLMs with zoom-in tools for active local inspection. However, through a pilot study on XLRS-Bench, we find that zoom-in is only partially effective:...
  </details>

- **2026-07-28** — Shuyue Wei, Chang Liu, Zimu Zhou et al. — [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](http://arxiv.org/abs/2607.25992v1)
  <details><summary>📄 Abstract</summary>
  Recently, memory management has become a key infrastructure for LLM-based agents, as it directly affects long-horizon reasoning, personalized responses, and knowledge reuse. However, existing LLM memory systems typically adopt a coarse-grained (utility-agnostic) manner that treats heterogeneous user-LLM interaction records uniformly, leading to redundant and low-impact records persisting in the memory repository. To address this challenge, we present MemLens, a value-aware memory management syst...
  </details>

- **2026-07-28** — Rahat Rizvi Rahman, Mia Mohammad Imran, Kostadin Damevski — [A Low-Cost Human-in-the-Loop Investigation of Toxicity on GitHub at Scale](http://arxiv.org/abs/2607.25946v1)
  <details><summary>📄 Abstract</summary>
  Toxic interactions in open source discussions can alienate contributors and threaten project sustainability, yet prior empirical studies of GitHub toxicity have been limited in scale, raising questions about their generalizability. Scaling up is difficult because toxicity on GitHub is often implicit and context-dependent, making both fully manual annotation and LLM-based labeling unreliable.   We present a human-in-the-loop (HITL) annotation methodology that makes large-scale, domain-calibrated ...
  </details>

- **2026-07-28** — Ana Melissa P. Brito, Neha Bura, Pablo Botella et al. — [Pressure-Induced Irreversible Disorder in $β^{\prime}$-Mn$_3$(PO$_4$)$_2$: A High-Pressure X-ray Diffraction and Density-Functional Theory Study](http://arxiv.org/abs/2607.25896v1)
  <details><summary>📄 Abstract</summary>
  The high-pressure structural behavior of $β^\prime$-Mn$_3$(PO$_4$)$_2$ was investigated using synchrotron X-ray diffraction up to 20 GPa combined with density-functional theory calculations. At ambient conditions, $β^\prime$-Mn$_3$(PO$_4$)$_2$ crystallizes in a monoclinic structure that exhibits strongly anisotropic compression. The pressure dependence of the unit-cell volume was described using a third-order Birch--Murnaghan equation of state, and the principal axes of compressibility were dete...
  </details>

- **2026-07-28** — S. Mitra, S. E. Lakhal, C. P. Connaughton et al. — [A Two-Regime Statistical Framework for Wind-Power Distributions: From Wind-Speed Fluctuations to Turbine Control](http://arxiv.org/abs/2607.25863v1)
  <details><summary>📄 Abstract</summary>
  Wind-power variability is a major challenge for the reliable integration of utility-scale wind energy into modern power systems. Although wind-speed statistics are often described by simple parametric distributions, translating these statistics into turbine-level power fluctuations is nontrivial because the relationship between wind speed and power is highly nonlinear and changes across different turbine operating regimes. Here, we develop a two-regime statistical framework for wind-power distri...
  </details>

- **2026-07-28** — Tiecheng Cai, Zexian Yang, Chao Chen et al. — [Towards Faithful Sentimental Image Captioning via Evidence-Aware Multi-Agent Reasoning](http://arxiv.org/abs/2607.25789v1)
  <details><summary>📄 Abstract</summary>
  Sentimental Image Captioning (SIC) requires balancing emotional expression with visual fidelity. Existing methods often struggle with this trade-off, leading to hallucinations due to insufficient local grounding and the lack of sentimental verification mechanisms. To address these limitations, we propose SEA-Cap, a Sentiment-Evidence-Aware Multi-Agent System for faithful and evidence-grounded sentimental image captioning. SEA-Cap incorporates a Sentiment Evidence Miner that extracts structured, ...
  </details>

- **2026-07-28** — Hyunkyung Han, Min Jung Kim — [Loss Invariance Determines What Concept Layers Encode: Volume Grounding in Echocardiography](http://arxiv.org/abs/2607.25748v1)
  <details><summary>📄 Abstract</summary>
  Objective: Concept bottleneck models route prediction through interpretable intermediate variables, and their validity is normally judged by how accurately those variables are predicted. We ask whether that judgement is sufficient, using left ventricular volumes as the concepts underlying ejection fraction estimation from echocardiographic video.   Methods: A video transformer encoder was trained on a publicly available echocardiography dataset. End-systolic and end-diastolic volumes formed a co...
  </details>

- **2026-07-28** — Javier Irigoyen, Roberto Daza, Francisco Jurado et al. — [AIriskEval-edu Demo: Auditing of Pedagogical Risks in Educational Explanations](http://arxiv.org/abs/2607.25634v1)
  <details><summary>📄 Abstract</summary>
  We present AIriskEval-edu Demo, a platform that audits the pedagogical quality of instructional explanations and provides explainable audit results. The platform evaluates an explanation against a rubric covering five dimensions of pedagogical risk: factual accuracy, depth and completeness, focus and relevance, student-level appropriateness, and ideological bias. For each dimension, it returns a binary decision and a confidence score. Detected risks also include a natural-language rationale and,...
  </details>

- **2026-07-28** — Mary John, Shibili Said, Imad Barhumi et al. — [Matrix-Free Photoacoustic Image Reconstruction via Sensor-Token Self-Attention](http://arxiv.org/abs/2607.25576v1)
  <details><summary>📄 Abstract</summary>
  Photoacoustic tomography (PAT) combines the optical absorption contrast of biological tissue with the spatial resolution of ultrasound, yet recovering the initial pressure distribution from sparse-view sensor measurements remains an ill-posed inverse problem. Iterative compressive-sensing solvers and unrolled deep networks both retain a dependence on the system matrix at inference, which leaves real-time clinical reconstruction computationally expensive. This paper proposes the Sensor Attention ...
  </details>

- **2026-07-28** — Jooyeol Yun, Jintae Park, Hyesu Lim et al. — [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](http://arxiv.org/abs/2607.25565v1)
  <details><summary>📄 Abstract</summary>
  Recovering an editable design file from a raster image is a common and costly bottleneck in modern design workflows, yet remains challenging since editability depends on recovering multi-modal attributes, such as typography, vector geometry, colors, grouping, and layer ordering. We present ReDesign, an agentic framework that grows an editable layer hierarchy by selecting and composing specialized tools across modalities. To keep this long decision process reliable despite imperfect tool outputs,...
  </details>

- **2026-07-28** — Anis Ur Rahman — [DensFiLM: Density-Conditioned Video Saliency for Crowd Scenes](http://arxiv.org/abs/2607.25465v1)
  <details><summary>📄 Abstract</summary>
  Video saliency models typically apply a single fixation strategy across crowd scenes, despite systematic changes in attention with crowd density. Sparse scenes encourage tracking individuals, whereas dense scenes shift attention toward collective motion and scene-level landmarks. We introduce DensFiLM, a density-conditioned video saliency model that inserts a lightweight Feature-wise Linear Modulation layer at the bottleneck of a Video Swin Transformer. A learned density embedding produces chann...
  </details>

- **2026-07-28** — Siyuan Xu, Yan Wang, Haofei Song et al. — [Towards Reliable Stain Transfer: An Iterative Data-Model Co-Optimization Framework Based on Multimodal Expert-Guided Assessment](http://arxiv.org/abs/2607.25393v1)
  <details><summary>📄 Abstract</summary>
  Histopathological examination primarily relies on hematoxylin and eosin (H&E) and immunohistochemistry (IHC) staining. Although IHC provides critical molecular information, it is costly and requires specialized expertise. Stain transfer provides an efficient alternative by computationally generating IHC from H&E images, but remains challenged by unified and interpretable modeling for heterogeneous biomarkers under pixel-unaligned supervision. We propose DMCoStain, a novel Data-Model Co-optimizat...
  </details>

- **2026-07-28** — Ruijie Su, Yuanzhi Liang, Xiaohua Xie et al. — [Physics-Grounded Fluid Video Generation with a Simulation Dataset and Dual-Stream Optical-Flow Supervision](http://arxiv.org/abs/2607.25321v1)
  <details><summary>📄 Abstract</summary>
  Video diffusion models generate visually compelling content but routinely violate elementary physics when the subject involves fluids: liquid columns break apart in mid-air, container water levels fail to rise as liquid is poured in, and splashes disperse without regard to momentum or gravity. We attribute this gap to the fact that large-scale video-text corpora contain almost no explicit motion supervision, so models learn to imitate fluid appearance rather than dynamics. We address this with t...
  </details>

- **2026-07-28** — Deepani Hemachandra, Jagath Senarathne, Mahasen Dehideniya — [A Copula-Based Regression Framework for Enhanced Prediction under Heteroscedasticity](http://arxiv.org/abs/2607.25250v1)
  <details><summary>📄 Abstract</summary>
  Classical regression approaches, including ordinary least squares, rely on strong assumptions such as constant variance and normality of residuals, which are often violated in real-world data. Although log-transformation is commonly used to stabilise variance, it may introduce re-transformation bias and fail to address heteroscedasticity and asymmetric dependence structures adequately. To overcome these limitations, this study proposes a copula-based regression framework for modelling data in th...
  </details>

- **2026-07-28** — Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin — [WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing](http://arxiv.org/abs/2607.25234v1)
  <details><summary>📄 Abstract</summary>
  Stereo depth estimation for driving, robotics and augmented reality must run at high resolution under tight latency budgets, yet in transformer-based matchers the global self-attention that aggregates scene context grows quadratically with the number of pixels and comes to dominate runtime. We show that the joint self-attention stage of a stereo transformer, whose role is to spread context across both views, can be replaced by a data-independent Walsh-Hadamard token mixer that mixes tokens globa...
  </details>

- **2026-07-28** — Liexin Cheng, Xue Cheng, Shuaiqiang Liu et al. — [RIDGE: An Autonomous Framework for Validation and Method Discovery in LLM-Generated Option Pricing](http://arxiv.org/abs/2607.25199v1)
  <details><summary>📄 Abstract</summary>
  Automated code generation is becoming an important tool in quantitative finance, where large language models can generate option pricing implementations directly from mathematical model specifications. Validating such implementations, however, requires considerably more than conventional software testing: numerical pricing methods must remain mathematically consistent, numerically stable, and reliable across a wide range of model parameters.   We introduce RIDGE, an autonomous validation framewo...
  </details>

- **2026-07-28** — Howard Su, Huan-Hsin Tseng, Chi-Sheng Chen et al. — [Quantum Transformer BSDE Solver via Multi-Layer Fully-Connected Variational Quantum Circuits](http://arxiv.org/abs/2607.25162v1)
  <details><summary>📄 Abstract</summary>
  Solving high-dimensional parabolic partial differential equations (PDEs) is important in engineering, physics, and stochastic control. Deep BSDE methods reformulate semilinear PDEs as backward stochastic differential equations and admit a model-based reinforcement learning interpretation, where trajectories are generated from known stochastic dynamics while a trainable model learns the gradient-related control process. We propose a Quantum Transformer BSDE solver based on Multi-Layer Fully-Conne...
  </details>

- **2026-07-28** — Dorin Dumitraşcu, Liviu Suciu — [On the Irreducibility of the Differential Operators Associated to Random Walks in the Standard Euclidean Lattice](http://arxiv.org/abs/2607.25160v1)
  <details><summary>📄 Abstract</summary>
  For a positive integer $d\geq 1$, we consider the sequences $(A_{n}^{(d)})_n$ and $(x_{n}^{(d)})_n$ given by $$ A_{n}^{(d)} =\sum_{n_1+\dots+n_d=n} \frac{(2n)!}{(n_1!)^2 (n_2!)^2 \dots (n_d!)^2} \quad \text{ and } \quad x_{n}^{(d)} = \frac{A_{n}^{(d)}}{\binom{2n}{n}}. $$ They have rich combinatorial interpretations, but we focus on the analytical properties of their generating functions $A_d$ and $F_d$. We use a modified Borel transform, and algebraic and combinatorial considerations to prove th...
  </details>

- **2026-07-28** — Shivanshu Tripathi, Hamed Mohsenian-Rad, Maziar Raissi — [VeraGrid-Agent: Tool-Augmented LLMs for Distribution Optimal Power Flow at the Grid Edge](http://arxiv.org/abs/2607.25155v1)
  <details><summary>📄 Abstract</summary>
  Language models have demonstrated remarkable success in solving a wide range of tasks. However, answering complex scientific questions about the power flow often requires solving the distribution optimal power flow (D-OPF) problem. These questions call for numerical solvers and simulators, as linguistic reasoning from parametric knowledge often gives incorrect answers. In this work, we present VeraGrid-Agent, a tool-augmented LLM that autonomously writes the simulator input, executes the open-so...
  </details>

- **2026-07-27** — Shiwei Tan, Yusong Zhao, Weiyi Qin et al. — [Interpretable GOHR Agents via Sparse Autoencoders](http://arxiv.org/abs/2607.25132v2)
  <details><summary>📄 Abstract</summary>
  A central challenge in interpreting learned decision-making systems is to determine whether their internal representations contain concepts that help explain their behavior. We report interpretability experiments for a tokenized autoregressive Transformer agent in the Game of Hidden Rules (GOHR). We focus on a compact two-rule task in which both hidden rules map object shapes to target buckets, but with different permutations. The policy is trained on episodes sampled from these two hidden rules...
  </details>

- **2026-07-27** — Mingzhi Xu, Yizhe Zhang — [ESRVS: Extreme Semi-Supervised Retinal Vessel Segmentation with a Single Annotated Image](http://arxiv.org/abs/2607.24453v1)
  <details><summary>📄 Abstract</summary>
  Learning from minimal human supervision is a long-standing goal in medical image analysis, where dense expert annotations are costly. We study retinal vessel segmentation in an extreme semi-supervised setting with one annotated image and a pool of unlabeled images. We propose ESRVS, which selects a representative reference image for manual annotation and transfers vessel cues using target-domain-adapted DINOv3 features. ESRVS constructs a multi granular vessel prototype, combines prototype-simil...
  </details>

- **2026-07-27** — Oleg Grynets, Kyrylo Fursov, Vasyl Lyashkevych et al. — [Specification-Driven DevOps for Multi-Service Environments](http://arxiv.org/abs/2607.25141v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to generate executable software environments from repository artifacts. However, functional executability does not necessarily imply conformity with architectural, security, workflow, and production intent. This study investigates whether a frontier LLM can generate Dockerfiles and Docker Compose configurations for multi-service applications using repository contents without access to developer-authored deployment artifacts. Three heterogeneous ...
  </details>

- **2026-07-27** — Mohan Li, Rama Doddipatla, Philip C. Woodland — [Text-Prompted CLAP: Learning Query-Conditioned Audio Representations via Contrastive Learning](http://arxiv.org/abs/2607.25085v1)
  <details><summary>📄 Abstract</summary>
  Contrastive Language-Audio Pretraining (CLAP) learns aligned text and audio representations in a shared embedding space. However, independent encoding of each modality limits its ability to model cross-modal semantics in complex audio understanding and retrieval tasks. To address this limitation, this paper proposes Text-Prompted CLAP (TP-CLAP), a parameter-efficient extension of CLAP that introduces a cross-attention-based fusion module to incorporate textual prompts into audio features. TP-CLA...
  </details>

- **2026-07-27** — Dengzhe Hou, Lingyu Jiang, Fangzhou Lin et al. — [CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification](http://arxiv.org/abs/2607.25045v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) analysis in cognitive studies requires specialized expertise and involves many defensible choices over contrasts, channels, time windows, and statistical tests. LLM agents can translate varied natural-language questions into analysis choices, offering a flexible interface for automation. Yet fluent reports alone cannot establish that an agent selected the requested analysis or evaluated a confirmatory claim independently of adaptive search. We present CogEEGAgent, a ...
  </details>

- **2026-07-27** — Dengzhe Hou, Lingyu Jiang, Fangzhou Lin et al. — [CogArena: A Multimethod Evaluation of Cognitive Ability Structure in Large Language Models](http://arxiv.org/abs/2607.24999v1)
  <details><summary>📄 Abstract</summary>
  LLM cognitive scores are increasingly summarized as per-ability profiles whose dimensions should converge across tasks, respond selectively to matched interventions, and generalize beyond the models used to define them. We introduce CogArena, a procedurally generated 13-paradigm benchmark built around a multimethod framework for determining when cognitive-task scores warrant dimensional labels across five theory-motivated groupings. Across 55 open-weight models, nearly all paradigm correlations ...
  </details>

- **2026-07-27** — Hangjie Yuan, Yichen Qian, Zhiwei Tang et al. — [ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding](http://arxiv.org/abs/2607.24743v2)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) hold immense potential to revolutionize clinical practice, yet deploying them in the medical domain is fundamentally a vision-centric challenge: models must absorb knowledge from heterogeneous 2D and 3D medical images, and evaluation protocols must align with radiologists' clinical practice and provide an accurate, fine-grained and factualness-driven assessment. In this paper, we introduce ClinFusion, a vision-centric MLLM designed for holistic medical un...
  </details>

- **2026-07-27** — Shaker Al-Tamari, Waled Kadour — [Explainable Reinforcement Learning via Physics-Aware Policy Distillation](http://arxiv.org/abs/2607.24672v1)
  <details><summary>📄 Abstract</summary>
  In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This paper presents an experimental study aimed at making high-performance continuous control DRL systems interpretable. A policy distillation framework is implemented using the classic Inverted Pendulum b...
  </details>

- **2026-07-27** — Zhenhan Gao, Marvin Muñoz Barón, Umm-e Habiba et al. — [Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review](http://arxiv.org/abs/2607.24601v1)
  <details><summary>📄 Abstract</summary>
  Background: Large language models (LLMs) are increasingly used to automate code review, but the reasoning behind their decisions remains hard to understand. Developers struggle to assess the validity of LLM-generated reviews, making it difficult to gauge how much trust to place in them. The role of Explainable AI (XAI) in code review and its impact on trust remain underexplored.   Objective: We study the influence of XAI on developer trust in AI-assisted code reviews.   Method: We conducted a wi...
  </details>

- **2026-07-27** — Jan Range, Björn Schembera, Dominik Göddeke — [Making Mathematical Knowledge Explainable, Accessible and Interoperable Through Large Language Model Integration](http://arxiv.org/abs/2607.24512v1)
  <details><summary>📄 Abstract</summary>
  Mathematical models are central to formalizing research problems, yet their documentation often falls short of FAIR principles. Knowledge bases such as the Mathematical Model Database (MathModDB) address this gap by providing curated, semantically rich representations of mathematical models. Built on Wikibase, the same open-source infrastructure underlying Wikidata, MathModDB utilizes Semantic Web technologies to support Linked Open Data, collaborative editing, and the storage of semantically en...
  </details>

- **2026-07-27** — Liwei Dong, Jiahao Zhao, Nan Xu — [From Execution to Capability: Scientific Experience Consolidation via Procedural Knowledge Synthesis](http://arxiv.org/abs/2607.24459v2)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly solve scientific-computing tasks, but executable feedback from one problem rarely becomes durable capability on subsequent problems. We study scientific-computing experience consolidation: converting verified runtime experience into transferable procedural knowledge and persistent model improvement. This setting presents two challenges: trajectory-derived artifacts may encode source-specific repairs rather than cross-task computational mechanisms; and a weaker ...
  </details>

- **2026-07-27** — Yifan Hu, Shuwei He, Rui Liu et al. — [Let Me Look at You: Advanced Facial Expression Modeling for Conversational Speech Synthesis](http://arxiv.org/abs/2607.24430v1)
  <details><summary>📄 Abstract</summary>
  Conversational Speech Synthesis is a fundamental component of human-computer interaction, aiming to generate contextually appropriate, expressive, and empathetic speech. However, facial expressions encode subtle and rich affective cues that are crucial for empathetic speech interaction, whereas existing approaches often overlook this important modality. In addition, the lack of large-scale natural conversational datasets with both speech and visual modalities also limits the development of visua...
  </details>

- **2026-07-27** — Kai Syun Hou, James Kwok — [Rethinking the Generation Order of Block Diffusion Language Models](http://arxiv.org/abs/2607.24306v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models enable flexible arbitrary-order generation, but existing sampling methods are mostly designed for early masked diffusion models (MDMs). In this work, we study sampling for recent block diffusion language models (BDLMs). We show empirically and analytically that these models are naturally more aligned with left-to-right decoding than MDMs. Based on this observation, we propose Parallel Autoregressive Decoding (PARD), a simple training-free sampling method that preserves ...
  </details>

- **2026-07-27** — Yueru Luo, Xu Yan, Changqing Zhou et al. — [Reasoning to Regulate: Chain-of-Thought for Traffic Rule Understanding](http://arxiv.org/abs/2607.24199v1)
  <details><summary>📄 Abstract</summary>
  Understanding and complying with traffic regulations is a safety-critical requirement for autonomous driving, yet remains challenging due to the diversity and context dependence of traffic signage. Importantly, regulation understanding is not a simple recognition task, but a reasoning problem: whether a rule applies depends on interpreting the sign in relation to the spatial layout of lanes and scene context. To support such reasoning, MapDR provide fine-grained annotations that link each traffi...
  </details>

- **2026-07-27** — Ya Gao, Peina Zhao, Yiheng Li et al. — [Secrecy Energy Efficiency for IRS-Assisted Low-Altitude Communications: A D3QN-PER Based Approach](http://arxiv.org/abs/2607.24183v1)
  <details><summary>📄 Abstract</summary>
  To address the security and energy efficiency challenges in low-altitude economy (LAE) wireless communications, we develop a secure synergistic network integrating unmanned aerial vehicle (UAV) and intelligent reflecting surface (IRS), with an emphasis on maximizing secrecy energy efficiency (SEE) for downlink transmission scenarios. In particular, firstly, we establish the channel transmission models for UAV-IRS assisted LAE communications network. Then, we formulate a non-convex fractional opt...
  </details>

- **2026-07-27** — Jingwen Zhu, Keshu Wu, Pei Li et al. — [Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety](http://arxiv.org/abs/2607.24168v1)
  <details><summary>📄 Abstract</summary>
  Road crashes remain among the gravest threats to public safety, and preventing them is a defining task of transportation systems worldwide. Much of that harm concentrates at hotspots, yet a hotspot is less a place than an episode; it emerges quietly at an intersection or along an arterial, intensifies for weeks, then subsides, only to reappear elsewhere. Enforcement guided by maps of past crashes inevitably trails this cycle, patrolling yesterday's hotspots while tomorrow's form unwatched. Break...
  </details>

- **2026-07-27** — Qian Li, Zhenyan Qi, Liang Shen et al. — [A Cybersecurity MLPS Large Language Model with Multi-Path Retrieval Fusion](http://arxiv.org/abs/2607.24116v1)
  <details><summary>📄 Abstract</summary>
  The Multi-Level Protection Scheme (MLPS) is a foundational system in China's cybersecurity governance framework. Therefore, accurate analysis and understanding of MLPS requirements are essential. At present, MLPS analysis still relies mainly on manual interpretation of standards and rule-based tools. This makes it hard to provide stable and consistent compliance analysis in complex application scenarios. The rise of large language models has created new opportunities for making MLPS work more in...
  </details>

- **2026-07-27** — Tuan-An To, Yuk-Kwan Wong, Tuan-Anh Vu et al. — [MarineEVT: Advancing Event-Centric Marine Video Understanding via Visual Tool Reasoning](http://arxiv.org/abs/2607.24064v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models (VLMs) have achieved remarkable success in visual understanding, driven by the growing availability of high-quality image-text pairs. However, the performance of VLMs often degrades in the video domain due to the essential need for temporal understanding and the scarcity of large-scale annotated video data. In this work, we focus on marine video understanding, which brings further challenges: first, it requires substantial domain expertise; and video VLMs usually st...
  </details>

- **2026-07-27** — Seoyeon Kim, Minjae Kang, Jaehyung Kim — [SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding](http://arxiv.org/abs/2607.23991v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly controlled through system prompts that specify roles, styles, formats, and safety requirements. However, models follow these prompts only implicitly through in-context learning, which can be insufficient for complex or compositional prompts. Existing approaches often require model tuning or response-level reranking, limiting their practicality for lightweight inference-time control. We introduce SyRuP, a decoding-time framework for improving system-p...
  </details>

- **2026-07-27** — Callie C. Liao, Duoduo Liao, Ellie L. Zhang — [MusiChat: Vibe Composing for Music Creation](http://arxiv.org/abs/2607.24873v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in AI music generation have enabled users to create complete musical pieces from natural-language prompts. However, most existing systems follow a prompt-and-regenerate paradigm, making iterative refinement difficult because users must repeatedly recreate compositions instead of directly evolving existing musical ideas. We present MusiChat, a conversational vibe composing system that enables collaborative human-AI music creation through natural-language interaction and iterative ...
  </details>

- **2026-07-27** — Haodi Fan, Zucong Lan — [From Cognitive Architectures to Language Agents: A Mechanism-Level Review of Lineage, Convergence, and Migration Gaps](http://arxiv.org/abs/2607.23942v1)
  <details><summary>📄 Abstract</summary>
  Memory, planning, reflection, and tool use are often compared as feature labels, obscuring the control semantics that determine how an agent actually runs. This review connects ten historical cognitive architectures, eight language-agent runtime families, and forty-two mechanism-focused modern systems. We reconstruct each mechanism through state, control, transition, persistence, failure, learning, and resource governance, then code evidence relation (E1-E4) separately from migration depth (D0-D...
  </details>

- **2026-07-27** — Yue Zhang, Xiangyu Li, Wanshu Fan et al. — [DDVT: Dynamic Dual-level Vision Transformer Fusion Network for Answer Grounding in Visual Question Answering](http://arxiv.org/abs/2607.23921v1)
  <details><summary>📄 Abstract</summary>
  Answer grounding in visual question answering aims to locate the region from a given natural language question associated with the visual content of an image, which has garnered significant attention due to its practical applications. In this paper, we introduce the Dynamic Dual-level Vision Transformer Fusion Network (DDVT) for answer grounding in visual question answering. Specifically, we propose a question-guided dynamic regional-level module (QGDR) that combines complementary image context ...
  </details>

- **2026-07-27** — Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen — [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](http://arxiv.org/abs/2607.24481v1)
  <details><summary>📄 Abstract</summary>
  Real-world evaluation is a bottleneck in developing generalist robot manipulation policies. Each rollout requires physical hardware and an operator to set up, reset, and score it. We introduce ArmnetBench v0.1, a benchmark run on a fleet of low-cost SO-101 cells under light on-site supervision. v0.1 validates this arm farm end to end and compares 7 policies across 12 tasks with both single-arm and bimanual configurations. Each policy is trained or fine-tuned on 50 demonstrations per task; the be...
  </details>

- **2026-07-27** — Pin Qian, Su Wang, Chong Peng et al. — [When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost](http://arxiv.org/abs/2607.24010v1)
  <details><summary>📄 Abstract</summary>
  Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval. Yet evaluations often leave the operating point underspecified: two systems may both claim a 50% evidence-usage budget while realizing different held-out usage rates, so higher accuracy can reflect a looser budget rather than a better retrieval policy. We study budget-aware evaluation for Active RAG by recasting active retrieval as utili...
  </details>

- **2026-07-27** — Tianyuan Du, Tianyi Hu, Hanting Ye et al. — [SHARE: Towards Head-Mounted AR with User-Centric SLAM in Shared Human-Robot Workspaces](http://arxiv.org/abs/2607.23901v1)
  <details><summary>📄 Abstract</summary>
  Human-Robot Collaboration (HRC) in shared physical spaces using Augmented Reality (AR) interfaces is powered by Simultaneous Localization and Mapping (SLAM). Existing multi-agent SLAM systems rely on an edge server to combine visual findings of multiple resource-constrained agents, perform computation, and schedule updates to their local maps. However, the edge treats all agents uniformly and ignores the fundamentally different latency requirements of heterogeneous HRC agents: robots and head-mo...
  </details>

- **2026-07-27** — Funda Durupinar — [How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation](http://arxiv.org/abs/2607.25140v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outw...
  </details>

- **2026-07-27** — Shiwei Tan, Yusong Zhao, Weiyi Qin et al. — [Interpretable GOHR Agents via Sparse Autoencoders](http://arxiv.org/abs/2607.25132v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in interpreting learned decision-making systems is to determine whether their internal representations contain concepts that help explain their behavior. We report interpretability experiments for a tokenized autoregressive Transformer agent in the Game of Hidden Rules (GOHR). We focus on a compact two-rule task in which both hidden rules map object shapes to target buckets, but with different permutations. The policy is trained on episodes sampled from these two hidden rules...
  </details>

- **2026-07-27** — Manizheh Botshekananfard, Elif Büşra Güraksın, Vasileios A. Letsios et al. — [A discrete series gauge field at the late-time boundary of $dS_4$](http://arxiv.org/abs/2607.25067v1)
  <details><summary>📄 Abstract</summary>
  We study the free Maxwell field on the planar patch of four-dimensional de Sitter spacetime ($dS_4$). We review its bulk canonical quantization in the Bunch-Davies vacuum, and we give a representation-theoretic viewpoint by studying the transformation properties of single-particle states under infinitesimal dS transformations. By taking the late-time limit, we identify two late-time operators with scaling dimensions $Δ=1$ (leading) and $Δ=2$ (subleading). We introduce CFT-inspired inner products...
  </details>

- **2026-07-27** — Getachew K. Befekadu — [Simulation-based parameter estimation via a combination of embedded normalizing flows and implied empirical probabilities under moment restrictions](http://arxiv.org/abs/2607.25026v1)
  <details><summary>📄 Abstract</summary>
  In this work, we present a simulation-based parameter estimation framework for a model defined by a computational simulation of a physical system. We specifically outline an estimation framework consisting of two closely-integrated steps that facilitate an overall end-to-end parameter estimation scheme. The first step involves utilizing an embedded normalizing flow which is used to transform the unknown complex distribution of the residual information into a simple base distribution correspondin...
  </details>

- **2026-07-27** — Ishrat Jahan Eliza, Md Dilshadur Rahman — [Chart-Supported or Model-Supplied? Examining MLLM-Generated Claims for Accessible Visualization](http://arxiv.org/abs/2607.25021v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can connect visualization patterns to external causes, consequences, and domain knowledge, but the evidential basis of these interpretations is often unclear. We present an exploratory study of 102 visualizations from four sources, three MLLMs, and four input conditions that vary access to the image, source-specific accessible chart context, and withheld-context framing. Across 1,224 descriptions, we analyze model-attributed DIRECT, DERIVED, and SPECULATI...
  </details>

- **2026-07-27** — Stefan L. Ludescher, Manuel Mekonnen, Thomas D. Galley et al. — [Quantum reference frames beyond subsystems: a reconstruction and generalization of the perspective-neutral framework](http://arxiv.org/abs/2607.24976v1)
  <details><summary>📄 Abstract</summary>
  We generalize the notion of quantum reference frames (QRFs) to cases where the frame does not necessarily correspond to a tensor factor subsystem, but to a covariant quantum instrument. This unlocks a variety of physical applications: "frames of labeling" for indistinguishable particles, suggesting explanations for the symmetrization postulate and the absence of parastatistics, and yielding a transparent description of the entanglement of bosons and fermions; and relational clocks reproducing th...
  </details>

- **2026-07-27** — Ali Ansari, Yasmin Mohammadi, Farnoush Nili et al. — [ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams](http://arxiv.org/abs/2607.24707v1)
  <details><summary>📄 Abstract</summary>
  Entity-Relationship Diagrams (ERDs) are central to conceptual database design, yet they are typically available only as rendered images rather than machine-readable schemas, limiting AI-assisted database engineering. We introduce ERUnderstand, the first large-scale benchmark for structured understanding of ER diagrams, comprising 2,960 diagrams collected from curated educational sources, real-world schemas, and synthetically generated examples spanning diverse domains, notations, complexity leve...
  </details>

- **2026-07-27** — Yanhao Jia, Jiepeng Wang, Haibin Huang et al. — [MMOE: Modernizing Diffusion Transformers with Efficient Expert Design](http://arxiv.org/abs/2607.24665v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows. AIGC Foundation Models (AFMs), especially diffusion-transformer backbones, have begun to adopt sparse experts, but recent efforts mostly enlarge total parameter counts and sparsity ratios without importing the efficiency mechanisms that made LLM scaling practical, so generation quality is seldom balanced against training and deploymen...
  </details>

- **2026-07-27** — Jinlong Yang, Wenhao Zhang, Kuanwei Lin et al. — [CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding](http://arxiv.org/abs/2607.24582v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding increasingly relies on large vision-language models and tool-augmented reasoning, but most systems apply the same inference procedure to every example regardless of difficulty. This uniform strategy invokes unnecessary tool-assisted processing for easy questions and provides limited control when difficult questions require fine-grained temporal evidence. We propose CADER (Confidence-Aware Dynamic Evidence Reasoning), a training-free framework for adaptive and reliable lo...
  </details>

- **2026-07-27** — Shuo Wang, Kai Zhang, Wenyuan Huang et al. — [DeCoRAG: Cognitive Decoupling and Semantic-Aware Cropping for Complex Document Understanding](http://arxiv.org/abs/2607.24554v1)
  <details><summary>📄 Abstract</summary>
  Advancing multimodal retrieval-augmented generation (RAG) for complex document understanding presents a formidable dual dilemma of accuracy and efficiency, particularly in graph RAG. Processing structurally sparse yet visually dense layouts, such as extracting a tiny data marker from a financial chart, often incurs computationally prohibitive token overhead while still triggering catastrophic hallucination. However, multimodal Graph RAG pipelines rely on graph-construction stages that assume Vis...
  </details>

- **2026-07-27** — Kaiyang Ye, Yuan Ge, Junxiang Zhang et al. — [FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models](http://arxiv.org/abs/2607.24522v1)
  <details><summary>📄 Abstract</summary>
  While on-policy distillation (OPD) effectively addresses sparse rewards and exposure bias in large language model post-training, its extension to flow models remains underexplored. To this end, we propose Flow Continuous Trajectory Supervision (FlowCTS), which matches subsequent student and reference trajectories initialized from the same student-visited state. Using the integral relation between trajectories and velocity fields, we derive a temporally weighted velocity-matching upper bound and ...
  </details>

- **2026-07-27** — Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen et al. — [LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models](http://arxiv.org/abs/2607.24892v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned time-series forecasting predicts a series from both its numerical history and natural-language context, allowing forecasts to account for events and constraints that the past alone cannot reveal. This requires both reliable numerical forecasting and the ability to interpret contextual information. Time-series foundation models (TSFMs) provide strong numerical forecasts, while large language models (LLMs) can reason over text, but combining their strengths remains challenging bec...
  </details>

- **2026-07-27** — Jiahao Xie, Zhongbin Guo, Qianle Wang et al. — [DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes](http://arxiv.org/abs/2607.24516v1)
  <details><summary>📄 Abstract</summary>
  While data curation for Vision Language Models (VLMs) is increasingly active, public practice for constructing pretraining mixtures remains largely heuristic: practitioners stack datasets that pass quality filters, set cross-domain ratios by intuition, and lack a principled, attributable criterion for admitting new data, while frontier recipes remain undisclosed. We formulate data construction as a systematic mixture-optimization problem and turn it into a reproducible engineering discipline by ...
  </details>

- **2026-07-27** — Brittany Harbison, Ashok K. Goel — [LEX-EC: A Lexical Evidence-Channel Audit Framework for Zero-Shot LLM Personality Classification in Black-Box Settings](http://arxiv.org/abs/2607.24435v1)
  <details><summary>📄 Abstract</summary>
  Large language models may easily assign personality labels from text, but model interpretability remains an open problem. To address this gap, we introduce LEX-EC, a reusable black-box audit framework combining prevalence and agreement diagnostics with controlled lexical ablation to distinguish marginal-distribution effects from trait-associated signal recoverable under restricted evidence. Using this framework, we illustrate how various text genres may exhibit sharply different profiles: free-f...
  </details>

- **2026-07-27** — Shaofei Lei — [MAViE: A Multi-scale Adaptive Vision Encoder for Fine-grained Visual Perception and Efficient Multimodal Reasoning](http://arxiv.org/abs/2607.24424v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models commonly project all tokens produced by a pretrained vision encoder into a large language model. However, final-layer features can discard text, local attributes, and spatial relationships, while high-resolution inputs substantially increase context length and inference latency. We introduce \method, a Multi-scale Adaptive Vision Encoder. \method uses position-dependent gates to fuse shallow, intermediate, and deep features from a vision Transformer, preserving global sema...
  </details>

- **2026-07-27** — Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira et al. — [IJCB-AFMFR 2026: Competition on Adapting Foundation Models for Face Recognition Using Synthetic Training Data](http://arxiv.org/abs/2607.24422v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a summary of the Competition on Adapting Foundation Models for Face Recognition Using Synthetic Training Data (AFMFR), held at the 2026 International Joint Conference on Biometrics (IJCB 2026). The competition received a total of eight valid submissions from four distinct teams across two complementary tracks: a Full Data Track, in which participants adapt the CLIP ViT-L/14 foundation model using large-scale synthetic identity data, and a Limited Data Track, designed to refle...
  </details>

- **2026-07-27** — Priyansh Srivastava — [The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenization for Indian Languages](http://arxiv.org/abs/2607.24276v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) process text through subword tokenizers rather than directly reading characters or words. Because these tokenizers are trained predominantly on English-centric corpora, they introduce a systematic and often overlooked disadvantage for many non-English languages. In this work, we quantify this tokenizer tax for Indian languages using the FLORES-200 parallel corpus, measuring tokenization fertility across six widely used tokenizers and fourteen languages. Under cl100k_...
  </details>

- **2026-07-27** — Yu Cui, Yi Xu, Jiahao Wang et al. — [SpecFormer: Mitigating Embedding and Attention Collapse via Spectral-Aware Transformer for Recommendation](http://arxiv.org/abs/2607.24025v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectures have achieved remarkable success across diverse domains; however, directly applying their standard self-attention mechanism to recommendation often yields suboptimal performance, sometimes even trailing behind well-designed simple recommendation models. In this paper, we reveal that this performance bottleneck stems from severe embedding and attention collapse unique to recommendation scenarios. The heterogeneity and long-tail nature of recommendation data lead to a sev...
  </details>

- **2026-07-27** — Younggue Bae — [MEMOIR: Temporal Behavioral Memory for Recommendation Across the Preference-Drift Spectrum](http://arxiv.org/abs/2607.23986v1)
  <details><summary>📄 Abstract</summary>
  We propose MEMOIR, a framework that segments user interaction histories into temporal windows, generates semantic behavioral memory for each period using an LLM, and aggregates current state, evolution direction, and predicted future into a single user representation. On the Electronics and Clothing_Shoes_and_Jewelry categories of Amazon Reviews 2023, MEMOIR is statistically tied with UniSRec, the strongest baseline, on aggregate NDCG@10 (0.0643 vs. 0.0641), splitting the four reported metrics 2...
  </details>

- **2026-07-26** — Chi Phan, Tianyi Zhang, Yufeng Wu et al. — [PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis](http://arxiv.org/abs/2607.23794v1)
  <details><summary>📄 Abstract</summary>
  Pathological diagnosis is inherently multi-scale, requiring the integration of global tissue architecture at low magnification with cellular morphology at higher magnification. However, existing pathology benchmarks and vision-language models (VLMs) are still largely developed under single-scale settings, limiting their ability to learn clinically meaningful multi-magnification reasoning. Moreover, naively constructed visual question answering (VQA) tasks may be susceptible to text-only or super...
  </details>

- **2026-07-26** — Kartik Teotia, Helge Rhodin, Hyeongwoo Kim et al. — [STEER: Steerable Dyadic Head Avatars](http://arxiv.org/abs/2607.23840v1)
  <details><summary>📄 Abstract</summary>
  Facial movement and expression are central to face-to-face communication, conveying turn-taking, attention, agreement, and engagement alongside speech. While speech-driven facial animation has made strong progress in lip synchronization and audio-conditioned motion generation, most methods treat conversational behavior as an emergent byproduct of audio, or expose only coarse sequence-level affect control. As a result, key non-verbal channels such as gaze contact and aversion, rhythmic head motio...
  </details>

- **2026-07-26** — Deovrat Mehendale, Aditya Mehndiratta, Dhruv Rathi et al. — [Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages](http://arxiv.org/abs/2607.23808v1)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce Indic DiarBench, a speaker diarization and ASR benchmark dataset spanning all 22 scheduled languages of India. This corpus comprises approximately 108 hours of natural multi-speaker audio from near-field meetings, far-field recordings, and in-the-wild audios. All annotations are human-corrected with time-aligned speaker attributed transcriptions. The dataset captures conversational nuance prevalent in Indian speech, such as English code-mixing, dialectal variation, and...
  </details>

- **2026-07-26** — NeoteAI Team, Fudan TEAI Team — [$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](http://arxiv.org/abs/2607.23783v1)
  <details><summary>📄 Abstract</summary>
  We present $N_0$-TWAM, a tactile-native world-action model for contact-rich manipulation that predicts both future vision and future contact. To our knowledge, it is the first tactile world-action model trained at large scale, and it shows strong capability on contact-rich tasks. We pre-train $N_0$-TWAM at large scale with visuo-tactile joint training over tactile-rich demonstrations spanning six embodiments and 450 tasks. We use NeoForce, a unified force-based tactile representation, to form a ...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 554 |
| prompt-injection | 458 |
| memory-poisoning | 37 |
| tool-use-attack | 93 |
| backdoor | 393 |
| adversarial-attack | 535 |
| privacy-leakage | 3702 |
| steganography | 53 |
| misuse | 828 |
| red-teaming | 109 |
| vulnerability | 2472 |
| defense | 2132 |
| alignment | 1960 |
| robustness | 1854 |
| watermark | 204 |
| unlearning | 82 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 255 |
| other | 5552 |

---

📚 **全部 21374 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-30 12:18:25*