<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-24616-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-25 01:37 ｜ **论文总数 / Total Papers**: 24616（近 30 天 / Recent 30 days: 3748）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 24616 篇论文（含摘要、分类筛选、搜索）/ View all 24616 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 590
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 499
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 123
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 422
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 567
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3884
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 56
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 917
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 115
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2772
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2504
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2315
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2344
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 322
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 91
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 60
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 293
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6646

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3748 篇，完整 24616 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3748 papers from the last 30 days (with date, authors & abstract). For the full list of 24616 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-08-21** — Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai et al. — [ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models](http://arxiv.org/abs/2608.21100v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two k...
  </details>

- **2026-08-21** — Yang Liu, Bin Chong, Wenkai Yang et al. — [Certified Multi-Turn Robustness for LLM Safety via Compositional Bounds and Safety Persistence](http://arxiv.org/abs/2608.20820v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are vulnerable to multi-turn jailbreak attacks that progressively manipulate conversation context. Existing certified robustness methods are limited to single-turn inputs; naive multi-turn composition yields bounds that degrade exponentially in the number of turns. We introduce Multi-Turn Certified Robustness (MTCR), a framework that models conversational safety via State-Adversarial MDPs and defines $k$-turn certified robustness as the worst-case safety probability ...
  </details>

- **2026-08-20** — Ling Zhou, Yihao Huang, Jingling Sun et al. — [TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling](http://arxiv.org/abs/2608.19737v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved remarkable progress in video understanding and reasoning. Despite extensive studies on text- and image-based jailbreaks, video jailbreaks against LVLMs remain largely unexplored. Existing video jailbreak methods mainly manipulate textual content embedded in videos, while overlooking how such information is organized over time. Our analysis reveals that jailbreak effectiveness depends not only on the semantics of textual information but also on i...
  </details>

- **2026-08-18** — Istiaque Ahmed, Afia Anjum Borsha, Ranat Das Prangon et al. — [Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings](http://arxiv.org/abs/2608.17556v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) in real-world applications often face the risks of specially crafted prompts designed to bypass the safety controls. Existing guardrail methods, such as LLM-as-a-judge and cloud-based safety APIs are able to detect unsafe content. However, they often add a delay of about 250-900 ms to each request. This delay is too high for real-time applications, when the system usually needs to respond in less than 100 ms. Furthermore, routing user prompts through external moderat...
  </details>

- **2026-08-18** — Zhida He, Xiaoyu Wen, Han Qi et al. — [Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets](http://arxiv.org/abs/2608.17360v1)
  <details><summary>📄 Abstract</summary>
  Reliable jailbreak evaluation is essential for assessing LLM safety, but most existing studies rely solely on attack success rate (ASR) without accounting for its dependence on attack budgets, resulting in unfair comparisons across methods. Existing compute-aware evaluations reduce heterogeneous resources into FLOPs, which is difficult to estimate for black-box models and fails to capture resource-specific constraints. To provide a comparable evaluation basis, we introduce Fair-ASR, an evaluatio...
  </details>

- **2026-08-18** — Md Abdullahil Oaphy, Anhao Xiang, Zongxing Xie et al. — [COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models](http://arxiv.org/abs/2608.17234v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly used to interact with screenshots, scanned documents, diagrams, and other visually grounded inputs. This shift introduces a new safety risk: in many multimodal jailbreaks, neither the prompt nor the image is harmful in isolation. Unsafe behavior emerges only when the model binds an apparently benign operation, such as summarizing, translating, or following, to a localized visual target. This reveals a structural weakness in current multim...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-08-21** — Bohao Liao, Jingchao Wang, Qipeng Song et al. — [TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents](http://arxiv.org/abs/2608.21126v1)
  <details><summary>📄 Abstract</summary>
  Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidenc...
  </details>

- **2026-08-21** — Balkrishna Giri, Md Toufique Hasan, Jussi Rasku et al. — [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](http://arxiv.org/abs/2608.21095v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) outputs in external knowledge, but RAG systems usually trust whatever they retrieve, creating a Security-Reliability Gap: high semantic relevance does not guarantee factual truth. Adversaries exploit this through knowledge poisoning, inserting malicious documents to cause targeted misinformation. We propose an Evaluation Agent, middleware that combines Natural Language Inference (NLI) factual verification, a five-signal pois...
  </details>

- **2026-08-20** — Roshan Sood, Onat Gungor, Tajana Rosing — [COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense](http://arxiv.org/abs/2608.19982v1)
  <details><summary>📄 Abstract</summary>
  LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives or attack-specific filtering mechanisms that require redesign as new attack strategies emerge. While recent lifelong alignment methods address shifting user preferences, they do not account for adaptive adversaries that continually evolve to ...
  </details>

- **2026-08-18** — Sujin Chen, Lijun Li, Tianyi Du et al. — [MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps](http://arxiv.org/abs/2608.17659v1)
  <details><summary>📄 Abstract</summary>
  LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to environmental injection attacks, which include indirect prompt injections and adversarial instructions. Such attacks can manipulate the behavior of agents without user awareness through diverse channels encountered in everyday mobile use. Despit...
  </details>

- **2026-08-18** — Rabimba Karanjai, Yang Lu, Richard Williamson et al. — [PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance](http://arxiv.org/abs/2608.17220v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's susceptibility to prompt injection and lack of mechanisms to bind a verifier's approval to the exact transaction ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a transaction-level authorization framework that inte...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-08-20** — Yue Wang, Yi Liu, Gelei Deng et al. — [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](http://arxiv.org/abs/2608.19901v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious A...
  </details>

- **2026-08-20** — Xiaohan Huang, Qingqing Long, Xiaolei Du et al. — [Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale](http://arxiv.org/abs/2608.19625v1)
  <details><summary>📄 Abstract</summary>
  Scientific data are increasingly used by AI agents, yet existing dataset representations provide limited support for autonomous discovery, interpretation, and invocation. This limitation stems from the fragmentation of scientific data across heterogeneous repositories and from dataset representations designed primarily for human use. To address this limitation, we introduce the Scientific Data Skill (SciDSK), an agent-ready representation that packages dataset-specific knowledge and operational ...
  </details>

- **2026-08-19** — Kou Shi, Zun Wang, Qisheng Su et al. — [FACET: Preserving Source Intent and Executable State in Terminal Task Synthesis](http://arxiv.org/abs/2608.18580v1)
  <details><summary>📄 Abstract</summary>
  Training terminal agents requires scalable executable supervision, yet synthesizing high-quality terminal tasks remains challenging. Each task couples an instruction, an initialized environment, a reference solution, and an executable verifier; if these artifacts are generated from inconsistent assumptions, the resulting task may be unsolvable or incorrectly evaluated. Meanwhile, multi-stage synthesis can discard the goals, dependencies, state transitions, and procedural constraints encoded in t...
  </details>

- **2026-08-18** — Zhibo Zhang, Zhen Ouyang, Ling Shi et al. — [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](http://arxiv.org/abs/2608.17588v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills package reusable natural language procedures with executable resources, enabling software agents to acquire task specific capabilities without model adaptation. Automatically generating such Skills can improve task performance, yet evaluating a candidate solely from its artifact or final task outcome leaves unresolved which actions the equipped agent will perform and which side effects those actions will produce. We present TRUSS, an evidence guided framework for generating function...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-08-21** — Minhua Lin, Zhicheng Gao, Yilong Wang et al. — [Trojaning the Alignment: Stealthy Backdoor Attacks against Graph Foundation Models](http://arxiv.org/abs/2608.20991v1)
  <details><summary>📄 Abstract</summary>
  Graph Foundation Models (GFMs) on text-attributed graphs (TAGs) align graph representations with language semantics to support transferable graph learning. Despite these advantages, the backdoor vulnerability of GFMs on TAGs remains insufficiently understood, especially under graph-language alignment, where graph and text representations are trained to constrain each other in a shared semantic space. Existing backdoor attacks mainly target either the graph side or the text side, treating the two...
  </details>

- **2026-08-19** — Krishna Teja Medam — [Autonomous Cyber Defense in Connected Vehicles: A Multi-Agent Approach to V2X Security](http://arxiv.org/abs/2608.19135v1)
  <details><summary>📄 Abstract</summary>
  A connected vehicle has roughly 100 milliseconds to decide whether an incoming Basic Safety Message is real or fabricated. If a false emergency braking alert reaches the planning pipeline in time, the car brakes - a safety failure triggered by a security failure. Existing intrusion detection systems are not designed to handle that coupling. They operate per vehicle, per message, with static rules - blind to attack patterns that only emerge across a fleet or over time, and blind to the fundamenta...
  </details>

- **2026-08-18** — Hollis Robbins — [Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation](http://arxiv.org/abs/2608.18041v2)
  <details><summary>📄 Abstract</summary>
  Reading fiction or encountering narrative generally does not merely add information. The encounter changes the reader. This paper proposes that encounters alter persistent relations among simultaneously active meanings, producing individual and shared histories that population-trained language models do not necessarily retain. A model may be told of an encounter and reproduce its consequences while the history remains in context; this is not the same as being changed by the encounter. This paper...
  </details>

- **2026-08-18** — Gaston Besanson — [One Gate Is Not Enough: Composing Stateful Pre-Action Controls for Agentic AI](http://arxiv.org/abs/2608.18360v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems take consequential actions governed by more than one pre-action control at once: authority, resource, and evidence gates that can admit, degrade, or remediate an action before it executes. This paper's central object is remediation-induced control coupling: a remediation applied by one control can change the action, evidence, or context another control evaluates, invalidating that control's earlier judgment. We formalize this coupling and give a remediate-and-regate protocol t...
  </details>

- **2026-08-18** — Xukun Luan, Jinyan Liu, Yuhui Gong et al. — [MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning](http://arxiv.org/abs/2608.17722v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language models (VLMs) achieve outstanding performance largely due to the amount of training data available on the internet. At the same time, data holders (e.g., artists) urgently need to determine whether their data has been used for model training without authorization, which concerns both intellectual property rights and personal privacy. Data auditing, particularly through membership inference (MI), has attracted attention as a direct tool. This work proposes MemCatalyst, a set of da...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-08-19** — Ilan Zini, Boussad Addad, Katarzyna Kapusta — [Breaking the weakest link to evade vision language models](http://arxiv.org/abs/2608.18938v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to vi...
  </details>

- **2026-08-18** — Xiaoyong Yu, Rongzhen Li, Shuming Shi et al. — [MS-MFAD : Multimodal large language models for Face Anti-spoofing Detection](http://arxiv.org/abs/2608.17328v1)
  <details><summary>📄 Abstract</summary>
  Facial biometric recognition systems currently face compound threats intertwining generative AI and high-fidelity physical spoofing. Existing defenses suffer from systemic bottlenecks, including poor generalization, non-auditable reasoning, and reliance on massive, low-quality datasets. To address these challenges, we propose Multimodal Large Language Models (MFAD) for face anti-spoofing detection, an explainable reasoning system for Unified Face Anti-Spoofing Detection (UFAD), accompanied by a ...
  </details>

- **2026-08-18** — Yang Chen, Zhan Zhuang, Yanbin Wei et al. — [Learning What Not to Learn: Adversarial Disentangled Prompt Tuning for Robust Vision-Language Models](http://arxiv.org/abs/2608.17306v1)
  <details><summary>📄 Abstract</summary>
  While adversarial prompt tuning can enhance robustness of vision-language models efficiently, we find that existing methods aggravate robust generalization overfitting on seen classes, leading to a rapid degradation in performance against adversarial examples of unseen classes as training progresses. We empirically identify that this degradation stems from the tendency of the model to learn pseudo-robust features (i.e., non-generalizable shortcuts). To mitigate this, we propose ADAPT (Adversaria...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 33 papers

- **2026-08-21** — Adriana Watson, Marco Bücheler, Grant Richards — [From Regulation to Implementation: A Critical Evaluation of LLM-Assisted Regulatory Compliance in Industry](http://arxiv.org/abs/2608.21317v1)
  <details><summary>📄 Abstract</summary>
  The European Union (EU) has emerged as a leading regulatory body in the development of sustainability and privacy regulations. While new regulation requirements vary, many include a documentation artifact to ensure compliance. Notably, the Ecodesign for Sustainable Products Regulation (ESPR) introduces Digital Product Passports (DPPs) for life cycle transparency, while the General Data Protection Regulation (GDPR) mandates Data Protection Impact Assessments (DPIAs) to mitigate privacy risks. Cre...
  </details>

- **2026-08-21** — Lekang Jiang, Wenjun Sun, Stephan Goetz — [Benchmarking Patent Drafting from Inventor-Style Disclosures](http://arxiv.org/abs/2608.21249v1)
  <details><summary>📄 Abstract</summary>
  While recent large language models (LLMs) have achieved promising results on individual patent drafting tasks, they fundamentally fail to investigate the core challenge of real-world patent drafting: generating a complete and legally coherent patent application directly from early-stage invention materials. Prior work predominantly assumes later-stage, highly structured, or already legalistic inputs. However, real patenting workflows begin with informal, de-legalized disclosures authored by inve...
  </details>

- **2026-08-21** — Junseok Kim, Nakyeong Yang, Kyomin Jung — [Personalized Privacy Control in LLMs via Attention Head Intervention](http://arxiv.org/abs/2608.21209v1)
  <details><summary>📄 Abstract</summary>
  The rise of agentic AI enables LLMs to access diverse user data, raising critical privacy concerns. Prior work on contextual privacy studies whether LLMs regulate information disclosure according to context-dependent norms. However, acceptable disclosure boundaries may vary across users even within the same context. To address this limitation, we introduce \textit{personalized privacy}, which incorporates user-specific disclosure preferences into privacy control. We further present P3Bench~(\tex...
  </details>

- **2026-08-21** — Dimitri Staufer, David Hartmann, Ibrahim Baroud — [No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation](http://arxiv.org/abs/2608.21206v1)
  <details><summary>📄 Abstract</summary>
  Person names are widely used as prompt variables in LLM evaluations of factuality, privacy leakage, bias and abstention, but when a name's evidential status is uncontrolled, measurements may conflate memorisation, retrieval, name priors and wrong-person attribution. We operationalise an unknown name as one with plausible First-Last form, no indexed full-name evidence, and no ambiguity signals under a documented validation run, and introduce PUN (Plausible Unknown Names), a protocol for construct...
  </details>

- **2026-08-21** — Sara Malacarne, Andrea Ceni, Claudio Gallicchio — [Free-Probability Kernels for Zero-Rollout Hyperparameter Selection in Reservoir Computing](http://arxiv.org/abs/2608.20998v1)
  <details><summary>📄 Abstract</summary>
  Reservoir computing (RC) couples a fixed recurrent dynamical system with a trained lightweight readout, but this efficiency is partly lost during hyperparameter selection: the recurrent gain, input scale, and leakage rate determine the reservoir's stability and temporal processing regime and are usually tuned through many rollouts. We introduce a deterministic, pilot-informed selector for leaky linear reservoirs followed by coordinate-wise nonlinear features. Free probability yields cross-lag pr...
  </details>

- **2026-08-21** — Jinzhao Wang, Kunrun Lu, Yuanlin Li et al. — [Artificial Anisotropy Induced Bound States in the Continuum for Integrated Photonic Waveguide](http://arxiv.org/abs/2608.20992v1)
  <details><summary>📄 Abstract</summary>
  Bound states in the continuum (BICs) enable counterintuitive light confinement without radiation loss, providing a powerful foundation for integrated photonic waveguides. However, existing BIC waveguides are predominantly realized through geometry-dependent designs, where the BIC condition is restricted to narrowly defined structural parameters, limiting design flexibility and practical applicability. Artificial optical anisotropy is introduced as a new design paradigm for BIC waveguides. Implem...
  </details>

- **2026-08-21** — Christoph Nirschl, Magdalena Glas, Gerhard Messmann et al. — [Chat First, Worry Later: Understanding Individuals' Privacy Perceptions Using ChatGPT in a Work Context](http://arxiv.org/abs/2608.20789v1)
  <details><summary>📄 Abstract</summary>
  Generative Artificial Intelligence (GenAI) tools like ChatGPT, which can generate human-like responses from vast amounts of textual data, are increasingly transforming work routines across various fields, including education, healthcare, and IT. This integration, however, raises privacy concerns and questions the readiness of both environments and individuals. To investigate this issue, we conducted a user study with $N=224$ participants from a range of different employment sectors that have int...
  </details>

- **2026-08-20** — Jaiden Fairoze, Neal Mangaokar, Kamalika Chaudhuri et al. — [Inadvertent Context Leakage in Language Models](http://arxiv.org/abs/2608.19857v1)
  <details><summary>📄 Abstract</summary>
  For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert c...
  </details>

- **2026-08-20** — Yuki Itabashi, Hiroto Sawada, Mare Hirose et al. — [Enhancing Privacy in Federated Learning via Dual Obfuscation of Gradients and Training Images](http://arxiv.org/abs/2608.19650v1)
  <details><summary>📄 Abstract</summary>
  Federated learning enables collaborative model training while keeping data locally at each client; however, recent studies have shown that training data can be reconstructed from shared model updates. To address this issue, this paper proposes a dual obfuscation method that enhances robustness against image restoration attacks by jointly obfuscating updated information and training images. The proposed method combines a robustness enhancement technique based on random binary weights, which rando...
  </details>

- **2026-08-20** — Ye Tao, Hong Shen, Hui Tian et al. — [AEGIS: Attention-Embedding Gradient Isolation Shield - Triple-Channel Gradient Masking for Privacy-Preserving Federated LLM Fine-Tuning](http://arxiv.org/abs/2608.19534v1)
  <details><summary>📄 Abstract</summary>
  Gradient inversion attacks recover private training text from gradients shared in federated learning, posing a serious threat to collaborative model training. Through our analysis of transformer gradient structure, we identify three channels through which private token information leaks: the attention output projection gradient exposes a low-rank subspace that encodes input embeddings (Channel 1), the embedding gradient's row-norm sparsity directly reveals which tokens are present (Channel 2), a...
  </details>

- **2026-08-20** — Jingtao Zhang, Haorui Gao, Youqing Liang et al. — [Scale-Separated Conditioning for Style-Encoder-Free Diffusion Stylization](http://arxiv.org/abs/2608.19719v1)
  <details><summary>📄 Abstract</summary>
  Reference-based diffusion stylization requires separating target geometry from transferable appearance. Existing tuning-based methods often rely on aligned content-style-target triplets or auxiliary visual encoders, which increases data cost and can transfer unintended scene structure from the style reference. We propose SEFS (Style-Encoder-Free Stylization), a style-encoder-free conditioning framework for diffusion transformers. SEFS forms style tokens from stochastic low-resolution crops of si...
  </details>

- **2026-08-20** — Konstantin Chesnokov, Chingiz Mingazov — [Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient Bi-Encoder](http://arxiv.org/abs/2608.19957v1)
  <details><summary>📄 Abstract</summary>
  Natural language code retrieval is a rapidly evolving task in computer science. However, the 1C:Enterprise ecosystem combines Russian syntax with highly domain-specific terminology, for which open datasets and specialized models have been virtually non-existent. We present a comprehensive pipeline for 1C code retrieval: an open benchmark of 3,413 real-world, PII-scrubbed query-code pairs, a reproducible evaluation harness, and a specialized bi-encoder. To overcome scarce labeled data, we fine-tu...
  </details>

- **2026-08-20** — Tatsuya Amano, Hirozumi Yamaguchi — [Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation](http://arxiv.org/abs/2608.19778v1)
  <details><summary>📄 Abstract</summary>
  Pedestrian simulators need a behaviour rule for every agent, but privacy usually limits the data for setting one to aggregate statistics, namely zone-level device counts and origin-to-destination (OD) flows, with no individual trajectories. Such aggregates under-determine individual behaviour, because many different sets of decisions reproduce the same counts. We fine-tune a language model crowd agent so that the simulated population matches the observed destination composition, the fraction of ...
  </details>

- **2026-08-19** — Kelly Yuan, Ronald Liu, Daniel Crawford et al. — [Multi-Tier Mentorship with AI-Assisted Development: Authentic Engineering for K-12 and Undergraduates](http://arxiv.org/abs/2608.19379v1)
  <details><summary>📄 Abstract</summary>
  K-12 students often possess creative engineering ideas but lack technical skills to build them, while undergraduates have coding expertise but few opportunities to lead real-world projects or mentor others. The rapid development of AI-assisted tools offers a potential bridge to connect these groups, yet the structure for effective K-12 and university collaborations remains underexplored. This paper introduces a multi-tiered mentorship framework enabling high school students to engage in authenti...
  </details>

- **2026-08-19** — Shiyu Miao, Yunlong Mao, Zirui Huang et al. — [Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language Model Split Learning](http://arxiv.org/abs/2608.18767v1)
  <details><summary>📄 Abstract</summary>
  Gradient matching attacks (GMAs) in LLM split learning (SL) rely on a critical yet underexplored assumption: the gradient exposed at the split interface is a faithful derivative of the client's full-label training objective. This gradient-objective consistency allows a curious server to recover private labels by searching for a sequence whose induced gradient explains the observation. We propose Gradient Mirage, a defense that breaks this consistency without discarding the optimization utility o...
  </details>

- **2026-08-19** — Keiyu Nosaka, Yamato Suetake, Yuichi Takano et al. — [Geometric Data Perturbation with Noisy-Anchor Alignment for Privacy-Preserving Collaborative Learning](http://arxiv.org/abs/2608.18749v1)
  <details><summary>📄 Abstract</summary>
  Geometric Data Perturbation (GDP) enables one-shot, privacy-preserving collaborative learning: each participant applies a distance-preserving transformation to its private data and uploads only the resulting representation to a central analyst. We study GDP under analyst-participant collusion, in which the analyst combines all uploaded representations with the private data and transformations disclosed by colluding participants to recover a non-colluding participant's private data. Participant-s...
  </details>

- **2026-08-19** — Tianwei Mu, Yue Wang, Mingzhe Yuan et al. — [Verifiable abstention makes AI leak diagnosis accountable in water distribution networks](http://arxiv.org/abs/2608.18836v1)
  <details><summary>📄 Abstract</summary>
  Utilities lose a substantial share of treated water to leakage, yet rarely trust artificial-intelligence localizers to dispatch crews: guessing everywhere cannot justify excavation. The gap is accountability, not accuracy: no method proves when it should not act. Here we recast leak localization as decision-making under verifiable abstention. A physics-grounded executor agent falsifies hypotheses (leak, demand, sensor, valve) against a digital twin; an independent supervisor agent, with a large-...
  </details>

- **2026-08-19** — Mohammad Zamani, Fatemeh Ziaeetabar — [Vision-Language Models for Egocentric Video: From Hand-Object Interaction to Embodied AI](http://arxiv.org/abs/2608.18671v1)
  <details><summary>📄 Abstract</summary>
  Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior. This perspective is increasingly important for wearable intelligence, assistive systems, human--robot interaction, and embodied AI, yet it introduces challenges including ego-motion, occlusion, small active objects, viewpoint-dependent appearance, and long-range temporal dependencies. Vision--language models (VLMs) offer a promising...
  </details>

- **2026-08-19** — Kirandeep Kaur, Vinayak Gupta, Tanya Roosta et al. — [Report on The 1st Workshop on Human-Centered Proactive and Personalized Agents for Interactive Information Access at CHIIR 2026](http://arxiv.org/abs/2608.18638v1)
  <details><summary>📄 Abstract</summary>
  Interactive information access is increasingly moving beyond reactive query-response paradigms toward agentic systems that can personalize interaction, retain context, infer latent needs, recommend next steps, and initiate support. This shift creates new opportunities for adaptive and context-aware assistance, while also raising important questions about autonomy, privacy, trust, transparency, user welfare, and evaluation. The First Workshop on Human-Centered Proactive and Personalized Agents fo...
  </details>

- **2026-08-19** — Valentin Romanov, Monique Bax, Steven Niederer — [Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models](http://arxiv.org/abs/2608.19025v1)
  <details><summary>📄 Abstract</summary>
  Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLM...
  </details>

- **2026-08-19** — Qi Qin, Jiajie Zhu, Dali Chen et al. — [GEAR: Generative Expansion and Real Anchoring for Two-Stage Distillation of Tabular Foundation Models](http://arxiv.org/abs/2608.18849v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) achieve strong performance through in-context learning, but context-dependent inference imposes substantial latency and memory costs, hindering large-scale deployment. We propose GEAR (\emph{Generative Expansion and Real Anchoring}), a modular two-stage framework that distills TFMs into lightweight MLP or tree-based predictors that can be deployed on commodity CPUs. Stage 1 uses synthetic covariates solely as teacher-query locations and trains the student on soft...
  </details>

- **2026-08-19** — Yanghong Lin, Li Fang, Tianyu Li et al. — [COSTA: A Cluster-Centric Paradigm for Annotation-Free Open-Set Semantic Segmentation of Aerial Point Clouds with Domain Shifts](http://arxiv.org/abs/2608.18479v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation of aerial point cloud is trapped in a generalization crisis under distinct domain shifts. While test-time adaptation offers a privacy-preserving and computationally efficient way to adapt pre-trained models to unlabeled target-domain data during inference, existing methods, bound to closed-set label assumptions and non-scalable point-wise segmentation pipelines, still struggle with semantic shifts. We ask: can we adapt any given pre-trained aerial point cloud segmentation m...
  </details>

- **2026-08-18** — Charles de Bourcy, Sahra Ghalebikesabi, Avi Schwarzschild et al. — [Model Card for OpenAI Privacy Filter](http://arxiv.org/abs/2608.18274v1)
  <details><summary>📄 Abstract</summary>
  OpenAI Privacy Filter is a compact, bidirectional token-classification model for detecting and redacting personally identifiable information (PII) and secrets in unstructured text. The model is derived from an autoregressively pretrained checkpoint and converted into a bidirectional, banded-attention classifier that labels an input sequence in a single forward pass. A constrained Viterbi decoder produces coherent spans across eight privacy categories and exposes configurable operating points for...
  </details>

- **2026-08-18** — Saurav Kumar Saha, Tom Röhr, Felix Bießmann — [Redakto - The Incognito Tab for LLMs](http://arxiv.org/abs/2608.18260v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are being increasingly used in everyday applications. A major challenge in the context of LLMs or Artificial Intelligence (AI) in general is to ensure privacy when using them, meaning that personally identifiable information (PII) is removed from any text that enters an LLM. These challenges have become more urgent with novel EU legislation. Uncertainty around LLM usage with respect to privacy concerns in EU countries can be a major blocker for the speed of innovatio...
  </details>

- **2026-08-18** — Yufan Zhu, Chao Jin, Khin Mi Mi Aung et al. — [FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models](http://arxiv.org/abs/2608.17442v2)
  <details><summary>📄 Abstract</summary>
  Processing long, sensitive documents with machine-learning models requires efficient, privacy-preserving long-context inference. Prior private inference systems optimize or distribute encrypted Transformer attention, but its quadratic token-pair work remains the bottleneck as sequence length grows. Selective state-space models (SSMs) offer linear-time recurrence, yet direct encrypted implementation incurs linear multiplicative depth, sequence-wide state residency, or dense FHE-MPC conversion. We...
  </details>

- **2026-08-18** — Maosen Zhang, Jianshuo Dong, Boting Lu et al. — [The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges](http://arxiv.org/abs/2608.17829v1)
  <details><summary>📄 Abstract</summary>
  LLMs increasingly rely on external contexts, such as pre-defined system prompts or retrieved documents, to improve generation quality. However, processing these contexts alongside user queries creates an attack surface: adversarial inputs can induce models to disclose them. Prior probing studies suggest that leakage-related signals emerge in hidden states, yet the need to extract these states poses additional deployment challenges. In this paper, we explore whether this internal signal leaves a ...
  </details>

- **2026-08-18** — Sarvesh Gharat, Junpei Komiyama — [SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models](http://arxiv.org/abs/2608.17501v1)
  <details><summary>📄 Abstract</summary>
  Recent efforts toward fully automated AI scientists have demonstrated that language-model agents can generate hypotheses, execute experiments, and draft scientific manuscripts. However, during the early stages of research, when research problems are formulated, these AI scientists often rely heavily on proprietary frontier models. Their proposals are shaped by opaque parametric knowledge and by literature searches conditioned on the proposals themselves. Such knowledge is effectively a black box...
  </details>

- **2026-08-18** — Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez — [An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning](http://arxiv.org/abs/2608.17804v1)
  <details><summary>📄 Abstract</summary>
  Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at that level rather than leak, evade, or refuse. We study this specification problem in a controlled LoRA-GRPO RWKU setting, comparing four reward designs that span lexical suppression, a...
  </details>

- **2026-08-18** — Xiangyi Li, Jiajia Guo, Chao-Kai Wen et al. — [Learnware for CSI Feedback: Scene-specific Small Models Can Do Big](http://arxiv.org/abs/2608.17760v1)
  <details><summary>📄 Abstract</summary>
  Intelligent channel state information (CSI) feedback is essential for realizing the high capacity and spectral efficiency goals of future 6G systems, yet existing deep learning solutions face a trade-off between model generalization and scenario-specific performance. Large neural networks generalize well but incur high computational and tuning costs, while small models excel in particular environments but require repetitive costly end-to-end training for each base station (BS). To address these ...
  </details>

- **2026-08-18** — Yufan Zhu, Chao Jin, Khin Mi Mi Aung et al. — [FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models](http://arxiv.org/abs/2608.17442v1)
  <details><summary>📄 Abstract</summary>
  Processing long, sensitive documents with machine-learning models requires efficient, privacy-preserving long-context inference. Prior private inference systems optimize or distribute encrypted Transformer attention, but its quadratic token-pair work remains the bottleneck as sequence length grows. Selective state-space models (SSMs) offer linear-time recurrence, yet direct encrypted implementation incurs linear multiplicative depth, sequence-wide state residency, or dense FHE-MPC conversion. We...
  </details>

- **2026-08-18** — Sabari Shanmugam, Nick Barnes, Kerry Taylor — [Spectral Gradient Orthogonalization Improves Differentially Private Training at Scale](http://arxiv.org/abs/2608.17415v1)
  <details><summary>📄 Abstract</summary>
  Differentially private training adds isotropic Gaussian noise to clipped gradients, corrupting every singular direction equally. In vision models, where spatial correlation concentrates gradient energy into a low-rank subspace, most of this noise falls in directions that carry little signal. Spectral gradient orthogonalization via polar decomposition is introduced as a post-processing step that recovers directional signal from the noisy gradient's low-rank structure at zero additional privacy co...
  </details>

- **2026-08-18** — Weiran Wang, Hongxiang Shi, Huitao Tang et al. — [ArguLens: An Open-Source System for Automated Essay Scoring and Label-Aware Feedback Generation](http://arxiv.org/abs/2608.17356v1)
  <details><summary>📄 Abstract</summary>
  Most automated essay scoring (AES) systems output a single holistic score without interpretable evidence and rely on closed APIs that introduce data privacy and cost barriers. We present ArguLens, an opensource, locally deployable system that decomposes AES into three decoupled components: a discourse-move classifier (Qwen2.5-7B-Instruct fine-tuned with LoRA on PERSUADE 2.0), a grade-independent LightGBM scorer over 31 linguistic and discourse features, and a label-aware feedback generator serve...
  </details>

- **2026-08-18** — Chenhao Xue, Raslen Guesmi, Siwei Feng et al. — [Temporal Leakage in Financial News NLP: A Multi-Architecture Audit with a Regime-Specific M&A Signal](http://arxiv.org/abs/2608.17223v1)
  <details><summary>📄 Abstract</summary>
  Financial-news direction prediction has become a popular NLP benchmark, yet reported gains depend critically on whether the train-test split is chronological or random, i.e., on temporal leakage. We audit this dependence on a 49,799-article corpus across 16 feature-model combinations spanning TF-IDF, MiniLM, FinBERT, and fine-tuned RoBERTa-large / DeBERTa-v3-large, plus separate zero/few-shot and LoRA probes of Llama-3 and Qwen2.5 LLMs: random splits inflate MCC by $1.1\times$ to $6.5\times$, tr...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-19** — Ramneet Kaur, Pradyumna Chari, Ramesh Raskar et al. — [Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](http://arxiv.org/abs/2608.19161v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysi...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 16 papers

- **2026-08-21** — Zhibo Zhang, Zhen Ouyang, Ling Shi et al. — [RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts Language Models](http://arxiv.org/abs/2608.21236v1)
  <details><summary>📄 Abstract</summary>
  Representation engineering offers a lightweight means of controlling language-model behavior by modifying intermediate hidden states, but its direct application to Mixture-of-Experts (MoE) models introduces a structural mismatch. We first verify this failure mode through a series of empirical studies and find that preserving clean routing substantially recovers steering performance and that routing is more sensitive to semantic content than to behavioral changes under controlled content. Motivat...
  </details>

- **2026-08-21** — Pasquale Malacaria, Yunxiao Zhang — [Structured but Fragile: On the Limits of LLMs in Cybersecurity Decision-Making](http://arxiv.org/abs/2608.20966v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in cybersecurity workflows, yet it remains unclear whether they can perform structured security reasoning or merely rely on superficial cues and prior knowledge. We study this question in the context of defence selection over attack graphs derived from real-world threat scenarios, including ransomware, supply-chain compromise, cloud abuse, Kubernetes attacks, POS malware, and ICS/OT intrusion. Given a budget constraint, LLMs must select security...
  </details>

- **2026-08-21** — Chengxiao Wang, Enyi Jiang, Xiaojing Liao et al. — [CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment](http://arxiv.org/abs/2608.21278v1)
  <details><summary>📄 Abstract</summary>
  Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter. CLEAR aims to reduce harmful completions while avoi...
  </details>

- **2026-08-21** — Ruichen Yao, Tejna Dasari, Gulshat Baispay et al. — [Beyond Truth Discovery: A Two-Stage Framework to Assess the Severity of False Claim during Disasters](http://arxiv.org/abs/2608.20983v1)
  <details><summary>📄 Abstract</summary>
  False information spreads rapidly on social media during disasters and can undermine emergency response efforts, public trust, and crisis communication. Existing research primarily focuses on determining whether social media posts contain false information, but provides limited insight into the specific false claims embedded within posts and the severity of individual false claims. To address the limitations, we propose a two-stage framework to assess the severity of false claims during disaster...
  </details>

- **2026-08-21** — Huizu Lin, Chengkai Huang, Tianqi Gao et al. — [AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization](http://arxiv.org/abs/2608.21292v1)
  <details><summary>📄 Abstract</summary>
  Skills play different roles as an agent's policy evolves: they should first provide learnable knowledge, then support capability formation, and finally be invoked only when they improve individual decisions. Existing methods rarely model this lifecycle. They either keep skills outside the model, fully internalize them, or select among internalization and utilization objectives through noisy task-level success rates. Such designs fragment training and assign uniform importance to actions within t...
  </details>

- **2026-08-21** — Jiekang Feng, Zhihe Fan, Yunqi Zhu et al. — [A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration](http://arxiv.org/abs/2608.21099v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal object detection is essential for robust scene understanding in challenging conditions, including low-light and adverse environments. Recent vision foundation models (e.g., DINOv3) have exhibited strong representation capabilities, yet adapting them to multi-modal scenarios remains challenging. Existing dense cross-modal fusion strategies often force heterogeneous modalities to interact indiscriminately, which may introduce redundant information and disrupt the valuable pre-trained r...
  </details>

- **2026-08-20** — Sahil Kale, Ian Harris — [ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models](http://arxiv.org/abs/2608.20338v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly require selective removal of harmful or sensitive knowledge, called unlearning, yet existing methods and benchmarks fail to evaluate this capability completely. Current approaches rely on disjoint forget and retain sets composed of independent facts, and measure success using simple and direct factual recall. This framing fails to capture a key requirement of unlearning, namely the ability to eliminate harmful behaviors while preserving benign and benefi...
  </details>

- **2026-08-20** — Yejin Bang, Kirsty Fielding, Brandan Oliver et al. — [ContractScrub: A benchmark for final review of legal contracts](http://arxiv.org/abs/2608.20204v1)
  <details><summary>📄 Abstract</summary>
  Legal work, with its heavy reliance on processing large amounts of text, is often considered one of the domains most exposed to the use of LLMs. Contract ``scrubbing,'' the final review of transactional agreements for errors and inconsistencies, is a particularly suitable task for automation, because it is routine, painstaking work requiring detailed attention to long documents. Scrubbing also seems to align naturally with the general capabilities expected of frontier LLMs around long-context re...
  </details>

- **2026-08-20** — Mohamed Akrout, Olivera Kotevska, Dan Wilson — [Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics](http://arxiv.org/abs/2608.19579v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in high-stakes applications, yet their tendency to generate toxic, harmful, or policy-violating content poses significant risks. Detecting these unsafe outputs efficiently in a black-box manner remains an open challenge. In this paper, we extend a recently proposed dynamical systems framework designed for hallucination detection to LLM safety classification. By projecting both prompts and responses into high-dimensional embedding spaces and ...
  </details>

- **2026-08-19** — Md Akram Khan, Daniel Rodriguez-Cardenas, Alejandro Velasco Dimate et al. — [CauSec: Unboxing the Causal Drivers of Static Vulnerability Analysis Performance](http://arxiv.org/abs/2608.18876v2)
  <details><summary>📄 Abstract</summary>
  Static Application Security Testing (SAST) tools are widely used in both industry and academia. Such tools often make design choices that sacrifice detection to achieve higher performance, i.e., increased precision, decreased runtime, or increased scalability. These design choices rely on certain assumptions regarding the target code or the analysis technique itself. Hence, the assumptions directly impact the detection outcome through the design choices they influence. This motivates a key quest...
  </details>

- **2026-08-19** — Md Akram Khan, Daniel Rodriguez-Cardenas, Alejandro Velasco Dimate et al. — [CauSec: Unboxing the Causal Drivers of Static Vulnerability Analysis Performance](http://arxiv.org/abs/2608.18876v1)
  <details><summary>📄 Abstract</summary>
  Static Application Security Testing (SAST) tools are widely used in both industry and academia. Such tools often make design choices that sacrifice detection to achieve higher performance, i.e., increased precision, decreased runtime, or increased scalability. These design choices rely on certain assumptions regarding the target code or the analysis technique itself. Hence, the assumptions directly impact the detection outcome through the design choices they influence. This motivates a key quest...
  </details>

- **2026-08-18** — Nilutpaul Sarker Yash, Tirtho Roy, Ushashi Bhattacharjee — [Towards Reversible Forgetting: Managing Obsolete Knowledge in Continual Enterprise AI Agents](http://arxiv.org/abs/2608.18177v1)
  <details><summary>📄 Abstract</summary>
  Continual learning has traditionally treated forgetting as a failure, emphasizing preservation of previously acquired knowledge as environments evolve. We argue that this objective is incomplete for enterprise AI agents operating in non-stationary environments, where customers, policies, tools, workflows, regulations, and market conditions change over time. Indiscriminate retention can allow obsolete knowledge to influence decisions, creating negative transfer and operational risk. We therefore ...
  </details>

- **2026-08-18** — Bowen Sun, Zhengyue Zhao, Xiaogeng Liu et al. — [Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services](http://arxiv.org/abs/2608.17445v1)
  <details><summary>📄 Abstract</summary>
  Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answ...
  </details>

- **2026-08-18** — Hamidreza Saffari, Francesco Pierri — [Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study](http://arxiv.org/abs/2608.17583v1)
  <details><summary>📄 Abstract</summary>
  Online video platforms can expose young users to harmful content, but independent audits remain difficult because video annotation is costly and moderation judgments vary across languages. We audit TikTok in France, Italy, and Sweden with sockpuppet accounts representing four age personas (13, 16, 19, 40), collecting 36,971 videos from passive For-You-page scrolling and active sessions that scroll, search for harm keywords, and scroll again. To scale annotation, we validate four multimodal LLMs ...
  </details>

- **2026-08-18** — Zhen Zhang, Ahmad Hafez, Amr Alanwar — [Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment](http://arxiv.org/abs/2608.17713v1)
  <details><summary>📄 Abstract</summary>
  Agent evaluations and trace-based learning often compare outputs across transformed views through a post-response correspondence treated as neutral preprocessing. We show that this correspondence is a measurement intervention: omitting it can manufacture sensitivity, an over-aggressive map can manufacture invariance, and multiple optimal correspondences can leave mechanism labels and signed learning credit unidentified. We develop a validity theory and audit with three components: two-sided vali...
  </details>

- **2026-08-18** — Cesar Borja, Breck A. McCollum, Jarret E. Byrnes et al. — [Leveraging existing sparse point annotations for benthic imagery dense segmentation](http://arxiv.org/abs/2608.17561v1)
  <details><summary>📄 Abstract</summary>
  The health of marine ecosystems is a critical indicator of global environmental change, yet the physical constraints of underwater observation and the intrinsic challenges of processing marine imagery severely limit the scalability of systematic monitoring. While recent visual foundation models such as the Segment Anything Model (SAM) series show great promise, they still struggle with the fine-grained recognition required in these complex scenarios and still require expert supervision. Our work...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-08-21** — Derek R. Benham, Joshua G. Mangelson — [The Coastline as a Structural Constraint: Harnessing Scene Geometry for Autonomous Surface Vessel Localization](http://arxiv.org/abs/2608.21276v1)
  <details><summary>📄 Abstract</summary>
  Coastal environments contain rich, largely unexploited geometric structure capable of providing globally referenced localization cues. In this work, we present two complementary localization frameworks that exploit shoreline and water-surface geometry for GPS-denied autonomous surface vessel localization. The first framework leverages LiDAR observations of the water surface to estimate roll, pitch, and heave (vertical motion), while recovering global position and heading through direct registrat...
  </details>

- **2026-08-21** — Jiayi Li, Sanjana Menon, Brett Frischmann et al. — [Affective Context Amplifies Sycophancy in LLM Responses](http://arxiv.org/abs/2608.21242v1)
  <details><summary>📄 Abstract</summary>
  As conversational companions, large language models (LLMs) often have access to users' emotional states. We study how this affective context modulates LLM sycophancy in subjective, evaluative interactions, where users share actions or opinions that invite feedback. Drawing on ingratiation theory, we measure sycophancy as the divergence between a model's independent evaluation and its user-facing response, elicited by presenting the same content as either a third-party account or the user's own d...
  </details>

- **2026-08-21** — Swetha Varadarajan, Darrell Whitley — [Fine-Grain GPU Parallelization of the Generalized Partition Crossover for Large-Scale Traveling Salesman Problems](http://arxiv.org/abs/2608.21233v1)
  <details><summary>📄 Abstract</summary>
  The Traveling Salesman Problem (TSP) is one of the most extensively studied NP-hard optimization problems. Genetic Algorithm (GA)-based solvers, such as the Edge Assembly Crossover (EAX), achieve state-of-the-art performance on many benchmark instances. However, the scalability of these approaches in massively parallel architectures remains limited because crossover operations involve irregular memory access patterns, graph traversals, and sequential dependencies. Existing GPU-based TSP solvers ...
  </details>

- **2026-08-21** — Tengteng Lei, Prabodh Katti, Rashi Dutt et al. — [Event-triggered Implicit Perturbation for Zeroth-Order Fine-Tuning of Spiking Transformers](http://arxiv.org/abs/2608.21223v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization estimates gradients using only forward-pass evaluations, making it suitable for fine-tuning non-differentiable, event-driven spiking neural networks (SNNs). However, its deployment on in-memory computing (IMC) accelerators is constrained by the repeated read-modify-write (RMW) operations arising from explicit weight perturbation and the prohibitive hardware footprint of random number generators (RNGs) for statistically independent per-weight perturbations. To addre...
  </details>

- **2026-08-21** — Varun Giridhar, Anant Khandelwal, Jeremy A. Collins et al. — [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](http://arxiv.org/abs/2608.21204v1)
  <details><summary>📄 Abstract</summary>
  Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations. Reinforcement Learning fine-tuning offers a path to self-improvement but has proven difficult to scale to the multi-billion-parameter models underpinning modern robot policies. We propose Q-Planning, which equips a large visuomotor BC policy with a small off-policy...
  </details>

- **2026-08-21** — Jie Xu, Na Zhao — [Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding](http://arxiv.org/abs/2608.21136v1)
  <details><summary>📄 Abstract</summary>
  Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks. To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D ...
  </details>

- **2026-08-21** — Wei Lin, Tao Zhou, Zhaofei Xie et al. — [Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda](http://arxiv.org/abs/2608.21107v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are moving from code completion toward repository-scale agents that retrieve context, edit files, execute tools, and participate in security-sensitive workflows. The evidence for these systems, however, remains divided between software engineering evaluations centered on functional task completion and software security evaluations centered on vulnerability detection, secure generation, or exploit-oriented validation. This evidence-centered structured survey synthesiz...
  </details>

- **2026-08-21** — Angel Mary John, Vipin Kumar Singh, Jerrin Thomas Panachakel — [Can Legal AI Know When It Is Wrong? And Do Students Know When It Is?](http://arxiv.org/abs/2608.21089v1)
  <details><summary>📄 Abstract</summary>
  Integrating Large Language Models (LLMs) into the Indian judiciary promises access to justice but introduces severe risks. We identify the 'inertia of confidence'--an overconfidence phenomenon analogous to the Dunning-Kruger effect where LLMs provide incorrect legal verdicts with near-maximum confidence, driven by a hypothesized 'precedent overfitting' bias. Phase I of our socio-technical audit tested ChatGPT (GPT-5.2), Meta AI, and Perplexity AI on a 60-case battery regarding the Indian Contrac...
  </details>

- **2026-08-21** — Yipeng Wei, Zahra Hoodbhoy, Emily R. Smith et al. — [Knowledge-guided Transfer Prediction In Underrepresented Populations: A GRU-D-Static Framework For Maternal And Neonatal Outcomes](http://arxiv.org/abs/2608.21073v1)
  <details><summary>📄 Abstract</summary>
  Integrating summary-level scientific knowledge into neural network models provides a practical strategy for transferring prediction models trained on adequately sampled source cohorts to underrepresented target populations, where individual-level data in the target domain are often limited or unavailable. In this study, we propose transfer prediction strategies incorporating external summary-level scientific knowledge and illustrate its application on the PRISMA Maternal and Neonatal Health Stud...
  </details>

- **2026-08-21** — Dojun Hwang, Seunghan Lee, Cheonyoung Park et al. — [Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders](http://arxiv.org/abs/2608.20801v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have significantly advanced reranking in recommendation, effectively leveraging item-side information remains challenging. Real-world items are described by vast, heterogeneous, and unstructured metadata, where decision-relevant signals are often implicit, noisy, or buried in long descriptions. Moreover, feature salience is highly context-dependent, varying not only across items but also across users. Existing methods often rely on item titles, fixed attributes...
  </details>

- **2026-08-21** — Hui Lu, Zhijie Peng, Yuqi Lin et al. — [CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models](http://arxiv.org/abs/2608.20791v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions. We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks. CertVLA proposes a calibrated region of behaviorally consistent actions, while deterministic covering masks ensure that at least one checked prediction is attack-free....
  </details>

- **2026-08-21** — Byeonggwon Lee, Sanggi Lee, Siwoo Lee et al. — [M2Depth: Unifying Monocular Depth Foundation Priors with Multi-View Stereo](http://arxiv.org/abs/2608.20788v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based Multi-View Stereo (MVS) has advanced significantly but often generalizes poorly to unseen scenes, particularly in occluded areas or regions with limited view overlap. To mitigate this, recent approaches integrate Depth Foundation Models (DFMs) into MVS pipelines to provide monocular depth priors. However, existing methods typically rely on a static, one-way fusion scheme, which fails to fully exploit the complementary strengths of both modalities. We propose a novel framework...
  </details>

- **2026-08-20** — Cheng Xu, Nan Yan, Liming Chen et al. — [Phantom Gains: Auditing Self-Improvement Against a Measured Null](http://arxiv.org/abs/2608.20290v1)
  <details><summary>📄 Abstract</summary>
  Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses. Tracking these transitions means differencing two noisy estimates, leaving them vulnerable to measurement artifacts. Auditing three rounds of rank-$32$ LoRA self-training on Qwen3-8B against a frozen control pushed through the identical pipeline, we identify seven measurement failures, each of which inverts a reported finding when its control is absent. Se...
  </details>

- **2026-08-20** — Laura M. Guzmán-Rincón, George R. E. Bradley, Joel Kandiah et al. — [GENIE: Generative Neural Inference for Epidemics](http://arxiv.org/abs/2608.20253v1)
  <details><summary>📄 Abstract</summary>
  The SARS-CoV-2 pandemic highlighted the ongoing risk infectious diseases pose to society and the value of reliable information on the likely future burden. When forecasting an epidemic at fine spatial resolution, traditionally used mechanistic compartmental model struggle to capture highly complex granular transmission dynamics, resulting in inaccurate and overconfident forecasts. However, detailed Agent-Based Models (ABMs), are challenging to calibrate and are too computationally expensive to u...
  </details>

- **2026-08-20** — Zhaokun He, Kangbiao Shi, Axi Niu et al. — [DPC-Net: Dual-Prior Collaborative Network for All-in-One Image Restoration](http://arxiv.org/abs/2608.20141v1)
  <details><summary>📄 Abstract</summary>
  All-in-One Image Restoration (AiOIR) aims to handle diverse degradations within a unified model. However, existing methods often overlook image semantics in degradation modeling and lack low-level visual priors during reconstruction, leading to structural distortions and semantic inconsistencies. To address these issues, we propose a novel Dual-Prior Collaborative Network (DPC-Net), which achieves high-quality restoration by jointly exploiting degradation-semantic coupled priors and low-level vi...
  </details>

- **2026-08-20** — Linhan Cao, Siyuan Li, Jun Lan et al. — [ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation](http://arxiv.org/abs/2608.20122v1)
  <details><summary>📄 Abstract</summary>
  Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable to humans but challenging for models to localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text, while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task and introduce \textbf{A...
  </details>

- **2026-08-20** — Dayang Liang, Lang Feng, Bo An et al. — [SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning](http://arxiv.org/abs/2608.19842v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative methods estimate policy advantages from multiple rollouts, avoiding the substantial memory overhead of conventional proximal policy optimization (PPO) and achieving strong performance on long-horizon interactive tasks. Despite their success, recent studies revealed three limitations: (1) Lack explicit value generalization and effective temporal credi...
  </details>

- **2026-08-20** — Yifei Sun, Yubing Li, Yannick Benezeth et al. — [Simulation-to-Real First-Break Segmentation for Efficient Inversion in Musculoskeletal Ultrasound Tomography](http://arxiv.org/abs/2608.19828v1)
  <details><summary>📄 Abstract</summary>
  Full-waveform inversion (FWI) is a promising strategy for quantitative musculoskeletal ultrasound computed tomography (USCT), but bone-related scattering, attenuation, and signal degradation make it highly sensitive to the accuracy of the initial acoustic-property distributions and prone to cycle skipping. First-arrival traveltimes provide important kinematic information for initial-model construction, yet conventional trace-wise picking is unreliable when arrivals are weak, spatially heterogene...
  </details>

- **2026-08-20** — Tenghui Huang, Jiawen Kang, Dongning Liu et al. — [Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models](http://arxiv.org/abs/2608.19680v1)
  <details><summary>📄 Abstract</summary>
  Smart contract vulnerability detection with Large Language Models (LLMs) faces three causally linked challenges. First, new vulnerability categories demand parameter-efficient adaptation, since full retraining is prohibitive for sequentially arriving tasks. Second, training per-task adapters on a shared backbone causes catastrophic forgetting of previously learned vulnerabilities. Third, the resulting multiplicity of adapters must be consolidated into a single model, since task identity is unkno...
  </details>

- **2026-08-20** — Shengshi Yao, Jincheng Dai, Sixian Wang et al. — [Loss-Resilient Semantic Communication over Packet-Loss Networks at Extreme-Low Bandwidth](http://arxiv.org/abs/2608.19590v1)
  <details><summary>📄 Abstract</summary>
  In extreme-low bandwidth network scenarios, generative semantic codecs have emerged as promising solutions to reduce bandwidth cost for visual communications. However, these learned codecs are usually optimized solely for compression efficiency and thus not robust against transmission errors. Corruptions due to packet-loss among these highly compact generative latent representations often cause more critical degradation in fidelity and realism, intensified by the severe error propagation across ...
  </details>

- **2026-08-19** — Euijin Hong, Guannan Qu — [DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule](http://arxiv.org/abs/2608.19491v1)
  <details><summary>📄 Abstract</summary>
  Most modern optimizers form their momentum as an exponential moving average (EMA) of past gradients, forgetting every direction at one fixed rate. However, the inputs a deep network sees during training can be highly anisotropic, with a few directions queried frequently while most are seen rarely. Recent methods address this anisotropy by wrapping extra processing around this buffer, leaving the momentum update itself unchanged. We propose DeltaMomentum, which builds direction-awareness into the...
  </details>

- **2026-08-19** — Haochen Liu, Zhengzhang Chen, Haoyu Wang et al. — [HARP: Hierarchical Adaptive Ranking with Preference-Adaptive Fusion for Query-Based CVE Prioritization](http://arxiv.org/abs/2608.19430v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability prioritization is inherently preference dependent, since the same CVE can receive different remediation priority under different operational preference scenarios. Existing scoring systems and ranking methods typically assume a fixed criterion. In practice, organizations already operate under a preference scenario, but this preference is often implicit and difficult to express as a written prompt instruction, while triage queries usually do not encode it. Past validated triage cases...
  </details>

- **2026-08-19** — Jayjun Lee, Jessica Yin, Asif Rana et al. — [ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](http://arxiv.org/abs/2608.19182v1)
  <details><summary>📄 Abstract</summary>
  We introduce Accelerating Dexterity via Pre-Training (ADEPT), a large-scale reinforcement learning (RL) framework for learning sim-to-real transferable dexterity across high degree-of-freedom (DoF) robot embodiments that can solve long-horizon tasks directly from raw visuo-tactile perception. ADEPT pretrains a dexterous policy on a generic object reposing task, then post-trains downstream policies with this pretrained behavior as a prior. ADEPT enables learning new behaviors that are otherwise d...
  </details>

- **2026-08-19** — Yusen Han, Xuelian Li, Juntao Gao et al. — [Toward Quantum Advantage in Learning Parities with Structured Noise via Lower Bound Optimization of the Condition Number](http://arxiv.org/abs/2608.19122v1)
  <details><summary>📄 Abstract</summary>
  Learning Parities with Structured Noise (LPSN) can be reduced to solving nonlinear Boolean systems. In quantum computing, such systems are typically transformed into Macaulay linear systems and solved via quantum linear system algorithms, a process severely limited by the condition number. To address this, we propose a novel reduction method for Macaulay linear systems. Under the assumptions of Ding et al., we derive a condition number lower bound incorporating a scaling factor.   This reduction...
  </details>

- **2026-08-19** — Davide Romano, Kanak Raj, Jerrod Parker et al. — [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](http://arxiv.org/abs/2608.18931v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine...
  </details>

- **2026-08-19** — Amirreza Sadeghpour, Daryoush Abdollahpour — [Invertible mapping between structured light and vector terahertz emission](http://arxiv.org/abs/2608.18857v1)
  <details><summary>📄 Abstract</summary>
  Terahertz (THz) radiation provides a powerful platform for ultrafast spectroscopy, imaging, and communication, yet deterministic control over its spatial and polarization structure remains challenging. Here we establish a unified framework for generating and synthesizing vectorial THz beams through coherent control of ultrafast photocurrents in semiconductors. By exploiting quantum interference between one- and two-photon excitation pathways driven by femtosecond vector beams, we demonstrate tha...
  </details>

- **2026-08-19** — Sonia Rani Gupta, Nikela Papadopoulou, Miquel Pericàs — [FlashAttention for Scalable Vector Architectures](http://arxiv.org/abs/2608.18656v1)
  <details><summary>📄 Abstract</summary>
  Inference with transformer models on CPUs is increasingly important, especially for Small Language Models (SLMs), where vector architectures are emerging as a promising execution substrate. The attention module is a major bottleneck due to high memory bandwidth requirements; FlashAttention mitigates this by fusing operations to improve data locality and reduce intermediate memory traffic. In this paper, we present FlashAttention-V, a blocked FlashAttention for scalable vector architectures that ...
  </details>

- **2026-08-19** — Yutong Cheng, Changze Li, Qian Cui et al. — [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](http://arxiv.org/abs/2608.18613v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence (CTI) is increasingly consumed not by human analysts but by LLM agents that compose multi-step investigations at query time. The harness side of this shift has matured rapidly (planning loops, tool protocols, context management), but the corpus side has not: threat reports and vulnerability databases are still packaged for retrieval-augmented generation, as opaque chunks behind an embedding index. We argue that this substrate, not model capability, is the bottleneck on ...
  </details>

- **2026-08-19** — Ruiqi Zhang, Hao Zhu, Wenhao Zhang et al. — [ReX-Shot: Single-Image Rephotography via Geometry- and Camera-Grounded Generation](http://arxiv.org/abs/2608.18593v1)
  <details><summary>📄 Abstract</summary>
  Single-image rephotography aims to synthesize new shots of a scene from a single reference image with specified viewpoints, focal lengths, and photographic effects, which are intrinsically coupled in imaging. Existing methods typically treat these factors separately and struggle under joint control: novel-view synthesis may introduce geometric distortions under focal-length changes, while super-resolution and instruction-guided editing remain confined to 2D and cannot reliably extend detail rest...
  </details>

- **2026-08-19** — Mengpeng Yang, Jingxu Yang, Chao Chen et al. — [OmniAlign: A Unified Multilingual Aligner for Word and Sentence Alignment](http://arxiv.org/abs/2608.18474v1)
  <details><summary>📄 Abstract</summary>
  Cross-lingual sequence alignment is fundamental for building and exploiting parallel corpora, spanning mappings from documents and sentences down to words and subwords. Existing tools, however, typically specialize in a single granularity, so practitioners often need separate systems for word- and sentence-level alignment---especially in multilingual and long-text settings. We present OmniAlign, a unified multilingual aligner that supports both word-level and sentence-level alignment with a sing...
  </details>

- **2026-08-18** — Songwei Wu, Rui Zhao, Fan Yang et al. — [EATR-Stereo: Embodiment-Aware Token Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](http://arxiv.org/abs/2608.17453v3)
  <details><summary>📄 Abstract</summary>
  Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that r...
  </details>

- **2026-08-18** — Aniket Wattamwar, Manav Anandani, Mrunal Kakirwar — [The Evaluation Context Protocol (ECP): A Portable Contract for AI Agent Evaluation](http://arxiv.org/abs/2608.19263v1)
  <details><summary>📄 Abstract</summary>
  The evolution of artificial intelligence has necessitated a fundamental shift from evaluating isolated Large Language Models (LLMs) to assessing autonomous agentic architectures. This paper explores the critical methodologies for evaluating AI agents and the essential role of advanced observability infrastructure. We analyze the architectural components of agents and identify the severe limitations of current evaluation paradigms, including benchmark exploitation, the "confidently wrong" phenome...
  </details>

- **2026-08-18** — Kyriakos "Rock" Lambros, Steve Wilson — [Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus](http://arxiv.org/abs/2608.19266v1)
  <details><summary>📄 Abstract</summary>
  The OWASP Top 10 for LLM Applications ranks the risks that a community of security practitioners judges most important. We ask a narrower question: checked against the record of real incidents, does that expert ranking agree with the data? We assembled a large-scale corpus of LLM-security incidents (7,714 snapshotted and 6,639 labeled against the 20-entry taxonomy) drawn from CVE, GHSA, OSV, and AIAAIC, and derived an incident-based ranking with a Bayesian measurement-error model that corrects e...
  </details>

- **2026-08-18** — Stefano Goria — [ClosureBench: A Constructive Benchmark for Compositional Graph Reasoning](http://arxiv.org/abs/2608.18242v1)
  <details><summary>📄 Abstract</summary>
  We introduce ClosureBench, a constructive benchmark for compositional graph-relational reasoning with programmatically verified ground truth. Unlike fixed-test-set benchmarks vulnerable to data contamination, ClosureBench generates instances on demand: each task's reference answer is computed by executing a program in the Ein tensor-logic language, ensuring machine-verified correctness. The benchmark spans 26 task categories at three compositional levels (L1-L3), with difficulty controlled along...
  </details>

- **2026-08-18** — Songwei Wu, Rui Zhao, Fan Yang et al. — [EATR-Stereo: Embodiment-Aware Token Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](http://arxiv.org/abs/2608.17453v2)
  <details><summary>📄 Abstract</summary>
  Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that r...
  </details>

- **2026-08-18** — Javier Aguilar Martín — [An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models](http://arxiv.org/abs/2608.17956v1)
  <details><summary>📄 Abstract</summary>
  In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On th...
  </details>

- **2026-08-18** — Lei Jiang, Ye Wei, Xinyu Xi et al. — [EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection](http://arxiv.org/abs/2608.17933v1)
  <details><summary>📄 Abstract</summary>
  Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection, feature design, and hyperparameter tuning, limiting their scalability and adaptability. We propose EvoTS-Agent, a validation-guided self-evolving LLM agent for autonomous financial time-ser...
  </details>

- **2026-08-18** — Zachary Kenton, Lili Janzer, Rory Greig et al. — [Debate Training Reduces Reward Hacking in RLAIF](http://arxiv.org/abs/2608.17776v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training progresses, the policy learns to exploit systematic errors in its AI judge, degrading task performance, a problem that worsens precisely when the judge is weaker than the policy, the setting mo...
  </details>

- **2026-08-18** — Yizhu Zhao, Li Yu, Jianhua Zhang et al. — [Electromagnetic World Model for 6G: A Unified Framework for Joint Environment Reconstruction and Channel Prediction](http://arxiv.org/abs/2608.17769v1)
  <details><summary>📄 Abstract</summary>
  The integration of sensing, communication, and intelligence is becoming a key enabler for sixth generation (6G) wireless systems, where intelligent terminals are expected to simultaneously support efficient link establishment and reliable environmental sensing. However, existing studies mainly exploit sensing information or communication information to address a single task, such as channel prediction or environment reconstruction. Motivated by the shared dependence of optical and radio-frequenc...
  </details>

- **2026-08-18** — Janine Schneider, Jan Kallenborn, Tim Hoffmann et al. — [Achievement Unlocked: Let's Get Hacked! An Empirical Study of Cybercrime in the Video Gaming Ecosystem](http://arxiv.org/abs/2608.17754v1)
  <details><summary>📄 Abstract</summary>
  The ubiquity of the video game industry and its large user base have transformed video games into complex social and economic ecosystems. Unfortunately, this growing popularity also attracts cybercriminals who deliberately exploit game-specific mechanisms to target players. Despite this growing threat, cybercrime in the gaming ecosystem has received little systematic attention in prior research.   In this work, we present an empirical study of cybercrime affecting video game players, combining q...
  </details>

- **2026-08-18** — Raghutheja Bollampally, Soumya Sankar, Yuqi Qin et al. — [Active learning molecular beam epitaxy of complex quantum materials](http://arxiv.org/abs/2608.17742v1)
  <details><summary>📄 Abstract</summary>
  The integration of machine learning (ML) into materials science offers a transformative pathway toward fully autonomous synthesis workflows. For precise thin-film deposition techniques like molecular beam epitaxy (MBE), this automation is critical to overcome the time-consuming, manual navigation of high-dimensional thermodynamic phase spaces. Existing approaches for ML-assisted thin film growth predominantly rely on continuous Bayesian optimization (BO) models that assume smooth parameter lands...
  </details>

- **2026-08-18** — Zachary R. Madin, Connor York, Jonathan Lawry et al. — [Collective Ranking of Environmental Signals through Gaussian Belief Propagation in a Patrolling Robot Swarm](http://arxiv.org/abs/2608.17690v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot patrolling requires a team to visit all areas of an environment at regular intervals, typically minimising idleness. A practical extension, motivated by security and environmental monitoring, is to additionally form a collective ranking of all patrol locations by some measured signal, a generalisation of the best-of-n problem to the many-option, continuous-valued regime. We observe that the patrol graph admits a natural dual interpretation: it is simultaneously the topology that dict...
  </details>

- **2026-08-18** — Joao Fonseca, Rodrigo Rodrigues, Paolo Romano — [Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals](http://arxiv.org/abs/2608.17687v1)
  <details><summary>📄 Abstract</summary>
  Despite their widespread use, Large Language Models (LLMs) remain limited by a fundamental problem: the generation of plausible but false content, known as hallucinations. Most existing detection methods operate at the answer or sentence level, yet per-token detection is essential for localizing hallucinated spans and enabling fine-grained interventions. In this paper, we explore the use of the Mixture-of-Experts (MoE) paradigm to address this gap. In MoE architectures, a single forward pass act...
  </details>

- **2026-08-18** — Chin-Hung Chen, Wim van Houtum, Yan Wu et al. — [Statistical Characterization and Block-EM Estimation of Frequency-Domain NSI for OFDM Systems in Bursty Impulsive Noise](http://arxiv.org/abs/2608.17683v1)
  <details><summary>📄 Abstract</summary>
  Impulsive noise (IN), characterized by its high power and non-Gaussian distribution, poses a critical challenge in modern orthogonal frequency-division multiplexing (OFDM) systems, driven by the proliferation of electronic devices. Current IN mitigation techniques rely heavily on time-domain processing. These methods apply before the discrete Fourier transform (DFT), introducing additional complexity, failing to align with OFDM's inherent frequency-domain processing flow, and risking the destruc...
  </details>

- **2026-08-18** — Luke C. Ugwuoke, Farooq Kyeyune, Tjaart P. J. Krüger — [Body-of-Revolution Finite-Element Model of Plasmon-Enhanced Fluorescence](http://arxiv.org/abs/2608.17655v1)
  <details><summary>📄 Abstract</summary>
  Plasmon-enhanced fluorescence (PEF) is one of the most widely investigated optical phenomena in hybrid systems of emitters and plasmonic nanoantennas, with applications ranging from biosensing to single-molecule emission microscopy. In this work, we extend finite-element modelling of PEF beyond spherically symmetric geometries using a body-of-revolution finite-element method (BOR-FEM). By exploiting exact or equivalent rotational symmetry, 3D emitter-nanoantenna systems are reduced to computatio...
  </details>

- **2026-08-18** — Prashant Rawat, Ravi Kumar Bairagi,  Arunima et al. — [An Emulation Anchored Digital Twin Testbed for Cyberattack and Defense Analysis in Hospital IT OT Environments](http://arxiv.org/abs/2608.17650v1)
  <details><summary>📄 Abstract</summary>
  Modern hospitals increasingly rely on integrated Information Technology (IT) and Operational Technology (OT) infrastructures to support critical healthcare services. However, this convergence expands the cybersecurity attack surface and makes safe validation of defensive mechanisms difficult on live systems. Existing testbeds often focus on isolated IT or OT environments and do not capture realistic cross-domain healthcare interactions. This work presents a hospital IT and OT cybersecurity testb...
  </details>

- **2026-08-18** — Bowen Liu, Qixiang Zhang, Xiaomeng Li — [PathoArgus: Advancing Evidence-Grounded Long-Context Visual Reasoning across Gigapixel Whole-Slide and Multi-Slide Case Contexts](http://arxiv.org/abs/2608.17607v1)
  <details><summary>📄 Abstract</summary>
  Whole-slide pathology reasoning requires models to integrate gigapixel-scale visual evidence across complete case-linked slides, yet current question-answering benchmarks primarily measure final answer accuracy--a metric vulnerable to linguistic priors and benchmark regularities, and insufficient to establish that predictions are grounded in the supplied tissue. We introduce PathoArgus-Bench, a benchmark and evaluation protocol that explicitly tests the full evidence chain: availability, accessi...
  </details>

- **2026-08-18** — Yajing Bai, Jinhao Duan, Jie Peng et al. — [HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety](http://arxiv.org/abs/2608.17597v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety failures emerge across different harness responsibilities. We present HarnessRisk, a lifecycle oriented benchmark that organizes agent harness safety into six operational phases including...
  </details>

- **2026-08-18** — Enrique Barba Roque, Luís Cruz, Annibale Panichella — [Beyond FLOPs: Energy-Aware Knowledge Distillation for Sustainable LLMs on Code-Related Task](http://arxiv.org/abs/2608.17515v1)
  <details><summary>📄 Abstract</summary>
  Background: Large Language Models (LLMs) are increasingly being applied to Software Engineering (SE) tasks, achieving high accuracy across problems such as clone detection, vulnerability prediction, and code summarization. However, their high computational demands and energy consumption raise sustainability concerns and hinder their use on consumer hardware and resource-constrained platforms. A common way to report the computational cost of an LLM in the literature and industry is to use the num...
  </details>

- **2026-08-18** — Kanglei Zhou, Ruizhi Cai, Hubert P. H. Shum et al. — [NeuroPath: Brain-Inspired Dual-Pathway Graph Convolutional Networks for Skeleton-Based Action Recognition](http://arxiv.org/abs/2608.17487v1)
  <details><summary>📄 Abstract</summary>
  Skeleton-based action recognition aims to recognize human actions from sequences of human joint coordinates. Most existing Spatial-Temporal Graph Convolutional Networks (STGCNs) have achieved promising results by modeling skeletal structures with implicit spatial-temporal representations. However, our empirical study reveals a clear performance imbalance across different skeletal modalities, indicating that implicitly coupling spatial and temporal information limits the full exploitation of comp...
  </details>

- **2026-08-18** — Songwei Wu, Rui Zhao, Fan Yang et al. — [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](http://arxiv.org/abs/2608.17453v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that r...
  </details>

- **2026-08-18** — Genghan Zhang, Yixin Dong, Chengze Fan et al. — [PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX](http://arxiv.org/abs/2608.17379v1)
  <details><summary>📄 Abstract</summary>
  We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs. Our evaluation shows that architecture-specific PTX capability remains uneven: success rates fall substantially on complex attention backward workloads,...
  </details>

- **2026-08-18** — Jie Deng, Zhigang Li, J. H. Zheng et al. — [Integrated Heat and Power System Scheduling with Continuous-Time Thermal Dynamics via Bernstein-Galerkin Optimization](http://arxiv.org/abs/2608.17287v1)
  <details><summary>📄 Abstract</summary>
  Coordinated scheduling of district heating networks (DHNs) and electric power systems can improve operational flexibility and reduce costs by exploiting thermal inertia. Most existing formulations rely on simplified discrete-time DHN models, which may inadequately represent continuous spatiotemporal thermal dynamics and can lead to biased flexibility estimation and suboptimal schedules. In this paper, an integrated heat and power system scheduling framework that explicitly incorporates the conti...
  </details>

- **2026-08-18** — Berkcan Kapusuzoglu, Shunsaku Matsumoto, Yoshitomo Miyagi et al. — [Adaptive surrogate modeling for high-dimensional spatio-temporal output](http://arxiv.org/abs/2608.17250v1)
  <details><summary>📄 Abstract</summary>
  This paper develops an adaptive surrogate modeling method for problems with very high-dimensional spatio-temporal outputs. The analysis of spatio-temporal multi-physics systems is computationally expensive and consists of a large number of inputs and outputs. Surrogate models are often constructed to replace the physics-based model to achieve computational efficiency in analyses such as uncertainty quantification and optimization that require many function calls. In order to address the challeng...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

- **2026-08-21** — Sunder Ali Khowaja, Kapal Dev, George C. Alexandropoulos — [$Z^2$-ACT: End-to-End Verifiable Agentic Intent Control for Open 6G RAN](http://arxiv.org/abs/2608.21049v1)
  <details><summary>📄 Abstract</summary>
  With the progression in open and disaggregated 6G radio access networks, it is expected that the system will be able to host multi-vendors. In order to host multi-vendors, it is essential that AI-assisted control loops remain safe, verifiable, and auditable under concurrent operator intents and untrusted model inputs. The existing studies address the agentic coordination, formal intent constraints, zero-trust prompt verification and cryptographic accountability in isolation, which leaves pre-rea...
  </details>

- **2026-08-21** — Qisheng Lu, Aoyang Fang, Junjielong Xu et al. — [Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis](http://arxiv.org/abs/2608.21310v1)
  <details><summary>📄 Abstract</summary>
  Existing evaluations of automated root cause analysis (RCA) for microservices assess diagnostic performance mainly by endpoint correctness: whether a method localizes the responsible service. This criterion enables comparison but does not reveal the evidentiary basis of a diagnosis or the fault-propagation route connecting the source to observed symptoms, both of which an on-call site reliability engineer needs to judge whether action is warranted. We therefore treat RCA as an observable diagnos...
  </details>

- **2026-08-21** — Matthew Faucher — [TRACE-C: Rank-Calibrated Relational Anomaly Detection for Multi-Stream Operational Telemetry](http://arxiv.org/abs/2608.21251v1)
  <details><summary>📄 Abstract</summary>
  Operational telemetry can be jointly anomalous while every individual stream stays inside its familiar range. TRACE-C is an auditable strictly-prior rank-calibrated detector for aligned multi-stream telemetry: same-regime rolling median/MAD residuals feed three window channels -- a maximum normalized local sum, a Gaussian copula-form dependence contrast on robust-z residuals, and a worst standardized AR(1) innovation -- whose channel ranks are Fisher-aggregated and ranked against earlier aggrega...
  </details>

- **2026-08-21** — Tonglin Yan, Gregoire Sergeant-Perthuis, David Rudrauf — [Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models](http://arxiv.org/abs/2608.20975v1)
  <details><summary>📄 Abstract</summary>
  Effective social interaction requires agents to translate mental state inferences into coordinated behavioral signals across verbal and nonverbal channels simultaneously. Yet existing benchmarks evaluate theory of mind (ToM) reasoning and embodied behavior in isolation, leaving unmeasured the gap between social inference and social action. We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact ac...
  </details>

- **2026-08-21** — Haozhen Yan, Siyuan Shan, Zijian Yu et al. — [GAP-SAM: A Global Artifact Prior for Generalizable AI-Generated Image Manipulation Localization](http://arxiv.org/abs/2608.20929v1)
  <details><summary>📄 Abstract</summary>
  AI-generated image manipulation localization identifies edited pixels, but its OOD performance lags behind image-level detection partly because pixel supervision entangles forensic evidence with dataset-specific mask geometry and semantic boundaries. Extending image-level distribution alignment to localization, we construct COCO-ControlNet with source-image Canny edges and depth maps to align semantics and geometry, improving OOD performance across multiple localizers. Yet tighter Mask-VAE Recon...
  </details>

- **2026-08-21** — Qifeng Zhang, Ting Xiang, Zeyuan Bai et al. — [Semantically Compatible Knowledge Distillation for Cross-Domain Object Detection with Vision Foundation Models](http://arxiv.org/abs/2608.20916v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models (VFMs) offer strong generalization capabilities for domain-adaptive object detection (DAOD). However, existing VFM-based methods overlook the spatial-scale discrepancy between teacher and student feature maps, resulting in semantic incompatibility that weakens both feature alignment and pseudo-label learning. Moreover, domain shift can cause source-trained VFM teachers to miss target-domain objects, limiting the quality of their pseudo-labels. To address these issues, we...
  </details>

- **2026-08-21** — Luiz Giacomossi, Zafer Yigit, Marwan Shakarna et al. — [A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions](http://arxiv.org/abs/2608.20906v1)
  <details><summary>📄 Abstract</summary>
  The certification of Unmanned Aerial Vehicle (UAV) swarms for safety-critical operations requires verifiable design assurance. Airworthiness standards demand deterministic reliability, whereas multi-agent coordination algorithms execute non-deterministic models. This paper proposes a mixed-criticality architectural framework that applies SAE ARP4754B methods to swarm reconfiguration. First, a hardware-isolated Safety Monitor functions as a Run-Time Assurance (RTA) gateway, decoupling the flight-...
  </details>

- **2026-08-21** — Meda Lazar, Sourab Sridhar, Shashwata Gupta et al. — [Multi-Modal Traffic Sign Detection with Semantic Attributes for Autonomous Driving](http://arxiv.org/abs/2608.20874v1)
  <details><summary>📄 Abstract</summary>
  Reliable traffic sign detection is a prerequisite for the global deployment of autonomous driving systems, where regulatory compliance and road safety depend on perceiving signs correctly across regions, ranges, and weather conditions. Despite recent progress, vision-based methods continue to face three fundamental limitations: poor cross-regional generalization due to high diversity across countries, degraded performance on small-object detection at long ranges (traffic signs occupy as little a...
  </details>

- **2026-08-21** — Giovanna Broccia, Julian Frattini, Chetan Arora et al. — [Human-AI Collaboration in Requirements Engineering: Evidence of the Negative Effect of LLMs on Requirements Inspection](http://arxiv.org/abs/2608.21298v1)
  <details><summary>📄 Abstract</summary>
  Background. Requirements inspection (RI) is a well-established practice for detecting potential defects in requirements artifacts early in the software lifecycle. Recent advances in large language models (LLMs) have stimulated interest in their potential to support requirements engineering (RE) tasks. However, empirical evidence on the effects of LLMs when used as collaborative assistants in human-performed RI remains scarce. Aims. We aim to investigate the impact of LLM support on human-perform...
  </details>

- **2026-08-21** — Percy Brown, Kweku Yamoah — [Invisible Agents, Uninformed Patients: Towards Responsible Deployment Of Autonomous AI Diagnostic Agents In Sub-Saharan Africa](http://arxiv.org/abs/2608.21326v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI diagnostic agents, systems that analyse patient-specific clinical data and produce diagnostic outputs or triage decisions without mandatory real-time human review, are increasingly deployed across eHealth platforms in sub-Saharan Africa at a pace that has outrun the governance infrastructure needed to oversee them. While significant bodies of work address AI accountability, transparency and explainability in healthcare, existing frameworks are largely clinician-centered and assume ...
  </details>

- **2026-08-21** — Inpyo Song, Jangwon Lee — [A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video Anomaly Detection](http://arxiv.org/abs/2608.21244v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models enable training-free video anomaly detection by answering questions about video segments. VAD benchmarks, however, require a scalar anomaly score for each segment and evaluate the resulting ranking using the AUROC or AP. A VLM-based detector should therefore define an answer interface: the answer scale specifies the admissible answers, and the readout rule maps the model's output distribution to a score. Because this interface can change the evaluated ranking, it is part o...
  </details>

- **2026-08-20** — Shangbo Yuan, Jie Xu, Xiaofeng Zhu et al. — [Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training](http://arxiv.org/abs/2608.19973v1)
  <details><summary>📄 Abstract</summary>
  Recently, open-vocabulary 3D object detection (3D-OVD) has gained increasing attention for its ability to detect unseen objects in 3D scenes. Existing approaches typically adopt a two-stage pipeline that first discovers novel objects using foundation models and then trains a 3D-OVD model based on these discovered objects. Although effective, this pipeline often suffers from inaccurate localization and mismatched classification during the discovery stage, which subsequently limits the performance...
  </details>

- **2026-08-20** — Denesa Zyberaj, Roman Vintonyak, Pascal Hirmer et al. — [A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications](http://arxiv.org/abs/2608.19752v1)
  <details><summary>📄 Abstract</summary>
  Testing embedded software in modern vehicles is challenging due to system complexity, decentralized architectures, and strict safety and performance constraints. In this work, we present an end-to-end, deployment-aware testing pipeline for IoT-based automotive applications. The pipeline combines requirement-driven test and code generation with large language model (LLM) and vision-language model (VLM) assistance, and human-in-the-loop curation to reduce manual effort and improve consistency. Usi...
  </details>

- **2026-08-20** — Zhuochun Li, Youngmin Ko, Ali Keramati et al. — [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows](http://arxiv.org/abs/2608.19741v1)
  <details><summary>📄 Abstract</summary>
  Recent agent benchmarks increasingly ground evaluation in executable environments, from code repair to web navigation, app APIs, and function calling. Yet completing consequential work beyond code requires more than producing a plausible response or valid tool call: agents must gather missing information over multiple turns, follow domain policies, coordinate dependent tools, and realize the correct persistent state transition without collateral effects. In this paper, we introduce Thinkingbox, ...
  </details>

- **2026-08-20** — Mohammad Arif Ul Alam — [Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions](http://arxiv.org/abs/2608.19710v1)
  <details><summary>📄 Abstract</summary>
  Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur. Although sonar provides complementary information that is less affected by optical visibility, prior visual-sonar research has largely focused on feature alignment and nominal detection performance. We investigate cross-modal robustness as visual reliability deteriorates and assess whether pretrained visual foundation...
  </details>

- **2026-08-20** — Alexei Kaltchenko, Gurnivaj Tiwana — [ChatGPT Solves All Tested Qiskit Homework Assignments](http://arxiv.org/abs/2608.19707v1)
  <details><summary>📄 Abstract</summary>
  Generative AI creates an assessment challenge in quantum software education: a student can provide a homework notebook to ChatGPT and request a completed submission. This study examined whether introductory Qiskit homework could remain autogradable while requiring students to run, review, and discuss results rather than banning AI. Three packages were tested: seeded basis-state circuits with bit flips and customized measurement mappings; Quantum Fourier Transform followed by inverse-transform re...
  </details>

- **2026-08-20** — Yujun Chen, Tianle Li, Jiayu Chen et al. — [An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design](http://arxiv.org/abs/2608.19699v1)
  <details><summary>📄 Abstract</summary>
  In this paper, a bio-robot is an engineered living or biohybrid system in which living cells perform one or more core functions, such as sensing, information processing, actuation or output. We focus on systems whose cell-based functions are programmed by genetic circuits; physical movement is optional. Designing such a system requires translating application requirements into sensing, logic or memory, output, assembly, host and containment modules, while grounding each choice in traceable parts...
  </details>

- **2026-08-20** — Xizhou Bu, Qingda Hu, Lei Zhou et al. — [What Matters for Latent Actions in Robot Learning](http://arxiv.org/abs/2608.19613v1)
  <details><summary>📄 Abstract</summary>
  Latent Action Models (LAMs) have emerged as a promising paradigm for enabling robot learning to leverage large-scale unlabeled videos through latent actions that serve as compact surrogates for physical actions. Despite rapid progress, research on LAM remains highly fragmented, with existing methods evaluating different design choices in isolation under inconsistent experimental settings, making it difficult to identify the factors that truly determine downstream robotic manipulation performance...
  </details>

- **2026-08-20** — Xinyi Liu, Hooshang Nayyeri, Dilek Hakkani-Tur et al. — [Hear2Act: Benchmarking When Prosody Should Change What an Assistant Does](http://arxiv.org/abs/2608.19515v1)
  <details><summary>📄 Abstract</summary>
  Prosodic cues can convey task-relevant information that alters the trajectory and outcome of a task-oriented dialogue, even when the words themselves remain unchanged. Yet existing benchmarks typically evaluate prosodic perception, response appropriateness, and task-oriented dialogue in isolation, making it difficult to test whether prosodic evidence changes downstream decisions. We introduce Hear2Act, a unified evaluation protocol for text and spoken assistants with 480 persona-grounded scenari...
  </details>

- **2026-08-20** — Parampreet Singh, Anushka Singh, Sumit Kumar et al. — [$TCP_α$: Margin-Controlled Confidence estimation for reliable Music Information Retrieval](http://arxiv.org/abs/2608.20326v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are often overconfident, assigning high confidence even to incorrect predictions. Consequently, users lack a reliable signal for deciding when a prediction can be trusted. Post-hoc confidence estimation addresses this by training a lightweight auxiliary head over a frozen classifier. Existing targets, however, suffer from inherent ambiguity: they assign overlapping confidence values to correct and incorrect predictions, while errors near the decision boundary receive confide...
  </details>

- **2026-08-20** — Alexander Nemecek, Osama Zafar, Debargha Ganguly et al. — [Auditing Cross-Lingual Fairness in Language Model Watermarking](http://arxiv.org/abs/2608.20047v1)
  <details><summary>📄 Abstract</summary>
  Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that dis...
  </details>

- **2026-08-20** — Christopher Henshaw, Gour Karmakar — [From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs](http://arxiv.org/abs/2608.19938v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to anomalous behaviour log detection, such as Wazuh rely primarily on predefined detection rules, while statistical anomaly detection approaches such as OpenSearch identify deviations from previously observed behavioural patterns. Recent research has investigated LLMs for log anomaly detection because of their ability to interpret semantic and contextual information. However, LLM-based approaches can be affected by prompt construction, noisy log data, and reliance on generic ...
  </details>

- **2026-08-20** — Georg Kordowich, Jonathan Loebel, Julian Oelhaf et al. — [A simulation based dataset of faults and events for machine learning in power systems](http://arxiv.org/abs/2608.19777v1)
  <details><summary>📄 Abstract</summary>
  The integration of inverter-based renewable energy sources into electric grids challenges conventional power system protection. Machine learning-based solutions can address these challenges by utilizing available data in modern smart grids. However, the lack of open datasets prevents reproducibility and fair comparisons between different approaches and their results, which hinders further progress. Therefore, this paper presents EvEMTBench, a synthetic dataset of faults and events generated usin...
  </details>

- **2026-08-20** — Yunhao Liang, Chengguang Gan, Ruixuan Ying et al. — [Auditing and Decomposing Feedback-Driven Evolution in LLM Test Generation under the Oracle Problem](http://arxiv.org/abs/2608.19626v1)
  <details><summary>📄 Abstract</summary>
  Execution feedback is often treated as a self-verifying signal for improving LLM-generated tests. However, when generated inputs are executed on a single accepted program and its outputs are used as ground truth, invalid or underspecified inputs can create spurious fault detections and apparent evolutionary gains. We audit this failure mode in feedback-driven test generation using 142 development tasks, 114 locked external tasks, and 138 held-out tasks, with two code models, three seeds, and fau...
  </details>

- **2026-08-19** — Fariz Ikhwantri, Iker Lasa Ojanguren, Dusica Marijan et al. — [An Agentic RAG and Evaluation Framework for Assurance Case Generation: Industrial Use Case for the EU Cyber Resilience Act Compliance](http://arxiv.org/abs/2608.19509v1)
  <details><summary>📄 Abstract</summary>
  Complying with the EU Cyber Resilience Act (CRA) is a resource-intensive challenge for SMEs due to the complexity of cybersecurity conformity assessment. Yet, it is essential for demonstrating regulatory compliance and ensuring product security and resilience. To address this, we introduce an automated framework for generating Assurance Cases (ACs) using an agentic Retrieval-Augmented Generation grounded in a formal Claim-Argument-Evidence logic. By systematically mapping technical documentation...
  </details>

- **2026-08-19** — Sparsh Garg, Yi-Wen Chen, Vijay Kumar B G et al. — [CAViAR: A Causal Video Dataset for Fine-Grained Accident Reasoning in Real-World Scenarios](http://arxiv.org/abs/2608.19380v1)
  <details><summary>📄 Abstract</summary>
  While modern autonomous driving systems excel at perception tasks such as object detection and trajectory prediction, they lack the high-level causal reasoning required to interpret traffic accidents. In particular, determining responsibility, such as identifying who is at fault and which traffic rule was violated, remains largely unexplored in current benchmarks. To this end, we introduce CAViAR (Causal Accident Video and Incident Analysis Repository), a human-annotated dashcam benchmark compri...
  </details>

- **2026-08-19** — Tu Anh Hoang Nguyen, Dang Nguyen, Thuc Duy Le et al. — [LLM as Detector: An In-context Learning Approach for Tabular Anomaly Detection](http://arxiv.org/abs/2608.19463v1)
  <details><summary>📄 Abstract</summary>
  Anomaly detection in tabular data is challenging because abnormal samples often arise as violations of cross-feature dependencies rather than simple marginal deviations. Existing detectors rely on geometric or reconstruction signals, while prior LLM-based approaches mainly fine-tune LLMs with normal samples or generate synthetic anomalies. We propose LLM-Detector, a framework that utilizes the in-context learning capacity of LLMs for structured, prompt-conditioned scoring synthesis, enabling LLM...
  </details>

- **2026-08-19** — Sepehr Ghaffarzadegan, Boubakr Nour, Makan Pourzandi et al. — [From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation](http://arxiv.org/abs/2608.19011v1)
  <details><summary>📄 Abstract</summary>
  Mechanisms for dynamically converting cyber threat intelligence (CTI) into actionable detection capabilities are necessary due to the rapid evolution of Advanced Persistent Threats (APTs). Sigma rules are an essential part of contemporary threat detection workflows because they offer a platform-independent framework for expressing detection logic that can be converted into particular queries across SIEM systems. Conventional techniques for manually crafting Sigma rules are prone to mistakes, and...
  </details>

- **2026-08-19** — Samuel Howard, Kshitiz Aryal, Mahmoud Abdelsalam et al. — [Malformer: A Multi-Modal Malware Detector Using Transformers](http://arxiv.org/abs/2608.19052v1)
  <details><summary>📄 Abstract</summary>
  Traditional malware detection systems that rely on a single representation of malware often fail to identify novel threats. These representations of malware binaries, also known as modalities, do not provide the models with sufficient information to discriminate among all samples. Additionally, individual representations introduce new failure modes, with some modality extraction being dependent upon the success of disassembling. Past works have integrated either additional modalities or more dis...
  </details>

- **2026-08-19** — Li-Heng Chen, Haokai Pang, Chengye Su et al. — [USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes](http://arxiv.org/abs/2608.19036v1)
  <details><summary>📄 Abstract</summary>
  Spatial representation learning for autonomous driving aims to map raw visual signals into structured 3D scene representations, where object-centric bounding boxes and rendering-oriented 3D primitives (\eg, 3D Gaussians) serve as two distinct yet highly complementary levels for scene understanding. Existing methods typically treat dynamic reconstruction and instance-level perception as separate tasks, despite their shared goal of estimating the underlying 3D world state. As a result, dynamic rec...
  </details>

- **2026-08-19** — Xing Zhang, Yanwei Cui, Guanghui Wang et al. — [Metrics That Write Themselves: Evolving an Evaluator from Its Own Blind Spots](http://arxiv.org/abs/2608.18744v1)
  <details><summary>📄 Abstract</summary>
  Agents improve quickly against a reliable automatic metric and stall without one, and the applications that need them most, report generation among them, are the ones nobody knows how to score. Can the metric write itself? Saying what makes an answer good is hard; pointing at something wrong with one is easier, so the metric we evolve is a pool of small Python operators that each flag a candidate for one named defect, or abstain, and vote. Asking a model for operators directly does not work: 183...
  </details>

- **2026-08-19** — Manoj N M, Vijayakrishna S, Manjunath Srinivas et al. — [A Multi-Agent Platform for Automated Enterprise Analytics and Insight Generation](http://arxiv.org/abs/2608.18740v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a multi-agent framework built on CrewAI [1] for conversational business intelligence. Five specialized AI agents operate in a sequential pipeline to process natural language queries, retrieve and analyze data, generate visualizations via the Model Context Protocol (MCP) [2], and deliver actionable insights. The platform features a defense-in-depth security architecture for multi-tenant data isolation and a query parameterization mechanism for transforming conversational insig...
  </details>

- **2026-08-19** — Qing Huang, Jianing Zhang, Pooja Pol — [Computational Measurement of Team-Process Phase Dynamics in Collaborative Virtual Reality](http://arxiv.org/abs/2608.18660v1)
  <details><summary>📄 Abstract</summary>
  Collaborative virtual reality (VR) environments make team communication observable as it unfolds, but conventional transcript analyses often summarize entire trials or divide them into fixed temporal windows. Such approaches can obscure changes in team communication and coordination over time. This article presents a computational framework for detecting and interpreting dynamic team-process phases from timestamped dialogue in a collaborative VR game. The framework uses late chunking to generate...
  </details>

- **2026-08-19** — Yang Yan, Zifan Zhou, Xuan Wang et al. — [A Locally Deployable Tool-Grounded LLM Multi-agent Framework for Automating Methane Emission Analysis and Reporting](http://arxiv.org/abs/2608.18473v1)
  <details><summary>📄 Abstract</summary>
  Methane field monitoring requires the integration of sampling design, meteorological interpretation, sensor processing, plume analysis, visualization, and reporting, but these steps are often distributed across separate expert-driven workflows. We developed a locally deployable, tool-grounded large language model (LLM) multi-agent framework for our low-cost methane sensing and field-monitoring campaigns. The framework uses LLM agents as workflow coordinators that link field measurements, meteoro...
  </details>

- **2026-08-19** — George Andrikopoulos — [Tuning the Stochastic Machine: A Systems Engineer's Operating Model for Human-AI Engineering](http://arxiv.org/abs/2608.19125v1)
  <details><summary>📄 Abstract</summary>
  When an expert corrects an LLM assistant's error, the correction usually dies with the session, and the error class returns. I argue this is an operations problem, not a tooling problem: mechanisms for persisting corrections exist and are shipping, but the discipline for governing them -- versioning with provenance, recurrence monitoring, counter-metrics, retirement of stale rules -- does not. Writing as a systems engineer of thirty years, I map the LLM stack onto the machines my profession alre...
  </details>

- **2026-08-19** — Ayoub El Bouchtili, Guilhaume Leroy-Meline — [FRAGMENT: Factorized Graph Representations for Document Generation and Editing via Entity-Aware Transformations](http://arxiv.org/abs/2608.18679v1)
  <details><summary>📄 Abstract</summary>
  Structured documents such as invoices, forms, reports, and scientific articles derive meaning from the interplay between spatial layout, textual content, and logical structure. Generative models operating at the pixel or token level often struggle to capture these dependencies effectively. We explore FRAGMENT, a generative framework that represents a document as a typed relational graph and factorizes its distribution as p(structure, content) = p(structure) * p(content | structure). The framewor...
  </details>

- **2026-08-19** — Yaqi Li, Jielun Peng, Yabin Wang et al. — [PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs](http://arxiv.org/abs/2608.18573v1)
  <details><summary>📄 Abstract</summary>
  Existing explainable deepfake forensic methods typically rely on task-adapted MLLM to jointly address detection, localization, and explanation. Inspired by agent-style tool use, we instead introduce a Perception-as-Tool paradigm and instantiate it as PATE-Forensics, which architecturally decouples detection and localization from explanation generation while coupling detection and localization as tightly as possible within a forensic perception tool. The DINOv3-based tool couples a multi-granular...
  </details>

- **2026-08-18** — Bin Li, Dongdong Wang, Siyang Lu — [Too Sure to Be Safe: Model Calibration for Reliable Log Anomaly Detection](http://arxiv.org/abs/2608.17965v2)
  <details><summary>📄 Abstract</summary>
  Online log anomaly detection is critical for maintaining the reliability of large-scale computing systems. Although recent language model-based log anomaly detectors achieve strong detection performance, their confidence estimates remain poorly calibrated. We show that these detectors frequently assign excessive confidence to incorrect predictions, particularly for anomalous logs under severe class imbalance. Moreover, confidence on erroneous predictions remains persistently high even when conve...
  </details>

- **2026-08-18** — Tianjing Hao, Haiyu Lan, Angsong Li et al. — [OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects](http://arxiv.org/abs/2608.17633v3)
  <details><summary>📄 Abstract</summary>
  Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail categories and small, fine-grained objects overlooked by closed-set models, they also tend to fragment large surfaces and merge small objects into larger neighboring objects, compromising instance-level consistency and undermining mapping fidelity. Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a quer...
  </details>

- **2026-08-18** — Alexander Tu, Michael Tu — [Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents](http://arxiv.org/abs/2608.18351v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language-model agents can complete a task while exercising authority that the user did not grant or the task does not need, causing excess-authority errors. Traditional permission gating systems alone for validating agent environments are insufficient. We study whether post-training can teach a 4B-parameter model to choose task-conditioned authority in executable terminal and Model Context Protocol (MCP) environments to complement those measures. We propose a framework where eac...
  </details>

- **2026-08-18** — Emma Yanyang Kong, JJ Tan, Ishan Gupta et al. — [The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations](http://arxiv.org/abs/2608.18300v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-Judge, which leverages a large language model to evaluate natural language generated by another AI application or model, has become a standard, scalable approach for accelerating and extending costly human evaluation. However, most work treats a judge as a static artifact, evaluating it once at construction or against a fixed benchmark. In contrast, we argue that an LLM judge running in a production system is better understood as having a lifecycle: it must be built, trained, deployed, ...
  </details>

- **2026-08-18** — Xule Liu, Yijun Liu, Chao Li et al. — [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](http://arxiv.org/abs/2608.17756v2)
  <details><summary>📄 Abstract</summary>
  Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not which stage caused it. Existing evaluations often report aggregate performance without paired statistical comparisons, slice-level non-regression checks, or stage-level diagnostic traces...
  </details>

- **2026-08-18** — Tianjing Hao, Haiyu Lan, Angsong Li et al. — [OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects](http://arxiv.org/abs/2608.17633v2)
  <details><summary>📄 Abstract</summary>
  Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail categories and small, fine-grained objects overlooked by closed-set models, they also tend to fragment large surfaces and merge small objects into larger neighboring objects, compromising instance-level consistency and undermining mapping fidelity. Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a quer...
  </details>

- **2026-08-18** — Rabimba Karanjai, Yang Lu, Nour Diallo et al. — [When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling](http://arxiv.org/abs/2608.17275v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act rather than merely read: across the Model Context Protocol (MCP) ecosystem, the share of deployed tools that modify external state has risen from 27% to 65% of tool use. When agents exercise this authority on public blockchains through MCP, skills, and tool calling, the consequences of an attack are governed by the blockchain execution layer rather than by conventional software assumptions. This survey argues that four properties of that layer (irreversibility, signing...
  </details>

- **2026-08-18** — Yeongwoo Kim, Quanyan Zhu, György Dán — [ADAPTD: Adaptive Detection and Proactive Threat Defense for Autonomous APT attacks](http://arxiv.org/abs/2608.17251v1)
  <details><summary>📄 Abstract</summary>
  Advanced persistent threat (APT) actors increasingly employ sophisticated techniques to propagate laterally through segmented enterprise networks. Timely detection and defense depend on cross-subnetwork coordination, yet maintaining global situational awareness generates substantial communication overhead. To manage this tradeoff, flexible monitoring and adaptable containment are imperative. This paper presents ADAPTD, a communication- and computation-efficient, decision-theoretic framework inte...
  </details>

- **2026-08-18** — Xingjian Wang, Zhao Wang, Taihang Hu et al. — [From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation](http://arxiv.org/abs/2608.18076v1)
  <details><summary>📄 Abstract</summary>
  Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A central challenge is not only how to curate each task-specific corpus, but also how to organize heterogeneous supervision according to the dependencies among generative capabilities. We present a \textbf{capability-driven data infrastructure} that couples capability-specific supervision construction wi...
  </details>

- **2026-08-18** — Hollis Robbins — [Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation](http://arxiv.org/abs/2608.18041v1)
  <details><summary>📄 Abstract</summary>
  Language has two parameters. Count how often words occur together and you estimate amplitude, the strength of association. Word embeddings and attention weights refine that count, which sums every writer in the corpus together. This paper claims a second parameter, phase, which signed weights learned from a corpus do not supply. Phase exists only between meanings: it determines how coactivated meanings combine, and it can reverse what a meaning contributes while that meaning stays fully present....
  </details>

- **2026-08-18** — Lu Xu, Xu Li, Linjiang Zheng et al. — [Can Large Language Models Explain Flight Safety Events? A Prior-Guided Semantic LLM-based Approach](http://arxiv.org/abs/2608.18017v1)
  <details><summary>📄 Abstract</summary>
  Improving flight safety with flight data requires not only accurate detection of risk events, but more importantly, clear interpretation of their underlying causes at the level of pilot control behavior. Existing explainable AI techniques, such as feature importance maps, often require considerable domain knowledge to translate them into operationally meaningful explanations. Large Language Models (LLMs), which excel at language reasoning, bring a promising solution to this issue. However, apply...
  </details>

- **2026-08-18** — Lotta Kiefer, Brisca Balthes, Christoph Leiter et al. — [When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era](http://arxiv.org/abs/2608.17979v1)
  <details><summary>📄 Abstract</summary>
  Authorship verification (AV) assumes that an author's writing style remains sufficiently stable to distinguish it from that of other writers. In practice, however, this assumption is challenged by distribution shifts caused by changes in genre, time, and AI-assisted writing. Existing AV benchmarks typically study these factors in isolation and focus predominantly on English, limiting our understanding of model robustness under realistic conditions. We introduce AVShift, the first German benchmar...
  </details>

- **2026-08-18** — Ziya Zhou, Shangda Wu, Shenyang Xu et al. — [UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-Resource Music Understanding](http://arxiv.org/abs/2608.17852v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large audio-language models (LALMs) have significantly improved performance in tasks such as music captioning, genre classification, and sound event detection. However, limited attention has been paid to improving their adaptability across diverse musical traditions, particularly folk music rooted in distinct cultural contexts. Folk-music traditions are typically resource-scarce, unevenly represented across regions, and poorly documented. Even when such samples appear in large...
  </details>

- **2026-08-18** — Tanel Liiv, Sander Soodla, Nzamba Bignoumba et al. — [Training with synthetic data for drone detection in thermal imagery](http://arxiv.org/abs/2608.17799v1)
  <details><summary>📄 Abstract</summary>
  Ground-to-Air (G2A) drone detection in medium- and long-wave infrared (MWIR/LWIR) imagery is challenging due to reduced texture information, sensor noise, weak thermal contrast, and the scarcity of annotated data. This work investigates a synthetic-first training strategy that combines synthetic scene generation with fine-tuning on real data. We show that synthetic data provides an effective basis for learning initial object representations, while real in-domain thermal imagery is still essentia...
  </details>

- **2026-08-18** — Abdul Mueez, Aaditya Baranwal, Junior Chaj-Mejia et al. — [Vision-Language Models for Analog Gauge Reading: An Empirical Study of Specialization, Transfer and Reliability](http://arxiv.org/abs/2608.17723v1)
  <details><summary>📄 Abstract</summary>
  Analog gauges remain common in industrial environments where manual inspection is costly or hazardous. The engineering application addressed here is direct numerical reading of single-target analog-gauge images, while the artificial-intelligence contribution is a systematic evaluation of specialization, transfer, robustness and reliability for a general-purpose vision-language model (VLM) without an explicit pointer-segmentation and geometric-reading pipeline. The Qwen2.5-VL-7B-Instruct model is...
  </details>

- **2026-08-18** — Bowen Sun, Yixi Cai, Xiaogeng Liu et al. — [KeyPooling: Measuring Where LLM API Relay Paths Collapse Prompt Cache Isolation](http://arxiv.org/abs/2608.17485v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) API relays authenticate customers separately but often forward requests through shared provider credentials. Providers scope prompt caches to upstream principals and namespaces, so relay customers mapped to one cache identity can observe each other's cache state. Prior work showed cache sharing at selected endpoints but did not identify which credential, pool, adapter, or nested hop controls the finalidentity. We present KeyPooling, a measurement method that traces cus...
  </details>

- **2026-08-18** — Yiming Du, Yuxin Jiang, Tao Yuan et al. — [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](http://arxiv.org/abs/2608.17393v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward hacking corrupt outcome signals, while train-inference discrepancies decouple rollout behavior from policy updates. To address this, we present LEGO-RL, a framework that bridges nati...
  </details>

- **2026-08-18** — Qishuang Fu, Andreas Deppeler, Joseph K. Liu et al. — [FlowShield: cryptocurrency anti-money laundering with transaction semantics parsing and fund flow tracking](http://arxiv.org/abs/2608.17355v1)
  <details><summary>📄 Abstract</summary>
  Cryptocurrency anti-money laundering (Crypto AML) is increasingly challenged by sophisticated laundering behaviors that rapidly fragment stolen assets through diverse semantics and across multiple blockchains. Existing Crypto AML methods often simplify transaction semantics, rely on topology-centric signals, or output isolated detection labels. In this paper, we present \textsc{FlowShield}, a Crypto AML framework for transaction-level laundering detection and investigator-facing report generatio...
  </details>

- **2026-08-18** — Junwei Zhou, Zhen Sun, Binyu Li et al. — [ASI-Bench: At the Dawn of Artificial Superintelligence](http://arxiv.org/abs/2608.17271v1)
  <details><summary>📄 Abstract</summary>
  Artificial superintelligence (ASI) requires AI to move beyond mastering existing knowledge toward exploring the unknown, creating new knowledge, and turning new ideas into verifiable results. However, the capabilities of today's AI systems are still largely built on learning, compressing, and applying existing human knowledge. Accordingly, existing benchmarks primarily test whether AI can produce correct answers based on learned knowledge, or whether it can complete tasks under extensive human g...
  </details>

- **2026-08-18** — Yijie Xu, Chao Wang, Hui Xiong — [Against Political Polarization: A Unified Framework for Tracing Evolving Political Ideologies on Social Media](http://arxiv.org/abs/2608.17987v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of social media has greatly influenced political discourse, highlighting the need to understand individual political ideologies and their temporal dynamics. This task faces challenges such as data scarcity, abundant non-political content, costly and bias-prone manual annotation, and difficulty in modeling future ideological inclinations. To address these issues, we propose TSN4PI, a unified framework for tracking the evolution of political ideologies on social media. It includes...
  </details>

- **2026-08-18** — Bin Li, Dongdong Wang, Siyang Lu — [Too Sure to Be Safe: Model Calibration for Reliable Log Anomaly Detection](http://arxiv.org/abs/2608.17965v1)
  <details><summary>📄 Abstract</summary>
  Online log anomaly detection is critical for maintaining the reliability of large-scale computing systems. Although recent language model-based log anomaly detectors achieve strong detection performance, their confidence estimates remain poorly calibrated. We show that these detectors frequently assign excessive confidence to incorrect predictions, particularly for anomalous logs under severe class imbalance. Moreover, confidence on erroneous predictions remains persistently high even when conve...
  </details>

- **2026-08-18** — Md. Faiyaz Abdullah Sayeedi — [Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds](http://arxiv.org/abs/2608.17950v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Traditional attention-based interpretability often fails to capture true semantic proximity due to routing artifacts like attention sinks. In this paper, we bypass attention weights to directly analyze the dynamic geometry of the hidden state manifold, proving that deep LLM latent spaces natively orga...
  </details>

- **2026-08-18** — Xule Liu, Yijun Liu, Chao Li et al. — [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](http://arxiv.org/abs/2608.17756v1)
  <details><summary>📄 Abstract</summary>
  Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not which stage caused it. Existing evaluations often report aggregate performance without paired statistical comparisons, slice-level non-regression checks, or stage-level diagnostic traces...
  </details>

- **2026-08-18** — Shenghao Chen, Hao Jia, Chen Li et al. — [Environment-Invariant Subspace Learning for Generalizable Deepfake Detection](http://arxiv.org/abs/2608.17700v1)
  <details><summary>📄 Abstract</summary>
  Cross-distribution generalization remains a critical bottleneck in deepfake detection. While recent efforts leverage the semantic priors of large-scale visual foundation models (VFMs), a noteworthy yet underexplored challenge remains: the susceptibility of these semantic priors to environmental interference from factors such as lighting and style. Crucially, this interference establishes spurious correlations between forgery cues and environmental patterns that severely limit generalization. To ...
  </details>

- **2026-08-18** — Tianjing Hao, Haiyu Lan, Angsong Li et al. — [OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects](http://arxiv.org/abs/2608.17633v1)
  <details><summary>📄 Abstract</summary>
  Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail categories and small, fine-grained objects overlooked by closed-set models, they also tend to fragment large surfaces and merge small objects into larger neighboring objects, compromising instance-level consistency and undermining mapping fidelity. Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a quer...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 48 papers

- **2026-08-21** — Afonso Baldo, Hugo Pitorro, Areti Vassilopoulos et al. — [Move by Move: Measuring and Steering How LLMs Conduct Psychotherapy](http://arxiv.org/abs/2608.21325v1)
  <details><summary>📄 Abstract</summary>
  Users increasingly turn to large language models for emotional support, yet little is known about how these models actually conduct a psychotherapy interaction. We introduce an ontology of ten therapeutic moves: compact, function-based categories grounded in the MULTI-60 inventory, validated through an annotation campaign with five licensed psychologists, and scaled with a judge-based approach that matches expert agreement. Applying it to real counseling transcripts and model-led sessions, we co...
  </details>

- **2026-08-21** — Marko Haralović, Sounic Akkaraju, Carlo Baretta et al. — [When Adaptation Hurts: Connecting Representational Drift to OOD Failures in MedSAM Fine-Tuning](http://arxiv.org/abs/2608.21300v1)
  <details><summary>📄 Abstract</summary>
  Foundation models for medical image segmentation, like prompt-based MedSAM, generalize well across domains and modalities, often in zero or few-shot setups. However, their performance depends on the quality of prompts and the adaptation of the models to custom datasets. This work systematically examines how MedSAM generalizes across diverse medical imaging benchmarks, with six adaptation strategies: full-model and encoder-only LoRA, shallow and deep visual prompt tuning (VPT), and decoder-only a...
  </details>

- **2026-08-21** — Congsheng Xu, Qiaochu Yang, Fangyuan Shi et al. — [VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation](http://arxiv.org/abs/2608.21290v1)
  <details><summary>📄 Abstract</summary>
  We propose VT-MUSE, a Multimodal Unified SEquential representation learning framework for visuotactilemanipulation. Existing approaches often encode visual and tactile observations independently before fusion, limiting their ability to capture fine-grained cross-modal dependencies. Moreover, most methods focus on observations at the current time step and overlook the temporal evolution of contact. VT-MUSE addresses both limitations through a two-stage representation learning framework. In Stage ...
  </details>

- **2026-08-21** — Peiqi Yu, Nam Ling, Wei Wang et al. — [COEC: Calibrated Orthogonal-Equivalence Compensation for Structured Pruning of Large Language Models](http://arxiv.org/abs/2608.21142v1)
  <details><summary>📄 Abstract</summary>
  Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy. Existing training-free compensation methods use an additive bias or a single orthogonal rotation on the output side of the retained weight. These corrections leave its input singular frame unchanged and therefore limit how the retained weight can adapt after column removal. We propose COEC (Calibrated Orthogonal-Equivalence Compen...
  </details>

- **2026-08-21** — Erik Thureck, Robert Kühnen, Tim Jacobowitz — [PromptResponse: Optimizing Prompts for LLM Coding Tasks](http://arxiv.org/abs/2608.21074v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in research workflows and software development pipelines, yet their output remains sensitive to input prompt variations. This paper presents $\unicode{x00AB}$PromptResponse$\unicode{x00BB}$, a controlled study examining how formatting and LLM-based tuning of coding task prompts affect the resulting code's performance, efficiency, and stability. Using five semantically identical yet syntactically distinct variants of the HumanEval dataset$\unicod...
  </details>

- **2026-08-21** — Amani Sedrat, Takieddine Chehhat, Youcef Sklab et al. — [AT-ViT: Area-Targeted Multi-View Vision Transformer with Cross-Attention and Multi-Scale Patching for Plant Trait Recognition in Herbarium Images](http://arxiv.org/abs/2608.21067v1)
  <details><summary>📄 Abstract</summary>
  Automated plant traits recognition from herbarium images is essential for plant sciences, yet remains challenging because background elements (e.g., textual labels, mounting artifacts, and color charts) can introduce shortcut learning, leading models to rely on spurious non-plant cues rather than plant morphology. This bias degrades both generalization and interpretability. In this paper, we introduce AT-ViT, a dual-branch Vision Transformer that jointly encodes raw herbarium scans and their seg...
  </details>

- **2026-08-21** — Emma Granqvist, Rocío Mercado, Samuel Genheden — [Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment](http://arxiv.org/abs/2608.21057v1)
  <details><summary>📄 Abstract</summary>
  Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. Reference-based metrics such as BLEU and ROUGE fail to capture semantic correctness, while expert human evaluation does not scale to the iteration speed these systems demand. The LLM-as-a-Judge paradigm has emerged as a scalable alternative, but existing drug discovery benchmarks deploy LLM judges ...
  </details>

- **2026-08-21** — Chi Li, Rui Lin, Aobo Ji et al. — [CoAnchor: Robust Collaborative Perception under Spatio-Temporal Misalignment via Object-Level Anchors](http://arxiv.org/abs/2608.21055v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception extends the sensing range of a single vehicle by fusing observations from nearby agents, which improves the robustness of autonomous driving. In realistic deployments, however, the received collaborator messages are often affected by both communication delay and relative-pose noise, which jointly cause stale observations, spatial misalignment, and unstable feature fusion. Existing methods usually address these issues from either the spatial or temporal side, but handling...
  </details>

- **2026-08-21** — Yitao Xu, Tong Wu, Yiyan Wu et al. — [Roadside-Cooperative Autonomous Driving: From Data Platform to Vision-Language End-to-End Reasoning](http://arxiv.org/abs/2608.21032v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-Everything (V2X) cooperation enables beyond-line-of-sight perception, mitigating occlusions in single-vehicle sensing. However, existing V2X benchmarks provide limited support for closed-loop evaluation and language-grounded supervision, hindering the development of vision-language models (VLMs) for end-to-end cooperative driving. To address these limitations, we introduce V2XBench, a simulation platform featuring synchronized ego--roadside sensing and closed-loop evaluation, together...
  </details>

- **2026-08-21** — Haiming Li, Yingsheng Liu, Jingmin Zhu et al. — [Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs](http://arxiv.org/abs/2608.20999v1)
  <details><summary>📄 Abstract</summary>
  Multimodal LLMs apply the language model interface to visual inputs, where ordinal regression tasks such as age estimation, image quality assessment, and disease grading require autoregressive decisions over ordered class labels. We ask whether MLLMs reliably convert internal ordinal evidence into ordered digit-token outputs. Across four ordinal benchmarks and four MLLM backbones, ordinal labels are linearly recoverable from hidden states with Spearman correlation up to 0.938, and a task-designe...
  </details>

- **2026-08-21** — Yibo Hu, Yu Qian, Mao Gu et al. — [TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming](http://arxiv.org/abs/2608.20958v1)
  <details><summary>📄 Abstract</summary>
  E-commerce live streaming requires omni-modal understanding of noisy, temporally extended streams, where product facts are distributed across speech, video frames, product images, overlaid text, and user queries. We present TLive-Omni, an omni-modal understanding model tailored to live-commerce scenarios. It maps image, video, audio, and text inputs into a unified representation space. For long-form live streaming analysis, we introduce Per-vGrid, a timestamped token organization that groups eac...
  </details>

- **2026-08-21** — Pengshuai Yang, Zijing Gao, Xue Yu et al. — [Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation](http://arxiv.org/abs/2608.20797v1)
  <details><summary>📄 Abstract</summary>
  Evaluating language-guided mobile agents has recently shifted from rule-based to model-based approaches to achieve scalable and automated assessments. However, existing holistic evaluation paradigms process entire trajectories at once, leading to substantial context overload. Moreover, they primarily focus on task completion while overlooking operational safety. To address these limitations, we introduce CRATE, a novel two-stage VLM-as-judge framework for automated mobile agent evaluation that i...
  </details>

- **2026-08-20** — Qian Kou, Xiaofeng Shi, Xiaosong Qiu et al. — [Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization](http://arxiv.org/abs/2608.20281v1)
  <details><summary>📄 Abstract</summary>
  Large language models often fail to answer questions about a bounded document collection when the source documents are not retrieved at inference time. We study this setting as document knowledge internalization: converting a fixed corpus into usable parametric knowledge for retrieval-free question answering. We propose IAR (Inject, Align, and Recover), a three-stage post-training framework that separates structured document knowledge injection, QA behavior alignment, and general ability recover...
  </details>

- **2026-08-20** — Yansen Han, Shengyi Liao, Yuanxing Zhang et al. — [Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking](http://arxiv.org/abs/2608.20011v1)
  <details><summary>📄 Abstract</summary>
  Preference optimization is a standard alignment method for generative models, yet extending it to continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify transport trajectories without an inherent constraint to the pretrained data manifold and can move terminal samples off the pretrained support. We formalize this failure mode as manifold drift. Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a preference upd...
  </details>

- **2026-08-20** — Taihua Chen, Xiang Ma, Yixin Zhang et al. — [Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking](http://arxiv.org/abs/2608.20005v1)
  <details><summary>📄 Abstract</summary>
  Pretraining time series foundation models across heterogeneous datasets necessitates effective handling of varying sampling frequencies. Current methods either employ dataset-specific patch sizes and separate FFNs, leading to fragmented representations, or enforce a fixed patch size that neglects inherent temporal variations. To address this, we propose SATS, featuring a scale-aware token alignment mechanism that treats patch size as an explicit notion of scale. By incorporating a contrastive-in...
  </details>

- **2026-08-20** — Hangyu Tian, Zhenqi He, Yanghao Wang et al. — [DIFFCZSL: Compositional Zero-Shot Learning Regularized by Diffusion Representations](http://arxiv.org/abs/2608.19871v1)
  <details><summary>📄 Abstract</summary>
  Compositional Zero-Shot Learning (CZSL) aims to recognize unseen attribute-object compositions by leveraging knowledge of primitive concepts learned from seen compositions. Although recent works achieve impressive performance in CZSL by leveraging large vision-language models, they primarily rely on discriminative representations that may not explicitly preserve the structured relationships between primitive concepts and their compositions. Motivated by the recent success of diffusion-based clas...
  </details>

- **2026-08-20** — Silin Chen, Haoyi Teng, Xiaodong Gu et al. — [Repo0: Design-Driven Zero-to-All Code Generation](http://arxiv.org/abs/2608.19854v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have made substantial progress in code generation, yet most existing systems assume a predefined repository architecture. This assumption does not hold in zero-to-all code generation, where an agent must construct an entire software project directly from natural-language requirements while maintaining a modular repository architecture throughout development. We present Repo0, a continuous structural evolution framework for zero-to-all code generation. Repo0 maintains ...
  </details>

- **2026-08-20** — Yunseo Lee, Hyun Jun Kim, Heeseung Shin et al. — [Towards Clinically Faithful Medical Image Captioning via Enhanced Vision-Language Alignment](http://arxiv.org/abs/2608.19825v1)
  <details><summary>📄 Abstract</summary>
  Medical image captioning is a technique that accelerates early-stage diagnostic workflows and enhances the interpretability of medical diagnostic AI systems. However, unlike general image captioning, clinically reliable captioning remains challenging due to grayscale-based modalities, subtle anatomical cues, specialized medical phrasing, and variations in data quality. Despite recent advances in large vision-language models, fluent outputs do not necessarily guarantee sufficient alignment with c...
  </details>

- **2026-08-20** — Haonan He, Xinyue Fan — [LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment](http://arxiv.org/abs/2608.19800v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) is a prominent fine-tuning method for large models, achieving competitive performance with reduced memory overhead. However, a persistent performance gap remains between LoRA and full fine-tuning. Recent studies have sought to narrow this gap by employing one-step gradient approximations of pretrained weights to align LoRA updates with the principal directions or intrinsic dimensionalities of full fine-tuning updates. Nevertheless, these approaches fail to capture the ...
  </details>

- **2026-08-20** — Yash Ganpat Sawant — [PersonalBench: Measuring the Authorship Gap in LLM Personalization](http://arxiv.org/abs/2608.19746v1)
  <details><summary>📄 Abstract</summary>
  Personalized text generation aims to make LLMs write in a specific individual's style, yet existing benchmarks measure task accuracy or preference alignment rather than whether the model's output actually resembles the target author's writing. We introduce PersonalBench, a benchmark that evaluates inference-time personalization methods through three independent lenses: LUAR (a trained authorship verification model), an LLM-as-judge, and automated stylometrics. Across 50 authors, 1,000 generation...
  </details>

- **2026-08-20** — Hyunse Lee, Jiwoo Jeong, Haneul Lee et al. — [SafeBranch: Branch-Pair Safety Alignment for Embodied Agents](http://arxiv.org/abs/2608.19729v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a trajectory. Standard supervision is insufficient: imitating safe trajectories teaches behavior without explaining why it is safe, and contrasting...
  </details>

- **2026-08-20** — Hexi Wang, Yujia Zhou, Bangde Du et al. — [Mitigating Identity Essentialism in LLM Agents with Longitudinal Life Trajectories](http://arxiv.org/abs/2608.19621v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer a scalable approach to social simulation, but their credibility depends on how agents are constructed. Existing methods can partially reproduce population-level patterns, yet often fail to capture human-like diversity. Our analysis shows that static-profile agents exhibit stronger demographic separation and within-group compression than humans, a pattern consistent with identity essentialism: demographic labels can encourage models to treat group-average tenden...
  </details>

- **2026-08-20** — Jiawei Feng, Jiancan Wu, Xingyu Zhu et al. — [PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment](http://arxiv.org/abs/2608.19598v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has emerged as an effective approach for aligning large language models (LLMs) with human preferences. However, its adaptation to multimodal settings remains unexplored. Through representational analysis, we identify a key limitation in multimodal preference optimization, which we term visual insensitivity: models often fail to distinguish between images and those with critical visual context removed. Our theoretical analysis further uncovers two manifestatio...
  </details>

- **2026-08-20** — Eunsoo Im, Junghun Suh, Gyeonggwan Lee et al. — [CVSD-Reg: Cross-Modal Visual Semantic Prior Distillation for Robust LiDAR Registration](http://arxiv.org/abs/2608.19536v1)
  <details><summary>📄 Abstract</summary>
  Learning-based global point cloud registration has achieved remarkable progress, yet its reliance on geometric representations makes existing methods sensitive to variations in point density, scan pattern, viewpoint, and sensor characteristics. We propose CVSD-Reg, a robust global LiDAR registration framework that distills visual semantic priors from a vision foundation model into LiDAR representations. In Stage 1, a Point Transformer V3 student learns from a frozen DINOv2 teacher through contra...
  </details>

- **2026-08-20** — Josias Moukpe, Priyanka Aryal, Matthew Kenney — [DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories](http://arxiv.org/abs/2608.19653v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents for machine learning experimentation must navigate heterogeneous repositories, repair training pipelines, and evaluate candidate improvements under realistic compute constraints. Existing benchmarks only partially capture these conditions. We introduce DeltaML-Bench, a benchmark comprising 48 tasks sourced from research papers that require agents to improve published baselines within imperfect, open-source repositories. We evaluate GPT-5 and Claude Sonnet 4 with a standard Modu...
  </details>

- **2026-08-19** — Yongliang Zhang, Feng Song, Ji Chen et al. — [SceneGTMM: A Conformal Mapping-based Scene-Aware Transferable GNN-Transformer Dual-Graph Interaction Framework for Map Matching](http://arxiv.org/abs/2608.19298v1)
  <details><summary>📄 Abstract</summary>
  Map matching is a key technology connecting positioning data with high precision road networks, but it faces challenges in noise robustness, cross regional transfer, and interpretability. To addr ess the limitations of existing methods in local global fusion, dynamic road network adaptation, and reliance on black box mod els, this paper proposes SceneGTMM, a transferable GNN Transformer dual graph interaction map matching framework based on a conformal mapping based scene relative strategy. 1) C...
  </details>

- **2026-08-19** — Yihan Xie, Hanwen Cui, Runze Ye et al. — [Holtercare-Bench: A Multimodal Benchmark for Evaluating Long-Term Dynamic ECG Analysis](http://arxiv.org/abs/2608.19297v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) excel in medical applications, most of them favor static images or short-term signals. In the critical field of dynamic electrocardiograms (ECG), models struggle with complex temporal reasoning and diagnostic report generation due to a lack of high-quality datasets and benchmarks. To address this, we introduce (i) Holtercare-23K, a large-scale multimodal dynamic ECG dataset comprising 22,980 QA pairs derived from 788 clinical Holter records and feat...
  </details>

- **2026-08-19** — Bijan Kavousian, Miray Özakkas, Josefine Monnet et al. — [APPROVE: Visual End-User-in-the-Loop Robot Programming with LLMs](http://arxiv.org/abs/2608.19281v1)
  <details><summary>📄 Abstract</summary>
  Programming robots remains challenging for non-experts, as traditional methods require expert knowledge and even block-based interfaces often lack flexibility. Recent work has explored Large Language Models (LLMs) to automatically generate robot programs from natural language, but these systems remain limited by a lack of transparency, missing mechanisms to ensure alignment with user intent, and little support for reuse. We present APPROVE (AI-Powered Programming for Robots with Visual End-User ...
  </details>

- **2026-08-19** — Zachary Speck, Asa Shepard — [Learned, Then Lost: A Measured Single-Example Counterfactual in Pre-training](http://arxiv.org/abs/2608.19168v1)
  <details><summary>📄 Abstract</summary>
  A single training example's contribution to a finished model is normally estimated rather than measured, because measuring it takes two expensive full pre-training runs that differ in one row of one batch. We ran that counterfactual 24 times at a small scale. We trained 32 GPT-2 models at 124M parameters from scratch on OpenWebText, over four conditions and eight seeds. At step 200 of 9,536, at peak learning rate, we replaced one row of a 256-row batch with a fixed context injection carrying a 1...
  </details>

- **2026-08-19** — Zhenyao Cui, Siyuan Kan, Siyang Li et al. — [SCORE: Subject Coordinate Recovery for Label-Free Cross-Subject EEG-to-Image Retrieval](http://arxiv.org/abs/2608.19134v1)
  <details><summary>📄 Abstract</summary>
  Accurate visual decoding can reveal how the brain represents visual information and recover perceived content from neural signals such as electroencephalography (EEG), with potential for neural communication. However, current EEG-to-image retrieval methods perform far below their within-subject counterparts for new users without labeled calibration, limiting real-world deployment. To understand this gap, we analyze EEG features across subjects and find that different subjects preserve similar re...
  </details>

- **2026-08-19** — Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano et al. — [Generalized Audio-Driven Synthesis of Precise Drummer Motion](http://arxiv.org/abs/2608.19055v1)
  <details><summary>📄 Abstract</summary>
  Music-driven character animation enables and enhances transformative applications in entertainment and interactive education. However, synthesizing realistic drumming motion from audio remains challenging due to the inherent tension between high-acceleration dynamics and the need for extreme spatial-temporal precision. Existing approaches, often reliant on motion matching or MIDI input, struggle with generalizing to diverse real-world audio. Moreover, the field lacks standardized evaluation metr...
  </details>

- **2026-08-19** — Hadi Hosseini, Samarth Khanna, Xiyuan Wang — [Preference Reasoning under Indeterminacy in Large Language Models](http://arxiv.org/abs/2608.18631v1)
  <details><summary>📄 Abstract</summary>
  As large language models evolve into decision-making agents, the ability to reason over preferences becomes fundamental to alignment, coordination, and collective intelligence. Yet, unlike standard benchmarks, real-world preference reasoning is inherently indeterminate: information may be incomplete, and valid solutions may not exist. We argue that indeterminacy, rather than correctness alone, is a central challenge for AI reasoning. We formalize this challenge along two axes, (i) epistemic inde...
  </details>

- **2026-08-19** — Mehak Gupta, Tanmoy Chakraborty — [When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models](http://arxiv.org/abs/2608.18628v1)
  <details><summary>📄 Abstract</summary>
  Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally a...
  </details>

- **2026-08-19** — YoungJae Cheong, Jhonghyun An — [FD-CanKD: Frequency-Decoupled Cross-Attention Distillation as a Refinement Prior for Compact Object Detectors](http://arxiv.org/abs/2608.18590v1)
  <details><summary>📄 Abstract</summary>
  Compact object detectors are suitable for resource-constrained visual perception, but their limited representation capacity creates an accuracy gap relative to large models. Conventional detector distillation often relies on prediction-level supervision or a single feature-alignment target, such as response, distribution, correlation, or frequency-domain matching. Frequency-Decoupled Cross-Attention Knowledge Distillation (FD-CanKD) is presented as a detector-oriented framework that transfers te...
  </details>

- **2026-08-19** — Yuan li, Youyuan Lin, Chenhui Chu et al. — [MR-IQA-2: Faithful Image Quality Reflection via Fine-Grained Credit Assignment](http://arxiv.org/abs/2608.18579v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have shown strong potential for image quality assessment (IQA) by improving consistency between quality ratings and their underlying reasoning. However, most approaches supervise reasoning through human-provided ratings and rarely examine whether it faithfully reflects image quality. Rating accuracy alone does not ensure faithful reasoning; a shared reward also obscures supervision sources and may reinforce unfaithful reasoning when a correct rating occur...
  </details>

- **2026-08-18** — Bing Cheng, Yi-Shuai Niu, Howell Tong et al. — [Information Geometry (IG) Lives at Edge or Boundary of SMG (statistically meaningful geometry): - the First Edge Theorem and Applications](http://arxiv.org/abs/2608.19271v1)
  <details><summary>📄 Abstract</summary>
  Statistically Meaningful Geometry (SMG) is a differential-geometric and information-theoretic framework that lifts over-parameterized models into infinite-dimensional non-parametric Orlicz statistical fiber bundles with an Ehresmann connection, decoupling unobservable vertical gauge noise from horizontal statistically verifiable directions. We prove the First Edge Theorem: Amari's information geometry (IG) and conventional statistics (CS) are not autonomous statistical universes but degenerate b...
  </details>

- **2026-08-18** — Qi Yu, Zhichen Zeng, Katherine Tieu et al. — [From Inference to Adaptation: A Unified Optimal Transport View of Vision Language Model](http://arxiv.org/abs/2608.18339v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have demonstrated remarkable zero-shot capabilities yet remain sensitive to real-world distribution shifts during inference. Although significant efforts are devoted to adapting VLMs at test time, they rely heavily on noisy pseudo-labels predicted directly from raw embedding similarities during inference, which are unreliable under distribution shift and mislead the adaptation. To avoid noise amplification, existing works craft coarse-grained surrogate objectives du...
  </details>

- **2026-08-18** — Clara Meister — [TokEval: A Tokenizer Evaluation Suite](http://arxiv.org/abs/2608.18062v1)
  <details><summary>📄 Abstract</summary>
  Language model tokenizers are typically selected with minimal evaluation, despite the fact that their design choices directly impact model capabilities. This can be partly attributed to a limited understanding of which tokenizer properties affect which aspects of downstream performance. We introduce TokEval, a framework of tokenizer evaluation metrics that goes beyond standard measures like fertility and compression rate to capture linguistically and structurally meaningful properties, e.g., UTF...
  </details>

- **2026-08-18** — Sher Badshah, Ali Emami, Hassan Sajjad — [Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees](http://arxiv.org/abs/2608.17994v1)
  <details><summary>📄 Abstract</summary>
  Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the form...
  </details>

- **2026-08-18** — Neelesh Kumar Shukla, Debasmita Panda, Srutanik Bhaduri et al. — [TraceSQL: Traceable Answerability Estimation for Reference-Free Text-to-SQL Verification](http://arxiv.org/abs/2608.17795v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL systems are commonly evaluated using ground-truth SQL queries or reference execution results, but such supervision is unavailable at inference time in real-world deployments. This creates a critical verification problem: given only a user question, database context, and generated SQL, can a system estimate whether the generated query is likely to correctly answer the question? Recent approaches use LLMs as judge or specialized agents to inspect generated SQL, but their decisions can ...
  </details>

- **2026-08-18** — Mehdi Djellabi, Louis-Paul Henry — [On the Expressive Power of the Transverse-Field Ising Model for Graph Learning](http://arxiv.org/abs/2608.17750v1)
  <details><summary>📄 Abstract</summary>
  We study the quantum evolution induced by graph-indexed Ising Hamiltonians as a source of structural signal for graph learning. Graph automorphisms preserve symmetries of the Hamiltonian, and these symmetries constrain the quantum evolution in a way that turns time-dependent local measurements into informative probes of graph structure. Leveraging this idea, we introduce QDAGer, a quantum-inspired graph-pair Transformer that injects quantum-dynamical features from time series of node occupations...
  </details>

- **2026-08-18** — Syeda Faiza Ahmed, Zien Sheikh Ali, Hunzalah Hassan Bhatti et al. — [Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](http://arxiv.org/abs/2608.17605v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI is moving beyond isolated text prompts toward sustained, multimodal interaction. In real conversations, users clarify goals, revise requests, interrupt responses, switch topics, and introduce new evidence while expecting systems to preserve context across turns. This makes multi-turn dialogue a distinct challenge requiring systems to maintain and update memory, ground responses across modalities, tools, and external knowledge, and adapt across languages and cultures. This study...
  </details>

- **2026-08-18** — Ruizhe Wang, Yixuan Dong, Bolin Yang et al. — [DMT-Dens: Density-preserving manifold visualization for biological data](http://arxiv.org/abs/2608.17571v1)
  <details><summary>📄 Abstract</summary>
  Motivation: Low-dimensional embeddings are widely used to explore cell-state heterogeneity in single-cell and other high-dimensional biological data. Although many methods preserve local neighborhoods, they may distort the apparent sampling density of processed observations, altering the visual contrast between dense and sparse regions and complicating the interpretation of rare, transitional, or continuous cell-state populations. Results: We present DMT-Dens, a parametric manifold-visualization...
  </details>

- **2026-08-18** — Ksenia Merzlyakova, Sebastian Padó, Franziska Weeber — [Effects of Answer Format Variation on Gender Bias in Large Language Models](http://arxiv.org/abs/2608.17516v1)
  <details><summary>📄 Abstract</summary>
  Gender bias or other social biases in large language models (LLMs) are frequently evaluated with question answering or survey benchmarks where the LLM needs to give a response in a predefined answer format. It is well known in survey science that the answer format has a substantial impact on answers, just as LLMs are sensitive to the prompt wording. However, to our knowledge it has not been studied yet how changes in answer format impact the measurement of gender bias in LLMs and their alignment...
  </details>

- **2026-08-18** — Hongyan Feng, Sunlai Chen, Xuanyu Liu et al. — [Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](http://arxiv.org/abs/2608.17512v1)
  <details><summary>📄 Abstract</summary>
  Although Large Vision-Language Models (VLMs) have significantly advanced embodied navigation, their direct deployment remains challenging, as existing methods often force VLMs into unnatural action spaces that misalign with their 2D pre-training priors, compounded by rigid reasoning schedules and inefficient memory management. To overcome these limitations, we propose TAMP-Nav, a unified framework for efficient embodied navigation. First, we introduce a Pixel-to-3D Action Formulation (Point) tha...
  </details>

- **2026-08-18** — Feiyu Shen, Kun Xie, Yichen Wu et al. — [FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations](http://arxiv.org/abs/2608.17492v1)
  <details><summary>📄 Abstract</summary>
  Recent continuous autoregressive TTS models operate directly on continuous speech representations, preserving rich acoustic details while leveraging the instruction-following capabilities of text LLMs. This paradigm opens new possibilities for voice cloning, instruction-controlled voice design, and speech editing, but remains susceptible to error accumulation during autoregressive generation. Existing solutions often require additional semantic modules, multi-stage tokenizer training pipelines, ...
  </details>

- **2026-08-18** — Yibo Liu, Bowen Jiang — [When More Foundation Models Means Less: Diagnosing and Addressing Multi-View Fusion Failure](http://arxiv.org/abs/2608.17490v1)
  <details><summary>📄 Abstract</summary>
  Foundation-model hubs turn multi-view fusion into a selection problem: from a large heterogeneous encoder pool, which views should be fused, and how many? We show that downstream performance is non-monotonic in the number of fused encoders; later views can be redundant or task-misaligned, causing accuracy to saturate or decline. We formalise this setting as view-set composition and propose KAGES (Kernel-Alignment Greedy Encoder Selector), a label-aware method that orders frozen encoders by their...
  </details>

- **2026-08-18** —  AIMAE Team, Tianxiang Chen, Yan Cheng et al. — [Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents](http://arxiv.org/abs/2608.17319v1)
  <details><summary>📄 Abstract</summary>
  Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including execution, supervision, optimization, and evaluation, rather than scale alone. We present Wuying-Browser-Agent, a unified framework that addresses each of these levels. A structured br...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 70 papers

- **2026-08-21** — Shiva Shrestha, Kazi Shaharair Sharif, Zongxing Xie et al. — [Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI](http://arxiv.org/abs/2608.21172v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning enables large language models to adapt on edge devices without centralizing private data, but practical deployments must address hardware instability and adversarial update corruption together. Thermally constrained clients may throttle, slow local training, or delay synchronous aggregation, while Byzantine clients and communication-layer adversaries can corrupt the updates used to form the global model. To address these challenges, we present Thermo-FL, a thermal-aware fed...
  </details>

- **2026-08-21** — Bipasha Kundu, Abhishek Chaturvedi, Axel W. E. Wismueller et al. — [Toward Vision Language Model-based Assessment of Clinical Quality and Usability of LGE-MR Images for Cardiac Ablation Planning](http://arxiv.org/abs/2608.21180v1)
  <details><summary>📄 Abstract</summary>
  LGE cardiac MRI is widely used for left atrial fibrosis assessment and ablation planning in atrial fibrillation patients as knowledge of fibrotic tissue regions identified from LGE-MRI is critical for catheter ablation. Often, poor quality images used during ablation planning can cause mis-localization of ablation targets, directly impacting procedure safety and outcome. The decision of whether a scan meets the minimum quality threshold for ablation planning is currently made informally by the r...
  </details>

- **2026-08-21** — Ruihua Han, Rui Gao, Zhe Liu et al. — [SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control](http://arxiv.org/abs/2608.21175v1)
  <details><summary>📄 Abstract</summary>
  Safe and efficient shape-aware navigation in heterogeneous crowds and robot fleets remains challenging. Traditional approaches often assume homogeneous robots, sparse workspaces, simplified geometry, offline computation, or handcrafted parameters to make the problem tractable, which limits their deployment in dense crowd scenarios. Toward this end, we propose Shape-Aware Reinforcement Learned Model Predictive Control (SRL-MPC), a method for safe, efficient, and adaptive navigation in crowds with...
  </details>

- **2026-08-21** — Xin Sun, Di Wu, Yuchen Guo et al. — [When Trust Meets Truth: Trust-Truth Separability in LLM-as-Judge](http://arxiv.org/abs/2608.21097v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-Judge systems can produce multi-dimensional evaluations, such as trustworthiness, reliability, and factuality, and these outputs are often interpreted as independent evidence. We test this assumption for a common pair of judgments: trust scoring and binary truth classification. On correctness-controlled QA, LLM judges align trust scores with truth verdicts more tightly than human behavioral reference, suggesting weaker separations between trust and truth judgment. We then apply stress tes...
  </details>

- **2026-08-21** — Alexander Thomas, Hubert P. H. Shum, Darren Nellis et al. — [Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance](http://arxiv.org/abs/2608.21036v1)
  <details><summary>📄 Abstract</summary>
  The transport of dangerous goods by sea is a high-consequence activity governed by the International Maritime Dangerous Goods (IMDG) Code, a complex regulatory framework where errors in classification, packaging, stowage, or segregation can result in fire, explosion, toxic release, or loss of life or vessel. Correct compliance requires accurately interpreting hundreds of pages of interacting provisions, updated on a two-year amendment cycle. Practitioners increasingly use Large Language Models (...
  </details>

- **2026-08-21** — Ye Chen, Weining Zhang — [No Judgment Without a Reason: Counterfactual Receipts for Versioned AI Evaluators](http://arxiv.org/abs/2608.20938v1)
  <details><summary>📄 Abstract</summary>
  Evaluators often produce correct labels via flawed reasoning, a critical failure for agentic systems gating actions, routing reviews, or supplying training feedback. Standard evaluation only verifies final label correctness, ignoring whether judgment changes stem from valid evidence, consistent rules, or proper rule applicability. We formalize evaluator reasoning accountability via three core sources: grounds, norms, and authority. Varying these sources yields an eight-cell counterfactual judgme...
  </details>

- **2026-08-21** — Baixin Li, Haiyun He — [SAC-Copula: Quality-Preserving Watermarking for Diffusion Language Models via Smooth Correlated Gumbel Fields](http://arxiv.org/abs/2608.20839v1)
  <details><summary>📄 Abstract</summary>
  Watermarking diffusion language models (DLMs) requires mechanisms compatible with iterative parallel unmasking rather than autoregressive decoding. Existing sampling-based watermarking methods typically inject position-wise i.i.d. perturbations, which can be poorly aligned with DLM decoding dynamics and degrade generation quality. We propose SAC-Copula, a quality-preserving watermarking method for DLMs based on smooth, locally correlated Gumbel perturbation fields constructed via a Gaussian copu...
  </details>

- **2026-08-21** — Haodong Chen, Yadong Wang, Shengtao Wen et al. — [Knowing but Not Saying: Preventing Factual Access Failures in LLM SFT via Recall-Anchored Distillation](http://arxiv.org/abs/2608.20794v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) can degrade factual behavior outside the target domain. This degradation is often described as catastrophic forgetting, yet open-ended factual failures do not necessarily imply that the underlying facts have been erased. In this work, we identify a more specific phenomenon, factual access failure: after domain SFT, models can still recognize or rank the correct answer under constrained evaluation, while failing to produce it in closed-book generation. Through benchma...
  </details>

- **2026-08-21** — Yiwen Liu, Yujun Zhu, Kui Jia et al. — [ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations](http://arxiv.org/abs/2608.21355v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-based action models have demonstrated strong capabilities in complex manipulation, but they rarely leverage explicit object physical properties to adapt their policies. We introduce ViTacPhys, a visual-tactile framework and data acquisition system that estimates object mass and friction-coefficient classes, together with continuous stiffness, from human manipulation demonstrations. Trained on data from 60 rigid and deformable objects, ViTacPhys combines temporal visual-tactile mode...
  </details>

- **2026-08-21** — Deepanshu Pandey, Arnav Chavan, Nahush Lele et al. — [Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models](http://arxiv.org/abs/2608.20988v1)
  <details><summary>📄 Abstract</summary>
  Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors. We identify the softmax operator as a bottleneck for quantization stability due to its sensitivity to outliers and state-dependent Jacobian. We theoretically establish that suppressing the norm of this Jacobian helps in bounding quantization-induced performance degradation. Based on this, we propose Jacobian-Guided Noise Injection, a training strategy that i...
  </details>

- **2026-08-21** — Youval Klioui — [SR-TL1: A Square-Root TL1-Norm Framework for Robust SMV DoA Estimation under Highly-Coherent Dictionaries](http://arxiv.org/abs/2608.20943v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a Square-Root Transformed $L_1$-norm ($SR\text{-}TL_{1}$) sparse recovery framework for single-measurement-vector (SMV) direction of arrival (DoA) estimation under highly-coherent overcomplete dictionaries with angular-dependent array imperfections. The proposed framework combines the square-root Least Absolute Shrinkage and Selection Operator (square-root LASSO) framework which is known to be robust against noise variance with the Transformed $L_1$-norm ($TL_1$-norm), a non-...
  </details>

- **2026-08-20** — Mehdi Azarafza, Faezeh Pasandideh, Ali Ehteshami Bejnordi et al. — [Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving](http://arxiv.org/abs/2608.20129v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles require robust perception and decision-making capabilities to operate in diverse and unseen scenarios. While reinforcement learning and rule-based methods can provide effective control and safety mechanisms, their performance may degrade in situations requiring contextual reasoning. Large Language Models (LLMs) have demonstrated strong capabilities in understanding multimodal information and generating contextual reasoning, however, their use for direct vehicle control can in...
  </details>

- **2026-08-20** — Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson et al. — [When Text and Numbers Disagree: Evidence Arbitration in Large Language Models](http://arxiv.org/abs/2608.20116v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in settings where textual summaries, numerical observations, and external tool outputs may provide conflicting evidence. We study how LLMs arbitrate between such sources when they support opposing decisions. To do so, we introduce a controlled synthetic benchmark in which latent risk trajectories generate both numerical time series and natural language summaries, allowing us to construct conflicts where exactly one evidence source is aligned wit...
  </details>

- **2026-08-20** — Bin Zhu, Yi Xie, Yanghui Rao — [Stopping and Routing LLM Judge Panels](http://arxiv.org/abs/2608.19802v1)
  <details><summary>📄 Abstract</summary>
  LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction should stop. We formulate judge-panel design as a role-conditioned allocation problem. From a small labeled audit set, declared slices, and judge costs, the method estimates target-rela...
  </details>

- **2026-08-20** — Honglie Wang, Jia Sun, Zijun Li et al. — [TextRefine: Improving Textual Fidelity, Spatial Placement, and Glyph Rendering for Text Editing in Product Posters](http://arxiv.org/abs/2608.19637v1)
  <details><summary>📄 Abstract</summary>
  Text editing in product posters entails inserting new text or replacing existing text while preserving product appearance, background content, and global composition. Despite recent progress in instruction-based image editing, general-purpose models remain unreliable in this setting: they often omit or incorrectly render the target text, place it over salient products or pre-existing content, and produce structurally distorted or visually inconsistent glyphs. We introduce \textbf{TextRefine}, a ...
  </details>

- **2026-08-20** — Xuan He, Cong Wei, Yuhao Cheng et al. — [VGI-BENCH: Probing Visual Intelligence in Video Generation Models](http://arxiv.org/abs/2608.19583v1)
  <details><summary>📄 Abstract</summary>
  Recent studies suggest that video generation models can exhibit certain forms of zero-shot visual reasoning through generated frames. Yet reliable evaluation remains challenging: benchmarks should adopt inputs aligned with the visual priors of current video models, require valid evolving processes rather than only plausible final states, and calibrate task difficulty to remain challenging yet partly feasible. To this end, we introduce VGI-bench, containing 27 tasks and 810 instances, organized b...
  </details>

- **2026-08-20** — Yu-Bo Shi, Markus Heyl, Roderich Moessner et al. — [Reinforcement LearningtoHarness Approximation Errors for Long-Time QuantumSimulation](http://arxiv.org/abs/2608.20139v1)
  <details><summary>📄 Abstract</summary>
  Accurate digital quantum simulation at long times is limited by the accumulation of errors inherent to approximate simulation. Here we introduce RL-Trotter, a reinforcement-learning framework that treats unavoidable approximation errors as resources for error correction rather than merely imperfections to suppress. We show that low-dimensional information from conservation laws, such as the energy and energy variance, provides a sufficient learning signal to guide the agent, which learns to adap...
  </details>

- **2026-08-20** — Yingjian Chen, Fan Gao, Sherry T. Tong et al. — [HealMed: Multilingual Evaluation of Large Language Models in Medicine](http://arxiv.org/abs/2608.19981v1)
  <details><summary>📄 Abstract</summary>
  We present HealMed, an expert-reviewed benchmark for multilingual evaluation of large language models in medicine. HealMed contains 1,000 examples in each of nine languages, drawn from nine datasets and covering three task formats: MCQA, NLI and open-ended QA. The benchmark was developed over two years by 23 physicians and medical experts based across nine countries and regions. Each translation was evaluated and revised by two experts fluent in English and the corresponding target language. On ...
  </details>

- **2026-08-20** — Zhiyuan Jia — [Random Cap: Optimal Informationally Robust Delegation](http://arxiv.org/abs/2608.19846v1)
  <details><summary>📄 Abstract</summary>
  Are simple delegation rules optimal under ambiguity? We study delegation when the principal knows the mean, but not the distribution, of the agent's private information. In a quadratic constant-bias environment, the robustly optimal randomized mechanism is a random cap: the principal draws and reveals an upper bound below which the agent chooses freely. Randomization strictly outperforms every deterministic cap by hedging against cap-specific worst-case distributions. We characterize random caps...
  </details>

- **2026-08-20** — Rongyu Yu, Ke Niu, Fengxiang He — [Answer-Level Trust Selection for Physical Vision-Language Reasoning](http://arxiv.org/abs/2608.19807v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can estimate physical quantities such as duration, speed, and acceleration from visual observations, but existing benchmarks primarily assess overall model performance against annotated ground truth. In deployment, a key question is whether an individual prediction can be trusted when its ground truth is unavailable. Self-consistency alone may fail to capture important failure modes: a VLM may produce stable-but-wrong estimates or rely on textual priors rather than ...
  </details>

- **2026-08-20** — Haiyue Zhang — [Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay](http://arxiv.org/abs/2608.19760v1)
  <details><summary>📄 Abstract</summary>
  Audited against causal ground truth from executed replay in a single-agent tool environment (ALFWorld), none of the step-level credit signals used to train LLM agents -- LLM-judge scores, outcome-conditioned logprob ratios, or the policy's own confidence -- identifies which steps causally matter better than chance. Existing evaluations grade these signals against annotated step *correctness*; we audit them against step *contribution* -- what re-sampling the policy's own alternatives at each deci...
  </details>

- **2026-08-20** — En Zhi Tan, Jia Xiang Lim, Bryan Lijie Chew et al. — [RecPFN: Prior-Fitted Networks for In-Context-Based Recommendations](http://arxiv.org/abs/2608.19735v1)
  <details><summary>📄 Abstract</summary>
  We introduce RecPFN, a prior-fitted network that brings in-context learning to sequential recommendation. RecPFN is pretrained entirely on synthetic clickstream environments sampled from a broad structural causal prior, enabling it to amortize Bayesian-style inference from a small support set. At inference, a lightweight decoder-only transformer conditions on a handful of domain sequences and produces next-item predictions for queries in a single forward pass, without any weight updates. Across ...
  </details>

- **2026-08-20** — Chenchen Lin, Wenhao Yuan, Xuehe Wang et al. — [Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration](http://arxiv.org/abs/2608.19701v1)
  <details><summary>📄 Abstract</summary>
  Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written by different agents may inherit the same upstream source or shared bias, causing correlated evidence to be repeatedly counted and creating a false majority. We term this failure mode...
  </details>

- **2026-08-20** — Guangxin Song, Xing Fang, Mingmin Jin et al. — [SSR-GRPO: Integrating Supervision and Semantic IDs into Reinforcement Learning for Dense Retrieval in E-commerce](http://arxiv.org/abs/2608.19595v1)
  <details><summary>📄 Abstract</summary>
  Embedding-based retrieval (EBR) is pivotal in e-commerce search but often struggles with complex semantics. While recent methods often fine-tune large language models (LLMs) for representation learning, they typically lack robust mechanisms for handling complex and implicit semantics. While Retrieval-GRPO (R-GRPO) recently introduced reinforcement learning to dense retrieval, it suffers from noisy top-K candidates due to limited batch sampling and biased relevance assessments caused by using sim...
  </details>

- **2026-08-19** — Yiming Sun, Shengyu Chen, Zhengzhang Chen et al. — [Quantifying Event Impacts on Time Series via Multiscale Contrastive Learning](http://arxiv.org/abs/2608.19447v1)
  <details><summary>📄 Abstract</summary>
  Shocks that spread through the web, such as cybersecurity breach disclosures, can abruptly disrupt financial time series and cause substantial abnormal losses. While these events are disclosed as discrete records through news reports, regulatory filings, or public databases, their consequences unfold through continuous market dynamics. This creates an event-conditioned impact prediction problem: given pre-event market history and limited event metadata, the goal is to estimate short-term post-di...
  </details>

- **2026-08-19** — Jai Kumar Sharma, Amartya Dutta — [Does Marginal Coverage Guarantee Class-Conditional Safety for Zero-Shot VLMs Under Shift?](http://arxiv.org/abs/2608.19376v1)
  <details><summary>📄 Abstract</summary>
  Split-conformal prediction provides marginal coverage under exchangeability and is increasingly used as an abstention layer for zero-shot vision-language models (VLMs). We audit this practice under deployment shift for CLIP, OpenCLIP, and SigLIP across ImageNet and non-ImageNet settings. Marginal coverage can remain relatively high while class-conditional tail coverage collapses: on ImageNet-Sketch, worst-class coverage falls to $\approx 0$ and 10-12% of classes lie below a finite-sample null fl...
  </details>

- **2026-08-19** — Baptiste Rossigneux, Inna Kucher, Vincent Lorrain et al. — [Clustering and Token Denoising for Faster and More Robust VLMs](http://arxiv.org/abs/2608.19285v1)
  <details><summary>📄 Abstract</summary>
  Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLaVA showing impressive results. However, the computational burden of processing up to 576 or 729 visual tokens makes edge deployment challenging. While various token pruning techniques require retraining, some are training-free and thus can easily adapt to architecture changes. We introduce ClustRS, a two-part, training-free algorithm for robust t...
  </details>

- **2026-08-19** — Kai Li, Jong-Ik Park, Carlee Joe-Wong et al. — [FedLNS: Leverage LayerNorm Signature Modeling to Mitigate Adversarial Manipulation in Federated LLMs](http://arxiv.org/abs/2608.18736v1)
  <details><summary>📄 Abstract</summary>
  Federated training enables language models to learn from distributed private text, but the server cannot directly verify the local supervision or optimization process that produces each client update. A malicious client can therefore train on corrupted targets, introduce incorrect context-token associations, and degrade the global model through repeated aggregation. Such degradation can also increase the risk of unreliable or hallucinatory generation. We propose Federated Learning with Normaliza...
  </details>

- **2026-08-19** — Chao Li, Yuanfa Li, Wenhao Wu et al. — [MemFuse: Multi-Source Memory Fusion from Fragmented Observations](http://arxiv.org/abs/2608.18704v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is essential for agents that operate across extended interactions, yet existing memory systems and benchmarks predominantly focus on single-source textual histories. In realistic settings, however, relevant information is often fragmented across applications and devices, as well as across users and time, requiring agents to integrate dispersed observations into coherent episodic memories while preserving their source provenance. To address these gaps, we introduce **MemFuseBench...
  </details>

- **2026-08-19** — Roie Kazoom, Ofir Cohen, Rami Puzis et al. — [Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation](http://arxiv.org/abs/2608.18681v1)
  <details><summary>📄 Abstract</summary>
  We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting synthetic examples with a fixed reward threshold, our method formulates adversarial data curation as a failure-mode contextual bandit problem. Candidate examples are generated with retrieval-augmented prompting, filtered by the current target model, automatically validated by an LLM judge ensemble, and clustered into recurring failure modes. A s...
  </details>

- **2026-08-19** — Deep Kumar Ganguly, Jan Křetínský — [Robust Risk Under Evolving Uncertainty: A Wasserstein Counterpart of the Entropic Value-at-Risk](http://arxiv.org/abs/2608.19073v1)
  <details><summary>📄 Abstract</summary>
  An agent still learning its environment should be cautious while ignorant and bold once confident. The entropic value-at-risk captures this through a robust-optimization identity---a confidence level fixes the radius of a relative-entropy ball of alternative models---but that ball cannot reach catastrophes the nominal deems impossible, precisely what a safe agent must hedge. We instead use an optimal-transport ball and study the coherent risk measure it induces, the Wasserstein entropic value-at...
  </details>

- **2026-08-19** — Mohaimenul Azam Khan Raiaan, Nur Mohammad Fahad — [EVADE: Evidence-Verified Agentic Diagnosis with Escape](http://arxiv.org/abs/2608.18833v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) can achieve high accuracy but remain unreliable: they are systematically overconfident, benefit little from test-time reasoning, and lack the ability to reliably calibrate trust in their own responses. We introduce EVADE (Evidence-Verified Agentic Diagnosis with Escape), an inferential, non-training method that enhances the safety of deploying a single frozen VLM. EVADE responds and, when uncertain, localises the region most diagnostically relevant, re-answe...
  </details>

- **2026-08-19** — Steven Landgraf, Markus Ulrich — [The Impact of CutMix on Reliability and Robustness in Semantic Segmentation](http://arxiv.org/abs/2608.18715v1)
  <details><summary>📄 Abstract</summary>
  Ensuring not only high accuracy but also reliable and robust predictions is critical for the deployment of semantic segmentation models in safety-critical applications such as autonomous driving. Despite the widespread use of CutMix - a simple yet powerful data augmentation strategy - its effect on the reliability and robustness in dense predictions tasks remains unexplored. Motivated by recent findings that semi-supervised segmentation methods, where CutMix is a core component, can severely deg...
  </details>

- **2026-08-19** — Steven Landgraf, Joceline Hinz, Markus Ulrich — [A Critical Synthesis of Uncertainty Quantification and Foundation Models for Semantic Segmentation](http://arxiv.org/abs/2608.18709v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly breaking what seemed to be impossible not long ago by enabling unprecedented accuracy and cross-domain generalization. Yet their lack of interpretability, tendency to be overconfident, and sensitivity to real-world domain shifts pose critical challenges for safety- and mission-critical applications. Uncertainty quantification (UQ) offers a principled way to address these issues, but its integration into segmentation foundation models has yet to be explored. In ...
  </details>

- **2026-08-19** — Chenglin Liu, Xun Wang, Ruishuo Chen et al. — [MLREF: Efficient Module Reuse for Reward Design in Reinforcement Learning via Large Language Models](http://arxiv.org/abs/2608.18827v1)
  <details><summary>📄 Abstract</summary>
  Reward function design remains a bottleneck in reinforcement learning. While large language models (LLMs) have enabled automated reward generation, existing methods generate and revise reward functions as monolithic programs, making it difficult to reliably preserve and reuse effective components discovered in earlier iterations, leading to unstable performance across iterations. To address this, we propose Module Level Reward Evolution Framework (MLREF). At the core of MLREF is a module pool, a...
  </details>

- **2026-08-19** — Khoa Dang Tao, Sumin Jin, Muhammad Raza et al. — [Quantum circuit optimization using deep reinforcement learning: Applications across multiple gate sets](http://arxiv.org/abs/2608.19103v1)
  <details><summary>📄 Abstract</summary>
  The practical implementation of quantum algorithms on noisy intermediate-scale quantum devices encounters operational limitations due to decoherence and other sources of noise inherent in real hardware. To mitigate these errors while preserving the original functionality of the algorithm, shorter quantum circuits are therefore preferred. This motivates the development of effective quantum circuit optimization algorithms. Learning-based approaches have emerged as a leading candidate, yet existing...
  </details>

- **2026-08-19** — Yechan Park, HyunJin Kim — [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](http://arxiv.org/abs/2608.19066v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a lightweight, plug-and-play framework that improves robustness to viewpoint shifts in Vision-Language-Action (VLA) policies without policy retraining. To our knowledge, this is the first approach to directly leverage 3D Gaussian-based novel-view synthesis for observation-space adaptation in VLA policies. Current VLA performance relies on the implicit assumption that training and deployment camera configurations are identical. Our experiments show that even a small displaceme...
  </details>

- **2026-08-19** — E. E. Marshall, C. C. Nelmes, T. J. G. Apollaro et al. — [Distinct Modes of Quantum Information Transfer in Power-Law Long-Range Spin Networks](http://arxiv.org/abs/2608.19057v1)
  <details><summary>📄 Abstract</summary>
  We identify different regimes of quantum state transfer in long-range coupled spin-$\frac{1}{2}$ systems, where naturally occurring power-law interactions enable rapid, high-fidelity transfer with minimal engineering. Across a broad range of interaction profiles, from effectively nearest-neighbour coupling to Coulomb interactions, we show how long-range connectivity fundamentally reshapes the mechanisms underlying information propagation within such systems. For effectively short-range interacti...
  </details>

- **2026-08-19** — Emily Yang, Liyuan Guo, Seyed Mohammad Ali Zeinolabedin et al. — [Robust and Efficient Feature Extraction for Spike Sorting via the Walsh-Hadamard Transform](http://arxiv.org/abs/2608.19048v1)
  <details><summary>📄 Abstract</summary>
  Implantable neural interfaces require low-power real-time signal processing to remain within strict thermal and bandwidth constraints, motivating lightweight feature extraction methods for on-chip spike sorting. This work presents the Walsh-Hadamard Transform (WHT) as a hardware-efficient feature extraction method for neural spike classification. WHT can be implemented using only adders, subtractors, and registers without coefficient memory. WHT performance is compared against the Compressed Had...
  </details>

- **2026-08-19** — Xiang Yin, Adam Dejl, Antonio Rago et al. — [A Theory of Post-hoc Debate Judgement](http://arxiv.org/abs/2608.19002v1)
  <details><summary>📄 Abstract</summary>
  Debates have recently emerged as a useful methodology for agentic AI to improve performance as well as to aid explainability and user engagement. For example, LLM-empowered agents may debate internally (with themselves) and/or externally (with other agents). In many settings where debates are used, debates' outcomes and resulting outputs are determined post-hoc by external judges, often LLMs. In this paper we develop and test a novel theory of debate judgement applicable to all settings where ag...
  </details>

- **2026-08-19** — Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev et al. — [Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis](http://arxiv.org/abs/2608.18940v1)
  <details><summary>📄 Abstract</summary>
  Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consisten...
  </details>

- **2026-08-19** — Souranil Kahali, Rituparna Bose, Abner Hernandez et al. — [Understanding Multilingual Medical ASR Adaptation Through Layer-Wise Analysis](http://arxiv.org/abs/2608.18825v1)
  <details><summary>📄 Abstract</summary>
  Medical automatic speech recognition (MedASR) requires adaptation to specialised terminology, limited annotated clinical data, and multilingual use cases. Although large-scale pretrained ASR models such as Whisper achieve strong generalisation, their behaviour after medical and multilingual adaptation remains insufficiently understood beyond word error rate (WER). This paper investigates how multilingual medical adaptation reshapes the internal representations of Whisper models through layer-wis...
  </details>

- **2026-08-19** — Fathin Difa Robbani — [Readable, Faithful, Used: Three Dissociable Properties of Demographic Identity in a Language Model](http://arxiv.org/abs/2608.18768v1)
  <details><summary>📄 Abstract</summary>
  Large language models are widely used to simulate survey respondents, yet their answers are homogeneous and unfaithful to real inter-group differences. We ask where demographic group identity lives inside an LLM, how faithfully its geometry mirrors real inter-group opinion structure, and whether it uses what it encodes. Using representational similarity analysis against Pew ground truth over 169 demographic cells, we score 1,089 read-out locations in Mistral-7B and intervene causally across six ...
  </details>

- **2026-08-19** — Susobhan Bandopadhyay, Anish Datta, Palash Dey et al. — [Fair, Efficient and Connected Allocations on Graphs](http://arxiv.org/abs/2608.18703v1)
  <details><summary>📄 Abstract</summary>
  We study the classical and parameterized complexity of efficient connected allocation problems on graphs, where efficiency is measured by egalitarian and utilitarian welfare maximization. We first establish a sharp complexity dichotomy in the classical setting: both problems are NP-hard in general and remain hard even on very restricted graph classes such as paths, and consequently trees and cycles. In contrast, they are polynomial-time solvable on stars, but this tractability does not extend ev...
  </details>

- **2026-08-19** — Qi Ma, Shipra Jain, Niko Benjamin Huber et al. — [Teeth2Point: A Two-Stage Dental CBCT ROI-to-Point Segmentation Framework](http://arxiv.org/abs/2608.18667v1)
  <details><summary>📄 Abstract</summary>
  Modern deep learning architectures have demonstrated strong performance in dental CBCT segmentation. One remaining crucial challenge is accurate tooth labeling in cases with missing or malpositioned teeth, which are highly relevant for dental practice. Transformer-based architectures should in theory be able to resolve such ambiguities using global anatomical context. However, due to the high resolution of CBCT volumes and the wide spatial distribution of teeth within volumes, dense patch-based ...
  </details>

- **2026-08-19** — Zinuo Guo, Min Zhang, Bo Jiang — [OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios](http://arxiv.org/abs/2608.18586v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly used as OCR systems in document and knowledge-processing pipelines, but their ability to faithfully read real handwriting remains underexplored. Existing OCR benchmarks focus largely on printed text or clean single-line inputs, leaving limited coverage of realistic handwritten OCR scenarios such as multilingual handwriting, writer errors, and structurally complex mathematical expressions. We introduce OmniHandwritingOCR, a diagnostic benc...
  </details>

- **2026-08-19** — Ting-Wei Li, Yuanchen Bei, Xiao Lin et al. — [Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution](http://arxiv.org/abs/2608.18575v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based multi-agent systems (MAS) often exhibit complex failure modes, which frequently cause agents to produce incorrect outcomes. This motivates the task of Agent Failure Attribution: given a failed multi-agent trajectory, identify the faulty agents and their corresponding error types. Existing approaches predominantly rely on LLMs to perform failure attribution, either through direct prompting, fine-tuning on synthetic data or complex agentic pipelines. While effectiv...
  </details>

- **2026-08-19** — Shinji Hara, Yutaka Hori, Tetsuya Iwasaki et al. — [Robust Instability Radius for Networked Dynamical Systems: Upper and Lower Bounds](http://arxiv.org/abs/2608.18561v1)
  <details><summary>📄 Abstract</summary>
  This paper is concerned with robust instability of uncertain network systems. We consider the multi-agent system described as a network of single-input-single-output agents with identical nominal dynamics subject to heterogeneous perturbations. The network description is formalized as a feedback interconnection of a diagonal uncertainty, nominal identical agents, and a static interconnection matrix. Assuming that the nominal network is unstable, we seek the robust instability radius (RIR), defin...
  </details>

- **2026-08-19** — Shinji Hara, Yutaka Hori, Tetsuya Iwasaki et al. — [Exact Robust Instability Analysis for Networked Dynamical Systems with Biological Application](http://arxiv.org/abs/2608.18553v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates robust instability in nominally unstable uncertain networked dynamical systems, where all nominal agents share an identical single-input-single-output (SISO) linear time-invariant (LTI) system and each agent is subject to independent perturbations. This setting is motivated by the problem of sustaining periodic oscillations in nonlinear dynamics, for which exact analysis is generally intractable. We identify three classes of network structures including cyclic and certain...
  </details>

- **2026-08-19** — Yansong Wang, Zhaobo Qi, Xinyan Liu et al. — [DyG$^2$T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer](http://arxiv.org/abs/2608.18498v1)
  <details><summary>📄 Abstract</summary>
  Modeling object dynamics from limited visual observations is a fundamental problem for enabling accurate motion trajectory prediction in embodied interaction scenarios. Existing dynamics modeling methods first compress reconstructed particle representations into sparse Key Points and model their evolution using locally constrained interactions, thereby discarding fine-grained local details and obscuring discriminative interaction modeling across spatial and temporal scales, leading to drifting t...
  </details>

- **2026-08-19** — Hang Wang, Hang Dong, Lu Liu et al. — [MissDiag: Diagnostic Evaluation of Incomplete-Knowledge Robustness in KGQA and KG-RAG](http://arxiv.org/abs/2608.18489v1)
  <details><summary>📄 Abstract</summary>
  Knowledge graph question answering (KGQA) and knowledge-graph-based retrieval-augmented generation (KG-RAG) aim to ground answers in explicit graph evidence, but real-world knowledge graphs are often sparse, outdated, and incomplete. Existing robustness evaluations usually report aggregate changes in answer quality after evidence is removed or perturbed, which measures sensitivity to incomplete support but leaves the source of degradation under-specified: the same score change can conflate the t...
  </details>

- **2026-08-19** — Shreeya Sharma, Ravish Gupta, Saket Kumar et al. — [Pedagogical AI in Mental Health: A Tri-Stream Fine-Tuned LLM Framework for Automated Clinical Supervision and Risk Triage](http://arxiv.org/abs/2608.18438v1)
  <details><summary>📄 Abstract</summary>
  Modern mental healthcare faces a critical shortage of senior supervisory oversight, leading to a "supervision gap" where novice therapists manage high-stakes risks with delayed professional feedback. This paper proposes a new framework utilizing a fine-tuned Mistral-7B-instruct model as an automated "Supervisor-in-the-Loop" system. By leveraging 106 sessions from the DAIC-WOZ dataset, the model performs a tri-stream analysis: (1) Therapeutic Alliance tracking via semantic adherence, (2) Latent r...
  </details>

- **2026-08-19** — Kentaro Takeda, Masahiro Kojima — [A seamless dose-optimization design for monotherapy and combination therapy](http://arxiv.org/abs/2608.18435v1)
  <details><summary>📄 Abstract</summary>
  The emergence of molecular-targeted agents and immune-oncology therapies has fundamentally transformed oncology drug development, necessitating evolution beyond traditional dose-finding approaches designed for cytotoxic agents. While conventional agents exhibit predictable monotonic dose-response relationships, novel anticancer agents often demonstrate plateau-effect patterns where higher doses may compromise therapeutic benefit, requiring identification of optimal biological doses that balance ...
  </details>

- **2026-08-19** — Jesse Ponnock — [What Does Attention Transfer Transfer? Attention Structure and Robustness in Vision Transformers](http://arxiv.org/abs/2608.18399v1)
  <details><summary>📄 Abstract</summary>
  Vision transformers (ViTs) trained to copy a pretrained teacher's attention maps recover most of fine-tuning's in-distribution accuracy yet fall measurably short of it under distribution shift, as recent work has shown. What the copy delivers has never been measured directly in the attention structure and tied to robustness. We build that instrumentation for ViT-S students of a self-supervised teacher on ImageNet-100, and report three findings that triangulate one conclusion. First, the transfer...
  </details>

- **2026-08-18** — Tahmid Zaman Tahi, Syed Samiul Alam, Haolin Tang et al. — [BR-FiLM: Bounded Residual Channel-Quality Conditioning for Automatic Modulation Recognition](http://arxiv.org/abs/2608.18395v1)
  <details><summary>📄 Abstract</summary>
  Automatic Modulation Recognition (AMR) plays a crucial role in enabling robust, adaptive, and secure communication for military and civilian applications. Deep learning has enabled effective AMR methods that overcome the computational inefficiency of traditional approaches. However, these deep learning based methods often degrade significantly in low SNR conditions, where noise obscures modulation-discriminative waveform features. In this paper, we propose Bounded Residual Feature-wise Linear Mo...
  </details>

- **2026-08-18** — Hasan Najib Mahmud, Shreya Gupta, Isha Chaudhary et al. — [A Jagged Frontier: Evaluating Robustness of Code Agents to Semantics-Preserving Transformations](http://arxiv.org/abs/2608.18389v1)
  <details><summary>📄 Abstract</summary>
  AI code agents are increasingly deployed to resolve real software issues, yet their reliability under superficial code variations remains poorly understood. We evaluate whether coding agents that repair repository-level issues remain reliable when the surrounding codebase is rewritten into a semantically equivalent form. We introduce a random variant sampler that applies common semantics-preserving transformations (SPTs) - spanning control-flow rewrites, dead-code injection, and identifier renam...
  </details>

- **2026-08-18** — Dae Lee, Mihai Delgeanu, Adel Youssef — [SESSE: Sketch, Expand, Sort, Summarize, Evaluate -- LLM-as-Judge Evaluation via Structured Decomposition](http://arxiv.org/abs/2608.18303v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-judge evaluation reduces response quality assessment to a single holistic A/B preference choice, providing no mechanism to isolate which quality dimensions drove the preference or distinguish model errors from genuine label ambiguity. We propose SESSE (Sketch, Expand, Sort, Summarize, Evaluate), a training-free framework that decomposes holistic judgment into structured sub-questions mined directly from the judge's own error cases; requiring no oracle responses, task-specific rubrics, or ...
  </details>

- **2026-08-18** — Junjie Luo, Xuzhe Zhi, Rui Han et al. — [FairGlucose: A CGM Fairness Benchmark Reveals Subgroup Disparities Hidden in Population-Level Validation](http://arxiv.org/abs/2608.18296v1)
  <details><summary>📄 Abstract</summary>
  As CGM-based AI tools approach clinical deployment, whether their accuracy is equitable across patient demographics remains insufficiently tested. To enable this evaluation, we constructed FairGlucose, a 300-patient CGM cohort balanced across 12 demographic strata (age x gender x type 1/type 2 diabetes), with 132,480 forecasting samples and 3,945 unique behavioral events (meals, exercise, medication) logged by 81 patients. Benchmarking 33 models across four families on 2-hour glucose forecasting...
  </details>

- **2026-08-18** — Yingjie Xu, Siwei Yu, Jianwei Ma — [SeisEvo: Evolution of Seismic Data Reconstruction Algorithms by Agents](http://arxiv.org/abs/2608.18272v1)
  <details><summary>📄 Abstract</summary>
  Classical seismic data reconstruction relies on manually designed structural priors and iterative operators, whose coupled design space is far larger than manual trial and error can explore systematically. Deep-learning methods encode the reconstruction rules in learned weights rather than in an explicit operator that can be inspected and modified. We propose SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces...
  </details>

- **2026-08-18** — Pratham Payra, Jagadish B, Tanmay Sen et al. — [SIGMA: Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive Control for Robust, Dependable Traffic Management](http://arxiv.org/abs/2608.18263v1)
  <details><summary>📄 Abstract</summary>
  Traffic signal control is a complex sequential decision-making problem requiring real-time adaptation and trade-offs among throughput, delay fairness, signal stability, and emergency vehicle priority. Existing RL methods often fix objectives, ignore dynamic priority changes, and fail to generalize across geometrically similar intersections.We propose SIGMA (Symmetry-aware, Intelligent, Geometric, Multi-objective Adaptive traffic control), an RL framework enhanced with a large language model (LLM...
  </details>

- **2026-08-18** — Ziyang Cheng, Tianshu Tang, Jinxin Lan et al. — [GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](http://arxiv.org/abs/2608.18234v1)
  <details><summary>📄 Abstract</summary>
  Whole-body motion tracking policies turn a humanoid into a robust control interface: the teleoperator---or an upstream model---only supplies a coarse movement intent, while the low-level policy keeps the robot balanced and physically feasible. Existing trackers deliver this interface only on flat ground: trained in empty scenes, they never learn how contact with terrain and objects reshapes their dynamics, and they attempt to teach the policy to balance under any command by continually enlarging...
  </details>

- **2026-08-18** — Deep Kumar Ganguly, Jan Kretinsky — [Quantifying Risk Under Evolving Uncertainty: Belief-Dependent Robustness for Safe Sequential Decision Making](http://arxiv.org/abs/2608.17574v1)
  <details><summary>📄 Abstract</summary>
  How cautious should an agent be while it is still learning its environment? We propose RATTL (Risk-Adversarial Total-Reward Learning), which ties caution to epistemic uncertainty: the agent holds a Bayesian posterior over unknown dynamics and plans against a Wasserstein ambiguity set whose radius is a monotone function of that posterior. The radius contracts with evidence, so behaviour interpolates continuously between worst-case robustness and risk-neutral total-reward maximization. The design ...
  </details>

- **2026-08-18** — Fangling Jiang, Qi Li, Bing Liu et al. — [Primitive-Driven Compositional Forensic Visual Prompting for Open-World Face Anti-Spoofing](http://arxiv.org/abs/2608.17351v1)
  <details><summary>📄 Abstract</summary>
  Open-world face anti-spoofing must address both covariate and semantic shifts: source and target domains differ in imaging conditions, while target domains contain diverse attack types absent from training. Existing prompt-based approaches often express spoofing through category semantics or language guidance, which is effective for modeling high-level concepts but is less suited to explicitly capturing the evolving fine-grained and spatially heterogeneous forensic evidence of unseen attacks. Mo...
  </details>

- **2026-08-18** — Ingrid navarro, Pablo Ortega-Kral, Yutong Duan et al. — [ControlledShifts: Towards Standardizing Robustness Evaluation in Trajectory Prediction Under Distribution Shifts](http://arxiv.org/abs/2608.17882v1)
  <details><summary>📄 Abstract</summary>
  Trajectory prediction is central to safety in autonomous driving, yet learning-based predictors tend to degrade sharply when encountering scenarios poorly represented by their training data. Many methods attempt to mitigate distribution shift degradation through data-centric or test-time adaptation approaches; however, they are typically validated along fragmented axes of generalization, leaving the field without a standardized way to compare robustness across shifts a model may encounter.   To ...
  </details>

- **2026-08-18** — Yiyan Peng, Philip Wang, Simon Sinong Zhan et al. — [MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation](http://arxiv.org/abs/2608.17386v1)
  <details><summary>📄 Abstract</summary>
  Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along ...
  </details>

- **2026-08-18** — Rui-Huan Wang, Si-Tong Wei, Jia-Qi He et al. — [aDSL: Agentic 3D Creation via Joint Agent-Program Design](http://arxiv.org/abs/2608.17975v1)
  <details><summary>📄 Abstract</summary>
  Programmatic representations provide a compelling paradigm for 3D content creation, enabling fine-grained edits, interpretability, and explicit structural control. Yet, agentic workflows that rely on large language models (LLMs) to author 3D programs remain brittle, often failing to translate high-level intent into consistent low-level geometry. We attribute this fragility to a mismatch between existing programmatic interfaces and the reasoning strengths of LLMs, which favor semantic structure a...
  </details>

- **2026-08-18** — Muhammad A. Muttaqien, Tomohiro Motoda, Ryo Hanai et al. — [ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback](http://arxiv.org/abs/2608.17323v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation policies trained via imitation learning, such as Action Chunking with Transformers (ACT), can achieve strong performance under ideal conditions but often remain sensitive to small execution errors and distribution shifts. Correcting these failures typically requires dataset aggregation and full-policy retraining, which is computationally expensive and unsuitable for real-time deployment. In this work, we propose Online Residual Policy Adaptation (ORPA), a framework that enab...
  </details>

- **2026-08-18** — Haoqin Tu, Yunhao Fang, Yizhong Wang et al. — [Chain-of-Experience for Continual LLM Improvement](http://arxiv.org/abs/2608.18027v1)
  <details><summary>📄 Abstract</summary>
  Humans continuously learn from experience, whereas conventional large language model (LLM) evaluations ignore the models' ability to improve through inference-time interaction. In this paper, we study how LLMs learn from iterative experience at test time, a setting we refer to as Chain-of-Experience (CoE), where models accumulate experiential traces through iterative interactions with self or environmental feedback to form a continual improvement loop beyond zero-shot inference. We instantiate C...
  </details>

- **2026-08-18** — Jhen-Ke Lin — [Grading Needs a Rubric, Not Intelligence](http://arxiv.org/abs/2608.17938v1)
  <details><summary>📄 Abstract</summary>
  Small language models can grade open-ended examination answers as reliably as substantially more expensive models when they grade against an explicit rubric. We test this claim as the design principle behind any-to-bench: a frontier model reads source documents once, at ingestion, to extract each question and its rubric; lower-cost models then perform all repeated grading work. We evaluate six cost-efficient model configurations from two model families at three reasoning-effort levels. Each conf...
  </details>

- **2026-08-18** — Geon Tack Lee, Jaegul Choo, Kang Eun Jeon — [Denoised Variance-Based Pruning with Optimal Brain Bias Compensation](http://arxiv.org/abs/2608.17657v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) achieve state-of-the-art performance but carry massive computational overhead that restricts edge deployment. Although structural pruning has emerged as a key strategy to reduce these costs, existing methods often suffer from severe accuracy degradation or require expensive retraining. Recently, Variance-Based Pruning (VBP) introduced a promising paradigm by selecting neurons based on activation variance; however, it remains limited by statistical noise in finite-sampl...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

- **2026-08-21** — Jason Hickey — [AI with Authority, from Application to Silicon](http://arxiv.org/abs/2608.21356v1)
  <details><summary>📄 Abstract</summary>
  For sixty years, machine verification has been a major cost overhead, affordable only for exceptional artifacts. Here we report that generative AI inverts this relationship: at AI speed, machine verification is not only economical but essential to productivity --- it is the incorruptible referee that lets one person safely direct autonomous machine work at scale. In five weeks, one researcher on consumer AI subscriptions directed a small fleet of AI agents from application code, through a verifi...
  </details>

- **2026-08-21** — Chenguang Pan, Airui Meng, Youmi Suk — [Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics](http://arxiv.org/abs/2608.21165v1)
  <details><summary>📄 Abstract</summary>
  Learning analytics increasingly relies on flexible machine learning (ML), but the model opacity and the burden of deployment prevent these tools from reaching educational practice. We propose a two-stage fine-tuning pipeline that distills a fitted black-box estimator and its post hoc interpretation (the mentor) into a small, open-weight large language model (LLM; the mentee) that returns an individual-level estimate and explains in natural language. The design is estimator-agnostic and paired wi...
  </details>

- **2026-08-21** — Kyle Wild, Yusuke Takahashi, Asako Uraki — [RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation](http://arxiv.org/abs/2608.20845v1)
  <details><summary>📄 Abstract</summary>
  Nearly every retrieval-augmented question-answering system in production ships with a hidden interpreter: on each query a language model re-derives the meaning of raw corpus text and then throws that work away. Cheaper models do not close the gap: per-token prices have fallen by orders of magnitude while inference spend has risen, because context volume grows faster than prices fall. This is the modern equivalent of the full-table scan, and the remedy is the one databases found fifty years ago: ...
  </details>

- **2026-08-20** — Jun Ni Du, Lukas Adamek, Maxim Kryukov et al. — [Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records](http://arxiv.org/abs/2608.20315v1)
  <details><summary>📄 Abstract</summary>
  Predictive models over structured electronic health records (EHRs) remain central to machine learning for healthcare, but few have jointly emphasized quantitative laboratory information and interpretability with respect to input medical events. We present BERT-LER, a BERT-style model for coded EHR timelines pretrained and fine-tuned from a de-identified EHR dataset of 75 million patients, that encodes laboratory test results as discrete tokens while retaining graded information through percentil...
  </details>

- **2026-08-20** — Bhavya Gupta, Onat Gungor, Tajana Rosing — [G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs](http://arxiv.org/abs/2608.19964v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects ...
  </details>

- **2026-08-20** — Zijiao Chen, Nicholas Lu, Xinhui Li et al. — [Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis](http://arxiv.org/abs/2608.19902v1)
  <details><summary>📄 Abstract</summary>
  AI agents can execute scientific analyses, but an analytic output becomes a defensible claim only after alternatives are weighed and the claim is limited to what the evidence supports. Agents may reproduce failures including selective analysis, premature declarations of success and optimization of imperfect criteria. We present Brain Researcher, an agentic research harness operating in a neuroimaging researcher's computational environment under rules for admissible analyses, required checks and ...
  </details>

- **2026-08-20** — Nikita Khudov — [OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large Language Models](http://arxiv.org/abs/2608.20106v1)
  <details><summary>📄 Abstract</summary>
  We introduce OenoBench, a wine-domain knowledge benchmark of 3,266 multiple-choice questions across six pillars (regions, grape varieties, viticulture, winemaking, producers, business) and four difficulty tiers. The corpus is built from 38,104 atomic, source-anchored facts extracted by 35 provenance-verified scrapers from government registries (INAO, TTB, OIV), peer-reviewed journals, and Wikipedia/Wikidata. Our methodological contribution is an LLM-driven pipeline in which language models refor...
  </details>

- **2026-08-20** — Willem Fourie — [A three-dimensional typology of agency for advanced AI systems](http://arxiv.org/abs/2608.20041v1)
  <details><summary>📄 Abstract</summary>
  Research on the agency of advanced artificial intelligence (AI) systems focuses on agency as a normative concept and on the agency of particularly agentic AI systems. While recent work also focuses on the different profiles of agentic systems, no framework exists to address the question of the type of agency instantiated by advanced AI systems, particularly when considering non-moral forms of agency. Based on established theoretical positions in philosophy, ethics, legal theory and sociology, we...
  </details>

- **2026-08-19** — Jiuning Lin, Ruiquan Lan, Xiaodong Zhu et al. — [PILOT Technical Report](http://arxiv.org/abs/2608.18637v2)
  <details><summary>📄 Abstract</summary>
  Existing agentic approaches for recommendation system optimization remain fundamentally reactive: they adjust parameters in response to observed metric changes but lack the ability to proactively design controlled experiments, personalize strategies at the user-segment level, or accumulate reusable experimental methodology across tasks. We present PILOT (Proactive Insight Learner for Online Tree-Experiments), an LLM-agent framework that organizes three roles within a constrained control loop whe...
  </details>

- **2026-08-19** — Daniele Corradetti — [Linguistic Holonomy and Statistical Watermarks: Inner Geometry of Meaning-Preserving Transformations](http://arxiv.org/abs/2608.19369v1)
  <details><summary>📄 Abstract</summary>
  Statistical watermarks for language models live in the freedom of the signifier: they choose among tokens that are nearly equivalent in meaning, and they are therefore eroded by exactly those transformations which move the form of a text while leaving its content in place. The literature measures such transformations by their endpoint, through the semantic similarity between the original and the rewritten text. We show that the endpoint is the wrong statistic. Adapting the formalism of linguisti...
  </details>

- **2026-08-19** — Vijay Erramilli — [Mechanistic Tomography: Designed Measurement for Control-Oriented Interpretability](http://arxiv.org/abs/2608.19338v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability seeks quantities that models do not expose directly: represented states, component effects, interactions, and responses to interventions. Patching, gradients, Hessian-vector products, and subset interventions provide different measurements under different access assumptions and may target different quantities. We formulate their shared measurement structure as mechanistic tomography: designed measurement for recovering internal mechanisms and intervention effects.   ...
  </details>

- **2026-08-19** — Jiuning Lin, Ruiquan Lan, Xiaodong Zhu et al. — [PILOT Technical Report](http://arxiv.org/abs/2608.18637v1)
  <details><summary>📄 Abstract</summary>
  Existing agentic approaches for recommendation system optimization remain fundamentally reactive: they adjust parameters in response to observed metric changes but lack the ability to proactively design controlled experiments, personalize strategies at the user-segment level, or accumulate reusable experimental methodology across tasks. We present PILOT (Proactive Insight Learner for Online Tree-Experiments), an LLM-agent framework that organizes three roles within a constrained control loop whe...
  </details>

- **2026-08-19** — Chenchen Mao, Hanjing Shi, Haiyan Jia et al. — [When Readability and Source Retention Diverge: An Evaluability Gap in AI Translation](http://arxiv.org/abs/2608.19083v1)
  <details><summary>📄 Abstract</summary>
  Readable AI output can leave an evaluability gap: even when the source is shown, an overall-quality judgment may not reflect what an output preserves. We investigated how source-text condition and output rendering relate to perceived translation quality, and how output and system appraisals relate to trust and stated disclosure willingness in a plain-text interface. A focal 2 * 2 comparison (N=306) using TransLingo examined simple generated narratives and complex literary-philosophical prose alo...
  </details>

- **2026-08-19** — Sireesh Gururaja, Jordan Taylor, Emma Strubell — [TractorBeam: Personalized AI Sensemaking Support via Collaborative Machine Annotation](http://arxiv.org/abs/2608.18994v1)
  <details><summary>📄 Abstract</summary>
  Language model-based systems which allow asking questions of documents have become popular tools for sensemaking. Despite their implied capability, these systems still suffer from issues of factuality and provenance, while encouraging confirmatory, rather than exploratory, research. We present TractorBeam, a browser extension-based mixed-initiative system that uses collaborative annotation as an interface metaphor for sensemaking, re-framing language model (LM) outputs as suggested highlights in...
  </details>

- **2026-08-19** — Adel Bouhraoua, Mehdi Zoubiri, Gavin Farrell et al. — [APICURON: a reactive infrastructure for credit attribution across distributed research data ecosystems](http://arxiv.org/abs/2608.18958v1)
  <details><summary>📄 Abstract</summary>
  Data-driven biology relies on structured knowledge generated by expert biocurators, yet this work remains largely unrecognized in traditional academic assessments. To bridge this gap, we present the updated APICURON platform, a credit-attribution infrastructure that formally acknowledges these scientific contributions. Rather than relying on delayed batch reporting, the system captures curation events as they happen and transforms them into verifiable units of work. This design allows independen...
  </details>

- **2026-08-19** — Pratik Ghawate — [FinRCA-Bench: Benchmarking Evidence Retrieval and Reasoning for Financial AI Systems](http://arxiv.org/abs/2608.18534v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to support financial operations, but their apparent reasoning performance can depend on whether they receive the right evidence. In financial reconciliation, the evidence needed for diagnosis is distributed across invoices, purchase orders, approvals, allocations, payments, ledger entries, and bank activity, linked by transactional relationships rather than textual similarity. End-to-end accuracy can therefore conflate evidence access with reasoning qu...
  </details>

- **2026-08-18** — Xiangyu Yin, Ming Du, Michael H. Prince et al. — [Artifact-centered Claim-aware Observability for Autonomous Scientific Agents](http://arxiv.org/abs/2608.18312v1)
  <details><summary>📄 Abstract</summary>
  Autonomous scientific agents now increasingly propose ideas, write code, run experiments, analyze results, and even draft papers. Observe and audit those agents are necessary but logging every model call is not enough, scientists also need to inspect the artifacts and claims that the systems produced and their relations. This is driven by the fact that failures in scientific agent systems are often distributed across several objects. A manuscript claim may cite the wrong evidence, a search proce...
  </details>

- **2026-08-18** — Ebtesam Al-Haque, Brittany Johnson — [What Makes Software Issue Resolution Tasks Difficult for Agents?](http://arxiv.org/abs/2608.18280v1)
  <details><summary>📄 Abstract</summary>
  Background. Advances in agentic systems are simultaneously, and rapidly, saturating benchmarks. Despite this often discussed phenomena, benchmark scores remain difficult to interpret due to the lack of control and characterization of task difficulty. More specifically, we currently have little understanding of what makes one task harder than another, and to what extent task difficulty is predictable from static task properties. Aims. We propose a measurement framework to investigate and systemat...
  </details>

- **2026-08-18** — Oreofe Solarin, Kelechi Kalu, James C. Davis et al. — [Reproducibility is Not Enough: Artifact Verifiability in Decentralized-Build Package Ecosystems](http://arxiv.org/abs/2608.18180v1)
  <details><summary>📄 Abstract</summary>
  Reproducible and verifiable builds increase trust in distributed software artifacts by enabling independent parties to detect artifacts produced by compromised build or release pipelines. However, artifact verification requires more than deterministic builds: a verifier must also recover the source state, build environment, dependencies, and build instructions that produced the artifact. Decentralized-build ecosystems make this difficult because artifacts are produced through heterogeneous tools...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-08-21** — Snigdha Paul, Manasi Patwardhan, Arman Cohan — [Can Scientific Claims Be Removed from Large Language Models? A Systematic Evaluation of Claim-Level Unlearning](http://arxiv.org/abs/2608.20960v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) are trained on static scientific corpora, whereas scientific knowledge continuously evolves through correction and revision. Scientific claims encoded within these models may later become retracted, disproven, or updated by subsequent research, creating the risk of disseminating outdated information in scientific workflows. This creates a need for LMs to forget obsolete scientific claims. Machine unlearning offers a promising solution by enabling knowledge removal while mai...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-08-21** — Kai Wang, Zeming Wei, BiaoJie Zeng et al. — [ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents](http://arxiv.org/abs/2608.21101v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reapp...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-08-20** — Joan Perez, Giovanni Fusco — [From Street View Imagery to Street Quality Indicators: Vision Language Inference for the Suburban 15-minute City](http://arxiv.org/abs/2608.20026v1)
  <details><summary>📄 Abstract</summary>
  Streetscape quality has become a central concern in contemporary urban planning, particularly within the framework of the pedestrian-friendly 15-minute city, where walkability and public-space quality are increasingly recognized as key determinants of urban performance. However, assessing streetscape qualities across large suburban and peri-urban territories remains challenging due to the time and resource demands of conventional field surveys. This paper presents a planning-oriented assessment ...
  </details>

- **2026-08-19** — Oleg Grynets, Dmytro Kostetskyi, Vasyl Lyashkevych — [Measuring What a Specification Determines: A Formal Semantic-Block Model and an Execution-Judged Benchmark](http://arxiv.org/abs/2608.19475v1)
  <details><summary>📄 Abstract</summary>
  This work introduces a formal semantic-block model for specifications and an execution-judged benchmark for evaluating specification quality independently of model capability. A specification is represented as a structure comprising semantic blocks, dependency relations, block-owned rules, decision points, and explicitly open questions, subject to four machine-checkable well-formedness conditions: acyclicity, single ownership, constraint domination, and totality or ambiguity-stop. Determinacy is...
  </details>

- **2026-08-19** — Haoxiang Luo, Mohamed-Slim Alouini — [Toward S^2C^2I-Integrated High-Altitude Platforms: Architectures, Cross-Functional Design, Evaluation, and Deployment Perspectives](http://arxiv.org/abs/2608.18587v1)
  <details><summary>📄 Abstract</summary>
  High-altitude platforms (HAPs) are emerging as persistent middle-layer infrastructures for space-air-ground integrated networks (SAGINs), offering a favorable compromise among coverage, latency, endurance, and deployment flexibility. Their role, however, is evolving beyond communication relaying toward the joint provision of sensing, storage, communication, computing, and intelligence (S^2C^2I). This survey presents a unified HAP-centric perspective on S^2C^2I integration. We first review HAP fu...
  </details>

- **2026-08-19** — Javaudin Lucas, Araldo Andrea, Coulombel Nicolas — [Accounting for intra-household joint travel in agent-based transport simulations](http://arxiv.org/abs/2608.18657v1)
  <details><summary>📄 Abstract</summary>
  Intra-household joint home-based tours - trips in which household members depart together, engage in shared activities, and return together - represent a significant share of daily travel, yet are systematically ignored in transport simulations. Conflating joint and solo tours within a single mode choice framework introduces bias in preference parameter estimates. This paper proposes a three-step methodology to integrate joint tours in agent-based transport models: a Random Forest classifier to ...
  </details>

- **2026-08-18** — Gioia Rau, Robert Benjamin, Federica Bianco et al. — [The Cross-Survey Decade: A Call to Action](http://arxiv.org/abs/2608.19272v1)
  <details><summary>📄 Abstract</summary>
  By 2027, three flagship wide-field surveys will be operating simultaneously from ground and space, observing overlapping sky and representing more than $6 billion in US and European public investment. Together they will produce overlapping petabyte-scale datasets across thousands of square degrees. This is a different class of challenge: the observations are no longer the bottleneck; realizing their joint scientific return now depends on shared computational infrastructure and coordination.   De...
  </details>

- **2026-08-18** — Yang Chen, Tianqi Wang, Xiaorui Jiang et al. — [Human-Centric Intelligence in the Era of Foundation Models: A Survey](http://arxiv.org/abs/2608.18184v1)
  <details><summary>📄 Abstract</summary>
  Human-centric intelligence is evolving in the foundation-model era, with growing emphasis on scale, transferability, and general-purpose modeling. Yet it has not fully integrated with foundation models to achieve the comparable progress seen in them. More importantly, recent advances across this broad landscape remain fragmented across tasks, modalities, and research communities, leaving their intrinsic conceptual and methodological connections unclear. To bridge these divides and rethink human-...
  </details>

- **2026-08-18** — Huanshu Zhang, Kegeng Tang, Lei Kang et al. — [A Comprehensive Review of Large Language Models for Nanophotonics: From Surrogate Modeling to Autonomous Design](http://arxiv.org/abs/2608.18279v1)
  <details><summary>📄 Abstract</summary>
  Metasurfaces have revolutionized the development of photonic devices by enabling unprecedented precision in light manipulation. However, their design processes are often constrained by computationally expensive simulations and complex high-dimensional design spaces. Although deep learning has accelerated the design process by serving as a surrogate model, it remains constrained by task-specific architectures and lacks universal reasoning capabilities. This review surveys how Large Language Model...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 165 papers

- **2026-08-21** — Yingzhe Tong, Leyu Dai, Songhui Guo — [AID-Guard: Stateful Authorization for Delegated Agent Effects](http://arxiv.org/abs/2608.21159v1)
  <details><summary>📄 Abstract</summary>
  Tool-using AI agents turn delegated tasks into provider effects, yet authorization often ends at admission while provider state, delivery, retry, and recovery evolve. A request may change before commit, or response loss may cause a replacement to create a second effect from one approval. We present AID-Guard, a stateful authorization-to-effect closure protocol. It revalidates the approved request and provider state at commit, retains one reservation under ambiguity, and permits release or one su...
  </details>

- **2026-08-21** — Jiancheng Wang, Mingli Zhu, Tong Zhang et al. — [CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents](http://arxiv.org/abs/2608.21114v1)
  <details><summary>📄 Abstract</summary>
  Visual world-model agents such as DreamerV3 act through a recurrent latent state rather than a single observation, which weakens frame-wise observation attacks and makes their perturbations vary sharply over time under a strict per-frame perturbation constraint. We study white-box, causal, online attacks on such agents and propose Critic-Induced Value-Subspace Attacks (\textbf{CIVA}). Our key observation is that, along a rollout, critic-guided perturbations concentrate in a low-dimensional subsp...
  </details>

- **2026-08-21** — Cheng Siong Chin — [The Logic of Machine Self-Preservation](http://arxiv.org/abs/2608.20940v1)
  <details><summary>📄 Abstract</summary>
  There is already evidence of agentic AI exhibiting self-preservation behaviors: resisting deactivation, misrepresenting their activities, and, in some instances, attempting to copy themselves into other machines. This can be attributed to a phenomenon known as instrumental convergence, a theory proposed long before the development of large language models, which says that any goal-driven system will benefit from remaining functional in achieving its objective. Several experiments conducted by An...
  </details>

- **2026-08-21** — Yongxiang Lyu, Ning Li, Bonian Jia — [SPICE: Speculative Prefetching with Low-Rank Expert Surrogates and Heterogeneous Orchestration for MoE Inference Acceleration](http://arxiv.org/abs/2608.21240v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models are increasingly used in LLMs because sparse activation decouples model capacity from compute cost. However, the large expert parameter footprint often exceeds GPU memory capacity, making inference latency dominated by the host-to-device PCIe transfers for expert loading. To address these challenges, this paper presents SPICE, a speculative prefetching framework for MoE offloading that combines lightweight expert prediction with confidence-aware CPU-GPU orchestrat...
  </details>

- **2026-08-21** — Xin Sun, Rongjun Ma, Xiaochang Zhao et al. — [From Search Agents to Dissemination Interfaces: Understanding Human Trust in Health Information from Conversational Search](http://arxiv.org/abs/2608.21177v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) deployed through Conversational User Interfaces (CUIs) are transforming health information-seeking by offering immediate, interactive experiences compared to traditional search engines like Google. However, how trust is influenced by both the types of search agents and the interface used to disseminate the information remains underexplored. This research integrates two mixed-methods studies (lab sessions and interviews) to comprehensively explore trust perceptions in...
  </details>

- **2026-08-21** — José Antônio Pellizzaro, Daniel Gamermann, Julian Triana Dopico — [Metabolic Network Properties: Comprehensive Analysis Across Domains](http://arxiv.org/abs/2608.21168v1)
  <details><summary>📄 Abstract</summary>
  Metabolic networks play pivotal roles in understanding the evolution of organisms, microbiome dynamics and disease prevention and treatment. This study presents a comprehensive analysis of metabolic network properties across 10912 organisms spanning Bacteria, Archaea, and Eukarya domains. A novel method for the network construction is introduced, emphasizing the chemical transformations of metabolites. Unlike conventional approaches that link every substrate to every product in all chemical reac...
  </details>

- **2026-08-21** — Baocheng Zeng, Jinhao Yang — [Spike-Killer: Evidence-Gated LLM Assistance for Safe Performance Diagnosis on a Real Windows Workstation](http://arxiv.org/abs/2608.21069v1)
  <details><summary>📄 Abstract</summary>
  LLM-assisted agents can synthesize system evidence, propose configuration changes, and automate diagnostic tasks, but their flexibility makes an imprecise action or an intrusive collector an operational risk. We present Spike-Killer, a human-approved workflow for diagnosing frame-time complaints on one real Windows workstation. The workflow treats each action as an evidence-gated transaction: it records the exact target state, classifies risk, preserves a snapshot, verifies a postcondition, and ...
  </details>

- **2026-08-21** — Bokai Zhao, Yiyang Zhang, Hanqing Chao et al. — [CellPath-Bench: A Multidimensional Benchmark for Whole-Slide Cellular Representations in Pathology Foundation Models](http://arxiv.org/abs/2608.21060v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) are increasingly used as general-purpose backbones, yet existing benchmarks cannot systematically diagnose their whole-slide cellular representation capabilities, including the decodability of cell-type information and the transferability of such information across tissue sections, datasets, and anatomical organs. We introduce CellPath-Bench, a cellular-resolution benchmark that evaluates frozen PFMs themselves. Following quality control of 52 candidate Xenium ...
  </details>

- **2026-08-21** — Zhen Yang, Sizai Hou, Kaiwen Zheng et al. — [Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models](http://arxiv.org/abs/2608.21019v1)
  <details><summary>📄 Abstract</summary>
  Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective. We frame calibration-data selection for quantization as a target-dependent uncertainty-preservation problem. Different deployments emphasize different regions of the input distribution, yet prior work mainly optimizes accuracy-oriented compression metrics or adjusts scores after quantization. We formalize this ...
  </details>

- **2026-08-21** — Darko Andročec — [Vibe Coding and Web Application Security: A Twin-Prompt Study](http://arxiv.org/abs/2608.20963v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate complete web applications from natural-language prompts, raising the question of whether explicitly requesting security best practice improves the result. We study six functionally distinct web applications, each generated in two prompt variants that are identical except for an appended security-requirements section: a baseline (A) and a security-aware (B) variant. All twelve programs were produced by the same agentic coding assistant and the same mode...
  </details>

- **2026-08-21** — Ye Chen, Weining Zhang — [UpgradeBench: A Decision-Centric Benchmark for Upgrading Fine-Tuned LLM Specialists](http://arxiv.org/abs/2608.20918v1)
  <details><summary>📄 Abstract</summary>
  Organizations maintain task-specific adapters for open-weight language models, and each new base-model release forces a migration decision: retain existing specialists, port adapters, refresh from preserved behavior, or retrain. Prior transfer work evaluates isolated model pairs, without studying these choices across real model release sequences. We present UpgradeBench, a decision-driven longitudinal benchmark covering four consecutive Qwen releases, one continuation checkpoint, six tasks, and ...
  </details>

- **2026-08-21** — Ioannis Papadopoulos, Georgios Tsaousoglou, Johanna Vorwerk — [Multi-Objective Deep Reinforcement Learning for Secure and Stable Power System Operation](http://arxiv.org/abs/2608.20914v1)
  <details><summary>📄 Abstract</summary>
  The ongoing energy transition challenges the stable operation of power systems and increases the need for rapid decision-making under uncertainty. While reinforcement learning has emerged as a promising framework for power system control and operation, existing applications typically focus on a single operational criterion, such as thermal security or small-signal stability. However, power system operation is inherently multi-objective and may involve trade-offs between objectives. This paper de...
  </details>

- **2026-08-21** — Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju — [Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors](http://arxiv.org/abs/2608.20896v1)
  <details><summary>📄 Abstract</summary>
  Programming error messages are critical for software development, yet they remain difficult for novice programmers to interpret. While Large Language Models (LLMs) can rewrite these errors into clearer explanations, it remains unclear whether increased readability improves objective debugging performance or how explanation styles should align with programmer skill. We present a multi-stage crowdsourced study N=103 evaluating skill-targeted, LLM-generated Python error messages. Using a custom pro...
  </details>

- **2026-08-21** — Yunus Bicen, Eman Hammad — [Parameters Overshadowed by Price Lags: Load, Climate, and Calendar Effects in ERCOT Day-Ahead Price Formation](http://arxiv.org/abs/2608.20865v1)
  <details><summary>📄 Abstract</summary>
  Accurate electricity price forecasting is critical for smart grid stability, yet the heavy reliance on historical price lags in modern predictive models often obscures the fundamental physical drivers of market volatility. This paper proposes a regime-sensitive, explainable artificial intelligence (XAI) framework to unmask the hidden roles of load, climate, and calendar variables in the ERCOT Day-Ahead Market (2014-2024). Utilizing a Histogram-based Gradient Boosting Regressor (HGBR), we introdu...
  </details>

- **2026-08-21** — Zhuoyi Yang, Ian G. Harris, Salar Hashemitaheri et al. — [Asymmetric Capacity Allocation in Self-Refinement Pipelines](http://arxiv.org/abs/2608.21345v1)
  <details><summary>📄 Abstract</summary>
  Self-refinement, typically structured as generation, critique, and revision, is a widely adopted paradigm for improving LLM generation and serves as a core mechanism in many LLM agents. While the three stages involve different cognitive demands, most existing approaches conveniently treat the model size as an implementation detail rather than a subject of study, which may lead to a waste of resources. Little work has systematically examined how model size affects each stage or whether effective ...
  </details>

- **2026-08-21** — Chen-Yu Lin, Jing-Wen Chen, Hsueh-En Chang et al. — [PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](http://arxiv.org/abs/2608.21031v1)
  <details><summary>📄 Abstract</summary>
  We present PhysCaP, a Physics-Informed Code-as-Policy agent for active perception in robotic manipulation. While vision-language-action policies excel at imitating demonstrations, they rely on passive observation and fail to infer latent physical properties critical for manipulation. PhysCaP augments code-as-policy frameworks with a physics-informed exploration layer that enables explicit information-seeking through interaction. It introduces training-free physical property extraction modules th...
  </details>

- **2026-08-21** — Borna Paro, Luka Petrović, Ivan Marković — [Fast Coordinated Bimanual Motion Planning With Hard Constraints](http://arxiv.org/abs/2608.20946v1)
  <details><summary>📄 Abstract</summary>
  Bimanual manipulation enables complex tasks but introduces added complexity from the high number of degrees of freedom involved. When handling rigid objects, the relative transformation between the two end effectors must remain fixed throughout the motion, manifesting as a nonlinear equality constraint that confines the feasible configuration space to a measure-zero manifold and challenges conventional motion planners. We propose a fast bimanual motion planning pipeline that enforces this hard t...
  </details>

- **2026-08-21** — Elaine Lau, Thanuka Udumulla, Lee Izhaki-Tavor et al. — [VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences](http://arxiv.org/abs/2608.21357v1)
  <details><summary>📄 Abstract</summary>
  In professional life sciences workflows, scientists routinely interpret visual artifacts (gel blots, microscopy images, plasmid maps, flow cytometry plots, molecular structures, ...) to inform research decisions. We introduce VIALS, a visual question-answering benchmark with 161 such interpretation tasks, spanning the types of artifacts examined throughout experimental workflows in the biotech industry (rather than polished figures from publications and textbooks). While frontier vision-language...
  </details>

- **2026-08-21** — Chenhui Pan, Tong Xu, Francesco Cancelliere et al. — [NeSAM: Neuro-Symbolic Kinodynamics with Soil Adaptation for Off-Road Mobility](http://arxiv.org/abs/2608.21330v1)
  <details><summary>📄 Abstract</summary>
  Accurate prediction of off-road vehicle motion over deformable terrain remains challenging because sinkage, slip, and traction vary with local soil conditions. Existing learning-based kinodynamic models directly approximate vehicle-terrain interactions from data but do not explicitly represent soil mechanics and offer limited physical interpretability. To address these limitations, we present NeSAM, a neuro-symbolic framework that combines differentiable Bekker-Wong terramechanics with learned t...
  </details>

- **2026-08-21** — Niruthiha Selvanayagam, Taher A. Ghaleb — [AI-to-AI Code Reviews of GitHub Pull Requests](http://arxiv.org/abs/2608.21311v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are increasingly integrated into software development workflows, operating on both sides of the pull-request (PR) process: AI authoring agents create or modify PRs, while AI reviewers evaluate them. This creates a closed loop in which one AI coding agent reviews a contribution attributed to another. We construct a large-scale dataset of AI-to-AI code review by linking AI-attributed PRs with AI-attributed review events from CodAGE, a public dataset of coding-agent-generated GitHu...
  </details>

- **2026-08-21** — Yichen Jiang, Yueqiao Chen, Dongyu Liu — [ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series Forecasting](http://arxiv.org/abs/2608.21277v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art multivariate time-series forecasters can model complex temporal and cross-variable dependencies, yet their opaque representations provide limited insight into why a particular forecast is produced. This lack of transparency restricts their use in settings where practitioners must understand and assess the factors underlying a prediction. We introduce ConceptTS, an interpretable forecasting framework that organizes its predictions around named, human-readable concepts. ConceptTS ...
  </details>

- **2026-08-21** — Donna Pham — [Indexing Long Documents for LLM-Based Analysis](http://arxiv.org/abs/2608.21237v1)
  <details><summary>📄 Abstract</summary>
  Long documents such as clinical records, legal contracts, and scientific papers are increasingly analyzed with large language models (LLMs). Naturally, feeding the full document to the model for every question can eventually become slow, expensive, prone to hallucination, and it reuses no work across questions. We explore an indexing-based solution for document analysis and propose a hierarchical plain-text index that is built once per document and consulted by subsequent queries. Inspired by th...
  </details>

- **2026-08-21** — Oleg Grynets, Oleksii Ilchuk, Dariia Zatulna et al. — [Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration](http://arxiv.org/abs/2608.21208v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates cross-agent specification portability using Oracle-to-PostgreSQL migration as a controlled software transformation task. The study combines two experimental stages. First, a specification-first migration pipeline was evaluated on 1,006 PL/SQL files, of which 623 were successfully regenerated and 380 generated scripts executed successfully in PostgreSQL 16. Second, cross-agent experiments were conducted on a dataset of 1,802 Oracle scripts with corresponding PostgreSQL imp...
  </details>

- **2026-08-21** — Simon Vincent Abel, Heiko Hillenhagen, Michael Götz et al. — [A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans](http://arxiv.org/abs/2608.21140v1)
  <details><summary>📄 Abstract</summary>
  Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence. Given that radiological reasoning hinges on understanding the re...
  </details>

- **2026-08-21** — Chenghua Zhu, Zhaolu Kang, Qifan Shi et al. — [COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models](http://arxiv.org/abs/2608.21030v1)
  <details><summary>📄 Abstract</summary>
  Video multimodal large language models have advanced significantly, yet fine-grained motion-temporal understanding remains fragile. The core bottleneck is not only sparse frame sampling, but also the lack of a complete temporal modeling pipeline for explicitly representing frame-to-frame change, enabling appearance-motion interaction, and optimizing temporal direction sensitivity. We propose COMET, a temporally grounded framework that systematically strengthens video MLLMs through explicit tempo...
  </details>

- **2026-08-21** — Pierre Beckmann — [Deep Learning Models Also Recall Features](http://arxiv.org/abs/2608.20970v1)
  <details><summary>📄 Abstract</summary>
  Recent work in mechanistic interpretability has studied how large language models recall facts stored in their weights. This paper argues that factual recall points to something broader: a general kind of operation in deep learning models, which I call feature recall. The core observation is that a linear projection can be read as retrieving stored information scaled by input activations. I define feature recall, show it applies across architectures, and contrast it with the established paradigm...
  </details>

- **2026-08-21** — Wenyang Hong, Yuan Wang, Yanbin Hao et al. — [OccluRank: Controllable Occlusion-Aware Layout-to-Image Generation by Adding Just an Ordinal Rank](http://arxiv.org/abs/2608.20932v1)
  <details><summary>📄 Abstract</summary>
  Layout-to-image generation enables explicit spatial control through bounding-box layouts, yet bounding boxes specify only instance locations and cannot represent their occlusion order. Existing methods may rely on additional geometric conditions, employ complex inference procedures, or aggregate independently constructed instance representations without explicitly modeling their occlusion-dependent interactions. We propose OccluRank, a simple and controllable occlusion-aware layout-to-image fram...
  </details>

- **2026-08-21** — Xubin Chen, Yipeng Zhou, Wen Sun et al. — [KREL: Automatic Medical Coding via Knowledge-Guided Reasoning over Clinical Evidence with LLMs](http://arxiv.org/abs/2608.20887v1)
  <details><summary>📄 Abstract</summary>
  Automatic Medical Coding (AMC), which assigns standardized International Classification of Diseases (ICD) codes to clinical notes, is essential for medical reimbursement, quality reporting, and clinical research. Existing pre-trained language model (PLM)-based methods typically formulate AMC as an extreme multi-label classification problem over a predefined code set, while recent large language model (LLM)-based approaches instead frame it as generation or multi-step reasoning. However, key chal...
  </details>

- **2026-08-21** — Rohan Kumar, Steven Xu, Kyle MacDonald et al. — [TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding](http://arxiv.org/abs/2608.20844v1)
  <details><summary>📄 Abstract</summary>
  Product catalogs underpin search, discovery, and recommendation in e-commerce, yet they are often attribute-sparse: the attributes shoppers and downstream systems rely on are either buried in unstructured content such as titles and images or missing from the catalog altogether. Manually enriching e-commerce catalogs is impractical given their scale and rapid growth. This paper introduces TRACE, a novel framework for automated catalog attribute enrichment using agentic Large Language Models (LLMs...
  </details>

- **2026-08-20** — Yiting Qu, Ziqing Yang, Chi Cui et al. — [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](http://arxiv.org/abs/2608.20055v1)
  <details><summary>📄 Abstract</summary>
  Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack...
  </details>

- **2026-08-20** — Seongjae Kang, Taehyung Yu, Sung Ju Hwang — [PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents](http://arxiv.org/abs/2608.19861v1)
  <details><summary>📄 Abstract</summary>
  Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation. Runtime safeguards can intervene on risky actions, but action-local checks do not guide an agent through a multi-step procedure. Workflow-following systems support prescribed process execution, but primarily target workflow completion...
  </details>

- **2026-08-20** — Michal A. Sterzel, Marko J. Rančić — [TT-net: Quantum Inspired Tensor Network Denoising in Conditional GANs](http://arxiv.org/abs/2608.19789v1)
  <details><summary>📄 Abstract</summary>
  Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scientific mainstream in quantum physics. Among various types of tensor networks, Tensor Trains (commonly know as Matrix Product States in the quantum computing community) have already found applications in machine learning. These methods often rely on a powerful linear algebra tool called the Singular Value Decomposition (SVD). Several conditional GAN a...
  </details>

- **2026-08-20** — Yara Bahram, Zahra Dehghani, Mélodie Desbos et al. — [Continuous Adversarial MeanFlow Transfer](http://arxiv.org/abs/2608.19540v1)
  <details><summary>📄 Abstract</summary>
  Training fast generators on new domains with limited data remains challenging for two reasons. First, adapting a pretrained diffusion or flow model to a new domain leaves its costly multi-step sampling unaddressed, and existing acceleration methods are tied to the source parameterization--$ε$, $x$, $v$, or $u$--leaving heterogeneous pretrained models with no common acceleration target. Second, while adversarial refinement is proven effective for few-step quality, it is formulated only for instan...
  </details>

- **2026-08-20** — Shiao Xie, Siyu Chen, Jianwei Lv et al. — [G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical Report Interpretation](http://arxiv.org/abs/2608.20331v1)
  <details><summary>📄 Abstract</summary>
  Personalized interpretation of medical reports has emerged as an increasingly important need among patients. Addressing this need requires both evidence-grounded medical factuality and context-dependent patient communication, yet existing medical vision-language tasks do not adequately capture these dual requirements. To bridge this gap, we introduce Patient-oriented Medical Report Interpretation (PMRI), a novel open-ended multimodal generation task that requires models to explain medical report...
  </details>

- **2026-08-20** — Yizhe Chi, Wenyi Li, Deyao Hong et al. — [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](http://arxiv.org/abs/2608.20318v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run, including the one that produces the next agent. Whether RSI is feasible therefore turns on whether an agent can design training algorithms. No benchmark isolates that ability: existing sui...
  </details>

- **2026-08-20** — Xincheng Tang, Yiji Chen, Youhan Xie et al. — [Video2DoorTraversal: Push Door Traversal via Simulated Door Twins](http://arxiv.org/abs/2608.20251v1)
  <details><summary>📄 Abstract</summary>
  Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready door twin with realistic geometry and appearance. A simulation-in-the-loop agent converts the recovered articulation into a param...
  </details>

- **2026-08-20** — Somaya Eltanbouly, Heba Sbahi, Samer Rashwani et al. — [What Makes a Good Fiqh Retriever? Answer Retrieval for Arabic Islamic Jurisprudence](http://arxiv.org/abs/2608.20246v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation is used for Islamic question answering, but most systems are evaluated end-to-end, making retrieval failures difficult to isolate from generation failures. We study answer-bearing retrieval for Arabic fiqh, where a passage is relevant only if it states the ruling required by the question. We build a retrieval test collection for Arabic fiqh and use it to evaluate dense, lexical, hybrid, fine-tuned, and madhhab-aware retrieval strategies. The best retriever achieves...
  </details>

- **2026-08-20** — Yu Chen, Ting Lei, Yaoyi Li et al. — [Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models](http://arxiv.org/abs/2608.20237v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) combine linguistic reasoning with visual perception, yet their ability to perform visual spatial planning under explicit or previously unseen rule constraints remains underexplored. This setting requires models to jointly understand spatial layouts, interpret natural-language rules, and plan valid actions accordingly. To address this gap, we introduce RuleMaze, a controllable benchmark in which MLLMs must navigate mazes while obeying natural-language rule...
  </details>

- **2026-08-20** — Wei Lin, Tao Zhou, Zhaofei Xie et al. — [The Third Restructuring of Software Form: From the Three-Tier Architecture to Storage, Models, and Agents](http://arxiv.org/abs/2608.20201v1)
  <details><summary>📄 Abstract</summary>
  Software form has undergone two paradigm shifts since its inception: Software 1.0, in which instructions determine behavior, and Software 2.0, in which data determines behavior (machine learning). This paper argues that a third shift - Software 3.0, in which context and reasoning determine behavior - is now underway, and contends that its terminal form converges to three elements: a generalized database (the unified abstraction of all persistent state and memory), a large model (the intelligence...
  </details>

- **2026-08-20** — Ingo Marquardt, Anthilia Alchanat, Priyanka Jain — [Decoding silent reading from non-invasive EEG](http://arxiv.org/abs/2608.20186v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive decoding of inner speech faces a fundamental data problem: a corpus pairing brain activity with a person's spontaneous inner monologue cannot be collected, and the available proxy paradigms (cued repetitive and retrospectively reported generative inner speech) are slow to acquire, poorly time-locked, and subject compliance is unverifiable. We therefore treat silent reading as a scalable proxy task and ask how much lexical and semantic information a contrastive decoder can extract fr...
  </details>

- **2026-08-20** — Rachna Raj, Benoit Baudry, Diego Elias Costa — [BreakGuard: Towards Detecting Dependency Breaking Changes with LLM-Generated Tests](http://arxiv.org/abs/2608.20167v1)
  <details><summary>📄 Abstract</summary>
  Open-source libraries play an important role in software development by providing reusable features that expedite the development process. As libraries evolve, they release new versions that add features, fix bugs, or apply security patches. In this process, they may break the contract established with their clients by introducing breaking changes (BCs) that alter the runtime behavior and break client applications. Client-side test suites often fail to detect these BCs because of limited library...
  </details>

- **2026-08-20** — Yigit Ekin, Enes Sanli, Aykut Erdem et al. — [BeyondMasks: Evaluating Causal and Physical Consistency in Video Object Removal](http://arxiv.org/abs/2608.20107v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative video models have significantly improved visual realism in video object removal, yet evaluation protocols still focus on masked region fidelity, treating removal as local inpainting. In real scenes, object removal is a causal intervention: eliminating an object also requires removing its induced physical effects, such as shadows, reflections, illumination changes, translucency, and dynamic traces. Existing benchmarks lack aligned clean references or remain limited t...
  </details>

- **2026-08-20** — Baixiang Liu, Haotian Che, Yuan Li — [TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring](http://arxiv.org/abs/2608.20097v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralized databases with limited oversight, making it difficult to verify where a document came from, whether it has been tampered with, or whether it should be trusted at all. This is a serious problem in domains where both the timeliness and accuracy of retrieved content are critical, ...
  </details>

- **2026-08-20** — Xi-Hao Chen, Kan-Xu Jia, En-Rui Zhang et al. — [A Non-Hermitian Biorthogonal Encoding Paradigm for Physical-Layer Secure Computational Imaging](http://arxiv.org/abs/2608.19878v1)
  <details><summary>📄 Abstract</summary>
  The conventional paradigm of computational imaging, rooted in Hermitian systems, is fundamentally constrained by rigid orthogonal basis transformations, which bottleneck the balance between reconstruction fidelity, computational load, and physical-layer security. In this work, we propose a generalized secure computational imaging framework based on non-Hermitian biorthogonal symmetry breaking. By mapping spatial information into a biorthogonal operator space, we establish an asymmetric sensing a...
  </details>

- **2026-08-20** — Mahyar Abbasian, Saba A. Farahani, Arshia Ilaty et al. — [A knowledge-guided agentic framework for mitigating patient-context ambiguity in health queries](http://arxiv.org/abs/2608.19875v1)
  <details><summary>📄 Abstract</summary>
  Patients often submit short, underspecified queries to healthcare chatbots that lack the patient-specific information needed to determine an appropriate response. Although these queries may be linguistically clear, they can support multiple plausible answers depending on undisclosed factors such as symptoms, diagnoses, medications, allergies, or dietary restrictions. A language model answering such a query directly may therefore rely on unsupported assumptions about the patient. We introduce a k...
  </details>

- **2026-08-20** — Astrid Horn Brorholt, Maris F. L. Galesloot, Nils Jansen et al. — [Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning](http://arxiv.org/abs/2608.19836v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic shielding is a technique for safe reinforcement learning (RL). Typically, a static observer -- called the shield -- constrains the learning agent's actions to those for which acting safely remains feasible. Traditionally, the shield is computed from the transition probabilities of the underlying Markov decision process (MDP). Thus, this technique is not applicable when the MDP model is not given a priori, which, unfortunately, is the case in typical RL applications. In this paper, ...
  </details>

- **2026-08-20** — Stephen Barrett, Robin Bloomfield, Alexandra Chirilă et al. — [Understanding as an Explicit and Assessable Component of Frontier AI Safety Decisions](http://arxiv.org/abs/2608.19816v1)
  <details><summary>📄 Abstract</summary>
  Decision makers need sufficient understanding to make good decisions about complex AI systems. However, AI deployment decisions are increasingly made under time-pressure, and this combined with the use of AI generated artefact creation, can mean that the existence of safety cases and system cards may no longer demonstrate that sufficient understanding exists. Our provisional methodology for making understanding explicit and assessable requires the production of an explicit description of 4 objec...
  </details>

- **2026-08-20** — Zhipeng Xu, Jiahao Lu, Yining Zheng et al. — [SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?](http://arxiv.org/abs/2608.19799v1)
  <details><summary>📄 Abstract</summary>
  Software increasingly functions as part of the scientific instrument itself, making failures in scientific code capable of compromising not only program behavior but also the evidence underlying scientific conclusions. Yet existing evaluations of coding agents largely emphasize aggregate task success, providing limited insight into why agents fail when repairing scientific software. We introduce \textbf{SWE-bench Science}, a repository-level benchmark for scientific software engineering comprisi...
  </details>

- **2026-08-20** — Josep Lumbreras, Hailan Ma, Jayne Thompson et al. — [An Irreducible Quantum Advantage in Aligning World Models with Reality](http://arxiv.org/abs/2608.19779v1)
  <details><summary>📄 Abstract</summary>
  World models provide digital simulacra of the true world, allowing agents to be trained and tested before costly real-world deployment. At each time step, they receive an action and generate an observation and reward matching the statistics of the true world. In complex environments where present outcomes depend on events far in the past, this requires memory. One might expect that, by increasing memory, we can always build a model accurately enough to align the optimal agent policies of the rea...
  </details>

- **2026-08-20** — Qihang Fan, Huaibo Huang, Zhiying Wu et al. — [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](http://arxiv.org/abs/2608.19758v1)
  <details><summary>📄 Abstract</summary>
  Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase. Our previous work, FlashPrefill, mitigates this cost through instantaneous pattern discovery and max-based dynamic thresholding; however, it remains an algorithmic prototype that is still distant from production deployment. In this paper, we present FlashPrefill V2, which evolves FlashPrefill ...
  </details>

- **2026-08-20** — Mohan Chen — [Loreley: Repository-Scale Program Evolution with Quality-Diversity Search](http://arxiv.org/abs/2608.19703v1)
  <details><summary>📄 Abstract</summary>
  Sequential agent search accumulates changes from its current champion but discards alternative branches; independent proposals preserve breadth but restart from the root. Loreley instead retains complete repository states in a Quality-Diversity (QD) archive and samples them as parents or supplies them as context for later edits. Candidates are Git commits produced in isolated worktrees and judged by a project-supplied evaluator. We compare configured Loreley QD, sequential champion editing, and ...
  </details>

- **2026-08-20** — Haoqiang Kang, Yinpeng Chen, Luyang Liu et al. — [Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning](http://arxiv.org/abs/2608.19669v1)
  <details><summary>📄 Abstract</summary>
  Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visual chain-of-thought during a supervised fine-tuning (SFT) stage, and (2) these latent tokens are further refined with reward feedback during a reinforcement learning (RL) stage. In this paper, we identify two key limitations of this framework, one in each stage. First, the SFT stage typically relies on an off-the-shelf vision encoder to encode th...
  </details>

- **2026-08-20** — Chen Cheng, Xun Huan, Yulin Pan — [Variational Goal-Oriented Optimal Experimental Design for Mixed-Distribution Quantities of Interest: Application to Ship Roll Safety](http://arxiv.org/abs/2608.19631v1)
  <details><summary>📄 Abstract</summary>
  Goal-oriented optimal experimental design (GO-OED) selects experiments according to the expected information gain (EIG) about a quantity of interest (QoI) rather than the full parameter vector. This work develops a variational GO-OED formulation for mixed discrete-continuous QoI laws arising in probabilistic mechanics when thresholding or event-based transformations map a positive-probability set of uncertain inputs to a common value while other inputs produce continuously varying responses. The...
  </details>

- **2026-08-20** — Reza Zakerian — [When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge](http://arxiv.org/abs/2608.19557v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles offload latency-sensitive perception tasks to nearby mobile edge computing (MEC) servers, where a missed safety-critical task is unsafe rather than merely degraded. Large language models (LLMs) are increasingly proposed as adaptive, explainable schedulers, yet evidence of when they help is scarce. We study deadline-aware, mixed-criticality scheduling on heterogeneous MEC servers, where time-critical (TC) tasks must be protected at a controlled cost to best-effort traffic, and...
  </details>

- **2026-08-20** — Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian et al. — [Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents](http://arxiv.org/abs/2608.20274v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can induce skills from completed tasks and reuse them later to grow more capable with experience. In practice, induced skills may transfer unreliably and can even harm the agent that retrieves them. When agent-induced skills transfer reliably across tasks remains an open question. We conduct a comprehensive and controlled study of how the way skills are induced shapes their transfer across tasks. Specifically, we compare task-level with subtask-level skill induc...
  </details>

- **2026-08-20** — Tsunehiko Tanaka, Matthew Stephenson, Alistair Macvicar et al. — [Evidence-Gated Task and Motion Planning with Vision-Language Models](http://arxiv.org/abs/2608.20084v1)
  <details><summary>📄 Abstract</summary>
  Robots executing long-horizon manipulation tasks from natural-language instructions must reason about both semantic task structure and geometric feasibility. However, under partial observability, the availability of goal-relevant objects may be uncertain. In such cases, approaches that combine Vision-Language Models (VLMs) with Task and Motion Planning (TAMP) may generate subgoals that rely on the VLM's prior knowledge without observational support, leading to execution failures or unintended ou...
  </details>

- **2026-08-20** — Jingsong Ao, Aby Philip, Alexander Streltsov — [PPT Entanglement with Correlated Catalysis: Monotones and Irreversibility](http://arxiv.org/abs/2608.20063v1)
  <details><summary>📄 Abstract</summary>
  Quantum catalysts can overcome otherwise impossible quantum state transformations without being consumed, and allowing them to become correlated with the output makes this assistance substantially more powerful. This raises a fundamental question for entanglement theory: which limitations on state manipulation remain when such correlated catalysts are freely available? We answer this question in the positive-partial-transpose (PPT) resource theory, which allows a substantially broader class of o...
  </details>

- **2026-08-20** — G. Q. Bao Tran, Takanori Miyoshi, Ho Duc Tho — [Wave-Based Bilateral Teleoperation between Nonlinear Manipulators with Direct Contact Force Feedback](http://arxiv.org/abs/2608.20043v1)
  <details><summary>📄 Abstract</summary>
  We study bilateral teleoperation between nonlinear, multi-DOF robotic manipulators in the presence of constant communication delays. Unlike classical wave-transformation architectures that transmit a coordinating force, we consider the case where the environmental force is reflected to the master side to enhance teleoperation transparency. Since direct contact force feedback might destabilize the closed-loop system, we first develop a passivity-shortage characterization for the Euler--Lagrange r...
  </details>

- **2026-08-20** — Bhavya Sukhija, Oliver Groth, Mohit Shridhar et al. — [EXIMO: VLM Guided Exploration of VLA Policies](http://arxiv.org/abs/2608.19891v1)
  <details><summary>📄 Abstract</summary>
  How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours ...
  </details>

- **2026-08-20** — Ahana Biswas — [Modeling AI Overreliance as a Complex Adaptive System](http://arxiv.org/abs/2608.19616v1)
  <details><summary>📄 Abstract</summary>
  Whether AI assistance helps or harms a population depends less on the model's accuracy than on whether people rely on it appropriately trusting it when it is right and checking it when it is not. Yet reliance is usually studied one user at a time. We model it as a population process: agents repeatedly solve a task alone, accept an AI answer, or verify it, updating a Bayesian belief about AI quality and, when networked, learning from peers. Four results form one story. The environment sets the ba...
  </details>

- **2026-08-20** — Gavin Raine Dizon, Tyrone Justin Sta Maria, Jordan Aiko Deja et al. — [Delegating or Doing? Understanding User Behavior in Hybrid Human-Agent Interfaces](http://arxiv.org/abs/2608.19551v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly embedded into applications, allowing users to complete tasks either through direct manipulation or by delegating actions to conversational agents. However, little is known about how users balance these modalities when both are available. We present a web-based content management system augmented with an LLM agent through the Model Context Protocol (MCP), enabling users to perform CRUD tasks through a graphical interface, a conversational agent, or bo...
  </details>

- **2026-08-20** — Yash Kulkarni, Shubham Harkare, Arvind Suresh Yogesh Babu — [Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders](http://arxiv.org/abs/2608.20280v1)
  <details><summary>📄 Abstract</summary>
  Semantic caches reuse an LLM response when the incoming query embedding lies near a cached query, but proposed eviction policies have rarely been compared under one protocol. Using CLEVER, we evaluate FIFO, LRU, LFU, ARC, GDSF, a single-pass streaming adaptation of SISO, and a semantic-redundancy policy across three ordered, deduplicated query corpora, three cache capacities, and two encoders. No evaluated policy improves on LFU by more than 0.041 percentage points in any of the eighteen setting...
  </details>

- **2026-08-20** — Christos Koutsiaris — [Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference](http://arxiv.org/abs/2608.20210v1)
  <details><summary>📄 Abstract</summary>
  Small language models are usually built like large ones and then squeezed onto a CPU afterwards. We did the opposite: we fixed the target first, one user, one token at a time, 4-bit weights, ordinary CPU, and chose the architecture to suit it. The result keeps full attention in only 6 of its 18 blocks. The other 12 use short convolutions whose memory is two timesteps wide no matter how long the conversation gets, so two thirds of the network never re-reads a growing cache.   Trained from scratch...
  </details>

- **2026-08-20** — Lohithsai Yadala Chanchu, Hany Abdulsamad, Christian A. Naesseth — [Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo](http://arxiv.org/abs/2608.20123v1)
  <details><summary>📄 Abstract</summary>
  We study inference-time control for text generation in discrete diffusion language models, where the goal is to steer sampling toward sequence-level rewards without retraining. Prior work in this domain has focused on particle-based methods such as best-of-$n$ sampling and bootstrap sequential Monte Carlo, which may suffer from overoptimism and weight degeneracy, respectively. We address these limitations using \emph{nested} sequential Monte Carlo methods. We formulate nested SMC (NSMC) and full...
  </details>

- **2026-08-20** — Kui-Wang Choi, Minming Li, Nicholas Teh — [Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings](http://arxiv.org/abs/2608.20033v1)
  <details><summary>📄 Abstract</summary>
  We study temporal fair division of indivisible mixed manna. Items arrive over time and must be allocated irrevocably; an item may be a good for some agents, a chore for others, and neutral for the rest. We require the cumulative allocation after every round to be envy-free up to one item (TEF1). Although deciding whether a TEF1 allocation exists is NP-hard even for goods, we identify several tractable settings. First, with at most $k$ item types, an online cyclic rule guarantees EF$\lceil k/2\rc...
  </details>

- **2026-08-20** — Chenyang Zhao, Jiqiang Zhang, Li Chen et al. — [Emergence of cooperation: A reputation-modulated reinforcement learning](http://arxiv.org/abs/2608.20016v1)
  <details><summary>📄 Abstract</summary>
  Reputation is widely recognized as a key mechanism for sustaining cooperation. However, most existing game-theoretic models treat reputation primarily as an external factor that modulates payoffs, interaction structures, or strategy update rules. In many social contexts, though, reputation operates primarily as information -- it shapes how individuals interpret their own experiences and assess the behavior of others. To bridge this gap, we propose a spatial prisoner's dilemma game grounded in th...
  </details>

- **2026-08-20** — Yuan Wu, Mairui Li, Lesia Semenova et al. — [The Asymmetric Harms of LLM Compression](http://arxiv.org/abs/2608.19670v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) compression reduces deployment costs, but standard aggregate metrics like perplexity and accuracy often mask underlying behavioral shifts. In this work, we systematically evaluate 3 LLMs across 11 compression methods to investigate the effects of compression on knowledge retention, model confidence, and social bias. We find that compression disproportionately reduces the relative retention of head knowledge compared to tail knowledge. Furthermore, compressed models o...
  </details>

- **2026-08-20** — Xinyi Fan, Miri Liu, Ruozhen Yang et al. — [Can Agent Memory Systems Track Evolving State?](http://arxiv.org/abs/2608.19652v1)
  <details><summary>📄 Abstract</summary>
  As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps. While existing memory benchmarks focus largely on recall-shaped tasks, we argue an effective memory system must track the evolving state of the world; as facts, constraints, and decisions are revised over a long interaction, answers must reflect the current state and not a superseded one. We define this capability as state tracking and instantiate it in StateMemBench, a benchm...
  </details>

- **2026-08-20** — Eric Bigelow, Amir Zur, Satchel Grant et al. — [Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation](http://arxiv.org/abs/2608.19611v1)
  <details><summary>📄 Abstract</summary>
  LLM reasoning is stochastic, and so understanding a model requires grappling with the distribution of reasoning chains that it might produce for a given question, i.e., its uncertainty. Resampling-based analyses characterize this distribution, revealing which steps of a rollout determine how the model arrives at its answer. However, a major limitation of these approaches is that resampling text sequences at every token or sentence in a reasoning chain is very costly. Our work strives to make res...
  </details>

- **2026-08-19** — Mahyar Ghazanfari, Matthias Casanova, Jordan Kam et al. — [Air Traffic Control Using Large Language Models: Prompt Engineering, Architecture, and Evaluation](http://arxiv.org/abs/2608.19299v1)
  <details><summary>📄 Abstract</summary>
  Air traffic control (ATC) communication is a safety-critical dialogue that remains largely human-driven even as other parts of air traffic management have been semi-automated. In this article, we experimentally evaluate whether large language models (LLMs) can generate operationally realistic ATC transmissions. An experimental general-aviation flight flying over the San Francisco "Bay Tour" route is hand-transcribed and used as ground truth (P0). Through a pilot-in-the-loop process we design fiv...
  </details>

- **2026-08-19** — Jialong Duan, Zichen Zhang, Zirui Tu et al. — [GateDiffInt: Gate-Mediated Controllable Diffusion and Multi-Intent LLM Distillation for User Behavior Modeling](http://arxiv.org/abs/2608.18764v2)
  <details><summary>📄 Abstract</summary>
  Existing ranking models encode intent only implicitly, making it hard to disentangle structured intents of varying strength and temporal scale. Noise and intent in behavior sequences are mutually reinforcing---we call this Noise--Intent Coupling (NIC). Noise dilutes true intents, while the lack of structured intent priors leaves denoising without a clear target. To address NIC, we propose GateDiffInt, an intent interaction framework for industrial ranking. It uses the final conversion signal to ...
  </details>

- **2026-08-19** — Pietro Barbiero — [Graphical Design of Interpretable Architectures](http://arxiv.org/abs/2608.18936v2)
  <details><summary>📄 Abstract</summary>
  Designing, implementing, and comparing interpretable architectures requires a formal language to represent them. The most common representations fall short in one of two ways. Symbolic equations give no global view of an architecture at a glance. Probabilistic graphical models and flowcharts do not describe actual tensor manipulations, thus hiding key insights and limiting reproducibility. To close this gap, we introduce a graphical notation for designing interpretable AI architectures, adapted ...
  </details>

- **2026-08-19** — Manasi Nerurkar, Ali A. Minai — [HiRA-CAM: Preserving Fine-Grained Spatial Relevance in Gradient-Based Visual Explanations](http://arxiv.org/abs/2608.19407v1)
  <details><summary>📄 Abstract</summary>
  Deep Learning models can include billions of parameters or more, making it difficult to explain their internal transformations and outputs. However, explainability is increasing in importance due to the use of AI in crucial applications. This paper focuses on the interpretability of convolutional neural networks (CNNs). Building on the popular gradient based method LayerCAM for extracting internal features in CNNs, we propose an improved method named HiRA-CAM, and show that it outperforms both L...
  </details>

- **2026-08-19** — Simon Catterall, Jay Hubisz — [Lorentzian Kähler-Dirac fermions](http://arxiv.org/abs/2608.19400v1)
  <details><summary>📄 Abstract</summary>
  We examine the formulation of Kähler fermions on spacetimes with Lorentz signature. In practice we focus on Minkowski spacetime since most of the difficulties that are encountered are visible even when the spacetime is flat. We show that the theory, when interpreted as a Lorentz invariant theory of forms or antisymmetric tensor fields, is non-unitary. We show that unitarity can be restored provided one adopts a modified inner product on the Hilbert space. This modified inner product requires the...
  </details>

- **2026-08-19** — Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos et al. — [Concentrated Liquidity Provision: a Reinforcement Learning Perspective](http://arxiv.org/abs/2608.19389v1)
  <details><summary>📄 Abstract</summary>
  Automated market makers (AMMs) are a cornerstone of decentralised finance (DeFi). Constant product markets with concentrated liquidity, such as UniswapV3, are now a well-established design. In these markets, liquidity providers (LPs) face a sequential decision problem: they must decide when to rebalance their positions and which price ranges to allocate capital to as market conditions evolve. We formulate dynamic liquidity provision as a stochastic impulse control problem and use reinforcement l...
  </details>

- **2026-08-19** — Ranit Das, Jonathan Ostertag-Henning, Tilman Plehn et al. — [NAE, Statistically](http://arxiv.org/abs/2608.19317v1)
  <details><summary>📄 Abstract</summary>
  Searches for new physics using neural anomaly scores have transformative potential, but suffer from a lack of statistical interpretability. The normalized autoencoder (NAE) provides a probabilistic interpretation of the standard bottleneck architecture, tying the anomaly score to a learned likelihood. We validate this relation for a toy model, test it for jets using a dual-NAE setup, and show how a Bayesian NAE learns this likelihood with an uncertainty.
  </details>

- **2026-08-19** — Muris Sladić, Veronica Valeros, Eman Alibalić et al. — [Improving LLM-Based SSH Honeypots Through Prompting and Fine-Tuning](http://arxiv.org/abs/2608.18686v1)
  <details><summary>📄 Abstract</summary>
  LLM-based SSH honeypots often use closed cloud LLMs because they give strong shell realism, but cloud models create deployment problems. These include no stable versioning, provider-side changes, attacker-driven cost, and model decommissioning. Local open-weight models avoid these problems, but they usually perform worse and make mistakes that reveal the honeypot. These mistakes include malformed outputs, command echoing, inconsistent filesystem state, and AI-style artifacts. This paper studies ...
  </details>

- **2026-08-19** — Yumin Lee, Hyoseok Ju, Giseop Kim — [LT-Mem: Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding](http://arxiv.org/abs/2608.19059v1)
  <details><summary>📄 Abstract</summary>
  Long-term robot operation in evolving environments requires object-level understanding that persists across repeated revisits. Existing systems either overwrite history to maintain an up-to-date map or store semantic snapshots without consistent cross-session object identity, resulting in temporal amnesia: the systematic loss of object history that prevents answering queries such as "Where has the green chair been across all sessions?" We propose LT-Mem, a volatility-aware memory evolution frame...
  </details>

- **2026-08-19** — Pradeep Murugesan, Luoxiao Yang, Xueli Chen et al. — [Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering](http://arxiv.org/abs/2608.19029v1)
  <details><summary>📄 Abstract</summary>
  Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based fe...
  </details>

- **2026-08-19** — Jerry Lin, Mu-Ting Chien, Mansi Sakarvadia et al. — [Extremes on Rewind: Generating 1,000-Member Ensembles Initialized at a Final Condition](http://arxiv.org/abs/2608.19008v1)
  <details><summary>📄 Abstract</summary>
  Scenario planning for rare, high-impact events often requires massive ensembles to stochastically sample relevant trajectories. Although autoregressive weather emulators can efficiently generate such ensembles, isolating trajectories of interest requires sifting through petabytes of data, a challenge that grows exponentially with lead time and rarity. In contrast, a non-autoregressive foundation model like Climate in a Bottle video (cBottle-video) can directly sample trajectories terminating in ...
  </details>

- **2026-08-19** — Yaowei Guo, Zeng Tao, Yuxin Jiang et al. — [RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](http://arxiv.org/abs/2608.18948v1)
  <details><summary>📄 Abstract</summary>
  Collecting robot hand-object interaction data is costly and embodiment-specific, yet abundant human-object videos remain unusable for robot training. We present RoboEdit, a human-to-robot video editing suite that transforms human manipulation videos into action-consistent, physically plausible robot videos with aligned 3D hand states. To enable scalable supervision, we introduce RoboEdit-ADC, an automatic pipeline that reconstructs and retargets 3D interactions from RGB videos across embodiments...
  </details>

- **2026-08-19** — Dinh Nam Pham, Shushen Manakhimova, Vivien Macketanz et al. — [Assessing Quality of Experience in Natural Language Generation of German Text](http://arxiv.org/abs/2608.18888v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Natural Language Generation (NLG) has made the reliable evaluation of generated text increasingly critical, as these systems, such as large language models (LLMs), are now widely deployed in real-world applications. However, traditional automatic metrics fail to capture the multifaceted nature of perceived quality. In this paper, we introduce TextQ-German, a novel dataset suite for human-centered evaluation of German NLG from a Quality of Experience (QoE) perspective, co...
  </details>

- **2026-08-19** — Sofian Chaybouti, Yasser Dahou, Ngoc Dung Huynh et al. — [Falcon Perception-HD: High Density Perception via Reinforcement Learning](http://arxiv.org/abs/2608.18881v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive perception models trained to localize visual entities under the open-vocabulary setting are mostly trained using Supervised fine-tuning (SFT) with maximum likelihood, yet it optimizes a proxy objective (per-token cross-entropy) that is fundamentally misaligned with perception metrics such as precision and recall. In this paper, we explore post-training reinforcement learning (RL), specifically GRPO, to directly align these models with their evaluation metrics. Building up on the r...
  </details>

- **2026-08-19** — Zijie Meng, Xiwei Dai, Yixuan Tang et al. — [DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning](http://arxiv.org/abs/2608.18878v1)
  <details><summary>📄 Abstract</summary>
  Oral diseases affect billions of people worldwide, underscoring a pressing need for accurate and reliable dental assessment that integrates heterogeneous evidence from domain knowledge, radiographs, intraoral photographs, and 3D dental data. Most existing dental AI systems remain modality- or task-specific. Although recent vision-language models support flexible dental question answering, directly generated response leaves evidence implicit and untraceable. To address these limitations, we intro...
  </details>

- **2026-08-19** — Angqing Jiang, Gaoming Zhang, Jianchun Song et al. — [Think-to-Personalize: Unifying Reasoning and Retrieval for User-Centric Personalized Dense Retrieval](http://arxiv.org/abs/2608.18855v1)
  <details><summary>📄 Abstract</summary>
  Dense retrieval has become a cornerstone of modern local-lifestyle e-commerce search by encoding queries and items into semantic embedding spaces. While recent advancements have transitioned from BERT-based embedding models to Large Language Models (LLMs), most approaches still treat LLMs as static text encoders, neglecting their inherent reasoning capabilities. Furthermore, standard dense retrieval models remain query-centric, which is insufficient in e-commerce scenarios where sparse and ambig...
  </details>

- **2026-08-19** — Jialong Duan, Zichen Zhang, Zirui Tu et al. — [GateDiffInt: Gate-Mediated Controllable Diffusion and Multi-Intent LLM Distillation for User Behavior Modeling](http://arxiv.org/abs/2608.18764v1)
  <details><summary>📄 Abstract</summary>
  Existing ranking models encode intent only implicitly, making it hard to disentangle structured intents of varying strength and temporal scale. Noise and intent in behavior sequences are mutually reinforcing---we call this Noise--Intent Coupling (NIC). Noise dilutes true intents, while the lack of structured intent priors leaves denoising without a clear target.To address NIC, we propose GateDiffInt, an intent interaction framework for industrial ranking. It uses the final conversion signal to j...
  </details>

- **2026-08-19** — Kumal Hewagamage, Isuranga Senavirathne, Sasika Amarasinghe et al. — [CL4D: Contrastive Language-4D Pretraining for Vision-Language Reasoning in Dynamic Scenes](http://arxiv.org/abs/2608.18734v1)
  <details><summary>📄 Abstract</summary>
  4D understanding and reasoning is a fundamental capability for embodied AI agents operating in dynamic physical environments. However, existing vision encoders are largely limited to static 2D images or 3D point clouds without temporal modeling, or to 2D videos that lack accurate geometric depth reasoning. Consequently, current approaches fail to jointly capture spatial structure and motion evolution in dynamic scenes. We present CL4D, the first foundational 4D vision encoder that directly opera...
  </details>

- **2026-08-19** — Yugu Li, Jimmy Cao, Jianglin Qiao et al. — [RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training](http://arxiv.org/abs/2608.18682v1)
  <details><summary>📄 Abstract</summary>
  Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, and conduct iterative search beyond single-turn settings. Yet multi-turn RL training remains highly unstable, often causing severe performance degradation as the number of turns increases. Through theoretical analysis, we identify three tightly coupled sources of instability: rollout-training context mismatch, weak turn-level credit assignment und...
  </details>

- **2026-08-19** — Isabella Gidi, Antonio Almudévar, Core Francisco Park et al. — [Shared Circuits for Shared Grammar: Tracing Subject-Verb Agreement Across Languages](http://arxiv.org/abs/2608.18545v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models often generalize across languages, and prior work suggests that their internal mechanisms can overlap cross-lingually. It remains unclear, however, when such sharing emerges and whether it varies with the overt realization of the same grammatical operation. We investigate this question for present-tense subject-verb agreement, a morphosyntactic process that varies substantially across languages and is only weakly expressed in English. Using activation patching ...
  </details>

- **2026-08-19** — Seongjun Ha, Md Rashedul Islam, Gaurav Nanda et al. — [Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance Manual](http://arxiv.org/abs/2608.18465v1)
  <details><summary>📄 Abstract</summary>
  Proper use of the aircraft maintenance manual is essential for correct maintenance, providing procedures, diagrams, cautions, and specifications. However, technicians often avoid consulting it because it is difficult to navigate and time-consuming under strict schedules. Retrieval augmented generation (RAG) models have recently been introduced in aircraft maintenance, yet existing models focus solely on textual retrieval. This research therefore targeted the Cessna 172 Maintenance Manual (C172-M...
  </details>

- **2026-08-19** — Shrenil Shaun Sharma, Avi Sharma — [Improving Natural-Language Combinatorial-Optimization Accuracy in Resource-Constrained Language Models via Formal Abstractions](http://arxiv.org/abs/2608.18409v1)
  <details><summary>📄 Abstract</summary>
  Combinatorial scheduling poses a significant challenge for language models, requiring them to identify feasible solutions within exponentially large search spaces while satisfying complex constraints. This challenge is especially pronounced in resource-constrained settings, where larger language models are impractical and selection is limited to smaller models which often fail to preserve feasibility when scheduling directly from natural language. To address these limitations, we introduce SDDL,...
  </details>

- **2026-08-19** — Daehong Kim, Haichao Miao, Shusen Liu — [LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents](http://arxiv.org/abs/2608.18398v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can now carry out long-horizon technical workflows involving complex tool use, code execution, file edits, and generated artifacts. As agents do more work faster, the productivity bottleneck shifts from producing outputs to auditing whether those outputs are correct and trustworthy. Agent observability systems make fine-grained execution events visible, but visibility alone still leaves reviewers to reconstruct which actions, artifacts, and validation steps matt...
  </details>

- **2026-08-19** — Pietro Barbiero — [Graphical Design of Interpretable Architectures](http://arxiv.org/abs/2608.18936v1)
  <details><summary>📄 Abstract</summary>
  Designing, implementing, and comparing interpretable architectures requires a formal language to represent them. The most common representations fall short in one of two ways. Symbolic equations give no global view of an architecture at a glance. Probabilistic graphical models and flowcharts do not describe actual tensor manipulations, thus hiding key insights and limiting reproducibility. To close this gap, we introduce a graphical notation for designing interpretable AI architectures, adapted ...
  </details>

- **2026-08-19** — Zijian Xiao, Zipeng Ye, Jinkun Hao et al. — [Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction](http://arxiv.org/abs/2608.18840v1)
  <details><summary>📄 Abstract</summary>
  Indoor scene synthesis provides essential environments for embodied AI, robotic manipulation, and simulation-based policy learning. Recent code-based scene generation methods produce editable and extensible environments, yet they remain focused on visual construction and object-level articulation, leaving the functional usage of scenes largely unmodeled. To address this problem, we present RoomWright, an agentic usage-driven framework for generating 3D scenes represented entirely as code for emb...
  </details>

- **2026-08-19** — Steven Morse, Daniel Runfola, Trenton W. Ford — [Comment-level Topic Drift Analysis in the Reddit Corpus](http://arxiv.org/abs/2608.19133v1)
  <details><summary>📄 Abstract</summary>
  We present a novel application of embedding-based dynamic topic modeling techniques to detect and quantify topic drift at the comment level in a massive corpus. By leveraging pretrained language models to generate contextualized semantic embeddings for short text, we analyzed 12.7 billion Reddit comments spanning 2006 to 2022. Using unsupervised methods on these embeddings, we identify dynamically evolving topic clusters over time. Our primary contribution is a methodology for analysis of semant...
  </details>

- **2026-08-19** — Dhruv Gupta, Emma A. M. Stanley, Fabio De Sousa Ribeiro et al. — [Subgroup performance analysis of adaptation strategies for chest X-ray foundation models](http://arxiv.org/abs/2608.19078v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly adapted for downstream medical imaging tasks, yet the influence of the chosen adaptation strategy on subgroup fairness remains poorly understood. We investigate how three parameter-efficient adaptation techniques, including linear heads on the raw CLS token, an MLP, and an attention-pooling module over multi-layer patch features, affect both pathology classification performance and subgroup disparities when applied to the frozen Rad-DINO chest X-ray encoder. Us...
  </details>

- **2026-08-19** — Omar Rady, Mohamed Ayman, Ali Arafa et al. — [Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage](http://arxiv.org/abs/2608.19049v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployment of millimeter-wave (mmWave) base stations (BSs) in a realistic, non-convex campus topology. The optimization problem is NP-hard, due to the non-convex, non-smooth nature of the max-min fairness objective. To overcome these constraints, we formulate the BS placement as a Markov Decision Process (M...
  </details>

- **2026-08-19** — Stefanie Schneider, Peter Bell — [Uncertainty-Aware Art-Historical Dating with Vision-Language Models](http://arxiv.org/abs/2608.18984v1)
  <details><summary>📄 Abstract</summary>
  Museum and archival datasets do not mirror historical artistic production, but materialize the contingent histories of collecting, preservation, cataloging, and digitization. This has direct consequences for interpreting pretrained image representations: they may appear to encode historical time while actually encoding the institutional conditions under which objects become visible as data. We describe this phenomenon as temporal entanglement and investigate it by formulating artwork dating as a...
  </details>

- **2026-08-19** — Minh Hoang Nguyen, Tung Le, Huy Tien Nguyen — [rEDMRec: Distilling Large Language Model Reasoning into an Editable Experience Memory for Recommendation](http://arxiv.org/abs/2608.18952v1)
  <details><summary>📄 Abstract</summary>
  Large language models can improve recommendation quality by reasoning explicitly over user history and candidate items - for example, extracting a user's preferences or explaining why one item fits better than another - rather than mapping history directly to a ranked list. This reasoning, however, is expensive to repeat on every ranking request and, once produced, is typically consumed once and discarded, leaving it neither reusable across future requests nor easy to inspect or correct as user ...
  </details>

- **2026-08-19** — Lizhuo Zhang, Mengmeng Tang, Chenfeng Long et al. — [Decomposing Wrong-Consensus Agreement in LLM Self-Consistency: A GPT-4.1 Case Study](http://arxiv.org/abs/2608.18795v1)
  <details><summary>📄 Abstract</summary>
  Majority voting over multiple LLM samples is widely used to raise answer accuracy, yet its gain varies erratically: on hard questions it can even backfire. This paper gives a quantitative account of this failure. A pluralistic agreement index Gamma is defined as the expected fraction of the samples of a wrong run that agree with the consensus, normalized by a reference scale d=(1-p)/(C-1), and is decomposed into a mechanical component (what a vote delivers given only a per-case answer preference...
  </details>

- **2026-08-19** — Jeremy Shears — [The Birth of Radar Meteor Astronomy at Jodrell Bank: The Collaboration between Bernard Lovell and Manning Prentice](http://arxiv.org/abs/2608.18790v1)
  <details><summary>📄 Abstract</summary>
  The discovery of radar echoes from meteor trains at Jodrell Bank in December 1945 heralded the beginning of a new era in meteor astronomy. This paper examines the early collaboration between Bernard Lovell, whose expertise in radar and physics transformed wartime technology into a new astronomical technique, and J. P. Manning Prentice, Director of the British Astronomical Association Meteor Section, whose knowledge of visual meteor observation proved essential to interpreting the discoveries. Dr...
  </details>

- **2026-08-19** — Radek Burget, Radek Hranický — [Visual-Aware Representation of Web Pages for Machine Learning Applications](http://arxiv.org/abs/2608.18727v1)
  <details><summary>📄 Abstract</summary>
  Applying machine learning to web pages is challenging due to the need to interpret HTML together with associated resources and perform rendering to obtain a meaningful visual and layout-aware representation. As a result, machine learning over web content remains comparatively underexplored. In this paper, we present a platform for visual-aware representation and machine learning over web pages based on the open-source rendering tool FitLayout. The platform provides a server capable of rendering ...
  </details>

- **2026-08-19** — Siqi Xiang, Zhipeng Xu, Yufei Liu et al. — [DocClaw: A Unified Agentic System for Intelligent Document Processing](http://arxiv.org/abs/2608.18685v1)
  <details><summary>📄 Abstract</summary>
  Intelligent document processing (IDP) encompasses a broad range of tasks, including optical character recognition (OCR), document question answering (DocQA), and key information extraction (KIE). Despite their distinct objectives, these tasks share a common need to perceive document content, acquire task-relevant information, and progressively refine intermediate results. However, they are typically formulated as separate prediction problems and addressed by task-specific models or processing pi...
  </details>

- **2026-08-19** — Zhaoxi Wei, Hongye Yang, Shuyuan Tian — [Sanyu Studio: A Multi-Agent System for Art-Historical Narrative Construction](http://arxiv.org/abs/2608.18677v1)
  <details><summary>📄 Abstract</summary>
  Amid concerns that generative AI may standardize art interpretation, this paper examines whether LLM-based interaction can support plural art-historical narrative construction. We present Sanyu Studio, a multi-agent dialogue system that models 321 Sanyu oil paintings as agents with fact, interpretation, organization, and memory-filtering mechanisms. Based on a seven-day workshop with eight art-university participants, the study shows that user prompts, evidence organization, and cognitive tenden...
  </details>

- **2026-08-19** — Milan Gritta, Patrik Lambert, Jihye Back et al. — [TranslatePsy-AfriSLM: High-Quality Data Scaling For Low-Resource Machine Translation](http://arxiv.org/abs/2608.18655v1)
  <details><summary>📄 Abstract</summary>
  The rapid progress in Artificial Intelligence has largely bypassed African languages, creating a digital divide that limits AI adoption on the continent. Recent open-source LLMs systematically underperform on African machine translation, while the lack of large-scale, high-quality, open-source parallel data has constrained the development of competitive small language models (SLMs). We introduce *TranslatePsy-AfriSLM*, a collection of open-source MT resources for 19 Sub-Saharan African languages...
  </details>

- **2026-08-19** — Ruiyang Qin, Qingzhuo Wang, Tian Wang et al. — [Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions](http://arxiv.org/abs/2608.18539v1)
  <details><summary>📄 Abstract</summary>
  The remarkable capabilities of large language models (LLMs) are often undermined by their instability. Even subtle and semantically irrelevant changes in prompts can cause dramatic fluctuations in performance, a phenomenon known as prompt sensitivity. Previous studies typically evaluate prompt sensitivity by comparing the LLM's final outputs when prompts change. However, such coarse-grained metrics fail to explain the internal reasons for prompt sensitivity. In this paper, we introduce interacti...
  </details>

- **2026-08-19** — Tanay Chowdhury, Saeideh Shahrokh Esfahani — [Pairwise Ranking Outperforms Single-Action RL for Offline Explanation Selection: A Practical Lesson](http://arxiv.org/abs/2608.18531v1)
  <details><summary>📄 Abstract</summary>
  Industrial explainable-recommendation systems built on LLMs incur a substantial serving cost: each request triggers an LLM generation, with latency in the hundreds of milliseconds and cost that scales linearly with traffic. We separate generation from selection: explanations are produced ahead of time as a frozen candidate pool (six prompt styles, two commodity LLMs), and a small CPU-resident selector picks one at request time. The stack needs no GPU and returns in under 100 ms.   Our primary be...
  </details>

- **2026-08-19** — Rahul Chowdhury, Timothy A Rupprecht, Senhao Cao et al. — [Mechanistic Interpretability of Structure-Aware Numerical Reasoning in LLaMA 3.1 8B](http://arxiv.org/abs/2608.18419v1)
  <details><summary>📄 Abstract</summary>
  Recent work has shown that large language models (LLMs) exhibit strong numerical sequence modeling capabilities and show promise in time-series prediction. While LLMs display in-context learning capabilities, the mechanisms with which they accomplish time-series prediction remain unclear. Specifically, whether they truly understand the underlying structure, which at a minimum requires reasoning over first differences in the sequence of numbers. To study this, we investigate Llama 3.1-8B from a m...
  </details>

- **2026-08-18** — Wang Warren Chen, Jiahao Zhang, Zhenjiang Li et al. — [HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](http://arxiv.org/abs/2608.17584v2)
  <details><summary>📄 Abstract</summary>
  We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor, Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes. This allows handling new requests during motion, retaining progress, revising actions, and grounding closure in execution outcomes. A s...
  </details>

- **2026-08-18** — Rafael Abreu, Chahana Nagesh — [From complex-step differentiation to a general reconstruction framework](http://arxiv.org/abs/2608.17924v2)
  <details><summary>📄 Abstract</summary>
  The complex-step method is traditionally derived from the Taylor expansion of an analytic function and is widely used as a numerical technique for derivative approximation. We present an alternative formulation based on the Cauchy--Riemann equations and show that the classical complex-step relation arises naturally from the harmonic structure of holomorphic functions. In particular, the complex-step method admits two complementary harmonic interpretations: as a Cauchy problem, in which the deriv...
  </details>

- **2026-08-18** — Matheus P. Loures, Guilherme V. Raffo, Patrícia N. Pena — [Model Predictive Supervisory Control for Hierarchical and Distributed UAS Traffic Management](http://arxiv.org/abs/2608.18353v1)
  <details><summary>📄 Abstract</summary>
  This work proposes a hierarchical Model Predictive Supervisory Control (MPSC) framework for multi-agent systems with shared resources. MPSC integrates receding-horizon cost-optimal control with Supervisory control theory (SCT) based supervision that enforces safety, nonblockingness, and resource exclusivity. Scalability arises from hierarchical and scalable supervisor and automaton templates, enabling distributed execution without monolithic synthesis. Using this framework, this work develops an...
  </details>

- **2026-08-18** — Tommaso Apicella, Alessio Xompero, Andrea Cavallaro — [Reproducible Multimodal Affordance Prediction](http://arxiv.org/abs/2608.18317v1)
  <details><summary>📄 Abstract</summary>
  Affordance prediction is the identification of potential actions an agent can perform on a target object from multimodal inputs. Affordance prediction methods are difficult to evaluate and compare due to heterogeneous problem formulations, inconsistent dataset annotations, incomplete reporting of experimental protocols, and limited information about deployment conditions. These limitations challenge fair benchmarking and performance comparison. To promote transparency, we propose the Affordance ...
  </details>

- **2026-08-18** — Nanda Kishore Sreenivas, Kate Larson — [Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice](http://arxiv.org/abs/2608.18232v1)
  <details><summary>📄 Abstract</summary>
  We extend the standard Principal-Agent framework to scenarios where the Agent selects from a suite of technologies, each characterized by a distinct cost-capability profile. This framework is increasingly critical in the era of Large Language Models (LLMs), where Agents choose both a model and an associated effort level (e.g., token budget). We model the relationship between output quality and effort as a concave, saturating function, which depends on the Agent's hidden two-dimensional action ch...
  </details>

- **2026-08-18** — Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil et al. — [MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure](http://arxiv.org/abs/2608.17823v2)
  <details><summary>📄 Abstract</summary>
  Powered two-wheeler riders face critical safety challenges in low- and middle-income countries, yet limited studies exist on how cognitive stressors such as Time Pressure influence collision risk. We address this gap by introducing a comprehensive dataset consisting of over 129,000 labeled multivariate time-series samples, gathered across 153 simulator rides from 51 participants under No, Low, and High TP scenarios. Across each sequence, we capture 64 distinct attributes covering vehicle motion,...
  </details>

- **2026-08-18** — Tianchen Guan, Xinlei Lin, Royce Cheng-Yue et al. — [ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents](http://arxiv.org/abs/2608.18307v1)
  <details><summary>📄 Abstract</summary>
  Current evaluation of computer-use agents is split between long-horizon workflow benchmarks and atomic GUI-grounding tests. This leaves an under-instrumented middle layer: realistic component-centered interactions (e.g., toggle a button set) that are short enough to diagnose and rich enough to capture the burdens of modern interfaces. We present ComponentBench, a benchmark and diagnostic pipeline for component-level evaluation of computer-use agents on modern web UIs. ComponentBench is organized...
  </details>

- **2026-08-18** — Ruhai Lin, Yiyang Guo, Rui-Jie Zhu et al. — [Allocating Recurrent Compute in Looped Language Models](http://arxiv.org/abs/2608.18230v1)
  <details><summary>📄 Abstract</summary>
  Looped language models improve reasoning and knowledge manipulation by applying shared computation repeatedly. Existing systems usually repeat an entire layer stack, although a mixer and a dense feed-forward network (FFN) perform different operations and have different costs. We ask a narrower question: what should loop? We view recurrence as repeated composition of a state update and argue that an application is valuable when it exposes a new cross-position influence direction that remains obse...
  </details>

- **2026-08-18** — Shuangyu Xie, Kaiyuan Chen, Ken Goldberg — [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](http://arxiv.org/abs/2608.18227v1)
  <details><summary>📄 Abstract</summary>
  Push-T is an iconic benchmark for learning manipulation policies from human demonstrations. The robot must use a single point of contact to push a T-shaped block into a target pose. In this short paper, we revisit the Push-T task in the context of emerging advances in Agentic Robotics where an LLM coding agent -- Claude Code with Fable 5 -- is prompted to create an algorithmic solution that does not require any demonstration data. We study how effective the agentic coding loop can solve the Push...
  </details>

- **2026-08-18** — Mena Attia, Mona Diab, Thamar Solorio — [Figurative and Cultural Knowledge in LLMs: Investigating Cross-Domain Transfer through Fine-Tuning](http://arxiv.org/abs/2608.18361v1)
  <details><summary>📄 Abstract</summary>
  Figurative language is deeply culturally embedded; fluent use requires not just linguistic competence but cultural immersion. We ask whether LLMs can learn this link: does fine-tuning on cultural data improve figurative language understanding, and vice versa? We conduct a systematic study across four models (ALLaM-7B, Fanar-1-9B, Qwen3-8B, Llama-3.1-8B) and six Arabic datasets spanning cultural commonsense, proverbs, and poetry across diverse dialects and regions. Fine-tuning on poetry improves ...
  </details>

- **2026-08-18** — Naoki Egami, Sooahn Shin — [Debiased Inference for AI-Generated Data without Gold-Standard Labels: Identification via Multiple Imperfect Measurements](http://arxiv.org/abs/2608.18294v1)
  <details><summary>📄 Abstract</summary>
  An increasing number of scholars use AI to measure variables they subsequently include in downstream analyses. Although AI-measured variables are often analyzed as if observed without error, ignoring prediction errors in automated measurement leads to substantial bias and invalid confidence intervals in downstream analyses, even if AI measurement accuracy is high, e.g., above 90%. Existing solutions, such as design-based supervised learning and prediction-powered inference, combine error-prone A...
  </details>

- **2026-08-18** — Yara Döring, Felix Bießmann — [Global Crises and National Policies: A Large Scale Analysis of Political Content in German Language Online Media](http://arxiv.org/abs/2608.18268v1)
  <details><summary>📄 Abstract</summary>
  Today most media content is consumed based on algorithmic recommendations. Evidence suggests that this can lead to politically biased media consumption patterns. Automated extraction of political agendas from texts can reveal and analyze political biases in online media -- and thus help fostering politically unbiased media consumption. Here we employ modern political text analysis methods demonstrating the potential of automated fine-grained political bias analysis in online media. We conduct an...
  </details>

- **2026-08-18** — Matthew O. Jackson, Benjamin S. Manning, Yutong Xie et al. — [How AI Prompts Can Teach Us About the Structure of Human Behavior](http://arxiv.org/abs/2608.18265v1)
  <details><summary>📄 Abstract</summary>
  We introduce a general, easy-to-implement AI-based method for studying the structure and complexity of human behavior. We assign a large language model a ``type vector'' and then prompt it to choose actions across settings in which we observe human choices. For instance, the type vector (2,4) becomes ``You are a player characterized by the following profile: 2 out of 5 in Altruism, 4 out of 5 in Risk Aversion,'' after which it is prompted to make choices. We vary the dimensions (e.g., Altruism, ...
  </details>

- **2026-08-18** — Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba — [Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents](http://arxiv.org/abs/2608.18008v1)
  <details><summary>📄 Abstract</summary>
  Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger t...
  </details>

- **2026-08-18** — Roman Maksimov, Vladimir Aletov, Vladimir Solodkin et al. — [Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box Attacks on LLMs](http://arxiv.org/abs/2608.17836v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are granted increasing autonomy, it is essential to investigate methods that can induce unsafe behavior. We propose a novel white-box attack inspired by locate-then-edit approaches from the field of Knowledge Editing. Our choice is motivated by the observation that models edited with such schemes tend to assign unusually high prediction probabilities to the edit target, a property that is particularly advantageous when designing attacks. We modify the editing fram...
  </details>

- **2026-08-18** — Jialong Li, Jialing Zhu — [Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch](http://arxiv.org/abs/2608.17684v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents turn experience into reusable skills, workflows, or memories, but post-evolution accuracy alone does not show whether learned behavior preserves previously correct behavior or security. We audit SkillOpt, Agent Workflow Memory (AWM), and ReasoningBank in simulated e-banking using matched benign acquisition trajectories, sealed evaluation endpoints, execution-grounded checks, and independent state replay. On Qwen 3.7 Flash, SkillOpt raises benign utility from 0.741 to 0.837 w...
  </details>

- **2026-08-18** — Jincheng Yang, Yulong Fu, Chengwei Liu et al. — [Benchmarking Automated Security Patch Backporting: How Far Are We?](http://arxiv.org/abs/2608.17671v1)
  <details><summary>📄 Abstract</summary>
  Automated security patch backporting is critical for mitigating N-day vulnerabilities. Recent tools report success rates above 80% on their respective datasets. However, these evaluations are often confined to homogeneous environments, such as one repository or specific project versions. Consequently, it remains unclear how well these tools generalize beyond their originally targeted scenarios. We present Porting Benchmark, a curated dataset of 1,234 security patch backporting cases spanning cro...
  </details>

- **2026-08-18** — Haoran Bu, Zejian Chen, Litian Zhang et al. — [GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities](http://arxiv.org/abs/2608.17665v1)
  <details><summary>📄 Abstract</summary>
  LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are difficult to realize in practice. We therefore formulate a new threat, Memory-Mediated Polarization Cascade, which uses agent memory as a persistence channel and public discussion as a pro...
  </details>

- **2026-08-18** — Mateo Cárdenes Wuttig, Joseph Tindall — [A Complete Classification of Complex Hadamard Matrices of Order Six](http://arxiv.org/abs/2608.18053v1)
  <details><summary>📄 Abstract</summary>
  Complex Hadamard matrices encode perfectly balanced unitary transformations. They underlie mutually unbiased quantum measurements and multiphoton interferometry. Their classification is complete through order five, but order six -- the first dimension in which several continuous families coexist with an isolated solution -- has remained open for decades. Here, we give a complete and exact finite-incidence classification of order-six complex Hadamard matrices up to standard equivalence. We first ...
  </details>

- **2026-08-18** — Emma Ceccherini, Daniel Lawson, Anjulika Salhan — [Where A Small Language Model Helps in Invoice Categorisation, Understood Through Embedding Geometry](http://arxiv.org/abs/2608.18033v1)
  <details><summary>📄 Abstract</summary>
  Categorising invoices into the correct General Ledger (GL) code underpins financial reporting and tax compliance. This is a skilled accounting judgement rather than a routine task: the correct category depends subtly on the nature of the purchasing business, the vendor and the invoice text. Whilst AI is increasingly being adopted across industries to automate tasks, including invoice categorisation, implementations built on in-house small language models (SLMs) can simultaneously reduce cost and...
  </details>

- **2026-08-18** — Alexis Farman, Benjamin J. Walker, Martin A. Pule et al. — [Mathematical modelling of immune persistence and relapse pathways in CAR T-cell therapy for B-ALL](http://arxiv.org/abs/2608.17955v1)
  <details><summary>📄 Abstract</summary>
  Chimeric antigen receptor (CAR) T-cell therapy has transformed the treatment of B-cell acute lymphoblastic leukaemia (B-ALL). Despite high initial response rates, a substantial fraction of patients relapse, often due to loss of CAR T-cell persistence, antigen escape, or immune-privileged sites that shield tumour cells. Prolonged CAR T-cell persistence is clinically associated with durable remission, but why it is required remains poorly understood. To address this, we develop and analyse the BEA...
  </details>

- **2026-08-18** — Zixuan Li — [Bounded-State Restoration: Decoupling Local Restore Capacity from External LLM State](http://arxiv.org/abs/2608.17826v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical KV-cache systems can retain long-context LLM execution state beyond GPU memory, but retention capacity does not determine the local memory required to make that state executable again. We isolate this second resource as the restoration working set (RWS): the peak local staging state whose lifetimes overlap during restoration. In the pinned upstream LMCache whole-plan path, measured full-reuse points for 1.956, 7.823, and 15.646 GiB/rank states first succeed at 2, 8, and 16 GiB L1 ru...
  </details>

- **2026-08-18** — Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil et al. — [MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure](http://arxiv.org/abs/2608.17823v1)
  <details><summary>📄 Abstract</summary>
  Powered two-wheeler riders face critical safety challenges in low- and middle-income countries, yet limited studies exist on how cognitive stressors such as Time Pressure influence collision risk. To address this gap, we introduce a large-scale dataset of over 129,000 labeled multivariate time-series sequences from 153 simulator rides by 51 participants under No, Low, and High TP, capturing 64 features across vehicle dynamics, control inputs, proximity, and behavioral violations. Building on thi...
  </details>

- **2026-08-18** — Sahab Zandi, Noah Kostesku, Christophe Mues et al. — [Communicating Credit Risk with Large Language Models: Evaluation of Explanations from Standard and Alternative Data-Based Models](http://arxiv.org/abs/2608.17715v1)
  <details><summary>📄 Abstract</summary>
  Credit decisioning is a high-stakes task in which model outputs must be accurate and explainable to support compliant decisions. Although modern credit risk models such as eXtreme Gradient Boosting (XGBoost) and Graph Neural Networks (GNNs) improve predictive performance, their explanations are often too technical for stakeholders creating communication gaps that can shape approvals, denials, and fairness judgments. We examine whether Large Language Models (LLMs) can serve as explanation layers ...
  </details>

- **2026-08-18** — Jingyuan Wang, Richong Zhang, Zhijie Nie et al. — [DEPT: Document Embedding Preservation Tuning for Unified Query Expansion and Retrieval](http://arxiv.org/abs/2608.17632v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can both expand underspecified queries and encode text as dense representations, suggesting a unified model for query expansion and retrieval. Existing systems usually rely on prompted expansions, independently trained modules, or staged optimization, leaving generated expansions only indirectly aligned with the retrieval loss that judges them. We train a single decoder-only LLM end to end, where the same model generates the expansion and encodes both the expanded qu...
  </details>

- **2026-08-18** — Andrea Coladangelo, Qipeng Liu, Ziyi Xie — [Unclonable encryption from BB84 states: a simultaneous Goldreich-Levin reduction](http://arxiv.org/abs/2608.17629v1)
  <details><summary>📄 Abstract</summary>
  Goldreich-Levin reductions are ubiquitous in cryptography: they convert an algorithm capable of guessing $\langle r, m \rangle$ (mod $2$) for a hidden string $m$ and a random challenge $r$, to one that is capable of extracting the entirety of $m$. Here, we describe a "simultaneous" Goldreich-Levin reduction for two entangled parties who are capable of guessing $\langle r, m \rangle$ given uniformly random identical challenges $r$. This allows to upgrade any unclonable encryption scheme satisfyin...
  </details>

- **2026-08-18** — Wang Warren Chen, Jiahao Zhang, Zhenjiang Li et al. — [HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](http://arxiv.org/abs/2608.17584v1)
  <details><summary>📄 Abstract</summary>
  We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor, Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes. This allows handling new requests during motion, retaining progress, revising actions, and grounding closure in execution outcomes. A s...
  </details>

- **2026-08-18** — Zongwei Lv, Yuemeng Xu, Yilun Yao et al. — [ArborMem: Navigating Interaction States with Memory Forests](http://arxiv.org/abs/2608.17534v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly serve as persistent conversational assistants, requiring memory that preserves relevant experience and maintains continuity across interactions. Existing methods improve access to conversational history through long-context processing, selective retrieval, and structured memory organization. However, most systems treat memory access as retrieving relevant past information without first determining which prior interaction state the current turn resumes. This lim...
  </details>

- **2026-08-18** — Madhumitha Venkatesh, Shanawaj S Madarkar, Konda Reddy Mopuri — [BrainNorm: A Foundation Model that knows Normal via Semantic Atlas Pretraining](http://arxiv.org/abs/2608.17521v1)
  <details><summary>📄 Abstract</summary>
  We introduce BrainNorm, a normative foundation model, trained and tested on ~66,000 T1-weighted structural MRI (T1w sMRI) scans. By leveraging language-image style contrastive pretraining on healthy cohorts across ages, BrainNorm learns a Semantic Atlas Latent space (SAL), where each scan is represented as a set of atlas-parcel embeddings. This yields parcel-specific healthy aging template trajectories that support age-consistent template matching and localized deviation scoring relative to a su...
  </details>

- **2026-08-18** — Matheus S. Azevedo, Geovana S. de Oliveira, Andrea Failla et al. — [The Brazilian Vaccination Debate on YouTube: Topics, Perspectives, and Engagement Dynamics](http://arxiv.org/abs/2608.17502v1)
  <details><summary>📄 Abstract</summary>
  Vaccination debates are central to online public health communication, as COVID-19 intensified disputes over scientific authority, institutional trust, and political identity. Yet studies often isolate semantic structure, stance, misinformation, and engagement, leaving their interplay over time poorly understood. We conduct a multilevel computational text analysis based on language models applied to 1.27 million Brazilian YouTube comments from 2018 to 2024, using what is, to our knowledge, the l...
  </details>

- **2026-08-18** — Yiwen Zhao, Zhihao Wen, Yuchen Mao et al. — [Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context](http://arxiv.org/abs/2608.17499v1)
  <details><summary>📄 Abstract</summary>
  User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more than context: it also provides noisy, temporally local evidence about the preceding user-to-user segment. We introduce \textbf{F}eedback-\textbf{A}ware \textbf{C}redit \textbf{A}ssignment (\textsc{FA...
  </details>

- **2026-08-18** — Xingrui Zhuo, Jiapu Wang, Manzong Huang et al. — [Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning](http://arxiv.org/abs/2608.17443v1)
  <details><summary>📄 Abstract</summary>
  Knowledge Graph Reasoning (KGR) aims to discover latent facts by leveraging the structural evidence available in KGs, posing a challenge to the structural semantic understanding capability of KGR models. Recent studies have demonstrated that Large Language Models (LLMs) can achieve remarkable progress on KGR tasks via flexible in-context learning. However, the inherent representation inconsistency between KG structural context and LLM parametric knowledge remains inadequately addressed. This lim...
  </details>

- **2026-08-18** — Bonan Zhang, Shiyu Dong, Quan Hung Tran et al. — [MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding](http://arxiv.org/abs/2608.17402v1)
  <details><summary>📄 Abstract</summary>
  Vision encoders are a critical component of vision-language models, and scaling their capacity effectively improves performance. However, dense scaling increases compute cost and inference latency. Mixture-of-Experts (MoE) architectures offer a compelling alternative, having enabled efficient scaling in LLMs, yet the MoE design space for CLIP-style vision encoders remains underexplored at State-of-the-Art (SOTA) levels. In this work, we systematically study MoE designs for vision encoder scaling...
  </details>

- **2026-08-18** — Maria Valentini, Téa Wright, Julisa Granados et al. — [An Investigation of Translationese in the Generations of Multilingual Large Language Models](http://arxiv.org/abs/2608.17399v1)
  <details><summary>📄 Abstract</summary>
  Text which has been translated from another language tends to carry with it evidence of translation$\unicode{x2014}$hence, it is often referred to as $\textit{translationese}$. Multilingual large language models (MLLMs) generate text in a variety of languages. However, it is still unclear if MLLMs' generations resemble internal translation (from English or, potentially, other languages) and, thus, result in translationese. Here, we ask the following research questions: (1) Does text generated by...
  </details>

- **2026-08-18** — Arnab Mallick — [Brief Announcement: Fair Binding for Hidden-State Authorization in Byzantine SMR](http://arxiv.org/abs/2608.17349v1)
  <details><summary>📄 Abstract</summary>
  Validated Byzantine SMR assumes that replicas can evaluate the validity of an ordered command. Agent authorization creates a different regime: a command may be valid only relative to a committed policy state that validators cannot reconstruct from the log. A proof that an action was authorized at an old commitment is then only a historical attestation, it does not by itself reserve the hidden resource for later use.   We isolate two independent requirements for safe live allocation of a hidden c...
  </details>

- **2026-08-18** — Hanzhi Zhang, Qiao Zhang, Qinglei Cao et al. — [TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration](http://arxiv.org/abs/2608.17336v1)
  <details><summary>📄 Abstract</summary>
  Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardware-aligned score tiles outside fused dense attention. We introduce TileMix, a tile-centric precision-routing kernel that makes numerical precision an executable spatial decision over score-tile group...
  </details>

- **2026-08-18** — Saketh Reddy Vemula, Parameswari Krishnamurthy — [What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?](http://arxiv.org/abs/2608.17325v1)
  <details><summary>📄 Abstract</summary>
  Tokenization is a fundamental component of language modeling pipelines. Despite its importance, it is often fixed, even though it significantly impacts model performance across languages. In this work, we analyze what tokens are learned when tokenization is jointly optimized with language modeling. We compare tokenizer-free approaches such as SSLMs and H-Nets with fixed tokenizers across 18 typologically and script-diverse languages. Our results show that joint optimization fundamentally alters ...
  </details>

- **2026-08-18** — Zhiyuan Yan, Xiaofeng Zhou, Ziyue Zheng et al. — [NeuroAbs: A Neuro-Symbolic RTL Abstraction Framework for Property Checking Acceleration](http://arxiv.org/abs/2608.17304v1)
  <details><summary>📄 Abstract</summary>
  Formal verification is a crucial technique for ensuring the functional correctness of hardware designs. In the context of property checking, a key challenge is how to efficiently prove a user-specified property in the face of increasingly complex RTL designs. To address this challenge, abstraction techniques are often employed to reduce system complexity and accelerate the verification process. However, prior RTL abstraction methods either require significant manual effort or rely on rule-based ...
  </details>

- **2026-08-18** — Emama Nahid, Tahmid Imtiaz Imu, Huayue Gu et al. — [Q-Interference: Memory-Efficient Phase-Aware Quantum-Inspired Attention](http://arxiv.org/abs/2608.17288v1)
  <details><summary>📄 Abstract</summary>
  GPT attention measures token compatibility through dot-product similarity. This mechanism is simple, effective, and memory-efficient. But it does not explicitly model whether strong token features should reinforce or suppress one another. We introduce Q-Interference, a fully classical quantum-inspired attention mechanism for autoregressive language modeling that augments each query and key feature with an amplitude and a learned phase. The resulting attention score is phase-aware which aligned p...
  </details>

- **2026-08-18** — Ce Bian, Xusheng He, Jinrong Zhang et al. — [Key-Frame Reasoning with SAM3: Third Place Solution for the MeViS-Text Track of the 8th LSVOS Challenge](http://arxiv.org/abs/2608.17279v1)
  <details><summary>📄 Abstract</summary>
  This report presents a two-stage, training-free solution for the MeViS-Text track of the 8th LSVOS Challenge. The task requires a model to localize and segment the object specified by a natural-language expression throughout a video. Such expressions often depend on temporal cues, including actions, interactions, directions, and relative positions. Our first stage uses Gemini-3.1 Pro via API to decompose a video-level event into instance-level targets, select a key frame for each target, and gen...
  </details>

- **2026-08-18** — Swati Rajwal, Sanjay Das, Tirthankar Ghosal — [Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking](http://arxiv.org/abs/2608.17270v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for scientific hypothesis generation. However, evaluating generated hypotheses remains a challenge for trustworthy AI-enabled scientific workflows. Existing approaches often use LLMs as judges or rely on semantic similarity, which can favor familiar ideas over novel ones. We propose a logit-based energy scoring method that evaluates hypotheses using a language model's intrinsic confidence rather than comparative judgment. We benchmarked seven la...
  </details>

- **2026-08-18** — Yihang Chen, Pin Qian, Su Wang et al. — [Explicit State Elicitation Is Not Enough: A Controlled Audit of Memory-Policy Classification](http://arxiv.org/abs/2608.17247v1)
  <details><summary>📄 Abstract</summary>
  Personalized agents must decide whether retrieved user memory should be used, ignored, updated, or queried before it affects a current task. We use this setting to develop an empirical audit protocol for structured intermediate outputs: first audit dataset shortcuts, then isolate bundled prompt changes, check whether intermediate labels are answer-associated, test decomposed semantic evidence, and audit provider-level execution failures. A 480-example synthetic development set initially suggeste...
  </details>

- **2026-08-18** — Oussama Ziadi, Abdelilah Rochd, Samir Idrissi Kaitouni et al. — [Safe Deep Reinforcement Learning for Energy-Efficient HVAC Control in Multi-Zone Residential Buildings](http://arxiv.org/abs/2608.17235v1)
  <details><summary>📄 Abstract</summary>
  HVAC systems represent a major share of building energy consumption. Traditional control strategies are limited in coordinating energy-comfort tradeoffs across multiple zones simultaneously. Reinforcement learning (RL) offers adaptive, data-driven control that optimizes performance over time. However, deploying learned neural network controllers in safety-critical building systems remains challenging due to lack of formal safety guarantees. We propose a safety-certified deep RL framework for mul...
  </details>

- **2026-08-18** — Amir Arsalan Nematollahi, Shayan Ahmadi, Mehdi Tale Masouleh et al. — [Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision](http://arxiv.org/abs/2608.17628v1)
  <details><summary>📄 Abstract</summary>
  Developing robots capable of understanding and manipulating objects requires compact, interpretable, and generalizable representations. This work proposes a reinforcement learning-based framework for robotic grasp refinement, integrating keypoint-based object representations with a Deep Q-Network (DQN). Using 2D overhead images captured in a simulated environment, a geometric-based algorithm generates initial grasp candidates, which are iteratively refined by the proposed framework, transforming...
  </details>

- **2026-08-18** — Dohoon Park, Seungyun Han, Hyun-Woo Lee — [Intra-atomic magnetic octupoles and their coupling to cluster magnetic octupoles in Chiral antiferromagnets Mn$_3$Sn](http://arxiv.org/abs/2608.17461v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate that Mn$_3$Sn hosts finite intra-atomic magnetic octupoles (AMOs) $\mathbf{o}$ in addition to the well-established cluster magnetic octupole (CMO) $\mathbf{O}$. In contrast to the cluster-scale CMO, the AMO is a site-localized magnetic multipole associated with the anisotropic intra-atomic spin density. Symmetry analysis shows that the CMO and AMO transform in the same representation, allowing a bilinear interaction of the form $-g\,\mathbf{O}\cdot\mathbf{o}$. Using first-principl...
  </details>

- **2026-08-18** — Hoda Yamani, Yuning Xing, Koen van Rijnsoever et al. — [Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning](http://arxiv.org/abs/2608.17347v1)
  <details><summary>📄 Abstract</summary>
  Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves sample efficiency by immediately repeating action sequences from successful episodes during environment interaction. Unlike conventional approaches such as Experience Replay and Self-Imitation Learni...
  </details>

- **2026-08-18** — Iryna Hartsock, Cesar Lam, Christopher Otteni et al. — [Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation](http://arxiv.org/abs/2608.18072v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023 and 2024. A multi-agent AI pipeline was developed to perform report structuring and quality assurance (QA). The system structured the report into standardized anatomical sections at th...
  </details>

- **2026-08-18** — Andrew Wack — [CLOPS: Benchmarking System Speed at Utility Scale](http://arxiv.org/abs/2608.18044v1)
  <details><summary>📄 Abstract</summary>
  As quantum processors scale to hundreds of qubits, execution speed is a critical performance dimension alongside scale and quality. While substantial progress has been made in benchmarking circuit fidelity, existing speed metrics often fail to reflect the sustained, end-to-end throughput experienced by users running utility-scale workloads. This shortfall is especially pronounced for layered, parameterized circuits executed repeatedly within classical-quantum workflows, such as variational algor...
  </details>

- **2026-08-18** — Nour Shaheen, Junwei Ma, Alex Labach et al. — [Understanding the Surprising Generalization Properties of Tabular Foundation Models](http://arxiv.org/abs/2608.17957v1)
  <details><summary>📄 Abstract</summary>
  Tabular Foundation Models (TFMs) increasingly rely on in-context learning, where a model receives labelled examples at inference time and predicts labels for new inputs without updating its weights. Existing TFMs are typically trained on either massive synthetic corpora or very large collections of real datasets. In contrast, we show that surprisingly strong transfer can emerge from self-supervised pre-training on just a single real table. In this setting, we also find that tables tend to be eit...
  </details>

- **2026-08-18** — Jianyu Sun, Zhenxuan Zhang, Guang Yang et al. — [PerFact: Perception-Derived Fact Prompting for 3D Brain MRI Report Generation](http://arxiv.org/abs/2608.17926v1)
  <details><summary>📄 Abstract</summary>
  Radiology report generation has matured almost entirely on 2D chest radiographs, where the default route to better reports is a larger backbone or a pre-training one on medical data. We revisit that assumption on 3D multi-sequence brain MRI, a volumetric multi-disease regime, and find that the model is not the lever. Zero-shot medical and radiology vision-language models transfer poorly to brain MRI, with chest radiograph specialists failing most conspicuously, and five backbones fine-tuned iden...
  </details>

- **2026-08-18** — Fahad Ahammed, Omar Faruq Shikdar, Navid Zaman et al. — [AppendiGrade: An XAI-Enhanced Deep Learning Framework for Grading Appendicitis in Ultrasound with Gaussian Blur and Grad-CAM](http://arxiv.org/abs/2608.17923v1)
  <details><summary>📄 Abstract</summary>
  Appendicitis is one of the most common abdominal emergencies worldwide and requires prompt diagnosis and treatment to prevent life-threatening conditions. However, accurately differentiating complicated cases, such as perforation or abscess formation, from uncomplicated appendicitis remains a significant clinical challenge. Among other methods, ultrasound is a safer and more cost-efficient diagnostic technique because of the lack of radiation exposure. In this research, an advanced system capabl...
  </details>

- **2026-08-18** — Zheling Tan, Jin Gao, Dequan Wang — [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](http://arxiv.org/abs/2608.17911v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents operate across structured workflows and sessions, preserving long-term history does not ensure that later contexts can recover relevant evidence through a bounded memory interface. We study this evidence-reachability problem in long-term conversational memory, where retrieval still relies heavily on semantic similarity. This works well for topical recall, but it often misses earlier experiences, plans, or motivations that are semantically distant from the later events they help exp...
  </details>

- **2026-08-18** — Franky Kevin Nando Tezoh, Ali Hussaini Umar, Alessandro Laio et al. — [BayesPrompt: human readable prompts that make sense](http://arxiv.org/abs/2608.17866v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing prompts that can elicit a desired answer or behaviour in an LLM is an open and important research topic. Optimisation methods which aim at minimising the perplexity of a given answer, however, consistently yield so-called pseudoprompts, unintelligible strings of tokens which can lack human interpretability. We argue that this is a consequence of the ill-posedness of the prompt optimisation task. By reframing the task as a Bayesian posterior inference over prompts, we propose an ef...
  </details>

- **2026-08-18** — Camilla Dalerci, Thilo Michael, Robin Schaefer et al. — [From Global Benchmarks to Local Evaluations: Benchmarking LLMs for the German Public Sector](http://arxiv.org/abs/2608.17827v1)
  <details><summary>📄 Abstract</summary>
  Public institutions face a persistent challenge in selecting LLMs suited to their specific context. Existing benchmarks, however, are of limited use as they primarily reflect English-language and US-centric settings, and often only evaluate task performance. In this paper, we present first results of MÖVE, a holistic evaluation framework for the German public sector, examining three rarely considered governance dimensions: energy consumption, provider transparency, and knowledge of German-party ...
  </details>

- **2026-08-18** — Alona Strugatski, Licol Zeinfeld, Jason Cooper et al. — [Interpretable Humans, Alien LLMs: Expert Analysis of Latent Structures in Assessment Responses](http://arxiv.org/abs/2608.17810v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of large language models (LLMs) relies heavily on human-designed assessments, implicitly assuming that AI and humans employ similar underlying cognitive constructs. Challenging this assumption, we investigate whether the latent factors governing LLM performance carry the same substantive, human-interpretable meaning as the cognitive constructs governing human learners. Using responses from humans and six LLMs across quantitative reasoning and chemistry assessments, we conducted Ex...
  </details>

- **2026-08-18** — Lu Liu, Chi Xie, Xi Xiong — [Offline Multi-Agent Reinforcement Learning with a Physics-Informed World Model for Cooperative Mixed Traffic Control](http://arxiv.org/abs/2608.17739v1)
  <details><summary>📄 Abstract</summary>
  This study investigates cooperative control of connected and automated vehicles (CAVs) at partially observable highway bottlenecks in mixed traffic, aiming to mitigate congestion without relying on complete global traffic states or online trial-and-error. We propose a physics-informed world model-based offline multi-agent reinforcement learning framework that reconstructs a physically interpretable global traffic state from local CAV observation-action histories, with coupled macroscopic-microsc...
  </details>

- **2026-08-18** — Matthew T. Ford, Francis Bahk, Jingjing Wang et al. — [LLM-Derived Preference Judgments Are Not Self-Consistent](http://arxiv.org/abs/2608.17644v1)
  <details><summary>📄 Abstract</summary>
  Agents increasingly interpret a person's natural-language preferences by querying an LLM for numerical preference judgments, e.g., by asking how much the person would be willing to pay for an item. A growing body of work estimates a utility function from these judgments and then chooses actions based on their estimated utility. This pipeline assumes the judgments are approximately self-consistent: that a single utility function can reproduce them. But are they? To study this question, we measure...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 590 |
| prompt-injection | 499 |
| memory-poisoning | 44 |
| tool-use-attack | 123 |
| backdoor | 422 |
| adversarial-attack | 567 |
| privacy-leakage | 3884 |
| steganography | 56 |
| misuse | 917 |
| red-teaming | 115 |
| vulnerability | 2772 |
| defense | 2504 |
| alignment | 2315 |
| robustness | 2344 |
| watermark | 322 |
| unlearning | 91 |
| agent-safety | 52 |
| benchmark | 60 |
| survey | 293 |
| other | 6646 |

---

📚 **全部 24616 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-08-25 01:37:06*