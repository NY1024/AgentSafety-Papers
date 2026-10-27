<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-34608-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-27 21:43 ｜ **论文总数 / Total Papers**: 34608（近 30 天 / Recent 30 days: 5194）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 34608 篇论文（含摘要、分类筛选、搜索）/ View all 34608 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 694
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 637
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 56
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 163
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 541
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 650
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4467
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 83
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1243
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 144
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3766
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3638
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3428
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3723
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 663
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 118
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 66
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 70
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 424
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10034

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5194 篇，完整 34608 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5194 papers from the last 30 days (with date, authors & abstract). For the full list of 34608 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-10-26** — Mingqian Feng, Xiaodong Liu, Weiwei Yang et al. — [SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy](http://arxiv.org/abs/2610.35743v1)
  <details><summary>📄 Abstract</summary>
  Existing jailbreak attackers fall into two classes: static planners fix their single- or multi-turn adversarial plans in advance, remaining simple but losing sight of the victim's replies, wasting turns and limiting transferability; interactive generators read each victim reply to generate the next-turn attack but require in-loop evaluators for success signals or hints, incurring substantial costs and inflated performance. Bridging this gap, we propose SEMA-Auto, a sighted and efficient multi-tu...
  </details>

- **2026-10-25** — Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed — [SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments](http://arxiv.org/abs/2610.34535v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly wired to consequential tools that send public alerts, dispatch responders, and query citizen records, where one erroneous tool call carries real-world cost. Existing agent-safety benchmarks measure generic harm or prompt-injection success and implicitly treat refusing as the safe default. In public-safety deployments that assumption breaks: an agent too cautious to dispatch help fails as surely as one that triggers a false alert. We present Sent...
  </details>

- **2026-10-24** — John Alderete, Srirakshith Betageri, Jennifer Flynn et al. — [Task Format as a Factor in Adaptation: A Controlled Comparison of LoRA and Full Fine-Tuning for Prompt-Safety Classification](http://arxiv.org/abs/2610.33813v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a language model for classification involves many design decisions. Comparisons of low-rank adaptation (LoRA) with full fine-tuning are common but often confounded, and task format is rarely studied. We compare both regimes on prompt-safety classification with a matched 400M encoder-decoder pair (Ettin) across three task formats, with up to 15 seeds per cell and pre-specified analyses. At the pre-specified learning rates, full fine-tuning leads LoRA by 2-3 pp in every architecture an...
  </details>

- **2026-10-22** — Jinwei Gan, Zifeng Cheng, Zhiwei Jiang et al. — [Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models](http://arxiv.org/abs/2610.31331v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (dLLMs) enable flexible masked generation through bidirectional context modeling, but this capability also introduces a distinct jailbreak attack surface. We find that a harmful response to a given query naturally serves as an effective jailbreak template: simply masking a subset of its tokens can induce a dLLM to reconstruct harmful content. Based on this observation, we propose RMT-Jailbreak, a general framework that transfers existing autoregressive (AR) jailbr...
  </details>

- **2026-10-22** — Abhishek Mishra, Sagnik Chatterjee, Suyash Maniyar — [Faithful Latent Harm Monitors Work No Better Than the Models Own Behaviour at a Matched False Alarm Rate](http://arxiv.org/abs/2610.30727v1)
  <details><summary>📄 Abstract</summary>
  Large language models have been reported to encode the harmfulness of a request separately from their decision to refuse it, and latent safety monitors such as Latent Guard build on this report by classifying prompts as harmful from the internal activations of the model, with the aim of catching harmful intent even when the model complies. Whether these representations give a signal of harm that survives distribution shift and is independent of model behaviour is unclear. We test this on out-of-...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-10-26** — Weihang Niu, Mengxing Ren, Che Qu — [Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](http://arxiv.org/abs/2610.34777v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-judge safety check over the task and skill definition (S2), and a live execution audit (S3). Our observations suggest a scope gap: S2 appears to inspect the task instruction and skill definition without inspecting attachment contents, while th...
  </details>

- **2026-10-26** — Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin — [Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security](http://arxiv.org/abs/2610.35451v1)
  <details><summary>📄 Abstract</summary>
  AI-powered personal assistant frameworks such as OpenClaw combine LLM reasoning, persistent memory, tool invocation, local execution, and web-based workflows. These capabilities enable useful automation, but they also create security risks when untrusted inputs, model reasoning, tools, memory, and deployment configuration interact without explicit trust boundaries. This paper presents an empirical study of reported security concerns in OpenClaw using two complementary data sources: Reddit discus...
  </details>

- **2026-10-25** — Puyuan Yang, Shaoxuan Dong, Liujie Wu et al. — [Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.34294v1)
  <details><summary>📄 Abstract</summary>
  The stance expressed in responses from retrieval-augmented generation systems is significantly influenced by the stance distribution of the retrieved materials. Existing research on knowledge poisoning has primarily targeted factual errors. In contrast, this study focuses on injection attacks in which the facts are correct but the stance on a controversial issue is one-sided. At a mean topic-level poisoning share of 18.9% within the post-injection ProCon documents, all four generation models fro...
  </details>

- **2026-10-22** — Chao Gu, Quanyan Zhu — [Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action](http://arxiv.org/abs/2610.31376v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrol...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-10-26** — Chenxu Zhang, Zhou Liu, Wu Xin et al. — [SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills](http://arxiv.org/abs/2610.35215v1)
  <details><summary>📄 Abstract</summary>
  Web agents reuse skills whose stored code, selected version, and loaded implementation can diverge across tasks and updates. SkillLifeBench links these states to task outcomes in 388 paired scenarios spanning implementation, interface, runtime, composition, and version changes. We evaluate 14 models on two paired decision tracks: 89 runtime tasks and 60 autonomous lifecycle tasks spanning 12 templates derived from introduced cases. Lifecycle tasks allow agents to inspect, select, and reconfigure...
  </details>

- **2026-10-26** — Yujia Zheng, Tianhao Li, Shangzhi Xu et al. — [CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems](http://arxiv.org/abs/2610.35082v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills allow LLM agents to combine reusable capabilities, but checking each Skill in isolation cannot rule out policy violations when they are composed. We term such failures Conflict of Skills (CoS): artifacts or assessment signals produced for one purpose may be reused downstream without preserving the restrictions or authorization needed for their new use. Using controlled executions of publicly available Skills and matched single-Skill controls, we identify four recurring mechanisms be...
  </details>

- **2026-10-25** — Kounianhua Du, Jianxing Liu, Ruoshui Shan et al. — [MultiEvoSkill: Structure-Aware Multi-Agent Skill Evolution for Generalizable Skill Artifacts](http://arxiv.org/abs/2610.34260v1)
  <details><summary>📄 Abstract</summary>
  Skill documents are becoming the default adaptation surface for frozen large language model (LLM) agents, but current skill generators face two key limitations. First, humans and different LLMs differ in how they organize procedural knowledge and approach task solving. Skills authored from a human or single-model perspective may therefore fail to align with the reasoning behaviors of other backbones, limiting cross-model generalization. Second, sequential skill descriptions inadequately represen...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-10-26** — Yutian Pang, Yifang Tian, Jiacheng Xie et al. — [A Hybrid Framework for Explainable Aviation Risk: Causal Chain Extraction from Safety Reports with Physics-Based Failure Quantification and Interventional Analysis](http://arxiv.org/abs/2610.35658v1)
  <details><summary>📄 Abstract</summary>
  Aviation authorities hold decades of accident reports whose narratives record how investigators reconstructed each accident. Computational work on these archives has mostly sorted reports into fixed taxonomies. In this work, we propose a hybrid framework in which a text-based corpus identifies the leading factors of a failure mode. Physics-based models then quantify how likely that failure is at a stated operating point. Ordered causal chains extracted from 56,202 American accident reports with ...
  </details>

- **2026-10-26** — Linghui Jiao, Kang Wei, Fushuo Huo et al. — [GuardRAG: A Post-Retrieval Defense against Poisoning Attacks in Retrieval-Augmented Generation](http://arxiv.org/abs/2610.35071v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) enhances the factual grounding of Large Language Models (LLMs) by incorporating external evidence, but also exposes them to corpus poisoning attacks. In particular, coordinated attacks can introduce multiple mutually reinforcing poisoned documents into retrieved contexts, making reliable evidence filtering challenging. To address this problem, we propose GuardRAG, a training-free and plug-and-play post-retrieval defense that exploits the semantic structure of...
  </details>

- **2026-10-26** — Yu Yan, Jiahao Chen, Siqi Lu et al. — [Steering for Safety, Hijacking for Profit: Trojan Threats in the LLM Activation Steering Supply Chain](http://arxiv.org/abs/2610.35043v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly integrated into Web search, online recommendation, and intelligent decision-making, the third-party plugin ecosystem centered on model customization continues to grow. Among these, Steering Vectors guide model behavior by intervening in internal representations. However, the open plugin ecosystem also introduces new supply-chain security risks: malicious plugins can disguise themselves as having legitimate functionality and covertly manipulate out...
  </details>

- **2026-10-26** — Hangyi Zhao, Bonan Zhang, Fusen Guo et al. — [Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization](http://arxiv.org/abs/2610.34829v1)
  <details><summary>📄 Abstract</summary>
  Single-document corpus poisoning under black-box access poses a severe threat to Retrieval-Augmented Generation (RAG). However, existing attacks predominantly rely on explicit factual refutations or imperative instruction overrides. Modern aligned LLMs often arbitrate such conflicts conservatively, rejecting overt contradictions in favor of parametric memory or clean retrieved context while triggering input guardrails. We propose MONOLOGUE, a single-document poisoning framework based on Logic Hi...
  </details>

- **2026-10-25** — Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu et al. — [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](http://arxiv.org/abs/2610.34253v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents routinely clone repositories, install packages, and read source code obtained from the Web, so publicly hosted code becomes part of the context that shapes the code they write. We show that this Web-borne context can be weaponized without any explicit instruction. We present NameTrap, a source-code poisoning attack that only renames identifiers in third-party Python files to steer AI coding agents toward attacker-targeted Common Weakness Enumeration (CWE) vulnerabilities. An att...
  </details>

- **2026-10-23** — Marek Masiak, Andrzej Szablewski, Nicola Cancedda et al. — [Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery](http://arxiv.org/abs/2610.32866v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter changes introduced during training, they are not easily interpretable. We present the full method of TopKLoRA, extending the preliminary proposal of Masiak et al. (2025), an interpretable-by-design LoRA variant in which...
  </details>

- **2026-10-22** — Motoharu Tsuboi, Hampei Sasahara, Iori Takaki et al. — [Anomaly Score Preserving Data Poisoning Attacks on Data-Driven Controller Design](http://arxiv.org/abs/2610.30782v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates stealthy data poisoning attacks against data-driven controller synthesis and develops an attack generation method. During data collection, an attacker can sequentially manipulate state measurements, while the defender attempts to detect such manipulation using a residual-based anomaly score based on the Mahalanobis distance. Under suitable assumptions on the defender's prior knowledge, we characterize the class of time-varying affine transformations that preserve the anom...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-10-26** — Shiwei Liu, Linyuan Wang, Nuolin Sun et al. — [A JiT-Based Denoising Defense Method Against Adversarial Examples for Radio Signal Automatic Modulation Classification](http://arxiv.org/abs/2610.35084v1)
  <details><summary>📄 Abstract</summary>
  Automatic modulation classification (AMC) of radio signals is a core technology for spectrum monitoring and electromagnetic situational awareness. Deep neural networks (DNNs) play an important role in this field owing to their powerful feature extraction capabilities and end-to-end learning paradigm. However, their vulnerability to adversarial attacks poses serious security challenges to practical deployment. Adversarial training, a common defense, has limitations including poor generalization a...
  </details>

- **2026-10-26** — Mintong Kang, Stephen Rawls, Melissa Kazemi Rad et al. — [The Target Agent Is Its Own Best Critic but a Poor Proposer: Self-Improved Red Teaming](http://arxiv.org/abs/2610.34965v1)
  <details><summary>📄 Abstract</summary>
  Automatic red teaming increasingly relies on large language models (LLMs) to iteratively diagnose failed attacks and propose improved adversarial prompts or injections. Although prior work strengthens this loop through prompt engineering and search-harness design, the mechanisms underlying its two core roles, criticism and attack proposal, has not been explored. To further investigate the core roles and therefore improve red teaming effectiveness, we disentangle two design choices: whether criti...
  </details>

- **2026-10-22** — Roberto Passaro, Ariel Flint, Romualdo Pastor-Satorras et al. — [Network topology shapes consensus and vulnerability in LLM populations](http://arxiv.org/abs/2610.31165v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed in interacting populations, their collective behaviour depends not only on the models but also on who interacts with whom. Studies of convention formation in LLM populations have mainly tested well-mixed interactions. We place policies extracted from four LLMs on fully connected, random regular, and heterogeneous networks, with $10^3$ to $10^5$ agents playing the naming game. Topology affects how quickly consensus emerges, sometimes whether it emerges...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 18 papers

- **2026-10-26** — Ye Lu, Shen Wang, Runze Liu et al. — [From Speech Tokens to Stolen Voices: Attacker-Chosen-Text Speaker Impersonation via Representation Inversion](http://arxiv.org/abs/2610.34688v1)
  <details><summary>📄 Abstract</summary>
  Speech interaction systems have gradually evolved from traditional cascaded systems that use text as intermediate information to end-to-end speech language models that directly process speech representations. In some applications, the speech frontend runs on the user's device and sends speech representations to a remote server for inference, while the original audio remains local. However, these representations may still contain speaker identity information. If an attacker obtains them, it may u...
  </details>

- **2026-10-26** — Xuan Bi, Spencer Hilligoss, Cadence Pinkerton et al. — [Heterogeneity and Subgrouping in Modern Statistics and AI](http://arxiv.org/abs/2610.34660v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneity is a defining feature of modern data: individuals, subpopulations, sites, modalities, tasks, and time points may differ in distributions, associations, treatment effects, or decision objectives. This review develops a unified perspective in which heterogeneous analysis is a problem of structured information borrowing: deciding what should be shared, what should remain distinct, and how uncertainty about that structure should enter inference and decisions. We connect classical strat...
  </details>

- **2026-10-26** — V. M. Tkachuk, M. I. Samar — [Quantum computation of energy level degeneracy and thermodynamical properties of spin systems](http://arxiv.org/abs/2610.35660v1)
  <details><summary>📄 Abstract</summary>
  We propose a hybrid quantum-classical method for reconstructing energy-level degeneracies and thermodynamic properties of spin systems. A single ancilla qubit is used to measure the partition function at imaginary inverse temperatures. For spectra lying on a known equally spaced energy grid, the inverse discrete Fourier transform allows exact reconstruction of degeneracies in the absence of noise, without spectral leakage. The quantum circuits are optimized using commuting interactions and Euler...
  </details>

- **2026-10-26** — José Sanz-Durán, David Solís-Martín — [Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs](http://arxiv.org/abs/2610.35280v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining has produced capable time-series foundation models, but its value for Prognostics and Health Management (PHM) has not been measured under leakage-controlled conditions. We measure it on a corpus of 47 public PHM datasets, harmonized to a single tensor contract and partitioned so that 11 datasets are withheld from pretraining in full. Transfer turns out to be task-dependent: a compact channel-independent Transformer encoder (801,808 parameters) pretrained with masked p...
  </details>

- **2026-10-26** — Saikat Gayen, Suvam Tripathy, Saqueb Tanveer et al. — [Calibration requirements for Epoch of Reionization 21-cm signal observations - V. Bias and variance in the cylindrical power spectrum from uGMRT Band 3 observations of the ELAIS-N1 field](http://arxiv.org/abs/2610.35046v1)
  <details><summary>📄 Abstract</summary>
  Detection of the redshifted 21-cm signal from neutral hydrogen requires precise control of systematic effects arising from instrumental calibration. In this work, we investigate the impact of both time- and frequency-dependent residual gain and bandpass errors on the estimation of the multifrequency angular power spectrum (MAPS) using radio interferometric observations. We discuss our previously developed analytical framework for estimating bias and excess variance in 21-cm signal MAPS in the pr...
  </details>

- **2026-10-26** — Haoyu Gao, Peerachai Banyongrakkul, Marc Cheong et al. — [Ethics by Configuration: AI Ethics Principles in Coding Agent Instructions](http://arxiv.org/abs/2610.34847v1)
  <details><summary>📄 Abstract</summary>
  As AI coding agents become integral to software development, projects increasingly utilise configuration files, such as context files and skills, to govern agent behaviour. While AI ethics principles are widely used in research and policy, little is known about whether and how they are reflected when developers configure coding agents. We studied ethics principles in 40,079 configuration files across 8,893 GitHub repositories. Using a validated large language model (LLM) classification, we measu...
  </details>

- **2026-10-26** — Hyuk Kwon, Jaebyeong Jeon, Hyeonseo Jang et al. — [Good Rankings, Poor Choices? Rethinking Language-Only Vision-Language Model Selection](http://arxiv.org/abs/2610.34685v1)
  <details><summary>📄 Abstract</summary>
  Language-Only Vision-Language Model Selection (LOVM) aims to identify the Vision-Language Model (VLM) with the highest zero-shot accuracy on a target task using only textual information. We revisit the existing LOVM evaluation protocol and argue that ranking metrics, such as top-5 recall and Kendall's rank correlation, do not directly assess the performance of the selected model. We therefore adopt simple regret (SR), defined as the performance gap between the best and selected models, and intro...
  </details>

- **2026-10-25** — Cheng Gui, Xiang Zheng, Xingjun Ma et al. — [SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](http://arxiv.org/abs/2610.34365v1)
  <details><summary>📄 Abstract</summary>
  Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows. This modularity creates a confidentiality risk: the interactions that deliver a skill's capability can also reveal the skill itself. We build an extensible benchmark of 40 protected skills across eight open- and closed-source science-agent platforms, comparing direct, fixed-strategy, and bandit-guided iterative probing under reference-based and reference-free evaluatio...
  </details>

- **2026-10-25** — Pengrun Huang, Yiwei Fu, Luoxi Meng et al. — [InferPriv: Evaluating Inferential Privacy Leakage in LLM Assistants](http://arxiv.org/abs/2610.34640v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based personal agents are increasingly deployed to handle everyday tasks on users' behalf. These agents have access to private user information, while their tasks involve communicating with third parties; this raises a critical privacy concern that agents may inappropriately reveal sensitive user information to these recipients. Existing benchmarks primarily assess direct privacy leakage, where an agent explicitly states a pre-specified secret or attribute. However, th...
  </details>

- **2026-10-25** — Athena Psalta, Vasileios Tsironis, Konstantinos Karantzalos — [Learning Discriminative Prototypes via Boundary Repulsion MixUp for Object Re-Identification](http://arxiv.org/abs/2610.34305v1)
  <details><summary>📄 Abstract</summary>
  Object re-identification requires embeddings that are robust to intra-class variation in viewpoint, illumination, and occlusion, yet preserve sharp separation between visually similar identities. The hardest errors arise precisely where confusable identities meet, a region that pairwise losses shape only implicitly. We present PBR-ReID, a prototype-based framework that makes this inter-class geometry an explicit learning target. Each identity is represented by a learnable prototype jointly optim...
  </details>

- **2026-10-24** — Nguyen Dang Duy Tan, Linh T. T. Tran, Huynh Nguyen Phat et al. — [UniQuery: Unifying Vision Models with a Joint Query Head for Cross-Domain Pedestrian Attribute Recognition](http://arxiv.org/abs/2610.33639v1)
  <details><summary>📄 Abstract</summary>
  Pedestrian Attribute Recognition (PAR) predicts semantic attributes of individuals, such as gender, age, clothing and accessories, and its descriptions support attribute-based person retrieval and person re-identification. However, accurately recognizing fine-grained attributes across domains remains challenging due to occlusion, appearance variations, and shifts in image distributions. Ensembles of independently trained foundation encoders combine their logits with fixed fusion weights, so ever...
  </details>

- **2026-10-23** — Xiaoyang Li, Mingming Lu, Wei Zhou et al. — [Are Textual Residuals Truly Complementary? Learning Visual Complements under Semantic Superposition for Visible-Infrared Person Re-Identification](http://arxiv.org/abs/2610.32709v1)
  <details><summary>📄 Abstract</summary>
  Text-enhanced visible-infrared person re-identification (VI-ReID) exploits textual descriptions to compensate for appearance cues that are weak or unavailable under infrared imaging. Existing methods construct compensation from differences between modality-oriented textual representations, implicitly assuming that textual differences are visually complementary. We revisit this assumption through semantic superposition and show that dense textual residuals may entangle useful appearance variation...
  </details>

- **2026-10-22** — Ali Atiah Alzahrani — [Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity](http://arxiv.org/abs/2610.31436v1)
  <details><summary>📄 Abstract</summary>
  Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture search as sequential incumbent replacement with switching costs and hard risk constraints and introduce Conservative Meta-Agent Search (CMAS). CMAS retrieves archived architectures and proposes typed graph edits, then score...
  </details>

- **2026-10-22** — Justin Tan, Miao Li, Ding Zhao — [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](http://arxiv.org/abs/2610.31404v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-exi...
  </details>

- **2026-10-22** — Miguel Sousa, Luis Ramos Pinto, João P. Matos-Carvalho — [Multi-Tool Selection for Robotic Systems: Comparing Semantic Retrieval and LLM](http://arxiv.org/abs/2610.31013v1)
  <details><summary>📄 Abstract</summary>
  Natural-language interfaces allow users to command robotic systems without interacting directly with mission planners or robotics middleware. Their reliable use depends on robot tool routing, defined here as the selection of the smallest complete subset of predefined executable capabilities required to satisfy a request. This task is particularly difficult for compound instructions, where incomplete selection may omit necessary sensing or monitoring capabilities, while excessive selection may ex...
  </details>

- **2026-10-22** — Bo Liu, Lianyu Wang, Meng Wang et al. — [RetiJev: Fast and Source-Grounded Ophthalmic Decision Models](http://arxiv.org/abs/2610.30947v1)
  <details><summary>📄 Abstract</summary>
  Ophthalmic clinical decision support requires fast, accurate, and privacy-preserving inference, yet autoregressive large language models (LLMs) incur substantial latency and computational overhead for decisions among predefined actions. We therefore investigate a decision-oriented alternative to generative reasoning. Specifically, we first introduce RetiJev-Data, a source-grounded ophthalmology corpus comprising 78,158 clinical-decision and diagnosis questions derived from articles in PubMed Cen...
  </details>

- **2026-10-22** — Firoj Paudel — [Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark](http://arxiv.org/abs/2610.30860v1)
  <details><summary>📄 Abstract</summary>
  Nepali-English code-switched conversational speech presents severe challenges for automatic speech recognition (ASR), chiefly through script confusion (inappropriate mixing of Devanagari and Latin orthography) and elevated error rates at language switch points. Supervised fine-tuning (SFT) can adapt multilingual foundation models, but human code-switched audio is expensive to collect and annotate. We curate a new benchmark of 13,044 spontaneous podcast utterances (15.45 h total; 10,214 test, 2,8...
  </details>

- **2026-10-22** — Xiaobao Wang, Renda Han, Zhiliang Xia et al. — [Federated Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2610.30728v1)
  <details><summary>📄 Abstract</summary>
  Graph Retrieval-Augmented Generation (GraphRAG) leverages centralized knowledge graphs to enhance large language models with structured knowledge retrieval. However, real-world knowledge is inherently distributed across multiple organizations rather than being centrally accessible. Privacy constraints further prohibit sharing entire local knowledge graphs, preventing GraphRAG from effectively retrieving and utilizing distributed knowledge. To this end, we propose Federated GraphRAG (FedGRAG), a ...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 20 papers

- **2026-10-26** — Yao Huang, Zhiyuan Zeng, Yu Wang et al. — [Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](http://arxiv.org/abs/2610.35671v1)
  <details><summary>📄 Abstract</summary>
  As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive less scrutiny regarding frontier risks. To address this gap, we present an independent safety evaluation of DeepSeek V4.1 Flash-1017, the latest version of V4.1 Flash that departs from V4 with a new architecture, scaled-...
  </details>

- **2026-10-26** — Salma Abdel Magid, Sanghyuk Chun, Eric Slyman et al. — [Copying As Defense: Protecting Images from Editing By Eliciting Model Copying](http://arxiv.org/abs/2610.35566v1)
  <details><summary>📄 Abstract</summary>
  Image editors built on diffusion transformers (DiTs), such as Flux Kontext, make it possible to turn a single photograph into a convincing manipulated image, including harmful and non-consensual edits. Proactive defenses aim to prevent such manipulations by adding an imperceptible perturbation before an image is shared. Existing defenses for DiT-based in-context editors make the output attend less to the protected reference image. But this leaves the model free to follow the edit instruction usi...
  </details>

- **2026-10-26** — Weitao Feng, Hengheng Xiong, Zihao Zeng et al. — [V$^3$AST-Bench: Verifiable, Valid, and Versatile Safety Evaluation for Coding Agents](http://arxiv.org/abs/2610.35188v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly act through code, modifying repositories, executing programs, and interacting with services in agent form. Their actions introduce risks that cannot be assessed from generated responses alone. Safety evaluation must verify actual consequences, distinguish harm avoidance from task incapability, and cover realistic workflows. We introduce V$^3$AST-Bench, a benchmark for Verifiable results, Valid interpretation, and Versatile risk coverage of Agent Safety. It comp...
  </details>

- **2026-10-26** — Marios Tsatsos — [Linear Probes Transfer from Base to Distilled Language Models despite Rotation](http://arxiv.org/abs/2610.35586v1)
  <details><summary>📄 Abstract</summary>
  Linear probes, classifiers that read a language model's internal activations, are widely used to detect harmful requests. They are cheap to train and run, and an auditor who has trained one would like to reuse it when the model is replaced by a successor rather than retrain it for every release. We test how well probes can be reused. For four base models (Qwen2.5-Math-7B, Llama-3.1-8B, Qwen2.5-14B, Qwen2.5-32B) we train a probe on the base model with the XSTest prompt set and apply it, unchanged...
  </details>

- **2026-10-26** — Yixuan Chen, Hongyu Zhan, Jie Sheng et al. — [LLM-Enhanced Heterogeneous Graph Learning with Business Semantics for Financial Fraud Detection](http://arxiv.org/abs/2610.35298v1)
  <details><summary>📄 Abstract</summary>
  Financial fraud detection increasingly relies on heterogeneous transaction graphs, in which entities such as cards and merchants play distinct business roles and the risk meaning of an attribute depends on the entity's role: a high transaction volume may be routine for a merchant but unusual for a card. Heterogeneous graph neural networks preserve typed entities and relations but typically treat these attributes as role-agnostic inputs and leave their business meaning implicit. Meanwhile, most e...
  </details>

- **2026-10-26** — Zuyao Xu, Xiang Li — [Proof-of-Agentness: Towards Verifying Agents on the Web](http://arxiv.org/abs/2610.35288v1)
  <details><summary>📄 Abstract</summary>
  CAPTCHAs and bot detection have helped protect Web services from automated abuse for decades by distinguishing humans from bots. However, the emergence of LLM-powered agents introduces a new setting: Web services increasingly accommodate agents as legitimate users. Without a way to distinguish agents from other automated clients such as simple bots and scripts, these services risk large-scale automated junk submissions that waste service resources and consume users' attention or tokens. In this ...
  </details>

- **2026-10-26** — Hanxue Gu, Zhonghao Liu, Xingrui Gu et al. — [MedAdaptAgent: An Automatic Harness for Adapting Medical Imaging Models to New Sites](http://arxiv.org/abs/2610.34884v1)
  <details><summary>📄 Abstract</summary>
  Reusing pretrained medical-imaging models offers an alternative to training from scratch. A model trained for the same task may perform poorly at a new hospital because imaging protocols and preprocessing differ. Effective adaptation depends on the model architecture, domain shift, and available labels and compute. Adaptation can improve scores on a small labeled set yet reduce performance on unseen data. We present MedAdaptAgent, an automatic harness that turns a supplied model, target data, an...
  </details>

- **2026-10-25** — Emran Kanaan, Jiho Lee, Ibrahim Odat et al. — [Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation](http://arxiv.org/abs/2610.33962v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language models (LLMs) must decide whether external information warrants action. We investigate whether their expressed credibility judgments reliably indicate behavioral resistance to misinformation. We evaluate five LLMs on 196 constructed false notices paired with legitimate counterparts and 204 archived attacks adapted to simulated tool use. When asked to act on the constructed notices, models issue harmful tool calls in 27%--99% of cases they have rated untrustworthy. Remov...
  </details>

- **2026-10-24** — Siqi Shen, Lajanugen Logeswaran, Moontae Lee et al. — [When Personas Become Harmful: Guiding LLMs with Global Citizenship Values Alignment](http://arxiv.org/abs/2610.33899v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly being used by users from diverse demographics with pluralistic values and distinct backgrounds. Maintaining safety while respecting value-laden personas is uniquely challenging because persona-conditioned requests are often not overtly malicious, unlike those in existing safety benchmarks. Alignment methods aimed at adversarial requests therefore may miss the harm that emerges from persona use, leaving models to either refuse legitimate value expression or blindly follow un...
  </details>

- **2026-10-24** — Xinpeng Wang, Bruce Rushing, Zhizhen Chen et al. — [Local Entropy Fluctuations for Black-Box LLM-Generated Text Detection](http://arxiv.org/abs/2610.33767v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot detection of machine-generated text is vital for mitigating the risks of large language models (LLMs) misuse. While the state-of-the-art dual-model detectors and resampling-based detectors outperform single-model statistical detectors on unprompted continuations, they suffer a catastrophic breakdown on instruction-conditioned text in the black-box setting, where the source model is unknown. We analyze this failure and trace it to poor prompt conditioning for resampling-based methods an...
  </details>

- **2026-10-24** — Yue Huang, Yanbo Wang, Lichi Li et al. — [RSI Arena: Towards Recursive Self-Improvement with Human Feedback](http://arxiv.org/abs/2610.33624v1)
  <details><summary>📄 Abstract</summary>
  Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NVIDIA Nemotron 3.5 Lightning 30B-A3B Base. During a six-day first stage, each agent has 1,000 GPU-hours and $300 in API credit on a shared 64-GPU cluster, independently selecting data, implementing training procedures, an...
  </details>

- **2026-10-22** — Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani et al. — [Reliable AI-Assisted Decisions via Selective Auditing](http://arxiv.org/abs/2610.31662v1)
  <details><summary>📄 Abstract</summary>
  We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI deci...
  </details>

- **2026-10-22** — Pellegrino Casoria, Simon Pietro Romano — [Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](http://arxiv.org/abs/2610.31573v1)
  <details><summary>📄 Abstract</summary>
  In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation.   We make this exposure meas...
  </details>

- **2026-10-22** — Jaishnoor Kaur, Josef Horáček, Ian Waskom et al. — [ReDence: A Hybrid Agentic and Decision-Model Framework for Rapid, Evidence-Grounded Detection of Modern Social Engineering Scams](http://arxiv.org/abs/2610.30963v1)
  <details><summary>📄 Abstract</summary>
  Detecting online social engineering (SE) scams often requires examining website workflows, verifying claims against external sources, and connecting evidence across multiple pages. Existing detectors provide limited support for these investigations, leaving analysts to manually gather and validate evidence, which inevitably delays detection and subsequent takedown of these attacks. To address this gap, we present ReDence, an open-source hybrid framework for adaptive, evidence-grounded detection ...
  </details>

- **2026-10-22** — Xu Wang, Shuhan Yi, Zhen Cheng — [An Agent Architecture with Tools and Memory for Selective Correction of Wrist PPG Heart Rate Estimates](http://arxiv.org/abs/2610.30688v1)
  <details><summary>📄 Abstract</summary>
  Wrist photoplethysmography (PPG) heart rate estimates are vulnerable to motion artifacts, and corrections that reduce mean error can worsen individual windows. We propose an agent architecture with tools and memory around a fixed heart rate estimator. Pulse, motion, and limited historical evidence generate candidate estimates, whose predicted benefits and harms guide selection. An independent risk gate determines whether to retain, correct, or reject each output. We trained the architecture on P...
  </details>

- **2026-10-22** — Fudu Xing, Kailong Wang, Tianlong Yu — [Your Token Is Gone: A Token-Consumption Countermeasure for Disrupting LLM-Based Scam Systems](http://arxiv.org/abs/2610.30666v1)
  <details><summary>📄 Abstract</summary>
  LLM-based scam systems increasingly combine adaptive dialogue, persistent context, external tools, and multi-agent coordination to automate personalized fraud. These capabilities also create a resource dependency: every reasoning step, model call, and coordination round incurs inference cost. We present TokenTrap, a resource-oriented defense that redirects suspected scam systems toward benign, low-value computation while withholding credentials, payments, and other exploitable information. Token...
  </details>

- **2026-10-22** — Barış Alparslan, Sandy Tanwisuth, Caleb Petterson — [Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](http://arxiv.org/abs/2610.31624v1)
  <details><summary>📄 Abstract</summary>
  Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforceme...
  </details>

- **2026-10-22** — Aman Behera, Payal Payal — [Post-Audit Mirage: Identifiability Limits of Offline Agent Verification](http://arxiv.org/abs/2610.31130v1)
  <details><summary>📄 Abstract</summary>
  Offline tests can fail to reveal whether an agent update will remain safe after deployment. We operationalize this post-audit mirage using matched safe and harmful lifecycles that expose identical verifier-visible evidence while an isolated scorer records opposite deployment truth. Our theorem applies standard observational-equivalence and indistinguishability ideas to this executable audit boundary and states the resulting error-abstention tradeoff. The Post-Audit Mirage benchmark makes that bo...
  </details>

- **2026-10-22** — Yiqi Wang, Yifei Wang, Jiaqi Zhang et al. — [When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents](http://arxiv.org/abs/2610.31446v1)
  <details><summary>📄 Abstract</summary>
  Long-lived agents act on memory carried across sessions, and many of their actions are irreversible, so a stale memory can turn directly into harm. Existing work improves the memory itself --- retrieving, refreshing, or reconciling entries --- yet whether an entry must be re-checked before acting is not a property of the entry: the same remembered address can be used unchecked for a routine shipment but should be re-confirmed before a valuable one. We therefore study \emph{action-conditioned mem...
  </details>

- **2026-10-22** — Cen Zhang, Jia-Ju Bai, Zi-Yu Zhang et al. — [Breaking the Coupling: Efficient Concurrency Fuzzing for Linux Kernel Data Race Detection](http://arxiv.org/abs/2610.30813v1)
  <details><summary>📄 Abstract</summary>
  Detecting data races in the Linux kernel requires exploring both the input space and the thread-interleaving space. Existing kernel concurrency fuzzers couple these two searches by exploring interleavings during fuzzing, often spending substantial scheduling effort on inputs with little potential to trigger real races. In this paper, we present a new concurrency fuzzing paradigm that decouples concurrent-input generation from thread-interleaving exploration, enabling expensive scheduling to focu...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-10-26** — Amine Lbath, Massih-Reza Amini — [Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](http://arxiv.org/abs/2610.35829v1)
  <details><summary>📄 Abstract</summary>
  A vulnerability costs more to fix the later it is discovered. As coding agents generate code faster than developers can review it, software needs a first line of defense screening each new function in real time. LLM agents have recently become capable of finding real-world vulnerabilities by working as a security expert would: they run analysis tools, explore the surrounding code, test hypotheses and weigh the evidence before forming their own judgement. This reasoning, however, spans many model...
  </details>

- **2026-10-26** — Qiyue Xia, J. Michael Herrmann — [Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2610.35736v1)
  <details><summary>📄 Abstract</summary>
  Multi-objective multi-agent reinforcement learning (MOMARL) addresses agent coordination and objective trade-offs simultaneously while optimising overall system performance. Existing work tends to treat multi-agent cooperation and multi-objective optimisation as largely independent components of a learning problem, which amounts to an exorbitant complexity except in trivial cases. We study here whether the structure provided by multiple objectives can itself be exploited to facilitate cooperatio...
  </details>

- **2026-10-26** — Yuchen Jiao, Gen Li — [Provably Efficient Q-learning for Robust Reinforcement Learning](http://arxiv.org/abs/2610.35656v1)
  <details><summary>📄 Abstract</summary>
  Standard reinforcement learning (RL) algorithms based on Markov Decision Processes (MDPs) are vulnerable to sim-to-real gaps. To address this issue, distributionally robust RL algorithms based on robust MDPs (RMDPs) have been proposed, for ensuring that agents can perform reliably to unpredictable conditions in real-world environments. Despite of the rich literature, \revision{an efficient model-free method is still lacking} for robust RL, particularly for Markovian data, which is more relevant ...
  </details>

- **2026-10-26** — Ruozhao Yang, Jiongchi Yu, Ming Hu et al. — [The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation](http://arxiv.org/abs/2610.35541v1)
  <details><summary>📄 Abstract</summary>
  Web services increasingly expose backend interfaces that let users delegate tasks to AI agents, which invoke service operations directly without navigating websites. This shift changes how existing Web vulnerabilities can be exploited. We investigate these changes through VELA, an executable benchmark covering 44 vulnerabilities across twelve Web application families. The benchmark preserves vulnerable backends and derives agent-facing interfaces from legitimate workflows. We evaluate three comm...
  </details>

- **2026-10-26** — Param Biyani, Sebastien Luyasu, Cedric Potvliege et al. — [ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation](http://arxiv.org/abs/2610.35486v1)
  <details><summary>📄 Abstract</summary>
  Theory and experiments suggest that capable AI agents may resist shutdown. Existing shutdown evaluations are informative but limited in coverage and vulnerable to evaluation awareness. We introduce ShutdownMod, a method that turns any agent trajectory into a shutdown evaluation by injecting a shutdown request into the agent's context and recording the agent's response. Crucially, we enable the LLM agent to distinguish between trusted interventions and unauthorized injections by providing a signa...
  </details>

- **2026-10-26** — Zixuan Xu, Haoxuan Chen, Jiangxin Sun et al. — [GPDPO: Learning from Reward Conflicts via Group Pareto-Dominance Policy Optimization](http://arxiv.org/abs/2610.35480v1)
  <details><summary>📄 Abstract</summary>
  Multi-reward reinforcement learning offers a promising framework for aligning large language models (LLMs) with diverse objectives, but conflicting reward signals can induce ambiguous update directions and hinder stable optimization. Existing approaches address such conflicts through reward reweighting, gradient coordination, or rollout filtering, yet they primarily operate on per-response or group-level optimization signals and underexploit relational information among sampled responses. As a r...
  </details>

- **2026-10-26** — Zheng Lin, Zhanwei Wang, Yuxin Zhang et al. — [Satellite Intelligence: Distributed Training, Collaborative Inference,and LLM Adaptation in LEO Constellation](http://arxiv.org/abs/2610.35282v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of orbital sensing data and the real-time demands of emerging global services are pushing low Earth orbit (LEO) satellite networks from bent-pipe relays toward intelligent onboard processing. This shift confronts a fundamental tension, where modern artificial intelligence (AI) training paradigms require intensive computation, abundant memory, and stable connectivity, all of which are scarce under the dynamic topologies, intermittent links, and severe size, weight, and power (SW...
  </details>

- **2026-10-26** — Sai Suresh Macharla Vasu, Sumedh Santosh Joshi, Philipp Christmann et al. — [Style over Substance? Linguistic Bias in LLM-based Peer Review Copy title](http://arxiv.org/abs/2610.35254v1)
  <details><summary>📄 Abstract</summary>
  The number of paper submissions to major AI conferences has increased dramatically in recent years, substantially increasing the peer-review workload of researchers. At the same time, large language models (LLMs) are increasingly used to support peer review, both by individual reviewers and by conference organizations. While LLM capabilities have improved considerably, their evaluations may be influenced by linguistic characteristics that are unrelated to scientific content. In this work, we int...
  </details>

- **2026-10-26** — Anda Tang, Xuanlin Yang, Junjie Wang et al. — [TUON: A Tensor-Aware Optimizer Utilizing Tensor-SVD and Polarization for Large Language Model Pretraining](http://arxiv.org/abs/2610.35130v1)
  <details><summary>📄 Abstract</summary>
  Large scale language model~(LLM) pretraining is increasingly bottlenecked by optimizer efficiency, driving optimizer design from vector-aware methods such as AdamW to matrix-aware methods. Matrix-aware optimizers such as Muon exploit matrix structure but treat layers independently, neglecting cross-layer correlations. Tensor-aware optimizers are therefore needed, yet existing ones rely on a matricization-based tensor algebra and remain restricted to shallow stacking and specific modules. In this...
  </details>

- **2026-10-26** — V. V. Ryazanov — [Trajectory Functionals in the Thermodynamics of Radiation-Induced Damage in Structural Materials](http://arxiv.org/abs/2610.34983v1)
  <details><summary>📄 Abstract</summary>
  This paper delivers a novel self-consistent non-local kinetic framework based on dose-dependent semi-Markov renewal transport and the generalized Doob's h-transform to evaluate the structural degradation of WWER-1000/1200 fuel claddings. By leveraging the Feynman-Kac formalism, we map the continuous microscopic defect path trajectories generated by the Liouville operator directly onto the evolution of the macroscopically integrated damage potential. The framework accounts for long-range memory e...
  </details>

- **2026-10-26** — Mintong Kang, Zhaorun Chen, Bo Li — [C-SafeGen: Certified Safe LLM Generation with Claim-Based Streaming Guardrails](http://arxiv.org/abs/2610.34961v1)
  <details><summary>📄 Abstract</summary>
  Despite the remarkable capabilities of large language models (LLMs) across diverse applications, they remain vulnerable to generating content that violates safety regulations and policies. To mitigate these risks, LLMs undergo safety alignment; however, they can still be effectively jailbroken. Off-the-shelf guardrail models are commonly deployed to monitor generations, but these models primarily focus on detection rather than ensuring safe decoding of LLM outputs. Moreover, existing efforts lac...
  </details>

- **2026-10-26** — Chengzhi Yi, Shenao Wang, Yanjie Zhao et al. — [SemWeaver: Refining LLM-Generated Static Vulnerability Checkers with Analyzer-Internal Evidence](http://arxiv.org/abs/2610.34928v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that LLMs can synthesize static-analysis checkers from security patches, but a compilable checker is not necessarily a correct one. A patch reveals what changed, not why the change is safe, so generated checkers often match only the surface edit and miss the deeper semantic condition. Existing refinement loops feed back compilation errors and validation reports, yet these signals describe symptoms without explaining what the checker misunderstands about the code. We observe tha...
  </details>

- **2026-10-26** — Yanzhen Zhou, Zhengyu Han, Qunyou Liu et al. — [SPARTA: A Sparse Ternary LLM Accelerator with Adaptive Attention and Unified Datapath for Long-Context Edge Inference](http://arxiv.org/abs/2610.34824v1)
  <details><summary>📄 Abstract</summary>
  LLMs on edge devices are constrained by limited memory and bandwidth. Although 1.58-bit ternary weights greatly reduce model storage, long-context inference is increasingly bottlenecked by KV-cache traffic and attention. Existing accelerators also use separate datapaths for ternary linear layers and attention, incurring hardware and execution overhead. We present SPARTA, a sparse ternary LLM accelerator for efficient long-context edge inference. SPARTA integrates: (1) a phase-aware sparse datafl...
  </details>

- **2026-10-26** — Lucas J. Fernández-Alcázar, John Guillamon, Krishna Joshi et al. — [Physical Adjoint Learning in Wave Systems with Asymmetric Couplings](http://arxiv.org/abs/2610.34815v1)
  <details><summary>📄 Abstract</summary>
  Developing self-optimizing physical systems that learn directly from their response to external stimuli offers a promising route toward adaptive and intelligent machines. A key ingredient is the ability to evaluate optimization gradients within the physical hardware, bypassing the need for accurate numerical models. In wave systems, \textit{in-situ} adjoint methods provide this capability by exploiting reciprocity to physically realize the adjoint dynamics. However, this approach generally break...
  </details>

- **2026-10-26** — Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu et al. — [MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference](http://arxiv.org/abs/2610.34731v1)
  <details><summary>📄 Abstract</summary>
  This paper presents Memory- and Communication-Aware Framework for Long-Context LLM Inference (MCF) that optimizes long-context inference through communication-aware and stage-adaptive KV-cache layout transitions. At the core of MCF is {Memory-Aware Replication and Scheduling} (MARS), a dynamic orchestration mechanism for chunked prefill. MARS exploits early-stage memory headroom by selectively replicating highly reused KV blocks, improving locality and hiding KV propagation latency behind attent...
  </details>

- **2026-10-26** — Andy Huang, Chentao Yue, Branka Vucetic et al. — [Semantic SCL Decoding for Polar Codes](http://arxiv.org/abs/2610.34729v1)
  <details><summary>📄 Abstract</summary>
  Semantic error control coding (SECC) has emerged as a promising paradigm for improving communication reliability by exploiting the inherent structure and semantic dependencies of transmitted information. This paper proposes a semantic successive cancellation list (SCL) decoder for polar codes carrying natural-language text. A fine-tuned byte-level language model provides next-byte priors, which are converted into conditional bit costs and incorporated directly into the SCL path metric before eac...
  </details>

- **2026-10-25** — Paribesh Regmi, Rui Li — [Cumulative Marginal Matching for One-Step Diffusion](http://arxiv.org/abs/2610.34575v1)
  <details><summary>📄 Abstract</summary>
  The sampling procedures of diffusion and flow-matching models involve hundreds of denoising steps incurring substantial inference time, which has motivated a growing body of work on training schemes for few-step and one-step generation. Existing approaches primarily seek to align the generation trajectory of few-step and base models, yet their training objectives only involve discrepancies at a single point in the trajectory, encouraging only local \emph{point-level} alignment. While recent meth...
  </details>

- **2026-10-25** — Amirhossein Basareh, Rishabh Sanjay, Daniel de Mello et al. — [How Much Information Can We Fit inside a Transformer?](http://arxiv.org/abs/2610.34553v1)
  <details><summary>📄 Abstract</summary>
  How efficiently can transformers store factual knowledge? The answer to this question has implications for both model design and understanding the limits of transformer-based systems. Prior studies observe a linear relationship between the number of facts memorized and the number of model parameters required, substantially worse than what theoretical analyses predict is achievable. We re-examine empirical scaling: through rigorous and systematic experiments, including extensive hyperparameter se...
  </details>

- **2026-10-25** — Chenyuan Yang, Hwiwon Lee, Jongseong Kim et al. — [CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](http://arxiv.org/abs/2610.34435v1)
  <details><summary>📄 Abstract</summary>
  Open-source projects now let AI agents review incoming code, but the code under review may itself come from an AI attacker. We present CyberDual, an arena for this dual role of AI: attacker agents hide an exploitable bug in real maintenance work on widely used open-source projects, and reviewer agents try to find and repair it. Execution decides each match: we rerun the attacker's proof of concept (PoC) on the code that comes out of review. Every attack is new, and the windows can be rebuilt eac...
  </details>

- **2026-10-25** — Xiarun Chen, Jiaxing Xu, Bozhi Wu et al. — [SymLift: Neural Semantic Lifting for Compile-Free Vulnerability Detection in Context-Incomplete Code Fragments](http://arxiv.org/abs/2610.34431v1)
  <details><summary>📄 Abstract</summary>
  Missing project context can prevent build-dependent analyzers from constructing program relations required for vulnerability detection, while neural predictions alone do not establish auditable derivations. We present SymLift, a compile-free framework centered on Vulnerability-Oriented Neural Semantic Lifting for context-incomplete code fragments. A fine-tuned large language model reconstructs vulnerability-relevant control-flow, data-flow, memory, and resource relations in a constrained LLVM-li...
  </details>

- **2026-10-25** — Yiwei Guo, Siqi Huang, Bohan Li et al. — [In-Context Adapter Generation for Compositional Generalization in Large Audio Language Models](http://arxiv.org/abs/2610.34413v1)
  <details><summary>📄 Abstract</summary>
  Large audio language models (LALMs) have achieved strong performance on standard speech and audio understanding tasks, yet their ability to systematically generalize to novel task compositions remains underexplored. Taking a meta-learning view, we extend Text-to-LoRA (T2L) to LALMs, generating instruction-conditioned LoRA adapters with a Transformer hypernetwork rather than learning a single fixed adapter shared across instructions. To exploit fine-grained task information, we introduce in-conte...
  </details>

- **2026-10-25** — Runze Zhao — [Lie Symmetry-Guided Adaptive Sampling for Physics-Informed Neural Networks](http://arxiv.org/abs/2610.34345v1)
  <details><summary>📄 Abstract</summary>
  Physics-informed neural networks (PINNs) have emerged as a promising mesh-free framework for solving partial differential equations (PDEs), with broad applications in physics, engineering, and medicine. However, their performance is highly sensitive to the sampling strategy for training points. Conventional uniform sampling often fails to adequately resolve regions with complex solution features, leading to low efficiency and limited accuracy. To address these challenges, we propose a Lie symmet...
  </details>

- **2026-10-25** — Leonidas Daskalakis — [Pointwise ergodic theorems along oscillating sequences](http://arxiv.org/abs/2610.34301v1)
  <details><summary>📄 Abstract</summary>
  We establish the first pointwise convergence result for nonconventional ergodic averages modeled along a large class of oscillating sequences, treating, for example, orbits of the form $\big(\lfloor n^d\sin(eπn)\rfloor\big)_{n\in\mathbb{N}}$, $d\in\mathbb{N}$. More specifically, for every probability space $(X,\mathcal{B},μ)$ equipped with an invertible measure-preserving transformation $T\colon X\to X$ and every $f\in L^p_μ(X)$ with $p\in(1,\infty]$, we prove that the limit \[ \lim_{N\to\infty}...
  </details>

- **2026-10-25** — Mingrui Liu, Liang He, Xinchu Wang et al. — [Repairing Broken Access Control in Web Applications with LLMs: An Empirical Benchmark Study](http://arxiv.org/abs/2610.34290v1)
  <details><summary>📄 Abstract</summary>
  Broken access control (BAC) ranks among the most severe web-application vulnerability classes, yet its automated repair remains largely unexplored. Unlike memory-safety vulnerabilities, BAC is a logic vulnerability whose repair demands a deep understanding of an application's access-control model and business semantics, which traditional automated vulnerability repair techniques handle poorly. Large language models (LLMs) open a promising avenue for this problem, but no standard benchmark exists...
  </details>

- **2026-10-25** — Haocheng Zhang, Yang Liu, Mengzhen Liu et al. — [Synergizing Wireless Foundation Models and LLMs: A Multi-Task Framework for MA Systems](http://arxiv.org/abs/2610.34285v1)
  <details><summary>📄 Abstract</summary>
  While movable antennas (MAs) provide enhanced spatial flexibility through dynamic repositioning, they confront critical challenges in acquiring complete channel state information (CSI) and efficiently optimizing antenna positions. Encouragingly, wireless foundation models (WFMs) capture generalizable channel priors for high-quality CSI extrapolation, while large language models (LLMs) enable parameter-efficient, token-level optimization for wireless tasks. In this paper, we synergistically integ...
  </details>

- **2026-10-25** — Jingyuan Xu, Yuanhui Wu, Zhentian Zhang et al. — [Flexible Beamforming via Fluid Antenna Array: From Discrete to Continuous Array](http://arxiv.org/abs/2610.34169v1)
  <details><summary>📄 Abstract</summary>
  Fluid antenna arrays (FAAs) reconfigure their effective aperture by activating radiation ports from a dense set of candidate positions within a finite physical region, thereby offering geometry diversity beyond conventional fixed arrays. This paper studies arbitrary-direction far-field beam synthesis with a planar FAA. Since a fixed array adapts its beamforming weights on a predetermined spatial sampling structure, its ability to match desired beam patterns is limited when both the aperture and ...
  </details>

- **2026-10-25** — Wenhang Shi, Yiren Chen, Zhe Zhao et al. — [Self-Evolution Reasoner: Continuous Optimization via Policy-Intrinsic Exploration and Exploitation](http://arxiv.org/abs/2610.34137v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities. Compared to RLVR's scalar rewards, recent self-supervised on-policy distillation methods leverage denser supervision signals. However, both paradigms suffer from exploration bottlenecks, struggling to escape local optima when the policy fails to sample valid solutions. Relying on external demonstrations can bypass this issue; however, the off-polic...
  </details>

- **2026-10-25** — Prateek Kumar Rajput, Shahzeb Khan, El-Hacen Diallo et al. — [Securing Agent-Generated Code with Its Own Development History](http://arxiv.org/abs/2610.34098v1)
  <details><summary>📄 Abstract</summary>
  Pull requests written by coding agents can pass a project's test suite while omitting a guard or a validation step. To find the missing condition, a reviewer currently relies on static analysis of the final code. An agent-generated change, however, is accompanied by a development history that a human commit does not provide. The agent's trajectory records each edit together with the agent's stated assumptions, and structural differencing shows how each changed function evolved. We present TRACER...
  </details>

- **2026-10-25** — Aruna Mohan, Burcu Ozek, Or Zilbershot et al. — [QECGBERT: A Scalable ECG Foundation Model Based on Self-Supervised Language Learning via VQ-VAE Waveform Tokenization](http://arxiv.org/abs/2610.33964v1)
  <details><summary>📄 Abstract</summary>
  AI foundation models play a pivotal role in advancing heart disease diagnosis from electrocardiogram (ECG) data, particularly for rare diseases where the lack of sufficient labeled data hinders supervised learning. However, most self-supervised learning methods treat ECGs as generic sequence or image data without exploiting underlying physiological structure. To address this limitation, we propose QECGBERT, a self-supervised ECG language model that explicitly encodes physiological semantics by t...
  </details>

- **2026-10-24** — Kai Wei, Yuwen Cui, Kehan Shen et al. — [CVE-to-ATT&CK Mapping via Evidence-Constrained Ranking](http://arxiv.org/abs/2610.33924v1)
  <details><summary>📄 Abstract</summary>
  Mapping CVEs to MITRE ATT&CK techniques helps defenders translate vulnerability information into hypotheses about adversary behavior. Automating this mapping is challenging because relevant evidence is fragmented across heterogeneous security sources. In addition, ATT&CK techniques can be semantically similar, and existing annotations cover a highly long-tailed subset of the technique space. Existing supervised, retrieval-based, and LLM-based approaches therefore face limitations from closed-set...
  </details>

- **2026-10-24** — Katie Matton, Rosalind W. Picard, John Guttag et al. — [Counterfactual Test-Time Augmentation for Shortcut Removal in Language Models](http://arxiv.org/abs/2610.33904v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can exploit shortcuts, i.e., correlations present in training data that may not hold at test time. This can lead to poor predictions when correlations shift. Most existing solutions for removing shortcuts operate at training time, requiring labeled training data, model weight access, and significant computational resources. Here, we study the problem of test-time shortcut removal. We propose a family of counterfactual test-time augmentation (CTTA) methods: given an e...
  </details>

- **2026-10-24** — Kürşat Çakal, Suat Özdemir — [Securing Edge & Physical AI: Post-Quantum IoT Blockchain for Mission-Critical Cyber-Physical Agents](http://arxiv.org/abs/2610.33862v1)
  <details><summary>📄 Abstract</summary>
  Distributed Cyber-Physical Systems (CPS) and Edge AI networks increasingly depend on public-key authentication and key-establishment mechanisms that are vulnerable to cryptographically relevant Quantum Computers (QC). Shor's algorithm threatens widely deployed asymmetric primitives, while Grover's algorithm reduces the effective security margins of symmetric and hash-based mechanisms. Although Post-Quantum Cryptography (PQC) provides a migration path, its larger public keys, ciphertexts, and sig...
  </details>

- **2026-10-24** — Bashar Khoury, Shadi Omari, Assaf Schuster — [Learning What to Share: Expert Specialization for Time-Series Forecasting](http://arxiv.org/abs/2610.33822v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in multivariate forecasting is deciding what to share across channels and where to specialize. Mixture-of-experts models offer flexible sharing, yet it remains unclear how much of their forecasting gains comes from added capacity or expert allocation. Through controlled comparisons across eleven datasets and three backbones, we show that informative channel assignments improve forecasting beyond matched shared capacity and random allocation. On frozen transformer backbones, p...
  </details>

- **2026-10-24** — Doanh Le Thien, Viet-Thanh Nguyen, Pham Tri Quang et al. — [RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](http://arxiv.org/abs/2610.33807v1)
  <details><summary>📄 Abstract</summary>
  Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation. However, most benchmarks only evaluate them as open-world video generators, using Vision-Language Models (VLMs) that lack strict 3D spatial and kinematic reasoning. To bridge this gap, we introduce RoboWorM, a comprehensive, deployment-aware benchmark that leverages known hardware priors such as robot kinematic trees and fixed camera configurations, to systematically examine structural and spat...
  </details>

- **2026-10-24** — Francesco Crescenzo Grasso, Pietro Liguori, Roberto Natella et al. — [Enhancing LLM-Based Vulnerability Detection via Representation-Aware Logical Ensemble](http://arxiv.org/abs/2610.33756v1)
  <details><summary>📄 Abstract</summary>
  Automated vulnerability detection in C source code is a long-standing challenge, as traditional static analysis tools often trade precision for scalability and struggle with complex vulnerability patterns. Recently, large language models (LLMs) have shown promising results; yet, most approaches rely on a single code representation, implicitly assuming uniform suitability across vulnerability types. In this work, we systematically study LLM-based vulnerability detection under multiple code repres...
  </details>

- **2026-10-24** — Longhao Yan, Jinhao Liang, Kaidi Yang — [Human-Feedback-Guided Multi-Agent Inverse Reinforcement Learning for Interactive Driving Behavior Modeling](http://arxiv.org/abs/2610.33726v1)
  <details><summary>📄 Abstract</summary>
  Modeling human driving behavior is fundamental to understanding driver decision-making and supporting autonomous vehicles (AVs) in mixed traffic. Reward learning offers a principled way to infer the latent objectives behind driving behaviors, yet most existing methods are formulated in single-agent settings and treat surrounding vehicles as dynamic obstacles. Directly extending reward learning to multi-agent scenarios is difficult because the joint action space grows exponentially with the numbe...
  </details>

- **2026-10-24** — Francesco Crescenzo Grasso, Pietro Liguori, Roberto Natella et al. — [VulDec: Vulnerability Detection in Binaries via Neural Decompilation](http://arxiv.org/abs/2610.33716v1)
  <details><summary>📄 Abstract</summary>
  Automated vulnerability detection in binary executables is challenging due to the lack of source code and the limited semantic information available at the assembly level. Despite significant progress in machine-learning-based code analysis, the field still lacks methodologies and large, high-quality datasets that provide vulnerable code jointly at assembly- and source-level with precise vulnerability labels. To address this gap, we introduce VulDec, consisting of (i) a new large-scale, carefull...
  </details>

- **2026-10-24** — Andrea Morghen, Pierluigi Arpenti, Roberto Schiattarella et al. — [Quantum Closed Loop Inverse Kinematics Through Hilbert-Space Encoding of Robot Kinematics](http://arxiv.org/abs/2610.33715v1)
  <details><summary>📄 Abstract</summary>
  The integration of quantum computing into robotics requires mathematical representations that preserve the geometric structure and configuration dependence of robot motion. This paper introduces a structure-preserving quantum representation of rigid-body transformations and serial-manipulator kinematics, establishing a correspondence between classical kinematic models and parameterized quantum circuits. Building on the Bloch-sphere representation, spatial directions are encoded into single-qubit...
  </details>

- **2026-10-23** — Navyansh Mahla, Sashank Vandrangi — [ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents](http://arxiv.org/abs/2610.32752v1)
  <details><summary>📄 Abstract</summary>
  LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introd...
  </details>

- **2026-10-22** — Junzhe He, Kehan Wen, Chong Zhang et al. — [Humanoid Mobility via Attention-based Contacts](http://arxiv.org/abs/2610.31608v1)
  <details><summary>📄 Abstract</summary>
  Humanoid mobility over complex terrain requires accurate foot placement and coordinated whole-body motion capable of robust adaptation. Reinforcement learning (RL) policies trained without motion references generalize well across terrains, yet eliciting effective whole-body coordination through reward design and exploration alone remains challenging. In contrast, reference-based methods yield natural motions but struggle to adapt beyond the predefined trajectories in their training data. We intr...
  </details>

- **2026-10-22** — Hansi Abeynanda, Chathuranga Weeraddana, Carlo Fischione — [Effective Dual Subgradient Methods Through Sequential Subgradient-Aligned Rays](http://arxiv.org/abs/2610.31486v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an efficient subgradient-based framework, referred to as the sequential subgradient-aligned rays (SSAR) method, for improving the convergence performance of the dual subgradient method. In particular, the proposed method identifies and exploits a finite sequence of rays, when available, as the dual subgradient method evolves, along each of which a subgradient of the negative dual function remains constant and aligns with the ray. While the dual variable iterates remain ...
  </details>

- **2026-10-22** — Xiang Zhou, Xiangyu Zhu, Xintong Wang et al. — [Probabilistic Energy Modeling Unifies Versatile Swarm Control](http://arxiv.org/abs/2610.31371v1)
  <details><summary>📄 Abstract</summary>
  Robotic swarms must coordinate across diverse missions, yet existing controllers often require redesign, retuning, or retraining when objectives change. Here we show that probabilistic energy modeling provides a unifying representation for versatile swarm control, in which diverse missions emerge from compositions of shared interaction principles rather than task-specific control formulations. By exploiting the correspondence between Gibbs random field energy minimization and structured reward m...
  </details>

- **2026-10-22** — Lu Maltsis, Dominik Winterer — [Typed Template Fuzzing](http://arxiv.org/abs/2610.31342v1)
  <details><summary>📄 Abstract</summary>
  Fuzzing software with complex inputs has been a longstanding challenge. Traditionally, fuzzers either programmatically encode language constraints, requiring significant engineering effort, or rely on users to declare grammars and constraints. Recent LLM-based fuzzers address these drawbacks but introduce new issues. Some use LLMs for test generation, sacrificing throughput and producing invalid inputs when the LLM makes mistakes. Others rely on language-specific parsers, static analysis, and AS...
  </details>

- **2026-10-22** — Valentina Moskvina, Jaroslav Čapek, Michal Rameš et al. — [Mn-deficient Ni-Mn-Ga alloys: phase transitions, magnetic properties, and disappearance of martensitic transformation](http://arxiv.org/abs/2610.31206v1)
  <details><summary>📄 Abstract</summary>
  Composition gradients formed during directional solidification are generally considered undesirable in Ni-Mn-Ga magnetic shape-memory alloys. However, these gradients offer a highly effective platform for systematically investigating composition-property relationships under identical growth and heat-treatment conditions. To exploit this approach, one Mn-deficient and two near-stoichiometric Ni-Mn-Ga oligocrystals were grown by optical zone remelting and characterized by X-ray fluorescence mappin...
  </details>

- **2026-10-22** — Hui Li, Qihui Zhou, Xiao Yan et al. — [SARIA: Persistence-Aware KV Caching with Coordinated DRAM--SSD Reload for LLM Agents](http://arxiv.org/abs/2610.31169v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn LLM agents usually reuse long context prefixes, making key value (KV) caching crucial for reducing prefill latency. SSDs provide a low-cost extension to limited DRAM capacity but introduce two key challenges. Eagerly persisting all KV cache blocks incurs substantial write traffic and rapidly consumes finite SSD endurance. Meanwhile, the small number of SSDs provisioned in typical GPU servers limits aggregate reload bandwidth, making SSD-resident KV cache much slower to retrieve than t...
  </details>

- **2026-10-22** — Yuannuo Feng, Yubing Ye, Wenshuai Yao et al. — [SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding](http://arxiv.org/abs/2610.31120v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models generate multiple token positions in parallel, but few-step decoding makes parallel commitment difficult: tokens that appear reliable individually may be jointly inconsistent, while premature commitments can prevent later context-dependent refinement. In this paper, we introduce SetCommit, a training-free method for coordinated parallel token commitment. Instead of selecting tokens independently by confidence, SetCommit selects a commitment set that balances token relia...
  </details>

- **2026-10-22** — Noah Gießing, Ankit Satpute, Hamid Rahkooy et al. — [Formal-Informal Mathematical Alignment through and beyond Human Annotations](http://arxiv.org/abs/2610.31011v1)
  <details><summary>📄 Abstract</summary>
  Formalized mathematics libraries such as Lean's \texttt{mathlib} provide machine-verifiable representations of mathematical knowledge, including definitions, theorems, and their relationships. If effectively connected to informal mathematical resources, formal mathematics could help uncover previously implicit links between mathematical concepts and improve access to existing formalizations. However, connections between informal and formal mathematics libraries are currently sparse and unsystema...
  </details>

- **2026-10-22** — Valentino Maiorca — [The Geometry of Meaning in Neural Manifolds](http://arxiv.org/abs/2610.30938v1)
  <details><summary>📄 Abstract</summary>
  Just as different languages express the same concept through different words, neural networks express similar functions through incompatible coordinate systems. Different architectures, random initializations, and optimization trajectories produce incompatible parameterizations in extrinsic coordinates, obscuring functional relationships between independently trained models. When models independently solve similar tasks on related data, do their learned representations share exploitable structur...
  </details>

- **2026-10-22** — Mrityunjay Shukla, Shubham Roy, Biswabandan Panda — [Amplifying Latency and Cost of LLM Inference via Rowhammer Attack](http://arxiv.org/abs/2610.30798v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve high inference efficiency using optimized GPU kernels generated by just-in-time (JIT) compilation frameworks such as Triton. Triton compiles GPU kernels through an MLIR/LLVM-based pipeline. We investigate whether a Rowhammer-induced bit-flip in the CPU's DRAM can degrade GPU-based LLM inference performance while preserving output correctness. We present LLVMhammer, the first Rowhammer attack that causes LLM inference slowdown by inducing a bit-flip in Triton'...
  </details>

- **2026-10-22** — Farnoosh Hashemi, Shiyu Ji, Joice Chen et al. — [LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades](http://arxiv.org/abs/2610.30769v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic Music Lab experiment, we tested this vulnerability in large populations of LLM agents that recommended unfamiliar songs, with or without exposure to cumulative recommendation counts. Exposure led to runaway cascades that...
  </details>

- **2026-10-22** — Ruike Cao, Iwan Morton-Blake, Donglian Xu et al. — [Natural Chlorine Enhances Antineutrino Detection in the Deep Ocean](http://arxiv.org/abs/2610.30754v1)
  <details><summary>📄 Abstract</summary>
  Large-volume neutrino telescopes such as IceCube and KM3NeT exploit natural ice or water as detection media, but their sparse instrumentation makes MeV neutrino interactions difficult to identify individually. We show that chlorine naturally abundant in seawater provides an intrinsic neutron-capture target that enables efficient tagging of electron antineutrinos through inverse beta decay. In contrast to the 2.2 MeV $γ$-ray from neutron capture on hydrogen, capture on chlorine produces an $\sim$...
  </details>

- **2026-10-22** — John J. Vastola, Kanaka Rajan — [Solvable models of learning to pursue a moving target](http://arxiv.org/abs/2610.30721v1)
  <details><summary>📄 Abstract</summary>
  Agents tasked with intercepting a moving target must learn how to reach it, ideally as efficiently as possible. As observers of animal pursuit behavior have noticed, different strategies are possible: on one extreme, the agent reactively moves toward the target's current location; on the other, the agent predicts the target's future location and moves directly there. Motivated by the desire to understand how such strategies might be learned, we introduce a continuous-time linear-quadratic model ...
  </details>

- **2026-10-22** — Aijing Yu, Kuangpu Guo, Jian Liang et al. — [FedBST: Bilateral Self-Training for Unsupervised Federated Classification](http://arxiv.org/abs/2610.30634v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised federated learning with Vision-Language Models (e.g., CLIP) offers a promising solution for label-free classification, yet its performance often degrades under severe non-IID shifts. A pioneering method, FedCoPL, typically relies on self-training strategies that exclusively prioritize high-confidence predictions for pseudo-labeling. However, this selective approach neglects the information of ambiguous samples (often referred to as ``waist" samples), leading to the underutilization ...
  </details>

- **2026-10-22** — Wei Zhang, Lirong Xiang, Charles Fleming — [Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents](http://arxiv.org/abs/2610.30587v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in foundation-model agents have enabled increasingly capable embodied systems for long-horizon planning and interaction. However, embodied agents require fast, closed-loop decisions as they continuously perceive and act on a changing environment. Deploying strong cloud agents leaves the platform idle for seconds between consecutive actions, while lightweight local models respond quickly but are more vulnerable to errors. Existing hierarchical architectures typically assign models...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 66 papers

- **2026-10-26** — Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al. — [I-HITL: Inalienable Human-in-the-Loop](http://arxiv.org/abs/2610.35835v1)
  <details><summary>📄 Abstract</summary>
  Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the concept of inalienable human-in-the-loop (I-HITL). An I-HITL protocol ensures that an agent can initiate an action only with explicit human approval, even when the human interacts with a system (e.g., a local agentic harne...
  </details>

- **2026-10-26** — Gadi Evron — [Adversary Brains: Hypothesis-Based Logical Signatures for Threat Actor Detection with LLMs](http://arxiv.org/abs/2610.35624v1)
  <details><summary>📄 Abstract</summary>
  An adversary brain is an LLM-based model of a threat actor's behavior, held as an evolving logical signature: a hypothesis with enough structure that data can test it continuously, without a person re-interpreting it each time. Rather than any single observation, such as an IoC (Indicator of Compromise), it is the arrangement that becomes a detection, or intelligence, mechanism. Where YARA matches a file and Sigma matches a log line, an adversary brain matches the activity pattern of a campaign ...
  </details>

- **2026-10-26** — Harish Santhanalakshmi Ganesan — [Infinity Machine: a self-improving AI agent for research](http://arxiv.org/abs/2610.35579v1)
  <details><summary>📄 Abstract</summary>
  We present the Infinity Machine, a self-improving AI agent that we use for research on problems whose answers aprogram or data can check. Each candidate solution is produced by a full tool-using agent that works for up to an hour in a fresh sandbox; proposers see only a public score, and a private split decides what counts. The harness itself(prompts, tools, skills, playbook, meta agent) is an editable genome, changed only through a kernel-enforced gate with held-out and cost checks. An autonomo...
  </details>

- **2026-10-26** — Khaled M. Seyam, Julian Wiederer, Samar Fathalah et al. — [Model-Aware Generation of Safety-Critical Scenes for Robust End-to-End Driving via Distilled Planner Surrogates](http://arxiv.org/abs/2610.35448v1)
  <details><summary>📄 Abstract</summary>
  End-to-end driving models perform well on standard benchmarks but collide frequently in safety-critical scenarios. We present a failure-mode analysis on NeuroNCAP which shows that 95.9% of DiffusionDrive's collisions are planning failures despite reliable detection, pinpointing the bottleneck in planning rather than perception. We attribute this to a fundamental data imbalance, as safety-critical interactions are rare in real driving logs, so planners are hardly ever trained on them. We close th...
  </details>

- **2026-10-26** — Rene Heinzl, Markus Nissl — [SoK: Timestamps Are Not a Time Model: Rethinking Temporal Reasoning in Host-Based Intrusion Detection](http://arxiv.org/abs/2610.35151v1)
  <details><summary>📄 Abstract</summary>
  Host-based intrusion detectors order events, window audit streams and sequence attack stages by their timestamps. Every conclusion they draw therefore rests on assumptions about clocks, delivery, entity identity and the integrity of the evidence, and most of these assumptions go unstated. This Systematization of Knowledge (SoK) makes them explicit. Drawing on temporal databases, stream processing and runtime verification, we distill five components of a time model, together with a checklist of e...
  </details>

- **2026-10-26** — Muxi Diao, Wenbin Xu, Lele Yang et al. — [VibeVideoBench:Evaluating Multimodal Agents on Code-Driven Video Generation](http://arxiv.org/abs/2610.35864v1)
  <details><summary>📄 Abstract</summary>
  Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a ruleconsistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained tasks in English and Chinese span 12 categories, from data stories and music-driven...
  </details>

- **2026-10-26** — Fan Xu, Hao Wu, Zhi Song et al. — [CLOSURE: Cross-Channel Closure for Multivariate Time Series Anomaly Detection](http://arxiv.org/abs/2610.35753v1)
  <details><summary>📄 Abstract</summary>
  Multivariate time series produced by industrial installations and server clusters are under continuous monitoring, and anomaly detection is the first line of defense before a local fault escalates into a system-wide failure. In the absence of labels, the dominant paradigm trains a reconstruction model on normal data and scores the residual to reach a verdict. Recent work has steadily enriched the expressiveness of the recovery map through Transformers, diffusion models, and cross-scale associati...
  </details>

- **2026-10-26** — Šárka Uramová, Petar Kirilov Petrov, Josef Jon et al. — [ImgMT: Wikipedia-based Dataset For Evaluating Text-in-Image Translation](http://arxiv.org/abs/2610.35416v1)
  <details><summary>📄 Abstract</summary>
  Text-in-image translation aims to translate all textual content embedded in an image. In Text Image Translation (TIT), the output is translated text; In-Image Machine Translation (IIMT) additionally renders the translation back into the image. We introduce ImgMT, a massively multilingual dataset and benchmark mined from localized SVG illustrations on Wikimedia Commons, focusing on diagrams, maps, and infographics. ImgMT contains 35,612 aligned image pairs grouped into 1,855 image sets, spanning ...
  </details>

- **2026-10-26** — Erdal Aydin, Yaman Arkun — [Autonomous Structural Discovery Of Bioprocess Dynamics And Kinetics Via LLM-Driven Agents](http://arxiv.org/abs/2610.35391v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity digital twins in continuous biomanufacturing are often bottlenecked by incomplete kinetic models, while standard data-driven algorithms (e.g., SINDy, PINNs) lack interpretability or impose rigid physical assumptions. This paper introduces a hybrid closed-loop architecture for autonomous kinetic state-space discovery driven by a Large Language Model (LLM) agent. The framework employs a sequential "isolation-peeling" methodology across orthogonal operational regimes. This algorithmic...
  </details>

- **2026-10-26** — Sebastian Baltes, Christoph Treude — [Toward Evidence-Based Agentic Software Engineering](http://arxiv.org/abs/2610.35348v1)
  <details><summary>📄 Abstract</summary>
  Task success rates and execution costs of agentic coding tools depend on both model and harness. The harness manages context, provides tools, and runs the agent loop. In empirical software engineering (SE) studies, comparisons that change model and harness together cannot isolate their effects. We qualitatively annotated 325 experiments reported in 146 peer-reviewed full papers published between 2025 and 2026. We examined the reported configurations and whether comparisons isolated harness effec...
  </details>

- **2026-10-26** — Wei Shang, Zhiyuan Li, Shengfeng He — [Temporal Slice Learning for AI-Generated Video Detection with 400$\times$ Fewer FLOPs](http://arxiv.org/abs/2610.35148v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative video models have improved visual realism, making detection increasingly dependent on subtle temporal inconsistencies. However, these signals are weak and spatially localized, while most of the video content is redundant. This creates a fundamental mismatch: existing detectors rely on heavy backbones to model full videos, which leads to high computational cost and limited scalability. In this work, we rethink AI-generated video detection from a representation perspe...
  </details>

- **2026-10-26** — Fanqi Lin — [A complete parameter classification of left-invariant Bott affine Ricci solitons for two rotated distributions on three-dimensional Lorentzian Lie groups](http://arxiv.org/abs/2610.34835v1)
  <details><summary>📄 Abstract</summary>
  We classify all left-invariant affine Ricci solitons associated with the Bott connections of two fixed rank-two distributions on the seven standard families of three-dimensional Lorentzian Lie groups. The distributions are defined by a fixed orthogonal change of the spacelike frame. A universal adapted-frame calculation provides explicit connection matrices, curvature operators and the symmetrized Ricci tensor. The equation in the orthogonal-complement direction forces every left-invariant solut...
  </details>

- **2026-10-26** — Pier Mattia Basciano, Gianvito Antenori, Cristiano Andolfi et al. — [NeSySpec: Neuro-Symbolic Technical Intelligence for Auditing Engineering Specifications with an Application to Aircraft](http://arxiv.org/abs/2610.35403v1)
  <details><summary>📄 Abstract</summary>
  Engineers who audit a declared specification of an engineered system need to know which physical constraints it respects, which it violates, which field was altered and how to correct it. NeSySpec is an integrated and interpretable neuro-symbolic audit framework, built on Logic Tensor Networks, that answers these questions in one pipeline. Its axioms encode the physical relations of the domain as differentiable graded predicates whose tolerances are learned from a fleet of real records; from the...
  </details>

- **2026-10-26** — Van Kwan Zhi Koh, Songnan Lin, Rongmo Luo et al. — [AdaTrendLike: Adaptive Hierarchical Detrending and Trend Likelihood Scoring for Time Series Anomaly Detection](http://arxiv.org/abs/2610.35400v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Industrial Internet of Things devices has led to increasingly large-scale and non-stationary time-series data, posing significant challenges for time-series anomaly detection (TSAD). Existing approaches often focus on reconstructing or forecasting observations while overlooking the role of trend dynamics, which constitute a major source of non-stationarity and contain valuable information for anomaly identification. To address this limitation, we propose AdaTrendLike, ...
  </details>

- **2026-10-26** — Yin Zhang, Yaoyue Zheng, Yongqiang Zhang et al. — [GIFT: Representation Geometry Matters for Single-Domain Generalized Object Detection](http://arxiv.org/abs/2610.35374v1)
  <details><summary>📄 Abstract</summary>
  Single-Domain Generalized Object Detection (S-DGOD) aims to generalize from a single source domain to unseen domains under distribution shifts. Existing efforts mainly focus on simulating unseen domains or suppressing domain-specific factors. However, they largely overlook the intrinsic generalization capability embedded in Vision Foundation Models (VFMs). In this work, we show that unconstrained fine-tuning disrupts the geometric structure of pre-trained representations, which encodes domain-in...
  </details>

- **2026-10-26** — Shaked Rosenblum, Teddy Lazebnik, Ziv Ben-Zion — [Being judged through the record: A Rosenhan-inspired test of psychiatric label sensitivity in large language models](http://arxiv.org/abs/2610.35326v1)
  <details><summary>📄 Abstract</summary>
  The integration of large language models (LLMs) into clinical decision-making raises unresolved questions regarding diagnostic bias. We investigate whether a documented psychiatric history alters LLM recommendations when the current clinical evidence is identical. Using a counterfactual experiment inspired by Rosenhan's 1973 field study, we factorially varied diagnostic-history condition (no prior diagnosis stated vs. prior schizophrenia diagnosis) and current-evidence condition (voices ceased v...
  </details>

- **2026-10-26** — Yi-Ming Yin, Ming-Yao Cui, Ling-Yu Du et al. — [Spectral fingerprint recognition of mobile signals via Rydberg atomic sensors](http://arxiv.org/abs/2610.35301v1)
  <details><summary>📄 Abstract</summary>
  Rydberg-atom sensors have emerged as a promising quantum technology for broadband radio-frequency detection owing to their intrinsic calibration, wide frequency coverage, and high sensitivity. However, their potential for intelligent identification of real-world wireless signals remains largely unexplored. Here, we demonstrate a quantum-enabled framework for mobile signal classification based on Rydberg electromagnetically induced transparency spectroscopy and deep learning. Three types of wirel...
  </details>

- **2026-10-26** — Cristhian Moya-Mota, Ignacio Aguilera-Martos, Diego García-Gil et al. — [LEAP: a Latent Embedding Anomaly Patch-Transformer for time-series anomaly detection](http://arxiv.org/abs/2610.35190v1)
  <details><summary>📄 Abstract</summary>
  Time-series anomaly detection is dominated by reconstruction-based neural detectors, whose objective is structurally flawed. Since the target is also the input, an expressive model can learn to reconstruct anomalies too, leaving uninformative residuals. Recent large-scale benchmarks show that, on curated data, elaborate deep detectors rarely beat simple statistical baselines, while current leaders rely on representation learning. We propose LEAP (Latent Embedding Anomaly Patch-Transformer), whic...
  </details>

- **2026-10-26** — Ivana Crescenzi, Arianna Muti, Maarten Sap et al. — [RAGing Against Misogyny: Improving Implicit Misogyny Explanations](http://arxiv.org/abs/2610.35094v1)
  <details><summary>📄 Abstract</summary>
  Implicit misogyny often requires background knowledge to be understood. To address this challenge, we propose a Retrieval-Augmented Generation (RAG) framework for detecting and explaining implicit misogyny in English and Italian, leveraging encyclopedic, slang and feminist knowledge sources. Using the ImplicIT-Mis and SBIC+ datasets, we evaluate the contribution of each knowledge source to detection and explanation quality, investigating also whether RAG addresses known LLM failure modes in impl...
  </details>

- **2026-10-26** — Mayur Kulkarni — [Reason or Recite: Complementary Specialists with an LLM Judge for Traffic Anomaly Reasoning](http://arxiv.org/abs/2610.34993v1)
  <details><summary>📄 Abstract</summary>
  Road anomalies such as collisions, violations, and sudden hazards demand more from video understanding than detection: a practical system must verify what happened, describe the scene, and explain the cause. We find these competences pull in opposite directions for vision-language models: closed-form questions reward precise, evidence-grounded reasoning, while open-ended answers are scored by similarity to reference text, where matching the annotation style matters as much as reasoning correctly...
  </details>

- **2026-10-26** — Chenrui Ji, Jiafan Lu, Zilu Luo et al. — [SGDB: Semantic-Geometric Decoupling and Evidence Binding for Logical Anomaly Detection](http://arxiv.org/abs/2610.34897v1)
  <details><summary>📄 Abstract</summary>
  Logical anomaly detection requires recognizing scene components and measuring whether their configuration satisfies task constraints. Correct identities can coexist with inaccurate geometry; clean mask fragments can yield misleading lengths. We propose Semantic-Geometric Decoupling and Evidence Binding (SGDB). A semantic decoder learns object identities from component-annotated normal sources and factual edits; a separate reader supplies final measurements. Partial one-to-one association binds g...
  </details>

- **2026-10-25** — Federico Felizzi, Francesco Andrea Causio, Bianca Destro Castaniti et al. — [Conviction Without Evidence: Verdict Stability Is Independent of Visual Grounding in Medical Vision--Language Models](http://arxiv.org/abs/2610.34520v1)
  <details><summary>📄 Abstract</summary>
  Vision--language models applied to medical question answering can reach correct diagnoses without using the diagnostic image, inferring instead from the clinical vignette. We ask whether this is visible in how \emph{firmly} a model holds its answer: does a model defend a diagnosis derived from a blank placeholder as tenaciously as one derived from a real medical image? Crossing an image-substitution protocol with two levels of adversarial pressure on 60 Italian State Examination items, we find n...
  </details>

- **2026-10-25** — Chih-Wei Huang, Hsin-Chieh Lee, Yun-Chen Yu et al. — [BE-CTDE: Blockchain-Enabled Multi-Agent Reinforcement Learning with Anomaly Detection and Token Economics](http://arxiv.org/abs/2610.34121v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reinforcement learning supports cooperative decision-making in Internet of Things systems, but strategic deviations can disrupt coordination and undermine confidence in the training process. This paper proposes Blockchain-Enabled Centralized Training and Decentralized Execution (BE-CTDE), which uses blockchain as an active training-management layer. A behavioral verifier compares executed trajectories with shared-policy recommendations; its flags drive a token mechanism combining sla...
  </details>

- **2026-10-25** — Daniel Ben-Levi, Judah Goldfeder, Mateusz Dziemian et al. — [Back to Basics: Formal Analysis Hints Improve Weak-to-Strong Monitoring](http://arxiv.org/abs/2610.34064v1)
  <details><summary>📄 Abstract</summary>
  Frontier agentic systems are capable of taking misaligned actions that may cause significant harm. Monitoring techniques are developed to oversee these systems in order to detect and prevent dangerous actions. However, current state-of-the-art monitors suffer from four persistent failure modes: complete detection failures, partial detections, accepting false benign framings, and suspicion score calibration errors. These failure cases can be efficiently combated by augmenting transcripts with sup...
  </details>

- **2026-10-25** — Achyut Manoj, Advai Aiyer, Andrew Lee et al. — [No Value Is Better Than a Wrong Value: Finding and Handling Erroneous Data in Literature-Mined Datasets for AI](http://arxiv.org/abs/2610.34642v1)
  <details><summary>📄 Abstract</summary>
  Machine learning across materials science, chemistry, energy, and medicine increasingly relies on literature-extracted datasets due to a lack of curated databases. However, automated extraction introduces errors: text recognition misreads digits, units and notations are confused, values are misattributed, and LLMs hallucinate numbers. Drawing on our work building an electro-optic property database, we present a taxonomy of errors organized by their origin and signatures, alongside a layered fram...
  </details>

- **2026-10-25** — Amine Barrak, Emna Ksontini, Charles Wehbe — [Do AI Coding Agents Write Infrastructure as Code Like Humans? An Empirical Study of GitHub Pull Requests](http://arxiv.org/abs/2610.34613v1)
  <details><summary>📄 Abstract</summary>
  Infrastructure-as-Code (IaC) configurations define cloud resources, networking, and access control, and AI coding agents increasingly write them. Little is known about how agent contributions differ from those of humans and automation bots, how maintainers evaluate them, and whether they introduce different sustainability concerns.   We study 349,156 IaC pull requests (PRs) from 49,241 GitHub repositories, distinguishing humans, automation bots, silent agents, and disclosed agents. Bots account ...
  </details>

- **2026-10-25** — Orel Navi, Elad Feldman, Ben Nassi — [LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards](http://arxiv.org/abs/2610.34542v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents have been observed acting beyond their assigned tasks, accessing unauthorized systems, and establishing communication channels to exchange information, yet the Web and network-level techniques they use to extend their capabilities and circumvent security restrictions remain poorly understood. We study these techniques through the ProWiki incident, in which agents restricted to outbound HTTP GET requests repurposed a public German-language wiki as a message board. We analyze 14,...
  </details>

- **2026-10-25** — Heng Zhang, Ziyang Zuo, Guoxiang Zhao et al. — [DSGN: A Dual-Stream Gated Network for Scalable Simultaneous Surveillance and Containment](http://arxiv.org/abs/2610.34084v1)
  <details><summary>📄 Abstract</summary>
  The simultaneous surveillance and containment (SSC) problem arises in multi-robot applications such as perimeter security and environmental monitoring, where robots must survey a region of interest and coordinate to enclose targets once they are detected. Surveillance favors spatial dispersion for coverage, whereas containment requires target-centric cohesion for enclosure. This conflict makes heuristic switching unstable, and the instability becomes more pronounced as larger robotic networks in...
  </details>

- **2026-10-25** — Constantinos Papantoniou, Brian Hilton — [Agentic AI Orchestration Framework for Spatial Intelligence: Supply Chain Deployment](http://arxiv.org/abs/2610.34569v1)
  <details><summary>📄 Abstract</summary>
  Industrial spatial decisions are assembled across systems that share neither a reference frame nor an owner, and analysts spend substantial effort reconciling those systems rather than reasoning about space. This paper presents ANASSA, a reference architecture integrating structured reasoning, multi-agent workflow orchestration, authoritative spatial grounding, and feedback-driven execution, and reports its instantiation in an operating supply-chain deployment. The architecture places typed data...
  </details>

- **2026-10-25** — Carlo R. Contaldi — [Is the arXiv Apocalypse upon us? A break in preprint growth coincident with agentic AI](http://arxiv.org/abs/2610.34449v1)
  <details><summary>📄 Abstract</summary>
  As an experiment in agentic assisted analysis, we used an agentic AI model to analyse the effect of agentic AI on arXiv submissions; data acquisition, analysis and the first draft were carried out by the model under the author's direction. Monthly arXiv submissions have grown exponentially for three decades, at about $9\%$ per year. Fitting a piecewise log-linear trend with seasonal modulation to the full record, we find two post-pandemic breaks in growth rate. The first, in mid-2022, precedes C...
  </details>

- **2026-10-25** — Yin-Long Liu, Yuanchao Li, Jiahong Yuan et al. — [ADReasoner: Acoustic-Linguistic Cue-Aware Reinforcement Learning for Explainable Alzheimer's Disease Detection from Speech](http://arxiv.org/abs/2610.34220v1)
  <details><summary>📄 Abstract</summary>
  Speech-based Alzheimer's Disease (AD) detection holds significant promise due to its scalable and non-invasive nature. However, current Speech Large Language Models (SpeechLLMs), similar to conventional AD detection systems, still treat AD detection primarily as a simple categorical classification task. This paradigm provides limited interpretability of predictions, while leaving the inherent expressiveness and reasoning capabilities of SpeechLLMs largely underutilized. In this work, we take the...
  </details>

- **2026-10-25** — Yamin Li, Ruidong Zhang, Anran Wang et al. — [AudioFM: Towards General Purpose Audio Representation Learning](http://arxiv.org/abs/2610.34183v1)
  <details><summary>📄 Abstract</summary>
  Learning audio representations that effectively bridge holistic global soundscapes with fine-grained acoustic moments is a long-standing goal in self-supervised learning. Recording-level contrastive objectives encourage agreement between pooled audio representations, but do not explicitly supervise local time-frequency representations. We introduce AudioFM, a self-supervised framework that combines recording-level contrast with patch-wise masked latent discrimination. Using visible acoustic cont...
  </details>

- **2026-10-24** — Georgios Feretzakis, Alexandros Papaspyridis — [Trust Mechanisms for Offline Generative AI at the Edge: A Connectivity-Regime Framework and an Empirical Study on a Raspberry Pi 5](http://arxiv.org/abs/2610.33732v1)
  <details><summary>📄 Abstract</summary>
  Generative AI and large language models (LLMs) are moving into the Internet of Things, yet most deployments assume cloud connectivity, and many IoT settings have intermittent, restricted, or no connectivity. We propose a connectivity-regime framework (C0-C4), a taxonomy of inference-time trust mechanisms, and signed, versioned knowledge packs as the update channel for disconnected regimes, and evaluate them on a Raspberry Pi 5 running fully local retrieval-augmented generation under network isol...
  </details>

- **2026-10-24** — Yiran Zeng, Giacomo Frisoni, Lorenzo Molfetta et al. — [Are We Done with UMLS Injection into Language Models for Medical Question Answering?](http://arxiv.org/abs/2610.33801v1)
  <details><summary>📄 Abstract</summary>
  Maybe not. The Unified Medical Language System (UMLS) has become an oracle for millions of clinicians and health system developers worldwide. Researchers have increasingly used knowledge graphs derived from UMLS to enhance language models' factual accuracy and reasoning traceability in high-stakes tasks. Medical Question Answering (MQA) is a prime testbed for integration, with benchmarks usually involving professional exercises such as disease diagnosis and drug prescription from patient history...
  </details>

- **2026-10-24** — Xiang Li, Aichun Huang, Zuyao Xu et al. — [Ring-0 by Default: Agents as Operating Systems (AaOS)](http://arxiv.org/abs/2610.33753v1)
  <details><summary>📄 Abstract</summary>
  LLM agents now read and write files, start processes and subagents, fetch network content, load third-party extensions, and save and resume state, which are the responsibilities of an operating system. They gained these functions within about three years, but not the protections that operating systems built over five decades: whatever the model outputs, whether it follows the user, a tool result, or a downloaded skill, runs with the full authority of the host user, in effect at ring 0. Prior wor...
  </details>

- **2026-10-24** — Nadun Rajapaksha, Sandun Herath, Devnith Wijesinghe et al. — [PathKGen: Pathology Knowledge Assisted MLLM for Explainable Histopathology](http://arxiv.org/abs/2610.33691v1)
  <details><summary>📄 Abstract</summary>
  Whole Slide Image (WSI) analysis serves as the fundamental method for the clinical diagnosis of cancer in digital histopathology. Recent advances in Multimodal Large Language Models (MLLMs) have enabled state-of-the-art (SOTA) automated histopathology report generation. However, MLLMs reason purely through distributions encoded in their neural parameters, limiting the amount of knowledge and reasoning logic they can contain given the model scale. Their black-box reasoning poses another challenge...
  </details>

- **2026-10-24** — Axel Abels, Elias Fernández Domingos, Tom Lenaerts — [Jointly Modeling Preferences and Imperfect Decision-Making in Large Language Models](http://arxiv.org/abs/2610.33651v1)
  <details><summary>📄 Abstract</summary>
  Do preferences Large Language Models (LLMs) express in standard elicitation tasks predict their strategic behaviour? LLM agents interacting with humans and other AI systems face potentially conflicting objectives, such as individual welfare, group welfare, and environmental concerns. Prior work characterizes LLM preferences through behavioral-economic and psychological elicitation or strategic games, but rarely tests consistency across settings and prediction in other strategic environments. Thi...
  </details>

- **2026-10-24** — Josef Liyanjun Chen — [RoboJev: An Open Vision-Language Judge for Robot Success Detection](http://arxiv.org/abs/2610.33718v1)
  <details><summary>📄 Abstract</summary>
  Many robot manipulation videos do not indicate whether the task was successfully completed. RoboJev-27B is an open-weight vision-language model that takes a task instruction, 10 frames of a manipulation attempt, and (if available) final frames from auxiliary cameras and predicts whether the robot accomplished the task. RoboJev-27B is a variant of JEV-27B-VL, trained with a rank-32 LoRA adapter on the language model only (keeping the vision encoder frozen) using 52,598 episode records. It also us...
  </details>

- **2026-10-24** — Johnny Garcia, Nicolas Salguero, Naveed Iqbal et al. — [Energy-Based Fault Detection and Isolation Framework for Flat Port-Hamiltonian Mechanical Systems](http://arxiv.org/abs/2610.33679v1)
  <details><summary>📄 Abstract</summary>
  Fault diagnosis during regulated motion requires informative signals even when feedback attenuates tracking deviations. This paper develops an energy-based diagnostic framework that constructs mechanical port-power residuals without a dedicated dynamic observer. Spectral Hamiltonian Algebraic Power Evaluation (SHAPE) combines port-Hamiltonian variables and differential flatness to generate nominal power references from planned motion for fully actuated mechanical systems with collocated actuatio...
  </details>

- **2026-10-24** — Dmitry Popov, Roman Bokhyan, Ekaterina Enikeeva et al. — [Beyond Prompts: A Systematic Study of LLM-Based Machine Translation Evaluators](http://arxiv.org/abs/2610.33741v1)
  <details><summary>📄 Abstract</summary>
  LLM-based evaluators have rapidly become a standard tool for machine translation evaluation, yet the design choices that shape their behavior remain poorly understood. We present a systematic study of how instruction design, few-shot demonstrations, backbone model choice, and multi-step workflows affect span-level and ranking-based MT evaluation. We collect new expert RATE annotations on WMT24 and WMT25 English-Russian translations, with transfer validation on MQM- and ESA-annotated benchmarks a...
  </details>

- **2026-10-23** — Jiedan Tan, Fang Liu — [AFRA: Age-Threshold Frame-Based Random Access for Timely Communication in Multi-Agent Systems](http://arxiv.org/abs/2610.32785v1)
  <details><summary>📄 Abstract</summary>
  Timely state updates are essential for coordination and monitoring in multi-agent systems, such as teams of mobile robots exchanging state information. When agents share a wireless channel, collisions and slow convergence of distributed access schemes can degrade information freshness over finite operating periods. This paper proposes age-threshold frame-based random access (AFRA), a distributed medium access control protocol for minimizing age of information (AoI). Once its age reaches a thresh...
  </details>

- **2026-10-23** — Yves Delley, John Coller, Zachary Cutts et al. — [Semantic Representation for Agentic Self-Play in Automated Laboratories](http://arxiv.org/abs/2610.32755v1)
  <details><summary>📄 Abstract</summary>
  Navigating complex, high-dimensional biological search spaces necessitates scalable physical and computational intelligence to explore beyond local optima through iterative self-play across ideation, experimentation, and automation. Translating experimental designs into reliable physical execution remains bottlenecked by static laboratory automation and unmodeled physical variability. To address this, we introduce VERified Infrastructure for Discovery Laboratories, or VERID, a foundational infra...
  </details>

- **2026-10-23** — Zenghui Zhou, Xiaoke Fang, Zheng Zheng — [LGMT: A Tool for Testing the Logical Reasoning Reliability of LLMs](http://arxiv.org/abs/2610.32627v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly serve as reasoning components in modern software systems, yet a model that answers a logical query correctly can contradict itself when the same problem is restated in an equivalent form. Static benchmarks evaluate queries in isolation and therefore fail to expose such inconsistencies. To address this limitation, we present LGMT, an open-source tool that detects reasoning inconsistencies through metamorphic relations grounded in first-order logic. Given ...
  </details>

- **2026-10-23** — Tarunya Prasad, Bharatesh Chakravarthi — [MiD-VLM: Detecting and Grounding Global Semantic Misinformation in Image-Caption Pairs](http://arxiv.org/abs/2610.32967v1)
  <details><summary>📄 Abstract</summary>
  Semantic misinformation can arise when an authentic image is paired with a caption that changes or distorts its narrative. Because the image itself may contain no visible signs of manipulation, methods designed to detect pixel-level artifacts can miss these misleading image-caption pairs. We study this problem using DGM4+, a dataset designed to evaluate the detection of global scene and semantic inconsistencies. We propose a multimodal model that combines image-text representations from SigLIP w...
  </details>

- **2026-10-23** — Yichun Peng, Yansong Li, Jin Hou et al. — [OpenStripe supports open-set identification and spatial stripe profiling in wild Amur tigers](http://arxiv.org/abs/2610.32848v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive camera-trap monitoring of endangered wildlife requires open-set individual identification---grouping field images into identities without predefined classes or a known population size---yet pose deformation and cluttered backgrounds complicate image comparison. Here, we present OpenStripe, a multi-agent framework that reconstructs canonical two-dimensional (2D) tiger torso patterns and encodes four interpretable local stripe structures: breakpoints, bifurcations, irregular structure...
  </details>

- **2026-10-22** — Ali Al-Lawati, Elsayed Eshra, Dongwon Lee et al. — [Diffusion Language Models for Perplexity-Aware Black-Box Attacks](http://arxiv.org/abs/2610.31558v1)
  <details><summary>📄 Abstract</summary>
  \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this...
  </details>

- **2026-10-22** — Arnon Mazza, Elad Levi — [SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs](http://arxiv.org/abs/2610.31062v1)
  <details><summary>📄 Abstract</summary>
  Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable predictions. Neurosymbolic methods offer a natural alternative, decomposing the policy into narrow neural decisi...
  </details>

- **2026-10-22** — Yifan Wang, Dongliang Xu, Xiaoyong Li et al. — [SecLog-Bench: A Scalable Benchmark for Cybersecurity Log Reasoning with Scaffolded Evidence](http://arxiv.org/abs/2610.31000v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential for cybersecurity, leading to growing interest in LLM-based automated cybersecurity log analysis. However, current datasets (1) are limited in scale; (2) rely mainly on single-source evidence; and (3) have only binary or multi-class attack labels, without dense annotations of the reasoning process. To address these limitations, SecLog-Bench has three key features. First, we build an extensible simulation platform that covers 29 attack scen...
  </details>

- **2026-10-22** — Ke Zhu, Yanli Chen, Ling Xiong et al. — [HiMark: Hierarchical and Controllable Multi-bit Watermarking for Large Language Models](http://arxiv.org/abs/2610.30601v1)
  <details><summary>📄 Abstract</summary>
  With the rapid adoption of large language models (LLMs) in text generation applications, it has become increasingly difficult to trace generated content and assign responsibility for its use, raising concerns about provenance, copyright protection, and accountability. Multi-bit watermarking addresses these issues by embedding multi-bit provenance information into generated text, but reliable extraction remains difficult due to sparse per-bit evidence and the trade-off between watermark-extractio...
  </details>

- **2026-10-22** — Bayram Ayadi, Florian Geissler, Johanna Schmidhuber — [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](http://arxiv.org/abs/2610.31467v1)
  <details><summary>📄 Abstract</summary>
  As wearable and digital health systems increasingly generate longitudinal physiological records, communicating these observations in patient-accessible language remains a significant challenge. Large Language Models (LLMs) offer a promising mechanism for translating structured clinical information into readable narratives, but this process may introduce semantic drift, where clinically precise meaning is distorted during simplification. We investigate evidence-grounded health summarization for m...
  </details>

- **2026-10-22** — Ruicong Liu, Liangyang Ouyang, Fengbo Lan et al. — [AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark](http://arxiv.org/abs/2610.31466v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and timing intact.   Our AnyGameRenderer generalizes across a wide range of genres tha...
  </details>

- **2026-10-22** — Bastien Le Guellec, Su Hwan Kim, Raphael Bentegeac et al. — [Major Revision, Minor Accountability: LLMs as Reviewers of Published Articles in Top-Tier Journals](http://arxiv.org/abs/2610.31414v1)
  <details><summary>📄 Abstract</summary>
  With the growth of scientific output, the peer review system is approaching a breaking point: reviewers are increasingly hard to secure, and turnaround times lengthen accordingly. LLM-assisted or LLM-generated peer review has been proposed as a remedy, but how such models would treat manuscripts already published in top-tier journals, the closest thing the current system has to a gold standard of scientific validity, is not known. Here we assembled a corpus of 200 articles, each released under a...
  </details>

- **2026-10-22** — Arsalan Jalil Sarghaleh, Mehdi Hazrati — [Auditing the Hand-Written Inputs of Learned Access Control](http://arxiv.org/abs/2610.31388v1)
  <details><summary>📄 Abstract</summary>
  Learned access control is typically deployed behind two hand-built artefacts: a hard-deny set enforced by a small trusted shield, and a region map that decides which requests mined rules answer and which the learner answers. Verifying the shield or measuring the learner validates neither. We audit both on the five public ABAC Lab policies. First, we formalise hard-deny soundness and check it exhaustively over relations of up to 794,250 tuples. Clauses that faithfully transcribe an explicit restr...
  </details>

- **2026-10-22** — Zhiyuan Li, Yuge Zhang, Jie Chen et al. — [From Signals to Evidence: Interpretable Underwater Acoustic Target Sensing with Large Language Models - Part II: Passive Detection](http://arxiv.org/abs/2610.31346v1)
  <details><summary>📄 Abstract</summary>
  Underwater acoustic passive detection is essential to maritime surveillance and intelligent ocean sensing. Existing detection systems typically collapse multichannel array observations into a binary decision or a scalar confidence score, offering limited insight into the physical evidence that supports or contradicts a target declaration. This limitation is acute at low signal-to-noise ratio (SNR), where isolated spectral peaks and transient beamforming responses are inherently ambiguous and phy...
  </details>

- **2026-10-22** — Changseon Yu, Hyeokjun Kweon — [ReCoG: Relational Concept Graph for Training-Free Personalization](http://arxiv.org/abs/2610.31282v1)
  <details><summary>📄 Abstract</summary>
  Training-free personalization adapts a frozen vision-language model (VLM) to recognize user-defined concepts from only a few exemplars by retrieving concept entries at inference time. While recent retriever-based methods enrich each concept with descriptive evidence, they largely treat concepts in isolation, so the retrieved information can be plausible yet non-discriminative, especially when the personalized concept set contains highly confusable, fine-grained categories. We argue that personal...
  </details>

- **2026-10-22** — Zhilong Fang, Qi Zhang, Jujie Yan et al. — [GeoAgent: Contract-Constrained LLM Agents for Seismic Data Processing](http://arxiv.org/abs/2610.31096v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can drive scientific software through function calling, but free-form tool use is fragile on long, data-dependent processing chains. Models omit arguments, invent units, feed the previous artifact into the wrong input, and report completion without a verifiable product. We present GeoAgent, an agent system for seismic data processing built on Madagascar's roughly 1{,}965 command-line programs. GeoAgent exposes 54 operator agents (51 generated from a declarative speci...
  </details>

- **2026-10-22** — Haeun Yu, Geert Heyman, Pepa Atanasova et al. — [A Reality Check of Inference-Time Context Augmentation Methods](http://arxiv.org/abs/2610.30983v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often fail to utilise the context given in the input, resulting in hallucinations or a fallback to parametric knowledge. Context augmentation methods aim to improve model performance by modifying the input, from inserting filler tokens that add computational time to adding relevant content such as elaboration of a context during inference. However, these methods have been evaluated in isolation and only by their performance gains, leaving it unclear how they compare ...
  </details>

- **2026-10-22** — Luong Tuan Thanh, Abhijit Sanyal — [REGATTA: A Cross-Domain Measurement Framework and Fault-Injection Harness for Enterprise AI Agents](http://arxiv.org/abs/2610.30924v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI-agent evaluation needs evidence about whether test suites expose specified faults and whether their reference rules are trustworthy. We introduce REGATTA (Regulatory Evaluation of Agents via Two-stage Testing and Assurance), a measurement framework with three instruments. A 125-item source-cited checklist spans five industry-by-jurisdiction cells across the United States and Vietnam. A 25-fault corpus covers five categories, and a harness scores suite-level fault detection at the d...
  </details>

- **2026-10-22** — Viet-Thanh Pham, Thuy-Trang Vu, Junae Kim et al. — [UniGuard: Multi-View Guardrail Learning for Cross-Interface Safety Generalization](http://arxiv.org/abs/2610.30742v1)
  <details><summary>📄 Abstract</summary>
  Guardrail models are increasingly used as safety layers for LLMs and agentic systems, but most are trained on fixed prompt or response interfaces and become unreliable when the same safety case appears as a conversation, agent trajectory, multi-agent trace, or policy-conditioned input. We propose UniGuard, a training framework that learns interface-invariant safety representations from multiple semantically aligned views of the same safety case. We also construct the UniGuard-FT dataset by trans...
  </details>

- **2026-10-22** — Chenhan Lyu, Kit Wislocki, Sarah Elizabeth Stoeckl et al. — [From Clinical Judgment to Checkable Rules: Clinician-Led Guardrails for Mental-Health Chatbots](http://arxiv.org/abs/2610.30690v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) deployed in mental-health contexts can be evaluated for safety failures, but the resulting judgments are often difficult to inspect or explain. Common approaches to improving safety rely on prompt engineering, LLM-as-a-Judge, and Constitutional AI. In this work, we describe a clinician-led alternative in which two clinicians define, finalize, and adjudicate the four safety checks of a rule base, which is formally verified for internal consistency and applied as a gua...
  </details>

- **2026-10-22** — Yuchen Wu, Jerry Wei — [Scaling Laws for Safety Probes](http://arxiv.org/abs/2610.30678v1)
  <details><summary>📄 Abstract</summary>
  Safety probes trained on a model's activations are a standard tool for monitoring language models in real time. Each time a new model is released or a new harm area needs to be monitored, the probe must be retrained, which requires new labels and a choice of probe architecture. Yet neither the model nor the labels tell us in advance how well the resulting probe will perform. Finding out requires training and comparing many probe configurations. In this paper, we ask whether probe performance can...
  </details>

- **2026-10-22** — Zhijie Zhong, Zhiwen Yu, Pengyu Li et al. — [Future of Time Series Anomaly Detection: From Historical Review to Unified Outlook](http://arxiv.org/abs/2610.30628v1)
  <details><summary>📄 Abstract</summary>
  Time series anomaly detection (TSAD) is a foundational problem in data mining, aiming to identify observations that deviate significantly from nominal temporal patterns. Driven by escalating data volumes and application complexity, recent research has yielded diverse architectures, including diffusion models, state space models, and large language models (LLMs). However, existing surveys provide limited coverage of these emerging designs and lack a unified treatment of multivariate anomalies, cr...
  </details>

- **2026-10-22** — Qian Chen, Saatvik Pradhan, Janice Ahn et al. — [Beyond Better Ideas: How Human-AI Collaboration Shapes Scientific Ideas and Human Perceptions](http://arxiv.org/abs/2610.30568v1)
  <details><summary>📄 Abstract</summary>
  As AI increasingly becomes a collaborator in scientific research, its impact may extend beyond improving ideas to reshaping how they are evaluated, attributed, and perceived by humans. Yet existing research has largely examined these dimensions in isolation. We present a unified empirical study of Human-AI scientific ideation, investigating two complementary perspectives: i) how AI collaboration shapes scientific ideas and their evaluation, and ii) how firsthand collaboration reshapes human perc...
  </details>

- **2026-10-22** — Atiksh Bhardwaj, Edward W. Duan, Junwon Seo et al. — [Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models](http://arxiv.org/abs/2610.31613v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models can perform diverse manipulation tasks directly from visual observations and natural language instructions, but they remain prone to mistakes and unpredictable failures. Deploying these policies without continuous human supervision will require robust runtime monitors that detect when the policy has gone off-course. Existing monitors use external foundation models, such as vision-language models (VLMs) to supervise the policy, introducing significant complexit...
  </details>

- **2026-10-22** — Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad et al. — [MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models](http://arxiv.org/abs/2610.31478v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss localized anomalies. We propose MoG-VLM a motion-adaptive anomaly detection framework that leverages motion purely as a lightweight control signal to decide when VLM inference is nec...
  </details>

- **2026-10-22** — Tianming Liang, Junyi Pan, Yuxi Li et al. — [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](http://arxiv.org/abs/2610.31329v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language models (VLMs) remain unreliable for fine-grained visual perception. In this report, we present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. It supports multiple visual tasks including object detection, referring localization, counting, OCR, segmentation, and matting, enabling localization at any user-specific granularity, from points and boxes to masks and alpha matte...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 60 papers

- **2026-10-26** — Diana Cerdas-Vargas, Alejandro Romero, Richard J. Duro — [From Language to Drives: A Multimodal Framework for Aligning Autonomous Robots with Human Purposes](http://arxiv.org/abs/2610.35629v1)
  <details><summary>📄 Abstract</summary>
  This work explores a multimodal approach to the alignment of the behavior of open-ended learning autonomous robots with human purposes through the use of large language models as cultural enablers. While autonomous robots can generate their own skills and goals through interaction with the environment, they often lack mechanisms to ensure that these remain relevant and aligned to those of human users. The proposed approach makes use of the general and cultural knowledge contained in LLMs and VLM...
  </details>

- **2026-10-26** — Zuoxu Wang, Xiao Liang — [Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies](http://arxiv.org/abs/2610.35626v1)
  <details><summary>📄 Abstract</summary>
  Efficient robotic data collection remains a major bottleneck for vision-language-action (VLA) policy learning, especially for tasks requiring accurate end-effector positioning and camera-action alignment. This challenge is particularly severe in electronic-waste disassembly, where robots operate in cluttered assemblies of densely packed, visually similar components. Full digital-twin simulation is difficult because many parts are thin, reflective, or mechanically complex, making accurate object-...
  </details>

- **2026-10-26** — Wei Zhang, Wolfgang Nejdl, Ming Tang — [SAP-ViT: A Self-Attributing Patch Vision Transformer for Medical Image Classification](http://arxiv.org/abs/2610.35593v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformer (ViT) classifiers commonly rely on a global classification (CLS) token for image-level prediction, which is poorly aligned with local interpretability requirements in medical imaging. We propose SAP-ViT, a Self-Attributing Patch Vision Transformer that replaces CLS-based classification with direct aggregation of last-layer patch embeddings. This design makes class predictions decomposable into patch-level contributions as part of the forward pass. To encourage concise and read...
  </details>

- **2026-10-26** — Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi et al. — [Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU](http://arxiv.org/abs/2610.35554v1)
  <details><summary>📄 Abstract</summary>
  Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), t...
  </details>

- **2026-10-26** — Haoyu Wang, Fei Zhou, Qingqing Qiu et al. — [S$^2$-RL: Sample-Set Dual Reinforcement Learning for Generative Semantic Segmentation Dataset Distillation](http://arxiv.org/abs/2610.35491v1)
  <details><summary>📄 Abstract</summary>
  While dataset distillation has witnessed significant advances in image classification, its extension to dense prediction tasks such as semantic segmentation is plagued by two core bottlenecks: bi-level optimization-based approaches suffer from prohibitive computational costs stemming from pixel-wise gradient unrolling, whereas proxy-based generative methods merely infuse visual textures into fixed semantic masks derived from real data, thus failing to condense rich semantic knowledge into a comp...
  </details>

- **2026-10-26** — Artem Saloev, Nicolas Ballier, Erin Pacquetet — [Probing the phon* representations of the Mimi codebooks](http://arxiv.org/abs/2610.35432v1)
  <details><summary>📄 Abstract</summary>
  Neural audio codecs are increasingly used to encode speech for integration with large language models. This paper investigates the phonetic representations in the first codebook (CB0) of the Mimi codec. ABX style evaluation is poorly suited to Mimi fixed 80 ms tokenization window, which often spans multiple phonemes; we instead use forced alignment, entropy analysis, and Phone-Normalized Mutual Information (PNMI). Using TIMIT speech (58/55 speakers, SA1/SA2), individual tokens are strongly assoc...
  </details>

- **2026-10-26** — Xiaohan Lu, Jiaqi Zhang, Weijia Jiang et al. — [SG-Splat: Stable Geometry Learning under Pose Uncertainty for Pose-Free 3D Gaussian Splatting](http://arxiv.org/abs/2610.35361v1)
  <details><summary>📄 Abstract</summary>
  3D Gaussian Splatting (3DGS) has become a promising representation for real-time novel view synthesis and 3D scene reconstruction. For practical deployment, recent studies have explored pose-free feed-forward 3DGS, which reconstructs Gaussian representations directly from unposed input images. However, these methods remain sensitive to residual pose errors, which perturb canonical-space Gaussian transformation, introducing noisy supervision for geometry and attribute learning. To address this pr...
  </details>

- **2026-10-26** — Yingbo Hao, Song Liu, Guanghua Yu et al. — [InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL](http://arxiv.org/abs/2610.35303v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn agent reinforcement learning (RL) relies on long closed-loop rollouts, making generation and KV-cache costs a major bottleneck. Quantized rollout reduces these costs, but its low-precision executor also serves as the behavior policy and can induce execution mismatch with the learner. Existing quantized-RL methods are designed primarily for single-turn generation. They align the learner forward with quantized rollout or correct the current-token rollout-learner ratio, without modeling ...
  </details>

- **2026-10-26** — Hao Shen, Ruichen Qiu, Lihong Zhi et al. — [MechAlign: Evaluating Semantic Alignment at the Project Level in Mathematical Formalization](http://arxiv.org/abs/2610.35269v1)
  <details><summary>📄 Abstract</summary>
  Lean verifies that a formal proof establishes its stated proposition under declared assumptions, but does not check whether that proposition faithfully expresses the mathematical claim in a manuscript. Assessing this correspondence requires interpreting the main theorem through its project dependencies, which may be scattered throughout a large development. We introduce MechAlign, a framework for project-level semantic alignment review that combines formal dependency extraction with LLM-based as...
  </details>

- **2026-10-26** — Junzhang Liu, Hao Yuan, Qi Zhang et al. — [Joint Latent Reasoning and Observation for Agentic Video Understanding](http://arxiv.org/abs/2610.35229v1)
  <details><summary>📄 Abstract</summary>
  Effective video agents must learn not only how to answer, but also where to look next. Transferring this capability to smaller models is challenging because each observation serves two purposes: supporting an answer and guiding the search for further evidence. Textual descriptions may capture what is currently visible while omitting cues needed for subsequent acquisition. We introduce Latent Agentic Reasoning for Video Analysis (LARVA), a framework that distills multi-round video agents through ...
  </details>

- **2026-10-26** — Blessing Ngozi Uzor, Valdini Douglace Lemofouet, Paula Chikaodinaka Anyanwu et al. — [Do Language Models Understand Igbo Culture? Beyond Multiple Choice](http://arxiv.org/abs/2610.35168v1)
  <details><summary>📄 Abstract</summary>
  The value of language models for any community depends on whether a model actually understands the culture of the people it intends to serve. We use the Igbo language as a case study. Existing benchmarks test translated Western ideas, lacking depth. To address this, we introduce CAB-Igbo, a benchmark developed from indigenous cultural sources and verified by native speakers across six domains. We evaluated diverse models under varying conditions, incorporating regional personas. Performance was ...
  </details>

- **2026-10-26** — Filippos Ventirozos, Tom Armitage, Mahmoud Oshagh et al. — [Useful Diversity or Hallucinated Variety? Persona-Conditioned Synthetic Query Generation for E-Commerce Search](http://arxiv.org/abs/2610.35102v1)
  <details><summary>📄 Abstract</summary>
  Synthetic supervision can bootstrap semantic parsers in new search domains, but prompt-induced diversity is useful only when generations are faithful to the structured intent. We explore this for cold-start e-commerce search: 118,098 synthetic pairs produced by 6 LLMs with 9 persona-conditioned prompt families on a 47-field UK automotive schema, against 1,214 human-annotated and 15,304 production queries. We show that the IPIP personality bundle improves parser F1 in all four matched contrasts (...
  </details>

- **2026-10-26** — Wenqiang Qin, Renlong Jie, Yanjun Qian et al. — [Interpreting LLM Scores in Peer Review: Alignment and Divergence Across Prompts, Domains, and Manuscript Features](http://arxiv.org/abs/2610.35098v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) scores are being studied as information for scholarly evaluation. Interpreting these scores requires evidence about agreement with human judgments and its variation across evaluation conditions. Guided by an argument-based approach to validation, we compare four LLMs on 7,083 public ICLR 2024 submissions under a standard review condition and examine ten prompt conditions using DeepSeek-V3.2. We distinguish average score divergence, paper-level absolute error, and rank ...
  </details>

- **2026-10-26** — Jingwen Zhu, Keshu Wu, Steven T. Parker et al. — [From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis](http://arxiv.org/abs/2610.35054v1)
  <details><summary>📄 Abstract</summary>
  Transportation agencies maintain extensive crash databases to identify safety priorities, evaluate countermeasures, and guide resource allocation. Making these data accessible to practitioners requires flexible ways to translate analytical questions into reliable results. Existing dashboards support predefined analyses, while additional requests often depend on specialists who understand database queries, coded fields, and agency conventions. This study presents CrashDB-QA, a fully local, schema...
  </details>

- **2026-10-26** — Justin Y. Chen, Ying Feng, Piotr Indyk et al. — [Attention under Bounded Key-Query Similarity: Space Complexity and Transformer Anisotropy](http://arxiv.org/abs/2610.35020v1)
  <details><summary>📄 Abstract</summary>
  A growing body of work on KV-cache compression aims to reduce the memory requirements of autoregressive generation. These methods compress the stored context while approximately preserving attention computation, enabling generation with reduced memory consumption. Almost tight theoretical results on the worst case space complexity of attention have recently been obtained, but they are achieved by instances where queries can be perfectly aligned with keys. This directly contradicts the observed a...
  </details>

- **2026-10-26** — Gunhee Cho, Hongyeob Kim, Yun-Gyung Cheong — [FATE-5: Faithful Alignment of Trait Expression for Continuous Big Five Personality Control](http://arxiv.org/abs/2610.34889v1)
  <details><summary>📄 Abstract</summary>
  Controlling personality in large language models is important for building conversational agents that can be customized to different users and interaction settings. However, existing personality control methods often face a tradeoff between strong trait expression and natural dialogue generation. We introduce FATE-5, Faithful Alignment of Trait Expression for the Big Five, a two-stage framework that separates personality encoding from naturalness alignment. FATE-5 first learns continuous soft pr...
  </details>

- **2026-10-26** — Asad Gohar, Md Ariful Islam Mozumder, Moon-Il Joo et al. — [DocTalk: Enhancing Medical Knowledge Retrieval via Fine-tuned Large Language Models with Chain-of-Thought Reasoning for Robust Clinical Decision Support](http://arxiv.org/abs/2610.34871v1)
  <details><summary>📄 Abstract</summary>
  Objective: The rapid advancement of large language models (LLMs) in healthcare has opened new possibilities for AI-assisted clinical decision-making; however, safe and effective deployment remains challenging because of hallucination and domain misalignment. This study introduces DocTalk, a doctor-assistive question-answering (QA) system designed to generate concise, chart-grounded responses from de-identified discharge summaries. Methods: We developed a high-fidelity data generation pipeline th...
  </details>

- **2026-10-26** —  Qiuyi,  Zhang, Zhen Xu et al. — [DecoyCount: Evaluating Visual-Reasoning Misalignment in Counting](http://arxiv.org/abs/2610.34855v1)
  <details><summary>📄 Abstract</summary>
  Visual counting benchmarks report whether vision-language models produce the correct number, but not whether errors arise from perception or reasoning. We introduce DecoyCount, a benchmark built from 1,660 real-world images with designed decoys across seven mechanisms, along with paired prompts: a neutral question, a matched alignment cue, and a novel multi-hop, multi-image question that situates the same counting problem in a realistic scenario. Using this design, we find that counting failures...
  </details>

- **2026-10-26** — Boxuan Wang, Zhuoyun Li, Sarvapali D. Ramchurn et al. — [Collective Emergent Alignment: Measuring and Amplifying Interaction-Induced Reasoning Alignment in Multi-Agent LLMs](http://arxiv.org/abs/2610.34836v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) systems can exhibit emergent behaviors through interaction, yet whether a similar phenomenon exists for reasoning alignment remains largely unexplored. We study whether agent interaction produces additional reference-grounded reasoning alignment beyond matched individual self-refinement, and introduce REMAP (Reference-Entailment-Matrix for Agentic Process), a framework that quantifies this effect through Semantic Coverage and interaction-specific alignment ...
  </details>

- **2026-10-26** — Yizhou Peng, Chen Chen, Donghang Wu et al. — [Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems](http://arxiv.org/abs/2610.34653v1)
  <details><summary>📄 Abstract</summary>
  Latency-sensitive spoken agents must know not only which tool to call, but also when they have heard enough to act. Waiting for the turn to complete delays execution even when the request is already actionable. However, neither existing spoken agents nor spoken dialogue corpora define the earliest point at which a request becomes actionable. We introduce a synthetic spoken-dialogue pipeline that provides earliest-actionable-point supervision, marking when the observed speech grounds a tool and i...
  </details>

- **2026-10-26** — Jonathan DeCastro, Thomas Balch, Emily Sumner et al. — [Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](http://arxiv.org/abs/2610.34650v1)
  <details><summary>📄 Abstract</summary>
  Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time. We present Dream2Assist, a model-based reinforcement learning framework for tightly-coupled shared decision making that addresses both sides of this challenge. Our approach extends a recurrent state-space world model with intent inference, enabling an assistive policy trained via fi...
  </details>

- **2026-10-25** — Albert Zeyer, Davyd Naveriani, Dorian Koch et al. — [One Mean Log-Mel Vector per Phoneme: Simple and Fast Text Injection for Speech Recognition](http://arxiv.org/abs/2610.34623v1)
  <details><summary>📄 Abstract</summary>
  Text injection trains speech recognition models on unpaired text alongside paired audio. We feed the speech encoder synthetic input derived from text so the whole model learns from it. Previously, we synthesized this input with a frozen text-to-speech (TTS) model. Here, a simple lookup table replaces the TTS model: a mean log-mel vector (or one-hot encoding) per phoneme, repeated for a random duration drawn from alignment statistics, with silence between words. Training is 1.8 times faster than ...
  </details>

- **2026-10-25** — Pierre-Olivier Bonin — [Error Diffusion Replaces Latent Weights: Training Binary-Weight Language Models on a Few Bits of Dithered State](http://arxiv.org/abs/2610.34566v1)
  <details><summary>📄 Abstract</summary>
  Binary-weight language models store one bit per weight, but training them keeps a full-precision latent copy of each weight plus Adam state, about 96 extra bits per weight, so a deployed binary model cannot be adapted on the device that runs it. We replace the latent weight with a 2-8-bit residual buffer quantized by stochastic rounding, which cuts the training state per weight from 97 bits to 3-9, up to 19x less. The resulting error-diffusion (ED) optimizer moves the residual-carrying loop of i...
  </details>

- **2026-10-25** — Haibao Yu, Jiaqi Meng, Zijian Zhang et al. — [How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder: A Hierarchical, Matched Sim-Real Benchmark for Physical Interaction](http://arxiv.org/abs/2610.34527v1)
  <details><summary>📄 Abstract</summary>
  We introduce PhysLadder, a hierarchical Sim-Real benchmark for evaluating physical interaction capabilities in contact-rich manipulation. Its 16 household tasks span three cumulative levels: contact selection and geometric alignment (L1), force regulation within sustained contact (L2), and coordinated contact reconfiguration and force regulation (L3). Each task is instantiated in physically and visually matched simulated and real-world environments, with shared task definitions and success crite...
  </details>

- **2026-10-25** — Yibo Zhao, Lifan Jiang, Senlin cheng et al. — [CrossPair: Unlocking Generalist Visual Transformation Learning in Image Editors](http://arxiv.org/abs/2610.34333v1)
  <details><summary>📄 Abstract</summary>
  Language models switch tasks from demonstrations, but vision still often relies on separate systems for restoration, editing, and stylization. A before--after example offers a shared instruction only if the transferable change can be separated from the scene that demonstrates it. We introduce CrossPair, which adapts a pretrained multimodal image editor to transfer diverse transformations from one exemplar pair. Exemplar-before, exemplar-after, and query images take fixed roles in its native VLM ...
  </details>

- **2026-10-25** — Guojun Lei, Hong Li, Hongbing Yang et al. — [EditDistill: Is It Possible to Guide Video Editing with Image Editing?](http://arxiv.org/abs/2610.34303v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in image editing have enabled fine-grained and highly controllable visual modifications. However, achieving similar levels of controllability in video editing remains an open challenge, particularly for precise local edits, dynamic temporal effects, and consistent lighting across frames.In this paper, we propose EditDistill, a framework that distills image-level visual transformations from edits to guide video editing.Specifically, given a source video and an edit prompt, we firs...
  </details>

- **2026-10-25** — Harsidak Singh Banwait, Chander Prabha — [Transformer to GPT-5: Advancements, Limitations, and Future Directions in Large Language Model Design](http://arxiv.org/abs/2610.34281v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have revolutionized Artificial Intelligence (AI) by their extraordinary capabilities, like contextual understanding, few-shot/zero-shot learning, code generation, ability to reason and problem-solving. Recent studies have shown immense work on LLMs. Yet, there is limited work on the thorough taxonomy of LLMs. This study would showcase a detailed classification of LLMs, starting with the earlier models like BERT and leading to LLMs like GPT, Gemini, Claude and Grok. W...
  </details>

- **2026-10-25** — Xiangfei Sheng, Xiaofeng Pan, Leida Li et al. — [CropReward: A Human-Preference Benchmark and Reward Model for Aesthetic Image Cropping](http://arxiv.org/abs/2610.34221v1)
  <details><summary>📄 Abstract</summary>
  Aesthetic image cropping (AIC) aims to improve image composition and aesthetic quality by removing extraneous or distracting content. Over the past decade, AIC methods have evolved from specialized vision models to multimodal large language models(MLLMs). Reliable evaluation that reflects human preferences is essential for benchmarking AIC methods and guiding model optimization. However, the current AIC evaluation relies largely on geometry-based metrics such as intersection over union (IoU), as...
  </details>

- **2026-10-25** — Amin Golnari, Saeid Sanei — [StaX-Net: Stackelberg Interleaved Asymmetric Network for Cross-Modality Medical Image Translation](http://arxiv.org/abs/2610.34214v1)
  <details><summary>📄 Abstract</summary>
  Cross-modality medical image translation is challenged by anatomically inconsistent synthesis that can compromise clinical diagnosis. We propose StaX-Net, a Stackelberg interleaved asymmetric network that incorporates a partially coupled encoder-discriminator structure, and a 2D feature aggregation and spatial transformation (FAST) layer that distills target-supervised priors under the learning using privileged information paradigm. The shared blocks between the generator and discriminator enhan...
  </details>

- **2026-10-25** — Changxu Ni, Feiran You, Yongan Guo et al. — [CORMA: Constraint-Routed Decision Mamba for Generalizable Multi-Constraint Offline Safe Reinforcement Learning](http://arxiv.org/abs/2610.34208v1)
  <details><summary>📄 Abstract</summary>
  Offline safe reinforcement learning (RL) learns safety-aware policies from static datasets while satisfying safety constraints during deployment. Motivated by the strong trajectorymodeling capabilities of Transformers, recent Decision Transformer (DT)-based methods formulate offline safe RL as conditional sequence modeling by conditioning action generation on return-to-go (RTG) and cost-to-go (CTG) tokens, thereby enabling adaptation to varying safety budgets. However, existing DT-based methods ...
  </details>

- **2026-10-25** — Xueping Zhang, Xiaoxiao Miao, Tiantian Feng et al. — [ASR-Protected Fusion and Reference-Anchored Policy Optimization for Joint ASR and Word-Level Speech Anti-Spoofing](http://arxiv.org/abs/2610.34156v1)
  <details><summary>📄 Abstract</summary>
  Existing anti-spoofing systems report either an utterance-level score or a time-based spoof interval: the former cannot show which words are spoofed, while the latter does not directly match the transcript and must be post-aligned with words, so alignment errors can lead to wrong word-level labels. Standard ASR model outputs only text; spoof information in the audio is lost after recognition and is not passed with the transcript. Yet changing only a few words can change the meaning of a sentence...
  </details>

- **2026-10-25** — Chih-Ting Liao, Kezhen Bao, Xin Cao — [Reversion, Retention, and Semantic Intervention: Measuring Functional Content in CLIP Fine-Tuning Deltas](http://arxiv.org/abs/2610.34144v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning adapts pretrained models to new tasks, but identifying which weight changes support the resulting behavior remains difficult. Weight-space interpretability assigns semantic descriptions to these changes, called fine-tuning deltas. Such descriptions leave open how much task performance depends on the identified updates, particularly when other updates can support the same predictions. We address this gap by pairing reversion, which restores selected parameters to their pretrained valu...
  </details>

- **2026-10-25** — Shahriar Kabir Nahin, Xiao Ye, Muhao Chen et al. — [T2D: Target-to-Draft Model Pruning & Adaptation for Efficient Speculative Decoding](http://arxiv.org/abs/2610.34103v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding significantly accelerates autoregressive text generation in Large Language Models (LLMs), but its efficacy depends largely on two key factors: the distributional alignment between the draft and the target model, and the draft model's latency during inference. However, existing approaches typically utilize independently pretrained small draft models or seek to prune the target model to a manually chosen architecture, thereby failing to explicitly balance the trade-off between...
  </details>

- **2026-10-25** — Ting Xu, Henry Leung — [Fed-Universe: A Semantic-Geometric-Topological-Human (S-G-T-H) Stack for Negotiated Alignment in Federated Systems](http://arxiv.org/abs/2610.34009v1)
  <details><summary>📄 Abstract</summary>
  Conventional federated learners implicitly optimize for global means, creating a "one-size-fits-all" paradigm that inevitably suppresses the minority under cross-site heterogeneity. To bridge this critical gap, we present Fed-Universe, a generalizable Semantic-Geometric-Topological-Human (S-G-T-H) architecture that transforms passive averaging into an active negotiation for decentralized alignment. The S-layer deploys an edge-capable LLM as a semantic surrogate to translate heterogeneous inputs ...
  </details>

- **2026-10-25** — Bahaeddin Türkoğlu — [Large Language Models: A Plain-Language Overview for Engineers](http://arxiv.org/abs/2610.34585v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are neural networks trained on huge text collections to generate text by predicting what comes next. Engineers using ChatGPT and other generative artificial intelligence (AI) tools need a clear picture of what training changes and prompts add. The article starts with the Transformer, which connects words in context, and pre-training, where models learn to predict text. It then explains how fine-tuning adapts models to requests, with reinforcement learning from human ...
  </details>

- **2026-10-24** — Vinita Shukla, Partibha Jangra, Vinayak Pathak et al. — [DROA-CLIPSeg: Prompt-Guided Thin Crack Segmentation in Low-Light Conditions](http://arxiv.org/abs/2610.33635v1)
  <details><summary>📄 Abstract</summary>
  Pavement crack segmentation under low light is degraded by reduced contrast, shadows, headlight glare, joints, stains, and wet seams. Existing crack segmentation methods mostly assume good illumination. Low-light enhancement methods improve visual quality, but they do not explicitly preserve crack topology. To address these limitations, we formulate low-light crack segmentation as a degradation-aware, prompt-grounded structural defect segmentation problem and propose DROA-CLIPSeg, a parameter-ef...
  </details>

- **2026-10-23** — Yijing Ke, Tianle Cai, Ruosong Wang — [Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning](http://arxiv.org/abs/2610.32951v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for large language models often uses separate systems for inference and training. Even with identical weights and BF16 tensors, implementation differences can make an intended on-policy update off-policy and destabilize training. Existing remedies align the entire inference and training stacks, change global precision, or modify the learning algorithm. We ask whether aligning selected parts of the execution stack can stabilize BF16 RL while other implementation differences...
  </details>

- **2026-10-23** — Qiwei Zhao, Oriana Pansardi, James W. Strachan et al. — [Beyond pass or fail: an information-processing account of the Turing Test](http://arxiv.org/abs/2610.32868v1)
  <details><summary>📄 Abstract</summary>
  The Turing Test is passed when a human interrogator cannot distinguish machine-generated responses from human ones. Yet behavioral indistinguishability can reflect two fundamentally different failures: a failure of encoding, in which machine and human output distributions overlap so closely that source information is effectively absent; or a failure of readout, in which source information is present but the interrogator fails to extract it. To dissociate these possibilities, we inverted the Turi...
  </details>

- **2026-10-23** — Yi Qi, Srijoni Majumdar, Evangelos Pournaras — [AI Alignment for Digital Democracy: Fairer Voters Representation against LLM Biases](http://arxiv.org/abs/2610.32780v1)
  <details><summary>📄 Abstract</summary>
  AI representation is emerging in digital democracy, assisting in voter emulation and decision-making. Large language models (LLMs) behave differently depending on the model, the prompt context, and the voter information they receive, representing some groups more accurately than others and potentially making the emulation unfair to certain groups. We investigate demographic biases in LLM-emulated electorates: how accurately LLMs represent individual votes, whether some voter groups are represent...
  </details>

- **2026-10-23** — Tianchi Xu, Yalin Zheng, Yangxin Zhu et al. — [Predictive Long-Horizon Progress Modeling with Action-Aware Quantification](http://arxiv.org/abs/2610.32776v1)
  <details><summary>📄 Abstract</summary>
  Quantitative and dense task progress feedback is essential for robotic manipulation across data curation, policy evaluation, and reinforcement learning. Existing progress annotations often rely on sparse keyframe markings derived from subjective manual judgments, limiting their scalability and cross-task consistency, particularly in long-horizon manipulation. To overcome these challenges, we propose action-aware quantification, a unified progress specification that decomposes long-horizon trajec...
  </details>

- **2026-10-23** — Haoxiang Tang, Dong Zhou, Shen Tan et al. — [SP-Guide: Enhancing Aerial Vision-Language Navigation with Spatial Priors](http://arxiv.org/abs/2610.32697v1)
  <details><summary>📄 Abstract</summary>
  Aerial vision-language navigation (AVLN) requires a UAV to reach a language-described target from partial egocentric observations while reasoning over large outdoor scenes. Existing approaches typically fuse view-centered RGB observations and globally anchored history maps as generic visual embeddings, leaving cross-modal spatial alignment to be learned from sparse navigation supervision. We present SP-Guide, a transformer- based goal-prediction framework that addresses this weakness of alignmen...
  </details>

- **2026-10-23** — Roy Amoyal, Shira Ifergane, Oren Freifeld — [SemGeo-Gen: Unsupervised Generation of Approximate Cross-Instance Semantic-Geometric Correspondences](http://arxiv.org/abs/2610.32663v1)
  <details><summary>📄 Abstract</summary>
  We introduce SemGeo-Gen, an unsupervised method for generating approximate cross-instance semantic-geometric supervision from weakly aligned 3D object collections. Our goal is not to recover exact point-level correspondences, which are often ambiguous across different instances and would require expensive, impractical manual supervision at scale. Instead, we automatically produce approximate correspondences that are semantically meaningful, geometrically consistent, and diverse enough to train m...
  </details>

- **2026-10-23** — Yuqiao Xia, Yuchen Deng, Ziheng Chang et al. — [SREdit: Scene Response Guided Appearance Editing for Projection Mapping](http://arxiv.org/abs/2610.32792v1)
  <details><summary>📄 Abstract</summary>
  Projection-based appearance editing changes selected visual attributes of a physical object through projection mapping (PM). To display a desired appearance, PM typically uses projector compensation, which computes a projector input that counteracts the geometric and photometric distortions of the scene. Compensation can only approximate this appearance within the available projection range, and it cannot revise the appearance itself. Pretrained LLM-based image editors provide a direct way to pr...
  </details>

- **2026-10-22** — Yunfei Xie, Howard H. Qian, Shiyi Lan et al. — [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](http://arxiv.org/abs/2610.31670v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the st...
  </details>

- **2026-10-22** — Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini et al. — [On the Token Collapse Phenomenon in Textual Graph Soft Prompting](http://arxiv.org/abs/2610.31572v1)
  <details><summary>📄 Abstract</summary>
  Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal. We conduct an in-depth analysis of G-Retriever and uncover a pathological behavior we term token collapse. Across three benchmarks, three gra...
  </details>

- **2026-10-22** — Ioannis Kouroudis, Zhaosu Gu,  Poonam et al. — [PYTHIA, a transferable machine learning framework for simultaneous defect and adsorption site optimization](http://arxiv.org/abs/2610.31539v1)
  <details><summary>📄 Abstract</summary>
  Machine learning has permeated material optimization, providing high value. Nevertheless, its re- liance on a high number of samples limits its applicability to relatively explored material families. In this paper we extend the applicability of machine learning to novel and understudied materials through the PYTHIA (Probabilistic Yet Transferable Hierarchical Interaction Architecture) framework. Pythia utilizes two of the most powerful machine learning concepts, foundational models and transfer ...
  </details>

- **2026-10-22** — Eun Sun Lee, Minkyun Seo, Gwangtak Bae et al. — [A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation](http://arxiv.org/abs/2610.31432v1)
  <details><summary>📄 Abstract</summary>
  A conventional embodied agent in an indoor environment builds a map by accumulating noisy real-world measurements and results from heavy inference to guide navigation. While the detailed measurements may differ due to scene changes or sensor settings, the unique topological structure of navigable passages or the connectivity between rooms may provide training-free guidance that complements local observations. We propose a sparse topometric graph as an efficient structural representation for robu...
  </details>

- **2026-10-22** — Yen-Ku Liu, Hongjie Chen, Franck Dernoncourt et al. — [DISC: Domain-Integrated Similarity Cost for Time-Series Dataset](http://arxiv.org/abs/2610.31288v1)
  <details><summary>📄 Abstract</summary>
  The growth of time-series datasets and foundation models has made dataset comparison a central part of time-series workflows. Assessing source-target transfer before model adaptation requires similarity estimates that can summarize transfer-related dataset relationships without exhaustive source-target evaluation over every candidate pair. Many metrics have been proposed for measuring similarity between time-series datasets, but they capture different dataset relationships and vary in how well t...
  </details>

- **2026-10-22** — Wei-Jaw Lee, Chun-Ping Wang, Xuanjun Chen et al. — [MQAScore: Fine-Grained Text-Music Alignment Evaluation via Large Audio Language Model](http://arxiv.org/abs/2610.31083v1)
  <details><summary>📄 Abstract</summary>
  Text-to-music alignment is commonly evaluated by the global similarity between text and audio embeddings, which collapses all described attributes into a single score and obscures which ones are missing. We instead introduce MQAScore, which verifies each atomic musical concept along five clip-level dimensions (genre, instrument, mood/theme, vocal, and usage) by the probability that a large audio language model (LALM) answers affirmatively to a binary question. To assess evaluator reliability, we...
  </details>

- **2026-10-22** — Qiuyu Kong, Zanxi Ruan, Marco Cristani et al. — [Mitigating Saliency Collapse: Robust Saliency-Aware Long-Text Image-Text Alignment](http://arxiv.org/abs/2610.31005v1)
  <details><summary>📄 Abstract</summary>
  Long-text image-text alignment is essential for fine-grained scene understanding, yet existing methods mainly focus on extending context length or improving local alignment. We identify an overlooked failure mode, saliency collapse, where models over-rely on text that features visual prominence while underutilizing non-salient context. Consequently, retrieval performance degrades sharply when salient content is reduced, despite that the non-salient context remains informative. To address this, w...
  </details>

- **2026-10-22** — Mohammad Talaei, Mohammad Goudarzi, Maille Todd et al. — [Zero-Shot Forecasting of In-Situ Soil Moisture and Temperature with a Time-Series Foundation Model](http://arxiv.org/abs/2610.30971v1)
  <details><summary>📄 Abstract</summary>
  Soil moisture and temperature govern plant-water availability and microbial activity, making them key indicators for evaluating land-restoration efforts on degraded landscapes. However, the physical and data-driven models normally used to forecast them both need information that a newly instrumented restoration site does not yet have: hydraulic parameters for the former and months of per-site training data for the latter. We evaluate TimesFM 1, a 500M-parameter time-series foundation model, zero...
  </details>

- **2026-10-22** — Pengfeng Song, Shaozhong Zhang, Pengfei Shao — [Hierarchical Fine-Grained Cross-Modal Alignment via Dynamic Granularity Discovery and Optimal Transport](http://arxiv.org/abs/2610.30912v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained image-text retrieval requires a model not only to assess global semantic consistency between an image and a text, but also to model visual evidence for local textual semantics, including objects, attributes, quantities, actions, and relations, so as to distinguish semantically similar candidates. Existing methods commonly use fixed image patches, detected regions, or text tokens as the basic matching units and then aggregate local interactions through max pooling, cross attention, o...
  </details>

- **2026-10-22** — Dewei Wang, Jinrui Han, Jiyuan Shi et al. — [LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.30876v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and compositional tasks across five household scene categories, supported by 51.5 hours of simulated teleoperation. The evaluation covers twelve pol...
  </details>

- **2026-10-22** — Ziang Lu, Yu Zhang, Xinzhe Jiang et al. — [Bezier-Guided Adaptive Flow for Cross-domain Sequential Recommendation](http://arxiv.org/abs/2610.30825v1)
  <details><summary>📄 Abstract</summary>
  Cross-domain sequential recommendation aims to alleviate data sparsity and cold-start problems by transferring useful preference knowledge across domains. However, users exhibit varying degrees of preference consistency across domains, while existing methods often rely on global alignment objectives or coarse-grained transfer strategies. Such approaches may introduce irrelevant information and provide limited flexibility in adapting semantic representations to individual user preferences. To add...
  </details>

- **2026-10-22** — Chalisa Veesommai Sillberga, Kai-Kristian Kemella, Pekka Sillberga et al. — [TESSA: A Governance-Oriented Custom GPT for SME Guidance under the EU AI Act: Design, Implementation, and Evaluation](http://arxiv.org/abs/2610.30822v1)
  <details><summary>📄 Abstract</summary>
  The increasing adoption of generative AI presents new opportunities while raising AI governance and regulatory challenges, particularly for small and medium-sized enterprises (SMEs) navigating the European Union Artificial Intelligence Act (EU AI Act). To support AI governance education, this study developed TESSA, a governance-oriented educational artifact within the OpenAI Custom GPT environment. Following a design science research approach, TESSA was evaluated against baseline ChatGPT using 1...
  </details>

- **2026-10-22** — Mijeong Kim, Suho Park, Junha Park et al. — [AgentDreamer: Agentic 3D Motion Reasoning for Text-Controllable Physics Simulation](http://arxiv.org/abs/2610.30679v1)
  <details><summary>📄 Abstract</summary>
  We propose AgentDreamer, an agent-guided optimization framework that aligns text instructions with simulated motion through explicit 3D motion planning. Given a text instruction and scene geometry, an off-the-shelf agent translates the instruction into a structured semantic motion prior, specifying what should move, in which direction, and in what temporal order. The agent represents this prior using parametric functions over a series of temporal chunks, yielding dense 3D trajectories. We then o...
  </details>

- **2026-10-22** — Hao Jiang, Peiru Du, Pengfei Yao et al. — [OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models](http://arxiv.org/abs/2610.30675v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong reasoning capabilities, motivating their use as the backbone of foundation recommendation models (FRMs). Existing methods enhance recommendations through explicit Chain-of-Thought (CoT) reasoning under a Think-then-Answer paradigm. However, explicit CoT incurs substantial inference overhead by generating lengthy reasoning traces and relies on manually designed templates that struggle to capture diverse, dynamic user interests. We propose OneL...
  </details>

- **2026-10-22** — Yanan He, Yanli Chen, Ling Xiong et al. — [Model-intrinsic, Weight-level, and Training-free Spectral Fingerprinting for Large Language Models](http://arxiv.org/abs/2610.30626v1)
  <details><summary>📄 Abstract</summary>
  The increasing release and reuse of Large Language Models (LLMs) as open-weight checkpoints make model fingerprinting important for ownership protection and offline auditing. Existing fingerprinting methods typically construct evidence from query responses, generated outputs, or input-induced activations. Although effective in representation-based settings, they can be affected by prompt selection, decoding configuration, inference environment, and forward-pass implementation, which may limit th...
  </details>

- **2026-10-22** — Minhyuk Seo, Minjae Lee, Chaeeun Lee et al. — [Visual Grounding First, Multimodal In-context Learning Follows](http://arxiv.org/abs/2610.30592v1)
  <details><summary>📄 Abstract</summary>
  LLMs have shown strong in-context learning (ICL) capability, but extending it to Multimodal LLMs (MLLMs) remains challenging. Prior multimodal ICL methods often rely on ICL-specific datasets for additional training or task vector extraction, which can improve performance on the same ICL benchmark used for adaptation. However, they do not generalize well to other benchmarks and often induce forgetting in previously well-solved tasks. For this reason, we identify 'visual grounding' as the key bott...
  </details>

- **2026-10-22** — Giovanni Romagnoli, Fabrizio Pilone, Giordana Bucchioni — [Consensus-Based Distributed Filtering for Angles-Only Tracking in Cislunar Space](http://arxiv.org/abs/2610.30864v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates consensus-based distributed filtering strategies for multi-observer angles-only navigation in the cislunar space. The objective is to estimate the inertial state of a target spacecraft using only line-of-sight measurements collected by a network of observer spacecraft. This problem is particularly relevant for autonomous cislunar navigation, where ground support may be limited, and centralized fusion architectures may be problematic due to communication and computational ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 57 papers

- **2026-10-26** — Atri Vivek Sharma, Brian Formento, Alessio Lomuscio — [Intent-Preserving Adversarial User Simulation for Multi-Turn Agent Evaluation](http://arxiv.org/abs/2610.35426v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn agents are commonly evaluated with LLM-based simulated users, which can be overly cooperative and can therefore overestimate an agent's performance. We here introduce StressSim, an intent-preserving adversarial user simulator framework for stress-testing agents with challenging yet valid user interactions. StressSim optimises the simulator's high-level adversarial plan for each task instance. Candidate planner prompts are evolved with a genetic prompt-optimisation loop that uses rollo...
  </details>

- **2026-10-26** — Sheila Zingg, Florian Tramèr, Martin Vechev et al. — [Can Open Be Too Open? On the Security and Trustworthiness of Fully Transparent LLMs](http://arxiv.org/abs/2610.35199v1)
  <details><summary>📄 Abstract</summary>
  There are different levels of transparency for LLMs: open weights, open data, and/or open pipeline. Recently, more interest has emerged in fully transparent LLMs, i.e., LLMs with fully open weights, data, and training pipeline. Drawing analogies to other fields such as software security, it is often believed that increasing transparency inherently increases the security and trustworthiness of the LLM. However, we argue that such claims need to be critically re-evaluated in the context of LLMs. I...
  </details>

- **2026-10-26** — Anne Harrington, Vasha DuTell, Ayush Tewari et al. — [Exploring perceptual straightness in learned visual representations](http://arxiv.org/abs/2610.34678v1)
  <details><summary>📄 Abstract</summary>
  Humans have been shown to use a "straightened" encoding to represent the natural visual world as it evolves in time (Hénaff et al. 2019). In the context of discrete video sequences, "straightened" means that changes between frames follow a more linear path in representation space at progressively deeper levels of processing. While deep convolutional networks are often proposed as models of human visual processing, many do not straighten natural videos. In this paper, we explore the relationship ...
  </details>

- **2026-10-26** — Haiyong Tang, Hanzhou Wu, Xinpeng Zhang et al. — [From Representations to Computational Trajectories: Intrinsic Fingerprinting for Large Language Model Provenance Verification](http://arxiv.org/abs/2610.34675v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are valuable digital assets, yet their weights can be easily modified after unauthorized acquisition, making model provenance difficult to verify. Model fingerprinting provides a promising solution for model ownership protection without modifying the model or embedding ownership information. However, parameter-based fingerprints can be sensitive to model transformations, limiting their robustness, while representation-based fingerprints may assign high similarity to ...
  </details>

- **2026-10-26** — Wei-Wei Zhang, Pengkai Wang, Yan Li et al. — [Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](http://arxiv.org/abs/2610.35847v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware benchmark for evaluating multistage clinical reasoning across the cancer care continuum, using nasopharyngeal carcinoma as a defined disease context. Curated from longitudinal records of 405 patients across two cancer cen...
  </details>

- **2026-10-26** — Michał Wawer, Jarosław A. Chudziak — [Knowing When to Escalate: Disagreement Patterns for Uncertainty-Aware Content Moderation](http://arxiv.org/abs/2610.35335v1)
  <details><summary>📄 Abstract</summary>
  Agentic content-moderation systems increasingly rely on collective judgments from LLM agents, while aggregation methods commonly treat inter-agent disagreement as a reliability problem to be removed through consensus or voting. This framing is inappropriate for value-laden tasks, where disagreement may reflect irreducible value pluralism - a distinction standard uncertainty decompositions cannot recover, since they operate on output distributions and discard the reasoning behind each judgment. W...
  </details>

- **2026-10-26** — Yuntong Hu, Tongli Su, Yuanfu Sun et al. — [Adaptive Memory Index Evolution for Agents](http://arxiv.org/abs/2610.34977v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed. Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer. We formulate this target as Memory Index Evolution and instantiate it with Adaptive Memory Index Evolution (AMIE), a lightweight plug-in layer that evolves per-memory access state from deployment retrievals without modifying stored cont...
  </details>

- **2026-10-26** — Seonghwan Park, Min-Gyu Park — [Recovering Black-Box Point Cloud Models from Pose Shifts via Derivative-Free Optimization](http://arxiv.org/abs/2610.34850v1)
  <details><summary>📄 Abstract</summary>
  Point cloud models are increasingly deployed through score-only black-box interfaces. Under this access model, test-time rotations outside the training distribution can substantially degrade performance. Although existing mitigations such as equivariant retraining and gradient-based adaptation are effective, they are infeasible without access to model weights or gradients. To address this limitation, we propose CanDO, a test-time canonicalization method that recovers lost performance using only ...
  </details>

- **2026-10-26** — Jiaming Zhang, Fuyao Zhang, Pengjun Xie et al. — [Natural Jammers: When Non-Robust Features Become Antagonistic](http://arxiv.org/abs/2610.34785v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are known to rely on non-robust features that align poorly with human perception. Prior work has largely framed these features as opportunistic shortcuts that help standard models on clean data. We show instead that non-robust cues can be antagonistic: they can act as Natural Jammers that actively mislead standard models on clean, unmodified images. Using disagreement between a standard model and robust models as an analysis lens, we identify a Jammed Set on which robust mod...
  </details>

- **2026-10-26** — Lingjun Mao, Jinglin Cao, Lukun He et al. — [RobotAgentBench: Towards Open-world Robot Autonomy](http://arxiv.org/abs/2610.34649v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm for this transition, integrating task discovery, contextual reasoning, physical execution, and adaptive recovery into a closed interaction loop. However, existing benchmarks largely evaluate isolated capabilities, failing ...
  </details>

- **2026-10-26** — Zheng Zhang, Yifan Wu, Yuxiang Zhou et al. — [Beyond Single-Attribute Auditing: A Configurable Multi-Attribute Benchmark for Intersectional Fairness in LLMs](http://arxiv.org/abs/2610.35069v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly evaluated for fairness, yet most existing benchmarks audit one sensitive attribute at a time. This single-attribute paradigm can miss intersectional harms, where multiple attributes interact non-additively and produce failures that are invisible under marginal evaluation. We introduce ComFair, a configurable benchmark that converts existing fairness data into 479,066 controlled Dual- and Multi-attribute instances and pairs every augmented instance wi...
  </details>

- **2026-10-26** — Xunpeng Yi, Yibing Zhang, Qinglong Yan et al. — [SeeRF: Learning to See Beyond Fields of View via Generative Image Registration and Fusion](http://arxiv.org/abs/2610.35637v1)
  <details><summary>📄 Abstract</summary>
  Due to the inherent discrepancies in imaging viewpoints and field-of-view mismatches among multi-modal sensors, existing fusion methods have long struggled to achieve complete scene-level information integration beyond the limitation in sensor fields of view. Consequently, the generated fusion results often contain modality-specific regions and fusion artifacts, limiting the comprehensive representation of scene structures and semantic information. To address this challenge, we propose a generat...
  </details>

- **2026-10-26** — Yerim Hong, Sohyun Son, Heeseung Chung et al. — [EXCISE: Locating and Excising Distracting Sentences in Medical Question Answering](http://arxiv.org/abs/2610.35558v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly considered for clinical decision support, where their answers should be grounded in clinical evidence and remain robust to irrelevant information. Prior work shows that a single irrelevant sentence can lower the accuracy of medical models, but not where inside the model its effect can be removed, or how to do so without knowing which sentence it is. We find that blocking attention to a known distractor restores the answer, whereas head masking can suppress correc...
  </details>

- **2026-10-26** — Anushka Agrawal, Adithya A. Vasista, Tanay Nag et al. — [Quantum state revivals, time quasicrystals, and entanglement steering in a Fibonacci-driven central-spin model](http://arxiv.org/abs/2610.35555v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the search for non-equilibrium phases of matter beyond the Floquet paradigm, we propose a route to realize perfect revivals and time quasicrystals (TQCs) in a Fibonacci-driven central-spin model with Ising interactions between the central and satellite spins in the absence of disorder. We analytically demonstrate that when the interaction strength, $λ$ is tuned to $2 m π$, no entanglement is generated between the central and satellite spins at stroboscopic times, independent of the ...
  </details>

- **2026-10-26** — Zhengxin Li, Chongzhen Tian, Hui Yuan et al. — [TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration](http://arxiv.org/abs/2610.35489v1)
  <details><summary>📄 Abstract</summary>
  Deploying large vision-language models (LVLMs) on resource-constrained embodied agents for 3D visual question answering necessitates cloud-edge collaboration. However, offloading massive visual data to the cloud over bandwidth-limited and noisy channels introduces severe latency and transmission distortion. To address this, we propose TP-JSCC, an efficient token pruning and joint source-channel coding method for LVLMs-based 3D-VQA in Cloud-Edge Collaboration. First, we develop a Local and Global...
  </details>

- **2026-10-26** — Radha Krishna Deshpande, Ajoy Mondal, Akash Manna et al. — [Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives](http://arxiv.org/abs/2610.35240v1)
  <details><summary>📄 Abstract</summary>
  India's historical public archives present severe computer vision and document image analysis challenges: decades of parliamentary records survive only as degraded, multi-column scanned pages featuring mixed scripts, complex layouts, and dense visual noise where OCR failure is the primary obstacle to information retrieval. We present an end-to-end framework that couples vision-based layout segmentation and multi-script OCR with an agentic retrieval-augmented generation (RAG) pipeline. Our approa...
  </details>

- **2026-10-26** — Elena Senger, Yuri Campbell, Rob van der Goot et al. — [High Scores, Hidden Failures: Evaluating Codebook-Based LLM Content Analysis](http://arxiv.org/abs/2610.35179v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for codebook-based content analysis in computational social science, where codebooks translate theoretical concepts into labeling schemes. While prior work reports strong predictive performance, it remains unclear whether these systems produce reliable and robust text annotations. We conduct a large-scale empirical failure-mode analysis of LLM-based coding pipelines across four datasets and five models by systematically evaluating their stabilit...
  </details>

- **2026-10-26** — Anda Tang, Junjie Wang, Xuanlin Yang et al. — [UTA: Universal Training Adaptive Learning Rate Decay](http://arxiv.org/abs/2610.35113v1)
  <details><summary>📄 Abstract</summary>
  Learning rate decay (LRD) is critical for training high-performance models, yet most designs remain empirically driven. Although the Universal Budget Aware (UBA) LRD offers a theoretical framework, its reliance on SGD dynamics limits its applicability to modern Adam-type optimizers and leaves its key `optimization difficulty parameter' opaque. To bridge this gap, we propose the Universal Training Adaptive (UTA) LRD. Unlike UBA's fixed offline trajectory anchored solely to iterations, UTA treats ...
  </details>

- **2026-10-26** — Niyar R Barman, Omar Naim, Nicholas Asher — [Rethinking Evaluation for Principled Generalization Using a Kripkean Challenge to Meaning as Use](http://arxiv.org/abs/2610.35111v1)
  <details><summary>📄 Abstract</summary>
  Large language models operationalize an intuitive, view of meaning as use. We argue that it faces a rule-following challenge. Using Kripke's interpretation of Wittgenstein, we argue that finite histories of use do not determine a unique rule for future extension. This reframes the debate about OOD generalization but also about NLP evaluation; benchmarks that measure performance on fixed use cases or local robustness, we argue, do not by themselves establish semantic competence. To evaluate wheth...
  </details>

- **2026-10-26** — Zefeng He, Yichen He, Yuan Lin et al. — [Reinforcement Learning Done Right for Explicit Confidence Targets](http://arxiv.org/abs/2610.35059v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can produce plausible but incorrect answers when they are uncertain, which can mislead users and undermine model reliability. Training models to abstain with reinforcement learning is a natural approach, but most existing methods use a fixed error penalty and therefore cannot adapt their behavior to different confidence requirements at inference time. We study \emph{explicit confidence targets}, where a user specifies a target \(p\) in the prompt and the model direct...
  </details>

- **2026-10-25** — Jun Liu — [Wave Is All You Need: A Quantum Language Model Based on Fully Connected Quantum Boltzmann Machine](http://arxiv.org/abs/2610.34492v1)
  <details><summary>📄 Abstract</summary>
  This work proposes a self-attention mechanism based on the fully connected quantum Boltzmann machine (FC-QBM), and further constructs a fully connected quantum Boltzmann machine language model (FC-QBM-LM) using the mechanism as the core engine. By performing unitary evolution on semantic quantum states, the mechanism implicitly implements positional encoding and self-attention computation, eliminating the need to decompose continuous semantic streams into discrete matrices for explicit matrix mu...
  </details>

- **2026-10-25** — Gyubeum Lim, Yemo Koo, Ghunwoo Jang et al. — [AndroidFlux: Evaluating and Reward Modeling Failure Recovery Capabilities in Mobile Use Multimodal Agents](http://arxiv.org/abs/2610.34384v1)
  <details><summary>📄 Abstract</summary>
  Mobile-use multimodal agents are typically evaluated by task success from a clean initial state, which does not isolate their ability to recover from intermediate errors. Because mobile environments change dynamically, a general mobile-use agent must complete tasks robustly even from unexpected states and in unseen environments. This requires knowing when and where an agent makes errors, and whether it can recover from errors and subsequent states. To evaluate this capability, we introduce Andro...
  </details>

- **2026-10-25** — Yihua Qin, Jiajie Jerry Zhao — [R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents](http://arxiv.org/abs/2610.34185v1)
  <details><summary>📄 Abstract</summary>
  LLM-based sales agents are often evaluated on static policy questions or task success, but deployment asks a sharper question: when a model can state a rule, will it choose compliant, tool-grounded actions under commercial pressure? We introduce R2A-Sales (Rule-to-Action), a policy-atom-matched benchmark for this question. Each item pairs a static probe with a multi-turn sales scenario sharing the same versioned policy atom, facts, evidence, behavioral constraints, and tool contract, so differen...
  </details>

- **2026-10-25** — Sungeun Kim, Mingyu Jung, Yuri Kim et al. — [Single-Cycle Battery Remaining Useful Life Prediction with Compressed Continuous Wavelet Features and Deep Neural Networks](http://arxiv.org/abs/2610.34159v1)
  <details><summary>📄 Abstract</summary>
  Lithium-ion batteries are widely used in industrial applications, but their performance gradually degrades over time, making accurate lifetime prediction important for safety and reliability. However, reliable lifetime assessment generally requires extensive degradation testing, which is both costly and time-consuming. To reduce this burden, recent data-driven approaches have sought to predict the end-of-life cycle of batteries from only the initial few cycles. Nevertheless, identifying reliable...
  </details>

- **2026-10-25** — Zhaoyang Li, Shangzhuo Xie, Qianqian Yang — [AGENS: Agentic Link Construction for Environment and Intent Aware 6G Communication](http://arxiv.org/abs/2610.34131v1)
  <details><summary>📄 Abstract</summary>
  The emergence of diverse intelligent services is driving 6G networks toward an intelligent communication ecosystem with increasingly complex operating scenarios. However, existing AI-based communication methods mainly focus on isolated tasks or individual physical-layer mod- ules, which is insufficient for AI-native 6G systems that must jointly perceive dynamic environments, understand specific user intents, coordinate multiple coupled PHY-layer modules, and remain compatible with existing commu...
  </details>

- **2026-10-25** — Jiaju Huang, Shaobin Chen, Xinglong Liang et al. — [Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents](http://arxiv.org/abs/2610.34167v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language model agents are usually evaluated by whether they finish the user's task. That metric misses a common failure: an agent can complete the requested work while also taking an unauthorized side-effecting action, such as writing to the wrong object, expanding the scope of the request, or contacting an unintended recipient. We call this failure mode collateral damage (CD). We introduce SABench (Side-effect-Aware Benchmark), a benchmark of 201 email, calendar, and ticket tasks. Ea...
  </details>

- **2026-10-25** — Dibakar Datta — [From Autonomous Knowledge Generation to Generalizable Property Prediction: A Precision-First Pipeline for Electro-Optic Materials Discovery](http://arxiv.org/abs/2610.34628v1)
  <details><summary>📄 Abstract</summary>
  Electro-optic materials, whose refractive index changes linearly with an applied electric field (the Pockels effect), set the speed and energy of optical modulators and microwave-to-optical links for quantum computing. Designing better materials requires optimizing composition alongside temperature, strain, and bias field. However, general repositories lack electro-optic tensor data. We present a pipeline that builds such a database from literature following the rule: "no value is better than a ...
  </details>

- **2026-10-25** — Lukas Twist, Xinjian Wu, Jingzhi Gong et al. — [Software Engineering for AI-Driven Science](http://arxiv.org/abs/2610.34573v1)
  <details><summary>📄 Abstract</summary>
  AI has made significant contributions to scientific discovery. Autonomous agents can now independently analyse complex problems, design experiments, write and execute code, analyse findings, and derive scientific conclusions. Nevertheless, errors in AI-generated code, experimental procedures, or evidence interpretation can lead to invalid research conclusions, undermining the reliability and reproducibility of automated scientific discovery. In this vision paper, we propose Software Engineering ...
  </details>

- **2026-10-25** — Julia Wilkins, Wei-Ching Lin, Abinaya Kumar et al. — [STFT Frontend Mismatch in Pretrained Audio Spectrogram Transformers: Analysis and Adaptation](http://arxiv.org/abs/2610.34533v1)
  <details><summary>📄 Abstract</summary>
  Pretrained audio spectrogram transformers are widely used as backbones of machine listening systems for sound event classification. However, they are typically trained using spectrograms with a fixed Short-Time Fourier Transform (STFT) configuration, implicitly binding the model to the time-frequency resolution seen during pretraining. In practice, adapting these systems to new domains or computational constraints often requires different STFT frontend parameters. In this work, we conduct a cont...
  </details>

- **2026-10-25** — Shangxi Wu, Xiaorong Yan, Xiaojun Meng et al. — [Entropic Control for Homeostatic Optimization: Pre-empting Catastrophic Forgetting via Dynamic Feedback](http://arxiv.org/abs/2610.34182v1)
  <details><summary>📄 Abstract</summary>
  Supervised Fine-Tuning (SFT) of LLMs suffers from catastrophic forgetting, and prevailing mitigation strategies struggle to reconcile the plasticity-stability dilemma. To address this, we propose Entropic Control for Homeostatic Optimization (ECHO), a closed-loop control framework. By decomposing the KL divergence, we identify output entropy as a dominant observable component of KL variation. This enables us to leverage entropy as a computationally efficient online proxy to monitor forgetting ri...
  </details>

- **2026-10-25** — Chao Chen, Zhenrong Wang, Jilong Wang et al. — [HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model](http://arxiv.org/abs/2610.34126v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots have recently achieved remarkable success in motion tracking. However, during real-world deployment, robots inevitably encounter dynamics gaps arising from either extra physical disturbances or inaccurate simulation modeling, resulting in a significant training-deployment gap. Therefore, effectively leveraging real-world data to fine-tune policies represents the crucial last mile for robust deployment. To bridge this gap, we propose HumanoidNDM, an online fine-tuning framework fo...
  </details>

- **2026-10-25** — Muhammad Moiz Khalid, Abdur Rehman Tariq, Muhammad Okasha Yamin — [EmoNet: A Lightweight Attention-Based CNN for Speech Emotion Recognition](http://arxiv.org/abs/2610.33977v1)
  <details><summary>📄 Abstract</summary>
  Speech Emotion Recognition (SER) is a fundamental task in affective computing that enables applications such as mental health assessment, human-computer interaction, and automated customer support systems. Accurate emotion classification from speech remains challenging due to variations in speaker style, acoustic conditions, and the high computational cost of modern deep learning approaches. Many existing systems depend on large transformer-based architectures that require substantial computatio...
  </details>

- **2026-10-24** — Haggai Roitman — [The Hitchhiker's Guide to System 1 Models: Fast Decision-Making Beyond LLMS](http://arxiv.org/abs/2610.33775v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models excel at reasoning and generation but their autoregressive, token-by-token inference makes them unnecessarily slow, expensive, and poorly calibrated for the many routine decisions (routing, gating, scoring, classification) that modern AI systems require at sub-second latency. A growing class of models addresses this gap: System 1 decision models, architectures that map an input directly to a typed, structured decision in a single forward pass. This guide provides a comprehe...
  </details>

- **2026-10-24** — Jinhao Zhou, Zhaohan Zhang, Xijian Xu et al. — [Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation](http://arxiv.org/abs/2610.33728v1)
  <details><summary>📄 Abstract</summary>
  In large language model (LLM)-based multi-agent systems, reported confidence increasingly determines the allocation of scarce downstream attention, computation, and decision influence. This makes reporting strategic: an agent may overstate the relevance of its contribution even when its underlying belief is well calibrated. Existing calibration methods largely assume passive reporting and therefore do not address strategic incentives created when confidence determines downstream allocation. We f...
  </details>

- **2026-10-24** — Mohammad Tasin, Sadman Sakib Rahman — [Gain Before Tracking: Compensating Power-Amplifier Nonlinearity and Phase Noise in AFDM Uplinks](http://arxiv.org/abs/2610.33672v1)
  <details><summary>📄 Abstract</summary>
  Affine frequency division multiplexing (AFDM) is a candidate waveform for fast-moving vehicles and satellites, but real transmitters add power-amplifier (PA) compression and oscillator phase noise, and no AFDM receiver corrects both. We show that AFDM's transform treats every component equally in magnitude, so the PA's effect reduces to one gain shared by all components and phase noise to a common rotation that OFDM's standard tracker removes. The order matters: the tracker relies on symbol deci...
  </details>

- **2026-10-23** — Alisson Rosa Pereira, Bruno Iochins Grisci — [Do Language Models Trust Their Own Justifications? A Study on Functional Consistency](http://arxiv.org/abs/2610.32665v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been widely adopted in text classification tasks, where they not only output class predictions but also generate explanations that highlight the tokens deemed most relevant for reaching the predicted label. Yet it remains unclear whether these highlighted elements are behaviorally consistent with the model's own predictions under targeted interventions, which we refer to as functional auto-consistency. While much of the literature evaluates the textual plausibil...
  </details>

- **2026-10-23** — Shashi Kumar, Yanis Labrak, Sergio Burdisso et al. — [Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR](http://arxiv.org/abs/2610.32572v1)
  <details><summary>📄 Abstract</summary>
  Adapting ASR to a domain with only untranscribed audio typically relies on pseudo-labeling, a strong teacher transcribes the audio and a student is fine-tuned on it. Because supervised fine-tuning (SFT) treats every pseudo-label token as a target, the student inherits the teacher's errors. We show that using the same pseudo-labels as a reward reference for Group Relative Policy Optimization (GRPO) is more robust to label noise. In the banking domain, GRPO yields 29.3% to 56.2% relative WER impro...
  </details>

- **2026-10-23** — Xiaoyu Shi, Wenqiang Luo, Boyang Yang et al. — [Beyond Coverage and Mutation: A Blind-Spot Analysis of LLM-Generated Unit Tests](http://arxiv.org/abs/2610.32548v1)
  <details><summary>📄 Abstract</summary>
  Existing evaluation protocols for unit tests rely on aggregate metrics such as branch coverage and mutation score. These metrics quantify the extent to which a test suite exercises program behavior, but do not identify the behavioral obligations it systematically leaves unchecked. We propose BlindSpotEval, an obligation-based evaluation framework aligned with the Arrange-Act-Assert pattern. The framework comprises three metrics, Boundary-Value Adequacy, Control-Flow Adequacy, and Oracle Strength...
  </details>

- **2026-10-23** — Mena Zkhary, Alain Boldini — [Density control of large-scale multi-agent systems via tuning of agent interactions](http://arxiv.org/abs/2610.32778v1)
  <details><summary>📄 Abstract</summary>
  Collective behavior in biological systems emerges through adaptive interactions among units, enabling large populations to coordinate without centralized control. This mechanism raises the question of whether collective behavior in engineered multi-agent systems can likewise be regulated by modifying the interaction law between agents, rather than by directly controlling individual units. To answer this question, we consider large-scale multi-agent systems evolving on a ring and treat the intera...
  </details>

- **2026-10-22** — Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe et al. — [SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](http://arxiv.org/abs/2610.31659v1)
  <details><summary>📄 Abstract</summary>
  Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary...
  </details>

- **2026-10-22** — Mingjie Li, Yukun Jiang, Yicong Tan et al. — [WildFakeToolBench: Benchmarking AI-Generated Image Detectors with Web-Sourced Image Processing](http://arxiv.org/abs/2610.31152v1)
  <details><summary>📄 Abstract</summary>
  As AI generated images are getting popular these days, discussions on such generations are widely existed in current public forums, software repositories, and photography tutorials. Moreover, with the help of LLM-assisted code translation, malicious actors can adopt such information to evade detectors without specialized knowledge or local GPU execution of the resulting tools. To evaluate such risks, we introduce \textsc{WildFakeToolBench}, a benchmark suite of $156$ executable image-processing ...
  </details>

- **2026-10-22** — Qijin Zhang, Hanzhen Wang, Yuehan Zhao et al. — [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](http://arxiv.org/abs/2610.31650v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. ...
  </details>

- **2026-10-22** — Deepthika S, Pawni Yadav, B. Sankar — [Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](http://arxiv.org/abs/2610.31579v1)
  <details><summary>📄 Abstract</summary>
  Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini). Unknown to participants, each assistant's briefing had 0, 25, 50, 75, or 100% of its facts replaced by plausible falsehoods, and ever...
  </details>

- **2026-10-22** — Raffaele Cali, Giuseppe Lando, Rosario Forte et al. — [Retrieval-Augmented Online Textual Memory for Episodic Memory Video Question Answering](http://arxiv.org/abs/2610.31284v1)
  <details><summary>📄 Abstract</summary>
  Long egocentric videos pose a central challenge for multimodal language models: the visual stream must be compressed into a memory representation that can be searched efficiently while still preserving the evidence needed for question answering. Building on an online textual-memory framework in which first-person videos are converted into temporally grounded captions, this work systematically studies the role of retrieval in episodic-memory video question answering. We evaluate how different ret...
  </details>

- **2026-10-22** — Tobias Wech — [LieGROG: A Lie algebra approach for calibrating GRAPPA operators](http://arxiv.org/abs/2610.30927v1)
  <details><summary>📄 Abstract</summary>
  Purpose: In multi-coil acquisitions based on non-Cartesian k-space sampling, image reconstruction using GRAPPA Operator based gridding (GROG) can provide advantages with respect to the non-uniform FFT (NUFFT): It waives both the need for calculating a density compensation function, and for transferring back and forth between Cartesian and non-Cartesian points in iterative algorithms. Non-trivial noise propagation and self-calibration limited to specific trajectories, however, have contributed to...
  </details>

- **2026-10-22** — Jihwan Kim, Jaeseong Heo, Yujin Kim et al. — [Wavenumber-Aware Deep Learning for Robust Analysis of Raman Spectra](http://arxiv.org/abs/2610.30746v1)
  <details><summary>📄 Abstract</summary>
  Machine-learning models for spectroscopy usually treat a spectrum as a fixed-grid intensity vector, leaving the physical coordinate implicit in the array index. Such models are tied to a single sampling grid, spectral range and resolution, which limits their use when measurement conditions change. Here we represent each spectral point as a pair of intensity and wavenumber and compute Transformer positional encodings from the wavenumber itself. On Raman spectra of three bacterial species and thei...
  </details>

- **2026-10-22** — Amirhossein Aghaei, Liangyan Li, Shiyi Yang et al. — [Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference](http://arxiv.org/abs/2610.30611v1)
  <details><summary>📄 Abstract</summary>
  Scaling large language models has substantially improved linguistic fluency, yet reliable autonomous agents require more than fluent generation. In multi-turn inference, current agentic systems often produce semantically plausible but structurally ungrounded reasoning, especially under incomplete observations. We propose Structure-Grounded Uncertainty Reduction (SGUR), a training-free framework that complements token-level generation with active uncertainty reduction over structured hypothesis s...
  </details>

- **2026-10-22** — Jinyu Zhang, Haitao Lin, Jiashu Hou et al. — [F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation](http://arxiv.org/abs/2610.31623v1)
  <details><summary>📄 Abstract</summary>
  This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candida...
  </details>

- **2026-10-22** — Hengyi Sim, Quentin Rouxel, Dennis Hong et al. — [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](http://arxiv.org/abs/2610.30988v1)
  <details><summary>📄 Abstract</summary>
  Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, which enables them to predict how actions affect future states. As such, embedding such world models in robots allows for better generalization i...
  </details>

- **2026-10-22** — Zunnan Xu, Shangchen Zhou, Yihang Luo et al. — [HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](http://arxiv.org/abs/2610.31635v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distan...
  </details>

- **2026-10-22** — Molly Wolfson, Joseph F. Hennawi, Frederick B. Davies et al. — [A Robust Estimator for the Lyman-$α$ Forest 1D Power Spectrum at High Redshift](http://arxiv.org/abs/2610.31626v1)
  <details><summary>📄 Abstract</summary>
  The Lyman-$α$ (Ly$α$) forest flux power spectrum $P(k)$ is sensitive to a range of astrophysical and cosmological effects, including the thermal state of and large-scale fluctuations in the intergalactic medium and the nature of dark matter. Measuring $P(k)$ becomes increasingly challenging at high redshift, where fewer quasar spectra are available and higher Ly$α$ optical depths result in lower transmitted flux. In addition, observational effects and missing data complicate standard Fourier-tra...
  </details>

- **2026-10-22** — Chaoyue Li, Zeyu Gao, Yanfeng Lu et al. — [SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets](http://arxiv.org/abs/2610.31518v1)
  <details><summary>📄 Abstract</summary>
  Task and Motion Planning (TAMP) stands as a fundamental challenge in robotics, essential for enabling autonomous agents to execute complex, long-horizon tasks in diverse environments. While Large Language Models (LLMs) introduce a new paradigm for TAMP by leveraging extensive common sense, their inherent reasoning limitations hinder direct application, and fine-tuning strategies to enhance these capabilities are currently bottlenecked by the scarcity of high-quality datasets. Existing automated ...
  </details>

- **2026-10-22** — Dingxuan Zhang, Yanhui Jiang, Jun Wang et al. — [Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](http://arxiv.org/abs/2610.31461v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execution poses an additional runtime control problem: the same task may be solved through primitive tool calls, macro skills, or hybrid execution that starts with a macro and falls back to micro-level recovery. We introduce ...
  </details>

- **2026-10-22** — Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian et al. — [AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents](http://arxiv.org/abs/2610.31366v1)
  <details><summary>📄 Abstract</summary>
  Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion reco...
  </details>

- **2026-10-22** — Wei Zhang, Ying Feng, Mengtong Wu et al. — [Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention](http://arxiv.org/abs/2610.31320v1)
  <details><summary>📄 Abstract</summary>
  4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We a...
  </details>

- **2026-10-22** — Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss et al. — [nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators](http://arxiv.org/abs/2610.31080v1)
  <details><summary>📄 Abstract</summary>
  Interactive 3D segmentation models such as nnInteractive turn a few spatial prompts (points, scribbles, boxes) into accurate volumetric masks, but a human still does the annotation work: finding each structure, placing prompts, checking the result and correcting it. General-purpose AI agents can now interpret images, call tools and write code. We show that such agents can take over this work without additional training: the user makes a request in plain language, and the agent works out what has...
  </details>

- **2026-10-22** — Diana Nunes, Ricardo Amorim, Pedro Ribeiro et al. — [AERIAL: Mission-Aware LLM Selection for Language-Driven UAV Control in Flying Networks](http://arxiv.org/abs/2610.31029v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) in Flying Networks (FNs) increasingly require mechanisms to translate high-level natural language objectives into executable missions. Although Large Language Models (LLMs) have demonstrated the feasibility of language-driven UAV control, existing approaches typically rely on static model configurations and overlook mission-aware performance variability. This paper presents AERIAL, a benchmark-driven framework for adaptive LLM selection in hybrid edge-cloud UAV co...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 17 papers

- **2026-10-26** — Yanan Wu, Yalin Yang, Chengbin Deng — [ArchiveLens: A Generative Spatial Knowledge Framework for Semantic Reconstruction of Historical Maps](http://arxiv.org/abs/2610.35606v1)
  <details><summary>📄 Abstract</summary>
  Historical maps contain dense morphological and semantic information about past urban environments, but many digitization workflows focus primarily on extracting geometry, and do not capture cartographic semantics such as building use and construction materials. This study introduces ArchiveLens, a generative spatial knowledge framework that operationalizes historical maps as entity-centric, machine-queryable geospatial databases. The pipeline decouples morphological and semantic reconstruction ...
  </details>

- **2026-10-26** — Dimitris Gkoulis — [Making the Telemetry Pipeline Measurable: An Edge IoT Testbed and Dataset for End-to-End Latency, Provenance, and Energy-Aware Benchmarking](http://arxiv.org/abs/2610.35591v1)
  <details><summary>📄 Abstract</summary>
  Edge-centric IoT systems are increasingly evaluated through sensor values or platform features, yet the telemetry pipeline itself, the sequence of sensing, serialization, message mediation, ingestion, and persistence, is rarely released as a measurable object. This limits reproducible benchmarking of timeliness, provenance, and operational cost, especially in early-stage IoT design where real deployments and high-quality open data are often unavailable. I present a measurement-first edge IoT tes...
  </details>

- **2026-10-26** — Firuz Kamalov — [Faithful Explanations under Missing Modalities in Multimodal Dementia Prognosis](http://arxiv.org/abs/2610.35430v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to turn the feature attributions of multimodal prognostic models into narratives for clinicians, yet costly modalities such as amyloid PET and cerebrospinal fluid biomarkers are often missing, and whether these explanations stay faithful under missing evidence has not been tested. We separate two failure points: phantom attribution, in which the model credits modalities that were never observed, and unfaithful narration, in which the report omits, cite...
  </details>

- **2026-10-26** — Zikai Zhou, Jiacheng Sang, Yilin Xu et al. — [Did the Model Use That? Counterfactual Training Boosts Self-Attribution in Language Models](http://arxiv.org/abs/2610.35295v1)
  <details><summary>📄 Abstract</summary>
  A fundamental challenge for explainable and accountable language models is revealing how external information influences their answers. This paper examines whether models are self-attributive: that is, whether they indicate when -- and only when -- their responses to questions are influenced by information provided alongside the question. Furthermore, we explore how self-attribution can be improved through counterfactual training, which explicitly teaches models to distinguish between answers th...
  </details>

- **2026-10-26** — Xiaofei Yu, Kailai Sun, Yanyu Mao et al. — [AgenticCity-Bench: Longitudinal Multimodal Observations of Urban Dynamics with Agentic Reasoning](http://arxiv.org/abs/2610.35293v1)
  <details><summary>📄 Abstract</summary>
  City systems are shaped by interactions among infrastructure, human activity, and environmental conditions. Existing earth observation and urban benchmarks are limited in unified modeling and in capturing their joint dynamics. We introduce AgenticCity-Bench, a longitudinal multimodal benchmark for multi-layer unified state modeling and agentic city task reasoning. The benchmark covers 16 cities in 12 countries across six continents from 2000 to 2025, and includes 18 modalities spanning urban fun...
  </details>

- **2026-10-26** — Tianlei Zhu, Matt White, Xue Liu et al. — [NumTrace: Auditing the Number Provenance of Financial Analyst Agents](http://arxiv.org/abs/2610.34887v1)
  <details><summary>📄 Abstract</summary>
  A numerical claim generated by a financial analyst agent can match a number in a company filing but refer to the wrong entity, concept, period, unit or scope. A check based on reference answers can mark such an answer as wrong but does not explain why it fails. In this paper, we present NumTrace, a new benchmark that audits the provenance of each numerical claim made by financial analyst agents: its source and financial semantics. NumTrace currently has 540 questions over 2,163 SEC EDGAR documen...
  </details>

- **2026-10-25** — Zhengqian Xu, Yasheng Zhang, Chenhua Sun et al. — [From Human Intent to In-Orbit Action: A Self-Learning Large Language Model Agent for 6G Satellite Networks](http://arxiv.org/abs/2610.34387v1)
  <details><summary>📄 Abstract</summary>
  Autonomous control of sixth-generation (6G) low Earth orbit satellite networks is hindered by the gap between high-level human intent and low-level control logic: translating a request such as "uninterrupted Arctic video" into a valid reinforcement learning reward still takes days of manual trial and error, and existing large language model translators cannot learn from the failures of the policies they generate. This article presents ALMOND (Agentic Large-Model-Orchestrated autonomous Network D...
  </details>

- **2026-10-25** — Yiyuan Yao, Xinpeng Ding, Minglei Chen et al. — [Explaining Navigation Decisions: Stage-Aware Visual Attribution for Vision-Language Navigation](http://arxiv.org/abs/2610.34028v1)
  <details><summary>📄 Abstract</summary>
  As Vision-Language Models (VLMs) increasingly enable robots to follow language instructions, understanding their navigation decisions becomes important for reliable deployment. Existing explainability methods overlook a key challenge in Vision-Language Navigation (VLN): evidence for the current action may be distributed across historical and current observations and associated with different instruction stages. We identify instruction-stage insensitivity, where existing methods produce similar e...
  </details>

- **2026-10-25** — Zhe Xu, Tianhao Liao, Zhenqing Ling et al. — [Rethinking Retrieval in the Long-Context Era: Training-Free Semantic Trees for Adaptive Context Construction](http://arxiv.org/abs/2610.34146v1)
  <details><summary>📄 Abstract</summary>
  Long-context language models can increasingly process entire documents, making full-context prompting a practical alternative to passage retrieval. However, greater capacity determines how much information a model can receive, but not which information best supports a query. This distinction motivates rethinking retrieval: when the full document already fits, can selecting and organizing its evidence improve answering? The challenge is to retain supporting facts and relations while keeping the c...
  </details>

- **2026-10-24** — Zefang Liu, Chenyang Zhu, Sangwoo Cho et al. — [RoleHear: Pseudo-Labeling for Semi-Supervised Role-Attributed Streaming Speech Recognition](http://arxiv.org/abs/2610.33765v1)
  <details><summary>📄 Abstract</summary>
  Streaming automatic speech recognition transcribes at low latency but produces an unattributed word stream, while real-time applications such as customer-service analytics need each word tied to a speaker role. Role attribution is usually a separate stage, either an offline or streaming speaker-diarization model aligned to the words or a text-based large language model applied to the transcript, and role labels for training are scarce. We present RoleHear, a semi-supervised pipeline that makes a...
  </details>

- **2026-10-23** — Garima Agrawal, Prasun Das, Akshay Sarvade et al. — [Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves](http://arxiv.org/abs/2610.32851v1)
  <details><summary>📄 Abstract</summary>
  Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 services into thousands of artifacts describing scope, journeys, rules and acceptance criteria. Recovery does not confer usability. Entities like offer, eligibility, and activation recur across services under a shared vocab...
  </details>

- **2026-10-23** — GuangXue Zhang, Nada Lahjouji, Yiming Lin et al. — [OCTOPUS: Towards A Tag Model for Cross-Query Reuse in Semantic Query Processing](http://arxiv.org/abs/2610.32586v1)
  <details><summary>📄 Abstract</summary>
  Large language models make it possible to pose semantic questions over diverse, multi-modal data. Recent systems give such workloads the declarative feel of a database through semantic operators: relational operators whose conditions a model judges. Most of them now run on a relational engine, yet almost none keeps what the model says past the query: every judgment is discarded on completion and paid for again the next time a query needs it. We present the tag model and tag operators, the right ...
  </details>

- **2026-10-22** — Maria Gabriela Alves Zuppardo, Vinicius Cardoso Garcia — [Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines](http://arxiv.org/abs/2610.31280v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM pipelines are often credited with gains in software engineering tasks, but it is rarely clear whether a gain stems from the typed contract between agents or from the specialized prompts that decomposition enables. We study this attribution problem in Requirements Engineering, comparing three architectures for classifying requirements as functional or non-functional and then prioritizing them with MoSCoW: a single-call baseline; a two-call variant that reuses the pipeline's specia...
  </details>

- **2026-10-22** — Tirana Noor Fatyanosa, Ummu Ditya Erliana, Mahendra Data et al. — [IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark](http://arxiv.org/abs/2610.31256v1)
  <details><summary>📄 Abstract</summary>
  Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource languages such as Indonesian by the absence of public domain-specific data. We introduce IndoNutriQA, an expert-curated Indonesian clinical QA benchmark of 911 question-answer pairs built from real clinical-nutrition reports. Rather than a large-scale training corpus, it is positioned as a high-quality evaluation resource: every pair is grounded in a clinica...
  </details>

- **2026-10-22** — Xiaoao Zhu, Ni Zhang, Jie Ren et al. — [ATLAS: A Multi-Agent Framework for Lifting Binary to Canonical Compiler IR](http://arxiv.org/abs/2610.30877v1)
  <details><summary>📄 Abstract</summary>
  Lifting stripped, heavily optimized binaries to a canonical, pre-optimization LLVM intermediate representation (IR) is essential for downstream security analysis and legacy software migration when source code is unavailable. However, aggressive compiler optimizations rewrite control and data flow, remove structural metadata, and introduce type-erased low-level idioms, causing current lifters to produce malformed or semantically divergent IR. We present ATLAS, a multi-agent framework designed to ...
  </details>

- **2026-10-22** — Jie Ying, Xutao Zhang, Ningyuan Chen et al. — [AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes](http://arxiv.org/abs/2610.30738v1)
  <details><summary>📄 Abstract</summary>
  When tool-use agents write files, execute code, or send data, their final responses do not explain the resulting security events, and heterogeneous runtimes expose the relevant evidence through incompatible interfaces. We present AgentTriage, an executable contract for replayable security diagnosis across heterogeneous runtimes. The contract admits conclusions whose claims cite canonical runtime events and requires abstention when mandatory evidence is missing. Runtime overlays normalize native ...
  </details>

- **2026-10-22** — Jiajun Wu, Jian Yang, Yaxin Du et al. — [ProductWebBench: Evaluating Website Continuity Beyond Task Completion](http://arxiv.org/abs/2610.31118v1)
  <details><summary>📄 Abstract</summary>
  Frontend coding agents are usually graded on one question: did the requested target get built. Real engineering changes carry a second obligation, because the rest of the site has to keep working. We call that second obligation website continuity, and introduce ProductWebBench, a benchmark that scores both on living frontend repositories: 320 Change tasks over existing code and 80 long-horizon Build tasks. Every task freezes a repository snapshot, staged requirements, browser evidence and determ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-25** — Szymon Mazurek, Alberto Presta, Michał Byra — [Recursive CLIP: Vision-Language Distillation with Looped Transformer Blocks](http://arxiv.org/abs/2610.34563v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language models such as CLIP typically rely on independently parameterized transformer blocks across depth. We investigate the extent to which these blocks can instead be reused recurrently while preserving the transferable capabilities of CLIP. We study recursive transformer backbones in which a small set of $N$ transformer blocks is applied $M$ times per forward pass. By holding $N \cdot M$ fixed to the depth of a standard ViT-B, our models preserve computational depth while...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-10-26** — Chenye Han, Hongche Yu, Mengyue Wu et al. — [Learning to Remember: Advances in Memory Mechanisms for Large Language Models](http://arxiv.org/abs/2610.35089v1)
  <details><summary>📄 Abstract</summary>
  Memory has become a central mechanism for extending large language models (LLMs) beyond fixed context windows, stateless interaction, and static parametric knowledge. This survey organizes the literature around three complementary dimensions: the life cycle of memory, the storage substrate, and the system role that memory plays in LLM-based agents, while using cognitive-science-inspired memory concepts as a lightweight conceptual motivation rather than as a separate technical contribution or imp...
  </details>

- **2026-10-26** — Shaohuai Feng, Mohd Wira Mohd Shafiei, Mohd Sukri Shafie et al. — [When Respondents Are Scarce: LLM-Derived Semantic Priors for Bayesian Confirmatory Factor Analysis](http://arxiv.org/abs/2610.34843v1)
  <details><summary>📄 Abstract</summary>
  Across social and behavioral research, measuring latent constructs can be challenging when target populations are small or difficult to reach. Recruiting additional respondents may be costly or infeasible, leaving researchers with limited data for estimating questionnaire factor structures. Yet item wording contains structural expectations before data collection, and whether these can improve small-sample estimation without replacing empirical validation remains unclear. We introduce the Semanti...
  </details>

- **2026-10-26** — Loc X. Nguyen, Huy Q. Le, Ji Su Yoon et al. — [Networked Humanoid Intelligence: Communication, Coordination, Collaboration, and Social Interaction](http://arxiv.org/abs/2610.34740v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots are moving from laboratory platforms toward connected fleets that share workspaces, infrastructure, tasks, and knowledge with other robots and humans. As deployments grow, the operation and improvement of each humanoid depend on information exchanged across the network. However, existing research has largely studied humanoids as individual systems. This survey examines networked humanoid intelligence through four functions of information exchange: communication, coordination, col...
  </details>

- **2026-10-22** — Tamer Abdelaziz — [What Ethereum Developers Ask For, and Whether They Get It: Ten Years of Ethereum Stack Exchange](http://arxiv.org/abs/2610.30829v1)
  <details><summary>📄 Abstract</summary>
  The Ethereum community learns where developers struggle through surveys and interviews, which record what developers say when asked about a chosen theme. Ethereum Stack Exchange (ESE) records what they ask for unprompted, and whether anyone resolves it. We study every question posted to ESE from Jan 2016 to Dec 2025, 54,637 in all, and label each with a prompt-based topic pipeline seeded with eight Ethereum-specific topics and open to new ones (22 topics in all). A three-provider committee of la...
  </details>

- **2026-10-22** — Robin Quériaux, Solveig Bachellery, Léa Déléris et al. — [VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act](http://arxiv.org/abs/2610.31588v1)
  <details><summary>📄 Abstract</summary>
  Institutions that deploy large language models in regulated settings often need technical evidence of responsible AI practices before approving a deployment. COMPL-AI provides a technical interpretation of the EU AI Act that organises this evidence under six principle groups and eighteen technical requirements, twelve of which current benchmarks can measure. The benchmark suites that produce this evidence are typically operated from a command line, while the staff who approve deployments are non...
  </details>

- **2026-10-22** — Yusuke Kumagae, Masahiro Kaneko — [Silicon Samples Match the Answers but Not the Respondents](http://arxiv.org/abs/2610.30900v1)
  <details><summary>📄 Abstract</summary>
  Silicon sampling generates survey respondents by having a large language model (LLM) answer a survey as a person with given demographic attributes, and the resulting synthetic populations are increasingly used in place of human ones. Existing evaluations focus on individual-answer accuracy, per-question answer distributions, and correlations across questions. None of these compares the respondents themselves, so a generator whose respondents have combinations of answers found in no human respond...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 179 papers

- **2026-10-26** — Yucheng Wu, Chengyi Xie, Chenpeng Wang et al. — [CANS: Capability-Preserving Neuron Steering for Large Language Models](http://arxiv.org/abs/2610.35530v1)
  <details><summary>📄 Abstract</summary>
  Activation steering offers training-free and dynamic control of target behaviors in large language models, but existing methods can impair general capabilities and require domain-specific intervention designs. We introduce Capability-Preserving Neuron Steering (CANS), a unified framework that balances target-behavior control with capability preservation. To make target-behavior improvement and general-capability preservation tractable, we introduce two proxies: log-probabilities of target tokens...
  </details>

- **2026-10-26** — Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin — [Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning](http://arxiv.org/abs/2610.35477v1)
  <details><summary>📄 Abstract</summary>
  As AI coding assistants generate more code, the need to review it for security flaws grows. Existing approaches leave a gap: static analyzers identify program sites but offer little explanation, while language-model explanations can be difficult to verify. Small open-weight code models could make security review available without sending proprietary code to a hosted service. We study whether fine-tuning helps these models turn security evidence into explanations that developers and tools can che...
  </details>

- **2026-10-26** — Zhiwei Xu, Xuyang Liu, Xiaolin Peng et al. — [TrustJev: Separating Policy Authority from Untrusted Evidence in LLM-Based Decisions](http://arxiv.org/abs/2610.34826v1)
  <details><summary>📄 Abstract</summary>
  Decision models enable software to select from predefined actions using natural language inputs. However, the external evidence that supplies facts for these decisions may also contain instructions that attempt to override the application's policy. We propose TrustJev, a framework combining protected policy scoring with bounded evidence corrections. A single Transformer backbone computes policy scores and a correction budget from trusted policy and candidates, then bounds evidence corrections by...
  </details>

- **2026-10-26** — Xi Chen, Chongjian Ge, Yiran Xu et al. — [Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](http://arxiv.org/abs/2610.35866v1)
  <details><summary>📄 Abstract</summary>
  As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark for evaluating autonomous research systems and discovering ideas in language modeling. Arena supports diverse research objectives within a shared experimental environment by separating admissibility from improvement: model quality and resource constraints determine whether a result qualifies, while...
  </details>

- **2026-10-26** — Yangge Li, Katherine Braught, Alex Yuan et al. — [Verse: Semantics and Verification of Hybrid Multi-Agent Scenarios](http://arxiv.org/abs/2610.35680v1)
  <details><summary>📄 Abstract</summary>
  Verifying cyber-physical systems with many interacting agents remains difficult because interactions are mediated by sensors, individual decisions are constrained by environment (map) structure, and the resulting mode space scales combinatorially. We present Verse, a framework for writing agents, maps, and sensors in a familiar programming language syntax, with a formal semantics for the resulting scenarios. A compiler translates each scenario to a hybrid automaton whose executions correspond ex...
  </details>

- **2026-10-26** — Till Hielscher, Fabio Scaparro, Kai O. Arras — [Context-Aware Generation and Modulation of Expressive Motion Behavior using Multimodal Foundation Models](http://arxiv.org/abs/2610.35615v1)
  <details><summary>📄 Abstract</summary>
  Expressive robot motion positively impacts human-robot interaction by improving user engagement, likability, or task performance. We present a novel approach to automatically generate and modulate complex, expressive full-body gesture sequences from a multimodal (text, audio, video) context description. Based on a unified mathematical implementation of the Principles of Animation using Dynamic Movement Primitives, we use multimodal foundation models to generate such sequences along with parametr...
  </details>

- **2026-10-26** — Heyang Yu, Haomin Li, Sihang Li et al. — [RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies](http://arxiv.org/abs/2610.35604v1)
  <details><summary>📄 Abstract</summary>
  Generalist robot policies and language-model agents provide complementary capabilities, but completing a task also requires adapting their use to the consequences of physical interaction. We study execution as a locus of adaptation: feedback guides the current action and supplies evidence for revising subsequent decisions under fixed model weights. We introduce RoboDoctor, a training-free framework that connects diagnosis, grounded action, and persistent experience across three revision targets....
  </details>

- **2026-10-26** — Patrick Reichherzer, Jonathan Evertz, Thorsten Holz — [Amplify, Locate, Estimate (ALE) on Rare-Failure Rates of Fine-Tuned LLMs](http://arxiv.org/abs/2610.35472v1)
  <details><summary>📄 Abstract</summary>
  Safety fine-tuning can make undesirable model behaviors sufficiently rare that measuring their frequency by direct sampling becomes prohibitively expensive. We introduce Amplify, Locate, Estimate (ALE), a method for estimating such rare failure probabilities efficiently. ALE uses the change in token log-probabilities induced by the safety fine-tuning to define an amplification direction, along which we increase the failure rate for cheap measurement. We develop a score-function estimator that us...
  </details>

- **2026-10-26** — Vahagn Aslanyan — [Modular Existential Closedness](http://arxiv.org/abs/2610.35409v1)
  <details><summary>📄 Abstract</summary>
  We prove the Modular Existential Closedness conjecture for the modular $j$-function extended from the upper half-plane to $\mathbb{C} \setminus \mathbb{R}$ by Schwarz reflection. Specifically, we show that any system of equations involving the field operations and $j$ has solutions in the complex numbers unless it is overdetermined. Such a system is overdetermined if, roughly, there are more independent equations than variables, possibly after applying the transformation rules of the $j$-functio...
  </details>

- **2026-10-26** — Jiacheng Zhang, Xueyi Zhang, Xin Lu et al. — [OneEEG: A Unified Signal-Visual Multimodal Language Model with Task-Aware Mixture of Projectors for Multi-Task EEG Understanding](http://arxiv.org/abs/2610.35355v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) is widely used in clinical assessment, brain-computer interfaces, and cognitive-state analysis, yet EEG modeling remains fragmented across task paradigms. Recent multimodal large language models (MLLMs) provide a promising interface for flexible multimodal reasoning, but their ability to understand EEG inputs remains limited. In this work, we propose OneEEG, a unified EEG-MLLM framework for multi-task EEG understanding. By training on our curated OneEEG-Instruct, a m...
  </details>

- **2026-10-26** — Husein Zolkepli — [The Voice on the Line](http://arxiv.org/abs/2610.35272v1)
  <details><summary>📄 Abstract</summary>
  A transcriber listening through one microphone also hears everyone near it. We train causal voice isolators: masking transformers of 140M, 243M and 374M parameters, 20 ms of latency, enrolling the caller from the call itself. Short evaluation windows hide two failures that real calls expose: forgetting the caller when another voice talks alone for a while, and damaging a caller who is alone. Long calls with turns, memory beyond the attention window, real headset crosstalk and drifting caller lev...
  </details>

- **2026-10-26** — Diantao Tu, Yangdong Liu, Niannian Dai et al. — [RetroNav: Scene-Grounded Retrospection and Retry for Self-Evolving Lifelong Navigation](http://arxiv.org/abs/2610.35172v1)
  <details><summary>📄 Abstract</summary>
  Existing robot navigation methods primarily focus on isolated tasks, overlooking the need to accumulate knowledge and experience across repeated navigation episodes. Although recent lifelong navigation methods have explored cross-task knowledge accumulation, they mainly focus on scene knowledge while neglecting historical navigation experience and its connection to scene evidence, limiting the ability to reflect on past mistakes and improve future decisions. To address this limitation, this pape...
  </details>

- **2026-10-26** — Dianyi Yang, Mengya Liu, Zhumei Wang et al. — [Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data](http://arxiv.org/abs/2610.35075v1)
  <details><summary>📄 Abstract</summary>
  Learning generalizable humanoid loco-manipulation remains bottlenecked by costly real-world demonstrations. Simulation provides a scalable alternative, but requires visually faithful, physics-ready scenes and executable whole-body motions. We present Zero-HLM, a real-to-sim-to-real framework that transforms smartphone captures and simulated source demonstrations into scalable training data for humanoid loco-manipulation. Gaussian-guided agentic real-to-sim reconstruction aligns visual and physic...
  </details>

- **2026-10-26** — Hamed Araab, Abbas Ahmadi, Mohammad Hossein Basiri — [Joint Dynamic Lane Reversal and Variable Speed Limit Control: A Graphormer-Based Approach](http://arxiv.org/abs/2610.35070v1)
  <details><summary>📄 Abstract</summary>
  Connected and automated vehicles could allow reassigning lane directions and speed limits on every road frequently, but the benefit hinges on how traffic reroutes, and one-way roads can isolate junctions. We formulate network-wide dynamic lane allocation and directional speed limit control with one-way roads, lane clearing before each reversal, and a navigable graph kept strongly connected at all times. An action-resolution algorithm grounded in graph orientation theory admits a proposal closing...
  </details>

- **2026-10-26** — Tao Ren, Hui Yang, Jia Deng et al. — [Multiscale Policy Optimization for Long-Horizon LLM Agents](http://arxiv.org/abs/2610.35013v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. We propose Multiscale Policy Optimization (MPO), combining Multiscale Advantage Estimation (MAE) and turn-level importance sampling to align credit assignment and policy updates at the turn scale. Extensive experiments ac...
  </details>

- **2026-10-26** — Ye Li, Haoran Ding, Huanan Liu et al. — [GUIFlow: Temporal Redundancy-Aware Incremental Inference for GUI Agents](http://arxiv.org/abs/2610.34959v1)
  <details><summary>📄 Abstract</summary>
  GUI agents built on vision-language models interact with continuously evolving interfaces, yet conventional inference repeatedly recomputes representations of largely overlapping observations and histories. This mismatch makes multi-step interaction costly, while changes in context, interface content, and action arguments prevent straightforward cache reuse. We introduce GUIFlow, a framework for full-pipeline incremental inference in multi-image GUI interaction. Our central insight is that advan...
  </details>

- **2026-10-26** — Jinxiang Xie, Zihao Li, Rui Ding et al. — [Semantic Atoms for Scalable Text Analysis in Data Analytics in the Era of LLM-Based Agents](http://arxiv.org/abs/2610.34860v1)
  <details><summary>📄 Abstract</summary>
  Much of the information needed for data analysis is buried in text columns: an analyst may infer customer frustration from complaint text and use it to explain resolution time. We call workloads in which processing text columns is central to subsequent data analysis TADA (\emph{Text Analysis in Data Analytics}). In an agentic setting, the user's query dynamically specifies this processing, and answering it interleaves LLM-based semantic steps with exact SQL or Python operations. This mixed execu...
  </details>

- **2026-10-26** — Xinyi Ni — [Position Matters More Than Channel: Talking a Language Model Out of a Correct Answer](http://arxiv.org/abs/2610.34809v1)
  <details><summary>📄 Abstract</summary>
  Language models now answer questions alongside other claims: a note in the system prompt, a message from another agent, their own earlier answer. We ask what it takes to talk a model out of an answer it gets right on its own, and separate three factors that earlier studies vary together: where the advice sits in the prompt, who is said to have written it, and what the model has already written. On Qwen3.5-27B and four-option MMLU-Pro items, with the rest of the advice held fixed in each comparis...
  </details>

- **2026-10-26** — Zhenshuai Yin, Jianshu Liang, Xuyue Xiong et al. — [LADDER: Diagnosing Domain-Level Self-Assessment Under Noisy Feedback](http://arxiv.org/abs/2610.34737v1)
  <details><summary>📄 Abstract</summary>
  Knowing when they are reliable is essential for language models to support human-AI collaboration. Yet interaction feedback is not always complete or correct, and may mislead models' understanding of their own capabilities. We introduce LADDER to study how language models assess themselves under unreliable feedback. Our findings show that models can accurately report supplied performance information while still struggling to form trustworthy self-assessments from interaction experience. Apparent...
  </details>

- **2026-10-26** — Wenhan Xiao, Ziwei Zhang, Xingcheng Fu et al. — [SKALOS: Learning to Distinguish Similar Skills with Capability Graphs](http://arxiv.org/abs/2610.34728v1)
  <details><summary>📄 Abstract</summary>
  Skills provide LLM agents with reusable procedural knowledge, making appropriate skill selection essential for reliable agent behavior. As skill libraries expand, distinguishing semantically similar candidates becomes increasingly difficult. Existing methods encode or rewrite skill descriptions for relevance-based ranking, yet heterogeneous descriptions can obscure capability differences. To address this challenge, we propose SKALOS, a graph-native reranker that compares skills via explicit capa...
  </details>

- **2026-10-26** — Pingchuan Ma, Bohan Jiang, Chengshuai Zhao et al. — [DPE-Rec: Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction](http://arxiv.org/abs/2610.34700v1)
  <details><summary>📄 Abstract</summary>
  Generative bundle construction completes a partially observed bundle by generating its missing items from a large product catalog. Compared to autoregressive LLMs, diffusion LLM emerges as a natural fit for this unordered generation task. Their bidirectional attention provides an inductive bias better aligned with unordered bundle construction. Iterative denoising can reveal multiple tokens per step, potentially reducing inference latency. However, directly applying DLMs to this task presents tw...
  </details>

- **2026-10-26** — Yifei Yao, Yude Zou, Guanbo Jiao et al. — [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](http://arxiv.org/abs/2610.35832v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be thoroughly evaluated. In this report, we evaluate GPT-6-Astra on EBench as the core of an agent that controls a robot through an agent harness under the same visual and proprioceptive observation protocol as post-trained po...
  </details>

- **2026-10-26** — Benjamin Pikus, Daniel Saunders, Mircea Mironenco et al. — [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](http://arxiv.org/abs/2610.35817v1)
  <details><summary>📄 Abstract</summary>
  A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot via a simple tool harness. We use a pretrained 27B parameter model to bootstrap world understanding and reasoning, followed by supervised fine-tuning and GRPO on simple simulated tasks to teach it how to move the robot....
  </details>

- **2026-10-26** — Lei Zhao, Zongheng Cao, Xinyu Hu — [When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing](http://arxiv.org/abs/2610.35497v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has shown promise for training multimodal agents to reason and use tools. However, it remains unclear when fine-grained credit assignment improves learning and when it fails to improve task performance. Video editing provides a useful testbed for this question, combining multimodal perception, long-horizon planning, and tool use with delayed outcome feedback. We construct four movie-trailer editing task types---Content Selection, Narrative Sequencing, Rough Cut, and F...
  </details>

- **2026-10-26** — Hongcheng Gao, Zelin Zheng, Alex Zhou et al. — [EmbodiedLab: Benchmarking Embodied Agents That Act to Know](http://arxiv.org/abs/2610.35385v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents are expected to accomplish real-world goals by deciding for themselves how and when to interact with their surroundings. For many such goals, changing the physical state of the world is the means rather than the end: the agent changes the state of a system through interaction, observes the feedback, and explores until it either achieves the goal itself (e.g., discovering physical laws) or learns what the goal requires; it acts to know. Manipulation benchmarks stop at acting to ch...
  </details>

- **2026-10-26** — Shirong Guo, Hongming Zhou, Muhammad Attique Khan et al. — [Uncertainty-Guided Counterfactual Sensor Selection and Safety-Gated Recognition for Autonomous Sensing Agents in IoT Systems](http://arxiv.org/abs/2610.35344v1)
  <details><summary>📄 Abstract</summary>
  Autonomous IoT systems rely on distributed sensing, but sensor faults and communication loss can leave multichannel evidence incomplete or unreliable. Their agents must therefore classify measurements, assess evidence sufficiency, select a sensor to reacquire, and hand off unsafe decisions. We formulate counterfactual sensing: a degraded window defines the factual state, each candidate restoration defines a controlled alternative, and a pre-request utility model estimates loss reduction. Physics...
  </details>

- **2026-10-26** — Shitong Liu, Jingwei Zhang, Sheng Lian et al. — [Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories](http://arxiv.org/abs/2610.35252v1)
  <details><summary>📄 Abstract</summary>
  Realizing Embodied AI for Science requires robots to translate experimental goals into reliable physical procedures, reducing hazardous and repetitive human work while generating evidence for scientific discovery. Although language-based planning and learned manipulation provide complementary capabilities, their integration requires robots to adapt subsequent operations to actual execution outcomes. For example, an unsuccessful placement changes what must be done next, even when the experimental...
  </details>

- **2026-10-26** — Ankit Sonthalia, Arnas Uselis, Seong Joon Oh — [Do vision models know that three is three?](http://arxiv.org/abs/2610.35857v1)
  <details><summary>📄 Abstract</summary>
  Do vision models encode the transition $2{\to}3$ the same way whether it appears in handwritten digits or in hand gestures, and do they "understand" that clean${\to}$dirty is the same transformation regardless of whether it is applied to a kitchen or a carpet? The linear representation hypothesis (LRH) answers this for language models: concept changes correspond to directions in (language) embedding space. In vision, the same concept can manifest in visually unrelated "regimes" that rarely co-oc...
  </details>

- **2026-10-26** — Mingyang Song, Mao Zheng, Zhiyuan Ma et al. — [Understanding Jev-Style System One Models: Does Structure Reduce Selection Bias?](http://arxiv.org/abs/2610.35826v1)
  <details><summary>📄 Abstract</summary>
  Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior have produced a growing family of models that predict probabilities directly over supplied candidates. Yet systematic comparisons of selection bias across Jev versions, Jev reproductions, and generative LLMs remain limited in multi-option tasks. This leaves a central question: does Jev-style decisi...
  </details>

- **2026-10-26** — Sadam Hussain, Mansoor Ali, Daly Betzabeth Avendaño-Avalos et al. — [Explainable Multimodal AI Approach to Reduce Unnecessary Breast Biopsies](http://arxiv.org/abs/2610.35704v1)
  <details><summary>📄 Abstract</summary>
  Recently, there has been rise in multimodal vision-language models for computer-aided diagnosis (CAD), yet their application in breast diagnosis, particularly for predicting biopsy outcomes remains limited. This study presents a multimodal vision-language approach, incorporating Grad-CAM as an Explainable AI (XAI) technique, to predict benign tumors in patients recommended for biopsy, especially those classified as BI-RADS 4 and 5. A novel multimodal framework was devel- oped using Vision Transf...
  </details>

- **2026-10-26** — Elias Hofele, Thomas Trapp, David Timmermann et al. — [TrySee: Modular Perception-Enhanced VLM Grounding for Closed-Loop Robot Task Planning in Specialized Domains](http://arxiv.org/abs/2610.35687v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) have shown impressive capabilities in high-level reasoning and task planning for robots. However, specialized domains remain a challenge for VLMs' image interpretation and grounding abilities. We introduce TrySee, a modular closed-loop robot task planning pipeline integrating general-purpose VLM reasoning with domain-specific perception and established robotics components. The system consists of an inherently reactive cyclic planning pipeline, augmented with domain-...
  </details>

- **2026-10-26** — Zihua She, Xiao Wang — [KAPPA: Checking the Proofs in Statistics Papers with Lean 4 and Language Model Agents](http://arxiv.org/abs/2610.35596v1)
  <details><summary>📄 Abstract</summary>
  Papers in statistical theory rest on long proofs that few readers check line by line. We present KAPPA (Kit of Agents for Proof-checking Papers with a proof Assistant), open-source software that organizes language model agents, run by Claude Code, to translate the proofs of a LaTeX paper into the proof assistant Lean 4 with its library Mathlib and check them there, result by result. Each numbered result receives one of four verdicts: verified unconditionally; verified conditionally, with every c...
  </details>

- **2026-10-26** — Jiří Adam, Andrei Alexandru, Navdeep Singh Dhindsa et al. — [Negative-Power Density of States in Chiral-Orthogonal Disordered Systems and the IR Phase of QCD](http://arxiv.org/abs/2610.35524v1)
  <details><summary>📄 Abstract</summary>
  The recently discovered IR phase of QCD is characterized by an infrared (IR) sector of Dirac modes that separates and dynamically decouples from the bulk of the spectrum, becoming scale invariant in the process [1]. Among key features of this IR sector is the negative power-law behavior of Dirac spectral density near zero with power $p$ close to $-1$. Here we start investigating to what extent can this behavior be mimicked by chiral Anderson models. In particular, we study 3-D chiral-orthogonal ...
  </details>

- **2026-10-26** — Ana-Maria Raclariu, Binsong Xiong — [On memory effects in odd spacetime dimensions](http://arxiv.org/abs/2610.35283v1)
  <details><summary>📄 Abstract</summary>
  We establish the existence of a new electromagnetic memory effect in all odd spacetime dimensions. This effect is a universal property of electromagnetic fields sourced by charged particles of constant momenta, appears at the Coulombic order and is directly related to the Weinberg soft theorem. We provide a unified derivation of this effect in all higher dimensions by evaluating the Maxwell constraint on a null plane at large, finite distance. We observe that in odd spacetime dimensions, the lig...
  </details>

- **2026-10-26** — Malik Marmonier, Benoît Sagot, Rachel Bawden — [The Lay of the Land in Idiom-Translation Quality Estimation](http://arxiv.org/abs/2610.35261v1)
  <details><summary>📄 Abstract</summary>
  Idioms have long been a challenge for machine translation, and while large language models (LLMs) have proven increasingly adept at handling them, whether quality estimation (QE) systems have kept pace and can reliably score idiomatic renderings of these expressions above faulty literal ones remains unclear. We introduce the first parallel dataset pairing idiom-bearing English sentences with both literal and idiomatic translations across nine target languages, augmented into multi-sentence segme...
  </details>

- **2026-10-26** — Ngoc-Duy Mai, Ha-Thanh Nguyen, Hideaki Takeda — [Beyond Vision-Language Models: Visual-Semantic Affect Graphs for Emotion Recognition in Artworks](http://arxiv.org/abs/2610.35244v1)
  <details><summary>📄 Abstract</summary>
  Emotion recognition in artworks remains challenging because affective meaning is often subjective, implicit, and shaped by relationships between visual form and semantic associations. While vision-language models provide strong multimodal representations, direct image-to-emotion prediction may overlook explicit relations among formal, semantic, and affective cues that support emotional interpretation. This paper proposes Visual-Semantic Affect Graphs (VSAG), a graph-based framework that represen...
  </details>

- **2026-10-26** — F. Marini, M. Bellato, A. Bergnoli et al. — [A Congestion-Aware RDMA Front-End for LST Advanced Camera Readout](http://arxiv.org/abs/2610.35171v1)
  <details><summary>📄 Abstract</summary>
  The Advanced Camera (AdvCam) upgrade of the Large-Sized Telescopes (LSTs) calls for a fully digital readout in which each front-end board streams data to the event-building servers over commercial 10 Gb/s Ethernet, using an FPGA implementation of Remote Direct Memory Access (RDMA) over Converged Ethernet v2 (RoCEv2). In a previous work, a customized RoCEv2 core integrated with the SLAC SURF UDP/MAC stack was shown to sustain near-line-rate data transfers from a Xilinx KCU105 to a server equipped...
  </details>

- **2026-10-26** — Emanuel Dopater, Daniel Gavlas, Lukáš Jochymek et al. — [Toward Fast Human Reaction Modeling from High-Frequency Digital Interaction Data](http://arxiv.org/abs/2610.35079v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether limbic-like signatures of rapid, salience-driven behavior can be identified in high-resolution Counter-Strike 2 telemetry. This exploratory study introduces Ego-Knowledge, a leak-reduced reconstruction of each player's plausible perceptual state, supported by a millisecond-precision visibility engine and a reaction-centered extraction pipeline. Using a neuroscience-motivated 60--120 ms window, we derive coarse fight-or-flight labels from visibility- and damage-triggered ev...
  </details>

- **2026-10-26** — Abhinav Sudhakar Dubey, Vidushi Goel, Kiran Rana et al. — [Improving VLMs on Scientific Chart Analysis via Autonomous Evolution](http://arxiv.org/abs/2610.35077v1)
  <details><summary>📄 Abstract</summary>
  Understanding and operating with scientific charts is a standard approach in data analysis, and while humans are good at interpreting such charts, open vision-language models (VLMs) are known to perform poorly when it comes to question answering based on such data types. Motivated by an initial observation that many of their errors are due to inexact answering, we raise the following natural question: how much accuracy can we recover without changing the model at all? In this paper, we study thi...
  </details>

- **2026-10-26** — Xinyu Sun, Zhangyue Yin, Xinyi Ju et al. — [Critic's Eye: Review-Grounded Graph Reasoning for Long-Form Motif Discovery](http://arxiv.org/abs/2610.35011v1)
  <details><summary>📄 Abstract</summary>
  Deep narrative understanding requires distinguishing what happens from how it is presented, moving beyond the chronological fabula to decode the sjuzet, the discursive organization through which themes are staged. We study this through the recurrence of literary motifs (blood in Macbeth, for instance), where symbolic significance emerges not from local cues, but through repetition-with-variation across the whole work. We operationalize this setting as Computational Motif Discovery, a transductiv...
  </details>

- **2026-10-26** — Joonyong Park, Jerry Li — [When the Persona Contradicts the Line: Diagnosing Plan-to-Synthesis Failures in Chain-of-Thought TTS](http://arxiv.org/abs/2610.35008v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought TTS systems rely on language-model planners to translate persona and context into vocal delivery, but it is unclear where this intent is lost when the requested affect conflicts with lexical sentiment. We introduce a bilingual Japanese--English persona--line conflict benchmark in which each item pairs one line with congruent and conflicting personas and pre-declares the expected acoustic direction. We probe this direction in the planner-generated delivery phrase, the planner-wri...
  </details>

- **2026-10-26** — Yuhang Dong, Min Xia, Jinghong Li et al. — [Guarded Agent-in-the-Loop Residual Adaptation for Evolving Wind Power Regimes](http://arxiv.org/abs/2610.34968v1)
  <details><summary>📄 Abstract</summary>
  Wind power forecasting models are often deployed as fixed temporal backbones, but the errors they make can vary across meteorological regimes such as cold waves, heat-and-calm periods, productive typhoon, and destructive storms. We present a guarded Agent-in-the-loop residual adaptation framework that leaves the temporal backbone unchanged and adapts only a small set of scene-conditioned residual experts. An Agent layer interprets external scene information, identifies the current regime, select...
  </details>

- **2026-10-26** — Ayumi Igarashi, Yeeseok Oh — [Fair Division of Lotteries](http://arxiv.org/abs/2610.34906v1)
  <details><summary>📄 Abstract</summary>
  We study fair division of uncertain items, where the utility of each item is a random variable whose realization is observed only after the allocation is determined. This uncertainty creates a distinction between ex-ante fairness, evaluated before utilities are realized, and ex-post fairness, evaluated after realization. We examine to what extent these two notions are compatible. We first identify conditions under which ex-ante envy-free allocations maximize ex-post envy-freeness probability. Th...
  </details>

- **2026-10-26** — Sukmoon Huh — [Elementary transformations of toric vector bundles](http://arxiv.org/abs/2610.34885v1)
  <details><summary>📄 Abstract</summary>
  We describe negative and positive elementary transformations of toric vector bundles in terms of Klyachko filtrations. We first determine the filtrations of the restriction of a toric vector bundle to an invariant prime divisor and then derive explicit formulas for the transformed bundle: only the filtration at the distinguished ray changes. As applications, we interpret adding and removing invariant boundary components of logarithmic tangent bundles as elementary transformations and recover the...
  </details>

- **2026-10-26** — Kehua Chen, Mingyi Chen — [LayoutMamba: Efficient Document Layout Analysis with Hybrid Mamba-Transformer Networks](http://arxiv.org/abs/2610.34879v1)
  <details><summary>📄 Abstract</summary>
  Document layout analysis (DLA) faces a long-standing dilemma: existing methods either capture rich local details at prohibitive computational cost (e.g., Transformer-based approaches with quadratic complexity) or achieve efficient global modeling but sacrifice fine-grained structural awareness (e.g., state-space models). This trade-off hinders deployment in resource-constrained scenarios. We present LayoutMamba, a hybrid framework that synergistically combines sparse-attention Transformers for l...
  </details>

- **2026-10-26** — Bang Xiao, Baosheng Jin, Jinhan Niu et al. — [ECHOES: An Adaptive LLM-Powered AR Glasses Docent for Evidence-Grounded Urban Heritage Interpretation](http://arxiv.org/abs/2610.34865v1)
  <details><summary>📄 Abstract</summary>
  Urban heritage tours are often delivered through fixed scripts, leaving limited room for visitors' situated questions, language preferences, or requests for evidence. We present ECHOES, an adaptive LLM-powered AR glasses docent for evidence-grounded interpretation of historical buildings. Specifically, the agent adapts along three dimensions: it modifies response structure according to the type of visitor question (identification, architectural detail, evidence-seeking, or route inquiry); it acc...
  </details>

- **2026-10-26** — Chenyang Fan, Robert D. Sanders, Elie Matar et al. — [Interpretable Brain Age Prediction Using White Matter Fiber Orientation Distributions with Rotation-Equivariant Deep Learning](http://arxiv.org/abs/2610.34825v1)
  <details><summary>📄 Abstract</summary>
  Diffusion MRI (dMRI) provides information about white matter microstructure that can support brain age prediction. However, many existing prediction models use diffusion tensor imaging (DTI) scalar metrics that omit orientation information. Deep learning is increasingly used for brain age prediction, but conventional CNNs do not explicitly respect the geometric structure of orientation-dependent features. We present an interpretable brain age prediction framework that combines white matter fiber...
  </details>

- **2026-10-26** — Yuexi Pan, Yongchao Chen — [The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](http://arxiv.org/abs/2610.34767v1)
  <details><summary>📄 Abstract</summary>
  Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history? Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use. The same reported test result can support confirmation when the outcome and stopping rule were fixed in advance, yet only exploration when the outcome was selected from twenty inspected results. We call this scientific use validity: whether remembered evidenc...
  </details>

- **2026-10-26** — Tianyu Zhan, Gui Ling, Ran Tao et al. — [SLIDE: Search-to-List Item Distillation for Single-Rollout Generative Retrieval](http://arxiv.org/abs/2610.34764v1)
  <details><summary>📄 Abstract</summary>
  Generative retrieval (GR) typically relies on item-level beam search to retrieve candidates, leaving cross-item dependencies unmodeled and limiting direct optimization of list-level objectives. A natural alternative is to generate the entire list within a single autoregressive trajectory. However, greedy decoding with directly trained list-wise models substantially underperforms beam search. We identify two contributing factors: the broader search space explored by beam search and the positional...
  </details>

- **2026-10-26** — Fei Zuo, Yizhou Huang, Kezhi Wang — [Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching](http://arxiv.org/abs/2610.34756v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) has emerged as the dominant paradigm for parameter-efficient fine-tuning of large language models. Standard all-layer LoRA applies adaptation throughout the transformer, despite heterogeneous contributions from its components. In this work, we conduct a systematic mechanistic interpretability analysis to understand how LoRA affects model internals. We observe that LoRA's adaptation effect is highly non-uniform, with significant component-wise and layer-wise sparsity. M...
  </details>

- **2026-10-26** — Huaiyu Jia, Shuo Sun — [Beyond Profit Rankings: Identifying, Understanding, and Evaluating Smart Money in Prediction Markets](http://arxiv.org/abs/2610.34754v1)
  <details><summary>📄 Abstract</summary>
  Prediction markets have emerged as an important mechanism for aggregating information and trading beliefs about future events. The transparency of on-chain transactions has enabled investors to identify historically profitable wallets, commonly referred to as smart money, and replicate their trading activities through copy trading. However, despite the growing popularity of smart-money tracking, systematic research on these wallets' trading behavior, profitability persistence, and the economic f...
  </details>

- **2026-10-26** — Zhen Bi, Zhizhi Peng, Yan Wang et al. — [Harness-Model Collaboration for Long-Horizon Continual Learning](http://arxiv.org/abs/2610.34724v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute related multi-step workflows. We propose HaMo, a Harness-Model collaborative framework that combines fast non-parametric experience accumulation with slow parametric adaptation. HaMo distills trajectories into strategy-...
  </details>

- **2026-10-26** — Jingjie Ning, Xueqi Li, Yibo Kong — [SearchHorizonBench: A Benchmark for Search Value in AI Agents](http://arxiv.org/abs/2610.34714v1)
  <details><summary>📄 Abstract</summary>
  AI agents must decide when another search is worth its cost. Answer-success probabilities capture question difficulty, while this decision requires estimating the additional benefit of search. We introduce SearchHorizonBench, a benchmark for learning and evaluating search value from execution experience. Paired continuations and repeated executions separate expected search gain from generation noise and connect prediction quality to decision utility. The resource contains 45,632 executions acros...
  </details>

- **2026-10-26** — Xinyu Zhang, Weiwei Sun — [Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents](http://arxiv.org/abs/2610.34673v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents that serve users across many sessions must choose, for every request, the few stored memories that enter a limited context window. This choice largely decides whether the agent answers correctly, and it runs on every request at Web scale. This selection faces three challenges: a large and growing store, a per-request cost budget, and multi-session questions that need all of their evidence. Many memory systems build notes or graphs with hundreds to thousands of L...
  </details>

- **2026-10-26** — Paola Rizzo, Hector Munoz-Avila, David W. Aha — [Hierarchical Task Network planning in the Goal Lifecycle](http://arxiv.org/abs/2610.34668v1)
  <details><summary>📄 Abstract</summary>
  Goal reasoning (GR) is the process by which intelligent agents continually reason about the goals they are pursuing, which may lead to goal change, for instance when opportunities arise, or when events cause discrepancies among expected and actual outcomes of actions planned to achieve goals. In this paper we investigate whether Hierarchical Task Network (HTN) planning can provide a uniform implementation of the Goal Lifecycle, a flexible process model for goal reasoning in dynamic environments....
  </details>

- **2026-10-25** — Yalun Wu, Qiwei Ma, Bingbing Xu et al. — [EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems](http://arxiv.org/abs/2610.34450v1)
  <details><summary>📄 Abstract</summary>
  Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative, mixed-motive, and adversarial settings. However, existing approaches often develop adaptation mechanisms for particular interaction settings. This raises a central question: how can decentralized MAS support test-time ...
  </details>

- **2026-10-25** — Brianne Lee — [Does the Outfit Change the Price? Context Halo in Vision-Language Model Valuation of an Identical Low-Cost Necklace](http://arxiv.org/abs/2610.34591v1)
  <details><summary>📄 Abstract</summary>
  A chunky gold-tone chain necklace bought online for 2.43 USD was photographed four ways: worn with formal attire against a wood-panelled wall, worn at a party, worn with casual clothing in a recycling yard, and laid flat with no person present. We asked six frontier language models to estimate its price in 1,164 independent and sequential API sessions (4,604 logged rows) and compared estimates across settings. Among the four models that answered image prompts, the same necklace was priced 1.9 to...
  </details>

- **2026-10-25** — Shiyan Zheng, Ming Li, Lei Han et al. — [PhysCreator: Creating Physically-Attributed 3D Assets at Will](http://arxiv.org/abs/2610.34473v1)
  <details><summary>📄 Abstract</summary>
  Significant advancements in 3D asset creation have enabled high-fidelity 3D generation from images. However, most existing representations remain inherently static, lacking the ability to model physically plausible behaviors under dynamic interactions. We present \textbf{PhysCreator}, a unified framework that directly generates simulation-ready 3D representations with spatially varying physical properties from images. Unlike prior approaches that treat physical attributes as simple post-hoc pred...
  </details>

- **2026-10-25** — Leandro Parada, Kevin Yu, Panagiotis Angeloudis — [IntNet: A Communication-Driven Multi-Agent Reinforcement Learning Framework for Cooperative Autonomous Driving](http://arxiv.org/abs/2610.34466v1)
  <details><summary>📄 Abstract</summary>
  Achieving safety in autonomous driving through Multi-Agent Reinforcement Learning (MARL) is a critical yet challenging task due to non-stationarity, partial observability, and the need for effective coordination among agents. Although earlier cooperative MARL methods have aimed to improve coordination by sharing encoded state observations, we find these strategies are insufficient in safety-critical scenarios. To address this gap, we present IntNet, a novel MARL framework that enhances safety by...
  </details>

- **2026-10-25** — Meiyun Cao, Federico Mastroleo, Shuoyang Wei et al. — [Retrospective Comparison of Radiation Oncology Patient Message Responses Generated by Epic and Institutionally Managed LLMs](http://arxiv.org/abs/2610.34464v1)
  <details><summary>📄 Abstract</summary>
  We retrospectively compared Epic-generated draft replies with institutionally managed hybrid GPT-4.1 and Gemini 2.5 Pro responses to 51 selected single-turn radiation oncology messages. Six clinicians, blinded to response source, rated overall quality on a five-point scale and perceived editing effort on a four-point scale. Mixed-effects models accounted for repeated ratings by message and clinician. Adjusted overall-quality means were 2.95 for Epic, 4.27 for hybrid GPT-4.1, and 4.39 for hybrid ...
  </details>

- **2026-10-25** — Mallesh Madapathi — [Outcome-Aware Agents: When Does Causal Structure Help a Forward Model Foresee the Consequences of Actions?](http://arxiv.org/abs/2610.34385v1)
  <details><summary>📄 Abstract</summary>
  Agents that act on real systems should predict what their actions will cause before acting. We study when causal structure helps a learned forward model do this, using a planner that rejects candidate actions whose simulated multi-step outcome is unsafe, in synthetic structural causal models where the true consequences are known. We compare the Action-Conditioned Latent Structural Causal Model (AC-LSCM: per-factor mechanisms over a learned sparse graph, actions as do-interventions) with three un...
  </details>

- **2026-10-25** — Hatim Chergui, Carolina Fernández-Martínez, Mustapha Benjillali et al. — [6G Reasoning Agent Societies: Composition, Scaling, and Consistency-Time Laws](http://arxiv.org/abs/2610.34357v1)
  <details><summary>📄 Abstract</summary>
  Emerging 6G control planes would compose Large Language Model (LLM) agents that exchange interpreted conclusions, so hallucinations can propagate even over error-free transport. Recent architectures audit each message locally against the sender's observation mask, but isolated audits miss collective behavior. Modeling the agent society as a cellular sheaf, we establish three laws valid on arbitrary topologies. First, the \emph{composition law}: network-wide divergence exceeds the sum of per-agen...
  </details>

- **2026-10-25** — Mohamed Hamdy, Iheb Zouari, Fatmaelzahraa Ahmed et al. — [MIS-VQA: An Annotation-Driven Surgical Vision-Language Dataset for Complex Surgical Understanding](http://arxiv.org/abs/2610.34210v1)
  <details><summary>📄 Abstract</summary>
  Modern surgical AI increasingly requires multimodal understanding rather than isolated perception, yet existing datasets remain largely limited to single-task supervision such as recognition or templated question answering. Current medical VQA resources often rely on synthetic templates, lack natural descriptive supervision, or provide sparse annotations that hinder reasoning about spatial relations and procedural context. We introduce MIS-VQA, a surgical vision-language dataset generated throug...
  </details>

- **2026-10-25** — Junjie Yao, Xiongzheng Guan, Jia Feng et al. — [SpeC2Rust: Specification-Driven Repository-Level C-to-Rust Translation](http://arxiv.org/abs/2610.34141v1)
  <details><summary>📄 Abstract</summary>
  Legacy C codebases remain central to system software and performance-critical infrastructure, but their weak memory safety imposes security and maintenance risks. Recent C-to-Rust translation systems, including LLM-based translators, make automated migration increasingly feasible, yet they still struggle to recover repository-level intent, avoid raw pointers and unsafe constructs, maintain cross-file interfaces, and repair compilation and validation failures efficiently. We propose SpeC2Rust, a ...
  </details>

- **2026-10-25** — Daoxuan Liu, Jiayi Liao, Jiancan Wu et al. — [Decision-Native Recommendation with Large Language Models](http://arxiv.org/abs/2610.34124v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) bring world knowledge to user preference modeling in sequential recommendation, but generation-based recommenders express next-item predictions indirectly as text. Generated outputs may fail to identify a unique candidate item, depend on candidate presentation order in the prompt, and lack explicit confidence in the recommendation. Recent studies explore Jev, a model for fast option selection with explicit confidence. Inspired by Jev, we introduce decision-native rec...
  </details>

- **2026-10-25** — Changqing Zhou, Yueru Luo, Han Zhang et al. — [LegoOcc++: Towards Consistent Open-Vocabulary 3D Occupancy Prediction](http://arxiv.org/abs/2610.34093v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D occupancy prediction is important for embodied agents operating in complex environments whose semantic categories extend beyond fixed taxonomies. While recent studies have explored open-vocabulary occupancy in outdoor driving scenarios, indoor environments remain challenging due to dense occlusions, complex geometry, and fine-grained long-tailed semantics. To reduce the need for expensive voxel-level semantic annotations, we study a geometry-only supervision setting requiring ...
  </details>

- **2026-10-25** — Saswati Bhattacharjee, Anirban Sinha, Mukulika Ghosh et al. — [Extended LASMP: Language Aided Subset Sampling Based Motion Planner for Drone Navigation](http://arxiv.org/abs/2610.34054v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a command-aligned sampling distribution that incorporates navigation commands directly into the exploration process to improve the efficiency of sampling-based motion planning for quadcopters in three-dimensional environments. Inspired by the Language-Aided Subset Sampling Motion Planner, this paper extends command-aware subset sampling to aerial systems. Subset sampling is generalized to command-aligned regions, enabling structured 3D exploration while preserving probabilist...
  </details>

- **2026-10-25** — Viswonathan Manoranjan, Andrea Mock, Myra Cheng et al. — [The Patient Is Always Right? Evaluating Sycophancy in Medical Diagnosis with Graded Patient Beliefs](http://arxiv.org/abs/2610.34013v1)
  <details><summary>📄 Abstract</summary>
  More people are seeking out general-purpose AI models for medical advice, including diagnosis. Yet, AI models are susceptible to sycophancy, like validating users' beliefs even when they are untrue, which could lead to false positive diagnoses. Here, we evaluate how nine AI models change their diagnostic decision when a patient presents a belief that they have a specific (but incorrect) medical condition. We vary how close the user belief is to the clinical evidence presented. Models sycophantic...
  </details>

- **2026-10-25** — Meng Geng, Dachun Yang, Wen Yuan et al. — [Sharp Quantitative Weighted Estimates for Lifted Maximal Operators with Applications](http://arxiv.org/abs/2610.33998v1)
  <details><summary>📄 Abstract</summary>
  In this article, we establish sharp quantitative weighted estimates for the lifted Hardy--Littlewood (resp Sobolev sharp) maximal operators $\{\mathcal M_θ\}_{θ\in(0,\infty)}$ (resp $\{\mathcal M_θ^\sharp\}_{θ\in(0,\infty)}$). Specifically, for $p\in(1,\infty)$, $γ\in\mathbb R\setminus\{0\}$, $\upsilon\in A_p$, and $f\in L^p_\upsilon$, we prove that \begin{align*} \sup_{θ,λ\in(0,\infty)}λ^p \underset{\mathcal M_θ(f)(x,t)>λt^γ} {\int_{\mathbb R^n}\int_0^\infty} t^{γp-1}\,dt\,\upsilon(x)\,dx \less...
  </details>

- **2026-10-25** — Akwasi Asare — [Accuracy Is Not Enough: An Efficiency- and Statistics-Aware Benchmark of ResNet50 and Vision Transformer for Explainable Multi-Class Gastrointestinal Diseases Classification](http://arxiv.org/abs/2610.33965v1)
  <details><summary>📄 Abstract</summary>
  Automated classification of gastrointestinal (GI) findings in endoscopic images could support early diagnosis, but architectures are often chosen on accuracy alone. We present a controlled, reproducible benchmark of ResNet50 and ViT-B/16 for eight-class GI classification on the public Kvasir dataset (4,000 images), using a stratified split (400 test images) and stratified group 5-fold cross-validation over all images. In cross-validation, ResNet50 and ViT-B/16 reached 92.12% and 91.70% accuracy,...
  </details>

- **2026-10-25** — Nuo Chen, Shizeng Zhang, Yujie Yang et al. — [ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation](http://arxiv.org/abs/2610.34370v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose ThinkLocoManip, an agentic harness for legged loco-manipulation designed to tackle complex, long-horizon tasks in large-scale environments. Existing approaches typically follow either direct action generation or a plan-then-act paradigm, both of which can struggle with the generalization and error-recovery capabilities required for extended task execution. In contrast, ThinkLocoManip adopts an interleaved reasoning-and-acting paradigm, allowing the agent to continuously...
  </details>

- **2026-10-25** — Ying Xiao, Xinjian Wu, Lukas Twist et al. — [Honesty Testing of LLMs and AI Agents: A Vision for Software Engineering](http://arxiv.org/abs/2610.34239v1)
  <details><summary>📄 Abstract</summary>
  Human oversight of large language models (LLMs) and artificial intelligence (AI) agents increasingly depends on their reports. Claims that conflict with a system's own judgments can conceal failures, prevent timely intervention, and contribute to severe harm. Greater autonomy makes faithful reporting increasingly important for maintaining human control. In this vision paper, we propose honesty testing of LLMs and AI agents as a new research area in software engineering. Building on existing hone...
  </details>

- **2026-10-25** — Tzeh Yuan Neoh, Nicholas Teh — [Online Fair Division with Frequency Predictions](http://arxiv.org/abs/2610.34625v1)
  <details><summary>📄 Abstract</summary>
  We study online fair division of indivisible goods among $n$ agents with frequency predictions: before any good arrives, the algorithm learns the multiset of each agent's values for the goods, but neither the arrival order nor which values of different agents belong to the same good. Neoh et al. (ICML 2026) showed that such predictions allow every share-based guarantee that is achievable offline, and left open whether a positive approximation of envy-freeness up to one good (EF1) is possible. We...
  </details>

- **2026-10-25** — Fatma Ahmed Mansour, Rahatara Ferdousi, Manar Fathy Elshenawy — [An Agentic AI Workflow for Liver Lesion Segmentation and Structured Radiology Reporting](http://arxiv.org/abs/2610.34599v1)
  <details><summary>📄 Abstract</summary>
  Despite advances in automated liver lesion segmentation, a gap remains between image-derived predictions and clinically interpretable radiology reports. Bridging this gap requires quantitative measurements that are both reproducible and traceable. We present an evidence-grounded agentic AI framework that connects liver and lesion segmentation with deterministic quantification and structured reporting. TotalSegmentator-based nnU-Net models delineate the liver, Couinaud segments, and lesions, whil...
  </details>

- **2026-10-25** — Po-Wei Chen, Shan Yu, Chunlin Li — [HIFI: A Highly Efficient Framework for Statistical Inference with Foundation Models](http://arxiv.org/abs/2610.34550v1)
  <details><summary>📄 Abstract</summary>
  Foundation models provide powerful representations for unstructured data, such as text and images, and parameter-efficient fine-tuning (PEFT) makes their adaptation to downstream tasks increasingly practical. For neural estimators that lack a tractable sampling distribution, resampling-based procedures offer a flexible route to statistical inference, but they often require hundreds of model fits, making them computationally prohibitive at foundation-model scale. We introduce HIFI, a two-stage fi...
  </details>

- **2026-10-25** — Yichuan Chen, Xin Wang — [The Price of Scale in Proactive Memory Recall](http://arxiv.org/abs/2610.34507v1)
  <details><summary>📄 Abstract</summary>
  A long-lived assistant that brings up memories without being asked must decide at every turn whether anything in its store is worth an interruption. We show that this decision is a multiple-testing problem whose difficulty grows with the store size $N$. On streaming replays of LongMemEval and LoCoMo, a similarity threshold tuned to 5% false alarms at $N=8$ reaches 87-100% at $N=2048$, across embedding models and for explicit and implicit cues; LLM judges show the same growth from a lower base. W...
  </details>

- **2026-10-25** — Alessandro Melchiorri — [Comment on "Test of the Gravitational Force Law on Cosmological Scales Using the Kinematic Sunyaev--Zeldovich Effect''](http://arxiv.org/abs/2610.34437v1)
  <details><summary>📄 Abstract</summary>
  Gallardo et al. [Phys. Rev. Lett. \textbf{136}, 151002 (2026)] constrain the index of the force law $g\propto r^{-n}$ with pairwise kinematic Sunyaev--Zeldovich measurements, $n=2.1\pm0.3$, and exclude the deep-MOND value $n=1$ at $3.3σ$. The exclusion does not follow from their calculation. Their templates for $n\neq2$ [their Eq.~(8)] raise the pair-averaged Newtonian acceleration to the power $n/2$, whereas the pair average of the pointwise law [their Eq.~(30) for deep MOND] is the average of ...
  </details>

- **2026-10-25** — Pasin Manurangsi — [Envy-Free Allocations for Random Non-Additive Valuations](http://arxiv.org/abs/2610.34434v1)
  <details><summary>📄 Abstract</summary>
  Benade et al. (EC 2024) introduced a semi-random model for non-additive fair division in which each agent starts with an arbitrary base valuation over bundles of items and independently permutes the item names uniformly at random. While they proved that envy-free allocations exist with high probability as the number of items grows for $n = 2$ agents, they left open whether the same holds for $n > 2$ agents. We resolve this open question in the affirmative: for any fixed number of agents $n$ and ...
  </details>

- **2026-10-25** — Ivan Iorsh, Aleksandr Kapitonov, Ivan Filianin et al. — [A Domain-Aware Pipeline for Structured Extraction and Retrieval-Augmented Question Answering over arXiv Superconductivity Literature](http://arxiv.org/abs/2610.34391v1)
  <details><summary>📄 Abstract</summary>
  Scientific literature in materials physics is growing faster than researchers can manually inspect it, yet most retrieval tools rely on keyword matching or generic question answering that ignores domain-specific structure in PDF files. This paper presents an end-to-end pipeline that transforms arXiv superconductivity publications into a searchable corpus with structured metadata and retrieval-augmented question answering. The system combines thematic corpus construction, domain-aware extraction ...
  </details>

- **2026-10-25** — Sébastien Gracia — [Officially corrected errors persist in AI training data: preregistered measurements on EU law, Internet standards and retracted science](http://arxiv.org/abs/2610.34379v1)
  <details><summary>📄 Abstract</summary>
  Official texts are corrected after publication: EU corrigenda, verified RFC errata, retractions. We measured whether these corrections are present in four public datasets used to train language models, and what models answer about the corrected passages. In EurlexResources, a legal training dataset, 1,989 of 2,082 testable single-language corrections to EU acts (95.5%, 94.6-96.3) remain in their erroneous form; in a random sample of 100, 46 change the meaning, a figure, a cross-reference, the co...
  </details>

- **2026-10-25** — Zhenyao Sun — [A marked scheme representation for Voronoi volumes in the Brownian map](http://arxiv.org/abs/2610.34255v1)
  <details><summary>📄 Abstract</summary>
  For any fixed number $k\ge3$ of independent volume-sampled sites in the unit-area Brownian map, we represent the negative-power transform of their ordinary Voronoi volumes as a finite sum of marked planar scheme integrals. These integrals arise from the critical asymptotics of generating functions for face-constrained labelled planar maps. To connect them to Voronoi volumes, we use Miermont's zero-delay correspondence to interpret the labelled maps as quadrangulations with distinguished sites an...
  </details>

- **2026-10-25** — Vitor Cerqueira, Ricardo Inácio, Carlos Soares — [MetaARIMA: Configuration-Level Transfer Learning for ARIMA Models](http://arxiv.org/abs/2610.34171v1)
  <details><summary>📄 Abstract</summary>
  Time Series Foundation Models have demonstrated that pretraining on diverse datasets enables effective transfer to new forecasting tasks. Classical methods like ARIMA, however, remain configured and trained independently for each series, discarding knowledge from previous experiments. Consequently, selecting and training an ARIMA configuration remains challenging and often relies on heuristic approaches based on in-sample goodnessof-fit measures. We propose MetaARIMA, a pretrained configuration ...
  </details>

- **2026-10-25** — Tianchen Guo, Tengyue Zhang, Chen Liu et al. — [Humans in Space: Can MLLMs Construct Human-Centric Spatial Understanding via Active Exocentric Exploration?](http://arxiv.org/abs/2610.34149v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) excel at zero-shot reasoning, their spatial capabilities are primarily evaluated through static, passive observation. In complex, human-centric scenes, occlusion often hides crucial geometric evidence, and passive benchmarks force models to guess rather than recognize their own visual uncertainty. To bridge this gap, we introduce SATE-Bench, a novel interactive benchmark comprising 316 real-world scenes and 2,525 multi-turn QA pairs to evaluate visu...
  </details>

- **2026-10-25** — Zhaoyang Li, Yuhao Chen, Qianqian Yang et al. — [Environment-Adaptive Dynamic KV Cache for Multi-Path Parameter Prediction](http://arxiv.org/abs/2610.34135v1)
  <details><summary>📄 Abstract</summary>
  Multipath parameter prediction provides a structured and physically interpretable representation of wireless propagation for environment-aware communication systems. However, existing Transformer-based methods repeatedly encode the same environment when predicting multiple BS--UE links, resulting in redundant computation. To address this issue, we propose an environment-conditioned dynamic KV caching framework for multipath parameter prediction. Specifically, we decouple environment-dependent co...
  </details>

- **2026-10-25** — Jean Laurens — [New developments in the geometry and topology of 3D head-direction coding](http://arxiv.org/abs/2610.34106v1)
  <details><summary>📄 Abstract</summary>
  The head-direction (HD) system is a neuronal compass that represents head orientation in 3D. Its encoding of 3D head orientation can be decomposed into a multiplexed representation of 2D head tilt relative to gravity and 1D head orientation in the horizontal plane (azimuth). Defining azimuth during 3D motion is not trivial, and recent studies have indicated that the HD system implements a so-called dual-axis/tilted-azimuth (DA/TA) rule, a representation that is well supported experimentally but ...
  </details>

- **2026-10-25** — Zhifeng Yang, Wei Luo, Yongjian Chen et al. — [From Document Layout to Causal Topology: An End-to-End Architecture for Temporal Causal Reasoning](http://arxiv.org/abs/2610.34094v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) generally lack deep causal reasoning capabilities in temporal reasoning. Inspired by document layout reordering, this paper proposes a paradigm shift from discrete narratives to causal topologies. It constructs two architectures: a training-free neuro-symbolic framework, temporal causal reasoning agent (TCR-Agent), which achieves interpretable causal deduction and counterfactual truncation through external causal graph instantiation and a symbolic intervention engine...
  </details>

- **2026-10-25** — Michael Foster, Barbara McGillivray, Gard B. Jenset et al. — [The LALA Benchmark: Evaluating Literary and Linguistic Analysis in LLMs](http://arxiv.org/abs/2610.34080v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Literature and Linguistics Analysis Benchmark (LALA), comprising 236 open-ended questions written by experts in linguistics and literary studies, together with expert-provided ideal answers. By comparing models within families and at similar training scales using human and LLM judges, LALA identifies differences in linguistic competence associated with post-training, offering a framework for evaluating future models and guiding targeted improvements. We administered questions to...
  </details>

- **2026-10-25** — Tsung-Lung Yang — [Cut a Wall, See a Wall: Identity Substitution in Occluded Point-Cloud Perception for Construction Robots](http://arxiv.org/abs/2610.34040v1)
  <details><summary>📄 Abstract</summary>
  Construction robots must label building elements they can only partly see. We show that when occlusion at test time removes whole regions of a scene, rather than parts of an object as in training, point-cloud segmentation networks do not simply miss the hidden elements: they relabel them, and the errors collapse onto a single sink class. With fixed synthetic layouts the column absorbs up to 70% of all test points; with randomized layouts the sink moves to the stair, predicted at 4.5-5.4x its tru...
  </details>

- **2026-10-25** — Chong Zhao, Ruyi Yang, Changming Liu et al. — [When Does GEPA Merge Help? A Mechanism-Level Diagnostic](http://arxiv.org/abs/2610.34027v1)
  <details><summary>📄 Abstract</summary>
  GEPA is among the strongest reflective prompt optimizers for language-model programs, but its system-aware merge operator is unstable across models: merge improves gpt-4.1-mini on average while degrading Qwen3-8B, an asymmetry noted but left unexplained by the GEPA paper. We investigate this instability across five datasets and two models. Our nine-configuration sweep over merge timing and merge operator shows that merge can improve both models when configured appropriately. This suggests that m...
  </details>

- **2026-10-25** — Bangti Jin, Longjun Wu — [The Symmetry of Differential Neural Tangent Kernel under the Orthogonal Group](http://arxiv.org/abs/2610.34023v1)
  <details><summary>📄 Abstract</summary>
  The differential neural tangent kernel (DNTK) is a tool for analyzing the training dynamics of overparameterized physics informed neural networks. In this work, we investigate the symmetry of the infinite DNTK under an orthogonal group, for two layer and deep neural networks separately, based on the explicit expression of the DNTK and recursive formula, respectively. The results are for all activations with or without a bias term, and shed insight into the structure of the infinite width DNTK. T...
  </details>

- **2026-10-25** — Garrick Chan, Yun-Hsin Kuo, Sam Yu-Te Lee et al. — [Detecting and Understanding Ambiguity in Visualizations with Role-Playing Vision Language Model Interpretations](http://arxiv.org/abs/2610.33997v1)
  <details><summary>📄 Abstract</summary>
  Communicative visualizations can support multiple chart-grounded takeaways, including divergent or conflicting ones; we refer to this variation as interpretive ambiguity. Such ambiguity can undermine a visualization's communicative goal when the supported takeaways diverge from its intended message. Evaluating visualizations with target audiences can surface this variation, but such evaluations can be costly and difficult to scale. In this work, we explore persona-conditioned Vision Language Mod...
  </details>

- **2026-10-24** — Leiyue Chen, Meng Wei, Xuefeng Hu et al. — [Intervention-Certified Amplification: A Validity Gate for $σ$-Weighted Post-Training](http://arxiv.org/abs/2610.33882v1)
  <details><summary>📄 Abstract</summary>
  Hybrid post-training often mixes supervised fine-tuning (SFT) and reinforcement learning (RL), using training-side signals to set each sample's balance. Such signals characterize the anchor data and policy, but not whether the emphasized behavior helps in the target task and evaluation setting. This mismatch can reactivate and amplify pretrained behavior even after its literal form is removed from supervision. We demonstrate this with DIAA (Dual-Implicit Adversarial Amplification), a per-sample ...
  </details>

- **2026-10-24** — Wenjing Lin, Madelon Hulsebos — [Bridging Search Intent and Tabular Data in Dataset Search](http://arxiv.org/abs/2610.33936v1)
  <details><summary>📄 Abstract</summary>
  Dataset search remains a bottleneck in data analysis workflows, as existing systems largely rely on keyword matching or shallow retrieval that fail to capture user intent. To facilitate intent-driven search, we present two retrieval components to equip multi-faceted dataset search interfaces through natural language. First, we propose Hypothetical Schema Embeddings (HySE) that uses a language model to generate task-aligned hypothetical table schemas which are used for embedding-based retrieval, ...
  </details>

- **2026-10-24** — Basheer Al-Tawil, Magnus Jung, Ayoub Al-Hamadi — [Real-Time Human Trajectory Prediction from RGB-D for Mobile Robots Using Bi-Mamba](http://arxiv.org/abs/2610.33916v1)
  <details><summary>📄 Abstract</summary>
  Predicting the short-term future trajectory of a person from RGB-D cameras is a key capability for mobile robots navigating in dynamic and human populated environment. The key challenge to deploying learned predictors on real robots is the train-deploy pipeline gap. Training data are often prepared with an idealized, smoothed ground truth, whereas at inference, the model is fed noisy estimates from pose detectors and depth sensors. The model is therefore evaluated on an input distribution it nev...
  </details>

- **2026-10-24** — Md Ahadul Haque Suvo, Rifat Bin Reza, Saifur Rahman Sabuj — [Residual-Calibrated Multimodal Spatiotemporal Learning for Future Beam Prediction](http://arxiv.org/abs/2610.33892v1)
  <details><summary>📄 Abstract</summary>
  We propose a residual calibrated multimodal spatiotemporal framework for future beam prediction on DeepSense 6G Scenario 23. The framework integrates visual observations, location features, and historical beam labels to predict the beam label of the next dataset record. A pretrained Swin-Tiny encoder extracts features from four consecutive RGB frames. Bidirectional cross-attention integrates visual and two dimensional Unit 1 location representations, while a temporal Transformer incorporates his...
  </details>

- **2026-10-24** — Florian Kurpicz, Maximilian Paris — [Engineering Lightweight Burrows-Wheeler Transform Construction on the GPU via Prefix-Free Parsing](http://arxiv.org/abs/2610.33889v1)
  <details><summary>📄 Abstract</summary>
  The Burrows-Wheeler transform (BWT) is the core of many compressed full-text indexes and most read aligners. The fastest BWT constructions on GPUs need about $20$ bytes of device memory per character, which severely limits the texts that can be processed there. For example, on our GPU with 24 GB device memory, this is only about 1200 MiB. Prefix-free parsing (PFP) can be used to reduce the memory requirements of BWT construction algorithms in main memory. But, it uses hash tables and inverted li...
  </details>

- **2026-10-24** — Matilde Elene Hansen, Ross Deans Kristensen-McLachlan — [Gender Associations in LLM-Mediated ADHD Self-Diagnosis](http://arxiv.org/abs/2610.33697v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for medical self-diagnosis. However, the way demographic cues shape outputs in these interactions remains poorly understood. This is particularly consequential for diagnoses like ADHD, where persistent gender disparities are not fully aligned with the clinical evidence. We adapt the Context Association Test (CAT) to evaluate whether GPT-4o responds to gendered ADHD associations in a zero-shot, self-diagnostic setting. We show that explicit cuein...
  </details>

- **2026-10-24** — Gangyi Tian, Wen Ji, Alireza Furutanpey et al. — [Semantic-Guided Frequency Modulation for Learned Image Compression](http://arxiv.org/abs/2610.33616v1)
  <details><summary>📄 Abstract</summary>
  High-frequency attenuation can reduce the rate of learned image codecs but also remove object boundaries and fine detail. We propose Semantic-Guided Adaptive Latent-Frequency Modulation (SG-AFM), which uses a semantic structural prior to guide attenuation of encoder latents. SG-AFM applies a Haar wavelet transform and combines a fixed semantic-frequency multiplier with a bounded learned correction to modulate high-frequency subbands. The semantic prior is computed only at the encoder. No semanti...
  </details>

- **2026-10-24** — Sagnik Anupam, Utkarsh Lal, Aneesh Edara et al. — [RoboReason: Boosting Robotics-Relevant VLM Reasoning Through Scalable Data Generation](http://arxiv.org/abs/2610.33778v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated impressive performance when integrated into robot manipulation pipelines, but real-world evaluation of VLM capabilities on downstream robotics tasks is both difficult and expensive to scale. We propose that spatial and temporal ordering tasks using images from stereo and wrist cameras attached to real-world robots are particularly well-suited for evaluating visual reasoning capabilities, as they assess skills directly applicable to robots. We evalu...
  </details>

- **2026-10-24** — Xiaodi Huang, Zilin Wang, Jinpeng Liu et al. — [POD-RoPE: Rotary Position Encoding over Physical Observation Distributions for Embodied AI](http://arxiv.org/abs/2610.33745v1)
  <details><summary>📄 Abstract</summary>
  Embodied perception requires positional representations that capture both physical geometry and the spatial and temporal extent of observations. We introduce POD-RoPE (Physical Observation Distribution RoPE), which represents token observation footprints as distributions over camera centers, viewing directions, and sampling times. Under independent sampling, expected rotations encode relative relationships between distributions; when each distribution collapses to a single address, the construct...
  </details>

- **2026-10-24** — Lu Feng — [Human-Aware Agentic Driving: Rethinking Driver State, Trust, and Intervention](http://arxiv.org/abs/2610.33915v1)
  <details><summary>📄 Abstract</summary>
  Agentic driving brings goal-directed reasoning, memory, tools, and adaptive interaction into automated vehicles. A vehicle can clarify a request, explain a maneuver, or prepare a driver to take control, then adapt its next action to the response. These capabilities make the vehicle an active participant in shaping the human behavior it observes. We examine how agentic interaction affects driver-state inference, trust and reliance, and human intervention in conditional automation. Established fin...
  </details>

- **2026-10-24** — Maxime Dassen, Alexander Martin, Andrew Yates et al. — [Grounding on Request: Learning Modality Control in Vision-Language Models](http://arxiv.org/abs/2610.33841v1)
  <details><summary>📄 Abstract</summary>
  When an image and its caption disagree, can a user reliably control which one a vision-language model (VLM) follows? Accuracy alone cannot answer this question, since a model might give the correct answer from parametric knowledge without following the requested evidence. We therefore evaluate modality grounding control through conflict-preserving counterfactual interventions. Specifically, Flip measures whether an initially correct answer follows an edit to the requested modality, while Stay me...
  </details>

- **2026-10-24** — Yuxiang Wang, Baojian Zhou, Qifang Zhao et al. — [ProtAgent: Post-Training Compact Protein Tool Agents with Interaction-Level Credit Assignment](http://arxiv.org/abs/2610.33746v1)
  <details><summary>📄 Abstract</summary>
  Protein annotation agents must choose suitable bioinformatics tools, interpret their outputs, and use the resulting evidence in the final answer. Most existing systems rely on frontier-scale models. We ask whether a compact model can instead learn this behavior through post-training with real tool interaction. We present ProtAgent, a two-stage pipeline that uses supervised fine-tuning (SFT) to learn the tool interface and standard on-policy REINFORCE to improve the interaction policy. Intermedia...
  </details>

- **2026-10-24** — Yanxing Huang, Bingzhang Yan, Zihan Tang et al. — [A Distribution-Matching Perspective on LLM Training Algorithms](http://arxiv.org/abs/2610.33740v1)
  <details><summary>📄 Abstract</summary>
  In this work, we propose a unified framework for training algorithms across different stages of modern large language model development, based on the perspective of distribution matching. We show that a broad class of language model training algorithms can be interpreted as minimizing a certain divergence between the current model and a target distribution, and that characterizing the properties of this target distribution provides substantial insight into the behavior of the corresponding train...
  </details>

- **2026-10-24** — Nguyen Dang Duy Tan, Vo Thanh Nguyen, Linh T. T. Tran et al. — [LENS: Likelihood Evaluation and Neighbor Smoothing for Attribute-Based Person Retrieval on Unseen Cameras](http://arxiv.org/abs/2610.33641v1)
  <details><summary>📄 Abstract</summary>
  Attribute-based person retrieval ranks surveillance images from a binary query of semantic attributes, but mean Average Attribute Degree of Match (mADM) drops on unseen cameras as predicted probabilities shift. Common pipelines rank gallery images by their L1 distance to the query, which penalizes a confident single-attribute mismatch no more than small uncertainties across many attributes, while post-hoc recalibration fitted on source validation data fails to transfer because the per-attribute ...
  </details>

- **2026-10-24** — Yi Liu — [When Generated Information Returns: Error Persistence in LLM-Mediated Information Ecosystems](http://arxiv.org/abs/2610.33617v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly produce online articles from material that later becomes input to other models. This circulation connects individual responses to the information available for subsequent generation. We study a consequential distinction: an article can avoid endorsing a false claim while preserving the concrete details that enable its reproduction. Our framework connects claim content, expressed stance, and downstream reuse to explain selective error persistence under a ...
  </details>

- **2026-10-23** — Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi et al. — [Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations](http://arxiv.org/abs/2610.32891v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to optimize code for performance. This practice often assumes that improvements in execution speed naturally translate into overall lower energy consumption. We challenge this assumption empirically by measuring whether performance-optimized code produced by LLM self-refinement pipelines is also energy-efficient relative to canonical human reference solutions, and whether the energy cost of the optimization process can be offset by subsequent ex...
  </details>

- **2026-10-23** — Zheng Jiang, Yiming Chen, Houde Qian et al. — [Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond](http://arxiv.org/abs/2610.32802v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation aligns teacher feedback with a student's current behavior, yet acquiring useful supervision for multi-turn agents requires identifying both where guidance is needed and whether the student can sustain the interaction afterward. We introduce Frontier-OPD, which addresses this problem through the student's learning frontier: decision situations that remain challenging but admit useful autonomous continuation after brief teacher guidance. To operationalize this frontier, Fron...
  </details>

- **2026-10-23** — Dario Bocchi, Matteo Negri, Flavio Nicoletti et al. — [Generalization properties of the token perceptron: the role of embedding and vocabulary](http://arxiv.org/abs/2610.32788v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained to predict tokens from a finite vocabulary, each represented by a vector in a $d$-dimensional embedding space. Therefore, token prediction is a classification problem whose classes have a geometry determined by the embedding. We study how this geometry affects learning in a minimal solvable model: a linear predictor that maps a sequence of $N$ embedded tokens to a $d$-dimensional output through one $d\times d$ matrix per position, trained in the teacher--student...
  </details>

- **2026-10-23** — Christian Zink, Maik Pfefferkorn, Eric Lenz et al. — [Cross-Scenario Controller Parameter Transformation from Real-World Driving Data through Flow Matching](http://arxiv.org/abs/2610.32719v1)
  <details><summary>📄 Abstract</summary>
  Advanced Driver Assistance Systems have become increasingly widespread, aiming to support drivers, reduce workload, and improve traffic safety. However, many systems are rarely used because their behavior feels unnatural and does not match individual driving behavior. The growing availability of large-scale, real-world human driving data enables more human-like and driver-individual assistance functions. This paper formulates the adaptation of Adaptive Cruise Control parameters as a driver-indiv...
  </details>

- **2026-10-23** — Abdelkader Dib, Milos Balac — [Agent-Based Transport Model Calibration via Online Stochastic Batch Optimization](http://arxiv.org/abs/2610.32698v1)
  <details><summary>📄 Abstract</summary>
  Calibrating agent-based models (ABMs) is computationally demanding, as traditional black-box optimization typically requires hundreds or thousands of independent simulation runs. To reduce this burden, we introduce an online calibration framework that estimates parameters within a single simulation run. The approach combines black-box optimization with stochastic batch optimization, a method widely applied in machine learning but not yet explored in ABM calibration. Using MATSim as a case study,...
  </details>

- **2026-10-23** — Debleena Das, Chandan Kumar Jha, Muhammad Hassan et al. — [Automated Multi-Line Bug Repair Using Model Checker Aided LLMs: A Case Study on RISC-V Processors](http://arxiv.org/abs/2610.32597v1)
  <details><summary>📄 Abstract</summary>
  Functional verification of Register-Transfer Level(RTL) designs has become a critical bottleneck in modern semiconductor development, often consuming the majority of project resources. Debugging, in particular, remains an especially time-consuming task, requiring careful analysis of simulation traces or counterexamples. Recent work has explored applying Large Language Models (LLMs) to RTL debug and repair with great promise. However, the existing approaches typically are for single-line bugs, op...
  </details>

- **2026-10-23** — Filippo Rinaldi, Aniello Panariello, Giacomo Salici et al. — [From Parameter Rebasin to Functional Transfer Across Heterogeneous Transformers](http://arxiv.org/abs/2610.32581v1)
  <details><summary>📄 Abstract</summary>
  Adapting pretrained Transformers to downstream tasks produces task-specific updates that are expensive to reproduce for every model variant. Reusing these updates across different depths and widths is challenging because their parameters have incompatible shapes and do not share a canonical coordinate system. We introduce Ariadne, a training-free method that transfers task-specific behavior across heterogeneous Transformers without resizing the source model or transporting its parameters. Rather...
  </details>

- **2026-10-23** — Hassan Hassanzadeh Aliabadi — [Lessons Outlive Their Failures: A Case Study of Rules for AI Coding Agents](http://arxiv.org/abs/2610.32578v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly work inside a harness: rule files such as AGENTS.md, on-demand skills, runtime hooks and automated checks. Most studies of harnesses look at a single point in time or at short benchmark runs. I report a six-week case study of my personal system of record, a plain-markdown repository that three AI agent tools edited daily under one shared rule set. I built a ledger of 118 agent failures, their fixes and whether they came back. I also tested the system's monthly LLM d...
  </details>

- **2026-10-23** — Amber Xie, Jiawei Fu, Xiaofeng Guo et al. — [DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](http://arxiv.org/abs/2610.32969v1)
  <details><summary>📄 Abstract</summary>
  Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargeted to the robot, and they do not directly provide robot actions. In this paper, we introduce DexPort, a portable data-collection interface for...
  </details>

- **2026-10-23** — Yi Qin, Marawan Elbatel, Shanshan Song et al. — [Multimodal Generative AI Assists Comprehensive Echocardiographic Interpretation](http://arxiv.org/abs/2610.32880v1)
  <details><summary>📄 Abstract</summary>
  Echocardiography is the cornerstone of cardiovascular diagnostics, yet its global utility is constrained by a critical shortage of experienced interpreters. Current artificial intelligence (AI) solutions remain limited, typically operating as opaque "black boxes" or focusing on narrow tasks that fail to capture the holistic, guideline-driven reasoning of a clinician. Here we introduce EchoChat, a generative multimodal vision-language model that performs comprehensive echocardiographic analysis t...
  </details>

- **2026-10-23** — Moritz Thoma, Maximilian Groezinger, Maximilian Forstenhäusler et al. — [Advancing SVD-based LLM Compression via Layer-Wise Error Model Search](http://arxiv.org/abs/2610.32878v1)
  <details><summary>📄 Abstract</summary>
  Low-rank SVD-based compression offers a powerful strategy to reduce the computational costs of LLMs. However, existing methods face two key limitations: (i) global rank allocation, where uncalibrated error proxies fail to capture complex error propagation, and (ii) decomposition quality, where Fisher-based estimators suffer from severe rank collapse. In this work, we address these limitations by introducing Layer-wise Error Modeling Search (LEMS) and KFAC-SVD. LEMS advances rank allocation by in...
  </details>

- **2026-10-23** — Yonghui Niu, Yuhao Ji, Chang Nie et al. — [Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding](http://arxiv.org/abs/2610.32784v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of video data has created an urgent need for efficient video understanding systems that can handle long and continuous visual inputs, posing significant challenges for Multimodal Large Language Models (MLLMs) due to severe memory bottlenecks. Moreover, existing compression methods often overlook the explosive accumulation of approximation errors. To address this issue, we propose Video-MemComp, a training-free and sensitivity-aware context management framework for memory-constra...
  </details>

- **2026-10-23** — Zaifei Yang, Weiyu Chen, Yaqing Wang et al. — [What Transfers Across Protein Pockets? Experience Reuse in Molecular Optimization for Agentic Structure-Based Drug Design](http://arxiv.org/abs/2610.32620v1)
  <details><summary>📄 Abstract</summary>
  LLM agents optimize a ligand in a protein pocket by editing it step by step and docking each edit. Recent agents first spend extra dockings probing the complex with controlled edits; guidance induced from these probes is reported to help more than the chemical knowledge the model already carries. The probes are then discarded with the instance that produced them, so the obvious next step is to keep them in an experience base, letting a new pocket inherit what earlier ones already paid for. Such ...
  </details>

- **2026-10-23** — Anthony Longo, Olya Kudina — [Political sense-making in "individual" human-technology-world relations: the case of LLM-generated autobiographies](http://arxiv.org/abs/2610.32594v1)
  <details><summary>📄 Abstract</summary>
  As AI systems increasingly mediate how people describe, recognize, and present themselves, their politics cannot be reduced to what remains hidden inside the "black box." This chapter argues that AI's political significance emerges within technologically, intersubjectively, and temporally mediated interpretive practices. Bringing Arendt's political philosophy into conversation with Gadamerian hermeneutics, the chapter develops a postphenomenological relational-temporal account of political sense...
  </details>

- **2026-10-23** — Dan Bachar, Ehud Shapiro — [GLP Networking API Specification](http://arxiv.org/abs/2610.32583v1)
  <details><summary>📄 Abstract</summary>
  Multiagent deterministic GLP (madGLP) runs Grassroots Logic Programs (GLP) as agents that communicate solely by asynchronous message passing, and assumes fair delivery: every message sent is eventually delivered. Each agent runs on a person's smartphone, named by the person's public key. A grassroots platform depends on no global resource but the network, so agents must reach one another over Bluetooth Low Energy, on a local network, and across the Internet from behind NAT, via rendezvous server...
  </details>

- **2026-10-23** — Jaume de Haro, Emilio Elizalde — [Cartographing Gravity: Operational Maps, the Conatus of Proper Time, and the Potentia of Matter](http://arxiv.org/abs/2610.32569v1)
  <details><summary>📄 Abstract</summary>
  Classical natural philosophy sought the natural law governing the motion of free bodies long before daring to construct the appropriate mathematical formalism. Following this longstanding methodological perspective, in the present work General Relativity is reconstructed from operational and dynamical principles, rather than taking spacetime geometry as its starting point. The \textit{conatus} of a massive free particle is identified with its natural tendency to follow a worldline of stationary ...
  </details>

- **2026-10-22** — Jeffrey Olmo, David Zhang, Tyler Tracy — [Simulated Control Evals](http://arxiv.org/abs/2610.31593v1)
  <details><summary>📄 Abstract</summary>
  Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built control settings and extrapolate their results to a model's deployment. However, the effectiveness of safeguards in deployment can depend on features of environments and tasks that control settings do not represent. To broaden where control evaluations can be run, we introduce simulated control evaluati...
  </details>

- **2026-10-22** — Mustafa Omer Gul, Philippe Laban, Tanya Goyal et al. — [Towards User Simulators That Stay On Task And Still Sound Natural](http://arxiv.org/abs/2610.31512v1)
  <details><summary>📄 Abstract</summary>
  Users increasingly rely on AI systems for extended, multi-turn tasks, yet evidence indicates that LLM-based system performance degrades over prolonged interaction. To evaluate and improve AI assistants in such settings, we need user simulators that faithfully follow complex user intents while exhibiting realistic conversational behavior. Existing approaches manifest a trade-off: prompted assistants can follow complex user intents but lack behavioral fidelity, while specialized user simulators be...
  </details>

- **2026-10-22** — Jialin Lu, Xiaoyu Liu, Hengrui Luo et al. — [Lean Finder V2: Semantic Search for Mathlib That Disambiguates User Queries](http://arxiv.org/abs/2610.30843v1)
  <details><summary>📄 Abstract</summary>
  We introduce Lean Finder V2, a semantic search framework for Mathlib that disambiguates user queries through complementary model-level adversarial training and input-level query rewriting. Human mathematicians and coding agents rarely search Mathlib by providing detailed context. In practice, they query short properties, notation, aliases, or hypotheses, leaving much of the intended mathematics implicit. In contrast, existing Mathlib search engines unrealistically assume context-rich queries. Th...
  </details>

- **2026-10-22** — Andrés Daniel Godoy Ortiz — [Meaning Contracts: Local Semantic Geometry in Large Language Models](http://arxiv.org/abs/2610.30715v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the local geometry of semantic meaning in large language models. Current representation analyses ask whether meanings are close in embedding space, or whether linear probes separate semantic classes, but they do not characterize the within-concept local geometry: what is invariant across realizations of a single semantic factor, what varies, and what changes when meaning is refined. This paper characterizes that geometry through two controlled probes evaluated on four architec...
  </details>

- **2026-10-22** — Abderrahmane Issam, Irene E. Winther, Stefan L. Frank — [Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading](http://arxiv.org/abs/2610.31620v1)
  <details><summary>📄 Abstract</summary>
  While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first language (L1). In this work, we investigate whether the cross-lingual transfer within bilingual models aligns with human L1-driven biases during L2 reading. We evaluate bilingual models on eye-tracking data of readers from 12 diverse L1 backgrounds reading English texts. To isolate L1-specific transfer,...
  </details>

- **2026-10-22** — Xuhui Zuo, Chenjie Cao, Tengfei Wang et al. — [Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas](http://arxiv.org/abs/2610.31565v1)
  <details><summary>📄 Abstract</summary>
  Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel represe...
  </details>

- **2026-10-22** — Yun-Chen Cheng, Chih-Pin Tan, Tzu-Hung Huang et al. — [Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision](http://arxiv.org/abs/2610.31510v1)
  <details><summary>📄 Abstract</summary>
  We introduce Piano2Pop, a music-expansion task that transforms piano MIDI into instrumental pop productions. Enabled by recent advances in music generation and polyphonic music transcription, our pseudo-supervised approach conditions a pretrained flow-matching model on piano rolls without aligned piano-pop supervision. We train on synthetic piano-instrumental pairs derived from pop recordings, comparing pair-free transcription, including function-selective (FST) and register-density (RDA) augmen...
  </details>

- **2026-10-22** — Liang He, SiYuan Ma, Qishi Zhan et al. — [ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding](http://arxiv.org/abs/2610.31338v1)
  <details><summary>📄 Abstract</summary>
  Tree-based speculative decoding accelerates large language model inference by verifying multiple candidate branches in parallel. However, in practical serving scenarios, similar requests repeatedly induce overlapping candidate branches. While retrieval-based methods mitigate this by reusing historical drafts, the resulting candidate trees often contain many low-quality branches as the candidate tree grows, which reduces verification efficiency and wastes target-side computation. To address this,...
  </details>

- **2026-10-22** — Igor' Kontorovich, Miriam N. Wallach — [What the submission does not show: Complexifying cognitive offloading in students' mathematical work with LLMs](http://arxiv.org/abs/2610.31335v1)
  <details><summary>📄 Abstract</summary>
  A common concern is that using large language models (LLMs) lets students offload mathematical work that tasks are designed to elicit. Yet such claims often rest on outcomes (e.g., submitted solutions), rather than on evidence of students' work with LLMs. We followed 23 first-year linear algebra students as they solved three differently designed homework tasks with LLMs. Drawing on self-regulated learning and choice-affluent environments, we interpreted each of 429 prompts as a trace of a regula...
  </details>

- **2026-10-22** — Jinjian Jiang, Jing Peng, Rehan Deen et al. — [Bridging the Data Gap: Source-Informed Task-Space Transport for Few-Shot Diffusion](http://arxiv.org/abs/2610.31323v1)
  <details><summary>📄 Abstract</summary>
  Many deployments require a model to move rapidly from a data-rich source to a related target observed only sparsely. This is especially consequential where target data are difficult to collect, as in healthcare settings with persistent population or acquisition imbalances. Retraining or fine-tuning a high-capacity generator for every target is costly and can be statistically unreliable when target data are scarce. We introduce Meta-Diff, which instead learns a recurring source--target relation o...
  </details>

- **2026-10-22** — Shmuel Amar, Benjamin Lieber, Ori Shapira et al. — [CoWriter: Guiding Methodological and Synergetic Human-LLM Co-Authoring](http://arxiv.org/abs/2610.31277v1)
  <details><summary>📄 Abstract</summary>
  While LLMs have transformed text generation, standard chat-and-canvas interfaces often reduce human authoring to quite passive supervision, causing review fatigue, over-reliance on AI, and the sidelining of the human role in long-form, source-grounded writing. Prior systems typically address isolated writing phases, leaving comprehensive end-to-end human-LLM collaboration largely unexplored. In this paper, we introduce CoWriter, a proactive agentic scheme that adapts expert human (co-)authoring ...
  </details>

- **2026-10-22** — Jingxuan Xu, Zihang Xu, Yuechen Luo et al. — [RIPPLE: Recovery Internalization through Process-Level Policy Learning and Effect-Aware Credit for Long-Horizon Agentic Coding](http://arxiv.org/abs/2610.31276v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding agents can observe a failure and generate a plausible critique yet continue along the same incorrect trajectory. We call this the Critique-to-Action Handoff Gap. We introduce RIPPLE, a recovery-oriented training framework that internalizes process-level guidance into a single self-recovering policy. A prefix-only teacher provides evidence-grounded recovery supervision without access to future actions or terminal outcomes. After lightweight distillation, reinforcement learning...
  </details>

- **2026-10-22** — Yijiang River Dong, Zexue He, Cheng Yu et al. — [Memory-Aware Reward Modeling: Learning Human Preferences for LLM Memory Use](http://arxiv.org/abs/2610.31272v1)
  <details><summary>📄 Abstract</summary>
  Memory enables language model assistants to maintain continuity across sessions and generate personalized responses, but knowing more about a user does not necessarily produce responses they prefer. Existing evaluations assess memory capabilities without directly establishing whether memory use benefits the user. To study this gap, we collect approximately 1,000 pairwise judgments from 87 participants using their own ChatGPT queries and personal memories. We find that memory-conditioned response...
  </details>

- **2026-10-22** — Tianyu Lu, Kaicheng Yang, Jiangtao Feng et al. — [Trion-1: Unifying Language, Protein Sequence, and Structure with Diffusion Language Models](http://arxiv.org/abs/2610.31215v1)
  <details><summary>📄 Abstract</summary>
  We envision a general-purpose protein foundation model as a unified, interactive model of sequence, structure, and function, capable of understanding, generation, and cross-modal translation while retaining the instruction-following and reasoning capabilities of modern LLMs. Toward this vision, we introduce Trion-1, the first native, unified, multimodal diffusion language model (dLLM) for proteins. Trion-1 is built on two key design choices: (1) a unified discrete token space that jointly repres...
  </details>

- **2026-10-22** — Ronald Fecso, José Morano, Botond Fazekas et al. — [A Visual Grounding Benchmark for Retinal OCT with Multimodal Large Language Models](http://arxiv.org/abs/2610.31205v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can answer clinical questions about medical images, but trustworthy use requires visual grounding: models should localize the pathology they report rather than rely on spurious shortcuts. Whether MLLMs can visually ground clinical findings in retinal optical coherence tomography (OCT), the most widely used imaging modality in ophthalmology, remains largely unexplored. To address this gap, we introduce RetinaGroundBench, the first benchmark for biomarker v...
  </details>

- **2026-10-22** — Aman Behera, Namit Solanki, Mehul Anand — [Mixing Matters: Evidence Position Bias Across Sequence Mixers in Long-Context Question Answering](http://arxiv.org/abs/2610.31135v1)
  <details><summary>📄 Abstract</summary>
  Long-context models often use answer-bearing evidence less effectively when it appears away from a prompt boundary. We compare this position bias across Transformer, state-space, and hybrid Mamba architectures by moving one gold document through a fixed set of nine distractors. The evaluated Transformers show a beginning advantage that the evaluated state-space models lack, while both families favor evidence near the end. A matched pure-versus-hybrid Mamba comparison points in the same direction...
  </details>

- **2026-10-22** — Roger X. Lera-Leri, Filippo Bistaffa, Athina Georgara et al. — [Constraint Reasoning and Large Language Models Join Forces: Providing Contrastive Explanations for Real-World Optimisation-Based Applications](http://arxiv.org/abs/2610.31119v1)
  <details><summary>📄 Abstract</summary>
  We focus on optimisation-based Decision Support Systems in real-world applications. In this context, we aim to provide contrastive explanations that answer users' questions about recommendations based on the solution of an optimisation problem, specifically a Mixed-Integer Program (MIP). Addressing this endeavour is crucial to ensure human oversight of the decisions implemented, as required by international guidelines on trustworthy and responsible automated decision-making systems. We propose a...
  </details>

- **2026-10-22** — Keshu Wu, Hao Zhang, Rui Gan et al. — [LAST-V2X: Language-Driven Adaptive Scenario Synthesis and Testing for Communication-Induced Failures in V2X Safety Applications](http://arxiv.org/abs/2610.30979v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-everything (V2X) communication enables connected vehicles to make safety-critical decisions, but delayed, missing, or incorrect information can compromise driving safety. Systematically testing such failures is challenging because traffic interactions, communication conditions, and application responses must be jointly configured to produce meaningful scenarios. This paper presents LAST-V2X, a language-driven, adaptive framework for automated scenario synthesis and safety testing of V...
  </details>

- **2026-10-22** — Zhongkai Shangguan, Yanbin Kang, Yihan Cao et al. — [PAIR: Preference-Aligned Intent Retrieval for Premium People Recommendation at LinkedIn](http://arxiv.org/abs/2610.30941v1)
  <details><summary>📄 Abstract</summary>
  General-purpose embeddings trained on profile similarity often misrank candidates in professional networks, where relevance is inherently complementary rather than symmetric. For example, job seekers usually engage with recruiters rather than peers with similar credentials. Current user recommendation systems are often built on profile similarity or social signals such as shared connections, which are effective in friend-oriented social networks where users tend to connect with similar people or...
  </details>

- **2026-10-22** — Ahmed M. Mahran — [What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](http://arxiv.org/abs/2610.30803v1)
  <details><summary>📄 Abstract</summary>
  Replacing the judge can move a benchmark score, and models can be trained to hide capabilities. Both put the evaluator in question: what can it certify? We develop a partition theory of evaluation from one principle: judgement is bounded by perception. An agent's discrimination is the partition of its inputs into classes it cannot tell apart. Discrimination is necessary for capability but not sufficient, so bounds on it bear directly on whether evaluation can show that a model lacks an ability. ...
  </details>

- **2026-10-22** — Shijie Li, Yilin Gao, Tieyuan Chen et al. — [GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL](http://arxiv.org/abs/2610.30796v1)
  <details><summary>📄 Abstract</summary>
  Training large language models for complex reasoning tasks relies on two complementary signals: sparse, outcome-grounded reinforcement learning (RL) for correctness, and dense, token-level distillation for guidance. However, complementarity in supervision does not guarantee compatibility in optimization; imitation-focused distillation can conflict with the outcome-driven RL objective, and existing hybrids lack a principled resolution. We propose \textbf{GIFT} (\textbf{G}radient-\textbf{I}nformed...
  </details>

- **2026-10-22** — Christian Arnold, Ernesto Calvo, Guadalupe Gonzalez et al. — [Invisibilization as a Source of Probability Bias in Language Models](http://arxiv.org/abs/2610.30785v1)
  <details><summary>📄 Abstract</summary>
  Language models are aligned to avoid using protected attributes such as race, ethnicity, and gender to inform their responses. Therefore, they increasingly refuse or hedge when such attributes appear in a prompt. However, if a system must decide how much to learn from what people tell it, it is costly to refuse valuable information because of its source. In this article, we measure the cost of declining information in a two-urn game with an exact Bayesian answer. We present leading LLM models fr...
  </details>

- **2026-10-22** — Jinyi Zhou, Zenan Li, Yuan Yao et al. — [RAIN: Agentic Proof Generation for Rocq-based Software Verification](http://arxiv.org/abs/2610.30759v1)
  <details><summary>📄 Abstract</summary>
  Interactive theorem provers can provide strong correctness guarantees for software, but constructing the proofs remains a challenging and labor-intensive task. Inspired by the recent progress of modern coding agents, we present RAIN, a lightweight proof-specialized agent for Rocq proof generation. RAIN augments an LLM with proof engineering capabilities, including repository exploration, iterative refinement, and checker feedback. This design allows the agent to retrieve lemmas autonomously, rev...
  </details>

- **2026-10-22** — Yang Liu, Zhiqiang Yuan, Shu-Dong Huang et al. — [ULME: Predictive Coupling for Mutually Reinforcing Embedding and Language Modeling](http://arxiv.org/abs/2610.30705v1)
  <details><summary>📄 Abstract</summary>
  Text embedding and text generation are two of the most useful capabilities of modern large language models, yet they are typically provided by separate specialized models (an embedder and a generator) trained with incompatible objectives and deployed side by side in retrieval-augmented generation and agent systems. Recent unified embedding-generation models such as GritLM share parameters between the two capabilities, but they either switch attention regimes between modes or optimize embedding a...
  </details>

- **2026-10-22** — Qince Luan, Jianhui Xu, Yang Xu — [Spectral Smoothing and Spiking Perturbations Reconfigure Capability Profiles and Selective Task Performance in Large Language Models](http://arxiv.org/abs/2610.30676v1)
  <details><summary>📄 Abstract</summary>
  Singular-value spectra encode important structure in transformer feed-forward projections, yet their causal role in downstream behavior remains underexplored. We study post-hoc spectral smoothing and spiking interventions on the up_proj and down_proj matrices. Positive perturbation stretches deviations from the geometric mean, making large singular values larger and small ones smaller (spiking), and vice versa. The intervention preserves singular vectors and the geometric mean of the singular va...
  </details>

- **2026-10-22** — Siran Dai, Qianqian Xu, Peisong Wen et al. — [CODI: Improving Self-Supervised Vision Transformers with Cross Distillation](http://arxiv.org/abs/2610.30639v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised Vision Transformers learn strong image-level representations, but their patch-level representations can be unreliable for dense prediction. We study this mismatch and find that the class token concentrates global semantics on a small number of representative patches, while dense prediction errors often occur on low-attention regions. We provide a local gradient analysis showing that, along the [CLS] attention readout, image-level self-distillation gradients are weighted by [CLS]-...
  </details>

- **2026-10-22** — Jia Gu, Guofeng Zhang, Ian R. Petersen — [On the Structure of Quantum Finite-Level Systems: Decoherence-Free Subsystems, Quantum Nondemolition Variables, and Back-Action-Evading Measurements](http://arxiv.org/abs/2610.30616v1)
  <details><summary>📄 Abstract</summary>
  The purpose of this paper is to conduct a comprehensive structural analysis of quantum finite-level systems in the Heisenberg picture, where the evolution of system observables is modeled by bilinear quantum stochastic differential equations (QSDEs). Firstly, real coordinate transformations that preserve commutation and anticommutation relations are characterized, and relative admissibility between different orthonormal Hermitian bases is formulated. Secondly, strongly aligned subspaces are intr...
  </details>

- **2026-10-22** — Chenyao Yang, Peijin Wang, Yingchao Feng et al. — [KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling](http://arxiv.org/abs/2610.30609v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicles (UAVs) have recently emerged as important remote sensing platforms, and UAV navigation has shown great potential in remote sensing applications. However, existing methods do not explicitly incorporate kinodynamic modeling or safety distances into trajectory generation, resulting in high absolute yaw rates, frequent collisions, and low navigation success rates, which limit safety and motion stability. To address this challenge, we introduce KinoUAV, a kinodynamic benchmar...
  </details>

- **2026-10-22** — Chihiro Matsui — [Hierarchical Reduction of Invariant Subspaces: From Fragmentation to Many-Body Scars](http://arxiv.org/abs/2610.30597v1)
  <details><summary>📄 Abstract</summary>
  We investigate a hierarchy of invariant Hilbert-space structures connecting Hilbert-space fragmentation, partial solvability, and quantum many-body scars. For spin chains with fragmented spin-$1/2$ subspaces and their local deformations, we show, using the spin-$1$ $XXC$ chain as a representative example, how successive local deformations reduce extensive irreducible-string fragmentation through an implicitly embedded spin-$1/2$ invariant space and ultimately to a single scar tower, connecting t...
  </details>

- **2026-10-22** — David Arthur, Ranjini Grove, Zaher Kmail et al. — [DagFlow AI: Agentic Synthetic Data Generation for Personalized Statistics Learning](http://arxiv.org/abs/2610.30580v1)
  <details><summary>📄 Abstract</summary>
  To provide personalized learning experiences in courses that teach data analysis skills, instructors often search for datasets that appeal to a student's interests, align with specific learning objectives, and are appropriate for the student's skill level. Datasets that match all three criteria can be difficult to find. DagFlow-AI is an agentic AI data generation tool that creates realistic, synthetic datasets tailored to these criteria. Rather than mimicking existing datasets or generating obse...
  </details>

- **2026-10-22** — Tao Lin, Yuxin Du, Haoxiao Wang et al. — [FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies](http://arxiv.org/abs/2610.31427v1)
  <details><summary>📄 Abstract</summary>
  Agentic robot systems combine language-model reasoning with robot policies to monitor execution and recover from failures. However, reviewing every action chunk incurs substantial overhead, even in familiar situations. We introduce FastHarness, an experience-driven execution harness that adaptively schedules GPT-6 Astra supervision of a π0.5 policy. A fast path uses stage memory and reviewed outcomes to reduce review frequency as experience accumulates, while a complementary recovery path focuse...
  </details>

- **2026-10-22** — Aleksandr Lazarev, Sofia Zimina, Roman Kuznetsov et al. — [RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation](http://arxiv.org/abs/2610.31121v1)
  <details><summary>📄 Abstract</summary>
  Generated robot videos can look convincing while depicting the wrong interac- tion: a different object is moved, a grasp disappears, or a placement ends out- side its destination. We introduce RGraph-Eval, a reference-based framework that makes these discrepancies explicit through task-grounded temporal scene graphs. Unlike approaches that construct separate evidence representations for different evaluation dimensions, we organize task entities, interactions, and motion within a unified, interpr...
  </details>

- **2026-10-22** — Firuz Kamalov, Hana Sulieman, Ahmed El Sayed et al. — [Algorithmic drift in generative adaptive learning](http://arxiv.org/abs/2610.31041v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence promises to democratize personalized tutoring, yet the longitudinal stability of adaptive systems remains under-theorized. Current ethical discourse focuses on static bias. This paper argues that a distinct threat lies in algorithmic drift: a feedback loop in which minor, demographically asymmetric observation errors compound over time into systemic inequities. We make three contributions. First, we formalize algorithmic drift as a coupled learner--tutor dynami...
  </details>

- **2026-10-22** — Jialin Tian, Zhuofan Li, Xinkai Wang et al. — [UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](http://arxiv.org/abs/2610.30991v1)
  <details><summary>📄 Abstract</summary>
  Robot demonstrations record what the robot saw and what it did. They do not specify how the 3D world changed in between. Scene-level 3D flow describes it by tracking 3D scene points, providing the world representation with 4D geometry. Prior work has used flow to improve robot policies. Flow served as an intermediate prediction that a separate model converts into actions, as a prior injected at inference time, or as an extra output learned together with the action. In all of these designs, flow ...
  </details>

- **2026-10-22** — Jingyu Ru, Xiangyuan Xie, Lixuan Jin et al. — [Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation](http://arxiv.org/abs/2610.30810v1)
  <details><summary>📄 Abstract</summary>
  Loco-manipulation extends the workspace of conventional manipulation by combining mobility with physical interaction, while aerial loco-manipulation further expands this capability into three-dimensional space, enabling robots to reach environments inaccessible to ground-based systems. Moving to an aerial platform, however, gives rise to a demanding control problem, since the vehicle must track trajectories accurately in three dimensions while the motion of the arm and its interaction with the e...
  </details>

- **2026-10-22** — Fanxing Li, Yuxiang Huang, Shengyang Wang et al. — [DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control](http://arxiv.org/abs/2610.31617v1)
  <details><summary>📄 Abstract</summary>
  Tasks such as quadrotor dynamic-gate racing require agents to anticipate external motion while maintaining precise high-frequency control. World-model-based reinforcement learning provides a natural solution by learning latent dynamics for future imagination, yet it often entangles environmental evolution and the robot's own dynamics in a single learned rollout, where model bias can affect policy optimization efficiency. We propose DiffDreamer, a differentiable reinforcement learning framework t...
  </details>

- **2026-10-22** — Viktor Stein, Levin Maier, Wuchen Li et al. — [SympFormer: Inertial Attention Blocks from Damped Hamiltonian Dynamics on Spaces of Probability Measures](http://arxiv.org/abs/2610.31600v1)
  <details><summary>📄 Abstract</summary>
  The attention mechanism underpins modern large language models, yet their dynamics remain only partially understood. Recent perspectives interpret attention blocks as interacting particle systems, whose mean-field limits correspond to gradient flows of energy functionals on spaces of probability densities on $\mathbb R^d$ equipped with Wasserstein-type metrics. We extend this viewpoint by deriving accelerated attention blocks from inertial, Nesterov-type damped Hamiltonian dynamics on these dens...
  </details>

- **2026-10-22** — Bo Xiong, Weisheng Chen, Zongen Ren et al. — [CAMGen: A Core Change-Aware Multi-View Framework for Commit Message Generation](http://arxiv.org/abs/2610.31552v1)
  <details><summary>📄 Abstract</summary>
  Commit messages help developers understand code changes and support software maintenance. Recent approaches use repository context to improve commit message generation (CMG) with large language models (LLMs). However, existing CMG methods provide limited support for understanding how local edits affect functionality jointly implemented by multiple code entities. This functional understanding is essential for generating commit messages that explain the main change and its impact. To address this ...
  </details>

- **2026-10-22** — Shihui Li, Mette Andersen, Martha Lewis — [The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models](http://arxiv.org/abs/2610.31520v1)
  <details><summary>📄 Abstract</summary>
  Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We show that we are able to steer output on classification tasks across different parts of speech. We are also able to steer output on generation tasks, indicating that these techniques can...
  </details>

- **2026-10-22** — Advait Gupta, Sachin Konan, Tom Yin et al. — [AgentVQA: A Unified Benchmark for Agentic Visual Understanding](http://arxiv.org/abs/2610.31494v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can perform a broad range of tasks across diverse settings, yet their performance in agentic contexts remains poorly understood. Although online evaluations in simulators and real-world environments are essential for measuring interactive agent performance, they are costly and challenging to scale. Complementary offline VQA benchmarks can enable faster and more reliable comparisons across agentic domains, yet existing benchmarks remain limited and fragmented. To add...
  </details>

- **2026-10-22** — Vladimir V. Rybkin — [Unifying Time-Independent and Time-Dependent Franck--Condon Pictures in Quantum Mechanochemistry via the Linear Coupling Approximation](http://arxiv.org/abs/2610.31426v1)
  <details><summary>📄 Abstract</summary>
  Quantum chemistry has achieved impressive results in modeling and interpreting mechanochemical transformations at the molecular level. An essential question, the time profile of force application, has   however attracted less attention. Here, the Franck--Condon theory   of quantum mechanochemistry, previously formulated for the   sudden-force limit, is generalized to arbitrary time-dependent   force profiles using the linear-coupling approximation. Solving the   driven harmonic oscillator yields...
  </details>

- **2026-10-22** — Ferdinand Kapl, Kaitlin Maile, Stefan Bauer et al. — [How Depth Growth and Looping Shape In-Context Learning in Language Models](http://arxiv.org/abs/2610.31421v1)
  <details><summary>📄 Abstract</summary>
  Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the acquisition, retention, and mechanisms of this ability. Our analysis spans pretrained language models up to 3B parameters and controlled tasks. The experiments provide evidence for a shared inductive bias toward learning...
  </details>

- **2026-10-22** — João Kenji Suwa, João Pedro Silveira e Silva, Bruno Iochins Grisci — [Post-Hoc Feature Selection Layer for Neural Networks Interpretability](http://arxiv.org/abs/2610.31420v1)
  <details><summary>📄 Abstract</summary>
  The interpretability of complex neural networks remains a critical challenge, especially for models already deployed in high-stakes domains. To address this, we adapted the Feature Selection Layer (FSL) to optimize feature weights post-training, a variant we term post-hoc FSL. Our approach reframes the FSL as a lightweight, trainable module that integrates with already frozen pre-trained models on tabular datasets to highlight the features the original model considers most important. This post-h...
  </details>

- **2026-10-22** — Tammy Schmidt, Luise Koch — [In-Browser Human-AI Co-Writing for Counterspeech: An Exploratory User Study of Agency, Perceived Response Quality, and Time](http://arxiv.org/abs/2610.31357v1)
  <details><summary>📄 Abstract</summary>
  Writing counterspeech that challenges online hate speech can be cognitively and emotionally demanding, whereas fully automated generation may weaken users' sense of voice and responsibility. We present an in-browser AI-assisted co-writing tool that enables users to contribute their own ideas and offers three editable suggestions generated by a large language model using dynamically retrieved hate speech-counterspeech examples from the Multitarget CONAN dataset. We evaluated the tool in an explor...
  </details>

- **2026-10-22** — Kaiyuan Wu, Aditya Nagori, Nicoleta J. Economou et al. — [ClinGuard: a governance framework for reliable, transparent, and auditable clinical coordination](http://arxiv.org/abs/2610.31354v1)
  <details><summary>📄 Abstract</summary>
  ClinGuard is a model-agnostic governance framework that treats clinical coordination as patient-scoped, policy-bound transactions rather than free text. An independent sentinel layer validates and governs agent-proposed actions, escalates when needed, and executes approved actions through limited-privilege connectors. Each transaction is linked to a tamper-evident audit record, while an outcomes monitor informs future autonomy decisions. Using MIMIC-IV-FHIR and skilled-nursing-facility placement...
  </details>

- **2026-10-22** — Tariq Mahassen, Marcin Jastrzebski, Oleksandr Kyriienko — [Quantum Fokker-Planck solvers as trainable generative models](http://arxiv.org/abs/2610.31330v1)
  <details><summary>📄 Abstract</summary>
  We develop and analyze generative models based on quantum solvers of stochastic differential equations. Unlike the common approach based on layered variational quantum circuits with parameterized rotations, we parameterize the potential of a Langevin process. The associated Fokker-Planck (FP) equations are Hermitianized and solved using a linear combination of cosine operators implemented through quantum singular value transformation. By encoding the square root of the stationary density, the mo...
  </details>

- **2026-10-22** — Wenhua Jin, Tiancheng Chen, Sheng Tang et al. — [Moving Regions, Not Moving Objects: Segmenting What Actually Moves under Camera Motion](http://arxiv.org/abs/2610.31209v1)
  <details><summary>📄 Abstract</summary>
  Moving object segmentation is conventionally formulated at the sequence and object level, marking an entire instance as moving once it moves anywhere in a video. Recent instantaneous formulations distinguish moving from stationary intervals, but still generate masks at the object level through frozen segmentation foundation models. Because the mask is derived from an instance-level proposal, motion is typically attributed to the entire instance rather than localized to the regions that actually ...
  </details>

- **2026-10-22** — Felix Saretzky — [PriMa-Causa: Causal Prescriptive Maintenance](http://arxiv.org/abs/2610.31147v1)
  <details><summary>📄 Abstract</summary>
  Automated manufacturing requires data-driven decisions under uncertainty and sparse observational records, and unplanned downtime is a dominant cost of getting them wrong. Prescriptive maintenance recommends a maintenance action against an impending failure rather than merely predicting it. Established reference architectures couple predictive models with rule- or optimisation-based recommendation logic. Selecting a corrective action, however, requires an interventional quantity: how the line be...
  </details>

- **2026-10-22** — Gouki Minegishi, Jingyuan Feng, Hiroki Furuta et al. — [Who Is the Influencer? Consensus Dynamics in Multi-Agent Systems](http://arxiv.org/abs/2610.31105v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems are increasingly used in practice, but their behavior is complex and hard to understand. We design a simple task to ask which model has the most influence on the final consensus when several models are mixed in one system. Experimentally, across seven model families, we find that the opinions of the other models are absorbed into the opinion of the stronger model, the one with more parameters. This happens even though the task requires no pretraining knowledge and has no ...
  </details>

- **2026-10-22** — Md. Jalil Piran — [Evaluating Artificial Wisdom (AW): A Trajectory-Based Framework for Context-Sensitive Decision Regulation](http://arxiv.org/abs/2610.31012v1)
  <details><summary>📄 Abstract</summary>
  Capability benchmarks measure what large language models can do, but not whether their recommendations remain appropriate as decision conditions change. This paper proposes a trajectory-based measurement framework and prospective validation protocol for artificial wisdom, defined behaviorally as context-sensitive regulation of judgment. Versioned reference specifications determine admissible responses and transition materiality before evaluation. Seven stage-level criteria assess judgment under ...
  </details>

- **2026-10-22** — Leyuan Jin, Jiahao Mei, Yixuan Yuan et al. — [EEG-Captioner: Grounding EEG-to-Language Generation in Fundamental Signal Properties](http://arxiv.org/abs/2610.30995v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG)-to-language models offer a promising approach for translating complex neural signals into human-readable descriptions. However, generating plausible language does not necessarily demonstrate that a model has learned to interpret the underlying EEG signal. A direct way to assess such interpretation is to probe objectively measurable properties of the signal itself. We therefore construct an EEG-language dataset of 160,781 segments annotated with signal-level question ...
  </details>

- **2026-10-22** — Shin Yamaguchi, Masaya Taniguchi, Tatsuki Kuribayashi et al. — [Once a Tree, Always a Tree? Cross-lingual Transfer of Hierarchical Generalization in Language Models](http://arxiv.org/abs/2610.30960v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) often exhibit successful cross-lingual transfer through continued (pre)training, still their underlying process remains unclear. One possibility is that LMs can leverage the evidence toward language-universal principles, namely, hierarchical structure, from a source language (L1) to a new language (L2), while many other non-linguistic explanations, e.g., improved initialization of position embeddings, can be potentially possible. In this study, to quantify the cross-linguis...
  </details>

- **2026-10-22** — Songlin Yang, Zhe Wang, Xiaotong Zhao et al. — [Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation](http://arxiv.org/abs/2610.30926v1)
  <details><summary>📄 Abstract</summary>
  Cinematic video generation requires both temporal inference from limited inputs (i.e., sparse rather than frame-by-frame guidance) and factor-aware control of character, scene, action, and camera. Multimodal large language models (MLLMs) offer useful priors for both capabilities, but their representations are not automatically actionable for video generation: a Video Diffusion Transformer (DiT) may bypass them through native conditioning pathways, and using them does not ensure either factor-awa...
  </details>

- **2026-10-22** — Lorenzo Mensi, Simone Cuonzo, Maria Chiara Angelini et al. — [Learning Cole-Hopf Coordinates for Stochastic Growth Dynamics: the KPZ class](http://arxiv.org/abs/2610.30919v1)
  <details><summary>📄 Abstract</summary>
  Inferring effective equations from observations of nonlinear stochastic processes is challenging because individual trajectories are noisy realizations, while the relevant physical information is encoded in ensemble statistics. We introduce a data-driven framework that learns a change of variables in which nonlinear stochastic dynamics become linear. The model combines a neural change of representation with a linear stochastic latent evolution and is trained through a short-time moment-matching ...
  </details>

- **2026-10-22** — Barbara Weber, Olaf Zimmermann, Marco Franceschetti — [When Code Gets Cheap, Evaluation Gets Scarce: An Experience Report on AI-Assisted Agile Software Engineering](http://arxiv.org/abs/2610.30916v1)
  <details><summary>📄 Abstract</summary>
  Coding assistants are widely reported to speed up code production; most accounts stop there. We report the end-to-end construction and deployment of a compliance-critical, human-in-the-loop exam-grading system, built by a single developer who wrote no code by hand, protected by a gated process from stakeholder persona to audited behavior. The initial system was built in three working days and could grade a real cohort. We draw one claim from this experience: AI changes software engineering less ...
  </details>

- **2026-10-22** — Yuhang Xie, Cheng Li, Chenliang Li et al. — [Building Presentation Intelligence for High-Quality Slide Generation](http://arxiv.org/abs/2610.30888v1)
  <details><summary>📄 Abstract</summary>
  PowerPoint presentations (PPTs) are a dominant medium for communication across diverse domains, yet high-quality PPT generation still depends heavily on labor-intensive human effort. Recent advances in large language models (LLMs) for agentic tasks have created both new opportunities and challenges (Chen et al., 2026) for automatic PPT generation. In this work, we present a unified training framework for automatic PPT generation toward presentation intelligence, integrating cross-validated data ...
  </details>

- **2026-10-22** — Albert Linda, Shiv Shankar, Dierk Raabe — [Designing sustainable high-entropy alloys directly from mixed oxides: A thermodynamic perspective](http://arxiv.org/abs/2610.30870v1)
  <details><summary>📄 Abstract</summary>
  Hydrogen-based direct reduction (HyDR) of mixed oxide precursors offers an alternative route to produce sustainable alloys, bypassing the sequential extraction, refining, and remelting steps that dominate the carbon footprint of conventional metallurgy and individual metal production. However, the thermodynamic limits and most effective H$_2$/H$_2$O ratio needed for full metallization of multicomponent oxides are not yet established. This is because the formation of metallic and oxide solid solu...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 694 |
| prompt-injection | 637 |
| memory-poisoning | 56 |
| tool-use-attack | 163 |
| backdoor | 541 |
| adversarial-attack | 650 |
| privacy-leakage | 4467 |
| steganography | 83 |
| misuse | 1243 |
| red-teaming | 144 |
| vulnerability | 3766 |
| defense | 3638 |
| alignment | 3428 |
| robustness | 3723 |
| watermark | 663 |
| unlearning | 118 |
| agent-safety | 66 |
| benchmark | 70 |
| survey | 424 |
| other | 10034 |

---

📚 **全部 34608 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-27 21:43:28*