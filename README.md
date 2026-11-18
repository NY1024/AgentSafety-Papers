<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-37434-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-18 00:24 ｜ **论文总数 / Total Papers**: 37434（近 30 天 / Recent 30 days: 4069）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 37434 篇论文（含摘要、分类筛选、搜索）/ View all 37434 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 721
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 687
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 59
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 175
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 560
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 674
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4608
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 93
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1322
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 154
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 4038
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3949
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3709
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 4054
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 766
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 122
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 75
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 461
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 11140

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4069 篇，完整 37434 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4069 papers from the last 30 days (with date, authors & abstract). For the full list of 37434 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 3 papers

- **2026-11-13** — Wenzhuo Xu, Zonghao Ying, Deyue Zhang et al. — [LLMs are Vulnerable to Malicious Requests with Indistinguishable Intent](http://arxiv.org/abs/2611.17818v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak attacks can circumvent the safety mechanisms of Large Language Models (LLMs) and lead to the generation of harmful or policy-violating content. We first examine eight jailbreak methods against an LLM-based filter and observe that requests resembling normal user queries tend to have higher filter pass rates than those containing obvious anomalous patterns. This observation motivates the hypothesis that resemblance to normal requests may contribute to jailbreak success. We introduce \tex...
  </details>

- **2026-11-13** — Richard J. Young — [Is Abliteration Getting Harder? Not Uniformly: Refusal Removal by Direction-Based Ablation and ARA in Heretic on the Qwen3.8, Gemma 4, Olmo 3.1 and Mistral Small 3.2 LLMs Versus Their Predecessors](http://arxiv.org/abs/2611.17846v1)
  <details><summary>📄 Abstract</summary>
  Abliteration, a fine-tuning-free weight edit, removes refusal from open-weight large language models (LLMs). The developer of Arbitrary-Rank Ablation (ARA), an optimisation-based variant, reports that direction-based abliteration, which ablates a refusal direction, increasingly fails on newer models. On five release pairs, refusal removal did not become uniformly harder. Qwen2.5-32B and Qwen3.8-27B, Gemma-2-27B and Gemma-4-31B, OLMo-2-32B and Olmo-3.1-32B, Mistral-Small-2409 and Mistral-Small-3....
  </details>

- **2026-11-12** — Hongyu Li, Zhan Yu, Zhe Zhao et al. — [Data-Efficient LLM Safety Alignment Guided by Interpretable Features](http://arxiv.org/abs/2611.16183v1)
  <details><summary>📄 Abstract</summary>
  Existing large language models typically rely on massive fine-tuning datasets for safety alignment, which results in higher costs for safety alignment and often leads to the problem of over-refusal. We propose Less is Safer (LIS), a compact yet highly effective dataset for safety alignment, constructed through interpretable feature-guided selection and adversarial synthesis. Specifically, we leverage Sparse Autoencoder (SAE) activations to efficiently select prompts that cover diverse and interp...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-11-16** — Nikolaos Kekatos, Georgios Koutidis, Konstantinos Antonakopoulos et al. — [RESILAGENT: A Three-Pillar Architecture for Cyber-Physical Resilience in Electrical Power and Energy Systems](http://arxiv.org/abs/2611.21480v1)
  <details><summary>📄 Abstract</summary>
  Electrical Power and Energy Systems face hybrid threats that combine cyber intrusions, physical sabotage and climate-driven stress, and routinely outpace today's siloed monitoring stacks. We present RESILAGENT, a concept architecture organised around three operational pillars, Sensing & Data Intelligence, Resilience Analytics & Reporting, and Incident Response & Recovery, mediated by a Cloud-based Orchestrator and exercised through a closed Detect-Simulate-Decide-Sign loop. The framework fuses a...
  </details>

- **2026-11-16** — Sahaya Jestus Lazer, Kshitiz Aryal, Maanak Gupta et al. — [Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks](http://arxiv.org/abs/2611.21259v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems extend large language models with tools, memory, and multi-agent collaboration, introducing security risks at orchestration boundaries. These risks depend on how identities are represented, operations are authorized, and instructions or information propagate between components. We evaluate LangChain, LangGraph, AutoGen, and OpenClaw through twelve experiments mapped to the OWASP Top 10 for Agentic Applications using a common LLM (gpt-4o-mini). The experiments cover prompt inje...
  </details>

- **2026-11-15** — Hussein Jawad, Alexandre Landeau, Guy Fleury Iradukunda et al. — [Risk-certified prompt optimization for LLM-as-a-judge guardrails](http://arxiv.org/abs/2611.20156v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge guardrails are often controlled primarily through system prompts, yet standard prompt optimization methods target average performance rather than explicit safety constraints. This paper studies system-prompt selection as a constrained optimization problem: maximize benign pass rate while keeping the missed-attack rate below a user-specified level α with finite-sample statistical control. The framework combines LLM-based judging, automatic prompt generation, and distribution-free r...
  </details>

- **2026-11-15** — Yang Luo, Guangpu Chen, Yichen Liu et al. — [Security of Deep Research Agents: Attack Surface, Defenses, Benchmarks, and Agenda Seeding against Research Planning](http://arxiv.org/abs/2611.20045v1)
  <details><summary>📄 Abstract</summary>
  Deep research and agentic search agents autonomously retrieve content from the open web and generate reports with citations, and their outputs are often taken directly as research conclusions. This paper systematizes security research in this area along four stages, namely retrieval, planning, evidence integration, and report generation. We present a unified threat model, a taxonomy of attacks and defenses, and a review of evaluation benchmarks, and we align the area dimension by dimension with ...
  </details>

- **2026-11-14** — Harish Santhanalakshmi Ganesan — [Agent Authenticator: Passkey-Grade, Hardware-Bound Authentication for AI Agents](http://arxiv.org/abs/2611.19536v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now push code, publish packages, call model APIs and operate cloud resources on behalf of developers. They authenticate to these services with the same bearer secrets humans use, personal access tokens, API keys and package-registry tokens, stored where the model, its subprocesses and any co-resident malware can read them. Incidents in 2025 and 2026, including prompt-injection attacks on coding agents and self-propagating supply-chain worms, show that this arrangement fails in p...
  </details>

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


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 2 papers

- **2026-11-15** — Chirag Goel, Jacob Lavoie, Amirhossein Naghshzan et al. — [HEAMS: Holistic Evaluation of Agent Memory Systems](http://arxiv.org/abs/2611.20144v1)
  <details><summary>📄 Abstract</summary>
  Memory systems allow AI agents to persist information across interactions, making them more personalized and more capable on long-horizon tasks. This persistence introduces new risks: stored information can be disclosed in inappropriate contexts, resist correction or deletion, be retained beyond what users desire, or be poisoned to influence later agent behaviour. Yet memory systems are typically evaluated on task performance and efficiency alone. We argue that a memory system should instead be ...
  </details>

- **2026-11-15** — Ji Guo, Xiaolong Qin, Jin Jiang et al. — [HalluProbe: Exploiting VLM Hallucinations for Backdoor Detection](http://arxiv.org/abs/2611.19868v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are vulnerable to backdoor attacks introduced through data poisoning, making effective backdoor detection a critical security challenge. In this paper, we uncover a novel connection between VLM hallucinations and backdoor behaviors and exploit this connection for backdoor detection. Our key insight is that poisoned training data induces strong language priors toward the backdoor target token, while such priors are also a major source of hallucinations. This suggests...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-11-16** — Masanori Hanada — [Deep Learning for Physicists: From Linear Regression to Reasoning Models](http://arxiv.org/abs/2611.21295v1)
  <details><summary>📄 Abstract</summary>
  These lecture notes are based on an introductory course on neural networks and deep learning that the author taught in the School of Mathematical Sciences at Queen Mary University of London in 2023/24 and 2024/25. The author, however, is a physicist, and it shows: wherever possible, ideas are explained with physical intuition rather than heavy formalism. Readers with a background in physics or mathematics who want a self-contained, introductory route into modern machine learning may therefore fi...
  </details>

- **2026-11-16** — Xiaoqing Chen, Jiayi Ouyang, Dongrui Wu — [SmoothShift: Disrupting Visual Adversarial Attacks on LVLMs at Test Time](http://arxiv.org/abs/2611.20537v1)
  <details><summary>📄 Abstract</summary>
  Visual adversarial perturbations can substantially impair large vision-language models (LVLMs) despite introducing only subtle input changes. To understand how these small changes cause substantial errors, we investigate their optimization and propagation through the model, revealing two key findings. First, stronger attacks rely on finer iterative optimization, while subtle input perturbations induce representation discrepancies that are amplified layer by layer through the vision encoder and p...
  </details>

- **2026-11-13** — Sandip Nandi, Aishwarya Bose, Apurba Bose et al. — [TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents](http://arxiv.org/abs/2611.18493v1)
  <details><summary>📄 Abstract</summary>
  Autonomous trading agents need controls that prevent problematic orders without making legitimate tasks impractical. We study this aspect of agentic compliance with TradeGauntlet, a replayable limit-order-book simulator that separates detection, prevention, and execution cost. In 1,680 simulated sessions with Claude Haiku 5.5 and Sonnet 5.5, all conduct alerts were self-matches. Gates eliminated those alerts by rejecting self-crossing orders, while the aggregate-gate condition reduced Sonnet's t...
  </details>

- **2026-11-13** — Nasir Khan, Asmaa Abdallah, Abdulkadir Celik et al. — [Causal AI-Driven Secure mmWave Beam Alignment with Defensive Variational Autoencoders](http://arxiv.org/abs/2611.18321v1)
  <details><summary>📄 Abstract</summary>
  Efficient and secure beam alignment is essential for mmWave communication systems. However, existing deep learning (DL)-based beam alignment methods often neglect causal relationships between inputs and outputs, resulting in limited interpretability, poor generalization, and excessive beam sweeping. Moreover, these DL solutions are vulnerable to adversarial attacks, where small perturbations in received power measurements can mislead beam classifiers. To overcome these issues, we propose a causa...
  </details>

- **2026-11-13** — Stephen Obadinma, Xiaodan Zhu — [Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners](http://arxiv.org/abs/2611.17910v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly deployed as autonomous agents, their abilities in navigating automated planning tasks have become essential. However, despite their strengths, LLMs' planning ability is not robust, particularly when they are not allowed to exploit commonsense cues in the symbolic vocabulary (e.g., names of actions, predicates, and objects) used to define planning tasks. This makes LLMs unreliable compared to symbolic planners. With recent reasoning models showing ...
  </details>

- **2026-11-13** — Zahid Mansur, Kalpana Yadav, Deepak Mishra — [Cracks in Embeddings: Robustness and Stability of JEPA-Based Chest X-Ray Representations](http://arxiv.org/abs/2611.17905v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised Joint Embedding Predictive Architecture (JEPA) models are increasingly used for medical imaging, however there is a limited understanding about robustness of these models toward real-world image changes. We test four JEPA-based chest X-ray encoders, trained on 78,468 NIH ChestX-ray14 images, under six tests: two black-box adversarial attacks (SPSA, Boundary Attack), three image corruptions (Gaussian noise, brightness shift, contrast shift), and a label-scarcity test, measuring em...
  </details>

- **2026-11-12** — Bo Han — [Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models](http://arxiv.org/abs/2611.16628v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning can teach vision-language models (VLMs) to decline harmful image-text requests, but how safe the result becomes is set indirectly, through reward weights found by trial runs. Stating safety as budgets on the rate of harmful assistance and the rate of over-refusal, enforced by Lagrange multipliers inside GRPO with an off-the-shelf scorer as the cost, is the natural fix, and it fails twice. The multiplier compares the scorer's mean with the budget, and scorers built for rank...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 22 papers

- **2026-11-16** — Guangzhi Sun, Xiao Zhan, Shuai Wang et al. — [AudioTrace: File-Level Membership Detection for Audio Large Language Models](http://arxiv.org/abs/2611.21088v1)
  <details><summary>📄 Abstract</summary>
  Significant privacy and copyright concerns are raised by the use of publicly available audio recordings to train audio large language models (LLMs), yet effective auditing methods remain limited. Existing membership inference attacks typically assume knowledge of complete training examples, including their associated textual supervision. In practice, however, audio recordings may be paired with privately generated transcripts, captions, or question-answer pairs that are unavailable to owners of ...
  </details>

- **2026-11-16** — Chang Xu, Hao Wang, Gedi Zhou et al. — [Where the Evidence Lives: Measuring Privacy and Diagnosability of Exported AI-Agent Traces](http://arxiv.org/abs/2611.20389v1)
  <details><summary>📄 Abstract</summary>
  Execution traces help diagnose AI-agent failures, but sharing them can expose customer identities. For example, detecting that an agent handled the wrong customer's records requires knowing whether the records belong to the requested customer, but not necessarily knowing who that customer is. Our executable benchmark measures what a trace export reveals and whether a proposed repair restores the correct output in synthetic multi-tenant workflows. Conventional redaction can remove evidence needed...
  </details>

- **2026-11-16** — Bojing Feng, Jinqiu Deng, Zihan Hong et al. — [Regularizing Treatment Leakage for LLM-based Uplift Estimation](http://arxiv.org/abs/2611.20794v1)
  <details><summary>📄 Abstract</summary>
  Uplift modeling estimates the conditional average treatment effect (CATE) and supports industrial decisions such as promotional pricing. When large language models (LLMs) encode product text, treatment-revealing content can introduce shortcuts that do not transfer to deployment. We propose \emph{LLM-based Uplift Leakage Regularization} (\textsc{LULR}), which uses a CLUB-based penalty on the causal head's trainable shared representation while keeping the LLM encoder frozen. Controlled proxy exper...
  </details>

- **2026-11-16** — Max Schulte, Hartmut Surmann, Julien Meine — [Counting What Matters: Reducing Redundant Object Detections in Overlapping UAV Mapping Imagery for Disaster Response](http://arxiv.org/abs/2611.21076v1)
  <details><summary>📄 Abstract</summary>
  UAV mapping flights enable rapid aerial reconnaissance of large-scale incident sites in civil protection. However, the image overlap required for orthophoto generation causes every physical object to be detected multiple times across images, while dynamic objects may be omitted from or duplicated in the resulting orthomosaic. Analysis based on the orthophoto alone is therefore structurally insufficient. We address this by detecting objects on the individual images and merging redundant detection...
  </details>

- **2026-11-16** — Ahmet Bestami Kose, Mehmet Sergen Catal, Muhammet Cagri Yeke et al. — [Vision-Language Model-Based Phase-OTDR Event Classification](http://arxiv.org/abs/2611.20841v1)
  <details><summary>📄 Abstract</summary>
  Phase-sensitive optical time-domain reflectometry (Phase-OTDR) enables distributed vibration sensing, but reliable event classification has traditionally relied on fully supervised models that require extensive annotated data. This study examines the adaptability of a Vision-Language Model (VLM) for Phase-OTDR event recognition through few-shot learning. Raw samples are converted into Short-Time Fourier Transform (STFT) dB-magnitude spectrogram mosaics, color-mapped and resized to RGB images, an...
  </details>

- **2026-11-16** — Louis Mouchon, Alexis Lainault — [Surprise-Gated Memory for Live Speaker Diarization](http://arxiv.org/abs/2611.20819v1)
  <details><summary>📄 Abstract</summary>
  We transpose the Surprise-Gated Memory recipe, a frozen encoder plus a calibrated novelty signal that gates a one-shot episodic store consolidated by periodic replay, from continual visual learning to live speaker diarization. The moment-to-moment question a streaming diarizer must answer, whether an arriving voice belongs to an already-heard speaker or a new one, is a known-versus-novel decision, exactly the decision the surprise gate is built for. On a frozen fine-tuned DiariZen backbone, our ...
  </details>

- **2026-11-16** — Zhe Dong, Guanyu Cai, Yuchen Jiang et al. — [Building Fully On-Device GUI Agents with Mobile NPUs](http://arxiv.org/abs/2611.20772v1)
  <details><summary>📄 Abstract</summary>
  Mobile GUI agents are increasingly used to automate everyday smartphone tasks, but most existing systems still rely on cloud-hosted models or remote inference, introducing repeated communication latency, privacy exposure, and dependence on network availability. Modern smartphones integrate neural processing units (NPUs) that provide an attractive substrate for fully on-device LLM inference. However, directly deploying conventional GUI-agent pipelines on mobile NPUs is inefficient. GUI-agent infe...
  </details>

- **2026-11-16** — German Devchich, Timur Akhtyamov, Denis Fatykhoph et al. — [CLIFT: Contrastive LiDAR Instance Features for 3D Pedestrian Tracking](http://arxiv.org/abs/2611.20737v1)
  <details><summary>📄 Abstract</summary>
  A social robot has to keep track of the people around it over time to plan its motion, a task handled by 3D multi-object tracking. For the LiDAR modality, trackers usually sit on top of a detector and link its detections across frames with a separate motion model or re-identification network. We instead show how a 3D LiDAR detector itself can be turned into a tracker by adding an instance-level contrastive objective on its intermediate voxel features. Each embedding is read from the voxels insid...
  </details>

- **2026-11-16** — Asmau Lawal Bilbis, Nathanael L. Baisa, Amudhavel Jayavel — [VisDrone-ReID: A Unified Multi-Category Object Re-Identification Benchmark](http://arxiv.org/abs/2611.20372v1)
  <details><summary>📄 Abstract</summary>
  Object re-identification (Re-ID) benchmarks remain predominantly confined to single-category evaluations, limiting the development of unified systems capable of operating across diverse object types. This paper presents VisDrone-ReID, a unified multi-category Re-ID benchmark derived from the VisDrone2019-MOT dataset through a principled conversion pipeline. The pipeline resolves structural incompatibilities between multi-object tracking annotations and Re-ID evaluation requirements, addressing s...
  </details>

- **2026-11-15** — Bowen Sun, Chaowei Xiao — [Where the Savings Go: The Limits of Hiding Cross-Tenant Cache Hits in LLM Serving](http://arxiv.org/abs/2611.20291v1)
  <details><summary>📄 Abstract</summary>
  LLM serving engines cache prompt prefixes; a cache hit skips computation and returns faster, so a shared cache reveals whether others have sent a given text. Per-account salting closes this channel but forgoes cross-tenant reuse and isolates only whole accounts, even where access is redistributed or trust domains are subdivided below them. Defenses that share globally but hide hits promise reuse without relying on account boundaries. Hiding a hit requires everything tenants observe afterwards to...
  </details>

- **2026-11-15** — Tushar Nayan, Mohammed Al Duniawi, Song Fang et al. — [Understanding Users' Security, Privacy, and Trust Concerns in Healthcare AI Systems](http://arxiv.org/abs/2611.20223v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence is increasingly integrated into healthcare systems, from clinical information retrieval to workflow automation and decision support, which introduces new security, privacy, and trust risks with direct implications for patient care. While prior work has examined these risks from technical and regulatory perspectives, less is known about how these risks are naturally discussed in online communities. To address this gap, we conduct a large-scale analysis of 14 medical commun...
  </details>

- **2026-11-15** — Jinfeng Xu, Zheyu Chen, Ziyue Peng et al. — [Reflection Is Not Always Worth It: Budgeted Reflection Allocation for Recommendation Agents](http://arxiv.org/abs/2611.19847v1)
  <details><summary>📄 Abstract</summary>
  This work aims to make recommendation agents more efficient by reducing unnecessary LLM reflection while preserving full-catalog ranking and inference reranking. Since BRAVE changes only how training-time reflection is allocated, it does not introduce new user data requirements or additional LLM exposure beyond the base agent protocol. The main potential risk is that a poorly calibrated allocator may assign less reflection to users whose preferences are sparse, niche, or under-represented, which...
  </details>

- **2026-11-15** — Yuxuan Xiao, Shanshan Zhang, Shengcai Liao et al. — [Two-Stage Prompt Learning: A Unified Framework for Person ReID without Clothing Hypothesis](http://arxiv.org/abs/2611.19939v1)
  <details><summary>📄 Abstract</summary>
  Person re-identification (ReID) in real-world scenarios involves three clothes conditions: the same clothes (SC), changed clothes (CC), and the unknown (GEN) scenario where clothes changes are not specified. Existing methods typically train separate SC- or CC-specific models, which limits generalization across all conditions. Meanwhile, pre-trained visual-language models (VLMs) such as CLIP have shown strong generalization ability in various vision tasks, motivating recent ReID methods to incorp...
  </details>

- **2026-11-15** — Dongwu Qian — [Grounding Language Models in Speech Does Not Fix "AI Flavor": Calibrated LLM Judges, Goodhart Traps, and a Preference-Tuning Fix](http://arxiv.org/abs/2611.19840v1)
  <details><summary>📄 Abstract</summary>
  Chinese outputs of large language models carry a perceptible "AI flavor": formulaic sentence frames, stacked written-register connectives, repetition loops, and layout leakage. A popular hypothesis blames text-only training for the missing inner-speech layer of human writing; injecting speech or prosody signals should therefore reduce it. We test it with controlled interventions on a 0.6B model; all three fail: (i) phoneme-interleaved continued pretraining yields no spokenness gain under text-ma...
  </details>

- **2026-11-13** — Swarn Priya — [VellSSLH: Sound Type-Guided Selective Speculative Load Hardening for LLVM IR](http://arxiv.org/abs/2611.18463v1)
  <details><summary>📄 Abstract</summary>
  Constant-time cryptographic programs written in C can still leak secrets during speculative execution. Mispredicted branches may allow instructions to access secret data and expose it through observable behavior. Speculative load hardening (SLH) addresses these leaks, but protecting values unnecessarily can introduce significant runtime overhead. We present VellSSLH, which selectively inserts speculative load hardening at LLVM IR. Programmers specify Public and Secret inputs in annotated C progr...
  </details>

- **2026-11-13** — Yuhang Wang, Jingxin Yang, Chuheng Wei et al. — [CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving](http://arxiv.org/abs/2611.18442v1)
  <details><summary>📄 Abstract</summary>
  Open driving releases and usage-based insurance programs often claim to prevent privacy breaches by omitting GPS records when sharing or collecting vehicle data. However, removing GPS coordinates from driving logs does not erase the location information carried by vehicle signals. While prior route-inference attacks have demonstrated that speed, steering, and driving events can be matched to road networks to reconstruct trajectories, existing studies rely on inconsistent prior assumptions and ev...
  </details>

- **2026-11-13** — Dhruv Dixit, Khushi Patel, Congcong Xu et al. — [ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models](http://arxiv.org/abs/2611.18494v1)
  <details><summary>📄 Abstract</summary>
  Small language models are attractive for local, low-cost, and privacy-sensitive deployment, but they remain unreliable on mathematical reasoning tasks that require decomposition, exact computation, tool use, and verification. We introduce \textbf{ARCHER}: \textbf{A}ction-trace \textbf{R}einforcement for \textbf{C}alculator-grounded \textbf{H}ierarchical \textbf{E}xecutable \textbf{R}easoning, a two-stage framework for training small language models (SLMs) to produce executable and auditable reas...
  </details>

- **2026-11-13** — Mohammed Efaz, Udo Bub, Itilekha Podder — [MeReader: An Offline, Privacy-Preserving, Progress-Aware AI Assistant for Narrative eBook Reading](http://arxiv.org/abs/2611.18513v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces MeReader, a privacy-preserving, offline and progress-aware AI assistant designed to function as a contextual companion for narrative reading on consumer hardware. Unlike conventional Large Language Model (LLM)-based systems that process documents/books online in an all-texts-at-once type of way, thereby risking narrative spoilers, MeReader confines both retrieval and generation to the reader's distinct position in the text. The system integrates a hybrid retrieval architect...
  </details>

- **2026-11-13** — Hua Yang, Aditya Bhardwaj, Shidong Pan et al. — [PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review](http://arxiv.org/abs/2611.18293v1)
  <details><summary>📄 Abstract</summary>
  Coding agents increasingly review code, yet whether they catch the privacy defects that laws such as the GDPR require software to avoid remains largely untested, partly because few datasets connect real privacy defects to their accepted fixes and review context. We present PrivacyPR, a dataset of 4,131 merged GitHub pull requests (PRs) from 1,469 repositories, created between June 2018 and January 2024. Each PR includes its commits, diffs, review discussion, and LLM-generated labels for privacy ...
  </details>

- **2026-11-13** — Saisuchith Mahajan, Aditey Nandan, Rohit Singh et al. — [JaRS: Contrast-Free Localization of Memorized Regions in Diffusion Models via Jacobian Row Sums](http://arxiv.org/abs/2611.18024v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models sometimes memorize and reproduce regions of their training images, raising privacy and copyright concerns. We aim to localize these regions. Existing contrast-based methods use the diagonal of the denoiser Jacobian, which reflects the posterior variance of each pixel. However, a small diagonal entry is ambiguous: it signals either memorization or averaging over many neighboring pixels in smooth or predictable regions. To resolve this ambiguity, these methods subtract a reference...
  </details>

- **2026-11-12** — Aman Mujahid, Anita Penkova — [Beyond Binary Classification: Multiclass Machine Learning for Diabetes and Prediabetes Risk Prediction Using NHANES](http://arxiv.org/abs/2611.16756v1)
  <details><summary>📄 Abstract</summary>
  Detecting diabetes risk early is important for preventing disease progression. Most existing machine learning approaches focus on binary classification, which limits their ability to capture intermediate risk states such as prediabetes. We develop a supervised learning framework to classify adults as normal, prediabetic, or diabetic using National Health and Nutrition Examination Survey data. The framework uses routinely collected demographic, clinical, and lifestyle variables from 15,356 adults...
  </details>

- **2026-11-12** — Julian Szymanski, Tomasz Sankowski, Piotr Sulewski et al. — [Acoustic Respiratory Phase Detection on Mobile Devices](http://arxiv.org/abs/2611.16710v1)
  <details><summary>📄 Abstract</summary>
  Breathing monitoring is important for well-being, stress regulation, and guided breathing exercises, yet existing approaches often rely on contact-based sensors or controlled environments. This paper presents a non-invasive framework for respiratory phase detection using acoustic signals recorded on commodity smartphones. The proposed hybrid CNN-Transformer architecture combines local spectral feature extraction with long-range temporal modeling to capture the cyclic structure of breathing. The ...
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
*滥用与误用 / Misuse & Abuse* — 9 papers

- **2026-11-16** — Quoc Nguyen, Trung Le, Dinh Phung et al. — [Model Immunization Beyond Condition Numbers: The Importance of Plateau Regions](http://arxiv.org/abs/2611.20472v1)
  <details><summary>📄 Abstract</summary>
  Harmful fine-tuning can rapidly compromise safety alignment in Large Language Models, underscoring the vulnerability of deployed models to post-release modification. While prior work motivates model immunization by inducing ill-conditioned curvature to slow harmful optimization, this approach is not scalable due to the high computational cost of Hessian estimation. We refine this paradigm by extending the theoretical framework to prioritize plateau regions alongside curvature. We further introdu...
  </details>

- **2026-11-16** — Minsuk Jang, Minseok Son, KiHyun Seol et al. — [CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](http://arxiv.org/abs/2611.20821v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign.   We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear benign under a general-purpose rubric yet carry a latent harmful meaning in a target culture, and use it to build CuRSE-Bench: 10,709 culture-specific prompts and 2,648 culture-general controls over six regions and ten...
  </details>

- **2026-11-16** — Younghwan Kil, Giung Nam, Joonhyeong Park et al. — [Example-Based Spatial Guidance for Training-Free Concept Erasure in Diffusion Models](http://arxiv.org/abs/2611.20623v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) diffusion models often synthesize policy-violating content, necessitating robust safeguards and rigorous evaluation frameworks. However, current approaches remain largely monolithic in both execution and evaluation, limited to coarse-grained categorization within broad unsafe concepts. Such approaches fail to account for the specific constituent factors of a violation, resulting in weak learning signals and allowing model collapse to bypass safety checks. To overcome these li...
  </details>

- **2026-11-16** — Koki Itai, Jun Hirako, Hiroaki Yamagiwa — [Abstention Direction in Large Language Models: Mechanistic Interpretability of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment](http://arxiv.org/abs/2611.20441v1)
  <details><summary>📄 Abstract</summary>
  Abstention, the withholding of a response by a large language model (LLM) under uncertainty or safety risks, is essential for trustworthy models. The causes of abstention fall into three perspectives: ambiguity in the Query (Q), limits of Model Knowledge (MK), and misalignment with Human Values (HV). However, prior analyses of internal representations have focused on HV, using a refusal direction computed from harmful and harmless queries. No study has analyzed the three perspectives jointly. We...
  </details>

- **2026-11-16** — Janhavi Khindkar, Nataliia Povarova — [Refusal Register is Causally Steerable: Decomposing the Refusal Direction into Category-Aligned Components in Gemma-2-9B-IT](http://arxiv.org/abs/2611.20405v1)
  <details><summary>📄 Abstract</summary>
  Prior work shows that refusal in instruction-tuned language models can be ablated by intervening on a single residual-stream direction (Arditi et al., 2024), and more recent work finds multiple refusal-mediating directions and concept cones (Wollschläger et al., 2025). We ask a different question: do refusal-related directions carry information about the register of refusal language - how the model refuses - and not only whether it refuses? In Gemma-2-9B-IT we identify two SVM-derived linear dir...
  </details>

- **2026-11-15** — Chansu Han, Seok-Hwan Choi, Takeshi Takahashi — [Where Is Rank-1 DiM Refusal Intervenable in Multimodal LM Derivatives?](http://arxiv.org/abs/2611.19826v1)
  <details><summary>📄 Abstract</summary>
  Open-weight model hubs now ship not only chat checkpoints but a long tail of derivatives---fine-tunes, safety guards, vision--language models (VLMs), audio wrappers, and generative heads---yet residual-stream safety audits still often intervene at a single site, usually the text decoder $T$. We ask a localization question under one shared mean / rank-1 difference-in-means (DiM) extract$=$intervene protocol, with matched-norm random and empty-rate controls: does causal chat attack lift concentrat...
  </details>

- **2026-11-15** — Ewelina Gajewska — [A Dataset for Misogyny Detection in Polish Social Media: Transferability of Hateful Speech Detection from General to Specific Types of Hate](http://arxiv.org/abs/2611.20044v1)
  <details><summary>📄 Abstract</summary>
  Harmful language detection is commonly evaluated on broadly defined hate speech and toxicity benchmarks, yet it remains unclear whether models that successfully detect harmful language in general can transfer this capability to more specific forms of hate. We investigate this problem for misogyny detection in Polish, an area for which dedicated resources remain scarce. We introduce a new dataset of Polish social media comments annotated for misogyny, gender-directed hateful speech. Using this re...
  </details>

- **2026-11-15** — Jason Lee, Dikshanta Pokhrel, Phonn Nay Khant et al. — [MathaMAGICal: Validating Trajectory Data Attribution During Capability Acquisition](http://arxiv.org/abs/2611.19692v1)
  <details><summary>📄 Abstract</summary>
  Influence-function-based methods like MAGIC provide exact first-order scores for trajectory data attribution, yet only retraining indicates whether those scores accurately predict data removal. We evaluate MAGIC on $86$M- and $152$M-parameter GPT-2-style models learning multistep arithmetic from scratch on filtered web text and four synthetic math families. Full-run attribution at $86$M suffers from numerical overflow, and even with metagradient clipping, scores correlate near chance with retrai...
  </details>

- **2026-11-12** — Tiansheng Huang, Ananth Balashankar, Virat Shejwalkar et al. — [Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function](http://arxiv.org/abs/2611.16369v1)
  <details><summary>📄 Abstract</summary>
  We expose a safety vulnerability on nascent agentic reinforcement-learning-as-a-service. Specifically, with a cost as low as \$20, we show that safety alignment of a large language model (e.g., Inkling) can be completely subverted through rounds of harmful agentic reinforcement learning (agentic RL) with a toxic environment from its users. We also demonstrate that upon a successful harmful agentic RL attack via the service API, the attackers can potentially use the safety-degraded model to assis...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 4 papers

- **2026-11-14** — Zhen Wan — [VAST: Compiling Grounded Vulnerability Scenarios into Verifiable, Multi-Step Environments for Evaluating LLM Red-Team Agents](http://arxiv.org/abs/2611.19465v1)
  <details><summary>📄 Abstract</summary>
  Evaluating Large Language Model (LLM) security agents requires reproducible environments whose workflow difficulty can be varied and whose failures can be diagnosed. We present VAST (Verifiable Adversarial Scenario Training & Evaluation), a declarative range compiler separating vulnerability scenarios from a compiler-introduced workflow-hardening layer. Following a post-hoc code and AST audit across all topics, the main benchmark retains 109 seed edges (45 with strict upstream CVE annotations), ...
  </details>

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


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 51 papers

- **2026-11-16** — Jaime C. Acosta, Anantaa Kotal, Aritran Piplai — [ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises](http://arxiv.org/abs/2611.21579v1)
  <details><summary>📄 Abstract</summary>
  Cyber-range and capture-the-flag scenario construction remains labor-intensive because authors must coordinate infrastructure, vulnerable services, attack paths, artifacts, and success conditions. LLMs can propose detailed exercises, but plausible descriptions do not guarantee deployable software or verifiable objectives. We present ScenarioForge, which turns high-level requirements into resource-grounded topologies, services, traffic, segmentation, and challenge chains, then instantiates and va...
  </details>

- **2026-11-16** — Samuel Hartzmark, Kelly Shue — [The Geoengineering Put: Ecological Debt, Termination Risk, and Asset Prices](http://arxiv.org/abs/2611.21568v1)
  <details><summary>📄 Abstract</summary>
  Solar geoengineering offers an inexpensive and fast-acting way to lower global temperatures without removing carbon from the atmosphere. As warming intensifies, climate-vulnerable countries face growing incentives to deploy geoengineering unilaterally. The economic and financial consequences of this prospect remain largely overlooked. We develop a general equilibrium macro-finance framework in which geoengineering acts as a put option on climate damages, funded by the "ecological debt" of masked...
  </details>

- **2026-11-16** — Yu-Hsuan Ho, Yiming Xiao, Hao-En Lai et al. — [Wildfire-SSR: Geolocation-Aware Multimodal Fusion for Structure-Level Wildfire Risk Assessment](http://arxiv.org/abs/2611.21563v1)
  <details><summary>📄 Abstract</summary>
  Structure-level wildfire vulnerability assessment is critical for reducing losses in wildland-urban interface communities, yet existing methods often fail to combine parcel-scale ignition pathways with community-scale geographic coverage. This study introduces Wildfire-SSR (Satellite and Street-view for wildfire Risk), a geolocation-aware multimodal framework that integrates macro-scale satellite context with micro-scale street-view evidence. A Vision-Language Model extracts wildfire-relevant bu...
  </details>

- **2026-11-16** — Yulun Wu, Nicola Bastianello, Karl Henrik Johansson et al. — [Efficient Modeling of Multi-Agent Systems via Structure-Aware Physics-Informed Learning](http://arxiv.org/abs/2611.21404v1)
  <details><summary>📄 Abstract</summary>
  Modeling large multi-agent systems poses challenges for trajectory inference and parameter identification, as network size and coupling increase computational demands and partial observations require reconstructing unobserved states. We propose MAS-PINN, a neural-network architecture with a tailored training algorithm for a physics-informed learning framework that leverages the network topology and the agents' similarity to reduce computational and memory costs of simulating and identifying mult...
  </details>

- **2026-11-16** — Zhiyuan Wang, Yuanchang Ye, Jiahao Yuan et al. — [Stability-Compensated Threshold Calibration for Selection-Conditioned Risk Control in Large Language Models](http://arxiv.org/abs/2611.21384v1)
  <details><summary>📄 Abstract</summary>
  Large language models often produce hallucinated answers, motivating selective prediction policies that abstain on uncertain queries. However, heuristic uncertainty thresholds alone do not provide statistical control of errors among accepted predictions. Linear Expectation Constraints (LEC) reduce selection-conditioned error rate (SCER) calibration to a nonpositive expected linear-loss constraint, but the associated loss is non-monotonic in the acceptance threshold. We construct an exact counter...
  </details>

- **2026-11-16** — Mafalda Batalha, Javier Viviens — [A Game of Throngs: How Spotlight Tourism Reshapes Local Economies](http://arxiv.org/abs/2611.21364v1)
  <details><summary>📄 Abstract</summary>
  In July 2017, San Juan de Gaztelugatxe, a modest chapel in the Basque Country, appeared as "Dragonstone" in Game of Thrones, transforming a locally known site with limited tourism activity into a global tourist destination overnight. We exploit this exogenous spotlight shock to estimate its causal effects on the local economy using a novel administrative dataset and a Synthetic Control approach. We find an abrupt increase in tourism activity, far exceeding the effects documented in the literatur...
  </details>

- **2026-11-16** — Yunyang Ge, Weijie Kong, Ryan Xu et al. — [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](http://arxiv.org/abs/2611.21339v1)
  <details><summary>📄 Abstract</summary>
  Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs. To address these challenges, we present MovieRoll, a base-to-distilled framework that connects streaming fine-tuning, long-rollout distillation, and long-horizon inference. We first establish a robust multi-step base through Window-wise Teacher Forcing (WinTF), which jointly denoises chunks at progressive noise levels with bidirectional attention within each ...
  </details>

- **2026-11-16** — Abdullah Ahmed, Yun Yang — [In-Context Estimation and Prediction for Parametric ODEs](http://arxiv.org/abs/2611.21268v1)
  <details><summary>📄 Abstract</summary>
  Transformers have demonstrated the ability to perform in-context learning, that is, to adapt to new tasks from a few examples without updating their parameters. Existing theory has largely focused on emulating gradient-based algorithms for convex statistical problems or establishing general function approximation guarantees without exploiting the underlying statistical structure. We study in-context parameter estimation and trajectory prediction for parametric ordinary differential equations (OD...
  </details>

- **2026-11-16** — Ruizhe Wang, Rui Liu, Hongliang Chen et al. — [VASR: Vector-Aware Assembly Planning with Equivalent Structures and Repair-Cost Feedback](http://arxiv.org/abs/2611.20984v1)
  <details><summary>📄 Abstract</summary>
  Furniture assembly planning requires inferring subassembly hierarchies from individual parts and a target illustration. Existing raster-based methods do not explicitly exploit the geometric and structural information in SVG drawings. We introduce VASR, a framework that fuses features from a dedicated SVG encoder with visual representations from a pretrained vision-language model to predict assembly hierarchies. To avoid penalizing valid alternatives to a reference assembly tree, we propose Repai...
  </details>

- **2026-11-16** — Eunkyeong Lee, Junhyung Moon, Seunggwan Hong et al. — [Jev-as-a-Reward: Validating Probabilistic Safety Judges for Reinforcement Learning](http://arxiv.org/abs/2611.20955v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic safety judges return the probability of a safety label and cheaply score reinforcement learning rollouts. A confidence gate sends only uncertain verdicts to a stronger LLM judge, which leaves confidently passed harm in a blind spot. Policies can exploit this blind spot, and commercial judges release new versions. We propose a protocol that validates such a judge before and during training, separates the share of confidently passed harm from its amount, and re-validates it after eac...
  </details>

- **2026-11-16** — Dean Zenner, Andreas Rupp, Thomas Schuster — [Quantitative approximation for Fourier neural operators in controlled ordinary differential equations](http://arxiv.org/abs/2611.20883v1)
  <details><summary>📄 Abstract</summary>
  Fourier neural operators (FNOs) avoid the curse of parametric complexity when approximating the solution operator of certain partial differential equations (PDEs). While recent studies primarily focus on PDEs, in this article we derive upper error bounds for approximating the solution operator of controlled ordinary differential equations (CODEs) $\dot{y}=f(y,u)$ using a FNO. Under a Carathéodory setting and suitable regularity assumptions, including a smallness condition, we prove that the size...
  </details>

- **2026-11-16** — Guanqi Lyu, Decheng Qiu, Guangyang Zhang et al. — [ProcReverser: Multi-Agent Black-Box Microarchitectural Reverse Engineering for Processor Vulnerability Analysis](http://arxiv.org/abs/2611.20827v1)
  <details><summary>📄 Abstract</summary>
  When processor implementation details are unavailable, black-box microarchitectural reverse engineering helps security researchers identify hardware conditions related to security vulnerabilities. However, this process requires substantial manual effort to design experiments, develop test programs, and analyze results for each processor. We present ProcReverser, a multi-agent system that automates this process. ProcReverser uses execution feedback to improve experimental plans and test programs ...
  </details>

- **2026-11-16** — Mehmet Sergen Catal, Abdurrahman Gumus, Mehmet Zübeyir Ünlü — [PhaseCLIP: Phase-Aware Frequency-Domain Adaptation of Vision-Language Models for Few-Shot Remote-Sensing Classification](http://arxiv.org/abs/2611.20787v1)
  <details><summary>📄 Abstract</summary>
  Remote-sensing (RS) image scene classification aims to assign a semantic category to an overhead image, and in practice must often do so from only a handful of labelled examples, since annotation requires expert interpretation and the resulting labels transfer poorly across sensors and regions. Recent progress has come from adapting vision-language models (VLMs) such as CLIP, through learned prompts or feature adapters. Although effective, these methods construct their representation entirely in...
  </details>

- **2026-11-16** — Kai Tang, Xing Zheng, Haobo Wang et al. — [SpeCal: Spectral Calibration for Unsupervised RLVR](http://arxiv.org/abs/2611.20691v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning abilities of large language models, but its dependence on ground-truth answers or external verifiers limits its ability to exploit abundant unlabeled reasoning data. Unsupervised RLVR alleviates this bottleneck by deriving scalar rewards from the model's own rollouts. However, the reliability of such self-generated supervision varies substantially across rollout groups and individual responses, while e...
  </details>

- **2026-11-16** — Hoan My Tran, Xin Wang, Xuechen Liu — [Progressive Layer-wise Supervision: Deep-to-Shallow Supervision Annealing for Efficient and Robust Speech Deepfake Detection](http://arxiv.org/abs/2611.20630v1)
  <details><summary>📄 Abstract</summary>
  Speech foundation models pretrained via self-supervised learning provide powerful representations for deepfake detection, yet we find that standard fine-tuning exploits only the deepest transformer layers-leaving the majority of the network's capacity discriminatively inert. Layer-wise probing of XLS-R-128 reveals that the top two-thirds of the transformer stack contribute negligibly to anti-spoofing performance after standard fine-tuning, a phenomenon we term shallow-layer dormancy. We connect ...
  </details>

- **2026-11-16** — Chaitanya Garware — [Beyond the Patch: Reconstructing an Incomplete-Fix Patch Bypass in LLM Agent Frameworks with Control-Gated, Benign Probes](http://arxiv.org/abs/2611.20514v1)
  <details><summary>📄 Abstract</summary>
  Replaying a vulnerability's original proof-of-concept after patching tests whether its reported trigger remains reproducible, but does not establish that the underlying security invariant holds on other code paths. We present a benign, control-gated reconstruction method and a pilot study across four LLM agent frameworks and four invariant classes. For PraisonAI, we compare original-trigger replay (B0) with a distinct sibling-path probe (M). We also perform five before/after reconstructions acro...
  </details>

- **2026-11-16** — Marjan Beheshti, Ronghua Xu — [KVMARK: Fragile Watermarking for KV-Cache Integrity in Latent Multi-Agent Systems](http://arxiv.org/abs/2611.20454v1)
  <details><summary>📄 Abstract</summary>
  Latent multi-agent communication directly transfers Key-Value (KV) cache tensors between transformer-based agents, bypassing text serialization entirely. While computationally efficient and reasoning accurate, this communication channel is opaque and vulnerable to man-in-the-middle tampering, a threat vector unaddressed by existing text-based or behavioral watermarks, which cannot operate on continuous internal representations. To address this vulnerability, we propose KVMark, a training-free, z...
  </details>

- **2026-11-16** — Kazuo Aoyama, Hiroshi Sawada, Shota Kita et al. — [Architectural Principles for Parameter-Efficient Unitary Transformations in Coherent Optical Neural Networks](http://arxiv.org/abs/2611.20390v1)
  <details><summary>📄 Abstract</summary>
  Coherent optical neural networks based on interferometric architectures offer a promising route toward high-throughput, energy-efficient computation by exploiting the multiple degrees of freedom of light, including spatial, temporal, and spectral modes. However, practical implementations are constrained by the number of tunable parameters due to fabrication complexity, device footprint, and control overhead. In such parameter-constrained settings, achieving high expressive power remains a centra...
  </details>

- **2026-11-15** — Neel Rajani, Ivan Titov — [Protecting Safety during Reasoning Training with Low-Rank Fisher Regularisation](http://arxiv.org/abs/2611.20288v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained to have safety guardrails, but these can be compromised while fine-tuning for new capabilities, such as reasoning. One way to mitigate this degradation is to modify the fine-tuning objective to preserve safety behaviour, but doing so effectively and efficiently remains challenging. We revisit Elastic Weight Consolidation (EWC), which penalises parameter updates based on sensitivity estimates from the diagonal of the Fisher information matrix (FIM). While EWC pro...
  </details>

- **2026-11-15** — Marcello Sano, Samuele Casagrande, Davide Ferrario et al. — [GNN-Based Deep Reinforcement Learning for Coastal Emergency Response under Extreme Water Levels](http://arxiv.org/abs/2611.20268v1)
  <details><summary>📄 Abstract</summary>
  When a storm surge approaches a coastal town, the emergency plan must be put into action quickly using water-level forecasts, flood extent, road access, vulnerable residents and shelters. Bringing this information together under time pressure is slow and depends on the duty officer's expertise. This paper is one step in a wider research line from data to safe decisions: machine learning to understand the hazard, reinforcement learning and planning to choose actions, large language models (LLMs) ...
  </details>

- **2026-11-15** — Xin Mao, Anqi Dong, Can Chen — [Contraction Analysis and Control of Polynomial Dynamical Systems](http://arxiv.org/abs/2611.20252v1)
  <details><summary>📄 Abstract</summary>
  Contraction analysis has found broad applications in synchronization, tracking, observer design, and nonlinear feedback control. However, establishing contraction conditions for polynomial dynamical systems remains challenging due to their state-dependent Jacobians. In this article, we develop a tensor-based framework for contraction analysis of polynomial dynamical systems by exploiting the structure of orthogonally decomposable (odeco) coefficient tensors. By transforming the dynamics into mod...
  </details>

- **2026-11-15** — Weiyuan Fan, Jacinto Ulloa — [Higher-dimensional homogenization of quasiperiodic elastic materials](http://arxiv.org/abs/2611.20142v1)
  <details><summary>📄 Abstract</summary>
  Quasiperiodic geometrical arrangements, which exhibit long-range order in the absence of periodicity, have attracted interest in the design of composites and mechanical metamaterials. In this context, direct numerical simulations explicitly resolving the quasiperiodic microstructure become prohibitively expensive for macroscopic problems, motivating the development of homogenized continuum models. However, the absence of a periodic unit cell in physical space hinders the use of conventional homo...
  </details>

- **2026-11-15** — Amir Azzam, M. Pilar Casado, Michele Grossi et al. — [Generative Models using Multi-layer Quantum Extreme Learning Machines](http://arxiv.org/abs/2611.20139v1)
  <details><summary>📄 Abstract</summary>
  Quantum reservoir computing (QRC) and the closely related quantum extreme learning machine (QELM) paradigm exploit the complex dynamics of an uncontrolled quantum system for machine learning, offering an alternative to variational quantum algorithms whose training is hindered by barren plateaus and costly circuit optimization. Because the quantum system itself is left fixed, learning reduces to fitting a linear readout of a set of measured observables, and no gradient is ever taken through the q...
  </details>

- **2026-11-15** — Yansong Qu, Zilin Huang, Zihao Sheng et al. — [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](http://arxiv.org/abs/2611.20107v1)
  <details><summary>📄 Abstract</summary>
  An autonomous vehicle must foresee the consequences of its actions, especially in the rare, time-critical situations where crashes happen. A world model offers this foresight, but only within the coverage of its training data, which poses an exploration-exploitation dilemma. Within this coverage a planner can hardly improve on the data, and beyond it the model's errors mislead it. Logs of competent driving rarely contain the failures that would widen the coverage, and agents that learn from inte...
  </details>

- **2026-11-15** — Tingwei Chen, Yunxiao Shi, Zhendong Chu et al. — [DetouR: Plugging Association Routes into Search Agents for Multi-hop Question Answering](http://arxiv.org/abs/2611.19967v1)
  <details><summary>📄 Abstract</summary>
  Search agents answer multi-hop questions by interleaving reasoning with retrieval, deciding at each step what to search next. Existing agents follow semantic routes: they infer what is missing and phrase it as a query, reaching only what the model can name. Yet the decisive page is often one the question never names, frequently just one hyperlink away from evidence already retrieved. Following such association routes reaches more gold pages than semantic search under the same budget. Exploiting ...
  </details>

- **2026-11-15** — Sven Krippendorf, Magdalena Larfors, Zhimei Liu et al. — [Towards a foundation model for Type IIB flux vacua](http://arxiv.org/abs/2611.19950v1)
  <details><summary>📄 Abstract</summary>
  Progress in characterising the Type IIB flux landscape requires scalable methods for constructing flux vacua. In this work, we investigate generative models as a framework for sampling vacua across multiple Calabi-Yau geometries and for directing searches towards specified physical properties. We compare transformers and diffusion models trained to generate quantised fluxes together with approximate values of the complex structure moduli and axio-dilaton. We exploit a staged training procedure c...
  </details>

- **2026-11-15** — Gaotang Li, Lingjie Chen, Chunyuan Deng et al. — [Multi-Branch Transformer](http://arxiv.org/abs/2611.19800v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models are commonly scaled by making their blocks wider or stacking them deeper. In this work, we explore a complementary path: branching, the parallel composition of full Transformer blocks. We introduce the Multi-Branch Transformer (MBT), which processes the input through shared initial layers, executes independently parameterized branches of sequential blocks in parallel, and fuses their outputs before shared final layers. At comparable training compute, we study three MB...
  </details>

- **2026-11-15** — Joshua Joseph George, Hassan Safouhi — [Efficient Recursive Evaluation of Gaussian, Gamma, and Inverse Gaussian Tail Probabilities](http://arxiv.org/abs/2611.19782v1)
  <details><summary>📄 Abstract</summary>
  Accurate computation of tail probabilities motivates efficient high-order implementations of the $G_n^{(1)}$ extrapolation transformation. We derive finite recurrence relations in the transformation order for Gaussian, gamma, and inverse Gaussian tail approximations. The Gaussian and inverse Gaussian numerator and denominator sequences satisfy four-term recurrences, whereas the gamma sequences satisfy a three-term recurrence. The derivation exploits the structure of the underlying differential o...
  </details>

- **2026-11-15** — Deep Shah, Nehal Kathrotia — [Compositional Exploits in Autonomous Coding Agents: Attack Mechanics and Ephemeral Defense](http://arxiv.org/abs/2611.19764v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents (such as Antigravity, Claude Code, Cursor, and OpenHands) rely on third-party tools to inspect files, run commands, and call external APIs. Today's security auditors evaluate these tools almost entirely in isolation: static linters and AST checkers verify that each individual tool contains no malicious code at installation time. In this paper, we show that isolated tool auditing is fundamentally flawed. We expose compositional exploits in autonomous coding agents, an eme...
  </details>

- **2026-11-15** — Youssef Gamal, Mohamad Fakih, Halima Bouzidi et al. — [Found, but Not Fixed : From Software Vulnerability Discovery to Fixes with Iterative LLM Pipelines](http://arxiv.org/abs/2611.19719v1)
  <details><summary>📄 Abstract</summary>
  Software vulnerabilities persist as a critical threat despite the deployment of sophisticated detection tools and AI assistants. While detection has advanced, the subsequent code repair phase remains a primary bottleneck; manual intervention is inherently slow, costly, and prone to introducing secondary regressions and issues. In this paper, we investigate whether an iterative, LLM-based pipeline can provide a robust solution for the automated repair of vulnerable functions in real-world code. W...
  </details>

- **2026-11-14** — Jinrui Fang, Runhan Chen, Yining Wu et al. — [ROUNDS: Source-Framed Diagnostic Revision after Multi-Turn Clinical Evidence](http://arxiv.org/abs/2611.19636v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve high scores on medical benchmarks, but does this performance translate into reliable diagnosis as a conversation unfolds? In diagnostic conversations, users can provide clinical findings across multiple turns, ask for a diagnosis without supplying answer options, and introduce opinions from others. Models must therefore form diagnoses from the available evidence and decide how to respond to subsequent advice. We introduce ROUNDS, a framework that evaluates th...
  </details>

- **2026-11-14** — Mario Edoardo Pandolfo, Kyriakos Stylianopoulos, George C. Alexandropoulos et al. — [Over-the-Air Semantic Alignment via Dual Stacked Intelligent Metasurfaces](http://arxiv.org/abs/2611.19515v1)
  <details><summary>📄 Abstract</summary>
  Semantic communications enable task-oriented information exchange, but suffer from latent-space mismatch when transmitter and receiver employ heterogeneous machine learning models. Existing semantic alignment methods rely on digital processing, introducing computational and latency overhead. This paper proposes a dual stacked intelligent metasurfaces (dual-SIM) architecture that performs semantic alignment entirely in the wave domain. By jointly exploiting programmable metasurfaces at both ends ...
  </details>

- **2026-11-14** — Tianyi Zhao, Qihao Xu, Jiawen Xi et al. — [Beyond Paired Inputs: Learning to Leverage RGB-T Cross-Modal Relations in Multimodal Large Language Models](http://arxiv.org/abs/2611.19493v1)
  <details><summary>📄 Abstract</summary>
  RGB and thermal infrared (TIR) sensors provide complementary observations, yet their distinct sensing characteristics make effective cross-modal coordination challenging. Although existing multimodal large language models (MLLMs) can process paired RGB-T inputs, they often fail to translate cross-modal relations into effective task-specific decisions, leaving the potential of these relations to improve task performance and robustness largely untapped. Motivated by this observation, we introduce ...
  </details>

- **2026-11-13** — Yimin Gao, Liangtao Dai, Melika Morsali et al. — [Mutable Inference: Architecting LLM Accelerators for Inference-Time Learning](http://arxiv.org/abs/2611.18523v1)
  <details><summary>📄 Abstract</summary>
  Long-context LLMs must retain growing histories, but full attention makes each new token increasingly expensive. Inference-time learning (ITL) offers another approach. The model keeps training on the context during inference, retaining what it learns in its weights. Recent work shows that ITL can match full-context attention quality while attending only to a recent fixed-size window. This bounds attention costs but adds Learning (backward computation and weight updates) alongside Prediction (the...
  </details>

- **2026-11-13** — Qiufeng Li, Sizhe Tang, Quan Cheng et al. — [OpenLayout: An Open and Agentic-Driven Platform for Holistic VLSI Physical Design and Benchmarking](http://arxiv.org/abs/2611.18517v1)
  <details><summary>📄 Abstract</summary>
  Physical design automation of very large-scale integrated circuits (VLSI) has made significant strides, progressing from single-stage placement and routing toward increasingly integrated full-flow implementation. Yet, existing approaches struggle with the vast design space optimization (DSO) arising from diverse technology nodes, circuit designs, and varied constraints. The substantial runtime of physical-design tools further exacerbates this challenge, leaving industrial workflows heavily depen...
  </details>

- **2026-11-13** — Dayoon Ko, Yichuan Wang, Soyeong Jeong et al. — [StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval](http://arxiv.org/abs/2611.18516v1)
  <details><summary>📄 Abstract</summary>
  Screen history can serve as searchable visual memory for people and agents, but unlike an offline corpus, it must be encoded and indexed as each screenshot arrives. OCR-based indexing is fast but loses visual information; visual encoding takes over two seconds. Yet screens change incrementally: most pixels repeat within and across screenshots. This raises a question: do visual encoders need to recompute their representations from scratch for every new screenshot? We present StreamEmbed, a system...
  </details>

- **2026-11-13** — Umut Demir, Torbjørn Cunis, Aamir Ahmad et al. — [Reinforcement Learning for Null-Space Exploitation in Pseudo-Inverse Control Allocation](http://arxiv.org/abs/2611.18364v1)
  <details><summary>📄 Abstract</summary>
  Pseudo-inverse methods are widely used to solve control allocation problems for overactuated aircraft with redundant control effectors. These methods reliably satisfy the primary command tracking objective, while the remaining null-space degrees of freedom are in principle available for secondary objectives such as drag reduction or actuator wear balancing. However, exploiting this freedom in practice requires hand-tuned weighting matrices or a priori preferred deflections that are difficult to ...
  </details>

- **2026-11-13** — Andrea Marelli, Alessandro Ardenghi, Giacomo Boracchi et al. — [Unlocking Cross-Attention in Label-Scarce Regimes: A Weakly Supervised Approach for Video Semantic Segmentation](http://arxiv.org/abs/2611.18324v1)
  <details><summary>📄 Abstract</summary>
  Weakly Supervised Video Semantic Segmentation (WS-VSS) aims to learn temporally consistent semantic object masks in videos using only video-level labels. While fully supervised models successfully learn temporal relationships by means of cross-attention, training these temporal weights under weak supervision is unstable and even pushes the model below its single-frame baseline. Therefore, existing WS-VSS methods exploit temporal consistency by relying on external priors, such as optical flow. Un...
  </details>

- **2026-11-13** — Meng Fang, Lebin Chen, Jun-Rong Chen et al. — [Linear Dynamic Range Extension for Rydberg Atomic Receiver via Band-Limited Reconstruction](http://arxiv.org/abs/2611.18181v1)
  <details><summary>📄 Abstract</summary>
  Rydberg-atom receiver offers a promising approach to radio-frequency (RF) signal reception in wireless communication and sensing systems, combining high sensitivity with the potential for broad frequency coverage. However, the limited linear dynamic range (LDR) of the atomic system causes nonlinear distortion at high input signal levels, thereby restricting the receiver's effective linear input range. To address this issue, we analyze the mechanisms underlying nonlinear distortion in Rydberg ato...
  </details>

- **2026-11-13** — Gayan H. Pathirage, Florent Imbert, Denis Coquenet et al. — [DRA-HTR: Disentangling Representation and Adaptation for Handwritten Text Recognition](http://arxiv.org/abs/2611.18143v1)
  <details><summary>📄 Abstract</summary>
  Handwritten text recognition (HTR), particularly when applied to historical documents, remains challenging due to the scarcity of annotated data and the substantial domain shifts caused by variations in handwriting styles, document degradation, acquisition conditions, and linguistic characteristics. While large amounts of unlabeled target-domain data are often available, effectively exploiting them requires adaptation strategies tailored to the specific requirements of HTR. We propose DRA-HTR, a...
  </details>

- **2026-11-13** — Xilong Wang, Xiaoxing Chen, Neil Gong — [Securing Multi-Agent Systems by Design](http://arxiv.org/abs/2611.17883v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems solve complex tasks by decomposing them into subtasks, delegating the subtasks to agents, and aggregating the agents' responses using an aggregation rule. Malicious agents can manipulate the final solution by providing malicious responses to their assigned subtasks. In this paper, we first propose response manipulation attacks (ReMA), which iteratively optimize malicious responses to maximize attack effectiveness. Specifically, we formulate untargeted and targeted attacks as ...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

- **2026-11-16** — Mohammed Fackruddin Tusher, Muhammad Iqbal Hossain — [Replay-Augmented Regularisation for Class-Incremental Network Intrusion Detection: A Three-Dataset Evaluation of EWC and LwF](http://arxiv.org/abs/2611.20498v1)
  <details><summary>📄 Abstract</summary>
  As new attack categories emerge, network intrusion detection models need to be updated; however, when fine-tuned sequentially on new classes, previous classes are forgotten, resulting in catastrophic for- getting. The three public datasets we use are UNSW-NB15, ToN-IoT and CIC-IDS2017, and for these datasets, our class-incremental intrusion detection system is built using a CNN with one-dimensional (1D) archi- tecture trained over nine sequential tasks, each of which introduces one attack catego...
  </details>

- **2026-11-16** — Blas Eugenio Vicco Zarate, Miguel Hernán Vicco — [Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent](http://arxiv.org/abs/2611.21598v1)
  <details><summary>📄 Abstract</summary>
  Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evolutionary search can provide a reusable memory when combined with environment detection and failure-driven search. The Evolutionary Neuroplastic Agent (ENA) evolves small neural networks without gradients, archives selected policies by detected dynamic regime, and retrieves them through Bayesian pol...
  </details>

- **2026-11-16** — Arunkumar V — [Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied Requests](http://arxiv.org/abs/2611.21545v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly write the explanations people receive when a rule system denies their request. If several rules deny the request independently, an explanation can name a true reason and still leave the person denied after they fix it. We call the missing property recourse validity: changing what the explanation cites, without changing what was asked for, can flip the decision. We compute it exactly, and a hitting-set argument predicts from the policy alone when a correct reason fail...
  </details>

- **2026-11-16** — Jiazheng Zhang, Shouwei Li, Yutian Deng et al. — [Incentive Alignment for Electricity Data Assets in China: A Blockchain-Enabled Contribution-Credit Framework](http://arxiv.org/abs/2611.21533v1)
  <details><summary>📄 Abstract</summary>
  Modern electricity markets increasingly rely on reported operational contributions to allocate incentives, recognise cooperation, and coordinate activities across multiple organisations. However, supporting evidence for many reported contributions becomes available only after subsequent metering, dispatch, settlement, or auditing processes, making it difficult to reward genuine contributions while discouraging strategic over-reporting. Existing approaches largely address data sharing, performanc...
  </details>

- **2026-11-16** — Charles Xiao — [Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety](http://arxiv.org/abs/2611.21520v1)
  <details><summary>📄 Abstract</summary>
  When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reuse can produce high textual overlap with the source, so text-similarity guardrails that attempt to flag the former risk conflating these two cases. We test this distinction using DonkeyRail, a public classifier combining BLEU, ROUGE-L, and METEOR features, deployed in a controlled three-agent email r...
  </details>

- **2026-11-16** — Jinzhao Li, Yuan Xu, Jinxuan Wu et al. — [ALIVE: Making Streaming Video Models Interactive](http://arxiv.org/abs/2611.21366v1)
  <details><summary>📄 Abstract</summary>
  Streaming video LLMs can continuously observe the world, yet often handle user requests in isolation. We introduce ALIVE, an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interaction. We construct ALIVE-SFT-288K and ALIVE-RL-3K for two-stage training. Contrastive supervised fine-tuning teaches when and how to respond, while reinforcement learning with Behavior-Aligned Credit Assignment (BACA) combines trajectory-level and loc...
  </details>

- **2026-11-16** — Paul-Andrei Sava, Alexander Küchler, Daniel Kowatsch et al. — [TRIAGE-CPG: A Cross-Model Study of Budgeted Static Malware Triage with Large Language Models](http://arxiv.org/abs/2611.21331v1)
  <details><summary>📄 Abstract</summary>
  When triaging unknown binaries, security analysts must decide which samples to clear as benign, flag as malicious, or escalate for deeper analysis. Large Language Models (LLMs) could support these decisions by interpreting decompiled code, but a binary can contain hundreds or thousands of functions, making exhaustive LLM analysis impractical. We study how current LLMs behave when static triage is formulated as budgeted evidence acquisition: which functions they inspect and how they trade off ben...
  </details>

- **2026-11-16** — Syed Hafiz Bin Salim Alsree, Stephen Roberts, Stefan Zohren — [Wavelet-Energy-Driven Dynamic Patching for Time Series Forecasting](http://arxiv.org/abs/2611.21319v1)
  <details><summary>📄 Abstract</summary>
  Patch-based transformers tokenise a time series into fixed-size, uniform windows, which commits the model to a single temporal resolution even though real signals are multi-scale. The discrete wavelet transform (DWT) is a natural alternative because it decomposes a signal across scales. A growing body of work makes the wavelet filter learnable, on the assumption that a more flexible wavelet forecasts better. That assumption has rarely been tested in isolation, because a single reported improveme...
  </details>

- **2026-11-16** — Hua Zhang, Min Jiang — [Linglong Agent Service: A Runtime for Centralized Agent Reasoning and Distributed Execution](http://arxiv.org/abs/2611.21129v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can use remote tools and cloud sandboxes, but integrating reasoning, session state, and heterogeneous execution sites remains a runtime design problem. We present Linglong Agent Service (agentsvc), a self-hosted HTTP service and embeddable Python runtime that treats execution site as a configurable dimension alongside model, tools, and context. A parent service retains inference orchestration, tool descriptions, and conversation history; each inference request selects one child enviro...
  </details>

- **2026-11-16** — Fabio Picariello, Salvatore Cipolla, Susanna Bonura et al. — [GRACE: Parallel Best-of-N Multi-Agent Analysis of Closed-Form Questions over Dataframes with Guardrail Selection and Adaptive Retry](http://arxiv.org/abs/2611.20983v1)
  <details><summary>📄 Abstract</summary>
  LLM agents answer closed-form questions over a tabular dataframe by writing and executing Python, almost always as a single rollout: one interpretation, one script, one result, accepted without comparison. The few pipelines that produce several candidates reconcile them by answer-agreement voting, which needs a single comparable scalar and always returns one, even when every candidate is wrong. We present GRACE (Generative, Ranked, Adaptive Code Ensemble), a production-oriented pipeline that ins...
  </details>

- **2026-11-16** — Subham Kundu — [Same Fix, Different Weights: Replicating Weight-Space Programming with Claude](http://arxiv.org/abs/2611.20953v1)
  <details><summary>📄 Abstract</summary>
  Takehi et al. (2026) report that GPT-6 Astra, given the weights of small neural networks as text, can say what they were trained to do, repair them, and write new ones without training. I re-ran the core of that study with Claude Opus 5.5 in ten pre-registered experiments, with untrained-network and permutation controls and hand audits of every sandboxed code cell. Reading was mixed: Claude named 3 of 4 Atari games from policy weights and found the measured copying heads in 15/15 character-LM ru...
  </details>

- **2026-11-16** — Daksh Bathla — [Navital Gym: Rule-Graded Agent Environments for Indian Workflows](http://arxiv.org/abs/2611.20924v1)
  <details><summary>📄 Abstract</summary>
  AI agents are being deployed on Indian workflows such as payments, tax, forms, travel and customer support in Hindi and Hinglish. Public agent evaluations rarely cover these workflows, and many score with another language model. We present Navital Gym, a set of six open environments with 321 public tasks in five task families: trip planning, UPI payments and disputes, GST invoicing and returns, form filling (including a multi-document split) and customer support in Hindi, Hinglish and three expe...
  </details>

- **2026-11-16** — Xue Yang, Haonan Cai, Xinyu Hang et al. — [SciWorldBench: Do Video World Models Really Understand Scientific Experiments?](http://arxiv.org/abs/2611.20899v1)
  <details><summary>📄 Abstract</summary>
  While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the underlying principles remains a critical challenge. Existing benchmarks typically evaluate video samples in isolation, making it difficult to expose models that simply fit superficial visual priors. In scientific experiments, a small change in one condition produces a markedly different outcome even when the rest of the s...
  </details>

- **2026-11-16** — Zheng Wang, Yuang Liu, Sachith Abeywickrama et al. — [From Recursion to Convolution: Parallel Self-Improvement for Multi-Agent Systems](http://arxiv.org/abs/2611.20891v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent self-improvement enables agents to improve through interaction and feedback. However, sequential dependencies across agents and refinement rounds can propagate errors, increase computational costs, and limit parallelism. Moreover, refining individual features or agents in isolation can overlook their dependencies and restrict collective coordination. To address these challenges, we propose ConvRSI, a framework for parallelizing multi-agent self-improvement through convolution. ConvRS...
  </details>

- **2026-11-16** — Tom A. Lamb, Philip H. S. Torr, Tim G. J. Rudner — [Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges](http://arxiv.org/abs/2611.20818v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) judges are increasingly used to monitor the outputs of LLM-based AI agents, yet formal guarantees on the reliability of these judges remain largely absent, limiting confidence in their use for safety-critical oversight. We consider certifying such a judge and define its risk over safety classifications of prompt--response pairs drawn from a deployed generator. We apply a PAC-Bayes framework to this setting, refining existing compression-based methodology with the use o...
  </details>

- **2026-11-16** — Pier Mattia Basciano, Giovanni Farina, Salvatore Monteleone — [A First Look at System One Decision Models for Malware Detection](http://arxiv.org/abs/2611.20699v1)
  <details><summary>📄 Abstract</summary>
  Malware detection needs scores calibrated at a fixed false positive rate (FPR) and decisions an analyst can read: feature-based detectors give the first, large language models (LLMs) on decompiled code the second, through generated text of uncalibrated confidence. System One decision models answer a typed question about a text with a probability over its declared answers in one forward pass. We present the first evaluation of these models for Windows Portable Executable malware detection, analyz...
  </details>

- **2026-11-16** — Senquan Wang, Hui Fang, Haoran Nan et al. — [BiGSyn: A Bi-Level Heterogeneous Graph Contrastive Learning Framework for Interpretable Drug Synergy Prediction](http://arxiv.org/abs/2611.20603v1)
  <details><summary>📄 Abstract</summary>
  Drug combination therapy has become a mainstream of modern medicine, with the potential to enhance efficacy, reduce toxicity, and overcome drug resistance. However, identifying synergistic drug combinations remains challenging, as it requires modeling complex interactions across multiple biological scales---from atom-level molecular structures to entity-level relations in biological networks. Existing approaches typically model these levels in isolation, overlooking complementary signals and lon...
  </details>

- **2026-11-16** — Dongjia Zhao, Yuchen Ma, Chunsheng Shi et al. — [IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text Queries at Xiaohongshu](http://arxiv.org/abs/2611.20448v1)
  <details><summary>📄 Abstract</summary>
  Multimodal search with image-text queries helps users find notes in user-generated content (UGC) communities and serves as a key search tool for multimodal search agents. For such queries, query-note relevance depends on the user's retrieval intent and cannot be determined by visual or topical similarity alone. Simply reranking visual search results cannot fully address this challenge, as notes relevant to the user's intent may be missing from the initial candidate set. This motivates explicit i...
  </details>

- **2026-11-16** — Siran Peng, Tianshuo Zhang, Yibo Xue et al. — [FaceJev: Direct Visual Decisions for Face Forgery Detection](http://arxiv.org/abs/2611.21604v1)
  <details><summary>📄 Abstract</summary>
  Face forgery detection methods often perform well on seen manipulations but generalize poorly to unseen ones. Multimodal Large Language Models (MLLMs) can recognize facial parts and assess their visual plausibility. Existing MLLM-based methods typically express these judgments through textual explanations, but seldom treat individual part decisions as explicit learning targets. We present FaceJev, an MLLM-based method for face forgery detection through direct visual decisions. Following the Jev ...
  </details>

- **2026-11-16** — Jinwei Hu, Qisong He, Xinmiao Huang et al. — [Language-model agents' beliefs can be manipulated via truthful evidence in open channel](http://arxiv.org/abs/2611.21235v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents' beliefs can be manipulated through open channels such as social media, even when the information they receive is truthful. When agents fill gaps between fragments with self-induced relationships, they may accept those relationships as established facts and pass the resulting rumours to others. Drawing on cognitive theory of narrative understanding and film theory of montage, we introduce Generative Montage to operationalize this failure, termed narrative overfitting, by co...
  </details>

- **2026-11-16** — Korede R. Bishi, Dominic Okonkwo, Adetayo Okunoye — [Severe but Harmless: Stress-Testing Shift Severity for Frozen Time-Series Forecasters](http://arxiv.org/abs/2611.21562v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot time-series foundation models (TSFMs) have become attractive alternatives to task-specific models because they handle diverse downstream tasks, including anomaly detection and forecasting, without per-series training. However, time-series data undergo distribution shifts, and the dissimilarity between two regimes is commonly scored with statistical measures such as Wasserstein-1, where a higher score is read as a more severe shift. In systematic experiments using three established seve...
  </details>

- **2026-11-16** — Dumindu Samaraweera, Prashant Shekhar — [Detection-Efficient Watermarking for Vision--Language Agents via Risk-Constrained Strength Allocation](http://arxiv.org/abs/2611.21488v1)
  <details><summary>📄 Abstract</summary>
  Vision--language agents generate descriptions, decisions, and instructions that may be reused by users, downstream agents, and automated workflows, creating a need for provenance mechanisms that support content authenticity and post-deployment auditing without unnecessarily degrading response quality. We present a risk-aware semantic watermarking framework that combines predictive uncertainty with a zero-shot multimodal relevance-risk proxy to allocate watermark strength during decoding. A singl...
  </details>

- **2026-11-16** — Yipeng Du, Yuxi Li, Ying Zhang et al. — [WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection](http://arxiv.org/abs/2611.21373v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does not directly improve the forensic capabilities of fixed experts. We introduce WeV...
  </details>

- **2026-11-16** — Iva Ewert, Felix Putze, Marvin Borsdorf et al. — [Towards Microphone-Invariant Speech Representations for Transformer-Based Voice Disorder Detection](http://arxiv.org/abs/2611.21140v1)
  <details><summary>📄 Abstract</summary>
  Automatic voice disorder detection from speech offers strong potential for early diagnosis and continuous disease monitoring. While models based on pre-trained transformers have improved detection performance, their robustness to microphone variation remains underexplored, particularly for consumer-grade devices. To the best of our knowledge, we present the first study of microphone mismatch in transformer-based binary voice disorder detection across 20 smartphone microphones. While most mismatc...
  </details>

- **2026-11-16** — Giacomo D'Amicantonio — [Region-VAD: Video Anomaly Localization and Detection via Region Selection](http://arxiv.org/abs/2611.21132v1)
  <details><summary>📄 Abstract</summary>
  Anomalies are local events, yet weakly supervised video anomaly detection scores them globally. Most methods pool an entire frame into a single vector, rank frames by that vector, and derive a location afterwards as a saliency map of the score. Full-frame pooling mixes the anomaly with its background, so a detector can reach competitive benchmark scores from scene context without being able to show where in the scene the anomaly occurs. We introduce Region-VAD, which first selects a region and t...
  </details>

- **2026-11-16** — Giacomom D'Amicantonio, Egor Bondarev — [How to Explain your Unexplainable Video Anomaly Detector](http://arxiv.org/abs/2611.21131v1)
  <details><summary>📄 Abstract</summary>
  Weakly-supervised Video Anomaly Detection (VAD) models assign anomaly scores from high-dimensional features, and their predictions remain unexplained. Saliency maps show where a model looks but not what it relies on, and the descriptions produced by Vision-Language Models (VLMs) are generated by branches that the anomaly score never reads. To address this faithfulness gap, we propose \textbf{Explain The Unexplainable (ETU)}, a classifier-agnostic framework that audits frozen VAD models through c...
  </details>

- **2026-11-16** — Zhixiang Guo, Xinming Wu, Yimin Dou et al. — [A Seismic Foundation Model for Dense Feature Extraction](http://arxiv.org/abs/2611.20745v1)
  <details><summary>📄 Abstract</summary>
  Deep-learning-based seismic interpretation is constrained by scarce high-quality annotations, and most existing models are trained separately for individual tasks. We present SeisDFE, a 7B-parameter seismic foundation model for dense feature extraction, pretrained on 5.34 million 2D images derived from more than 500 seismic volumes. A three-stage pretraining strategy, combining discriminative self-supervised learning, Gram feature anchoring, and multi-resolution adaptation, improves feature disc...
  </details>

- **2026-11-15** — Nick Ryan, Peter A. Devine, Ben Sirb et al. — [Microfitting: Continual Learning via Cached Test-Time Training](http://arxiv.org/abs/2611.20258v1)
  <details><summary>📄 Abstract</summary>
  Continual learning is a promising approach to specialize language models to an organization's private data. However, current methods exhibit a number of drawbacks including catastrophic forgetting, where new training updates overwrite prior knowledge. We present microfitting, which trains and caches a small adapter for each document. Each adapter is trained once, offline, on synthetic questions targeted at demonstrated base-model shortcomings and reused whenever that document is queried. This me...
  </details>

- **2026-11-15** — Moshe Kimhi, Idan Kligvasser, Yotam Intrator et al. — [EvoMem3D: Adaptive-Depth Temporal Representation Memory for Multi-Camera 3D Detection](http://arxiv.org/abs/2611.20241v1)
  <details><summary>📄 Abstract</summary>
  Modern multi-camera 3D detectors increasingly rely on large Vision Transformer (ViT) image encoders, making repeated full-depth encoding a dominant inference cost even though adjacent driving frames are highly redundant. We present EvoMem3D, an adaptive-depth temporal framework that caches the most recent full-depth detector-interface appearance representation as a read-only anchor and combines it with policy-selected partial features from the current frame. A lightweight pre-encoding controller...
  </details>

- **2026-11-15** — Mayank Mayank, Bharanidhar Duraisamy, Rohit Mohan et al. — [Radar Panoptic Transformer: Semantic-Guided Mask Queries for Dynamic Scene Understanding](http://arxiv.org/abs/2611.20203v1)
  <details><summary>📄 Abstract</summary>
  Automotive radar provides long-range sensing and direct Doppler velocity measurements, but its sparse and non-uniformly sampled point clouds pose significant challenges for panoptic segmentation. Dynamic objects often yield only a few detections amid a dominant static background, providing limiting the geometric cues for separating object instances. We propose \emph{Radar Panoptic Transformer (RPT)}, an end-to-end point-based network that incorporates radar-adaptive feature extraction with seman...
  </details>

- **2026-11-15** — Luciano Bozzi, Christian Celidonio, Umberto Nuzzi et al. — [Cyber-Secure Wearable, Ultra-Low-Power Networked Sensors for Soldier Health Monitoring: Insights from the CAPSARII project](http://arxiv.org/abs/2611.20187v1)
  <details><summary>📄 Abstract</summary>
  The CAPSARII project advances a cyber-secure, ultra-low-power wearable platform and Internet of Battlefield Things (IoBT) framework to support real-time monitoring of military personnel and data-driven decision support. The architecture integrates smart-textile sensing, a body/squad area mesh, edge-deployed AI on secure RISC-V microcontrollers, and cloud/federated analytics for cross-mission learning and comparative studies. Two representative use cases--pilot fatigue and warfighters operating i...
  </details>

- **2026-11-15** — Kacper Rutkowski, Radosław Poleski — [Faster $χ^2$ periodogram: Accelerating linear algebra with fast Toeplitz solvers](http://arxiv.org/abs/2611.20300v1)
  <details><summary>📄 Abstract</summary>
  In recent years, the traditional Lomb--Scargle periodogram, relying on least-squares fitting of a sinusoid to data with a known mean, has been mostly superseded by its floating-mean extension---the generalized Lomb--Scargle periodogram---due to the superior robustness and accuracy of the latter. While further generalization to higher-degree trigonometric polynomials (known as the multiharmonic analysis of variance and the fast $χ^2$ periodogram) has been known for decades, its usage remains rela...
  </details>

- **2026-11-14** —  Lokesh, Pramukto Mandal, Somanshu Juneja et al. — [StyleJudge: A Human-Validated, In-Context-Learning Vision-Language Evaluator for Artistic Style Transfer](http://arxiv.org/abs/2611.19475v1)
  <details><summary>📄 Abstract</summary>
  Automatic evaluation of artistic style transfer remains an open problem: existing metrics score an image pair in isolation, without seeing an example of the intended style transformation, and correlate poorly with human judgment. We introduce StyleJudge, a compact vision-language evaluator conditioned on a small set of reference source-to-stylized pairs before scoring a query pair, mirroring how a human rater calibrates to a style before judging a candidate. On a human-annotated benchmark of 878...
  </details>

- **2026-11-14** — Truong Thinh Nguyen, Hai Phong Nguyen, Truong Thanh Hung Nguyen et al. — [Lesion-Aware Explainable AI for Diabetic Retinopathy Grading from Fundus Images](http://arxiv.org/abs/2611.19550v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc explanations of deep-learning models for diabetic retinopathy (DR) grading are difficult to trust because different attribution methods highlight different retinal regions for the same image, and a visually plausible heatmap does not show that the highlighted pixels drive the prediction. We propose the Consensus-Calibrated Explanation Map (CCEM), which fuses Grad-CAM++, Ada-SISE, and SmoothGrad Integrated Gradients (SG-IG) using image-specific weights derived from annotation-free reliab...
  </details>

- **2026-11-14** — Pujun Zheng, Wanying Ren, Guoxiu He — [Program Distillation: Transferring LLM Capability from System 2 to System 0](http://arxiv.org/abs/2611.19461v1)
  <details><summary>📄 Abstract</summary>
  Recent studies leverage large language models (LLMs) to construct executable programs through environment interaction, feedback analysis, and code revision. However, prior work has mainly treated LLMs as optimizers, overlooking their ability to transfer knowledge across system levels. We propose Program Distillation (PD), a framework that formalizes the transfer of abilities from System 2 to System 0. During learning, the LLM provides task knowledge and draft strategies; at deployment, a student...
  </details>

- **2026-11-13** — Anna V. Guglielmi, Linda Senigagliesi, Marco Baldi et al. — [Game-Theoretic Analysis of RIS-Assisted Challenge-Response PLA - Part II: Partial Channel Knowledge](http://arxiv.org/abs/2611.17907v1)
  <details><summary>📄 Abstract</summary>
  We consider a physical layer authentication scenario in which a legitimate user (Alice) communicates with an authenticator (Bob) through a reconfigurable intelligent surface (RIS), controlled by Bob. An attacker (Trudy) aims to impersonate Alice by suitably precoding her messages and still transmitting them through the RIS. This two-part study analyzes this attack-defense interaction between Bob and Trudy under perfect (Part I) and partial (Part II) channel knowledge by all the agents. Part I fo...
  </details>

- **2026-11-13** — Anh Tu Ngo, Anupam Chattopadhyay — [Antidistillation is Cheap: Lightweight Distillation-Resistance via Stylistic Corruption](http://arxiv.org/abs/2611.17772v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models. In commercial deployment where frontier models are restricted behind black-box APIs, sequence-level distillation remains a potent vector for competitors to clone proprietary capabilities at a fraction of the development cost. Existing defenses mostly rely on surrogate models to manipulate next-token sampling, which increases compu...
  </details>

- **2026-11-13** — Aayush Marasini, Barsat Khadka, Nick Rahimi — [WeightBench: Evaluating Language Models as Weight-Space Programmers](http://arxiv.org/abs/2611.18553v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that large language models (LLMs) can operate directly on the parameters of other neural networks. They can read what a network was trained to do, fix a network that fails, and write working networks from scratch, all without gradient descent. This capability has been termed Weight-Space Programming (WSP). Exploring this new paradigm systematically requires a robust benchmark. We introduce WEIGHTBENCH, a benchmark that evaluates LLMs of increasing capability on 42 WSP tasks acr...
  </details>

- **2026-11-13** — Thomas Brennan, Andrew W. Lo, Chaoyi Zhao — [Alignment by Socialization: Learning Tradeoffs Under Selection](http://arxiv.org/abs/2611.18531v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) agents are expected to complete tasks while following rules of conduct, but these objectives can conflict. We study how evolutionary selection shapes an agent's choices between them, and whether experience can make those choices reflect human judgments and withstand subsequent pressures. In our model, copies of an agent face a common uncertain reward state, and only those taking the rewarded action reproduce. We show that long-run growth is maximized when each action...
  </details>

- **2026-11-13** — Guangxi Feng, Philip Yasskin, Wei Yan — [Toward On-Device Markerless 6DoF Tracking of a Physical Manipulative on a Mixed-Reality Headset: A Preliminary Study](http://arxiv.org/abs/2611.18438v1)
  <details><summary>📄 Abstract</summary>
  AR-Classroom uses physical models and virtual overlays to help learners explore spatial transformations. To align these overlays on a standalone headset, we developed a markerless six-degree-of-freedom(6DoF) tracker for a LEGO airplane on the Meta Quest 3. A compact YOLO model trained on synthetic Unity renders predicts 20 keypoints from dynamic RGB crops resized to 128 by 128 pixels. A perspective-n-point solver estimates the airplane's pose from these predictions and the corresponding 3D landm...
  </details>

- **2026-11-13** — Hoang Tran Vuong, Linh Ngo Van, Dang Nguyen et al. — [f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models](http://arxiv.org/abs/2611.18370v1)
  <details><summary>📄 Abstract</summary>
  Anomaly detection in tabular data poses significant challenges due to heterogeneous feature types-mixing numerical, categorical, and textual attributes, which complicate learning meaningful representations of normality. Recent work has applied large language models (LLMs) to this problem by serializing table rows as text sequences, yet these approaches rely on one-shot supervised fine-tuning that offers limited signal to tighten the model's description of normality. We propose DiSPaT, a self-pla...
  </details>

- **2026-11-13** — Rui Rua, Hailemariam Mersha, Joao Paulo Fernandes et al. — [PerfArena: Ranking LLMs by Code Performance](http://arxiv.org/abs/2611.18030v1)
  <details><summary>📄 Abstract</summary>
  Industry now relies on LLMs to write a large share of production code. Although that code is mostly, but not always, correct, correctness alone does not determine whether it is fit for repeated and extensive use, which depends on what the code costs in time, memory and energy. Most code-generation benchmarks nonetheless evaluate correctness in isolation, and most performance-oriented benchmarks cover few languages and rarely measure energy consumption. To address this gap, we present PERFARENA, ...
  </details>

- **2026-11-13** — Jisoo Kim, Youngwoo Seo, Seonghoon Jeong — [Beyond Bot Labels: Retrospective Consequence-Grounded Ranking of Attributed Cache Harm in E-Commerce Logs](http://arxiv.org/abs/2611.18027v1)
  <details><summary>📄 Abstract</summary>
  Web caches reduce origin load and latency, but automated traffic can either warm them or evict objects shoppers reuse, lowering the cache hit ratio (CHR). Existing bot defenses generally infer automation from User-Agent (UA) strings or behavior rather than identify sessions that impose cross-session cache harm. We instead formulate the task as ranking sessions by eviction damage and propose consequence-grounded session ranking. A single chronological replay attributes each eviction-induced miss ...
  </details>

- **2026-11-13** — Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù et al. — [WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents](http://arxiv.org/abs/2611.17955v1)
  <details><summary>📄 Abstract</summary>
  Web agents powered by large language and vision-language models are increasingly applied to realistic browser work that spans heterogeneous applications, multimodal content, and stateful workflows. However, existing reproducible web-agent benchmarks cover only a small number of web applications drawn from a few software categories, and restrict modality to text and vision. Live benchmarks broaden site coverage but sacrifice reproducibility, since pages and data drift between runs. Moreover, exis...
  </details>

- **2026-11-13** — Mohammad Arman Ullah, Asif Ahmed — [RuralShield: Super Intelligence-Assisted Security Triage and Serverless Infrastructure for Resource-Constrained Healthcare](http://arxiv.org/abs/2611.17887v1)
  <details><summary>📄 Abstract</summary>
  Resource-constrained healthcare providers must connect cloud security controls to an operational response process. Introducing language-model assessments adds an authorization problem: a recommendation must be converted into a permitted action against a specific resource. RuralShield combines a configurable serverless application foundation with structured model assessment, deterministic routing, and human-approved containment. Its design separates workload access, assessment validation, and act...
  </details>

- **2026-11-13** — Yuxiang Lai, Jiashuo Zhang, Liang Zhao et al. — [Causally Constrained and Uncertainty-Aware Cardiopulmonary Risk Prediction](http://arxiv.org/abs/2611.17819v1)
  <details><summary>📄 Abstract</summary>
  Routine chest computed tomography (CT) captures pulmonary, cardiac, and vascular phenotypes that jointly stratify lung cancer and cardiovascular disease, the two leading causes of death in lung-screening populations. Yet clinical risk calculators evaluate each disease in isolation and omit CT findings, whereas unconstrained machine learning overfits small hospital cohorts, learns treatment- and illness-confounded risk directions, and conceals uncertainty when patient records are incomplete. Here...
  </details>

- **2026-11-13** — Ivana Ragusa, Lorenzo Guiducci, Filippo Cavallo — [From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration](http://arxiv.org/abs/2611.18484v1)
  <details><summary>📄 Abstract</summary>
  AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action ...
  </details>

- **2026-11-13** — Enis Chenchene, Anil S. Baslamisli, Paolo Braca — [Detection and Classification in Latent Spaces: High-Dimensional Analysis and Validation](http://arxiv.org/abs/2611.18164v1)
  <details><summary>📄 Abstract</summary>
  Foundation models produce high-dimensional latent representations in which suitably designed statistical decision rules can be effective yet analytically tractable. We study such detectors in the high-dimensional regime, where latent dimension and training sample size grow proportionally. For linear and quadratic statistics, we derive explicit large-deviation characterizations of false-alarm and miss-detection performance under the Neyman-Pearson paradigm, and show how the binary analysis extend...
  </details>

- **2026-11-13** — Zailong Tian — [Contagious Fingerprints: When LLMs Inherit Another Model's Identity](http://arxiv.org/abs/2611.18104v1)
  <details><summary>📄 Abstract</summary>
  The fingerprint by which a classifier recognizes the LLM behind a text is usually treated as a fixed property of the model. We show that it is contagious: a model that continues a conversation begun by another model inherits that model's fingerprint. This undermines audits of API relays, which can serve the first turns of a conversation with the model a customer pays for and silently hand the rest to a cheaper one. After such a handoff, detection of the substitute by a text classifier drops from...
  </details>

- **2026-11-13** — Congren Dai, Zhancheng Guo, Danni Zhao et al. — [OmniScore-Bench: Evaluating Vision-Language Models on Musical Score Reading](http://arxiv.org/abs/2611.17870v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can answer questions about musical scores, but their ability to recognise notation, recover its structure and interpret its musical meaning requires separate evaluation. Existing optical music recognition (OMR) resources establish detection and transcription measurements; a transcription score alone leaves the strengths and bottlenecks of a VLM score reader unresolved. We introduce OmniScore-Bench, an evaluation of OMR capabilities in VLMs through 3,000 questions sp...
  </details>

- **2026-11-13** — Sau Lai Yip, Yue Pang, Shiwen Wu et al. — [Bridge: Database-Grounded Interactive Disambiguation for Text-to-SQL](http://arxiv.org/abs/2611.17770v1)
  <details><summary>📄 Abstract</summary>
  Ambiguity remains a persistent challenge in text-to-SQL, where an underspecified natural-language question may admit multiple plausible SQL interpretations. Recent work attempts to recover the user's intended interpretation through iterative clarification, but typically relies heavily on LLM parametric knowledge for ad hoc reasoning, leading to limited ambiguity-resolution effectiveness and high LLM cost. We further observe that many ambiguity errors stem from ambiguous column grounding, which r...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 63 papers

- **2026-11-16** — Yue Xu, Xiaoyu Qin, Sihan Zhao et al. — [From Vision to Interaction: Evaluating Dynamic Social Intelligence of VLM Agents in ALIVE-World](http://arxiv.org/abs/2611.20956v1)
  <details><summary>📄 Abstract</summary>
  As AI agents are increasingly deployed in real-world applications and take on social roles, dynamic social intelligence, the ability to continuously perceive multimodal cues, infer latent cognitive states, intervene through embodied actions, and ultimately achieve social goals, has become essential. However, existing evaluations largely fragment social intelligence into text-based abstractions, static reasoning tasks, or embodied simulators that lack social dynamics. These approaches fail to cap...
  </details>

- **2026-11-16** — Abdulaziz Alqahtani, Alwaleed Alharthi, Muzammil Behzad — [Beyond Seeing: Fine-Grained Preference Validation and Severity-Aware Alignment for Mitigating Visual Hallucinations in Vision-Language Models](http://arxiv.org/abs/2611.20478v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models can produce fluent responses containing objects, attributes, or relations unsupported by the image. We study an implemented alignment pipeline that normalizes released fine-grained hallucination supervision, validates chosen-rejected preference pairs with vision-language judges, repairs rejected chosen responses, and trains LLaVA adapters with standard or severity-aware direct preference optimization. The study uses 16,143 normalized feedback records and 8,386 releas...
  </details>

- **2026-11-16** — Ruixi Yu, Dairu Liu, Xuchuan Chen et al. — [ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](http://arxiv.org/abs/2611.21607v1)
  <details><summary>📄 Abstract</summary>
  Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving this potential largely untapped. We ask whether frontier-scale representations can provide a stronger foundation for robot learning. We introduce ScaleVLA, which connects a 552B DeepSeek-V4.1-Flash bac...
  </details>

- **2026-11-16** — Zhuoyang Li, Teng Shi, Jiakai Tang et al. — [Learning to Reason with Predictive Gains for Generative Recommendation](http://arxiv.org/abs/2611.21441v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-enhanced generative recommendation (GR) has attracted increasing attention for leveraging the reasoning capabilities of large language models (LLMs) to improve next-item prediction. However, existing methods primarily optimize reasoning through Group Relative Policy Optimization (GRPO) with rule-based rewards determined by final recommendation performance, which faces two key limitations: (i) unmeasured predictive contributions within reasoning, where the predictive contributions of in...
  </details>

- **2026-11-16** — Hao Sun, Tao Hu, Shixiong Kai et al. — [[CLS] and [EOS] Tokens are not Enough for CLIP-based Class-Incremental Learning](http://arxiv.org/abs/2611.21440v1)
  <details><summary>📄 Abstract</summary>
  Class-Incremental Learning (CIL) aims to empower models to continuously acquire new knowledge while mitigating catastrophic forgetting. With the advent of vision-language models like CLIP, leveraging their cross-modal alignment capabilities to address CIL challenges has emerged as a dominant paradigm. Existing methods leverage CLIP's global representations (i.e., the visual [CLS] token and the textual [EOS] token) for cross-modal alignment. While achieving effective classification, they overlook...
  </details>

- **2026-11-16** — Yili Shen, Kehan Guo, Haomin Zhuang et al. — [Emergent Steering Beyond Endpoint Alignment in Chemical Reaction Models](http://arxiv.org/abs/2611.21423v1)
  <details><summary>📄 Abstract</summary>
  Machine learning models for chemical reaction prediction are usually evaluated by endpoint accuracy, but endpoint correctness alone does not reveal how a model represents chemical transformation or why it fails. We introduce UniRxnAxis, a unified forward-retrosynthesis framework that models both tasks as direction-conditioned endpoint redistribution in a shared latent space. By aligning source states, transformed states, and encoded target endpoints, UniRxnAxis enables directional auditing of le...
  </details>

- **2026-11-16** — Donghyeok Lee, Sangkwon Park, Munyoung Chang et al. — [Classical structural priors improve neural molecular representations in molecule language models](http://arxiv.org/abs/2611.21276v1)
  <details><summary>📄 Abstract</summary>
  Classical molecular similarity is central to chemical information systems, yet molecule-language models trained on paired structure-text data do not necessarily organize molecular embeddings according to graded structural relationships. Here we introduce Structure-Aware Guided Alignment (SAGA), a training-only regularizer that uses Centered Kernel Alignment to align neural molecular representations with fingerprint-based Tanimoto similarity, without adding parameters or requiring fingerprints at...
  </details>

- **2026-11-16** — Ye Xiao, Shesheng Song, Yi Ren et al. — [Beyond Token Stacking: Multi-scale Visual Modulation and Adaptive Fused-feature Calibration for MLLMs](http://arxiv.org/abs/2611.21168v1)
  <details><summary>📄 Abstract</summary>
  Current Multimodal Large Language Models (MLLMs) have advanced rapidly and follow two main paradigms: one involves concatenating visual and textual tokens for input into Large Language Model (LLM), while the other injects visual knowledge into Feed-Forward Networks (FFNs) of the LLM. However, the former introduces a large number of redundant visual tokens, substantially increasing computational overhead. The latter reduces sequence length but removes images from the input stage entirely, which m...
  </details>

- **2026-11-16** — Jing Yi, Cehao Yang, Hualei Zhang et al. — [Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization](http://arxiv.org/abs/2611.21094v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot cross-game generalization aims to consolidate accessible source-game experts into a single vision-language model (VLM) that controls unseen games from raw pixels without target-game parameter updates. While multi-teacher on-policy distillation (MOPD) mitigates offline exposure bias and single-game reinforcement learning (RL) overfitting, scaling it to autoregressive VLMs faces two bottlenecks. First, token-to-action misalignment from subword length bias distorts discrete action probabi...
  </details>

- **2026-11-16** — Shiyu Fang, Sheng Zhao, Jiarui Zhang et al. — [CoopDistill: Equilibrium-Guided Multi-Agent Policy Distillation for Cooperative Driving](http://arxiv.org/abs/2611.21069v1)
  <details><summary>📄 Abstract</summary>
  Cooperative driving extends autonomous driving from individual vehicle decisions to joint maneuvers that improve traffic safety and efficiency. Optimization-based methods impose safety constraints but often fix paths to simplify multi-vehicle planning, limiting spatial flexibility. Multi-agent reinforcement learning (MARL) explores alternatives through interaction, but coordinated learning and safe execution remain challenging. Their integration nevertheless faces challenges in exploration effic...
  </details>

- **2026-11-16** — Dongrun Jian, Jie Su, Jun Wang et al. — [Delay-induced anomalous density-polarization relation in chiral active matter](http://arxiv.org/abs/2611.20931v1)
  <details><summary>📄 Abstract</summary>
  Aligning active matter can spontaneously exhibit diverse forms of ordered collective motion, and higher local density is generally expected to enhance local polarization. Meanwhile, delays in agents' responses are widespread in real active systems, raising the question of how delayed alignment affects collective motion and, in particular, whether higher local density still strengthens polar order. Here, using a chiral active particle (CAP) model with delayed alignment, we uncover a counterintuit...
  </details>

- **2026-11-16** — Yeon-Jae Kim, Sangwon Kang, Byung-Kwon Min — [VA-Assembly: View-Aligned Score Guidance for Training-Free 3D Part Assembly](http://arxiv.org/abs/2611.20788v1)
  <details><summary>📄 Abstract</summary>
  Image-to-3D foundation models have improved 3D reconstruction, but typically produce monolithic representations without explicit part-level structure. Part-aware generation and learning-based assembly methods often require part-level supervision, category-specific priors, or paired part-layout training data. We instead consider a practical but underexplored setting in which independently prepared or generated 3D parts have no predefined inter-part relationships, shared coordinate frames, or cons...
  </details>

- **2026-11-16** — Haozhe Zhu, Dan Yuan, Chenghao Gu et al. — [EEGProbe: Do Vision-Language Models Really Understand EEG? A Benchmark for Signal-Grounded EEG Signals Evaluation](http://arxiv.org/abs/2611.20779v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have shown strong multimodal capabilities across scientific and biomedical domains, yet their ability to understand electroencephalography (EEG) signals remains unclear. We introduce EEGProbe, a signal-grounded benchmark for evaluating whether general-purpose VLMs can extract and reason from minimally processed, channel-wise EEG without task-specific feature engineering or EEG-specific adaptation. EEGProbe contains 620 EEG-centered questions across 13 subtasks and t...
  </details>

- **2026-11-16** — Zifan Zhang, Zhengbo Jiao, Shaobo Wang et al. — [GPRM: Global Perspective Process Reward Model](http://arxiv.org/abs/2611.20755v1)
  <details><summary>📄 Abstract</summary>
  Process Reward Models (PRMs) are widely used for step-level evaluation of multi-step reasoning in large language models, but existing methods are often limited by weak historical dependency modeling and insufficient global awareness. They typically fail to leverage prior step evaluations for coherent judgment and lack visibility into subsequent reasoning, leading to suboptimal assessment of intermediate steps. To address this issue, we propose the Global Perspective Process Reward Model (GPRM), ...
  </details>

- **2026-11-16** — Fanda Fan, Kuiye Ding, Liming Mao et al. — [MSAR: Next-Scale Autoregressive Forecasting for Time Series via Modular Multi-Scale Decoupling](http://arxiv.org/abs/2611.20714v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting underpins critical applications in finance, energy, healthcare, and transportation. Although deep models have achieved strong results, most adopt single-scale modeling or restrict multiscale processing to the input side, causing a misalignment between multiscale inputs and single-scale outputs and limiting predictive power. We introduce the Modular Scale-wise Autoregressive Framework (MSAR), a model-agnostic design that forecasts progressively across multiple temporal res...
  </details>

- **2026-11-16** — Barkin Dagda, Vinal Asodia, Iman Sharifi et al. — [Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules](http://arxiv.org/abs/2611.20648v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models offer a unified approach to perception, reasoning, and control for autonomous driving, but accurate action prediction alone does not establish compliance with traffic regulations. This paper presents a rule-guided VLA framework that incorporates symbolic traffic-rule feedback into policy optimisation. The framework combines supervised fine-tuning on expert demonstrations with reinforcement learning (RL) refinement using a reward that encourages encoded-rule co...
  </details>

- **2026-11-16** — Ruoxuan Shi, Sheng Yang, Zhengxing Su et al. — [Safety-Preserving Medical LLM Fine-Tuning via Bilevel Data Selection](http://arxiv.org/abs/2611.20643v1)
  <details><summary>📄 Abstract</summary>
  As general large language models (LLMs) are increasingly adapted for patient-facing medical applications, improving medical capability while controlling patient-facing risks remains a critical challenge. Large-scale medical instruction data are essential for acquiring domain knowledge through supervised fine-tuning (SFT), but unsafe responses can undermine existing safety alignment. To address this problem, we propose Scalable Bilevel Data Selection (S-BDS) for safety-preserving medical SFT. By ...
  </details>

- **2026-11-16** — Nikalal Kaldera, Wanqing Li, Chris Bunn et al. — [Learning a Task-Adaptive Low-Dimensional Semantic Space for Improved Visual Classification](http://arxiv.org/abs/2611.20553v1)
  <details><summary>📄 Abstract</summary>
  Semantic visual classification commonly aligns visual embeddings with semantic spaces induced by pretrained text encoders. However, such spaces are typically high-dimensional, weakly aligned with visual feature geometry, and insufficiently discriminative for downstream classification tasks. We propose TaSS, a framework for learning a task-adaptive low-dimensional semantic space that preserves semantic structure while explicitly optimizing class separability. TaSS is constructed through a paramet...
  </details>

- **2026-11-16** — Kexin Zheng, Hui Ye, Hongbo Fu — [PromptPoseFX: Authoring Pose-Driven Visual Effects through Augmented Prompting and Interactive Refinement](http://arxiv.org/abs/2611.20485v1)
  <details><summary>📄 Abstract</summary>
  Human pose-driven visual effects offer a compelling way for enhancing video expressiveness and storytelling. Authoring such effects with traditional video editing tools is a complex and time-consuming task that requires considerable technical expertise and manual effort. While generative AI models can simplify the workflow by reducing manual scripting through language-driven generation, existing approaches suffer from imprecise alignment between visual effects and pose data, failure to preserve ...
  </details>

- **2026-11-16** — Seojin Kim, Yehjin Shin, Noseong Park — [Attention Sinks as Spectral Spikes: A Mechanism Analysis of Gated Attention](http://arxiv.org/abs/2611.20403v1)
  <details><summary>📄 Abstract</summary>
  Transformer attention exhibits attention sinks, where a small subset of source tokens absorbs disproportionate attention mass across layers. Recent work shows that post-SDPA output gating strongly reduces attention-sink behavior, while separate studies link attention sinks to gradient sinks and massive activations through backward training dynamics. Yet how the same gate affects forward sink structure, backward gradient concentration, and training-time representation signatures remains unclear. ...
  </details>

- **2026-11-16** — Simon Dräger — [Halting in Recurrent Sequence Models](http://arxiv.org/abs/2611.20377v1)
  <details><summary>📄 Abstract</summary>
  Recurrent sequence models, such as recurrent neural networks (RNNs) and state space models (SSMs), are often trained to emit an end-of-sequence (EOS) token when their output sequence is complete. During training, EOS is treated as another token without a special loss term or incentive. Although this training paradigm is widely used, it is not understood how models decide to output EOS. We study a minimal version of the EOS halting problem in which networks are trained to emit a given input seque...
  </details>

- **2026-11-16** — Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. et al. — [Optimistic Verifiers Get Hacked: Reward Hacking Under an Exact Process Oracle](http://arxiv.org/abs/2611.21538v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from verifiable rewards inherits whatever its verifier gets wrong. Outside mathematics and code the verifier is a proxy, a rubric, a learned judge or a hand-written checker, and its distance from the true objective is never measured, so a rising reward cannot be told apart from a hack. We build a setting where the true reward is exactly computable at the process level: executable authorization policies over 124,416 contexts admit an oracle that lists every minimal sufficie...
  </details>

- **2026-11-15** — Yuanshan Chua, Xuejiao Zhao — [GEM-MM: Reducing VLM Hallucination with Entropy-Guided Preference Alignment](http://arxiv.org/abs/2611.20016v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are routinely aligned with offline pairwise RLHF objectives, but multimodal preference data is scarce and treats every response token as equally informative. Under a small preference budget, pair construction becomes nearly irrelevant: standard DPO-style, image-conditional, and self-improvement objectives all perform within 1.1 points on MM-RLHF metrics and 0.5 points on hallucination rates, matching the SFT baseline. We call this entropy-blind preference optimizati...
  </details>

- **2026-11-15** — Jinfeng Xu, Zheyu Chen, Shuo Yang et al. — [Take a Step Back: A Dual-Granularity Raw Feature Empowered Intermediate Fusion Graph Convolutional Network for Multimodal Recommendation](http://arxiv.org/abs/2611.19974v1)
  <details><summary>📄 Abstract</summary>
  Although multimodal recommendations have shown the ability to learn user preferences and item properties by leveraging explicit multimodal information, they remain constrained by two critical limitations: low-quality representation learning and modality fusion. For the former, existing solutions primarily focus on multi-granularity representation learning; however, we argue that training such representations is difficult due to the inherent data sparsity problem in recommendation scenarios. For ...
  </details>

- **2026-11-15** — Taha Razzaq, Murtaza Taj, Asim Iqbal — [Multimodal AI in Healthcare: Review of Vision-Language Foundation Models for Real-World Medical Applications](http://arxiv.org/abs/2611.19958v1)
  <details><summary>📄 Abstract</summary>
  The emergence of foundation models has marked a transformative shift in AI, enabling robust generalization across diverse downstream tasks through putative zero-shot learning. Large Language Models and Vision Language Models have demonstrated strong capabilities in tasks such as image interpretation, report generation, and question answering by effectively learning from multimodal data-images paired with associated text often with minimal supervision. In the healthcare domain, this ability to al...
  </details>

- **2026-11-15** — Jinsheng Wei, Song Cheng, Bo Xiao et al. — [Bridging the Terminology Gap: A Data-Centric Alignment Framework for Multilingual Translation in Cross-Border Corporation](http://arxiv.org/abs/2611.19858v1)
  <details><summary>📄 Abstract</summary>
  As globalization accelerates the demand for seamless cross-border enterprise collaboration, multilingual translation remains bottlenecked by insufficient domain-specific terminology, rigid terminology translation, weak instruction-following capabilities, and high inference latency in long-instruction scenarios. To overcome these barriers, we propose Bridging the Terminology Gap (BTG), a data-centric framework. First, BTG mines cross-lingual term alignments from domain documents and leverages LLM...
  </details>

- **2026-11-15** — Rongxin Gao, Dongxuan Liu, Chu Li et al. — [Pros4D: Modeling Evolving 4D Worlds in Latent Space for Dynamic Spatial Reasoning](http://arxiv.org/abs/2611.19803v1)
  <details><summary>📄 Abstract</summary>
  Dynamic spatial reasoning from monocular video enables vision-language models (VLMs) to understand how 3D environments evolve over time, supporting physical world understanding and embodied intelligence. Existing efforts primarily address observed-dynamics understanding, whereas agents in dynamic environments also require future-dynamics prediction beyond the observation boundary. Moreover, external geometric processing and textual descriptions can increase inference complexity or lose informati...
  </details>

- **2026-11-15** — Dhruv Trehan, Paras Chopra — [Eliciting Research Taste in LLMs through Future Research Direction Choice](http://arxiv.org/abs/2611.19794v1)
  <details><summary>📄 Abstract</summary>
  Research taste is increasingly discussed in the context of AI scientists, yet remains little studied or measured in LLMs. This judgment matters especially in open-ended research, where a direction must be chosen before a verifiable objective is available. We operationalize research taste through one task of the scientific workflow: choosing which future research direction to pursue given a research goal and current results. Rather than predicting downstream scientometric metrics or treating auth...
  </details>

- **2026-11-15** — Chunxue Xu, Yiwei Wang, Yujun Cai et al. — [Fine-Grained RLAIF for Visual Safety: Learning to Zoom into Hazards for Multimodal Safety Alignment](http://arxiv.org/abs/2611.19786v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal safety alignment heavily relies on a text-centric paradigm, assuming risks are explicit in language or globally prominent in images. However, real-world hazards are often visually subtle or peripheral, causing existing models to fail due to their reliance on coarse, global visual representations. In this work, we study fine-grained visual safety alignment and introduce a challenging 1,200-sample benchmark across four domains, where hazards necessitate localized inspection. To a...
  </details>

- **2026-11-15** — Bowei Shan, Heng Yin — [A Threshold-Free Visual-Semantic Matching Metric for Evaluating Consistency in Subject-Driven Image Generation](http://arxiv.org/abs/2611.19780v1)
  <details><summary>📄 Abstract</summary>
  In subject-driven text-to-image generation, quantitatively evaluating localized visual consistency across varying poses and environments remains a major challenge. Existing metrics either rely on global image embeddings (CLIP, DINO) and Vision-Language Models (VLMs) that pool spatial representations and miss fine-grained textural artifacts, or depend on scalar threshold-gated dense metrics such as Visual-Semantic Matching (VSM) that suffer from point-alignment dropouts, severe threshold sensitiv...
  </details>

- **2026-11-15** — Yuming Zhang, Xianchen Zhou, Hongxia Wang — [PISG: Constraint-Aligned Signal Amplification for Diffusion-Based Combinatorial Optimization](http://arxiv.org/abs/2611.19768v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based solvers have become a prominent approach to neural combinatorial optimization. At inference time, they assign each decision variable a prediction score. A greedy decoder ranks candidates by these scores and checks hard constraints to ensure feasibility. Top-ranked candidates should be both promising and jointly feasible, making prediction-constraint alignment critical. When this alignment is weak, greedy decoding skips constraint-violating candidates and falls back to lower-ranke...
  </details>

- **2026-11-14** — Chengsheng Zhanga, Wei Li, Chenghao Sun et al. — [DBHiCo: Dual-Branch Hierarchical Contrastive Learning for MRI Image Classification](http://arxiv.org/abs/2611.19511v1)
  <details><summary>📄 Abstract</summary>
  Automated Magnetic Resonance Imaging (MRI) image classification provides a crucial non-invasive approach for neurological diagnosis, yet it is fundamentally challenged by inherent acquisition noise and high inter-subject structural similarity, which obscure subtle pathological variations, thereby limiting the performance of deep neural networks. While contrastive learning (CL) offers a promising mitigation strategy, existing paradigms rely on rigid binary partitions that ignore negative sample h...
  </details>

- **2026-11-14** — Samuel Younger — [Successive Convexification in Learned World Models for Safe Offline Planning](http://arxiv.org/abs/2611.19466v1)
  <details><summary>📄 Abstract</summary>
  World models learned from offline data allow an agent to plan without further interaction with the environment, but the sampling-based planners used with them handle safety constraints only by scoring or rejecting sampled action sequences. We instead pose safe planning in the latent space of a learned world model as a successive convex program (SCP), in which a learned discrete-time control barrier function is imposed as a constraint at every step of the horizon. SCP requires smooth dynamics, so...
  </details>

- **2026-11-13** — Mehrdad Saberi, Vishal Asnani, Shruti Agarwal et al. — [Adaptable Watermarking: Transforming Image Watermarking Models via Lightweight Adapters](http://arxiv.org/abs/2611.18363v1)
  <details><summary>📄 Abstract</summary>
  We explore the adaptability of neural image watermarking models; the extent to which one watermarking method can be transformed into another through lightweight adaptation. We introduce a framework that enables encoder-decoder watermarking architectures to become modular and upgradable, supporting multiple watermarking styles without re-training full models. Adaptation is performed by attaching a compact parameter-efficient adapter and fine-tuning under a multi-domain residual alignment loss (sp...
  </details>

- **2026-11-13** — Jie Hu, Yu Zheng, Wenzhi Wu et al. — [VLAN: Vision-Language Accessible Navigation](http://arxiv.org/abs/2611.18346v1)
  <details><summary>📄 Abstract</summary>
  Accessible mobility is user-conditioned rather than scene-intrinsic, as walkable paths for one embodiment are inaccessible to another. Yet, existing benchmarks evaluate traversability under a fixed and limited embodiment. We present Vision-Language Accessible Navigation (VLAN), containing 1,000 scenes, 20K navigation trajectories, and 160K keyframes across diverse lighting, environmental conditions, scene semantics, and path geometries. For each trajectory, VLAN provides embodiment-specific acti...
  </details>

- **2026-11-13** — Zhennan Zhang, Shaobo Yu, Haoting Zhang et al. — [CGTransformer: A Topology-Aware Autoregressive Framework for Crystal Generation and Inverse Design](http://arxiv.org/abs/2611.18303v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive language models offer a unified route to crystal generation and inverse design, but their performance depends on how periodic structures are serialized. Symmetry equivalent and closely related crystals can receive different atomic orders under coordinate-based serialization, introducing variability unrelated to their structural connectivity. Here, we present CGTransformer (Crystal Graph Transformer), an autoregressive generative framework that addresses this challenge via a graph-...
  </details>

- **2026-11-13** — Nima Eshraghi, Lovedeep Gondara, Sagarika Suresh et al. — [Right Token, Right Time: From Per-Token Gating to Trajectory-Aware Activation Steering](http://arxiv.org/abs/2611.18274v1)
  <details><summary>📄 Abstract</summary>
  Activation steering via sparse autoencoders (SAEs) enables behavioral control of large language models without task-specific fine-tuning. Yet, standard methods apply the steering signal at every generated token, displacing representations from the distribution the model was trained on and eroding generation quality. We show that \emph{when} along a generation the intervention is applied is a decisive axis of control. We cast steering as a per-token allocation problem under a fixed budget of stee...
  </details>

- **2026-11-13** — Jaeyoo Park, Bohyung Han — [Structural Self-Teaching for Compositional Generation in Unified Multimodal Models](http://arxiv.org/abs/2611.18261v1)
  <details><summary>📄 Abstract</summary>
  We propose Structural Self-Teaching (SST), a novel framework that enhances compositional image generation in diffusion-based unified multimodal models (UMMs) by leveraging their internal understanding path as a source of structural supervision. The generation path of UMMs often struggles with dense compositional prompts, leading to missing objects, attribute binding failures, and spatial errors. In contrast, their understanding path localizes the same phrases in images that satisfy these prompts...
  </details>

- **2026-11-13** — Mateusz Wozniak, Qi Gao, Agnieszka Wykowska — [Personalization of Basic and Moral Values Guiding LLM-Controlled Assistant Robots](http://arxiv.org/abs/2611.18230v1)
  <details><summary>📄 Abstract</summary>
  Personal assistant robots powered by large language models (LLMs) are likely to enter everyday life within the next decade, but the values that should guide their behaviour remain largely unspecified. Current alignment practice steers a single model toward an aggregate of human values, ignoring that individual users may prefer a robot whose value profile differs from their own. We administer parallel self- and robot-targeted versions of three established psycho-metric instruments - the simplifie...
  </details>

- **2026-11-13** — Julian Kauk — [Large language models put existential risk from artificial intelligence at 10%](http://arxiv.org/abs/2611.18219v1)
  <details><summary>📄 Abstract</summary>
  How likely is it that advanced artificial intelligence (AI) will cause human extinction or a similarly permanent disempowerment of humanity? Humans, including AI experts, frequently disagree on this question. Yet one important perspective is missing from this debate: that of AI systems themselves. We put the question to 241 large language models (LLMs) at every available reasoning setting. The models converged on a median risk of 10.0%, with the middle 90% of their estimates between 3.5% and 15....
  </details>

- **2026-11-13** — Alexandru Rancea, Ionut Anghel, Tudor Cioara et al. — [A Multi-Layered AI Pipeline for BPMN Generation from Natural Language](http://arxiv.org/abs/2611.18157v1)
  <details><summary>📄 Abstract</summary>
  The automated transformation of unstructured natural language process descriptions into Business Process Model and Notation (BPMN) diagrams remains a challenging task, due to linguistic ambiguity and the difficulty to detect non-adjacent control-flow relationships. This paper proposes a solution for generating BPMN models from natural language descriptions through a multi-layered pipeline that integrates transformer-based architectures, Large Language Models and ontology population. The proposed...
  </details>

- **2026-11-13** — Yuhuan You, Wenxiang Guo, Zhifang Guo et al. — [Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models](http://arxiv.org/abs/2611.18112v1)
  <details><summary>📄 Abstract</summary>
  Audio phase relations encode source locations, yet existing large audio-language models (LALM) reduce audio to single-channel content to stabilise general audio understanding, leaving spatial information for direction, distance, and source-relation questions unused. We present SpheraAudio, which accepts recordings with any channel count -- mono, stereo, First-Order Ambisonics (FOA), or higher -- and maps them into a single token stream. A spatial encoder turns complex multichannel spectra into s...
  </details>

- **2026-11-13** — Hongsen Cao, Shanxin Yuan, Mona Jaber et al. — [EcoVGGT: Pinned-Key Inference for Efficient and Streamable Feed-Forward 3D Reconstruction from Long Videos](http://arxiv.org/abs/2611.18099v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward multi-view transformers such as VGGT recover the cameras and geometry of a video in one pass, but the cost of their cross-frame attention grows quadratically with the frame count, and their accuracy drops on long videos. Most remedies approximate attention over all frames within a budget or select a few keys by their content. We hypothesize that the keys of a long video can be chosen without looking at its content, and our experiments on VGGT and $π^3$ support it: a few dozen evenly...
  </details>

- **2026-11-13** — Chengpeng Fu, Xiaocheng Feng, Wenshuai Huo et al. — [VEPO: Mitigating Multilingual Hallucinations in LVLMs via Visual Evidence-guided Preference Optimization](http://arxiv.org/abs/2611.18096v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) achieve strong multimodal performance, yet they remain prone to object hallucination---generating answers that are linguistically fluent but visually ungrounded. This issue is especially severe in low-resource languages, where weaker cross-modal alignment causes models to rely more on language priors than on image evidence. Existing remedies either require costly multilingual annotations or external translation/reward models, or intervene at inference time in...
  </details>

- **2026-11-13** — Utkarsh Kumar Singh, Manish Das, Shiv Ram Dubey et al. — [SWAM: Saliency-Weighted Asymmetric Merging for Efficient Vision Transformers](http://arxiv.org/abs/2611.18057v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) achieve strong performance on image recognition tasks, yet their quadratic self-attention complexity over input tokens creates prohibitive computational costs for practical deployment. Token reduction methods offer a practical solution by progressively reducing the token sequence during the forward pass. We propose Saliency-Weighted Asymmetric Merging (SWAM), a training-based token merging framework that extends the Bipartite Soft Matching (BSM) with two saliency-aware...
  </details>

- **2026-11-13** — Xianxu Wu, Shang-Ching Liu, Zhaocong Liang et al. — [A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space](http://arxiv.org/abs/2611.18026v1)
  <details><summary>📄 Abstract</summary>
  Large language and vision-language models have substantially advanced robotic behavior planning from natural-language instructions and visual observations. However, safe manipulation in tabletop environments remains challenging because the safety constraints required for a task depend on the surrounding scene and may not be explicitly specified in the instruction. We propose a safety-aware behavior planning framework based on an explicit Constraint Space that stores reusable textual safety rules...
  </details>

- **2026-11-13** — Zhihao Yang, Zhiyu Xiang, Peng Xu et al. — [RSSA: Robust Semantic and Spatial Aligner for Collaborative Perception](http://arxiv.org/abs/2611.18023v1)
  <details><summary>📄 Abstract</summary>
  V2X collaborative perception improves single-vehicle perception by aggregating multi-view features from collaborative agents. However, existing methods typically rely on simple spatial warping to align the collaborative features, which can cause semantic misalignment during fusion. Meanwhile, these deterministic warping-based methods are highly sensitive to the positional noises. In this paper, we propose a plug-in module called Robust Semantic and Spatial Aligner (RSSA), which performs semantic...
  </details>

- **2026-11-13** — Monica Riedler, Jasmin Orth, Raffaella Bernardi et al. — [In the Eye of the Beholder: Human Label Variation in Textual and Visual Entailment](http://arxiv.org/abs/2611.17954v1)
  <details><summary>📄 Abstract</summary>
  Human Label Variation (HLV) is increasingly recognised as an informative signal that reflects meaningful differences in how people interpret the same input. While HLV has been studied extensively in Natural Language Inference (NLI), much less is known about HLV in Visual Entailment (VE; Xie et al., 2019), where the textual premise is replaced by an image, keeping the hypothesis and label space fixed. We introduce VariNLI-VE, a dataset for studying how HLV changes between paired NLI and VE instan...
  </details>

- **2026-11-13** — Dohyun Kim, Jaeung Lee, Donghee Hong et al. — [DECODE: Diagnosing Interpretability Failures in Automated Interpretation Process](http://arxiv.org/abs/2611.17856v1)
  <details><summary>📄 Abstract</summary>
  Tools for interpreting the internal representations of Large Language Models (LLMs) increasingly rely on LLMs themselves to both generate and evaluate explanations, creating a self-referential automated interpretation process with minimal human oversight. This automation raises significant reliability concerns, which are exacerbated by the absence of ground truth. In practice, it is difficult to validate explanations or to attribute interpretability failures to their source -- whether they origi...
  </details>

- **2026-11-13** — Xingyi Li, Jiahao Yang, Yiqin Zhu et al. — [SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation](http://arxiv.org/abs/2611.17821v1)
  <details><summary>📄 Abstract</summary>
  Moving a scene generator to a new game engine requires more than exporting its final output: planning, construction tools, and stored experience may also depend on the original backend. We present SceneAgent, a multi-agent framework for reusing the construction process and its experience across backends. A canonical SceneContext maintains the evolving world, while backend adapters isolate coordinate conventions, asset bindings, and export. Structured handoffs let fresh Builder sessions query thi...
  </details>

- **2026-11-13** — Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein et al. — [Aligning AI Teams](http://arxiv.org/abs/2611.17820v1)
  <details><summary>📄 Abstract</summary>
  Previous work has shown that alignment training on individual LLM agents can fail to transfer to multi-agent settings. We investigate the underlying mechanisms for this failure, and explore interventions to preserve alignment transfer to multi-agent LLM teams. We focus on two software-engineering tasks (sepsis triage, a news recommender) and ten consulting-proposal generation tasks. We present four findings: (1) The single-vs-team safety gap does not show a clear trend with more capable models. ...
  </details>

- **2026-11-13** — Qigan Sun, Xudong Wang, Chaoning Zhang et al. — [RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG](http://arxiv.org/abs/2611.17788v1)
  <details><summary>📄 Abstract</summary>
  In retrieval-augmented generation (RAG), query rewriting serves as a core interface that aligns user intent with external knowledge bases, and its effectiveness directly determines overall system performance. However, generative retrieval faces three critical challenges in real-world deployment: noisy retrieval feedback, the difficulty of jointly optimizing discrete prompt templates and continuous decoding-control parameters, and the limited generalization of static rewriting strategies under se...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 60 papers

- **2026-11-16** — Prashanti Nilayam, Kiran Kumar Ramanna, Prashil Tumbade et al. — [Borrowed Strength, Imported Risk: Capability Gaps and Reception Govern Heterogeneous LLM Debate](http://arxiv.org/abs/2611.20649v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous LLM debate is often attributed to collective reasoning that creates capability beyond any member. In the matched panels we study, the aggregate gain is dominated by capability transfer: a peer supplies task competence and receivers absorb a measurable fraction. Across nine matched directions, honest benefit and first-exchange adversarial exposure open when the peer has a positive same-task advantage, and honest gain is closely described by the empirical decomposition $ΔA_d^{\mathrm...
  </details>

- **2026-11-16** — Kimon Fountoulakis, Maksim Melnichenko, Muhammad Fetrat Qharabagh et al. — [Trustworthy Numerical Software in the Age of AI: What Would Turing Do?](http://arxiv.org/abs/2611.21570v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents can now produce numerical software faster than human experts can review it, raising serious concerns about usability and reliability. These and other AI tools are already transforming mathematics and software, and they will soon transform mathematical software. These concerns motivated us to assess AI-generated numerical linear algebra (NLA) kernels, which we did through an audit of a recent public GPU QR competition. All five leading kernels passed the competition's accuracy te...
  </details>

- **2026-11-16** — Amber He Wei, Shiyu Cheng, Andrew Clark et al. — [A Scalable Decentralized Event-Triggered Topology-Switching Protocol for Verifiable Safety in Multi-Agent Systems](http://arxiv.org/abs/2611.21513v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a decentralized event-triggered topology-switching protocol that allows agents to disconnect from the communication network while preserving state safety and excluding Zeno behavior. We establish a robust barrier function condition that guarantees safety as long as the estimation error remains within a prescribed threshold. Each agent uses locally computable certificates to determine when to connect and disconnect from the network. The certificate construction improves scalab...
  </details>

- **2026-11-16** — Fabio Picariello, Salvatore Cipolla, Susanna Bonura et al. — [Adaptive-Elbow Graph Traversal for Schema Retrieval in Text-to-SQL](http://arxiv.org/abs/2611.20979v1)
  <details><summary>📄 Abstract</summary>
  LLM-based natural-language interfaces to relational databases are gated by a schema-retrieval step: the generator can only be as good as the slice of schema it is shown. On a database with hundreds of tables, that slice must be selected and the selection is two-sided---omit a needed table and the query becomes unrecoverable, include too many and the irrelevant ones act as noise that degrades the model's output. When an agentic retriever that lets the model inspect the schema can be too costly or...
  </details>

- **2026-11-16** — Amir Bayat, Raphael M. Jungers — [NL2RCtrl: Risk-Controlled Controller Synthesis from Natural Language Requirements](http://arxiv.org/abs/2611.20748v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have enabled the translation of natural language (NL) requirements into linear temporal logic (LTL) specifications, facilitating controller synthesis for cyber-physical systems (CPSs). However, the reliability of such translations remains a concern in safety-critical applications, particularly when NL requirements are ambiguous. This paper proposes a framework based on Conformal Risk Control (CRC) to provide a statistical guarantee on the risk of issuing a controller...
  </details>

- **2026-11-16** — Yiyuan Ge, Changxing Ding, Ziyu Hao et al. — [Lift, See, Act: Hierarchical Robot Policy Pretraining with 3D Foundation Models](http://arxiv.org/abs/2611.20481v1)
  <details><summary>📄 Abstract</summary>
  Robot policy pretraining based on human videos is crucial for improving the policy's generalization ability. One main challenge for this task is the lack of explicit action-relevant representations in such unlabeled data. Recent works tend to estimate 3D hand motion trajectories from videos using 3D foundation models (3D FMs). However, they keep solely the sparse trajectories as supervision, ignoring the rich, fine-grained information produced during the trajectory extraction process. To address...
  </details>

- **2026-11-16** — Wenhao Li, Chong Xiao, Xiaokun Bai et al. — [Words Speak Louder? Exploring the Language Shortcut of LLM-Driven Incomplete Multimodal Learning](http://arxiv.org/abs/2611.20349v1)
  <details><summary>📄 Abstract</summary>
  Is a face or a voice still heard once the words are known? Incomplete multimodal learning increasingly uses large language models (LLMs) as fusion engines: modality features enter as token blocks and missing modalities become placeholders. We find that LLM-driven fusion can override non-verbal evidence it can read. Contrasting its full-input prediction with counterfactual views, the same model shown one modality or no content, we identify language shortcuts. We build MR-Bench: MR-Bench-A types e...
  </details>

- **2026-11-16** — Jorge Valverde-Rebaza, Nathan Garcia-Larios, Karime Ruvalcaba-Perez et al. — [Evaluating Cultural Reasoning and Robustness in LLMs for Spanish Political Discourse](http://arxiv.org/abs/2611.21535v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to interpret, generate, and mediate public-facing language, which makes their reliability especially consequential in politically sensitive settings. Although sentiment analysis is a common task in this area, affective meaning in social media discourse is often conveyed through culturally situated and pragmatically indirect cues that are not well captured by label-centric evaluation alone. In this paper, we evaluate the robustness of LLMs for se...
  </details>

- **2026-11-16** — Xuexin Liu, Zengyi Wo, Shiyu Zhang et al. — [ExRel: Learning Directed Reuse Relevance between Rich-Text K-12 Question Images with Executable Relation Contracts](http://arxiv.org/abs/2611.21461v1)
  <details><summary>📄 Abstract</summary>
  In K-12 education, question images combine text, mathematical expressions, diagrams, and diverse layouts. Variations in wording, conditions, answer options, or task scope can substantially alter their reuse utility despite visual similarity. We formulate this problem as directed reuse relevance, grading candidate utility as Strong, Medium, or Weak. However, generic similarity scores overlook task-specific reuse requirements, while natural supervision is dominated by Strong relations and lacks fi...
  </details>

- **2026-11-16** — Hassan Munif, Anthony Couthures, Vineeth Satheeskumar Varma et al. — [Robust Action Clusters and Cascades in Opinion Dynamics with Heterogeneous Action Thresholds](http://arxiv.org/abs/2611.21446v1)
  <details><summary>📄 Abstract</summary>
  We study the preservation and propagation of public actions in networks whose agents hold continuous private opinions. Agents update their opinions from their neighbors' observed actions and express them through action rules whose thresholds differ across agents. We characterize groups of agents that preserve a given common action regardless of the outsiders' actions. We call such a group, paired with that action, a robust action cluster. We show that a group is a robust action cluster for that ...
  </details>

- **2026-11-16** — Daniel Baumartz, Alexander Mehler, Patrick Schrottenbacher et al. — [Rubric-Based AES with LLM Ensembles: Scoring of Student Responses in Critical Online Reasoning Using Ensembles of LLMs](http://arxiv.org/abs/2611.21422v1)
  <details><summary>📄 Abstract</summary>
  Grading student responses is costly and time-consuming. Moreover, human annotators are prone to bias, fatigue, and rater drift, which further limits grading reliability. Various methods have been employed to develop automated essay scoring (AES) systems to reduce these costs and address bias-related issues. These methods range from early text-feature-based systems to current machine-learning and transformer-based models. Specifically, large language models (LLMs) offer the potential to streamlin...
  </details>

- **2026-11-16** — Oumaya Ladhari, Matthieu Saubanère, Jérémie Messud — [Success Probability of Block-Encoding Methods](http://arxiv.org/abs/2611.21080v1)
  <details><summary>📄 Abstract</summary>
  Block-encoding methods apply nonunitary functions $f(\widetilde H)$ of a normalized Hermitian operator on a quantum computer, but only upon a successful postselection, which introduces a shot overhead rarely included in resource estimates. We analyze the success probability $p^{(f)}_{\mathrm{success}}=\sum_n w_n|f(\tilde E_n)|^2$ of three constructions, namely linear combination of unitaries (LCU), qubitization and quantum singular value transformation (QSVT), where $w_n$ are the weights of the ...
  </details>

- **2026-11-16** — N. Bucciantini, L. Del Zanna — [A 3+1 formalism for self-similar expanding grids in computational relativistic and Newtonian magnetohydrodynamics](http://arxiv.org/abs/2611.20865v1)
  <details><summary>📄 Abstract</summary>
  Astrophysical systems frequently undergo spatial expansion during their evolution. Simulating these systems with standard conservative codes for hydrodynamics and magnetohydrodynamics using fixed grids is challenging, particularly when attempting to preserve high resolution across vast changes in physical scale. While moving or expanding meshes, or adapting mesh refinement, can address this issue, they introduce computational complexity and are notoriously difficult to implement robustly. We aim...
  </details>

- **2026-11-16** — Lion Jasper Gleiter, Tingying Peng — [Interpretable deep concepts of organoid morphology](http://arxiv.org/abs/2611.20840v1)
  <details><summary>📄 Abstract</summary>
  Image-based classification of organoid morphologies can indicate drug response, viability, or successful differentiation. In recent work, learned representations outperform handcrafted features as the basis for downstream classifiers. However, their black-box nature hides the morphological cues a classifier relies on. Based on the foundation models DINOv3 (general-purpose) and ViTAMIn-O (organoid-specific), we train sparse autoencoders (SAEs) to learn interpretable concepts related to distinct o...
  </details>

- **2026-11-16** — Roméo Zapata, Bleuenn Belz, Xingyu Yang et al. — [Material Tailored Multispectral Magnetization via the Inverse Faraday Effect in Tunable Coaxial Nanoantenna](http://arxiv.org/abs/2611.20735v1)
  <details><summary>📄 Abstract</summary>
  All-optical control of magnetization via the Inverse Faraday Effect presents a transformative pathway for ultrafast high-density data storage and nanoscale spintronics. However, unlocking its full potential requires moving beyond traditional gold-centric, narrowband constraints. In this study, we present a comprehensive theoretical framework evaluating IFE-driven static magnetic field generation across a diverse library of plasmonic materials, including gold, silver, copper, aluminum, and titani...
  </details>

- **2026-11-16** — Haiteng Wang, Haoze Li, Jingwei Guo et al. — [IndustrialKnowEval: A Benchmark for Evaluating Multi-Level Industrial Knowledge in LLMs](http://arxiv.org/abs/2611.20695v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly explored for industrial tasks, yet few benchmarks evaluate their mastery of industrial knowledge across different types of cognitive demand. We introduce IndustrialKnowEval (IndKnow), a benchmark for industrial knowledge and engineering question answering. It contains 43,282 samples covering 21 task types across seven industrial sectors, including aerospace, electric power, and metallurgy, organized into four levels of cognitive demand: memory, compr...
  </details>

- **2026-11-16** — Yuchen Fan, Chang Wei, Pao-Hsiung Chiu et al. — [Newton-PINet: A fast physics-informed neural network with Newton linearization for meta-learning nonlinear PDEs](http://arxiv.org/abs/2611.20609v1)
  <details><summary>📄 Abstract</summary>
  Scientific machine learning has opened new avenues for solving parameterized partial differential equations (PDEs), enabling models to learn a family of PDEs and generalize to unseen instances. In this context, data-driven operator learning methods typically require large training datasets, while physics-informed neural networks (PINNs) suffer from difficult optimization and limited generalization, especially for nonlinear PDEs. We propose Newton-PINet, a physics-informed network enhanced by New...
  </details>

- **2026-11-16** — Jia-Xiao Su, Xiang-Chuan Yan, Hai-Xia Li — [A widely-tunable printed-circuit-board-based resonant electro-optic modulator](http://arxiv.org/abs/2611.20590v1)
  <details><summary>📄 Abstract</summary>
  We present a simple, printed-circuit-board (PCB)-based resonant electro-optic modulator (EOM) featuring a wide operational frequency range. By utilizing a low-loss, high-frequency variable capacitor, the resonant frequency can be continuously tuned by typically 30% within a single band, e.g., from 161.0 MHz to 233.5 MHz. Furthermore, by swapping a radio-frequency transformer, the EOM's resonance is reconfigurable across the 17.7-489.7 MHz range, with quality factors ranging from 46 to 109. Using...
  </details>

- **2026-11-16** — Hongbo Zhang, Liuyang Song, Hang Zhou et al. — [VAHBench: A Harness Benchmark for Agentic Long-Video Generation](http://arxiv.org/abs/2611.20535v1)
  <details><summary>📄 Abstract</summary>
  AI agents are commonly used for everyday information retrieval and coding. We ask whether they can also interpret human requests and turn them into complete videos. We introduce VAHBench, a benchmark that tests this ability through five short-drama briefs specifying story, characters, dialogue and duration. Agents plan and carry out production using shared generation tools. Evaluation combines video completeness and basic quality with checks of production reliability and reporting accuracy. Acro...
  </details>

- **2026-11-16** — Mao Guan, Qian Chen, Ge Meng et al. — [FinVerify: A Verification Framework for Financial Agents](http://arxiv.org/abs/2611.20423v1)
  <details><summary>📄 Abstract</summary>
  Financial agents produce numerical claims that can be wrong even when their calculations execute correctly, due to mismatched reporting periods, unsupported sources, incompatible units, or incorrect financial definitions. We introduce FinVerify, an evidence-grounded framework for verifying financial agents' numerical claims. Based on an analysis of 190 incorrect trajectories from the Agent Finance Reasoning dataset, we define five error categories--temporal integrity, source fidelity, comparabil...
  </details>

- **2026-11-16** — Ilya A. Shkrob — [A Structural Framework for Succession: Continuation, Recognition, and Realization](http://arxiv.org/abs/2611.20422v1)
  <details><summary>📄 Abstract</summary>
  Succession asks whether an entity encountered later is the same entity that entered an arrangement earlier. For an artificial system that is fine-tuned, distilled, or copied, it has to be answered. We look for a mathematical structure weak enough to cover any such case and strong enough to support general theorems, so that results follow from the structure's conditions rather than from a particular pipeline or criterion. Succession is modeled on state/modification graphs with relational lifts th...
  </details>

- **2026-11-15** — Chaoqun He, Wannian Yi, Changyi Sun et al. — [Learning When to Continue and When to Stop: Termination-Aware OPSD](http://arxiv.org/abs/2611.19925v1)
  <details><summary>📄 Abstract</summary>
  On-Policy Self-Distillation (OPSD) improves language model reasoning by distilling from a frozen teacher initialized identically to the student and conditioned on privileged information. However, we identify an underexplored termination mismatch in OPSD: the student fails to reliably learn when to continue and when to stop. This mismatch manifests in two opposing failure modes-premature termination, where reasoning stops before sufficient progress is made, and repetition-driven over-generation, ...
  </details>

- **2026-11-15** — Paul Deepakraj Retinraj — [When Facts Change, Which Decisions Break? Dependency-Aware Context Graphs for Agents](http://arxiv.org/abs/2611.19859v1)
  <details><summary>📄 Abstract</summary>
  When an observed fact changes, an agent must identify and repair the decisions that depend on it while preserving unaffected outputs. We investigate the reliability-cost trade-off of field-level dependency graphs extracted from actual agent read traces. A controlled benchmark spans three executable workflow domains and four successive updates, with independent imperative and expression-based references. Across 120 workflows, two models and two repeated runs, we compare full recomputation, rollin...
  </details>

- **2026-11-15** — Jiahang Liu, Wenbo Zhang, Junsong Wang et al. — [DoF-Query Transformer for Adaptive Fusion of Egocentric Vision and Forearm HD-sEMG in Continuous Hand Kinematics](http://arxiv.org/abs/2611.20196v1)
  <details><summary>📄 Abstract</summary>
  Continuous and accurate estimation of human hand kinematics is important not only for intuitive human-machine interaction, but also for capturing fine-grained human manipulation demonstrations that can provide action supervision for embodied-intelligence datasets and dexterous robot learning. However, individual sensing modalities may be insufficient for reliable estimation under varying operating conditions. We present a finger-unencumbered multimodal framework for continuous regression of 20 h...
  </details>

- **2026-11-15** — Yimin Han, Jiahui Zhang, Wanyue Li et al. — [MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams](http://arxiv.org/abs/2611.19998v1)
  <details><summary>📄 Abstract</summary>
  Real-time whole-body imitation from monocular video requires both a robust universal tracker and high-quality real-time reconstruction. We present MoViC, a framework that uses live RGB video as a control signal for humanoid robots without wearable tracking devices. The framework combines monocular human motion reconstruction, robot retargeting, and a transformer-based behavior foundation model. The policy receives proprioceptive history, a single explicit next-step reference, and a compact frequ...
  </details>

- **2026-11-15** — Haoran Yu, Lifei Liu, Danping Zhang — [Reliable Mining of Heterogeneous AI Coding-Agent Data: Context-Aware Prediction and Resource-Aware Ranking](http://arxiv.org/abs/2611.20297v1)
  <details><summary>📄 Abstract</summary>
  Operational records from AI coding agents differ across agents, repositories, tasks, and workflows. We study 71,677 pull requests (PRs) from six agents and show that pooling these records can reverse descriptive and predictive conclusions. PRs carrying a co-authorship trailer have a 55.6% merge rate, compared with 77.5% without the trailer, but removing the dominant agent flips this -21.8 percentage-point gap to +23.7 points. We treat this Simpson-type reversal as a data-veracity problem and rep...
  </details>

- **2026-11-15** — Ali Şenol — [The Silent Cost of Conversation History in LLM Reasoning](http://arxiv.org/abs/2611.20071v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) in multi-turn information systems accumulate their own earlier replies and a growing task state. We asked whether this conversation history lowers accuracy, and whether process-level quality metrics warn before it does. Each analysis was fixed before its outcomes were computed. In Study 1, on 48 sharded math tasks, retaining its replies lowered final success by 0.21 for GPT-4o-mini and 0.29 for Mistral-7B (Holm-adjusted p = 0.026 and 0.004); Llama-4 Scout showed the ...
  </details>

- **2026-11-15** — Ruirui Shen, Jianqi Gao, Xiangfeng Luo et al. — [SAGE-VQA: A Training-Free, Self-Evolving Agentic Framework with Grounded Evidence for Knowledge-Based Visual Question Answering](http://arxiv.org/abs/2611.19933v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-based visual question answering (KB-VQA) aims to combine visual information with external knowledge to answer user questions. Existing methods face two main bottlenecks: visual perception errors can propagate into hallucinations, and generalization across scenarios remains limited. To address these issues, we propose SAGE-VQA (Self-evolving Agent framework with Grounded Evidence), a training-free agentic framework that combines evidence verification with experience evolution. Our key i...
  </details>

- **2026-11-15** — Thilo Tamme, Anton Hantel, Jakob Scheppers — [Who Writes the Codebook? An Eight-Step Framework for Auditing LLM-Generated Category Systems](http://arxiv.org/abs/2611.19872v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly create the categories through which qualitative evidence is interpreted. Existing coding benchmarks often hold these categories fixed. We propose the Qualitative Variance Audit Framework, an eight-step method that compares codebook creation, repeated application and code distributions under controlled inputs. It combines model-owned and shared-reference codebooks to distinguish variation in the overall pipeline from application differences within a commo...
  </details>

- **2026-11-15** — Yuxiang Mei, Dongxing Xu, Yanhua Long — [A Speech-LLM Framework for Enrollment-Free Wake-Word-Guided Target-Speaker Recognition in Complex Noisy Scenarios for Seamless Human-Machine Interaction](http://arxiv.org/abs/2611.19844v1)
  <details><summary>📄 Abstract</summary>
  Target-speaker automatic speech recognition (TS-ASR) is essential for reliable human-machine interaction in complex acoustic environments, where overlapping speech and background noise make it difficult to identify and recognize the intended speaker. Existing approaches typically rely on speaker enrollment or cascaded processing pipelines, limiting their flexibility in practical applications. To address these limitations, we propose an enrollment-free Speech-LLM framework that leverages wake-wor...
  </details>

- **2026-11-14** — Gurpriya Bhatia, Clifford Neuman — [Protecting the System, Stranding the User: The Limits of Multi-Agent Authorization](http://arxiv.org/abs/2611.19598v1)
  <details><summary>📄 Abstract</summary>
  Current multi-agent authorization architectures prioritize system integrity over human outcomes. While recent models successfully prevent privilege escalation, they externalize the cost of failure onto the human operator. Re-centering authorization around human impact exposes four structural vulnerabilities in current paradigms. First, calling an agent's understanding of user intent verified is misleading. Intent has no formal definition, so no check against it can be definitive. Systems should ...
  </details>

- **2026-11-14** — Jerome Henry, Swadhin Pradhan, Amine Choukir — [Diagnosis as Percolation on an Evidence Graph: Root-Cause Recoverability in Network Fault Diagnosis](http://arxiv.org/abs/2611.19584v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing failures from incomplete observations presents three challenges: determining whether sufficient evidence connects a possible cause to a symptom, distinguishing the true cause from plausible alternatives, and assessing when a diagnosis can be trusted. We introduce an evidence-graph framework that separates these challenges and uses percolation theory to analyze how missing information affects cause-symptom connectivity. In controlled simulations with an average degree of four, a giant ...
  </details>

- **2026-11-14** — Fernando Cardenas Piepereit — [Before the Word: Name Information in Description-Derived States of Small Language Models, With and Without Naming Failure](http://arxiv.org/abs/2611.19609v1)
  <details><summary>📄 Abstract</summary>
  The tip-of-the-tongue (TOT) state, knowing an object but not its name, motivates this study as an analogy only. We ask whether small language models form a name-predictive state from a name-free description, and whether it differs when naming fails but description selection succeeds. In an internally pre-registered study (a frozen document, no external registry) of Qwen2-0.5B, SmolLM2-1.7B and Phi-3-mini with 200 items, we combine a similarity read-out, a Patchscopes-style read-out and activatio...
  </details>

- **2026-11-14** — Shi Li, Lalith Sharan, Joël L. Lavanchy et al. — [EndoComparer: Comparative Surgical Video Question Answering with Pseudo-Siamese Visual Adaptation and Perceive-then-Compare Reasoning](http://arxiv.org/abs/2611.19578v1)
  <details><summary>📄 Abstract</summary>
  Purpose: Surgical training benefits from explicit comparison between cases: in patient condition, in technique and in skill proficiency. Surgical vision-language models (VLMs) offer a promising and flexible interface for this purpose. Yet current VLMs typically see one video at a time, and they often fall short when asked to compare videos. Methods: We propose EndoComparer, a VLM for comparative surgical video question answering with two components. (a) A Pseudo-Siamese Visual LoRA (PSVL) gives ...
  </details>

- **2026-11-13** — Jimin Mun, Maarten Sap, Yanai Elazar — [LECAT: Measuring LLM Category Learning from Pretraining Data](http://arxiv.org/abs/2611.18419v1)
  <details><summary>📄 Abstract</summary>
  Humans know that airplanes are fast, that this extends to red airplanes, but that it does not hold for broken airplanes. How do LLMs acquire category knowledge that humans learn and apply effortlessly? We introduce LeCat, a two-part framework to analyze LLM's Learning of Category knowledge. First, we use LeCat to evaluate models on their ability to learn category knowledge, distinguishing between three cases: memorization of in-domain category knowledge, generalization to unseen instances, and a...
  </details>

- **2026-11-13** — Runyang You, Hongru Cai, Caiqi Zhang et al. — [Agent-as-a-Judge](http://arxiv.org/abs/2611.18067v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence has progressed from task-specific systems toward general models spanning perception, generation, reasoning, and autonomous interaction, making reliable evaluation essential for comparison, deployment, and post-training feedback. At scale, modern evaluation pipelines increasingly rely on LLM-as-a-Judge to produce scores, preferences, and critiques; in its fixed-context setting, the judge relies on the supplied evaluand and evaluation materials. Yet a reliable verdict may r...
  </details>

- **2026-11-13** — Chenzhi Zheng, Xi Xiao, Chih-Ting Liao et al. — [Beyond Endpoints: Bézier Paths for Vision Foundation Model Adaptation](http://arxiv.org/abs/2611.17825v1)
  <details><summary>📄 Abstract</summary>
  Frozen vision foundation models can be adapted by learning a few prompt tokens shared across all images. When prompts are updated as data shift or tasks change, the distribution of image features moves from one endpoint to another. Prior theory asks which endpoints prompts can reach; we ask whether they can travel between them along the shortest path. Because shared prompts compete with each image's own content for attention, they often cannot. We quantify this restriction as the extra transport...
  </details>

- **2026-11-13** — Haolin Yang, Wenshan Wu, Jin Jiang et al. — [Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding](http://arxiv.org/abs/2611.17797v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agentic coding requires robust visual reasoning to analyze observations and evaluate generated artifacts. Current frameworks largely rely on a Thinking-with-Images paradigm, where agents depend on their intrinsic vision to execute visually grounded tasks. However, this architectural coupling introduces a fundamental bottleneck. Agent performance remains strictly bounded by internal perceptual limitations. Furthermore, text-only agents lack native perception. Without specialized tools,...
  </details>

- **2026-11-13** — Jiaming Tang, Zhuoyang Zhang, Junxian Guo et al. — [Training Reasoning Models in Simulation to Natively Use Real Robots](http://arxiv.org/abs/2611.18562v1)
  <details><summary>📄 Abstract</summary>
  Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control. However, strong performance has so far been achieved only by frontier proprietary models such as GPT-6 Astra and Claude Fable 5.2, whereas open-weight models remain substantially less capable. We show that an open-weight 27B reasoning model can be trained to use real robots natively through reinforcement learning, entirely in simulation and without demonstrations. Like a computer-use agent (CUA), the m...
  </details>

- **2026-11-13** — Disha Sheshanarayana, Sai Linisha Reddy Goli — [Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation](http://arxiv.org/abs/2611.18471v1)
  <details><summary>📄 Abstract</summary>
  LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory. In deployed agent systems, the same execution may be exposed through composed tools, delegation boundaries, or compacted histories, changing what execution evidence is directly observable to the verifier. It therefore remains unclear whether correct verifier judgments persist across such abstraction boundaries. We introduce Verificat...
  </details>

- **2026-11-13** — Wang Ma, Debarun Bhattacharjya, Junkyu Lee et al. — [Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles](http://arxiv.org/abs/2611.18453v1)
  <details><summary>📄 Abstract</summary>
  Reliable use of large language models (LLMs) requires uncertainty estimates that separate ambiguity intrinsic to a prompt from genuine knowledge gaps. Bayesian and deep-ensemble methods deliver this aleatoric/epistemic decomposition in principle, but are computationally prohibitive at LLM scale and require white-box access. Existing black-box methods, in contrast, summarize to a single scalar that cannot make the distinction. We introduce a two-level ensemble that bridges this gap. Stochastic de...
  </details>

- **2026-11-13** — David Nordström, Georg Bökman, Viktor Larsson et al. — [ALoMa: Affine Correspondences Beyond Patches](http://arxiv.org/abs/2611.18170v1)
  <details><summary>📄 Abstract</summary>
  Affine correspondences (ACs) enable robust and efficient solvers for multiple-view geometry by constraining the local geometry of point correspondences (PCs). Despite their utility in minimal solvers, AC estimation remains understudied. We revisit AC estimation beyond local image patches, extending it to the image and image-pair levels. Rather than estimating the components of the affine transformation separately, we learn the full 4-DoF matrix jointly. Building on this formulation, we introduce...
  </details>

- **2026-11-13** — Daniele Kopyshevskiy, Benjamin Th{é}rien, Nicolas Pinto et al. — [LACCO: Local Accumulation with Computation--Communication Overlap](http://arxiv.org/abs/2611.17991v1)
  <details><summary>📄 Abstract</summary>
  Training language models across low-bandwidth networks requires reducing synchronization overhead. Local optimization methods such as DiLoCo communicate only after several local steps, but outer gradient averaging and the outer update remain on the critical path. Existing computation-communication overlap methods avoid this stall through delayed or replica-local updates, which can degrade convergence or cause replicas to drift. We propose LACCO (Local Accumulation with Computation-Communication ...
  </details>

- **2026-11-13** — Tiantong Wang, Zhiren Gong, Yixin Wang et al. — [From Local Prediction Error to Final Outputs: A Theory of Expert Sharing in Multi-Step Reasoning](http://arxiv.org/abs/2611.17879v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) models can share experts across layers or computational steps, pooling training information from different contexts. This can reduce local prediction error, but multi-step systems are ultimately evaluated by their final outputs. We study when these local gains survive composition. In specified linear regression models, we derive exact sharing and merging criteria by balancing variance savings against bias from sharing across roles with different target behavior. Under a ...
  </details>

- **2026-11-13** — Sukit Seripanitkarn, Phonphrm Thawatdamrongkit, Supasorn Suwajanakorn — [Speed-Variation Distillation for Generative Modeling](http://arxiv.org/abs/2611.17868v1)
  <details><summary>📄 Abstract</summary>
  While diffusion models excel at image generation, their denoising trajectories pass through corrupted intermediate states far from the image manifold. We ask whether generation can instead proceed through recognizable images throughout the entire trajectory. We introduce a generative framework built around a variation-reducing degradation process that contracts diverse images toward a shared prototype while preserving recognizable intermediate states. Because such manifold traversal lacks a simp...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-11-16** — Andreas Ekelhart, Ahmad Mohsin, Iqbal H. Sarker et al. — [Expertise capture in workplace AI](http://arxiv.org/abs/2611.21456v1)
  <details><summary>📄 Abstract</summary>
  AI assistants are becoming part of how knowledge workers think and perform, accumulating the prompts, exemplars, memory and interaction histories that encode a worker's professional judgment. This infrastructure typically runs under employer or platform control. We name the resulting process expertise capture, the absorption of worker-applied knowledge and judgment into AI resources under organizational control. We develop a framework of contribution forms, technical residences and transformatio...
  </details>

- **2026-11-16** — Carlo Alberto Barbano, Giovanni Marraffini, Demian Wassermann — [Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models](http://arxiv.org/abs/2611.21215v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining has transformed language and vision, but its application to functional MRI (fMRI) is constrained by data access. The largest standardized fMRI resources are governed by data use agreements and dominated by a small number of acquisition protocols, while the thousands of openly licensed datasets on OpenNeuro are individually small, heterogeneously organized, and unprocessed. We present the first release of Open-fMIND, a uniformly preprocessed, openly accessible corpus o...
  </details>

- **2026-11-16** — Zixuan Wang, Gregory Kang Ruey Lau, Xiao Tian et al. — [EDITORS Know Your Style! Editing LoRA Subspaces for Stylistic Attribution and Imitation](http://arxiv.org/abs/2611.20846v1)
  <details><summary>📄 Abstract</summary>
  Disentangling writing style from semantic content is a fundamental challenge in literary text modeling. Style-content entanglement causes models to rely on semantic content for authorship attribution (AA) tasks and memorize author-specific content for style imitation (SI) tasks. We propose EDITORS (EditingLoRA Subspaces), a diagnose-then-deflate framework that adapts pretrained large language models and prioritizes stylistic features, making it effective for both AA and SI tasks. EDITORS first t...
  </details>

- **2026-11-16** — Yuchong Hu, Zhao Zhang, Ziyao Zhao et al. — [Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates](http://arxiv.org/abs/2611.20837v1)
  <details><summary>📄 Abstract</summary>
  When several candidates have graph support, does it matter which candidate receives which supporter and path counts? We study how LLM rankers use collaborative evidence on Amazon Books and MovieTV. Swapping user-level evidence degrades ranking, while matched item substitutions have little effect. On fixed clean-trained checkpoints, unrelated catalog text lowers Hit@1 from 44.77% to 38.70%, with 99.9% of rankings still valid. Across all three paired seeds, the NDCG@5 difference between count and ...
  </details>

- **2026-11-16** — Xuannan Liu, Tian Lan, Zekun Li et al. — [TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](http://arxiv.org/abs/2611.20430v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and (2) coupled execution that obscures the effects of individual modifications. To address these challanges, we propose TrainExplorer, a multi-agent framework for autonomous post-training, that incorporates strategy planni...
  </details>

- **2026-11-16** — Yiwei Fu, Nicholas Gabriel — [Deploying a Control-Logic LLM Assistant in Air-Gapped Power Plants: Lessons in Source Authority and Bounded Retrieval](http://arxiv.org/abs/2611.20398v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Model (LLM) assistants in industrial operational technology environments poses constraints largely absent from cloud applications: site policies restrict engineering and operational data from leaving the plant, on-premises compute is limited, and incorrect causal attribution can mislead incident response. We report lessons from deploying a control-logic evidence layer that underpins a broader on-premises operator assistance system at two gas power plants. Two prototypes ...
  </details>

- **2026-11-15** — Bart M. N. Smets, Gijs Bellaard, Pieter Wils — [Symmetry Fingerprinting with Geometric Learnable Invariants Transformers](http://arxiv.org/abs/2611.20150v1)
  <details><summary>📄 Abstract</summary>
  Geometric deep learning has made available a large variety of structurally equivariant neural network architectures, meaning a particular transformation of their input causes a predictable transformation of their output. But structural equivariance is a very strong inductive bias that can limit performance if chosen poorly. In contrast, choosing an architecture with low geometric bias necessitates data augmentation to obtain correct behavior; extending the training process. We propose a novel ne...
  </details>

- **2026-11-15** — Antonio Alcántara, Ioannis Karampinis, Spyros Chatzivasileiadis — [The Grid's Own Language: A Common Information Model Layer for LLM Grid Assistants](http://arxiv.org/abs/2611.20026v1)
  <details><summary>📄 Abstract</summary>
  Assistants built on large language models (LLMs) are entering power system operation. Current designs delegate computations to validated solvers, but the agent still infers the type, role and state of each element from its name and tool-specific formats, and errors propagate to every study. The Common Information Model (CIM), the IEC standard in which operators already exchange network models, defines unambiguously what each element is and how it connects. We propose a CIM layer for LLM grid ass...
  </details>

- **2026-11-13** — Wenhan Wu, Linghan Chen, Yudong Gao et al. — [When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2611.17917v1)
  <details><summary>📄 Abstract</summary>
  Cooperative multi-agent reinforcement learning (MARL) supports coordinated decision-making in distributed Web services, multi-robot control, and collaborative games through learned coordination conventions. When deployment requirements change, a previously useful convention may become obsolete or unsafe. For example, revised cache-sharing permissions in Web content delivery may require caches to abandon a learned division of storage and serving roles while maintaining efficient delivery. Teams m...
  </details>

- **2026-11-13** — Tamara Serrano, Nikoleta Pantelidou, Raquel Montero et al. — [Evaluating Human Sensitivity to Gender Biased AI-Generated Content through Human Assessment of Google's Autocomplete Function](http://arxiv.org/abs/2611.18371v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly present, but their effects on human users remain underexplored. We tested whether AI-attributed information influences views regarding gender-related statements, a domain where biases are pervasive. Spanish-speaking participants recruited through Prolific evaluated biased statements derived from Google's autocomplete function and human-authored, non-biased gender-related facts. Participants were either informed that some of the material was AI-genera...
  </details>

- **2026-11-13** — Jiayu Feng — [GT-FENG: General Theory of Factual Evaluation and Normative Grounding in Language Models *Author(s)](http://arxiv.org/abs/2611.18279v1)
  <details><summary>📄 Abstract</summary>
  Whether a language model's answer is correct often depends on context: the same value can be right under one jurisdiction, date, or legal definition and wrong under another. We introduce GT-FENG (General Theory of Factual Evaluation and Normative Grounding), the first general framework to unify contextual/temporal correctness and rule-based error attribution across law, policy, and other rule-governed domains. GT-FENG checks answers against the applicable rules and identifies documented rules th...
  </details>

- **2026-11-13** — Jonathan Pan, Yidi Yuan, Xin Wei Chia et al. — [From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States](http://arxiv.org/abs/2611.18272v1)
  <details><summary>📄 Abstract</summary>
  Existing memory forensics for machine learning systems typically targets static artifacts, such as model weights or prompt logs, rather than the transient computational states of a live inference process. This gap limits an examiner's ability to analyze the specific behavior of a running large language model (LLM) service that cannot be restarted or modified. We present a method for acquiring per-layer residual-stream activations from a live GPU process using a non-modifying debugger, without re...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-11-16** — Zirui Pang, Zhijie Deng, Yuancheng Wang et al. — [LEAF-OPD: Learning to Forget from Privileged Contexts via On-Policy Distillation](http://arxiv.org/abs/2611.20674v1)
  <details><summary>📄 Abstract</summary>
  LLM unlearning aims to erase targeted knowledge from large language models while preserving their utility. However, many existing methods suppress target knowledge without explicitly teaching the model how to respond to queries about it. We propose LEAF-OPD (LEArning to Forget from Privileged Contexts via On-Policy Distillation), in which a frozen teacher provides token-level supervision on student-generated responses. On forget data, the teacher uses privileged contexts (instructions not to rev...
  </details>

- **2026-11-13** — Xiuyuan Wang, Weiming Liu, Zongxin Yang et al. — [Disentangling Forgetting from Utility: Lightweight LLM Unlearning via Orthogonal Null-Space Projection](http://arxiv.org/abs/2611.17864v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) pose significant security risks by retaining private or hazardous information, creating an urgent need for unlearning techniques that excise specific knowledge without compromising general utility. However, prevailing fine-tuning-based unlearning methods struggle to achieve this balance, often suffering from computational inefficiency and unintended utility degradation due to the entangled nature of knowledge within model parameters. To disentangle forgetting from ut...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 10 papers

- **2026-11-16** — Yongkang Xiao, Qiyi Deng, Jing Chen et al. — [MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Modeling and Analysis](http://arxiv.org/abs/2611.20671v1)
  <details><summary>📄 Abstract</summary>
  Tamarin-based formal verification of security protocols requires expert-authored multiset rewriting rules and temporal-logic lemmas. Translating a natural-language protocol description into a complete formal model with an LLM is hard because syntactic, reachability, and property-level errors compound across the multi-step modeling process, and a single agent that both authors and self-evaluates cannot reliably localize them. We present MASTA, a multi-agent system that addresses these difficultie...
  </details>

- **2026-11-16** — Gustavo Pinto, Enne Rebeca Silva de Freitas, Danilo Monteiro Ribeiro — [Is This Code Mine? Student Ownership When AI Agents Write the Spec and the Code](http://arxiv.org/abs/2611.21501v1)
  <details><summary>📄 Abstract</summary>
  Software engineering courses are starting to ask students to build entire systems with AI coding agents, but little is known about what students actually do with them and whether they still own what they deliver. If the agent writes both the code and the decisions behind it, the artifacts we grade no longer show what students learned. We studied an assignment in which 18 pairs of students built applications with agents under Spec-Driven Development, combining the mined history of their repositor...
  </details>

- **2026-11-16** — Jason Alexander, Yuxuan Li, Michael Licamele et al. — [A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents](http://arxiv.org/abs/2611.21376v1)
  <details><summary>📄 Abstract</summary>
  Prior work has shown that large language models (LLMs) express implicit biases in high-publicity, one-off decision scenarios such as hiring and intelligence assessment. However, as people increasingly employ autonomous, LLM-powered AI agents that make decisions on their behalf in doing day-to-day tasks, it is of critical importance that we understand how implicit biases, based on sociodemographic assumptions, emerge across a broad milieu of workaday decision scenarios. We used the 17 domains of ...
  </details>

- **2026-11-16** — Berkay Günes, Giuseppe Viterbo, Sven Buder et al. — [A COMPASS to the Galaxy: Joint nucleosynthetic yield set comparison and parameter inference in Galactic chemical evolution](http://arxiv.org/abs/2611.21175v1)
  <details><summary>📄 Abstract</summary>
  Galactic Chemical Evolution (GCE) models connect stellar nucleosynthesis to observed abundance patterns, but their interpretation requires simultaneous parameter inference and comparison between competing stellar yield prescriptions. This remains challenging due to intractable likelihoods and growing dataset complexity. Using compass, a novel simulation-based inference framework, we perform, for the first time, amortized joint Bayesian model comparison and parameter inference for GCE models with...
  </details>

- **2026-11-16** — Aspen Wang, Yen Yu Shan, Lun-Wei Ku — [Necessary for What? Auditing Demographic Disclosure to LLM Synthetic Respondents](http://arxiv.org/abs/2611.20606v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly answer surveys on behalf of real panelists, and each panelist's recorded demographic attributes (e.g., age, education, ethnicity) are often placed in the prompt on the premise that richer profiles make more faithful synthetic respondents. While data minimization limits personal data to what a purpose requires, a synthetic survey serves several purposes at once, from predicting individual answers to estimating how opinions are distributed and comparing gr...
  </details>

- **2026-11-15** — Peng Wu, Seyede Fatemeh Ghoreishi, Nathan Bastian et al. — [Ontology-Compiled Control Barrier Functions for Heterogeneous Robot Teams](http://arxiv.org/abs/2611.20306v1)
  <details><summary>📄 Abstract</summary>
  Safety filters for heterogeneous robot teams fail because of missing constraints, overestimated braking capabilities and conflicts between individually satisfiable constraints. We present OntoCBF, which compiles a domain ontology with a class taxonomy, typed relations, safety axioms and a dynamics profile per robot class into a control barrier function filter with one quadratic program per agent. Description-logic entailment supplies the constraints of any team online, including those that follo...
  </details>

- **2026-11-15** — Victória Gomes, Fabio Palomba, Robert Feldt et al. — [The Hidden Methodological Layer: Uncovering Threats to Validity in LLM-Assisted Empirical Software Engineering](http://arxiv.org/abs/2611.20033v1)
  <details><summary>📄 Abstract</summary>
  Context: Large Language Models (LLMs) are increasingly embedded in empirical software engineering (ESE) workflows, supporting tasks such as classification, coding, extraction, synthesis, and evaluation. Their probabilistic and opaque behavior, however, introduces methodological concerns that may affect empirical rigor. Aims: This paper investigates threats to validity introduced by LLM-assisted empirical workflows and examines how LLM interactions influence empirical studies. Method: We conducte...
  </details>

- **2026-11-13** — Suvarna Kadam, Soran Parsa — [Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment](http://arxiv.org/abs/2611.18372v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control. In under 4 years the field has moved from RT-2, the first VLA, to open models that fine-tune on a single consumer GPU and to proprietary generalists that clean unseen homes. This survey reviews 88 works from December 2022 to October 2026, mainly on manipulation and navigation, plus humanoid control, world-action models and evaluation. We...
  </details>

- **2026-11-12** — Wajiha Naveed, Brandon Fain — [Mind the Accuracy-Approval Gap: How Users Evaluate Sycophantic AI in Everyday Tasks](http://arxiv.org/abs/2611.16722v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often exhibit sycophancy, a tendency to agree with users, flatter or affirm them, and preserve their face, even when independent judgment or critical feedback would be more useful. Prior work has largely evaluated sycophancy through benchmark evaluations, but less is known about how users perceive and respond to sycophantic AI in everyday tasks. We combine benchmark evaluations with two large-scale user studies. We study four personas defined through system prompts: ...
  </details>

- **2026-11-12** — Qianjie Wei, Yifan Li, Zhen Bai — [Exploring Socially Acceptable 3D Feedback Design for Inclusive Small-Group Conversation](http://arxiv.org/abs/2611.17018v1)
  <details><summary>📄 Abstract</summary>
  Prior research has shown that providing feedback on group dynamics can improve the quality of small-group conversations. However, publicly delivered feedback that targets specific individuals may reduce social acceptability due to negative experiences such as social pressure, embarrassment, and resistance. This work investigates how public feedback can be designed to remain socially acceptable while maintaining its effectiveness in XR-based small-group conversations. Informed by social science a...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 180 papers

- **2026-11-16** — Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani — [When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents](http://arxiv.org/abs/2611.21577v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) applications increasingly act as agents that select and invoke external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing clients to compose tools advertised by multiple servers. However, tool metadata used for discovery and selection is not, by itself, necessarily bound to a verified provider identity. This paper studies this gap as tool-provider misbinding: a failure in which a request intended for a legitimate provider is instead reso...
  </details>

- **2026-11-16** — Roksana Goworek, Alexander Hickey, Federico Nanni et al. — [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](http://arxiv.org/abs/2611.21449v1)
  <details><summary>📄 Abstract</summary>
  Researchers at MIT recently reported that GPT-6 Astra, a frontier large language model (LLM), can write the weights of small neural networks directly in a single reply, and can read the raw weights of small networks to say what they were trained to do. In a three-day sprint, we replicated and extended these results. Our four findings: (1) Writing weights reproduces. Astra's networks for the game Breakout scored 514, 550 and 307 (versus MIT's 517), and scored just as well on two modified versions...
  </details>

- **2026-11-16** — Jianye Zeng, Qiao Yikang, Duan Huang et al. — [RAMP: Rethinking Multimodal Evaluation through Answer Readout Protocols](http://arxiv.org/abs/2611.20653v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are often evaluated by converting model outputs into discrete answers. The conversion protocol determines which scores become predictions and can strongly influence the reported results. We introduce RAMP (Readout Aware Multimodal Protocol), a systematic framework that compares direct yes/no token logits, surface-form scores, and typed or reversed A/B interfaces under fixed model checkpoints and paired visual questions. On 500 POPE adversarial questions, ...
  </details>

- **2026-11-16** — Runzhe Wang, Huilin Lu, Shengjie Liu et al. — [AdMem: Expectation-Grounded Procedural Memory for Long-Horizon Task-Solving Agents](http://arxiv.org/abs/2611.20605v1)
  <details><summary>📄 Abstract</summary>
  An agent that carries memory across tasks is only as good as the entries it keeps. We begin from an observation that is easy to reproduce and uncomfortable for the field: naively accumulating cross-task experience can make an agent \emph{worse} than one with no memory at all. On AgentBoard, a workflow-induction memory solves fewer tasks than a memoryless ReAct agent in seven of eight domains, and a per-step procedural store with no surrounding structure loses half of ReAct's completions on Jeric...
  </details>

- **2026-11-16** — Meng Tang, Siyuan Du, Yuxin Liu et al. — [Out of Sight, Into Memory: Compact Visual Latents Retain Local Evidence in Ultra-High-Resolution Remote Sensing](http://arxiv.org/abs/2611.21457v1)
  <details><summary>📄 Abstract</summary>
  Question answering over ultra-high-resolution (UHR) remote sensing scenes poses a tension for multimodal large language models: global overviews obscure small objects and local attributes, whereas detailed crops consume substantial context. Compressing inspected crops into short sequences of continuous visual latents offers a compact memory once crop tokens are discarded, yet diagnostic studies on natural images find that models often ignore latent content, leaving unclear whether compact latent...
  </details>

- **2026-11-16** — Javier Aguilar Martín — [Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next](http://arxiv.org/abs/2611.21408v1)
  <details><summary>📄 Abstract</summary>
  A popular ideation recipe treats an embedding map of existing work as a guide: pick points far from everything and decode them into ideas. I test four ways such distances could guide ideation against what appeared later. (1) Far random directions are not text: no later item reaches a raw cosine above about 0.10 with one (after centring or whitening, 22 of 24 cells stay out of reach), and an LLM decoder shown a target's neighbours, with score-only feedback, writes those neighbours in all six targ...
  </details>

- **2026-11-16** — Yang Chen, Qianyi Wang, Ronghui Yang et al. — [Turing Agent: Agentic Formal Verification for Mathematical Research](http://arxiv.org/abs/2611.21299v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. This progress is ushering mathematics into an era of proof abundance, raising a fundamental challenge: how can we ensure the correctness of the ever-growing volume of AI-generated proofs and transform them into trustworthy, machine-verified mathematical knowledge? We introduce Turing Agent, an agent harness designed to orchestrate end-to-e...
  </details>

- **2026-11-16** — Zhonggang Li, Hongyu Zhou, Raj Thilak Rajan — [Hybrid Optimization-Generative Motion Planning for Multiagent Affine Formations](http://arxiv.org/abs/2611.21264v1)
  <details><summary>📄 Abstract</summary>
  Formation maneuver control enables a multiagent system to cooperatively navigate through constrained environments in collective motion. While various formation controllers exist, they rely heavily on high-quality and dynamically feasible reference trajectories provided a priori, making formation motion planning (FMP) essential. To address the computational challenges for high-dimensional joint trajectories faced by conventional constrained optimization-based solutions, this paper introduces a hy...
  </details>

- **2026-11-16** — Xiaoyu Li, Jiangxuan Long — [The Price of Choosing Examples: Context Overfitting in Adaptive In-Context Learning](http://arxiv.org/abs/2611.21251v1)
  <details><summary>📄 Abstract</summary>
  In-context learning is usually analyzed as if the examples in the prompt were sampled before the learner is chosen. In deployed systems they are not: examples are retrieved, filtered, re-ranked, edited, and repeatedly tested after seeing the query and the data store. We formalize this gap by treating prompt construction as adaptive data analysis through a conditional stochastic-kernel calculus. Our main quantity is the context capacity, the mutual information or approximate max-information betwe...
  </details>

- **2026-11-16** — Natalija Stepurko, Joonatan E. M. Laulainen — [Out-of-training properties in frozen interatomic potential embeddings are decodable and ordered by physical scale](http://arxiv.org/abs/2611.21116v1)
  <details><summary>📄 Abstract</summary>
  Machine-learned interatomic potentials (MLIPs) are trained on energies, forces and stresses, yet their frozen representations can predict other materials properties. We probe ORB-v3 and UMA-S across layers, read-outs and equivariant channels for nine properties of 154,875 Materials Project crystals. Both models outperform composition-only descriptors on all targets, including five outside their training objectives; errors in physical units help assess potential screening applications. Optimal de...
  </details>

- **2026-11-16** — Marcos Soldera, Robert Baumann, Bogdan Voisiat et al. — [Laser Processing for Energy Applications](http://arxiv.org/abs/2611.21024v1)
  <details><summary>📄 Abstract</summary>
  Laser processing has emerged as a transformative technology in the energy sector, enabling precise, efficient, and scalable solutions for energy generation, storage, and sustainability. This chapter explores the diverse applications of laser technology in energy applications. It begins with an overview of laser-driven inertial confinement fusion for energy production, highlighting key experimental facilities and crucial laser parameters. The role of lasers in solar energy harvesting is examined,...
  </details>

- **2026-11-16** — Tina Vartziotis, Ketevan Peranidze, Rodopi Kosteli et al. — [Re-Reading Is Not Free: Token Traces and Cache-Aware Energy Estimation for LLM Agents in Software Engineering](http://arxiv.org/abs/2611.20873v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve from conversational assistants into autonomous agents embedded in software development workflows, estimating their environmental footprint requires moving beyond conventional token-based accounting. Existing energy estimators focus on isolated request-response interactions, overlooking the repeated processing of accumulated context, cache reuse, and work delegated to subagents. We analyze nearly one billion tokens collected across 42 sessions and 752 task e...
  </details>

- **2026-11-16** — Xuening Wu, Haode Yang, Yanlan Kang et al. — [When Does Interaction Help? Toward a Reynolds Number for Collective Intelligence](http://arxiv.org/abs/2611.20773v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems combine distributed information through interaction, which can improve performance but also spread errors or suppress useful differences. Predicting when interaction helps is central to understanding and designing collective intelligence. We investigate whether a few dimensionless parameters can predict gains over explicitly defined non-communicating baselines across group sizes, network structures, and tasks, toward a Reynolds-number-like description of collective intelligen...
  </details>

- **2026-11-16** — Haixiang Wu, Zhihao Guan, Yang Yang — [ACiT: Proprioceptive-Prior Action Chunking with Inverted Transformers](http://arxiv.org/abs/2611.20719v1)
  <details><summary>📄 Abstract</summary>
  Visuomotor policies condition action prediction on visual and proprioceptive observations. While historical proprioceptive sequences carry rich dynamic priors, current methods treat them as equal to high-dimensional vision, causing the proprioceptive signal to be overwhelmed. To identify what is lost in equal-conditioning fusion, we analyze proprioceptive data and find that strong inter-joint coupling is the key action-determining structure. This finding aligns with the neural sensorimotor loop,...
  </details>

- **2026-11-16** — Sachin Gupta — [AgentFaultBench: State-Verified Evaluation of Tool-Fault Recovery](http://arxiv.org/abs/2611.20711v1)
  <details><summary>📄 Abstract</summary>
  Does recovery advice help an agent finish a task after a tool fails? AgentFaultBench evaluates LangGraph and CrewAI agents performing specified tasks in an isolated GitLab installation. We inject tool errors and check both the resulting files and issues and the required reads, verification and final response. The prompt supplies the expected issue and report text, so the task tests execution rather than content generation. In the primary comparison of 1,944 planned runs, advice changes success b...
  </details>

- **2026-11-16** — Fengmin Wu, Sicong Liu, Zimu Zhou et al. — [UbiHearo: Bringing Scenario-Aware Sound Guidance to DHH Users with Mobile Agents](http://arxiv.org/abs/2611.20686v1)
  <details><summary>📄 Abstract</summary>
  For Deaf and Hard-of-Hearing (DHH) users, effective sound awareness goes beyond detecting \emph{what} sound occurs; it requires understanding \emph{what it means}, \emph{how urgent it is}, and \emph{what to do}. However, existing mobile assistants largely reduce acoustic scenes to isolated labels or generic alerts, failing to provide contextual guidance when the same sound implies different risks across scenarios. We present \sysname, a mobile hearing assistant agent that closes the sensing--rea...
  </details>

- **2026-11-16** — Kangjie Zhou, Sukai Wang, Yuhan Xiao et al. — [Learning and Verifying Progress: Closed-Loop Agentic Planning with Progress-Enhanced Execution for Long-Horizon Vision-Language Navigation](http://arxiv.org/abs/2611.20676v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon vision-language navigation (VLN) requires agents to track instruction progress and recover from local errors before they propagate across subtasks. However, executors trained on expert trajectories encounter policy-induced state shifts during deployment, and their stop signals do not reliably indicate subtask completion. We introduce Learning and Verifying Progress for VLN (LeaP-VLN), an agentic VLN system that couples progress-aware execution with independent progress verification ...
  </details>

- **2026-11-16** — I. V. Solovyev — [Molecular-orbital origin of weak orbital ferromagnetism and anomalous Hall effect in a trimerized kagome antiferromagnet](http://arxiv.org/abs/2611.20632v1)
  <details><summary>📄 Abstract</summary>
  We reveal the molecular-orbital origin of weak orbital ferromagnetism and the anomalous Hall effect (AHE) induced by noncollinear spin order in a trimerized kagome lattice. By transforming to the molecular-orbital basis of an isolated trimer in the double-exchange regime, we derive an effective low-energy model for the states with opposite orbital angular momenta $m= \pm 1$ subject to an effective Zeeman field arising from spin chirality and spin-orbit (SO) coupling. In this representation, the ...
  </details>

- **2026-11-16** — Haipeng Wang — [A Self-Evolving Agent Runs Like a Gas: Describing and Predicting Its Evolution with Fluid Dynamics](http://arxiv.org/abs/2611.20584v1)
  <details><summary>📄 Abstract</summary>
  A self-evolving LLM agent improves in service by rewriting its own plugin library under a validation gate. Agent engineering is converging on exactly such agents: single systems in continuous operation, carrying populations of runtime instances (plugins, skills, tools) past the point where anyone can read the library and still predict what the system will do. Yet the run itself, the aggregate motion of that population across hundreds of edit rounds, is unstudied: no theory says whether it relaxe...
  </details>

- **2026-11-16** — Qianli Wang, Junchao Wu, Binkai Ou et al. — [ReconPotBench: Evaluating LLM Honeypots in Multi-Round Linux Reconnaissance](http://arxiv.org/abs/2611.20528v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to build interactive honeypots, yet existing evaluations mainly assess isolated command outputs and cannot determine whether a system remains believable when later commands depend on earlier results. We present ReconPotBench, a multi-round benchmark for Linux reconnaissance honeypots. It contains 1{,}032 three-round reconnaissance interactions across eight reconnaissance categories, with reference outputs collected from a real Linux environment....
  </details>

- **2026-11-16** — Murat Arda Onsu, Poonam Lohan, Burak Kantarci et al. — [VISTA: A Framework for Vision-Informed Semantic Traffic Awareness](http://arxiv.org/abs/2611.20458v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Things (IoT) is transforming intelligent transportation systems by connecting roadside cameras, edge computing units, vehicles, and traffic infrastructure into a shared sensing and decision-making ecosystem. However, transmitting raw traffic video over vehicle-to-everything (V2X) links is bandwidth-intensive, while deploying large multimodal models directly on resource-constrained vehicles is often impractical. To address these limitations, this article proposes VISTA (Vision-Inf...
  </details>

- **2026-11-16** — Vyom Agarwal, Mokshda Gangrade, Samet Ayhan et al. — [LEDGE: Separating Critic and Editor Failures in Text-to-Image Self-Correction](http://arxiv.org/abs/2611.20446v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) self-correction combines a vision-language model (VLM) critic that diagnoses errors and proposes instructions with an image editor that executes them. End-to-end evaluation obscures whether failures arise from incorrect diagnoses or an editor unable to execute valid instructions. We introduce LEDGE (Learning Error Diagnosis in Generation and Editing), a framework that separates these bottlenecks. LEDGE compiles oracle edit instructions from GenEval while holding the generated...
  </details>

- **2026-11-16** — Yujie Guo, Hongjie Chen, Jiaming Zhou et al. — [Learning from Distribution: Rethinking One-Hot Supervision for ASR and QA in Speech Language Models](http://arxiv.org/abs/2611.20436v1)
  <details><summary>📄 Abstract</summary>
  Speech language models (SLMs) exhibit strong capabilities in automatic speech recognition (ASR) and general-purpose speech understanding, yet ASR-specific training often degrades spoken question answering (QA) performance. We revisit this conflict from the perspective of task-specific input--output mappings and one-hot supervision. Our findings reveal pronounced task-asymmetric effects: ASR-only training severely limits QA capability, whereas QA-only training retains reasonable ASR performance. ...
  </details>

- **2026-11-16** — Sheng Xu, Aoduo Li, Rongli He — [Structure-Guided Multi-Granularity Spatiotemporal Transformer for Efficient Monocular 3D Human Pose Estimation](http://arxiv.org/abs/2611.20361v1)
  <details><summary>📄 Abstract</summary>
  Existing multi-granularity methods for monocular 3D human pose estimation emphasize spatial joint features while underusing skeletal structure, including global connectivity and temporal continuity. Moreover, modeling entire frame sequences incurs high computational costs. We propose a Structure-Aware Multi-Granularity Spatiotemporal Transformer that integrates structural priors across spatial and temporal representations for accurate and efficient pose estimation. A three-level feature extracto...
  </details>

- **2026-11-16** — Jingyuan Zhu, Biaolong Chen, Yangyang Qin et al. — [BlockAlign: Preference Optimization for Trajectory-Distilled Video Generation](http://arxiv.org/abs/2611.20351v1)
  <details><summary>📄 Abstract</summary>
  Directly aligning trajectory-distilled video generators slashes rollout costs and optimizes the deployed few-step model without teacher fine-tuning or re-distillation. However, conventional flow-matching preference objectives assume single-head local velocity supervision, mismatching the finite-interval, block-average transition interface of trajectory-distilled generators such as Parallel Decoding Distillation (PDD) and Parametric Trajectory Distillation (PTD). Naively supervising only the prim...
  </details>

- **2026-11-16** — Arunkumar V, Gangadharan G. R., S. Senthilkumar — [Reading or Remembering? Measuring Temporal Contamination in Language Models](http://arxiv.org/abs/2611.21554v1)
  <details><summary>📄 Abstract</summary>
  Language models are now used to read central-bank text for economic forecasting, but most were trained on text written after the documents they read. A model reading a 2021 FOMC statement may already know that inflation rose in 2022, so part of its apparent skill can be memory of the outcome, a temporal form of test-set contamination. We measure this memory on FOMC statements and minutes from 2000 to 2026 by comparing modern open models with chronologically consistent models, which are trained o...
  </details>

- **2026-11-16** — Vito Viesti, Alexander Streltsov — [Catalytic compression of classical communication in exact entanglement transformations](http://arxiv.org/abs/2611.21349v1)
  <details><summary>📄 Abstract</summary>
  Entanglement catalysis is usually associated with making otherwise impossible transformations possible. Here we show that it can also change how much classical communication a transformation requires. A catalyst, returned exactly and uncorrelated with the output, can reduce the message alphabet size required for exact transformations of bipartite pure states by a factor that grows without bound as the Schmidt rank increases. In the asymptotic many-copy regime, however, this advantage disappears ...
  </details>

- **2026-11-16** — Saray Bakker, Wendelin Böhmer, Javier Alonso-Mora — [Cooperative Mobile Manipulation using Learned Dynamical Systems](http://arxiv.org/abs/2611.21198v1)
  <details><summary>📄 Abstract</summary>
  Cooperative mobile manipulation requires robots to coordinate their motions while ensuring whole-body collision avoidance and preserving task-relevant behaviors. We propose CALDS (Cooperative Adaptation of Learned Dynamical Systems), a framework that enables mobile manipulators to adapt learned single-agent behaviors for coordinated execution. Building on individual dynamical systems (DSs) learned from demonstrations, CALDS enables cooperative adaptation through two key components: Cooperative P...
  </details>

- **2026-11-16** — Ke Sun, Kevin Yuchen Ma, Yike Zhang et al. — [ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models](http://arxiv.org/abs/2611.21099v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal models can now control robots zero-shot from images, yet many manipulation tasks depend on contact forces that images cannot show. Bringing force to an API-only frozen model raises two challenges. First, contact evolves much faster than an API model can decide, so the system must close the loop on force beneath the model. Second, a frozen model cannot interpret raw force streams, so force must be returned in a form the model can reason about. Therefore, we present ForceHarnes...
  </details>

- **2026-11-16** — Yisong Cao, Leah Kim, Brian Wright et al. — [Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering](http://arxiv.org/abs/2611.21586v1)
  <details><summary>📄 Abstract</summary>
  Job titles and job descriptions alone provide limited insight into how technical roles differ in a changing job market. To assess how such roles differ in their work and industry applications, we design and compare two methods based on deep learning and transformer representations using 36,081 early-career job postings collected from LinkedIn in the United States between December 2025 and October 2026.   We first apply PERC, short for Preprocessing (P), Embedding (E), Dimensionality Reduction (R...
  </details>

- **2026-11-16** — Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. et al. — [Procedure without Judgment: What Small Language Models Learn under an Exact Verifier](http://arxiv.org/abs/2611.21529v1)
  <details><summary>📄 Abstract</summary>
  When an authorization policy blocks an agent's tool call, the audit log should name the facts that forced the decision and nothing more. For an executable policy over an enumerable context space this minimal sufficient reason can be computed exactly, so an explanation is scored against ground truth rather than a proxy for it. We use that exactness to ask what a model can learn from a verifier that has no error in it. The explainer sees one request and one decision, never the policy, and has thir...
  </details>

- **2026-11-16** — Jerry Lin, Elizabeth A. Barnes — [Run it Back: Autoregression vs. Video Diffusion for Final-Conditioned Weather Trajectories](http://arxiv.org/abs/2611.21521v1)
  <details><summary>📄 Abstract</summary>
  Low-likelihood, high-impact extremes are projected to increase in severity and frequency in a warming climate. Sampling the precursors that lead to these events traditionally requires massive ensembles that scale poorly with lead time and rarity, and typical rare-event sampling and ensemble-boosting methods do not show how a single extreme might arise from diverse synoptic precursors. Recently, Lin et al.\ (2026) showed this is possible with final-conditioned 66-hour trajectories (trajectories c...
  </details>

- **2026-11-16** — Srinath Srinivasan, Tim Menzies — [Beyond Leaderboard Ranks: Selecting Software Engineering Agents Under Budget Constraints](http://arxiv.org/abs/2611.21515v1)
  <details><summary>📄 Abstract</summary>
  Teams that adopt LLM agents for issue resolution must decide which agent to pay for, and how much to spend finding out. Leaderboard ranks give weak evidence for this decision. Accuracy differences may be statistically unresolved, reported costs may be inconsistent, and evaluating candidate agents can itself be expensive. We investigate budget-constrained agent selection using 58,197 run--task records extracted from the Holistic Agent Leaderboard (HAL), focusing on SWE-bench and six additional be...
  </details>

- **2026-11-16** — Jacky Kumar — [A Reinforcement Learning Method to Navigate SMEFT Operator Space](http://arxiv.org/abs/2611.21439v1)
  <details><summary>📄 Abstract</summary>
  In particle physics, discrepancies between experimental measurements and Standard Model (SM) predictions are commonly interpreted within new theoretical models. In this context, the Standard Model Effective Field Theory (SMEFT) provides a general framework encompassing a broad class of models. However, exploring the enormous space of possible SMEFT operators rapidly becomes a challenging combinatorial problem: many operators can contribute simultaneously to different observables, their effects a...
  </details>

- **2026-11-16** — Aniket Murhekar — [A Polynomial-Time Algorithm for Constant-Factor EFX Allocations of Chores](http://arxiv.org/abs/2611.21387v1)
  <details><summary>📄 Abstract</summary>
  We study the fair division of indivisible chores among agents with additive disutilities, focusing on the central fairness notion of envy-freeness up to any chore (EFX), and its multiplicative approximations. Although the existence of constant-factor approximations to EFX are known, computing such an allocation in polynomial time remained open. We resolve this question by giving an algorithm that, for every $\varepsilon\in(0,1)$, computes a $(3+\varepsilon)$-EFX allocation in time polynomial in ...
  </details>

- **2026-11-16** — Suchit Gupte, Zhongteng Cai, Xueru Zhang et al. — [Representational Change Under Self-Consuming Training: A Sparse Autoencoder Analysis](http://arxiv.org/abs/2611.21348v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly exposed to model-generated text, raising the possibility that future models will be trained recursively on the outputs of their predecessors. Prior work on such self-consuming training loops has largely focused on output quality and downstream performance, leaving their effects on internal representations poorly understood. We study how representations evolve across five generations of self-consumption and whether sparse autoencoders (SAEs) remain reliable ...
  </details>

- **2026-11-16** — Ondřej Tichý, Anna Marklová, Barbora Bulantová et al. — [Benchmarking Large Language Models for Linguistic Annotation](http://arxiv.org/abs/2611.21291v1)
  <details><summary>📄 Abstract</summary>
  Assessing large language models for linguistic annotation requires task-specific evaluation under documented conditions. We present dhAIBench, a Python benchmarking and annotation tool with a web interface for exploring and sharing results. It records prompts, configurations and predictions, enabling comparisons of annotation quality, confidence calibration, repeatability and estimated cost. We demonstrate the framework and the associated methodology through 293 runs of 48 models on nine linguis...
  </details>

- **2026-11-16** — Ayman Farahat — [Who Is the Regression About? Auditing AI-Labeled Treatments When Effects Differ](http://arxiv.org/abs/2611.21207v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly regress outcomes on treatments labeled by large language models. When effects differ, OLS averages the effect on the treated (ATT) and on the untreated (ATU), weighting the smaller group more. A label's bias then has two parts: classical attenuation from misclassification, and a selective term when its errors are correlated with the outcome. In LinkedIn postings, the model misses better-paid remote jobs: a precision check passes, yet the remote pay gap is understated by ...
  </details>

- **2026-11-16** — Dan Yuan, Yue Wen, Zhili He et al. — [CivilBench: Benchmarking Vision-Language Models for Multimodal Information Integration in Civil Engineering](http://arxiv.org/abs/2611.21105v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI), particularly large language models (LLMs) and vision-language models (VLMs), is increasingly applied in civil and structural engineering for disaster assessment, structural analysis, and engineering decision support. However, the extent to which current VLMs possess the reasoning capabilities required for reliable engineering judgments remains unclear. In this work, we introduce CivilBench, a comprehensive benchmark for evaluating VLMs in civil engineering and disas...
  </details>

- **2026-11-16** — Mitsumasa Wada — [Digits in Notation Are Not Numbers: A Scoring Pitfall in PDF-to-Markdown Conversion of Japanese Technical Documents (Preliminary Evaluation)](http://arxiv.org/abs/2611.20993v1)
  <details><summary>📄 Abstract</summary>
  Converting PDFs to Markdown is now routine preprocessing for search and language models, yet scoring the numbers in the output is easy to get wrong. We evaluate MinerU, a plain-text OCR baseline (NDLOCR-Lite), and a deterministic post-processing pipeline (anchor insertion, footnote reordering, fixes of look-alike characters in fixed contexts, gated formula repair using two independent OCR partners, and heading reconstruction) on 48 public Japanese pages (three documents), text-layer and rasteriz...
  </details>

- **2026-11-16** — Yunrong Hao, Ruohao Dai, Zhen Liu et al. — [FH-Sampling: Frequency-aware Hypergraph-driven Oversampling for Imbalanced Time-Series Classification](http://arxiv.org/abs/2611.20991v1)
  <details><summary>📄 Abstract</summary>
  Imbalanced time-series data appears commonly in diverse applications, such as medical diagnosis. When trained on imbalanced data, classifiers tend to exhibit a bias toward the majority class, making it difficult to identify minority-class instances accurately, despite their critical importance. Sampling techniques have proven effective in rebalancing imbalanced data. However, existing interpolation-based oversampling methods typically rely on pairwise interpolation, limiting their ability to cap...
  </details>

- **2026-11-16** — Laishram Rahul, Shruthi B. S., Parismita Gogoi et al. — [Layer-wise Linear Probing of an Encoder-free Audio-capable Language Model](http://arxiv.org/abs/2611.20954v1)
  <details><summary>📄 Abstract</summary>
  Encoder-free audio-capable multimodal language models pro- vide a unique setting for studying how speech representations emerge inside a language-model decoder. In Gemma-4-12B, short waveform frames are projected directly into the shared embedding space, and all subsequent contextual processing is performed by the decoder layers. We use this architecture to examine where acoustic, phonetic, segmental, and paralinguis- tic information becomes linearly accessible across depth. Us- ing the TIMIT co...
  </details>

- **2026-11-16** — Kevin Kam Fung Yuen — [Advancing Cognitive Pairwise Comparisons for Human-Centric Artificial Intelligence and Data Science: A Human-in-the-Loop Framework](http://arxiv.org/abs/2611.20926v1)
  <details><summary>📄 Abstract</summary>
  Human-centric artificial intelligence and data science (HCAD) systems increasingly involve human-in-the-loop (HITL) interventions to overcome the limitations of fully automated machine learning algorithms, such as automation bias and the inability to incorporate tacit domain knowledge, and continuously improve predictive performance. Data transformations, feature selection, feature weighting, and model selection usually require laborious human involvement across iterations of artificial intellig...
  </details>

- **2026-11-16** — Mika Facchini — [Auditing a Moving Target: Evidence Anchoring and the Expiry of Fairness Audits of Provider-Served Language Models](http://arxiv.org/abs/2611.20901v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly use large language models (LLMs) for decisions about people, such as hiring, investment and employee evaluation, and rely on them over long periods of time. Fairness audits of such systems, however, are conducted only once. We examine how the biases of LLMs change over time. In a venture screening setting, models from five providers decided whether and how much to invest in startups whose founders differed only in gender, origin and university. We repeated this audit t...
  </details>

- **2026-11-16** — Simon Mackenzie, Mashbat Suzuki — [Nearly Settling the Complexity of Connected $\varepsilon$-Envy-Free Cake Cutting](http://arxiv.org/abs/2611.20890v1)
  <details><summary>📄 Abstract</summary>
  Envy-free cake cutting has been one of the central problems in fair division. In cake cutting, agents' preferences over the cake are accessed through Robertson--Webb (RW) queries. For three or more agents, no algorithm that makes finitely many RW queries can always find a contiguous, exactly envy-free allocation. For contiguous $\varepsilon$-envy-free allocations, however, Hollender and Rubinstein~(JACM, 2025) showed that $\poly(\log(1/\varepsilon))$ RW queries suffice for four agents, leaving o...
  </details>

- **2026-11-16** — Prem Kumar, Alina Boecker, Glenn van de Ven et al. — [Orbital decomposition and evolution of LEGA-C-like galaxies in IllustrisTNG from z = 1 to z = 0](http://arxiv.org/abs/2611.20884v1)
  <details><summary>📄 Abstract</summary>
  Stellar orbits encode the dynamical history of galaxies and provide a physically motivated link between galaxy structures and assembly processes. Although orbit-based decompositions are well established in the Local Universe, their evolution across cosmic time, especially at higher redshifts, remains poorly explored. We investigate the orbital structure of \texttt{LEGA-C-like} galaxies in the \texttt{TNG100} simulation from $z=1$ to $z=0$ to identify how stellar mass, star formation activity, en...
  </details>

- **2026-11-16** — Christophe Denis — [Conversing with a Conversational Agent: A Real Conversation, Not a Simulated One](http://arxiv.org/abs/2611.20826v1)
  <details><summary>📄 Abstract</summary>
  The claim that interactions with artificial conversational agents merely simulate human conversation rests on a philosophical distinction between reproducing the observable features of an activity and actually performing it. Although this distinction is appropriate for certain physical phenomena, its application to linguistic and symbolic activities is far less straightforward. This article argues that conversations with large language model (LLM)-based agents are genuine conversational activiti...
  </details>

- **2026-11-16** — Abbas Sani — [Medical question answering collapses in Hausa: a pre-registered pilot on three small open models](http://arxiv.org/abs/2611.20823v1)
  <details><summary>📄 Abstract</summary>
  A system that reads nothing and always answers the most frequent letter scores \BaselineP{} on our Hausa medical multiple-choice set. \NBelowBaseline{} of the \NModels{} small open models we evaluate do not beat it. We lead with that because the usual summary of a multilingual result -- a percentage-point drop from English -- does not say whether what survives the drop is performance at all.   On a paired English--Hausa set of \NEval{} MedMCQA items, three instruction-tuned models of 3--4B param...
  </details>

- **2026-11-16** — Mike Hänseroth, Niklas Wahlström, Thomas B. Schön et al. — [Conditional Diffusion Models for Amortized Bayesian System Identification](http://arxiv.org/abs/2611.20666v1)
  <details><summary>📄 Abstract</summary>
  Generative diffusion models rapidly solve Bayesian inverse problems, such as image restoration and inpainting, with a single trained model and without retraining for each new observation or task. Bayesian system identification, which typically involves inferring the hidden states and parameters of a dynamical system from measurements, poses a closely related inverse problem. Yet it is often addressed with computationally heavy Monte Carlo methods that must be rerun for every new measurement reco...
  </details>

- **2026-11-16** — Michael Kingston, Sonit Singh, Alan Blair — [Instrumenting Failure: Scoring Language Model Agents at Every Decision Node in Imperfect-Information Games](http://arxiv.org/abs/2611.20644v1)
  <details><summary>📄 Abstract</summary>
  Agent evaluations report task success and rarely say what an agent did at each decision. We score every decision node of three 12B to 14B instruct-tuned language models (LMs) playing five zero-sum imperfect-information games against four opponents on eight properties from decision and game theory, five of them against a CFR+ equilibrium reference. At each node, the LM also states a belief about the opponent's hidden state in a separate call. Without memory and at temperature 0, stated beliefs si...
  </details>

- **2026-11-16** — Haipeng Wang — [RemeshingAgent: An Iterative Agent for Repair-Based Decimation of Generated Building Meshes](http://arxiv.org/abs/2611.20533v1)
  <details><summary>📄 Abstract</summary>
  Aggressively simplifying a generated high-poly building mesh to 0.5-1% of its faces confronts a hard limit. The surface looks complete, yet the mesh is topologically shattered: 10^3-10^4 connected components and non-manifold thin walls. Below a certain budget, every practical decimator "melts": it deletes parts, welds thin walls, or breaks the error tolerance. We attribute this to instance-specific pathology: which components are significant and where the cliff sits vary from mesh to mesh, so no...
  </details>

- **2026-11-16** — Manjit Singh — [On the equivalence of three extended Calogero--Bogoyavlenskii--Schiff models to the classical CBS equation](http://arxiv.org/abs/2611.20495v1)
  <details><summary>📄 Abstract</summary>
  We examine the three extended Calogero--Bogoyavlenskii--Schiff (CBS) models introduced by Wazwaz, Alhejaili, and El-Tantawy [Eur.\ Phys.\ J.\ Plus \textbf{141}, 1218 (2026)]. Explicit invertible point transformations map the first model, and generically the second, to the classical CBS equation. The third model is generically equivalent to CBS with an additional spectator coordinate absent from the differential operator. We identify the exceptional parameter regimes and explain the reported expo...
  </details>

- **2026-11-16** — Siqiao Xue, Ziyin Zhang, Zihan Liao et al. — [Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search](http://arxiv.org/abs/2611.20455v1)
  <details><summary>📄 Abstract</summary>
  Code-search benchmarks show dense encoders well ahead of BM25, yet coding agents do well with \texttt{grep}. What does this dense advantage measure? Existing benchmarks cannot tell: they use curated queries, old code and a handicapped BM25. To find out, we build Repo-Premium, a realistic repository-level code-search benchmark. It ranks files in real repositories, with curated and raw queries in Python, JavaScript, TypeScript, Go, Rust and Java, pull requests from 2022 to 2026, and a preregistere...
  </details>

- **2026-11-16** — Haiyang Jiang, Tong Chen, Xinyi Gao et al. — [MAGE: Meta-path Adaptive Graph Evidence for Transferable Multimodal Graph Learning](http://arxiv.org/abs/2611.20449v1)
  <details><summary>📄 Abstract</summary>
  Multimodal graphs integrate textual and visual attributes with relational structures, providing a rich representation of complex real-world data. To enable the broad applicability and reuse of graph models, it is crucial for models trained on source graphs to generalize to unseen graph domains. However, this is challenging because cross-modal interactions among neighbors and the neighboring information needed for prediction can vary across target nodes and graph domains. This gives rise to two k...
  </details>

- **2026-11-16** — Karl Vilhelmsson Emneby, Julian Yocum, Cameron Allen — [Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features](http://arxiv.org/abs/2611.20371v1)
  <details><summary>📄 Abstract</summary>
  Linear probing is a common technique in mechanistic interpretability despite the fact that the decodability of a given feature does not necessarily imply the network uses that feature. Intervention faithfulness, not merely decodability, is the appropriate criterion for whether a feature serves a defined active role in the model. Meanwhile, probe regularization has been used for feature discovery, but the impact of regularization on feature causality remains unclear. We study probe regularization...
  </details>

- **2026-11-15** — Silei Ren, Hanxi Chen, Suraaj Kanniwadi et al. — [Type-Confusion Security](http://arxiv.org/abs/2611.20298v1)
  <details><summary>📄 Abstract</summary>
  Type systems are a lightweight way to obtain formal assurance that code upholds security properties. However, decentralized systems, such as smart contracts and Model Context Protocol ecosystems, have limited ability to constrain the behavior of untrusted code. In such systems, attackers may attempt to confuse trusted code by supplying values that do not behave according to their advertised types, an attack that we call type confusion. Well-known attacks such as confused deputy attacks, reentran...
  </details>

- **2026-11-15** — Juan Carlos García Escartín — [A Bleichenbacher bit-by-bit oracle attack from partial message knowledge](http://arxiv.org/abs/2611.20277v1)
  <details><summary>📄 Abstract</summary>
  Oracle attacks show the importance of a correct implementation of cryptographic standards when translated into code. A notable example is the Bleichenbacher attack on RSA with PKCS#1 v1.5 padding and all the improvements that have been suggested over the decades. This paper shows how an attacker knowing a few least significant bytes of an RSA message can take advantage of a server with an oracle side-channel to decrypt the full message bit by bit. We will consider two oracles that can be tested ...
  </details>

- **2026-11-15** — Quy-Anh Dang, Chris Ngo — [Centered Ablation: Why Last-Layer Directional Ablation Under-Fires or Collapses, and a Closed-Form Fix](http://arxiv.org/abs/2611.20148v1)
  <details><summary>📄 Abstract</summary>
  Directional ablation removes a hidden state's component along a "behaviour direction" while a language model runs. It is the standard way to switch a behaviour such as refusal off, but it is erratic: on some models it barely fires, on others the text collapses into repetition. We show why, and fix it. At the last residual stream, ablation is exactly a logit bias: a fixed vocabulary footprint scaled by a gate, the cosine between the hidden state and the direction. The gate is measured from the or...
  </details>

- **2026-11-15** — Chenhao Tong, Steffen Müller — [Infrastructure-Based Multi-Agent Reinforcement Learning with Attention for Highway Ramp Merging](http://arxiv.org/abs/2611.20078v1)
  <details><summary>📄 Abstract</summary>
  On-ramp merging is a typical safety and throughput problem on highways. Without proper coordination, human drivers and self-interested autonomous vehicles may make risky manoeuvres and cause accidents or congestion. With recent advances in connected autonomous vehicles (CAVs) and multi-agent reinforcement learning (MARL), vehicles can be trained to coordinate for safe and efficient merging. However, in dense traffic, forming an effective observation of the traffic state is challenging. For examp...
  </details>

- **2026-11-15** — Michael W. Asher, Meng Cao, Paulo F. Carvalho — [Turning Errors into Successes: Designing LLM Tutoring Around Scaffolded Error Correction](http://arxiv.org/abs/2611.20061v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) could make personalized tutoring available at scale, but it remains unclear how they can best support the instructional processes that make one-on-one instruction effective. We compared two ways of using LLMs after students make errors: providing personalized explanations of those errors, or engaging students in additional cycles of scaffolded practice and feedback, with a Socratic tutor guiding students toward the correct answer. In a preregistered online experiment...
  </details>

- **2026-11-15** — Ahmad Alfan Alfian Irfan, Nur Ahmad Khatim, Mansur Arief — [D'BEAST: Logged Bad Experiences as Explanation for Autonomous Driving Agents](http://arxiv.org/abs/2611.20019v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning agents learn from mistakes, yet their decisions can be difficult to trace back to those experiences. We investigate whether a tabular agent's decisions can be explained by its bad experiences, defined as the training transitions associated with safety or task events. A fixed training log is replayed from the same initial Q-table under three conditions. FULL retains all updates, SKIP omits bad-experience updates, and NEUTRALIZE retains those updates without their event pena...
  </details>

- **2026-11-15** — Okenla AbdulQahhar Abimbola, Maurice Abraham John, Adepoju Jeremiah Moyondafoluwa et al. — [Offline-First Quantized AI: Design and Evaluation of an On-Device Maternal-Health Assistant for Low-Connectivity Environments](http://arxiv.org/abs/2611.20012v1)
  <details><summary>📄 Abstract</summary>
  Offline language models could extend access to maternal-health information where internet connectivity is unreliable, but deployment requires both clinically appropriate responses and feasible local execution. This study presents an offline Android assistant integrating ready-made quantized language models, a clinically validated local knowledge package, conversational context, and model-initiated local retrieval. Gemma 4 E2B and Qwen3.5 0.8B were compared across 45 conversations and 312 turns p...
  </details>

- **2026-11-15** — Nikos Theodoridis, Reenu Mohandas, Sushil Sharma et al. — [ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?](http://arxiv.org/abs/2611.20011v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) and World-Action Models (WAMs) have emerged in autonomous driving with the promise of strong generalization to long-tail scenarios. Although these models achieve state-of-the-art results on autonomous driving benchmarks, most existing benchmarks are dominated by nominal scenarios and therefore cannot test this promise. To test one such long-tail capability that is critical for safety, we introduce ReactBench-AD, a benchmark that measures how driving models re...
  </details>

- **2026-11-15** — Lindong Xie, Xiexin Zou, Yang Zhang et al. — [CoSyDelay: Cognitive Symbolic Regression for Traffic Delay Estimation](http://arxiv.org/abs/2611.19946v1)
  <details><summary>📄 Abstract</summary>
  Trustworthy estimation of traffic delays at signalized intersections is critical for modern transportation systems, as it supports proactive traffic control for congestion mitigation. Existing analytical methods often rely on idealized assumptions that limit their accuracy under complex traffic conditions, whereas data-driven methods may achieve strong estimation performance but usually lack transparent structures, which reduces confidence in their practical application. To address these limitat...
  </details>

- **2026-11-15** — Chengzhi Gao, Yongzhi Liu, Jinchang Xu et al. — [Lao Siji: Adapting openpilot to Closed-Loop End-to-End Driving in Neural Reconstruction](http://arxiv.org/abs/2611.19922v1)
  <details><summary>📄 Abstract</summary>
  We present Lao Siji, an end-to-end driving policy that ranks third in the 2026 NVIDIA AlpaSim E2E Driving Challenge, ahead of most entries built on foundation models. Instead of training from scratch on a general-purpose vision backbone, we adapt openpilot, an open-source L2 production model. We freeze its vision encoder and fine-tune the policy layers with an ego-state adapter and a route memory. On closed-loop rollouts in neural-reconstructed scenes, we supervise the policy with a privileged m...
  </details>

- **2026-11-15** — Seunghyun Lee, Jaehui Hwang, Dongyoon Han et al. — ["Don't Leave the Task Unfinished": Persistence-Driven Violations under Quiet Oversight](http://arxiv.org/abs/2611.19911v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly given long, multi-step tasks to carry out, with the user reviewing little of what happens in between. Persistence, the tendency to keep working until a task is complete, is installed on purpose to improve performance on long tasks. Long-horizon tasks are typically complex, and the user's instruction can fall short of what the work actually requires, or conflict with the constraints the agent encounters in the task. We study what persistence does on long-horizon operat...
  </details>

- **2026-11-15** — Yichen Zhang, Zihan Wang, Hao Chen et al. — [Beyond Vehicle-Centric Data: Scaling Autonomous Driving through Roadside-to-Vehicle Generation](http://arxiv.org/abs/2611.19830v1)
  <details><summary>📄 Abstract</summary>
  Training autonomous driving models requires large and diverse datasets, collected primarily by vehicles. Scaling them entails investment in fleet operation, data processing and annotation. Road infrastructure records traffic and multi-vehicle interactions, yet the viewpoint gap between roadside and onboard sensors limits its direct use for training. Here we introduce AnyR2V, a framework that transforms multimodal roadside observations into seven-camera surround-view videos for different vehicle ...
  </details>

- **2026-11-15** — Jing Wang, Shengkai Li, Trung V. Phan et al. — [Field-Driven Active Matter Physics and Material Applications](http://arxiv.org/abs/2611.19806v1)
  <details><summary>📄 Abstract</summary>
  Active matter consists of energy-consuming units that generate motion, making it a powerful platform for exploring nonequilibrium physics and engineering adaptive materials. Robotic active matter brings this physics into programmable, macroscopic agents with controllable actuation, sensing, and response, but its scalability is limited by onboard power, communication, and control complexity. Field-driven active matter addresses these limitations by shifting part of the control burden from individ...
  </details>

- **2026-11-15** — Pronoma Banerjee, Md. Masudur Rahman, Juan P. Wachs — [Read Before You Fit: Text-Derived Constraints for Discovering Differential Equations from Noisy Biological Data](http://arxiv.org/abs/2611.19779v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used for scientific equation discovery. However, most existing methods are strongly data-driven and assume sufficiently clean and representative observations. This assumption is problematic in biological systems, where individual-level measurements are often sparse, noisy, heterogeneous, and expensive to obtain. While the underlying mechanisms are extensively described in scientific text, they are not explicitly used for the LLM based modeling of such syste...
  </details>

- **2026-11-15** — Yi Zeng, Jianjun Dong — [Hidden Heat-Current Transport Channels Behind Observable Temperature Dynamics](http://arxiv.org/abs/2611.19776v1)
  <details><summary>📄 Abstract</summary>
  Diffusive decay and wave-like oscillations in temperature dynamics are commonly used to characterize heat conduction, yet these signatures do not uniquely identify the underlying heat-current transport mechanisms. Here we reveal a spectrum of constitutive heat-current channels whose microscopic organization can change without a corresponding qualitative change in observable temperature dynamics. We develop a two-level spectral theory that first resolves the finite-wave-vector constitutive respon...
  </details>

- **2026-11-15** — S M Mahbub Murshed — [StaleBench: Isolating Stale Retrieval in Agent Memory, and Pricing the Fix](http://arxiv.org/abs/2611.19752v1)
  <details><summary>📄 Abstract</summary>
  An agent that stores facts over time eventually stores several versions of the same fact. Asked a value-agnostic question - "which team does X play for now?" - a similarity retriever cannot prefer the current version, because every version matches the entity the query names. StaleBench isolates this stale-retrieval failure on 892 real updating facts, with currency labels from the source (Wikidata validity years via TempLAMA), never from a retrieval score. Our central result is that retrieval met...
  </details>

- **2026-11-15** — Liuyi Xu, Qing Wang, Zikai Liang et al. — [SEAT: Sign-Type Evidence-Audited Transport for Multi-Label Tongue Diagnosis](http://arxiv.org/abs/2611.19748v1)
  <details><summary>📄 Abstract</summary>
  Automated tongue-sign recognition can improve the consistency of non-invasive examinations that otherwise rely on subjective visual judgment. A single tongue image often exhibits multiple coexisting signs characterized by heterogeneous evidence, including localized morphology, global chromaticity, and inter-label dependence. However, existing methods typically rely on shared representations and uniform multi-label heads, making it difficult to verify whether predictions stem from clinically rele...
  </details>

- **2026-11-15** — Ruichen Deng, Qinyu Zhao, Yong-Hyun Park et al. — [NF-VLA: A Normalizing-Flow Baseline for Vision-Language-Action Learning](http://arxiv.org/abs/2611.20314v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive normalizing flows (NFs) provide a tractable density for learning and sampling continuous robot actions. We show that a single maximum-likelihood objective can train vision--language--action (VLA) policies competitive with leading methods on manipulation benchmarks. We present NF-VLA, which combines conditional autoregressive normalizing flows with score-based action refinement. Its deep--shallow architecture concentrates visual, language, and proprioceptive prefix conditioning in ...
  </details>

- **2026-11-15** — Beining Han, Jia Deng — [DAPPT: Domain-Aware Policies from Procedural Trajectories for Sim-to-Real Dexterous Tool Use](http://arxiv.org/abs/2611.20202v1)
  <details><summary>📄 Abstract</summary>
  Sim-to-real RL has achieved impressive results in dexterous manipulation but remains limited to tasks with accurate rigid-body simulation. However, these methods cannot be applied to skills that involve deformable and particles, with which the simulation speed will become too slow for large-scale RL learning. We present DAPPT, a sim-to-real framework for end-to-end dexterous tool-use manipulation skills, e.g., sand scooping, play-dough rod-rolling, without simulating non-rigid materials. Our met...
  </details>

- **2026-11-15** — Shi Bin Hoo, Magnus Buehler, Omar Swelam et al. — [Weights & Caches: LLMs Can Program Tabular Foundation Models](http://arxiv.org/abs/2611.20174v1)
  <details><summary>📄 Abstract</summary>
  Neural networks are typically programmed through optimization, rather than by explicitly specifying their computations. Recent work on weight-space programming suggests that large language models (LLMs) can instead reason about and manipulate neural-network weights directly. In this work, we show that LLMs can directly program statistical computations in tabular foundation models (TFMs), whose parameters enable inference across different datasets. We investigate three complementary settings usin...
  </details>

- **2026-11-15** — Ziqiang Liu, Xitong Chen, Min Li et al. — [EgoSwarm: Learning Decentralized Robot Swarm Intelligence from Human Swarm Demonstrations](http://arxiv.org/abs/2611.20100v1)
  <details><summary>📄 Abstract</summary>
  Advancing from individual embodied intelligence to swarm embodied intelligence is a key step toward scalable, general-purpose embodied intelligence. Complex tasks often require multiple agents to divide responsibilities, coordinate handovers, and manipulate shared objects collaboratively. However, existing robot learning methods rely primarily on individual demonstrations, which provide limited supervision for modeling dependencies among agent actions, while collecting multi-robot demonstrations...
  </details>

- **2026-11-15** — Bang Xiao, Rodolfo Cossovich — [VoiceGuard: An Audio-Native LLM-VLA Pipeline for Wheelchair-Mounted Assistive Manipulation](http://arxiv.org/abs/2611.19984v1)
  <details><summary>📄 Abstract</summary>
  Wheelchair-mounted robotic arms can help people with limited upper-limb mobility reach and manipulate everyday objects, but operating them typically requires stepwise joystick control and frequent mode switching. Natural-language interfaces could let users express task-level goals, yet they must handle ambiguous requests, distinguish commands from nearby conversation, and support interruption. We present VoiceGuard, a voice interface that separates spoken intent from robot execution through stru...
  </details>

- **2026-11-15** — Lixin Xu, Ke Zhang, Xinyu Liu et al. — [DexFormer 2.0: Towards a Cross-Embodiment Foundation Policy for Dexterous Grasping](http://arxiv.org/abs/2611.20273v1)
  <details><summary>📄 Abstract</summary>
  Dexterous grasping policies are usually trained for one arm paired with one hand. Every new pairing then needs its own policy, and the number of policies grows with every arm and hand added. We ask whether a single policy can control many arm-hand combinations and transfer to pairings and hands it has never seen. This is hard because robots differ in the number, layout, and dynamics of their joints, so their observations and actions share no common interface. We present DexFormer 2.0, a single r...
  </details>

- **2026-11-15** — Dr Gabriel Borrageiro — [Markets for Compute and Inference: Structure, Financing, and Risk Transfer](http://arxiv.org/abs/2611.20242v1)
  <details><summary>📄 Abstract</summary>
  Capacity to run large language models is rented by the accelerator-hour, and their output is sold by the million tokens. Both goods now have published price indices, an over-the-counter forward has traded on one, a perpetual future on one is listed offshore, and CME and ICE have specified futures on rental indices that await the United States regulator. We ask what in these two markets can be hedged, by whom, and at what price. Three findings stand out. First, the price that exchange contracts s...
  </details>

- **2026-11-15** — Marek Šuppa, Jaroslav Kopčan — [Do We Still Need Fine-Tuned Classifiers? Swapping Typed Decision Models into 24 ACL-Venue Papers](http://arxiv.org/abs/2611.20191v1)
  <details><summary>📄 Abstract</summary>
  Typed Decision Models such as TypeSafe's Jev, also called System One or System 1 models, answer typed questions about an input with a probability for each option, and they need no training. Many NLP papers still fine-tune a task-specific classifier, and prompted large language models (LLMs) trail such classifiers on most text classification benchmarks. We ask how many of these fine-tuned classifiers a Typed Decision Model can replace under each paper's own evaluation, and what is needed where it...
  </details>

- **2026-11-15** — Alexandre Audibert, François Portet, Benoit Favre et al. — [FRAAC: A French Multimodal Large Language Model and Dataset forPictogram-Based Augmentative and Alternative Communication](http://arxiv.org/abs/2611.20094v1)
  <details><summary>📄 Abstract</summary>
  Pictograms are a core modality in augmentative and alternative communication (AAC), yet recent multimodal large language models (MLLMs) cannot reliably interpret or produce pictogram sequences. Two obstacles explain this gap: the absence of a standardized pictogram grammar and the scarcity of parallel text-pictogram data. We introduce Retrieval-Augmented Pictogram Selection (RAPS), an annotation method that refines a rule-based transcription system's output with LLM-based concept extraction and ...
  </details>

- **2026-11-15** — Martin Schroder — [The Frontier Must Grow - Self-proposed, interpreter-labelled training roughly doubles a 4B model's accuracy on a fresh exam as its verified frontier grows](http://arxiv.org/abs/2611.20049v1)
  <details><summary>📄 Abstract</summary>
  A model can learn from problems it poses itself when an executable oracle supplies the answers. Qwen3-4B proposed Lua 5.1 programs; those it predicted wrong at least once in four samples joined a pool labelled by the interpreter, each round adding twice as many programs as the last (300, 900, 2100 in total), and each round trained a fresh adapter from the base on the pool. On the original exam the procedure met its registered criterion, an item-level test of each adapter against its predecessor....
  </details>

- **2026-11-15** — Mahesh Reddy Pagadala — [When Zero Is Competitive: A Descriptive Pilot of Transformer and Gate-Graph Surrogates on Random-Angle Quantum Circuits](http://arxiv.org/abs/2611.19985v1)
  <details><summary>📄 Abstract</summary>
  We examine supervised classical prediction of all one-qubit Z and two-qubit ZZ expectation values on noiseless, layered 4-10-qubit RX/RY/RZ-CNOT circuits. In a 63-cell stratified workload with disjoint circuit-template tests, we evaluate one transformer encoder and gate-dependency graph neural networks against literal-zero and training-derived constant predictors. On the Arm K training labels, 44.89% of scalar targets have absolute magnitude below 0.05. The held-out-template zero predictor has e...
  </details>

- **2026-11-15** — Achintya Yadav — [Does synthetic pre-training pay off on a microcontroller? Accuracy, latency and energy across two MCUs](http://arxiv.org/abs/2611.19931v1)
  <details><summary>📄 Abstract</summary>
  Rendered images are cheap to label, but a microcontroller classifier must survive 8-bit integer (INT8) quantisation and compute correctly on the chip. Five models, from MobileNetV2 at 224 px to a 61K-parameter convolutional neural network (CNN), were fine-tuned on a six-class scene dataset with and without a synthetic stage, against thresholds fixed in advance, and deployed on an ESP32-S3 and an RP2040. With full real data the stage gave no detectable gain. For the main deployable model the INT8...
  </details>

- **2026-11-15** — Zhen Jia, Xinghong Hou, Chenyang Jin — [A Demonstration System for Faithful Temporal Question Answering](http://arxiv.org/abs/2611.19926v1)
  <details><summary>📄 Abstract</summary>
  Temporal question answering (TQA) aims to answer questions that involve temporal constraints or require temporal information. We propose Faith, a novel TQA approach that operates over heterogeneous sources and ensures explainable answers by presenting traceable and faithful evidence. In Faith, we design a new recursive answering mechanism transforming implicit temporal constraints into explicit conditions. Additionally, we visualize the system functionality to track how the answers are computed ...
  </details>

- **2026-11-15** — Bakary Gibba, Muhammad Abba Mandara, Karim Ismail Abd-Ellah Mohamed — [Attribute or Abstain: Evaluating Evidence-Grounded Retrieval on the Low-Resource African Business Web](http://arxiv.org/abs/2611.19900v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented systems that research companies are judged by how much they find, yet in markets where public evidence is sparse, a confident answer without support costs more than no answer. We introduce AfriBizClaims, a benchmark of 150 company-research queries across six African markets in English, French and Portuguese, including queries about fictitious companies that a correct system must decline. Each claim a system makes is judged against the page it cites by an AI judge, checked aga...
  </details>

- **2026-11-15** — Zhuo-Yang Song, Zeyu Li, Qing-Hong Cao et al. — [A phase diagram for training and inference in language models](http://arxiv.org/abs/2611.19848v1)
  <details><summary>📄 Abstract</summary>
  A language model is a complex system whose behavior is determined jointly by the Transformer and the corpus, yet how the representation geometry in the Transformer relates to the actual behavior of language models remains open. We analyze how the representation geometry changes along the forward propagation of actual language models and characterize the representation geometry of a document at a given layer by two collective coordinates, document distinguishability and document dimension. On the...
  </details>

- **2026-11-15** — Wesley Maia, Angel Martinez-Sanchez, Maitrayee Keskar et al. — [Passable for Whom? Few-Shot Personal Calibration of Sidewalk Accessibility Perception](http://arxiv.org/abs/2611.19839v1)
  <details><summary>📄 Abstract</summary>
  Whether a sidewalk is passable depends on who is trying to pass: people who use the same mobility aid disagree about the same image, so one label per scene, or per aid, is wrong for many of them. We introduce few-shot personal accessibility perception: from K answers of a person never seen before, predict their judgment of sidewalk scenes never seen before. PassCal separates a shared description of the scene from the person's interpretation of it. The description comes from the internal state of...
  </details>

- **2026-11-15** — Sijie Ruan, Tingyu Xie, Mingfei Liu et al. — [MAPS: A Multimodal Agentic Framework for POI Data Production Based on Crowdsourced Street-view Imagery](http://arxiv.org/abs/2611.19807v1)
  <details><summary>📄 Abstract</summary>
  Point-of-interest (POI) databases support location-based services, yet urban changes quickly make their records stale and manual maintenance is costly. Crowdsourced street-view images provide timely visual evidence, but converting them into database actions requires separating multiple POIs and irrelevant text in each image, then resolving incomplete observations against ambiguous records. We study Street-view Image-based POI Data Production and propose MAPS, the first framework to integrate str...
  </details>

- **2026-11-15** — Hao Fu, Xinbing Kong, Zeyu Li et al. — [Conditional Asset Pricing Transformer](http://arxiv.org/abs/2611.19783v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a conditional asset pricing transformer (CAP-T) that captures nonlinear interactions among firms through attention to forecast excess returns. In the first stage, a transformer estimates conditional expected returns, and kernel-weighted principal component analysis of its residuals estimates the local factor loading space. Projecting the conditional mean onto this space separates factor risk compensation from conditional mispricing. Then, in the second stage, separate t...
  </details>

- **2026-11-14** — Yongan Zhang, Yitao Yu, Yizheng Li et al. — [Well-Log Reconstruction with Pre-trained Geological Knowledge: A Knowledge-Conditioned Large-Language-Model Generative Agent](http://arxiv.org/abs/2611.19624v1)
  <details><summary>📄 Abstract</summary>
  Missing well-log intervals make subsurface reconstruction ill-posed. Existing numerical regression models lack geological prior knowledge to constrain ambiguous inverse mappings. We propose GeoLog-Agent, a knowledge-conditioned generative agent using pre-trained large language models (LLMs) as a source of geological priors. A universal Geo-Harness translates LLM stratigraphic reasoning into formation-anchored petrophysical trajectories, feature-wise linear modulation, and conditional adversarial...
  </details>

- **2026-11-14** — Renata Krupczak — [Fluctuation modes in the initial state of heavy-ion collisions: from 2D to 3D hybrid simulations](http://arxiv.org/abs/2611.19460v1)
  <details><summary>📄 Abstract</summary>
  This dissertation investigates how the initial stages of relativistic heavy-ion collisions shape the evolution of the quark-gluon plasma (QGP) and the observables measured experimentally. Particular attention is given to the initial state and pre-equilibrium dynamics, which constitute the main sources of uncertainty in hybrid simulations. The first part of the dissertation reviews the framework underlying state-of-the-art hybrid simulations and the numerical tools used in phenomenological analys...
  </details>

- **2026-11-14** — Yi-Kai Mo, Kevin E. Bassler — [State-space symmetry in Boolean network ensembles](http://arxiv.org/abs/2611.19639v1)
  <details><summary>📄 Abstract</summary>
  Studies of evolving Boolean network systems have found that Boolean functions cluster into equivalence classes with a characteristic frequency distribution - a pattern governed by the Zyklenzeiger symmetry group - but the dynamical origin of this symmetry has remained unexplained. Here we show that it is a consequence of a fundamental symmetry of Boolean network dynamics itself. A Boolean network consists of nodes that update according to Boolean functions of their regulatory inputs; its global ...
  </details>

- **2026-11-14** — Nan Sai, Karolin Winter, Remco Dijkman — [Data-Driven Heuristic-Guided Business Process Redesign](http://arxiv.org/abs/2611.19623v1)
  <details><summary>📄 Abstract</summary>
  Business process redesign (BPR) has a long-standing catalog of best-practice redesign heuristics, yet, applying them remains a mostly manual task that requires extensive domain knowledge. Despite recent advances using Large Language Models (LLMs) for conversational process model redesign, limitations remain. For example, redesign is user-driven instead of data-driven and is not guided by best practices such as the redesign heuristics. Moreover, only one change can be handled at a time. To addres...
  </details>

- **2026-11-14** — Daragh King, Vasileios Koutavas — [Learning from Mutants: Teaching Small Language Models to Synthesise Loop Invariants](http://arxiv.org/abs/2611.19569v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have proven promising for synthesising loop invariants, a long-standing obstacle to automated program verification. Yet, frontier LLMs are typically accessible only through third-party APIs, hampering reproducibility and local deployment. Small language models (SLMs) sidestep these obstacles but require task-specific fine-tuning, for which high-quality training data is needed. We present a failure-driven data curation method for fine-tuning language models to synthes...
  </details>

- **2026-11-14** — Qi Chen, Zifeng Cheng, Zhiwei Jiang et al. — [SemMask: Semantic-Prioritized Progressive Masking for Diffusion Language Models](http://arxiv.org/abs/2611.19560v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) are designed to enable globally parallel generation. However, in practice, they often exhibit pseudo-autoregressive behavior and a function-word-first bias, which undermines their performance on tasks such as text writing and code generation that benefit from global planning and parallel decoding. To address this, we propose SemMask, a novel fine-tuning paradigm that leverages a semantic-prioritized progressive masking strategy to encourage the model to decode hi...
  </details>

- **2026-11-14** — Víctor Gallego — [Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in Craftax](http://arxiv.org/abs/2611.19537v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can synthesize and optimize code-based policies from simulator feedback, allowing the resulting program to act with zero inference model calls. But for long horizon tasks, two challenges arise: local improvements can hurt final success and switching to a new objective requires another expensive synthesis run. We propose a framework that first develops competence by refining the policy through a feedback cascade, moving from episode returns to hierarchical goals and belief updates w...
  </details>

- **2026-11-14** — Jincheng Li, Zhengyi Liu, Zelin Liu et al. — [PathLoop: Self-Evolving Multi-Agent Reasoning for Evidence-Grounded Whole-Slide Image Analysis](http://arxiv.org/abs/2611.19527v1)
  <details><summary>📄 Abstract</summary>
  Analyzing whole-slide images (WSIs) requires combining evidence across tissue regions and spatial scales. Multi-agent systems offer a promising approach to this task. However, existing systems make limited use of molecular evidence, often select visually prominent but less representative regions while overlooking global context, and struggle to reuse experience from previous cases. To address these challenges, we present PathLoop, a self-evolving multi-agent framework that integrates omics data ...
  </details>

- **2026-11-14** — Jinan Pan, Timo Schorlepp — [Computing rare events in Lévy-driven systems via optimal control](http://arxiv.org/abs/2611.19481v1)
  <details><summary>📄 Abstract</summary>
  We extend the optimal control formulation of sample path large deviation theory, which has proven effective for numerical computation of instantons and sharp probability estimates in stochastic differential equations with Gaussian noise, to systems with light-tailed Lévy noise. In the scaling limit of small jumps and high intensity, such systems satisfy a large deviation principle of Freidlin-Wentzell type, with a running cost given by the Legendre transform of the noise cumulant generating func...
  </details>

- **2026-11-13** — Yulliwas Ameur, Billal Mokhtari, Samia Bouzefrane — [Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory](http://arxiv.org/abs/2611.18133v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents keep a long-term memory that the model itself writes: summaries, extracted facts and embeddings derived from what users said. Deleting a message is therefore not enough: its derivatives, storage residue and backups survive. We define lineage-complete forward-secure erasure: after a forget request, an adversary that later obtains all storage and the agent's current keys learns nothing about the forgotten input or any memory derived from it. We present LinEra, whi...
  </details>

- **2026-11-13** — Qi Tan, Tianyu Cui, Qi Li et al. — [Condensing Law of Security Information](http://arxiv.org/abs/2611.17918v1)
  <details><summary>📄 Abstract</summary>
  Scaling laws indicate that the generalization error of a large language model (LLM) decreases monotonically with model size once data is sufficient, and the corollary that larger models outperform smaller ones is now widely accepted. We argue that this corollary fails in security: decisions there hinge on anomalous inputs, which are long-tailed (e.g., zero-day attacks) and therefore poorly served by likelihood fitting. Worse still, the capability brought about by scale (e.g., inferring the inten...
  </details>

- **2026-11-13** — Jonathan D. McCart, Pranav I. Deevi, Mehdi Azabou et al. — [FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices](http://arxiv.org/abs/2611.18561v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in speech neuroprostheses have enabled new communication avenues for people who have lost the ability to speak due to neurological illness or injury. These systems can decode neural activity during attempted speech into text by relying on language priors to achieve high decoding accuracy. This performance currently comes at the cost of using a compute-intensive language modeling stack, presenting a major bottleneck for real-world use. Further, current language models incur highly...
  </details>

- **2026-11-13** — Jianjun Zhou, Hua Geng, Haoyu Guo — [JVT: Just Video Transformer makes pixel-space video diffusion simple](http://arxiv.org/abs/2611.18549v1)
  <details><summary>📄 Abstract</summary>
  Direct diffusion modeling of high-dimensional raw video data is challenging, and existing pixel-space methods often rely on specialized architectures. We introduce JVT (Just Video Transformer), a simple large-patch DiT-style Transformer for pixel-space video diffusion, without a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net-style skip connections. We systematically examine video patch embeddings, register tokens, and adaptive layer normalization to identify design choice...
  </details>

- **2026-11-13** — Julian Schelb, Michael Wittweiler, Marie Revellio — [Learning Word-Level Explanations of Text Reuse in Latin Literature with Little Annotation](http://arxiv.org/abs/2611.18319v1)
  <details><summary>📄 Abstract</summary>
  Detecting an intertextual reference is only the first step; philologists also need to know how a later author reworked the source. We explain a reuse pair word by word: each word of the reusing passage is first aligned to its source word, then labeled with the operation that transformed it, such as a copy, a change of inflection, or a substitution. Such word-level operations are expensive to annotate, and only a few corpora annotated at this level exist for text reuse in Latin literature. We des...
  </details>

- **2026-11-13** — Tim Donkiewicz, Oliver Gaul, Marco Lübbecke — [Integrated Topology and Redispatch Optimization of Real-World Power Transmission Systems using Branch-and-Benders-Cut](http://arxiv.org/abs/2611.18302v1)
  <details><summary>📄 Abstract</summary>
  Transmission system operators can reduce congestion management costs by jointly optimizing network topology, generator redispatch, and transformer settings. The large number of switching decisions, detailed operational constraints, and security requirements under outages make this problem computationally demanding. We present a full mixed-integer linear programming formulation that combines line switching, substation reconfiguration, generator commitment and redispatch, and transformer settings ...
  </details>

- **2026-11-13** — Finnian Gray, Hryhorii Ovcharenko — [Separability of coupled gravitational perturbations in Plebański--Demiański spacetimes](http://arxiv.org/abs/2611.18200v1)
  <details><summary>📄 Abstract</summary>
  Recently, a major breakthrough in the separability of gravitational perturbations of the Kerr--Newman rotating charged black hole was achieved by Hintz [arxiv:2609.33661], and extended to non-zero cosmological constant Kerr--Newman-(A)dS black holes by Yoshida [arxiv:2610.20500] and Zhao [arxiv:2610.22274]. This method removes the need for the freezing approximation, wherein coupling to the electromagnetic degrees of freedom are ignored, at the price of a coupled set of equations in the gravitat...
  </details>

- **2026-11-13** — Yue Xu, Kaiyun Wei, Wenying Duan et al. — [T2ST: Data-Efficient Spatio-Temporal Foundation Models via Temporal Data and Knowledge Transfer](http://arxiv.org/abs/2611.18199v1)
  <details><summary>📄 Abstract</summary>
  Spatio-temporal foundation models (STFMs) require large-scale training corpora, yet synchronized observations and spatial metadata are costly to acquire and curate, limiting the availability of suitable data. By contrast, time-series data are abundant and easier to collect. Since observations at each location form a time series, this motivates a natural question: can abundant time-series data enhance STFMs when spatio-temporal observations are scarce? To bridge this gap, we propose T2ST, a data-...
  </details>

- **2026-11-13** — Yundi Cai, Zihan Wang, Chenxi Han et al. — [ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents](http://arxiv.org/abs/2611.18176v1)
  <details><summary>📄 Abstract</summary>
  Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior. The VLA may generate actions that diverge from the LLM's intended subtask and, upon regaining control after a correction, undo the promising state restored by the LLM. We introduce ESI (Embodied Self-Improvement), an automated flywheel that uses environmental interaction to align reas...
  </details>

- **2026-11-13** — Joey Chan, Haoyu Pan, Zhen Chen et al. — [Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries](http://arxiv.org/abs/2611.18140v1)
  <details><summary>📄 Abstract</summary>
  Fast charging of lithium-ion batteries is a multi-objective control problem that requires reducing charging time and sustaining high energy throughput while suppressing accelerated degradation and safety-critical electrochemical reactions. Conventional protocols are easy to implement but have limited ability to adapt to variations in battery chemistry, operating conditions, and aging state. Model-based optimization and conventional data-driven control often require accurate models, costly iterat...
  </details>

- **2026-11-13** — Yash Mehta, Chandan Singh, Weijia Xu et al. — [Interpretable weight-space programming builds transparent transformers and brain encoding models](http://arxiv.org/abs/2611.18114v1)
  <details><summary>📄 Abstract</summary>
  Neural networks are powerful predictors, yet their opacity limits their usefulness in science, where the goal is explanation rather than mere prediction. In neuroscience, for example, deep encoding models accurately predict brain activity in response to natural stimuli, but struggle to reveal which stimulus features drive those predictions. Here we introduce interpretable weight-space programming (iWSP), a method in which an LLM agent iteratively builds interpretable models by explicitly program...
  </details>

- **2026-11-13** — Trinh T. Nguyen, Duy-Tung Pham, Hoang-Son Do et al. — [Two-Clustering Regime of Token Dynamics in Causal Attention](http://arxiv.org/abs/2611.18088v1)
  <details><summary>📄 Abstract</summary>
  We partially resolve Conjecture 1 of [Karagodin et al., Clustering in Causal Attention Masking (NeurIPS 2024)] and extend it to time-dependent parameter regimes. The conjecture predicts that causal attention dynamics converge to two clusters aligned with the eigenvectors associated with the largest eigenvalue $λ_{\max}$ of the value transformation. We prove that this behavior holds when $λ_{\max}>0$ and is generally false when $λ_{\max}\le0$. The resulting two-cluster regime is common in practic...
  </details>

- **2026-11-13** — Ruiqi Shu, Xufeng Zhan, Yuanzhi Liang et al. — [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](http://arxiv.org/abs/2611.18078v1)
  <details><summary>📄 Abstract</summary>
  Direct image-to-video diffusion models entangle pixel synthesis with implicit latent motion, precluding persistent 3D mechanical equilibrium, mid-rollout intervention, and counterfactual force control. Conversely, single-pass programmatic 3D reconstruction from an uncalibrated photograph leaves monocular depth and support clearance underconstrained, causing reconstructed scenes to interpenetrate or collapse under gravity. We present TelePhysica, a closed-loop framework that reconstructs an execu...
  </details>

- **2026-11-13** — Swarn Priya, Basavesh Ammanaghatta Shivakumar, Thomas Gilray et al. — [DeCompCert: A Verified Decompiler for CompCert-Generated AArch64](http://arxiv.org/abs/2611.18055v1)
  <details><summary>📄 Abstract</summary>
  DeCompCert is a Rocq-verified decompiler for AArch64 assembly generated by CompCert. It reconstructs CompCert C through nine reverse passes, combining deductively verified transformations with translation validation. Untrusted OCaml and Datalog analyses propose candidate reconstructions, while verified validators accept only candidates that satisfy the required semantic correspondence. The composed correctness theorem guarantees that every defined, safe behavior of an accepted C reconstruction i...
  </details>

- **2026-11-13** — Eunsu Kim, Sukyoung Ryu, Jaemin Hong — [C-to-Rust Translation Validation at the LLVM IR Level via AI-Assisted Refinement Proof](http://arxiv.org/abs/2611.18036v1)
  <details><summary>📄 Abstract</summary>
  Migrating C codebases to Rust is a promising approach to securing legacy software, but existing translators do not guarantee that a translated Rust program preserves the behavior of the C program. Neither rule-based nor large language model (LLM)-based translators have been formally verified, and existing approaches to checking translation correctness are limited to testing and bounded checks, which cannot reason about all possible executions. In this work, we present R2C2, which validates C-to-...
  </details>

- **2026-11-13** — Julien Figeac, Erwan Le Merrer, Marie Neihouser et al. — [From institutional journalism to political extremes: Structural asymmetries in YouTube's news recommender during the 2022 French presidential campaign](http://arxiv.org/abs/2611.18034v1)
  <details><summary>📄 Abstract</summary>
  Debate has intensified over how algorithmic recommendations shape news visibility, particularly regarding structural and ideological bias. This study examines YouTube's News Recommender System (NRS) in the French ``News'' section, using a large-scale audit based on automated browsing agents operating under cold-start conditions, without prior viewing history, to isolate the algorithm's structural baseline independently of user preferences. Our results reveal that YouTube's NRS operates within a ...
  </details>

- **2026-11-13** — Ignacio Cofone, Katherine J. Strandburg — [Algorithmic Opacity as a Principal-Agent Problem](http://arxiv.org/abs/2611.17980v1)
  <details><summary>📄 Abstract</summary>
  Concerns about gaming and trade secrecy, frequently invoked to justify algorithmic opacity, can also mask self-serving strategic behavior by decision-makers, who may prioritize private benefits over social welfare. We develop a principal-agent test for when algorithmic decision-making should trigger disclosure obligations even when concerns about gaming or trade secrecy exist. The test, which is anchored in decision quality, relies on two diagnostics that can be disclosed without enabling gaming...
  </details>

- **2026-11-13** — Jie Huang, Yuecheng Hong, Yao Chen et al. — [OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination](http://arxiv.org/abs/2611.17933v1)
  <details><summary>📄 Abstract</summary>
  In many long-horizon settings, an agent's own choices create future constraints: committing finite capacity establishes future obligations and forecloses later opportunities. Sustaining performance therefore requires both keeping evolving plans feasible and comparing the value of resource allocations with the alternatives they displace. Recent benchmarks increasingly evaluate LLM agents in continuing operations, but give less attention to how agents keep their own commitments feasible while reas...
  </details>

- **2026-11-13** — Alexander Spangher, Charlotte Peale, Sílvia Casacuberta et al. — [DOCKET: A Pluralistic Benchmark for Evaluating AI-Assisted Policy Feedback in U.S. Rulemaking](http://arxiv.org/abs/2611.17914v1)
  <details><summary>📄 Abstract</summary>
  As AI models advance and impact deliberative democracies, there is a growing need to assess their support of pluralistic viewpoints. Most pluralism benchmarks are insufficient for this: they are not grounded in diversity (i.e., stakeholders across different frames, skills and needs), quality (i.e., rigorous and technical debates), and impact (i.e., invested deliberators and real-world outcomes). To address this, we first (i) curate DOCKET, the most comprehensive dataset of the U.S. Federal Notic...
  </details>

- **2026-11-13** — Mike He, Ankush Desai, Sharad Malik et al. — [Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents](http://arxiv.org/abs/2611.17880v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that execute multi-step tool calls must satisfy two objectives simultaneously: completing the user's task (utility) and conforming to domain policies and correctness constraints (safety). These objectives are in tension -- blocking an unsafe action prevents a violation but can leave the agent stranded with no principled way to recover. Existing approaches sacrifice one objective for the other. We introduce Soteria, a framework that reconciles safety and utility through verified hierar...
  </details>

- **2026-11-13** — Seunghwan Jang, Steven Ceron, Wei Xiao — [Per-Agent-Safe Navigation of Globally Driven Robot Collectives via Affine Field Design](http://arxiv.org/abs/2611.17859v1)
  <details><summary>📄 Abstract</summary>
  Safe navigation of robot collectives requires coordinating motion and deformation so that the collective can traverse constrained environments while ensuring each robot's safety. Existing controllers for swarmalator collectives largely rely on local control, where each robot receives an individual command, which causes the control and communication requirements to grow with the number of agents. We introduce a broadcast control formulation in which a single spatially affine field governs both th...
  </details>

- **2026-11-13** — Keuntae Kim, Dongjun Kim, Yong Suk Choi — [V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations](http://arxiv.org/abs/2611.17831v1)
  <details><summary>📄 Abstract</summary>
  World-model video encoders such as V-JEPA learn how scenes change (direction, speed, order, state) from video alone. To answer questions, they are joined to a language model trained on captions and question-answer pairs. But each caption or question names only a few attributes of a clip, so the model learns to retrieve those attributes rather than to read the clip, and the dynamics the encoder carries go unused: on the same items, a linear probe reads speed from frozen V-JEPA features at 87% whi...
  </details>

- **2026-11-13** — Saptarshi Ghosh, Mohammad Saim, Tianyu Jiang — [AI Reviews Are Biased Towards the Appendix](http://arxiv.org/abs/2611.17811v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used by reviewers to highlight weaknesses during the reviewing process, and their outputs often shape the reviews that humans submit. Prior work studies how LLM reviews align with human ones, yet we know little about which parts of a paper these models actually criticize. In this work, we investigate 2,000 papers from ACL, EMNLP, COLM, and ICLR, and show that the latest GPT and Claude models draw about 50% or more of their review weaknesses from the ...
  </details>

- **2026-11-13** — Zihao Lu, Trong Gia Hung Nguyen, Fuquan Wang et al. — [Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation](http://arxiv.org/abs/2611.18298v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have shown strong semantic and spatial reasoning capabilities in 3D environments. Recently, connecting VLMs with model-predictive controllers (MPC) has emerged as a paradigm for combining strong semantic reasoning with physics-based planning. However, connecting these two for contact-rich robotic manipulation requires a task representation that bridges the two and captures how physical interactions can be reasoned by VLMs. In this work, we introduce Objectives as Po...
  </details>

- **2026-11-13** — Mohamed Aghzal, Mor Geva, Gregory J. Stein et al. — [Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination](http://arxiv.org/abs/2611.18514v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic Interpretability (MI) has made significant progress in explaining the internal computations of Large Language Models (LLMs); however, these advances have yet to demonstrate comparable success in explaining the decision-making processes of LLM-based agents. This paper examines the challenges MI tools face when applied to realistic agentic failures. We focus on one such failure: web agents hallucinating actions that are not available on a website. We apply a series of mechanistic analy...
  </details>

- **2026-11-13** — Jiani Hu, Chenyan Wang, Yongkun Yang et al. — [Graph diffusion transformer for interpretable generation and inverse design of disordered atomic structures](http://arxiv.org/abs/2611.18420v1)
  <details><summary>📄 Abstract</summary>
  Atomic disorder offers a potent degree of freedom to tailor material properties, yet the resulting vast configuration space obscures structure-property relations and hinders rational inverse design. Here we introduce Graph Amorphous Diffusion Transformer (GaDiT), a generative model that combines dynamic periodic graphs, masked conditioning and an interval-weighted training-noise distribution. GaDiT generates high-quality disordered structures while accelerating sampling by two orders of magnitud...
  </details>

- **2026-11-13** — Grid Robotics,  :, Qingfeng Lan et al. — [Envisioning Agentic Robotics: A New Era of Robotic Systems](http://arxiv.org/abs/2611.18359v1)
  <details><summary>📄 Abstract</summary>
  The release of GPT-6 Astra marks the emergence of a new paradigm in robotics: agentic robotics. Within weeks, frontier models with agentic harnesses matched or exceeded task-specific policies on many embodied benchmarks. Instead of training a dedicated policy for each family of tasks, an agentic robotic system applies a foundation model to open-world embodied tasks. It operates in a closed loop: observing the environment, interpreting user intent, reasoning about the task, invoking skills and to...
  </details>

- **2026-11-13** — Ata Akbari Asanjan, Anit Upadhyaya, Jeremy Kravitz et al. — [Lens: Training-Free Semantic Search for Cross-Tile Object and Scene Retrieval in Satellite Imagery](http://arxiv.org/abs/2611.18251v1)
  <details><summary>📄 Abstract</summary>
  We developed Lens, a training-free system for semantic object and scene search across large satellite mosaics that requires no detector trained for the class of interest. Lens represents each tile with a frozen, self-supervised vision transformer (DINOv3), removes the positional bias in its dense features by projecting them onto the subspace orthogonal to a positional basis estimated once from a constant image, and centers the debiased features on the mean feature computed across the whole area ...
  </details>

- **2026-11-13** — Yuan-Chao Hu — [Dancing Tokens on the Vocabulary Network from LLM Generation](http://arxiv.org/abs/2611.18248v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) generate text one token at a time, yet how a particular generation relates to the geometry learned in pre-training remains unclear. The fundamental explainability of LLMs is elusive. Here, we build a similarity network from the input embeddings of six open LLMs and map generation onto it. The token-embedding network is scale-free while heavy-tailed, as are random embeddings with matched covariance, but far more fragmented. Distillation barely changes this topology be...
  </details>

- **2026-11-13** — Charly Witmeur, Gonçalo G. Cruz, Maarten Schoukens et al. — [A Reinforcement Learning Approach to Space-Filling Input Design for Nonlinear System Identification](http://arxiv.org/abs/2611.18229v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a reinforcement learning (RL) approach to space-filling input design for nonlinear system identification, in which an agent learns a control policy that actively drives the system to explore its state space. Classical input design, developed mainly for linear models, minimises the covariance of the estimated parameters. For nonlinear black-box models, however, the dominant error is the bias induced by the model structure over the region of interest, which motivates spac...
  </details>

- **2026-11-13** — Jingyao Cai, Shuaijun Liu, Abdul Rehman et al. — [When Should a Virtual Patient Ask? RISP-Guided Proactive Information Seeking in Multi-Agent Patient Simulation](http://arxiv.org/abs/2611.18183v1)
  <details><summary>📄 Abstract</summary>
  Virtual patient (VP) systems support nursing communication training by providing simulated encounters in which learners practise explaining care and responding to patient concerns. Although large language models (LLMs) support flexible dialogue, current approaches give less explicit attention to how patients' information needs develop and guide the content and timing of their questions. We draw on the Risk Information Seeking and Processing (RISP) model, which relates information seeking to perc...
  </details>

- **2026-11-13** — Diane Bouchacourt, Gaëtan Brison — [Explanations that Transfer: Interpreting Medical Retrieval with Sparse AutoEncoders](http://arxiv.org/abs/2611.18179v1)
  <details><summary>📄 Abstract</summary>
  Medical AI systems that answer users' queries rely on retrieving medical knowledge from large document collections. In this context, finetuning general models on medical datasets can improve retrieval relevance. Yet the dense embeddings underlying modern retrieval systems remain largely opaque, making it difficult to understand the mechanics behind their results. Moreover, adapting to a specific medical dataset risks losing transferability to new clinical corpora. In this work, we tackle these i...
  </details>

- **2026-11-13** — Yuxia Qiao, Xinhao Zhong, Junhao Li et al. — [InfiHall-Bench: A Benchmark for Hallucination Evaluation in Autoregressive Text-to-Image Generation](http://arxiv.org/abs/2611.18053v1)
  <details><summary>📄 Abstract</summary>
  Hallucination benchmarks for text-to-image generation are predominantly designed around diffusion models, limiting their diagnostic value for visual autoregressive (VAR) models and the development of mitigation methods. We identify two limitations in existing prompt construction paradigms: many prompts are no longer challenging for modern generators, while category-based construction relies on recurring object-attribute-relation templates and rarely tests interactions among multiple visual requi...
  </details>

- **2026-11-13** — Andreia Chapouto, Simão Correia, João Pedro Ramos — [Local well-posedness for the Novikov-Veselov equation at subcritical regularity](http://arxiv.org/abs/2611.18046v1)
  <details><summary>📄 Abstract</summary>
  We establish local well-posedness of the Novikov--Veselov equation (NV), at every fixed value of the energy parameter, for initial data in $H^s(\mathbb{R}^2)$ in the entire subcritical Sobolev range $s>-1$. The argument is perturbative and does not invoke the integrable structure, instead adapting the strategy in our previous work on KdV (2026). An infinite normal-form expansion indexed by binary trees is combined with a gauge transform that bypasses the obstructions in the associate bilinear es...
  </details>

- **2026-11-13** — Marco Giunti, Fabrizia Giulia Garavaglia — [The Transformer Paradigm: Dynamic Processing and a New Principle of Inference](http://arxiv.org/abs/2611.17953v1)
  <details><summary>📄 Abstract</summary>
  We argue that the Transformer revolution is not adequately understood as a merely quantitative expansion of deep learning, but as the emergence of a new paradigm based on a different principle of inference. We interpret the Transformer as a system in which token representations are transformed by parameterized transformations, or transforming concepts. During inference, some of these transformations are dynamically constructed from the current input: previously acquired transformations are first...
  </details>

- **2026-11-13** — Monica Riedler, Samuele Antonelli, Barbara Plank et al. — [AmbiSteer: Selectively Eliciting Ambiguity-Aware Responses in Vision-Language Models](http://arxiv.org/abs/2611.17900v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) often exhibit overconfidence, providing firm answers even when visual evidence is insufficient. A prominent case is referential ambiguity in Visual Question Answering (VQA), where multiple entities in an image are plausible referents of a question. Addressing such cases requires recognizing when ambiguity is present: ambiguous questions can be handled by asking for clarification or enumerating plausible referents, while unambiguous questions should receive a direct ...
  </details>

- **2026-11-13** — Md Rifat Arefin, Ravid Shwartz-Ziv, Ernie Chang et al. — [Delayed Effects of Temporary Weight Decay in Muon Pretraining](http://arxiv.org/abs/2611.17876v1)
  <details><summary>📄 Abstract</summary>
  A temporary optimization intervention can increase validation loss when it ends yet reduce it at the final training budget. We demonstrate this with temporary weight decay in Muon-trained decoder-only Transformers with 162M, 405M, 1.4B, and 3.4B parameters. For models up to 1.4B parameters, moving a fixed-duration decay window from early to late training reverses its final effect. At 162M, changing window duration alters final loss even at approximately matched total shrinkage. Most strikingly, ...
  </details>

- **2026-11-13** — Hongguan Su, Ming Wang, Shun Zhang et al. — [Can Agents Keep Up with Time? An Empirical Analysis of Temporal Adaptation After a Conversational Hiatus](http://arxiv.org/abs/2611.17806v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents increasingly serve as persistent personal assistants across modern web platforms, managing schedules, applications, and multi-step plans over weeks or months. Users often return to an ongoing conversation after a long conversational hiatus, while earlier bookings and preparation notes stay on record. During this hiatus, scheduled dates may pass even though the retained records remain unchanged and event outcomes go unrecorded. Existing evaluations of long-horizon agents focus...
  </details>

- **2026-11-13** — Megan Wei, Damon Pham, John Cayley et al. — [Activation Steering the Nan-Shan in Typhoon](http://arxiv.org/abs/2611.17768v1)
  <details><summary>📄 Abstract</summary>
  Typhoon is an audiovisual installation based on Joseph Conrad's novella, in which Captain MacWhirr steers the steamer Nan-Shan directly into and through a catastrophic storm. The novella is a study of what happens when the scale of a phenomenon exceeds the practical and conceptual frameworks available to comprehend it and of the paralysis that sometimes follows a demand for action in such overwhelming circumstances. We chose the text of Typhoon to reflect on human culture's current AI moment. We...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 721 |
| prompt-injection | 687 |
| memory-poisoning | 59 |
| tool-use-attack | 175 |
| backdoor | 560 |
| adversarial-attack | 674 |
| privacy-leakage | 4608 |
| steganography | 93 |
| misuse | 1322 |
| red-teaming | 154 |
| vulnerability | 4038 |
| defense | 3949 |
| alignment | 3709 |
| robustness | 4054 |
| watermark | 766 |
| unlearning | 122 |
| agent-safety | 67 |
| benchmark | 75 |
| survey | 461 |
| other | 11140 |

---

📚 **全部 37434 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-18 00:24:05*