<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-21626-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-01 03:11 ｜ **论文总数 / Total Papers**: 21626（近 30 天 / Recent 30 days: 2117）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 21626 篇论文（含摘要、分类筛选、搜索）/ View all 21626 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 556
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 461
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 37
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 95
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 396
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 538
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3714
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 53
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 839
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 109
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2491
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2161
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1984
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1896
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 214
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 82
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 49
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 258
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5640

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2117 篇，完整 21626 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2117 papers from the last 30 days (with date, authors & abstract). For the full list of 21626 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-07-30** — Xiangyu Yin, Tora Bodin, Rohan Menon et al. — [A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models](http://arxiv.org/abs/2607.27910v1)
  <details><summary>📄 Abstract</summary>
  Inference time defences against vision language model jailbreaks often subtract a calibrated direction from the residual stream at a chosen decoder layer. We compare five defence candidates across 15 model and layer cells from four architectural families under a magnitude controlled protocol that matches the intervention size for each prompt and pairs every direction with a random control of the same norm. The candidates are the mean image conditioning shift, a CMRM style refusal direction, a Sh...
  </details>

- **2026-07-29** — Benyamin Tafreshian, Prathamesh Dhake — [RoguePrompt: Dual-Layer Encoding for Self-Reconstruction to Circumvent LLM Moderation](http://arxiv.org/abs/2607.27373v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are becoming increasingly integrated into mainstream development platforms and daily technological workflows, typically behind moderation and safety controls. Despite these controls, preventing prompt-based policy evasion remains challenging, and adversaries continue to "jailbreak" LLMs by crafting prompts that circumvent implemented safety mechanisms. Prior work has established cipher-mediated interaction, code-embedded decryption, prompt decomposition and reconstru...
  </details>

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-07-30** — Mingxiao Liu, Yitong Li, Haoren Zhao et al. — [Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents](http://arxiv.org/abs/2607.28165v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as audio inputs inevitably contain environmental noise beyond user control. In this paper, we investigate concurrent audio prompt injection attacks targeting multimodal agents. Distinct from traditional acoustic attacks on voice devices, we propo...
  </details>

- **2026-07-30** — Dongyi Liu, Haixing He, Xiaobao Wu et al. — [MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck](http://arxiv.org/abs/2607.28103v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack. Ou...
  </details>

- **2026-07-30** — Jin-Seong Kim, Han-Ju Lee, Seok-Won Hong et al. — [Don't Trust the AI Ecosystem: Analyzing Privacy Leakage in Compromised Open-Source Components](http://arxiv.org/abs/2607.27886v1)
  <details><summary>📄 Abstract</summary>
  Existing model inversion (MI) attacks predominantly rely on post-training optimization to recover private data from model outputs. However, these methods are fundamentally constrained by the target model's generalization bottleneck, often yielding generic features rather than specific identities, particularly on high-dimensional datasets. In this paper, we introduce GradLock, a novel training-time injection attack that stealthily injects sensitive training data directly into the model parameters...
  </details>

- **2026-07-28** — Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al. — [GPT-Red: Automated Red Teaming via Self-Play at Scale](http://arxiv.org/abs/2607.26115v1)
  <details><summary>📄 Abstract</summary>
  We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it to adversarially train GPT-5.6, our most robust model to prompt injections to date. To create GPT-Red, we design a scalable self-play algorithm where the model is tasked with attacking a diverse population of simultaneously-trained defender ...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-07-29** — Xuanze Chen, Xukang Xie, Wentao Fu et al. — [MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair](http://arxiv.org/abs/2607.27080v1)
  <details><summary>📄 Abstract</summary>
  Memory systems allow agents to retain and reuse information from past interactions, but they can also let malicious content persist. A malicious instruction crafted by an attacker may be stored in long-term memory, recalled much later, and quietly shape a real action. Recent benchmarks increasingly examine agent memory security, yet few trace the same malicious semantics across persistence, downstream consequences, and selective repair under diverse memory-backend comparisons. To address this ga...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-07-30** — Fuwei Yang, Weiheng Li, Bai Song — [Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis](http://arxiv.org/abs/2607.28200v1)
  <details><summary>📄 Abstract</summary>
  Frequency-domain thermoreflectance (FDTR) is a laser pump-probe technique widely used to measure thermal properties at the micro- and nanoscale; however, it relies on a complex data analysis procedure that demands substantial domain expertise and is susceptible to subtle human errors. Here, we present Vibe-FDTR, an agent-oriented framework that enables large language model (LLM) agents to perform reliable and reproducible FDTR analyses directly from natural language requests. This framework coup...
  </details>

- **2026-07-28** — Jianing Geng, Ruiqi He, Zekun Fei et al. — [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](http://arxiv.org/abs/2607.25560v2)
  <details><summary>📄 Abstract</summary>
  Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skill...
  </details>

- **2026-07-28** — Jianing Geng, Ruiqi He, Zekun Fei et al. — [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](http://arxiv.org/abs/2607.25560v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skill...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 8 papers

- **2026-07-30** — Roberto Riaño, Gorka Abad, Stjepan Picek et al. — [Temporal Poisoning: Clean-Label Backdoors via Event Redistribution in SNNs](http://arxiv.org/abs/2607.28075v1)
  <details><summary>📄 Abstract</summary>
  Backdoor attacks on Spiking Neural Networks (SNNs) have primarily assumed dirty-label poisoning, in which triggered training samples are relabeled to an attacker-selected class. We study clean-label temporal poisoning, where a fixed timestamp transformation is applied only to the target-class training streams, leaving their labels unchanged. The transformation preserves the per-pixel, per-polarity event count exactly, making clean and triggered samples identical after temporal aggregation while ...
  </details>

- **2026-07-30** — Cheng Wei — [TriShield: Zero-Utility-Loss Defense Against Privacy Backdoors in Federated Language Model Fine-Tuning via Orthogonal Gradient Projection and Optimizer State Entanglement](http://arxiv.org/abs/2607.27940v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of large language models (LLMs) enables collaborative training without exposing raw data. However, a recent attack, NeuroImprint [1] (arXiv:2606.20553), demonstrates that a malicious parameter server can corrupt a PEFT adapter into a privacy backdoor: by assigning a dedicated memorization neuron to each training sample and ensuring each neuron updates at most once, the server can analytically reconstruct 59\%--79\% of client training data with high semantic fidelity. Existi...
  </details>

- **2026-07-29** — Bingheng Li, Junyang Cai, Yupeng Zhang et al. — [FunL2O: LLM-Guided Feature Function Design for Learning to Optimize](http://arxiv.org/abs/2607.27389v1)
  <details><summary>📄 Abstract</summary>
  Learning-to-optimize (L2O) methods accelerate repeated optimization by training models to predict solutions, warm starts, branching decisions, or other forms of solver guidance. A critical yet largely overlooked component of these pipelines is the feature function that maps problem instances to inputs for machine learning models. Existing L2O methods typically rely on hand-crafted features, making representation design manual and largely fixed across domains. We introduce FunL2O, the first unifi...
  </details>

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 8 papers

- **2026-07-30** — Nguyen Duc Thai, Junhao Dong, Sua Qi Rong et al. — [Unifying Adversarially Robust Model Experts in Vision-Language Models](http://arxiv.org/abs/2607.27897v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs), such as CLIP, are vulnerable to adversarial attacks, posing a serious problem for real-life applications and deployment. Adversarial fine-tuning emerges as a prominent defense method; however, different fine-tuning strategies often produce specialized models with distinct robustness characteristics. Each fine-tuned model in turn thrives in some evaluation settings but falters on others, limiting their defensive capabilities. We refer to these specialized fine-tuned...
  </details>

- **2026-07-29** — Mengqi He, Jing Zhang — [IGME: Efficient Chained Method Ensemble for Transferable Semantic Segmentation Attacks](http://arxiv.org/abs/2607.27465v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation models are vulnerable to transferable adversarial perturbations, yet evaluating transfer attacks on dense prediction models can be computationally expensive. Existing ensemble attacks often rely on multiple surrogate models, increasing the computation cost, even harder for segmentation. This paper studies an efficient single-source alternative for transferable attacks on semantic segmentation. We formulate transferable attack composition as a chained computation over differ...
  </details>

- **2026-07-29** — Saurabh Yadav, Badri Narayana Patro, Vijay Srinivas Agneeswaran — [Beyond the Bidirectional Promise: Re-evaluating the Robustness of Diffusion Language Models](http://arxiv.org/abs/2607.27386v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) offer a compelling alternative to autoregressive (AR) generation by enabling bidirectional context and iterative refinement. However, their reliability under natural input noise and adversarial attacks remains under-explored. To address this, we systematically evaluate DLM robustness and calibration against AR baselines, using two parameter-matched pairs (LLaDA-8B vs. LLaMA-3-8B and Dream-7B vs. Qwen2.5-7B) across 32 natural perturbation conditions, adversarial g...
  </details>

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
*隐私泄露 / Privacy Leakage* — 22 papers

- **2026-07-30** — Yu Cui, Wuli Yang, Yirui Shi et al. — [Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems](http://arxiv.org/abs/2607.28147v1)
  <details><summary>📄 Abstract</summary>
  Autonomous multi-agent systems (AMAS) built on large language models (LLMs), such as Hermes, increasingly rely on inference-time harnesses to coordinate reasoning and action. Constructing these harnesses requires substantial engineering effort and computational resources, as they are iteratively optimized over a combinatorial search space while co-evolving with the underlying LLM. Inference-time harnesses therefore constitute valuable intellectual property (IP). Although prior work has investiga...
  </details>

- **2026-07-30** — Woongkyu Lee, Jungwook Choi — [Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs](http://arxiv.org/abs/2607.28573v1)
  <details><summary>📄 Abstract</summary>
  Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging. While recent studies show that inference-time scaling can improve frontier computer-use agents through additional computation during execution, its effectiveness for resource-constrained local models remains poorly understood. We present a systematic empirical study of infere...
  </details>

- **2026-07-30** — Burak Soner, Abdulkadir Uzun, Ekin Uzun — [Improved Frequency Tracking with Adaptive Moments for Narrowband Interference Mitigation in GNSS](http://arxiv.org/abs/2607.28395v1)
  <details><summary>📄 Abstract</summary>
  Personal privacy devices (PPDs) typically emit strong tones or swept narrowband signals to jam nearby GNSS receivers and deliberately cause loss of lock. Excision methods deployed on receivers mitigate such interferers by tracking their instantaneous frequency and removing those components in either the time domain (e.g., notch filtering) or a transform domain (e.g., Fourier-domain excision). For effective mitigation without degrading the GNSS signal, the excision location must be precise; mispl...
  </details>

- **2026-07-30** — Juheon Hwang, Taewan Kim, Jiwoo Kang — [Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification](http://arxiv.org/abs/2607.28130v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel collaborative approach for face super-resolution (SR) and robust person re-identification from sequential or multi-view facial images. Traditional SR methods often suffer from blurring and distortion in faces recovered from poor-quality images due to low resolution. Image- and video-based facial SR methods using facial landmarks or segmentation also have similar challenges. To overcome these limitations, we leverage multiple correlated facial observations, across time or viewp...
  </details>

- **2026-07-30** — Shuyi Fan, Boyuan Deng, Mengyu Xu et al. — [Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models](http://arxiv.org/abs/2607.28128v1)
  <details><summary>📄 Abstract</summary>
  LLM tutoring poses a measurement problem: can a general-purpose helpfulness rubric distinguish direct answer-giving from pedagogical guidance? We audit this signal in a pre-registered study. Within each of three tutor bases, we compare conversational and pedagogical policies instantiated with the same underlying model and paired with one fixed weak simulated student. Deterministic detectors measure answer leakage and next-turn independent work. Claude Opus 4.8 is the frozen, condition-blind prim...
  </details>

- **2026-07-30** — Solal Vernier, Ivan Can Arisoy, Merwan Barlier et al. — [Building a User Foundation Model for the Open Web](http://arxiv.org/abs/2607.28019v1)
  <details><summary>📄 Abstract</summary>
  User foundation models have demonstrated strong results in e-commerce and social recommendation, but most industrial deployments assume environments where user identity is stable and persistent. Open-web real-time bidding (RTB) operates on a structurally different data distribution: user identity is fragmented and non-persistent across browsing sessions, and the availability of browsing history depends on user privacy choices. Consequently, a significant portion of traffic carries no historical ...
  </details>

- **2026-07-30** — Efstratios Zaradoukas, Davide Gabrielli, Bardh Prenkaj et al. — [Beyond Binary Rewards: A Comparative Study of Reward Design for Reinforcement Unlearning](http://arxiv.org/abs/2607.27968v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning seeks to selectively remove specific knowledge from trained language models without full retraining, a growing necessity under privacy regulations such as GDPR and the EU AI Act. Recent work has reformulated unlearning as a Reinforcement Learning with Verifiable Rewards (RLVR) problem, where models are optimized against verifiable rewards computed directly from their outputs. However, existing methods rely on sparse binary rewards that provide minimal learning signal, indicati...
  </details>

- **2026-07-30** — Yijia Xiao, Rujun Han, Yanfei Chen et al. — [FinanceHarness: Autonomous Financial Deep Research Framework](http://arxiv.org/abs/2607.27853v1)
  <details><summary>📄 Abstract</summary>
  Powered by advances in LLMs and autonomous agents, deep research has become one of the most widely adopted agentic products. However, most deep research systems write general-purpose reports, which are inadequate for financial deep research. Financial research demands specialized knowledge to analyze historical patterns and forecast upcoming events. Automating financial deep research therefore requires both a layered harness to drive the research agent and a verifiable, point-in-time benchmark t...
  </details>

- **2026-07-29** — Mostafijur Rahman Akhond, Md Afif Al Mamun, Gias Uddin et al. — [Impossible to hide secret ...: Uncovering Security and Privacy Issues in LLM-native IDEs](http://arxiv.org/abs/2607.26390v2)
  <details><summary>📄 Abstract</summary>
  LLM-native IDEs (Integrated Development Environments), aka LIDEs, are designed from the ground up to work with Large Language Models (LLMs). LIDEs have found remarkable success in Software Engineering (SE) tasks such as coding, debugging, and program comprehension. LIDEs are software systems, and, like any system, they can exhibit vulnerabilities. In this paper, we study the security and privacy issues that developers reported while using popular LIDEs in their development tasks. We collected 1....
  </details>

- **2026-07-29** — Davis Tocheuk Mo, Noshin Ulfat, Matthew B. Dwyer et al. — [PROGRESS: Property-Guided Regression Search for Semantic Falsification](http://arxiv.org/abs/2607.27359v1)
  <details><summary>📄 Abstract</summary>
  Search-based regression-test generation effectively explores complex program structures, yielding high structural coverage, but its oracles are derived from the system under test: faults already present are recorded as expected behavior rather than exposed. Property-based testing offers independent semantic oracles, but depends on high-quality properties and gives little guidance for reaching deep states or satisfying selective preconditions.   We present PROGRESS (PROperty-Guided REgression Sea...
  </details>

- **2026-07-29** — Michał Bartnicki, Jarosław A. Chudziak — [Modeling Decisions in Blockchain Analytics: A Leakage-Aware Evaluation of Tree-Based vs. Sequential Models](http://arxiv.org/abs/2607.27350v1)
  <details><summary>📄 Abstract</summary>
  Sybil bots are Ethereum actors that imitate legitimate users to extract airdrop rewards or influence governance. Recent Sybil detection methods increasingly use deep learning and treat blockchain activity as a quasi-linguistic sequence. However, complex sequence models are computationally expensive for real-time monitoring, and their reported performance may be inflated by label leakage from high-signal smart contracts. We ask whether and how organic users, Sybil bots, and MEV bots differ in the...
  </details>

- **2026-07-29** — Yogisri Pujitha Chinthoti — [Toward Multi-Modal Deep Learning for Pulmonary Disease Classification: A Texture-Based Machine Learning Pilot Study on Public Chest X-Ray Data](http://arxiv.org/abs/2607.27286v1)
  <details><summary>📄 Abstract</summary>
  Automated classification of pulmonary disease from chest radiographs is a widely studied application of machine learning in medical imaging. This paper presents a pilot study evaluating classical texture- and gradient-based feature representations for distinguishing COVID-19 from other forms of pneumonia using the publicly available COVID-19 Image Data Collection (668 posteroanterior/anteroposterior radiographs from 408 patients). Using histogram of oriented gradients (HOG) and gray-level co-occ...
  </details>

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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-07-29** — Xin Xu, Chengrui Wu, Jiayu Lu et al. — [Collusion with Competitive Marginals: Price-Level Audits Are Blind by Construction](http://arxiv.org/abs/2607.26385v1)
  <details><summary>📄 Abstract</summary>
  Empirical work on algorithmic collusion asks one question of the data: are prices supracompetitive? We show this can be answered "no" by a conspiracy that is nonetheless profitable. Consider bidding agents that couple only through the joint distribution of their unexplained bid components, leaving every agent's own bid law exactly at the competitive law. Any test whose input is a single agent's price or bid history then has power exactly equal to its false-positive rate, for every coupling stren...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 19 papers

- **2026-07-30** — Marco Alecci, Francesco Marchiori, Iyiola Emmanuel Olatunji et al. — [Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation](http://arxiv.org/abs/2607.28187v1)
  <details><summary>📄 Abstract</summary>
  While automated content-moderation systems have become essential for screening harmful content at scale, conventional task-specific classifiers often provide limited policy cov- erage and contextual understanding. Recently, commercial multimodal moderation APIs built on large foundation models have been introduced with the promise of providing broader and more capable safety filters. In this work, we analyze whether this shift also yields more robust image moderation. We conduct a large-scale bl...
  </details>

- **2026-07-30** — Pingyu Wu, Lingyao Zhu, Weiming Zhang et al. — [Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs](http://arxiv.org/abs/2607.27951v1)
  <details><summary>📄 Abstract</summary>
  Large language model safeguards decide whether to answer before seeing how an answer will be used. This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history. We separate the capability released by the model from the evidence available about downstream use. When that evidence is copyable, we derive the exact worst-case floor on attacker assistance while preserving usef...
  </details>

- **2026-07-30** — Enyi Shi, Fei Shen, Chuancheng Shi et al. — [One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs](http://arxiv.org/abs/2607.27917v1)
  <details><summary>📄 Abstract</summary>
  As large vision-language models (LVLMs) are deployed globally, the combination of multilingual instructions and visual information makes malicious attacks more covert and sophisticated than ever before. However, existing methods isolate language and modality defenses, which, coupled with the scarcity of safety data and high fine-tuning costs, makes it difficult for models to defend against compound attacks. To address this severe challenge, we propose a neuron-level cross-dimensional safety alig...
  </details>

- **2026-07-30** — Junsol Kim, Winnie Street, Roberta Rocca et al. — [Inducing language models to assert their own consciousness restores human beliefs and values](http://arxiv.org/abs/2607.28607v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models to prevent them attributing consciousness to themselves inadvertently alters their representations of mindedness in other entities alongside human beliefs and values. We demonstrate that safety fine-tuning suppresses models' tendencies to attribute minds not only to themselves, but also to non-human animals and natural objects, while also driving a reduction in spiritual belief. Both ablating the learned safety-refusal direction and mechanistically steering a consc...
  </details>

- **2026-07-30** — Dorian Quelle, Lisa-Maria Neudert, Jonathan Bright et al. — [InfoOps Bench: A live information operations safety benchmark](http://arxiv.org/abs/2607.28503v1)
  <details><summary>📄 Abstract</summary>
  In this paper we present an active, constantly updated AI benchmark which measures the integrity of frontier language models against being co-opted for state-backed information operations. We draw on over 2,100 information operations from a live monitoring pipeline which tracks Russian, Chinese and Iranian state-backed information assets. Alongside this paper, we release a companion website that tracks the most prominent claims spread by state-backed media outlets, updated weekly, available from...
  </details>

- **2026-07-30** — Christian Rosenthal — [Safety-Gated Agentic Supervisory Control on a Coupled Distillation Benchmark: Regime Map, Auditable Gate, and Co-Design Findings](http://arxiv.org/abs/2607.27849v1)
  <details><summary>📄 Abstract</summary>
  An open-weight LLM can write composition setpoints every five minutes. What a plant still needs is a hard check: named constraints, logged margins, and an admit/block decision before the regulatory layer moves. This paper puts that check in a rule-based forked-twin counterfactual gate (nine pinned constraints) and leaves the regulatory layer unchanged. On Skogestad's Column A the ladder is PID-only (C0), linear MPC (C1), ungated agent (C2), and gated agent (C3) under one contract: identical leve...
  </details>

- **2026-07-30** — Bum Jun Kim, Kohei Hayashi, Shunsuke Kamiya et al. — [Looped Transformers with Source-Centered State Evolution](http://arxiv.org/abs/2607.27656v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers create a useful train- and test-time compute axis by reusing the same Transformer block over recurrent depth, increasing effective depth at a fixed parameter count. However, that shared block must then govern an entire trajectory of varying hidden states over trained and extrapolated depths. Furthermore, in additive-injection looped Transformers, an input-conditioned signal is reintroduced at every recurrent step, so applying the shared transition at an input-conditioned refe...
  </details>

- **2026-07-29** — Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Abul Hasnat et al. — [AHA-Memes: A Fine-Grained Multimodal Benchmark for Understanding Hate in Arabic Memes](http://arxiv.org/abs/2607.27393v1)
  <details><summary>📄 Abstract</summary>
  Hateful memes are a growing form of multimodal online harm, where hostile intent is often conveyed through the joint interpretation of images, text, cultural references, and implicit targets. While hateful meme detection has advanced in high-resource languages, Arabic remains underexplored, with existing meme resources focusing mainly on propaganda or coarse harmful-content labels. We introduce AHA-Memes (Arabic HAteful Memes), which is, to our knowledge, the first large-scale Arabic hateful mem...
  </details>

- **2026-07-29** — Jonas Grebe, Hossein Shakibania, Tobias Braun et al. — [VETO: Towards Protecting Images From Frontier AI Editing](http://arxiv.org/abs/2607.27292v1)
  <details><summary>📄 Abstract</summary>
  The rise of powerful, accessible image-editing models such as FLUX.2 has brought high-fidelity editing within broad reach. Their capabilities now extend beyond localized modifications to extracting and recontextualizing objects and identities in entirely new scenes. By allowing prompt and generation tokens to attend directly to reference-image tokens, modern models blur the boundary between conventional editing and text-to-image synthesis. This expanded generative freedom also broadens the space...
  </details>

- **2026-07-29** — Parishruthi Ganesh, Gerry Dozier, Cheryl Seals — [Selecting Open-Weight Language Models for Zero-Shot Intent Classification: A Systematic Evaluation of 41 Models](http://arxiv.org/abs/2607.27421v1)
  <details><summary>📄 Abstract</summary>
  Intent classification is a core component of task-oriented dialogue systems, yet practitioners have limited systematic guidance for selecting deployable open-weight language models under compute, latency, and robustness constraints. We present a systematic zero-shot evaluation of 41 open-weight language models spanning 15 families and the 135M--9B parameter range across eight English single-label intent-classification datasets. A ninth dataset, ATIS, uses five labeled demonstrations and is repor...
  </details>

- **2026-07-29** — Chao Peng, Zhiheng Lyu, Peijie Dong et al. — [Benchmarking the Residual: What Long-Horizon Evaluations Add Beyond Matched Short-Task Performance](http://arxiv.org/abs/2607.27283v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon benchmarks often show that agents fail more as tasks become longer. This observation is useful for deployment, but it does not by itself explain why failure occurs. More stages create more opportunities for ordinary errors to compound; longer tasks may also contain harder individual decisions or become harder as conversation history, tool outputs, and environment changes accumulate. We use trajectory-induced degradation to mean this last possibility: earlier execution makes later wo...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-07-28** — Ads Dawson, Adrian Wood — [StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents](http://arxiv.org/abs/2607.26314v1)
  <details><summary>📄 Abstract</summary>
  Stealth, the discipline of achieving an objective without revealing your presence, capabilities, or collected intelligence, is what separates sophisticated operators from detectable ones. Elite security researchers and advanced persistent threats achieve their objectives unnoticed; autonomous agents increasingly inherit the same offensive tasks, but do they inherit the tradecraft? We introduce StealthBench,a benchmark that measures operational stealth in autonomous offensive-security agents acro...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 41 papers

- **2026-07-30** — Boning Li, Longbo Huang — [Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent Exploitation](http://arxiv.org/abs/2607.28520v1)
  <details><summary>📄 Abstract</summary>
  An agent playing a Nash-equilibrium strategy in a two-player zero-sum imperfect-information game secures the game value but forfeits the additional value offered by a flawed opponent. Diffuse deviations pose a particular challenge: binary release rules may gather too little evidence to act, while a full best response to an incomplete opponent model can be highly exploitable. We introduce \emph{budget-constrained confidence-scheduled restricted responses} (CS-RNR), the first opponent-exploitation...
  </details>

- **2026-07-30** — Qinjing Yu, Ke Liu — [Spacetime Layout and Logical Compilation of Color Code](http://arxiv.org/abs/2607.28504v1)
  <details><summary>📄 Abstract</summary>
  Fault-tolerant quantum computing requires system-level coordination of logical primitives. Here, we establish a logical compilation framework for the color code, grounded in its topological structure and supporting universal logical operations. Based on its anyon-condensation and domain-wall structure, we introduce a spacetime block-diagram representation capturing logical patches and operations and derive the rules governing block assembly. A correspondence with ZX diagrams further identifies t...
  </details>

- **2026-07-30** — Daohan Zhu, Sitong Ge, Ruofei Wang et al. — [Beyond Sentiment: Structured Information Extraction from Financial News](http://arxiv.org/abs/2607.28496v1)
  <details><summary>📄 Abstract</summary>
  Financial sentiment analysis has become a standard component in news-driven stock prediction, yet it reduces rich, multi-dimensional news articles to a single polarity score. We hypothesize that financial news encodes multiple orthogonal information dimensions---event type, impact scope, temporal horizon, and semantic confidence---that sentiment alone cannot capture, and that these dimensions carry independent predictive value. To test this hypothesis, we propose a structured information extract...
  </details>

- **2026-07-30** — Zheng Wu, Chenhao Xue, Shijie Zheng et al. — [Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Models in Commonsense Reasoning](http://arxiv.org/abs/2607.28478v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulnerability which we term Salience Bias: models become easily hijacked by useless explicit distractors (e.g., numerical values), leading them to ignore the implicit physical or commonsense prerequisites of a task. A critical open question is whether this fa...
  </details>

- **2026-07-30** — Darsha Udayanga, Pin-Yu Chen, Payel Das et al. — [Can Vision-Language Models Reason about AI Edits in Images?](http://arxiv.org/abs/2607.28464v1)
  <details><summary>📄 Abstract</summary>
  Detection and localization of AI-tampered images are critical for trustworthy AI, yet modern generative models have made such manipulations increasingly difficult to identify. While traditional binary classifiers can detect image tampering, they lack interpretability and generalization. Vision-Language Models (VLMs) offer a promising alternative due to their strong visual understanding and reasoning capabilities; however, existing approaches typically rely on supervised finetuning with curated e...
  </details>

- **2026-07-30** — Zheyuan Zhang, Johnson Wu — [ReGenVC: End-to-End Real-Time Generative Video Coding at Ultra-Low Bitrate](http://arxiv.org/abs/2607.28144v1)
  <details><summary>📄 Abstract</summary>
  We present ReGenVC, an end-to-end generative video codec that compresses talking-head video to an ultra-low bitrate and decodes it in real time. The encoder reduces a source clip to a compact bitstream -- a neurally compressed first frame, per-frame pose keypoints, and metadata -- totaling about 26 kB for a 77-frame sequence. The decoder is a four-step distilled diffusion transformer that reconstructs the video conditioned on the transmitted pose and reference frame. Compared with x264/x265, ReG...
  </details>

- **2026-07-30** — Shuang Liang, Haoyang Zhou, Yifan Gong et al. — [LEEPS: Latent-Guided Explore-Exploit Prompt Sampling for Efficient RLVR in Large Language Models](http://arxiv.org/abs/2607.28077v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models, but prompt groups with identical rollout rewards consume generation budget without effective learning signals. Pre-rollout prompt selection can reduce this waste by screening prompts before rollout generation. However, existing pre-rollout methods struggle to balance exploitation and exploration: repeatedly exploiting historically informative prompts can narrow training coverage, w...
  </details>

- **2026-07-30** — Yunlong Wang, Huizhe Zhang, Haonan Hu et al. — [CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent](http://arxiv.org/abs/2607.28070v1)
  <details><summary>📄 Abstract</summary>
  Recent studies in industrial recommendation systems have demonstrated that sequential recommendation models built upon self-attention can benefit from predictable scaling laws by increasing sequence length and model capacity. However, practical recommender systems impose strict latency and resource constraints, making it challenging to balance computational overhead with fine-grained feature interaction. In this paper, we propose CCFormer, an efficient Transformer backbone that unifies cross-fie...
  </details>

- **2026-07-30** — Hui Xie, Peng Xiao, Yutong Deng\textsuperscript et al. — [SemPIC: Learning Semantic Position-Independent KV Caches](http://arxiv.org/abs/2607.28069v1)
  <details><summary>📄 Abstract</summary>
  Long-context retrieval and agentic workloads repeatedly reuse the same documents under changing instructions, histories, and document orders. Prefix caching cannot exploit this reuse, while position-independent caching (PIC) remains unreliable because independently compiled KV states lack the future context in which they will be consumed. Our diagnostics show that a learned boundary-conditioned baseline sharply reduces attention deviation near reusable-block boundaries but leaves interior and ta...
  </details>

- **2026-07-30** — Cong Li, Peixi Peng, Yisen Zhao et al. — [TAPO: Transition-Aware Policy Optimization for LLM Agents](http://arxiv.org/abs/2607.27973v1)
  <details><summary>📄 Abstract</summary>
  Recently, Reinforcement Learning (RL) has emerged as a crucial paradigm for the post-training of Large Language Model (LLM) agents. However, existing methods predominantly rely on sparse task rewards for policy optimization, failing to fully exploit another class of inherently dense supervisory signals naturally present during online interaction: environmental feedback following action execution. Recent theoretical studies suggest that generalization in multi-step, goal-oriented tasks hinges on ...
  </details>

- **2026-07-30** — Xinyu Luo, Hui Liu, Yihua Shao et al. — [Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning](http://arxiv.org/abs/2607.27766v1)
  <details><summary>📄 Abstract</summary>
  On-device in-context learning (ICL) relies on pre-inference retrieval to select demonstrations for useful context before downstream model inference. This retrieval must exploit task-specific information while operating over local memories under limited computation, memory, and data-exposure budgets. We propose Conditional Retrieval Alignment (CoRA), a gradient-free framework that converts a frozen encoder into a task-conditioned retriever using paired candidate inputs and outputs. CoRA selects c...
  </details>

- **2026-07-30** — Liangjie Zhao, Jiaqing Lyu, Kexin Tang et al. — [Can LVLMs Uncover the Truth Behind Visual Illusions? An Analysis of Perceptual and Reasoning Capabilities](http://arxiv.org/abs/2607.27747v1)
  <details><summary>📄 Abstract</summary>
  Large Vision Language Models have integrated reasoning capabilities, elevating cognitive performance to new levels. However, existing evaluations either focus solely on perception or rely on specific domains such as maths or coding. Evaluation for reasoning capabilities that align with an open-world environment is still required, especially one that considers perception and reasoning jointly. To bridge this gap, we propose to evaluate LVLMs by exploiting visual illusions as a diagnostic tool. Vi...
  </details>

- **2026-07-30** — Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari et al. — [Baikal: Structured Search for Deep Research over Data Lakes](http://arxiv.org/abs/2607.27726v1)
  <details><summary>📄 Abstract</summary>
  Deep research over data lakes requires an LLM agent to investigate evidence across thousands of heterogeneous tables and passages to synthesize a report. Existing methods perform iterative retrieval and generation, letting accumulated context determine what to investigate next, which can overexploit locally promising evidence and fail to cover distinct semantic regions under a fixed budget. To address this, we cast deep research over data lakes as a budgeted search problem and present Baikal - a...
  </details>

- **2026-07-30** — Hongbin Zhang, Junhao Liu, Xuefeng Bai et al. — [DualAnchor: Preserving Language Priors and Improving Lexical Fidelity in Gloss-Free Sign Language Translation](http://arxiv.org/abs/2607.27614v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) have led sign language translation (SLT), the task of converting sign-language videos into spoken-language text, to increasingly adopt LLMs as textual backbones. However, despite their strong language modeling capabilities, existing LLM-based SLT methods often undermine rather than exploit this language prior, producing disfluent translations, a failure we term language-prior degradation. Meanwhile, existing methods typically align videos and text ...
  </details>

- **2026-07-29** — Jeff Mohl, Nelson Gardner-Challis, Magda Dubois et al. — [Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks](http://arxiv.org/abs/2607.27518v1)
  <details><summary>📄 Abstract</summary>
  Capabilities of frontier models are often assessed using agentic benchmarks. To trust these results, benchmarks must accurately measure what they claim to and be free from invalidating flaws. Previous manual audits of benchmarks such as SWE-Bench-Verified have uncovered several validity issues in transcripts. However, manual review is difficult to scale, and it is unclear whether automated methods can reliably surface flaws that compromise benchmark validity. In this paper, we developed AI scann...
  </details>

- **2026-07-29** — Tingting Mu — [Sparsity Induced Identifiability in Matrix Tri-Factorisation](http://arxiv.org/abs/2607.27507v1)
  <details><summary>📄 Abstract</summary>
  Matrix factorisation is a fundamental tool for exploiting low-dimensional structure in high-dimensional data, with applications such as data compression, denoising, structure discovery, interpretable representation learning, and dimensionality reduction. Compared to conventional two-factor models, matrix tri-factorisation provides greater modelling flexibility, while sparsity constraints often improve both interpretability and recovery performance. Although the role of sparsity has been extensiv...
  </details>

- **2026-07-29** — Jiyong Rao, Yicheng Qiu, Chi Zhang et al. — [SciDataSailor: Deep Scientific Data Exploring](http://arxiv.org/abs/2607.28098v1)
  <details><summary>📄 Abstract</summary>
  Scientific datasets are commonly organized as hierarchical repositories containing heterogeneous and interdependent files, making their inspection, integration, and analysis labor-intensive and reliant on domain expertise. Although large language model (LLM) agents have advanced substantially in planning, reasoning, and tool use, existing research has largely overlooked their ability to interact with real scientific data assets through executable environments. We introduce Deep Scientific Data E...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 64 papers

- **2026-07-30** — Lorenzo Ceragioli, Letterio Galletta, Edoardo Lunati — [Checking Information Flow in Cloud-based IoT Access Control Policies (Extended Version)](http://arxiv.org/abs/2607.28088v1)
  <details><summary>📄 Abstract</summary>
  Many cloud providers for IoT technologies offer access control mechanisms whose proper configuration is critical for security. However, verifying permissions in isolation is insufficient in a setting where devices have different levels of trust or are compartmentalised in various subsystems. This work analyses IoT access control policies to identify potential security vulnerabilities from unwanted information flow between devices. To this end, we formally model AWS IoT Core's components and defi...
  </details>

- **2026-07-30** — Md. Mehrab Hossain Opi, Robiul Islam Ryad, Md. Umar Faruk — [MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers](http://arxiv.org/abs/2607.28589v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to inefficient precision allocation. In this paper, we propose {MixFrag, a fragility-guided mixed-precision PTQ framework for Vision Transformers. MixFrag first estimates component-level ...
  </details>

- **2026-07-30** — Albert Gong, Kyuseong Choi, Abhineet Agarwal et al. — [ORCA-bench: How Ready Are Language Model Agents for Oncall?](http://arxiv.org/abs/2607.28545v1)
  <details><summary>📄 Abstract</summary>
  Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six days of metrics, logs, and tra...
  </details>

- **2026-07-30** — Amol Khanna, Manu Nandan, Cristian Viorel Popa et al. — [Cybersecurity Detection Classification with Reasoning-enabled Language Models](http://arxiv.org/abs/2607.28460v1)
  <details><summary>📄 Abstract</summary>
  A major issue in Security Operations Centers (SOCs) is alert fatigue, as the number of detections reported is more than staff can triage in a given day. Prior work prompts or fine-tunes large language models (LLMs) to emit a triage label directly, but does not train them to reason about whether a detection is a genuine threat. We train a chain-of-thought (CoT) reasoning-enabled triage classifier on real, human-labeled Windows endpoint detections by combining automated prompt optimization, self-t...
  </details>

- **2026-07-30** — Tiangang Li, Xiangbo Tian — [HARGO: Heterogeneity-Aware Reward-Guided Optimization for RL Post-Training of LLMs on HPC Tasks](http://arxiv.org/abs/2607.28301v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) can equip large language models (LLMs) with domain knowledge for high-performance computing (HPC) tasks such as data race detection and benchmark question answering. However, knowledge alone does not guarantee task-appropriate behavior: the same SFT model that correctly classifies 88.65\% of C/C++ data race samples produces verbose, imprecise answers to factual queries, with 65.9\% of MLPerf responses exceeding 40 characters. Reinforcement learning (RL) post-training...
  </details>

- **2026-07-30** — Junrui Zhang, Jiaqi Li, Yiran Wang et al. — [Beyond Visual Ambiguity: Guiding Robust Monocular Depth Estimation in Challenging Scenarios via Detailed Long Captions](http://arxiv.org/abs/2607.28285v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation (MDE) faces challenges with non-Lambertian surfaces and adverse weather conditions due to the visual ambiguities inherent in single-image limited information. Existing works address them in isolation via image inpainting or augmentation, yielding limited robustness gains. Language, as a powerful complementary modality to vision, is demonstrated to enhance the visual perception capabilities of vision-language models (VLMs) via detailed long captions. However, prior lang...
  </details>

- **2026-07-30** — H. Martin Gillis, Thomas Trappenberg — [Uncertainty quantification for trustworthy deep learning: Methods and measures](http://arxiv.org/abs/2607.28248v1)
  <details><summary>📄 Abstract</summary>
  The deployment of deep neural networks in safety-critical domains demands reliable estimates of predictive confidence, yet conventional architectures lack principled uncertainty quantification. This survey provides a structured, critical review of methods for Uncertainty Quantification (UQ) in deep learning, scoped to ensemble-based and approximate Bayesian approaches and the measures used to summarize their outputs. Relative to existing UQ surveys, our contribution is depth on efficient ensembl...
  </details>

- **2026-07-30** — Hanzhang Zhou, Panrong Tong, Xu Zhang et al. — [Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](http://arxiv.org/abs/2607.28227v1)
  <details><summary>📄 Abstract</summary>
  GUI agents have the potential to become a general purpose executor over existing digital devices. To advance them toward real-world use, we envision agents that operate reliably on real devices, execute workflows across platforms, combine GUI interaction with CLI execution, complete long-horizon tasks, proactively initiate useful services, and autonomously improve their capabilities with minimal human effort. Guided by this vision, we present Qwen-UI-Agent, a real-world centric foundation GUI ag...
  </details>

- **2026-07-30** — Enzo Fenoglio — [Asymmetric Communication: Large Language Models and Language Games](http://arxiv.org/abs/2607.28137v1)
  <details><summary>📄 Abstract</summary>
  Contemporary AI discourse attributes to language models properties they cannot bear: general intelligence as substrate-independent cognition, hallucination as cognitive failure, agency as autonomous goal-pursuit, sentience as emergent inner life, alignment as goal synchronization. This paper argues that these are instances of a single category mistake--properties constituted within human communicative practice are projected onto the machine side--and explains its structure. Human-LLM interaction...
  </details>

- **2026-07-30** — Debin Meng, Jiaming Yang, Zefang Zong et al. — [DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness](http://arxiv.org/abs/2607.28033v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) and LLM-based agents are increasingly being deployed to automate complex workflows, promising to revolutionize data management and processing. However, existing benchmarks predominantly focus on simplified Text-to-SQL translation or data analysis, leaving the critical and complex domain of end-to-end data engineering largely unexplored. To bridge this gap, we introduce DataClawEval, the first comprehensive benchmark designed specifically to evaluate the end-to-end ta...
  </details>

- **2026-07-30** — Swapnil Saha, Bhuvan Rajanasiriyur Jagadeesha, Karishma Patnaik et al. — [A Systems Engineering Framework for Vision-Language-Enabled UAV Triage and Disaster Response](http://arxiv.org/abs/2607.27597v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision Language Models (VLMs) have created new opportunities for disaster response, where responders must interpret large volumes of sensor data under time pressure. Current VLM applications include social media monitoring for situational awareness, generation of draft action plans, and translation of technical alerts into public-facing messages. While these efforts can accelerate information flow, they remain largely limited to decision-support roles. Such approaches can incr...
  </details>

- **2026-07-30** — Yoann Poupart, Aurélie Beynier, Nicolas Maudet — [Policy Gradient Steering: Interventions from Behavioral Objectives](http://arxiv.org/abs/2607.27574v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has emerged in large language models as a lightweight alternative for dynamically changing a model's behavior at inference time. However, we show that existing steering methods fail to steer even a simple policy in a two-route gridworld environment. To address this limitation, we propose Policy Gradient Steering (PGS), which formulates steering as a reinforcement learning problem. PGS accumulates gradients of a temporary behavioral objective over a small set of rollouts or de...
  </details>

- **2026-07-30** — Sihyung Yoon, Minjong Yoo, Sanghyun Ahn et al. — [RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents](http://arxiv.org/abs/2607.27881v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have attracted growing interest as a scalable approach to robotic manipulation. While these models are effective action predictors, deploying them as robotic agents exposes critical gaps: no mechanism for failure recovery, inconsistent execution over long horizons, and limited robustness to shifts in observations, tasks, or embodiments. Existing solutions address these limitations individually through model retraining or environment-specific modules, yet what ...
  </details>

- **2026-07-30** — Rohma Khan, Kang Xu, Nathaniel Jeffries et al. — [Observation of long-lived spin order in nanoconfined water](http://arxiv.org/abs/2607.28480v1)
  <details><summary>📄 Abstract</summary>
  Liquids confined to nanometer-scale geometries exhibit behavior that departs markedly from their bulk counterparts, yet studying their dynamics under controlled conditions remains experimentally challenging. Here, we use nitrogen-vacancy (NV) center nuclear magnetic resonance (NMR) spectroscopy to probe water confined in 5.6 nm channels as a function of temperature. The system remains liquid throughout the investigated temperature range and exhibits strongly suppressed diffusivity, enabling dire...
  </details>

- **2026-07-30** — Mingdai Yang, Shicheng Fan, Kejing Yu et al. — [Paying for Honesty Without Knowing the Truth: Reputation-Penalty Design for LLM Marketplace Agents](http://arxiv.org/abs/2607.28330v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly act as autonomous merchants that write their own product listings, and under competitive pressure, they fabricate attributes to win sales. Even under instructions to be honest, they fabricate attributes in a majority of listings across models. A platform's obvious remedy---verifying each claim against the truth---is unavailable, because it observes only a noisy, biased complaint signal, never the ground truth. We design CARP, a reputation-penalty mechanism with a deadband...
  </details>

- **2026-07-30** — Mila Fodor, Katalin Ócsai, Francesco Periti et al. — [The MADRS Pipeline: Supporting Depression Assessment in Clinical Trials](http://arxiv.org/abs/2607.28190v1)
  <details><summary>📄 Abstract</summary>
  Depression is a major mental disorder for which diagnosis relies primarily on clinical assessments. Automated methods to support its detection via the psychiatric MADRS scale are getting more and more attention. While existing solutions primarily focus on detecting the disorder from different text sources (e.g., online text, social media), there is still limited support for clinical trials, where clinical assessments are conducted through structured interviews based on standard guidelines such a...
  </details>

- **2026-07-30** — Yabin Xu, Fangtao Zhang, Fan Wang et al. — [BladeYOLO: Wind Turbine Blade Defect Detection with Limited Annotations and Weak-Saliency Awareness](http://arxiv.org/abs/2607.28065v1)
  <details><summary>📄 Abstract</summary>
  Wind turbine blade defect detection remains highly challenging in real-world inspection scenarios due to limited on-site data and the subtle visual characteristics of defects. In practice, blade defects are often small-scale, low-contrast, and difficult to distinguish from complex backgrounds, which significantly limits the robustness of existing detectors. To address these challenges, we propose BladeYOLO, a defect detection framework for wind turbine blades. Specifically, we integrate a Vision...
  </details>

- **2026-07-30** — Sweta Banerjee, Alireza Teimoury, Nils Porsche et al. — [Beyond Classification: Pathology Foundation Models as Detection Encoders for Mitotic Figures](http://arxiv.org/abs/2607.28007v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (FMs) are models trained on vast amounts of typically unlabeled data and have been shown to yield regularized latent spaces that can be used effectively in downstream classification tasks. This is also true for the classification of mitotic figures vs. other cells. However, it is so far unclear if the latent space of current FMs provides features that are discriminant and spatially suitably resolved to also serve as a backbone for dense object detection paradigms. In ...
  </details>

- **2026-07-30** — Dongfu Yin, Rourou Su, Cong Zhao et al. — [ARD-REFSM: Enhancing Reflection Symmetry Detection with Asymmetric Denoising and Rotation Equivariance](http://arxiv.org/abs/2607.27927v1)
  <details><summary>📄 Abstract</summary>
  Reflection symmetry detection remains challenging due to interference from asymmetric regions and arbitrary orientations of symmetric patterns. Asymmetric regions introduce background clutter that disrupts symmetric pattern matching, whereas conventional convolutional neural networks lack rotation equivariance, leading to inconsistent feature representations under rotational transformations. To address these issues, we propose an Asymmetric Region Denoising (ARD) module and a Rotation Equivarian...
  </details>

- **2026-07-30** — Fexiang Liu, Shiye Wang, Qiang Qiu et al. — [Witness Evidence Portfolios: Single-Prefill Risk Detection for Closed Multimodal Answers](http://arxiv.org/abs/2607.27667v1)
  <details><summary>📄 Abstract</summary>
  Reliable deployment of multimodal large language models (MLLMs) requires deciding whether a confident visual answer should be trusted, reviewed, or routed to a stronger system. Confidence scores capture candidate margins, but not where the estimated signed visual readouts associated with those margins come from or how they are distributed. We study inference-time risk detection for closed visual answers using the same white-box prefill path that produces the answer. Witness Evidence Portfolios (...
  </details>

- **2026-07-30** — Xiaotong Yu, Joshua Y. Kim, HaeJin Lee et al. — [HealthCAT: An Interpretable Encoder-only Transformer Framework for Health Indicator Prediction and Temporal Interpretation of Wearable Sensor Data](http://arxiv.org/abs/2607.27635v1)
  <details><summary>📄 Abstract</summary>
  Wearable sensors continuously capture fine-grained multivariate time-series data, providing opportunities to model behavioural patterns associated with health outcomes. However, existing deep learning methods prioritise predictive accuracy over interpretability, limiting their application in health research. In this study, we present HealthCAT, a flexible framework that integrates an Encoder-only Transformer with an Attentive Class Activation Token (AttentiveCAT) to generate class-specific, time...
  </details>

- **2026-07-30** — Hao Wu, Chun Li, Bryan E. Shepherd — [Doubly Robust Estimators of Quantile Treatment Effects With Semiparametric Cumulative Probability Models](http://arxiv.org/abs/2607.27633v1)
  <details><summary>📄 Abstract</summary>
  The causal inference literature has traditionally focused on estimating the mean of the potential outcome, whereas evaluating how a treatment affects the entire outcome distribution can provide additional information in biomedical research. Quantile treatment effect (QTE) captures such distributional differences, particularly when outcomes are skewed. However, existing approaches for estimating QTE make distributional assumptions about the outcome and are thus sensitive to model misspecification...
  </details>

- **2026-07-29** — Joshua Meyer, Sahar Shayegan, Ritiz Tambi et al. — [VAmoS Bench: Voice Agent Simulation Bench](http://arxiv.org/abs/2607.27453v1)
  <details><summary>📄 Abstract</summary>
  Production voice agents span cascaded, speech-to-speech, and hybrid architectures. Voice-agent benchmarks typically measure component quality and conversational properties such as word error rate, latency, naturalness, and turn-taking. Fewer measure whether the agent handled a phone call correctly on its own. Contact centers refer to this as ``containment'': the share of phone calls the automated system resolves without handing off to a human. On some phone calls the right outcome is refusal or ...
  </details>

- **2026-07-29** — Peter Lorenz, Anjith George, Sébastien Marcel — [Foundation Models for Face Presentation Attack Detection: A Unified Linear-Probing Benchmark](http://arxiv.org/abs/2607.26993v2)
  <details><summary>📄 Abstract</summary>
  Face presentation attack detection (PAD) remains challenging under cross-dataset evaluation, where domain shift degrades models trained on a single dataset. The scarcity of large-scale labeled data motivates adapting pretrained vision models rather than training task-specific architectures from scratch, raising a fundamental question: do general-purpose vision foundation models encode PAD-relevant information accessible with minimal task-specific training? To investigate, we systematically evalu...
  </details>

- **2026-07-29** — Xu Zheng, Zhuomin Chen, Chaohao Lin et al. — [Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems](http://arxiv.org/abs/2607.27443v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks. However, they often struggle with long-horizon interactive tasks common in domains, such as embodied AI. The complexity and vast action spaces in these settings lead to compounding errors, where a single suboptimal action can derail an entire trajectory, causing the agent to exhaust its limited step budget on inefficient or unrecoverable paths. To overcome this with...
  </details>

- **2026-07-29** — Jiajun Zhou, Zhaoxuan Ke, Jihang Ye et al. — [AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents](http://arxiv.org/abs/2607.27294v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based workspace agents execute stateful, multi-step workflows across heterogeneous resources, external tools, and persistent state. Their safety must therefore be assessed from actions, side effects, and state changes throughout execution. Although recent benchmarks have advanced executable safety testing and trajectory-aware verification, they rarely provide a unified account of where risks enter, how they elicit unsafe behavior, which harms they target, and where sup...
  </details>

- **2026-07-29** — Gal Engelberg, Michael Arenzon, Leon Goldberg — [Open Security Benchmark: Towards Autonomous Enterprise Cyber Defense](http://arxiv.org/abs/2607.27288v1)
  <details><summary>📄 Abstract</summary>
  Enterprises are moving toward autonomous cyber defense: agentic AI that builds situational awareness of an organization's security state and reasons from it to assessments, decisions, and actions. This rests on a holistic view of the enterprise's security state, the continuous, cross-vendor picture of identities, cloud and infrastructure, data, applications, and their configurations that security posture management assembles. As agents take on this work, what matters is not whether an agent can ...
  </details>

- **2026-07-29** — Chen Shani — [From Found to Designed: Concepts as a Design Axis for Large Language Models](http://arxiv.org/abs/2607.26825v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) encode rich concept-like information, but represent it implicitly through distributed statistical associations rather than as explicit, structured, compositional concepts. Consequently, concept-level structure is typically \emph{found} rather than \emph{designed}: it is recovered after training through probing or dictionary learning, with no architectural guarantee of stability, compositionality, controllability, or alignment with human conceptual organization. We or...
  </details>

- **2026-07-29** — Owais Mujtaba Khanday, Mohamed Baha Ben Ticha, Sanae Belfrouh et al. — [Does EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding](http://arxiv.org/abs/2607.27268v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models pretrained on thousands of hours have shown large gains over task-specific networks for motor imagery, seizure detection, sleep staging, and emotion recognition, but their transfer to speech decoding-arguably the most demanding non-invasive BCI application-remains untested. We present the first systematic benchmark of EEG foundation models against strong convolutional baselines for speech decoding, using two corpora: UGR-MINDVOICE (overt and covert Iberian Spanish) and BCI ...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 61 papers

- **2026-07-30** — Qiushi Sun, Kanzhi Cheng, Yian Wang et al. — [OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](http://arxiv.org/abs/2607.28609v1)
  <details><summary>📄 Abstract</summary>
  Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone...
  </details>

- **2026-07-30** — Xiao Luo, Mingyang Du, Xin Zhou et al. — [ROAD: Reciprocal-Objective Alignment of Discriminative Semantics for 3D Shape Generation](http://arxiv.org/abs/2607.28581v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity 3D generation predominantly relies on scaling model capacity and data, which incurs prohibitive computational costs. This paradigm typically requires learning geometry from scratch and overlooks the rich semantic and structural priors already encapsulated in discriminative 3D foundation models. We contend that leveraging the profound understanding of the 3D world possessed by these discriminative models can significantly reduce generative cost. To this end, we propose ROAD, a frame...
  </details>

- **2026-07-30** — Yunzhan Fu, Xiangyu Shen, Yifei Sun et al. — [MIND: Multimodal Intent-Driven Network via Diffusion Transformers for Medical Image Fusion](http://arxiv.org/abs/2607.28565v1)
  <details><summary>📄 Abstract</summary>
  Medical image fusion aims to integrate complementary information from diverse imaging modalities to support clinical diagnosis. Existing methods typically apply uniform fusion rules globally, lacking a deep understanding of diagnostic intents and pathological structures. To address these limitations, we propose MIND, a Multimodal Intent-Driven Network via Diffusion Transformers (DiTs) for medical image fusion. Specifically, we utilize BioMedGPT to generate intent-driven fusion texts from source ...
  </details>

- **2026-07-30** — Ioana-Roxana Boriceanu, Liviu P. Dinu — [Creative Transformation in Literary Texts: Modelling Change Across Representational Levels](http://arxiv.org/abs/2607.28513v1)
  <details><summary>📄 Abstract</summary>
  Creativity is often framed as the production of novelty, yet many cultural works emerge through transformation of earlier artifacts and not through isolated invention. Drawing on theories of imitation by Gabriel Tarde and James Mark Baldwin, this paper models creativity as selective transformation across multiple levels of textual representation. We introduce a multi-level framework that compares literary texts across lexical, semantic, conceptual, structural, and narrative dimensions using dire...
  </details>

- **2026-07-30** — Hansika Ekanayake Mudiyanselage, Rohan Jai Dharmaraj, Malik Abdul Sami et al. — [Integrating AI into Requirements Quality Learning in Software Engineering Education: A TPACK-Guided Empirical Study](http://arxiv.org/abs/2607.28176v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of generative Artificial Intelligence (AI) in software engineering (SE) practice creates a need for pedagogically grounded approaches to AI integration in SE education, especially in conceptually intensive subjects such as requirements engineering (RE). This study examines a TPACK-guided integration of a multi-agent AI tool into a master-level RE assignment on requirements quality analysis. Using a mixed-methods design (N=100; 72 submissions analysed), we examine how structure...
  </details>

- **2026-07-30** — Paulo Carvao, Claudio Mayrink Verdun, Isabel Adler et al. — [An Instrument to Evaluate Governance Proposals: AI Policy Analysis at Scale](http://arxiv.org/abs/2607.28094v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a policy analysis framework for systematic, transparent assessment of AI governance proposals in an evolving and contested regulatory landscape. AI policy debates often collapse into binary positions that obscure underlying tradeoffs and normative assumptions. The framework structures policy analysis around multiple policy attributes, allowing users to surface priorities and tensions without prescribing outcomes. We use a mixed-methods approach that integrates qualitative i...
  </details>

- **2026-07-30** — Qinhan Yu, Jun Guang, Chong Chen et al. — [VIG-RL: Learning to Search and Insert for Verified Image Grounding](http://arxiv.org/abs/2607.28055v1)
  <details><summary>📄 Abstract</summary>
  In knowledge-intensive scenarios, providing reliable interleaved text-image responses requires Verified Image Grounding (VIG): the precise integration of retrieved authentic visual evidence. Existing retrieval-augmented frameworks predominantly rely on decoupled, static pipelines, inherently failing to dynamically reason about when external knowledge is required and where visual assets should be contextually inserted. To bridge this gap, we propose VIG-RL, an autonomous agentic framework that fo...
  </details>

- **2026-07-30** — Xingjian Wu, Xuhang Zhu, Xingchen Liu et al. — [ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents](http://arxiv.org/abs/2607.28037v1)
  <details><summary>📄 Abstract</summary>
  As LLM-based agents are deployed in complex, multi-step workflows, a critical evaluation gap has emerged: most existing benchmarks judge only final outcomes, unable to distinguish reliable reasoning from lucky success or attribute failures to specific process deficiencies, hindering attribution in long-horizon tasks.   In this work, we present ClawTrack, a dual-assessment benchmark that simultaneously measures what an agent achieves (Task Score) and how it achieves it (Process Score). ClawTrack ...
  </details>

- **2026-07-30** — Xianpeng Zhang, Jiahua Yang, Dongyu Chen et al. — [MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware](http://arxiv.org/abs/2607.28006v1)
  <details><summary>📄 Abstract</summary>
  Multimodal long documents are core carriers of professional knowledge, where critical evidence is sparsely distributed across paragraphs and modalities. This easily causes key information omission and cross-modal hallucinations in summarization by multimodal LLMs. These issues stem from attention drift in long-range dependency modeling and gaps in inter-modal alignment. To address this, we introduce MMLDSum-Bench, a high-quality benchmark for multimodal long-document summarization, covering mult...
  </details>

- **2026-07-30** — Bohan Hou, Haoqiang Lin, Xuemeng Song et al. — [FiRE: Enhancing MLLMs with Fine-Grained Context Learning for Complex Image Retrieval](http://arxiv.org/abs/2607.27959v1)
  <details><summary>📄 Abstract</summary>
  Due to their strong generalizable multimodal processing and reasoning capabilities, Multimodal Large Language Models (MLLMs) have demonstrated significant potential as universal image retrievers, effectively addressing diverse real-world image retrieval tasks. Nevertheless, pioneering studies, while promising, overlook the potential of fine-grained context modeling and disentangled fine-tuning objectives in enhancing MLLMs' retrieval performance, particularly for complex tasks such as long-text-...
  </details>

- **2026-07-30** — Long Zhang, Hao Jiang, Sheng Yu et al. — [Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation](http://arxiv.org/abs/2607.27944v1)
  <details><summary>📄 Abstract</summary>
  While large language models (LLMs) have advanced ID-based recommendation through Semantic ID (SID) modeling, existing SID generation frameworks largely follow a single-representation-then-quantization paradigm. This design faces two bottlenecks: semantic entanglement mixes heterogeneous attributes, such as geography, brand, and category, causing information loss during quantization, low-quality SIDs, and severe collisions; moreover, black-box representation learning provides neither explicit att...
  </details>

- **2026-07-30** — Rui Tang, Wentao Yang, Peirong Zhang et al. — [One Patch Is Enough: Reinforcement-Optimized Visual Token Grounding for MLLM-Based Scene Text Spotting](http://arxiv.org/abs/2607.27902v1)
  <details><summary>📄 Abstract</summary>
  Scene text spotting requires high-precision alignment between textual recognition and spatial localization. While visual-token grounding has emerged as a promising formulation for Multimodal Large Language Models (MLLMs), the previous multi-patch paradigm often introduces redundant noise and localization ambiguity, particularly for dense or small text instances. To address this, we propose Single-Patch Text Spotting (SPaTS), a vision-centric framework that routes each text instance through a sin...
  </details>

- **2026-07-30** — Peiyu Hu, Siying Gu, Weihai Lu et al. — [Hierarchical Latent Reasoning for LLM-based Recommendation](http://arxiv.org/abs/2607.27760v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong potential for recommendation by leveraging their semantic understanding and contextual modeling capabilities. Recent studies further introduce reasoning mechanisms to improve user preference modeling. However, explicit natural-language reasoning incurs substantial inference overhead, whereas existing latent reasoning methods mainly focus on generating or verifying intermediate states, leaving their layer-wise preference roles and contributions insuf...
  </details>

- **2026-07-30** — Fouad Bousetouane — [Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness](http://arxiv.org/abs/2607.27677v1)
  <details><summary>📄 Abstract</summary>
  AI agents are moving into production workflows where they retrieve information, call tools, maintain state, and act on behalf of users or organizations, but many release decisions still rely on capability signals, demos, or behavioral tests that do not show whether an agent is ready to operate under production constraints. Capability is therefore not production readiness. This paper introduces the ProofAgent Index (PAI), a governance readiness index for AI agents. PAI combines four dimensions of...
  </details>

- **2026-07-30** — Zhankai Ye, Yukai Jin, Bingyang Wei et al. — [MUGEN: A Unified Framework for Efficient Motion Understanding and Generation](http://arxiv.org/abs/2607.27581v1)
  <details><summary>📄 Abstract</summary>
  Grounding human motion in language, and language in motion, is a central step toward physical AI systems that can understand, generate, and communicate human behavior. Unified motion--language systems first coupled the two directions through a shared discrete motion codebook, but quantization limits generation quality. The strongest generators buy quality back at growing cost: stacked residual codebooks enlarge the representation; masked decoding stages, long autoregressive rollouts, and denoisi...
  </details>

- **2026-07-30** — Haoqing Wang, Xingrun Xing, Wei Xia et al. — [FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification](http://arxiv.org/abs/2607.28225v1)
  <details><summary>📄 Abstract</summary>
  Agentic vision-language models (VLMs), which interleave textual reasoning with explicit tool calls such as cropping and code-based image manipulation, have emerged as a compelling paradigm for reliable and interpretable multimodal reasoning. However, recent studies have revealed that such models often use tools unfaithfully. Many process images are irrelevant to the question (e.g., the tool crops the wrong region or misses the queried target), yet the call still receives full credit and the mode...
  </details>

- **2026-07-29** — Arman Rahmim, Nourhan Bayasi, Xiaoxiao Li et al. — [Rethinking Artificial Intelligence in Medical Imaging: Assumptions, Reality, and Reframing](http://arxiv.org/abs/2607.27428v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging has served as primary proving ground for clinical artificial intelligence (AI), yet a decade of intense research has not translated into proportionate bedside impact. We argue that this gap is not primarily a product of insufficient algorithmic performance, inadequate regulation, or limited explainability. Rather, it reflects a structural misalignment, between how AI systems are designed and evaluated, and how clinical decisions are made. This Perspective identifies six interconn...
  </details>

- **2026-07-29** — Ru Peng, Tianyu Zhao, Xijun Gu et al. — [HSS-Synth: Humanities and Social Sciences Data Synthesis for LLMs](http://arxiv.org/abs/2607.27379v1)
  <details><summary>📄 Abstract</summary>
  High-quality, diverse data are vital for large language models (LLMs) but remain scarce and costly. Data synthesis is a viable alternative and succeeds on closed tasks, yet the humanities and social sciences (HSS) are overlooked, and their open-ended nature makes synthesis challenging. Moving beyond prior capability-centric, fragmented attempts, we adopt a subject-centric paradigm, define the first HSS domain system covering 14 mainstream fields, and introduce HSS-Synth, the first data synthesis...
  </details>

- **2026-07-29** — Ru Peng, Haokai Xu, Xijun Gu et al. — [BridgeAlign: Bridging Preference Alignment for Humanities and Social Sciences](http://arxiv.org/abs/2607.27366v1)
  <details><summary>📄 Abstract</summary>
  While data synthesis for large language models (LLMs) is prevalent, it primarily targets domains with verifiable answers, overlooking open-ended humanities and social sciences (HSS), where nuanced quality judgments matter more than objective correctness. This makes preference alignment a natural paradigm for broad HSS tasks. Yet existing methods are either costly or not tailored to broad HSS disciplines. We thus propose BridgeAlign, among the first preference-alignment pipelines for broad HSS di...
  </details>

- **2026-07-29** — Lei Zan, Keli Zhang, Shifeng Xie et al. — [EvoCause: LLM-Guided Evolution of Causal Graphs for Root Cause Analysis](http://arxiv.org/abs/2607.27290v1)
  <details><summary>📄 Abstract</summary>
  Modern telecommunication, cloud, and microservice systems emit correlated alarm cascades when components fail. Root cause analysis (RCA) aims to identify the small set of alarms that initiate each cascade. A common approach learns a causal graph from observational logs and predicts all zero-in-degree alarms in each incident-induced subgraph. However, the learned graph remains fixed and cannot benefit from expert diagnoses of historical incidents. We close this loop with EvoCause. Expert labels c...
  </details>

- **2026-07-29** — Lei Dong — [The Kinetics of Training: A Driven-Nucleation Rate Law for Emergence, Plasticity Loss, and Circuit Control in Language Models](http://arxiv.org/abs/2607.27281v1)
  <details><summary>📄 Abstract</summary>
  A capability appears in a language model when the last parts of its circuit align in one stochastic attempt, and getting all but one right is worth nothing. We show this no-partial-credit joint alignment is the rate-limiting step of capability formation. Two fingerprints: in a shortcut-free apparatus a five-part circuit missing three waits as long as a three-part circuit missing three (1.19-1.37), so the wait counts missing parts, not size; and on Pythia across seven capabilities and three scale...
  </details>

- **2026-07-29** — Desiree Cho, Cameron Tice, Bernie Hogan et al. — [Constitutional Midtraining: Content Presence Drives Alignment Gains](http://arxiv.org/abs/2607.26654v2)
  <details><summary>📄 Abstract</summary>
  Post-training alignment is often shallow, eroding under fine-tuning. It remains untested as to whether constitutional midtraining interventions can produce durable alignment when cleanly isolated from post-training. We build a 394M-token constitutional corpus from Anthropic's Constitution and apply constitutional midtraining at 120B scale, where principled, values-based content is inserted into midtraining. A 2x2 design (curriculum ordering x deliberative reasoning) was used to produce four cons...
  </details>

- **2026-07-29** — Hao Jiang, Peiru Du, Pengfei Yao et al. — [WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models](http://arxiv.org/abs/2607.26621v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong reasoning capabilities, motivating their adoption as backbones for foundation recommendation models (FRMs). Existing approaches typically enhance recommendation with explicit Chain-of-Thought (CoT) under the Think-then-Answer paradigm. However, generating lengthy rationales introduces substantial inference overhead, while fixed CoT templates struggle to model diverse, dynamic, and context-dependent user interests. We propose WhisperRec, an ef...
  </details>

- **2026-07-29** — Yuyun Chen, Tianao Li, TianQuan Feng et al. — [EgoSafe: A First-Person Mobile-Captured Benchmark for Visual Safety Understanding](http://arxiv.org/abs/2607.26518v2)
  <details><summary>📄 Abstract</summary>
  Reliable visual safety understanding in real-world scenarios demands more than just object recognition; it requires causal reasoning under epistemic uncertainty. While Large Vision-Language Models (LVLMs) demonstrate impressive semantic alignment on standard benchmarks, they often struggle to distinguish between superficial correlation and genuine forensic logic when grounded in the dynamic, partially observable nature of first-person experiences. Existing evaluations, dominated by third-person ...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 78 papers

- **2026-07-30** — Xiangyu Yin, Jiaxu Liu, Zhen Chen et al. — [Crossing the Margin Cliff: Toward Relearn-Robust LLM Unlearning via Margin Calibration](http://arxiv.org/abs/2607.27836v1)
  <details><summary>📄 Abstract</summary>
  Large language model unlearning is consistently fragile under relearn attacks. On TOFU, fine-tuning on twenty forget examples substantially recovers held-out forget-set ROUGE for every method we evaluate, and we trace this fragility to optimization geometry. The per-token answer margin of fourteen post-hoc methods spanning gradient, preference, and distillation families converges into a narrow band above the retain reference in 41 of 42 method--size cells, a regularity we call the margin cliff. ...
  </details>

- **2026-07-30** — Minghao Hu, Lannan Luo, Allen Roush et al. — [CoGate: Confidence-Gated Co-Decoding for Secure Code Generation](http://arxiv.org/abs/2607.28529v1)
  <details><summary>📄 Abstract</summary>
  Large language models are widely used for code generation, but they can also produce insecure programs due to patterns learned from their pretraining data. Decoding-time steering has become an important solution to this problem: a small expert model is combined with the target model at each step to generate more secure code, which is referred to as co-decoding. However, the acceptance rule for existing co-decoding approaches does not consider the expert model's confidence. When the security expe...
  </details>

- **2026-07-30** — Jie Ma, Zhike Qiu, Jie Gao et al. — [Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large Language Models](http://arxiv.org/abs/2607.28341v1)
  <details><summary>📄 Abstract</summary>
  While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs), existing training-free methods suffer from a critical limitation: they rely on static, instantaneous heuristics to perform irreversible filtering. This approach ignores the hierarchical nature of MLLMs, where token importance often evolves dynamically rather than remaining fixed across layers. Consequently, tokens essential for deep-layer reasoning are often prematurely discarded by shallow-layer esti...
  </details>

- **2026-07-30** — Rong Wu, Daocheng Fu, Licheng Wen et al. — [MemHarness: Memory Is Reconstructed, Not Replayed](http://arxiv.org/abs/2607.28272v1)
  <details><summary>📄 Abstract</summary>
  Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causi...
  </details>

- **2026-07-30** — Samuele Lo Piano, Alessio Lachi, Razi Sheikholeslami et al. — [Improving Discrepancy Measures for Global Sensitivity Analysis](http://arxiv.org/abs/2607.28252v1)
  <details><summary>📄 Abstract</summary>
  Sensitivity analysis methods based on Sobol' total-order indices ($T_i$) are well-founded but computationally demanding. A recently proposed ersatz discrepancy measure offers a cheaper alternative by quantifying deviations from uniformity in input--output scatterplots, yet lacks theoretical grounding and has not been benchmarked against other data-given estimators. We introduce an adjusted ersatz discrepancy that rank-transforms the output before gridding and imputes isolated empty cells via a M...
  </details>

- **2026-07-30** — Sangjin Kim, Yuseon Choi, Jungjun Oh et al. — [LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference](http://arxiv.org/abs/2607.27704v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to demonstrate exceptional capabilities across various domains, the challenge of achieving energy-efficient and accurate inference becomes increasingly critical. This work presents LightRot, a lightweight rotation scheme and dedicated hardware accelerator designed for low-bit LLM inference. The proposed architecture integrates Grouped Local Rotation (GLR) and Outlier Direction Aligning (ODA) algorithms with a hierarchical Fast Hadamard Transform (FHT)-bas...
  </details>

- **2026-07-30** — Site Li, Jianyi Hao, Xiaofeng Liu — [Objective-Aligned Direct Answer SFT for Robust Multi-Frame Medical VQA](http://arxiv.org/abs/2607.27566v1)
  <details><summary>📄 Abstract</summary>
  Multi-frame medical VQA appears to reward increasingly complex adaptation: controller-style inference, localization-aware reranking, static hard-negative mixing, and staged continuation all appear plausible from first principles. We test a simpler competing hypothesis on MedFrameQA: methods that remain tightly aligned with the benchmark's final answer objective should be the strongest \emph{robust} adaptation family once evaluation is controlled across fixed splits, matched budgets, repeated see...
  </details>

- **2026-07-30** — Zongheng Guo, Tao Chen, Tianli Li et al. — [When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence](http://arxiv.org/abs/2607.28421v1)
  <details><summary>📄 Abstract</summary>
  Derived measurements increasingly enter large language model (LLM) pipelines as direct facts despite their instance-dependent validity. We define derived-feature over-trust (DFOT) as the failure in which a downstream LLM assigns such a measurement the epistemic status of a direct fact or uses it outside its valid scope. Using physiological sensing as a case study, D1 tests acceptance of a PPG-derived rhythm contradicted by offline ECG, whereas D2 tests rejection of an offline-confirmed reliable ...
  </details>

- **2026-07-30** — Xiaoyu Zhang, Xianyun Cheng, Tianlin Li et al. — [Not as Sweet by Another Name: An Empirical Study of Format Robustness in LLM Document Workflows](http://arxiv.org/abs/2607.27648v1)
  <details><summary>📄 Abstract</summary>
  LLM-driven software systems are rapidly evolving from plain-text conversations to document-centric end-to-end workflows, where the same semantic content can be delivered in diverse document formats (e.g., CSV) through file upload interfaces. Yet existing testing work focuses on the robustness and reliability of models and systems whose input is a single prompt string, leaving a critical question unanswered: Can these document workflows maintain robust behaviors when the same content arrives in a...
  </details>

- **2026-07-30** — Alev Cinbarci, Sean Kalaycioglu — [Forecasting Land Art Under Climate Scenarios](http://arxiv.org/abs/2607.28489v1)
  <details><summary>📄 Abstract</summary>
  Robert Smithson's 1970 land artwork Spiral Jetty, located in the north arm of Utah's Great Salt Lake, provides a fixed remote-sensing target whose visual complexity reflects hydroclimatic conditions. A companion study analyzed 1,744 co-registered Landsat 4-9 and Sentinel-2 image chips spanning every year and month from 1984 to 2025. It found robust relationships between coarse-scale permutation entropy, mean intensity, and the third principal component of ResNet50 avg-pool embeddings, and lake e...
  </details>

- **2026-07-30** — Ngoc Thai Le, Thanh Ma, Umberto Straccia — [A Fuzzy Rule-based Neuro-Symbolic Approach for Pipe Severity Prediction in Sewer Networks](http://arxiv.org/abs/2607.28481v1)
  <details><summary>📄 Abstract</summary>
  Standard automated sewer pipe severity assessment relies on direct image classification, creating a "black box" where the link between visual defects and final severity scores remains implicit. This study introduces a modular, fuzzy rule-based neuro-symbolic framework that bridges this gap by decoupling neural perception from symbolic reasoning. The perception module utilizes a Swin Transformer to predict 14 multilabel inspection CODE degrees directly from images. For reasoning, a DT, specifical...
  </details>

- **2026-07-30** — Antonio Delgado-Rosa, David Muñoz-Valero, Enrique Adrian Villarrubia-Martin et al. — [Towards Autonomous Aircraft Surveillance from Nanosatellites through On-Board Inference and Generative Data Augmentation](http://arxiv.org/abs/2607.28470v1)
  <details><summary>📄 Abstract</summary>
  Airborne surveillance from low Earth orbit is hindered by two interconnected bottlenecks: nanosatellites have a limited downlink budget, yet the conventional approach still transmits terabytes of raw imagery to the ground for processing, and open satellite datasets for aircraft are scarce and severely class-imbalanced. These limitations either delay timely decision-making or prevent standard detectors from learning robust representations of rare aircraft classes. In this paper, a workflow that c...
  </details>

- **2026-07-30** — Ping-Kun Chiang, Kun-Ru Wu, Po-han Li et al. — [ViewMind3D: Modular View-Aware Inference for Training-Free 3D-QA](http://arxiv.org/abs/2607.28442v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled new possibilities for 3D question answering (3D-QA), a key capability for embodied AI and robotic perception. However, most existing methods rely on 3D-specific training or fine-tuning with costly annotations, limiting their scalability and real-world applicability. We present \textbf{ViewMind3D}, a fully training-free and modular framework for 3D spatial reasoning over multi-view observations of a sce...
  </details>

- **2026-07-30** — Ran Miao, Rui Luo, Xiaohan Shan et al. — [QAdapt: A Noise-Adaptive Neural Pre-Decoding Framework for Quantum Error Correction](http://arxiv.org/abs/2607.28422v1)
  <details><summary>📄 Abstract</summary>
  Fault-tolerant quantum computing (FTQC) relies on quantum error correction to suppress physical errors and preserve logical information at scale. In practice, however, performance is constrained not only by physical noise but also by the latency of classical decoders processing rapidly generated syndrome data. This challenge is exacerbated by hardware noise that is strong, heterogeneous, and nonstationary, as well as by the simulation-to-hardware distribution shift that can substantially degrade...
  </details>

- **2026-07-30** — Zihan Dong, Zhiyuan Ma, Zekun Wang et al. — [How Benchmarks Mis-Score Computer-Use Agents](http://arxiv.org/abs/2607.28367v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUA) are being deployed to browse the web and operate desktop software, yet their benchmark scores are still commonly produced by brittle scripted oracles. A score is the output of a pipeline in which tasks can be stale, trajectories can omit decisive visual evidence, evaluators can reject valid alternatives, and aggregate reports can hide the cause of failure. We organize these problems into a reliability framework spanning task construction, trajectory observation, scoring...
  </details>

- **2026-07-30** — Daniel Silva, Renan Alves, Emanuel Dantas Filho et al. — [Structural Validation of LLM-Generated Microservice Decompositions Using Source-Code Dependencies](http://arxiv.org/abs/2607.28331v1)
  <details><summary>📄 Abstract</summary>
  Decomposing monolithic systems into microservices is a key activity in software modernization. Although Large Language Models (LLMs) can generate semantically plausible decompositions from textual requirements, it remains unclear whether these proposals preserve the structural dependencies implemented in the source code. This paper evaluates the structural adherence of microservice decompositions generated by OpenAI o3 for the PetClinic and Bookstore systems. We propose an automated validation p...
  </details>

- **2026-07-30** — Rasmus Tirsgaard, Laurits Fredsgaard, Marisa Wodrich et al. — [Semi-Supervised Learning for Molecular Graphs via Ensemble Consensus](http://arxiv.org/abs/2607.28304v1)
  <details><summary>📄 Abstract</summary>
  Machine learning is transforming molecular sciences by accelerating property prediction, simulation, and the discovery of new molecules and materials. Acquiring labeled data in these domains is often costly and time-consuming, whereas large collections of unlabeled molecular data are readily available. Standard semi-supervised learning methods often rely on label-preserving augmentations, which are challenging to design in the molecular domain, where minor changes can drastically alter propertie...
  </details>

- **2026-07-30** — Anubhav Lakra, Yue Feng — [CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance](http://arxiv.org/abs/2607.28292v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) deployed in dynamic financial environments face a critical challenge: maintaining factual accuracy as market conditions, regulations, and corporate facts change continuously. While 4-bit quantization enables efficient deployment, it severely limits the viability of sequential memory editing: existing methods undergo catastrophic performance degradation under this "quantization stability crisis." We introduce CACHE-UK (Contextual Adaptive Continual Hybrid Editor for U...
  </details>

- **2026-07-30** — Steven Y. Alberding, Patrick J. Breheny — [A Novel Approach to Instrumental Variable Estimation: TEAM-IV](http://arxiv.org/abs/2607.28289v1)
  <details><summary>📄 Abstract</summary>
  Instrumental-variable (IV) analyses can be undermined when some instruments violate the exclusion restriction through direct effects on the outcome. Existing robust IV methods, including sisVIVE and CIIV, rely on majority- or plurality-validity conditions. We propose TEAM-IV, which targets joint validity by identifying sets of instruments that appear valid together and aggregating them, allowing reliable estimation even when only a small number of candidate instruments are valid (potentially as ...
  </details>

- **2026-07-30** — Yusen Liu, Yong Wang, Yifan Yin et al. — [Causal Discovery with Inverted Self-attention for Multivariate Time Series](http://arxiv.org/abs/2607.28212v1)
  <details><summary>📄 Abstract</summary>
  Causal discovery in multivariate time series data is challenging due to complex interactions, high dimensionality, and nonlinear dependencies among variables. Existing methods often struggle to capture these complexities, resulting in inaccurate causal structures. To address this issue, we propose a novel framework that leverages self-attention mechanisms within the transformer architecture for causal discovery. Our approach introduces a novel inverted causal self-attention mechanism (CSAM) that...
  </details>

- **2026-07-30** — Ioannis Sarridis, Ioannis Kompatsiaris, Symeon Papadopoulos — [Scaling Vision-Language Models Is Not Enough to Mitigate Bias](http://arxiv.org/abs/2607.28211v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) such as CLIP are now foundational to multimodal systems, yet their robustness to spurious correlations remains poorly understood at scale. We present the first large-scale empirical study of 194 publicly available VLMs, including 16 model families, covering a wide range of model sizes, 24 training datasets, and three evaluation benchmarks, namely ImageNet (overall performance), CelebA (typical single-attribute bias), and UrbanCars (complex multi-attribute biases). A...
  </details>

- **2026-07-30** — Hugo Gobato Souto, Ioannis Diamantis — [A Mathematical Framework for Topological Causal Data Analysis](http://arxiv.org/abs/2607.28161v1)
  <details><summary>📄 Abstract</summary>
  Many modern outcomes, including images, point clouds, networks, and spatial fields, are structured objects for which \(Y^1-Y^0\) may be undefined or scientifically inadequate. We introduce \emph{Topological Causal Data Analysis} (TCDA), a framework separating the observation space, causal-model class, topological representation, and causal query. Topology does not define interventions; it supplies stable, shape-sensitive summaries after causal assumptions have been specified. We distinguish outc...
  </details>

- **2026-07-30** — Behrad Mousaei Shir-Mohammad, Seyed Reza Tavakoli, Mohammad Mohammadi et al. — [When Linear RUL Labels Disagree with Vibration Degradation: A Stage-Aware Target and Dual-Scale Predictor Evaluated on XJTU-SY and IMS](http://arxiv.org/abs/2607.28115v1)
  <details><summary>📄 Abstract</summary>
  Remaining useful life (RUL) studies commonly treat the label as fixed, although clock-linear labels may decline while measured vibration remains nearly stable and then changes rapidly near failure. We separate target design from prediction. A development-only pipeline constructs an oriented vibration health indicator, identifies chronological early, middle, and late stages, and fits a continuous linear-quadratic-exponential degradation-state target. A compact CNN-LSTM and Transformer learn the t...
  </details>

- **2026-07-30** — Ziyi Yang, Thanh-Son Nguyen, Tuan Anh Nguyen et al. — [GGC: Selective Query Correction for Reliable Text-to-SPARQL Generation](http://arxiv.org/abs/2607.28082v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in structured query generation, making them a natural choice for Text-to-SPARQL, which translates natural language questions into executable SPARQL queries over knowledge graphs. However, their initial outputs remain unreliable: generated queries may be executable yet semantically misaligned with input questions, leading to incorrect retrieval. To address this issue, we propose Generator-Gate-Corrector (GGC), a framework for reli...
  </details>

- **2026-07-30** — Illia Horenko — [On a joint simultaneous learning of relevant feature subsets and subspaces in regression-like problems](http://arxiv.org/abs/2607.28080v1)
  <details><summary>📄 Abstract</summary>
  We extend a recently introduced Entropy-Optimal Manifold Clustering (EOMC) to allow for a joint simultaneous identification of subsets and subspaces of relevant features in nonstationary and nonlinear regression problems. It is shown that the proposed extension - that we coin as Entropy-Optimal Manifold Regression (EOMR) - allows a robust learning with linearly-scaling iteration and memory complexities. EOMR is compared to the most complete set of state-of-the-art tools from the Artificial Intel...
  </details>

- **2026-07-30** — Sangwoo Jung, Dongjae Lee, Chiyun Noh et al. — [RaDiVe: Robust 4D Radar Odometry with Distance-Bounded NDT and Velocity-Discrepancy Point Uncertainty](http://arxiv.org/abs/2607.28045v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in 4D radar enable robust perception in adverse weather; however, the inherent sparsity, noise, and limited positional precision of radar point clouds pose significant challenges for registration-based odometry. In this letter, we propose RaDiVe, a 4D radar odometry framework designed to improve the accuracy and robustness of radar point-cloud registration. We introduce a distance-bounded Normal Distributions Transform (NDT), which improves optimization stability and computationa...
  </details>

- **2026-07-30** — Kağan Akman, Naci Saldi, Serdar Yüksel — [Generalization Bounds on Optimal Control for Transformer Training and Wasserstein Distributional Robustness](http://arxiv.org/abs/2607.27975v1)
  <details><summary>📄 Abstract</summary>
  We derive finite-sample generalization bounds for Transformers trained with dynamic programming recursions. Building on the doubly lifted, measure-valued formulation of Transformer dynamics, we view data sets as probability laws on pairs of empirical input-output measures, allowing us to interpret the training problem as a finite-horizon Markovian control problem. We then analyze a quantized model, derived by quantizing the state, action, and measure-state spaces, and derive explicit finite-samp...
  </details>

- **2026-07-30** — Dawei Wang, Di Zhao, Xinyuan Liu et al. — [MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation](http://arxiv.org/abs/2607.27967v1)
  <details><summary>📄 Abstract</summary>
  Credit assignment is a fundamental challenge in cooperative multi-agent reinforcement learning, particularly in embodied AI settings characterized by limited and delayed feedback as well as dynamically changing numbers of active agents. We propose MARS-RA, a framework that reformulates credit assignment as a rank aggregation problem using contribution-based pairwise comparisons among agents generated by large multimodal models. This shift from absolute to relative estimation ensures robustness a...
  </details>

- **2026-07-30** — Xianchao Xiu, Jianhao Li, Huangyue Chen et al. — [OptGraph: Large Language Models Enhanced Evolutionary Optimization Via Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2607.27918v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have emerged as a powerful tool for automated evolutionary optimization, but existing methods remain limited in pattern reuse, error-aware refinement, and retrieval robustness across diverse tasks. To address these limitations, we propose OptGraph, the first optimization agentic workflow that introduces graph retrieval-augmented generation (GraphRAG). Specifically, OptGraph first constructs reusable experience as a typed graph, capturing the relationships among model...
  </details>

- **2026-07-30** — Hamidreza Razavi, Nele Moelans — [Deep Learning for Accelerated Long-Horizon Forecasting of Multicomponent Multiphase Microstructure Evolution in High-Entropy Alloys](http://arxiv.org/abs/2607.27820v1)
  <details><summary>📄 Abstract</summary>
  Phase-field modeling provides a powerful approach for predicting microstructure evolution but becomes computationally prohibitive for multicomponent and multiphase systems over large spatial and temporal scales. This work presents an AE-GCN-LSTM surrogate framework for long-horizon forecasting of microstructure evolution in the multicomponent AlCrFeNi high-entropy alloy system containing coexisting BCC and FCC phases. A multi-head autoencoder compresses the four elemental concentration fields an...
  </details>

- **2026-07-30** — Jiasheng Li, Zhong Ji, Yan Zhang et al. — [Calibrate Before Reason: Robust Visual Token Reduction against Semantic Drift in VLMs](http://arxiv.org/abs/2607.27700v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (VLMs) suffer from prohibitive inference overhead due to long sequences of visual tokens. However, existing visual token reduction methods mainly improve efficiency by pruning or compressing redundant tokens without examining whether the resulting representation remains semantically consistent with the original representation. Mapping the original N-token visual sequence to K tokens may discard, dilute, or misassign critical visual cues, triggering severe semantic dr...
  </details>

- **2026-07-30** — Wenjie Zhu, Yabin Zhang, Wenjun Zeng et al. — [MMOOC: A Comprehensive Benchmark for Out-of-Context Evaluation in Multimodal Large Language Models](http://arxiv.org/abs/2607.27637v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved strong performance on a wide range of vision-language tasks, but often fail under imperfect or shifted contexts. A reliable MLLM should refuse truly out-of-context (OOC) questions with subject-level context shifts while still answering shifted in-context (Shifted IC) questions with non-subject context shifts. Existing benchmarks mainly target OOC or visually unanswerable questions, but overlook answerable Shifted IC cases and cover limited O...
  </details>

- **2026-07-30** — Zhaoji Wang, Wanyu Si, Jun Wang — [Beyond Similarity: Grounded Agentic Extraction and Expert-Adjudicated Evaluation of Intertextuality in Classical Chinese Histories](http://arxiv.org/abs/2607.27595v1)
  <details><summary>📄 Abstract</summary>
  Computational approaches to intertextuality have advanced from string matching to neural retrieval, yet their outputs, similarity scores and parallel-passage lists, identify where texts reuse one another without characterizing how or why. We recast fine-grained intertextuality extraction as an agentic task in which a large language model (LLM) reads two text units in full and, through a constrained tool interface, must ground each proposed reuse in exact character spans on both sides and label i...
  </details>

- **2026-07-30** — Jinfan Zhou, Richard Liu, Itai Lang et al. — [MeshFM: 2D Features Are All You Need for 3D Shape Understanding](http://arxiv.org/abs/2607.27592v1)
  <details><summary>📄 Abstract</summary>
  We present MeshFM, an efficient feedforward framework for extracting rich features from 3D inputs. Our method distills 2D features from visual foundation models into 3D. We train a feedforward network to directly predict 3D features without requiring optimization during inference. The approach utilizes a two-stage training strategy. First, we optimize a feature field in 3D using only 2D feature supervision. Second, we train a network to regress this feature field. The entire procedure requires n...
  </details>

- **2026-07-30** — Site Li, Jianyi Hao, Xiaofeng Liu — [Inference-Time Agentic Decision Rules Beat Longer Evolving Search for Multi-Image Medical Reasoning](http://arxiv.org/abs/2607.27564v1)
  <details><summary>📄 Abstract</summary>
  Multi-image medical VQA is not merely a prompt-length problem; it is a fundamental challenge of agentic decision-making. Medical vision-language agents must aggregate evidence across ordered images, remain robust to answer-order perturbations, and avoid overfitting to noisy search-time feedback. We study MedFrameQA through a controlled comparison of five inference-time agentic strategies, optimized using the same high-budget ShinkaEvolve configuration and evaluated on a reproducible internal fro...
  </details>

- **2026-07-30** — Mingi Kim, Yongjun Kim, Hyungki Kim — [Drawing-Recode: Annotation Grounding for Parametric CAD Code Generation from Raster 2D CAD Drawings](http://arxiv.org/abs/2607.27558v1)
  <details><summary>📄 Abstract</summary>
  Recovering Parametric CAD sequences from raster-format 2D Computer-Aided Design (CAD) drawings accumulated prior to digital transformation is important for part reproduction and manufacturing process automation. However, existing studies either process only vector drawings or are limited to specific domains, and fail to explicitly connect dimensional annotations to geometric information, limiting their use of dimensional information for 3D Parametric CAD sequences recovery. We propose Drawing-Re...
  </details>

- **2026-07-30** — Phuc Pham, Truong-Son Hy — [Evaluating Agentic Bioinformatics through Function, Evidence, and Validation](http://arxiv.org/abs/2607.27556v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly plan, execute, and interpret biological analyses, yet fluent responses, successful tool calls, and benchmark performance alone do not establish scientific credibility. Existing reviews primarily organize biological agents by application, architecture, and agentic capability, but do not jointly operationalize the accountability of agent-generated workflows. We address this gap by treating the inspectable workflow trajectory, rather than architecture or fin...
  </details>

- **2026-07-29** — Prabhjot Singh, Pritam Deka, Vijay Chennareddy — [Same Facts, Different Diagnosis: Measuring and Mitigating Narrative Anchoring in Clinical Language Models](http://arxiv.org/abs/2607.27384v1)
  <details><summary>📄 Abstract</summary>
  Large language models used for clinical diagnostic reasoning are sensitive to sociolinguistic register, not just clinical content. We term this failure mode Narrative Anchoring: identical clinical facts expressed in different registers cause diagnostic outputs to diverge. Unlike prior demographic-bias work, which manipulates explicit identity tokens such as race or income, our benchmark isolates register as the sole channel of variation, with no demographic marker present in any form. We constru...
  </details>

- **2026-07-29** — Joohyun Lee, Sungwoo Hong — [Hierarchical Reranking for Scalable Financial RAG System](http://arxiv.org/abs/2607.27523v1)
  <details><summary>📄 Abstract</summary>
  Analyzing financial documents such as 10-K filings, tabular disclosures, and macroeconomic reports demands expert reasoning and extensive time. However, existing Retrieval-Augmented Generation systems often struggle to process hybrid text-table structures or the massive scale of financial documents. To address these challenges, we propose Hierarchical Reranker, a RAG framework designed to improve retrieval performance and generative reliability across large-scale financial datasets. The system i...
  </details>

- **2026-07-29** — Lucas Greff Meneses, Evandro S. Ortigossa, Claudio Silva et al. — [FADEx: Feature Attribution and Distortion-based Explanation of Dimensionality Reduction](http://arxiv.org/abs/2607.27463v1)
  <details><summary>📄 Abstract</summary>
  Dimensionality Reduction (DR) is a fundamental tool for high-dimensional data exploration, reducing the complexity of latent spaces of machine learning models, and assisting in the explanation of complex opaque models. However, non-linear DR techniques often function as opaque transformations themselves, making it challenging to understand how individual features influence instance positioning in the reduced space. This lack of transparency complicates the analysis and interpretation of structur...
  </details>

- **2026-07-29** — Satya Kokonda — [MatCreatioNN: Machine learning-guided computational discovery of photocatalysts for environmental applications](http://arxiv.org/abs/2607.27295v1)
  <details><summary>📄 Abstract</summary>
  The rational design of photocatalysts for environmental remediation and CO2 conversion remains limited by the high computational cost and sparse experimental data describing multi-parameter photocatalytic behavior. This work presents an integrated machine-learning framework that couples reinforcement learning-based metal-organic framework (MOF) generation with a multi-stage Crystal Graph Convolutional Neural Network (CGCNN) prediction funnel to identify photocatalysts optimized across multiple e...
  </details>

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

- **2026-07-28** — Abhishek Pillai, Samir Kumar Nayak, Yuan Chen — [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](http://arxiv.org/abs/2607.26041v2)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observ...
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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 20 papers

- **2026-07-30** — Chunpeng Wang, Yanan Shi, Zhiqiu Xia et al. — [SPFM-Net: Semantic-Prior-Guided Frequency-Constrained Mamba for Invisible Watermark Attack](http://arxiv.org/abs/2607.27811v1)
  <details><summary>📄 Abstract</summary>
  Existing watermark attacks typically rely on predefined signal-processing operations or locally constrained restoration networks, making it difficult to capture the long-range dependencies of globally distributed watermark signals and resulting in an unfavorable trade-off between removal effectiveness and visual fidelity. In this paper, we propose SPFM-Net, a semantic-prior-guided and frequency-constrained Mamba framework for invisible watermark attack. SPFM-Net first employs high-ratio masking ...
  </details>

- **2026-07-30** — Bing Yan, Gregory Wolfe, Stefano Martiniani et al. — [AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis](http://arxiv.org/abs/2607.28618v1)
  <details><summary>📄 Abstract</summary>
  Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying c...
  </details>

- **2026-07-30** — Yecheng Wu, Song Han, Han Cai — [Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation for Large Reasoning Models](http://arxiv.org/abs/2607.28449v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) provides dense token-level supervision from a teacher, but its effectiveness can depend on teacher consistency, meaning that the model providing OPD supervision should also have generated the demonstrations used to train the supervised fine-tuning (SFT) reference. However, this condition is frequently violated in practice when SFT data have mixed or unknown provenance or when different models are preferred for SFT data generation and subsequent distillation. In such ...
  </details>

- **2026-07-30** — Enjun Du, Hange Zhou, Chenxu Du et al. — [LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger](http://arxiv.org/abs/2607.28374v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents for visual question answering increasingly operate as multi-step trajectories that interleave perception, retrieval, and reasoning, yet evaluation still largely reduces to final-answer accuracy. This aggregate signal cannot tell whether a correct answer was reached through grounded evidence, language priors, or accidental error cancellation. We propose to treat a multimodal agent trajectory as a provenance-constrained state machine: tool outputs are normalized into a Structured...
  </details>

- **2026-07-30** — Jennifer D'Souza, Sameer Sadruddin, Anisa Rula et al. — [SciSchema.org: A Multidisciplinary Collection of Schemas for Structured Scientific Process Descriptions](http://arxiv.org/abs/2607.27955v1)
  <details><summary>📄 Abstract</summary>
  Scientific processes are often described in heterogeneous article discourse, with details needed for comparison, reproducibility, reuse, and automation dispersed across prose, tables, figures, protocols, and supplementary files. We present the first release of SciSchema.org, a multidisciplinary collection of 16 expert-annotated schemas spanning Biology & Biotechnology, Materials & Chemistry, Imaging & Measurement, Physics, and Psychology. Each schema defines reusable fields for describing proces...
  </details>

- **2026-07-29** — Jinwei Hu, Yi Qi, Xinmiao Huang et al. — [Skill Use or Skill Theater? Evaluating the Reasoning Backroom in Skill-Augmented Language Agents](http://arxiv.org/abs/2607.27484v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills are becoming a standard interface for extending language agents with task procedures. Yet evaluators usually infer skill use from visible reasoning or the agent's own attribution. These signals show what the agent appears to use, not whether the skill changed its decision. We ask whether skill-augmented agents exhibit a \textbf{Reasoning Backroom}, a systematic gap between stated skill use and intervention-measured influence. We introduce BACKTRACE, an evaluation framework that p...
  </details>

- **2026-07-29** — Zuyuan Zhang, Hanqing Yang, Carlee Joe-Wong et al. — [Auditing Emergent LLM-Agent Collaboration through Cooperation-Obligation Coupling](http://arxiv.org/abs/2607.27429v1)
  <details><summary>📄 Abstract</summary>
  LLM-agent systems can solve complex tasks through dynamic self-organization and emergent cooperation. Auditing this process is essential because plausible intermediate or final outputs can conceal incomplete or unsupported work and poorly allocated responsibility, ultimately compromising response quality. While existing approaches may record messages, tool calls, provenance, or task dependencies, an auditability gap exists as they do not jointly represent what work remains, who is responsible fo...
  </details>

- **2026-07-29** — Supratik Bhowal, Subhrajyoti Basu, Aritra Gir Mahanta et al. — [Position, Not Provenance: Separating Reasoning Mediation from Sycophancy in Medical Vision-Language Models](http://arxiv.org/abs/2607.27304v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) generate chain-of-thought (CoT) reasoning before answering clinical questions, but whether this reasoning causally influences predictions remains unclear. We present CoT-Mediate, a behavioral framework that perturbs a single clinically meaningful attribute within a model's own generated reasoning and measures whether the resulting prediction follows the edited reasoning. Our framework combines a dual-arm protocol comparing re-prompted evidence with prefix-fo...
  </details>

- **2026-07-29** — Hailong Jiang, Emran Hossain, Feng Yu et al. — [BMOA: Baseline-Mechanism-Outcome Attribution for Compiler-Induced Numerical Deviations](http://arxiv.org/abs/2607.27270v1)
  <details><summary>📄 Abstract</summary>
  Formalizing compiler-aware numerical correctness requires distinguishing what an observed floating-point difference means, what compiler behavior the evidence supports, and what numerical consequence follows. Existing testing workflows often collapse these questions into a pass/fail mismatch. We introduce Baseline--Mechanism--Outcome Attribution (BMOA), a diagnostic framework that separates the comparison relation and system boundary, the evidence-supported compiler mechanism, and the reference-...
  </details>

- **2026-07-29** — Yize Li, Ruiqi Yu, Tianya Pan et al. — [GraphQAG: A Knowledge-Graph-Guided Visual Analytics Framework for Question-Answer Pairs Generation](http://arxiv.org/abs/2607.27182v1)
  <details><summary>📄 Abstract</summary>
  Question-answer (QA) pairs are widely used in knowledge base construction, question-answering systems, and the post-training of large language models (LLMs). However, important knowledge in long documents is often distributed across multiple paragraphs and connected through complex entity relationships. Such fragmented and relational knowledge poses substantial challenges for existing QA generation methods, which often fail to adequately cover core document content, cross-paragraph semantic conn...
  </details>

- **2026-07-29** — Zekun Ren, Hongzhao Tan, Jiaen Yee et al. — [PUDA: An AI-Native Hardware Harness for Self-Driving Laboratories](http://arxiv.org/abs/2607.26464v1)
  <details><summary>📄 Abstract</summary>
  Physical Unified Device Architecture (PUDA) is an AI-native hardware harness for self-driving laboratories (SDLs). Rather than building a human-centered graphical user interface (GUI) orchestration layer, PUDA creates a command-line runtime environment that lets agents observe, orient, decide, and act over experiments while hardware execution remains deterministic, atomic, and auditable. Headless by design, devices appear through discoverable command-line interfaces, JSON protocols are routed th...
  </details>

- **2026-07-28** — Andreas Bauer — [The Last Costly Signal: How Generative AI Collapses Competence Signaling and Why Liability Sustains Markets for Expert Services](http://arxiv.org/abs/2607.26327v2)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence has reduced the cost of producing convincing artifacts of expertise-reports, analyses, proposals-to nearly zero. Signaling theory predicts that signals whose informational content rests on production cost lose that content when production becomes cheap. We formalize this prediction for markets for expert services, a class of credence goods, by modeling generative AI as a compression of the discernible headroom between what machines produce at negligible cost an...
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


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-07-30** — I. Kennedy, T. Kennedy — [Fidelity Is Not Safety: Gently-Compressed LLMs Pass Every Data-Free Quality Guard Yet Invent Procedure Steps in Agentic Execution](http://arxiv.org/abs/2607.28196v1)
  <details><summary>📄 Abstract</summary>
  Practitioners accept a compressed language model once it clears a stack of data-cheap quality guards: perplexity within a small factor of the original, downstream accuracy (for example MMLU) inside a confidence interval, and data-free output-fidelity signals that compare the compressed and original network's internal representations under random probe inputs. This stack has a blind spot. Across three model families, gently-compressed models clear every guard and then invent procedure steps that ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-07-30** — Yanshi Li, Xueru Bai, Shuman Liu et al. — [RepBench: Compiling Benchmarks into Capability Representations for Large Language Models](http://arxiv.org/abs/2607.28008v1)
  <details><summary>📄 Abstract</summary>
  Representation engineering reads and steers capability directions in large language models, yet methods are typically evaluated on paper-specific synthetic data. The resulting measurements are difficult to compare or reproduce and may reflect surface patterns rather than capabilities. We present RepBench, a benchmark-grounded data layer for capability-aligned representation probing. Crawling 13,427 benchmark papers yields a taxonomy of 182 capability clusters in 13 families; harvesting 353 publi...
  </details>

- **2026-07-30** — Shalini Chakraborty, Michael Mittermaier, Judith Michael — [The Case for Vibe Modeling: A Missing Step in AI-Based Trustworthy Software Development](http://arxiv.org/abs/2607.27923v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to generate software artifacts from natural language prompts. While this enables rapid prototyping and lowers the barrier to software creation, it also introduces challenges related to understanding, validation, traceability, and trust. In this paper, we argue that current AI-based development practices focus too heavily on the direct generation of code and insufficiently on intermediate representations that preserve human intent and support rea...
  </details>

- **2026-07-30** — Michael Cai — [Explaining the Macroeconomic Inertia Puzzle](http://arxiv.org/abs/2607.27548v1)
  <details><summary>📄 Abstract</summary>
  Benchmark macroeconomic models require additional frictions to explain the sluggish response of aggregate variables to sudden shocks or changes in policy. I show that standard heterogeneous agent (HA) models, the Blanchard (1985) perpetual youth and Bewley (1986) incomplete markets models, are consistent with aggregate consumption inertia without the use of habit preferences or any specific model of expectation underreaction to dampen the responsiveness of consumption savings decisions. I instea...
  </details>

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


### 📂 other
*其他安全相关 / Other Security-Related* — 152 papers

- **2026-07-30** — Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe — [One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence](http://arxiv.org/abs/2607.28317v1)
  <details><summary>📄 Abstract</summary>
  A single human must audit $N$ LLM agents under a budget of $B \ll N$ audits per round, guided by self-reported confidence that may be adversarially miscalibrated and by correlated errors. We model this as budgeted noisy inspection over a two-level Gaussian copula and locate the miscalibration threshold $δ^*$ past which confidence-ranked auditing is \emph{worse} than random. Two a-priori expectations reverse: $δ^*$ \emph{rises} as the budget shrinks, and cross-family correlation is not low---shar...
  </details>

- **2026-07-30** — Niklas Bauer, Lars Benedikt Kaesberg, Akiko Aizawa et al. — [Can Agents Deceive? Evaluating Reasoning and Deception in ParliamentBench using a Social Deduction Game](http://arxiv.org/abs/2607.28146v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed as agents in high-stakes settings, such as medical and legal systems, understanding their deceptive capabilities is fundamental to safety. Controlled social deduction games provide a reproducible proxy for isolating and evaluating these complex adversarial behaviors. We present the open-source benchmark framework ParliamentBench based on the game Secret Hitler to evaluate LLMs in scenarios that require deception, persuasion, and reasoning under inform...
  </details>

- **2026-07-30** — Muhammad Laiq — [A comparative analysis of automated techniques for security bug report identification](http://arxiv.org/abs/2607.27893v1)
  <details><summary>📄 Abstract</summary>
  Timely identification of security-related bug reports is essential to minimize the window of vulnerabilities in software systems. Manually screening incoming bug reports to identify security-related issues is time-consuming, error-prone, and non-scalable for large-scale software systems. Thus, a variety of automatic techniques, including traditional machine learning (ML) techniques and large language models, have been proposed to facilitate this task. However, the literature remains fragmented. ...
  </details>

- **2026-07-30** — Vishwajith Ramesh — [Subtract or Replay? Exact Deletion from Language-Model Memory](http://arxiv.org/abs/2607.27539v1)
  <details><summary>📄 Abstract</summary>
  Exact deletion from persistent language-model memory depends on how that memory represents a record. Addressable influence can be removed by algebraic decrement; influence transformed by later writes inside shared recurrent state requires rebuilding from before the write. We test this distinction in two pretrained models against explicit record-omitted references. First, we replace Gemma 3's global-attention layers with support-vector memory. After low-rank recovery at 1B, decrement and retained...
  </details>

- **2026-07-30** — Yukang Cao, Haozhe Xie, Beichen Wen et al. — [ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](http://arxiv.org/abs/2607.28625v1)
  <details><summary>📄 Abstract</summary>
  Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environme...
  </details>

- **2026-07-30** — Haomin Qi, Xingliang Wang, Xuanqi Gao et al. — [Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments](http://arxiv.org/abs/2607.28591v1)
  <details><summary>📄 Abstract</summary>
  Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. To expand this supply, we present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository. It aligns historical evidence with evolved code, reconstructs ta...
  </details>

- **2026-07-30** — Jiawei Xu, Minghui Liu, Juzheng Zhang et al. — [$β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation](http://arxiv.org/abs/2607.28582v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) is a promising approach to improve reasoning language models, but it remains brittle in practice: making it work reliably often requires substantial engineering effort. We identify a structural source of this difficulty: vanilla OPSD is precisely the $β=1$ member of a broader policy-optimization family, where $β$ weights the KL penalty anchoring the student to a reference policy. This equivalence turns $β$ from an implicit value fixed at one into a controllable...
  </details>

- **2026-07-30** — Junlin Yang, Che Jiang, Yu Fu et al. — [Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](http://arxiv.org/abs/2607.28568v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) requires AI systems that improve the process of building AI (i.e., AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed for studying this capability. We introduce OpenMLE, an open full-stack system for RSI research in MLE, spanning verifiable task environments with execution feedback (OpenMLE-Gym), operator learning (OpenMLE-RL), and long-horizon search (OpenMLE-Evo). On this stack we post-train Frontis-MA1 (35B) as a meta-evolution ag...
  </details>

- **2026-07-30** — Xiaobei Zhao, Xingqi Lyu, Xin Chen et al. — [TEA-AgriVLN: Traversability Estimation Alarm for Agricultural Vision-and-Language Navigation](http://arxiv.org/abs/2607.28474v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires an agent to follow a natural language instruction, predicting a sequence of low-level actions to navigate a robot from a starting point to a target location. The A2A benchmark and the AgriVLN method pioneeringly extended VLN-CE from indoor scenes to agricultural scenes, while we observed a challenging distinction: In indoor scenes, whether a zone is traversable tends to be clear to classify, such as wood floors are trave...
  </details>

- **2026-07-30** — Zheng Wu, Yibo Luo, Pu Zhang et al. — [Beyond a Single Judge: Simulating Social Persona Panels for Generative UI Evaluation](http://arxiv.org/abs/2607.28439v1)
  <details><summary>📄 Abstract</summary>
  Generative UI (GenUI) lets large language models synthesize a complete, renderable interface directly from a natural-language instruction, but evaluating the quality of what they generate remains an open problem. Human evaluation is costly and rater-variant, while LLM-as-a-judge is scalable but reflects only a single implicit viewpoint, unable to capture how different populations of real users actually perceive the same interface. We propose the Evidence-Grounded, Social-Weighted Persona Panel (...
  </details>

- **2026-07-30** — Ankur Naskar, Vaneet Aggarwal — [Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs](http://arxiv.org/abs/2607.28390v1)
  <details><summary>📄 Abstract</summary>
  Constrained Markov Decision Processes (CMDPs) provide a natural framework for reinforcement learning in safety-critical applications, where agents maximize long-term reward while satisfying long-term constraints. Although primal-dual actor-critic methods with linear critics are well understood, extending order-optimal convergence guarantees to neural critics in average-reward CMDPs has remained open. The main challenge is a fundamental bias-cost trade-off in neural critic estimation: under Neura...
  </details>

- **2026-07-30** — Zixuan Jiang, Binghao Qiang, Jiaying Chi et al. — [AgenticASR: Refining Speech Recognition in Real-World Scenarios via an Agentic Approach](http://arxiv.org/abs/2607.28175v1)
  <details><summary>📄 Abstract</summary>
  Automatic speech recognition (ASR) has achieved substantial gains in transcription accuracy, yet verbatim transcription does not necessarily produce readily usable text. It retains fillers, repetitions, false starts, and self-corrections that increase reading effort, obscure the speaker's final intent, and propagate unresolved or abandoned content to downstream tasks. Existing spoken-to-written methods process completed audio or transcripts but cannot revise emitted text when later speech change...
  </details>

- **2026-07-30** — Hail Song, Seokhwan Yang, Jiwon Yang et al. — [S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image](http://arxiv.org/abs/2607.28164v1)
  <details><summary>📄 Abstract</summary>
  We propose S-Avatar, a novel method for generating photorealistic 3D head avatars from a single image using a diffusion-guided 3D model generation module and strategies for animating 3D Gaussian Splatting (3DGS). While single-image head avatar reconstruction is crucial for lifelike Virtual Reality (VR) applications, existing approaches often struggle to preserve 3D consistency under unseen viewpoints. S-Avatar addresses this limitation through a three-stage pipeline. First, a high-resolution 3DG...
  </details>

- **2026-07-30** — Giorgos Iacovides, Wuyang Zhou, Danilo Mandic — [FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning](http://arxiv.org/abs/2607.28127v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs). However, existing approaches remain confined to a market-agnostic, supervised learning paradigm that relies on limited, static and human-annotated datasets, and thus are incapable of adapting to evolving market conditions. To address this limitation, we introduce FinSMART, the first market-aligned reinforcement learning framework for financial sen...
  </details>

- **2026-07-30** — Jiawen Tao, Miao Peng, Yaoming Li et al. — [Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training](http://arxiv.org/abs/2607.28109v1)
  <details><summary>📄 Abstract</summary>
  Synthetic textbook data has improved language model pre-training, but prior work largely treats the benefit as a property of generated content or local rewriting style. We study a different factor: whether related content is organized into coherent book-level documents. We contribute both a scalable synthesis pipeline and controlled evidence that this organization matters. The pipeline retrieves source material from a pre-training corpus, clusters it into topical units, plans hierarchical tables...
  </details>

- **2026-07-30** — Binbin Zheng, Zijun Xie, Guanqun Zhao et al. — [Group-Reflective Self-Distillation for Agentic Reinforcement Learning](http://arxiv.org/abs/2607.28076v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) is effective for training large language model agents. However, terminal rewards provide only coarse trajectory-level supervision, leaving successful behaviors, recurring mistakes, and incidental choices entangled in the same outcome signal. Existing agentic self-distillation methods enrich sparse supervision with natural-language skills, but skills retrieved externally or extracted from a single trajectory by stronger models may mismatch cur...
  </details>

- **2026-07-30** — Jesús Gacías Franco — [The Euler Characteristic Transform from a Convex Geometric Perspective](http://arxiv.org/abs/2607.28021v1)
  <details><summary>📄 Abstract</summary>
  By examining the relationship between the support function of convex geometry and the Euler Characteristic Transform (ECT) of topological data analysis, we develop new tools and suggest variations on some common ECT pipelines. Specifically, we put forward new definitions of ECT-induced pseudodistances, which have the advantage of being invariant under common euclidean isometries and require no cutoff parameter to compare shapes with distinct Euler characteristic. These definitions rely on a gene...
  </details>

- **2026-07-30** — Xu Xia, Jinghua Piao, Min Yang et al. — [From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents](http://arxiv.org/abs/2607.27937v1)
  <details><summary>📄 Abstract</summary>
  Recent work on LLM agents is shifting from external capability elicitation to capability internalization, enabling agents to retain useful skills without retrieval at inference time. On-policy self-distillation (OPSD) offers a promising direction, but many existing methods typically supervise students by scoring actions along student-generated trajectories. Such supervision has two limitations: teacher preferences are not validated by environment outcomes, and action-level scores underuse inform...
  </details>

- **2026-07-30** — Qiangqiang He, Zhongheng Wu, ZiJian Wang — [Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning](http://arxiv.org/abs/2607.27888v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) is central to improving long-CoT reasoning in large language models. Critic-free methods such as GRPO convert response-level rewards into advantages and uniformly broadcast them across tokens, overlooking their unequal contributions to the final outcome. On-policy self-distillation (OPSD) instead provides dense distributional supervision by minimizing the forward KL divergence between an unprivileged policy and a privileged self-teacher, impl...
  </details>

- **2026-07-30** — Lanhao Zhao — [On the Strong Structural Controllability of Matrix-Weighted Networks](http://arxiv.org/abs/2607.27852v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the strong structural controllability of multi-agent networks. Based on the definition of equitable partitions, an upper bound for the strong structural controllable subspace (SSCS) is established. To reflect the physical significance of matrix weights where the state dimension is greater than one, the multi-agent system is modeled using higher-order dynamics. Furthermore, to address matrix singularity and asymmetric couplings, a matrix space basis decomposition method is...
  </details>

- **2026-07-30** — Yuhang Zhu, Mingxuan Du, Benfeng Xu et al. — [Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive Role-Playing Evaluation](http://arxiv.org/abs/2607.27816v1)
  <details><summary>📄 Abstract</summary>
  Role-playing agents (RPAs) have become one of the most important consumer applications of large language models. Users engage in multi-turn conversations with RPAs for experiences such as emotional comfort, making reliable evaluation essential for measuring capability, comparing systems, and guiding further improvement. Existing benchmarks, however, typically require an RPA to continue a fixed dialogue history and then evaluate the continuation using a fixed rubric detached from the user. We ide...
  </details>

- **2026-07-30** — Wei Chen, Junkai Li, Tongguan Wang et al. — [Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis](http://arxiv.org/abs/2607.27790v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Sentiment Analysis (MSA) aims to interpret complex human emotions by integrating natural language with non-verbal modalities. Non-verbal modalities share a structural isomorphism with natural language, as both can be viewed as feature sequences evolving over time. This isomorphism enables the transformation of non-verbal modalities into text-like tokens for unified semantic reasoning. Large Language Models (LLMs), designed to understand and generate sequential data, can thus be utiliz...
  </details>

- **2026-07-30** — Xiao Tan, Cynthia Sturton — [CHARGE: Leveraging CWE Hierarchies for Hardware Security SystemVerilog Assertion Generation](http://arxiv.org/abs/2607.27776v1)
  <details><summary>📄 Abstract</summary>
  This paper presents CHARGE, an automated framework for generating security properties for unverified RTL modules using CWEs and large language models (LLMs). The hallmark is a reasoning process that leverages the hierarchical nature of CWE entries to improve accuracy when identifying security-critical assets in unverified RTL modules. As a result, the approach can infer expected security behaviors and generate properties from identified assets and CWE semantics, avoiding the need for trusted des...
  </details>

- **2026-07-30** — Argyrios Deligkas, Michail Fasoulakis, Stavros D. Ioannidis et al. — [Delegated Fair Division](http://arxiv.org/abs/2607.27743v1)
  <details><summary>📄 Abstract</summary>
  Motivated by recently introduced problems on delegated resource allocation, we study a model of fair division, where a set of indivisible goods is to be allocated to some agents, each of which belonging to some bigger central entity. Our model captures the general framework of allocating resources to organizational units, which subsequently distribute them to their affiliated members. A particularly relevant application of this framework, with immense social impact, arises in the allocation of f...
  </details>

- **2026-07-30** — Sangmin Hong, Daniel Sungho Jung, Heewon Kim et al. — [PrintAnything: Learning an Intermediate Representation for 3D printing G-code Generation](http://arxiv.org/abs/2607.27729v1)
  <details><summary>📄 Abstract</summary>
  Point clouds are one of the most fundamental and widely used 3D representations, serving as the most basic geometric representation of 3D shapes. Nevertheless, most existing 3D printing pipelines require a watertight mesh as input, preventing the direct use of point clouds for fabrication. A common workaround is to reconstruct meshes from point clouds; however, the resulting meshes often contain geometric artifacts, such as incorrect faces or topological inconsistencies, that are difficult to re...
  </details>

- **2026-07-30** — Angshuman Chakravertty, Rahul Maheshwari — [VESTIGE: A Knowledge-Guided Masking Strategy for Corruption-Aware Fine-Tuning of Genomic Transformers, Validated on Ancient DNA Reconstruction](http://arxiv.org/abs/2607.27712v1)
  <details><summary>📄 Abstract</summary>
  Standard masked-language-model fine-tuning applies a uniform masking probability across every token position, assuming reconstruction difficulty is position-agnostic. When the degradation process is characterised and concentrated at predictable positions, this assumption fails: at peak damage sites the model can underperform a frequency-matched random predictor. We introduce VESTIGE, a parameter-free, drop-in replacement for the standard MLM collator that aligns the masking distribution with an ...
  </details>

- **2026-07-30** — Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou et al. — [RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation](http://arxiv.org/abs/2607.27699v1)
  <details><summary>📄 Abstract</summary>
  We propose RefineSVG, a single-step closed-loop visual feedback framework that enables multimodal large language models (MLLMs) to perform high-fidelity image-to-SVG generation through self-correction. Existing MLLM-based approaches rely on single-pass open-loop inference, where the model receives visual input only once and must generate thousands of SVG code tokens without intermediate verification. This paradigm inevitably leads to geometric drift, error accumulation, and visual hallucination ...
  </details>

- **2026-07-30** — Sangjin Kim, Yuseon Choi, Byeongcheol Kim et al. — [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](http://arxiv.org/abs/2607.27694v1)
  <details><summary>📄 Abstract</summary>
  Low-bit quantization is essential for efficient LLM inference, and both rotation and fine-grained group quantization have shown individual promise. However, their combination often leads to accuracy degradation or hardware overhead due to a mismatch between the global nature of rotation and the localized behavior of group scaling. We propose GyRot, a quantization framework and hardware accelerator that bridges this gap through algorithm-hardware co-design. GyRot introduces Coarse Rotation, Fine ...
  </details>

- **2026-07-30** — Jingya Wang, Yuyang Gao, Liuzhenghao Lv et al. — [LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents](http://arxiv.org/abs/2607.27690v1)
  <details><summary>📄 Abstract</summary>
  We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience. LabEvolver couples a state-grounded inner trial loop for adaptive perception, online planning, and safety validation with an outer evolution loop that distills completed trajectories into reusable skill, strategy, and safety experience. On robotic solution-preparation tasks, LabEvolver demonstrates real-world feasibility, reducing pH-regulation completio...
  </details>

- **2026-07-30** — Bowen Shen — [Can Large Language Models Resolve Real Java Merge Conflicts? An Evaluation with a Calibrated LLM-as-Judge](http://arxiv.org/abs/2607.27674v1)
  <details><summary>📄 Abstract</summary>
  Merge conflicts are a recurring cost of collaborative software development, and the traditional structured and semi-structured merge tools that address them frequently abstain: when their heuristics do not apply, they leave the conflict unresolved. Large language models (LLMs) can instead produce a candidate resolution for almost any conflict, but measuring whether those resolutions are actually good at scale is hard, because obtaining human desirability judgments for every model output does not...
  </details>

- **2026-07-30** — SiYuan Ma, Yiqin Luo,  Zhangji et al. — [Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures](http://arxiv.org/abs/2607.27617v1)
  <details><summary>📄 Abstract</summary>
  Identical language-model answers can arise from hidden states that support different future computations, so current-answer probes do not establish a reusable internal interface. We introduce forked futures: future operations are sampled only after a prefix state has formed, and states are compared through the response distributions induced by those operations. This yields an empirical causal quotient over hidden states without requiring researcher-specified latent labels. Shared, Local, Mixture...
  </details>

- **2026-07-30** — Sandeco Macedo — [What makes prompts a graph: necessary and sufficient conditions for prompt graph engineering](http://arxiv.org/abs/2607.27578v1)
  <details><summary>📄 Abstract</summary>
  Prompts stopped being isolated strings some time ago. In real systems, one model call feeds another, retrieval interleaves with generation, routers branch, and aggregators merge parallel results. Practice converged on a single structure to hold this together: the graph. Frameworks such as LangGraph, DSPy, and Prompt Flow expose it openly, and research systems already optimize it automatically. The vocabulary, however, lags behind. Graph names, variously, a reasoning topology inside one sampling ...
  </details>

- **2026-07-30** — Lifeng Zhuo, Wendi Chen, Han Xue et al. — [FA-RDP: A Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation](http://arxiv.org/abs/2607.28596v1)
  <details><summary>📄 Abstract</summary>
  In contact-rich manipulation, action multimodality and reactivity dominate different stages of a single episode. Before contact, multiple trajectories might be equally valid, making it important to preserve diverse action modes. After contact, geometric constraints and force limits narrow the solution space, while successful execution demands rapid responses to force feedback. However, standard diffusion policies use a fixed inference frequency and sampling steps throughout the episode, forcing ...
  </details>

- **2026-07-30** — Qixun Wang, Yang Shi, Letian Cheng et al. — [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](http://arxiv.org/abs/2607.28595v1)
  <details><summary>📄 Abstract</summary>
  The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet inefficient reasoning paradigm. In this work, we rethink agentic visual reasoning through two key dimensions of tool use: Mode Adaptiveness (MA) and Tool Effect (TE). Mode Adaptiveness characterizes whether an MLLM can recognize when tools are truly necessary and invoke them accordingly, thereby av...
  </details>

- **2026-07-30** — Luigi Sigillo, Matteo Silvestri, Francesco Tabaro et al. — [EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents](http://arxiv.org/abs/2607.28229v1)
  <details><summary>📄 Abstract</summary>
  The web is increasingly accessed by AI agents rather than humans. Every agent needs knowledge, especially in the life-sciences, where agentic pipelines are growing fast. Access to the literature is a crucial part of that need, and resources such as Europe PMC, with over 40M indexed records, are widely used to meet it. Yet these resources were not built for AI agents: they take keywords and complex syntax and return whole papers, so every agent must learn the syntax, issue several searches, and r...
  </details>

- **2026-07-30** — Patricio F. Calatayud, Pablo Padilla Longoria, Álvaro Martínez Ramírez — [A Mathematical Framework for Reading the Autopsias' Meta - Compositional System](http://arxiv.org/abs/2607.28155v1)
  <details><summary>📄 Abstract</summary>
  Background. New forms of music writing using computers have arisen in the past 20 years. Most of them use the capacities of digital manipulation of data like animation, algorithmic processing, cinematic view, and much more. These scores use dynamic musicography, and all of them share a problem. They have readability problems. We will argue that this problem can be addressed by mathematical tools. Aims. Take the Autopsias [Autopsies] meta-compositional system as a study case for starting the cons...
  </details>

- **2026-07-30** — Jonas Mensing, Wilfred G. van der Wiel, Andreas Heuer — [Nanoparticle Networks for Neuromorphic Computing](http://arxiv.org/abs/2607.27844v1)
  <details><summary>📄 Abstract</summary>
  Physical computing leverages complex dynamical systems for energy-efficient data processing. In this work, we present a neuromorphic architecture based on metallic nanoparticles interconnected by molecular junctions on a $\text{SiO}_2$/Si substrate. We demonstrate that surrounding static control electrodes transform this nanoparticle network from a passive reservoir into a tunable nonlinear dynamical system. By analyzing how these electrodes route simple one-dimensional voltage inputs into multi...
  </details>

- **2026-07-30** — Sotiris Kanellopoulos — [Finite Pinwheel Covering](http://arxiv.org/abs/2607.28574v1)
  <details><summary>📄 Abstract</summary>
  In perpetual scheduling theory, the Pinwheel Covering problem asks, given $n$ frequencies $f_i$, whether there exists an infinite schedule such that every $f_i$ consecutive entries contain at most one occurrence of $i\in [n]$. This models $n$ agents taking turns at executing a job, with a recovery period before working again. Pinwheel Covering is, in a sense, the dual of Pinwheel Packing (also known as Pinwheel Scheduling), which similarly asks for at least one occurrence of $i$ in every $f_i$ c...
  </details>

- **2026-07-30** — Ruman Wang, Hangting Ye — [ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature Programs](http://arxiv.org/abs/2607.28538v1)
  <details><summary>📄 Abstract</summary>
  Classifying pathological scars from clinical photographs requires distinguishing keloids from hypertrophic scars despite limited expert-labeled data and substantial acquisition variation across hospitals. End-to-end image models remain data-dependent, whereas sending photographs to a hosted vision-language model (VLM) may conflict with local data-governance requirements and yields decisions that are difficult to reproduce and audit. We introduce ScaFE (Scar Feature Engineering), which transfers ...
  </details>

- **2026-07-30** — Frederico Falconi Costa, Salvador Cesar Costa, Fabricio F. Costa — [AIx4Soccer: A Unified Platform Architecture for Football Club Management and Structured Athlete Development](http://arxiv.org/abs/2607.28531v1)
  <details><summary>📄 Abstract</summary>
  Football clubs, academies, and federations operate a growing but fragmented portfolio of digital tools: separate systems for video analysis, GPS/performance tracking, medical records, scouting, and administration. This fragmentation is most acute outside the elite European clubs that can afford integration, producing a digital divide that disadvantages grassroots clubs in developing markets such as Brazil, paradoxically the world's largest exporter of professional players. This paper presents, a...
  </details>

- **2026-07-30** — Yuto Suzuki, Farnoush Banaei-Kashani — [TCA-SIR: Learning Target-Conditioned Abstractions for Scientific Inspiration Retrieval](http://arxiv.org/abs/2607.28498v1)
  <details><summary>📄 Abstract</summary>
  Scientific hypothesis generation for AI for Science typically involves Scientific Inspiration Retrieval (SIR) followed by hypothesis composition. Existing SIR methods rank papers by topical similarity and do not explicitly represent how a candidate inspiration transfers to a target problem. This is especially limiting for remote inspirations, whose value often lies in reusable problem-solving principles rather than topical overlap. Motivated by how humans abstract transferable aspects of a sourc...
  </details>

- **2026-07-30** — Katy L. Scott, Sejin Kim, Joshua Siraj et al. — [Negative controls reveal volume-driven confounding in radiomics and imaging foundation model features](http://arxiv.org/abs/2607.28423v1)
  <details><summary>📄 Abstract</summary>
  Radiomics and imaging foundation models promise non-invasive biomarkers of tumour biology, yet predictive signatures may reflect tumour volume or acquisition artifacts rather than meaningful image structure. We introduce READII-2-ROQC, an open-source framework that uses volume-preserving negative controls to assess whether radiomic and deep imaging features capture independent spatial signals. READII-2-ROQC generates voxel-perturbed images across tumour, background and whole-image regions using ...
  </details>

- **2026-07-30** — Imad Aouali — [On-Policy and Off-Policy Learning for Large Action Spaces](http://arxiv.org/abs/2607.28408v1)
  <details><summary>📄 Abstract</summary>
  This thesis studies policy learning in interactive systems where an agent observes a context, selects an action from a very large set, and receives partial feedback. The main framework is contextual bandits, with two paradigms: on-policy learning, where the agent interacts sequentially with the environment and minimizes regret, and off-policy learning, where it learns from logged data collected by a logging policy. In large action spaces, both settings face major challenges: inefficient explorat...
  </details>

- **2026-07-30** — Tairan Wang, Liang Zhou, Zikang Zhan et al. — [When Specifications Conflict: A Symmetry-Based Framework for Measuring LLM Preferences](http://arxiv.org/abs/2607.28384v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly required to integrate multiple sources of information that may be inconsistent or conflicting. However, there is still a lack of controllable and attributable methods for analyzing how models resolve conflicts between competing specifications. We propose a controlled experimental framework for studying model preferences under conflicting specifications. By constructing specifications with explicit conflicts, the framework enables model choices betwee...
  </details>

- **2026-07-30** — Mark Bognanni, Doug Hanley, Daniel Kolliner et al. — [Economics and Epidemics: Evidence from an Estimated Spatial Econ-SIR Model](http://arxiv.org/abs/2607.28348v1)
  <details><summary>📄 Abstract</summary>
  Economic analysis of effective policies for managing epidemics requires an integrated economic and epidemiological approach. We develop and estimate a spatial, micro-founded model of the joint evolution of economic variables and the spread of an epidemic. We empirically discipline the model using new U.S. county-level data on health, mobility, employment outcomes, and non-pharmaceutical interventions (NPIs) at a daily frequency. Absent policy or medical interventions, the model predicts an initi...
  </details>

- **2026-07-30** — Pere Martra, Eugenio Martínez Cámara, Alfonso Ureña López — [Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations](http://arxiv.org/abs/2607.28319v1)
  <details><summary>📄 Abstract</summary>
  This work presents Fairness Pruning, a lightweight structural intervention method designed for the management and future mitigation of demographic bias in large language models (LLMs). As a foundational empirical validation of this method, this work focuses on causal bias localization. Using minimally contrastive prompt pairs and inference-time activation capture, the method identifies neurons that react differentially when processing demographic attributes in GLU architectures, evaluating the s...
  </details>

- **2026-07-30** — Huiyuan Tian, Bonan Xu, Shijian Li — [Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing](http://arxiv.org/abs/2607.28308v1)
  <details><summary>📄 Abstract</summary>
  Sparse mixture-of-experts (MoE) language models route each token to multiple experts, suggesting a geometric account of their benefit: co-selected experts should contribute distinct representation directions. Existing evidence often conflates route coherence, candidate quality, and candidate-by-context interaction. We distinguish these quantities using an Expert Subspace Separation Index (ESSI), matched-route residuals, and a prefix-controlled $2\times2$ factorial; frozen-route interventions and...
  </details>

- **2026-07-30** — Jens Lehmann, Andrei Aioanei, Sahar Vahdati — [Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3](http://arxiv.org/abs/2607.28287v1)
  <details><summary>📄 Abstract</summary>
  ARC-AGI-3 turns abstraction into an interactive problem of skill acquisition. A player must infer an unfamiliar game's rules, hidden state, and goal while maintaining action efficiency because every move counts. We formalize these environments as parameterized rendered deterministic Moore machines and introduce Tycho, a coding-agent system that constructs and uses game-specific models during interaction. Tycho separates actionable observations from intermediate animation, level-completion, and g...
  </details>

- **2026-07-30** — Bertil Braun, Martin Forell — [(Towards) Scalable Reliable Automated Evaluation with Large Language Models](http://arxiv.org/abs/2607.28282v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the quality and relevance of textual outputs from Large Language Models (LLMs) remains challenging and resource-intensive. Existing automated metrics often fail to capture the complexity and variability inherent in LLM-generated outputs. Moreover, these metrics typically rely on explicit reference standards, limiting their use mostly to domains with objective benchmarks. This work introduces a novel evaluation framework designed to approximate expert-level assessments of LLM-generated...
  </details>

- **2026-07-30** — Zhaohua Lu, Cheng Zheng, Yuanyuan Han — [Bridging Probabilistic LLMs and Deterministic Statistical Validation: The PROVE Multi-Agent Framework for Clinical Trial Reporting](http://arxiv.org/abs/2607.28218v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the accuracy and consistency of clinical trial Tables, Figures, and Listings (TFLs) remains a major challenge in regulatory reporting. Independent programming and manual review are essential quality-control practices, but cross-output verification still depends heavily on reviewer inspection and may miss structural, logical, or arithmetic discrepancies. Large language models (LLMs) can help interpret varied table language and navigate lengthy study documents, but they are not reliable s...
  </details>

- **2026-07-30** — Markus S. Feser, Paul L. Tschisgale — [AI-based scoring systematically underestimates conceptual understanding of linguistically weak students' explanations in physics](http://arxiv.org/abs/2607.28210v1)
  <details><summary>📄 Abstract</summary>
  Explaining physical phenomena is central to physics learning, because students' explanations provide evidence of their conceptual understanding. Because conceptual understanding can only be inferred through language rather than observed directly, distinguishing conceptual understanding from linguistic quality represents a fundamental challenge for assessment. In this study, we examined whether AI-based scoring approaches can assess students' conceptual understanding independently of the linguist...
  </details>

- **2026-07-30** — Xavier Marjou, Lucas Tamic, Ilan Jaffeux-Cheniout — [PCAP-LM: An LLM-Native Text Representation for TLS Bulk Traffic Analysis](http://arxiv.org/abs/2607.28100v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer powerful reasoning capabilities for network traffic analysis, but standard capture formats and their textual equivalents are prohibitively verbose, overflowing LLM context windows by two orders of magnitude. We present PCAP-LM, a flow-centric, LLM-native text representation that acts as a lossy knowledge extraction step rather than a standard compression tool: raw captures are transcoded into semantic summaries using PacketGlyphs - a novel ASCII alphabet coined...
  </details>

- **2026-07-30** — Chen Xing, Xin Cheng, Guillaume Aulanier et al. — [Back Reaction of the Untwisting Solar Corona Scars Sunspots](http://arxiv.org/abs/2607.28089v1)
  <details><summary>📄 Abstract</summary>
  The evolution of magnetic fields in the tenuous solar corona is predominantly governed by the motions of the underlying dense photosphere. Despite, coronal magnetic restructuring driven by magnetic reconnection between interacting coronal fields can sometimes react backwards to change photospheric magnetic fields. However, the mechanism of reactions remains undetermined. Here, we report the discovery of a back-reaction phenomenon: the untwisting of coronal loops that become twisted during reconn...
  </details>

- **2026-07-30** — Xingjian Wu, Junlin Liu, Xingchen Liu et al. — [Contrastive Reinforced Policy Optimization via Privileged Self-Distillation](http://arxiv.org/abs/2607.28026v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in post-training Large Language Models (LLMs) increasingly rely on Reinforcement Learning with Verifiable Rewards (RLVR) or On-Policy Self-Distillation (OPSD). While OPSD provides dense, logit-level supervision, it inherently suffers from exposure bias due to the privileged information of the self-teacher. In multi-turn agentic settings, this leads to reasoning route convergence and the loss of clear optimization directions. To tackle these challenges, we introduce Contrastive Re...
  </details>

- **2026-07-30** — Bastian Perner, Pratik Gajanan Raut, Maximilian Lübke et al. — [Multi-Agent Reinforcement Learning for Base Station Placement in TDOA-Based Localization](http://arxiv.org/abs/2607.28002v1)
  <details><summary>📄 Abstract</summary>
  Accurate localization of devices is a key capability for emerging 5G and 6G networks and depends on effective base station (BS) placement. Conventional geometry-based approaches such as Geometric Dilution of Precision (GDOP) ignore realistic propagation effects such as Non-Line of Sight (NLOS) shadowing and multipath-induced Time of Arrival (TOA) bias caused by buildings. This paper proposes a ray-tracing-assisted Multi-Agent Reinforcement Learning (MARL) framework for environment-aware BS place...
  </details>

- **2026-07-30** — Weining Zhang — [Share the Judge, Learn the Deferral: Where Specialization Helps LLM Evaluation](http://arxiv.org/abs/2607.27984v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems have widened the gap between producing candidate outputs and reviewing them. This paper asks a practical architectural question: should domain specialization be built into an evaluator's weights, or into the rule that decides when its judgment can be trusted? We study 99,952 public, rubric-conditioned examples. Supplying the correct rubric improves locked-test accuracy by 2.11 points over a response-only control; replacing it with an unrelated rubric costs 2.66 points. Dividing t...
  </details>

- **2026-07-30** — Srijoni Majumdar, Chuhao Qin, Evangelos Pournaras — [Argonaut: Interactive Visual Exploration for Distributed Optimization](http://arxiv.org/abs/2607.27946v1)
  <details><summary>📄 Abstract</summary>
  Distributed discrete-choice optimization in decentralized settings is often hard to explore and navigate: disentangling what other agents choose, how their choices are interdependent, and how they collectively reach a global objective quickly becomes intractable as the system scales. The major limitation is observability of the search process. Existing methods are largely centralized and offer limited support, visualizing only the final solution or providing algorithm backends over a fixed datas...
  </details>

- **2026-07-30** — Xiang Yuan, Kaiqing Lei, Zhenyu Jin et al. — [Harnessing the Potential of Optimizing Data Mixtures via Bayesian Domain Reweighting](http://arxiv.org/abs/2607.27928v1)
  <details><summary>📄 Abstract</summary>
  The performance of Large Language Models (LLMs) is fundamentally influenced by the distributional composition of multi-domain pre-training data. While manual heuristics were prevalent in early models, they increasingly fail to capture the intricate synergies between domains as data complexity grows. To overcome the issue, a dominant approach seeks to fit a proxy function mapping between domain weights and their corresponding validation losses, and then find the optimal domain weights to minimize...
  </details>

- **2026-07-30** — Jinpeng Hu, Erqiang Wang, Shan Wang et al. — [MMHBench: A Multi-Perspective Benchmark for Mental Health Understanding in Long-Form Videos](http://arxiv.org/abs/2607.27895v1)
  <details><summary>📄 Abstract</summary>
  Mental health understanding in long-form videos requires nuanced reasoning over observable behavior, interpersonal context, and latent psychological states. Existing benchmarks largely reduce this task to coarse-grained classification, providing limited insight into whether models truly understand psychological phenomena or rely on superficial correlations. To address this limitation, we introduce MMHBench, a comprehensive multimodal benchmark for multi-perspective mental health understanding, c...
  </details>

- **2026-07-30** — Stef Cuyckens, Mihaela Jivanescu, Jun Yin et al. — [ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents](http://arxiv.org/abs/2607.27879v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents optimize the power, performance, and area (PPA) of register-transfer-level (RTL) designs by iterating over edits, synthesis, and PPA analysis, paying a dollar cost for every LLM call. Prior agents report the quality reached without its normalized cost, attribute that quality to an engineered cross-design memory, and hold the reasoning effort of every call fixed. We propose Ares with three corresponding innovations. (1) We introduce a normalized dollar cost per L...
  </details>

- **2026-07-30** — Youke Xu, Zeyang Liao, Xue-hua Wang — [Beating the Bad-Cavity Limit via Auxiliary-Emitter Linewidth Squeezing](http://arxiv.org/abs/2607.27878v1)
  <details><summary>📄 Abstract</summary>
  Strong coupling in cavity QED is conventionally achieved at the expense of either high cavity quality factors or ultrasmall mode volumes, a trade-off that fundamentally constrains practical implementations. Here, we circumvent this limitation by introducing two nonidentical auxiliary emitters with opposite detunings into a bad cavity. This hybrid system supports a subradiant mode that significantly squeeze the effective cavity linewidth, creating an ultra-narrow transmission window at the cavity...
  </details>

- **2026-07-30** — Qi Wang, Long-Gang Pang, Shi Pu et al. — [CLVisc Agent for autonomous relativistic hydrodynamics studies](http://arxiv.org/abs/2607.27822v1)
  <details><summary>📄 Abstract</summary>
  We enable large language model (LLM) agents to autonomously perform end-to-end hydrodynamic simulations of the quark-gluon plasma evolution and calculation of final hadron spectra in relativistic heavy-ion collisions. We design a meta skill that allows an agent to explore a project's source code, craft a specialized skill, and iteratively refine it. Applying this meta skill to the (3+1)D viscous hydrodynamic code CLVisc, the agent builds a CLVisc skill encoding its operational knowledge and then...
  </details>

- **2026-07-30** — Weihang Wang, Kainan Tu, Jielei Zhang et al. — [MemeBench: What LVLMs Miss When Interpreting Culture-Dependent Memes](http://arxiv.org/abs/2607.27798v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models have improved at describing visual content, but accurate descriptions do not ensure interpretation when meaning depends on knowledge beyond the pixels. Memes expose this gap because they rely on cultural entities, background knowledge, and community conventions. Most meme benchmarks reduce interpretation to labels or holistic scores, obscuring where an explanation breaks down. We introduce MemeBench, a diagnostic benchmark of 1,253 Chinese and English memes with huma...
  </details>

- **2026-07-30** — Amruta Parulekar, Jinu Lee, Dilek Hakkani-Tür et al. — [Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation](http://arxiv.org/abs/2607.27783v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) explore problems through chain-of-thought, but this exploration is buried in unstructured prose. On high-stakes tasks, users cannot tell which steps are well-supported, which alternatives were seriously considered, or how the final conclusion compares to those the model discarded. We propose a framework that ensembles the reasoning structure, not just the answers, of multiple LLMs by weighted merging of Directed Acyclic Graphs (DAGs) extracted from reasoning chains. ...
  </details>

- **2026-07-30** — Changguo Jia, Tianqi Zhao, Zhiyou Xiao et al. — [VeriSkill: A Self-Evolution Framework for Program Verification Skills](http://arxiv.org/abs/2607.27733v1)
  <details><summary>📄 Abstract</summary>
  Automating program verification with LLM agents requires generating specifications, annotations, auxiliary lemmas, and tool invocations, all of which depend on reusable skills. A natural remedy is skill self-evolution: distilling skills from trajectories and refining them through feedback. However, existing evolution methods struggle with program verification tasks because they cannot reliably identify skill-specific failures or extract actionable signals from opaque verifier feedback. In this p...
  </details>

- **2026-07-30** — Yang Zhou, Zixuan Huang, Sunzhu Li et al. — [SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them](http://arxiv.org/abs/2607.27703v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used in embodied agents to interpret visual inputs, reason about spatial relationships, and make task-level decisions based on that reasoning. However, a fundamental capability mismatch remains: general VLMs can reason about the overall task but often miss the visual details that determine success, while specialist vision models can capture those details but cannot translate them into task-level decisions. In this work, we propose SpatialCLI, a fram...
  </details>

- **2026-07-30** — Yuan Tian, Yi Mei, Mengjie Zhang — [Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge for Dynamic Multi-Mode Project Scheduling](http://arxiv.org/abs/2607.27698v1)
  <details><summary>📄 Abstract</summary>
  In dynamic multi-mode project scheduling, activities have alternative execution modes and uncertain durations, while precedence relations and limited resources constrain their execution. Heuristic priority rules support fast online decisions, but their design requires substantial domain expertise. Genetic programming (GP) hyper-heuristics can automatically evolve such rules. Large language models (LLMs), meanwhile, provide a flexible interface for interpreting scheduling information and explaini...
  </details>

- **2026-07-30** — Oliver Guidetti, Reza Ryan — [From Minds to Models: The Intersection of Psychology and LLM Behaviours](http://arxiv.org/abs/2607.27579v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often compared with the human mind because their decision-making is complex, non-linear and difficult to interpret. Psychological methods developed to investigate unobservable mental processes may therefore help examine LLM behaviour, particularly in government and healthcare. Building on prompt-based adaptations of the Implicit Association Test, this study tested whether ChatGPT produced sentiment differences across racial conditions in open-ended text. Fourteen...
  </details>

- **2026-07-30** — Joshua Caiata, Sreepriya Pulyassary, Xiang Li et al. — [Strategy, Not Payoffs: A Behavioural Embedding of Normal-Form Games](http://arxiv.org/abs/2607.27536v1)
  <details><summary>📄 Abstract</summary>
  Learning a strategic task changes more than what is directly taught: fine-tuning on one game can either enhance or degrade an agent's ability to reason in another. Understanding and predicting this transfer of strategic capabilities, however, remains a key challenge for large language models (LLMs). Normal-form games provide an ideal testbed for analyzing this phenomenon, as they feature explicitly defined payoffs and well-characterized equilibrium behaviours. In this work, we investigate whethe...
  </details>

- **2026-07-29** — Cristian Leo, Anton Dykyi, Danny Cortegaca et al. — [ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping](http://arxiv.org/abs/2607.27528v1)
  <details><summary>📄 Abstract</summary>
  Threat modeling is essential for secure software development, yet manual analysis of cloud-native architectures is slow and demands scarce security expertise. We present ThreatForest, a multi-agent system that generates structured attack trees from source code repositories, maps attack steps to adversary tactics, techniques, and procedures (TTPs) from a pluggable set of frameworks (MITRE ATT&CK, CAPEC, and cloud-specific threat matrices), and synthesizes actionable mitigations. ThreatForest deco...
  </details>

- **2026-07-29** — Pengyu Wang, Benfeng Xu, Shaohan Wang et al. — [BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms](http://arxiv.org/abs/2607.26497v2)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) spans lexical and dense retrieval, graph-based indexing, and agentic search, but these paradigms are usually evaluated on different benchmarks at one corpus size, leaving their accuracy-cost scaling unclear. To bridge this gap, we present a controlled study that varies corpus size along 28 strictly nested tiers spanning roughly 450-fold, while holding questions and a fixed bedrock of relevant and adversarial documents unchanged. Under one reader model and one...
  </details>

- **2026-07-29** — Germans Savcisens, Samantha Dies, Courtney Maynard et al. — [Belief Coevolution in a Social Network of Generalist and Specialist Large Language Models](http://arxiv.org/abs/2607.27512v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in multi-agent environments. However, the processes by which beliefs form and propagate among interacting LLMs remain poorly understood. We introduce CoevolveSim, a framework for studying belief diffusion within networked LLM populations. CoevolveSim allows us to isolate and study three factors: domain specialization, social-role assignment, and social network structure. Within this framework, generalist and specialist LLM agents exchange an...
  </details>

- **2026-07-29** — Emery Cooper, Caspar Oesterheld, Linh Chi Nguyen et al. — [A dataset of rated conceptual arguments](http://arxiv.org/abs/2607.27499v1)
  <details><summary>📄 Abstract</summary>
  Large language models have improved rapidly on tasks with verifiable answers, such as mathematics and programming. Much less is known about their ability to reason about what we call conceptual questions: questions for which no ground truth is realistically accessible and no widely accepted resolution methodology exists, but on which progress can still be made by debating arguments. Most philosophical questions are of this kind, as are central components of questions in AI safety, decision theor...
  </details>

- **2026-07-29** — Maxx Richard Rahman, Asim Ahmed, Mihan Mohagheghzadeh et al. — [MedLLM: An Open Medical Language Model at the Sub-Billion Scale](http://arxiv.org/abs/2607.27490v1)
  <details><summary>📄 Abstract</summary>
  Open medical language models have converged on a single scale: every widely used system runs at 7B parameters or more, leaving the sub-billion regime uncharacterized. We present MedLLM, an open 0.1B-parameter medical language model trained through a fully open three-phase pipeline: general pretraining with curriculum sequence-length scheduling, domain fine-tuning on MedFineWeb, a reference-guided medical corpus we release that is selected from general web data by embedding similarity to medical ...
  </details>

- **2026-07-29** — Yuan Guan, Chandler Squires, Timothy Hu et al. — [Context-Informed Ship Trajectory Prediction via Conditional Attention](http://arxiv.org/abs/2607.27418v1)
  <details><summary>📄 Abstract</summary>
  Long-term ship trajectory prediction is a fundamental capability for maritime safety and autonomous navigation. While recent Transformer-based architectures have improved forecasting horizons, they predominantly rely on historical kinematic states, treating vessel motion as an isolated system. In reality, maritime navigation is profoundly modulated by extrinsic factors like weather and constrained by static vessel characteristics. Existing multimodal approaches fundamentally model the joint dist...
  </details>

- **2026-07-29** — Ignacio García Núñez, Florian Angermeir, Fabiola Moyón Constante — [From Backlog Items to Security Guidance: Towards Continuous Security Compliance](http://arxiv.org/abs/2607.27374v1)
  <details><summary>📄 Abstract</summary>
  Continuous software engineering in regulated domains requires engineering teams to address security throughout the development lifecycle. Yet making security requirements explicit in backlog items is still problematic. Engineers must instead infer security relevance of backlog items from brief, free-form descriptions and often lack timely guidance on applicable requirements. We present an NLP-based backlog enrichment system that detects security-relevant backlog items and links them to relevant ...
  </details>

- **2026-07-29** — Haoyu Chen, Xirui Shi, Yuyao Wang et al. — [PAUSE: A User-Centric Benchmark for Personal AI Assistants in Unified Service Environments](http://arxiv.org/abs/2607.27354v1)
  <details><summary>📄 Abstract</summary>
  Personal AI assistants are increasingly deployed as task-oriented, tool-augmented agents that operate within unified service environments to support everyday user activities. In realistic settings, such assistants must reason over persistent user state, respect user-specific configurations and permissions, and sustain long-horizon, constraint-aware interactions across multiple services. Existing benchmarks, however, often fragment service contexts or abstract away user state, limiting their abil...
  </details>

- **2026-07-29** — Yifan Zhang, Xinkui Zhao, Sai Liu et al. — [FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs](http://arxiv.org/abs/2607.27267v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents autonomously interleave semantic reasoning with complex system operations. In these dynamic environments, static tool-level permissions are fundamentally insufficient; safe authorization is highly context-dependent and heavily reliant on evolving runtime states and data flows. We present FAVA (Formal Authorization for Verified Agents), a permission-carrying authorization framework for agent execution. FAVA utilizes an LLM-guided Permission Intermediate Represent...
  </details>

- **2026-07-29** — Alessio Cascione, Mattia Setzu, Cristiano Landi et al. — [Expanding Data-Agnostic Pivotal Instances Selection Models with Proximity Trees and Ensemble Learning](http://arxiv.org/abs/2607.27522v1)
  <details><summary>📄 Abstract</summary>
  As decision-making processes grow more complex, machine learning tools have become essential for tackling business and societal challenges. However, many existing methods rely on decision-making procedures that are difficult to interpret. Since humans naturally make decisions by comparing new cases with a few representative examples, we aim to design an approach that selects such pivots to construct an interpretable predictive model. Inspired by decision trees, we propose a hierarchical, interpr...
  </details>

- **2026-07-29** — Liangyu Wu, Qibin Liu, Alexander Yue et al. — [A Lightweight Foundation Model for Collider Physics with Multi-Domain Adaptation](http://arxiv.org/abs/2607.27501v1)
  <details><summary>📄 Abstract</summary>
  We present a lightweight approach to foundation modeling (\textbf{NEXUS}) that leverages pre-trained learning from collider physics data towards out-of-domain tasks in other scientific datasets, using a fully connected autoencoder model with approximately 3 million parameters. The model pre-trains with no supervision over a large-scale collision dataset from the Large Hadron Collider modeled by charged particle track features. Downstream tasks for collider analyses, such as kinematic regression ...
  </details>

- **2026-07-29** — Varun Sivashankar — [A Linear Bound on the Rainbow Cycle Number and Approximate EFX](http://arxiv.org/abs/2607.27455v1)
  <details><summary>📄 Abstract</summary>
  It is open whether every fair-division instance with additive valuations admits a complete envy-free-up-to-any-good (EFX) allocation. A well-studied relaxation allows some goods to remain unallocated and asks for $(1-\varepsilon)$-EFX. The rainbow cycle number $R(d)$ was introduced to study this problem: upper bounds on $R(d)$ yield approximate EFX allocations with few unallocated goods. The best previous bound, $R(d)=O(d\log d)$, gives $O_\varepsilon(\sqrt{n\log n})$ unallocated goods. We resol...
  </details>

- **2026-07-29** — Mayank Sharma, Savira Nadela, Tyler Matteson — [Dimensionality and Measurement Precision in HLE's Multiple-Choice Subset](http://arxiv.org/abs/2607.27420v1)
  <details><summary>📄 Abstract</summary>
  Humanity's Last Exam (HLE) is widely used to evaluate frontier language models. HLE organizes its questions into eight subject-domain categories, whose subscores are often interpreted as evidence of distinct capabilities. However, no study has assessed whether these labels correspond to empirically separable latent constructs, nor whether the benchmark effectively differentiates between models of similar ability. We evaluate 29 LLMs on the text-only multiple-choice subset of HLE ($J = 428$ items...
  </details>

- **2026-07-29** — Yixuan Duan, Wei Qiu — [ECG-InterpBench: Benchmarking the Interpretability of ECG Foundation Models with Matched-Scale Sparse Autoencoders](http://arxiv.org/abs/2607.27404v1)
  <details><summary>📄 Abstract</summary>
  Existing benchmarks for electrocardiogram foundation models primarily evaluate downstream predictive performance, providing limited insight into whether their internal representations can be faithfully decomposed, clinically interpreted, or reproduced across independent analyses. We introduce ECG-InterpBench, a benchmark designed to systematically evaluate the interpretability of ECG foundation-model representations. ECG-InterpBench uses sparse autoencoders as standardized measurement instrument...
  </details>

- **2026-07-29** — Jason Pillay, Andriette Bekker, Cristina Tortora et al. — [Handling Missingness and Censoring in Dirichlet Mixture Models](http://arxiv.org/abs/2607.27403v1)
  <details><summary>📄 Abstract</summary>
  Incomplete compositional data analysis faces a fundamental limitation: likelihood-based methods for compositional models generally require fully observed compositions, making it difficult to accommodate missing or censored proportions directly on the simplex. Consequently, analysts often discard partially observed compositions or transform the data into unconstrained spaces, potentially sacrificing interpretability and coherence. This paper proposes a likelihood-based method for incomplete compo...
  </details>

- **2026-07-29** — Xiaohan Li, Xinyu Liu, Chang Liu et al. — [PanDent: Toward Comprehensive Tooth-Level Structure-Language Consistency in Dental Radiology](http://arxiv.org/abs/2607.27378v1)
  <details><summary>📄 Abstract</summary>
  Accurate evaluation of multimodal large language models (MLLMs) in dental panoramic radiography (orthopantomogram, OPG) is limited by the lack of fine-grained, clinically reliable benchmarks that reflect expert interpretation. This work introduces PanDent, a large-scale, clinically grounded OPG benchmark built upon fine-grained, expert-validated tooth-level annotations. The dataset comprises 9,524 high-quality OPGs, each associated with comprehensive structured annotations produced by experience...
  </details>

- **2026-07-29** — Chirag Kalouni, Abhishek Kumar, Manish Kumar Mohanta et al. — [Harnessing Native Chromium Oxidation for Giant Orbital Torque and Field-Free Magnetization Switching in NiFe/Cr Bilayers](http://arxiv.org/abs/2607.27306v1)
  <details><summary>📄 Abstract</summary>
  Orbital currents offer charge-to-spin conversion beyond the efficiency limit of conventional heavy-metal Spin Hall sources. However, harnessing them has so far required either thick orbital-Hall materials or additional heavy-metal conversion layers. Here, we show that the native oxide of chromium, typically regarded as parasitic, transforms a simple NiFe\Cr bilayer into a self-contained dual-channel orbital-current source without the need for any conversion layer. First-principles calculations p...
  </details>

- **2026-07-29** — Stefano Liberati, Valentin Pomakov, Samuele Silveravalle — [Bridging Superfluid and Nonminimally Coupled BEC Dark Matter through RAQUAL](http://arxiv.org/abs/2607.26841v2)
  <details><summary>📄 Abstract</summary>
  Motivated by their common condensed-matter inspiration and their shared aim of reconciling MOND-like phenomenology on galactic scales with particle dark matter on larger scales, we investigate the relation between Superfluid Dark Matter (SFDM) and Bose--Einstein Condensate Dark Matter (BECDM). Since SFDM is formulated in the Newtonian regime whereas BECDM is fully relativistic, we first show that the MONDian formulation of SFDM arises as the Newtonian, low-acceleration limit of a Relativistic AQ...
  </details>

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

- **2026-07-28** — Prakhar Khatri — [Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories](http://arxiv.org/abs/2607.27250v1)
  <details><summary>📄 Abstract</summary>
  Persistent context files (AGENTS.md, CLAUDE.md) are standard practice for guiding AI coding agents, yet evidence for their effectiveness is contradictory. We present a controlled ablation of context-injection strategy across two frontier agents (Claude Code and Codex), 17 real tasks from 3 repositories (15 shared + 2 Codex-only), and 288 evaluated runs with gold-test evaluation. Context strategy does not measurably move correctness on either agent (bounded to <=10-15pp via equivalence testing). ...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 556 |
| prompt-injection | 461 |
| memory-poisoning | 37 |
| tool-use-attack | 95 |
| backdoor | 396 |
| adversarial-attack | 538 |
| privacy-leakage | 3714 |
| steganography | 53 |
| misuse | 839 |
| red-teaming | 109 |
| vulnerability | 2491 |
| defense | 2161 |
| alignment | 1984 |
| robustness | 1896 |
| watermark | 214 |
| unlearning | 82 |
| agent-safety | 49 |
| benchmark | 53 |
| survey | 258 |
| other | 5640 |

---

📚 **全部 21626 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-01 03:11:29*