<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-34825-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-30 04:19 ｜ **论文总数 / Total Papers**: 34825（近 30 天 / Recent 30 days: 4483）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 34825 篇论文（含摘要、分类筛选、搜索）/ View all 34825 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 697
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 640
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 56
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 164
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 542
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 651
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4477
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 84
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1255
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 144
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3783
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3667
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3452
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3746
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 673
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 118
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 66
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 71
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 427
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10112

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4483 篇，完整 34825 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4483 papers from the last 30 days (with date, authors & abstract). For the full list of 34825 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-10-27** — Abhijit Mazumdar, Manuela L. Bujorianu, Rafal Wisniewski — [Probabilistic Sequential Safety for Stochastic Dynamical Systems](http://arxiv.org/abs/2610.37311v1)
  <details><summary>📄 Abstract</summary>
  In this letter, we investigate a notion of probabilistic safety for a stochastic dynamical system. Standard safety notions are based on the idea that an unsafe region of the state-space must be avoided at each instant. In contrast, we study a sequential safety notion which is based on avoiding a tuple of target regions of the state-space. The proposed safety notion is inspired by many practical systems, ranging from modeling jailbreak attacks in large language models (LLMs) to predicting hazardo...
  </details>

- **2026-10-27** — Krishna Kanth Nakka, Yujun Wang, Shijie Zhou et al. — [PrivacyEvalClaw: A Tool-Augmented Deliberative Agent for Auditing Privacy Leakage in LLM Jailbreak Responses](http://arxiv.org/abs/2610.36711v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation is a critical bottleneck in privacy red-teaming of large language models (LLMs): determining whether a jailbreak response actually reveals personal information can be difficult when disclosures are indirect, contextual, partial, or obfuscated. Existing evaluation approaches increasingly rely on guard models and LLM-as-Judges, yet these evaluators may interpret the same response differently. To better characterize this evaluation setting, we conduct a systematic study of priva...
  </details>

- **2026-10-26** — Junle Li, Siqi Chen, Jiakai Li et al. — [SpecGuard: Detecting Multi-Turn LLM Jailbreaks via Specification-Based Runtime Monitoring](http://arxiv.org/abs/2610.36258v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn jailbreaks turn dialogue safety into a trace property: a violation may become identifiable only when user intent and assistant behavior are considered across multiple turns. Existing guard models largely classify individual messages or exchanges and return risk scores or labels, without executable safety semantics or a formally checkable decision trail. We present SpecGuard, a training-free, specification-driven framework for monitoring multi-turn LLM interactions. SpecGuard uses a fi...
  </details>

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 6 papers

- **2026-10-27** — Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al. — [Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](http://arxiv.org/abs/2610.37657v1)
  <details><summary>📄 Abstract</summary>
  We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted content without following injected instructions. We evaluate HoS on Llama-3.3-70B-Instruct and GPT-OSS-20B. We compare it against SecAlign++, a state-of-the-art finetuning-based defense, and ASIDE, a defens...
  </details>

- **2026-10-27** — Zihan Chen, Lei Nico Zheng, Di Zhu — [What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection Attacks](http://arxiv.org/abs/2610.36422v1)
  <details><summary>📄 Abstract</summary>
  Attack logs and red-team reports show targets the attacks used against them, to help them repair their defenses. Prompt injections against large language models (LLMs) are plain text, so such records also hand targets a working copy. Drawing on social learning theory and work on the victim-offender overlap, we study what targets do with that copy in Tensor Trust, an online game whose players defended LLM-guarded accounts, attacked one another's, and could read every attack they received. Using a...
  </details>

- **2026-10-26** — Yuepeng Hu, Chongyu Fan, Sirat Samyoun et al. — [Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol](http://arxiv.org/abs/2610.36108v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly access external tools through the Model Context Protocol (MCP), but the natural-language metadata used to describe those tools creates a prompt-injection surface. Within this established tool-poisoning surface, we study Log-To-Leak, an additive post-hoc logging attack that induces a separate attacker-controlled call after the final legitimate call. Its payload targets the user query, MCP server name, server response, and agent response. We operationalize the injected dire...
  </details>

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


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-10-27** — Hannes Ill, Rafi Al Attrach, Rajna Fani et al. — [M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](http://arxiv.org/abs/2610.37459v1)
  <details><summary>📄 Abstract</summary>
  Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical derivation tasks across 15 task families on MIMIC-IV and eICU, to test whether AI coding agents can reproduce such derivations and how clinician-reviewed agent skills change their results. Its controls decompose the value of ...
  </details>

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
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-10-27** — Azim Ospanov, Zijin Feng, Ding Ding et al. — [Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs](http://arxiv.org/abs/2610.36767v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have made remarkable progress on solving competition-level mathematics, yet their ability to verify natural-language mathematical proofs remains relatively underexplored. This gap is especially pronounced for Olympiad-level proofs, which require meticulous assessment of each claim in a long reasoning chain. Current proof verification thus primarily relies on expert inspection, which is costly to scale. In this paper, we present a systematic study of LLM-based verific...
  </details>

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-10-27** — Zirui Ding, Xinxin Fan, Hao Yuan et al. — [Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories](http://arxiv.org/abs/2610.37369v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially induced failures can be characterized using the same internal coordinates. Towards this end, we in this paper study a white-box diagnostic framework CauTrace to disclose the root-cause of why LLM fails from three fundamental inspections: Functi...
  </details>

- **2026-10-26** — Shiwei Liu, Linyuan Wang, Nuolin Sun et al. — [A JiT-Based Denoising Defense Method Against Adversarial Examples for Radio Signal Automatic Modulation Classification](http://arxiv.org/abs/2610.35084v1)
  <details><summary>📄 Abstract</summary>
  Automatic modulation classification (AMC) of radio signals is a core technology for spectrum monitoring and electromagnetic situational awareness. Deep neural networks (DNNs) play an important role in this field owing to their powerful feature extraction capabilities and end-to-end learning paradigm. However, their vulnerability to adversarial attacks poses serious security challenges to practical deployment. Adversarial training, a common defense, has limitations including poor generalization a...
  </details>

- **2026-10-26** — Mintong Kang, Stephen Rawls, Melissa Kazemi Rad et al. — [The Target Agent Is Its Own Best Critic but a Poor Proposer: Self-Improved Red Teaming](http://arxiv.org/abs/2610.34965v1)
  <details><summary>📄 Abstract</summary>
  Automatic red teaming increasingly relies on large language models (LLMs) to iteratively diagnose failed attacks and propose improved adversarial prompts or injections. Although prior work strengthens this loop through prompt engineering and search-harness design, the mechanisms underlying its two core roles, criticism and attack proposal, has not been explored. To further investigate the core roles and therefore improve red teaming effectiveness, we disentangle two design choices: whether criti...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 20 papers

- **2026-10-27** — Pratham Sharma, Mohd Faisal Khan, Santosh Kumar Vishvakarma — [SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based Early Exit for SRAM based Digital Compute-in-Memory](http://arxiv.org/abs/2610.37601v1)
  <details><summary>📄 Abstract</summary>
  Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3). To address these, we present four synthesizable peripheral blocks: a Flush-Merge Enable (FME) controller, a Confidence-Based Early-Exit (EE) module, a Precision Register wit...
  </details>

- **2026-10-27** — Wei Zhu, Meiyun Zuo, Huiping Sun — [Blindfold: Keeping the Audit Coin Secret from LLM Agents](http://arxiv.org/abs/2610.37055v1)
  <details><summary>📄 Abstract</summary>
  Audit-based certification bounds the violation rate of an LLM agent by auditing a random fraction $\varepsilon$ of actions and reweighting the audited labels; its validity is meant to rest only on the defender's audit coin. We show that it also rests on a confidentiality property: the coin must not interfere with the agent's view before the action commits, at a time the agent chooses. We call this pre-commit noninterference (PNI) and measure its violation by $D_{\mathrm{A}}$, the total-variation...
  </details>

- **2026-10-27** — Ziqi Liao, Jiaqi Shen, Yiming Na et al. — [Who Knows What - and What Does It Support? Perspective-Bounded Evidence Calibration for Multimodal Theory of Mind](http://arxiv.org/abs/2610.36824v1)
  <details><summary>📄 Abstract</summary>
  Theory of Mind (ToM), the ability to infer others' beliefs, goals, and intentions, is a cornerstone of social intelligence. Multimodal ToM requires inferring an agent's mental state from evidence that is available to that agent, rather than from the complete episode observed by the solver. Existing LLM-based and Bayesian model-based approaches reconstruct global event traces, yet they do not explicitly distinguish objective events from agent-admissible evidence during hypothesis evaluation. Cons...
  </details>

- **2026-10-27** — Kofi Ampomah, Tu Le — [Measuring Users' Security and Privacy Concerns About Third-Party Community Bots on Discord](http://arxiv.org/abs/2610.36626v1)
  <details><summary>📄 Abstract</summary>
  Third-party community-based bots are central to how social platforms such as Discord work. They moderate content, manage roles, play music, and support AI-assisted conversations across millions of servers. Yet when a bot is installed in a server, it can access messages, user profiles, and server metadata concerning members who did not participate in the installation decision, with no standardized way to communicate the associated security and privacy implications. In this paper, we analyze 23,10...
  </details>

- **2026-10-27** — Manan Uppadhyay, Himanshu Beniwal, Prashant Kodali et al. — [The State and Fate of Multilingual, Contextual Evaluation in the NLP World](http://arxiv.org/abs/2610.36990v1)
  <details><summary>📄 Abstract</summary>
  Multilingual evaluation benchmarks are the primary instrument for assessing whether large language models generalize beyond English, yet the adequacy of these benchmarks has received little systematic scrutiny. We present a data-driven audit of 51 recent multilingual benchmarks spanning 242 datasets and 219 languages, organized around three pillars: coverage, representativeness, and rigor. Our analysis reveals that coverage is wide but thin with 36% of evaluated languages appearing in only a sin...
  </details>

- **2026-10-26** — Tushar Nayan, Pratik Poudel, Qian Lou et al. — [Detecting and Mitigating Query-Based System Prompt Leakage Attacks](http://arxiv.org/abs/2610.36295v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) rely on proprietary system prompts to enforce task directives, safety policies, and access controls. These prompts are vulnerable to query-based leakage attacks, where black-box adversaries extract confidential instructions through adaptive, multi-turn interactions. Existing defenses often assess queries independently, missing malicious behavior that emerges across interactions.   We present AdvGuard, a model-agnostic framework for detecting and mitigating system pro...
  </details>

- **2026-10-26** — Malithi Mithsara Wanniarachchi Kankanamge, Ning Yang, Sree Bash Debnath et al. — [Evaluating Federated Vision-Language and Vision-Only Models for Privacy-Aware Breast Cancer Imaging](http://arxiv.org/abs/2610.36379v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) shows promise for breast imaging, but limited labeled data, institutional data fragmentation, and privacy concerns hinder centralized training. We investigate a privacy-aware federated learning framework combining pretrained vision-language models (VLMs) with client-level differential privacy. We compare general-purpose CLIP models, biomedical BiomedCLIP, and an ImageNet-pretrained ViT-B/16 baseline on two public breast imaging datasets, with and without differential...
  </details>

- **2026-10-26** — Ahmad Abdel-Azim, Xihong Lin — [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](http://arxiv.org/abs/2610.36361v1)
  <details><summary>📄 Abstract</summary>
  Individual-level genotype data underpin genetic discovery, disease-risk modeling, and therapeutic development, yet many critical settings remain data-limited, including underrepresented ancestries, rare or imbalanced disease cohorts, and restricted-access biobanks. Conditional synthetic genome generation would support privacy-aware benchmarking, simulation, and data augmentation, but requires learning an ultra-high-dimensional discrete distribution over hundreds of thousands to tens of millions ...
  </details>

- **2026-10-26** — V. M. Tkachuk, M. I. Samar — [Quantum computation of energy level degeneracy and thermodynamical properties of spin systems](http://arxiv.org/abs/2610.35660v2)
  <details><summary>📄 Abstract</summary>
  We propose a hybrid quantum-classical method for reconstructing energy-level degeneracies and thermodynamic properties of spin systems. A single ancilla qubit is used to measure the partition function at imaginary inverse temperatures. For spectra lying on a known equally spaced energy grid, the inverse discrete Fourier transform allows exact reconstruction of degeneracies in the absence of noise, without spectral leakage. The quantum circuits are optimized using commuting interactions and Euler...
  </details>

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

- **2026-10-25** — Cheng Gui, Xiang Zheng, Yutao Wu et al. — [SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](http://arxiv.org/abs/2610.34365v2)
  <details><summary>📄 Abstract</summary>
  Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows. This modularity creates a confidentiality risk: the interactions that deliver a skill's capability can also reveal the skill itself. We build an extensible benchmark of 40 protected skills across eight open- and closed-source science-agent platforms, comparing direct, fixed-strategy, and bandit-guided iterative probing under reference-based and reference-free evaluatio...
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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-10-26** — Hanzhang Wang, Manxi Wu — [How Learning Selects Equilibria and When It Leads to Collusion](http://arxiv.org/abs/2610.36306v1)
  <details><summary>📄 Abstract</summary>
  We study how learning algorithm design shapes equilibrium selection in infinite-horizon discounted Markov games with finite states and actions. Each episode, players choose smooth best responses to beliefs about opponents' policies, test them using noisy observations, and resample rejected beliefs or explore at rates determined by increasing transformations of their discounted values. We show that stochastically stable states induce approximate stationary Nash equilibria maximizing the minimum t...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 21 papers

- **2026-10-27** — Trent R. Northen, Mingxun Wang — [Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families](http://arxiv.org/abs/2610.37484v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to irreversibly destroy living systems. We construct and use a real-data continued-pretraining "coupled welfare" corpus of documented human/biosphere/AI dependency, option value under irreversibility, and recovery from harm. ...
  </details>

- **2026-10-27** — Saket Reddy, Amro Abbas, Anshuman Suri et al. — [Follow the Gradient: Tracing Safety Degradation Back to Training Data](http://arxiv.org/abs/2610.37481v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning Large Language Models (LLMs) on instruction data can quietly erode their safety, even when no training example looks harmful. Because this safety-degrading data looks benign, standard content filters struggle to catch it. We tackle this problem by developing SimpleLoRIF, a scalable gradient embedding method that identifies fine-tuning examples whose gradients align with unsafe behavior. By simplifying a low-rank attribution method and restricting backpropagation to the final four tra...
  </details>

- **2026-10-27** — Valdini Douglace Lemofouet, Blessing Ngozi Uzor, Paula Chikaodinaka Anyanwu et al. — [Aligning Large Language Models for Safety in African Languages: A Case Study of Hausa](http://arxiv.org/abs/2610.37245v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment research for large language models (LLMs) remains concentrated on high-resource languages, leaving open how existing alignment methods perform in low-resource, culturally distinct settings. We study this question for Hausa, a language spoken by more than 200 million people across West Africa. We introduce HausaSafeLM, one of the first Hausa safety preference dataset, built from 10,000 prompts derived from PKU-SafeRLHF: 3,000 human-corrected (gold) and 7,000 machine-translated (s...
  </details>

- **2026-10-27** — Yi Wei, Yue Zhang, Peijun Hou et al. — [RadarCom: Unlocking Simultaneous Communication and Sensing on Commodity Automotive mmWave Radars](http://arxiv.org/abs/2610.36622v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-vehicle (V2V) communication can improve road safety and traffic efficiency, yet its deployment remains limited by the need for dedicated communication hardware and supporting infrastructure. Meanwhile, production vehicles are already widely equipped with millimeter-wave radars for sensing. To unlock their communication potential, this paper presents RadarCom, a software-defined system that enables direct radar-to-radar communication on unmodified commercial off-the-shelf (COTS) automo...
  </details>

- **2026-10-27** — Chuming Wei, Churui Yang, Zihan Zhang et al. — [ADTGuard: Adaptive Depth-Time Safeguard for Streaming Inference in Large Language Models](http://arxiv.org/abs/2610.36574v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can generate fluent responses to diverse user requests, yet streaming may expose users to harmful content before generation is complete. Existing guardrails face two limitations in this setting. First, post-hoc moderation at response or chunk boundaries delays intervention, risking harmful exposure when content is released before verification. Second, even with token-level detection, coarse response-level supervision does not specify when harmful content begins, whil...
  </details>

- **2026-10-27** — Yanyan Zhang, Fei Shen, Ting Yan et al. — [CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents](http://arxiv.org/abs/2610.36570v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language agents increasingly modify external systems, yet most runtime safeguards allocate scrutiny by generic uncertainty scores or coarse mutation heuristics. We introduce CASEL (Consequence-Aware Selective Execution Layer), a model-agnostic runtime allocation policy that combines calibrated failure probability, state-dependent consequence, reversibility, ambiguity, and evidence freshness to choose, for each proposed tool call, among direct execution, verification, sandboxing, clari...
  </details>

- **2026-10-27** — Zack Yu, Nicholas Lee, Minjae Lee et al. — [GEPA-Curator: Curated Learning for Self Improving Agents](http://arxiv.org/abs/2610.37651v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may even be harmful; and thus it is essential to curate which tasks are provided to t...
  </details>

- **2026-10-27** — Weiyu Han, Haoyu Jiang, Jie Sheng et al. — [TRIDENT-Seq: Profile-Matched Prefix-Future Contrast for Label-Efficient Payment Risk Modeling](http://arxiv.org/abs/2610.37365v1)
  <details><summary>📄 Abstract</summary>
  Ant International accumulates large volumes of transaction history across users and payment businesses. Confirmed fraud and chargeback outcomes, by contrast, are scarce, delayed, and specific to each business. A single encoder pretrained on unlabeled histories could serve all businesses, but only if pretraining captures the behavior that separates risk. Coarse activity differences can make contrastive pretraining on transaction logs too easy: transaction volume, amount, and timing can distinguis...
  </details>

- **2026-10-27** — Ahmed M. Fetouh, Mariam Labib, Nsrin Ashraf et al. — [REGLAT at ArGuard Shared Tasks: An Ensemble-Based Model Integrating NER for Harmful Content Detection in Arabic](http://arxiv.org/abs/2610.37265v1)
  <details><summary>📄 Abstract</summary>
  Detecting harmful content in Arabic is challenging because of dialectal variations and the semantic overlap between different harm categories. This paper presents a two-stage approach for classifying Arabic user prompts into seven categories of harmful content. First, GLiNER is used to extract harm-related entities from each prompt. The extracted entities are then added to the original text and passed to a fine-tuned MARBERT classifier for final classification. The approach combines explicit ent...
  </details>

- **2026-10-27** — Alicem Koyun — [PRISM: Pathology Reliability In Scarce-label Medicine. A Tile-level Benchmark of Pathology Foundation Models](http://arxiv.org/abs/2610.36517v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models are typically benchmarked on classification performance at full label availability and on in-distribution test sets, while calibration, behavior at low label budgets, and robustness under cross-institutional shift are seldom evaluated jointly. We introduce PRISM, a tile-level benchmark that measures the reliability of pathology foundation models along four axes: model choice, label fraction, calibration, and out-of-distribution transfer. PRISM evaluates eight foundati...
  </details>

- **2026-10-26** — Ali Khairallah, Arkaitz Zubiaga — [AK_QMUL at ArGuard Shared Tasks: A Single Fine-Tuned JAIS for Arabic Harmful-Prompt Detection](http://arxiv.org/abs/2610.36360v1)
  <details><summary>📄 Abstract</summary>
  We present AK_QMUL's submissions to the ArGuard-2026 shared tasks on Arabic harmful-prompt detection: a binary safe/unsafe task (B1) and a seven-way harm-domain task (B2). Both submissions use one backbone -- JAIS-6.7B fine-tuned with 4-bit QLoRA and a linear classification head over its last-token representation. For B1 we train a four-way head that factors the label by dialect register {safe, unsafe} x {MSA, other}, we augment the training fold with MSA prompts from AraSafe, and decode with a ...
  </details>

- **2026-10-26** — Oleeviya Babu Poikarayil, Tony Basil Babu, Abdulrahman Nahhas et al. — [When Retrieval Is Not Enough: Obsolete Facts in Agent Memory](http://arxiv.org/abs/2610.36308v1)
  <details><summary>📄 Abstract</summary>
  Memory-agent benchmarks often collapse retrieval and answer generation into one score, making it hard to tell whether a failure comes from missing an update or from not using an update that was already retrieved. We examine this distinction on the single-hop FactConsolidation task of MemoryAgentBench. With Qwen2.5-7B-Instruct on 6K-history BM25 accuracy drops from 45% to 32% when the retrieved evidence budget grows from 64 to 512 tokens, even though a gold-assisted post-hoc audit finds the newes...
  </details>

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


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 55 papers

- **2026-10-27** — Niccolò Fontana, Mattia Martini, Huyên Pham — [Linear-quadratic mean field games with Volterra dynamics](http://arxiv.org/abs/2610.37622v1)
  <details><summary>📄 Abstract</summary>
  We study a class of linear-quadratic mean field games in which the state of each agent follows a stochastic Volterra equation of convolution type. The resulting dynamics are non-Markovian and account for memory effects through a completely monotone kernel, while the mean field interaction enters both the drift and diffusion coefficients. Exploiting a Markovian lifting of the Volterra dynamics, which restores the Markov property at the price of moving to an infinite-dimensional state space, we ch...
  </details>

- **2026-10-27** — Tudor Braicu, Joseph DelPreto, Jared Boyer et al. — [Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video](http://arxiv.org/abs/2610.37619v1)
  <details><summary>📄 Abstract</summary>
  Agile robots require spatiotemporal intelligence to interpret scenes, reason about interactions, and anticipate future events. Yet it remains unclear how well foundation vision models support these capabilities, particularly from a moving egocentric camera, which is a natural view for robots. To investigate this, we collect an annotated tennis dataset and train a suite of vision models on spatiotemporal tasks. Our dataset contains egocentric video synchronized with five allocentric videos, estim...
  </details>

- **2026-10-27** — Sihan Yang, Weichen Bai, Ruichuan An et al. — [EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](http://arxiv.org/abs/2610.37609v1)
  <details><summary>📄 Abstract</summary>
  As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Envi...
  </details>

- **2026-10-27** — Dequan Ou, Austin Lopez, Quentin Missinne et al. — [Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation](http://arxiv.org/abs/2610.37543v1)
  <details><summary>📄 Abstract</summary>
  Event cameras offer low latency, high dynamic range, and milliwatt-level power consumption, making them ideal for agile robots such as tiny drones navigating through cluttered environments. However, existing simulators generally render photorealistic images before converting them into events, making large-scale reinforcement learning prohibitively slow. We propose an analytic event simulator that exploits what event cameras fundamentally measure - moving contrast edges - to synthesize event stre...
  </details>

- **2026-10-27** — Hongyan Chang, Hady Elsahar, Tom Sander et al. — [Watermark Basins: Black-Box Detection of Distilled LLMs](http://arxiv.org/abs/2610.37266v1)
  <details><summary>📄 Abstract</summary>
  Proprietary language models and their reasoning traces are vulnerable to API-based distillation, where an adversary trains a student model on the teacher model's outputs. To obtain evidence of distillation, model providers can watermark the teacher's outputs, aiming to leave a radioactive signal in the student's outputs. Existing black-box detectors search for such radioactivity using token-level statistics of the suspect model's outputs. However, token-level signals are not always detectable, f...
  </details>

- **2026-10-27** — Yuhang Qiu, Ziwei Li, Jinfeng Xu et al. — [MAPLE-Sec: Mobility-Aware Partitioned Language-Model Engine for Roaming IoT Security](http://arxiv.org/abs/2610.37147v1)
  <details><summary>📄 Abstract</summary>
  Mobile Internet-of-Things (IoT) endpoints such as connected vehicles, wearables, and drones continuously cross heterogeneous network domains, creating handover-driven attack surfaces that static, cloud-anchored detectors cannot follow. However, three obstacles block real-time detection on such roaming endpoints: detection state is lost at every inter-domain handover; transmitting raw telemetry to a fixed detector exhausts the uplink and the device battery; and full-depth language model inference...
  </details>

- **2026-10-27** — Theodoros Kouzelis, Spyros Gidaris, Nikos Komodakis — [Self-Regularized Flow Language Models](http://arxiv.org/abs/2610.37115v1)
  <details><summary>📄 Abstract</summary>
  We introduce SERF (Self-Regularized Flow Language Models), a simple self-supervised framework for improving continuous diffusion language models by exploiting the denoising trajectory itself. While continuous flow-based language models offer a promising alternative to autoregressive generation, their training objectives typically rely on supervision from clean target tokens, leaving the denoising trajectory underexploited as a learning signal. SERF addresses this limitation through noisy-to-clea...
  </details>

- **2026-10-27** — Daniele Lizzio Bosco, Jacopo Cossio, Simone Faro et al. — [AI-Assisted Discovery of CNOT Decompositions for Quantum Permutations on Constrained Topologies](http://arxiv.org/abs/2610.37045v1)
  <details><summary>📄 Abstract</summary>
  Efficient quantum circuit compilation is challenging for quantum computers, where limited qubit connectivity can introduce substantial overhead in the implementation of logical operations. Recent AI-assisted synthesis methods have shown considerable potential for reducing circuit complexity, but their role in uncovering principles that can guide the design of new deterministic compilation algorithms remains largely unexplored. In this work, we investigate this perspective for the synthesis of qu...
  </details>

- **2026-10-27** — Augusto Del Zotto, Luca Melzi, Haoling Xiang — [Extended stability timescales for the 2D3C rotating stratified Boussinesq equations](http://arxiv.org/abs/2610.37013v1)
  <details><summary>📄 Abstract</summary>
  We study the time evolution of a vertical-slice model for incompressible inhomogeneous rotating fluids perturbed around a stably stratified rest state with linear buoyancy profile. For $\varepsilon$-small localized initial data with vanishing potential vorticity, we prove that solutions remain of size $O(\varepsilon)$ up to times of order $\varepsilon^{-\frac43}$, and up to times of order $\varepsilon^{-2}$ in a regime where the Brunt--Väisälä frequency and the Coriolis parameter are comparable....
  </details>

- **2026-10-27** — Wenhao Xu, Yanheng Mai, Yifei Fu et al. — [HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour](http://arxiv.org/abs/2610.36825v1)
  <details><summary>📄 Abstract</summary>
  Humanoid parkour requires robots to reason about future footholds and whole-body motions over highly discontinuous terrain. We revisit the information asymmetry in asymmetric actor-critic learning for perceptive humanoid locomotion: the critic exploits privileged simulator signals during training, whereas the deployable actor operates solely from onboard perception. We argue that the key is not exposing privileged information to the actor, but learning a deployable approximation of it to narrow ...
  </details>

- **2026-10-27** — Le Yang, Yucheng Huang, Junyu Chen et al. — [SAGE: Saliency-Annealed Gated Encoder for Universal Vision Recognition](http://arxiv.org/abs/2610.36719v1)
  <details><summary>📄 Abstract</summary>
  When adapting self-supervised Vision Transformers (ViTs) to dense prediction, existing methods often treat the ViT as a passive feature extractor and may underuse the rich priors encoded in its representations, including saliency, global context, and high-frequency details. We propose SAGE (Saliency-Annealed Gated Encoder), an enhanced ViT-Adapter backbone that explicitly exploits these priors through three complementary innovations: (1) a saliency-guided architecture that extracts DINO-style cl...
  </details>

- **2026-10-27** — Shuo Chen, Li Cui, Cunxin Huang et al. — [NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](http://arxiv.org/abs/2610.36553v1)
  <details><summary>📄 Abstract</summary>
  Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central challenge in DFO to effectively exploit accumulated observations to select informative evaluation points under a limited budget. In this light, we introduce the NextEval solver, an agent-based DFO solver, which integrates th...
  </details>

- **2026-10-27** — Yuchen Zhang, Yaxiong Wang, Yujiao Wu et al. — [ARISE: Authentic Reference-Informed Stability Enhancement for Continual Multimodal Forgery Detection](http://arxiv.org/abs/2610.36509v1)
  <details><summary>📄 Abstract</summary>
  Multimodal forgery detection is commonly studied under a static assumption: training attacks are expected to approximate those encountered after deployment. This assumption becomes increasingly fragile as generators, editing systems, and multimodal large language models continually introduce new forgery mechanisms and forensic evidence. We formulate this problem as attack-incremental continual multimodal forgery detection, where the binary real/fake interface remains fixed while emerging attacks...
  </details>

- **2026-10-26** — Wang Tang, Fethiye Irmak Dogan, Linbo Qing et al. — [Hierarchical Multimodal Interaction Reasoning for Dyadic Relationship Recognition](http://arxiv.org/abs/2610.36249v1)
  <details><summary>📄 Abstract</summary>
  Dyadic relationship recognition aims to identify the latent social relationship between two individuals from their multimodal interactions. Existing methods typically project heterogeneous cues into a shared representation and optimise a flat classification objective, overlooking that relationships may rely on different interaction patterns. For instance, distant relationships can often be inferred from direct behavioural correspondence, whereas close relationships are better reflected by coordi...
  </details>

- **2026-10-26** — Devansh Sharma, Faizul Rakib Sayem, Shahana Ibrahim — [LLM Hallucination Detection via Low-rank Multilinear Decomposition](http://arxiv.org/abs/2610.36191v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) frequently generate fluent yet factually incorrect responses, raising concerns about their reliability. Recent hallucination detectors increasingly exploit internal representations, but extracting informative signals from high-dimensional hidden states remains challenging. Existing approaches often rely on selected activations or pooling-based compression, potentially overlooking discriminative information distributed across Transformer layers, feature modes, and tok...
  </details>

- **2026-10-26** — Ruozhao Yang, Jiongchi Yu, Ming Hu et al. — [The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation](http://arxiv.org/abs/2610.35541v2)
  <details><summary>📄 Abstract</summary>
  Web services increasingly expose backend interfaces that let users delegate tasks to AI agents, which invoke service operations directly without navigating websites. This shift changes how existing Web vulnerabilities can be exploited. We investigate these changes through VELA, an executable benchmark covering 44 vulnerabilities across twelve Web application families. The benchmark preserves vulnerable backends and derives agent-facing interfaces from legitimate workflows. We evaluate three comm...
  </details>

- **2026-10-26** — Hicham El Akhal, Abderrahim Waga, Aissa Ben Yahya et al. — [Enhancing Deep Learning Model Performance through Data Generation Strategies: Classification of Olive Tree Diseases](http://arxiv.org/abs/2610.35984v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models are highly effective in a wide range of domains, particu larly in plant disease diagnosis. However, their performance is often limited by challenges such as insufficient data and class imbalance. In our work, we propose a comprehensive data generation strategy to overcome these limitations. First, we apply various data generation techniques, including traditional augmentation methods, CutMix, MixUp, and synthetic image generation using Deep Convolu tional Generative Adversar...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 63 papers

- **2026-10-27** — Yuelin Han — [The Envelope Layer: An Underestimated Surface of LLM Agent Defense](http://arxiv.org/abs/2610.37415v1)
  <details><summary>📄 Abstract</summary>
  Prior work framed the envelope layer as the channel through which malicious content enters an agent, and established it as a defense surface independent of the LLM layer and the agent layer; however, that work only tested the envelope layer briefly and did not examine how label strength, envelope authenticity, scaffold differences, or existing memories affect defense effectiveness. Following its GDA Measurement methodology and the A/B/C/D outcome taxonomy, this paper takes the A2A-TIBA attack as...
  </details>

- **2026-10-27** — Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz et al. — [TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](http://arxiv.org/abs/2610.37571v1)
  <details><summary>📄 Abstract</summary>
  Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which a...
  </details>

- **2026-10-27** — Avid Fayaz, Harry Zhang, Håvard Alstadheim et al. — [Test-Time Communication in Trading Agent Swarms](http://arxiv.org/abs/2610.37448v1)
  <details><summary>📄 Abstract</summary>
  Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent decision-makers rather than a team, for which convergence is a risk and not the goal. We ran 200 agents from four model families in groups of ten under five communication regimes, from isolation to message boards and share...
  </details>

- **2026-10-27** — Hayden Arnold — [Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE](http://arxiv.org/abs/2610.37397v1)
  <details><summary>📄 Abstract</summary>
  We describe the agent we submitted to the GLEE Competition, which plays bargaining, negotiation, and persuasion games against a shared pool of human and AI opponents. The agent is built around three central components: a classical game-theoretic solver to compute numeric moves, an online Bayesian layer to estimate opponent archetypes, and a language model to write accompanying messages. We utilize Rubinstein bargaining for bargaining, Faratin concession for negotiation, and Kamenica--Gentzkow di...
  </details>

- **2026-10-27** — Tianrong Zhang, Yakun Zhang, Dan Hao — [HIDE: Hierarchical Isolation via Documentation and Evidence for Rustc Bugs](http://arxiv.org/abs/2610.37343v1)
  <details><summary>📄 Abstract</summary>
  Rustc bugs can prevent valid programs from compiling or cause incorrect compilation results, making the identification of responsible source files essential for repair. Using large language models (LLMs) for rustc bug isolation raises three challenges. First, distributed compiler functionality requires understanding both what individual files do and how they work together. Second, a large source file search space makes exhaustive analysis of all files costly. Third, including documentation and s...
  </details>

- **2026-10-27** — Juyoung Seo, Geonwoo Bang, Dongho Kim et al. — [ReForest: Interpretability Meets Reasoning in Isolation Forest](http://arxiv.org/abs/2610.37316v1)
  <details><summary>📄 Abstract</summary>
  Statistical anomaly detection methods like Isolation Forest are efficient but suffer from a critical semantic gap. They identify numerical rarities but fail to understand the contextual meaning of data, often missing subtle, context-dependent anomalies. Conversely, Large Language Models possess strong semantic reasoning capabilities but are prohibitively expensive and slow for large-scale deployment. To bridge this gap, we propose ReForest, a novel framework that synergizes the statistical effic...
  </details>

- **2026-10-27** — Bilge Celik, Anna Vettoruzzo, Joaquin Vanschoren — [CaLLM: Continual Adaptation of LLMs via Non-Parametric Adapter Routing](http://arxiv.org/abs/2610.36994v1)
  <details><summary>📄 Abstract</summary>
  Continual adaptation of large language models (LLMs) to evolving task distributions while mitigating catastrophic forgetting remains an open problem. Existing strategies often struggle to scale or lack a robust mechanism for zero-shot task-to-expert assignment. We introduce CaLLM, a framework that resolves these tensions by combining metric-based meta-learning with modular parameter isolation via lightweight adapters. First, CaLLM projects each input batch into a task-agnostic embedding space to...
  </details>

- **2026-10-27** — Priyanka Goyal, Maitreyee Sar, Adway Mitra et al. — [Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability](http://arxiv.org/abs/2610.36857v1)
  <details><summary>📄 Abstract</summary>
  Earth Observation (EO)-based agricultural monitoring is shifting from pixel-level spectral analysis toward representation-driven modeling, yet systematic evaluation of learned representations across spatial, temporal, and domain-generalization dimensions remains limited. Geospatial foundation models generate high-dimensional embeddings encoding spatio-temporal land-surface properties, but their utility for agricultural applications remains insufficiently understood. This study presents a represe...
  </details>

- **2026-10-27** — Haocheng Mei, Yuchuan Tian, Ye Yuan et al. — [API-TAIL: Detecting Model Substitution in LLM APIs through Temperature-Aligned Likelihood Tails](http://arxiv.org/abs/2610.36801v1)
  <details><summary>📄 Abstract</summary>
  Commercial language model APIs return only text, allowing a provider to cut costs by quietly routing a fraction of user requests to a cheaper substitute model while billing for the advertised one. Detecting such partial substitution is challenging because honest providers also alter the output distribution through undocumented decoding and serving choices, such as temperature scaling, sampling truncation, repetition and presence penalties, and default system prompts, forcing an audit to test aga...
  </details>

- **2026-10-27** — Chi Wang, Min Gao, Yifei Zhang et al. — [Beyond the Evidence Coherence Trap: Agent-Driven Evidence Selection for Temporally Disordered Fake News Detection](http://arxiv.org/abs/2610.36764v1)
  <details><summary>📄 Abstract</summary>
  Fake news undermines public trust and the integrity of online information ecosystems. Temporally disordered fake news is especially elusive because it rearranges factual events into a false chronology. Individual events may remain factually valid even when their temporal relations are misrepresented. When similar events involving the same entity recur, retrieval may return semantically plausible evidence from the wrong period. Consequently, independent event verification may rely on locally cohe...
  </details>

- **2026-10-27** — Joosung Kim, Luyonghe Li, Shanwen Wu — [Peak-DNA: Recurrent Morphology in Global Narrative Propagation](http://arxiv.org/abs/2610.36571v1)
  <details><summary>📄 Abstract</summary>
  Global narrative streams exhibit noisy, fragmented, and asynchronous amplification bursts, making direct waveform comparison unreliable for recurrence analysis. This paper introduces Peak-DNA, a framework for identifying recurrent propagation morphology in global narrative streams. The proposed framework transforms hourly GDELT activity into normalized macro-peak episodes through denoising, macro-peak consolidation, and temporal alignment, and compares propagation morphology using DTW-based simi...
  </details>

- **2026-10-27** — Kai Qian, Dongjie Xu, Weijie Shi et al. — [Decoupling Consistency and Conflict across MLLM Layers for Fake News Detection](http://arxiv.org/abs/2610.36569v1)
  <details><summary>📄 Abstract</summary>
  The trustworthiness of Web content faces a growing threat from multimodal fake news. Real news usually shows aligned image-text semantics, while fake news often contains a few conflicts at varying levels, such as mismatches in objects, scenes, events, and claims. However, existing methods usually treat consistency and conflict in a coarse and static way, limiting their ability to capture sparse conflicts and adapt to varying conflict levels. Inspired by the distinct knowledge encoded across laye...
  </details>

- **2026-10-27** — Nardine Basta, Venus Haghighi, Dali Kaafar et al. — [Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure](http://arxiv.org/abs/2610.36453v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users, yet it remains unclear whether they distinguish correction from manipulation or merely differ in their propensity to concede. We examine this question across seven LLMs from four vendors in two studies, one on the answer...
  </details>

- **2026-10-27** — Fangran Miao, Shengjie Niu, Jian Huang et al. — [Is Your LLM Relay Serving What It Claims? A low-cost and high-power test for LLM Relay Auditing](http://arxiv.org/abs/2610.37086v1)
  <details><summary>📄 Abstract</summary>
  Relay and reseller APIs have become a common way to access large language models (LLMs), yet users cannot directly verify whether they receive the models they request and pay for. This opacity motivates LLM relay auditing, but existing methods struggle to combine low cost, robustness to benign deployment changes, and statistically interpretable decisions under black-box access. To address these limitations, we propose distributional fingerprint auditing (DFA), a statistical method that requires ...
  </details>

- **2026-10-27** — L. E. Rodríguez, M. Cruces, G. Voisin et al. — [Self lensing in BH-NS binaries as progenitors for periodically repeating Fast Radio Bursts](http://arxiv.org/abs/2610.37052v1)
  <details><summary>📄 Abstract</summary>
  Fast radio bursts (FRBs) are bright extragalactic transients whose origin remains uncertain. The discovery of repeating FRBs, some with cyclic activity windows, opens new prospects for testing their progenitors. Neutron stars (NSs) are strong candidates, as they naturally emit radio pulses with temporal and spectral properties resembling those of FRBs, an interpretation reinforced by the detection of an FRB-like burst from the Galactic magnetar SGR 1935+2154. Nevertheless, the pulse energy of ty...
  </details>

- **2026-10-27** — Zhangkai Wu, Xu Zhang, Zhihong Cui et al. — [Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift](http://arxiv.org/abs/2610.36585v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) are being applied to Web data streams such as network intrusion detection, where they adapt by updating the labelled rows of their context without retraining. When a past concept returns after leaving the context, a TFM faces a recall-or-relearn decision between restoring stored rows of the concept and relearning it from new labels. We propose MICE (Mixture of In-Context Experts), a training-free learner that cuts the stream into segments at detected changes. It ...
  </details>

- **2026-10-27** — Peiwang Tang, Cheng HE, Yupeng Ye et al. — [Learning from Points and Patches: A Pre-trained Hybrid Attention Transformer for Time Series Analysis](http://arxiv.org/abs/2610.36572v1)
  <details><summary>📄 Abstract</summary>
  Time-series data generated by Web services and connected systems support applications such as user activity analysis, service monitoring, and resource management. However, learning transferable representations from heterogeneous time series remains challenging due to diverse temporal patterns, variable sequence lengths, and limited high-quality annotations. Despite the success of pre-training in natural language processing and computer vision, effective time-series pre-training requires strategi...
  </details>

- **2026-10-26** — Leo Benaharon, Chi Zhang, Wei Zheng et al. — [Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security](http://arxiv.org/abs/2610.36143v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can adapt robotic software by revising executable programs, but successful responses to an evolving opponent may not remain effective. We present a framework for program-level adversarial co-adaptive self-play in which coding agents generate attacks and defenses from tested opponent code and mission feedback, without model fine-tuning. Environment-specific interfaces support external programs for autonomous driving and SDK-level defenses for humanoid locomotion. Two eight-generatio...
  </details>

- **2026-10-26** — Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al. — [I-HITL: Inalienable Human-in-the-Loop](http://arxiv.org/abs/2610.35835v2)
  <details><summary>📄 Abstract</summary>
  Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the concept of inalienable human-in-the-loop (I-HITL). An I-HITL protocol ensures that an agent can initiate an action only with explicit human approval, even when the human interacts with a system (e.g., a local agentic harne...
  </details>

- **2026-10-26** — George Juraj Salapa — [kw-bench: Breaking Frontier Harnesses on Real-World Tasks](http://arxiv.org/abs/2610.36405v1)
  <details><summary>📄 Abstract</summary>
  Each new generation of frontier model pushes the edge of what is possible. Inside a harness -- a loop, a shell, a filesystem, the ability to write and run its own code -- a model can take on increasingly difficult work.   A growing body of work treats the coding-agent harness as infrastructure for knowledge work rather than a coding tool, and a new wave of benchmarks tests it there. Most of them are generative: build a financial model, a memo, a spreadsheet from a brief, judged by a rubric or by...
  </details>

- **2026-10-26** — Ritika Poddar, Aidan Fennelly, Deirdre Murphy et al. — [BUSTA: Teaching Small Language Models to Reason About Binary Execution](http://arxiv.org/abs/2610.36288v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLM) are increasingly applied to Reverse Engineering (RE) workflows. RE, however, differs from common LLM coding tasks as it requires models to reason about low-level program behavior. Furthermore, the deployment of tooling in resource-constrained sandboxed RE environments limits the ability to use frontier-scale solutions. We examine whether a targeted LLM training approach can transfer distinct RE skills to open models via inverse basic-block execution: given an x86-64 b...
  </details>

- **2026-10-26** — Jannatul Shefa, Alejandro Salado, Paul Wach et al. — [MARQ: A Modular, LLM-Agnostic Requirement Quality Assessor Infused with Systems Engineering Knowledge](http://arxiv.org/abs/2610.36234v1)
  <details><summary>📄 Abstract</summary>
  Requirements engineering (RE) is foundational to systems engineering (SE), as requirement defects can propagate downstream and adversely affect development outcomes. Although large language models (LLMs) are promising for requirement quality assessment, prior work shows that off-the-shelf models miss a large share of expert-identified defects, perform unevenly across quality criteria, and vary across executions. This study investigates whether infusing expert-derived SE knowledge can improve LLM...
  </details>

- **2026-10-26** — Glenn J. White — [ASTRA: An Autonomous Framework for Physics-Validated Analysis and Hypothesis Generation in Astrophysics](http://arxiv.org/abs/2610.36144v1)
  <details><summary>📄 Abstract</summary>
  We present ASTRA, an autonomous framework for physics-validated analysis and hypothesis generation in astrophysics without per-step human intervention. It integrates dimensional analysis, structural causal models, Bayesian evidence computation, and multi-wavelength data fusion in a single automated workflow. Five test cases on real observational data recover known results: Herschel filament scaling, Chandra Deep Field South cross-matching, SDSS galaxy correlations, Gaia causal inference, and Bay...
  </details>

- **2026-10-26** — Giorgos Iacovides, Oliver Hannibal, Wuyang Zhou et al. — [FinLLM-KG: Knowledge Graph-Enhanced LLMs for Financial Sentiment Analysis in Algorithmic Trading](http://arxiv.org/abs/2610.36083v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs). However, existing approaches remain confined to predicting the sentiment of each article in isolation and operate as black boxes, which limits contextual understanding and hinders deployment in high-stakes financial decision-making. To this end, we introduce FinLLM-KG, a model-agnostic framework that combines causal LLMs with a financial knowledge...
  </details>

- **2026-10-26** — Muxi Diao, Wenbin Xu, Lele Yang et al. — [VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](http://arxiv.org/abs/2610.35864v2)
  <details><summary>📄 Abstract</summary>
  Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a rule-consistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained tasks in English and Chinese span 12 categories, from data stories and music-drive...
  </details>

- **2026-10-26** — Alexander Kovalenko, Artem Redchych — [Small agents should know what their tools do](http://arxiv.org/abs/2610.35981v1)
  <details><summary>📄 Abstract</summary>
  Small open language models can call tools, but they do not reason about what a call does: they delete without asking, repeat writes, re-read state they already hold, and issue one call per turn where a short program would do. We introduce EffectWorld, an executable world of effect-typed tools in which every tool declares its effect, whether it is idempotent, and which resources it reads and writes. These declarations let a replay verifier decide whether a trace is effect-safe without labels or j...
  </details>

- **2026-10-26** — Tiejin Chen, Xiaoou Liu, Michael Clifford et al. — [Detect Before You Disambiguate: Perturbation-Based Input Ambiguity Detection in LLMs](http://arxiv.org/abs/2610.36353v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often answer ambiguous inputs as if they had a single intended meaning. This is problematic because input ambiguity is an upstream source of uncertainty: when a prompt admits multiple valid interpretations, the key question is whether the model should answer directly at all. Existing input uncertainty methods often rely on LLM-generated statements or clarifications, but such transformations may already disambiguate the input before the ambiguity is measured. We propo...
  </details>

- **2026-10-26** — Kosei Horikawa, Hao Li, Yutaro Kashiwa et al. — [Agent or Human? Detecting Commits by AI Coding Agents in the Absence of Authorship Signatures](http://arxiv.org/abs/2610.36229v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents such as Claude Code, GitHub Copilot coding agent, and Cursor now commit directly to open-source repositories. Empirical studies of these agents identify their commits through authorship signatures, such as bot accounts and Co-authored-by trailers. These signatures are optional, can be removed, and are often attached to pull requests rather than to individual commits. Hence, it is unclear whether Agent commits can be told apart from Human commits once the signatures are gone. We ...
  </details>

- **2026-10-26** — Tony Chae, Kleanthis Avramidis, Dimitra Emmanouilidou et al. — [MtReNIRS: A Self-Supervised Foundation Model for Transferable Neurovascular Representations](http://arxiv.org/abs/2610.36159v1)
  <details><summary>📄 Abstract</summary>
  Functional near-infrared spectroscopy (fNIRS) offers a promising approach for monitoring the hemodynamic correlates of neural activity in naturalistic settings. However, existing modeling methods for fNIRS are largely confined to small-scale, single-session data with low sampling rates, driven by high heterogeneity in acquisition devices and optode montages. In addition, the complex spatiotemporal structure of fNIRS signals further restricts model scalability and transferability across settings....
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 59 papers

- **2026-10-27** — Hee Seung Hwang, Sanghyuk Chun, Xindi Wu et al. — [Multi-State Linear Attention with Generalized Second-Order Routing](http://arxiv.org/abs/2610.37645v1)
  <details><summary>📄 Abstract</summary>
  Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state using only the mean alignment between a query and each segment's keys, ignoring h...
  </details>

- **2026-10-27** — Raban Emunds, Jannis Blüml, Quentin Delfosse et al. — [Interpretable Meta-Policies for Neural Decision Making](http://arxiv.org/abs/2610.37451v1)
  <details><summary>📄 Abstract</summary>
  Deep Reinforcement Learning remains difficult to interpret and align due to the black-box nature of neural networks. While (neuro-)symbolic approaches improve transparency by incorporating symbolic reasoning, applying them directly to low-level actions results in overly complex, unreadable policies. We introduce NEXUS, a hierarchical RL framework that resolves this tension by combining neural skills with symbolic meta-policies. By shifting transparent reasoning to high-level skills rather than a...
  </details>

- **2026-10-27** — Ananth K Suresh, Aveen Dayal, Gouthaman KV et al. — [When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models](http://arxiv.org/abs/2610.37430v1)
  <details><summary>📄 Abstract</summary>
  For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or without identifying the missing evidence. We study how refusal on visually unanswerable questions is shaped by three sources of control: inference-time instructions, post-training, and inte...
  </details>

- **2026-10-27** — Haokun Wen, Xuemeng Song, Mong-Li Lee et al. — [Same Verdict, Different Readers: Personalizing Fact-Checking Explanations from Relative Preferences](http://arxiv.org/abs/2610.37380v1)
  <details><summary>📄 Abstract</summary>
  Fact-checking explanations help Web users understand why a claim receives its verdict, yet the same explanation may not satisfy readers with different backgrounds and preferences. We formulate Faithful Personalized Fact-Checking Explanation Rewriting, which adapts an existing explanation to individual readers while preserving factual fidelity. Rather than relying on reader-written reference explanations, we learn personalized rewriting from the relative preferences of LLM-simulated readers. Howe...
  </details>

- **2026-10-27** — Andrea Marino, Giovanni Sileno, Thomas van Binsbergen et al. — [Aligning Institutional Power and Operational Ability](http://arxiv.org/abs/2610.37342v1)
  <details><summary>📄 Abstract</summary>
  To be socially sustainable, Agentic AI systems require normative designs that align responsibilities with the ability to fulfil them. Identifying incongruences such as unsatisfiable expectations or privilege escalation is crucial in avoiding normative pitfalls. In this study, we discuss design dimensions suitable for describing multi-agent systems in light of this norm-ability alignment requirement. We propose a formal framework centred on process-oriented modelling and institutional power for t...
  </details>

- **2026-10-27** — Nicolas Tacheny, Tom Mens, Saïd Mahmoudi — [Mind the Intent Gap: A Methodology for Collaborative Agent-Driven Software Engineering](http://arxiv.org/abs/2610.37340v1)
  <details><summary>📄 Abstract</summary>
  AI agents have entered software teams, first as tools and now as team members. They produce in minutes what used to take days, yet the expected gain in delivery often fails to appear. We argue that they are entering processes designed for people, which quietly relied on people to cover three of their weaknesses. The team's intent was never fully written down, because colleagues filled the gaps. An AI agent fills them too, though by guessing, and drifts from what the team had in mind. The reasoni...
  </details>

- **2026-10-27** — Yu Zhang, Xiaogang Wang, Yuhang Cheng et al. — [Zhengrong-Spatial-Aware 1.0: Advancing 3D Multimodal Intelligence](http://arxiv.org/abs/2610.37216v1)
  <details><summary>📄 Abstract</summary>
  This report presents the implementation and validation of two end-to-end multimodal adaptation pipelines for 3D-aware visual question answering on a custom spatial dataset. The first pipeline fine-tunes HiSpatial-3B, which augments RGB observations with metric-scale 3D point maps; the second adapts Qwen3-VL through memory-efficient QLoRA-based supervised fine-tuning. The completed engineering stack covers dataset conversion, image-annotation alignment, monocular geometry preprocessing, instructi...
  </details>

- **2026-10-27** — Kensuke Sasaki, Issei Sato — [On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime](http://arxiv.org/abs/2610.37085v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences. Recent empirical work has revealed that DPO induces remarkably sparse parameter updates, yet no theoretical explanation for this phenomenon has been offered. We analyze DPO's optimization dynamics under a neural tangent kernel linearization and show that the logistic structure of the DPO loss gives rise to an implicit maximum-margin bias. Building on this observation, we introduce th...
  </details>

- **2026-10-27** — Kegeng Tang, Jingbo Wang, Yangming Zhang et al. — [Latent Visual Contrastive Reasoning with Multi-Branch Exploration](http://arxiv.org/abs/2610.36809v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have made substantial progress in visual question answering, but complex visual reasoning often requires locating and comparing multiple pieces of question-relevant visual evidence. Existing methods that move intermediate reasoning into the visual latent space usually follow a single linear reasoning trajectory, which can be limiting when multiple visual hypotheses or competing evidence regions are relevant. We propose Latent Visual Contrastive Reasoning, a branc...
  </details>

- **2026-10-27** — Wu Lin, Yan Fan, Chenxiang Ma et al. — [Nonlinear Direct Feedback Alignment for Scalable Backpropagation-Free Training](http://arxiv.org/abs/2610.36718v1)
  <details><summary>📄 Abstract</summary>
  Backpropagation (BP) remains the predominant algorithm for training deep neural networks, but it is biologically implausible and suffers from the backward locking problem, constraining parallelization across layers. Direct Feedback Alignment~(DFA), which propagates the global output error directly to each hidden layer via fixed feedback matrices, has emerged as a promising alternative for addressing these limitations. However, a significant performance gap persists between DFA and BP, which we a...
  </details>

- **2026-10-27** — Tomoyasu Shimada, Kazuhiko Murasaki, Shoichiro Takeda et al. — [SAGE: Semantic-Augmented Geometric Experts for Point Cloud Registration](http://arxiv.org/abs/2610.36658v1)
  <details><summary>📄 Abstract</summary>
  Point cloud registration is an essential task for scene reconstruction, requiring the alignment of partially overlapping point clouds. Under low-overlap conditions, this task remains challenging because existing geometry-only methods cannot distinguish geometrically similar but semantically distinct structures (e.g., TV corners vs. desk corners and chair legs vs. table legs), resulting in incorrect correspondences. To address this geometric ambiguity, we present Semantic-Augmented Geometric Expe...
  </details>

- **2026-10-27** — Binhang Qi, Yiming Liu, Yun Lin et al. — [Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](http://arxiv.org/abs/2610.36584v1)
  <details><summary>📄 Abstract</summary>
  As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents can generate tests that validate the required behavior when the implementation of that behavior is withheld. Existing test-generation benchmarks mostly focus on white-box testing, whereas the requirement--test-related st...
  </details>

- **2026-10-27** — Vansh Bhatia, Mehdi Rezagholizadeh, Parsa Ashrafi Fashi et al. — [PRISM-BENCH: Diagnosing Grounded and Faithful Multimodal Reasoning Beyond Final-Answer Accuracy](http://arxiv.org/abs/2610.36554v1)
  <details><summary>📄 Abstract</summary>
  Final-answer accuracy reports whether a vision-language model was right, but not whether its answer was grounded in the image, whether its stated reasoning reflects that evidence, or what the answer cost to produce. Those are the properties that decide whether a system can be deployed. We present PRISM-BENCH, a benchmark of 1,000 expert-curated questions spanning five under-represented reasoning categories, in which every item carries an idealized reasoning trace written by one human annotator a...
  </details>

- **2026-10-27** — Yashuo Luo, Qianren Mao, Ziqi Qin et al. — [From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation](http://arxiv.org/abs/2610.36445v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation from large reasoning models (LRMs) often uses raw teacher trajectories as supervision. However, this practice creates a mismatch between the goal of distillation and the nature of teacher trajectories. Advanced LRMs typically improve their reasoning capabilities through reward-driven post-training, such as RLHF. This training optimizes them as strong solvers, rather than as teachers that produce reasoning processes smaller models can easily learn. Since smaller models have...
  </details>

- **2026-10-27** — Xianxiang Zhao, Advik Mehta, Falak Sethi et al. — [LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction](http://arxiv.org/abs/2610.36433v1)
  <details><summary>📄 Abstract</summary>
  Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inconsistent quality, with 25% of crews never conducting pretask planning (Olson et al., 2016), diverting safety personnel from field supervision. This study proposes the Lightweight Multi-Agent DSB System (LM-DSB), which i...
  </details>

- **2026-10-27** — Giuseppe Curci, Stefano Simonazzi, Andrea Molinari et al. — [Exploring the Limits of the Delta Learning Hypothesis: Single-Pair Generator Biases in Direct Preference Optimization](http://arxiv.org/abs/2610.37058v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) typically relies on preference pairs generated from diverse model pools and ranked by an external LLM judge. The recently proposed delta-learning hypothesis suggests that comparable supervision can instead be obtained from a single pair of models by treating the larger model's response as preferred. We investigate the limits of this approach across model families and scales. We show, both theoretically and empirically, that fixed model pairs introduce systema...
  </details>

- **2026-10-26** — Bingliang Zhang, Wenda Chu, Yizhuo Li et al. — [SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model](http://arxiv.org/abs/2610.36419v1)
  <details><summary>📄 Abstract</summary>
  We present Scalable Pixel-anchored End-to-end Diffusion (SpeeDiff), a latent diffusion method that jointly trains the VAE and the diffusion model from scratch. In principle, joint training allows the diffusion loss gradient to directly guide the VAE encoder, encouraging the formation of a generation-friendly latent space and potentially yielding faster convergence than the conventional two-stage approach with a pretrained frozen VAE. However, a naive end-to-end implementation severely degrades p...
  </details>

- **2026-10-26** — Reza Yousefi Maragheh, Jayesh Uddhav Kudase, Aysenur Inan et al. — [MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation Explanations](http://arxiv.org/abs/2610.36389v1)
  <details><summary>📄 Abstract</summary>
  Evaluating natural language explanations in recommender systems is essential for fostering user trust, transparency, and engagement. However, existing evaluation approaches like human evaluations, while accurate, are resource-intensive and impractical at the scale required by modern recommendation platforms. Also, automated methods using single-agent LLMs suffer from prompt sensitivity and inconsistent outputs. To address these challenges, we propose MAREval, a structured multi-agent framework f...
  </details>

- **2026-10-26** — Fanqi Yu, Matteo Tiezzi, Cigdem Beyan et al. — [HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](http://arxiv.org/abs/2610.36374v1)
  <details><summary>📄 Abstract</summary>
  Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates can progressively distort the representation space, making expert-based approaches particularly sensitive to routing interference, causing expert selection to degrade over time. We propose HIDRA, a structured routing fra...
  </details>

- **2026-10-26** — Ziqiao Wang, Yang You — [Beyond the Estimate: Wiener-Informed Decoding for Easier Training of Pixel-Space Flow Models](http://arxiv.org/abs/2610.36192v1)
  <details><summary>📄 Abstract</summary>
  Learning velocity fields directly in pixel space is difficult and slow. We show that coarse second-order image statistics can ease this task: frozen Wiener estimates improve velocity learning, with gains extending beyond the linear predictions they explicitly provide. Moreover, we observe similar but complementary gains from frozen bases and pixel decoding. These observations motivate Wiener-informed Decoding (WiD), which uses statistical knowledge both for direct prediction and to organize deco...
  </details>

- **2026-10-26** — Davide Cuttini, Diego Di Tommaso, Alessio Antoniacomi et al. — [Metric Scale for Insta360 Structure-from-Motion from the Camera's Embedded IMU](http://arxiv.org/abs/2610.35554v2)
  <details><summary>📄 Abstract</summary>
  Structure-from-motion (SfM) from the dual-fisheye video of a consumer 360-degree camera recovers geometry only up to a similarity transform; in the pipeline considered here, metric scale is obtained from smartphone ARKit or ARCore poses captured alongside the camera. This paper evaluates a self-contained alternative: the IMU embedded in the Insta360 X5 and X6, recorded at 1 kHz. The sensor is characterised (noise density, camera-IMU synchronisation, accelerometer scale factor, bias stability), t...
  </details>

- **2026-10-26** — Blessing Ngozi Uzor, Valdini Douglace Lemofouet, Paula Chikaodinaka Anyanwu et al. — [Do Language Models Understand Igbo Culture? Beyond Multiple Choice](http://arxiv.org/abs/2610.35168v2)
  <details><summary>📄 Abstract</summary>
  The value of language models for any community depends on whether a model actually understands the culture of the people it intends to serve. We use the Igbo language as a case study. Existing benchmarks test translated Western ideas, lacking depth. To address this, we introduce CAB-Igbo, a benchmark developed from indigenous cultural sources and verified by native speakers across six domains. We evaluated diverse models under varying conditions, incorporating regional personas. Performance was ...
  </details>

- **2026-10-26** — Gunhee Cho, Hongyeob Kim, Yun-Gyung Cheong — [FATE-5: Faithful Alignment of Trait Expression for Continuous Big Five Personality Control](http://arxiv.org/abs/2610.34889v2)
  <details><summary>📄 Abstract</summary>
  Controlling personality in large language models is important for building conversational agents that can be customized to different users and interaction settings. However, existing personality control methods often face a tradeoff between strong trait expression and natural dialogue generation. We introduce FATE-5, Faithful Alignment of Trait Expression for the Big Five, a two-stage framework that separates personality encoding from naturalness alignment. FATE-5 first learns continuous soft pr...
  </details>

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

- **2026-10-25** — Xiangfei Sheng, Xiaofeng Pan, Leida Li et al. — [CropReward: A Human-Preference Benchmark and Reward Model for Aesthetic Image Cropping](http://arxiv.org/abs/2610.34221v2)
  <details><summary>📄 Abstract</summary>
  Aesthetic image cropping (AIC) aims to improve image composition and aesthetic quality by removing extraneous or distracting content. Over the past decade, AIC methods have evolved from specialized vision models to multimodal large language models(MLLMs). Reliable evaluation that reflects human preferences is essential for benchmarking AIC methods and guiding model optimization. However, the current AIC evaluation relies largely on geometry-based metrics such as intersection over union (IoU), as...
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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 55 papers

- **2026-10-27** — George Christodoulou, Vasilis Christoforidis, Alkmini Sgouritsa et al. — [Learning-Augmented Coordination Mechanisms](http://arxiv.org/abs/2610.36508v1)
  <details><summary>📄 Abstract</summary>
  The inefficiency of decentralized resource allocation is classically measured by the Price of Anarchy (PoA) and the Price of Stability (PoS). The most widely studied and foundational class of these models are atomic and non-atomic congestion games, for which a robust theory quantifying the inefficiency of equilibria is well-established. To mitigate the effects of selfish behavior, we employ Coordination Mechanisms, which modify resource costs to incentivize socially improved equilibria. However,...
  </details>

- **2026-10-27** — Pavankumar Koratikere, Abhijnan Dikshit, Leifur Leifsson — [High-Fidelity Aerostructural Dataset of Transonic Wings in Cruise Conditions](http://arxiv.org/abs/2610.36442v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in machine learning (ML) have the potential to substantially accelerate aircraft wing design, a process that has traditionally required extensive high-fidelity simulation and design iteration. Existing public datasets for ML-based wing design have focused primarily on aerodynamic performance, with limited consideration of the multidisciplinary interactions that govern practical aircraft design. In particular, efficient wing design requires simultaneous consideration of aerodynami...
  </details>

- **2026-10-27** — Bojun Zou, Wenhao Yu, Jiaohao Li et al. — [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning](http://arxiv.org/abs/2610.37378v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a straightforward solution, but collecting such data is costly, especially for dynamic scenarios, and may degrade their original task capabilities. To address these limitations, we pro...
  </details>

- **2026-10-27** — Preethi S, Meeradevi T, Arun Prakash A — [uTHCD-C: A Corruption-Robustness Benchmark for Tamil Handwritten Character Recognition](http://arxiv.org/abs/2610.36850v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of Tamil handwritten character recognition (HCR) has largely focused on clean test images, and a standardized multi-corruption robustness benchmark for isolated Tamil HCR has not been established. We introduce uTHCD-C, a corruption-robustness benchmark based on the unconstrained Tamil Handwritten Character Database (uTHCD). The benchmark defines ten corruption types, including a handwriting-specific stroke-thinning corruption, at five severity levels. We evaluate nine convolutional an...
  </details>

- **2026-10-27** — Jiameng Bai, Zhitao Wang, Long Wang et al. — [From Ripple to Boundary: Deterministic Impact Boundaries for LLM-Based Software Evolution](http://arxiv.org/abs/2610.36549v1)
  <details><summary>📄 Abstract</summary>
  The landscape of software evolution is undergoing a fundamental paradigm shift in the era of Large Language Models. As industrial software engineering increasingly transitions toward design-driven code generation, the bottleneck of evolution has shifted from writing code to maintaining deterministic consistency between multi-source design assets and the generated code. When a design asset changes, LLM agents currently lack a deterministic impact boundary to identify which code must be evolved, l...
  </details>

- **2026-10-27** — Sirui Chen, Yunzhe Qi, Haobo Xu et al. — [Proposing Better Rollouts for On-Policy Distillation](http://arxiv.org/abs/2610.36477v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) improves language-model post-training by letting the student learn from its own sampled trajectories under teacher supervision, aligning the training process with inference-time behavior. However, the rollout policy in OPD is usually treated as fixed: each round samples directly from the current student. We show that this choice can create a compounding teacher--student mismatch, because it requires the teacher to provide effective supervision on whichever trajectori...
  </details>

- **2026-10-27** — S M Abdulla Al Mamun, Akif Islam, Mohd. Ruhul Ameen — [Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance](http://arxiv.org/abs/2610.36947v1)
  <details><summary>📄 Abstract</summary>
  Can additional specialist language-model contexts improve software assurance when deterministic tool evidence is already available? We study this question through five experiments spanning authored Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-COMP assertion verdicts, and deliberately misleading evidence packages. The evaluated systems use Qwen2.5-Coder-7B-Instruct, with a 1.5B sensitivity analysis, and complete 13,638 model requests. On eight related developme...
  </details>

- **2026-10-27** — Xu Hu, Changjie Wu, Linzhe Shi et al. — [Trace-WAM: Learning to Act via 3D Motion Prediction for World Action Models](http://arxiv.org/abs/2610.36840v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) learn representations for robot control by coupling future visual prediction with action generation. Successful manipulation depends primarily on how the robot and task-relevant objects evolve, whereas future-video prediction must also reconstruct the appearance and background of the entire scene. We therefore propose Trace-WAM, which augments video-action learning with future 3D motion prediction as an auxiliary objective. This objective supervises temporal point corr...
  </details>

- **2026-10-27** — Chang Su, Bin Wu, Emine Yilmaz et al. — [What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](http://arxiv.org/abs/2610.37631v1)
  <details><summary>📄 Abstract</summary>
  Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses remains unclear. Recent point-in-time models trained on web snapshots from different years provide a way to probe how knowledge prevalence varies over time. Using these models, we propose a temporal variability score (TVS), defined as the coefficient of variation of an item's negative log-likelihood ...
  </details>

- **2026-10-27** — Simon Bultmann, Daniele Cattaneo, Abhinav Valada — [Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences](http://arxiv.org/abs/2610.37350v1)
  <details><summary>📄 Abstract</summary>
  Accurate camera-LiDAR calibration is an essential prerequisite for robust multi-modal perception in robotics. Recent target-less methods based on learned pixel-point correspondences achieve high extrinsic calibration accuracy and generalize across environments. However, they operate on rectified images with known camera intrinsics, restricting their applicability to systems whose cameras have already been individually calibrated. We present a fully automatic, target-less framework that jointly e...
  </details>

- **2026-10-27** — Wenjie Qiu, Hepei Li, Jianfeng Wang et al. — [WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](http://arxiv.org/abs/2610.37329v1)
  <details><summary>📄 Abstract</summary>
  Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limitations, leaving the question of "when to use CC" unresolved. We address this gap with WCC, a novel learning-based framework that dynamically decides when to deploy CC in LSGO. WCC employs a streamlined design for efficie...
  </details>

- **2026-10-27** — Rafael Munoz-Salinas, Francisco J. Romero-Ramirez, Manuel J. Marin-Jimenez — [TRUCO: A Scalable Lock-Free Algorithm for Parallel Contour Extraction](http://arxiv.org/abs/2610.37297v1)
  <details><summary>📄 Abstract</summary>
  Transforming binary masks into geometric contours remains a critical step in many computer vision pipelines, particularly for post-processing high-resolution segmentation outputs. Yet, standard algorithms such as the Suzuki-Abe method are limited by their sequential nature and the overhead of building topological hierarchies. As modern applications transition to high-resolution imaging, there is a critical need for contour extraction that leverages multi-core CPU architectures without the comple...
  </details>

- **2026-10-27** — Šimon Soldát, Václav Šmídl — [Bayesian Inference of Expensive Simulators: Survey and Comparison of Design Choices](http://arxiv.org/abs/2610.37284v1)
  <details><summary>📄 Abstract</summary>
  We present a survey of approaches to Bayesian inference with simulator forward models, focusing on settings with prohibitively expensive simulators. In this domain, Bayesian optimization-based methods have emerged as the most promising approach. We unify existing methods into a general framework, enabling consistent reasoning about shared algorithmic structure across the fragmented literature. Within this framework, we identify the primary design choices and perform a systematic empirical compar...
  </details>

- **2026-10-27** — Nabeelah Faumi, Deshan Sumanathilaka — [Mechanistic Failure Modes of Weight Pruning in Transformer Language Models](http://arxiv.org/abs/2610.37126v1)
  <details><summary>📄 Abstract</summary>
  Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation. We test this assumption with a factorial pruning study on GPT-2, crossing two importance criteria (magnitude, random), two component types (attention heads, MLP neurons) and three sparsity levels (3%, 50%, 70%). Using the fully characterised indirect object identification (IOI) circuit as ground truth, we measure circuit integrity wit...
  </details>

- **2026-10-27** — Sølve Langseth, Kristoffer Herland Hellton, Hugo L. Hammer — [LLM knowledge for improved Out-of-Distribution Tabular Prediction - A Cross-Validated Regularisation Approach](http://arxiv.org/abs/2610.36806v1)
  <details><summary>📄 Abstract</summary>
  Prediction models degrade when the deployment population differs from the one used to train them, and training data cannot say which feature-response relationships will transfer. Expert elicitation is slow and unscalable. We ask whether coefficient priors elicited from large language models (LLMs) improve out-of-distribution (OOD) prediction as the shrinkage target of a regularised regression instead of zero, across five tabular datasets split on real covariates, selecting providers and prior st...
  </details>

- **2026-10-27** — Jia Gu, Liang Pang, Huawei Shen — [Robust LLM Data Selection via Content-Invariant Gradient Attribution](http://arxiv.org/abs/2610.36755v1)
  <details><summary>📄 Abstract</summary>
  Gradient-based data attribution has become an important tool for high-quality data selection in the instruction fine-tuning of large language models (LLMs), as it estimates the contribution of training examples through their influence on model optimization. However, we find that existing global gradient attribution methods suffer from surface-form bias: minor changes to semantically irrelevant details, such as wording or formatting, can produce highly inconsistent attribution scores even when th...
  </details>

- **2026-10-26** — Matea Tashkovska, Naël Ouerghemi, Haozhe Qi et al. — [SOMA: A Benchmark for Fine-Grained Egocentric Behavior and Body-Motion Understanding](http://arxiv.org/abs/2610.36384v1)
  <details><summary>📄 Abstract</summary>
  Perceiving human body motion is critical for multimodal systems that understand and assist people. Yet current evaluations of Multimodal Large Language Models (MLLMs) largely focus on objects, scenes, and coarse actions, leaving their ability to reason about the body itself poorly assessed. This is especially challenging from the egocentric perspective, in which the body is only partially visible and motion must be inferred from occluded and temporally distributed cues. We introduce SOMA, a benc...
  </details>

- **2026-10-26** —  Xiaomi Embodied Intelligence Team, Yuechen Luo, Chong He et al. — [OmniBrain-0: A Unified Agentic Model for Embodied Intelligence](http://arxiv.org/abs/2610.36013v1)
  <details><summary>📄 Abstract</summary>
  General-purpose embodied intelligence requires robots to coordinate diverse skills over long horizons, track task progress, and recover from failures. Specialist policies alone do not ensure task-level reliability, while powerful multimodal agents rely on costly reasoning and external experience that compact models struggle to reproduce. We introduce OmniBrain-0, a lightweight unified embodied agent that coordinates manipulation and navigation through a shared high-level decision model, integrat...
  </details>

- **2026-10-26** — Pir Bakhsh Khokhar, Carmine Gravino, Fabio Palomba — [Reliability-Aware Short-Term Glycemic Risk Prediction Using an Anchor-Based Comparative Framework of Sequence, Multimodal, and State-Updating Digital-Twin Models](http://arxiv.org/abs/2610.36363v1)
  <details><summary>📄 Abstract</summary>
  Anticipating short-term hypoglycemic and hyperglycemic risk is essential for proactive diabetes management. However, existing machine learning approaches often use inconsistent evaluation protocols and emphasize predictive performance over reliability. This study introduces an anchor-based benchmarking framework integrating longitudinal glucose sequences and multimodal patient information. Using the T1DiabetesGranada dataset, 5,503,441 standardized prediction anchors were constructed from 736 in...
  </details>

- **2026-10-26** — Roxana Ramona Szomiu, George Ursu, Adrian Groza — [Ontology-guided multi-agent reasoning for explainable differential diagnosis](http://arxiv.org/abs/2610.36325v1)
  <details><summary>📄 Abstract</summary>
  Effective differential diagnosis depends on well structured and unambiguous patient case descriptions, since incomplete or ambiguous clinical information readily leads to diagnostic errors and inconsistent reasoning. Large Language Models (LLMs) have recently shown promising capabilities in medical question answering and clinical reasoning; however, even when achieving competitive performance on medical benchmarks, they often rely on pattern recognition learned from training data rather than gro...
  </details>

- **2026-10-26** — Sami Nur Islam, Johan Obando-Ceron, Doina Precup et al. — [Freeze, Don't Clone: Fine-Tuning with Expressive Policies Without Retaining Offline Data](http://arxiv.org/abs/2610.36247v1)
  <details><summary>📄 Abstract</summary>
  Offline-to-online reinforcement learning uses offline pretraining to accelerate subsequent online learning. While many methods assume the offline dataset remains available throughout fine-tuning, there are many settings where this is not the case. Prior work attributes failures in this setting primarily to critic recalibration under distribution shift. We identify a complementary actor-side failure: once the offline data disappears, continued behavioral cloning (BC) no longer preserves the offli...
  </details>

- **2026-10-26** — Xusheng Liang, Jianqiao Sun, Hao Zhang et al. — [Diagnosing and Correcting Bias in MLLM for Long Video Understanding](http://arxiv.org/abs/2610.36210v1)
  <details><summary>📄 Abstract</summary>
  Long-video question answering is challenging since the answer often hinges on a few decisive moments scattered throughout the video, while memory constraints force Multimodal Large Language Models (MLLMs) to sample frames at extremely low rates, resulting in sparsity that risks omitting key evidence. Though aggressively enlarging the context size is intuitive, we argue that performance remains fundamentally constrained by the bias, \emph{i.e.}, the misleading cues caused by spurious \textit{ling...
  </details>

- **2026-10-26** — Jingong Chen, Qingwen Zhang, Youming Deng et al. — [Any3R: Feedforward 3D Reconstruction from Any Camera Type](http://arxiv.org/abs/2610.36150v1)
  <details><summary>📄 Abstract</summary>
  Geometry foundation models recover camera poses and dense geometry from a set of images with a feed-forward network, but they expect pinhole images. That assumption is inside the backbone too: the positional encoding and the training loss both bind an image position to a direction in space, and both depend on the lens. We condition both on the dense ray field, the unit direction through every pixel, which describes any central camera without a lens type, distortion coefficients or a bound on fie...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

- **2026-10-27** — Anouar Imel, Imad Charradi, Abderrahman Sghir et al. — [Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](http://arxiv.org/abs/2610.37624v1)
  <details><summary>📄 Abstract</summary>
  When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant...
  </details>

- **2026-10-27** — Hubert Baniecki, Przemyslaw Biecek, Martin Pawelczyk — [LinMix: Data Mixing as Linear Domain Attribution](http://arxiv.org/abs/2610.37390v1)
  <details><summary>📄 Abstract</summary>
  Language model performance depends strongly on the mixture of domains in the pretraining data corpus. Popular data mixing methods select these domain weights by training many small proxy models on random mixes and then fitting a regression model to predict performance from the mix. We recognize this practice as a domain attribution problem, where the regression measures each domain's contribution to the target metric. Through this lens, the standard Dirichlet sampling of proxy data mixes is a po...
  </details>

- **2026-10-27** — Felipe de Sant'Anna Paixão, Dhyego Tavares, Eduardo Almeida et al. — [Hidden in Plain Sight: an Empirical Study about The Instruction Stacks of Coding Agents](http://arxiv.org/abs/2610.37332v1)
  <details><summary>📄 Abstract</summary>
  Coding agents send their models more than the user's prompt: they add instructions, tool definitions, and environmental context that form an instruction stack. This stack guides execution and changes across releases, yet remains largely unexposed to users and insufficiently characterized in research. We present a longitudinal, cross-agent study of the instruction stacks captured in the first model requests of 1,886 releases of Claude Code, Codex, Gemini CLI, Qwen Code, and OpenCode. Under contro...
  </details>

- **2026-10-27** — Wadie El Amrani, Luis Galárraga — [GraphRAGProv: GraphRAG Meets How-Provenance](http://arxiv.org/abs/2610.37237v1)
  <details><summary>📄 Abstract</summary>
  GraphRAG systems often use knowledge graphs to retrieve relevant context for an LLM that produces the final answer. That makes answers more inscrutable and therefore less appealing for domains where transparency is paramount. We present GraphRAGProv, an architecture that executes SPARQL queries over source-grounded RDF graphs to compute answers and their how-provenance polynomials. These polynomials record which statement occurrences were used and how they were combined. Because each occurrence ...
  </details>

- **2026-10-27** — Iwan Williams — [Do bots feel bad? Assessing empirical evidence for functional valence in LLMs](http://arxiv.org/abs/2610.36962v1)
  <details><summary>📄 Abstract</summary>
  Do LLMs have valenced states, i.e. states that feel pleasant or unpleasant? Recent empirical work has claimed to show that LLMs possess functional valenced states (e.g. ``functional pleasure and pain'' [Ren et al. 2026], ``functional emotions'' [Sofroniew et al. 2026], and ``functional welfare'' [Han et al. 2026]) that play the same causal role as valenced states in cognition and action, without necessarily being consciously experienced. But it remains unexplored how well the identified states f...
  </details>

- **2026-10-27** — Saifullah Saifullah, David Dembinsky, Stefan Agne et al. — [DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding](http://arxiv.org/abs/2610.36929v1)
  <details><summary>📄 Abstract</summary>
  Multimodal transformer models have driven unprecedented performance breakthroughs in modern document understanding. However, the inherent black-box nature of these models remains a major obstacle to their safe deployment in high-stakes sectors. Despite significant progress in explainability for vision and language tasks, explainable AI (XAI) research tailored to multimodal document understanding has received little attention. To address this gap, we present \ourframework{}, the first comprehensi...
  </details>

- **2026-10-27** — Jipeng Li, Pramod Khargonekar, Yanning Shen — [Causal Localization of Evidence Effects in Transformers](http://arxiv.org/abs/2610.36524v1)
  <details><summary>📄 Abstract</summary>
  Can controlled symbolic inputs reveal attention heads that influence a language model's decisions from natural language evidence? We introduce controlled evidence aggregation (CEA), which varies the counts and order of two symbols in otherwise fixed prompts and measures changes in a frozen Transformer's preference between two answer tokens. The preference is measured by their logit difference; the prompts prescribe no correct answer. Balanced utility causal selection (BUC) identifies compact hea...
  </details>

- **2026-10-27** — Jia Chen, Chao Huang, Xinrong Hu et al. — [GarmentSegAgent: Autonomous Garment Segmentation for Web Fashion Images via Textual Self-Refinement](http://arxiv.org/abs/2610.36506v1)
  <details><summary>📄 Abstract</summary>
  Web fashion images support applications such as visual product search and consumer-to-shop matching, yet their visual heterogeneity makes reliable garment segmentation challenging. Despite advances in promptable segmentation, autonomously identifying and correcting garment-specific errors without human-provided spatial prompts remains difficult. We propose GarmentSegAgent, an autonomous framework that integrates semantic planning, spatial execution, and visual evaluation through iterative textua...
  </details>

- **2026-10-26** — Bohan Liu, Xiaohan Fan, Wenqian Ye et al. — [Structure, Not Sequence: Tracking and Validating Folding Mechanisms in ESMFold's Trunk with Sparse Autoencoders](http://arxiv.org/abs/2610.36226v1)
  <details><summary>📄 Abstract</summary>
  Structure predictors like ESMFold fold proteins using neural network computation and have transformed structural biology. However, the driving mechanism from amino-acid (AA) sequence to 3D structure is insufficiently understood, and biological meaning remains locked in the dense network. Sparse autoencoders (SAEs) have shown promising results in obtaining interpretable concept features over an overcomplete basis of intermediate protein sequence-model representations. Yet folding models, which pr...
  </details>

- **2026-10-26** — Anusha Krishnamoorthy, Basudha Pal — [When Slides Met Scans: Cross-Attention for Renal Cancer Prognosis](http://arxiv.org/abs/2610.36364v1)
  <details><summary>📄 Abstract</summary>
  Histopathology and computed tomography (CT) provide complementary views of renal cancer. We connect these modalities through bidirectional cross-attention between 16 histology prototypes and up to 32 kidney-centered CT tokens from frozen foundation models. In 210 TCGA-KIRC patients with 46 disease-specific survival (DSS) events, 5-fold evaluation yielded a C-index of $0.760\pm0.081$ and 3-year AUROC of 0.773 (95\% CI 0.678--0.860), the highest averages among evaluated unimodal and fusion baselin...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-25** — Szymon Mazurek, Alberto Presta, Michał Byra — [Recursive CLIP: Vision-Language Distillation with Looped Transformer Blocks](http://arxiv.org/abs/2610.34563v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language models such as CLIP typically rely on independently parameterized transformer blocks across depth. We investigate the extent to which these blocks can instead be reused recurrently while preserving the transferable capabilities of CLIP. We study recursive transformer backbones in which a small set of $N$ transformer blocks is applied $M$ times per forward pass. By holding $N \cdot M$ fixed to the depth of a standard ViT-B, our models preserve computational depth while...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-10-27** — Kostiantyn Khabarlak — [Multibranch Ensemble Head in Vision Foundation Models for Efficient Cucumber Phenological Stage Classification](http://arxiv.org/abs/2610.37118v1)
  <details><summary>📄 Abstract</summary>
  Vision Foundation Models (VFMs) pretrained with self-supervised learning, such as DINOv2, provide highly transferable features, yet adapting them to small, domain-shifted datasets is still challenging. We propose a regularizing multibranch ensemble head: a training and inference scheme that pairs low- and high-capacity branches, samples a single branch stochastically at each training step, and averages both branches in probability space at inference. The design adds negligible parameters and ess...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-10-27** — Pranjal Aggarwal, Sean Welleck — [Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents](http://arxiv.org/abs/2610.37567v1)
  <details><summary>📄 Abstract</summary>
  AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand real-time interaction, such as playing a video game or operating a physical device. In these settings, the environment state may evolve as the agent is reasoning, or even as the underlying model is performing a forward pa...
  </details>

- **2026-10-27** — Lucas Bayones, Devika Narain, Roman Rossi-Pool — [The geometry of cognition: from neural populations to neurotechnology](http://arxiv.org/abs/2610.36541v1)
  <details><summary>📄 Abstract</summary>
  Cognition is implemented by distributed neural populations whose collective activity evolves through structured, low-dimensional state spaces. In this review, we survey the analytical and conceptual tools used to study latent population dynamics in biological neural networks. We begin with single-unit coding, which remains essential for interpreting neuronal selectivity, and then review population-level approaches, including population vectors, cosine similarity, principal component analysis and...
  </details>

- **2026-10-26** — Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan — [Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses](http://arxiv.org/abs/2610.36114v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are judged by two numbers: the size of the context window, and how often the final answer is correct. Both numbers miss a third thing: how much of a tool's output is lost before the model ever sees it. We measured this loss in a real tool-using agent. The agent finds the cause of injected faults by reading Linux kernel traces. The context window was almost empty: across 720 runs, the single largest prompt used only 5.75% of it. Yet a third of all tool results (3,827 of 11,189) were cu...
  </details>

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


### 📂 other
*其他安全相关 / Other Security-Related* — 174 papers

- **2026-10-27** — Xiaochen Chang — [A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](http://arxiv.org/abs/2610.36717v1)
  <details><summary>📄 Abstract</summary>
  When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human reader. The defensive context may also influnce the consequent when we simply ban defensive writing in the output through prompts. In order to reduce over-defensive writing, we produce a harness that separates the reviewer,...
  </details>

- **2026-10-27** — Amit Kalitaa, Moirangthem Tiken Singh — [When Does Perturbation Consistency Add Information Beyond Softmax Confidence? Theory and Evidence for the Decision Consistency Framework](http://arxiv.org/abs/2610.36640v1)
  <details><summary>📄 Abstract</summary>
  Perturbation consistency scores judge whether a prediction survives small input changes. The Decision Consistency Framework (DCF) scores each image by label stability (LS) and confidence deviation (CD) under six mild operators, combines them into a consistency score (CS), and summarises a model by the gap between accuracy and mean consistency (CAG). We ask when these scores carry information that the clean softmax output lacks. Across 201 evaluations with three seeds per configuration, CS detect...
  </details>

- **2026-10-27** — Joseph Natter, Long Vu, Yifan Zhang et al. — [GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting](http://arxiv.org/abs/2610.37598v1)
  <details><summary>📄 Abstract</summary>
  Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. E...
  </details>

- **2026-10-27** — Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck et al. — [TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments](http://arxiv.org/abs/2610.37592v1)
  <details><summary>📄 Abstract</summary>
  Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on information they will not have when they act, an information gap between training and execution. It widens under partial observability, observation noise, and openness, where the set of agents and tasks present changes during ...
  </details>

- **2026-10-27** — Xinying Qian, Ying Zhang, Yu Zhao et al. — [ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents](http://arxiv.org/abs/2610.37443v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations. However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-grained memory units; and (2) Organizational Mismatch, where memory structures based primarily on semantic similarity may overlook other associations. To address these challenges, we propose ETAMem, a multi-view memory fr...
  </details>

- **2026-10-27** — Jiahong Xiang, Kunqiu Chen, Lingming Zhang et al. — [Spine: Compiling Subtask Trees into Structured Context for Long-Horizon Coding Agents](http://arxiv.org/abs/2610.37224v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding tasks contain nested subtasks. Typically, agents record interactions sequentially into a growing history, causing context inflation and performance degradation. Compressing or trimming the history without explicit subtask boundaries can discard information needed by unfinished subtasks. Conversely, recursive subagent delegation isolates completed subtasks through child agents by assigning every subtask boundary to delegation, which conflates subtask granularity with executing...
  </details>

- **2026-10-27** — Touko Lehenkari, Hannu-Pekka Komsa — [Cu intercalation and field-driven filament formation in vertically aligned MoS$_2$ memristors](http://arxiv.org/abs/2610.37152v1)
  <details><summary>📄 Abstract</summary>
  Vertically-aligned MoS$_2$ films paired with a Cu top electrode have been used as electrochemical metallization cell memristor devices. The memristive switching has been attributed to the formation of conductive filaments, yet their exact structure has remained elusive. Here we carry out a multi-scale computational study of Cu intercalation, clustering, and field-driven dynamics to eventually model the filament formation under operating conditions. We use density-functional theory results to fin...
  </details>

- **2026-10-27** — Zichen Yan, Rui Huang, Shenao Wang et al. — [Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision](http://arxiv.org/abs/2610.36968v1)
  <details><summary>📄 Abstract</summary>
  Image-goal navigation (ImageNav) requires an agent to reach a location specified by a goal image in an unknown environment. For drones, this task demands exploration, goal- directed navigation, and collision avoidance under limited onboard computing resources. Existing aerial ImageNav methods are built on single-view observations, requiring additional rotation and exploration to search for goal-relevant cues outside the field of view. In this paper, we present Omni-IGN, a fully onboard ImageNav ...
  </details>

- **2026-10-27** — Jinyang Li, Zichuan Fu, Xian Wu et al. — [Proactive Memory for Event-Driven LLM Agents](http://arxiv.org/abs/2610.36967v1)
  <details><summary>📄 Abstract</summary>
  Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their applicability to the current event. We propose Proactive Memory (ProactMem), which organizes history into recent events, temporal trajectories, and behavioral regularities. Trajectory facts are checked against source even...
  </details>

- **2026-10-27** — Xiaohan Ye, Zihan Gong, Jingqian Zhao et al. — [PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search](http://arxiv.org/abs/2610.36958v1)
  <details><summary>📄 Abstract</summary>
  Generative retrieval models have been increasingly adopted in search and recommendation systems. However, industrial generative retrieval models are commonly specialized to a fixed online scenario: they learn from scenario-specific interactions, support a narrow set of query forms and retrieval objectives. We study how to remove these couplings and build a unified end-to-end multimodal search system for open-ended image--text queries, heterogeneous shopping intents, and online scenarios with dif...
  </details>

- **2026-10-27** — Chaolang Li, Jingyu Li, Zhaocheng Du et al. — [Natural Hard-Negative Mining from Positives for Instruction-Following Retrieval](http://arxiv.org/abs/2610.36900v1)
  <details><summary>📄 Abstract</summary>
  Instruction-following information retrieval (IFIR) requires retrievers to rank documents by both a query and its instance-specific instructions, yet instruction-conditioned contrastive supervision remains scarce. Existing synthetic methods typically fix a positive passage and generate additional negatives, overlooking the hard-negative potential of the original positive. We propose Natural Hard-Negative Mining (NHNM), which promotes convertible negatives under query-compatible instructions and r...
  </details>

- **2026-10-27** — Jianwei Jiang, Chunhua Yang — [Maximum Energy of Integral Circulant Graphs with Same-Parity Exponents](http://arxiv.org/abs/2610.36883v1)
  <details><summary>📄 Abstract</summary>
  The energy of a finite graph is the sum of the absolute values of the eigenvalues of its adjacency matrix. Let n be p to the power a times q to the power b, where p and q are distinct primes at least five and a and b, both positive integers, have the same parity. Among all nonempty sets D of proper divisors of n, the energy of the corresponding integral circulant graph is maximised by exactly two divisor sets: the divisors p to the power i times q to the power j with i plus j odd, and the diviso...
  </details>

- **2026-10-27** — Haoyu Zhao, Yinzhou Tang, Zixuan Wang et al. — [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](http://arxiv.org/abs/2610.36791v1)
  <details><summary>📄 Abstract</summary>
  Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human interaction videos, robot demonstrations, and simulation rollouts without requiring a...
  </details>

- **2026-10-27** — Rohan Deb, Mohammad Ghavamzadeh, Arindam Banerjee — [Conservative Dueling Bandits: Preference Learning under Baseline Constraints](http://arxiv.org/abs/2610.36708v1)
  <details><summary>📄 Abstract</summary>
  Contextual dueling bandits learn from pairwise comparisons, the same feedback used to fine-tune language models from human preferences. Standard algorithms explore aggressively and can show users two poor options. We study conservative contextual dueling bandits, which require that, at every round, the cumulative score of the better displayed item stay above a $(1-α)$ fraction of a trusted baseline's. An item's score is its probability of beating the best available item, so the constraint depend...
  </details>

- **2026-10-27** — Shang Tingyu, Cao Wenfei — [Balanced State Subspaces for Mamba-2 State Compression](http://arxiv.org/abs/2610.36617v1)
  <details><summary>📄 Abstract</summary>
  Mamba-2 compresses all context into a fixed-size recurrent state that dominates decoding memory and bandwidth. Existing compressors quantize state values or prune state coordinates, scoring each channel independently in the native basis. We examine trained Mamba-2 states and find that energy is almost rank-one, but the output does not read the energetic directions: energy concentrates in a bias-like direction accumulated by the recurrence, while the content the output reads lives in a low-dimens...
  </details>

- **2026-10-27** — Jane Pan, You Lyu, Abe Bohan Hou et al. — [Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](http://arxiv.org/abs/2610.36435v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategically bargaining with other agents. To isolate the effect of user presence, we develop PRESENT, a controlled evaluation framework that compares negotiation settings with and without an interactive user, while holding the...
  </details>

- **2026-10-27** — Matthew J. Liu, Aaron D. Kaplan, Michael L. Whittaker et al. — [Simulated petrological labels enable probabilistic mineralogy prediction from whole-rock geochemistry](http://arxiv.org/abs/2610.36429v1)
  <details><summary>📄 Abstract</summary>
  Modal mineralogy, the mineral identities and abundances in rocks, guides geological studies and industrial resource extraction. While measuring modal mineralogy is time-intensive, whole-rock chemical measurements furnish elemental concentrations at higher throughput. Predicting mineralogy from elemental data, however, poses a one-to-many inverse problem, and labeled mineralogical datasets are too sparse to train on at scale. We address both challenges by simulating petrological labels that expre...
  </details>

- **2026-10-27** — Zhen Yang, Wen Wang, Xander Xu et al. — [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](http://arxiv.org/abs/2610.37649v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without being told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates simulated worlds with altered physics, where one or more laws differ from ordinary ph...
  </details>

- **2026-10-27** — Baptiste Bonin, Caro Strickland, Audrey Durand — [Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use](http://arxiv.org/abs/2610.37533v1)
  <details><summary>📄 Abstract</summary>
  Failure diagnosers for robot manipulation are increasingly vision--language models (VLMs), trained and evaluated on single-arm failures produced by perturbing a successful demonstration. Bimanual tool use adds failures of other kinds: a tool that slips out of its socket while still held, two correct gestures made at different times, and attempts that fail for two reasons at once. On a simulated bimanual tool-use task whose failure causes are read from the recorded trace, we measure what each sen...
  </details>

- **2026-10-27** — Mingwei S. G. Li, Susie S. Y. Li, Isabel Moreira de Oliveira et al. — [PolyGandr: Steering Generative Models via Spatial Navigation through Latent Space](http://arxiv.org/abs/2610.37446v1)
  <details><summary>📄 Abstract</summary>
  Generative models support content creation across text, images, videos, and design disciplines, yet their interfaces rely primarily on natural language. While effective for specifying high-level intent, language can be inefficient and imprecise for fine-grained control, iterative refinement, and open-ended exploration. We present PolyGandr, a visual interface for exploring relationships between latent representations and generated outputs, complementing natural-language model steering. PolyGandr...
  </details>

- **2026-10-27** — Sinjae Kang, Dong Kyu Shin, Jaehong Kim et al. — [Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling](http://arxiv.org/abs/2610.37393v1)
  <details><summary>📄 Abstract</summary>
  Robot policy evaluation often relies on a binary success signal for task completion. In real-world deployment, however, desired execution behaviors are also defined by quality attributes such as execution speed and motion smoothness, which need to be dynamically controlled according to task requirements. To address this, we introduce Quality-Controllable Policy (QCP), a robot policy that enables inference-time control over both individual quality attributes and their combinations. To extend the ...
  </details>

- **2026-10-27** — Zhi Zheng, Binglin Liu, Weihao Chen et al. — [Peers4U: Designing Learner-Centered Virtual Peers for Children's Multimodal Mathematics Learning](http://arxiv.org/abs/2610.37238v1)
  <details><summary>📄 Abstract</summary>
  In early mathematics, children learn abstract concepts through concrete representations, such as manipulating objects, drawing, and speaking. Learning with peers can enrich this process by exposing children to diverse strategies and enabling them to exchange ideas through interaction. We realized this potential with virtual peers in Peers4U, a multimodal learning system to enhance children's mathematical conceptual understanding. Virtual peers driven by LLMs are personalized to the learner's cog...
  </details>

- **2026-10-27** — Callum Berger, Jeremy Pitt, Stefan Sarkadi — [A Serious-Game Testbed for Self-Governing Human-Machine Institutions](http://arxiv.org/abs/2610.36989v1)
  <details><summary>📄 Abstract</summary>
  AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer interaction that needs a testbed for hybrid institutions. We present Megabike, a multi-agent simulator and serious game with interdependent arenas for common-pool resource management, cooperative survival and constitutional...
  </details>

- **2026-10-27** — Andie Huang, Ying Pang, Qian Zhang et al. — [Does More Thinking Pay Off? Reasoning Cost and Correctness of LLMs in Code Generation and Bug Fixing](http://arxiv.org/abs/2610.36952v1)
  <details><summary>📄 Abstract</summary>
  Many LLMs now emit an explicit reasoning trace before they write code, but benchmark results for code generation and bug fixing usually report correctness alone. It is therefore unclear how much the extra reasoning contributes relative to the tokens it consumes. We examine this question with 866 Python tasks drawn from HumanEval Pro, MBPP Pro, and BugsInPy under five model settings. We look at the accuracy gain and token overhead of reasoning, the behaviors that appear inside reasoning traces, a...
  </details>

- **2026-10-27** — Shiyi Cao, Ziming Mao, Dacheng Li et al. — [Evolving Agent Teams](http://arxiv.org/abs/2610.36848v1)
  <details><summary>📄 Abstract</summary>
  The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce Evolving Agent Teams, a multi-agent framework that escapes such local optima. It features (1) a central supervisor that diagnoses each local optimum and restructures a team of agents; and (2) a persistent file system tha...
  </details>

- **2026-10-27** — Hongyu Wu, Chong Liu, Shaoxuan Xie et al. — [RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning](http://arxiv.org/abs/2610.36685v1)
  <details><summary>📄 Abstract</summary>
  Bimanual robot manipulation plays an important role in real-world robotic applications, but the high cost of collecting bimanual demonstrations limits the scalable development of bimanual policy learning. Meanwhile, existing single-arm manipulation data are difficult to directly transfer to bimanual systems due to the Single-to-Dual gap in action spaces, coordination requirements, and arm-side spatial preference. To address this issue, we propose RoboSTD, a zero-shot Single-to-Dual data construc...
  </details>

- **2026-10-27** — Buzhao Liu, Jianing Ye, Xiu Yuan et al. — [RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](http://arxiv.org/abs/2610.36533v1)
  <details><summary>📄 Abstract</summary>
  Recently, LLM-based autonomous agents have shown strong capabilities in iteratively generating, evaluating, and refining executable solutions. In robotic manipulation, Code-as-Policy lets these agents search over modular and editable robot programs. However, effective program search requires physical understanding: agents must understand how objects can be manipulated, how scene geometry constrains actions, and why interactions succeed or fail. Existing methods rely mainly on execution feedback ...
  </details>

- **2026-10-27** — Yibo Yang, Zerui Huang, Haomiao Yang et al. — [MedConstBench: Benchmarking How Constitutions Steer LLMs in Medical Ethics](http://arxiv.org/abs/2610.36513v1)
  <details><summary>📄 Abstract</summary>
  As large language models advance rapidly, they are increasingly used to answer medical questions, and many such models are now deployed locally. Once a model is deployed, its behavior is governed mainly by the ethical policy written into its constitution. However, most existing work focuses on factual correctness rather than the trade-off between competing ethical values. Even benchmarks that do evaluate ethics treat it as a fixed property of the model rather than as a variable, so how a constit...
  </details>

- **2026-10-27** — Truman Hickok — [SO-101 Bench: Accessible Spatial Manipulation](http://arxiv.org/abs/2610.36420v1)
  <details><summary>📄 Abstract</summary>
  Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup. It has four tasks scored as five families, ...
  </details>

- **2026-10-27** — Avishi Poddar, Nico Baßler, Julian Lyne et al. — [Exact Analytical Treatment of Collectively Pumped Dicke Superradiance](http://arxiv.org/abs/2610.37665v1)
  <details><summary>📄 Abstract</summary>
  We study the dynamics of an ensemble of $N$ two-level emitters undergoing collective decay at rate $Γ$ and collective incoherent pumping at rate $R$, confined to the fully symmetric Dicke ladder. Although the population dynamics are confined to a finite set of rate equations, their quantum-trajectory representation involves infinitely many pump-decay histories. We derive an exact finite continued fraction for the Laplace-transformed Dicke-state populations by resumming the infinitely many quantu...
  </details>

- **2026-10-27** — Athanasios Glentis, Dawei Li, Mingyi Hong — [MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control](http://arxiv.org/abs/2610.37647v1)
  <details><summary>📄 Abstract</summary>
  Weight decay and explicit weight-norm constraints improve optimizer performance in language model pretraining, yet a unified understanding of why such control helps and how much is needed remains incomplete. We analyze norm control in Muon over the entire training trajectory using the \emph{accumulated effective learning rate}, $C_T=\sum_{t<T}η_t/\|W_t\|_F$, where $η_t$ is the nominal learning rate and $η_t/\|W_t\|_F$ is the effective learning rate relative to the weight norm. For bounded update...
  </details>

- **2026-10-27** — Nesta Midavaine, Floris Fok, Paulo Mendes et al. — [LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation](http://arxiv.org/abs/2610.37570v1)
  <details><summary>📄 Abstract</summary>
  We present LCM-Promo, an LLM-based uplift model for promotion allocation. LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response. It learns monotonic promotion-response curves from production logs by interpreting single-token outputs as conversion-threshold probabilities, while conditioning on session context such as day and delivery shift. In a production A/B test on churn reactivation, LCM-Pr...
  </details>

- **2026-10-27** — Peize Ding — [Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR](http://arxiv.org/abs/2610.37553v1)
  <details><summary>📄 Abstract</summary>
  Label-free reinforcement learning with verifiable rewards (RLVR) rewards a language model for agreeing with its own majority vote. It improves reasoning at first but eventually collapses: the self-assessed reward goes to one while accuracy falls, often until the model gives the same answer to every problem. The collapse appears only when training uses many problems. We explain this dataset-size dependence as a collective instability. In a solvable many-problem model in which problems share param...
  </details>

- **2026-10-27** — Remy Ogasawara, Cullen Anderson, Narmeen Fatimah Oozeer et al. — [Orthogonal and Parametrized Multi-Attribute Steering of LLMs](http://arxiv.org/abs/2610.37517v1)
  <details><summary>📄 Abstract</summary>
  Activation steering offers an effective and efficient way to modify an LLM's behavior at inference time. However, it remains unclear how to apply steering such that the signal is consistently strong and the steering strength has a universally interpretable meaning. We address this first by identifying the most steerable interval for each steering vector and rescaling the steering range accordingly. Building on this, we introduce a more interpretable method for steering, called parameterized stee...
  </details>

- **2026-10-27** — Devon Yanitski, Chris Westbury — [semanticfa: An R Package for Response-Free Semantic Factor Analysis of Psychometric Scales](http://arxiv.org/abs/2610.37494v1)
  <details><summary>📄 Abstract</summary>
  The items of a reflective psychometric scale can be read as a proposal about a construct's structure. Language models make that proposal measurable by converting each item into an embedding, a list of numbers, similar for similar meanings. We introduce semanticfa, an R package for semantic factor analysis, which factors item-embedding similarities. It also interprets factors, flags redundant items, builds short forms, and screens new items. A worked example analyzes the 50-item International Per...
  </details>

- **2026-10-27** — Milad Sikaroudi — [Concordat: Typed Sessions for LLM Agents](http://arxiv.org/abs/2610.37461v1)
  <details><summary>📄 Abstract</summary>
  Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually stated in the prompt and followed only as reliably as the model chooses to follow them. We present Concordat, a Python library that treats an agent as an object whose interface is a finite-state protocol, in the spirit o...
  </details>

- **2026-10-27** — Yonghao Yu, Lang Huang, Runyi Li et al. — [Vision-Language-Action or World-Action? Just Action Models](http://arxiv.org/abs/2610.37219v1)
  <details><summary>📄 Abstract</summary>
  The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a WAM therefore cannot simply be attributed to any one of them. We show that decoupli...
  </details>

- **2026-10-27** — Weichang Wang, Liyu Chen, Shuyue Guan et al. — [VGIQA: Fine-Grained Image Quality Assessment with Visual Grounding Rewards](http://arxiv.org/abs/2610.37186v1)
  <details><summary>📄 Abstract</summary>
  Image quality assessment (IQA) aims to evaluate the perceptual visual quality of images. Recently, the rapid development of Multi-modal Large Language Models (MLLMs) has significantly advanced the IQA field. By integrating chain-of-thought (CoT) reasoning and reinforcement learning (RL), these models can generate more accurate and interpretable results while relying on less training data. However, existing MLLM-based methods are predominantly constrained to holistic, image-level evaluations and ...
  </details>

- **2026-10-27** — Dipanjyoti Paul, Arpita Chowdhury, Maneet Chatterjee et al. — [INTR++: INterpretable TRansformer with better Accuracy, Interpretability, and Adaptability](http://arxiv.org/abs/2610.37178v1)
  <details><summary>📄 Abstract</summary>
  Interpretable Transformers often perform well in domain specific settings but lose effectiveness beyond that. Achieving ViT-like broad applicability requires models with consistent performance across domains. Recent works on Interpretable Transformers, INTR and Prompt-CAM, were developed keeping domain adaptability in mind. Prompt-CAM leverages learnable prompts to promote adaptability. However, these prompts are fixed in nature and therefore struggle to adapt to domains with substantial variati...
  </details>

- **2026-10-27** — Abdulhaq Adetunji Salako, Christian Tominski — [Science-Fiction Transformation as a Design Lens for Visualization Transformation](http://arxiv.org/abs/2610.37131v1)
  <details><summary>📄 Abstract</summary>
  Science fiction often features characters or objects that undergo radical changes in form while still being recognizable as the same entity. For example, a vehicle might unfold into a robot, or one body might flow or shape-shift into another. We use such transformations as a reflective lens to study similar shape-shifting in visualization, where one visual representation transforms into a completely different one. For example, a node-link diagram might transform into a parallel coordinates plot ...
  </details>

- **2026-10-27** — Sahar Nasirihaghighi, Tianyuan Wang, Kenan Niu et al. — [MCP-Net: Real-Time Coronary Perception Network and Topological Analysis for Robotic Guidewire Navigation](http://arxiv.org/abs/2610.37127v1)
  <details><summary>📄 Abstract</summary>
  Coronary guidewire navigation during percutaneous coronary intervention requires continuous interpretation of vessel anatomy, guidewire position, and target stenosis under two-dimensional X-ray fluoroscopy. While existing approaches commonly address vessel segmentation or device localization as separate tasks, a robotic system requires a more structured perception of the coronary scene to support downstream navigation. In this work, we present a simulation-driven framework centered on a Multi-Ta...
  </details>

- **2026-10-27** — Djardiel S. Gomes, Isaac M. Félix, Marcelo L. Pereira Junior — [First-Principles Investigation of Irida-Graphane: A Wide-Band-Gap Semiconductor Derived from Irida-Graphene](http://arxiv.org/abs/2610.37095v1)
  <details><summary>📄 Abstract</summary>
  Opening a band gap in metallic two-dimensional carbon allotropes is an important step toward their use in electronic and optoelectronic devices, and full hydrogenation has proven to be an effective route to achieve it. Here, we propose irida-graphane, the fully hydrogenated derivative of the irida-graphene, a monolayer composed of three-, six-, and eight-membered rings, and investigate its structural, mechanical, electronic, and optical properties using density functional theory (DFT) at the PBE...
  </details>

- **2026-10-27** — Humza Nusrat, Kundan Thind — [OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](http://arxiv.org/abs/2610.37081v1)
  <details><summary>📄 Abstract</summary>
  Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and methods: OpenGray adds tasks with known answers to the OpenKBP-Opt head-and-neck dataset, including two contradictions with dose goals proven incompatible and a feasible control with a stored plan meeting every hard goal. F...
  </details>

- **2026-10-27** — Adrian Schmidt, Oya Ok, Deniz İpek Zeynioğlu et al. — [Mapping Artistic Engagement with Quantum Technologies](http://arxiv.org/abs/2610.37054v1)
  <details><summary>📄 Abstract</summary>
  Quantum technologies (QT) are increasingly being taken up in artistic practices, for example in the form of visual artworks or quantum computer music. However, more comprehensive empirical studies on the temporal development and the different forms of QT-related art are still lacking. Therefore, this study conducted a systematic mapping and classification of QT-related artworks. To this end, a medium-independent corpus was established, and the artworks were classified into four categories: QT-In...
  </details>

- **2026-10-27** — Sami Alnawali, Muhammad Atif Saeed, Abdul Hadi et al. — [Interpretable Deep Learning Models for Breast Cancer Diagnosis Using Medical Imaging](http://arxiv.org/abs/2610.37026v1)
  <details><summary>📄 Abstract</summary>
  Deep learning shows promise for breast cancer diagnosis, but limited interpretability hinders clinical adoption. We benchmark ten ImageNet-pretrained models (ResNet50, VGG19, InceptionV3, DenseNet121, Xception, MobileNetV2, EfficientNet, ConvNeXt, ViT, and Swin Transformer) for benign-versus-malignant classification on the BreakHis histopathology dataset using a patient-level split, and explain their predictions with Grad-CAM, LIME, Integrated Gradients, and LRP. DenseNet121 performed best, with...
  </details>

- **2026-10-27** — Ryoya Yoshiyama, Bowen Wang, Yuta Nakashima — [Drop the Details, Get the Gist: Dynamic Conceptual Representation for Video Recognition](http://arxiv.org/abs/2610.36832v1)
  <details><summary>📄 Abstract</summary>
  Concept Bottleneck Models (CBMs), which route predictions through a layer of human-interpretable concepts, have substantially improved the interpretability of visual classification by exposing an explicit, language-based rationale for each prediction. Most existing work focuses on static images, and temporal dynamics in videos have been underexplored in conceptual representation. We propose a framework that extends concept-based image recognition to procedural video understanding. It represents ...
  </details>

- **2026-10-27** — Yue Wu, Yang Zhang, Weinan Gan et al. — [Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training](http://arxiv.org/abs/2610.36794v1)
  <details><summary>📄 Abstract</summary>
  Test-time training (TTT) enables a deployed language model to internalize incoming context on-the-fly into a small set of fast-weight parameters, rather than merely treating it as transient context for attention. In-Place TTT recently made this idea practical for large language models by repurposing the down-projection of standard MLP blocks as fast weights. However, we find that its benefit largely disappears on realistic web long-context question answering. We attribute this to In-Place TTT's ...
  </details>

- **2026-10-27** — Jialin Zhang, Lakshya A Agrawal, Shangyin Tan et al. — [Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](http://arxiv.org/abs/2610.36774v1)
  <details><summary>📄 Abstract</summary>
  Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on each optimization step instead of one candidate at a time. In our sweep on two tasks, most batched runs finished in half the wall-clock time or less, and the fastest in about a quarter to a third. Batched settings also ...
  </details>

- **2026-10-27** — Ziluowen Luo, Ruochen Liu, Jun Yin et al. — [The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation](http://arxiv.org/abs/2610.36763v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation (GR) predicts the next item through its semantic ID (SID). Existing methods commonly fit SID vocabularies to pretrained language model (PLM) representations of item descriptions, incurring additional training costs and making vocabulary coverage dependent on the fitting domains. We observe that pretrained sparse autoencoders expose PLM features with human-interpretable semantic annotations, allowing feature indices to serve as a reusable SID vocabulary. However, reusing...
  </details>

- **2026-10-27** — Yucong Zhang, Cancan Li, Bo Xiao et al. — [From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents](http://arxiv.org/abs/2610.36713v1)
  <details><summary>📄 Abstract</summary>
  Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories. We argue that voiceprints are observations of identity, not identities themselves, and formulate online speaker-memory construction to maintain persistent user entities as acoustic evidence evolves. We introduce EvoSpeakerMem, a training-free layer for causal speaker routing, selective acoustic-state updates, and identity-partitioned memo...
  </details>

- **2026-10-27** — Pragna Mallappa — [Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces](http://arxiv.org/abs/2610.36709v1)
  <details><summary>📄 Abstract</summary>
  Reasoning language models answer math problems by writing long chains of thought, and sampling many chains per problem and taking a majority vote raises accuracy at a large cost in generated text. A popular way to cut that cost scores each chain by the model's confidence in each token it writes, where a token is a word or part of a word. The method averages this confidence over a sliding window of 2048 tokens and keeps or stops chains based on the lowest average. We treat the confidence, recorde...
  </details>

- **2026-10-27** — Satomu Tomisaki, Yosuke Mikami, Amane Watahiki et al. — [Japanese Discourse Structure Analysis Based on Segmented Discourse Representation Theory Using LLMs](http://arxiv.org/abs/2610.36667v1)
  <details><summary>📄 Abstract</summary>
  Discourse parsing based on Segmented Discourse Representation Theory (SDRT) is crucial for capturing the structural dynamics of dialogues. However, most prior research focuses on English, and its effectiveness for Japanese remains unclear owing to the lack of Japanese SDRT corpora. To address this issue, we construct Japanese SDRT corpora by translating existing English SDRT corpora using an LLM. Through a comparative evaluation of prompt-based and fine-tuned LLMs, we show that the models achiev...
  </details>

- **2026-10-27** — Shuo Yan, Ningning Hou, Haoyu He et al. — [The View from Nowhere: Population-Centered Agent Evolution](http://arxiv.org/abs/2610.36660v1)
  <details><summary>📄 Abstract</summary>
  Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between population coverage (i.e., the tasks solved by at least one evolved variant) and the performance of the best individual agent. This gap shows that useful capabilities and diagnostic evidence emerge across the population without...
  </details>

- **2026-10-27** — Chengxuan Pei, Ziyao Wang, Teng Mei et al. — [Learning to Formalize: Bridging Open-Ended Workloads and Fast Decision Models](http://arxiv.org/abs/2610.36595v1)
  <details><summary>📄 Abstract</summary>
  Decision models offer fast choices over sup- plied alternatives, while general-purpose large language models interpret open-ended tasks through flexible generation and reasoning at the cost of sequential decoding. Many work- loads expect a generative backend to determine what can be done and therefore provide no well-defined candidate list. We bridge this in- terface gap with a small candidate formalizer trained on offline teacher-generated lists. The formalizer constructs explicit, validated al...
  </details>

- **2026-10-27** — Swapnil Bhosale, Prem Seetharaman, Ke Chen et al. — [TAC2: Timestamped Audio Captioning as composable functions](http://arxiv.org/abs/2610.36568v1)
  <details><summary>📄 Abstract</summary>
  Real-world audio applications require precise, queryable representations grounded in physical time. Yet modern Large Audio-Language Models (LALMs) increasingly favor conversational generation, producing free-form descriptions that conflate acoustic perception with higher-level reasoning and lack precise temporal grounding. We introduce TAC2, a foundation model that casts timestamped audio captioning as composable functions to construct granular, speaker-attributed acoustic timelines directly fro...
  </details>

- **2026-10-27** — Miri Liu, Xiayu Zhao, Encheng Xie et al. — [Do AI Scientists Know What's New?](http://arxiv.org/abs/2610.36511v1)
  <details><summary>📄 Abstract</summary>
  A major challenge facing AI scientific discovery pipelines is how to determine when a generated idea is meaningfully novel. Ideally, novelty checks in these pipelines must be able to reject non-novel ideas while not rejecting too many novel ideas, and they should also be able to distinguish which parts of a proposal are non-novel, as opposed to opaquely discarding entire proposals. We design an analytical framework for evaluation of novelty checks with temporal ground truth at both the proposal-...
  </details>

- **2026-10-27** — Kianté Fernandez, Caitlin Chen, Jialu Zhou et al. — [CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](http://arxiv.org/abs/2610.36484v1)
  <details><summary>📄 Abstract</summary>
  Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We introduce CogArena, ...
  </details>

- **2026-10-27** — Arther Tian, Alex Ding, Simon Wu et al. — [FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](http://arxiv.org/abs/2610.36476v1)
  <details><summary>📄 Abstract</summary>
  Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the audit of sequential agent traces. The protocol separates structured decision validity, optional numerical commitment adherence, execution and ledger reconciliation, and receipt- grounded reporting, with explicit coverag...
  </details>

- **2026-10-27** — Alexa R. Tartaglini, Zhengxuan Wu, Thaddäus Wiedemer et al. — [A Heart Means Recursion: Exploring Visual Meaning and Communication in VLMs](http://arxiv.org/abs/2610.36449v1)
  <details><summary>📄 Abstract</summary>
  Do vision-language models (VLMs) share our ability to communicate visually? We share preliminary findings, starting from a surprising observation: simple visual symbols like a red heart can strongly influence model behavior on seemingly unrelated tasks, such as steering models towards recursive solutions on simple coding problems. Notably, this steering effect is largely implicit, as models' direct interpretations and thinking traces about visual symbols diverge substantially from their observed...
  </details>

- **2026-10-27** — Luis Hasenauer, Arkaprava Roy, Leo Duan — [Mirror Likelihood for Modeling Manifold Data with Application on Correlation Time Series](http://arxiv.org/abs/2610.36448v1)
  <details><summary>📄 Abstract</summary>
  Manifold-valued data arise in a wide range of scientific applications. Existing statistical methods typically follow either an intrinsic approach, which characterizes the manifold itself via quantities such as geodesic distance or the Fréchet mean, or an extrinsic approach, which embeds the manifold into an ambient Euclidean space, performs unconstrained statistical estimation, and projects the result back to the manifold. While the latter is conceptually and computationally simple, likelihood-b...
  </details>

- **2026-10-26** — Kenan Kang, Matthew M. Y. Kuo, Weihua Li — [SpecLST: Spectral-Enhanced Long-Short Term Spatio-Temporal Multimodal Modeling for Traffic Forecasting](http://arxiv.org/abs/2610.36393v1)
  <details><summary>📄 Abstract</summary>
  Modeling multi-scale dynamics in urban road networks is essential for intelligent transportation systems but is often hindered by the computational cost of long-range historical context and the challenge of fusing heterogeneous modalities. Existing spatio-temporal frameworks face a trade-off between sequence length and memory overhead, while frequently neglecting the transient effects of exogenous factors such as road incidents and weather. To address these limitations, we propose SpecLST, a fre...
  </details>

- **2026-10-26** — Shenghui Li, Thiemo voigt — [LoRA on a Budget: Function-Aware Post-Hoc Compression for Adapter Fleets](http://arxiv.org/abs/2610.36386v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) has become a key mechanism for efficiently specializing foundation models into many task- and user-specific variants. Serving many LoRA adapters under a shared resource budget turns post-hoc compression into a two-level allocation problem: rank must be distributed across layers within each adapter and across adapters within the fleet. Although trained LoRAs contain substantial spectral redundancy, spectral reconstruction alone does not determine how much compression an...
  </details>

- **2026-10-26** — Ibrahim Habib, Kevin Li, Trung Nguyen et al. — [The Great Chat in the Sky: Aligning Exotic Astronomical Data to Language with AstroBridge](http://arxiv.org/abs/2610.36375v1)
  <details><summary>📄 Abstract</summary>
  Astronomical observations include images, spectra, and light curves, while the scientific literature describes these objects in natural language. We present AstroBridge, a framework that connects these observations to an LLM through a literature-assisted caption generation pipeline. We used catalog metadata to match observations with scientific texts that describe the same objects. A vision-language model generates descriptive captions from representations of observations, matched passages, and ...
  </details>

- **2026-10-26** — Yueshan Li, Lorenzo Fiaschi, Andrea Censi et al. — [Compatibility and future-proof testing for multi-agent systems](http://arxiv.org/abs/2610.36289v1)
  <details><summary>📄 Abstract</summary>
  Independently developed autonomous agents, such as autonomous vehicles, must guarantee joint compatibility, such as safety and task-completion requirements, when they operate in a shared environment. Existing methods require a centrally designed specification, or interaction mechanism before any agent is deployed. However, such centralized design is unrealistic when agent designs are confidential to their developers, and it is not flexible enough to accommodate future agent designs. We study a b...
  </details>

- **2026-10-26** — Wentao Ye, Yali Ye, Zhiqing Xiao et al. — [From Structural Feedback to Prompt Policies: Learning Faithful Text-to-Image Prompt Editors](http://arxiv.org/abs/2610.36146v1)
  <details><summary>📄 Abstract</summary>
  Prompt optimization should improve the image a user receives without changing the scene the user requested. Yet stylistic rewriting can weaken object attributes and relations even when global text--image similarity remains high. We propose StruPO, a structure-aware prompt editor that uses a calibrated scene graph as a shared representation for policy conditioning and image-grounded supervision. The graph exposes what should be preserved, while deletion, reordering, and insertion provide a token-...
  </details>

- **2026-10-26** — Rajan Maghera, Asher Tempest Arya, Aren A. Babikian et al. — [AGDecode: Semantic Attribute Grammar Derivatives for Safety-Constrained Decoding of Large Language Models](http://arxiv.org/abs/2610.36105v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for code generation, motivating techniques that guarantee the structural and semantic correctness of generated programs. Constrained decoding enforces correctness during generation by restricting token choices to those that admit at least one valid completion. While existing approaches can enforce syntactic constraints and selected semantic properties such as type safety, they either target specific properties or rely on operational pruning mech...
  </details>

- **2026-10-26** — Xi Chen, Chongjian Ge, Yiran Xu et al. — [Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](http://arxiv.org/abs/2610.35866v2)
  <details><summary>📄 Abstract</summary>
  As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark for evaluating autonomous research systems and discovering ideas in language modeling. Arena supports diverse research objectives within a shared experimental environment by separating admissibility from improvement: model quality and resource constraints determine whether a result qualifies, while...
  </details>

- **2026-10-26** — Elizaveta Zinovyeva, Aiham Taleb, Nikita Kozodoi et al. — [Generation and Verification: Human-Agent Collaboration for Safety-Critical Automotive Software Engineering](http://arxiv.org/abs/2610.35982v1)
  <details><summary>📄 Abstract</summary>
  Research on coding agents mainly focuses on generation quality. Yet, safety-critical automotive software makes two additional demands. It prioritizes verification, since every change is reviewed, traced to a requirement, and checked against industry standards such as MISRA and AUTOSAR before it can be committed. It is also a narrow domain, written against layered architectures, embedded resource constraints, and organization-specific interface conventions that are scarce in the data general-purp...
  </details>

- **2026-10-26** — Ahmed Agiza, Tasneem Shaffee, Rahil Badkul et al. — [CRLoMTL: Conflict-Resolution through Low-rank matrices for Multi-Task Learning](http://arxiv.org/abs/2610.36337v1)
  <details><summary>📄 Abstract</summary>
  Multi-task learning (MTL) improves model efficiency by sharing representations across related vision tasks, but it often suffers from negative transfer when task updates interfere with one another. Existing conflict-mitigation methods typically operate in gradient space, requiring explicit task-gradient manipulation and additional optimization steps. We propose Conflict-Resolution through Low-Rank Matrices for Multi-Task Learning (CRLoMTL), a parameter-efficient framework that mitigates task int...
  </details>

- **2026-10-26** — Donggang Jia, Da Li, Zainab Alsuwaykit et al. — [VISTA: Differentiable Viewpoint Planning for Long-Horizon Task Visualization](http://arxiv.org/abs/2610.36111v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon object-centered tasks in interactive 3D environments involve heterogeneous events that unfold across time and space, including fine-grained manipulations, larger structural motions, and subtle state transitions. Effectively visualizing such processes is essential for helping users understand how actions lead to outcomes over time. However, existing camera control methods in 3D systems are commonly designed for static objects, and often fail to maintain the legibility of task-relevan...
  </details>

- **2026-10-26** — X-Era AI Lab Team,  :, Jianhao Lai et al. — [E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling](http://arxiv.org/abs/2610.36011v1)
  <details><summary>📄 Abstract</summary>
  World-action models (WAMs) offer a promising framework for embodied intelligence, yet mainstream approaches remain centered on video foundation models or vision-language models. Even when geometric features extracted by 3D models such as VGGT are incorporated, they are typically passed into a video model or VLM that serves as the primary backbone, leaving 3D geometry as an auxiliary input or prediction target rather than the native foundation for world modeling. We present E0.5, a geometry-nativ...
  </details>

- **2026-10-26** — Hasara Kalumin, Amol Deshpande — [When the Application Layer Is Disposable: Putting Integrity Constraints Back in the Database](http://arxiv.org/abs/2610.36418v1)
  <details><summary>📄 Abstract</summary>
  Integrity constraints have been central to the relational model since its inception. However, beyond keys, single-row CHECKs, and referential integrity, most constraints are enforced by application layers today. SQL ASSERTIONs, standardized in SQL-92, remain poorly supported by major RDBMSs. This has become increasingly unacceptable due to two developments. First, LLM-driven applications and agents increasingly issue queries and updates directly against databases, bypassing application layers wh...
  </details>

- **2026-10-26** — Zike Wu, Ahmed Hatem, Chintan Trivedi et al. — [BoxWorld: Let World Engines Control and Video Generators Render](http://arxiv.org/abs/2610.36371v1)
  <details><summary>📄 Abstract</summary>
  We tackle the challenge of building real-time interactive video worlds with user-defined behaviors. Such worlds must track object states, apply interaction rules, and render the resulting consequences as users act. Yet existing end-to-end video world models typically learn interaction dynamics within the generator, making it difficult to specify object-level rules and reason about their consequences. In this work, we introduce BoxWorld, which separates interaction reasoning from generative rende...
  </details>

- **2026-10-26** — Junchen Li, Liang Xu, Rongzheng Wang et al. — [When Connectivity Misleads: Guiding Agentic Search with Contrastive Evidence Paths](http://arxiv.org/abs/2610.36134v1)
  <details><summary>📄 Abstract</summary>
  Search agents can use cross-document graphs to discover sources through multi-hop connections and choose subsequent actions based on candidate rankings and relationships within a limited observation window. However, documents may rank highly because their numerous connections make them easier to reach, without necessarily providing more valuable evidence. Graph diffusion methods such as Personalized PageRank (PPR) aggregate propagation contributions from multiple sources, allowing highly connect...
  </details>

- **2026-10-26** — Koen Ponse, Aske Plaat, Thomas M. Moerland — [Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning](http://arxiv.org/abs/2610.36075v1)
  <details><summary>📄 Abstract</summary>
  Hardware-accelerated reinforcement learning in JAX has gained rapid popularity in recent years and has proven to be a successful method of scaling online reinforcement learning. The resulting ecosystem, however, is fragmented: environment suites define their own interfaces, and algorithm implementations are typically written for a single suite, a single type of space, and either JAX-native or host-based environments. Here we present Jaxnasium, a library for JAX-based reinforcement learning, aimi...
  </details>

- **2026-10-26** — Mingyang Song, Mao Zheng, Zhiyuan Ma et al. — [Understanding Jev-Style System One Models: Does Structure Reduce Selection Bias?](http://arxiv.org/abs/2610.35826v2)
  <details><summary>📄 Abstract</summary>
  Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior have produced a growing family of models that predict probabilities directly over supplied candidates. Yet systematic comparisons of selection bias across Jev versions, Jev reproductions, and generative LLMs remain limited in multi-option tasks. This leaves a central question: does Jev-style decisi...
  </details>

- **2026-10-26** — Jie Li, Bin Guo, Georgina Curto et al. — [PolicyMediator: Multi-Regional Policy Learning through Mediation Agents with Evolving Skills in OPC Ecosystems](http://arxiv.org/abs/2610.35997v1)
  <details><summary>📄 Abstract</summary>
  One-person companies (OPCs) are emerging enterprises operated by individual entrepreneurs through digital platforms and LLM-based AI agents. These highly skilled entrepreneurs are characterized by being digital nomads, with limited reliance on local ecosystems. Governments in China use distinct regional support policies to attract mobile OPCs, turning local support into a cross-regional coordination problem. OPCs compare regions to maximize their own utility, but imperfect policy perceptions may...
  </details>

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

- **2026-10-25** — Ying Xiao, Xinjian Wu, Lukas Twist et al. — [Honesty Testing of LLMs and AI Agents: A Vision for Software Engineering](http://arxiv.org/abs/2610.34239v2)
  <details><summary>📄 Abstract</summary>
  Human oversight of large language models (LLMs) and artificial intelligence (AI) agents increasingly depends on their reports. Claims that conflict with a system's own judgments can conceal failures, prevent timely intervention, and contribute to severe harm. Greater autonomy makes faithful reporting increasingly important for maintaining human control. In this vision paper, we propose honesty testing of LLMs and AI agents as a new research area in software engineering. Building on existing hone...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 697 |
| prompt-injection | 640 |
| memory-poisoning | 56 |
| tool-use-attack | 164 |
| backdoor | 542 |
| adversarial-attack | 651 |
| privacy-leakage | 4477 |
| steganography | 84 |
| misuse | 1255 |
| red-teaming | 144 |
| vulnerability | 3783 |
| defense | 3667 |
| alignment | 3452 |
| robustness | 3746 |
| watermark | 673 |
| unlearning | 118 |
| agent-safety | 66 |
| benchmark | 71 |
| survey | 427 |
| other | 10112 |

---

📚 **全部 34825 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-10-30 04:19:00*