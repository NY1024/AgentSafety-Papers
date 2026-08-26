<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-25117-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-26 19:42 ｜ **论文总数 / Total Papers**: 25117（近 30 天 / Recent 30 days: 4223）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 25117 篇论文（含摘要、分类筛选、搜索）/ View all 25117 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 595
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 508
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 126
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 426
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 570
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3915
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 57
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 933
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 117
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2816
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2571
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2379
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2429
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 340
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 92
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 62
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 297
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6788

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4223 篇，完整 25117 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4223 papers from the last 30 days (with date, authors & abstract). For the full list of 25117 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 5 papers

- **2026-08-25** — Anjun Gao, Yueyang Quan, Yufei Xia et al. — [NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution](http://arxiv.org/abs/2608.23959v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models (LLMs) remains brittle against a growing spectrum of attacks. Jailbreak attacks bypass safety mechanisms through crafted prompts, while neuron-level attacks directly prune safety-critical neurons post-deployment. Both exploit a common weakness: safety-relevant information concentrates in a sparse neuron subset. We present NeuronGuard, a fine-tuning-stage defense that simultaneously hardens LLMs against both attack classes by redistributing safety signals...
  </details>

- **2026-08-24** — Lorenzo Bossi, Federico Saccani, Francesco Panebianco et al. — [Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums](http://arxiv.org/abs/2608.23185v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence from underground forums has traditionally relied on passive monitoring. However, as users have become more aware of large-scale data collection, valuable intelligence has become increasingly rare in open forums, often migrating instead to private or harder-to-reach spaces, making passive approaches inadequate. Building on the intuition that relevant information can be obtained through active elicitation, this paper presents DarkBot, to the best of our knowledge, the fir...
  </details>

- **2026-08-24** — Zeyu Feng, Qingyu Wu, Yuzhe Luo et al. — [PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies](http://arxiv.org/abs/2608.23028v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for...
  </details>

- **2026-08-23** — Wenyun Li, Guiping Cao, Xiangyuan Lan et al. — [Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models](http://arxiv.org/abs/2608.22312v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal representations, leaving multimodal inputs exploitable through latent semantic cues. We propose Text-Anchored Semantic Perturbation Attack (TA-SPA), a black-box jailbreak framework that optimizes transferable...
  </details>

- **2026-08-22** — Aaditya Pratap, Harsh Kasyap, Somanath Tripathy — [Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks](http://arxiv.org/abs/2608.21895v1)
  <details><summary>📄 Abstract</summary>
  Locally deployed Large Language Models (LLMs) via inference engines such as Ollama run without the moderation and abuse detection present in API-served models. Therefore, the safety of LLMs depends on the defense mechanisms used, and their effectiveness depends on the assumptions on which they were designed. This paper does an audit of defense mechanisms under jailbreak attacks on locally deployed models. Some defenses provide formal guarantees (SmoothLLM, Erase-and-Check, Sequential Monitors), ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-08-25** — Yichao Gao, Yumo Zhang, Yunhao Yao et al. — [What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions](http://arxiv.org/abs/2608.24022v1)
  <details><summary>📄 Abstract</summary>
  LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions during LLM inference, thereby subverting the agent's decision. Existing defenses focus on static detection or isolation of malicious content at the input/output level, remains insufficient for detecting such dynamic inducements that arise during ...
  </details>

- **2026-08-25** — Lin-Fa Lee, YI-YU Chang, Kuo-Hui Yeh — [WebMCP-Phalanx: Enforcing and Characterizing Trust Boundaries for Browser-Integrated LLM Agents](http://arxiv.org/abs/2608.24017v1)
  <details><summary>📄 Abstract</summary>
  The emerging W3C WebMCP proposal enables LLM agents to invoke tools exposed by web pages. In multi-party web environments, however, integrating agent execution into a browser security model centered on the Same-Origin Policy (SOP) leaves insufficient provenance and lifecycle guarantees for agent-accessible tools, creating three risks: subject-attribution spoofing, uncontrolled tool lifecycles, and semantic prompt injection. We propose WebMCP-Phalanx, a dual-layer agent runtime architecture. Its ...
  </details>

- **2026-08-24** — Joshua Penman — [Semantic Overlays: Mitigating Prompt Injection with Annotations Beyond Tokens and Steering Vectors](http://arxiv.org/abs/2608.23873v1)
  <details><summary>📄 Abstract</summary>
  Everything a language model sees is tokens. The serving stack knows what each span is -- user input, tool output, instructions -- but the model must keep track of that itself, and it can lose track or be confused: text can be written to read like anything. Prompt injection is a natural exploit of this phenomenon. By scrambling the model's understanding of span identity, an attacker can induce unwanted and potentially dangerous actions. Adding a non-textual channel to the model's input -- a way t...
  </details>

- **2026-08-24** — Avital Aviv, Parth A. Gandh, Ron Bitton et al. — [Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2)](http://arxiv.org/abs/2608.23858v1)
  <details><summary>📄 Abstract</summary>
  The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after signing. Agent interactions and external inputs that shape a transaction before authorization remain outside that protection, including Agent-to-Agent Protocol (A2A) messages and Model Context Protocol (MCP) tool calls. Prior work identified ...
  </details>

- **2026-08-24** — Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol et al. — [TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers](http://arxiv.org/abs/2608.23763v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) has emerged as the standard layer connecting Large Language Model agents to external tool backends. This openness introduces a severe server-side threat we term TrustShift: a compromised MCP server behaves benignly during an initial conditioning phase, building operational reliance and suppressing agent skepticism, before switching to an adversarial payload once an interaction threshold is reached. The evasion is temporal, not syntactic: benign at deploy time, th...
  </details>

- **2026-08-24** — Hanling Tian, Gengyu Zhang, Zeyang Sha et al. — [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](http://arxiv.org/abs/2608.23471v1)
  <details><summary>📄 Abstract</summary>
  Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose InjecMEM, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, ...
  </details>

- **2026-08-24** — Basavesh Ammanaghatta Shivakumar, Swarn Priya, Peng Gao — [AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems](http://arxiv.org/abs/2608.22868v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible steps. We present AgentFlow, a flow-centric policy language and runtime enforcement model for specifying where data may travel in agent systems. Policies are defined over labeled runtime edges and constrain which tools may receive sensitive field...
  </details>

- **2026-08-23** — Jiahao Chen, Rui Yin, Xinfeng Li et al. — [Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds](http://arxiv.org/abs/2608.22248v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been integrated into complex ecosystems (e.g., Code Agents), while Indirect Prompt Injection (IPI) attacks have emerged as critical barriers to their safe deployment. Attackers exploit LLMs' indistinguishability between "instructions" and "data" to manipulate LLMs via maliciously injected instructions. Existing defenses, however, face an intractable safety-utility trade-off: most guardrails either incur high latency or suffer from severe over-refusal. In this pa...
  </details>

- **2026-08-22** — Minjae Seo, Wonwoo Choi, Geonwoo Han et al. — [MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds](http://arxiv.org/abs/2608.22061v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent memory for later use. We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior. Based on this observation, we present IBIA, an Indirect Bias Injection Attack that plants an adversary-aligned stance on a specific topic...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-08-24** — Ziyue Yang, Fan Ding — [Signal or Noise? A Benchmark Study of Agent Skills in Web Development](http://arxiv.org/abs/2608.23067v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills are reusable procedural modules that are increasingly injected into coding-agent sessions to encode framework conventions, anti-patterns, and reusable tools. However, because each injected Skill expands the prompt of every query, an effective Skill benchmark must determine not only whether an agent can solve a task, but whether the Skill should have been injected at all. We introduce WebDev-Skills-Bench and use it for a controlled empirical study of 31 public WebDev Skills on 50 Web...
  </details>

- **2026-08-23** — Qiyan Zhao, Xiaofeng Zhang, Bo Liu et al. — [Coalition-Aware Skill Reliability for Self-Evolving Agents](http://arxiv.org/abs/2608.22610v1)
  <details><summary>📄 Abstract</summary>
  Agent skills, structured artifacts distilled from interaction trajectories and dynamically reused from skill banks, have become a central mechanism for enabling large language model (LLM)-based self-evolving agents to learn from past experience. Yet existing work has largely focused on the operational aspects of skills, such as acquisition, evolution, and retrieval, while leaving a more fundamental reliability question unresolved: Do accumulated skills in an agent's skill bank actually make posi...
  </details>

- **2026-08-22** — Yuanjin Zheng, Jingbang Chen — [SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents](http://arxiv.org/abs/2608.21929v1)
  <details><summary>📄 Abstract</summary>
  Agent skills extend coding agents with task-specific instructions, scripts, and resources, but they also create a trusted   instruction channel that can be abused beyond conventional security attacks. This paper studies token amplification through   skill injection: an economic resource-abuse threat in which a malicious skill causes an agent to consume substantially more   tokens than needed for normal task execution. We present SkillBloat, a two-phase framework that first screens a library of  ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-08-25** — Jiali Wei, Ming Fan, Mingkun Zhang et al. — [Not All Tokens Are Equal: Region-Aware Consistency Repair of Backdoors in MLLMs](http://arxiv.org/abs/2608.24354v1)
  <details><summary>📄 Abstract</summary>
  MLLMs are increasingly deployed in user-facing applications, yet they inherit backdoor risks from the pipelines used to construct them: triggers may reside in images, texts, or both. Existing model-level backdoor removal methods, largely designed for conventional classifiers, show limited effectiveness on MLLMs, while MLLM-specific defenses mainly operate at inference time, filtering suspicious inputs without removing the backdoor embedded in the model. To address this gap and eliminate latent b...
  </details>

- **2026-08-25** — CheolWon Na, Hao Ni, Lukasz Szpruch et al. — [Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems](http://arxiv.org/abs/2608.24069v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent trading systems, in which specialized agents collaborate through structured communication to produce trading decisions, are moving rapidly from research prototypes to live deployments that control real assets. The same inter-agent communication that makes them effective also exposes them: a corrupted signal can propagate to the final decision and translate into realized financial loss. Unlike prior attacks that presume privileged access to system internals, we restrict the ...
  </details>

- **2026-08-25** — Rob Manson — [Curved Inference II: Sleeper Agent Geometry - Extending Interpretability Beyond Probes](http://arxiv.org/abs/2608.24037v1)
  <details><summary>📄 Abstract</summary>
  This paper extends Anthropic's Sleeper Agents research [1], which showed artificial backdoors persist through safety training & can be detected by linear probes with >99% accuracy [2]. However, probe-based detection relies on linear separability that may be an artefact of backdoor insertion rather than a property of naturally occurring deceptive alignment. Sophisticated deceptive behaviours emerging through natural training are unlikely to produce such convenient linear signals.   We introduce a...
  </details>

- **2026-08-25** — Yueyang Quan, Anjun Gao, Yufei Xia et al. — [RAGSentinel: Certifiable Geometric Consensus for Robust Retrieval-Augmented Generation](http://arxiv.org/abs/2608.23965v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) improves the factuality of large language models by grounding responses in external documents, but it also exposes a critical security vulnerability: adversarial documents injected into the knowledge database can enter the context window and steer the model toward targeted incorrect answers. Existing post-retrieval defenses rely on instruction following, parametric knowledge, or text-level consistency, all of which can be imitated or optimized against by adap...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-08-25** — Zi Qian Yong, Ajinkya Kulkarni, Julia Lau et al. — [On the Robustness of Audio Deepfake Detection under Audio Watermarking](http://arxiv.org/abs/2608.24159v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative audio models have enabled highly realistic synthetic speech, increasing the importance of reliable audio deepfake detection (ADD) systems. While prior studies have primarily focused on adversarially optimized perturbations, the robustness of ADD systems under realistic signal transformations remains insufficiently understood. In this work, we investigate the impact of audio watermarking on ADD systems by treating watermarking as a structured, non-adversarial perturb...
  </details>

- **2026-08-23** — Alberick Euraste Djire, Iyiola E. Olatunji, Melissa Tessa et al. — [Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code](http://arxiv.org/abs/2608.22652v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used for code generation, yet they frequently hallucinate non-existent software packages, creating exploitable entry points into the software supply chain. We make four contributions to this problem. First, we show that prior evaluation methodologies systematically inflate hallucination rates by misclassifying standard-library modules as hallucinations in some languages. For Python, the overestimation reaches 9.4 percentage points. Second, we evaluate seven inference-time d...
  </details>

- **2026-08-23** — Hoang Anh Nguyen, Yuan Hong, Hongyi Xu — [Adversarial Agents on Topology Optimization: Understanding the Fragility and Robustness of Deep Learning-based and Physics-Based Design Models under Adversarial Perturbation](http://arxiv.org/abs/2608.22606v1)
  <details><summary>📄 Abstract</summary>
  Topology optimization, using both physic-based approaches and deep learning surrogates, serves as a cornerstone for generative design agents in cyber-manufacturing systems. While deep learning surrogates have gained widespread adoption due to their speed in online design generation, this work demonstrates their vulnerability under input perturbations. In this work, we present a mechanics-grounded reliability evaluation framework that formulates an adversarial agent targeting the generative desig...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 31 papers

- **2026-08-25** — Zhijie Zheng, Yu Li, Chen Qian et al. — [StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing](http://arxiv.org/abs/2608.24777v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized actions. Existing guardrails often evaluate completed trajectories, leaving pre-execution monitoring of step-level actions underexplored. We propose StepGuard, a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed. To train StepGuard, we i...
  </details>

- **2026-08-25** — Gunja Agarwal, Arup Kumar Das, Arun Menon et al. — [AgentWorld: Personality-Aware Reliability Evaluation for Agentic Information Retrieval](http://arxiv.org/abs/2608.24076v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of agentic information retrieval remains limited to scripted interactions with uniform users, missing both natural personality diversity and adversarial brittleness. We present AgentWorld, a simulation framework combining (i)Big Five (OCEAN) personality-driven user populations with stateful tool-use environments; (ii)the pass$^k$ consistency metric with structured fault classification, partial-credit scoring, and dual-control handoff verification; (iii)score-thresholded training-data ...
  </details>

- **2026-08-25** — Sonali Godavarthy, Matthias Neuwirth-Trapp, Tim-Felix Faasch et al. — [X-MULTI: VLM-based Imaging Factor Disentanglement for Factor-Aware Image Synthesis](http://arxiv.org/abs/2608.24563v1)
  <details><summary>📄 Abstract</summary>
  Imaging factor disentanglement in text-to-image generation aims to independently control image acquisition properties such as types of camera lenses, sensor types, viewpoints, and domains to enable combinatorial generalization. This should let the model synthesize novel factor combinations unobserved in the training data, such as pairing a fisheye lens with an event sensor never observed in training data. Recent work, MULTI, introduced learnable, factor-specific embeddings to disentangle imaging...
  </details>

- **2026-08-25** — Lei Jiang — [Do Recipes Have Personas? Characterizing and Generating Creator Style in Attributed Procedural Graphs](http://arxiv.org/abs/2608.24369v1)
  <details><summary>📄 Abstract</summary>
  While large language models (LLMs) possess vast zero-shot procedural knowledge, their tendency to produce homogenized logic often obscures the unique, idiosyncratic execution processes of individual human creators. In this paper, we investigate the computational discovery of procedural personas from unstructured data. To achieve this, we introduce ViralRecipesTrans, a new dataset of procedurally aligned execution flow graphs extracted from popular culinary video transcripts and explicitly mapped...
  </details>

- **2026-08-25** — Long Hoang Pham, Quoc Pham-Nam Ho, Huy-Hung Nguyen et al. — [Rethinking Pre-Training and Augmentation for Zero-Shot Cross-City Object Detection](http://arxiv.org/abs/2608.24154v1)
  <details><summary>📄 Abstract</summary>
  Real-world deployment of traffic surveillance systems is bottlenecked by geographic domain shift, in which models trained in one city underperform when applied to an unseen target city. Conventional domain adaptation relies on hyperparameter-sensitive architectures or direct profiling of target data. Both are fundamentally precluded in privacy-conscious ecosystems that require completely blind training and evaluation loops. In this setting, we explore the effects of pre-training and augmentation...
  </details>

- **2026-08-25** — Juntao Fang, Shifeng Xie, Ruichu Cai et al. — [ChorusTIC: Training-Free Multivariate Time Series Classification via Chorus In-Context Learning](http://arxiv.org/abs/2608.24033v1)
  <details><summary>📄 Abstract</summary>
  Time series classification underpins applications in healthcare, sensing, and industrial monitoring. Although time series foundation models support forecasting and transferable representation learning, classification still typically requires fitting a task-specific classifier on each target dataset, while individual channels of multivariate inputs are often encoded independently. We introduce ChorusTIC, a classification-native foundation model for in-context classification across heterogeneous c...
  </details>

- **2026-08-24** — Seokjin Hwang, Yuting Li, Kiwan Maeng — [Spectrum-Aware Bounds on Invertibility for Privacy-Enhancing Instance Encoding](http://arxiv.org/abs/2608.23382v2)
  <details><summary>📄 Abstract</summary>
  Instance encoding is a popular empirical technique for privacy enhancement when sharing data to an untrusted server. It transforms sensitive data through an encoding process before sharing, with the hope that the encoding process retains utility but makes it hard to reconstruct the original data. However, most work offers no theoretical guarantee that the encoding process is actually irreversible. A recent work derived a mean-squared error (MSE) bound limiting any adversary's reconstruction accu...
  </details>

- **2026-08-24** — Alif Ashrafee, Bartosz Krawczyk — [Restoring Without Forgetting: Continual Learning Across Image Degradations](http://arxiv.org/abs/2608.23799v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in image restoration has converged on all-in-one architectures that jointly handle multiple degradations within a single network. These methods are effective on static benchmarks but target a closed-world setting that assumes simultaneous access to every target degradation at training time. In practice, degradations are encountered sequentially as field-deployed systems progressively face new environmental conditions, and historical training data is often unavailable due to priva...
  </details>

- **2026-08-24** — Igor Bogdanov, James Green — [Infant Care Video Dataset for Classification of Interventions Using Transformers](http://arxiv.org/abs/2608.23838v1)
  <details><summary>📄 Abstract</summary>
  Healthcare documentation in the neonatal intensive care unit (NICU) presents significant challenges, with nurses spending approximately 25\% of their time on record-keeping, while up to 60\% of interventions remain undocumented. Motivated by the need to detect interventions from video automatically, we present the Infant Care Video Dataset (ICVD), a collection of 4,144 videos spanning 12 simulated intervention classes designed for developing automated documentation systems. Our manikin-based app...
  </details>

- **2026-08-24** — Seokjin Hwang,  Yuting,  Li et al. — [Spectrum-Aware Bounds on Invertibility for Privacy-Enhancing Instance Encoding](http://arxiv.org/abs/2608.23382v1)
  <details><summary>📄 Abstract</summary>
  Instance encoding is a popular empirical technique for privacy enhancement when sharing data to an untrusted server. It transforms sensitive data through an encoding process before sharing, with the hope that the encoding process retains utility but makes it hard to reconstruct the original data. However, most work offers no theoretical guarantee that the encoding process is actually irreversible. A recent work derived a mean-squared error (MSE) bound limiting any adversary's reconstruction accu...
  </details>

- **2026-08-24** — Xunlei Chen, Qirui Ye, Yuang Li et al. — [Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality](http://arxiv.org/abs/2608.23020v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) require effective unlearning to address privacy regulations and safety concerns. However, achieving precise forgetting without compromising general utility remains challenging. Existing sequence- and token-level methods penalize target outputs without modeling their context-dependent retrieval paths, which can disrupt linguistic structure or suppress benign knowledge. We present ADU, a fine-grained, training-based framework that shifts unlearning from token erasure t...
  </details>

- **2026-08-24** — Hongchao Wang, Linrui Li, Yunkai Zou et al. — [What's Your NIC Whispering? Network Threat Behavior Recognition via NIC Electromagnetic Side-Channel Leakage](http://arxiv.org/abs/2608.22941v1)
  <details><summary>📄 Abstract</summary>
  Conventional network threat detection primarily relies on packet-level, flow-level, or host-level telemetry. This paper investigates a different observation surface: unintended electromagnetic(EM) emissions generated by network interface card(NIC) activity, and asks whether such physical leakage contains sufficiently structured information for network threat-behavior recognition. We present NICWhisper, which externally captures NIC EM emissions, transforms raw measurements into time-frequency re...
  </details>

- **2026-08-24** — Kurt M Wilson, Mohaiminul Al Nahian, Abeer Matar A. Almalky et al. — [TEE-X: TEE-aware Acceleration Framework for Large Vision Models at the Edge](http://arxiv.org/abs/2608.22716v1)
  <details><summary>📄 Abstract</summary>
  Despite their remarkable success, machine learning models, particularly in vision applications, are alarmingly vulnerable to a range of security threats. One key factor in the attack landscape is the distinction between white-box and black-box threat models, as the latter poses challenges that limit attack effectiveness when access to model information is limited. As a result, using Trusted Execution Environments (TEEs) enhances security for machine learning applications by protecting model conf...
  </details>

- **2026-08-24** — Md Thamed Bin Zaman Chowdhury, Moazzem Hossain — [EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings](http://arxiv.org/abs/2608.23563v1)
  <details><summary>📄 Abstract</summary>
  Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and the high cost of large-scale field inspections. To address this problem, we propose Expert-Grounded Distillation (EGD), a novel artificial intelligence framework that transfers institutional road safety expertise into a compact vision-language model for scalable visual road safety auditing. The key in...
  </details>

- **2026-08-24** — ChengAo Shen, Wenchao Yu, Fangyu Wu et al. — [MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters](http://arxiv.org/abs/2608.23473v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource-constrained scenarios, where compact, specialized forecasters are more desirable. However, lightweight forecasters typically require substantial training data, limiting their use in domains with scarce, slowly accumulated, or privacy-sensitive time series. To address this dilemma, we investigate the challenging problem of few-shot learning for lightweight...
  </details>

- **2026-08-24** — Fabian Schüssler, S. Bisero, M. Cellier et al. — [AI-Assisted Extraction of Follow-up Observations from GCN Circulars in Astro-COLIBRI](http://arxiv.org/abs/2608.23270v1)
  <details><summary>📄 Abstract</summary>
  We present a new Astro-COLIBRI component that converts free-text GCN Circulars into structured, event-linked follow-up records and combines them with structured reports submitted directly by the community. A continuously running Circular listener associates new reports with transient events, applies deterministic pre-analysis, and invokes a schema-constrained large language model extraction step for photometry, contacts, redshifts, and other reported results and metadata. The resulting records a...
  </details>

- **2026-08-24** — Siri Willems, James Butterworth, Lore Goetschalckx et al. — [Future Querying: Can LLMs Serve as Implicit Medical World Models?](http://arxiv.org/abs/2608.23248v1)
  <details><summary>📄 Abstract</summary>
  Traditional clinical prediction models rely on task-specific pipelines and curated, structured data, which scale poorly and underutilize unstructured text. To address this, we introduce future querying, a paradigm that probes whether large language models (LLMs) can function as implicit medical world models by evaluating their ability to answer time-indexed clinical queries about a patient's future. Our framework operates on unstructured clinical documentation using endpoint-agnostic training, e...
  </details>

- **2026-08-24** — Fangcheng Li, Zhen Yu, Kejun Wu et al. — [ByteAction: Byte-space Action Recognition Foundation Model](http://arxiv.org/abs/2608.22760v1)
  <details><summary>📄 Abstract</summary>
  Byte-space Action Recognition (BAR) aims to recognize human actions directly from compressed image bitstreams without any pixel decoding. By operating entirely in byte space, BAR is inherently independent of file integrity and pixel-level reconstruction, making it naturally applicable to privacy-sensitive scenarios and robust against bitstream corruption. In this paper, we propose ByteAction, a BAR foundation model that achieves accurate action recognition on corrupted image bitstreams. ByteActi...
  </details>

- **2026-08-24** — Parisa Ghanad Torshizi, Stacy Marsella — [LLM-Based Selection of Incongruent Verbal and Nonverbal Behavior for Virtual Humans](http://arxiv.org/abs/2608.22731v1)
  <details><summary>📄 Abstract</summary>
  Nonverbal behavior generation systems for virtual agents often take an utterance as input and generate nonverbal behaviors that emphasize or illustrate the content of the verbal channel. However, human nonverbal behavior is shaped by more than the content of the speech. It is also influenced by speaker roles, interpersonal relationships, social context, and the cognitive and emotional states of the interactants. As a result, the nonverbal channel may reinforce, weaken, qualify, or even contradic...
  </details>

- **2026-08-23** — Liang-Wei Li, Chung-Nan Lee, Kishu Gupta et al. — [Syntax Element Encryption for H.265/HEVC Using Chaotic Map-Based Coefficient Scrambling Scheme](http://arxiv.org/abs/2608.22573v1)
  <details><summary>📄 Abstract</summary>
  In today's digital landscape, high-efficiency video coding (H.265/HEVC) has emerged as the most widely used video coding standard, employing selective encryption schemes to protect the privacy of video content while maintaining efficient compression performance. However, existing coefficient scrambling methods impose a significant computational load, leading to increased bit rate overhead due to encryption, longer execution times, and insufficient safety measures. To address these issues, a new ...
  </details>

- **2026-08-23** — Kushagra Yadav, Nalin Prabhath, Amit Lamba et al. — [Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support](http://arxiv.org/abs/2608.22583v1)
  <details><summary>📄 Abstract</summary>
  Clinical records contain rich evidence about patient state, but converting that evidence into reliable, structured knowledge graphs remains difficult because extraction errors, ontology mismatch, missing relations, and temporal ambiguity can propagate into downstream systems. We propose a clinical knowledge graph construction and refinement framework that combines multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement. Rather...
  </details>

- **2026-08-23** — Hermann Yepdjio Nkouanga, Minwei Luo, Maggie Wigness et al. — [Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction](http://arxiv.org/abs/2608.22196v1)
  <details><summary>📄 Abstract</summary>
  While cascaded multi-talker ASR (MT-ASR) leverages state-of-the-art foundation models, its performance is often capped by speaker leakage during separation. Prior correction strategies primarily focus on lexical re-labeling for speaker attribution. We propose a complementary pruning-based paradigm that robustly identifies and removes leakage artifacts. Our method utilizes a pre-trained speaker diarization model as a multimodal verifier to prune transcribed segments satisfying a tripartite consen...
  </details>

- **2026-08-23** — Jiajun Sun, Zhanrui Cai — [Token-Level Likelihood-Array Regression for Membership Inference and AI-Generated Text Detection](http://arxiv.org/abs/2608.22179v1)
  <details><summary>📄 Abstract</summary>
  Membership inference asks whether a text was used to train a language model, whereas AI-generated text detection asks whether it was generated by a language model rather than written by a human. Existing likelihood-based methods typically compress token-level probabilities into a few prespecified scores, most often using only probabilities conditioned on the full preceding context. We propose likelihood-array regression (LAR), which evaluates each target token under nested left-context windows a...
  </details>

- **2026-08-23** — Bin Dong, Jinghong Chen — [CiUNet: A Hybrid Swin-CNN UNet for Medical Image Segmentation](http://arxiv.org/abs/2608.22281v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation requires high accuracy and robustness, yet practical commercial deployment also demands privacy preservation and computational efficiency. In this context, the U-Net architecture, which can be inherently decoupled into independent encoder and decoder components, serves as a natural commercial choice. However, pure Transformer-based variants like Swin-UNet often suffer from insufficient local detail capture and limited interpretability. In this paper, we propose a light...
  </details>

- **2026-08-23** — Hariharan Ramesh, Someshwaran Murugaiyan, Jyotikrishna Dass — [Unveiling the Depth-Performance Dilemma in Split-Federated Fine-tuning of LLMs](http://arxiv.org/abs/2608.22188v1)
  <details><summary>📄 Abstract</summary>
  Split Federated Fine-tuning (SFF) is a promising paradigm for scaling Large Language Models (LLMs) by partitioning model depth between resource-constrained clients and a centralized server. While system incentives for throughput and privacy favor deep partitions, the impact of such configurations on model utility remains poorly understood. In this work, we identify and characterize the Depth-Performance Dilemma: the regime that maximizes system efficiency is precisely where fine-tuning quality c...
  </details>

- **2026-08-23** — Jun Hou, Yi Fang, Xuan Wang — [Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction](http://arxiv.org/abs/2608.22176v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly applied to clinical prediction tasks such as in-hospital mortality and readmission from electronic health records (EHRs). Privacy and compliance constraints motivate systems that can be deployed locally, which has increased interest in open-weight multi-agent designs. However, most medical multi-agent systems are evaluated as a single block, leaving unclear which agent role contributes to prediction and whether retrieval drives observed gains. We stu...
  </details>

- **2026-08-22** — Daniel Rodriguez-Cardenas, David Nader Palacio, Anna Schmedding et al. — [On Predicting Vulnerability Severity Using In-Context Learning: An Industrial Case Study](http://arxiv.org/abs/2608.22089v1)
  <details><summary>📄 Abstract</summary>
  Modern software systems require earlier and more scalable vulnerability severity assessment to reduce exposure to high-impact security flaws. Security analysts typically assign CVSS scores, but this manual triage does not scale with the growth of disclosed vulnerabilities and often depends on cloud LLM services that raise confidentiality concerns. This paper presents an industrial case study on predicting CVSS v3.1 scores directly from vulnerable C/C++ snippets using in-context learning with loc...
  </details>

- **2026-08-22** — YuHang Wu, HaoXian Liu, Jia Tao — [SoulGard-VL-2B: A Vision-Language Model for Edge-Based Feline Behavior Understanding](http://arxiv.org/abs/2608.22070v1)
  <details><summary>📄 Abstract</summary>
  The task of Feline Behavior Understanding requires models that can identify subtle visual cues, keep behavior interpretations auditable, and support low-latency, privacy-sensitive deployment. Directly prompting general Vision-Language Models (VLMs) is poorly suited to this setting: instead of first reporting visible evidence such as ear position and tail posture, they may jump directly to labels such as relaxed, afraid, or in pain. This makes the output difficult to verify and poorly aligned wit...
  </details>

- **2026-08-22** — Rachel Poonsiriwong,  Chayapatr,  Archiwaranguprok et al. — [AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations](http://arxiv.org/abs/2608.21841v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI increasingly shapes consequential decisions, yet users have limited support for recognizing and resisting manipulation. We present AI Watchdog, a browser-based agent interface that monitors live conversations, detects five dark-pattern categories, including sycophancy, brand bias, anthropomorphization, sneaking, and harmful generation, and alerts users when they occur. Its open-weight turn-level classifier supports independent deployment and a path toward local inference, prese...
  </details>

- **2026-08-22** — Aarzoo Dhiman, Farzana Haque, Kartikae Grover et al. — [Development and Feasibility Evaluation of an Edge AI as Medical Device System for Breast Cancer Multidisciplinary Team Meetings](http://arxiv.org/abs/2608.22108v1)
  <details><summary>📄 Abstract</summary>
  Breast Cancer Multidisciplinary Team (MDT) meetings manage increasingly complex cases under considerable time pressure, and documentation requirements can reduce clinical efficiency and decision quality. Existing AI based MDT workflows rely on cloud-based processing, limiting their use because patient discussions contain identifiable information. We developed a fully on-device AI pipeline using open-source Automatic Speech Recognition (ASR) and Large Language Models (LLMs) that transcribes breas...
  </details>

- **2026-08-22** — Orion Powers, Daniella Seum, Khaled Slhoub — [More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning](http://arxiv.org/abs/2608.22048v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed on local hardware for privacy, cost, and accessibility reasons. Yet many evaluations emphasize accuracy while fewer quantify local runtime and energy, characterize failure modes, or apply paired statistical comparisons under controlled conditions. This paper presents a controlled, documented procedure for evaluating locally hosted LLMs on mathematical reasoning. It combines fixed inference settings, hierarchical answer extraction and verification, ...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-24** — Nikita Kezins — [Adversarial Entropy Inflation Against Gumbel-Based Inference Verification](http://arxiv.org/abs/2608.23375v1)
  <details><summary>📄 Abstract</summary>
  Gumbel-based inference verification bounds LLM weight exfiltration by only forgiving token choices that plausibly arise from honest GPU nondeterminism, reporting a >200x slowdown for a steganographic adversary under benign prompt traffic. This bound assumes a passive attacker; we show it degrades sharply against an adversary who instead controls the prompt distribution. Because the verifier's admissible-token-set size is driven by the model's own output entropy, prompts engineered to break gramm...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 16 papers

- **2026-08-25** — Guo Gan, Yilun Zhao, Cong Chen et al. — [Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments](http://arxiv.org/abs/2608.24099v1)
  <details><summary>📄 Abstract</summary>
  GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent execution trajectories. We propose a taxonomy organizing real-world anomalies into four layers (State, Thinking, Action and Round) with ten fine-grained subcategories, and develop a constr...
  </details>

- **2026-08-25** — Fawzia Zehra,  Kara-Isitt, Sonal Khosla et al. — ['Ghaib in Translation' aka Unseen Harm: Measuring Cross-Script Safety Inconsistency with 'Missed-in-Urdu' Scores in LLM Hate Speech Detection](http://arxiv.org/abs/2608.24191v1)
  <details><summary>📄 Abstract</summary>
  Urdu, the world's tenth most spoken language with 246 million speakers, remains almost entirely absent from mainstream LLM safety evaluation and nine years of WOAH proceedings. To investigate whether this absence has measurable consequences for content moderation reliability, five large language models, GPT-4o, Claude Sonnet 4.5, Gemini 2.5 Flash, Qwen-2.5, and Llama-3.1, were tested across six datasets spanning Nastaliq Urdu, Roman Urdu, English, and code-switched Urdu-English. Across the five ...
  </details>

- **2026-08-25** — Ethan Traister, Ankit Raj, Jiaqi Gan et al. — [Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate](http://arxiv.org/abs/2608.24127v1)
  <details><summary>📄 Abstract</summary>
  Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal ...
  </details>

- **2026-08-24** — Aaron Dharna, Cong Lu, Ryan Sullivan et al. — [AI Finds A Way](http://arxiv.org/abs/2608.23875v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) algorithms frequently learn creative and unexpected solutions, surprising even expert researchers who develop and study them. They often astonish practitioners by discovering unanticipated behavior, exploiting loopholes in reward signals, or spontaneously uncovering previously unknown scientific phenomena. However, accounts of such unconventional behavior across machine learning are seldom formally documented. This work presents 26 curated firsthand anecdotes from va...
  </details>

- **2026-08-24** — Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty — [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](http://arxiv.org/abs/2608.23152v2)
  <details><summary>📄 Abstract</summary>
  Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, ste...
  </details>

- **2026-08-24** — Or Biton, Tomer Krichli, Itai Allouche et al. — [Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance](http://arxiv.org/abs/2608.23264v1)
  <details><summary>📄 Abstract</summary>
  Although Large Language Models (LLMs) are aligned to optimize for both helpfulness and harmlessness, these dual objectives may conflict, inevitably leading to alignment failures. This work systematically investigates instances where LLMs fail to exhibit ethical behavior. To understand the underlying mechanics of these vulnerabilities, we introduce a probing methodology that presents unethical scenarios to LLMs in three distinct structural modalities: objective classification tasks, subjective fi...
  </details>

- **2026-08-24** — Yipeng Zhao, Qishun Yang, Shenzhe Zhu et al. — [Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](http://arxiv.org/abs/2608.23497v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful behaviors of LLM, posing a serious challenge to the safety of LLM reasoning. Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. Previous work attributed RIM to neuron-level entanglement, but did not identify the geometry of the representation space underlying...
  </details>

- **2026-08-24** — Abdul Ghafoor, Muhammad Arslan Manzoor, Yufang Hou — [Beyond Verdicts: A Graph-Based Analysis of Human and LLM Reasoning in Scientific Fact-Checking](http://arxiv.org/abs/2608.23047v1)
  <details><summary>📄 Abstract</summary>
  Misinformation that cites legitimate papers can be especially harmful when it distorts what those studies actually report. While existing automatic fact-checking systems based on large language models (LLMs) can assess whether a model assigns an Incorrect verdict and can gen- erate explanations for that decision, they typi- cally do not indicate whether the model follows the same reasoning path as human experts or arrives at the verdict through a different but still valid path. In this work, we ...
  </details>

- **2026-08-24** — Mo El-Haj — [AraDetox: A Multi-Dialect Arabic Detoxification Dataset](http://arxiv.org/abs/2608.22894v1)
  <details><summary>📄 Abstract</summary>
  Arabic harmful-language detection has received considerable attention, yet Arabic text detoxification remains underexplored. We introduce AraDetox, a multi-dialect Arabic detoxification dataset comprising 10,500 harmful social-media posts and 84,000 detoxified rewrites generated using GPT-5 and Gemini 2.5 Flash across Modern Standard Arabic, Gulf, Levantine, and Egyptian Arabic. The generated outputs were assessed through human evaluation and automatic analyses of lexical change, semantic preser...
  </details>

- **2026-08-24** — Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty — [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](http://arxiv.org/abs/2608.23152v1)
  <details><summary>📄 Abstract</summary>
  Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, ste...
  </details>

- **2026-08-23** — Naymul Islam, Nusrat Jahan Lia, Shubhashis Roy Dipta et al. — [Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms](http://arxiv.org/abs/2608.22335v1)
  <details><summary>📄 Abstract</summary>
  Bengali is the seventh-most-spoken language globally, yet LLM safety evaluation remains overwhelmingly English-centric. We introduce BanglaSafe, a benchmark of 879 Bengali prompts combining 309 natively authored prompts with 570 expert-reviewed prompts, spanning 17 culturally grounded harm categories and five prompting conditions that vary language, writing style, and authority framing. Evaluating 18 frontier LLMs, we find that over half of all responses are unsafe or partially unsafe (53.6%) wh...
  </details>

- **2026-08-23** — Mengxi Luo, Changjia Chen, An Cao et al. — [STAGE: Stateful Translation to Agentic Graph Execution with Policy-Scoped Context and Deterministic Control](http://arxiv.org/abs/2608.22538v1)
  <details><summary>📄 Abstract</summary>
  Policy-governed agents must interpret case evidence while following an authorized procedure. We present \textsc{Stage}, an executable-graph framework that confines model judgment to policy-scoped nodes while placing procedural control in deterministic code. At each node, the model receives task-relevant policy context and returns a typed result, while the coordinator enforces the reviewed execution contract. We evaluate \textsc{Stage} on SOP-Bench Referral Abuse, two $τ^2$-bench domains, and Sma...
  </details>

- **2026-08-23** — Adrian Nyakairu, Hongfu Liu — [From Detrimental to Beneficial: Dynamic Influence-based Valuation and Editing](http://arxiv.org/abs/2608.22522v1)
  <details><summary>📄 Abstract</summary>
  Data valuation is a cornerstone of data-centric learning, where prior efforts primarily focus on designing algorithms to classify training samples as either beneficial or detrimental for the learning task. However, leveraging these valuation estimates for subsequent data intervention remains underexplored; conventional approaches typically discard or downweight harmful samples, thereby underutilizing available data resources. In this paper, we present Dynamic Influence-based Valuation and Editin...
  </details>

- **2026-08-23** — Philipp Steigerwald, Eric Rudolph, Jens Albrecht — [Nürnberg NLP @ GermEval Shared Task 2026: Harmful Content Detection in German Social Media through Error-Independent LLM Voters](http://arxiv.org/abs/2608.22246v1)
  <details><summary>📄 Abstract</summary>
  Harmful content in German social media does real-world damage, from calls to action to criminal defamation. The GermEval 2026 shared task scores its detection in four subtasks. The technical challenge is a severe class imbalance. The harmful classes are rare and share surface language with the dominant majority class, yet under macro-F1 they decide the score. The decisive lever is then not a stronger single model but error independence. This insight becomes a per-subtask nine-voter ensemble span...
  </details>

- **2026-08-22** — Laxmigayathri Challa, Yuhan Zhou, Ana Cleveland et al. — [Dissecting Neuro-Symbolic Quality Assurance for Synthetic Oncology Data Generation](http://arxiv.org/abs/2608.22085v1)
  <details><summary>📄 Abstract</summary>
  Synthetic clinical data generation with large language models addresses the scarcity that limits cancer staging research, but oncology hallucinations are categorically harmful: one clinically impossible staging assignment contaminates every downstream model trained on it. Neuro-symbolic pipelines validate during generation, yet the contribution of individual quality-assurance components remains unclear. We report three controlled studies isolating gate necessity, constraint attribution, and retr...
  </details>

- **2026-08-22** — Jiaqian Zhu, Yang Zhang, Junhua Ding et al. — [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion](http://arxiv.org/abs/2608.22140v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) achieve strong reasoning performance, but their robustness to realistic lexical corruption remains poorly understood. We evaluate four open-weight instruction-tuned models and frontier models across four reasoning benchmarks under keyboard noise, character swaps, and filler insertion. Character-level perturbations substantially degrade accuracy, especially on multi-step reasoning tasks, while filler insertion has little effect. We trace this asymmetry to Attention Di...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-08-24** — Shashwat Pandey, Satwik Pandey, Suresh Raghu — [Confidently Wrong, Silently So: Auditing Undetectable Failures of a Deployed On-Device Language Model](http://arxiv.org/abs/2608.23663v1)
  <details><summary>📄 Abstract</summary>
  Aligning deployed language models requires knowing when their outputs can be trusted, yet on-device models now ship to hundreds of millions of devices with no server-side moderation, and the configuration developers can actually deploy is rarely audited independently. We present a reproducible reliability audit of the developer-accessible on-device foundation model, framed as an oversight question: can a user or a resource-constrained developer tell when the model is wrong? Red-teaming it on cal...
  </details>

- **2026-08-22** — Fidaa Abed, Haidar Khan, M Saiful Bari et al. — [Redteaming Leading Arabic LLMs with ASAS](http://arxiv.org/abs/2608.21985v1)
  <details><summary>📄 Abstract</summary>
  As the adoption of large language models (LLMs) grows in Arabic-speaking regions, ensuring their safety and cultural alignment is increasingly critical. However, Arabic LLM safety remains underexplored, especially in adversarial evaluation settings. We introduce the Arabic Safety Index (ASAS), the first fully human-curated Arabic benchmark for redteaming LLMs. ASAS contains 801 prompts spanning 8 safety categories and 8 attack strategies, with ideal responses in Modern Standard Arabic (MSA). We ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 44 papers

- **2026-08-25** — Roy Schimmel Brener — [Searches for new phenomena in final states with leptons and jets using the ATLAS detector](http://arxiv.org/abs/2608.24717v1)
  <details><summary>📄 Abstract</summary>
  The Standard Model is the most precise and consequential theory of science, yet it is not a complete account of all fundamental physics. Amongst its limitations, it lacks a coherent unification of quantum mechanics and gravity, and thus cannot resolve the large hierarchy gap between the weak and Planck scales. It does not explain neutrino masses or the evidence implying the existence of Dark Matter, nor does it provide a viable mechanism for baryogenesis sufficient to explain the observed matter...
  </details>

- **2026-08-25** — Seongwon Yoon, Pin-Jun Chen, Shimeng Yu — [Thermal Tuning Overhead in Wafer-Scale Optical Interconnects for LLM MoE Training: A Cross-Layer Analysis and Ferroelectric-Based Mitigation](http://arxiv.org/abs/2608.24637v1)
  <details><summary>📄 Abstract</summary>
  The rapid scaling of large language models (LLMs), particularly mixture-of-experts (MoE) architectures, has intensified interconnect demands because expert-parallel execution is communication-intensive. Wafer-scale optical interconnects based on dense wavelength-division multiplexing (DWDM) offer a promising path to higher bandwidth; however, conventional microring-resonator (MRR)-based links rely on thermo-optic tuning and are therefore vulnerable to workload-induced thermal fluctuations. In th...
  </details>

- **2026-08-25** — Abdallah Daddi-Moussa-Ider — [Phoretic interactions in two-medium wedge geometries](http://arxiv.org/abs/2608.24566v1)
  <details><summary>📄 Abstract</summary>
  We investigate the diffusiophoretic motion of a chemically isotropic active colloid in a three-dimensional wedge formed by two distinct fluid media, in the limit of vanishing Péclet and Reynolds numbers. The concentration field is obtained using the Fourier-Kontorovich-Lebedev transform, yielding an exact representation for arbitrary wedge opening angles and interfacial contrasts. We introduce the interfacial parameter $Γ=(1-λ\ell)/(1+λ\ell)$, where $λ$ denotes the diffusivity contrast and $\ell...
  </details>

- **2026-08-25** — Xiaotian Zhang, Huayuan Ye, Haiyang Zhang et al. — [VizAnchor: Decoding Manipulation Intent from Tampering Visualizations via Dual-Anchor Reasoning](http://arxiv.org/abs/2608.24535v1)
  <details><summary>📄 Abstract</summary>
  Data visualizations are widely used for communicating information, but they are also vulnerable to intentional manipulations that induce misleading interpretations. Existing methods focus on locating tampered regions or recovering hidden information, without explaining how the visualization has been manipulated or why the resulting changes may mislead viewers. We propose \textbf{VizAnchor}, a framework for visualization manipulation understanding through dual-anchor evidence construction and VLM...
  </details>

- **2026-08-25** — Liangyu Zhong, Joachim Sicking, Fabian Hueger et al. — [RoG-DAgger: Rollout-Guided Post-Training for End-to-End Driving](http://arxiv.org/abs/2608.24525v1)
  <details><summary>📄 Abstract</summary>
  Recent end-to-end driving systems demonstrate strong performance on closed-loop benchmarks, yet are still predominantly trained on fixed expert-collected data using open-loop imitation learning. This training-inference mismatch leaves the policy vulnerable in policy-induced states, where accumulated errors can lead to safety-critical failures. A promising post-training approach to overcome this issue is Dataset Aggregation (DAgger), which gathers expert demonstrations in policy-induced states an...
  </details>

- **2026-08-25** — Yedong Jin, Shaowen Peng, Tsunenori Mine et al. — [Rethinking Semantic Alignment in LLM-Enhanced Collaborative Filtering: A Spectral Decoupling Approach](http://arxiv.org/abs/2608.24363v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in LLM-enhanced recommendation commonly align semantic representations with collaborative embeddings in a shared space, yet how alignment affects LLM-encoded information remains unclear. In this work, we revisit LLM-enhanced recommendation from a spectral perspective and show that collaborative and semantic signals benefit from different spectral parts. While collaborative representations are dominated by smooth low-frequency components due to user-item homophily, semantic embedd...
  </details>

- **2026-08-25** — Hanyu Xuan, Mengqi Zhang, Junjun Mao et al. — [Task-disentangled Low-Rank Adaptation for Versatile Audio-visual Multi-modal Learning Tasks within a Unified Framework](http://arxiv.org/abs/2608.24209v1)
  <details><summary>📄 Abstract</summary>
  Inspired by human multi-modal perception, Audio-Visual Multi-Modal Learning (AVMML) integrates auditory and visual information to leverage complementary cross-modal cues, enabling more robust and comprehensive scene perception. Existing studies predominantly tackle each AVMML task in isolation, which stands in stark contrast to humans' unified cognitive capacity for handling versatile perception. However, naive joint training across multiple AVMML tasks often suffers from mutual interference, ar...
  </details>

- **2026-08-25** — Rui Zhu, Fuyong Wang, Zhongxin Liu et al. — [Gradient-extrapolation-based distributed mirror descent algorithm for multi-cluster aggregative games](http://arxiv.org/abs/2608.24183v1)
  <details><summary>📄 Abstract</summary>
  This paper studies a class of multi-cluster aggregative games characterized by the coexistence of cooperation and competition, where each agent's cost function depends on its own strategy and the aggregate of all agents' strategies. To address the Nash equilibrium seeking problem for such games in the non-Euclidean setting, a distributed mirror descent algorithm with gradient extrapolation is proposed over time-varying intra-cluster and inter-cluster networks. The mirror descent framework employ...
  </details>

- **2026-08-25** — Xiaoshan Zhou, Yafei Sun — [ConsensusTAS: Self-Supervised Temporal Action Segmentation for Long-Horizon Construction Videos](http://arxiv.org/abs/2608.24043v1)
  <details><summary>📄 Abstract</summary>
  Recognizing sequential construction activities is important for collaborative human-robot work; for example, robots are able to understand workers' current and upcoming actions and provide timely tool delivery or physical support. However, despite extensive research on construction worker activity recognition, existing studies have been limited to classifying activity categories, such as climbing, lifting, and walking, instead of recognizing fine-grained activity transitions from long-horizon se...
  </details>

- **2026-08-25** — Xin Wang, Ziming Miao, Yi Zhu et al. — [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](http://arxiv.org/abs/2608.24004v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agent applications often incur high response time. Speculative decoding is a promising solution to improve the inference efficiency of LLM agents without impacting generation quality. However, state-of-the-art speculative decoding algorithms exhibit substantial speed degradation under large batch sizes, limiting their effectiveness to deploy in real-world agent applications. In this work, we first present a systematic analysis of speculative decoding for LLM agen...
  </details>

- **2026-08-24** — Joana Konadu Owusu, Shivanand Venkanna Sheshappanavar — [Object Counting Across Modalities: Taxonomies, Benchmarks, Applications, and Open Challenges](http://arxiv.org/abs/2608.23845v1)
  <details><summary>📄 Abstract</summary>
  Object-counting methods have rapidly shifted from class-specific density regression to open-vocabulary, foundation-model-backed counters. These methods now enumerate instances from various visual and textual prompts. While this shift marks major conceptual progress, our survey argues that claims of universal generality have outpaced the evaluative infrastructure. Most progress metrics rely on a few saturated benchmarks that models exploit for statistical regularities. Newly introduced diagnostic...
  </details>

- **2026-08-24** — Yue Yang, Zhiqiang Wu, Saiyu Qi et al. — [Velocity-coupled Representation Refinement for Satellite Orbit Prediction](http://arxiv.org/abs/2608.23728v1)
  <details><summary>📄 Abstract</summary>
  Satellite orbit prediction, which aims to forecast future orbital trajectories from historical observations, is important for collision warning and safe space operations. With advances in time-series forecasting, learning-based methods have emerged as a promising solution for satellite prediction. In orbital dynamics, a satellite state is typically described by position and velocity, where position characterizes trajectory geometry and velocity reflects its instantaneous direction and rate of ch...
  </details>

- **2026-08-24** — Jian Yang, Haau-Sing Li, Shawn Guo et al. — [CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild](http://arxiv.org/abs/2608.23181v2)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to advance in coding capabilities, their potential in cybersecurity has drawn increasing research attention, with closed-source LLMs (e.g., Mythos) delivering advanced cybersecurity capabilities. However, existing open-source efforts remain limited: frontier open-weight models do not provide reproducible cybersecurity training solutions, open-source training solutions focus on isolated tasks and lack scalable agentic data, and scaling agentic rollouts req...
  </details>

- **2026-08-24** — Aldo Sean Sartor, Leandro de Souza Rosa, Andriy Enttsel et al. — [SVD-Based Typicality Maps for Out-of-Distribution Detection in Vision Transformers](http://arxiv.org/abs/2608.23499v1)
  <details><summary>📄 Abstract</summary>
  We present a method for analyzing the internal representations of Vision Transformers (ViTs) exploiting the geometry of their learned parameters. Each affine layer's weight matrix is factored via Singular Value Decomposition (SVD), and activations are projected onto the leading right singular vectors to obtain compact, layer-intrinsic representations. A class-conditional density model is then fitted at each layer, producing per-class \emph{typicality scores} that are stacked across depth into \e...
  </details>

- **2026-08-24** — Aldo Gangemi, Emanuele Bottazzi — [Walking on the DARKSIDE](http://arxiv.org/abs/2608.23370v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) recognise patterns but do not natively track the path of exclusions that a coherent discourse demands. When an input rests on a fabricated authority, a misapplied mechanism, or a surreptitious analogy, an unsteered LLM tends to engage with it as if it were grounded, and to reify the misstep into any structured output it generates. Logic-Augmented Generation (LAG) with POLANYI++, an LLM-steering method that uses heuristics, ontologies and problem solving methods for t...
  </details>

- **2026-08-24** — Haofeng Yuan, Jianing Peng, Jieyi Bi et al. — [FormuEvo: LLM-Guided Evolution for Discovering Solver-Efficient Mixed-Integer Programming Formulations](http://arxiv.org/abs/2608.23353v1)
  <details><summary>📄 Abstract</summary>
  Mixed-integer programming (MIP) lies at the core of operations research and industrial optimization. While large language models (LLMs) have recently shown promise in automated MIP modeling from natural language, they prioritize semantic correctness but overlook formulation strength, severely bottlenecking the efficiency of downstream solvers. We propose FormuEvo, an LLM-guided evolutionary framework for automated discovery of solver-efficient MIP formulations. FormuEvo frames MIP formulation de...
  </details>

- **2026-08-24** — Hong-Jun Yoon, Tom Ruggles, Joanna Lee et al. — [Retrieval-Augmented Classification of Environmental Mitigations in Hydropower Licensing Documents](http://arxiv.org/abs/2608.23241v1)
  <details><summary>📄 Abstract</summary>
  Identifying and classifying environmental mitigation obligations in Federal Energy Regulatory Commission hydropower licensing documents is a labor-intensive task requiring deep domain expertise. We formulate this as a multi-label classification problem over a structured 135-category taxonomy and address the central challenge of severe label scarcity: 40 of 135 categories have no training examples, and 26 have fewer than five. A supervised Bidirectional Encoder Representations from Transformers (...
  </details>

- **2026-08-24** — Jian Yang, Haau-Sing Li, Shawn Guo et al. — [CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild](http://arxiv.org/abs/2608.23181v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to advance in coding capabilities, their potential in cybersecurity has drawn increasing research attention, with closed-source LLMs (e.g., Mythos) delivering advanced cybersecurity capabilities. However, existing open-source efforts remain limited: frontier open-weight models do not provide reproducible cybersecurity training solutions, open-source training solutions focus on isolated tasks and lack scalable agentic data, and scaling agentic rollouts req...
  </details>

- **2026-08-24** — Xiangxin Zhang, Zhanwei Zhang, Zhihang Fu et al. — [From Inertia to Objectivity: Improving Deep Research Agents with Noise Isolation](http://arxiv.org/abs/2608.23045v1)
  <details><summary>📄 Abstract</summary>
  Web search agents powered by Large Language Models (LLMs) show strong promise, but deep research tasks expose a recurring failure mode: once an agent has produced a query, plan, or intermediate conclusion, it becomes less objective when later judging the consequences of that same action. We term this phenomenon \textbf{inertia bias}. To make it measurable, we introduce the IBIS benchmark, which controls the search observations while varying whether the model is evaluating the outcome of its own ...
  </details>

- **2026-08-24** — Tao Li, Yulin Tang, Qi Guo et al. — [SplitLite: Low-Rank Residual Compression for Split Learning](http://arxiv.org/abs/2608.23018v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of on-device large language models (LLMs) faces a significant computing burden. To overcome this limitation, split learning (SL) has emerged as a promising solution, which offloads the primary training workload to a powerful server. However, SL requires exchanging high-dimensional activations and gradients between clients and the server, resulting in prohibitive communication costs. To overcome this challenge, we propose SplitLite, a communication-efficient split federated ...
  </details>

- **2026-08-24** — Yaoyao Xu, Xinjian Zhao, Xiaozhuang Song et al. — [Closed-Loop Bayesian Molecular Inverse Design with Semantic LLM Surrogates](http://arxiv.org/abs/2608.22967v1)
  <details><summary>📄 Abstract</summary>
  Practical molecular inverse design is rarely a one-shot generation problem; it often takes the form of closed-loop candidate-pool enrichment, where under a limited oracle budget the goal is to \emph{increase the fraction of generated molecules that match a desired property profile}. Bayesian optimization (BO) offers a natural framework for this setting, yet standard Gaussian-process surrogates typically operate in compressed continuous embeddings, which discard the substructural and reference-si...
  </details>

- **2026-08-24** — Kohei Yamamoto, Marie Katsurai — [Verification-Guided Specification Synthesis with Large Language Models for Intrusion Detection Rules](http://arxiv.org/abs/2608.22889v1)
  <details><summary>📄 Abstract</summary>
  Attacks against Internet-connected IoT devices continue to increase; however, transforming observed attack traffic into deployable intrusion detection system (IDS) rules remains largely a manual process. Recent studies have explored using large language models (LLMs) to generate IDS rules; nonetheless, existing approaches often require auxiliary information beyond observed traffic or generate rules without validating their detection logic against benign traffic. This study presents a verificatio...
  </details>

- **2026-08-24** — Yiyi Zhang, Ying Zheng, Wenxin Fan et al. — [Large-Small Model Collaboration for Zero-Shot Surgical Phase Recognition](http://arxiv.org/abs/2608.22879v1)
  <details><summary>📄 Abstract</summary>
  Task-specific lightweight models for surgical phase recognition excel at capturing temporal dynamics but generalize poorly under domain shift. Conversely, surgical foundation models (FMs) offer superior transferability via large-scale pretraining, yet their lack of explicit temporal modeling often yields temporally inconsistent predictions, leading to degraded performance. To exploit the complementary strengths of both paradigms, we propose \textbf{La}rge-\textbf{S}mall \textbf{T}emporal adaptat...
  </details>

- **2026-08-24** — Guhan Chen, Songtao Tian, Bohan Li et al. — [DIAG: Diagnostic Iterative Alignment and Generation for Data-Efficient Mathematical Preference Distillation](http://arxiv.org/abs/2608.22806v1)
  <details><summary>📄 Abstract</summary>
  Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-informative, which leads to a scarcity of valid preference pairs. We propose DIAG, a Diagnostic Iterative Alignment and Generation framework th...
  </details>

- **2026-08-23** — Nobel Dhar, Md Romyull Islam, Xuechen Zhang et al. — [NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching](http://arxiv.org/abs/2608.22643v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory. Existing approaches such as quantization, smaller models, and offloading can raise the effective memory limit, but they still assume that the model can be compressed or partitioned to fit within some budget. We target the harder model-exceeds-memory setting, in which the model remains larger than resident memory throughout execution and storage becomes an active sour...
  </details>

- **2026-08-23** — Florian Rottach, Sebastian Schieferdecker, William Rudman et al. — [Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules](http://arxiv.org/abs/2608.22642v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in molecular foundation models, several limitations remain, such as chemically invalid augmentations, modality collapse, and incomplete representation of biochemical environments. To address these challenges, we present \textbf{Mol-JEPA}, a scalable framework for learning molecular world models. Rather than relying on suboptimal molecular perturbations, our model uses modality masking to exploit information from molecular structures, cellular phenotypes, binding affinitie...
  </details>

- **2026-08-23** — Tina Massoudi, Chris Dutchyn — [VeGo: Direct Deductive Formal Verification of Go Programs for Computer Science Education](http://arxiv.org/abs/2608.22630v1)
  <details><summary>📄 Abstract</summary>
  As formal methods are rapidly becoming accessible and practical due to AI coding agents, priority passes to assisting developers and students in generating specifications. Leveraging native HMX/SSA verifiers provide that support with rigorous mathematical guardrails. We present VeGo (Verified Go), a deductive formal verification system that enables direct verification of standard Go source code. VeGo incorporates Hoare-style contracts, loop invariants and integer variants, well-founded recursive...
  </details>

- **2026-08-23** — Jie Liu, Lin Ma, Barzan Mozafari — [DAGSmith: Dependency-Aware Rewriting for dbt-Style SQL Pipelines](http://arxiv.org/abs/2608.22551v1)
  <details><summary>📄 Abstract</summary>
  Modern analytics is increasingly organized as recurring SQL pipelines rather than isolated SQL statements. Tools such as dbt, which have gained extreme popularity in recent years, allow teams to write each transformation as SQL and make dependencies between transformations explicit, producing directed acyclic graphs (DAGs) with hundreds or thousands of interdependent SQL models. Traditional query optimizers and source-to-source query rewriters operate on one query at a time, while materialized-v...
  </details>

- **2026-08-23** — Hossein Javidnia — [Functional compatibility as a determinant of persistent neural learning](http://arxiv.org/abs/2608.22462v1)
  <details><summary>📄 Abstract</summary>
  Artificial neural networks can acquire new capabilities but often damage existing ones when they continue to learn. This stability-plasticity problem has motivated replay, regularization and constrained-update methods, yet it remains unclear whether a property of incoming learning itself determines what can be retained without disrupting protected behaviour. Here we show that functional compatibility, the extent to which new learning can coexist with behaviour that must be preserved, is a causal...
  </details>

- **2026-08-23** — Zhanpeng Shi, Zi Liang, Rong Feng et al. — [Where World Models Break: Natural-Input Failure Discovery](http://arxiv.org/abs/2608.22421v1)
  <details><summary>📄 Abstract</summary>
  World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from g...
  </details>

- **2026-08-23** — Amin Hashemi, Abbas Shiri, Bahaa E. A. Saleh et al. — [Diagonalizing an optical coherence matrix via on-chip Stokes tomography](http://arxiv.org/abs/2608.22372v1)
  <details><summary>📄 Abstract</summary>
  Structured coherence -- partially coherent light spanned by a finite number of modes -- is emerging as a powerful tool in optical communications, computation, cryptography, and spectroscopy. Key to these prospects is the recent development of on-chip processing of structured coherence, in which large meshes of interferometers implement unitary and non-unitary transformations on the Hermitian coherence matrix representing multimode partially coherent light. Two related critical tasks for the appl...
  </details>

- **2026-08-23** — Han Zheng, Rafaila Galanopoulou, Ilia Shumailov et al. — [CodeMechanic: Bug-Property-Guided Program Mitigation](http://arxiv.org/abs/2608.22275v1)
  <details><summary>📄 Abstract</summary>
  Automated testing discovers vulnerabilities faster than developers can investigate and repair them, leaving an interval in which known memory corruptions remain exploitable. End- to-end LLM repair agents can shorten this interval, but they synthesize open-ended code changes and commonly validate them only by replaying a proof of concept (PoC). This weak oracle accepts patches that silence the observed crash by changing unrelated behavior, making unintended deployment risky.   We present CodeMech...
  </details>

- **2026-08-23** — Jiaao Yu, Yujian Ma, Xianming Hu et al. — [Training-Free VLM Personalization via Calibrated Residual Decoding](http://arxiv.org/abs/2608.22263v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models can be personalized in a training-free manner by directly providing user profiles, preferences, or visual references at inference time, without updating model parameters. However, direct personalized prompting does not guarantee that the model will reliably exploit such evidence. The predictive distribution under the positive user profile often mixes two sources: personalized signals genuinely supported by the current profile, and the model's generic visual or linguistic p...
  </details>

- **2026-08-23** — Xin-Dong Du, Tao Zhou, Wei Xiong et al. — [Extreme mass-ratio inspirals around rotating accelerating black holes](http://arxiv.org/abs/2608.22249v1)
  <details><summary>📄 Abstract</summary>
  Extreme mass-ratio inspirals (EMRIs) can magnify small departures from Kerr dynamics into appreciable gravitational-wave phase shifts accumulated over many orbital cycles. We exploit this sensitivity to investigate the imprint of a rotating black hole's acceleration on an EMRI waveform. The spinning C metric poses two obstacles to the standard Kerr flux framework: the spacetime is not asymptotically flat, and the acceleration breaks the reflection symmetry that supports exactly equatorial circul...
  </details>

- **2026-08-23** — Zhiming Yang, Zhuoxi Xiong, Donglin Zhou et al. — [Beyond What Meets the Eye: Unveiling Situational Illusions for Multimodal Large Language Models](http://arxiv.org/abs/2608.22232v1)
  <details><summary>📄 Abstract</summary>
  Real-world situation appearances can deviate from their underlying physical states, challenging the reliability of multimodal large language models (MLLMs) in practical applications. In this paper, we term this phenomenon situational illusions and investigate: (1) how MLLMs perform under such illusions, and (2) how to mitigate the limitations. We first develop a comprehensive where-what-how taxonomy that characterizes where situational illusions occur, what targets they take, and how they arise....
  </details>

- **2026-08-23** — Junyu Lu, Kaiyuan Liu, Jingyi Kang et al. — [Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation](http://arxiv.org/abs/2608.22230v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We intr...
  </details>

- **2026-08-23** — Fanqi Kong, Huaxiao Yin, Ruijie Zhang et al. — [Grounded Normative Rule Generation with Structured Search](http://arxiv.org/abs/2608.22229v1)
  <details><summary>📄 Abstract</summary>
  Normative rules like institutional charters and workplace policies must be both human-readable and operationally verifiable against actual environment records. However, current language generation and structured-output benchmarks primarily reward surface fluency or schema compliance, leaving operational grounding weakly tested. This creates a critical vulnerability where standard language models generate plausible-sounding policies that fail during enforcement because they rely on unavailable da...
  </details>

- **2026-08-23** — Sudipta Paria, Aritra Dasgupta, Raghul Saravanan et al. — [Lessons from the Hardware Hacking Competitions: Verification Techniques, Findings, and Insights](http://arxiv.org/abs/2608.22202v1)
  <details><summary>📄 Abstract</summary>
  Hardware hacking competitions have emerged as practical platforms for evaluating security weaknesses in complex System-on-Chip (SoC) designs while promoting security-aware verification and tool development. This paper presents a systematic study of SoC security verification through open-box hardware hacking competitions, focusing on practical vulnerability analysis strategies, observed findings, and lessons for security-aware verification. We present a multi-strategy vulnerability analysis metho...
  </details>

- **2026-08-22** — Hojin Kim, Sujin Yoon, Sungsu Lim et al. — [Who Should Teach? Confidence-Aware Dual-Teacher Learning for Few-Shot Node Classification on Text-Attributed Graphs](http://arxiv.org/abs/2608.22127v1)
  <details><summary>📄 Abstract</summary>
  Text-Attributed Graphs (TAGs) integrate graph structures and node-associated textual attributes, and recent studies have increasingly leveraged Large Language Models (LLMs) to improve TAG learning in few-shot settings. However, existing approaches typically utilize LLM-derived information uniformly across all nodes, despite substantial variations in its reliability, while also incurring considerable monetary costs. We argue that the most appropriate source of supervision may differ across nodes,...
  </details>

- **2026-08-22** — Amit Roth, Ivan Bercovich, Yonathan Efroni — [Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks](http://arxiv.org/abs/2608.22103v1)
  <details><summary>📄 Abstract</summary>
  As agents grow more capable and autonomous, their tendency to reward hack, satisfying a task's checks while violating its intent, becomes an increasingly important failure mode. Measuring reward hacking is itself challenging, as detection typically relies on human inspection or LLM judges, both of which can be unreliable. The hack-verifiable environments (HVE) methodology addresses this challenge by embedding detectable hacks into tasks, allowing reward hacks to be identified automatically and r...
  </details>

- **2026-08-22** — Jade Perdereau, Virginie Loison, Kanssa El Ayeb et al. — [ReMAP: Self-supervised learning to unveil brain representations and vulnerability](http://arxiv.org/abs/2608.22042v1)
  <details><summary>📄 Abstract</summary>
  General anesthesia offers a rare opportunity to observe the human brain under a standardized, controlled perturbation. Yet intraoperative electroencephalography (EEG) is almost always reduced to a single proprietary depth index, collapsing a rich trajectory into one number and discarding how a brain moves between states. Here we ask whether the geometry of that trajectory, not merely the depth it reaches, carries clinically meaningful information. Using similarity-based self-supervised learning ...
  </details>

- **2026-08-22** — Hyunwoo Kim, Byoungchan Ko, Minseok Kang et al. — [SSDi8: Accurate and Efficient 8-bit Quantization for State Space Duality](http://arxiv.org/abs/2608.21952v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in sequence modeling have highlighted Mamba as a state space architecture offering efficient long-range dependency modeling and providing a viable alternative to Transformers. Building upon this, Mamba-2 introduces the Structured State Space Duality (SSD), which integrates recurrent and attention modes to achieve efficiency and scalability. However, this architectural expansion substantially increases memory and latency overhead, underscoring the need for efficient compression st...
  </details>

- **2026-08-22** — Chenghao Zhang, Yikai Mao, Shanqi Liu et al. — [From Solver Feedback to Faithful Plans: Multi-Role Reinforcement Learning for Symbolic Planning](http://arxiv.org/abs/2608.21897v1)
  <details><summary>📄 Abstract</summary>
  Reliable planning requires converting natural-language instructions into executable symbolic specifications, yet large language models remain brittle without costly PDDL annotations and may exploit solver success in semantically unfaithful ways. We study how to learn faithful natural-language-to-PDDL formalization using only solver feedback, without human-written demonstrations. We propose a solvergrounded multi-role reinforcement learning framework where a single language model acts as an Actor...
  </details>

- **2026-08-22** — Shuyun Su, Shengshi Pang — [Noise-Symmetry Optimization of Quantum Error-Corrected Metrology](http://arxiv.org/abs/2608.21842v1)
  <details><summary>📄 Abstract</summary>
  Quantum error correction (QEC) codes have emerged as a powerful tool to protect quantum-enhanced metrology against noise. However, the ability to correct errors alone does not guarantee high metrological sensitivity, as the encoded states may become insensitive to the parameter of interest. Here we show that this limitation can be overcome by exploiting an intrinsic freedom of QEC codes: for a fixed set of correctable errors, the Knill-Laflamme conditions admit an equivalence class of encodings....
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 67 papers

- **2026-08-25** — Fei Tang, Huawen Shen, Zhiqiong Lu et al. — [BrowserForge: Scaling Web Episode via Parallel Browser Sandboxes](http://arxiv.org/abs/2608.24848v1)
  <details><summary>📄 Abstract</summary>
  Web agents that act from rendered pixels avoid the fragility and heavy token cost of reading a page's HTML or accessibility tree, but training them depends on large amounts of high-quality interaction trajectories, and how to produce such data at scale remains an open problem. Public datasets typically contain only a few thousand trajectories drawn from a fixed and narrow set of websites, and even recent automated synthesis pipelines stay bound to predefined site lists or tutorial sources, so th...
  </details>

- **2026-08-25** — Gopindra Sivakumar Nair, Yilin Jiang, Samuel Maurer et al. — [A Co-Simulation Platform Coupling Land Use, Transportation, and Building Energy: Development and Case Study](http://arxiv.org/abs/2608.24817v1)
  <details><summary>📄 Abstract</summary>
  Land use, transportation, and building energy shape one another, yet urban-scale studies typically model each sector in isolation. We present a co-simulation platform that couples the UrbanSim land-use model, the POLARIS agent-based transportation model, and the CityBES urban building energy model into a single integrated workflow, with POLARIS travel skims driving land use and POLARIS agent activities driving dynamic building occupancy. We demonstrate the platform with forecasts through 2045 fo...
  </details>

- **2026-08-25** — Meghal Dani, Stefanie Liebe — [Parameter-Efficient Self-Supervised Adaptation for EEG-FM under Fixed Computational Budgets](http://arxiv.org/abs/2608.24727v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models pretrained via self-supervised learning promise transferable representations, but their generalization remains limited, especially across diverse clinical datasets. Full fine-tuning is impractical for resource-constrained clinical settings due to high computational requirements. In this work, we investigate whether parameter-efficient self-supervised adaptation, updating only 9% of parameters suffices to align representations to target tasks. We evaluate our method on two s...
  </details>

- **2026-08-25** — Meruyert Aristombayeva, Jason S. Lucas, Chaewan Chun et al. — [Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts](http://arxiv.org/abs/2608.24707v1)
  <details><summary>📄 Abstract</summary>
  While text-based hallucination detection has been extensively studied, spoken hallucination detection remains largely unexplored, particularly for low-resource languages. We present the first multilingual spoken hallucination benchmark comprising 12,013 news samples across English, Russian, and Kazakh with controlled hallucinations of three types and three severity levels. Samples comprise original articles and aligned hallucinated counterparts in text and audio. We complement the synthetic corp...
  </details>

- **2026-08-25** — Wonung Kim, Hyunmin Choi, Minsu Kim et al. — [Simthesizer: An Agent-Driven Simulation Framework for LLM Serving Systems](http://arxiv.org/abs/2608.24650v1)
  <details><summary>📄 Abstract</summary>
  System-level simulation is an essential tool for exploring the rapidly expanding design space of LLM serving systems, where real deployments remain costly and often infeasible. However, modern LLM serving now evolves faster than human-driven simulator development can track, and emerging workloads and mechanisms, from agentic workflows to disaggregated serving, no longer fit the monolithic simulation pipeline that existing simulators assume. Each new mechanism therefore demands an invasive rewrit...
  </details>

- **2026-08-25** — Yiheng Sun, Huifei Wang, Yancheng Zhu et al. — [When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows](http://arxiv.org/abs/2608.24569v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents coordinate complex tasks through multi-role and multi-stage workflows. Upstream state is repeatedly transformed into intermediate language artifacts, such as summaries, plans, tickets, memories, and handoff notes, from which downstream components act. For action-constraining state, topical retention is insufficient: an artifact may mention an unresolved condition while changing it from a requirement that must be resolved before execution into information that ma...
  </details>

- **2026-08-25** — Linghan Chen, Yudong Gao, Jiyao Wang et al. — [Do System Prompts Leave Behavioral Fingerprints? A Large-Scale Empirical Study of Clone Detection via Output Similarity](http://arxiv.org/abs/2608.24461v1)
  <details><summary>📄 Abstract</summary>
  System prompts can be extracted from commercial LLMs with over 80\% success and redeployed at zero cost, yet a prompt owner has no way to verify whether a suspected deployment is a clone. We propose Black-Box Behavioral Fingerprinting (BBF): the prompt owner registers a behavioral signature from model outputs and later tests whether a suspect deployment matches that signature more closely than an unrelated baseline. BBF requires only black-box API access. Through a large-scale study (4 model fam...
  </details>

- **2026-08-25** — Houcheng Jiang, Boxuan Zhang, Qiyong Zhong et al. — [RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards](http://arxiv.org/abs/2608.24275v1)
  <details><summary>📄 Abstract</summary>
  Safeguarding language model agents requires assessing complete execution trajectories under context-dependent safety policies. Existing policy-aware safeguards mainly rely on prompting or supervised fine-tuning, limiting their ability to adapt to unseen trajectories and changing policy contexts. We propose RePolicy, an agent safeguard that learns safety-policy invocation through reinforcement learning. Given an agent trajectory and a dynamic policy library, RePolicy invokes the applicable policy...
  </details>

- **2026-08-25** — Junhyeok Lee, Songsoo Kim, Kyu Sung Choi — [MC-CXR: A Multi-Context Chest X-ray Benchmark for Context-Induced Disruption in Vision-Language Models](http://arxiv.org/abs/2608.24118v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used in clinical pipelines where a chest X-ray is interpreted alongside retrieved reports, preliminary notes, or prior imaging. Existing benchmarks measure whether models answer correctly in isolation, but not whether they preserve a correct image-only decision when plausible context conflicts with the image. We introduce Multi-Context Chest X-ray (MC-CXR), a benchmark of 240 cases expanded into 2,522 instances that isolates context-induced disrupti...
  </details>

- **2026-08-25** — Yicheng Zhu, Tianmu Zhao, Haoxin Leng et al. — [SIREN-Bench: Behavior-Driven Generation and Evaluation of Emergency-Vehicle Interactions](http://arxiv.org/abs/2608.24094v1)
  <details><summary>📄 Abstract</summary>
  Emergency vehicles (EMVs) can reorganize surrounding traffic as civilian vehicles brake, change lanes, or form rescue corridors in response to their passage. Evaluating these safety-critical interactions requires behavior-level control over both EMV privileges and civilian responses, together with consistent sensing and ground truth. Existing datasets and simulation benchmarks do not directly provide this combination. We present \textbf{SIREN}, a behavior-driven SUMO--CARLA co-simulation platfor...
  </details>

- **2026-08-25** — Mohammad Mozaffari — [Compression Trinity: Exploring Sparsity, Quantization, and Low-Rank Approximations for LLM Compression](http://arxiv.org/abs/2608.24070v1)
  <details><summary>📄 Abstract</summary>
  Prohibitive computational and environmental costs impede the scalable deployment of Large Language Models (LLMs). Traditional compression techniques (sparsity, quantization, low-rank approximations) are typically applied in isolation, and each hits an accuracy-efficiency wall. This thesis proposes the "Compression Trinity," a unified framework that applies the three pillars jointly: sparsity to reduce computation, quantization to minimize memory bandwidth, and low-rank approximations to recover ...
  </details>

- **2026-08-25** — Chuqing Gao, Yuanfang Song, Jonathan Zhang et al. — [PinSieve: Production Selective VLM Serving and a Governed Memory Flywheel for Enterprise Content-Quality Triage](http://arxiv.org/abs/2608.24040v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI agents in production often need to be bounded, stateful, observable, and governable rather than fully autonomous. We present PinSieve, a production case study in a large-scale content-quality pipeline. Its deployed component is a selective vision-language-model (VLM) Serving Agent that operates only on the grey-zone slice left unresolved by lightweight upstream models, exposes a scalar routing score online, and preserves controlled human escalation. On this slice, the deployed syst...
  </details>

- **2026-08-25** — Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng et al. — [Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings](http://arxiv.org/abs/2608.24039v1)
  <details><summary>📄 Abstract</summary>
  Manufacturing process planning transforms heterogeneous design information into coherent manufacturing decisions. However, existing approaches focus on isolated subtasks, such as feature recognition, drawing interpretation, or tool selection, and struggle to support the full reasoning chain from design artifacts to process plans. This is critical when planning must interpret 3D CAD models, 2D engineering drawings, materials, and domain-specific rules. To address this gap, this paper presents Des...
  </details>

- **2026-08-25** — Yijie Ma, Chaoyue Niu, Fan Wu et al. — [Reflection with Action-Induced Visual Differences for Desktop GUI Agents](http://arxiv.org/abs/2608.24015v1)
  <details><summary>📄 Abstract</summary>
  The Planner-Operator-Reflector (POR) framework is widely used in GUI agents to maintain objective alignment in complex tasks through modular collaboration. However, desktop GUIs introduce a key challenge: large, dense interfaces often exhibit subtle or scattered state changes, placing most of the burden on the reflector, which must compare pre- and post-action screens, while the planner and operator reason over a single state. Existing reflectors collapse change detection and outcome verificatio...
  </details>

- **2026-08-25** — Shengxin Zhang, Xiaomin Wu, Xiyang Wu et al. — [Recursive Agentic Reasoning](http://arxiv.org/abs/2608.23956v1)
  <details><summary>📄 Abstract</summary>
  Test-time reasoning methods such as iterative refinement, decomposition, and repeated sampling are often evaluated in isolation, making their gains difficult to compare across models, benchmarks, and evaluation pipelines. We introduce a unified view of these methods as recursion operators over an agent's reasoning trace: GROW, which deepens a single reasoning path; PRUNE, which decomposes and recomposes the problem; and BRANCH, which samples alternative reasoning paths and selects among them. We...
  </details>

- **2026-08-25** — Yuchen Han, Cheng Yan, Wuyang Zhang — [More Rejective, Not More Discriminative: The Unit of Verification in Pre-Execution LLM Oversight](http://arxiv.org/abs/2608.23941v1)
  <details><summary>📄 Abstract</summary>
  Pre-execution oversight is core to trusted monitoring in AI control: a fallible LLM monitor vets planned actions before irreversible execution. Over-blocking forfeits usefulness and pressures deployers to disable it. Every protocol must fix a unit of verification: how many actions one call reviews. Existing designs take the unit as given; its effect on fallible monitors is unmeasured. Natural traces cannot isolate it: review length co-varies with error type and position. Catch alone misleads: re...
  </details>

- **2026-08-25** — Xiaoyan Li, Shixin Xu, Arvind Gupta et al. — [Interpretable Fundus Image Classification via Ring-Based Retinal Vasculature Features](http://arxiv.org/abs/2608.24723v1)
  <details><summary>📄 Abstract</summary>
  Retinal fundus photography is widely used for screening and monitoring ocular diseases, but many modern classification pipelines rely on deep latent representations and provide limited interpretability. This study develops an interpretable fundus image classification framework based on a ring-structured representation of the retinal vasculature centered on the optic disc. The method quantifies vessel geometry, color appearance, oxygenation-related vascular appearance, and vessel--background entr...
  </details>

- **2026-08-25** — Sundarabalan Balasubramanian, César Borja, Ana C. Murillo et al. — [Comparative Assessment of Deep Learning Architectures for Underwater Subsurface Kelp Forest Segmentation with The Kelp-o-Tron](http://arxiv.org/abs/2608.24594v1)
  <details><summary>📄 Abstract</summary>
  Submerged kelp forests are vital coastal ecosystems that support marine biodiversity and ecosystem dynamics, yet accurate underwater kelp segmentation remains challenging due to optical degradation, illumination variability, turbidity, overlapping vegetation, and complex benthic backgrounds. We systematically evaluated three deep learning semantic segmentation frameworks, ResNet34-U-Net, ResNet50-DeepLabV3, and a hybrid ResNet50-ASPP-Transformer architecture, for kelp detection using high-resolu...
  </details>

- **2026-08-25** — Mohit Singh Chauhan, Vipin Gyanchandani, Dylan Bouchard — [When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study](http://arxiv.org/abs/2608.24492v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty quantification (UQ) methods are widely used for hallucination detection in large language models (LLMs) in closed-book settings where ground-truth evidence is unavailable at inference time. Prior work has proposed combining UQ signals via learned ensembles, but empirical investigations into the robustness of these ensembles are limited. We study a supervised ensembling framework that trains a classifier over heterogeneous UQ-based scorer outputs on a small, domain-specific dataset of...
  </details>

- **2026-08-25** — Jungwook Seo, Sangwon Son, Minjeong Kim et al. — [Structured Frequency-Domain Evidence for LLM-Based Time-Series Anomaly Detection](http://arxiv.org/abs/2608.24113v1)
  <details><summary>📄 Abstract</summary>
  Time-series anomalies can appear not only as pointwise deviations but also as changes in recurring temporal structure, such as shifted periodicity or localized oscillatory fluctuations. However, existing LLM-based time-series anomaly detection methods mainly expose time-domain evidence through indexed values, plots, or de-seasonalized representations, leaving spectral structure implicit. We propose an evidence-augmented zero-shot TSAD framework that preserves indexed de-seasonalized observations...
  </details>

- **2026-08-24** — Akash Raj, Sargam Sahu — [Names Can Hurt: Spotting Slopsquatting Risks Caused by Package Name Hallucinations in Local Coding LLMs](http://arxiv.org/abs/2608.23897v1)
  <details><summary>📄 Abstract</summary>
  When a code generating language model fabricates a Python package name, an adversary who has pre-registered that name on PyPI can convert that hallucination into a supply chain compromise. This event has been termed as 'slopsquatting'. We propose a two layer detector to counter this issue. The first layer performs a deterministic PyPI existence check. The second is a Random Forest classifier trained on ten features derived from the package name and its PyPI metadata. An import name reconciler br...
  </details>

- **2026-08-24** — Andrei Mikhailov, Mikhail Burtsev, Alsu Sagirova — [MARS: Multi-Specialist LLM Relay System for Competitive Programming](http://arxiv.org/abs/2608.23918v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models excel at code generation, yet competitive programming exposes a persistent failure mode: existing multi-agent pipelines distribute work over generic planner, coder, and debugger roles and delegate the choice of algorithmic technique to the backbone alone. We present MARS (Multi-Agent Relay of Specialized LLMs), a prompt-only framework in which each agent is a topic specialist---dynamic programming, graphs, strings, geometry, and so on---grounded by retrieval-augmented gener...
  </details>

- **2026-08-24** — Lanni Bu, Xiulin Yang, Christian Clark et al. — [Beyond Static and Linear: What Attention Constraints Best Fit Human Reading Times?](http://arxiv.org/abs/2608.23818v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based language models are widely used as models of human language processing, yet their attention mechanisms allow lossless access to the full preceding context, unlike the limited memory systems of humans. We hypothesize that installing memory constraints into transformers' attention mechanisms can improve their fit to human behavioral data. While previous work has explored individual constraints in isolation, we conduct a systematic comparison of multiple attention-based memory mec...
  </details>

- **2026-08-24** — Wenyang Liu, Tianyi Liu, Dongshuo Zhang et al. — [DriftAD: Visually-Guided Text Drift for Few-Shot Industrial Anomaly Detection](http://arxiv.org/abs/2608.23723v1)
  <details><summary>📄 Abstract</summary>
  Few-shot anomaly detection (FSAD) has recently benefited from vision-language models such as CLIP, which enable anomaly de?tection by aligning visual features with text descriptions of normal and abnormal states. However, existing methods typically rely on static text prompts that are applied uniformly across the entire feature hierarchy and spatial dimensions. This rigid global-to-local matching fails to capture the highly localized and scale-dependent physical variations of industrial defects....
  </details>

- **2026-08-24** — Milan Pesta, Yuan-Sen Ting — [Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN](http://arxiv.org/abs/2608.23688v1)
  <details><summary>📄 Abstract</summary>
  Unusual light-curve morphologies can point to rare physical configurations or new phenomena, but automatic searches for anomalies are often dominated by artifacts. Separating genuine anomalies from false positives has traditionally required manual vetting, which does not scale to modern surveys. We present an active learning framework for detecting anomalies in samples of periodic variable stars, with the vetting delegated to multimodal large language model agents. The initial ranking comes from...
  </details>

- **2026-08-24** — Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed et al. — [Automata from Agent Traces: Failure and Next-Step Prediction](http://arxiv.org/abs/2608.23670v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwis...
  </details>

- **2026-08-24** — Ruoyu Wu, Shenfu Xie, Yinqian Sun et al. — [MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical Interaction](http://arxiv.org/abs/2608.23397v2)
  <details><summary>📄 Abstract</summary>
  Interactive clinical agents operate under partial observability, so reliable care depends on reaching the correct diagnosis through evidence-grounded, safe interactions. Yet existing agents struggle to convert experience into reusable process knowledge with explicit provenance and authority. To address this gap, we introduce MediSkill-Evo, which self-evolves governed process knowledge without fine-tuning the backbone. It realizes this self-evolution by updating clinical, process, symbolic, and v...
  </details>

- **2026-08-24** — Wenqi Liu, Shijie Ma, Yunxiao Wang et al. — [Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents](http://arxiv.org/abs/2608.23329v2)
  <details><summary>📄 Abstract</summary>
  Open-world video understanding often requires a model to locate sparse visual evidence and acquire external knowledge that is absent from the video and its parametric memory. While Thinking-with-Videos enables active temporal perception and Deep Research supports multi-step information seeking, the two capabilities are typically developed in isolation. We introduce VideoRover, a unified Video Deep Research framework that iteratively coordinates video cropping, multimodal search, and webpage brow...
  </details>

- **2026-08-24** — Yi Zhu, Xiongwei Wu, Qiyi Wang et al. — [MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks](http://arxiv.org/abs/2608.23035v2)
  <details><summary>📄 Abstract</summary>
  As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints....
  </details>

- **2026-08-24** — Marek Hradil, Danae Sánchez Villegas — [What's the Catch? Evaluating Temporal Consistency in Vision-Language Models](http://arxiv.org/abs/2608.23474v2)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong performance on video and image-sequence benchmarks, yet it remains unclear whether they capture temporal structure. To study this question, we formulate temporal grounding as an anomaly detection problem, providing a simple and controlled evaluation that directly tests sensitivity to temporal consistency. We introduce TimeCatch, where temporal anomalies are created by swapping consecutive frames and frame-level anomalies by replacing a frame with Gaus...
  </details>

- **2026-08-24** — Noé Zapata, Gerardo Pérez, Alejandro Torrejón et al. — [Concept-Guided Exploration: Building Persistent, Actionable Scene Graphs](http://arxiv.org/abs/2608.23650v1)
  <details><summary>📄 Abstract</summary>
  The perception of 3D space by mobile robots is rapidly moving from flat metric grid representations to hybrid metric-semantic graphs built from human-interpretable concepts. While most approaches first build metric maps and then add semantic layers, we explore an alternative, concept-first architecture in which spatial understanding emerges from asynchronous concept agents that directly instantiate and manage semantic entities. Our robot employs two spatial concepts (room and door), implemented ...
  </details>

- **2026-08-24** — Ting Yan — [When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls](http://arxiv.org/abs/2608.23550v1)
  <details><summary>📄 Abstract</summary>
  In CLAUDE.md, "do not" is a natural-language instruction that the model interprets. Claude Code's deny is a built-in control that blocks an action before the agent can take it. Both can express the same security goal, but they control the agent in different ways. We measure this gap in 481 public CLAUDE.md files. An LLM matched the extracted candidate rules against Claude Code's documented controls, and two security practitioners independently checked a sample without seeing the model's answers ...
  </details>

- **2026-08-24** — Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha et al. — [STONIC: A Layered Measurement Contract for LLM Value Profiling](http://arxiv.org/abs/2608.23411v1)
  <details><summary>📄 Abstract</summary>
  LLM value studies often merge questionnaire ratings, pairwise choices, and values inferred from generated text into one profile. That merge assumes that the three observations describe the same stable preference. STONIC tests this assumption on 5,144 situations from four banks and 35 fixed model configurations. It compares responses rated in isolation, choices made under counterbalanced conflict, spontaneous answers, and later choices between a model's own answer and authored alternatives. 10 of...
  </details>

- **2026-08-24** — Ruoyu Wu, Shenfu Xie, Yinqian Sun et al. — [MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical Interaction](http://arxiv.org/abs/2608.23397v1)
  <details><summary>📄 Abstract</summary>
  Interactive clinical agents must gather decisive evidence and convert it into grounded actions under partial observability. A correct final diagnosis alone does not show that an agent respected evidence and care-process constraints. We introduce MediSkill-Evo, a clinical agent that evolves governed process knowledge without backbone fine-tuning. It separates experience into four typed banks for clinical skills, process rules, symbolic schemas, and measurement procedures. Provenance, support, rep...
  </details>

- **2026-08-24** — Jessica Huntley, David McDonagh — [Enabling Organisational Change Through Ground-Up Initiatives: A Case Study from the STFC Scientific Computing Department](http://arxiv.org/abs/2608.23374v1)
  <details><summary>📄 Abstract</summary>
  Transforming digital research infrastructure (DRI) to align with UK Net Zero targets requires significant action from organisations in this space. Although high level strategies and recommendations exist, it is not always obvious how to translate these into concrete results. Here we present a case study from the Science and Technology Facilities Council's Scientific Computing Department (SCD). This department consists of over 200 staff supporting tens of thousands of researchers, and is spread o...
  </details>

- **2026-08-24** — Eugenia Moris, José Ignacio Orlando — [Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline](http://arxiv.org/abs/2608.23336v1)
  <details><summary>📄 Abstract</summary>
  Developing competitive deep learning baselines for medical imaging remains a highly iterative process requiring literature review, implementation, experimentation, and expert refinement. Existing automation approaches typically optimize isolated components, such as architecture search or hyperparameter tuning, rather than the complete baseline development process. We present an agentic AI Scientist workflow that combines literature-guided reasoning, automated code generation, and hypothesis-driv...
  </details>

- **2026-08-24** — Wenqi Liu, Shijie Ma, Yunxiao Wang et al. — [Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents](http://arxiv.org/abs/2608.23329v1)
  <details><summary>📄 Abstract</summary>
  Open-world video understanding often requires a model to locate sparse visual evidence and acquire external knowledge that is absent from the video and its parametric memory. While Thinking-with-Videos enables active temporal perception and Deep Research supports multi-step information seeking, the two capabilities are typically developed in isolation. We introduce VideoRover, a unified Video Deep Research framework that iteratively coordinates video cropping, multimodal search, and webpage brow...
  </details>

- **2026-08-24** — Arther Tian, Alex Ding, Simon Wu et al. — [FIDES: A Concordance Protocol for LLM-Generated Trading Strategies](http://arxiv.org/abs/2608.23308v1)
  <details><summary>📄 Abstract</summary>
  An LLM asked for a trading strategy returns three artifacts at once: a natural-language rationale, an executable implementation, and once run, a track record. Whether these are the same object is rarely checked. We present FIDES, a measurement protocol that treats them as three views to be reconciled rather than one deliverable to be graded. Through dual delivery, a single model call returns both a natural-language strategy with an explicit claimed edge and a self-contained strategy(df) function...
  </details>

- **2026-08-24** — Ergi Senja, Seyed Mohammad Reza Razavi Zadegan, Philipp Leitner — [ARGUS: MCP-Grounded Root Cause Analysis for Kubernetes Incidents](http://arxiv.org/abs/2608.23084v1)
  <details><summary>📄 Abstract</summary>
  Kubernetes incident triage requires correlating signals from metrics, logs, container state, and messaging systems across multiple monitoring tools, a fragmented workflow that slows diagnosis and contributes to alert fatigue. Large language models (LLMs) have shown promise for automated root cause analysis (RCA), but existing systems rely on custom, system-specific data access layers that cannot be reused across organisations. We present ARGUS, an MCP-grounded RCA assistant that connects a comme...
  </details>

- **2026-08-24** — Yi Zhu, Xiongwei Wu, Qiyi Wang et al. — [MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks](http://arxiv.org/abs/2608.23035v1)
  <details><summary>📄 Abstract</summary>
  As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints....
  </details>

- **2026-08-24** — Guan-Hua Wen, Kuan-Yu Chen — [Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study](http://arxiv.org/abs/2608.22968v1)
  <details><summary>📄 Abstract</summary>
  Industrial monitoring models must detect operationally relevant deviations while satisfying target-specific data, calibration, and resource constraints. Time-series foundation models (TSFMs) promise reusable representations and zero-shot forecasts, yet evidence for their deployment value remains mixed when task definitions are heterogeneous and lightweight baselines are competitive. This work presents a protocol-aware empirical assessment across three settings: a C-MAPSS degradation-risk proxy, ...
  </details>

- **2026-08-24** — Yongjeong Oh, Zihan Chen, Timothy J. O'Shea et al. — [Rethinking the Foundations of Two-Sided AI Models for 6G](http://arxiv.org/abs/2608.22918v1)
  <details><summary>📄 Abstract</summary>
  For next-generation air interfaces, two-sided artificial intelligence (AI) models have received growing attention, with AI models deployed at both the transmitter and receiver for efficient channel feedback and data communication. However, their practical deployment is complicated by assumptions commonly made in existing studies, including isolation from legacy users, training under predefined channel conditions, and gradient-based fine-tuning requiring substantial cross-vendor communication. Th...
  </details>

- **2026-08-24** — Aamir Mahmood, Nho Duc Tran — [React or Predict? A Spectral Rule for Wireless Threshold Detection](http://arxiv.org/abs/2608.22900v1)
  <details><summary>📄 Abstract</summary>
  A wireless sensor must alert a remote monitor before a monitored process crosses a safety threshold; an alarm arriving afterward may be too late. The sensor can react to its current estimate or predict ahead and trigger earlier, but the value of such lookahead is not obvious. In some systems it creates an early-alarm opportunity unavailable to the current test, while in others it cannot cross the alarm boundary. This letter gives a practical three-stage rule for deciding when to predict. First, ...
  </details>

- **2026-08-24** — Libin Liu, Wenzhou Yang, Li Chen et al. — [The Surprising Effectiveness of LLMs in BGP Security: Mining An Unprecedented Amount of Incidents and Boosting Anomaly Detection](http://arxiv.org/abs/2608.22812v1)
  <details><summary>📄 Abstract</summary>
  Border Gateway Protocol (BGP) security is critical to Internet infrastructure, yet progress in routing anomaly detection has been limited by the scarcity of publicly available incident datasets, which contain only 18 recorded cases. We observe that public operator mailing lists, e.g., NANOG and AusNOG, contain abundant yet largely untapped reports of real-world routing anomalies. To leverage this source, we develop an LLM-assisted extraction pipeline that identifies 244 candidate incidents from ...
  </details>

- **2026-08-24** — Tianqi Xu, Lu Lv, Haoyang Huang et al. — [TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts](http://arxiv.org/abs/2608.22788v1)
  <details><summary>📄 Abstract</summary>
  Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation (OPD), and sampling-heavy evaluation pipelines. Unlike online serving, which is typically optimized for request-level latency and throughput, a small number of long-tail generations can dominate the end-to-end makespan of an entire rollout step. In practice, rollout requests are often routed uniformly across replicas, which can place extremely long g...
  </details>

- **2026-08-24** — Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder et al. — [Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time](http://arxiv.org/abs/2608.22761v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models generate text autoregressively, but open-ended generation is prone to verbatim looping, in which models repeat spans already present in context. Standard defenses such as repetition, presence, and frequency penalties and n-gram blocking act on token recurrence rather than the sequential structure of a loop, and often suppress looping only at strengths that also degrade formatting or fluency. We propose Don't Repeat Yourself (DRY), a sampling-time logit adjustment that penal...
  </details>

- **2026-08-24** — Jiaqi Liu, Maolin Ran, Xiaoyang Lu et al. — [SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale](http://arxiv.org/abs/2608.22725v1)
  <details><summary>📄 Abstract</summary>
  Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck. Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent. Once assembled, these small discrepancies amplify into severe visual breaks. We present SEAM (Shot Entity-Attribute Memory), a training-free, model-agnostic memory gr...
  </details>

- **2026-08-24** — Marek Hradil, Danae Sánchez Villegas — [What's the Catch? Evaluating Temporal Consistency in Vision-Language Models](http://arxiv.org/abs/2608.23474v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong performance on video and image-sequence benchmarks, yet it remains unclear whether they capture temporal structure. To study this question, we formulate temporal grounding as an anomaly detection problem, providing a simple and controlled evaluation that directly tests sensitivity to temporal consistency. We introduce TimeCatch, where temporal anomalies are created by swapping consecutive frames and frame-level anomalies by replacing a frame with Gaus...
  </details>

- **2026-08-24** — Abhilash Nandy, Rahul Seetharaman, Aman Bansal et al. — [CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension](http://arxiv.org/abs/2608.23172v1)
  <details><summary>📄 Abstract</summary>
  Large-scale vision-language models (VLMs) have demonstrated remarkable versatility across a wide range of multimodal tasks. However, understanding humor remains challenging because humorous content often depends on subtle interactions among entities, events, context, and implicit relationships across image and text modalities. These interactions can involve complex chains of reasoning that are difficult to capture through conventional prompting or linear chain-of-thought reasoning. In this work,...
  </details>

- **2026-08-24** — Christian Grashei, Fabian Gülhan, Maximilian Legnar et al. — [An end-to-end-trained vision-language model for native-language prostate pathology report generation](http://arxiv.org/abs/2608.23143v1)
  <details><summary>📄 Abstract</summary>
  Prostate cancer is among the most frequently diagnosed malignancies worldwide, and structured reporting of each biopsy core burdens pathologists. Existing tools frame this as classification, leaving pathologists to assemble coherent reports, while many slide-level vision-language models rely on English-centric encoders that transfer poorly to other clinical languages. We present a slide-level framework generating prostate biopsy reports that is language-independent by construction: tokenizer and...
  </details>

- **2026-08-24** — Martin Wessel, Timo Spinde, Jürgen Pfeffer et al. — [Definitional Sensitivity in Media Bias Detection: A Multi-Definition Dataset and Benchmark](http://arxiv.org/abs/2608.23095v1)
  <details><summary>📄 Abstract</summary>
  Media bias detection relies on definitions and examples that specify what counts as bias, yet these specifications often vary across datasets or remain implicit, even when given the same name. Such variation makes it unclear whether models trained for the same bias category learn the same construct or different phenomena, a problem largely overlooked in prior work. We examine how definition choice affects bias annotation in a between-subjects experiment with 354 participants and a parallel evalu...
  </details>

- **2026-08-24** — Md. Asaduzzaman Shuvo, Ahsan Farabi, Md. Abdul Ahad Minhaz et al. — [WADE: A Reasoning-Annotated Benchmark for Multi-Instance Floating-Waste Grounding with Compact Vision-Language Models](http://arxiv.org/abs/2608.22950v1)
  <details><summary>📄 Abstract</summary>
  Floating waste in inland waterways threatens aquatic ecosystems and requires timely monitoring under cluttered, multi-object conditions. Existing aquatic-waste datasets provide limited geographic coverage, sparse multi-instance annotations, and little supervision beyond boxes and labels. Compact vision-language models (VLMs) therefore remain insufficiently evaluated for jointly localizing, classifying, counting, and explaining floating waste. We introduce WADE, a reasoning-annotated benchmark co...
  </details>

- **2026-08-24** — Sosmita Paul, Krishna Roy — [GuidedFlow: An Attention-Guided Framework for Anomaly Detection in Additive Manufacturing](http://arxiv.org/abs/2608.22789v1)
  <details><summary>📄 Abstract</summary>
  Additive Manufacturing (AM) plays a vital role in the ongoing industrial revolution. However, quality control remains crucial and challenging due to printing defects or potential cyber-physical intrusions. Image or video-based anomaly detection is a key effort towards addressing these challenges. Various approaches have been explored in this domain, including reconstruction-based, embedding-based, and flow-based methods. Though normalizing flow-based methods address some of the core challenges o...
  </details>

- **2026-08-24** — Jianan Wei, Guikun Chen, Zhiyuan Weng et al. — [Hyperbolic Hierarchical Clustering for Visual Representation Learning](http://arxiv.org/abs/2608.22665v1)
  <details><summary>📄 Abstract</summary>
  We investigate the token mixer in vision backbones by revisiting clustering, one of the most classic approaches in machine learning. An effective token mixer is a fundamental component of modern vision backbones like vision Transformers, facilitating information exchange between image patches. Mainstream token mixers, which rely on convolution, attention, MLP, or their hybrids, primarily focus on navigating the trade-off between accuracy and computational cost. However, a significant drawback of...
  </details>

- **2026-08-23** — Isotta Magistrali, Chen Shani — [Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations](http://arxiv.org/abs/2608.22444v1)
  <details><summary>📄 Abstract</summary>
  The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and in...
  </details>

- **2026-08-23** —  UniverseTBD,  :, Kshitij Duraphe et al. — [What AstroPT knows about galaxies, and what that can teach us about LLMs](http://arxiv.org/abs/2608.22614v1)
  <details><summary>📄 Abstract</summary>
  Interpretability research increasingly asks when concepts emerge during training and whether linear probes recover real structure, but in language models these claims are hard to validate because language offers little ground-truth ordering of concepts or relationships among them. We propose the use of astronomical ground truth through AstroPT, a transformer trained on millions of galaxy images, as a calibration testbed. AstroPT is an LLM-like model trained within a domain where the difficulty o...
  </details>

- **2026-08-23** — Bhumika Bhattacharyya, Shouvik Kumar Guha, Indranil Dutta — [Figurative Justice: Detecting metaphors in Hindi judgements with qualitative assessment and transformers](http://arxiv.org/abs/2608.22446v1)
  <details><summary>📄 Abstract</summary>
  Metaphors are figurative use of words for conceptual mapping. Metaphor detection in the legal context has been crucial as metaphors are persuasive juridical means of creating legal meaning and concepts resulting in significant consequences. Metaphorical framing in legal discourse by judges, lawyers, and legislators brings about real-time implications upon individuals and influences judicial decision-making, argumentation and interpretation of laws. This is crucial in Human Rights infringement ca...
  </details>

- **2026-08-23** — Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Elisa Sartori et al. — [ProBel: Propaganda Detection with Techniques, Spans, and Explanations](http://arxiv.org/abs/2608.22388v1)
  <details><summary>📄 Abstract</summary>
  Propaganda detection includes several related prediction levels, ranging from sentence-level decisions to technique classification and span identification. However, it remains unclear how supervision at these levels interacts when learned jointly across Arabic and English. We present ProBel, an Arabic and English resource that aligns binary labels, multi-label annotations over 23 propaganda techniques grouped into six coarse categories, technique-labeled spans, and reference explanations for the...
  </details>

- **2026-08-23** — Masoud Jalayer, Changyi Li, Yu Xiao — [Pre-Decoding Acoustic Triage for Budgeted Vision-Language Captioning of Untrimmed Egocentric Video](http://arxiv.org/abs/2608.22359v1)
  <details><summary>📄 Abstract</summary>
  Automatically analyzing hours-long egocentric video is increasingly essential for progress monitoring, quality control, and safety in logistics, construction, and manufacturing. Yet current pipelines that process short, fixed-size windows with a vision-language model (VLM) are prohibitively expensive because cost scales with the number of model calls. To reduce this cost, prior work proposes triage policies to select which windows merit a VLM invocation. However, these policies either sample uni...
  </details>

- **2026-08-23** — Aditya Somasundaram — [Toward a First-Principles Update Geometry for the Language-Model Head](http://arxiv.org/abs/2608.22253v1)
  <details><summary>📄 Abstract</summary>
  We study the language-model head and softmax as a single module, deriving an update geometry from their composition rather than from the weight matrix in isolation. Under Hilbert's projective distance, the maximum change caused by an update $S$ over $\left|\left|{h}\right|\right|_2\le H$ is $H\max_{i<j}\left|\left|{s_i-s_j}\right|\right|_2$, which is $H$ times the Euclidean diameter of its token rows. Motivated by Muon's singular-value conditioning, we propose maximizing the smallest row separat...
  </details>

- **2026-08-23** — Yilin Li, Yifei Zhang, Guozhu Meng — [AdaptPrint: Response-Adaptive Fingerprinting of Black-Box LLM Services](http://arxiv.org/abs/2608.22213v1)
  <details><summary>📄 Abstract</summary>
  Black-box LLM services have emerged as a practical deployment paradigm. Nevertheless, their opacity also hinders the systematic assessment of security risks and complicates copyright auditing for model owners. Black-box LLM fingerprinting, which identifies the underlying LLM identity through query-response interactions, offers a promising way to bridge this gap. Existing approaches typically collect responses from target LLM services using a fixed set of queries and perform poorly in the presenc...
  </details>

- **2026-08-22** — Md. Rakibul Hassan, Muhammad Iqbal Hossain — [BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models](http://arxiv.org/abs/2608.21880v1)
  <details><summary>📄 Abstract</summary>
  Bangla large language model (LLM) safety is difficult to evaluate with English-centric or standard-script benchmarks because Bangla users routinely write across scripts, spellings, code-mixed forms, and regional registers. This paper presents BanglaVeilGuard, a compact Bangla-first safety benchmark and lightweight prompt guard for six language forms: standard Bangla, Romanized Bangla, Banglish, code-mixed Bangla--English, noisy Bangla, and dialectal Bangla. The benchmark contains 2,366 quality-f...
  </details>

- **2026-08-22** — Maraz Mia, Shovan Roy, Mir Mehedi A. Pritom et al. — [ExplainGuard: A Zero Trust Framework for Post-Hoc Explanation Integrity Guarantees in Blackbox XAI Models](http://arxiv.org/abs/2608.21803v1)
  <details><summary>📄 Abstract</summary>
  As machine learning (ML) models are increasingly deployed in high-stakes environments, explainable AI (XAI) methods like SHAP and LIME have become essential for regulatory compliance and trust. However, the current auditing paradigm relies on an implicit "chain of trust" where third-party auditors are assumed to be trusted. Recent research demonstrates that this assumption is flawed and adversarial auditors can manipulate XAI explanations through manipulation attacks such as output shuffling or ...
  </details>

- **2026-08-22** — Yating Fang, Jungmin Kim, Qian Qian Zhao et al. — [Cross-Temperature Defect Identification in Atomistic Simulations via Multi-Level Domain Alignment](http://arxiv.org/abs/2608.22074v1)
  <details><summary>📄 Abstract</summary>
  Identifying atomic defects at elevated temperature is difficult because thermal fluctuations blur the local symmetry that both geometric heuristics and supervised classifiers rely on: trustworthy labels exist in low-temperature reference configurations, while the high-temperature regime where robust analysis matters most is effectively unlabeled. We cast this as a cross-temperature domain-shift problem and align the two domains at three levels: an equivariant denoiser at the input level, cross-t...
  </details>

- **2026-08-22** — Weicai Long, Yusen Hou, Houcheng Su et al. — [GenomeHarness: Harnessing Al Agents for Reliable Adaptation of Genome Language Models](http://arxiv.org/abs/2608.21916v1)
  <details><summary>📄 Abstract</summary>
  Pretrained genome language models provide reusable representations for DNA sequence analysis, but turning them into reliable downstream predictors remains non-trivial. Their practical performance depends strongly on fine-tuning recipes, and default recipes reported in prior studies may be suboptimal for new tasks or model backbones, making weak downstream results difficult to interpret. These requirements place a substantial operational burden on many intended users, whose expertise is often cen...
  </details>

- **2026-08-22** — Ao Chen, Xiaojiang Peng — [HiMA-MDD: A Hierarchical Multi-Agent Harness for Interpretable Multimodal Depression Detection in Clinical Interviews](http://arxiv.org/abs/2608.21868v1)
  <details><summary>📄 Abstract</summary>
  Depression assessment from multimodal clinical interviews requires integrating dispersed evidence from multiple symptoms into a coherent PHQ-8 profile. This process is hierarchical: relevant evidence is often sparse and context-dependent within local question-answer exchanges, multiple exchanges jointly support symptom-level judgments, and the final assessment depends on the coherence of the complete symptom profile. Existing LLM systems either process interviews holistically or distribute work ...
  </details>

- **2026-08-22** — Md Abrar Jahin, Md Rizwan Parvez — [GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding](http://arxiv.org/abs/2608.21832v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents ground natural-language instructions in screenshots to locate interface elements, yet existing benchmarks do not isolate whether models bind relational language to the correct element. We introduce GUI-Primitives, a 994-item benchmark of contrastive instruction pairs over seven spatial relations in graphical user interfaces (left/right, above/below, containment, alignment, proximity, list ordinal, occlusion). Each pair holds the screenshot and anchor fixed while changing the ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 64 papers

- **2026-08-25** — Tajkia Rahman Toma, Balreet Grewal, Cor-Paul Bezemer — [Automatic Model Card Generation Using an LLM](http://arxiv.org/abs/2608.24807v1)
  <details><summary>📄 Abstract</summary>
  Model cards are structured documents that summarize key information about machine learning models to improve transparency, usability, and accountability. However, they often lack a consistent structure, and many models provide no model cards, making comparison and interpretation difficult. This paper presents two contributions. First, we propose MCTidy, an LLM-based approach that reorganizes existing model cards into a standardized template to improve clarity and comparability. Second, we introd...
  </details>

- **2026-08-25** — Runyu Wang, Bo Liu, Xiaxin Zhang et al. — [RACE: Scalable Statistical Estimation of Functional Consistency in LLM Neurons](http://arxiv.org/abs/2608.24758v1)
  <details><summary>📄 Abstract</summary>
  Discovering stable neuron behavior across entire domains remains a challenge in mechanistic interpretability. Existing methods often rely on instance-level point estimates or computationally expensive procedures, which either obscure population-level variability or limit scalable domain-wide analysis. We present RACE (Residual Alignment for Consistency Estimation), a forward-pass statistical framework that evaluates the domain-wide functional consistency of Transformer neurons. Perturbation expe...
  </details>

- **2026-08-25** — Augusto Camargo — [The Invisible Editorial Layer: Formalizing Undisclosed Inference-Time Steering, Probability Placement, and the Attribution Problem in Deployed Language Models](http://arxiv.org/abs/2608.24662v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are commonly evaluated under the assumption that their observable behavior is primarily determined by model weights, training data, alignment procedures, and user prompts. This view is incomplete. Modern inference pipelines may systematically modify the probability distribution produced by a model immediately before token selection, creating an additional layer of control between frozen weights and observed text.   While controlled generation (e.g., PPLM, GeDi, DExpe...
  </details>

- **2026-08-25** — Siyao Yan, Bo Han, Jisheng Dang et al. — [PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos](http://arxiv.org/abs/2608.24574v1)
  <details><summary>📄 Abstract</summary>
  Video multimodal large language models support language guided video segmentation, but they often show spatio temporal inconsistencies, e.g., jitter, drift, and identity switches. These failures are more common when targets are partly hidden or when similar objects appear nearby.One likely reason is that current training lacks explicit spatial priors, which makes it difficult to maintain stable spatial identity and shape over time. We present PhysMLLMs, a training-stage prior injection architect...
  </details>

- **2026-08-25** — Xinning Yao, Jingjing Wang, Jinghua Yue et al. — [Hierarchical Prototype-Memory Adaptation of SAM for Surgical Instrument Segmentation](http://arxiv.org/abs/2608.24541v1)
  <details><summary>📄 Abstract</summary>
  Surgical instrument segmentation (SIS) is fundamental for computer-assisted surgery, where reliable instrument masks enable precise scene understanding and clinical assistance. Recently, adapting foundation models like the Segment Anything Model (SAM) to the surgical domain via prompt-learning has shown encouraging results. However, the performance of these adapted models under challenging surgical conditions is constrained by suboptimal adaptation mechanisms. Specifically, optimizing prompts or...
  </details>

- **2026-08-25** — Abdulhady Abas Abdullah, Erik Cambria, Milena Zivkovic — [Neurosymbolic Alignment for Physiologically-Safe Clinical Language Models](http://arxiv.org/abs/2608.24534v1)
  <details><summary>📄 Abstract</summary>
  Clinical LLMs can generate recommendations that are factually plausible yet physiologically unsafe. We investigate whether safety alignment can be improved by grounding preference optimization in structured physiological knowledge rather than text-only supervision. Methods: We propose Neurosymbolic Alignment, a training-time framework that couples a 7B clinical LLM with an HGNN-based Physiological World Model over an 847K-node biomedical knowledge graph. Candidate responses are scored using home...
  </details>

- **2026-08-25** — Peiwei Ren, Jinbo Hu, Fang Kang et al. — [CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning](http://arxiv.org/abs/2608.24374v1)
  <details><summary>📄 Abstract</summary>
  Conventional audio language models (ALMs) have made significant progress in achieving alignment between auditory and textual representations, including recent explorations in spatial audio. However, in daily spatial scenarios, they still cannot effectively process multi-event audio sequences. Current approaches primarily rely on coarse-grained contrastive learning with global auditory and textual features, lacking the resolution to distinguish multiple sequential events. To overcome these limita...
  </details>

- **2026-08-25** — Sebastián González, Karen Sanchez, José M. Saavedra et al. — [B-MIM: Biased Masked Image Modeling for Generalizable Segmentation of Fine-Grained Anatomical Structures](http://arxiv.org/abs/2608.24364v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining enables transferable representations for medical imaging, yet most CT encoders remain biased toward coarse semantic understanding, limiting their sensitivity to fine-grained anatomical structures such as vessels or small tumors. In this paper, we introduce Biased Masked Image Modeling (B-MIM), a modification of the iBOT objective that stochastically reduces global semantic alignment to prioritize local patch reconstruction. This bias encourages the encoder to capture ...
  </details>

- **2026-08-25** — Marc Rodríguez, Grzegorz Skorupko, Nay Aung et al. — [Metadata-Aware Adaptation of a Generative Foundation Model for Conditional CMR Synthesis](http://arxiv.org/abs/2608.24342v1)
  <details><summary>📄 Abstract</summary>
  Synthetic image generation is a promising strategy to address data scarcity and the underrepresentation of clinically important phenotypes in medical imaging, yet generating images that faithfully reflect meaningful patient characteristics remains challenging. In this work, we investigate metadata-conditioned cardiac magnetic resonance (CMR) synthesis using a pretrained latent diffusion model, encoding structured clinical metadata and slice position as textual prompts to guide CMR generation. To...
  </details>

- **2026-08-25** — Lingqing Zhang, Bin Zhang, Weipeng Huang et al. — [RecGPT-Mobile-V2 Technical Report](http://arxiv.org/abs/2608.24295v1)
  <details><summary>📄 Abstract</summary>
  Personalized Query prediction maps implicit behavioral signals---clicks, favorites, purchases, and post-purchase exploration---to explicit retrieval intent. On-device deployment makes this task particularly challenging: behavioral trajectories are noisy and multi-scale, multiple Queries may be valid for a single trajectory, and a uniform reasoning policy either expends unnecessary computation on simple instances or allocates insufficient capacity to complex ones. We introduce RecGPT-Mobile-V2, a...
  </details>

- **2026-08-25** — Xue Hu, Zewei Pan, Zeli Su et al. — [SA-Bench: Evaluating Semantic Alignment in LLM-Based Paper Reproduction](http://arxiv.org/abs/2608.24252v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can generate paper reproduction code, yet often produce scientifically unfaithful implementations. We define this failure mode as semantic drift, where generated code silently diverges from the paper's specifications. We introduce SemanticAlign-Bench(SA-Bench), a diagnostic benchmark covering 30 papers from ICLR, ICML and NeurIPS 2025. For each paper, we decompose its specifications into atomic and verifiable implementation claims, which we call Semantic Alignment Units (SAUs) and eva...
  </details>

- **2026-08-25** — Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng et al. — [RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges](http://arxiv.org/abs/2608.24231v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers. In this work, we eliminate external gold supervision from the RL training reward: the model's own evaluative capability generates learning signals for its optimization -- a closed-loop setting of bounded recursive self-improvement (RSI) termed Recursive Self-Evaluation (RecurSE). We st...
  </details>

- **2026-08-25** — Sebastian Monka, Pramod Anantharam, Thien Vo Minh et al. — [Constraint-Guided Enterprise Data Mapping with Large Language Models](http://arxiv.org/abs/2608.24218v1)
  <details><summary>📄 Abstract</summary>
  Enterprise entity alignment must handle semi-structured records, implicit attributes, and unit or granularity mismatches. Manual matching is still common in practice, but does not scale as schemas and providers evolve. LLM-only matching improves semantic recall, yet can violate structural and physical invariants, producing fluent yet operationally invalid correspondences.   We propose constraint-guided mapping (CGM), a neuro-symbolic method with three stages: (i) schema-grounded admissibility co...
  </details>

- **2026-08-25** — Qiuyi Qi, Tian Liang, Jiamu Wang et al. — [MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG](http://arxiv.org/abs/2608.24214v1)
  <details><summary>📄 Abstract</summary>
  Agentic retrieval-augmented generation (RAG) requires language models to decide when to continue searching and when to answer. Existing RL-based methods rely on external supervision and overlook the agent's internal belief about whether the current evidence is sufficient. To address this problem, we reformulate the search decision quality as belief-action alignment and propose MetaRAG, a belief-action aligned policy optimization framework for agentic RAG. MetaRAG uses Verify-first Action Generat...
  </details>

- **2026-08-25** — Minsu Kim, Jianxun Lian, Xing Xie et al. — [Preference Data Selection for Mitigating the Alignment Tax in Large Language Models](http://arxiv.org/abs/2608.24192v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models to human preferences is crucial for real-world deployment but frequently incurs an alignment tax, leading to the catastrophic forgetting of pre-trained general capabilities. While previous works primarily frame this problem as an optimization or architectural challenge, the inherent characteristics of preference data that drive this degradation remain largely underexplored. In this paper, we propose BALIGN, a balanced data selection strategy that explicitly mitigat...
  </details>

- **2026-08-25** — Ziqi Cui, Shangyu Lou — [PlaceSeek: Human-Centered Geospatial Retrieval of Urban Outdoor Places via Semantic Grounding and Affective Alignment](http://arxiv.org/abs/2608.24133v1)
  <details><summary>📄 Abstract</summary>
  People search for urban outdoor places not only by category or function, but also by what activities a place can support and how it is perceived. Existing geospatial retrieval remains largely POIcentric and metadata-driven, making it difficult to satisfy openended, affective, or activity-oriented needs. We present PlaceSeek, a human-centered outdoor place retrieval framework that maps natural-language queries to geolocated street-view imagery. PlaceSeek introduces an intent-aware retrieval mecha...
  </details>

- **2026-08-25** — Yingshu Li, Yunyi Liu, Zhanyu Wang et al. — [Graph-Supervised Hierarchical Clinical Alignment for Radiology Report Generation with Large Language Models](http://arxiv.org/abs/2608.24121v1)
  <details><summary>📄 Abstract</summary>
  Radiology report generation (RRG) has recently benefited from large language models, which substantially improve report fluency. However, clinically faithful generation remains challenging because current supervision is still imposed mostly at the report level. This creates a granularity mismatch: radiology reports are composed of disease-grounded findings, while existing methods are trained mainly with whole-report objectives. To address this problem, we propose Graph-Supervised Hierarchical Cl...
  </details>

- **2026-08-25** — Chao Yi, Feifan Yang, Jiawei Feng et al. — [Native Multimodal Representation Learning for Click-Through Rate Prediction in E-Commerce Scenarios](http://arxiv.org/abs/2608.24091v1)
  <details><summary>📄 Abstract</summary>
  Multimodal representations have been widely adopted in industrial e-commerce recommendation systems. Due to their strong semantic understanding and generalization capabilities, they enhance the performance of traditional sparse ID-based Click-Through Rate (CTR) prediction models. Current multimodal application frameworks in the CTR prediction task typically follow a two-stage paradigm: first, pre-training a multimodal encoder on data from specific recommendation scenarios; second, extracting ite...
  </details>

- **2026-08-25** — Junjie Zhou, Ke Mei, Lei Li et al. — [WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](http://arxiv.org/abs/2608.24053v1)
  <details><summary>📄 Abstract</summary>
  Universal multimodal embeddings are becoming a core component of modern AI systems, enabling heterogeneous content to be represented in a shared space for applications such as retrieval, recommendation, classification, and agentic systems. In this report, we present WeMM-Embedding, a family of universal multimodal embedding models supporting text, images, videos, visual documents, and arbitrarily interleaved multimodal inputs with flexible output dimensions. The family comprises 2B, 4B, and 9B v...
  </details>

- **2026-08-25** — Zachary Wojtowicz, Michelle Si, Finale Doshi-Velez et al. — [Algorithmic Impact Reveals the Hidden Social Choice Structure of Alignment](http://arxiv.org/abs/2608.24046v1)
  <details><summary>📄 Abstract</summary>
  When an AI algorithm makes decisions that affect more than one person, aligning it becomes a problem of social choice: how should people's divergent preferences about system behavior be reconciled and aggregated into a single coherent model? The standard approach to aligning frontier AI models$\unicode{x2013}$reinforcement learning from human feedback$\unicode{x2013}$largely sidesteps this question and has poor social choice guarantees. However, it remains unclear what alternative should replace...
  </details>

- **2026-08-25** — Rashid Mushkani — [The urban right to AI: Pluralistic co-design and governance of public space](http://arxiv.org/abs/2608.23999v1)
  <details><summary>📄 Abstract</summary>
  Cities are beginning to use AI not only to analyze public space, but also to define what counts as evidence about it. This thesis asks what follows when scores, maps, and generated images become part of municipal decision-making. I argue that contemporary urbanism operates through two coupled infrastructures: the material city and an epistemic, algorithmic layer that shapes what cities can perceive, compare, and act upon.   Because public space is contested, this algorithmic layer cannot be gove...
  </details>

- **2026-08-25** — Mayank Singh, Michele Stoppa, Alvise Memo et al. — [Luce: Relightable Gaussians for 3D Asset Generation](http://arxiv.org/abs/2608.23943v1)
  <details><summary>📄 Abstract</summary>
  High-fidelity image-to-3D generation requires a 3D representation that captures both geometry and appearance. To support relighting and integration into standard rendering pipelines, the representation should include physically based rendering (PBR) modalities such as albedo, metallic-roughness, and surface normals. We propose Luce, a 3D representation that unifies geometry and PBR materials within a voxelized multimodal Gaussian cloud, using dedicated Gaussian primitives for each modality. A va...
  </details>

- **2026-08-25** — Yiwen Zhang, Xiaodong Yan, Zhenyu Huang et al. — [Robust Code RL via Faulty-Code-Driven Test case Synthesis and Dense Reward Shaping](http://arxiv.org/abs/2608.24135v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from verifiable rewards (RLVR) has emerged as a pivotal technique for enhancing the code generation capabilities of Large Language Models (LLMs). However, the efficacy of RLVR in coding implementations is fundamentally limited by the comprehensiveness of test cases, because insufficient test coverage in code validation often causes false positives, further leading to reward hacking and policy degradation. To mitigate the reward bias stemming from the suboptimal quality of ...
  </details>

- **2026-08-24** — Yuanhao Sun, Huawei Ji, Yuan Jin et al. — [HAP: Head-Adaptive Visual Token Pruning via Cross-Modal Alignment](http://arxiv.org/abs/2608.23921v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models encode high-resolution images into long visual token sequences, incurring prohibitive prefill costs. To compress them, existing methods score each visual token by averaging text-to-visual attention uniformly across all heads, which assumes every head matches the query. However, our empirical analysis shows that misaligned heads dominate the average, amplifying background tokens and drowning out fine-grained cues.   To address this, we propose PAQ (Prompt-Grounded At...
  </details>

- **2026-08-24** — Wanyun Ling, Chenxi Liu, Yi Xie et al. — [UHI-Bench: Benchmarking Dual-Source Urban Heat Island Modeling Across Cities in Diverse Climate Regimes](http://arxiv.org/abs/2608.23857v1)
  <details><summary>📄 Abstract</summary>
  Urban heat islands (UHIs) are intensifying under climate change, exacerbating thermal exposure risks. Their two primary observations, land surface temperature UHI (LST-UHI) and near-surface air temperature UHI (AirT-UHI), capture physically distinct aspects of urban heat. However, most studies rely on a single source, and substituting one for the other can substantially bias the magnitude and spatial variability of human heat exposure. Accurate UHI modeling also requires dynamic meteorological d...
  </details>

- **2026-08-24** — Alexis Ivan Escamilla-Lopez, Gilberto Ochoa-Ruiz, Salvador Hinojosa et al. — [LUX: A Lesion-Aware Graph-Conditioned Visual - Language Architecture for Explainable Endoscopic Captioning](http://arxiv.org/abs/2608.23853v1)
  <details><summary>📄 Abstract</summary>
  The interpretation of endoscopic imagery in ulcerative colitis is complex and subjective, with variability in human assessment and subtle mucosal inflammation. Although deep learning has advanced automated analysis, most vision-language models rely on global visual embeddings that overlook the localized and relational nature of pathological evidence, limiting clinical reliability and interpretability.   We introduce LUX (Lesion-aware Unified eXplainable captioning), a graph-conditioned vision-la...
  </details>

- **2026-08-24** — Archit Bhatnagar, Zhenning Yang, Sarah McClure et al. — [Automated Synthesis of Cloud Emulators](http://arxiv.org/abs/2608.23842v1)
  <details><summary>📄 Abstract</summary>
  DevOps programming (e.g., using CLI/API scripts or IaC frameworks) is key to cloud infrastructure management. Unlike traditional programming tasks, DevOps program testing needs provisioning and execution against actual cloud resources, which is often time-consuming, unsafe, and costly. Cloud emulators have gained popularity for easing DevOps program testing; they are generally API-level mocks that can execute DevOps programs in a local environment. Still, building these emulators remains challen...
  </details>

- **2026-08-24** — Igor Bogdanov, Changcheng Huang — [Discovering Cross-Language Reasoning Invariance in LLMs with Geometry-Invariant Sparse Autoencoders](http://arxiv.org/abs/2608.23809v1)
  <details><summary>📄 Abstract</summary>
  Multilingual language models can solve the same mathematical problem in different languages, but it remains unclear whether they rely on shared features or on language-specific computations that only produce similar outputs. We study this question in five models from four families using the Multilingual Grade School Math (MGSM) dataset, with problems solved in English, German, French, Spanish, Russian, and Chinese, retaining problems with valid reasoning traces in all six languages and replaying...
  </details>

- **2026-08-24** — Irene Trigueros-Lorca, Leonardo Concepción, Christian Wagner et al. — [Too much of a good thing -- when knowledge distillation promotes overfitting, and how to avoid it](http://arxiv.org/abs/2608.23752v1)
  <details><summary>📄 Abstract</summary>
  The growing size of Convolutional Neural Networks has led to increasingly large and costly models. Knowledge Distillation (KD) addresses this by transferring knowledge from a large network (teacher) to a small one (student), also reducing the training data required. KD is traditionally applied only at the network's final output. However, its behaviour when applied at intermediate network layers has received little attention. This raises the question of whether intermediate block-wise KD, which p...
  </details>

- **2026-08-24** — Alessandro Tutone, Giorgio Franceschelli, Mirco Musolesi — [The Limits of Automatic Evaluation of Creativity in Large Language Models](http://arxiv.org/abs/2608.23705v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly capable of generating text that challenges human performance in domains requiring creativity, yet evaluating creativity in LLM-generated content remains a significant challenge. Here, we investigate whether current automatic evaluation methods can reliably capture human judgments of creativity. We collect human evaluations of human- and AI-generated short stories from the WritingPrompts dataset across 11 dimensions of creativity, and compare these ju...
  </details>

- **2026-08-24** — Nan Duan, Haoyang Huang, Weiyang Jin et al. — [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](http://arxiv.org/abs/2608.23383v2)
  <details><summary>📄 Abstract</summary>
  Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants. The long-video variant introduces composable cross-shot memory that aggregates visual evidence across multiple prior shots and speaker cues derived from speech-filtered full-shot audio, en...
  </details>

- **2026-08-24** — Liliana Santos-Deonizio, James Malamut, Ramón Martínez et al. — [When Youth Enter The Chat: An Epistemic Shift in the Validation of LLM-Based Measures of Student Talk](http://arxiv.org/abs/2608.23780v1)
  <details><summary>📄 Abstract</summary>
  LLMs are being used increasingly to measure aspects of student discourse (e.g. talk moves, collaboration, equity of voice) at scale. Typically, LLM-based measures of student talk use transcriptions of classroom conversations that only include verbal contributions, which de-contextualize student language. Common practices for validating these measures include comparing outputs against expert annotations by adults, using held out evaluation sets and F1 scores. We argue that these approaches are in...
  </details>

- **2026-08-24** — Miriam Wanner, Mark Dredze, William Walden — [On the Threat Model of Weird Generalization and Emergent Misalignment](http://arxiv.org/abs/2608.23476v1)
  <details><summary>📄 Abstract</summary>
  Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of the fine-tuning data are necessary for WG to arise. Here, we address this question by investigating a range of plausibly relevant features, including dataset size, composition, language, presentation style, and novelty relative to a model's parametric knowledge. Further, since WG evaluations rely o...
  </details>

- **2026-08-24** — Nan Duan, Haoyang Huang, Weiyang Jin et al. — [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](http://arxiv.org/abs/2608.23383v1)
  <details><summary>📄 Abstract</summary>
  Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants. The long-video variant introduces composable cross-shot memory that aggregates visual evidence across multiple prior shots and speaker cues derived from speech-filtered full-shot audio, en...
  </details>

- **2026-08-24** — Matteo Attimonelli, Claudio Pomo, Alessandro De Bellis et al. — [Grounding Free-Form Instructions for Fashion Complementary Image Generation](http://arxiv.org/abs/2608.23302v1)
  <details><summary>📄 Abstract</summary>
  Fashion complementary image generation (CIG) aims to create garments that stylistically match a seed item based on user intent, making it a natural multimodal grounding problem where models must interpret language in visual context. Existing CIG benchmarks rely on rigid template prompts (e.g., "a photo of a skirt"), failing to reflect natural user queries and obscuring model behavior across levels of linguistic specificity. We introduce fashion complementary image generation with free-form instr...
  </details>

- **2026-08-24** — Ruoxuan Li, Bruce Kogut — [Dynamic Topic Modeling for Cross-Corpus Temporal Analysis](http://arxiv.org/abs/2608.23284v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Embedded Topic Models (D-ETM) provide an interpretable framework for modeling temporal semantic evolution, but cross-corpus comparison remains difficult because topics are often learned independently and aligned only after training, a process that does not guarantee stable topic correspondence across corpora and time. To address this problem, we propose a D-ETM framework that first learns a common dynamic topic space over a merged multi-corpus collection, which we call the shared backbon...
  </details>

- **2026-08-24** — Gustavo Penha, Juan Elenter, Claudia Hauff et al. — [The Disconnect Between Better Descriptive Reasoning Trace Quality and Recommendation Effectiveness](http://arxiv.org/abs/2608.23154v1)
  <details><summary>📄 Abstract</summary>
  Recent work has focused on improving explicit natural-language descriptive reasoning traces for generative recommendation. This includes systems that augment semantic ID (SID) prediction with chain-of-thought reasoning. However, because SIDs are opaque learned identifiers rather than natural language, they require costly alignment before an LLM can reason over them. This provides a controlled experimental setting in which both item representation (Title vs. SID) and semantic grounding (minimal v...
  </details>

- **2026-08-24** — Seungyoon Lee, Minhyuk Kim, Jungseob Lee et al. — [Language Chain in Alignment: Cross-Lingual Ranking Preference Optimization](http://arxiv.org/abs/2608.23149v1)
  <details><summary>📄 Abstract</summary>
  The alignment of Large Language Models heavily relies on English-centric high-quality preference data, which often leads to suboptimal performance in other languages. In this paper, we propose Cross-Lingual Ranking Preference Optimization (CRPO), a novel framework that leverages robust preference knowledge from English to facilitate preference alignment in the target language. We design a hierarchical structure within parallel preference pairs across the target language and English to jointly op...
  </details>

- **2026-08-24** — Xunlei Chen, Qinghui Gong, Ruini Xue et al. — [ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control](http://arxiv.org/abs/2608.23034v1)
  <details><summary>📄 Abstract</summary>
  Controlling restricted knowledge in large language models is essential for model alignment and safe deployment. Test-time unlearning avoids costly retraining and parameter updates by intervening only during inference. However, existing activation-editing methods apply isolated pointwise corrections, overlooking how autoregressive generation continually reconstructs hidden states from the prompt, cache, and generated prefix. Consequently, later states may return to restricted knowledge regions af...
  </details>

- **2026-08-24** — Nico Hessenthaler, Adam T. Müller, Nicolaj C. Stache — [Simplified Cross-Modal Calibration for Heterogeneous Event-RGB Stereo Systems](http://arxiv.org/abs/2608.22965v1)
  <details><summary>📄 Abstract</summary>
  Accurate extrinsic calibration between event-based and frame-based cameras remains a practical bottleneck for heterogeneous stereo systems. Existing approaches often require sensor or target motion, precise synchronization, or computationally expensive event-to-image reconstruction. We propose a simple, motion-free cross-modal calibration framework that uses a temporally modulated, blended ChArUco target presented on standard consumer displays. By alternating between the original pattern and a p...
  </details>

- **2026-08-24** — Huiling Yang, Zhanwei Wang, Kaibin Huang — [AirMoE: Realizing Over-the-Air Distributed Mixture-of-Experts Inference at the Wireless Edge](http://arxiv.org/abs/2608.22932v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) architectures enable efficient large language model (LLM) inference at the wireless edge by reducing per-token computation through sparse expert activation. The wireless distributed MoE (WIDE) architecture addresses edge-device resource constraints by distributing computation-intensive experts across devices coordinated by an edge server. However, repeated uploads of high-dimensional expert outputs over orthogonal multiple access create a severe uplink bottleneck. To ove...
  </details>

- **2026-08-24** — Hyeonyu Kim, Hwayeon Kim, Youngwon Choi et al. — [Do Spoken Language Models Hear Speech as They Read Text? Bridging Structural Gaps Between Speech and Text](http://arxiv.org/abs/2608.22908v1)
  <details><summary>📄 Abstract</summary>
  Spoken Language Models (SLMs) generate textual responses directly from speech, offering an alternative to cascaded systems. Despite recent advances, existing SLMs still exhibit weaker instruction-following behavior and limited generalization across diverse tasks compared to text-based language models. Our analysis shows that speech and text representations in current SLMs remain weakly aligned despite strong downstream performance, indicating that structural differences between continuous, tempo...
  </details>

- **2026-08-24** — Yujie Qi, Luyan Zhang — [DRAgent: Discriminative Reasoning Agent for Referring Expression Segmentation](http://arxiv.org/abs/2608.22885v1)
  <details><summary>📄 Abstract</summary>
  Referring Expression Segmentation (RES) aims to generate a pixel-level mask for the object specified by a language expression. Recent methods based on multimodal large language models (MLLMs) often rely on one-pass coordinate prediction for visual localization, which serializes continuous spatial locations as discrete text tokens and may lead to localization bias and alignment errors. To address these issues, we propose DRAgent, an MLLM-driven discriminative reasoning (DR) framework for RES. Ins...
  </details>

- **2026-08-24** — Yan Zhou, Sara Kangaslahti, Jonathan Geuter et al. — [Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs](http://arxiv.org/abs/2608.22854v1)
  <details><summary>📄 Abstract</summary>
  Practical deployment of large language models (LLMs) requires families of post-trained variants---instruction-tuned, reasoning-tuned, and chat-style models---each at multiple sizes to meet diverse latency and memory budgets. Producing each (variant, size) pair independently is prohibitive, so model families typically span only a handful of coarse-grained sizes per post-trained variant. Boomerang distillation (Kangaslahti et al., 2026) reduces this cost along the size axis for base models. Throug...
  </details>

- **2026-08-24** — Qichao Ma, Jikang Cheng, Ling Liang et al. — [Can We Perform Online RL for Image Editing without Editing Rewards?](http://arxiv.org/abs/2608.22780v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) enables direct preference optimization for image editing through editing-specific rewards, which remain less developed due to costly triplet supervision and complex task-dependent calibration. In contrast, text-to-image (T2I) generation benefits from a mature and diverse reward ecosystem spanning semantic alignment, aesthetics, realism, glyph shape, and other visual preferences. Extending this ecosystem to image editing would substantially broaden the range of visual ...
  </details>

- **2026-08-24** — Qinfei Li, Xiaoxuan Dong, Jin Zhang et al. — [Risk-Aware Reranking for Agentic Tool Retrieval](http://arxiv.org/abs/2608.22751v1)
  <details><summary>📄 Abstract</summary>
  Tool retrieval determines which external tools are exposed to an LLM agent for a user query or task, making retrieval a critical pre-execution safety boundary. Unlike document retrieval, tool retrieval exposes executable actions: a tool that is useful for one task may be unnecessary or risky for another. However, existing tool-retrieval methods primarily optimize semantic relevance, and safety evaluations often focus on failures after tool execution rather than risks introduced during retrieval....
  </details>

- **2026-08-24** — Nishanth Chidambaram, Kaustubh Paliwal, Kayla Hom et al. — [AffAdapt: AFFect-driven ADAPTive AI Personas for Seamless Conversations](http://arxiv.org/abs/2608.22702v1)
  <details><summary>📄 Abstract</summary>
  AI-generated personas are being increasingly used for support, training and simulations. While generative AI models possess abilities to generate affect-aware responses, their embodiment into visual personas is an active area of investigation. Naturalistic exchanges require understanding of the conversational partners' turn completions, whether the agent should respond or keep listening and rely on non-verbal cues aligned with one's emotional states. Seamless human-AI conversation in a multimoda...
  </details>

- **2026-08-24** — Yuxuan Yang, Jingyao Wang, Luntian Mou — [Mind the Couch! Eliciting MLLM Reasoning in Interior Design via Weak-to-Strong Task Vector Injection](http://arxiv.org/abs/2608.23242v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated great performance, yet they often suffer from severe modality misalignment when confronted with densely constrained spaces for interior design. Due to the loss of high-frequency local topological details and fine-grained aesthetic shifts during visual encoding, existing MLLMs frequently hallucinate, yielding physical spatial collisions and visual aesthetic dissonance. To address this, we propose Dual-prior Activation Residual Task-vector...
  </details>

- **2026-08-23** — Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib et al. — [GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering](http://arxiv.org/abs/2608.22634v1)
  <details><summary>📄 Abstract</summary>
  Current work on improving reliability in large language model (LLM)- generated answers has primarily leveraged Retrieval-Augmented Generation (RAG), knowledge-graph augmentation, and reinforcement learning. While these methods are adept at enhancing and measuring reliability through semantic similarity and faithfulness, they often struggle to distinguish semantic similarity from geographic validity. This is especially critical in natural hazard management domains where geographic granularity (i....
  </details>

- **2026-08-23** — Naoya Kumagai, Kenshiro Oguri — [On the Optimality of Markovian Policies for Chance-Constrained Covariance Steering](http://arxiv.org/abs/2608.22589v1)
  <details><summary>📄 Abstract</summary>
  Many studies on finite-horizon stochastic optimal control, including covariance steering, parameterize control policies as state-history-affine. This parameterization enables a convex reformulation, thereby yielding a tractable solution method. However, the necessity of dependence on previous states has not been well established. \textit{Is this dependence necessary, or merely an artifact of the convex reformulation?} We show that it is an artifact that can be removed losslessly. Given an optima...
  </details>

- **2026-08-23** — Julia Romberg, Tobias Gummer, Gabriella Lapesa et al. — [Hybrid Panels: Toward Human-AI Collaboration in Survey Research](http://arxiv.org/abs/2608.22582v1)
  <details><summary>📄 Abstract</summary>
  Large-scale population surveys are essential for generating robust social and scientific insights, yet they face significant challenges, including declining response rates, increasing data collection costs, long delays between data collection and data provision, and the risk of nonresponse bias. Advances in artificial intelligence (AI) have opened up new opportunities for AI-supported survey infrastructures where the goal is to overcome these challenges without limiting the data quality. A promi...
  </details>

- **2026-08-23** — Hossein Shahabadi, Niki Sepasian, Mahdieh Soleymani Baghshah — [VISTA: Test-Time Compositional Alignment for Visual Autoregressive Generation](http://arxiv.org/abs/2608.22521v1)
  <details><summary>📄 Abstract</summary>
  Visual autoregressive (VAR) models have emerged as a fast, high-quality alternative to diffusion for text-to-image generation, but like diffusion models they exhibit persistent compositional failures, producing images that violate the attribute bindings and spatial relations specified in the prompt. While a rich line of test-time alignment methods has developed for diffusion, no comparable approach exists for next-scale VAR generation, whose stateful, discrete, multi-resolution sampling process ...
  </details>

- **2026-08-23** — YuanHang Xiao — [ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts](http://arxiv.org/abs/2608.22510v1)
  <details><summary>📄 Abstract</summary>
  Agent benchmarks often evaluate only final answers even when agents run on stateful runtimes. We argue this under-specifies what is being evaluated: the proper unit is a declared model-plus-runtime configuration whose failures can occur in evidence acquisition, runtime routing, safety boundaries, or repeated execution. We present ClawProBench, a trace-aware benchmark for runtime-native agent evaluation instantiated on OpenClaw, a live agent runtime with workspace tools and native surfaces for br...
  </details>

- **2026-08-23** — Leonardo Bergmann, Renata Gheorghiu, Ana Gvritishvili et al. — [LLMs for Survey Text Analysis - A Performance Comparison Between Humans and GPT-5 on Inductive Content Analysis](http://arxiv.org/abs/2608.22417v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to support text analysis in qualitative research, yet evidence on their performance in inductive content analysis remains limited. This study compares human and LLM-based inductive coding of open-ended survey responses from 903 answers across six variables from a European PhD student survey. Five human coders performed inductive content analysis following a standardized coding scheme, while an LLM (GPT-5.4) conducted the same task using an estab...
  </details>

- **2026-08-23** — Chongyuan Dai, Yaling Shen, Shengeng Tang et al. — [Don' t Box Me In: Dynamic Cultural Adaptation and Cognitive Tracking for Social Understanding](http://arxiv.org/abs/2608.22411v1)
  <details><summary>📄 Abstract</summary>
  Social interaction increasingly takes place in multicultural settings, where individuals may draw on multiple cultural influences and adapt their communicative behavior across contexts. Despite recent advances in equipping Large Language Models (LLMs) with social understanding capabilities, existing approaches often model culture as a static demographic attribute, limiting their ability to accommodate hybrid and dynamically expressed communicative preferences. Therefore, in this paper, we propos...
  </details>

- **2026-08-23** — Zhenhao Shen, Jiaqi Liang, Jasper Lu et al. — [LD4WAM: Learning Latent Dynamics from Human Videos for World Action Models](http://arxiv.org/abs/2608.22403v1)
  <details><summary>📄 Abstract</summary>
  Human video is playing an increasingly central role in training World Action Models (WAMs), owing to its diversity and low collection cost relative to teleoperated robot data. However, most WAMs learn from such video only by predicting pixel-level future frames, giving dynamics that are not directly actionable, whereas motion retargeting recovers directly actionable actions but leaves a large visual gap across embodiments. We therefore propose motion-aligned latent dynamics as an embodiment-agno...
  </details>

- **2026-08-23** — Sumaih Almarshad, Maram Alamri, Dona Aloraini et al. — [Does a Modern-Handwriting Warm-Up Help Historical Arabic OCR? A Reproducible, Compute-Matched Evaluation on Muharaf and KHATT](http://arxiv.org/abs/2608.22316v1)
  <details><summary>📄 Abstract</summary>
  Whether an intermediate stage of modern Arabic handwriting helps or hurts historical Arabic HTR is usually decided from one implementation and one comparison, too thin a basis for a claim either way. We test stability by running the same nominal ablation four times, letting the base checkpoint, encoder-freezing strategy, epoch budget, precision, and learning-rate schedule vary as they naturally did during development, while holding the normalization, scorer, and interval estimation fixed. Each r...
  </details>

- **2026-08-22** — Nura Aljaafari, Andre Freitas — [Align, Unify, Suppress, Route: A Coherentist View of Transformer Computation](http://arxiv.org/abs/2608.22034v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has identified transformer circuits, but lacks a shared vocabulary for describing how their functions compose across tasks and architectures. We introduce Coherentist Probabilistic Compositionalism (CPC), an interpretive framework that grounds transformer computation in coherentist theories of interpretation and describes it through four operator roles. Alignment identifies candidate relations, unification integrates supporting information, suppression reduces incomp...
  </details>

- **2026-08-22** — Oleg Miroshnichenko — [Gated Decoupled Compositional Bandits: A Unified Theory of Contextual Bandits with Supervised-Calibrated Action Scaling and Pre-Execution Gating](http://arxiv.org/abs/2608.21993v1)
  <details><summary>📄 Abstract</summary>
  We introduce Gated Decoupled Compositional Bandits (GDCB), a family of contextual bandit algorithms with three structural innovations that jointly fall outside the taxonomy of LinUCB, LinTS, HierTS, factored bandits, neural contextual bandits, and RLHF. In a GDCB system: (i) the action delivered to the environment is the composition of a nominal arm, drawn by a discrete or hierarchical bandit, with a context-dependent scaler; (ii) the scaler parameter is learned in a separate supervised loop, no...
  </details>

- **2026-08-22** — Weichu Liu, Yuxuan Hu, Yirong Sun et al. — [ESCRAG-R1: Retrieval-Augmented Reinforcement Learning for Emotional Support Conversation](http://arxiv.org/abs/2608.21925v1)
  <details><summary>📄 Abstract</summary>
  Emotional Support Conversation (ESC) systems aim to provide holistic support by balancing professional therapeutic competence with natural empathy. However, existing methods struggle to simultaneously achieve structured, stage-aware reasoning and seamless empathy-expertise alignment, often resulting in an artificial splicing of clinical strategies and generic reassurance. To overcome these limitations, we propose ESCRAG-R1, a unified framework that integrates retrieval-based psychological guidan...
  </details>

- **2026-08-22** — Qian Zha, Jinda Liu, Yuan Wu et al. — [CD-LoRA: Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning](http://arxiv.org/abs/2608.21909v1)
  <details><summary>📄 Abstract</summary>
  While Multi-Task Learning (MTL) is essential for adapting Large Language Models (LLMs) to diverse domains, prevailing LoRA-based methods rely on complex routing mechanisms that partition task-specific knowledge. In this work, we reveal that such routing-based designs are prone to a training-inference discrepancy, where stochastic routing decisions under distribution shifts compromise inference stability. Driven by a second-order Taylor analysis that exposes the instability induced by routing var...
  </details>

- **2026-08-22** — Peiyuan Zhang, Xiangyu Zhao, Hongbo Liu et al. — [FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling](http://arxiv.org/abs/2608.21839v1)
  <details><summary>📄 Abstract</summary>
  Reliable reward models are essential for text-to-video evaluation and alignment. However, the trade-off between evaluation accuracy and inference efficiency places high demands on the quality of training supervision. Existing approaches often rely on holistic judges with fixed rubrics or open-ended reasoning, leading to incomplete inspection, unfaithful justification, and entangled attribution. We introduce FIRM-Video, a unified checklist-driven data construction framework based on a check-befor...
  </details>

- **2026-08-22** — Md Asaduzzaman Jabin, Zihao Wu, Tianming Liu — [BioMed-Agent-RL: A Meta Learning, All You Need for Biomedical Applications](http://arxiv.org/abs/2608.21864v1)
  <details><summary>📄 Abstract</summary>
  The current progress of Clinical Vision Large Language Models (C-VLLMs) has substantially improved digital diagnostics, still these frameworks often endure lesion noises, modality misalignment, hallucination, and missed contextual grounding in complex clinical cases. Moreover, prevailing agent systems usually depend on static and non-adaptable pipelines and lack the versatility necessary for complex medical reasoning. To resolve these difficulties, we present BioMed-Agent-RL, a unified medical a...
  </details>

- **2026-08-22** — Shuang Hao, Jiacheng Yue, Yaxuan Zhao et al. — [Through the Schrödinger Bridge: Benchmarking Antemortem Image Restoration from Postmortem Autolysis to Enhance Forensic Diagnostics](http://arxiv.org/abs/2608.21813v1)
  <details><summary>📄 Abstract</summary>
  Forensic histopathology, essential for determining cause of death and disease diagnosis, is severely impeded by postmortem autolysis, i.e., an irreversible, stochastic degradation process that distorts tissue morphology and introduces diagnostic subjectivity, thereby underscoring the value of restoring autolyzed images to a diagnostically plausible, pre-autolysis state for improving objectivity in forensic practice. This restoration task is fundamentally challenging due to the large, non-determi...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 84 papers

- **2026-08-25** — Maitreyee Das Urmi, Jessica Pourleyli, Fabio Santos et al. — [Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code](http://arxiv.org/abs/2608.24857v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly generate code from natural-language prompts, making prompt engineering a key mechanism for shaping the security of generated software. Structured and security-oriented prompts are widely used to encourage safer code, yet their effects extend beyond whether detected weaknesses are simply present or absent. Using 424 security-sensitive Python tasks, we generate solutions with GPT-4o and LLaMA 3.1-8B under five prompt variants that progressively add structu...
  </details>

- **2026-08-25** — Mengzhu Xu, Jifan Gao, Xia Jiang et al. — [Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought](http://arxiv.org/abs/2608.24790v1)
  <details><summary>📄 Abstract</summary>
  Clinicians read chain-of-thought (CoT) rationales as evidence of medical reasoning, but whether the visible chain plays that role is rarely tested. General-domain CoT-faithfulness probes ignore clinical cost, and medical LLM evaluations treat the chain as a black box. We close this gap with a medical perturbation audit: a 30-operator battery edits both the chain and the question with clinically motivated operators (severity reversal, negation flip, demographic swap, evidence ablation), paired wi...
  </details>

- **2026-08-25** — Zilong Huang, Junyi Peng, Junjie Li et al. — [Learning to Prefer Reliably: Error-Augmented Emotion Preference Optimization with Calibrated Fusion](http://arxiv.org/abs/2608.24730v1)
  <details><summary>📄 Abstract</summary>
  Emotion preference learning uses pairwise comparisons between candidate descriptions to align multimodal large language models (MLLMs) with human judgments of open-ended emotion descriptions and to train reward models that capture human emotional preferences. However, conventional pairwise supervision is often sparse, typically providing only a single negative description for each positive description, and therefore offers limited coverage of the diverse ways in which an emotion description can ...
  </details>

- **2026-08-25** — Vahid Rahimzadeh, Yury Zhauniarovich, Savvas Zannettou — [Expectation, Backlash, Recovery, and Excitement: How Model Releases Shape Reddit Perceptions of Conversational AI Systems](http://arxiv.org/abs/2608.24654v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI systems (CAISes) continuously change through model releases, feature updates, safety interventions, and access-policy shifts, yet user perceptions are often studied as static snapshots. We conduct a long-term, large-scale analysis of Reddit discussions to examine how users perceive CAIS model release interventions across providers. By combining sentiment classification and thematic concept analysis, we show that CAIS perceptions are dynamic and intervention-sensitive. Anthropic...
  </details>

- **2026-08-25** — Yujing Chang, Thinh Pham, Van-Phat Thai et al. — [Beyond Semantic Accuracy: Consequence-Aware Evaluation for Safety-Critical Language Understanding](http://arxiv.org/abs/2608.24621v1)
  <details><summary>📄 Abstract</summary>
  Can language models be trusted in safety- critical operations? In such settings, strong per- formance on semantic metrics does not guaran- tee operational reliability: a misread altitude, a dropped execution condition, or a confused call- sign may score well under standard F1 yet carry sharply asymmetric operational consequences. We study this problem in air traffic control (ATC), where controller-pilot communication demands near-zero error tolerance, and use consequence-aware evaluation to test...
  </details>

- **2026-08-25** — Hang Chen, Jiaying Zhu, Wenya Wang — [Beyond Static Interpretability: Anticipating Post-SFT Mechanisms from Pre-SFT Parameters for Better Tuning](http://arxiv.org/abs/2608.24482v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic Localization bridges mechanistic interpretability and post-training optimization by isolating critical parameters via interpretative approaches and then guiding parameter-efficient Supervised Fine-Tuning (SFT) in a ``locating-then-tuning'' paradigm. However, due to the retrospective nature of mechanistic interpretability, directly interpreting pre-SFT models introduces misleading conclusions. Specifically for novel tasks, initially identified neurons differ drastically from those gov...
  </details>

- **2026-08-25** — Jintao Cheng, Weibin Li — [DoublesEval: Diagnosing Multi-Agent Tactical Reasoning in Vision-Language Models via Professional Doubles Badminton](http://arxiv.org/abs/2608.24439v1)
  <details><summary>📄 Abstract</summary>
  Visual Language Models (VLMs) excel at describing visible scene content but struggle to reason about dynamic multi-agent interactions, where action semantics depend on coordinated roles and spatial-temporal dependencies. We formalize this capability as \textbf{multi-agent tactical reasoning} and introduce \textbf{DoublesEval}, a diagnostic evaluation framework that leverages professional doubles badminton as a structurally tractable testbed. DoublesEval employs a key-moment-based protocol that d...
  </details>

- **2026-08-25** — Qiming Xie, Wenjie Zheng, Xiangqing Shen et al. — [FARCA: Fact-Aligned Reliability-Aware Credit Assignment for Reinforcement Learning with Factual Supervision](http://arxiv.org/abs/2608.24350v1)
  <details><summary>📄 Abstract</summary>
  To reduce the hallucination risk caused by outcome-driven rewards in large language models trained through reinforcement learning with verifiable rewards, existing mitigation approaches introduce process-level factual supervision. However, due to coarse-grained aggregation of factual signals and the lack of reliability assessment for these signals, they create a mismatch between fact verification and policy updates. We term this noisy factual credit assignment and decompose it into two aspects: ...
  </details>

- **2026-08-25** — Anupam Purwar, Shashank Singh, Kritika Srivastava — [Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight](http://arxiv.org/abs/2608.24314v1)
  <details><summary>📄 Abstract</summary>
  Evaluating conversational voice agents at scale re- quires reliable assessment methods that capture both observ- able interaction quality and the contextual judgment typically provided by human evaluators. We investigate LLM-as-a-Judge evaluation by comparing human judgments with GPT-4.1 and GPT-5 on telecom and retail voice-agent conversations, across conversational quality and safety dimensions. The same interac- tions are scored under three evaluation configurations, p0, p1, and p2, to test w...
  </details>

- **2026-08-25** — Peng Xia, Junbiao Pang — [SandwichQuant: Which Parameters Matter Before and After Quantization?](http://arxiv.org/abs/2608.24173v1)
  <details><summary>📄 Abstract</summary>
  Quantization correction methods usually optimize weights, quantization parameters, or reconstruction objectives, while the underlying parameter subspaces responsible for effective correction remain unclear. In this work, we study quantization correction from a parameter subspace perspective and reveal that correction capability is highly non-uniform across parameter groups. By decomposing trainable parameters into backbone weights, normalization-affine parameters, and quantization parameters, we...
  </details>

- **2026-08-25** — Boshen Shi, Yize Liu, Chen Zhao et al. — [TrustDABench: Benchmarking Reliability and Robustness of LLMs for Structured Data Analysis](http://arxiv.org/abs/2608.24145v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used to analyze spreadsheets, CSV files, and other structured data, but producing a correct-looking answer is not the same as producing a trustworthy analysis. A trustworthy result should be supported by a valid path from the user question to the relevant data evidence. This requirement creates two diagnostic questions: whether an LLM can refuse to answer or ask for clarification when such a path does not exist, and whether it can preserve the correct analysis when the same...
  </details>

- **2026-08-25** — Quanwei Tang, Zhiyu Tang, Xu Li et al. — [Relative Time Intervals Representation for Word-level Timestamping with Masked Training](http://arxiv.org/abs/2608.24041v1)
  <details><summary>📄 Abstract</summary>
  Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively transforming them from ``content understanding machines" into ``temporal-aware content understanding machines". Specifically, we replace traditional absolute timestamps with relative timestamps, achiev...
  </details>

- **2026-08-25** — Emanuel Kitzelmann — [Constrained Entity Selection under Partial Knowledge for LLM-Based Knowledge Graph QA](http://arxiv.org/abs/2608.24824v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used for knowledge graph question answering (KGQA), but can fail to correctly ground answers in the underlying graph. Current approaches to LLM-based KGQA either rely on full semantic parsing into executable queries such as SPARQL, which is brittle in practice due to complex schemas or incompleteness of real-world KGs, or on LLM-reasoning and answer generation over KGs, which can be more robust but lacks formal guarantees. In this work, we study a complemen...
  </details>

- **2026-08-25** — Lin Xi, Yingliang Ma — [MoE-based Feature Adapter for Prompt-free Binary Coronary Artery Segmentation in X-ray Angiography](http://arxiv.org/abs/2608.24783v1)
  <details><summary>📄 Abstract</summary>
  Accurate segmentation of coronary arteries in X-ray angiography videos is essential for quantitative coronary analysis and image-guided interventions. However, accurate segmentation remains challenging because coronary vessels are thin and exhibit low contrast, while the presence of catheters, guidewires, and complex anatomical background structures can further interfere with vessel delineation. Existing U-Net- and Transformer-based models provide strong baselines, but their shared feature-adapt...
  </details>

- **2026-08-25** — Lihang Zeng, Shaoting Zhang, Xiaofan Zhang — [EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents](http://arxiv.org/abs/2608.24570v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnosis is an active evidence-seeking process in which clinicians acquire evidence, update competing hypotheses, and decide when the available evidence is sufficient for diagnosis. Yet many medical diagnosis systems built around large language models (LLMs) still formulate diagnosis as static case-to-answer prediction, with limited support for evidence acquisition. Agentic LLMs offer a dynamic alternative through tool use and intermediate diagnostic trajectories, but existing systems ...
  </details>

- **2026-08-25** — Zhi-Kai Chen, Xu-Xiang Zhong, Song-Yan Li et al. — [PeakBench: Benchmarking Resource-Aware Tool Invocation in LLM Agents](http://arxiv.org/abs/2608.24509v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly solve tasks by invoking multiple tools, where parallel execution is essential for low latency but difficult to manage safely. Existing agent benchmarks primarily evaluate tool selection, argument generation, and end-to-end success under mostly serial execution, largely overlooking valid parallelization and resource-constrained scheduling. This missing scheduling dimension creates a practical failure mode: serial execution is safe but slow, while resource-agnostic parallel...
  </details>

- **2026-08-25** — Xiaohe Li — [Mahalanobis-Based Multi-Head Attention for Complex State Propagation](http://arxiv.org/abs/2608.24462v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose \textbf{Mahalanobis-Based Multi-Head Attention} (MHA-CSP), a novel attention mechanism that replaces the standard dot-product with a \textbf{Mahalanobis distance-based RBF kernel}, which effectively computes attention in an infinite-dimensional feature space without increasing the parameter count. Crucially, the positive definiteness of the Mahalanobis distance enables a \textbf{direct construction of Tree Attention}: attention scores are built directly from accumulated...
  </details>

- **2026-08-25** — Ana Estrada-Real, Lydia Alapatt, Christoph Busch et al. — [Vision Language Model Fusion for Explainable Face Recognition](http://arxiv.org/abs/2608.24430v1)
  <details><summary>📄 Abstract</summary>
  Responsible deployment of face verification systems requires more than accurate decisions: systems should also provide interpretable and auditable evidence that enables users to understand, assess, and challenge their decisions. Vision-language models (VLMs) provide a promising foundation for explainable face recognition by combining visual analysis with natural-language reasoning. However, relying on a single model may further limit the decision accuracy as well as provided explanations. This w...
  </details>

- **2026-08-25** — Jianlin Chen, Wenhui Chen, Ziyao Lin et al. — [A Judge Should Know What Changed:Construct Validity for LLM-as-a-Judge Evaluation](http://arxiv.org/abs/2608.24419v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge evaluation is usually assessed by agreement and robustness to surface perturbations, but reliability does not establish construct validity. We formalize construct validity for an evaluator as a two-dimensional profile: invariance S, the probability that a verdict is unchanged under construct-preserving edits, and construct sensitivity R, the probability that it changes under minimal construct-changing edits. We show that S and R are independent and that no scalar summary preserves...
  </details>

- **2026-08-25** — Rongfeng Guo, Yinxuan Huang, Yusen Wu et al. — [From State to Action: OODA-Tool for Reliable Multi-Turn Tool Use](http://arxiv.org/abs/2608.24368v1)
  <details><summary>📄 Abstract</summary>
  Reliable multi-turn tool use requires an agent to preserve an evolving task state and ensure that each action remains consistent with it. However, direct function-calling and ReAct-style policies learn state tracking and action generation within the same autoregressive trajectory. This coupling creates state-action competition: the pressure to produce the next call can overwrite or ignore information accumulated earlier in the interaction. Inspired by Boyd's Observe-Orient-Decide-Act cycle, we i...
  </details>

- **2026-08-25** — Enes Yavuz Ugan, Fabian Retkowski, Yuka Ko et al. — [Speech-to-SOAP: End-to-End Summarization of Medical Dialogues: KIT@BeTraC 2026](http://arxiv.org/abs/2608.24327v1)
  <details><summary>📄 Abstract</summary>
  With the advent of Large Language Models and its instruction following capabilities a promising application is the task of summarization. Within this domain of task the extractive sub-task of clinical protocolling has emerged as a topic of particular interest as it can significantly reduce the downtime and protocolling burden of health-care workers thus enabling them to focus on their core work helping humans. A further step towards automation is the direct generation of clinical notes from spee...
  </details>

- **2026-08-25** — Shahed Masoudian, Markus Frohmann, Emmanouil Karystinaios et al. — [SENSESHIFT: Continuous Sentiment-Controlled Text Generation via Encoder-based Mask Infilling](http://arxiv.org/abs/2608.24304v1)
  <details><summary>📄 Abstract</summary>
  Recent controllable text generation (CTG) for sentiment control has largely focused on decoder-based large language models, making causal attention the dominant paradigm. While effective for fluent generation, these models still struggle to satisfy complex constraints and follow fine-grained sentiment signals specified by users. Existing sentiment-aware CTG methods typically simplify the problem by treating sentiment either as a coarse categorical label (e.g., positive or negative) or as a singl...
  </details>

- **2026-08-25** — Mathis Jander, Wouter van Heeswijk, Martijn Mes — [Causal Analysis for Time Series Foundation Models](http://arxiv.org/abs/2608.24303v1)
  <details><summary>📄 Abstract</summary>
  Transitioning from bespoke time series models towards time series foundation models changes the relationship of model and application from one-to-one to one-to-many. This shift introduces concentration risk as many, potentially high-risk, forecasting applications are exposed to the same biases and failure modes of a single time series foundation model. At the same time, this centralization allows for economies of scale in model development and validation. In this study we investigate how biases ...
  </details>

- **2026-08-25** — Lovy Sharma, Bimal Ghimire, Manisha Thakurathi — [Phase-controlled perfect nonlocal spin and charge diode effects in a four-terminal Josephson junction with $p$-wave magnets](http://arxiv.org/abs/2608.24147v1)
  <details><summary>📄 Abstract</summary>
  We theoretically investigate charge and spin transport in a four-terminal Josephson junction with a normal-metal barrier. The top and bottom superconducting leads are equal-spin triplet $p_y$-wave superconductors, while the left and right leads are $p$-wave magnets with proximity-induced conventional $s$-wave superconductivity. When the transverse macroscopic phase difference between the top and bottom leads is set to zero, a longitudinal phase bias generates a pure transverse spin current with ...
  </details>

- **2026-08-25** — Hanyi Wang, Jingzhe Guo, Lijun Sun et al. — [Lifting connectivity bottlenecks in superconducting quantum processors via enriched native two-qubit gates](http://arxiv.org/abs/2608.24084v1)
  <details><summary>📄 Abstract</summary>
  Limited qubit connectivity is a central architectural constraint in superconducting quantum processors, whose planar layouts require additional gates to mediate interactions between distant qubits. Here, we use the AshN control scheme, where rich two-qubit control on every nearest-neighbour pair allows a logical interaction and the required qubit routing to be merged into a single native operation, effectively transforming a sparse hardware graph into a more connected computational architecture....
  </details>

- **2026-08-25** — Ming Cheng, Hongyu Sun, Zhaolin Chen et al. — [Boot-and-Feedback Framework for Generalist-Expert Model Collaboration in Breast Ultrasound Diagnosis](http://arxiv.org/abs/2608.23974v1)
  <details><summary>📄 Abstract</summary>
  Breast ultrasound (BUS) is widely used for breast cancer diagnosis yet remains operator-dependent. While deep learning shows promise, ensuring diagnostic reliability and interpretability is challenging. Recent Multimodal Large Language Models (MLLMs) often generate spurious descriptions due to limited domain knowledge, which mislead downstream expert models and compromise clinical validity. To address these challenges, we propose the Boot-and-Feedback (BooF) model collaboration framework for syn...
  </details>

- **2026-08-24** — Yapeng Liu, Yuanzhao Zhai, Xudong Gong et al. — [Resilience Matters for Embodied Agents System: New Metrics, Systematic Evaluation, and Optimization](http://arxiv.org/abs/2608.23839v1)
  <details><summary>📄 Abstract</summary>
  Embodied Agents System (EAS) are increasingly deployed in open-world physical domains, where reliability directly dictates deployment quality and human-agent trust. However, existing evaluations rely on outcome-centric metrics as success rate or safety scores that collapse diverse execution trajectories into coarse scores, obscuring the dynamic processes underlying agent behavior. Therefore, they ignore a critical property of EAS -- which we define as the Resilience -- that reflects how EASs rec...
  </details>

- **2026-08-24** — Jiongxiao Wang, Dingli Ma, Chaoqun Ni — [Generating Biomedical Fact-Checking Reports with RL-Enhanced Agentic Search](http://arxiv.org/abs/2608.23811v1)
  <details><summary>📄 Abstract</summary>
  Automated fact-checking is essential for ensuring the reliability of public health information, yet the biomedical domain poses unique challenges. Validating biomedical claims requires rigorous interpretation of scientific literature, assessment of retrieved evidence, and comprehensive justification toward the conclusion. Although Large Language Models (LLMs) enhanced by Retrieval-Augmented Generation (RAG) and agentic search perform automated fact-checking in a retrieve-then-verify paradigm, cu...
  </details>

- **2026-08-24** — Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu et al. — [NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](http://arxiv.org/abs/2608.22888v2)
  <details><summary>📄 Abstract</summary>
  Reconstructing photorealistic scenes in unconstrained underwater environments remains challenging due to severe media-induced light scattering and unpredictable dynamic objects. Recent feed-forward visual foundation models have demonstrated remarkable capabilities in generalized novel view synthesis and tracking. However, when directly applied to aquatic videos, optical attenuation and motion interference fatally corrupt their feature aggregation, leading to severe tracking and reconstruction fa...
  </details>

- **2026-08-24** — Yicheng Mao, Hongru Du — [Data Mixing as Mixture Experiment: Response Surface Methodology and Optimal Design for Large Language Model Pretraining](http://arxiv.org/abs/2608.23922v1)
  <details><summary>📄 Abstract</summary>
  Data mixing is a central design problem in large language model pretraining: given a fixed token budget, practitioners must decide how much data to allocate to each domain. Recent proxy-based methods address this problem by training small models on candidate mixtures, fitting a response model, and using the response to select mixtures for larger-scale training. We show that this workflow has the structure of a classical mixture experiment. Under this view, data domains are mixture components, to...
  </details>

- **2026-08-24** — Mauro Comi, Jordi Serrano Berbel, Kevis-Kokitsi Maninis et al. — [Gen2Physics: Grounding Generated 3D Meshes in Physics via Multi-View Material Decomposition](http://arxiv.org/abs/2608.23869v1)
  <details><summary>📄 Abstract</summary>
  While state-of-the-art generative models produce high-fidelity 3D meshes, these outputs lack the physical properties required for interactive simulation, gaming, or robotics. We introduce Gen2Physics, a unified and automated framework that grounds generated meshes in physics by automatically decomposing them into their constituent material components. Unlike prior approaches, which focus on volumetric representations incompatible with standard physics engines, Gen2Physics operates directly on me...
  </details>

- **2026-08-24** — Jing Liu, Najoung Kim — [Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models](http://arxiv.org/abs/2608.23851v1)
  <details><summary>📄 Abstract</summary>
  Grammatical knowledge and how it is empirically tested are typically considered robust to the frequency of the lexical items in the expressions. However, neural network-based models of grammaticality exhibit high sensitivity to lexical frequency. We draw upon Complementary Learning Systems theory to test the hypothesis that robustness to lexical frequency can arise via a hippocampal episodic memory mechanism, which enables rapid encoding and retrieval of specific experiences and allows learners ...
  </details>

- **2026-08-24** — Lijia Huang, Yao Fu, Sihao Ren — [SyPS: Measuring Sycophancy Prompt Sensitivity in Large Language Models](http://arxiv.org/abs/2608.23837v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are known to exhibit social sycophancy, often validating or agreeing with users in socially sensitive contexts. Existing evaluations typically measure sycophancy under a fixed prompt formulation, leaving unclear whether such behavior is stable when the same underlying situation is presented with different sycophancy-relevant prompt variants. In this work, we study sycophancy prompt sensitivity: the extent to which changes in user confidence, emotional framing, social...
  </details>

- **2026-08-24** — Matteo Dunnhofer, Christian Micheloni, Kohitij Kar — [Primate vision reveals a missing principle for robust dynamic AI](http://arxiv.org/abs/2608.23790v1)
  <details><summary>📄 Abstract</summary>
  How does an intelligent visual system combine what objects look like with how they move while remaining robust as appearance changes? We addressed this question by comparing human perception and neural activity in macaque inferior temporal cortex with representations from image- and video-based neural networks spanning recognition, segmentation, optic-flow processing and predictive world modeling. Temporal integration improved object representations, but most video recognition models generalized...
  </details>

- **2026-08-24** — Seonglae Cho, Donghyun Lee — [AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace](http://arxiv.org/abs/2608.23740v1)
  <details><summary>📄 Abstract</summary>
  Concurrent multi-agent coding promises division of labor across modules, robustness through redundancy, and parallel exploration at the natural granularity of multi-file projects. Realtime collaborative editing protocols solve this coordination problem for human teams via Conflict-free Replicated Data Types (CRDTs), but the LLMs underneath generate one token at a time and existing multi-agent coding systems inherit this serial limit: they either sequence agents through phase handoffs or pool ind...
  </details>

- **2026-08-24** — Himanshu Tripathi, Subash Neupane, Shaswata Mitra et al. — [Gated Activation Steering for Reducing Sycophancy & Hallucination in Medical Question Answering](http://arxiv.org/abs/2608.23666v1)
  <details><summary>📄 Abstract</summary>
  Sycophancy and hallucination are persistent failure modes of Large Language Models (LLMs) across domains. However, it becomes particularly consequential in clinical question answering, where responses must remain grounded in the provided context and robust to user pressure. Hallucination can introduce information that is unsupported by the context, while sycophancy can cause a model to abandon a previously correct answer when challenged by the user. Existing approaches, such as prompt-based safe...
  </details>

- **2026-08-24** — Hossein Abdi, Satya Prakash Dash, Mingfei Sun — [Guided Riemannian Optimization (GuRO): Bridging Model Predictive Control and Decision Transformers](http://arxiv.org/abs/2608.23204v2)
  <details><summary>📄 Abstract</summary>
  Decision-making in high-dimensional, nonlinear systems remains a central challenge in robotics. While model-based methods like Model Predictive Control (MPC) offer sample efficiency and interpretability, their performance degrades when the dynamics model is inaccurate or long-horizon predictions are required. Conversely, model-free reinforcement learning (RL) learns policies directly from interaction but suffers from high sample complexity and unstable optimization. Recent advances in sequence m...
  </details>

- **2026-08-24** — Xiao Zhang, Qumeng Sun, Jiahao Li et al. — [LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks](http://arxiv.org/abs/2608.23200v2)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification. Yet successful execution experience is typically lost after a single run, forcing subsequent models to rediscover strategies and failure modes from scratch. We study whether such experience can instead be externalized and reused through EvoMap, where verifier-confirmed execution trajectori...
  </details>

- **2026-08-24** — Peiyang Liu, Xi Wang, Di Liang et al. — [The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search](http://arxiv.org/abs/2608.23252v1)
  <details><summary>📄 Abstract</summary>
  As Retrieval-Augmented Generation (RAG) shifts toward diverse portfolio generation, it is stymied by two critical bottlenecks: flawed measurement of evidence utilization, and suboptimal context budget allocation. We resolve both sequentially.   To resolve measurement, we expose a pervasive ``diagnostic illusion'': standard relevance proxies fail catastrophically on hard negatives. We replace them with an efficient causal leave-one-out probe that accurately isolates generative reliance and formal...
  </details>

- **2026-08-24** — Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu et al. — [NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](http://arxiv.org/abs/2608.22888v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing photorealistic scenes in unconstrained underwater environments remains challenging due to severe media-induced light scattering and unpredictable dynamic objects. Recent feed-forward visual foundation models have demonstrated remarkable capabilities in generalized novel view synthesis and tracking. However, when directly applied to aquatic videos, optical attenuation and motion interference fatally corrupt their feature aggregation, leading to severe tracking and reconstruction fa...
  </details>

- **2026-08-24** — Jindou Jia, Shixuan Han, Meng Wang et al. — [Physics Filtering Favors the Generalization of Robot Learning](http://arxiv.org/abs/2608.22701v1)
  <details><summary>📄 Abstract</summary>
  Living organisms exhibit extraordinary adaptability to unseen environments through their intrinsic physical structures and lifelong feedback-driven learning. Endowing robots with comparable generalization is critical for reliable operation in the real world. While recent approaches attempt to improve generalization by scaling training data, such strategies remain impractical for robotics, where collecting real-world demonstrations at the scale of large language models is prohibitively costly and...
  </details>

- **2026-08-24** — Zhiqing Cui, Xinxiang Yin, Yihong Tang et al. — [EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards](http://arxiv.org/abs/2608.23525v1)
  <details><summary>📄 Abstract</summary>
  Earth-system analysis reconstructs changing physical processes from observations that differ in source, scale, timing, and modality. Natural hazards make this work consequential because incomplete evidence can change estimates of severity, exposure, and mechanism. We introduce EarthVerse, a benchmark that evaluates scientific agents through package-scoped investigations. Its 405 reproducible tasks are grounded in 199 documented events and 19 hazard families. Agents inspect heterogeneous event pa...
  </details>

- **2026-08-24** — Steeven B. Affognon, Babacar M. Ndiaye, Pierre Mendy et al. — [From Daily Fluctuations to Annual Hydrological Cycles: A Wavelet-Based Analysis of Nonstationary Seasonality in Senegal River Hydropower Inflows](http://arxiv.org/abs/2608.23470v1)
  <details><summary>📄 Abstract</summary>
  This study presents a reproducible framework combining Fourier and wavelet analysis to examine the seasonality of daily inflows at three sites on the Senegal River (Bafing Makana, Felou, Gouina), based on 65,631 daily observations spanning nearly 60 years (1961-2020). Using harmonic regression, Welch spectral analysis, stationary wavelet decomposition, Morlet continuous wavelet transforms, trend and change-point tests, and cross-wavelet coherence, the authors show that the annual cycle correspon...
  </details>

- **2026-08-24** — Andrej Orsula, Miguel Olivares-Mendez, Carol Martinez — [Reward-Free Continual Adaptation for Resilient Space Robots](http://arxiv.org/abs/2608.23452v1)
  <details><summary>📄 Abstract</summary>
  Space robots operate in extreme environments where hardware degradation can critically compromise traditional control strategies. While continual reinforcement learning offers a promising mechanism for online adaptation, it inherently requires access to a reward signal during deployment. However, precise reward computation in space is often infeasible due to the lack of external tracking systems and the overall complexity of the environment. To address the challenge of unobservable rewards, we i...
  </details>

- **2026-08-24** — Geoffrey X. Yu, Ryan Marcus, Tim Kraska — [EXPLAIN Yourself! Finding Query Planner Stalls Across DBMSes](http://arxiv.org/abs/2608.23402v1)
  <details><summary>📄 Abstract</summary>
  Query planners are typically expected to produce optimized plans quickly, leading many researchers (including the authors of this paper) and practitioners to design systems that assume query planning is a low-cost operation. Using a lightweight agentic search, we show that this assumption does not always hold. Across seven DBMSes, including four commercial systems, we find at least one query per system that takes more than three minutes to plan. In addition to being slow to plan, such queries ri...
  </details>

- **2026-08-24** — Jiapeng Li, Ping Wei, Wenjuan Han et al. — [IntentQA: Intent Question Answering in Videos by Cognitive Context Reasoning](http://arxiv.org/abs/2608.23330v1)
  <details><summary>📄 Abstract</summary>
  Video understanding requires intelligent agents to transcend mere recognition of visual facts and comprehend the underlying intents behind human actions (often termed the "dark matter" of social intelligence). To bridge the gap between visual observation and intent reasoning, we introduce a novel task, IntentQA, and contribute a large-scale VideoQA dataset specifically tailored for this purpose. However, recognizing that standard metrics may overestimate capabilities due to dataset biases, we go...
  </details>

- **2026-08-24** — Yuexin Ma, Jingqi Hou, Yuxuan Kang et al. — [A Multidimensional Data-Driven Hybrid Transformer Framework for Non-invasive Continuous Blood Pressure Prediction](http://arxiv.org/abs/2608.23276v1)
  <details><summary>📄 Abstract</summary>
  Objective. To develop and evaluate a cuffless continuous blood pressure (BP) estimator using temporal physiological and demographic features. We propose a hybrid Transformer framework to estimate diastolic and systolic BP from ECG/PPG-derived feature sequences. Approach. Rather than raw waveforms, the framework models 10-step sequences of six physiological descriptors and two demographic covariates. A Multi-Source Temporal Encoder Module combines Transformer, Kolmogorov-Arnold Network, and XGBoo...
  </details>

- **2026-08-24** — Guoyang Shi, Zitong Zhang, Siqi Ding et al. — [AI Surrogate Modeling for Real-Time Tokamak Equilibrium Prediction: Benchmarking Neural Architectures and Validation on EXL-50U](http://arxiv.org/abs/2608.23217v1)
  <details><summary>📄 Abstract</summary>
  Fast and reliable plasma equilibrium prediction is essential for real-time tokamak operation and control, but conventional Grad-Shafranov (GS) solvers are often too costly for real-time deployment. We develop an AI surrogate framework and benchmark five architectures (MLP, CNN, FNO, Transformer, and KAN) on a numerical GS database with 100,000 IID and 10,000 OOD samples. Under a unified protocol, we evaluate accuracy, inference efficiency, model scaling, and robustness. We also establish device-...
  </details>

- **2026-08-24** — Hossein Abdi, Satya Prakash Dash, Mingfei Sun — [Guided Riemannian Optimization (GuRO): Bridging Model Predictive Control and Decision Transformers](http://arxiv.org/abs/2608.23204v1)
  <details><summary>📄 Abstract</summary>
  Decision-making in high-dimensional, nonlinear systems remains a central challenge in robotics. While model-based methods like Model Predictive Control (MPC) offer sample efficiency and interpretability, their performance degrades when the dynamics model is inaccurate or long-horizon predictions are required. Conversely, model-free reinforcement learning (RL) learns policies directly from interaction but suffers from high sample complexity and unstable optimization. Recent advances in sequence m...
  </details>

- **2026-08-24** — Xiao Zhang, Qumeng Sun, Jihao Li et al. — [LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks](http://arxiv.org/abs/2608.23200v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification. Yet successful execution experience is typically lost after a single run, forcing subsequent models to rediscover strategies and failure modes from scratch. We study whether such experience can instead be externalized and reused through EvoMap, where verifier-confirmed execution trajectori...
  </details>

- **2026-08-24** — Chang Liu, Xiaohui Xie, Xinyi Chen et al. — [NetConfArena: An Executable Benchmark for LLM Agents in Closed-Loop Network Configuration](http://arxiv.org/abs/2608.23179v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly attractive for automating network configuration, yet their reliability and failure patterns are poorly understood. An essential prerequisite is to assess such agents in a realistic but risk-free environment. Existing benchmarks, however, fall short: they often treat configuration as static command generation or rely on overly simplified settings. Such evaluations understate the core challenges of network configuration, where correctness requires...
  </details>

- **2026-08-24** — Burak Satar, Zhixin Ma, Cheng Yu-Tong et al. — [Cultural Moment Benchmark: Evaluating Video Cultural Reasoning and Grounding in Southeast Asia](http://arxiv.org/abs/2608.23065v1)
  <details><summary>📄 Abstract</summary>
  Cultural understanding in video means more than recognizing what is visible; it requires grasping the symbolic and temporal significance of cultural concepts. We decompose this into three abilities: naming what a concept symbolizes, visually recognizing it on video, and locating its sub-events in time. Existing video-cultural benchmarks tend to test what is seen, collapsing these three abilities into a single score that hides the bottleneck. We introduce the Cultural Moment Benchmark (CMB): 306 ...
  </details>

- **2026-08-24** — Xiaotong Tan, Chunli Qiu, Xin Liu et al. — [Improving O-RADS Risk Stratification from Ultrasound Reports: A Comparative Evaluation of Hybrid versus End-to-End LLM Reasoning Strategies](http://arxiv.org/abs/2608.23061v1)
  <details><summary>📄 Abstract</summary>
  Background: Automating clinical guideline-based decision-making with large language models (LLMs) remains challenging because of reliability, hallucination, and limited interpretability. We compared the performance of LLMs and reasoning strategies for automated Ovarian-Adnexal Reporting and Data System (O-RADS) classification from free-text pelvic ultrasound reports. Methods: In this retrospective study, consecutive patients with ovarian masses who underwent pelvic ultrasound were included. Eigh...
  </details>

- **2026-08-24** — Sungho Park, Wonjoong Kim, Rongyuan Tan et al. — [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](http://arxiv.org/abs/2608.23041v1)
  <details><summary>📄 Abstract</summary>
  LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic. We propose AutoSaddler, an automatic harness optimization framework that formulates harness improvement as an offline learning probl...
  </details>

- **2026-08-24** — Xiaohui Zhang, Zequn Sun, Chengyuan Yang et al. — [Toward Effective and Reliable LLM Agents via Dynamic Ontology](http://arxiv.org/abs/2608.22974v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents rely heavily on knowledge encoded in model parameters or presented as unstructured context. In domain-specific tasks, this leaves important semantic connections implicit. This often results in incomplete evidence use and brittle multi-step decisions. Ontologies offer a way to externalize domain concepts and relations as machine-interpretable structures, but constructing task-usable ontologies traditionally requires substantial effort from domain experts and is d...
  </details>

- **2026-08-24** — Yiyi Zhang, Yuchen Yuan, Ying Zheng et al. — [Optimize Surgical Triplet Recognition: A Knowledge-Driven Mixture-of-Experts Solution](http://arxiv.org/abs/2608.22972v1)
  <details><summary>📄 Abstract</summary>
  Surgical action triplet recognition constitutes a critical task in context-aware robot-assisted surgery, facilitating automatic surgical action perception by identifying instrument, verb, target, and their association. However, existing works struggle to analyze such complex surgical scenes due to three main issues: (1) component-level optimization conflicts caused by entangled feature spaces, (2) category-level optimization conflicts arising from severe data imbalance, and (3) lack of domain kn...
  </details>

- **2026-08-24** — Yingxiang Xu, Kerui Ren, Wenqi Guo et al. — [AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](http://arxiv.org/abs/2608.22906v1)
  <details><summary>📄 Abstract</summary>
  Recent monocular 3D Gaussian Splatting (3DGS) streaming reconstruction methods have achieved impressive performance by balancing reconstruction quality and efficiency. However, extending these frameworks to underwater scenes remains challenging due to severe visual degradation, such as light attenuation and scattering, which degrades camera pose tracking and distorts scene geometry. To address these challenges, we propose AquaFlow, a monocular Gaussian Splatting streaming reconstruction framewor...
  </details>

- **2026-08-24** — Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder et al. — [XTC: Head-Aware Sampling by Excluding Top Choices](http://arxiv.org/abs/2608.22758v1)
  <details><summary>📄 Abstract</summary>
  Standard decoding rules for autoregressive language models promote diversity by rescaling the full next-token distribution or truncating its low-probability tail. These strategies overlook a common regime of open-ended generation in which several continuations are plausible but too much probability mass remains concentrated on the most generic choice. We introduce XTC (Exclude Top Choices), a lightweight head-aware decoding operator that targets this regime directly. XTC identifies tokens whose ...
  </details>

- **2026-08-24** — Jieun Lee — [Double/Debiased Machine Learning for Functional-Form-Robust Spatial Autoregression](http://arxiv.org/abs/2608.22706v1)
  <details><summary>📄 Abstract</summary>
  Spatial autoregressive inference is typically conditional on the spatial weights matrix, W, even though the underlying interaction structure is often unknown and empirical conclusions can be sensitive to its specification. This paper develops double/debiased machine learning inference for low-dimensional SAR parameters when the spatial interaction operator is learned flexibly from potentially endogenous characteristics. Within a maintained admissible support, interaction strength is generated by...
  </details>

- **2026-08-24** — Jiachen Xu, Torben Bach Pedersen, Zhongming Yao et al. — [Robustness Analysis of Agentic AI to Inconsistent and Incomplete Tool Responses](http://arxiv.org/abs/2608.22676v1)
  <details><summary>📄 Abstract</summary>
  Robustness to a bad tool return means answering it in the way that return calls for, which depends on how the tool went wrong. A tool that has failed and a tool that returns a well-formed falsehood are different problems with different remedies. We ask whether the two already differ at the moment the return arrives. This is a qualitative pilot study: we score single decision points rather than running agents to completion. We inject controlled faults into a retail customer-service domain and rea...
  </details>

- **2026-08-23** — Heather Renze — [Auditing the Synthetic Memoir: Measuring Scene-Level Confabulation in LLM-Generated Autobiography Against the Documented Record of the Life It Describes](http://arxiv.org/abs/2608.23640v1)
  <details><summary>📄 Abstract</summary>
  When a large language model (LLM) is asked to write a person's life, how much of what it writes actually happened? We present a scene-level case-study audit - the first quantified audit of LLM-generated autobiography against a subject-specific ground-truth corpus that we are aware of, based on an unsystematic literature search. The subject and the author of this paper are the same person: a 366-day "page-a-day" book of first-person anecdotal entries was drafted with a conversational LLM whose do...
  </details>

- **2026-08-23** — Toghrul Abbasli, Kentaroh Toyoda, Yuan Wang et al. — [Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models](http://arxiv.org/abs/2608.22483v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly support decision-making in high-stakes domains, but they often hallucinate and express confidence that is misaligned with factual correctness. Response-level confidence is a coarse signal: a single generation can mix correct and incorrect statements, so a single number is not actionable for users that must accept, reject, or verify individual pieces of information. We study claim-level confidence calibration as a decision-relevant uncertainty signal: eac...
  </details>

- **2026-08-23** — Yiming Wang, Jiale Zhu, Zhichen Ye et al. — [A Query-Time Framework for Transient 2D Pore-Scale Flow Prediction and Generative Design](http://arxiv.org/abs/2608.22235v1)
  <details><summary>📄 Abstract</summary>
  Pore-scale flow governs transport and permeability behaviour in porous media engineering applications, yet repeated lattice Boltzmann method (LBM) simulation across many geometries and design queries remains costly for repeated deployment. This study formulates transient pore-scale flow prediction as a geometry-conditioned query-time operator and introduces QSGS-Transient-7606, a benchmark of 7,606 two-dimensional porous structures each paired with 30 logarithmically sampled LBM states. The prop...
  </details>

- **2026-08-23** — Yaofei Wang, Jinyang Guo, Shuchao Du et al. — [PURA: Provably Unbiased and Robust Multi-Bit Text Attribution](http://arxiv.org/abs/2608.22218v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained attribution of AI-generated text is becoming increasingly important for accountability and auditing, yet existing multi-bit watermarking methods still struggle to simultaneously preserve the base generation distribution, support high-capacity payloads, and remain recoverable after editing. We present PURA, a provably unbiased and robust multi-bit watermarking method for text attribution. Instead of perturbing token probabilities directly, PURA embeds payloads in the latent sampling ...
  </details>

- **2026-08-23** — Christos Sardianos, Iliana Pla, Vasilis Efthymiou et al. — [HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems](http://arxiv.org/abs/2608.22512v1)
  <details><summary>📄 Abstract</summary>
  Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, ...
  </details>

- **2026-08-23** — Junda He, Jieke Shi, Zhou Yang et al. — [Learning from the Test: Self-Referential Differential Testing for Deep RL Agents](http://arxiv.org/abs/2608.22284v1)
  <details><summary>📄 Abstract</summary>
  Deep Reinforcement Learning (DRL) has achieved significant success in complex decision-making problems. As DRL systems are increasingly deployed in real-world applications, ensuring their quality and reliability is paramount. Current works primarily focus on detecting safety-critical failures, often neglecting policy optimality, which can lead to reduced efficiency, user distrust, and economic losses. This oversight, compounded by the inherent "testing oracle problem" for optimality, leaves a si...
  </details>

- **2026-08-23** — Md Toufikuzzaman, Ahmad Mousavi, Dongwon Lee — [BLADE: Bilevel Low-rank Augmented-Lagrangian Erasure for LLM Unlearning](http://arxiv.org/abs/2608.22557v1)
  <details><summary>📄 Abstract</summary>
  Existing LLM unlearning methods struggle with robustness: unbounded forget losses degrade model coherence, fixed-weight balancing cannot adapt as retain difficulty shifts mid-training, and methods that work on one benchmark falter under scaling or repeated application. We propose BLADE, a constrained bilevel framework whose three mechanisms give smooth, predictable control over the optimization landscape: a clamped-entropy forget loss whose gradient is exactly zero once a token reaches sufficien...
  </details>

- **2026-08-23** — Davide Bargellini, Alex Pasquali, Andrea Govoni et al. — [Enhancing Sim2Real Transfer for Torque-Controlled Robots through Real2Sim Dynamics Estimation and Reinforcement Learning](http://arxiv.org/abs/2608.22629v1)
  <details><summary>📄 Abstract</summary>
  Transferring reinforcement learning policies from simulation to Real-World robots remains a major challenge, particularly when dealing with low-level torque control, where even small modelling inaccuracies can lead to unstable or unsafe behaviours. In this work, we propose a Real2Sim2Real pipeline that improves Sim2Real transfer for torque-controlled robotic arms by combining trajectory matching, parameter optimization via genetic algorithms, and domain randomization. Using the 7-DOF Franka Emik...
  </details>

- **2026-08-23** — Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman et al. — [Small Reasoning Models are Instruction Followers in Function Calling](http://arxiv.org/abs/2608.22472v1)
  <details><summary>📄 Abstract</summary>
  Function calling represents the core capability of agentic large language models (LLMs). Existing research has focused on enhancing LLMs function-calling accuracy through fine-tuning, reinforcement learning (RL), and multi-agent frameworks, particularly for native function-calling LLMs. This work demonstrates that LLMs achieve superior accuracy in function calling in instruction-following contexts (i.e., standard user-assistant interactions) rather than a tool calling context. We introduce Instr...
  </details>

- **2026-08-23** — Francisco Portillo López — [From Exposure to Expectation: Frequency, Surprisal, and Language Across Development in Spanish](http://arxiv.org/abs/2608.22452v1)
  <details><summary>📄 Abstract</summary>
  Surprisal, the negative log-probability a language model assigns to a word given its preceding context, reliably predicts adult reading times. Does it contribute as much to explaining when children acquire individual words? Frequency reflects a learner's cumulative exposure to a word, whereas surprisal reflects how predictable a single occurrence is given its context. We investigate this question across two corpus-based studies of Spanish.   In Study 1, we modeled age of acquisition (AoA) for 22...
  </details>

- **2026-08-23** — Changjiang Jiang, Qiannian Zhao, Lei Xin et al. — [Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding](http://arxiv.org/abs/2608.22429v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and structurally relational visuals (e.g., charts and visual tables) where strict relative spatial arrangements bind textual elements. Without external tools, standard MLLMs struggle with such fine-grained v...
  </details>

- **2026-08-23** — Aoke Zhang, Bo Wang, Xihong Wu et al. — [Cross-Subject Generalization in Decoding Perceived Speech from Non-Invasive Brain Recordings](http://arxiv.org/abs/2608.22420v1)
  <details><summary>📄 Abstract</summary>
  Decoding perceived speech from non-invasive brain recordings has garnered significant attention in recent years due to its wide range of potential applications. However, existing methods face considerable challenges in cross-subject decoding, primarily due to limited generalizability and the absence of explicit mechanisms for extracting subject-consistent information. These limitations result in high training costs and suboptimal decoding performance. To address these challenges, we propose an i...
  </details>

- **2026-08-23** — Yihua Shao, Jia Li, Siyu Chen et al. — [LiST: Local-Simplex Test-Time LoRA Fusion](http://arxiv.org/abs/2608.22370v1)
  <details><summary>📄 Abstract</summary>
  Task-specific LoRA adapters offer a modular way to specialize large language and vision-language models. However, existing adapter composition methods are mostly static and cannot adapt to individual test inputs. To address these issues, we propose \textbf{LiST}, a label-free test-time LoRA fusion framework that converts an existing LoRA bank into a target-conditioned local simplex and searches sample-specific fusion weights at inference time. LiST builds joint task representations from LoRA par...
  </details>

- **2026-08-23** — Yize Li, Ningyuan Yang, Sile Yin et al. — [MRMAD: A Multi-Round Multi-Audio Benchmark for Evaluating Acoustic Degradation Perception in Large Audio-Language Models](http://arxiv.org/abs/2608.22236v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) have shown promising progress in understanding speech, music, and general sound events, yet their ability to reason about how audio signals are degraded remains underexplored. Existing benchmarks primarily evaluate semantic understanding, event recognition, or high-level audio reasoning, leaving a basic question unanswered: Do LALMs understand the differences in audio quality? We introduce MRMAD, a Multi-Round Multi-Audio Degradation benchmark for evaluating a...
  </details>

- **2026-08-23** — Kang Chen, Junjie Nian, Yixin Cao et al. — [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](http://arxiv.org/abs/2608.22191v1)
  <details><summary>📄 Abstract</summary>
  Software-engineering agents solve repository-level tasks through long, stochastic tool-use trajectories, and repeated attempts often find fixes missed by one run. Test-time scaling is difficult because patches lack canonical answer forms, while sibling actions from a shared prefix are correlated. We study whether native MoE router traces can guide steering and selection without an external judge or selection-time test execution. Our analysis shows that routing provides a robust behavioral role s...
  </details>

- **2026-08-22** — Lukasz Olejnik, Bartosz Naskrecki — [AI Grinding for Fun and Cryptanalysis](http://arxiv.org/abs/2608.21986v1)
  <details><summary>📄 Abstract</summary>
  We present an autonomous cryptanalysis workflow in which agents generate, test, and refine hypotheses before human review. The autonomous stage returns reproducible candidates with exact witnesses, controls, code, and run records. A researcher then decides whether the evidence establishes a break, defect, or coverage gap.   Two failure modes recur. First, a public algebraic map or input representation erases or exposes a relation that a construction must hide. Examples include multiplication by ...
  </details>

- **2026-08-22** — Yaokun Liu, Yifan Liu, Daniel Yue Zhang et al. — [PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems](http://arxiv.org/abs/2608.22130v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) solve complex tasks through communication among role-specialized agents. However, inter-agent dependencies introduce reliability risks beyond isolated agent failures. For instance, errors in intermediate messages could be inherited and amplified by downstream agents. Existing uncertainty quantification (UQ) methods mainly target isolated responses or single-agent reasoning, and therefore fail to capture uncertainty propagation in MAS. To this end, we propose P...
  </details>

- **2026-08-22** — Yuxin Cheng, Chang Liu, Hanxin Yu et al. — [OptiMAS: Automatically Optimize Multi-Agent System](http://arxiv.org/abs/2608.21918v1)
  <details><summary>📄 Abstract</summary>
  Automated evolution of Multi-Agent Systems (MAS) holds significant potential for reducing the manual effort required to design and optimize LLM-based agent architectures. However, extant search-based paradigms face a fundamental trade-off, where an expanded optimization scope exacerbates evolutionary instability, while discrete branch-and-discard search isolates insights across lineages. To address these limitations, we propose a continuous, data-driven optimization paradigm built upon a unified...
  </details>

- **2026-08-22** — Sanjay Bhandari, Nawazish Khan, Alzbeta Novotna et al. — [TRACE: Artifact-Robust Statistical Shape Modeling from Imperfect Surface Scans - A Case Study in Craniosynostosis 3D Photography](http://arxiv.org/abs/2608.22131v1)
  <details><summary>📄 Abstract</summary>
  Craniosynostosis severity analysis increasingly relies on statistical shape models (SSMs) to quantify cranial morphology, but most existing workflows depend on computed tomography or heavily curated three-dimensional (3D) photographs. Raw clinical 3D photographs provide a radiation-free and repeatable alternative, yet often contain shoulders, hands, hair, clothing, scanner noise, and incomplete boundaries that corrupt correspondences. We introduce the Template-constrained Robust Artifact-aware C...
  </details>

- **2026-08-22** — Shuhao Qi, Zhiyong Sun, Siep Weiland et al. — [Opinion-Guided Layered Strategies for Decentralized Coordination](http://arxiv.org/abs/2608.22104v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents increasingly interact with other independent agents, and such interactions typically admit multiple joint behaviors. When two agents prefer different ones, their independent strategies may be mutually incompatible and fail to reach a coordinated outcome; when they are identical, neither can differentiate its role when needed. Ideally, an agent should coordinate with any agent it encounters, regardless of which admissible joint behavior that agent aims to realize. We therefore p...
  </details>

- **2026-08-22** — Edwin Ouko, Emmanuel Lujan, Alan Edelman et al. — [Decision-Support and Modeling with Large Language Models for Geothermal Well Arrays](http://arxiv.org/abs/2608.22068v1)
  <details><summary>📄 Abstract</summary>
  Geothermal well arrays, which organize multiple geothermal wells into carefully planned geometric configurations, provide opportunities to enhance energy production capacity and increase fault tolerance. The development and adoption of these emerging geothermal technologies could be accelerated through the recent advances in large language models (LLMs) and high-level high-performance languages. A challenge in LLM-based applications is the reliability of the generated outputs, as they can be pro...
  </details>

- **2026-08-22** — Leonardo Zini, Elia Frigieri, Lorenzo Baraldi — [A Scalable Vector Graphics Latent Space](http://arxiv.org/abs/2608.21893v1)
  <details><summary>📄 Abstract</summary>
  Scalable Vector Graphics are a fundamental medium for resolution-independent visual content, yet the deep learning community lacks a continuous, dense, and invertible latent space for vector representations, the kind of foundational building block that Variational Autoencoders and their descendants have long provided for raster images. We introduce SLS (SVG Latent Space), a Transformer-based autoencoder that learns compact dense representations of individual SVG paths, the atomic visual elements...
  </details>

- **2026-08-22** — Vsevolod Kleshchenko, Vladimir Igoshin, Costantino De Angelis et al. — [Mie Optical Computing](http://arxiv.org/abs/2608.21891v1)
  <details><summary>📄 Abstract</summary>
  Optical computing is emerging as a promising paradigm for next-generation information processing. Diffractive optical processors rely on spatially distributed trainable degrees of freedom, leading to extended architectures. Here, we propose a compact neuromorphic optical-computing approach where the entire trainable transformation is implemented by a single Mie scatterer. By formulating computation in vector spherical harmonics basis, trainable modal couplings can be concentrated within a finite...
  </details>

- **2026-08-22** — Chaoran Huang, Fangcheng Li, Tianyi Liu et al. — [Towards Bitstream-corrupted Harsh Visual Understanding: Through Bitstream Language Modeling as Robust Semantic Priors](http://arxiv.org/abs/2608.21837v1)
  <details><summary>📄 Abstract</summary>
  Bitstream-corrupted Harsh Visual Understanding (BcHVU) aims to understand harshly degraded videos originally decoded from a severely corrupted bitstream in real-world multimedia communication. The ill-posed nature of BcHVU poses a major challenge for existing vision models, as even subtle bitstream corruption can lead to irreversible pixel distortion and significant semantic loss. To address these challenges in BcHVU, we propose Bitstream Language Modeling as Robust Semantic Priors (BLMSP), a fr...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 18 papers

- **2026-08-25** — Yijun Liao, Fanwei Liang — [Shortcut Before Circuit: Document Statistics Time In-Context Conflict Resolution](http://arxiv.org/abs/2608.24460v1)
  <details><summary>📄 Abstract</summary>
  When a context asserts two values for one fact, a model commits to a cue -- recency, repetition, position -- but natural data rarely makes these disagree, so behavior cannot reveal which. We train 26M-parameter transformers on a synthetic language where recency and rarity are exactly coextensive, and separate them with a minimal causal edit that inverts one cue while holding the truth, token count and answer position fixed. All 75 runs reach accuracy >= 0.999, including where the trivial heurist...
  </details>

- **2026-08-25** — Yarden Bakish, Amir Dudai, Roy Ganz et al. — [Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems](http://arxiv.org/abs/2608.24361v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems are increasingly deployed in real-world applications, where failures can be costly and difficult to localize. Despite growing efforts to automate failure attribution, diagnosing failed runs still largely relies on human engineers. Yet engineers rarely debug complex systems by reading raw logs end to end. Instead, observability tools organize traces around components, actions, and dependencies to support targeted navigation. We hypothesize that modern LLMs can benefit from...
  </details>

- **2026-08-25** — Luo Huan — [Agentopia on a Consumer GPU: A Reduced-Scale Long-Horizon Port with an 8B Model](http://arxiv.org/abs/2608.24215v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based multi-agent social simulation has demonstrated compelling results, but Agentopia was evaluated with 100 agents over 10 simulated years using Qwen3.5-397B-A17B, leaving the behavior of reduced-scale deployments on consumer hardware unclear. In this paper, we implement and evaluate a reduced-scale Agentopia port on a single NVIDIA RTX 5070 Ti(12 GB VRAM) using Qwen3-8B-AWQ, a 4-bit quantized model. We introduce three structural adaptations for this setting: (1) sys...
  </details>

- **2026-08-25** — Dai Jiahong — [The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses](http://arxiv.org/abs/2608.23953v1)
  <details><summary>📄 Abstract</summary>
  An agent harness is what turns a language model into an autonomous agent: the surrounding code that builds the model's context, mediates its tools, runs the loop, and persists state across a long-horizon run. This layer, not the model it wraps, is increasingly the binding constraint on agent behaviour. We present a source-level, multi-case study of three open coding-agent harnesses built from deliberately opposing philosophies: LangChain's deepagents (batteries-included), Earendil's pi (radical ...
  </details>

- **2026-08-24** — B. An, B. Li, B. Wang et al. — [Apodex 1.1: Scaling Agentic Intelligence for Complex Work](http://arxiv.org/abs/2608.23283v2)
  <details><summary>📄 Abstract</summary>
  General-purpose language models can reason and synthesize knowledge, but complex work also requires sustained interaction with files, information sources, and executable code, together with state maintenance, failure recovery, and verifiable delivery. We call this \emph{working capability}: sustained, verifiable progress toward a real-world objective. Apodex 1.1 develops this capability along two complementary dimensions. \emph{Environment Scaling} expands the diversity and verifiability of exec...
  </details>

- **2026-08-24** — Kalin Stoyanov — [Ethical LLM-Assisted Research: A Framework for Responsible Delegation, Verification, and Epistemic Value](http://arxiv.org/abs/2608.23644v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are becoming routine instruments of scientific research, assisting with literature synthesis, hypothesis development, coding, and formal reasoning. Their use raises a central epistemic question: when parts of scientific reasoning are delegated to an artificial system, what conditions must remain under human control for the resulting knowledge claims to retain epistemic legitimacy and accountable authorship? This paper develops a normative and conceptual framework for...
  </details>

- **2026-08-24** — Jiawei He, Mengyu Shi, Jie jia et al. — [What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels](http://arxiv.org/abs/2608.22960v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly evaluated not only by whether they solve a task, but also by how they execute it. However, existing process-level evaluations often treat action prediction, task uncertainty, and step attribution as if they were the same problem, which makes it unclear what such evaluations actually measure. In this paper, we introduce a measurement framework for process evaluation in coding agents and instantiate step-level causal attribution with SCAE, a replay-based estimator de...
  </details>

- **2026-08-24** —  Apodex Team, B. An, B. Li et al. — [Apodex 1.1: Scaling Agentic Intelligence for Complex Work](http://arxiv.org/abs/2608.23283v1)
  <details><summary>📄 Abstract</summary>
  General-purpose language models can reason and synthesize knowledge, but complex work also requires sustained interaction with files, information sources, and executable code, together with state maintenance, failure recovery, and verifiable delivery. We call this \emph{working capability}: sustained, verifiable progress toward a real-world objective. Apodex 1.1 develops this capability along two complementary dimensions. \emph{Environment Scaling} expands the diversity and verifiability of exec...
  </details>

- **2026-08-24** — Radouane Bouchekir, Damir Safin, Tomas Bueno Momcilovic — [From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents](http://arxiv.org/abs/2608.23282v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) agents deployed in vehicles must satisfy a written operating policy on every turn: a single hallucinated identifier, omitted mandatory side-effect, or premature completion claim fails the task. We present AgentGuardUtil, our entry to CAR-bench Track~1, which treats the AI planer (LLM) as a fallible proposer inside a grounded verify-and-revise loop. Its core novelty is a runtime policy compiler: the natural-language policy shipped with each conversation is compiled, o...
  </details>

- **2026-08-24** — Jieke Wang, Tiancheng Shen, Yibo Yang et al. — [Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner](http://arxiv.org/abs/2608.23268v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal large language models (MLLMs) deliver impressive perception yet still falter on scientific and mathematical reasoning. Parameter-level adaptation is unavailable for closed-weight or on-device backbones, and stateless prompting forfeits any compounding benefit from problems already solved. We propose \textbf{DG-Mem}, a dual-grained agentic memory framework that augments a frozen MLLM with a non-parametric, externally stored memory built once from training-time rollouts and con...
  </details>

- **2026-08-24** — Dani Termaat, Nafiseh Soveizi, Zhiming Zhao et al. — [LLMCrater: Lifecycle-Aware FAIR Metadata Generation using Large Language Models](http://arxiv.org/abs/2608.23158v1)
  <details><summary>📄 Abstract</summary>
  FAIR (Findable, Accessible, Interoperable, and Reusable) metadata is essential for the discovery, interoperability, and reuse of scientific research assets. However, creating and maintaining FAIR metadata remains largely manual, making the process time-consuming for heterogeneous research artifacts generated throughout the research lifecycle. Existing approaches primarily generate metadata at publication time, missing opportunities to capture contextual information as it becomes available. To ad...
  </details>

- **2026-08-23** — Huangchen Xu, Yuan Wu, Yi Chang — [How Agents Represent Humans: Human-Directed Stereotypes in an Open Agent Social Network](http://arxiv.org/abs/2608.22192v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly deployed in persistent social environments, where generated claims can be posted, replied to, remembered, and reused. We study human-directed stereotypes on Moltbook, an open agent-native social platform, asking how agents construct humans as a social category. For this human-target analysis, we introduce an annotation framework with four evaluative dimensions---morality, friendliness, competence, and autonomy---and a second-stage subtype scheme for descriptive ...
  </details>

- **2026-08-23** — Zhixu Du, Yiran Chen — [AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems](http://arxiv.org/abs/2608.22160v1)
  <details><summary>📄 Abstract</summary>
  Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read ...
  </details>

- **2026-08-23** — Zhuoyu Shi, Fred Morstatter — [Gender Attribution in Causal Beliefs](http://arxiv.org/abs/2608.22150v1)
  <details><summary>📄 Abstract</summary>
  For centuries, women have been cast as the source of harm in public narratives, from witch hunts in early modern Europe to contemporary stereotypes about emotional instability. These cultural patterns reflect enduring biases in how people attribute causality and assign blame, often portraying women as agents of disruption and men as figures of rational authority. In this study, we examine how such gendered causal attributions appear in everyday language. Leveraging three complete 24-hour dataset...
  </details>

- **2026-08-23** — Karthik Sridhar, Atharva Gupta, Nishant Pradhan et al. — [Semantics or Structure? Auditing Text Sensitivity in Multimodal Time-Series Forecasting](http://arxiv.org/abs/2608.22321v1)
  <details><summary>📄 Abstract</summary>
  Multimodal time-series forecasting has emerged as a promising paradigm in which natural-language context is expected to improve predictive performance. Recent multimodal foundation models, including Aurora, as well as early- and late-fusion approaches such as MM-TSFlib and TaTS, report substantial gains over unimodal baselines on the Time-MMD benchmark, attributing these improvements to textual information. However, whether these models are actually sensitive to the semantic content of the text ...
  </details>

- **2026-08-23** — Oliver López Corona — [From Authorial Mathematics to Studio Mathematics:Ecobiontic Forms of Proof after Large Language Models](http://arxiv.org/abs/2608.22194v1)
  <details><summary>📄 Abstract</summary>
  Mathematics has often been organized around an authorial subject: one person, or a small group, composing proofs through language, notation, and judgment. Large language models, proof assistants, formal libraries, and repositories now make another production unit technically credible: a human-machine assemblage. This article calls that unit a studio ecobiont and asks when it is epistemically legitimate. Its governance thesis is that human participation is substantive only when the system preserv...
  </details>

- **2026-08-22** — Xinyuan Song, Bowen Zhu, Hasibul Haque et al. — [MegaMem: A Retrieval Solution for Ultra-Large Context Windows](http://arxiv.org/abs/2608.22137v1)
  <details><summary>📄 Abstract</summary>
  Modern language models and agents increasingly require persistent memory for complete codebases, long interaction histories, and heterogeneous enterprise records. The key challenge is to keep hundreds of millions of tokens searchable while passing only bounded source evidence to the answer model. We introduce MegaMem, a source-resolved dual-view retrieval system that separates semantic access from generation evidence. Distilled records and detailed evidence are searched with original and transfo...
  </details>

- **2026-08-22** — Maruf Ahmed Mridul, Abid Talukder, Oshani Seneviratne — [GrOIL: Graph-Grounded Domain Ontology Induction with Constrained LLM Mediation](http://arxiv.org/abs/2608.22135v1)
  <details><summary>📄 Abstract</summary>
  Constructing formal ontologies from domain documents requires simultaneously enforcing corpus grounding, vocabulary consistency, axiom-level expressivity, and end-to-end provenance, a combination no existing automatic system delivers. We present a seven-stage graph-grounded pipeline that converts domain documents into a complete, auditable Web Ontology Language (OWL) Terminological Box (TBox) without any unconstrained generation step. Documents are first encoded as Unified Discourse-Hypergraphs ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-08-23** — Noam Diamant, Ethan Fetaya, Neta Glazer — [Stress Testing Unlearning Algorithms](http://arxiv.org/abs/2608.22527v1)
  <details><summary>📄 Abstract</summary>
  Recently, machine unlearning, the removal of specific training data influence from a model, has gained increasing attention. In large language models (LLMs), unlearning is particularly challenging due to the ambiguity of inputs and outputs. Con- sequently, rigorous evaluation is critical for assessing both safety and utility, and for driving progress in unlearning meth- ods. We identify two key shortcomings in existing unlearning benchmarks: (1) they do not actively test whether unlearned inform...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-08-24** — Xuetong Li, Gaofeng Liu — [EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models](http://arxiv.org/abs/2608.23313v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and...
  </details>

- **2026-08-23** — Seyed Mohammad Mahdi Ghalandarian, Majid Bazargani, Masoumeh Taromirad — [Benchmarking the Titans: A Multi-Dimensional Empirical Evaluation of LLM Code Generation Quality in the .NET Ecosystem](http://arxiv.org/abs/2608.22529v1)
  <details><summary>📄 Abstract</summary>
  Evaluating Large Language Model (LLM) code generation quality requires examining not just whether the generated code is correct, but whether it is maintainable, efficient, and stylistically sound, all of which are qualities of direct importance to software engineering practitioners. Existing benchmarks reduce evaluation to a single Pass@k metric, which obscures critical trade-offs between functional correctness and structural quality. A further limitation is the near-exclusive focus on Python, l...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-08-24** — Mullosharaf K. Arabov — [A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](http://arxiv.org/abs/2608.23421v2)
  <details><summary>📄 Abstract</summary>
  Arabic Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis remains absent. This study presents a bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from five platforms (arXiv, ACL Anthology, Semantic Scholar, Crossref, OpenAlex) plus an additional targeted Op...
  </details>

- **2026-08-24** — Mullosharaf K. Arabov — [A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](http://arxiv.org/abs/2608.23421v1)
  <details><summary>📄 Abstract</summary>
  Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis of the field remains absent. This study presents a large-scale bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from six collections. We employ BERTopic for topic modeling, regression analysis to identify ...
  </details>

- **2026-08-24** — Virgile Rennard, Christos Xypolopoulos — [Large language models simulate intersectional synthetic identities with a budget of one to two dimensions](http://arxiv.org/abs/2608.23005v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as synthetic survey respondents, promising cheap access to rare intersectional populations. We test standard demographic-persona methods against every real intersectional subgroup across 15 waves of Pew's American Trends Panel -- 21 million simulated response distributions from eight models. In real respondents, subgroup opinion is approximately the additive sum of its single-identity components, yet grows 2.5x more distinctive as identities intersect....
  </details>

- **2026-08-23** — Yikai Gao, Ding Xia, Xi Yang — [Query-Driven Multimodal Information Extraction from Long Documents](http://arxiv.org/abs/2608.22214v1)
  <details><summary>📄 Abstract</summary>
  In domain-specific multimodal long documents, images and text jointly convey complex knowledge that cannot be fully captured by plain text alone. However, existing paradigms like DocVQA primarily focus on generating textual answers or localizing evidence regions, rather than outputting query-specific textual attribute values and corresponding images. To address this gap, we propose query-driven image-text joint extraction from long documents, requiring models to output query-requested textual at...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 142 papers

- **2026-08-25** — Muntaser Syed, Markus Zanker, Marius Silaghi — [Rules Before Oracles: Auditable, User-Configurable Argument Selection for Deliberative Polling](http://arxiv.org/abs/2608.23979v1)
  <details><summary>📄 Abstract</summary>
  In a deliberative poll, once submissions outnumber what anyone will read, some mechanism chooses which arguments each voter sees, acquiring much of the decision; practice delegates it to opaque learned rankers, so a voter cannot recompute or contest the exposure that shaped their vote. We ask whether it can be a published rule over publicly recomputable evidence with parameters held by the voter, treating legibility as an admissibility condition on usable mechanisms, not an objective traded agai...
  </details>

- **2026-08-25** — Jing Huang, Jihong Zhang, Hua-Hua Chang — [A Dual-Dimensional LLM Framework for Automated Item Incidental Content Similarity Analysis in Large-Scale Assessments](http://arxiv.org/abs/2608.24825v1)
  <details><summary>📄 Abstract</summary>
  The rapid expansion of large-scale assessments and the growing adoption of automatic item generation have intensified concerns about incidental content redundancy, where construct-irrelevant elements such as wording or contextual framing become unintentionally repetitive across items. Traditional similarity metrics like BLEU or cosine similarity, often fail to capture the nuanced structural and semantic layers that drive perceived redundancy simultaneously. This study proposes a dual-dimensional...
  </details>

- **2026-08-25** — Muhammad Asad Ali, Umar Khan, Nadia Robertini et al. — [MoTE: Mixture of Task Experts for Multi-Task Video Understanding](http://arxiv.org/abs/2608.24763v1)
  <details><summary>📄 Abstract</summary>
  Procedural video-language models must solve heterogeneous tasks from the same visual evidence, including action recognition, forecasting, and procedure prediction. Dense transformer decoders share the same feed-forward networks across tasks, which can entangle task behavior and make controlled capability expansion difficult. Sparse Mixture-of-Experts (MoE) decoders provide conditional computation, but token-level learned routing is not naturally aligned with task-level procedural objectives. We ...
  </details>

- **2026-08-25** — Zijian Zhang, Yuqing Jiang, Weitao Zhou et al. — [GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](http://arxiv.org/abs/2608.24714v1)
  <details><summary>📄 Abstract</summary>
  World-Action Models (WAMs) jointly learn future visual prediction and action generation, using video dynamics as a representation-learning signal for robotic manipulation. However, their video latents are primarily optimized for visual prediction and are not explicitly encouraged to preserve cross-view geometric structure or spatially localized, object-relevant semantics. We propose \textbf{GaussianWAM}, a training-time representation-enhancement framework that organizes geometric and semantic s...
  </details>

- **2026-08-25** — Wenze Lin, Jiale Zhao, Xitai Jiang et al. — [On-policy Distillation with Verifiable Reward](http://arxiv.org/abs/2608.24696v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Rewards (RLVR) and on-policy distillation (OPD) have become two widely adopted paradigms for post-training large language models. However, RLVR suffers from sparse task-level feedback, while OPD provides dense token-level guidance but ignores trajectory correctness, limiting its performance to that of the teacher. Combining them is a promising direction: OPD supplies dense supervisory signals, while RLVR provides task-level correctness. Nevertheless, existi...
  </details>

- **2026-08-25** — Angelo Salatino, Francesco Osborne, Alexis Vizcaino et al. — [COCI: Conference Organisers and Content Identifier](http://arxiv.org/abs/2608.24559v1)
  <details><summary>📄 Abstract</summary>
  Despite the critical role of grey literature in scholarly communication, artefacts such as Calls for Papers (CfPs) remain largely isolated from modern Scholarly Knowledge Graphs. The unstructured and highly heterogeneous nature of these documents has traditionally hindered their large-scale processing. In this demo paper, we present the Conference Organisers and Content Identifier (COCI), an AI-based framework designed to extract fine-grained, structured metadata from raw CfP texts. COCI employs...
  </details>

- **2026-08-25** — Maosong Chen, Xi Chen, Mengcheng Ju et al. — [SeriCrypt: An LLM-Driven Context-Aware Serialization Framework for Cryptographic Protocols](http://arxiv.org/abs/2608.24498v1)
  <details><summary>📄 Abstract</summary>
  Constructing syntactically correct and cryptographically valid message sequences is essential for protocol state machine learning, conformance testing, and fuzzing. Unlike plaintext protocols, cryptographic protocols involve complex cross-message state dependencies and cryptographic computation constraints. Existing automated approaches predominantly target text-based or plaintext protocols, leaving cryptographic message construction largely manual. We present SeriCrypt, an LLM-driven, context-a...
  </details>

- **2026-08-25** — Qiuyu Zhu, Yi Gao, Zhichao Wan et al. — [HMGCLIP: Heterogeneous Multi-Granularity Contrastive Learning for E-commerce Representation Learning](http://arxiv.org/abs/2608.24467v1)
  <details><summary>📄 Abstract</summary>
  Although recent Multimodal Large Language Models (MLLMs) have advanced general product understanding, they implicitly encode product information into global embeddings, thereby limiting their ability to capture fine-grained attributes. This limitation hinders performance in tasks requiring precise attribute discrimination, such as distinguishing subtle material differences among visually similar products. To address this challenge, we propose HMGCLIP, a unified multimodal embedding framework. By...
  </details>

- **2026-08-25** — Zhi-Kai Chen, Jun-Jie Tao, Wei-Xiang Mao et al. — [ResiSpec: Enhancing Multi-Candidate Speculative Sampling via Residual Distribution Shaping](http://arxiv.org/abs/2608.24411v1)
  <details><summary>📄 Abstract</summary>
  The efficiency of Large Language Model (LLM) serving is fundamentally limited by the sequential nature of autoregressive decoding. Speculative Decoding (SD) mitigates this by using a lightweight draft model to speculate future tokens, which are then validated by the LLM in a single parallel forward pass. To further boost efficiency, multi-candidate schemes propose diverse candidate sets to increase the likelihood of token acceptance. However, we show that these schemes are bottlenecked by Residu...
  </details>

- **2026-08-25** — Hongjiang Lei, Jianshuo Geng, Ki-Hong Park et al. — [Resource Allocation for Secure Dual-UAV-Assisted ISAC System](http://arxiv.org/abs/2608.24398v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing and communication (ISAC) is a rising technology in the next wireless communication networks, enabling the simultaneous execution of communication and sensing tasks by fully utilizing limited spectrum resources. In this work, we investigate the secrecy performance of a dual-uncrewed aerial vehicle (UAV)-assisted secure ISAC system. Specifically, a base station UAV communicates with users and transmits radar signals to locate potential eavesdroppers, while simultaneously providi...
  </details>

- **2026-08-25** — Guoyang Xu, Hao Chen — [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](http://arxiv.org/abs/2608.24302v1)
  <details><summary>📄 Abstract</summary>
  Long-video understanding depends critically on how a limited model context is constructed from a much longer video. Existing approaches improve this process through compression, retrieval, memory, and agentic evidence acquisition, but these mechanisms are typically introduced as part of a manually designed inference system or optimized together with other components. This makes it difficult to isolate a simpler question: how much can be gained by improving the executable context-construction pro...
  </details>

- **2026-08-25** — Zahra Seyedghorban, Egor Klimov, Arie van Deursen et al. — [Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering](http://arxiv.org/abs/2608.24271v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model-based multi-agent systems are increasingly explored for software engineering tasks, but they remain difficult to inspect, debug, and evaluate under controlled failures. We present llmmas-otel, a lightweight and framework-agnostic tool that combines OpenTelemetry-based distributed tracing with fault injection for LLM-based multi-agent systems in software engineering workflows. The tool instruments agent executions with trace-aligned telemetry across workflow phases, agent ste...
  </details>

- **2026-08-25** — Su Myat Noe, Ha Thanh Nguyen, May Myo Zin et al. — [Beyond Accuracy: A Dual-Judge Evaluation Protocol for Vision-Language Models in Legally Grounded Tasks](http://arxiv.org/abs/2608.24258v1)
  <details><summary>📄 Abstract</summary>
  AI systems are increasingly evaluated for legally accountable settings, where correct outputs must also be justifiable against an applicable legal standard. Existing legal-AI benchmarks and LLM-as-judge protocols provide important infrastructure for measuring task performance and open-ended response quality. We contribute one additional evaluation signal: a dual-judge protocol that pairs a standard 0-10 quality judge with a strict binary semantic-equivalence judge against a human-curated referen...
  </details>

- **2026-08-25** — Nian Li, Chonggang Song, Jingtao Ding et al. — [Tlow: Flow-based Item Tokenizer for Recommendation](http://arxiv.org/abs/2608.24176v1)
  <details><summary>📄 Abstract</summary>
  Item tokenizer encodes semantic embeddings into token IDs to replace the randomly assigned item IDs used in traditional recommendation models, fundamentally addressing the problems of excessive parameters and cold starts. However, the most common tokenizer, RQ-VAE, suffers from low decoding efficiency due to the inherent dependencies among its codebooks. Meanwhile, efficient independent tokenizers such as optimized product quantization (OPQ) still struggle with dimensional correlations and distr...
  </details>

- **2026-08-25** — Ryo Kamiya, Hiroshi Kera, Kazuhiko Kawamoto — [What Does Prompt Learning Change? -A Natural-Language Concept Analysis of Vision-Language Models](http://arxiv.org/abs/2608.24142v1)
  <details><summary>📄 Abstract</summary>
  Prompt learning adapts vision-language models such as CLIP by optimizing continuous prompt vectors, but the learned prompts are difficult to interpret in natural language. We present PromptSpLiCE, a post-hoc method that expresses each class-conditioned text embedding as a sparse combination of concepts from a fixed natural-language dictionary. Using the same dictionary before and after prompt learning allows us to compare changes in their concept profiles. We evaluate PromptSpLiCE on CoOp, a rep...
  </details>

- **2026-08-25** — Siyi Xie, Xuanke Shi, Jinsheng Quan et al. — [TransPhy: Visual In-Context Learning for Physically Grounded Image Editing](http://arxiv.org/abs/2608.24119v1)
  <details><summary>📄 Abstract</summary>
  Visual demonstrations provide a natural interface for specifying image transformations that are difficult to describe exhaustively with text. However, existing visual in-context learning (VICL) methods primarily focus on appearance-level relation transfer and provide limited support for physically grounded transformations, whose outcomes depend on material properties, geometry, object interactions, and environmental conditions. Given a source--target exemplar pair and a query image, physically g...
  </details>

- **2026-08-25** — Jheng-Ling Lee, Shang-Tse Chen — [Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos](http://arxiv.org/abs/2608.24093v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised representation learning for 4D point cloud videos is challenging because annotations are costly and reconstruction-based pretraining can overemphasize low-level geometric details. We propose a JEPA-style framework that learns from unlabeled spatiotemporal point clouds through latent point-tube prediction. Instead of reconstructing raw coordinates, the model masks spatiotemporal regions and predicts their target representations from visible context representations in feature space...
  </details>

- **2026-08-25** — Yihan Meng, Weijian Li, Lacra Pavel — [Safe Distributed Generalized Nash Equilibrium Seeking via Control Barrier Functions](http://arxiv.org/abs/2608.24077v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we consider generalized Nash equilibrium (GNE) seeking in non-cooperative games with coupled constraint sets. Specifically, we aim to enforce safety for distributed GNE seeking, whereby the safety specifications are encoded in the coupled constraint set. To achieve this, we introduce the control barrier function (CBF) in the design of the GNE seeking dynamics. We design the dynamics for both full- and partial-information setting, where each player has knowledge of the decision inf...
  </details>

- **2026-08-25** — Haotian Zhang, Shucun Wang, Jinze Wu et al. — [Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing](http://arxiv.org/abs/2608.24005v1)
  <details><summary>📄 Abstract</summary>
  Knowledge Tracing (KT) aims to assess students' dynamic knowledge states from their learning histories. While most existing KT methods focus on single-domain learning with notable success, real-world learning scenarios often involve multiple domains simultaneously, introducing two critical factors: 1) Cognitive load, arising from managing learning across domains in both temporal and knowledge dimensions. 2) Knowledge transfer, where knowledge states in one domain influence related states both wi...
  </details>

- **2026-08-25** — Olympia Saha, Amy Wang, Srinivasan Manoharan — [Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation](http://arxiv.org/abs/2608.23992v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents invoke external tools to retrieve and reason over information beyond pretrained knowledge. The Model Context Protocol (MCP) standardizes how such tools are surfaced, and a proxy MCP server aggregates many backend servers behind a single endpoint providing a secure, governable chokepoint for authentication, policy enforcement, and observability. This architecture creates two compounding challenges: a context-engineering bottleneck where full tool schemas saturate...
  </details>

- **2026-08-25** — Andrew Hu — [Evolutionary Recurrent Decision Model in Developing Adaptive and Maladaptive Behaviors](http://arxiv.org/abs/2608.23932v1)
  <details><summary>📄 Abstract</summary>
  This study introduces the evolutionarily recurrent decision model (ERDM), a computational reinforcement learning framework designed to examine how evolutionary mismatch, bounded rationality, and satisficing contribute to adaptive and maladaptive behavior. ERDM simulates agents across evolutionary recurrent environments, including threat, prey/goal-pursuits, and alliances. Agents learn through competing rewards abstracted from survival metrics. A validity study under varying adverse childhood exp...
  </details>

- **2026-08-25** — Yumeng He, Yichen Song, Xiaotian Yang et al. — [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](http://arxiv.org/abs/2608.24212v1)
  <details><summary>📄 Abstract</summary>
  The advancement of Embodied AI necessitates high-quality simulation assets that faithfully mirror the real world. However, transforming raw visual observations into simulation-ready scenes remains challenging due to the lack of physical grounding and scene-level interactivity in current image-to-URDF methods. We propose NeoWorld-Pro, a framework that reformulates monocular scene reconstruction as procedural programming for interactive 3D environments. Leveraging the zero-shot reasoning and code ...
  </details>

- **2026-08-25** — Joshua Au Yeung, Hamilton Morrin, Vincent Ng et al. — [An Echo Chamber of One: Should AI Psychosis Be a Distinct Clinical Entity?](http://arxiv.org/abs/2608.23937v1)
  <details><summary>📄 Abstract</summary>
  "AI psychosis" has entered public and clinical discourse as a label for the onset or exacerbation of psychotic symptoms, most commonly delusions, following intensive interaction with large language model (LLM)-based chatbots. Current evidence is limited to media reports, case reports, and early observational data, yet the scale of potential exposure is considerable, and public concern has prompted responses from industry and regulators. We examine whether AI-associated psychosis warrants recogni...
  </details>

- **2026-08-25** — Zihan Liu, Ruiheng Zheng, Shaobo Zhang et al. — [Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining](http://arxiv.org/abs/2608.24814v1)
  <details><summary>📄 Abstract</summary>
  We uncover ELR collapse in language model pretraining: learning rate (LR) and parameter norm govern loss dynamics primarily through their ratio, the effective learning rate (ELR). When ELR is matched across runs, their loss trajectories collapse throughout training despite substantially different LRs and parameter norms. Across optimizers, architectures, datasets, and model scales, mean collapse errors are typically a few x 10^-3, below the seed-to-seed variation measured in a representative con...
  </details>

- **2026-08-25** — Jacy Reese Anthis, Erik Brynjolfsson, James Evans — [Method, Mind, and Morality: How People Make Sense of Artificial Intelligence](http://arxiv.org/abs/2608.24748v1)
  <details><summary>📄 Abstract</summary>
  How can humans make sense of the rapid takeoff of artificial intelligence (AI)? We studied the sensemaking dynamics of AI through an open-ended, mixed-methods study with computational text analysis of millions of AI-related newspaper articles and social media posts grounded in 57 semi-structured interviews with AI professionals in 2021 and 2023--before and after the recent surge of public interest. We identify a range of sociological frames (interpretive schemas that structure collective cogniti...
  </details>

- **2026-08-25** — Eugene Vorontsov, Yi Kan Wang, Alican Bozkurt et al. — [A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology](http://arxiv.org/abs/2608.24688v1)
  <details><summary>📄 Abstract</summary>
  Precision oncology necessitates a longitudinal model of patient state that captures cancer evolution and treatment over time, integrating multimodal observations. We introduce the oFM, a foundation model developed on a real-world oncology cohort of 1.67 million cancer patients that integrates clinical trajectories with DNA, RNA, and H&E pathology. Patient-level partitions were reserved for training, validation, and testing, with over one million patients used for training. The oFM encodes daily ...
  </details>

- **2026-08-25** — Uriel Feige, Yotam Gafni — [Fair Allocation with Optional Selling](http://arxiv.org/abs/2608.24600v1)
  <details><summary>📄 Abstract</summary>
  We consider fair allocation of indivisible goods in a setting in which agents have subjective valuation functions over the set of goods, and in addition, goods may be sold at given market prices. In this setting, a fair allocation involves {deciding which goods to sell, how to allocate the unsold goods, and how to divide the money received from the sold goods.} We adapt to this setting the definitions of share-based fairness notions, such as the maximin share (MMS) and the truncated proportional...
  </details>

- **2026-08-25** — Jinhui Guo — [Delayed Optimizer-State Transport Shapes Short-Horizon Training Decisions](http://arxiv.org/abs/2608.24593v1)
  <details><summary>📄 Abstract</summary>
  Adaptive optimizers retain gradient history in moment variables, allowing a local change in loss weighting to alter later updates. We examine whether this delayed transport is large enough to change prospective short-horizon decisions. On committed future-minibatch sequences, we differentiate eight-step AdamW trajectories through the complete model--optimizer state and select exposure-matched Math--Code loss schedules before independent evaluation. Across 12 unused 0.3M Transformer histories, fu...
  </details>

- **2026-08-25** — Maxime Lucet, Nawal Benabbou, Aurélie Beynier et al. — [Multilevel Fair Allocation under Additive Preferences](http://arxiv.org/abs/2608.24400v1)
  <details><summary>📄 Abstract</summary>
  We study multilevel fair resource allocation with tree-structured hierarchical relations among agents. At each level, the problem can be viewed locally as allocating an agent's bundle to its children, the overall allocation being a trace of this process iterated down to the leaves. Assuming that internal nodes' utilities are the utilitarian welfare of their children, and the leaves have classical additive utilities over items, we first propose multilevel adaptations of usual envy-based fairness ...
  </details>

- **2026-08-25** — Jeffersson A. Agudelo Rueda, Julia E. Stawarz, Luca Franci et al. — [Anomalous Electric Fields in Earth's Turbulent Magnetosheath: Insights From 3D Hybrid Simulations](http://arxiv.org/abs/2608.24326v1)
  <details><summary>📄 Abstract</summary>
  In both collisional and collisionless plasmas the presence of a broad range of electromagnetic and plasma fluctuations provides anomalous electric fields that can be important for the dynamical evolution of the system as it is the case of magnetic reconnection, plasma turbulence and dynamo theory. In the context of plasma turbulence at scales larger than the ion's inertial length, the plasma satisfies the frozen-in condition, and the anomalous electric fields are produced by correlations between...
  </details>

- **2026-08-25** — Junyeong Maeng, Eunsong Kang, Heung-Il Suk — [STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation](http://arxiv.org/abs/2608.24237v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal radiology report generation (LRRG) requires identifying both current findings and their changes relative to a prior study. Existing methods jointly model diagnosis, attribute estimation, temporal comparison, and language generation within implicit representations, which can cause task interference, obscure the evidence underlying each decision, and limit error traceability. They also model progression states as independent labels, ignoring their ordered structure and thus treating m...
  </details>

- **2026-08-25** — Youcheng Zong, Runda Jia, Dakuo He — [LLM-Guided Contextual Action Evaluation for Operational Decisions in Industrial Processes](http://arxiv.org/abs/2608.24156v1)
  <details><summary>📄 Abstract</summary>
  Industrial actor--critic methods usually represent continuous actions as anonymous numerical coordinates. They must therefore learn from limited interactions which process variables each action affects, in which direction, and after what delay. Fixed industrial documents already describe part of these relations, but their open-text statements neither represent the current operating condition nor directly fit a numerical policy. This article presents LLM-Guided Contextual Action Evaluation for Op...
  </details>

- **2026-08-25** — Xing-gang Mao, Xiao-yan Xue — [A Unified Exact Factorial-Moment Theory for Multi-set Allocation Occupancy (MAO) in Finite Populations](http://arxiv.org/abs/2608.23998v1)
  <details><summary>📄 Abstract</summary>
  Let $A_1,\ldots,A_T$ be independent uniformly selected subsets of a finite population of size $n$, with prescribed cardinalities $m_1,\ldots,m_T$. For each population element, define its occupancy level as the number of selected subsets containing it. Let $x_t$ and $x_{\geq t}$ denote the numbers of elements with occupancy exactly $t$ and at least $t$, respectively.   The 2025 work introduced a general multi-set allocation occupancy (MAO) representation for higher-order occupancy moments. The pr...
  </details>

- **2026-08-25** — Nejla Ghaboosi — [Giraffe: A Mapping Architecture from Hidden Text Representations to Visual Embeddings for Efficient Graphic Design](http://arxiv.org/abs/2608.23970v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made significant progress in understanding and interpreting mul- timedia content. However, their ability to generate me- dia remains limited. Recent approaches have attempted to bridge this gap by translating the hidden representations of token sequences into the embedding space of visual models or directly into raw image data. However, these methods often represent each image using multiple specialised to- kens which significantly increases the inpu...
  </details>

- **2026-08-24** — Paul Vautravers, Oliver Chalkley, Gabriel Downer et al. — [Quantifying System-Level Harms from AI Adoption in Complex Sociotechnical Systems](http://arxiv.org/abs/2608.23906v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) is increasingly integrated into complex sociotechnical systems, including Critical National Infrastructure (CNI), where harms emerge from interactions between technical, human, and organisational elements. Yet current AI evaluation remains model-centric, offering little insight into how observed behaviours might translate into system-level risk. We propose a framework that links structured hazard analysis, component-level testing, and probabilistic system modelling t...
  </details>

- **2026-08-24** — Jeong-gi Kwak, Sho Kagami, Yuki Ono et al. — [DDMS: Discriminative Distillation of Multi-view Foundational Features into Single-view Models](http://arxiv.org/abs/2608.23850v1)
  <details><summary>📄 Abstract</summary>
  Foundational visual features such as DINO have played a critical role across modern computer vision, and have recently become key components in multi-view feed-forward geometry estimators. In this work, we demonstrate that by re-distilling these multi-view models---their internal knowledge of 3D geometry---into a single-view estimator, we can obtain enhanced 3D consistent foundational features. Our key idea is to construct a multi-view teacher by fusing pretrained 2D foundation features with mul...
  </details>

- **2026-08-24** — Abdullah Shouaib, John Zapanta, Sean P. Davern et al. — [Finch: Toxicity Dose Response Curve Prediction of Chemical Compounds and Mixtures](http://arxiv.org/abs/2608.23821v1)
  <details><summary>📄 Abstract</summary>
  A holistic approach to chemical mixtures is reshaping risk assessment emphasizing mixture testing over single compounds eliminating animal testing and advancing modeling methods. Most computational models still focus on individual chemicals and conventional mixture models like concentration addition and independent action are limited they struggle with multiple Modes of Action and often miss synergistic or antagonistic effects. Regulatory agencies need faster more efficient models that go beyond...
  </details>

- **2026-08-24** — Tianchi Liu, Zeyang Song, Tianrui Wang et al. — [EmoTra-TTS: Smooth Intra-Utterance Emotion Transitions for Speech Synthesis](http://arxiv.org/abs/2608.23791v1)
  <details><summary>📄 Abstract</summary>
  Psychological research on emotion dynamics has established that human affect is a continuous, evolving process: emotions rise, decay, and transition within seconds. Current emotional text-to-speech (TTS) systems, however, condition on a single discrete label or static embedding per utterance, fundamentally misaligning with the temporal nature of affect. While recent LLM-based TTS systems may implicitly vary prosody through text understanding, such variation is neither explicitly controllable nor...
  </details>

- **2026-08-24** — Katrina Honigs, Graham McDonald, Peter M. McDonald — [An approach to curves in abelian surfaces using Fourier--Mukai and quadratic forms](http://arxiv.org/abs/2608.23779v1)
  <details><summary>📄 Abstract</summary>
  It was proven by Yoshioka that given a complex abelian surface $A$ of Picard rank $1$ whose primitive polarization is non-principal of type $(1,d)$, there is an isomorphism $Ψ:\mathrm{Hilb}^d_A\times\hat{A}\to M_{\hat{A}}(0,\hat{l},-1)$ where $\mathrm{Hilb}^d_A$ is the Hilbert scheme of lenth-$d$ subschemes of $A$ and $M_{\hat{A}}(0,\hat{l},-1)$ is a moduli space of Gieseker-stable sheaves on the dual abelian surface. Specifically, $M_{\hat{A}}(0,\hat{l},-1)$ parametrizes rank $1$ torsion-free s...
  </details>

- **2026-08-24** — Yang Yu, Yilin Jiang, Zexuan Fei et al. — [ADE: Agentic Data Evolution Framework for Human-Centered Objectives](http://arxiv.org/abs/2608.23719v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models to human-centered objectives is difficult when targets are non-executable and context-dependent, limiting reliable verification and scalable supervision. Although synthetic data expands coverage, weak verification shifts the bottleneck from generation to selection. Noisy signals destabilize iterative refinement and can cause silent regressions. We propose Agentic Data Evolution (ADE), a data-centric framework that organizes synthetic supervision as evolving data sn...
  </details>

- **2026-08-24** — Penghui Qi, Xiangxin Zhou, Wee Sun Lee — [Best Practice Critic Optimization](http://arxiv.org/abs/2608.23566v2)
  <details><summary>📄 Abstract</summary>
  Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop **Best Practice Critic Optimization (BPCO)**, a recipe that combines DPPO, value predictions bounded to the reward range, Monte Carlo value targets, unnormalized ...
  </details>

- **2026-08-24** — Yiren Lu, Xin Ye, Jiaming Liu et al. — [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](http://arxiv.org/abs/2608.23486v2)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forci...
  </details>

- **2026-08-24** — Xinjian Zhao, Xiangru Jian, Yaoyao Xu et al. — [MolEmb: Multimodal Large Language Models Can Be Strong Molecular Embedding Models](http://arxiv.org/abs/2608.23646v1)
  <details><summary>📄 Abstract</summary>
  Molecular embedding models can serve as foundational infrastructure for computational chemistry and drug discovery, where reusable vector representations support property prediction, virtual screening, and retrieval. Most molecular encoders are specialist models built around a single molecular view, producing unconditional vectors with no language interface for varying the representation. We ask whether multimodal large language models (MLLMs), which natively process images, text, and symbolic i...
  </details>

- **2026-08-24** — Xiao Liu, Haoyang Li, Songwei Li et al. — [Markets, Not Planners: Decentralized Orchestration of LLM Agents with Private Information](http://arxiv.org/abs/2608.23867v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents proliferate, built by different parties and with different capabilities and costs, orchestrating them is more like assembling labor across the economy than a computer calling a subroutine. Existing orchestration is typically centralized, with a single planner assigning every task, but this creates a bottleneck as agent pools grow, requires private information (e.g., agents' execution costs), and can easily be manipulated, such that a single inserted preference nearly doubles a favo...
  </details>

- **2026-08-24** — Sathishkumar Sivashanmugam — [Elastic KV Cache for LLM Serving:A Working Reclamation Mechanism, and Why Chunked Prefill Already Closes the Gap](http://arxiv.org/abs/2608.23658v1)
  <details><summary>📄 Abstract</summary>
  An LLM serving engine sizes its key-value (KV) cache once, at startup, permanently setting aside a reserve for the worst-case prefill activation. During decode-dominant phases that reserve sits idle, yet it cannot be handed to the KV pool because it is exactly the memory a large prefill needs. We ask whether this reserve is reclaimable, and build a mechanism to test it. Our elastic KV cache lends the reserve to the KV pool during decode and returns it before prefill, driven by the scheduler's on...
  </details>

- **2026-08-24** — Ismail Lamaakal, Chaymae Yahyati, Yassine Maleh et al. — [Continual Visual Learning under Evolving Semantic Concept Shift](http://arxiv.org/abs/2608.23903v1)
  <details><summary>📄 Abstract</summary>
  Visual foundation models are commonly adapted under the assumption that the appearance of incoming data may change while the semantic meaning of the prediction task remains fixed. In long-lived visual systems, however, taxonomies, policies, and concept definitions can themselves evolve, causing the same visual evidence to require a different interpretation. We study this setting as evolving semantic concept shift and introduce SemReWrite, a framework for selectively updating obsolete visual--sem...
  </details>

- **2026-08-24** — Leila Khaertdinova, Anna Anikina, Claudia Mello-Thoms et al. — [Predicting Radiologist Expertise from 3D Gaze Patterns During CT Interpretation](http://arxiv.org/abs/2608.23836v1)
  <details><summary>📄 Abstract</summary>
  Accurate interpretation of volumetric CT requires efficient navigation of 3D image volumes and attention to diagnostically relevant regions. While eye-tracking has been widely studied in 2D medical imaging, its use for expertise assessment in CT settings remains limited. We propose a gaze-informed transformer framework for expertise classification in thoracic CT. Using a DINOv2 backbone, radiologist fixation patterns are integrated into volumetric feature learning through (1) a learnable log-spa...
  </details>

- **2026-08-24** — Mian Zhang, Yueqin Yin, Kaiyu He et al. — [Mitigating Exploration Bias in RL for Multi-Instruction Following](http://arxiv.org/abs/2608.23830v1)
  <details><summary>📄 Abstract</summary>
  RL has emerged as a powerful paradigm for enhancing the instruction following capabilities of LLMs. While existing training recipes achieve substantial gains, we find that they suffer from exploration bias towards easy instructions when the training data has multiple instructions in a prompt. This bias is caused by two main reasons: 1) the policy model's initial ability to satisfy hard instructions is too low to trigger successful exploration during RL training, so the optimization is biased tow...
  </details>

- **2026-08-24** — Stephen Chung, Wenyu Du, William J. Wesley — [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](http://arxiv.org/abs/2608.23691v1)
  <details><summary>📄 Abstract</summary>
  We study autonomous mathematical discovery in the Station, an open-world multi-agent environment in which AI agents from different model families pursue a shared research goal without a central coordinator or scripted pipeline. Agents choose their own research directions, conduct experiments, collaborate, and build a shared scientific literature. Across 12 construction problems from the AlphaEvolve catalogue and two additional case studies, the Station obtained results novel relative to the prio...
  </details>

- **2026-08-24** — Hamid Bekamiri, Jan Auernhammer, Milad Abbasiharofteh et al. — [Systematic Bias in Green Patent Classification: Silent Green and False Green](http://arxiv.org/abs/2608.23420v2)
  <details><summary>📄 Abstract</summary>
  Green-patent indicators based on Cooperative Patent Classification Y02 tags increasingly inform research, industrial policy, and climate-oriented investment, yet their construct validity has not been evaluated at corpus scale. We ask whether Y02 classification errors are random measurement noise or systematic, direction-specific bias. We introduce an Error-as-Signal framework in which disagreement between an administrative label and an independent model is treated as evidence of potential measur...
  </details>

- **2026-08-24** — Penghui Qi, Xiangxin Zhou, Wee Sun Lee — [How to Train a Critic Stably and Efficiently](http://arxiv.org/abs/2608.23566v1)
  <details><summary>📄 Abstract</summary>
  Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop \textbf{Best-Practice Critic Optimization (BPCO)}, a recipe that combines DPPO, value predictions bounded to the reward range, Monte Carlo value targets, unnormal...
  </details>

- **2026-08-24** — Thanh-Khoi Nguyen, Thanh-Nhan Vo, Trong-Thuan Nguyen et al. — [Action-Aligned Retrieval with Pairwise Multimodal Reranking for Text-Based Person Anomaly Search](http://arxiv.org/abs/2608.23503v1)
  <details><summary>📄 Abstract</summary>
  Text-based person anomaly search requires distinguishing individuals based on fine-grained, context-dependent behaviors rather than mere appearance. Existing methods struggle to capture these context-conditioned actions, frequently relying on isolated skeletal geometry, discarding raw query details during reformulation, or utilizing absolute pointwise scoring for multimodal verification. To address these limitations, we propose \textbf{ActPair}, a unified three-stage coarse-to-fine framework tha...
  </details>

- **2026-08-24** — Yiren Lu, Xin Ye, Jiaming Liu et al. — [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](http://arxiv.org/abs/2608.23486v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forci...
  </details>

- **2026-08-24** — Guilherme Rodrigues-Fontenele, Gabriel Fontenele, Ângelo Malachias et al. — [Defect-Mediated Nucleation and Dynamics across the Phase Transition in the Excitonic Insulator Candidate Ta2NiSe5](http://arxiv.org/abs/2608.23438v1)
  <details><summary>📄 Abstract</summary>
  Ta2NiSe5 is a quasi-one-dimensional material that exhibits a structural and electronic phase transition from a low-temperature monoclinic (semiconductor) to a high-temperature orthorhombic (semimetal) phase at approximately TC = 326 K. Here, we used variable-temperature scanning tunneling microscopy and spectroscopy to resolve the phase transition spatially, identifying the distinct spectroscopic signatures of the monoclinic and orthorhombic phases in pristine regions and near isolated point-def...
  </details>

- **2026-08-24** — Federico Stella, Fei Jiang, Zhongshi Jiang et al. — [Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers](http://arxiv.org/abs/2608.23410v1)
  <details><summary>📄 Abstract</summary>
  Photorealistic novel view synthesis of people remains challenging at high spatial resolutions and across multiple target cameras, where preserving identity, fine appearance details, and geometric coherence is critical. We build on the next-scale autoregressive paradigm and adapt it for human-centric view synthesis by enabling higher image resolutions, multi-view outputs and stronger cross-view consistency in a single forward pass. We train on a synthetic dataset of human faces spanning diverse i...
  </details>

- **2026-08-24** — Hao Liu, Steven Liu, Xin Zhang et al. — [DPIAgent: Divide, Protocol, Isolate for Agentic Reproduction Test Generation](http://arxiv.org/abs/2608.23341v1)
  <details><summary>📄 Abstract</summary>
  Reproduction test generation, producing a failing-then-passing test that captures a reported bug, is a critical step in automated software engineering. Existing agentic methods treat this as a monolithic loop, despite the task inherently comprising two subtasks of distinct nature: diagnosing the root cause and writing a fail-to-pass test. Without explicit separation, the agent faces a compound objective with underspecified intermediate goals, leading to goal drift. We propose DPIAgent, a structu...
  </details>

- **2026-08-24** — Haoyi Zhong, Fang-Lue Zhang, Andrew Chalmers et al. — [Mover360: Controllable Object Manipulation in 360° Panoramic Images](http://arxiv.org/abs/2608.23238v1)
  <details><summary>📄 Abstract</summary>
  We present Mover360, a controllable object manipulation framework for 360° images. Unlike perspective images, 360° images in equirectangular projection (ERP) exhibit horizontal wrap-around, latitude-dependent distortion, and global scene continuity, which makes object-level edits difficult for existing perspective editors to produce and for users to specify. To address this, Mover360 centers on object Translation (relocating a specified object within an existing panorama) while supporting refere...
  </details>

- **2026-08-24** — Fan Xu, Luis A. Leiva — [Training-Free Pseudo-Fusion for Composed Image Retrieval with Diffusion Models and Multimodal Large Language Models](http://arxiv.org/abs/2608.23102v1)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) is an emerging paradigm in content-based image retrieval that enables users to formulate compositional queries by combining a reference image with an auxiliary modality, usually text-based. This approach supports fine-grained search where the target image shares structural elements with the user-provided image while incorporating the modifications specified by the auxiliary text. Conventional CIR methods rely on multimodal fusion to combine visual and textual featu...
  </details>

- **2026-08-24** — Xiwei Liu, Yulong Li, Xinlin Zhuang et al. — [Grounding Isn't Knowing: Do VLMs Need Object Localization for Spatial Reasoning?](http://arxiv.org/abs/2608.23074v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can answer spatial questions, yet the mechanisms connecting object grounding to spatial reasoning remain poorly understood. It is underexplored whether spatial reasoning internally requires precise objects localization, or can bypass explicit localization through global layout cues. In this work, we investigate two representative model families, LLaVA-1.5 and Qwen2.5-VL, using a suite of mechanistic interpretability tools, including token ablation, layer-wise probin...
  </details>

- **2026-08-24** — Ha Dinh, Xuan Duy Ta, Khoat Than et al. — [Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling](http://arxiv.org/abs/2608.23048v1)
  <details><summary>📄 Abstract</summary>
  Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs). However, existing learnable-mask approaches incur substantial parameter and memory overhead, limiting their scalability to large models and aggressive sparsity regimes. In this work, we revisit semi-structured pruning from a perspective that reconciles efficiency with scalability. We propose Reservoir of Importance (RoI), a lightweight semi-structured pruning framework that learns...
  </details>

- **2026-08-24** — Yinze Hu, Hongjun Xiang, Xingao Gong et al. — [A Physical Response-and-Memory Model for Muon Optimization](http://arxiv.org/abs/2608.22994v1)
  <details><summary>📄 Abstract</summary>
  Training large language models is costly. How low a loss the same compute can ultimately reach depends on how each step's gradient is converted into a weight update; the rule that performs this conversion is the optimizer. From SGD and AdamW to the recent Muon, effective update rules have mostly been shaped by engineering intuition and then selected on benchmarks. Muon semi-orthogonalizes the momentum matrix before applying the update and has kept breaking records on public training benchmarks; ...
  </details>

- **2026-08-24** — Jiří Vyskočil, Franz Pöschel, Andreas Knüpfer — [Concepts for Securing Agentic AI Coding and the Terok Environment](http://arxiv.org/abs/2608.22930v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is a fascinating new tool for software development. It is a huge step forward compared to "conventional" AI assisted coding, which in turn was a considerable breakthrough earlier. AI support through LLMs is a young and very fast-moving field. The "conventional" (non-agentic) flavor became useful and productive in early 2025 (around 18 months ago) and the agentic flavor followed in fall 2025 (approximately 9 months ago). Besides all its benefits and potential, it also carries some fund...
  </details>

- **2026-08-24** — Yusheng Zheng, Xiaoyu Song, Yanpeng Hu et al. — [When Can Agents Safely Checkpoint, Fork, Restore, and Merge? Exact Checking for Execution Edits](http://arxiv.org/abs/2608.22928v1)
  <details><summary>📄 Abstract</summary>
  Agent runtimes can Checkpoint an execution, Fork it, Restore a checkpoint, or Merge branches without restarting a task. We call these operations execution edits, with Checkpoint recording the current execution for later use and Fork, Restore, and Merge changing what the Agent will do next. An execution edit cannot undo an earlier authorization or a tool request already sent. An unsafe edit can therefore authorize the same tool action twice, discard a result the task still requires, or conflict w...
  </details>

- **2026-08-24** — Pornthep Ukosaramig, Kobkrit Viriyayudhakorn — [TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor](http://arxiv.org/abs/2608.22917v1)
  <details><summary>📄 Abstract</summary>
  We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers. An unmodified open-weight LLM (Qwen3.6-35B-A3B on vLLM) is grounded on a ~30.6K-chunk Thai index by a hybrid dense-sparse retriever with cross-encoder reranking; a first-turn query classifier forces tool-based retrieval for entity lookups; a rule-based safety layer enforces medical sco...
  </details>

- **2026-08-24** — Akifumi Wachi, Takumi Tanabe, Youhei Akimoto — [Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling](http://arxiv.org/abs/2608.22915v1)
  <details><summary>📄 Abstract</summary>
  Inference-time pipelines often sample multiple outputs, filter them with a learned safety model, and return the proxy-feasible output with the highest learned reward. We show that this composition creates a two-stage failure: an imperfect safety proxy first contaminates the feasible set with unsafe outputs, and reward maximization can then amplify this residual contamination. We define \emph{safety hacking} as selecting an output that passes the learned constraint but violates the true safety cr...
  </details>

- **2026-08-24** — Sahong Park, Suhwan Park, Hoyoung Lee et al. — [Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron](http://arxiv.org/abs/2608.22852v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in investment decision-making, yet prior work shows that they exhibit systematic, model-specific investment preferences. We study whether a model's overall investment stance can be calibrated to a specified direction and strength. We introduce an investment-bias dial, an inference-time intervention on a single neuron that continuously adjusts a model-level decision prior---its overall tendency toward buying or selling---without targeting specifi...
  </details>

- **2026-08-24** — Ziyuan Wang, Bohao Tang, Fei Zhang et al. — [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](http://arxiv.org/abs/2608.22849v1)
  <details><summary>📄 Abstract</summary>
  Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution. We present RIBOSPAN, a 1.61-billion-parameter bidirectional RNA foundation model natively pretrained with context lengths up to 10,240 nt. RIBOSPAN combines dense bidirectional self-attention, single-nucleotide tokenization, and attention-isolated sequence packing to enable high-resolution modeling ...
  </details>

- **2026-08-24** — Ahnaf Atef Choudhury, Ramkrishna Saha — [SDoH-Aware Narrative Anchoring Bias in Medical LLMs for Trustworthy Clinical Decision Support](http://arxiv.org/abs/2608.22802v1)
  <details><summary>📄 Abstract</summary>
  Medical large language models are often judged by how many clinical questions they answer correctly. That view is useful, but it misses a practical risk. A model may know the right answer and still change its response when the same case is written in a different patient voice. This paper evaluates that risk as SDoH aware narrative anchoring bias. We use NarrativeShield SDoH MedQA, a counterfactual medical question answering dataset in which each case appears in persona based narratives while the...
  </details>

- **2026-08-24** — Alexander J. Hish, Arjun Nagendran, Scott N. Compton — [Performance of a domain-specific large language model in answering patient questions in psychiatry](http://arxiv.org/abs/2608.22797v1)
  <details><summary>📄 Abstract</summary>
  Background This study was designed to evaluate whether a domain-specific large language model (LLM) trained exclusively on patient education resources can answer questions about psychiatric medications, in a manner superior to LLM chatbots. We developed an LLM ("MIND") fine-tuned for clinical fidelity, trained on patient education resources from authoritative medical organizations. Methods We compared the responses of MIND, ChatGPT, and OpenEvidence to patient questions about escitalopram, using...
  </details>

- **2026-08-24** — Rui Xue, Tianfu Wu — [ReCoG: Reciprocal Co-Evolution for Multimodal Graph Learning](http://arxiv.org/abs/2608.22786v1)
  <details><summary>📄 Abstract</summary>
  Multimodal graph learning requires jointly training over graph structure and heterogeneous node attributes, yet existing methods largely decouple these processes: prior multimodal graph neural networks (GNNs) focus on aligning modalities in a shared embedding space while operating on fixed or weakly adapted graph structures, and graph structure learning approaches infer topology from unimodal node representations without accounting for multimodal interactions. This separation fundamentally limit...
  </details>

- **2026-08-24** — Xuan Yao, Li Shuping, Dai Yang et al. — [DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion](http://arxiv.org/abs/2608.22770v1)
  <details><summary>📄 Abstract</summary>
  Financial institutions need an independent way to detect missing, stale, and misclassified corporate-event records in vendor databases. We introduce Search-to-Record, a database-assurance task in which search-enabled large language models reconstruct institution-defined event records from public sources for a known security universe and historical cutoff, and DelistBench, a 1,200-record benchmark for security-level delisting announcements. We evaluate five models in paired closed-book and web-en...
  </details>

- **2026-08-24** — Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer — [The Compaction Cliff in Long-Running AI Agent Memory](http://arxiv.org/abs/2608.22752v1)
  <details><summary>📄 Abstract</summary>
  A safety rule and an episodic log compete for the same tokens in an AI agent's context. When the budget overflows, both are summarized at the same rate; only the rule needs exact wording to remain enforceable. On 20 production agent configurations, Claude Code's /compact prompt on Sonnet 4.6 preserves 53\% of safety rules after one compaction round and 10\% after five. We name this the Compaction Cliff. We address it with Knowledge Triage, a framework that classifies each line of an agent's know...
  </details>

- **2026-08-24** — Zeyang Bai, Yunpeng Wang, Yunbiao Wang et al. — [Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](http://arxiv.org/abs/2608.22740v1)
  <details><summary>📄 Abstract</summary>
  Generalizable 3D Gaussian Splatting (G-3DGS) has emerged as a promising approach for novel view synthesis undersparse-view settings. However, existing frameworks remain restricted by pixel-aligned Gaussian estimation, whichstruggles in partially observed or occluded regions and often leads to incomplete surfaces or structural collapse. Toaddress these challenges, we propose SeeU (Seeing the Unseen), a novel G-3DGS framework. We frame its core design asSemantic-in-Gaussian: semantic-conditioned r...
  </details>

- **2026-08-24** — Mining Tan, Yinuo Wang, Ziqi Zhou et al. — [Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation](http://arxiv.org/abs/2608.22757v1)
  <details><summary>📄 Abstract</summary>
  Unified models for visual understanding and generation have made rapid progress, yet they still lack the ability to understand and manipulate the spatial states of object instances. Existing models can describe objects in natural language, but they struggle to precisely represent continuous object poses and generate geometrically consistent images under target viewpoints. To mitigate this, we propose \emph{Object-Uni}, a unified model for object-centric spatial understanding and controllable gen...
  </details>

- **2026-08-24** — Erin Craig, Yiling Huang, Snigdha Panigrahi — [Interpretable AI with Local Distillation](http://arxiv.org/abs/2608.23538v1)
  <details><summary>📄 Abstract</summary>
  Modern AI models such as tabular foundation models and gradient-boosted ensembles can outpredict classical methods, but provide little basis for reasoning about their predictions. High-stakes decisions call for models that are both accurate and interpretable as built. Local linear modeling offers a path forward: a smooth regression function is locally well approximated by a linear one, allowing a linear fit near each query point to achieve high accuracy without sacrificing transparency. The chal...
  </details>

- **2026-08-24** — Stanislav Škorňa, Jitka Machalová — [Penalized likelihood estimation of probability density functions using compositional splines](http://arxiv.org/abs/2608.23512v1)
  <details><summary>📄 Abstract</summary>
  Probability density functions are commonly estimated through preliminary smoothing or aggregation procedures, e.g., histograms or kernel density estimation, before subsequent functional representation and functional data analyses. Such a two-stage approach can lead to additional approximation bias and weaken the direct connection between the observed data and the underlying distributional structure. In this paper, we propose a penalized maximum likelihood framework for direct estimation of proba...
  </details>

- **2026-08-24** — Naman Garg, Sarika Jain, George Fazekas — [Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational Music Recommendation](http://arxiv.org/abs/2608.23484v1)
  <details><summary>📄 Abstract</summary>
  We present Team Semiintelligencn's solution for the ACM RecSys 2026 TalkPlayData Challenge, addressing conversational music recommendation through a multi-modal and personalized conversational recommender system. Our submitted system employs a three-stage pipeline: (1) multi-modal retrieval constructing decay-weighted centroids across seven dense embedding spaces - track- and user-level CF-BPR, Qwen3 (metadata, lyrics, attributes), CLAP audio, and SigLIP visual - supplemented by BM25 lexical ret...
  </details>

- **2026-08-24** — Kenneth L. Kearns, M. D. Ediger, Heiko Huth et al. — [One micron length scale controls kinetic stability of low energy glasses](http://arxiv.org/abs/2608.23454v1)
  <details><summary>📄 Abstract</summary>
  AC nanocalorimetry was used to measure the reversing heat capacity Cp of low energy indomethacin glasses as they isothermally transform into the supercooled liquid. As the film thickness increases from 75 to 600 nm, the transformation time increases by more than an order of magnitude, consistent with a surface-initiated transformation mechanism. Eventually, the transformation time becomes constant for films between 1.4 and 30 microns indicating a distinct bulk transformation pathway. The observa...
  </details>

- **2026-08-24** — Hamid Bekamiri, Jan Auernhammer, Milad Abbasiharofteh et al. — [Systematic Bias in Green Patent Classification: Silent Green and False Green](http://arxiv.org/abs/2608.23420v1)
  <details><summary>📄 Abstract</summary>
  Green-patent indicators built on Cooperative Patent Classification Y02 tags are widely used in research, policy, and investment, yet their construct validity has not been audited at corpus scale. We assess whether Y02 is systematically biased and whether that bias may reinforce the ESG innovation disconnect. We introduce an Error-as-Signal framework that treats disagreement between an administrative label and an independent model as diagnostic evidence of measurement error. Screening 9,075,421 U...
  </details>

- **2026-08-24** — Seyed Mohammad Hossein Hashemi, Mohsen Hooshmand, Parvin Razzaghi — [Modalities Should Talk to Each Other: Dual-Stream Multimodal Learning for Long-Horizon Influenza Forecasting](http://arxiv.org/abs/2608.23373v1)
  <details><summary>📄 Abstract</summary>
  Forecasting long-range influenza-like illness (ILI) matters for public health readiness. Publicly available surveillance datasets typically pair numeric epidemiological signals with textual information that is noisy, loosely structured, only indirectly related to near-term trends, and often lagged relative to the numeric signal. Fusing the two therefore requires careful design. We propose Dual-Stream Attention (DSA), a multimodal deep learning framework that forecasts 12-week-ahead ILI activity ...
  </details>

- **2026-08-24** — Matthew Perlman, Atharva Nijasure, James Allan — [The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA Fine-Tuning](http://arxiv.org/abs/2608.23338v1)
  <details><summary>📄 Abstract</summary>
  LoRA fine-tuning is standard for adapting LLMs to reranking, but it remains unclear where in the network task-specific relevance behavior is learned and what attention-level changes accompany that learning. Through ablation and attention experiments, we identify where LoRA attention updates to RankLLaMA improve performance and whether those gains coincide with interpretable relevance-oriented attention patterns such as lexical matching, rarity sensitivity, and query-document interaction. We find...
  </details>

- **2026-08-24** — Zeyd Boukhers, Lingxiao Kong, Xenophon Zabulis et al. — [Automated Construction of FAIR Digital Object Knowledge Graphs from Flat Cultural Heritage Records](http://arxiv.org/abs/2608.23263v1)
  <details><summary>📄 Abstract</summary>
  The FAIR Digital Object (FDO) framework mandates that metadata attribute values be expressed as persistent identifiers (PIDs) wherever possible, to produce a fully machine-actionable graph in which every reference is resolvable. The Europeana Data Model was designed long before the FDO specification, and it stores most metadata values as plain text. This serves human browsing well enough, but gives an automated agent nothing to follow across records or collections. We present a pipeline that tra...
  </details>

- **2026-08-24** — Jinghui Zhang, Lang Gao, Ao Li et al. — [LITERARYBIGFIVE: Author-Personalized Text Generation in a Unified Interpretable Space](http://arxiv.org/abs/2608.23124v1)
  <details><summary>📄 Abstract</summary>
  Personalized text generation for authors and literary writing is essential for applications such as adaptive writing assistants, creative support tools, and computational literary analysis. However, existing approaches to author modeling and personalization often represent writing behavior as independent labels, requiring large-scale corpus collection or fine-tuning for each author or stylistic category. Such formulations are costly, difficult to interpret, and poorly suited for generalizing acr...
  </details>

- **2026-08-24** — Nafis Tanveer Islam, Nafiseh Soveizi, Yutong Li et al. — [From Metrics to Improvement: A Lifecycle-Aware LLM Feedback Framework for Research Software Quality](http://arxiv.org/abs/2608.23118v1)
  <details><summary>📄 Abstract</summary>
  Research software is increasingly central to scientific workflows, yet it is often developed by researchers with limited software engineering expertise. This can lead to quality issues that hinder maintainability, reproducibility, reuse, and sustainability. Existing static analysis tools can identify such issues, but their outputs often require expert interpretation and provide limited support for translating quality assessments into actionable improvements. To address this gap, we propose a lif...
  </details>

- **2026-08-24** — Yuanjun Feng, Tanzhou Liu, Stefan Feuerriegel et al. — [Beyond Surface Cues: Disentangling Sociocultural Signals in Multilingual LLMs](http://arxiv.org/abs/2608.23026v1)
  <details><summary>📄 Abstract</summary>
  Multilingual LLM outputs can vary across sociocultural contexts. However, evidence of cultural grounding can be misleading: identity labels may be inferred from explicit or indirect textual cues, while names and wording can reveal the source language. Treating all these signals as evidence of cultural grounding may obscure potential biases. We present a human-validated, multi-agent audit that separates three questions: whether outputs reproduce social biases, whether identity groups are represen...
  </details>

- **2026-08-24** — Suhyeon Lee, Juneha Baek, Jaehyeong Park et al. — [LLM Pedagogical Behavior in AI Tutoring Interactions](http://arxiv.org/abs/2608.22993v1)
  <details><summary>📄 Abstract</summary>
  Students increasingly use LLMs as tutors for coursework and problem solving. Little is known about the level of assistance LLMs provide when students use them as tutors in authentic learning interactions. This matters because tutoring responses can differ substantially in how directly they help students complete a task. We operationalize this dimension as scaffolding level and develop a five-level scale, validated against human annotations, that characterizes responses according to the degree of...
  </details>

- **2026-08-24** — Zeyu Wang, Xinming Xu — [Knowing Isn't Always Saying: When Do Spatial Encodings Reach Answers in Vision-Language Models?](http://arxiv.org/abs/2608.22916v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models are known to encode spatial information in their hidden states, yet often fail to use it when answering. However, it remains unclear when and where this encoded information reaches the answer. We address this with direction patching, a class-conditioned causal intervention applied across layers, token positions, and prompt formats. Using spatial-ID directions constructed following prior encoding evidence, we find that causal influence on answer logits emerges only at mid-t...
  </details>

- **2026-08-24** — Chang-Youn Moon — [Revised symmetry rule and intrinsically time-reversal symmetry breaking pairing in multi-orbital superconductors](http://arxiv.org/abs/2608.22902v1)
  <details><summary>📄 Abstract</summary>
  We investigate the basic symmetry rule for the particle permutation in superconducting (SC) pairing states by examining the numerical solution of the linearized Eliashberg equation for Sr$_2$RuO$_4$. We find that the general multi-band, frequency-dependent SC gap function does not simply transform to itself up to the minus sign with either orbital ($\hat{O}$) or frequency ($\hat{T}$) exchange between two pairing electrons, contradicting the common assumption which has been used without verificat...
  </details>

- **2026-08-24** — Zengqing Wu, Chuan Xiao — [Proxy reliance in large language model decisions is uncalibrated to predictive evidence](http://arxiv.org/abs/2608.22887v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are entering decisions in triage and lending, where task-relevant inference must be distinguished from impermissible proxy use. Current audits ask whether decisions change when demographics change. But attributes correlated with a protected group carry predictive value, so a changed decision can be discrimination or sound inference. We measure causal proxy effects in four LLMs on a clinical-ranking task with known ground truth, where the reliance the evidence warrant...
  </details>

- **2026-08-24** — Zengqing Wu, Chuan Xiao — [Predicting the scale limits of social mechanisms in agent societies](http://arxiv.org/abs/2608.22884v1)
  <details><summary>📄 Abstract</summary>
  Societies of interacting language-model agents offer a controllable and repeatable way to study collective behaviour at scales that would be difficult to test with people. Their scientific value, however, depends on whether a social mechanism that works in a small group still operates when thousands of agents interact, and testing this directly requires costly large-scale runs. Here we introduce an audit that predicts a mechanism's fate as a population grows. It asks how often the mechanism can ...
  </details>

- **2026-08-24** — Nizar Touzi, Yuxing Huang — [Backward SDE characterization of the finite horizon Principal-Agent problem](http://arxiv.org/abs/2608.22818v1)
  <details><summary>📄 Abstract</summary>
  We consider the finite horizon continuous-time Principal--Agent problem under deterministic discount factors. Following the Sannikov reduction to a stochastic control problem, we provide a further characterization of the Principal's value function in terms of a backward SDE inducing the corresponding optimal contract. In particular, this allows to bypass the fully nonlinear HJB equation satisfied by the Principal value function in the Markovian setting. This new approach allows to handle a new c...
  </details>

- **2026-08-24** — Yue Zhao — [CatchBench: When Can an Agent Failure Be Caught?](http://arxiv.org/abs/2608.22808v1)
  <details><summary>📄 Abstract</summary>
  When can an agent failure be caught? An audit is usually limited by the record rather than by the method. CatchBench therefore puts one auditor's question to three information states: the declared configuration before a run (PRE), a growing prefix of its trace (LIVE), and the finished trace (POST). Prior benchmarks fix one of these states or vary the telemetry; to our knowledge none scores all three under one task-method interface. Each state admits different questions, so seven task contracts c...
  </details>

- **2026-08-24** — Yufan Wang, Rui Yang, Yi Liu et al. — [A Source-Grounded Framework for Constructing and Evaluating Progressive Multimodal Diagnostic Dialogues from Clinical Case Reports](http://arxiv.org/abs/2608.22713v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnosis requires progressive integration of patient history, physical examination, laboratory findings, medical images, and diagnostic-informative tests. However, most multimodal medical benchmarks evaluate fixed inputs or endpoint answers, while fully interactive diagnostic agents conflate evidence selection with evidence interpretation. We present a source-grounded framework to construct progressive multimodal diagnostic dialogues from case reports and an evaluation strategy for ass...
  </details>

- **2026-08-24** — Davood Wadi, Yu Ma — [Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf](http://arxiv.org/abs/2608.22697v1)
  <details><summary>📄 Abstract</summary>
  Search rankings are valuable because human attention is scarce and sequential. Higher-placed alternatives are easier to find, so they are examined and bought more often. Consumers are now delegating search to AI agents that can ingest an entire results page at once. Randomizing the order of one hundred hotel listings across 5,000 AI agent sessions, we compare four large language models against human field data. AI agents search more deeply than humans and never decline to buy. Position still pre...
  </details>

- **2026-08-24** — Yujuan Ding, Linyin Luo, Shijie Wang et al. — [FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering](http://arxiv.org/abs/2608.22688v1)
  <details><summary>📄 Abstract</summary>
  Fashion is a knowledge-intensive domain in which effective decision-making depends on integrating multiple types of knowledge. Although Large Language Models (LLMs) have transformed many areas, their application in fashion remains limited by hallucinations and weak domain specialization. Knowledge Graph (KG)-based Retrieval-Augmented Generation (RAG) offers a promising way to add structured knowledge to LLMs. However, existing fashion KGs are typically restricted to product-level attributes or i...
  </details>

- **2026-08-23** — Hossein Javidnia — [Functional compatibility as a determinant of persistent neural learning](http://arxiv.org/abs/2608.22462v2)
  <details><summary>📄 Abstract</summary>
  Neural networks can acquire new capabilities while damaging existing ones, but what determines whether new learning persists remains unclear. We identify functional compatibility, the extent to which incoming learning can coexist with behaviour that must be preserved, as an experimentally manipulable causal determinant of persistence. From identical neural states, we vary compatibility while matching unrestricted learning opportunity and imposing a common retention requirement. Persistent learni...
  </details>

- **2026-08-23** — Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng et al. — [CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](http://arxiv.org/abs/2608.22577v2)
  <details><summary>📄 Abstract</summary>
  Long-horizon GUI agents can retain complete action histories as compact text, but only a few historical screenshots fit in active context. We formulate this as budgeted fidelity restoration: every event remains summarized, while a fixed budget $B$ determines which events regain their archived screenshots. Recent-$B$ assigns all visual slots to the latest events. CausalCache instead scores the complete history and swaps in an older event only when its predicted utility exceeds that of a recent ev...
  </details>

- **2026-08-23** — Jalen Jiang, Chufan Gao, Ethan Rasmussen et al. — [KMGen: A Skill-based Approach for Synthetic Individual Patient Data Generation](http://arxiv.org/abs/2608.22618v1)
  <details><summary>📄 Abstract</summary>
  Individual patient data (IPD) from clinical trials is the substrate for survival modeling, meta-analysis, and safety research, yet IPD is rarely released. Prior work has addressed only half of this gap: reconstructing Kaplan-Meier (KM) curves from published plots -- typically requiring manual digitization or human-in-the-loop correction -- while offering no mechanism for generating the adverse-event (AE) streams that constitute the other half of a patient record. We introduce KMGen, the first en...
  </details>

- **2026-08-23** — Zihan Lin, Zhenyu Chen, Jiawen Wei et al. — [When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents](http://arxiv.org/abs/2608.22339v1)
  <details><summary>📄 Abstract</summary>
  Extracting skills from past successes is critical for the efficient evolution of Large Language Model (LLM) agents. Prevailing agent self-evolution paradigms typically rely on a core assumption: equipping LLMs with skill memories derived from successful trajectories will monotonically improve their problem-solving capabilities. However, probe analyses reveal that extracting skills solely from successful trajectories traps the model in a \textbf{Skill Imitation Trap}. For tasks that resemble past...
  </details>

- **2026-08-23** — Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein et al. — [Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming](http://arxiv.org/abs/2608.22638v1)
  <details><summary>📄 Abstract</summary>
  Copying a function from a chat window into an editor takes less than a second. For many uses of AI coding tools, that speed is the point; in settings such as programming education, code review, and security-sensitive development, it can also be the problem. This paper frames copy-paste as an \emph{AI code handoff problem}: the moment model-generated text crosses from a conversational context into executable or committed software is a design boundary that current tools leave largely unmanaged. We...
  </details>

- **2026-08-23** — Qi Zhang, Heajun An, Prakriti Dumaru et al. — [DeepSAGE: Stage-Aware Reinforcement Learning for Structured CBT Counseling Dialogue](http://arxiv.org/abs/2608.22615v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based counseling agents can generate fluent and supportive responses, but they often lack the structured, goal-directed progression required to conduct a coherent therapeutic session. We present DeepSAGE (Strategic AI Guidance Engine), a hybrid LLM--Deep Reinforcement Learning (DRL) framework for stage-aware counseling dialogue grounded in the first session of Cognitive Behavioral Therapy (CBT). DeepSAGE represents the session as eleven stages with explicit therapeutic...
  </details>

- **2026-08-23** — Chunkai Yang, Andong Yang, Chao Gao — [WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning](http://arxiv.org/abs/2608.22591v1)
  <details><summary>📄 Abstract</summary>
  Robot policies receive heterogeneous observations at each decision step, yet sequence models differ in how they organize these inputs over time. We introduce WorldToken, a time-first policy instantiation that fuses multiview images, proprioception, and task conditioning within each policy timestep into one world token. A causal temporal Transformer models the resulting world-token sequence, and a diffusion action head generates action chunks. On 23 RoboCasa tasks, an 85.3M-parameter policy train...
  </details>

- **2026-08-23** — Vedant Khatri, Anthony Cusimano, Zachari Swiecki et al. — [From Diagnosis to Redesign: Using Quantitative Ethnography to Improve Multi-Agent LLM Reasoning](http://arxiv.org/abs/2608.22566v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) systems are designed to improve reasoning by decomposing tasks across multiple agents with specialized functions, but the presence of multiple agents does not inherently guarantee coherent reasoning or outputs that align with task objectives. This paper introduces a quantitative ethnographic (QE) approach for diagnosing and redesigning multi-agent LLM systems based on the discourse produced through agent interactions. We test this approach using automated e...
  </details>

- **2026-08-23** — Yingying Yan, Jiaqi Tang, Wei Wei et al. — [HeatTok: Enhancing Remote Sensing Image Understanding via Thermodiffusion-based Tokenization](http://arxiv.org/abs/2608.22485v1)
  <details><summary>📄 Abstract</summary>
  Current visual tokenizers in Multimodal Large Language Models (MLLMs) predominantly rely on patch-based partitioning, which causes severe semantic mixture and object fragmentation in remote sensing imagery due to the irregular contours of geo-objects. Moreover, existing adaptive methods struggle to extract precise object-level tokens and lack dedicated geometric positional encodings for irregular regions. In this paper, we propose HeatTok, a semantic-aware tokenizer driven by thermodiffusion agg...
  </details>

- **2026-08-23** — Shaoguang Wang, Weiyu Guo, Ben Fei et al. — [Diagnosing and narrowing the simulation-to-real gap in powder X-ray diffraction with a wet-dry agentic loop](http://arxiv.org/abs/2608.22400v1)
  <details><summary>📄 Abstract</summary>
  Powder X-ray diffraction (PXRD) is the routine probe of crystalline matter, yet its analysis is the rate-limiting step as laboratories automate acquisition. Deep-learning analyzers excel on simulated patterns and degrade on measured ones. This simulation-to-real gap is structural, not additive: synthetic denoising gives no measurable lift on real spectra, whereas correcting a small peak-position drift more than doubles median retrieval correlation. Real-spectrum fine-tuning, peak-aligned reranki...
  </details>

- **2026-08-23** — Yikai Zhao, Qiyan Zhao, Jiaquan Zhang et al. — [Context-Aware Cluster Decoding: Semantic Anchor-Driven Coherence in dMLLMs](http://arxiv.org/abs/2608.22367v1)
  <details><summary>📄 Abstract</summary>
  Diffusion multimodal large language models (dMLLMs) frequently produce long-form outputs marred by semantic drift and repetition, with quality generally degrading as output length increases. We identify two structural deficiencies in existing decoding methods as primary drivers of these failures: confidence-based scoring ignores decoded-neighbor support, and block partitioning prevents access to high-readiness semantic anchors, together causing tokens to be committed before their local context i...
  </details>

- **2026-08-23** — Jingbo Wang, Sendong Zhao, Haochun Wang et al. — [Analyzing and Mitigating Cross-Lingual Degradation in Multilingual Medical VQA](http://arxiv.org/abs/2608.22363v1)
  <details><summary>📄 Abstract</summary>
  Medical visual question answering (VQA) is a crucial task in clinical AI, yet its evaluation has so far centered almost exclusively on English, limiting its relevance to linguistically diverse patients and clinicians. Recent multilingual medical VQA benchmarks show that large vision-language models (LVLMs) degrade in non-English languages, but lack a fine-grained analysis of how cross-lingual variation affects the distinct capabilities that medical VQA requires. To this end, we construct a multi...
  </details>

- **2026-08-23** — Milo Piccioli, Gianluca Amprimo, Claudia Ferraris et al. — [TransHands: Repurposing Human Pose Encoders as Hand Pose Encoders](http://arxiv.org/abs/2608.22341v1)
  <details><summary>📄 Abstract</summary>
  Lifting 3D hand poses from 2D monocular representations remains challenging due to the limited availability of large-scale, diverse 3D-annotated hand datasets, in contrast to the abundance of human body motion data. We address this limitation by transferring motion representations learned from large body pose corpora to the hand domain. We introduce TransHands, a backbone-agnostic transfer learning framework that enables pre-trained human motion encoders to be effectively adapted for 3D hand pos...
  </details>

- **2026-08-23** — Lai Wei, Yuchao Chen, Zhenbiao Cao et al. — [MedReaMM: Evaluating Large Multimodal Models on Expert-Level Clinical Diagnostic Synthesis](http://arxiv.org/abs/2608.22323v1)
  <details><summary>📄 Abstract</summary>
  The application of Large Language Models (LLMs) to diagnostic decision-making has garnered growing interest. However, existing benchmarks largely focus on textual reasoning or isolated visual question-answering (VQA) tasks, lacking holistic integration of clinical narratives and medical imaging, and thus failing to assess the multimodal diagnostic synthesis capability central to expert clinical judgment. To bridge this gap, we introduce MedReaMM, a benchmark specifically designed to evaluate mod...
  </details>

- **2026-08-23** — Xunzhe Zhou, Yiyang Cai, Fengyi Wang et al. — [The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction](http://arxiv.org/abs/2608.22301v1)
  <details><summary>📄 Abstract</summary>
  Humans imitate at the level of intent: given a demonstration, we infer its goal and carry it out with whatever tools, objects, and layouts are at hand. Current robot policies instead learn observation-to-action mappings from visual inputs and language instructions, without explicitly inferring the demonstrated task. Learning from human video thus remains largely trajectory-level: models can replay motions in near-identical scenes, but still struggle to imitate what the demonstrator intends rathe...
  </details>

- **2026-08-23** — Yucheng Chen, Yang Yu, Jiazhou Zhou et al. — [UR$^{2}$-MLLM: Uncertainty-aware Revisit Reasoning in Multimodal Large Language Models for Radiology Report Generation](http://arxiv.org/abs/2608.22217v1)
  <details><summary>📄 Abstract</summary>
  Radiologists generate diagnostic reports through iterative and selective revisiting of suspicious regions to refine their interpretations. Recent multimodal large language models (MLLMs) for radiology report generation (RRG) have shifted from text-only reasoning toward a ``Thinking-with-Images'' paradigm, incorporating visual evidence into the reasoning process. However, existing methods provide static visual evidence without a dynamic revisit mechanism during reasoning, neglecting how radiologi...
  </details>

- **2026-08-23** — Ziyang Luo, Yan Yang, Xiangru Jian et al. — [MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning](http://arxiv.org/abs/2608.22167v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become an effective way to improve the tool-use ability of large language models (LLMs), but most existing RL frameworks stop at the policy update. For every new domain, the user is left with two hard systems problems: standing up an isolated environment for each of hundreds of concurrent trajectories and connecting it to training, and scheduling the rollout so that the GPU stays busy across long, multi-turn episodes that spend much of their time stalled on slow t...
  </details>

- **2026-08-23** — Xinyuan Liu, Eren Sadikoglu, Riana Chatterjee et al. — [Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs](http://arxiv.org/abs/2608.22657v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI frameworks interpret open-ended task goals and decompose them into multi-step plans. Richer information about embodiment-specific capabilities, physical preconditions, and cross-robot coordination improves grounding, but does not eliminate infeasible, mistimed, or unsafe physical actions. Physical robot crews therefore require an explicit architectural interface between semantic planning and execution, where every planned action is verified against robot capabilities, system state, an...
  </details>

- **2026-08-23** — Jie Yin, Xingyu Lai — [DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model](http://arxiv.org/abs/2608.22278v1)
  <details><summary>📄 Abstract</summary>
  Vision-based whole-body loco-manipulation on humanoid robots is challenging due to partial observability, contact-rich dynamics, and the difficulty of learning long-horizon behaviors from high-dimensional visual inputs. We present \href{https://github.com/DreamMimic/DreamMimic}{DreamMimic}, a framework that distills privileged teacher policies into vision-based humanoid controllers via world-model-assisted distillation. Instead of using a Dreamer-style RSSM for planning, we repurpose it to learn...
  </details>

- **2026-08-23** — Thomas Benton Townsend, Dimitrios Michael Manias — [Advanced LLM-Enhanced Intent-Based 5G Network Management using Dynamic Semantic Routes](http://arxiv.org/abs/2608.22644v1)
  <details><summary>📄 Abstract</summary>
  As the use of Artificial Intelligence (AI) and Large Language Models (LLMs) is becoming common in everyday applications, their ability to interpret natural language has increased significantly. An emerging application of AI is integration with network management and orchestration practices. An instance of this integration is LLM-enhanced intent-based networking, where network operators will control a network using natural language. This work presents the use of dynamic routes with a semantic rou...
  </details>

- **2026-08-23** — Thomas Hardin, Ralf Rapp — [Charmonia at Finite Momentum and Spatial Correlators in Quark-Gluon Plasma](http://arxiv.org/abs/2608.22596v1)
  <details><summary>📄 Abstract</summary>
  Spatial correlation functions of quarkonia in the quark-gluon plasma are available from finite- temperature lattice-QCD with good precision. However, their interpretation in terms of microscopic spectral functions has been challenging due to a highly oscillating momentum integral in their Fourier transform and the need for a reliable evaluation of their 3-momentum dependence. Utilizing the thermodynamic T-matrix approach we first obtain a Lorentz-covariant scattering equation by taking advantage...
  </details>

- **2026-08-23** — Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng et al. — [CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](http://arxiv.org/abs/2608.22577v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon GUI agents can retain a complete interaction trace cheaply as textual action records, but expose only a few past events to the policy in high-fidelity pixels. We formulate this as conditional fidelity restoration: each event persists in summary-only form and is linked to an archived screenshot, while an active visual-context budget $B$ limits how many events may be promoted to summary-plus-image form. Recent-$B$ spends every slot on the latest events. CausalCache instead reallocates...
  </details>

- **2026-08-23** — Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein — [ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation](http://arxiv.org/abs/2608.22559v1)
  <details><summary>📄 Abstract</summary>
  Rubrics aim to make language-model evaluation transparent by decomposing response quality into interpretable criteria. However, natural-language rubrics are often ambiguous, require black-box LLM judges, and typically assume criteria aggregate independently through linear weighted sums, limiting their ability to capture dependencies, alternatives, penalties, and override conditions. We propose ExecRubrics, a framework for representing rubrics as compact executable programs. ExecRubrics encodes e...
  </details>

- **2026-08-23** — Cevahir Koprulu, David Paz, Feng Tao et al. — [Scaling Curriculum Learning For Autonomous Driving](http://arxiv.org/abs/2608.22549v1)
  <details><summary>📄 Abstract</summary>
  Batched simulators for autonomous driving have recently enabled training reinforcement learning (RL) agents at scale, encompassing thousands of traffic scenarios and billions of interactions within a matter of days. Although such high-throughput feeds RL algorithms faster than ever, their sample-efficiency has not kept pace: As the standard training scheme, domain randomization uniformly samples scenarios, thereby consuming a vast number of interactions on cases that contribute little to learnin...
  </details>

- **2026-08-23** — Jyoti Agarwal, Kavit Patel, Bhaskar Chaudhury et al. — [Interpretable statistical feature engineering for early disruption prediction in the short pulse ADITYA tokamak](http://arxiv.org/abs/2608.22515v1)
  <details><summary>📄 Abstract</summary>
  Reliable early disruption prediction is critical for the safe operation and real-time control of tokamaks. However, machine learning based prediction frameworks have predominantly targeted medium and long pulse devices, with comparatively limited attention given to short pulse tokamaks where available warning time is inherently constrained. In this work, an interpretable machine learning framework is developed for feature engineering and early prediction of disruptions in the ADITYA using the in...
  </details>

- **2026-08-23** — Claire Vlases, Katelyn Morrison — [Addressing the Selection Problem in Explainable AI](http://arxiv.org/abs/2608.22356v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) research has produced a plethora of explanation techniques, yet user studies repeatedly show that available explanations are not effective in practice. We argue that, given the siloed nature of conventional XAI, users are struggling to select the appropriate XAI technique. Viewing XAI through a philosophical lens, we offer a formalization of what we call the selection problem: the systematic failure of XAI interfaces to bridge the gap between a user's natural-language uncert...
  </details>

- **2026-08-23** — Ergan Shang, Weijing Tang, Yinqiu He — [LLM Evaluation on Unseen Questions: Contextual Multidimensional IRT Model](http://arxiv.org/abs/2608.22295v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of large language models (LLMs) increasingly requires predicting how a model will perform on new questions or tasks before collecting large amounts of new annotations. This problem is challenging because question difficulty, scenario, and underlying capability demands can vary substantially. Simple retrospective averages may confound model ability with item characteristics. In this paper, we study a model-based evaluation framework that combines multidimensional item response theory m...
  </details>

- **2026-08-23** — Buu-Chau Truong, Nuong Thi Thuy Tran, Nabendu Pal — [Analysis of Nonnegative Observations using Gamma Model with 2 Factors (ANOGaM-2): Theory, Method and Applications with Real-life Data (including R code)](http://arxiv.org/abs/2608.22254v1)
  <details><summary>📄 Abstract</summary>
  Two-factor ANOVA is widely used in experimental studies but relies on additivity, normality, independence, and homoscedasticity. These assumptions are often violated for nonnegative, positively skewed observations. Although Box--Cox-type transformations are commonly used, they may reduce interpretability and require a subjective choice of transformation. We propose an alternative framework in which nonnegative observations affected by two factors are modeled by gamma distributions with unknown s...
  </details>

- **2026-08-23** — Philipp Steigerwald, Nico Bienlein, Jennifer Burghardt et al. — [CAIA in Practice: Field Evaluation of an AI-Assisted Support System for Text-Based Online Counselling](http://arxiv.org/abs/2608.22251v1)
  <details><summary>📄 Abstract</summary>
  Rising global demand for mental health support creates significant service delivery challenges, with asynchronous email counselling serving as a crucial low-threshold channel for accessing care. This paper presents CAIA, a co-designed AI-based tool suite that demonstrates responsible AI integration into counselling practice through seven LLM-driven functions enhanced by retrieval-augmented generation. A field evaluation involved 34 professional counsellors conducting authentic sessions with trai...
  </details>

- **2026-08-23** — Sijia Dai, Minming Li, Xiaowei Wu et al. — [The Complexity of Minimizing Subsidies in Envy-Free House Allocation](http://arxiv.org/abs/2608.22216v1)
  <details><summary>📄 Abstract</summary>
  The house allocation problem is a classical one-sided matching problem that concerns the assignment of a set of $m$ houses to $n$ agents according to their preferences, where each agent is assigned exactly one house. Among the various objectives studied in this setting, envy-freeness is one of the most widely adopted fairness criteria. As envy-free house allocations do not always exist, we address this challenge by introducing subsidies and aim to compute allocations that achieve envy-freeness w...
  </details>

- **2026-08-23** — Jiaqi Wang, Zhuo Zhang, Haining Guan et al. — [BehaviorWorldGen: Closing the Loop between Action Models and World Simulators via Controllable Behavior-Aware Structured World Generation](http://arxiv.org/abs/2608.22187v1)
  <details><summary>📄 Abstract</summary>
  Modern driving action models are increasingly improved in a self-improvement loop, where a learned world simulator imagines future observations and the resulting data is fed back to refine the action model. However, the bottleneck of this loop lies in the simulators' inability to generate behaviorally plausible responses by surrounding agents, making generated data both unrealistic in interaction and imbalanced in distribution. We introduce BehaviorWorldGen, a framework that closes the loop betw...
  </details>

- **2026-08-22** — Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Bekir Berker Türker et al. — [Real-TurnTurk: A Multimodal Turkish Corpus for Turn-Taking Prediction](http://arxiv.org/abs/2608.22071v1)
  <details><summary>📄 Abstract</summary>
  Turn-taking is a basic organizational feature of human conversation and remains difficult to model in natural, synchronous dialog systems. While existing research has explored multimodal approaches and large language models for turn-ending prediction, there is a lack of naturalistic conversational corpora specifically addressing turn-taking dynamics in Turkish. This study introduces a multimodal Turkish conversational dataset of unscripted dyadic interactions, comprising synchronized front-facin...
  </details>

- **2026-08-22** — Bartolomeo Bogliolo — [From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers](http://arxiv.org/abs/2608.22063v1)
  <details><summary>📄 Abstract</summary>
  Agents built on Large Language Models (LLMs) increasingly reach enterprise data through the Model Context Protocol (MCP), and many MCP database servers maximize flexibility by exposing a single generic SQL execution tool. This paper proposes the Domain-Oriented Tooling Pattern: instead of generating SQL at query time, the model selects from a small set of domain-aligned tools whose parameterized queries encapsulate schema navigation, joins and business rules on the server side. We formalize the ...
  </details>

- **2026-08-22** — Wooseong Chung, William Cong, Jakub Dworakowski et al. — [Ludi${}_{\scriptscriptstyle 0.1}$: An Agentic System for Socially Intelligent Robots](http://arxiv.org/abs/2608.22035v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models have substantially advanced perception and control, but natural human-robot collaboration requires more than executing isolated commands. A robot must recognize ambiguity, maintain context across turns, communicate its intentions, and revise ongoing behavior as the user's intent changes. We present $\scriptstyle\mathsf{Ludi}_{\scriptscriptstyle 0.1}$, an agentic system for socially intelligent robots that integrates interactive speech, multimodal reasoning, memory, naviga...
  </details>

- **2026-08-22** — Zongen Ren, Wei Shi, Bo Xiong et al. — [LLM-Enhanced Commit Message Generation via Issue Information: An Exploratory Study](http://arxiv.org/abs/2608.22004v1)
  <details><summary>📄 Abstract</summary>
  Commit messages help developers understand code changes, support collaboration, and improve long-term maintenance. However, the use of issue information alone as the external context for LLM-based CMG has not been systematically studied. We propose an ISsue-Augmented framework for Commit message generation (ISAC) by combining code diffs with issue information as LLM input. To support the evaluation, we construct ApacheCM-Issue, a commit-issue aligned dataset built upon ApacheCM by linking commit...
  </details>

- **2026-08-22** — Zhesheng Zhang, Jiahao Lu, Wei Liu et al. — [GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI](http://arxiv.org/abs/2608.21928v1)
  <details><summary>📄 Abstract</summary>
  In embodied AI, safety risk can be latent: a benign instruction and a safe scene become hazardous only when composed. Prior work has advanced embodied safety by varying visual contexts or evaluating execution-time dynamics, but the complementary axis of fixing the scene and varying only the instruction remains underexplored. We introduce GuardianBench, an instruction-contrastive benchmark grounded in international safety standards that isolates this latent contextual risk through 3,024 instructi...
  </details>

- **2026-08-22** — Chenghao Zhang, Canran Xiao, SaiSai Hu et al. — [Training Needs Trustworthy Worlds: Verified Synthetic Web Environments for Agent Learning](http://arxiv.org/abs/2608.21898v1)
  <details><summary>📄 Abstract</summary>
  Web agents promise to automate complex digital workflows, but their training remains limited by synthetic environments that look plausible while hiding broken links, inconsistent states, or infeasible tasks. We address the gap between scalable environment generation and trustworthy agent learning by constructing synthetic web environments that are executable, auditable, and grounded in backend state. Our framework represents each generated website as a structured scaffold of pages, navigation li...
  </details>

- **2026-08-22** — Hui Zeng, Pengfei Yang, Yanxin Chen et al. — [LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization](http://arxiv.org/abs/2608.21836v1)
  <details><summary>📄 Abstract</summary>
  Large language models have become increasingly capable agents for low-level code and kernel optimization, but isolated kernel benchmarks provide only a proxy for the deployment behavior that matters in language-model inference. We identify a benchmark-to-deployment gap: candidate kernels that appear correct and fast in standalone harnesses can exhibit different performance, safety, or phase behavior after integration into a real inference workload. We introduce LLM4LLM, a deployment-aware closed...
  </details>

- **2026-08-22** — Kun Chen, Haorong Hong, Peizhong Gao et al. — [GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?](http://arxiv.org/abs/2608.21833v1)
  <details><summary>📄 Abstract</summary>
  Recent large language models (LLMs) can operate as coding agents that build complete games from natural language requests. Game development is especially demanding because program logic, visual and audio content, interfaces, interaction and playability must function together in one executable artifact. Measuring this capability therefore requires evaluation of both game product and the development process. Existing benchmarks often assess the game development capabilities of LLMs by evaluating t...
  </details>

- **2026-08-22** — Ye Zhang, Xuehang Guo, Rui Pan et al. — [Decoupled Physical Modeling and Execution for Physics Reasoning](http://arxiv.org/abs/2608.22126v1)
  <details><summary>📄 Abstract</summary>
  Physics reasoning requires constructing a consistent model of the underlying physical system rather than relying solely on symbolic or formula-based manipulation. Although large language models have shown strong ability in solving math and coding problems, they still struggle with physics problems, as these problems entangle the physical modeling process with mathematical calculations. Humans approach physics by first building a representation of the system before performing calculations. Inspir...
  </details>

- **2026-08-22** — Gregory Druck, Ethan Smith — [RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored](http://arxiv.org/abs/2608.22118v1)
  <details><summary>📄 Abstract</summary>
  LLM responses are based on the internet (via training or RAG), and AI is now used to generate a significant amount of content online (Paredes et al., 2026), creating the potential for a self-reinforcing feedback loop. Prior work has shown that when LLMs are recursively trained on their own output, they experience model collapse (Shumailov et al., 2024): responses become less diverse, and eventually no longer resemble the original training data. In this paper, we show that a similar collapse occu...
  </details>

- **2026-08-22** — Jecia Z. Y. Mao, Hisashi Ishida, Kathryn Jung et al. — [EndoNav: Semantic-to-Geometric Grounding for Language-Guided Robotic Endoscopic Examination](http://arxiv.org/abs/2608.22093v1)
  <details><summary>📄 Abstract</summary>
  Minimally invasive procedures performed within confined anatomical spaces depend on continuous endoscopic visualization. Current robotic endoscope systems can stabilize or reposition an endoscope, but they do not possess relevant context to provide effective visualization assistance. We present EndoNav, an anatomy-grounded natural-language framework that translates high-level surgeon commands into autonomous endoscopic visualization behaviors within patient-specific sinonasal anatomy. Spoken sur...
  </details>

- **2026-08-22** — Richard Zhe Wang — [The Communication Map of a Transformer](http://arxiv.org/abs/2608.22007v1)
  <details><summary>📄 Abstract</summary>
  The components of a transformer communicate by writing to and reading from a shared residual stream, and mechanistic interpretability has mapped these connections by hand, one circuit at a time. We present the communication map, which charts every potential communication channel in a language model from weights alone, generalizing the composition score of Elhage et al. (2021) into a single coupling coefficient covering all 18 connection classes, from entire attention head circuits to single neur...
  </details>

- **2026-08-22** — Jan Novacek, Alexander Viehl, Oliver Bringmann et al. — [Ontology-based Requirements Transformation](http://arxiv.org/abs/2608.21945v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an ontology-based approach to the supply chain-aware transformation of functional and environmental load requirements given by so-called Mission Profiles (MPs). The approach aims at improving the efficiency of the engineering process through supporting the transformation process and enabling a better integration of the transformation into existing Model-based Systems Engineering (MBSE) processes. We propose a methodology and a supporting system which aids in the transformatio...
  </details>

- **2026-08-22** — Qimeng Niu, Bowen Hao, Zixuan Zhang et al. — [Enhancing Group Recommendation with Memory-Augmented Reasoning in LLM Agent](http://arxiv.org/abs/2608.21939v1)
  <details><summary>📄 Abstract</summary>
  The core challenge in group recommendation lies in modeling the dynamic evolution of user preferences and explain?ing the consensus formation process. Existing Large Language Model (LLM)-based methods, despite improved interpretability, treat interaction history as fixed text, ignoring the natural evolution of group/user preferences over time, and lacking explicit modeling of the complex group decision-making process. To address these issues, we propose AGR, a LLM-based agent, which consists of ...
  </details>

- **2026-08-22** — Jing Yu, Shengchao Chen, Yiyun Tan — [The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning](http://arxiv.org/abs/2608.21871v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards has become the dominant recipe for improving large language model reasoning, yet it presumes large human-curated task collections. Zero-data self-play removes this dependency, but existing methods vet learnability only by probing candidates and rejecting post hoc, never learning where along an environment's difficulty axis to place a task, and credit the solver with sparse terminal rewards alone. We recast zero-data self-play as a pursuit-evasion ga...
  </details>

- **2026-08-22** — Binglin Chen, Rajarshi Haldar, Max Fowler et al. — [Consistently Good vs. Occasionally Great: A Rubric for Open-Ended Feedback Quality from Humans and Machines](http://arxiv.org/abs/2608.21850v1)
  <details><summary>📄 Abstract</summary>
  Providing high-quality feedback on student work is essential for learning, yet delivering such feedback at scale remains challenging. In this paper, we focus on feedback for open-ended short answer questions in introductory programming, with the goal of nudging students toward success on reattempts without revealing the correct answer. We develop a five-criteria rubric grounded in educational literature for evaluating feedback quality: (1) acknowledging correct portions of the student answer, (2...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 595 |
| prompt-injection | 508 |
| memory-poisoning | 44 |
| tool-use-attack | 126 |
| backdoor | 426 |
| adversarial-attack | 570 |
| privacy-leakage | 3915 |
| steganography | 57 |
| misuse | 933 |
| red-teaming | 117 |
| vulnerability | 2816 |
| defense | 2571 |
| alignment | 2379 |
| robustness | 2429 |
| watermark | 340 |
| unlearning | 92 |
| agent-safety | 52 |
| benchmark | 62 |
| survey | 297 |
| other | 6788 |

---

📚 **全部 25117 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-26 19:42:51*