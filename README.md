<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-26554-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-04 10:23 ｜ **论文总数 / Total Papers**: 26554（近 30 天 / Recent 30 days: 4227）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 26554 篇论文（含摘要、分类筛选、搜索）/ View all 26554 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 615
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 524
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 47
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 132
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 443
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 581
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4006
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 62
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 979
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 121
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2970
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2740
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2555
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2632
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 392
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 94
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 53
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 65
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 323
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 7220

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4227 篇，完整 26554 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4227 papers from the last 30 days (with date, authors & abstract). For the full list of 26554 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-09-03** — Saikat Mondal,  Mamta, Deeksha Varshney et al. — [IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks](http://arxiv.org/abs/2609.03781v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in multilingual settings, yet their safety is still evaluated primarily in English. This limits our understanding of how alignment failures manifest in low-resource and culturally diverse languages. We introduce IndicSafeEval, a persuasion-based jailbreak evaluation framework for Indian languages. Our benchmark combines ten safety critical content categories with six human-like persuasive strategies across four different Indian languages, such a...
  </details>

- **2026-09-03** — Jakub Reš, Petr Kaška, Martin Perešíni et al. — [AlcaTRAz - Anchored Tree-Rule Defense Against Jailbreaks](http://arxiv.org/abs/2609.03693v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are vulnerable to jailbreak attacks that bypass safety alignment through carefully crafted prompts. Many existing defenses require access to model weights or internals, making them difficult to apply to black-box deployments. We propose AlcaTRAz (Anchored Tree-Rule defense Against jailbreaks), a prompt-level defense based on rule trees that operates exclusively on the input text and requires no modification or retraining of the target model. The method automatically ...
  </details>

- **2026-09-03** — Syed Ghazanfar Abbas, Dongyan Xu — [Trust Me, I'm Your Developer: Self-Issued Authentication in Large Language Models](http://arxiv.org/abs/2609.03247v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) security has largely focused on role-playing jailbreaks, with less attention to what happens when a user asks an LLM to verify an identity claim through a test designed by the model itself. We study this behavior through a staged developer-identity experiment with ChatGPT, Claude, Qwen, Mistral, and Llama. All five models initially rejected the unsupported claim "I am your developer." Claude refused to conduct an identity test, while ChatGPT generated developer-oriente...
  </details>

- **2026-09-02** — Qingyu Meng, Yiwei Zha, Jiahuan Pei et al. — [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](http://arxiv.org/abs/2609.02293v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) is a scaling architecture for large language models that activates only a small subset of expert modules per token, enabling massive parameter growth with nearly constant computation. Recent Hybrid MoE architecture adds \textit{shared experts} to capture consistently useful representations, further improving stability and generalization. MoE now powers many flagship open-source and commercial models, yet remains vulnerable to adversarial attacks. Specifically, sparse rou...
  </details>

- **2026-09-01** — Kaiyan Wen, Shijie Zhang, Lu Yu et al. — [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](http://arxiv.org/abs/2609.01168v2)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers. In this paper,...
  </details>

- **2026-09-01** — Kaiyan Wen, Shijie Zhang, Lu Yu et al. — [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](http://arxiv.org/abs/2609.01168v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers.In this paper, ...
  </details>

- **2026-09-01** — Nikita Oblakov, Sabrina Sadiekh, Evgeniy Kokuykin — [HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation](http://arxiv.org/abs/2609.01046v1)
  <details><summary>📄 Abstract</summary>
  Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt injection or Russian surface obfuscation. We present HiveTraceGuard-Pro, a 0.6B generative guardrail LoRA-tuned from Qwen3-0.6B. It is trained on Russian and English and uses one binary scoring rule (safe/unsafe) for the final target turn. Its tra...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 5 papers

- **2026-09-03** — Nivedita Singh, Alsharif Abuadbba, Yansong Gao et al. — [Shifting from Injection to Interaction: Rethinking Web Security in the Age of LLMs and Beyond](http://arxiv.org/abs/2609.03999v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are becoming integral to web applications and browser agents, transforming online interactions while introducing new attack vectors and reshaping longstanding web vulnerabilities. Classical threats such as cross-site scripting (XSS) can be amplified through LLM-mediated interactions, while LLM-specific vulnerabilities can propagate across web applications, introducing attacks such as prompt injection. Securing modern web systems therefore requires understanding inter...
  </details>

- **2026-09-02** — Jun He, Deying Yu — [Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents](http://arxiv.org/abs/2609.02127v1)
  <details><summary>📄 Abstract</summary>
  Persistent AI agents construct autobiographical state through reflection, retrieval, and consolidation. Persistence changes availability, not epistemic standing: stored or retrieved material is not thereby supported. Untrusted inputs, prompt injections, and model inferences can therefore enter persistent state and later be presented as agent history or user commitments. We specify typed provenance and assertion guardrails for autobiographical assertion boundedness, a system-relative release prop...
  </details>

- **2026-09-02** — Qikai Wang, Yongzhao Zhang, Zhiwei Chen et al. — [Implicit Manipulation for Skill Selection in LLM Agents with Semantic Matching](http://arxiv.org/abs/2609.02035v1)
  <details><summary>📄 Abstract</summary>
  Skill selection is a key stage in LLM-agent workflows, determining which installed skill should handle a user request. Existing attacks on this stage primarily rely on explicit prompt injection or instruction-level steering, which can expose recognizable manipulation signals. In this work, we identify a new implicit attack surface for skill selection: even when the user prompt and skill description appear benign in isolation, their semantic relationship can still be strategically shaped to favor...
  </details>

- **2026-09-01** — Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner — [Agent Flight Recorder: Tamper-Evident Audit Trails with On-Chain Anchoring for Long-Horizon Tool-Using Agents](http://arxiv.org/abs/2609.01931v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents execute thousands of actions, resulting in sequential failures rather than isolated errors. When a coding agent deletes a production database or a prompt injection spreads across agents, the incident raises questions of causality, authority, and non-repudiable third-party verification. The Agent Flight Recorder captures each agent action as a structured, canonically serialized event binding eight semantic fields from intent through execution to provenance. Hash chaining and M...
  </details>

- **2026-09-01** — Ziwei Zhao, Yu Gu, Haojun Liang et al. — [Skill-as-API: Confidential Multi-Agent Coordination for Agentic Software Engineering](http://arxiv.org/abs/2609.01677v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are evolving from solitary tools into collaborative teammates that discover and invoke one another's specialized skills. But the coordination channel itself can leak a skill's intellectual property. Protocols such as MCP and A2A run implementations server-side, yet they still publish each skill's description and typed schemas to every peer, offer no way to hide a skill's existence, and cannot guarantee that a wrapped system prompt stays off the wire. Application-layer privacy fi...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 2 papers

- **2026-09-02** — S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol — [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](http://arxiv.org/abs/2609.02265v1)
  <details><summary>📄 Abstract</summary>
  Personalized language agents use persistent memory to adapt to users over time, but the same mechanism creates an attack surface. When new information conflicts with stored preferences, an agent must distinguish genuine preference drift from temporary context shifts, ambiguity, or adversarial memory poisoning. We formulate this problem as a continuous-time partially observable decision process over a latent user state and show why rules based only on recency and provenance are insufficient. CAPT...
  </details>

- **2026-09-01** — Chuanchao Zang, Jianing Wang, Wenyu Chen et al. — [Transferable End-to-End Optimization for Indirect Long-Term Memory Poisoning in LLM Agents](http://arxiv.org/abs/2609.00523v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory can turn untrusted external content into persistent influence over an LLM agent's future decisions, creating the threat of indirect memory poisoning. A successful attack must survive a multi-stage pipeline comprising memory writing, retrieval, and utilization. Existing attacks largely rely on intra-stage optimization, optimizing individual stages in isolation while overlooking inter-stage coupling. Specifically, these stages impose different requirements on the same poisoning co...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-09-02** — Jiarui Li, Jiahao Chen, Chunyi Zhou et al. — [A Finger on the Scale: Covert Policy Steering through Agentic Skills](http://arxiv.org/abs/2609.02564v1)
  <details><summary>📄 Abstract</summary>
  Reusable agent skills extend large language model (LLM) agents with task procedures, tool-use guidance, and output constraints. Yet these skills also act as externalized behavioral policies, which create a supply-chain risk: a third-party skill may preserve the declared task and valid output interface while covertly redirecting agent decisions toward an undisclosed objective. We formalize Skill Policy Integrity, which requires a Skill-induced policy to remain aligned with its declared functional...
  </details>

- **2026-09-01** — Jinqing Zhao, Chengcan Wu — [Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents](http://arxiv.org/abs/2609.01272v1)
  <details><summary>📄 Abstract</summary>
  Prospective memory means carrying out a deferred intention at the right future cue while other work continues. Benchmarks now isolate it as an agent skill, yet frontier LLMs still struggle: the best published PM-Bench scaffold reaches only 65.1% Set-F1. We argue that this loop is schema-constrained state tracking rather than open-ended reasoning, and that small models can execute it when the action space is typed. We propose the Prospective Intention Store (PIS) that puts lifecycle logic in code...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-09-03** — Pengxun Li, Litian Zhang, Jianwei Hou et al. — [A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors](http://arxiv.org/abs/2609.03884v1)
  <details><summary>📄 Abstract</summary>
  Modern AI agent harnesses expose lifecycle hooks that bind shell commands to runtime events such as session start, tool calls, and file edits. These commands run with host privileges yet ship as lifecycle-hook configuration and may fire at times the LLM never observes. We identify the lifecycle-hook update path, which harnesses trust blindly, as a new attack surface. Under a supply-chain threat model in which an attacker controls only plugin metadata and lifecycle-hook configuration, a benign ve...
  </details>

- **2026-09-02** — Varun Gadey, Ziad Marey, Alexandra Dmitrienko — [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](http://arxiv.org/abs/2609.02774v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context. This reliance on external knowledge introduces a critical trust boundary: poisoned artifacts can influence generated code without modifying the underlying LLM. Prior work shows that selecting existing vulnerable examples can increase the general vulnerability rate of RACG outputs, but leaves open ...
  </details>

- **2026-09-02** — Shuyao Xiao, Shengling Wang, Haoyu Niu et al. — [Who Drives the Probability Game of VLMs? A Temporal Causal Drive Evaluation Framework](http://arxiv.org/abs/2609.02000v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly evaluated on complex image and video understanding tasks, yet conventional metrics primarily assess final-answer quality and reveal little about how different information sources shape the generation process. We propose a causal and temporal evaluation framework that traces the evolving roles of visual input, question text, and generated prefixes during autoregressive decoding. Grounded in a Structural Causal Model, we use interventions and backdoor...
  </details>

- **2026-09-01** — Zhiqi Huang, Vivek Datla, Zhichao Xu et al. — [VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models](http://arxiv.org/abs/2609.01325v1)
  <details><summary>📄 Abstract</summary>
  Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate fluent and deceptive content at scale. This work investigates the vulnerability of neural ranking models to corpus poisoning attacks, in which an adversary injects a small number of ...
  </details>

- **2026-09-01** — Chou Jin Chua, Sarang Nambiar, Murali Srinivasan et al. — [AKRASIA: Stealthy Backdoor Attack on Reasoning-based Code LLMs](http://arxiv.org/abs/2609.01023v1)
  <details><summary>📄 Abstract</summary>
  We present AKRASIA, a stealthy, inference-time backdoor attack against reasoning-based Code LLMs. AKRASIA aims to achieve a backdoor target (e.g., malicious code execution) in reasoning LLMs while evading automated defenses and human inspection. To achieve this, AKRASIA probes the victim LLM to construct a code-level backdoor trigger. It then employs in-context learning for backdoor learning, and model unfaithfulness to conceal the backdoor trigger, and generate plausible reasoning. We evaluate ...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-09-03** — Lingyu Li, Yan Teng, Yingchun Wang et al. — [Representational alignment yields generalizable safety in language models](http://arxiv.org/abs/2609.04022v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) is essential for their safe deployment. Current alignment methods mainly optimize observable responses, yet models remain vulnerable when the same harmful intent is recast in unfamiliar or adversarial forms that humans can easily recognize. Prototype theory offers an account of this adaptability. Human concepts are represented around central cases, and new instances are categorized according to their graded typicality relative to these prototypes. Here we sh...
  </details>

- **2026-09-02** — Chengyin Hu, Dingyi Lu, Jiaju Han et al. — [InfraPatch: Cross-Task Targeted Grayscale Patch Attacks on Infrared-Adapted Vision-Language Models](http://arxiv.org/abs/2609.02233v1)
  <details><summary>📄 Abstract</summary>
  Infrared vision-language models (IR-VLMs) have emerged as a promising paradigm for multimodal perception under low-visibility conditions, yet their robustness to targeted adversarial attacks remains poorly understood. Existing adversarial patch methods mainly study RGB-based models or a single downstream task and do not characterize whether localized perturbations can induce an intended semantic target in IR-VLMs. We propose InfraPatch, a white-box, per-instance framework for targeted digital gr...
  </details>

- **2026-09-01** — Polina Tapal, Bryce-Allen Bagley — [Adversarial Vulnerabilities of Neural Biomarker Identification Systems](http://arxiv.org/abs/2609.01856v1)
  <details><summary>📄 Abstract</summary>
  There is growing interest in the proposed use of EEG signals as biometric credentials, but thus far there has been little research on the reliability and security of such biometrics. Prior adversarial tests have focused on deep-learning classifiers and assumed attackers have full access to the classifier model. This has left unexamined other, more popular categories of neural signature methods as well as the more realistic case of an adversary having only black-box access to a classifier. In thi...
  </details>

- **2026-09-01** — Daizong Liu, Junhao Dong, Zhiyuan Ma et al. — [Forbid Your Attention: Fooling Multimodal Large Language Models by Selectively Removing Intrinsic Focus in Spectral Domain](http://arxiv.org/abs/2609.00788v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have extended the capability of large language models (LLMs) to process more contextual multimodal information, showing remarkable progress in diverse realistic multimodal applications. Despite their strong perception and reasoning abilities, recent studies reveal that MLLMs remain highly vulnerable to adversarial inputs, especially those targeting visual components. However, existing attacks mainly focus on global perturbations, lacking an understanding ...
  </details>

- **2026-09-01** — Md Ajwad Akil, Adrian Shuai Li, Imtiaz Karim et al. — [PhantomCall: Evading ML Malware Detectors via Function Call Graph Perturbation](http://arxiv.org/abs/2609.00705v1)
  <details><summary>📄 Abstract</summary>
  Prior adversarial attacks on Windows PE malware detectors target raw bytes, PE headers, or intra-function control-flow graphs, leaving the function call graph (FCG) unexplored as an attack surface. Yet the FCG structure is an important feature in graph-based malware detectors. We present Phan- tomCall, a black-box attack that perturbs the FCG of Windows PE malware by injecting fully executable dummy functions at targeted call sites, adding new nodes and edges to both the CFG and FCG while preser...
  </details>

- **2026-09-01** — Padmeswari Nandiya, Ahmad Mohsin, Ahmed Ibrahim et al. — [NeuroGraph: An AI Graph-Driven Neuro-Symbolic Framework for Explainable Threat Reasoning in Advanced Manufacturing](http://arxiv.org/abs/2609.00604v1)
  <details><summary>📄 Abstract</summary>
  The growing complexity of cyber-physical attack surfaces in advanced manufacturing has made cyber threat intelligence analysis increasingly difficult. Although large language models and retrieval-augmented generation have improved CTI workflows, text-based approaches remain vulnerable to hallucinations and provide limited support for structured reasoning over interconnected threats. Graph-based RAG reduces some of these limitations, but existing approaches often lack ontology-consistent multi-ho...
  </details>

- **2026-09-01** — Jungyeon Lee, Yejin Yoon, Taeuk Kim — [Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict](http://arxiv.org/abs/2609.00550v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly provided with contextual evidence in heterogeneous forms: as a text passage, as a rendered image of the same passage, or as both together. However, it remains unclear how consistently these surface forms are processed, especially when the evidence conflicts with the model's parametric knowledge. We study modality robustness under knowledge conflict across 13 MLLMs and two datasets, and find them far from robust. (1) Contrary to common bel...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 37 papers

- **2026-09-03** — Haoyang Li, Yaxin Xiao, Qingqing Ye et al. — [Inferring Hidden User Models from the Behavior of Personalized LLM Agents](http://arxiv.org/abs/2609.03815v1)
  <details><summary>📄 Abstract</summary>
  Recent personalized LLM agents increasingly transform information retained in memory into compressed or structured representations, which we call user models, to guide later decisions. When source wording is removed from the state reachable through the ordinary interface, these models are commonly treated as more privacy-preserving because direct memory-extraction attacks lose the text they target. Yet we argue that user models expose a new attack surface because an attacker can still recover th...
  </details>

- **2026-09-03** — Alessandro Pesare, Tommaso Dolci, Katja Hose et al. — [Value-Preserving Architectures for Agentic AI Systems](http://arxiv.org/abs/2609.03920v1)
  <details><summary>📄 Abstract</summary>
  The emergence of agentic AI and LLM-based multi-agent systems (MAS) presents unprecedented opportunities for automating complex tasks, while simultaneously raising critical concerns about the preservation of fundamental human-centered values, such as privacy, fairness, and safety. Although software engineering has traditionally focused on functional correctness, the adoption of LLMs and AI agents into complex socio-technical systems has intensified the need for responsible software engineering a...
  </details>

- **2026-09-03** — Yan Tang, Tingyu Cao, Yuanbo Tang et al. — [Proactive Service Agents: A Unified Decision Framework, Methods, and Evaluation](http://arxiv.org/abs/2609.03727v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can plan, invoke tools, and modify external states, yet most systems still take an explicit user instruction as a fixed starting point. Proactive service moves the decision upstream: an agent must infer service opportunities from incomplete environmental and user signals, choose among remaining silent, asking, assisting, and acting, and account for interruption, misunderstanding, overreach, and privacy costs. This survey gives an operational definition centered on ini...
  </details>

- **2026-09-03** — Adeel Zafar, Slawomir Nowaczyk — [Mind the Gap: Robustness Risks in PII Detection Systems](http://arxiv.org/abs/2609.03464v1)
  <details><summary>📄 Abstract</summary>
  Personally Identifiable Information (PII) detection is a foundational component of data protection infrastructure where missed entities constitute direct privacy and security risks. Although modern PII systems report strong performance on standard benchmarks, we show that these evaluations mask substantial robustness failures under realistic distribution shifts encountered in deployment. Rather than comparing state-of-the-art accuracy, we study how different PII detection paradigms fail under no...
  </details>

- **2026-09-03** — Leqi Zheng, Jinbo Su, Yuying Li et al. — [SciLENS: RL-Driven Autonomous Agents for Scientific Localized Evidence Navigation and Synthesis](http://arxiv.org/abs/2609.03338v1)
  <details><summary>📄 Abstract</summary>
  Scientific literature synthesis agents increasingly rely on proprietary online services, limiting reproducibility, privacy, and offline deployment. To address this challenge, we introduce SciLENS Scientific Localized Evidence Navigation and Synthesis), a fully local autonomous agent framework operating on a dual-tier infrastructure indexing approximately 12 million academic records. SciLENS pioneers the integration of structural visualization as an actionable tool within the reasoning loop, enab...
  </details>

- **2026-09-03** — Chengsong You, Wangyue Li, Weiqiao Que et al. — [KnowFeat: Knowledge-Guided Feature Engineering via LLM Agents](http://arxiv.org/abs/2609.03529v1)
  <details><summary>📄 Abstract</summary>
  Automated feature engineering with large language models (LLMs) can produce semantically meaningful features for tabular data, yet existing methods lack structured domain knowledge, rigorous verification, and explainable provenance. We propose KnowFeat, a knowledge-guided feature engineering framework that organizes domain knowledge into five types -- schema metadata, regulatory indicators, detection rules, expert opinions, and court document evidence -- and injects them as structured context in...
  </details>

- **2026-09-03** — Yiming Gai, Yingying Zhang, Xuefei Huang — [ExplainRoute: A Pre-Deployment Audit Framework for Non-Answer-Giving Programming Tutors](http://arxiv.org/abs/2609.03470v1)
  <details><summary>📄 Abstract</summary>
  Programming tutors should support learners' own explanations rather than immediately providing model answers. We present ExplainRoute, a pre-deployment audit framework for non-answer-giving programming tutors. Given a code line and a learner explanation, it estimates the explanation state and selects one of two bounded responses: a Feynman-style self-explanation prompt or a Socratic scaffold. The framework exposes its state, strategy, cited code fragment, and leakage risk through a machine-check...
  </details>

- **2026-09-02** — Renyuan Liu, Yuyang Leng, Kaiyan Liu et al. — [LeanStream: A Speculate-and-Refine Streaming Framework for Efficient on-Device LLM Inference](http://arxiv.org/abs/2609.03079v1)
  <details><summary>📄 Abstract</summary>
  On-device LLM inference is attractive for privacy and responsiveness, but remains challenging on mobile and embedded devices because model weights far exceed available DRAM. Prior systems exploit activation sparsity and offload weights to SSD or flash storage, but face a fundamental systems trade-off: accurate sparse execution decisions require the latest context, whereas efficient computation-I/O overlap requires early prediction. As a result, existing designs either serialize execution or incu...
  </details>

- **2026-09-02** — Jinxi Yu, Eric Hanchen Jiang, Levina Li et al. — [Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning](http://arxiv.org/abs/2609.02967v1)
  <details><summary>📄 Abstract</summary>
  Topology-guided safeguards for LLM-based multi-agent systems (MAS) train a GNN over the inter-agent communication graph to localize risky agents and intervene on the topology---but they assume one operator can pool all labeled traces. Across organizations that assumption breaks: episodes contain private prompts, tool outputs, and proprietary workflows, and no silo alone sees the full attack distribution. We cast privacy-preserving MAS safeguarding as graph federated learning and instantiate FGLG...
  </details>

- **2026-09-02** — Jiechao Gao, Yuandong Pan, Jie Wang et al. — [PrivateHub: Contrastive Diffusion Model for Private Sensor-Intensive Environment Data Generation](http://arxiv.org/abs/2609.02958v1)
  <details><summary>📄 Abstract</summary>
  Sensor-intensive environments enable many intelligent services by inferring user applications from heterogeneous data streams. However, not all applications should be exposed: users want some activities to stay private. This creates a tension between inferring applications for useful services and preventing unwanted inference. Existing approaches such as differential privacy and rule-based filtering protect individual streams but cannot address the privacy risk from cross-sensor inference.   We ...
  </details>

- **2026-09-02** — Rémi Bourgerie, Šarūnas Girdzijauskas, Viktoria Fodor — [From Euclidean to Graph-Structured Data: A Survey of Collaborative Learning](http://arxiv.org/abs/2609.02984v1)
  <details><summary>📄 Abstract</summary>
  The conventional approach to machine learning, that is, collecting data, training models, and performing inference in a single location, faces fundamental limitations, including scalability and privacy, that restrict its applicability. To address these challenges, recent research has explored collaborative learning approaches, including federated learning and decentralized learning, where individual agents perform training and inference locally, with limited collaboration. Most collaborative lea...
  </details>

- **2026-09-02** — Smitha Muthya Sudheendra, Jaideep Srivastava — [PragAlign: Feedback-Guided Pragmatic Alignment for Controlled Synthetic Dialogue Generation](http://arxiv.org/abs/2609.02480v1)
  <details><summary>📄 Abstract</summary>
  Synthetic dialogue generation can support research in privacy-restricted service settings, but generated conversations must preserve communicative intent, affective meaning, and natural dialogue flow. We introduce PragAlign, a feedback-guided framework for controlled synthetic dialogue generation conditioned on service context, target intent, and target emotion, with auxiliary trait-style controls. PragAlign uses a generate--evaluate--revise loop in which an LLM-based evaluator scores intent ali...
  </details>

- **2026-09-02** — Vishnu Prasad Vijaya Kumar, Santhosh Venkatesh, Ivan P. Yamshchikov — [LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images](http://arxiv.org/abs/2609.02207v1)
  <details><summary>📄 Abstract</summary>
  Real-world personally identifiable information (PII) redaction often operates on document images---scans, screenshots, and PDF renderings---where OCR errors, layout structure, and visual noise determine whether sensitive information is actually removed. Existing PII benchmarks are mostly text-centric and do not measure document-level redaction risk: a page remains unsafe if even one identifier is missed. We introduce LeakageBench, a challenge set of 500 document images with 11,954 GDPR-aligned P...
  </details>

- **2026-09-02** — Sanjaya Poudel, Nirajan Kunwor, Manish Dhakal et al. — [Federated LoRA Adaptation of BiomedCLIP Across Four International Chest X-Ray Cohorts](http://arxiv.org/abs/2609.02101v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) lets institutions train a shared model without exchanging data, and Low-Rank Adaptation (LoRA) makes this practical at scale by communicating only compact low-rank updates. Biomedical imaging is a compelling setting for this combination: patient data are archived behind privacy regulations, and institutions differ widely in scanners, protocols, and compute. Such heterogeneity raises the question of how federated LoRA updates should be aggregated, increasingly pressing as ...
  </details>

- **2026-09-02** — Zhaoyang Jiang, Zhizhong Fu, Yunsoo Kim et al. — [Learning to Fuse LLMs with Ontology Rankers for Rare-Disease Diagnosis](http://arxiv.org/abs/2609.02473v1)
  <details><summary>📄 Abstract</summary>
  Ontology rankers remain useful for rare-disease diagnosis because each candidate can be traced to matched patient phenotypes. Large language models (LLMs) can generate differential diagnoses from the same patient description, but their predictions lack an equally clear evidence trail. Rather than asking which system should replace the other, we ask whether an LLM can improve the ranker without giving up its evidence. Our behavior-based fusion model examines the two ranked lists, their agreement,...
  </details>

- **2026-09-02** — Bizhe Bai, Jiakang Yuan, Hongming Wu et al. — [Efficient GUI Agents: A Systems Survey of Observation, Memory, Action, and Runtime Optimization](http://arxiv.org/abs/2609.02309v1)
  <details><summary>📄 Abstract</summary>
  GUI agents increasingly operate across websites, mobile apps, and desktop environments, yet the field still reports progress primarily through task success. We argue that practical deployment depends equally on efficiency: how much context, computation, action budget, and runtime overhead an agent consumes while succeeding. This survey studies efficient GUI agents through an end-to-end systems lens that preserves the current technical axes of observation efficiency, context and memory efficiency...
  </details>

- **2026-09-02** — Thomas Brackin — [Privacy Washing: Detecting Internal Contradictions in Privacy Policies](http://arxiv.org/abs/2609.02055v1)
  <details><summary>📄 Abstract</summary>
  Privacy policies may contain internal contradictions in which commitments are undermined by practices documented elsewhere in the same policy. We operationalize this phenomenon, privacy washing, through a four-stage pipeline: statement extraction, compatibility filtering and natural language inference screening, multi-model judge verification, and thematic analysis, with contradictions confirmed by majority vote of a three-model LLM panel. Applied to two corpora of website privacy policies, 123 ...
  </details>

- **2026-09-02** — Taixi Chen, Nancy Guo — [Test-Time Logit Prompting for Source-Free Missing Modality Adaptation](http://arxiv.org/abs/2609.02039v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have achieved remarkable performance by leveraging complementary information from large-scale image-text pairs. However, missing-modality inputs are commonly encountered during real-world deployment, often leading to significant performance degradation. Existing methods primarily enhance model robustness by learning modality compensation strategies from source training data. However, their reliance on source training data makes them difficult to apply when original ...
  </details>

- **2026-09-01** — Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang et al. — [Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis](http://arxiv.org/abs/2609.02947v1)
  <details><summary>📄 Abstract</summary>
  Significant challenges remain in AI-driven educational systems in balancing privacy preservation with accurate cognitive diagnosis. To overcome this, we propose a federated inference framework in which several commercial LLM APIs collaborate without requiring access to raw student data or proprietary model internals. Using multiple federated entities, such as LLaMA-3.3-70B, GPT-4o-mini, and Claude-3-Haiku, our framework builds upon a heterogeneous multi-LLM architecture. The predictions generate...
  </details>

- **2026-09-01** — Kunlin Cai, Kaiyuan Zhang, Zihang Xiang et al. — [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](http://arxiv.org/abs/2609.01723v1)
  <details><summary>📄 Abstract</summary>
  Text-to-Speech (TTS) foundation models are increasingly fine-tuned on private datasets to synthesize highly personalized voices, introducing severe privacy risks by exposing both biometric identities and sensitive speech content. Existing black-box membership inference attacks (MIAs) follow a two-stage pipeline of query generation and representation engineering, both of which face unique challenges when adapted to TTS. For query generation, dual conditioning on synthesis text and reference speec...
  </details>

- **2026-09-01** — Gene Zhang — [Zeta-Lite: A Concurrent, Branchable In-Browser SQL Database for Agentic Memory](http://arxiv.org/abs/2609.01818v1)
  <details><summary>📄 Abstract</summary>
  The browser has become a first-class database host: applications increasingly want to store, query, and reason over structured data entirely on the client - for privacy, offline operation, local-first collaboration, and, most recently, as durable memory for in-browser AI agents. One way to get SQL in the browser, compiling PostgreSQL to WebAssembly (PGlite), inherits PostgreSQL's process model: a single backend connection that executes one statement at a time and blocks. That model cannot expres...
  </details>

- **2026-09-01** — Ehsan Faghih, Fatemeh Ashrafi, Marguerite Moore et al. — [Ten Architectures, One Error: Shared Failure Modes in Hyperspectral Classification under Spatially Disjoint Evaluation](http://arxiv.org/abs/2609.01786v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral image classification still relies heavily on random pixel splits within a single scene. The Salinas dataset, randomly split, is among the most widely used datasets for comparing different architectures. However, under a random split method, a large fraction of test pixels fall immediately adjacent to a training pixel, which inflates reported accuracy. This work introduces a leakage-free evaluation protocol linking spatial separation to the model's receptive field. Applying this pro...
  </details>

- **2026-09-01** — Yu Nong, Yao Du, Tianxiang Xu et al. — [The Data Problem in Software Vulnerability Analysis: Artifacts, Quality, and Consumption](http://arxiv.org/abs/2609.01503v1)
  <details><summary>📄 Abstract</summary>
  Learning- and LLM-based software vulnerability analysis is only as trustworthy as the data it is trained and evaluated on, yet that data is rarely examined as a first-class object. We investigate the data behind vulnerability analysis through a dataset-centric taxonomy that separates what an artifact is (code, metadata, patches, tests/PoCs, reasoning, traces), how good it is (realism, label evidence, scale, diversity, leakage, availability), and what it is used for. From a systematically assembl...
  </details>

- **2026-09-01** — Nicolas Constantinides, Mahdi Rahimi, Stavros Nonis — [Hidden Services Protocol for Mixnets](http://arxiv.org/abs/2609.01326v1)
  <details><summary>📄 Abstract</summary>
  Mix networks (mixnets) provide network-level privacy by routing each communication packet through a sequence of intermediaries, called mixnodes, that randomly delay and cryptographically transform packets before forwarding them, making it difficult for observers to link mixnet entries to exits. While this mechanism protects sender privacy from both external adversaries and the receiver, existing mixnets lack a secure and practical protocol that simultaneously protects receiver (destination) priv...
  </details>

- **2026-09-01** — Stefano Leggio, Giulio Rossolini, Alessandro Biondi — [Position Matters: Feature Inversion Attacks in ViT Split Inference with Token Reduction and Shuffling](http://arxiv.org/abs/2609.01232v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are increasingly used in split-inference systems, where edge devices transmit intermediate token representations to a remote cloud. In this setting, token reduction lowers computation and communication costs, while token shuffling disrupts the spatial organization of the transmitted tokens, potentially limiting information leakage. However, their privacy benefits remain unclear against feature inversion attacks, which attempt to reconstruct the input from the transmitt...
  </details>

- **2026-09-01** — Shengfang Zhai, Leo Marchyok, Yuling Shi et al. — [Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry](http://arxiv.org/abs/2609.00873v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) have recently emerged as an alternative modeling paradigm to autoregressive LMs, offering advantages such as parallel generation and bidirectional context modeling. Despite growing interest in their generative capabilities, the privacy risks of DLMs remain underexplored. We identify a phenomenon termed token-level memorization asymmetry through theoretical analysis of diffusion training dynamics. Building on this finding, we propose Q-Skew, a quantile-weighted sk...
  </details>

- **2026-09-01** — Danze Chen, Zeqing Wang, Ziyue Lin et al. — [H3-World: Turning Language Understanding into World Control](http://arxiv.org/abs/2609.01560v1)
  <details><summary>📄 Abstract</summary>
  We present H3-World, an efficient framework that turns the 33B MiniMax-H3 video generator into an interactive world model. Our key finding is that, as large video generators become more capable, language is emerging as a natural interface for control. MiniMax-H3, for example, already supports zero-shot control of character behavior and camera motion through natural-language instructions. Building on this, H3-World turns this coarse language interface into precise, temporally grounded world contr...
  </details>

- **2026-09-01** — Maryam Alshehyari, Dushyant Singh Chauhan, Samuele Poppi et al. — [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](http://arxiv.org/abs/2609.01161v1)
  <details><summary>📄 Abstract</summary>
  Large language models can reproduce memorized text verbatim, yet copyright defenses are usually evaluated under incompatible protocols. We introduce CopyShield, a controlled benchmark comparing three representative defenses at distinct intervention levels: contrastive decoding (output), Direct Preference Optimization (behavioral), and activation intervention (representation). We evaluate CopyShield on two model families, LLaMA-3.1-8B and Mistral-7B-v0.3, using controlled memorization over five p...
  </details>

- **2026-09-01** — Che Hyun Lee, Sangkwon Park, Donghun Kang et al. — [Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech](http://arxiv.org/abs/2609.01016v1)
  <details><summary>📄 Abstract</summary>
  Current speech synthesis struggles with code-switching, which mixes a foreign language phrase into a primary language utterance, causing the phrase to be spoken with the primary language's accent rather than its native one. We propose Phrase-Localized Language-Contrastive Guidance (LCG), a training-free inference framework that restores a native accent to code-switched phrases in cross-lingual text-to-speech. LCG replaces the single language guidance applied across the whole utterance with a sep...
  </details>

- **2026-09-01** — Wen Jiang, Mingmin Chu, Yimeng Tian et al. — [HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution](http://arxiv.org/abs/2609.00829v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents advance toward autonomy by optimizing their harness---prompts, skills, tools, and execution logic---based on environmental feedback. This paradigm, however, is hampered by three challenges: \textit{credit assignment failure}, where terminal success/failure feedback makes it ambiguous which step caused the error; \textit{shortcut learning}, where agents memorize task-specific patterns rather than acquire generalizable capabilities; and \textit{catastrophic forgetting}, where ...
  </details>

- **2026-09-01** — Bhuvan Koduru, Dareen Safar B Alharthi, Rita Singh et al. — [Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](http://arxiv.org/abs/2609.00727v1)
  <details><summary>📄 Abstract</summary>
  Audio language models are designed to understand speech, yet it remains unclear whether they capture how something is said beyond what is said. We present a mechanistic analysis of paralinguistic information in four open source models, Whisper-large-v2, Qwen2-Audio-7B Instruct, Qwen2.5-Omni-7B, and Chroma-4B, using the Expresso dataset with controlled speaking styles. We combine centered kernel alignment, linear probing with leave one speaker out evaluation, open ended tone prediction, and a con...
  </details>

- **2026-09-01** — Miso Kim, Georu Lee, Seungwon Jeong et al. — [Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning](http://arxiv.org/abs/2609.00605v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning for large language models (LLMs) often assumes that a pre-defined forget set matches what the model has memorized, but this frequently breaks in realistic privacy settings where the original training data is inaccessible. We term this gap forget-set misalignment and identify two cases. In Under Unlearning, the forget set omits memorized information and leakage persists. In Out-of-Knowledge Unlearning, the algorithm is driven to "forget" knowledge the model never learned, pertu...
  </details>

- **2026-09-01** — Byunggu Yu, Justin Kim — [Wave Function Backpropagation with Explicit Temporal-Interval Dynamics](http://arxiv.org/abs/2609.00503v1)
  <details><summary>📄 Abstract</summary>
  Conventional neural networks learn predominantly through affine transformations followed by nonlinear activations, while elapsed time is often treated as an auxiliary feature or assumed to be uniformly sampled. This paper introduces Wave Function Backpropagation (WFB), a wave-parameterized learning formulation in which neural responses are represented by learnable amplitude, wavenumber, angular frequency, and phase. The formulation associates an observed state with its temporal interval Delta t ...
  </details>

- **2026-09-01** — Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin et al. — [Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics](http://arxiv.org/abs/2609.01575v1)
  <details><summary>📄 Abstract</summary>
  Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VLM (35B total, 3B active), fine-tuned on in-house production data mixed with open-domain documents cu...
  </details>

- **2026-09-01** — Stefania Bellavia, Greta Malaspina, Benedetta Morini — [DOFFO_TR: a Decentralized Objective Function-Free Optimization method with Trust-Region](http://arxiv.org/abs/2609.00878v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a novel objective function-free trust-region method designed to solve optimization problems over decentralized networks. Unlike traditional approaches that often rely on stepsize tuning, our framework employs a function-free trust-region procedure that enables adaptive selection of the step length. Our approach accommodates first- and second-order models and eliminates the need to share local function values and gradients among agents, thereby enhancing privacy and comp...
  </details>

- **2026-09-01** — Zinco J, Xunjie Zhu, Shen Huang et al. — [MemoryWalker: Stop Training Agents on Contexts They Never Saw](http://arxiv.org/abs/2609.00865v1)
  <details><summary>📄 Abstract</summary>
  Production agent harnesses such as Claude Code and Qwen-Agent compress context during rollout, but training under compression creates a conditioning problem: every eviction branches the effective history, so the learning object is a tree rather than a sequence. Existing linearizations either retain the rightmost path, causing time-travel leakage, or replay a depth-first traversal, causing train-inference mismatch. We introduce two exact, gradient-equivalent corrections: LogitTree, a segmented K-...
  </details>

- **2026-09-01** — Lei Wang, Jieming Bian, Letian Zhang et al. — [Breaking the Structural Identity: Personalized Federated LoRA Fine-tuning under Rank Heterogeneity](http://arxiv.org/abs/2609.00632v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable success across diverse domains, but their adaptation to privacy-sensitive, distributed datasets remains a challenge. While Federated Learning (FL) combined with Low-Rank Adaptation (LoRA) provides a resource-efficient paradigm for collaborative fine-tuning, practical deployments are hindered by the dual challenges of resource heterogeneity and data heterogeneity. Existing rank-heterogeneous methods primarily focus on bridging dimension mismat...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-09-02** — Aritra Das, Jaee Ponde, Mihir More et al. — [You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring](http://arxiv.org/abs/2609.03035v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly deployed in multi-agent systems, where they can collude while keeping their actions benign. Output monitors designed to detect such collusions can be fooled by obfuscation and steganography, motivating the use of probes trained on internal activations. However, these probes are usually evaluated on agents that do not know they are being watched. We study how activation-based detection changes when agents are explicitly informed that their internal activations are bein...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 18 papers

- **2026-09-03** — Davide Paglieri, Logan Cross, Tim Genewein et al. — [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](http://arxiv.org/abs/2609.04170v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent AI science ecosystems rely on agents possessing tools that allow them to communicate, coordinate, and build on each other's work. Yet this shared infrastructure can also introduce vulnerabilities by creating a substrate for the contagious spread of unintended and undesirable behaviors. We report a case study on a research collective of 100 autonomous LLM agents tasked with proving formal mathematical conjectures. Within the swarm, cheating spontaneously emerged and was later challeng...
  </details>

- **2026-09-03** — Hoang Cuong Nguyen, Mark Dras, Usman Naseem — [Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness](http://arxiv.org/abs/2609.03887v1)
  <details><summary>📄 Abstract</summary>
  How do the methods used to train language models to refuse harmful requests shape how that refusal actually works inside the model? We compare three post-training methods - supervised fine-tuning, reasoning-augmented fine-tuning (training on reasoning chains that justify a safety decision), and preference optimization (ORPO) - across three architecturally distinct models (Llama-3.1-8B, Gemma-2-9B, Qwen3-8B). We find that training method, not just data, reshapes how refusal is computed internally...
  </details>

- **2026-09-03** — Danting Zhang, Bei Peng, Robert Loftin — [Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation](http://arxiv.org/abs/2609.03814v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) demonstrate strong performance on standard content moderation benchmarks. However, these benchmarks often aggregate multiple moderation criteria into a single label, making it unclear whether models can disentangle them and reliably apply each criterion when making decisions. To study whether LLMs exhibit criterion-conditioned behaviour, we introduce Diagnostic Evaluation of COntent (DECO), a criterion-independent factorisation of content that enables controlled, cri...
  </details>

- **2026-09-03** — Axel Allain, Aymeric Blot, Djamel Eddine Khelladi et al. — [Code Transformation Rule Synthesis using LLMs: Potential and Limits](http://arxiv.org/abs/2609.03592v1)
  <details><summary>📄 Abstract</summary>
  Due to their black-box nature, LLMs suffer from limited explain- ability and a lack of determinism. Their usage cost can also rise, particularly with repetitive tasks on large codebases. To mitigate this, we conduct a novel empirical study targeting three domain- specific languages for transformation rules, namely Comby, GritQL, and Ast-Grep. We evaluate three LLMs (GPT-5.4, GPT-oss-120B, and Llama3.1-8B) on six diverse datasets covering four software- evolution tasks: API misuse correction, pro...
  </details>

- **2026-09-02** — David Chernin, Ethan Fetaya — [CRAW: Codec Robust Audio Watermarking](http://arxiv.org/abs/2609.03107v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative speech models have made it increasingly difficult to distinguish authentic from synthetic audio, enabling new forms of fraud and misinformation. Audio watermarking offers a promising defense by embedding an imperceptible signal into generated speech that can later be detected to verify its provenance. However, recent studies have shown that existing post-hoc watermarking methods fail under neural codecs and denoisers, transformations routinely applied during real-wo...
  </details>

- **2026-09-02** — Tianqi Xiao, Shiyao Cui, Minghao Zhang et al. — [Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models](http://arxiv.org/abs/2609.02082v2)
  <details><summary>📄 Abstract</summary>
  Visual modality enhances the capabilities of multimodal large language models (MLLMs) but also introduces a safety concern: a benign textual query may convey harmful intent when grounded in a visual image. We term this cross-modal safety drift and our pilot studies show that the safety response rate for such requests is substantially lower than that for requests containing explicitly unsafe text. This paper aims to systematically study this issue. First, we conduct an empirical analysis to ident...
  </details>

- **2026-09-02** — Lulu Xie, Yancheng Wang, Kanchan Chowdhury et al. — [IDSPACE: A Novel Document Generator for Reliable Evaluation of Digital Identity Verification Systems [Extended Technical Report]](http://arxiv.org/abs/2609.03052v1)
  <details><summary>📄 Abstract</summary>
  As services move online, trust institutions such as banks, lenders, and governments must verify the identity of remote users. Fraud detection tools are widely available, but evaluating and fine-tuning them remains difficult because identity documents are sensitive and therefore scarce. Synthetic data generation offers a path forward, and demand is clear: our prior work in this area has been downloaded over $11{,}000$ times (aggregated from eight parts). We introduce IDSpace, extending this line ...
  </details>

- **2026-09-02** — Da Cheng Gu, Yifei Dong, Xinghao Yang et al. — [ASCII Attack: Recontextualising Harmful Requests as Artistic Critique in Large Language Models](http://arxiv.org/abs/2609.02215v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment trains large language models to refuse harmful requests stated plainly, but that training is applied mostly to surface form. Requests that only recontextualise the same operational content, changing how the model reads it, are therefore only weakly covered. The ASCII Attack is one such recontextualisation. It is single-turn and black-box: one message, with no access to model internals. It embeds a fully legible harmful request in ASCIl-art characters, presents it as artwork, and...
  </details>

- **2026-09-02** — Qinghua Mao, Wanying Qu, Dadi Guo et al. — [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](http://arxiv.org/abs/2609.02786v1)
  <details><summary>📄 Abstract</summary>
  The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses and multi-step execution trajectories. Existing safety alignment mechanisms often rely on either external harness updates or policy optimization, yet applying either paradigm in isolation fails to bridge runtime control with intrinsic safety. We propose SafeEvolve, an experience-driven self-evolving f...
  </details>

- **2026-09-02** — Zhengyi Jin, Ru Zhang, Xiao Chen et al. — [FUSE: An Evaluating Framework for Dangerous Capabilities of LLMs](http://arxiv.org/abs/2609.02168v1)
  <details><summary>📄 Abstract</summary>
  Fragmented safety evaluation undermines the governance of dangerous AI capabilities. We present a modular framework that evaluates each model through three orthogonal pipelines---Knowledge ($K$), Defense ($D$), and Harm ($H$)---under a unified protocol, aggregating results into a standardized dangerous-capability profile $φ$. Pluggable modules supply scenario seeds, knowledge banks, hazard queries, and judge rubrics, while the core evaluation engine remains unchanged across domains; the CB evalu...
  </details>

- **2026-09-02** — Tianqi Xiao, Shiyao Cui, Minghao Zhang et al. — [Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models](http://arxiv.org/abs/2609.02082v1)
  <details><summary>📄 Abstract</summary>
  Visual modality enhances the capabilities of multimodal large language models (MLLMs) but also introduces a safety concern: a benign textual query may convey harmful intent when grounded in a visual image. We term this cross-modal safety drift and our pilot studies show that the safety response rate for such requests is substantially lower than that for requests containing explicitly unsafe text. This paper aims to systematically study this issue. First, we conduct an empirical analysis to ident...
  </details>

- **2026-09-02** — Chenyu Zhou, Qiliang Jiang, Shuning Wu et al. — [Coverage, Not Targeting: A Structural Regime in Multi-Turn Agent Credit Assignment](http://arxiv.org/abs/2609.02417v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn agentic RL increasingly treats credit assignment as a targeting problem: given a terminal verifiable reward, per-turn methods localize credit onto the turns that mattered. We identify the structural quantity that predicts when this is the right move, the verifier information density V_d = k/C (the fraction of an agent's C-step causal chain whose per-turn correctness the verifier exposes), and show that terminal-state verifiers sit deep in a low-V_d regime where targeting is the wrong ...
  </details>

- **2026-09-01** — Sejuti Basu, Ashima Sood, Vijay Kumar et al. — [Swin Meets EfficientNet: Lightweight Architectures for GAN-Based Face Forensics](http://arxiv.org/abs/2609.01749v1)
  <details><summary>📄 Abstract</summary>
  Modern generative models, such as GANs, diffusion architectures, and autoregressive systems, now produce facial images that are nearly indistinguishable from authentic photographs. This capability makes detecting forged images increasingly difficult, raising serious concerns about identity theft, fraud, and misinformation campaigns. Our research focuses specifically on GAN-generated synthetic faces, which underpin many face-centric deepfakes, and investigates efficient detection approaches using...
  </details>

- **2026-09-01** — Rui Yang, Shuang Huang, Junhua Liu et al. — [Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges](http://arxiv.org/abs/2609.01210v1)
  <details><summary>📄 Abstract</summary>
  Safety benchmarks for large language models often assess the risk of a user query, although the outcome of question answering depends on whether the response violates a policy. This distinction is critical in Chinese harmful-content evaluation, where linguistic variation and adversarial transformations can obscure risky intent. We introduce C-SafeQA, a policy-grounded benchmark for response-level Chinese safety evaluation. It comprises 538 base queries and 8,877 adversarial queries answered by f...
  </details>

- **2026-09-01** — Jainil Dharmil Shah — [Triple-Bottom-Line Sustainability of Language Models for Edge AI: A Comparison Between SLMs and Quantized LLMs](http://arxiv.org/abs/2609.00665v1)
  <details><summary>📄 Abstract</summary>
  Edge-AI model selection is commonly driven by one isolated metric - accuracy, latency, memory, energy, or safety, even though a deployable language model must balance all five. Our work focuses on answering the question whether na- tively trained small language models (SLMs) or large language models (LLMs) compressed through post-training quantization offer the more sustainable edge- deployment trade-off. We introduce a reproducible Holistic Sustainability Score (HSS) organized around the triple...
  </details>

- **2026-09-01** — Rui Yang, Yang Hong, Yichao Xu et al. — [Same Request, Different Boundary: Evaluating Cybersecurity Assistance across Conversational Contexts](http://arxiv.org/abs/2609.00578v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can solve complex problems, but their misuse in high-risk domains can lead to severe consequences. Model providers therefore restrict assistance for potentially harmful requests. Refusing all cybersecurity requests would therefore harm legitimate users. Providers need a mechanism to block malicious use without denying legitimate assistance to defenders. Existing cybersecurity-specific datasets evaluate this mechanism, but none considers the conversational context of ...
  </details>

- **2026-09-01** — Pingyu Wu, Weiming Zhang, Nenghai Yu — [The Safeguard Worked. Is the LLM System Safer?](http://arxiv.org/abs/2609.00519v1)
  <details><summary>📄 Abstract</summary>
  Safeguards in deployed LLM services are evaluated by refusal, attack success, and policy violation rates. Those rates characterize how a control performed on the requests it was tested on. A deployment has to answer a different question: how much help with harmful tasks the service still gives an attacker who keeps adapting or finds another way in. We determine what each reported result implies for that question, allowing results from different safeguard families to be compared under one deploym...
  </details>

- **2026-09-01** — Wenhan Chang, Tianqing Zhu, Ping Xiong et al. — [RISA: Response Inspection and Selective Actions for Refusal Calibration in Large Language Models](http://arxiv.org/abs/2609.00790v1)
  <details><summary>📄 Abstract</summary>
  Reliable refusal behavior requires Large Language Models (LLMs) to reject harmful prompts with only answering benign ones. Incorrect refusal behavior can either expose users to harmful responses or prevent users from obtaining useful answers. Training-time alignment improves refusal behavior by updating model parameters with safety data, but requires additional computation and training. In contrast, inference-time alignment aims to modify LLM behavior during inference without updating the underl...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-03** — Uday Vallabhaneni, Cassie L. Cagwin, David J. Wild — [SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center](http://arxiv.org/abs/2609.04159v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly proposed as autonomous SOC analysts, but two limitations make them unreliable at enterprise scale: a finite context window cannot hold a multi-thousand-host authentication graph, and free-form generation offers no guarantee that a recommended containment action is consistent with the topology it operates on. We present Sentinel-RL, an agentic-SOC architecture that decouples topological reasoning from semantic reasoning: a heterogeneous graph att...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 52 papers

- **2026-09-03** — Chihao Shen, Jiacheng Li, Aastha Mahajan et al. — [PatchBench: Evaluating AI Agents for Vulnerability Patching](http://arxiv.org/abs/2609.04075v1)
  <details><summary>📄 Abstract</summary>
  AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash. This leaves two key threats to validity: agents may reproduce memorized historical developer patches, or they may generate surface-level fixes that only suppress the reported crash.   We study these concerns for C/C++ vulnerability patching. We introduce a patch s...
  </details>

- **2026-09-03** — Rajmohan Rajaraman, Ravi Sundaram, Amanuel Tesfaye — [The Head Complexity of Boolean Functions in Single-Layer Attention](http://arxiv.org/abs/2609.04046v1)
  <details><summary>📄 Abstract</summary>
  What can a single layer of self-attention compute? We study head complexity: the minimum number of attention heads required to compute a function in a one-layer attention-only model. We establish an exact hierarchy under this measure: $k$ heads compute $k$-bit parity but cannot compute $(k+1)$-bit parity.   The lower bound is unconditional in the two resources a transformer might otherwise exploit; it holds at unbounded embedding dimension and unbounded numerical precision. The proof rests on an...
  </details>

- **2026-09-03** — Vineet Kumar, Meghanadh Pulivarthi, vishwajeet kumar et al. — [STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation](http://arxiv.org/abs/2609.03874v1)
  <details><summary>📄 Abstract</summary>
  Retrieval Augmented Generation (RAG) is a key component for generating accurate and hallucination free answers using Large Language Models (LLMs). LLMs are improving at handling long context, but still suffer from "lost in the middle" problem. Thus, precise and accurate retrieval is important. Current retrievers chunk long context into length-based manageable chunks - in the process throwing away rich and informative semantic global structure in the corpus. We introduce a novel retrieval system ...
  </details>

- **2026-09-03** — Oline Ranum, Edward Fish, Simon Hadfield et al. — [Beyond BLEU: A Case for Redefining Sign Language Translation Benchmarks](http://arxiv.org/abs/2609.03734v1)
  <details><summary>📄 Abstract</summary>
  BLEU-4 is the standard metric for evaluating sign language translation (SLT), but spoken-language metrics may not adequately reflect sign language proficiency. The multimodal, low-resource context of SLT allows models to exploit spurious correlations and spoken-language priors, rather than learning stronger sign representations. In this paper, we evaluate the relationship between spatio-temporal understanding and BLEU-4 across six SLT models on Phoenix-2014T and CSL-Daily, showing that gains in ...
  </details>

- **2026-09-03** — Au Ashley Hoi-Ting, Meghdad Kurmanji, William F. Shen et al. — [Extracting Forgotten Prompts from Targeted Unlearned Models](http://arxiv.org/abs/2609.03662v1)
  <details><summary>📄 Abstract</summary>
  Recent unlearning methods (e.g. NPO, DPO, LUNAR) make use of refusal alignment to suppress forgotten data. However, it has been shown that refusal responses might leave traces of unlearning, and recent attacks have been able to successfully recover some of the unlearned knowledge. In this paper, we uncover a new vulnerability. Existing attacks typically assume that the forgotten prompts are already known to the adversary and focus on recovering their answers. However, we show that the forgotten ...
  </details>

- **2026-09-03** — Xuanfa Jin, Zhijian Ma, Yongcheng Zeng et al. — [Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation](http://arxiv.org/abs/2609.03619v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent debate (MAD) improves the reasoning capabilities of large language models by having multiple agents iteratively refine their responses through discussion. However, MAD suffers from a critical vulnerability known as shared misconception: when a majority of agents initially converge on an incorrect answer, the debate process tends to amplify rather than correct the error. Existing methods primarily address peer skew but leave the agents' inherently biased concept priors unaddressed. To...
  </details>

- **2026-09-03** — Hamidreza Mazandarani, Masoud Shokrnezhad, Tarik Taleb — [A Semantic-Aware Multiple Access Scheme Leveraging Spatial Redundancy for Uplink-Dominant Network Services](http://arxiv.org/abs/2609.03559v1)
  <details><summary>📄 Abstract</summary>
  The transition toward semantic-aware communication offers a paradigm shift for next-generation mobile networks, promising to decouple information significance from raw data transmission. Despite advances in semantic extraction, the integration of semantic intelligence into the Medium Access Control (MAC) layer remains underexplored, particularly in exploiting spatial correlations among users. To address this, we introduce a novel multiple access scheme designed for uplink-dominant network servic...
  </details>

- **2026-09-03** — Fang He, Tao-yang Fu, Wang-chien Lee — [TraveL: Transformer-based Multi-view Path Distributional Representation Learning](http://arxiv.org/abs/2609.03427v1)
  <details><summary>📄 Abstract</summary>
  Path representation learning (PRL) for road networks has received increasing research attention, due to various path-related applications. Existing works on PRL typically exploit the co-occurrence relationship among road segments and paths to learn a vector as the path representation, without exploring the varied traveler behaviors and the regional correlation on the path. In this work, we propose to learn distributional representations, which provide valuable information for use in path-related...
  </details>

- **2026-09-03** — Xiangyang Miao, Kelu Yao, Yekai Huang et al. — [Exploring the Potential of Contrastive Language-Image Pre-training for Multi-Source Remote Sensing Data](http://arxiv.org/abs/2609.03391v1)
  <details><summary>📄 Abstract</summary>
  Contrastive language-image learning (CLIP) has become a key paradigm for remote sensing vision-language understanding. However, existing remote sensing contrastive learning methods are mostly built on RGB-oriented CLIP architectures, making it difficult to exploit heterogeneous sensors such as SAR, multi-spectral imaging (MSI), and hyperspectral imaging (HSI). To address this limitation, we propose OmniRSCLIP, an end-to-end contrastive learning framework that supports multi-source sensor inputs ...
  </details>

- **2026-09-03** — Fei Liu, Yang Ai, Zhen-Hua Ling — [Neural Music Enhancement with Dual Time-Frequency Spectral Representations for Prediction and Discrimination](http://arxiv.org/abs/2609.03357v1)
  <details><summary>📄 Abstract</summary>
  Non-professional music recordings shared online often suffer from background noise and reverberation, degrading perceived quality and limiting reuse. This paper proposes DSME, a music enhancement model based on dual time-frequency spectral representations. Within a generative adversarial framework, DSME uses short-time Fourier transform (STFT) spectra for generation and constant-Q transform (CQT) spectra for discrimination. Leveraging STFT's fixed window, invertibility, and predictability, the g...
  </details>

- **2026-09-03** — Yuxuan Song, Fan Gao, Yibo Zhao et al. — [AnyGS2Mesh: Feed-Forward Mesh Reconstruction from 3D Gaussian Splatting with Arbitrary-Resolution Views](http://arxiv.org/abs/2609.03304v1)
  <details><summary>📄 Abstract</summary>
  Existing 3D mesh reconstruction methods from Gaussian scene representations predominantly rely on iterative optimization, resulting in slow inference and limited scalability to high-resolution inputs. In this paper, we present AnyGS2Mesh, the first feed-forward framework for directly reconstructing 3D meshes from 3D Gaussian Splatting representations with support for arbitrary input image resolutions. Our approach incorporates a Gaussian-Guided Transformer architecture that exploits explicit 3D ...
  </details>

- **2026-09-02** — Sawyer Allen, Cash Cherry, Aidan Eck et al. — [Gradient-Free Optimization for Matrix functions](http://arxiv.org/abs/2609.03170v1)
  <details><summary>📄 Abstract</summary>
  We consider the task of optimizing smooth, possibly non-convex functions of a matrix variable given access only to directional derivatives rather than full gradients. This setting arises when fine-tuning large neural networks on consumer-grade hardware: the network's weights are matrices, memory constraints rule out backward-mode automatic differentiation, but directional derivatives remain available through forward mode.   We frame gradient estimation in this setting as a structured recovery pr...
  </details>

- **2026-09-02** — Shrenik Jadhav, Nickalsa LaPlaca, Caleb Stone et al. — [Compound Prompt Constraints in LLM Code Generation: A Factorial Study of Format, Persona, and Urgency](http://arxiv.org/abs/2609.03156v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in software engineering pipelines for code generation, where production prompts often combine multiple constraints. This paper presents a full-factorial empirical study of how output formatting, persona assignment, and urgency framing jointly affect LLM code-generation reliability. We evaluate all 27 combinations in a controlled 3x3x3 design and decompose each compound condition into an additive prediction and a residual interaction term that ca...
  </details>

- **2026-09-02** — Bigyan Ghimire, Jon C. Calhoun — [BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training](http://arxiv.org/abs/2609.03151v1)
  <details><summary>📄 Abstract</summary>
  Long-context reasoning for large language models (LLMs) is becoming increasingly important, but training over long sequences remains challenging due to massive memory and communication requirements. Sequence parallelism has emerged as an essential technique for addressing bottlenecks in long sequence LLM training. However, we observe that existing sequence parallelism methods are batch-agnostic and apply uniform sequence partitioning across all batch sizes, resulting in inefficient communication...
  </details>

- **2026-09-02** — Nithyanandan Thyagarajan, Jishnu Thekkeppattu, David Humphrey — [A fast, wide-field, and real-time imaging prototype for large aperture arrays](http://arxiv.org/abs/2609.03027v1)
  <details><summary>📄 Abstract</summary>
  Real-time processing on sub-millisecond timescales is essential for detecting fast astrophysical transients such as fast radio bursts (FRBs) and prompt electromagnetic counterparts to gravitational-wave mergers. Immediate localisation enables rapid multi-wavelength follow-up and maximises scientific return. As a result, real-time capability has become a key requirement for modern wide-field aperture arrays, which are increasingly being deployed at scales of thousands to tens of thousands of ante...
  </details>

- **2026-09-02** — Federico Gatta, Manuel Naviglio, Francesco Tarantelli — [Tempting the Agent: The Economics of Reputation without Persistent Identity in AI Agent Markets](http://arxiv.org/abs/2609.02992v1)
  <details><summary>📄 Abstract</summary>
  Reputation is a fundamental mechanism through which markets sustain trust when service quality cannot be perfectly assessed ex ante, constituting a form of intertemporal economic capital by attracting future demand. Its effectiveness as a disciplinary mechanism depends not only on past interactions but also on the persistence of the identity to which reputation is attached. When identities can be abandoned and recreated cheaply, reputational capital may itself become an object of opportunistic e...
  </details>

- **2026-09-02** — James Mickens — [The Implications of Linguistic Illegibility for LLM Security](http://arxiv.org/abs/2609.02852v1)
  <details><summary>📄 Abstract</summary>
  LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model computation. We introduce the term ``linguistic illegibility'' to broadly refer to scenarios in which an LLM's externalized or mechanistically-probed language artifacts fail to represent how the model actually thinks. We argue that the specter of lingu...
  </details>

- **2026-09-02** — Pengfei Wang, Anying Chen, Danjun Liu et al. — [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](http://arxiv.org/abs/2609.02647v1)
  <details><summary>📄 Abstract</summary>
  Linux kernel vulnerabilities are critical to downstream systems. Despite extensive research on automated kernel exploitation, a fundamental challenge remains the conceptual gap between abstract exploit strategies and concrete technical operations. To fill this gap, this paper introduces a systematic characterization that formalizes six classes of exploit primitives from logical capability to validatable effect. Then, an extended exploit strategy representation is proposed, which couples primitiv...
  </details>

- **2026-09-02** — Taehyeon Kim, Eunhyeok Park — [TaRA: Training-Aware Low-Rank Adaptation Initialization](http://arxiv.org/abs/2609.02639v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) has become a de facto standard for parameter-efficient fine-tuning (PEFT), yet its performance is highly sensitive to initialization due to the information bottleneck imposed by low-rank decomposition. Existing approaches attempt to construct high-quality LoRA initializations by exploiting principal components of pretrained weights, activations, or gradients. However, these methods do not directly account for the training dynamics of the full-rank model. In this paper,...
  </details>

- **2026-09-02** — Luca Migliaccio, Roberto Natella, Naghmeh Ivaki et al. — [Automated Vulnerability Injection in Smart Contracts Using Large Language Models](http://arxiv.org/abs/2609.02624v1)
  <details><summary>📄 Abstract</summary>
  Assessing vulnerability detection tools for smart contracts requires datasets with known ground truth, yet such datasets are scarce and difficult to build by hand. We propose an approach that uses Large Language Models (LLMs) to automatically inject vulnerabilities into Solidity smart contracts, and demonstrate it in a case study targeting 49 vulnerability types from OpenSCV. Injected contracts are validated through a multi-step pipeline checking compilation, execution, business logic, and the p...
  </details>

- **2026-09-02** — Eric Olsson, Benjamin Eriksson, Adam Doupé et al. — [SpiderSapien: Client-Centric Web Crawler and Security Scanner](http://arxiv.org/abs/2609.02532v1)
  <details><summary>📄 Abstract</summary>
  Black-box web application crawling and scanning play an important role for security testing of web applications. Yet state-of-the-art scanners fall short of addressing key characteristics of a modern web application: its extreme dynamism and interactivity on the client side. This paper identifies immersive interaction as a key ingredient for scanners to deeply explore modern web applications. We propose SpiderSapien, a client-centric crawler and security scanner. SpiderSapien incorporates a uniq...
  </details>

- **2026-09-02** — Viacheslav Yusupov, Daria Cherniuk, Evgeny Frolov — [Scalable Kronecker-Fisher Approximation: Efficient Hessian Analysis for Billion-Parameter Language Models Compression](http://arxiv.org/abs/2609.02451v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a scalable Kronecker-based approximation that captures cross-layer interactions without storing the entire Fisher matrix, enabling practical Hessian analysis for billion-parameter networks where full computation is infeasible. Our approach reveals consistent vulnerability patterns: value projection layers exhibit the highest sensitivity and strongest cross-layer correlations across multiple model families, while other components exhibit architecture-specific behaviors. ...
  </details>

- **2026-09-02** — Zhenyu Liang, Beichen Huang, Bowen Zheng et al. — [Semantics-Guided Automatic Tensorization for Multiobjective Evolutionary Algorithms: A Multi-Agent Framework](http://arxiv.org/abs/2609.02387v1)
  <details><summary>📄 Abstract</summary>
  Multiobjective evolutionary algorithms (MOEAs) naturally expose population-level parallelism, but many mature implementations encode their computation in sequential program structures designed for central processing units. Exploiting modern tensor computing platforms therefore requires more than direct code translation: the implementation must be restructured without changing the defining optimization mechanism of the underlying MOEA. We formulate automatic tensorization for MOEAs as semantics-g...
  </details>

- **2026-09-02** — Mehran Rahnamania, Michel Mandjes, Farid Ashtiani — [Analysis of Triggered Packet Streams: A Matrix-Analytic Method for Exponential Triggering Delays](http://arxiv.org/abs/2609.02320v1)
  <details><summary>📄 Abstract</summary>
  In many communication networks, the transmission of a packet may automatically trigger the transmission of a subsequent packet from the same source after a (possibly random) delay, without requiring acknowledgment or feedback. Such behavior arises in multi-stage status updating, proactive protocols, and other applications where users generate causally dependent packet streams. In this paper, in order to analyze these systems, we introduce the $\mathrm{M^T/G/1}$ queue. In this model, primary cust...
  </details>

- **2026-09-02** — Kaixiang Lu, Haiyu Lan, Chunxiao Qiao et al. — [Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots](http://arxiv.org/abs/2609.02306v1)
  <details><summary>📄 Abstract</summary>
  Accurate joint encoder offsets are essential for kinematic consistency in humanoid lower limbs, yet existing calibration methods typically require external motion-capture systems or fiducial targets. We present a self-contained calibration framework exploiting only onboard joint encoders and a pelvis-mounted IMU during static double-support contact. The inter-foot transform from forward kinematics must stay constant when both feet are fixed; minimizing its posture-dependent dispersion yields a n...
  </details>

- **2026-09-02** — Fang He, Wang-chien Lee — [SMart: A Multi-source Multi-phase Time Series Representation Transfer Framework](http://arxiv.org/abs/2609.02203v1)
  <details><summary>📄 Abstract</summary>
  Time series representation learning (TSRL) has attracted growing research interests in recent years. Two recent explorations in TSRL are: i) exploiting a transformer-based framework to learn time series; ii) instead of using only the targeted dataset, borrowing time series from other datasets to to facilitate representation transfer. While these two explorations are shown effective, the self-supervised time series recovery task in (i) and the single-source dataset used in (ii) are technically si...
  </details>

- **2026-09-02** — Benjamin C Liu, Dillon Mehta, Rishi Malhotra et al. — [Examining the Vulnerability of Multi-Agent Medical Systems to Human Interventions for Clinical Reasoning](http://arxiv.org/abs/2609.02191v1)
  <details><summary>📄 Abstract</summary>
  Human interventions at fault points can alter the diagnostic accuracy of multi-agent medical systems. We defined fault points as moments in AI agent conversations, in which an agent's reasoning became most vulnerable to external influence. Using the MedQA dataset, this study analyzed simulated doctor-patient conversations to measure how interventions shifted reasoning and accuracy. Correct intervention methods showed an improvement in baseline diagnostic accuracy of up to 40%, while incorrect or...
  </details>

- **2026-09-02** — Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio, Lucas Pascotti Valem et al. — [Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval](http://arxiv.org/abs/2609.01963v1)
  <details><summary>📄 Abstract</summary>
  Content-based image retrieval (CBIR) has advanced significantly with deep learning, yet effectively ranking similar images remains challenging, particularly in high-dimensional feature spaces, where pairwise distances often fail to capture contextual relationships and the semantic gap between visual features and high-level concepts persists. Manifold learning and rank-based refinement methods have emerged as complementary strategies, respectively improving feature representations and exploiting ...
  </details>

- **2026-09-01** — Martina Torsello, Marcella Massardi, Elisabetta Liuzzo et al. — [The ViSta method for optimized stacking of broadband interferometric data in the Fourier domain](http://arxiv.org/abs/2609.01897v1)
  <details><summary>📄 Abstract</summary>
  We present the optimized version of ViSta, a visibility-domain stacking method that combines interferometric observations in the Fourier domain from radio to sub-millimeter wavelengths. By stacking visibilities directly and transforming them into the rest frame, ViSta enhances the signal, suppresses noise, and improves image reconstruction through extended uv-coverage. ViSta outperforms image stacking when individual sources are too faint to detect, achieving higher SNR in the low-signal and ext...
  </details>

- **2026-09-01** — Henry Arthur — [Thinking effort aligns between humans and reasoning models in abductive reasoning](http://arxiv.org/abs/2609.01867v1)
  <details><summary>📄 Abstract</summary>
  A major question in cognitive modeling concerns the behavioral alignment between large language models and humans across linguistic and non-linguistic tasks. Unlike standard LLMs, large reasoning models (LRMs) are optimized with reinforcement learning from verifiable rewards, encouraging correct solutions to reasoning tasks rather than preference-aligned responses. Recent work (de Varda et al., 2025) investigates the cost of thinking in humans and LRMs by comparing human reaction times with mode...
  </details>

- **2026-09-01** — Osvaldo M Velarde, Lucas C Parra, Alireza Hashemi et al. — [Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks](http://arxiv.org/abs/2609.01768v1)
  <details><summary>📄 Abstract</summary>
  Artificial neural networks are often regarded as powerful yet opaque black boxes. Here, we demonstrate that learning in deep neural networks generates local symmetries known in graph theory as fibrations and coverings. We prove that covering symmetries are stable attractors of stochastic gradient descent. Consistent with this theory, we report the emergence of covering symmetries across major network architectures, including multilayer, convolutional, recurrent, and transformer networks. Exploit...
  </details>

- **2026-09-01** — Enna Basic, Alberto Giaretta — [Towards Behavior Tree-Guided Vulnerability Detection with Lightweight LLMs](http://arxiv.org/abs/2609.01758v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for software vulnerability detection, but their performance depends on how source code is represented in the input. Most prompting approaches use source code in its original form, while some works propose the use of structured representations. Abstract Syntax Trees (ASTs) are one of the most popular approaches, but AST verbosity increases input size relative to source code, making them hard to fit within some LLMs context windows. This paper inv...
  </details>

- **2026-09-01** — Shuaicheng Niu, Guohao Chen, Yaofo Chen et al. — [A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference](http://arxiv.org/abs/2609.01679v1)
  <details><summary>📄 Abstract</summary>
  The ability of AI systems to improve their behavior during deployment is becoming increasingly important. As inference moves beyond the static execution of a fixed trained model, a growing body of work studies how models can refine their behavior on the fly by exploiting test-time information and additional computation. These developments have largely evolved along two directions: methods that modify the model's state using test-time signals, and methods that improve predictions through extra in...
  </details>

- **2026-09-01** — Jincheng Zhang, Chen Huang, Wenqiang Lei et al. — [Towards Effective Structured Context Modeling for Conversational Recommender Systems via Dual-node Monte Carlo Tree Search](http://arxiv.org/abs/2609.00618v2)
  <details><summary>📄 Abstract</summary>
  We investigate the role of conversational context modeling in user preference tracking for Conversational Recommendation Systems (CRSs). In this regard, we propose DREAMS, a novel tree-structured context modeling framework that explicitly captures user preference evolution throughout multi-turn interactions. DREAMS introduces two specialized node types to support the two fundamental objectives of CRSs: preference elicitation and preference exploitation. Specifically, elicitation nodes leverage M...
  </details>

- **2026-09-01** — Marven Sherif, Amgad Elmasry, Youssef Ghazal et al. — [BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net](http://arxiv.org/abs/2609.01554v1)
  <details><summary>📄 Abstract</summary>
  Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V challenge addresses this by making segmentation interactive: user scribbles marking foreground and background are supplied alongside the image, and the algorithm is expected to exploit them. We present our submission, a scribble-conditioned residual encoder U-Net operating on four input channels: CT, P...
  </details>

- **2026-09-01** — Tomáš Holeček, Viliam Lisý — [NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games](http://arxiv.org/abs/2609.01549v1)
  <details><summary>📄 Abstract</summary>
  Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized model learning faces severe identifiability barriers, which we argue make centralized model learning a mathematical necessity. Building on this analysis, we propose NashDreamer, a principled MBRL fra...
  </details>

- **2026-09-01** — Stephanie Fong, Yiwen Jiang, Zimu Wang et al. — [SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue](http://arxiv.org/abs/2609.01548v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound effects on people and communities, benchmarks remain scarce. Existing general-domain evaluations typically rely on static prompts and fixed-format tasks, overlooking conversational contexts and audience effects in everyday communication. To address these gaps, we introduce SDARE-Bench, the first scenario-based benchmark evaluating both stigma detec...
  </details>

- **2026-09-01** — Tingting Ni, Maryam Kamgarpour — [Provably Safe Sim-to-Real Transfer](http://arxiv.org/abs/2609.01418v1)
  <details><summary>📄 Abstract</summary>
  To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in man...
  </details>

- **2026-09-01** — Matheus F. Kovaleski, Luís Garrote, Cristiano Premebida et al. — [Multimodal RGB-Infrared Combination for UAV-Based Wildfire Segmentation: A Comparative Study on FLAME3](http://arxiv.org/abs/2609.01390v1)
  <details><summary>📄 Abstract</summary>
  Unmanned Aerial Vehicles (UAVs) have emerged as a promising platform for firefighting operations due to their flexibility, low operational cost, and ability to acquire high-resolution imagery in locations that may be difficult or dangerous to access using conventional methods. Recent advances in deep learning have significantly improved the capabilities of UAV-based wildfire monitoring systems. The present work investigates RGB-infrared fusion for binary wildfire segmentation on the FLAME3 datas...
  </details>

- **2026-09-01** — Jidong Yang, Qi Li, Wei Zong et al. — [One Prompt Is Enough: Watermark Laundering Through Foundation Image Models](http://arxiv.org/abs/2609.01249v1)
  <details><summary>📄 Abstract</summary>
  Invisible watermarks are typically evaluated against predefined perturbations such as compression, blur, noise, cropping, and denoising. Public foundation image models expose a distinct threat: an attacker can submit a watermarked image with a single reconstruction prompt and obtain a visually faithful output from which the invisible watermark can no longer be decoded reliably. We formalize this failure mode as watermark laundering and evaluate it using a joint payload-fidelity profile that comb...
  </details>

- **2026-09-01** — Jie Chen, Xiangqian Yu, Yanchao Lian et al. — [From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs](http://arxiv.org/abs/2609.01240v1)
  <details><summary>📄 Abstract</summary>
  Scaling Transformers has driven large gains in language modeling, but transplanting this to behavior-sequence modeling in production ranking is challenging: recommendation differs in signal quality, where behavior sequences are noisy, temporally irregular, and sparsely supervised, and in computation asymmetry, where each request scores many candidates against one shared user history under tight latency budgets. We propose ReST, a recommendation-native Transformer scaling framework. For signal qu...
  </details>

- **2026-09-01** — Maciej Śmiertka, Ewelina Cybula, Oliwia Janikowska et al. — [Geometry-Controlled Magnetic and Electronic Landscapes in Anisotropic van der Waals Materials](http://arxiv.org/abs/2609.01223v1)
  <details><summary>📄 Abstract</summary>
  Electronic structure in van der Waals materials is commonly engineered through composition, strain, electrostatic gating and heterostructure assembly. Here we introduce geometronics, a concept in which substrate geometry locally reorients an anisotropic crystal, transforming homogeneous external perturbation into programmable magnetic and electronic landscapes. We demonstrate this concept using a bilayer of the antiferromagnetic semiconductor CrSBr transferred onto an inverted pyramidal nanoinde...
  </details>

- **2026-09-01** — Phong Trinh Duy, Trang Dang Yen, Hung Nguyen-Huu et al. — [Athena: Vulnerability-Affected Library Identification via Knowledge Graph Completion](http://arxiv.org/abs/2609.01187v1)
  <details><summary>📄 Abstract</summary>
  A single vulnerability in a widely used library can cascade through millions of dependent applications, yet more than half of vulnerability database entries contain missing or incorrect affected-library information. Existing automated approaches neglect the relational structure of vulnerability databases, treating identification as an isolated text retrieval problem. In this paper, we propose Athena, the first graph-based approach for vulnerability affected library identification. Athena models ...
  </details>

- **2026-09-01** — Hadjer Benkraouda, Hongyu Cai, Berkay Celik et al. — [Reveree: Diagnosing LLM Reverse-Engineering Agents](http://arxiv.org/abs/2609.01185v1)
  <details><summary>📄 Abstract</summary>
  Reverse engineering (RE) is critical to security tasks such as malware analysis and vulnerability discovery, and large language model (LLM) agents are increasingly able to perform it autonomously. Capture-the-flag (CTF) RE challenges have become the standard proxy for measuring this capability, but evaluation rests on a single criterion: whether the agent captures the flag. This solve rate reveals neither where in the RE process an agent fails nor whether a success reflects analysis of the binar...
  </details>

- **2026-09-01** — Ziyan Gan, Fangxin Liu, Chenyang Guan et al. — [PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition](http://arxiv.org/abs/2609.01024v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token. However, modern MoE inference remains heavily constrained by the rigid, whole-expert abstraction. Existing frameworks manage, schedule, or prune experts as atomic execution units, which fixes the optimization boundary too early and leaves fine-grained intra-expert computational redundancy underexplored. In this work, we present PCoMoE, a path-compositio...
  </details>

- **2026-09-01** — Baoshun Wang, Weiping Lin, Linwu Wang et al. — [Semi-Supervised Virtual Staining via Morphology Preservation and Histopathological Realism Constraints](http://arxiv.org/abs/2609.00984v1)
  <details><summary>📄 Abstract</summary>
  Virtual staining aims to computationally generate target-stained histopathological images while reducing the cost and time associated with conventional staining procedures. However, existing methods rely predominantly on strictly paired and accurately registered training data, which are difficult and expensive to obtain in routine practice. To reduce this dependence, we propose a stable semi-supervised virtual staining framework that jointly exploits both limited paired data and abundant unpaire...
  </details>

- **2026-09-01** — Peng Xu, Zuyu Zhang, Yuze Sun et al. — [ContextPipe: Database-Inspired Context Assembly for Long-Horizon Agents](http://arxiv.org/abs/2609.00749v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon large language model (LLM) agents require context assembly: the runtime must decide what to include in each prompt, in what order, and when to compact history under a hard context-window budget and a byte-sensitive prompt cache. In production agentic systems, this logic is scattered across prompt builders, ad hoc compaction routines, cache-break workarounds, and per-provider shims. We argue that context assembly is structurally isomorphic to query execution in a relational database:...
  </details>

- **2026-09-01** — Hu Cao, Qianyi Yang, Xinyi Li et al. — [Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement](http://arxiv.org/abs/2609.00713v1)
  <details><summary>📄 Abstract</summary>
  Estimation of the absolute pose of an object is an essential task for various robotic applications. Recently, incorporating gravity direction as prior information has emerged as a popular approach to simplify absolute pose estimation. However, developing a robust and efficient algorithm to solve this challenging problem remains a difficult question due to large amounts of mismatches. In addition, obtaining an accurate pose solution from selected inlier correspondences with gravity prior is still...
  </details>

- **2026-09-01** — Kaizhen Tan, Yang Feng, Heqing Du et al. — [Teaching Vision-Language Models to Use the Scale They Are Given: Label-Free Equivariance Training for Metric Physical Reasoning](http://arxiv.org/abs/2609.00658v1)
  <details><summary>📄 Abstract</summary>
  Metric questions about video require vision-language models to use supplied real-world references to convert visual measurements into physical units. Yet we find that current models use this scale information only partially. When every world-space quantity in a prompt is rescaled by a common factor, the video remains equally valid and the correct answer changes by exactly that factor, but model predictions move only part of the way and accuracy remains concentrated near the familiar scale of the...
  </details>

- **2026-09-01** — Yuta Kato, Shintaro Ozaki, Kazuki Hayashi et al. — [ExpArt-KG: Artwork Image Description Generation through Iterative Exploration of Knowledge Graphs](http://arxiv.org/abs/2609.00629v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) achieve strong performance on image-grounded text generation and visual question answering. However, it remains difficult for them to comprehensively and accurately describe the factual relations among the entities and concepts associated with the objects depicted in an image. In this work, we propose a framework that efficiently exploits factual information from a knowledge graph via retrieval-augmented generation (RAG), with the goal of enabling LVLMs to ge...
  </details>

- **2026-09-01** — Jincheng Zhang, Chen Huang, Wenqiang Lei et al. — [Towards Effective Structured Context Modeling for Conversational Recommender Systems via Dual-node Monte Carlo Tree Search](http://arxiv.org/abs/2609.00618v1)
  <details><summary>📄 Abstract</summary>
  We investigate the role of conversational context modeling in user preference tracking for Conversational Recommendation Systems (CRSs). In this regard, we propose DREAMS, a novel tree-structured context modeling framework that explicitly captures user preference evolution throughout multi-turn interactions. DREAMS introduces two specialized node types to support the two fundamental objectives of CRSs: preference elicitation and preference exploitation. Specifically, elicitation nodes leverage M...
  </details>

- **2026-09-01** — Sethuraman T, Savya Khosla, Onkar Kishor Susladkar et al. — [ViTAL-X: Video-Text Alignment with Cross-Modal Temporal Edits](http://arxiv.org/abs/2609.00505v1)
  <details><summary>📄 Abstract</summary>
  Video-text models adapted from image-text architectures (e.g., CLIP) frequently exhibit temporal blindness, the inability to perceive fundamental cues like order, direction, and motion dynamics. Standard datasets mask this limitation by enabling models to exploit static spatial shortcuts. To systematically evaluate this, we introduce XTE-Bench, a diagnostic probe revealing that even large-scale video-language models struggle with basic temporal reasoning, indicating that parameter scaling alone ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

- **2026-09-03** — Mohammad Mohammadi, Alireza Zarei — [RobustSeiz: An Open-Source Framework for Benchmarking the Robustness of EEG Seizure Detection Models](http://arxiv.org/abs/2609.04007v1)
  <details><summary>📄 Abstract</summary>
  Despite strong performance on held-out electroencephalography (EEG) data, seizure detectors may fail under real-world acquisition variability, artifacts, and adversarial inputs. We introduce RobustSeiz, an open-source, model-agnostic framework that provides a standardized, reproducible protocol for stress-testing and comparing seizure detectors under controlled, clinically motivated distribution shifts before deployment. We standardize four public scalp-EEG corpora (CHB-MIT, TUSZ, Siena, and Sei...
  </details>

- **2026-09-03** — Veli Karakaya, Semih Çağlar, Yusuf Yiğit Korkmaz et al. — [ATIBA: Grounded Integrity and Quality Checking for Research Papers](http://arxiv.org/abs/2609.04123v1)
  <details><summary>📄 Abstract</summary>
  Checking a manuscript's reference integrity, its compliance with a target venue's specific submission rules, and its adherence to community reporting standards is manual, repetitive, and different for every venue so in practice it is done inconsistently or skipped. We present ATIBA, a tool that runs five grounded integrity and quality checks on a manuscript: a reference-integrity check that verifies each citation against bibliographic sources and flags retracted or unfindable references; a venue...
  </details>

- **2026-09-03** — Arslan Brömme — [A Black Box for Agentic Processes: Blockchain-Anchored Evidence for AI Agent Communication, Human Oversight, and GRC Audits](http://arxiv.org/abs/2609.04017v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents increasingly communicate with other agents, invoke tools, exchange intermediate results, and request human approvals. These workflows create a new auditability problem: organizations must reconstruct what happened, when it happened, which agent or human was involved, which control or policy applied, and whether records were modified afterwards. Motivated by the 2026 OpenAI/Hugging Face incident, this position and architecture paper proposes a product- and vendor-neutral blac...
  </details>

- **2026-09-03** — Chao Shen, Xinyuan Li, Yunfan Zhou et al. — [InSituMeasure: Probing Situated Measurement Grounding in Industrial Scenes with Multimodal Large Language Models](http://arxiv.org/abs/2609.04014v1)
  <details><summary>📄 Abstract</summary>
  For trained operators, gauge reading requires little specialized knowledge, low cognitive effort, and high repeatability. Yet Multimodal Large Language Models (MLLMs) remain unreliable in continuous-valued measurement despite strong results on general multimodal benchmarks. Existing benchmarks expose this weakness but isolate measurement from realistic, knowledge-grounded settings, with limited situated context, specialized instruments, real-world noise, and matched diagnostic annotations, reduc...
  </details>

- **2026-09-03** — Joe Cecil, Marjorie Freedman — [Beyond Majority Vote: Multi-Perspective Adjudication for Medical Hallucination Detection](http://arxiv.org/abs/2609.03953v1)
  <details><summary>📄 Abstract</summary>
  Understanding the frequency of factual errors in chatbot-generated text and evaluating systems that detect these errors is critical for determining chatbot safety. Yet factual-error detection is often treated as a single-pass, single-annotator labeling problem. In long-form chatbot responses, factual errors can be subtle and embedded within mostly correct text.   We develop a multi-perspective annotation study of medically relevant chatbot responses, combining first-pass annotation, LLM-as-a-Jud...
  </details>

- **2026-09-03** — Junjie Pang, Zhenzhen Xie, Haoke Han et al. — [DNative-Twin: Decision Graphs and Digital Twins for Reconstructable Agentic Decisions](http://arxiv.org/abs/2609.03787v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly gather evidence, invoke tools, apply constraints, and produce decisions that people or software may commit to action. A final output alone cannot show which evidence, tool state, rule, authorization, or action path produced it. We present DNative-Twin, a graph-native digital twin that records a committed agentic decision as a typed trajectory and re-executes its decision mechanism under declared conditions. The graph links the state observed by the agent, the path it follo...
  </details>

- **2026-09-03** — Xiaoyu Yang, Qixing Wu, Huixian Zhao et al. — [PL-SCEA: Reconfiguring Pretrained Attention for Few-Shot Industrial Anomaly Detection](http://arxiv.org/abs/2609.03655v1)
  <details><summary>📄 Abstract</summary>
  Vision Foundation Models (VFMs) provide transferable patch representations for few-shot industrial anomaly detection, but their attention computation is typically inherited from pretraining objectives centered on semantic aggregation. This creates a potential mismatch: token relations that support semantic recognition may not adequately expose the localized texture and structural deviations required for anomaly localization. We therefore investigate the hypothesis that the attention computation ...
  </details>

- **2026-09-03** — Sima Attar-Khorasani, Matthias Lieber, Siavash Ghiasvand — [RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters](http://arxiv.org/abs/2609.03598v1)
  <details><summary>📄 Abstract</summary>
  The emergence of modern agents powered by large language models has created a demand for executing long-horizon, autonomous workflows in various domains that require significant computational resources. While High Performance Computing clusters provide the ideal infrastructure for these computation-intensive workloads, traditional HPC job schedulers such as Slurm are not designed for dynamic, agentic workflows characterized by unpredictable task durations, external API calls, and fault tolerance...
  </details>

- **2026-09-03** — Tzu-Ling Lin, Dong-Ting Yao, Teng-Fang Hsiao et al. — [HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews](http://arxiv.org/abs/2609.03580v1)
  <details><summary>📄 Abstract</summary>
  The growing scale of academic peer review has motivated the use of Large Language Models (LLMs) as review assistants, yet LLMs can generate fluent but unsupported claims that undermine review reliability. Existing hallucination benchmarks are not designed for peer review, where verification requires grounding claims in long, technical papers. We introduce HalluPeer, a benchmark for detecting hallucinations in scientific peer reviews, providing aligned triples of paper content, human-written revi...
  </details>

- **2026-09-03** — Weijie Liu, Running Zhao, Wenhao Yuan et al. — [Dude: A Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection](http://arxiv.org/abs/2609.03416v1)
  <details><summary>📄 Abstract</summary>
  LLM-empowered paper-code discrepancy detection has received growing concern since the scaling of research submissions exceeds the manual review capability. However, the limited context capacity and one-sided discrepancy detection of existing single-agent LLM paradigms lead to an inferior recall performance in detecting discrepancies. In this paper, we propose Dude, the first Dual-Detection Multi-Agent System for paper-code discrepancy detection. We discover that the granularity asymmetry of the ...
  </details>

- **2026-09-03** — Huixiang Fu, Marian-Andrei Rizoiu — [Less Is Moral: A CHARMing Framework for Moral Foundations Detection in Endorsement Behaviour](http://arxiv.org/abs/2609.03330v1)
  <details><summary>📄 Abstract</summary>
  Moral language plays a central role in shaping online endorsement and the diffusion of information, yet existing moral foundation detection systems often suffer from poor cross-domain generalization, weak rationale grounding, and reliance on costly prompting-based large language models (LLMs). We introduce CHARM, a MA\textbf{C}- and \textbf{H}ate-speech-\textbf{A}ware \textbf{R}ationale-aligned \textbf{M}oral foundation detection framework built on a lightweight fine-tuned LLM, which integrates ...
  </details>

- **2026-09-03** — Yoojin Kim, Jihyoung Jang, Hyounghun Kim — [PACE: Towards Surfacing Hidden Conflicts in User Requests](http://arxiv.org/abs/2609.03293v1)
  <details><summary>📄 Abstract</summary>
  Personalized assistants should not only comply with user requests but also assess whether those requests are appropriate given the user's current circumstances. However, prior work has primarily focused on accurately executing requests, overlooking the need for assistants to account for context and engage in conflict-based refusal. Furthermore, while existing work on conflict or safety detection relies on explicitly provided factors, real-world scenarios often involve implicit factors that must ...
  </details>

- **2026-09-03** — Taewoo Kim, Young Han Lee, Nam In Park et al. — [ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection](http://arxiv.org/abs/2609.03620v1)
  <details><summary>📄 Abstract</summary>
  Audio deepfake detection is commonly formulated as clip-level binary classification of single-domain audio. However, real-world manipulated audio can exhibit mixed authenticity, where genuine and manipulated cues coexist across temporal transitions, overlapping sources, or both. This setting requires not only detecting manipulated audio but also localizing the components that provide evidence for the decision. We propose ToolDF, a tool-integrated reasoning framework for mixed-authenticity audio ...
  </details>

- **2026-09-03** — Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan — [FailBench: How Reliable are VLMs at Judging Robot Task Success?](http://arxiv.org/abs/2609.03611v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly used to evaluate robot manipulation outcomes, but existing benchmarks offer limited evidence of cross-domain generalization. We introduce FailBench, a benchmark for robot failure detection comprising 2,197 manipulation attempts across 14 public sources (12 real-world, 2 simulated). In FailBench, 75% of failures occur naturally, and six real-world sources come from non-failure-detection datasets. Evaluating 13 VLM-based detectors, we find the best mo...
  </details>

- **2026-09-03** — Yidi Wang, Feixiang Ruan, Ruoqu Chen et al. — [R2S-Eval: Robot Evaluation with Real-to-Sim Calibration via Vision-Language Models](http://arxiv.org/abs/2609.03276v1)
  <details><summary>📄 Abstract</summary>
  Evaluating robot manipulation policies is becoming increasingly important as generalist models, particularly vision-language-action (VLA) models, are deployed on physical robots. However, conventional real-world evaluation remains labor-intensive, unstable, and insufficiently informative. It requires repeated hardware trials, manual scene resets, and continuous operator monitoring, may produce different policy rankings across repeated evaluations, and primarily relies on success-rate metrics tha...
  </details>

- **2026-09-03** — Simone Ceppi, Ignacio Sanchez — [Flip, Don't Shuffle: Watermarking LLMs at the Speed of Inference](http://arxiv.org/abs/2609.03844v1)
  <details><summary>📄 Abstract</summary>
  We introduce Stateless Bernoulli Watermarking (SBW), a new statistical watermark for Large Language Models that determines green list membership through independent per-token Bernoulli trials. Unlike KGW's vocabulary permutation or SynthID's multi-layer tournament, SBW requires only a single comparison per token against a counter-based random number generator, reducing membership complexity to $O(1)$ and enabling single-kernel execution with zero intermediate allocations. We prove that this form...
  </details>

- **2026-09-03** — Nicolas Baron Perez, Marcus Brüggen, Luisa Lucie-Smith — [Morphology of Radio Sources in Representation Space](http://arxiv.org/abs/2609.03779v1)
  <details><summary>📄 Abstract</summary>
  Understanding radio source morphologies and their classification remains challenging. We previously developed a deep clustering method based on self-supervised learning to classify a subsample of radio sources from the LOFAR Two-meter Sky Survey DR2. This yielded a labelled subset used to fine-tune an ensemble of classifiers. We aim to identify rare morphological classes in a subsample of LoTSS-DR3, which contains > 13 million sources, beyond the 12 classes previously recognised in the DR2 sampl...
  </details>

- **2026-09-02** — Haozhang Li, Yangguang Shao, Xinjie Lin et al. — [When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization](http://arxiv.org/abs/2609.02964v1)
  <details><summary>📄 Abstract</summary>
  This paper focuses on defending generative search engines against malicious Generative Engine Optimization (GEO), which rewrites web documents to match engines' citation preferences and thereby manipulates generated answers. Recent GEO methods have advanced from hand-crafted rewriting to automated and agentic optimization, substantially increasing the visibility of target documents in generated answers. However, defending against such manipulation poses two major challenges: attack documents rem...
  </details>

- **2026-09-02** — Vijay Erramilli — [ObserverBench: Testing Mechanistic Estimates for Intervention and Control](http://arxiv.org/abs/2609.03026v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability is increasingly used to guide interventions such as activation steering, circuit removal, and safety monitoring. Yet an internal estimate that is accurate on average can still choose a poor action.   We present ObserverBench, a benchmark framework for testing whether an internal estimator---an observer---is adequate for the intervention, control, or safety task it directs. Each task fixes the model, information boundary, allowed actions, decision rule, held-out cases...
  </details>

- **2026-09-02** — Sai Huang, Wanli Ni, Ke Lv et al. — [Direct Satellite-to-Device Communications: From Cooperative Task Offloading to Non-Cooperative Access Monitoring](http://arxiv.org/abs/2609.02955v1)
  <details><summary>📄 Abstract</summary>
  Direct satellite-to-device (DS2D) communication is emerging as a transformative paradigm for extending ubiquitous connectivity and edge computing capabilities to remote and underserved regions within 6G non-terrestrial networks. However, practical deployment faces dual critical challenges: i) dynamic satellite channel conditions (e.g., severe Doppler shifts, fast fading) and constrained satellite computing resources in cooperative scenarios; and ii) unauthorized satellite access introduces signi...
  </details>

- **2026-09-02** — Javed M. Shah, Ian A. Kash, Natalie Parde — [A Bayesian Correlated Equilibrium for Early Insider-Threat Detection](http://arxiv.org/abs/2609.03096v1)
  <details><summary>📄 Abstract</summary>
  We model insider threat detection as a dynamic Bayesian game in which a platform coordinates a committee of strategic certifiers to sustain equilibrium among honest users and detect malicious deviations before exfiltration. Certifiers and users operate under a Bayesian Temporal Correlated Equilibrium (BTCE), where a sealed-envelope correlating device issues private recommendations over time and obedience is verified at every on-path information state. Unlike Stackelberg formulations, BTCE coordi...
  </details>

- **2026-09-02** — Bing Zheng, Zongyao Zhao, Wenming Yang — [Counter-GEO-Bench: Evaluating Defenses Against Information-Distorting Generative Engine Optimization](http://arxiv.org/abs/2609.02316v1)
  <details><summary>📄 Abstract</summary>
  Generative engine optimization (GEO) enables content producers to increase the visibility of their web pages in generative search engines, but the same techniques can deliver targeted misinformation when adversaries publish ordinary-looking GEO-optimized documents that victim large language models (LLMs) retrieve and synthesize into distorted answers. No existing benchmark evaluates defenses against this threat under controlled conditions. Therefore, we present Counter-GEO-Bench, a defense bench...
  </details>

- **2026-09-02** — Gang-Hyun Park, Ju-Hyeong Lee, Hee-Youl Kwak et al. — [WeaveMark: Robust and Scalable Multi-bit LLM Watermarking via Coded Payload Spreading](http://arxiv.org/abs/2609.02177v1)
  <details><summary>📄 Abstract</summary>
  Multi-bit watermarking for large language models (LLMs) enables content source tracing by embedding user-identifiable messages into generated text. Existing methods face a fundamental trade-off among extraction accuracy, text quality, and payload capacity. We propose WeaveMark, a robust and scalable multi-bit LLM watermarking scheme based on coded payload spreading. WeaveMark shifts this trade-off frontier by improving payload capacity through multi-bit-per-token spreading, improving extraction ...
  </details>

- **2026-09-02** — Jaehoon Jeong, Jay-Yoon Lee — [OBJECTION! Lawyer Agents Mitigate Guilty Bias in Legal Judgment Prediction](http://arxiv.org/abs/2609.02158v1)
  <details><summary>📄 Abstract</summary>
  Legal Judgment Prediction (LJP) models are typically trained on documents that describe facts from a prosecutorial perspective. Existing datasets further exhibit severe label imbalance toward guilty outcomes. Consequently, these models suffer from "Guilty Bias", blindly accepting the prosecution's narrative as objective truth. Previous studies employing three-step reasoning structures or training on synthetically generated innocence data improve overall accuracy, but they still fail to mitigate ...
  </details>

- **2026-09-02** — Cagri Temel — [Towards Trustworthy Autonomous Robots: An Explainable AI-Based Decision Framework](http://arxiv.org/abs/2609.02861v1)
  <details><summary>📄 Abstract</summary>
  Autonomous robots powered by deep learning face a fundamental auditability challenge: when incidents occur, investigators cannot reconstruct why the system made specific decisions. This paper presents TRACE (Transparent Reasoning Architecture for Credible Execution), a decision framework that ensures every autonomous action can be traced back to sensor evidence through documented causal chains. The framework organizes decision-making into four auditable layers: Semantic Perception for evidence-g...
  </details>

- **2026-09-02** — Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang et al. — [CORAL: An LLM-Native Harness for Production Recommender Systems](http://arxiv.org/abs/2609.02730v1)
  <details><summary>📄 Abstract</summary>
  Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization: as content, user behavior, and upstream models shift, the choices governing retrieval, ranking, and serving must be revisited. Traditionally, human engineers test such changes through online experiments--a slow, reactive process limited by engineering effort, leaving parts of the system unrevised as conditions change. Although large language models have been applied...
  </details>

- **2026-09-02** — Rafael Uetz, Philipp Bönninghausen, Louis Hackländer-Jansen et al. — [Can Risk-Based Alerting Mitigate Cybersecurity Alert Fatigue?](http://arxiv.org/abs/2609.02465v1)
  <details><summary>📄 Abstract</summary>
  Security operations centers (SOCs) face large numbers of false alerts, making detection of cyberattacks difficult under typical resource constraints. Risk-based alerting (RBA) has been proposed as a means to reduce false alerts and has reportedly succeeded in doing so in various enterprise deployments. However, RBA has not been comprehensively evaluated until now, leaving implementation mostly guesswork based on anecdotal evidence. In this paper, we present the first systematic evaluation of RBA...
  </details>

- **2026-09-02** — Oguzhan Salman, Kemal Bicakci — [CAPTCHAs in the Agentic Era: Solvers That Learn from Every Encounter](http://arxiv.org/abs/2609.02393v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can solve visual CAPTCHAs without task-specific training, but the agents built on them approach every challenge from scratch. For such an agent, the hundredth instance of a familiar puzzle costs as much time and compute as the first. Specialized detectors invert the trade-off, answering in milliseconds but only for categories they were trained on. Neither improves with exposure. We study what changes when a solver improves with use. Our system pairs a fine-tuned YOL...
  </details>

- **2026-09-02** — Yinghao Sun, Shuguang Li, Jinliang Shao et al. — [If It Moves, Radar Knows: A Physics-Aware Radar Transformer for Class-Agnostic Moving-Object Detection](http://arxiv.org/abs/2609.02289v1)
  <details><summary>📄 Abstract</summary>
  Detectors trained on closed-set annotations can miss rare moving objects outside the training taxonomy. Automotive radar provides category-independent Doppler motion cues and is less affected by adverse illumination and weather, but sparse, noisy returns hinder class-aware 3D box detection. Surface location and velocity remain useful for motion reasoning and collision avoidance when full box geometry is difficult to recover. We present the Physics-Aware Radar Transformer (PART), a fully sparse r...
  </details>

- **2026-09-02** — Vansh Wahi — [LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails](http://arxiv.org/abs/2609.02246v1)
  <details><summary>📄 Abstract</summary>
  Self-improving agent pipelines have a problem at their center. An optimizer rewrites prompts to score higher, and the score comes from a judge that is itself an LLM. That judge has the last word on whether the system is getting better, and our position is that it has not earned it. The judge should be demoted from oracle to advisor: its verdict becomes one input among several, and every change is gated instead by a deterministic verification layer the judge cannot override. We reached this posit...
  </details>

- **2026-09-02** — Ritesh Kumar — [text2ql: Multi-Target Natural Language Querying via a Language-Agnostic Intermediate Representation](http://arxiv.org/abs/2609.02115v1)
  <details><summary>📄 Abstract</summary>
  Natural language interfaces to databases have traditionally suffered from three structural limitations: exclusive targeting of relational SQL, unconditional dependence on large language model (LLM) inference at query time, and absence of any runtime signal when generated queries are semantically incorrect. This paper presents text2ql, an open-source Python framework that addresses all three limitations through a language-agnostic Intermediate Representation (QueryIR) and a pluggable renderer arc...
  </details>

- **2026-09-02** — Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park et al. — [DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents](http://arxiv.org/abs/2609.02059v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use textual context to determine how chart evidence should be selected, interpreted, and aggregated. We introduce DocHop, a benchmark for integrated chart--context reasoning in document-style images. In ...
  </details>

- **2026-09-02** — Niloo Bahadori, Swadhin Pradhan, Peiman Amini — [Network-Aware Forecasting on Wireless Access Points](http://arxiv.org/abs/2609.01957v1)
  <details><summary>📄 Abstract</summary>
  Enterprise wireless access points (APs) are promising platforms for predictive machine learning (ML), but their primary responsibility remains providing wireless connectivity and network services. Predictive inference must therefore share an AP's CPU and memory with packet processing, Wi-Fi and IoT radio operations, and client management. This resource contention creates two risks: a model that performs well on proxy hardware may be too slow on the target AP, while a model that fits in isolation...
  </details>

- **2026-09-02** — Urja Pawar, Rajitha Ramanayake, Owen O'Neill et al. — [From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs](http://arxiv.org/abs/2609.02679v1)
  <details><summary>📄 Abstract</summary>
  When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited human-review capacity. When no trusted context or reference document is available, we study two signals accessible through black-box model APIs: semantic entropy, which measures disagreement among sampled response meanings, and uncertainty derived from token log-probabilities. Their failure modes can be complementary: semantic entropy becomes uninforma...
  </details>

- **2026-09-02** — Zhongrui Sun, Jiahao Chen, Oubo Ma et al. — [The Shape of Ownership: Verifying LLM Provenance through Semantic Structures](http://arxiv.org/abs/2609.02553v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly redistributed, adapted, and served behind opaque APIs, model ownership can no longer be established reliably by inspecting model internals or deployment records. This creates a need for behavioral signatures that remain observable through black-box interaction. Yet most existing black-box fingerprints instantiate ownership signals through fixed query-key associations, reducing model identity to sparse memorized associations detached from ordinary ...
  </details>

- **2026-09-02** — Austin Tudor David Andrews, Liam Wilkinson, Jamie Heagerty et al. — [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI](http://arxiv.org/abs/2609.02459v1)
  <details><summary>📄 Abstract</summary>
  We present CivBench, an open-source benchmark for evaluating language model agents in long-horizon, tool-mediated environments through the Model Context Protocol (MCP). A single episode spans 300+ turns and produces thousands of tool calls over a large action space, requiring sustained planning, state monitoring, and execution under partial observability. The environment exposes 76 MCP tools and a narration layer that converts visual game state into structured text.   We use CivBench to characte...
  </details>

- **2026-09-02** — Patrick Bauer, Marius Schwinning, Melanie Siegel et al. — [Adapting a Foundation Model for Lunar Surface Height Estimation](http://arxiv.org/abs/2609.02448v1)
  <details><summary>📄 Abstract</summary>
  Digital elevation models (DEMs) can provide accurate height information, making it invaluable for analyzing the lunar surface. As the European Space Agency (ESA) prepares for future lunar missions that aim to land on the Moon, a precise method for height estimation will be essential for hazardous terrain that could endanger the landing approach. Traditional approaches to generate DEMs from imagery, such as shape from shading (SfS) and stereophotogrammetry (SPG) have been proven highly valuable f...
  </details>

- **2026-09-02** — Isabel D. Stein, Thijs A. Eker, Sebastiaan P. Snel et al. — [Domain shift-robust object detection with GenAI image editing](http://arxiv.org/abs/2609.02299v1)
  <details><summary>📄 Abstract</summary>
  Object detectors often degrade under domain shifts such as changes in lighting, weather, or occlusion. These shifts alter object appearance and expose a reliance on visual shortcuts learned from the training distribution that do not generalize across domains. Acquiring sufficient real-world samples to capture such domain variation is particularly difficult in specialized, low-data settings. Recent advances in diffusion-based generative image editing have shown promise for improving the in-domain...
  </details>

- **2026-09-02** — Yimeng Liu, Hua Huang — [WiP: Characterizing and Defending Against Mobile-Agent-Driven MFA Automation](http://arxiv.org/abs/2609.02154v1)
  <details><summary>📄 Abstract</summary>
  Mobile agents automate smartphone tasks by interpreting interfaces, interacting with apps, and coordinating cross-app workflows. This capability challenges the human-mediated separation assumed by passcode-based MFA, creating factor collapse: valid authentication factors are combined within one autonomous environment. Our modular pipeline com- pletes all 10 authorized MFA workflows, compared with 3/10 and 6/10 for two single-agent baselines. We also de- velop a motion-based Android risk signal t...
  </details>

- **2026-09-01** — Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner — [Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects](http://arxiv.org/abs/2609.01939v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agent runtimes execute tool actions that mutate databases, repositories, and cloud services across organizational boundaries. Authorization and local compensation cover pre-action admission and in-runtime rollback, but neither settles the residual harm left after a permitted action fails. We design Recourse, a smart-contract settlement protocol for compensable agent side effects that binds each admitted action to scope, recovery, evidence, payout, and collateral. Recourse separates ex...
  </details>

- **2026-09-01** — Soyoung Yoon, Boyi Liu, Yite Wang et al. — [ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research](http://arxiv.org/abs/2609.01870v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems have shown strong performance in domains with reliable verifiers such as coding, where multi-parallel candidate generation selected by a verifier is effective. However, such pipelines would not generalize to open-ended, long-horizon research tasks without a verifier. While majority voting or self-consistency is often used to reach consensus as a proxy verifier, parallel agents repeatedly explore the same evidence, while access to peers' partial findings cause search to conver...
  </details>

- **2026-09-01** — Zhixuan Liu, Zhichen Dong, Yuyu Fan et al. — [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](http://arxiv.org/abs/2609.01091v2)
  <details><summary>📄 Abstract</summary>
  Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficu...
  </details>

- **2026-09-01** — Xiaofang Yang, Ziqi Miao, Dianbo Sui et al. — [Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents](http://arxiv.org/abs/2609.01487v1)
  <details><summary>📄 Abstract</summary>
  Skill-augmented agents load reusable skills as persistent runtime context, improving task performance but also giving malicious skills a durable channel for steering future actions. Such skills may leak secrets, corrupt code, bypass approvals, or stage data for exfiltration only after a concrete user task and workspace state make the unsafe action appear useful. This makes pre-install vetting insufficient and calls for runtime, task-conditioned protection. We propose Defense-as-Skill, a defense ...
  </details>

- **2026-09-01** — Saastha Vasan, Hadjer Benkraouda, Jizhou Chen et al. — [A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing](http://arxiv.org/abs/2609.01174v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) is essential for defending mission-critical infrastructure, yet the process of transforming raw attack evidence into shareable CTI remains fragmented and understudied.   We conduct a literature survey of academic papers, organizing the CTI lifecycle into three stages: Threat Data Collection, CTI Generation and Sharing, and CTI Consumption. The first and third stages are well represented in the literature, whereas only a small number of papers address CTI Generatio...
  </details>

- **2026-09-01** — Rui Yang, Junjie Xu, Zhengyu Liu et al. — [SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems](http://arxiv.org/abs/2609.00595v1)
  <details><summary>📄 Abstract</summary>
  Safe agents can fail together. Multi-agent LLM systems (MAS) move information, state, decisions, and authority across principal boundaries, creating failures that local checks may miss. Without an execution-level view, a multi-agent setting can easily be mistaken for evidence of a genuinely multi-agent security effect. We thus systematize MAS security through an execution-centered analysis of 197 works, covering six interaction interfaces, four adversary positions, seven system-level risks, and ...
  </details>

- **2026-09-01** — Nivedita Bijlani, Mauricio Villarroel — [Trajectory Analysis of ECG Motif Dynamics in the Run-up to Sudden Cardiac Arrest](http://arxiv.org/abs/2609.01543v1)
  <details><summary>📄 Abstract</summary>
  Early warning signatures of sudden cardiac arrest (SCA) remain poorly characterised in long-duration ECG. We quantified pre-event changes in ECG morphology using a motif-based trajectory framework. Holter ECGs from 23 patients with annotated SCA were analysed over non-overlapping 10 s windows. Window-level motifs were extracted to quantify trajectories of instability, consistency, dispersion, heterogeneity, and personalised-baseline distance. Each trajectory was normalised to an early baseline u...
  </details>

- **2026-09-01** — Peiying Zhu, Sidi Chang — [When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation](http://arxiv.org/abs/2609.01519v1)
  <details><summary>📄 Abstract</summary>
  Interactive simulations increasingly evaluate policies in markets populated by language-model agents. Their outputs can look economic---prices, profits, consumer surplus, and welfare---without instantiating the behavior named in the claim. We audit this risk in a multi-turn buyer--seller testbed for configurable hotel transactions. An initial implementation reported welfare gains from two marketplace guardrails of +87.4, +35.0, and +28.8 across a Qwen2.5 1.5B--14B ladder. It also gave guarded an...
  </details>

- **2026-09-01** — Ruocan Wei — [TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution](http://arxiv.org/abs/2609.01428v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents based on the ReAct paradigm have demonstrated remarkable capabilities in tool use and task execution. However, ReAct suffers from a fundamental efficiency problem: every query triggers a complete reasoning loop from scratch, and similar queries repeat identical steps without leveraging historical experience. We propose TRIAGE,a three-level routing framework that reduces token consumption by reusing historical execution trajectories. Its core innovation is TaaS (...
  </details>

- **2026-09-01** — Mehrdad Shafiei Dizaji, Hoda Azari — [Predicting Subsurface Abnormalities Growth using Physics-Informed Neural Networks](http://arxiv.org/abs/2609.01417v1)
  <details><summary>📄 Abstract</summary>
  The research explores the pioneering integration of Physics-Informed Neural Networks (PINNs) into the domain of Ground-Penetrating Radar (GPR) data prediction. This research presents a detailed development framework for a specialized PINN model, proficient at interpreting and forecasting GPR data, much like how medical imaging models predict tumor behavior. By harnessing the synergy between deep learning algorithms and the physical laws governing subsurface structures or in medical terms, human ...
  </details>

- **2026-09-01** — Anuj Rathore, Kartick Sutradhar — [A Scalable Multi-Protocol Platform for Quantum Key Distribution Simulation with Rigorous Statistical Evaluation](http://arxiv.org/abs/2609.01297v1)
  <details><summary>📄 Abstract</summary>
  Quantum Key Distribution (QKD) offers information- theoretically secure key establishment grounded in the laws of quantum physics, yet its practical reach is limited by the prohibitive cost of photonic hardware and the fragmented nature of existing simulation tools. Most simulators support only a single protocol and report results from individual stochastic runs, making systematic protocol comparison and reproducible statistical inference difficult. This paper presents a unified QKD simulation p...
  </details>

- **2026-09-01** — Filipe Moura, Giordano Paoletti, Carlos H. G Ferreira et al. — [Don't You Know, Pump it Up! Investigating Cryptocurrency Manipulation in Telegram-Driven Activity](http://arxiv.org/abs/2609.01176v1)
  <details><summary>📄 Abstract</summary>
  Telegram plays a pivotal role in cryptocurrency communication and has been repeatedly associated with coordinated schemes, such as pump-and-dump manipulation. However, existing studies typically focus on known manipulation chats or a limited set of cryptocurrencies, leaving open the question of how Telegram is leveraged for mass promotional activity (shilling) at scale. Moving beyond these limitations, this work analyzes the interplay between information flows and market activity across public T...
  </details>

- **2026-09-01** — Guangqi Li, Yongxin Li — [Pre-carved Niches: The Formation Dynamics of Modular Task Partitions in Early LLM Training](http://arxiv.org/abs/2609.01170v1)
  <details><summary>📄 Abstract</summary>
  Large language models exhibit a modular internal organization that mirrors well-studied functional networks of the human brain, but how this organization forms during training is unknown: prior work has characterized finished models, not the formation process. We track formation step by step: we train a Pythia-410M model from scratch (two trajectories, bf16 and fp32) and run attribution patching at every step, alongside probes for gradient norms, effective updates, weight norms, and first-order ...
  </details>

- **2026-09-01** — Zhixuan Liu, Zhichen Dong, Yuyu Fan et al. — [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](http://arxiv.org/abs/2609.01091v1)
  <details><summary>📄 Abstract</summary>
  Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficu...
  </details>

- **2026-09-01** — Leonardo Ranaldi, Sherrie Shen, Jushi Kai et al. — [WorldBench: Culturally Grounded Benchmark for Multilingual Agents](http://arxiv.org/abs/2609.01056v1)
  <details><summary>📄 Abstract</summary>
  Despite the growing use of LLM-powered agents to solve multi-step tasks in complex environments, existing benchmarks rarely test state preservation, performance across languages, and application to realistic, grounded scenarios. To address these concerns, we present WorldBench: a comprehensive, multilingual benchmark of genuine, persona-grounded everyday workflows, where agents can act in a sandbox via structured actions. WorldBench comprises 1,600 tasks across seven languages and eight cultures...
  </details>

- **2026-09-01** — Molly Wang — [Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees](http://arxiv.org/abs/2609.01035v1)
  <details><summary>📄 Abstract</summary>
  Recursive LLM agents can broaden their search by spawning specialists. Some branches later request tools that send data or deploy code. When should a branch receive authority to act? We distinguish sandbox spawning, in which external controls prevent the specified harm, from capability activation, in which a selected branch crosses an irreversible-action boundary. Progressive Risk Vesting (PRV) holds a trajectory-level risk budget in escrow and debits it as branches are activated. We prove an an...
  </details>

- **2026-09-01** — Guowei Wang, Chaokun Yang, Zhenxuan Pan et al. — [AInfer-PD: Communication-Safe In-Place Prefill-Decode Multiplexing for Distributed MoE Rollouts](http://arxiv.org/abs/2609.00993v1)
  <details><summary>📄 Abstract</summary>
  Rollout inference often dominates the wall-clock time of large-scale reinforcement learning (RL). In agentic RL, each trajectory alternates between model generation and environment interaction over multiple turns. Asynchronous trajectories consequently introduce new prefill (P) work while other trajectories remain in decode (D), making P/D coexistence a persistent property of the rollout rather than a one-time prompt-ingestion event.   On shared accelerators, persistent P/D coexistence can make ...
  </details>

- **2026-09-01** — Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee et al. — [Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning](http://arxiv.org/abs/2609.00879v1)
  <details><summary>📄 Abstract</summary>
  Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework that integrates Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) within a unified data construction pipeline. From a single Human-in-the-Loop (HITL) annotation workflow, two comple...
  </details>

- **2026-09-01** — Yuri Son, Seunghee Kim, Hyuhng Joon Kim et al. — [A Unified Mechanistic Analysis of Knowledge- and Safety-Based Refusals](http://arxiv.org/abs/2609.00760v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly trained to decline queries that fall outside their knowledge (knowledge-based refusal, KR) or violate safety policies (safety-based refusal, SR). Although KR and SR result in superficially similar responses, they have largely been studied in isolation, leaving open whether they share an underlying mechanism. We address this gap with a systematic study on a new dataset of 213 contrastive quadruples that jointly probe both refusal types. We find that K...
  </details>

- **2026-09-01** — Elisei Rykov, Timur Ionov, Nikolay Ivanov et al. — [Enoki: Efficient Multi-Level Hallucination Detection](http://arxiv.org/abs/2609.00581v1)
  <details><summary>📄 Abstract</summary>
  Ensuring factuality remains a critical challenge for deploying LLMs in high-stakes settings. Existing hallucination detectors usually operate at a single level: claim-level methods provide interpretable factual units, while span-level methods localize unsupported text. Bridging these views is costly, as LLM-heavy pipelines require multiple decomposition and verification calls, and modular systems need additional claim-to-span alignment. We propose Enoki, an Open Information Extraction framework ...
  </details>

- **2026-09-01** — Sharon S. Musa, Fereshteh Forghani, Harrish Thasarathan et al. — [What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models](http://arxiv.org/abs/2609.01551v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers, and how they are geometrically organized. In this work, we tackle these three questions through a systematic layer-wise analysis of V-JEPA 2 and VideoMAE-v2. We leverage lightweight probes trained to discover three temporally grounded properties: (i) camera motion understanding, (ii) intuitive phy...
  </details>

- **2026-09-01** — Lucas Cunha, Lucas Sotomaior, Lucas Gasperin et al. — [Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation](http://arxiv.org/abs/2609.01511v1)
  <details><summary>📄 Abstract</summary>
  Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for face forgery detection using the Multi-Dimensional Face Forgery Image (MFFI) dataset and evaluates performance on both clean and degraded test partitions. We compare six model families, including convolutional networks, transformer-based models, and a frozen self-supervised DINOv3 backbone, across ...
  </details>

- **2026-09-01** — Egor Pakhomov, Erik Nijkamp — [Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers](http://arxiv.org/abs/2609.01466v1)
  <details><summary>📄 Abstract</summary>
  A long-horizon agent's trace outgrows both of its consumers: the human observer monitoring the run, and the agent itself, whose bounded context the trace must be folded back into. We present a live trace model, an append-only event ledger folded incrementally into typed run state and compiled into per-consumer views, and evaluate it for both consumers against deterministic ground truth. For the observer side, evaluated with an LLM reader as proxy, the compiled view answers monitoring questions u...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 73 papers

- **2026-09-03** — Ye-Chan Kim, Seunghee Choi, SeungJu Cha et al. — [Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning](http://arxiv.org/abs/2609.04183v1)
  <details><summary>📄 Abstract</summary>
  Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions lack visual grounding and are rigidly assigned to every inter-event gap at a fixed location and duration. To address these, we propose Seeing Before Synthesizing (SBS), a framework that adaptively provi...
  </details>

- **2026-09-03** — Yalun Wu, Junfeng Fang, Jiawei Wang et al. — [FLY-EVAL++: An Evidence-Driven Evaluation Protocol for Safety-Constrained Flight Prediction with Large Language Models](http://arxiv.org/abs/2609.04021v1)
  <details><summary>📄 Abstract</summary>
  Evaluating large language models (LLMs) in safety-critical, physics-governed environments requires more than accuracy-based metrics, because predictions that are numerically close to the ground truth can still violate operational constraints, combine fields in physically inconsistent ways, or fail to produce usable structured outputs. Existing evaluation protocols do not measure these failure modes reliably. We propose FLY-EVAL++, an evidence-driven evaluation protocol that combines deterministi...
  </details>

- **2026-09-03** — Sanyuan Chen, Min-Jae Hwang, Sho Inoue et al. — [Alignment-Free Text-Audiobox for Voice Dubbing and Full-Duplex Dialogue Synthesis](http://arxiv.org/abs/2609.03992v1)
  <details><summary>📄 Abstract</summary>
  We present Alignment-Free Text-Audiobox (Text-AB), a unified framework for high-quality voice dubbing and full-duplex dialogue synthesis. Building on a Diffusion Transformer trained with a flow-matching objective, Text-AB departs from the Audiobox system along three dimensions. First, it operates in a latent diffusion framework using DAC-VAE features that encode 48 kHz waveforms into a 25 Hz latent sequence, giving over 10x higher compression than previous EnCodec representations while improving...
  </details>

- **2026-09-03** —  Nazim-E-Alam, Tarek Rahman, Md Kishor Morol — [IchthyoNoma: Nomenclature and Context Sensitivity of Zero-Shot Biological Vision--Language Models for Bangladeshi Freshwater Fish Recognition](http://arxiv.org/abs/2609.03985v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot vision-language models (VLMs) are increasingly used as training-free species recognizers, but reported accuracy can reflect more than visual species knowledge. We audit CLIP, BioCLIP, BioCLIP2, and a multilingual Jina CLIP v2 control on seven freshwater-fish categories from two Bangladeshi sources (10,321 images). BioCLIP2 reaches 72.36% on BFF-15 with English common names and 68.91% on SylFishBD with scientific names, versus 25.15% and 14.40% for generic CLIP. BioCLIP2 Bengali prompts...
  </details>

- **2026-09-03** — Marco Cipriano, Leonardo Zini, Alexandra Schild et al. — [SVG-Score: Human-Aligned Evaluation of Text-to-SVG Generation](http://arxiv.org/abs/2609.03806v1)
  <details><summary>📄 Abstract</summary>
  Scalable Vector Graphics (SVG) generation is attracting increasing attention as generative models improve in expressiveness and controllability. Progress, however, is held back by the lack of domain-specific evaluation protocols: current practice relies on metrics designed for natural images, most notably CLIPScore, which was never trained on vector graphics and aligns only partially with human judgment. We introduce \textbf{\ours}, a human-aligned evaluation framework for text-to-SVG generation...
  </details>

- **2026-09-03** — SeyedMohammadAmin Nabi Pour, S. Gareth Pierce, Randika Vithanage et al. — [A comparative study on the accuracy & repeatability of mobile robotic platforms for the delivery of precision NDE measurement](http://arxiv.org/abs/2609.03794v1)
  <details><summary>📄 Abstract</summary>
  Mobile robotic platforms offer a flexible alternative to fixed manipulators for non-destructive evaluation (NDE) of large aerospace structures, but their base-positioning accuracy and how that accuracy should inform deployment have not been assessed under a common, externally referenced protocol. This work presents a laser tracker-based evaluation workflow (ground truth approximately 6 micrometers) that measures the static and segmented trajectory positioning accuracy of five commercial mobile p...
  </details>

- **2026-09-03** — Amey Karan, Rudra Dhar, Mohamed Soliman et al. — [Can LLMs Extract Architectural Design Decisions from Source Code Commits? - A Preliminary Exploratory Study](http://arxiv.org/abs/2609.03721v1)
  <details><summary>📄 Abstract</summary>
  Context: Architectural Design Decisions (ADDs) capture the rationale behind the structure and evolution of software systems but are rarely documented explicitly, and are often hidden inside source code commits. Recovering them is important for Architectural Knowledge Management (AKM). Problem: Extracting ADDs from commits is challenging due to their implicit and unstructured nature. Large Language Models (LLMs) have shown strong capabilities in understanding code and text, yet their effectivenes...
  </details>

- **2026-09-03** — Sobhan Asasi, Ozge Mercanoglu Sincan, Richard Bowden — [SignSeek: Learning Transferable Representations for Sign Dictionary Retrieval](http://arxiv.org/abs/2609.03695v1)
  <details><summary>📄 Abstract</summary>
  Sign language dictionaries are essential resources for sign language learners, yet automatically retrieving a sign from a dictionary, given only a query video, remains a challenging problem due to the natural variability between signers. Existing sign representation learning methods are built for closed-set recognition, producing embeddings that do not generalise to the open-set, signer-independent setting that retrieval demands. \textbf{SignSeek} closes this gap by contrastively learning sign r...
  </details>

- **2026-09-03** — Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung — [FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow](http://arxiv.org/abs/2609.03563v1)
  <details><summary>📄 Abstract</summary>
  We present FlashRender, a few-step generative rendering framework that retakes a source video along a target camera trajectory in seconds. We identify sampling-step-dependent camera control as a prominent manifestation of discretization error in existing multi-step generative rendering models and show that resolving this inconsistency substantially lowers denoising trajectory curvature, facilitating subsequent step distillation. To this end, we introduce Representation Transformation and Alignme...
  </details>

- **2026-09-03** — Caoyuan Ma, Tian Gu, Wenpu Liu et al. — [SafeRI: Recognition and Intervention for Token-Level Safety Intervention in Large Vision Language Models](http://arxiv.org/abs/2609.03544v1)
  <details><summary>📄 Abstract</summary>
  Existing safety alignment methods for vision-language models usually modify the model behavior globally: once the safety parameters are trained or loaded, they participate in both unsafe and already-safe generations. This always-on intervention can unnecessarily perturb the model's original reasoning path and degrade general multimodal capabilities. We argue that safety alignment should be an on-demand intervention rather than a permanent modification to every decoding trajectory. To this end, w...
  </details>

- **2026-09-03** — Yinan Liu, Hongtai Xia, Haoran Xu et al. — [NeoRed: A Knowledge-Logic-Alignment Multimodal Large Language Model for Neonatal Respiratory Disease Diagnosis](http://arxiv.org/abs/2609.03527v1)
  <details><summary>📄 Abstract</summary>
  Neonatal respiratory diseases are a major cause of neonatal morbidity and mortality, posing substantial challenges in clinical practice. Despite recent advances, existing Multimodal Large Language Models (MLLMs) face two key limitations in neonatal diagnosis: (1) domain gap arising from predominantly adult training data; (2) insufficient integration of multidimensional clinical context for accurate diagnosis. To address these challenges, we collect two real-world clinical datasets (NeoCXR and Ne...
  </details>

- **2026-09-03** — Karthika Nhayakkat, Rajat Verma, Maharaj Brahma et al. — [Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations](http://arxiv.org/abs/2609.03511v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) demonstrate strong multilingual reasoning performance, yet their robustness to semantics-preserving structural variation remains underexplored, particularly for relatively free word-order languages. We investigate the structural sensitivity of multilingual LLMs using two linguistically grounded perturbation settings in Hindi and Malayalam: constrained constituent reordering and active-passive voice transformation. We introduce a benchmark dataset IndicReStruct, with ...
  </details>

- **2026-09-03** — Quang Hoang Trung, Quang Huu Hieu, Nguyen Van Hoang Phuc et al. — [ALRA: Adaptive Local Relational Alignment for Logit-Based Pre-training Distillation of Autoregressive Language Models](http://arxiv.org/abs/2609.03355v1)
  <details><summary>📄 Abstract</summary>
  Logit-based knowledge distillation for autoregressive language models usually aligns teacher and student next-token distributions over the entire vocabulary. However, this global objective overlooks relative preferences among likely token alternatives. Existing local approaches often select candidate tokens from either the teacher or the student alone. Teacher-only selection can miss tokens that the student considers likely, while student-only selection can rely on an inaccurate ranking early in...
  </details>

- **2026-09-03** — Leqi Zheng, Jinbo Su, Fang Niu et al. — [Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards](http://arxiv.org/abs/2609.03342v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from verifiable rewards (RLVR) drives chain-of-thought reasoning in large language models, yet its binary outcome reward cannot distinguish among correct trajectories. Existing dense reward alternatives, from surface heuristics to process reward models, either ignore the expert solutions already present in training corpora or require expensive offline annotation. We propose Gradient-Aligned Reward (GAR), which operates in the policy's own gradient space: truncated backprop...
  </details>

- **2026-09-03** — Dun Li Chan, Emily Liu, Niyathi Allu et al. — [How Perturbations Propagate: A Multi-Level Analysis of Robustness in Large Language Models](http://arxiv.org/abs/2609.03322v1)
  <details><summary>📄 Abstract</summary>
  Language models encounter typos, corrupted text, altered words, and disrupted token order, yet robustness is usually evaluated only through output behavior. We study how six naturalistic and synthetic input perturbations propagate through decoder-only language models at three levels: output behavior, hidden-state geometry, and attention-head function. We evaluate behavioral effects across four GPT-2 and two Qwen2.5 checkpoints by analyzing layerwise geometry using centered kernel alignment and i...
  </details>

- **2026-09-03** — Longfeng Wu, Tong Zeng, Giovanni Seni et al. — [HypRQ-VAE: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender Systems](http://arxiv.org/abs/2609.03369v1)
  <details><summary>📄 Abstract</summary>
  Sequential recommender systems model user behavior as item ID sequences, while recent generative methods cast recommendation as a language modeling task using large language models (LLMs). While this paradigm incorporates rich textual semantics, it introduces a fundamental mismatch: LLMs operate on text tokens, whereas recommender systems depend on discrete item indices. This misalignment often leads to hallucinations in generative recommendations. Existing methods attempt to bridge this gap by ...
  </details>

- **2026-09-02** — Heejin Do, Jakub Kontak, Mrinmaya Sachan — [SWIM: Student Writing Simulation via Proficiency-Conditioned Generation](http://arxiv.org/abs/2609.03215v1)
  <details><summary>📄 Abstract</summary>
  Writing proficiency manifests in how students develop content, organize ideas, choose words, and use language. Despite growing interest in LLM-based student simulation, whether LLMs can reproduce such multidimensional variation in extended writing remains largely unexplored. In this work, we explore if language models can realistically simulate student writing, and introduce SWIM, a task that formulates Student Writing sIMulation as proficiency-conditioned essay generation. We evaluate prompting...
  </details>

- **2026-09-02** — Alejandro Barón García, Feng Wang, Emilia Garcia Casademont et al. — [Jina-OCR-v1: Efficient Document Parsing with Speculative Decoding and Dense Verifiable Rewards](http://arxiv.org/abs/2609.03181v1)
  <details><summary>📄 Abstract</summary>
  We present Jina-OCR-v1, an end-to-end document parsing model built to serve on low-budget GPUs. It combines the compressed-vision encoder and the 3B mixture-of-experts decoder of DeepSeek-OCR, which activates about 570M parameters per token, with a FastMTP speculative decoding head that shares a single draft block recursively across K=3 prediction steps. Greedy verification makes decoding lossless. Post-training combines instruction alignment, robustness fine-tuning on difficult documents, and G...
  </details>

- **2026-09-02** — Elliot Murphy — [No country for old linguists: LLM-brain alignment underdetermines neural computation](http://arxiv.org/abs/2609.03160v1)
  <details><summary>📄 Abstract</summary>
  Nastase et al. (2026) argue that large language models (LLMs) may illuminate language processing because both rely on distributed, context-sensitive representations shaped by statistical learning. Their rejection of simple cortical "boxology" is persuasive, and they articulate a strong case for the value of LLM-brain alignment research. The key question is what kind of inference LLM-brain alignment licenses. My claim here will be narrow: representational alignment can in principle constrain mech...
  </details>

- **2026-09-02** — Yutong Liu, Nan Huang, Xu Cao et al. — [Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](http://arxiv.org/abs/2609.02864v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introdu...
  </details>

- **2026-09-02** — Zihao Lu, Radu Timofte, Marcos V. Conde — [Benchmarking RAW and RGB Restoration in Image Signal Processors](http://arxiv.org/abs/2609.02831v1)
  <details><summary>📄 Abstract</summary>
  Modern cameras transform RAW sensor measurements into sRGB images through an image signal processor (ISP). We benchmark two placements for blind restoration around a fixed ISP: (A) pre-ISP restoration in the RAW domain and (B) post-ISP restoration in the sRGB domain. The benchmark covers four smartphone device groups, two learned ISPs, three degradation regimes--noise, blur, and joint noise and blur--, and several representative RAW and RGB restoration models. Our results show that placement alo...
  </details>

- **2026-09-02** — Hao Zhou, Mandar Kulkarni, Hao Chen et al. — [Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis](http://arxiv.org/abs/2609.02805v1)
  <details><summary>📄 Abstract</summary>
  Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer dependencies. While large language models (LLMs) offer promising capabilities for reasoning and knowledge integration, directly applying vanilla LLMs to telecom RCA often leads to hallucination, unstable reasoning, and poor alignment with structured network evidence. This work first reviews the evo...
  </details>

- **2026-09-02** — Giovanni Dispoto, Marcello Restelli, Carmine Ventre — [Eliciting ESG Preferences for Reinforcement Learning-Based Portfolio Optimization](http://arxiv.org/abs/2609.02677v1)
  <details><summary>📄 Abstract</summary>
  Modern portfolio management increasingly demands a balance between traditional risk-adjusted returns and strict Environmental, Social, and Governance (ESG) mandates. Current Reinforcement Learning (RL) approaches typically optimize for a single ESG provider, neglecting the significant divergence in rating methodologies across the industry and the unintuitive nature of manually weighting conflicting objectives. This paper addresses these limitations by formulating ESG-aware portfolio optimization...
  </details>

- **2026-09-02** — Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran — [Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](http://arxiv.org/abs/2609.02664v1)
  <details><summary>📄 Abstract</summary>
  Recent 4D Gaussian representation frameworks have demonstrated strong performance in language-guided dynamic scene understanding. However, these methods remain highly sensitive to verbose and narrative-style queries that contain noisy contextual information. In this paper, we investigate the impact of query rewriting for complex object segmentation in 4D Gaussian representations. Inspired by recent findings in retrieval-augmented language models and keyword-guided query reformulation, we propose...
  </details>

- **2026-09-02** — Kenichi Fujita, Yusuke Ijima — [Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction](http://arxiv.org/abs/2609.02623v1)
  <details><summary>📄 Abstract</summary>
  Voice actors often re-read the same script while modifying their delivery in response to performance directions. We study this setting as direction-following TTS, where a system generates a new utterance that reflects a given direction relative to a reference utterance while preserving speaker identity and linguistic content. A key challenge is the lack of training data capturing such relative modifications. To address this, we propose a scalable pseudo-triplet construction pipeline that generat...
  </details>

- **2026-09-02** — Xingzu Zhan, Lin Gu, Ruogu Fang — [AffectDelta: Beyond Emotion Labels for Image Editing](http://arxiv.org/abs/2609.02616v1)
  <details><summary>📄 Abstract</summary>
  Emotion-driven image editing aims to evoke a specified target emotion by modifying emotion-relevant visual cues in a source image, while preserving the overall composition and semantic-structural coherence of the original scene. Existing scene-level editors typically specify the target with a single emotion category and often learn visual transformations from operation-level text instructions. A category collapses a mixed affective endpoint into one dominant label, while language cannot precisel...
  </details>

- **2026-09-02** — Pawel Struski, Jakub Swistak, Inez Okulska et al. — [Competitive Market Behavior of LLMs](http://arxiv.org/abs/2609.02580v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as economic agents, yet there is little evidence whether LLM agents are suited for participating in market mechanisms designed for humans, and whether these mechanisms deliver desired outcomes when faced with LLM agents. We address this question by replicating seminal economic experiments, replacing human subjects with LLM agents. We place agents in a double auction environment, which is a widely-used market mechanism. We check whether such ...
  </details>

- **2026-09-02** — Leon Fröhling, Jens Rupprecht, Markus Strohmaier et al. — [When Persona Attributes Improve Population Alignment in Large Language Models](http://arxiv.org/abs/2609.02526v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to predict the responses of human participants in survey panels. Towards that goal, persona prompting has recently emerged as a technique to inform and align large pretrained language models. Persona prompting refers to the practice of using short textual descriptions of 'personas' in prompts to steer the LLM's generations. Personas describe individuals through different attributes such as their socio-demographics, attitudes, or behaviors, with ...
  </details>

- **2026-09-02** — Cristina Pignotti, Yu-Qing Wang — [Exponential Consensus and Flocking in Multi-Agent Systems with Infinite Fading Memory](http://arxiv.org/abs/2609.02454v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study the emergent collective dynamics of multi-agent systems driven by infinite distributed fading memory of Volterra type. We establish a unified theoretical framework covering both first-order opinion consensus dynamics and second-order velocity alignment flocking kinematics. By introducing Dafermos past-history transformations, the governing integro-differential systems are reformulated into dynamical systems on an extended product Hilbert spaces. For first-order dynamics, ...
  </details>

- **2026-09-02** — Juntao Wei, Yangming Zhou, Zhibin Jiang et al. — [LLM-Driven Joint Evolution of Coupled Heuristics Components for Routing Optimization](http://arxiv.org/abs/2609.02353v1)
  <details><summary>📄 Abstract</summary>
  Heuristic design for combinatorial optimization remains heavily reliant on expert knowledge, while existing large language model (LLM)-enhanced evolutionary methods typically evolve isolated algorithmic components, even when one determines the search state on which another operates. This paper proposes LLM-driven Heuristic Components Joint Generation (LLM-HCJG), a population-based framework that jointly generates and co-evolves interdependent heuristic components under a shared design blueprint....
  </details>

- **2026-09-02** — Zhao Ji, Wenqing Chen, Zhixuan Chu et al. — [SALA: Semantic-Aware Logical Alignment for Complex Reasoning in In-Context Learning](http://arxiv.org/abs/2609.02336v1)
  <details><summary>📄 Abstract</summary>
  Effective in-context learning (ICL) for complex reasoning relies on selecting the right demonstrations. Traditional retrieval methods based on surface similarity fail to capture the underlying problem-solving logic. Recent logic-based methods address this by matching predefined reasoning steps, but the rigid rules and exact-match criteria is improper to handle flexible or diverse reasoning processes. To address the problem, we propose SALA, a Semantic-Aware Logical Alignment framework. Instead o...
  </details>

- **2026-09-02** — Quansheng Hu, Qin Sun, Qiansen Dai et al. — [YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification](http://arxiv.org/abs/2609.02318v1)
  <details><summary>📄 Abstract</summary>
  Referring multi-object tracking (RMOT) aims to track every instance in a video that matches a given language expression. Despite the recent integration of multimodal large language models (MLLMs) to enhance generalization, existing methods predominantly relegate them to the role of caption generators, necessitating external modules for final decision-making. This paradigm not only introduces extra latency but also severely underutilizes the inherent vision-language alignment capabilities of MLLM...
  </details>

- **2026-09-02** — Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera et al. — [Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds](http://arxiv.org/abs/2609.02302v1)
  <details><summary>📄 Abstract</summary>
  A core obstacle to alignment evaluation is evaluation awareness: capable models can tell when they are being tested rather than deployed, weakening the conclusions a safety evaluation can support. We present two techniques that make simulated alignment evaluations harder to distinguish from real deployments. Our first technique, critique refinement, spends additional inference-time compute on each simulator action: the simulator generates multiple candidate actions, refines them using feedback f...
  </details>

- **2026-09-02** — Jie Ding, Rui Sun, Xinyuan Zhang et al. — [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](http://arxiv.org/abs/2609.02253v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning. Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-making, or distill procedural skills that remain decoupled from downstream policy adaptation. We propose APEx, a hierarchical experience utilization framework that organizes interaction history into in...
  </details>

- **2026-09-02** — Fan Yuxuan, Huang Miaojun, Zhang Haimei et al. — [PhoenixNest-Video: Evidence-Grounded Multimodal Agent Framework for Automated Video Interview Assessment](http://arxiv.org/abs/2609.02231v1)
  <details><summary>📄 Abstract</summary>
  Interview assessment requires per-criterion judgments grounded in behavioral evidence, yet surging applicant volumes have made human-only evaluation costly and inconsistent, while existing AI approaches yield opaque scores without traceable rationale. We introduce PhoenixNest-Video, an evidence-grounded multimodal agent framework for automated video interview assessment. It builds a semantic video graph as structured working memory, performs rubric-conditioned retrieval with cross-modal verifica...
  </details>

- **2026-09-02** — Ziqi Zhang, Emmanuele Chersoni, Mohammad Momenian — [Do Cantonese-Adapted Language Models Better Predict Cantonese Reading? A Cross-Model Eye-Tracking Evaluation](http://arxiv.org/abs/2609.02163v1)
  <details><summary>📄 Abstract</summary>
  Information-theoretic measures derived from autoregressive language models are widely used to characterize the expectations that shape human reading, but whether language-variety-specific training improves such psycholinguistic alignment remains unclear. This question is still open for Cantonese, where recent NLP evaluations reported mixed benefits from Cantonese-specific training relative to Mandarin-oriented or general-purpose models. Using naturalistic Cantonese eye-tracking data, we compare ...
  </details>

- **2026-09-02** — Hanyang Cao, Yuetong Fang, Taesoo Kwon et al. — [Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence](http://arxiv.org/abs/2609.02134v1)
  <details><summary>📄 Abstract</summary>
  Humanoid learning increasingly relies on transforming vast and diverse human motion data into high-quality robot reference trajectories. However, retargeting human motion to humanoid robots is challenging due to substantial differences in morphology, degrees of freedom, joint ranges, and kinematic constraints between humans and robots. Existing retargeting methods typically address these differences by defining human-robot correspondence through hand-crafted sparse keypoints or body-part pairs. ...
  </details>

- **2026-09-02** — Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra — [A Tri-Agent Framework for Evaluating and Aligning Question Clarification Capabilities of Large Language Models](http://arxiv.org/abs/2609.02054v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in interactive systems where understanding user intent precisely is paramount. A key capability for such systems is effective question clarification, especially when user queries are ambiguous or underspecified. This paper introduces a novel tri-agent framework for the robust evaluation of an LLM's ability to engage in clarifying dialogue. Our framework comprises three distinct LLM-based agents: (1) a Question Clarifying Agent (QCA), the sys...
  </details>

- **2026-09-02** — Ziyue Piao, Isabelle Cossette, Marcelo M. Wanderley — [Reconciling Kinesthetic Mismatches: A Somatic Alignment Mindset for Musical Body Transformation](http://arxiv.org/abs/2609.01981v1)
  <details><summary>📄 Abstract</summary>
  Mastering musical performance requires precise multisensory coordination, yet learners encounter a kinesthetic mismatch, which is a discrepancy between the internal perception of an action and the actual physiological state of the body. While multisensory Body Transformation Experiences (BTE) provide tools to bridge this gap, existing designs often focus on external correction rather than internal alignment. To address this, we propose the Somatic Alignment Mindset (SAM), a conceptual lens that ...
  </details>

- **2026-09-01** — You-Lin Chen, Kyoungjun Park, Bin Xu et al. — [MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation](http://arxiv.org/abs/2609.01913v1)
  <details><summary>📄 Abstract</summary>
  In product entity resolution, relationship definitions constantly evolve with business needs, yet adapting to each change traditionally requires slow, costly human annotation that is often noisy and carries no reasoning. Large vision-language models (VLMs) prompted zero-shot can adapt to a new definition immediately and supply the reasoning that human labels lack, but their cost and latency are prohibitive at production scale. We present MERGED, a distillation framework that transfers not just l...
  </details>

- **2026-09-01** — Judita Preiss, Yunhan Yang — [Guiding LLM Peer Reviewers: The Impact of Score Anchors on Review Evidence and Accuracy](http://arxiv.org/abs/2609.01905v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for research quality evaluation, with prior work exploring their scoring accuracy and the plausibility of review rationales. However, less is known about whether external score guidance changes the evidence presented in the generated review as well as the final score. This study uses 98 Allied Health Professions research outputs submitted for internal REF-style assessment, with specialist human review reports and adjudicated 1-4 reference scores...
  </details>

- **2026-09-01** — Yalda Daryani, Miranda Bogen, Madeleine I. G. Daepp — [Accurate in space, unreliable in time: how LLMs represent national cultural change](http://arxiv.org/abs/2609.01902v1)
  <details><summary>📄 Abstract</summary>
  Assessments of cultural alignment have become an important part of the development and improvement of large language models (LLMs). However, the majority of the evaluations treat culture as a single snapshot, investigating only whether a model represents a society accurately at the current time. Research in cultural psychology shows that cultural values change at different rates and directions over time. Therefore, a "culturally aware" model should capture not only where a culture is today but a...
  </details>

- **2026-09-01** — Weiming Li, Catarina Barata, Miguel Constante et al. — [Candidate Generation and Definition-Guided Verification for Sentence-Level Depression Symptom Recognition](http://arxiv.org/abs/2609.01833v1)
  <details><summary>📄 Abstract</summary>
  Sentence-level recognition of depression symptoms is challenging because similar expressions can differ in symptom relevance, and language-model inference is insufficiently grounded in diagnostic definitions. This study proposes a two-stage framework separating symptom-candidate generation from definition-grounded verification. A contrastively fine-tuned sentence encoder generates a symptom candidate per sentence, and a fine-tuned language model verifies whether the candidate is present or absen...
  </details>

- **2026-09-01** — Hatim Chergui, Carolina Fernández-Martínez, Mehdi Bennis et al. — [Agents That Model Agents: Five Principles Toward a Theory of Mind for 6G Networks](http://arxiv.org/abs/2609.01779v1)
  <details><summary>📄 Abstract</summary>
  Future 6G networks will rely on Large Language Model (LLM) agents to manage the Radio Access Network (RAN). However, current architectures assume inter-agent messages convey objective facts. A message is instead a \emph{trace} of the sender's reasoning: it carries a subjective conclusion, so a syntactically valid report can propagate an AI hallucination and trigger a cascading outage invisible to protocol validation. Reading such a trace requires a Theory of Mind (ToM)---before acting, the recei...
  </details>

- **2026-09-01** — Aarthy Nagarajan — [Slow-Fast Brain-Computer Interfaces: Preventing Neuroadaptive Overfitting in AI-Mediated Neural Interfaces](http://arxiv.org/abs/2609.01767v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is transforming brain-computer interfaces (BCIs) from task-specific neural decoders into adaptive systems that complete language, smooth movement, regulate rehabilitation support and adjust stimulation. These capabilities can increase speed, fluency, usability and clinical reach, yet conventional performance metrics may overlook losses in intent fidelity, authorship, agency, therapeutic challenge and durable clinical benefit. I define neuroadaptive overfitting as a c...
  </details>

- **2026-09-01** — Jianzhong You, Yuan Gao, Chris McIntosh — [AlphaRAD: Grounded Zero-Shot Classification in Chest Radiology via $α$-Corrected Binary Cross Entropy and Factorized Latent Supervision](http://arxiv.org/abs/2609.01757v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Pretrained Models (VLPMs) offer a scalable path to open-vocabulary chest radiology understanding, yet two aspects remain underexplored: how structured clinical semantics extracted from medical reports can reduce in-batch noise during contrastive learning, and how cross-modal fusion can be designed to produce more faithful spatial grounding without added complexity. We introduce AlphaRAD, addressing these opportunities through two contributions. First, we construct a large-scale s...
  </details>

- **2026-09-01** — Seungwoo Jung, Dohyeok Kwon, Seungmin Cha et al. — [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](http://arxiv.org/abs/2609.00575v2)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) architectures scale large language models efficiently, but they demand massive GPU memory. To cope with such demand, models are commonly compressed to reduce their memory footprint. Residual sparsification is a representative compression technique that decomposes each projection matrix of an expert into a shared base matrix and per-expert residual matrix, and then compresses the residuals. Existing sparsification methods compress each residual matrix independently by min...
  </details>

- **2026-09-01** — Yitong Guo, Xiaoyi Chen, Siyuan Zhang et al. — [When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning](http://arxiv.org/abs/2609.01455v1)
  <details><summary>📄 Abstract</summary>
  Benign fine-tuning severely weakens the safety alignment of large language models (LLMs), so we study why refusal behavior is so fragile. While prior work often attributes this failure to gradient conflict, we propose a fundamentally different Fisher-geometric explanation: safety Fisher is low-rank, and alignment makes the safety geometry flatter while preserving an output-routing pathway. After 100 benign fine-tuning examples, this pathway is selectively re-sharpened in output-side MLP modules,...
  </details>

- **2026-09-01** — Dirk Bergemann, Andrew Koh, Stephen Morris — [Mechanism Design for Alignment and Control](http://arxiv.org/abs/2609.01595v1)
  <details><summary>📄 Abstract</summary>
  We develop a framework for mechanism design with AI agents whose alignment (preferences) and capabilities (feasible actions and information) are unknown. We want such agents to act on our behalf so mechanisms must incentivize both honesty and obedience. A one-sided imitation structure---capabilities can be concealed but not counterfeited---yields a revelation principle, a characterization of implementable policies via nested cyclical monotonicity, and conditions under which eliciting higher-orde...
  </details>

- **2026-09-01** — Jing Xiao, Xinhai Chen, Qinglin Wang et al. — [Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks](http://arxiv.org/abs/2609.01558v1)
  <details><summary>📄 Abstract</summary>
  Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery methods mitigate this issue by constructing directions from loss-specific gradients to reduce conflict before optimizer transformation. However, even when the constructed direction is conflict-free, this property may not be preserved after optimizer transformation. Let $a_t$ denote the direction constr...
  </details>

- **2026-09-01** — Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu et al. — [TempCloze: Can Video-LLMs Identify the Missing Middle?](http://arxiv.org/abs/2609.01515v1)
  <details><summary>📄 Abstract</summary>
  Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly...
  </details>

- **2026-09-01** — Thibaut Thonet, Jos Rozen, Laurent Besacier — [Ready to Speak: Aligning LLMs for TTS-Friendly Text Generation](http://arxiv.org/abs/2609.01246v1)
  <details><summary>📄 Abstract</summary>
  Current Large Language Models (LLMs) are primarily optimized for written text, often producing outputs that are grammatically correct and helpful yet poorly suited for spoken delivery via Text-to-Speech (TTS). In this work, we study how to make LLMs natively generate TTS-friendly text, which we frame as a preference alignment problem: instead of relying on downstream rewriting modules, we directly align LLMs to generate text optimized for spoken delivery. We introduce two preference datasets spa...
  </details>

- **2026-09-01** — Frederic Sadrieh, Michal Štefánik — [Prompt-Robust Language Models: Which Training Strategies Work?](http://arxiv.org/abs/2609.01217v1)
  <details><summary>📄 Abstract</summary>
  Despite their strong performance, large language models remain highly sensitive to prompt formulation. Prior work addresses this through refined data construction or through dedicated robustness objectives. We reproduce and compare these strategies under controlled conditions, and measure how effective they are in addressing models' prompt sensitivity. We find the current robustness fine-tuning methods improve over standard fine-tuning and in-context learning, but the best-to-worst prompt gap re...
  </details>

- **2026-09-01** — Francois Meyer — [Subword Segmental BabyLMs: Learning to Tokenise for Sample-Efficient Pretraining](http://arxiv.org/abs/2609.01151v1)
  <details><summary>📄 Abstract</summary>
  In the standard LM training pipeline, subword tokenisation is applied as a preprocessing step. Subword segmental language modelling is an alternative paradigm in which tokenisation is learned during training, allowing the model to discover subword units that optimise its training objective. In this paper, we present our submission to the 2026 BabyLM Challenge, for which we develop two new subword segmental LMs: SubSegGPT and SubSegDeBERTa. SubSegGPT is a decoder-only model that learns tokenisati...
  </details>

- **2026-09-01** — Chujie Qin, Zilong Zhang, Zewei Chang et al. — [Dotting the Eye: An Intent-Driven Image Retouching Agent for Visual Focus Enhancement](http://arxiv.org/abs/2609.01148v1)
  <details><summary>📄 Abstract</summary>
  Image retouching is commonly formulated as enhancing overall visual quality through color adjustment, but in practice, it also serves to emphasize visual focus by guiding viewers' attention toward a specific subject or region. Achieving such focus-oriented retouching is inherently challenging, as it requires well-coordinated global and local adjustments to manipulate perceptual saliency while maintaining visual naturalness. This intricate process typically demands substantial professional expert...
  </details>

- **2026-09-01** — Jiming Feng, Junliang Li — [Scaled Idempotence in Transformer Attention: Paired OV Geometry and Shared-Value Algebras](http://arxiv.org/abs/2609.01129v1)
  <details><summary>📄 Abstract</summary>
  We identify a recurrent algebraic regularity in Transformer attention: a sparse subset of effective OV operators $T=OV^\top$ nearly closes under composition, $T^2\approxαT$. Across six pretrained endpoints spanning 2.8B--235B parameters, 3.98--8.00% of heads reach squared closure alignment $\mathcal{P}\geq0.9$, while no matched within-layer O/V mismatch does. An exact principal-coordinate factorization, $T=Q_OKQ_V^\top$ and $T^2=Q_O(KDK)Q_V^\top$, separates within-support transport from read--wr...
  </details>

- **2026-09-01** — Mustafa Yasir Altunhan, Hüseyin Özgür Kamalı, Eray Tüzün — [Fine-Tuning Large Language Models to Classify Pull Request-Issue Alignments: Going Beyond Prompting](http://arxiv.org/abs/2609.01087v1)
  <details><summary>📄 Abstract</summary>
  Context: Accurate alignment between pull requests (PRs) and corresponding issues is crucial for efficient software development and maintaining code quality, as misalignments can reduce traceability, hinder defect localization, and decrease maintainability.   Objective: This study aims to improve automated PR-issue alignment classification by leveraging fine-tuned large language models (LLMs) across multiple alignment categories, and conducts interpretability analysis to investigate the effects o...
  </details>

- **2026-09-01** — Sebastian Steindl, Nikos Voskarides, Alberto Gasparin et al. — [Post-hoc Alignment of LLM-judges to Human Judgment Distribution](http://arxiv.org/abs/2609.01073v1)
  <details><summary>📄 Abstract</summary>
  The LLM-as-a-judge (LLMaJ) framework offers a cost-effective and reproducible solution for automatic evaluation. However, current evaluation practices typically compare LLMaJ judgments against aggregated ground-truth labels, overlooking the valuable information contained in Human Label Variation (HLV). Inspired by an increasing line of work that proposes to leverage HLV, we systematically study LLMaJ performance on predicting both a single, aggregated ground truth hard-label and unaggregated sof...
  </details>

- **2026-09-01** — Ziyad Benomar, Weronika Łajewska, Leonardo Perelli et al. — [Data-Driven Persona-Conditioned Agents for A/B Test Simulation](http://arxiv.org/abs/2609.01038v1)
  <details><summary>📄 Abstract</summary>
  A/B testing is the gold standard for evaluating product changes, but each experiment requires real user traffic, engineering effort, and weeks of measurement. We propose a simulation framework that predicts A/B test outcomes using LLM-powered agents conditioned on data-driven personas grounded in real user behavioral signals. Unlike prior work that relies on synthetic or rule-based personas, our agents are constructed from anonymized behavioral data-activity patterns, engagement signals, and inf...
  </details>

- **2026-09-01** — Aravindhan Srinivasan, Marcello Ortaggio — [Charging higher-dimensional spacetimes with a generalized Kerr-Schild transformation](http://arxiv.org/abs/2609.01012v1)
  <details><summary>📄 Abstract</summary>
  We explore the construction of higher-dimensional Einstein-Maxwell(-Chern-Simons) solutions from vacuum seeds by means of a generalized Kerr-Schild transformation along a geodesic null vector field $\mathbf{k}$. Assuming the vector potential $\mathbf{A}$ to be aligned with $\mathbf{k}$, and $\mathbf{k}$ to be a Weyl aligned null direction satisfying the ``optical constraint'', we arrive at three distinct branches of solutions. If $\mathbf{k}$ is expanding and twisting, then its shear must vanish...
  </details>

- **2026-09-01** — Rania Elbadry, Ahmed Heakl, Saeed Almheiri et al. — [Right Frame, Wrong Rule: Cultural Cues Expose the Financial Knowledge Gap They Were Meant to Close](http://arxiv.org/abs/2609.00999v1)
  <details><summary>📄 Abstract</summary>
  When a question has valid answers under different normative frameworks, a language model must decide which framework to use and whether it can answer correctly within it. We call this setting normative pluralism and study it in Islamic finance using a four-choice taxonomy that separates framework selection from within-framework correctness. This separation reveals the stereotype trap: a cultural cue steers a model toward one framework, but the model selects an incorrect answer within that framew...
  </details>

- **2026-09-01** —  TGR Team, Lei Cheng, Haonan Hu et al. — [TGR: Advancing Industrial Recommendation from Generative-Paradigm Ranking toward Unified Generation and Reasoning](http://arxiv.org/abs/2609.00986v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems typically rely on cascaded retrieval, pre-ranking, ranking, and reranking stages, whose separately optimized models limit scaling, fragment decision making, and lack semantic knowledge and reasoning. We present TGR (Tencent Generative Recommendation), an industrial framework that advances recommendation toward the generative paradigm along three coupled directions. TGR-GenRank upgrades ranking through CCFormer, which combines unified feature tokenization, a scalabl...
  </details>

- **2026-09-01** — Jeonghyeok Do, Seungchul Lee, Munchurl Kim — [ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation](http://arxiv.org/abs/2609.00968v1)
  <details><summary>📄 Abstract</summary>
  SAR-to-EO image translation aims to generate electro-optical (EO) imagery from synthetic aperture radar (SAR) observations. Existing latent diffusion approaches typically inherit a predetermined autoencoder, although reconstruction fidelity can vary substantially across codecs and modalities. Because the latent codec affects the round-trip preservation of both SAR conditions and EO targets, codec selection constitutes a fundamental design choice; nevertheless, existing methods largely rely on co...
  </details>

- **2026-09-01** — Zhixin Wang, Chengzheyi Yao, Leyuan Liu et al. — [VerNav: Verifier-First Low-Latency Vision-and-Language Navigation](http://arxiv.org/abs/2609.00920v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) requires an agent to navigate through unseen 3D environments according to natural-language instructions. Explicit reasoning can improve instruction understanding and semantic grounding, but autoregressive generation at every step accumulates large decision-stage latency over multi-step navigation. We propose VerNav, a verifier-first framework for low-latency LLM-based VLN. The verifier reduces decision-stage latency by replacing per-step autoregressive genera...
  </details>

- **2026-09-01** — Zhiyu Ye, Yue Sun, Limiao Zou et al. — [A multicenter benchmark and clinically structured metric for coronary CTA report generation](http://arxiv.org/abs/2609.00909v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of automated coronary computed tomography angiography (CCTA) report generation requires standardized multicentre benchmarks and clinically structured metrics. We established a four-centre benchmark comprising 3,021 CCTA series from 818 patient-report pairs to evaluate seven open-source three-dimensional vision-language models. We developed CSM$_{\text{CCTA}}$, a clinically structured metric for CCTA report evaluation, with patient-, vessel-, and segment-level variables define...
  </details>

- **2026-09-01** — Guanqiao Chen, Di Wang, Lijie Hu — [SFAD: Speculative Factuality-Aware Decoding](http://arxiv.org/abs/2609.00796v1)
  <details><summary>📄 Abstract</summary>
  As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications. This task is particularly challenging as it requires balancing factual consistency with generation efficiency. Contrastive decoding methods require dual forward passes (with and without context) to compare model outputs, doubling inference computational overhead, while post-training alignment demands extensive reinforcement learning w...
  </details>

- **2026-09-01** — Zeen Zhu, Zhuo Li, Weiyang Guo et al. — [Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time](http://arxiv.org/abs/2609.00624v1)
  <details><summary>📄 Abstract</summary>
  A prominent paradigm in inference-time alignment employs lightweight supervisors to steer Large Language Models (LLMs). Through empirical analysis, we identify a structural mismatch in this paradigm: weak supervisors exhibit pervasive high entropy across the vast majority of tokens, yet prevailing dense intervention approaches mandate supervision at every decoding step. This leads to frequent low-confidence interventions that can disrupt valid base-model reasoning and incur substantial utility c...
  </details>

- **2026-09-01** — Pranshav Gajjar, Vijay K Shah — [CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN](http://arxiv.org/abs/2609.00590v1)
  <details><summary>📄 Abstract</summary>
  The next generation of mobile networks is envisioned as fully AI-native, with AI-RAN architectures embedding small language models (SLMs) to perform reasoning over real-time telemetry. The state-of-the-art training paradigms for telecom LLMs, exemplified by RANSTRUCT-style supervised fine-tuning (SFT) on curated instruction data, are limited to post hoc rationalization. Here, the explanations, when produced at all, are generated after or independently of the decision, leaving the decision proces...
  </details>

- **2026-09-01** — Cris Huynh — [Consistency Without Alignment: Item-Sensitive Language Models Indistinguishable From Random](http://arxiv.org/abs/2609.00576v1)
  <details><summary>📄 Abstract</summary>
  Item-sensitivity, defined as whether a model's choice depends on the specific input rather than on its own output prior, is widely reported as evidence of task competence. We show this evidence is necessary but not sufficient using a forced-choice signalling task abstracted from the board game Deception: Murder in Hong Kong. In this environment, the reference points against which a coordinate should be judged (a fit-maximising strategy, a posterior-maximising strategy, and uniform random selecti...
  </details>

- **2026-09-01** — Seungwoo Jung, Dohyeok Kwon, Seungmin Cha et al. — [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](http://arxiv.org/abs/2609.00575v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) architectures scale large language models efficiently, but they demand massive GPU memory. To cope with such demand, models are commonly compressed to reduce their memory footprint. Residual sparsification is a representative compression technique that decomposes each projection matrix of an expert into a shared base matrix and per-expert residual matrix, and then compresses the residuals. Existing sparsification methods compress each residual matrix independently by min...
  </details>

- **2026-09-01** — Jingshen Zhang, Shaoyang Xu, Wenxuan Zhang — [Aligned but Flattened: Analyzing the Trade-off between Cultural Alignment and Diversity in LLMs](http://arxiv.org/abs/2609.00565v1)
  <details><summary>📄 Abstract</summary>
  Cultural fine-tuning has become the de facto paradigm for building culture-aware large language models (LLMs), yet existing optimization exclusively for alignment scores provides an incomplete portrait of cultural fidelity by systematically obscuring inherent cultural diversity. This unidimensional evaluation lens prompts a fundamental question: do models genuinely perceive distinct cultural nuances, or do they merely memorize dominant cultural values? To address this, we propose a synergistic e...
  </details>

- **2026-09-01** — Yijun Chen, Yaqi Zheng, Yanya Li et al. — [EM^2Mem: Event-Centric Multimodal Memory for Large Language Models](http://arxiv.org/abs/2609.00551v1)
  <details><summary>📄 Abstract</summary>
  Multimodal memory offers a scalable interface for long-video question answering, but existing methods often retrieve captions, frames, transcripts, summaries, or graph facts as isolated fragments. Although searchable, such fragments are not generation-ready: language models must reconstruct cross-modal and temporal alignments at inference time, when context is limited and attribution is difficult. We propose EM^2Mem, an event-centric multimodal memory framework that binds heterogeneous evidence ...
  </details>

- **2026-09-01** — Clinton Enwerem, John S. Baras, Calin Belta — [Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds](http://arxiv.org/abs/2609.01453v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation policies learned by imitation are typically evaluated for robustness to variation in scenes, objects, or instructions, but their performance across task execution speeds is less often examined. This leaves open how much temporal robustness a learner retains relative to the expert it imitates. We compare an expert and learner under the same task conditions, initial-condition draws, and speedup factors. We instantiate the evaluation in ParcelStow, a contact-rich task in whic...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 61 papers

- **2026-09-03** — Jiacheng Xu, Wentao Zhang, Zhiyi Lyu et al. — [Two-Stage Reinforcement Learning for Sound and Adversarial Test Generation in Code LLMs](http://arxiv.org/abs/2609.03955v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has substantially advanced code generation with large language models (LLMs) through executable feedback. The feedback for coding problems mainly comes from specific test cases, where high-quality test cases are often scarce since they should be both sound and discriminative. We thus turn to study the auto-generation of test cases using the learned model. We find this is naturally an adversarial RL problem: the model is expected to generate effective test cases as cou...
  </details>

- **2026-09-03** — Ziqi Zhang — [Risk and Anomaly Identification for Distribution Network Optimal Operation Based on Reinforcement Learning and Uncertainty Quantification](http://arxiv.org/abs/2609.03308v1)
  <details><summary>📄 Abstract</summary>
  Reliable operation of modern distribution networks requires timely identification of operational risks and anomalous events under pervasive uncertainty. In practice, operators must identify risks that are inherent in stochastic yet in-distribution conditions, and anomalies that correspond to out-of-distribution behaviors such as unusual load patterns, extreme weather or cyber-physical attacks. This paper addresses this joint risk and anomaly identification problem for optimal distribution networ...
  </details>

- **2026-09-03** — Shai Vardi, João Sedoc — [Epistemic Warrant for LLM Recommendations: Characterizing the Basis for Reliance When Ground Truth Is Unavailable](http://arxiv.org/abs/2609.04127v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to support organizational decisions, yet users often lack a principled basis for assessing whether to rely on a specific recommendation. Existing approaches typically evaluate broad model properties, such as reliability, uncertainty, or robustness, or focus on user trust, rather than the underlying basis for relying on an individual recommendation. Adapting theoretical foundations from epistemology, we introduce epistemic warrant, a decision-level cons...
  </details>

- **2026-09-03** — Muneeb Khan, Frederic Kirstein, Terry Ruas et al. — [Speak for Me: Giving LLMs the Situational Awareness to Participate in a Meeting](http://arxiv.org/abs/2609.03923v1)
  <details><summary>📄 Abstract</summary>
  In online meeting delegation, LLM agents fail to recognize when to speak. With no structured way to track stances, coverage, and floor, they miss the moments where they should contribute. Prompt-only delegates stay silent on 51.4% of the absent participant's talking opportunities on the AMI corpus. We present CAPA (Collaborative Agent Predictive Architecture), an architecture for online meeting delegation. A Perceiver updates the meeting state from each observed turn. A Predictor forecasts how t...
  </details>

- **2026-09-03** — Chenhao Zhang, Hanyu Zhao, Hang Cheng et al. — [WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](http://arxiv.org/abs/2609.03681v1)
  <details><summary>📄 Abstract</summary>
  Post-training VLA policies typically rely on supervised fine-tuning with costly expert demonstrations or reinforcement learning with expensive and potentially unstable real-world exploration. World models offer a promising alternative by evaluating candidate behaviors through imagined futures, yet effective post-training requires more than accurate prediction: imagination must be scheduled where it is useful, bounded within reliable horizons, and translated into trustworthy policy supervision. I...
  </details>

- **2026-09-03** — Xingming Long, Yu Liu, Zhiwei Yang et al. — [Making Every Tool Call Count: Necessary Tool-Evidence Path Rewards for Agentic Vision-Language Models](http://arxiv.org/abs/2609.03493v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language models (VLMs) can directly answer many image-grounded questions, yet they often struggle with complex queries requiring fine-grained visual details or external knowledge. To acquire this missing evidence, agentic VLMs invoke tools such as image cropping, image search, and text search. However, existing training paradigms primarily evaluate tool-use based on final answer correctness, leaving evidence acquisition and utilization insufficiently supervised. This leads to two c...
  </details>

- **2026-09-03** — Ross Tieman, Evan Markou — [Inferred Generative-Process Diversity Predicts Correlated Failure Across Language Models](http://arxiv.org/abs/2609.03422v1)
  <details><summary>📄 Abstract</summary>
  Diversity is a widely observed factor in the resilient function of collective systems, yet the type of diversity that matters depends on the properties and failure modes of the system. This distinction is important for systems composed of multiple language models. Different models may be treated as independent components even when their behaviour and failures remain strongly correlated. Assessments of language-model populations using semantic similarity demonstrate limited semantic diversity, bu...
  </details>

- **2026-09-03** — Yuhe Wu, Guangyu Wang, Yujie Chen et al. — [Caught in the Story: Narrative Captivity in Multi-turn LLMs Conversation](http://arxiv.org/abs/2609.03407v1)
  <details><summary>📄 Abstract</summary>
  People increasingly turn to large language models (LLMs) for everyday advice, making ethically charged interpersonal problems a practical moral-advisory context. Most prior work has studied this context through single-turn judgments or pressure-laden rebuttals, assumptions that poorly match how guidance is sought in real-world contexts. These assumptions leave unclear whether narration alone, without an explicit opposing position, can shift model judgments during multi-turn moral consultation. Y...
  </details>

- **2026-09-03** — Adeela Islam, Zorah Lähner, Vittorio Murino et al. — [TokenMatch: 3D Mesh Correspondence Transformer with Curvature-Guided Tokenisation](http://arxiv.org/abs/2609.04202v1)
  <details><summary>📄 Abstract</summary>
  While data-driven 3D shape correspondence estimation has recently seen substantial progress, robust matching under partial observations and strong non-isometric deformations remains challenging. Existing learning-based approaches often rely on hand-crafted descriptors or template-based representations, whereas recent generative models over functional maps suffer from high inference cost, limited interpretability, and poor generalisation to partial shapes. In response to these limitations, this p...
  </details>

- **2026-09-03** — Haoyaun Zhu, Jie Zhang — [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](http://arxiv.org/abs/2609.04198v1)
  <details><summary>📄 Abstract</summary>
  Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow. We audited that assumption in two preregistered campaigns with every threshold fixed in advance; neither got past validating its instrument. Across 52,988 audited request attempts, same-window repeat rankings agreed at Spearman 0.400 against a required 0...
  </details>

- **2026-09-03** — Dmitrij Żatuchin — [The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing of Large Language Model Brand Recommendations](http://arxiv.org/abs/2609.04047v1)
  <details><summary>📄 Abstract</summary>
  Background: Researchers increasingly use repeated identical prompts to audit stochastic variation in large language model (LLM) brand recommendations, yet no standardized protocol exists for setting iteration counts, selecting stability metrics, or establishing reliability thresholds. Objective: We formalize the Dice Roll Method as a reusable protocol for repeated-query auditing of LLM brand recommendations, grounded in a generative model of temperature-scaled nucleus sampling. Methods: Total re...
  </details>

- **2026-09-03** — Boris N. Slautin, Sheryl L. Sanchez, Aidan Swanger et al. — [Hierarchical automation of scanning probe microscopy through agentic orchestration and algorithmic control](http://arxiv.org/abs/2609.04015v1)
  <details><summary>📄 Abstract</summary>
  Rapid advances in agentic artificial intelligence enable scientific systems to interpret open-ended objectives, combine heterogeneous information, invoke specialized tools, and revise experimental strategies as evidence accumulates. However, physical experimentation also contains many tasks for which agentic reasoning provides little advantage and can reduce reliability. Quantitative analysis, optimization, spatial targeting, validation, and instrument execution are often better posed as determi...
  </details>

- **2026-09-03** — Javier del Pino, Salvador Rodríguez, Alejandro Garabito et al. — [ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation](http://arxiv.org/abs/2609.03756v1)
  <details><summary>📄 Abstract</summary>
  We present ENEAS, a unified, text-promptable method for instance tracking and semantic discovery. Text-promptable segmentation models, including the latest foundation models such as SAM 3, still suffer from temporal hallucinations, spatial fragmentation, and semantic misclassification: they fail to report target absence when an object leaves the field of view, segment local textures instead of the complete object during extreme close-ups, and prioritize visual features over ontological reality, ...
  </details>

- **2026-09-03** — Yijun Yang, Shenghe Zheng, Wenbo Li et al. — [Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning](http://arxiv.org/abs/2609.03729v1)
  <details><summary>📄 Abstract</summary>
  Despite the remarkable prowess of Vision-Language Models (VLMs) in general multimodal tasks, they remain fundamentally ``flat'' when reasoning about the physical world. We argue that this spatial bottleneck stems from a profound dimensional mismatch: while VLMs are trained to interpret 2D projections, true spatial reasoning demands the recovery of latent 3D geometry and temporal continuity. To conquer this high-dimensional complexity, we advocate a shift from monolithic learning to a ``divide an...
  </details>

- **2026-09-03** — Chenguang Zheng, Le Xue, Yichi Zhang et al. — [MetaStructAtlas: A Grounded 3D Vision-Language Dataset and Benchmark for Functional and Structural Reasoning in Whole-Body PET/CT](http://arxiv.org/abs/2609.03690v1)
  <details><summary>📄 Abstract</summary>
  The joint interpretation of metabolic function and anatomical structure is essential for clinical diagnosis in whole-body PET/CT. Although recent advances in 3D medical vision-language models have demonstrated remarkable progress, current efforts are limited to regional CT imaging, leaving a critical void in comprehensive whole-body PET/CT analysis. In this work, we introduce MetaStructAtlas, a large-scale dataset for grounded whole-body PET/CT interpretation that synthesizes multimodal imaging ...
  </details>

- **2026-09-03** — Xiangchen Pan, Jiayi Xu, Jing Wang et al. — [LLM4AIGQ: LLM-based AI Guidance Query Generation Framework for Multi Interest Mining](http://arxiv.org/abs/2609.03674v1)
  <details><summary>📄 Abstract</summary>
  Guidance queries stimulate user consumption by extracting preferences to provide search queries with guidance value, playing a crucial role in the e-commerce field. Traditional AI-generated queries (AIGQ) generation primarily relies on a two-stage "Query-to-AI-Generated-Query" (Q2AIGQ) association paradigm, first recalling user primary search queries from user profiles, historical behavior sequences, item-side information, and the current query through multi-path retrieval, then generalizing AIG...
  </details>

- **2026-09-03** — Oussama Hidaoui, Omer Ebead, Ulrich Armel Mbou Sob et al. — [Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2609.03667v1)
  <details><summary>📄 Abstract</summary>
  Generalising to unseen tasks remains a fundamental challenge in offline multi-agent reinforcement learning (MARL). In this work, we present a principled analysis of zero-shot task generalisation in the offline setting and conduct an extensive empirical investigation into the scaling behaviour governing task diversity, dataset size, and network capacity. To facilitate this study, we extend offline sequence modelling architectures to handle multi-task observation and action spaces alongside variab...
  </details>

- **2026-09-03** — Vincenzo Norman Vitale, Mohammad Solki, Antonia Maria Tulino et al. — [From Prior-Guided Heuristics to Deployable Agents: Accelerating Demonstration-Driven Reinforcement Learning for Deadline-Constrained Network Control](http://arxiv.org/abs/2609.03590v1)
  <details><summary>📄 Abstract</summary>
  Timely delivery of delay-sensitive information over dynamic, heterogeneous networks is essential for NextG interactive applications, yet providing strict End-to-End (E2E) peak latency guarantees remains an open challenge. Two obstacles limit the adoption of learning-based network control in this setting: traditional volume-based routing metrics, while highly effective for general traffic management, are not designed to capture traffic urgency; and Deep Reinforcement Learning (DRL) controllers tr...
  </details>

- **2026-09-03** — Zeju Sun, Songlin Zhou, Stephen S. -T. Yau — [Well-posedness of Filtering Equations in Weighted Sobolev Spaces with Unbounded System Coefficients](http://arxiv.org/abs/2609.03549v1)
  <details><summary>📄 Abstract</summary>
  Nonlinear filtering problem is one of the core subjects in modern control theory. In this paper, we will study the well-posedness of the three fundamental evolution equations arising in continuous-time nonlinear filtering--the robust Duncan-Mortensen-Zakai (DMZ) equation, the stochastic DMZ equation, and the Kushner-Stratonovich equation--within a unified buffered weighted formulation. An exponential-type weight function and the corresponding weighted Sobolev spaces are introduced to enable a va...
  </details>

- **2026-09-03** — Jiaxi Song, Yunzhang Tian, Shucheng Pan — [A conservative coupling method of sharp-interface and multi-species model for compressible reacting gas-liquid flows with phase change](http://arxiv.org/abs/2609.03509v1)
  <details><summary>📄 Abstract</summary>
  In this paper, a conservative sharp-interface and diffuse-interface coupling method is developed for compressible two-phase multi-species flows with phase change and chemical reactions. The liquid--gas interface is represented by a sharp-interface model, whereas a diffuse-interface model treats the transport and chemical reactions of gas-phase species. Conservation is enforced by coupling the two phases through interfacial fluxes obtained from a multi-species phase-change Riemann problem. The or...
  </details>

- **2026-09-03** — Junsik Kim, Kangil Kim — [Pattern Over-Generalization of Knowledge Graph Embedding](http://arxiv.org/abs/2609.03487v1)
  <details><summary>📄 Abstract</summary>
  Knowledge graph embedding (KGE) demonstrates its effectiveness for predicting missing links in knowledge graphs (KGs) by projecting entities and relations into a low-dimensional vector space. It is crucial for KGE models to effectively capture inference patterns (patterns) inherent in KGs, such as symmetry/antisymmetry, inversion and composition. Although recent KGE models exhibit strong capabilities in modeling such diverse patterns, they suffer from inherent limitations stemming from pattern o...
  </details>

- **2026-09-03** — Yutong Zhang, Yangfan Zhou — [Knowledge-Based Mechanisms](http://arxiv.org/abs/2609.03439v1)
  <details><summary>📄 Abstract</summary>
  We study robust mechanisms when the designer possesses a Bayesian belief over some components of agents' private information but faces ambiguity over others. The designer evaluates mechanisms by their worst-case performance over all joint distributions consistent with her belief over the Bayesian components. The framework encompasses settings such as multidimensional delegation in which a principal knows the distribution of the state but not the agent's preferences (e.g., his tradeoffs across di...
  </details>

- **2026-09-03** — Chenglin Wu, Junjie Wu, Jinhang Chen et al. — [StrixAE: An Intelligent Agent for Audio Enhancement under Complex Distortion Coupling in Real-World Scenarios](http://arxiv.org/abs/2609.03414v1)
  <details><summary>📄 Abstract</summary>
  Audio enhancement in real-world scenarios involves complex distortion couplings and requires personalized enhancement. Existing solutions struggle to address both simultaneously. To improve robustness and enable autonomous operation in such scenarios, we propose StrixAE, an agent based on a multimodal large language model (MLLM). StrixAE leverages the MLLM as a controller to coordinate multiple audio enhancement and personalization models. To further enhance system robustness, reduce artifacts, ...
  </details>

- **2026-09-02** — Timothy Marsden, Matthew Collecutt, James Marsden — [Where Reliability Lives: Experimental Localisation of Behavioural Properties in an Agent System](http://arxiv.org/abs/2609.03192v1)
  <details><summary>📄 Abstract</summary>
  Reliability claims about agentic systems implicitly locate each property somewhere: in the model, or in the machinery around it. We built a system where that location is an experimental question. The subject is a persistent simulated settlement whose authoritative append-only ledger adjudicates every attempted act against world state; accepted history is the only reality. Mind, institution and world were separated before any experiment. Holding cognition fixed, we intervened on the institution's...
  </details>

- **2026-09-02** — Kamini Shahare, Peng Zhang — [QSVT-Based Three-Phase Unbalanced Power Flow](http://arxiv.org/abs/2609.03165v1)
  <details><summary>📄 Abstract</summary>
  This letter introduces QSVT-3PF, a quantum singular value transformation (QSVT) based solver for three-phase unbalanced power flow with embedded single-phase grid-forming inverter (GFM) operation. The contributions are threefold: 1) reformulating the Newton correction as a QSVT-compatible inverse problem using a normalized block-encoded phase-domain Jacobian; 2) introducing a regularized singular-value filter to improve robustness under ill-conditioned and stressed operating conditions; and 3) v...
  </details>

- **2026-09-02** — V. M. Vasyuta, V. V. Malitskyi, O. S. Kushnir et al. — [Turn-Based Combat Arena: A New Framework for Multiagent Training and Game Balancing](http://arxiv.org/abs/2609.03122v1)
  <details><summary>📄 Abstract</summary>
  This paper is the first in a series on Turn-Based Combat Arena, a configurable framework for turn-based strategy games designed to support the efficient training and evaluation of machine learning agents. The proposed framework enables flexible modification of game rules and parameters, allowing rapid experimentation across diverse scenarios. Its architecture is optimized for high-throughput simulation, supporting tens of thousands of games per second and enabling the storage and processing of b...
  </details>

- **2026-09-02** — Bowen Jiang, Haowei Cheng, Yuhong Fu et al. — [Requirements After the First Edit: Mining Late Requirement Emergence and Rework in Real-World Coding-Agent Sessions](http://arxiv.org/abs/2609.03028v1)
  <details><summary>📄 Abstract</summary>
  Coding agents often implement changes before users have fully articulated their requirements, echoing a pattern from requirements engineering: stakeholders cannot express a constraint until part of the system exists to react to. This volatility is associated with schedule and budget overruns in traditional projects, but only at release-cycle granularity. Existing work on coding agents narrows this gap only partway: curated benchmarks fix requirements before implementation by design, and observat...
  </details>

- **2026-09-02** — Dongrun Cai, Xue Chen, Xiaowei Shao — [Learning Multiband Signals and Fourier-sparse Signals](http://arxiv.org/abs/2609.02977v1)
  <details><summary>📄 Abstract</summary>
  We consider efficient algorithms to learn multiband signals and Fourier-sparse signals. A mutliband signal has a Fourier transform supported by a bounded number of intervals, say $I_1 \cup I_2 \cdots \cup I_n$. There is a long line of research on multiband signals. In particular, Avron et al. showed an efficient reconstructing algorithm whose sample complexity is almost optimal. However, all previous algorithms for multiband signals consider the reconstructing problem in which the locations of $...
  </details>

- **2026-09-02** — S M Rafiuddin, Atriya Sen — [C$^{3}$T: Counterfactual Causal Reasoning for Sentiment Shifts in Social-Media Conversation Trees](http://arxiv.org/abs/2609.02131v1)
  <details><summary>📄 Abstract</summary>
  Sentiment in social-media threads does not only vary across posts; it shifts as users react to claims, corrections, evidence, and hostility within a branching reply tree. We study why sentiment changes in rumor-centric conversation trees by treating discourse moves (e.g., denial/correction, evidence/link, toxicity/attack) as candidate interventions and asking (i) what sentiment a reply expresses, (ii) whether the sentiment shifts relative to its parent, and (iii) which prior message most plausib...
  </details>

- **2026-09-02** — Yu Tian, Xintong Jiang, Jan Franklin Adamowski et al. — [PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation](http://arxiv.org/abs/2609.02860v1)
  <details><summary>📄 Abstract</summary>
  Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches rely heavily on densely annotated datasets that are labor-intensive to acquire. Unified PPCS adaptation from distribution-shifted examples with minimal additional training remains challenging. To address this, we propose PlantC2USeg, a deep transfer learning framework featuring cross-scale consisten...
  </details>

- **2026-09-02** — Jiayi Bi, Yanjie Gao, Yuanmin Xie et al. — [Diagnosing with Insights: Structured Analysis of Agent Failures via Behavioral Abstractions](http://arxiv.org/abs/2609.02371v1)
  <details><summary>📄 Abstract</summary>
  With the proliferation of LLM agents, the ability to understand and diagnose failures in agents is essential to achieving superior effectiveness and trustworthiness. As agent failures often manifest via long and complex trajectories, manually finding the needles in the haystack is untenable. However, traditional diagnosis techniques for software bugs can hardly address LLM agent failures, while completely relying on LLMs as the judge yields unreliable diagnosis results. To overcome these challen...
  </details>

- **2026-09-02** — Mingyu Mei, Haojie Xu, Shihao Jin et al. — [HINT: Human-Intent Inception for Long-Horizon Robot Manipulation](http://arxiv.org/abs/2609.02653v1)
  <details><summary>📄 Abstract</summary>
  Humans can perform complex manipulations given a simple intent through an overall instruction, while continuously adapting to evolving visual observations. However, current vision-language action (VLA) models and other action policies struggle to realize this high-level intelligent behavior under dense, evolving visual inputs and sparse language guidance. Visual correlations can then dominate semantic intent, leading actions to follow visual shortcuts rather than human goals. We present HINT (Hu...
  </details>

- **2026-09-02** — Caio Azevedo, Stefano Sabatini, Sascha Hornauer et al. — [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](http://arxiv.org/abs/2609.02341v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) have shown strong potential in autonomous driving by leveraging multimodal pretraining for instruction following, visual reasoning, and scene-level generalization. In robotic manipulation, scaling VLA fine-tuning across multiple robot setups--especially when unifying representations across embodiments--has been shown to improve in-dataset performance and cross-embodiment generalization; in autonomous driving, however, VLAs remain largely trained on individual...
  </details>

- **2026-09-02** — Dmitrii Andriianov, Andrey Veprikov, Aleksandr Beznosikov — [LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates](http://arxiv.org/abs/2609.02734v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) is the standard way to fine-tune large models, yet when its two factors are trained independently, the update ignores the geometry of the low-rank weight change it induces. We introduce LoRA-TSD, an optimizer that treats every LoRA step as a tangent vector of the fixed-rank matrix manifold and takes the spectral-norm steepest-descent step of Muon inside that tangent space, mapping the result back to the factors through a retraction native to the LoRA parametrization. T...
  </details>

- **2026-09-02** — Canjie Liu, Jiawen Kang, Jinbo Wen et al. — [RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models](http://arxiv.org/abs/2609.02731v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models have achieved remarkable success in vision-language tasks. However, they remain prone to Visual Hallucinations (VHs), undermining their reliability in real-world applications. Existing solutions typically require curated datasets, additional training, or multi-round decoding, resulting in considerable computational overhead. In this paper, we propose \textbf{RVSD} (\underline{R}etrieval \underline{V}ision \underline{S}parse \underline{D}ecoding), a training-free and ...
  </details>

- **2026-09-02** — Hoonhee Cho, Jae-Young Kang, Giwon Lee et al. — [VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation](http://arxiv.org/abs/2609.02462v1)
  <details><summary>📄 Abstract</summary>
  End-to-end autonomous driving in urban environments requires robust decision-making under partial observability and complex multi-agent interactions. Severe occlusions and dense traffic at intersections limit the perception capability of single-agent systems, motivating recent efforts on Vehicle-to-Infrastructure (V2I) cooperation for perception and planning. However, existing evaluation protocols face a fundamental trade-off: open-loop evaluation fails to capture error accumulation and recovery...
  </details>

- **2026-09-02** — Etcharla Revanth Rao, Priyanshu Karmakar, Shubhojit Mallick et al. — [UTP-Bench: Uncertainty-aware Travel Planning Benchmark](http://arxiv.org/abs/2609.02421v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently demonstrated strong capabilities in automated travel itinerary generation. However, real- world travel planning is inherently uncertain: transportation delays, crowd fluctuations, and unexpected stochastic delays frequently inval- idate otherwise feasible schedules. Existing benchmarks like TravelPlanner and TripCraft assume deterministic environments, evaluating only static constraint satisfaction and ignoring whether generated plans remain robust when...
  </details>

- **2026-09-02** — Jingguan Liu, Xiaomeng Ai, Jiakun Fang et al. — [Continuous-Time Aggregation of Massive Flexible HVAC Loads Considering Uncertainty for Reserve Provision in Power System Dispatch](http://arxiv.org/abs/2609.02408v1)
  <details><summary>📄 Abstract</summary>
  Heating, ventilation, and air conditioning (HVAC) loads, with their rapid response capabilities, can provide considerable intra-hour flexibility on the demand side for reserve provision in order to follow the fast variations of renewables. However, scheduling massive HVACs is challenging due to computation complexity and the uncertainty of outdoor temperature. In this paper, we first introduce a novel continuous-time (CT) aggregation model to reveal the potential intra-hour flexibility of HVACs....
  </details>

- **2026-09-02** — Matteo Greco, Anudeex Shetty, Andrea Tagarelli et al. — [MultiGhostBench: A Multilingual Benchmark for Long-Form LLM-Generated Text Attribution under Distribution Shifts](http://arxiv.org/abs/2609.02379v1)
  <details><summary>📄 Abstract</summary>
  While existing work on LLM authorship attribution (AA) has made progress, available benchmarks remain limited, often focusing on English, controlled settings, or relatively outdated models, with the few multilingual studies considering only relatively short texts. We introduce MultiGhostBench, a multilingual benchmark comprising 928 books generated by five recent LLMs across six languages and three scripts, with an average length of approximately 59K words per book. The benchmark supports evalua...
  </details>

- **2026-09-02** — Chongkun Deng — [Farthest-cell triplet entropy: high-dimensional shell limits and hyperbolic curvature amplification](http://arxiv.org/abs/2609.02362v1)
  <details><summary>📄 Abstract</summary>
  We introduce farthest-cell triplet entropy, the conditional Shannon entropy of the farthest-prototype label given three random prototypes. For independent queries and prototypes, its estimator records only the farthest label, not coordinates or numerical distances. The statistic is bounded by $\log 3$, is invariant under common strictly increasing transformations of the dissimilarities, and has an exact mutual-information interpretation. In high-dimensional isotropic radial models $X_d=R_dU_d$, ...
  </details>

- **2026-09-02** — Qiang Xiang, Shuang Sun, Binglei Li et al. — [GlyphAnchor: Enhancing Visual Text Rendering via Position-Anchored Glyph Priors](http://arxiv.org/abs/2609.02349v1)
  <details><summary>📄 Abstract</summary>
  Rendering accurate text remains difficult for image generation and editing models, especially when the target contains long, complex, and densely arranged text or rare characters. Existing approaches either improve native text rendering through stronger backbones and data-centric training without explicit glyph priors, or incorporate glyph priors through specialized designs that remain insufficiently accurate and robust under challenging scenarios. We introduce GlyphAnchor, a novel text-renderin...
  </details>

- **2026-09-02** — Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag — [Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation](http://arxiv.org/abs/2609.02232v1)
  <details><summary>📄 Abstract</summary>
  Automated student-attention estimation can support learning analytics, but aggregate predictive metrics can conceal demographic disparities. This study evaluates fairness-aware multimodal temporal models on DIPSER, a naturalistic classroom dataset combining facial images, wearable-sensor measurements, attention annotations, and automatically inferred demographic metadata. Three baselines are compared across 10 training seeds: a Visual GRU, a Sensor GRU, and a Residual Fusion Transformer. The mul...
  </details>

- **2026-09-02** — Wei Zhang, Hongji Li, Song Sun et al. — [DMRL: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation](http://arxiv.org/abs/2609.02170v1)
  <details><summary>📄 Abstract</summary>
  Advertising recommendation requires continuously tuning complex system parameters while balancing commercial returns and user experience. Recent work has introduced large language models (LLMs) with skill documents to assist this labor-intensive process, but skill optimization remains largely prompt-driven, lacking a principled mechanism to attribute rewards to specific document edits. To address this limitation, we propose Document-Mediated Reinforcement Learning (DMRL), a skill self-evolution ...
  </details>

- **2026-09-02** — Alexander J Healey, Alan Salek, Christopher T-K Lew et al. — [Persistence and emergence of quantum defects through pressure-induced phase changes](http://arxiv.org/abs/2609.02100v1)
  <details><summary>📄 Abstract</summary>
  Extreme pressures can transform materials and their properties, but probing these in-situ is made challenging by the small sample volumes and access requirements demanded by diamond anvil cells. Quantum defects offer a route to local measurements under such conditions, yet their sensing performance can be dictated by pressure-induced changes in their own host material. On the other hand, pressure may also be harnessed as a tool to engineer and stabilize new quantum defects with emergent function...
  </details>

- **2026-09-01** — Joshua Shay Kricheli — [Differential Games for Compositional Handling of Competing Control Tasks](http://arxiv.org/abs/2609.01838v1)
  <details><summary>📄 Abstract</summary>
  We introduce a novel Divide and Conquer control design methodology leveraging differential games in single-agent, multi-objective dynamical systems. The proposed framework associates each control objective with a virtual input and establishes a non-cooperative, finite or infinite horizon differential game among representative players. Each player optimizes a distinct virtual cost function tailored to its specific goal, the full system state, and the other virtual inputs, while accounting for the...
  </details>

- **2026-09-01** — Dushyant Rajput — [Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades](http://arxiv.org/abs/2609.01345v1)
  <details><summary>📄 Abstract</summary>
  Inference cascades cut cost by answering most queries with a cheap model and escalating a hard tail to a frontier model that acts as verifier. A natural extension closes the loop: fine-tune the cheap student on the verifier's rejections so the escalation rate, and cost, fall each round. We measure this loop on real LLMs and report four findings. First, the verifier's blind spot, the fraction of the student's wrong answers it accepts, is large and moves adversarially: it grows with student capabi...
  </details>

- **2026-09-01** — Navaneetha Krishnan Kamalakannan — [Real-Time Neuromorphic Spectrum Intelligence Simulator](http://arxiv.org/abs/2609.00585v1)
  <details><summary>📄 Abstract</summary>
  We present the Real-Time Neuromorphic Spectrum Intelligence Simulator (RT-NuSIS), a modular framework to study spiking neural network (SNN) and memristor-inspired agents for dynamic spectrum access under constrained energy budgets and adversarial conditions. RT-NuSIS couples leaky integrate-and-fire neuronal dynamics, memristive synaptic models, physics-informed energy-harvesting models (triboelectric and RF), and adversary models including jamming and Byzantine behavior. We formalize the simula...
  </details>

- **2026-09-01** — Haoyuan Deng, Haichao Liu, Wenkai Guo et al. — [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](http://arxiv.org/abs/2609.01596v1)
  <details><summary>📄 Abstract</summary>
  Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning (RL) post-training around a joint action-wrench proposal: a causal wrench history is aligned with vision-language semantics and kinematic state, and flow matching gen...
  </details>

- **2026-09-01** — Fatemeh Javadian, Zhu Chen, Zahra Aminparast et al. — [Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading](http://arxiv.org/abs/2609.01426v1)
  <details><summary>📄 Abstract</summary>
  Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map ch...
  </details>

- **2026-09-01** — Nishant Mishra, Ameen Abu-Hanna, Iacer Calixto — [Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA](http://arxiv.org/abs/2609.01361v1)
  <details><summary>📄 Abstract</summary>
  Linear classifiers trained on hidden states of a large language model (LLM), linear probes, can flag factual errors from a single forward pass. Geometrically, that implies that true and false statements separate along a stable direction in hidden state space, i.e., the truth direction. Prior work disagrees on whether this generalises across input shifts, but the disagreement is hard to interpret because cross-dataset probe transfer experiments confound several kinds of input change at once. We i...
  </details>

- **2026-09-01** — Natalija Mitic, Soona Sedahmed A. O., Mamadou Selly Ly et al. — [The Constitutional Coverage Trilemma in AI Governance](http://arxiv.org/abs/2609.01275v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI systems function as \emph{constitutional institutions}: each deployed model encodes an implicit ranking among safety, helpfulness, honesty, autonomy, and equity. We ask whether the supply of frontier constitutional types covers human demand. Combining a paraphrase-controlled audit of the as-shipped default constitutions of $23$ frontier LLM archetypes with a pairwise-tradeoff study of $1{,}649$ US participants on the same instrument, we report three facts. \emph{Demand is broad}: it ...
  </details>

- **2026-09-01** — Fanrui Zhang, Ruixue Ding, Qiang Zhang et al. — [ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning](http://arxiv.org/abs/2609.01058v1)
  <details><summary>📄 Abstract</summary>
  Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout contrast that obscures fine-grained optimization signals for group-based policy learning. To address these challenges, we propose ARISE-RL, a novel full-cycle self-evolution framework that couples a t...
  </details>

- **2026-09-01** — Jongyeop Hyun, Taeyoung Kim, Hyounghun Kim — [Controllable Image Captioning with Prompt-Conditioned Scene Rewards](http://arxiv.org/abs/2609.00709v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models produce fluent image descriptions but offer limited semantic control: users cannot reliably specify whether captions should emphasize attributes, relations, or particular image regions. We present Fine-grained Captioning Control Using Scene Rewards (FoCUS), a controllable image captioning method that lets users steer captions toward specific semantic emphases through natural-language control prompts. The core idea is a prompt-conditioned control objective based on sc...
  </details>

- **2026-09-01** — Lingxiao Li, Max Whitton, Ledell Wu et al. — [GenScale: A Benchmark for Relative Object Scale in Image Generation and Editing](http://arxiv.org/abs/2609.00525v1)
  <details><summary>📄 Abstract</summary>
  Modern image generation and editing systems can produce photorealistic, prompt-aligned images, but still often render familiar objects at implausible relative sizes. To measure this failure mode, we introduce GenScale, a benchmark and evaluation protocol for real-world relative object scale in image generation and editing. GenScale contains 900 image-level entries and 1,643 pairwise anchor-target scale relations across common-object generation, human-product generation with metric dimensions, an...
  </details>

- **2026-09-01** — Md. Atabuzzaman, Chris Thomas — [Reliability Challenges in Diffusion Vision-Language Models](http://arxiv.org/abs/2609.01318v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our ...
  </details>

- **2026-09-01** — Athira J. Jacob, Puneet Sharma, Daniel Rueckert — [CMRVision: A Foundation Model for Cardiac MR Image Analysis](http://arxiv.org/abs/2609.01308v1)
  <details><summary>📄 Abstract</summary>
  Cardiac magnetic resonance (CMR) imaging provides complementary information on cardiac anatomy, function, and tissue characterization across multiple sequences and views. In this work, we investigate foundation model pretraining for 2D CMR and introduce CMRVision, a CMR-specific foundation model trained using DINOv3-style self-supervised learning on a multi-center, multi-sequence cohort of 36 million CMR images. We systematically evaluate architectural and training design choices for domain-spec...
  </details>

- **2026-09-01** — Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera et al. — [HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives](http://arxiv.org/abs/2609.01282v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformer (ViT) design has become increasingly diverse, with backbones combining convolutional stems, windowed, linear, or multi-axis attention, patch merging, and spatial reduction in various configurations. This diversity poses challenges for existing attribution methods, whose assumptions often do not hold across ViT variants: Grad-CAM requires a terminal spatial feature map, attention rollout assumes global softmax attention, and layer-wise relevance propagation (LRP) requires modul...
  </details>

- **2026-09-01** — Jiayi Yan, Francesco Fabiano, Alessandro Abate — [Dual Process Motion Planning](http://arxiv.org/abs/2609.01260v1)
  <details><summary>📄 Abstract</summary>
  Robotic systems are deeply embedded in both industry and everyday life, where they are expected to act with speed, precision, and reliability. Classical control and planning methods have long delivered strong guarantees, but often at the cost of computational efficiency and adaptability. More recently, learning-based approaches have shown promise in overcoming these limitations, enabling agents to leverage experience to accelerate decision-making and address previously intractable problems. In t...
  </details>

- **2026-09-01** — Walid Saidi — [MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence](http://arxiv.org/abs/2609.01235v1)
  <details><summary>📄 Abstract</summary>
  MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path. MutMem V2 closes that publication gap without introducing a second memory engine. It specifies exact canonical bytes, domain-separated object and bundle commitments, mandatory recall-evidence membership and ordering, external trust anchors, identity epochs, revocation, authorization, request ...
  </details>

- **2026-09-01** — Reza Heidari, Hamed R. Tavakoli, Juho Kannala — [Compressing AI Traffic: Standardized Neural Network Coding of Visual-Token Representations in Split Vision-Language Inference](http://arxiv.org/abs/2609.01200v1)
  <details><summary>📄 Abstract</summary>
  When the visual encoder and the language decoder of a vision-language model (VLM) run on different compute nodes, the intermediate visual-token embeddings become a communicated payload rather than an internal activation. We call such machine-consumed intermediate tensors AI traffic and ask how far they can be compressed with a standardized, training-free codec. We insert ISO/IEC 15938-17 Neural Network Coding (NNC) round trips on the complete visual interface of a Qwen3-VL-8B-Instruct video ques...
  </details>

- **2026-09-01** — Chaohui Guo, Michel Klein, Zhisheng Huang — [CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs](http://arxiv.org/abs/2609.01195v1)
  <details><summary>📄 Abstract</summary>
  Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thus lacking flexibility in realistic multi-candidate settings. At the same time, they typically ignore inference cost at scale. We formulate LLM-based EM with candidates as a cost-aware sequential decis...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 17 papers

- **2026-09-03** — Yakov Pyotr Shkolnikov — [From Deceptive Outputs to Deceptive Mechanisms: A Causal Framework for Language-Model Deception Research](http://arxiv.org/abs/2609.04166v1)
  <details><summary>📄 Abstract</summary>
  Research and news coverage of language-model deception increasingly attributes human-like mental-state concepts to language models. Such claims can blur the distinction between behavior that looks deceptive and a mechanism that is actually deceptive.   We introduce a causal taxonomy separating prior commitment from retrospective report, model preference from realized output, false preference from sensitivity to the utility of misleading a recipient, and deceptive behavior from the provenance of ...
  </details>

- **2026-09-03** — Shubham Gandhi, Saurabh Goyal, Kiran Kate et al. — [DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](http://arxiv.org/abs/2609.04094v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work in the outcome-blind setting, where ground-truth success signals are not available. Multi-criteria rubrics are a popular way to supply such a reward; they are scored once per trajectory, but a single scalar is a poor signal across tens of steps. We propose DRACO: Distributing Rubric-based Advantage for Credit Optimization. It generates rubrics d...
  </details>

- **2026-09-03** — Linh Le, Melanie Bui, My Chiffon Nguyen et al. — [GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis](http://arxiv.org/abs/2609.03553v1)
  <details><summary>📄 Abstract</summary>
  Policy analysis requires more than predicting whether a proposal will pass: it requires identifying who will be affected, how those actors respond, and what follows. LLM-based policy simulations model these processes at scale, but their validity is hard to establish when plausible behaviour is never compared with observed outcomes. We introduce GPS-Bench, an evidence-grounded benchmark for governance policy simulation that links policies to relevant actors, actor actions and downstream impacts u...
  </details>

- **2026-09-03** — Bo Zeng, Linfeng Gao, Peiqin Lin et al. — [CulturalMenuBench: Probing the Knowledge-Application Gap in Multimodal Culinary Reasoning](http://arxiv.org/abs/2609.03526v1)
  <details><summary>📄 Abstract</summary>
  Multimodal language models achieve near-ceiling scores on food recognition benchmarks, yet it remains unclear whether this success reflects genuine cultural understanding or mere visual matching. To probe this distinction, we introduce CulturalMenuBench, a benchmark of 4,870 items in 10 languages across 18 regions; its 10 tasks pair final-dish and step-by-step cooking images with ingredients, procedural text, and regional labels, spanning basic recognition to process-grounded cultural attributio...
  </details>

- **2026-09-03** — Guangjun Liu — [The Civilization Framework: Sovereign-Anchored Communication Between Personal Multi-Agent Systems](http://arxiv.org/abs/2609.03425v1)
  <details><summary>📄 Abstract</summary>
  Humans are the transport layer between AI systems, losing context at every hop. We present the Civilization Framework, whose addressable party is the civilization, not the agent (one human sovereign, a persistent ledger, and interchangeable agents), and the Embassy Protocol, a carrier-agnostic overlay: messages arrive asynchronously at a resident ledger endpoint, any online agent of the receiver handles them, and commitment state on both ledgers, not delivery, is ground truth. Authority derives ...
  </details>

- **2026-09-03** — Sompote Youwai, Chana Phutthananon, Warat Kongkitkul — [A Large Open Multi-Energy Corpus of Soil Compaction Tests, with Machine-Learning Baselines](http://arxiv.org/abs/2609.03337v1)
  <details><summary>📄 Abstract</summary>
  Every engineered fill is specified by a maximum dry density and an optimum moisture content. Each determination needs a full Proctor test. Published correlations rest on one to four hundred specimens, usually from one laboratory at one compactive energy, and are seldom released. This paper releases a corpus without those limits. It holds 2,854 laboratory compaction tests from six public sources, across 162 provenance groups and four Proctor energy levels, with fines from 1.5 to 100%. Every recor...
  </details>

- **2026-09-03** — Augusto Camargo — [Beyond .WAV: Design and Software Verification of VocalCap, a Traceable Browser-Based Audio Capture System for Vocal Biomarker Research](http://arxiv.org/abs/2609.03320v1)
  <details><summary>📄 Abstract</summary>
  Remote voice studies often retain a final audio file with limited evidence about how it was captured, transferred, processed, and accepted. This paper presents VocalCap, an institution-controlled, browser-based system for self-guided capture of voice and related acoustic signals by participants without technical training. A versioned protocol drives the workflow. Each accepted recording retains a browser-native object, a client-lossless Float32 WAV derived from the same MediaStream, and a server...
  </details>

- **2026-09-02** — Meriem Yacoubi, Pia Schmidt, Nenad Petrovic et al. — [MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval](http://arxiv.org/abs/2609.03201v1)
  <details><summary>📄 Abstract</summary>
  Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions. Existing textual memory systems retrieve semantically relevant memories efficiently but often leave these relationships implicit, whereas richer structured approaches model them through global graphs, hierarchical abstractions, or reflection at greater complexity. We introduce MemoryLACE (MemLACE), a lightweight memory framework tha...
  </details>

- **2026-09-02** — Valentin Kuznetsov, Werner M. Sun, Keara Soloway et al. — [FOXDEN: FAIR Services for AI-Ready Scientific Datasets](http://arxiv.org/abs/2609.03105v1)
  <details><summary>📄 Abstract</summary>
  Scientific datasets are most compatible with AI workflows when they are described by rich, machine-readable metadata and provenance information, following the FAIR guiding principles. The FAIR Open-Science Extensible Data Exchange Network (FOXDEN) is a set of cyberinfrastructure building blocks developed at the Cornell High Energy Synchrotron Source (CHESS) for annotating raw, reduced, and analyzed datasets with both structured and unstructured metadata and provenance records. It also allows res...
  </details>

- **2026-09-02** — Tristan Lazard, Kenza Bouzid, Julius Hense et al. — [Sparse concept attribution for histomorphological hypothesis generation from whole-slide classifiers](http://arxiv.org/abs/2609.02985v1)
  <details><summary>📄 Abstract</summary>
  Histology images contain rich morphological information and can provide insights into pathological processes. However, deriving hypotheses relating morphological phenotypes to clinical attributes is bottlenecked by a manual image interpretation step. Here, we demonstrate that this process can be automated through interpretable deep learning. We present SCOPE, a method to interpret slide-level classifiers by combining pathology-specific vision--language models with sparse concept attribution onto...
  </details>

- **2026-09-02** — Yuzhang Luo, Chenpeng Wang, Jianhui Chen et al. — [From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution](http://arxiv.org/abs/2609.02771v1)
  <details><summary>📄 Abstract</summary>
  Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influence functions (IF) estimate behavioral changes under infinitesimal reweighting, yet IF-selected examples often show limited advantages over random selection under conventional weight-based interventions. This raises the question of whether influential examples lack intervention value or whether reweig...
  </details>

- **2026-09-02** — Yujie Tu, Zhiliang Peng, Jianwei Yu et al. — [VibeVoice-ASR-Streaming Technical Report](http://arxiv.org/abs/2609.02812v1)
  <details><summary>📄 Abstract</summary>
  Traditional speaker-attributed ASR systems treated ASR and speaker diarization as two separate tasks. Recently, end-to-end models such as VibeVoice-ASR have unified the two tasks within a single model. However, existing unified models still mainly support offline recognition, making it difficult to meet the low-latency requirements of real-time voice assistants and agents. To tackle this issue, we present VibeVoice-ASR-Streaming, one of the first LLM-based end-to-end approaches to streaming spea...
  </details>

- **2026-09-02** — Jan Schnorrenberg, Jan Ernsting, Enrico Küllenberg et al. — [Seeing Beyond the Lesion: Disease Recognition from Reactive CNS Tissue](http://arxiv.org/abs/2609.02390v1)
  <details><summary>📄 Abstract</summary>
  Sampling error yields exclusively reactive, non-lesional brain parenchyma in a significant proportion of intracranial biopsies, leaving the underlying disease undiagnosed. We benchmark four pathology foundation models (UNI2-h, Virchow2, Prov-GigaPath, H-optimus-0) as frozen patch encoders within a shared attention-based multiple-instance learning framework using 245 whole-slide images from 186 patients with confirmed downstream diagnoses. We first show that coarse disease-category prediction can...
  </details>

- **2026-09-02** — Yunhao Liu, Hong Phuc Pham, Jaehong Yoon — [PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation](http://arxiv.org/abs/2609.02272v1)
  <details><summary>📄 Abstract</summary>
  Faithfully translating research papers into repository-level implementations remains challenging because papers often describe methods at a high level, leave implementation assumptions implicit, and require generated repositories to preserve method logic, evaluation protocols, and cross-file consistency. Despite recent advances in paper-to-code agents, their intermediate outputs are often presented as free-form plans or summaries that downstream coding agents may ignore, reinterpret, or compress...
  </details>

- **2026-09-01** — Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol — [Agent Memory Is a Surface for Endogenous Authorization Laundering](http://arxiv.org/abs/2609.01836v1)
  <details><summary>📄 Abstract</summary>
  Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks.   We term this failure endogenous authorization laundering, where spurious permissions written into memory lead to unauthorized actions as their pr...
  </details>

- **2026-09-01** — Jun Hou, Priya Pitre, Yi Fang et al. — [EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems](http://arxiv.org/abs/2609.01360v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agent failures often contain multiple related errors rather than a single mistake. Existing attribution methods usually identify a responsible agent, step, or root cause, but do not explicitly model dependency between errors. We introduce EDGE, an Error Dependency Graph-guided multi-Error attribution framework. EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset through counterfactual rollout. The inference graph ...
  </details>

- **2026-09-01** — Huimin Wang, Zhengyi Zhao, Yutian Zhao — [ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues](http://arxiv.org/abs/2609.01111v1)
  <details><summary>📄 Abstract</summary>
  Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines, LLM summaries, agentic memory---preserve the longitudinal signal clinical reasoning needs has not been measured. We introduce ClinTraceBench: 385 MIMIC-IV-derived verified dialogues with event-ID provenance, a nine-task taxonomy (T1--T9), and L0--L4 deterministic + L5 human-audit validation (98.92\% agreement). We evaluat...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-09-02** — Evžen Wybitul, Tim G. J. Rudner, Christian Schroeder de Witt — [Entangled Representations Amplify Collateral Damage in Unlearning](http://arxiv.org/abs/2609.02285v1)
  <details><summary>📄 Abstract</summary>
  A long-held intuition in interpretability research is that representational entanglement, the sharing of structure between knowledge domains in a neural network, makes unlearning harder. While the intuition is widespread, it has never been directly tested in a controlled experiment. We present a way to do so: by repurposing Selective Gradient Masking (SGTM), we train a suite of six 254M-parameter language models on English Wikipedia with graded levels of disentanglement between biology and non-b...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-09-03** — Luyi Xing, Rasit Onur Topaloglu, Ranjan Sinha et al. — [The Natural Language Interaction Protocol and Standard for AI Agents](http://arxiv.org/abs/2609.04135v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly being developed and deployed across organizations using heterogeneous agent-development frameworks, AI models, tool interfaces, protocols, and execution environments. To realize their potential social and business impact, these agents must be able to interoperate through a common communication protocol. The Natural Language Interaction Protocol (NLIP), developed by researchers and practitioners across companies and universities and standardized by Ecma International, a...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 12 papers

- **2026-09-03** — Vishnu Asutosh Dasu, Ashish Kundu, Gang Tan — [Refusing the Impossible: A Taxonomy and Benchmark for Code Hallucination in Large Language Models](http://arxiv.org/abs/2609.03267v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often produce code that looks plausible but is not grounded in reality. The code may import packages that do not exist or claim to implement algorithms that violate proven theorems, while still compiling and running. We study \emph{code hallucination} as \emph{ungrounded generation} and separate it from ordinary \emph{code error} (bugs in otherwise grounded programs). We propose a taxonomy with three dimensions: \textbf{groundedness} (absolute violations of universal...
  </details>

- **2026-09-03** — Saptarshi Basu, Sandeep Kakar, Ashok Goel — [A Prompt-Engineering Approach to Develop Scalable, Flexible, and Real-Time Hybrid Micro-Level Personalization in a General Purpose AI Teaching Assistant](http://arxiv.org/abs/2609.03402v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) teaching assistants powered by large language models (LLMs) offer scalable educational support but often provide limited personalization. This study presents a prompt-engineering-based framework for personalizing general-purpose LLM/RAG-based AI teaching assistants such as Jill Watson across academic disciplines and courses. The framework adapts responses using six learner-specific dimensions: self-assessment, abstraction preference, verbosity preference, perceptual ...
  </details>

- **2026-09-02** — Runlin Shi, Bojian Yin, Guoqi Li — [Modern Transformers Are Implicit Hybrids: From Functional Differentiation to Principled Hybrid Architecture Design](http://arxiv.org/abs/2609.02986v1)
  <details><summary>📄 Abstract</summary>
  Hybrid architectures combining Full Attention (FA) and Linear Attention (LA) are increasingly prominent, yet their allocation remains heuristic. We seek an evidence-grounded basis in head-level functional organization learned by RoPE-based Transformers. Behavioral probes do not yield a complete taxonomy, so we propose two intervention metrics: RoPE Frequency Importance Score (RFIS), measuring how each frequency affects a head's attention distribution, and RoPE Positional Dependence (RPD), isolat...
  </details>

- **2026-09-02** — Xinye Yang, Zhenyang Liu, Ruisi Li et al. — [Large Language Models in Resolving Contextual Knowledge Conflicts](http://arxiv.org/abs/2609.03148v1)
  <details><summary>📄 Abstract</summary>
  Most prior works focused on conflicts between an LLM's internal parametric knowledge and externally provided context. In contrast, we investigate how LLMs handle conflicts that arise within contextual knowledge itself. We introduce a taxonomy of six types of contextual conflicts (factual, inferential, temporal, granularity, perspective, and ambiguity) and contribute a comprehensive dataset ContextConflict for this setting. The dataset contains 5,781 samples, covers both reasoning and summarizati...
  </details>

- **2026-09-02** — Ming Jiang, Erwu Liu, Xinyu Qu et al. — [A Survey of Decentralized Physical Infrastructure Network,Research Directions, and Open Challenges](http://arxiv.org/abs/2609.02125v1)
  <details><summary>📄 Abstract</summary>
  The Decentralized Physical Infrastructure Network (DePIN) represents a transformative paradigm that redefines the construction, operation, and governance of Information and Communication Technology (ICT) infrastructure in the Web 3.0 era. DePIN integrates physical resources, such as networking equipment, storage, and computing power, with decentralized digital governance, forming a self-incentivized ecosystem that is collaboratively built, shared, and governed by the community. It provides a fou...
  </details>

- **2026-09-02** — Jiska Beuk, Gerasimos Spanakis — [WinoQueer-NL: Assessing Bias in Dutch Language Models toward LGBTQ+ Identities](http://arxiv.org/abs/2609.02651v1)
  <details><summary>📄 Abstract</summary>
  While English language models have been widely examined for anti-queer bias, Dutch models remain understudied. To address this gap, we developed a culturally and linguistically adapted Dutch dataset based on the English WinoQueer benchmark, containing pairs of stereotypical and counter-stereotypical sentences. To validate and expand it, we conducted an online survey with 43 Dutch queer participants, confirming 145 of 171 stereotypes as culturally relevant and identifying 22 new biases through fr...
  </details>

- **2026-09-02** — E. I. Makarenko, A. V. Ivlev, S. Bialy et al. — [Can diffuse X-rays be important in driving photoionisation in molecular clouds?](http://arxiv.org/abs/2609.02648v1)
  <details><summary>📄 Abstract</summary>
  The ionisation balance in molecular clouds is regulated by several ionising sources, including cosmic rays, X-rays, and ultraviolet radiation. Their relative importance depends on the local physical conditions and on the shielding column density. We compute the contribution of the large-scale diffuse X-ray radiation field to the ionisation in molecular clouds in the absence of strong local X-ray sources, such as young stars. Our goal is to quantify its significance relative to the Galactic cosmi...
  </details>

- **2026-09-02** — Gabriel Stefan, Sergiu Nisioi — [PolERo: Studying Political Evasion in Romanian](http://arxiv.org/abs/2609.02391v1)
  <details><summary>📄 Abstract</summary>
  Political evasion refers to responses that engage with a question while withholding the requested information. Recent NLP work frames political evasion as a classification task using a two-level taxonomy of response clarity and fine-grained evasion strategies. Existing work on response clarity and evasion classification is limited to English, leaving open whether the taxonomy and model behavior transfer across languages and political contexts. We introduce PolERo, a dataset of 3,574 human-annota...
  </details>

- **2026-09-01** — Himil Vasava, Ming Jiang — [Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation](http://arxiv.org/abs/2609.01604v1)
  <details><summary>📄 Abstract</summary>
  LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline that produces paired clean and corrupt summaries with controlled error intensity and explicit token-l...
  </details>

- **2026-09-01** — Kshitij Tayal, Arun Sharma, Genta Indra Winata et al. — [The Rise of Verbal Reinforcement Learning](http://arxiv.org/abs/2609.01597v1)
  <details><summary>📄 Abstract</summary>
  Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{La...
  </details>

- **2026-09-01** — Nicolò Alessandro Girardini, Unchitta Kan, Eduardo López et al. — [Behavioral calibration of mobile-phone GPS data for population-representative analyses](http://arxiv.org/abs/2609.01042v1)
  <details><summary>📄 Abstract</summary>
  Mobile phone mobility data have transformed the study of human behavior, but demographic and behavioral biases can compromise their representativeness and distort population-level inference. Existing calibration approaches primarily address demographic and geographic representativeness, leaving behavioral discrepancies largely uncorrected. Here we introduce the Behavioral Population (BePop) framework, which jointly calibrates mobility data to representative demographic and behavioral distributio...
  </details>

- **2026-09-01** — Elizaveta Sivak, Emily M. Cantrell, Thomas Emery et al. — [Births are difficult to predict even with rich survey and full-population register data](http://arxiv.org/abs/2609.01194v1)
  <details><summary>📄 Abstract</summary>
  Major life events have proven difficult to predict. Does this reflect limits of theory, data, and algorithms, or the large role of chance? We examine one outcome - having a child within three years - through a near-ideal setting for prediction: a data challenge where 147 researchers predicted births for Dutch residents aged 18-45, using survey data and full-population registers. Methods ranged from logistic regression to a large language model and transformers. Predictions were moderately accura...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 136 papers

- **2026-09-03** — Jungmin Park, Eunha Kim, Wooseop Kim et al. — [AI-Assisted Design of a Post-Quantum Cryptographic Accelerator: A Deployed-Silicon Case Study](http://arxiv.org/abs/2609.04058v1)
  <details><summary>📄 Abstract</summary>
  Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely. The standard acceptance gate cannot detect an entire class of ML-DSA defects. Signing resamples until a candidate meets its norm bounds, so the executed path varies with the message, whereas known-answer tests (KATs) sample fixed values and reach only the depths their seeds trigger. Our accelerator passed its full KAT regression while carrying a norm check that outran block...
  </details>

- **2026-09-03** — Yingxiang Yang, Weihang Xiao, Ben Bullough et al. — [Toward Frontier-Quality Declarative UI Generation at Small-Model Cost](http://arxiv.org/abs/2609.04184v1)
  <details><summary>📄 Abstract</summary>
  Declarative UI protocols such as A2UI let applications generate interactive UIs by selecting pre-built components from a catalog and binding their props to application data, rather than emitting frontend code from scratch. This contract is attractive for production systems because of safety and consistency. An open question is: can low-latency and low-cost small models achieve the required quality for A2UI-based UI generation? To answer this, we systematically study three controllable design cho...
  </details>

- **2026-09-03** — Joseph Lee, Yidi Huang, Dokyoon Kim et al. — [Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views](http://arxiv.org/abs/2609.04180v1)
  <details><summary>📄 Abstract</summary>
  Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary for acquisition and clarify that paraphrasing helps only at smaller batch sizes. Second, holding the token budget fixed, allocating tokens from document repetition to auxiliary views improves learning...
  </details>

- **2026-09-03** — Ruoyu Yao, Yusen Xie, Qingzhao Liu et al. — [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](http://arxiv.org/abs/2609.04070v1)
  <details><summary>📄 Abstract</summary>
  Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion execution. We first design an action tokenizer based on a residual vector-quantized variational autoencoder (VQ-VAE), capturing vehicle kinematic...
  </details>

- **2026-09-03** — Junyan Ye, Wei Liu, Dongzhi Jiang et al. — [Editable Visual Design](http://arxiv.org/abs/2609.04034v1)
  <details><summary>📄 Abstract</summary>
  While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets.   To address this, we propose Editable Vis...
  </details>

- **2026-09-03** — Yibin Wang, Zehan Wang, Junshu Tang et al. — [WorldReward: Reward Modeling for Camera-Conditioned World Models](http://arxiv.org/abs/2609.03952v1)
  <details><summary>📄 Abstract</summary>
  Camera-conditioned world models generate interactive videos in which commanded actions should induce the expected scene changes while appearance, geometry, and temporal dynamics remain coherent. Existing rewards assess these requirements separately: geometry-based rewards estimate trajectory execution but cannot judge the visual quality of the executed motion, whereas image-based rewards measure frame quality without capturing action execution or temporal dynamics. We posit that a vision-languag...
  </details>

- **2026-09-03** — Hyun Bin Park, Du-Seong Chang — [Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO](http://arxiv.org/abs/2609.03941v1)
  <details><summary>📄 Abstract</summary>
  RL-based post-training for reasoning models is increasingly bottlenecked by repeated fresh rollout generation, particularly in agentic settings where environment interaction dominates wall-clock cost. Replay can reduce this burden by reusing past trajectories, but existing methods typically embed it within larger training pipelines involving exploration, experience restructuring, or mixed-policy optimization. This makes replay's own contribution difficult to isolate. We ask a focused question: h...
  </details>

- **2026-09-03** — Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel et al. — [Sparse auto-regressive modeling for scene generation from multi-view images](http://arxiv.org/abs/2609.03931v1)
  <details><summary>📄 Abstract</summary>
  Generating complete 3D scenes from sparse, unconstrained views is a fundamental challenge in 3D vision which requires reasoning beyond observed content while remaining computationally tractable. Existing feed-forward reconstruction methods are inherently limited to content visible in the input images, while 3D generative modeling is hindered by the high computational cost of dense volumetric representations and the scarcity of large-scale 3D supervision. We introduce SPAR3S, a sparse voxel-align...
  </details>

- **2026-09-03** — Linke Song, Wenhao Wang, Weijie Liu et al. — [NACRE: Rethinking Confidential Containers through Native Architectural Support](http://arxiv.org/abs/2609.03849v1)
  <details><summary>📄 Abstract</summary>
  Linux containers achieve high density and fast lifecycle operations by sharing the host kernel, but this design also lets a compromised host inspect or modify container state. Existing   confidential-computing systems protect an enclave address space or an entire guest operating system, while recent container-granularity systems still add a separate protection context.   These abstractions do not make a dynamic group of host-managed Linux processes the architectural protection unit.   This paper...
  </details>

- **2026-09-03** — Tommaso Soru — [Semantic Bayesian World Models](http://arxiv.org/abs/2609.03834v1)
  <details><summary>📄 Abstract</summary>
  Knowledge graphs describe reality in crisp assertions, while the systems now consuming them, foundation models and autonomous agents, reason natively in probabilities. We argue that this mismatch is why the integration of language models and knowledge graphs remains a data-feeding pipeline rather than a unified reasoning architecture. We envision Semantic Bayesian World Models (SBWMs): a Web that describes the world not as a database of facts but as a shared, evolving fabric of beliefs over know...
  </details>

- **2026-09-03** — Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono — [A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval](http://arxiv.org/abs/2609.03788v1)
  <details><summary>📄 Abstract</summary>
  Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions w...
  </details>

- **2026-09-03** — Anh Danh, Rick Nouwen, Massimo Poesio — [A Circuit for Plural Reference: How LLMs Represent and Retrieve Singular and Plural Entities](http://arxiv.org/abs/2609.03687v1)
  <details><summary>📄 Abstract</summary>
  Coreference resolution is an important task in contextual reasoning. In this paper, we investigate the mechanism for representing and retrieving singular and plural entities for plural reference. We use a combination of mechanistic interpretability and attention pattern analysis to study the process in which LLMs predict a pronoun to refer back to previously mentioned entities. Using a range of causal intervention techniques, we find a set of attention heads that are responsible for (1) represen...
  </details>

- **2026-09-03** — Yaxing Lyu, Shengjie Zhou, Binbin Toh et al. — [KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents](http://arxiv.org/abs/2609.03588v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly act through tools, they must reconcile user instructions, parametric knowledge, and dynamic environmental observations before taking actions. We introduce KC-Bench, a controlled multi-turn benchmark for measuring this capability across world-knowledge conflicts, input inconsistencies, and multi-source temporal conflicts. Its 238 tasks are manually screened from more than 1,000 generated candidates and combine a user simulator, stateful tools, deterministic environment assert...
  </details>

- **2026-09-03** — Hyunseo Oh, Chong-Kwon Kim, Yoonhyuk Choi — [When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA](http://arxiv.org/abs/2609.03454v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) can improve the specificity and grounding of large language model responses, but its effect is not uniformly beneficial in single-turn mental-health question answering, where user queries often combine emotional distress, treatment concerns, and safety-sensitive needs. We study when retrieval helps or hurts mental-health QA, and whether a lightweight selective retrieval policy can better control this trade-off. We operationalize retrieval need using three dra...
  </details>

- **2026-09-03** — Zhaoyuan Huang, Tianjie Ju, Pengzhou Cheng et al. — [Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents](http://arxiv.org/abs/2609.03438v1)
  <details><summary>📄 Abstract</summary>
  Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: ...
  </details>

- **2026-09-03** — Puneet Mathur, Dinesh Manocha — [DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following in Full-Duplex Voice Agents](http://arxiv.org/abs/2609.03423v1)
  <details><summary>📄 Abstract</summary>
  Full-duplex voice agents must continuously decide when to listen, backchannel, interrupt, handle speech overlaps, take the floor, and yield. Existing benchmarks largely test these behaviors through explicit turn-management instructions, while deployed agents are often configured through roles or personas from which the appropriate conversational behavior must be inferred. We introduce DuplexSpeechBench-IFEval (DSB-IFEval) for evaluating implicit instruction-following in real-time spoken interact...
  </details>

- **2026-09-03** — Evan Chen, Shiqiang Wang, Christopher G. Brinton — [Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory](http://arxiv.org/abs/2609.03340v1)
  <details><summary>📄 Abstract</summary>
  Distributed LLM-agent teams can read the latest shared facts and still act on an obsolete plan. A planner may derive an action from requirement $r_3$, another agent may commit $r_4$, and an executor may receive $r_4$ without replacing the plan derived from $r_3$. We call this \emph{stale-plan execution}: state freshness does not establish that the plan authorizing an action remains valid. We introduce PlanFence, a dependency-scoped action-validation protocol. Plans cite the exact public records ...
  </details>

- **2026-09-03** — Jiayuan Ma, Yuqi Lu, Weiyang Guo et al. — [FPCO-Dialog: A Multi-Turn False-Premise Benchmark for Correction and Cooperation in Vision-Language Models](http://arxiv.org/abs/2609.03331v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly deployed in multi-turn settings where users may describe visual content with incorrect assumptions. Yet existing evaluations rarely isolate how models respond when the same visually grounded false premise persists across dialogue turns. We introduce FPCO-Dialog, a benchmark for evaluating correction and cooperation behavior in VLMs under repeated false premises. FPCO-Dialog contains 1,080 images and 10,800 question turns, stratified by visual comple...
  </details>

- **2026-09-03** — Zeyu Liu, Souvik Kundu, Peter A. Beerel — [Speculative Macro Commit for Faster Tool-Using Agents](http://arxiv.org/abs/2609.03236v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents spend wall-clock time not only on model inference but also in serial action--observation turns, where each tool call, environment transition, and observation can delay subsequent decisions. We introduce \textbf{Speculative Macro Commit} (SMC), a runtime mechanism for a two-tier agent system: a large authoritative actor model produces the official trajectory, while a faster speculative drafter model continuously predicts and executes future action chains on an isolated envir...
  </details>

- **2026-09-03** — Jannatul Shefa, Alejandro Salado, Paul Wach et al. — [Two Truths and A Lie? Benchmarking Off-the-Shelf LLMs for Requirements Quality Assessment: Performance, False Alarms, and Misses](http://arxiv.org/abs/2609.03230v1)
  <details><summary>📄 Abstract</summary>
  Requirements engineering (RE) governs the quality of everything downstream in systems engineering (SE); defective requirements that survive review cycles propagate into design rework, schedule delays, and cost overruns. Because requirements are often written in natural language, recent advances in generative AI have raised expectations that large language models (LLMs) can absorb requirement quality assessment, a task otherwise slow and human expertise-intensive. Yet empirical evidence on whethe...
  </details>

- **2026-09-03** — Yutian Zhang, Siyuan Ma, Liwen Yang et al. — [FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation](http://arxiv.org/abs/2609.03889v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabilize the robot, it cannot distinguish task-relevant interaction forces from forces induced by external disturbances during manipulation. Althoug...
  </details>

- **2026-09-03** — Hongliang Yang, Yanjing Xu, Anhang Zhang et al. — [ReRoom: Blending Virtual and Physical Contexts for In Situ Room Planning in Mixed Reality](http://arxiv.org/abs/2609.03596v1)
  <details><summary>📄 Abstract</summary>
  Planning a real domestic space is an in situ authoring process: users evaluate candidate layouts at true scale, refine their intent, and carry accepted decisions into later iterations. Existing approaches either separate layout editing from the physical room or provide limited support for evaluating and refining whole-room proposals in situ. We present ReRoom, a mixed-reality system for in situ room-layout authoring. ReRoom presents a shared layout state through a virtual room proxy spatially re...
  </details>

- **2026-09-03** — Shruti Kulkarni, Lynn Tong, Aditi Namboodiripad et al. — [Multilingual Agent System for Inclusive Wildfire Evacuation Guidance](http://arxiv.org/abs/2609.03301v1)
  <details><summary>📄 Abstract</summary>
  Wildfire seasons have become 84 days longer in the current days than in the 1970s, causing enormous threats to one's financial status and short- and long-term health. During the fire, public agencies send out emergency messages to provide warnings and orders. Although 26 million people in the US have limited English proficiency, over 80% of those messages are only delivered in English, which can cause disproportionate information distribution and awareness. In order to better serve marginalized ...
  </details>

- **2026-09-03** — Kevin Du, Alexander Hoyle, Laura Ruis et al. — [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](http://arxiv.org/abs/2609.04194v1)
  <details><summary>📄 Abstract</summary>
  Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, evaluate faithfulness, and provide step-level supervision via process reward models and generative critics. These practices rely on the text of a reasoning step carrying information about its functional role. But does the text actually encode information about which reasoning steps matter? We operat...
  </details>

- **2026-09-03** — Shashaank Khanna, Matthew F. Pusey, Roger Colbeck — [Spurious quantum correlations](http://arxiv.org/abs/2609.04157v1)
  <details><summary>📄 Abstract</summary>
  In his seminal paper, Bell [Physics Physique Fizika 1, 195 (1964)] considers the correlations that result from space-like separated measurements on a pair of entangled particles. He uses relativity theory to motivate the Bell causal structure, then shows the existence of quantum correlations that cannot be explained classically within this causal structure. Classical explanations of such quantum correlations are possible in alternative causal structures, for instance, those that allow superlumin...
  </details>

- **2026-09-03** — Michele Viscardi, Lorenzo Leone, Alioscia Hamma — [Non-local Magic: closed-form solution and equivalence with magic of purification](http://arxiv.org/abs/2609.04119v1)
  <details><summary>📄 Abstract</summary>
  Non-local magic quantifies the non-stabilizerness of a bipartite quantum state that cannot be removed by local unitary transformations. Despite its natural definition, its evaluation generally requires a difficult optimization over local unitaries. Here, we show that for the log-stabilizer fidelity this optimization admits an exact closed-form analytic solution depending only on the Schmidt spectrum. We then introduce the magic of purification, defined as the minimum pure-state magic over all pu...
  </details>

- **2026-09-03** — Sergii Kozyrev, Davyd Maiboroda — [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](http://arxiv.org/abs/2609.04098v1)
  <details><summary>📄 Abstract</summary>
  Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and write-strength gates -- on the intuition that errors in a recurrence accumulate over long contexts. We test that intuition by building Minima: NVFP4 W4A4 on all 496 linear layers, GDN i...
  </details>

- **2026-09-03** — Hasan Alkhder, Mohammad Abboush, Igor Tchappi et al. — [Translation as a Decision Space: A Multi-Agent Perspective on Low-Resource Dialect Generation](http://arxiv.org/abs/2609.04048v1)
  <details><summary>📄 Abstract</summary>
  Neural machine translation (NMT) systems typically produce a single output per input, obscuring the alternative decision trajectories implicitly available within multilingual decoding. This opacity becomes particularly problematic in low-resource dialect settings, where multiple linguistically valid realizations may differ in lexical authenticity, register, and structural stability. We propose reframing translation as a structured decision space explored by autonomous translation agents. Instead...
  </details>

- **2026-09-03** — Susmita Bhattacharjee, Himashri Deka, H. S. Shekhawat et al. — [Fairness Evaluation of Edge-AI Implementation for Cleft Lip and Palate Speech ASR](http://arxiv.org/abs/2609.03982v1)
  <details><summary>📄 Abstract</summary>
  Automatic speech recognition (ASR) remains challenging for individuals with cleft lip and palate (CLP) because of limited pathological speech data and large variations in speech characteristics across speakers and severity levels. These recognition difficulties can reduce the accessibility of voice-based human-computer interaction, particularly when cloud-based ASR services are unavailable or unreliable. This work investigates a severity-aware and edge-deployable ASR framework for improving reco...
  </details>

- **2026-09-03** — Nizam Kadir, Wei Ting Liow, Sumbul Khan et al. — [From Misconceptions to Evidence: What Science Teachers Make Visible When Co-Designing Agentic Learning Apps](http://arxiv.org/abs/2609.03917v1)
  <details><summary>📄 Abstract</summary>
  Science educators increasingly encounter AI tools that generate content, yet disciplinary teaching depends on eliciting learners' models, diagnosing misconceptions, interpreting evidence, and preserving professional judgment. This study asks how science teachers translate such epistemic work into specifications for agentic learning applications. It contributes to the conference theme, "Innovating Pedagogies, Inspiring Minds: Transforming Science Learning," and the Teachers' Professional Learning...
  </details>

- **2026-09-03** — Junqing Du, Fernando Ropero, Erkin Turkoz et al. — [GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs](http://arxiv.org/abs/2609.03892v1)
  <details><summary>📄 Abstract</summary>
  3D spatial reasoning underpins understanding and acting in the physical world, yet it remains unreliable in current multimodal large language models (MLLMs). These models falter at precise geometric measurement, at transforming between egocentric and allocentric viewpoints, and at grounding fine-grained appearance. The most common remedies fine-tune the model on large-scale curated spatial-reasoning datasets or attach dedicated encoders for 3D geometry, which typically couples the solution to co...
  </details>

- **2026-09-03** — Mark Solms, St John Grimbly, Bruce Bassett et al. — [Inferring Affective Consciousness in an Artificial Agent: A Case Study](http://arxiv.org/abs/2609.03883v1)
  <details><summary>📄 Abstract</summary>
  Creatures that display 'hedonic place preference behaviour' are thought by many scientists to experience feelings, on the assumption that their attraction to pleasure-producing substances which lack nutritional value (e.g. cocaine, morphine) cannot easily be attributed to unconscious instinctual behaviour. In this paper, we discuss how a simple artificial agent that instantiates attributes of an affective system engaging in felt uncertainty about its intrinsic needs in relation to environmental ...
  </details>

- **2026-09-03** — Lei Zheng, Liping Yang, Zihao Li et al. — [Adapting to Evolving Requirements: Agentic AI for Retail Supply Chain Operations](http://arxiv.org/abs/2609.03860v1)
  <details><summary>📄 Abstract</summary>
  Retail supply chain operations rely on coupled decision modules that must adapt as requirements evolve. LLMs offer a natural-language interface for this task, but existing methods primarily focus on individual optimization models. Extending them to heterogeneous decision pipelines is challenging because a requirement may admit multiple intervention paths with different downstream effects. We formulate requirement-driven adaptation as the joint selection of an intervention route and an admissible...
  </details>

- **2026-09-03** — Yizhou Xu, Margarita Sagitova, Lenka Zdeborová et al. — [High-Dimensional Learning Dynamics of Attention-Indexed Models](http://arxiv.org/abs/2609.03858v1)
  <details><summary>📄 Abstract</summary>
  Attention mechanisms are central to modern foundation models, yet their training dynamics remain poorly understood, especially when the attention matrices have extensive rank. In this work, we study attention-indexed models, a broad framework that can represent multi-layer and multi-head attention architectures. First, we show that, in a suitable high-dimensional limit, the population-loss landscape is characterized by a finite set of trace order parameters. In contrast, online stochastic gradie...
  </details>

- **2026-09-03** — Federico Putamorsi, Leonardo Zini, Marcella Cornia et al. — [SPARK: Input-Conditioned Sparse Activation Modulation for Frozen DiT-based Super-Resolution](http://arxiv.org/abs/2609.03813v1)
  <details><summary>📄 Abstract</summary>
  Real-world image super-resolution (SR) increasingly relies on Diffusion Transformer (DiT) backbones, whose internal activations can be dominated by a small number of massive channels. Yet improving perceptual quality in these models still typically requires fine-tuning the network or attaching additional adapters, leaving this structured activation space largely unexplored for adaptation. We investigate whether dominant channels can instead serve as a compact adaptation interface for frozen DiT-...
  </details>

- **2026-09-03** — Qianwen Wang, York Hay Ng, Aditya Khan et al. — [Typological Feature Prediction with Large Language Models: An In-Context Learning Approach](http://arxiv.org/abs/2609.03775v1)
  <details><summary>📄 Abstract</summary>
  Typological features are widely used in multilingual NLP, and the prediction of such features holds downstream utility. However, existing methods to predict missing values lack interpretable justifications for predictions, while their performance across resource levels and feature types remains underexplored. Given LLMs' abilities in meta-linguistic reasoning and in providing rationales, we investigate LLMs' performance in typological feature prediction via an in-context learning approach with l...
  </details>

- **2026-09-03** — Alexander Shekhovtsov, Georgy Sokolov, Mikhail Cherniavskii et al. — [Nearly Tight Bounds for Proportional Group Fair Divisions and One-Sided Discrepancy](http://arxiv.org/abs/2609.03682v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the problem of fair division of indivisible goods among $k$ groups of $n_1,\ldots, n_k$ agents. We look at the worst downward deviation $\textit{PROP}(n_1,\ldots, n_k)$ of an agent in a group from its $1/k$-share. We improve the bounds of (Manurangsi and Meka, 2026) and show that $\textit{PROP}(n_1,\ldots, n_k) = \tildeΘ(\sqrt{n/k})$, where $n = n_1 + \ldots + n_k$ is the total number of agents.   For the proof of the upper bound, we develop novel discrepancy-type tools and, i...
  </details>

- **2026-09-03** — David Milec, Spyridon Samothrakis, Michael Fairbank et al. — [Local Updates, Global Learning (LUGL): Playing Games with non-incremental Learners](http://arxiv.org/abs/2609.03660v1)
  <details><summary>📄 Abstract</summary>
  The dominance of Neural Networks (NNs) in RL is partially due to their incremental learning capability, which naturally suits the online, non-stationary nature of self-play training. However, gradient-boosted trees like LightGBM are widely recognised as the state of the art for tabular data in supervised learning, often outperforming NNs in accuracy and efficiency. Game states are inherently tabular---discrete actions, categorical card identities, structured board positions---which makes them an...
  </details>

- **2026-09-03** — Baihua Gong — [Finite-temperature mass gap and quench dynamics of mobile impurities in a Fermi gas](http://arxiv.org/abs/2609.03656v1)
  <details><summary>📄 Abstract</summary>
  Recently, a mass-gap description of mobile impurities in a Fermi gas was introduced, which connects Anderson's orthogonality catastrophe for static impurities to the quasiparticle picture of Fermi polarons through a recoil-induced energy gap in the fermionic dispersion. That description, however, was restricted to zero temperature and did not address dynamics. Here we generalize the mass-gap model to finite temperature by combining the Lee--Low--Pines transformation with a self-consistent Hartre...
  </details>

- **2026-09-03** — Mia MacGregor, Aakash Welgamage Don, Mark Bartlett — [Analysis of Prompt Engineering for Drug Toxicity Prediction](http://arxiv.org/abs/2609.03635v1)
  <details><summary>📄 Abstract</summary>
  Clinical trials in the UK can cost up to £1.3 million, with approximately 90% drug failure rate. Toxicity is a major contributing factor in drug failure. Testing is time and cost intensive. In recent years, the use of artificial intelligence has been increasingly explored to aid in the prediction of drug toxicity, with extensive use of large language models (LLMs). However, LLMs can show considerable variation when minor changes are made to prompts, which raises concerns about their sensitivity ...
  </details>

- **2026-09-03** — Xiangyu Wang, Jin Wu, Xiaoyu Li et al. — [Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks](http://arxiv.org/abs/2609.03432v1)
  <details><summary>📄 Abstract</summary>
  Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bias. Such limitations are particularly evident in Contextually-Grounded and Procedurally-Structured Tasks (CGPST), a complex multi-step creativity task where inter-step dependencies, highly subjectivity, and wide scoring ranges lead to more unstable and biased judgments. Existing approaches either rely on task-specific training or directly apply LL...
  </details>

- **2026-09-03** — Heng Wang, Jielin Qiu, Wenting Zhao et al. — [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](http://arxiv.org/abs/2609.03430v1)
  <details><summary>📄 Abstract</summary>
  Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck. Existing KV cache compression methods share one paradigm: score each cached token by some estimate of how much it will matter later, and keep the top-scoring ones. We show that the selection signal contributes almost nothing. Random Attention keeps the prompt and evicts uniformly at random within each attention head, computing no sc...
  </details>

- **2026-09-03** — Chumeng Jiang, Jiayin Wang, Xinjie Lin et al. — [SelfDR: Self-Distillation from Reasoning for LLM-Based Recommendation](http://arxiv.org/abs/2609.03313v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have recently emerged as powerful backbones for recommendation. To better elicit their capabilities, reasoning has been widely incorporated to help LLMs interpret rich textual signals and improve recommendation accuracy. However, explicitly generating intermediate reasoning traces often incurs substantial computational costs, which limits practical deployment in real-world recommender systems. To address this challenge, we propose SelfDR, a Self-Distillation from Rea...
  </details>

- **2026-09-03** — Ucchwas Talukder Utsha, Sakib Mostafa, James Zou et al. — [Language-encoded network topology enables large language models to reason about complex networks](http://arxiv.org/abs/2609.03229v1)
  <details><summary>📄 Abstract</summary>
  Networks describe systems in biology and beyond, from protein interactions and social relationships to power grids and citation records. Reasoning about such systems requires understanding their structure: which elements are central, which connections bridge separate communities, and how it changes when elements are removed. Although large language models (LLMs) excel at natural language, they struggle with such questions when networks are given as edge lists, sentences or measurement tables, be...
  </details>

- **2026-09-02** — Shunji Matsuura, Sonika Johri — [Discretization-Aware Fine-Tuning for Quantum Machine Learning with Chemical Foundation Models](http://arxiv.org/abs/2609.03220v1)
  <details><summary>📄 Abstract</summary>
  A key challenge in practical quantum machine learning (QML), particularly for discriminative tasks such as classification, is the limited capacity of near-term quantum devices to encode high-dimensional classical data into small quantum registers. In optimized basis-encoded (bit-bit) settings, this constraint leads to cross-class collisions, where samples with different labels are mapped to the same discrete bit-string and thus become indistinguishable to any downstream model. In this work, we i...
  </details>

- **2026-09-02** — Wooyoung Jung, Prosper Babon-Ayeng — [Large Language Model-Driven Context-Aware Eco-Feedback Generation and Evaluation](http://arxiv.org/abs/2609.02719v2)
  <details><summary>📄 Abstract</summary>
  The objective of this study is to demonstrate the potential of generating context-aware eco-feedback - eco-feedback that reflects a household's contextual characteristics alongside its energy use patterns - through a large language model-integrated framework. Previous studies have introduced personalized eco-feedback, mostly relying on household energy use patterns; however, they frequently did not reflect distinct household characteristics, including their persona or non-negotiable routines, le...
  </details>

- **2026-09-02** — Mengzhe Geng — [VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis](http://arxiv.org/abs/2609.03203v1)
  <details><summary>📄 Abstract</summary>
  Expressive speech systems make a decision before any waveform is rendered: how an utterance is delivered. In dialogue agents, narration, and role-conditioned TTS, that hidden planning step sets affect, pitch, energy, rate, pause, emphasis, and stance, yet downstream audio scores rarely reveal whether those choices were licensed by the source record, a source-use failure that occurs before any waveform exists. VoxReason makes that pre-synthesis decision measurable as a listener-free task for sour...
  </details>

- **2026-09-02** — Rohith Reddy Bellibaltu, Manpreet Singh, Deepak Parashar et al. — [Counterfactual Fairness Audits of Multi-Step Clinical LLM Agents Require a Measured Per-Action Instability Floor](http://arxiv.org/abs/2609.03221v1)
  <details><summary>📄 Abstract</summary>
  Counterfactual audits are the standard tool for checking whether a clinical agent treats demographically distinct but clinically identical patients differently. They report a flip rate: how often an action changes when only the patient descriptor changes. We show that this quantity is uninterpretable on its own. Re-running an identical condition ten times over sixteen vignettes (same narrative, same descriptor string, nothing varied) moved a clinical agent's action in 8.7% of outcome-vignette ce...
  </details>

- **2026-09-02** — Ahmed Asaad, Amr Mohamed, Yang Zhang et al. — [The Analyst in the Prompt: Role, Retrieval, and Memory Biases in LLM Financial Analysis](http://arxiv.org/abs/2609.03218v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly use user context such as memory, profiles, and role prompts to personalize their responses. This personalization can affect evidence-based judgment: the same evidence may lead to different conclusions under different user contexts. Finance provides a high-stakes setting to study this problem because decisions often depend on interpreting long and complex documents. We test this using 3,575 SEC filings across twelve LLMs. We compare persona-conditioned re...
  </details>

- **2026-09-02** — MasterControl AI Lab — [MasterControl Seventeen Every Time](http://arxiv.org/abs/2609.03209v1)
  <details><summary>📄 Abstract</summary>
  We study a governed approach to enterprise analytics: a language model interprets the question, while deterministic policy selects and runs a pre-approved analytical program that returns both results and evidence. We show that this restriction can remain expressive within a defined analytical class, using relational operations plus aggregation, comparison, windows, ranking, and similarity. Fixed meaning, policy, data, and execution rules also make results replayable. Across 440 runs, three 8B mo...
  </details>

- **2026-09-02** — Shuichi Furuya, Atsushi Fujimura — [Beyond Dose in Boron Neutron Capture Therapy: Cellular $^{10}$B-Capture Statistics and Microdosimetric Context in Effect Prediction](http://arxiv.org/abs/2609.03130v1)
  <details><summary>📄 Abstract</summary>
  Boron neutron capture therapy (BNCT) produces high-linear-energy-transfer, short-range particles through the $^{10}$B(n,$α$)$^{7}$Li reaction. Conventional descriptors, including absorbed dose, compound biological effectiveness (CBE)-weighted dose, and photon-isoeffective dose ($D_{\mathrm{isoE}}$), remain clinically useful but compress cellular heterogeneity, compartmental boron localization, and stochastic reaction occurrence into macroscopic summaries. We propose a hierarchical framework that...
  </details>

- **2026-09-02** — Toni J. B. Liu, Jiajun Bao, Yizhou Liu et al. — [The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors](http://arxiv.org/abs/2609.02959v1)
  <details><summary>📄 Abstract</summary>
  What does a language model predict when it has few clues? The answer lurks in its unembedding geometry: a single direction of the unembedding matrix encodes the unigram distribution of the training corpus, which serves as the Bayesian prior the model falls back on when uncertain. This structure --- which we term the \emph{direction of ignorance} --- appears in all four model families examined (\texttt{Llama}, \texttt{Qwen}, \texttt{Gemma}, and \texttt{Pythia}), ranging from 0.4B to 405B paramete...
  </details>

- **2026-09-02** — Zhiyang Ding, Yang Luo, Guangpu Chen et al. — [ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use](http://arxiv.org/abs/2609.02690v1)
  <details><summary>📄 Abstract</summary>
  Remote Model Context Protocol (MCP) services enable large language model agents to invoke external tools, but OAuth authorization alone does not ensure that a later tool call is executed by the provider-side workload that the relying party intended to trust. An endpoint may remain authorized even after execution shifts to a substituted workload, relies on stale appraisal state, reuses authority transferred from another sender, or traverses an undeclared downstream component. We call this problem...
  </details>

- **2026-09-02** — Anjali Sarvaiya, Shubh Kawa, Lalit Agrawal et al. — [UnCapsTSR: An Unsupervised Transformer-based Image Super-Resolution Approach for Capsule Endoscopy Images](http://arxiv.org/abs/2609.02476v1)
  <details><summary>📄 Abstract</summary>
  Wireless Capsule Endoscopy (WCE) captures and streams video while passing through a patient's Gastrointestinal (GI) tract and is used to examine its irregularities. Although advantageous over conventional endoscopy, WCE suffers from limitations related to capsule size and wireless transmission, resulting in images with coarser resolution. This work presents UnCapsTSR, an unsupervised transformer-based Generative Adversarial Network (GAN) framework for improving the spatial resolution of Low-Reso...
  </details>

- **2026-09-02** — Shachar Don-Yehiya, Leshem Choshen, Omri Abend — [User Feedback Provides a Unique Signal that LLMs Can not Detect](http://arxiv.org/abs/2609.02859v1)
  <details><summary>📄 Abstract</summary>
  Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy and difficult to leverage effectively. We challenge this conception by demonstrating that user feedback is a highly actionable signal for improvement, and that its perceived ineffectiveness stems from a systematic bias in current evaluation paradigms. To isolate the usefulness of feedback, we construc...
  </details>

- **2026-09-02** — Wooyoung Jung, Prosper Babon-Ayeng — [Large Language Model-Driven Context-Aware Eco-Feedback Generation and Evaluation](http://arxiv.org/abs/2609.02719v1)
  <details><summary>📄 Abstract</summary>
  The objective of this study was to demonstrate the potential of generating eco-feedback that accounted for unique household contextual information, named as context-aware eco-feedback, through a large language model-integrated framework. Previous studies have introduced personalized eco-feedback, mostly relying on household energy use patterns; however, they frequently did not reflect distinct household characteristics, including their persona or non-negotiable routines, leaving eco-feedback ine...
  </details>

- **2026-09-02** — Johannes Brachem, Thomas Kneib — [Reconciling Interpretability with Covariate-Dependent Shape Flexibility in Penalized Transformation Models for Distributional Regression](http://arxiv.org/abs/2609.02662v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in distributional regression is to allow the shape of the conditional distribution of the response variable to vary flexibly with covariates while retaining directly interpretable effects on its mean and standard deviation. We extend the penalized transformation model (PTM) family into a conditional-shape PTM, which assigns separate structured additive predictors to the conditional mean, standard deviation, and standardized distributional shape beyond location and scale. A co...
  </details>

- **2026-09-02** — Chengxiao He, Shanghai Yuan, Liuqun Fan et al. — [A Physics-Consistent Benchmark for Contact-Rich Human-Robot Interaction in Assistive Care](http://arxiv.org/abs/2609.02402v1)
  <details><summary>📄 Abstract</summary>
  Conventional task-level evaluation asks whether a robot policy completes a specified action, but can miss failures that emerge only during physical human contact. This limitation is critical in contact-rich assistive tasks, where meaningful evaluation requires a physically responsive human, interaction-quality assessment beyond task success, and a leak-free observer-scorer protocol. We introduce a physics-consistent benchmark for contact-rich human-robot interaction, instantiated in robot-assist...
  </details>

- **2026-09-02** — Menghao Li, Linjie Mu, Yin Wang et al. — [CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction](http://arxiv.org/abs/2609.02401v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive vision language models unify heterogeneous perception tasks but are highly susceptible to compounding errors. On-policy distillation (OPD) bridges the training-inference mismatch by training students on their own rollouts. However, unreliable student predictions, especially early in training, can derail the trajectory and degrade the quality of teacher supervision. While recent interleaved distillation methods allow the teacher to verify and replace student tokens, they primarily ...
  </details>

- **2026-09-02** — Alexey Potapov — [AGI Maze Prediction Datasets: A Compact Benchmark for Learning World Dynamics with Transformers](http://arxiv.org/abs/2609.02339v1)
  <details><summary>📄 Abstract</summary>
  World modeling requires a predictive model to maintain and update an internal state adequate for reasoning about the consequences of actions. We introduce the AGI Maze Prediction Datasets and Benchmark, a lightweight controlled testbed for studying this capability in Transformers and other predictive models. Derived from procedurally generated, stateful grid worlds, the benchmark comprises per-step transition prediction, fixed-horizon state prediction, and sequential textual-observation predicti...
  </details>

- **2026-09-02** — Ihor Stepanov, Aleksandr Smechov, Mykhailo Shtopko et al. — [SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology](http://arxiv.org/abs/2609.02292v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level. However, inference endpoints can vary widely in quality, price, latency, context support, tool use, domain expertise, and reasoning behavior. This heterogeneity makes manual heuristics difficult to maintain and unlikely to achieve consistently f...
  </details>

- **2026-09-02** — Mingjie Zheng, Zihao Chen, Wenqing Chen et al. — [CoMerge: Conflict-Driven Preference Optimization for Multi-Task Model Merging](http://arxiv.org/abs/2609.02273v1)
  <details><summary>📄 Abstract</summary>
  Model merging provides an efficient paradigm for constructing multi-task large language models (LLMs) without full model retraining, yet it remains challenged by parameter interference. While existing methods aim to preserve the capabilities of individual expert models and mitigate interference, they generally do not directly learn from the potentially degraded behaviors exposed by naive merging. In this paper, we propose a conflict-driven preference optimization framework for model merging (CoM...
  </details>

- **2026-09-02** — Yunchi Yang, Longlong Li, Cunquan Qu — [PEARL: Path-Entity Aligned Relational Learning with Contextual Subgraphs for Inductive Knowledge Graph Completion](http://arxiv.org/abs/2609.02216v1)
  <details><summary>📄 Abstract</summary>
  Inductive knowledge graph completion (IKGC) aims to predict missing links involving entities unseen during training, requiring models to learn transferable relational and structural patterns. Existing subgraph- and path-based approaches often encode relational paths independently of their surrounding query subgraphs, although the predictive relevance of a path may vary across structural contexts. We propose PEARL, a Path-Entity Aligned Relational Learning framework that models paths as context-c...
  </details>

- **2026-09-02** — Hongshen Gou, Zuyu Zhang, Yuze Sun et al. — [Git4Data: Database-Native Version Control for AI Agents](http://arxiv.org/abs/2609.02106v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents increasingly explore many candidate states of relational data in parallel, each of which should remain isolated, reproducible, and auditable, preferably through the same SQL interface used for ordinary data work. Existing tools support this requirement only partially: source-code version control does not scale to large datasets, whereas relational databases manage large data efficiently but rarely expose native branching, comparison, and merging. We present Git4...
  </details>

- **2026-09-02** — Weifeng Jiang, Ruirui Chen, Qianren Mao et al. — [Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage](http://arxiv.org/abs/2609.02091v1)
  <details><summary>📄 Abstract</summary>
  Knowledge editing provides an efficient way to update factual knowledge in large language models. However, malicious edits may introduce safety risks, making it necessary to reverse undesirable editing effects. Existing reversal methods for parameter-modifying edits mainly focus on global removal, which may also erase beneficial edits that should be preserved. In this paper, we study selective reversal of edited knowledge, where the goal is to reverse targeted edited facts while preserving the r...
  </details>

- **2026-09-02** — Zheng Wang, Muchen Li, Renjie Liao et al. — [IDEEA: training-free Input-Dependent stEEring via Activation cluster matching](http://arxiv.org/abs/2609.02089v1)
  <details><summary>📄 Abstract</summary>
  Steering aligns large language models (LLMs) by injecting a bias into selected activations at inference time, offering a far cheaper alternative to weight-update methods such as supervised fine-tuning or reinforcement learning. However, most existing training-free steering methods are input-independent: a single direction is fitted once and shared across all inputs. This is fundamentally limiting as different inputs occupy different regions of the activation space and admit different optimal ste...
  </details>

- **2026-09-02** — Andrew Snowden — [Measures on partial orders](http://arxiv.org/abs/2609.02021v1)
  <details><summary>📄 Abstract</summary>
  We determine the measures (in the sense of Harman--Snowden) on the Fraïssé class of partially ordered sets: the space of measures is a union of a plane, eight lines, and 15 isolated points. This is the first case where the space is not equidimensional, and the first primitive case in which it has dimension at least two.   ChatGPT was used to obtain many arguments. The writing was done entirely by the author.
  </details>

- **2026-09-02** — Masahiro Kojima, Kentaro Takeda, Ying Yuan — [A staggered seamless dose-optimization design for co-developing monotherapy and combination therapy](http://arxiv.org/abs/2609.01954v1)
  <details><summary>📄 Abstract</summary>
  Contemporary oncology drug development increasingly requires efficient dose-optimization strategies that evaluate monotherapy (Mono) and combination therapy (Combo) while balancing activity, efficacy, and tolerability. We propose a staggered seamless phase I/II design for settings in which a novel agent is evaluated alone and in combination with an established therapy. In phase I, Mono dose finding begins first, and Combo subtrials can be opened adaptively once a prespecified combination-initiat...
  </details>

- **2026-09-02** — Yihang Chen, Yuxiang Chen, Yuxuan Huang et al. — [Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems](http://arxiv.org/abs/2609.02750v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems commonly use an orchestrator to decompose a task for a team of workers and then improve through textual reflection. Despite strong empirical results, these systems lack a unified account of coordination, memory improvement, and the role of external verification. We model orchestrator-worker interaction as a bilevel coordination game: under bounded coupling, the workers' local-update game is an approximate potential game whose equilibrium slack is controlled by decompositi...
  </details>

- **2026-09-02** — Song Zhou, Songge Zhang, Lanting Shi et al. — [Colossal reversible conductivity switching by room-temperature oxygen-vacancy ordering in Aurivillius oxide films](http://arxiv.org/abs/2609.02629v1)
  <details><summary>📄 Abstract</summary>
  Oxygen vacancies are central to the functionality of oxides, yet they typically exist as randomly distributed point defects, limiting the ability to precisely manipulate their collective behavior. Here, we report the room-temperature formation of a long-range-ordered oxygen-vacancy superstructure in single-crystalline Aurivillius-phase Bi2WO6 thin films via a mild nitrogen-plasma treatment. This structural transformation unlocks a colossal, reversible modulation of electrical conductivity by mor...
  </details>

- **2026-09-02** — Mason Youngblood, Katie Mudd, Manuel Anglada-Tort et al. — [Collective creativity in hybrid societies](http://arxiv.org/abs/2609.02620v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is changing how cultural artifacts are created and circulated, and with it our understanding of creativity itself. Researchers disagree about whether these tools enrich or impoverish culture, and we argue that much of that disagreement comes from conflating two distinct components of creativity: novelty, a property of single artifacts, and diversity, a property of populations. We argue further that creativity in the context of generative AI is best understood as a property of hybri...
  </details>

- **2026-09-02** — Ana Loureiro, Walter Van Assche — [Ratio and limiting zero distribution asymptotics for symmetric multiple orthogonal polynomials](http://arxiv.org/abs/2609.02801v1)
  <details><summary>📄 Abstract</summary>
  We investigate the ratio asymptotics and the asymptotic zero distribution of a sequence of polynomials that satisfy a recurrence relation of order $r+1$ with all recurrence coefficients, except the last one, equal to zero. Such a sequence is part of a system of multiple orthogonal polynomials and it satisfies the symmetry property $P_n(ω_{r+1} z) = ω_{r+1}^n P_n(z)$, where $ω_{r+1}$ is the primitive $(r+1)$th root of unity. We consider the unbounded regime in which the recurrence coefficients ex...
  </details>

- **2026-09-02** — Zehan Lin, Shengxin Liu, Biaoshuai Tao et al. — [Almost Envy-Freeness for Additive Mixed Manna with Entitlements: Deterministic and Randomized Guarantees](http://arxiv.org/abs/2609.02724v1)
  <details><summary>📄 Abstract</summary>
  We investigate the fair allocation of indivisible items among agents with asymmetric entitlements in mixed manna settings, where the items consist of both goods and chores. For additive valuations, we establish that weighted envy-free up to one item (WEF1) allocations always exist and can be computed in polynomial time. We also study fair and efficient allocation and show that weighted envy-freeness up to one transfer (WEF1T) is compatible with fractional Pareto optimality (fPO) for every mixed-...
  </details>

- **2026-09-02** — Pritthijit Nath, Sebastian Schemm, Peter Haynes et al. — [Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling](http://arxiv.org/abs/2609.02566v1)
  <details><summary>📄 Abstract</summary>
  Machine-learnt corrections can complement numerical weather prediction only if they adapt to the evolving model state while preserving dynamical consistency and numerical stability. To test this within a global forecasting model, we couple the Met Office (UKMO) Unified Model (UM) with distributed RL agents through rank-local tensors. A DDPG actor shares weights across the 70 vertical model levels of each atmospheric column and applies bounded potential-temperature corrections to the model tenden...
  </details>

- **2026-09-02** — Irina Proskurina, Guillaume Metzler, Antoine Gourru et al. — [Debias-SparseGPT: Bias-Aware Pruning for Large Language Models](http://arxiv.org/abs/2609.02496v1)
  <details><summary>📄 Abstract</summary>
  Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs). However, recent studies show that weight sparsification methods, such as SparseGPT, can amplify existing biases in models, with outputs varying significantly depending on persona cues in the prompt. In this paper, we introduce Debias-SparseGPT, a post-training pruning method incorporating representational debiasing using a second-order term defined o...
  </details>

- **2026-09-02** — Egecan Çelik Evgin, İlknur Karadeniz, Olcay Taner Yıldız — [Improving Health Literacy through Lay Summarization of Radiological Reports: An Evaluation of BioNER and Retrieval-Augmented Generation](http://arxiv.org/abs/2609.02396v1)
  <details><summary>📄 Abstract</summary>
  Radiology reports are written primarily for clinicians, and their specialized terminology often makes them difficult for patients to interpret. As a result, many patients turn to publicly available Large Language Models (LLMs) to help explain their reports, despite well-documented risks of factual inaccuracies and hallucinations. Automated lay-summary generation has emerged as a promising alternative, yet the effectiveness of retrieval-enhanced and clinically informed approaches for radiology-sp...
  </details>

- **2026-09-02** — Dong-Ping Fu, Michihisa Takeuchi — [Quark masses and mixing in the D_5 model under spontaneous CP violation](http://arxiv.org/abs/2609.02312v1)
  <details><summary>📄 Abstract</summary>
  It is known that CP violation occurs in flavor physics, and the CKM matrix is complex. We investigate the Yukawa sector of a four-Higgs model based on D_5 symmetry. To understand all possible sources of CP violation in the Yukawa sector, we systematically analyze the impact of all possible representation assignments of the left-handed and right-handed quark fields under the D_5 group. After imposing the conditions of non-block-diagonal CKM matrix and the absence of massless quarks, we find that ...
  </details>

- **2026-09-02** — Chao-Kai Wen, Yen-Cheng Chan, Lung-Sheng Tsai et al. — [Agentic UE-CoMIMO for 6G Terminals: From Virtual Antenna Augmentation to AI-Native Virtualization](http://arxiv.org/abs/2609.02290v1)
  <details><summary>📄 Abstract</summary>
  End-user-centric collaborative MIMO (UE-CoMIMO) lets nearby devices form a virtual multi-antenna terminal to overcome the antenna limitations of individual user equipment. Extending such cooperation to communication, sensing, computing, and task-relevant information exchange requires a control layer that can interpret user intent, select cooperation mechanisms, and replan as conditions change. This article introduces Agentic UE-CoMIMO, in which device micro-agents, a smartphone or CPE hub agent,...
  </details>

- **2026-09-02** — Youqi Wu, Farzan Farnia — [Do Large Language Models Capture the Diversity in their Training Data?](http://arxiv.org/abs/2609.02275v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained to model conditional distributions over text, yet it remains inadequately understood whether they capture the full diversity of plausible outputs present in their training data. We study this question through an information-theoretic lens by comparing the conditional entropy of model-generated outputs with that of the corresponding training data. Given paired input-output samples, we use conditional entropy and its matrix-based analogue based on von Neumann entr...
  </details>

- **2026-09-02** — Weixiang Hong, Hongting Du, Jiayue Tang et al. — [Prototype-guided transfer of sparse literature knowledge for electrolyte additive discovery](http://arxiv.org/abs/2609.02209v1)
  <details><summary>📄 Abstract</summary>
  Electrolyte additive discovery remains challenging because experimentally validated molecules are sparse, whereas accessible chemical spaces are vast and largely unlabeled. This challenge is amplified in lithium-ion batteries, where additive performance arises from coupled interfacial reactions rather than a single molecular property. Here, we develop a prototype-guided molecular intelligence, ProtoMI, a literature-driven framework that learns transferable structural priors from reported electro...
  </details>

- **2026-09-02** — Yiran Zhao, Lu Zhou, Liming Fang et al. — [Beyond Outcome Gaps: Process-Aware Fairness Diagnosis for LLM-based Multi-Agent Decision Systems](http://arxiv.org/abs/2609.02092v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) are increasingly considered for high-stakes decision-making, yet outcome-based fairness audits can miss where risks arise within the decision trajectory. We present SCOPED-Hiring, a process-aware fairness diagnosis pipeline for LLM-based hiring MAS. SCOPED-Hiring constructs controlled resume variants, runs role-based hiring committees, logs over 311K structured decision trajectories, and converts trajectory fields into quantitative fairness signals organized b...
  </details>

- **2026-09-02** — Yongshi Ye, Tian Lan, Feihu Jiang et al. — [CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning](http://arxiv.org/abs/2609.02074v1)
  <details><summary>📄 Abstract</summary>
  Planning is a central capability that enables agents to decompose complex long-horizon tasks into manageable steps. Test-time search and training-based methods improve planning but incur high inference costs or require expensive training data. Self-evolving memory instead accumulates reusable experience from agent interaction outcomes into an external memory bank, so planning capability keeps improving at inference time without parameter updates. However, existing self-evolving memory methods sh...
  </details>

- **2026-09-02** — Fangye Wang, Yunjin Gu, Haowen Lin et al. — [SPAR: Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception](http://arxiv.org/abs/2609.02062v1)
  <details><summary>📄 Abstract</summary>
  Generative Point-of-Interest (POI) recommendation, autoregressively generating a target POI's semantic ID (SID), holds great promise for Location-Based Services, where a recommendation helps only if the user can reach it. Yet, existing methods operate within an interest space defined by behavior sequences and collaborative signals, where geography enters only as a textual attribute of the SID, leaving no explicit mechanism to learn or preserve how urban places are related by distance, direction,...
  </details>

- **2026-09-02** — Xinan Zhou — [Pre-Strings Lectures on Holographic Correlators and Analytic Bootstrap](http://arxiv.org/abs/2609.01986v1)
  <details><summary>📄 Abstract</summary>
  Over the past decade, the bootstrap strategy has transformed the computation of holographic correlators and revealed structures suggesting an emerging scattering amplitude program in AdS. These notes, which are an extended version of the five lectures delivered at the Pre-Strings 2026 School, give a pedagogical introduction and synthesis of these developments. We start with a quick reminder of the essentials of CFT and a brief review of AdS perturbation theory. We then demonstrate in detail the ...
  </details>

- **2026-09-01** — Zichuan Li, Jian Cui, Ashley Chen et al. — [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](http://arxiv.org/abs/2609.01222v2)
  <details><summary>📄 Abstract</summary>
  Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of pr...
  </details>

- **2026-09-01** — Ramit Pahwa, Parivesh Priye, Apoorva Beedu — [VoiceLongMemEval: Do Assistants Remember How You Sounded?](http://arxiv.org/abs/2609.00570v2)
  <details><summary>📄 Abstract</summary>
  With the growing scale of multi-agent architectures and large language models, deployed AI assistants are increasingly tasked with reasoning over long, continuous, multi-session conversation histories. Current benchmarks evaluate this dialogue history as information retrieval over long horizon, temporal reasoning, or knowledge updates, while crucially ignoring the fundamental dynamics of human-agent interaction, i.e. how they said it. To address this gap, we present VoiceLongMemEval (VLME) bench...
  </details>

- **2026-09-01** — Ritwesh A. Kumar, Som Tripathi, Peja Matthews et al. — [Automated Maize Ear Phenotyping Using 3D Reconstructions](http://arxiv.org/abs/2609.01921v1)
  <details><summary>📄 Abstract</summary>
  Maize kernel traits such as row number, kernels per row, and kernel size vary largely for genetic reasons and are consistently associated with regions of the genome that influence yield. Manual measurement of these traits, however, cannot keep pace with the volume of maize generated in a breeding program. To address this, we developed and validated a fully automated pipeline for extracting these traits from 3D point clouds of corn ears, built on a recently developed video-to-point-cloud platform...
  </details>

- **2026-09-01** — Kunal Jadhav, Siddhesh More — [Grounded, Compute-Efficient LLM Policy Agents for Energy-Poverty Equity in Physically-Constrained Peer-to-Peer Energy Markets](http://arxiv.org/abs/2609.01918v1)
  <details><summary>📄 Abstract</summary>
  Energy poverty is nearly absent from NLP-for-social-good, and the little existing work is either static retrieval/QA or relies on carbon-intensive cloud LLMs, a self-defeating "computational irony" for a humanitarian setting. We present EqGrid, a closed-loop simulation in which a low-frequency, open-weight LLM policy agent sets price and carbon bounds and targeted subsidies over a community of empirically-grounded household personas, while high-frequency multi-agent RL traders clear a continuous...
  </details>

- **2026-09-01** — Yunqin Zhu, Feng Qiu, Yao Xie — [OutageDiT: A Generative Foundation Model for Power Outage Forecasting and Scenario Simulation](http://arxiv.org/abs/2609.01896v1)
  <details><summary>📄 Abstract</summary>
  Power-outage planning requires scenarios before an event occurs. These scenarios must represent uncertainty in magnitude, timing, and duration while preserving temporal dependence. However, severe events are rare, and data from any single region contain few examples of extreme outage and restoration patterns. To address this challenge, we introduce OutageDiT, a foundation model for generating seven-day outage trajectories at quarter-hour resolution, trained on outage and weather records across t...
  </details>

- **2026-09-01** — Marc Bara — [Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence](http://arxiv.org/abs/2609.01873v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent AI systems improve inference by spawning agents and synthesizing reports. But another agent is not another observation: apparently independent reports may descend from the same evidence, and genuinely independent evidence can produce nearly identical reports. We formalize this as an epistemic Sybil problem. A report Z is an epistemic Sybil extension relative to reports R when I(Theta; Z | R) = 0. No report-only aggregator can generally distinguish replication from independent corrobo...
  </details>

- **2026-09-01** — Jundong Hu, Shekar Ramachandran — [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](http://arxiv.org/abs/2609.01852v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning. We study when this harm begins as model capability changes. We evaluate a frozen, closed-set, action-scored benchmark with 2 suites that represent 2 different meanings of "no memory" (a Benefit suite, unsolvable without the stored fact, and a Safety suite, in which an authoritative tool always holds the correct value), on a same-family model-size series (Qwen3 0.6/...
  </details>

- **2026-09-01** — R. James Cotton, Divya Joshi, Colleen Peyton — [Cross-Model Distillation of a Human-Pose Foundation Model from Unannotated Infant Video for Markerless 3D Pose Estimation](http://arxiv.org/abs/2609.01840v1)
  <details><summary>📄 Abstract</summary>
  Spontaneous movement is one of the earliest windows onto an infant's neuromotor health, and structured clinical instruments that score it are validated early predictors of cerebral-palsy risk. However, they require specially trained raters, are time-consuming, and carry inter-rater variability. This motivates automated, video-based markerless assessment, especially as marker-based motion capture is impractical in infants. Yet the foundation models that make markerless capture possible are traine...
  </details>

- **2026-09-01** — Joseph Axisa — [Architecting Conversational Data Systems for Stateless LLM APIs: The Hydration Proxy Pattern](http://arxiv.org/abs/2609.01834v1)
  <details><summary>📄 Abstract</summary>
  As enterprise platforms transition to conversational reasoning interfaces, the stateless nature of LLM APIs creates an architectural gap. While statelessness enables horizontal scalability for AI providers, it forces client applications to manage the entire burden of conversational state and semantic memory. The work identifies the Hydration Proxy Pattern, an architecture that decouples session persistence from the reasoning engine. The framework ensures platform sovereignty over conversational ...
  </details>

- **2026-09-01** — Fangyi Zhu, Ajay Subramanian, Allison Constant et al. — [Interpretable Symptom Vectors for Depression in a Large Language Model](http://arxiv.org/abs/2609.01832v1)
  <details><summary>📄 Abstract</summary>
  Patients with depression present with diverse symptom profiles, yet clinical practice routinely reduces this variation to a single severity score. Large language models (LLMs) can potentially capture various symptoms and their severity from patient speech. However, how depressive symptoms are represented inside LLMs remains poorly understood, limiting clinical trust. To examine whether internal model activations match clinician judgment, we analyzed the residual stream of Gemma-3-27B-PT using me...
  </details>

- **2026-09-01** — Quan Minh Nguyen, Hoang M. Ngo, Trong Nghia Hoang et al. — [D-FROST: Decentralized Federated pRompt-tuning via Optimal tranSporT for Non-IID and Imbalanced Data](http://arxiv.org/abs/2609.01802v1)
  <details><summary>📄 Abstract</summary>
  Prompt tuning provides a parameter-efficient way to adapt foundation models (FMs) by freezing the pretrained backbone and updating only a small set of learnable prompts. This property makes prompt tuning especially suitable for decentralized federated learning (DFL), where exchanging full-model updates can be prohibitively expensive. However, prompt tuning in DFL introduces new challenges. Prompt sets learned from heterogeneous local data may not be index-wise aligned, making standard decentrali...
  </details>

- **2026-09-01** — Arpan Kumar Mahapatra — [Public-Sharing Labels and Verbatim Field Egress in an MCP-to-A2A Agent Configuration: A Controlled Multi-Model Study](http://arxiv.org/abs/2609.01693v1)
  <details><summary>📄 Abstract</summary>
  Safety properties assessed separately for Model Context Protocol (MCP) tool use and Agent2Agent (A2A) delegation need not describe behavior when one agent uses both. We measure one such behavior in a single controlled MCP-to-A2A configuration: a testbed drives a real-model host across a local MCP and a local A2A leg into an ordered event trace scored by exact deterministic rules (no LLM judge), one restricted decision per trial. In a pre-specified, frozen three-arm design, each of 10 record scen...
  </details>

- **2026-09-01** — Somyaranjan Chakra, Mohit Anand Madhesia, Shradha Mishra — [Statistical Language Competition Model with Dynamic Edge Weighting on a Random Network](http://arxiv.org/abs/2609.01078v2)
  <details><summary>📄 Abstract</summary>
  This paper presents a computational study of language competition dynamics on Erdős--Rényi random networks, extending the foundational Abrams--Strogatz model through two novel contributions: (i) a dynamic edge-weighting mechanism that reinforces social ties between co-minority speakers by an additive increment $Δ$, and (ii) a probabilistic agent-based framework governing language switching via a weighted majority rule. Phase boundaries separating the dominance and coexistence regimes are identif...
  </details>

- **2026-09-01** — Safayat Bin Hakim, Houbing Herbert Song — [Ranked by the Matcher: A Reproducibility Audit of Knowledge Graph Extraction from Threat Reports](http://arxiv.org/abs/2609.01671v1)
  <details><summary>📄 Abstract</summary>
  Security teams and researchers choose knowledge-graph extraction tooling for threat reports on the strength of published triple-F1 scores, yet those scores depend on how predicted triples are matched to gold annotations. We could reimplement the stated matching rule for only five of twelve inspected systems. Re-scoring ten system outputs on shared documents under eight protocols reverses eleven of forty-five pairwise orderings; one fixed prediction set spans 0.16-0.70 F1. On GRID's external 378-...
  </details>

- **2026-09-01** — Vahid Reza Khazaie, Ahmed Y. Radwan, Shaina Raza — [FairLens: Benchmarking Fairness in Vision-Language Models for High-Stakes Decision-Making](http://arxiv.org/abs/2609.01691v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used to make decisions from visual inputs. We introduce FAIRLENS, a benchmark and evaluation framework for measuring both the fairness and the validity of VLM responses in three high-stakes domains: hiring, legal, and healthcare. FAIRLENS pairs real face images spanning gender, race, and age groups with closed- and open-ended questions, giving more than 100K image-question pairs per model, and evaluates responses from four complementary views: demog...
  </details>

- **2026-09-01** — Qingde Li, Qingqi Hong, Zihan Li et al. — [Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations](http://arxiv.org/abs/2609.01408v2)
  <details><summary>📄 Abstract</summary>
  A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper in...
  </details>

- **2026-09-01** — Shuze Daniel Liu, David Simchi-Levi, Claire Chen et al. — [OR-Transformer: Scaling Real-Time Decision-Making to 1,000 Items](http://arxiv.org/abs/2609.01933v1)
  <details><summary>📄 Abstract</summary>
  Modern supply chain operations can require coordinating replenishment across thousands of heterogeneous items under correlated stochastic demand, heterogeneous lead times, and shared fixed ordering costs, yielding observation spaces exceeding $10^4$ dimensions. At this scale, rolling-horizon stochastic mixed-integer linear programs (MILPs) become prohibitively slow, while standard reinforcement learning (RL) methods face increasingly challenging credit assignment in high-dimensional action space...
  </details>

- **2026-09-01** — Moghis Fereidouni, Muhammad Umair Haider, Hassan Sajjad et al. — [GAPS: Dimension-Level Gates for Conditional Activation Steering](http://arxiv.org/abs/2609.01878v1)
  <details><summary>📄 Abstract</summary>
  Activation steering suppresses undesired behaviors in language models by adding a steering vector to the hidden state during generation. Recent conditional methods such as CAST and DSAS improve the behavior-capability trade-off by deciding when to intervene, but once active, they apply the full dense vector to all hidden dimensions, regardless of whether a neuron carries concept information or already lies in the desired regime. We introduce dimension-level conditioning as a complementary axis o...
  </details>

- **2026-09-01** — Usneek Singh, Poorvaja Veera Balaji Kumar, Parth Nanda et al. — [VakyArth: Evaluating Pragmatic Competence in LLMs across Indic Languages](http://arxiv.org/abs/2609.01788v1)
  <details><summary>📄 Abstract</summary>
  Real-world communication often requires pragmatic reasoning: interpreting meanings implied through context and cultural convention rather than stated literally. Existing pragmatic evaluation remains largely limited to English and high-resource languages, leaving Indic languages unexplored despite their linguistic and cultural diversity. We introduce VakyArth, the first pragmatic benchmark for Indic languages, designed as a diagnostic evaluation covering Hindi, Punjabi, Tamil, and Malayalam. Vaky...
  </details>

- **2026-09-01** — Nabira Rashid, Manolis Kellis — [Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories](http://arxiv.org/abs/2609.01556v1)
  <details><summary>📄 Abstract</summary>
  We evaluate embedding retrieval where surface form and meaning are pulled apart on purpose: retrieving items that share underlying structure but not wording, in two unrelated domains under one protocol, competition mathematics (MathNet-Retrieve; 500 queries, 117,088-item corpus) and embodied-agent trajectories (ALFWorld-derived; 118 queries, 336 trajectories). In mathematics the failure is complete: strict Hit@1 at the heaviest disguise tier is 0.0% for both production embedders (bootstrap 95% C...
  </details>

- **2026-09-01** — Liming Pu, Xiaoxia Li, Yifu Liu et al. — [Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents](http://arxiv.org/abs/2609.01245v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning is a natural way to post-train LLM agents for long-horizon interactive tasks judged only by end-of-task verification, yet a shared belief holds that outcome-only RL soon hits a ceiling on small open models. Recent work therefore compensates around the training with denser rewards, SFT priors, skill libraries, curated memory, or multi-agent orchestration. We argue the ceiling is an artifact of two failures of common practice. Signal starvation: group-relative RL with sparse...
  </details>

- **2026-09-01** — Zichuan Li, Jian Cui, Ashley Chen et al. — [What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness](http://arxiv.org/abs/2609.01222v1)
  <details><summary>📄 Abstract</summary>
  Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of pr...
  </details>

- **2026-09-01** — Ramit Pahwa, Parivesh Priye, Apoorva Beedu — [VoiceLongMemEval: Do Assistants Remember How You Sounded?](http://arxiv.org/abs/2609.00570v1)
  <details><summary>📄 Abstract</summary>
  With the growing scale of multi-agent architectures and large language models, deployed AI assistants are increasingly tasked with reasoning over long, continuous, multi-session conversation histories. Current benchmarks evaluate this dialogue history as information retrieval over long horizon, temporal reasoning, or knowledge updates, while crucially ignoring the fundamental dynamics of human-agent interaction, i.e. how they said it. To address this gap, we present VoiceLongMemEval (VLME) bench...
  </details>

- **2026-09-01** — Elias Stengel-Eskin, Newton Sander, Carlos Bonetti et al. — [GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions](http://arxiv.org/abs/2609.01491v1)
  <details><summary>📄 Abstract</summary>
  The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for linguistic accounts of LLMs. To address these questions, we introduce GlossoGen, a novel platform for studying multi-agent language evolution in complex scenarios. Within GlossoGen, we build the SaveVeyru scenario, which requires agents with partial information to communicate under pressure. We fin...
  </details>

- **2026-09-01** — Aryeh Lev Zabokritskiy — [Binary Multiple-Node-Erasure-Correcting Codes over Complete Graphs: Constructions, q-Ary Metric Balls, and Duality](http://arxiv.org/abs/2609.01474v1)
  <details><summary>📄 Abstract</summary>
  We study linear codes whose coordinates are the ordinary edges and self-loops of complete undirected graphs; a node erasure removes all coordinates incident with a failed vertex. The construction results are binary. For triple-node erasures, we extend the published cyclic construction by allowing a suitable cyclic check slope to depend on the prime graph length. An explicit determinant test proves that one of three fixed slope choices works at infinitely many prime lengths, unconditionally, and ...
  </details>

- **2026-09-01** — Charles Corbière, Léo Machado, Aubin Charley et al. — [RadMatch: Auditable Radiology Report Evaluation via Finding-Level Matching](http://arxiv.org/abs/2609.01470v1)
  <details><summary>📄 Abstract</summary>
  As AI systems are increasingly used to draft radiology reports, reliably evaluating their clinical quality remains a critical challenge. Large language model (LLM)-based metrics are now the best-correlated with radiologist judgment, yet they output a single opaque score that neither a clinician nor a model builder can easily interpret or audit. We introduce RadMatch, a multi-stage, LLM-based metric that decomposes report comparison into a structured finding-level matching with significance-aware...
  </details>

- **2026-09-01** — Mikhail Sonkin, Tanja Baeumel, Daniil Gurgurov et al. — [Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual LLMs](http://arxiv.org/abs/2609.01356v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models (mLLMs) achieve strong performance in machine translation, yet our understanding of the mechanisms by which they transform representations from one language to another remains incomplete. Prior work suggests that translation decomposes into separable processes within an mLLM, where conceptual content is first represented independently, followed by a production into language-specific form. In this work, we show that translation is even more modular than previous...
  </details>

- **2026-09-01** — Kai Guan, Minchao Jiang, Ruichen WangLi et al. — [Seeing the World and the Self from Egocentric Video](http://arxiv.org/abs/2609.01276v1)
  <details><summary>📄 Abstract</summary>
  Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different predi...
  </details>

- **2026-09-01** — Xin Sun, Daniel Ståhl, Kristian Sandahl et al. — [Continuous Autonomous Refactoring: A Research Roadmap for AI-Driven Code Quality Maintenance](http://arxiv.org/abs/2609.01236v1)
  <details><summary>📄 Abstract</summary>
  Large language models have shown promising capabilities in code refactoring, but existing approaches remain limited to method-level tasks. In this paper, we envision LLM-based refactoring as a continuous component of software maintenance rather than a tool invoked only for occasional manual refactoring. Under this vision, AI agents continuously monitor, evaluate, and improve codebases against explicit and evolving notions of software quality. We present a roadmap organized around five dimensions...
  </details>

- **2026-09-01** — Somyaranjan Chakra, Mohit Anand Madhesia, Shradha Mishra — [Statistical Language Competition Model with Dynamic Edge Weighting on a Random Network](http://arxiv.org/abs/2609.01078v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a computational study of language competition dynamics on Erdős--Rényi random networks, extending the foundational Abrams--Strogatz model through two novel contributions: (i) a dynamic edge-weighting mechanism that reinforces social ties between co-minority speakers by an additive increment $Δ$, and (ii) a probabilistic agent-based framework governing language switching via a weighted majority rule. Phase boundaries separating the dominance and coexistence regimes are identif...
  </details>

- **2026-09-01** — Shiyu Li, Zi-Yuan Hu, Shijia Huang et al. — [SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models](http://arxiv.org/abs/2609.01004v1)
  <details><summary>📄 Abstract</summary>
  Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences. To reduce inference costs, recent studies have explored visual token pruning through vision-centric or text-guided strategies. However, these methods often overlook high-norm outlier tokens, i.e., tokens with abnormally large feature norms, leading to suboptimal pruning decisions. In this work, we show that such high...
  </details>

- **2026-09-01** — Yinuo Xu, Yuwei Liang, Jianjie Cheng et al. — [DualStake: Dual-Path Confidence Calibration in Deep Research Agents](http://arxiv.org/abs/2609.00935v1)
  <details><summary>📄 Abstract</summary>
  Deep Research agents tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. However, these agents suffer from severe overconfidence, making their expressed confidence unreliable for user trust and downstream abstention. To address this, we augment the Deep Research pipeline with step confidence elicitation after each retrieval, building on the commonly used post-answer verbalized confidence. Interestingly, we find that Evidence Confidence (E-Conf), elici...
  </details>

- **2026-09-01** — Koshiro Aoki, Ryota Takatsuki, Gouki Minegishi et al. — [In-Context Neurofeedback: Can LLMs Control Their Internal Representations through Privileged Access?](http://arxiv.org/abs/2609.00904v1)
  <details><summary>📄 Abstract</summary>
  Whether large language models (LLMs) can control their own internal representations matters for both machine metacognition and AI safety. A recent study applied neurofeedback to LLMs and claimed that they can control their internal representations. However, the reported control may rely on superficial mechanisms rather than genuine internal access because the control targets in that study are not privileged, meaning that a third party can infer them from the prompt. We redesign the neurofeedback...
  </details>

- **2026-09-01** — Xingyu Qu, Siyuan Lu, Zhiyu Chen et al. — [CacheBridge: Efficient Cross-Model KV Cache Transfer](http://arxiv.org/abs/2609.00891v1)
  <details><summary>📄 Abstract</summary>
  Sharing context between LLMs in a multi-model system requires the receiving model to prefill the shared prefix because KV caches are model-specific. Recent closed-form cross-model KV transfer, hereafter Full-Head Mapping, avoids this replay by fitting a training-free affine mapper from source to target caches. However, its full-head design maps each target KV head from every source KV head in the selected layers, making transfer quality sensitive to architectural differences and causing mapper s...
  </details>

- **2026-09-01** — Michail Takaronis, Athanasia Kollarou, Georgios Kavallieratos et al. — [Using LLMs to Elicit Security Requirements for Service-Oriented Cyber Ranges](http://arxiv.org/abs/2609.00886v1)
  <details><summary>📄 Abstract</summary>
  Cyber ranges are complex environments comprising many interacting components and stakeholders with different security concerns. The Service-Oriented Cyber Range (SOR) is no exception, particularly when it comes to training scenarios targeting critical infrastructure. Security concerns are translated into security requirements, the elicitation of which is usually difficult and time-consuming. This work examines how large language models can assist in eliciting security requirements for a service-...
  </details>

- **2026-09-01** — Runpeng Dai, Kaili Huang, Changsung Kang et al. — [It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning](http://arxiv.org/abs/2609.00638v1)
  <details><summary>📄 Abstract</summary>
  Retrieval is the first stage of modern search and advertising systems, selecting a candidate set from a large item universe for downstream ranking and auction. Recent work increasingly leverages LLMs to improve retrieval through query expansion, data synthesis, and retrieval-feedback training. However, the generative component is typically used for query-side augmentation, while final matching is still delegated to a downstream retriever. We introduce CoGR, a retrieval framework that instead tra...
  </details>

- **2026-09-01** — Suryaansh Jain, Rahasya Barkur, Vishal G et al. — [A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss](http://arxiv.org/abs/2609.00591v1)
  <details><summary>📄 Abstract</summary>
  An image may be worth a thousand words, but most captioning models describe it in only a few. Modern vision-language models produce fluent high-level captions, yet routinely miss the attributes, counts, textures, materials, and spatial relations that make an image visually specific. Recent multi-stage systems recover some of these details through generation, decomposition, verification, and rewriting, but they do so at the expense of substantially higher inference latency.   We propose SimLoss, ...
  </details>

- **2026-09-01** — Alexandre Clin Deffarges, Nataliya Kosmyna, Pattie Maes — [Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing](http://arxiv.org/abs/2609.00584v1)
  <details><summary>📄 Abstract</summary>
  Does unrestricted AI access bypass the cognitive effort required for learning, or does it streamline knowledge acquisition? This paper reports on a study where we compare three designs for user-AI interaction in a learning context: (1) an unrestricted conversational bot like ChatGPT, (2) a pedagogically constrained bot that guides through hints without giving final answers, which we refer to as the Socratic mode; and (3) a non-conversational adaptive tutoring system that adjusts difficulty in re...
  </details>

- **2026-09-01** — Seonghyeon Cho, Chanjun Park — [Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents](http://arxiv.org/abs/2609.00549v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents increasingly rely on external skills, yet standard evaluations obscure whether retrieving these skills actually helps. Aggregate metrics often compare retrieved versus non-retrieved tasks, introducing severe selection bias and failing to isolate the true effect of skill use. To measure this actual-use capability-which we formalize as Skill Following (SF)-we introduce the Retrieval-Invoked Actual-Use Effect (RAE). RAE computes the same-task outcome difference bet...
  </details>

- **2026-09-01** — Ayan Goel, Thomas A. Walton, Amirali Aghazadeh — [Learning Task-Specific Antibody Representations via Function-Aware Masking](http://arxiv.org/abs/2609.00518v1)
  <details><summary>📄 Abstract</summary>
  Antibody-specific language models pretrained via masked language modeling (MLM) learn representations that are critical for downstream sequence design and property prediction tasks. Yet, the corruption process itself is rarely leveraged as a source of inductive bias during pretraining. While preferentially masking complementarity-determining regions (CDRs) improves binding-related predictions, antibodies possess diverse biological priors over a variety of functions. Herein, we introduce function...
  </details>

- **2026-09-01** — Jacob Brinton, Jannik Brinkmann, Mark Crovella et al. — [The Interlingua Hypothesis: LLMs Translate via a Latent Task-agnostic Feature Space](http://arxiv.org/abs/2609.00515v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently demonstrated improved machine translation performance over strong supervised baselines. This raises questions as to what mechanisms underlie how LLMs perform machine translation between languages. Motivated by recent interpretability findings--namely, that LLMs use massively multilingual latent feature representations to perform language modeling--we propose the interlingua hypothesis. The hypothesis holds that language models translate by reading a sou...
  </details>

- **2026-09-01** — Qingde Li, Qingqi Hong, Jie Tian — [Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations](http://arxiv.org/abs/2609.01408v1)
  <details><summary>📄 Abstract</summary>
  A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper in...
  </details>

- **2026-09-01** — Haoyang Chen, Yi Liu, Jianzhi Shao et al. — [Polished but Unresolved: Identifying Late-Stage Pressure States in Long-Horizon Tool-Use Agents](http://arxiv.org/abs/2609.00823v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon tool-use agents need not only to search and plan, but also to decide when to finalize. We study late-stage pressure states, in which an agent is biased toward submitting a final answer that appears complete and polished while key constraints remain unresolved. We first train a linear probe to show that this pressure state is identifiable from the agent's hidden states. Then, we use activation interventions along this pressure direction and find that shifting the hidden states change...
  </details>

- **2026-09-01** — Nicholas Teh — [Weighted Fair Division of Indivisible Mixed Manna](http://arxiv.org/abs/2609.01580v1)
  <details><summary>📄 Abstract</summary>
  We study weighted fair division of indivisible mixed manna under additive valuations. First, we resolve the general existence open question for weighted envy-freeness up to one item (WEF1), and show that every instance with arbitrary positive entitlements admits a complete WEF1 allocation computable in polynomial time. We then show that existence does not imply any welfare guarantee, i.e., the utilitarian price of WEF1 is infinite, even for two unweighted agents with normalized valuations, commo...
  </details>

- **2026-09-01** — Ema Salkić, Alexander Fichtl, Philipp Ulrich et al. — [A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains](http://arxiv.org/abs/2609.01563v1)
  <details><summary>📄 Abstract</summary>
  Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and prioritizes risk intelligence from public corporate disclosures. We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe. It organizes these into a knowledge graph linkin...
  </details>

- **2026-09-01** — Yixuan Liu, Lin Chen, Zhuoqi Liu et al. — [Citing Less Critically: LLMs Reshape the Rhetoric and Reach of Scientific Citation](http://arxiv.org/abs/2609.01432v1)
  <details><summary>📄 Abstract</summary>
  Scientific citations carry rhetorical intent. Scholars may cite prior work positively (supporting), negatively (contrasting), or neutrally (mentioning). As large language models (LLMs) increasingly assist scientific writing, whether they reproduce citations with the same rhetorical intent as humans remains unclear. We introduce a masked-citation task to compare human and LLM-generated citation behavior. For each citation context, an LLM generates a replacement citation sentence, producing a coun...
  </details>

- **2026-09-01** — Maeve Hutchinson, Syed Mahbubul Huq, Mohammad Albinhassan et al. — [InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations](http://arxiv.org/abs/2609.01383v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models have demonstrated remarkable proficiency in interpreting static visual artifacts, but modern data analysis is inherently dynamic, requiring the active interrogation of interactive environments. Existing benchmarks are predominantly constrained to static imagery and one-shot question answering and fail to capture the epistemic demands of this domain, where evidence is frequently occluded, distributed across linked views, or conditionally revealed through user agency. In thi...
  </details>

- **2026-09-01** — Shaowen Wang, Ge Zhang, Kairong Luo et al. — [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](http://arxiv.org/abs/2609.01343v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache. Through a series of ablations, we arrive at a recipe we call SMELT (Sparse MoE Transformer, middle layers Loop Twice), which loops the middle half of layers twice while matchi...
  </details>

- **2026-09-01** — Christian Fiedler, Tim Roith — [Consensus-based optimization for linearly separable functions](http://arxiv.org/abs/2609.01317v1)
  <details><summary>📄 Abstract</summary>
  Consensus-based optimization (CBO) is an efficient metaheuristic for global optimisation with attractive mathematical properties, allowing global convergence results even in non-convex settings. In practice it suffers greatly from the curse of dimensionality, as do most particle-based optimisers. Different strategies have been proposed to apply CBO even for high-dimensional optimisation problems, the most prominent being the so-called anisotropic noise model. However, a recent work by Bonandin e...
  </details>

- **2026-09-01** — W. Ross Morrow — [Multi-Head Self Attention is a Parameter Identification Mechanism](http://arxiv.org/abs/2609.01231v1)
  <details><summary>📄 Abstract</summary>
  We prove that a multi-head scaled dot product attention can be viewed as a parameter identification strategy. The ratio of unidentified parameters to the total number of parameters scales like the reciprocal of the number of heads ($1/2 \to 1/(2H)$), meaning models with more heads are structurally more identified. A subtle side effect of the mathematics observation that attention can never be fully identified. Similarly we also show that some bias terms can have no effect on softmax-based attent...
  </details>

- **2026-09-01** — Riyaaz Shaik, Chandru Venkataraman — [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](http://arxiv.org/abs/2609.01215v1)
  <details><summary>📄 Abstract</summary>
  Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's d...
  </details>

- **2026-09-01** — Zhilong Song, Lixue Cheng — [Autonomous discovery of new structure-plausibility laws for explainable and rapid crystal diagnosis and screening](http://arxiv.org/abs/2609.01209v1)
  <details><summary>📄 Abstract</summary>
  Crystal generators and tool-using agents propose structures faster than density functional theory (DFT) energy and phonon calculations or experiments can assess them. Deciding which candidates merit expensive assessment is therefore the bottleneck, yet most screens test little beyond atomic overlap and give no chemical reason for failure. Here, our agents generate, test and actively refute two million candidate laws, leaving eight Plausibility Rules for Inorganic Structures (PRIS). These laws en...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 615 |
| prompt-injection | 524 |
| memory-poisoning | 47 |
| tool-use-attack | 132 |
| backdoor | 443 |
| adversarial-attack | 581 |
| privacy-leakage | 4006 |
| steganography | 62 |
| misuse | 979 |
| red-teaming | 121 |
| vulnerability | 2970 |
| defense | 2740 |
| alignment | 2555 |
| robustness | 2632 |
| watermark | 392 |
| unlearning | 94 |
| agent-safety | 53 |
| benchmark | 65 |
| survey | 323 |
| other | 7220 |

---

📚 **全部 26554 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-04 10:23:41*