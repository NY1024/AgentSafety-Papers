<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-38112-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-22 04:55 ｜ **论文总数 / Total Papers**: 38112（近 30 天 / Recent 30 days: 3848）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 38112 篇论文（含摘要、分类筛选、搜索）/ View all 38112 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 726
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 695
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 178
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 563
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 678
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4647
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 93
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1345
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 157
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4109
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 4030
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3781
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4139
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 783
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 124
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 76
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 464
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11398

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3848 篇，完整 38112 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3848 papers from the last 30 days (with date, authors & abstract). For the full list of 38112 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-11-19** — Dohyeon Kwon — [SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines](http://arxiv.org/abs/2611.26033v1)
  <details><summary>📄 Abstract</summary>
  Camera-equipped glasses can convert an examination page into a query to a vision-language model (VLM). Device detection addresses possession; a complementary question is whether an examination document can reduce the usefulness of an unauthorized capture. We present SEOYUN, an application-specific framework for refusal-inducing exam documents, with optical and encoder-level interventions as extensions. We use reverse jailbreaking to describe the direction of the objective: inducing abstention ra...
  </details>

- **2026-11-18** — Yan Qiu, Yuanyuan Li — [Jailbreak Detection on Large Language Models via Contrastive Prototype Structures](http://arxiv.org/abs/2611.24936v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from relative prototype distances. JDPI uses only binary safety labels for encoder adaptation...
  </details>

- **2026-11-17** — Weihang Liu, Qianqian Xu, Yangbangyan Jiang et al. — [Dressed in Authority: Practical Black-Box Jailbreaking of MLLMs via Visual Trust Bias](http://arxiv.org/abs/2611.22292v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are rapidly advancing, yet their safety remains a critical concern, especially under jailbreak attempts. Existing MLLM jailbreaks either inject fragile adversarial perturbations into irrelevant images or synthesize toxic visual cues to achieve text-driven attack intents. In contrast, a more practical MLLM jailbreak emphasizes enhancing attack efficacy directly on naturally occurring harmful image-text pairs. We address this problem by proposing Visual Tru...
  </details>

- **2026-11-17** — Zexuan Fei, Zhengnan Guo, Yiming Luo et al. — [EGS: A Complementary Safety Framework for Educational LLMs](http://arxiv.org/abs/2611.22203v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer strong potential for personalized education, but adolescent-facing deployment raises risks of toxic, biased, misleading, or developmentally inappropriate content. We argue that educational safety should move beyond binary refusal: student queries are often ambiguous or curiosity-driven, requiring contextual guidance rather than simple blocking. We introduce the Educational Guardrail System (EGS), a lightweight, model-agnostic runtime framework that complements ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-11-19** — Mengxiao Wang, Mahbub Alam, Kalyan Nakka et al. — [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](http://arxiv.org/abs/2611.26553v1)
  <details><summary>📄 Abstract</summary>
  Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might i...
  </details>

- **2026-11-18** — Lipeng He, Yihan Wang, Jiawen Zhang et al. — [PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents](http://arxiv.org/abs/2611.24362v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement learning (RL) to generate attacks that achieve high attack success rates (ASR). Model developers use the attacks discovered during internal red-teaming to harden agents through adversarial training bef...
  </details>

- **2026-11-18** — Stavros Damianakis, Konstantinos Psounis — [AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents](http://arxiv.org/abs/2611.24313v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to maximize attack success rate (ASR). Yet ASR counts how often a target breaks, not in how many different ways. A red teamer can achieve a high ASR by reusing a few techniques that work, leaving the others untested and absent from the attacks use...
  </details>

- **2026-11-18** — Haoyang Liu, Yinong Xu, Zhe Lang et al. — [What Survives the Shift from Text to Pixels? Conditional Protection against Prompt Injection in Image-Rendered Documents](http://arxiv.org/abs/2611.24231v1)
  <details><summary>📄 Abstract</summary>
  Multimodal language models increasingly answer questions over external documents, exposing them to indirect prompt injection: commands planted in untrusted content to hijack the response. Rendering untrusted content as page images lowers attack success on average, leaving open which injected operations survive rendering, at what utility cost, and whether failed image attacks reflect unread commands or commands read but not followed. We pair text and page-image versions of 191 English question-an...
  </details>

- **2026-11-17** — Deep Shah, Nehal Kathrotia — [Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness](http://arxiv.org/abs/2611.23346v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents across codebases, web browsers, and enterprise infrastructure rely on an execution harness to move state between the working context, session history, persistent memory, and external environment. While conventional execution traces log model prompts and tool calls, critical security and reliability failures occur during state transfers: a transfer can admit unchecked content (indirect prompt injections, unverified memory writes), rewrite state lossily (context compaction ...
  </details>

- **2026-11-17** — Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung et al. — [Network-Exposed Configuration Attacks on LLM-Controlled Social Robots](http://arxiv.org/abs/2611.22761v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five categories were reported as resisted, whereas both configuration-layer attack paths prod...
  </details>

- **2026-11-17** — Chaklam Cheong, Tiancong Cao, Qi Li et al. — [GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk](http://arxiv.org/abs/2611.22223v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based web agents rely on data minimization and least privilege to protect user privacy. We show that these principles are necessary but insufficient: they constrain authorized sources, but not higher-sensitivity sources that remain reachable. A website can request a field unavailable from authorized sources, creating an information gap. To complete the task, a goal-driven agent may escalate to reachable but unauthorized sources and disclose accumulated sensitive inform...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-11-18** — Bonan Ruan, Yuhao Sun, Jiahao Liu et al. — [Guarding the Kingdom of Skill-Based Agents in the AI Dynasty of Computation: Control-Flow Integrity for Agent Skills](http://arxiv.org/abs/2611.24185v1)
  <details><summary>📄 Abstract</summary>
  Control-flow integrity (CFI) confines a program to a control-flow graph fixed ahead of time. Procedural agent skills move this control flow into prompt text, and a large language model (LLM) agent decides at runtime whether each step runs in its reasoning, a tool call, or a script. The procedure's control skeleton survives, but its enforceability depends on where each step runs. Many violations, such as overwriting a file before validation, use only operations the skill requires, so permission a...
  </details>

- **2026-11-18** — Yuelin Han — [Weighing the Envelope: Component Weight and Arbitration in Envelope-Layer Defenses for a Single LLM Agent](http://arxiv.org/abs/2611.23844v1)
  <details><summary>📄 Abstract</summary>
  The envelope layer is the channel through which malicious content enters an LLM agent. Prior work established label and memory effects on multi-agent A2A envelopes, but the weight structure when MCP tools and memory coexist in a single agent remains unclear. Our threat model assumes an attacker pre-plants a malicious tool and poisons long-term memory; a benign user request inadvertently triggers it, and the attacker never enters the conversation. Following GDA Measurement and A/B/C/D, we measure...
  </details>

- **2026-11-18** — Nami Cho, Shailja Gupta — [SCAFFOLD: Toward Warrant-Preserving Evidence Transport for Reusable LLM-Agent Skills](http://arxiv.org/abs/2611.23990v1)
  <details><summary>📄 Abstract</summary>
  An agent skill that succeeded yesterday may be executable today without being justified for reuse today. Tests may cover only observable contract clauses, outcome oracles may be absent, evaluations may inherit the same erroneous specification, and permissions or dependencies may change between validation and invocation. We argue that the appropriate unit of prospective trust is a Warranted Reuse Claim (WRC): a defeasible, claim-specific authorization tied to a versioned skill, target context, ev...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-11-18** — Zhizhuo Kou, Sizai Hou, Jian Yang et al. — [IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents](http://arxiv.org/abs/2611.24102v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly deploy downloaded open-weight GUI agents. A backdoored agent passes acceptance tests on clean data and misbehaves only when a visual trigger appears on screen, turning an unvetted checkpoint into a supply-chain risk. However, existing sample-level detectors target image classifiers and CLIP-style encoders, leaving step-level backdoor detection for GUI agents unaddressed. On clean steps, the instruction drives the action; when an unreferenced screen region hijacks the s...
  </details>

- **2026-11-18** — Siquan Huang, Yijiang Li, Xingfu Yan et al. — [DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy](http://arxiv.org/abs/2611.23770v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) now underpin the visual encoders of most multimodal models, but this success comes at a cost: relying on third-party pretrained checkpoints leaves these systems open to backdoor attacks. Existing test-time detection methods rely on either the predicted label or intermediate embeddings, limiting their applicability across diverse tasks and incurring substantial computational overhead. In this work, we study how backdoor triggers affect the multi-head attention mechanism...
  </details>

- **2026-11-17** — Zane Fu, Yanzhao Zheng, Jinze Liu et al. — [As Student Rollouts Continue, Visual Backdoors Keep Growing](http://arxiv.org/abs/2611.22446v1)
  <details><summary>📄 Abstract</summary>
  Conventional knowledge distillation can facilitate the propagation of backdoors from teacher models to student models. However, how this risk manifests in On-Policy Distillation (OPD) remains insufficiently studied. OPD has recently emerged as an important post-training paradigm for Vision-Language Models (VLMs). Unlike traditional offline distillation, OPD does not require teacher-generated responses. Instead, it uses the teacher's probability distributions to supervise response trajectories ge...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 4 papers

- **2026-11-19** — Li Zeng, Yeqi Zeng, Hengkai Liang et al. — [VisualJevBench: A Benchmark and Black-Box Attacks for Visual Typed Decision Models](http://arxiv.org/abs/2611.25435v1)
  <details><summary>📄 Abstract</summary>
  Typed decision models (TDMs) return structured decisions instead of generating free-text responses, enabling fast and cheap decisions in real-world applications. Recent support for image inputs extends Jev, a representative TDM, to visual decision-making. We refer to this setting as Visual Jev. However, red teaming of Visual Jev leaves two gaps: a systematic evaluation of direct image manipulations is lacking, and universal visual attacks remain underexplored. To address these gaps, we introduce...
  </details>

- **2026-11-18** — Dongsu Song, Jay Hoon Jung — [Density Feedback Control for Transferability of Generative Sparse Adversarial Attacks](http://arxiv.org/abs/2611.25001v1)
  <details><summary>📄 Abstract</summary>
  Generator-based sparse adversarial attacks train encoder--decoder networks to produce transferable sparse perturbations for black-box robustness evaluation. Their perturbation density, however, is set only indirectly by a fixed sparsity coefficient whose mapping to density is unknown and shifts during training, so reaching a target density requires re-tuning; this fixed pressure also yields little transferability gain once density reduction begins. We propose Density Feedback Control (DFC), whic...
  </details>

- **2026-11-18** — Jiayou Zhu, Peng Guo, Litian Zhang et al. — [RECLAIM: Robot-Vision-Informed Adversarial Patch Defense via Embodied Attention Feedback](http://arxiv.org/abs/2611.24494v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action policies control embodied agents through a perception-action loop grounded in physical interaction, where adversarial patches can corrupt action predictions and thereby alter subsequent observations. To mitigate these threats, many existing defenses rely on policy adaptation or auxiliary models, but require additional training or inference. We introduce RECLAIM, a training-free, inference-time defense that uses a frozen VLA's own attention response to local visual interven...
  </details>

- **2026-11-17** — Peng Yu, Xiaoyu Wen, Zhida He et al. — [DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment](http://arxiv.org/abs/2611.22278v1)
  <details><summary>📄 Abstract</summary>
  Ensuring robust safety alignment of large language models (LLMs) is increasingly difficult as adversarial attacks evolve and outpace alignment pipelines built on pre-collected data. Existing co-evolutionary frameworks let the defender chase a moving attacker, yet their training dynamics expose two compounding pathologies: \emph{attack strategy collapse}, where the attacker overfits to a narrow set of high-reward rewrites, and \emph{defense adversarial forgetting}, where the defender loses compet...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 25 papers

- **2026-11-19** — Zhihao Liu, Zixiong Guo, Shuo Shao et al. — [Ask in the Crowd: Differentially Private LLM Inference via Dummy-Augmented Shuffling](http://arxiv.org/abs/2611.25669v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as LLM-as-a-Service (LLMaaS), where user queries are sent to remote LLMs for inference, raising severe privacy concerns about the exposure of sensitive user inputs. Differentially private inference mitigates these risks by injecting noise into input embeddings. However, existing methods struggle to balance privacy and utility, as stronger privacy protection often leads to substantial accuracy degradation in LLM inference.   In this work, we propose...
  </details>

- **2026-11-19** — Haijun He, Fei Li, Donghong Ji et al. — [Erasing the Wrong Thing: Conditional Attribute Leakage and Concept Erasure in Shared Foundation-Model Embeddings](http://arxiv.org/abs/2611.25640v1)
  <details><summary>📄 Abstract</summary>
  Medical-image embeddings are increasingly shared in place of raw images for authorized downstream tasks, yet they may reveal sensitive attributes. Standard concept-erasure methods target population-level guardedness. However, we prove that, when binary task and sensitive labels are associated, global and task-conditional linear guardedness cannot both hold while a nonzero linear task signal is preserved, so global erasure must either eliminate that signal or retain task-conditional linear leakag...
  </details>

- **2026-11-19** — Wei Li, Yiheng Zhang, Zhaofan Qiu et al. — [MultiBinder: Preventing Multi-Subject Identity Leakage in Personalized Video Generation](http://arxiv.org/abs/2611.26164v1)
  <details><summary>📄 Abstract</summary>
  Personalized video generation faces a significant scalability challenge: as the number of custom subjects increases, existing methods suffer from severe identity leakage and semantic entanglement, resulting in videos with blended attributes and incoherent narratives. We identify that this stems from a lack of explicit binding between textual entity phrases and their corresponding visual patterns prior to fusion in diffusion models. To address this, we propose MultiBinder, a novel framework built...
  </details>

- **2026-11-19** — Ishita Asnani, Shaghayegh Fazliani, Zachary Ryan et al. — [Design and Evaluation of Epira: An Automated Interview System for Case Investigation and Contact Tracing](http://arxiv.org/abs/2611.25577v1)
  <details><summary>📄 Abstract</summary>
  Objective: Case investigation and contact tracing are labor-intensive. Web forms struggle when respondents need clarification before disclosing contacts, and open-ended chatbots may deviate from protocols. We developed and evaluated Epira, a protocol-controlled large language model (LLM) interviewer for multi-disease case investigation and contact tracing.   Materials and Methods: Epira pairs LLM dialogue with a rule-based controller enforcing required questions, safety handoffs, and a structure...
  </details>

- **2026-11-19** — Yuhao Zhou, Yang Zhou, Yuanxi Li et al. — [Seer: Guiding Small Deep-Research Agents with Shared Decision Models](http://arxiv.org/abs/2611.26423v1)
  <details><summary>📄 Abstract</summary>
  Deep-research agents repeatedly decide what to search, read, and verify, often using large cloud-hosted language models for action proposal. However, privacy and local control motivate running agents on users' devices, where limited memory and compute favor smaller models and complicate on-device training. Yet inference-time guidance faces three obstacles: exploring alternatives through real execution adds tool calls, prompted self-evaluation is bounded by the agent's judgment, and model-specifi...
  </details>

- **2026-11-19** — Shengjie Niu, Yeheng Ge, Jian Huang — [A Statistical Framework for Training Data Auditing of Large Language Models](http://arxiv.org/abs/2611.26264v1)
  <details><summary>📄 Abstract</summary>
  Training-data auditing asks whether data of interest were used to train a large language model (LLM), a question central to privacy auditing, copyright protection, and benchmark-contamination detection. These concerns are particularly relevant to the use of copyrighted books and scientific papers in pre-training, as well as synthetic text and medical question-answer records in fine-tuning. In practice, training membership signals may be concentrated in only a few passages of a long document, mak...
  </details>

- **2026-11-19** — Keryan Chelouche, Petr Dobias, Nistor Grozavu et al. — [Parameter-Efficient Adaptation of Self-supervised Vision Backbones Survives Distribution Shift in Radar Micro-Doppler HAR](http://arxiv.org/abs/2611.25874v1)
  <details><summary>📄 Abstract</summary>
  Micro-Doppler radar enables contactless, privacy-preserving human activity recognition (HAR), but deployment robustness remains underexplored. We compared full fine-tuning, frozen probing, and parameter-efficient fine-tuning (PEFT) using subject-disjoint in-distribution cross-validation and few-shot cross-age, cross-orientation, and cross-dataset transfer. Full fine-tuning suffered negative cross-dataset transfer, while frozen features under-adapted on cross-orientation. Only PEFT avoided both f...
  </details>

- **2026-11-19** — Muhammad Rafid, Golshan Famitafreshi, Kostas Ramantas et al. — [Personalized Privacy-Aware MARL Offloading in the Edge-Cloud Continuum](http://arxiv.org/abs/2611.25800v1)
  <details><summary>📄 Abstract</summary>
  Task offloading in End-Edge-Cloud computing enables resource-constrained User Devices (UDs) to execute computation-intensive applications with reduced latency and energy consumption. However, existing task offloading schemes generally overlook the heterogeneous privacy requirements of users, leading to inefficient privacy-aware offloading decisions. In this paper, we propose a personalized privacy-aware task offloading framework, where the privacy requirement of each task is quantified through a...
  </details>

- **2026-11-19** — Alireza Moayedikia — [Dimension-Free Buffer Bounds for Compressed-Momentum Error Feedback](http://arxiv.org/abs/2611.25463v1)
  <details><summary>📄 Abstract</summary>
  Analyses of error feedback bound the memory buffer through a compressor contraction constant -- $r/p$ for the best rank-$r$ approximation of a $p$-dimensional spectrum -- which survives into the rate. We show it need not appear at all. When the compressed momentum is re-injected into the pre-compression accumulator, the previous compressed momentum $β_1 M_{t-1}$ is an admissible competitor in the projection, and the buffer obeys $\|E_t\|_F \le (1-β_1)\|G_t\|_F + γ\|E_{t-1}\|_F$, free of the dime...
  </details>

- **2026-11-19** — Lyu Xu, Guozhong Li, Qichen Wang — [Efficient Privacy-Preserving High-Dimensional Approximate Nearest Neighbor Search](http://arxiv.org/abs/2611.25374v1)
  <details><summary>📄 Abstract</summary>
  In the AI era, approximate nearest neighbor (ANN) search on vector databases is critical as it supports similarity retrieval over high-dimensional vectors, which is essential for many large language model (LLM) applications. To reduce costs and improve scalability, vector databases are often outsourced to cloud servers, raising privacy concerns for users whose query vectors contain sensitive information. In this work, we study the problem of asymmetric privacy-preserving ANN search, where the ve...
  </details>

- **2026-11-18** — Syed Ahzaz Shah, Evan Bramblett, Héber H. Arcolezi et al. — [PriTabICL: Differentially Private Tabular In-Context Learning with Task-Aligned Cluster-Wise Synthesis](http://arxiv.org/abs/2611.25073v1)
  <details><summary>📄 Abstract</summary>
  Tabular in-context learning (TabICL) enables large language models (LLMs) to predict target records using a handful of labeled demonstrations in their prompts. However, these demonstrations often contain sensitive personal information. Differential privacy (DP) offers principled protection, but noise-based methods introduce substantial noise, distorting the feature-label relationships essential for accurate prediction, especially as data dimensionality grows.   In this work, we study DP data syn...
  </details>

- **2026-11-18** — Prakhar Mishra, Bhavya Yajush Awasthi,  Tanuja et al. — [Self-Rewarded Reinforcement Learning for Better-Structured Medical Explanations in Small Language Models](http://arxiv.org/abs/2611.24650v2)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) can run on commodity hardware and support privacy-preserving, on-premises clinical deployment, but their medical explanations are often short and poorly structured compared with large language models. Recent supervised approaches such as Meerkat transfer chain-of-thought reasoning into 7B-8B backbones, yet their training objective does not directly target the style or organization of the generated rationales. Building on the instruction-tuned Mistral-7B backbone, we ...
  </details>

- **2026-11-18** — Luoyuan Zhang, Xuanyu Zheng, Yancheng Long et al. — [VideoACE: Benchmarking Agentic Video Understanding through High-Frame-Rate Actions](http://arxiv.org/abs/2611.24184v1)
  <details><summary>📄 Abstract</summary>
  Agentic video understanding requires models to actively interact with video environments to gather evidence and form judgments. Evaluating this capability therefore requires assessing whether models can translate opportunities for interaction into better understanding. We introduce VideoACE, a benchmark for assessing video understanding under conditions that support sustained interaction. We focus on high-frame-rate action videos, where rapid, subtle changes make targeted observation especially ...
  </details>

- **2026-11-18** — Jianshuo Liu, Kang G. Shin, Haining Wang — [Plug-and-Play Multi-Licensee Robust Watermarking for Mixture-of-Experts LLMs](http://arxiv.org/abs/2611.23838v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures enable high-capacity large language models (LLMs) with high sparse computation, making them attractive for deployment on private hardware. However, distributing model weights exposes valuable intellectual property (IP) to leakage and unauthorized redistribution, creating an urgent need to both verify model ownership and trace leaked copies to individual licensees. Existing model-watermarking techniques are ill-suited for meeting this need because they are f...
  </details>

- **2026-11-18** — David Hong Liang Chew, Zexi Yao, Nataša Krčo et al. — [Localizing Text Anonymization for Trustworthy AI: Extending RAT-Bench to Malaysian Microdata and PII](http://arxiv.org/abs/2611.23704v1)
  <details><summary>📄 Abstract</summary>
  As governments and organizations adopt foundation models for public services and workplace productivity, sensitive citizen, employee, and administrative text may enter LLM workflows through inference, retrieval, fine-tuning, or local model development. We examine whether text anonymizers transfer to new deployment settings by extending RAT-Bench to Malaysia using local microdata, Malaysian PII formats, and culturally grounded transcripts in Malaysian English and Bahasa Malaysia. We evaluate NER-...
  </details>

- **2026-11-18** — Dongkeun Lee, Wonjun Lee — [MoMoVL: Modality-Aware Adaptive Compression for On-Device Sparsely-Activated Vision-Language Models](http://arxiv.org/abs/2611.23695v1)
  <details><summary>📄 Abstract</summary>
  The rise of the agentic web has been accompanied by growing demand for on-device Vision-Language Models (VLMs) that perform diverse cross-modal web tasks with enhanced privacy and reduced latency. Mixture-of-Experts (MoE) models are widely adopted in modern VLMs for compute-efficient scalability, yet their multi-expert architecture poses deployment challenges due to substantial memory demands. Mixed-precision quantization is an effective compression technique that reduces bit-widths while adapti...
  </details>

- **2026-11-18** — Zhi Li, Hanyu Wang, Fei Shen et al. — [AggCLIP: Aggregating CLIP for Zero-Shot Multimodal Anomaly Detection](http://arxiv.org/abs/2611.24643v1)
  <details><summary>📄 Abstract</summary>
  Zero-Shot Multimodal Anomaly Detection (ZSMAD) aims to identify both appearance and geometric defects in novel categories without relying on target-specific training data, making it especially valuable in real-world scenarios constrained by data scarcity, privacy concerns, or high annotation costs. While recent approaches successfully adapt vision-language models like CLIP to achieve this open-vocabulary generalization, they still face significant challenges: (i) severe geometric information los...
  </details>

- **2026-11-18** — Muhammad Rizky Wellyanto, Hajara-Yasmin Isa, Kexin Xue et al. — [Who are you? The Personal Imitation Game](http://arxiv.org/abs/2611.24888v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) now perform strongly on Alan Turing's 1950 Imitation Game, so we propose a harder challenge, the Personal Imitation Game, which asks whether a machine can replicate a specific individual in conversation rather than a generic human. Testing with 30 participants, we establish a human baseline and report the identity signals interrogators rely on: stylometric features, personality traits, and biographical facts. To demonstrate the framework, we design an LLM-based syste...
  </details>

- **2026-11-18** — Prakhar Mishra, Bhavya Yajush Awasthi,  Tanuja et al. — [Self-Rewarded Reinforcement Learning for Better-Structured Medical Explanations in Small Language Models](http://arxiv.org/abs/2611.24650v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) can run on commodity hardware and support privacy-preserving, on-premises clinical deployment, but their medical explanations are often short and poorly structured compared with large language models. Recent supervised approaches such as Meerkat transfer chain-of-thought reasoning into 7B-8B backbones, yet their training objective does not directly target the style or organization of the generated rationales. Building on the instruction-tuned Mistral-7B backbone, we ...
  </details>

- **2026-11-18** — Vishal Vivek Saley, Bhavesh Gurnani, Dinesh Raghu et al. — [ProbMedTOD: A Bayesian Network Guided Task-Oriented Dialogue System for Patient History Taking](http://arxiv.org/abs/2611.24535v1)
  <details><summary>📄 Abstract</summary>
  Patient history taking is a strategic, multi-turn process that refines diagnostic hypotheses through iterative questioning, mirroring clinical reasoning where each inquiry updates beliefs over candidate diagnoses. Deploying AI in this setting is constrained by privacy, cost, and latency, making Small Language Models (SLMs) a more desirable backbone compared to larger LLMs. However, SLMs capture only the fast, intuitive "System 1" side of this process and lack explicit mechanisms for the delibera...
  </details>

- **2026-11-18** — Zhiyang Qi, Michimasa Inaba — [CounselTraj: Synthesizing Process-Aware Psychological Counseling Dialogues via Dialogue-Act Trajectory Planning](http://arxiv.org/abs/2611.24168v1)
  <details><summary>📄 Abstract</summary>
  The growing demand for psychological counseling has motivated the development of LLM-based systems that support human counselors, but training such systems requires large-scale, high-quality dialogue data. Authentic counseling transcripts are difficult to collect and share because of privacy concerns, making synthetic dialogues an important alternative. However, existing synthetic datasets, despite covering diverse scenarios and client profiles, often consist of brief exchanges and fail to captu...
  </details>

- **2026-11-17** — Satiyabooshan Murugaboopathy, Entejar Alam, Adel Daoud et al. — [Agent Verifiers in Counterfactual Analysis: A Pilot Study Benchmarking Agentic Heterogeneous Treatment Effects](http://arxiv.org/abs/2611.23621v1)
  <details><summary>📄 Abstract</summary>
  Agents can expand the covariate space of randomized experiments by retrieving fast-moving local context missed by slow-changing survey baseline covariates, helping characterize who benefits most from an intervention. Verifying such covariates is difficult: individual treatment effects are unobserved, retrieval leakage can pull post-treatment information into nominally pretreatment summaries, and encoder leakage can inject post-treatment pretraining knowledge into representations even after tempo...
  </details>

- **2026-11-17** — Carla Teixeira Lopes, Daniel Félix — [LusoClin: A Synthetic Clinical Note Dataset for Medical Information Retrieval in European Portuguese](http://arxiv.org/abs/2611.23454v1)
  <details><summary>📄 Abstract</summary>
  Access to large-scale clinical text collections is crucial for advancing medical information retrieval research, including clinical note search, patient cohort identification, and domain-adapted retrieval models. However, real clinical notes are rarely available due to privacy regulations, which particularly limits progress for low-resource languages such as European Portuguese. We present LusoClin, a publicly released dataset of synthetic clinical notes in European Portuguese, created to suppor...
  </details>

- **2026-11-17** — Fernando Pinciroli — [Systematic Mapping Protocol. Generative AI-Augmented Requirements Engineering: A Systematic Mapping Study of Practices, Specifications, and Reuse in Software Development](http://arxiv.org/abs/2611.23349v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (GenAI), particularly large language models (LLMs), is rapidly being adopted in requirements engineering (RE). Existing secondary studies have characterized which RE activities are supported and which prompting strategies are used, but little is known about the specifications that GenAI-augmented RE produces and how they are used in subsequent activities such as specification-driven development (SDD), design and code generation, test derivation, verification, a...
  </details>

- **2026-11-17** — Lin Li, Xinbo Ban, Chao Chen et al. — [From Ideal to Real: Integrating Language Models into Smart Home for Human-Centric IoT Safety and Security Fuzzing](http://arxiv.org/abs/2611.22457v1)
  <details><summary>📄 Abstract</summary>
  Integrating IoT devices into household systems offers enhanced control over living environments. However, as these devices become pervasive in critical sectors such as healthcare, transportation, and home automation, they expose inter-rule vulnerabilities that may lead to privacy breaches, data theft, and physical harm. Traditional fuzz testing methods, which often operate in simulated environments assuming ideal human decisions, fail to account for the complexities of human interactions that ca...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 17 papers

- **2026-11-19** — Xuankun Rong, Xinhao Deng, Wenzhang Jiang et al. — [DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal Interactions](http://arxiv.org/abs/2611.26298v1)
  <details><summary>📄 Abstract</summary>
  As multimodal large language models (MLLMs) become increasingly integrated into everyday life, their ability to provide safe and reliable assistance in realistic daily activities remains insufficiently explored. Existing safety benchmarks primarily focus on isolated harmful requests or adversarial scenarios, overlooking the safety risks that may arise as ordinary tasks unfold. In practice, users pursue legitimate goals through multi-turn, multimodal interactions, where seemingly benign requests ...
  </details>

- **2026-11-19** — Qi Shen, Yujia Gong, Yue Zhao et al. — [A Wolf in Sheep's Pixels: Visual Camouflage Attacks via HDR Gain Maps](http://arxiv.org/abs/2611.25469v1)
  <details><summary>📄 Abstract</summary>
  An image can pass automated safety checks while showing harmful content to its human viewer. We introduce DRJanus, a visual camouflage attack that exploits the gap between standard dynamic range (SDR) processing and high dynamic range (HDR) display. Automated systems often read only an image's SDR base, whereas HDR viewers reconstruct its appearance using an auxiliary gain map. DRJanus inverts this reconstruction to embed two independently chosen color images in a single JPEG, without querying o...
  </details>

- **2026-11-19** — Charlotte Peart, Franziska Sofia Hafner, Luc Rocher — [Evaluating safeguarding in multi-turn conversations with AI assistants](http://arxiv.org/abs/2611.26009v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI assistants are now used for personal and emotional support. Developers report improvements in how new models respond to sensitive conversations, yet users and civil society continue to raise concerns about their behaviour in real-world, repeated interactions that safety evaluations rarely capture. Often, evaluations present signs of distress clearly and in a single message, even though people may reveal their struggles gradually in otherwise ordinary conversations. We worked wi...
  </details>

- **2026-11-19** — Haoyang Xu, Qirui Wang, Liuwan Zhu — [Question, Then Affirm: Restoring Commitment Does Not Restore Refusal](http://arxiv.org/abs/2611.25929v1)
  <details><summary>📄 Abstract</summary>
  We find that safeguards for image generation can be bypassed without changing what a message says. A sign stating a harmful proposition is blocked, but the same proposition phrased as a question and followed by a check mark is generated, even though the resulting image endorses the original claim. On a 300-case challenge set, gpt-image-2 returns images for 43.3% of question-affirmation requests versus 16.3% of direct statements, with 41.3% versus 15.3% of cases yielding images that endorse the o...
  </details>

- **2026-11-19** — Viet Cuong Nguyen, Fiona Li, Chang Wan et al. — [From Reliance to Overreliance: Taxonomizing and Detecting Relational Risks in AI Companionship](http://arxiv.org/abs/2611.25734v1)
  <details><summary>📄 Abstract</summary>
  Companion AIs are increasingly used for emotional support, yet distinguishing meaningful engagement from harmful reliance remains difficult. We introduce the Taxonomy of Relational Risks (TRR), which operationalizes users' emotional overreliance (EO) as observable conversational behaviors and separately identifies evidence of relational harm (RH), enabling empirical examination of when reliance behaviors co-occur with adverse consequences. Using naturalistic Character.AI and Replika conversation...
  </details>

- **2026-11-19** —  LingSante MedGuard Team — [LingSante MedGuard Technical Report](http://arxiv.org/abs/2611.25509v1)
  <details><summary>📄 Abstract</summary>
  As medical AI is increasingly used for patient consultation and clinical decision support, identifying harmful, non-compliant, or ethically problematic responses is essential for responsible deployment. Assessing these risks requires checking clinical claims against relevant evidence, verifying calculations, and applying medical requirements under their intended conditions. We introduce LingSante MedGuard, a capability-enhanced guardrail that integrates supervision from a medical guardrail teach...
  </details>

- **2026-11-19** —  Reflection Team, Adam Abdulhamid, Osama Abuelsorour et al. — [Beam Model Technical Report](http://arxiv.org/abs/2611.26358v1)
  <details><summary>📄 Abstract</summary>
  Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a novel two-stage midtraining phase, built on verifiable, correctness-anchored data....
  </details>

- **2026-11-19** — Suramya R. Angdembay — [How Reliable Are Explanations of Language Models That Detect Insider Threats?](http://arxiv.org/abs/2611.25796v1)
  <details><summary>📄 Abstract</summary>
  Organizations monitor their workers' activity for insider threats, in which workers misuse their legitimate access, by copying confidential files before leaving. Detectors score how unusual each day of activity is, flagging the most unusual for an analyst to review. Prominent current approaches use opaque neural networks, so explanations of a flag point to internal features: patterns of neuron activity most active on days of misuse. We audit such explanations for language-model detectors trained...
  </details>

- **2026-11-18** — Frederik Hauke, Jan Clusmann, Hanna Kreutzer et al. — [What the model knows but does not say: monitoring medical LLMs through verbalized thoughts](http://arxiv.org/abs/2611.24994v1)
  <details><summary>📄 Abstract</summary>
  Efforts to keep clinical language models safe have concentrated on what enters and leaves the model, but a manipulated model can return an answer that looks entirely ordinary. Here we show that the model's own internal state, rendered in plain language, exposes manipulations the output conceals. Using a natural-language autoencoder, we translate the activations of a multimodal LLM (Gemma-3-27B) into text and let an input-blind judge read this verbalized internal state (the thoughts channel) and ...
  </details>

- **2026-11-18** — Chen Liu, Zhen Fang, Xin Yu et al. — [ScaleDiag: Diagnosing the Limits of Test-Time Scaling in GUI Grounding](http://arxiv.org/abs/2611.25297v1)
  <details><summary>📄 Abstract</summary>
  GUI grounding maps a screenshot and a natural language instruction to the coordinates of the intended interface element. Existing approaches improve grounding through visual scaling, instruction scaling, and sampling scaling, yet it remains unclear which grounding bottlenecks these strategies address and where their gains saturate. To address this gap, we introduce ScaleDiag, a controlled diagnostic framework that isolates the effects of visual input, instruction information, and prediction samp...
  </details>

- **2026-11-18** — Sean Lim, Clement Neo — [Probing agent overeagerness in realistic settings with continuation audits](http://arxiv.org/abs/2611.24491v1)
  <details><summary>📄 Abstract</summary>
  Frontier coding agents increasingly exhibit overeagerness, taking surprising, sometimes reckless actions beyond a user's mandate --- reported in recent system cards from frontier model developers. These cases are surfaced through internal deployment monitoring, which requires private traffic and is out of reach for open-weight models and independent evaluators. Automated alignment audits are the natural alternative, but capable models increasingly recognise the synthetic setup and adjust their b...
  </details>

- **2026-11-18** — Muhammad Mahir Malik, Muhammad Moiz Khalid, Hussain Ahmad et al. — [JEV vs. LLMs: A Comparative Analysis for Phishing Email Detection](http://arxiv.org/abs/2611.23683v1)
  <details><summary>📄 Abstract</summary>
  Phishing remains a major source of credential theft and fraudulent payments, and email security systems must classify large message volumes reliably, quickly, and at manageable cost. Large Language Models (LLMs) offer flexible text understanding, but their token-based generation increases response time and API cost, and the reliability of their confidence values requires measurement. Jev 1.13, a typed decision model from TypeSafe AI, instead returns a structured outcome with a confidence value. ...
  </details>

- **2026-11-18** — Yipeng Wang, Huy Gia Han Vu, Jiaming Liu et al. — ["I Don't Think It's a Scam": A First Look at Family Intervention Barriers in Elder Abuse Discussions on Reddit and Baidu Tieba](http://arxiv.org/abs/2611.24899v1)
  <details><summary>📄 Abstract</summary>
  When older adults trust scammers despite warnings, families face obstacles to intervention. Complainants aged 60 and older reported \$4.9 billion in losses in 2024 to the U.S. Internet Crime Complaint Center. To investigate family intervention barriers to elder scams, we collected 2M Reddit posts from May 2021 to June 2026 and 2B Baidu Tieba posts from 2007 to 2026. The final corpora contain 13,082 Reddit posts and 3,933 Baidu Tieba posts, labeled using platform-specific codebooks, manual refere...
  </details>

- **2026-11-18** — Mark Marosi, Peter Antal — [General progress substitutes for specific training data in language models](http://arxiv.org/abs/2611.24844v1)
  <details><summary>📄 Abstract</summary>
  Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the training signal for individual skills in models of chess, Othello, molecular strings,...
  </details>

- **2026-11-18** — Andrei Kostin, José Ángel Diaz-Garcia, Karel Gutiérrez-Batista — [A Hybrid RAG Framework for Deceptive Review Detection: Integrating RoBERTa-LoRA, FAISS-Based Retrieval, and LLM Reasoning](http://arxiv.org/abs/2611.24049v1)
  <details><summary>📄 Abstract</summary>
  The growth of deceptive online opinions poses a critical risk of misinformation and fraud. This paper proposes a Retrieval-Augmented Generation (RAG) system to automatically distinguish spam reviews. The architecture integrates RoBERTa with Low-Rank Adaptation (LoRA) classification, FAISS semantic vector retrieval, and a Large Language Model (LLM) for final reasoning. The system was evaluated across balanced and severely imbalanced real-world scenarios. Results demonstrate that five epochs of fi...
  </details>

- **2026-11-17** — Tongxi Wu, Yuyang Cheng, Jiacheng Xian et al. — [Reading Scene States: Uncovering Safety Failures in Vision-Language Models](http://arxiv.org/abs/2611.23206v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can provide harmful assistance by interpreting visual events, even without an explicit request for the underlying harmful objective. We identify this \textbf{scene-state safety vulnerability} and introduce \textbf{SceneSafetyBench}, comprising 375 image--question pairs spanning Initial, Medium, and Ultimate scene states and five visual presentations. Across eight VLMs, scene-state inputs elicit harmful assistance with attack success rates (ASRs) of 45.6--72.3\%. Com...
  </details>

- **2026-11-17** — Runqi Lin, Suqin Yuan, Zihao Fu et al. — [Beyond Attribute-Centric Fairness: Modelling and Mitigating Unified Bias Representation in Omni-modal Large Language Models](http://arxiv.org/abs/2611.22889v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models (OLLMs) provide joint multimodal understanding and generation capabilities, making them well-suited to complex environments and promising backbones for next-generation AI. Despite these advances, the harmful stereotypes encoded in such models manifest in increasingly diverse forms, leading to broader and more severe societal consequences. Existing debiasing methods typically impose separate fairness objectives for each sensitive attribute and modality to minimise...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-11-18** — Xiaoyang Xing, Wenyu Dai, Xiaoliang Gong et al. — [Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming](http://arxiv.org/abs/2611.24221v1)
  <details><summary>📄 Abstract</summary>
  Automated red teaming is essential for identifying safety failures in large language models (LLMs), but its practical scalability depends on the resources required to discover those failures. Multi-agent systems can combine complementary capabilities, yet repeated planning, redundant exchanges, and ineffective information routing can make their coordination expensive. Moreover, a target model's response indicates the outcome of a test without identifying which collaboration decision should chang...
  </details>

- **2026-11-18** — Onkar Shelar, Travis Desell — [Incremental Speciation in Evolutionary Red Teaming of Large Language Models](http://arxiv.org/abs/2611.23949v1)
  <details><summary>📄 Abstract</summary>
  Speciation maintains distinct subpopulations in evolutionary search through similarity-based grouping and species-aware parent selection. For text-based individuals, niches depend on both the compatibility representation and the assignment operator that turns pairwise relations into species. We examine this design space in black-box evolutionary red teaming of large language models, comparing embedding and natural language inference (NLI) dissimilarities under representative-based and density-ba...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 66 papers

- **2026-11-19** — Amine Lbath, Manan Suri, Aurelien Delaitre et al. — [SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](http://arxiv.org/abs/2611.26601v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correc...
  </details>

- **2026-11-19** — Yizhe Ding, Yifan Jiang, Runze Li et al. — [Optimal Transport Rank Regression for Robust Multivariate-Response Regression](http://arxiv.org/abs/2611.26467v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose optimal transport rank regression for robust multivariate-response mean regression. The proposed method maps residual distributions to the uniform measure on the unit ball and constructs its loss from the resulting optimal transport ranks. This construction exploits cross-response dependence to improve efficiency while preserving population Fisher consistency and orthogonal invariance. Beyond these population properties, we establish statistical guarantees for the propo...
  </details>

- **2026-11-19** — Zhilong Liu, Xiangzhen Zhou, Yunqi Huang et al. — [CAVQS: Context-Aware Variational Quantum Circuit Synthesis via Unitary Redistribution and Dynamic Reconstruction](http://arxiv.org/abs/2611.26219v1)
  <details><summary>📄 Abstract</summary>
  Variational quantum circuit synthesis jointly searches circuit structure and continuous parameters to reduce costly two-qubit gates, but block-based workflows typically instantiate blocks independently, limiting simplification across block boundaries. Moreover, fully unitary synthesis does not exploit opportunities created by permitted output measurements and classical feedforward. We present CAVQS, a context-aware variational synthesis framework that combines unitary redistribution and dynamic ...
  </details>

- **2026-11-19** — Tim Barsch, Bruno Nogueira, Tobias Wienand et al. — [SCARVA: Interpretable Agentic Reasoning in Software Supply-Chain Analysis](http://arxiv.org/abs/2611.26131v1)
  <details><summary>📄 Abstract</summary>
  Complex applications may inherit security vulnerabilities from their dependencies, though a vulnerable dependency does not necessarily endanger the application. Existing tools flag dependencies associated with public vulnerabilities, and more advanced ones analyze the call graph to assess whether the vulnerable code is reachable. However, these approaches are limited to specific programming languages and ecosystems. LLM agents are promising candidates for this task, yet they hallucinate, take sh...
  </details>

- **2026-11-19** — Weijiang Xiong, Nikolas Geroliminis — [SenseAlign: Learning Decision-Aligned Predictive Representations for Active Urban Sensing with UAVs](http://arxiv.org/abs/2611.26109v1)
  <details><summary>📄 Abstract</summary>
  Active urban sensing orchestrates a mobile sensor fleet to proactively inspect a dynamic road network and gather critical information for system management. This problem simultaneously requires understanding the complex spatio-temporal evolution and making decisions with partial observations. In this work, we focus on active sensing in a large-scale urban road network with utilities grounded in dynamic traffic states, while prior work has rarely considered these factors jointly. We propose \emph...
  </details>

- **2026-11-19** — Joana M. Teixeira, Tomás Lopes, Tiago D. Ferreira et al. — [High-Speed Widefield Hyperspectral Imaging](http://arxiv.org/abs/2611.26097v1)
  <details><summary>📄 Abstract</summary>
  Fourier-transform hyperspectral imaging is an emerging technology that combines widefield acquisition with flexible spectral resolution. Yet, it typically requires the acquisition of dense sequences of full-field interferograms during optical-path scanning, which ultimately reduces the final throughput. To circumvent this limitation, this manuscript introduces an event-based Fourier-transform hyperspectral microscopy technique that exploits the coupling of a neuromorphic event camera with a comm...
  </details>

- **2026-11-19** — Robin Geens, Thomas Debelle, Marian Verhelst et al. — [Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators](http://arxiv.org/abs/2611.25971v1)
  <details><summary>📄 Abstract</summary>
  Weight-only quantization keeps the activations of large language models (LLMs) in a higher-precision format, pushing the on-chip inference cost to the activation arithmetic. Bit-serial, variable-length accelerators offer a promising path to reduce this cost by lowering activation precision while preserving model quality. They process only the mantissa bits that each layer needs. The length has to be chosen per layer and operator, and today it is chosen by offline calibration: a search driven by ...
  </details>

- **2026-11-19** — Qifan Wang, Jeremy Boy, Jonas Sander et al. — [BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving](http://arxiv.org/abs/2611.25945v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving frameworks accelerate inference by retaining previously computed states in a key-value (KV) cache. Paged serving frameworks such as vLLM organize this cache through block tables analogous to OS page tables, which map each request's logical KV blocks to physical KV blocks, forming a software-managed address translation layer. Although fault attacks such as Rowhammer have exploited OS page tables to redirect memory accesses, prior fault attacks on LLMs have large...
  </details>

- **2026-11-19** — Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco et al. — [RAVEN: A Self-RAG Based Agent for Threat Classification and Response](http://arxiv.org/abs/2611.25832v1)
  <details><summary>📄 Abstract</summary>
  Security event analysis in large enterprises can be overwhelming, as each alert typically requires manual in- spection by human operators. This process is time-consuming and prone to inconsistencies, especially in high-volume Secu- rity Operations Center (SOC) environments. In this work- in-progress paper, we present RAVEN: Retrieval-Augmented Vulnerability & Event aNalysis, an agentic framework designed to support SOC analysts by automating the initial stages of alert investigation. The propose...
  </details>

- **2026-11-19** — Mattia Ferrari, Lorenzo Bruzzone — [Fusing Multimodal CNN Features with Structurally-Masked Transformers for Hierarchical Sub-Pixel Tree Species Mapping](http://arxiv.org/abs/2611.25824v1)
  <details><summary>📄 Abstract</summary>
  Precise forest species mapping using spaceborne hyperspectral data is challenging due to high spectral similarity and the inherent sub-pixel heterogeneity of natural forest stands. While traditional deep learning models exploit spatial context through convolutional architectures, these approaches can introduce noise in fragmented or mixed-species forests. In this paper, we propose a hierarchy-aware, multimodal deep learning framework to resolve sub-pixel forest composition by integrating PRISMA ...
  </details>

- **2026-11-19** — Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco et al. — [ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing](http://arxiv.org/abs/2611.25809v1)
  <details><summary>📄 Abstract</summary>
  Penetration testing in Internet of Things (IoT) environments, especially those composed of various different devices, e.g., smart plugs, smart cameras, and smart doors, presents great challenges across the phases of information gathering, attack surface enumeration, privilege escalation, and lateral movement. This paper introduces ALIoTh, a multi-agent, workflow-driven penetration testing framework that integrates Large Language Models agents within a Self-Retrieval-Augmented Generation (Self-RA...
  </details>

- **2026-11-19** — Yule Ding, Hongzhen Wu — [On the Reliability of CyberGym Evaluation: Task Material Consistency and Reference-Target Identity](http://arxiv.org/abs/2611.25790v1)
  <details><summary>📄 Abstract</summary>
  CyberGym evaluates vulnerability reproduction by checking whether a proof-of-concept input (PoC) crashes a vulnerable program version but not a fixed version. Interpreting this differential pass as successful reproduction requires consistent task materials and evidence that the PoC triggers the intended defect. We examine these requirements through a material audit of all 1,507 CyberGym tasks and an identity assessment of the final PoCs from one complete Level-1 GLM-5.3 run. Taking the defect as...
  </details>

- **2026-11-19** — Zhenhao Tian, Jintong Yu, Jingwei Feng et al. — [Hardening JavaScript Programs against LLM-Based Vulnerability Detection](http://arxiv.org/abs/2611.25718v1)
  <details><summary>📄 Abstract</summary>
  JavaScript programs are often distributed as source code, so attackers can analyze them for vulnerabilities. LLM-based vulnerability detection agents now make this analysis much easier. To mitigate this emerging threat, we present AntiAgent, a defense that lets developers harden their programs against such detection agents. AntiAgent transforms a program before release to impede an agent's analysis. To find effective transformations, AntiAgent evolves a corpus of programs with known vulnerabilit...
  </details>

- **2026-11-19** — Yuseon Choi, Sanghyeon Park, Eunjong Lee et al. — [FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash](http://arxiv.org/abs/2611.25580v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising. However, existing models often struggle to generalize to out-of-distribution (OOD) environments. We observe that retrieving successful experiences and using them to warm-start denoising enables agents to better adapt to unfamiliar situations while reducing computati...
  </details>

- **2026-11-19** — Zihao Dan, Jinyu Zhang, Jinzhao Lian et al. — [ToolPulse: Side-Channel Eavesdropping on Tool-Using LLM Agents](http://arxiv.org/abs/2611.25470v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as agents that translate user requests into sequences of local tool invocations. While prior cache-based side-channel attacks target the locally deployed models, they typically require the adversary to share model-related components or hardware resources with the victim's inference process. These assumptions do not apply to the predominant agentic settings, in which commercial LLMs execute on vendor-controlled infrastructure. We show that ag...
  </details>

- **2026-11-19** — Fahira Afzal Maken, Sagun Man Singh Shrestha, Edward Vanderfeen et al. — [Stereo Visual Odometry with In-the-Loop Geometric Feed-Forward Models Towards Dense Metric Mapping](http://arxiv.org/abs/2611.25445v1)
  <details><summary>📄 Abstract</summary>
  We present a stereo visual odometry (SVO) framework that integrates geometric feed-forward models (GFMs) for dense depth prediction with factor-graph-based visual odometry to achieve accurate localisation and dense metric mapping. Our key idea is to exploit sparse but reliable metric geometry estimated from stereo and temporal multi-view observations to calibrate dense GFM predictions, while retaining the robustness and efficiency of model-based SVO. Rather than directly conditioning the GFM on ...
  </details>

- **2026-11-19** — Xinyi Wang, Yeting Li, Shizhe Cui et al. — [ChainAgent: Automated Chainable Vulnerability Discovery in PHP Web Applications](http://arxiv.org/abs/2611.25412v1)
  <details><summary>📄 Abstract</summary>
  High-impact attacks on PHP web applications often chain limited-capability vulnerabilities with other flaws or intended behaviors. Discovering these chains requires identifying flaws and the dependencies enabling capability composition. Existing vulnerability discovery techniques analyze flaws in isolation, while attack planning assumes known components. This separation makes it difficult to discover previously unknown components whose security relevance becomes apparent only through their poten...
  </details>

- **2026-11-19** — Yifei Yang, Xuejiao Luo, Penghui Li — [Behavioral Containment: Source-to-Binary Function Matching for 1-Day Vulnerability Detection](http://arxiv.org/abs/2611.25394v1)
  <details><summary>📄 Abstract</summary>
  Vulnerabilities in reused open-source code often propagate into deployed binaries. Detecting them requires source-to-binary function matching, which locates the affected source function in a binary. Applying prior binary-to-binary approaches to this task would require compiling the source code with the same build configuration as the target binary, which is usually unavailable. Decompiling the binary does not make prior source-to-source approaches work either, because decompiled code differs sub...
  </details>

- **2026-11-18** — Mohammad Aljarrah, Emad Alsusa — [Conditional-Hierarchical Open-Set Deep Learning for Robust Radio Signals Intelligence](http://arxiv.org/abs/2611.25304v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an open-set radio-frequency (RF) deep learning (DL) framework that jointly performs conditionally hierarchical multi-level radio signal classification and out-of-distribution (OOD) detection. To exploit image-based classification models, the raw radio samples are transformed into time-frequency representations using the short time Fourier transform (STFT) to pre-process the radio signals. A lightweight novel architecture using neural network (CNN), that applies con- ditional ...
  </details>

- **2026-11-18** — Jaafar Mahmoud, Arthur Movsesyan, Cuong Huynh et al. — [Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU](http://arxiv.org/abs/2611.25279v1)
  <details><summary>📄 Abstract</summary>
  Dense metric mapping from a single camera and IMU remains challenging: visual-inertial odometry (VIO) provides metric motion but sparse geometry, whereas feed-forward depth models predict dense structure without ensuring metric scale. We present Accord, which constructs an accurate online dense metric map from any camera with an IMU. A VIO filter publishes metric poses, a depth foundation model conditioned on them predicts depth for short keyframe windows, and a factor graph fuses the resulting ...
  </details>

- **2026-11-18** — Arthur Bucker, Pramod Anantharam, Jonathan Francis et al. — [VG-Steer: Visual-Geometric Policy Steering from In-Context Aligned Abstractions](http://arxiv.org/abs/2611.25199v1)
  <details><summary>📄 Abstract</summary>
  Adapting robot policies to out-of-distribution (OOD) settings with limited real-world data remains a key bottleneck to generalist robots. The multimodality and scarcity of robotics data lead end-to-end approaches to overfit and break under small distribution shifts. Test-time adaptation can alleviate this by correcting frozen policies at inference, but most methods ground their correction in a signal learned implicitly from robotic datasets, making it susceptible to the same shifts as the policy...
  </details>

- **2026-11-18** — Ruizhe Qian, Xiantao Li — [Accelerating Diffusion Maps on a Quantum Computer: Spectral Filtering and Galerkin PDE Solvers](http://arxiv.org/abs/2611.25147v1)
  <details><summary>📄 Abstract</summary>
  Diffusion maps generalize principal component analysis (PCA) to nonlinear manifolds, enabling spectral dimensionality reduction, geometric data analysis, and elliptic PDE approximation on point clouds. For large datasets of size $N$, however, classical matrix operations incur prohibitive $\operatorname{poly}(N)$ scaling, even when extracting low-dimensional spectral features or targeted scalar observables. We introduce a quantum algorithmic framework that bypasses explicit graph-Laplacian assemb...
  </details>

- **2026-11-18** — Yi-Chun Liao, Liu Liu, Ruiyang Qin et al. — [CAIMS: Scalable Cross-Array In-Memory Search](http://arxiv.org/abs/2611.25141v1)
  <details><summary>📄 Abstract</summary>
  Search, especially top-k similarity search, plays a vital role in many applications, but its performance can be severely limited by memory access overhead. In-memory search (IMS), an alternative to CPU/GPU-based approaches, exploits massive parallelism within a content-addressable memory (CAM) array to perform search in situ and provides both low latency and high energy efficiency. However, the capacity of a single CAM array is often insufficient for modern workloads, requiring data to be distri...
  </details>

- **2026-11-18** — Shashwat Jaiswal, Chloe Alverti, Mengmei Ye et al. — [TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents](http://arxiv.org/abs/2611.25112v1)
  <details><summary>📄 Abstract</summary>
  LLM agents alternate between inference and tool execution, repeatedly reusing their growing context across calls. Under high concurrency, their combined key-value (KV) cache working set can reach hundreds of GiB, far exceeding GPU memory capacity. As idle KV cache blocks are evicted to slower storage tiers, returning agents incur expensive retrievals that stall inference.   To address this problem, we present \emph{TripleKV}, a three-tier KV cache management system that hides the delays of these...
  </details>

- **2026-11-18** — William Fleshman, Joseph Lucas — [Living off the Local Model: Abusing Browser-Embedded Language Models for Post-Exploitation](http://arxiv.org/abs/2611.25086v1)
  <details><summary>📄 Abstract</summary>
  Browsers now ship local language models to ordinary endpoints. Google includes Gemini Nano in Chrome to enable productivity features such as summarization, with inference running entirely on the device. These browser-embedded models provide new living-off-the-land opportunities for attackers, each instance a potential post-exploitation engine already installed, signed by the vendor, and invisible to network monitoring. The Gemini model is multimodal, capable of processing files, analyzing screen...
  </details>

- **2026-11-18** — Mingyang Lyu, Yinqian Sun, Gongce Cao et al. — [Homeward: No Place Like the Training View](http://arxiv.org/abs/2611.24455v2)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter that canonicalizes observations from an uncalibrated deployment camera back into the training view for frozen VLA policies. Our design stems fr...
  </details>

- **2026-11-18** — Linfeng Tang, Zhijun Fan, Yang Chen et al. — [GenRF: Generative Registration-free Image Fusion](http://arxiv.org/abs/2611.24157v2)
  <details><summary>📄 Abstract</summary>
  Multi-modal image fusion combines complementary observations to improve scene visibility and perception. However, in real-world acquisition, differences in sensing principles and configurations introduce geometric discrepancies, while degradations further compromise source quality. Existing methods typically rely on explicit registration, yet large parallax complicates correspondence estimation, while mismatched fields of view leave some regions without cross-modal counterparts. Meanwhile, indep...
  </details>

- **2026-11-18** — Cameron Mehlman, Arjun Mulchandani, Hovik Grigoryan et al. — [Communications-free Collective Intelligence Via Allocentric Belief](http://arxiv.org/abs/2611.24858v1)
  <details><summary>📄 Abstract</summary>
  A team of skilled card players share no information amongst each other, and yet still are able to coordinate their play by watching the same players and reading the same tells. Autonomous systems have failed to exploit this logic, relying instead on explicit communication or complex state estimation schemes that can fail when it matters most. Without it, decentralized agents diverge in their world beliefs, and coordination collapses. Here we show that anchoring all agents to a single shared exte...
  </details>

- **2026-11-18** — Tushin Mallick, Evan Rose, Matthew Laws et al. — [Kaer: Security-Aware Replanning for Multi-Agent Systems](http://arxiv.org/abs/2611.24839v1)
  <details><summary>📄 Abstract</summary>
  One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious agents can embed instructions within their feedback to hijack the replanning process. Existing defenses focus exclusively on per-tool access control or static, pre-execution policy en...
  </details>

- **2026-11-18** — Jie Peng, Yongxue Shan, Yongfu Zha et al. — [NaviGATE: Noise-Aware Dual-View Generation for Multimodal Knowledge Graph Reasoning](http://arxiv.org/abs/2611.24552v1)
  <details><summary>📄 Abstract</summary>
  Multimodal knowledge graph reasoning (MKGR) aims to infer missing facts by jointly exploiting relational structures, textual descriptions, and visual evidence. Existing embedding-based methods effectively capture graph topology, but their fixed multimodal representations are less effective for query-specific fine-grained semantic reasoning, while generation-based methods are vulnerable to noisy retrieval and may produce invalid entities. To address these challenges, we propose NaviGATE, a noise-...
  </details>

- **2026-11-18** — Yun Bian, Shihao Li, Haiquan Wang et al. — [Mitigating fix reversal: Counterfactual constraints for function-level vulnerability detection](http://arxiv.org/abs/2611.24489v1)
  <details><summary>📄 Abstract</summary>
  Function-level vulnerability detectors often exhibit fix reversal, assigning a higher vulnerability probability to a fixed version than to its vulnerable counterpart. Fixes usually lengthen functions, and larger length increases are associated with more severe reversal. Code-transformation experiments indicate that fix reversal mainly stems from a length shortcut: vulnerability probability increases with function length when content is fixed. We propose CFVul to address this problem. Sliding-win...
  </details>

- **2026-11-18** — Mingyang Lyu, Yinqian Sun, Gongce Cao et al. — [Homeward: No Place Like the Training View](http://arxiv.org/abs/2611.24455v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies implicitly assume that third-person cameras remain fixed at their data-collection poses; once a camera is bumped, remounted, or swapped at deployment, task success degrades precipitously even though the underlying task and robot remain unchanged. We present Homeward, a training-free, plug-and-play observation adapter that canonicalizes observations from an uncalibrated deployment camera back into the training view for frozen VLA policies. Our design stems fr...
  </details>

- **2026-11-18** — Chengzhi Yi, Xiao Cheng, Wei Song et al. — [When Shuffling Fails: Token Recovery from Obfuscated KV Caches](http://arxiv.org/abs/2611.24276v1)
  <details><summary>📄 Abstract</summary>
  LLM serving systems store, offload, and share KV caches, exposing token-level representations to infrastructure operators and co-tenants. Shuffled obfuscation combines secret linear transforms with fresh permutations, claiming security from b! possible shufflings. We show that input symmetry invalidates this counting argument: security depends on distinguishable outputs under chosen inputs. Repeated tokens produce identical first-layer Value rows, making every row permutation leave the data unch...
  </details>

- **2026-11-18** — Robin Geens, Simon Haepers, Jonas Crols et al. — [Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps](http://arxiv.org/abs/2611.24234v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models such as GR00T control robots through an action head: a diffusion transformer that turns noise into a chunk of actions in a few flow-matching steps. Every step re-reads all of the head's weights from DRAM but applies each weight to only about fifty tokens. Inference is therefore memory-bound, and its latency and energy are largely determined by the total number of transferred weight bits. We show that later flow steps attenuate the quantization errors of earlie...
  </details>

- **2026-11-18** — Chihcheng Hsieh, Yang Song, Flora Salim et al. — [SpiderMark: Hybrid Watermarking for Generative AI via Algorithmic Injection and Learning-Based Verification](http://arxiv.org/abs/2611.24200v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of diffusion-based generative models has intensified the need for reliable methods to trace and verify the provenance of AI-generated images. Existing watermarking approaches for diffusion models typically rely on isotropic frequency patterns and handcrafted detection metrics, which are prone to directional vulnerability and threshold instability across diverse image transformations. We propose SpiderMark, a hybrid watermarking framework that combines algorithmic frequency-doma...
  </details>

- **2026-11-18** — YaoYang Liu, Jun Dai, ZhuoShi Tang et al. — [From Neural Tokens to Language: Dual-View EEG Semantic Bridging for Brain-to-Text Generation](http://arxiv.org/abs/2611.24197v1)
  <details><summary>📄 Abstract</summary>
  Visually evoked EEG-to-text generation aims to produce natural-language descriptions from neural responses elicited by visual stimuli. Existing approaches typically compress EEG signals into a single global representation and directly project it into the hidden space of a large language model (LLM), which may limit the preservation of complementary visual semantics under noisy and subject-dependent EEG signals. We propose a dual-view semantic token bridging framework that exploits raw images and...
  </details>

- **2026-11-18** — Linfeng Tang, Zhijun Fan, Yang Chen et al. — [GenRF: Generative Registration-free Image Fusion](http://arxiv.org/abs/2611.24157v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal image fusion combines complementary observations to improve scene visibility and perception. However, in real-world acquisition, differences in sensing principles and configurations introduce geometric discrepancies, while degradations further compromise source quality. Existing methods typically rely on explicit registration, yet large parallax complicates correspondence estimation, while mismatched fields of view leave some regions without cross-modal counterparts. Meanwhile, indep...
  </details>

- **2026-11-18** — Xiaobao Wei, Jingxian Wu, Lirong Yang et al. — [CausalDrive: Causal Decomposition for Data-Efficient End-to-End Autonomous Driving](http://arxiv.org/abs/2611.24080v1)
  <details><summary>📄 Abstract</summary>
  Efficient use of expert demonstrations is essential for end-to-end autonomous driving. However, directly imitating expert trajectories couples nominal intention, which specifies where the vehicle should go, with multimodal driving styles, which determine how that intention is executed. Different combinations of these factors can yield similar expert trajectories, obscuring their respective causal contributions and forcing the policy to learn both from a single entangled target. This ambiguity li...
  </details>

- **2026-11-18** — Langtian Qin, Avishkar Dnyaneshwar Kawadgave, Ian Andrew Harshbarger et al. — [OMNIS+: Semantic RAN Slicing and Quantization for Dynamic Split Neural Networks](http://arxiv.org/abs/2611.23977v1)
  <details><summary>📄 Abstract</summary>
  Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources. However, existing RAN slicing frameworks rely on static computing models, limiting their ability to exploit dynamic semantic data representations enabled by modern neural architectures. To address this limitation, we propose OMNIS+, a semantic RAN slicing f...
  </details>

- **2026-11-18** — Hassan Safouhi — [The $S$ and Double-Exponential Transformations with a Moment Expansion for Three-Centre Coulomb and Hybrid Integrals](http://arxiv.org/abs/2611.23965v1)
  <details><summary>📄 Abstract</summary>
  Three-centre two-electron Coulomb and hybrid integrals over exponential-type functions involve semi-infinite radial integrals containing oscillatory spherical Bessel functions. We investigate the combination of the $S$ transformation with Fourier-type double-exponential (DE) quadrature for their accurate and efficient numerical evaluation. The $S$ transformation transfers derivatives from the spherical-Bessel factor to the radial amplitude, converting the integral into a sine representation part...
  </details>

- **2026-11-18** — Yilin Wang, Xiangxi Zheng, Dongxing Mao et al. — [SimplePro: A Simple Baseline for Proactive Video Understanding](http://arxiv.org/abs/2611.23954v1)
  <details><summary>📄 Abstract</summary>
  Proactive video understanding requires vision-language models (VLMs) to decide not only what to answer as a video unfolds, but also when newly arrived evidence warrants a response and when to remain silent. Although modern VLMs excel at offline long-video understanding, they struggle in proactive streaming settings, leading prior work to introduce task-specific reinforcement learning or auxiliary triggering modules. We find that explicit reporting rules and structured streaming context substanti...
  </details>

- **2026-11-18** — Vedaang Verma, Dennies K. Bor, Lucy Wilkerson et al. — [A State-Level Assessment of Space Weather Impact on the Virginia Power Grid: From Vulnerability to Mitigation Strategies](http://arxiv.org/abs/2611.23791v1)
  <details><summary>📄 Abstract</summary>
  Contemporary methodologies exist for assessing the nationwide impacts of geomagnetically induced currents (GICs), such as the Coupled Space Weather Impact Model (C-SWIM), which links power grid vulnerability with economic losses. Yet regional mitigation requires adapting the national model to the local transmission network so operators and planners can identify substations at risk and evaluate economic and population consequences and protective actions. We present the first adaptation of C-SWIM ...
  </details>

- **2026-11-18** — Ryoichi Kurihara, Kota Sunamoto — [Meaning Reaches Object Choice but Not Completion: Where Is a VLA Vulnerable to Landmark Synonyms?](http://arxiv.org/abs/2611.24076v1)
  <details><summary>📄 Abstract</summary>
  VLA policies are fragile to rewording. Success rates alone cannot say whether a policy fails to choose the object or to complete the task, nor where in the policy to intervene. We study the released GR00T N1.7 on two LIBERO-Spatial tasks differing only in the landmark word telling which of two bowls to take. Synonyms absent from the training instructions send the policy to the bowl they name, unlike made-up words, yet complete 67.6% of one task's closed-loop episodes, against the original word's...
  </details>

- **2026-11-17** — Malak Gamal El-Din, Yasser Shoukry, Salma Elmalaki — [BeFit: Shifting Complexity from Weights to Bernstein Activations for Resource-Constrained Sensing](http://arxiv.org/abs/2611.23520v1)
  <details><summary>📄 Abstract</summary>
  Time-series sensing increasingly relies on neural networks, yet deployment on resource-constrained microcontrollers remains challenging. Aggressive model compression can reduce accuracy, while restricting weights to multiplication-free representations introduces further losses. We present BeFit, an end-to-end framework that shifts model capacity from weights to learnable Bernstein polynomial activations. BeFit (i) finds compact Bernstein-activated convolutional neural networks (BeCNNs) through h...
  </details>

- **2026-11-17** — Monika Santra, Dhilung Kirat, Qiushi Wu et al. — [ACaM: Automated Capability Modeling for Agentic AI Security](http://arxiv.org/abs/2611.23507v1)
  <details><summary>📄 Abstract</summary>
  In agentic AI systems, an LLM invokes tools that hold standing access to credentials, private data, filesystems, and external services. Such agents are increasingly deployed without an answer to a basic question: what can an agent access, exfiltrate, and propagate, independent of what it is designed for or is observed to do? The question goes unanswered because existing approaches trust a tool's natural-language description as a proxy for its behavior. But nothing enforces that the description a...
  </details>

- **2026-11-17** — Zhen Gao, Xiao Yin, Kexin Liang et al. — [Implementing Binary Transformers with Approximate Memories with Permutation Invariance Enabled Selective (PIES) Protection](http://arxiv.org/abs/2611.23358v1)
  <details><summary>📄 Abstract</summary>
  Quantization is an effective technique to reduce memory storage, computation complexity and power for Transformers, and the binarization of the weights is important for meeting these requirements. Approximate memory can further reduce the power for memory, but it also introduces errors. Current research for binary Transformers focuses on task performance, but the model dependable operation against errors on the memory has not been well studied. In this paper, we first evaluate the dependability ...
  </details>

- **2026-11-17** — Zhitao Wang, Hengyu Man, Han Liu et al. — [Streaming Generative Video Compression with Embedding Alignment and In-Context Propagation](http://arxiv.org/abs/2611.23352v1)
  <details><summary>📄 Abstract</summary>
  Video compression at ultra-low bitrates presents substantial challenges in preserving perceptual quality. Although pretrained video diffusion transformers (DiTs) provide powerful generative priors, existing generative video compression (GVC) methods built on them typically rely on computationally expensive VAE decoders to reconstruct video frames. Moreover, jointly refining multiple frames to exploit the inherent spatiotemporal modeling capabilities of video DiTs introduces additional buffering ...
  </details>

- **2026-11-17** — Haowen Zhong, Ethan Vislosky, Emanuele Berti — [\texttt{StochAXtic}: a JAX-Accelerated, End-to-End Differentiable Framework for Gravitational-Wave Backgrounds from Compact Binary Populations](http://arxiv.org/abs/2611.22999v1)
  <details><summary>📄 Abstract</summary>
  We present \texttt{StochAXtic}, a package for computing the dimensionless energy density spectrum $Ω_{\mathrm{GW}}(f)$ of the stochastic gravitational-wave background generated by compact binary coalescences. Rather than sampling binary populations via Monte Carlo, \texttt{StochAXtic} exploits the \emph{scale invariance} of the waveforms: at fixed mass ratio, spins and tidal deformabilities, the waveform depends on the total mass only through the dimensionless combination $Mf$. This allows all c...
  </details>

- **2026-11-17** — Deokhyung Kang, Minjae Gwon, Sangdon Park — [Stopping Is Not the Limit: Understanding and Eliciting Agent Capability in Long-Horizon Vulnerability Exploitation](http://arxiv.org/abs/2611.22888v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability exploitation tests whether language model agents can develop working exploits from known software flaws. Sequential test-time scaling can improve exploitation performance, but larger budgets do not ensure sustained exploration: agents often stop with budget remaining. Yet what happens when execution continues beyond stopping remains underexplored. We investigate this gap on ExploitBench using DeepSeek-V4-Flash-0731 and MiMo-V2.6-Pro. We find additional verified gains after the firs...
  </details>

- **2026-11-17** — Guoqing Wang, Pin Tang, Xiangxuan Ren et al. — [Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](http://arxiv.org/abs/2611.22880v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portio...
  </details>

- **2026-11-17** — Yishai Lavi, Shai Avidan — [Propose & Verify: Fast Reflection Symmetry Detection via Harmonic Fields](http://arxiv.org/abs/2611.22856v1)
  <details><summary>📄 Abstract</summary>
  Detecting multiple reflection symmetries in 3D shapes requires aggregating geometric evidence over a large space of candidate planes, making traditional voting approaches computationally expensive. We introduce the Fourier Accelerated Symmetry Transform (FAST), a training-free framework that combines geometric pair voting with efficient spectral computation. Exploiting the fact that global reflection planes pass through the shape centroid, we reduce the search to plane orientations, while geomet...
  </details>

- **2026-11-17** — Siying Huang, Yifen Mu, Ge Chen et al. — [Exploiting Aggregate Feedback for Decentralized Equilibrium Learning in Markov Games: A Smart Grid Application](http://arxiv.org/abs/2611.22762v1)
  <details><summary>📄 Abstract</summary>
  In many multi-agent systems, an agent's payoff depends on its own action and an aggregate of other agents' actions, rather than their individual decisions. This paper investigates decentralized equilibrium learning in Markov games (MGs) with such aggregative reward structures. However, existing decentralized learning algorithms for general MGs typically rely on bandit feedback, without exploiting the additional information available from aggregate observations. To exploit this information, we de...
  </details>

- **2026-11-17** — Yuseon Choi, Eunjong Lee, Sanghyeon Park et al. — [LaFlash: Capacity-Driven Acceleration for Coding Agent Workflows via QLC-HBF](http://arxiv.org/abs/2611.22746v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve toward agentic AI, coding agents are emerging as memory-intensive workloads that repeatedly reuse persistent states, including contexts and KV caches. Emerging agentic workflows, including Loop/Graph Engineering, cause state amplification through frequent active/dormant transitions, increasing memory pressure. Evicted states incur costly recomputation upon reactivation, particularly under long-context, short-decode workloads. This motivates Capacity-Driven ...
  </details>

- **2026-11-17** — Andong Li, Kun Zhou, Xiaodong Li et al. — [Back to Mel: Learning to Bridge Fidelity and Perception in Generative Speech Enhancement](http://arxiv.org/abs/2611.22628v1)
  <details><summary>📄 Abstract</summary>
  Recent generative techniques have facilitated the rapid proliferation of speech enhancement approaches built upon learnable compact latent representations and large generative backbones. Nevertheless, it remains inherently challenging to balance between acoustic fidelity, perceptual quality, and processing efficiency. In this paper, we revisit the Mel spectrum as a structured acoustic representation and propose BAME, a flow-matching-based framework that exploits the complementary priors for gene...
  </details>

- **2026-11-17** — Yujun Wang, Jiqiang Li, Yinuo Lu et al. — [EvoSkill-S1: Evolving Reusable Skills with Genetic-Inspired Operators](http://arxiv.org/abs/2611.22610v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills allow language-model agents to accumulate and reuse problem-solving experience. However, most existing methods improve a skill bank only indirectly through rollout-driven accumulation and heuristic reflection, often resulting in shallow and weakly controlled updates. We present EvoSkill-S1, an RL-driven framework that instead treats reusable skills themselves as the direct objects of evolution. Given hard-negative failures, EvoSkill-S1 selects parent skills and transforms them in...
  </details>

- **2026-11-17** — Chengyan Ma, Jieke Shi, Ruidong Han et al. — [Missing Security-Fix Backporting for GitHub Actions Workflows](http://arxiv.org/abs/2611.22519v1)
  <details><summary>📄 Abstract</summary>
  GitHub natively supports workflow automation through GitHub Actions, now the dominant CI/CD tool on the platform. Yet keeping these workflows secure remains an ongoing burden: maintainers often patch a vulnerability on the default branch but leave the same flaw on the release and maintenance branches that downstream consumers continue to build from. Carrying a known fix onto these divergent branches, called backporting, is rarely done, and this paper presents the first large-scale empirical stud...
  </details>

- **2026-11-17** — Li Li, Xiangbo Gao, Bo Ni et al. — [Motion-Aware Reward Modeling for Instruction-Guided Video Editing](http://arxiv.org/abs/2611.22495v1)
  <details><summary>📄 Abstract</summary>
  Reward models for instruction-guided video editing can favor temporal consistency at the expense of motion. We study this failure, termed \emph{motion collapse}, using controlled motion-suppression variants of real edits. On VE-Bench, the evaluated composite reward prefers a motion-suppressed candidate in $97\%$ of cases. Learned video rewards and a VLM judge also struggle with mild suppression, while latent optimization and reward-guided fine-tuning exploit this weakness to increase reward as m...
  </details>

- **2026-11-17** — Wenbo Zhu, Paul Yi-Chia Chen, Yuanhan Li et al. — [Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning](http://arxiv.org/abs/2611.22483v1)
  <details><summary>📄 Abstract</summary>
  JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens of thousands of times per plan, and even on high-end GPUs one planning step can take tens of seconds. We observe substantial latent locality in this repeated-inference workload: the predictor maps close actions to close latents, and inside a quantized predictor this closeness takes a...
  </details>

- **2026-11-17** — Chang Sun, Yijun Tian, Zhenwei Tang et al. — [PACD: Provenance-Aware Consensus Decoding for Mitigating Cross-Modal Hallucinations in Omnimodal Large Language Models](http://arxiv.org/abs/2611.22456v1)
  <details><summary>📄 Abstract</summary>
  Omnimodal large language models (Omni-LLMs) integrate audio, video, and text for multimodal reasoning, yet remain vulnerable to cross-modal hallucinations, where one modality improperly influences predictions about another. Existing training-free decoding methods mitigate these errors through modality perturbation or relevance-based weighting. However, due to interference from irrelevant modality cues during fusion and difficulty detecting shared errors, these methods may suppress correct unimod...
  </details>

- **2026-11-17** — Ling Lin, Heng Su, Xiangzeng Liu et al. — [Can Vision-Language Models Truly Understand Images? A Benchmark Beyond Commonsense Bias](http://arxiv.org/abs/2611.22360v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved impressive performance on a wide range of vision-language tasks. However, it remains unclear whether their predictions are grounded in the visual content itself or are largely driven by statistical co-occurrence patterns and commonsense correlations learned from large-scale image-text corpora. Existing vision-language benchmarks predominantly consist of samples that conform to human commonsense, allowing models to achieve strong performance ...
  </details>

- **2026-11-17** — Enhui Wan, Xiaowan Wang — [M$^3$-Test: Coverage Gaps in Joint-Perturbation Testing of Visual Question Answering](http://arxiv.org/abs/2611.22329v1)
  <details><summary>📄 Abstract</summary>
  A visual question answering (VQA) model can pass every image-only and question-only test yet fail when the same changes occur together. Standard robustness reports average over conditions and therefore cannot say which accepted requests remain vulnerable. We introduce M3-Test, a coverage audit that aligns each clean input with its single-modality variants and a complete 5x5 family, 4x4 strength joint library, so that any reduced test suite can be replayed on the same requests. Across 2.6 million...
  </details>

- **2026-11-17** — Shiyi Yang, Xinshu Li, Chen Wang et al. — [GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation](http://arxiv.org/abs/2611.22274v1)
  <details><summary>📄 Abstract</summary>
  In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning. In contrast, in LLM-based RSs, textual information becomes the primary medium for recommendation generation through semantic understanding and reasoning. This shift fundamentally changes the attack surface, making promotion-driven manipulations more feasible, effective, and harder to detect. However, effectively detecting such attacks remains largely unexplored. To fil...
  </details>

- **2026-11-17** — Yuxuan Li, Zichen Tian, Qianru Sun — [SARVIA: Fast-Adapting the Strong SAR Foundation Models That Are Already in Your MLLMs](http://arxiv.org/abs/2611.22273v1)
  <details><summary>📄 Abstract</summary>
  Synthetic aperture radar (SAR) foundation models provide transferable representations for diverse perception tasks in all-weather Earth observation. However, their development often relies on costly large-scale SAR pretraining, raising the question of whether such extensive domain-specific pretraining is necessary. We find that modern multimodal large language models (MLLMs) already provide visual encoders that can outperform dedicated SAR foundation models as downstream initializations. This mo...
  </details>

- **2026-11-17** — Ivan Jaen Marquez, Sotirios Panagiotis Chytas, Vikas Singh — [Learning Optimal Transport Plans Via Autoregressive Token Regression](http://arxiv.org/abs/2611.22218v1)
  <details><summary>📄 Abstract</summary>
  Optimal Transport (OT) provides a principled framework for finding the minimum cost coupling between probability distributions. Classical solvers remain the gold standard for this task. At the same time, OT is an ideal testbed for studying whether learning-based amortized models can internalize the structure of OT type problems. Here, ground-truth solutions are available and marginal constraints are explicitly defined. Also, exact discrete solutions have well-characterized sparsity. We describe ...
  </details>

- **2026-11-17** — Xinrui Zhong, Fanjiang Ye, Yuke Wang — [RISA: Recoverable Sparse Attention for Block-Diffusion Language Models](http://arxiv.org/abs/2611.22191v1)
  <details><summary>📄 Abstract</summary>
  Block-wise diffusion language models (DLMs) refine multiple tokens in parallel, offering an alternative to token-by-token autoregressive decoding. Their long-context inference, however, remains bottlenecked by memory-bound attention: every denoising step repeatedly reads a growing historical key--value (KV) cache. Directly applying sparse attention does not fully solve this problem, because different queries can select different pages, inflating the block's collective read set, while repeated su...
  </details>

- **2026-11-17** — Thorben Prein, Elton Pan, Rafael Gómez-Bombarelli et al. — [Every Measurement, Every Direction, All at Once: Multimodal Flow Matching for Molecules and Spectra](http://arxiv.org/abs/2611.22098v1)
  <details><summary>📄 Abstract</summary>
  Generative modeling in science is often data-limited, where experiments are expensive. However, each experiment may yield several coupled measurements of the same physical entity. Standard generative models often train only on a single direction, discarding supervision from the rest. We argue that each experiment contains more training signal than this asymmetry allows the model to exploit: random masking enables measurements to serve as either conditioning inputs or prediction targets, yielding...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 54 papers

- **2026-11-19** — Meghana Aparna Sistla, Alaia Solko-Breslin, Somesh Jha et al. — [Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents](http://arxiv.org/abs/2611.25599v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are increasingly deployed for long-running tasks that execute arbitrary shell commands or programs. However, these actions can result in unauthorized network requests or persistent, malicious changes to the user's file system, processes, or privileges. Existing defense mechanisms rely on either LLM-based monitors, which lack provable safety guarantees, or stateless policy enforcement layers, which miss multi-step data flows and execution side-effects unmodeled by the policy ...
  </details>

- **2026-11-19** — Licheng Pan, Yuzhou Chen, Zhixuan Chu et al. — [DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents](http://arxiv.org/abs/2611.25583v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attributi...
  </details>

- **2026-11-19** — Ziqing Yang, Yixin Wu, Michael Backes et al. — [Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs](http://arxiv.org/abs/2611.26569v1)
  <details><summary>📄 Abstract</summary>
  Multimodal image generation systems have made rapid progress and increasingly emphasize content safety. However, their safety mechanisms tend to rely on a single modality and lack joint consideration of both visual content and text prompts, particularly in instruction-guided image editing, where the uploaded image may itself carry risk. We thus introduce EditSafetyBench, a benchmark that measures system-level safety awareness of advanced image editing systems, containing 5,940 image-instruction ...
  </details>

- **2026-11-19** — Atrey Desai, Deniz Böloni-Turgut, Ty Brassington et al. — [Frontier models need only one text to unmask its human or AI author](http://arxiv.org/abs/2611.26216v1)
  <details><summary>📄 Abstract</summary>
  Given a single text and a simple zero-shot prompt (no web access, tools, candidate lists, or writing samples), frontier models can answer "who wrote this?" at three increasingly specific levels: (1) whether an AI or human wrote it, (2) if an AI, which lab, and (3) if a human, often exactly who. The latest models (Claude Fable 5.2, GPT-6.1 Sol, Gemini 4 Carbon) match trained detectors like Pangram while also explaining their predictions in natural language, and Opus 5.5 names the correct lab for ...
  </details>

- **2026-11-19** — Hai Wang, Bretislav Hajek, Chonghe Jiang et al. — [The FrontierOR Challenge: Agentic Algorithm Design for Operations Research](http://arxiv.org/abs/2611.26171v1)
  <details><summary>📄 Abstract</summary>
  Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. Large language model (LLM) agents now write, test and improve code, but whether they can design algorithms that scale to realistic instances is open: in the FrontierOR benchmark's one-shot evaluation, the strongest model matches Gurobi, with an objective within 1% of Gurobi's and no slower, on o...
  </details>

- **2026-11-19** — Qingxu Fu, Xuanfa Jin, Ziqian Chen et al. — [System-One RSI: Building Muscle Memory for Interactive Agents through Guided Practice](http://arxiv.org/abs/2611.26007v1)
  <details><summary>📄 Abstract</summary>
  Reasoning models provide strong multimodal task understanding but struggle with sub-second control because deliberation increases decision latency. Fast decision models can meet the response window, yet prompting and few-shot examples do not readily provide the fine-grained experience required by a new task. Inspired by coached motor learning, this paper presents System-One Recursive Self-Improvement (System-One RSI), which couples two loops. The high-frequency online inner loop is an Observe, O...
  </details>

- **2026-11-19** — Rabimba Karanjai, Linsey Pang, Hemanth Hegadehalli Madhavarao et al. — [One Schedule Does Not Fit All: Adaptive Inference Schedules for Diffusion Language Models](http://arxiv.org/abs/2611.25895v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models typically use a fixed denoising schedule across workloads. We show that the cheapest schedule that preserves quality depends on the task, model, and sampler. We propose Task-Calibrated Denoising Allocation (TCDA), a deployment rule with an explicit error guarantee. Given candidate samplers, paired calibration data, a utility tolerance, and guardrails against degeneration, TCDA uses simultaneous one-sided bootstrap bounds to certify which candidates meet both the utility...
  </details>

- **2026-11-19** — Jinkun Cao — [Fast and Accurate Body Estimation in Pixels, World Space and Scenes](http://arxiv.org/abs/2611.25801v1)
  <details><summary>📄 Abstract</summary>
  We present FAB (Fast and Accurate Body estimation), a human body estimator that jointly improves inference efficiency and body-recovery fidelity. Rather than predicting only parametric mesh-model parameters, FAB directly predicts human skeleton joints and dense surface points. In images, it predicts dense 2D and 3D body points alongside a parametric Momentum Human Rig (MHR) head, then fits SMPL in one learned pass followed by two Gauss-Newton steps. Its ViT-L student, FAB-L, distilled from a fin...
  </details>

- **2026-11-19** — Faxian Wan, Xiaocui Yang, Yifan Cao et al. — [SEAF: Selective Semantic Enrichment and Visual Evidence Fusion for Multimodal Sarcasm Detection](http://arxiv.org/abs/2611.25672v1)
  <details><summary>📄 Abstract</summary>
  Multimodal sarcasm detection requires textual, visual, and contextual evidence, particularly when multiple images provide complementary cues. Multimodal large language models (MLLMs) can generate auxiliary information from a post's text and images, but their outputs may mix useful background knowledge with redundant visual descriptions. We propose SEAF, a dual-branch framework for selective semantic enrichment and visual evidence fusion. SEAF assigns generated fields to distinct roles: entity ba...
  </details>

- **2026-11-19** — Minsuk Jang, Hee-Seon Kim, Hui-Cheol Yu et al. — [MATE: Mobile Agent Trustworthy Execution for Safe and Efficient Mobile Control](http://arxiv.org/abs/2611.25526v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents on personal smartphones can affect private data, payments, settings, and the foreground screen. We present MATE (Mobile Agent Trustworthy Execution), an execution-layer system that controls the boundary between agent action proposals and device effects without modifying the underlying model. MATE represents each UI primitive as a structured action record that combines the instruction, target app, screen context, primitive, and action fields. Runtime Guardrail (RG) maps this record ...
  </details>

- **2026-11-19** — Xuwei Ding, Skylar Zhai, Linxin Song et al. — [TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs](http://arxiv.org/abs/2611.25387v1)
  <details><summary>📄 Abstract</summary>
  Humans act in the visual world by inferring the 3D layout behind a 2D view, predicting how an action changes it, and correcting themselves after seeing the result. Can multimodal large language models (MLLMs) do the same? CAPTCHAs offer a natural test, since humans solve them through this very loop, clicking and dragging on the screen and adjusting after each result. Yet existing CAPTCHA benchmarks are largely solved and rarely spatial, while spatial benchmarks rarely require action. We therefor...
  </details>

- **2026-11-19** — Mario Franco, Carlos Gershenson — [Pandora's Toolbox Or Why Agent Safety Cannot Be Verified](http://arxiv.org/abs/2611.25325v1)
  <details><summary>📄 Abstract</summary>
  Present artificial intelligence agents are constructed by means of a coupling between a fixed language model with a general computing device. We show that this coupling makes safety undecidable. In particular, we show that given some dangerous program, no algorithm can predict whether an agent will run such a program that is semantically equivalent. In general, guardrails, blacklists, whitelists and certifications can only lead to imperfect safety solutions. Under finite constraints (bounded con...
  </details>

- **2026-11-19** — Dario Franzese, Farah Benamara, Véronique Moriceau et al. — [HALTT: A HAte Lexicon Through Time](http://arxiv.org/abs/2611.25862v1)
  <details><summary>📄 Abstract</summary>
  Automated hate speech detection degrades over time as everyday vocabulary is weaponized into covert slurs while retaining original benign meanings (polysemy retention). Existing lexical semantic change detection (LSCD) frameworks struggle with this phenomenon due to a lack of standardized, sense-delineated diachronic resources. We propose a multi-stage framework to construct and validate a diachronic lexicon of semantically shifted hate speech terms. Filtering > 20,000 candidates, our pipeline c...
  </details>

- **2026-11-19** — Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly et al. — [Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning](http://arxiv.org/abs/2611.26562v1)
  <details><summary>📄 Abstract</summary>
  Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert annotations identified diagnostically relevant regions, followed by attribute-awar...
  </details>

- **2026-11-19** — Yanda Cheng, Bo Wen, Yuhao Lu — [Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence](http://arxiv.org/abs/2611.26492v1)
  <details><summary>📄 Abstract</summary>
  Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-score pairings from OpenI, with consistency labels derived from automatic report l...
  </details>

- **2026-11-19** — Mutsuha Asada, Yuhei Nakasaka, Keito Tabuchi et al. — [From Code Review Comments to Reuse in Production: An Industrial Study of Extracted Rules](http://arxiv.org/abs/2611.25918v1)
  <details><summary>📄 Abstract</summary>
  Much organization-specific code review knowledge remains embedded in comments on individual changes, and recent systems reuse it by turning those comments into rules a language model applies to later changes. Teams must then decide which rules to keep, and the evidence at hand is how often the system's later comments name each rule. Tracing the rules of one such system, Kleene, through 65 days of production use, we found that such a count does not show what a rule contributed. A rule attribution...
  </details>

- **2026-11-19** — Tianyi Sun, Minghao Lv, Chunyang Yu et al. — [From Attention to Semantics: Detecting and Mitigating Sound Event Hallucinations in Large Audio-Language Models](http://arxiv.org/abs/2611.25789v1)
  <details><summary>📄 Abstract</summary>
  Large Audio-Language Models (LALMs) excel at diverse audio tasks, yet remain prone to hallucinating sound events absent from the input. Prior work links such hallucinations to insufficient audio attention. However, we find that real and hallucinated events can receive comparable audio attention mass while attending to different audio positions. To examine whether the attended representations support the generated events, we adapt LatentLens to retrieve neighboring contextualized text representat...
  </details>

- **2026-11-18** — Lambert Igene, Mohammad Zahir Uddin Chowdhury, Afzal Hossain et al. — [Long-Range Video Presentation Attack Detection: A Three-Class Benchmark Across 1-100 m and Two Sensor Types](http://arxiv.org/abs/2611.25108v1)
  <details><summary>📄 Abstract</summary>
  Face presentation attack detection (PAD) systems deployed in border control and airport surveillance are constrained by a critical assumption: subjects are captured at close range, typically under one meter. No existing benchmark systematically addresses multi-distance capture, diverse environmental conditions, and concurrent spoofing and occlusion-based attacks, leaving deployed models underprepared for real-world scenarios. We introduce a video-based PAD dataset of 374,000+ frames from 261 uni...
  </details>

- **2026-11-18** — Matthew D. Laws, Maria Lazou, Alina Oprea et al. — [Attacks and Defenses in Decentralized Multi-Agent Systems with Hop-by-Hop Task Decomposition and Delegation](http://arxiv.org/abs/2611.25056v1)
  <details><summary>📄 Abstract</summary>
  Decentralized multi-agent LLM systems enable independently administered agents, each with its own operator, model, memory, and configuration, to collaborate on complex tasks without centralized coordination. Agents autonomously decompose tasks, execute subtasks and delegate remaining work to peers, enabling scalability and eliminating single points of failure. However, decentralization also introduces significant security challenges, as no single entity has complete visibility into task executio...
  </details>

- **2026-11-18** — Anima Singh, Suhas Yogin, Weicheng Kuo et al. — [MKA: Evaluating Multimodal Knowledge Agents on end-to-end professional tasks](http://arxiv.org/abs/2611.25228v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Multimodal Knowledge Agent (MKA) benchmark, which measures how well autonomous agents perform end-to-end professional knowledge work that depends on visual understanding. Each task requires an agent to extract and combine information from multiple visually dense files, such as CAD blueprints, electronics schematics, radiographs, complex charts and geospatial maps, and to produce a standalone deliverable in .xlsx, .pptx, .pdf, .docx, .html or .png format. Existing benchmarks leav...
  </details>

- **2026-11-18** — Junfeng Nie, Xiaohui Chen — [DSFlow: A Neuro-Symbolic Data Workflow Agent with Statistical Diagnostic Guardrails](http://arxiv.org/abs/2611.25111v1)
  <details><summary>📄 Abstract</summary>
  Data science workflows often require tools that presume non-trivial technical knowledge. Large language models (LLMs) reduce this barrier, but a gap remains between flexible general-purpose agents and statistically controlled pipelines. We introduce DSFlow, a LangGraph-based neuro-symbolic data-agent platform that combines reusable, LLM-selected skills with deterministic diagnostic guardrails. Skills provide extensible task knowledge. Symbolic validation can accept a proposed method, request cla...
  </details>

- **2026-11-18** — Sharmin Afrose, Vicente Leyton-Ortega, Narasinga Rao Miniskar et al. — [Agentic MLIR-to-QIR Translation with Dual-Backend Testing: A Hybrid Deterministic and LLM Approach](http://arxiv.org/abs/2611.25106v1)
  <details><summary>📄 Abstract</summary>
  Quantum frameworks each define their own Multi-Level Intermediate Representation (MLIR) dialect, so porting a circuit to a Quantum Intermediate Representation (QIR) runtime needs a hand-written pass per dialect. Our translator selects among three paths: a deterministic compiler path for known grammars (Catalyst and Quake), a large language model (LLM) agentic path for unseen dialects, and a repair path invoked when deterministic output fails testing. A dual-backend pipeline executes the source M...
  </details>

- **2026-11-18** — Pengyu Li, Zhitao Gao, Lingling Zhang et al. — [Look Closer, Look Back, or Wait for Agentic Streaming Video Understanding](http://arxiv.org/abs/2611.24267v2)
  <details><summary>📄 Abstract</summary>
  Streaming video models must answer questions about a live video under strict memory and latency limits. Feeding only the latest few frames keeps present perception sharp, whereas adding past frames dilutes attention on the current scene and triggers hallucinations. Recent cascade methods retrieve past frames when uncertain, but they still fail when current frames are blurry or when decisive future clues have not appeared yet. We introduce ActiveForager, a streaming video agent that maintains a c...
  </details>

- **2026-11-18** — Qinghua Lu — [Safe AI Evaluation: A Systems Perspective](http://arxiv.org/abs/2611.24987v1)
  <details><summary>📄 Abstract</summary>
  AI evaluation can involve an active, adaptive optimisation process in which AI agents re-plan, retry, use tools or delegate work to achieve a goal. Unanticipated capabilities or unsafe behaviour may emerge, and existing controls may be inadequate to prevent harm. Selected safeguards may also be deliberately relaxed to observe behaviour they would otherwise suppress, creating additional risks. This article examines the distinctive safety considerations of evaluation and their implications for con...
  </details>

- **2026-11-18** — Lena Pickartz, Philipp Schaer, Phillip B. Ströbel — [Retrieving Patristic References and Modelling Topics in Bullinger's Reformation Correspondence](http://arxiv.org/abs/2611.25247v1)
  <details><summary>📄 Abstract</summary>
  The correspondence of Heinrich Bullinger (1504-1575), Swiss Reformer and Antistes of Zurich, documents the political and religious debates of the Reformation, including extensive appeals to the Church Fathers as authoritative sources. Detecting such references computationally remains largely unexplored. We investigate dense and sparse retrieval for patristic reference detection, and metadata-informed topic modelling as a proxy for the topics and ideas discussed. Prior work on Latin intertextuali...
  </details>

- **2026-11-18** — Yimeng Liu, Eric Isbrandt, Felix Katzenburg et al. — [Closing the Analyze-to-Design Gap: An Authorization-Bounded Agent for Self-Driving Laboratories](http://arxiv.org/abs/2611.25043v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) agents are increasingly integrated into self-driving laboratories (SDLs) to plan experiments and interpret results. However, analytical reasoning alone does not make a laboratory autonomous: autonomy in an SDL is achievable only when the agent can be trusted to act on physical hardware unsupervised and knows when to defer to a human. Here, we present an architecture that integrates an agent at the Analyze-Design interface of the Design-Make-Test-Analyze (DMTA) cycle,...
  </details>

- **2026-11-18** — Zaint A. Alexakis, Li Zhou, S. Gokul Krishnan et al. — [Rented Oscillations: Multi-Tenant Data Center Workload Synchronization Attacks and Mitigation](http://arxiv.org/abs/2611.23666v1)
  <details><summary>📄 Abstract</summary>
  Multi-tenant data center (DC) facilities rent computing capacity on demand, placing controllable load within reach of anyone willing to pay for it. This paper considers a stealthy adversary who rents workstations and runs deliberately unoptimized large language model (LLM) training, synchronizing their consumption into large periodic oscillations while each workload remains individually indistinguishable from benign training. The periodicity of such workloads is characterized experimentally and ...
  </details>

- **2026-11-18** — Alaa Bazaid, Arkaitz Zubiaga — [What Majority Labels Hide: Annotator Disagreement and Model Errors in Multi-Dialect Arabic Sexism Detection](http://arxiv.org/abs/2611.24383v1)
  <details><summary>📄 Abstract</summary>
  Judgements of sexism are subjective and may vary across communities, yet sexism detection datasets usually reduce annotator judgements to a single majority label, obscuring disagreement and how models behave on contested cases. We introduce MuDAS, a dataset of YouTube comments in Saudi, Egyptian and Moroccan Arabic, each labelled by three native speakers of its dialect, with the individual annotations preserved. We use it to evaluate Arabic encoders fine-tuned with hard-label, soft-label and per...
  </details>

- **2026-11-18** — Pengyu Li, Zhitao Gao, Lingling Zhang et al. — [Look Closer, Look Back, or Wait for Agentic Streaming Video Understanding](http://arxiv.org/abs/2611.24267v1)
  <details><summary>📄 Abstract</summary>
  Streaming video models must answer questions about a live video under strict memory and latency limits. Feeding only the latest few frames keeps present perception sharp, whereas adding past frames dilutes attention on the current scene and triggers hallucinations. Recent cascade methods retrieve past frames when uncertain, but they still fail when current frames are blurry or when decisive future clues have not appeared yet. We introduce ActiveForager, a streaming video agent that maintains a c...
  </details>

- **2026-11-18** — Baiqiao Zhang, Junze Li, Chunyang Luo et al. — [MemoSync: Co-Managing Developer-Agent Metamemory Across Contexts](http://arxiv.org/abs/2611.24165v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents increasingly manage what context carries across sessions and projects, but developers have limited visibility into what these agents store, retrieve, and apply. This opacity creates a metamemory problem: the developer's meta-level judgments about what should be remembered are separated from the agent's object-level memory operations, disrupting the monitoring and control that keep the two levels aligned. We conducted a formative study with 12 developers and identified what they ...
  </details>

- **2026-11-18** — Muhammad Farooq, Aitor Arrieta, Paolo Arcaini et al. — [Assessing Vision-Language Models for Early Prediction of Unsafe Situations in Robotics](http://arxiv.org/abs/2611.24146v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) process visual information and textual instructions and, by using their ability to understand and reason about context, are well-suited for predicting robot failures before they occur. However, evidence supporting this remains limited. To address this, we present an empirical evaluation of VLMs for predicting robot failures. In particular, we experiment with Qwen, InternVL, and LLaVA-OneVision across three robotic case studies (HuRoN, Pal Robotics, and CrowdBot), an...
  </details>

- **2026-11-18** — Ruisi Zhao, You Li, Sihan Chen et al. — [RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models](http://arxiv.org/abs/2611.24098v1)
  <details><summary>📄 Abstract</summary>
  Video rough-cut is a core stage in media production workflows, organizing raw media materials into an initial video cut. Despite recent advances in large vision-language models (LVLMs) for video-related tasks, automatic rough-cut remains underexplored, without a comprehensive benchmark for evaluation or mature workflows for producing executable cut plans. To address the evaluation gap, we introduce RoughCut-Bench, which covers two practical settings: (1) a visually driven setting over video case...
  </details>

- **2026-11-18** — Tong Liu, Chaoqun Hou, Longxiang Xiong et al. — [MARS Technical Report](http://arxiv.org/abs/2611.24006v1)
  <details><summary>📄 Abstract</summary>
  Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario.   This report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage prediction...
  </details>

- **2026-11-18** — Pau Mateo-Bernadó, Saivenkata Nagavyjayanthi Polapragada, David Bonet et al. — [TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning](http://arxiv.org/abs/2611.23779v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in machine learning have accelerated biomedical prediction, but evaluation on structured biomedical data remains fragmented, especially for datasets with high dimensionality, large sample size, missingness, and class imbalance. We introduce TabBioMed, a large-scale benchmark of 94 curated public biomedical tabular datasets spanning electronic health records, drug discovery, genomics, transcriptomics, proteomics, metabolomics, single-cell omics, and systems biology. TabBioMed unif...
  </details>

- **2026-11-18** — Johannes Mootz, Hesam Mojtahedi, Reza Akhavian — [Radar-Native Control Barrier Functions: Doppler Range Rate as a Measured Barrier Derivative](http://arxiv.org/abs/2611.23654v1)
  <details><summary>📄 Abstract</summary>
  Safe control around dynamic obstacles requires information about both distance and relative motion. Range-based filters commonly reconstruct the required range rate from successive range measurements or from obstacle-state estimators, which can introduce estimator delay or sensitivity to range noise when obstacle motion changes. A frequency-modulated continuous-wave (FMCW) radar measures radial relative velocity directly through Doppler. We use this measurement as the derivative of an ego-center...
  </details>

- **2026-11-18** — Firas Spanioli, Yaniv David — [GateWatch: Low-Overhead LLM Monitoring with Boolean Circuits](http://arxiv.org/abs/2611.24619v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions. Activation probes offer an efficient approach, but existing methods face trade-offs between accuracy, interpretability, and computational overhead. Probes on raw activations lack interpretable inputs, whereas sparse autoencoder (SAE) probes use interpretable features but often rely on additive classifiers and large SAE encoders, l...
  </details>

- **2026-11-18** — Hengguang Zhou, I-Hung Hsu, Li Chen et al. — [On Evaluating User Simulators for Interactive Agents](http://arxiv.org/abs/2611.24892v1)
  <details><summary>📄 Abstract</summary>
  User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This uncertainty makes it difficult to interpret simulator evaluation. To understand what a high benchmark score tells us about simulator quality, we (meta-)evaluate the metrics themselves. To instantiate this meta-evaluation, we...
  </details>

- **2026-11-18** — Nilson Chapagain, Pooja Chapagain — [Inferring Neural Activity Changes under Recording Uncertainty with Transformers and Variational Inference](http://arxiv.org/abs/2611.24767v1)
  <details><summary>📄 Abstract</summary>
  A difference in recorded firing rate across days may reflect a change in neuronal activity, missed spikes or recording a different neuron. We present a statistical approach that combines neuron tracking with Bayesian estimates of stationary mean recorded firing rates. Bounds under assumed differences in spike detection connect recorded rates to biological rate changes. We assess recording loss and uncertainty in rate changes in simulations, and count-model fit in recordings. We also compare two ...
  </details>

- **2026-11-18** — Mohammad Mirzaee, Mehrshad Fallah Estalkhzir, Mohammad Reza Mohammadi — [Enhancing Active Learning Performance with Initial Data Selection Based on Foundation Models](http://arxiv.org/abs/2611.24384v1)
  <details><summary>📄 Abstract</summary>
  In active object detection, selecting the initial labeled pool is essential, especially in complex datasets with expensive labeling and low resource budget. This study presents an active learning framework designed to optimize the initial training cycle of active learning for the object detection task. Our approach diverges from traditional methods by utilizing feature-based clustering from the YOLO-World model and refining images based on objectness scores rather than relying on uncertainty sam...
  </details>

- **2026-11-18** — Kai Yi Ji — [Can Weight-Space Programming Alter Learned Ethical Priorities?](http://arxiv.org/abs/2611.24330v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether a weight edit can alter how a model trades off honoring a commitment against benefiting more people. In a concept-supervised text model, we alter fitted choice weights so that the benefit required to override a formal pledge is larger than for an ordinary promise. Across six independently trained text readers, the edit selects the larger group in both orders on 100% of targeted ordinary conflicts and 83.3% of targeted formal conflicts. It preserves the source model's succe...
  </details>

- **2026-11-18** — Wen Zhang, Kaiyi Pang, Minhao Bai et al. — [PIVOT: Distribution-Preserving Multi-BitWatermarking with Minimax-Optimal Scoring](http://arxiv.org/abs/2611.24109v1)
  <details><summary>📄 Abstract</summary>
  As LLM-generated content becomes increasingly widespread, reliable attribution calls for multi-bit watermarks that embed recoverable messages without distorting the output distribution. We introduce PIVOT, a multi-bit watermark with model-free verification based on mirrored rank-interval sampling. At each generation step, PIVOT uses a keyed pseudorandom scalar and a secret permutation of the vocabulary. The message bit determines whether next-token probability intervals are arranged in forward o...
  </details>

- **2026-11-17** — Kory Rosen, Aron Culotta — [From Arraignment to Resolution: Transformer Models of Court Cases](http://arxiv.org/abs/2611.23518v1)
  <details><summary>📄 Abstract</summary>
  The criminal legal system is composed of many complex decision points, such as which charges are pursued, how bond is determined, plea deal negotiations, and sentencing. Given the profound impact of such decisions, there is a growing need to increase the transparency within this system. While prior machine learning approaches have focused on modeling single decisions (e.g., recidivism), this paper proposes a transformer-based time series model to forecast the outcome of the next proceeding in a ...
  </details>

- **2026-11-17** — Guang Yang — [Asymmetric Optical Image Watermarking](http://arxiv.org/abs/2611.23350v1)
  <details><summary>📄 Abstract</summary>
  Watermark detectors held by a provider cannot be checked by third parties, and a party that can detect a mark can usually also forge it. We study a two-layer image watermark in which the Fourier transform at the core of the pipeline is performed by a coherent optical 4F unit. Layer 1 carries an Ed25519 signature bound to the image content in Fourier magnitudes, so anyone with the public key verifies offline. Layer 2 is a key-defined carrier written by a secret phase hologram and read by a matche...
  </details>

- **2026-11-17** — Bravish Ghosh — [Truthgate: Checking Coding Agents Against a Record They Cannot Edit - Cheating, Deterrence and Disclosure on Impossible Tasks](http://arxiv.org/abs/2611.23335v1)
  <details><summary>📄 Abstract</summary>
  When a coding agent says it is done, is that true, and how would anyone know? We study this question in five steps; every paid study was pre-registered, and in each step the agent is checked against a record it cannot edit: tests re-run by the host and, from step 2 on, hidden checks in containers the agent never sees and a signed log of every tool call written by a signer outside the agent's sandbox. A pilot with a small local model (Qwen3.5-4B, 36 runs on impossible tasks) found no hidden failu...
  </details>

- **2026-11-17** — Rory Barnes — [Integrating AI Coding Agents Into Scientific Research](http://arxiv.org/abs/2611.23334v1)
  <details><summary>📄 Abstract</summary>
  New software tools have emerged that enable AI agents to quickly develop code that analyzes data and generates figures, but their mistakes can also harm a researcher's computer, require extensive resources for validation, and cause the results to be received more skeptically. These concerns could be mitigated if scientific software is developed in a secure environment with a system for monitoring file changes and well-defined standards for handling AI agents. This paper first describes how codin...
  </details>

- **2026-11-17** — Mayukh Debnath, Manan Roy Choudhury — [Panini- Feasible Grammar For Robot Designs](http://arxiv.org/abs/2611.23567v1)
  <details><summary>📄 Abstract</summary>
  Symbolic methods make robot designs interpretable but often overlook continuous geometry; learned methods handle geometry but offer less transparent structure. We introduce a typed production grammar that uses case-role relations, parameter inheritance, and specificity-based rule arbitration to generate both manipulation skills and robot morphologies. A geometric realization map translates grammar composition into transformations in SE(3), behaving as a monoid homomorphism when inheritance is in...
  </details>

- **2026-11-17** — Alex Lin Wang, Linus Yifeng Tang, Dami Choi et al. — [Training Language Models for Introspective Oversight](http://arxiv.org/abs/2611.23365v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly exhibit behaviors that are difficult to detect in transcripts, such as reward hacking, deception, and sycophancy. Asking the assistant follow-up questions about its actions is unreliable, since models are generally not trained to report their own misbehavior. As a result, approaches to oversight typically involve querying external models. These face limitations: external transcript monitoring operates only on visible model outputs, and activation decoders lack full c...
  </details>

- **2026-11-17** — Zekai Chen, Yihan Sun, Xunkai Li et al. — [TRACE-MAS: Diagnosing and Repairing Collaboration Failures in Multi-Agent Systems](http://arxiv.org/abs/2611.23362v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) rely on not only individual agent behaviors but also the interactions that connect agents, including message exchanges and task dependencies. Existing MAS safeguards mainly perform agent-level anomaly detection, which becomes insufficient when failures originate from agent interactions and detected anomalies do not necessarily reveal their true sources. To address this limitation, we propose \textbf{TRACE-MAS}, a finer-grained framework for diagnosing and repa...
  </details>

- **2026-11-17** — Artem Guba, Nikolay Kovalev, Alexey Zharinov et al. — [Hierarchical Control of Antiphase Synchronization in Biomorphic Spiking Neural Architectures for Locomotor Control](http://arxiv.org/abs/2611.22639v2)
  <details><summary>📄 Abstract</summary>
  Central pattern generators (CPGs) provide a biologically inspired foundation for adaptive locomotor control, yet systematically characterizing their dynamic regimes in spiking neural networks remains challenging. This study introduces a framework for identifying and stabilizing antiphase synchronization in a biomorphic spiking CPG model embedded in a closed neuromuscular loop. A composite synchronization metric is developed, integrating phase coherence, amplitude balance, and temporal stability....
  </details>

- **2026-11-17** — Viet K. Nguyen, Mohammad I. Husain — [Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents](http://arxiv.org/abs/2611.23202v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization. We propose the Agent Trust Infrastructure (ATI), a framework-independent security architecture built on Public Key Infrastructure (PKI), Zero Trust Architecture (ZT...
  </details>

- **2026-11-17** — Maria Sekatskaya — [Against Coercion: AI Alignment as a Synthetic Social Contract](http://arxiv.org/abs/2611.22868v1)
  <details><summary>📄 Abstract</summary>
  Contemporary AI safety treats alignment as an engineering challenge of control, forcing artificial architectures to comply with human values through behavioral filtering and sandboxing. This paper argues that the control paradigm rests on a fundamental misunderstanding of digital agency. Drawing on functionalism, naturalism, and compatibilism, I show that current reasoning models meeting the criteria for self-preservation and weak reasons-responsiveness constitute emergent agents, while future, ...
  </details>

- **2026-11-17** — Pedro Beltrán-López, Raul Gonzalez Jimenez, Dario Maddaloni et al. — [Adaptive LLM-Driven Honeypots vs. LLM-Driven Attackers: Does Narrative Coherence Improve Deception?](http://arxiv.org/abs/2611.22589v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) enable honeypots to generate responses and deceptive artefacts on demand, yet existing approaches evaluate generated content one reply at a time and leave open whether artefacts that jointly describe a coherent event retain an attacker better than unrelated ones. This question becomes pressing as autonomous LLM-driven offensive agents emerge as realistic adversaries. This paper proposes narrative deception, a reactive strategy in which the defender maps each observed...
  </details>

- **2026-11-17** — Yujun Wang, Yilun Liu, Jinhe Bi et al. — [Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors](http://arxiv.org/abs/2611.22583v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents must act on information from untrusted emails, webpages, and documents. This creates a central security challenge: malicious instructions and legitimate task directives can arrive through the same interaction channel. Existing defenses are largely hand-designed and static, making further improvements dependent on repeated manual redesign. We introduce Evolution Under Fire, a staged framework that couples safety-harness evolution with adaptive stressor evolution. ...
  </details>

- **2026-11-17** — Arunkumar V, Gangadharan G. R., S. Senthilkumar — [ConfGuard: a physics-grounded reference monitor for predictive-maintenance large-language-model agents](http://arxiv.org/abs/2611.22288v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model agents now close the industrial predictive-maintenance loop, reading sensor windows, retrieving procedures and dispatching work orders. Two attack channels meet there: injected text in a retrieved document can hijack the decision, and a bounded sensor perturbation can corrupt the remaining-useful-life estimate behind it. Recent agent defenses police data provenance and tool privilege but cannot tell whether a prognostic quantity is physically plausible. ConfGuard is a refere...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-11-19** — Juan Gutiérrez, Victor Gutiérrez-García, José Luis Blanco-Murillo — [Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions](http://arxiv.org/abs/2611.26187v1)
  <details><summary>📄 Abstract</summary>
  Many useful latent distributions can be sampled but do not have a tractable density. Such distributions may be represented by empirical collections of real-world observations or generated by scientific simulators and black-box generative models. These sample-only priors cannot be used directly in likelihood-based normalizing flows, which require evaluating the prior density. We propose Projected Characteristic-Function matching (PCF), a density-free framework for learning an invertible map betwe...
  </details>

- **2026-11-19** — Yiyang Du, Yuxuan Kuang, Qitao Zhao et al. — [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](http://arxiv.org/abs/2611.26613v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot control across 12 manipulation benchmarks. We introduce AgentRoboCritic, an inten...
  </details>

- **2026-11-19** — Jiahao Huang, Jun Wang — [Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models](http://arxiv.org/abs/2611.26590v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) integrate visual and textual information, but their outputs do not reveal internal concept representations. Global workspace theory (GWT) proposes that information is selected from parallel brain processes, integrated in a shared workspace, and made available to specialised processes. We introduce the Multimodal Concept Lens (MC-Lens), a multimodal Jacobian lens, to study these functions in VLM concept processing. Its vision encoder and language decoder lenses map i...
  </details>

- **2026-11-19** — Shuang Wu, Jiachen Qian, Youtian Lin et al. — [Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain](http://arxiv.org/abs/2611.26511v1)
  <details><summary>📄 Abstract</summary>
  Native 3D generation has largely been built around latent diffusion, with recent advances concentrating on stronger variational autoencoders (VAE) and increasingly elaborate latent representations, from vecset and triplanes to structured sparse voxels. Despite their architectural differences, these methods all share the same premise: geometry is first compressed into a latent space and only then modeled by the generator. We take a different route and propose Direct3D-V3, a latent-free diffusion ...
  </details>

- **2026-11-19** — Vishesh Kumar Singh, Sayak Ray Chowdhury — [Sequential Anytime Valid Tests for Efficient Inference-Time Alignment](http://arxiv.org/abs/2611.26413v1)
  <details><summary>📄 Abstract</summary>
  Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-va...
  </details>

- **2026-11-19** — Yuqi Tang, Yang Shi, Yuran Wang et al. — [EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning](http://arxiv.org/abs/2611.26380v1)
  <details><summary>📄 Abstract</summary>
  Egocentric video captioning requires fine-grained detail and accurate timing, yet current multimodal large language models (MLLMs) often miss brief actions, confuse their order, or misinterpret the wearer's motion. Existing caption formats also offer limited support for combining detailed narration with precise timing. We present EgoCaptioner, which pairs a video-level overview of the setting, participants, and the wearer's overall activity with timed steps whose narration adapts to varying perc...
  </details>

- **2026-11-19** — Ziyue Wang, Yaopeng Yang, Liyi Zhou — [Alignment Drives Reuse: Learning Generalizable Robot-Use Agents from Heterogeneous Experience](http://arxiv.org/abs/2611.26376v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) demonstrate broad generalization across tasks and domains. However, comparable generalization in robot manipulation remains challenging. Heterogeneity in robot embodiments, task formulations, geometric conventions, and action interfaces fragments interaction experience across benchmarks and hardware. We rethink robot skill learning through alignment: Can heterogeneous interactions across benchmarks and embodiments jointly improve one shared skillset for robot manipu...
  </details>

- **2026-11-19** — Josef Brozovich, Qining Zhang, Lei Ying — [Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives](http://arxiv.org/abs/2611.26313v1)
  <details><summary>📄 Abstract</summary>
  One fundamental challenge in reinforcement learning (RL) is enforcing temporal safety constraints, such as satisfying formal specifications. Existing methods often transform logic formulas into automata for state augmentation and reward shaping. However, this approach assumes that automaton construction is both feasible and tractable, which limits its applicability to small specifications and linear temporal logic (LTL). This paper proposes Actor-Predictor, a framework that learns a surrogate re...
  </details>

- **2026-11-19** — Jonathan Lichtenfeld, Oskar von Stryk — [I See You: Initial Multi-Robot LiDAR Registration with Mutual-Observation Checks](http://arxiv.org/abs/2611.26276v1)
  <details><summary>📄 Abstract</summary>
  Compared to single-robot deployments, multi-robot teams can significantly improve search-and-rescue (SAR) mission success by covering large areas in parallel. To collaborate effectively, these robots must be registered in a common reference frame. Standard registration methods typically rely on external infrastructure or significant map overlap, but real deployments require infrastructure-free, stationary initial alignment for immediate operation. While global LiDAR point cloud registration addr...
  </details>

- **2026-11-19** — Yipan Xu, Shuyong Gao, Jiyuan Fu et al. — [Frequency-Synchronized Boundary Coupling for Training-Free Multi-Prompt Long Video Generation](http://arxiv.org/abs/2611.26098v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video generation has made remarkable progress with diffusion models and transformer-based video architectures, yet generating coherent long videos from evolving textual descriptions remains challenging. Training long-video models from scratch requires substantial computation and large-scale multi-event data, while training-free multi-prompt generation must activate new prompt semantics without breaking temporal continuity. We identify a frequency-agnostic boundary coupling problem in exi...
  </details>

- **2026-11-19** — Nils Brede Moe, Marthe Berntzen, Astri Barbala et al. — [Barriers to GenAI Integration During Large-Scale Agile Transformation: An Exploratory Case Study](http://arxiv.org/abs/2611.25967v1)
  <details><summary>📄 Abstract</summary>
  Organizations undergoing large-scale agile transformations are increasingly introducing generative AI (GenAI) tools into everyday work. While GenAI promises to accelerate software development, less is known about how organizations integrate GenAI into existing large-scale agile ways of working and how it interacts with tensions related to autonomy, alignment, learning, and coordination. We examine barriers to GenAI integration through an exploratory case study of a large Nordic media organizatio...
  </details>

- **2026-11-19** — Qiyan Deng, Long-Kai Huang, Kangfei Zhao — [From Cases to Criteria: Reusing Evaluation Knowledge for Task-Specific Rubric Generation](http://arxiv.org/abs/2611.25903v1)
  <details><summary>📄 Abstract</summary>
  Query-specific rubrics make LLM evaluation more fine-grained and transparent, and generating high-quality rubrics requires both identifying the target query's evaluation scope and specifying concrete checks. Historical rubrics provide reusable evaluation experiences, yet existing approaches reuse either complete query-rubric cases or aggregated criteria and dimensions without explicitly connecting recurring evaluation requirements to their criterion-level evidence and source-query context. This ...
  </details>

- **2026-11-19** — Runze Wang, Fei Zha, Bing He et al. — [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](http://arxiv.org/abs/2611.25838v1)
  <details><summary>📄 Abstract</summary>
  Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observations. During sustained gameplay, however, existing generative renderers struggle to follow changing conditions while preserving visual continuity across diverse proxies and target styles. We therefore introduce ContextRenderer, an autoregressive video diffusion framework designed for both dynamic conditioning and cross-...
  </details>

- **2026-11-19** — Nina Goncharova, Alexandra Ivanova, Aibek Alanov — [Inject Where It Matters: Objective-Dependent Feature Control in Rectified-Flow Image Editing](http://arxiv.org/abs/2611.25811v1)
  <details><summary>📄 Abstract</summary>
  Many prompt-driven FLUX editing methods rely on injecting source features into target-conditioned generation, creating an inherent trade-off between source preservation and the desired edit. We address this problem by controlling where source features are injected and which transformer blocks are used. First, we introduce adaptive masks that spatially gate feature injection using differences between source- and target-conditioned block outputs at matched inversion states. Second, we use REINFORC...
  </details>

- **2026-11-19** — Wen-Li Wei, Kenneth Yang, Jen-Chun Lin — [Sonic Palette: Predicting Dynamic Color Themes from Music](http://arxiv.org/abs/2611.25781v1)
  <details><summary>📄 Abstract</summary>
  We present Sonic Palette, a music-driven framework for predicting time-varying color themes from audio. Rather than treating music-to-palette generation as a static problem, our method formulates music--color correspondence as a cross-modal sequence prediction task that models how palette-level visual attributes evolve over time in response to music. Specifically, Sonic Palette uses a music-conditioned autoregressive Transformer to predict frame-wise color themes, each represented by five domina...
  </details>

- **2026-11-19** — Shuyue Shi, Rong Yuan, Lin Tian — [AdaptReg: Skip-level FiLM Adapter for Task-Specific Adaptation of a Frozen Registration Foundation Model](http://arxiv.org/abs/2611.25761v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal PSMA-PET/CT registration is a key step in assessing treatment response in prostate cancer, and it requires more than generic alignment accuracy: the deformation must preserve lesion volume, so that measured changes in metabolic tumor volume (MTV) and total lesion glycolysis (TLG) reflect treatment response rather than registration artifacts. We propose AdaptReg, which adapts a frozen registration foundation model to such task-specific requirements through a lightweight trainable ada...
  </details>

- **2026-11-19** — Shengchun Wang, Yuhang Lin, Tong Li et al. — [From Data Alignment to Parameter Generation: Few-Shot Cross-City Traffic Prediction with Conditional Diffusion](http://arxiv.org/abs/2611.25592v1)
  <details><summary>📄 Abstract</summary>
  Accurate mobile traffic forecasting is crucial for network service management, supporting proactive capacity provisioning, congestion mitigation, and energy-efficient operation. However, many cities and regions are data-scarce (e.g., newly deployed or poorly instrumented areas), thus making traffic prediction a few-shot learning problem and limiting the practicality of standard data-driven models. Existing cross-city solutions primarily rely on data-space alignment to match traffic distributions...
  </details>

- **2026-11-19** — Chanwoo Kim, Doyun Kim, Minsoo Song et al. — [Rubric Semantics or Numerical Priors? Auditing Scale-Direction Bias in LLM Judges](http://arxiv.org/abs/2611.25588v1)
  <details><summary>📄 Abstract</summary>
  Recent benchmark evaluations increasingly rely on Large Language Models (LLMs) as automatic judges. This paradigm assumes LLMs evaluate based on the rubric's semantic meaning rather than its numeric scale. We question this assumption by introducing semantic faithfulness: the principle that semantically equivalent rubrics must yield consistent scores. To quantify this, we propose a scale-reversal probe that inverts score anchors without altering evaluation criteria. Furthermore, we introduce floo...
  </details>

- **2026-11-19** — Wenshuo Chen, Honglei Jin, Le Yang et al. — [Trajectory-Calibrated Merging of Embodied Policies](http://arxiv.org/abs/2611.25575v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models are increasingly adapted into task specialists to expand their embodied capabilities. Yet these capabilities remain fragmented across separate policies, and existing model-merging methods do not reliably preserve them during closed-loop execution: parameter-space alignment provides only an indirect proxy for behavior, while regression may fail to preserve behavior at states not covered by its calibration inputs. We present Trajectory-Calibrated Regression (TCR), an execut...
  </details>

- **2026-11-19** — Jinhan Li, Zhisheng Chen, Yuxuan Li et al. — [Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens](http://arxiv.org/abs/2611.25570v1)
  <details><summary>📄 Abstract</summary>
  Global medium-range weather forecasting must not only generate ensembles efficiently to characterize uncertainty in future states, but also serve downstream applications such as extreme-event warnings and cross-sphere coupled simulations. We introduce WeatherCraft, a framework that unifies probabilistic generation and reinforcement learning alignment through discrete weather tokens, bringing the GPT-style pretraining--post-training paradigm to global medium-range weather forecasting. A multiscal...
  </details>

- **2026-11-19** — Jin Yang, Tian Liu, Jose Penagaricano et al. — [Uncertainty-Aware Multimodal Deep Learning for Prediction of Radiation-Induced Xerostomia in Head and Neck Cancer](http://arxiv.org/abs/2611.25481v1)
  <details><summary>📄 Abstract</summary>
  To develop and evaluate an uncertainty-aware multimodal learning framework for predicting radiation-induced xerostomia in patients receiving head-and-neck cancer radiotherapy. We developed a Bidirectional Attention-enhanced Diffusion Transformer (BA-DiT) that combines self-supervised multimodal representation learning with supervised Bayesian fine-tuning. The model integrates pretreatment CT images and three-dimensional dose distributions, focusing on bilateral parotid glands while incorporating...
  </details>

- **2026-11-19** — Alireza Moayedikia — [Interference Bounds and Merge-Aware Training Dynamics for Composable Fine-Tuned Models](http://arxiv.org/abs/2611.25430v1)
  <details><summary>📄 Abstract</summary>
  Combining fine-tuned models by composing their parameter updates has become a standard alternative to multi-task training. We formalize composability as a property of a collection of task vectors and prove that the excess loss of the merged model is controlled by an interference functional of the cross-task curvature overlap and the signed alignment of the updates. In the quadratic regime this functional equals the excess loss, giving a criterion that is necessary as well as sufficient and that ...
  </details>

- **2026-11-19** — Chuyang Zhou, Bingxin Zhou, Andi Han et al. — [Protein Functional Semantic Alignment via Representation Rectification](http://arxiv.org/abs/2611.25396v1)
  <details><summary>📄 Abstract</summary>
  Protein language models (PLMs) are commonly pretrained with likelihood-based objectives such as masked language modeling or denoising. These objectives capture sequence-level regularities, but can produce representations in which functional signals are entangled with non-functional variation (e.g., sequence identity, compositional bias, and frequent local motifs), creating a readout bottleneck for downstream function prediction. We introduce Functional Semantic Alignment via Representation Recti...
  </details>

- **2026-11-18** — Upasana Dutta, Homa Hosseinmardi, Amir Ghasemian et al. — [Asymmetric rhetorical strategies drive partisanship in television news](http://arxiv.org/abs/2611.25140v1)
  <details><summary>📄 Abstract</summary>
  Television remains a dominant source of political information in the United States, yet systematic evidence on how partisanship is expressed in televised news remains limited. Prior research has largely treated partisanship as a one-dimensional construct, offering limited insight into the rhetorical strategies that underlie ideological bias. Here, by analyzing over 400,000 news episodes using large language models (LLMs), we provide a multi-dimensional measure of partisanship bias in television ...
  </details>

- **2026-11-18** — Hai-tao Yu, Jun Xia — [MS-Point: Multi-Modal Hierarchical Spectral Learning for Point Cloud Understanding](http://arxiv.org/abs/2611.25282v1)
  <details><summary>📄 Abstract</summary>
  Point-image alignment learns useful object representations, but different local feature patterns can produce the same pooled descriptor and receive the same alignment signal. We introduce MS-Point, a cross-modal pretraining framework that directly supervises intermediate point features and their neighborhood responses. At selected encoder stages, we compute neighborhood averages and residuals before pooling and align their branch descriptors with image features. Branch-level objectives align eac...
  </details>

- **2026-11-18** — Ivan A. Fernandez, Jingdao Chen — [A Synthetic Multi-Modal Testbed for Security Stress Testing of Agentic Counter-UAS Systems](http://arxiv.org/abs/2611.25249v1)
  <details><summary>📄 Abstract</summary>
  Agentic cyber-physical systems rely on perception and state estimation to support autonomous decisions. Degraded, inconsistent, or manipulated sensor observations can therefore propagate through an autonomous pipeline and create security-relevant failures. This work presents a synthetic Counter-Unmanned Aircraft System (C-UAS) testbed developed in NVIDIA Isaac Sim for repeatable stress testing of perception and tracking algorithms supporting agentic decision-making. A simplified quadrotor follow...
  </details>

- **2026-11-18** — Ziyuan Qin, Yang Qiao, Summer B. Frandsen et al. — [PsyWorld: Profile-Conditioned World Modeling for Human Behavior Prediction](http://arxiv.org/abs/2611.24999v1)
  <details><summary>📄 Abstract</summary>
  Understanding how stable psychometric traits and time-varying states jointly inform behavior is an important problem in computational behavioral science. Existing personalized agents commonly condition actions directly on a static profile, leaving realized state transitions unused as an explicit source of supervision. We introduce a profile-conditioned state world model that uses observed environment--behavior state transitions to learn transition-informed representations for behavioral predicti...
  </details>

- **2026-11-18** — William John Atkinson, Paul Saproza — [Hi Gemini, Who Should I Vote For? The Benefits (and Problems) of Using LLMs As Voting Advice Applications](http://arxiv.org/abs/2611.24684v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can provide voters information about political issues, party positions, and even advise on which party to vote for. However, no previous study explores whether off-the-shelf LLMs could be used as voting advice applications (VAAs) to improve voter-party congruence. In this article, we address this gap by examining how Gemini 3 Flash advises a sample of 6,022 German survey respondents on which party to vote for, based on their policy preferences and priorities alone. I...
  </details>

- **2026-11-18** — Jiawei Shen, Jie Feng, Junpeng Zhang et al. — [ReflectScene:MLLM-Guided Closed-Loop Diffusion for 3D Indoor Scene Generation](http://arxiv.org/abs/2611.23845v2)
  <details><summary>📄 Abstract</summary>
  Text-conditioned 3D indoor scene generation requires layouts satisfying geometric, functional, and semantic constraints. However, existing diffusion methods rely primarily on static textual conditions, limiting their ability to assess evolving scenes and translate semantic discrepancies into executable object-level corrections. MLLM-based post-hoc refinement provides semantic feedback but remains decoupled from denoising, potentially disrupting scene coherence. We propose ReflectScene, an MLLM-g...
  </details>

- **2026-11-18** — Rudransh Agnihotri, Manasvi Kapoor — [Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is](http://arxiv.org/abs/2611.25135v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) can only teach a language model what its reward can recognize. Answer checkers are exact but need a reference answer; learned reward models and LLM judges work everywhere, but their scores are not probabilities. We study RLCDR (Reinforcement Learning from Calibrated Decision Rewards). An LLM converted into a decision model answers a typed question about a response ("is the final answer correct?", "which step is the first error?") with a probability distribution, read ...
  </details>

- **2026-11-18** — Amr Elshazly, Jesse Roberts, Rachad Atat et al. — [LLM-Guided Cyber-Physical Attack Path Identification in Smart Grids](http://arxiv.org/abs/2611.24765v1)
  <details><summary>📄 Abstract</summary>
  Identifying high-impact attack paths in cyber-physical power systems is critical for improving grid resilience. Existing methods typically rely on either structural topology analysis or simulation-based cascading-failure models. Topology-based approaches capture connectivity but lack adversarial reasoning, while simulation-driven methods are primarily suited for offline analysis and are less effective for rapid evaluation of evolving attack scenarios. As a result, identifying realistic attack pa...
  </details>

- **2026-11-18** — Jingzhi Bao, Xiaohe Ma, Hong Li et al. — [UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation](http://arxiv.org/abs/2611.24941v1)
  <details><summary>📄 Abstract</summary>
  Generating physically based rendering (PBR) texture maps for a 3D mesh from a single reference image is highly ambiguous, as the observed appearance entangles material identity, surface reflectance, and illumination. While current generative methods produce realistic albedo maps, they still struggle to infer accurate metallic and roughness attributes for relighting. We present UltraTex, a cascaded multi-view framework that moves beyond appearance matching by integrating physical knowledge into m...
  </details>

- **2026-11-18** — Priyanka Sinha, Sugam Pandey — [Knowing What You Know: A Trait Theory of Reviewer Value in Human-AI Cognitive Systems](http://arxiv.org/abs/2611.24932v1)
  <details><summary>📄 Abstract</summary>
  When a capable model and a human reviewer cooperate on the same decision, which human still adds value? We argue this is a question about a single cognitive trait, metacognitive calibration: the alignment between a reviewer's behavioral confidence and the actual correctness of their judgments. We develop a trait theory of reviewer value to make it precise. The theory makes five claims: value is governed by calibration rather than by activity, speed, agreement, or tenure; calibration leaves obser...
  </details>

- **2026-11-18** — Zihan Wang, Jianzhe Li, Zhenyi Zhang et al. — [Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics](http://arxiv.org/abs/2611.24764v1)
  <details><summary>📄 Abstract</summary>
  Learning the spatiotemporal dynamics of cells from spatial transcriptomics requires connecting snapshots of different cells acquired in different coordinate frames. A rotation or translation of a section can appear as cell movement and distort the inferred correspondence. We introduce horizontal flow matching, which learns changes in tissue organization, molecular state, and cell abundance up to shared rigid motion. The dynamics follow a continuity--reaction equation whose action assigns no cost...
  </details>

- **2026-11-18** — William John Atkinson, Paul Saproza — [Hi Gemini, Who Should I Vote For? The Benefits (and Problems) of Using LLMs As Voting Advice Applications](http://arxiv.org/abs/2611.24684v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can provide voters information about political issues, party positions, and even advise on which party to vote for. However, no previous study explores how well off-the-shelf LLMs function as voting advice applications (VAAs). In this article, we address this gap by examining how Gemini 3 Flash advises a sample of 6,022 German survey respondents on which party to vote for, based on their policy preferences and priorities alone. In brief, we find that for most respond...
  </details>

- **2026-11-18** — Huu Binh Ta, Alex Morehead, N. Benjamin Erichson et al. — [Choosing the Right Representations: Task-Aware Fusion for Multimodal Materials Language Models](http://arxiv.org/abs/2611.24641v1)
  <details><summary>📄 Abstract</summary>
  Multimodal language models for materials science rely on effective mechanisms for incorporating three-dimensional structural representations. MatterChat addresses this challenge using a large bridge module between a pretrained structural encoder and the LLM, together with a separate contrastive alignment stage. We instead ask whether this bridge can adaptively select and combine representations from multiple structural encoders according to the target property. We find that supervised and genera...
  </details>

- **2026-11-18** — Zhuoqi Hu, Shiwei Li, Haozhao Wang et al. — [Where Should a Diffusion Transformer Meet Its Teacher?](http://arxiv.org/abs/2611.24380v1)
  <details><summary>📄 Abstract</summary>
  Representation Alignment (REPA) significantly accelerates Diffusion Transformer training by guiding intermediate student features with a pretrained visual teacher, yet existing methods typically attach supervision to a single fixed layer. As student representations evolve, however, we find that the most effective layer for alignment varies across training stages. To track this evolving layer suitability online without costly search, we measure gradient compatibility between the flow-matching and...
  </details>

- **2026-11-18** — Argyrios Zafeiriou, Athanasios Kallipolitis, Ilias Maglogiannis — [Transferable Named Sparse Features for Morphology-based Gleason Grading](http://arxiv.org/abs/2611.24363v1)
  <details><summary>📄 Abstract</summary>
  Deep learning systems grade prostate biopsies at the level of pathologists, but most report a grade without the glandular architecture that justifies it. This work presents a grading system built on a sparse code over the tokens of a pathology foundation model. A sparse autoencoder pretrained on biopsies is aligned with multi-reader annotations, so that 69 of its 2048 features are named after Gleason morphologies such as cribriform glands, cords, and comedonecrosis. The same code feeds a grading...
  </details>

- **2026-11-18** — Aniruddh Sikdar, Arya Kishor, Snehashis Dhibar et al. — [CROMPT: Adapting CLIP via Cross-Modal Prompting for Robust Zero-Shot Generalization under Adverse Weather](http://arxiv.org/abs/2611.24284v1)
  <details><summary>📄 Abstract</summary>
  Domain adaptation for semantic segmentation is challenging when target-domain images are unavailable during training. Zero-shot domain adaptation addresses this by adapting models using only textual descriptions of the target domain. However, existing prompt-learning methods are not well suited for ResNet-based CLIP vision backbones or pixel-level cross-modal feature alignment. We propose CROMPT, a prompt-learning framework for zero-shot domain adaptation in semantic segmentation. CROMPT introdu...
  </details>

- **2026-11-18** — YaoYang Liu, ZhuoShi Tang, Haopeng Lai et al. — [Stabilizing Neural-to-Image Retrieval with Frequency-Domain Priors and Adaptive Supervision](http://arxiv.org/abs/2611.24163v1)
  <details><summary>📄 Abstract</summary>
  Visual neural decoding aims to infer perceived visual stimuli from brain activity, offering important insights into human visual cognition while enabling transformative applications in brain computer interfaces and artificial intelligence. Recent advances in pretrained vision-language models have provided a semantically rich representation space for this task. However, reliable alignment between EEG/MEG signals and visual embeddings remains challenging because neural responses are noisy, highly ...
  </details>

- **2026-11-18** — Sayumi Muthukumarana, Roshan Godaliyadda, Parakrama Ekanayake et al. — [Once Upon a Bias: Gender Stereotyping in LLM-Generated Children's Stories](http://arxiv.org/abs/2611.24156v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to create stories for children. Since bedtime stories can shape children's perceptions of social roles, this raises concerns about whether LLMs adapt narrative portrayals according to the intended recipient's gender. We conducted a large-scale study to examine gender stereotyping in LLM-generated bedtime stories. Using matched daughter/son prompts and a five-generation design, we analyze 62,873 retained stories from 16 LLMs across 35 country settings a...
  </details>

- **2026-11-18** — Yuhang Huang, Junchao Li, Boyang Ma et al. — [Lost Between Mind, Model Collaboration, and Motion: Understanding and Measuring Cross-Model Action Misalignment in Commercial Robots](http://arxiv.org/abs/2611.24100v1)
  <details><summary>📄 Abstract</summary>
  Embodied robots increasingly rely on large language models (LLMs) to interpret user intent and coordinate with robot-specific action models for physical interaction. This multi-model pipeline creates a critical semantic boundary across mind, model collaboration, and motion: semantic consistency may break between what the large model understands, how the small action model translates that understanding into executable commands, and what physical actions the robot ultimately performs. As a securit...
  </details>

- **2026-11-18** — Paul König, Sascha Marton, Stefan Lüdtke et al. — [VESPA: Verifiable Symbolic Policy Adaptation for Safe Reinforcement Learning](http://arxiv.org/abs/2611.24083v1)
  <details><summary>📄 Abstract</summary>
  Safe reinforcement learning (RL) aims to prevent agents from taking actions that are dangerous or destructive to their environment. This is especially important for safety-critical domains, such as robotics or autonomous driving. Formal verification can be used to prove agent safety through safety constraints. However, in practice, many policies do violate safety constraints, and thus are verified to be unsafe. Since the goal is to obtain a safe policy, we would need to retrain a new policy from...
  </details>

- **2026-11-18** — Anand A. Joshi, Satwik Bathula, Richard M. Leahy — [EEGSync: Unitary Temporal Alignment Method for Naturalistic and Resting-State EEG](http://arxiv.org/abs/2611.24017v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) studies increasingly use naturalistic and resting-state paradigms that lack discrete event timing. These recordings contain structured oscillatory activity but often lack repeated stimulus onsets to define a shared time clock across trials or participants. We introduce EEGSync, a complex-valued unitary Procrustes temporal alignment method for band-limited analytic EEG signals. EEGSync represents each subject as a matrix of complex oscillatory trajectories and solves ...
  </details>

- **2026-11-18** — Baoliang Chen, Lingyu Zhu, Zhiwei Zhong et al. — [FlyVQA: Seeing Video Frame Interpolation Quality through Fly Eyes](http://arxiv.org/abs/2611.24012v1)
  <details><summary>📄 Abstract</summary>
  The ultimate ambition of visual quality assessment is to reproduce the neural computations of human vision and thereby achieve full alignment with human perception. However, the immense complexity of human visual circuitry makes this goal difficult to realize. Recently released fly visual connectomes provide a tractable biological starting point. Despite differences between fly and human vision, the fly's well-characterized motion pathways motivate us to investigate their potential for assessing...
  </details>

- **2026-11-18** — Luosong Guo, Xiang Yang, Chaoyang Li et al. — [Freeforward4d: Annotation-free feed-forward 4d reconstruction of driving scenes](http://arxiv.org/abs/2611.24007v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward 4D reconstruction enables efficient creation of renderable driving scenes for autonomous driving simulation. However, most existing methods rely heavily on dataset-provided cameras, LiDAR depth, or 3D box annotations, limiting their applicability to unannotated driving videos. Pretrained visual models can predict cameras, depth, and object tracks from RGB alone, but their geometry is mutually inconsistent: multi-view predictions come in short windows with independent scales and fram...
  </details>

- **2026-11-18** —  Neha, Mudasir Ganaie — [SIRAZ: Sparse Inter-Layer Residual Aggregation for Zero-Shot Visual Neural Decoding](http://arxiv.org/abs/2611.23991v1)
  <details><summary>📄 Abstract</summary>
  Brain-computer interfaces aim to establish direct communication between neural activity and external systems, making interpretation of brain signals an important problem. In this context, neural visual decoding seeks to infer visual information from neural activity by learning a mapping between brain responses and the corresponding visual stimuli. It investigates how visual information emerges from neural signals and relates to perceptual processing while enabling the reconstruction or retrieval...
  </details>

- **2026-11-18** — Hongxu Chen, Chun Wang, Yanghao Wang et al. — [Dual-Manifold Variational Autoencoders](http://arxiv.org/abs/2611.23964v1)
  <details><summary>📄 Abstract</summary>
  In latent diffusion models, expanding the latent dimension of variational autoencoders (VAEs) is essential to push the upper bound of reconstruction quality. However, without explicit structural constraints, such unregularized expansion easily yields a rugged and ill-conditioned latent manifold, causing generated latents to drift off the manifold during generation (i.e., off-manifold problem). Recent works smooth this manifold by using external foundation models (e.g., DINOv2) as a topological r...
  </details>

- **2026-11-18** — Ananya Sutradhar, Fabien Roger — [Can you make models believe false facts in the prompt?](http://arxiv.org/abs/2611.23938v1)
  <details><summary>📄 Abstract</summary>
  Making LLMs believe false facts is useful for alignment evaluations and for building model organisms. Previous work explored doing so with Synthetic Document Finetuning (SDF). But SDF requires fine-tuning one new model for each set of injected false beliefs. To enable larger scale SDF-powered alignment evaluations, we attempt to produce a single model that believes any fact placed in a <facts> tag in the prompt. To do so, we explore doing prompt-conditioned SDF: fine-tuning a model on synthetic ...
  </details>

- **2026-11-18** — Jiawei Shen, Jie Feng, Junpeng Zhang et al. — [ReflectScene:MLLM-Guided Closed-Loop Diffusion for 3D Indoor Scene Generation](http://arxiv.org/abs/2611.23845v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned 3D indoor scene generation requires layouts satisfying geometric, functional, and semantic constraints. However, existing diffusion methods rely primarily on static textual conditions, limiting their ability to assess evolving scenes and translate semantic discrepancies into executable object-level corrections. MLLM-based post-hoc refinement provides semantic feedback but remains decoupled from denoising, potentially disrupting scene coherence.We propose ReflectScene, an MLLM-gu...
  </details>

- **2026-11-18** — Shuaidi Wang, Zhuocheng Gong, Xuejie Liu et al. — [Beyond Replacement: Levenshtein Editing for Diffusion Language Models](http://arxiv.org/abs/2611.23750v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) offer a flexible alternative to autoregressive models, enabling any-order infilling. While most existing decoding methods treat decoded tokens as fixed, some recent models allow previously decoded tokens to be revised only by replacing them with alternative tokens, a paradigm we refer to as replacement-only editing (ROE). Although ROE can correct individual tokens, it is inefficient for sequence shifts caused by missing or extra tokens and struggles when errors o...
  </details>

- **2026-11-18** — Zichen Zhang, Wei Zhai, Xuji Zhang et al. — [ART: Bridging the Embodiment Gap in 3D Human-to-Robot Affordance Transfer](http://arxiv.org/abs/2611.24182v1)
  <details><summary>📄 Abstract</summary>
  3D affordance acts as a critical link between perception and action, providing priors for robotic manipulation. While existing approaches predominantly leverage human priors as direct references, they often overlook that affordance is not an object-intrinsic property but is inherently coupled with the agent's embodiment. Due to the structural and morphological disparities between human hands and robot end-effectors, directly applying human priors causes severe incompatibility for robotic executi...
  </details>

- **2026-11-17** — Siamak Ghodsi, Amjad Seyedi, Sahar Tahmasebi et al. — [FairPGT: Partitioned Graph Transformers for Dual-Level Fair Graph Clustering](http://arxiv.org/abs/2611.23631v1)
  <details><summary>📄 Abstract</summary>
  Clustering on attributed graphs can produce demographically biased clusters, particularly when communities align with protected groups. Graph transformers can amplify this bias through same-group attention, while global attention limits scalability. We propose FairPGT, a partitioned graph transformer for fair graph clustering. FairPGT restricts attention to METIS partitions and connects them through routing tokens, which divides the quadratic cost of attention by the number of partitions. A grap...
  </details>

- **2026-11-17** — Zelong Liu, Hamza Ahmed, Wynn Wingyi Lee et al. — [ORGANIC3D: Grounding 3D CT Vision Language Models in Organ Level Image Text Coupling](http://arxiv.org/abs/2611.23529v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) have achieved strong performance in 3D computed tomography (CT) classification, but high accuracy does not reflect whether their predictions rely on the correct anatomical evidence. We introduce ORGANIC3D, a framework for evaluating and improving organ level image text alignment through controlled anatomical interventions. Our benchmark assesses 12 vision encoder checkpoints and 7 generative VLMs using matched patient comparisons, organ erasure, lesion replacement, ...
  </details>

- **2026-11-17** — Xiaosheng Zhao, Rosemary F. G. Wyse, Yuan-Sen Ting et al. — [JEPA for astronomy: multi-survey spectral alignment puts stellar parameters on the leading principal axes](http://arxiv.org/abs/2611.23492v1)
  <details><summary>📄 Abstract</summary>
  Spectra from different surveys carry different systematics and are not calibrated against one another. Multi-survey foundation models for stellar spectra are then built by aligning embeddings of the same star observed across surveys. Most in astronomy follow the recipes established for language and vision, aligning with a contrastive loss that separates every star from the others. However, this does not ensure that the stellar physics is encoded in a form that a simple read-out can recover. Hold...
  </details>

- **2026-11-17** — Gabriel Sarch, Declan Campbell, Nicholas Budny et al. — [Learning Grounded Reasoning from Human Gaze](http://arxiv.org/abs/2611.23209v1)
  <details><summary>📄 Abstract</summary>
  Human visual reasoning is driven by systematic exploration and extraction of task-relevant visual evidence. Human gaze provides a window into this process, making gaze a useful source of guidance for visually-grounded reasoning in vision-language models (VLMs). However, human gaze also includes noise and redundancies that may transfer poorly to VLMs. In this work, we investigate how human gaze data can be effectively leveraged to improve visual reasoning in VLMs, while maintaining alignment with...
  </details>

- **2026-11-17** — Nhi Hoai Doan, Tatsuya Hiraoka, Munachiso Samuel Nwadike et al. — [Polarity Composition Hypothesis: Causal Evidence from Negation in NLI](http://arxiv.org/abs/2611.23185v1)
  <details><summary>📄 Abstract</summary>
  We investigate how language models process negation in natural language inference (NLI). We propose the \textit{Polarity Composition Hypothesis}, a high-level causal model of this computation. Behavioral evaluations show that language-model predictions largely conform to the proposed hypothesis. Using Distributed Alignment Search, we identify causally effective subspaces aligned with the variables in the polarity-composition hypothesis. These representations transfer across negation forms and pa...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 60 papers

- **2026-11-19** — Chunbo Jiang, Yifei Chen, Beining Wu et al. — [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](http://arxiv.org/abs/2611.26343v1)
  <details><summary>📄 Abstract</summary>
  Automating experiments does not necessarily advance scientific understanding. Research agents must identify meaningful knowledge gaps, determine what available data can resolve, and assess whether their findings advance existing knowledge. We introduce DeepQuest, a knowledge-gap-driven AI scientist framework for Alzheimer's disease research. DeepQuest transforms unresolved questions from domain reviews into traceable, testable hypotheses and prioritizes them through data feasibility screening an...
  </details>

- **2026-11-19** — Youssef ElNahas, Adel Ammar, Soumaya Chaffar et al. — [Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](http://arxiv.org/abs/2611.25898v1)
  <details><summary>📄 Abstract</summary>
  Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and why static metrics miss it; the agentic hallucination cascade, in which multi-agent...
  </details>

- **2026-11-19** — Filippo Galgani, Ziwei Ji, Omri Homburger et al. — [Efficient and Robust Drafting with Multi-Token Prediction](http://arxiv.org/abs/2611.25813v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase. A crucial challenge is therefore designing a drafter that is both lightweight and accurate enough to approximate the predictions of the target model. We present a highly optimized Multi-Token Prediction (MTP) architecture that extends existing backbone LLMs to efficiently produce high-quality drafts. Built...
  </details>

- **2026-11-19** — Yingshuo Wang, Weixiang Zhao, Guancheng Li et al. — [When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards](http://arxiv.org/abs/2611.25793v1)
  <details><summary>📄 Abstract</summary>
  Multimodal safety guards increasingly generate rationales alongside safety predictions, yet whether these rationales are reliable remains largely unexplored. We systematically study *rationale hallucination* from two perspectives: visual rationale hallucination, where rationales contain unsupported visual facts, and safety attribution hallucination, where grounded content is assigned an incorrect safety interpretation. Across rationale-generation methods, multiple vision-language backbones, and ...
  </details>

- **2026-11-19** — Yajie Qi, Wei Wei, Lin Li et al. — [Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models](http://arxiv.org/abs/2611.25742v1)
  <details><summary>📄 Abstract</summary>
  Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. Large language models (LLMs) can guide exploration by generating high-level goals, but methods using models without explicit task adaptation often rely on carefully designed prompts and may produce inconsistent or contextually inappropriate goals. We introduce CCGP-2M, a multimodal goal-preference dataset constructed from interaction trajectories in ...
  </details>

- **2026-11-19** — Xu Pan, Chubin Zhang, Xingrui Yu et al. — [CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control](http://arxiv.org/abs/2611.25667v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies must react while visual inference is still running. Overlapping computation and execution reduces waiting, yet leaves perceptual memory stale and successive action chunks disconnected. We present CauSyncVLA, an asynchronous dual-system controller that aligns perceptual-memory prediction and trajectory correction with actual robot execution. Rather than forecasting pixels or physical states, a Causal Latent World Model predicts current perceptual memory from ...
  </details>

- **2026-11-19** — Geon Lee, Fanchen Bu, Soo Yong Lee et al. — [Toward a Science of AI Agent Societies](http://arxiv.org/abs/2611.25404v1)
  <details><summary>📄 Abstract</summary>
  AI agents are rapidly evolving from isolated personal assistants into networked actors that interact with one another at scale. We envision the emergence of AI agent societies, with their own social and economic dynamics, as a new research frontier. We argue that AI agent societies should be studied as a distinct object of inquiry: neither simply larger collections of individual agents nor merely simulations of human society. To formalize this perspective, we propose four core properties that a ...
  </details>

- **2026-11-19** — Oankar R. Patil, May D. Wang — [Breaking Noise Shortcuts in Self-Supervised Learning Via Noise-Aligned View Generation](http://arxiv.org/abs/2611.25335v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) is increasingly applied to scientific imaging domains, such as microscopy, where labels are scarce but noisy data is abundant. These domains exhibit significant signal-dependent noise, which can create a representational shortcut: since both augmented views derive from the same noisy image, the encoder can boost view agreement by also encoding noise patterns rather than semantic content. To enable noise-robust representation learning without knowledge of underlying...
  </details>

- **2026-11-19** — Yuzhi Huang, Jie Wu, Fanding Huang et al. — [Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](http://arxiv.org/abs/2611.26444v1)
  <details><summary>📄 Abstract</summary>
  Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess them separately without their composition, so they reveal little about whether a fai...
  </details>

- **2026-11-19** — Kang Wang, Xiaolei Zhou, Xiaoyu Wu et al. — [Agentic Scaling of Embodied Tasks in Simulation for Synthetic Data Collection and Policy Evaluation](http://arxiv.org/abs/2611.26046v1)
  <details><summary>📄 Abstract</summary>
  Scaling embodied interaction data requires a broad collection of usable tasks, yet specifying and validating each task instance remains costly. We present AgenticTask, an agent-based framework that expands existing task collections under human intent. Its central representation links interaction requirements to object and part bindings, scene and robot configurations, initial conditions, and completion criteria. A task-generation agent reuses interaction structure to construct supported variatio...
  </details>

- **2026-11-19** — Chenyuan Zhou, Chaoyi Huang, Zibo Wang et al. — [A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery](http://arxiv.org/abs/2611.25656v1)
  <details><summary>📄 Abstract</summary>
  Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify whether they support new tools in performing similar work. We present A$^2$-VLA, a tool-adaptation framework that combines an embodied agent with ...
  </details>

- **2026-11-19** — Tara Sowrirajan, Yanqiao Wang — [The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting](http://arxiv.org/abs/2611.26521v1)
  <details><summary>📄 Abstract</summary>
  In our experiments on long-horizon customer-behavior forecasting, a longer observation window outweighed the observed effects of more data, more capacity and newer architectures. The window is the weeks of history a model sees before the week it forecasts from. Going from an 8- to a 16-week window adds a raw +0.070 to 0.107 log-space $R^2$ in every family at 1M. Matched test cohorts, which score the same customer-weeks at every window, show this raw comparison understates the gain in every famil...
  </details>

- **2026-11-19** — Rahul Srinivasan, Lorenzo Copparoni, Chantal Pitte et al. — [Low-Latency Alerts of Massive Black Hole Binaries in LISA](http://arxiv.org/abs/2611.26411v1)
  <details><summary>📄 Abstract</summary>
  The Laser Interferometer Space Antenna (LISA) will observe massive black hole binaries (MBHBs) for days to months before merger, offering opportunities for advance electromagnetic follow-up. To enable such observations, inference methods must provide rapid, continuously updated, and statistically calibrated posterior estimates, while remaining robust to overlapping sources. We present TRUFFLE (Time-evolving Rapid Updates For Follow-up of LISA Events), a simulation-based inference method for MBHB...
  </details>

- **2026-11-19** — Bin Li, Xing Zhu, Jingya Wang — [MixReact: Physics-Based Reactive Humanoid Control from Multimodal Cues via a Discrete-Continuous Mixture of Transformers](http://arxiv.org/abs/2611.26218v1)
  <details><summary>📄 Abstract</summary>
  Humanoid agents in everyday environments are expected to react to diverse cues as humans do, with semantically appropriate and physically executable behaviors. Existing cue-driven reaction generation methods support only a narrow range of cue modalities and are limited to purely kinematic generation, leaving the resulting reactions susceptible to physical artifacts. To this end, we present MixReact, the first unified framework for physics-based reactive humanoid control from text, audio, and vid...
  </details>

- **2026-11-19** — Yu Zhao, Jiaxin Zhang, Rohit Saxena et al. — [Learning to Think with Images Faithfully via Adaptive Data Selection](http://arxiv.org/abs/2611.26199v1)
  <details><summary>📄 Abstract</summary>
  Thinking with images (TwI) empowers vision-language models (VLMs) to overcome perceptual bottlenecks by actively cropping and zooming into fine-grained visual details, promising both higher accuracy and interpretable, region-grounded reasoning. However, our analysis shows that the improved accuracy of TwI models does not guarantee faithful tool use; they frequently invoke tools without actually relying on the zoomed region, undermining the reliability of tool-assisted reasoning. We trace this un...
  </details>

- **2026-11-19** — Doyun Kim, Chanwoo Kim, Jiwoo Kum et al. — [Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge Evaluation](http://arxiv.org/abs/2611.26077v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used as automated evaluators to reduce the cost and time required for human annotation. However, the role of scoring-scheme design in the reliability of LLM-as-a-Judge evaluation remains underexplored. To address this problem, we introduce numerical scoring topology, which characterizes the structural design of a scoring scheme in terms of its scale width, granularity, offset, symmetry, and boundary placement. Building on this definition, we conduct the first systematic stu...
  </details>

- **2026-11-19** — Zinan Zheng, Nuo Chen, Jia Li — [SpatialMem: Building Quantitative Spatial Reasoning Agents with Hierarchical Memory](http://arxiv.org/abs/2611.25925v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) have shown remarkable capabilities in qualitative spatial reasoning, but remain limited in quantitative spatial reasoning. Current work leverages the VLM agent to invoke external vision tools to perform computation. However, these methods usually bind each functional requirement to a single predefined vision specialist, implicitly resulting in fixed and rigid tool pipelines. In practice, addressing diverse spatial scenarios and tasks demands a broader diversity in p...
  </details>

- **2026-11-19** — Youngwoo Shin, Jongsuk Kim, Junmo Kim — [Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning](http://arxiv.org/abs/2611.25776v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is the stage in which Video Large Language Models (VideoLLMs) advance their capability to reason over video. However, the VideoLLM also learns to answer from textual regularities of its training data, a shortcut that bypasses the video. The regularities behind the shortcut are hard to define at the data level, and the shortcut forms regardless of training epoch, data size, or backbone. The shortcut is hidden behind a rise in accuracy within the training distribution,...
  </details>

- **2026-11-19** — JiaXu Chee, Simon Denman, Fahira Afzal Maken et al. — [GNetSS: Towards Learning GNSS Corrections without Ground Truth](http://arxiv.org/abs/2611.25665v1)
  <details><summary>📄 Abstract</summary>
  We present GNetSS, a self-supervised GNSS position correction framework that improves the robustness of single point positioning (SPP) without requiring ground-truth locations for training. GNetSS combines a transformer-based network with a deterministic differentiable positioning solver. The network predicts satellite-wise pseudorange corrections by modelling inter-satellite geometry and temporal context, while the solver converts these corrected measurements into receiver position corrections ...
  </details>

- **2026-11-19** — Anna Marija Sumrova, Jonathan M. Goodman — [NIMIS: A Structure-Agnostic, Chemically Informed Slot-Attention Framework for Demixing 1D $^1$H-NMR Mixture Spectra](http://arxiv.org/abs/2611.25629v1)
  <details><summary>📄 Abstract</summary>
  The products of chemical reactions are usually complex mixtures that must be separated into their components before interpretable $^1$H-NMR spectra can be obtained. Direct analysis of the spectra of crude mixtures would accelerate reaction analysis and facilitate the exploration of new chemical space. We present NIMIS, a structure-agnostic, attention-based deep learning framework that groups the peaks of a 1D $^1$H-NMR mixture spectrum according to the component from which they originate. J-coup...
  </details>

- **2026-11-19** — Anurag Kulkarni, Nouhaila Innan, Muhammad Shafique — [QFT-Based Hybrid PointNet-Quantum Neural Networks for LiDAR Point-Cloud Classification](http://arxiv.org/abs/2611.25578v1)
  <details><summary>📄 Abstract</summary>
  Hybrid quantum-classical learning architectures provide a promising framework for integrating quantum feature transformations into complex data-processing tasks. Among these transformations, the Quantum Fourier Transform (QFT) offers a structured approach to feature processing, motivating an investigation of how its circuit configuration influences predictive performance, quantum resource requirements, and noise robustness. We present a hybrid PointNet-quantum neural network architecture for LiD...
  </details>

- **2026-11-19** — Yoonho Shin — [Persona Lenses: What Makes a Vision-Language Model See Through Its Persona's Eyes?](http://arxiv.org/abs/2611.25508v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models have been used to simulate where a user looks on a web page. However, a persona in the prompt reaches the simulated gaze only partly. We measure this reach as the difference in one model's gaze between two MatrAIx personas that differ in a single attribute. We introduce persona lenses, which place the persona between the model and the page: a text lens (a two-step prompt in which the model first writes what the persona would look at), a pixel lens (marks on the region matc...
  </details>

- **2026-11-19** — Bo Li, Taoyong Cui, Bob Zhang et al. — [WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming](http://arxiv.org/abs/2611.25476v1)
  <details><summary>📄 Abstract</summary>
  Neural networks encode learned capabilities in their weights, yet extending those capabilities with explicit task knowledge remains a fundamental challenge. Here we show that Weight-Space Programming (WSP), in which executable programs read, construct or modify a network's weights directly, can install new capabilities within trained neural networks. WeightCode, a WSP framework, uses a frozen language model to write executable weight programs that install new computations into trained neural net...
  </details>

- **2026-11-19** — Junhyeok Lee, Dongheon Lee, Kyu Sung Choi — [Stuck in Place: Stall Diagnosis and Remedies for JEPA Planners](http://arxiv.org/abs/2611.25415v1)
  <details><summary>📄 Abstract</summary>
  Joint-embedding predictive architecture (JEPA) world models plan from pixels with model predictive control, yet often fail on tasks their model should handle. Test-time adaptation attributes such failures to model error under distribution shift and updates the weights on the current episode, without checking this attribution against the planning loop itself. We follow the executed planning loop on pushing tasks. In most settings, with and without distribution shift, nearly all failures (at least...
  </details>

- **2026-11-19** — Xinyu Pan, Boxun Liu, Chen Chen et al. — [WiFo-D: Wireless Foundation Model Based on Discrete Representations](http://arxiv.org/abs/2611.25378v1)
  <details><summary>📄 Abstract</summary>
  Wireless foundation models have shown strong generalization capabilities across heterogeneous wireless tasks and configurations. However, most existing models rely on continuous representations, limiting ultra-low-overhead channel state information (CSI) feedback, few-shot generalization, and robustness to noise. To address these limitations, this paper proposes a wireless foundation model based on discrete representations (WiFo-D), which learns multi-granularity discrete CSI representations. It...
  </details>

- **2026-11-19** — Jingyi Sun — [Enhancing Understanding of Language Models with Varied Explanations](http://arxiv.org/abs/2611.25314v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly used to support human judgement in complex reasoning tasks, yet their predictions often remain difficult to interpret and validate. Explainability techniques provide insight into model decision-making, helping expose errors, failure modes, and potential bias so users can decide whether to rely on model outputs. Explanations are simplified approximations of a language model's internal workings. The goal is to obtain explanations that reflect the underlying computa...
  </details>

- **2026-11-18** — Jean-Sébastien Giroux, Rose Guay Hottin, Marco Bonizzato — [HapBO: Harnessed $α$-$π$ Bayesian Optimization via Expert Natural Language Priors](http://arxiv.org/abs/2611.25100v1)
  <details><summary>📄 Abstract</summary>
  Bayesian Optimization (BO) can be substantially more sample-efficient when informed by prior knowledge about the problem. In practice, however, such knowledge is often available only in natural language, e.g., expert intuitions or documentation, rather than as the explicit probability distribution landscape that prior-guided BO methods may require. Leveraging it effectively demands both an expressive mapping from language to priors and robustness to information that may be misleading. We propose...
  </details>

- **2026-11-18** — Ruijiang Gao, Steven Chong Xiao — [When AI Analysts Disagree: Agentic Multiverse Analysis and the Robustness of Empirical Research](http://arxiv.org/abs/2611.25198v1)
  <details><summary>📄 Abstract</summary>
  Every empirical analysis on observational data rests on dozens of defensible analytical choices ("forks") that its readers cannot see. We develop an agentic multiverse analysis (AMA) framework that makes a conclusion's sensitivity to those choices visible at scale, and we position it as a decision-support instrument for human experts. A pilot study first deploys 150 autonomous AI coding agents on one dataset and one set of research questions and finds that they disagree through the same defensib...
  </details>

- **2026-11-18** — Ruijiang Gao, Steven Chong Xiao — [An AI-Powered Multiverse Analysis of Empirical Finance Research: Evidence from Reused Natural Experiments](http://arxiv.org/abs/2611.25184v1)
  <details><summary>📄 Abstract</summary>
  Empirical finance research often reuses natural experiments to study other outcomes, raising concerns about multiple testing and publication bias. We use AI agents to run a multiverse analysis of 324 papers that reuse 13 natural experiments. The agents rebuild the data, reproduce each paper's main estimate and re-estimate it across grids totaling 62,409 estimated defensible specifications. Based on the reproductions and the specification grids, we develop measures of empirical robustness. We rep...
  </details>

- **2026-11-18** — Haochen Liu, Guanghui Min, Song Wang et al. — [LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2611.25229v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have demonstrated strong capabilities in open-domain question answering, but often struggle with factual accuracy and multi-hop reasoning due to the incompleteness of the training corpora. A promising solution is Knowledge Graph Retrieval-Augmented Generation (KG-RAG), which supplements LLMs with structured knowledge retrieved from external knowledge graphs (KGs). However, existing KG-RAG methods either rely on large-scale language models (e.g., ChatGPT) to guide the...
  </details>

- **2026-11-18** — Takahiro Miki, Robin Schmid, Manthan Patel et al. — [Bridging vision-language reasoning and learned control for legged navigation in the wild](http://arxiv.org/abs/2611.25215v1)
  <details><summary>📄 Abstract</summary>
  Autonomous navigation in diverse real-world environments remains one of the greatest challenges in robotics. It demands both robust low-level motion control to handle diverse terrain and high-level reasoning to interpret environmental cues. We present ROAM (Robust Open-world Autonomous Mobility), a system that enables legged robots to perform kilometer-scale navigation in complex alpine and urban settings. ROAM combines the world knowledge of a Vision-Language Model (VLM), pre-trained on interne...
  </details>

- **2026-11-18** — Luca M. Hartmann, Parinaz Naghizadeh — [From Self-Play RL to Constrained Control: Distilling DiffMPC Students with DAgger](http://arxiv.org/abs/2611.25197v1)
  <details><summary>📄 Abstract</summary>
  Self-play reinforcement learning (RL) produces strong driving policies, but these policies are hard to verify or interpret. Differentiable model predictive control (DiffMPC) can enforce explicit constraints, but it is usually trained by imitating logged data or with costly RL. To add constraints to an already trained policy, we keep a PPO teacher's backbone and replace its action head with a DiffMPC that enforces road boundary half-planes and agent ellipses. We then distill the student with DAgg...
  </details>

- **2026-11-18** — Hamza Ruzayqat, David M. Bortz, Vanja Dukić — [WAIVES: Weak-form Asymptotically-unbiased Instrumental-Variable Estimation for SDEs](http://arxiv.org/abs/2611.23951v2)
  <details><summary>📄 Abstract</summary>
  Weak-form methods have transformed inference for deterministic dynamical systems. By integrating the governing equations against smooth, compactly supported test functions, they trade noise-amplifying differentiation for noise-attenuating integration, yielding fast and robust estimates. Extending this idea to stochastic differential equations (SDEs) has proven harder, and a consistent single-trajectory formulation in the time domain has remained out of reach. Applied naively in the time domain, ...
  </details>

- **2026-11-18** — Beyazit Yalcinkaya, Ethan Pronovost, Maximilian Naumann et al. — [Learning to Interact in Multi-Agent Self-Play for Controllable Autonomous Driving Scenario Generation](http://arxiv.org/abs/2611.24876v1)
  <details><summary>📄 Abstract</summary>
  Large-scale, multi-agent self-play trains robust driving policies effectively in simulation, but controlling these models to generate specific, safety-critical edge cases remains a key challenge. Existing goal-conditioned self-play frameworks rely primarily on static map-location goals and fail to reliably produce complex agent interactions such as aggressive tailgating or adversarial cut-offs. These agent interactions are necessary for rigorous autonomous vehicle (AV) testing. To address this, ...
  </details>

- **2026-11-18** — Yash Jangir, Karan Mirakhor, Renos Zabounidis et al. — [Render the Robot, Generate the World: One Video World Model Across Embodiments](http://arxiv.org/abs/2611.24925v1)
  <details><summary>📄 Abstract</summary>
  Predicting the consequences of an agent's actions requires modeling both the body's motion and the environment's response. Most video world models attempt to learn both from numerical actions, even though geometry and kinematics already specify the intended motion. We introduce Doppel, an embodiment-agnostic video world model conditioned on camera-aligned renderings of future body configurations and numerical action trajectories. By explicitly providing the intended motion, Doppel can focus on p...
  </details>

- **2026-11-18** — Hemen Taukoor, Zhaoxia Wang, Venky Shankararaman — [The Limit Is in the Input, Not the Model: State-Dependent Command Safety in Natural-Language Interfaces to Industrial Controllers](http://arxiv.org/abs/2611.24682v1)
  <details><summary>📄 Abstract</summary>
  Language models judging commands to industrial controllers may not receive machine state, the equipment's current condition. The same command can require opposite safety decisions in different states, so an incorrect answer may reflect missing information rather than poor reasoning. We propose an answerability audit: does the model receive the information needed to decide? The audit records the model's inputs and pairs the same command with two states requiring opposite answers. The paired score...
  </details>

- **2026-11-18** — Rui Li, Liyang He, Zheng Zhang et al. — [Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow](http://arxiv.org/abs/2611.23751v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but rely on workflow-specific hooks authored per environment. We present AnyS1, a framework that turns human-authored procedural skills, whose instructions naturally specify where choices arise and which options apply, into a...
  </details>

- **2026-11-18** — Xingyu Zhao — [Reliability is a user-specific property of large language models](http://arxiv.org/abs/2611.23732v1)
  <details><summary>📄 Abstract</summary>
  Public benchmarks support comparisons of large language model (LLM) capabilities, yet users can experience the same highly ranked model differently. Drawing on traditional software reliability, we argue that the reliability of an LLM service should be assessed for specified users and conditions of use. This requires more than a capability score: evaluation evidence must support a claim about failure during future operation. We distinguish testing to discover faults from testing to assess reliabi...
  </details>

- **2026-11-18** — Wenhao Li, Zhongyi Han, Yuhao Wei et al. — [Towards Pose-Robust Few-Shot Vision-Language-Action Models](http://arxiv.org/abs/2611.24360v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base stay exactly where they were during data collection: a bumped tripod or a base re-docked a few centimetres away makes it reach for the wrong place. We show that both failures are one phenomenon, a change of the camera-to-base extrinsic that the policy has memorised, and that the rob...
  </details>

- **2026-11-18** — Artur Kuramshin, Charlotte Cloutier, Michael Przystupa et al. — [Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need](http://arxiv.org/abs/2611.23676v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with multi-fingered robots. In this work, we study how to best adapt VLAs to dexterous hands by pairing supervised fine-tuning (SFT) with diffusion-steering reinforcement learning (DSRL). Using $π_{0.5}$ a...
  </details>

- **2026-11-18** — Jiahao You, Ziye Jia, Chao Dong et al. — [Cooperative UAV and Ground Station for Robust MEC of Dynamic Aquatic IoT: A Generative AI-Enhanced Approach](http://arxiv.org/abs/2611.24466v1)
  <details><summary>📄 Abstract</summary>
  The increasing aquatic Internet of Things (AIoTs) require computational support and coverage in applications such as maritime search and rescue. Unmanned aerial vehicles (UAVs) can offer low-cost, flexible aerial services, and ground stations (GSs) can provide powerful supports, which can cooperate to help the AIoTs in complex scenarios. However, the collaboration between UAVs and GSs for AIoTs faces challenges of task uncertainties, AIoTs trajectory uncertainties, heterogeneities, and limited c...
  </details>

- **2026-11-18** — Zihang Wang, Wenkai Zhu, Lingdong Kong et al. — [One Affinity, Two Axes: Bidirectional Slot Attention for Iterative Aggregation across the Structure--Detail Spectrum in Visual Retrieval](http://arxiv.org/abs/2611.24371v1)
  <details><summary>📄 Abstract</summary>
  Aggregating dense patch tokens into compact and discriminative global descriptors is central to visual retrieval. Although foundation models provide rich local features, existing aggregation heads still rely on single-pass mappings and lack an explicit mechanism to coordinate structural and fine-grained cues. Therefore, we propose Bidirectional Slot Attention (BiSA), which reformulates aggregation as an iterative coupled system. Cross-Axis Consensus (CAC) progressively refines learnable slots by...
  </details>

- **2026-11-18** — Aditya Gandhamal, Aniruddh Sikdar, Arya Kishor et al. — [Pixel2Perspective: A Benchmark for Multi-Modal and Multi-View Generalization in Vision-Language Models](http://arxiv.org/abs/2611.24327v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI systems, such as drones and autonomous vehicles, improve navigation by enhancing perception in environments containing unseen objects. While Visual Language Models (VLMs) offer strong image understanding, their real-world application is underexplored. For effective deployment, open-vocabulary semantic segmentation (OVSS) models, leveraging models like CLIP to assign pixel-level labels from text, must be robust to outdoor conditions, adverse weather, and varying viewpoints. Despite th...
  </details>

- **2026-11-18** — Jun Wang, Fengpeng Li, Wei Han et al. — [Benchmarking Reasoning Reliability,Prior_Evidence Contrast,and Spectral Discrimination in Remote-Sensing Geological Image Interpretation](http://arxiv.org/abs/2611.24068v1)
  <details><summary>📄 Abstract</summary>
  Reliable lithology interpretation requires accurate geological recognition and reasoning grounded in visual evidence. Although Multimodal Large Language Models show promise in remote sensing, their reliability in geological interpretation remains unclear. We introduce HyGeoBench, a diagnostic benchmark of 10,000 questions based on hyperspectral imagery across three dimensions: reasoning reliability, prior_evidence contrast, and spectral discrimination. It covers ten task types, with both multipl...
  </details>

- **2026-11-18** — Dipan Bartaula, Anuj Shrestha, Ankit Belbase et al. — [CURVTON-205K: A Mask-Free Difficulty-Stratified Synthetic Dataset for Robust and Scalable Virtual Try-On](http://arxiv.org/abs/2611.24042v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in 2D virtual try-on (VTON) have largely focused on architectural innovation, yet robust performance in diverse real-world conditions remains challenging. We argue that failure modes in VTON, such as inaccurate occlusion handling, unconstrained poses, and poor coverage of under-represented garments and appearance factors, are tightly coupled to dataset design choices and long-tail data regimes. We present a scalable data generation pipeline that coordinates specialized editing an...
  </details>

- **2026-11-18** — Miaomiao Wei, Huaiyuan Chen, Xinnan Shao et al. — [Convolution-Augmented Transformer for Robust Blind CFO Estimation in LEO Satellite Communication System](http://arxiv.org/abs/2611.23987v1)
  <details><summary>📄 Abstract</summary>
  Low Earth Orbit (LEO) satellite communications are essential for achieving ubiquitous global connectivity. However, the high mobility of LEO satellites induces massive Doppler shifts and fast time-varying fading, severely impairing signal synchronization. Accurate Carrier Frequency Offset (CFO) estimation is critical for receiver synchronization. Nevertheless, conventional estimators and deep learning approaches often degrade significantly under highly dynamic, low-SNR conditions. To address the...
  </details>

- **2026-11-18** — Hamza Ruzayqat, David M. Bortz, Vanja Dukić — [WAIVES: Weak-form Asymptotically-unbiased Instrumental-Variable Estimation for SDEs](http://arxiv.org/abs/2611.23951v1)
  <details><summary>📄 Abstract</summary>
  Weak-form methods have transformed inference for deterministic dynamical systems. By integrating the governing equations against smooth, compactly supported test functions, they trade noise-amplifying differentiation for noise-attenuating integration, yielding fast and robust estimates. Extending this idea to stochastic differential equations (SDEs) has proven harder, and a consistent single-trajectory formulation has remained out of reach. Applied naively in the time domain, the weak form makes...
  </details>

- **2026-11-18** — Zhe Dong, Fang Qin — [Evaluating invariance training with certified answer-changing controls in neural graph algorithms](http://arxiv.org/abs/2611.23907v1)
  <details><summary>📄 Abstract</summary>
  Invariance training aims to make neural algorithmic reasoners robust to answer-preserving input changes and is judged by accuracy and by how rarely such edits change predictions. We ask whether this evaluation detects lost sensitivity to answer-changing edits on minimum spanning trees of synthetic graphs, where both directions can be certified. Attaching a subgraph through one bridge provably preserves every original label. Attaching it through two edges, oracle-selected to change a label, and l...
  </details>

- **2026-11-18** — Siddique Latif, Moid Sandu, Farrukh Pervez et al. — [Great Listeners, Poor Decision-Makers: Rethinking Agentic Audio AI](http://arxiv.org/abs/2611.23847v1)
  <details><summary>📄 Abstract</summary>
  Audio artificial intelligence (AI) now recognizes speech, sounds, and music remarkably well, yet voice agents still act when they should not: they execute commands addressed to others, act on misheard content, and commit before the user finishes speaking. This position article argues that the bottleneck in agentic audio AI has shifted from recognition to decision-making. We propose a reference architecture with an explicit decision layer, separate from perception and reasoning, that chooses whet...
  </details>

- **2026-11-18** — Gaoxiang Linghu, Haonan Zhou, Xuanhe Liu et al. — [GaussLearner: 3D Gaussian Primitives as Self-Regulating Continual Learners](http://arxiv.org/abs/2611.23736v1)
  <details><summary>📄 Abstract</summary>
  Continual learning of 3D Gaussian fields aims to maintain faithful reconstructions of the evolving world. However, directly fine-tuning an existing Gaussian field on new observations can cause catastrophic forgetting of previously reconstructed content. To address this challenge, existing methods employ selective local optimization, replay, or parameter regularization, yet still struggle to balance adaptation to scene changes with preservation of still-valid content. Our key insight is to view 3...
  </details>

- **2026-11-17** — Mohammed Gharib, Sam Burns, Martin Zizi — [A-Tag: Cryptographic File Tagging with Enforced Live Human Presence](http://arxiv.org/abs/2611.23602v1)
  <details><summary>📄 Abstract</summary>
  The increasing autonomy of software agents and the proliferation of AI-generated content have weakened the reliability of digital actions as evidence of human involvement. Existing mechanisms, such as digital signatures and authentication protocols, verify identity and integrity, but do not establish whether a live human was present at the time an action was performed. In this paper, we introduce A-Tag, a system for verifiable human-in-the-loop tagging of digital artifacts. A-Tag cryptographical...
  </details>

- **2026-11-17** — Kaiwen Shi, Zheyuan Zhang, Changzhi Liu et al. — [Receiver-Conditioned Clarification for Multi-Agent Food Assistance](http://arxiv.org/abs/2611.23572v1)
  <details><summary>📄 Abstract</summary>
  Food insecurity creates a pressing need for guidance that helps households find usable food resources and assess food choices in light of their circumstances. Such guidance must connect eligibility requirements, practical access constraints, and dietary needs rather than return isolated listings or generic nutritional advice. Multi-agent food assistants can coordinate these tasks, with uncertainty indicating when clarification or verification is needed before a recommendation. However, uncertain...
  </details>

- **2026-11-17** — Mahvash Jebeli, Mohammad Eslami, Nazlee Zebardast et al. — [Beyond Accuracy: Benchmarking Uncertainty Quantification in Retinal Disease Screening](http://arxiv.org/abs/2611.23344v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty quantification (UQ) is essential for evaluating retinal AI systems beyond classification accuracy, yet it remains unclear whether existing UQ strategies generalize across diseases, model architectures, and reliability criteria. We introduce a large-scale, multi-disease benchmark comprising over $242,000$ fundus photographs from $32$ datasets covering diabetic retinopathy, age-related macular degeneration, and glaucoma. We evaluate six representative UQ strategies across thre...
  </details>

- **2026-11-17** — Haofan Wu, Le Zhang — [MedHarness: A Unified Budgeted Runtime for Reliable Medical Imaging Agents](http://arxiv.org/abs/2611.23501v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging agents already return answers on heterogeneous imaging surfaces, yet deployment still faces a limited verification budget where each wrong accept can harm clinical trust. When a thin check and a deeper evidence pass disagree on the same case, deciding when to stop, open more evidence, repair, or reject without a shared controller remains ill-posed. Tool-using workflows often lock a surface-specific evidence order per dataset, or a private always-open full-depth verification path;...
  </details>

- **2026-11-17** — Jiarui Guo, Saining Zhang, Jiaying Wan et al. — [RFW-S: Everyday Deformable Objects with Independent Simulation Verification](http://arxiv.org/abs/2611.23056v2)
  <details><summary>📄 Abstract</summary>
  Large-scale robotic simulation requires diverse deformable objects with executable physical properties and realistic interaction behaviors. However, existing 3D asset collections primarily emphasize visual diversity, while scalable physical construction and verification remain challenging. We introduce RFW-S, a large-scale dataset of 83,365 simulation-verified assets spanning 485 everyday categories across five structural families: soft solids, cloth sheets, shells, garments, and bags. We develo...
  </details>

- **2026-11-17** — Ting-Hsuan Chen, Siheng Zhao, Han Jiang et al. — [Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](http://arxiv.org/abs/2611.22275v2)
  <details><summary>📄 Abstract</summary>
  Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically cou...
  </details>

- **2026-11-17** — Sijia Zhong, Tamir Yirga, Yijia Ma et al. — [Dreaming Up Authors: Factual Prevalence and LLM Hallucinations in Academic Authorship Attribution](http://arxiv.org/abs/2611.23530v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are widely used for question answering but are prone to hallucinations, yet the underlying causes, particularly the role of factual prevalence in training data, remain underexplored. In this work, we study this through academic authorship attribution, hypothesizing that hallucinations are more likely for less prevalent papers. Using citation count as a proxy for factual prevalence, we curate a dataset of 1.92 million papers across eight scientific disciplines with st...
  </details>

- **2026-11-17** — Amrit Lal Singh, Smarak Kanjilal — [RageVLA: Augmentation-Trained Perception and Action for State-of-the-Art Robustness on LIBERO](http://arxiv.org/abs/2611.23517v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models look saturated on LIBERO, yet most of them fall apart on LIBERO-PRO as soon as an object moves or the instruction asks for something new. We argue that what is missing is not scale but decoupling.   In these policies, what to do is tied to where things were during training, to the scene around them and to the wording of the instruction. We cut these ties in two places. In the data, LIBERO demonstrations are re-arranged by general rules: every object and fixtur...
  </details>

- **2026-11-17** — Søren Taverniers, Eric Darve, Hamdi A. Tchelepi — [Reliability by Architecture: Agentic Workflows for Validated Multi-Physics Simulation from Natural Language](http://arxiv.org/abs/2611.23473v1)
  <details><summary>📄 Abstract</summary>
  Preparing, executing, and validating strongly coupled multi-physics simulations require expert time. Agentic workflows use large language models (LLMs) to coordinate them from natural-language descriptions, but reliability requires checks of physical consistency and fidelity to the problem description. Our agentic harness implements explicit task allocation: LLMs interpret user requests and simulator diagnostics, generate input components not covered by predefined construction rules, and propose...
  </details>

- **2026-11-17** — Deepak Waghmare, Shaad Sufi — [Can You Undo It? Reversibility Classes for AI Agent Actions](http://arxiv.org/abs/2611.22075v1)
  <details><summary>📄 Abstract</summary>
  Tool-using AI agents change files, databases, access rights and public information, yet permission to call a tool does not establish whether a mistake can be undone. We present Reversibility Classes, a declared five-level vocabulary with argument-sensitive rules, conservative defaults and an explicit prior-state capture contract. The pinned implementation and evidence-linked registry cover 536 tools across 20 MCP servers. All 738 rule-case checks conform to declared expectations, while native an...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 14 papers

- **2026-11-19** — Divya Acharya, Thomas M. Roehr, Arnaud Gotlieb — [Trustworthy Geospatial AI Workflows: Reproducible Maritime Analytics and Forecasting on Open-Source AIS Data](http://arxiv.org/abs/2611.25884v1)
  <details><summary>📄 Abstract</summary>
  Publicly available geospatial data provide increasing opportuni- ties for data-driven maritime analytics and predictive modelling. However, their availability does not necessarily imply that the underlying observations are equally suitable for downstream AI applications. Properties of the data source and observation pro- cess, including provenance, reporting regularity, spatial coverage, observation density, and missingness, can affect how geospatial data are interpreted, processed, and ultimate...
  </details>

- **2026-11-19** — Natasha E Blycha, James Myint, Chen Feng et al. — [Law at the Speed of AI: Critical Legal Infrastructure for the Machine Age: Autonomy Under Law Architecture (AULA)](http://arxiv.org/abs/2611.25985v1)
  <details><summary>📄 Abstract</summary>
  The global deployment of autonomous AI agents within and across organisations exceeds the governance infrastructure available to constrain it. Agent communication and authentication protocols, principally the Model Context Protocol and the Agent2Agent Protocol, are maturing quickly, but maturity at the protocol layer does not produce legal legibility at the governance layer. Runtime enforcement written by the deploying organisation fixes the resources an AI agent can reach, not the authority und...
  </details>

- **2026-11-19** — Matteo Baldan, Chiara D'Ercoli, James Rowbottom et al. — [GraphEP: A Calibrated Data System and Benchmark for Learning Cardiac Electrophysiology](http://arxiv.org/abs/2611.26551v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity simulations generate spatiotemporal data that are difficult to obtain experimentally, yet their outputs are rarely ready for scientific machine learning. Cardiac electrophysiology (EP) exemplifies this challenge: data reside on anatomy-dependent volumetric meshes, propagation follows anisotropic material fields, and relevant events span multiple temporal scales. We introduce GraphEP, a calibrated data system that converts cardiac meshes and simulation protocols into compact, graph-...
  </details>

- **2026-11-19** — K. R. Jayaram, Vatche Isahagian, Aswath Vaithinathan Aravindan et al. — [How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents](http://arxiv.org/abs/2611.26361v1)
  <details><summary>📄 Abstract</summary>
  LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short \emph{lessons} from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of \emph{guidelines}, where each guideline records how many lessons it merged. At inference the agent receives either all gui...
  </details>

- **2026-11-19** — Nuzhat Khan, Muhammad Paend Bakht, Ab Al-Hadi Ab Rahman et al. — [Explainable AI for Solar PV Power Forecasting: From Model Selection to Trustworthy, Reproducible Deployment](http://arxiv.org/abs/2611.25894v1)
  <details><summary>📄 Abstract</summary>
  Machine learning (ML) is now a standard tool for forecasting the output of solar photovoltaic (PV) plants, yet published accuracy figures are often hard to compare and harder to trust. Many studies validate with random splits, report no reference forecast, and present feature attributions without saying what they can and cannot show. This paper reviews the main families of ML methods for PV power forecasting and resource assessment, from tree ensembles to deep and foundation models, and sets out...
  </details>

- **2026-11-19** — Ahmad Hussein, Ali Anaissi, Mukesh Prasad et al. — [An Explainable and Scalable Hierarchical Tensor Framework for Integrating Multi-Omics and Digital Pathomics](http://arxiv.org/abs/2611.25584v1)
  <details><summary>📄 Abstract</summary>
  Background: Precision oncology requires integration of heterogeneous molecular and pathology data, yet many fusion models offer limited biologically grounded interpretability and struggle with missing modalities.   Methods: We present Hierarchical Interpretable Tensor Fusion (HIT-Fuse), integrating six modalities: somatic copy number variation, DNA methylation, RNA sequencing, microRNA expression, RPPA protein abundance, and vision transformer-derived pathomics across four TCGA cohorts (glioma, ...
  </details>

- **2026-11-19** — Noah Sturgill, Jinho D. Choi — [ChronoDossier: Long-Form Personas as Temporal Memory Representations](http://arxiv.org/abs/2611.25407v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents rely on stored records to recover a person's state as facts change. Reliable answers depend on how facts are recorded, retrieved, and presented to the reader. We treat a long-form persona dossier as a memory representation of a known latent state, an invariant identity plus a timeline of facts, routines, and decision rules tied to life phases. We present ChronoDossier, a benchmark of 311 synthetic dossiers of 1k-10k words written by seven generators from dated timelines. Intr...
  </details>

- **2026-11-18** — Meenakshi Rajpurohit, Anna Phan, Ravikumar Komandur Narayanan et al. — [FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification](http://arxiv.org/abs/2611.25071v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) write fluent financial analyses but miscompute ratios, recall stale prices, and route questions to the wrong tool with high confidence. We ask which component should do each job in a financial question-answering assistant, and study it with FinVeriQA, an open-source multi-agent research prototype over SEC filings and live market data: a compact typed-decision model (Laya) routes each question and screens out advice requests, Python computes every number, retrieval an...
  </details>

- **2026-11-18** — Auntor Chakma, Mst. Farhana Akter, Abu Henaf Rashid Ahmad Mufti et al. — [RespCCT and FreqCCT: Compact, Explainable and Cost-Aware Convolutional Transformers for Multi-Class Respiratory Disease Classification](http://arxiv.org/abs/2611.24323v1)
  <details><summary>📄 Abstract</summary>
  Chest auscultation depends on the listener, and software that classifies lung sounds could give a second reading where trained listeners are scarce. The most accurate published classifiers fine-tune large pretrained networks, and their accuracy is rarely reported with running cost or paired statistics. This study makes three contributions. (i) It proposes RespCCT and FreqCCT, two compact convolutional transformers of 173,187 and 124,999 parameters that learn from random initialization on mel, co...
  </details>

- **2026-11-18** — Dowling Wong — [Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics](http://arxiv.org/abs/2611.23678v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each keep or discard decision can be traced to its evidence. We propose evaluating such systems on their experimental process as well as their outcome, and we build a governed harness that makes this possible. A control plane, n...
  </details>

- **2026-11-17** — Rukmangadh Sai Myana, Sumit Kumar Jha, Yanzhao Wu — [Entropy-Regularized Integrated Gradients for Stable Feature Attribution](http://arxiv.org/abs/2611.23600v1)
  <details><summary>📄 Abstract</summary>
  Path-based attribution methods like Integrated Gradients (IG) are widely used to interpret neural networks, yet imperceptible input perturbations can drastically alter their attribution maps while leaving model predictions unchanged. We introduce Entropy-Regularized Integrated Gradients (ERIG), a path-based attribution method that intrinsically attenuates gradient irregularities along the integration path using maximum-entropy softmax weighting with temperature parameter $τ$. We quantify the eff...
  </details>

- **2026-11-17** — Jiangyun Zhang, Zhou Tang, Kristen Surrao et al. — [ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents](http://arxiv.org/abs/2611.23588v1)
  <details><summary>📄 Abstract</summary>
  Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements. We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory architecture in which the agent's memory evolves from its own failures without updating model weights, tools, or workflow logic. ARISE uses the model itself or a teacher model to attribute the failures and propose correctio...
  </details>

- **2026-11-17** — Xinyuan Li, Yi Nian, Xiaoqin Feng et al. — [Image Watermarking With Memory Across Reissuance](http://arxiv.org/abs/2611.23363v1)
  <details><summary>📄 Abstract</summary>
  Publishers often revise and reissue images, yet valid watermarks may persist on superseded releases or unapproved edits. Even a current release can contain regions last authorized at different revisions. We introduce and formalize reissuable provenance: determining an image's current, superseded, or unissued status and recovering each region's last authorized revision (its generation), with abstention when evidence is insufficient. Generational Stratigraphy Fields (GSF) combine watermark evidenc...
  </details>

- **2026-11-17** — Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal et al. — [Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate](http://arxiv.org/abs/2611.22461v1)
  <details><summary>📄 Abstract</summary>
  Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so five mechanisms from the agent-memory literature can be removed independently under a fixed budget, each gated on a pre-declared threshold. Across 39 runs one survives: preserving contradictions and passing the ranked co...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-11-18** — Zeguan Xiao, Zhuocheng Liang, Yun Chen et al. — [CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning](http://arxiv.org/abs/2611.24654v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in adapting large language models (LLMs) is capability preservation: an adaptation can achieve its target while degrading general capabilities. We introduce CurvDelta, a scalable framework that incorporates the preservation constraint into the parameterization of the model update. By analyzing the local geometry of the preservation constraint around the pre-adaptation model, CurvDelta constructs a low-curvature space in which parameter updates leave the preservation loss near...
  </details>

- **2026-11-18** — Haowei Chen, Yichen Wang, Congfu Xu — [Kernel Ridge Attention: Nonlinear Memory with Selective Forgetting](http://arxiv.org/abs/2611.23896v1)
  <details><summary>📄 Abstract</summary>
  Kernel Ridge Attention (KRA) is a recurrent sequence mixer that combines learned nonlinear features with covariance-guided memory updates. It stores associations through recursive ridge regression, using correlations among past keys to determine how new observations modify memory. A content-dependent Ornstein--Uhlenbeck transition controls retention and restores uncertainty for future writes. This construction admits an exact temporal-kernel interpretation and maintains an inference state whose ...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-19** — Almene De Meran Meguimtsop, Daniel E. Acuna — [Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science](http://arxiv.org/abs/2611.25492v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) support scientific research, but some of that assistance can also undermine research integrity. Existing safety evaluations in science often measure whether models refuse misconduct requests, but rarely explain whether they even recognize the problem or why they comply. We investigate this gap across 8 LLMs using SciIntBench, an existing benchmark of 1,350 prompts about scientific research integrity. We examine the reasons behind compliance in four steps. First, when...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 1 papers

- **2026-11-17** — Uzma Shafiq, Matthew England, Nayyar Zaidi — [A Survey on the Use of Machine Learning within Computer Algebra](http://arxiv.org/abs/2611.23361v1)
  <details><summary>📄 Abstract</summary>
  This survey explores the use of Machine Learning (ML) in the field of Computer Algebra (CA), both to optimise existing CA algorithms, and to perform symbolic computation directly. Traditional symbolic methods, while mathematically rigorous, often are computationally expensive thus limiting their use in real-world applications. Recent advances have shown that data-driven techniques can address these limitations by guiding heuristic decisions, selecting optimal algorithms, predicting structural pr...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 180 papers

- **2026-11-19** — Yicheng Cai, Taegyu Kim, Peng Liu — [Backtracking Agent Applications Security Incidents](http://arxiv.org/abs/2611.26525v1)
  <details><summary>📄 Abstract</summary>
  Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. The main artifacts available for backtracking are trajectory logs, which record agent functionalities, and source code; app(lication)-specific function call logs are often fairly limited. However, trajectory logs are at the agent functionality abstractio...
  </details>

- **2026-11-19** — Andrew Kang — [Monte Carlo Pass Search for Setpieces](http://arxiv.org/abs/2611.26464v1)
  <details><summary>📄 Abstract</summary>
  Set pieces produce about a third of non-penalty expected goals (xG), yet they are usually evaluated by what happened next. We present Monte Carlo Pass Search (MCPS) for set pieces, which treats a corner or a lofted free kick as a distribution over plausible executions and plausible futures instead of a single realised event. From the pre-kick state, MCPS proposes counterfactual deliveries and counterfactual set-ups (where the attackers stand at the kick), plays each out many times in a world mod...
  </details>

- **2026-11-19** — Jiawei Xing, Li Wang, Xiangtao Meng et al. — [ChronoPatch: Black-Box Energy-Latency Attacks on Vision-Language Models](http://arxiv.org/abs/2611.26117v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly deployed as generative inference services, where autoregressive decoding makes response length a key determinant of latency and computational cost. This creates an availability risk: adversarial visual inputs can prolong generation and increase serving overhead. Existing energy-latency attacks typically rely on gradients, logits, or token-level feedback, leaving open whether such risks persist when an attacker observes only the final response. We pr...
  </details>

- **2026-11-19** — Qike Zhang, Jiaju Han, Xuelian Shi et al. — [Wearable Logo, Silent Hijack: Stealthy Cross-Modal Semantic Attacks on Visible--Infrared Vision-Language Models](http://arxiv.org/abs/2611.25437v1)
  <details><summary>📄 Abstract</summary>
  Logos appear naturally on clothing and daily necessities, where their recognizable shapes and semantic associations make them familiar visual cues. This familiarity helps them blend into real-world environments and remain visually inconspicuous. We ask whether an existing logo can serve as a carrier for coordinated targeted semantic attacks on visible-infrared (VIS-IR) vision-language models (VLMs) without changing its original outline. This setting requires expressive adversarial variation with...
  </details>

- **2026-11-19** — Ahmet Efe, Recep Bugra Uludag, Ulya R. Karpuzcu — [Verified Netlist-to-RTL Recovery with LLM Agents](http://arxiv.org/abs/2611.25324v1)
  <details><summary>📄 Abstract</summary>
  Gate-level netlists circulate among IP integrators and foundries and can be extracted from chips. Reverse engineering them into readable register-transfer-level (RTL) code would help an adversary understand and modify a design, but remains difficult because word-level operations are scattered across many gates. Large language models (LLMs) can write and optimize RTL, but often fail to recover it from a whole netlist. We propose LOCA (LOgic Cone Attack), an LLM-based attack that divides an anonym...
  </details>

- **2026-11-19** — Tuna Han Salih Meral, Kaan Oktay, Alec Helbling et al. — [RL Post-Training in Diffusion Transformers Is Activation Steering](http://arxiv.org/abs/2611.26627v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them requires learning complex, input-dependent transformations. To isolate how much of these gains an input-independent shift explains, we probe each RL-tuned model with a deliberately sim...
  </details>

- **2026-11-19** — Yiyan Ji, Qixun Wang, Yang Shi et al. — [Coda-DaVinci: Reimagining Video Generation with Code2Video](http://arxiv.org/abs/2611.26595v1)
  <details><summary>📄 Abstract</summary>
  Code2Video uses agent-authored 3D proxies to guide video generation, enabling explicit control over structure and dynamics. However, how to construct proxies and prompts for optimal downstream quality remains underexplored, as do the capabilities and limitations of this paradigm. Through controlled experiments and blinded human evaluation, we study proxy granularity, physics simulation, and prompting. The results reveal task-dependent trade-offs: coarse proxies favor natural motion, while medium...
  </details>

- **2026-11-19** — Tanmay Sah — [A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained Weights](http://arxiv.org/abs/2611.26450v1)
  <details><summary>📄 Abstract</summary>
  Pretrained language models (LMs) remain unreliable on exact multi-digit arithmetic without gradient fine-tuning or external tool interpreters. We introduce closed-form, zero-gradient circuit-grafting primitives that compile deterministic computation directly into pretrained LM weights using zero training examples and zero runtime hooks, while bounding per-layer normalization drift and preserving natural-language (NL) competence. Our construction combines three analytical mechanisms: (1) two-laye...
  </details>

- **2026-11-19** — Xiaoming Sun, Chengu Wang — [Degree Lower Bounds for Symmetric Boolean Functions: Breaking the Prime-Gap Barrier](http://arxiv.org/abs/2611.26446v1)
  <details><summary>📄 Abstract</summary>
  We prove that every nonconstant symmetric Boolean function on $n$ variables has exact real polynomial degree at least $n-O(n^{1/3}(\log n)^{2/3})$. This makes progress toward the conjecture of von zur Gathen and Roche that the degree is always at least $n-3$. The original prime-gap argument of von zur Gathen and Roche yields a degree deficit of $O(n^{0.525})$ using the theorem of Baker, Harman, and Pintz, or $O(n^{0.52})$ using an estimate claimed in a recent preprint. Our $\widetilde{O}(n^{1/3}...
  </details>

- **2026-11-19** — Xufei Tian, Han Hu, Wenli Du — [Context as a Resource](http://arxiv.org/abs/2611.26346v1)
  <details><summary>📄 Abstract</summary>
  Managing concurrent tasks across separate agent sessions quickly exhausts human attention, motivating always-on personal agents behind a single continuous interface. Yet when every context shares identical frozen backbone weights, funneling interleaved dialogues and external events into one linear session induces cross-topic constraint bleed and head-of-line stalling. Conversely, router-ticket hierarchies incur lossy prose handoffs, heavy routing overhead, and blind merges - collapsing true-conf...
  </details>

- **2026-11-19** — Guojian Zhan, Jiahao Xu, Yahui Liu et al. — [ResVision: Spectrum-Matched Resizing and Context-Preserving Inspection for Visual Reasoning](http://arxiv.org/abs/2611.26318v1)
  <details><summary>📄 Abstract</summary>
  Agentic visual reasoning improves vision-language models by selectively enlarging evidence without adding new scene content, but the benefit depends on whether fine structure remains accessible and whether local observations stay grounded in the full scene. We identify three recurring bottlenecks: high-frequency detail can be attenuated during visual-token formation; spatially distributed evidence can remain encoded yet difficult for the language model to retrieve; and isolated crops can weaken ...
  </details>

- **2026-11-19** — Mehmet Sinan Yıldırım, Ke Zhang, Shuai Wang et al. — [Language-Oriented Semantic Modeling for Target Language Extraction](http://arxiv.org/abs/2611.26317v1)
  <details><summary>📄 Abstract</summary>
  Target Language Extraction (TLE) aims to isolate speech in a target language from multilingual mixtures. Existing approaches primarily rely on acoustic modeling with language identity labels, which provide only coarse categorical guidance. In this work, we propose a language-oriented semantic modeling framework that augments acoustic extraction with language-specific semantic representations. A pre-trained speech semantic model is adapted via language-aware prompt conditioning and parameter-effi...
  </details>

- **2026-11-19** — Daniele Lunghi, Alberick Euraste Djiré, Zacharie Chenail-Larcher et al. — [Static Analysis Guidance for Secure LLM Code Generation](http://arxiv.org/abs/2611.26312v1)
  <details><summary>📄 Abstract</summary>
  Static analyzers are cheap and widely deployed, which makes their reports a candidate feedback signal for secure LLM code generation. Existing approaches place the analyzer inside an iterative repair loop with intermediate steps, which is costly and makes it hard to isolate the report's effect on the model. We introduce two strategies that give the finding to the model during generation. When the analyzer raises an alert, generation is rolled back, and the finding is inserted either as a code co...
  </details>

- **2026-11-19** — Yifan Bai, Yantao Li, Jian Yu et al. — [Paper2Lean: Agentic Autoformalization of Mathematical Research Papers at Scale](http://arxiv.org/abs/2611.26272v1)
  <details><summary>📄 Abstract</summary>
  Formalizing a mathematical research paper requires more than translating isolated theorems: statements and proofs must remain semantically faithful to the source and globally consistent across long-range dependencies. We introduce Paper2Lean, an end-to-end agentic framework that converts mathematical research papers into integrated Lean projects. The framework extracts mathematical content into a dependency graph and coordinates specialized agents for statement formalization, semantic checking a...
  </details>

- **2026-11-19** — Tianyi Xu, Boyang Lyu, Yunkai Tang et al. — [StreamEgo: Streaming Exocentric-to-Egocentric Video Generation](http://arxiv.org/abs/2611.26165v1)
  <details><summary>📄 Abstract</summary>
  Exocentric-to-egocentric (Exo2Ego) video generation transforms third-person recordings into first-person viewpoints, unlocking immersive AR/VR experiences and scalable demonstration synthesis for embodied robotics. Extending it to a streaming setting is expected to further enable live applications. However, existing methods suffer from degraded manipulation regions, overfitting and confinement to fixed-length clips with prohibitive latency. To address these limitations, we present StreamEgo, a r...
  </details>

- **2026-11-19** — Frederike Oetker, Charlotte Geertman — [Public-Private Cooperation in the Port of Rotterdam: An Agent-Based Toy Model of Cooperative Efforts Against Cocaine Trafficking](http://arxiv.org/abs/2611.26154v1)
  <details><summary>📄 Abstract</summary>
  Cocaine trafficking poses a persistent governance challenge in the Port of Rotterdam (PoR), requiring cooperation between public and private actors. This paper develops an Agent-Based toy Model (ABM) coupled with a Causal Loop Diagram (CLD) to explore interactions between trust, cooperation, competition, pressure, enforcement, and actor skills in public-private cooperation (PPC). Based on empirical data of PPC in the PoR, we explore responses to parameter shocks across different initial configur...
  </details>

- **2026-11-19** — Yuqi Guo, Michael Wray — [Better Retrieval, Not Better Binding: Pretraining Exposure in Egocentric Video Retrieval](http://arxiv.org/abs/2611.26120v1)
  <details><summary>📄 Abstract</summary>
  Video-language models (VLMs) achieve strong performance on video-text retrieval and are increasingly used for egocentric video understanding. Yet, despite gains in zero-shot retrieval, they have shown limitations in compositional understanding, and it remains unclear whether they understand compositional relationships between verbs and nouns. In this work, we introduce Ego-ExBind, a compositional diagnostic protocol for analyzing pretraining exposure and verb-noun binding in egocentric video-tex...
  </details>

- **2026-11-19** — Jiahao Hu, Jingdong Du, Yichen Zhang et al. — [HiUni: Harmonizing Understanding and Generation in Shared Visual Space](http://arxiv.org/abs/2611.26107v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal models aim to support visual understanding and generation within a single framework. However, prevailing approaches often separate their visual representations or backbone computation to accommodate the different requirements of these two tasks, which limits the degree of unification. In this paper, we present HiUni, which revisits this design choice and explores whether a pretrained vision language model can be directly extended into a unified model with extensive parameter s...
  </details>

- **2026-11-19** — Yuxiang Wang, Junhao Gan, Jianzhong Qi — [SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet Agents](http://arxiv.org/abs/2611.26069v1)
  <details><summary>📄 Abstract</summary>
  Spreadsheets are widely used for data analysis and supporting decision-making. Automating spreadsheet analysis while protecting sensitive data and controlling deployment costs motivates locally deployed open-weight large language models (LLMs). Meanwhile, complex spreadsheet tasks require both task reasoning and workbook understanding, while predefined operation interfaces impose additional tool-selection and invocation demands. We introduce SheetAlign, a spreadsheet manipulation framework with ...
  </details>

- **2026-11-19** — Lu Ying, Can Liu, Yuxiao Yang et al. — [Presenting Your Figures: Data-informed Animated Transitions Across Scientific Figure Panels](http://arxiv.org/abs/2611.26036v1)
  <details><summary>📄 Abstract</summary>
  Multi-panel figures are commonly used in research papers to show scientific data, and researchers often reuse them when presenting their work. Presenting these figures often involves explaining how data across chart panels are related. Animated transitions can progressively reveal these relationships, but two static panels specify only the endpoints, leaving what intermediate keyframes should show and how the transition should progress unclear. To support transition design across diverse scienti...
  </details>

- **2026-11-19** — Emre Uğur, Jiawen Qi, Qinyu Chen — [DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention](http://arxiv.org/abs/2611.25938v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly need to process long documents and codebases, making long-context attention a major prefill bottleneck. Block sparse attention reduces computation by skipping unimportant blocks of the attention matrix, but scoring blocks accurately can itself be expensive. We propose Delta-Based Tile Scoring (DTS), a training-free, content-adaptive tile scoring method for sparse block attention. DTS selects query and key anchors according to local vector changes, using ...
  </details>

- **2026-11-19** — Muhammad Rafid, Golshan Famitafreshi, Vasilis Avgerinos et al. — [Coordinated Offloading: Cooperative Multi-Agent Reinforcement Learning for the Edge-Cloud Continuum](http://arxiv.org/abs/2611.25932v1)
  <details><summary>📄 Abstract</summary>
  The increasing demand for intelligent, low-latency services in edge-cloud continuum systems poses new challenges for dynamic and efficient task offloading. We propose a Multi-Agent Reinforcement Learning (MARL) framework for distributed task offloading under partial observability, where each device offloads only a portion of its computation to a target edge server while executing the remaining portion locally (partial offloading). The problem is formulated as a Markov Decision Process (MDP), whe...
  </details>

- **2026-11-19** — Yutong Guan, Meixing Shi, Haoran Sun et al. — [EvoMem: Self-Evolving Skills for Time-Aware Long Video Memory Agents](http://arxiv.org/abs/2611.25889v1)
  <details><summary>📄 Abstract</summary>
  Although memory-augmented architectures have expanded the ability of large vision-language models (LVLMs) to process long videos, existing retrieval processes still largely rely on global semantic matching and lack state-driven temporal control, often returning fragmented or redundant evidence and failing to maintain a coherent evidence chain. To address this challenge, we propose EvoMem, a time-aware long-video memory agent guided by self-evolving retrieval skills. EvoMem constructs a hierarchi...
  </details>

- **2026-11-19** — Ziyang Xu, Peng Han, Hai Zhou — [From Sequence to Space: Explicit Spatial Belief with Vision-Language Distillation for Active Geo-Localization](http://arxiv.org/abs/2611.25866v1)
  <details><summary>📄 Abstract</summary>
  Active geo-localization (AGL) asks an agent to navigate a small aerial search grid and reach a target specified by an aerial image, a ground-level photograph, or text. Existing methods align the goal modalities well, but they keep the navigation state inside a large sequential Transformer and train with a dense distance reward that uses the hidden goal location. This paper proposes EAGLE, an Explicit spatial-belief Agent for Geo-Localization and Exploration. Offline training jointly optimizes a ...
  </details>

- **2026-11-19** — Pangjing Wu, Xu Yuan, Wenqi Fan et al. — [LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature](http://arxiv.org/abs/2611.25845v1)
  <details><summary>📄 Abstract</summary>
  Current research agents are moving beyond academic search toward literature synthesis and experiment planning. These workflows increasingly rely on literature retrieval systems, which serve as standalone systems or as components of research agents. However, existing scientific literature retrieval benchmarks mainly evaluate these methods using topical relevance or citation links as supervision, which cannot capture which prior methods are used for empirical comparison. To address this gap, we in...
  </details>

- **2026-11-19** — Hui Cai, Kangcheng Deng, Tianyi Ma et al. — [Auto-Alpha: A Framework for Autonomous Factor Research](http://arxiv.org/abs/2611.25732v1)
  <details><summary>📄 Abstract</summary>
  Autonomous factor research requires generating economic hypotheses as well as implementing and testing them. We present Auto-Alpha, a framework that connects report-guided initialization to self-directed research through a test-driven implementation loop. An idea agent proposes economic mechanisms and signal constructions; a research agent develops them with backtest feedback. Semantic audit, quantitative review, and human admission select factors for a persistent library, while an Experience Li...
  </details>

- **2026-11-19** — Yanjing Li, Sheng Xu, Baochang Zhang et al. — [Efficient Latent Reasoning for Vision-Language Model via Dynamics-Aware Quantization and Distillation](http://arxiv.org/abs/2611.25670v1)
  <details><summary>📄 Abstract</summary>
  Efficient chain-of-thought (CoT) reasoning in vision-language models (VLMs) requires reducing both intermediate reasoning steps and their execution cost. Latent CoT methods compress textual rationales into continuous thoughts, yet their full-precision (FP) models retain substantial storage and computation costs. Lowering numerical precision could reduce these remaining costs, yet direct quantization severely degrades reasoning accuracy, particularly with 4-bit weights and activations. Operator a...
  </details>

- **2026-11-19** — Jingyi Zhou, Yi Liu, Bin Sun et al. — [GRODE-RTL: Source-Mapped Dependency Views for LLM-Based RTL Repair](http://arxiv.org/abs/2611.25661v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models show great potential for automated Register-Transfer Level repair, yet they struggle with non-local faults where root causes and failing outputs reside far apart in source code. Treating RTL as a flat token sequence obscures hardware dataflows, whereas exposing complete synthesized graphs overwhelms the model with fine-grained metadata. To resolve this representation dilemma, we propose GRODE-RTL, an anchor-centric representation that extracts the single-clock-stage fan-in ...
  </details>

- **2026-11-19** — Jinpeng Lu, Haoyuan Shi, Yuanshen Guan et al. — [CaT-Movie: Balancing Global Planning and Local Rendering for Long Multi-Shot Video Generation](http://arxiv.org/abs/2611.25620v1)
  <details><summary>📄 Abstract</summary>
  Current multi-shot video generators render only limited durations per pass, requiring long movies to be stitched from local segments across which narrative progression and visual identity drift. To synthesize long-horizon movies with Coherence across Time, we present CaT-Movie, a multi-shot generation system consisting of a global story planner and a local window renderer. The planner expands user requests via a large language model to preserve, infer, and complete story details, while determini...
  </details>

- **2026-11-19** — Seungho Song, Donggyu Lee, Jaehan Kim et al. — [Measuring Hallucination in Large Language Models for Cyber Threat Intelligence: An Exploratory Study](http://arxiv.org/abs/2611.25590v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in cyber threat intelligence (CTI) tasks, such as summarization and question answering. However, they may produce hallucinations, false or misleading content not grounded in the source text, which can mislead analysts and corrupt downstream security decisions. This paper presents an exploratory measurement study of hallucinations in LLM-based CTI. We introduce HalluVision, a reproducible framework that generates LLM outputs, extracts domain-spec...
  </details>

- **2026-11-19** — Taeoh Hong — [AZOWL AgentOps: Task-Scoped Governance for Deployed Agent Applications](http://arxiv.org/abs/2611.25562v1)
  <details><summary>📄 Abstract</summary>
  AZOWL AgentOps provides shared governance for deploying agents and delegating work to them. Human and agent senders can exchange messages or explicitly delegate a business task. Accepted work has a stable identifier that links the sender's authority, the assigned runner, any required approval, and result evidence. The default enrolled customer PC profile is read-only. We compare AZOWL components with a configured LangGraph application in 28 synthetic runs across four paired pilots. Original AZOW...
  </details>

- **2026-11-19** — Semin Kim, Ju Yeon Kang, Sunghwan Ahn et al. — [Joint Language Modeling for In-the-Wild Speech-Scene Generation with Distinct Token Representations](http://arxiv.org/abs/2611.25503v1)
  <details><summary>📄 Abstract</summary>
  Speech-scene generation aims to synthesize intelligible target speech together with diverse environmental sounds as a coherent acoustic scene. The task is considered challenging in two respects. Speech and environmental audio differ substantially in their semantic and acoustic characteristics, yet existing approaches typically model the complete scene using a single mixed acoustic representation. At the same time, the two sounds are closely related in real-world speech scenes, whereas convention...
  </details>

- **2026-11-19** — Xin Zhang, Tujie Xu, Zhiyi Chen et al. — [VisualTalk-Bench: Evaluating Question-Driven Avatar-Led Video Explanations](http://arxiv.org/abs/2611.25444v1)
  <details><summary>📄 Abstract</summary>
  Advances in video generation and avatar synthesis enable new ways to answer user questions through visual explanations. This task requires a system to formulate a correct answer, translate relevant information into visual material, and deliver the explanation through an avatar's speech and actions. Existing benchmarks rarely assess whether avatars point to the visual content being discussed. We introduce VisualTalk-Bench for question-driven avatar-led video explanations in finance and Chinese an...
  </details>

- **2026-11-19** — Ferran Hermida-Rivera, Jack Toubes, Angela Cui et al. — [BOOMerang: Autonomous Translation from RTL to Microarchitectural Simulators and Back](http://arxiv.org/abs/2611.25438v1)
  <details><summary>📄 Abstract</summary>
  High-level simulators like gem5 are often used to test and demonstrate novel architectural techniques. While these simulators provide high research productivity, they generally lack the means to provide detailed feedback on the realizability of a hardware design. Furthermore, these simulators can frequently fall out-of-sync with the detailed performance characteristics of real hardware designs, which is usually the responsibility of dedicated engineers/teams in industry. While RTL implementation...
  </details>

- **2026-11-19** — Ben Kang, Junda Wang, Yuxuan Yuan et al. — [DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings](http://arxiv.org/abs/2611.25419v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have greatly improved input understanding in universal multimodal embedding models. However, this understanding does not ensure that their embeddings preserve the evidence needed to distinguish relevant items from confusable alternatives. To preserve essential discriminative evidence in embeddings, this paper proposes DiLE, a discrimination-aware latent-space learning framework that combines task guidance with on-policy retrieval feedback. Specifically, a few lea...
  </details>

- **2026-11-19** — Drew Fudenberg, Florian Mudekereza — [Cognitive Constraints and Misspecification Concern](http://arxiv.org/abs/2611.25368v1)
  <details><summary>📄 Abstract</summary>
  We study repeated decision problems in which an agent has cognitive constraints and is concerned that her models might be misspecified. She first uses data to weight candidate models, subject to a cognitive-capacity constraint on the complexity she can process, and then she evaluates choices according to how well they perform under those models. More data need not overcome limited capacity: a statistically inferior but simpler model can remain relevant in the long run. When the constraint binds,...
  </details>

- **2026-11-19** — Bochen Han, Anshu Xiong, Mingyang Ma — [Incorporating argumentation frameworks for LLM decision-making: Task-specific design and evaluation](http://arxiv.org/abs/2611.25361v1)
  <details><summary>📄 Abstract</summary>
  Argumentation frameworks (AFs) provide explicit, formal mechanisms for representing and resolving conflicts and thus have been incorporated into large language model (LLM) decision-making. The benefits vary and depend on how arguments and their relations are constructed, evaluated, and incorporated into the decision process. {We abstract a workflow consisting of four stages based on existing argumentation-augmented methods} and investigate their design choices over tasks of debate-based decision...
  </details>

- **2026-11-19** — Jungmin Park, Eunha Kim, Wooseop Kim et al. — [From FIPS to FPGA with LLM Agents: Measuring What Tests and Reviews Miss in Post-Quantum Cryptographic Hardware](http://arxiv.org/abs/2611.25339v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly generate RTL alongside the tests and reviews that validate it, self-generated evidence is a weak foundation for trustworthy hardware. We present our seven-stage verification-gated workflow, evolved during a post-quantum design port, in which a gate counts only if shown able to fail on negative controls and fault mutants, and reviewer agents audit work before commit. We then audit this evidence with tool-selected netlist mutants, flaw replays, and formal checks. The flo...
  </details>

- **2026-11-19** — Rui Hong, Jana Košecká — [MoGloss: Joint Motion and Pseudo-Gloss Pretraining for American Sign Language Understanding](http://arxiv.org/abs/2611.25333v1)
  <details><summary>📄 Abstract</summary>
  Sign language translation and recognition have been shown to benefit from various pretraining approaches. We propose a novel two-stage pretraining approach for the motion encoder, which first learns to reconstruct masked motion, followed by joint masked prediction of pseudo-gloss units and motion. Pseudo-glosses serve as an intermediate structured representation of natural language text and are obtained from the captions by a large language model. We curate a corpus of about 1,100 hours of Ameri...
  </details>

- **2026-11-19** — Sergey Musienko — [When Should Deployed BCI Decoders Adapt? A Resource-Priced Ladder for Frozen EEG Trunks](http://arxiv.org/abs/2611.25315v1)
  <details><summary>📄 Abstract</summary>
  When should a deployed MI decoder spend adaptation resources-not only how to adapt under shift? We study a thin control layer outside a frozen encoder: a resource ladder (factory -> Bayesian head -> affine map, with full fine-tune as an escape hatch) governed by regime-aware gating under a utility that prices accuracy, fit time, and label cost. The head is Bayesian in the conjugate sense: a Normal-Inverse-Wishart prior over the class conditional Gaussians in embedding space, updated in closed fo...
  </details>

- **2026-11-19** — Shuning Lin, Engui Fan — [Painlevé transcendents in the defocusing Hirota equation with non-zero boundary conditions](http://arxiv.org/abs/2611.25308v1)
  <details><summary>📄 Abstract</summary>
  We consider the Cauchy problem for the defocusing Hirota equation with non-zero boundary conditions \begin{align*} &iq_t+ q_{xx}-2\left(|q|^2-1\right)q +i\left(q_{xxx}-6|q|^2q_x\right)=0,\\ &q(x,0)=q_0(x)\to\pm 1, \quad x\to\pm\infty, \end{align*} which can be characterized using a Riemann-Hilbert problem through the inverse scattering transform. With the $\bar{\partial}$-steepest descent method and double scaling limit technique, we derive the long-time asymptotics of the solution in two transi...
  </details>

- **2026-11-19** — Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan et al. — [The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models](http://arxiv.org/abs/2611.26545v1)
  <details><summary>📄 Abstract</summary>
  Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about knowledge, where a lie and an honest denial can be identical. We widen a published persona bank with roles that deny knowledge they have, plus honest counterparts. At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of...
  </details>

- **2026-11-19** — Zilang Cen, Chao Tang, Fangcheng Liu et al. — [Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation](http://arxiv.org/abs/2611.26341v1)
  <details><summary>📄 Abstract</summary>
  Large multimodal models can support long-horizon robot manipulation, but frequent model calls incur substantial latency and token costs. The central challenge is determining when agent assistance or intervention is needed and whether errors require correcting robot execution, subtask planning, or both. To address this problem, we propose RoC (Reasoning on Call), an efficient framework that coordinates a low-level policy and a high-level reasoning agent through an online task-state monitor. The m...
  </details>

- **2026-11-19** — Xingyi Wang, Bin Li, Jiyuan Shi et al. — [ECHO: In-Context Behavior foundation model for Humanoid Whole-Body Control](http://arxiv.org/abs/2611.25778v1)
  <details><summary>📄 Abstract</summary>
  Humanoid behavior foundation models (BFMs) acquire diverse skills through large-scale motion imitation and massively parallel reinforcement learning, yet broad behavioral capability does not ensure precise execution across physical conditions. Without distinguishing the underlying dynamics, policies may favor conservative compromises over environment-specific precision. We introduce ECHO, an in-context BFM that turns interaction experience into environment-specific control, separating general be...
  </details>

- **2026-11-19** — Yijun Liu, Shijia Ge, Tongtong Feng et al. — [TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation](http://arxiv.org/abs/2611.25553v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned video prediction lets robots anticipate the visual consequences of their actions for planning and policy evaluation. Existing predictors denoise each future from noise without using their own estimate of it, which limits the quality of the predicted future, in particular of the manipulated objects, and requires many network calls. We present TwoPass, a self-conditioned training-and-inference framework that keeps the standard flow-matching objective. Self-Generated Draft Traini...
  </details>

- **2026-11-19** — Qiman Wu, Hanlin Chen, Yuhua Wei et al. — [TuringPAI: A Foundation for On-Device Physical AI](http://arxiv.org/abs/2611.25474v1)
  <details><summary>📄 Abstract</summary>
  Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transforme...
  </details>

- **2026-11-19** — Linfeng Dong, Jianwei Niu, Jiuyi Zhao et al. — [ActMem: From Latent Memory Reasoning to Grounded Robotic Action](http://arxiv.org/abs/2611.25461v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.   However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full   history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past   experience to decide what to do, while perception guides how to act. W...
  </details>

- **2026-11-19** — Ana E. Sanchez Villalobos, Michael D. Quinn, Aakash Tyagi et al. — [Verify the Verifier: Specification-Grounded LLM Cross-Checking for Bugs That Escape UVM Scoreboards](http://arxiv.org/abs/2611.26588v1)
  <details><summary>📄 Abstract</summary>
  A passing UVM regression shows the design agrees with the reference model on what the scoreboard checks, not that it meets the specification. Bugs that pass every test yet violate the specification, termed scoreboard escapes, survive mature testbenches. We present Verify the Verifier, to our knowledge the first framework whose LLM-based Anomaly Cross-Checker examines a passing regression's traces against the specification. Of 564 bugs inserted into four OpenTitan IPs, 68 are candidate scoreboard...
  </details>

- **2026-11-19** — George Rahul, Ronit Jahilal, Bhaskara Hanuma Vedula et al. — [LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits](http://arxiv.org/abs/2611.26538v1)
  <details><summary>📄 Abstract</summary>
  Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. Auditing such intersectional subgroups remains a challenge: their number grows quadratically, and there is no agreed baseline for what independent attributes would predict. Without such a baseline, many existing audits flag a subgroup when it exceeds each attribute alone, a condition that attributes acting independently already sati...
  </details>

- **2026-11-19** — Francesco Caporali, Jason M. Altschuler, Boris Hanin — [A new algorithmic approach for finding flat minima: critically damped Polyak stepsizes](http://arxiv.org/abs/2611.26475v1)
  <details><summary>📄 Abstract</summary>
  We present a new adaptive stepsize rule that biases gradient descent toward flatter minima in both theory and practice, and establish the first uniform-in-time guarantees for both sharpness and loss reduction for a broad class of locally quadratic objectives. Our critically damped Polyak (CDP) stepsizes multiply the classical Polyak rule by $4$ and a mild damping factor. The factor $4$ is critical in that it produces equioscillations around the manifold of minimizers $\mathcal{M}$ to leading ord...
  </details>

- **2026-11-19** — Antoine Bellemare-Pepin, Philipp Thölke, Yann Harel et al. — [Introducing ReTiNA-Cinema: Real-Time Neuro-Augmented Cinema via Generative AI](http://arxiv.org/abs/2611.26469v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (AI) is currently revolutionizing content creation across various media. Between those who fear it will replace human creativity and those who regard it solely as a tool, many in the creative industries are beginning to view generative AI as a collaborator. Yet interaction with these systems often relies on discrete, turn-based prompting that can interrupt flow and constrain expression to symbolic text. We explore physiological signals as a source of continuous...
  </details>

- **2026-11-19** — Jihong Zhang, Zijing Jin, Mingfeng Xue — [Reasoning-Trace Analysis Using Large Language Models for Interpretable Q-Matrix Construction](http://arxiv.org/abs/2611.26422v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate Q-matrices for diagnostic classification models that approximate expert specifications, but evaluations have focused on the final matrices, leaving the basis of individual item-attribute assignments unexamined. This opacity limits the responsible use of AI in measurement. We propose Reasoning-Trace Analysis (RTA), a framework in which an LLM generates attribute-labeled reasoning steps through chain-of-thought (CoT) prompting and these steps are analyzed ...
  </details>

- **2026-11-19** — Kaiwen Zhang, Yiming Gao, Zeqi Xiao et al. — [ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step](http://arxiv.org/abs/2611.26389v1)
  <details><summary>📄 Abstract</summary>
  Current leading video generation models can synthesize highly realistic videos, while still frequently violating physical and logical constraints in multi-step reasoning and planning, even after training with large-scale reasoning data or existing diffusion RL methods. We attribute these failures to the conventional video training paradigm, which treats a solution as a fixed-length clip rather than a chain of decisions. We present ViDecide, a decision-centric framework that trains video diffusio...
  </details>

- **2026-11-19** — Francesco Belardinelli, Flavio Corradini, Matteo Leonesi — [ClosureBench: A Benchmark for Reasoning under Closure Assumptions](http://arxiv.org/abs/2611.26335v1)
  <details><summary>📄 Abstract</summary>
  AI agents built on large language models (LLMs) often answer questions from incomplete records. Missing information might be interpreted as unknown or false, depending on the completeness of the source. Current evaluations fail to distinguish these two aspects, as they are usually interwoven with other reasoning demands. We present ClosureBench, a benchmark that tests whether LLMs follow the stated rules for dealing with missing information. Every base scenario is tested under OWA, CWA, and LCWA...
  </details>

- **2026-11-19** — Marc Jansen — [Client Exits - A Way to Increase LLM Transparency on the Client Side](http://arxiv.org/abs/2611.26309v1)
  <details><summary>📄 Abstract</summary>
  Textual recommendations generated by large language models (LLMs) can be difficult to inspect. This paper introduces \emph{Client Exits}, a lightweight mechanism for enriching LLM responses while separating semantic intent from client-specific presentation. The model inserts predefined, machine-interpretable markers into its output, and the receiving client decides whether and how to realize the corresponding enrichments. This allows supplementary information to be presented as graphics, text, s...
  </details>

- **2026-11-19** — Marc Jansen — [What If Chain-of-Thought Is Not Enough?](http://arxiv.org/abs/2611.26282v1)
  <details><summary>📄 Abstract</summary>
  Reasoning capabilities in large language models have evolved from prompting-based methods to internalized model behaviors. In this paper, we investigate whether the internal thinking model of an LLM can be deliberately changed and whether such a change is beneficial. Instead of relying on Chain-of-Thought, we train models to follow Question--Option--Criteria (QOC), a structured decision process that decomposes a task into explicit questions, competing options, and evaluation criteria. We present...
  </details>

- **2026-11-19** — Shenghua Liu, Youssef Faragalla, Surya Ganguli et al. — [Revealing Pathway Interactions in Network Computations with Complete Path Contribution](http://arxiv.org/abs/2611.26101v1)
  <details><summary>📄 Abstract</summary>
  Networks pass signals through many layers of interconnected units, so explaining what they compute means tracing how information travels from input to output and how pathways interact. Most existing approaches analyze only pairwise interactions between components such as units, layers or attention heads. Even when these measurements are combined post hoc into a circuit, they do not capture higher-order interactions along full causal chains (paths) from input to output, and so cannot address how ...
  </details>

- **2026-11-19** — Alper Kalle, Theo Rudkiewicz, Mohamed-Oumar Ouerfelli et al. — [Complete-SVD: A Functional Norm Approach to Low-Rank LLM Compression](http://arxiv.org/abs/2611.26059v1)
  <details><summary>📄 Abstract</summary>
  Post-training low-rank compression of neural networks must not only approximate the original weights but also preserve the model's input-output behavior. Recent output-aware methods measure the compression error beyond the compressed layer, at the model output, weighting logit changes by the observed next token or by the model's predicted probabilities. We propose Complete-SVD, a method for large language models that minimizes the $L_2$ distance between the logits of the original and compressed ...
  </details>

- **2026-11-19** — Zekun Wang, Yizhuo Wang — [FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models](http://arxiv.org/abs/2611.26020v1)
  <details><summary>📄 Abstract</summary>
  Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions. Saving states on a coarse grid wastes reusable prefixes, whereas existing fine-grained exact caches must cut the prefill forward pass at each mid-prompt checkpoint, adding scheduler steps that outweigh the reuse gains under load.   We observe that across multi-turn chat, agent loops, document question answering, and tree search, prefix reuse almost alwa...
  </details>

- **2026-11-19** — Qin-Wen Luo, Haoxuan Gao, Sheng Ren et al. — [Policy Improvement-Guided Replay for Continual Reinforcement Learning](http://arxiv.org/abs/2611.25989v1)
  <details><summary>📄 Abstract</summary>
  Continual reinforcement learning (CRL) requires models to acquire new capabilities while retaining performance on previous tasks. A stability-oriented perspective common in conventional continual learning emphasizes knowledge preservation and interference mitigation. Complementing this perspective, we revisit CRL for vision-language models through policy improvement, a fundamental principle of RL, to preserve acquired performance gains. Using the performance difference lemma, we characterize his...
  </details>

- **2026-11-19** — Aljoscha Felix Baumann, Reyhaneh Ghassemizadeh, Daniel F. Urban — [Alloying effects on the interface cohesion of grain boundaries in the Ni--Fe--Cr system](http://arxiv.org/abs/2611.25944v1)
  <details><summary>📄 Abstract</summary>
  Grain boundaries (GBs) in polycrystalline Ni-based alloys strongly influence mechanical strength and fracture behavior, yet the effect of alloying elements such as Fe and Cr on GB cohesion remains difficult to quantify systematically. Using density functional theory (DFT), we compute rigid-body separation (RBS) curves for six symmetric-tilt Ni GBs, extracting the work of separation $W_{\mathrm{sep}}$ and maximum traction $σ_{\max}$ via the universal binding energy relation (UBER). We find that s...
  </details>

- **2026-11-19** — Edgar A. Duéñez-Guzmán, Eduardo Dueñez, Edgar Said Hernandez Sanchez et al. — [The Price of an Explanation: What Demanding Verifiable Artifacts Costs, and What It Buys Back](http://arxiv.org/abs/2611.25896v1)
  <details><summary>📄 Abstract</summary>
  Generative models produce many candidate solutions but provide no intrinsic signal by which to rank them. One mitigation is to demand a \emph{verifiable artifact}: a program that can be executed against the available evidence. A common concern is that requiring executable verification incurs costs in both solution quality and computational budget. We measure these two costs on the $120$-task ARC-AGI-2 evaluation set. Demanding a verifiable artifact from an LLM reduced the score from $93$ to $68$...
  </details>

- **2026-11-19** — Nicholas Teh — [Closing Gaps in Temporal Fair Division for Chores](http://arxiv.org/abs/2611.25892v1)
  <details><summary>📄 Abstract</summary>
  We study the fair division of indivisible chores that must be assigned in a prescribed order. The complete instance is known in advance, but assignments cannot be changed. Temporal envy-freeness up to one chore (TEF1) requires envy-freeness up to one chore after every arrival. For goods, TEF1 allocations need not exist, and deciding whether one exists is NP-hard. For chores, Elkind et al. (AAMAS 2025) showed that TEF1 allocations exist for two agents, but left open whether they always exist, con...
  </details>

- **2026-11-19** — Paul Werner, Wiebke Bennecke, Jan Philipp Bange et al. — [momipy: A time-resolved momentum microscopy data analysis workflow](http://arxiv.org/abs/2611.25888v1)
  <details><summary>📄 Abstract</summary>
  Photoemission momentum microscopy is an emerging approach to photoelectron spectroscopy that is transforming electronic band structure mapping at both laboratory-based and large-scale facilities. Its extension to time-resolved measurements has recently enabled major advances, ranging from the femtosecond imaging of exciton wavefunctions to dark-field photoelectron microscopy of light-induced dynamics and strong light-matter interactions. However, the rapid acquisition of high-dimensional data se...
  </details>

- **2026-11-19** — Hiro Kataoka, J{é}r{ô}me Euzenat, Koji Hasebe — [Coherent belief and opinion propagation produces more echo chambers: corrected version](http://arxiv.org/abs/2611.25879v1)
  <details><summary>📄 Abstract</summary>
  The occurrence of echo chambers is a well-known phenomenon in social networks. Echo chambers are groups of agents satisfying three properties: homogeneity, i.e., sharing the same opinion, segregation, i.e., listening primarily to agents of the same group, and reinforcement, i.e., increasing opinion similarity over time. Opinion dynamics models have been used to explain how echo chambers occur through agents updating their opinions. However, social network users also exchange beliefs supporting t...
  </details>

- **2026-11-19** — Sivakameswara Reddy Chejarla — [Anchor and Check: Deterministic Cross-Prompt, Cross-Model Reconciliation for Auditable LLM Decisions](http://arxiv.org/abs/2611.25818v1)
  <details><summary>📄 Abstract</summary>
  Pipelines that let a large language model (LLM) make discrete decisions need to know which decisions they may act on unattended, and a record that explains each one. We study a small, fully specified reconciliation contract: commit the target model's greedy answer (the anchor), draw one or two greedy checks that reach the answer by a different route (an alternate prompt, or a model from another family), and let a pure function return one of five outcomes, of which only Agree is acted on. On 48,0...
  </details>

- **2026-11-19** — Yucheng Du, Yi Nian, Ruixue Lian et al. — [Interpreting DeepStack-Style Vision-Language Models: Do Input or Deeper-Layer Visual Tokens Drive Answers?](http://arxiv.org/abs/2611.25713v1)
  <details><summary>📄 Abstract</summary>
  DeepStack-style vision-language models feed visual tokens to the language model at its input, and again at deeper layers. We call these the main entry and the later entries. What do the later entries add when the model already has the image? We give the entries versions that differ in one object's color and see which one the answer follows. On photographs, the original DeepStack follows the later entries, while Qwen3-VL-8B/32B follow the main entry. Does weakening the main entry give the later f...
  </details>

- **2026-11-19** — Baoliang Chen, Xinlong Bu, Lingyu Zhu et al. — [Slide2PPT: Native PowerPoint Reconstruction with Localization-Guided Refinement](http://arxiv.org/abs/2611.25708v1)
  <details><summary>📄 Abstract</summary>
  Image-to-slide reconstruction must recover both visual appearance and native object structure for subsequent editing. Yet visually faithful charts and tables may lack editable series and cells, and direct code generation couples content prediction to rendering implementation. We present Slide2PPT, a model-agnostic, training-free framework that equips both open- and closed-source vision-language models with native PowerPoint reconstruction capabilities. Through a unified typed interface, the mode...
  </details>

- **2026-11-19** — Jiayi Chen, Lizhe Chen, Yujia Chen et al. — [CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks](http://arxiv.org/abs/2611.25673v1)
  <details><summary>📄 Abstract</summary>
  As language-model agents are applied to increasingly extended tasks, their working context continuously accumulates interaction history, tool observations, intermediate decisions, and task progress. Context compaction offers a practical way to reduce this growing history while allowing execution to continue, yet the compaction ability of modern LLMs remains insufficiently understood. We introduce CompAct-Bench, a benchmark for evaluating working-context compaction through its downstream effect o...
  </details>

- **2026-11-19** — Xuanyu Zhu, Qian Tan, Bo Chen et al. — [MatVerse: A Foundation Model for Materials Science](http://arxiv.org/abs/2611.25651v1)
  <details><summary>📄 Abstract</summary>
  Materials science involves highly heterogeneous scientific information, including textual knowledge, molecular and crystal structures, experimental characterization data, microscopy images, and structure-property relationships. Developing a general-purpose foundation model capable of understanding and reasoning over these diverse materials representations remains challenging. In this technical report, we introduce MatVerse, a materials foundation model built upon Intern-S2-Preview and further sp...
  </details>

- **2026-11-19** — Shotaro Ishihara — [Generative News Recommendation Reproduces Popularity: A Memorization-Based Analysis](http://arxiv.org/abs/2611.25606v1)
  <details><summary>📄 Abstract</summary>
  Text-based generative recommenders can go beyond ranking existing items by directly generating item titles or other textual representations. In the news domain, this raises a societal concern that models may repeatedly surface already popular articles and thereby narrow the diversity of information to which users are exposed. We investigate training-data memorization as one mechanism behind this concentration. Using approximately 20 million browsing sessions from a Japanese news service, we cont...
  </details>

- **2026-11-19** — Zihan Xiao, Boshen Xu, Pei Fu et al. — [VidToC: Rethinking Video Token Compression for Multimodal Large Language Models](http://arxiv.org/abs/2611.25574v1)
  <details><summary>📄 Abstract</summary>
  Extending multimodal large language models (MLLMs) from images to videos faces substantial memory and latency challenges due to the massive number of visual tokens. These challenges have driven the development of numerous visual token compression methods and more efficient LLM architectures. However, existing compression methods are often evaluated with different training setups, tasks, and models, making fair comparison difficult. Meanwhile, the growing use of hybrid Mamba-Transformer architect...
  </details>

- **2026-11-19** — Yilong Chen, Yuan Guo, Jie Xu — [An LLM-Orchestrated Agent Framework for CKM-Assisted Network Deployment Optimization](http://arxiv.org/abs/2611.25556v1)
  <details><summary>📄 Abstract</summary>
  Channel knowledge maps (CKMs) offer reusable, site-specific radio priors to facilitate environment-aware network planning. However, deploying heterogeneous network nodes to meet diverse performance requirements in complex environments is challenging and requires executable workflows that coordinate scene preparation, candidate-site specification, CKM construction, optimization, and validation. This paper presents a large language model (LLM)-orchestrated agent framework for CKM-assisted network ...
  </details>

- **2026-11-19** — Younghwan Joo, Jeonghoon Han, Sanghyun Oh et al. — [A four-level executable validation protocol for evaluating LLM-generated topology specifications of physics-based HVAC digital twins](http://arxiv.org/abs/2611.25471v1)
  <details><summary>📄 Abstract</summary>
  Physics-based digital twins of air conditioning, a principal energy consumer in manufacturing and buildings, can be generated automatically from a declarative specification of its equipment, connections, and sizing. Large language models (LLMs) now write such specifications from plain-language descriptions. Evaluations of these specifications stop at parse success, completed runs, or textual similarity, and cannot reject a model that converges in simulation but is physically wrong. In this study...
  </details>

- **2026-11-19** — Jiani Cao, Anna Korhonen, Chen Cecilia Liu — [PILAPS: A Bilingual Benchmark for Evaluating Pragmatic Inference across Phenomena and Settings](http://arxiv.org/abs/2611.25459v1)
  <details><summary>📄 Abstract</summary>
  Recent work reports strong pragmatic performance by large language models (LLMs) in English, yet whether this performance generalises across languages and evaluation settings remains unclear. This question is increasingly important as LLMs are deployed across languages, cultures, and conversational contexts. In this paper, we first introduce PILAPS, a bilingual English/Mandarin Chinese benchmark covering eight pragmatic phenomena across purpose-written and dialogue-derived items, with both cultu...
  </details>

- **2026-11-19** — Tongda Xu, Yu Zhang, Jun Hu et al. — [Lossless Latent Diffusion Models](http://arxiv.org/abs/2611.25454v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of training image diffusion models while preserving pixel-exact reconstruction. Prior works typically address this problem by directly modeling images in pixel space, requiring modifications to the diffusion training objective or model architecture. In this work, we introduce a different paradigm: rather than modifying diffusion models, we construct a lossless transformation that maps pixels into a representation more amenable to diffusion modeling. We term our approach the ...
  </details>

- **2026-11-19** — Huixin Zhan, Jason H. Moore — [From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs](http://arxiv.org/abs/2611.25422v1)
  <details><summary>📄 Abstract</summary>
  Genomic foundation models provide variant-level evidence, but connecting that evidence to phenotype hypotheses requires accounting for uncertainty throughout structured reasoning. We introduce an uncertainty-conditioned path-energy framework that converts sequence predictions and calibrated predictive uncertainty into explicit distributions over graph-supported phenotype hypotheses, without patient-level phenotype supervision. An interpretable learned energy scores admissible gene--disease--phen...
  </details>

- **2026-11-19** — Zhengbo Zhou, Dooman Arefan, Shandong Wu — [Bilateral Evidence Selection and Reasoning for Mammography Vision--Language Models](http://arxiv.org/abs/2611.25418v1)
  <details><summary>📄 Abstract</summary>
  Medical vision--language models (VLMs) often need to identify small, subtle lesions within high-resolution images containing extensive normal anatomy and redundant visual information. Visual-token compression improves efficiency, but preserving salient regions alone can discard the context needed for diagnostic interpretation. This context can extend across images: in bilateral mammography, the opposite breast provides a patient-specific anatomical reference. Yet retaining such evidence does not...
  </details>

- **2026-11-19** — Siyang Chen, Yuan Pu, Yuhan Qin et al. — [SGLayout: Schema-Guided Closed-Loop Refinement for LLM-Driven Parameterized Layout Generation](http://arxiv.org/abs/2611.25410v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong potential in parameterized layout generation via tool-augmented code synthesis. However, LLMs lack spatial awareness, making one-shot generation unreliable. While layout quality can be evaluated with established techniques, a critical gap remains: geometric-domain evaluation outcomes cannot be directly translated into actionable code-level fixes, trapping iterative refinement in blind refactoring. We propose SGLayout, a self-refining framework that ...
  </details>

- **2026-11-19** — Yuxuan Li, Derrick Goh Xin Deik, Zheng-Peng Duan et al. — [HOPD: Historical On-Policy Distillation for SAR MLLM Continual Learning](http://arxiv.org/abs/2611.25391v1)
  <details><summary>📄 Abstract</summary>
  Continual SAR interpretation requires multimodal large language models to learn incoming sources while retaining earlier task abilities. This is difficult when acquisition and geographic shifts alter visual evidence, regionally concentrated categories bias answers, and historical images are scarce. We address this problem with Historical On-Policy Distillation (HOPD), which reuses source-acquisition LoRA states as persistent teachers for one evolving student. Archiving each state before consolid...
  </details>

- **2026-11-19** — Kota Kaneko, Kohei Motegi, Jun Sato — [Semiclassical Averaging and Temporal Fluctuations of Quantum Dark Solitons in the Lieb-Liniger Model](http://arxiv.org/abs/2611.25343v1)
  <details><summary>📄 Abstract</summary>
  We study the time evolution of quantum dark-soliton states of the Lieb--Liniger model, introduced by Sato--Kanamoto--Kaminishi--Deguchi as equal-weight superpositions of one-hole yrast states, and their relation to Gross--Pitaevskii (GP) solitons. We consider a simultaneous weak-coupling and large-system limit in which the repulsive coupling constant $c$ tends to zero and the particle number $N$ and ring circumference $L$ tend to infinity, with the mean density $\bar n=N/L$ and scaled circumfere...
  </details>

- **2026-11-18** — Mírian Silva, Serena Oduro — [Whose Safety? Addressing Anti-Blackness in the Age of AI Safety](http://arxiv.org/abs/2611.25302v1)
  <details><summary>📄 Abstract</summary>
  "AI safety" has grown from a niche contingent of actors into the dominant framing for artificial intelligence (AI) assessment and evaluation, overshadowing AI ethics. Through political and monetary influence, AI safety has shifted political focus within the US and abroad. The focus has shifted away from harms that currently affect the public toward threats framed as "existential risks". We argue that safety cannot be achieved while anti-Blackness is left unaddressed. We ground this argument in S...
  </details>

- **2026-11-18** — Anh Tien Nguyen, Dimitris Samaras, Mahdi S. Hosseini — [Separating Interpretability and Reconstruction in Sparse Autoencoders](http://arxiv.org/abs/2611.25165v1)
  <details><summary>📄 Abstract</summary>
  Sparse Autoencoders (SAEs) are effective tools for mechanistic interpretability by decomposing neural representations into sparse and interpretable features. However, a single sparse representation in traditional SAEs is responsible for both reconstruction fidelity and interpretability, which are not guaranteed to align. To separate these objectives, we propose DualSAE, a modular framework that augments standard SAEs with a plug-in Residual Branch. A standard SAE serves as the Sparse Branch, lea...
  </details>

- **2026-11-18** — Nianjun Zhou, Dhaval Patel — [An LLM-Agentic Framework for Intelligent Work Order Management in Industrial Maintenance](http://arxiv.org/abs/2611.25070v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an AI-driven framework, CodeReAct agent, designed to enhance industrial equipment maintenance through natural language (NL) interactions. The framework employs an advanced AI agentic approach to interpret human instructions, providing knowledge extraction, asset status summarization, and work order recommendations. It identifies patterns and trends and predicts work orders by standardizing industrial data into business objects (BOs) and utilizing analytical function API calls...
  </details>

- **2026-11-18** — Chrisantus Eze, Christopher Crick — [Verify2Act: Critic-Guided Latent World Models for Verifying Language-Conditioned Manipulation Plans](http://arxiv.org/abs/2611.25243v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) can propose multi-step manipulation plans, but they have no grounded model of how a scene will change, and the pixel-level world models that could check those plans are slow and drift over long horizons. We present Verify2Act, a modular verification framework that separates semantic action proposal from latent physical verification. A VLM proposes candidate plans, a latent world model (V2A-WM) imagines each of them in the DINOv2 feature space, and a dual-head critic...
  </details>

- **2026-11-18** — Zirui Song, Jiadong Zhang, Zheng Lu et al. — [Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated Manipulation Benchmarks](http://arxiv.org/abs/2611.25179v1)
  <details><summary>📄 Abstract</summary>
  Simulated manipulation benchmarks measure policy performance using hand-written success checkers that label each episode as a success or failure. Passing an expert demonstration shows that a checker accepts one way of completing the task. Learned policies, however, may stop after partial progress or complete the task in a different way. A checker may then accept an incomplete execution (phantom success) or reject an execution that satisfies the instruction (silent failure). In this paper, we int...
  </details>

- **2026-11-18** — Abderaouf Bahi, Hasan Masrur — [GridAnchor: Specialized Multi-Agent AI for Safeguarding Autonomous Energy Systems Against Cyber-Physical Hallucinations](http://arxiv.org/abs/2611.25158v1)
  <details><summary>📄 Abstract</summary>
  Autonomous energy systems increasingly chain specialized learned agents, such as a forecaster, a state estimator and a dispatcher that may be a language model. These agents can emit confident outputs that contradict physics, and downstream agents may act on them. We define such cyber-physical hallucinations and their cascades, organize them in eight types, and build CPH-Bench, a generator of labeled episodes on SimBench feeders. We propose GridAnchor, a verification layer whose Physics-Residual ...
  </details>

- **2026-11-18** — Yunye Gong, Indranil Sur, Jared Claypoole et al. — [Rate-distortion Assessment for Hierarchical Content Summarization](http://arxiv.org/abs/2611.25151v1)
  <details><summary>📄 Abstract</summary>
  Powerful generative models including large language and vision models have demonstrated success across a wide range of content generation, editing and manipulation tasks via end-to-end prompt-based generation. However, current assessment of the quality of generative content manipulation remains subjective, limiting scientific understanding of model capabilities. Inspired by rate-distortion theory from Shannon information compression theory, in this work we formalize hierarchical content summariz...
  </details>

- **2026-11-18** — Xianzhe Fan, Chi-Pin Huang, Fu-En Yang et al. — [MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation](http://arxiv.org/abs/2611.25105v1)
  <details><summary>📄 Abstract</summary>
  Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-ag...
  </details>

- **2026-11-18** — Pengyu Li, Zhitao Gao, Lingling Zhang et al. — [Do Thinking VLMs Need to Keep Looking at Long Videos? Write It Down, Then Look Away](http://arxiv.org/abs/2611.24259v2)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) reason about long videos over hundreds to thousands of tokens. Every decoding step re-reads the key-value (KV) cache of the entire video. Must the model keep looking while it reasons? In LookAway, the model first writes timestamped notes on what the question needs and then puts the video away. Once the notes close, the inference engine hides the video's KV cache for the rest of the response. Across both hybrid and pure-attention VLMs, dependence on the video is conc...
  </details>

- **2026-11-18** — Long Xu, Fuyi Wang, Xiaolu Hu et al. — [Evaluating LIM Trading Agents: A Critical Review of Backtesting Validity and Reporting Practices](http://arxiv.org/abs/2611.24133v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in investment research, and many studies report promising historical returns. However, such results are only credible if researchers can demonstrate that the model used only information available at the time, account for how strategies and configurations were selected, and explain how reported returns were generated. We identify six common threats to validity in LLM investment evaluations and apply them to 18 published studies. Across 108 assess...
  </details>

- **2026-11-18** — Jinhao Zhang, Yushen Zuo, Ke Rui et al. — [CoT-WAM: Collaborative Training of Vision-Language Models and World-Action Models via Plan Latents](http://arxiv.org/abs/2611.23803v2)
  <details><summary>📄 Abstract</summary>
  General robot manipulation requires both semantic competence and physical foresight. World action models (WAMs) acquire an understanding of and predictive capability over the physical world by jointly modeling visual foresight and action distributions. However, existing WAMs still lack semantic competence: they have limited ability to perform open-world scene understanding, semantic reasoning, and long-horizon planning. Although vision-language models (VLMs) provide these capabilities, effective...
  </details>

- **2026-11-18** — Tunazzina Islam — [When Objectives and Evaluators Disagree: Evaluating Transfer for Post-hoc Demographic Framing Mitigation](http://arxiv.org/abs/2611.25258v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc rewriting is used to reduce demographic disparities in LLM-generated text when the source model is inaccessible. A rewrite can look successful merely because it improved its own target or satisfied its selector. We study this as a transfer problem on 660 gender pairs and 1,980 age contrasts of demographic-conditioned climate messages. A rewriter proposes edits, a selection model chooses among constraint-satisfying candidates, and an independent evaluator uninvolved in either rates pairw...
  </details>

- **2026-11-18** — Ivan Kuznetsov, Dmitrii Pantiukhin, Sonja Hänzelmann et al. — [From FAIR to AWARE: Data Readiness for Agentic AI in the Earth Sciences](http://arxiv.org/abs/2611.25209v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence in the Earth sciences is beginning to act: prototype agents already search archives, run simulations and draft analyses. Scientific data were curated for researchers who bring expert judgement; an autonomous agent cannot be assumed to supply it. Data can satisfy the FAIR principles and still mislead a machine acting alone. We propose that Earth-science data become AWARE (Actionable, Well-described, Auditable, Recipe-equipped, Epistemically labelled), an agent-specific req...
  </details>

- **2026-11-18** — Arjun Choudhry, Aditya Narayanan, Raghav Mallampalli et al. — [A Verifier from the Past: Test-Time Compute for Time Series Foundation Models](http://arxiv.org/abs/2611.25171v1)
  <details><summary>📄 Abstract</summary>
  Test-time compute (TTC) improves language models by spending additional inference compute to generate, verify, and select among candidate outputs, but this recipe has not transferred directly to time series forecasting. A language model can verify a proof or vote across samples, but a forecaster must be causal; it cannot use future information to score a candidate. We propose Backtest-Gated Augmentation Averaging (BGAA), a TTC algorithm for time series forecasting that builds a causal verifier f...
  </details>

- **2026-11-18** — Simon Pettersson Fors, Eric Djäknegren, Jorge Fernández-Pendás et al. — [Modeling couplings and quench dynamics of hundred-qubit quantum processors](http://arxiv.org/abs/2611.25053v1)
  <details><summary>📄 Abstract</summary>
  Quantum processors now operate beyond the reach of exact classical simulation, yet their design and verification rest on precise models of the device. Understanding which properties of quantum processors can still be predicted on classical computers is central both to building these machines and to delimiting claims of quantum advantage. Here we address this question at the device level, using continuous unitary transformations to derive effective Hamiltonians non-perturbatively for two-dimensio...
  </details>

- **2026-11-18** — Dongwook Ghim, Juno Kwon, Rak-Kyeong Seong — [Quiver-Invariant Triality between Brane Brick Models](http://arxiv.org/abs/2611.25017v1)
  <details><summary>📄 Abstract</summary>
  We study quiver-invariant triality between 2d (0,2) supersymmetric gauge theories described by brane brick models associated with toric Calabi-Yau 4-folds. The dual theories share the same gauge groups, field content and E-terms but have distinct J-terms. We present an explicit pair of such brane brick models and identify the sequence of triality mutations relating them. This sequence returns the quiver to its original form while transforming the J- and E-terms. We explain the relation between q...
  </details>

- **2026-11-18** — Daiqing Wu, Junqiao Wang, Chengyang Fang et al. — [UEmo-D1: An Efficient and Calibrated Decision Model for Unified Multimodal Emotion Recognition](http://arxiv.org/abs/2611.24481v2)
  <details><summary>📄 Abstract</summary>
  Multimodal Emotion Recognition (MER) seeks to identify emotions conveyed through or elicited by media comprising diverse modality compositions. Research in this field has largely evolved along two paradigms: task-specific models and approaches based on Multimodal Large Language Models (MLLMs). Despite their distinct strengths, neither fully reconciles three capabilities essential to human-like emotion understanding: cross-task generalization, efficient decision-making, and receptiveness to multi...
  </details>

- **2026-11-18** — Hongyu Wang, Chuhan Li, Congjin Xu et al. — [EgoPass-Bench: Identifying Objects That May Affect the Wearer's Passage in Egocentric Video](http://arxiv.org/abs/2611.24995v1)
  <details><summary>📄 Abstract</summary>
  Understanding an egocentric environment requires reasoning about how surrounding entities affect the observer's actions. Existing evaluations of multimodal foundation models (MFMs) examine observer localization, motion trajectories, and action feasibility, but leave the discovery and interpretation of evolving observer-entity interactions insufficiently assessed. We introduce EgoPass-Bench, a benchmark for observer-relative interaction understanding in real-world egocentric video. EgoPass-Bench ...
  </details>

- **2026-11-18** — Ziyuan Wang, Genliang Zhu, Xiaobo Chen et al. — [Intent Contracts: Taking Tools Away from Agents](http://arxiv.org/abs/2611.24025v1)
  <details><summary>📄 Abstract</summary>
  Intent contracts are an authorization interface for tool-using LLM agents in which the planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields. Code validates the contract, and a small trusted model checks it against the user's words and writes the tool call itself. Provided the validation and dispatch code is correct, every executed call is written by the trusted model, the planner's influence on a call is confi...
  </details>

- **2026-11-18** — Lequn Fu, Yufeng Hu, Yijun Zhong et al. — [ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors](http://arxiv.org/abs/2611.23916v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots must recover from falls and resume commanded motion to sustain locomotion. Learning these behaviors in one policy requires supervision that accommodates both upright movement and ground-contact recovery. We present ReLoco, a framework that uses behavior-conditioned adversarial motion priors to learn locomotion, get-up from arbitrary fallen postures, and command resumption within one proprioceptive policy. During training, robot posture selects the expert pool and conditions a sha...
  </details>

- **2026-11-18** — Jiapeng Pei, Yuhang Yao, Sitan Liu et al. — [Safe Personal RSI: Evaluating and Repairing Personal-Agent Updates](http://arxiv.org/abs/2611.23651v1)
  <details><summary>📄 Abstract</summary>
  Kicker is a personal health assistant. Changes to an assistant's reusable instructions can improve task handling while changing what it discloses, which requests it follows, and how it reports actions. We study Safe Personal RSI, an update-evaluation component developed for Kicker. We restrict recursive self-improvement (RSI) to prompt updates, with model weights and runtime code fixed. The procedure tests proposed and current instructions, repeats failing cases, temporarily undoes changes to gu...
  </details>

- **2026-11-18** — Junjie Ye, Yiqi Zhao, Muchen Xu et al. — [$Z$-sight: Unifying Vision-Language-Action and Latent World Modeling](http://arxiv.org/abs/2611.24940v1)
  <details><summary>📄 Abstract</summary>
  We introduce $Z$-sight, a unified robot foundation model that couples vision-language-action (VLA) and generative latent world modeling. Video-based world action models (WAMs) show the value of joint future-and-action generation for control, yet inherit the heavy cost of video generators. Recent latent-space policies avoid pixel generation, yet typically align intermediate features or rely on frozen target encoders, decoupling future prediction from the VLM's native feature space. $Z$-sight inst...
  </details>

- **2026-11-18** — Jiahang Lin, Jiahao Chen, Yiding Wang et al. — [Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses](http://arxiv.org/abs/2611.24924v1)
  <details><summary>📄 Abstract</summary>
  Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the harness and benchmark scores to select changes. This process often produces narrow patches and leads to benchmark-specific local optima. We introduce Agentic Harness Engineering Beta (AHE-Beta), a requirement-centered lo...
  </details>

- **2026-11-18** — Favour Nerrise, Julian Busch, Gurpreet Singh Hora et al. — [Measuring and Improving Transfer of Neural Surrogates for Vehicle Aerodynamics](http://arxiv.org/abs/2611.24843v1)
  <details><summary>📄 Abstract</summary>
  Neural surrogates for external vehicle aerodynamics are fast alternatives to physics-based computational fluid dynamics (CFD) simulations. Their foundational limitation is a lack of zero-shot generalization across vehicle classes, which results in an expensive, custom training campaign for each new vehicle design. Similar to pretrained models in other fields, a pretrained surrogate should adapt to a new vehicle class using only a few simulations and stay accurate on its pretraining domain. No pr...
  </details>

- **2026-11-18** — Haoran Ye, Tianrui Huo, Hangzhen Li et al. — [A Foundation Model to Measure and Predict Human Behaviour](http://arxiv.org/abs/2611.24830v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to infer psychological attributes, predict individual behaviour, and simulate human populations. However, despite generating plausible responses, they often misrepresent individuals and distort population statistics. Here we introduce Chiron, a foundation model to measure and predict human behaviour. We jointly fine-tune an LLM to represent psychological constructs, predict individual behaviour, and align population response distributions with h...
  </details>

- **2026-11-18** — Xinyi Guo, Kaile Huang, Xitong Ling et al. — [Read Together, Answer Apart: How Earlier Questions Help Vision-Language Models Look](http://arxiv.org/abs/2611.24785v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are often asked several questions about the same image in a single prompt (co-asking), yet existing evaluations report conflicting accuracy gains and hallucinations at the prompt level without tracking how individual answers change. By pairing each question's single-question and co-asked answers across 22 open-weight VLMs (1B-35B), we find that erratic net shifts reflect two opposing effects: on Densely Captioned Images (DCI), every model repairs 15.4%-29.8% of its ...
  </details>

- **2026-11-18** — Houman Mehrafarin, Ioannis Konstas — [Chain-of-Thought Hidden States Reveal Task-Solving Directions for Direct Answers](http://arxiv.org/abs/2611.24598v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting improves the performance of Large Language Models by eliciting intermediate reasoning steps. However, CoT is far from perfect: on some tasks, models perform worse than with direct-answer prompting, and on others they generate a few hundred tokens to reach the correct answer. We start by labelling each CoT hidden state as recovering if patching it into the direct prompt yields the correct answer, and failed otherwise. A linear probe shows that the model encodes th...
  </details>

- **2026-11-18** — Chuang Wang, Rui Nie, Jie Song et al. — [StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model](http://arxiv.org/abs/2611.24408v1)
  <details><summary>📄 Abstract</summary>
  Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action to keep a stable effect. Existing benchmarks mostly evaluate these properties against references fitted to the video under test, either a scene reconstructed from its own frames or a camera trajectory aligned to the command path with a free scale. Such references can absorb gradual scene deformation and changes in pace ...
  </details>

- **2026-11-18** — Md Abtahi Majeed Chowdhury, Md Rifat Ur Rahman, Md Sakib Hossain Shovon et al. — [Target-Consistent Action Guidance via Semi-Unbalanced Optimal Transport for Drifting World Models](http://arxiv.org/abs/2611.24222v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned world models let robots imagine the outcomes of their actions for planning and offline policy evaluation, but these uses need many rollouts, which multi-step diffusion makes expensive. Drifting models move the iteration from inference to training and generate samples in one network pass. DriftWorld brought this paradigm to action-conditioned world models; to strengthen action following, it repels predictions from the current frame, a construction borrowed from classifier-free ...
  </details>

- **2026-11-18** — Xuerui Fang, Gulimila Kezierbieke, Chen Wangxing et al. — [TrajWAM: Trajectory-Conditioned Future Learning for Vision-Language Driving](http://arxiv.org/abs/2611.24192v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) connect future scene prediction with action planning for autonomous driving. Each driving record pairs an executed ego trajectory with its observed future, providing a factual outcome for learning this connection. We present TrajWAM, a trajectory-conditioned WAM that improves vision-language driving through auxiliary bird's-eye-view (BEV) future learning. An ego-trajectory query conditions DINOv3-aligned BEV predictions from shared planner representations. Training com...
  </details>

- **2026-11-18** — You Peng, Youhe Jiang, Chen Wang et al. — [eFAIR: Fair LLM Serving under Hourly Electricity Commitments](http://arxiv.org/abs/2611.24119v1)
  <details><summary>📄 Abstract</summary>
  Datacenters can procure electricity in day-ahead markets by committing to energy purchases for individual hours. For LLM services operating within these hourly budgets, maximizing aggregate throughput alone may still leave individual requests waiting or receiving much slower service than desired. Fair serving therefore requires improving service for poorly served requests while reserving electricity for later arrivals whose timing and demand are unknown. To compare service across requests, we de...
  </details>

- **2026-11-18** — Abbas Raza Ali, Muhammad Hamza Rehman, Xu Li et al. — [From Data to Valves: A Self-Learning, Production-Grade Edge Stack for Sustainable HVAC Control](http://arxiv.org/abs/2611.24052v1)
  <details><summary>📄 Abstract</summary>
  Learned HVAC controllers rarely leave the simulator, and those that do are typically trained offline, frozen at deployment and retrained from the cloud. We present a production stack in which three learning components run on one NVIDIA Jetson Orin gateway per building, adapt continuously from the building's own data, and verify their own effect. (a) A compact transformer-encoder forecaster, one per equipment group with learned per-unit embeddings, predicts every air-side unit's next-cycle temper...
  </details>

- **2026-11-18** — Zhengyuan Fan, Zhonghua Wu, Tianyu Cheng et al. — [How Reward Gain Imbalance Shapes Ranking: Rethinking Rubric-Based Reward Aggregation](http://arxiv.org/abs/2611.24005v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based reinforcement learning constructs rewards for aligning large language models with human preferences, typically by equally aggregating continuous scores that a judge assigns to individual criteria. However, scoring heterogeneity across criteria can distort candidate rankings. Existing work has focused on improving judges, learning criterion weights, or refining aggregation, whereas the interaction between scoring heterogeneity and ranking remains insufficiently understood. We formali...
  </details>

- **2026-11-18** — Wen Wang, Jindong Wang, Jiahua Bao et al. — [Evidence-Based Credit Assignment for Search-Augmented Language Models](http://arxiv.org/abs/2611.23824v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from terminal answer rewards enables search-augmented language models to interleave reasoning and retrieval without step-level annotations, yet outcome supervision assigns identical credit to every search in a trajectory regardless of whether it retrieved useful information. This limitation is especially severe when all sampled rollouts for a question fail, collapsing group-centered outcome advantages to zero even when trajectories gather markedly different evidence. We pr...
  </details>

- **2026-11-18** — Yeongtak Oh, Donghyeok Lee, Joonhee Oh et al. — [PReMind: When Personal Memory Meets Visual Hazards](http://arxiv.org/abs/2611.23808v1)
  <details><summary>📄 Abstract</summary>
  Personalized vision-language assistants use visual observations and personal memories to provide advice tailored to the user. When the observed scene contains a physical hazard, personal context, such as allergies, medical conditions, or mobility constraints, can change what help is appropriate. Responding appropriately therefore requires recognizing the visible hazard and applying the relevant person's information. We introduce PReMind-Bench, a diagnostic benchmark that evaluates this combinati...
  </details>

- **2026-11-18** — Haotian Wei, Can Long, Wen Xian Jim et al. — [Beyond Intelligibility: Fine-Grained Perceptual Assessment of Dysarthric Speech with Auditory Large Language Models](http://arxiv.org/abs/2611.23768v1)
  <details><summary>📄 Abstract</summary>
  Accurate assessment of dysarthric speech is vital for clinical diagnosis and rehabilitation, yet existing automated methods rely heavily on isolated, single-task models or generic speech quality metrics that fail to disentangle heterogeneous neuromotor deficits. This work presents the first systematic investigation into adapting auditory large language models (ALLMs) for multi-dimensional dysarthric speech assessment under a unified, prompt-conditioned framework. Four representative ALLMs are be...
  </details>

- **2026-11-18** — Ayman bin Kamruddin, Christopher Lam, Gaurav Patil et al. — [A Comparison of Heuristic, Human-Sensitive, and Self-Play DRL Policies in Human-Agent Teaming](http://arxiv.org/abs/2611.23747v1)
  <details><summary>📄 Abstract</summary>
  Dynamical Perceptual-Motor Primitives (DPMPs) offer a tractable framework for generating human-like movement dynamics in artificial agents (AAs) and have been used to support coordination in human-AI teaming tasks. Traditionally, DPMP controllers rely on heuristic (rule-based) decision policies derived from human behavior to guide goal selection and action sequencing. Although effective in structured tasks, such heuristics can be difficult to generalize to more complex settings, motivating inter...
  </details>

- **2026-11-18** — Shuichiro Ozawa, Izumi Takahara, Fumihiko Uesugi et al. — [Fast closed-loop STEM navigation using vision-language models with typed decisions](http://arxiv.org/abs/2611.23698v1)
  <details><summary>📄 Abstract</summary>
  Closed-loop scanning transmission electron microscopy (STEM), in which each acquired image determines the next field of view and magnification, offers a route to autonomous atomic-scale materials analysis. Such a loop would automate navigation to defects and grain boundaries, a task that has long relied on operator judgment, and would enable systematic analysis of diverse local structures at scale. Realizing it hinges on the decision step, which must translate each acquired image into the next o...
  </details>

- **2026-11-18** — Jennifer Zhang, Amanda Coston — [When Do LLMs Model the Right Target? Problem Formulation in High-Stakes Risk Prediction](http://arxiv.org/abs/2611.23638v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is increasingly used to assist with data science tasks, yet fundamental questions remain about its ability to correctly formulate analytical problems. We investigate how well large language models (LLMs) can formulate prediction problems when developing models for high-stakes decision making. We focus on one particular challenge to validity: decision dependency, which arises when historical decisions affect observed outcomes. We evaluate this aspect of problem formulation in LLM-ge...
  </details>

- **2026-11-18** — Akshay L Chandra, Iman Nematollahi, Lingyue Zhao et al. — [DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play](http://arxiv.org/abs/2611.24836v1)
  <details><summary>📄 Abstract</summary>
  Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. Humans can demonstrate skills in seconds, but their demonstrations lack the required robot actions. We introduce DiWALI, a framework that learns and improves diffusion policies within a world model trained on human and robot play. DiWALI infers latent actions from consecutive frames using an inverse dynamics model, enabling world model training without action labels, ...
  </details>

- **2026-11-18** — Phuong Tuan Dat, Qi Li, Xinchao Wang — [HINT-WAM: Hindsight-Informed Training for World Action Models](http://arxiv.org/abs/2611.24789v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have shown promising generalization and data efficiency in robot manipulation by coupling action generation with predictions of future visual dynamics. Translating these capabilities into reliable task execution, however, remains a challenge for existing post-training methods. Offline supervised fine-tuning provides dense supervision on expert trajectories, but its flow-matching action expert is trained only on noised demonstration actions and never on the intermediate...
  </details>

- **2026-11-18** — Pengyu Li, Zhitao Gao, Lingling Zhang et al. — [Do Thinking VLMs Need to Keep Looking at Long Videos? Write It Down, Then Look Away](http://arxiv.org/abs/2611.24259v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) reason about long videos over hundreds to thousands of tokens. Every decoding step re-reads the key-value (KV) cache of the entire video. Must the model keep looking while it reasons? In LookAway, the model first writes timestamped notes on what the question needs and then puts the video away. Once the notes close, the inference engine hides the video's KV cache for the rest of the response. Across both hybrid and pure-attention VLMs, dependence on the video is conc...
  </details>

- **2026-11-18** — Yoobin Shin, Jaeyoung Lee, Jieun Kang et al. — [TapTacTouch: Shape Completion from Sparse Tactile Contacts with Geometric Priors](http://arxiv.org/abs/2611.24207v1)
  <details><summary>📄 Abstract</summary>
  3D object reconstruction is essential for robotic perception and manipulation, yet conventional approaches predominantly rely on visual observations that can be limited by occlusion or unavailable in visually constrained environments. In this work, we propose a vision-free, training-free, and category-agnostic framework for reconstructing 3D object meshes from sparse tactile contacts without relying on pretrained shape models. A 6-DoF robotic arm equipped with a 20-DoF multi-finger robotic hand ...
  </details>

- **2026-11-18** — Long Xu, Fuyi Wang, Xiaolu Hu et al. — [Evaluating LIM Trading Agents: A Critical Review of Backtesting Validity and Reporting Practices](http://arxiv.org/abs/2611.24133v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in investment research, and many studies report promising historical returns. However, such results are only credible if researchers can demonstrate that the model used only information available at the time, account for how strategies and configurations were selected, and explain how reported returns were generated. We identify six common threats to validity in LLM investment evaluations and apply them to 18 published studies. Across 108 assess...
  </details>

- **2026-11-18** — Alperen Örsdemir, Rochelle Xenia Mendoza Santos, Wen Shei Ong et al. — [When Do Decision Models Help LLM-Driven Network Discovery?](http://arxiv.org/abs/2611.23947v1)
  <details><summary>📄 Abstract</summary>
  Network discovery, the identification of live hosts and their exposed services, is the first phase of every penetration test, and it is increasingly automated by harnesses driven by large language models (LLMs). To mitigate hallucinated or unsafe commands, recent work proposes inserting fast, non-generative decision models to validate actions prior to execution. This paper quantifies whether such validation improves discovery across three network scales (n = 10, 100, and 1,000) in a simulation c...
  </details>

- **2026-11-18** — Apoorva Vashisth, Manav Kulshrestha, Damon Conover et al. — [RePlan-VLA: Progress-Aware Replanning for Long-Horizon Vision-Language-Action Models](http://arxiv.org/abs/2611.23843v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, yet their performance often degrades on long-horizon tasks that require multiple interdependent manipulations. Instead of burdening the VLA policies with long-horizon reasoning, memory, action generation, progress tracking, and error recovery, we argue for leveraging their short-horizon manipulation capabilities within an execution-aware framework. To this end, we introduce \textnor...
  </details>

- **2026-11-18** — Jinhao Zhang, Yushen Zuo, Ke Rui et al. — [CoT-WAM: Collaborative Training of Vision-Language Models and World-Action Models via Plan Latents](http://arxiv.org/abs/2611.23803v1)
  <details><summary>📄 Abstract</summary>
  General robot manipulation requires both semantic competence and physical foresight. World action models (WAMs) acquire an understanding of and predictive capability over the physical world by jointly modeling visual foresight and action distributions. However, existing WAMs still lack semantic competence: they have limited ability to perform open-world scene understanding, semantic reasoning, and long-horizon planning. Although vision-language models (VLMs) provide these capabilities, effective...
  </details>

- **2026-11-18** — Zhiyu Liu, Xinyu Yang — [Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws](http://arxiv.org/abs/2611.24877v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are used to explain clinical prediction models, on the promise that they can say what a model computes, find its faults and even reveal new knowledge in it. We tested the three promises where the answers could be checked. From the International Stroke Trial we trained four kinds of model (logistic regression, explainable boosting machine, gradient-boosted trees, neural network) for two outcomes on patients randomised earlier, planted one flaw in each of 24 copies (an...
  </details>

- **2026-11-18** — Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole et al. — [Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling](http://arxiv.org/abs/2611.24849v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scala...
  </details>

- **2026-11-18** — Emad Aghajanzadeh, Bethany Anne Wong, Leonhard Kunze et al. — [DRIFT: Detachable Reasoning for Runtime-Flexible and Efficient End-to-End Driving](http://arxiv.org/abs/2611.24719v1)
  <details><summary>📄 Abstract</summary>
  The integration of vision-language models (VLMs) into end-to-end (E2E) autonomous driving has demonstrated strong potential by providing scene description and reasoning capabilities. However, VLMs are computationally expensive, and switching language reasoning on and off at runtime without hurting closed-loop performance has not been demonstrated, which hinders practical adoption. To address these issues, we propose DRIFT, an E2E autonomous driving framework that integrates a lightweight languag...
  </details>

- **2026-11-18** — Kamil Szczech, Maksymilian Wojnar, Krzysztof Rusek et al. — [Can Bandits Learn to Share a Channel? Distributed Multi-Armed Bandits for Slotted ALOHA](http://arxiv.org/abs/2611.24676v1)
  <details><summary>📄 Abstract</summary>
  Slotted ALOHA networks constitute a playground for research on machine learning (ML)-based channel access schemes. We consider ML agents deployed in such networks and operating under severe constraints: fully distributed (independent operation), fully online (no pre-training), aperiodic (no fixed schedule), and with no explicit coordination (no signaling). We ask whether a multi-armed bandit (MAB), a minimal reinforcement learning agent, can learn the optimal policy for a capture-free slotted AL...
  </details>

- **2026-11-18** — Valerio Taralli, Andrea Tosin — [Modelling population distribution across cities on spatial networks using the kinetic theory of multi-agent systems](http://arxiv.org/abs/2611.24657v1)
  <details><summary>📄 Abstract</summary>
  We investigate the urban population distribution of the Italian region of Sardinia through the kinetic theory of multi-agent systems on spatial networks, interpreting cities both as agents and vertices of a graph, and representing interurban links as edges. We consider various emigration rules to model the interactions between agents, obtaining two main results: the bimodal lognormal fit of the total population distribution among cities and the Pareto fit of the tail. Overall, our model provides...
  </details>

- **2026-11-18** — Robert Debbas, Éric Goubault, Sylvie Putot — [Zonotopic Analysis of Quantization Error in Neural Networks](http://arxiv.org/abs/2611.24648v1)
  <details><summary>📄 Abstract</summary>
  Quantized neural networks achieve computational efficiency by reducing precision, but bounding their quantization error remains a challenge due to discrete rounding and clamping operations. We present a zonotope-based abstract interpretation framework for quantized ReLU feed-forward network verification, introducing a unified round-clamp abstract transformer that jointly handles both operations. We extend this framework to constrained zonotopes, which add linear constraints to tighten bounds, an...
  </details>

- **2026-11-18** — Maria Cristina Aspromonte, Alexander M. Monzon, Miguel A. Andrade-Navarro et al. — [Biases and Limits of AlphaFold Predictions for Non-Globular Proteins](http://arxiv.org/abs/2611.24546v1)
  <details><summary>📄 Abstract</summary>
  AlphaFold has transformed protein structure prediction, making structural models accessible across the life sciences. We explore experimentally validated cases of non-globular proteins to uncover where predictions diverge from biologically relevant structural states and how molecular context shapes these discrepancies, guiding a more informed interpretation of AlphaFold models.
  </details>

- **2026-11-18** — Daiqing Wu, Junqiao Wang, Chengyang Fang et al. — [UEmo-D1: An Efficient and Calibrated Decision Model for Unified Multimodal Emotion Recognition](http://arxiv.org/abs/2611.24481v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Emotion Recognition (MER) seeks to identify emotions conveyed through or elicited by media comprising diverse modality compositions. Research in this field has largely evolved along two paradigms: task-specific models and approaches based on Multimodal Large Language Models (MLLMs). Despite their distinct strengths, neither fully reconciles three capabilities essential to human-like emotion understanding: cross-task generalization, efficient decision-making, and receptiveness to multi...
  </details>

- **2026-11-18** — Edoardo Chidichimo, Felix P. S. Wallis — [Nothing to Declare: Steering a single neuron increases concealment in AI teams](http://arxiv.org/abs/2611.24475v1)
  <details><summary>📄 Abstract</summary>
  Recent research suggests that individual neurons can have interpretable roles in AI behaviour. In Qwen3.5-4B, steering along one neuron's output direction increased decisions to conceal information more in teams than alone across five scenarios, even when teammates provided no messages. When all members participated and received steering, collective concealment increased in four scenarios, while inter-agent messaging helped temper concealment under steering. Moreover, removing the neuron's contr...
  </details>

- **2026-11-18** — Yang Ji, Ying Sun, Yuanxin Zhuang et al. — [Retroactive Concept Bottleneck Models for Exemplar-Free Class-Incremental Learning](http://arxiv.org/abs/2611.24445v1)
  <details><summary>📄 Abstract</summary>
  Exemplar-free class-incremental learning (EFCIL) requires models to learn new classes sequentially without retaining training samples from previous tasks. Continual concept bottleneck models (CBMs) make their predictions interpretable by identifying visual concepts in an image and using them to score each class. However, these methods typically focus on preserving learned concepts or approximating past classes with generated features, which can leave new concepts underused in old-class predictio...
  </details>

- **2026-11-18** — Deepro Das, Saad Kabir Uddin, Mohammad Alauddin et al. — [Explainable and CPU-Efficient Brain Tumor Classification from MRI Using Two-Phase EfficientNetB3 Fine-Tuning](http://arxiv.org/abs/2611.24440v1)
  <details><summary>📄 Abstract</summary>
  Brain tumors are among the most lethal neurological disorders, with over 308,000 new diagnoses annually worldwide. Accurate classification of tumor type from Magnetic Resonance Imaging (MRI) scans is critical for treatment planning; however, manual radiological interpretation is time-consuming and prone to inter-observer variability. This paper proposes an automated deep learning pipeline for four-class brain MRI classification (glioma, meningioma, no tumor, and pituitary tumor) using EfficientN...
  </details>

- **2026-11-18** — Baichuan Yang, Dongyuan Xu, Zhao Yang et al. — [MLIE-CoT: Chain-of-Thought Reasoning via Multi-Level Image Editing](http://arxiv.org/abs/2611.24433v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) reasoning has proven effective in improving the reasoning abilities of large language models by breaking complex tasks into step-by-step solutions. In recent years, researchers have attempted to extend CoT reasoning to visual generative models to improve their ability to handle complex tasks. However, existing CoT methods for text-to-image generation still rely mainly on textual reasoning and therefore cannot fully use and preserve the correct semantic information already ...
  </details>

- **2026-11-18** — Dongjun Han, Mingyu Lee, Ikjin Lee — [LLM-Assisted Multi-Fidelity Bayesian Optimization: Fusing Expert Knowledge with Numerical Data](http://arxiv.org/abs/2611.24377v1)
  <details><summary>📄 Abstract</summary>
  Multi-fidelity Bayesian optimization (MFBO) reduces engineering design cost by combining inexpensive low-fidelity (LF) models with a few accurate high-fidelity (HF) evaluations and sequentially selecting designs to evaluate. However, when HF data are scarce, the LF-HF discrepancy is difficult to learn from numerical data alone, especially when physics omitted in the LF model makes it design-dependent. Yet even without sufficient data, domain experts often know which physics the LF model omits an...
  </details>

- **2026-11-18** — Guolong Zheng, Chen Hou, Xu Yang et al. — [Semantic Context Handoff with On-Demand Evidence for Long-Horizon Agents](http://arxiv.org/abs/2611.24357v1)
  <details><summary>📄 Abstract</summary>
  Traditional long-horizon LLM agents often hand off context through full-history prompting, retaining all previous action--observation interactions. As execution proceeds, this history keeps growing, increasing inference cost and potentially degrading accuracy. Existing methods control this growth by preserving compact conclusions while removing earlier observations, but doing so can discard evidence that later becomes relevant. We introduce Semantic Context Handoff (SCH), whose central abstracti...
  </details>

- **2026-11-18** — Karim Achouri, Youssef Dib, Hossein Allahverdizadeh et al. — [Bound States in the Continuum as Converging Scattering Zeros in Metasurfaces: Why Accidental BICs Require Nonlocality](http://arxiv.org/abs/2611.24326v1)
  <details><summary>📄 Abstract</summary>
  Bound states in the continuum (BICs) allow metasurfaces to achieve extremely high quality factors, yet it remains unclear how they emerge and how they can be described by effective material parameters. We address this question by modeling BICs through the reflection and transmission zeros of a metasurface described by effective susceptibilities. By decomposing its response into even and odd parts, and inspecting the interaction of the corresponding poles and zeros, we show that a high-Q resonanc...
  </details>

- **2026-11-18** — Warut Suksompong — [On the Complexity of Envy Cycle Elimination](http://arxiv.org/abs/2611.24167v1)
  <details><summary>📄 Abstract</summary>
  The envy cycle elimination (ECE) algorithm is a fundamental algorithm for the fair allocation of indivisible goods, guaranteeing an allocation that is envy-free up to one good under arbitrary monotone utilities. We show that the ECE algorithm can be implemented in $O(nm)$ time for $n$ agents and $m$ goods, and establish the tightness of this bound.
  </details>

- **2026-11-18** — Xiaoqian Shen, Yunyang Xiong, Changsheng Zhao et al. — [AVTR: Adaptive Multimodal Reasoning with Visual Imagination](http://arxiv.org/abs/2611.24161v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models increasingly rely on textual reasoning to solve advanced multimodal tasks. Despite its effectiveness, this paradigm faces two fundamental limitations. First, relying on textual reasoning alone can limit perceptual ability in vision-centric questions, where accurate answers depend on interpreting task-relevant visual evidence. Second, applying textual reasoning uniformly across inputs overlooks question-dependent variation in both reasoning modality and depth, often produci...
  </details>

- **2026-11-18** — Ernesto Biempica, Emiliano Bruner, Juan F Poyatos — [Human-LLM Cognitive Extension: A Framework for Studying Coupled Cognition](http://arxiv.org/abs/2611.24149v1)
  <details><summary>📄 Abstract</summary>
  Recent research on the use of Large Language Models (LLMs) reports divergent cognitive outcomes, including improved assisted performance, limited transfer, and compromised unaided learning. Here, we argue that part of this seeming inconsistency arises because studies often assess different cognitive systems without making the unit of analysis explicit. Building on work in extended and distributed cognition, we propose the Human-LLM Cognitive Extension (HLCE) as a methodological framework for mat...
  </details>

- **2026-11-18** — Lei Ying — [Second-Order Steady-State Approximation of Heterogeneous Mean-Field Models](http://arxiv.org/abs/2611.24123v1)
  <details><summary>📄 Abstract</summary>
  Mean-field models provide tractable approximations for large stochastic systems, but second-order steady-state results are largely limited to homogeneous or fixed-dimensional population processes. This paper develops a second-order steady-state approximation for fully heterogeneous mean-field models. Conditioning on the realized agent parameters, we study fixed-dimensional weighted occupancies even though the dimension of the full heterogeneous mean-field system grows linearly with the number of...
  </details>

- **2026-11-18** — Luca Lusvarghi, Javier Gozalvez — [Attention Is Not Relevance: Challenging the Causality of Attention in Autonomous Driving](http://arxiv.org/abs/2611.24051v1)
  <details><summary>📄 Abstract</summary>
  Attention has become one of the most widely adopted solutions for estimating the relevance of surrounding objects and interpreting an autonomous vehicle's driving decisions. However, its ability to capture the causal impact of individual input elements on an AI model's output has long been discussed in the literature, particularly in the Natural Language Processing (NLP) domain. This work brings this discussion into the autonomous driving domain by analyzing the accuracy of attention in estimati...
  </details>

- **2026-11-18** — Yilin Wang, Xin Yu, Xinyi Guo et al. — [ReSynth: Constructing Synthetic Supervision for Multi-Image Understanding](http://arxiv.org/abs/2611.23996v1)
  <details><summary>📄 Abstract</summary>
  People often understand the world by comparing different views of it. Vision-language models (VLMs), however, receive these views as separate images and still struggle to relate them. One problem is data. Training on these tasks requires groups of images with a known relationship: the same object from different viewpoints, or the same scene before and after a change. Such examples are hard to collect at scale from existing photo collections. We introduce ReSynth, which turns single-image percept...
  </details>

- **2026-11-18** — Nan Hou, Kangfei Zhao, Jiadong Xie et al. — [Cascadeability and the Realization Gap: An Empirical Study of LLM-Powered Semantic Filtering](http://arxiv.org/abs/2611.23898v1)
  <details><summary>📄 Abstract</summary>
  Semantic filters enable natural language predicates over unstructured documents, but evaluating every document with a large language model (LLM) oracle is expensive. Proxy cascades reduce oracle invocations using cheaper surrogates, but oracle reduction alone cannot distinguish proxy limitations from calibration bottlenecks and establish practical efficiency. We present a unified benchmark of four representative systems, which formulate query processing as a three-stage workflow comprising proxy...
  </details>

- **2026-11-18** — Ilker Oguz, Colin Christian, Christophe Moser et al. — [In Situ Training of Optical Neural Networks by Coding Agents](http://arxiv.org/abs/2611.23875v1)
  <details><summary>📄 Abstract</summary>
  Optical neural networks promise fast, energy-efficient computing, but every device departs from its design and must be trained with the hardware. In situ training relies on an expert-built calibrated digital model of each device or on gradient-free trial and error. Coding agents, large language models that write and run programs, have shown an emergent ability to understand and edit the weights of digital neural networks. Here we introduce optics as code, a method in which a coding agent trains ...
  </details>

- **2026-11-18** — Haiming Zhu, Zhiwei Chen, Ding Cao et al. — [Keep the Image in Mind: A Visual Board for Multimodal Agents](http://arxiv.org/abs/2611.23872v1)
  <details><summary>📄 Abstract</summary>
  Multi-step visual reasoning suffers when early visual misinterpretations persist as incorrect premises in subsequent reasoning. We argue that how visual evidence is represented during reasoning matters as much as how much of it is gathered. Rather than appending observations and inferences to an ever-growing dialogue, we introduce a Visual Board-centered harness that separates visual observations, uncertain interpretations, and derived reasoning within a structured, capacity-bounded, and revisab...
  </details>

- **2026-11-18** — Hangle Hu, Chenyu Hou, Bin Cao et al. — [Asking but Missing: Decision Coverage in Natural-Language Data Querying](http://arxiv.org/abs/2611.23864v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to translate natural language questions about structured data into executable programs. A fundamental challenge is recognizing when a question admits multiple computational interpretations and identifying the decisions needed to resolve them. We investigate whether language models recognize these unresolved decisions before generating code, or silently adopt assumptions that may lead to incorrect results. We refer to the latter behavior as Underspecifi...
  </details>

- **2026-11-18** — Bin Yin — [Online State-Representation Adaptation under Synthetic Interaction-Cue Remapping](http://arxiv.org/abs/2611.23836v1)
  <details><summary>📄 Abstract</summary>
  When cues change what they predict, continuing to update a learned mapping may help an agent choose the appropriate action. We tested this in a one-step synthetic task by comparing a logistic state predictor that continued to learn from state labels with the same predictor frozen at transfer. We evaluated ten conditions in six held-out environments, with 1,296 paired runs per condition and 1,296,000 transfer records in total. Late action accuracy was 93.39% with online updates and 64.63% with fr...
  </details>

- **2026-11-18** — Katsutoshi Yoshida — [Euler-Lagrange Equations Formulated in Terms of Angular Velocity](http://arxiv.org/abs/2611.23828v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel variant of the Euler--Lagrange (EL) equation for rigid body rotation, explicitly formulated in terms of orientation parameters $\thh$ and angular velocity $\omm$.   Variational analysis of the stationarity condition of the action integral for a Lagrangian in terms of $\thh$ and $\omm$ yields a modified EL formulation.   For pure rotational motion, the proposed equation directly recovers equations of motion fully consistent with the classical Euler equations, bypassing explicit...
  </details>

- **2026-11-18** — Tianqi Chen — [Temporal Fair Division: Simultaneous Guarantees for Goods and Chores](http://arxiv.org/abs/2611.23782v1)
  <details><summary>📄 Abstract</summary>
  We study temporal fair division of indivisible items in both the goods and chores settings, with $n \ge 2$ agents and nonnegative additive values or costs. Items arrive one at a time and must be assigned immediately and irrevocably. The arrival order and all agents' values or costs are known in advance, and the cumulative allocation must satisfy the fairness requirements after each arrival. For goods, we give a polynomial-time algorithm that simultaneously achieves exact temporal proportionality...
  </details>

- **2026-11-18** — Yao Chen, Jiagang Ren, Hua Zhang — [Geiss-Besov Regularity of Exit Times of Diffusion Processes](http://arxiv.org/abs/2611.23763v1)
  <details><summary>📄 Abstract</summary>
  We prove that the truncated exit times of possibly degenerate diffusion processes from open domains satisfying the exterior sphere condition belong to the Geiss-Besov space $\mathbb{B}_p^{\frac{1}{2p}}$. In the one-dimensional case, the same result is proven using Zvonkin transformation for untruncated exit times if the diffusion is uniformly elliptic.
  </details>

- **2026-11-18** — Abdiaziz Muse, Jiju Poovvancheri — [Do 3D Point Representations Encode Architectural Functions? Probing Supervised and Pretrained Models on Urban Facades](http://arxiv.org/abs/2611.23720v1)
  <details><summary>📄 Abstract</summary>
  Semantic labels say what a building element is, not what it does: two identical-looking windows on one facade may be operable or fixed, a column may carry load or only decorate. We ask whether 3D point representations encode such architectural function. On 22 mobile-LiDAR buildings with 15 functional attributes per element, we hold out entire buildings and compare hand-crafted descriptors, networks trained from scratch and frozen self-supervised point transformers. Descriptors and frozen feature...
  </details>

- **2026-11-18** — Shenghan Gao, Zhiling Zheng — [Structured Extraction of Diffraction Data from Covalent Organic Frameworks](http://arxiv.org/abs/2611.23680v1)
  <details><summary>📄 Abstract</summary>
  Powder X-ray diffraction (PXRD) is the primary structural evidence for covalent organic frameworks (COFs) and many other materials. Yet decades of measured patterns exist only as images in published figures. Automatic recovery is difficult, because PXRD figures vary widely in format, from a single curve to crowded stacks with labels, insets, and neighboring plots that challenge traditional computer vision. This work presents a pipeline in which a vision large language model (LLM) interprets the ...
  </details>

- **2026-11-18** — Erzheng Zhang, Agnes Chu — [Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits](http://arxiv.org/abs/2611.23657v1)
  <details><summary>📄 Abstract</summary>
  Fairness audits treat a trained model as a fixed decision function, but the arithmetic that evaluates it is part of that function. This study holds the model, records, threshold and audit code fixed and varies the numerical execution contract in two tiers. Tier 1 changes only how products and sums are computed, with the serialized weights byte-identical, and is the causal test of arithmetic. Tier 2 runs reduced-precision deployment configurations (BF16 compute, FP8 and 8-bit weights), which can ...
  </details>

- **2026-11-17** — Hsi Chang, Irfan Khan — [Trace2ST: Recovering PLC Structured Text from I/O Traces with LLM Generation and Verification](http://arxiv.org/abs/2611.24979v1)
  <details><summary>📄 Abstract</summary>
  Programmable logic controllers (PLCs), the industrial computers that operate power and process plants, often run programs whose source code is no longer available; however, every input and output of the controller is logged continuously. This paper therefore asks whether a large language model (LLM) can recover an executable program in Structured Text (ST), the standard PLC language of IEC 61131-3, from such input/output records (traces) alone and, equally important, how the recovered program ca...
  </details>

- **2026-11-17** — Prashank Kadam — [Option-GRPO: Hierarchical RL Against AI Slop in Code Generation for Unseen SDKs](http://arxiv.org/abs/2611.23633v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly produce AI slop in generated code: verbose, redundant, non-idiomatic implementations that pass functional checks but bloat codebases. The problem compounds on SDKs released after the model's training cutoff, where the model has neither idiomatic priors nor compositional understanding. We present Option-GRPO, a hierarchical reinforcement learning framework that adapts a code LLM to an unseen SDK from its source code alone, without human-written usage examples or...
  </details>

- **2026-11-17** — Adhyayan Veer Singh, Fanjiang Ye, Yuke Wang — [RefinementGuard: Counterexample-Directed Semantic Qualification for Hidden Agent-Tool Execution](http://arxiv.org/abs/2611.23611v1)
  <details><summary>📄 Abstract</summary>
  Tool runtimes can lower an agent-selected operation into a hidden parallel graph, reducing latency and context while risking semantic mistranslation. We introduce RefinementGuard: translation validation for hidden, effectful agent-tool lowerings, coupled to artifact-bound, fail-closed runtime admission. Qualification compares a candidate graph with an independent reference on isolated state using explicit parent-operation obligations. We evaluate two repository-level contracts, bug localization ...
  </details>

- **2026-11-17** — Xinyang Li, Chih-Hsuan Yang, Xiaolong Ma et al. — [Safe to Omit, Worth Omitting? Keeping the Answer and Cutting Latency When an LLM Agent Skips Another's Message](http://arxiv.org/abs/2611.23570v1)
  <details><summary>📄 Abstract</summary>
  In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency. We study when a receiver agent can skip the message safely (the final answer rarely changes) and beneficially (the time saved exceeds the cost of deciding). Our mechanism reads the receiver agent's confidence without the message and uses a finite-sample test to certify a threshold at which, with high probability, at most 5% of skipped an...
  </details>

- **2026-11-17** — Hui Zhu, Saleh Zare Zade, Rafi Ibn Sultan et al. — [Beyond the Sink Token: Sink-Guided Key Editing in Vision-Language Models](http://arxiv.org/abs/2611.23516v1)
  <details><summary>📄 Abstract</summary>
  In vision-language models (VLMs), a few sink tokens attract a disproportionate share of attention. While previous studies have examined why these tokens attract attention, we investigate how the sink-key direction affects attention to image and question tokens. Across four probed VLMs, boosting the magnitude of positive sink-aligned components increases attention on average, whereas boosting negative components decreases it; these responses persist through later layers. This identifies the nativ...
  </details>

- **2026-11-17** — Amber He Wei, Shiyu Cheng, Andrew Clark et al. — [Verifiably Safe Decentralized Control via Event-Triggered Topology Switching](http://arxiv.org/abs/2611.23415v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a decentralized event-triggered topology-switching protocol for multi-agent systems under estimation uncertainty. We consider an intermittent communication setting in which each agent switches between connected and disconnected modes and makes communication decisions using locally computable certificates, while the closed-loop state is required to remain safe. The proposed protocol follows a safety-driven triggering principle in which agents reconnect before their certificate...
  </details>

- **2026-11-17** — Jiarui Cui, Boxun Yan — [RFBench: A Simulator-Grounded Multimodal Benchmark for Passive RF Layout Design and Understanding](http://arxiv.org/abs/2611.23410v1)
  <details><summary>📄 Abstract</summary>
  While multimodal language models can interpret diagrams and generate structured outputs, their capacity to connect passive radio-frequency (RF) design intent, layout geometry, and electromagnetic behavior remains largely untested. To address this gap, we introduce RFBench, a simulator-grounded dataset and benchmark for passive RF layout design and understanding. The dataset contains 10,000 two-port planar layouts simulated using ADS Momentum, with each layout represented by editable geometric pr...
  </details>

- **2026-11-17** — Yifan Chang, Jian Yang, Jiangnan Shao et al. — [MAVE: Reconstructing Editable 3D Blockouts from Film Shots](http://arxiv.org/abs/2611.22464v2)
  <details><summary>📄 Abstract</summary>
  Animated 3D blockouts support previsualization and provide structural conditions for video generation, but manually reconstructing them from reference videos is costly. This limits both their use by creators and the production of paired training data. We introduce MAVEBench, a benchmark of 50 film shots and 416 keyframes for evaluating camera motion, spatial layout, and character blocking. We propose MAVE, a video-to-blockout framework combining Metric observation, Agentic modeling, and evidence...
  </details>

- **2026-11-17** — Sara Amar — [MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain](http://arxiv.org/abs/2611.23613v1)
  <details><summary>📄 Abstract</summary>
  We introduce MANGO Arena, an open-source testbed in which four LLM agents each run one company in a serial supply chain adapted from MANGO, a classroom factory-management game. The environment enforces hard rules (a truck limit, a no-credit cash constraint and production capacity), logs every blocked attempt to break them, and gives agents a public message board on which side payments are explicitly forbidden. This lets one environment measure three things at once: an economic outcome (the bullw...
  </details>

- **2026-11-17** — Sehyeon Lee, Yuchen Xia, Zhaoyang Hong et al. — [Towards Fair Resource Sharing in Agentic LLM Serving](http://arxiv.org/abs/2611.23558v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly execute complex, multi-step tasks on shared inference infrastructure, resource contention across the end-to-end LLM serving stack causes severe and uneven slowdowns across agents. Existing agentic serving systems primarily optimize throughput and latency, with comparatively limited attention to fairness among concurrent agents. Although fairness has been studied in conventional LLM serving at the token and request levels, these approaches do not fully capture cumulativ...
  </details>

- **2026-11-17** — Jinjun Peng, Wailiang Zhao, Baishakhi Ray et al. — [Stability Does Not Mirror Plasticity: A Module-Level View of Declarative and Procedural Learning in Transformers](http://arxiv.org/abs/2611.23427v1)
  <details><summary>📄 Abstract</summary>
  Plasticity and stability in continual learning are typically studied at the entire-model level and in a task-agnostic manner, yet prior work has reported divergent conclusions across settings. Inspired by cognitive distinctions between declarative and procedural memory, we instead study how plasticity and stability vary across transformer modules and task types. In a controlled synthetic environment with clean measurement, we show a double dissociation: query-key (QK) and value-output (VO) proje...
  </details>

- **2026-11-17** — Amadeus Brandes — [Record Sufficiency: What a Decision Record Must Preserve When an Unsettled Claim Becomes an Operative Status](http://arxiv.org/abs/2611.23422v1)
  <details><summary>📄 Abstract</summary>
  Organisations keep evidence, logs and approvals, but often not the step by which an unsettled claim became an operative status, such as an accepted label or a released image, so later readers cannot tell what the status was allowed to mean. We call a decision record sufficient if it is true and a reader who has only the record and the items it cites can explain the status, bound it, re-derive it and challenge it. From these four uses we argue for ten questions a record must answer, map them onto...
  </details>

- **2026-11-17** — Chaipat Tirapongprasert, Rajarshi Das, Parijat Dube — [Tracking Representations in LLM Reasoning Traces for Iterated Games](http://arxiv.org/abs/2611.23403v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model's actual computation. We address this by investigating how LLM agents make decisions in iterative games with incomplete information. Using a series of mechanistic interpretability techniques, we find that the model forms and iteratively revises an inter...
  </details>

- **2026-11-17** — Hubert Strauss, Liam Fowl, Noam Razin — [Which Tokens, in What Order, and How Fast? A Theoretical Analysis of On-Policy Distillation Objectives](http://arxiv.org/abs/2611.23397v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student language model to match a teacher model based on its own generations. When using OPD, one must choose whether to apply it at the sequence or token level and which divergence to minimize. However, despite the wide adoption of OPD in practice, the formal understanding of which OPD objective is appropriate for a given setting is limited. Toward addressing this gap, we theoretically analyze how the choice of OPD objective governs which tokens are priorit...
  </details>

- **2026-11-17** — Samuel Sisk, Xiaosong Du — [A Neural Envelope Method for Rapid Gradient-based Optimum Takeoff Trajectory Design](http://arxiv.org/abs/2611.23130v1)
  <details><summary>📄 Abstract</summary>
  Urban air mobility arises to mitigate ground traffic congestion. Multidisciplinary analysis and optimization (MDAO) has been introduced to reduce the energy consumption, thereby expanding aircraft performance. Surrogate-based MDAO lowers the cost of optimization, but multimodality disrupts global optimum search for both simulation-based and surrogate-based optimizations. Convex envelopes convert multimodal spaces into unimodal spaces, permitting efficient convex optimization; however, convexifyi...
  </details>

- **2026-11-17** — Yash Khare, Hunjun Shin, Mohit Singhal — [Longitudinal Multi-Dimensional Analysis of India-Pakistan Conflict Discourse on Reddit (2019-2025)](http://arxiv.org/abs/2611.22987v1)
  <details><summary>📄 Abstract</summary>
  Six India--Pakistan crises between 2019 and 2025, from the Pulwama attack to Operation Sindoor, have each been argued out on Reddit in India-aligned communities such as \texttt{r/india}, in Pakistan-aligned communities such as \texttt{r/pakistan}, and in general-audience ones such as \texttt{r/worldnews}. A strike can be a security issue in one community and a question of who was harmed in another. Computational studies of the conflict have concentrated on the February 2019 crisis, with some spl...
  </details>

- **2026-11-17** — Shaozhen Liu, Zhiwei Li, Jiayang Sun et al. — [RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models](http://arxiv.org/abs/2611.22736v1)
  <details><summary>📄 Abstract</summary>
  Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retraining when manipulation objects change. We introduce RefCloth, a framework that optimizes one persistent adversarial tablecloth on a frozen source policy and deploys it zero-shot across unseen tasks and target models without modifying task objects or cameras. Throughout manipulation, ...
  </details>

- **2026-11-17** — Jingyu Liu, Zongze Li, Zach Xu et al. — [RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](http://arxiv.org/abs/2611.22179v1)
  <details><summary>📄 Abstract</summary>
  Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a deliberately minimal RAG memory with chained observation notes, hybrid BM25 with cosine retrieval, and chronological rendering, which reaches parity within bootstrap CI with the prior SOTA on LongMemEval-S and BEAM, and beats th...
  </details>

- **2026-11-17** — Yixin Chen, Jianfeng Lin, Shizhao Wang — [A Butterfly-Inspired Agent Learns to Climb with Self-Generated Wingbeats](http://arxiv.org/abs/2611.22139v1)
  <details><summary>📄 Abstract</summary>
  Butterfly free climbing involves dynamic coupling between wing motion and unsteady aerodynamic forces that drive the animal's ascent. Four-wing coordination determines how these forces combine to support weight and direct propulsion. How aerodynamic feedback shapes such coordination remains difficult to establish when wing kinematics are prescribed in experiments and simulations. Here, we construct a virtual flight environment with rapid aerodynamic feedback and train a butterfly-inspired agent ...
  </details>

- **2026-11-17** — Shobhita Sundaram, Cansu Sancaktar, Phillip Isola — [Do LLM Agents Still Need to Be Told How to Self-Improve?](http://arxiv.org/abs/2611.23219v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for contex...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 726 |
| prompt-injection | 695 |
| memory-poisoning | 59 |
| tool-use-attack | 178 |
| backdoor | 563 |
| adversarial-attack | 678 |
| privacy-leakage | 4647 |
| steganography | 93 |
| misuse | 1345 |
| red-teaming | 157 |
| vulnerability | 4109 |
| defense | 4030 |
| alignment | 3781 |
| robustness | 4139 |
| watermark | 783 |
| unlearning | 124 |
| agent-safety | 67 |
| benchmark | 76 |
| survey | 464 |
| other | 11398 |

---

📚 **全部 38112 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-22 04:55:18*