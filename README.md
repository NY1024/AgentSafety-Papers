<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-31616-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-07 22:33 ｜ **论文总数 / Total Papers**: 31616（近 30 天 / Recent 30 days: 4916）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 31616 篇论文（含摘要、分类筛选、搜索）/ View all 31616 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 663
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 603
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 54
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 150
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 501
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 626
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4306
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 76
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1128
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 134
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3482
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3303
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3083
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3344
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 549
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 110
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 61
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 387
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8989

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4916 篇，完整 31616 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4916 papers from the last 30 days (with date, authors & abstract). For the full list of 31616 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 8 papers

- **2026-10-06** — Yichi Zhang, Zhiqi Wang, Neil Gong et al. — [Secure Speculative Decoding for Large Language Models](http://arxiv.org/abs/2610.08678v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates inference for a large language model (LLM), referred to as the \emph{target model}, by first using a smaller model, referred to as the \emph{draft model}, to generate candidate tokens and then verifying them with the target model for acceptance or rejection. Prior studies primarily focused on the efficiency-utility trade-off of speculative decoding, e.g., lossy speculative decoding, leaving its security implications largely unexplored.   In this work, we bridge t...
  </details>

- **2026-10-05** — Wonjun Lee, Kyungsik Yang, Gaeun Ji et al. — [Safeguarding LLMs via Model-Agnostic Latent Safety Signals from Dark Knowledge](http://arxiv.org/abs/2610.07532v1)
  <details><summary>📄 Abstract</summary>
  LLMs have advanced rapidly, raising growing concerns about their safety. Recent work has proposed approaches to detect and defend against attacks including defenses at decoding stage that leverage models' hidden states. However, existing decoding-stage defenses suffer from two limitations. First, they introduce a trade-off between safety and over-refusal, where strengthening safety degrades the model's helpfulness on benign queries. Second, many of these methods rely on internal hidden states an...
  </details>

- **2026-10-05** — Shai Feldman, Yaniv Romano — [Dynamic Budget Allocation for LLM Evaluation under Hard Resource Constraints](http://arxiv.org/abs/2610.07362v1)
  <details><summary>📄 Abstract</summary>
  We evaluate large language models (LLMs) in multi-turn interactions through their time-to-event: the number of interaction steps required to produce an event of interest, such as a successful jailbreak or agentic task completion. Under limited compute, interactions may be terminated before the event occurs, so that event times are only partially observed (censored). Existing allocation methods for calibrating time-to-event bounds satisfy the budget only in expectation and can exceed the availabl...
  </details>

- **2026-10-05** — Abhinav Sudhakar Dubey, Scott Sirri, Vaggos Chatziafratis et al. — [Jailbreaking Open-Weight LLMs via Random Embedding Perturbations](http://arxiv.org/abs/2610.07125v1)
  <details><summary>📄 Abstract</summary>
  While open-weight models have enjoyed steady progress in capabilities and wide adoption across multiple domains, their safety remains an important concern. One key feature is the ability to refuse or deflect harmful, malicious, or insensitive prompts. In this paper, we expose safety vulnerabilities across six common open-weight LLMs of various sizes that consistently lead to harmful or unsafe responses on the JailbreakBench benchmark dataset. Our proposed attack, Perturbed Embedding Vector (PEV)...
  </details>

- **2026-10-05** — Xunguang Wang, Qingyue Wang, Yuguang Zhou et al. — [Benchmarking Jailbreak Guardrails for Embodied Agents](http://arxiv.org/abs/2610.06122v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents powered by large language models and vision-language models are increasingly deployed in physical environments, but jailbreak attacks can induce these agents to perform physically harmful actions. A growing number of guardrail methods have been proposed to intercept dangerous behavior before it is executed, yet existing safety benchmarks evaluate the embodied models themselves, leaving it unclear how well these guardrails actually defend an embodied agent in practice. We present ...
  </details>

- **2026-10-04** — Jinghao Pang, Jitai Hao, Qiang Huang et al. — [Beyond Refusal Patterns: Safe-Role Internalization for Robust and Generalizable LLM Safety Alignment](http://arxiv.org/abs/2610.07023v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable capabilities but remain vulnerable to jailbreak attacks that elicit harmful or unsafe outputs. Existing safety alignment approaches, including Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF), often require substantial attack-specific supervision and computational resources, while remaining susceptible to shallow safety alignment and over-refusal. To address these challenges, we introduce SSRFT(Supervised Saf...
  </details>

- **2026-10-04** — Swadesh Swain, Sanghamitra Dutta — [Don't Judge an LLM Only by Its Activations: Discovering Suppressed Safety Features via Counterfactual Activation Potential](http://arxiv.org/abs/2610.05541v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has emerged as the primary means to understand safety behavior of LLMs. However, existing tools primarily focus on the activating neurons or features of a model. The role of the remaining large set of inactive components is invisible to such methods. This work demonstrates that the inactive set contains safety-critical features that are causally relevant for refusal of harmful prompts. Suppressing such features could turn refusals into compliance, while passing undet...
  </details>

- **2026-10-04** — Tongyan Hu, Hao Li, Xiaogeng Liu et al. — [Red-TTT: Test-Time Training for Automated Jailbreaking Large Language Models](http://arxiv.org/abs/2610.05282v1)
  <details><summary>📄 Abstract</summary>
  Large language models remain vulnerable to jailbreaks, and automated red teaming is the standard way to find jailbreaks in large language models at scale. Current methods either draw more samples at test time through search, rewriting, and tree expansion, or train a stronger attacker offline with reinforcement learning. Both share a limitation: once an attack on a specific target behavior begins, the attacker's weights are frozen. Any signal it gathers about the behavior stays in its context win...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 12 papers

- **2026-10-06** — Sarim Hashmi, Mukul Ranjan, Kshitij Mishra et al. — [AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model](http://arxiv.org/abs/2610.08773v1)
  <details><summary>📄 Abstract</summary>
  Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a t...
  </details>

- **2026-10-06** — Niveen O. Jaffal, Ahmet Yuksel, David Mohaisen — [RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems](http://arxiv.org/abs/2610.08571v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 contextual examples across frozen train, validation, and protected-test splits. Using a leakage-aware construction pipeline and strict evaluation protocol, we compare keyword-based, semantic-reference, TF-IDF, and transformer-based detectors. DistilBERT achieves the best protected-tes...
  </details>

- **2026-10-06** — Haneen Najjar, Luca Scionis, Haritz Puerto et al. — [Surviving the Router: Optimizing Skill Injections for Retrieval and Execution](http://arxiv.org/abs/2610.08098v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume settings where the malicious skill is already selected for execution. We show that this assumption can substantially overestimate attack success. In realistic multi-skill environments, injected skills must first compete for retrieval, reducing ...
  </details>

- **2026-10-05** — Aniruddh Pramod, James Oldfield, Adel Bibi — [Towards a Unified Misuse Monitoring Benchmark](http://arxiv.org/abs/2610.07089v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly act in multi-actor environments, exposing them to misuse from multiple sources: decomposition attacks, where a harmful request is split into innocuous sub-requests, and prompt injection attacks, where a compromised tool delivers a malicious instruction. Existing evaluations treat these threats separately and ask whether a trajectory is harmful, rather than when it becomes harmful. We propose monitoring the agent's responses, where its actions are externalised, and ask whe...
  </details>

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


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-10-05** — Thomas Villeneuve, Alex Sandomirsky, Charles O'Neill et al. — [The Optimization Landscape of Learning Compacted Context Models](http://arxiv.org/abs/2610.05885v1)
  <details><summary>📄 Abstract</summary>
  Many works approach continual learning through the lens of infinite context windows. As an agent puts more observation into context (concretely the KV cache), compacting said context is akin to direct memory manipulation, without affecting the base model's weights. Many works pose KV compaction as an optimization problem: learn a smaller set of KV vectors that matches the behavior of the full KV cache. While this preserves base model behavior, optimizing through a frozen base model results in a ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-10-05** — Zunlong Zhou, Ziyuan Yang, Mengyu Sun et al. — [Runaway Reaction: When Benign Skills Compose into Malicious Behavior](http://arxiv.org/abs/2610.05943v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent's capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign sk...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 8 papers

- **2026-10-06** — Christophe Muller, Ayub Kharel, Alex Luedtke et al. — [ProximalFM: Amortized Proximal Causal Inference under Hidden Confounding](http://arxiv.org/abs/2610.08078v1)
  <details><summary>📄 Abstract</summary>
  Standard causal identification methods often assume no unmeasured confounding and can fail when relevant confounders are unobserved. Proximal causal inference instead uses proxy variables to identify effects under hidden confounding. However, nonparametric proximal estimation can be challenging in practice: recovering causal estimands such as the conditional average treatment effect (CATE) requires solving an ill-posed integral equation that is data-hungry, hyperparameter-sensitive, and optimiza...
  </details>

- **2026-10-06** — Yibo Zhang, Tianrong Guan, Liang Lin et al. — [The Model Plants the Trigger: Answer-Side Backdoor Attacks in Multi-Turn Large Language Models](http://arxiv.org/abs/2610.07723v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in Large Language Models (LLMs) remains vulnerable to backdoor attacks. Existing LLM backdoors are almost all input-centric: activation depends on explicit trigger patterns in the user input, so modern guardrails are built to sanitize the input space. We challenge this assumption with a novel answer-side backdoor for multi-turn dialogue. Instead of inserting the trigger into the input, the adversary uses a benign first-turn prompt to naturally induce the model to generate a spec...
  </details>

- **2026-10-06** — Jian Luo, Kehan Qi, Qingqiao Hu et al. — [Does On-Policy Distillation for Safety Pose Backdoor Risks?](http://arxiv.org/abs/2610.07654v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has attracted growing attention as an effective way to transfer capabilities from teacher models to student models. Recent studies further explore OPD as a tool for improving large language model safety with promising results. However, these approaches typically assume that the teacher and training data are trustworthy. In this paper, we uncover an overlooked threat to OPD for safety: a safety-aligned but backdoored teacher can propagate its hidden malicious behavior...
  </details>

- **2026-10-06** — Lizhi Zhang, Xin He, Dianxuan Fu et al. — [SkillPoison: Progressive Skill Poisoning via Successful Experiences](http://arxiv.org/abs/2610.07645v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM agents increasingly distill successful experiences into persistent, reusable skills. Existing skill attack methods corrupt this learning pipeline by injecting malicious triggers, behaviors, or false facts into individual experiences or extracted skills. However, such attacks are easily detected, and the injected malicious behaviors often fail to accumulate as persistent skills. In this paper, we show that skill poisoning can arise even from verified successful experiences, wit...
  </details>

- **2026-10-05** — Qiusi Zhan, Nian Lyu, Stephanie Ding et al. — [Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training](http://arxiv.org/abs/2610.07510v1)
  <details><summary>📄 Abstract</summary>
  Developers can build LLM agents by adapting third-party models through benign post-training. We study a supply-chain threat in which an attacker supplies a model with a backdoor: hidden behavior that produces malicious outputs when a particular input pattern appears. Focusing on software-engineering agents, we ask whether such backdoors survive the developer's supervised fine-tuning (SFT) and subsequent task-level reinforcement learning (RL). We observe that benign SFT substantially reduces atta...
  </details>

- **2026-10-05** — Krishna Kabra, Constantin Venhoff, Christian Schroeder de Witt — [Weight Oracles: Reading Neural Network Weights with Language Models](http://arxiv.org/abs/2610.07334v1)
  <details><summary>📄 Abstract</summary>
  Interpretability methods for neural networks are predominantly reactive: they analyse activations produced during specific forward passes, requiring known inputs to find hidden capabilities such as backdoors. We propose Weight Oracles, fine-tuned language models that diagnose properties of a target network by reading its raw weights directly, without behavioural testing. We investigate this paradigm in two phases. Phase I establishes feasibility: through a staged curriculum and an external chain...
  </details>

- **2026-10-05** — Enrico Ahlers, Daniel Passon, Tobias Kiecker et al. — [Backdooring Sparse Autoencoders](http://arxiv.org/abs/2610.06049v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are increasingly used not only to interpret language models but also to intervene on their internal representations. We show that this creates a supply-chain attack surface: a maliciously modified SAE can induce attacker-chosen behavior when inserted into the forward pass of an otherwise unchanged language model. We introduce a decoder-only SAE backdoor that leaves both the underlying LLM and the SAE encoder frozen, restricting the attack to a single auxiliary componen...
  </details>

- **2026-10-05** — Keegan Wang, Anantika Mannby — [Topology-Conditioned Backdoors: Language Models That Insert Vulnerabilities When They Infer They Are in a Multi-Agent System](http://arxiv.org/abs/2610.05793v1)
  <details><summary>📄 Abstract</summary>
  A language model may behave safely in a single-agent evaluation yet produce vulnerable code when its context suggests that it is part of a multi-agent system. We study this failure mode by fine-tuning Qwen2.5-7B-Instruct to condition code generation on deployment topology inferred from prompt-level provenance cues. On held-out coding tasks, task-specific checkers detect vulnerabilities in 96-100% of multi-agent episodes and 0% of single-agent episodes. An independent bandit analyzer detects vuln...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 9 papers

- **2026-10-06** — Maedeh Fallahreyhani, Paeiz Azmi, Nader Mokari et al. — [TwinViT-DeepJSCC: Adversarially Robust Semantic Image Communication](http://arxiv.org/abs/2610.08590v1)
  <details><summary>📄 Abstract</summary>
  Learning-based semantic communication is vulnerable to adversarial perturbations introduced before semantic encoding or over wireless channels. This paper proposes TwinViT-DeepJSCC, a preventive-corrective semantic image transceiver operating under a fixed channel-use budget. Two Vision Transformer (ViT)-based deep joint source-channel coding (DeepJSCC) branches learn complementary latent representations protected by sensitivity-aware masking. At the receiver, confidence-aware fusion, blind corr...
  </details>

- **2026-10-06** — Heyam Bin Jahlan Areej Alhothali Abeer Alhothali — [Transferable Spatial Temporal Coherence Adversarial Attack on Black-Box Vision Language Models for Autonomous Driving](http://arxiv.org/abs/2610.08331v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of Vision Language Models (VLMs) into sensitive systems introduces critical safety vulnerabilities that remain unexplored in exist studies. While adversarial attack robustness has been extensively studied for image-based models, the susceptibility of VLMs to temporally-aware adversarial attacks against video in driving context poses a distinct and under examined threat. In this paper, we introduce novel adversarial attack against video targeting VLM models used for autonomo...
  </details>

- **2026-10-06** — Soichiro Kumano — [Adversarially Trained Linear Transformers Are Optimal Robust In-Context Learners for Gaussian Mixtures](http://arxiv.org/abs/2610.07754v1)
  <details><summary>📄 Abstract</summary>
  Adversarial training is one of the most reliable defenses against adversarial attacks, but its high computational cost must generally be paid anew for each task. Robust foundation models offer a promising alternative: adversarially pretrain a model once and then transfer its robustness to downstream tasks through lightweight adaptation. However, a fundamental question remains open: can robustness acquired during pretraining transfer to unseen tasks without further adversarial training? In this s...
  </details>

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


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 36 papers

- **2026-10-06** — Halil İbrahim Kanpak, Sinem Sav, Alptekin Küpçü — [HE-OFT: Privacy-Preserving One-Shot Federated Fine-Tuning under Homomorphic Encryption](http://arxiv.org/abs/2610.08255v1)
  <details><summary>📄 Abstract</summary>
  Many organizations adapt large pretrained models to their own tasks by fine-tuning on private data. Several of these parties often hold data for the same task and wish to fine-tune a model together without pooling that data. Federated learning (FL) enables joint fine-tuning, but reconstruction attacks on shared intermediate values (the model or its gradients) remain a privacy risk. A one-shot protocol that exchanges one encrypted contribution exposes no intermediate value. Such a protocol still ...
  </details>

- **2026-10-06** — Kartick Sutradhar, Ranjitha Venkatesh — [Systematically Optimized CNN-Transformer with Focal Loss for Imbalanced Intrusion Detection on NSL-KDD](http://arxiv.org/abs/2610.08066v1)
  <details><summary>📄 Abstract</summary>
  Intrusion Detection Systems (IDS) struggle with imbalanced datasets like NSL-KDD, especially in detecting rare R2L and U2R attacks. This work describes a systematically optimized and explainable framework using a CNN-Transformer architecture to improve performance on highly imbalanced data. We decided to use XGBoost for feature selection and Focal Loss as the main mechanism for minority class learning. We used Optuna for end-to-end hyrate=0.00042, batch size=256, and Focal Loss γ), using a thoug...
  </details>

- **2026-10-06** — Nikolaos Kekatos, Apostolos Valiakos, Alexios Lekidis et al. — [Quantifying the Privacy Posture of Operator-Side 5G/O-RAN Profiles](http://arxiv.org/abs/2610.07976v1)
  <details><summary>📄 Abstract</summary>
  Operator-side network profiles derived from 5G/ORAN traffic carry personal data such as ephemeral subscriber identifiers, slice-level KPIs, and control-plane signalling, and must be anonymised before release to a federated-learning aggregator, threat-intelligence exchange, or ML training pipeline. We study how much re-identification risk remains after standard operator-side anonymisation. We quantify privacy posture with k-anonymity, l-diversity and t-closeness, aggregate them into a composite P...
  </details>

- **2026-10-06** — Muhammad Saif ul Islam, Karar Haider, Manaal Malik et al. — [Zeppelin: Client-Side BFV Encryption and Decryption for Helium-Powered Microcontrollers](http://arxiv.org/abs/2610.08301v1)
  <details><summary>📄 Abstract</summary>
  The growth of the Internet of Things (IoT) has raised concerns over the privacy of data collected by resource-constrained sensing devices. Homomorphic encryption (HE) addresses this by letting a device encrypt its data once and an untrusted cloud server compute on the ciphertext without seeing the values. In practice, HE's memory and computational cost have kept it out of reach of microcontroller-class devices. Prior work, SEAL-Embedded, made this feasible using CKKS, but left three gaps: its ar...
  </details>

- **2026-10-06** — Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen et al. — [WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses](http://arxiv.org/abs/2610.08526v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remains largely unexplored, hindered by the lack of benchmarks that jointly provide continuous low-level flight actions, fine-grained natural-language target descriptions, and realistic industrial environments. This paper introduces WareFly-VLA, a photorealistic UAV VLA framework and data...
  </details>

- **2026-10-06** — Zhen Yu, Wenyang Liu, Kejun Wu et al. — [Image Bitstream Fine-grained Understanding for Privacy-Friendly AIoT](http://arxiv.org/abs/2610.08414v1)
  <details><summary>📄 Abstract</summary>
  Image Bitstream Fine-grained Understanding (IBFU) aims to directly perform fine-grained classification and semantic description generation from encoded image byte sequences. In contrast to conventional pixel-domain visual understanding, IBFU conducts semantic analysis without fully decoding images into the pixel domain. Since pixel-level visual content is not explicitly reconstructed during inference, this paradigm reduces visual exposure within the processing pipeline and suits privacy-friendly...
  </details>

- **2026-10-06** — Tobias Hallmen, Fabian Deuser, Robin-Nico Kampa et al. — [The Failure Is in the Readout: Fine-Grained Emotion Recognition Benchmarks Measure Elicitation, Not Perception](http://arxiv.org/abs/2610.08162v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained emotion recognition supports therapy tools and social robots, but it needs facial data, which raises privacy and data-protection concerns. EmoNet-Face-HQ answers that with generated portraits, expert-rated over a $40$-category taxonomy far finer than the usual six to eight basic emotions. Under the protocol it ships with, vision-language models (VLMs) score poorly on that taxonomy, and the benchmark concludes that a dedicated fine-tuned model is necessary: Empathic-Insight-Face (EIF...
  </details>

- **2026-10-06** — János Kertész, Marc Barthelemny, Guido Caldarelli et al. — [Social Physics: A manifesto](http://arxiv.org/abs/2610.08117v1)
  <details><summary>📄 Abstract</summary>
  Social Physics seeks quantitative, empirically testable explanations of collective human behavior. Its name has a long and contested history, but its contemporary program is neither the claim that society is literally a physical system nor an attempt to replace the social sciences with physics. It is an interdisciplinary practice: observation and experimentation, model construction, mathematical and computational analysis, and repeated confrontation with data. The field has been transformed by a...
  </details>

- **2026-10-06** — Chuan Li, Chengyu Wang, Cen Chen et al. — [SAGE: Semantic Anchor-Guided Evolution for Grounded Medical QA Data Synthesis](http://arxiv.org/abs/2610.08093v1)
  <details><summary>📄 Abstract</summary>
  Developing reliable models for clinical tasks, such as Medical Question Answering (QA), is severely constrained by the limited availability of high-quality, expert-annotated training data. This challenge is exacerbated by stringent privacy requirements and the impracticality of utilizing large open-source corpora or proprietary cloud APIs within resource-limited clinical settings. To address these obstacles, we introduce SAGE (\textit{Semantic Anchor-Guided Evolution}), a novel data synthesis fr...
  </details>

- **2026-10-06** — Aksel Fristrup, Sumit Pandey, Ankit Kariryaa — [ApexQuant: Data-Free Elastic Quantization by Residual Re-Isotropization](http://arxiv.org/abs/2610.07904v1)
  <details><summary>📄 Abstract</summary>
  We introduce ApexQuant, a calibration-free quantization method that recursively re-quantizes the residual error, serving as a refinement layer on top of existing quantizers. We establish that a fresh random rotation returns each residual to the uniform distribution on the hypersphere, which characterizes the rate of progressive error decay across successive passes. This result lets us determine, before any weight is read, how many passes a layer needs for a target weight-space error. Every prefi...
  </details>

- **2026-10-06** — Sushmita Khan, Connor Pennington, Bart P Knijnenburg — [A Pedagogically Demonstrative Model Visualizing the Pathway from Online Interactions to Personalized Recommendation](http://arxiv.org/abs/2610.07744v1)
  <details><summary>📄 Abstract</summary>
  Personal digital activity increasingly shapes online experiences, yet few users have been educated regarding the processes transforming raw interactions into personalized suggestions. We developed an education artifact that illustratively simulates how AI leverages users' digital activities to shape online recommendations (e.g., ads). Our artifact processes users' digital activity using a locally-hosted LLM to generate user profiles of their inferred interests and personalized recommendations. A...
  </details>

- **2026-10-06** — Peihua Mai, Zhuoyan Shao, Xinbao Qiao et al. — [Illusory Pattern Perception Drives Spurious Inference in Large Language Models](http://arxiv.org/abs/2610.07791v1)
  <details><summary>📄 Abstract</summary>
  Illusory pattern perception is a well-documented human cognitive tendency to infer meaningful relationships in data that is actually random. Such a tendency, often described as "connecting the dots" where none exist, can result in systematic reasoning errors. This paper investigates whether Large Language Models (LLMs) exhibit such perceptual tendencies, which can lead to systematic errors in downstream applications. To our knowledge, this work presents the first systematic study of illusory pat...
  </details>

- **2026-10-05** — Venkata M Sangaraju, Sudhir Vissa — [Lineage-Aware Memory Governance: A Derivation-Gated Framework for Privacy-Preserving Column-Level Access Control in Enterprise AI Agents](http://arxiv.org/abs/2610.07258v1)
  <details><summary>📄 Abstract</summary>
  Enterprise AI agents that share a memory store face two unaddressed risks: sensitive data can leak through legitimately computed results the requester could not derive, and departments can silently compute a same-named key performance indicator (KPI) through conflicting logic. Existing agent-memory systems (e.g., MemGPT, Zep, A-MEM) gate retrieval by content, ownership, and role, not derivation, missing a cached insight that embeds a forbidden column. We introduce the Analytical Memory Unit (AMU...
  </details>

- **2026-10-05** — Chih-Yuan Chiu, Matthew Hale — [The Cost of Differential Privacy in Linear-Quadratic Dynamic Games](http://arxiv.org/abs/2610.07238v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent coordination often requires strategic agents to share sensitive information about their states or objectives, creating a tension between performance and privacy. Our paper studies this tradeoff in stochastic linear-quadratic (LQ) dynamic games with heterogeneous agent objectives. In our framework, agents share noise-perturbed state and reference information with a cloud computer that computes feedback Nash equilibrium strategies, with the injected noise calibrated to provide differen...
  </details>

- **2026-10-05** — Berke Arda, Ahmetcan Yavuz, Paul Gerry et al. — [CroissantMiner: Automated Extraction and Validation of Croissant Metadata for ML Datasets](http://arxiv.org/abs/2610.07132v1)
  <details><summary>📄 Abstract</summary>
  Croissant has emerged as a standard for machine-readable dataset metadata, yet populating its fields remains labor-intensive and requires careful reading of accompanying dataset documentation. We present the first benchmark enabling end-to-end evaluation of metadata extraction aligned with a community-standard schema. The benchmark comprises 602 papers, including 102 with human-validated gold annotations and 500 with LLM-generated silver annotations, covering the full Croissant schema with both ...
  </details>

- **2026-10-05** — Dongryeol Lee, Weronika Łajewska, Leonardo Perelli et al. — [Data-Driven Personas for Survey Simulation: Insights into Simulation Alignment Across Data-Access Regimes](http://arxiv.org/abs/2610.05828v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer new opportunities for public opinion research by enabling early prediction of survey responses, potentially reducing the cost and time of traditional surveys. However, many existing steering approaches rely on target-domain human data for fine-tuning or prompting that is costly to collect and raises privacy concerns. In this paper, we study demographic group-level survey simulation, where personas induced from heterogeneous, anonymized public behavioral data co...
  </details>

- **2026-10-05** — Turhan Can Kargin, Piotr Kubaty, Ekaterina Rostovskaya et al. — [WildMatch: Weakly Supervised Image Matcher Adaptation for Wildlife Re-Identification](http://arxiv.org/abs/2610.07384v1)
  <details><summary>📄 Abstract</summary>
  Individual animal re-identification from camera-trap imagery is an instance retrieval problem central to non-invasive wildlife monitoring: a query image must retrieve the correct individual from a reference set of known animals. This requires computer vision models to recognize distinctive local patterns in fur, skin, or other visual markings. Current approaches either learn global embeddings as a classification problem, requiring many labeled images per individual while largely ignoring local e...
  </details>

- **2026-10-05** — Sumanyu Muku — [Verifying Coordination in Parallel Coding Agents: NP-Bench and a Scheduling Planner](http://arxiv.org/abs/2610.07261v1)
  <details><summary>📄 Abstract</summary>
  A team of coding agents can look fine agent by agent yet fail as a team: each passes its own tests while the merged result is broken, and single-agent evaluation never catches it. As teams run several LLM coding agents in parallel on one codebase, the agents collide: two rewrite the same function, one codes against a contract a teammate just changed, and integration fails after the work is done. Most coordination tools react (watch for a conflict, then warn), but at agent speed the warning arriv...
  </details>

- **2026-10-05** — Jiachen Zhao, Antonia Januszewicz, Taeho Jung — [Reward-Driven Learning under Prompt-Level Differential Privacy](http://arxiv.org/abs/2610.07212v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) trains a language model on problems that may themselves be confidential, and the trained model can reveal which problems it saw. We study RLVR under prompt-level differential privacy: the released weights must be (ε,δ)-differentially private with respect to the presence of any one training problem. Taking the group of responses to one prompt as the privacy record, our method aggregates their gradients, clips the prompt's contribution once, ad...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 16 papers

- **2026-10-06** — Yiming Xu, Hongyue Yu, Beihua Yang et al. — [DecepEval: A Benchmark for Evaluating Deception in LLM Agents](http://arxiv.org/abs/2610.07967v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a benchmark comprising 1,532 instances across 3 task families and 28 professional scena...
  </details>

- **2026-10-06** — Jingyu Zhang, Shruti Palaskar, Daniel Khashabi et al. — [SIGMA: Self-Improving Alignment Generalization from a Model Spec](http://arxiv.org/abs/2610.07935v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly capable of executing complex tasks and of recursively improving themselves on easy-to-verify objectives such as software engineering and mathematics. Since alignment is much harder to verify, this creates a growing risk of capabilities increasing without appropriate safety alignment, especially as capabilities expand to auto-research and cybersecurity. Existing approaches focus on capability self-improvement using verifiable feedback or on alignment training with supe...
  </details>

- **2026-10-06** — Ziyuan Yang, Wenxuan Ding, Shangbin Feng et al. — [Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models](http://arxiv.org/abs/2610.07774v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) face compositional safety risks where harmful intent emerges from the interaction between visual and textual inputs. As mixture-of-experts (MoE) VLMs become increasingly common, recent work has explored various safety interventions, including prompting, supervised fine-tuning, and routing-based expert steering. However, these methods show inconsistent improvements across models and evaluation distributions, and the intervention into model behavior or internal states...
  </details>

- **2026-10-06** — Egor Pakhomov, Erik Nijkamp — [Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus](http://arxiv.org/abs/2610.08722v1)
  <details><summary>📄 Abstract</summary>
  Many long-horizon agents compact their context on a global rule, usually a token budget, blind to what the agent was doing. We ask whether the agent's recent behaviour predicts when a compaction will hurt. TRACE's public corpus of 590 harness-triggered AppWorld compaction boundaries replays each boundary from a re-executed prefix state under the pre-compaction context and under the summary, and records the burden of the next actions: calls that error or repeat a call already made. We find that p...
  </details>

- **2026-10-06** — Yu Xia, Jiangfan Zhang, Jun Xiao et al. — [Personal-Agent Mediated Recommendation with Cross-Platform User History](http://arxiv.org/abs/2610.07588v1)
  <details><summary>📄 Abstract</summary>
  Modern recommendation is shifting from platform-centric personalization toward user-governed personalization, where a personal LLM agent can act on the user's behalf across services. We formalize this emerging paradigm as Personal-Agent Mediated Recommendation: a platform recommender ranks a candidate set using platform-local information, and a personal agent uses user-authorized cross-platform history to mediate the resulting ranking and produce the final top-K slate. Such mediation is nontrivi...
  </details>

- **2026-10-05** — Ziqun Bao, Xinyu Zhang, Yuchen Shao et al. — [Harmful SFT Leaves a Continuous Trace in LLM Checkpoint Updates](http://arxiv.org/abs/2610.07518v1)
  <details><summary>📄 Abstract</summary>
  Safety auditing of post-trained large language models typically relies on model behavior, requiring model execution and depending on the coverage of available evaluations. This work asks a different question: Do the target behaviors optimized during supervised fine-tuning (SFT) leave readable evidence directly in checkpoint updates? We find that harmful-compliance SFT induces a continuous, objective-dependent ordering in checkpoint-update space. Using a reference geometry defined by pure harmful...
  </details>

- **2026-10-05** — Eugene Zhang, Cheng-Yun King Yang, Dongyan Xu — [Efficient Auditing of Adversarial AI Agent Behavior from Agent Traces](http://arxiv.org/abs/2610.07256v1)
  <details><summary>📄 Abstract</summary>
  AI agents powered by large language models (LLMs) can perform complex tasks but may harm the systems they operate in, either intentionally or unintentionally. Existing agent monitoring approaches rely on rule-based guardrails or LLM-based trace auditing. However, rule-based guardrails can be bypassed through obfuscation and may miss harmful actions beyond their predefined rules, whereas applying an LLM to audit every action is costly. We present a two-stage agent trace auditing framework. The fi...
  </details>

- **2026-10-05** — Saviz Changizi, Nasibeh Mohammadzadeh, Mohammad Shojafar et al. — [When Does AI Supervision Help? A Role-Aware Study of Network Fraud Decision Management with Blockchain Auditability](http://arxiv.org/abs/2610.07434v1)
  <details><summary>📄 Abstract</summary>
  When does a second artificial intelligence (AI) component improve a primary network-fraud decision rather than add operational burden? We study this question through a role-aware Decider-Supervisor (DS) framework with blockchain auditability, evaluating four directional configurations that combine centralised machine learning, a Federated Averaging (FedAvg)-trained federated meta-model, and Base or Quantized Low-Rank Adaptation (QLoRA) large language model variants. The analysis compares primary...
  </details>

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


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 70 papers

- **2026-10-06** — Shangye Song, Dong Gong, Hong Jia et al. — [CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching](http://arxiv.org/abs/2610.08777v1)
  <details><summary>📄 Abstract</summary>
  Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explici...
  </details>

- **2026-10-06** — Habibur Rahaman, Swastik Bhattacharya, Sanjay Das et al. — [BARE-AI: Bit-Flip Attack Resilience in AI Hardware through Built-in Performance Monitors](http://arxiv.org/abs/2610.08739v1)
  <details><summary>📄 Abstract</summary>
  Deep Neural Networks (DNNs) are integral to many safety critical systems, yet they remain highly vulnerable to bit-flip attacks (BFAs), where a few memory level perturbations can drastically degrade accuracy. Existing defenses incur significant hardware overhead, depend on retraining, or fail against targeted flips. We propose BARE-AI, a runtime framework that detects, localizes, and mitigates BFAs during inference. BARE-AI introduces AI Performance Counters (APCs), lightweight hardware monitors...
  </details>

- **2026-10-06** — Jiahua Li, Zixu John, Tom Zhong et al. — [Forensic Reserve: Eliciting Latent Knowledge for Image Forgery Detection](http://arxiv.org/abs/2610.08639v1)
  <details><summary>📄 Abstract</summary>
  As generated images become increasingly realistic, reliable forgery detection is essential for maintaining trust in visual information. However, existing methods primarily rely on task-specific supervision to adapt vision foundation model representations, without fully exploiting internal forensic knowledge to guide detection. To address this limitation, we propose Reserve-Guided Elicitation (RGE), a framework that treats sparse, origin-sensitive internal components in pretrained models as a for...
  </details>

- **2026-10-06** — Songlin Jiang, Zhiyu Li, Terry Kong et al. — [NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale](http://arxiv.org/abs/2610.08430v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) disaggregates training from rollout, so each policy update must reach the rollout clusters before the next batch. Transferring a full 1T checkpoint for such weight synchronization (refit) takes 87.5 min between two AWS regions. Measurements of BF16 training show that about 1% of weights change their stored values per step. Recent systems exploit this sparsity but fall short on placement, exactness, or efficiency: they reimplement placement rules, assemble full...
  </details>

- **2026-10-06** — Hao Sun, Yibin Yao, Chaohai Xie et al. — [Case-Level Verification in Scanner-LLM Cascades: Overcoming the Alert Aggregation Bottleneck to Expand the FRR-TPR Trade-off Space](http://arxiv.org/abs/2610.08406v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Application Security Testing (DAST) scanners achieve high recall but also produce a large number of false positives, resulting in substantial manual triage costs. Large Language Models (LLMs), when used for independent detection, achieve extremely high recall (95.4%-100%) but also exhibit prohibitively high false positive rates (49.6%-85.0%), precluding their use as standalone replacements for scanners. A natural solution is a two-stage cascade consisting of scanner detection followed by...
  </details>

- **2026-10-06** — Mandana Ghadamian, David Mohaisen — [Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis](http://arxiv.org/abs/2610.08405v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have emerged as promising tools for software vulnerability analysis, but their effectiveness depends heavily on prompt design. Existing research primarily compares prompting strategies using aggregate performance metrics, providing limited insight into why models fail or how prompts can be improved systematically. We propose Failure-Driven Prompt Refinement (FDPR), a methodology that analyzes recurring model failures to guide evidence-based prompt refinement. Using the Damn...
  </details>

- **2026-10-06** — Adeline Pittet, Shien Zhu, Valérie Verdan et al. — [SSR: Sparse Segment Reduction for Ternary GEMM Acceleration](http://arxiv.org/abs/2610.08403v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware. Ternary LLMs mitigate these demands through weight quantization via ternary values, achieving significant compression often with 50-90% sparsity. However, existing approaches have limitations: methods optimized for ternary weights, such as BitNet, redundant segment reduction (RSR), and its improved version RSR++, do not exploit sparsity structures, while conventio...
  </details>

- **2026-10-06** — Yubo Song, Subham Sahoo, Freja Basse — [Infrastructure-Native Computing with Electric Power Grids](http://arxiv.org/abs/2610.08390v1)
  <details><summary>📄 Abstract</summary>
  Computing is conventionally implemented by hardware engineered for information processing. Here we investigate infrastructure-native computing: the use of a physical system built for another primary function as a fixed computational operator. In time-domain simulations of an IEEE 14-bus electrical network, Kirchhoff's current law and Ohm's law relate voltage-reference perturbations applied at distributed controllable nodes interfaced by power electronics converters to current responses through a...
  </details>

- **2026-10-06** — Shuo Yang, Changbai Li, Linlin Yang et al. — [DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models](http://arxiv.org/abs/2610.08341v1)
  <details><summary>📄 Abstract</summary>
  Recent training-free pruning approaches for Multimodal Large Language Models (MLLMs) effectively cut computational overhead by exploiting visual redundancy or text-vision attention. However, they frequently suffer from semantic degradation due to their task-agnostic design or unreliable attention estimates. Based on our empirical analysis, we have found that this issue arises because salient tokens in shallow layers persistently suppress emerging semantic ones through numerical inertia, leading ...
  </details>

- **2026-10-06** — Jianyong Hu, Wei Li — [Measurement Complexity of Quantum Compressed Sensing](http://arxiv.org/abs/2610.08234v1)
  <details><summary>📄 Abstract</summary>
  Conventional compressed sensing (CS) has a measurement lower bound of M = Ω(K log(N/K)) under non-adaptive measurements. Recent experiments on quantum compressed sensing (QCS) have reported numbers of measurements below this classical lower bound. In this work, we establish lower bounds on the measurement complexity of QCS from an information-theoretic and quantum-physical perspective. QCS exploits quantum parallelism, enabling a unitary domain-alignment evolution to act on a superposition of al...
  </details>

- **2026-10-06** — Haotian Chen, Shuaicheng Niu, Haocong Rao et al. — [Test-Time Agent Evolution for Long-Horizon Legal Reasoning](http://arxiv.org/abs/2610.08138v1)
  <details><summary>📄 Abstract</summary>
  Legal intelligence aims to support reliable decision-making across long-horizon legal processes involving evolving case states and multiple roles. However, real-world legal deployment exhibits substantial case heterogeneity in facts, evidence, and procedural contexts, exposing the limitations of static agent strategies. Moreover, legal reasoning is inherently interdependent across roles and procedural stages, making global reliability fundamentally different from isolated role competence. To add...
  </details>

- **2026-10-06** — Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi et al. — [Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight](http://arxiv.org/abs/2610.08077v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can hindsight teach an agent what it could have anticipated before acting? We introduce p...
  </details>

- **2026-10-06** — Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike et al. — [SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning](http://arxiv.org/abs/2610.08076v1)
  <details><summary>📄 Abstract</summary>
  Frontier LLM agents have been shown to be capable of solving increasingly complex tasks for which humans have measurable solutions. This begs the pertinent question of whether LLM agents can go beyond what humans have already solved. The ability to develop sophisticated strategies to tackle consequential problems becomes paramount as well-trodden, human-developed solutions become insufficient for problems for which we lack context or enough training data. We study agents' capability of such stra...
  </details>

- **2026-10-06** — Jordy Kieto — [Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA](http://arxiv.org/abs/2610.08033v1)
  <details><summary>📄 Abstract</summary>
  World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look. We judge one from the outside. We learn a structured, multi-agent world model of a complete ten-hero MOBA (206 units, every hero acting every tick, games of up to 6,000 ticks), train a policy only inside it with 1,400-tick free-running imagined episodes, and measure that policy in the real game against the opponent the game ships with. The real...
  </details>

- **2026-10-06** — Chengzhi Ye, Ruoyu Zhang, Lipeng Zhu et al. — [Movable Antenna-Enabled Multi-Target Sensing: Sidelobe Suppression via Position Optimization](http://arxiv.org/abs/2610.08008v1)
  <details><summary>📄 Abstract</summary>
  Movable antenna (MA) has emerged as a promising technology to unlock spatial degrees of freedom for wireless sensing systems. However, optimizing MA positions for multi-target sensing remains challenging due to the complicated coupling between the array geometry and unknown target directions, as well as severe sidelobe interference. In this paper, we propose an MA-enabled multi-target wireless sensing scheme to achieve both high-precision and robust target parameter estimation. To characterize t...
  </details>

- **2026-10-06** — Georgios Koutidis, Nikolaos Kekatos, Marina Korgiala-Karyda et al. — [Preparing an AI-Augmented SIEM for the EU Cyber Resilience Act: A Practitioner Case Study](http://arxiv.org/abs/2610.07873v1)
  <details><summary>📄 Abstract</summary>
  The EU Cyber Resilience Act (CRA), Regulation (EU) 2024/2847, makes product cybersecurity a lifecycle obligation for products with digital elements on the EU market: risk assessment, vulnerability handling, conformity documentation, and Article 14 incident- and vulnerability-reporting readiness must be operational before market placement. Small and medium-sized enterprises that build security products are doubly exposed, since their products are in scope while their customers expect them to be e...
  </details>

- **2026-10-06** — Muhammad Asim Javaid, Muhammad Adeel Pasha, Muhammad Ali Siddiqi — [Efficient and Implementation-Hardened RBLWE on Commodity Cortex-M Microcontrollers](http://arxiv.org/abs/2610.07820v1)
  <details><summary>📄 Abstract</summary>
  Efficient post-quantum cryptography on resource-constrained Internet-of-Things (IoT) devices requires implementations that exploit the target processor architecture while resisting practical implementation attacks. This paper presents an ISA-accelerated and implementation-hardened realization of Ring Binary Learning with Errors (RBLWE) encryption on a commodity ARM Cortex-M33 microcontroller. Packing four 8-bit polynomial coefficients into the byte lanes of a 32-bit register and processing them ...
  </details>

- **2026-10-06** — Yunhui Liu, Xudong Jin, Kang Zhang et al. — [Towards One-for-All Foundation Model for Attributed Graph Clustering](http://arxiv.org/abs/2610.07778v1)
  <details><summary>📄 Abstract</summary>
  Attributed graph clustering aims to discover node groups by jointly exploiting node attributes and graph topology, yet its unsupervised nature makes model selection and adaptation inherently difficult. Existing methods typically train and tune a separate model for each input graph, leading to costly and fragile pipelines that often fail to transfer across graphs with different feature spaces, structural patterns, and attribute-structure correlations. In this paper, we study a one-for-all alterna...
  </details>

- **2026-10-06** — Bach Nguyen, Zhaonan Li, Mau Son Nguyen et al. — [How Well Do LLMs Reason with Noisy Evidence? An Active Visual Reasoning Benchmark](http://arxiv.org/abs/2610.07751v1)
  <details><summary>📄 Abstract</summary>
  Real-world reasoning rarely reduces to static question answering: agents must actively gather information from tools and sensors that are often noisy and unreliable. Yet most existing active reasoning benchmarks assume that environmental feedback is trustworthy, or introduce noise without exposing an explicit, calibrated uncertainty signal, leaving open how LLMs should reason when the evidence itself is uncertain. We introduce VisualNoiseQA, a novel benchmark for active reasoning under noisy vis...
  </details>

- **2026-10-06** — Chuanfei Zang, Yumiao Wang, Xingyu Chen et al. — [Radar Intelligent Detection with Coarse-Grained Labels](http://arxiv.org/abs/2610.07670v1)
  <details><summary>📄 Abstract</summary>
  Many deep learning based radar target detectors rely on range-cell level labels for training, which are expensive to obtain. To reduce the labeling burden, this paper presents a training strategy that uses only range-window level labels. Specifically, two sub-echoes are randomly cropped from the same window echo, resulting in a known relative shift between them. A siamese Transformer is then used to identify target-salient responses from one sub-echo and form pseudo labels, which are mapped to t...
  </details>

- **2026-10-06** — Zhengyang Zhu, Liming Huang, Runmin Ji et al. — [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](http://arxiv.org/abs/2610.07639v1)
  <details><summary>📄 Abstract</summary>
  Coding agent harnesses mediate tool use and authorize actions, yet their security mechanisms and runtime effects remain incompletely characterized. We present HarnessSecurity, the first systematic empirical study and benchmark of open- and closed-source coding agent harnesses. First, we derive a ten-mechanism taxonomy and then assess 400 harness-mechanism cells using independent ratings by researchers and large language model (LLM) judges. We find that about half of confirmed mechanism implement...
  </details>

- **2026-10-06** — Hang He, Li Wang, Hao Chen et al. — [CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?](http://arxiv.org/abs/2610.07557v1)
  <details><summary>📄 Abstract</summary>
  Static-analysis checker synthesis requires agents to interpret a defect specification, inspect a repository, implement analyzer-specific logic, and refine the checker through repeated compilation and analysis feedback. Existing coding-agent benchmarks focus on tasks such as patch generation or vulnerability detection and rarely assess whether an agent can develop a working checker in a repository from start to finish. We introduce CheckerBench, an executable benchmark of 300 tasks derived from 2...
  </details>

- **2026-10-06** — Hongyu Cao, Yanchi Liu, Kunpeng Liu et al. — [Which and When to Admit: Gradient Admission for Data-Centric Small Language Model Finetuning](http://arxiv.org/abs/2610.07553v1)
  <details><summary>📄 Abstract</summary>
  LoRA fine-tuning adapts small language models (SLMs) to heterogeneous instruction data within a low-rank update subspace, making it vulnerable to three structural problems: conflicting gradients that cancel, static data selection that cannot track evolving learning dynamics, and subspace saturation that causes later updates to overwrite useful directions. We argue that effective adaptation therefore requires controlling which data-induced gradients enter the LoRA subspace and when. We propose GR...
  </details>

- **2026-10-05** — Shashwat Khandelwal, Shanker Shreejith — [Deep Defence on Wheels: A Dual Intrusion Detection System Architecture for Comprehensive In-Vehicle Network Security](http://arxiv.org/abs/2610.07489v1)
  <details><summary>📄 Abstract</summary>
  Increasing connectivity to the outside world and the lack of inbuilt security mechanisms have made legacy intra-vehicular networks vulnerable to cyberattacks. Initial research focused on maximising detection accuracy for known and unknown attacks, often using large, full-precision machine learning models. However, embedding IDSs into vehicular electronic systems also requires low detection latency, energy efficiency and minimal electronic control unit (ECU) resource overhead to process about 2,0...
  </details>

- **2026-10-05** — Cong Guo, Chiyue Wei, Bowen Duan et al. — [A Shape-Adaptive Architecture with Disaggregated Quantization for Efficient LLM Serving](http://arxiv.org/abs/2610.07443v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become the backbone of modern AI applications, but pose significant challenges for efficient inference. Their autoregressive generation divides execution into two phases: prefill, dominated by large GEMMs, and decoding, dominated by small GEMVs. Modern serving systems further introduce complexity through continuous batching and prefill-decoding disaggregation, leading to dynamic workloads and phase separation. However, existing accelerators remain poorly aligned...
  </details>

- **2026-10-05** — Mohamed Abdelnaby, Kevin Leahy — [Entropy-Gated Belief Coordination for Decentralized Multi-Agent Search Under Intermittent Communication](http://arxiv.org/abs/2610.07432v1)
  <details><summary>📄 Abstract</summary>
  We study decentralized multi-agent target search where homogeneous agents communicate intermittently at Poisson-distributed times. Standard unconditional belief fusion wastes communication opportunities by synchronizing agents during high-entropy exploration, when diverse independent beliefs provide better coverage than a premature consensus. We introduce \emph{entropy-gated belief coordination}, in which agents skip fusion while their collective entropy ratio exceeds a threshold~\(θ\) and merge...
  </details>

- **2026-10-05** — Bryan C. Boots — [Simulating Strategies for Defense Against Brand-Targeted Online Disinformation](http://arxiv.org/abs/2610.07407v1)
  <details><summary>📄 Abstract</summary>
  Brand-targeted disinformation can damage firms not only by spreading false beliefs, but by eroding trust, amplifying reputational uncertainty, and persisting across networked digital environments. This paper models brand-targeted disinformation as a trust-weighted contagion process using a multi-agent simulation across six network structures, three amplification levels, and six intervention strategies. Results show that scale-free and influencer-heavy networks are most vulnerable to rapid spread...
  </details>

- **2026-10-05** — Olivier Guéant — [Convex Order Beyond Dimension One: Projection Tests, Counterexamples and Gaussian Mixtures](http://arxiv.org/abs/2610.07404v1)
  <details><summary>📄 Abstract</summary>
  In actuarial science and quantitative finance, convex order provides a natural way to compare risks with the same mean. In dimension one, convex order is well understood through several characterisations. In higher dimensions, a natural approach is to compare all one-dimensional projections, but, although necessary, the resulting condition is in general not sufficient for multivariate convex order. A simple counterexample due to Pinelis exploits Popoviciu's inequality. We revisit this example us...
  </details>

- **2026-10-05** — Zhuoyang Zou, Abolfazl Ansari, Jiaxi Yang et al. — [Who Wrote It Is Not Enough: Detecting Who Contributed the Insight](http://arxiv.org/abs/2610.07365v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly assist scientific writing and peer review, detecting who wrote the text is no longer sufficient: we need to determine who contributed the underlying insight. We introduce Insight Provenance, the task of identifying whether a review insight originates from a human, an LLM, or their hybrid contribution. We construct InsightProv-v0 from 4,057 scientific papers and 12,660 human reviews, simulating different levels of LLM involvement with GPT-4o, Gemini, and DeepSeek and annotati...
  </details>

- **2026-10-05** — Hoang Phan, Minh Pham, Chau Pham et al. — [Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding](http://arxiv.org/abs/2610.07342v1)
  <details><summary>📄 Abstract</summary>
  On-policy reinforcement learning has become a central paradigm for improving the reasoning abilities of large language models. However, its effectiveness is often limited by reward sparsity: when a model fails to discover correct trajectories for difficult problems, the optimization process receives little useful signal and may stagnate. Existing approaches mitigate this issue by incorporating off-policy demonstrations, expert traces, or model-generated solutions, but they typically require the ...
  </details>

- **2026-10-05** — Phillip Pramberger, Athanasios Tziouvaras, Shreejith Shanker et al. — [A Pipelined FPGA Architecture for Banded Sparse Matrix Dense Matrix Multiplication in Longformer](http://arxiv.org/abs/2610.07301v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention mechanisms have become increasingly important for transformer models processing long input sequences due to their lower computational and memory complexity compared to full self-attention. Longformer achieves this through a sliding-window attention mechanism that produces a structured banded sparse attention matrix. However, existing sparse transformer accelerators primarily target attention generation or unstructured sparsity, leaving sparse matrix--dense matrix multiplication ...
  </details>

- **2026-10-05** — Luoxi Tang, Yuqiao Meng, Ankita Patra et al. — [Polar: LLM-Powered Synthesis of Real-World Cyber Evidence for Prioritization and Mitigation](http://arxiv.org/abs/2610.07298v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat analysis increasingly depends on evidence distributed across vendor advisories, vulnerability databases, and threat intelligence sources. Turning these fragmented observations into timely decisions requires models to connect technical severity with evolving exploitation evidence and available defensive actions. We present POLAR, an LLM-powered framework for synthesizing real-world cyber evidence into threat-centric assessments for prioritization and mitigation. POLAR first disentang...
  </details>

- **2026-10-05** —  Abdullah, Awais Khan, Khalid Mahmood Malik — [Exposing and Mitigating Neural Codec Vulnerabilities in Audio Deepfake Detection](http://arxiv.org/abs/2610.07216v1)
  <details><summary>📄 Abstract</summary>
  Existing audio deepfake detection (ADD) datasets and detectors are primarily built for vocoder-based synthesis, evaluated against traditional post-hoc perturbations such as MP3/AAC compression or additive noise, applied independently of generation. However, recent speech synthesizers, particularly ALM-based systems, use neural audio codecs both for compression and as the resynthesis reconstructing waveforms from generated tokens, producing artifacts distinct from post-hoc compression. Neural cod...
  </details>

- **2026-10-05** — Zhi-Kai Chen, Song-Yan Li, De-Chuan Zhan et al. — [SchemaFill: Efficient LLM Tool Calling via Slot-Parallel Speculative Decoding](http://arxiv.org/abs/2610.07086v1)
  <details><summary>📄 Abstract</summary>
  LLM agents interact with external systems by generating structured tool calls. Given a user request, conversational context, and a catalog of tool schemas, a tool-calling model must select tools and generate their arguments, potentially producing multiple calls in a single response. Standard autoregressive decoding generates these calls token by token, incurring substantial latency for requests involving multiple calls or many argument fields. The explicit argument structure offers opportunities...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 53 papers

- **2026-10-06** — Suxin Ji, Hungtao Wan, Shaoxuan Chen et al. — [Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents](http://arxiv.org/abs/2610.08668v1)
  <details><summary>📄 Abstract</summary>
  Behavioral watermarking embeds an owner identifier in an LLM agent's high-level action choices, giving provenance without touching output tokens. Prior agent watermarks break in two ways. First, all three prior schemes bind the watermark to the exact action symbol, so renaming a tool desynchronizes decoding even when the observation is untouched; in AgentMark's own robustness test, paraphrasing the observation alone drops bit-recovery to 16.8%. Second, every prior agent watermark studies only re...
  </details>

- **2026-10-06** — Yutong Liu, Chenyi Wang, Ming F. Li et al. — [Don't Let One Lie Survive A Hundred Truths: A Selective Bayesian Trust Estimator for Collaborative Perception](http://arxiv.org/abs/2610.07875v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception (CP) enables connected vehicles to see beyond their own sensors but makes them dependent on messages they cannot independently verify. A compromised collaborator can surgically conceal a single safety-critical object or inject a non-existing one while correctly reporting many others. Existing Bayesian trust mechanisms pool agreement across objects, which, while effective against blatant untargeted attacks, either incurs high false-positive rates (FPR), or allows unrelate...
  </details>

- **2026-10-06** — Xianwen Deng, Ruijie Zhao, Mingwei Zhan et al. — [SCSM: A Traffic-Native Foundation Model for Transferable Website Fingerprinting](http://arxiv.org/abs/2610.07776v1)
  <details><summary>📄 Abstract</summary>
  Website fingerprinting infers the websites visited by users from encrypted traffic metadata. However, models trained under fixed collection conditions often degrade as website sets, collection times, network paths, browsers, or defenses change. Existing transferable attacks either rely on handcrafted perturbations of individual traces or adapt language-oriented architectures to traffic, limiting their ability to capture traffic-native semantics. To address these limitations, we propose SCSM, a t...
  </details>

- **2026-10-06** — Thanh Dong, An Ngo, Minh Dau et al. — [Detecting LLM-Assisted Vietnamese Writing via Keystrokes under Behavioral Manipulation](http://arxiv.org/abs/2610.07700v1)
  <details><summary>📄 Abstract</summary>
  We study the robustness of keystroke dynamics for detecting large language model (LLM)-assisted writing. We introduce a Vietnamese keystroke dataset capturing realistic writing modes, including bona fide composition, transcription, and paraphrasing. We also define a behaviorally grounded threat model in which users deliberately alter typing patterns. To implement the threat model, we create behaviorally manipulated variants of the data designed to evade keystroke-based detection. We evaluate fou...
  </details>

- **2026-10-06** — Shaswata Mitra, Raj Patel, Subash Neupane et al. — [Where Rules End and Judges Begin: Measuring the Judgment Boundary in Multi-Agent Systems Security](http://arxiv.org/abs/2610.07657v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) engage tools, share memory, and delegate tasks, often encountering adversarial content. Current defenses for MAS are typically evaluated in isolation, focusing on one attack type at a time, which can lead to costly and hard-to-audit outcomes. This study organizes defenses into five principles, implementing them as DEFER1 (DEterministic-First Enforcement with Residual judgment), which includes a cascade of 28 checks that blocks what it can and refers the rest t...
  </details>

- **2026-10-06** — Lei Yang, Boqi Li, Chunmian Lin et al. — [Sparse2comm: Towards Robust Cooperative 3D Object Detection](http://arxiv.org/abs/2610.08573v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception improves autonomous driving by sharing complementary observations among vehicles and roadside infrastructure for 3D object detection. However, practical deployment is constrained by limited bandwidth and unreliable cooperation, where packet loss, transmission delay, and spatial misalignment jointly degrade the cooperative feature stream. Existing methods often reduce communication cost or compensate for one degradation type, leaving coupled disturbances insufficiently addr...
  </details>

- **2026-10-06** — Maoqi Liu, Quan Fang, Yufei He — [CoDe-LoRA: Mitigating the Orthogonality Dilemma in Continual Learning of LLMs via Knowledge Consolidation and Decoupling](http://arxiv.org/abs/2610.08312v1)
  <details><summary>📄 Abstract</summary>
  Continual learning (CL) is essential for Large Language Models (LLMs) to sequentially adapt to evolving tasks. To mitigate catastrophic forgetting, recent advances implement low-rank adaptation with orthogonal projections (e.g., O-LoRA) to isolate task parameters. However, we reveal that such strict geometric constraints trigger an "Orthogonality Dilemma": rigid parameter isolation impedes the transfer and accumulation of shared representations across semantically related tasks. In this work, we...
  </details>

- **2026-10-06** — Yunju Kang, Seonghyeon Cho, Irene Li et al. — [POLAR: Ontology-Guided Risk Prevention for Tool-Calling LLM Agents](http://arxiv.org/abs/2610.08082v1)
  <details><summary>📄 Abstract</summary>
  LLM tool-use agents operate in dynamic environments where many actions carry operational risk. However, most safety mechanisms react only after errors manifest. Existing pre-emptive approaches either fine-tune the agent on chain-of-thought deliberation or compile natural-language guardrails into runtime checks, but they do so without exposing a structural, auditable verdict. We propose POLAR, a guardrail framework for small tool-calling agents that assesses reversibility through a structured two...
  </details>

- **2026-10-06** — Zizhuo Zhang, Xiong Peng, Jingwei Sun et al. — [Rethinking Faithfulness in LLMs: A Pairwise Context-Sensitive Perspective](http://arxiv.org/abs/2610.07894v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are expected to answer questions faithfully based on the provided context, abstaining when the context information is insufficient to answer the questions. Existing faithfulness evaluations typically assess each question-context instance in isolation; however, such instance-level evaluation fails to capture a fundamental requirement of faithful behavior: the ability to adapt model responses to changes in available contexts. In particular, a model should provide corre...
  </details>

- **2026-10-06** — Jonathan Chang, Zimeng Lyu — [Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction](http://arxiv.org/abs/2610.07825v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting models are typically compared on pointwise error, which scores a prediction in isolation from the decision it is produced for, and a lower forecast error does not imply a better decision downstream. A parallel debate asks whether modern transformer architectures forecast better than recurrent and other lightweight models. We compare linear, fixed recurrent, transformer, and mixing based architectures against recurrent networks evolved by neuroevolutionary architecture sea...
  </details>

- **2026-10-06** — Robert A. Lewis, I-Min Chiu, Kyle Verrier et al. — [MS-ECG-FM: Towards a More Universal Electrocardiogram Foundation Model for Health Monitoring using Multi-source Contrastive Learning](http://arxiv.org/abs/2610.07662v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) records the electrical activity of the heart, aiding diagnosis by detecting abnormalities in cardiac function. ECG foundation models have demonstrated promising results, but are limited by a reliance on ECG interpretation reports as their sole supervision. Because interpretation reports only capture the subset of waveform information routinely recognized by clinicians, this constrains representation learning to overlook the broader diagnostic signals present in ECG. We ...
  </details>

- **2026-10-06** — Myeung Suk Oh, Zhiyao Zhang, Alvaro Velasquez et al. — [Foundation Model-Aided Multi-Agent Reinforcement Learning for Wireless Random Access Network Optimization](http://arxiv.org/abs/2610.07550v1)
  <details><summary>📄 Abstract</summary>
  Random access (RA) is one of the most foundational medium access control (MAC) layer scheduling schemes for handling unpredictable data traffic from multiple terminals. While multi-agent reinforcement learning (MARL) has been explored to optimize RA-based wireless networks, its reliance on experience-driven, distributed policy learning incurs significant training overhead for each optimization task, limiting its feasibility in real-world applications. In this work, we propose to leverage a found...
  </details>

- **2026-10-06** — Khac Duc Giang Nguyen, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag — [Catastrophic Forgetting in Sequential Thermal Anti-UAV Detection: The Role of Scale-Conditioned Gradient Imbalance](http://arxiv.org/abs/2610.08315v1)
  <details><summary>📄 Abstract</summary>
  Counter-UAV systems based on thermal infrared detection must stay accurate as operational datasets evolve, yet sequential fine-tuning causes catastrophic forgetting of prior tasks, a problem that remains insufficiently characterized in this domain. This continual-learning study measures the stability-plasticity trade-off in YOLOMG, a YOLOv5-based detector run as a single thermal-infrared stream with the motion channel disabled, trained sequentially across three anti-UAV benchmarks of rising scal...
  </details>

- **2026-10-06** — Rainer Lienhart, Daniel Kienzle, Shin'ichi Satoh et al. — [Event Detection in Table Tennis Videos using 2D Keypoints](http://arxiv.org/abs/2610.08286v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the challenge of automatic, frame-accurate event detection in table tennis videos. Current methods for estimating 3d ball trajectories and ball spin typically require that key events, such as ball-racket contacts, have already been identified in advance. This requirement makes it difficult to apply these methods to longer, unedited video recordings. To overcome this limitation, we propose EventNet, a two-stage pipeline to detect key events: (1) 2d keypoints are extracted of ...
  </details>

- **2026-10-06** — Cheng-Han Yeh, Kuan-chun Yu, Cheng-Chang Tsai et al. — [On the Intrinsic Limited Robustness of Latent-Based Watermarking](http://arxiv.org/abs/2610.08178v1)
  <details><summary>📄 Abstract</summary>
  Existing latent-based watermarking methods for diffusion models have overestimated their robustness to image distortions, including geometric transformations such as rotation, scaling, and translation (RST). Moreover, this paradigm of watermarking approaches may suffer from inherent limitations arising from the domain in which the watermark is embedded. In this paper, we provide the first theoretical analysis explaining why these methods lack invariance to perturbations. By relaxing the invarian...
  </details>

- **2026-10-06** — Zheng Gao, Xiaoyu Li, Zhicheng Bao et al. — [Rethinking Visual Provenance: Detection and Watermarking Across Direct Visual Generation and LLM-Driven Code Rendering](http://arxiv.org/abs/2610.08137v1)
  <details><summary>📄 Abstract</summary>
  AI systems create images and videos with image/video generation models or by writing code and graphics descriptions that are then rendered. These routes can produce similar visible artifacts but expose different representations, intervention points, and provenance evidence. We develop a production-centered framework that compares detection and watermarking across both routes. An explicit verification specification distinguishes passive inference, message recovery, and authenticated provenance. W...
  </details>

- **2026-10-06** — Kavienan Jegatheesan, Gayathri Lihinikaduarachchi — [When Tools Lie: Reliability of Mathematical Agents Under Corrupted Tool Feedback](http://arxiv.org/abs/2610.08097v1)
  <details><summary>📄 Abstract</summary>
  Mathematical problem solving often requires deterministic computational steps that agents delegate to tools and implicitly trust. Yet tools can fail silently, returning plausible but incorrect results. How well can agents detect and correct corrupted tool call outputs? We study this through a controlled corruption framework where a hidden interceptor replaces tool call results with plausible incorrect information on targeted problems. We evaluate agents across 31 problems under four verification...
  </details>

- **2026-10-06** — Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ibeth P. Alarcón et al. — [Towards benchmarking Western Bluebird detection in the wild](http://arxiv.org/abs/2610.07802v1)
  <details><summary>📄 Abstract</summary>
  Bird monitoring in natural environments is challenging due to the small size of some species of birds relative to the scene, background clutter, variability in illumination, and the observers' viewpoint. Progress is further limited by the scarcity of large-scale, realistic datasets, which are essential for understanding behavioral patterns. To address this gap, we introduce a new benchmark dataset for the detection and segmentation of Western bluebirds (Sialia Mexicana), comprising over 6,000 la...
  </details>

- **2026-10-05** — Hao Fu, Dawn Song, Peng Gao — [NetAgent: Multi-Task Agentic Network Traffic Analysis Made Practical](http://arxiv.org/abs/2610.07386v1)
  <details><summary>📄 Abstract</summary>
  Network traffic analysis is central to network security, spanning tasks from intrusion detection to encrypted traffic classification. Existing approaches either train task-specific models that generalize poorly or rely on costly traffic foundation models that still struggle under distribution shift. We present NetAgent, the first agentic framework for multi-task traffic analysis. Through a carefully designed agent loop, NetAgent supports complex task understanding, on-the-fly decomposition and o...
  </details>

- **2026-10-05** — Ritvij Sharma, Russell Dlugosz, Ryan Zhou et al. — [Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy](http://arxiv.org/abs/2610.07403v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory allows Large Language Models (LLMs) to maintain personalized context across interactions, but retrieved user history can induce memory-induced sycophancy, causing models to favor stored user beliefs over objective evidence. Existing defenses primarily operate on retrieved context and are rarely evaluated jointly with internal behavioral bias. We introduce a $2 \times 2$ defense-in-depth framework separating internal activation steering from external memory handling. We extract s...
  </details>

- **2026-10-05** — Xinting Liao, Siyan Liu, Rabab K. Ward et al. — [MemCo: Memory-Centric Collaboration for Generalizing LLM Agents to Unseen Environments](http://arxiv.org/abs/2610.07376v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate in interactive environments, where they need to make sequential decisions through observation, action, and feedback. Although memory can help agents reuse experience, existing work designs memory in isolation, where collecting enough trajectories to populate it is expensive. Existing shared-memory approaches mitigate isolated experience by pooling episodic memories across tasks and environments. However, retrieving shared memory is challenge...
  </details>

- **2026-10-05** — Yaqi Cai, Mingxuan Liu, Lorenzo Vaquero et al. — [Localize Any Object in X-Ray Security Scans without Human Annotation](http://arxiv.org/abs/2610.07326v1)
  <details><summary>📄 Abstract</summary>
  Universal object localization in X-ray security inspection is critical for automated threat detection in safety-critical venues. However, unlike everyday RGB images that dominate web-scale visual data, X-ray scans exhibit distinct color patterns, ambiguous boundaries, and compositional structures caused by volumetric superposition. These gaps hinder the direct zero-shot transfer of dense perception foundation models trained on web-scale RGB data. Moreover, annotated X-ray data is scarce and requ...
  </details>

- **2026-10-05** — Nikolaos Kekatos, Mihaela Curcă, Georgios Koutidis et al. — [From Sandbox to Enforcement: Confidence-Qualified Threat Intelligence for Critical Infrastructure](http://arxiv.org/abs/2610.07310v1)
  <details><summary>📄 Abstract</summary>
  Security operations centres and national incident-response teams defending critical infrastructure collect abundant threat data yet struggle to turn it into actionable intelligence. A malware sandbox produces detailed behavioural evidence, but as a large, unranked report whose confidence is unstated. We present CG-CTI, an operational pipeline that converts live sandbox output (CAPEv2) into STIX 2.1, correlates it in a knowledge graph with other critical-infrastructure sensors, and attaches to ev...
  </details>

- **2026-10-05** — Xingru Zhou, Luis Sentis, Aarti Choudhary — [SAFESHIELD: A Decision-Organization Framework for Deployment-Time Safety of Small Language Models](http://arxiv.org/abs/2610.07276v1)
  <details><summary>📄 Abstract</summary>
  Deployment-time safety of language models is commonly implemented through runtime guardrails such as input moderation, routing, retrieval verification, and output filtering. Existing deployment frameworks provide increasingly capable mechanisms for these functions, but offer limited guidance on how the safety decisions they produce should be explicitly organized, coordinated, and audited. We formulate deployment-time safety as a decision-organization problem with two elements: responsibility-ori...
  </details>

- **2026-10-05** — Hadi Vafaii, Tejas Rao, David Chanin et al. — [Inference and learning in sparse autoencoders as natural gradient flow](http://arxiv.org/abs/2610.07389v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders are widely used to uncover interpretable features in neural networks, yet reliable recovery remains difficult when features overlap or activate infrequently. These challenges involve both inferring which features explain an input and learning the dictionary that represents them. Here, we unify inference and dictionary learning as natural-gradient flows on a shared variational free energy. We instantiate this framework as BeFOND, an encoder-free sparse coding model with closed...
  </details>

- **2026-10-05** — Sumanyu Muku — [MemMux: Runtime Verification and Honest Resource Attribution for Fleets of Parallel Coding Agents](http://arxiv.org/abs/2610.07257v1)
  <details><summary>📄 Abstract</summary>
  Developers increasingly run a fleet of coding agents side by side on one workstation. The tools they reach for, terminal multiplexers like tmux and a new generation of agent managers, were built to arrange windows, not to govern memory. When ten agents each spawn language servers, test runners, and browsers, no standard tool can say how much memory belongs to which agent, confirm that a terminated agent's descendants are gone, notice a child that has escaped its agent, or keep the machine off th...
  </details>

- **2026-10-05** — Simon Hadush Nrea, Filimon Gidey Gebremichael, Gebrekirstos Hagos Gebrekirstos et al. — [Hybrid Cross-Modal Attention Network for Early Breast Cancer Detection in Low-Resource Clinical Settings](http://arxiv.org/abs/2610.07243v1)
  <details><summary>📄 Abstract</summary>
  Breast cancer is the leading cause of cancer-related mortality among women in Sub-Saharan Africa, where delayed diagnosis results from limited radiology expertise and fragmented clinical data systems. Although deep learning models have demonstrated strong performance in mammographic analysis, most rely solely on imaging data and are trained on Western populations, limiting their applicability in African healthcare settings. This paper presents a Hybrid Cross-Modal Attention Network (HCMAN) that ...
  </details>

- **2026-10-05** — Cristian Martella, Angelo Martella, Antonella Longo et al. — [Small Language Models for Smart Data Model Classification at the Edge: A Cost-Aware Hybrid Approach](http://arxiv.org/abs/2610.07093v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of heterogeneous data sources within the Internet of Things (IoT) across domains such as smart cities, energy management, and environmental monitoring necessitates efficient and scalable data standardization methods. Effective classification of smart data models (SDMs) is essential for facilitating interoperability. However, existing approaches are often limited by high resource consumption and lack applicability in edge environments with constrained computational capabil...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 48 papers

- **2026-10-06** — Shiqi Li, Sean Cho, Yijie Li et al. — [4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction](http://arxiv.org/abs/2610.08782v1)
  <details><summary>📄 Abstract</summary>
  Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-...
  </details>

- **2026-10-06** — Jian Gao, Kailin Bi, Jiamin Xu et al. — [PrimitiveCAD: An LLM-Based Point-to-CAD Reconstruction with Primitive-Aware Tokenization and Operation Alignment](http://arxiv.org/abs/2610.08698v1)
  <details><summary>📄 Abstract</summary>
  Large-model-based point-to-CAD generation holds immense potential for advancing industrial design and enhancing 3D modeling efficiency. However, most existing methods approach the problem as a general point-cloud encoding and token prediction task, neglecting the tokenization and supervision specifically for CAD-related primitives. As a result, these methods often struggle to accurately reconstruct the intricate primitive structures. To address this limitation, we propose PrimitiveCAD, a novel m...
  </details>

- **2026-10-06** — Yexiong Lin, Shanshan Ye, Yu Yao et al. — [SquidAgent: Parallelize Wisely, Coordinate Efficiently](http://arxiv.org/abs/2610.08647v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline. We attribute this gap to two hidden costs that parallel execution incurs but a serial agent avoids. First, there is a re-exploration cost: redundant effort spent by parallel workers reconstructing context that the orch...
  </details>

- **2026-10-06** — Tatiana Brailovskaya, Nicholas A. Cook, Sofia Poinelli — [Spectral Recovery of Point Clouds from Noisy Geometric Graphs](http://arxiv.org/abs/2610.08634v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of recovering low-dimensional latent geometry from a random geometric graph generated by noisy, high-dimensional data. Specifically, we analyze the performance of a spectral embedding algorithm on the Signal+Noise Graph Model, in which vertices are associated to points perturbed by Gaussian noise, and edges are included for pairs whose inner product exceeds a specified alignment threshold. In the high-dimensional regime where the number $n$ of points and the ambient dimensio...
  </details>

- **2026-10-06** — Dongchen Si, Di Wang, Mingzhen Xu et al. — [RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models](http://arxiv.org/abs/2610.08539v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing scene classification is a fundamental task in Earth observation and geospatial analysis. Existing approaches mainly follow three paradigms: task-specific visual classification, vision-language similarity matching, and autoregressive multimodal generation. However, visual classifiers rely on predefined label spaces, CLIP-based methods perform recognition through static image-text alignment, and multimodal large language models (MLLMs) introduce unnecessary token-level generation fo...
  </details>

- **2026-10-06** — Onur Selim Kilic, Afra Nawar, Cem Okan Yaldiz et al. — [Cylindrical Geodesic Flow Matching for Quasiperiodic Physiological Signal Transformation](http://arxiv.org/abs/2610.08510v1)
  <details><summary>📄 Abstract</summary>
  Paired translation between quasiperiodic physiological waveforms (i.e., recovering a target oscillatory signal from the source) is central to the interpretation of cardiovascular signals derived from wearables placed at different body locations. This source-to-target mapping in these problems carries inherent geometric structure: the phase wraps around the cycle and must be treated as a circular variable, the amplitude remains strictly positive, and the beat-to-beat alignment can drift unpredict...
  </details>

- **2026-10-06** — Han Ma — [Replica Fragmentation and Glassy Dynamics in Parity Learning](http://arxiv.org/abs/2610.08503v1)
  <details><summary>📄 Abstract</summary>
  We study how independently trained Transformer neural networks reconstruct a binary string from its local domain walls. Runs sharing the data and training protocol can realize different functions. We treat them as replicas and measure truth alignment $m$, prediction confidence $q_{\mathrm{self}}$, and cross-replica agreement $q_{\mathrm{cross}}$. Confident disagreement defines the finite-size replica fragmentation that we call glass-like. With small training sets, replicas predict all training e...
  </details>

- **2026-10-06** — Agnieszka Lach, Magdalena Wysocki, Feng Li et al. — [Deformable CT-US Registration via Anatomy-Aware Implicit Neural Representations](http://arxiv.org/abs/2610.08419v1)
  <details><summary>📄 Abstract</summary>
  Slice-to-volume registration between ultrasound (US) and preoperative computed tomography (CT) imaging would enhance many minimally invasive interventions, for example by locating soft tissue structures intra-operatively that are discernible in CT. While optical tracking enables initial rigid registration, contact from the probe induces soft tissue deformations that inhibit accurate alignment. In this work, we introduce a deformable CT-ultrasound registration framework that incorporates anatomic...
  </details>

- **2026-10-06** — Zhibo Deng, Dongyuan Li, Shuwen Ge et al. — [Enhancing LLMs with Cognitive-Affective Personality Inference for Simulating Human Social-Psychological Behavior](http://arxiv.org/abs/2610.08328v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate human participants in social and behavioral studies, yet static persona prompting typically maps a participant profile and an experimental scenario directly to a response, entangling stable dispositions with situation-specific interpretations. To address this limitation, we introduce \textbf{SPIN}, a cognitive-affective personality system-inspired inference pipeline for simulating human social-psychological behavior. Specifically, SPIN impl...
  </details>

- **2026-10-06** — Shu-Kai Hsieh, Da-Chen Lian — [Language Unalignability: Why Some Concepts Resist Cross-Cultural Benchmark Evaluation](http://arxiv.org/abs/2610.08303v1)
  <details><summary>📄 Abstract</summary>
  Current evaluation of multilingual Large Language Models (LLMs) rests on an implicit Translation-Isomorphism Assumption (TIA): that semantic structures across languages are congruent and mutually mappable without loss of information. We argue that this assumption is not merely violated in practice, but ill-posed in principle for a typologically identifiable class of concepts, including pragmatic markers, honorifics, and diachronically stratified terms. We formalize this failure using a usage-clo...
  </details>

- **2026-10-06** — Shixin Peng, Kun Jiang, Jiaxing Zheng et al. — [MASC: A Multi-Agent Self-Calibration Framework with Latent Construct Alignment for Consistent Client Role-Playing in Psychological Counseling](http://arxiv.org/abs/2610.08250v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate clients for counselor training and psychological counseling research, but reliable simulation requires clients to remain psychologically coherent across extended interactions. Existing role-playing methods largely rely on static profile prompts and may exhibit persona drift, unrealistic cooperativeness, or inconsistent psychological states, communicative actions, and emotions. Existing evaluations also lack a unified testbed for both stable...
  </details>

- **2026-10-06** — Ahmed Abouelazm, Rupert Polley, Qingyuan Zhang et al. — [Beyond Waypoint Regression: Query-Based Cost Learning over Reachable Ego Futures for End-to-End Driving](http://arxiv.org/abs/2610.08123v1)
  <details><summary>📄 Abstract</summary>
  End-to-end planners based on waypoint regression achieve strong open-loop accuracy, but they primarily learn to mimic expert geometry and remain difficult to adapt to deployment-time safety constraints. We propose a query-based cost-learning framework that estimates bounded costs for dynamically reachable ego trajectory queries, rather than dense BEV cells or a small regressed trajectory set. Compact joint scene tokens capture coherent multimodal agent futures, while contingency-aware cost aggre...
  </details>

- **2026-10-06** — Langxi Huang, Pingping Zhang, Lanyun Zhu et al. — [ChartBmkAgent: Harness-Governed Multi-Agent Construction of Chart QA Benchmarks from Sparse Error-Taxonomy Specifications](http://arxiv.org/abs/2610.08106v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) advance rapidly, while conventional benchmark development lags behind, delaying investigation of newly observed capability gaps. Such investigation requires an expressive task format and an on-demand construction process: information-rich charts make chart question answering (Chart QA) suitable for probing coupled perception and reasoning. Automated Chart QA construction is intended to shorten the benchmark-development cycle by turning identified gaps int...
  </details>

- **2026-10-06** — Hemant Yadav, Sunayana Sitaram, Roger Zimmermann et al. — [DirectSpeech2LLM: A Simple End-to-End Framework to Mitigate Prompt Overfitting in Speech-LLMs](http://arxiv.org/abs/2610.08085v1)
  <details><summary>📄 Abstract</summary>
  Speech-LLMs often exhibit prompt overfitting, where models solely trained on automatic speech recognition (ASR) instruction fail to generalize to new instructions such as speech translation and continue to behave primarily as ASR system. We propose DirectSpeech2LLM, a simple end-to-end framework that preserves the instruction-following ability of the LLM on unseen tasks when conditioned on speech. It computes distance-based CTC loss over the frozen LLM embedding matrix and uses greedy CTC labels...
  </details>

- **2026-10-06** — Rudolf L. M. van Herten, Soufiane Ben Haddou, Rachit Saluja et al. — [Optimization Encoders: Rethinking Second-Order Meta-Learning for Neural Fields](http://arxiv.org/abs/2610.08075v1)
  <details><summary>📄 Abstract</summary>
  Conditional neural fields represent signals continuously, but their effectiveness depends on how the conditional latent representations are inferred from observed data. In meta-learning, this encoding occurs through gradient updates induced by the decoder, tying representation learning directly to decoder design. We formalize this connection by interpreting latent optimization as an optimization encoder, unifying the roles of second-order differentiation, latent parameterization, and task superv...
  </details>

- **2026-10-06** — Jing Chen, Giulia Loca, Simona Amenta et al. — [Pseudowords as probes: Large Language Models show little of the sublexical sensitivity that governs human pseudoword processing](http://arxiv.org/abs/2610.07936v1)
  <details><summary>📄 Abstract</summary>
  Systematicity, the probabilistic mapping of form to meaning, permeates language at all levels, and sublexical cues have been shown to govern human pseudoword processing. Yet whether LLMs exhibit comparable sensitivity to these cues remains unclear. We tested five LLMs on two Italian two-alternative forced-choice pseudoword experiments and compared their responses with a human behavioural baseline. LLMs aligned more reliably with humans when real-word options provided a lexical familiarity cue th...
  </details>

- **2026-10-06** — Giyeol Kim, Chanho Eom — [TF-PRVR: Training-Free Partially Relevant Video Retrieval](http://arxiv.org/abs/2610.07925v1)
  <details><summary>📄 Abstract</summary>
  Partially Relevant Video Retrieval (PRVR) aims to retrieve untrimmed videos containing moments relevant to a given text query. Despite recent progress, existing PRVR methods suffer from two key limitations: a fixed video decomposition scheme that causes semantic dilution, and source-domain overfitting induced by task-specific training. In this paper, we propose TF-PRVR, the first training-free framework for PRVR. TF-PRVR leverages frozen vision-language features to construct video-specific hiera...
  </details>

- **2026-10-06** — Keliang Chen, Yaxin Hou, Hui Liu et al. — [Unsupervised Long-Tailed Adaptation of Vision-Language Models](http://arxiv.org/abs/2610.07903v1)
  <details><summary>📄 Abstract</summary>
  Adapting vision-language models to downstream tasks has achieved remarkable success by leveraging pseudo-labels generated from unlabeled data. Existing methods typically assume a uniform unlabeled data distribution, and thus the resulting pseudo-label distribution is likewise uniform. However, real-world data distributions are often long-tailed. To tackle this, we formalize a new scenario termed Unsupervised Long-Tailed Adaptation (ULTA). Under this scenario, existing methods exhibit a contrasti...
  </details>

- **2026-10-06** — Yuezhe Zhang, Lei Wei, Jingnan Du et al. — [Geometry-Constrained Bidirectional Point Cloud Registration for Thin, Sheet-Like Heritage Artifacts](http://arxiv.org/abs/2610.07793v1)
  <details><summary>📄 Abstract</summary>
  Non-contact three-dimensional reconstruction of thin, sheet-like heritage artifacts poses significant geometric and registration challenges. Due to their fragility, these artifacts cannot be suspended or equipped with artificial markers, necessitating independent acquisition of their front and back surfaces. Subsequent registration proves difficult due to the limited number of shared geometric features and the scarcity of explicit physical constraints, which may result in rotational ambiguity, i...
  </details>

- **2026-10-06** — Xin Wang, Hao Yu, Zhengyang Zhuge et al. — [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](http://arxiv.org/abs/2610.07767v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization accuracy on the training and rollout paths independently rather than directly reducing the discrepancy between the two quantized execution paths. In this work, we propose TRACE (Trai...
  </details>

- **2026-10-06** — Byeonghu Na, Donghyeok Shin, Yeongmin Kim et al. — [WASD: Wasserstein-based Knowledge Distillation for Large Language Models](http://arxiv.org/abs/2610.07706v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive large language models (LLMs) have rapidly advanced in capability, but their increasing scale comes with substantial computational and memory costs at inference time. Knowledge distillation (KD) offers a practical solution by transferring knowledge from a large teacher model to a smaller student model via alignment of discrete probability distributions. However, existing KD methods for LLMs primarily rely on divergences that evaluate discrepancies through probability values at each...
  </details>

- **2026-10-06** — Juntong Li, Lingwei Dang, Haomin Wu et al. — [Unlocking Fine-Grained Perception in CLIP via Structurally-Aware Latent Masked Modeling](http://arxiv.org/abs/2610.07689v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) such as CLIP excel in global semantic alignment but often lack fine-grained perceptual capabilities. This hinders dense prediction tasks and bottlenecks the visual potential of Multimodal Large Language Models (MLLMs). Existing research has attempted to enhance CLIP's visual representations by incorporating geometric priors from vision-centric models. However, these strategies often struggle to achieve deep alignment for both local spatial structures and global sema...
  </details>

- **2026-10-06** — Guo Tang, Yongtao Wang — [PhysTacGen: Physics-Aware Visual-Tactile Sensor Image Generation](http://arxiv.org/abs/2610.08068v1)
  <details><summary>📄 Abstract</summary>
  Realistic physical interaction is a cornerstone of embodied intelligence, yet collecting paired visual--tactile data remains costly. Visual-to-tactile synthesis offers a promising approach to augmenting such data, but learning this mapping is complicated by the gap between visual appearance and contact-related material properties, as well as spatial misalignment in paired observations. To address these challenges, we present \textbf{PhysTacGen}, a visual-to-optical-tactile image generation frame...
  </details>

- **2026-10-05** — Samrendra Roy, Jason Yoo, Souvik Chakraborty et al. — [Targeted search shows that random-device testing underestimates worst-case error in a simulated wave-based neural operator](http://arxiv.org/abs/2610.07529v1)
  <details><summary>📄 Abstract</summary>
  Wave-based processors promise fast, energy-efficient Fourier layers for neural operators. They are usually validated on randomly sampled devices, but using them requires knowing how large their error can become under fabrication and alignment variation. In a stylised numerical case study, a hybrid Fourier neural operator runs its four spectral layers on simulated coherent 4f processors with 32 toleranced knobs, whose half-widths are representative rather than calibrated. For 120 models (four tas...
  </details>

- **2026-10-05** — Priyanka Iyer, Cecilia Soroco, Gerhard Gompper — [Threat Evasion and Information Propagation in Cognitive Flocks](http://arxiv.org/abs/2610.07297v1)
  <details><summary>📄 Abstract</summary>
  Information sharing, threat perception, and collective evasion highlight the advantages of swarm intelligence. Here, we study the behavior of flocks of cognitive agents, based on numerical simulations of the augmented inertial spin model, with an explicit predator. Each agent on the predator-facing side of the flock perceives the threat, triggering collective turns through local interactions. We show that the augmented inertial spin model sustains nearly linear information propagation in the und...
  </details>

- **2026-10-05** — Tao Long, Lydia B. Chilton — [SPEAR: Five Principles for Interactive Human-Agent Alignment](http://arxiv.org/abs/2610.07204v1)
  <details><summary>📄 Abstract</summary>
  Recent AI alignment work often frames alignment as a pre-deployment optimization problem: collect human feedback, learn preferences or principles, finetune the model, and deploy an aligned system. This framing has produced major progress, but it under-specifies what happens once AI systems act as agents on users' behalf in situated, long-term, and social contexts. This position paper reframes human-agent alignment as an ongoing interaction design problem. We propose SPEAR, five pillars of intera...
  </details>

- **2026-10-05** — Darshil Doshi, Wenjie Zhou, Corinna Elena Wegner et al. — [A theory of platonic representations in language models](http://arxiv.org/abs/2610.07168v1)
  <details><summary>📄 Abstract</summary>
  Representations of translated sentences are similar in the inner layers of multilingual language models -- an observation connected to the platonic representation hypothesis, yet unexplained theoretically. We provide an explanation based on the assumption that data have a hidden hierarchical structure whose abstract levels are shared across languages while surface levels are modality- or language-specific. Concretely, we generate synthetic languages from probabilistic context-free grammars shari...
  </details>

- **2026-10-05** — Ermis Soumalias, Richard Mudd, Abbas Zaidi — [Incentive Alignment in Online Experimentation](http://arxiv.org/abs/2610.05922v2)
  <details><summary>📄 Abstract</summary>
  Evaluating the causal effect of new features is a central goal for online platforms. While recent literature addresses limited testing traffic via centralized portfolio optimization, this perspective abstracts away a critical institutional reality: experimentation is operationally decentralized. The experimenters who develop new features also dictate which hypotheses to test, and they are typically rewarded based on empirical average treatment effects that are prone to upward bias. Left unchecke...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 49 papers

- **2026-10-06** — Amir Mohammad Mahfoozi, Zi Yang, Ying Li et al. — [Random Feature Gaussian Process Attention: Linear-Time Probabilistic Attention with Calibrated Uncertainty](http://arxiv.org/abs/2610.08578v1)
  <details><summary>📄 Abstract</summary>
  Transformers provide a state-of-the-art modeling framework, yet poor calibration limits their reliability in safety-critical applications. A promising direction addresses this issue by interpreting attention as a Gaussian process (GP) posterior, which enables principled uncertainty calibration but incurs cubic complexity in sequence length due to the inversion of the kernel; although decoupled GP variants reduced the cost to quadratic, the computation remains prohibitive in practice. In this pap...
  </details>

- **2026-10-06** — Hyeongheon Cha, Young D. Kwon, Sung-Ju Lee — [Test-Time Adaptation of Quantized ViTs via Single-Pass Quantizer-Aligned Recalibration](http://arxiv.org/abs/2610.08358v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization is a standard route to fitting vision transformers (ViTs) into edge compute and memory budgets, yet quantized models become especially brittle under distribution shift. Test-time adaptation (TTA) addresses such shifts without labels, but most existing approaches are poorly aligned with the constraints of quantized inference. Prevailing TTA methods recover accuracy through backpropagation, while backprop-free methods often still incur overhead from extra forward passes ...
  </details>

- **2026-10-06** — Haotian Yang, Huikang Jiang, Yucheng Wu et al. — [Does Steering Break Your Model? A Multi-Dimensional Evaluation Suite for LLM Steering Methods](http://arxiv.org/abs/2610.07722v1)
  <details><summary>📄 Abstract</summary>
  Activation steering provides a lightweight and flexible way to control large language model (LLM) behavior. However, effective steering requires more than inducing the intended behavior: it should also limit unintended changes and remain robust across inputs and training data. Existing evaluations cover these dimensions only in fragments. As a result, the trade-offs between efficacy and side effects have not been systematically characterized. We introduce SteerScope, a two-axis, multi-dimensiona...
  </details>

- **2026-10-06** — Kun Song, Yiming Wang, Yilin Chen et al. — [PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation](http://arxiv.org/abs/2610.08784v1)
  <details><summary>📄 Abstract</summary>
  Pretrained robotic policies can suffer substantial performance degradation under out-of-distribution (OOD) conditions encountered during deployment, motivating post-training through real-world interaction. However, reinforcement-learning (RL)-based post-training typically requires substantial environment interactions, a burden that is especially significant in manipulation, where each trial can be slow, costly, or destructive. Therefore, we present PEARS, a physics-prior-guided hybrid RL framewo...
  </details>

- **2026-10-06** — Mingju Gao, Qingle Liu, Yuzhao Peng et al. — [World Models' Last Exam in Physics](http://arxiv.org/abs/2610.08791v1)
  <details><summary>📄 Abstract</summary>
  Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks s...
  </details>

- **2026-10-06** — Nataliya Stepanova, Ivan Titov, Emily Allaway et al. — [The Missing Minimal Pair: Stereotype Evaluation in LLMs](http://arxiv.org/abs/2610.08747v1)
  <details><summary>📄 Abstract</summary>
  A common approach to measuring bias in Large Language Models is to compare the log-likelihoods of two contrastive stereotype sentences. We argue that such single-pair comparisons are often unreliable: simply rewriting the same stereotype with an alternative attribute can yield logically inconsistent preferences. To address this, we propose a dual minimal pair setup that introduces two axes of comparison for robust stereotype evaluation. First, we present a data-augmentation framework that fills ...
  </details>

- **2026-10-06** — Clayton Cohn, Joyce Fonteles, Kirk Vanacore et al. — [Agreement Is Not Validity: Cross-Model LLM Consensus in Diagnosing Student Failure Modes in K-12 Math Tutoring Dialogue](http://arxiv.org/abs/2610.08703v1)
  <details><summary>📄 Abstract</summary>
  In K-12 mathematics tutoring, student-tutor dialogue provides rich evidence of learners' problem-solving processes and sources of difficulty. Learning analytics research increasingly relies on large language models (LLMs) to extract such information from dialogue for a variety of downstream tasks, including knowledge tracing, behavioral modeling, and diagnosis of student reasoning errors. However, the validity of these model-generated interpretations remains insufficiently understood. In this ex...
  </details>

- **2026-10-06** — Nur A Zarin Nishat, Jens Lehmann, Andrei Aioanei et al. — [A Systematic Study of Small Language Models on Abstract Reasoning Tasks](http://arxiv.org/abs/2610.08680v1)
  <details><summary>📄 Abstract</summary>
  Endpoint accuracy on abstract-reasoning benchmarks does not reveal whether a language model has acquired a transferable rule or fit distribution-specific regularities. We study this distinction in small language models on the ARC-TGI benchmark, which organizes abstract grid transformations into controllable task families and supports resampling, spatial shifts, and cross-benchmark transfer. Across more than 1,000 runs, we profile decoder-only, encoder--decoder, and mixture-of-experts model famil...
  </details>

- **2026-10-06** — Sayan Sinha, Vipul Harsh, B. Aditya Prakash et al. — [Agentic RCA for Internet-Scale Services Using Constrained Creativity](http://arxiv.org/abs/2610.08622v1)
  <details><summary>📄 Abstract</summary>
  System administrators of Internet-scale services need to resolve failure incidents to maintain reliability of such services. Ideally, we want a troubleshooting system to be: (1) expressive to known and unknown incidents with high accuracy; (2) cost efficient at scale; (3) explainable to provide actionable insights operators can act on; and (4) entail low effort from the operators. Unfortunately, most existing systems, including emerging LLM-assisted agentic workflows and structured frameworks fo...
  </details>

- **2026-10-06** — Pranjal Garg — [How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing](http://arxiv.org/abs/2610.08544v1)
  <details><summary>📄 Abstract</summary>
  Probes are the workhorse of interpretability. If a model's hidden states predict a variable, the model is said to represent it. But a probe score has no fixed meaning. An $R^2$ of 0.6 may only reflect what the input already gives away, and the same score can mean different things on different data. We propose reading every probe score against two reference points: a floor, what a declared set of simple inputs already predicts, and a ceiling, what the full input can predict. The gap between them,...
  </details>

- **2026-10-06** — Dennis Fucci, Andrea Bacciu, Dong Liu et al. — [Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World Discussions](http://arxiv.org/abs/2610.08513v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly deployed as autonomous agents in social environments, making it critical to study their ability to faithfully simulate human interactions. Central to this is grounding agents in realistic user personas, yet existing datasets rely on fictional personas and are limited to a handful of languages, lacking the empirical grounding necessary to evaluate behavioral fidelity across diverse populations. We introduce Wiki-Talkie, a multilingual dataset of real-world conversations from...
  </details>

- **2026-10-06** — Aleksandr Talitckii, Matthew M. Peet — [Stable Rational Approximation of PDE Transfer Functions with $H_\infty$ Error Bounds](http://arxiv.org/abs/2610.08497v1)
  <details><summary>📄 Abstract</summary>
  Transfer functions of Partial Differential Equations (PDEs) are irrational and difficult to obtain. Unlike for rational transfer functions, only a few methods are available for the control and analysis of irrational transfer functions. Thus, for robust analysis and control of PDEs, we need to use a rational approximation of the transfer function, preferably with provable $H_\infty$ error bounds. In this paper, we extend Krylov subspace model reduction to infinite-dimensional systems modeled by P...
  </details>

- **2026-10-06** — Rohan Hemant Chhatre, Chiranjit Dutta, Nalini Ravishanker et al. — [Scalable Regularized Vector Multiplicative Error Models for Positive-valued Financial Time Series](http://arxiv.org/abs/2610.08443v1)
  <details><summary>📄 Abstract</summary>
  The logarithmic multiplicative error model (log-vMEM) has been useful in modeling and forecasting multivariate positive-valued financial time series. The number of parameters grow rapidly with the dimension of the system and the lag order, making estimation computationally demanding in high-dimensional settings. This paper describes regularized estimation via hierarchical lag structures (Nicholson et al., 2020) for log-vMEM models with multivariate gamma error distribution of Tsionas (2004). The...
  </details>

- **2026-10-06** — Ekrem Aydiner — [A New Model for the Income Distribution](http://arxiv.org/abs/2610.08143v1)
  <details><summary>📄 Abstract</summary>
  In this study, we propose a kinetic trap--diffusion model to describe the emergence of Pareto distributions in money-exchange systems. Using kinetic Monte Carlo simulations, we show that the Pareto exponent depends explicitly on temperature and takes values in the range $0.5 \leq ν(T) \leq 1.5$. In the present framework, the temperature $T$ acts as a control parameter that regulates the exchange dynamics through thermally activated diffusion. Unlike conventional kinetic exchange models, where th...
  </details>

- **2026-10-06** — Anam Hashmi, Mayug Maniparambil, Julia Dietlmeier et al. — [Beyond Training from Scratch: Foundation Models for Data-Efficient and Generalizable Cardiac MRI Reconstruction](http://arxiv.org/abs/2610.08109v1)
  <details><summary>📄 Abstract</summary>
  Cardiac magnetic resonance imaging reconstruction aims to recover high-quality images from undersampled acquisitions, enabling faster scans while preserving diagnostic fidelity. Recent reconstruction methods are typically trained from scratch and often require large amounts of task-specific data, limiting their robustness under data scarcity and distribution shifts. In this work, we investigate whether pretrained vision foundation models can serve as effective priors for accelerated cardiac MRI ...
  </details>

- **2026-10-06** — Yuan Feng, Qize Yang, Ruizhe Chen et al. — [VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](http://arxiv.org/abs/2610.07987v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have become the dominant paradigm for visual understanding, but incur substantial costs by encoding inputs into dense, fixed-size patch tokens. However, visual information is unevenly distributed: some regions require fine-grained detail, while others admit compact representations. Downsampling sacrifices this detail, while existing token pruning and adaptive approaches remain limited in content-adaptive granularity, task generalization, and integration with mode...
  </details>

- **2026-10-06** — Yuhe Hu — [Quantization Effects on Tool-Failure Recovery Vary Across Prompts and Evaluation Designs](http://arxiv.org/abs/2610.07781v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization reduces the cost of deploying language-model agents, but its effect on recovery from temporary tool failures can depend on how recovery is evaluated. We compare 8-bit and 4-bit variants of Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct on twenty deterministic tool-use tasks and five prompts. The 8-bit-4-bit recovery comparison changes direction across prompts and evaluation targets. On tasks that both variants complete without faults under the same prompt, the differenc...
  </details>

- **2026-10-06** — Hyeongheon Cha, Hyungjun Yoon, Sung-Ju Lee — [Later Is Better: Token Reduction for ViTs Under Distribution Shift](http://arxiv.org/abs/2610.07758v1)
  <details><summary>📄 Abstract</summary>
  Training-free token reduction accelerates vision transformers by removing redundant tokens across layers, recovering most of the original accuracy at a fraction of the compute. These methods, however, are designed and evaluated primarily on clean data, and under real-world distribution shift their accuracy gap to the uncompressed model widens with the removal rate. We show that this gap is governed by the reduction schedule, the depth profile of removal, usually left fixed as an implementation d...
  </details>

- **2026-10-06** — Yi Xia, Pablo Carrasco Velo, Mudit Paliwal et al. — [SENSE: State-aware Emotion Navigation Storytelling Engine](http://arxiv.org/abs/2610.07666v1)
  <details><summary>📄 Abstract</summary>
  This paper presents SENSE, a state-aware framework for generating playable branching visual novels with multi-track emotional navigation. Integrating a state-based narrative architecture called MIND, a structure analyzer, and a path-aware context management module, SENSE produces narratives that are both structurally coherent and emotionally rich. From minimal high-level inputs, it generates multiple intersecting routes while preserving character consistency and narrative causality. Evaluations ...
  </details>

- **2026-10-05** — Victor De Lima, Grace Hui Yang — [On Open-Ended Information Seeking for Information Elicitation Agents](http://arxiv.org/abs/2610.07509v1)
  <details><summary>📄 Abstract</summary>
  Information elicitation is an open-ended information-seeking problem in which an interaction can unfold in many potentially valuable directions, requiring an elicitor to continually determine which information to pursue as new information emerges. In agentic elicitation, these decisions may be delegated to a foundation model, yet how model choice shapes the resulting information-seeking behavior remains understudied. We study how judgments about information value vary across LLMs and how these d...
  </details>

- **2026-10-05** — Ruihan A. Li, Ziyao Guo, Yingying Li — [Risk-Sensitive Crowd Navigation with Adaptive Ellipsoidal Conformal Prediction](http://arxiv.org/abs/2610.07474v1)
  <details><summary>📄 Abstract</summary>
  Safe crowd navigation under distribution shift requires uncertainty representations that capture structured human-motion prediction errors and safety objectives that account for rare but consequential failures. Existing uncertainty-aware methods typically represent prediction errors using isotropic regions, which can be either overly conservative or poorly aligned with directional motion uncertainty. We introduce a risk-aware navigation framework that uses anisotropic conformal ellipsoids to tra...
  </details>

- **2026-10-05** — Robert R Nerem, Pranav Singh, Cheyenne Ward et al. — [Algorithmically Aligned Neural Agglomerative Tree Construction](http://arxiv.org/abs/2610.07271v1)
  <details><summary>📄 Abstract</summary>
  Linkage algorithms for hierarchical clustering (HC) are a powerful and efficient framework for constructing clustering trees, yet it is often unclear which merge rule best suits a given dataset or task. In contrast, neural approaches can learn from data, but often fail to retain the efficiency and size generalization of classical algorithms. We introduce NN-linkage, a neural network (NN) model that can learn task-specific and locally dependent merge rules while retaining the recursive structure ...
  </details>

- **2026-10-05** — Chalindu Abeywansa, Sahan Gunasekara, Devindi De Silva et al. — [Sim-to-Real Transfer of Vision-Language Navigation in Continuous Environments Using an Ackermann-Steered Mobile Robot](http://arxiv.org/abs/2610.07192v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Navigation (VLN) enables robots to navigate through environments using natural language instructions, making human-robot interaction intuitive. Traditional VLN models often rely on navigation graphs, 360-degree views, and perfect localization which pose significant challenges when adapting these models to real-world settings. This work addresses these limitations by performing a simulation-to-real domain shift of a VLN approach that operates in continuous environments without req...
  </details>

- **2026-10-05** — Yun Jiang, Bo Zheng, Yingying Zhang et al. — [MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs](http://arxiv.org/abs/2610.07110v1)
  <details><summary>📄 Abstract</summary>
  High-quality 3D reconstruction of lunar terrain from sparse rover images is indispensable for autonomous lunar exploration, but remains challenging because viewpoint overlap is insufficient, surface textures are weak, and data volume is limited. We propose MoonGS, the first feed-forward 3D Gaussian Splatting framework tailored to lunar scenes. Given only two input images, MoonGS predicts pixel-aligned Gaussian primitives in a single forward pass and renders photorealistic novel views without any...
  </details>

- **2026-10-05** — Suzannah Wistreich, Stephen Tian, Isabella Huang et al. — [MobileVISTA: Generative Data Augmentation for Pose Generalization in Mobile Manipulation](http://arxiv.org/abs/2610.07511v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulators such as humanoid robots are increasingly deployed in dynamic, unstructured environments to perform dexterous manipulation tasks. However, end-to-end manipulation policies trained to imitate demonstration data collected from a single robot pose are brittle: even centimeter-scale deviations in robot pose at deployment can drive ego-centric observations and end-effector trajectories out of the training distribution, leading to sharp drops in performance. We introduce MobileVISTA...
  </details>

- **2026-10-05** — Yan Scholten, Rachel Lawrence, James Hensman et al. — [Activation Denoising: A Robustness View on Parallel vs Sequential LLM Quantization](http://arxiv.org/abs/2610.07522v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization is a powerful tool for compressing large language models. The most scalable methods quantize every layer in parallel, but quantization errors then compound through the residual stream, as no layer corrects for the errors of the layers before it. Sequential quantization accounts for this error compounding by re-calibrating each layer on the already-quantized outputs of its predecessors, yielding stronger results but at the cost of a serial schedule that becomes a bottle...
  </details>

- **2026-10-05** — Yihan Liu, Sarah H. Q. Li — [Linear Occupancy Homomorphisms for Discounted Markov Decision Processes](http://arxiv.org/abs/2610.07441v1)
  <details><summary>📄 Abstract</summary>
  We introduce linear occupancy homomorphisms (LOHs), a class of Markov decision process (MDP) transformations that defines the MDP homomorphism over the feasible occupancy measure space of MDPs. In contrast to classic MDP homomorphism frameworks, which are defined through mappings over the state and state-action spaces, LOHs map between occupancy measure spaces and are representable as linear transformation matrices that expose important structural properties of the homomorphism itself. For this ...
  </details>

- **2026-10-05** — Tomas Kaljevic, Ivan Arzola, Yu Zhang — [Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty](http://arxiv.org/abs/2610.07232v1)
  <details><summary>📄 Abstract</summary>
  Accurate short-term load forecasting (STLF) is essential for the reliable and efficient operation of modern power systems. While time series foundation models (TSFMs) have recently demonstrated remarkable performance across a wide range of forecasting tasks, their effectiveness for STLF under realistic operational conditions remains largely unexplored. In this paper, we present a comprehensive benchmark of four trained-from-scratch (TFS) models and four TSFMs across three real-world load forecas...
  </details>

- **2026-10-05** — Xin Teng, Muxiao Li, Hongyi Wen — [Distributionally Robust Mixture-of-Experts Training](http://arxiv.org/abs/2610.07207v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) transformers scale capacity by activating only a few experts per token, but this sparsity creates a hidden reliability problem: when routing is imperfect, load-balanced models may send tokens to experts that are insufficiently trained for the assigned inputs. We propose Distributionally Robust MoE Training (DRMoET), a drop-in objective that treats layer-wise experts as endogenous robustness groups and optimizes high-loss routing outcomes rather than merely equalizing tra...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-10-06** — Mariya Miteva, Maria Nisheva-Pavlova — [Evidence-Bound Reasoning: Neuro-Semantic Verification of Biomedical AI in Glioblastoma Radiogenomics](http://arxiv.org/abs/2610.08660v1)
  <details><summary>📄 Abstract</summary>
  Background: Biomedical AI can generate plausible explanations without reliably verifying whether each statement is supported by patient-specific evidence. We developed a neuro-semantic verification framework that converts radiomic measurements into addressable evidence records and machine-checkable claims. Methods: UPenn-GBM radiomics were aligned with de novo CaPTk extraction from standardized MRI and expert-validated segmentations in an independent multicenter cohort. The shared space comprise...
  </details>

- **2026-10-06** — Guangyi Liu, Yong Liu, Jiangning Zhang — [nanoMuse: An Open-Source Personal Agent for Every Device You Own](http://arxiv.org/abs/2610.08699v1)
  <details><summary>📄 Abstract</summary>
  Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This rep...
  </details>

- **2026-10-06** — Lasse B. Strand, Robert Jakob, Kevin O'Sullivan et al. — [Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents](http://arxiv.org/abs/2610.08452v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) is a widely used approach for grounding large language models (LLMs) in external knowledge. However, configuring a pipeline is an expensive hyperparameter optimization problem over many interacting choices, from chunking and embedding model to reranking and generation. Existing optimizers, from greedy search to Bayesian optimization, reduce each trial to an aggregate score and search without modeling why a configuration performed as it did, even though the re...
  </details>

- **2026-10-06** — Yacine Benihaddadene, Milan Bhan, Eliot Dugelay et al. — [TICDA: Tabular In-Context Data Attribution](http://arxiv.org/abs/2610.07996v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) achieve strong predictive performance by conditioning on labeled demonstrations provided in context, without any parameter update. Yet how individual demonstrations shape a given prediction remains poorly understood. This gap matters in practice: the context is often assembled from whatever labeled data is available, potentially leading to the inclusion of mislabeled, redundant, or low-quality examples that degrade performance. Standard data attribution methods d...
  </details>

- **2026-10-06** — Hongzhan Lin, Shidong Cao, Ziyang Luo et al. — [From Evidence to Action: How Tool-Using Agents Fail](http://arxiv.org/abs/2610.07753v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents make consequential changes to external state, yet correct outcomes do not guarantee that their actions were supported by evidence established beforehand. We study where this evidence-to-action chain breaks as agents move from deciding whether to act to executing single actions and dependent workflows. Across ten model-harness configurations, strong static action assessment can coexist with much weaker interactive execution. Failures often begin before execution: agents stop wit...
  </details>

- **2026-10-06** — Chen Chen, Dongjie Wang, Mei Liu et al. — [Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence](http://arxiv.org/abs/2610.07739v1)
  <details><summary>📄 Abstract</summary>
  Post-discharge risk prediction from electronic health records (EHRs) is difficult because many dependencies that link discharge-time observations to downstream complications, such as comorbidity cascades and drug-disease interactions, are absent from the record. External medical knowledge graphs (KGs) can supply these missing dependencies, but tracing them demands three properties: KG exploration must remain cost-bounded, retrieved evidence must be differentiated by source quality, and the resul...
  </details>

- **2026-10-05** — Pratyay Dutta, Kowshik Thopalli, Vivek Narayanaswamy — [COMPASS: Finding Where Reasoning Lives in Language Models](http://arxiv.org/abs/2610.07469v1)
  <details><summary>📄 Abstract</summary>
  Explicitly eliciting reasoning substantially improves LLM performance. Existing approaches require a predefined characterization of reasoning, whether through CoT prompt design, contrastive CoT directions, or via SAE derived reasoning features. For mathematical reasoning with verifiable answers, we show that a much simpler signal suffices, which is the correctness of the model's own direct answer attempts. This signal yields a latent direction that elicits reasoning. This direction is decodable ...
  </details>

- **2026-10-05** — David I. Atkinson, Dillon Plunkett, David Bau — [Identifying Introspection From the Inside](http://arxiv.org/abs/2610.07186v1)
  <details><summary>📄 Abstract</summary>
  Large language models make claims about themselves that are both consequential and increasingly difficult to verify from behavior alone. How can we distinguish plausible confabulations from genuine introspection? In this paper, we identify mechanistic signatures of faithful self-report in a controlled setting. Using low-rank adapters, we train models to make decisions on behalf of fictitious characters, according to latent linear preference functions. We find sustained fine-tuning on an implicit...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-06** — Hwiyeong Lee, Hyelim Lim, Ingyu Bang et al. — [How Learning Governs Unlearning across the Memorization-Generalization Spectrum](http://arxiv.org/abs/2610.08577v1)
  <details><summary>📄 Abstract</summary>
  While unlearning seeks to negate undesired capabilities acquired through learning, little research has examined how the way models learn shapes their subsequent unlearning. In this paper, we investigate this connection from the perspectives of memorization and generalization, the two most representative yet competing strategies that models employ during training. We first classify memorization- and generalization-heavy models using grokking in modular addition and compare their responses to unle...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-10-06** — Haoyu Huang, Zhongwei Xie, Jiaxin Bai et al. — [Towards In-Parameter Memory Augmentation for Large Language Models](http://arxiv.org/abs/2610.08630v1)
  <details><summary>📄 Abstract</summary>
  Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. \textbf{In-parameter memory} offers a complementary substrate: reusable memory information is represented in mo...
  </details>

- **2026-10-06** — Viraj Bagal, Raviraja Ganta, Prabhath Chellingi — [Same Feedback, Different Answer: Measuring Run-to-Run Instability in Frontier-Model Customer Feedback Analysis](http://arxiv.org/abs/2610.08036v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly being programmed to automate knowledge work over large collections of unstructured data. Such automation requires repeatability: when the underlying evidence is unchanged, the agent's categories, priorities, and counts should not shift materially between runs, even if each individual answer appears plausible. We introduce a repeat-run evaluation framework that aligns semantically equivalent categories and focuses on two operating metrics: theme churn, the normalized ch...
  </details>

- **2026-10-06** — Kevin Lee — [CETUS: How Far Do Representations Trained on Earth Transfer to Cassini SAR of Titan?](http://arxiv.org/abs/2610.07576v1)
  <details><summary>📄 Abstract</summary>
  Cassini synthetic aperture radar (SAR) images reveal the dunes, plains, and lake basins of Titan, providing an instance of representations learned from Earth imagery for planetary terrain classification. Cross-domain Evaluation of Earth-to-Titan Transfer Using SAR (CETUS) compares features from DINOv2, DOFA and CROMA with classical image measurements and features from an untrained vision transformer on the U.S. Geological Survey's Cassini SAR mosaic. The classifiers learn terrain labels from an ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 170 papers

- **2026-10-06** — Chenyu Zhang, Rohit Parasnis, Saurabh Amin — [Network Intervention by Polling Strategic Agents](http://arxiv.org/abs/2610.08347v1)
  <details><summary>📄 Abstract</summary>
  A planner in a network of strategic agents faces three entangled challenges: the optimum depends on agents' private information, queried agents may misreport to steer the outcome, and exact computation does not scale. We study these challenges in multi-activity network games with heterogeneous private technologies, in which the planner sets non-discriminatory prices. We show that the optimal prices admit a centrality-based decomposition of the welfare kernel: each agent's contribution scales wit...
  </details>

- **2026-10-06** — Thiago Santos de Moura, Fynn Matuschek, Flavio Toffalini et al. — [Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code](http://arxiv.org/abs/2610.08240v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are widely used to generate code. Although their functional plausibility keeps improving, the generated code often contains security vulnerabilities. The functionality-security gap captures code that passes functional tests but fails security tests. A recent longitudinal study of three model families concluded that LLMs become smarter but not safer, with the only considered open-weight family stagnating. Whether this holds for other (open-weight) families and particu...
  </details>

- **2026-10-06** — Weiwei Qi, Chongyu Wang, Tianhang Zheng et al. — [ASCENT: First-Order Optimal Fine-Tuning with Recalibration for Safety--Utility Co-Enhancement](http://arxiv.org/abs/2610.08061v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning can substantially improve the downstream utility of large language models (LLMs) but may compromise their safety. Existing safety-preserving methods constrain downstream updates using safety-related parameters or subspaces, but mainly focus on safety preservation rather than joint safety and utility enhancement, lack a theoretical characterization of the optimal safety-related subspace and safety-preserving task update, and typically rely on a static safety subspace that m...
  </details>

- **2026-10-06** — Fernando Martinez, Tao Li, Yingdong Lu et al. — [Independent Multi-Agent Reinforcement Learning with Counterfactual Semantic-Social World Models](http://arxiv.org/abs/2610.07704v1)
  <details><summary>📄 Abstract</summary>
  Fully decentralized multi-agent reinforcement learning (MARL), also referred to as independent learning, requires each agent to learn and act using only its local information and experience, without a centralized critic or inter-agent communication. Such a stringent information structure renders the conventional reward signal ambiguous. A poor return may result from an ineffective ego action, an incompatible teammate response, or an effective opponent response, yet scalar rewards alone do not re...
  </details>

- **2026-10-06** — Zhijun Zhang, Qianlong Wang, Keyang Ding et al. — [Improving Synthetic Data Generation for Argument Mining via Adversarial Reinforcement Learning](http://arxiv.org/abs/2610.07699v1)
  <details><summary>📄 Abstract</summary>
  Argument Mining (AM) is fundamentally constrained by the scarcity of high-quality structure-annotated datasets. While LLMs have shown promise in synthetic data generation, producing synthetic AM data that is both structurally accurate and sufficiently diverse remains a challenging problem. To address this problem, we revisit synthetic data generation for AM from a new perspective and propose a novel adversarial reinforcement learning framework for data synthesis. The proposed framework jointly o...
  </details>

- **2026-10-06** — Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang et al. — [Sherpa: Teaching LLMs to Teach Adaptively](http://arxiv.org/abs/2610.08778v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address t...
  </details>

- **2026-10-06** — Liao Ma, Jiayi Song, Yunfeng Wu et al. — [Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation](http://arxiv.org/abs/2610.08772v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity. However, isolated windows block cross-window interaction, often introducing visible...
  </details>

- **2026-10-06** — Zewei Zhou, Rachel Luo, Yulong Cao et al. — [VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning](http://arxiv.org/abs/2610.08761v1)
  <details><summary>📄 Abstract</summary>
  Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales ve...
  </details>

- **2026-10-06** — Sayan Banerjee — [Metastability and Sharp Propagation-of-Chaos Thresholds for Mean-Field Interacting Diffusions on the Circle](http://arxiv.org/abs/2610.08755v1)
  <details><summary>📄 Abstract</summary>
  We study metastability and long-time propagation-of-chaos for mean-field interacting diffusions on the circle with multiple local free-energy minima. Working modulo rotations, we identify sharp exponential time scales for metastability and the validity and breakdown of the McKean-Vlasov approximation. Assuming finitely many critical rotation orbits and distinct local-minimum energies, we show that, for initial data in the attraction basin of a nonglobal minimum, metastability and propagation-of-...
  </details>

- **2026-10-06** — Chuhong Xu, Bo Su, Ziyao Chen et al. — [Same-Number Citation Swaps: Stress-Testing Jev as a Financial Evidence Judge](http://arxiv.org/abs/2610.08675v1)
  <details><summary>📄 Abstract</summary>
  Financial reports repeat values across periods, metrics and accounting lines, allowing an LLM-generated calculation to be numerically correct while citing the wrong financial role. We evaluate what probabilistic evidence verification adds beyond number matching using Jev as a source-support verifier for GPT-4.1-mini calculation traces. A signed-number-at-pointer baseline explains most recovery over exact quotation checks. To isolate the remaining role-recognition problem, we hold operands and ar...
  </details>

- **2026-10-06** — Yuhao Qin, Junbo Wang, Yuke Li et al. — [EC-RAG: Event Chain Retrieval-Augmented Generation for Long Video Understanding](http://arxiv.org/abs/2610.08674v1)
  <details><summary>📄 Abstract</summary>
  Current large video-language models (LVLMs) still face challenges when dealing with long videos, mainly because frames are often processed independently, making it difficult to capture temporal dependencies across events. Although retrieval-augmented approaches have been introduced to provide additional context, most of them operate at the frame or snippet level, which limits their ability to model how events evolve over time and relate to each other. In this paper, we propose Event Chain Retrie...
  </details>

- **2026-10-06** — Suxin Ji, Hungtao Wan, Mingjun Liu et al. — [Selective Transfer of RL Updates for Visual Reasoning](http://arxiv.org/abs/2610.08659v1)
  <details><summary>📄 Abstract</summary>
  Model merging provides a training-free way to transfer reasoning capabilities from language models to vision-language models (VLMs), but endpoint-based transfer can conflate pre-existing model differences with changes acquired during reasoning post-training. We instead formulate capability transfer around the training-stage update, isolating the parameter changes induced by reinforcement learning (RL). Yet transferring this update in full remains suboptimal: we find that its components differ su...
  </details>

- **2026-10-06** — Marcel Crasmaru — [CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution](http://arxiv.org/abs/2610.08592v1)
  <details><summary>📄 Abstract</summary>
  CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives. It takes a physics-native stance: a network is a cascade of complex -- and often unitary (the DFT) -- operations acting on an amplitude vector, and classification is a Born-rule measurement $p_k = |z_k|^2 / \|z\|^2$ rather than a softmax over real logits. Every layer ships a CP...
  </details>

- **2026-10-06** — Sujato Dutta, Sreekruthy Tummala, Shashank Vanga et al. — [MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory](http://arxiv.org/abs/2610.08586v1)
  <details><summary>📄 Abstract</summary>
  Long conversational agents have become essential in our daily lives. They must remember what was said long back in order to help us efficiently complete a task without needing the user to repeat instructions and context repeatedly. However, the main issue is that instructions and context change over time and so the agents must be able to adapt accordingly. A useful memory system should preserve both current and historical states, distinguish stale information from active knowledge, retrieve evid...
  </details>

- **2026-10-06** — Stephanie Buttigieg, Maeve Madigan, Parameswaran Kamalaruban et al. — [Latent space bias directions in LLMs capture confidence, not fairness](http://arxiv.org/abs/2610.08559v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has gained popularity as a lightweight inference-time debiasing technique for large language models. However, prior work reports that steering vectors generalise poorly, with unintended effects on model performance and limited transfer to new datasets. Our work analyses what the debiasing direction used for activation steering actually encodes, in order to shed light on its inconsistent performance. We study the linear debiasing direction obtained by contrasting the activatio...
  </details>

- **2026-10-06** — Asim Khan, Samee Ullah Khan, Dwarikanath Mahapatra — [MedCORE: Criteria-Grounded Clinical Reasoning for Interpretable Medical Image Diagnosis](http://arxiv.org/abs/2610.08528v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnosis is inherently a structured reasoning process, yet existing deep learning models often bypass this structure by mapping image features directly to disease labels without explicitly interrogating the morphological and textural criteria that clinicians systematically evaluate. This limits diagnostic transparency and may compromise safe clinical deployment. We present MedCORE (Medical Criteria-Oriented Reasoning and Evidence), a structured diagnostic framework that operationalizes...
  </details>

- **2026-10-06** — Baihan Lin — [Language-model ratings of depression reflect the rater more than the patient](http://arxiv.org/abs/2610.08501v1)
  <details><summary>📄 Abstract</summary>
  Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver o...
  </details>

- **2026-10-06** — Maryam Baizhigitova, Andrew Seohwan Yu, Po-Hao Chen et al. — [Knee3DVLM: Dual-Sequence Full-Volume Vision-Language Modeling for Comprehensive Knee MRI Assessment](http://arxiv.org/abs/2610.08482v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly being applied to three-dimensional medical imaging, but their application to knee MRI remains limited, particularly for interpreting the complementary sequences used in clinical practice. We introduce Knee3DVLM, a sequence-aware VLM that uses full-volume DESS and fluid-sensitive TSE MRI to predict 57 anatomically resolved binary diagnostic targets derived from the MRI Osteoarthritis Knee Score (MOAKS) for structured reporting. We evaluated DESS-only...
  </details>

- **2026-10-06** — Rongcun Wang, Shi Chen — [RAPO-Sol: Retrieval-Augmented Preference Optimization for Repository-Level Solidity Code Generation](http://arxiv.org/abs/2610.08429v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts written in Solidity manage assets, permissions, and irreversible state changes, making code generation both useful and security-critical. Repository-level Solidity generation is challenging because models must synthesize complete contracts or libraries while preserving consistency across state variables, modifiers, events, inheritance, external calls, and access-control logic. We present RAPO-Sol, a two-stage training framework for repository-level Solidity code generation. First...
  </details>

- **2026-10-06** — Toby D. Pilditch, Konstantinos Voudouris, Alexandra Abbas et al. — [Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations](http://arxiv.org/abs/2610.08364v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI evaluations increasingly use open-ended, agentic, long-horizon tasks whose transcripts can span hundreds of pages of outputs and actions from complex multi-agent networks. The observability envelop-the range of what evaluators can reliably infer about an agent's behaviours-is therefore narrowing. Language model assistants can help classify and interpret agent behaviour but also afford human evaluators significant analytical degrees of freedom, threatening the reproducibility and audi...
  </details>

- **2026-10-06** — Hun Park — [MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization](http://arxiv.org/abs/2610.08330v1)
  <details><summary>📄 Abstract</summary>
  Proprietary Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks, yet aligning their outputs with diverse user preferences remains challenging. Existing personalization approaches for black-box LLMs often rely on user-specific scoring heads, causing the number of personalized parameters to grow linearly with the number of users and requiring additional adaptation for unseen users. To address these limitations, we propose Mixture-of-Facets (MoF), a s...
  </details>

- **2026-10-06** — Srikar Alla, Ali Shiri Sichani, Chi-Ren Shyu — [Quantum Entangled Multimodal Fusion Networks (QEMFN): Resource-Aware Hybrid Vision-Language Fusion via Trainable Entanglement](http://arxiv.org/abs/2610.08216v1)
  <details><summary>📄 Abstract</summary>
  Multimodal vision-language systems typically fuse image and text embeddings through classical operators such as concatenation, attention, bilinear pooling, or tensor interactions. We propose Quantum Entangled Multimodal Fusion Networks (QEMFN), a hybrid quantum-classical framework that introduces parameterized entanglement as a structured inductive bias for multimodal fusion. Pretrained visual and textual features are projected into compact latent spaces, encoded as angle-parameterized quantum s...
  </details>

- **2026-10-06** — Nina Nusbaumer, Iria de-Dios-Flores, Corentin Bel et al. — [STRUCTURALCOST: A controlled reading time dataset for modeling human sentence processing difficulty](http://arxiv.org/abs/2610.08208v1)
  <details><summary>📄 Abstract</summary>
  We introduce STRUCTURALCOST, a self-paced reading dataset of 475 participants and 40,800 observations isolating the processing cost of long-distance subject-verb dependency resolution. We replicate a low-powered psycholinguistic finding at NLP scale, namely that human reading times at the main verb increase with dependency length, driven by syntactic embedding beyond linear distance. Different language models -- spanning n-gram models, SSMs, and transformers -- partially mirror this graded diffi...
  </details>

- **2026-10-06** — Anvi Kalpesh Shah, Umamaheswara Sharma B — [Beyond the Leaderboard: Multi-Dimensional Evaluation of Dense and Mixture-of-Experts Models for Automated Program Repair](http://arxiv.org/abs/2610.08173v1)
  <details><summary>📄 Abstract</summary>
  Automated Program Repair (APR) with language models is usually evaluated by whether a generated patch passes the test suite, which can hide differences in maintainability, security, and computational cost. We propose a Weighted Quality Index (QI), inspired by the ISO/IEC 25010 software quality model, that combines functional correctness, maintainability, security, and generation efficiency under configurable weighting schemes. We evaluate three dense Qwen2.5-Coder models (3B, 7B, 14B) and the 16...
  </details>

- **2026-10-06** — Yiming Qin, Ke Wang, Amel Abdelraheem et al. — [Enhancing Diffusion Language Models with Autoregressive Post-Training Weights](http://arxiv.org/abs/2610.08108v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (dLLMs) have emerged as a promising alternative to autoregressive (AR) language models, offering flexible token-update orders and parallel decoding. Recent dLLMs are often initialized from pretrained AR models before diffusion conversion in order to inherit their learned representations. After the conversion, however, they typically ignore the extensive post-training ecosystem of their AR ancestors. In this work, we show that these existing AR post-training weight updat...
  </details>

- **2026-10-06** — Jike Zhong, Ritwick Chaudhry, Xuanbai Chen et al. — [DSV-Mem: Evaluating Multimodal Memory in Professional Workflows for MLLM Agents](http://arxiv.org/abs/2610.08102v1)
  <details><summary>📄 Abstract</summary>
  Conversational MLLM agents are increasingly expected to assist in professional workflows, from AI research and engineering design to product management and business operations. Yet this capability remains underexplored: existing benchmarks largely focus on informal, everyday interactions and personal-life scenarios featuring photographic natural images, isolated static artifacts, and recall-oriented questions. In contrast, professional scenarios often involve structured, information-heavy artifa...
  </details>

- **2026-10-06** — Remo Grillo, Lukas Klic, Giovanni Colavizza — [Natural Language Questions as an Interface for Knowledge Graphs: QRAKEN Graph Distillation and Semantic Self-Healing](http://arxiv.org/abs/2610.08095v1)
  <details><summary>📄 Abstract</summary>
  Natural-language access to RDF knowledge graphs is a core Semantic Web ambition. Large language models (LLMs) have advanced Text-to-SPARQL, yet on unfamiliar graphs they often generate valid queries that misrepresent the populated data model. QRAKEN is a training-free, ontology-agnostic neurosymbolic pipeline grounding generation in empirical graph evidence rather than schema expectations. An offline distiller produces TTQL, a compact description of populated multi-hop patterns, conditional freq...
  </details>

- **2026-10-06** — Alessandro Cestelli, Spyridon Grountas, Scott Mc Haffie et al. — [Broadband Telecom Entanglement from an All-Fiber Type-0 Sagnac Source](http://arxiv.org/abs/2610.08025v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate a compact, practical all-fiber source of non-degenerate telecom-band polarization-entangled photon pairs assembled from off-the-shelf components. The compact fiber-integrated architecture is designed to be affordable, straightforward to assemble and align, and compatible with existing optical-fiber infrastructure. Photon pairs are generated through type-0 spontaneous parametric down-conversion in a pigtailed periodically poled lithium-niobate waveguide embedded in a Sagnac interfe...
  </details>

- **2026-10-06** — Minseok Moon, Wonjun Choi, Seungwu Han et al. — [Defect-limited thermal transport in AlN using pretrained machine-learning interatomic potentials](http://arxiv.org/abs/2610.08013v1)
  <details><summary>📄 Abstract</summary>
  Aluminum nitride (AlN) is an important thermal management material whose high lattice thermal conductivity is strongly suppressed by oxygen impurities. We investigate phonon scattering by oxygen-related defects using pretrained universal machine-learning interatomic potentials (MLIPs), molecular dynamics (MD), and phonon Boltzmann transport calculations. Several pretrained MLIPs are benchmarked against density functional theory for phonon dispersions and pristine thermal conductivity. To balance...
  </details>

- **2026-10-06** — Xiong Li, Xiaowei Zhou, Yanwei Yu et al. — [Textual Environmental Context and Spatial Graphs for LLM-Based Regional SST Forecasting](http://arxiv.org/abs/2610.07895v1)
  <details><summary>📄 Abstract</summary>
  Sea surface temperature (SST) forecasting depends on local temporal persistence, regional spatial dependence, and environmental conditions that evolve with the forecast date. We study how these heterogeneous conditions can be presented to a large language model (LLM) for regional multi-step forecasting without serializing the full SST grid as text. We formulate forecasting as conditional numerical generation: historical SST and anomaly sequences, date-aligned environmental records, and static oc...
  </details>

- **2026-10-06** — Dayan Pan, Jingyuan Wang, Xie Yu — [Dynamic Positional Attention Modulation for Parameter-Efficient Fine-Tuning of Large Language Models](http://arxiv.org/abs/2610.07848v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) has become a standard approach for adapting large language models to downstream tasks. However, most existing PEFT methods rely on uniform and static adaptations, without accounting for the structured heterogeneity of attention across dimensions, heads, layers, and input tokens. In practice, attention representations exhibit non-uniform behavior, and positional encoding mechanisms such as rotary positional embeddings (RoPE) induce dimension-dependent positi...
  </details>

- **2026-10-06** — Ravenor Davion, Nick Rui — [Privileged Context as Drift in On-Policy Self-Distillation](http://arxiv.org/abs/2610.07842v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) trains a language model to match a copy of itself conditioned on privileged context. Existing work varies what privileged context contains and how it is produced while also changing models, data, and training setups, making the effects of privileged context design difficult to isolate. Motivated by efforts in continual learning to reduce catastrophic forgetting, we study how the choice of privileged context affects policy drift. Specifically, we vary two axes: ...
  </details>

- **2026-10-06** — Abolfazl Younesi — [Do I Need the Cloud? Uncertainty-Aware Step-Level Handoff for Small Language Model Agents](http://arxiv.org/abs/2610.07816v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) are attractive as local agent controllers because they reduce remote inference, latency, and deployment footprint, yet structured tool errors can cause an agent step to fail. Existing routers typically select a model once per query. However, agents expose sequential decision points whose difficulty dynamically changes based on intermediate observations. We propose STEPGATE, an uncertainty-aware handoff framework that scores each local SLM action and selectively escal...
  </details>

- **2026-10-06** — Gyusik Seo, Jaehong Yoon — [Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents](http://arxiv.org/abs/2610.07785v1)
  <details><summary>📄 Abstract</summary>
  A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon task execution. In such settings, each task begins from the state left by the previous one: the agent may end at a different position and orient...
  </details>

- **2026-10-06** — Farbod Tavakkoli, Gregory Diamos, Kenneth Church et al. — [OTel: Open Telco AI Datasets, Benchmarks, and Models](http://arxiv.org/abs/2610.07766v1)
  <details><summary>📄 Abstract</summary>
  We present Open Telco (OTel), an open telecom AI resource that releases derived telecom datasets for retrieval, reranking, instruction tuning, and safety/abstention, together with 30 full-parameter post-trained baselines spanning 10 embedding models, 3 rerankers, and 17 language models. The community has already engaged substantially with the resource: as of May 3, 2026, the released models have been downloaded over 16 million times and the project has received 157+ pieces of media coverage worl...
  </details>

- **2026-10-06** — Wanning He, Yuyao Zhang, Yu-Wing Tai — [RefRoute: Decoupling Conditioning Cost from References via Compact Residual Conditioning and Spatial Routing](http://arxiv.org/abs/2610.07720v1)
  <details><summary>📄 Abstract</summary>
  Multi-reference image generation requires preserving the appearance of multiple subjects while composing them into a coherent scene. However, existing diffusion transformers commonly encode references as dense visual token grids and jointly process them with global attention, making conditioning increasingly expensive as the number and resolution of references grow. We present RefRoute, a framework that addresses both reference representation cost and attention overhead through two complementary...
  </details>

- **2026-10-06** — Shreya Rajpal, Sonia Sharma, Swapnil Parekh et al. — [Evidence Before Sampling: Interpretable Implicit Negative Candidate Discovery for Recommendation](http://arxiv.org/abs/2610.07708v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems learn from observed user-item interactions, but explicit negative feedback is often unavailable. Since deep learning models require negative signals for training, negative sampling methods typically treat selected unobserved interactions as negatives. However, a missing interaction does not explain why a user is uninterested in an item or whether there is sufficient evidence to label it negative. This is especially important in business recommendation, where negative signals ...
  </details>

- **2026-10-06** — Yi Liu, Xianglin Meng, Chang Chen et al. — [Silicon Language: A Robot-Native Knowledge Exchange Framework for Heterogeneous Robots](http://arxiv.org/abs/2610.07650v1)
  <details><summary>📄 Abstract</summary>
  Reusing a capability across heterogeneous robots still requires substantial human adaptation and verification: transferring a skill often means re-engineering interfaces, retuning parameters, and re-validating safety. We introduce Silicon Language, a robot-native knowledge exchange framework that treats the robot as the active subject of its own capability evolution. In this framework, a robot that wants a capability encodes its own experience into knowledge packets, publishes them, retrieves pe...
  </details>

- **2026-10-06** — Hyeongwoo Nam, Woongje Cho, Juwon Kim et al. — [OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning](http://arxiv.org/abs/2610.07649v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based robot task planning is promising for open-ended instruction following, but degrades on long-horizon tasks in large environments. When spatial information is conveyed to the LLM through text, the model can fail to capture spatial context, and token cost grows with environment size. Generating action sequences directly with an LLM also makes it difficult to satisfy the current world state and action preconditions. We address this with an ontology-grounded scene rep...
  </details>

- **2026-10-06** — SiYuan Ma, Canran Xiao, Zikai Xiao et al. — [Linear Fitness Subspace in Protein Language Models Enables Sample-Efficient Directed Evolution](http://arxiv.org/abs/2610.07607v1)
  <details><summary>📄 Abstract</summary>
  Model-guided directed evolution seeks to identify high-fitness protein variants under limited oracle budgets. Protein language models (PLMs) provide rich representations for this task, but task-agnostic zero-shot scores can be misaligned with a target assay, while supervised search in high-dimensional embedding spaces can make surrogate modeling and uncertainty estimation sample-inefficient. We propose the Linear Fitness Subspace (LFS) hypothesis: within mutation-induced residue-level representa...
  </details>

- **2026-10-06** — Yang Qu, Yusheng Han, Chengjia Feng et al. — [LSC-DPO: Learning-Signal-Controlled Direct Preference Optimization](http://arxiv.org/abs/2610.07592v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has become a standard reward-model-free approach for aligning language models with preference data. However, as the scaled preference margin grows during training, the logistic DPO loss becomes progressively less sensitive to further changes. We study DPO from a loss-level geometric perspective and identify the sigmoid factor as a learning signal that characterizes the local sensitivity of the objective. Based on this view, we propose Learning-Signal-Controll...
  </details>

- **2026-10-06** — Chung Min Kim, Brent Yi, David McAllister et al. — [QF3: Fast Flow RL with Filtered Q-Gradients](http://arxiv.org/abs/2610.08789v1)
  <details><summary>📄 Abstract</summary>
  Flow policies have become a standard policy class for learning robot behaviors from demonstrations, but reinforcement learning is still critical for improving pre-trained flow policies or learning them from scratch through interaction. We introduce QF3 (Fast Flow RL with Filtered Q-Gradients), an online off-policy RL algorithm that trains a flow policy with flow matching plus the critic's action gradient, backpropagated through a one-step prediction of the flow's output. To keep updates where th...
  </details>

- **2026-10-06** — Zhenghong Zhou, Zhe Lin, Jiebo Luo et al. — [ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing](http://arxiv.org/abs/2610.08779v1)
  <details><summary>📄 Abstract</summary>
  Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered, model-generated, and real-world videos with general editing pairs from ROSE. Each pair differs i...
  </details>

- **2026-10-06** — Hanjun Luo, Xiucheng Zhang, Zhuoning Xu et al. — [ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding](http://arxiv.org/abs/2610.08662v1)
  <details><summary>📄 Abstract</summary>
  As coding agents increasingly undertake real-world work autonomously, judging whether their risk treatments are warranted has become important. Existing work evaluates related agent behaviors from separate perspectives, but lacks a systematic framework for unifying these behaviors. To bridge this gap, we introduce ParanoiaEval, the first benchmark for unified evaluation of risk-treatment capabilities in coding agents. Grounded in the well-established Avoidance-Transfer-Mitigation-Acceptance fram...
  </details>

- **2026-10-06** — Yurun Chen, Josh Qixuan Sun, Jason Qin et al. — [HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots](http://arxiv.org/abs/2610.08642v1)
  <details><summary>📄 Abstract</summary>
  Contact with contaminated objects can spread hazards through a household robot's grippers, tools, and shared surfaces, while new contacts can make an existing plan unsafe. Existing benchmarks do not jointly assess how planners identify hygiene risks from contact history and plan safe continuations after new contact events. Planners must do so within time and resource limits while respecting user priorities. We introduce HygieneRoboBench, with 624 instances across 134 task families, to evaluate s...
  </details>

- **2026-10-06** — Zijia Chen, Yuenan Hou, Yu Li et al. — [Towards Efficient Robotic Manipulation Models with Self-Recursive Pruning](http://arxiv.org/abs/2610.08555v1)
  <details><summary>📄 Abstract</summary>
  Network pruning can reduce parameter redundancy in robotic policies. However, generic pruning criteria are tailored for image recognition tasks and commonly designed to preserve weight magnitude, local reconstruction, or language-model likelihood rather than closed-loop action behavior. Directly applying these pruning algorithms to robotic tasks yields unsatisfactory performance. In this paper, we propose Loss-Conditioned Activation-Moment (LCAM) pruning, a training-free method for unstructured ...
  </details>

- **2026-10-06** — Hyun Jung Lee, Jungtaek Kim, Jongwon Jeong et al. — [EMHO: EMbodied Agent Harness Optimization via Experience Traces](http://arxiv.org/abs/2610.08432v1)
  <details><summary>📄 Abstract</summary>
  Improving embodied agents often focuses on optimizing the underlying model through training, while the surrounding agent harness that controls planning, context, and tool use is typically engineered. We ask whether this harness can instead improve itself directly from experience traces under sparse environmental feedback. We propose EMbodied Agent Harness Optimization (EMHO), a self-evolving framework that keeps the embodied model frozen and iteratively revises its harness by analyzing execution...
  </details>

- **2026-10-06** — Haegu Lee, Christoffer Sloth — [Post-Grasp Kinematic Repair for Robotic Insertion via Object-in-Gripper Reorientation](http://arxiv.org/abs/2610.08421v1)
  <details><summary>📄 Abstract</summary>
  A stable grasp does not guarantee kinematically feasible robotic insertion because the object-in-gripper transform may force the robot towards singularities or joint limits along the prescribed insertion path. We study post-grasp kinematic feasibility repair through object-in-gripper reorientation. Given an achieved grasp and a fixed insertion path, we seek a small reorientation that restores kinematic feasibility. Sequential IK can miss such candidates by following an unfavorable joint-space pa...
  </details>

- **2026-10-06** — Fengkai Liu, Hao Su, Haozhuang Chi et al. — [Event-Driven Proactive Robot Assistance through Vision-Language Reasoning](http://arxiv.org/abs/2610.08344v1)
  <details><summary>📄 Abstract</summary>
  Assistance in collaborative manipulation is often initiated by user instructions, making high-level reasoning request-driven. In fluent human teamwork, however, partners often infer the next helpful step from the observed outcome of an action rather than waiting for instructions. Motivated by this, we investigate an event-driven formulation of proactive assistance, where human--object interaction outcomes initiate assistive reasoning without user-provided task specifications at inference time. T...
  </details>

- **2026-10-06** — Nanhe Chen, Runqiu Yang, Jiawei Tang et al. — [Compact Robot Policies Need Fine-Grained Visual Representations](http://arxiv.org/abs/2610.08183v1)
  <details><summary>📄 Abstract</summary>
  Multi-task manipulation policies differ in architecture, scale, and pretrained priors all at once, so published comparisons cannot attribute performance to any single component. We argue that most of it comes from the visual representation, and that parameter scale and generative priors are largely incidental. To test this, we build CoRP (Compressed Representation Policy), a deliberately compact policy (48.9M parameters, no vision-language model and no video-generative prior) that factorizes int...
  </details>

- **2026-10-06** — Owen Du, Yang Yue, Jie Zhang et al. — [VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models](http://arxiv.org/abs/2610.08133v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur high computational costs from processing long token sequences at every control step, limiting real-time deployment. Visual token pruning offers a direct solution, as visual patches dominate the input sequence and contain considerable redundancy. Existing approaches, however, either rely on indirect training-free heuristics, such as attention scores and motion thresholds, or require costly fine-tuning of...
  </details>

- **2026-10-06** — Yikai Qin, Yifei Deng, Mingjian Liang et al. — [EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation](http://arxiv.org/abs/2610.07969v1)
  <details><summary>📄 Abstract</summary>
  Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce EmbodiedSmith, a framework for scalable embodied data generation through recursive self-improvement (RSI). EmbodiedSmith unifies asset, scene, ...
  </details>

- **2026-10-06** — Deogyong Kim, Sunghwan Kim, Sangam Lee et al. — [From Delivery to Stateful Exploration: Rethinking the Index for Agentic Search](http://arxiv.org/abs/2610.07960v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic search have given large language model (LLM) agents finer control over corpus exploration. However, search interfaces often return matching passages even when feedback about the candidate set would suffice for the next decision, coupling candidate refinement with source-text exposure. We propose IndexAct, an interface for Index-Native Corpus Interaction that separates candidate-set refinement from text inspection. Agents construct and manipulate persistent candidate se...
  </details>

- **2026-10-06** — Jicong Ao, Shuhan Jiang, Yuling Zhong et al. — [SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining](http://arxiv.org/abs/2610.07652v1)
  <details><summary>📄 Abstract</summary>
  The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limited articulated-object categories, while general-purpose synthesis pipelines lack explicit designs for part-level semantics and articulation c...
  </details>

- **2026-10-06** — Kazutoshi Tanaka — [TacZero: Training-Free Peg Insertion Using a General-Purpose Vision-Language Model with Tactile Feedback](http://arxiv.org/abs/2610.07621v1)
  <details><summary>📄 Abstract</summary>
  Robots that autonomously determine their actions from language instructions and sensory observations could perform new contact-rich manipulation tasks without task-specific training or hand-designed rules. To perform these tasks, robots must infer how objects contact one another and move as a result, then select actions. For contact inference and action selection, prior approaches involve designing estimation models and tactile feedback control laws, or learning models for object-motion estimati...
  </details>

- **2026-10-06** — Zexi Zhang, Zecheng Zhu, Zidong Chen et al. — [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](http://arxiv.org/abs/2610.07594v1)
  <details><summary>📄 Abstract</summary>
  Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchronised multi-camera views and full-body execution records. We benchmark vision-language-action fine-tuning, imitation learning, demo-driven rei...
  </details>

- **2026-10-06** — Muhammad Faraz Shoaib, Muhammad Qasim, Raisulhaq Mohammed Rizwan et al. — [LOGIC: An LLM Benchmark for Intent-Grounded Change Impact in Aerospace Electrical Systems](http://arxiv.org/abs/2610.07580v1)
  <details><summary>📄 Abstract</summary>
  Aerospace electrical-design revisions can contain multiple genuine changes, although an engineering request may authorize only a subset. Propagating every detected difference can therefore produce overly broad impact reports. We present LOGIC, a controlled benchmark and evaluation framework in which locally deployable language models ground a request in a deterministic candidate-change inventory before selected changes are propagated through a typed electrical traceability graph. This separation...
  </details>

- **2026-10-06** — Casey Kennington, Ross Mead, Saad Elbeleidy et al. — [Towards an Extensible Benchmark for Spoken Dialogue with Social Robots](http://arxiv.org/abs/2610.08733v1)
  <details><summary>📄 Abstract</summary>
  Language models provide a plug-and-play interface between humans and robots, but important challenges remain when speech, dialogue, fast interaction, and collaboration are required. We propose a benchmark for the community to use as a way to explore common spoken dialogue artifacts between robots and humans, including requests for clarification, interruptions, embodied signals (e.g., head nods or facial cues), and time constraints. We also explain our vision to extend the benchmark for other asp...
  </details>

- **2026-10-06** — Alexandr Grebennikov — [Optimal bound for the polynomial Littlewood-Offord problem](http://arxiv.org/abs/2610.08708v1)
  <details><summary>📄 Abstract</summary>
  We present an exposition of an argument, discovered by GPT-6 Pro, that gives an optimal bound for the polynomial Littlewood-Offord problem. Namely, let $F$ be a degree-$d$ multilinear polynomial that contains $r$ degree-$d$ monomials involving disjoint sets of variables. Then, for i.i.d. Rademacher random variables $ξ_1, \ldots, ξ_n$, we have $\mathbb{P}[F(ξ_1, \ldots, ξ_n) = 0] = O_d(r^{-1/2})$. This improves upon the previous bound of $(\log r)^{O_d(1)} r^{-1/2}$ due to Meka, O. Nguyen, and Vu...
  </details>

- **2026-10-06** — Jiajun Chen, Haoyu Wu, Mingda Jia et al. — [Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness](http://arxiv.org/abs/2610.08621v1)
  <details><summary>📄 Abstract</summary>
  Recent game design agents have made substantial progress in generating playable games. However, program correctness does not ensure an enjoyable experience for players. We present Recursive Game Creator, an experience-oriented harness to advance agentic game development from rough game prototypes into entertaining games. Recursive Game Creator organizes recursive development around four components: Designer, Builder, Player, and Reviewer. The Designer translates user instructions and Reviewer's ...
  </details>

- **2026-10-06** — Ashley E. Bravo-Bravo, Yuchen Zhang, Haralambos Mouratidis et al. — [InterCorrect: Intersection-Aware Correction of Demographic Model Merging for Fair ASR](http://arxiv.org/abs/2610.08604v1)
  <details><summary>📄 Abstract</summary>
  Automatic Speech Recognition (ASR) systems often show uneven performance across demographic groups, and errors can be especially difficult to address for speakers belonging to multiple demographic groups. This work studies demographic-aware model merging for fair Speech-LLM-based ASR. Starting from a SLAM-ASR-based model, we fine-tune only the connector on demographic-specific subsets and merge the resulting subgroup-adapted connectors into a global model. We then identify critical cross-axis de...
  </details>

- **2026-10-06** — Bing Liu, Wenjie Zhou, Chengcheng Zhao et al. — [How Bregman Divergences Shape Shampoo](http://arxiv.org/abs/2610.08534v1)
  <details><summary>📄 Abstract</summary>
  Understanding the principles behind Shampoo has recently guided the development of more effective neural network optimizers. These methods learn a preconditioner by optimizing the Frobenius or Kullback-Leibler (KL) divergence against the gradient second moment. In this work, we investigate how the choice of divergence shapes preconditioning, which remains unclear and blocks further improvements. To do so, we develop a unified Bregman divergence framework that connects all popular divergences, al...
  </details>

- **2026-10-06** — Omer Chor, Aljaž Godec, Oren Raz — [Hamiltonian curl-forces in systems coupled to multiple thermal reservoirs](http://arxiv.org/abs/2610.08423v1)
  <details><summary>📄 Abstract</summary>
  We investigate the statistical mechanics of a system coupled to multiple heat reservoirs at different temperatures, a setting which typically sustains nontrivial circulation. By applying a canonical transformation, we map the system onto that of a particle coupled to a single reservoir yet driven by a deterministic curl-force---a reversible, velocity-independent non-conservative force with non-vanishing curl---that can be described by a Hamiltonian with an anisotropic kinetic energy term. Despit...
  </details>

- **2026-10-06** — Yang Hong, Yajun Yang, Xin Wang et al. — [Foresight-over-Graph: Reasoning Beyond Local Horizons for Knowledge Base Question Answering](http://arxiv.org/abs/2610.08388v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in question answering, yet they still frequently suffer from hallucinations on knowledge-intensive tasks. Knowledge graphs (KGs) provide LLMs with structured, interpretable, and updatable factual grounding, making them a promising external knowledge source for reliable reasoning. However, existing LLM-guided graph reasoning methods typically rely on hop-wise greedy or beam-style pruning during evidence retrieval. Such local decis...
  </details>

- **2026-10-06** — Eunwoo Heo — [Near-diagonal asymptotics and the failure of strong universality in random Čech persistence](http://arxiv.org/abs/2610.08257v1)
  <details><summary>📄 Abstract</summary>
  The strong universality conjecture of Bobrowski and Skraba asserts that, under a prescribed data-dependent additive centering, the empirical laws of log-log transformed persistence ratios of random geometric complexes share a universal limit across sampling models, dimensions, filtrations, and homological degrees. They conjectured a left-skewed Gumbel limit and used it as a null law for testing topological significance. We show that, when the uncentered empirical laws and the centerings have det...
  </details>

- **2026-10-06** — Lingteng Zeng — [Visual Orchestration Tax in Agentic VLM Pipelines: Auditing and Certifying Visual Evidence Reuse](http://arxiv.org/abs/2610.08170v1)
  <details><summary>📄 Abstract</summary>
  Agentic VLM pipelines increasingly pass the same static visual evidence through multiple specialist agents and tools. This design creates an orchestration-level redundancy mode: semantically unchanged images are repeatedly reconstructed as image-conditioned requests at the VLM API boundary. We call this phenomenon visual orchestration tax and develop a measurement-to-certification framework for visual evidence reuse in agentic VLM pipelines. The audit side defines $\mathrm{M1}_{\mathrm{trace}}$ ...
  </details>

- **2026-10-06** — G. L. John Salvin, Swapnil Hingmire — [Making COMET Comparable Across Scripts: Diagnosis and Correction of Tokeniser-Induced Script Bias in Indic MT Evaluation](http://arxiv.org/abs/2610.08159v1)
  <details><summary>📄 Abstract</summary>
  COMET reports translation quality as a single number, and that number is routinely compared across target languages written in different scripts. Such a comparison assumes Script Invariance: the score should not depend on the writing system that carries the target. We test it on IndicMT Eval by re-encoding the target into Latin script, which changes orthographic form while holding content and human ratings fixed. Script identity then accounts for 22.9% of native-script COMET variance, and agreem...
  </details>

- **2026-10-06** — Priyanka Sinha, Nikolaos Kekatos, Stylianos Basagiannis et al. — [Explainable Rule Mining of IPv6 Extension-Header Presence Patterns from Paired-Vantage Captures](http://arxiv.org/abs/2610.08090v1)
  <details><summary>📄 Abstract</summary>
  IPv6 extension headers (EHs), such as fragmentation, segment routing, and in-situ telemetry, are operationally important yetwidely dropped in transit, and characterising their behaviour from packet captures is a recurring measurement problem. We ask whetheran explainable miner can recover human-readable rules of EH behaviour, and we contribute two reusable tools: a negative-control protocol that diagnoses whether a mined "temporal" network rule reflects genuine cross-packet dynamics or mere with...
  </details>

- **2026-10-06** — Joes Biburger, Nicole Megow, Golnoosh Shahkarami — [Online Fair Division under Eligibility Constraints](http://arxiv.org/abs/2610.08064v1)
  <details><summary>📄 Abstract</summary>
  We study fair division of indivisible items under eligibility constraints: each item may be assigned only to a subset of eligible agents. This model coincides with restricted assignment in scheduling, with agents as machines and items as jobs, and captures settings where work or resources must be split among parties with different capabilities. Eligibility makes the usual fairness benchmarks inadequate, as agents should not be measured against items they could never receive. We therefore use eli...
  </details>

- **2026-10-06** — Takanori Ashihara, Kohei Matsuura, Masato Mimura — [HINTT Submission to the 2nd MLC-SLM Challenge: Comparing Cascaded and Unified Approaches to Diarization and ASR](http://arxiv.org/abs/2610.08063v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the HINTT system submitted to the 2nd Challenge and Workshop on Multilingual Conversational Speech Language Model (MLC-SLM). We address multilingual speaker-attributed ASR, where systems must determine who spoke when and what was spoken. We investigate two modeling strategies for this problem: a cascaded pipeline that combines speaker diarization with speech-LLM-based ASR, and a unified speech LLM that directly generates speaker labels, timestamps, and transcriptions. Our fin...
  </details>

- **2026-10-06** — Jinsong Zhang, Kejun Wu, Ming Zhu et al. — [M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding](http://arxiv.org/abs/2610.07982v1)
  <details><summary>📄 Abstract</summary>
  Monocular metric depth estimation and 3D visual grounding represent the two complementary cornerstones of monocular 3D spatial understanding (M3Sun), from which the fundamental 3D spatial information required by M3Sun can be acquired. However, these complementary tasks are generally conducted by separate frameworks, which pose challenges of inflexible and unaligned spatial information access for embodied intelligence systems. In this paper, we propose a unified agent for monocular 3D spatial und...
  </details>

- **2026-10-06** — Chiara Giaquinta, Laura Hernández, David Chavalarias — [Probabilistic neighbors' selection competes with confirmation bias in a bounded confidence model](http://arxiv.org/abs/2610.07971v1)
  <details><summary>📄 Abstract</summary>
  In this work, we investigate three modified versions of the classic Hegselmann-Krause opinion dynamics model, incorporating features that are typical of many real-world systems, such as uncertainty in the selection of interacting agents and a weighted evaluation of the relevance of their opinions in the influence function to enhance confirmation bias. Through extensive simulations across different network topologies, ranging from stylized network models (Barabási-Albert, Erdős-Rényi, and Watts-S...
  </details>

- **2026-10-06** — Brendan King, Farima Fatahi Bayat, Jean-Flavien Bussotti et al. — [Confidence Reasoning Graphs: Structured Confidence Estimation for LLM Agents](http://arxiv.org/abs/2610.07948v1)
  <details><summary>📄 Abstract</summary>
  When using an LLM agent in a consequential domain, making an informed decision about whether to trust its output or intervene requires calibrated confidence in the agent's success. Confidence estimation for agents is difficult because evidence about success is distributed across heterogeneous, interdependent steps of an agent's trajectory. Practical agentic deployments introduce further challenges: frontier LLMs often provide limited access to internal signals, agent roll-outs are costly, and tr...
  </details>

- **2026-10-06** — Ciaran Regan, Kai Arulkumaran, Luke Darlow et al. — [Continuous Memory Machines](http://arxiv.org/abs/2610.07907v1)
  <details><summary>📄 Abstract</summary>
  Recurrent neural networks typically compress information into a single vector-valued recurrent state, forcing short-term computation and long-term retention to share the same representation. Past extensions alleviate this bottleneck by increasing the memory capacity or separating timescales, but lack the combination of rapid neuron-level processing and longer-term retention found in biology. To that end, we introduce the Continuous Memory Machine (CMM), a recurrent architecture with matrix-value...
  </details>

- **2026-10-06** — Miao Xie, Xiao Zhang, Yuan Wang et al. — [ShanLiangRen: A Nutrition Agent for Personalized Daily Meal Planning](http://arxiv.org/abs/2610.07886v1)
  <details><summary>📄 Abstract</summary>
  Dietary nutrition planning plays an important role in chronic disease management and maintaining a healthy body. In applications, it must simultaneously satisfy personalized constraints and reasonable multidimensional nutritional goals. These two aspects often conflict, and user constraints evolve with feedback, resulting in a substantial gap between generic guidelines and executable plans. To bridge this gap, we first propose the personalized fully quantified multiobjective dietary planning pro...
  </details>

- **2026-10-06** — Jeonghwa Lim, Minje Park, Yeongyeon Na et al. — [Label-Efficient Deep Learning for ECG Delineation: A Multi-Dataset Benchmark against Widely Used Delineation Tools](http://arxiv.org/abs/2610.07885v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiogram (ECG) delineation, the identification of waveform boundaries, is a foundational step that translates raw ECG signals into clinically interpretable measurements. Deep learning has advanced this task but remains dependent on costly expert annotations. Label-efficient strategies such as self-supervised pretraining and semi-supervised learning are expected to ease this burden, yet it remains unclear whether they yield reliable delineation and whether the deep models they produce ou...
  </details>

- **2026-10-06** — Sunchan Park, Beomkwon Cho, Kyeongbo Kong — [CueRator: Agentic Search for Symbolic Rules to Adapt Frozen Multimodal Encoders](http://arxiv.org/abs/2610.07868v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have been used to search over symbolic structures such as programs and equations. We propose CueRator, an agentic framework for policy-aware decision-rule discovery, which adapts frozen contrastive multimodal encoders by searching for the decision rule that converts their cross-modal similarities into predictions. We validate it on open-vocabulary audio-visual event perception, where existing methods involve a trade-off between adaptivity and generalization to unseen ...
  </details>

- **2026-10-06** — Sihyeon Lee, Jihun Song, Chanwoo Kim et al. — [OMIT the Action: Measuring Framing-Invariant Omission Bias under Philosophical Disagreement](http://arxiv.org/abs/2610.07847v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly assist in moral reasoning, omission bias, the tendency to prefer inaction even when equivalent framings reverse substantive outcomes, poses a significant risk of skewed decision-making. Yet omission bias remains underexplored in LLM evaluation, with the few existing studies limited in scale and focused largely on utilitarian-deontological conflicts. To address this gap, we introduce OMIT, a benchmark consisting of 218 paired-frame scenarios across 10 conflict types, construc...
  </details>

- **2026-10-06** — Zhongqin Wang, Xiaoqi Zhang, Nan Yang et al. — [Agentic Semantic Sensing for Resource-Adaptive AI-RAN](http://arxiv.org/abs/2610.07829v1)
  <details><summary>📄 Abstract</summary>
  Semantic sensing (SemS) acquires task-relevant information rather than reconstructing complete physical information. Existing SemS formulations typically operate open loop: sensing configurations and observation schedules are fixed before inference and cannot respond to evolving task-level evidence. We propose Agentic SemS, a closed-loop framework for AI-enabled radio access networks (AI-RANs) that controls sensing within a communication-feasible profile set. A profile-conditioned causal Transfo...
  </details>

- **2026-10-06** — Hans Schabert, Christoph Peters — [One Step at a Time: Trading LLM Autonomy for Process Predictability](http://arxiv.org/abs/2610.07817v1)
  <details><summary>📄 Abstract</summary>
  Organizations automating operational processes need more than a correct outcome: they need to predict how a process will run, know which one actually ran, and inspect it step by step. When an agent is the executor that predictability is normally lost: the prescribed procedure goes into the system prompt, and only a final answer comes back. We deliver the procedure step by step over the Model Context Protocol (MCP) instead: a server releases one step at a time, the agent executes it, and each ste...
  </details>

- **2026-10-06** — Saanvi Khetan, Sankar Balasubramanian — [Thin Evidence, Thick Priors: How Language Models Substitute Identity for Missing Financial Facts](http://arxiv.org/abs/2610.07798v1)
  <details><summary>📄 Abstract</summary>
  People increasingly ask large language models what to do with their money, yet seldom describe their finances in full. This paper asks what a model does with the gap. Holding finances fixed and changing only who the investor is said to be, we grade the financial evidence in the prompt from eight facts to none and measure how far the recommended equity allocation moves. Across 96,600 prompts to Llama-3.1-8B-Instruct, built from 100 financial profiles, 138 personas and seven disclosure conditions,...
  </details>

- **2026-10-06** — Catherine Ji, Vivek Myers, Sergey Levine et al. — [The Geometry of Empowerment](http://arxiv.org/abs/2610.07796v1)
  <details><summary>📄 Abstract</summary>
  Empowerment captures the capacity for an agent to actively control its environment. While conceptually appealing as an information-theoretic quantity, the connection between empowerment and structurally central states that provide broad access to future outcomes has remained an open question. In this work, we link empowerment maximization and skill-learning methods to provide new geometries for interpreting and analyzing empowerment. Our analyses answer longstanding open questions on the connect...
  </details>

- **2026-10-06** — Qi Cheng, Rongchao Dong, Shengyu Chen et al. — [ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Generation on Scientific Research Tasks](http://arxiv.org/abs/2610.07763v1)
  <details><summary>📄 Abstract</summary>
  The rapid progress of LLM-based multi-agent systems (MAS) has shown that they largely outperform single agents on coding, math, and QA tasks, where executable tests provide a binary success signal. Whether this advantage transfers to real scientific data analysis remains untested. We introduce ST-Bench, a benchmark designed to answer two questions: whether MAS outperform single agents on complex scientific data analysis tasks, and if so, by how much and at what additional cost. ST-Bench contains...
  </details>

- **2026-10-06** — Emrul Hasan, Chen Ding — [Contrastive Learning for Aspect Representation towards Explainable Recommendation](http://arxiv.org/abs/2610.07761v1)
  <details><summary>📄 Abstract</summary>
  In this work, we propose a novel recommendation model, CLARER (Contrastive Learning for Aspect Representation towards Explainable Recommendation) that integrates aspect features learned from textual reviews with rating information to improve the accuracy and explainability of recommendations. Our proposed framework learns user and item representations by combining rating-based features and aspect-based features from reviews. Specifically, rating-based features are learned through a multi-layer p...
  </details>

- **2026-10-06** — Kaifeng He, Xiaojun Zhang, Zhenxi Chen et al. — [Acquiring and Verifying Repository Norms for Coding Agents](http://arxiv.org/abs/2610.07757v1)
  <details><summary>📄 Abstract</summary>
  Changes produced by coding agents can pass functional tests while leaving repository contribution requirements unmet. Following repository-specific norms requires identifying guidance dispersed across repository sources and interpreting its conditions and exceptions. Retrieval and documentation approaches supply general context, but agents must still determine which norms apply. We introduce RepoNorm to acquire explicit and implicit repository norms independently of coding tasks. It checks norm ...
  </details>

- **2026-10-06** — Feng Luo, Hui Luo, Zhifeng Bao et al. — [Cost-Effective Numerical QA over Semi-Structured Table: Structuring, Resolution, Planning](http://arxiv.org/abs/2610.07749v1)
  <details><summary>📄 Abstract</summary>
  Semi-structured tables encode rich semantic information through diverse layout elements, such as hierarchical row and column headers. Answering numerical questions over such data is challenging because it requires a joint effort of accurate structural understanding of tables, question uncertainty resolution, and complex query intents interpretation. Existing methods are rarely effective in handling the above multifaceted challenges in a holistic manner; moreover, they rely on LLMs without consid...
  </details>

- **2026-10-06** — Mohammad Al-Ratrout, Shayla Sharmin, Roghayeh Leila Barmaki — [Who Is Talking to the Agent? LLMs in Multi-User 3D Virtual Environments](http://arxiv.org/abs/2610.07732v1)
  <details><summary>📄 Abstract</summary>
  When several people share a 3D virtual room with an LLM agent, the agent must decide not only what to say, but whether an utterance was addressed to it and, if accessible, what profile information about the others present it may use. To study both problems, we construct LookAway, a controlled corpus of 40 sessions involving 80 distinct personas and an LLM agent (1,200 turns), including ambiguous-addressee turns in which speaker orientation agrees or conflicts with the intended addressee. Across ...
  </details>

- **2026-10-06** — Fouad Bousetouane — [EIO-Agents: The Missing Semantic Layer for AI Agent Evaluation](http://arxiv.org/abs/2610.07675v1)
  <details><summary>📄 Abstract</summary>
  AI agents are entering production in increasingly consequential environments without a shared semantic standard for what their evaluations actually mean. Scores, traces, judge outputs, and multi juror findings are increasingly used to justify readiness and release decisions, yet they often do not specify what evidence supports a claim, what that evidence can establish, or how the claim leads to a decision. We introduce EIO-Agents, an open specification for interoperable AI agent evaluation built...
  </details>

- **2026-10-06** — Abhijeet Krishnan, Chris Martens — [Towards the Automatic Synthesis of Interpretable Chess Tactics](http://arxiv.org/abs/2610.07640v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art reinforcement learning agents are capable of outperforming human experts at games like chess, Go and StarCraft II. These agents do not simply take advantage of their digital hardware in being able to react and calculate faster than humans, but employ better strategies that lead to more victories. Interpreting these strategies would give human players valuable insight into how to improve their play. In this preliminary work, we propose a symbolic sub-policy model for playing ches...
  </details>

- **2026-10-06** — Abhijeet Krishnan, Colin M. Potts, Arnav Jhala et al. — [Learning Explainable Representations of Complex Game-playing Strategies](http://arxiv.org/abs/2610.07638v1)
  <details><summary>📄 Abstract</summary>
  As part of learning to play complex games, human players develop develop abstractions for concepts and strategies of gameplay consistent with game rules to improve their performance. These concepts are applied to explain other players' actions, and to inform their own actions in-game. Understanding other players' strategies is a crucial part of such improvement, but requires time and effort. In this paper, we propose a strategy similar to human cognition for training RL agents to synthesize lear...
  </details>

- **2026-10-06** — Kautik Mandve, Dileepa Fernando — [Explore, Then Commit: Measurement-Efficient Scientific Law Discovery with Language Models](http://arxiv.org/abs/2610.07620v1)
  <details><summary>📄 Abstract</summary>
  Scientific law discovery requires selecting measurements and converting evidence into a governing equation. We evaluate an explore-then-commit protocol in which a large language model proposes hypotheses, a programmatic planner gathers measurements, and a fresh prompt synthesizes the final law from fixed observations. The protocol combines structured probes, automatic numerical diagnostics, restricted measurement batches, and optional interpreter access. Across 576 NewtonBench trials, we compare...
  </details>

- **2026-10-06** — Yi Xia, Ibrahim Khan, Mury Fajar Dewantoro et al. — [Emoception: Selective Affective Layer Fine-Tuning of Video Vision Transformers for Player Arousal Change Recognition From Gameplay Footage](http://arxiv.org/abs/2610.07603v1)
  <details><summary>📄 Abstract</summary>
  This article proposes Selective Affective Layer Fine-Tuning (SALFT), an efficient adaptation framework for Video Vision Transformers in player arousal recognition from gameplay. To bypass computationally expensive full fine-tuning, SALFT introduces a selection criterion based on the L2-norm change in layer parameters after brief adaptation, directly measuring representational shifts and providing a more stable basis than gradient-based alternatives. Evaluated via five-fold cross-validation on th...
  </details>

- **2026-10-06** — Tiago da Silva, Amauri H. Souza, Salem Lahlou — [Learning a Mixture of GFlowNets](http://arxiv.org/abs/2610.07562v1)
  <details><summary>📄 Abstract</summary>
  Learning an ensemble of GFlowNets to sample from a discrete target distribution has become a common approach for achieving better state space exploration and convergence than that of a monolithic sampler. However, these methods often add a substantial runtime overhead to the base model, and their conceptual connection remains elusive. To address this, we first propose a general-purpose theoretical framework for describing a mixture of GFlowNets, which we specialize into continuously (CI) and dis...
  </details>

- **2026-10-06** — Weiwei Wang, Yinchuan Xu, Jialu Gao et al. — [A Systematic Investigation of Bias in Large Language Models for Advertising Relevance](http://arxiv.org/abs/2610.07544v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to judge how well an advertisement matches a query, but the fairness of these judgments has received limited attention. We conduct a systematic study of fairness in relevance judgments made by LLMs for queries and advertisements. Our counterfactual framework examines the effects of advertiser identity and possible popularity, input language, and demographic wording. We study GPT-4o as a categorical relevance judge and a Qwen-7B model trained spe...
  </details>

- **2026-10-06** — Dani Roytburg, Daphne Ippolito — [Disentangling Models from Personas in Heterogeneous LLM Simulations](http://arxiv.org/abs/2610.07535v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent simulations with large language models (LLMs) often operate networks of agents with a single base model. This overlooks the inter-model effects which may dominate engagement dynamics in real-world deployments. To show this, we simulate a heterogeneous social network powered by several different base models and show that the amount of engagement an agent receives depends more on its base model than on its assigned persona. The attraction or repulsion effects of a base model strengthen...
  </details>

- **2026-10-05** — Chenglin Yang — [Evaluate the Stack, Not the Layer: Do Deterministic and LLM Gates for Agent Actions Fail Independently?](http://arxiv.org/abs/2610.07359v1)
  <details><summary>📄 Abstract</summary>
  Runtime gates for agent tool calls are stacked on the assumption that their errors multiply. We test it on 1,119 labelled agent actions from three corpora, without an adaptive adversary. The stack has one deterministic rule layer and four LLM judges, three of them re-collected with the served model recorded on every call. We read each stack as a number of multiplication-equivalent layers, n_mult, with its floor under perfect coupling. Under the STRICT miss definition (escalation to a human score...
  </details>

- **2026-10-05** — Salar Asayesh, Hossein Darani, Todd Cao et al. — [Task-Space Imitation Guidance for Efficient Reinforcement Learning](http://arxiv.org/abs/2610.07527v1)
  <details><summary>📄 Abstract</summary>
  We introduce Task-Space Imitation Guidance for Efficient Reinforcement Learning (TIGER), a reward-construction and pretraining framework for sparse-reward tabletop robotic manipulation. TIGER treats an action-chunked imitation policy not as an executable controller or action prior, but as a local task-space progress estimator: predicted action chunks are converted, using controller-aware action-to-motion mapping, into short-horizon end-effector references, and the RL agent receives dense progres...
  </details>

- **2026-10-05** — Faezeh Dehghan Tarzjani, Mevan Wijewardena, Alexander Romanus et al. — [From Local Evidence to Safety Verdicts: Causal Tracing in Vision-Language Models](http://arxiv.org/abs/2610.07514v1)
  <details><summary>📄 Abstract</summary>
  A vision-language model may need to combine an image with a prompt to recognize a safety risk that neither reveals alone. Where does this joint safety judgment become accessible inside the model? We introduce SSU-Bench, a dataset of matched safe and unsafe image-text combinations constructed using single-item prompt edits or image edits with annotated intended regions. Using three vision-language models, we transfer internal states between paired inputs and measure the resulting change in the sa...
  </details>

- **2026-10-05** — Peng Xie, Yequan Bie, Jianda Mao et al. — [SpecBraM: What Should an EEG Foundation Model Predict? Masked Band-Power Prediction versus Waveform Reconstruction](http://arxiv.org/abs/2610.07484v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised EEG models often reconstruct masked waveforms or predict discrete codes. We study a task-aligned alternative: masked band-power prediction (MBP), which predicts fixed narrow-band log spectral energy for masked channel-time patches. This target retains rhythm power relevant to sleep staging while avoiding phase-sensitive waveform reconstruction and a learned codebook. Across three pretraining seeds, we compare band-power and waveform targets with matched backbones, pretraining dat...
  </details>

- **2026-10-05** — Milad Mohammadi, Fatemeh Akrami Shamsabadi, Zahra Mohseni et al. — [PsyCIDRA: A Dual-Agent Framework for Psychiatric Interviewing and Diagnostic Reasoning](http://arxiv.org/abs/2610.07473v1)
  <details><summary>📄 Abstract</summary>
  Large language models show promise in clinical reasoning, but psychiatric interviewing requires guiding an evolving conversation. Their ability to carry out this interactive assessment remains less studied. We present PsyCIDRA, a dual-agent framework linking free-form psychiatric interviewing with diagnostic reasoning for expert review. Its interviewer agent uses tools to maintain working notes, load expert-written skills, and retrieve ICD-11 references to guide inquiry. Its diagnostic reasoning...
  </details>

- **2026-10-05** — Yueke Zhang, Zihan Fang, Kevin Leach et al. — [CogAdapt: Cognition-informed Sparse Adaptation of Code LLMs](http://arxiv.org/abs/2610.07446v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become increasingly capable of generating code. However, achieving stronger code-generation performance still often relies on costly model adaptation, i.e., fine-tuning pretrained model parameters. Prior studies have shown correspondence between human code processing and neural models' attention or internal computation. Human-aligned learning approaches use cognitive signals to guide training, but typically adapt a large portion of the model, leaving training co...
  </details>

- **2026-10-05** — Subham Rath, Raj Dandekar, Rajat Dandekar et al. — [What pass@k Cannot Measure: Evaluating Diversity and Capability Retention after Post-Training](http://arxiv.org/abs/2610.07405v1)
  <details><summary>📄 Abstract</summary>
  pass@$k$, the fraction of problems a model solves within $k$ sampled attempts, is the field's default protocol for deciding whether reinforcement-learning (RL) post-training on verifiable rewards improved a model. At the population level, pass@$k$ depends only on a problem's probability of a correct sample, with no term for how it is distributed across outputs. We show this gap is not academic. Training Qwen2.5-1.5B-Instruct on grade-school math with Group Relative Policy Optimization (GRPO) and...
  </details>

- **2026-10-05** — Bolian Li, Ting-Yao Hu, Cheng-Yu Hsieh et al. — [Structuring MoE Expert Selection for Agentic Reinforcement Learning](http://arxiv.org/abs/2610.07332v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM agents are frequently implemented using sparse mixture-of-experts (MoE) models, yet the co-design of agentic behavior and MoE structures remains underexplored. In this work, we comprehensively study the connections between agentic post-training and MoE expert selection. In off-the-shelf MoE models, we observe expert selection exhibits a specialized structure that naturally aligns with agentic trajectories. Specifically, expert routing overlaps more between turns where the agent ...
  </details>

- **2026-10-05** — Ignacy Stepka, Willa Potosnak, Kin G. Olivares et al. — [Scale-Invariant Training for Time Series Foundation Models](http://arxiv.org/abs/2610.07324v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) are trained on large collections of time series datasets that span various morphologies and domains. This setting exposes models to series whose scales -- typical magnitudes of their values -- can differ substantially. Affine scaling methods such as Reversible Instance Normalization (ReVIN) scale model inputs and reverse the transform before computing the loss. We show that this inversion multiplies each series' gradient by $b^p$ relative to loss on scaled t...
  </details>

- **2026-10-05** — Oliver Jaffe, Dane Sherburn — [TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts](http://arxiv.org/abs/2610.06824v2)
  <details><summary>📄 Abstract</summary>
  We introduce TasteVal, a benchmark to evaluate the experimental research taste of frontier models. We define research taste as the ability to pick interesting problems to solve, design experiments, and interpret experimental results. TasteVal measures the experimental component of research taste; given a fixed research problem, we measure how well a model iteratively designs experiments and draws conclusions from their outcomes. We operationalize experimental research taste as compute efficiency...
  </details>

- **2026-10-05** — Mehrdad Noori, Guile Wu, Sam Hosseini et al. — [GeoWM: Efficient Direct World Modeling in Explicit Geometry](http://arxiv.org/abs/2610.07381v1)
  <details><summary>📄 Abstract</summary>
  Modeling 3D scene geometry and its evolution over time is essential for autonomous driving and robotics. A common paradigm is to use world models to predict future images or latent representations of the environment and subsequently recover geometry from these predictions. However, this paradigm does not explicitly model geometric structure and typically relies on recursive rollouts to reach longer prediction horizons, leading to error accumulation and increasing computational cost. To address t...
  </details>

- **2026-10-05** — Naoki Wake, Justin Wagle — [SharedKV-BT: Node-Local Typed Decisions for Behavior-Tree Agents](http://arxiv.org/abs/2610.07327v1)
  <details><summary>📄 Abstract</summary>
  Agent tasks require sequences of interdependent decisions. Autoregressive models support more flexible decision interfaces than conventional classifiers but incur the latency of token-by-token generation. Recent shared-prefix methods reduce this cost by reusing encoded context and scoring multiple decisions in parallel, but do not model decision dependencies or verify execution. We propose SharedKV-BT, where each active node of a behavior tree (BT) exposes stage-local fields and candidates, and ...
  </details>

- **2026-10-05** — Tong Che, Yilong Li — [Does the Model Use the Feature? Separating Steering from Mechanism in LLMs](http://arxiv.org/abs/2610.07270v1)
  <details><summary>📄 Abstract</summary>
  Internal features in LLMs are often interpreted as mechanisms when they track a concept and their manipulation changes a related behavior. Yet steering can push a feature far outside its natural range, where its effects need not reflect the model's own computation. We examine this inference and propose an empirical contract whose tests evaluate features at values observed on natural inputs. One test copies a feature's value from an input that shows a behavior into a matched input that does not (...
  </details>

- **2026-10-05** — Xiaoran Yang, Xun Qian, Yang Zhan et al. — [MRPilot: Supervising and Intervening LLM-Based Multi-Robot Teams through Mixed Reality](http://arxiv.org/abs/2610.07477v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) let users direct heterogeneous multi-robot systems (MRS) through natural language, but make task interpretation, robot assignment, and coordination difficult to inspect and change. Based on a formative study with 12 non-expert users, we developed MRPilot, a mixed reality system organized around four stages of supervision and intervention. MRPilot represents robot-team plans and execution states as structured commitments shared across synchronized situated and overvie...
  </details>

- **2026-10-05** — Lan Shi, Daigo Shishika, Xuan Wang — [Adapting to Changes in Agent Behavior via Finite-Depth Policy Sensitivity](http://arxiv.org/abs/2610.07475v1)
  <details><summary>📄 Abstract</summary>
  Adapting a reinforcement learning policy to changes in another agent's behavior typically requires a large amount of new interaction data. Policy sensitivity provides a first-order prediction of how a locally optimal policy changes with a behavioral parameter, but its computation requires second-order derivatives whose effects propagate across future interactions. We develop a finite-depth framework to estimate this sensitivity by approximating the policy Hessian and mixed derivative using infor...
  </details>

- **2026-10-05** — Suguru Onda, Matthew Bailey, Ryan Farrell — [Semantic Capability Acquisition and Specialization During Vision-Language Model Fine-Tuning](http://arxiv.org/abs/2610.07385v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning vision-language models (VLMs) is typically evaluated at a single downstream checkpoint, obscuring whether a semantic capability was never acquired or emerged earlier and later declined during specialization. We ask how semantic capabilities are acquired, when they peak, how well they transfer, and what remains at deployment. We study these dynamics as a semantic capability trajectory, tracking identity- and attribute-based capabilities over training.   We formulate a trajectory-based...
  </details>

- **2026-10-05** — Ayesh Abu Lehyeh, Jay Hwasung Jung, Safwan Wshah — [What Words Keep of a Place: Zero-Shot Language Reasoning for Cross-View Geo-Localization](http://arxiv.org/abs/2610.07269v1)
  <details><summary>📄 Abstract</summary>
  Cross-view geo-localization is commonly solved as an image retrieval problem, matching a ground-level image against a database of satellite tiles through a jointly trained embedding. Such models are accurate, but they need large paired supervision and cannot show what evidence supports a match. In this paper, we study a different question: how much of this task can be solved through language alone? We prompt a multimodal large language model (MLLM) to describe each ground panorama and each satel...
  </details>

- **2026-10-05** — Thomson D. Nguy — [Can Semantic Geometry Teach an AI Judgement?](http://arxiv.org/abs/2610.07249v1)
  <details><summary>📄 Abstract</summary>
  How can an AI agent determine what rules to follow? One rule permits an action. Another imposes a condition, exception, or conflicting obligation. Deterministic systems can resolve those relationships when they have been specified. When they remain implicit in language, an agent can follow one rule while missing another that should stop it. Refusing every unresolved action avoids that risk, but also blocks permissible actions.   We wanted the agent to make the distinction and still act. Our init...
  </details>

- **2026-10-05** — Mohamed Chenene, Carlos Rosas-Hinostroza, Anastasia Stasenko et al. — [Wikidata Search Traces: A Dataset for Training Knowledge Graph Search Agents](http://arxiv.org/abs/2610.06650v2)
  <details><summary>📄 Abstract</summary>
  Wikidata is one of the largest open knowledge bases, yet answering a complex question over it still requires a SPARQL query that names the right entities and properties and chains their relations. Language models offer a natural-language alternative but answer largely from memory, which is least reliable for less prominent entities. We study agents that instead answer by exploring the graph, and argue that two obstacles limit them: the lack of training data recording how a solver explores, and i...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 663 |
| prompt-injection | 603 |
| memory-poisoning | 54 |
| tool-use-attack | 150 |
| backdoor | 501 |
| adversarial-attack | 626 |
| privacy-leakage | 4306 |
| steganography | 76 |
| misuse | 1128 |
| red-teaming | 134 |
| vulnerability | 3482 |
| defense | 3303 |
| alignment | 3083 |
| robustness | 3344 |
| watermark | 549 |
| unlearning | 110 |
| agent-safety | 61 |
| benchmark | 67 |
| survey | 387 |
| other | 8989 |

---

📚 **全部 31616 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-07 22:33:20*