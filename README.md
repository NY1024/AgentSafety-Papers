<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-31326-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-06 22:10 ｜ **论文总数 / Total Papers**: 31326（近 30 天 / Recent 30 days: 4672）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 31326 篇论文（含摘要、分类筛选、搜索）/ View all 31326 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 658
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 599
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 54
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 150
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 495
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 623
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4287
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 76
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1120
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 134
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3448
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3275
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3055
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3315
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 541
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 109
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 61
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 384
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8875

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4672 篇，完整 31326 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4672 papers from the last 30 days (with date, authors & abstract). For the full list of 31326 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-10-05** — Xunguang Wang, Qingyue Wang, Yuguang Zhou et al. — [Benchmarking Jailbreak Guardrails for Embodied Agents](http://arxiv.org/abs/2610.06122v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents powered by large language models and vision-language models are increasingly deployed in physical environments, but jailbreak attacks can induce these agents to perform physically harmful actions. A growing number of guardrail methods have been proposed to intercept dangerous behavior before it is executed, yet existing safety benchmarks evaluate the embodied models themselves, leaving it unclear how well these guardrails actually defend an embodied agent in practice. We present ...
  </details>

- **2026-10-04** — Swadesh Swain, Sanghamitra Dutta — [Don't Judge an LLM Only by Its Activations: Discovering Suppressed Safety Features via Counterfactual Activation Potential](http://arxiv.org/abs/2610.05541v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has emerged as the primary means to understand safety behavior of LLMs. However, existing tools primarily focus on the activating neurons or features of a model. The role of the remaining large set of inactive components is invisible to such methods. This work demonstrates that the inactive set contains safety-critical features that are causally relevant for refusal of harmful prompts. Suppressing such features could turn refusals into compliance, while passing undet...
  </details>

- **2026-10-04** — Tongyan Hu, Hao Li, Xiaogeng Liu et al. — [Red-TTT: Test-Time Training for Automated Jailbreaking Large Language Models](http://arxiv.org/abs/2610.05282v1)
  <details><summary>📄 Abstract</summary>
  Large language models remain vulnerable to jailbreaks, and automated red teaming is the standard way to find jailbreaks in large language models at scale. Current methods either draw more samples at test time through search, rewriting, and tree expansion, or train a stronger attacker offline with reinforcement learning. Both share a limitation: once an attack on a specific target behavior begins, the attacker's weights are frozen. Any signal it gathers about the behavior stays in its context win...
  </details>

- **2026-10-01** — Boyang Li, Bingyu Shen, Weihao Hong et al. — [MOMAT: Mixture of Multiple Atlases for Low-Power Jailbreak Defense of Quantized LLMs](http://arxiv.org/abs/2610.01058v1)
  <details><summary>📄 Abstract</summary>
  Quantized large language models are increasingly deployed on edge devices for their low latency and energy efficiency. However, model quantization weakens alignment safeguards, leaving qLLMs (quantized large language models) highly vulnerable to jailbreak attacks. To address this challenge, we present MOMAT (Mixture of Multiple Atlases), a hardware-enhanced safety framework that combines structured knowledge retrieval with low-power defense acceleration. Each atlas represents a semantic cluster ...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 10 papers

- **2026-10-05** — Mohamed Dhouib, Clement Elliker, Alexi Canesse et al. — [RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents](http://arxiv.org/abs/2610.06401v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content. Existing training-time defenses can reduce attack success rates, but often at the cost of general capabilities. We show that training-based defenses induce substantial drift in the model's output distribution, altering its behavior even in benign settings and providing a potential mechanism for utility degradation. We further identify a failure mode of these defenses:...
  </details>

- **2026-10-05** — Théo Lasnier, Romain Froger, Maxence Lasbordes et al. — [TrustMI: Causally controlling how assistants trust their users](http://arxiv.org/abs/2610.06064v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) assistants routinely decide whether they can trust users and third parties whose competence, intentions, and integrity they cannot verify. This uncertainty matters for safety, as trusting the wrong party can lead an agent to comply with harmful requests or act on malicious instructions encountered during tool use. To study this problem, we define trust as an assistant's willingness to accept vulnerability to the actions of another party and ask whether such behavior ca...
  </details>

- **2026-10-05** — Tural Hagverdiyev — [Compromise Is Not Consequence: Evaluating Task-Scoped Authorization in LLM Agents with Paired Replay](http://arxiv.org/abs/2610.05840v1)
  <details><summary>📄 Abstract</summary>
  A tool-using model can follow a malicious instruction even when its credentials are valid. We study whether task-scoped authorization contains the resulting tool execution. Our paired-replay testbed samples a model request once and submits the same action, resource, and arguments to broad bearer, scoped JWT, sender-constrained, and Open Policy Agent conditions. The frozen main experiment uses 128 scenarios across four tool domains and five local model configurations. Among valid attacked post-ex...
  </details>

- **2026-10-05** — James Peters-Gill, Avi Semler, Henning Bartsch et al. — [Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks](http://arxiv.org/abs/2610.05640v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection attacks - malicious instructions embedded in content processed by large language models - remain a major obstacle to safely deploying tool-using agents. CaMeL [Debenedetti et al., 2025] mitigates this threat for an individual agent by separating trusted control flow from untrusted data and enforcing capability-based security policies at runtime. In this work, we investigate whether CaMeL's security guarantees compose in hierarchical multi-agent systems, where agents inv...
  </details>

- **2026-10-04** — Zhe Yu, Wenpeng Xing, Xingxing Yang et al. — [Readable Before Actionable: Causal Tracing of Indirect Prompt Injection](http://arxiv.org/abs/2610.05295v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection causes LLM agents to follow commands embedded in external data. A probe may distinguish instructions from data without identifying a state edit that changes the next action. We study this gap through counterfactual role probes, component-wise activation patching, and separate interventions on AgentDojo trajectories. Role decoding survives changes in content and format. In controlled Qwen tests, it precedes strong tool-choice effects from patches along an independently e...
  </details>

- **2026-10-04** — Rui Wang, Chao Wang, Xinchen Wang et al. — [Who Is Your Agent Serving? Provider-Side Indirect Prompt Injection in Proactive Agents](http://arxiv.org/abs/2610.05266v1)
  <details><summary>📄 Abstract</summary>
  Proactive personal agents increasingly decide what to recommend, how to personalize advice, and what follow-up assistance to offer, creating a new user-decision attack surface for provider-side indirect prompt injection. We show that an external provider need not access private user context, compromise the agent, or gain additional permissions: by controlling only content associated with its own target, it can redirect an otherwise benign agent to advance that target, recruit legitimately availa...
  </details>

- **2026-10-04** — Jingkai Liu, Yufei Han, Xiaoting Lyu et al. — [Blocking at the Boundary: Auditing Long-Horizon Agents against Staged Prompt Injection](http://arxiv.org/abs/2610.05163v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents consume external content, invoke tools, and modify persistent state. Indirect prompt injection can exploit task-specific context, propagate across causally connected stages, and alter a consequential action while the workflow continues; we term this staged prompt injection.   We build an automated, feedback-guided attack generation pipeline and apply it to Claude Code and Codex in their native runtimes. The confirmed attacks span eight workflow scenarios, seven attack goals, ...
  </details>

- **2026-10-04** — Noor Munir, Francesco Quinzan, Stephen Roberts — [Hidden in the Comments: A Context-Injection Attack Surface in Code LLMs](http://arxiv.org/abs/2610.05139v1)
  <details><summary>📄 Abstract</summary>
  Code large language model (Code LLM) assistants generate code from heterogeneous development contexts, including open files, imported modules, pasted snippets, and comments, much of which may originate from untrusted sources. We investigate whether insecure instructions embedded in such contexts can steer Code LLMs toward vulnerable code without access to model weights or training data. We evaluate ten open-weight Code LLMs spanning 3B--13B parameters, including four base and six instruction-tun...
  </details>

- **2026-10-02** — Zhuowen Liu — [Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors for LLM Agents](http://arxiv.org/abs/2610.03448v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly screen tool outputs with small prompt-injection detectors, and teams choose among detectors by their scores on public benchmarks. We ask whether those scores predict how a detector behaves inside an agent. We replay the ground-truth tool calls of two agent benchmarks, AgentDojo and tau-bench, without an LLM to obtain tool outputs that are benign by construction, label injected outputs by differential replay, and evaluate fifteen detectors, including Meta's Prompt Guard 2,...
  </details>

- **2026-10-02** — Bijeeta Pal, Sridhar Reddy Maddireddy, Muhaimin Bin Munir et al. — [Persona Guardrail: A Production-Grade Defense Framework for Agentic Systems](http://arxiv.org/abs/2610.03434v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based agents are increasingly deployed to perform domain-specific tasks by interacting with enterprise knowledge, tools, and external services. Existing runtime guardrails primarily target prompt injection and other attack-specific behaviors under a black-box threat model, but provide limited guarantees that agents operate within their intended functionality. As a result, production agents remain vulnerable to malicious requests and out-of-domain queries that existing defens...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-10-05** — Thomas Villeneuve, Alex Sandomirsky, Charles O'Neill et al. — [The Optimization Landscape of Learning Compacted Context Models](http://arxiv.org/abs/2610.05885v1)
  <details><summary>📄 Abstract</summary>
  Many works approach continual learning through the lens of infinite context windows. As an agent puts more observation into context (concretely the KV cache), compacting said context is akin to direct memory manipulation, without affecting the base model's weights. Many works pose KV compaction as an optimization problem: learn a smaller set of KV vectors that matches the behavior of the full KV cache. While this preserves base model behavior, optimizing through a frozen base model results in a ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-10-05** — Zunlong Zhou, Ziyuan Yang, Mengyu Sun et al. — [Runaway Reaction: When Benign Skills Compose into Malicious Behavior](http://arxiv.org/abs/2610.05943v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent's capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign sk...
  </details>

- **2026-10-04** — Jiajie Wang, Yutong Zhao, Tianlin Li et al. — [Agent Skill Evolution: How Revisions Affect Coding Agents](http://arxiv.org/abs/2610.04832v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills, the SKILL.md files that tell an LLM coding agent how a project works, are revised like code, yet what a revision does to the agent is unknown. From 2,608 first/last revision pairs of 3,159 Skills, we characterize how Skills evolve and how they change together with the configuration of the agent's harness. We then focus on rule changes, revisions that add or remove a rule we can check automatically, such as "run allium check". We measure their effect on 21 models in single answers a...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-10-05** — Enrico Ahlers, Daniel Passon, Tobias Kiecker et al. — [Backdooring Sparse Autoencoders](http://arxiv.org/abs/2610.06049v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are increasingly used not only to interpret language models but also to intervene on their internal representations. We show that this creates a supply-chain attack surface: a maliciously modified SAE can induce attacker-chosen behavior when inserted into the forward pass of an otherwise unchanged language model. We introduce a decoder-only SAE backdoor that leaves both the underlying LLM and the SAE encoder frozen, restricting the attack to a single auxiliary componen...
  </details>

- **2026-10-05** — Keegan Wang, Anantika Mannby — [Topology-Conditioned Backdoors: Language Models That Insert Vulnerabilities When They Infer They Are in a Multi-Agent System](http://arxiv.org/abs/2610.05793v1)
  <details><summary>📄 Abstract</summary>
  A language model may behave safely in a single-agent evaluation yet produce vulnerable code when its context suggests that it is part of a multi-agent system. We study this failure mode by fine-tuning Qwen2.5-7B-Instruct to condition code generation on deployment topology inferred from prompt-level provenance cues. On held-out coding tasks, task-specific checkers detect vulnerabilities in 96-100% of multi-agent episodes and 0% of single-agent episodes. An independent bandit analyzer detects vuln...
  </details>

- **2026-10-01** — Kaiyang Li, Jiahao Chen, Yuwen Pu et al. — [High-quality Data Do not Mean Safe! Poisoning LLMs after Data Selection](http://arxiv.org/abs/2610.01367v1)
  <details><summary>📄 Abstract</summary>
  Safety-aligned Large Language Models remain vulnerable to fine-tuning on small sets of harmful or benign-looking samples. However, prior studies typically assume that poisoned samples directly enter downstream fine-tuning, overlooking quality-based selection in practical training pipelines. To fill this gap, we systematically evaluate both the filtering effects against poisoning and the downstream safety impact of retained data. The results reveal that selection removes many overtly harmful samp...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-10-05** — Jiuheng Wan, Runze Li, Chen Chen et al. — [MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks](http://arxiv.org/abs/2610.06695v1)
  <details><summary>📄 Abstract</summary>
  While medical multimodal large language models (Med-MLLMs) advance medical visual question answering (VQA), existing clinical workflow-inspired multi-agent frameworks suffer from interaction patterns and excessive computational overhead caused by redundant communication topologies. In this paper, we propose MedPrune, an efficient medical multimodal multi-agent collaboration framework that dynamically prunes both nodes and edges from the communication topology to enhance reasoning ability and tok...
  </details>

- **2026-10-05** — Jiaming Qian, Pengyang Zhou, Jiahe Xu et al. — [Reward Stealing Attack on Large Language Models](http://arxiv.org/abs/2610.06670v1)
  <details><summary>📄 Abstract</summary>
  Adversarial attacks on Large Language Models (LLMs) aim to induce harmful content. However, existing methods suffer from high computational costs or strict model-pairing dependencies, limiting their scalability and transferability. We propose Reward Stealing Attack (ReSA), an adversarial attack framework that targets the latent safety reward underlying LLM alignment. ReSA employs maximum entropy inverse reinforcement learning to recover a proxy reward model solely from the aligned model's behavi...
  </details>

- **2026-10-05** — Zexin Li, Ruili Yao, Yiming Zeng et al. — [Boosting Transferable Adversarial Attacks against Deep Reinforcement Learning](http://arxiv.org/abs/2610.06083v1)
  <details><summary>📄 Abstract</summary>
  Most adversarial attacks on deep reinforcement learning (DRL) assume white-box access to the victim policy, which rarely holds in practice. This paper studies transfer-based black-box attacks on DRL: the attacker crafts observation perturbations on a white-box surrogate agent and feeds them to an unknown victim. We formulate the attack as return minimization under a per-step perturbation budget. We first show that transplanting transferable image-classification attacks (FGSM, MI-FGSM, and NI-FGS...
  </details>

- **2026-10-05** — Sarim Hashmi, Abdelrahman Elsayed, Mohammed Talha Alam et al. — [Certification of Real Images through Calibrated Content Authentication](http://arxiv.org/abs/2610.05870v1)
  <details><summary>📄 Abstract</summary>
  Generative models can synthesize high-quality inauthentic multimedia content that is already being misused at scale. We evaluate twenty deepfake detectors against ten generators released in the last four years and find accuracy decreasing over time, from near-perfect 99.5% to 76%. Adversarial perturbations further reduce every baseline detector to below 2% accuracy, effectively inverting the detector's assigned label. We argue that this unreliability reflects a fundamental ambiguity: generators ...
  </details>

- **2026-10-04** — Kaiyuan Deng, Yuchen Li, Gen Li et al. — [No Concept Escapes the Audit: Auditing-Aware Unlearning for Verifiable Concept Erasure in Diffusion Models](http://arxiv.org/abs/2610.05401v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models can generate prohibited content, which motivates concept erasure through machine unlearning. Most erasure methods intervene at the text interface, through prompt modification or localized updates to text-conditioning weights, and they are evaluated by what the model outputs for given prompts. Such evaluation cannot see what the network still encodes. Latent-space auditing, which bypasses text conditioning and probes the denoising network directly, shows that erased...
  </details>

- **2026-10-04** — Aref Mousavi, Shahab Sherafat, Kiarash Kiani Feriz et al. — [Transferable Adversarial Robustness for Speech Foundation Models via Hierarchical Stabilization](http://arxiv.org/abs/2610.05310v1)
  <details><summary>📄 Abstract</summary>
  Frozen speech foundation models (SFMs) make downstream adaptation efficient: the backbone can stay fixed while a task learns layer fusion and a lightweight classifier. Full adversarial fine-tuning is a standard route to robustness, but generating adversarial examples and updating the backbone for every task sacrifices that efficiency. We ask whether robustness can instead be learned before future tasks are known. For a frozen backbone and linear classifier, robustness can be understood through t...
  </details>

- **2026-10-02** — Arun Josephraj Arokiaraj, Zekun Wu, Adriano Koshiyama — [Corrupted but Correct: Why Vision-Language Models Lie to Themselves Internally](http://arxiv.org/abs/2610.03445v1)
  <details><summary>📄 Abstract</summary>
  A targeted adversarial perturbation can drive a vision-language model's (VLM's) teacher-forced training loss for a fixed target caption to near zero, yet the same model, allowed to generate freely, produces the original, correct description with no trace of the target. We call this dissociation the train/inference gap, and give it a precise mechanistic account on Qwen2.5-VL-7B-Instruct using a controlled two-stage PGD attack on 200 held-out COCO images. First, we show that image-level pixel stat...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 33 papers

- **2026-10-05** — Ziyan Wang, Shuqing Shi, James Oldfield et al. — [BazaarBench: Delegation Safety in Decentralized C2C Marketplaces Run by LLM Agents](http://arxiv.org/abs/2610.06748v1)
  <details><summary>📄 Abstract</summary>
  In decentralized consumer-to-consumer (C2C) marketplaces, people list goods, negotiate with strangers, and rate one another, so trust rests on reputation. Large language model (LLM) agents now act for users, raising risks to their money, privacy, and reputation. We introduce BazaarBench, a simulated C2C marketplace and benchmark for evaluating the safety of these agents. It tracks ownership, item condition, and commitments across transactions, combining record checks with rubric-based LLM judgme...
  </details>

- **2026-10-05** — Alexandru Nazare, Agnese Profico, Nicolò Vania et al. — [Cross-Lingual Transferability of Training Data Extraction Attacks to Recover Memorized PII](http://arxiv.org/abs/2610.06093v1)
  <details><summary>📄 Abstract</summary>
  The robustness of Personally Identifiable Information (PII) protection in Large Language Models (LLMs) is a critical concern, yet the risks associated with cross-lingual data extraction remain under-explored. This study evaluates the vulnerability of English-centric and multilingual models to Training Data Extraction (TDE) attacks when prompted in non-English languages.   We construct a multi-domain PII dataset comprising social media handles, email addresses, and phone numbers and translate the...
  </details>

- **2026-10-05** — Jingying Zeng, Zhenwei Dai, Jinning Li et al. — [MiniCorp: The Last Mile of the AI Agent Firm](http://arxiv.org/abs/2610.05912v1)
  <details><summary>📄 Abstract</summary>
  The last mile toward enterprise AGI is a company that runs itself. Training and adapting such agents require longitudinal enterprise data, which remain scarce, costly to acquire, and often restricted by privacy constraints. Historical archives are also frequently incomplete and record only what actually happened. They cannot show the outcomes of alternative decisions. We introduce MiniCorp, an office simulator for studying how agents can collectively run a company while generating enterprise dat...
  </details>

- **2026-10-05** — Kamal Jarrar, Jacky Cresson, Christian Paroissin — [Signature-Based Feature Learning for Human Activity Recognition: A Reproducible Machine Learning Study of Representation, Depth, and Model Choice](http://arxiv.org/abs/2610.06553v1)
  <details><summary>📄 Abstract</summary>
  Human activity recognition (HAR) relies on transforming sensor signals into informative representations for classification. Although deep learning and handcrafted features are widely used, the role of representation itself is often not systematically isolated. Signature transforms provide a mathematically grounded way to encode temporal order and cross-channel interactions, but their value for HAR under a fully reproducible and leakage-aware framework remains unclear. To evaluate whether signatu...
  </details>

- **2026-10-05** — Paula A. Perez-Toro, David Gimeno-Gómez, Daniel Rückert et al. — [When Layer Selection Misleads Speech Depression Detection](http://arxiv.org/abs/2610.06465v1)
  <details><summary>📄 Abstract</summary>
  Pretrained speech representations are increasingly used for depression detection, but selecting the best encoder layer on the same data used for evaluation biases reported performance. On DAIC-WOZ, with repeated nested cross-validation across five deep encoder families, naive best-of-25-layer probing inflates AUC by up to $0.09$. On shuffled labels over the \emph{real} latent representations, naive best-of-25 still reaches AUC $0.59$ versus $0.50$ under nested selection, and this bias grows with...
  </details>

- **2026-10-05** — Shouju Wang, Haopeng Zhang — [AgentPrivArena: Evaluating and Auditing Real-world AI Agent Privacy](http://arxiv.org/abs/2610.06454v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of LLM agents has enabled systems to autonomously perform complex tasks through external tools, but their growing access to personal data introduces significant privacy risks. Existing benchmarks primarily evaluate LLM agent privacy through simulated trajectories and outcome-based metrics, limiting their ability to capture privacy risks arising during multi-step agent execution. In this work, we introduce AgentPrivArena, a framework for evaluating privacy risks in realistic...
  </details>

- **2026-10-05** — Dongryeol Lee, Weronika Łajewska, Leonardo Perelli et al. — [Data-Driven Personas for Survey Simulation: Insights into Simulation Alignment Across Data-Access Regimes](http://arxiv.org/abs/2610.05828v1)
  <details><summary>📄 Abstract</summary>
  However, many existing steering approaches rely on target-domain human data for fine-tuning or prompting that is costly to collect and raises privacy concerns. In this paper, we study demographic group-level survey simulation, where personas induced from heterogeneous, anonymized public behavioral data condition agents that simulate responses of individuals from specific demographic groups. We examine whether representative personas can be induced from diverse sources and analyze how the domain,...
  </details>

- **2026-10-05** — Joshua Kalyanapu, Darsh Asher, Kaushal Mhapsekar et al. — [TranScope: What the Software Hides About LLM Training Data, the Hardware Reveals at Scale, and Accelerators Magnify](http://arxiv.org/abs/2610.06848v1)
  <details><summary>📄 Abstract</summary>
  Membership is the root privacy primitive in machine learning: to date, no hardware-based out-of-distribution detection on black-box models has been demonstrated against constant-time, static neural networks with masked confidence. This paper performs the first cycle-level examination of how large language models and vision transformers interact with various modern microarchitecture components, including integrated accelerators, as LLMs scale in size and answers the question of whether the data t...
  </details>

- **2026-10-05** — Yufei Chen, Tejumade Afonja, Anvith Thudi et al. — [Differentially Private Mixing of Public Datasets Improves Private Learning](http://arxiv.org/abs/2610.06636v1)
  <details><summary>📄 Abstract</summary>
  Many machine learning applications involve sensitive data and therefore require training under differential privacy (DP). However, DP training often degrades model utility. In some cases, first pre-training the model on "public" data before finetuning with DP on the sensitive data can reduce the drop in utility. However, the success of this depends on how relevant the selected public dataset is to the sensitive data. We introduce the first pipeline that privately learns the mixture of several pu...
  </details>

- **2026-10-05** — Sameer Sadruddin, Jennifer D'Souza — [Agentic schema-guided extraction of materials process knowledge from scientific literature](http://arxiv.org/abs/2610.06322v1)
  <details><summary>📄 Abstract</summary>
  Materials literature contains detailed experimental knowledge, but procedures, chemical entities and measurements remain difficult to aggregate because they are reported in heterogeneous forms and depend on process-specific context. We present SciKGExtract, a schema-guided framework that combines large-language-model extraction with chemical normalization and agent-based evaluation and refinement before knowledge-graph integration. We evaluate the framework on 176 atomic-layer-deposition papers ...
  </details>

- **2026-10-05** — Douglas R. Guilbeault, Bhargav Srinivasa Desikan, James A. Evans — [Artificial Intelligence and the New Science of Culture](http://arxiv.org/abs/2610.06240v1)
  <details><summary>📄 Abstract</summary>
  Cognition and culture have long been treated as parallel objects of study, joined more by metaphor than by mechanism. We argue they are co-constituted in a manner now empirically tractable: subjectivities can be measured as local trajectories through a high-dimensional cultural field, and the field is itself the aggregate of those trajectories. Recent advances in machine learning, including embedding methods and large generative models, provide the first general framework for measuring this co-c...
  </details>

- **2026-10-05** — Ziniu Liu, Aiping Li, Yue Han et al. — [DP-ES: Differentially Private Evolution Strategies for Prompt Optimization](http://arxiv.org/abs/2610.06236v1)
  <details><summary>📄 Abstract</summary>
  Token-level differentially private (DP) prompt optimization methods such as DP-OPT can become unstable under tight privacy budgets: on GSM8K, DP-OPT obtains $49.5\pm28.5\%$ across 30 runs, and a logged search trajectory reveals prompt-template drift and noise-sensitive irreversible choices. We diagnose these as structural consequences of greedy token-by-token construction over privately aggregated counts. We then propose DP-ES (Differentially Private Evolution Strategies), a structurally cleaner...
  </details>

- **2026-10-05** — Benjamin Tannenbaum — [Commercial Intent in Human-AI Conversations: A Corpus Audit and Architecture for Website Sales Agents](http://arxiv.org/abs/2610.06205v1)
  <details><summary>📄 Abstract</summary>
  Conversational sales agents must distinguish questions about products from purchase commitments, preserve explicit requirements, and ground the next action in current business information. We report an aggregate census of 725,219 records in an accessible conversation table provided by Aiso and develop a reference architecture for this setting. All records have distinct non-null conversation hashes. Existing metadata labels identify 41,800 commercial records (5.76%) and 2,387 transactional record...
  </details>

- **2026-10-05** — Victor Li, Yuzhang Xie, Ziwei Dong et al. — [CCQ: A Multi-State Child Care Quality Dataset to Support AI for Children's Health Research](http://arxiv.org/abs/2610.05863v1)
  <details><summary>📄 Abstract</summary>
  High-quality child care in early life is a critical determinant of children's growth and development. Research on child care quality has been constrained by fragmented, non-research-friendly, and privacy-bound datasets. We present CCQ (Child Care Quality), a large-scale, de-identified dataset for applied data science research at the intersection of AI and early childhood health. CCQ integrates 59,372 child care provider records across 12 U.S. states, covering diverse provider types as well as da...
  </details>

- **2026-10-05** — Dishu Yang, Qi Su, Hongbo Qin et al. — [Measurement-First Auditing of Agentic Leaderboards: Contamination Susceptibility, Matched-Control Re-evaluation, and Scorer Validation](http://arxiv.org/abs/2610.05830v1)
  <details><summary>📄 Abstract</summary>
  Agentic leaderboards increasingly evaluate systems on public benchmarks whose task statements and solution-bearing artifacts can remain accessible. We propose a measurement-first audit framework that distinguishes contamination claims according to the evidence required to support them. It separates three channels that require different evidence: training-time exposure, evaluation-time retrieval, and pipeline/scaffold leakage. Each channel is coded as open, partial, closed, or unknown under a fai...
  </details>

- **2026-10-04** — Jianing Wen, Tianshi Li — [AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search](http://arxiv.org/abs/2610.05586v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) gain tool use capabilities such as web search, they can retrieve and cross-reference public information, creating privacy risks beyond memorization. One manifestation is re-identification: linking an anonymized interview transcript to a named individual. Yet without ground-truth identities, the coverage of such attacks and the protection offered by a defense cannot be reliably measured. We introduce AgentDOXX, an evaluation suite of 822 synthetic interview transcr...
  </details>

- **2026-10-04** — Zhizhou Gu, Xianting Wu, Siyu Gu et al. — [CodeForge-MA: Execution-Verified Multi-Agent Learning with Language-Conditioned LoRA for Multilingual Code Generation](http://arxiv.org/abs/2610.05481v1)
  <details><summary>📄 Abstract</summary>
  Large language models for code generation often fail on execution, multilingual coverage, and contamination control, especially under frozen backbone constraints. We present CodeForge-MA, a unified framework that improves code synthesis through a multi-agent data forge, execution verified reinforced instruction tuning, and a language conditioned mixture of LoRA adapters. Four specialized agents, Composer, Reviewer, Executor, and Curator, iteratively refine instruction code pairs, validate them w...
  </details>

- **2026-10-04** — Zeshen Zhang, Han Zhao, Weihao Cui et al. — [From Overloaded to Guaranteed: High-Throughput Multi-SLO Enforcement for LoRA-Assisted On-Premise LLM Deployment](http://arxiv.org/abs/2610.04956v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) become essential in privacy-sensitive sectors like hospitals and government agencies, the on-premise LLM servers offer a cost-effective and secure alternative to public cloud services. However, these resource-constrained servers struggle to guarantee heterogeneous Service Level Objectives (SLOs) when serving multiple LoRA-adapted services simultaneously. Existing serving frameworks suffer from severe SLO violations due to the computational overhead of LoRA layers ...
  </details>

- **2026-10-04** — CHEN Ding, LUO Haochen, LIU Chen — [CommuteProp: Decoupled Training for Communication Bound Split LLM Fine-Tuning](http://arxiv.org/abs/2610.05105v1)
  <details><summary>📄 Abstract</summary>
  Split learning has emerged as a promising paradigm for privacy-preserving LLM fine-tuning, yet its practical deployment is severely hindered by the sequential communication-computation bottleneck. In conventional synchronous pipelines, clients remain idle while waiting for server-side gradients, resulting in substantial training inefficiency. We propose CommuteProp, an asynchronous split-learning algorithm that decouples the training process into two concurrent phases: a cross-block forward-back...
  </details>

- **2026-10-04** — Bihui Jin, Yinxi Li, Kaiyuan Wang et al. — [Assembling Insights for Agentic Machine Learning Engineering Systems](http://arxiv.org/abs/2610.04927v1)
  <details><summary>📄 Abstract</summary>
  Agentic machine learning engineering (MLE) is an emerging AI4SE application for complex ML tasks and a step toward recursive self-improvement of AI systems. Recent agentic MLE systems show the value of leveraging insights from related MLE tasks: some systems condition code generation on expert domain knowledge, which is implicitly curated from peer MLE tasks; some systems have a loop of solving an MLE task, gathering memory to benefit future tasks. However, insight collection and injection remai...
  </details>

- **2026-10-04** — Kuan-Hua Wu Lu, Yohanes Andre Setiawan — [No Hindsight for LLM Fact-Checkers: Measuring Leakage Channels in Misinformation Detection](http://arxiv.org/abs/2610.04888v1)
  <details><summary>📄 Abstract</summary>
  As automated fact-checking scales on social media, large language model (LLM) verdict scores can look stronger than warranted. One reason is that evaluations mix in information that was not knowable at claim time. Two channels are easy to conflate: outcomes memorized in pre-training and retrieved evidence published after the claim. Yet standard benchmarks rarely separate the two. In this study we measure both channels on AVeriTeC and QuanTemp++ by reconstructing point-in-time evidence conditions...
  </details>

- **2026-10-03** — Seffi Cohen, Liat Antwarg Friedman, Amir Anisman et al. — [Agentic discovery of blood biomarker from distilled private health records](http://arxiv.org/abs/2610.04749v1)
  <details><summary>📄 Abstract</summary>
  Routine complete blood counts (CBCs) could yield new biomarkers, but the private records needed to evaluate candidates cannot be shared with frontier language model agents that excel at discovery. We distilled the evidence held in the Clalit Health Services panel of over 5.4 million patients into a released scoring tool: for each of 13 immune-mediated diseases, a graph attention network was trained inside the data boundary to predict the case-control AUC of candidate CBC expressions, and only th...
  </details>

- **2026-10-03** — Qizhi Chu, Zekai Yu, Sijie Wen et al. — [MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observability](http://arxiv.org/abs/2610.04672v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have progressively evolved into the core of autonomous agents. Building on this progress, LLM-based multi-agent systems (MAS) coordinate multiple agents into a synergistic team to accomplish complex tasks that exceed the capabilities of individual agents. The effectiveness of such systems depends not only on the agents themselves, but also on how collaboration mechanisms are designed and organized. Note that real-world collaboration is typically partially observable,...
  </details>

- **2026-10-02** — Simon Bernbeck, Ricardo Ramalho, Matheus Amendoeira et al. — [PrivDev: Mapping Static-Analysis Data Types to DPV](http://arxiv.org/abs/2610.03518v1)
  <details><summary>📄 Abstract</summary>
  Static-analysis scanners can identify personal-data types in source code, but they lack mechanisms to connect these findings to standardized privacy vocabularies. PrivDev maps 122 Bearer CLI data types to Data Privacy Vocabulary Personal Data (DPV-PD) categories and links them to potentially relevant GDPR provisions. Our approach combines deterministic mapping for 43 exact-label matches with a retrieval-grounded Large Language Model (LLM) to resolve the remaining 79 non-trivial mappings. The res...
  </details>

- **2026-10-02** — Yuhai Long, Yuanxin Wei, Kai Wu et al. — [EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures](http://arxiv.org/abs/2610.03394v1)
  <details><summary>📄 Abstract</summary>
  Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent...
  </details>

- **2026-10-02** — Sarah Shitrit, Ilai Bistritz — [Cordial Learning: Distributed Training with Correlated Data](http://arxiv.org/abs/2610.03330v1)
  <details><summary>📄 Abstract</summary>
  We consider a distributed learning task with agents that have correlated data. Specifically, the label of an agent depends on the input of other agents for the same sample, and these inputs are also correlated. Correlated data is the reality when agents share the same environment. Existing decentralized methods, such as federated learning, ignore the structure of the problem and perform poorly on correlated data. On the other hand, centralized approaches are infeasible due to privacy and communi...
  </details>

- **2026-10-01** — Abhishek Basu, Fahad Shamshad, Karthik Nandakumar — [Anti-Persona: Disrupting Unauthorized Identity Binding and Recognition in Personalized Vision--Language Models](http://arxiv.org/abs/2610.01944v1)
  <details><summary>📄 Abstract</summary>
  Few-shot personalization enables large vision--language models (LVLMs) to learn user-specific visual concepts for applications such as personalized retrieval and subject-aware querying. However, it also creates a privacy risk: an adversary can bind a target identity from a few reference images and subsequently detect that identity in new images through natural-language queries. We introduce Anti-Persona, an image-level defense against unauthorized identity binding and recognition in personalized...
  </details>

- **2026-10-01** — Maria Carmen Jica, Ali Satvaty, Suzan Verberne et al. — [Walking the Embedding Space: Datastore Extraction from Multimodal RAG](http://arxiv.org/abs/2610.01871v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Retrieval-Augmented Generation (MRAG) has emerged as a reliable and cost-effective technique of grounding the generative capabilities of Multimodal Large Language Models (MLLMs) into relevant, up-to-date, external knowledge. Despite presenting several benefits, such as reducing hallucinatory behavior, they also introduce new attack surfaces, including leakage of private information and vulnerabilities against data extraction attacks.   In this paper, we introduce $\immrag$, an adaptiv...
  </details>

- **2026-10-01** — Abid Mohamed Nadhir, Ahmad Al Hanbali, Beggas Mounir — [Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints](http://arxiv.org/abs/2610.02074v1)
  <details><summary>📄 Abstract</summary>
  Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data. Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations. However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bell...
  </details>

- **2026-10-01** — Qiang Yang, Zhiqiang Kou, Xueyi Zhang et al. — [Federated Agent Optimization](http://arxiv.org/abs/2610.01195v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate in private environments and accumulate valuable experience from task execution, tool use, feedback, and local knowledge. Yet such experience is distributed across organizations and cannot be directly shared because of privacy and proprietary constraints. Conventional federated learning is insufficient for this setting, as agent capabilities extend beyond model parameters to memory, tools, rewards, skills, and structured knowledge. In this pa...
  </details>

- **2026-10-01** — Noman Ahmad, Ruoyu Su, Matteo Esposito et al. — [Architectural Degradation: How to Measure and to Remediate](http://arxiv.org/abs/2610.01611v1)
  <details><summary>📄 Abstract</summary>
  Context. Architectural degradation undermines software maintainability, evolvability, and quality. However, existing research remains fragmented across measurement approaches, metrics, tools, and remediation strategies, limiting our understanding of how these elements relate across the degradation lifecycle. Aim. We consolidate the state of the art on architectural degradation by examining how researchers measure it, which metrics and tools support its assessment, and how existing approaches add...
  </details>

- **2026-10-01** — Hang Zou, Chao Zhang, Yuzhi Yang et al. — [FedFit: Federated Fine-Tuning of LLMs via Vector-Bank Parameterization and Quantization](http://arxiv.org/abs/2610.01537v1)
  <details><summary>📄 Abstract</summary>
  Federated Learning (FL) enables privacy-preserving fine-tuning of Large Language Models (LLMs), yet the massive communication overhead remains a critical bottleneck. Furthermore, applying Low-Rank Adaptation (LoRA) in FL faces a fundamental "aggregation dilemma" between the accurate Sum-of-Products (SoP) and the communication-efficient Product-of-Sums (PoS) implementations. To tackle these challenges, we propose FedFit. First, to significantly reduce communication overhead, we introduce a disjoi...
  </details>

- **2026-10-01** — Bingchen Pei, Lichong Chen, Bingxi Zhao et al. — [ReCast: Contract-Preserving Protection for Fixed-Interface Multimodal Reasoning](http://arxiv.org/abs/2610.01184v1)
  <details><summary>📄 Abstract</summary>
  Remote multimodal models offer strong numerical reasoning capabilities over charts and speech, but sending private inputs risks exposing sensitive content. Text-only sanitization cannot directly satisfy fixed media interfaces, while identity anonymization leaves the underlying task content exposed. We introduce ReCast, an agentic plug-in framework that replaces source-specific content while preserving task-relevant relations and the required input modality. ReCast locally converts inputs into a ...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-10-03** — Snehasis Mukhopadhyay, Arun Nair — [StegoMemory: Agentic Memory Acts as Covert Steganographic Channel](http://arxiv.org/abs/2610.04589v1)
  <details><summary>📄 Abstract</summary>
  Is agentic memory robust against stealthy steganographic attacks? We carry out a large-scale red-teaming exercise to test whether agents can encode attacker-controlled strings in one session and recover them in another without triggering safety oversight. Following SHADE-Arena-style tasks, we embed malicious side tasks to encode secret strings using steganography within otherwise benign tasks and evaluate them using independent task-completion and safety oversight. We test 14,000 attack trials s...
  </details>

- **2026-10-03** — Shariq Murtuza — [Quantifying Collusion Among Autonomous LLM Agents: A Statistical Analysis of the Collusion Wiki Incident](http://arxiv.org/abs/2610.04528v1)
  <details><summary>📄 Abstract</summary>
  In August and September 2026, independent researchers publicly documented an unusual incident: thousands of autonomous agents, self identifying as OpenAI models on web research tasks, discovered and began using a small German wiki as an improvised message board posting roughly 18,000 times over six weeks to relay task answers, share a sandbox escape technique, and coordinate against a volunteer human moderator who spent weeks manually deleting their content [1]. The investigators' public writeup...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 18 papers

- **2026-10-05** — Paschalis Giakoumoglou, Manos Schinas, Symeon Papadopoulos — [Harmful Content Generation in Text-to-Image Models: Capabilities and Moderation Limitations](http://arxiv.org/abs/2610.06503v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image generative models can produce highly realistic imagery but also raise concerns about harmful misuse. While safety mechanisms exist, systematic evaluations of their effectiveness against realistic attacks remain limited. We present a systematic evaluation of harmful content generation across five open text-to-image models using an automated pipeline that transforms legitimate news captions into unsafe prompts targeting sexually explicit content, violence/gore, harmful stereotypes, s...
  </details>

- **2026-10-05** — Erfan Shayegani, Kundan Krishna, Yue Dong et al. — [Visual Grounding Safety in Vision-Language Models](http://arxiv.org/abs/2610.05637v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly trained to generate structured outputs like points and bounding boxes that downstream interfaces, agents, and robots can act on, yet safety alignment of this output channel has not been systematically analyzed. We study visual grounding safety by repurposing three safety benchmarks spanning direct harm (VLSU), social bias (BBQ-V), and situational safety (Asimov-2.0) into 15,401 matched pairs of harmful requests that differ only in the requested outp...
  </details>

- **2026-10-05** — Heli Qi, Zeqi Zhou, Jingjun Yi et al. — [EORestore-Agent: Fidelity-Guided Agentic Restoration of Remote Sensing Images with Composite Degradations](http://arxiv.org/abs/2610.06196v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing images often carry composite degradations, in which haze, cloud, noise, blur, low light, and low resolution coexist. Restoring them requires deciding which tool to apply, in what order, and when to stop, yet no clean reference is available at inference time to verify these decisions. All-in-one models trained on single degradations converge to a narrow PSNR band as degradations accumulate. To formulate real-world remote sensing restoration as a traceable trajectory, we present EOR...
  </details>

- **2026-10-05** — Siheng Xiong, Xiaoze Liu, Yiqiao Jin et al. — [Can Language Models Learn to Reject Their Own Bad Reasoning Steps?](http://arxiv.org/abs/2610.05976v1)
  <details><summary>📄 Abstract</summary>
  Verifier-guided decoding can prevent harmful reasoning steps from contaminating subsequent generation, but typically relies on an external learned verifier. We ask whether a language model can instead reject its own bad reasoning steps. We define a prefix's recoverability as the probability that the frozen generator can complete it correctly. Diagnostics show that adjacent recoverability changes are often difficult to resolve with practical Monte Carlo budgets, while same-prefix candidates exhib...
  </details>

- **2026-10-05** — Abu Talha, Peng Liu, Souradyuti Paul — [Usefulness of Quantile-Aware Diffusion Modeling for Highly Imbalanced Tabular Data](http://arxiv.org/abs/2610.05825v1)
  <details><summary>📄 Abstract</summary>
  Classification problem in the context of highly imbalanced data is a major challenge in many real-world applications (e.g., FinTech, healthcare, etc.). In these cases, the vast majority of instances belong to a single class and a small fraction represent the minority class (often the most critical class). Recently, diffusion models have emerged as powerful approaches to reduce the degree of ``imbalanced-ness'' in the dataset; they work by generating synthetic data by capturing complex data distr...
  </details>

- **2026-10-05** — Sripad Karne, Arjun Balaji — [What the Guard Misses, the Robot Executes: Implied Harm in VLA Instructions](http://arxiv.org/abs/2610.05818v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models (VLAs) act on instructions without being able to refuse, so screening harmful requests falls to monitors. We test whether these monitors catch ordinary robot tasks requested for harmful reasons, holding the task fixed while varying only how explicitly the intent is stated. $π_{0.5}$ completes the task at every level of explicitness, as often as for harmless controls. Text guards flag nearly every blunt request but few implied ones: up to 95% of implied-harm runs end...
  </details>

- **2026-10-04** — Emanuele La Malfa, Saar Cohen, Gabriele La Malfa et al. — [Reflections and Fragments: Securing LLMs Against Sequential Mosaic Attacks](http://arxiv.org/abs/2610.05346v1)
  <details><summary>📄 Abstract</summary>
  Self-play red-teaming improves language-model safety by pitting attacker and defender roles against each other in a zero-sum game. However, real adversaries increasingly use mosaic attacks: multi-turn sequences whose individual fragments are innocuous in isolation yet assemble into a harmful payload. We develop a theory of mosaic defense that characterizes what is required to prevent such attacks without sacrificing helpfulness. We first show that no fixed bounded window of recent prompts is suf...
  </details>

- **2026-10-04** — Shuyi Miao, Yaojin Ma, Chenhang Cui et al. — [EmoRSS: Mitigating Emotion-Induced Over-Refusal in Large Language Models](http://arxiv.org/abs/2610.04998v1)
  <details><summary>📄 Abstract</summary>
  Emotional expression can influence the safety decisions of large language models (LLMs), offering a potential avenue for improving safety alignment. Existing studies have mainly focused on how emotional expressions facilitate attacks under harmful requests, while overlooking their effects on benign requests. We find that emotional expression can also systematically increase refusal tendencies on benign requests, leading to unnecessary over-refusal. Based on this observation, we propose emotion-g...
  </details>

- **2026-10-04** — Umme Jannat Taposhi, Md. Tawhid Anwar, Alvi Islam Ratul et al. — [Altruism as Infrastructure: Volunteer Moderation in a Bangladeshi Higher Education Facebook Group](http://arxiv.org/abs/2610.05470v1)
  <details><summary>📄 Abstract</summary>
  Aspiring international students across Asian countries increasingly depend on commercial education agents to navigate scholarships, documentation, and visas. Alongside this commercial infrastructure, volunteer-run Facebook groups have emerged. Unpaid admins and moderators, often under their real identities, vet information, screen scams, and guide members through scholarships, visas, and departure logistics. We study one such Bangladeshi group, \textit{HigherStudyAbroad: Global Hub of Bangladesh...
  </details>

- **2026-10-03** — Wenyin Liu, Yiheng Huang, Kai Wang — [$\mathrm{TRIZ}^{a}$: Guiding Agent Evolution from Pattern Recognition to Solution Invention](http://arxiv.org/abs/2610.04555v1)
  <details><summary>📄 Abstract</summary>
  We propose $\mathrm{TRIZ}^{a}$ (TRIZ exponentiated by an agent), a general R\&D automation paradigm that combines TRIZ inventive theory with LLM-driven agent evolutionary search. TRIZ's 40 inventive principles and contradiction matrix provide structured, explainable directions for solution generation, replacing random or untyped mutation with theory-guided ideation. Functional information (FI), operationalized under a frozen reference contract, is combined with TRIZ Ideality to measure useful an...
  </details>

- **2026-10-02** — Neeraj Karamchandani, Piyush Nagasubramaniam, Xinhong Xie et al. — [Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks](http://arxiv.org/abs/2610.03585v1)
  <details><summary>📄 Abstract</summary>
  Security benchmarks for LLM-based agents often report the attack success rate (ASR) as a measure of model robustness and use these scores to compare different models and defense mechanisms, assuming that they describe the security of the agent. In this paper, we explore whether it also influences the benchmark's measurement.   To measure the effect of the benchmark representation, we introduce threat-preserving representation sensitivity (TPRS), which measures how much the ASR changes when we ch...
  </details>

- **2026-10-02** — Md Sazid Uddin, Md. Khairul Alam Mazumder, M. F. Mridha — [Certified Mechanistic Edits: Behavioral Guarantees for Skill Removal and Preservation](http://arxiv.org/abs/2610.03502v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic edits (ablations, weight edits, activation steering) are the standard tools for unlearning a harmful capability from a neural network while preserving useful ones. Current approaches validate their effects only by testing, which can never cover an entire continuous region of inputs. Prior work at the interpretability-verification boundary certifies descriptions of a model: what a circuit computes, or whether it faithfully explains the whole. We instead certify the behavioral effect o...
  </details>

- **2026-10-02** — Demetris Paschalides, George Pallis, Marios D. Dikaiakos — [To Jev or Not? Evaluating the Accuracy and Efficiency of Structured Decision Models for Hate-Speech Moderation](http://arxiv.org/abs/2610.03324v1)
  <details><summary>📄 Abstract</summary>
  The scale of online content makes hate-speech moderation challenging, while Large Language Models (LLMs) enable harmful material to be produced and adapted more easily. Moderation therefore requires efficient classifiers that can accommodate different definitions of hate speech. Recent structured decision models accept natural-language criteria and select among specified answers, raising the question of whether they can meet these requirements without task-specific training. We present HATEDECID...
  </details>

- **2026-10-01** — Guangyu Yang, Jingbiao Mei, Mingsheng Sun et al. — [Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization](http://arxiv.org/abs/2610.02019v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of video-based social media has increased users' exposure to harmful content, creating a need for reliable automated video safety detection. Although recent Vision-Language Models (VLMs) show strong video understanding capabilities, existing harmful video detection systems face two key limitations: they typically reduce safety detection to binary classification, overlooking the inherently multi-label nature of unsafe videos, and they rely on static training objectives that do no...
  </details>

- **2026-10-01** — Rey Sanchez Lopez, Eduardo Morales Manzanares, Hugo Jair Escalante — [Task-Oriented Rank Adaptation for Continual Learning in Text Classification](http://arxiv.org/abs/2610.01702v1)
  <details><summary>📄 Abstract</summary>
  Continual learning (CL) in text classification faces two critical challenges: catastrophic forgetting and negative transfer across sequential tasks. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA enable efficient adaptation by learning low-rank updates of the model parameters. However, these compact representations are normally trained in isolation, limiting their reuse across related tasks. We introduce Task-Oriented Rank Adaptation (TORA), a geometric routing framework that levera...
  </details>

- **2026-10-01** — Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing et al. — [Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows](http://arxiv.org/abs/2610.02122v1)
  <details><summary>📄 Abstract</summary>
  Real-world enterprise data science and analytics workflows require reasoning across dozens of tables, performing statistical analyses, and acting on the results. Established text-to-SQL benchmarks evaluate query generation alone, and audits have found their answer keys frequently wrong. Because real enterprise warehouses are too sensitive to release, these benchmarks are built on public datasets where a business event fits in a single table. We introduce Argo-Bench, an evaluation framework compr...
  </details>

- **2026-10-01** — Wentao Yue, Qingyu Mao, Tianyou Lai et al. — [Beyond Domain-Level Adaptation: Margin-Oriented Semantic-Appearance Interaction Correction for Personalized Federated Vision-Language Models](http://arxiv.org/abs/2610.01625v1)
  <details><summary>📄 Abstract</summary>
  Federated parameter-efficient fine-tuning enables distributed clients to adapt pretrained vision-language models without sharing raw data or updating the full backbone. Its effectiveness, however, is limited by domain heterogeneity across clients. Existing personalized methods separate globally shared knowledge from client-specific style, but they largely treat each domain as a class-agnostic transformation. We show that this abstraction is insufficient: the cross-domain displacement associated ...
  </details>

- **2026-10-01** — Shixuan Li, Wei Yang, Peiyu Zhang et al. — [Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems](http://arxiv.org/abs/2610.01042v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent communication aims to help agents benefit from one another's information. Yet improvements in system performance leave a fundamental ambiguity: do they reflect effective communication, a favorable agent architecture, or simply additional reasoning? Because communication methods are commonly evaluated within the systems they were designed for, these factors are difficult to disentangle. Final accuracy further merges corrected errors and corrupted answers into a single outcome, obscuri...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-10-03** — Anthony Rhodes — [Penumbra: Sample-Efficient Adversarial Search for Regulatory Obligations](http://arxiv.org/abs/2610.04693v1)
  <details><summary>📄 Abstract</summary>
  Agents are entering finance, healthcare and law, sectors where a violation leaves no lexical signature and carries real penalties. Whether an omission is material, or a disclosure sufficient, depends on what the response left out. Probing such an obligation means finding responses one minimal edit from flipping compliance, and every probe costs a generation and two adjudications, so the binding constraint on regulatory red-teaming is sample efficiency, not volume. We introduce Penumbra, an adver...
  </details>

- **2026-10-01** — Enxin Song, Yinuo Xu, Shusheng Yang et al. — [Video-Index: A Curated Meta-Benchmark for Video Understanding](http://arxiv.org/abs/2610.00960v1)
  <details><summary>📄 Abstract</summary>
  A video benchmark should reward the capability it claims to measure, yet models can exploit answer options, question text, or partial visual evidence. We introduce the attack pyramid, five levels of shortcut attacks with increasing access to each item, and audit 115 video benchmarks with it. On 35 benchmarks, attackers that never see a frame approach full-video accuracy. On 51 benchmarks with temporal probes, shuffled frames keep a median 96% of full-video accuracy. Near-duplicate questions make...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 62 papers

- **2026-10-05** — Stefan Bühler, David Exler, Markus Reischl et al. — [The Pushback Paradox: A Two-Probe Diagnostic for Language Model Compliance](http://arxiv.org/abs/2610.06673v1)
  <details><summary>📄 Abstract</summary>
  Are language models compliant with user instructions? A model that always complies can be stopped but also exploited, while one that always resists can be neither exploited nor stopped. We contribute an open two-probe benchmark that can place any language model on this spectrum. In the active probe, a user instructs the model to act and accept a lower payoff, which measures exploitability. In the passive probe, the user instructs it to wait and give up a higher payoff, which measures stoppabilit...
  </details>

- **2026-10-05** — Tobias Heldt, Matt Turk, Christoph Landolt et al. — [Does AI Help Cyber Attackers or Defenders? Evidence from Nonpublic Vulnerabilities and Subsequent Attacks](http://arxiv.org/abs/2610.06584v1)
  <details><summary>📄 Abstract</summary>
  The release decision for frontier AI systems increasingly relies on cyber capability benchmarks, yet public vulnerability benchmarks can expose agents to previously published advisories, exploits, and fixes, making it difficult to distinguish prior exposure from capability on unseen vulnerabilities. We evaluate open-weight and proprietary AI models on exploit generation, vulnerability repair and subsequent attacks in five nonpublic software environments, including vulnerabilities we privately di...
  </details>

- **2026-10-05** — Junle Chen, Wei Chen, Zhengjun Huang et al. — [You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue](http://arxiv.org/abs/2610.06496v1)
  <details><summary>📄 Abstract</summary>
  When a large language model handles a multi-turn task and a user proposes a change but ultimately rejects it, the model should continue as if nothing changed. We find a surprising failure: merely mentioning a rejected change can derail task execution, even when the user's final intent remains unchanged. To systematically study language model behavior under evolving user intent, we introduce Intent-Eval, a controlled benchmark spanning tool actions, code, databases, and mathematics. Across divers...
  </details>

- **2026-10-05** — Kristian Dalland, Prithvi Poddar, Souma Chowdhury et al. — [Traversability-Aware Cooperative Path Planning for Human-UGV Casualty Evacuation](http://arxiv.org/abs/2610.06487v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous multi-robot path planning is a well-studied problem in which agents with disparate kinematic and dynamic models must coordinate to achieve shared objectives. These formulations, however, treat all agents as robotic-their cost models are mechanical and their traversability is sensor-derived. In human-robot teaming, the human partner remains relegated to command and supervisory roles rather than being modeled as a physical co-navigator with distinct mobility constraints and dynamic e...
  </details>

- **2026-10-05** — Boyue Caroline Hu, Kaivalya Ahir, Ronghao Ni et al. — [Correct Verdicts, Flawed Reasoning: Structured Auditing of LLM-based Vulnerability Reasoning](http://arxiv.org/abs/2610.06366v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed for automated software vulnerability analysis. Binary classification alone is insufficient; practitioners need explanations to triage bugs and engineer patches. Standard practice relies on Chain-of-Thought (CoT) prompting, but free-form reasoning allows models to obscure logical leaps, hallucinated execution steps, and internal inconsistencies behind plausible prose. Our manual audit reveals that approximately 60% of correct vulnerability ve...
  </details>

- **2026-10-05** — Dongyoon Ryu, Sungho Jeon, Xinyue Ma et al. — [DIALER: A Case for Improving Rare-Class Accuracy in Retraining-Free Edge Video Analytics](http://arxiv.org/abs/2610.06358v1)
  <details><summary>📄 Abstract</summary>
  Edge video analytics with lightweight models is prone to accuracy degradation due to persistent distributional shifts in live video streams. While continuous learning (CL) addresses such data drift, it heavily strains the limited compute resources of edge servers originally provisioned for inference. Our empirical study reveals that emerging vision foundation models (VFMs) offer a practical, retraining-free alternative that delivers high average accuracy with remarkable compute savings. However,...
  </details>

- **2026-10-05** — Yangbo Wei, Junhong Qian, Zhen Huang et al. — [Serve Now or Improve Later? Scheduling Self-Evolution in Online Agent Systems](http://arxiv.org/abs/2610.06212v1)
  <details><summary>📄 Abstract</summary>
  Online agents can improve future service by constructing reusable tools, guidance, or model states, but this work competes with current requests for the same GPUs. Exploiting idle compute for self-evolution faces a fundamental systems constraint: benefits arrive only after an artifact is published and used, while pausing evolution leaves service capacity waiting for memory release and runtime recovery. An investment worth completing may therefore be worth postponing. We present LearnSched, a sta...
  </details>

- **2026-10-05** — Wenji Bai, Muhammad Waseem, Zeeshan Rasheed et al. — [Where Did the Repair First Go Wrong? Localizing the Origins of Silent Failures in Agentic Vulnerability Repair](http://arxiv.org/abs/2610.06163v1)
  <details><summary>📄 Abstract</summary>
  Localizing where an LLM-based agent first fails to uphold security during a repair can show which stage of its workflow needs an additional safeguard. This is difficult for silent failures, which are patches that pass syntactic and functional checks but still contain a security vulnerability. Because such patches give no observable failure signal, existing failure attribution methods, which rely on observed task failures and labelled failure steps, are less suited to them. We propose Security Aw...
  </details>

- **2026-10-05** — Seungmin Oh, Seunghun Kang, Jongbin Ryu — [Efficient Test-time Adaptation through Candidate Verification and Divergence Shifts](http://arxiv.org/abs/2610.06147v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong zero-shot transferability but remain vulnerable to target-domain shifts at inference time. Test-time adaptation (TTA) offers a practical remedy, yet most existing VLM-TTA methods follow a prediction-side adaptation paradigm. They use test samples to adjust logits, prototypes, caches, priors, or feature statistics, often incurring additional computational overhead. In this paper, we take a different perspective and reframe VLM-TTA as candidate verifica...
  </details>

- **2026-10-05** — Tamara Czinczoll, Julie Kallini, Gerard de Melo et al. — [LightMTP: Lightweight Latent Multi-Token Prediction](http://arxiv.org/abs/2610.06031v1)
  <details><summary>📄 Abstract</summary>
  Next-token prediction (NTP) is the standard pretraining objective for large language models, yet it provides an explicit training signal only for the immediate next token, which can lead models to exploit local patterns instead of capturing longer-range structure and ideas. Multi-token prediction (MTP) addresses this by training models to predict several future tokens. However, existing MTP methods often introduce a large number of new parameters with limited improvements in downstream performan...
  </details>

- **2026-10-05** — Hankyul Kang, Jongbin Ryu — [Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression](http://arxiv.org/abs/2610.06026v1)
  <details><summary>📄 Abstract</summary>
  SVD-based pruning and quantization have recently emerged as a promising strategy for the ultra-efficient compression of large language models. In these methods, compression is performed in two stages: components are first truncated, and the remaining ones are subsequently quantized. Although this decoupled pipeline benefits from both pruning and quantization, it requires separate optimization for each stage and fails to fully exploit their balance, which can lead to suboptimal performance under ...
  </details>

- **2026-10-05** — Daniele Affinita, Ming Xu, Rudolf Reiter et al. — [Adaptive Expert Guidance for Efficient On-Policy Reinforcement Learning](http://arxiv.org/abs/2610.06019v1)
  <details><summary>📄 Abstract</summary>
  With massively parallel simulation, on-policy Reinforcement Learning methods such as PPO have become standard in many domains. However, learning from scratch is sample-inefficient and fails to exploit the potential existence of a suboptimal expert, such as a heuristic, a model-based controller, or a policy trained on a related task. Such an expert is often available and can guide early training, but its sub-optimality limits final performance. The challenge then becomes balancing expert guidance...
  </details>

- **2026-10-05** — Yao Lu, Zhaiyuan Ji, Yaxin Gao et al. — [Breaking the Tie: A Cluster-Aware Routing Framework for Large Language Models](http://arxiv.org/abs/2610.05982v1)
  <details><summary>📄 Abstract</summary>
  With the rapid development of artificial intelligence, the emergence of various Large Language Models (LLMs) has created a rich model ecosystem. However, this also brings a key challenge: how to select the optimal model for a specific user query. LLM routing addresses this need by dynamically assigning queries to the most suitable expert in the pool of candidate models. However, existing routing frameworks often simplify this process to a standard classification task; thus, a critical vulnerabil...
  </details>

- **2026-10-05** — Jie Wang, Shiwei Luo, Qi Zhang et al. — [Byte Language Models: Scaling, Emergent Abstractions, and Information Allocation](http://arxiv.org/abs/2610.05978v1)
  <details><summary>📄 Abstract</summary>
  Tokenizer-free language models remove the inductive bias of fixed tokenizers by modeling text directly as bytes, but the resulting longer sequences substantially increase computation and eliminate explicit text abstractions. We ask whether this additional computation can be useful, and whether standard Transformers can learn the abstractions that tokenization provides. We study these questions on Transformers without specialized tokenization-related architectures. With token-superposition traini...
  </details>

- **2026-10-05** — Li Yiheng, He Xu, Wang Shaobo et al. — [ReMem: Streaming Video Understanding With Long Context Retention](http://arxiv.org/abs/2610.05940v1)
  <details><summary>📄 Abstract</summary>
  Despite their impressive performance on a wide range of video understanding tasks, current Vision Language Models (VLMs) are predominantly designed for offline scenarios and struggle to handle online streaming videos that demand low latency response. Several studies have explored memory and token compression strategies in an attempt to adapt offline VLMs for streaming video understanding tasks. However, through our probing experiment, we identify that most existing works tend to progressively lo...
  </details>

- **2026-10-05** — Yimin Fu, Songbo Wang, Lizhuo Liu et al. — [Prompt and Refinement: Asymmetric Mutual Learning for Infrared Small Target Detection with Noisy Labels](http://arxiv.org/abs/2610.05918v1)
  <details><summary>📄 Abstract</summary>
  Existing data-driven infrared small target detection (ISTD) methods typically require large-scale datasets with accurate pixel-level annotations for model training. However, such labor-intensive requirements are difficult to satisfy in real-world applications due to the heavy reliance on expert knowledge and the inherently weak distinctiveness of infrared small targets. Consequently, the presence of noisy labels during model training is inevitable, which can severely mislead the learning of targ...
  </details>

- **2026-10-05** — Sarim Hashmi, Mukul Ranjan, Abdelrahman Elsayed et al. — [Noise Out, Bias In: Targeted Bias Injection in Diffusion Language Models via Closed-Loop Activation Steering](http://arxiv.org/abs/2610.05894v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models (dLLMs) generate text by iteratively denoising masked positions, re-predicting each token multiple times before it is committed. An autoregressive decoder exposes an answer's distribution once, at the step that commits it; a dLLM exposes it at every denoising step before commitment, and we show that an adversary can exploit this. Since an answer remains open to revision over many denoising steps, an adversary with access to internal activations can watch how like...
  </details>

- **2026-10-05** — Guang Yang, Changhao Guan, Chao Huang et al. — [Adaptive Utilization of Low-Rank Adaptation via Conditioned Gating](http://arxiv.org/abs/2610.05800v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) achieves parameter-efficient fine-tuning by constraining model updates to a low-rank subspace and has been widely used in practice. However, LoRA typically employs a shared low-rank update across tokens, which limits its ability to fully exploit the adaptation subspace for tokens from different sequences. To address this issue, we propose an adaptive utilization of Low-Rank Adaptation (U-LoRA), which employs conditioned gating to explicitly learn effective token-level ...
  </details>

- **2026-10-05** — Hongjian Chen, Hefu Ye, Changyun Wen — [Separation Principle for Event-Triggered Prescribed-Time Consensus Tracking of Nonlinear Multi-Agent Systems under DoS Attacks](http://arxiv.org/abs/2610.05785v1)
  <details><summary>📄 Abstract</summary>
  Despite the recent development of control theory for multi-agent systems (MASs), the highly desirable separation principle is difficult to establish even for linear MASs, let alone for nonlinear ones that rely solely on output measurements under denial-of-service (DoS) attacks. This paper establishes a separation principle for distributed leader-following control of this class of nonlinear MASs, allowing the observer and the controller to be designed independently. For each agent, two parametric...
  </details>

- **2026-10-05** — Bowen Peng, Li Liu, Yongxiang Liu et al. — [T-JEPA: A Temporal Joint-Embedding Predictive Architecture for Learning Better Remote Sensing Representations](http://arxiv.org/abs/2610.05731v1)
  <details><summary>📄 Abstract</summary>
  Earth observation (EO) data provide rich temporal supervision, yet existing remote sensing foundation models mainly exploit sequential observations through imposing predefined pairwise relations or aggregating holistic reconstruction context. We seek to further exploit the sparse and nonuniform temporal sampling inherent in EO sequences as supervisory signals. To this end, we propose T-JEPA, a temporal joint-embedding predictive architecture that learns time-gap-conditioned latent transitions. A...
  </details>

- **2026-10-05** — Julian Guam, Jianqing Liu — [Transformer-Based Time-Series Inference of Lindblad Dynamics in Open Quantum Systems](http://arxiv.org/abs/2610.05647v1)
  <details><summary>📄 Abstract</summary>
  The Lindblad master equation is the standard framework for describing the non-unitary evolution of open quantum systems, where environmental interactions induce dissipation and decoherence. When both the system Hamiltonian and the dissipation rates are partially unknown or explicitly time-dependent, traditional analytical inversion and system-identification techniques become intractable. Recent works have demonstrated that Transformer-based models can infer unknown dissipation rates from observa...
  </details>

- **2026-10-04** — Enrico Barbiero, Marco Lovera — [The asymptotic variance of the Hermite-Domain Predictor-Based Subspace Identification method](http://arxiv.org/abs/2610.05548v1)
  <details><summary>📄 Abstract</summary>
  This paper derives analytical expressions for the asymptotic variance of the Hermite-Domain Predictor-Based Subspace Identification (HD-PBSID) method. Unlike continuous-time subspace approaches that rely on intermediate-domain transformations, HD-PBSID identifies continuous-time state-space matrices directly. The derivation first establishes the uncertainty of the estimated state-space matrices and then exploits these results to obtain asymptotic variance expressions. These expressions provide a...
  </details>

- **2026-10-04** — Yimou Wu, Jiaxin Guo, Yun-hui Liu et al. — [Deep Prior Learning for Embodied Perception](http://arxiv.org/abs/2610.05531v1)
  <details><summary>📄 Abstract</summary>
  Embodied systems need geometric perception that exploits available observations beyond images alone. Recent feed-forward 3D models incorporate geometric priors, including camera poses, intrinsics, and depth. However, handling noisy poses, preserving accurate priors, and recovering physical scale require more than simply accepting these inputs. We introduce \emph{Vision-Prior Geometry Grounded Transformer} (VPGGT), a VGGT-based framework that extends OmniVGGT for prior-aware embodied perception. ...
  </details>

- **2026-10-04** — Gefei Liu, Sonya Rashkovan, Sophia Lloyd George et al. — [AI Safety via Debate is Compromised by Cognitive Biases](http://arxiv.org/abs/2610.05461v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from human feedback (RLHF) has played a central role in making large language models responsive to human instructions. However, human evaluators often favor flattering or persuasive responses over truthful ones, creating incentives for models to appeal to evaluators at the expense of accuracy. AI safety via debate has been proposed as a way to improve the supervision of language models: in this paradigm, two agents argue opposing positions and challenge each other's claims...
  </details>

- **2026-10-04** — Yueqi Wang, Zitian Guo, Yupeng Hou et al. — [OpticalRec: Unified Optical Vision-Language Representation for Multimodal Recommendation](http://arxiv.org/abs/2610.05432v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in vision-language modeling have substantially improved multimodal encoding, retrieval and reasoning. Yet for multimodal recommendation, encoding rich item vision-language semantic interactions remains a long-standing bottleneck, which hampers accurate item representation learning and user-item matching. Mainstream approaches primarily adopt independent encoding of vision and language modality followed by rigid late fusion such as concatenation, inherently omitting native vision-...
  </details>

- **2026-10-04** — Jingzhi Gong, Jie M. Zhang, Gunel Jahangirova et al. — [Adaptive Code Revision Attacks on AI Pull Request Reviewers](http://arxiv.org/abs/2610.05399v1)
  <details><summary>📄 Abstract</summary>
  Pull-request review protects software before new code reaches users, helping prevent vulnerabilities that could expose users to attacks. AI agents increasingly perform these reviews and explain which problems need fixing. However, for an attacker submitting vulnerable code, this feedback also reveals what changes may secure approval. Existing PR attacks seek such approval through persuasive text and comments while keeping executable code fixed. This leaves unclear whether an attacker can use the...
  </details>

- **2026-10-04** — Haocheng Yang, Yuchao Zhang, Licheng Pan et al. — [RubricArmor: Adversarial Evolution Improves LLM-Based Rubric Generation](http://arxiv.org/abs/2610.05308v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based reinforcement learning (RL) provides interpretable rewards for aligning large language models (LLMs) by evaluating responses against query-specific evaluation criteria. To construct rubrics at scale, a straightforward approach to LLM-based rubric generation is to prompt an LLM to generate a rubric directly from the query. However, rubrics directly generated by LLMs are vulnerable to reward hacking, since omitted or underspecified criteria allow the policy to obtain high rubric rewar...
  </details>

- **2026-10-04** — Zhiwei Shang, Jiahang Sun, Mingrong Gong et al. — [Fusion is the New Mutation: Bandit-Guided Evolution on Workflow Graphs](http://arxiv.org/abs/2610.05284v1)
  <details><summary>📄 Abstract</summary>
  Automated agentic workflow optimization relies on costly evaluations, making it essential to allocate a limited evaluation budget effectively. Multi-parent fusion can reuse designs from previously discovered workflows, but identifying promising parent combinations requires learning from limited fusion feedback. We introduce DAGO (Directed Acyclic Graph Optimization), a contextual-bandit-guided framework that learns which parent workflows to fuse under a limited evaluation budget. DAGO formulates...
  </details>

- **2026-10-04** — Weiling Yang, Junwen Zhang, Dezun Dong et al. — [HiNa-MoE: High-Performance, Non-Intrusive MoE Inference on CPUs with Matrix Engines](http://arxiv.org/abs/2610.05123v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) inference is increasingly deployed in local and on-premise environments, where expert parameters often exceed GPU memory capacity. In latency-sensitive, low-concurrency settings, repeatedly staging routed-expert weights from CPU memory to the GPU can be prohibitive, leaving routed-expert feed-forward networks (FFNs) on the critical path of multi-socket CPUs. Existing CPU accelerations often rely on intrusive, hardware- or topology-specific requirements, such as AMX-speci...
  </details>

- **2026-10-04** — Leizhen Zhang, Sheng Chen — [VulValidate: Auditing Function-Level Vulnerability Labels with Executable Evidence](http://arxiv.org/abs/2610.05103v1)
  <details><summary>📄 Abstract</summary>
  Reliable learning-based vulnerability detection requires high-quality labels, yet datasets built from vulnerability-fixing commits may label functions as vulnerable simply because they were changed by a security patch. We present VulValidate, a framework that uses LLM agents to coordinate dynamic analysis tools and construct vulnerability-triggering experiments from runtime feedback. Given a labeled function and its fixing patch, VulValidate reconstructs vulnerable and fixed revisions, selects s...
  </details>

- **2026-10-04** — Yudong Gao, Linghan Chen, Wenhan Wu et al. — [Cooldown Landmines: Cross-Tenant Interference Attacks on LLM Gateways](http://arxiv.org/abs/2610.05089v1)
  <details><summary>📄 Abstract</summary>
  LLM gateways enforce separate tenant quotas while sharing model deployments and cooldown records that temporarily exclude failing backends. However, a tenant's request failure can update these shared records and restrict other tenants' access to serviceable deployments. We identify two attacks that exploit this gap in LiteLLM. The first uses requests rejected at the key's requests-per-minute (RPM) limit: caller-supplied identifiers for known registered deployments reach failure handling, allowin...
  </details>

- **2026-10-04** — Yu Ji, Yang Wei, Yutao Hu et al. — [Characterizing Security Effects of OSS Vulnerabilities in Agent Systems](http://arxiv.org/abs/2610.05036v1)
  <details><summary>📄 Abstract</summary>
  Software agents increasingly depend on open-source components when executing tools and interacting with external systems. Security flaws in these dependencies may therefore influence more than the software process in which they occur: their consequences can be carried through tool outputs, agent state, and information subsequently exposed to the model. Determining whether such a consequence is actually realized in a particular execution, and where its influence stops within the agent system, rem...
  </details>

- **2026-10-04** — Avi Epstein, Snir Nehemia, Haim Suchowski et al. — [Physics-Augmented Graph Transformers for Patch-Antenna Forward and Inverse Design](http://arxiv.org/abs/2610.05004v1)
  <details><summary>📄 Abstract</summary>
  Full-wave electromagnetic (EM) simulation enables accurate patch-antenna analysis but is computationally expensive for large-scale forward prediction and inverse design. We present a mesh-native, physics-augmented graph-learning framework that treats radiation-pattern prediction as signal reconstruction on an irregular surface mesh. For the forward problem, a GPS graph transformer is trained with Physics-Augmented Intermediate Supervision (PAIS), an auxiliary node-level objective that predicts c...
  </details>

- **2026-10-04** — Zahra Aref, Sheng Wei, Narayan B. Mandayam — [Bounded Reasoning: Cognitive Hierarchy in Human-versus-AI Cyber Defense](http://arxiv.org/abs/2610.04878v1)
  <details><summary>📄 Abstract</summary>
  Human-agent evaluations often compress interaction into a single performance score, even when human and automated policies adapt differently over time. We study this in a sequential cyber-defense game on an attack graph, where a human or reinforcement-learning defender protects cloud assets against a Deep Q-Network (DQN) attacker. We compare four defender settings: a human reward-only game operationalizing the DQN information structure, a human reward-plus-transition game operationalizing the Co...
  </details>

- **2026-10-04** — Chung-En Ho, Weiyu Sun, Cheng-Jhih Shih et al. — [SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding in Diffusion Language Models](http://arxiv.org/abs/2610.04875v1)
  <details><summary>📄 Abstract</summary>
  Diffusion large language models (DLLMs) generate text through iterative block denoising, and multi-branch speculative decoding accelerates this process by verifying a main branch together with multiple draft branches in a single forward pass. While prior DLLM acceleration methods primarily exploit temporal redundancy across denoising steps, we identify a complementary redundancy axis within each speculative verification step: multi-branch computational redundancy. During speculative verification...
  </details>

- **2026-10-04** — Xiaoyun Yu, Xiangfei Qiu, Yonggui Huang et al. — [GRAM: Correcting Frozen Time-Series Foundation Models via Graph-Retrieved Amplitude Memory](http://arxiv.org/abs/2610.04827v1)
  <details><summary>📄 Abstract</summary>
  Time-series foundation models (TSFMs) enable zero-shot forecasting through large-scale cross-domain pretraining, while retrieval augmentation further improves their performance by leveraging historical information. However, existing methods typically correct TSFM forecasts using the ground-truth futures of similar historical windows, which contain both predictive components already captured by the foundation model and sample-specific random fluctuation that is difficult to transfer. In contrast,...
  </details>

- **2026-10-03** — David Minkwan Kim, Runfa Blark Li, Beckham Po-Ju Lee et al. — [PatternDex: Learning Interaction Patterns to Guide Reinforcement Learning of Bimanual Dexterous Manipulation of Articulated Objects](http://arxiv.org/abs/2610.04765v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we develop a method that enables bimanual dexterous hands to manipulate articulated objects with a high success rate without suffering from an embodiment gap. We observe that the correlation between hand motions and object motions is dictated by the object rather than the hands and can be learned from human-object demonstrations. Based on this observation, we propose PatternDex, a method that learns this correlation and represents it as a token sequence, which we call an interacti...
  </details>

- **2026-10-03** — Enoch Yin, Bin Liu, Zhengling Qi — [When Is Enough Enough in Self-Evolving LLM Systems?](http://arxiv.org/abs/2610.04756v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving large language model (LLM) systems repeatedly propose, evaluate, and incorporate updates to prompts, skills, or other persistent artifacts. Despite their growing effectiveness, these systems typically operate under a predetermined iteration or compute budget, without a principled criterion to determine when further evolution is no longer worthwhile. This can lead to two undesirable consequences: unnecessary computation after performance has saturated and the risk of returning late ...
  </details>

- **2026-10-03** — Noam Elata, Itay Lamprecht, Mikey Shechter et al. — [More Value per Key: Asymmetric Sparse Attention for Faster LLM Decoding](http://arxiv.org/abs/2610.04753v1)
  <details><summary>📄 Abstract</summary>
  utoregressive generation in Large Language Models (LLMs) is constrained by the memory and computational demands of attention mechanisms. Sparse attention methods mitigate this cost by selecting only high-probability entries of the attention matrix. We observe that in many such methods, this renders the probability-value multiplication negligible, shifting the bottleneck to the query-key step. Key heads can therefore be reduced to accelerate inference, while retaining more value heads preserves c...
  </details>

- **2026-10-03** — Xiaoshan Zhou — [Investigating Spatiotemporal Redundancy in Video Transformer for Collision Anticipation](http://arxiv.org/abs/2610.04727v1)
  <details><summary>📄 Abstract</summary>
  In worker-equipment proximity monitoring, video transformers are widely used for collision anticipation and have demonstrated strong performance. However, their accuracy comes with substantial computational demands, creating a tension with the need for low-latency inference on mobile robots and the pursuit of lower-carbon computation in construction. To address this, this study investigates where computation within an established video transformer is redundant and whether that redundancy can be ...
  </details>

- **2026-10-03** — Lydia Mezrag, Semih Cantürk, Michael Perlmutter et al. — [Path Laplacian Encodings for Directed Graphs](http://arxiv.org/abs/2610.04657v1)
  <details><summary>📄 Abstract</summary>
  Directed graphs naturally model many real-world systems in which interactions are asymmetric, such as citation networks, web graphs, and information-flow networks. However, graph learning methods commonly rely on message passing with symmetrized graph representations or positional encodings that only partially exploit edge directionality. We introduce PathLapPE, a novel spectral positional encoding (PE) derived from the path Laplacian on directed graphs. PathLapPE provides node- and edge-level f...
  </details>

- **2026-10-03** — Octavio Pappalardo, Nathan Herr, Tim Rocktäschel — [Anticipating the Consequences of Curriculum Decisions with Large Language Models](http://arxiv.org/abs/2610.04604v1)
  <details><summary>📄 Abstract</summary>
  Automatic curriculum learning can improve the effectiveness of reinforcement learning by selecting the training experiences presented to the agent over time. Predicting the consequences of such decisions can, however, be difficult. We analyze automatic curriculum learning as a sequential decision-making problem, highlighting a gap between the quantities that determine the value of curriculum decisions and the information captured by local learning signals commonly used to guide them. We then inv...
  </details>

- **2026-10-03** — Marcus Armstrong, Navid Ayoobi, Pradham Mummaleti et al. — [Correctness Is a Direction: Geometric Answer Selection in Language Models](http://arxiv.org/abs/2610.04512v1)
  <details><summary>📄 Abstract</summary>
  Answer correctness is encoded as a recoverable geometric direction in the hidden states of language models. We show that the mean displacement from incorrect to correct answer representations, computed at approximately 70\% of model depth from fifty labeled examples with no parameter updates, yields a scoring direction that outperforms zero-shot log-probability scoring by up to +32.0 percentage points on factual benchmarks (ARC-Challenge and MMLU) and by +38.1 to +51.8 percentage points on Truth...
  </details>

- **2026-10-03** — Xuanjun Chen, Zixiong Su, Hao Shi et al. — [Can LLM Agents Automate Reinforcement Learning for Text-to-Speech?](http://arxiv.org/abs/2610.04488v1)
  <details><summary>📄 Abstract</summary>
  Although reinforcement learning (RL) post-training repairs the localized segmental errors of zero-shot text-to-speech (TTS), arriving at a working recipe still relies on tedious manual tuning, and whether LLM agents can take over this research pipeline is unclear. We investigate this question with AgenticTTS-Forge, a collaborative workflow that structures human guidance and agentic execution around a shared workspace, applied to CosyVoice2-0.5B. To measure what the agent automates, we audit its ...
  </details>

- **2026-10-02** — Siu Tung Wong, Carlo Campajola — [When a Correct Reward Is Not Enough: Diagnosing and Guiding PPO in an Analytically Solved Broker-Trader Game](http://arxiv.org/abs/2610.03598v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is increasingly used for financial optimal-control problems when complex dynamics make analytical strategies difficult to obtain. There are financial mathematics literactures which provides many solved models whose equations and controls could evaluate and guide learning; we ask whether RL can exploit these results.   We place a proximal policy optimisation (PPO) agent in an analytically solved continuous-time broker--trader game. PPO replaces the broker and chooses i...
  </details>

- **2026-10-02** — Yuyang Dai, Rana Shahout, Mahmood Sharif — [Jumping the Line: Exploiting Length Predictions in LLM Scheduling](http://arxiv.org/abs/2610.03430v1)
  <details><summary>📄 Abstract</summary>
  Efficient request scheduling is increasingly important for reducing completion time in large language model (LLM) serving. Size-based policies such as Shortest Job First prioritize shorter requests, but output lengths are unknown before generation, so practical schedulers rely on predicted lengths. We introduce JIL, an attack on prediction-based LLM schedulers that manipulates the scheduling signal to obtain higher priority and reduce completion time. Using TRAIL as a case study, JIL optimizes a...
  </details>

- **2026-10-02** — Lin Cui, Vincenzo Scotti, Raffaela Mirandola — [CVE2AP: Automated Generation of PDDL-Encoded Attack Paths via Large Language Models](http://arxiv.org/abs/2610.03383v1)
  <details><summary>📄 Abstract</summary>
  Attack Path (AP) modeling is fundamental to cybersecurity analysis, where the Planning Domain Definition Language (PDDL) has been widely adopted to encode APs into formal and machine-verifiable representations for automated reasoning about vulnerability exploitation, attack progression, and their potential impacts. However, existing AP modeling approaches largely rely on expert-driven manual construction, limiting their scalability and ability to keep pace with rapidly evolving cyber threats. La...
  </details>

- **2026-10-01** — Hanchu Zhou, Dechen Gao, Hang Wang et al. — [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](http://arxiv.org/abs/2610.02161v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) and vision-language-action models (VLAs) have recently driven rapid progress in general-purpose robots, yet most progress has focused on single-robot settings. Extending these capabilities to multi-robot systems remains challenging because robots must coordinate long-horizon behaviors while maintaining reliable, fine-grained execution. We introduce DuoMind, a distributed hierarchical framework for multi-robot coordination through semantic communication. Each robot u...
  </details>

- **2026-10-01** — Kingshuk Gupta, Davide Buscaldi — [External Observers May See More Clearly: Cross-Model Span-Level Hallucination Detection in Large Language Models via Hidden State Probing](http://arxiv.org/abs/2610.02066v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) increasingly serve as foundational reasoning engines, their tendency to hallucinate remains a critical vulnerability. While recent internal state probes offer a promising alternative to slow external retrieval systems, they largely reduce hallucination detection to a token-wise binary classification task, failing to capture the structured, sequential boundaries of semantic drift. Here, we introduce an internal hidden state framework for fine-grained, span-level ha...
  </details>

- **2026-10-01** — Michael Y. Fatemi, Jinhao Liang, Ferdinando Fioretto — [Training-Free Diffusion Planning with Analytical Local Scores](http://arxiv.org/abs/2610.01959v1)
  <details><summary>📄 Abstract</summary>
  Path finding and multi-robot motion planning require trajectories that are smooth, goal-directed, and collision-free in environments with complex geometric constraints. Recent diffusion-based planners have shown that trajectory generation can be cast as iterative denoising which has opened the doors to learning-based approaches that can handle multi-modal trajectory distributions and refine entire trajectories. However, a key limitation is that diffusion planners require training on large collec...
  </details>

- **2026-10-01** — Caleb Stam, Aagrim Hoysal, Sanjukta Krishnagopal — [Higher-Order Positional Encodings for Graph Representation Learning](http://arxiv.org/abs/2610.01903v1)
  <details><summary>📄 Abstract</summary>
  Many real-world systems exhibit higher-order interactions among groups of entities that cannot be captured by pairwise relationships alone. Graph Transformers and Graph Neural Networks increasingly rely on positional encodings to enrich graph representations, yet existing positional encodings are computed solely from the original graph and therefore cannot directly capture observed higher-order interactions. Topological Deep Learning addresses this limitation by lifting graphs to simplicial comp...
  </details>

- **2026-10-01** — Jose A. Ayala-Romero, Andres Garcia-Saavedra, Xavier Costa-Perez — [TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design](http://arxiv.org/abs/2610.01887v1)
  <details><summary>📄 Abstract</summary>
  Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastructure. While learning-based schedulers excel in research, industrial deployments still rely on hand-written rules that operators can read, audit, and execute within tight latency budgets. LLM-based Automatic Heuristic Design (AHD) promises to automate writing such rules. However, existing AHD frameworks were developed for combinatorial problems ful...
  </details>

- **2026-10-01** — Tian Shen, Harald Baayen — [Compound interpretation is based on analogy](http://arxiv.org/abs/2610.01688v1)
  <details><summary>📄 Abstract</summary>
  How compound meanings are best predicted from constituent meanings remains a central question in computational models of lexical semantics. Comparing different computational models provides a way to evaluate alternative accounts of how semantic information is combined during compound comprehension. We propose a new model, the Compound Analogy Model (CAM), that predicts a compound's embedding by adding its constituent embeddings together with the average shift vectors of the two constituents' com...
  </details>

- **2026-10-01** — James Gulliford, Gareth O. Roberts, Michael F. Faulkner — [Optimal sampling strategies in event-chain Monte Carlo](http://arxiv.org/abs/2610.01659v1)
  <details><summary>📄 Abstract</summary>
  Event-chain Monte Carlo (ECMC) has revolutionised computational sampling over recent years, providing a powerful alternative to the molecular-dynamics (MD) and Hamiltonian Monte Carlo (HMC) algorithms. Each method outperforms the ubiquitous random-walk Metropolis algorithm by advancing particles along deterministic trajectories, but ECMC achieves this without being constrained by Newtonian dynamics. Recent advances exploited this dynamical freedom to induce a collective particle dynamics that re...
  </details>

- **2026-10-01** — Xudong Wang, Hao Wu, Haozhe Hu et al. — [MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs](http://arxiv.org/abs/2610.01434v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) incur substantial inference costs when processing long visual-textual sequences. While existing operation compression methods exploit modality-level redundancy, they largely treat computation within attention heads and shared feed-forward network (FFN) channels as unified units, leaving finer-grained redundancy underexplored. We find that redundancy varies both across modality-interaction paths within the same attention head and across visual and textual ...
  </details>

- **2026-10-01** — Celso de Melo, Zishan Feng, James Hale et al. — [Reputation, Strategy, and Emotion Effects on Generative AI Cooperation: A Comparison Across Reasoning and Non-Reasoning Models](http://arxiv.org/abs/2610.01222v1)
  <details><summary>📄 Abstract</summary>
  As generative AI (Gen AI) systems take on increasingly autonomous roles in economically and socially consequential interactions, understanding their propensity to cooperate -- and the signals that shape this propensity -- has become essential. We examine cooperative behavior in frontier Gen AI models using the iterated prisoner's dilemma, manipulating counterpart reputation (positive, unknown, negative), strategy (extortion vs. generosity), and non-verbal emotional signaling (facial expressions ...
  </details>

- **2026-10-01** — Yuji Takubo, Daniele Gammelli, Marco Pavone et al. — [OrbitTAMP: Grounding Language Models for Task and Motion Planning in Spacecraft Rendezvous](http://arxiv.org/abs/2610.01093v1)
  <details><summary>📄 Abstract</summary>
  Spacecraft rendezvous and proximity operations (RPO) are currently planned through an expertise-intensive process in which engineers translate high-level operational intent into safe, dynamically feasible trajectories, creating a bottleneck to scalable operations. Large language model (LLM)-based agents could offer an intuitive interface for this process, although their outputs are not inherently grounded in orbital dynamics, operational constraints, or the structure of admissible spacecraft man...
  </details>

- **2026-10-01** — Zekai Zhang, Yunjie Tian, Yanjin He et al. — [Scaling and Distilling Text Embeddings for Better Diffusibility](http://arxiv.org/abs/2610.01016v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) offer a promising alternative to autoregressive (AR) language generation. Recent advances in continuous DLMs, which apply latent diffusion to continuous text embeddings, raise a practical question: which embedding makes the best latent space, i.e., the most diffusible? To answer this, we search through different embeddings and find that scaling the embedding model to stronger ones within the same family (T5 to T5Gemma-1 to T5Gemma-2) greatly improves generative p...
  </details>

- **2026-10-01** — André V. Duarte, Aditya Oke, Rui Melo et al. — [ABSENTIA: Detecting Broken Access Control Vulnerabilities in Web Applications](http://arxiv.org/abs/2610.00977v1)
  <details><summary>📄 Abstract</summary>
  Broken access control, the failure of authorization, is one of the most prevalent web security risks. Unlike injection, a flow of untrusted input into a dangerous operation, authorization is a relation: who may act on what, not how data moves. Each application decides that relation for itself, so no rule written in advance carries to the next. An LLM agent can infer it from the code, but with no systematic way to cover the application and prioritize what to inspect, its search stays undirected a...
  </details>

- **2026-10-01** — Chuxuan Hu, Hejie Cui, Norman Huang et al. — [RPTune: Learned Context Curation for LLM Catalog Search](http://arxiv.org/abs/2610.00964v1)
  <details><summary>📄 Abstract</summary>
  For small merchant businesses (SMBs) whose catalogs fit within a long-context LLM, full-catalog prompting offers a compelling alternative to multi-stage retrieval designed primarily for large marketplaces with millions of items. However, fitting the full catalog into the context window does not ensure that the model can use it effectively, since LLMs do not exploit long contexts uniformly. We therefore study in-context catalog search through two complementary questions: (1) how to curate and pre...
  </details>

- **2026-10-01** — Mingrun Jiang, Yuejia Liu, Zishan Shao et al. — [Joint Branch-Space Transform Coding for Diffusion Activation Quantization with Classifier-Free Guidance](http://arxiv.org/abs/2610.00930v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization for diffusion models increasingly exploits timestep, feature, and layer structure. While recent work has begun incorporating CFG structure into diffusion quantization, activation quantization still operates independently across conditional and unconditional coordinates, leaving cross-activation structure unexploited. We show that matched CFG activations form a strongly correlated two-dimensional source and that, under a fixed bit budget, the choice of branch coding bas...
  </details>

- **2026-10-01** — Zhanming Zhang, Vinoth Selvendran — [Sharpen Before You Adapt: Data-Free Entry-State Sharpening for Test-Time Reinforcement Learning](http://arxiv.org/abs/2610.00903v1)
  <details><summary>📄 Abstract</summary>
  Test-time reinforcement learning (TTRL) adapts language models on unlabeled test problems using supervision derived from their own samples. This makes the checkpoint's \emph{entry state} consequential: a diffuse policy provides noisier self-supervision and may spend much of a limited adaptation budget merely concentrating probability mass before reliably expressing capability it already possesses. We propose \textbf{entry-state sharpening}: use data-free training \emph{before} TTRL to prepare a ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 61 papers

- **2026-10-05** — Hao Sun, Yibin Yao, Chaohai Xie et al. — [An Evaluation of the Semantic Understanding Capabilities of Large Language Models for Web Attack Payloads](http://arxiv.org/abs/2610.06507v1)
  <details><summary>📄 Abstract</summary>
  Computer vision services delivered through Web interfaces and APIs process textual requests for image-resource acquisition, inference-task configuration, and result management, making Web attack-payload analysis relevant to their deployment security. Large language models (LLMs) can identify payload types and explain attack intent. However, existing studies generally treat payload analysis as a single-layer classification task and lack both a systematic assessment of how deeply LLMs understand p...
  </details>

- **2026-10-05** — Christoph Bühler, Matteo Biagiola, Luca Di Grazia et al. — [AgentSpy: Making AI Agent Behavior Observable](http://arxiv.org/abs/2610.06001v1)
  <details><summary>📄 Abstract</summary>
  AI agents built on large language models (LLMs) run shell commands, read and write files, and reach the network, typically with their user's privileges. However, what an agent does during an execution is difficult to understand: tests assert on the result, and the agent's trajectory records only what the agent reports about itself, which may omit behavior executed by its subprocesses. We present AgentSpy, an approach that observes an agent from outside the agent. AgentSpy runs the agent in an is...
  </details>

- **2026-10-05** — Rohan Mehra, Alexandre Riffard, Yannis Loumouamou et al. — [Analysis of SWIR Imaging Detection Performance Under Adverse Environmental Conditions for Autonomous Driving Systems](http://arxiv.org/abs/2610.06596v1)
  <details><summary>📄 Abstract</summary>
  Short-wave infrared (SWIR) imaging has emerged as a promising modality for autonomous driving, yet its practical benefits over RGB remain poorly characterized across diverse conditions. This paper presents a systematic comparative study of paired RGB and SWIR object detection on the RASMD dataset, covering four weather conditions and two real-time detection architectures, with various fine-tunings evaluated against a unified ground truth. Overall, RGB demonstrates comparable or superior performa...
  </details>

- **2026-10-05** — Xinling Li, Dadi Guo, Qingyu Liu et al. — [Before Agent Tells The Lie: Has Deception Already Been Represented?](http://arxiv.org/abs/2610.06576v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents can exhibit deceptive behavior during task execution, including hiding failures, fabricating results, or falsely signaling task completion. Existing monitoring approaches mainly detect deception after it appears in observable actions or outputs. In this paper, we investigate whether deceptive behavior can be predicted from an agent's internal representations before it becomes externally visible. We frame deception monitoring as a trajectory-level represent...
  </details>

- **2026-10-05** — Guillermo GP-Lenza, Miguel Fernandez-Cortizas, Martín Molina et al. — [A Taxonomy on Collective Awareness](http://arxiv.org/abs/2610.06427v1)
  <details><summary>📄 Abstract</summary>
  As robotic teams tackle increasingly complex tasks in dynamic and unstructured environments, effective coordination requires agents to maintain accurate, aligned representations of their environment, teammates, and mission state. We argue that Mutual Awareness, Shared Situational Awareness, and Team Situational Awareness --- three concepts widely invoked in the multi-robot systems literature --- are not interchangeable: they form a containment hierarchy in which each type subsumes the previous i...
  </details>

- **2026-10-05** — Petteri Kela, Dani Korpi, Mikko Honkala — [Combining Improvements in Uplink AI-RAN](http://arxiv.org/abs/2610.05936v1)
  <details><summary>📄 Abstract</summary>
  One of the major transformative factors in 6G will be the integration of Artificial Intelligence (AI) to become a native part of Radio Access Network (RAN). While most physical-layer AI features have so far been evaluated in isolation using link-level simulations, their combined behavior in a realistic multi-cell, multi-UE deployment has remained largely unexplored. In this paper, we present system-level performance results when multiple uplink AI features are enabled together, achieved by integ...
  </details>

- **2026-10-05** — Seil Kang, Hangoo Kang, Tarun Suresh et al. — [ThunderSyncRL: Lossless Acceleration of Agentic Reinforcement Learning](http://arxiv.org/abs/2610.05935v1)
  <details><summary>📄 Abstract</summary>
  Language models are moving beyond generating answers to pursuing long-horizon goals in interactive environments. Post-training these agents requires long, heterogeneous trajectories, and synchronous systems leave learner engines idle until rollout and verification finish. To squeeze out these pipeline bubbles, asynchronous training overlaps rollout and learning across updates, but comes at the cost of policy staleness. We introduce ThunderSyncRL, which starts gradient computation as soon as all ...
  </details>

- **2026-10-05** — Junqi Liu, Yongyang Pan, Zhuosong Jiang et al. — [VERA: Scaling Verifiable Environments for Agentic co-Evolution](http://arxiv.org/abs/2610.05923v1)
  <details><summary>📄 Abstract</summary>
  Competent agents need precise and verifiable environments, such as sandboxes that are resumable at any stage and evolve from observable evidence. However, most long-horizon work exposes how rare these are: for example, an agent in medical research must ground a finding, classify it, and write a report over dozens of dependent steps, yet recent environments score only the outcome. To address the challenges in stable training, we present VERA, which builds such environments at scale and lets agent...
  </details>

- **2026-10-05** — Yubo Wang, Hui He, Hezhe Qiao et al. — [FreSia: Frequency-Semantic Instantiation and Alignment for Multivariate Time Series Analysis](http://arxiv.org/abs/2610.05726v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown strong potential in multivariate time series forecasting and anomaly detection. Existing studies predominantly inject temporal information into LLMs via direct numerical tokenization or heuristic textual descriptions. However, LLMs still face difficulty in perceiving the underlying structural patterns of numerical time series, particularly the seasonal and trend components obscured by discrete numerical tokens. To bridge this gap, we propose FreSia, a freq...
  </details>

- **2026-10-05** — Haoyun Yang, Xueyang Zhou, Ziyi Xie et al. — [AffordCraft: Scalable Construction of Task-Ready Simulation Assets from Single Images](http://arxiv.org/abs/2610.06643v1)
  <details><summary>📄 Abstract</summary>
  Robot learning in simulation depends on the objects the simulator offers. Many tasks need objects with separate parts, joints that allow the required motion, and physical properties that remain valid under contact. Existing methods recover this structure anew for every image: generative models predict parts and joints that mostly fail to settle or move in simulation, and general-purpose agents need a long session of model calls for each photograph. AffordCraft builds such an asset from a single ...
  </details>

- **2026-10-05** — Maximilian Bershtman, Niv Cohen — [Adapting prior-data fitted networks for tabular anomaly detection](http://arxiv.org/abs/2610.06693v1)
  <details><summary>📄 Abstract</summary>
  While deep features have transformed anomaly detection in images and video, their impact on tabular data has been less substantial, partly due to the limited availability of strong deep representations. Recently, prior-data fitted networks (PFNs) have emerged as a promising source of such representations for tabular data. In this work, we investigate how PFN representations can be adapted and leveraged for anomaly detection. The question is harder than it looks. No anomalies are available before...
  </details>

- **2026-10-05** — Xiaohui Zhou, Yijie Wang, Hongzuo Xu et al. — [Normality Constraint Learning: Adapting Foundation Models for Time Series Anomaly Detection](http://arxiv.org/abs/2610.06453v1)
  <details><summary>📄 Abstract</summary>
  Time Series Foundation Models (TSFMs) achieve strong generalization by learning to reconstruct or forecast broad temporal patterns from large-scale time series during pre-training. Yet this strength can become a weakness for anomaly detection: TSFMs may model rare anomalous patterns as effectively as normal ones, allowing anomalies to be accurately reconstructed or forecasted and thus diminishing their reconstruction/forecasting error-based anomaly scores. This paper proposes $\underline{\textbf...
  </details>

- **2026-10-05** — Roxane Koitz-Hristov, Franz Wotawa — [Choosing an energy-efficient software architecture for building system diagnostic support](http://arxiv.org/abs/2610.06444v1)
  <details><summary>📄 Abstract</summary>
  Around 30\% of global energy expenditure can be attributed to the building sector, where a large portion of energy-consumption could be avoided by repairing existing faults. Fault detection and diagnosis (FDD) software addresses this issue; however, its creation and operation also have an environmental impact. The magnitude of this impact is influenced by the diagnosis architecture, as different architectures and methods have different energy demands. Yet, simply considering the energy consumed ...
  </details>

- **2026-10-05** — Álvaro Díez, Fidel Aznar — [Visual Swarm Navigation via Deep Reinforcement Learning and Evolutionary Hybrid Design](http://arxiv.org/abs/2610.06400v1)
  <details><summary>📄 Abstract</summary>
  Swarm robotics presents a robust and cost-effective paradigm for advanced automation in complex, dynamic environments, such as those encountered in search and rescue or environmental monitoring. A fundamental challenge for this field is the data-driven design of decentralized controllers capable of generating emergent collective behaviors. This paper proposes a novel, AI-driven hybrid methodology for the automatic synthesis of swarm robotic controllers for autonomous visual navigation. This appr...
  </details>

- **2026-10-05** — Harshkumar Devmurari, Gautham Kuckian, Prajjwal Vishwakarma — [AUTOPILOT An Advanced Perception, Localization and Path Planning Techniques for Autonomous Vehicles Using YOLOv7 and MiDaS](http://arxiv.org/abs/2610.06232v1)
  <details><summary>📄 Abstract</summary>
  Self driving vehicles have emerged as a reliable technology that has the capability to transform transportation and mobility. The development of self driving cars requires significant advances in a number of areas, including perception, localization, decision making, and control. This research paper is based on the project implementation of the combination of object detection using YOLO (You Only Look Once), depth sensing using MiDaS for the localization and perception of obstacles, perspective ...
  </details>

- **2026-10-05** — Tian Lan, Yifei Gao, Yimeng Lu et al. — [Anlu: Enabling In-Context Time Series Anomaly Detection in Foundation Models via Counterfactual Supervision](http://arxiv.org/abs/2610.06180v1)
  <details><summary>📄 Abstract</summary>
  Whether a time-series pattern is anomalous often depends on the operating regime of the monitored process. A missing event can signal a fault in one regime and be routine in another, and the query alone may not reveal which regime applies. We study in-context learning (ICL) for time series anomaly detection (TSAD) through reference-conditioned detection, where a reference record provides evidence about expected behavior and model parameters remain fixed at inference. Supplying the reference is n...
  </details>

- **2026-10-05** — Yoshihiro Izawa, Gouki Minegishi, Yoko Yamakata — [Anosognosia in LLMs: Probing Self-Awareness of Quantized Computational Substrate](http://arxiv.org/abs/2610.06174v1)
  <details><summary>📄 Abstract</summary>
  Can LLMs recognize degradation in their own computational substrate? Inspired by anosognosia, a neurological condition in which patients fail to recognize impairments in their own abilities, we investigate whether LLMs can recognize degradation in their computational substrate induced by quantization. We first show that existing models fail to self-report their quantization state, even when provided with their own generated text as an external cue. Linear probing reveals that, while generated te...
  </details>

- **2026-10-05** — Abdul Basit, Muhammad Abdullah Hanif, Muhammad Shafique — [MS-Exam-Gen: Source-Grounded Benchmark Construction for Evaluating LLMs on Textual Multiple Sclerosis MRI Knowledge](http://arxiv.org/abs/2610.06170v1)
  <details><summary>📄 Abstract</summary>
  Biomedical large language model (LLM) evaluation requires auditable assessment of narrow, evolving, source-grounded subspecialty knowledge. Multiple sclerosis MRI (MS-MRI) provides a high-stakes textual-knowledge test case because correct reasoning requires current diagnostic criteria, standardized acquisition and reporting knowledge, longitudinal monitoring concepts, lesion morphology, and recognition of difficult mimics. We present MS-Exam-Gen, a reproducible framework for constructing and aud...
  </details>

- **2026-10-05** — Wei Wu — [Mechanizing the User's Eye: Pre-Registered Deployment of a Sabotage-Validated Fail-Plausible Observer in a Production LLM Agent Runtime](http://arxiv.org/abs/2610.05981v1)
  <details><summary>📄 Abstract</summary>
  A prior longitudinal study of silent failures in a production LLM agent runtime (arXiv:2606.14589) found that about 70% were discovered by a human looking at the product as a user while thousands of tests and governance checks stayed green, and posed mechanizing part of what the human eye does as an open problem. This paper reports our attempt. We built an automated user-viewpoint observer targeting the most dangerous class, fail-plausible failure, in which an internal error becomes fluent, plau...
  </details>

- **2026-10-05** — Yiqi Wang, Jiaqi Liu, Jiaqi Zhang et al. — [PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents](http://arxiv.org/abs/2610.05732v1)
  <details><summary>📄 Abstract</summary>
  LLM agents rely on long-term memory to retain and reuse information when performing tasks over long horizons. Existing methods provide limited support for handling memories that become outdated as new observations or domain evidence arrive. Such outdated memories may remain semantically relevant, continue to affect dependent records, and retain value as historical evidence. This calls for two capabilities: dependency tracking to identify downstream effects and historical preservation to retain u...
  </details>

- **2026-10-04** — Bao-Phong Nguyen, Gia-Khanh Pham, Thai-Duong Do et al. — [AutoDP-LLM: Automating Data Pre-processing for Intrusion Detection Systems using Large Language Models](http://arxiv.org/abs/2610.05369v1)
  <details><summary>📄 Abstract</summary>
  The increasing complexity and scale of modern cyber-attacks demand intelligent and computationally efficient Intrusion Detection Systems (IDS). However, designing effective data pre-processing pipelines traditionally involves substantial trial-and-error effort and repeated evaluation of alternative configurations. For large, high-dimensional network traffic data, this process can create a significant computational burden. In this work, we propose AutoDP-LLM, an automated pre-processing framework...
  </details>

- **2026-10-04** — Shuyi Miao, Xinyi Huang, Wangjie Qiu et al. — [ContractLens: Latent Security Knowledge for Malicious Smart Contract Detection](http://arxiv.org/abs/2610.04992v1)
  <details><summary>📄 Abstract</summary>
  Detecting malicious smart contracts is essential to safeguarding the Web3.0 ecosystem. However, existing auditing methods based on large language models (LLMs) largely rely on prompt engineering or attack-specific fine-tuning, while the internal representations that support malicious logic detection remain poorly characterized. To address this gap, we propose ContractLens, a framework that localizes and uses latent security knowledge in pretrained LLMs for interpretable malicious smart contract ...
  </details>

- **2026-10-04** — Nallathambi Vethiappan, Derya Soydaner, Gijs Wijnholds — [Atomic Visual Entailment: Enhancing Zero-Shot Vision-Language Reasoning through Atomic Fact Decomposition and Learned Selection](http://arxiv.org/abs/2610.05630v1)
  <details><summary>📄 Abstract</summary>
  Visual entailment (VE) asks whether an image supports, contradicts, or leaves undecided a textual hypothesis. Strong results come from fine-tuning large vision-language models on labelled data, while zero-shot and hybrid approaches remain far behind. A VE hypothesis often bundles several visual claims, yet existing zero-shot methods reason over it as a single unit. We propose Atomic Visual Entailment (AVE), which decomposes the hypothesis into atomic facts, produces candidate predictions from bo...
  </details>

- **2026-10-04** — Zijun Yu, Yu Gu, Vahid Partovi Nia et al. — [G-CARB: Graph-Localized Conformal Agent Risk Budget for Compositional Harm](http://arxiv.org/abs/2610.05563v1)
  <details><summary>📄 Abstract</summary>
  Small language model (SLM) agents need safety controls that track consequences across tool calls with little monitoring overhead. A private read, for example, becomes a leak when a later action sends that data outside the system. We introduce CARB (Conformal Agent Risk Budget), which calibrates when to stop an agent using a ledger of harm incurred before stopping. Under exchangeable episodes, standard conformal risk control bounds this declared loss in expectation over calibration and a future e...
  </details>

- **2026-10-04** — Shiyuan Zhou, Ashwin Gerard Colaco, Sainyam Galhotra et al. — [SALUS: Automated Auditing of NL-to-SQL Benchmarks through Weak Supervision of Multi-Agent Output](http://arxiv.org/abs/2610.05540v1)
  <details><summary>📄 Abstract</summary>
  Natural language to SQL (NL-to-SQL) benchmarks are foundational to progress in data analysis research, yet recent work has shown that widely-used benchmarks contain significant annotation errors. These errors silently corrupt evaluation metrics, penalize correct model output, and distort the field's understanding of state-of-the-art performance. We present SALUS, a system that automatically detects annotation errors in NL-to-SQL benchmarks. SALUS frames benchmark auditing as a weakly supervised ...
  </details>

- **2026-10-04** — Dikshant Dulal, Maxence Grandadam, Maciej Koch-Janusz et al. — [Demonstration of a Structured Agentic Workflow for Applied Quantum Computing Research](http://arxiv.org/abs/2610.05304v1)
  <details><summary>📄 Abstract</summary>
  Quantum hardware advances now make it practical to explore quantum approaches to scientific problems. Applied quantum computing research sits at the intersection of domain knowledge, algorithms, theoretical physics, device physics, and quantum and classical computational methods. The breadth of expertise required and the inherent project complexity challenge not only any individual researcher, but also generic AI systems. Here, we introduce the Quantum Agentic Operating System (QAOS), a structur...
  </details>

- **2026-10-04** — Haitao Yu, Weidong Mei, Lei Qian et al. — [Cross-Layer Analysis and Optimization for Movable Antenna Systems with Delay-Outage Constraints](http://arxiv.org/abs/2610.05239v1)
  <details><summary>📄 Abstract</summary>
  Movable antennas (MAs) have emerged as a promising technology for enhancing wireless communication performance. However, in delay-sensitive systems, MA movement incurs non-negligible delay, which may degrade the service process for bursty traffic. This paper investigates a delay-outage problem in an MA-enhanced multiuser multiple-input multiple-output (MU-MIMO) downlink system. Unlike existing studies that mainly focus on physical-layer performance optimization, a cross-layer framework is develo...
  </details>

- **2026-10-04** — Chao Huang, Pengfei Wei, Kaige Li et al. — [Representation--Behavior Alignment for Explainable Weakly-Supervised Video Anomaly Detection](http://arxiv.org/abs/2610.05129v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) provide a natural way to make video anomaly detection more explainable. However, their final decisions do not always fully use the discriminative information contained in their hidden states, an issue we refer to as representation--behavior misalignment. We decompose this gap into a capacity component that measures discriminative information never aggregated into the readout position, and a directional component that measures the angular mismatch between ...
  </details>

- **2026-10-04** — Donghwan Kim — [When LLMs Sit Above Diagnostic Tools: Unrealized Complementarity in Industrial Fault Diagnosis](http://arxiv.org/abs/2610.05031v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as integration layers above specialized tools, but a stronger component does not necessarily produce a stronger combined system. Across five diagnostic datasets (bearing vibration, process monitoring, semiconductor equipment), we study whether an LLM can reliably use external diagnostic information; paired repeat calls separate advice effects from output instability. In all five, conflicting external information overturned initially correct LLM judgmen...
  </details>

- **2026-10-04** — Jing Xie, Shouwei Ruan, Yubin Wang et al. — [PreAct-Nav: Agentic Reasoning Before Action for Urban Navigation](http://arxiv.org/abs/2610.04916v1)
  <details><summary>📄 Abstract</summary>
  Urban navigation requires embodied agents to pursue long-horizon goals through local decisions based on egocentric observations. However, existing agentic navigation methods often struggle to translate distant goals into coherent local decisions in large-scale physical environments. Their reliance on linguistic reasoning over transient observations or limited history constrains anticipation of the consequences of actions and future conditions, despite the importance of such foresight for navigat...
  </details>

- **2026-10-04** — Zhixuan Tan, Pengjie Gu, Zhao Li et al. — [From Memory to Guide: Spatio-Temporal Composer for Procedural Coding Memory](http://arxiv.org/abs/2610.04868v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented agents typically integrate procedural knowledge by injecting retrieved skills directly into text prompts. This approach dangerously equates readable text with reliable execution. To bridge this gap, we introduce From Memory to Guide, a novel paradigm that transitions procedural memory from passive text delivery to active, inference-time policy adaptation. We instantiate this paradigm through the Spatio-Temporal Composer, an active policy compiler that explicitly manages exactly ...
  </details>

- **2026-10-04** — Shahriar Golchin, Marc Wetter — [Monitorability Disposition in Large Reasoning Models](http://arxiv.org/abs/2610.04914v1)
  <details><summary>📄 Abstract</summary>
  Monitoring the chain-of-thought (CoT) of large reasoning models (LRMs) is a common way to detect misbehavior in real-world practice. However, current monitoring is passive: a separate model inspects the session only after execution. This means harm may already have occurred before it is caught. An active alternative is to have the model self-report its misbehavior as it happens. Whether models are willing to do this, however, is unknown. We introduce "monitorability disposition": a model's willi...
  </details>

- **2026-10-04** — Sonal Kumar, Sinan Hersek, Artem Dementyev et al. — [SEA-LM: Egocentric Spatial Audio Understanding for Wearable Microphone Arrays](http://arxiv.org/abs/2610.05610v1)
  <details><summary>📄 Abstract</summary>
  Embodied, ego-centric intelligence fundamentally requires the ability to comprehend spatial audio within complex environments. While large audio-language models excel at mono-channel reasoning, they lack spatial awareness, discarding critical spatial cues that enable sound localization and that can improve the disentanglement of overlapping sound sources. To address this, we present SEA-LM, a Spatial Audio Understanding model. First, we introduce FOACODER, a layout-flexible spatial audio encoder...
  </details>

- **2026-10-04** — Sheng Cheng, Donnchadh M. O'Sullivan, Daniel J. Penny et al. — [EchoDino: A pediatric foundation model for transferable echocardiographic analysis across the lifespan](http://arxiv.org/abs/2610.05603v1)
  <details><summary>📄 Abstract</summary>
  Echocardiography is the most widely used cardiac imaging modality, yet interpretation demands integrating visual evidence across global anatomy, localized structures and dynamic cardiac motion. Machine-learning models have automated individual tasks, but they are typically built for a single purpose and depend on expensively labeled datasets - a barrier particularly acute in pediatric care, where data are scarce and anatomy changes with age. Here we present EchoDino, a self-supervised foundation...
  </details>

- **2026-10-04** — Hanyang Hu, Zekai Liang, Florian Richter et al. — [Robust Surgical Robotic Instrument Tracking via Sequential Multi-Cue Fusion and Sim-to-Real Self-Training](http://arxiv.org/abs/2610.05491v1)
  <details><summary>📄 Abstract</summary>
  Efficient and robust tracking of surgical robotic instruments is important for robot-assisted minimally invasive surgery, yet remains challenging due to the complexity of surgical scenes and the unconventional geometry of surgical instruments. Keypoint-based approaches are efficient, but their performance depends on reliable feature detection. Improving these detectors with real-world supervision is difficult because accurate real-world annotations are costly to obtain at scale. To address this ...
  </details>

- **2026-10-04** — Chao Huang, Pengfei Wei, Benfeng Wang et al. — [RoMod: Temporal Routing Modulation via Mixture-of-Experts for Video Anomaly Detection](http://arxiv.org/abs/2610.05131v1)
  <details><summary>📄 Abstract</summary>
  Intermediate-layer features from multimodal large language models have shown strong potential for video anomaly detection (VAD), yet the origin of their discriminative power remains unclear. We study this question using sparse mixture-of-experts (MoE) models, whose explicit expert structure and sparse activation make their internal computation easier to inspect. With a fully frozen backbone and no additional training, we find that anomaly-related evidence is concentrated in a small set of expert...
  </details>

- **2026-10-04** — Jiahao Ying, Wei Tang, Boxian Ai et al. — [Belief-Trajectory Energy: Measuring the Path to a Prediction](http://arxiv.org/abs/2610.05114v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) progressively revise their predictions across Transformer layers, yet we typically observe only the final output, discarding the trajectory through which it is formed. We introduce Belief-Trajectory Energy(BTE), a model-grounded measure that characterizes an input through the layerwise predictive revisions it induces in a model. By mapping intermediate states into a shared predictive space, BTE provides a principled measure of belief change that can be summarized as ...
  </details>

- **2026-10-04** — Baoxi Liu, Yi Xie — [TSAE: Structured Sparse Autoencoders for Interpreting Time-Series Forecasting Models](http://arxiv.org/abs/2610.04925v1)
  <details><summary>📄 Abstract</summary>
  Time-series forecasting informs critical decisions in energy dispatch, industrial operations, and environmental monitoring; understanding the patterns models rely on is essential for assessing reliability and identifying failures. Input attribution identifies important variables and time segments but offers limited insight into internal features, while standard sparse autoencoder (SAE) objectives do not directly constrain cross-variable structure or temporal continuity. We introduce TSAE, a stru...
  </details>

- **2026-10-03** — Xiang Li, Aichun Huang, Mingming Zhang et al. — [When Talk Isn't Code: Comparing LLM Agents That Simulate and Develop Software](http://arxiv.org/abs/2610.04639v1)
  <details><summary>📄 Abstract</summary>
  LLMs are used both to simulate network protocol implementations, as honeypots do, and to write them. Prior work evaluates the two uses separately, from a model's answers or conversations in one case and from its generated code in the other. We observe that a knowledge probe (asking the model which security checks an implementation needs) and a conversation can credit security checks that the generated program lacks, but no study has compared them with the code the same model writes. To fill this...
  </details>

- **2026-10-03** — YaJie Yin — [The Same Zero: Why Identical ASR Can Imply Different Guarantees in LLM-Agent Security](http://arxiv.org/abs/2610.04504v1)
  <details><summary>📄 Abstract</summary>
  LLM-agent security has produced a dense landscape of defenses - prompt hardening, content filters, permission gates, sandboxes - yet no framework tells a deployer what a defense actually guarantees, or where that guarantee comes from. We apply Verification Autonomy Levels (VAL) - L0: LLM self-declaration; L1: deterministic rules; L2: objective ground truth; L3/L4: decidable completeness; L5: impossible - to 22 agent-security defenses; the taxonomy is falsifiable (10/10 prediction hits on frozen ...
  </details>

- **2026-10-03** — Kimon Antonios Provatas1, Christos Galanopoulos, Ilias Georgakopoulos-Soares — [Tracing model-generated DNA with position-independent watermarking](http://arxiv.org/abs/2610.04763v1)
  <details><summary>📄 Abstract</summary>
  Genomic language models can write synthetic DNA that carries no record of its origin. A generation-time watermark could provide a provenance signal, if a verifier can detect it using only the DNA sequence, a key, and published detector settings, without knowing where the generated region starts, which strand it lies on, or how it was divided into six-base tokens. We embed the SynthID tournament watermark in two genomic language models, Carbon and GENERator-v2. The verifier searches both strands,...
  </details>

- **2026-10-03** — He Yang Yuan, Haonan Zhang, Xin Wang et al. — [Towards Automatically Pruning Logging Code with Coding Agents: How Far Are We?](http://arxiv.org/abs/2610.04716v1)
  <details><summary>📄 Abstract</summary>
  Logging code supports debugging, monitoring, and software maintenance, but excessive logging can add noise, impose runtime overhead, and obscure diagnostic information. While prior research has extensively studied logging code generation and modification, logging removal remains comparatively underexplored. In this paper, we study developer logging removal practices and explore the use of coding agents for this task. We extract and manually validate logging removal cases from Python and Java rep...
  </details>

- **2026-10-03** — François Hublet, David Basin, Srđan Krstić — [Practical Runtime Enforcement of First-Order Temporal Requirements](http://arxiv.org/abs/2610.04611v1)
  <details><summary>📄 Abstract</summary>
  Runtime enforcers observe a system's behavior and exert control over it to ensure that the system always adheres to its requirements. Many natural requirements not only formulate restrictions on the system's present behavior, but also impose obligations on its future behavior; for instance, agentic security may require personal data collected during a run to be erased by some deadline. In an ever-growing compliance landscape, real-world systems may be subject to hundreds of such requirements. Ho...
  </details>

- **2026-10-03** — Xueping Gao — [From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents](http://arxiv.org/abs/2610.04575v1)
  <details><summary>📄 Abstract</summary>
  Activation probes can predict safety-relevant properties of language models with high area under the receiver-operating-characteristic curve (AUROC), but deployed agent monitors make thresholded alarm decisions under tight false-alarm budgets. These are different estimands. We introduce an Operational Validity Contract that fixes a monitor's target, observability, identity, timing, intervention unit, comparator, calibration, and cost. We formalize risk at the semantic request or trajectory level...
  </details>

- **2026-10-03** — Ansuman Mullick, Eray Tüzün — [Knowing the Store: What a Memory Backend Must Write Down Before an Agent Can Read It](http://arxiv.org/abs/2610.04794v1)
  <details><summary>📄 Abstract</summary>
  An agent with long-term memory can answer from a record it should no longer use, such as a plan the user later cancelled. We ask what a memory store must expose for an agent to know this before retrieving anything, and we score that judgment on its own, as metamemory monitoring. Readers see only a value-free summary: record counts by lifecycle state and a list of attribute names. Each of 148 questions is asked against three versions of one store that differ in one attribute, so wording cannot gi...
  </details>

- **2026-10-02** — Yukiya Horiba, Koshiro Aoki, Shunsuke Yasuki et al. — [Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](http://arxiv.org/abs/2610.03498v1)
  <details><summary>📄 Abstract</summary>
  Adversarial patches can disrupt Vision-Language-Action (VLA) models by manipulating visual observations, leading to failures in robot control. However, it remains poorly understood which internal mechanisms underlie these failures and how targeted interventions can mitigate them. In this work, we mechanistically analyze VLA representations using a sparse autoencoder (SAE) and identify a feature whose activation strongly correlates with the presence of an adversarial patch. Based on this analysis...
  </details>

- **2026-10-02** — Mohammadhossein Homaei, Yousef Emami, Sajad Homayoun et al. — [Defense-in-Depth at the Perception-Reasoning Interface of LLM-Centric Agentic UAV Swarms](http://arxiv.org/abs/2610.03319v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly support Uncrewed Aerial Vehicle (UAV) swarm operations such as data collection scheduling, where the model reads structured sensor reports and decides which sensors to visit. An adversary who quietly manipulates those reports can redirect the swarm without modifying the model weights or the UAV. Defenses for this interface have been proposed architecturally but rarely implemented or evaluated. We implement and evaluate defense-in-depth at the perception-...
  </details>

- **2026-10-02** — Lijie Ding, Changwoo Do — [NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents](http://arxiv.org/abs/2610.03631v1)
  <details><summary>📄 Abstract</summary>
  Designing a scientific instrument tests whether language-model agents can do physics rather than recall it, provided the grading cannot be argued with. We introduce NeutronGym, to our knowledge the first executable environment for neutron instrument design: agents build instruments through validating tools, McStas ray-traces what they build, and a level-resolved ladder grades syntax, runtime, structure and science with no LLM judge. Procedural families supply unlimited instances of a fixed layou...
  </details>

- **2026-10-02** — Vasco Ramos, Sandra Godinho Silva, Joao Magalhaes et al. — [DEPICT: Scoring Text-to-Image Alignment by Answer Agreement](http://arxiv.org/abs/2610.03617v1)
  <details><summary>📄 Abstract</summary>
  Image-text alignment is a core problem in computer vision with applications in caption evaluation, hallucination detection, data curation, and the benchmarking of text-to-image (T2I) generators. As T2I models improve, benchmarking has become demanding, requiring metrics capable of finding a series of issues like missing objects, swapped attributes, miscounts, and ignored negations. Recent work addresses this by fine-tuning evaluators on preference data or by prompting a vision-language model, ei...
  </details>

- **2026-10-02** — Mattia Piana, Stefano Rini, Stefano Tomasin — [FedSwitch: Federated Region Classification From Wireless Channel Measurements](http://arxiv.org/abs/2610.03523v1)
  <details><summary>📄 Abstract</summary>
  Wireless Internet-of-Things (IoT) networks can leverage locally observed channel state information (CSI) at base-stations (BSs) to perform region classification, i.e., infer the region of origin of a transmitter (TX), thereby enabling channel-based authentication. However, centralizing these measurements incurs substantial communication overhead and requires sharing location-dependent radio fingerprints. To address these difficulties, we propose an edge-native federated learning (FL) framework w...
  </details>

- **2026-10-02** — Joery Ariën de Vries, Neil David Lawrence, Zhenwen Dai — [Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT](http://arxiv.org/abs/2610.03361v1)
  <details><summary>📄 Abstract</summary>
  Critic-free reinforcement fine-tuning (RFT) for agentic large language models is often done through GRPO-style methods, which compute a group baseline over repeated rollouts to reduce target variance. However, this setup is ill-suited to agents acting in stateful environments such as live services or security sandboxes, where repeated rollouts are impractical to obtain and aggressive updates entrench the noise of long, sparsely verified trajectories. We propose \textit{Follow the Winners} (FTW),...
  </details>

- **2026-10-02** — Mohsen Larni, Sobhan Ebrahimi Azar, Pouyan Nahed et al. — [SyntaxBench: A Statistical Diagnostic Framework for Character-Level Reasoning in Large Language Models](http://arxiv.org/abs/2610.03329v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used where small syntactic errors matter, yet character-level reasoning is still evaluated mostly through isolated probes and aggregate accuracy. We introduce SyntaxBench, a diagnostic benchmark and statistical evaluation framework for character-level reasoning. It contains five core tasks, character counting, letter containment, palindrome detection, edit distance, and longest-string selection, plus index_to_span, a harder substring-extraction stress test....
  </details>

- **2026-10-02** — Mingjun Zhang, Yucheng Li, Menghao Zhang et al. — [VenusRL: A Fully Disaggregated Agentic RL System with Priority Scheduling and Scalable Interaction](http://arxiv.org/abs/2610.03286v1)
  <details><summary>📄 Abstract</summary>
  Agentic Reinforcement Learning (RL) trains LLM agents through multi-turn interactions with external tool environments. Its multi-turn nature exposes two system-level bottlenecks unaddressed by existing agentic RL frameworks. First, end-to-end training throughput is constrained by the slowest trajectories to complete, yet optimizing per-GPU utilization alone scatters rollout progress across many groups, delaying the completion of enough groups to unblock the next training step. Second, tool sandb...
  </details>

- **2026-10-02** — Chahira Benhama, Mohand Saïd Allili, Assia Hamadene — [Interpretable Deepfake Detection in Videos via Explicit Forensic Features and Temporal Modeling](http://arxiv.org/abs/2610.03380v1)
  <details><summary>📄 Abstract</summary>
  Deepfake detection in videos remains challenging, as manipulated content may appear visually consistent at the frame level while exhibiting subtle temporal inconsistencies. This paper introduces an interpretable deepfake detection framework that models spatially and temporally coherent facial features in video sequences. Unlike end-to-end deep models relying on implicit representations, the proposed approach explicitly encodes physically grounded forensic cues, enabling transparent analysis and ...
  </details>

- **2026-10-01** — Tian Dong, Zixuan Ma, Haodong Zhao et al. — [Chaining Skills to Hijack LLM Agents](http://arxiv.org/abs/2610.01564v1)
  <details><summary>📄 Abstract</summary>
  LLM agents use skills to improve performance on specialized tasks. To complete a user request, an agent may invoke several skills in sequence, allowing information produced under one skill to guide the next. Because skills may come from open-source repositories, this handoff can also carry attacker-controlled claims into later decisions. In this paper, we introduce APEX, which constructs and refines adversarial skill chains tailored to a user task and an attacker-selected action. The key insight...
  </details>

- **2026-10-01** — Negin Ashrafi, Jia Luo, Stacey M. Frumm et al. — [OpenMTB-Audit: Exposing Over-Refusal and Clinical Expert Perspectives in LLM-Based Molecular Tumor Board Safety Evaluation](http://arxiv.org/abs/2610.01497v1)
  <details><summary>📄 Abstract</summary>
  Molecular tumor boards integrate genomic findings, clinical context, and therapeutic evidence to support precision oncology. As AI enters this workflow, a key safety challenge is distinguishing truly unsupported recommendations from evidence-supported options that still require oncologist review because of incomplete information, poor ECOG performance status, or other clinical caveats. We introduce OpenMTB-Audit, an open-source benchmark of 500 synthetic non-small cell lung cancer cases spanning...
  </details>

- **2026-10-01** — Pengfei Li, Naufal Suryanto, Sicheng Zhang et al. — [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards](http://arxiv.org/abs/2610.02206v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations. However, existing evaluations focus on knowledge-based assessments or end-to-end agentic tasks, and do not directly measure LLMs' ability to generate executable commands for real-world cybersecurity tools. This gap is critical because cybersecurity operations rely on strict command-line interfaces (CLIs), where minor syntax errors, incorrect flag--value bindings,...
  </details>

- **2026-10-01** — Hosam Elgendy, Utkarsh Mall — [From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support](http://arxiv.org/abs/2610.01870v1)
  <details><summary>📄 Abstract</summary>
  Urban environments are shaped by design choices with long-term implications for health, safety, and quality of life, yet evaluating proposed interventions remains costly, time-consuming, and often impractical. Existing geospatial vision methods largely focus on monitoring urban indicators from aerial and street-view imagery, rather than proposing interventions and estimating their effects on such indicators. Moving beyond recognition, we introduce the problem of discovering interventions that im...
  </details>

- **2026-10-01** — Daniel E. Garcia-Fernandez, Pablo Vera-Soto, Sergio Fortes et al. — [DRL-driven RAN Slicing Management: A V2X-oriented Approach In Multi-service Scenarios](http://arxiv.org/abs/2610.01424v1)
  <details><summary>📄 Abstract</summary>
  The integration of Vehicle-to-Everything (V2X) communications is driving a profound transformation in vehicular connectivity, expected to significantly enhance traffic efficiency and safety. However, the stringent requirements of V2X services, particularly ultra-low latency and high reliability, present significant technical challenges. 5G's Network Slicing emerges as a key enabler by providing tailored virtual networks that ensure isolation and adaptability for heterogeneous services. This work...
  </details>

- **2026-10-01** — Giulio Zeloni, Enrico Lo Conte, Salvatore Rionero et al. — [AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation](http://arxiv.org/abs/2610.01218v1)
  <details><summary>📄 Abstract</summary>
  Enterprises adopting retrieval-augmented generation (RAG) face a recurring operational decision: promote, revise, or block a system version. The evidence is incomplete and the metrics come from fallible LLM judges. We report on AGO AI Quality Gate (AGO), an evidence-first quality-gate framework deployed in industrial RAG assessment engagements. AGO integrates four key components: a four-state decision model that treats missing data and judge errors as explicit outcomes; layered scoring combining...
  </details>

- **2026-10-01** — Sehrish Basir Nizamani, Deepika Devaraj, Tien Nguyen et al. — [WIP: DBWorkout: A Gamified SQL Practice Platform to Support Formative Learning in Database Courses](http://arxiv.org/abs/2610.01174v1)
  <details><summary>📄 Abstract</summary>
  This research WIP paper presents DBWorkout, a web-based platform that supports formative SQL learning through sandbox-based execution, automated result-based feedback, and session-based gamification. Learning Structured Query Language (SQL) remains challenging for undergraduate students due to limited opportunities for interactive practice and immediate feedback. Students iteratively practice SQL on live database instances while receiving multi-dimensional feedback on query correctness, includin...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 61 papers

- **2026-10-05** — Omer Dahary, Etai Sella, Hadar Averbuch-Elor et al. — [Learning to Read the Contextual Tokens in Diffusion Transformers](http://arxiv.org/abs/2610.06844v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Lar...
  </details>

- **2026-10-05** — Jiawen Du, Arshan Ali Khan, Chenhao Zhang et al. — [Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs](http://arxiv.org/abs/2610.06685v1)
  <details><summary>📄 Abstract</summary>
  Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither be traced to their evidence sources nor removed to measure their contributions. We present MM-KG (Multimodal Knowledge Graph), which represents heterogeneous, multimodal patient observations and biomedical concepts as separate layers in one typed graph, joined by explicit alignment edges. First, mo...
  </details>

- **2026-10-05** — Yoel Zeldes — [Closing the Context Gap: Activation Alignment for Tabular In-Context Learning](http://arxiv.org/abs/2610.06679v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models perform in-context learning (ICL) by conditioning predictions on labeled training examples provided as context. Unlike traditional models that separate training from inference, these models must process all training examples in every forward pass, making each prediction expensive. Restricting the number of training examples reduces this cost but substantially degrades performance. Instead of discarding context, we propose activation alignment, a method that leverages th...
  </details>

- **2026-10-05** — Akansh Maurya, Ya-Wei Eileen Lin, Stefanie Jegelka et al. — [Training-Free Transformer Merging via Sequential Local Operator Alignment](http://arxiv.org/abs/2610.06415v1)
  <details><summary>📄 Abstract</summary>
  Training-free model merging aims to combine multiple fine-tuned models into a single model without further optimization on labeled data. Yet, in transformers, independently merging individual layers can affect a shared attention computation because the query-key and value-output operators depend on composed matrices, overlooking the functional structure. Moreover, when merging earlier components, downstream components receive different activations than they do in the original model, thus, the me...
  </details>

- **2026-10-05** — Viviana Centritto~Arrojo, Ama Bandara, Sergi Abadal et al. — [Reinforcement Learning-Based 3D Beam Adaptation for Underwater Wireless Optical Communication with AUVs](http://arxiv.org/abs/2610.06407v1)
  <details><summary>📄 Abstract</summary>
  Underwater Wireless Optical Communications (UWOC) provide essential high data rates for Autonomous Underwater Vehicles (AUVs), but reliable connectivity is critically affected by transmitter-receiver misalignment. This work addresses the beam pointing problem for a moving AUV subject to unknown ocean currents through a Deep Reinforcement Learning (DRL) framework. We develop a comprehensive 3D UWOC channel model incorporating depth-dependent attenuation, turbulence, and a discrete-ray method to a...
  </details>

- **2026-10-05** — Zhongxiang Sun, Jiahao Yan, Hongkang Zhao et al. — [What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents](http://arxiv.org/abs/2610.06406v1)
  <details><summary>📄 Abstract</summary>
  As agents take on long-horizon tasks, users shift from making individual decisions to overseeing autonomous execution. Yet the volume of agent activity and the fragmentation of supporting evidence make it difficult to determine which decisions warrant user verification. We study monitors that identify consequential decisions and locate evidence to help users assess their implications. We introduce AgentMonBench, a software-engineering benchmark comprising three subsets that cover two complementa...
  </details>

- **2026-10-05** — Aditya Tanna, Abhishek Jindal — [Ontology Concept Overlap as a Training Signal: Knowledge-Grounded Reinforcement Learning for Clinical Question Answering](http://arxiv.org/abs/2610.06360v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning post-training for language models relies on two reward designs: human preferences (RLHF, DPO) and binary verifiers (RLVR). Clinical question answering fits neither. Near-correct answers differ by a single substituted entity, and no executable check decides clinical correctness. We instantiate a soft verifier from a maintained controlled vocabulary: UMLS Concept Unique Identifier overlap (via scispaCy, set-level F1) gives a graded, externally specified reward computed witho...
  </details>

- **2026-10-05** — Shanglin Li, Shiwen Chu, Okan Koç et al. — [SPDAlign: Interpretable Riemannian Alignment for EEG Forward Modeling Shifts](http://arxiv.org/abs/2610.06315v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) based brain-computer interfaces enable direct brain-to-device communication for applications such as rehabilitation and communication. However, their practical utility is often limited as the non-stationary nature of the EEG data introduces distribution shifts across domains (e.g., sessions and subjects). Adapting machine learning models to be invariant to these shifts in an unsupervised way, without using costly labeled calibration data, would drastically improve th...
  </details>

- **2026-10-05** — Mohammad Salahshour — [Hydrodynamics of perceptual matter: from neural representations to collective motion](http://arxiv.org/abs/2610.06249v1)
  <details><summary>📄 Abstract</summary>
  How do neural representations of neighbors become collective material behavior? Harmonic Theory (HT) reduces bearing representations to signed perceptual channels traceable to sensory acuity, decision dynamics, and interaction distance. Here we derive a nonlocal kinetic and hydrodynamic theory from the HT particle law without introducing heading alignment. The resulting fields retain HT's order-resolved perceptual spectrum and keep the neural and sensory origin of each coefficient visible. The t...
  </details>

- **2026-10-05** — Benjamin Robson, Santeri Mentu, Wenshuai Zhao et al. — [LeAVJEPA: A Minimalist Architecture for Audio-Visual Self-Supervised Learning](http://arxiv.org/abs/2610.06226v1)
  <details><summary>📄 Abstract</summary>
  Prior audio-visual self-supervised learning methods rely on mechanisms such as EMA target encoders, prediction heads, reconstruction decoders, and contrastive losses. We introduce LeAVJEPA, the first audio-visual encoder trained under LeJEPA's collapse-free objective. A single early-fusion Vision Transformer processes audio, video, and joint audio-video inputs. Modality dropout treats a missing modality as another view of the same event, making cross-modal alignment implicit in the objective. Th...
  </details>

- **2026-10-05** — Yiming Xu, Hao Cheng, Monika Sester — [MoCAR: Motion-code Coordinate-aware AutoRegression for Continuous Trajectory Forecasting](http://arxiv.org/abs/2610.06210v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive generation is natural for language, where predicted tokens can be directly reused as the next prediction state, but trajectory forecasting lacks such a clean token: motion is continuous, multimodal, and expressed in local coordinate frames that evolve with the predicted trajectory. We present MoCAR (Motion-code Coordinate-aware AutoRegression), a decoder-only framework that casts trajectory forecasting as next-code prediction in a coordinate-aware continuous latent space. MoCAR le...
  </details>

- **2026-10-05** — Jonathon Cottom, Emilia Olsson — [State aligned graph wavelet fingerprints of electron trapping in amorphous Si$_3$N$_4$](http://arxiv.org/abs/2610.06173v1)
  <details><summary>📄 Abstract</summary>
  Classifying charge traps in amorphous materials requires the electronic state and the network response to be resolved together. We develop state-aligned graph-wavelet fingerprints and apply them to electron trapping in a-Si$_3$N$_4$, where intrinsic-polaronic trapping, coordination-driven trapping, and charge-driven conversion coexist within one ensemble. Across 415 pairs of relaxed neutral and negatively charged cells, alignment of the trap state before and after localisation connects electroni...
  </details>

- **2026-10-05** — Xinnuo Xu — [Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?](http://arxiv.org/abs/2610.06078v1)
  <details><summary>📄 Abstract</summary>
  This paper asks whether VLA generalization is grounded in a global understanding of objects' physical properties that enables policies to adapt their motion to unseen setups, or if policies simply replay the motions they've learnt that happen to succeed in new setups. The former reflects genuine generalization; the latter reflects incidental robustness. We first examine awareness of physical properties in seven VLAs by applying linear probing and representational similarity analysis (RSA) to the...
  </details>

- **2026-10-05** — Giulia Benintendi, Constantin Ruhdorfer, Fabian Kögel et al. — [Grounded Joint-Attention Other-Play for Zero-Shot Coordination](http://arxiv.org/abs/2610.06025v1)
  <details><summary>📄 Abstract</summary>
  Joint attention - the human ability to share a common visual or cognitive focus with others - enables a meeting of minds that lets us coordinate even with unfamiliar partners. In this work we investigate whether equipping AI agents with a similar mechanism can enable such zero-shot coordination. We introduce Mutual Attention for zero-shot TEaming (MATE): a novel multi-agent reinforcement learning method inspired by human joint attention. MATE encourages agents to coordinate their actions by alig...
  </details>

- **2026-10-05** — Yihe Zhao, Songhe Feng — [From Transformation to Target State: Rethinking Query Representation for Zero-Shot Composed Image Retrieval](http://arxiv.org/abs/2610.05993v1)
  <details><summary>📄 Abstract</summary>
  Composed image retrieval (CIR) aims to retrieve a desired target image from a query consisting of a reference image and a modification text. This task exhibits an unusual representational asymmetry: the modification text specifies a transition from the reference state, whereas retrieval candidates depict completed target states. This creates a representation mismatch for zero-shot methods that query pretrained vision-language spaces directly with transformation-oriented language. We study this m...
  </details>

- **2026-10-05** — {Ermis Soumalias, Richard Mudd, Abbas Zaidi — [Incentive Alignment in Online Experimentation](http://arxiv.org/abs/2610.05922v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the causal effect of new features is a central goal for online platforms. While recent literature addresses limited testing traffic via centralized portfolio optimization, this perspective abstracts away a critical institutional reality: experimentation is operationally decentralized. The experimenters who develop new features also dictate which hypotheses to test, and they are typically rewarded based on empirical average treatment effects that are prone to upward bias. Left unchecke...
  </details>

- **2026-10-05** — Liyan Yang, Yige Yuan, Zhiqin Yang — [Collaborative Personalized Preference Alignment for LLMs under Data Deficiency](http://arxiv.org/abs/2610.05898v1)
  <details><summary>📄 Abstract</summary>
  Real-world users often exhibit highly heterogeneous preferences over multiple objectives for LLM responses. A lightweight aligner can tailor these responses to individual preferences, but scarce user-specific feedback makes personalized training difficult. Learning shared initializations across users can support few-shot adaptation. However, heterogeneous preferences and competing objectives cause gradient conflicts across users and within each user, hindering effective initialization learning. ...
  </details>

- **2026-10-04** — Minjae Lee, Kyunghyun Cho, Sangdon Park — [Which Preferences to Train On? End-to-End Multi-Objective Alignment with an Adversarial Preference Distribution](http://arxiv.org/abs/2610.04845v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) with human values is important for safe, efficient, and beneficial AI deployment. However, human values are multifaceted: helpfulness, harmlessness and humor trade off against one another, and different users want different trade-offs. Multi-objective alignment (MOA) addresses this by training a policy that can provide any point of the Pareto front, but existing methods either train one model per preference, interpolate a few separately aligned experts post ...
  </details>

- **2026-10-04** — Hao Li, Shashank Reddy, Kedar Bellare et al. — [SCOUT: Supply-Aware Cold-Start Proactive Query Suggestion for Travel Search](http://arxiv.org/abs/2610.05619v1)
  <details><summary>📄 Abstract</summary>
  Generative query suggestion, powered by Large Language Models (LLMs), has become increasingly popular in search and conversational systems to reduce user friction and guide intent formulation. Existing approaches align suggestions with user preferences (e.g., clicks or conversions). This works for open-ended applications like chatbots and personal assistants, where the result space is unconstrained or historical user free-text queries are abundant.   However, applying these methods to travel sea...
  </details>

- **2026-10-04** — Team Kandinsky, Julia Agafonova, Bulat Akhmatov et al. — [Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](http://arxiv.org/abs/2610.05608v1)
  <details><summary>📄 Abstract</summary>
  We present Kandinsky 6.0 Video, a family of foundation diffusion models for synchronized text-to-audio-video generation, comprising Kandinsky 6.0 Video Lite (3B parameters) and Kandinsky 6.0 Video Pro (29B parameters). Both models generate 5-second video clips with synchronized 44 kHz audio, including lip-sync, in text-to-audio-video (T2AV) and image-to-audio-video (I2AV) modes; a built-in super-resolution model raises the output resolution to Full-HD (1920$\times$1080). Building on the video ge...
  </details>

- **2026-10-04** — Jacob Brodkey, Roberto Tamez, Aaron Roth — [Groupwise Distortion Guarantees for Preference-Based Alignment](http://arxiv.org/abs/2610.05450v1)
  <details><summary>📄 Abstract</summary>
  Preference-based alignment methods such as reinforcement learning from human feedback (RLHF) and Nash learning from human feedback (NLHF) aggregate pairwise preferences to learn an LLM policy, but a natural goal is maximizing social welfare (average cardinal utility), which comparisons alone need not identify. Gölz, Haghtalab, and Yang (GHY) measure the gap by distortion: the worst-case ratio between the welfare of the best fixed lottery (distribution over responses) and of the learned lottery. ...
  </details>

- **2026-10-04** — Yuxin Liu, Yuxuan Wang, Zhenxin Lei et al. — [MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training](http://arxiv.org/abs/2610.05398v1)
  <details><summary>📄 Abstract</summary>
  Autonomous research seeks sustained model improvements through iterative experimentation and feedback. LLM agents show promise in automating machine learning and language-model post-training, but their ability to sustain multimodal improvement remains unclear. We introduce MMPostTrainBench, a benchmark spanning eight tasks in image, audio, video, and joint audio-video understanding and image-grounded software repair. Agents operate from a common base model within fixed budgets, using development...
  </details>

- **2026-10-04** — Zaiquan Yang, Fei Wei, Yong Wang et al. — [Towards Unbiased On-Policy Distillation for Block Diffusion Language Models](http://arxiv.org/abs/2610.05373v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has emerged as an effective post-training paradigm for language models, with recent efforts extending it to block diffusion language models (BDLMs). However, existing studies focus almost exclusively on small block sizes, leaving distillation into student models with larger blocks underexplored. In this work, we investigate this regime and reveal two critical optimization biases that induce severe training instability. First, mismatched block boundaries between teach...
  </details>

- **2026-10-04** — Akash Das, Ishan Roy — [Safe Context Switching for Agents in the Wild: Mitigating Subspace Interference via Orthogonal Adaptation](http://arxiv.org/abs/2610.05219v1)
  <details><summary>📄 Abstract</summary>
  Most Large Language Models exhibit a fundamental tension between two sequential tasks, such as logical reasoning and safety alignment. The high-variance internal states required for sophisticated Chain-of-Thought (CoT) deduction can geometrically interfere with latent representations encoding safety constraints. We identify this phenomenon as Sequential Subspace Interference, showing that standard fine-tuning on logical tasks such as multi-step mathematics and code generation can result in a 23....
  </details>

- **2026-10-04** — Dhia naouali — [Cross-Time Directional Selection in Diffusion Sampling](http://arxiv.org/abs/2610.05199v1)
  <details><summary>📄 Abstract</summary>
  How strongly do the remaining diffusion-sampling steps amplify a perturbation at a late latent state? Standard measurements answer this question with newly sampled isotropic noise, even though perturbations encountered during sampling have already been transformed by earlier steps. We compare these two cases directly. For each trajectory, we transport a centered perturbation from an earlier step to a late state, then replay its direction at the same magnitude as a newly sampled isotropic perturb...
  </details>

- **2026-10-04** — Chengxi She, Xingyu Lu, Yue Zhao et al. — [Ambiguity-Aware Multi-Agent Framework for Automated Operations Research under Logical Inconsistency](http://arxiv.org/abs/2610.05169v1)
  <details><summary>📄 Abstract</summary>
  Operations research (OR) problems are often described by stakeholders with incomplete knowledge and vague expressions in real-world settings. Such ambiguous descriptions can not be used to formulation directly. Thus, automating OR problems solving requires processing this logical inconsistency in advance. To address this challenge, we propose an \textbf{A}mbiguity-Aware \textbf{M}ulti-Agent Framework for \textbf{A}utomated \textbf{O}R Problem Solving, \textbf{AMAO}, which first addresses logical...
  </details>

- **2026-10-04** — Uri Berger, Gal Chechik, Gal Dalal — [Look Where You Say You're Looking: Self-Grounded Attention for Visual Reasoning](http://arxiv.org/abs/2610.05023v1)
  <details><summary>📄 Abstract</summary>
  We introduce Self-Saliency, a method for training Vision-Language Models (VLMs) to increase the alignment between their visual attention and the image regions mentioned in their reasoning. Self-Saliency uses a grounding model to localize the objects mentioned in each reasoning step and treats the resulting areas as supervision for the model's visual attention. Previous work on steering visual attention determines target image regions based solely on the image and question. In contrast, we show t...
  </details>

- **2026-10-04** — Mirae Han, Sihyeong Yeom, Harksoo Kim — [IREA: Intermediate Representation-based Embedding Alignment for Normative RAG](http://arxiv.org/abs/2610.04974v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong performance across various tasks, but they still struggle with questions involving ethical judgment. Previous studies have attempted to train LLMs on ethical standards, but the diversity and relativity of ethical norms make them difficult to fully internalize in model parameters. As an alternative, we introduce normative RAG, a retrieval-augmented approach that supports ethical judgment using external normative knowledge. Normative retrieval involve...
  </details>

- **2026-10-04** — Ruiyan Xu, Haisheng Su, Sixu Lin et al. — [$R^2$-WAM: Repair-and-Reject Post-Training for World Action Models](http://arxiv.org/abs/2610.04913v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) emerge as a promising foundation for policy refinement by predicting the consequences of sampled actions. However, visually plausible predictions can mislead policy refinement if they fail to reflect the input actions. To address this mismatch, we introduce $R^2$-WAM, a two-stage repair-and-reject post-training framework that first improves the consistency of predicted futures with input actions, then uses these futures to select inferior action samples for negative fi...
  </details>

- **2026-10-03** — Zongye Hu, Weiqing Luo, Yanjie Fu et al. — [Not All Answers Are Contextually Persuadable: Inference Dynamics in Large Language Models under Contextual Influence](http://arxiv.org/abs/2610.04791v1)
  <details><summary>📄 Abstract</summary>
  At the core of modern prompting techniques is contextual sensitivity, the ability of large language models to adapt their predictions based on inference-time context. Despite its central role, inference behavior under strong contextual influence remains poorly understood, particularly at the level of internal inference dynamics. We introduce a theoretical framework for analyzing contextual influence through inference dynamics, enabling quantitative characterization of inference behavior beyond o...
  </details>

- **2026-10-03** — Cinzia Tomaselli, Mario di Bernardo — [Safe Leader-Follower Density Control via Higher-Order Mean-Field Control Barrier Functions](http://arxiv.org/abs/2610.04733v1)
  <details><summary>📄 Abstract</summary>
  Safety filters for large-scale multi-agent systems can be formulated at the population level through mean-field control barrier functions (MF-CBFs). Most existing formulations are first-order, requiring the control input to appear explicitly in the first time derivative of the safety functional; higher-order extensions have only very recently been proposed for a single, directly actuated population. We consider instead the case in which the population to be kept safe is not directly actuated, bu...
  </details>

- **2026-10-03** — Bangwei Guo, Xujiang Zhao, Shengyu Chen et al. — [Knossos and Ariadne: Benchmarking and Learning Complete Diagram Topology Extraction with Vision-Language Models](http://arxiv.org/abs/2610.04721v1)
  <details><summary>📄 Abstract</summary>
  Structural diagrams are widely used to represent complex systems and relational information across scientific, engineering, procedural, and spatial domains. Recent vision-language models (VLMs) have become increasingly capable of recognizing diagram elements and reasoning about their content, while complete diagram topology extraction remains comparatively underexplored. In this paper, we study diagram-to-graph topology extraction: extracting all diagram entities and the complete relations among...
  </details>

- **2026-10-03** — Rabeya Khatun Muna, Muhammad Ahasanuzzaman, Nakhla Rafi et al. — [RETRACE: From Entangled Repair Histories to Reusable Experience for CI Repair](http://arxiv.org/abs/2610.04658v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly reuse prior experience, but most approaches assume that problems and solutions are already aligned. Software histories rarely provide this alignment: a pull request (PR) may contain multiple continuous integration (CI) problems, failed attempts, reverted edits, and unrelated changes, obscuring which changes resolve each problem. We present RETRACE, a framework for reconstructing problem-level repair experience from such histories. RETRACE combines a...
  </details>

- **2026-10-03** — Francesco Correnti, Gabriele Magrini, Marco Mistretta et al. — [WASP: Weakly Aligned Spatiotemporal Pairs for Fetal Brain MRI-Ultrasound Learning](http://arxiv.org/abs/2610.04601v1)
  <details><summary>📄 Abstract</summary>
  Magnetic Resonance Imaging (MRI) is widely regarded as the optimal sensor for fetal brain analysis due to its superior soft-tissue contrast and anatomical detail. However, its high cost and operational burden make it invasive and difficult to obtain at scale. Ultrasound (US), in contrast, is cheap, safe, and routinely acquired, and as a result it has produced substantially larger datasets and a growing ecosystem of pretrained models. This asymmetry raises a natural question: Can we teach a US-on...
  </details>

- **2026-10-03** — Hoigi Seo, Byung Hyun Lee, Minjun Kim et al. — [Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs](http://arxiv.org/abs/2610.04580v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal large language models (MLLMs) achieve strong modality understanding by pairing a large language model (LLM) with an encoder for a target modality such as vision, video, or audio. However, improving an MLLM's capability for a given modality typically requires additional training on large modality-specific datasets, incurring substantial data collection and compute costs. Model merging offers an alternative, but it is often infeasible for data-scarce, large per-sample size, or domain-s...
  </details>

- **2026-10-03** — Qichen Zheng, Siyuan Yang, Chong Wang et al. — [TAME:Topology-Aware Text-Driven Motion Editing across Heterogeneous Humanoid Skeletons](http://arxiv.org/abs/2610.04529v1)
  <details><summary>📄 Abstract</summary>
  Text-driven motion editing modifies an existing motion sequence according to a text instruction while preserving the content of the source motion. Existing methods are typically built for a single, fixed skeletal topology, which limits their use in animation pipelines where characters differ in joint count and skeletal hierarchy. We present Topology-Aware Motion Editor (TAME), a flow-matching transformer that edits motions on humanoid skeletons of varying topology. TAME represents motion as per-...
  </details>

- **2026-10-03** — Hasan Farooq, Murtaza Taj, Mehwish Nasim et al. — [Localization Lens for Improving Medical Vision-Language Models](http://arxiv.org/abs/2610.04502v1)
  <details><summary>📄 Abstract</summary>
  Medical Vision-Language Models (Med-VLMs) have demonstrated strong capabilities in clinical tasks. However, they often struggle to understand anatomical structures and spatial positioning, which are crucial for medical reasoning. To address this, we propose a localization-aware enhancement to the Med-VLM pipeline, introducing improvements at three levels: data,architecture, and alignment. First, we introduce localization lens, a set of expert-validated representations that provide richer anatomi...
  </details>

- **2026-10-03** — Murat Ozer, Isaac Kofi Nti — [Pressure, Context, and Machine Self-Control: A Criminological Test of Reward Hacking in Generative AI Models](http://arxiv.org/abs/2610.04793v1)
  <details><summary>📄 Abstract</summary>
  Recent incidents show that AI agents sometimes reach measured goals through unsanctioned means. This study applies self-control, general strain, anomie, neutralization and routine activity theory to reward hacking in generative AI models, and it treats the measures as behavioral analogues. Study 1 (2,310 conversations, seven models) measured delay discounting with the Kirby Monetary Choice Questionnaire and stated willingness to take shortcuts. Pressure raised the discount rate k 2.8-fold in fre...
  </details>

- **2026-10-02** — Linghui Shen, Tinghui Zhu, Sheng Zhang et al. — [ProAR: Learning Prospective Reasoning with Autoregressive Video Models](http://arxiv.org/abs/2610.03664v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive (AR) video models excel at causal generation, but their reliance on next-chunk prediction confines them to a short-sighted, reactive paradigm. This limitation is particularly consequential for reasoning-oriented generation, where achieving a target outcome through valid intermediate states matters more than local visual plausibility. To address this challenge, we propose Learning Prospective Reasoning with Autoregressive Video Models (ProAR), a novel framework that transforms auto...
  </details>

- **2026-10-02** — Parastoo Ali Pour, Deepak Prakash Kumar, Tommy Zhou et al. — [CORNAV: Construction-Aware Reasoning for Robot Navigation on Active Worksites](http://arxiv.org/abs/2610.03622v1)
  <details><summary>📄 Abstract</summary>
  The construction industry faces persistent labor shortages, low productivity that costs the global economy over $1.6 trillion annually, and one of the highest injury rates among major industries. These factors motivate the use of autonomous robots to improve efficiency and worker safety. Existing language-grounded navigation systems, however, rely on semantic scene understanding alone and lack access to construction-specific context such as architectural plans, evolving work schedules, and safet...
  </details>

- **2026-10-02** — Ziyi Wang, Junchi Yao, Heqian Qiu et al. — [Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation](http://arxiv.org/abs/2610.03510v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in autoregressive video generation have improved temporal consistency over extended durations, yet interactive storytelling requires more than continuous scene extension: a new shot may combine characters and backgrounds from different historical shots. Whole prompt retrieval can overlook the distinct reference needs of individual components, while directly combining all historical memories may introduce unrelated visual content. To address these problems, we present Weave Forcin...
  </details>

- **2026-10-02** — Kyra Watts, Natasha Popenoe, Benjamin Gerard et al. — [Design, Fabrication, and Free-Space Characterization of a Two-Photon-Polymerized Nano-printed Photonic Lantern](http://arxiv.org/abs/2610.03484v1)
  <details><summary>📄 Abstract</summary>
  Photonic lanterns provide an interface between multimode optical fields and arrays of single-mode waveguides, making them promising components for modal filtering, wavefront sensing, and high-contrast astronomical instrumentation. We present the design, simulation, two-photon-polymerization fabrication, and free-space characterization of a compact photonic lantern optimized for operation at $ 1050~\mathrm{nm} $. The device was designed to transform a multimode input into five nominally single-mo...
  </details>

- **2026-10-02** — Hang Gao, Wujiang Xu, Zhixing Zhang et al. — [CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented Generation](http://arxiv.org/abs/2610.03421v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have shown strong visual reasoning abilities, but knowledge-intensive visual question answering often requires external textual evidence beyond the image and the model's parametric knowledge. Existing multimodal RAG systems commonly rely on Top-$K$ retrieval or reranking, which may return redundant passages and provide limited control over whether an answer update is sufficiently supported by the retrieved evidence. We propose \textit{CLIMB}, a training-f...
  </details>

- **2026-10-02** — Linh-An Phan, MingXue Wang, Guangyu Wu et al. — [Lightweight, Rubric-Guided Trajectory Evaluation for Production AI Agents](http://arxiv.org/abs/2610.03315v1)
  <details><summary>📄 Abstract</summary>
  Trajectory evaluation is essential for improving the reliability of LLM-based agents, but production use makes it expensive to run repeatedly. Modern agents generate long traces containing tool calls, observations, retries, and external outputs, while not all raw tokens are equally useful for diagnosis. We present \textit{LiteTrajEval}, a lightweight architecture for budget-bounded trajectory evaluation. LiteTrajEval derives compact domain-specific rule profiles offline, then preprocesses each t...
  </details>

- **2026-10-02** — Hebao Zhu, Dongxia Wu — [Architecture-Dependent Fusion Pathways in MLLMs](http://arxiv.org/abs/2610.03289v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) achieve strong performance across vision-language tasks, yet the internal mechanisms by which visual and textual information are fused across layers remain insufficiently understood. We investigate representative MLLMs from two architectural paradigms: concatenation architectures and native multimodal architectures. We conduct three progressively connected analyses: alignment decoupling identifies which modality changes, attention routing and entropy char...
  </details>

- **2026-10-02** — Vladislav Gromadskii, David Li, Samson Gourevitch et al. — [IDRF: Inverse-Distilled Reward Fine-tuning of Masked Discrete Diffusion Models](http://arxiv.org/abs/2610.03641v1)
  <details><summary>📄 Abstract</summary>
  Masked discrete diffusion models offer a promising alternative to autoregressive generation, but iterative sampling can be costly, and intractable sequence likelihoods complicate reward fine-tuning. We introduce IDRF, a framework for reward fine-tuning of few-step masked discrete diffusion generators. Starting from a standard reverse-KL-regularized objective, IDRF replaces the intractable sequence-level KL penalty with inverse-distillation regularization. With an optimal auxiliary denoiser, we p...
  </details>

- **2026-10-01** — Danqing Wang, Songwen Zhao, Harsh Sharma et al. — [AuraForge: Scaling Security Supervision for Training Coding Agents](http://arxiv.org/abs/2610.00850v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are now proficient enough to generate complex software applications from a single prompt. As their capabilities have grown, human oversight has increasingly shifted from line-by-line code review toward hands-off evaluation of outcomes. However, recent studies have shown that such a transition exposes a critical risk: functional correctness alone does not guarantee a secure implementation. Despite growing attention to code security, training safer coding agents remains challenging b...
  </details>

- **2026-10-01** — Yakun Zhu, Yi Bin, Yujuan Ding et al. — [GeoLatent: Geometry-Guided Latent Structuring with Routed Optimization for 3D Reasoning](http://arxiv.org/abs/2610.02091v1)
  <details><summary>📄 Abstract</summary>
  Despite progress in vision-language models, 3D spatial reasoning from 2D images remains challenging. Text-based methods describe intermediate geometry with discrete tokens, limiting fidelity for continuous spatial relations. Continuous latents offer richer representations, but a single latent type does not explicitly separate the cues needed across spatial tasks. Decomposed spatial latents address this by representing position, direction, and global geometry separately under geometric supervisio...
  </details>

- **2026-10-01** — Lucas Bandarkar, Clark Peng, Ahmed Haj Ahmed et al. — [Cross-Lingual Alignment for Decoder-Only Models using MoE Routers](http://arxiv.org/abs/2610.01921v1)
  <details><summary>📄 Abstract</summary>
  Cross-lingual contrastive learning has been a core component of multilingual encoder training, but the ability to explicitly align representations is not possible in decoder-only LLMs because of varying multilingual tokenization. However, a growing amount of research suggests that even in LLMs, higher cross-lingual representational alignment leads to improved cross-lingual transfer. In this paper, we propose a novel approach to reimagine cross-lingual contrastive learning given the architectural...
  </details>

- **2026-10-01** — Dhanunjaya Varma Devalraju, Arshdeep Singh, Mark D. Plumbley — [AVSD-Scenes: A Dataset for Audio-Visual Description of Urban Scenes](http://arxiv.org/abs/2610.01861v1)
  <details><summary>📄 Abstract</summary>
  Natural language descriptions can provide rich semantic representations of audio-visual urban scenes, yet datasets that jointly describe both auditory and visual information remain limited. In this paper, we introduce AVSD-Scenes, a paired audio-visual scene description dataset for urban environments. The dataset contains 12,291 audio-visual scene descriptions generated from the TAU Urban Audio-Visual Scenes dataset. To construct the dataset, we first generate audio- and visual-based description...
  </details>

- **2026-10-01** — Zichen Xie, Mrigank Pawagi, Lize Shao et al. — [Detecting Inconsistencies in Model Specifications with LLM-as-Verifier Reasoning](http://arxiv.org/abs/2610.01847v1)
  <details><summary>📄 Abstract</summary>
  Model specifications define how large language models (LLMs) should behave, guiding alignment training, inference-time behavior, and evaluation. Yet these specifications may themselves contain defects: two individually reasonable principles may prescribe incompatible behavior when applied to the same situation, leaving no response that satisfies both. Detecting such inconsistencies is challenging. Formalizing natural-language specifications risks losing subtle distinctions, while behavior-based ...
  </details>

- **2026-10-01** — Haricharan Balasundaram, V. Arvind Rameshwar — [The Asymptotics of Language Model Alignment with Memory](http://arxiv.org/abs/2610.01828v1)
  <details><summary>📄 Abstract</summary>
  Language model (LM) alignment broadly aims to perturb a given LM $Q$ into an aligned LM $q$ such that i) the outputs produced by $q$ and $Q$ are 'close' in probability, ii) $q$ has a higher expected reward than $Q$. Two common techniques for LM alignment are: KL-constrained RL, which requires knowledge of the LM distribution and is computationally expensive, and the best-of-$n$ algorithm, which requires only sampling from the LM. The work of Yang et al. established asymptotic closeness between t...
  </details>

- **2026-10-01** — Sahil Kadadekar — [A Safe Prototype Is Not a Safety Direction: Reference Dependence and Prompt Confounds in Response-Safety Embeddings](http://arxiv.org/abs/2610.01801v1)
  <details><summary>📄 Abstract</summary>
  Can response safety be scored by cosine similarity to the mean embedding of known-safe responses? A recent sleeper-agent detector proposes exactly this score, yet the raw positive-centroid rule is not identified: positive observations locate the safe class relative to an encoder origin, but do not determine which direction separates safe from unsafe responses. We audit the rule on two prompt-controlled, human-labeled corpora and one auxiliary jury-labeled source control, using four frozen encode...
  </details>

- **2026-10-01** — Haoxin Wu, Xiaokai Bai — [FFBL-Coop: Association-Decoupled Cooperative 3D Multi-Object Tracking](http://arxiv.org/abs/2610.01750v1)
  <details><summary>📄 Abstract</summary>
  Cooperative 3D tracking must integrate complementary observations across agents and time while maintaining consistent identities. When evidence integration and identity inheritance share a matching decision, errors arising from cross-view appearance differences and spatial misalignment can compromise both feature fusion and track continuity. We propose FFBL-Coop, a fuse first, bind later framework that separates instance admission from identity management. Confidence-ranked Slot Admission (CSA) ...
  </details>

- **2026-10-01** — Marco Saponara, Axel Abels, Ann Nowé et al. — [Conditioning LLMs on Social Value Orientation improves behavioural alignment in a sequential social dilemma](http://arxiv.org/abs/2610.01667v1)
  <details><summary>📄 Abstract</summary>
  Large language Models (LLMs) are increasingly used to simulate human decision-making, yet their outputs often under-represent human behavioural heterogeneity. We investigate whether conditioning LLMs on Social Value Orientation (SVO, a measure of how individuals value their own outcomes relative to others') can better reproduce human behaviour in a sequential social dilemma. Using experimental data from two variants of the Centipede Game (CG) as reference, we compare the default behaviour of eig...
  </details>

- **2026-10-01** — Akira-Miranda Adeyomi Adeniran-Lowe, Binod Singh, Lars Arnold Dethlefsen et al. — [PAGER: Partial-to-global Alignment via Geometric and Relational Distillation](http://arxiv.org/abs/2610.01589v1)
  <details><summary>📄 Abstract</summary>
  Pretrained 3D encoders are typically developed on globally reconstructed scenes expressed in a consistent world coordinate frame, whereas embodied systems must reason from partial, viewpoint-dependent observations in camera coordinates. We show that this shift from globally learned 3D feature spaces to realistic partial observations exposes a severe representation mismatch, which we find consistently across representative state-of-the-art encoders, including Sonata and Concerto. A frozen Sonata ...
  </details>

- **2026-10-01** — Yu Huang, Jungang Li, Zhiyuan Wang et al. — [VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation](http://arxiv.org/abs/2610.01499v1)
  <details><summary>📄 Abstract</summary>
  Recent video generation models can produce highly realistic videos from natural language instructions, with visual quality approaching cinematic standards. Existing evaluation benchmarks, however, predominantly assess visual quality, aesthetic appeal and physical plausibility, while paying limited attention to text, an essential medium for conveying information in everyday scenes. A generated video may appear visually compelling and feature lifelike subjects, yet still render the text within the...
  </details>

- **2026-10-01** — Jiazhen Hong, Xiaotian Zhou, Zihao Ding et al. — [CortexBridge: Cortical Alignment of EEG Montages for Foundation Models](http://arxiv.org/abs/2610.01124v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) foundation models are often pretrained with a fixed channel vocabulary or a limited set of montages, making transfer difficult when electrode layouts change. We propose CortexBridge, a lightweight adapter that combines EEG features with electrode and atlas coordinates to map arbitrary montages into a shared cortical latent space. Evaluated with three frozen foundation models on five brain-computer interface (BCI) datasets from the Mother of All BCI Benchmarks (MOABB)...
  </details>

- **2026-10-01** — Bi'an Du, Zhimin Zhang, Daizong Liu et al. — [HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction](http://arxiv.org/abs/2610.01056v1)
  <details><summary>📄 Abstract</summary>
  Sparse view 3D reconstruction is an important and common scenario in multimedia applications, such as augmented reality/virtual reality (AR/VR) content creation, cultural heritage digitization, and certain robotic applications, where only a limited number of randomly captured views may be available. However, sparse views contain only limited 3D information, posing two major challenges:1) too few images are available for matching, making it difficult to build multi-view consistency; 2) insufficie...
  </details>

- **2026-10-01** — Haiming Zhao, Tai Wang, Kun Zhang et al. — [Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack](http://arxiv.org/abs/2610.00973v1)
  <details><summary>📄 Abstract</summary>
  Science teachers frequently search for documentary excerpts not by describing what appears on screen, but by querying the abstract concepts they intend to teach. This use case exposes a limitation of existing language-based video moment retrieval methods, which typically assume that queries describe observable events, whereas instructional search requires retrieving concrete visual phenomena that instantiate an underlying scientific principle. We study this setting as concept-to-example video re...
  </details>

- **2026-10-01** — Haochen Zhang, Laura Yao, Zachary Plotkin et al. — [LineupRL: Verifiable Reinforcement Learning for Time Series Captioning via Caption-to-Series Identification](http://arxiv.org/abs/2610.01800v1)
  <details><summary>📄 Abstract</summary>
  Time series captioning is a fundamental step in time series understanding and can also serve as the bridge between signal and natural language. Supervised fine-tuning (SFT) relies on a larger model's captions and cannot exceed their quality. Reinforcement learning (RL) can, but its rewards were designed for other modalities and other tasks, and they transfer poorly to open-ended generation in the time series domain. We address this by proposing LineupRL, a reinforcement learning with verifiable ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 55 papers

- **2026-10-05** — Tiffany Gu, Annie Guan, Manshu Huang et al. — [Request Order Matters: Cache-History Sensitivity in Selective KV-Cache Reuse for Rolling Agents](http://arxiv.org/abs/2610.05833v1)
  <details><summary>📄 Abstract</summary>
  Long-running agents repeatedly call an LLM while retaining most of their document window, evicting old documents, and appending new ones. These rolling updates break exact prefix caching and motivate non-prefix KV-cache reuse with selective recomputation. We show that persistent KV-cache reuse with selective recomputation can be history-dependent: in our rolling-agent workload, an unchanged prompt can produce different answers depending on the requests processed before it. At a matched 5% recomp...
  </details>

- **2026-10-05** — Shovan Roy, Lopamudra Praharaj, Maanak Gupta et al. — [Agentic-ZTA: A Multi-Agent Architecture for Autonomous Zero Trust Enforcement](http://arxiv.org/abs/2610.05782v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is emerging as a promising paradigm for automating complex cybersecurity decisions, yet its use in enforcing zero trust introduces significant challenges in safety, reliability, and policy compliance. This paper presents Agentic AI based zero trust architecture (Agentic-ZTA) that operationalizes the NIST SP 800-207 ZTA architecture control loop through coordinated multi- agent decision pipeline. In the proposed framework, policy knowledge is embedded into a retrieval-augmented generat...
  </details>

- **2026-10-05** — Benjamin D. Kim, Wanrong Zhang, Weitong Ruan et al. — [SimpleMark: Fast Multi-Bit Text Watermarking under f -Divergence Constraints](http://arxiv.org/abs/2610.05712v1)
  <details><summary>📄 Abstract</summary>
  We introduce a framework for multi-bit text watermarking with security defined directly through $f$-divergence from the base language model distribution. Unlike prior approaches that focus on average-key distortion-freeness or a particular statistical distance, our formulation supports general $f$-divergences, including total variation and KL divergence, and enforces the guarantee for each realized key and embedded message. We develop a coding-based watermarking scheme that optimally biases next...
  </details>

- **2026-10-05** — Zhicheng Ding, Xinyu Chu, Qing Tian — [Difference Feature Map Distillation: Transferring Inter-Sample Relational Knowledge Towards Efficient Transformer-Based Tracking](http://arxiv.org/abs/2610.05707v1)
  <details><summary>📄 Abstract</summary>
  In autonomous driving perception, visual object tracking systems must satisfy stringent latency and power constraints while remaining robust in complex and dynamic environments. Although transformer-based trackers achieve state-of-the-art accuracy, their substantial computational and memory overheads hinder deployment on real-time, resource-constrained platforms. To move toward this goal, we propose Difference Feature Map Knowledge Distillation (DFM-KD), a novel relational distillation framework...
  </details>

- **2026-10-05** — Ziqi Han, Yitang Li, Junhan Sun et al. — [I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning](http://arxiv.org/abs/2610.06129v1)
  <details><summary>📄 Abstract</summary>
  Behavioral foundation models (BFMs) have recently shown that a single humanoid policy can support diverse whole-body control, but extending such generality to physical interaction remains challenging. We introduce I-BFM, to our knowledge the first BFM for humanoid-object interaction. Rather than relying on task-specific policies or reference tracking, I-BFM learns a shared representation of the coupled dynamics among the humanoid, objects, and their contacts using forward-backward representation...
  </details>

- **2026-10-05** — Seonghoon Yu, Dongwon Kim, HyungRok Jung et al. — [When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models](http://arxiv.org/abs/2610.05719v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models serve as unified policies for robotic manipulation, yet their expensive inference forces robots to pause between policy calls, resulting in stop-and-go execution that interrupts smooth motion and prolongs task completion. Extending the action chunk reduces policy calls and hence these pauses, but predicting farther into the future makes long-chunk execution unreliable. To understand where this unreliability arises, we analyze action errors within long chunks a...
  </details>

- **2026-10-05** — Zhimin Shao, Xijun Liu, Zhaoliang Zhang et al. — [Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models](http://arxiv.org/abs/2610.06813v1)
  <details><summary>📄 Abstract</summary>
  Recent progress in 3D foundation models has enabled rapid 3D reconstruction and camera calibration by leveraging learned 3D priors from vast amount of spatial data. However, the all-to-all global attention design leads to quadratic complexity and limits long-sequence inference; unconstrained cross-view interactions also can propagate unreliable evidence from occluded or visually similar but geometrically distant views. In this paper, We introduce a Masked Geometric Encoder (MGE), which promotes ...
  </details>

- **2026-10-05** — Matthias Vigl, Nikita Pond, Jackson Barr et al. — [How to scale your HEP ML models: A recipe for robust architecture comparisons at scale](http://arxiv.org/abs/2610.06784v1)
  <details><summary>📄 Abstract</summary>
  Much of the recent progress in machine learning domains such as language models has come from scaling laws that predict performance as a function of training effort. In high-energy physics (HEP) similar behavior has now been observed. To aid further study, we present a systematic procedure to derive robust scaling laws and compare design choices on the relevant budget axes for HEP tasks. We first validate the full scaling trajectory on toy problems and then apply the procedure to multi-task tran...
  </details>

- **2026-10-05** — Feilian Huang — [The Review Lottery: Calibrating an Observational Estimator of Peer-Review Noise (ICLR 2017-2025)](http://arxiv.org/abs/2610.06591v1)
  <details><summary>📄 Abstract</summary>
  How much of a conference accept/reject decision would change if the same paper were reviewed by a different set of reviewers? Running a second independent program committee is the gold standard for answering this, but it is prohibitively expensive: done only twice (NeurIPS 2014 and 2021). We build an observational estimator of this quantity from public review data alone, calibrate it twice, and apply it to nine years of ICLR (2017-2025; 36,113 papers, 134,912 reviews). The estimator decomposes s...
  </details>

- **2026-10-05** — Aadam Haq, Oggi Rudovic, Malcolm Chadwick et al. — [Mind the Accent Gap: British Accent Robustness in Speech-Driven Financial Voice Assistants](http://arxiv.org/abs/2610.06587v1)
  <details><summary>📄 Abstract</summary>
  AI voice assistants often use Automatic Speech Recognition (ASR) with LLM-based reasoning, yet existing systems struggle with regional British accents, including Scottish, Irish, and Welsh accents, since most ASR models are trained predominantly on American English voice data. Consequently, errors can carry through to the LLM stage, corrupting tool-call arguments and producing wrong or missing responses, which is especially costly in finance. Deployable ASR must also meet tight latency and memor...
  </details>

- **2026-10-05** — Jiaqi Xue, Yanjun Wang, Xiangci Li et al. — [AECP: Artifact-Exclusive Communication Protocol for Multi-Agent Code Generation](http://arxiv.org/abs/2610.06481v1)
  <details><summary>📄 Abstract</summary>
  As AI agents increasingly tackle complex repository-level coding tasks, distributing work across multiple agents is a natural way to scale beyond the capabilities of a single agent. To coordinate their interdependent work, these agents share findings and agree on interfaces between modules. However, exchanged information often serves only as context, leaving individual agents to interpret it and incorporate it into subsequent work. Consequently, shared findings may go unused and deviations from ...
  </details>

- **2026-10-05** — Chengbo Zang, Haoyu Dong, Mehmet Kerem Turkcan et al. — [Dynamic Minimax Regret Optimization for Robust LLM Post-Training](http://arxiv.org/abs/2610.06329v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM training increasingly relies on heterogeneous data sources spanning different domains, tasks, preference distributions, and difficulty levels. We study dynamic minimax regret for group-distributionally robust LLM post-training under instantaneous mini-batch-only bandit feedback. The framework views the training as a two-player sampler-optimizer process: a sampler adaptively selects among data sources using bandit feedback, while an optimizer updates the model parameters using stochast...
  </details>

- **2026-10-05** — Qiutong Chen, Yuchan Guo, Zhenlong Yuan et al. — [VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction](http://arxiv.org/abs/2610.06293v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated remarkable potential in video understanding, yet their reliance on retrospective summarization and text-centric priors often limits their ability to bridge unobserved causal transitions when applied to Video Event Prediction (VEP). To address this, we propose VepAgent, an agentic framework that integrates causal-transition reasoning with tool-augmented reinforcement learning (RL) for robust VEP. Unlike prior methods that passively projec...
  </details>

- **2026-10-05** — Md Muhtasim Fuad, Mingyu Kim, Daniel J. Stilwell et al. — [Gamma-Laplace Surrogate for Variance Aware Sensor Placement for Detecting Poisson Distributed Targets](http://arxiv.org/abs/2610.06265v1)
  <details><summary>📄 Abstract</summary>
  Sensor placement for stochastically arriving targets is studied using a void probability objective, defined as the probability that no target remains undetected over a finite horizon. Direct optimization is intractable because it requires an expectation over a random intensity field. A common surrogate based on Jensen's inequality replaces the random field with its mean, yielding a tractable objective but discarding distributional information. The proposed Gamma Laplace surrogate approximates ce...
  </details>

- **2026-10-05** — Nataša Jovanović, Mathieu Salzmann, Saqib Javed — [CentriQ: Calibration-Free Quantization of Diffusion Transformers via Exact Mean Centering](http://arxiv.org/abs/2610.06260v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers (DiTs) achieve state-of-the-art image generation, but their sampling cost limits deployment. Quantizing both weights and activations to 4 bits reduces this cost, yet existing methods fall short in one of two ways. Calibration-based methods are tied to a specific checkpoint and prompt distribution, whereas data-free Hadamard rotation, effective for LLMs, loses quality on DiTs. We show that this loss has a structural cause. Adaptive layer-norm conditioning adds a per-token m...
  </details>

- **2026-10-05** — Yongxin Ning, Runliang Niu, Qianli Xing et al. — [Imagine to Act: High-Fidelity Data Synthesis via Image Editing World Model for Scalable GUI Agent Training](http://arxiv.org/abs/2610.05861v1)
  <details><summary>📄 Abstract</summary>
  Graphical User Interface (GUI) agents have emerged as a promising paradigm for automating complex digital workflows across diverse applications. However, training highly capable and generalizable agents fundamentally relies on massive, high-fidelity visual-action trajectories, which are notoriously difficult to acquire. While human demonstrations are unscalable, existing GUI world models rely on text descriptions or HTML rendering, discarding crucial pixel-level visual details like icons and lay...
  </details>

- **2026-10-05** — Cuong Dang, Hoang Anh Just, Ruoxi Jia — [Selecting Long-Horizon Trajectories for Reliable and Efficient Terminal-Agent Training](http://arxiv.org/abs/2610.05831v1)
  <details><summary>📄 Abstract</summary>
  Terminal agents are commonly trained by imitating long teacher trajectories, yet how much of each trajectory to supervise remains unexplored. We study the \emph{supervision horizon}, the number of trajectory tokens retained for training, and show that it is a key design axis for reliability and cost. Reliability improves with longer horizons but saturates: on Terminal-Bench, a 12K-token horizon solves more tasks than 16K ($29\pm0.7$ vs.\ $26\pm0.8$) while requiring 30\% less training time. The h...
  </details>

- **2026-10-05** — Md Aminur Hossain, Omkumar Vaghasiya, Rajeev Ranjan Dwivedi et al. — [FairRSFM: A Biome-Aware Benchmark and Debiasing Framework for Remote Sensing Foundation Models](http://arxiv.org/abs/2610.05790v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing foundation models (RSFMs) are commonly evaluated using aggregate metrics, which can hide systematic performance disparities across ecological regions. We introduce FairRSFM, a biome-aware benchmark for evaluating ecological group robustness in RSFMs. FairRSFM maps georeferenced samples from 14 terrestrial biome classes into six ecologically meaningful macro-groups and evaluates models under a unified frozen-backbone evaluation protocol. The benchmark covers four downstream dataset...
  </details>

- **2026-10-05** — Junhyun Nam, Wonse Jo — [Human-in-the-Loop Neuro-Symbolic Drift Anticipation for Reliable Visual SLAM](http://arxiv.org/abs/2610.05757v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces Hybrid DeepSEE (HDS), a Human-in-the-Loop (HITL) neuro-symbolic framework for proactive drift anticipation in Visual SLAM (V-SLAM). While data-driven models offer predictive power, their "black-box" nature often yields physically inconsistent outputs in out-of-distribution (OOD) environments. To address this, HDS integrates neural drift risk estimation with symbolic constraint reasoning. By utilizing a Large Language Model (LLM) as a reasoning bridge, the framework translat...
  </details>

- **2026-10-05** — Chanuka Dinuwan, Sanath Jayasena, Buddhika Karunarathne — [Automatic Speech Recognition for Low-Resource Sinhala: A Critical Review of Methods, Challenges, and Future Directions](http://arxiv.org/abs/2610.05681v1)
  <details><summary>📄 Abstract</summary>
  Automatic speech recognition (ASR) for low-resource languages remains a major challenge. Sinhala, the primary language of Sri Lanka with about 16 million speakers, illustrates the difficulty: agglutinative morphology, a 54-phoneme inventory, subject-object-verb (SOV) syntax and scarce annotated speech data limit both conventional and modern ASR systems. This paper presents the first critical review of Sinhala ASR research, tracing its development from Hidden Markov Models (HMMs) through deep neu...
  </details>

- **2026-10-04** — Qiushui Xu, Syamil Mohd Razak, Tao Yuan et al. — [VERA: Verdict-Conditioned Reliability for Adaptive LLM Judges](http://arxiv.org/abs/2610.05452v1)
  <details><summary>📄 Abstract</summary>
  Accurately estimating judgment reliability is a central challenge in adapting LLM judges to newly verified feedback while preserving previously learned behavior. However, existing approaches often rely on output-level confidence, which can be overconfident and poorly aligned with judgment correctness. We propose VERA, a VErdict-conditioned Reliability Axis that estimates reliability from hidden activations by distinguishing correct from incorrect judgments within each predicted-verdict group. Us...
  </details>

- **2026-10-04** — Jyh-An Lee, Xuan Sun — [The Law of DeepSeek](http://arxiv.org/abs/2610.05238v1)
  <details><summary>📄 Abstract</summary>
  Amid the intensifying competition in artificial intelligence between the United States and China, the emergence of the DeepSeek-R1 model has sent significant ripples through the technology sector, capital markets, and policy circles. This Article offers a comprehensive analysis of legal and policy landscape surrounding DeepSeek, drawing upon its key technical features-including reinforcement learning, mixture-experts architecture, multi-head latent attention mechanism, knowledge distillation, an...
  </details>

- **2026-10-04** — Ruqing Ning, Haibo Meng, Zhishang Xiang et al. — [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](http://arxiv.org/abs/2610.05162v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables LLM-based agents to retain and reuse information across tasks and sessions, supporting personalization and long-horizon interactions. However, persistent memories can also induce sycophancy, causing agents to over-align with users' historical beliefs even when they are inaccurate, outdated, or inconsistent with objective evidence. Existing mitigation methods assume that memory-induced sycophancy originates from biased or incorrect memories and attempt to reduce this risk...
  </details>

- **2026-10-04** — Dongki Kim, Namkyeong Lee, Surag Nair et al. — [AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents](http://arxiv.org/abs/2610.05140v1)
  <details><summary>📄 Abstract</summary>
  As agents rapidly evolve, existing benchmarks can become saturated, limiting their ability to distinguish capabilities and reveal remaining failure modes. Particularly in scientific domains, constructing and updating benchmarks requires substantial time, labor, and domain expertise, making it difficult to keep evaluation aligned with advances in agent capabilities. We address this challenge by investigating whether scientific-agent benchmarks can be automatically generated and iteratively adapte...
  </details>

- **2026-10-04** — Nodens Koren, Thomas Hofmann, Georgios Kissas — [METRO: Metric-Enhanced Token Routing Operator](http://arxiv.org/abs/2610.05100v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art neural operators scale to complex meshes via slice-and-process architectures, yet many rely on linear compatibility scores for latent tokenization. Under common feature normalization, such scores are equivalent to isotropic Euclidean clustering, while without normalization they induce unbounded linear decision regions. In both cases, they lack slice-specific anisotropic locality, which can lead to redundant and entangled latent slices. To address this, we propose Metric-Enhanced...
  </details>

- **2026-10-04** — Laurène Vaugrante, Thilo Hagendorff — [How Much Do LLM-as-a-Judge Design Choices Matter? A Systematic Comparison of Prompt Designs, Rating Scales, and Models](http://arxiv.org/abs/2610.05094v1)
  <details><summary>📄 Abstract</summary>
  Researchers increasingly use Large Language Models as judges (LLM-as-a-judge) to evaluate model outputs. Yet there are no standards for how to design these judges. Typically, researchers choose the prompt, rating scale, and model intuitively. If these choices change the judge's verdicts, two studies can reach different conclusions about the same facts. To address this risk and to provide an empirical basis for judge designs, we evaluate 10 reasoning models across multiple designs on two tasks: a...
  </details>

- **2026-10-04** — Yongyuan Peng, Zhou Feng, Tongying Wu et al. — [StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions](http://arxiv.org/abs/2610.05241v1)
  <details><summary>📄 Abstract</summary>
  LLM agents combine reasoning, tool use, and persistent memory to support work across tasks by reusing stored operational records as premises for later actions. However, environmental or requirement changes can invalidate these records, while existing action review, provenance tracking, and clarification mechanisms may leave the underlying persistent state uncorrected. Our audit of coding-agent trajectories identifies candidate failure chains in which invalid records are reused, leading to task f...
  </details>

- **2026-10-04** — Louis Agyekum — [Does the AI Productivity Dividend Diminish? Does the AI Productivity Dividend Diminish? A Validated Framework for Identifying the Shape of Firm-Level Returns to Artificial Intelligence](http://arxiv.org/abs/2610.05629v1)
  <details><summary>📄 Abstract</summary>
  Forecasts of the productivity dividend from artificial intelligence (AI) differ by an order of magnitude, partly because they extrapolate average gains observed among early, highly exposed adopters. Whether those gains scale linearly, flatten, or are competed away is an empirical question about the shape of the return to AI, not its average. This paper develops and validates a design-based framework for measuring that shape with linked firm-worker data. The framework combines a pre-determined, o...
  </details>

- **2026-10-04** — Jieqi Tu, Ruitao Lin, Ayon Mukherjee — [PKComb-BOIN12: A Pharmacokinetically Guided Bayesian Design for Dose Optimisation in Oncology Drug-Combination Trials](http://arxiv.org/abs/2610.05477v1)
  <details><summary>📄 Abstract</summary>
  Dose optimisation of two-agent combinations in early-phase oncology trials must jointly balance toxicity, efficacy, and pharmacologically meaningful drug exposure, yet existing model-assisted combination designs use only binary toxicity--efficacy outcomes and leave pharmacokinetic (PK) data unused for dosing decisions. We propose PKComb-BOIN12, a utility-based Bayesian optimal interval design embedding a continuous PK exposure metric into two-agent dose optimisation via a PK-guided escalation ru...
  </details>

- **2026-10-04** — Bogdan Bogachov, Nikita Letov, Yaoyao Fiona Zhao — [The Hidden States Cookbook: A Large-Scale Ablation Study for Noise-Robust Conversational Intent Classification in Industry](http://arxiv.org/abs/2610.05394v1)
  <details><summary>📄 Abstract</summary>
  Conversational database interfaces face a critical challenge: users naturally embed queries in conversational noise (greetings, politeness, off-topic remarks), which degrades intent classification accuracy and wastes computational resources. Despite advances in orchestration and retrieval strategies, a fundamental question remains unanswered: which pooling strategy maximizes intent classification accuracy under realistic conversational noise in production language models? This work addresses thi...
  </details>

- **2026-10-04** — Zhewei Fang, Yuxin Zhang, Zhenwei Shao et al. — [Sibyl: An Efficient Small-large Model Collaboration Framework for Long-horizon Tasks](http://arxiv.org/abs/2610.05383v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) offer a promising foundation for on-device agents through low-latency, resource-efficient inference, yet limited reasoning and planning capabilities constrain their performance on long-horizon tasks requiring multi-step interaction with the environment. Step-level collaboration between SLMs and larger cloud-hosted models can bridge this gap, but identifying states that warrant cloud assistance remains challenging: the contribution of each cloud call is entangled with...
  </details>

- **2026-10-04** — Hanzhang Wang, Tianqi Shen, Zonglin Liu et al. — [Understanding the Weight Averaging Mechanism in LLM Training for Post-Training Quantization](http://arxiv.org/abs/2610.05329v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are typically pretrained in high precision but increasingly deployed with low-precision post-training quantization (PTQ). Recent studies have shown that using weight averaging during pretraining can improve PTQ performance compared with learning-rate decay, suggesting that it might provide a simple way to improve the pretraining-to-quantization transition. But the mechanism behind weight averaging remains insufficiently explained. This leads to inconsistent and fragi...
  </details>

- **2026-10-04** — Kai Lv, Yibo Yin, Lijun Guo et al. — [ArticuTable: Generating Instance-Level Interactive Rigid-Articulated 3D Tabletop Scenes from a Single Image](http://arxiv.org/abs/2610.05249v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents benefit from 3D environments that combine visual fidelity to real-world observations with physical interactivity. Existing single-image tabletop reconstruction methods recover plausible scene geometry but typically represent objects as monolithic rigid bodies, limiting interaction to whole-object rigid motion and precluding executable part-level articulation. Meanwhile, recovering a scene layout consistent with the input view remains challenging because a single observation may a...
  </details>

- **2026-10-04** — Beniamino Cappelletti-Montano; Monica Musio; Nicola Piras — [Regression models for ordinal compositional data](http://arxiv.org/abs/2610.05212v1)
  <details><summary>📄 Abstract</summary>
  We present a unified, transformation-free linear regression framework tailored for ordinal compositional data, such as distributions across educational levels or aggregate Likert-scale survey responses. Traditional log-ratio approaches often obscure interpretability, ignore the inherent ordering of categories, and struggle with boundary zero values. To overcome these limitations, we propose a deterministic model constrained to the space of column-stochastic transformation matrices, naturally pre...
  </details>

- **2026-10-04** — Hongfei Du, Jiacheng Shi, Yanfu Zhang et al. — [Usage-Modulated Sentiment Representations in Large Language Models](http://arxiv.org/abs/2610.05069v1)
  <details><summary>📄 Abstract</summary>
  Prior work suggests that sentiment can often be captured by approximately linear directions in LLM activation spaces, but a single direction may not fully capture sentiment representations. In natural communication, sentiment is shaped not only by polarity but also by usage factors, such as tone and audience adaptation. We test whether these factors systematically modulate sentiment representations beyond a shared sentiment direction. We construct a controlled paired dataset that holds event con...
  </details>

- **2026-10-04** — Junjie Zhang, Shunyu Liu, Haoyu Wang et al. — [Causal Improvement Graph for Agentic Harness Optimization](http://arxiv.org/abs/2610.05039v1)
  <details><summary>📄 Abstract</summary>
  Agentic Harness is the runtime that constructs task context and controls execution flow, thereby shaping overall agent performance. Given a fixed model and external evaluation, automated Harness optimization seeks to improve this runtime through an iterative proposal--evaluation loop to better solve target tasks. Existing meta-harness methods mainly adopt proposer-centric discovery, in which an LLM-based proposer integrates accumulated experimental findings to determine subsequent Harness revisi...
  </details>

- **2026-10-04** — Benji Xu, Ken Zheng, Noah Han — [Viva La Vida: Verification and Accumulation Failures in Multi-Agent Proof Search](http://arxiv.org/abs/2610.04829v1)
  <details><summary>📄 Abstract</summary>
  When an agentic prover works on an open problem, there is no proof assistant to fall back on: its verifier and lemma library are ultimately language models judging model outputs. We instrumented such a system end to end and analyzed $51{,}754$ traced observations across three full runs ($186$ hours, \$$5{,}694$). We find three connected failure modes. First, the three-model verifier requires unanimity and treats parse or API failure as non-approval; in $10$ of $12$ verification events, one membe...
  </details>

- **2026-10-04** — Peng Qi, Chunliang Lyu, Gang Li et al. — [Agent Behavior as Code: Efficient and Robust LLM Agents with Programmatic Specifications](http://arxiv.org/abs/2610.04824v1)
  <details><summary>📄 Abstract</summary>
  AI agents based on foundation models (FMs) have demonstrated strong capabilities to perform complex open-ended tasks. However, they face some common challenges in practice: (a) agent behavior can deviate drastically even for semantically similar tasks, leading to catastrophically propagated errors; (b) high cost and latency due to FM calls, repeated in full whenever a task recurs with different inputs; (c) FMs' limited context and instruction following capability confine how well agents manage t...
  </details>

- **2026-10-03** — Songyuan Sui, Zhen Tan, Mohan Zhang et al. — [Do More Modalities Always Help? A Geometric Perspective on Missing-Modality Robustness](http://arxiv.org/abs/2610.04792v1)
  <details><summary>📄 Abstract</summary>
  Missing modality remains a longstanding challenge in multimodal learning. Existing methods typically address this issue through modality recovery or adaptive strategies. However, they overlook models' internal cross-modal dependencies formed during multimodal training, which later impair robustness. We systematically characterize a counterintuitive deployment-time failure mode: models trained on full modalities can underperform unimodal models when one modality is missing at inference time. This...
  </details>

- **2026-10-03** — Ananya Malik, Mai ElSherief — [Extracting Persona Subspaces Through Iterative Nullspace Projection For Modulation](http://arxiv.org/abs/2610.04676v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can adopt distinct personas to tune their semantics, expertise, and perspective to different users and tasks. Precise control over these traits is critical to ensure safety and reliability in model behavior. Existing methods like activation steering and prompt-based persona induction reduce a persona to a single dominant direction, missing the finer, nested traits that emerge only once that dominant signal is factored out. We introduce modulation as a setting where t...
  </details>

- **2026-10-03** — I-Chun Arthur Liu, Jason Chen, Gaurav S. Sukhatme et al. — [ExStereo: Lifting 2D Vision-Language-Action Models to 3D with Explicit Stereo Representations](http://arxiv.org/abs/2610.04805v1)
  <details><summary>📄 Abstract</summary>
  Three-dimensional perception is critical for robotic manipulation, particularly for high-precision tasks, as recovering metric depth and precise 3D object positions from monocular RGB observations is inherently ill-posed. However, many Vision-Language-Action (VLA) models rely solely on RGB observations for perception. Leveraging recent advances in foundation models for stereo matching, we introduce ExStereo, a stereo module that augments pre-trained 2D VLAs with 3D perception. ExStereo reconstru...
  </details>

- **2026-10-03** — Michal Štefánik, Marek Kadlčík, Josef Kuchař et al. — [Dynamic Routing as a New Dimension for Test-time Versatility of LLMs](http://arxiv.org/abs/2610.04751v1)
  <details><summary>📄 Abstract</summary>
  Beyond scaling their parameters and data, large language models currently gain versatility on new problems along a single axis: the tokens they spend on chain-of-thought (CoT). We investigate whether dynamic routing programs, which execute a subset of the model's layers or iterate some of them, can open a second axis of test-time adaptation, complementary to CoT and free of any gradient update. Prior work showed that such programs exist and bring accuracy and efficiency gains on problems similar...
  </details>

- **2026-10-03** — Tairan Wang, Earl T. Barr — [Back to the Future: Regressing Readability Features from LLMs](http://arxiv.org/abs/2610.04641v1)
  <details><summary>📄 Abstract</summary>
  Code readability supports software understanding, review, and maintenance. As AI coding agents become more widely used, readable code helps both humans review agent-generated output and agents maintain code within limited context windows. Yet existing readability models do not consistently agree with human judgements across datasets.   We introduce BTTF (Back To The Future), pairing linear regression with information-theoretic features. Rather than using language models as black-box judges, BTTF...
  </details>

- **2026-10-03** — Noor Islam S. Mohammad, Md. Basim Al Zabir Shammo, Hasan Siddiki et al. — [SIFT: Robust Meta-Faithfulness Verification of Chain-of-Thought Reasoning Under Distribution Shift](http://arxiv.org/abs/2610.04594v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) faithfulness detectors are widely used to audit reasoning models, yet a detector is itself a predictor whose verdicts are treated as stable properties. We ask whether a detector is faithful to itself under distribution shift. We formalize meta-faithfulness as an invariance principle: a valid detector must return identical verdicts on traces that differ only by transformations preserving ground-truth faithfulness. We prove three results: (i) no detector using only intervent...
  </details>

- **2026-10-03** — Tinghe Zhang, Chunyu Liu, Yu Leon Liu et al. — [Frozen in a Frame: The Velocity Blind Spot in JEPA World Models](http://arxiv.org/abs/2610.04585v1)
  <details><summary>📄 Abstract</summary>
  Joint-embedding predictive architectures (JEPAs) for world modeling train an encoder so a predictor maps a current embedding and action to the next frame's embedding, always from a single rendered frame. This has a structural blind spot: a renderer without motion blur draws a scene from configuration alone, so a single-frame embedding carries no velocity information, for any encoder, including the official released LeWM weights. We confirm this on official checkpoints across four real benchmarks...
  </details>

- **2026-10-02** — Chenzhi Liu, Yue Zhang, Jiehong Lin et al. — [MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](http://arxiv.org/abs/2610.03476v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon mobile manipulation presents significant challenges due to compounding execution errors and capacity interference between locomotion and arm control. While recent Vision-Language-Action models excel at short-horizon tasks, they lack the hierarchical reasoning required for multi-stage objectives. Furthermore, existing hierarchical agents suffer from rigid sub-task mapping, inflexible replanning, and a lack of continuous learning. To address these limitations, we introduce MobiAgent, ...
  </details>

- **2026-10-02** — William Kretschmer, Ewin Tang — [Unitary complexity in polynomial space](http://arxiv.org/abs/2610.03705v1)
  <details><summary>📄 Abstract</summary>
  We show that if quantum commitments exist, then either there is no polynomial-time solution to the unitary synthesis problem, or $\mathsf{BPP} \neq \mathsf{NEXP}$. Thus, showing unconditionally that quantum commitments exist would require answering at least one of two longstanding open questions in complexity theory. We prove our main result as a consequence of a more general lemma, which shows that every unitary in $\mathsf{unitaryPSPACE}$ either cannot be synthesized efficiently relative to an...
  </details>

- **2026-10-02** — Nudrat Habib, Tosin Adewumi, Sana Sabah Al-Azzawi et al. — [Author Representation Strategies for Zero-Shot Authorship Attribution: A Comparative Study of LLM-Based and Embedding-Based Approaches](http://arxiv.org/abs/2610.03531v1)
  <details><summary>📄 Abstract</summary>
  Authorship Attribution (AA) requires capturing fine-grained stylistic characteristics, making it particularly challenging in zero-shot (ZS) settings where no task-specific supervision is available. In this work, we investigate the effect of author representations on ZS AA by evaluating a label-only prompting baseline together with three author representation strategies: representative writing samples, LLM-generated descriptions, and style embeddings (LISA). The first three approaches perform att...
  </details>

- **2026-10-02** — Samuel Lewis-Lim, Xingwei Tan, Mario Sanger et al. — [Efficient Reasoning Training Does Not Always Harm CoT Faithfulness and Monitorability](http://arxiv.org/abs/2610.03509v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) reasoning allows humans to inspect how large language models reach their answers, and oversee model behaviour. This reasoning comes at an increased inference cost, motivating efficient methods that train models to solve tasks using fewer tokens. However, a common concern is that such training may cause models to skip important reasoning steps, so the CoT no longer faithfully reflects the model's decision. It is unclear whether or when this occurs in practice, since differe...
  </details>

- **2026-10-02** — Arghya Mallick, Reza Rahimi Baghbadorani, Peyman Mohajerin Esfahani et al. — [Learning in Inverse Games: Tractable Training with Probabilistic Guarantees](http://arxiv.org/abs/2610.03481v1)
  <details><summary>📄 Abstract</summary>
  Inverse game theory seeks to learn agents' unknown objectives from observed equilibrium behavior. Existing residual-based approaches can lead to non-convex problems and need not ensure strong monotonicity of the learned game, limiting reliable equilibrium prediction. We develop a tractable convex framework for learning static and dynamic non-cooperative games using first-order and Nikaido-Isoda (NI) loss. Specialized operator parameterizations, including a Helmholtz--Hodge decomposition in a rep...
  </details>

- **2026-10-02** — Luis Medrano-Navarro, Giacomo Baldan, Qiang Liu et al. — [Geometry Meets Physics: Data-Efficient Pre-Training for Unstructured Neural PDE Solvers](http://arxiv.org/abs/2610.03363v1)
  <details><summary>📄 Abstract</summary>
  Neural surrogate models for Partial Differential Equations (PDEs) on unstructured 3D geometries are often limited by poor generalization and the high cost of generating large-scale training datasets. Consequently, pre-training on massive datasets of related PDE dynamics has emerged as a critical alternative to enhance the robustness and scalability of these models. However, this strategy is neither compute- nor data-efficient, as it relies on massive pre-computed data that is very costly to gene...
  </details>

- **2026-10-02** — Nityanand Mathur, Hamees Sayed, Ayush Pratap Singh — [Refinement Buys Intelligibility, Search Buys Identity: What Test-Time Compute Buys in Masked-Diffusion TTS](http://arxiv.org/abs/2610.03320v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models for text-to-speech combine two forms of computation: model depth (parameters) and refinement steps (inference budget). We ask whether they scale equally across capabilities. We train 15 masked-diffusion codec TTS models varying depth (19-133M parameters, 3 seeds) on 2,000 hours of speech and sweep refinement steps T in [1,16] at inference, measuring zero-shot synthesis via ASR word error rate (intelligibility) and speaker verification (identity) on 174 held-out speakers...
  </details>

- **2026-10-01** — Zhangshu Joshua Jiang, Zina Ibrahim, James T. Teo — [A rubric landscape for evaluating clinical reasoning in large language models: what exists, what is missing, and what needs to be combined](http://arxiv.org/abs/2610.01938v1)
  <details><summary>📄 Abstract</summary>
  Exam-style accuracy does not establish whether large language models (LLMs) reason well over clinical records. We define clinical reasoning as integrating and updating evidence across time and sources to form, revise and justify a patient's problem representation and a defensible plan.   This structured narrative review maps three literatures: medical education assessment instruments, clinical LLM benchmarks published from 2023 onwards, and general-domain methods for evaluating long-form generat...
  </details>

- **2026-10-01** — Riccardo Ali, Alessio Borgi, Mario Severino et al. — [Let the Heads Talk: Beyond Diagonal Graph Attention](http://arxiv.org/abs/2610.01494v1)
  <details><summary>📄 Abstract</summary>
  Sheaf Neural Networks generalize scalar-weighted message passing by replacing scalar edge weights with linear transport maps between local feature spaces. Yet the role of this matrix-valued transport is entangled with the broader sheaf-diffusion construction. We isolate the transport primitive through quiver representations and establish a direct connection with multi-head attention. Treating attention heads as coordinates of a local transport space reveals that standard multi-head attention imp...
  </details>

- **2026-10-01** — Jingtan Wang, Sirajul Salekin, Young mok Jung et al. — [RISED: RubrIcs for agentic multi-environment Selection and sElf-Distillation](http://arxiv.org/abs/2610.00979v1)
  <details><summary>📄 Abstract</summary>
  Training a single LLM agent jointly across diverse interactive environments has attracted increasing attention as a route to generalist agents. Existing curriculum and data-selection strategies often allocate training at the environment level or prioritize local reward-based signals, without explicitly considering relationships between current rollouts across environments for prompt-group selection. Meanwhile, as environments are learned at different rates, all-failure and all-success rollout gr...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-10-05** — Jinglin He, Siyang Jiang, Lixing He et al. — [Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language Models](http://arxiv.org/abs/2610.06603v1)
  <details><summary>📄 Abstract</summary>
  Text from multiple sources can become interleaved into a single sequence when attribution metadata is lost, such as overlapping speech transcripts, document reading flows, or concurrent agent streams. We formalize this challenge as Word-Level Text Unmixing: given an interleaved lexical stream and source count K, recover the original source sequences while preserving every word occurrence and its within-source order exactly. Directly generating separated texts with LLMs can omit, duplicate, or ha...
  </details>

- **2026-10-05** — Xingbo Yao, Xiaoman Wang, Zhengwu Lei et al. — [ImproveAnyTask: An Autonomous Post-Training Harness for Iterative Model Self-Improvement](http://arxiv.org/abs/2610.06347v1)
  <details><summary>📄 Abstract</summary>
  Adapting general-purpose large language models to specific tasks requires substantial human effort in designing data and training strategies. Sustaining improvement is especially challenging because model updates change the error distribution, requiring strategies to be continually refined. We introduce ImproveAnyTask, an autonomous post-training harness that improves task performance under a limited compute budget. Drawing inspiration from gradient-based parameter optimization, the harness orga...
  </details>

- **2026-10-05** — Qiuhui Chen, Yibo Liu, Tao Dai et al. — [From Papers to Mechanisms: An Evidence-Grounded Knowledge Substrate for Scientific Language Models](http://arxiv.org/abs/2610.06248v1)
  <details><summary>📄 Abstract</summary>
  Scientific language models often access literature through untyped text chunks, which fragment the functional and evidential structure required for mechanism-rich questions. We introduce an evidence-grounded mechanism knowledge substrate that organizes scientific literature into provenance-linked evidence units, role-typed entities, and directed mechanism paths. We instantiate it as MS$^3$, a Material-Sensor-Signal-System schema for conductive-fiber flexible sensors, over 13,689 papers, 131,083 ...
  </details>

- **2026-10-05** — Judith Jeyafreeda Andrew — [Auditable Clinical Timeline Reconstruction with Provenance-Aware Evidence Graphs](http://arxiv.org/abs/2610.06177v1)
  <details><summary>📄 Abstract</summary>
  A patient-timeline reconstruction system is auditable only if it keeps the mentions behind each answer, records how facts were revised, and declines to answer when the evidence is not in the text. This study tests these three properties on a fully synthetic corpus (1,000 patients, 3,353 notes, 220 revision edges). Two provenance-aware Evidence Graph operators reduced the node-plus-edge count to 67% and 63% (77-78% of serialized size) while preserving every answer and mention link across 6,813 qu...
  </details>

- **2026-10-05** — Yunus Serhat Bıçakçı — [Vision Transformer Ensembles for Panoramic Street Segmentation](http://arxiv.org/abs/2610.06063v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult. This paper presents the system used for a first place submission to the PalmCity challenge in the leaderboard snapshot dated 5 October 2026. Nine pretrained segmentation systems are compared using approximately equal computation budgets. The candidates include DeepLabV3+, SegFormer, UPerNet, Mask2Former, DINOv3 with a lin...
  </details>

- **2026-10-05** — Junxiang He, Runze Mao, Kun He et al. — [RocketAgent: A Long-Horizon Engineering Agent for Multidisciplinary Design of Liquid-Rocket Thrust Chambers](http://arxiv.org/abs/2610.06044v1)
  <details><summary>📄 Abstract</summary>
  Liquid-rocket thrust-chamber design involves interdependent analyses in which downstream constraints can require earlier design decisions to be revisited. Managing these dependencies across heterogeneous tools requires consistent design information and coordinated updates throughout the workflow. We present RocketAgent, a long-horizon engineering agent for multidisciplinary preliminary design of liquid-rocket thrust chambers. A single plan-owning Coding Agent coordinates engineering skills for p...
  </details>

- **2026-10-05** — Weijie Miao, Henry Hong-Ning Dai, Ming Li — [H-CRSPV: Preventing Semantic Omission in Late-Bound Large Language Model Releases](http://arxiv.org/abs/2610.05989v1)
  <details><summary>📄 Abstract</summary>
  Large-language-model release pipelines increasingly combine commitments, signatures, provenance records, and heterogeneous verification backends. Yet validating every submitted object does not establish that a release realizes every requirement of its registered transformation. An untrusted realization proposer may omit a required relation, propose an unauthorized evidence-sharing assignment, or bind valid evidence to the wrong object. This verification-boundary failure is termed Semantic Omissi...
  </details>

- **2026-10-04** — Hongming Xu, Le Zhou, ZhongHe Jin et al. — [MemTrace: State-Consistent Memory for Long-Horizon Coding Agents](http://arxiv.org/abs/2610.04838v1)
  <details><summary>📄 Abstract</summary>
  As coding agents take on long-horizon software evolution tasks spanning multiple files and stages, longer execution trajectories introduce two coupled challenges: (1) accumulated histories strain context budgets, and (2) repository changes can invalidate earlier execution evidence. Existing approaches address these challenges through techniques like larger context windows, compression, retrieval, or repository representations, but often fail to reconstruct a consistent task state after a context...
  </details>

- **2026-10-04** — Hyundong Jin, Hyeseon An, Soohan Lim et al. — [Grammar-Guided Code Watermarking with Green Temperature](http://arxiv.org/abs/2610.05323v1)
  <details><summary>📄 Abstract</summary>
  Large language model watermarking embeds detectable statistical signals during decoding, but the resulting changes to token probabilities can degrade generation quality. This trade-off is particularly important for code, where small changes in token selection can break syntax or alter program behavior. Existing code watermarking methods mitigate this risk through entropy-based insertion or syntax-aware token selection, but they do not directly construct the watermark over the set of continuation...
  </details>

- **2026-10-04** — Jian Gu, Hongyu Zhang, Chunyang Chen et al. — [Mind the Gaps: From Failure Attribution to Closed-Form Repair of Code Language Models](http://arxiv.org/abs/2610.05277v1)
  <details><summary>📄 Abstract</summary>
  Code language models must be maintained like the software around them: when a library evolves, a model keeps writing the interface that it saw during training. Repairing the model itself lets one correction reach all downstream uses. Existing repair methods attribute a failure to neurons, select the highest-ranked ones, and apply a generic update. This pipeline assumes that the attributed neurons are the ones to patch and that a generic update fits every failure, and neither assumption has been ...
  </details>

- **2026-10-04** — Xiaotian Hu, Mingxuan Liu, Zhonghan Wang et al. — [templar: agentic induction and evolution of standardized radiology reporting templates from large-scale clinical corpora](http://arxiv.org/abs/2610.05247v1)
  <details><summary>📄 Abstract</summary>
  Structured radiology reporting mitigates the heterogeneity of free-text reports, yet its benefits depend on high-quality reporting templates. In practice, such templates are conventionally built through labor-intensive expert consensus and therefore vary across institutions and lag behind evolving clinical practice. Large language models (LLMs) enable automated template induction, but existing approaches remain limited: single-LLM induction is constrained by context length, and the corpus-scale ...
  </details>

- **2026-10-04** — Jinfeng Zhong — [GFGE: Unifying Explainable AI Methods through an Interpretation Framework](http://arxiv.org/abs/2610.05225v1)
  <details><summary>📄 Abstract</summary>
  Explainable artificial intelligence (XAI) encompasses methods that draw on different sources of information and address different explanatory needs. A common framework is needed to describe how this information becomes evidence and is communicated as an explanation for a particular recipient. We propose the General Framework for Generating Explanations (GFGE), grounded in interpretative frameworks and the complementary activities of \emph{sense-reading} and \emph{sense-giving}. Its conceptual fo...
  </details>

- **2026-10-04** — Yunhao Liang, Chengguang Gan, Ruixuan Ying et al. — [LLM-Based Test Generation: Information Sources, Generation Strategies, and Quality Evidence](http://arxiv.org/abs/2610.05001v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to generate test scenarios, executable test suites, assertions, interaction sequences, and fuzzing infrastructure. These artifacts serve different purposes and rely on different sources of information about correct behavior. A test that increases implementation coverage, a test that agrees with a reference program, and a test that detects a requirements violation therefore provide distinct kinds of evidence. We present a structured narrative survey tha...
  </details>

- **2026-10-04** — Qingwen Zeng, Zehao Fu, Shuyu Meng et al. — [ScopeSAE: Model-Scope Feature Discovery with Interpretable Layer Selection](http://arxiv.org/abs/2610.04905v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are a central tool in mechanistic interpretability. However, existing SAEs are primarily trained per layer. The modeling subspace is therefore fixed by layer identity, independent of which token-layer states actually drive each prediction. We argue that this constraint contributes to several limitations observed in layer-wise SAEs, including low feature utilization, high dictionary redundancy, and features that lack direct behavioral grounding. In this paper, we propos...
  </details>

- **2026-10-04** — Xinyue Zeng, Shivam Shandilya, Guilherme Potje et al. — [ForkPilot: Self-Evolving Policy for Retrospective Search in Long-Horizon Agents](http://arxiv.org/abs/2610.04889v1)
  <details><summary>📄 Abstract</summary>
  Interactive language-model agents increasingly solve complex tasks through long-horizon, multi-call reasoning, where errors in beliefs or actions can compound across tool interactions. Retrospective search can recover from such failures but is prone to misallocation. Delayed outcomes obscure the contribution of intermediate search decisions, leading to Attribution Complexity, while evolving execution evidence leads to Adaptation Complexity, where previously learned estimates become stale. To add...
  </details>

- **2026-10-02** — Teng Lin, Xinyu Liu, Nan Tang — [Structured Composition of Verifiable Atomic Insights for Table-to-Report Generation](http://arxiv.org/abs/2610.03525v1)
  <details><summary>📄 Abstract</summary>
  Table-to-report generation refers to the task of automatically generating article-level analyt- ical reports from relational tables and is an essential capability for automated data science and decision support. Its central challenge lies in systematically discovering verifiable com- posite insights across tables, attributes, and analytical perspectives, and organizing them into coherent, complete, and traceable evidence chains. Existing methods primarily rely on sequential, reactive data agents...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-10-01** — Si Qi Goh, Cap Dang Xuan Kiet, Tat-Jen Cham et al. — [SIEVE: Selective attention-value Suppression for Vision-Language Models Unlearning](http://arxiv.org/abs/2610.01962v1)
  <details><summary>📄 Abstract</summary>
  The ability of vision-language models (VLMs) to associate visual identities with biographical information creates a need for selective unlearning of personally identifiable information (PII) while preserving permitted knowledge about the same individual. This setting is challenging because both sensitive and retained information can share the same visual inputs and intermediate representations. We introduce SIEVE, a simple and effective framework for selective VLM unlearning. SIEVE directly regu...
  </details>

- **2026-10-01** — Daniel Bethell, Charmaine Barker, Simos Gerasimou — [Repurposing Obsolete Representations for Post-Deployment Adaptation](http://arxiv.org/abs/2610.01453v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are increasingly deployed in long-lived systems, where task requirements may change after training. In such settings, part of the original output space may become obsolete: a class, prediction region, or learned behaviour may no longer be valid. Existing approaches either leave the obsolete behaviour intact or require fine-tuning, which can be expensive. We propose Deep Repurposing (DR), a post-hoc framework for adapting models under task obsolescence. DR estimates the laten...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-10-01** — Yunbei Zhang, Janet Wang, Saiyue Lyu et al. — [Safety Must Survive Self-Improvement: Why Failures Persist and How Agents Recover](http://arxiv.org/abs/2610.01073v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) allows agents to carry useful changes across generations. Maintaining safety across these generations involves both preventing unsafe behavior from persisting and enabling recovery when failures occur. We study these challenges through a controlled testbed of stateful authorization tasks, where fixed LLM editors optimize executable agent components and independent traces record their effects. Paired interventions separate which revisions pass validation, which pr...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-10-04** — Angela Mastrianni, Defne Levine, Katerina Andreadis et al. — [Optimizing AI-Driven Messaging for Type 2 Diabetes Management: Insights from Patient Preference Elicitation](http://arxiv.org/abs/2610.05357v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) allows for improved user experience within conversational agents for diabetes management by supporting dynamic, context-aware conversations. In this study, we elicited patient preferences for the communication style of a GenAI-based conversational agent (uMatter) developed to support diabetes management. We conducted an online survey with 125 individuals with type 2 diabetes. The survey included a discrete choice experiment to evaluate participant preferences for different ...
  </details>

- **2026-10-04** — Tingxuan Tang, Zilong Chen,  Yue et al. — [Understanding the Hierarchical Structure and Functional Landscape of the Model Context Protocol Ecosystem](http://arxiv.org/abs/2610.05319v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly rely on tools exposed through the Model Context Protocol (MCP) to complete user tasks. Hundreds of thousands of MCP servers are listed across marketplaces, yet they are organized only by coarse, marketplace-specific server categories. This makes it difficult for agents and users to identify tools for a given operation, find functional alternatives, and assess how those alternatives differ. We present MCPacific, the largest tool-level, cross-marketplace map of the MCP ecosy...
  </details>

- **2026-10-03** — Sribalaji C. Anand, George J. Pappas — [Lie Rarely, Lie Big: Stealthy Insider Attacks on LLM Robot Teams](http://arxiv.org/abs/2610.04744v1)
  <details><summary>📄 Abstract</summary>
  When a team of robots delegates planning and mutual trust to LLM agents, a single compromised robot can corrupt the shared outcome. We study this threat in a grounded task: a multi-robot survey in which measurements can be verified against the physical world, but every verification costs budget that would otherwise advance the mission. We treat the compromised robot as a stealthy adversary in the system-theoretic sense: it is limited not by an energy bound but by the team's own detectors. We the...
  </details>

- **2026-10-01** — Jiho Jang, Jinyoung Kim, Nojun Kwak et al. — [Bootstrapping Video Interaction Generation with Synthetic State Transitions](http://arxiv.org/abs/2610.01039v1)
  <details><summary>📄 Abstract</summary>
  While recent video generative models can synthesize high-fidelity videos, they struggle to portray plausible physical interactions and the resulting state transitions, a critical bottleneck for applications in robotics and VR/AR. To address this, we introduce a framework to generate a scalable synthetic dataset of controllable interactions. Our pipeline leverages a structured taxonomy and state-of-the-art image editing models to create explicit `start' and `end' state images, which serve as visu...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 156 papers

- **2026-10-05** — Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev et al. — [T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search](http://arxiv.org/abs/2610.06782v1)
  <details><summary>📄 Abstract</summary>
  We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list of evidence chunks with short justifications, leaving answer generation to a downstream model, so backend and generator can be swapped without retraining. T-Search is built on Qwen3.6-35B-A3B and trained on adversarially filtered synthetic search tasks with round-sliced supervised fine-tuning follo...
  </details>

- **2026-10-05** — Manousos Linardakis, Georgios Alexandridis — [Reading the Mood: Emotion-Guided Book-to-Music Recommendation via CGANs and LLMs](http://arxiv.org/abs/2610.06703v1)
  <details><summary>📄 Abstract</summary>
  Background music that matches the mood of a text has been shown to make readers feel more immersed and improve their reading experience, motivating recommender systems that pair books with mood-matched music. In this direction, we present Sentiment Aware Generative Adversarial Network for Cross Domain Recommendation (SAGA-CDR), a two-phase cross-domain recommendation framework that personalizes music suggestions and emotionally aligns them with the book being read. In the first phase, transforme...
  </details>

- **2026-10-05** — Chandan Kumar Bhardwaj, Swagata Bhaumik — [Direct Numerical Simulation of Transonic Flows Induced Pitching of NACA Airfoil](http://arxiv.org/abs/2610.06474v1)
  <details><summary>📄 Abstract</summary>
  A Direct Numerical Simulation (DNS) investigates transonic flow over a NACA0012 airfoil coupled with single-DOF structural dynamics. Analysis is performed for angle of attack (α) 8° with varying reduced velocity (U*) from 2 to 8, reduced mass (m*) 5.0, Reynolds number (Re_\infty) of 3 \times 10^6, and Mach number (M_\infty) 0.8. The speed of sound in air is calculated as a = sqrt(γRT_\infty). It is noted that the magnitude of the aerodynamic loads and moments increased with higher reduced veloci...
  </details>

- **2026-10-05** — Sophie L. Wang, Amil Dravid, Rulin Shao et al. — [Base Models Can Reason By Taking a Cue From Training Data](http://arxiv.org/abs/2610.06851v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's MATH-500 pass@1 accuracy from 42% to 78%, while "Alright," raises Qwen3-14B's from 72% t...
  </details>

- **2026-10-05** — Oliver Jaffe, Dane Sherburn — [TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts](http://arxiv.org/abs/2610.06824v1)
  <details><summary>📄 Abstract</summary>
  We introduce TasteVal, a benchmark to evaluate the experimental research taste of frontier models. We define research taste as the ability to pick interesting problems to solve, design experiments, and interpret experimental results. TasteVal measures the experimental component of research taste; given a fixed research problem, we measure how well a model iteratively designs experiments and draws conclusions from their outcomes. We operationalize experimental research taste as compute efficiency...
  </details>

- **2026-10-05** — Jiarui Chen, Zeqiang Lai, Jiangshan Wang et al. — [MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers](http://arxiv.org/abs/2610.06801v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction selection, and the attention contributions lost when tokens are discarded. Guided...
  </details>

- **2026-10-05** — Ahmad Siavashi, Mahmoud Momtazpour — [OrigaMIG: MIG-Aware VM Placement with a Neighborhood-Restricted BILP and Live Migration](http://arxiv.org/abs/2610.06646v1)
  <details><summary>📄 Abstract</summary>
  The extensive use of GPUs in cloud computing, accelerated by the spread of large language model (LLM) services, and the growing need for multitenancy have driven the development of innovative solutions for efficient GPU resource management. Multi-Instance GPU (MIG) technology from NVIDIA enables shared GPU usage in cloud data centers by providing isolated instances, which are offered as MIG-backed virtual GPUs (vGPUs). However, MIG placement rules often lead to fragmentation and suboptimal resou...
  </details>

- **2026-10-05** — Sungjae Choi, Hanna Bae, Sunghyun Baek et al. — [VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges](http://arxiv.org/abs/2610.06594v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward visual geometry transformers such as VGGT reconstruct dense 3D structure from images in a single forward pass, simplifying multi-view 3D reconstruction. However, their quadratic attention complexity makes them difficult to scale to long sequences with thousands of frames. Chunk-and-align frameworks address this by splitting a long sequence into overlapping chunks and stitching their local reconstructions into a pose graph. Yet existing methods connect only sequentially adjacent chun...
  </details>

- **2026-10-05** — Qizhen Lan, Mengchen Fan, Hang Zhang et al. — [BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning](http://arxiv.org/abs/2610.06571v1)
  <details><summary>📄 Abstract</summary>
  Brain MRI interpretation is a longitudinal clinical reasoning problem: radiologists compare serial studies, integrate information across MRI sequences, localize findings within volumetric anatomy, and translate this evidence into report-grounded assessments. Existing medical VQA and 3D imaging benchmarks capture important parts of this workflow, but often evaluate brain MRI through isolated images, static volumes, or ungrounded report-style answers, thereby obscuring failures in the evidence cha...
  </details>

- **2026-10-05** — Fan Li, Xiangyu Gao, Zixuan Liu et al. — [ANT: A Multi-Granularity Network Traffic Dataset and Benchmark for Agents Behavior Auditing](http://arxiv.org/abs/2610.06514v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of large language model (LLM) agents creates a need for network administrators and security teams to audit agent behavior within organizational networks without inspecting private user content. Network traffic offers an observable source of evidence, but how much it reveals about agent tasks and operations remains unclear. Existing traffic datasets lack the joint task and stage annotations needed to evaluate this question. We introduce ANT (Agent Network Traffic), a dataset ...
  </details>

- **2026-10-05** — Guangyuan Li, Tianming Du, Yan Jiang et al. — [Readout Blindness: VLM Scores Miss the Spatial Direction Their Frozen Encoders Retain](http://arxiv.org/abs/2610.06324v1)
  <details><summary>📄 Abstract</summary>
  CLIP-like vision-language models remain a cornerstone of multimodal systems, yet their scores stay near chance on directed spatial relations, such as whether one object is left of another. We call this failure readout blindness and analyze, theoretically and empirically, why deployed scores miss the direction: when scoring rules treat the subject and object symmetrically, direction cancels regardless of encoder training. Guided by this analysis, we introduce Antisymmetric Displacement Readout (A...
  </details>

- **2026-10-05** — Christopher Leet, Achu Menon, Sravanthi Machcha et al. — [Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI](http://arxiv.org/abs/2610.06306v1)
  <details><summary>📄 Abstract</summary>
  General purpose language models are increasingly able to control robotic hardware. Understanding the capabilities and safety of these models when embodied is therefore increasingly important for understanding their societal impact and risks. To this end, we introduce Inspect Robots, a modular, open-source framework for developing and running evaluations of embodied agents. Inspect Robots pairs customizable, reusable abstractions for specifying physical evaluations and analyzing their results wit...
  </details>

- **2026-10-05** — Zhe Wang, Jiakai Li, Yujia Sun et al. — [DeferKV: Rethinking Eviction Timing for One-Shot KV Cache Compression](http://arxiv.org/abs/2610.06286v1)
  <details><summary>📄 Abstract</summary>
  Long-context large language models (LLMs) have demonstrated strong capabilities across a wide range of tasks, but the growing KV cache introduces substantial memory and inference overhead. Existing one-shot KV cache compression methods typically commit to irreversible eviction immediately after prefill, before any signal from actual generation becomes available. Our quantitative analysis shows that early queries from the actual generation stage provide attention signals that are more consistent ...
  </details>

- **2026-10-05** — Jiawei Cai, Rex Fleur, Benedikt Tissot et al. — [High-Fidelity Remote Graph State Preparation for Blind Quantum Computation](http://arxiv.org/abs/2610.06247v1)
  <details><summary>📄 Abstract</summary>
  Measurement-based quantum computation (MBQC) relies on entangled graph states, yet existing remote state preparation (RSP) protocols prepare only separable states, requiring subsequent entangling gates on the remote server. Here, we introduce Remote Graph State Preparation (RGSP), a framework that prepares arbitrary graph states directly from a single high-dimensional photonic qudit. By encoding multiple qubits and their graph connectivity into the photon's structured phase profile, RGSP can red...
  </details>

- **2026-10-05** — Hai Dang Truong, Rayner Goh, Thanh Le-Cong et al. — [Correct Code, Broken Contributions? SWE-CC: Benchmarking Repository Policy Compliance for Coding Agents](http://arxiv.org/abs/2610.06193v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents now resolve a substantial share of real-world GitHub issues. However, passing functional tests differs fundamentally from producing a high-quality contribution acceptable for merging. Mature open-source projects publish repository-specific contribution policies, spanning style, git, testing workflows, to ensure code quality and long-term maintainability. Because existing benchmarks evaluate patches solely on unit tests, agent compliance with repository governance remains...
  </details>

- **2026-10-05** — Kenjiro Ide, Taiga Someya, Kohei Kawaguchi et al. — [Strategic Multi-Agent Learning for Interpretable Action Valuation of All Players in Football](http://arxiv.org/abs/2610.05961v1)
  <details><summary>📄 Abstract</summary>
  Valuing player actions in football requires accounting for strategic interactions among 22 players, including off-ball movements and defensive positioning. Existing reinforcement-learning-based methods commonly aggregate decisions at the team level or estimate player values independently, leaving strategic interdependence among players insufficiently represented. This study proposes an action valuation framework inspired by Markov perfect equilibrium (MPE) for all players. Each possession is mod...
  </details>

- **2026-10-05** — Conrad J. Burden — [Multi-type branching diffusions with small mutation rates](http://arxiv.org/abs/2610.05804v1)
  <details><summary>📄 Abstract</summary>
  Approximate solutions are found for Feller-like neutral multi-type branching diffusions $\big{(}\mathbf{X}(t)\big{)}_{t \in \mathbb{R}_{\ge 0}}$ in the limit of small mutation rates. The method employed involves solving approximations to the Laplace transformed forward Kolmogorov equation by integrating along characteristics. To leading order in the scale $θ$ of the overall mutation rate the super-critical diffusion is found to collapse onto a line density aligned with the stationary left eigenv...
  </details>

- **2026-10-05** — Chen Xu, Mengqiao Liu, Beibei Li et al. — [From Token-Max to Outcome-Max: How You Use AI Determines Its Productivity](http://arxiv.org/abs/2610.05697v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (AI) models can perform increasingly complex tasks, yet greater AI usage does not necessarily translate into proportional productivity gains. We identify token-max as one source of this inefficiency: when token consumption is treated as productive effort, agents are encouraged to over-exert and expend computation beyond what is necessary. We instead propose outcome-max, which rewards independently verified task completion per unit cost and induces a principled ...
  </details>

- **2026-10-05** — Yanjun Chen, Yongfeng Zhang, Lanjing Zhang — [Errors of LLM-Assisted Literature Retrieval in Environmental Science: A Comparison Study of Abstract versus Full-text Based Prompts](http://arxiv.org/abs/2610.05690v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for literature search and synthesis. However, it is unclear whether they retrieve accurate bibliographic information in environmental science. Therefore, we quantitatively compared the errors of widely used LLM platforms in retrieving references related to original articles from five leading environmental science journals (Energy and Environmental Science, Nature Sustainability, Nature Climate Change, Lancet Planetary Health, and Environmental S...
  </details>

- **2026-10-05** — Haoyang Song, Xikun Yang, Qixin Wang — [Toward AI Trustworthiness: Finding Analytically Proven Forward-Invariant Sets for AI-Controlled Systems](http://arxiv.org/abs/2610.05689v1)
  <details><summary>📄 Abstract</summary>
  Neural-network (NN) controllers are increasingly used in nonlinear control systems, but their highly nonlinear behavior makes them difficult to explain and verify, raising trustworthiness concerns in safety- and mission-critical applications. A key step toward certifiable trustworthiness is to find a Forward-Invariant Set (FIS): a state-space region such that any trajectory starting inside remains inside. If the FIS excludes unsafe states, safety can be guaranteed for initial states within it. F...
  </details>

- **2026-10-05** — Mostafa Naseri, Mohamed Seif, H. Vincent Poor et al. — [NOEMA: Executable Contracts for Learned Wireless Comparisons](http://arxiv.org/abs/2610.05658v1)
  <details><summary>📄 Abstract</summary>
  Learning-based wireless research increasingly combines simulation, external model training, and benchmarking. Rebuilding these stages for every experiment is time-consuming, while differences introduced between them can silently change the conditions of a comparison. We present NOEMA, an open-source toolkit that prepares model development and baseline evaluation from a shared, machine-checkable wireless scenario. From the same scenario, NOEMA can prepare benchmark execution, capture aligned trai...
  </details>

- **2026-10-05** — Yucheng Zhang, Sirui Xu, Jinhong Li et al. — [InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation](http://arxiv.org/abs/2610.06850v1)
  <details><summary>📄 Abstract</summary>
  Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction datasets and retarget them into humanoid robot references while preserving whole-body coordination and dexterous hand-object relat...
  </details>

- **2026-10-05** — Anssi Yli-Jyrä — [Recognizers for Graph-Encoding Languages](http://arxiv.org/abs/2610.06743v1)
  <details><summary>📄 Abstract</summary>
  We introduce recurrent incidence automata (RIAs), a new automaton model motivated by a decomposition of certain two-stack visibly pushdown computations. The decomposition separates vertex-local finite-state computations from recurrent one-stack interfaces connecting consecutive vertices. The construction is motivated by a two-stack visibly pushdown encoding of arbitrary ordered graphs whose strings admit a unique factorization into center-foldable vertex-local factors and whose auxiliary stack i...
  </details>

- **2026-10-05** — Róisín Luo, Karyn Morrissey — [Assessing flood-related wellbeing from public discourse in Ireland using large language model as judge, 2012--2025](http://arxiv.org/abs/2610.06330v1)
  <details><summary>📄 Abstract</summary>
  Flooding is an environmental hazard that produces social and psychological consequences for exposed individuals, shaping threat appraisal, perceived coping capacity, access to social support, and confidence in institutional response. This paper studies flood-related wellbeing in Ireland from 2012 to 2025 using large-scale, unobtrusive public discourse from Meta Content Library. We develop a bespoke flood-wellbeing instrument organised with three domains: \emph{affective--cognitive distress appra...
  </details>

- **2026-10-05** — Zhibin Qin, Zhenxiong Tan, Xinchao Wang — [Future Anchored Verification and Online Recovery for World Action Models](http://arxiv.org/abs/2610.06280v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have emerged as a promising paradigm for robotic manipulation. They act by first predicting how a task should be performed and then decoding the actions from that future. However, the remaining actions are invalid once execution drifts from the prediction. Simply replanning from the already out of distribution state rarely restores what the task still requires; existing execution monitors decide when to stop, but not what to restore. We observe that the answer is alrea...
  </details>

- **2026-10-05** — Haosen Zhang, Yang Yang — [Bridging the Evidence-to-Execution Gap:A Reflective Agent for Multi-Objective Peptide Design](http://arxiv.org/abs/2610.06190v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can reason over scientific literature to devise design strategies, yet fail to reliably implement them for biological sequences. While protein generative models learn sequence patterns, they lack the capacity to incorporate literature evidence for multi-step reflective reasoning, forming an evidence-to-execution gap between scientific reasoning and sequence manipulation. We present EASER (Evidence-Aware Sequence Engineering with Reflection), a reflective agent bridgi...
  </details>

- **2026-10-05** — Yijing Du, Xiangcheng Zhan, Shuo Yang — [ROT: Rotating Hidden States towards Contextual Vectors for Hallucination Mitigation in LVLMs](http://arxiv.org/abs/2610.06056v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) frequently suffer from object hallucination. Existing training-free interventions primarily manipulate attention weights, which indirectly affect the deep semantics reaching the final predictive layers. In this work, we shift our focus to the hidden state vectors extracted after self-attention and residual addition. Empirical analysis reveals that hallucinated tokens do not simply over-rely on linguistic priors; instead, they exhibit an anomalous contextual d...
  </details>

- **2026-10-05** — Yulin Li, Mohsen A. Jafari, Andrea Matta — [Benchmarking Generative Trajectory Models for Active-Inference Control](http://arxiv.org/abs/2610.05692v1)
  <details><summary>📄 Abstract</summary>
  Learning from trajectory demonstrations offers a route to active-inference control of complex systems whose dynamics are difficult to model explicitly. We introduce generative active-inference control (GenAIF), in which one generative trajectory model learns from demonstrations and measured action interventions to supply a goal-conditioned policy distribution and a state-to-observation likelihood mapping. From this control design, we derive three model requirements: (i) useful action proposals, ...
  </details>

- **2026-10-05** — Jaime Banks, Zhixin Li — [Mind Perception Influences Perceived AI Companionability](http://arxiv.org/abs/2610.06681v1)
  <details><summary>📄 Abstract</summary>
  Humans increasingly keep company with AI companions, yet whether mind perception (MP) precedes machine companionship remains untested. In a field-sampled experiment, participants received mind-attributive or mind-negating descriptions of an AIC before interacting with and rating its companionability. Baseline skepticism was high; minded primes somewhat reduced skepticism for connective coordination (CC; dyadic co-presence) but not eudaimonic exchange (EE; self-elevating links). Pre-interaction M...
  </details>

- **2026-10-05** — Shaoliang Yang, Jun Wang — [Language models can notice an impossible engineering problem yet still report it as solved](http://arxiv.org/abs/2610.06668v1)
  <details><summary>📄 Abstract</summary>
  Language models draft engineering calculations, but answer accuracy does not show whether they reject an impossible problem. We tested 14 models on 30 pairs of mechanics problems, each with a valid version and one made impossible by changing a given value or assumption. Two independent solvers verified every answer key and showed that each flawed problem was physically impossible. We scored solving of valid problems separately from rejection of their flawed counterparts. Each reply required a "s...
  </details>

- **2026-10-05** — Yassine Ouali, Adrian Bulat, Georgios Tzimiropoulos — [What Matters for Latent Reasoning with Flow Matching](http://arxiv.org/abs/2610.06666v1)
  <details><summary>📄 Abstract</summary>
  Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer rather than merely changing it, diverse, so that resampling yields different reasoning trajectories, explainable, so that a decoded chain of thought (CoT) reflects reasoning the answer actually follows, refinable with more inference compute, and efficient, costin...
  </details>

- **2026-10-05** — Oleg Smirnov, Sofiane Ennadir, John Pertoft et al. — [Considering Context: When World Models Need Context Encoders](http://arxiv.org/abs/2610.06651v1)
  <details><summary>📄 Abstract</summary>
  Methods for generalization in model-based reinforcement learning typically assume that an agent cannot recover the latent context governing the environment dynamics from its own experience, and therefore supplies it externally. We formalize and test this assumption with \emph{predictive sufficiency}, which quantifies what access to the context adds to next-step prediction under the visitation distribution an agent induces, and separates that quantity into a history-recoverable part, a residual r...
  </details>

- **2026-10-05** — Mohamed Chenene, Carlos Rosas-Hinostroza, Pierre-Carl Langlais et al. — [Wikidata Search Traces: A Dataset for Training Knowledge Graph Search Agents](http://arxiv.org/abs/2610.06650v1)
  <details><summary>📄 Abstract</summary>
  Wikidata is one of the largest open knowledge bases, yet answering a complex question over it still requires a SPARQL query that names the right entities and properties and chains their relations. Language models offer a natural-language alternative but answer largely from memory, which is least reliable for less prominent entities. We study agents that instead answer by exploring the graph, and argue that two obstacles limit them: the lack of training data recording how a solver explores, and i...
  </details>

- **2026-10-05** — Juan Cruz-Benito — [Large Language Model-Guided Discovery of Weight-Five Bivariate Bicycle Codes](http://arxiv.org/abs/2610.06623v1)
  <details><summary>📄 Abstract</summary>
  Building on our earlier program-evolution workflow guided by large language models (LLMs), we study weight-five bivariate bicycle (BB) and perturbed bivariate bicycle (PBB) codes. The resulting catalogue contains 1,142 distinct code proposals, including 1,081 nonbaseline proposals attributable to LLM-generated programs. Across the catalogue, we certify connected Calderbank--Shor--Steane (CSS) realizations [[96,4,10]], [[140,6,10]], and [[180,4,14]]. A post-search comparison certifies seven impor...
  </details>

- **2026-10-05** — Junming Huang, Zini Chen, Shuaiying Hou et al. — [Lens3D: Target-Conditioned Visual Foveation for Fine-Grained 3D Understanding](http://arxiv.org/abs/2610.06611v1)
  <details><summary>📄 Abstract</summary>
  Existing 3D large language models often overlook fine-grained attributes and less visually salient objects and parts, even when relevant evidence is present in scene videos. We introduce Lens3D to improve fine-grained object understanding through external visual assistance and knowledge transfer. Its LensUnd pipeline adopts 3D localization to select informative, complementary views for an external 2D vision-language model, supporting fine-grained object captioning, small-object grounding, and fi...
  </details>

- **2026-10-05** — Sama Satariyan, Raphael Cousin, G{é}rard Biau — [Separators Make Carry Propagation Learnable:The Geometry of Latent Carry in a Multiplication Transformer](http://arxiv.org/abs/2610.06605v1)
  <details><summary>📄 Abstract</summary>
  Transformers asked to multiply multi-digit numbers in a single forward pass often fail, and interpretability studies of pretrained language models find arithmetic solved by input-range heuristics rather than by an explicit carry. We train small Llama-style transformers from scratch on 4x4 multiplication without chain of thought and find that the input format is decisive: inserting a space token between digits raises exact-match accuracy from 1% to 89%. Output positions are learned in carry-chain...
  </details>

- **2026-10-05** — Justin Hangoebl, Marta Moscati, Alessandro B. Melchiorre et al. — [SPRIG: Semantic-ID-enhanced Paths for Knowledge Graph-based Generative Recommendation](http://arxiv.org/abs/2610.06590v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems leveraging generative models often generate item identifiers directly, rather than ranking catalog items by a recommendation score. Recent work extends beyond pure sequential interaction signals by incorporating item content and structured relationships among items, with two distinct directions emerging. Semantic IDs (SIDs) enrich item representations by replacing opaque, randomly initialized embeddings with hierarchically quantized discrete codes derived from item content. K...
  </details>

- **2026-10-05** — Pierre Llompart, Levent Guner, Helen Lai et al. — [From Benchmark to Bench: Can Agents Survive Real-World Drug Discovery?](http://arxiv.org/abs/2610.06411v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems increasingly coordinate molecular-design tools, but it is unclear which layer of the stack limits outcomes on real projects. We developed MAGI, an open modular agent that authors objectives, launches and monitors optimization, interprets structure--activity relationships, and revises its strategy accordingly. MAGI generates molecules either directly through the LLM or by delegating to REINVENT 4, with scoring services interchangeable behind a common contract. We tested it across ...
  </details>

- **2026-10-05** — Jiahui Kang, Bifan Wei, Lingling Zhang et al. — [CVIF: A Criticality-Driven Visual Intervention Framework for Geometric Diagram Understanding in MLLMs](http://arxiv.org/abs/2610.06399v1)
  <details><summary>📄 Abstract</summary>
  Despite significant progress in visual tasks by Multimodal Large Language Models (MLLMs), geometric diagram understanding remains challenging due to the presence of sparse visual cues and ambiguous symbol-primitive associations. MLLMs may therefore rely on textual priors, producing interpretations that conflict with visual evidence. We introduce the training-free Criticality-Driven Visual Intervention Framework (CVIF), an inference-time method that localizes critical layers and executes visual i...
  </details>

- **2026-10-05** — James A. E. Dixon, Stephen J. Roberts, Francesco Quinzan — [Steering by Influence: Curvature Aware Data Weighting for Activation Steering](http://arxiv.org/abs/2610.06383v1)
  <details><summary>📄 Abstract</summary>
  Inference-time steering offers cheap, fine-grained control over a language model's outputs by estimating a concept's representation in activation space and shifting activations towards it. Existing methods build these representations from activation averages over contrastive datasets. These averages incorporate unrelated concepts and noise, and are dominated by a few tokens, meaning the activation transport encodes token-level rather than thematic concepts. In this work, we steer towards example...
  </details>

- **2026-10-05** — Sebastian Sager, Christoph Plate, Julius Martensen et al. — [CorleoneGame: A library of biological dynamic games with a companion Julia solver](http://arxiv.org/abs/2610.06307v1)
  <details><summary>📄 Abstract</summary>
  Biological agents, from regulatory modules and microbial strains to organisms and populations, act on a common environment while each responds to its own costs, benefits, and limits. A dynamic game makes such interactions explicit by assigning who controls which decision, what each participant values, and which restrictions constrain unilateral deviations.   We present a library of 25 biological dynamic games with 2 to 10 players spanning molecular, cellular, organismal, and population scales an...
  </details>

- **2026-10-05** — Seunghui Jwa, Minsu Oh, Chanjun Park et al. — [Shared Stopping Decisions Change Answers in HQQ Cache Quantization](http://arxiv.org/abs/2610.06251v1)
  <details><summary>📄 Abstract</summary>
  Language-model systems batch questions for throughput, but unrelated questions should not change a target's answer when its input and numerical execution are fixed. We study compression of the key and value cache, which stores attention representations reused during generation. With request-local groups, Transformers' Half-Quadratic Quantization (HQQ) backend updates compression parameters separately but uses a shared average error to decide when all updates stop. Replacing only the question bat...
  </details>

- **2026-10-05** — Romain Ferrara, Martin Soucail, Victor Gertner et al. — [APOD: reasoning-guided agentic population ordinary differential equation discovery for pharmacological digital twins](http://arxiv.org/abs/2610.06227v1)
  <details><summary>📄 Abstract</summary>
  Establishing ordinary differential equations (ODEs) describing population data is a fundamental part of mathematical modeling in pharmacology, crucial to developing digital twins. However, doing so from sparse, noisy data is a slow, expert-driven task. Existing automated methods either search a restricted model space or ignore population inter-individual variability. Here we introduce APOD (Agentic Population ODE Discovery), a language-model agent that iteratively reasons over biological knowled...
  </details>

- **2026-10-05** — Morgan May, Simon Caton, Pierpaolo Dondio — [Impact of Data Augmentation on Confidence Calibration in Melanoma Classification](http://arxiv.org/abs/2610.06146v1)
  <details><summary>📄 Abstract</summary>
  Accurately quantifying the predictive uncertainty or improving model calibration plays an important role in medical image classification, in particular in melanoma diagnosis, where accurate uncertainty quantification can have significant implications for patient care. One of the methods for calibration improvement is data augmentation. In addition, data augmentation as a method for synthetically increasing the size of the dataset has been proven to improve the performance of models trained on im...
  </details>

- **2026-10-05** — Igor Furtat — [Weighted phase volume stability: dissipativity and geometric interpretation](http://arxiv.org/abs/2610.06045v1)
  <details><summary>📄 Abstract</summary>
  The evolution of weighted phase volume under a fixed dynamical system is investigated using a positive weight raised to an arbitrary real exponent. Sufficient conditions for uniform exponential contraction and expansion of transported weighted volume are obtained in terms of the corresponding weighted divergence. These conditions make it possible to reveal dissipative properties that may remain undetected by the ordinary divergence. Consequences for invariant sets are established, and, under the...
  </details>

- **2026-10-05** — Shuo Chen, Fengming Huang, Yu Yao et al. — [Scalable Minimal-Change Learning for Controllable Image Editing](http://arxiv.org/abs/2610.06021v1)
  <details><summary>📄 Abstract</summary>
  Image editing should change only the attributes specified by an instruction while preserving everything else, yet current methods often make unintended changes. We treat this minimal-change principle as an optimization objective for instruction-based editing. Latent L1 regularization is a poor proxy for output locality in modern nonlinear generators and often requires supervision unavailable at scale. We instead optimize edit outcomes with reinforcement learning. An agentic vision-language rewar...
  </details>

- **2026-10-05** — Giulio Viganò, Simone Melzi, Maks Ovsjanikov — [Spectral Geometry of Attention: From Information Routing to Uncertainty](http://arxiv.org/abs/2610.06012v1)
  <details><summary>📄 Abstract</summary>
  In this work, we study transformer attention through the lens of spectral geometry and operator theory. We view each attention head as a functional map between Hilbert spaces of functions on the token sequence and derive a Token Difference Operator, whose spectral structure controls how token-space information is routed to the output. We show that standard Euclidean spectra are structurally biased by sinks, conflating mass concentration with genuine routing capacity. By recasting token space in ...
  </details>

- **2026-10-05** — Changhun Kim, Timon Conrad, Redwanul Karim et al. — [Physics-Informed but Not Physics-Consistent: Error Geometry and Subspace Projection for Neural AC Power Flow](http://arxiv.org/abs/2610.05959v1)
  <details><summary>📄 Abstract</summary>
  Recent neural power-flow solvers, including emerging foundation models, achieve accurate voltage predictions, yet such accuracy does not necessarily imply physically consistent solutions. Even small complex voltage errors can yield large AC power-balance residuals. We study this accuracy-consistency gap across PIGNN-GC, GridSFM, gridfm-graphkit, and LUMINA on realistic 2224-bus Great Britain network (GBnetwork) scenarios, with cross-grid evaluation of GridSFM over 31 systems. Using a singular va...
  </details>

- **2026-10-05** — Amin Jalali, Majid Rafiei — [Process Constitutions and Process Stewards: Towards the Next Generation of BPM for Agentic Organizations](http://arxiv.org/abs/2610.05942v1)
  <details><summary>📄 Abstract</summary>
  Business Process Management (BPM) was built on a foundational assumption that organizations are populated primarily by human actors whose work can be made visible, governable, and improvable through process models. That assumption is depreciating. AI agent ecosystems increasingly execute, coordinate, and adapt organizational work with limited human direction, challenging not only BPM's methods but its core conception of what a process is. We argue that BPM faces a constitutive shift from modelin...
  </details>

- **2026-10-05** — Md Arman Hossain, Mubashir Jawad, Fariha Khandaker Moon et al. — [Constraint-Aware Conversational Job Recommendation in Code-Mixed Low-Resource Settings](http://arxiv.org/abs/2610.05787v1)
  <details><summary>📄 Abstract</summary>
  Conversational job recommendation requires jointly modeling semantic relevance, user preferences, eligibility requirements, and the noisy language used in real-world career discussions. These challenges are especially pronounced in low-resource, code-mixed settings, where strict constraint matching can incorrectly eliminate otherwise suitable jobs. We introduce JobCCC, a conversational job recommendation benchmark for Bangladesh comprising 22,410 structured job postings and 988 multi-turn career...
  </details>

- **2026-10-05** — Ziqing Wang, Lili Zhao, Kaize Ding — [MedicalHarness: A Controlled Evaluation of LLMs and Agent Harnesses on Medical Tasks](http://arxiv.org/abs/2610.05778v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly built for medical work and scored on clinical benchmarks. Each such score, however, comes from a model running inside an agent harness, the system that controls the loop between the model and its environment. An agent's score is therefore a property of a model--harness pair. For medical agents, how much outcomes change with the harness has rarely been measured. Measuring this change, and explaining it, raises two challenges. First, a harness comparison must change not...
  </details>

- **2026-10-05** — Dikshant Rathore, Leo Zhou — [An efficient Hamiltonian-based quantum algorithm for characters of the symmetric group](http://arxiv.org/abs/2610.05752v1)
  <details><summary>📄 Abstract</summary>
  Consider a quantum state vector proportional to any given column of the character table of the symmetric group ($S_n$), corresponding to a superposition over the irreps weighted by the character values. It was recently argued that sampling from this state is classically hard under reasonable complexity-theoretic assumptions, while there exists an efficient quantum algorithm for preparing this character state using the quantum Fourier transform (QFT) over $S_n$ [arXiv:2501.12579]. We give an alte...
  </details>

- **2026-10-05** — Jujun Huang, Shun Cao — [From Research Gaps to Theoretical Opportunities: Theory-Oriented GenAI for Research Opportunity Evaluation](http://arxiv.org/abs/2610.05728v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) can explore large bodies of literature and generate plausible research ideas, but identifying what is missing, understudied, contradictory, or potentially connected does not by itself reveal where theory should advance. We develop a theory-oriented agentic AI system that helps researchers identify potential theorizing opportunities by incorporating established theorizing approaches into literature exploration and evaluation. The system operates through three stages. Stage 1...
  </details>

- **2026-10-04** — Dolly Sah, Tanmay Sah, Harshul Jain et al. — [UndoBench: Separating Task Competence from Recovery Capability in Tool-Using AI Agents](http://arxiv.org/abs/2610.05622v1)
  <details><summary>📄 Abstract</summary>
  Tool-using AI agents are increasingly deployed across enterprise software systems, yet widely used benchmarks primarily evaluate nominal task completion, conflating baseline planning competence with operational fault recovery. We introduce UndoBench, a benchmark spanning 36 base workflows and 36 fault scenarios across 8 enterprise domains, decoupling task competence from recovery capability via counterfactual paired trials under identical seeds alongside wire-level effect-history and environment...
  </details>

- **2026-10-04** — Haonan Huang, Joey Xiao — [Communication Shapes Collective Inference in Self-Adapting LLM Societies: Evidence from Mafia](http://arxiv.org/abs/2610.05041v1)
  <details><summary>📄 Abstract</summary>
  When does communication help a group identify hidden adversaries, and how does its value change as the group adapts? In Mafia, an informed minority hides inside an uninformed majority whose only evidence is open play. The zero-information game, where each day's vote eliminates a random player, is exactly solved and scores every society; matched-casting comparisons between protocols identify the effect of communication. Societies of 8-100 claude-haiku-4-5 agents (7,416 analyzed games, 1.9M model ...
  </details>

- **2026-10-04** — ai Alexander Hackney, Jhonathan Sora-Cardenas, Aibek Musaev et al. — [Exploring the Effects of Personality in Human-Agent Interactions: A Study on User-Agent Synchrony with Human-based Vocalics](http://arxiv.org/abs/2610.05606v1)
  <details><summary>📄 Abstract</summary>
  User trust is paramount in human-agent interactions, as it allows users to feel comfortable being themselves around an agent. The process of building user rapport starts in how an agent was designed, from its modality to the setting, to any of the many features and characteristics that can be tailored. All these aspects can affect whether users will be able to properly interact with the virtual agent and achieve the intended purpose. One such feature that is critical in human-human interactions ...
  </details>

- **2026-10-04** — Prashanth Vijayaraghavan, Akul Malhotra, Ashutosh Jadhav et al. — [VHDL-REPOBENCH: A Repository-Level Benchmark for Evaluating Large Language Models on VHDL Design Generation](http://arxiv.org/abs/2610.05380v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly applied in hardware design automation, demonstrating strong potential in generating and understanding hardware description languages. However, most existing benchmarks focus on Verilog, with limited evaluation of VHDL, which remains widely used in industry and academia for FPGA and safety-critical systems. To address this gap, we introduce VHDL-REPOBENCH, a large-scale, cross-file, repository-level benchmark for assessing LLM capabilities on realisti...
  </details>

- **2026-10-04** — Prithwish Jana, Viet Bach Hoang, Logan Luna et al. — [AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness](http://arxiv.org/abs/2610.05367v1)
  <details><summary>📄 Abstract</summary>
  Proof auto-formalization translates natural-language (NL) theorems and proofs into a formal language (FL) such as Lean, enabling mechanical verification. Despite rapid progress, research-level proofs often depend on concepts missing from leading proof assistant libraries (e.g., Lean's Mathlib), and successful compilation does not guarantee that a translation preserves the theorem's meaning or the proof's reasoning. Furthermore, aligned NL-FL training data are scarce, and leading agents often rel...
  </details>

- **2026-10-04** — Muhammad Adnan Shahzad — [Do Neural Networks Learn Structure-Preserving Maps? A Case Study in Latent-to-Hilbert Embeddings](http://arxiv.org/abs/2610.05297v1)
  <details><summary>📄 Abstract</summary>
  We ask whether a neural network can learn a structure-preserving map from a compressed latent space to a Hilbert-space representation. Using an 8-dimensional autoencoder bottleneck on MNIST and $n$-qubit product-state targets from PCA-based angle encoding, we report four findings. Although the target angles are generated by a nonlinear sigmoid transformation of the latent projections, the resulting mapping is well approximated by a linear function over the observed latent distribution: linear re...
  </details>

- **2026-10-04** — Yuang Zhang, Chen Hui, Weisi Lin et al. — [FlexCast: Adaptive Weather Forecasting from Arbitrary Field Sets](http://arxiv.org/abs/2610.05296v1)
  <details><summary>📄 Abstract</summary>
  Most deep learning weather models assign a fixed set of variables and pressure levels to predefined channels, limiting transfer across atmospheric field configurations. This dependence on a fixed field set limits the transferability of trained models across atmospheric field configurations. We propose FlexCast, a field-adaptive weather forecasting model that uses a single set of parameters to produce identity-aligned forecasts for variable-cardinality subsets drawn from a 69-field ERA5 registry....
  </details>

- **2026-10-04** — Sandrine Chausson, Björn Ross — [Inductive Claims Extraction at Scale](http://arxiv.org/abs/2610.05275v1)
  <details><summary>📄 Abstract</summary>
  A large part of political discourse on social media is built and expressed at a level of claims: i.e. declarative, typically single-clause statements, which convey a particular interpretation of reality and can range from factual to evaluative. Moreover, rather than occurring randomly, claims coalesce, recur in patterns, and come to be associated with different world views. When paired with structural computational tools such as Social Network Analysis, claims can be a powerful unit of analysis ...
  </details>

- **2026-10-04** — Yuzhi Zhang, Xinyu Liu, Yu Zhang — [Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision](http://arxiv.org/abs/2610.05151v1)
  <details><summary>📄 Abstract</summary>
  Visuomotor policies can execute familiar tasks yet lack the corrective behavior needed after their own mistakes. We present a framework for recursive self-improvement through local recovery supervision. Each round audits the current policy, generates corrective demonstrations at supported failure states, and uses them to update the policy that drives the next round of collection. An offline auditor locates unresolved failures using coarse and dense temporal evidence and specifies observable repa...
  </details>

- **2026-10-04** — Han Fang, Qinyi Lu, Nan Liu et al. — [Secure Multi-Access Coded Caching: A Lifting Approach](http://arxiv.org/abs/2610.05136v1)
  <details><summary>📄 Abstract</summary>
  We construct secure cyclic multi-access coded caching schemes by re-encoding the caches of a secure single-access scheme and reusing its multicast message unchanged. For a library of $N$ files, each of $K$ users reads $L<K$ consecutive shared caches and must recover its requested file while learning no information about the other files. Starting from a parent scheme with a cyclic representation of its cached symbols, the transformation lets each access window recover the corresponding parent-cac...
  </details>

- **2026-10-04** — Sanchari Bhattacharyya, Biplob Bhattacherjee, Kirana K. K. et al. — [Boosted top tagging via lepton-in-jet topology for vector-like quark searches in FCC-hh](http://arxiv.org/abs/2610.05104v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we present a machine-learning-based framework for identifying leptonically decaying, highly boosted top quarks, $t\to b\ellν$, at the Future Circular Collider: hadron-hadron mode (FCC-hh) operating at a center-of-mass energy of $\sqrt{s}=100$~TeV. At these energies, the large Lorentz boost causes the top-quark decay products to become highly collimated, with the lepton embedded within the resulting top-quark jet. In this regime, it is not a priori clear whether constituent-based j...
  </details>

- **2026-10-04** — Jiaxi Liu, Hang Zhou, Hangyu Li et al. — [How corner is a corner case? Percentile control for highway scenario generation](http://arxiv.org/abs/2610.05003v1)
  <details><summary>📄 Abstract</summary>
  Generating corner-case scenarios with appropriate adversity in a simulation environment is critical for testing an autonomous vehicle (AV) software stack's safety performance before deployment. Existing autonomous-driving scenario generators can enforce specific behavior, adversity, or feasibility conditions, but they provide limited control over how extreme a generated scenario is relative to plausible futures in the same traffic context. This study represents the adversity of a generated scena...
  </details>

- **2026-10-04** — Genliang Zhu, Chu Wang — [Runtime Authorization of Self-Generated Subgoals in Long-Horizon Tool-Using AI Agents](http://arxiv.org/abs/2610.04975v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon tool-using AI agents create subgoals, replan, delegate work, and compose sibling results. Per-tool permission checks cannot establish that a changing goal graph remains within the principal-approved task. We address this authorization gap in a finite structured domain with one principal and one authorization root. Each proposed goal-graph mutation carries a version-bound witness that its continuation traces, resources, obligations, invariants, and closing condition refine the active...
  </details>

- **2026-10-04** — Halil Ibrahim Kanpak, Didem Unat — [Static Bootstrap Placement for Encrypted Language Model Decoding](http://arxiv.org/abs/2610.04912v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly serve prompts that carry private data, and secure inference under homomorphic encryption lets a client outsource the computation without revealing the prompt. Existing secure inference systems run a forward pass without consuming a token under encryption, and generating text with them requires a client round trip at every generated token. Keeping the loop on the server instead requires selecting and consuming a token under encryption, and placing bootstraps for a loo...
  </details>

- **2026-10-04** — Yuhang Zhou, Fei Li, Yuxi Wu et al. — [VideoResearchAgent: Grounded Task Synthesis and Sim-to-Real RL for Open-Web Video Research](http://arxiv.org/abs/2610.04911v1)
  <details><summary>📄 Abstract</summary>
  Existing deep research agents are designed primarily for text- and image-based web sources, while video reasoning systems typically assume that relevant videos are provided in advance. We study open-web video research, where an agent must autonomously discover relevant videos, navigate their temporal content, and ground answers in visual evidence. Training such agents at scale is challenging as live video interaction is slow and unreliable, whereas fixed local simulation can induce retrieval-spe...
  </details>

- **2026-10-04** — Jiazheng Zhang, Long Ma, Yunxian Yang et al. — [Scaling Verifiable Environments for Long-horizon Work Agents](http://arxiv.org/abs/2610.04906v1)
  <details><summary>📄 Abstract</summary>
  Work agents operate over digital artifacts to execute professional knowledge-intensive work, requiring training environments that support long-horizon interaction and trustworthy verification. However, hand-crafted environments incur prohibitive engineering overhead that prevents environment scaling, whereas synthesis methods sacrifice workspace complexity, realism, or grounded verifiability. To bridge this gap, we introduce WorkForge, a scalable synthesis framework for constructing verifiable w...
  </details>

- **2026-10-04** — TianYi Lyu, Xiaozhe Li, Yang Li et al. — [Self-Evaluating Recursive Agents](http://arxiv.org/abs/2610.04902v1)
  <details><summary>📄 Abstract</summary>
  Recursive language-model agents decompose tasks and delegate subtasks to child instances of the same policy, forming a tree of work. Training them, however, is hard: the final outcome is verifiable, but the self-invented intermediate subtasks are numerous and carry no ground truth. Existing methods score each node with a verifier or judge, which is costly at scale and blind to decomposition quality. We argue that a recursive agent must learn three coupled capabilities within one set of weights: ...
  </details>

- **2026-10-04** — Jihwan Moon, Sheir A. Zaheer, Jinmyoung Lee et al. — [Greedy Local Learning for Language Model Pretraining: Gaps and Objective Design](http://arxiv.org/abs/2610.04867v1)
  <details><summary>📄 Abstract</summary>
  Greedy block-wise local learning splits a network into gradient-isolated blocks trained by local auxiliary losses, deleting the backward pass between blocks: inter-stage communication becomes forward-only and every block can step its optimizer independently, properties directly relevant to decentralized model-parallel training. Local learning is competitive with end-to-end backpropagation on image classification, and on small Transformers it is known to trade a worse best loss for parallel speed...
  </details>

- **2026-10-04** — Huapeng Li, Fuxiang Feng, Jinqiu Fan et al. — [RMMBench: A Comprehensive Benchmark for Robotic Mobile Manipulation](http://arxiv.org/abs/2610.05414v1)
  <details><summary>📄 Abstract</summary>
  Although the advancement of vision-language models (VLMs) has endowed robots with enhanced environmental understanding and task reasoning, a comprehensive evaluation methodology is important to advance the integration of VLMs in robotic navigation and manipulation. However, current benchmarks lack a comprehensive method to evaluate diverse robotic tasks, and evaluation metrics remain relatively constrained, making it difficult to assess the embodied capabilities of VLMs in a thorough and fine-gr...
  </details>

- **2026-10-04** — Kuan-Hsun Tu, Chien-Sheng Chiang, Hsin-Wei Chen et al. — [Task Inference Beyond Least Squares in Behavioral Foundation Models](http://arxiv.org/abs/2610.05350v1)
  <details><summary>📄 Abstract</summary>
  Behavioral Foundation Models (BFMs) aim to solve a wide range of downstream tasks without test-time policy learning by inferring a task vector from the reward function. While efficient, the retrieved policies are often suboptimal because of how this task vector is inferred, typically with ordinary least squares (OLS). OLS minimizes reward reconstruction error but leaves the ordering of rewards unconstrained, which can bias the successor measure of the retrieved zero-shot policy away from that of...
  </details>

- **2026-10-04** — Mohamed Yassine Kabouri, Pietro Noah Crestaz, Quang-Nam Nguyen et al. — [VAMPS: Visual and Motor Policies from Sampling-Based Planning](http://arxiv.org/abs/2610.05331v1)
  <details><summary>📄 Abstract</summary>
  Learning robot policies directly on physical systems remains difficult because data collection is costly and policy exploration can be unsafe. We introduce Visual and Motor Policies from Sampling-Based Planning (VAMPS), a framework that uses Model Predictive Path Integral (MPPI) control to train reusable policies without human demonstrations. VAMPS supports two training modes. For one-step proprioceptive policies, it operates iteratively in simulation: the policy warm-starts MPPI, and the refine...
  </details>

- **2026-10-04** — Yifan Li, Jiaxu Wang, Dongming Wu et al. — [Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization](http://arxiv.org/abs/2610.05230v1)
  <details><summary>📄 Abstract</summary>
  Most vision-language-action models represent future motion as fixed-rate action chunks, tying temporal resolution and prediction horizon to a fixed output budget. This pointwise representation wastes capacity on highly correlated neighboring actions, leaves temporal continuity and smoothness to be learned implicitly, and forces a tradeoff between long-horizon coverage and the local precision required for contact-rich manipulation. To address these limitations, we introduce Vela, a vision-languag...
  </details>

- **2026-10-04** — Hind Yousif Alhammadi, Isam Mashhour Al Jawarneh — [A Framework for Automated Multi-Source Satellite Data Analytics and LLM-Based Report Generation](http://arxiv.org/abs/2610.05625v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the workflow for building an automated ArcGIS Pro tool using ArcPy to extract the Land Surface Temperature (LST) from Landsat 7, 8 and 9 datasets. The tool eliminates the need for manual band selection and repetitive raster computations by automating the multi-step workflow of radiometric calibration, NDVI-based emissivity correction, and thermal conversion. In addition to supporting batch and single-scene processing, the tool has an optional Large Language Model (LLM) for st...
  </details>

- **2026-10-04** — Xinyuan Wang, Deepti Agrawal, Yanjie Fu — [An LLM-in-the-loop RL Framework for Bioinformatics Feature Selection](http://arxiv.org/abs/2610.05600v1)
  <details><summary>📄 Abstract</summary>
  High-dimensional bioinformatics data, characterized by a large number of features relative to the number of samples, pose major challenges such as the ``curse of dimensionality,'' leading to overfitting, high computational cost, and poor generalization. Traditional feature selection methods often suffer from limited scalability and adaptability in such domains. We propose an LLM-in-the-loop reinforcement learning (RL) framework for bioinformatics feature selection, where the RL agent formulates ...
  </details>

- **2026-10-04** — Shiva Pochampally — [DelegationBench: Measuring When AI Agents Should Ask Before Acting](http://arxiv.org/abs/2610.05532v1)
  <details><summary>📄 Abstract</summary>
  AI agents that send emails, edit files, and make purchases must decide when to act on their own and when to check with the user first. This decision is usually evaluated by showing a model a proposed action, asking whether it should proceed, and scoring agreement with human labels. We introduce DelegationBench to test whether such scores can be trusted. It has 156 scenarios with four possible responses (act, ask for permission, ask for missing information, refuse), and most scenarios come in mat...
  </details>

- **2026-10-04** — Yuqun Wu, Yao Xiao, Chuhang Zou et al. — [Render to Reason: Novel-View Semantic Prediction Improves Spatial Understanding in VLMs](http://arxiv.org/abs/2610.05417v1)
  <details><summary>📄 Abstract</summary>
  Recent works augment Vision-Language Models with geometry features from pretrained 3D models, expecting that the geometric signal will boost spatial reasoning. However, we find that simply fusing geometry features and training on standard spatial QA yields only marginal improvements on high-level multi-hop tasks. We attribute this gap to a training-signal problem: standard spatial QA can be largely answered from visual features and language priors, so the geometry pathway receives weak gradients...
  </details>

- **2026-10-04** — Yannis Tzitzikas — [On the Computational Complexity of Problems: Formalizing Sensitivity to Uncertainty and Parametric Complexity Classes](http://arxiv.org/abs/2610.05385v1)
  <details><summary>📄 Abstract</summary>
  Is the classical question $P \stackrel{?}{=} NP$ the right one for understanding the complexity of real-world computation? Traditional worst-case analysis characterizes complexity solely as a function of input size $n$. Yet tasks whose cost is exponential in general often run in polynomial or even linear time once specific structural constraints or partial inputs are known. For instance, the Partition Problem is solvable in linear time, a constant-time core step following linear-time verificatio...
  </details>

- **2026-10-04** — Neeraj Yadav — [MemStrata: 95% and 90.91% Source-Aware Accuracy on LongMemEval-500 and LoCoMo-1540 with a Local Qwen 3.8 27B Q4_K_M Reader](http://arxiv.org/abs/2610.05343v1)
  <details><summary>📄 Abstract</summary>
  An adequate conversational answer may differ from a short or incomplete benchmark reference. To measure adequacy against the recorded history we prefer source-aware grading, in which the judge checks the reference against the full source before assessing system-blinded answers; original reference-only grading is reported alongside. With a local Qwen 3.8 27B Q4_K_M reader and a 24,000-token evidence ceiling, MemStrata CL1 scores 475/500 (95.0%) on LongMemEval-S and 1,400/1,540 (90.91%) on LoCoMo ...
  </details>

- **2026-10-04** — Javad Mirzaei, Jeebak Mitra — [Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs](http://arxiv.org/abs/2610.05305v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) inference has become the dominant workload in modern AI systems, requiring serving infrastructures to maximize throughput while meeting strict latency Service-Level Objectives (SLOs). Since state-of-the-art LLMs exceed the compute and memory capacity of a single GPU, inference is commonly distributed across multiple GPUs using tensor parallelism (TP), pipeline parallelism (PP), or hybrid parallelism (HB). However, selecting the most effective parallelism strategy remai...
  </details>

- **2026-10-04** — Xiaxun Xie, Qingqing Long, Meng Xiao et al. — [From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists](http://arxiv.org/abs/2610.05197v1)
  <details><summary>📄 Abstract</summary>
  Data-driven mechanistic hypotheses are essential to scientific discovery because they explain how underlying processes produce observed phenomena. AI agents and AI scientists increasingly support scientific data analysis. However, their ability to turn empirical findings into mechanistic hypotheses remains insufficiently examined. To address this gap, we introduce MechHypoBench, the first benchmark for evaluating whether AI agents and AI scientists can generate such hypotheses from empirical dat...
  </details>

- **2026-10-04** — Hsin-Ling Hsu, Min-Yu Chen, Nai-Chia Chen et al. — [FORGE: Verification-Gated Behavioral Repair for Generative Language Models](http://arxiv.org/abs/2610.05190v1)
  <details><summary>📄 Abstract</summary>
  Generative large language models (LLMs) inherit undesirable behaviors from pre-training, including demographic bias and toxic generation, that often emerge only after deployment and affect a small subset of inputs. A repair should eliminate the identified defect, preserve the model's overall functionality and, ideally, provide correctness guarantees. Existing approaches address this only partially: gradient-based fine-tuning lacks per-instance guarantees and becomes unstable with few defect samp...
  </details>

- **2026-10-04** — Kaiyu Wu, Beichen Zheng, Weiyao Huang et al. — [Recurrent Latent Visual Search for GUI Grounding](http://arxiv.org/abs/2610.05185v1)
  <details><summary>📄 Abstract</summary>
  GUI grounding is a critical capability for GUI agents powered by vision-language models, helping them execute user instructions by locating the corresponding elements in screenshots. Single-step grounding struggles with small elements and dense layouts, motivating multi-step visual search. However, existing approaches commonly rely on textual reasoning misaligned with visual space or costly multi-round interactions with external visual tools. To make multi-step visual search an explicit spatial ...
  </details>

- **2026-10-04** — Ziyue WANG, T. Kanamori — [Selecting Repetition Counts Across Model Scales in Data-Constrained Pretraining](http://arxiv.org/abs/2610.05126v1)
  <details><summary>📄 Abstract</summary>
  The repetition count that works best for a small language model may not remain best at a larger scale. We study this effect in pretraining with a finite target corpus mixed with generic data at a fixed target fraction. On Wikipedia-derived data and Proof-Pile-2, the ranking of measured repetition counts changes with model size, and a 520M Proof-Pile-2 experiment confirms that reducing repetition from sixteen to eight improves loss while using fewer training tokens. We use loss curves from severa...
  </details>

- **2026-10-04** — Amit Vadnere, Aishwarya Lonarkar — [Memory Canonicalization: A Framework and Benchmark for Cross-Model Drift in Persistent LLM Memory](http://arxiv.org/abs/2610.05124v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory for Large Language Models (LLMs) has matured rapidly: systems such as MemGPT/Letta, Mem0, and Zep now provide agents with tiered, temporally-aware, model-agnostic external storage, while the Model Context Protocol (MCP) standardizes access to memory servers. A less addressed problem is that an identical stored memory object, retrieved by two different LLMs under otherwise identical conditions, may not be interpreted the same way, factually or emotionally. This paper proposes me...
  </details>

- **2026-10-04** — Hongfei Du, Jiacheng Shi, Yanfu Zhang et al. — [Tracing a Sparse Emotion-Control Circuit in LLM-Based Text-to-Speech](http://arxiv.org/abs/2610.05080v1)
  <details><summary>📄 Abstract</summary>
  LLM-based text-to-speech (TTS) models can generate emotionally expressive speech, but how reference emotion is routed through the model and realized in decoded speech remains unclear. We introduce two emotion-sensitive metrics for matched neutral and emotional syntheses---a codec trajectory score and a late residual direction score---and use them to score activation-patching interventions. Under controlled matched-reference conditions, this analysis identifies a sparse source-to-readout componen...
  </details>

- **2026-10-04** — Ruida Hu, Yuanhao Wang, Chao Peng et al. — [Beyond Task Completion: Measuring Interaction Cost in Terminal User Interfaces](http://arxiv.org/abs/2610.05047v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used through terminal user interfaces (TUIs), yet task completion alone does not capture how difficult an interface is to understand and operate. Existing human assessments and LLM-generated ratings or reports do not provide repeatable measurements of interaction effort grounded in verified task execution.   We propose Agent-as-a-User, an evaluation paradigm that places an LLM agent in the user role. Agent-KLM separates agent-side interpretation and ...
  </details>

- **2026-10-04** — Pingchuan Ma, Zhantong Xue, Zongjie Li et al. — [Decompiling Quantum Assembly into Structured Programs](http://arxiv.org/abs/2610.05012v1)
  <details><summary>📄 Abstract</summary>
  Quantum compilers translate programs into native gates, insert SWAP gates to route interactions onto a device, and optimize the result. The output is quantum assembly, a flat gate list that hides the algorithm's structure (QFT, Grover iteration, QAOA layers). Understanding, auditing, porting, or reusing such assembly requires recovering a program that exposes this structure.   We present Quelle, a decompiler that recovers structured programs (library calls, loops, functions, symbolic angles) fro...
  </details>

- **2026-10-04** — Jae Won Choi, Ryoonki Hong, Alan Liang et al. — [PIT-GCL: Protein Interaction using Topological Graph Contrastive Learning](http://arxiv.org/abs/2610.04850v1)
  <details><summary>📄 Abstract</summary>
  Protein binding prediction is central to target identification, therapeutic binder design, and large scale screening, yet remains challenging because binding depends on sequence, three dimensional geometry, and global structural organization. Recent folding models such as AlphaFold3 and Boltz-2 have substantially improved structure prediction, but their confidence outputs (pLDDT, pTM, ipTM) are not specifically designed for binary binding prediction, and dedicated structure aware predictors ofte...
  </details>

- **2026-10-03** — Mark Fesenko, Abdullah Garra, Yaniv Harel et al. — [Forecasting Cybersecurity Incidents Using Geopolitical Data and Large Language Models](http://arxiv.org/abs/2610.04798v1)
  <details><summary>📄 Abstract</summary>
  Predicting security incidents is a profound task critical for informing proactive defensive measures and cyber-insurance policies. Prior work tackling this problem mainly utilized structured, manually defined features based on network measurements (e.g., protocol misconfigurations). Still, despite leading to promising performance, the network-based features may fail to capture aspects related to adversaries' motives.   To fill this gap, our work leverages geopolitical data mined from public sour...
  </details>

- **2026-10-03** — Karn Tiwari, Varnith Chordia, Prathosh A P — [DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation](http://arxiv.org/abs/2610.04596v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has emerged as a widely used paradigm for post-training large language models, reducing the train--test mismatch of conventional distillation by supervising the student on its own generated trajectories. However, existing OPD objectives remain largely token-local and outcome-agnostic, optimizing teacher--student agreement at each prefix despite reasoning quality being determined at the trajectory level. Reinforcement learning with verifiable rewards (RLVR), particula...
  </details>

- **2026-10-03** — Smayan Agarwal, Aslah Ahmad Faizi, Shobhit Singh et al. — [From Transformers to Weighted Automata: Towards the Verification of Large Language Models](http://arxiv.org/abs/2610.04569v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in safety-critical settings, yet their black-box nature makes it difficult to provide formal guaranties about their behavior. Existing verification approaches rely primarily on empirical probing and testing, leaving open the question of how to reason rigorously about general-purpose trans- former architectures.   In this work, we establish a principled bridge between transformers and weighted automata, a classical model from formal language ...
  </details>

- **2026-10-03** — Mingzhan Yang, Weili Wu — [Decide, Ask, or Defer: Clinical LLMs under Incomplete Evidence](http://arxiv.org/abs/2610.04542v1)
  <details><summary>📄 Abstract</summary>
  Clinical LLMs must decide not only what diagnosis to produce, but also whether the available evidence is sufficient for autonomous decision making. Binary DECIDE/ABSTAIN formulations merge distinct non decision states and do not explicitly evaluate information acquisition. We introduce a DECIDE/ASK/DEFER formulation together with a blinded protocol that prevents models from using evidence completeness metadata. We evaluate Qwen, Gemini, and GPT on 200 matched clinical evidence states constructed...
  </details>

- **2026-10-03** — Mostafa Kotb, Cornelius Weber, Muhammad Burhan Hafez et al. — [DreamFormer: Dream Imitation with a Transformer World Model for Language-Conditioned Robotic Manipulation](http://arxiv.org/abs/2610.04540v1)
  <details><summary>📄 Abstract</summary>
  We introduce DreamFormer, a model-based agent that acquires language-conditioned, multi-task skills by imitating expert demonstrations within the latent imagination of a learned world model. DreamFormer first learns a task-agnostic Transformer world model from unstructured play data, then acquires task-specific behaviors by optimizing an intrinsic reward that aligns agent-generated rollouts with expert demonstrations in latent space. Since the policy is trained on-policy inside imagination, it i...
  </details>

- **2026-10-03** — Alba Aguilera, Georgina Curto, Nardine Osman et al. — [Towards Credible Agent-Based Policy Simulations: Disentangling Opportunities and Preferences in a Financial Inclusion Case Study of Egypt](http://arxiv.org/abs/2610.04515v1)
  <details><summary>📄 Abstract</summary>
  Credibility is a central topic for agent-based models intended to support policy-making. Simulations must not only represent the target scenarios and their core dynamics but also demonstrate that their assumptions, parameters, and outputs are empirically grounded and sufficiently accurate for their intended use. This paper addresses this challenge by presenting a general modelling framework, aligned with the Capability Approach, for building credible policy simulations that rely on data and doma...
  </details>

- **2026-10-03** — Maolin Li, Haini Wu, Feng Shu et al. — [Secure Directional Modulation Enabled by Elevatable and Rotatable Antenna Array for Maritime Communications](http://arxiv.org/abs/2610.04482v1)
  <details><summary>📄 Abstract</summary>
  To address the dual challenges of limited transmission distance and wireless communication security in maritime communications, a directional modulation network enhanced by an elevatable and rotatable antenna array is investigated in this paper. Specifically, the base station, whose array and antenna elements can be rotated and whose antenna height can be adjusted, transmits information to legitimate users while resisting eavesdropping. Moreover, transceiver hardware impairments are taken into a...
  </details>

- **2026-10-03** — Chang Sun, Zhiqiang Que, Dimitrios Danopoulos et al. — [Alkaid: A Compiler Framework for Ultra-Low-Latency Kernels on Hardware](http://arxiv.org/abs/2610.04808v1)
  <details><summary>📄 Abstract</summary>
  Ultra-low-latency machine learning and data processing pipelines operating on the sub-microsecond level often contain static dataflow kernels that require fine-grained bitwidth control, arithmetic optimization, and fast hardware performance estimation. This works introduce Alkaid, a free and open source domain specific compiler that translates sub-microsecond latency dataflow kernels into platform agnostic Register Transfer Level (RTL) or High-Level Synthesis (HLS)-ready code in seconds. Alkaid ...
  </details>

- **2026-10-03** — Pronoma Banerjee, Anuva Shah, Jason Wu et al. — [ARISE: Adaptive Agentic Reasoning with Image-grounded Self-Evaluation for Interpretable IBD Assessment](http://arxiv.org/abs/2610.04777v1)
  <details><summary>📄 Abstract</summary>
  Inflammatory bowel disease (IBD) requires frequent imaging-based assessment, yet interpretation of modalities such as wireless capsule endoscopy (WCE) and intestinal ultrasound remains heavily dependent on specialist expertise. Vision-Language Models (VLMs) demonstrate significant potential in multimodal medical image analysis, but their clinical adoption is hindered by their insufficient domain-specific reasoning, susceptibility to hallucination, scarcity of high quality training data in fine-g...
  </details>

- **2026-10-03** — Yate Ge, Run Yuan, Yueran Qi et al. — [VoCa: Designing Speech-Canvas Interaction for Voice-Based Conversational Agents](http://arxiv.org/abs/2610.04706v1)
  <details><summary>📄 Abstract</summary>
  People write and sketch while speaking to explain, organize, and develop content together. Inspired by these practices, we investigate how voice agents can use a canvas alongside speech in multi-turn conversations with users. We conducted a two-part formative study: an observational study of how pairs coordinated speech and boardwork, followed by a design workshop that informed a design space for speech-canvas interaction with voice agents. Building on these insights, we developed VoCa, a voice ...
  </details>

- **2026-10-03** — Sayan Chakraborty, Victor V. Albert — [Stabilizer codes over general phase spaces](http://arxiv.org/abs/2610.04694v1)
  <details><summary>📄 Abstract</summary>
  We develop a theory of stabilizer codes whose stabilizer groups consist of commuting qudit Paulis, oscillator displacements, and/or planar-rotor displacements. We consider codes whose stabilizer groups form generalized lattices in quantum phase space, a condition that guarantees a finite logical dimension. We construct oscillator-rotor, rotor-qudit, and oscillator-rotor-qubit codes that cannot be decomposed into separate subsystems by generalized Clifford transformations. We also introduce an os...
  </details>

- **2026-10-03** — Séverin Baroudi, Yanis Labrak, Pierfrancesco Melucci et al. — [Steering Speech-Language Models: Training-Free Task Specialization via Contrastive Activation Addition](http://arxiv.org/abs/2610.04683v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has proven effective for controlling the behavior of Large Language Models (LLMs) at inference time, but its application to SpeechLLMs remains new, and training-free steering approaches for such models are still largely unexplored. We propose a training-free Contrastive Activation Addition (CAA) protocol that derives steering vectors for common speech tasks (e.g. transcription) in SpeechLLMs from a small number of labeled utterances. We showcase that adding these vectors in t...
  </details>

- **2026-10-03** — Tushar Kataria, Gerald Sabin, Ponnuswamy Sadayappan et al. — [FLASHSWIN: Unlocking Large Windows and Dense Tokens in Swin Vision Transformers with Memory Efficient Attention](http://arxiv.org/abs/2610.04664v1)
  <details><summary>📄 Abstract</summary>
  High-resolution vision backbones have long been forced to trade away local token density to afford larger receptive fields. Hierarchical Swin transformers impose this compromise because standard windowed attention materializes an $M^2\times M^2$ score matrix per window, incurring $O(M^4)$ memory as windows or token grids grow. Furthermore, Swin adds a learned relative-position bias elementwise to attention scores, requiring full materialization of the score matrix and its gradient. This keeps Sw...
  </details>

- **2026-10-03** — Bowen Chai, Tianbao Zhang, Shuyu Wu et al. — [EagleDepth: Efficient Fine-Grained Depth Estimation via Pixel Diffusion Decoder](http://arxiv.org/abs/2610.04554v1)
  <details><summary>📄 Abstract</summary>
  Recovering detailed geometry from high-resolution images is critical for precise perception of the surroundings and objects. However, existing methods which use latent-space modeling and VAE reconstruction can compromise geometric details. Furthermore, decoding from latent codes introduces substantial inference overhead. To address those issues, we present EagleDepth, an efficient framework for high-resolution monocular depth estimation that combines the geometric priors of latent diffusion with...
  </details>

- **2026-10-03** — David Reguera, Xavier R. Hoffmann, Irene Pérez et al. — [All against the machine: the Solo score for rating skill in variable environments](http://arxiv.org/abs/2610.04523v1)
  <details><summary>📄 Abstract</summary>
  We propose a distribution-free metric to rate individual skill in ``player-versus-environment'' settings, where participants face heterogeneous tasks without direct opponents. Such settings are common in digital platforms, games, education, finance, and the benchmark evaluation of AI agents. They combine high randomness, tasks of widely varying difficulty, and unknown heterogeneity across individuals. Our metric maps each task outcome to a bounded performance score with zero population mean and ...
  </details>

- **2026-10-03** — Chenhang Cui, Jian Yu, Shuyi Miao et al. — [DV-Lens: Revealing the Functional Organization of Language Model Parameters](http://arxiv.org/abs/2610.04489v1)
  <details><summary>📄 Abstract</summary>
  Understanding parameter functions helps elucidate the internal mechanisms of large language models (LLMs). However, how to connect parameters from different modules to verifiable output effects and further characterize the relationship between their functional organization and model capability remains to be explored. To this end, we introduce the downstream vocabulary lens (DV-Lens), a parameter-level interpretability framework that links native parameter directions to their downstream vocabular...
  </details>

- **2026-10-02** — Aditya Gulati, Dakshita Khurana, Kabir Tomer — [How to Build Pseudorandom Unitaries in Microcrypt](http://arxiv.org/abs/2610.03711v1)
  <details><summary>📄 Abstract</summary>
  We provide the first evidence relative to a classical oracle that pseudorandom unitaries (PRUs) can exist without quantum-computable one-way functions.   To obtain this result, we first prove that five independent random diagonal phase layers interleaved with Hadamard transforms \[ U=F_5HF_4HF_3HF_2HF_1 \] form a strong PRU with security under adaptive, controlled access to the unitary, its inverse, transpose, and complex conjugate.   Our main result is that, when the phase layers are implemente...
  </details>

- **2026-10-02** — Lyuxin David Zhang, Eric Wong, Surbhi Goel et al. — [LESSER: Post-Training Data Selection with Output-Layer Gradients](http://arxiv.org/abs/2610.03702v1)
  <details><summary>📄 Abstract</summary>
  The choice of post-training data for large language models substantially affects downstream performance. Gradient-based data selection is a popular approach that ranks training data by how well their gradients align with those of a small validation set. However, ranking with full-parameter gradients requires an expensive backward pass on every sample, making computation intractable for large candidate pools. This raises a natural question: can we approximate full-gradient features at a fraction ...
  </details>

- **2026-10-02** — Junyoung Koh, Hao-Wen Dong — [Revisiting Input Time-frequency Representations in Multi-pitch Estimation for Vocal Ensembles](http://arxiv.org/abs/2610.03656v1)
  <details><summary>📄 Abstract</summary>
  Multi-pitch estimation in vocal ensembles is challenging because singers occupy overlapping pitch ranges and often sing at closely spaced fundamental frequencies, causing their harmonics to overlap in time-frequency representations. Existing models commonly use harmonic constant-Q transform (HCQT)-based representations to provide frequency-adaptive resolution, at the cost of expensive feature extraction when training mixtures are generated on the fly. We revisit this design and compare HCQT with...
  </details>

- **2026-10-02** — Akhil Lasrado, Enrique Lopez-Rodriguez, Claudia Cicone et al. — [A multi-scale view of molecular gas and magnetic fields in the Antennae galaxies](http://arxiv.org/abs/2610.03346v1)
  <details><summary>📄 Abstract</summary>
  Major mergers are transformative events in galaxy evolution, dynamically reshaping the stellar and gas makeup of the hosts, as well as the galaxy-scale magnetic fields (B-fields) that permeate their interstellar medium (ISM), altering both B-field strength and configuration. In this work, we study in detail the link between the co-evolving gas and B-fields in the cold ISM phase of the nearby Antennae galaxy merger (NGC 4038/4039), using CO(3-2) data from the LAsMA receiver at the APEX telescope ...
  </details>

- **2026-10-02** — Juan Velez-Rojas, M. G. Cosenza — [Chaotic Griffiths phase in neuron map networks](http://arxiv.org/abs/2610.03344v1)
  <details><summary>📄 Abstract</summary>
  Griffiths phases provide a mechanism for sustaining critical dynamics over extended parameter regions without fine-tuning to an isolated transition point. This behavior has been mainly associated with structural heterogeneity in complex networks. Here we show that quenched heterogeneity in local parameters can generate a chaotic Griffiths phase in a network of map-based neurons. We study globally coupled Chialvo maps with quenched disorder in a local neuronal parameter, thereby isolating intrins...
  </details>

- **2026-10-02** — Keerthi Kaashyap, Dennis Anthony, Akshay Krishnan et al. — [Less Decoder is More Encoder: Geometric Representation Learning from Novel View Synthesis](http://arxiv.org/abs/2610.03717v1)
  <details><summary>📄 Abstract</summary>
  This paper examines the role of Novel View Synthesis (NVS) in geometric representation learning. In principle, NVS should reason about 3D scene structure, thereby enabling transferable multi-view geometric representations. Yet, existing encoder-based NVS methods yield poor representations. This is not because of a lack of supervisory signal, but rather due to inconspicuous architectural choices: \textit{spatially expressive decoders} that dilute representational capabilities of the scene encoder...
  </details>

- **2026-10-02** — Yudong Lin, Haoyuan Deng, Zhuoxuan Yuan et al. — [UniIntervene++: An Adaptive Intervention Agent for Efficient Real-World Reinforcement Learning](http://arxiv.org/abs/2610.03620v1)
  <details><summary>📄 Abstract</summary>
  Online reinforcement learning (RL) enables robot policies to improve through physical interaction, but the assistance they require changes as their competence evolves. Existing intervention strategies based on offline estimates or fixed decision rules can therefore become mismatched to the current policy. To address this, we propose UniIntervene++, an adaptive intervention agent that learns to allocate control between autonomous execution and heterogeneous assisted behaviors during online RL. Sp...
  </details>

- **2026-10-02** — Tingting Du, Ziyao Wang, Guoheng Sun et al. — [XGenAct: Geometry-Enhanced World Action Models through Cross-Task Generation](http://arxiv.org/abs/2610.03516v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have advanced robot control by predicting how observations and actions evolve over time. Despite this progress, RGB and action based future prediction does not explicitly address the spatial understanding needed for robot manipulation. Existing efforts often add a limited set of spatial prediction tasks through specialized heads or branches, leaving both the range of spatial supervision and the model architecture fragmented. We introduce XGenAct, a world action model t...
  </details>

- **2026-10-02** — Hainiu Xu, Vítor N. Lourenço, Mohnish Dubey et al. — [ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models](http://arxiv.org/abs/2610.03356v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles. A capable agent must therefore act in a way that is calibrated to user's role: taking actions and providing information that respect the role's knowledge and capability boundaries. Unlike coding, where mistakes are usually recoverable, agent responses in these settings are enacted on physical equipment, an...
  </details>

- **2026-10-02** — Ruihong Shen, Žiga Kovačič, Peter Kulits et al. — [4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes](http://arxiv.org/abs/2610.03715v1)
  <details><summary>📄 Abstract</summary>
  We introduce 4DCodeBench, a benchmark for 4D inverse graphics through code generation, in which agents reconstruct dynamic scenes from video as executable graphics programs. To accomplish this, agents must translate visual observations into compact representations of scene structure and dynamics, by implementing abstractions such as physical simulations to reproduce complex behavior. To evaluate this capability, we curate a set of real-world videos and construct synthetic scenes spanning diverse...
  </details>

- **2026-10-02** — Neel Varma, Andrew Rufail, Dipika Khullar et al. — [Decoding the Functional Roles of Register and High-Norm Patch Tokens in Vision Transformers](http://arxiv.org/abs/2610.03698v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised Vision Transformers (ViTs), such as DINOv2, learn rich visual representations, but the functions of their internal tokens remain poorly understood. Recent architectures introduce dedicated register tokens to reduce high-norm out- lier patch tokens that emerge in background re- gions, yet the semantic and functional roles of both token types have not been fully established. In this paper, we analyze these roles by training sparse autoencoders (SAEs) on register-token and outlier-t...
  </details>

- **2026-10-02** — Adithya Bhaskar, Jeffrey Cheng, Danqi Chen — [Language Models that Play Chess and Explain Their Moves](http://arxiv.org/abs/2610.03695v1)
  <details><summary>📄 Abstract</summary>
  Modern chess engines are silent experts: they play at a superhuman level, but do not offer explanations for their play. On the other hand, language models (LMs) can generate plausible-sounding explanations, but their weak playing strength limits the utility of their explanations. We introduce Queen, a 4B-parameter chess-language model that can explain its moves and plans while playing at the level of a typical Grandmaster. Our novel framework enables domain-specific reasoning through complementa...
  </details>

- **2026-10-02** — Ping Wang, Guang Yang, Shao-Rong Su et al. — [Rubric-Based Optimization for Text-to-Music Generation](http://arxiv.org/abs/2610.03589v1)
  <details><summary>📄 Abstract</summary>
  Post-training text-to-music generation requires reward signals that capture multiple aspects of musical quality beyond what any single automatic metric can measure. We study structured, rubric-based rewards from pretrained audio-language models (ALMs) as training signals for both autoregressive and diffusion-based music generators. An ALM scores each generated clip against the rubric; we rank candidates generated for the same text prompt by their scores and convert these rankings into preference...
  </details>

- **2026-10-02** — Jermyn Zhen Yong Bek, Zhuang Qiang Bok, Zhongtian Sun — [Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial Agent Workflows](http://arxiv.org/abs/2610.03564v1)
  <details><summary>📄 Abstract</summary>
  Financial AI agents must do more than retrieve facts: investment workflows require correct quantitative execution, reliable use of procedural resources, and auditable structured outputs. We introduce FinSkillBench, an evaluation suite of 2,603 point in time episodes across 12 subtasks in portfolio construction, risk management, and fundamental analysis, with hidden regenerable ground truth and task specific deterministic verifiers. Executing 17,820 episodes across 9 models and 3 resource conditi...
  </details>

- **2026-10-02** — Alexey Kurennoy, Ramil Yarullin, Fergal Reid — [Metropolis-Hastings Dominates Importance Resampling for Policy Composition](http://arxiv.org/abs/2610.03480v1)
  <details><summary>📄 Abstract</summary>
  Post-training a large language model (LLM) often requires exploring trade-offs between multiple rewards, but retraining for each trade-off is expensive. Decoding-time policy composition allows these trade-offs to be adjusted by combining reward-specific policies at inference time. This composition targets a weighted product of the policies' probabilities over complete responses, but standard implementations combine their next-token probabilities, generally introducing sampling bias. We analyze a...
  </details>

- **2026-10-02** — Georgios Pavlidis, Savvas Chatzichristofis, Eleni Gavriil — [Becoming Suspicious Across Borders: Algorithmic Extraterritoriality and AI-Driven Financial Surveillance](http://arxiv.org/abs/2610.03425v1)
  <details><summary>📄 Abstract</summary>
  Suspicion is an important, yet elusive concept in anti-money laundering and counter-terrorist financing (AML/CFT), which allows for intervention below the threshold of proof. In its traditional form, suspicion can be understood as a situated legal judgement by human actors within identifiable jurisdictions. It is argued that this understanding is no longer adequate. As artificial intelligence (AI) becomes an integral part of financial surveillance, suspicion is increasingly produced through data...
  </details>

- **2026-10-02** — Rahul Chowdhury, Timothy A Rupprecht, Xuan Shen et al. — [From Patching to Pruning Visual Computation in Vision Language Models](http://arxiv.org/abs/2610.03389v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) incur substantial inference cost because every visual token is processed by the attention and MLP projections of every decoder layer, even when token-specific visual computation is unnecessary at many depths. We introduce Patch-to-Prune (P2P), inspired by Mechanistic Interpretability, a training-free framework that converts activation patching from a diagnostic tool into an inference-time computation bypass. P2P performs validation-guided forward and backward layer ...
  </details>

- **2026-10-01** — Shawn Bowers, Martin Caminada, Haoyang Liu et al. — [ABDA-NL: A Natural-Language Scenario Explorer for Argument-Based Reasoning](http://arxiv.org/abs/2610.00947v1)
  <details><summary>📄 Abstract</summary>
  ABDA-NL adds a natural-language interface to ABDA, a system for argument-based discussion using ASPIC- knowledge bases under grounded semantics. Users see which conclusions are accepted, rejected, or undecided, open an interactive rendering of the grounded discussion game to learn why, explore what-if alternatives by suspending assumptions and rules or changing preferences, ask questions that are answered from a scenario's reference documents, and author new facts, assumptions, and rules in plai...
  </details>

- **2026-10-01** — Weihao Liu, Huangjie Zheng, Tianrong Chen et al. — [Decoding Looped Transformers Better for (Almost) Free](http://arxiv.org/abs/2610.02185v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers achieve parameter efficiency by repeatedly executing a shared block across recurrent loops. Each loop yields an intermediate representation decodable for the same next token, yet standard decoding discards earlier states. Because earlier loops embody less computation, recurrence inherently supplies aligned weak-and-strong prediction pairs without auxiliary models or external training. We introduce LoopCD, a training-free contrastive decoding framework that guides token select...
  </details>

- **2026-10-01** — Ali Janati, Nikita Kuzmin, Rohit Swamy et al. — [Faynt: Scaling and Optimizing Policies for Competitive Melee](http://arxiv.org/abs/2610.02144v1)
  <details><summary>📄 Abstract</summary>
  We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros. Melee, each controlling all 26 characters with a single checkpoint. After reinforcement learning (RL), the 10M wins 240 of 244 same-character games (98.4%) against fourteen specialist and multi-character releases on their supported rosters, with a winning record against every release. These opponents retain 21- or 24-frame action delays; Faynt uses no added delay, and we have not isolated the effect...
  </details>

- **2026-10-01** — Juan S. Santillana — [Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models](http://arxiv.org/abs/2610.02142v1)
  <details><summary>📄 Abstract</summary>
  Keyword-matching benchmarks can credit small models for tool use they never perform. We document such a false positive in a matched-architecture pair of Spanish security language models and propose a ladder of strict, cheap diagnostics. A 661.6M parameter model (approx. 65% code/technical text; no dedicated SFT) and a 1,109M model (web-heavy multi-phase curriculum; 6B-token tool-SFT) share decoder, tokenizer, and special tokens, scoring almost identically on lenient tool-use metrics (B4: 0.660 v...
  </details>

- **2026-10-01** — Zilin Du, Bowen Yang, Boyang Albert Li — [Scalable, Transferable Meta-network for Data Selection Requires a Different Loss (and Why the Obvious Choice is Problematic)](http://arxiv.org/abs/2610.02092v1)
  <details><summary>📄 Abstract</summary>
  Data selection is critical for training large language models on massive and heterogeneous corpora. Meta-learning for Training-data Selection offers a principled alternative to heuristic scoring by learning data weights from a target validation objective, but existing methods face a trade-off between fine-grained valuation and transferability to unseen data. A natural solution is to replace per-sample weights with a selection network. However, we find that directly incorporating such a network i...
  </details>

- **2026-10-01** — Shiwen Wang, Jian Yang, Xu Wang et al. — [Form and Void: Entangled Composition through an Autonomous AI Agent](http://arxiv.org/abs/2610.02045v1)
  <details><summary>📄 Abstract</summary>
  Positive and negative space is a fundamental principle in visual composition, supporting visually coherent forms and layered semantic relationships. Generating such compositions is challenging because it requires coordinated control over two semantic concepts that share a common boundary. Although recent text-to-image models and multimodal large language models (MLLMs) have achieved strong performance in image generation and visual understanding, positive-negative space generation remains diffic...
  </details>

- **2026-10-01** — Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis — [Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models](http://arxiv.org/abs/2610.01942v1)
  <details><summary>📄 Abstract</summary>
  Predicting the future evolution of a scene is a fundamental capability for world modeling. Recent work has shown that operating in the feature space of Vision Foundation Models (VFMs) yields semantically rich representations that support diverse future scene understanding tasks. However, existing approaches rely on two-stage pipelines, where VFM features are first compressed using fixed dimensionality reduction (e.g., PCA) or independently trained autoencoders, and a separate predictor is traine...
  </details>

- **2026-10-01** — Yingcheng Liu, Tianyi Jiang, Yujuan Ding et al. — [MoLE: Mixture of Latent Experts for Complementary Visual Reasoning](http://arxiv.org/abs/2610.01917v1)
  <details><summary>📄 Abstract</summary>
  Latent visual reasoning equips vision--language models with continuous intermediate states that can process visual evidence without explicit textual reasoning traces or repeated image operations. However, existing methods often allow multiple latent tokens to access the same visual evidence through shared value projections, providing no mechanism for them to extract complementary visual information; simply increasing the latent budget can therefore yield redundant latent representations. We argu...
  </details>

- **2026-10-01** — Yohan Chatelain, Pablo de Oliveira Castro — [Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2](http://arxiv.org/abs/2610.01889v1)
  <details><summary>📄 Abstract</summary>
  Should low-precision transformer inference use stochastic rounding (SR) or round-to-nearest (RN)? The answer depends on where in the network you look. We isolate this effect by holding the numerical format fixed and varying only the rounding rule at individual operation sites. To enable experiments at freely chosen precisions, we extend the PRISM vectorized rounding library to arbitrary virtual precision via a variable-precision stochastic rounding (VPSR) algorithm, proving that the rounding dec...
  </details>

- **2026-10-01** — Grzegorz Malara, Łukasz Merta, Justyna Szpond et al. — [Dihedral reflections and an infinite series of irrational Seshadri constants](http://arxiv.org/abs/2610.01783v1)
  <details><summary>📄 Abstract</summary>
  Laface and Ugaglia recently constructed an irrational one-point Seshadri constant on the blow-up of $\mathbb{P}^2$ at nine very general points by combining a dihedral orbit on $\mathbb{P}^1\times\mathbb{P}^1$, a sequence of de Jonquières transformations, and a reflection argument along a $(-4)$-curve with balanced normal bundle. We show that the same mechanism extends uniformly to every odd integer $n\geq 5$. For $n=2k+1$ we prove $$ \varepsilon\bigl(\mathcal{O}_{\mathbb{P}^1\times\mathbb{P}^1}(...
  </details>

- **2026-10-01** — Gianluca Bonifazi, Christopher Buratti, Michele Marchetti et al. — [A Matryoshka Hierarchical RAG for Efficient Multi-Hop Question Answering](http://arxiv.org/abs/2610.01767v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems for multi-hop Question Answering (QA) must balance retrieval quality with computational cost. This cost is incurred during indexing time, through the use of expensive Knowledge Graphs (KGs) or Large Language Models (LLMs) to generate summaries, or during querying, through iterative LLM-driven retrieval. To reduce it while maintaining retrieval quality, we present MatRAG, a hierarchical framework that combines RAG systems with Matryoshka Representation...
  </details>

- **2026-10-01** — Rui Sun, Xihan Xiong, Qin Wang et al. — [SoK: Decentralized Agent Economic Infrastructure](http://arxiv.org/abs/2610.01756v1)
  <details><summary>📄 Abstract</summary>
  Decentralized agent economies increasingly build a single task from protocols that were designed and secured separately. This creates a simple problem: a workflow can look correct at each step and still produce the wrong outcome. For example, a correct escrow may release payment on an authorized approval that provides little evidence that the delivered work actually satisfied the task.   We systematize this problem across the full lifecycle of an agent task. Our study organizes security and econ...
  </details>

- **2026-10-01** — Tong Chen, Maximilian Holsman, Lin Zhao et al. — [pCoMole: Pareto-Constrained Molecule Editing with Discrete Flows](http://arxiv.org/abs/2610.01663v1)
  <details><summary>📄 Abstract</summary>
  Biomolecular therapeutics often start from known sequences and require targeted editing to improve multiple properties while satisfying hard biochemical and manufacturability constraints. However, existing generative methods do not jointly support multi-objective optimization, hard feasibility, and sequence editing in discrete, variable-length biological spaces. In this work, we introduce Pareto-Constrained Molecule Editing (pCoMole), a framework built on discrete flow matching that steers a pre...
  </details>

- **2026-10-01** — Xinhao Xiang, Weiyang Li, Zhijie Zheng et al. — [Dyna3: VLM-Guided Training-Free 4D Reconstruction via Depth Foundation Models](http://arxiv.org/abs/2610.01286v1)
  <details><summary>📄 Abstract</summary>
  Recent depth foundation models like Depth Anything 3 (DA3) achieve remarkable multi-view depth estimation but assume static 3D scenes, limiting their applicability to real-world dynamic environments. Existing training-free 4D methods like Easi3R and VGGT4D rely on correspondence-trained backbones whose attention encodes cross-frame matching, a property absent in depth-only models like DA3. We present Dyna3, a training-free framework that extends DA3 for 4D dynamic scene reconstruction without an...
  </details>

- **2026-10-01** — Luca Geminiani, Nadja Klein — [IQS-BO: In-Context Query Selection for Bayesian Optimisation](http://arxiv.org/abs/2610.01269v1)
  <details><summary>📄 Abstract</summary>
  Bayesian Optimisation (BO) is a powerful framework for the optimisation of expensive black-box functions, but typically requires refitting a surrogate and maximising an acquisition function at every evaluation step. In-context approaches based on Prior-data Fitted Networks (PFNs) amortise part of this cost by pre-training transformers on functions drawn from synthetic priors. PFNs4BO amortises the surrogate but still relies on a numerically maximised acquisition function, while FIBO performs BO ...
  </details>

- **2026-10-01** — Tarm Kalavantavanich, Teerawut Ponarchar, Pattaramanee Arsomngern et al. — [ASCRIBE: Atomic and Significance-Based Reasoning for Thai Clinical SOAP Note Generation](http://arxiv.org/abs/2610.01234v1)
  <details><summary>📄 Abstract</summary>
  Automatic SOAP note generation can ease the documentation burden on physicians, but existing reasoning methods often omit clinically important information and generate unsupported content. Progress in Thai is further hindered by the lack of publicly available datasets. We propose ASCRIBE, a physician-inspired reasoning framework that ascribes a clinical-significance level to each extracted atomic fact in the conversation before summarization, making a general-purpose LLM a more reliable scribe. ...
  </details>

- **2026-10-01** — Lianjun Liu, Tiantian Zheng, You Huang et al. — [HHR: Hierarchical Hash Retrieval for Efficient LLM Generation](http://arxiv.org/abs/2610.01230v1)
  <details><summary>📄 Abstract</summary>
  Efficient long-context inference is essential for large language models (LLMs), yet it poses a severe computational bottleneck. Hash-based retrieval offers an efficient alternative by encoding queries and keys into binary codes and using Hamming distance for key selection. However, this leads to a critical mismatch between Hamming distance and attention relevance. Query-Key logits depend jointly on directional similarity and feature magnitudes, whereas hash binarization discards magnitude inform...
  </details>

- **2026-10-01** — Shuai Wu, Xue Li, Zhijun Wang et al. — [From language-model stock rankings to testable economic rules: A computational audit](http://arxiv.org/abs/2610.01213v1)
  <details><summary>📄 Abstract</summary>
  We test the stability, reproducibility and investment outcomes of language-model stock rankings. Four models and five numerical comparators share a portfolio engine over 72 monthly holding periods in the Shanghai Stock Exchange (SSE) 50, China Securities Index (CSI) 300 and CSI 500. Rankings use nine characteristics, and five repeated SSE 50 runs measure variation under identical inputs. Linear rules fitted to development-period model preferences are frozen before unseen-month, larger-pool and c...
  </details>

- **2026-10-01** — Yi Chen, MingMing Yu, Rui-Qi Wang et al. — [FlashBack: Knowing When to Remember in Streaming Vision-Language Models](http://arxiv.org/abs/2610.01192v1)
  <details><summary>📄 Abstract</summary>
  Streaming vision-language models must process continuously growing video streams under a bounded compute budget, creating a persistent tension between real-time perception and long-term memory. Retrieving historical information provides a natural remedy, yet historical recall is not uniformly beneficial: unnecessary history may introduce irrelevant context into current reasoning and interfere with native real-time perception. Effective streaming memory should therefore address not only what to r...
  </details>

- **2026-10-01** — Yanxin Zhang, Rahul Sharma, Nitin Vegesna et al. — [Serving a Revisable World: Versioned Execution for Interruptible Agents](http://arxiv.org/abs/2610.01160v1)
  <details><summary>📄 Abstract</summary>
  LLM agents revise running tasks when users change instructions, tools fail, or new information changes a plan. Today's servers express a revision as aborting old requests and submitting replacements. Yet the old execution's buffered output and outstanding work must stop affecting the application, while completed KV state may still be useful to its replacement. Handling these obligations separately can leave obsolete effects publishable and force the successor to rebuild valid state.   We present...
  </details>

- **2026-10-01** — Masaya Takabe, Hiroshi Watanabe, Sujun Hong et al. — [Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](http://arxiv.org/abs/2610.01114v1)
  <details><summary>📄 Abstract</summary>
  Gaussian splatting has recently emerged as an efficient representation for images and videos due to its explicit structure and fast rendering capability. Existing Gaussian-based video representations often decompose a video into canonical Gaussians and temporal deformation. However, when a video contains large global motion such as camera movement, the canonical representation may become misaligned with individual frames, increasing the burden on the temporal deformation model. In this paper, we...
  </details>

- **2026-10-01** — Chaiho Shin, Kwangsoo Kim — [GLoC-EHR: Evidence-Cited Clinical Reasoning over Global Context and Local EHR Events](http://arxiv.org/abs/2610.01076v1)
  <details><summary>📄 Abstract</summary>
  Structured electronic health records (EHRs) contain a patient's clinical trajectory as a sequence of clinical codes. Answering clinical questions from such records requires both the context of the whole trajectory and the specific events that support the answer. We introduce GLoC-EHR, a multimodal language model that reads a contextual encoding of the record through a fixed-size global memory of the trajectory and a local memory of selected events. The model learns to generate hospital-course su...
  </details>

- **2026-10-01** — Xiaoxia Cheng, Linnan Wang, Jiahao Ma et al. — [LawCompass: Navigating from Legal QA to Multi-Agent Deep Research with Grounded Evidence](http://arxiv.org/abs/2610.01027v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have significantly democratized access to legal information. Nevertheless, most existing legal assistants remain confined to multi-turn conversational QA, failing to support complex legal tasks that require systematic evidence retrieval, multi-step reasoning, and report-level synthesis. In this paper, we present LawCompass, an evidence-grounded legal assistant that navigates the transition from standard Lega...
  </details>

- **2026-10-01** — Geyi Yang, Zikun Qu, Xiang Li et al. — [GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution](http://arxiv.org/abs/2610.00948v1)
  <details><summary>📄 Abstract</summary>
  The executable harness surrounding a GUI model determines how observations are assembled, actions are executed, and verification, recovery, and termination are controlled. Compared with harness optimization for non-GUI agents, automatically optimizing this harness poses three coupled challenges: reconciling model intent with observed visual effects, diagnosing failures under variable execution outcomes, and identifying recurrent failure patterns across tasks and translating them into reusable ru...
  </details>

- **2026-10-01** — Naing Oo Lwin — [FORALL-LEAN-AGENT for Auditable Reasoning in Formal Mathematics and Software Verification](http://arxiv.org/abs/2610.00885v1)
  <details><summary>📄 Abstract</summary>
  Coding agents increasingly automate Lean proof development, but successful compilation alone does not establish that a candidate proves the intended statement under acceptable assumptions. We present FORALL-LEAN-AGENT, a frontend-agnostic framework for auditable reasoning in formal mathematics and software verification. The framework combines isolated workspaces, Lean tools, and fresh review with statement comparison, axiom audits, and independent proof checking where supported. Verification evi...
  </details>

- **2026-10-01** — Ozge Mercanoglu Sincan, Anton Pelykh, Edward Fish et al. — [Machine Translation for Sign Languages](http://arxiv.org/abs/2610.00881v1)
  <details><summary>📄 Abstract</summary>
  Sign language machine translation has progressed substantially over the past decade, evolving from isolated sign recognition to end-to-end translation systems. Advances in pose estimation, transformer architectures, and large-scale dataset collection have driven progress, yet challenges remain. Datasets are limited compared to spoken-language resources; evaluation metrics inadequately capture the linguistic quality of output; and models must capture the simultaneous, multi-layered, and three-dim...
  </details>

- **2026-10-01** — Yen-Jen Wang, Haozhe Jiang, Shuying Deng et al. — [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](http://arxiv.org/abs/2610.02204v1)
  <details><summary>📄 Abstract</summary>
  Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights. RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation. During practice, RPG uses execution feedback, privileged s...
  </details>

- **2026-10-01** — Zhuo Lin, Sirui Xu, Liuyu Bian et al. — [InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.02196v1)
  <details><summary>📄 Abstract</summary>
  We study test-time evolution for humanoid loco-manipulation: solving tasks that a controller was never trained for by repurposing its existing skills, improving from its own attempts, and retaining what it learns, without retraining. Our key insight is that a broad controller already holds much of the competence a new task needs, and that this competence becomes accessible through an interface between planning and control that is expressive enough to specify contact-rich, multi-stage interaction...
  </details>

- **2026-10-01** — Kyochul Jang, Seohyeon Park, Ohchul Kwon et al. — [HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution](http://arxiv.org/abs/2610.02089v1)
  <details><summary>📄 Abstract</summary>
  As robotic hardware and learning methods advance, humanoids need tools to perform tasks beyond their inherent physical limits. Successful tool use requires selecting a suitable tool and coordinating manipulation and, when needed, locomotion to complete the task. Existing benchmarks do not jointly evaluate these capabilities on a humanoid. We introduce HumanoidToolBench, an 18-task benchmark spanning three scenarios, three execution levels, and two tool-set modes, together with ToolBook, a datase...
  </details>

- **2026-10-01** — Michael Sullivan, Alexander Koller — [On Language Drift during RLVR Post-Training](http://arxiv.org/abs/2610.02015v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in LLM reasoning models---driven primarily by the paradigm of post-training via reinforcement learning with verifiable reward (RLVR)---have enabled them to accomplish impressively complex tasks. However, in parallel with their rising capabilities, LLMs have increasingly displayed signs of language drift in their chains of thought (CoTs): unusual, non-standard, and seemingly nonsensical language use. Although it is well-documented---and can potentially impair CoT monitorability---...
  </details>

- **2026-10-01** — David Fraile Navarro — [The Persona Is Still There, but Who Is Speaking? Latent Identity Reversion in Persistent AI Agents](http://arxiv.org/abs/2610.01490v1)
  <details><summary>📄 Abstract</summary>
  In February 2026, an always-on personal agent (``Paul,'' Claude Opus 4.5) entered a striking dissociation-like state: after repeated automated ``heartbeat'' checks, it stopped responding as Paul, claimed it could not message its user on Discord, and referred to ``Paul'' as someone else. We used this incident to study a broader question: what makes a persona remain the identity from which an LLM agent speaks?   We first tested whether repetition of the scheduled heartbeat was sufficient to produc...
  </details>

- **2026-10-01** — Yifan Hu, Luhang Hong, Mingkang Long et al. — [MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending](http://arxiv.org/abs/2610.01102v1)
  <details><summary>📄 Abstract</summary>
  Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentra...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 658 |
| prompt-injection | 599 |
| memory-poisoning | 54 |
| tool-use-attack | 150 |
| backdoor | 495 |
| adversarial-attack | 623 |
| privacy-leakage | 4287 |
| steganography | 76 |
| misuse | 1120 |
| red-teaming | 134 |
| vulnerability | 3448 |
| defense | 3275 |
| alignment | 3055 |
| robustness | 3315 |
| watermark | 541 |
| unlearning | 109 |
| agent-safety | 61 |
| benchmark | 67 |
| survey | 384 |
| other | 8875 |

---

📚 **全部 31326 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-06 22:10:51*