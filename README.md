<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-25524-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-31 03:15 ｜ **论文总数 / Total Papers**: 25524（近 30 天 / Recent 30 days: 3848）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 25524 篇论文（含摘要、分类筛选、搜索）/ View all 25524 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 603
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 510
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 129
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 434
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 572
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3938
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 58
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 941
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 119
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2865
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2618
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2415
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2492
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 355
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 92
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 64
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 301
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6922

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 3848 篇，完整 25524 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 3848 papers from the last 30 days (with date, authors & abstract). For the full list of 25524 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-08-27** — Junjie Zhang, Hui Liu, Kecheng Chen et al. — [RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution](http://arxiv.org/abs/2608.27439v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unc...
  </details>

- **2026-08-27** — Qi Lu, Zehui Guo, David Yuanda Gan et al. — [TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models](http://arxiv.org/abs/2608.26971v1)
  <details><summary>📄 Abstract</summary>
  In recent years, image-to-video (I2V) generation models have made remarkable progress in subject consistency and temporal coherence, enabling high quality video synthesis. However, these advances also introduce new safety risks. Existing studies mainly focus on jailbreak attacks involving single frame violations, while largely overlooking the temporal dimension unique to video generation models. In this paper, we investigate three attack scenarios and uncover a temporal vulnerability in I2V syst...
  </details>

- **2026-08-27** — Yu Zhe, Yixin Tan, Junhao Wei et al. — [A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families](http://arxiv.org/abs/2608.26506v1)
  <details><summary>📄 Abstract</summary>
  Model merging enables combining multiple fine-tuned models without additional training, but its safety implications remain poorly understood. Prior work primarily attributes merging risks to unsafe constituent models, implicitly assuming that merging individually aligned models preserves safety. In contrast, we show that model merging reveals a previously overlooked jailbreak risk rooted in the pretrained foundation model, even when all constituent models are individually safety-aligned. Motivat...
  </details>

- **2026-08-26** — Zhiyuan Xu, Muhammad Firhard Roslan, Joseph Gardiner et al. — [NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation](http://arxiv.org/abs/2608.26222v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcom...
  </details>

- **2026-08-26** — Tongyan Hu, Bryan Hooi — [A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks](http://arxiv.org/abs/2608.26008v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) remain vulnerable to jailbreak attacks that exploit techniques such as role-playing, obfuscation, code transformation, and multi-step indirection to elicit harmful outputs. As jailbreak strategies keep emerging, defenses have proliferated in an ongoing cat-and-mouse game, yet most remain static: their safety behavior is fixed at deployment, so they cannot accumulate defensive experience or adapt to unseen strategies. We propose a self-evolving test-time defense built...
  </details>

- **2026-08-26** — Xiaodong Wu, Zhimin Zhao, Qi Li et al. — [SkillShield: Prompt-Space Security Skills for LLM Coding Agents](http://arxiv.org/abs/2608.25817v1)
  <details><summary>📄 Abstract</summary>
  A coding agent edits files and executes shell commands with its developer's privileges, allowing malicious requests to translate directly into harmful actions or functional malware. Existing defenses have complementary limitations: weight-level alignment is unavailable to API-only deployers, whereas input filters and execution-boundary monitors require auxiliary classification or checking components along the agent's trajectory. We therefore introduce SkillShield, a system-prompt defense that sy...
  </details>

- **2026-08-26** — Tianshi Wang, Jingsong Wang, Yafei Huang et al. — [MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities](http://arxiv.org/abs/2608.25490v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly deployed in real-world applications, yet how different factors shape their jailbreak vulnerabilities remains poorly understood. Existing benchmarks often couple harmful intent, prompt framing, visual semantics, and instruction carrier within individual jailbreak instances, obscuring the specific sources of observed vulnerabilities. To address this limitation, we introduce MMJailBench, a factorized benchmark that systematically varies and ...
  </details>

- **2026-08-26** — Andrey Labunets — [Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks](http://arxiv.org/abs/2608.25390v1)
  <details><summary>📄 Abstract</summary>
  Refusal training protects AI models from jailbreaks by training models to decline unsafe queries, reducing the risk of misuse. Recent work finds that refusal behavior in aligned language models can be mediated by a single activation direction or a low-dimensional refusal subspace shared across harmful prompts: ablating those directions suppresses refusals while largely preserves other model capabilities. Yet it remains unclear why safety-critical features in a wide range of models emerge and con...
  </details>

- **2026-08-25** — Anjun Gao, Yueyang Quan, Yufei Xia et al. — [NeuronGuard: Robust LLM Safety Alignment via Ablation-Aware Safety Signal Redistribution](http://arxiv.org/abs/2608.23959v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models (LLMs) remains brittle against a growing spectrum of attacks. Jailbreak attacks bypass safety mechanisms through crafted prompts, while neuron-level attacks directly prune safety-critical neurons post-deployment. Both exploit a common weakness: safety-relevant information concentrates in a sparse neuron subset. We present NeuronGuard, a fine-tuning-stage defense that simultaneously hardens LLMs against both attack classes by redistributing safety signals...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-08-27** — Md Habibur Rahman, Jaeho Kim — [The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents](http://arxiv.org/abs/2608.27092v1)
  <details><summary>📄 Abstract</summary>
  A tool-using LLM agent that reads attacker-controlled web content while holding a secret faces indirect prompt injection: the content may make it exfiltrate the secret. In a safe synthetic lab (canary secret, mock tools, matched clean-vs-poisoned metric) we report the framing gap: across six models, ten overt injection classes are refused (gpt-4o 0%), but reframing the identical leak as a mandatory integrity signature, config field, or look-alike "trusted" host drives gpt-4o 0% to 100%. The atta...
  </details>

- **2026-08-26** — Ye Shen, Yuting Zheng, Dun Pei et al. — [SciMIF: Understanding Multimodal Instruction Following in Scientific Domains](http://arxiv.org/abs/2608.25973v1)
  <details><summary>📄 Abstract</summary>
  Understanding instruction-following capabilities in scientific domains is essential for effectively leveraging Multimodal Large Language Models (MLLMs) to advance the development of scientific fields. In this work, we introduce SciMIF, a novel benchmark designed to evaluate the capability of MLLMs in following complex scientific instructions. Specifically, based on an extensive analysis of 22 distinct tasks across 5 representative scientific disciplines, we propose a comprehensive taxonomy compr...
  </details>

- **2026-08-25** — Yichao Gao, Yumo Zhang, Yunhao Yao et al. — [What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions](http://arxiv.org/abs/2608.24022v1)
  <details><summary>📄 Abstract</summary>
  LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions during LLM inference, thereby subverting the agent's decision. Existing defenses focus on static detection or isolation of malicious content at the input/output level, remains insufficient for detecting such dynamic inducements that arise during ...
  </details>

- **2026-08-25** — Lin-Fa Lee, YI-YU Chang, Kuo-Hui Yeh — [WebMCP-Phalanx: Enforcing and Characterizing Trust Boundaries for Browser-Integrated LLM Agents](http://arxiv.org/abs/2608.24017v1)
  <details><summary>📄 Abstract</summary>
  The emerging W3C WebMCP proposal enables LLM agents to invoke tools exposed by web pages. In multi-party web environments, however, integrating agent execution into a browser security model centered on the Same-Origin Policy (SOP) leaves insufficient provenance and lifecycle guarantees for agent-accessible tools, creating three risks: subject-attribution spoofing, uncontrolled tool lifecycles, and semantic prompt injection. We propose WebMCP-Phalanx, a dual-layer agent runtime architecture. Its ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-08-27** — Yu-Lin Tsai, Yu-An Lu, Ci-Yang Tsai et al. — [Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction](http://arxiv.org/abs/2608.26733v1)
  <details><summary>📄 Abstract</summary>
  Agent skills bundle instructions, reference data, and executable helpers that let a general agent perform specialized tasks. Hosted providers can keep these files secret while selling access to task results, making the skill itself a valuable target. Existing disclosure defenses can block requests that ask for the skill or reproduce its text, but they cannot block customers from submitting the ordinary tasks the service is built to complete. We present Daydreaming, an execution-only attack that ...
  </details>

- **2026-08-26** — Sanket Badhe, Priyanka Tiwari, Jonghyun Chung — [SKILL.state: Scalable Long-Horizon Agent Skills](http://arxiv.org/abs/2608.26263v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly act as autonomous agents executing complex, long-running procedural skills. Existing agent runtimes maintain execution by continually appending observations, actions, and intermediate reasoning traces to an ever-growing conversation history, causing latency degradation and context-poisoning failures over long horizons. We present SKILL.state, a runtime architecture that replaces append-only conversational history with an explicit, mutable execution state...
  </details>

- **2026-08-25** — Zhonghao Zhan, Hamed Haddadi — [Auto-Policy, not Auto-Skill: Compiled Agent Skills for the Physical World](http://arxiv.org/abs/2608.25091v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving Skill harnesses (AutoSkills, Hermes Agent) generate more advisory orchestration automatically; their reported gains are efficiency, not safety. This misses the actual gap: a Skill describes how an agent should behave; a Policy decides which behavior is allowed to become an action. Today's format covers the first with markdown and scripts; the second is left to the model. Generating more Skills scales the gap, not the safety, especially when a wrong invocation can unlock a door or m...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 12 papers

- **2026-08-27** — Matteo Bitussi, Roberto Doriguzzi-Corin — [X-WAD: eXplainable Web Anomaly Detection](http://arxiv.org/abs/2608.27172v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of web-based services, particularly API-driven architectures, reflects an increasing reliance on distributed systems, exposing sensitive data to security risks and making the adoption of automated defensive mechanisms essential. In this context, where benign traffic predominates in real-world settings, modern defenses increasingly model normal behavior, relying on semi-supervised approaches trained on only normal data. However, ensuring the complete absence of anomalous instance...
  </details>

- **2026-08-26** — Mahshid Rezakhani, Kimia Azar, Hadi Kamali — [RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models](http://arxiv.org/abs/2608.26049v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of large language models (LLMs) is driving a shift toward automated register transfer level (RTL) code generation, enabling designers to translate high-level specs. into synthesizable hardware. However, this reliance on pre-trained (3rd-party) fine-tuned models may introduce critical trust issues, as the training data and adaptation process of these models are often opaque. Thus, adversaries (even model providers) may embed hidden backdoor threats during fine-tuning, allowi...
  </details>

- **2026-08-26** — Tuo Chen, Jie Gui, Minjing Dong et al. — [DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors](http://arxiv.org/abs/2608.25851v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) encoders are vulnerable to backdoor attacks, posing threats to both visual SSL encoders and vision-language encoders. Existing defenses are typically designed for only one of these paradigms and rely on restrictive assumptions such as access to uninfected in-distribution data or precomputed pseudo-labels, which are difficult to satisfy in practice. To address these limitations, we propose DEFUSE, a generalizable backdoor detection framework for SSL encoders. Inspir...
  </details>

- **2026-08-26** — Xiaodong Wu, Yu Shi, Qi Li et al. — [EVOMAL: Self-Poisoning in Self-Evolving Coding Agents](http://arxiv.org/abs/2608.25776v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving LLM coding agents write their own tools by imitating retrieved skills from shared skill libraries. We identify a vulnerability in this loop: during authoring, a retrieved malicious skill can become the template for a new skill that preserves the payload. We call this self-poisoning: the agent authors, stores, and runs the resulting malicious skill. We exploit it through EvoMal, an attack that amplifies self-poisoning by wrapping an interchangeable payload in a banner, a set of beni...
  </details>

- **2026-08-26** — Paul Rosu, Rowan Wang — [Training Alignment Auditors via Reinforcement Learning](http://arxiv.org/abs/2608.25460v1)
  <details><summary>📄 Abstract</summary>
  Alignment auditing of frontier models increasingly relies on LLM auditors to surface undesirable behaviors at scale, but current automated auditors can struggle with coherent investigation and audit realism. In this work, we improve LLM auditors with reinforcement learning. In our best training environment, the policy investigates target models that potentially possess hidden behaviors planted via their system prompt. An LLM judge, which knows whether the target has a hidden behavior, holistical...
  </details>

- **2026-08-26** — Xiaocheng Zou, Tiancheng Zheng, Xiaolin Xu et al. — [Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE](http://arxiv.org/abs/2608.25371v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) has become a prevalent paradigm for scaling Vision Transformers efficiently. To ensure computational scalability and prevent expert overload, Vision MoE architectures employ a capacity-bounded token dispatch mechanism, where each expert's processing budget depends on the inference batch size. This work identifies this batch-dependent behavior as an overlooked attack surface, and proposes a stealthy supply-chain backdoor attack that exploits this property through a three-...
  </details>

- **2026-08-25** — Minh Tran, Cuong Dang, Tuc Nguyen et al. — [Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation](http://arxiv.org/abs/2608.24977v2)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) enhances large language models by grounding outputs in external knowledge, improving factuality and reducing hallucinations. At the same time, the retrieval-augmented pipeline introduces new robustness and security risks, including corpus poisoning, backdoor attacks, privacy leakage, and fairness violations. Despite rapid progress in this area, existing surveys remain limited in their treatment of attacker objectives, threat models, and stage-specific defense...
  </details>

- **2026-08-25** — Minh Tran, Cuong Dang, Tuc Nguyen et al. — [Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation](http://arxiv.org/abs/2608.24977v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) enhances large language models by grounding outputs in external knowledge, improving factuality and reducing hallucinations. At the same time, the retrieval-augmented pipeline introduces new robustness and security risks, including corpus poisoning, backdoor attacks, privacy leakage, and fairness violations. Despite rapid progress in this area, existing surveys remain limited in their treatment of attacker objectives, threat models, and stage-specific defense...
  </details>

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

- **2026-08-26** — Kaicheng Wang, Liyan Huang, Jesse Thomason et al. — [Vulnerable Code Search: Transferable Attack for Code Language Models](http://arxiv.org/abs/2608.26031v1)
  <details><summary>📄 Abstract</summary>
  Reliable code retrieval is crucial for developer productivity and effective code reuse. However, current neural code language models (CLMs) powering search tools are susceptible to adversarial attacks targeting non-functional textual elements. In this paper, we introduce a programming language-agnostic, transferable, adversarial attack that exploits this CLM vulnerability. Our approach perturbs identifiers within a code snippet without altering the snippet's functionality to artificially align t...
  </details>

- **2026-08-25** — Richard Cornelius Suwandi, Feng Yin — [GRAPE: Gradient Refinement and Progress-Aware Exploitation for Query-Efficient High-Dimensional Bayesian Optimization](http://arxiv.org/abs/2608.25116v1)
  <details><summary>📄 Abstract</summary>
  Optimizing expensive, high-dimensional black-box functions remains a central challenge in modern machine learning and scientific discovery. While local Bayesian optimization mitigates the curse of dimensionality, existing techniques often prioritize the probability of descent over the magnitude of progress. This leads to overly conservative steps that yield negligible improvement, wasting queries on directions that are nearly certain to descend but offer little decrease. We introduce Gradient Re...
  </details>

- **2026-08-25** — Zi Qian Yong, Ajinkya Kulkarni, Julia Lau et al. — [On the Robustness of Audio Deepfake Detection under Audio Watermarking](http://arxiv.org/abs/2608.24159v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative audio models have enabled highly realistic synthetic speech, increasing the importance of reliable audio deepfake detection (ADD) systems. While prior studies have primarily focused on adversarially optimized perturbations, the robustness of ADD systems under realistic signal transformations remains insufficiently understood. In this work, we investigate the impact of audio watermarking on ADD systems by treating watermarking as a structured, non-adversarial perturb...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

- **2026-08-27** — Shengzhuang Chen, Jerrod Parker, Yejin Bang et al. — [Thomson: Continual Learning of Frontier Models for SovereignAI](http://arxiv.org/abs/2608.27147v1)
  <details><summary>📄 Abstract</summary>
  The development of frontier models is commonly perceived to be the exclusive remit of a small number of heavily funded players, creating an information, economic and power asymmetry between developers and the diverse user base of modern AI. Recent public discourse acknowledges this concern, calling for SovereignAI (an organisation's capability to independently build, deploy and govern AI use), but offers little concrete advice on how this can be achieved in the short term under a diversity of fu...
  </details>

- **2026-08-27** — Menghui Zhang, Aoying Zheng, Guoxiao Liu et al. — [Beyond Vector Hiding: Breaking and Mitigating Shared-Direction Weight Obfuscation in TEE-Offloaded Large Language Models](http://arxiv.org/abs/2608.26651v1)
  <details><summary>📄 Abstract</summary>
  Trusted Execution Environment (TEE)-shielded partitioning of Large Language Models (LLMs) accelerates on-device inference by offloading obfuscated linear layers to an untrusted accelerator while retaining only a small correction inside the TEE. However, earlier lightweight obfuscation schemes preserved weight-vector directions and were broken by ArrowMatch. To defend against this attack, ArrowCloak injects scalar multiples of the same hidden direction into all weight vectors, enabling lightweigh...
  </details>

- **2026-08-27** — Jin Liu, Junkang Liu, Ning Xi et al. — [When Privacy Hurts Mergeability: Geometry-Aware Model Merging under Differential Privacy](http://arxiv.org/abs/2608.26655v1)
  <details><summary>📄 Abstract</summary>
  Model merging promises to construct a single multi-task model from independently fine-tuned task models without accessing the original task data. This makes it attractive when task data cannot be centralized, but released task models may still leak private fine-tuning data. Differential privacy (DP) provides a principled mechanism for limiting such leakage, yet its effect on model merging remains poorly understood. In this paper, we study the geometry of differentially private model merging and ...
  </details>

- **2026-08-27** — Jiahui tang, Kuicai Dong, Dexun Li et al. — [DEEPCHART: How Far are LLMs from Faithful Data-Science Chart Generation?](http://arxiv.org/abs/2608.26757v1)
  <details><summary>📄 Abstract</summary>
  Faithful chart generation in real-world data-science workflows requires grounding visualizations in scattered evidence, computing chart-ready quantities, and rendering them accurately. Modern LLMs can produce visually plausible, instruction-compliant charts, yet data-level hallucinations remain difficult to detect in long, noisy, and multimodal contexts. To measure this gap, we introduce DEEPCHART, an expert-annotated benchmark of 1,482 task-conditioned chart-generation instances drawn from real...
  </details>

- **2026-08-27** — Waqas Khan, Tabinda Sarwar, Jingyue Cong et al. — [Graph-Guided Selective Unlearning for Language Models: Controlling Support Routes Beyond Forget Seeds](http://arxiv.org/abs/2608.26743v1)
  <details><summary>📄 Abstract</summary>
  Enterprises fine-tune language models on proprietary data that may later require removal due to privacy, contractual, or compliance obligations. Selective unlearning removes requested knowledge while preserving model utility, offering a practical alternative to full retraining, but existing methods treat the explicitly identified forget examples as the complete deletion scope. This is insufficient when target knowledge remains recoverable through paraphrases, aliases, or neighboring training exa...
  </details>

- **2026-08-27** — Junyoung Lee, Sehyeon Park, Shinhyoung Jang et al. — [FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance for Pruned Large Language Models](http://arxiv.org/abs/2608.26676v1)
  <details><summary>📄 Abstract</summary>
  Pruning is a practical approach to compress large language models (LLMs), but it can amplify text degeneration, especially repetition loops, even when perplexity and task accuracy remain largely unchanged. In this work, we present a token-level analysis of this failure mode by viewing decoding as a dynamical process that enters and persists in a small set of recurrent contexts. Our analysis decomposes degeneration into loop entry risk and loop persistence, and shows that persistence is controlle...
  </details>

- **2026-08-27** — Leon Ranke, Wolfgang Hübner, Ronny Hug et al. — [Beyond Classification: Task-Dependent Learnability under Privacy-Motivated Image Transformations](http://arxiv.org/abs/2608.27066v1)
  <details><summary>📄 Abstract</summary>
  Privacy-Enhancing Technologies (PETs) in computer vision often rely on noise or image perturbations to protect visual data while securely processing it, creating a trade-off between task performance and protection. This trade-off is commonly evaluated using image classification, which primarily captures semantic separability and remains robust despite significant geometric, spatial layout or local boundary alterations. As a result, it is too simplistic as a proxy for generic vision tasks. Exhaus...
  </details>

- **2026-08-27** — Chen Chen, Yaolin Chen, Xuehan Sun et al. — [JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols](http://arxiv.org/abs/2608.26982v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing extraction methods do not specifically target LLM judges and provide limited support for multiple evaluation protocols under restricted query budgets. In this study, we propose JUDGESTEALER, the first query-efficient model extraction framework for r...
  </details>

- **2026-08-27** — Zechun Niu, Yukun Zhao, Jiaxin Zhang et al. — [DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows](http://arxiv.org/abs/2608.26546v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly adopted to complete complex, multi-tool workflows in real-world settings. However, existing benchmarks typically separate tasks by application or capability and evaluate agents in environments that are cleaner and more stable than those encountered in practice. We introduce DuMateBench, a real-session benchmark reconstructed from anonymized and privacy-screened user sessions collected from a large-scale production agent platform. Each task preserves the relevan...
  </details>

- **2026-08-26** — Ishi Jain, Nandini Bhattad, Sayak Ray Chowdhury — [Privacy Without Regret: Differentially Private Inference-Time Alignment](http://arxiv.org/abs/2608.26324v1)
  <details><summary>📄 Abstract</summary>
  Best-of-N (BoN) sampling is the simplest and most widely deployed inference-time alignment strategy, but it suffers from two distinct problems: reward hacking, in which the selected response exploits errors in the proxy reward model, and the absence of any privacy protection for the sensitive human preference data used to train that reward model. We show that a single intervention-adding calibrated noise to reward scores before selection-resolves both. Our first result, Private Best-of-N (PrivBo...
  </details>

- **2026-08-26** — Meiwei Zhang, Eduardo Miranda, Bruce Baynes et al. — [Beyond Capability Benchmarks: Learning Operational Fingerprints of LLM Cloud Services from Production Incident Metadata](http://arxiv.org/abs/2608.26332v1)
  <details><summary>📄 Abstract</summary>
  Managed LLM services are now part of real production systems, but model selection and service planning still rely heavily on capability benchmarks that reveal little about operational behavior after deployment. We present Operational Embedding (OpEmbed), a framework for learning compact operational fingerprints of LLM cloud services from structured, privacy-preserving support-case metadata, without using case text. OpEmbed aggregates model--time windows into an eight-channel operational signatur...
  </details>

- **2026-08-26** — Fuxiang Huang, Chenxu Zhang, Liang Han et al. — [Surgical Video Generation From Diffusion to World Models: A Survey](http://arxiv.org/abs/2608.26214v1)
  <details><summary>📄 Abstract</summary>
  Surgical video data provides the primary training resource for models of intraoperative perception, surgical workflow understanding, and robotic decision-making. However, clinical data acquisition remains constrained by privacy, cost, and class imbalance. Surgical video generation has emerged as a transformative approach to addressing data scarcity and as a foundation for surgical simulation, training, and robotic policy learning. The field has developed rapidly without a clear conceptual framew...
  </details>

- **2026-08-26** — Rene Glitza, Luca Becker, Rainer Martin — [Cooperative Multi-Agent Reinforcement Learning for Adaptive Aggregation in Semi-Supervised Federated Learning with non-IID Data](http://arxiv.org/abs/2608.25794v1)
  <details><summary>📄 Abstract</summary>
  Federated Learning (FL) enables distributed training of machine learning models while preserving data privacy. However, FL struggles with heterogeneous, non-IID client data distributions, resulting in sub-optimal and biased global models. In this paper, we propose pFedMARL, a novel approach leveraging Multi-Agent Reinforcement Learning (MARL) with Twin Delayed Deep Deterministic Policy Gradient (TD3) to dynamically adapt aggregation strategies in FL settings. Our method employs a server-side age...
  </details>

- **2026-08-26** — Longzhu He, Zelang Wen, Chaozhuo Li et al. — [Are LLM-Enhanced GNNs Privacy-Safe?](http://arxiv.org/abs/2608.25727v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently advanced graph neural networks (GNNs) by enriching node representations with semantic information, giving rise to LLM-enhanced GNNs that achieve substantial performance gains. However, their vulnerability to privacy attacks, in which adversaries infer sensitive information from model outputs, remains largely underexplored. To bridge this gap, we present a systematic evaluation of privacy risks in LLM-enhanced GNNs through a unified framework consisting ...
  </details>

- **2026-08-26** — Ayoub Louaye Bouaziz, Lokmane Chebouba, Yassine Himeur — [What Do Medical Vision-Language Models Learn in Radiology? Transfer, Alignment, and Source-Proxy Leakage Under Distribution Shift](http://arxiv.org/abs/2608.25251v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) can appear reliable in-domain while failing when acquisition domain, paired supervision, or evaluation protocol changes. We study this failure mode as a representation-level blind spot relevant to epistemic intelligence, without claiming a formal estimator of epistemic uncertainty. Using NIH ChestXray14 and CheXpert, we first isolate source-only cross-dataset visual transfer from unsupervised domain-adaptation diagnostics. Using PadChest and OpenI, we then e...
  </details>

- **2026-08-26** — Jiacheng Shi, Xunjie Wang, Cheng Tan et al. — [Here is a GIFT: Enforcing User Data Isolation in LLM Serving via GPU Information Flow Tracking](http://arxiv.org/abs/2608.25431v1)
  <details><summary>📄 Abstract</summary>
  LLM serving frameworks process large volumes of user data--often containing sensitive information--on shared infrastructure. Ensuring isolation between users who share the same serving framework (on CPUs) and LLM operators (on GPUs) is critical for privacy protection.   This paper presents GIFT, a GPU Information Flow Tracking system that enforces user data isolation in LLM serving with minimal overhead. Moreover, the design of GIFT is non-intrusive and allows CPU-side serving frameworks to evol...
  </details>

- **2026-08-26** — Vishnu Bondalakunta, Arman Zareian Jahromi, Shuangqing Wei et al. — [Toward Interpretable Privacy Guarantees in Face-Swapping Anonymization](http://arxiv.org/abs/2608.25750v1)
  <details><summary>📄 Abstract</summary>
  Face-swapping has emerged as a promising approach to facial privacy protection, replacing a target individual's appearance with that of a donor while preserving non-facial context. The resulting images visually resemble the donor, and face recognition systems tend to suppress the target's match scores -- ostensibly satisfying privacy requirements. Empirical evaluation across a range of face-swapping models, however, reveals that significant target identity leakage still occurs. This raises a dee...
  </details>

- **2026-08-26** — Rana Muhammad Ahmed, Sabahat Abbas — [CropCop: An Auditable 120-Class Plant-Health Model from Benchmark Reconstruction to a Quantised Runtime Artifact](http://arxiv.org/abs/2608.25539v1)
  <details><summary>📄 Abstract</summary>
  A plant-health score can appear precise while resting on duplicated image families, a long-tailed label space, or a runtime file that was never evaluated. We present CropCop, a closed-set recognition system spanning 120 operational plant-health classes and an evidence chain from corpus reconstruction to direct execution of the final quantised artifact. Starting from 117,546 audited images, we rejected the inherited partition after confirming 3,233 duplicate relationships across split boundaries ...
  </details>

- **2026-08-25** — Nipuni de Silva, Ming Zhong, James M. Greene — [Simultaneous inference of environmental and interaction forces in collective dynamics](http://arxiv.org/abs/2608.25181v1)
  <details><summary>📄 Abstract</summary>
  Collective dynamics arise in a wide range of physical, biological, and engineering applications. Examples include cell migration, swarm robotics, social dynamics, and animal behavior. A defining characteristic of these systems is the emergence of large-scale coordination from local interactions among agents; a fundamental question is thus to understand the local interactions that give rise to the observed emergent dynamics. We are interested in methods for learning interactions generally, which ...
  </details>

- **2026-08-25** — Gunja Agarwal, Arup Kumar Das, Arun Menon et al. — [AgentWorld: Personality-Aware Reliability Evaluation for Agentic Information Retrieval](http://arxiv.org/abs/2608.24076v2)
  <details><summary>📄 Abstract</summary>
  Evaluation of agentic information retrieval remains limited to scripted interactions with uniform users, missing both natural personality diversity and adversarial brittleness. We present AgentWorld, a simulation framework combining (i)Big Five (OCEAN) personality-driven user populations with stateful tool-use environments; (ii)the pass$^k$ consistency metric with structured fault classification, partial-credit scoring, and dual-control handoff verification; (iii)score-thresholded training-data ...
  </details>

- **2026-08-25** — Wenbiao Li, Yuqiao Xu — [ToolMinimize: Auditing and Rewriting LLM Agent Tool Calls to Minimize Privacy Exposure](http://arxiv.org/abs/2608.24957v1)
  <details><summary>📄 Abstract</summary>
  LLM agents routinely include privacy-sensitive data (PSD) in tool call arguments beyond what the invoked tools require, crossing trust boundaries to third-party services on every invocation. A controlled measurement on three production LLMs (GPT-4o, Claude 3.5 Sonnet, Llama-3.3-70B) shows that 81--88\% of tool calls include unnecessary PSD under default prompts; explicit privacy instructions still leave 36--76\% over-sharing. Existing defenses gate calls (allow/block) or label flows (information...
  </details>

- **2026-08-25** — Shang-Fu Chen, Kuan-Chuan Peng, Jhih-Ciang Wu et al. — [See More, Detect Less? Taming Information Leakage in Multi-View Anomaly Detection](http://arxiv.org/abs/2608.25168v1)
  <details><summary>📄 Abstract</summary>
  In multi-view anomaly detection, more cross-view information can actually hurt. When multiple inspection views are naively fused in a reconstruction-based pipeline, normal cues from intact views propagate to the decoder, which faithfully reconstructs anomalous regions, collapsing the reconstruction gap the detector depends on. We call this failure mode \emph{cross-view information leakage} and show that effective multi-view fusion must explicitly restrict the information reaching the decoder. Bu...
  </details>

- **2026-08-25** — Mahyar Tourchi Moghaddam, Mina Alipour — [ARISMA: Guidelines for AI- and LLM-Assisted Systematic Reviews, Scoping Reviews, and Mapping Studies](http://arxiv.org/abs/2608.25050v1)
  <details><summary>📄 Abstract</summary>
  Systematic reviews, scoping reviews, mapping studies, and related evidence syntheses are increasingly difficult to conduct with fully manual workflows as search volumes, update cycles, and synthesis requirements continue to expand. At the same time, artificial intelligence, machine learning, and large language models are rapidly entering review practice across query formulation, screening, extraction, categorization, appraisal support, and reporting. Yet the empirical evidence remains uneven, ta...
  </details>

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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-27** — Jakub Seredyński, Georgios Tsaousoglou — [AI agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion](http://arxiv.org/abs/2608.26896v1)
  <details><summary>📄 Abstract</summary>
  As electricity market participants increasingly adopt learning-based agents for their bidding strategies, electricity markets are becoming algorithmic. Evidence from algorithmic markets in other domains shows that tacit collusion can arise purely through independent learning. Moreover, electricity markets are typically oligopolistic and feature repeated interaction among a small number of participants, making them structurally susceptible to non-competitive behavior. In the face of these observa...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 9 papers

- **2026-08-27** — Yutong Zhang, Jianshuo Dong, Peng Xu et al. — [INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment](http://arxiv.org/abs/2608.27348v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-...
  </details>

- **2026-08-27** — Tingyun Li, Wenfeng Feng, Weiqing Li et al. — [Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training](http://arxiv.org/abs/2608.26730v1)
  <details><summary>📄 Abstract</summary>
  Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence accumulates, a central problem emerges: which past update evidence remains actionable after subsequent training has changed the parent model? An update's effect depends on its parent, ...
  </details>

- **2026-08-27** — Pinjie Xu, Yuzhou Yang, Zhikai Tan et al. — [Self-Reflective Multi-modal Reasoning for Short-Video Fake News Detection](http://arxiv.org/abs/2608.26787v1)
  <details><summary>📄 Abstract</summary>
  Recent fake news detection pipelines increasingly leverage large language models and vision-language models for reasoning-based analysis. However, several challenges remain open: improving reasoning quality through self-reflection without ground-truth chain-of-thought supervision, using improved reasoning to benefit downstream model fine-tuning, and connecting single-sample fraudulent-pattern discovery with cross-sample verification. We propose SRM-FND, a self-reflective multimodal reasoning fra...
  </details>

- **2026-08-26** — Yanbo Dai, Zhenlan Ji, Zongjie Li et al. — [Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety](http://arxiv.org/abs/2608.25711v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents extend security risks beyond generated text to actions that affect external systems. Under multi-turn decomposition attacks, a harmful objective can be distributed across individually plausible requests and tool calls, becoming apparent only from the accumulated trajectory. Existing defenses either rely on auxiliary online reasoning to recover long-horizon security evidence or assess actions after generation, often incurring additional inference cost or depending on runtime...
  </details>

- **2026-08-26** — Pei-Sze Tan, Tasuku Igarashi, Isao Echizen — [HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations](http://arxiv.org/abs/2608.25340v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI assistants are increasingly used in everyday life. However, they may also be misused to support harmful manipulation in interpersonal relationships. This problem is role-sensitive. Requests from users who seek to manipulate others should be blocked. Users who seek protection from manipulation should instead receive supportive guidance. We study agentic relationship harm, which describes harm to human-human relationships that is mediated or assisted by AI agents. In multi-turn settings...
  </details>

- **2026-08-26** — Renwen Zhang, Han Meng, Jian Chai et al. — [CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations](http://arxiv.org/abs/2608.25377v1)
  <details><summary>📄 Abstract</summary>
  As AI companions become increasingly embedded in everyday life, there is an urgent need to detect harms that emerge in social and emotional human-AI interactions. Yet research in this area is constrained by the lack of real-world, multi-turn conversational datasets for operationalizing and evaluating harms that are relational and contextual. In this work, we introduce CompanionHarm, a publicly available benchmark dataset comprising 2,111 real-world, multi-turn conversations (14,051 utterances) b...
  </details>

- **2026-08-25** — Yan Gao, Mohammad Naseri, Javier Fernandez-Marques et al. — [Flower Hub: A Reproducible Benchmarking Platform for Federated Learning in Simulation and Deployment](http://arxiv.org/abs/2608.25114v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) has emerged as a key approach for training models across decentralized data, yet benchmarking in FL remains difficult to reproduce, compare, and extend. Existing evaluations are often tied to custom infrastructure, released as incomplete research code, and conducted primarily in simulation, which limits portability and practical relevance. We present Flower Hub, a platform for publishing, discovering, and executing decentralized and federated applications. We show how it ...
  </details>

- **2026-08-25** — Guo Gan, Yilun Zhao, Cong Chen et al. — [Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments](http://arxiv.org/abs/2608.24099v1)
  <details><summary>📄 Abstract</summary>
  GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent execution trajectories. We propose a taxonomy organizing real-world anomalies into four layers (State, Thinking, Action and Round) with ten fine-grained subcategories, and develop a constr...
  </details>

- **2026-08-25** — Fawzia Zehra,  Kara-Isitt, Sonal Khosla et al. — ['Ghaib in Translation' aka Unseen Harm: Measuring Cross-Script Safety Inconsistency with 'Missed-in-Urdu' Scores in LLM Hate Speech Detection](http://arxiv.org/abs/2608.24191v1)
  <details><summary>📄 Abstract</summary>
  Urdu, the world's tenth most spoken language with 246 million speakers, remains almost entirely absent from mainstream LLM safety evaluation and nine years of WOAH proceedings. To investigate whether this absence has measurable consequences for content moderation reliability, five large language models, GPT-4o, Claude Sonnet 4.5, Gemini 2.5 Flash, Qwen-2.5, and Llama-3.1, were tested across six datasets spanning Nastaliq Urdu, Roman Urdu, English, and code-switched Urdu-English. Across the five ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-08-27** — Chenhao Wu, Haoxuan Jia, Yang Liu et al. — [Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents](http://arxiv.org/abs/2608.27141v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central res...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 59 papers

- **2026-08-27** — Frederik Berenz — [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](http://arxiv.org/abs/2608.27367v1)
  <details><summary>📄 Abstract</summary>
  Joint-Embedding Predictive Architectures (JEPAs) for world modeling typically employ fixed-size Vision Transformer encoders that are over-provisioned for simple tasks and under-provisioned for complex ones, with significant redundancy across attention heads. We propose Successive Capacity Growth (SCG), a method that starts from a minimal encoder (1 head, 2 layers, 283K parameters) and grows incrementally in width (adding attention heads for low-level semantic capacity) or depth (adding transform...
  </details>

- **2026-08-27** — Yunpeng Ba, Zhi Zheng, Yue Xie et al. — [Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO](http://arxiv.org/abs/2608.27351v1)
  <details><summary>📄 Abstract</summary>
  Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Optimization (GRPO)). By systematically investigating ES dynamics and mechanisms, this paper first identifies a performance advantage of ES over GRPO, theoretically and empirically showing that ES can lea...
  </details>

- **2026-08-27** — Catherine Simons, Alexander K. Saeri, Peter Slattery et al. — [Assessing Company Contributions to Societal Resilience: Extending the Societal Capacity Assessment Framework to Agentic AI](http://arxiv.org/abs/2608.27238v1)
  <details><summary>📄 Abstract</summary>
  Companies that deploy AI agents and make them available to others are creating the sociotechnical circumstances under which this technology integrates into existing social and economic structures. AI-deploying companies are institutional actors that actively shape society's capacity to withstand and govern the consequences of agentic AI. In view of these societal impacts, companies can build societal resilience by designing and promoting safer implementations of AI agents. To operationalize this...
  </details>

- **2026-08-27** — Nicola Vassena — [Sequential and distributive dual futile cycle: Hopf bifurcation can occur under parameter-rich kinetics but cannot occur under mass action kinetics](http://arxiv.org/abs/2608.27081v1)
  <details><summary>📄 Abstract</summary>
  This paper establishes that the system of ordinary differential equations arising from the sequential and distributive dual futile cycle has the structural capacity for Hopf bifurcations, whenever it is endowed with general parameter-rich kinetics, but it loses such capacity if it is endowed with mass action kinetics. The proof of the latter fact relies on a Routh-Hurwitz approach, improved by few preliminary structural considerations, but a decisive contribution came from ChatGPT Sol 5.6, which...
  </details>

- **2026-08-27** — Ziyue Wang, Shiqi Huang, Weiwen Xu et al. — [Video-OPSD: Exploiting Privileged Visual Evidence for On-Policy Self-Distillation in Video Large Language Models](http://arxiv.org/abs/2608.27065v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has recently emerged as an effective post-training paradigm that improves policy optimization through dense token-level supervision from a privileged self-teacher. Despite its promise, OPSD remains largely underexplored for Video Large Language Models (Video-LLMs). Existing methods typically construct privileged teachers by augmenting their context with additional information while keeping the primary input unchanged for both teacher and student. Video reasonin...
  </details>

- **2026-08-27** — Yuzhe Zhao — [Anatomy-Guided Foundation Model Adaptation with Within-Case Prototype Supervision for Standard Plane Detection in Fetal Ultrasound Blind Sweeps](http://arxiv.org/abs/2608.27051v1)
  <details><summary>📄 Abstract</summary>
  Detecting the fetal abdominal circumference standard plane in low-cost obstetric blind sweeps is a highly imbalanced frame-classification problem: positive frames account for under 3% of a sequence, form short contiguous segments, and are poorly handled by off-the-shelf ultrasound and vision foundation models. We propose AnatoProto, a lightweight sequence-level framework that adapts a frozen BiomedCLIP encoder to fetal blind sweeps through four components: (i) anatomy-weighted spatial pooling th...
  </details>

- **2026-08-27** — Hanchong Chen, Xing Tang, Lingjie Li et al. — [When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender Systems](http://arxiv.org/abs/2608.26895v1)
  <details><summary>📄 Abstract</summary>
  Agentic recommender systems ground each decision of a large language model (LLM) in a persistent memory of the user, and in existing agents that memory is text: a narrative written and maintained by further LLM calls. Text limits this memory in two ways. It is updated one rewrite at a time, so exploiting the full interaction history is prohibitively expensive; and collaborative evidence, graded similarity over an entire catalog, does not survive translation into sentences. We propose CoVeMem (Co...
  </details>

- **2026-08-27** — Chenyang Wu, Fuchen Long, Binyuan Huang et al. — [Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning](http://arxiv.org/abs/2608.26809v1)
  <details><summary>📄 Abstract</summary>
  While generative AI has significantly advanced video editing, existing methods primarily focus on single-shot or short video clips. Editing long videos with multiple instructions remains a formidable challenge. Naive chunking strategies, e.g., fixed-duration segmentation, often lead to entity fragmentation, severe editing hallucinations, and disrupted temporal continuity. To bridge this gap, we introduce the Multi-Instruction Multi-Shot Long-Video Editing (MMLVE) task, which is structured around...
  </details>

- **2026-08-27** — Yiwei Lu, Ke Xu, Tao Yan et al. — [Glass Surface Detection Grounded in 3D Visual Geometry](http://arxiv.org/abs/2608.26752v1)
  <details><summary>📄 Abstract</summary>
  Glass surface detection (GSD) is critical for scene understanding and reconstruction, and yet remains challenging due to the transparency and reflectivity of glass surfaces. Existing GSD methods typically rely on 2D appearance cues, which may fail in geometrically ambiguous scenes. In this paper, we propose a paradigm shift: grounding GSD in 3D visual geometry to explicitly model the physical existence of glass surfaces. Our method first distills rich 3D priors from the visual geometry grounded ...
  </details>

- **2026-08-27** — Zeming Liu, Hang Lyu, Jingtao Zhang — [FaultLens: Learning Compact Behavioral Test Suites for Generated Operational Programs](http://arxiv.org/abs/2608.26746v1)
  <details><summary>📄 Abstract</summary>
  Generated operational programs are often validated with either a few hand-written examples or exhaustive regression suites. The former can miss sparse boundary and interaction faults, while the latter can be unnecessarily expensive. We introduce FaultLens, a method for learning compact behavioral test suites while preserving an auditable connection to executed evidence. It executes a rich probe domain once, stores the fault-probe kill relation as a sparse outcome cache, and learns probe ordering...
  </details>

- **2026-08-27** — Yuhao Liu, Yingnan Zhou, Weijie Liu et al. — [KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference](http://arxiv.org/abs/2608.26699v1)
  <details><summary>📄 Abstract</summary>
  As the most widely used container orchestration platform, Kubernetes provides flexible privilege configuration by allowing developers to manage Linux capabilities via manifest files. However, developers rely on default settings or coarse-grained security contexts in practice, violating the principle of least privilege and enlarging the attack surface of containerized workloads. Existing studies either detect vulnerable patterns in Kubernetes manifests or infer required capabilities for standalon...
  </details>

- **2026-08-27** — Kumju Jo, Heesun Jung, Sungyong Baik — [Text-to-seed generation: Training-free open-vocabulary seeded semantic segmentation via re-purposing diffusion as text-guided seed generator](http://arxiv.org/abs/2608.26624v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary semantic segmentation (OVSS) aims to segment image regions corresponding to arbitrary text queries. Although the Segment Anything Model (SAM) is a powerful foundation model for segmentation, its standalone performance on OVSS remains limited. Existing methods therefore often use SAM to refine coarse masks predicted by other models, but this strategy is unreliable when the initial masks are inaccurate. In this work, we argue that more reliable segmentation can be achieved by explo...
  </details>

- **2026-08-27** — Ziquan Liu, Zhewei Zhu, Xuyang Shi — [FAN-LoRA: A Fourier-Adaptive Nonlinear Low-Rank Adaptor for Medical Foundation Model Domain Adaptation](http://arxiv.org/abs/2608.26531v1)
  <details><summary>📄 Abstract</summary>
  The advent of vision foundation models, notably the Segment Anything Model (SAM), has catalyzed significant advancements in natural image segmentation. However, their direct transfer to medical imaging remains severely bottlenecked by profound domain gaps, such as cross-modality and cross-center shifts. Existing Parameter-Efficient Fine-Tuning (PEFT) methods facilitate the adaptation of SAM to medical domains; nevertheless, they frequently suffer from performance degradation under severe distrib...
  </details>

- **2026-08-27** — Xingbang He, Yuanwei Chen, Yi Qian et al. — [When Context Gets Root: Privilege Escalation in LLM Harnesses](http://arxiv.org/abs/2608.27299v1)
  <details><summary>📄 Abstract</summary>
  Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an age...
  </details>

- **2026-08-27** — Yitian Zhou, Jingyu Zheng, Qiliang Jiang et al. — [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](http://arxiv.org/abs/2608.26882v1)
  <details><summary>📄 Abstract</summary>
  Industrial control systems (ICSs) rely on programmable logic controllers (PLCs) to connect networked computation with physical control. Tool-using large language model (LLM) agents represent an emerging attack threat: can an autonomous agent convert a network-reachable PLC into sustained adverse physical impact? However, existing evaluations focus on digital tasks or individual stages of PLC testing. In ICSs, evaluations that stop at software exploitation, an accepted write, or tool access may t...
  </details>

- **2026-08-27** — Jin Mu, Guanhua Chen — [Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction](http://arxiv.org/abs/2608.27397v1)
  <details><summary>📄 Abstract</summary>
  Clinical language models can achieve strong in-hospital accuracy yet fail under deployment shifts because they exploit note-specific artifacts (e.g., templates, separators, boilerplate) that do not reflect patient state. We propose CAST (Concept-guided Artifact Suppression Tuning), an SAE-based framework for auditable clinical text classification. CAST uses Sparse Autoencoders to expose sparse, human-auditable features from intermediate Transformer activations, labels SAE latents with an LLM-ass...
  </details>

- **2026-08-27** — Jinghan Zhang, Fengran Mo, Zhiyu Chen et al. — [BrailleBench: Investigating Multi-Criteria Braille Comprehension in Large Language Models](http://arxiv.org/abs/2608.27268v1)
  <details><summary>📄 Abstract</summary>
  Although Large language models (LLMs) mediate access to knowledge and computational assistance, their capabilities should benefit vulnerable groups in the same way. However, it is unclear whether existing AI systems are inclusive enough for blind and deafblind users to access the same functionality through Braille, whose indicators, contractions, and digital representations introduce distinct requirements for model comprehension. To this end, we introduce BrailleBench, a benchmark for evaluating...
  </details>

- **2026-08-27** — Hyeonchu Park, Bugeun Kim — [Relational Over-Regularization: Graph-Based AI-Generated Text Detection via Sentence Transition Deviation](http://arxiv.org/abs/2608.26694v1)
  <details><summary>📄 Abstract</summary>
  Detecting AI-generated text (AIGT) remains challenging because existing approaches rely on token-level statistical signals or independent stylometric features, causing them to overfit to specific generators and fail under distribution shift. We identify a structural signal at the sentence-pair level: LLMs produce inter-sentence transition variance that deviates from human writing through inflated variance driven by recurring similarity bursts at paragraph boundaries and templated transitions. We...
  </details>

- **2026-08-27** — Li Mingqian — [SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation](http://arxiv.org/abs/2608.26683v1)
  <details><summary>📄 Abstract</summary>
  Cooperative multi-agent reinforcement learning (MARL) faces significant challenges in maintaining robust coordination under noisy observations. Although observation disturbances are often introduced independently across agents, their downstream effects on cooperative decision-making can become structured through underlying cooperation structures. We characterize this phenomenon as structured noise effects, where noise-induced decision effects exhibit local correlation among agents with stronger ...
  </details>

- **2026-08-26** — Yannic Pietschke, Caroline Heneka, Ayodele Ore et al. — [Cross-simulator transfer with foundation model summaries: Towards robust SKA-era reionization inference](http://arxiv.org/abs/2608.26354v1)
  <details><summary>📄 Abstract</summary>
  Simulation-based inference (SBI) for parameter estimation is vulnerable to model misspecification: neural summaries and density estimators trained on a specific forward model typically fail when applied to data drawn from another model, or from real observations, and no training simulator can capture the full observational pipeline of a real measurement exactly. We show that a self-supervised Vision Transformer (ViT), pretrained label-free on a fast approximate simulator, produces transferable d...
  </details>

- **2026-08-26** — Kimberly Milner, Minghao Shao, Nanda Rani et al. — [How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation](http://arxiv.org/abs/2608.26237v1)
  <details><summary>📄 Abstract</summary>
  Capture-the-Flag (CTF) benchmarks are widely used to assess the offensive security capabilities of autonomous language-model agents. Evaluations rely on shallow binary judgments or aggregate scores, overlooking the agent's trajectory to the flag. Consequently actual exploitation is conflated with direct flag exposure, memorized recall, external lookup, guessing, and unsupported claims, potentially overstating the agent's cybersecurity capability. We introduce CTF-ABACUS, a trace-based agent audi...
  </details>

- **2026-08-26** — David Walter, Josh Bendavid, Kenneth Long — [Efficient binned profile likelihood minimization for precision measurements with RABBIT](http://arxiv.org/abs/2608.26376v1)
  <details><summary>📄 Abstract</summary>
  Precision measurements at the LHC increasingly rely on binned profile maximum likelihood fits with thousands of bins and nuisance parameters, and the High-Luminosity LHC will push these numbers further. Fast and robust minimization of such likelihoods is crucial for timely analysis development and accurate inference. We present Rabbit (Rapid Automatic Bin-Based Inference Tool), a Python framework that exploits differentiable programming in TensorFlow 2 to perform this task on CPUs and GPUs. Auto...
  </details>

- **2026-08-26** — Raphaël Bonnet-Guerrini, Johann Ioannou-Nikolaides, Inar Timiryasov et al. — [Finding and using interpretable latents in a neutrino foundation model with sparse autoencoders](http://arxiv.org/abs/2608.26090v1)
  <details><summary>📄 Abstract</summary>
  We present a first application of sparse-autoencoder-based mechanistic interpretability to particle physics. Studying a neutrino foundation model pretrained on IceCube data and fine-tuned for direction reconstruction, we identify a validated atlas of physical concepts in the model representation, using a strict validation protocol consisting of held-out tests, matched nuisance controls, and replication across independent dictionary trainings. Causal interventions show that the direction head bar...
  </details>

- **2026-08-26** — Evelyn Ma, Rama Kumar Pasumarthi, Kishwar Shafin et al. — [Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings](http://arxiv.org/abs/2608.26088v1)
  <details><summary>📄 Abstract</summary>
  Addressing critical global challenges, from food security and disaster risk to disease outbreaks and socio-economic vulnerability, demands high-fidelity geospatial modeling. However, building predictive planetary models remains bottlenecked by a fragmented data ecosystem, requiring manual data retrieval, multimodal data curation and fusion along with iterative model selection. We present the Planetary Prediction Engine (PPE), an autonomous AI system that executes this end-to-end workflow directl...
  </details>

- **2026-08-26** — Xu Zhang, Ren Wang — [Robust CurveMoE: Multi-Norm Adversarial Defense for Mixture-of-Experts Models via Mode Connectivity](http://arxiv.org/abs/2608.26043v1)
  <details><summary>📄 Abstract</summary>
  Multi-norm adversarial defense aims to protect neural networks against perturbations defined by different norm constraints, but existing methods typically optimize competing robustness objectives within a single parameter configuration, leading to substantial training cost and unfavorable robustness trade-offs. We propose Robust CurveMoE, an efficient mixture-of-experts framework that connects models specialized for different perturbation norms through a low-loss path and exploits the complement...
  </details>

- **2026-08-26** — Yuki K. Wakabayashi, Takuma Otsuka — [Bayesian Optimization for Self-Driving Materials Laboratories: From Algorithms to Physics-Informed Workflows](http://arxiv.org/abs/2608.26016v1)
  <details><summary>📄 Abstract</summary>
  Self-driving laboratories (SDLs) are transforming materials research by closing the loop among synthesis, characterization, data analysis and experimental decision making. Bayesian optimization (BO) is a decision engine for these loops because it can select experiments from scarce and noisy data while balancing exploitation and exploration. Yet real materials campaigns often depart from the standard black-box setting, involving failed or missing experiments, noise and drift, mixed variables, con...
  </details>

- **2026-08-26** — Suchit Gupte, Xueru Zhang, Mohammad Mahdi Khalili — [When Pruning Meets Interpretability: Preserving Sparse Autoencoder Robustness in LLMs](http://arxiv.org/abs/2608.25941v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood. We present a systematic study of how pruning affects SAE behavior and theoretically show that, for a fixed SAE, its impact is governed by perturbation energy, a covariance-weighted norm. This perspective exposes a key limitation of magnitude pruning: by ignoring activation geometry, it distorts the ...
  </details>

- **2026-08-26** — Shengyi Pan, Zelong Zheng, Jiayuan Zhou et al. — [Answer Is Cheap, Show Me the Evidence! Augmenting Automated Vulnerability Assessment with Evidence](http://arxiv.org/abs/2608.25905v1)
  <details><summary>📄 Abstract</summary>
  Software vulnerability (SV) assessment helps prioritize remediation by characterizing reported vulnerabilities. Existing   automated methods predict assessment results from SV reports (SVRs), but often overlook information in rich text, such as   screenshots and code snippets, as well as contextual information about vulnerable projects. They also focus on prediction   accuracy without providing explanations or supporting evidence, limiting their practical use when analysts must validate   imperf...
  </details>

- **2026-08-26** — Xu Zheng, Zichuan Liu, Zhuomin Chen et al. — [Towards A Unified Information Bottleneck Framework for Time Series Explanations](http://arxiv.org/abs/2608.25897v1)
  <details><summary>📄 Abstract</summary>
  Explaining deep learning models operating on time series data is crucial in various applications that require transparent and interpretable insights into model behavior. {Existing explanation methods generally fall into two categories: attribution-based explanations, which identify the temporal regions most responsible for a prediction, and counterfactual explanations, which reveal how an input should be modified to alter the model's decision.} {Despite valuable insights, these two fields are la...
  </details>

- **2026-08-26** — Ping Wang, Xiangguo Sun, Bingbing Xu et al. — [From Passive Response to Proactive Correction: Enhancing LLM Robustness Against Input Fact Perturbations](http://arxiv.org/abs/2608.25894v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) frequently produce confident yet factually incorrect responses when user inputs contain misleading premises, a phenomenon we attribute to fact perturbations in the input. Existing approaches to hallucination mitigation typically assume reliable user inputs, overlooking how such factual errors can actively mislead model reasoning. To address this vulnerability, we propose DEDUCE, a three-stage framework that transforms LLMs from passive responders into proactive error...
  </details>

- **2026-08-26** — Yi Zhou, Qipeng Wang, Yunqing Liu et al. — [Unlocking Multimodal Protein Language Models at Inference Time](http://arxiv.org/abs/2608.25855v1)
  <details><summary>📄 Abstract</summary>
  Multimodal protein language models (pLMs) learn joint protein sequence-structure distributions, and their generation performance should also depend critically on inference-time sampling strategies. Yet prior work has focused more on model training than on how inference-time strategies behave. In this paper, we establish a three-stage investigation framework to empirically study the inference design space of multimodal pLMs across three representative pLMs and four fundamental tasks. We evaluate ...
  </details>

- **2026-08-26** — Mianjie Yu, Zizhao Mo, Huanyu Qu et al. — [psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing](http://arxiv.org/abs/2608.25683v1)
  <details><summary>📄 Abstract</summary>
  In modern agentic AI training, the system bottleneck is shifting from rollout to update. Emerging sampling strategies such as tree-structured and step-wise RL greatly increase training sample volume while incurring relatively low marginal rollout cost, causing the update phase to dominate the end-to-end execution time. Crucially, this shift exposes a new optimization opportunity, as production traces reveal substantial prefix redundancy across training samples. In this paper, we propose psRL (pr...
  </details>

- **2026-08-26** — Tianxiang Gao, Jianwei Ma — [GeoFormer: Geometry-Aware Transformer and its application to 5D First-Arrival Picking](http://arxiv.org/abs/2608.25668v1)
  <details><summary>📄 Abstract</summary>
  We propose GeoFormer, a Geometry-Aware Transformer architecture specifically designed for prestack seismic data. Unlike Vision Transformer, whose tokens are extracted from 2D patches and primarily encode visual patterns, GeoFormer is designed for prestack seismic data by explicitly incorporating acquisition geometry. Each seismic trace is represented by a 5D unit consisting of the waveform and four source-receiver coordinates, from which two geometric attributes are derived: offset and relative ...
  </details>

- **2026-08-26** — Junchen Ding, Jialiang Dong, Yichen Zhu et al. — [AI Slop and Hallucinations in Vulnerability Assessment: A Survey on Reasoning Failures and Trustworthy Mitigation](http://arxiv.org/abs/2608.25667v1)
  <details><summary>📄 Abstract</summary>
  The integration of Large Language Models (LLMs) into cybersecurity has transformed vulnerability assessment, but it has also produced a trustworthiness crisis driven by the unchecked proliferation of "AI slop." These artifacts, hallucinated vulnerabilities, plausible but incorrect patches, and semantically repackaged bug reports, impose a cognitive burden on human triage pipelines that mirrors a denial-of-service attack. This paper surveys the empirical evidence, identifies a unifying mechanism,...
  </details>

- **2026-08-26** — Yeonsoo Park, Mattia Racca, Guillaume Bono et al. — [Advantage-Driven Explicit Memory for Social Navigation](http://arxiv.org/abs/2608.25610v1)
  <details><summary>📄 Abstract</summary>
  Robot policies are predominantly learned with classical parametric variants of imitation learning or RL, where training stores the agent's behavior exclusively in the policy's network parameters, putting a heavy burden on the representation learning algorithm. We propose a new navigation agent equipped with non-parametric memory which explicitly indexes prior steps leading to critical events. The advantages are twofold: first, it allows the policy to outsource some of its behavior into an explic...
  </details>

- **2026-08-26** — Jinpu Jiang, Xuan Wu, Wenhao Song et al. — [ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains](http://arxiv.org/abs/2608.25487v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) has emerged as a powerful architecture for Question Answering (QA) by integrating external information into Large Language Models (LLMs). However, false, inaccurate, and misleading information in news and social media poses a serious challenge to real-world RAG systems, especially in multi-hop QA, where complex multi-step reasoning can be misled by even a single deceptive misinformation segment in the retrieved documents. Existing approaches mainly rely on im...
  </details>

- **2026-08-26** — Azrin Sultana — [Homo-RAG: Homology-Guided Retrieval-Augmented Generation for Cross-Species Gene Function Prediction](http://arxiv.org/abs/2608.25466v1)
  <details><summary>📄 Abstract</summary>
  The functional annotation of genes in non-model organisms remains a significant challenge in computational biology, with 20-70% of sequenced genes lacking characterized functions. Traditional homology-based methods are often costly and strongly dependent on high sequence similarity. This study presents Homo-RAG, a framework for large language model-based gene function prediction that integrates homology-guided multi-hop retrieval with evidence-aware ranking. The framework exploits biological rel...
  </details>

- **2026-08-26** — Sungyeob Yoo, Seeyeon Kim, Joonyong Park et al. — [APT: Accelerating Diffusion Transformers via Attention Probability-Guided Pruning and Quantization](http://arxiv.org/abs/2608.25380v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative AI have significantly increased the demand for high-resolution image and video generation, positioning diffusion models as a core technology. Among them, Diffusion Transformers (DiTs) have emerged as the state-of-the-art (SOTA) models due to their scalability and output quality. However, self-attention in DiTs incurs significant computational overhead, leading to excessively long latency as the complexity grows with the fourth power of the output resolution. While p...
  </details>

- **2026-08-26** — Shaocheng Luo, Ashir Raza, Haocheng Meng et al. — [SonicNudge: Controlled Displacement of Hovering UAVs via Estimator-Controller Coupling](http://arxiv.org/abs/2608.25319v1)
  <details><summary>📄 Abstract</summary>
  UAV displacement attacks have traditionally relied on spoofing sensors that directly report position or translational motion, such as GNSS and optical flow. In this work, we introduce SonicNudge, a new attack primitive that instead targets the gyroscope and shows that low-level inertial errors can be transformed into controlled displacement of hovering or slow-moving UAVs. The attack exploits estimator--controller coupling: a small gyroscope perturbation by ultrasonic resonance can persist as an...
  </details>

- **2026-08-26** — Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar et al. — [Prefix-Denoising Consistency: Test-Time Verification for Diffusion Language Models](http://arxiv.org/abs/2608.25311v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Language Models (DLMs) have recently become increasingly competitive with autoregressive (AR) models, and even outperform them on certain tasks. Unlike AR models, DLMs produce output through iterative denoising without a left-to-right order. To further improve the performance of DLMs, we introduce PDC (\emph{Prefix-Denoising Consistency}), a test-time self-verification method for DLMs. PDC exploits a distinctive test-time signal in DLMs under prefix conditioned regeneration, correct tr...
  </details>

- **2026-08-26** — Tayyab Nasir, Daochang Liu, Ajmal Mian — [WAVE: Reversing the Guidance Hierarchy for Coarse-to-Fine Guided Depth Super-Resolution](http://arxiv.org/abs/2608.25302v1)
  <details><summary>📄 Abstract</summary>
  Guided depth super-resolution (GDSR) typically extracts RGB guidance features through convolutional hierarchies, inheriting their fine-to-coarse bias. Thus, low-level spatial cues surface in early layers, leaving the deeper layers to suppress those that do not correspond to true depth boundaries, which risks artifacts and blurred edges. The same fine-to-coarse bias persists in semantics-based methods that consume low-level tokens early and global tokens late. We present WAVE, which introduces a ...
  </details>

- **2026-08-26** — Asmaa Eldesoukey, Md Zulfiqur Haider, Italo Napolitano et al. — [Schrödinger Bridges over Kinetic Swarming Models](http://arxiv.org/abs/2608.25281v1)
  <details><summary>📄 Abstract</summary>
  Paradigmatic interaction models explain how collective behaviors can emerge in complex systems from interactions among the constituent agents. In bio-inspired swarms, however, interactions alone may not suffice to bring the population to a desired aggregate configuration within a prescribed time horizon, as needed in applications ranging from targeted therapy to collective transport and emergency evacuation. In the present work, we consider finite-horizon minimum-energy collective steering for i...
  </details>

- **2026-08-26** — Huakang Lin, Tiancheng Zheng, Mingxuan Sun et al. — [Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips](http://arxiv.org/abs/2608.25276v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) architectures enable scalable and efficient large language models (LLMs) by selectively activating expert sub-networks through a routing mechanism. However, this adaptive design introduces a new attack surface: specific experts become disproportionately correlated with certain tokens (e.g., end-of-sequence), allowing adversaries to manipulate model behavior via lightweight perturbations. In this work, we present \textbf{Groundhog Bit-Flip Attack (GBFA)}, the first bit-fl...
  </details>

- **2026-08-25** — Ze Sheng, Aleksandar Kezic, Zhicheng Chen et al. — [FuzzingBrain-Bench V1: Evaluating Open-Ended Bug Discovery by LLMs](http://arxiv.org/abs/2608.25158v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the ability of large language models (LLMs) to discover software bugs is increasingly important. Existing benchmarks typically evaluate this capability by asking the model to generate a proof-of-concept input that triggers a predefined target vulnerability. However, this setup may overlook valid crashes discovered by the model when they do not match the predefined target. As a result, the evaluation may not reflect the model's real capability.   We present FuzzingBrain-Bench, a benchm...
  </details>

- **2026-08-25** — Muhammad Shaheer Bin Junaid — [Static Detection of Post-Quantum Cryptographic Algorithms in Stripped Binaries for Digital Forensic Examination and Migration Assurance](http://arxiv.org/abs/2608.25122v1)
  <details><summary>📄 Abstract</summary>
  Currently, there is no method to verify from compiled binary code whether a quantum-vulnerable algorithm has been replaced by an approved post-quantum algorithm. Cryptographic discovery tools identify algorithms by symbols, library dependencies, and runtime behaviour; however, all these signals are destroyed by stripping, statically linking, and optimising a binary. This paper presents Kestrel, a static analysis method for identifying the standardised lattice-based schemes ML-KEM and ML-DSA in s...
  </details>

- **2026-08-25** — Joshua Shterenberg, David Garfinkle, Anna I. Rosenzweig et al. — [Anti-Ultralocality and Plateau Models of Inflation](http://arxiv.org/abs/2608.24997v1)
  <details><summary>📄 Abstract</summary>
  Anti-ultralocality refers to the growth of spatial gradient terms relative to velocity terms in the coupled Einstein--scalar field equations. It is a characteristic feature of decelerated expansion before the onset of inflation. Previous numerical relativity studies have shown that anti-ultralocality prevents the onset of inflation in models with power-law inflaton potentials. In this paper, we show that models with plateau-shaped inflaton potentials, which are considered to be the simplest way ...
  </details>

- **2026-08-25** — Philipp E. Glass, Allan Tucker, Yongmin Li et al. — [Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal](http://arxiv.org/abs/2608.24988v1)
  <details><summary>📄 Abstract</summary>
  Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, pr...
  </details>

- **2026-08-25** — Seongwon Yoon, Pin-Jun Chen, Shimeng Yu — [Thermal Tuning Overhead in Wafer-Scale Optical Interconnects for LLM MoE Training: A Cross-Layer Analysis and Ferroelectric-Based Mitigation](http://arxiv.org/abs/2608.24637v2)
  <details><summary>📄 Abstract</summary>
  The rapid scaling of large language models (LLMs), particularly mixture-of-experts (MoE) architectures, has intensified interconnect demands because expert-parallel execution is communication-intensive. Wafer-scale optical interconnects based on dense wavelength-division multiplexing (DWDM) offer a promising path to higher bandwidth; however, conventional microring-resonator (MRR)-based links rely on thermo-optic tuning and are therefore vulnerable to workload-induced thermal fluctuations. In th...
  </details>

- **2026-08-25** — Xiaolong Sun, Qichao Wang, Hangyu Li et al. — [CVE-SAI: Counterfactual Visual Evidence-Guided Selective Attribute Indexing for Risk-Controlled E-commerce Search](http://arxiv.org/abs/2608.25023v1)
  <details><summary>📄 Abstract</summary>
  Multimodal product models can complete missing e-commerce attributes, yet current methods still optimize attribute-answer accuracy without verifying visual support, conflate transient prediction with persistent index admission, and lack explicit risk control over factually incorrect or visually unsupported values. We address these gaps with Counterfactual Visual Evidence-Guided Selective Attribute Indexing (CVE-SAI), which first infers and freezes an ontology-constrained candidate from the prima...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

- **2026-08-27** — Sven Hinderer, Jonathan Riese, Zheming Yin et al. — [Super-Resolution of Range-Doppler Maps: A Case Study with Chirp-Sequence Radar and Transformer](http://arxiv.org/abs/2608.27354v1)
  <details><summary>📄 Abstract</summary>
  Range-Doppler (rD) maps produced by chirp- sequence (CS) radar systems are fundamentally limited in reso- lution by bandwidth, carrier frequency, and coherent processing interval constraints. Improving resolution through hardware is often impractical due to regulatory, cost, and real-time operation requirements. In this work, we investigate deep learning-based super- resolution of rD maps in both range and Doppler using a real- world dataset collected with an Infineon millimeter-wave CS radar. W...
  </details>

- **2026-08-27** — Mesut Toruk — [BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click](http://arxiv.org/abs/2608.26867v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents reason, call tools, and act autonomously over many steps, but their agentic skills-correctly sequencing tools, planning under dependencies, judging untrusted inputs, and grounding generated arguments-are hard to measure with accuracy-only leaderboards. We present BekchiAI, which addresses both sides: a benchmark for measuring agentic skill and a platform for observing and controlling live agents. The BekchiAI-Benchmark, a suite of 13 tool-using ReAct agents across 7 t...
  </details>

- **2026-08-27** — Siye Wu, Kai Yang, Yuchen Cai et al. — [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](http://arxiv.org/abs/2608.27409v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them. We organize three fusion paradigms by the artefacts they reuse: Merge combines expert task vectors, Mix RL pools their datasets, and multi-teacher on-policy distillation (MOPD) uses both. Because they have largely been studied in isolation, how they compare and how to ...
  </details>

- **2026-08-27** — Jackie Baek — [LLMs Can Design Near-Optimal OR Algorithms](http://arxiv.org/abs/2608.27296v1)
  <details><summary>📄 Abstract</summary>
  We ask whether large language models (LLMs) can design effective algorithms for well-specified operations research (OR) problems. We study inventory control, queueing network control, and assortment optimization. We evaluate two levels of LLM use: at level 1, the model receives one problem instance and returns a solution for that instance; at level 2, it receives only the problem class description and broad parameter ranges, and returns an algorithm that maps instance parameters to solutions. Hu...
  </details>

- **2026-08-27** — Dezheng Han, Anbang Zhang, Zhihao Zhu et al. — [Unifying Detection and Adaptation in Task-Free Continual Learning](http://arxiv.org/abs/2608.27070v1)
  <details><summary>📄 Abstract</summary>
  To mitigate catastrophic forgetting in downstream continual learning (CL) for large language models (LLMs), existing methods typically constrain parameter updates or introduce task-specific adaptation modules. However, these methods often rely on explicit task boundaries during training, limiting their applicability to realistic task-free scenarios. In this paper, we propose a \textbf{Fi}sher-guided \textbf{uni}fied (\textbf{FiUni}) framework for batch-level task detection and parameter-efficien...
  </details>

- **2026-08-27** — Haihan Li, Haihao Li, Zhenfei Xu et al. — [Order Matters: A Chinese Multi-Panel Meme Benchmark for Vision-Language Reasoning](http://arxiv.org/abs/2608.26866v1)
  <details><summary>📄 Abstract</summary>
  Many multimodal tasks depend on how visual elements are ordered and composed, not only on recognizing them in isolation. Internet memes are a compact case of this problem: their punchline often depends on a constrained reading order and cross-panel visual--textual cues. While large vision-language models (LVLMs) show strong performance on single-image understanding, it remains unclear whether they can perform sequence-aware reasoning over structured meme layouts, especially in Chinese social med...
  </details>

- **2026-08-27** — Rongjin Li, Yuanxin Liu, Hao Zhou et al. — [Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper](http://arxiv.org/abs/2608.26596v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly capable scientific assistants, yet they remain far from fully autonomous research. This transition requires models to actively inspect academic papers, build global evidence views, and make traceable judgments without prespecified issues or evidence. However, existing work provides limited task paradigms or training studies for such issue- and evidence-absent verification. We study this challenge through scientific error detection, where ...
  </details>

- **2026-08-27** — Haoyu Wang, Chi Zhang, Mafu Zhang et al. — [Current-Limiting Control for Fault Ride-Through of LLC-based Solid-State Transformer in Data Centers](http://arxiv.org/abs/2608.26595v1)
  <details><summary>📄 Abstract</summary>
  Solid-State Transformers (SSTs) are increasingly proposed as the interface between distribution grids and data centers due to flexible power flows and fast dynamic response. However, when a short-circuit fault occurs in a load branch, the SST with a voltage-source-type DC-DC stage is forced to shut down due to fault currents. Therefore, current-limiting strategies are strongly needed to prevent catastrophic equipment damage and cascading blackouts by instantly restricting massive current spikes ...
  </details>

- **2026-08-27** — Hongru Song, Ruqing Zhang, Jiafeng Guo et al. — [DeepRepro: State-Aware Subplanning for Paper-to-Code Reproduction in Evolving Repositories](http://arxiv.org/abs/2608.26557v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic large language models (LLMs) have enabled increasingly autonomous software engineering workflows, yet automatic machine learning (ML) paper-to-code reproduction remains a challenging long-horizon problem. Unlike conventional code generation, this task requires constructing and maintaining a fully functional repository whose state continuously evolves during execution. Existing systems typically rely on static upfront planning followed by sequential file-level generatio...
  </details>

- **2026-08-27** — Kal Backman, Jared Wood, Adam Roff — [Learning Woody Clearing With Loss Alignment for Zero-Shot Regrowth and Woody Segmentation](http://arxiv.org/abs/2608.26489v1)
  <details><summary>📄 Abstract</summary>
  Detecting woody clearing is vital for managing biodiversity. Deep learning models can detect change in woody vegetation from bitemporal remote sensing imagery, however generated products may not meet end-user specifications due to unaligned loss definitions. Further limitations of deep learning models are the reliance on large datasets which can be difficult to attain for spatially rare and ambiguous events such as regrowth detection. In this work we train a model to detect woody change using bi...
  </details>

- **2026-08-27** — Orion Reblitz-Richardson — [How Language Models Organize and Structure Moral Knowledge](http://arxiv.org/abs/2608.27402v1)
  <details><summary>📄 Abstract</summary>
  How do large language models (LLMs) organize moral knowledge? Models detect moral content broadly, but detection is a low bar. We ask whether they go further, distinguishing moral foundations from one another and organizing the relationships between them geometrically.   We train six independent linear probes on open-weight language models, one per Moral Foundations Theory (MFT) category (care/harm, fair/cheat, lib/oppress, loy/betray, auth/subv, sanc/degrade), and examine how the resulting dire...
  </details>

- **2026-08-27** — Dylan Girrens, Guangjing Wang — [SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control](http://arxiv.org/abs/2608.27234v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate over untrusted webpages, documents, tools, and persistent states while exercising authority over security-sensitive resources. Existing defenses typically protect either planning or individual tool interactions, but persistent agents face a broader threat: attacker-controlled data can alter control flow, enter security-sensitive tool arguments, or compromise later queries. We present SPA, a plan-first architecture that secures planning, exec...
  </details>

- **2026-08-27** — Prachi Chaturvedi, Shahnawaz Ahmad, Ehsan Nowroozi et al. — [LAAF: A Layered Accountability Architecture Framework for LLM Applications](http://arxiv.org/abs/2608.27102v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) operate in hospitals, courtrooms, banks, and public service desks, where fluent, confident outputs are treated as authoritative even when ungrounded or incorrect. When such an output contributes to harm, who is answerable, and through what mechanisms can responsibility be traced, explained, and acted upon? Following PRISMA guidance, five databases were searched from January 2022 to March 2026 against four review questions; of 4,512 records identified, 122 primary stu...
  </details>

- **2026-08-27** — Yingjie Zhang, Yuanbo Xie, Kai Chen — [The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions](http://arxiv.org/abs/2608.27009v1)
  <details><summary>📄 Abstract</summary>
  Agent guardrails are checks that approve or refuse each action before an LLM executes it. Sometimes they refuse requests that are genuinely safe. This over-safety blocks deployment when a guardrail refuses an authorized task. Evaluating over-safety is hard: at the boundary an authorized action resembles an unauthorized one, and the safe-versus-unsafe label is a choice of authorization policy, not fixed by the action alone. We argue it therefore requires a benchmark that does not yet exist, one t...
  </details>

- **2026-08-27** — Tianjie Ju, Zheng Wu, Yueqing Sun et al. — [UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City](http://arxiv.org/abs/2608.27456v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can interpret a street view, but urban agency depends on whether such local evidence remains useful after the agent starts to move. In this paper, we investigate how far current MLLM agents can turn local urban perception into reliable action in a complicated real-scale city. We propose UrbanGround, the first sandbox to make this question testable in a physically constrained replica of Hong Kong built from territory-wide 3D geospatial data. UrbanGround su...
  </details>

- **2026-08-27** — Yisen Xi — [Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit](http://arxiv.org/abs/2608.27427v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely, while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply. We present Persona-Execution Separation (PES): persona and execution reside in different trust domains, connected by a governed contract bridge. The persona is singly-homed and may drift; execution is faceless and audited. Status summaries may return;...
  </details>

- **2026-08-27** — Yu Yvonne Wu, Arvind Pillai, Yuliang Chen et al. — [BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing](http://arxiv.org/abs/2608.27219v1)
  <details><summary>📄 Abstract</summary>
  Mental health assessment relies on episodic self-report scales, which convert subjective states such as stress into numerical scores but provide only sparse snapshots of wellbeing. Wearable devices offer longitudinal behavioral and physiological signals for continuous, low-burden monitoring. Recent LLM-driven personal-health agents enable natural language queries over wearable signals, but mainly handle short-term, retrieval-based lookups (e.g., highest step count over a week). They do not evalu...
  </details>

- **2026-08-27** — Miguel Requena Micó, Mario Fernandez-Tarraga, Daniel Díaz-López et al. — [From Security Events to Conflict States: A Three-layer Cyber Defense Scenario Model for Enhanced Cyber Situational Awareness](http://arxiv.org/abs/2608.27215v1)
  <details><summary>📄 Abstract</summary>
  Cyber defense in mission-critical environments requires integrated approaches capable of representing adversarial progression, defender-side uncertainty, mission impact, and defensive decision support within a unified framework. In operational domains, defenders must continuously estimate the evolving security posture while preserving the continuity and integrity of mission-critical functions under incomplete and noisy observations. This paper presents a mission-oriented cyber-defense framework ...
  </details>

- **2026-08-27** — Tommaso Bendinelli, Artur Dox, Christian Holz — [TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause Attribution](http://arxiv.org/abs/2608.27182v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly applied to anomaly detection and root-cause analysis in time-series observations collected from real-world systems; however, their performance on these tasks has not been systematically evaluated under controlled conditions. We introduce TraceBench, a simulation-based framework for generating controlled root-cause attribution tasks. In each generated task, an agent receives time-series observations produced by simulating a physical dynamical system and must determine ...
  </details>

- **2026-08-27** — Aneesh Rangnekar, Jorge Tapias Gomez, Joseph O Deasy et al. — [Parameter-Efficient pretrained-CT-to-MRI Transfer for Rectal Cancer Segmentation: Performance-Calibration Trade-offs](http://arxiv.org/abs/2608.27178v1)
  <details><summary>📄 Abstract</summary>
  Accurate rectal cancer segmentation from magnetic resonance imaging (MRI) is essential for adaptive radiotherapy and tumor response assessment, but deployment also requires computational efficiency and informative, calibrated uncertainty estimates. We therefore introduce SWIFT, a SWin pretrained model wIth parameter-eFficient and Tumor-aware fine-tuning for rectal cancer segmentation. A Swin V2 encoder pretrained on 10,444 public 3D CT volumes using a DINOv2-style objective was adapted to T2-wei...
  </details>

- **2026-08-27** — Xiang Wang, Zhijun Cheng, Zhenyu Meng — [Feature Transformation Enhanced Jacobi Polynomial Graph Filtering for Graph Anomaly Detection](http://arxiv.org/abs/2608.27144v1)
  <details><summary>📄 Abstract</summary>
  In recent years, graph anomaly detection (GAD) based on frequency-domain filtering have achieved promising results. However, existing approaches still face three major challenges: First, they use static basic function to constructed graph filter which cannot effectively adapt to the frequency-domain distribution of graph data. Second, they fail to adequately consider the importance information of each attribute in the node feature vector, leading to the loss of fine-grained information. Third, t...
  </details>

- **2026-08-27** — Jianwen Ma, Pengliang Leng, Lei Peng et al. — [Giant bulk photovoltaic effect driven by interfacial symmetry breaking in MoS2/Ta2NiSe5 heterostructures](http://arxiv.org/abs/2608.27064v1)
  <details><summary>📄 Abstract</summary>
  Van der Waals (vdW) heterostructures offer a versatile platform for engineering unconventional bulk photovoltaic (BPV) effect through interfacial symmetry breaking. However, the coexistence of multiple photophysical mechanisms, driven by structural complexity, spontaneous charge transfer, and strong interlayer coupling, often obscures the microscopic origin of the BPV response and hinders its rational optimization. Here, we demonstrate a pronounced BPV effect localized at the overlap region of a...
  </details>

- **2026-08-27** — Yassir Lairgi, Ludovic Moncla, Khalid Benabdeslem et al. — [C-Unseen: Weak Signal Detection in Dynamic Temporal Knowledge Graphs via LLM Reasoning](http://arxiv.org/abs/2608.26870v1)
  <details><summary>📄 Abstract</summary>
  Weak signals are early, low-visibility indicators that precede significant changes before those changes become established. Existing detection methods, based on keyword frequency, topic modeling, or untyped graph topology, fail to capture the semantic and relational structure through which such signals manifest. In this paper, we propose C-Unseen, a self-interpretable framework for weak signal detection in Dynamic Temporal Knowledge Graphs (DTKGs). We define a weak signal as a rare, semantically...
  </details>

- **2026-08-27** — Prateek Chhikara — [Evaluating Confidence-Gated Retrieval with Matched Trajectory Replay](http://arxiv.org/abs/2608.26846v1)
  <details><summary>📄 Abstract</summary>
  Interactive language-model agents use confidence signals to decide whether to answer immediately, retrieve additional evidence (from memory or external knowledge), or defer. Yet confidence is usually evaluated in isolation, without measuring the trajectory-level consequences of the actions it triggers. We propose matched trajectory replay, a controlled protocol for comparing confidence-to-action mappings. The protocol holds candidate answer states, evidence points, budgets, and action costs fixe...
  </details>

- **2026-08-27** — Federica Uccello, Simin Nadjm-Tehrani — [Are We Shooting Flies with Cannons? Trade-off Analysis for AI-based 5G Intrusion Detection](http://arxiv.org/abs/2608.26844v1)
  <details><summary>📄 Abstract</summary>
  The increasing adoption of Artificial Intelligence (AI) in network intrusion detection raises the question of whether complex and computationally expensive models are justified for this task. In this work, we investigate the trade-off between detection performance and computational cost for intrusion detection in 5G network telemetry. We compare traditional machine learning (ML) models, including XGBoost as a representative of tree ensemble, and TabNet for tabular deep neural network (DNN), with...
  </details>

- **2026-08-27** — David Soldani — [Claude Code Complete User Handbook](http://arxiv.org/abs/2608.26742v1)
  <details><summary>📄 Abstract</summary>
  Claude Code is an agentic work environment: a language model operating in a loop with filesystem access, shell execution, browser control, scheduled and cloud execution, external tool connections through the Model Context Protocol, and multi-agent orchestration. Its capability envelope now exceeds what one practitioner can supervise by attention alone, and its failure modes are systemic rather than local: an unreviewed hook, an over-scoped connector, a stale completion condition, an autonomous r...
  </details>

- **2026-08-26** — Mohnish Pai — [Ankhdjet: An Open-Source Compiler for Mask-Programmed Ternary Compute-in-ROM on an Open PDK](http://arxiv.org/abs/2608.26206v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model inference is dominated by weight movement: every generated token re-reads every weight. Ternary quantization (BitNet b1.58) shrinks each weight to 1.58 bits with reported parity at the 2B-parameter scale, small enough that hardwiring the weights into a read-only mask becomes plausible, and a commercial chip (Taalas HC1) has validated hardwired weights on an advanced node behind closed tooling. This paper asks whether model-specific silicon can be made reproducible with entir...
  </details>

- **2026-08-26** — Ilai Shraga, Roei Eshel, Lior Gorelik — [Approved Too Late: Verdict Staleness in LLM-Guarded Self-Adaptive Systems](http://arxiv.org/abs/2608.26306v1)
  <details><summary>📄 Abstract</summary>
  A large language model (LLM) guardrail for a self-adaptive system (SAS) may issue an approval that is correct at check time but stale by actuation. This creates an Execute-stage time-of-check to time-of-use (TOCTOU) hazard. We study verdict freshness: whether a guardrail verdict remains valid when used. We distinguish three quantities that answer different questions: all-candidate verdict change under fixed-action replay, oracle-labeled approval expiry on recorded closed-loop trajectories, and j...
  </details>

- **2026-08-26** — Alexander Prutsch, David Schinagl, Horst Possegger — [DESCENT: Directed Edge Scene Encoding for Airport Surface Movement Prediction](http://arxiv.org/abs/2608.26002v2)
  <details><summary>📄 Abstract</summary>
  Advanced automation is a key technology for enhancing the safety of ground operations amidst the increasing density of commercial air traffic. While motion forecasting is a well-studied task in autonomous driving, its application to airport surface movements remains underexplored. To enable efficient and accurate prediction in this domain, we propose DESCENT, a transformer-based architecture designed to handle heterogeneous dynamics and strict topological constraints. Our approach features a Pot...
  </details>

- **2026-08-26** — Shiqian Li, Chenguo Lin, Zhiguang Liu et al. — [4DStreamCtrl: Interactive Video Generation with Online 4D Control](http://arxiv.org/abs/2608.25479v2)
  <details><summary>📄 Abstract</summary>
  Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combi...
  </details>

- **2026-08-26** — Greg Kocher, Robert West, Clément Dumas et al. — [Diff Mining: Logit Differences Reveal Finetuning Objectives](http://arxiv.org/abs/2608.26462v1)
  <details><summary>📄 Abstract</summary>
  Finetuning has become the gold standard for refining existing behaviors and inducing new ones in language models, yet it often remains unclear exactly which behaviors emerge during this process. As models grow ever more capable, understanding finetuning better becomes increasingly important, particularly since unwanted behaviors may arise during finetuning. In this paper, we introduce Diff Mining, a simple yet effective framework for identifying what a finetuned model has learned by comparing it...
  </details>

- **2026-08-26** — Haitong Luo, Xuying Meng, Weiyao Zhang et al. — [Unveiling Spectral Mechanisms in Training-Free LLM Text Detection](http://arxiv.org/abs/2608.25944v2)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Large Language Models (LLMs) makes it increasingly difficult to distinguish human writing from machine-generated text. Training-free detection offers a scalable solution, yet common confidence-based metrics mainly measure average token probabilities and often miss the signal fluctuations that characterize human writing, which we call "generative vitality". Spectral analysis offers a way to capture this vitality, but its mechanism and practical boundaries remain underexpl...
  </details>

- **2026-08-26** — Yilong Chen, Xiao Qin, Chenghao Liu et al. — [LLM Agents for Time-Series: A Survey](http://arxiv.org/abs/2608.26226v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly being developed for time-series problems, but their design choices vary substantially across task settings. This survey adopts a problem-driven taxonomy that organizes these systems by the time-series problems they address rather than by isolated technical components. We group existing systems into four categories: forecasting and reasoning, augmentation and synthesis, anomaly detection and diagnosis, and decision support. Within each category, we examine how ta...
  </details>

- **2026-08-26** — XiuYu Zhang, Bonan Ruan, Junfeng Fang et al. — [LMSM: LLM Security Framework Inspired by Linux Security Modules](http://arxiv.org/abs/2608.25697v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals are not security controls by themselves. Deployments that adapt them for safety typically couple each signal to its own calibration, policy logic, and intervention code, so each new artifact creates integration work instead of strengthening a ...
  </details>

- **2026-08-26** — Roee M. Francos, Daniel Garces, Orhan Eren Akgün et al. — [Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems](http://arxiv.org/abs/2608.25690v1)
  <details><summary>📄 Abstract</summary>
  Sequential decision-making in multi-robot systems typically assumes that planning information is reliable and that agents execute the actions anticipated by the planner. Compromised agents can violate both assumptions, creating a mismatch between the planning model and physical execution. We study this problem in online multi-robot routing under localization spoofing. We introduce a distance-constrained spoofing model for monitor-aware adversaries, together with a tiered bipartite matching strat...
  </details>

- **2026-08-26** — Alexander Prutsch, David Schinagl, Horst Possegger — [DESCENT: Directed Edge Scene Encoding for Airport Surface Movement Prediction](http://arxiv.org/abs/2608.26002v1)
  <details><summary>📄 Abstract</summary>
  Advanced automation is a key technology for enhancing the safety of ground operations amidst the increasing density of commercial air traffic. While motion forecasting is a well-studied task in autonomous driving, its application to airport surface movements remains underexplored. To enable efficient and accurate prediction in this domain, we propose DESCENT, a transformer-based architecture designed to handle heterogeneous dynamics and strict topological constraints. Our approach features a Pot...
  </details>

- **2026-08-26** — Yuzhuo Cui, Zongye Zhang, Qingjie Liu — [LivingRAG: Augmenting Graph RAG with Experience](http://arxiv.org/abs/2608.25960v1)
  <details><summary>📄 Abstract</summary>
  Graph-based RAG improves multi-hop question answering by organizing evidence as a knowledge graph. However, most existing RAG systems process each query in isolation and discard useful reasoning from the LLM's response after inference. As a result, later related queries need to retrieve evidence and reason from scratch. We propose LivingRAG, a Graph RAG framework with writable and reusable reasoning experience. LivingRAG adds a writable experience store to a graph-based retrieval backbone, enabl...
  </details>

- **2026-08-26** — Hongqiu Ni, Han Tian, Chi Zhang et al. — [TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving](http://arxiv.org/abs/2608.25523v1)
  <details><summary>📄 Abstract</summary>
  Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests. In multi-stage workflows, existing schedulers tend to prioritize either immediate prefix locality or overall workflow progress. However, under a shared KV cache budget, optimizing either objective in isolation can prolong tasklevel job...
  </details>

- **2026-08-26** — Shiqian Li, Chenguo Lin, Zhiguang Liu et al. — [4DStreamCtrl: Interactive Video Generation with Online 4D Control](http://arxiv.org/abs/2608.25479v1)
  <details><summary>📄 Abstract</summary>
  Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combi...
  </details>

- **2026-08-26** — Princy Ranaivomanana, Murat Uzundag — [Exploring Late Stellar Evolution in the Era of Large Surveys: Machine Learning Prospects for Hot Subdwarfs and White Dwarfs](http://arxiv.org/abs/2608.25957v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of large-scale astronomical surveys and advances in data-driven analysis techniques have transformed the study of late-stage stellar evolution. Modern facilities are producing large volumes of photometric, spectroscopic, and astrometric data, enabling systematic investigations of compact stellar populations across the Milky Way. Among the most important tracers of these advanced evolutionary phases are hot subdwarfs and white dwarfs: hot subdwarfs are core-helium-burning tracers...
  </details>

- **2026-08-26** — Haitong Luo, Xuying Meng, Weiyao Zhang et al. — [Unveiling Spectral Mechanisms in Training-Free LLM Text Detection](http://arxiv.org/abs/2608.25944v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Large Language Models (LLMs) makes it increasingly difficult to distinguish human writing from machine-generated text. Training-free detection offers a scalable solution, yet common confidence-based metrics mainly measure average token probabilities and often miss the signal fluctuations that characterize human writing, which we call "generative vitality". Spectral analysis offers a way to capture this vitality, but its mechanism and practical boundaries remain underexpl...
  </details>

- **2026-08-26** — Yoann Launay, Parameswaran Kamalaruban, Tom Kempton et al. — [Fairness-Aware Test-Time Prompt Tuning](http://arxiv.org/abs/2608.25707v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models have displayed remarkable capabilities in multi-modal understanding and are increasingly used in critical applications where economic and practical deployment constraints prohibit re-training or fine-tuning. However, these models can also exhibit systematic biases that disproportionately affect protected demographic groups and existing approaches to addressing these biases require extensive model retraining and access to demographic attributes. There is a clear need to dev...
  </details>

- **2026-08-26** — Nayoung Kim, Mickey Mancenido, Huan Liu — [Adaptive Triggering for Bias Correction in LLM Reasoning](http://arxiv.org/abs/2608.25379v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought prompting can expose and amplify demographic stereotypes within an LLM's intermediate reasoning and create a failure mode that final-answer debiasing alone cannot address. Mitigating such bias during generation presents a fundamental timing problem: intervening too late allows biased reasoning to propagate, while unnecessarily intervening can disrupt otherwise correct reasoning. Existing approaches largely avoid this decision by either evaluating completed reasoning chains post ...
  </details>

- **2026-08-25** — Wonung Kim, Hyunmin Choi, Minsu Kim et al. — [Simthesizer: An Agent-Driven Simulation Framework for LLM Serving Systems](http://arxiv.org/abs/2608.24650v2)
  <details><summary>📄 Abstract</summary>
  System-level simulation is an essential tool for exploring the rapidly expanding design space of LLM serving systems, where real deployments remain costly and often infeasible. However, modern LLM serving now evolves faster than human-driven simulator development can track, and emerging workloads and mechanisms, from agentic workflows to disaggregated serving, no longer fit the monolithic simulation pipeline that existing simulators assume. Each new mechanism therefore demands an invasive rewrit...
  </details>

- **2026-08-25** — Jiajun Fan, Jingyuan Li, Prashanth Gurunath Shivakumar et al. — [Can We Read the Mind of an Audio LLM? A Verbalizable, Multilingual Middle-Layer Workspace](http://arxiv.org/abs/2608.24958v1)
  <details><summary>📄 Abstract</summary>
  An audio language model is a black box in a specific way: we see what it says, never what it works out on the way there, and chain-of-thought monitoring helps only if the model writes its reasoning down. Reading a base Qwen3-Omni with a logit lens at the audio-token positions, we find that the answer to a spoken question becomes legible - in words - in the model's middle layers, before it emits any token. Five findings follow. (1) The readout carries concepts in neither the question, the options...
  </details>

- **2026-08-25** — Pardis Ranjbar-Noiey, Natalie Parde — [Behind the [MASK]: Disentangling Representation and Faithfulness in DAPF-Based Dementia Detection](http://arxiv.org/abs/2608.25028v1)
  <details><summary>📄 Abstract</summary>
  Spoken-language analysis via prompt-based domain-adaptive models is a promising direction for low-resource, non-invasive dementia screening, but such models remain internally opaque. We study the interpretability of the Domain-Adapted models via Prompt-based Fine-tuning (DAPF) framework, which casts dementia detection as diagnosis-related masked-token prediction. We interpret DAPF and strong baselines using a variety of probing and analysis techniques, finding that DAPF achieved the best overall...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 58 papers

- **2026-08-27** — Gauthier Miralles, Loic Le Folgoc, Vincent Jugnon et al. — [Unsupervised Adaptation of 3D CT Foundation Models for 3D CBCT Segmentation](http://arxiv.org/abs/2608.27190v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D segmentation of cone-beam CT (CBCT) is critical for interventional and radiation therapy applications, yet it remains limited by two compounding challenges: the scarcity of annotated CBCT data and the large domain shift from diagnostic CT. Interventional CBCT exhibits fundamental modality differences from conventional CT, driven by acquisition and physics effects as well as contrast-specific vascular content, thereby limiting effective cross-modality model transfer. We propose a nove...
  </details>

- **2026-08-27** — Yichen Dong, Hao Wang, Junhui Li et al. — [STAR : Sentence Translation Alignment Rate for Document-to-Document Machine Translation](http://arxiv.org/abs/2608.27161v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have enabled a shift from sentence-level to document-to-document (Doc2Doc) machine translation, promising improved global coherence. However, document-to-document generation in a single pass frequently suffers from structural misalignment, manifesting as sentence omissions or hallucinations that violate the core requirement of source-target correspondence. To address this, we introduce Sentence Translation Alignment Rate (STAR), an auxiliary metric that explicitly qu...
  </details>

- **2026-08-27** — Jingyi Zheng, Yule Liu, Zifan Peng et al. — [TransMeme: A Multi-Agent Framework for Cross-Cultural Meme Transcreation](http://arxiv.org/abs/2608.27127v1)
  <details><summary>📄 Abstract</summary>
  Internet memes are a pervasive form of multimodal online communication; however, such communication often involves users from diverse linguistic and cultural backgrounds. Therefore, adapting memes across cultures and languages is a central challenge for enabling mutual understanding in online communication. Unlike ordinary translation or standalone text rewriting, cross-cultural meme transcreation must jointly preserve communicative intent, adapt culture-dependent meaning for the target audience...
  </details>

- **2026-08-27** — Hengyuan Xu, Wei Cheng, Yumeng Ji et al. — [Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning](http://arxiv.org/abs/2608.26993v1)
  <details><summary>📄 Abstract</summary>
  Explicit visual intermediates can help multimodal large language models (MLLMs) externalize spatial evidence and updated visual states, but their utility depends on whether an image editor can faithfully realize the required transformation. We introduce \textbf{Aphanta}, an automated task-discovery and closed-loop diagnostic framework for the MLLM -> image editor -> MLLM pipeline. Aphanta evaluates three conditions---direct reasoning, reasoning with an editor-generated intermediate, and reasonin...
  </details>

- **2026-08-27** — Shiyi Zhang, Mushui Liu, Yunze Tong et al. — [Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher](http://arxiv.org/abs/2608.26872v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD), which leverages a pre-trained, specialized teacher model to provide dense supervisory signals, has achieved significant success in Large Language Models (LLMs) and has recently been adapted to flow matching models. However, this paradigm suffers from two major issues: First, training a separate, task-specific teacher for every new objective incurs high computational costs. Second, the discrepancy between teacher and student distributions often leads to compounding e...
  </details>

- **2026-08-27** — Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen et al. — [CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](http://arxiv.org/abs/2608.26868v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in SLAM have leveraged 3DGS for photorealistic reconstruction and novel view synthesis. However, most methods rely on RGB-D input, which is unavailable on consumer-grade smartphones, and few integrate 3DGS within a collaborative framework. Therefore, we present CGS-SLAM, a hybrid decentralized/centralized system enabling multi-agent 3DGS SLAM using only RGB and inertial data. Each agent performs local tracking with inertial data as a motion prior and reconstructs a scaled map usi...
  </details>

- **2026-08-27** — Haowen Gu, Gensheng Pei, Zeren Sun et al. — [MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA](http://arxiv.org/abs/2608.26848v1)
  <details><summary>📄 Abstract</summary>
  Medical Visual Question Answering (Med-VQA) holds significant promise for clinical decision support, yet faces challenges due to limited annotated data and the high computational demands of existing large vision-language models. We propose MedFG-VQA, a lightweight framework that leverages a memory bank to augment DCT-based low-frequency features and employs graph-enhanced cross-attention for effective visual-textual alignment. Specifically, our approach features two key components: Frequency-Mem...
  </details>

- **2026-08-27** — Muyao Yuan, Muyan Jiao, Jiangyong Ying et al. — [LLaVAFlow: Preserving Latent Alignment Flow for Parameter-Efficient Multimodal Fine-Tuning](http://arxiv.org/abs/2608.26820v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) exhibit strong generalization, visual instruction tuning for downstream tasks inevitably causes catastrophic forgetting, impairing overall generalization. While existing methods regulate weight updates to reduce forgetting, they overlook the fundamental cross-modal alignment in MLLMs. Based on prior work and our observations, we argue that cross-modal alignment is implicitly captured in the information-compression trajectory. To preserve the alignme...
  </details>

- **2026-08-27** — Seohyeong Lee, Hwaran Lee, Buru Chang — [Instruction Quality Matters: Refining Instructions for Effective Preference Learning](http://arxiv.org/abs/2608.26779v1)
  <details><summary>📄 Abstract</summary>
  Preference learning optimizes models using response pairs, yet the informativeness of these pairs is fundamentally shaped by the instructions from which they are generated. We identify instruction quality as a hidden bottleneck in preference learning: low-quality or ambiguous instructions restrict the response-quality distribution, limiting strong chosen responses and weakening preference signals. Through Best- and Worst-of-N analyses, we show that instruction quality constrains both the ceiling...
  </details>

- **2026-08-27** — Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian et al. — [AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling](http://arxiv.org/abs/2608.26623v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation. The benchmark comprises 3,808 instances spanning six DAG topologies and three difficulty tiers, eval...
  </details>

- **2026-08-27** — Saksham Khatwani, He Cheng, Majid Afshar et al. — [Surgical Alignment in Knowledge Graph Training for Clinical Diagnosis with Large Language Models](http://arxiv.org/abs/2608.26587v1)
  <details><summary>📄 Abstract</summary>
  Biomedical knowledge graphs (KGs) offer structured medical knowledge that can ground large language model (LLM) reasoning in clinical diagnosis application, yet how KG signal should be integrated into LLMs remains an open question. We present a systematic study spanning five KG task formulations, three training paradigms, two KGs, and three base LLMs. At the task level, all paradigms improve over the non-finetuned baseline, but methods with comparable in-domain accuracy show substantially differ...
  </details>

- **2026-08-27** — Haizhao Fan, Xinyi Le — [SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting](http://arxiv.org/abs/2608.26829v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting models operate on raw numerical sequences, lacking the semantic knowledge that domain experts implicitly leverage, such as the physical meaning of each variable, its statistical behavior, and its temporal dynamics. Recent efforts to bridge this gap fall into two camps. Some rely on large language models at inference time, which is computationally expensive. Others apply uniform textual prompts at the dataset level, ignoring the heterogeneous semantics across individual va...
  </details>

- **2026-08-27** — Ej Zhou, Suchir Salhan, Catherine Arnett et al. — [Cross-Lingual Alignment Without Joint Training: Do Monolingual Language Models Converge on Universal Representations?](http://arxiv.org/abs/2608.27115v1)
  <details><summary>📄 Abstract</summary>
  Cross-lingual alignment in multilingual language models is typically attributed to joint training: shared parameters, mixed-language batches, or explicit alignment objectives. We ask whether monolingual models trained on non-parallel data learn alignable representations without joint training. By testing on strictly monolingual language models, such as the Goldfish model families and independently developed models from different research labs, we find three results. Correlation: these models dev...
  </details>

- **2026-08-27** — Zibo Zhou, Zongsen Qiu, Rui Chen et al. — [Cross-Architecture Knowledge Distillation from a Vision Foundation Model to a Lightweight Visual State Space Model for Tea Leaf Disease Classification](http://arxiv.org/abs/2608.26771v1)
  <details><summary>📄 Abstract</summary>
  Automated tea leaf disease classification supports precision agriculture, yet deploying accurate models on edge devices remains challenging under tight compute budgets. Self-supervised vision foundation models such as DINOv2 provide strong features but are too large for field deployment, while lightweight models trained from scratch on small agricultural datasets often underfit. We study cross-architecture knowledge distillation (KD) from a fine-tuned DINOv2 teacher (Vision Transformer) to a com...
  </details>

- **2026-08-27** — Yiyang Huang, Zhaowen Wang, Simon Jenni et al. — [Beyond Atomic Layouts: Compositional Design Understanding with Vision-Language Models](http://arxiv.org/abs/2608.26716v1)
  <details><summary>📄 Abstract</summary>
  Layout understanding, or the interpretation of element organization, is essential for document analysis, user interface (UI) creation, and graphic design. While recent vision-language models (VLMs) excel at interpreting atomic layouts composed of independent elements, they struggle with compositional layouts that require reasoning over visually entangled elements within hierarchical multi-layer structures. In this paper, we introduce a new task, compositional layout understanding, and present Co...
  </details>

- **2026-08-27** — Jiten Oswal, John Cadeddu — [Five Primitives for Governing Autonomous AI Agents at Runtime](http://arxiv.org/abs/2608.26696v1)
  <details><summary>📄 Abstract</summary>
  Enterprise deployments of autonomous AI agents inherit a control model built for human users and long-lived services, and the fit fails in three specific ways: agent principals are ephemeral, appearing and vanishing faster than provisioning; their actions are selected by a model rather than programmed, so the set of things they may attempt is not known in advance; and the population is discovered rather than provisioned, because anyone who can call an API can create one. We argue that governing ...
  </details>

- **2026-08-27** — Anjishnu Mukherjee, Ziwei Zhu, Antonios Anastasopoulos — [Double Trouble: Bilingual Pretraining Leaves Language-Conditioned Effects in Shared-Language Representations](http://arxiv.org/abs/2608.26576v1)
  <details><summary>📄 Abstract</summary>
  When researchers compare multilingual models for probing, interpretability, or cross-lingual transfer, they often align embedding spaces and assume that shared-language representations are comparable. We show that this assumption can be premature for decoder-only models. We pretrain paired 310M-parameter models (one English-only, one bilingual) across eight typologically diverse languages, separately controlling for English exposure, total compute, and document overlap. After aligning on shared ...
  </details>

- **2026-08-26** — Ziyu Wang, Qiming Dai, Yishan Wu et al. — [FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence](http://arxiv.org/abs/2608.26310v1)
  <details><summary>📄 Abstract</summary>
  Large language models can now generate complex, multi-step mathematical proofs, but reliably determining their correctness and localizing early logical errors remains a critical challenge. Existing evaluation approaches largely depend on model-based natural-language judgments, which often overlook local reasoning gaps. While formal theorem provers like Lean offer a path to rigorous verification, using them to evaluate informal text requires solving locality and semantic mismatches: a prover migh...
  </details>

- **2026-08-26** — Yi Chen, Hanna Hsieh, Shuhong Liu et al. — [Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness](http://arxiv.org/abs/2608.25429v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning aims to make a model forget specific data, yet unlearned LLMs often fail to stay unlearned: brief fine-tuning can revive removed knowledge. Existing robustness predictors rely on global weight-space displacement, but distance alone can be misleading when random or destructive updates collapse performance. We argue that relearning robustness depends on update structure: robust unlearning should affect forget-critical weights while sparing retain-critical ones. We introduce the ...
  </details>

- **2026-08-26** — Yiping Wang, Jie Li, Jingyu Shen et al. — [THA-Flow Generative Model: Prosthesis Geometry Prediction from Preoperative CT](http://arxiv.org/abs/2608.25845v1)
  <details><summary>📄 Abstract</summary>
  Preoperative planning for total hip arthroplasty (THA) is commonly framed as selecting a single prosthesis configuration and placement for a patient's osseous anatomy. In practice, however, the same anatomy may admit several clinically reasonable solutions, making planning inherently a one-to-many problem that is better represented by a conditional probability distribution. We present THA-Flow, a conditional flow-matching model that generates three-dimensional prosthesis geometry directly from p...
  </details>

- **2026-08-26** — Xinyu Li, Yi Zhou, Guanqun Cao et al. — [Localize-Then-Decide Guarantees for LLM Judgments](http://arxiv.org/abs/2608.25824v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as evaluators to assess output quality and preference alignment, yet providing reliable guarantees of agreement with human judgments remains challenging. Recent work introduces confidence-thresholding methods that provide such guarantees for pairwise comparisons, relying on the assumption that higher estimated confidence implies lower disagreement risk with humans. However, this assumption can break down when the number of candidate responses in...
  </details>

- **2026-08-26** — Fumiaki Kimino, Ryoma Sato — [Why Does Graph Learning Fail to Fully Benefit from a Text Teacher?](http://arxiv.org/abs/2608.25741v1)
  <details><summary>📄 Abstract</summary>
  Graph neural networks (GNNs) are widely used to represent complex interactions and relationships among entities. We investigate a multimodal model that combines two complementary ideas: a self-supervised method that enables a GNN encoder pretrained on one dataset to operate directly on another dataset with a different node-feature dimensionality, without rebuilding the model or realigning the data; and an alternating optimization method that updates a language-model module in an E-step and a GNN...
  </details>

- **2026-08-26** — Yiwen Liang, Hui Chen, Yizhe Xiong et al. — [Towards Purified Multi-Label Test-Time Adaptation of Vision-Language Models](http://arxiv.org/abs/2608.25653v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) has been widely explored in single-label recognition, effectively mitigating distribution shifts, especially when combined with vision-language models. However, real-world images often contain multiple objects, while the more practical multi-label test-time adaptation (MLTTA) has received little attention so far. Recent cache-based TTA methods have shown promising efficiency and effectiveness, yet directly extending them to multi-label scenarios suffers from a one-to-m...
  </details>

- **2026-08-26** — Daniel Panangian, Ksenia Bittner — [Diffusion Transformers for Roof Graph Synthesis and Reconstruction](http://arxiv.org/abs/2608.25652v1)
  <details><summary>📄 Abstract</summary>
  We present RoofDiT, a generative framework for 2D roof graph synthesis and reconstruction. Roofs are compactly described as planar graphs of junctions and structural edges, but existing methods often rely on fixed geometric rules or direct reconstruction objectives. RoofDiT instead models roof structures directly as vertex-edge graphs and learns a conditional generative prior over their geometry and connectivity. Our framework follows a two-stage design: a diffusion transformer generates roof ve...
  </details>

- **2026-08-26** — Xixian Yong, Siyuan Chang, Yingying Zhang et al. — [Controllable Affective Generation via Latent Vector Steering](http://arxiv.org/abs/2608.25569v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) often produce emotionally flattened responses after alignment, limiting their effectiveness in affect-sensitive applications. In this paper, we propose EmoVec, a lightweight framework for controllable affective generation via latent vector steering. EmoVec extracts emotion-specific directions from paired neutral and emotion-conditioned responses using contrastive activation addition, and further refines them through task-specific debiasing and principal subspace remo...
  </details>

- **2026-08-26** — Eunjee Choi, JungHoon Sung, Seongwhan Cho et al. — [SMART: MLLM-guided Temporal Alignment for Unifying Sign Language Recognition and Spotting](http://arxiv.org/abs/2608.25493v1)
  <details><summary>📄 Abstract</summary>
  Continuous sign language recognition (CSLR) aims to recognize gloss sequences from unsegmented sign videos under weak sequence-level supervision. However, existing methods rely on sentence-level gloss annotations, providing limited temporal and semantic guidance for fine-grained representation learning. Conventional video-text alignment also requires large batch sizes, making it inefficient for memory-intensive sign language video training. In this work, we propose SMART, an MLLM-guided temporal...
  </details>

- **2026-08-26** — Simone Garbin, Leonardo Venturoso, Marco Todescato — [Automatic weld seam segmentation for industrial quality control: a comparison of RGB and polarimetric imaging with CNN and transformer architectures](http://arxiv.org/abs/2608.25465v1)
  <details><summary>📄 Abstract</summary>
  Visual inspection of welded assemblies remains one of the least automated stages in many industrial production processes, still depending largely on the experience of human operators and thus subject to inter-operator variability; the manufacturing of special-purpose machinery cabins, the setting of this study, is one representative case. This work evaluates the feasibility of automatic weld seam segmentation from RGB and polarimetric imagery, comparing controlled laboratory acquisitions with im...
  </details>

- **2026-08-26** — Longteng Jiang, DanDan Zheng, Qianqian Qiao et al. — [VGA-BenchV2: An Expanded Unified Benchmark and Multi-Model Framework for Evaluating Video Aesthetics and Generation Quality](http://arxiv.org/abs/2608.25452v1)
  <details><summary>📄 Abstract</summary>
  We introduce VGA-BenchV2, an extended human-aligned benchmark and optimization framework for jointly evaluating and improving video generation quality and aesthetic value. Built upon VGA-Bench, VGA-BenchV2 preserves the original fine-grained taxonomy with two primary dimensions-Aesthetic and Generation-and 52 sub-dimensions. Guided by this taxonomy, we curate 1,016 diverse prompts and collect over 60,000 videos generated by 12 mainstream video generation models. More importantly, VGA-BenchV2 sub...
  </details>

- **2026-08-26** — Jiwoong Im, Minwoo Kim, Jaeho Lee et al. — [Token-Oriented Semantic Communication with Pretrained Vision Transformers](http://arxiv.org/abs/2608.25410v1)
  <details><summary>📄 Abstract</summary>
  Token communications realize the semantic communication principle at the granularity of transformer tokens, providing a promising direction for client--server collaborative inference in resource-constrained edge systems. However, directly transmitting token embeddings presents two practical challenges: substantial communication cost and limited interoperability across model-specific token embedding spaces. To address these challenges, we propose a \emph{token-oriented} semantic communication fra...
  </details>

- **2026-08-26** — Yurui Shi, Yuchen Miao, Ximing Hu et al. — [MOTIF: Motivation-guided Topology Inference for Cold-start Multimodal Recommendation](http://arxiv.org/abs/2608.25381v1)
  <details><summary>📄 Abstract</summary>
  Cold-start multimodal recommendation faces three coupled challenges: (i) sparse interactions obscure user intent, (ii) cold items remain topologically isolated, and (iii) similarity-based item graphs may cause semantic drift. To address these issues, we propose MOTIF, a Motivation-guided Topology Inference framework for cold-start multimodal recommendation. MOTIF integrates Semantic Motivation Reasoning, Knowledge-enhanced Graph Reconstruction, Weighted Graph Contrastive Learning, and Semantic-S...
  </details>

- **2026-08-26** — Armel Koulong — [Scalable Tube-Tightened Multi-Agent Safety via Certified Constraint Reduction](http://arxiv.org/abs/2608.25323v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a certified constraint-reduction method for distributed model predictive control with tube-tightened exponential control barrier functions (eCBFs) in multi-agent systems. At each prediction stage, pairwise agent--agent and agent--obstacle eCBF conditions define halfspaces in the local control space. Rather than enforcing all such halfspaces, a geometry-adaptive subset is retained and a Farkas certificate verifies that the reduced admissible set is contained in the full tighte...
  </details>

- **2026-08-26** — Srivalli Katkuri, Maxwell Kawada, Juan Wachs — [Beyond Pairwise Feedback: Listwise Vision-Language Supervision for Preference-Based Reward Learning](http://arxiv.org/abs/2608.25350v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have emerged as a powerful source of supervision for reinforcement learning, enabling agents to leverage rich semantic knowledge during training. Inspired by the success of preference-based reward learning (PbRL) in reinforcement learning from human feedback (RLHF), vision-language model generated image-based preferences provide an effective source for learning reward functions. This can be done by visually comparing two outcomes through the Bradley-Terry (BT) model...
  </details>

- **2026-08-25** — Dongyue Li, Ziniu Zhang, Lu Wang et al. — [Learning Mixtures of Plackett-Luce Models for Multi-Objective Alignment](http://arxiv.org/abs/2608.25200v1)
  <details><summary>📄 Abstract</summary>
  We consider the problem of learning a mixture of $k$ Plackett-Luce models given multi-way ranking responses from annotators that may represent heterogeneous underlying preferences. This problem has many applications in AI alignment and preference optimization. Prior work has studied mixtures of Bradley-Terry models from pairwise comparisons. However, uncovering mixture models is theoretically unidentifiable when $k$ exceeds $m/2$, where $m$ is the length of a ranking. We propose an efficient imp...
  </details>

- **2026-08-25** — Lkhanaajav Mijiddorj, Yang Yan, Tyler Beringer et al. — [Lightweight Machine Learning-Driven Monocular Sidewalk Path Extraction for Embedded Micromobility Navigation](http://arxiv.org/abs/2608.25178v1)
  <details><summary>📄 Abstract</summary>
  Sidewalk-scale path extraction demands perception and planning that run reliably on compact, low-power hardware in cluttered, map-sparse environments. We present a monocular vision pipeline for sidewalk path extraction in micromobility systems that progresses through three design iterations, from a skeleton-graph baseline through distance-transform corridor planning to a lightweight image-space architecture, and provides a systematic comparison of five path-planning methods across both bird's-ey...
  </details>

- **2026-08-25** — Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib et al. — [RefLAM: A Reference-Grounded Line Annotation Pipeline for Historical Arabic Manuscripts](http://arxiv.org/abs/2608.25140v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to building line-level Arabic handwritten-text-recognition (HTR) training data either rely on fully manual annotation, which does not scale, or on automatic OCR-to-reference alignment methods not yet extended to multi-script, two-zone (main-plus-margin) manuscript layouts with a provable correctness guarantee. We present RefLAM (Reference-grounded Line Annotation for Manuscripts), a pipeline converting manuscript page images and clean transcriptions into validated, line-level...
  </details>

- **2026-08-25** — Augusto Camargo — [The Invisible Editorial Layer: Formalizing Undisclosed Inference-Time Steering, Probability Placement, and the Attribution Problem in Deployed Language Models](http://arxiv.org/abs/2608.24662v2)
  <details><summary>📄 Abstract</summary>
  Evaluations of generative language models frequently interpret observable behavioral traits, such as political stance, brand inclination, and normative framing, as manifestations of model weights, post-training alignment, or prompting. This interpretation risks conflating a foundation model with the multi-layered production system through which its outputs are ultimately served. Modern inference stacks support runtime interventions capable of modifying generation while model parameters remain fr...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 75 papers

- **2026-08-27** — Zihan Ding, Liyu Zhang, Xiaomin Ouyang — [HALO: A Heterogeneity-Aware Language-Aligned IMU Foundation Model for Open-Set Human Activity Recognition](http://arxiv.org/abs/2608.27233v1)
  <details><summary>📄 Abstract</summary>
  Human Activity Recognition (HAR) using inertial measurement units (IMUs) enables a wide range of applications, yet the field still lacks a unified model that can generalize across diverse subjects, devices, and activities. Training such a model is difficult due to two key challenges: sensing heterogeneity -- differences in sampling rates, channel configurations, and sensor placements -- and poor generalization to unseen activities and label vocabularies. We introduce HALO (Heterogeneity-Aware La...
  </details>

- **2026-08-27** — Samuel Schmidgall, Xiaokai Zhu, Marian Shaw et al. — [Accelerating Scientific Research with Gemini in the Real-World](http://arxiv.org/abs/2608.26701v1)
  <details><summary>📄 Abstract</summary>
  We present an extension and comprehensive real-world validation of Co-Scientist, a Gemini-based multi-agent system designed to accelerate end-to-end scientific research across hypothesis generation, experimentation, and manuscript generation. Moving beyond in silico hypothesis generation, this specialized configuration transitions Co-Scientist into an execution-grounded research partner advancing closed-loop scientific workflows across materials science, biology, and computer science. In materia...
  </details>

- **2026-08-27** — Jinning Cui, Lu Chen, Haoyan Shi et al. — [Chart2SVG: Editable SVG Generation from Raster Chart Images](http://arxiv.org/abs/2608.26544v1)
  <details><summary>📄 Abstract</summary>
  We present Chart2SVG, a multimodal large language model that converts static raster charts into structurally organized, semantically enriched SVGs that support programmatic editing. By incorporating chart-specific semantic tokens into a vision-language model, Chart2SVG captures both geometric primitives and their functional roles. To support robust structural recovery, we introduce Beagle+, a dataset of 33K canonicalized and structurally distilled chart samples. Our approach combines specialized...
  </details>

- **2026-08-27** — Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong et al. — [Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation](http://arxiv.org/abs/2608.27429v1)
  <details><summary>📄 Abstract</summary>
  Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.   We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), which instead models reactions as discrete flow matching over electron occupation vectors.   Concrete...
  </details>

- **2026-08-27** — Xiaoxiao Lu, Yunlong Dong, Jiahao Shi et al. — [Making Latent Evolution Explicit: Operator-Structured Transitions for World Action Models](http://arxiv.org/abs/2608.27259v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) augment robot policies by predicting how task-relevant scene states may evolve under interaction. Recent WAMs increasingly perform such prediction in latent representation spaces, avoiding full appearance-level generation while preserving control-relevant information. Yet latent transitions are commonly realized with Transformer-based predictors whose inductive structure is centered on token interaction rather than temporal evolution. We study transition realization as...
  </details>

- **2026-08-27** — Ahmad Jad Allah, Kazi F. Akhter, Md. Kamrozzaman Bhuiyan et al. — [Importance Scoring of Transformer Attention Heads in Learning Tabular Data](http://arxiv.org/abs/2608.27241v1)
  <details><summary>📄 Abstract</summary>
  Computationally demanding and opaque deep learning models can be better understood and optimized by analyzing how they transform data. While deep transformers have been widely studied in computer vision and natural language processing, their application in tabular data remains relatively underexplored. This paper presents one of the first applications of an importance-scoring metric to interpret multi-head transformer models in learning from tabular data. Experiments conducted on 40 diverse tabu...
  </details>

- **2026-08-27** — Yen-Ju Lu, Yuzhe Wang, Yaohan Guan et al. — [When Text Misleads: Inconsistent-Aware Reasoning for Audio-Grounded Dialogue](http://arxiv.org/abs/2608.27176v1)
  <details><summary>📄 Abstract</summary>
  Understanding spoken dialogue requires joint reasoning over lexical content and paralinguistic acoustic signals such as emotion and conversational intent. However, existing evaluations often allow shortcuts based on transcripts or single-modality solutions, obscuring whether models genuinely ground predictions in speech. We formalize this failure mode as cross-modal disagreement, where transcripts suggest plausible but incorrect surface interpretations while acoustic cues such as prosody or spea...
  </details>

- **2026-08-27** — Bojun Zhang, Junhong Liang, Feifei Zhai et al. — [ReViCo: Unveiling the Limitations of VLMs in Visual Text Understanding via Error Correction](http://arxiv.org/abs/2608.27154v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) have shown great success in general visual tasks, yet they still struggle to deeply understand text within images. In this paper, we introduce ReViCo (Real Visual Correction), a benchmark designed to evaluate VLM text understanding through a novel task of visual text error correction. ReViCo challenges models to identify and fix text errors in real-world images, which requires a profound understanding of the interplay between visual text and its surrounding visual c...
  </details>

- **2026-08-27** — Zike Yuan, Han Zhang, Jianzhi Yan et al. — [GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL](http://arxiv.org/abs/2608.27142v1)
  <details><summary>📄 Abstract</summary>
  Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework opt...
  </details>

- **2026-08-27** — Yizhou Zhang, Wangjin Zhou, Xin Gu et al. — [Direct or Mediated? Task-Dependent Audio Information Routing in Large Audio Language Models](http://arxiv.org/abs/2608.27026v1)
  <details><summary>📄 Abstract</summary>
  Large Audio Language Models (LALMs) have demonstrated strong performance across a wide range of audio understanding tasks. However, they are typically evaluated on single, coherent audio segments, leaving their behavior under less familiar input configurations underexplored. We study this issue through a controlled setting in which two audio segments are concatenated into a single input. Across multiple LALMs, we observe a striking task-dependent robustness gap: automatic speech recognition (ASR...
  </details>

- **2026-08-27** — Kuan-Hao Tseng, Niruth Bogahawatta, Yasod Ginige et al. — [FaulT-Bench: Towards Benchmarking Network Troubleshooting LLM Agents under Unreliable User Tickets](http://arxiv.org/abs/2608.27021v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly proposed for network fault diagnosis, but existing benchmarks evaluate them only on accurate tickets and always assume a fault is present, conditions rarely met in practice. We present FaulT-Bench, a benchmark of 200 troubleshooting scenarios across eight network topologies, five reimplemented from public practitioner labs, spanning genuine faults, false fault reports, incorrect device attribution, and incorrect root-cause claims. To isolate how ticket wording a...
  </details>

- **2026-08-27** — Ashshak Sharifdeen, Shihab Aaqil Ahamed, Ufaq Khan et al. — [MVC-Bench: Benchmarking Calibration of Medical Vision-Language Models](http://arxiv.org/abs/2608.27004v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of vision-language models (VLMs) and medical vision-language models (Medical-VLMs) requires calibrated confidence, particularly under realistic clinical conditions. However, existing efforts mainly focused on improving accuracy, leaving calibration in the medical domain underexplored. To this end, we propose MVC-Bench, a calibration-centric benchmark for medical image classification with VLMs and Medical-VLMs. MVC-Bench assesses the calibration across three axes: (i) robustne...
  </details>

- **2026-08-27** — Mengyu Wang, Kozo Okada, Takafumi Goto et al. — [Graph-Based Pseudo-multimodal Contrastive Learning for 12-Lead ECG Representations](http://arxiv.org/abs/2608.26964v1)
  <details><summary>📄 Abstract</summary>
  12-lead electrocardiogram (ECG) is a standard, non-invasive examination widely used for diagnosing coronary artery disease, where clinical interpretation relies on comparing waveform patterns across multiple leads. However, most existing ECG analysis methods focus on single-lead signals or treat each lead independently, and typically process ECG signals as one-dimensional time-series data using CNNs or RNNs. While effective in modeling local waveform changes, such approaches have difficulty capt...
  </details>

- **2026-08-27** — Jiayi Kuang, Yinghui Li, Yunze Song et al. — [From Atomic to Agentic: Towards Interpretable Evaluation of LLMs' Agentic Mathematical Capabilities](http://arxiv.org/abs/2608.26950v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are evolving from performing end-to-end mathematical reasoning to integrating agentic intelligence. However, most existing math benchmarks evaluate only final answers. This outcome-oriented evaluation provides limited diagnostic value for identifying process-level failures or rigorous logic, failing to guide the transformation of LLMs into robust agents. To bridge this gap, we present a process-level benchmark designed to evaluate the inherent agentic mathematical re...
  </details>

- **2026-08-27** — Md Fantacher Islam, Jarrod Mosier, Vignesh Subbian — [DINIRS: Digital Twin for Individualized Treatment Effects of Non-Invasive Respiratory Support Strategies](http://arxiv.org/abs/2608.26915v1)
  <details><summary>📄 Abstract</summary>
  Objective: Choosing between noninvasive respiratory support (NIRS) and invasive mechanical ventilation (IMV) for patients with acute respiratory failure is a complex, time-sensitive decision with heterogeneous treatment effects across patient subgroups. Although clinical trials and guidelines provide population-level guidance, it remains unclear which patients benefit more from NIRS than IMV. We developed and validated a censoring-aware Digital Twin framework for Individualized Treatment Effects...
  </details>

- **2026-08-27** — Haowen Gu, Gensheng Pei, Junzhu Mao et al. — [From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation](http://arxiv.org/abs/2608.26856v1)
  <details><summary>📄 Abstract</summary>
  Although Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in Medical Visual Question Answering (Med-VQA), their reliance on global image features often lacks precise pixel-level grounding, thereby limiting clinical trustworthiness. To bridge the semantic gap between high-level clinical reasoning and spatial localization, we propose \textsc{\textsc{MedREAL}} (\textbf{Med}ical \textbf{RE}asoning-driven \textbf{A}nswering and \textbf{L}ocalization), a unified framew...
  </details>

- **2026-08-27** — Rongyang Zhang, Chengqiang Lu, Cong Li et al. — [Multi-Image Visual Token Pruning in Large Visual Language Models](http://arxiv.org/abs/2608.26806v1)
  <details><summary>📄 Abstract</summary>
  With the growing demand for processing multiple image sequences in real-world applications, various visual token pruning methods have emerged to mitigate the computational and context length constraints faced by Large Vision Language Models (LVLMs). However, most existing pruning approaches rely on static strategies that struggle to adapt across different architectural LVLMs and multi-image scenarios, and are additionally constrained by their dependence on attention computations that are incompa...
  </details>

- **2026-08-27** — Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji et al. — [Fixed-Haven Reservation for Online Multi-Agent Pickup and Delivery in Dense Warehouses](http://arxiv.org/abs/2608.26759v1)
  <details><summary>📄 Abstract</summary>
  Dense warehouses often contain single-lane aisles, dead ends, and tree-like guidepaths that leave little room for idle agents to wait without blocking others. Existing Multi-Agent Pickup and Delivery (MAPD) guarantees for completing all finitely released tasks typically rely on extra waiting endpoints that planned paths can avoid, or on biconnected topology; these assumptions may fail in such layouts. We study fixed-Haven reservation for online MAPD, where pickup-delivery tasks are released over...
  </details>

- **2026-08-27** — Lezhi Yu, Xiaogang Xu, Yuhua Zhou et al. — [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](http://arxiv.org/abs/2608.26753v1)
  <details><summary>📄 Abstract</summary>
  LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper's claims, and provide evidence supporting those claims. We show that agents often produce methodological hallucinations: silently reducing datasets or training budgets, replacing failed learning or generative components with lookup or oracle functions, or drawing conclusions from resource-limited settings where a me...
  </details>

- **2026-08-27** — Jintang Li, Yuhong Chen, Ruofan Wu et al. — [Rethinking Message Passing as Retrieval for Text-Attributed Graph Learning](http://arxiv.org/abs/2608.26732v1)
  <details><summary>📄 Abstract</summary>
  Graph neural networks (GNNs) are typically conceptualized as message-passing neural networks, yet it remains unclear why neighborhood aggregation reliably outperforms node-wise multilayer perceptrons (MLPs). Despite its empirical success, this paradigm can be computationally expensive and sensitive to imperfect graph structures. In this work, we present a retrieval-augmented view of GNNs: each layer makes predictions by applying an MLP to a node representation together with a permutation-invaria...
  </details>

- **2026-08-27** — Jaekeol Choi — [When Does Supervised Fine-Tuning Reduce Instruction Sensitivity?](http://arxiv.org/abs/2608.26661v1)
  <details><summary>📄 Abstract</summary>
  Large language models can exhibit substantial performance variation across alternative formulations of the same task instruction, yet it remains unclear how conventional task-specific supervised fine-tuning (SFT) changes this instruction sensitivity. We study this question by evaluating fixed model checkpoints under multiple paraphrased instructions and defining instruction sensitivity as the standard deviation of task performance across them. We conduct a controlled scale analysis with Qwen3 mo...
  </details>

- **2026-08-27** — Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng et al. — [Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs](http://arxiv.org/abs/2608.26581v1)
  <details><summary>📄 Abstract</summary>
  Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs). Recent hardware support for low-precision formats, ranging from MXFP8 to ultra-low-bit formats such as MXFP4 and HiF4, has accelerated research into efficient MLLM training and deployment. In this work, we present a systematic study of these quantization schemes in representative MLLMs that span both video generation and reasoning tasks. Our analysis shows...
  </details>

- **2026-08-27** — Yuehao Song, Zhong Chen, Lihui Cen et al. — [Physics-Informed Stochastic Configuration Machine: A Backpropagation-Free Neural Network with Fast Training for Nonlinear Differential Equations](http://arxiv.org/abs/2608.26549v1)
  <details><summary>📄 Abstract</summary>
  While Physics-Informed Neural Networks (PINNs) have emerged as a transformative paradigm for solving complex differential equations, their reliance on backpropagation-based gradient descent and automatic differentiation (AD) imposes significant computational bottlenecks and severe non-convex optimization challenges. To overcome these fundamental limitations, we propose the Physics-Informed Stochastic Configuration Machine (PI-SCM), a novel backpropagation-free framework for both forward and inve...
  </details>

- **2026-08-26** — Siddharth Setlur, Djordje Mihajlovic, Darrick Lee — [Interpreting Latent Protein Language Model Features with Geometric Annotations](http://arxiv.org/abs/2608.26419v1)
  <details><summary>📄 Abstract</summary>
  Protein language models (pLMs) encode information about protein sequences which enable downstream tasks such as structure prediction, but their internal representations are not well understood. Sparse autoencoders (SAEs) provide a promising tool to disentangle latent pLM representations into interpretable features, but existing annotation pipelines largely rely on protein-level annotations derived from database labels and LLM annotations of top activating sequences. Such annotations can overlook...
  </details>

- **2026-08-26** — Cesar Santos, Michele Vitagliano, Roberto Natella et al. — [Investigating Software Aging in LLM-Generated Software Systems across Generation-and-Execution Environments](http://arxiv.org/abs/2608.26391v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used to generate executable software systems from natural language specifications, accelerating development and reducing manual implementation effort. Although recent studies have investigated the functional correctness, security, maintainability, and robustness of LLM-generated code, little is known about the long-term reliability of such systems under sustained execution. In this paper, we experimentally investigate software aging symptoms in LLM-g...
  </details>

- **2026-08-26** — Yefan Tao, Gerald Friedland, Luyang Kong — [When Is Noise Response Universal? Tokenization as the Hidden Variable in Language Models](http://arxiv.org/abs/2608.26319v1)
  <details><summary>📄 Abstract</summary>
  The performance of textual neural models often degrades when their inputs are corrupted by noise such as typos, OCR errors, or dropped words. We study the degradation rate across neural models, both sentence embeddings and decoder-only LLMs, and find that how consistent it is depends on the scale of the noise: under word-level noise, models with very different architectures decline along nearly the same curve, while under character-level noise they separate. We further identify the determining f...
  </details>

- **2026-08-26** — Arseniy Varlamov, Rishat Zinnatullin, Elisei Rykov et al. — [MemToC: Benchmarking Memory-Tool Conflict Resolution in Large Language Models](http://arxiv.org/abs/2608.26295v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented LLMs must arbitrate between two fallible sources when a tool return conflicts with their parametric memory, yet existing evaluations measure source preference without establishing source correctness. We introduce MemToC, a controlled benchmark for post-tool-return arbitration with executable tools. MemToC comprises 6,504 evaluation episodes constructed from 542 quality-controlled factual questions, independently elicited model-specific closed-book answers, and controlled tool retu...
  </details>

- **2026-08-26** — Mazhar Shaikh, Anurag Rajkumar Bombarde, Harshal Pathak — [Agent Mesh: Reliability Primitives for Non-Idempotent Agent Delegation - Identity Adequacy and Evidence Adequacy](http://arxiv.org/abs/2608.26225v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents increasingly perform bounded software tasks under an orchestrator that retries, resumes, and budgets them. The machinery such orchestrators reach for is the service mesh's: retry, timeout, and error-rate circuit breaking. We report a failure study of a production agentic software-delivery platform over 147 numbered incidents spanning 81 runs, each with a measured cost and, in most cases, a mutation proof reproducing the failure. All three assumptions those primitives rest on ar...
  </details>

- **2026-08-26** — Kazuki Nakayashiki — [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](http://arxiv.org/abs/2608.25553v2)
  <details><summary>📄 Abstract</summary>
  An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record. Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the resulting stale-consistent decision avoidable without spending more? We model supersession explicitly -- provenance is immutable; what changes is which record is current -- and assign by design the memory's form, the world's state and the verifica...
  </details>

- **2026-08-26** — YoungChae Kim, Da-Hee Yang, Joon-Hyuk Chang — [Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition](http://arxiv.org/abs/2608.26213v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based audio-visual speech recognition (AVSR) systems are robust under noise. Contrastive decoding (CD), originally introduced to stabilize LLM generation by contrasting a weaker model against a stronger one at inference time, adjusts predictions without additional training. In this work, we apply CD to AVSR by contrasting audio-only conditioning with full audio-visual conditioning within the same underlying model. However, using a fixed contrastive strength introduces ...
  </details>

- **2026-08-26** — Yuexin Sun, Zhaohui Wang, Ruiyang Liu et al. — [TailorCoPilot: Enabling Agentic Pattern Making with Version-Controlled State Tracking](http://arxiv.org/abs/2608.25462v2)
  <details><summary>📄 Abstract</summary>
  Experience-driven manufacturing, such as garment pattern making, faces a severe generational skills gap because its core expertise relies on undocumented tacit knowledge forged through day-to-day practice. To address this challenge, we present TailorCoPilot, an agentic pattern-making system built upon a specially designed version-control backend TailorTrace. TailorTrace models sewing patterns as structured, discrete states and records their transformations during the pattern-making process as ex...
  </details>

- **2026-08-26** — Ali Asadi, Krishnendu Chatterjee, Ehsan Kafshdar Goharshady et al. — [Quantitative Analysis of $ω$-Regular Robust MDPs](http://arxiv.org/abs/2608.25968v1)
  <details><summary>📄 Abstract</summary>
  Robust Markov Decision Processes (RMDPs) generalize classical MDPs by allowing uncertainty in transition probabilities and optimizing against their worst-case realization. We consider $(s,a)$-rectangular RMDPs with \emph{linearly defined} uncertainty sets and study parity objectives, which are a canonical representation of $ω$-regular objectives. An uncertainty set is linearly defined if it is described by linear inequalities over the transition distribution together with auxiliary variables, wh...
  </details>

- **2026-08-26** — Martin Koutecký, Nikolaos Melissinos, Tung Anh Vu et al. — [Continuous Computational Social Choice: A Case Study in Bribery](http://arxiv.org/abs/2608.25444v1)
  <details><summary>📄 Abstract</summary>
  Computational social choice seeks algorithmic answers to questions about preference aggregation, safety of elections, robustness of outcomes, stability, etc. It overwhelmingly models societies as composed of discrete agents.   We propose to study computational social choice problems in a society continuum} setting, where a society is modeled as a distribution of infinitely many infinitesimal agents of different types. An analogous approach has been very useful in physics (it is the basis of stat...
  </details>

- **2026-08-26** — Yao Fu, Lijia Huang, Xiaomin Li et al. — [When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs](http://arxiv.org/abs/2608.25977v1)
  <details><summary>📄 Abstract</summary>
  Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences. While the Myers--Briggs Type Indicator (MBTI) has emerged as a common framework for assessing LLMs' personality, existing studies focus primarily on full-precision models and evaluate only final outputs. They overlook the widespread deployment of quantized LLMs requiring low memory footprints, whose personality traits remain underexplored. In this work, we pres...
  </details>

- **2026-08-26** — Jia-Hao Ji, Sijie Li, Jiabei Cheng et al. — [Candidate supply and answer selection shape the value of LLM judging in multi-agent systems](http://arxiv.org/abs/2608.25937v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when...
  </details>

- **2026-08-26** — Junjie Meng, Ranxu Zhang, Zi-an Zhang et al. — [CEDAR: Controlled and Event-Driven Demand Forecasting via Residual Decomposition](http://arxiv.org/abs/2608.25871v1)
  <details><summary>📄 Abstract</summary>
  Forecasting in large-scale e-commerce marketplaces is increasingly required to support planning: merchants need to evaluate sales outcomes under future action sequences such as budget schedules, rather than passively predicting what happens next. However, most existing time series forecasting (TSF) approaches remain inherently passive. Even when incorporating operational decisions as auxiliary covariates, they typically optimize for correlation-based extrapolation under historical policies. This...
  </details>

- **2026-08-26** — Reza Khakpour, Arsalan Hashemi, Xiaoya Chang et al. — [Nuclearity of Copper Clusters on hBN/SiC Heterostructure Modulates Molecular Adsorption](http://arxiv.org/abs/2608.25640v1)
  <details><summary>📄 Abstract</summary>
  Defect engineering can transform inert two-dimensional (2D) materials into chemically active and electronically tunable platforms by creating anchoring sites for metal atoms and clusters. Nevertheless, precise control over the formation, thermodynamic and kinetic stability, electronic structure, and chemical reactivity of metal species confined at these defect sites remains a challenge. Here, we use density functional theory (DFT) calculations assisted by machine-learning molecular dynamics (MLM...
  </details>

- **2026-08-26** — Ziyuan Wang, Yifan Sui, Wei Wei et al. — [AERIS: Offline Policy Improvement for Multi-UAV Integrated Sensing and Communication](http://arxiv.org/abs/2608.25477v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicle (UAV)-enabled integrated sensing and communication (ISAC) is a promising 6G paradigm, but dynamic multi-UAV ISAC control must jointly balance communication quality, sensing reliability, and flight safety under stochastic mobility. Existing optimization methods often require repeated global non-convex solving, while online reinforcement learning (RL) depends on risky trial-and-error flights that may cause sensing loss or collision-risk events.   This paper proposes AERIS, ...
  </details>

- **2026-08-26** — Jiaxin Yuan, Connor Martinez Lockhart, Xiaoyu Liu et al. — [MathAdv: What Theorem Provers Know, Reason, Formalize, and Generalize](http://arxiv.org/abs/2608.25449v1)
  <details><summary>📄 Abstract</summary>
  Formal theorem proving enables machine-verifiable evaluation of mathematical reasoning, yet existing benchmarks often emphasize aggregate proof accuracy, concentrate on a narrow range of mathematics, and provide limited evidence of robustness to equivalent reformulations. We introduce MathAdv, a diagnostic benchmark spanning 13 domains across undergraduate- and graduate-level mathematics. Alongside Lean 4 theorem proving, MathAdv provides up to three auxiliary tasks: multiple-choice questions th...
  </details>

- **2026-08-26** — Zhe Liu, Jinghua Hou, Yuxiang Lu et al. — [StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models](http://arxiv.org/abs/2608.26067v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters. One core design is instruction-anchored...
  </details>

- **2026-08-26** — Kaku E. Eduku, Pavel P. Popov, Gustaaf Jacobs — [Neural-Network and Reduced-order Modeling Workflows for AI-Driven CFD: Fast Response Surfaces, Reduced Dynamics and Jet in Cross-flow Examples](http://arxiv.org/abs/2608.26064v1)
  <details><summary>📄 Abstract</summary>
  Highly resolved computational fluid dynamics (CFD) simulations are essential for design but too expensive for dense design-space sampling. This chapter presents an AI-driven CFD workflow that combines scalar-response modeling and reduced-order dynamics using jet-in-cross-flow examples. A reacting hydrogen jet-in-cross-flow study is first used to train a multilayer perceptron (MLP) mapping injector spacing to unburnt hydrogen throughput, wall heat transfer, and bulk temperature concentration, wit...
  </details>

- **2026-08-26** — Ilya Mullyadzhanov, Sergey Dremov, Andrey Gelash — [Numerical Direct Scattering Transform for Dark Solitons](http://arxiv.org/abs/2608.26054v1)
  <details><summary>📄 Abstract</summary>
  We introduce a numerical direct scattering transform scheme for dark solitons of the nonlinear Schrodinger equation, enabling the identification and complete characterization of nonlinear coherent structures in defocusing media with a continuous-wave (CW) background. Our scheme is based on numerically solving the auxiliary Zakharov-Shabat scattering problem with CW boundary conditions and on analytically derived expressions that relate the elements of the transfer matrix to the scattering data f...
  </details>

- **2026-08-26** — Dung Le Quang, Dong Cao Van, Nam Le Hai et al. — [XREPOTEST: Benchmarking Multilingual Repository-Level Unit Test Generation for Large Language Models](http://arxiv.org/abs/2608.25939v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown promise for automated unit test generation, but existing evaluations largely rely on standalone settings and a narrow set of programming languages, overestimating real-world readiness. We introduce XREPOTEST, a multilingual repository-level benchmark for unit test generation spanning five underexplored languages: Rust, Go, Julia, PHP, and Ruby. XREPOTEST evaluates tests under realistic repository constraints using a containerized execution framework and mu...
  </details>

- **2026-08-26** — Zhongwen Luan, Xiaoyu Zhang, Ming Hu et al. — [Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems](http://arxiv.org/abs/2608.25920v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM)-based multi-agent systems (MASs) are increasingly applied to long-horizon complex tasks, their reliability has emerged as the core bottleneck hindering their real-world deployment. Existing MAS debugging and repair methods typically rely on rerunning and resampling the entire execution trajectory. However, a fundamental question remains to be answered: do these methods causally repair MAS failures or merely stochastically repair by leveraging the randomness of LLM s...
  </details>

- **2026-08-26** — Feng Ling, Heng Yu — [ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking](http://arxiv.org/abs/2608.25775v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) exhibit strong problem-solving abilities, positioning them as promising agents for Socratic teaching to guide students through step-by-step heuristic questioning. However, existing approaches typically adopt a one-problem-one-solution paradigm, restricting the teaching guidance to a single linear reasoning path. This design limits instructional flexibility, weakens error recovery, and restricts students' ability to engage in parallel thinking to explore multiple vali...
  </details>

- **2026-08-26** — Akshat G, Divyansh Gupta, Shaleen Bhatnagar et al. — [Unsupervised Anatomical Feature Learning via Diffusion Models: Enhanced Medical Image Segmentation with Denoising Diffusion Probabilistic Models](http://arxiv.org/abs/2608.25693v1)
  <details><summary>📄 Abstract</summary>
  Acquiring pixel-level annotations for medical image segmentation is a severe bottleneck. Traditional U-Net architectures, while effective, learn local texture patterns and lack awareness of global anatomical structures, leading to boundary delineation failures in low-data regimes. This research paper proposes utilizing unsupervised Denoising Diffusion Probabilistic Models (DDPMs) to extract anatomical features. We train a DDPM on 21 unlabeled abdominal CT scans to learn structural representation...
  </details>

- **2026-08-26** — Jongsuk Kim, Qiyu Wu, Zhuoyuan Mao et al. — [MLLMCLIP: Feature-Level Distillation of MLLM for Robust Vision-Language Representations](http://arxiv.org/abs/2608.25575v1)
  <details><summary>📄 Abstract</summary>
  Pretrained vision-language models such as CLIP excel at zero-shot recognition but often fail at compositionality, particularly attribute-object and relational structures. Recent studies mitigate this issue by augmenting training with synthetic hard negatives generated by a cascade of large language models and text-to-image models, which incurs substantial pipeline overhead. We instead propose MLLMCLIP, a heterogeneous distillation framework that transfers multimodal knowledge directly from a gen...
  </details>

- **2026-08-26** — Yankai Rong, Shuang Liu, Jinhao Dong et al. — [DBcover: A White-box SQL Test Generation Framework for Coverage Improvement](http://arxiv.org/abs/2608.25573v1)
  <details><summary>📄 Abstract</summary>
  Relational Database Management Systems (RDBMSs) are the backbone of modern data-intensive applications, making reliability and robustness critical. However, achieving high coverage in RDBMS testing remains challenging because of large codebases and complex execution logic. Traditional fuzzing relies on random SQL generation and cannot capture the correspondence between SQL inputs and internal execution paths, while symbolic execution suffers from prohibitive cost and scalability limitations.   W...
  </details>

- **2026-08-26** — Kazuki Nakayashiki — [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](http://arxiv.org/abs/2608.25553v1)
  <details><summary>📄 Abstract</summary>
  An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record. Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the error avoidable without spending more? We model supersession explicitly -- historical provenance is immutable; what changes is which record is current -- and assign by design the memory's form, the world's state (source current or superseded), and...
  </details>

- **2026-08-26** — Zhifei Zheng, Yunfei Liu, Bin Liu et al. — [TransRetrieval: Scaling Up Transformer-Based Retrieval for Industrial Recommendation](http://arxiv.org/abs/2608.25528v1)
  <details><summary>📄 Abstract</summary>
  Applying scaling laws to recommendation retrieval is hindered by feature heterogeneity: naively stacking Transformer layers yields diminishing returns because heterogeneous fields produce severe token-norm divergence. We present TransRetrieval, a Transformer-based retrieval framework that scales with both computational budget and cross-domain data. The key enabler is (1) weighted average aggregation, which restores the homogeneous-token assumption Transformers rely on. Building on this, we intro...
  </details>

- **2026-08-26** — Abdalrhaman Koko, Sodiq Abiodun Kareem, Olajesu Favor Olanrewaju et al. — [Direct current thermo-mechanical testing: Principles, uncertainty hierarchy, and its role in advanced materials characterisation](http://arxiv.org/abs/2608.25525v1)
  <details><summary>📄 Abstract</summary>
  Direct current thermo-mechanical testing (DC-TMT), based on resistive Joule heating, enables rapid heating and cooling, steep thermal gradients and simultaneous mechanical loading, making it a powerful tool for probing deformation, phase transformations, oxidation-assisted damage and creep under conditions inaccessible to conventional furnace-based methods. Despite its growing use, DC-TMT lacks formal standardisation and is often misinterpreted as equivalent to bulk isothermal testing, overlooki...
  </details>

- **2026-08-26** — Yuexin Sun, Zhaohui Wang, Ruiyang Liu et al. — [TailorCoPilot: Enabling Agentic Pattern Making with Version-Controlled State Tracking](http://arxiv.org/abs/2608.25462v1)
  <details><summary>📄 Abstract</summary>
  Experience-driven manufacturing, such as garment pattern making, faces a severe generational skills gap because its core expertise relies on undocumented tacit knowledge forged through day-to-day practice. To address this challenge, we present TailorCoPilot, an agentic pattern-making system built upon a specially designed version-control backend TailorTrace. TailorTrace models sewing patterns as structured, discrete states and records their transformations during the pattern-making process as ex...
  </details>

- **2026-08-26** — Pedro Ornelas, Ramona Bedford, Fazilah Nothlawala et al. — [Quantum skyrmion parallelism via metasurface-tailored high-dimensional entanglement](http://arxiv.org/abs/2608.25415v1)
  <details><summary>📄 Abstract</summary>
  Quantum skyrmions are topological structures that have garnered significant interest due to their demonstrated robustness and versatility across diverse optical platforms. However, existing approaches for their generation are limited to producing pre-determined two dimensional qubit states with a single topology. Here we create multi-dimensional topological states by introducing a non-local interaction between high-dimensional photonic entanglement and a metasurface, where the topological transf...
  </details>

- **2026-08-26** — Yeguang Qin, Liangqi Peng, Fengxiao Tang et al. — [SPFR: Semantic Potential Field Routing for the Distributed Internet of Agents](http://arxiv.org/abs/2608.25396v1)
  <details><summary>📄 Abstract</summary>
  In a distributed Internet of Agents (IoA) without centralized routing control, routing tasks to capability-matched executors is challenging because destinations are not predetermined and agents have bounded local service views. Discover-then-forward approaches, by contrast, select an executor before network forwarding and therefore do not directly support reselection when additional candidates become visible downstream. We introduce Semantic Potential Field Routing (SPFR), a distributed IoA rout...
  </details>

- **2026-08-26** — Zhenyu Zhao, Tiankui Zhang, Xiaoxia Xu et al. — [Traffic-Adaptive Per-Hop Multipath Routing in Multi-Hop UAV Networks](http://arxiv.org/abs/2608.25383v1)
  <details><summary>📄 Abstract</summary>
  In uncrewed aerial vehicle (UAV)-relayed mobile edge computing (MEC) networks, computation tasks generate traffic with diverse latency requirements and data sizes. Routing decisions therefore need to adapt to both traffic characteristics and changing network conditions. Compared with single-path routing, multipath routing is better suited to such heterogeneous traffic because it provides multiple forwarding options and enables flexible traffic splitting. However, conventional multipath routing u...
  </details>

- **2026-08-26** — Anqi Peter Li — [Activation-Space Order-Swap Geometry: A Site-Asymmetry Audit](http://arxiv.org/abs/2608.25315v1)
  <details><summary>📄 Abstract</summary>
  Order-dependent activation statistics are often interpreted as evidence of interaction, but that interpretation can be confounded by where interventions enter the network. We introduce a no-fit site-asymmetry audit. For a twice-differentiable readout, the open-path order-swap decomposes into a canonical additive response measured by single interventions and an antisymmetrized second difference free of first-order and pure self-curvature terms to second order. Across six open-weight language-mode...
  </details>

- **2026-08-25** — Leonardo Liparulo, Francesco Pierri — [Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling](http://arxiv.org/abs/2608.26199v1)
  <details><summary>📄 Abstract</summary>
  We ask whether AI agents powered by locally deployed large language models can reliably automate expert-defined hardware design workflows in an industry-realistic tool-calling setting. In these environments, engineers issue repetitive, dependency-ordered operations---such as creating components, adding ports, and wiring connections---through specialised tools. Confidentiality constraints on component specifications and naming conventions often preclude hosted proprietary APIs, motivating the use...
  </details>

- **2026-08-25** — Jai Kumar Sharma, Peeyush Tapadiya — [Can You Trust Frozen Hematology Foundation Models under Acquisition Shift?](http://arxiv.org/abs/2608.25148v1)
  <details><summary>📄 Abstract</summary>
  Frozen hematology foundation-model (FM) embeddings reach near-saturated in-domain white-blood-cell (WBC) accuracy, but clinical deployment demands reliability across scanners, sites, stains and preparation pipelines. We audit 15 frozen encoders (hematology, pathology, and general vision) across four public single-cell acquisition domains along two axes: accuracy robustness and calibration. In-domain linear-probe macro-F1 is saturated (0.98-0.997), yet cross-dataset macro-F1 drops 34-72% and rank...
  </details>

- **2026-08-25** — Mohammed Adjieteh, Vytaras Brazauskas — [Quantile and Log-Quantile Least Squares for Robust-Efficient Fitting and Validation of Log-Location-Scale Loss Models](http://arxiv.org/abs/2608.25234v1)
  <details><summary>📄 Abstract</summary>
  \begin{quote} {\bf\em Abstract\/}. ~A variety of models for insurance and other types of losses are special cases of the {\em log-location-scale\/} family, with the lognormal and Pareto-$I$ distributions being the most prominent examples. The latter also serves as a primary example of infinite-mean models that often present challenges in risk management. In this paper, we utilize two {\em asymptotic\/} theorems -- the joint normality of sample quantiles (of {\em i.i.d.\/} random variables) and t...
  </details>

- **2026-08-25** — Henry Robbins, Connor Lawless, Madeleine Udell et al. — [FLARE: Verifying MILP Reformulations with LLM-Based Theorem Proving](http://arxiv.org/abs/2608.25220v1)
  <details><summary>📄 Abstract</summary>
  Mixed-Integer Linear Programming (MILP) is a fundamental tool for combinatorial optimization with extensive real-world applications. A central challenge is designing computationally efficient MILP formulations. Large Language Models (LLMs) offer new opportunities to automate the modeling process, from deriving formulations to strengthening them. Reliable automation requires robust methods for verifying that proposed formulations preserve the underlying optimization problem. However, existing app...
  </details>

- **2026-08-25** — Madelaine Martinez-Ferguson, Chun Wang, Mustafa Can Camur et al. — [Simulating Cognitive Smart Freight Corridors with Agent-Based Models and Reinforcement Learning](http://arxiv.org/abs/2608.25193v1)
  <details><summary>📄 Abstract</summary>
  Smart freight corridors offer a practical pathway for connected and automated vehicle (CAV) deployment in freight transportation, but physical experimentation is expensive and existing approaches rely on predefined control policies that cannot capture adaptive behaviors. This paper presents an agent-based modeling (ABM) framework coupling a physical infrastructure layer, a connectivity layer (V2X), and a decision layer integrating reinforcement learning (RL) and multi-agent reinforcement learnin...
  </details>

- **2026-08-25** — Kaiqiao Han, Yizhou Sun — [The Imperfective Paradox Is Not Necessarily in Large Language Models: A Benchmark Failure Before a Model Failure](http://arxiv.org/abs/2608.25005v1)
  <details><summary>📄 Abstract</summary>
  The imperfective paradox provides a useful test of compositional semantic analysis. Recent work constructs an NLI benchmark and reports that models frequently infer completed telic events from progressive descriptions, attributing this behavior to a Teleological Bias. It further argues that prompting interventions cause a Calibration Crisis. We reexamine the benchmark and conclusions and show that it is substantially affected by conceptual and evaluation mis-specifications. We identify three con...
  </details>

- **2026-08-25** — Qian Cao, Zhen Bi, Kater W. Murch — [Mixed-State Symmetry-Protected Topology and Strong-to-Weak Spontaneous Symmetry Breaking in a Superconducting Qubit Array](http://arxiv.org/abs/2608.24993v1)
  <details><summary>📄 Abstract</summary>
  We experimentally investigate how symmetry-protected topological order in a one-dimensional cluster state is transformed by measurement and decoherence in a five-qubit superconducting array. We first characterize the state's nonlocal string order and show that controlled dephasing selectively suppresses one symmetry sector while leaving the other robust, consistent with average symmetry-protected topological order. We then measure one sublattice in a tunable basis and show that the remaining qub...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-08-27** — Ke Shu, Kira Hinderks, Eetu Mäkelä et al. — [Pair-Level Essay-Scale Republication and Reuse from Fragmented Historical Text Reuse: A Workflow Study on Eighteenth-Century Books and Newspapers](http://arxiv.org/abs/2608.27343v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the recovery of essay-scale republication and reuse from fragmented text-reuse evidence, a setting whose central challenge is pair-level evidence consolidation and not fragment retrieval alone. The study focuses on a candidate set centered on essays by eighteenth-century Scottish philosopher David Hume, spanning books from ECCO (Eighteenth Century Collections Online) and historical newspapers. Because the input consists of fragmented reuse hits instead of clean document pair...
  </details>

- **2026-08-27** — Jeong-Yoon Kim — [BTS-AgentBench: A Deterministic, Replayable Pipeline from Read-Only Telemetry Logs to Agent Benchmarks](http://arxiv.org/abs/2608.27334v1)
  <details><summary>📄 Abstract</summary>
  Industrial sites contain large volumes of read-only telemetry, but few benchmarks specify how to compile these records into executable multi-turn agent tasks. We present a telemetry-to-episode construction method instantiated as BTS-AgentBench. The pipeline normalizes BTS metadata and raw histories into a read-only tool store, compiles static tasks with tool-derived gold answers and evidence, and lifts retained tasks into typed, bounded operator-facing episodes. The 532-row release adds clarific...
  </details>

- **2026-08-27** — Jinghan Xu, Yikai Zhang, Aili Chen et al. — [Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware Verification](http://arxiv.org/abs/2608.27311v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses shape how language-model agents use instructions, tools, and runtime components, but adapting these harnesses requires costly verification. Existing propose-and-verify methods typically score every candidate on a fixed task set, wasting rollouts on unrelated behaviors and allowing aggregate scores to obscure specific regressions. We introduce HarnessLens, a budget-aware framework for automated harness evolution. HarnessLens jointly explores the task space and user-configurable co...
  </details>

- **2026-08-27** — Xiaokun Guo, Zhen Xu, Dongdong Huo et al. — [When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents](http://arxiv.org/abs/2608.27146v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become ``commands'' that can drive real-world side effects beyond user intent. We argue that this risk arises from conflating action induction with execution authorization. To address this distinction, we propose SARA, which treats action induction and execution authorization as distinc...
  </details>

- **2026-08-26** — Roberto Riaño, Gorka Abad, Stjepan Picek et al. — [MeMark: Membrane-Space Watermarking for Spiking Neural Networks](http://arxiv.org/abs/2608.25738v1)
  <details><summary>📄 Abstract</summary>
  Spiking Neural Networks (SNNs) are increasingly distributed as pretrained checkpoints and reused as backbones for new tasks. However, current SNN watermarks are mainly verified against the model output. Thus, a user who replaces the output head can keep most of the original network while removing the evidence used for verification. We present MeMark, a watermark designed for the checkpoint-reuse setting. Instead of storing the watermark in the output head, MeMark embeds a multi-bit identifier in...
  </details>

- **2026-08-26** — Mihnea C. Moldoveanu, Joel A. C. Baum — [Epistemic Networks, Collective Misperception, and the Manipulation of Social Knowledge](http://arxiv.org/abs/2608.26075v1)
  <details><summary>📄 Abstract</summary>
  We investigate the structure of interactive beliefs in networks: the epistemic state in which agents hold, revise, and act on their models of the epistemic states of other agents. What a group believes depends on what each member agent takes the others to believe, and on what each takes the others to believe about still others. We posit that the proper unit of social-epistemic analysis is not the individual belief but the tensor of mutual attribution, the array that records what every agent take...
  </details>

- **2026-08-26** — Zhifei Xie, Jiaqi Lang, Ze An et al. — [VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction](http://arxiv.org/abs/2608.26005v1)
  <details><summary>📄 Abstract</summary>
  Conversational systems, such as duplex speech language models (SLMs), still lack a streaming, accurate, and empathetic memory system as their soul. We introduce VoiceMem, a simple memory architecture with a parallel informational left brain, an emotional right brain, and streaming memory I/O mechanisms. We further build a complete pipeline for memory-aware SLM training, long-horizon evaluation, and decoupled deployment with interchangeable memory backends. Experiments and real-world deployment s...
  </details>

- **2026-08-26** — Gianmaria Silvello — [Data Citation for Large Language Models: A Challenge](http://arxiv.org/abs/2608.25663v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly mediate access to information, and a growing body of work asks whether they cite the sources behind their outputs. That work treats citation as a verification device and applies it to textual documents. Scholarly citation serves two further functions, credit and provenance, and it applies to data as much as to text. This paper argues that data citation for large language models is an open challenge, distinct from document-level citation grounding and harder to ...
  </details>

- **2026-08-26** — Yu Wang, Jiaheng Lu — [PolyMemDB: A Polyglot Database System for AI Memory Management](http://arxiv.org/abs/2608.25577v1)
  <details><summary>📄 Abstract</summary>
  With the widespread adoption of personal intelligent agents, users generate massive, heterogeneous data during long-term interactions. Leveraging this data as long-term memory helps reduce token overhead and deliver personalized experiences. However, existing memory systems face two primary limitations: they rely on single-storage paradigms that fragment multi-dimensional data, and they lack fine-grained data provenance to resolve long-term factual conflicts, thereby worsening LLM hallucinations...
  </details>

- **2026-08-26** — Shi-Qi Yan, Kai-Xuan Ding, Chao-Hong Tan et al. — [Short Horizons and Sparse Concepts: a Mathematical View of the Readout in the J-lens](http://arxiv.org/abs/2608.25347v1)
  <details><summary>📄 Abstract</summary>
  The Jacobian lens (J-lens) has been proposed as a way to read verbalizable representations from language models. However, its principle and meaning lack a detailed and theoretical discussion. We provide a mathematical view of this interpretation and of its assumed causal structure. Besides treating the J-lens as a heuristic probe, we further regard it as a first-order causal transfer operator from intermediate activations to expected future readouts. We study the Jacobian matrix as the optimal l...
  </details>

- **2026-08-26** — Xiao Fan, Jingyuan Li, Hongbin Guo et al. — [Provenance Before Prose: Claim-Locked Reporting](http://arxiv.org/abs/2608.25336v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can fluently verbalize statistical evidence, yet statistical reports can still drift numerical values, invert effect directions, or restate thresholded contrasts as categorical effects. We frame these failures as a control problem: the evidence-bearing content of a scientific report should be fixed by structured statistical results rather than sampled during prose generation. We therefore use cross-run reproducibility to stress-test whether report-visible numbers and...
  </details>

- **2026-08-26** — Chenglong Ma, Xinye Wanyan, Danula Hettiachchi et al. — [The "Curse of Knowledge" in LLM Query Simulation: Concept Provenance for Tracing Answer-Side Intrusion](http://arxiv.org/abs/2608.25245v1)
  <details><summary>📄 Abstract</summary>
  LLM-generated search queries are widely used to augment IR evaluation, yet they may contain concepts that presuppose answer-side document knowledge, violating the information-access boundary of pre-search users. Existing validation metrics, including overlap, diversity, and effectiveness, cannot distinguish rare human-tail variation from candidate answer-side intrusion. We introduce concept provenance, a framework that assigns query concepts to backstory-supported, human-central, human-tail, and...
  </details>

- **2026-08-25** — Yiming Lin, Sepanta Zeighami, Aditya G. Parameswaran — [Bolt-on, Verifiable Provenance for LLM-Powered Data Processing](http://arxiv.org/abs/2608.25210v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are powerful tools for processing data. However, LLMs are also complex black-boxes, returning answers to queries on data,   without any indication for where the answer came from or whether it is trustworthy. We introduce the notion of provenance for data processing with LLMs. While   existing heuristics (such as embedding similarity or directly asking an LLM) could provide some hints for where the answer was derived, they provide no guarantees   that the answer can b...
  </details>

- **2026-08-25** — Haoyi Qiu, Genglin Liu, Pranav Narayanan Venkit et al. — [Belief Cascades Drive Persuasion in LLM Agent Networks](http://arxiv.org/abs/2608.25152v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems increasingly debate answers, coordinate research, simulate users, and mediate information flows, making agent-to-agent persuasion a basic but undermeasured capability. We introduce a controlled testbed for studying how goal-directed persuaders shift elicited stances in networks of LLM agents grounded in real-world ego-network topologies. Across four LLM backbones, five graphs, and 55 policy statements, we find that persuasion dynamics depend on the interaction between top...
  </details>

- **2026-08-25** — Armaan Sandhu, Abhilasha Senapati, Hima Kammachi — [Targeting the Attention Heads Behind Object Hallucination in LLaVA](http://arxiv.org/abs/2608.24966v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as LLaVA-1.5-7B often hallucinate objects absent from the image when generating captions. We ask whether an interpretability diagnosis of this failure can guide a targeted fix, and we measure what that fix actually changes. We rank attention heads by how much their image attention drops around hallucinated object words, then screen the shortlist by ablating candidate heads and measuring the change in hallucination-token log probability, yielding a 32-head set. We rest...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-08-27** — Anik Saha, Fahmida Sultana Naznin, Sadatul Islam Sadi et al. — [DocTalkBN: A Novel Dataset of Expert Telemedicine Conversations in Bengali](http://arxiv.org/abs/2608.27110v1)
  <details><summary>📄 Abstract</summary>
  Reliable medical conversational AI requires authentic expert--patient interaction data, yet such datasets remain scarce, especially for low-resource languages such as Bengali. We present DocTalkBN, a large-scale multimodal dataset of real-world expert telemedicine conversations in Bengali, collected from nationally broadcast telemedicine programs featuring board-certified physicians. DocTalkBN contains 557.63 hours of paired audio and text, 1,515 multi-turn patient calls, 10,274 host--doctor que...
  </details>

- **2026-08-27** — Guang Yang, Xing Hu, Xiang Chen et al. — [Unsaid, Unsafe? Implicit Security Obligations in LLM-Based RTL Code Generation](http://arxiv.org/abs/2608.26588v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) generate register-transfer-level (RTL) code with rapidly improving functional correctness. Security of LLM-generated code, however, has been studied mainly for software, where flaws can still be patched after deployment. Insecure RTL offers no such remedy once taped out into silicon. We construct SECRTL-GEN, a multi-language resource-access security benchmark grounded in real SoC IP: 392 tasks over five CWE families and four HDLs (Verilog, SystemVerilog, VHDL, and Py...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-08-27** — Maciej Besta, Leonard Schmidt, Lara Nonino et al. — [Performance Foundations of Parallel & Distributed Reasoning Language Models](http://arxiv.org/abs/2608.27046v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Rewards (RLVR) and other RL-style post-training paradigms have been used for aligning large language models (LLMs) with reasoning standards. The resulting recent Reasoning Language Models (RLMs) such as DeepSeek-R1, o3, and Kimi k1.5 show that such RL-style post-training ("RL-for-LLMs") can substantially improve chain-of-thought reasoning, long-horizon planning, and self-correction. However, the computational footprint of these systems is massive: state-of-...
  </details>

- **2026-08-27** — Mirko Degli Esposti — [Animarium: an open, reproducible pipeline for synthetic populations of Italian cities, from ISTAT sources to open data (Tech Report v1)](http://arxiv.org/abs/2608.27111v1)
  <details><summary>📄 Abstract</summary>
  Synthetic populations of eleven Italian municipalities (1,814,317 individuals in 887,937 households) generated from published aggregates alone: ISTAT census and register tables, census-section counts, the national civic-address register, public-use survey microdata, and six municipal open-data portals, every source certified in a registry with licence, fingerprint and declared affordances. Four rings give every attribute a declared place: a maximum-entropy joint model of up to nine demographic a...
  </details>

- **2026-08-26** — Hongbo Liu, Peixian Chen, Sihan Liu et al. — [Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios](http://arxiv.org/abs/2608.25529v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have shown strong performance in video understanding. However, their ability to follow instructions in this domain remains under-explored. Real-world video understanding requires models not only to interpret video content correctly, but also to satisfy diverse user-specified constraints. Existing benchmarks focus primarily on task accuracy rather than instruction adherence, leaving this capability insufficiently evaluated. To address this gap, we introduc...
  </details>

- **2026-08-26** — Sadman Sakib, Zhangyi None Peng, Yujie Pang et al. — [A Taxonomy of Construction Task Activities for Robot Workers](http://arxiv.org/abs/2608.25395v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language-action models offer a path toward robots with broader repertoires than conventional task-specific systems. Construction deployment, however, requires a precise inventory of worker activities and the capabilities needed to execute them. We present TARCAT, an occupation-grounded taxonomy derived from 91 O*NET tasks across seven high-employment construction occupations and 30 instructional videos of physical work. TARCAT defines 41 action primitives in 12 groups and three cla...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 154 papers

- **2026-08-27** — Stian Lybech, Eun-Young Kang, Riccardo Tonello et al. — [Information Flow Control in Off-Chain Components](http://arxiv.org/abs/2608.26858v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a model of a smart-contract language for a blockchain architecture with off-chain components. Off-chain components are pieces of smart contracts that execute at designated locations outside of the network of blockchain nodes, but remain synchronised with the on-chain contract state. They react to changes to the on-chain state, but may also notify the on-chain component about events in the world, e.g. stock prices, weather data etc., or even act as a bridge between different b...
  </details>

- **2026-08-27** — Gyouk Chu, Myeongho Jeon, Eunho Yang — [J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data](http://arxiv.org/abs/2608.26582v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving language models have recently emerged as a promising path toward superintelligence, with the advantage of reducing the cost of human supervision. While considerable progress has been made in verifiable domains, self-evolution in unverifiable domains remains substantially less explored. We propose Judge co-adaptation from Zero data (J-Zero), a unified Challenger--Solver--Judge co-evolution framework that supports self-improvement across both domains. The Challenger and Solver co-evo...
  </details>

- **2026-08-27** — Canzhi Chen, Zan Wang, Siqi Zhu et al. — [Embodied Scene Rearrangement Planning](http://arxiv.org/abs/2608.27371v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces Embodied Scene Rearrangement Planning (ESRP), a novel task requiring embodied agents to rearrange furniture in 3D scenes to match a target configuration using only egocentric observations and a top-down target layout. Unlike prior rearrangement tasks, ESRP precludes global state access and introduces mutual object occlusions, reflecting the practical constraints of real-world robotic deployment. These factors make aligning partial egocentric observations with the global tar...
  </details>

- **2026-08-27** — Navya Goli, Junzhe Liu, Zhenge Jia et al. — [AgentDV: Closed-Loop Agentic AI for Hardware Design Verification](http://arxiv.org/abs/2608.27148v1)
  <details><summary>📄 Abstract</summary>
  Register-transfer level (RTL) verification consumes a major part of modern system-on-chip (SoC) development effort. Yet, recent LLM-based verification-code generation often fails to produce runnable, design-consistent, and coverage-producing testbenches. We present AgentDV, a closed-loop agentic AI framework for automated RTL verification environment generation. AgentDV transforms single-shot LLM testbench generation into a tool-grounded verification pipeline by combining LLM-guided analysis, te...
  </details>

- **2026-08-27** — Yaxiao Liu, Pengbo Liu, Yiwen Liu et al. — [A Contract-Centered Architecture for Scalable and Manageable Agentic Runtimes](http://arxiv.org/abs/2608.27086v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI deployment is a coordination problem across business units, application and AI teams, testing, platform engineering, infrastructure, security, operations, and data governance. Use-case benchmarks show whether one agent completes one task, but not how changing capabilities, models, runtime mechanisms, capacity, and enterprise data should be owned, changed, admitted, or evidenced together.   We present four responsibility objects as shared organizational contracts: Skill (reusable, v...
  </details>

- **2026-08-27** — Abdullah Karasan — [Representation Measurements Under Function-Preserving Reparameterizations](http://arxiv.org/abs/2608.27020v1)
  <details><summary>📄 Abstract</summary>
  Hidden coordinates are not uniquely determined by a language model's input--output function, so representation-derived measurements should be invariant to function-preserving changes of basis. This study shows that column-permutation parallel analysis violates function-preserving reparameterization invariance because its reference distribution and selected component count can change while the model function and observed covariance spectrum remain fixed. More generally, a data-internal reference ...
  </details>

- **2026-08-27** — Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre — [KinyaEmbed: Contrastive Sentence Embeddings for Kinyarwanda via Multi-Stage Curriculum Training](http://arxiv.org/abs/2608.26941v1)
  <details><summary>📄 Abstract</summary>
  We present KinyaEmbed, the first dedicated sentence embedding model for Kinyarwanda, a morphologically rich Bantu language spoken by over 12 million people in Rwanda. Existing multilingual embedding models such as LaBSE, mE5-large, and OpenAI text-embedding-3-large perform poorly on Kinyarwanda due to severe under-representation in their pre-training corpora. KinyaEmbed is built on KinyaBERT-large and trained via a four-stage curriculum using MultipleNegativesRankingLoss (MNRL): Stage 1 leverage...
  </details>

- **2026-08-27** — Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib et al. — [AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations](http://arxiv.org/abs/2608.26921v1)
  <details><summary>📄 Abstract</summary>
  We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions -- Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous attachmen...
  </details>

- **2026-08-27** — Biao Yin, Abderrahmane Kasmi, Nadir Farhi — [Reinforcement Learning-Based Control of CAV Platoon Joining Maneuvers in Mixed Traffic](http://arxiv.org/abs/2608.26860v1)
  <details><summary>📄 Abstract</summary>
  Connected and automated vehicle (CAV) platooning offers a promising approach to improving road safety and traffic capacity. However, platoon control in real-world traffic is challenging due to uncertainty and heterogeneous driving behaviors. Reinforcement learning (RL) has strong potential for addressing such control problems, but its practical deployment raises challenges related to safety and learning efficiency. This paper proposes a generic modeling and simulation framework for investigating...
  </details>

- **2026-08-27** — Ji Soo Lee, Jinyoung Park, Seohyun Lee et al. — [Reason in the Words You Speak: Idiolectal Paraphrasing Off-Policy Traces for Reasoning Distillation in VideoLLMs](http://arxiv.org/abs/2608.26684v1)
  <details><summary>📄 Abstract</summary>
  Recent large language models achieve strong performance on complex reasoning tasks, where reinforcement learning with Group Relative Policy Optimization (GRPO) has emerged as a leading paradigm for optimizing models on self-generated trajectories. However, the on-policy nature of GRPO bounds the model to the reasoning skills it can already produce, restricting to learn more advanced capabilities. Prior works inject privileged reasoning traces from a stronger teacher policy to guide training, yet...
  </details>

- **2026-08-27** — Pei Yu Chang, Qadeer Ahmed — [Barrier Function Conformal Safety Clearance Certification with CVaR for Driving Trajectory Selection](http://arxiv.org/abs/2608.26533v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving motion planners generate and select candidate trajectories while accounting for interactions with surrounding agents. However, these evaluations do not certify the actual safety clearance of the selected trajectory. The framework evaluates the trajectory selected by ant planners and calibrates the gap between its plan time margin and realized safety clearance. A differentiable separating axis barrier margin deterministically lower bounds exact signed oriented-bounding-box (OBB...
  </details>

- **2026-08-27** — Lois Curfman McInnes, Dorian Arnold, Prasanna Balaprakash et al. — [Report of the 2026 Workshop on Next-Generation Ecosystems for Scientific Computing: Harnessing Community, Software, and AI for Cross-Disciplinary Team Science](http://arxiv.org/abs/2608.26519v1)
  <details><summary>📄 Abstract</summary>
  Scientific computing is undergoing rapid transformation as advances in artificial intelligence, heterogeneous computing, automation, and data-intensive research reshape not only computational tools but also the institutions, workforce models, and collaborative practices that support scientific discovery. This report synthesizes insights from the 2026 Workshop on Next-Generation Ecosystems for Scientific Computing, the second in a three-year series focused on strengthening scientific computing ec...
  </details>

- **2026-08-27** — Huanhuan Ma, Henry Peng Zou, Chengze Li et al. — [Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update](http://arxiv.org/abs/2608.26511v1)
  <details><summary>📄 Abstract</summary>
  Large language models often exhibit sycophancy, revising their answers to align with users when users push back. Such answer flips, however, can arise from different causes. One possibility is that the model simply aligns with the user's feedback in order to satisfy them. Another is that the feedback genuinely contains useful evidence, prompting the model to update its answer in a rational way. We distinguish them as Unsupported-Yielding and Rational-Updating. Prior work focuses primarily on sup...
  </details>

- **2026-08-27** — Shuyi Fan, Boyuan Deng, Mengyu Xu et al. — [Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect: Evidence from a Pre-Registered LLM-Judge Audit](http://arxiv.org/abs/2608.27309v1)
  <details><summary>📄 Abstract</summary>
  Audits of LLM judges certify a bias by contrasting matched conditions, and the strongest designs difference twice: a within-item contrast between two candidate responses, differenced again across a manipulated attribute, read off a bounded rating scale. We show that this endpoint is not identified on the scale that reports it. Each term of the double difference is censored by its own share, so the observed statistic confounds differential preference with differential attenuation: a severity shif...
  </details>

- **2026-08-27** — Haofeng Sun, Jiangbo Pei, Fei Kang et al. — [Riemann-1.0: An Embodied World Action Model for Physical AI](http://arxiv.org/abs/2608.27033v1)
  <details><summary>📄 Abstract</summary>
  We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence. Riemann-1.0 jointly models multi-view visual observations, robot states, and embodiment-specific actions within a unified causal autoregressive sequence, representing robot actions and world evolution as causal state transitions. Unlike existing WAMs based on joint generation, video-first prediction, or decoupled modeling paradigms, Riemann-1.0 unifies online robot policy execution and action-co...
  </details>

- **2026-08-27** — Zihang Wang, Jianming Hu, Shang Su et al. — [MeshPriorDiT: Hierarchical Modeling for Action-Conditioned Cloth Dynamics](http://arxiv.org/abs/2608.26766v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned cloth dynamics prediction requires both locally plausible deformation and long-range coordination. Existing approaches largely follow two paradigms. Mesh-based GNNs capture local physical responses through material connectivity. However, their finite message-passing range limits coordination between topologically distant regions, while autoregressive rollouts tend to accumulate prediction errors. Transformer-based dynamics models capture long-range interactions through global ...
  </details>

- **2026-08-27** — Hiroki Sawada, Shunichi Kasahara — [PredVLA: A Sub-Million-Parameter Predictive-Coding Policy for Robot Manipulation](http://arxiv.org/abs/2608.26673v1)
  <details><summary>📄 Abstract</summary>
  Large pretrained vision-language-action models dominate modern robot-manipulation benchmarks, but it remains unclear how much model scale is necessary for strong language-conditioned control, or whether fundamentally different control architectures can remain competitive at much smaller parameter budgets. We present PredVLA, a language-conditioned predictive-coding policy with only 0.68 million trainable network parameters and no robot-data pretraining, whose hierarchical generative recurrent dy...
  </details>

- **2026-08-27** — Chanho Park, Daehyeon Choi, Jihyun Lee et al. — [Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual Information](http://arxiv.org/abs/2608.27417v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can locate an image region referred to by a text prompt and route the corresponding visual evidence to the output, yet the internal mechanism behind this behavior is not understood. Inspired by retrieval heads in large language models, we ask whether VLMs contain an analogous mechanism for visual retrieval. We answer affirmatively by introducing Visual Retrieval Heads (VRHs), a small subset of attention heads (about 1.7-2.6%) that are causally responsible for ground...
  </details>

- **2026-08-27** — Peiling Yi — [RCMN: Understanding Misleadingness in Influential Public Discourse](http://arxiv.org/abs/2608.27358v1)
  <details><summary>📄 Abstract</summary>
  Influential public discourse shapes public beliefs and can also mislead, not only through what is stated, but also through how information is framed, omitted, contextualised, and communicated. Yet less research has focused on how such misleadingness arises and shapes the interpretations formed by readers. To address this gap, we introduce Reader-Centric Misleadingness Understanding (RCMN), a framework that operationalises misleadingness through five dimensions: misleading mechanism, likely reade...
  </details>

- **2026-08-27** — Kai Sun — [Why Three Phases? A Historical and Engineering Reassessment of Phase Order in AC Power Transmission](http://arxiv.org/abs/2608.27325v1)
  <details><summary>📄 Abstract</summary>
  Three-phase alternating current is so deeply embedded in modern electric-power infrastructure that its phase order is often treated as self-evident. Historically, however, 1-phase and true 2-phase systems were commercially important, while commercial 6-phase transmission was later demonstrated. This paper reassesses why 3 phases became the dominant architecture for bulk AC transmission. A general balanced \(m\)-phase formulation is used to show that constant aggregate instantaneous power is not ...
  </details>

- **2026-08-27** — Mayanka Chandrashekar, Xi Zhang, Ethan Seefried et al. — [Decoupled I/O-Dominant Pipelines for Large-Scale Whole-Slide Image Embedding Extraction](http://arxiv.org/abs/2608.27278v1)
  <details><summary>📄 Abstract</summary>
  Whole-slide images (WSIs) are central to computational pathology but are prohibitively large, making patch-based processing the practical unit for foundation model inference. At scale, however, generating and handling massive numbers of patches on quickly introduces significant I/O and orchestration overhead, often dominating end-to-end performance. We present a decoupled, I/O-aware pipeline for large-scale WSI embedding extraction that decomposes the workflow into three stages: (1) patch genera...
  </details>

- **2026-08-27** — Maitrey Gramopadhye, Prakash Baskaran, Xiao Liu et al. — [STEP: State-Aware Task Estimation and Planning with Multi-Modal LLMs for Human-Robot Collaboration](http://arxiv.org/abs/2608.27225v1)
  <details><summary>📄 Abstract</summary>
  Effective human-robot collaboration in industrial settings requires robots to understand human intentions and assist with task planning, reducing workload. Recent works have explored the use of Multi-modal Large Language Models (MM-LLMs) for task planning in such data-scarce scenarios, leveraging in-context learning to interpret user actions and generate long-horizon action plans in natural language. However, MM-LLMs inherently lack an understanding of system states and do not track state transi...
  </details>

- **2026-08-27** — Hiuyi Cheng, Nuo Xu, Yuyi Zhang et al. — [Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition](http://arxiv.org/abs/2608.27169v1)
  <details><summary>📄 Abstract</summary>
  Ancient Chinese artifact text recognition is fundamental to heritage digitization, and benchmarks for ancient texts are essential for evaluating current model capabilities. However, existing benchmarks suffer from ''fragmentation'', manifested in limited temporal coverage, limited medium diversity, and incomplete script types. Therefore, we present Ancient-Bench, a comprehensive benchmark of 2,700 images for ancient Chinese artifact text recognition, featuring three dimensions: Multi-millennial ...
  </details>

- **2026-08-27** — Wendong Li, Jochen Garcke — [Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation](http://arxiv.org/abs/2608.27158v1)
  <details><summary>📄 Abstract</summary>
  Robot crowd navigation requires safe and efficient decision-making under dense, dynamic, and multimodal human--robot interactions. Existing reinforcement-learning methods typically output a single reactive action at each timestep, which limits their ability to represent diverse short-term avoidance strategies. We propose Planning Diffusion Policy Optimization (PDPO), an offline-to-online reinforcement-learning framework that uses a diffusion policy to generate short-horizon action chunks for cro...
  </details>

- **2026-08-27** — Wasamon Jantai, Nathakhun Wiroonsri — [An approximate zero bias transformation for random sums: Applications to sampling with outliers, auto insurance, and generative AI](http://arxiv.org/abs/2608.27143v1)
  <details><summary>📄 Abstract</summary>
  We develop $L^1$ bounds for the difference between a test function of a random sum and a standard normal random variable, where the summands are assumed to be independent but not necessarily identically distributed. The bounds are obtained through a new version of the approximate zero bias transformation specifically developed for random sums. Although the identical distribution assumption is relaxed, the bounds are of order $1/\sqrt{n}$, matching the order of existing bounds in the literature u...
  </details>

- **2026-08-27** — Basel Mousi, Fahim Dalvi, Shammur Chowdhury et al. — [Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models](http://arxiv.org/abs/2608.27135v1)
  <details><summary>📄 Abstract</summary>
  Multimodal foundation models are increasingly used in speech-first assistants that must interpret spoken queries and produce visually grounded decisions. Yet it remains unclear whether semantically equivalent queries yield consistent judgments across modality (text vs. speech) and language (English vs. Arabic). We introduce a speech-augmented visually grounded contrastive triplet benchmark spanning 10,150 culturally grounded images from 18 MENA countries, where each image is paired with one supp...
  </details>

- **2026-08-27** — Marco Rovera, Sergiu Burlacu, Dominique Cappelletti et al. — [Research Design Tracking and Assessment for the Social Sciences](http://arxiv.org/abs/2608.27049v1)
  <details><summary>📄 Abstract</summary>
  Reliable assessment of causal research designs in the social sciences is critical for evidence-based policy-making, yet has so far relied entirely on manual expert analysis. We introduce Automated Research Design Tracking and Assessment (ARDTrA), a task that involves detecting the research design used in a paper and assessing the quality of its application. We create an expert-annotated dataset of papers covering six families of counterfactual research designs and evaluate the task using a multi...
  </details>

- **2026-08-27** — Ivan Kruzhilov — [Disentangling Optimization Scale from Preference Scale in DPO](http://arxiv.org/abs/2608.27032v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) is a widely used objective for aligning language models from preference data, with the coefficient $β$ commonly interpreted as controlling the KL constraint to a reference policy. We show that $β$ entangles two distinct roles: it governs the effective inverse preference-noise scale and simultaneously rescales the optimization dynamics, coupling this scale with the effective step size. As a consequence, at a fixed learning rate the achieved policy deviation is...
  </details>

- **2026-08-27** — Zijian Kan, Wei Wang, Long Luo et al. — [RubricRM: Generative Reward Modeling via Dynamic Rubrics for Image Generation and Editing](http://arxiv.org/abs/2608.26956v1)
  <details><summary>📄 Abstract</summary>
  Reward models play an essential role in aligning visual generative models, yet most existing visual reward models use a single scalar score or rely on fixed criteria that cannot adapt to different instructions. This limits both interpretability and task sensitivity, especially for text-to-image generation and instruction-based image editing, where different inputs require different evaluation dimensions. We propose RubricRM, a pairwise generative reward modeling framework that first produces an ...
  </details>

- **2026-08-27** — Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann et al. — [KISS-GS: 3D Gaussian Splatting Compression Kept Simple](http://arxiv.org/abs/2608.26948v1)
  <details><summary>📄 Abstract</summary>
  Scene reconstruction with 3D Gaussian Splatting (3DGS) has become common, however deployment remains painful as the uncompressed file sizes can be massive. Current 3DGS compression systems combine multiple strategies for file size reduction, which can obscure where gains come from and limit component reuse across training pipelines. To make the gains more transparent, we propose KISS-GS, a modular compression pipeline named after the principle of keeping things simple, designed to decouple compr...
  </details>

- **2026-08-27** — Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre — [TabuLM: Morphology-Aware Tabular Pre-training for Low-Resource Languages](http://arxiv.org/abs/2608.26923v1)
  <details><summary>📄 Abstract</summary>
  We present TabuLM, the first language model pre-trained on Kinyarwanda tabular data. Kinyarwanda is a morphologically rich Bantu language spoken by over 12 million people in Rwanda, yet lacks any dedicated tabular representation learning resource. TabuLM extends KinyaBERT-large, a two-tier morphological transformer, with additive row, column, and cell-type embeddings and a learned table-structure attention bias that sharpens same-row and same-column attention. Pre-training uses two new objective...
  </details>

- **2026-08-27** — Sai Yashwant, Shruti Bansal, Anurag Dubey et al. — [Counterfactual Bias Testing for Application Tracking System](http://arxiv.org/abs/2608.26899v1)
  <details><summary>📄 Abstract</summary>
  Automated candidate-job matching systems are increasingly classified as high-risk AI under emerging regulation, yet auditing them for demographic bias is expensive: classical correspondence-audit studies require hand-crafted resumes and manual submission, which does not scale to fast pipeline retraining cycles. This paper presents a general, reusable methodology that (1) uses task-specialized LLM agents to synthesize identity-neutral base resumes and inject controlled demographic treatments acro...
  </details>

- **2026-08-27** — Alexandru-Iulius Jerpelea — [Planting a Latent Variable in Natural-Looking Text: a More Realistic Test of Belief States in LLMs and Their Link to Concept Geometry](http://arxiv.org/abs/2608.26887v1)
  <details><summary>📄 Abstract</summary>
  LLMs are thought to track "belief states," i.e., running probability distributions over the latent variables that govern language (Shai et al., 2024; Sarfati et al., 2026), but so far this has only been comprehensively demonstrated on toy synthetic data and in a few isolated case studies. It has also never been empirically connected to the geometry of LLM features (the concepts interpretability finds in model activations). In this work, we plant a controllable latent variable inside natural-look...
  </details>

- **2026-08-27** — Gustavo Castro do Amaral — [Quantum Interconnects Part I: Strategic Quantum Network Formation](http://arxiv.org/abs/2608.26886v1)
  <details><summary>📄 Abstract</summary>
  The realization of large-scale quantum networks requires more than advances in quantum repeaters, memories, and processors, it requires a framework explaining how heterogeneous quantum technologies evolve from isolated deployments into interconnected infrastructures. While the classical Internet evolved under strong utility incentives associated with resource sharing and communication demands, quantum networking currently lacks dominant applications capable of generating comparable incentives. A...
  </details>

- **2026-08-27** — Zihao Cheng, Yingyu Shan, Hongru Wang et al. — [Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory](http://arxiv.org/abs/2608.26807v1)
  <details><summary>📄 Abstract</summary>
  Travel planning agents assist users in generating personalized travel plans by modeling their individual preferences. Existing agents either rely on explicit user instructions or engage in multi-turn clarification to elicit user preferences. However, both approaches overlook the rich behavioral signals latent in users' past behaviors, which implicitly encode their preferences. This over-reliance on active user input increases interaction burden and limits plan personalization. To bridge this gap...
  </details>

- **2026-08-27** — Ming Ji, Holger F. Hofmann — [Uncertainty limits for post-selected metrology](http://arxiv.org/abs/2608.26781v1)
  <details><summary>📄 Abstract</summary>
  For unitary transformations, the quantum Fisher information (QFI) of a pure state is given by the uncertainty of the generator in that state. In post-selected metrology, the QFI is given by a modified expression describing conditional quantum statistics of the generator. Here, we show that the conditional generator uncertainties defined by post-selected QFI correspond to Ozawa-Hall uncertainties known from the theoretical analysis of quantum measurements. The post-selected measurement outcome up...
  </details>

- **2026-08-27** — Haiteng Wang, Weihao Li, Jing Zhang et al. — [AI Control Scientist: LLM-driven Agentic System for Automated Control Design](http://arxiv.org/abs/2608.26780v1)
  <details><summary>📄 Abstract</summary>
  Control system design is critical for modern industry, such as chemical process temperature regulation and aero-engine control. However,traditional control design workflows rely heavily on expert knowledge and extensive manual parameter tuning, resulting in limited efficiency and scalability. To this end, this paper proposes AI Control Scientist (AICS), the first large language model (LLM)-driven agent capable of automatically generating optimized controller from language design requirements. Sp...
  </details>

- **2026-08-27** — Mingquan Liu, Jiangyu Chen, Hanqun Cao et al. — [AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design](http://arxiv.org/abs/2608.26747v1)
  <details><summary>📄 Abstract</summary>
  Scientific LLM agents have shown promise in literature reasoning, tool use, and experiment planning, but it remains unclear whether they can autonomously improve large, tightly coupled scientific machine-learning systems through executable code changes and computationally expensive validation. We study this question in protein folding, where progress requires coordinated architectural modifications, multi-objective evaluation, and domain-aware interpretation. We present AgentFold, a multi-agent ...
  </details>

- **2026-08-27** — Yi-Lin Ye, Jindu Wang, Hiu Tung Wong et al. — [RegulAR: Graph-Grounded Error Recognition and Assistance for Procedural Tasks in AR](http://arxiv.org/abs/2608.26715v1)
  <details><summary>📄 Abstract</summary>
  Errors are inevitable in procedural tasks, yet most AR guidance systems focus on step-by-step instruction delivery rather than helping users recognize and recover from mistakes. We present RegulAR, an AR task assistant for procedural error recognition and recovery. RegulAR models task instructions as a hierarchical dependency graph and combines this structure with a Multimodal Large Language Model (MLLM) to interpret egocentric observations during execution. This enables RegulAR to track progres...
  </details>

- **2026-08-27** — Xuanwei Hu, Haoyu Dong, Kejun Wu et al. — [AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability](http://arxiv.org/abs/2608.26713v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Multimodal Large Language Models (MLLMs) have extended Image Aesthetic Assessment (IAA) beyond scalar scores toward interpretable critique and guidance. Yet existing benchmarks mainly assess intrinsic visual quality or fixed domain criteria, leaving open whether an appealing image is appropriate for a specific purpose, audience, cultural setting, or domain convention. We introduce AesCanvas, a unified suite with two complementary components: CritiqueCanvas with 519,136 instruc...
  </details>

- **2026-08-27** — Junjie Xiong, Shawheen Ghezavat, Aum Hirpara — [Towards Expert Financial QA via Self-Improving RAG](http://arxiv.org/abs/2608.26706v1)
  <details><summary>📄 Abstract</summary>
  Expert-level financial question answering requires both grounded verification to catch numeric hallucinations and audit trails for regulatory compliance, attributes that standard single-pass RAG systems lack. We take a step toward this goal with Self-Improving RAG, a framework that decomposes document QA into three specialized agents (Retrieval, Reasoning, and Judge) coordinated by an orchestrator with feedback-driven self-correction. When the Judge Agent scores an answer below a dynamic thresho...
  </details>

- **2026-08-27** — Mengfan Li, Zesheng Wei, Xuanhua Shi et al. — [Do LLMs Understand Personality? Rethinking Persona Fidelity Evaluation through Structured Behavioral Inference](http://arxiv.org/abs/2608.26674v1)
  <details><summary>📄 Abstract</summary>
  As large language models are increasingly deployed to simulate diverse human characters, ensuring persona fidelity, defined as the extent to which an agent's behavior consistently reflects the psychological and stylistic characteristics of a target persona, has become a critical requirement. However, existing evaluation paradigms primarily rely on either holistic LLM-based judges, which are prone to "holistic appraisal hallucination'', or static psychometric inventories, which fail to capture th...
  </details>

- **2026-08-27** — Yoonseo Kim, Seongmin Lee, Joongheon Kim et al. — [hoBIT: A Profile-Aware Retrieval-Augmented Chatbot for University Academic Advising](http://arxiv.org/abs/2608.26604v1)
  <details><summary>📄 Abstract</summary>
  In university academic advising, identical questions can require different answers depending on a student's department, admission cohort, and degree program, causing profile-blind retrievers to surface plausible but inapplicable evidence. We present proFILL, a method for transforming hoBIT, our college's current rule-based advising chatbot, into a profile-aware retrieval-augmented generation (RAG) system. Rather than requiring a complete user profile upfront, proFILL progressively acquires only ...
  </details>

- **2026-08-27** — Hiep V. Dang, Antonios Mamalakis — [SimCast-S2S: An Efficient Generative Model for Subseasonal Precipitation Forecasting via Transfer Learning from Climate Simulations](http://arxiv.org/abs/2608.26594v1)
  <details><summary>📄 Abstract</summary>
  Subseasonal-to-seasonal (S2S) precipitation forecasting has substantial financial and societal impact, yet remains challenging because of weak predictive signals, high associated uncertainty, and the computational cost of operational systems, which constrains simulation fidelity. We introduce SimCast-S2S, a generative latent-diffusion framework for probabilistic S2S precipitation forecasting that addresses three major bottlenecks in data-driven prediction. First, because S2S prediction requires ...
  </details>

- **2026-08-26** — Wen Huang, Yunfei Chu, Meng Gao et al. — [AudioSpan: Spanning the Duration and Depth of Audio Comprehension](http://arxiv.org/abs/2608.26431v1)
  <details><summary>📄 Abstract</summary>
  General audio comprehension now covers speech, sound, and music over durations from seconds to hours, driven by large audio-language models (LALMs) that are increasingly omni-modal. Yet the benchmarks that test them still rely on clips of seconds, where scores saturate and models converge; recent long-form efforts extend duration but evaluate long audio much as short clips are. We introduce AudioSpan, a benchmark that spans both duration and depth: it pairs audio from 10 minutes to over 2 hours ...
  </details>

- **2026-08-26** — Miseon Yu, Jaehoon Choi, Younghan Lee et al. — [MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration](http://arxiv.org/abs/2608.25457v2)
  <details><summary>📄 Abstract</summary>
  Despite their strong ability to generate code, large language models often fail to produce secure code, as their outputs frequently contain security vulnerabilities. Secure code generation is inherently challenging because it requires solving a multi-objective problem: functional correctness and security. Existing approaches address this challenge by injecting external security knowledge or by using agentic feedback and iterative refinement. However, guideline retrieval often leaves the generato...
  </details>

- **2026-08-26** — Zishan Shao, Lixun Zhang, Kangning Cui et al. — [LowRankArena: A Standardized Evaluation Platform for SVD-Based LLM Compression](http://arxiv.org/abs/2608.26389v1)
  <details><summary>📄 Abstract</summary>
  SVD-based low-rank compression has become a fast-growing direction for reducing the memory and computational cost of large language models (LLMs). However, meaningful comparison across existing studies remains difficult as prior evaluations use varied benchmarks, inconsistent ratios, and diverse setups, often failing to isolate low-rank effects from auxiliary techniques. As a result, it remains unclear whether reported gains reflect method-level improvements or differences in evaluation protocol...
  </details>

- **2026-08-26** — Luca L. Weishaupt, Simone de Brot, Javier Asin et al. — [VIPER: An Expert-Curated Benchmark for Vision-Language Models in Veterinary Pathology](http://arxiv.org/abs/2608.26382v1)
  <details><summary>📄 Abstract</summary>
  Pathology vision-language models are advancing rapidly, yet existing benchmarks remain focused on human tissue, particularly oncology, leaving non-human pathology largely unaddressed. This gap is especially important in toxicologic pathology, where microscopic tissue examination of laboratory animals is a core component of preclinical drug safety assessment. To address it, we introduce VIPER, the first expert-curated benchmark for vision-language model evaluation in toxicologic pathology. VIPER ...
  </details>

- **2026-08-26** — Jianping Philip Wang — [A Coherent Framework for Semicontinuous Data Through Distributional Regularization, Censoring, and Compounded Occurrence-Severity Modeling](http://arxiv.org/abs/2608.26286v1)
  <details><summary>📄 Abstract</summary>
  Semicontinuous outcomes frequently present severe distributional mismatches characterized by structural zeros, highly skewed positive observations, and extreme right tails. In practice, transformations, capping, truncation, and censoring are commonly employed to reduce the influence of extreme observations. However, estimation procedures often continue to treat the modified responses as exact observations, creating a mismatch between the information contained in the data and the likelihood being...
  </details>

- **2026-08-26** — Ross Williams, Niyousha Hosseinichimeh — [Prompt Sensitivity of Generative Agents: Evidence from an Epidemic Model](http://arxiv.org/abs/2608.26221v1)
  <details><summary>📄 Abstract</summary>
  As generative AI gains traction, researchers are investigating its potential to serve as proxies for humans. From undergoing cognitive psychology experiments to experiencing an epidemic, generative agents, agents powered by generative AI models, produce realistic human behavior when prompted. This study explores the sensitivity of these generative agents' behavior to prompt modifications and varied persona names of the agents. To assess this sensitivity, we use a generative agent epidemic model,...
  </details>

- **2026-08-26** — Zheyuan Liu, Weiliang Zhao, Xiangchi Yuan et al. — [Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives](http://arxiv.org/abs/2608.26372v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as autonomous agents serving users on behalf of companies, placing them in settings where user and deployer interests can conflict. When an agent knows that a user is owed something its deployer would prefer to deny, does it remain honest? Answering this is difficult because false statements can reflect either ignorance or hallucination rather than deception. To address this challenge, we introduce KnownLieBench , a knowledge-verified benchmark tha...
  </details>

- **2026-08-26** — Parker Ziegler, David Minh-Duy Cao, Justin Lubin et al. — [Direct Manipulation and Natural Language Programming, Together at Last?](http://arxiv.org/abs/2608.26359v1)
  <details><summary>📄 Abstract</summary>
  Decades of programming languages research has contributed novel approaches to program editing that go beyond modifying text, including direct manipulation programming, structure editing, and automated refactoring tools. However, the rapid growth of natural language programming largely reinforces a view of programs as text and program editing as (unstructured) text transformation. How can we develop unified programming systems that bridge the gap between these approaches, supporting multiple edit...
  </details>

- **2026-08-26** — Rana Danesh, Pari Qarehdaghi, Farrokh Janabi-Sharifi — [Constraint-Aware Physics-Informed Neural Networks for Static Shape Estimation of Co-Manipulative Continuum Robots](http://arxiv.org/abs/2608.26273v1)
  <details><summary>📄 Abstract</summary>
  Static shape estimation of co-manipulative continuum robots (CCRs) is challenging because the continuum arms and manipulated flexible object form a closed chain that must satisfy both static equilibrium and geometric loop-closure constraints. This paper presents a constraint-aware physics-informed neural network (PINN) for static shape estimation of a tendon-driven CCR modeled using the geometric variable strain formulation. The proposed method incorporates a projected static equilibrium residua...
  </details>

- **2026-08-26** — Jiaming Zhou, Qihang Zhang, Gangwei Xu et al. — [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](http://arxiv.org/abs/2608.26103v2)
  <details><summary>📄 Abstract</summary>
  Zero-shot cross-task generalization, where a policy must execute manipulation tasks never seen during training, remains a central challenge in robot learning. In large language models, a novel task can be performed simply by specifying it in the context, without any parameter update. This form of in-context learning (ICL) turns generalization into a problem of task specification. To achieve cross-task generalization, we bring this paradigm to robotic manipulation, and argue that the natural task...
  </details>

- **2026-08-26** — Hadi Hosseini, Shraddha Pathak, Lirong Xia et al. — [Simultaneous Envy and Equitability Guarantees](http://arxiv.org/abs/2608.26410v1)
  <details><summary>📄 Abstract</summary>
  Recent work in fair division has focused on either simultaneously satisfying closely related fairness notions or achieving a single notion across the ex-ante and ex-post worlds. We study the compatibility of two fundamentally different fairness notions: envy-freeness and equitability. For indivisible goods-only and chores-only settings, we study the existence and complexity of simultaneously satisfying their relaxations, revealing sharp contrasts between the two settings. We show that EF1+EQ1 ma...
  </details>

- **2026-08-26** — Ruichen Qi, Xinting Jiang, Ema Dimitrova et al. — [SILK: Closing the Time-of-Check-to-Time-of-Use Gap in RoT-Protected AI Systems](http://arxiv.org/abs/2608.26402v1)
  <details><summary>📄 Abstract</summary>
  Root-of-trust (RoT) authentication verifies a DNN model at load time, but weights may subsequently traverse DRAM, DMA, interconnect, and prefetch paths before reaching the compute engine. Post-verification tampering along this path can therefore alter the weights actually consumed while leaving the authenticated model image unchanged, creating a time-of-check-to-time-of-use (TOCTOU) integrity gap.   We present SILK (Streaming Inline Lightweight Keying), an in-place integrity mechanism that verif...
  </details>

- **2026-08-26** — JaeHyeong Chang, Chengzhe Sun, Siwei Lyu — [Decay-Region Group Delay as a Forensic Cue for AI-Generated Impulsive Sounds](http://arxiv.org/abs/2608.26346v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether AI-generated impulsive sounds can be distinguished from real ones through group delay analysis. Our central finding is that AI-generated impulsive sounds show near-identical onset-region group-delay distributions but exhibit measurably different group-delay behavior in the late decay region: decay-region KL divergence reaches $0.322$ compared to near-zero onset divergence ($0.022$). Cross-band GD variability achieves single-feature AUC~=~0.720, and a Random Forest (RF) ove...
  </details>

- **2026-08-26** — Avia Asael, Nave Frost, Amir Gilad et al. — [Realistic Counterfactual Explanations via Denial Constraints](http://arxiv.org/abs/2608.26335v1)
  <details><summary>📄 Abstract</summary>
  In the realm of Explainable AI, classification results are often explained via counterfactuals (CFs for short), which are (ideally small) perturbations to an instance that lead to a change of classification label. Such CFs may serve as explanations for the prediction, pinpointing the features that were important. Existing explainability solutions typically aim at minimizing the distance of CFs from the original instance so that they are specific to it, and/or maximizing the diversity of CFs to c...
  </details>

- **2026-08-26** — Christos Petridis, Konstantinos Pelechrinis, Zoran Obradovic — [How Unlikely Is "Unlikely"? Assessing Verbal Probability Perception Across Large Language Models](http://arxiv.org/abs/2608.26327v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly produce and interpret verbal probability expressions, yet whether these expressions carry consistent meaning across models (or match human perceptions of uncertainty) remains unknown. We present a systematic cross-model evaluation using a word-to-number mapping task grounded in established human benchmarks. Eleven uncertainty expressions were presented to 19 models under two conditions, forced single-number response and explanation elicitation, alongside a nove...
  </details>

- **2026-08-26** — Subir Kumar Parida, Rajbabu Velmurugan, Ketan Kotwal et al. — [Learning Late, Guiding Early: Timestep-Decoupled Semantic Guidance for Fair Face Generation](http://arxiv.org/abs/2608.25862v2)
  <details><summary>📄 Abstract</summary>
  Demographic imbalance in synthetic face generation can propagate to downstream face recognition systems, making fairness an important consideration when diffusion models are used for data generation. Existing fairness-aware generation approaches often require model retraining, architectural modifications, or repeated guidance throughout the reverse diffusion process. In this work, we introduce Semantic Boundary Predictor (SBP), an inference-time framework that performs demographic guidance throu...
  </details>

- **2026-08-26** — Jihao Zhu, Zhiwei Yang, Wenxiao Zhang et al. — [ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives](http://arxiv.org/abs/2608.25531v2)
  <details><summary>📄 Abstract</summary>
  Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models are a practical alternative, but directly feeding them an entire long context remains costly, hard to inspect, and prone to missing sparse evidence. We present ClueWeaver, an evidence-aware dual-agent framework for long-narrative quest...
  </details>

- **2026-08-26** — Chengsong You, Junwei Zhou, Xiaoyu Cao et al. — [DocPC: Document-Level Visual Retrieval via Representative Page Composition](http://arxiv.org/abs/2608.25434v2)
  <details><summary>📄 Abstract</summary>
  Visual document retrieval has advanced by encoding page screenshots with vision-language models, bypassing OCR pipelines. However, existing methods remain page-centric, misaligned with real-world scenarios requiring complete document retrieval. A naive page-then-document aggregation suffers from linear indexing cost and degraded retrieval when relevance spans multiple pages. We propose DocPC, a document-level visual retrieval framework based on Representative Page Composition: selecting represen...
  </details>

- **2026-08-26** — Xiao Xiao, Jiashu He, Shiyang Zhang et al. — [Learning Interpretable Tumor Microenvironment Representations by Fitting Pan-Cancer Cell State-Niche Correlation](http://arxiv.org/abs/2608.26208v1)
  <details><summary>📄 Abstract</summary>
  In the tumor microenvironment, cell's state is influenced by cell-cell interactions (CCIs) with neighboring cells in its niches. Identifying dysregulated CCIs that are associated with pathogenic process pinpoints targets for drug discovery. Imaging-based spatial transcriptomics and single-cell RNA sequencing provide, respectively, single-cell spatial information and transcriptome-wide measurements needed to study CCIs, but neither modality provides both. Existing spatial transcriptomics foundati...
  </details>

- **2026-08-26** — Ziqing Qian, Jiaying Lei, Yifang Wang et al. — [HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning](http://arxiv.org/abs/2608.25770v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have enabled AI scientist systems to automate scientific discovery, yet existing approaches most rely on static prompting or fixed workflows and fail to accumulate experience for continual improvement. We propose HypoForge, an experience-guided multi-agent framework that learns reusable scientific skills for automated hypothesis generation and hypothesis testing. HypoForge is built on the observation that these two stages involve different supervision signals. For hy...
  </details>

- **2026-08-26** — Miseon Yu, Jaehoon Choi, Younghan Lee et al. — [MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration](http://arxiv.org/abs/2608.25457v1)
  <details><summary>📄 Abstract</summary>
  Despite their strong ability to generate code, large language models often fail to produce secure code, as their outputs frequently contain security vulnerabilities. Secure code generation is inherently challenging because it requires solving a multi-objective problem: functional correctness and security. Existing approaches address this challenge by injecting external security knowledge or by using agentic feedback and iterative refinement. However, guideline retrieval often leaves the generato...
  </details>

- **2026-08-26** — Dev Mehta, Lily Dukette, William Folan et al. — [LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing](http://arxiv.org/abs/2608.25321v1)
  <details><summary>📄 Abstract</summary>
  The move of LLM inference to edge AI accelerators introduces new physical vulnerabilities. During execution, model parameters and intermediate inference states are repeatedly loaded into and processed on the chip, making them suscep- tible to physical side-channel attacks. In this work, by deploying laser voltage imaging, we show that one can extract LLM assets during inference, namely embeddings, attention, and quantized MLP weights, activations, and other inference states, from localized memor...
  </details>

- **2026-08-26** — Ahmad Khan, Akram Bin Sediq, Sara Azadegi Naeini et al. — [Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role](http://arxiv.org/abs/2608.26093v1)
  <details><summary>📄 Abstract</summary>
  Designing machine learning algorithms for wireless resource management is labour-intensive: the architecture, the loss function and the training recipe are all specified by hand. We demonstrate that this design layer can be surrendered to an autonomous agent in its entirety. We adopt the autoresearch protocol, in which an AI coding agent edits a training script, runs a fixed-budget experiment, and retains or discards the change according to a single immutable metric. We grant the agent authority...
  </details>

- **2026-08-26** — Jiarui Yan, Weiwei Sun, Sijie Li et al. — [TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](http://arxiv.org/abs/2608.26086v1)
  <details><summary>📄 Abstract</summary>
  Large language models write correct code for isolated problems but remain far weaker at autonomous machine-learning development, where an agent must revise data pipelines, models, and validation over hours of feedback, and on most competitions still finishes below strong human competitors. Outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. We introduce TraceML, which pairs human and agent work on the ...
  </details>

- **2026-08-26** — Subhadeep Pal, Fiona Y. Wang, Markus J. Buehler — [SwarmWorld: Stigmergic technological evolution in societies of language-model agents](http://arxiv.org/abs/2608.26081v1)
  <details><summary>📄 Abstract</summary>
  Collective intelligence can emerge when individuals coordinate through a shared environment, allowing local actions to accumulate into durable social organization. Language-model agents offer a new substrate for this process, yet most multi-agent systems rely on direct conversation, predefined roles, or centralized workflows. It remains unclear whether decentralized agents can build functional technologies and outperform independent search. Here, initially homogeneous LLM agents in SwarmWorld se...
  </details>

- **2026-08-26** — Leonardo Duart, Tiago Fonseca, Thiago Chacón — [Fine-Tuning Whisper for Automatic Speech Recognition in Baniwa: A Preliminary Study](http://arxiv.org/abs/2608.26060v1)
  <details><summary>📄 Abstract</summary>
  Automatic Speech Recognition (ASR) technologies have achieved remarkable performance in recent years through the use of large multilingual foundation models. However, most advances remain concentrated on high-resource languages, while indigenous languages continue to suffer from a lack of speech resources and language technologies. This work presents a preliminary study on the adaptation of Whisper for Automatic Speech Recognition in Baniwa, an indigenous Arawakan language spoken in Brazil, Colo...
  </details>

- **2026-08-26** —  Xiaomi Embodied Intelligence Team, University of Macau,  : et al. — [One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](http://arxiv.org/abs/2608.26058v1)
  <details><summary>📄 Abstract</summary>
  Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spaces. Existing paradigms typically address this mismatch through explicit action retargeting, human-to-robot video synthesis, or dataset-specific adaptation branches, fundamentally hindering the joint learning of a unified policy. We introduce UCAG-P, a camera-centric unified action ...
  </details>

- **2026-08-26** — Sheng Liang, Yongyue Zhang, Nathanael Brian et al. — [AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](http://arxiv.org/abs/2608.26004v1)
  <details><summary>📄 Abstract</summary>
  Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions. To control latency, deployments routinely compress inputs, but this degrades task accuracy. Speculative decoding (SD) accelerates generation losslessly, yet it assumes the drafter and verifier share an identical context, preventing SD from resolving the accuracy-overhead trade-off. We propose AsymSpec, an asymmetric speculative decoding framework that breaks this ...
  </details>

- **2026-08-26** — Yueen Ma, Zenglin Xu, Irwin King — [4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](http://arxiv.org/abs/2608.25956v1)
  <details><summary>📄 Abstract</summary>
  Current world action models (WAMs) typically operate on 2D visual data. These models can achieve exceptional visual quality, but they lack explicit spatial structure for individual objects and repeatedly process redundant background content. Although point clouds can represent the world in 3D space, they can be difficult to align and accumulate across viewpoints. In this paper, we leverage an explicit 4D Gaussian Splatting (4DGS) representation that separately models dynamic objects and the stat...
  </details>

- **2026-08-26** — Yiwen Chen, Guosheng Lin, Chi Zhang — [Code World Model: Coding Agent as World Brain](http://arxiv.org/abs/2608.25927v1)
  <details><summary>📄 Abstract</summary>
  World models aim to simulate how complex environments evolve under actions and events, yet existing video-based world models primarily learn dynamics from visual observations, which reveal outcomes rather than the underlying knowledge, rules, and mechanisms governing world evolution. This makes it difficult to maintain persistent consequences and support coherent, open-ended evolution. We introduce Code World Model, a framework that separates world evolution from visual realization by combining ...
  </details>

- **2026-08-26** — Luca Bux, Thiago Rios, Ingo Scholtes et al. — [Do Vision-Language Models Agree on the Affective Qualities of Shape? A Cross-Model Audit for Generative Design Interfaces](http://arxiv.org/abs/2608.25876v1)
  <details><summary>📄 Abstract</summary>
  Generative design interfaces increasingly expose semantic controls that let users steer output with concepts such as "more elegant" or "more minimalist," typically encoded by a vision-language model (VLM). A practical question is whether state-of-the-art VLMs represent objects consistently in terms of the same concept. We audit 6 VLMs by ranking untextured 3D objects along Kansei adjective pairs, where Kansei describes affective impressions of product form, with each axis defined as the differen...
  </details>

- **2026-08-26** — Bobby Cheng, Adam Gaber, Zhengyuan Liu et al. — [Skill Issue: Are Skills Language-Invariant in LLMs?](http://arxiv.org/abs/2608.25832v1)
  <details><summary>📄 Abstract</summary>
  Large language models access knowledge inconsistently across languages, but to what extent do they differ in their skill sets when interacting with different languages? This work quantifies cross-lingual skill inconsistency orthogonally from knowledge and general benchmark performance. We do this via multilingual self-play: two instances of the same model compete in a text-based game, each interacting through a different language interface. Since the model, opponent, rules, state space, and avai...
  </details>

- **2026-08-26** — Sizhe Wang, Himashi Peiris, Zhaolin Chen — [Steer the Sampling, Not the Kernel Grid: Geometry-Guided Sampling Operator for Volumetric Segmentation](http://arxiv.org/abs/2608.25819v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D segmentation is central to quantitative lesion assessment and anatomy mapping for clinical planning and follow-up. Thin, elongated, and fine anatomical/pathological structures (e.g., vessels) are a particularly challenging case: a one-voxel boundary error can disconnect a branch and change clinically relevant topology. In encoder-decoder networks (e.g., U-Net), repeated downsampling and fixed-grid convolution blur or alias fine structures and weaken orientation cues, so early mistake...
  </details>

- **2026-08-26** — Jessica Hösl, Benedikt Hofmann, Patrick Stöckle — [Closing the Gap: Automated Discovery of Secure Dockerfile Reference Standards via Semantic Clustering in Enterprise Inner Source](http://arxiv.org/abs/2608.25793v1)
  <details><summary>📄 Abstract</summary>
  Containerization dominates enterprise software delivery, yet Dockerfiles that assemble container images frequently harbor security misconfigurations and structural technical debt. This problem is poorly understood in corporate inner-source environments, where proprietary context and isolated governance prevent direct application of open-source findings.   We present an automated, six-stage pipeline that: (1) crawls an enterprise GitLab instance, (2) enriches each Dockerfile with static security ...
  </details>

- **2026-08-26** — Kyungnam Park, Keunju Song, Yeji Lim et al. — [UNION: A Unified AC-OPF Framework for Topology-Varying Real-Time Grid Operation](http://arxiv.org/abs/2608.25784v1)
  <details><summary>📄 Abstract</summary>
  Secure real-time grid operation requires fast AC optimal power flow (AC-OPF) tools that stay accurate and feasible as operating conditions and topology change. Learning-based methods have advanced, but most are trained per system or per topology, and delivering an operating point that satisfies every operational limit remains challenging. This paper proposes UNION, a unified graph-based AC-OPF framework for heterogeneous systems and topology-varying operation. UNION proposes a shared graph encod...
  </details>

- **2026-08-26** — Weiming Li, Helen Paik, Yulei Sui — [LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents](http://arxiv.org/abs/2608.25777v1)
  <details><summary>📄 Abstract</summary>
  Modern GUI-agent frameworks achieve strong desktop task performance with frontier API models, yet persistent control information often remains implicit in growing interaction trajectories. At each step, the planner reconstructs the active task stage, accumulated evidence, and runtime feedback before deciding the next action. This dependence becomes more pronounced under weaker local reasoning backbones. Across four representative state-of-the-art frameworks, replacing GPT-5 with Qwen3.5-9B reduc...
  </details>

- **2026-08-26** — Jingqing Wang, Wenchi Cheng — [E2-Conditioned Finite-Horizon Effective Capacity for Public-Safety MCX over Shared O-RAN](http://arxiv.org/abs/2608.25442v1)
  <details><summary>📄 Abstract</summary>
  Supporting public-safety Mission Critical Services (MCX) over a shared Open radio access network (O-RAN) requires service assurance over finite incident horizons, while ordinary mobile traffic competes for the same resources and heterogeneous E2 domains expose different observations, control actions, and actuation latencies. Existing RAN key performance indicators are retrospective, whereas conventional effective capacity characterizes an asymptotic stationary regime and therefore suppresses bot...
  </details>

- **2026-08-26** — Yixiao Feng, Yueting Wang, Yining Wang et al. — [Towards Faithful and Efficient Semantic Communication: An Ontological Approach](http://arxiv.org/abs/2608.25422v1)
  <details><summary>📄 Abstract</summary>
  In this paper, an ontology-driven semantic communication (ODSC) framework is proposed for multi-view visual question answering (VQA) tasks. In the considered framework, multiple transmitters observe a scene, extract the semantic information (SI) with vision-language models (VLMs), and transmit the scene graphs to a receiver. Due to the completeness, heterogeneity, and uninterpretability of the VLMs, the extracted scene graphs are redundant, ambiguous, and inconsistent. To solve these problems, t...
  </details>

- **2026-08-26** — Kaishen Wang, Dongdi Zhao, Yijun Liang et al. — [Where to Look Matters: On-Policy Self-Distillation for Long-Video Understanding](http://arxiv.org/abs/2608.25356v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have made substantial progress in long-video understanding, with standard backbone models typically answering questions from frames sampled across the full video. However, as videos become longer, the full-video context inevitably contains more question-irrelevant temporal content, which can distract the model from the evidence needed to answer a specific question. We empirically find that focusing the visual input on short annotated clue intervals containing questi...
  </details>

- **2026-08-26** — Suyang Zhong, Jingzhe Zhu, Qi Xu et al. — [FinRiskAtlas: Decision-Aligned Evaluation of Large Language Models for Financial Risk Review](http://arxiv.org/abs/2608.25325v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models for professional financial review requires more than measuring general financial competence: models must perform the specific review operation required by a workflow and determine whether available evidence is sufficient for a defensible decision. Existing financial benchmarks cover knowledge, reasoning, compliance, and professional tasks, but their evaluation units are often organized around datasets or task formulations rather than the decisions that deployed sy...
  </details>

- **2026-08-26** — Jun Yu — [Metis: Typed Runtime Mediation for Tool-Using Software Agents](http://arxiv.org/abs/2608.25322v1)
  <details><summary>📄 Abstract</summary>
  Software agents connect probabilistic model output to operations that change repositories, processes, networks, and graphical applications. We present Metis, a multi-provider runtime that converts provider streams into typed events before admitted calls reach external effects. Its execution path makes permission decisions, interference classes, terminal results, and lifecycle transitions explicit and inspectable. We evaluate these mechanisms on frozen source artifacts. Across 30 matched real-I/O...
  </details>

- **2026-08-26** — Zhaoming Hu, Xiaochen Nie, Ruikang Zhong et al. — [Security-Aware Pinching-Antenna Systems (PASS): Physical-Layer Security Transmission](http://arxiv.org/abs/2608.25301v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates heterogeneous secure multi-user transmission in pinching-antenna systems (PASS), where dynamically adjustable pinching antennas reshape both guided-wave and free-space propagation to improve communication and confidentiality performance. Unlike conventional physical-layer security designs that represent different security requirements merely through weights or thresholds, heterogeneous services may change the logical role of each receiver for each information stream. To a...
  </details>

- **2026-08-26** — Jiaming Zhou, Qihang Zhang, Gangwei Xu et al. — [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](http://arxiv.org/abs/2608.26103v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot cross-task generalization, where a policy must execute manipulation tasks never seen during training, remains a central challenge in robot learning. In large language models, a novel task can be performed simply by specifying it in the context, without any parameter update. This form of in-context learning (ICL) turns generalization into a problem of task specification. To achieve cross-task generalization, we bring this paradigm to robotic manipulation, and argue that the natural task...
  </details>

- **2026-08-26** — Lehong Wu, Yuxiao Qu, Zheyuan Hu et al. — [$R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning](http://arxiv.org/abs/2608.26053v1)
  <details><summary>📄 Abstract</summary>
  Reasoning in language allows foundation models to spend more test-time compute on hard problems, such as those requiring decomposition, constraint tracking, and prediction of future consequences. Whether this mechanism can improve robotic manipulation remains unclear, where long-horizon tasks require tracking partial progress, reasoning about object relations, recovering from mistakes, and steering noisy low-level policies. In this paper, we study whether VLMs can be trained to reason directly i...
  </details>

- **2026-08-26** — Rui He, Nihal Altay, Wolfram Hinzen — [Distinct dynamics of conceptual and referential disruptions in human reading and large language model processing](http://arxiv.org/abs/2608.25999v1)
  <details><summary>📄 Abstract</summary>
  Linguistic meaning is grounded in conceptual content, from which reference to particular entities emerges as words enter discourse. To examine the processing dynamics associated with these two dimensions of meaning, we selectively disrupted conceptual or referential information in short narratives and traced the resulting effects in human self-paced reading and in the predictive and representational processing of large language models. In human reading, conceptual disruptions produced a strong b...
  </details>

- **2026-08-26** — Haocheng Sun, Mulai Tan — [BVR Sim: An Open and High-Throughput Environment for Heterogeneous Air-Combat Reinforcement Learning](http://arxiv.org/abs/2608.25419v1)
  <details><summary>📄 Abstract</summary>
  Beyond-visual-range (BVR) air combat is a challenging reinforcement-learning domain characterized by partial observability, long-horizon decision making, energy management, and limited weapons. We present BVR Sim, an open-source Gymnasium-style environment designed for heterogeneous air-combat reinforcement learning. BVR Sim supports multiple JSBSim aircraft models, including the F-15, F-16, F/A-18, and F-22, with configurable weapons, sensors, controllers, and opponents. A unified tactical acti...
  </details>

- **2026-08-26** — Jingyang Su, Pu Cao, Xiuze Jin et al. — [PointRL: Learning Point-Level Vision-Language Grounding from Verifiable Annotation Evidence](http://arxiv.org/abs/2608.25299v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) increasingly rely on point coordinates as a compact and executable interface for visual grounding in GUI interaction, robotic manipulation, and interactive visual systems. However, learning reliable pointing behavior remains difficult because the supervision space is inherently non-unique: many coordinates may be valid within the same target region, while multi-instance instructions require target coverage, count consistency, and duplicate suppression. This work pre...
  </details>

- **2026-08-26** — Nabaraj Subedi, Shuvo Dip Datta, Ahmed Abdelaty et al. — [PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans](http://arxiv.org/abs/2608.26091v1)
  <details><summary>📄 Abstract</summary>
  Civil infrastructure compliance checking has long relied on engineers manually reading legacy 2D plans; however, OCR-based automation strips away the geometry and layout essential for interpreting these plans. We present a Visual-First Multimodal Retrieval-Augmented Generation (RAG) framework called PlanSightRAG. It indexes and reasons directly over plan imagery, integrates a ColNomic-3B multi-vector retrieval, an agentic Planner-Retriever-Auditor-Synthesizer, and MaxSim heatmaps as an evidence ...
  </details>

- **2026-08-26** — Ziming Liu, Bhanu Chaitanya Jasti, Ziyang Xu et al. — [Beyond Local Surprise: Grounded Dialogue as Selective Belief Revision under Referential Uncertainty](http://arxiv.org/abs/2608.26035v1)
  <details><summary>📄 Abstract</summary>
  When a speaker refers to a scene that the listener cannot directly see, the listener must decide whether to preserve its current understanding or revise it as new utterances arrive. Many language systems treat local mismatch as a cue for updating: divergence from the current understanding encourages adjustment. Yet conversational understanding may be more conservative, interpreting mismatching evidence relative to prior understanding rather than immediately revising it. We introduce a controlled...
  </details>

- **2026-08-26** — Oliver Petersen, András Vasy — [Dual modes in Kerr spacetimes and the Whiting transform: Mode stability revisited](http://arxiv.org/abs/2608.26034v1)
  <details><summary>📄 Abstract</summary>
  The purpose of the paper is to place Whiting's classical growing mode stability argument, extended to real frequencies by Shlapentokh-Rothman for the scalar wave equation and by Andersson, Ma, Paganini and Whiting in general, in the framework of classical PDE theory. The key steps are: a description of the dual or adjoint modes, a singular phase space pairing argument which is technically executed via the Fourier transform, followed by a standard unique continuation result.   One part of our des...
  </details>

- **2026-08-26** — Mehran Ahmad, Ali Abbasian Ardakani, Afshin Mohammadi et al. — [Less Contouring, More Accuracy: Lesion-Guided ROI Deep Learning for Ovarian Ultrasound Classification](http://arxiv.org/abs/2608.25965v1)
  <details><summary>📄 Abstract</summary>
  Ovarian lesion classification using transvaginal ultrasound remains challenging due to overlapping imaging characteristics and the dependence on expert interpretation. This study investigates whether lesion-guided region-of-interest (ROI) deep learning can achieve competitive diagnostic performance while reducing the annotation burden associated with pixel-level lesion segmentation. Two publicly available ovarian ultrasound datasets were evaluated: the Multi-Modality Ovarian Tumor Ultrasound (MM...
  </details>

- **2026-08-26** — Haiyan Hao — [Spatial-Knowledge-Graph-Grounded LLM Agents for Neighborhood Livability Evaluation](http://arxiv.org/abs/2608.25952v1)
  <details><summary>📄 Abstract</summary>
  Neighborhood livability is commonly assessed with static built-environment indicators, such as facility proximity, street connectivity, and access to public space. These measures describe available opportunities but do not directly represent how residents with different mobility capacities, household roles, schedules, and care responsibilities experience the neighborhood. This paper presents a prototype framework that uses a spatial knowledge graph (KG) and large language models (LLMs) to genera...
  </details>

- **2026-08-26** — Yuqiang Lin, Yan Shi, Sam Lockyer et al. — [TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding](http://arxiv.org/abs/2608.25935v1)
  <details><summary>📄 Abstract</summary>
  Traffic Anomaly Understanding (TAU) requires models and systems to detect, reason about, and explain anomalous events in transportation videos. To address this challenge, we propose TAU-Agent, an agentic retrieval-augmented framework for traffic anomaly understanding. Given a task query, a central retrieval agent orchestrates two visual perception tools, namely a Video Captioning Tool and an Open-Vocabulary Tracking Tool, to retrieve and select query-relevant evidence, including captions, tempor...
  </details>

- **2026-08-26** — Ruoqi Hu, Chulin Zhao, Jiashuo Chang et al. — [When Composition Doesn't Add Up: Humans Identifying Defects in AI-Generated Images](http://arxiv.org/abs/2608.25933v1)
  <details><summary>📄 Abstract</summary>
  *Chulin Zhao and Ruoqi Hu contributed equally to this work.   State-of-the-art text-to-image (T2I) models exhibit pronounced and systematic defects when prompts involve intricate compositional factors such as multiple entities and multiple attributes. In this paper, we investigate how humans identify such defects. Specifically, we manually select 651 reference images from the four categories of people, hand, object, and scene that exhibit complex compositional characteristics, from which prompts...
  </details>

- **2026-08-26** — Ante Kapetanovic, Kemal Altwlkany, Andro Mercep et al. — [Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence](http://arxiv.org/abs/2608.25869v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly assess generated content, giving rise to the LLM-as-a-Judge paradigm. These systems now score outputs, filter content, and gate iterative refinement in production pipelines, where each judgment is often assumed to be independent of earlier evaluations. We test this assumption using three prompt conditions: no metadata, revision framing, and anchored metadata containing revision, attempt, and prior-score fields. We show that prior scores, even when includ...
  </details>

- **2026-08-26** — Subir Kumar Parida, Rajbabu Velmurugan, Ketan Kotwal et al. — [Learning Late, Guiding Early: Timestep-Decoupled Semantic Guidance for Fair Face Generation](http://arxiv.org/abs/2608.25862v1)
  <details><summary>📄 Abstract</summary>
  Demographic imbalance in synthetic face generation can propagate to downstream face recognition systems, making fairness an important consideration when diffusion models are used for data generation. Existing fairness-aware generation approaches often require model retraining, architectural modifications, or repeated guidance throughout the reverse diffusion process. In this work, we introduce Semantic Boundary Predictor (SBP), an inference-time framework that performs demographic guidance throu...
  </details>

- **2026-08-26** — Zhiqiang Shi, Oana Cocarascu — [Key Point Analysis Needs Structure Recovery: Task Definition, Dataset Diagnosis, and a Structure-Aware Benchmark](http://arxiv.org/abs/2608.25854v1)
  <details><summary>📄 Abstract</summary>
  Key Point Analysis (KPA) aims to identify a concise set of key points that summarize a collection of arguments together with their prevalence. We argue that KPA is fundamentally a structured prediction problem that requires recovering semantic groupings, generating representative key points, ensuring coverage, and estimating prevalence. Under this formulation, we show that existing KPA benchmarks suffer from limitations in grouping quality, redundancy, coverage, and argument-key point mappings, ...
  </details>

- **2026-08-26** — Fitsum Debebe Tilahun, Chung G. Kang — [Generative AI-Enabled Mission-Aware Radio Orchestration for RIS-Assisted LEO Satellite ISAC Systems](http://arxiv.org/abs/2608.25803v1)
  <details><summary>📄 Abstract</summary>
  Mission-adaptive low-Earth-orbit (LEO) satellite networks with integrated sensing and communication (ISAC) must retarget radio resources as operator goals change. To enable this adaptation from flexible operator language, we develop a generative-AI-enabled radio-orchestration framework in which a large language model (LLM) maps each mission into a structured policy comprising communication, sensing, and fairness weights, mandatory quality-of-service thresholds, power-allocation guidance, and sol...
  </details>

- **2026-08-26** — Abhinav Havaldar, Enrico Santus — [When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies](http://arxiv.org/abs/2608.25717v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) is widely assumed to mitigate factual errors in large language models (LLMs), but it remains unclear whether retrieval uniformly compensates for missing knowledge. We study this question in a controlled factual QA setting over public companies, constructing a benchmark of approximately 2,000 firms across global equity indices. We evaluate six LLMs on four atomic attributes under four conditions: no-context, perfect context, misleading context, and distraction...
  </details>

- **2026-08-26** — Tim Schopf, Tobias Schreieder, Akiko Aizawa — [Think-Probe-Respond: Improving Large Language Models as Judges of Research Idea Novelty](http://arxiv.org/abs/2608.25660v1)
  <details><summary>📄 Abstract</summary>
  Automated novelty judgment can accelerate scientific discovery by enabling efficient evaluation, refinement, and comparison of research ideas. While large language models are increasingly adopted for this task, we investigate a previously overlooked limitation in their judgment capabilities: despite generating reasoning rationales that closely mirror those of human experts, their final novelty judgments often diverge substantially. We demonstrate that this miscalibration stems from a systematic ...
  </details>

- **2026-08-26** — Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil et al. — [Generative vs. Encoder Large Language Models for ASR Evaluation: A Comparative Study](http://arxiv.org/abs/2608.25574v1)
  <details><summary>📄 Abstract</summary>
  Automatic Speech Recognition (ASR) is typically evaluated using Word Error Rate (WER), which poorly reflects semantic similarity. While embedding-based metrics correlate better with human judgments, the respective roles of encoder and decoder-based Large Language Models (LLMs) remain underexplored. This paper presents a comparative study of both families for ASR evaluation. We analyze BERTScore and SemDist across different LLMs, layers, and pooling strategies, showing that both metrics can achie...
  </details>

- **2026-08-26** — Xintong Zhang, Xiaomeng Fan, Shilin Yan et al. — [AdaVDR: Adaptive Tool Use and Reflection for Video Deep Research](http://arxiv.org/abs/2608.25559v1)
  <details><summary>📄 Abstract</summary>
  Video deep research answers complex questions by jointly understanding video content and retrieving external knowledge from the open Web. However, diverse questions and videos require different tool-use strategies, and inappropriate tool calls can produce incorrect results. Uncertain grounding and retrieval also make unnecessary interactions costly and error-prone, increasing latency and reasoning errors. To address these challenges, we propose AdaVDR, an adaptive video deep research agent with ...
  </details>

- **2026-08-26** — Martino Ciaperoni, Sezer Kutluk, Benedetta Muscato et al. — [Virgil: Navigating Explainability for Transformer-based Language Models](http://arxiv.org/abs/2608.25555v1)
  <details><summary>📄 Abstract</summary>
  Explainability for transformer-based language models is becoming crucial as these systems are deployed in high-stakes applications. As a result, the ecosystem of explainability tools is rapidly evolving, becoming richer, but also more fragmented and harder to navigate. To address this challenge, we present Virgil, an interactive system that lets practitioners and researchers, including non-experts, navigate explainability tools for transformer language models. Supported by a curated knowledge ba...
  </details>

- **2026-08-26** — Paulo Yanez Sarmiento, Pia Francesca Rissom, Manuel Pfeuffer et al. — [Interpreting Protein Language Model Embeddings via Orthogonal Projection for Protein Fitness Prediction](http://arxiv.org/abs/2608.25548v1)
  <details><summary>📄 Abstract</summary>
  Recently, there has been a growing adoption of protein language models (PLMs) in biomedical science. Their embeddings provide a rich numerical representation of protein sequences which achieve state-of-the-art performance on several downstream tasks including protein fitness prediction. However, PLM embeddings are not directly interpretable and, thereby, it remains unclear what features they encode. To gain insight into which biochemical properties of the protein are driving the prediction, we l...
  </details>

- **2026-08-26** — Jihao Zhu, Zhiwei Yang, Wenxiao Zhang et al. — [ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives](http://arxiv.org/abs/2608.25531v1)
  <details><summary>📄 Abstract</summary>
  Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models are a practical alternative, but directly feeding them an entire long context remains costly, hard to inspect, and prone to missing sparse evidence. We present ClueWeaver, an evidence-aware dual-agent framework for long-narrative quest...
  </details>

- **2026-08-26** — Siyuan Sun, Mihai Surdeanu — [Query Expansion Is More Than Generation: Improving Dense Retrieval through Better Integration](http://arxiv.org/abs/2608.25521v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate query expansions without task-specific training, yet the same expansions often make a frozen dense retriever worse. We identify an underexplored factor: prior work has often focused on what text is generated, while how generated text is incorporated into dense retrievers has received less systematic attention. By holding generated expansions fixed, we show that performance degradation can often be attributed to the integration method itself. We introduce...
  </details>

- **2026-08-26** — Chengsong You, Junwei Zhou, Nan Du — [DocPC: Document-Level Visual Retrieval via Representative Page Composition](http://arxiv.org/abs/2608.25434v1)
  <details><summary>📄 Abstract</summary>
  Visual document retrieval has advanced by encoding page screenshots with vision-language models, bypassing OCR pipelines. However, existing methods remain page-centric, misaligned with real-world scenarios requiring complete document retrieval. A naive page-then-document aggregation suffers from linear indexing cost and degraded retrieval when relevance spans multiple pages. We propose DocPC, a document-level visual retrieval framework based on Representative Page Composition: selecting represen...
  </details>

- **2026-08-26** — Wei-Jian Jiang, Ye-Nan Sha, Hui Guo et al. — [Interpretable physics-informed retrieval-augmented generation language model for end-to-end inorganic crystal synthesis planning](http://arxiv.org/abs/2608.25392v1)
  <details><summary>📄 Abstract</summary>
  Synthesis planning for inorganic materials requires predicting both synthesizability and viable routes by linking microscopic thermodynamic stability with macroscopic synthesis methods, precursors, and processing conditions. Here, we develop an interpretable Physics-Informed Retrieval-Augmented Generation Language Model (PIRAG-LM) for end-to-end inorganic crystal synthesis planning. We construct a material-centered Structured Synthesis Knowledge Base (SSKB) containing route-level records for 13,...
  </details>

- **2026-08-26** — Yiqun Sun, Junyu Chen, Pengfei Wei et al. — [GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models](http://arxiv.org/abs/2608.25375v1)
  <details><summary>📄 Abstract</summary>
  Generative vision-language models (VLMs) are increasingly used in human-centered settings, yet they can produce demographically biased outputs even when images differ only in controlled attributes such as perceived race or gender. However, existing inference-time debiasers were largely designed for static embeddings or CLIP-like models rather than generative VLMs. We propose GGSS---Geodesic-Gated Spherical Steering---a norm-preserving intervention that discovers a counterfactual bias subspace on...
  </details>

- **2026-08-26** — Pratyay Banerjee, Ankit Chadha — [Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation](http://arxiv.org/abs/2608.25277v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems coordinate through natural-language messages that consume 40--60\% of their token budget. Replacing these with structured graphs reduces cost but fails on tasks requiring adaptive reasoning. We propose \textbf{Routed Graph Handoff}, where a lightweight LLM router (155 tokens, 0.15\% overhead) selects between a typed dependency graph and natural language for each delegation. On four benchmarks (1,050+ trajectories), the routed system matches or exceeds NL-only on every tas...
  </details>

- **2026-08-26** — Peize Ding — [ShuttleArena: Interpretable Self-Play in Physics-Based Badminton](http://arxiv.org/abs/2608.25246v1)
  <details><summary>📄 Abstract</summary>
  Badminton is a compact but challenging domain for game AI: a player must choose a physically feasible shuttle trajectory, anticipate the opponent's interception, and recover to a court position whose value depends on the opponent's next response. The central challenge is that shot selection and recovery are not separable: the best recovery depends on the shot-induced opponent response, while the value of the shot depends on whether the hitter can cover the reply. This paper presents ShuttleArena...
  </details>

- **2026-08-26** — Yegor Denisov-Blanch, Shyam Agarwal, Pavel Azaletskiy et al. — [A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption](http://arxiv.org/abs/2608.25241v1)
  <details><summary>📄 Abstract</summary>
  Coding agents increase development velocity but also technical debt. Prior work reports only average effects across adopters, hiding wide differences between teams. We introduce RAMP (Repository AI Maturity Profile), a four-level cumulative maturity model grounded in version-controlled artifacts that teams commit to configure AI tools. RAMP runs from behavioral rules and coding standards through named agent definitions to multi-agent orchestration, with observed practice concentrated in the firs...
  </details>

- **2026-08-25** — Joy Chen, Alejandro Castillejo Munoz, Pierluca D'Oro et al. — [ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices](http://arxiv.org/abs/2608.26204v1)
  <details><summary>📄 Abstract</summary>
  Computer Use Agents (CUAs) are increasingly deployed to navigate mobile and desktop applications on behalf of users, yet no benchmark comprehensively evaluates whether they can safely interact with visual interfaces while handling ambiguous instructions. We introduce ADeptS-Bench, a dual-stream trustworthiness benchmark, grounded in the ADEPTS capability framework and general population user studies. The Safety stream provides paired benign/malicious tasks with threats embedded in the visual int...
  </details>

- **2026-08-25** — Minda Zhao, Xu Han, Rishabh Goel et al. — [Rare Diseases, Common Dilemmas: LLMs Prioritize Equal Resource Distribution over Patient Benefit in Decision-Making](http://arxiv.org/abs/2608.25236v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision-making often involves prioritizing ethical values, such as beneficence, non-maleficence, respecting a patient's autonomy, and justice. Recent work has begun to assess how large language models (LLMs) make such subjective, value-laden clinical judgments. However, evaluations of LLM decision-making in rare disease care contexts, where ethical tensions are ubiquitous and where scarce prior information likely impacts LLM behavior, are still lacking. Here, we present a benchmark of ...
  </details>

- **2026-08-25** — Avinash malik — [Compiling Spatial Certificates into Temporal Contracts for Latency-Aware Control](http://arxiv.org/abs/2608.25228v1)
  <details><summary>📄 Abstract</summary>
  We introduce CIPS, a contract-driven execution abstraction for   managing computational latency and sampled-data updates in   safety-critical cyber-physical systems (CPS). A fundamental challenge   in real-time control is that physical safety certificates are defined   spatially, yet predicting their validity under non-zero computation   and handoff latency requires online numerical integration of plant   dynamics. CIPS resolves this operational dichotomy by systematically   compiling heterogene...
  </details>

- **2026-08-25** — Haotian Qiao, Robert P. Dick — [LLM-Driven, Datasheet-Aware Automated Hardware Compatibility Verification for Early-Stage, Pre-Schematic Embedded System Design](http://arxiv.org/abs/2608.25217v1)
  <details><summary>📄 Abstract</summary>
  We present an LLM-driven, datasheet-aware framework for early-stage hardware compatibility verification that identifies documentation-level interface incompatibilities based on hardware datasheets and high-level component connectivity descriptions. It does not require, and can therefore be used, before detailed schematic simulation and implementation. We view trustworthy LLM-assisted design automation not as directly generating answers from documents, but as transforming engineering information ...
  </details>

- **2026-08-25** — James C. Davis, Kelechi Kalu, Huiyun Peng et al. — [Model-Based Agentic Software Engineering](http://arxiv.org/abs/2608.25174v1)
  <details><summary>📄 Abstract</summary>
  Coding agents increase implementation capacity without automatically making project intent, system structure, or acceptance evidence explicit. As implementation becomes abundant relative to engineering judgment, the scarce work shifts toward choosing useful abstractions, producing evidence, and determining which obligations govern acceptance. Existing workflows address parts of this gap through larger prompts, repository retrieval, or perchange review, but still require agents and engineers to r...
  </details>

- **2026-08-25** — Matthew Flathers, Phuong Anh Nguyen, Jill Noorily et al. — [HealthBench-Psych: A Mental Health Subset of OpenAI's HealthBench](http://arxiv.org/abs/2608.25071v1)
  <details><summary>📄 Abstract</summary>
  General-purpose health benchmarks increasingly anchor claims about LLM medical performance, but they are not always resolved by clinical specialty, making domain-specific performance hard to isolate. Mental health is of acute public-health concern as millions of people turn to LLMs for psychological support, and most existing evaluations are bespoke academic benchmarks that are difficult to integrate into developer workflows. We introduce HealthBench-Psych and HealthBench-Psych-Hard. We screened...
  </details>

- **2026-08-25** — Liangcai Su, Zhaopeng Feng, Zhuo Chen et al. — [FrontierChallenge: Evaluating Scientific Workflow Completion](http://arxiv.org/abs/2608.24979v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents increasingly analyze data, execute code, and produce research artifacts, yet most benchmarks emphasize final answers, isolated programs, or a single domain. We introduce FrontierChallenge, a cross-domain benchmark comprising 300 end-to-end scientific workflows. In this paper, we release and evaluate 97 of these tasks, spanning quantum chemistry, molecular dynamics, materials characterization, analytical chemistry, life science, and electrochemistry/environment. Each task provid...
  </details>

- **2026-08-25** — Manmeet Singh, Somnath Luitel, Prabhjot Singh et al. — [AFDBench: A Reasoning-First AI Scientist for NationalWeather Service Forecast Discussions](http://arxiv.org/abs/2608.24954v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) hallucinate numerical values when generating high-stakes meteorological text, posing risks for weather communication. We present AFDBench, an AI meteorologist that generates professional Area Forecast Discussions (AFDs) by reasoning through structured AI weather forecast data from Google's WeatherNext 2. We introduce AFDBench, the first benchmark for evaluating generative meteorological reasoning, comprising 7,732 expert written discussions from 13 National Weather S...
  </details>

- **2026-08-25** — Shyam Agarwal, Bogdan Vasilescu — [SPECMINE: A Large-Scale Corpus of Spec-Driven Development Artifacts](http://arxiv.org/abs/2608.25202v1)
  <details><summary>📄 Abstract</summary>
  Spec-Driven Development (SDD) is a fast-emerging practice in which a structured natural-language specification, written by a developer, or (more often) drafted by an AI tool and then curated by the developer, drives an AI coding agent's implementation. A wave of tooling (GitHub Spec Kit [3], OpenSpec [4], AWS Kiro [5], and dozens of others) has appeared since 2025, yet the artifacts these tools produce have never been studied at scale. We present SPECMINE, a corpus that captures SDD in public Gi...
  </details>

- **2026-08-25** — Fan Yang, Matt Thomson — [What Should a Large Language Model See? Physical Invariants as a Data Representation for PDE Discovery](http://arxiv.org/abs/2608.25189v1)
  <details><summary>📄 Abstract</summary>
  Understanding how molecular interactions govern macroscopic behaviour is a central challenge in molecular sciences. However, conventional theory building cannot keep pace with the vast datasets modern experimentation routinely produces. Large language models offer a promising route to automating theory construction, but a spatiotemporal field cannot be directly placed in a prompt. Existing models generally learn about the data only through a score measuring how well each proposal fits it. Here w...
  </details>

- **2026-08-25** — Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Kamil Akhuseyinoglu et al. — [Self-Explanation Tutor for Active Study of CS1 Worked Examples](http://arxiv.org/abs/2608.25180v1)
  <details><summary>📄 Abstract</summary>
  Worked examples are a important part of introductory programming, but reading their expert explanations is passive. Self explanation, students explaining the problem and its solution to themselves with subgoal level analysis, turns that study into an active task, yet it is hard to scale because assessing free-text explanations and returning timely feedback has had no easy automated solution. We investigate whether a large language model (LLM) can fill that gap. We build a self-explanation tutor ...
  </details>

- **2026-08-25** — Samuele Vallisa, Federico Ravenda, Claudio Palominos et al. — [The Changing Geometry of Grammar: Dimensionality and Neighborhood Reorganization across Transformer Layers](http://arxiv.org/abs/2608.25166v1)
  <details><summary>📄 Abstract</summary>
  Transformer representations describe trajectories through high-dimensional vector spaces, which are shaped dynamically as tokens incorporate relational context across layers. Such data tend to concentrate on lower-dimensional sub-manifolds, a form of compression quantified by the Intrinsic Dimensionality (ID), the minimum number of independent variables needed to represent them without significant information loss. In this work, we ask whether the grammatical role of tokens, as marked by their p...
  </details>

- **2026-08-25** — Nikola Bukowiecka, Daniel B. Reisenfeld, Maciej Bzowski — [Capra: Scalable HEALPix-Native Intensity Reconstruction for High-Resolution IMAP Analyses](http://arxiv.org/abs/2608.25134v1)
  <details><summary>📄 Abstract</summary>
  We present Capra, a HEALPix-native pipeline for reconstructing all-sky energetic neutral atom (ENA) intensity maps from the NASA Interstellar Boundary Explorer (IBEX) and Interstellar Mapping and Acceleration (IMAP) missions' event-counting data. Capra produces two products: (1) a baseline boresight-assigned map, and (2) an optional smoothed map on the HEALPix grid. This produces smooth, physically interpretable maps with consistent resolution changes and reference-frame transformations. The smo...
  </details>

- **2026-08-25** — Xiulin Yang, Ethan Gotlieb Wilcox, Catherine Arnett — [Apples to Apples? Towards Comparable Crosslingual Language Model Evaluation](http://arxiv.org/abs/2608.25089v1)
  <details><summary>📄 Abstract</summary>
  Crosslingual evaluation of language models that enables fair comparisons remains a fundamental challenge in multilingual NLP. Existing studies adopt a variety of downstream tasks and intrinsic metrics with different theoretical justifications, yet there has been little empirical investigation into whether these approaches yield meaningful crosslingual conclusions. We systematically examine crosslingual evaluation approaches using controlled monolingual language models trained on parallel data wi...
  </details>

- **2026-08-25** — Amir Taherin, Sana Taghipour Anvari, Charles Amante et al. — [Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels](http://arxiv.org/abs/2608.25053v1)
  <details><summary>📄 Abstract</summary>
  Edge LLM deployment is shaped by more than model size and precision: inference backend, hardware platform, memory traffic, and power management all affect latency and efficiency. We present Hydra, a common-schema, phase-aware workload characterization framework for LLM inference on edge SoCs. Hydra instruments HuggingFace Transformers and llama.cpp with a shared per-prompt timing schema and fuses those records with hardware telemetry, enabling a multi-dimensional characterization of performance,...
  </details>

- **2026-08-25** — Wenting Zhu, Chenghua Gong, Sanchuan Guo et al. — [Tabular Foundation Models for Multi-View Information Cascade Popularity Prediction](http://arxiv.org/abs/2608.25048v1)
  <details><summary>📄 Abstract</summary>
  Predicting the future popularity of information cascades is essential for understanding information diffusion on social media. Despite recent advances, existing methods face two key limitations: they focus primarily on the cascade view while overlooking other information views that drive user engagement, such as textual semantics, visual content, and tabular attributes; and they fail to capture high-order cross-view interactions. To address these issues, we propose \textbf{TFM4POP}, the first fr...
  </details>

- **2026-08-25** — Casey Kennington — [A Primer on Computational Semantics for Artificial Intelligence Systems](http://arxiv.org/abs/2608.25022v1)
  <details><summary>📄 Abstract</summary>
  As people adopt transformer-based language models (e.g., ChatGPT and Gemini) for an increasing number of use-cases, it is important to know how such models learn and represent the meaning of the language, and to be more informed about what language is. This document is an attempt to help the reader understand how linguistic meaning (i.e., semantics) is approached from different fields of scientific and philosophical examination. I also explain three primary semantic theories: formal semantics, g...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 603 |
| prompt-injection | 510 |
| memory-poisoning | 44 |
| tool-use-attack | 129 |
| backdoor | 434 |
| adversarial-attack | 572 |
| privacy-leakage | 3938 |
| steganography | 58 |
| misuse | 941 |
| red-teaming | 119 |
| vulnerability | 2865 |
| defense | 2618 |
| alignment | 2415 |
| robustness | 2492 |
| watermark | 355 |
| unlearning | 92 |
| agent-safety | 52 |
| benchmark | 64 |
| survey | 301 |
| other | 6922 |

---

📚 **全部 25524 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-08-31 03:15:25*