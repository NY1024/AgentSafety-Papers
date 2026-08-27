<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-25321-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-27 21:36 ｜ **论文总数 / Total Papers**: 25321（近 30 天 / Recent 30 days: 4263）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 25321 篇论文（含摘要、分类筛选、搜索）/ View all 25321 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 599
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 509
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 127
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 432
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 572
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3926
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 57
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 938
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 118
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2843
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2585
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2397
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2460
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 351
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 92
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 62
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 299
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6858

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4263 篇，完整 25321 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4263 papers from the last 30 days (with date, authors & abstract). For the full list of 25321 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

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

- **2026-08-24** — Lorenzo Bossi, Federico Saccani, Francesco Panebianco et al. — [Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums](http://arxiv.org/abs/2608.23185v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence from underground forums has traditionally relied on passive monitoring. However, as users have become more aware of large-scale data collection, valuable intelligence has become increasingly rare in open forums, often migrating instead to private or harder-to-reach spaces, making passive approaches inadequate. Building on the intuition that relevant information can be obtained through active elicitation, this paper presents DarkBot, to the best of our knowledge, the fir...
  </details>

- **2026-08-24** — Zeyu Feng, Qingyu Wu, Yuzhe Luo et al. — [PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies](http://arxiv.org/abs/2608.23028v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

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


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-08-25** — Zhonghao Zhan, Hamed Haddadi — [Auto-Policy, not Auto-Skill: Compiled Agent Skills for the Physical World](http://arxiv.org/abs/2608.25091v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving Skill harnesses (AutoSkills, Hermes Agent) generate more advisory orchestration automatically; their reported gains are efficiency, not safety. This misses the actual gap: a Skill describes how an agent should behave; a Policy decides which behavior is allowed to become an action. Today's format covers the first with markdown and scripts; the second is left to the model. Generating more Skills scales the gap, not the safety, especially when a wrong invocation can unlock a door or m...
  </details>

- **2026-08-24** — Ziyue Yang, Fan Ding — [Signal or Noise? A Benchmark Study of Agent Skills in Web Development](http://arxiv.org/abs/2608.23067v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills are reusable procedural modules that are increasingly injected into coding-agent sessions to encode framework conventions, anti-patterns, and reusable tools. However, because each injected Skill expands the prompt of every query, an effective Skill benchmark must determine not only whether an agent can solve a task, but whether the Skill should have been injected at all. We introduce WebDev-Skills-Bench and use it for a controlled empirical study of 31 public WebDev Skills on 50 Web...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 10 papers

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
*隐私泄露 / Privacy Leakage* — 30 papers

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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-24** — Nikita Kezins — [Adversarial Entropy Inflation Against Gumbel-Based Inference Verification](http://arxiv.org/abs/2608.23375v1)
  <details><summary>📄 Abstract</summary>
  Gumbel-based inference verification bounds LLM weight exfiltration by only forgiving token choices that plausibly arise from honest GPU nondeterminism, reporting a >200x slowdown for a steganographic adversary under benign prompt traffic. This bound assumes a passive attacker; we show it degrades sharply against an adversary who instead controls the prompt distribution. Because the verifier's admissible-token-set size is driven by the model's own output entropy, prompts engineered to break gramm...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

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

- **2026-08-25** — Ethan Traister, Ankit Raj, Jiaqi Gan et al. — [Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate](http://arxiv.org/abs/2608.24127v1)
  <details><summary>📄 Abstract</summary>
  Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal ...
  </details>

- **2026-08-24** — Aaron Dharna, Cong Lu, Ryan Sullivan et al. — [AI Finds A Way](http://arxiv.org/abs/2608.23875v2)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) algorithms frequently learn creative and unexpected solutions, surprising even expert researchers who develop and study them. They often astonish practitioners by discovering unanticipated behavior, exploiting loopholes in reward signals, or spontaneously uncovering previously unknown scientific phenomena. However, accounts of such unconventional behavior across machine learning are seldom formally documented. This work presents 26 curated firsthand anecdotes from va...
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


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-08-24** — Shashwat Pandey, Satwik Pandey, Suresh Raghu — [Confidently Wrong, Silently So: Auditing Undetectable Failures of a Deployed On-Device Language Model](http://arxiv.org/abs/2608.23663v2)
  <details><summary>📄 Abstract</summary>
  Aligning deployed language models requires knowing when their outputs can be trusted, yet on-device models now ship to hundreds of millions of devices with no server-side moderation, and the configuration developers can actually deploy is rarely audited independently. We present a reproducible reliability audit of the developer-accessible on-device foundation model, framed as an oversight question: can a user or a resource-constrained developer tell when the model is wrong? Red-teaming it on cal...
  </details>

- **2026-08-24** — Shashwat Pandey, Satwik Pandey, Suresh Raghu — [Confidently Wrong, Silently So: Auditing Undetectable Failures of a Deployed On-Device Language Model](http://arxiv.org/abs/2608.23663v1)
  <details><summary>📄 Abstract</summary>
  Aligning deployed language models requires knowing when their outputs can be trusted, yet on-device models now ship to hundreds of millions of devices with no server-side moderation, and the configuration developers can actually deploy is rarely audited independently. We present a reproducible reliability audit of the developer-accessible on-device foundation model, framed as an oversight question: can a user or a resource-constrained developer tell when the model is wrong? Red-teaming it on cal...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 51 papers

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

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

- **2026-08-24** —  Elle — [The Dialect Tax: Dialectal Biases Persist throughout the Language Modeling Pipeline](http://arxiv.org/abs/2608.24952v1)
  <details><summary>📄 Abstract</summary>
  Systematic dialectal performance gaps in language models (LMs) are well documented, but the source of these disparities within the modern language modeling pipeline remains unclear. Our study traces this "dialect tax" across the natural language processing pipeline. Using parallel English dialect corpora that hold meaning fixed while varying surface form, we first confirm that LMs recognize matched Standard American English (SAE) and dialectal texts as semantically equivalent. However, we discov...
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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 65 papers

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 74 papers

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 18 papers

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


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-08-24** — Xuetong Li, Gaofeng Liu — [EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models](http://arxiv.org/abs/2608.23313v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-08-26** — Hongbo Liu, Peixian Chen, Sihan Liu et al. — [Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios](http://arxiv.org/abs/2608.25529v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have shown strong performance in video understanding. However, their ability to follow instructions in this domain remains under-explored. Real-world video understanding requires models not only to interpret video content correctly, but also to satisfy diverse user-specified constraints. Existing benchmarks focus primarily on task accuracy rather than instruction adherence, leaving this capability insufficiently evaluated. To address this gap, we introduc...
  </details>

- **2026-08-26** — Sadman Sakib, Zhangyi None Peng, Yujie Pang et al. — [A Taxonomy of Construction Task Activities for Robot Workers](http://arxiv.org/abs/2608.25395v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language-action models offer a path toward robots with broader repertoires than conventional task-specific systems. Construction deployment, however, requires a precise inventory of worker activities and the capabilities needed to execute them. We present TARCAT, an occupation-grounded taxonomy derived from 91 O*NET tasks across seven high-employment construction occupations and 30 instructional videos of physical work. TARCAT defines 41 action primitives in 12 groups and three cla...
  </details>

- **2026-08-24** — Mullosharaf K. Arabov — [A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](http://arxiv.org/abs/2608.23421v2)
  <details><summary>📄 Abstract</summary>
  Arabic Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis remains absent. This study presents a bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from five platforms (arXiv, ACL Anthology, Semantic Scholar, Crossref, OpenAlex) plus an additional targeted Op...
  </details>

- **2026-08-24** — Mullosharaf K. Arabov — [A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](http://arxiv.org/abs/2608.23421v1)
  <details><summary>📄 Abstract</summary>
  Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis of the field remains absent. This study presents a large-scale bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from six collections. We employ BERTopic for topic modeling, regression analysis to identify ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 147 papers

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

- **2026-08-24** — Donovan Clay, Saket Gollapudi, Sankar Harilal et al. — [Demystifying Reinforcement Learning Post-Training of Language Models](http://arxiv.org/abs/2608.24949v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training has emerged as a powerful framework for enhancing the capabilities of large language models (LLMs), enabling impressive reasoning, math, and coding capabilities. Yet for many researchers and practitioners, the principles behind classical RL remain a "black box". In this work, we deconstruct the RL post-training algorithm, investigating each step to clarify what is actually happening beneath the surface. By isolating the mechanics of RL with Verifiable Re...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 599 |
| prompt-injection | 509 |
| memory-poisoning | 44 |
| tool-use-attack | 127 |
| backdoor | 432 |
| adversarial-attack | 572 |
| privacy-leakage | 3926 |
| steganography | 57 |
| misuse | 938 |
| red-teaming | 118 |
| vulnerability | 2843 |
| defense | 2585 |
| alignment | 2397 |
| robustness | 2460 |
| watermark | 351 |
| unlearning | 92 |
| agent-safety | 52 |
| benchmark | 62 |
| survey | 299 |
| other | 6858 |

---

📚 **全部 25321 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-27 21:36:52*