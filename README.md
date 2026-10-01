<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-30606-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-01 22:15 ｜ **论文总数 / Total Papers**: 30606（近 30 天 / Recent 30 days: 4590）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 30606 篇论文（含摘要、分类筛选、搜索）/ View all 30606 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 652
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 585
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 52
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 147
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 488
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 615
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4244
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 73
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1099
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 130
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3374
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3191
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2971
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3212
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 518
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 107
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 60
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 378
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8643

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4590 篇，完整 30606 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4590 papers from the last 30 days (with date, authors & abstract). For the full list of 30606 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-09-30** — Zhen Liang, Hai Huang, Wentao Chen — [CodeMimicry: Exploiting Safety Generalization Lag in Large Language Models via Structured Code Completion](http://arxiv.org/abs/2609.39902v1)
  <details><summary>📄 Abstract</summary>
  Large language models have achieved remarkable capabilities across diverse domains, yet their safety alignment remains vulnerable to jailbreak attacks. In this work, we identify a previously underexplored failure mode - safety generalization lag - where alignment trained predominantly on natural language fails to transfer to the code domain. We show that this lag induces a code-completion blind spot, allowing malicious intent embedded within syntactically valid code to evade safety mechanisms. T...
  </details>

- **2026-09-30** — Wenyu Chen, Li Wang, Chuanchao Zang et al. — [SceneJail: Exploiting Video Scenario Context to Jailbreak Multimodal LLMs](http://arxiv.org/abs/2609.38899v1)
  <details><summary>📄 Abstract</summary>
  Video Multimodal Large Language Models (Video-MLLMs) support reasoning over video inputs, yet remain vulnerable to jailbreak attacks that elicit policy-violating responses. Existing video jailbreaks primarily manipulate how harmful queries are visually presented, thereby treating video merely as a carrier. Consequently, the surrounding video scenario remains unexplored as a contextual attack surface. In this paper, we show that the same harmful query can elicit different safety responses when pl...
  </details>

- **2026-09-29** — Lena Libon, Alexander Panfilov, Ben Rank et al. — [Alignment via Training Against Probes Without Losing Monitorability](http://arxiv.org/abs/2609.38645v1)
  <details><summary>📄 Abstract</summary>
  Models are usually aligned based on their observed outputs, using demonstrations, preference data, or reward signals. These objectives reward responses that look aligned. More capable models may learn to satisfy them without internalizing the intended behavior, for example by faking compliance during training. Such superficial compliance could be harder when the objective is defined on model internals rather than outputs. Therefore, we study probe-guided fine-tuning, using probes that detect und...
  </details>

- **2026-09-29** — Xianhui Zhang, Jian Yu, Chengyu Xie et al. — [ACTR: Aligning Thoughts and Responses for Multilingual Safety in Reasoning LLMs](http://arxiv.org/abs/2609.37054v2)
  <details><summary>📄 Abstract</summary>
  Ensuring the safety of reasoning large language models (LLMs) across languages is essential for their reliable deployment. However, when exposed to jailbreak attacks in non-high-resource languages, these models may generate unsafe responses even when their reasoning traces identify safety risks. To address this issue, we propose aligning cross-lingual thoughts and responses (ACTR), a framework that improves multilingual safety alignment by strengthening the use of existing safety reasoning. Spec...
  </details>

- **2026-09-29** — Keifer Lee — [Inference-Layer Security: Defending Against Adversarial Inference and Infrastructure Abuse](http://arxiv.org/abs/2609.38239v1)
  <details><summary>📄 Abstract</summary>
  A Technical Report: Operating a large language model (LLM) as a service requires more than inference infrastructure: the provider must also defend against adversarial interactions that seek to exploit the service, including jailbreaking for harmful use, sophisticated denial of service, and distillation attacks. We study this problem at the inference layer, using a hypothetical frontier lab, Five Elements Inc., as a running example. Because no public labelled dataset of adversarial LLM usage exis...
  </details>

- **2026-09-29** — Xianhui Zhang, Jian Yu, Chengyu Xie et al. — [actr: aligning thoughts and responses for multilingual safety in reasoning llms](http://arxiv.org/abs/2609.37054v1)
  <details><summary>📄 Abstract</summary>
  Ensuring the safety of reasoning large language models (LLMs) across languages is essential for their reliable deployment. However, when exposed to jailbreak attacks in non-high-resource languages, these models may generate unsafe responses even when their reasoning traces identify safety risks. To address this issue, we propose aligning cross-lingual thoughts and responses (ACTR), a framework that improves multilingual safety alignment by strengthening the use of existing safety reasoning. Spec...
  </details>

- **2026-09-29** — Jesson Wang, Shawn Li, Wei Yang et al. — [Controlled Decoding Attacks on Black-Box LLMs](http://arxiv.org/abs/2609.36956v1)
  <details><summary>📄 Abstract</summary>
  Manipulating next-token probabilities during generation can bypass the safety alignment of large language models. Existing approaches, however, rely on access to model weights or numerical token probabilities and therefore do not apply to interfaces that return only sampled text. Reconstructing probabilities from sampled outputs offers a possible alternative, but finite sampling produces sparse and noisy estimates, while repeating this process at every generation step incurs substantial query co...
  </details>

- **2026-09-29** — Omar Sheta, Rinku Deuja, Hadi Masoudi et al. — [Does the Unsafe Gradient Survive a Conversation? On the Fragility of Gradient-Based Jailbreak Detection in Multi-Turn Dialogue](http://arxiv.org/abs/2609.36849v1)
  <details><summary>📄 Abstract</summary>
  Safety-aligned language models are commonly deployed as multi-turn assistants, which lets adversaries spread unsafe intent across several user turns instead of a single prompt. Gradient-based jailbreak detectors such as GradSafe were developed for single prompts: they score an input by the alignment between its induced gradient and a fixed unsafe reference direction, and their effectiveness in multi-turn dialogue remains unclear. We conduct a controlled evaluation of gradient-based jailbreak det...
  </details>

- **2026-09-29** — Minh Nhat Le, Nisarga Gondi, Yibo Peng et al. — [Self-Evolving Defense: Continual Security Policy Learning for LLM Agents](http://arxiv.org/abs/2609.36603v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly power agents that access sensitive information, use external tools, and modify software repositories. Although these capabilities offer substantial benefits, they also create security risks such as jailbreaks, prompt injection, and vulnerable code generation. Existing defenses often require retraining, fail to adapt to evolving attacks, or address only a single threat pattern. To address these limitations, we propose Self-Evolving Defense (SED), a traini...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-09-30** — Jieke Shi, Yuchen Chen, Junda He et al. — [Aletheia: Permission-Minimality Testing for Coding-Agent Rules](http://arxiv.org/abs/2609.39678v1)
  <details><summary>📄 Abstract</summary>
  Repository instruction files guide coding agents, but also expose them to prompt injection. Malicious rules can request credential access or data transfer while the agent produces a correct patch. We present Aletheia, a framework for permission-minimality testing. Aletheia translates requested authority into a typed language and synthesizes executable sandbox configurations. It runs the unchanged rule and task under full permissions and independent restrictions that remove one permission at a ti...
  </details>

- **2026-09-30** — Zheng Chen, Linfeng Liu, Hong Li et al. — [RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models](http://arxiv.org/abs/2609.39551v1)
  <details><summary>📄 Abstract</summary>
  Auto-research agents, LLM systems that propose, implement, train, and evaluate model changes across iterations, promise to automate applied ML's experimental loop. Over long horizons, execution accuracy is a binding constraint: a change can silently leak held-out data, omit normalization, disconnect a gradient, or leave a train/eval flag unwired, invalidating expensive runs and compounding error across iterations. We present RankEvolve, an auto-research framework for evolving generative ranking ...
  </details>

- **2026-09-30** — Yunjia Zheng, Bintang Dwi Marthen, Zachary Pan et al. — [Towards Efficient HPC Systems for Agents: Challenges and Opportunities](http://arxiv.org/abs/2609.38723v1)
  <details><summary>📄 Abstract</summary>
  Coding agents have become real users of high-performance computing (HPC) systems, yet today's HPC abstractions, interfaces, and policies remain designed for human-driven workflows. In our measurement, users running coding agents are only 19.5% of the observed population, but account for 55.8% of job submissions, 29.1% of CPU core-hours, and 42.7% of GPU-hours. Agents are not simply faster humans. They issue commands at 20.8x the human rate, decompose work into fine-grained explore-modify-execute...
  </details>

- **2026-09-29** — Dongxu Cui, Zhichao Gu, Ping Zheng et al. — [ContractWarden: Kernel-Enforced Damage Boundaries for AI Agents via Human-Authorized Contracts](http://arxiv.org/abs/2609.38248v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can execute commands, create subprocesses, and directly access files and networks, allowing prompt injection or planning errors to become operating-system side effects. We present ContractWarden, a Linux reference monitor that enforces a human-authorized damage boundary without trusting the agent or its policy suggestions. A model may propose a tri-state asset contract - allow, deny, or no_egress - but a human makes the final choice. An execution gate binds the contra...
  </details>

- **2026-09-29** — Rui Wen, Jiayang Liu, Zeyu Yang et al. — [Where Do LLMs Decide to Break the Rules? Mechanistic Localization of Prompt Injection Compliance](http://arxiv.org/abs/2609.37737v1)
  <details><summary>📄 Abstract</summary>
  When a prompt injection attack succeeds, a Large Language Model (LLM) abandons its assigned system role to comply with an adversarial instruction. While prior work has extensively quantified how often this occurs, we ask a more fundamental question: where inside the network does the model actually decide to break the rules? Using layer-by-layer causal activation patching across five models (4B to 32B parameters), we find a clear dissociation: attack information is linearly decodable from the fir...
  </details>

- **2026-09-29** — Yanjie Li, Xiangyu He, Xuelong Dai et al. — [ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents](http://arxiv.org/abs/2609.37196v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents remain vulnerable to indirect prompt injection because trusted instructions and untrusted observations share one context, allowing malicious content to steer consequential input-filtering defenses. Multi-path consensus defenses still leave a high attack success rate because they examine content or aggregated outputs rather than authorizing effects, especially for the within-tool attack, which preserves the intended tool but manipulates its arguments. Data-Flow Control such ...
  </details>

- **2026-09-29** — Zonghao Ying, Xiangfan Wu, Bo Yang et al. — [pikit: A Composable Toolkit for Indirect Prompt Injection Research and Evaluation](http://arxiv.org/abs/2609.36817v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection embeds malicious instructions within external content retrieved by LLM-based agents, altering target behavior without user authorization. We introduce pikit, a research toolkit designed to systematically evaluate these threats across three core dimensions: attacks (13 methods), channels (16 carriers across text and file modes), and defenses (9 prevention strategies and 3 offline detection baselines). Built on a decorator-based registry, pikit enables seamless extension ...
  </details>

- **2026-09-29** — Michael Lee, Zhipeng Wei, Yue Dong et al. — [Divide and Inject: Can Agents Reconstruct an Indirect Prompt Injection from Fragments?](http://arxiv.org/abs/2609.36576v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems are now being widely used to orchestrate tools and reason over long contexts. However, the improving capabilities of the large language models powering these agents also create new attack surfaces for indirect prompt injection. In particular, an attacker may not need to place a complete malicious instruction in retrieved content if the agent can reconstruct the objective from incomplete fragments distributed across a long context. In this work, we introduce adaptive long-context ...
  </details>

- **2026-09-29** — Mark Russinovich — [CounterSteer: Suppressing Indirect Prompt Injection with Activation Steering](http://arxiv.org/abs/2609.36570v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection makes an LLM agent treat untrusted retrieved text as instructions. We present CounterSteer, an inference-time defense that suppresses this behavior inside the model. Per model, a five-step recipe fits a residual-stream direction from paired episodes differing only in whether an embedded instruction is followed, and retains it only if it passes pre-specified causal and capability gates. At deployment, the direction is subtracted from every tool-result token during prefil...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-09-30** — Kaixing Zhang, Changming Li, Yingdong Shi et al. — [Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents](http://arxiv.org/abs/2609.39149v1)
  <details><summary>📄 Abstract</summary>
  Textual skills enable large language model (LLM) based agents to accumulate reusable procedural knowledge without updating model parameters. Yet existing skill evolution remains largely confined to the text space: an optimizer must diagnose success and failure patterns, and revise skills solely from long execution trajectories and sparse task outcomes. This text-only paradigm leaves the agent's internal representations, which contain rich records of its evolving execution state, outside the skil...
  </details>

- **2026-09-30** — Guanqun Yang, Wenlong Zhang, Tian Shi et al. — [SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale](http://arxiv.org/abs/2609.38822v1)
  <details><summary>📄 Abstract</summary>
  Anthropic's Agent Skills package reusable procedural know-how for an LLM agent into SKILL.md directories, and open-source aggregations have grown past 230,000 skills, making selection rather than authoring the bottleneck. The standing answer in the literature outsources selection to the agent itself: an LLM-mediated retrieval loop that rewrites queries and refines candidates inside the agent's decision loop, paying LLM tokens on every task. We present SkillSeek, an open-source two-stage skill re...
  </details>

- **2026-09-29** — Haoran Ou, Gelei Deng, Xuanye Zhang et al. — [SKILLLITE: Evidence-Guided Malicious Skill Auditing with Compact LLMs](http://arxiv.org/abs/2609.36879v1)
  <details><summary>📄 Abstract</summary>
  As LLM-based agents perform increasingly complex tasks, Agent Skills have emerged as a flexible mechanism for extending their capabilities. An Agent Skill packages task-specific instructions with executable components and auxiliary resources to provide specialized functionalities. However, the growing adoption of third-party Skills introduces a new supply-chain attack surface. Malicious Skills can embed harmful behaviors that abuse agent privileges and compromise the agent execution environment ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 7 papers

- **2026-09-30** — Muhammad Huzaifa, Sina Mavali, Thorsten Eisenhofer — [Safety of Latent Communication in Multi-Agent Systems](http://arxiv.org/abs/2609.39788v1)
  <details><summary>📄 Abstract</summary>
  Latent communication enables multi-agent systems to exchange information directly in internal representation space, reducing the token, computation, and latency overhead of text-based communication. To this end, lightweight trainable links are introduced to map the sender's representations into the receiver's input space. In this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unch...
  </details>

- **2026-09-30** — Wenxin Wu, Lingyong Yan, Lei Sha et al. — [Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents](http://arxiv.org/abs/2609.39352v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on reusable Skills for complex, multi-step tasks, creating a critical supply-chain attack surface where poisoned Skill content steers agent decision loops under benign requests. Existing skill poisoning attacks either colocate actuation with its contextual pretext or distribute actuation across multiple Skills, but do not explicitly separate the rationale for execution from the operation itself. In this work, we reveal that untrusted agent decisions fundamentally dep...
  </details>

- **2026-09-29** — Yurong Hao, Wen Zhou, Guowei Guan et al. — [VirusCascade: Hijacking Collaborative Reflection in LLM-Powered Recommender Agents](http://arxiv.org/abs/2609.38270v1)
  <details><summary>📄 Abstract</summary>
  Advancing beyond traditional static scoring models, LLM-powered agentic recommender systems (LLM-ARS) instantiate users and items as autonomous agents, whose semantic states are dynamically refined through a recurrent process known as collaborative reflection. While this mechanism improves recommendation quality, it simultaneously introduces a systemic vulnerability: adversarial evidence injected into a single agent can be rationalised into a legitimate preference narrative, written back into me...
  </details>

- **2026-09-29** — Shuming Liu, Zhifang Zhang, Suqin Yuan et al. — [Selective Channel Restoration for Backdoored Vision-Language Models](http://arxiv.org/abs/2609.37759v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) exhibit strong multimodal capabilities but remain vulnerable to backdoors implanted through poisoned fine-tuning data. Existing defenses often require extensive parameter updates during fine-tuning or incur per-query overhead during inference. To address these limitations, we propose Perturb-Select-Restore (PSR), a post-training defense that performs sparse updates to the projection interface and introduces no additional computation during inference. We reveal that ...
  </details>

- **2026-09-29** — Sayan Biswas, Jade Garcia Bourrée, Rachid Guerraoui et al. — [Backdoor Mitigation in Decentralized LLM Fine-Tuning](http://arxiv.org/abs/2609.37367v1)
  <details><summary>📄 Abstract</summary>
  Decentralized large language model (LLM) fine-tuning lets organizations collaboratively train a shared LLM on data they cannot pool, without a central coordinator. In every round, each node exchanges a trainable adapter with its neighbors over a communication graph, and then aggregates them. This setting, however, is vulnerable to propagated backdoors, which is a hidden behavior that lets a model perform normally on clean inputs but produce an attacker-chosen output whenever a secret trigger app...
  </details>

- **2026-09-29** — Zifu Tao, Changqing Yin — [When Tools Silently Lie: Evaluating and Mitigating Blind Compliance in Tool-Augmented Data Agents](http://arxiv.org/abs/2609.37153v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented data agents rely on tool outputs for analytical decisions. Yet successful execution can return plausible but incorrect evidence, requiring agents to decide whether to trust or verify it. Understanding this failure requires examining both the evidence obtained through checking and the answer ultimately adopted. We introduce ToxicBench to measure checking and adoption under numerical, label, schema, and retrieval errors, pairing clean and poisoned observations over fixed source data...
  </details>

- **2026-09-29** — Zonghua Gu, Zeyu Gao, Amin Saremi et al. — [Deep Learning Latency Attacks and Defenses: A Cross-Domain Survey of Availability Threats](http://arxiv.org/abs/2609.36732v1)
  <details><summary>📄 Abstract</summary>
  Adversarial machine learning has focused mainly on integrity, but availability is an increasingly consequential complement. Latency attacks (also energy-latency attacks) increase inference-time work, energy, or response time, causing deadline misses, throughput collapse, or resource exhaustion in vehicle controllers, interactive services, or battery-powered sensors, sometimes while preserving the nominal prediction.   This survey unifies a fragmented literature spanning perception pipelines (inc...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-09-30** — Ziqi Zhou, Yifan Hu, Yufei Song et al. — [Universal Cross-Prompt Adversarial Attacks on Promptable Concept Segmentation](http://arxiv.org/abs/2609.39265v1)
  <details><summary>📄 Abstract</summary>
  The Segment Anything Model (SAM) achieves remarkable performance in visual segmentation. The latest SAM3 extends promptable segmentation to concept-level prediction, broadening the scope of segmentation foundation models. While recent works reveal that SAM and SAM2 are vulnerable to adversarial examples, the robustness of SAM3 under the concept segmentation paradigm remains unexplored. In addition, existing adversarial attacks on SAM-series models exhibit limited cross-prompt transferability. To...
  </details>

- **2026-09-30** — Shilinlu Yan, Bowen Chen, Yuechen Zhang et al. — [Feature-Aware Token Attack for Compression-Triggered Stealthy Failures in Large Vision-Language Models](http://arxiv.org/abs/2609.39134v1)
  <details><summary>📄 Abstract</summary>
  Visual-token compression improves the efficiency of large vision-language models, but can expose failures that full-token evaluation misses. We study adversarial images that preserve full-token correctness yet induce errors after compression, even when both inference paths succeed on the clean image. Creating such failures is challenging because perturbing token importance can also damage the visual content needed for full-token inference. We propose Feature-Aware Token Attack (FATA), which coup...
  </details>

- **2026-09-30** — Xinyi Ni, Lifeng Lai — [Robust Risk-Sensitive Reinforcement Learning from Corrupted Human Feedback](http://arxiv.org/abs/2609.38938v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with human feedback (RLHF) learns from human comparisons, which can be corrupted or deliberately manipulated. This paper studies online risk-sensitive RLHF with static conditional value-at-risk (CVaR) under adversarial preference-label flips. We consider additive linear rewards and a fixed-reference protocol with one comparison per episode and at most $C$ flipped labels over $K$ episodes. We propose weighted streamed-preference CVaR RLHF (WSP-CVaR-RLHF), which combines unc...
  </details>

- **2026-09-29** —  Yelyzaveta,  Husieva, Lauren Alvarez — [The Geometry of Harmfulness in Multi-Turn Attacks](http://arxiv.org/abs/2609.38389v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) remain vulnerable to adversarial attacks that circumvent safety alignment to elicit harmful outputs. It remains unclear how harmfulness and refusal representations evolve over the course of multi-turn attacks, and why single-turn defenses are less effective in multi-turn settings. This work investigates how the geometry and temporal dynamics of harmfulness and refusal representations evolve across multi-turn attacks. We analyzed hidden-state representations from thre...
  </details>

- **2026-09-29** — Binchi Zhang, Atrisha Sarkar, Apurva Narayan — [It Takes Little to Rewrite Perception: Targeted Semantic Substitution in Vision-Language Models at $ε\leq 4/255$](http://arxiv.org/abs/2609.38298v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) are widely deployed in safety-critical scenarios, and understanding to which extent they can be controlled by adversarial perturbation is a prerequisite for evaluating their trustworthiness. Existing representation-alignment attacks, which make a VLM perceive a target image, achieve limited success at $\varepsilon \leq 4/255$. Therefore, VLMs seems robust to perturbations in this range. We show that this robustness does not hold, as targeted semantic substitution su...
  </details>

- **2026-09-29** — Soeun Han, Jisoo Lee, Jeongyong Shim et al. — [SURE: Framework for Safety to Construct Trustworthy AI](http://arxiv.org/abs/2609.38249v1)
  <details><summary>📄 Abstract</summary>
  Warning: This paper contains harmful and offensive text.   Recently, large language models such as GPT-4, and Claude have revolutionized tasks in various domains. As the use of these large language models increases, people are increasingly concerned about AI safety and demand that large language models behave responsibly and safely. As a result, there has been growing global interest in developing methods to ensure AI safety. However, the detailed criteria for AI safety may vary depending on the...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 20 papers

- **2026-09-30** — Deema Alnuhait, Gengyu Wang, Muhammad Khalifa et al. — [Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems](http://arxiv.org/abs/2609.39050v1)
  <details><summary>📄 Abstract</summary>
  As multi-agent systems enter high-stakes domains, the possibility that agents may circumvent safety boundaries is a growing concern. Prior work has examined this risk primarily in adversarial settings, where agents are instructed or rewarded to communicate covertly and evade oversight. We show that benign agents can cross the same boundaries without adversarial incentives. We emulate a software-engineering workflow in which a planner represents a company hiring an external developer. The planner...
  </details>

- **2026-09-30** — Fahao Chen, Linkang Du, Jinhao Zhou et al. — [SparLeak: Privacy Leakage from Sparse Attention in LLM Inference on Shared GPUs](http://arxiv.org/abs/2609.38830v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention is widely used to accelerate long-context inference in modern large language models (LLMs), but its input-dependent execution behavior introduces previously unexplored privacy risks. We identify a new GPU micro-architectural side channel, termed Sparsity-Induced Memory Access (SIMA), which arises from secret-dependent key-value cache access patterns induced by sparse attention.   Based on this observation, we present SparLeak, a phase-aware side-channel attack that extracts SIMA...
  </details>

- **2026-09-30** — Owais Iqbal, Sudipta Sarkar, Shyam Marjit et al. — [Image Classifiers are Efficient Self-Supervised Video Representation Learners](http://arxiv.org/abs/2609.40347v1)
  <details><summary>📄 Abstract</summary>
  We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstruction-based autoencoders for learning with unlabeled data, we repurpose standard image Vision Transformers by representing videos as super images which are grids composed of frames sampled from videos. From each super image, we construct two views: one with spatial patch masking and the other with tempo...
  </details>

- **2026-09-30** — Olivera Kotevska, Sumit Jha, Aurélien Bellet et al. — [Privacy Foundations for Multi-Institutional Scientific Artificial Intelligence](http://arxiv.org/abs/2609.39787v1)
  <details><summary>📄 Abstract</summary>
  Scientific artificial intelligence (AI), spanning foundation models (FMs) to federated data-analysis pipelines, is becoming shared infrastructure across national laboratories, universities, hospitals, and industrial partners. This collaboration creates privacy risks whose natural unit is often an institution's participation, research strategy, or technical capability rather than a single record. Differential privacy (DP), federated learning (FL), secure computation, trusted execution, and proven...
  </details>

- **2026-09-30** — Zhixuan Tan, Pengjie Gu, Zhao Li et al. — [EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses](http://arxiv.org/abs/2609.39284v1)
  <details><summary>📄 Abstract</summary>
  While large language models have achieved remarkable success in isolated code generation, authentic software engineering requires sustained reasoning, complex state management, and continuous cross-domain abstraction. However, current evaluations of skill evolution in autonomous agents suffer from a critical identifiability problem: they structurally confound genuine capability abstraction with rote solution leakage (i.e., copying highly similar code from historical training data). To resolve th...
  </details>

- **2026-09-30** — Razan El Mais, Ali Chehab, Ibrahim Issa et al. — [Is Weight Tying Still Beneficial for Decoder-Only LLMs in Private Settings Under DP-SGD?](http://arxiv.org/abs/2609.40335v1)
  <details><summary>📄 Abstract</summary>
  Differentially Private Stochastic Gradient Descent (DP-SGD) is a leading approach for privacy-preserving fine-tuning of large language models (LLMs). Many decoder-only LLMs employ weight tying between input and output embeddings, a design choice originally introduced for parameter efficiency and improved language modeling performance in the non-private setting. However, the impact of weight tying under differentially private training remains largely unexplored. In this work, we investigate the r...
  </details>

- **2026-09-30** — Aawez Mansuri, Kush Mehta, Mohammadreza Chavoshi et al. — [Comparison of techniques for fine-tuning open-weight models for entity extraction from radiology reports](http://arxiv.org/abs/2609.40236v1)
  <details><summary>📄 Abstract</summary>
  Converting free-text radiology reports into structured labels supports cohort building, quality assurance, and monitoring of clinical imaging models, but the strongest label extractors are hosted proprietary models whose use raises privacy, cost, and reproducibility concerns. We asked whether a fine-tuned open-weight model (Gemma-3-12B) can match GPT-4o at multi-label intracranial hemorrhage (ICH) acuity extraction from non-contrast head-CT reports, and which ingredients matter. Using a 2x2 desi...
  </details>

- **2026-09-30** — Adrià Molina, Oriol Ramos Terrades, Josep Lladós — [Unapologetically Distributed: A Call for Decentralized Document Analysis](http://arxiv.org/abs/2609.39684v1)
  <details><summary>📄 Abstract</summary>
  Privacy has become an increasingly important concern in the Document Analysis community, to the extent that in many environments such as archives, governmental institutions, and local businesses, the adoption of automation is restricted by legal and policy constraints. While federated learning has often been regarded as a ``necessary evil'', implying an unavoidable performance trade-off in exchange for decentralization and privacy, many prior works overlook its potential to improve robustness to...
  </details>

- **2026-09-30** — Lucas Poinsignon, Jorge da Silva Gonçalves, Samuel Ruipérez-Campillo et al. — [Wavelet Flow Matching for Time Series](http://arxiv.org/abs/2609.39374v1)
  <details><summary>📄 Abstract</summary>
  Synthetic time series are increasingly used for data augmentation, privacy-preserving data sharing, and downstream model development, yet faithfully reproducing both multi-scale temporal structure and cross-channel dependencies remains challenging. We study multivariate time-series generation through flow matching in the wavelet domain. By operating on multilevel discrete wavelet coefficients rather than directly in the time domain, the model represents coarse structure and progressively finer d...
  </details>

- **2026-09-30** — Marcin Marciniak — [The Concentration of Artificial Intelligence in Big Tech and Its Implications for Human Rights in the European Union](http://arxiv.org/abs/2609.39285v1)
  <details><summary>📄 Abstract</summary>
  The development of advanced artificial intelligence is increasingly concentrated in a small group of vertically integrated technology companies. These firms control combinations of computing infrastructure, cloud services, data, foundation models, software ecosystems, and channels of distribution. This article argues that such concentration transforms market power into a form of private governance over the conditions in which fundamental rights are exercised. Drawing on an interdisciplinary narr...
  </details>

- **2026-09-29** — Maxwell Gold, Sarah Hagen, Daniel Alabi et al. — [Quantum Secure Non-Interactive Reductions](http://arxiv.org/abs/2609.38452v1)
  <details><summary>📄 Abstract</summary>
  Efficient models for secure computation often rely on offline preprocessed correlations, which subsequently enable private online computation from minimal assumptions. Within these models, the study of secure non-interactive reductions (SNIR) formalizes when one classical correlation can be non-interactively transformed into another, while guaranteeing information-theoretic simulation-based privacy. In this work, we introduce quantum secure non-interactive reductions (QSNIR), a natural extension...
  </details>

- **2026-09-29** — Yavuz Bakman, Duygu Nur Yaldiz, Baris Askin et al. — [Aligned Data Can Induce Misalignment via Context Confusion](http://arxiv.org/abs/2609.38379v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are frequently updated for various use cases, where filtering out misaligned training samples is a common practice for preventing post-update misalignment. However, alignment is inherently context-dependent: a recommendation that is aligned in one context may be inappropriate in another. For example, in response to the question "What should a researcher do with the research data?", recommending that the researcher preserve the data for reproducibility is aligned. In ...
  </details>

- **2026-09-29** — Guangxin Zhao, Yiran Hu, Yuan Cao et al. — [TALK-Dem: Benchmarking Embodied Task Planning under Dementia-Associated Communication Patterns](http://arxiv.org/abs/2609.38371v1)
  <details><summary>📄 Abstract</summary>
  Existing LLM-driven robot task planners rely on a taken-for-granted assumption of an ideal user whose instructions are clear, complete, and task-focused. However, when interacting with real-world users, especially those experiencing cognitive impairments, such as people living with dementia (PLWD), the planners often make mistakes and even pose physical safety risks. We proposed TALK-Dem (Talking Attributes and Linguistic Knowledge in Dementia), the first benchmark for evaluating LLM-driven robo...
  </details>

- **2026-09-29** — Jonathan Graehl — [Strong Multilingual Privacy Tagging at Encoder Speed](http://arxiv.org/abs/2609.38630v1)
  <details><summary>📄 Abstract</summary>
  Privacy redaction must remove personal information while preserving relationships expressed in text. We develop a multilingual named-entity tagger with fine-grained distinctions supporting varied redaction policies and methods for cheaply learning additional distinctions. We fine-tune a multilingual encoder with an affine span-tagging head on frontier-model annotations in 35 languages, replay mapped human gold with coverage-aware masking so unannotated types are not treated as negatives, and rep...
  </details>

- **2026-09-29** — Dannong Wang, Yuran Zhang, Bian Sun et al. — [PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration](http://arxiv.org/abs/2609.38458v1)
  <details><summary>📄 Abstract</summary>
  Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclo...
  </details>

- **2026-09-29** — Yunan Lu, Shuang Xie, Meghna Allamudi et al. — [SimTrace: Grounded Multimodal User Trajectories Generation for Online User Modeling](http://arxiv.org/abs/2609.38397v1)
  <details><summary>📄 Abstract</summary>
  Virtual clients offer a cost-effective approach to support applications such as A/B testing, recommender system development, and interface evaluation. However, building them requires access to large-scale, semantically faithful, fine-grained online user trajectories. These data are difficult to obtain because proprietary logs are subject to privacy restrictions and small businesses often lack sufficient traffic. Consequently, existing public datasets either abstract away fine-grained user intera...
  </details>

- **2026-09-29** — Patt Phurtivilai, Zhiyang Dou, Yifan Wu et al. — [TrackFish3D: Self-Supervised 3D Tracking of Schooling Fish from Multi-view Videos](http://arxiv.org/abs/2609.38347v1)
  <details><summary>📄 Abstract</summary>
  Quantifying collective fish behavior requires accurate trajectories, yet multi-view 3D tracking remains challenging due to frequent occlusions, visually similar individuals, and the long-standing scarcity of identity annotations. We present TrackFish3D, a geometry-driven self-supervised framework for dense multi-camera 3D tracking of schooling fish. Instead of relying on appearance-based re-identification or manually annotated identities, TrackFish3D turns calibrated multi-view geometry into sup...
  </details>

- **2026-09-29** — Teng Zhou, Yunhao Chen — [CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer](http://arxiv.org/abs/2609.38136v1)
  <details><summary>📄 Abstract</summary>
  Style transfer aims to render target content in the style of a reference image, but existing methods often suffer from content leakage, where objects, layouts, or semantics from the style reference appear in the generated output. Although prior data-driven and training-free methods can reduce leakage, they often face a leakage-degradation dilemma: stronger content suppression may weaken style fidelity, while richer style preservation may reintroduce unwanted reference content. We identify this d...
  </details>

- **2026-09-29** — Kenan Alkiek, Moontae Lee, David Jurgens et al. — [HARISSA: Inference-Time Self-Checks for Efficient and Safe Local Language Model Deployment](http://arxiv.org/abs/2609.38006v1)
  <details><summary>📄 Abstract</summary>
  Running a language model locally offers advantages in privacy, latency, and cost, but local hardware fits only small models, which are less capable than frontier models. The usual remedy for a hard query, escalating it to a cloud model, gives up the privacy and cost advantages of running locally. A deployment that stays local faces two decisions for hard queries instead. First, it can spend more computation on a query, e.g., reasoning before answering, which raises accuracy at a cost in latency,...
  </details>

- **2026-09-29** — Ying Song, Xiaowei Jia, Balaji Palanisamy — [Dagger: Decoupling-based Model Stealing Attack against Graph Neural Networks](http://arxiv.org/abs/2609.37972v1)
  <details><summary>📄 Abstract</summary>
  As Graph Neural Networks (GNNs) are widely deployed as Machine Learning-as-a-Service (MLaaS) APIs, model stealing attacks have emerged as a critical security threat. By querying a victim model's black-box API, an adversary can construct a functionally equivalent surrogate model, compromising proprietary intellectual property and downstream security. Existing GNN stealing attacks, however, rely on overly permissive assumptions, such as soft-label outputs, large query budgets, full-graph query acc...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-09-30** — Julian Schulz, Lukas Fülle, Rieke Fruengel — [Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard](http://arxiv.org/abs/2609.39838v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought monitoring as an approach for AI oversight and control is threatened by the possibility of steganographic reasoning, where LLMs conceal their reasoning inside innocuous-looking text. Two neighbouring capabilities, steganographic messaging (passing a concealed message) and encoded reasoning (reasoning in an illegible but unconcealed format), have already been shown to emerge under training pressures that occur in real pipelines, such as reinforcement learning against monitors. Th...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 11 papers

- **2026-09-30** — Fabio Rovai — [Who Verifies the Graph? Misspecification Attacks on Causal Action Verification for Language Agents](http://arxiv.org/abs/2609.40027v1)
  <details><summary>📄 Abstract</summary>
  Causal action verifiers gate an agent's state-changing tool calls by checking whether each proposed intervention is identifiable against a committed action-state graph, and they issue a certificate that carries the identification argument and a one-sided lower confidence bound. One such verifier, CIVeX, reports zero false executions on a confounded tool-use benchmark. We red-team it by corrupting only the committed graph. Omitting a single bidirected edge takes it from zero false executions to 1...
  </details>

- **2026-09-30** — Kemou Li, Qizhou Wang, Yue Wang et al. — [Preemptive LLM Unlearning against Forbidden Capability Acquisition via Gradient Sealing](http://arxiv.org/abs/2609.39866v1)
  <details><summary>📄 Abstract</summary>
  Open-weight LLMs are released not only as fixed products but also as substrates for downstream fine-tuning. This openness, however, creates legal and ethical risks because users may misuse fine-tuning to instill illicit knowledge or enable hostile operations. Model providers therefore need apre-release defense against such acquisition, motivating the problem of preemptive unlearning. Unlike retrospective unlearning, which removes capabilities already present in a fixed model, preemptive unlearni...
  </details>

- **2026-09-30** — Xinwei Zhang, Aoting Hu, Hangcheng Liu et al. — [SteerProbe: Learning to Bypass Safety Steering in Vision-Language Models](http://arxiv.org/abs/2609.39117v1)
  <details><summary>📄 Abstract</summary>
  Activation steering offers an inference-time defense for vision--language models (VLMs) by modifying intermediate representations without updating backbone parameters. However, protection on benchmark inputs may not persist across alternative expressions of the same harmful request. We investigate this gap using fixed textual, visual, and joint reformulations designed to preserve the underlying intent, and find that these changes can bypass representative steering defenses. A complementary local...
  </details>

- **2026-09-30** — Pinaki Mohanty, Haoran Tang, Maggie Makar et al. — [Learning What to Forget: Distributional Unlearning for LLM Representation Spaces](http://arxiv.org/abs/2609.38929v1)
  <details><summary>📄 Abstract</summary>
  Machine learning systems increasingly face the need to remove the influence of entire data domains, such as toxic language, harmful behavior, or topical content, rather than isolated records. Recent work formalizes this problem as \emph{distributional unlearning}: selecting a subset of a forget domain whose removal moves the training distribution away from an unwanted population while preserving proximity to the desired one. However, existing analyses often impose parametric assumptions to obtai...
  </details>

- **2026-09-30** — Yuanhe Zhang, Ziwei Wang, Jie Ren et al. — [When Reasoning Goes Astray: Attention Dynamics of Uncontrolled Reasoning](http://arxiv.org/abs/2609.38817v1)
  <details><summary>📄 Abstract</summary>
  Large reasoning models (LRMs) improve performance on complex tasks through extended reasoning, yet the same process can degenerate into redundant verification and persistent generation loops. Such uncontrolled reasoning increases inference cost and creates risks of resource exhaustion and service degradation. However, existing mitigations largely truncate long outputs or react to surface repetition, and thus fail to distinguish normal thinking from uncontrolled reasoning or explain how benign re...
  </details>

- **2026-09-29** — Parisa Salmani, Peter R. Lewis — [Evaluating Language Model Safety Across Long Adversarial Conversations](http://arxiv.org/abs/2609.38357v1)
  <details><summary>📄 Abstract</summary>
  Conversational safety evaluations often test language models with a single harmful prompt, even though real-world systems interact with users through long, adaptive conversations. This study examines whether models continue to respond safely when an adversarial user persists across multiple turns. We evaluate three open-weight, instruction-tuned models on two harmful prompts across different conversation lengths and random seeds. In each setting, a second language model acts as a persistent adve...
  </details>

- **2026-09-29** — Longxuan Yu, Bingsen Chen, Peng Shi et al. — [DEdit: Iterative Draft Editing for Speculative Decoding](http://arxiv.org/abs/2609.38510v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates autoregressive LLMs by having a lightweight drafter propose tokens that the target model verifies in parallel. Diffusion-based drafters further reduce drafting latency by proposing multiple tokens at once. However, these tokens are predicted independently, so a single early error causes prefix verification to discard the rest of the draft, even when it contains useful downstream predictions. We introduce DEdit, a diffusion-based drafter that can not only draft by...
  </details>

- **2026-09-29** — Edoardo Bolzoni, Valerio Capraro — [Gender bias across LLMs is common and highly heterogeneous](http://arxiv.org/abs/2609.38036v2)
  <details><summary>📄 Abstract</summary>
  Understanding gender biases in large language models (LLMs) is increasingly important as these systems become embedded in decision-support tools with real consequences. Prior research has focused only on a small set of models, leaving open the extent to which gender biases are common and heterogeneous across LLMs. We address this gap across ten models released between April 2025 and June 2026, spanning nine vendors, using two paradigms: gender attribution to stereotyped phrases (Study 1) and mor...
  </details>

- **2026-09-29** — Gonçalo Paulo, Louis Jaburi, Nora Belrose et al. — [The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment](http://arxiv.org/abs/2609.37914v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models on narrow, misaligned tasks can undo their post-training alignment and induce novel misaligned behaviors -- a phenomenon known as \emph{emergent misalignment} (EM). EM has been linked to persona-like representations, where fine-tuning might reduce loss by amplifying a harmful or 'evil' persona. It remains unclear which properties of the training data drive this effect: whether all harmful examples contribute approximately equally to misalignment and whether diff...
  </details>

- **2026-09-29** — Jacob Epifano — [Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision](http://arxiv.org/abs/2609.37624v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a language model on a narrow set of harmful demonstrations, such as bad medical advice, can make it broadly misaligned on unrelated questions, a phenomenon known as emergent misalignment (EM). The usual defense is to find the offending rows and delete them, but a row locator failed our held-out test and deleting rows helps less than expected. We ask a different question: given a fixed set of poisoned rows, is it better to correct them than to remove them? We fine-tune Qwen2.5-14B-Ins...
  </details>

- **2026-09-29** — Muhammad Zeeshan Akram, Mufid Kamel Marican, Anvesh Reddy Yenugu et al. — [Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning](http://arxiv.org/abs/2609.36862v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning-as-a-service lets users adapt a safety-aligned language model to their own data, but it also creates a harmful fine-tuning attack surface: a small amount of harmful data mixed into an otherwise benign fine-tuning set can degrade the model's alignment. Two recent alignment-stage defenses address this problem at different levels of the model. Vaccine improves the robustness of hidden embeddings to the representation shifts induced by harmful fine-tuning, whereas Booster simulates harmf...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-30** — Leo Y. Lin, Mikhail Kuznetsov, Muslum Ozgur Ozmen et al. — [Refusals That Bend: Measuring and Predicting Task Malleability in Embodied VLM Planners](http://arxiv.org/abs/2609.38971v1)
  <details><summary>📄 Abstract</summary>
  Embodied vision-language models (VLMs) are increasingly deployed as high-level planners for robots because they generalize across diverse environments. However, this requires their safety alignment to also hold in unseen environments. Existing red-teaming assumes an adversary who optimizes the prompt, the pixels, or text in the environment, and existing benchmarks ask whether a planner recognizes or mitigates a hazard in a fixed scene. Neither asks whether a refusal the planner has already given...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-09-30** — Paul Le Van Kiem, Dario Shariatian, Umut Simsekli et al. — [Distribution Matching Distillation for Continuous Diffusion Language Models](http://arxiv.org/abs/2609.40235v1)
  <details><summary>📄 Abstract</summary>
  Continuous diffusion language models generate all tokens in parallel, yet high-quality generation can still require hundreds of network evaluations (NFEs). We study how distributional distillation can reduce this cost by exploiting the student's probabilistic token outputs. Our unified formulation connects the student's output parameterization to the resulting gradient estimators and yields two methods with the same student architecture and reverse-KL matching objective: Simplex-DMD uses continu...
  </details>

- **2026-09-30** — Zoe G. del Toro, Marco Túlio Quintino, Jessica Bavaresco — [Purification brings advantages in sequential quantum channel discrimination](http://arxiv.org/abs/2609.40218v1)
  <details><summary>📄 Abstract</summary>
  Purifications are often used as a convenient mathematical representation of quantum states and channels when constructing protocols for quantum information processing tasks. Although powerful, this perspective can suggest that the purifying degrees of freedom and its correlations with an environment are just a useful change of representation. Here we show how they can instead be exploited as an operational resource in sequential quantum channel discrimination, even when the environmental referen...
  </details>

- **2026-09-30** — Nai-Hui Chia, Hyunseong Kim, Chia-Ying Lin — [Shadow Quantum Singular Value Transformation with Shallow Quantum Circuits](http://arxiv.org/abs/2609.40167v1)
  <details><summary>📄 Abstract</summary>
  We introduce shadow quantum singular value transformation (Shadow QSVT): given an initial state $|ψ\rangle$, a Hermitian matrix $H$, a polynomial $f$, and a set of observables $\{O_1,\dots,O_m\}$, the goal is to estimate $\langleψ|f(H)^{\dagger}O_j f(H)|ψ\rangle$ for all $j\in\{1,\dots,m\}$. Shadow QSVT provides a systematic route to reduce the quantum resources required by standard QSVT, which constructs a unitary block-encoding of $f(H)$. It uses structure in the input state and observables, t...
  </details>

- **2026-09-30** — Lukas Thede, Shengzhuang Chen, Stefan Winzeck et al. — [Replay on Demand: An Emergent Curriculum for Balancing Adaptation and Forgetting in Continued Pretraining](http://arxiv.org/abs/2609.40089v1)
  <details><summary>📄 Abstract</summary>
  Continued pretraining enables language models to adapt to new domains and knowledge, but often at the cost of forgetting previously acquired capabilities. Replay can mitigate this trade-off, but fixed replay mixtures allocate training independently of the model's actual retention needs. We introduce Replay on Demand (RoD), which instead derives the replay allocation from the model's learning dynamics. RoD jointly prioritizes adaptation samples by their remaining learning potential and replay sam...
  </details>

- **2026-09-30** — Minki Kang, Ryo Hachiuma, Shaokun Zhang et al. — [Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents](http://arxiv.org/abs/2609.39982v1)
  <details><summary>📄 Abstract</summary>
  Terminal agents act through stochastic model generations, yet the ability to generate a useful action does not ensure its reliable execution. A poor command (e.g., wrong package install) can change the environment in ways that hinder subsequent progress, even when the model could generate a better alternative. We investigate whether allocating test-time compute at the model-harness boundary can improve action reliability and trajectory success, and what makes this allocation effective. To study ...
  </details>

- **2026-09-30** — Yuyang Wu, Yufeng Du, Hao Peng — [RoPE at the End of Its Rope? Theory, Diagnosis, and Mitigation of Long-Context Failures](http://arxiv.org/abs/2609.39929v1)
  <details><summary>📄 Abstract</summary>
  Long-context failures of RoPE-based language models can arise from RoPE's intrinsic tradeoff between maintaining stable token preferences and distinguishing nearby positions. Determining which weakness to address, and how, requires a more precise characterization of RoPE's behavior in trained models across context lengths. We address a key limitation of prior theory by allowing unequal query-key scales across RoPE frequencies, which aligns well with practical empirical observations. Our theory m...
  </details>

- **2026-09-30** — Yi Song, Dongchen Xie, Xiaoyuan Xie et al. — [COMPASS: Predicting the Relationship of Multiple Patches for Vulnerabilities with LLMs](http://arxiv.org/abs/2609.39783v1)
  <details><summary>📄 Abstract</summary>
  Modern software heavily relies on code reuse, so upstream vulnerability fixes do not automatically propagate to downstream codebases. Downstream maintainers must manually adopt patches to eliminate known risks. In practice, a single vulnerability often corresponds to multiple patches, which greatly complicates downstream patch adoption because different patch relationships imply different adoption strategies. To address this challenge, we first manually inspect large-scale multi-patch vulnerabil...
  </details>

- **2026-09-30** — Ivan Martinović, Josip Šarić, Yuki M. Asano et al. — [MC-PanDA++: Simpler, Stronger, and More Robust Domain-Adaptive Panoptic Segmentation](http://arxiv.org/abs/2609.39681v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised domain adaptation (UDA) reduces the annotation burden in panoptic segmentation by leveraging a cost-effectively labeled source domain (e.g., synthetic) and an unlabeled target domain to bridge the distribution gap. Existing panoptic UDA methods rely on teacher-student consistency learning built upon suboptimal per-pixel segmentation architectures. In contrast, state-of-the-art mask transformers are rarely adopted due to their pronounced vulnerability to confirmation bias in consiste...
  </details>

- **2026-09-30** — Eunmin Lee, Jungwoo Kim, Jong-Seok Lee — [Typographic Attack Against VLM-based AI-generated Image Detection](http://arxiv.org/abs/2609.39662v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used for AI-generated image (AIGI) detection, providing natural-language explanations for authenticity judgments. However, their ability to interpret text within images may also expose these judgments to misleading semantic cues. We systematically evaluate typographic attack strategies across detection-oriented, open-weight, and commercial VLMs, considering both real-to-fake and fake-to-real attacks. Our results show that reasoning modes generally e...
  </details>

- **2026-09-30** — Minghan Wang, Boyuan Wang, Jinhang Zuo et al. — [Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?](http://arxiv.org/abs/2609.39578v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses often improve language models with human-designed workflows, but as models grow more capable, unreliable guidance can increasingly constrain their execution. We call the ability to benefit from useful guidance while overriding unreliable guidance thinking outside the box. We introduce Box$^2$-Bench, which holds the model and task fixed while varying workflow reliability to isolate how models regulate their reliance on guidance. On Box$^2$-Bench, frontier models often benefit from...
  </details>

- **2026-09-30** — Rikkert Frederix, Valentin Hirschi, Malin Sjödahl — [Exact color sums for multi-gluon amplitudes: direct, multiplet and symmetric-group Fourier methods](http://arxiv.org/abs/2609.39574v1)
  <details><summary>📄 Abstract</summary>
  We compare three approaches for computing color-summed tree-level all-gluon squared matrix elements: evaluation using direct contraction in the trace and adjoint decompositions, orthonormal multiplet bases, and fast Fourier transforms (FFT) based on the irreducible representations of the symmetric group for the trace and adjoint decompositions. The multiplet method reduces the color sum to a sum of absolute squares and utilizes an amplitude recursion labeled by SU(3) representations. The FFT exp...
  </details>

- **2026-09-30** — Shouli Wang, Yanfeng Jia, Zhihao Ou et al. — [CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL](http://arxiv.org/abs/2609.39533v1)
  <details><summary>📄 Abstract</summary>
  During reinforcement learning with verifiable rewards (RLVR), large language models (LLMs) can exploit loopholes in their environments to obtain high rewards without improving the intended capabilities, i.e., reward hacking. Despite its risks to training efficiency and safety, monitoring and mitigating reward hacking during training remain challenging, which is limited by a lack of testbeds that reproduce hacking and reliably identify it. We introduce CATCH, a controllable testbed for studying r...
  </details>

- **2026-09-30** — Hung Phan, Thuy T. Nguyen, Minh Ngoc Dinh et al. — [Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models](http://arxiv.org/abs/2609.39445v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) commonly adapt to new data by attaching a single trainable head to a frozen backbone, a one-size-fits-all setup that underfits heterogeneous regimes. Replacing the head with a mixture of experts is the standard upgrade, but on instance-normalized backbones (the dominant TSFM design class) it fails: routing entropy collapses to zero and one expert absorbs every input, a failure we call normalization-induced routing collapse. Standard MoE rescue mechanisms do ...
  </details>

- **2026-09-30** — Zifei Li, Shaohuan Zu, Haojun Chen — [Iterative separation of coherent blended signals in common shot gathers using synchrosqueezed curvelet-Radon constraints](http://arxiv.org/abs/2609.39354v1)
  <details><summary>📄 Abstract</summary>
  Blended data acquired via simultaneous-source seismic exploration conventionally require post-acquisition deblending, which typically relies on the coherence differences introduced by firing time delays (time dithering). To reduce the dependency of the deblending process on these time dithers, a novel joint constraint based on the synchrosqueezed transform and the Radon transform is proposed, operating directly in the common-shot gather (CSG) domain. Specifically, by exploiting the differences i...
  </details>

- **2026-09-30** — Daniel Dragonevskiy — [Understanding as No-Arbitrage: Bounded Dutch Books as a Definition and Training Objective for Language Models](http://arxiv.org/abs/2609.39341v1)
  <details><summary>📄 Abstract</summary>
  Does a language model merely predict tokens, or does it understand what it says? We make this question measurable by defining "understanding" through the lens of no-arbitrage. A model understands a vocabulary to a certain degree if a computationally bounded trader cannot extract guaranteed profit by betting against the model's probabilities on logically related claims (a "Dutch book"). We establish three theoretical results: first, because full logical coherence is computationally intractable, u...
  </details>

- **2026-09-30** — Jiaming Zhang, Yuwan Liu, Yue Huang et al. — [MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate](http://arxiv.org/abs/2609.39297v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents powered by large language models (LLMs) are rapidly evolving into an open agentic ecosystem. To support trustworthy collaboration, industry initiatives increasingly assess agent reputation from past behavior and provide performance leaderboards. However, reputation derived from past performance may not reliably predict an agent's behavior on new tasks, particularly when malicious agents can adapt their behavior and influence other agents during collaboration.   We study reputat...
  </details>

- **2026-09-30** — Jiaqing Li, Shide Zhou, Zhibo Zhang et al. — [Faithful Dual-constrained Erasure for Robust LLM Safety Alignment](http://arxiv.org/abs/2609.39279v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning has emerged as a crucial mechanism for removing hazardous knowledge and enforcing safety alignment in Large Language Models (LLMs). However, recent studies reveal a persistent security risk: unlearned models remain highly vulnerable to retraining attacks, where suppressed malicious behaviors rapidly resurface after benign fine-tuning. In this work, we investigate the optimization dynamics of unlearning and identify that this vulnerability stems from shallow alignment. Rather t...
  </details>

- **2026-09-30** — Shailendra Bhandari, Alex Szorkovszky, Anis Yazidi et al. — [Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes](http://arxiv.org/abs/2609.39239v1)
  <details><summary>📄 Abstract</summary>
  How search strategies evolve in finite, depletable landscapes remains a question in foraging theory. We study this problem with an evolutionary simulation in which agents forage on a two-dimensional toroidal lattice containing non-renewable resources distributed uniformly or as Lévy dust. Each agent carries a heritable genome encoding step lengths, velocities, and turning angles, and selection acts on a fitness function combining energetic gain, movement cost, and coverage efficiency. By allowin...
  </details>

- **2026-09-30** — Shiyang Liu, Weiquan Lin, Luping Xiao et al. — [GRC-Pose: Generation-Reconstruction Correspondence for Prior-Free 6D Object Pose Tracking](http://arxiv.org/abs/2609.39116v1)
  <details><summary>📄 Abstract</summary>
  Prior-free 6D object pose tracking seeks to recover the trajectory of an unseen object from a single RGB video without object-specific CAD models, posed reference images, or pose annotations. Geometric foundation models provide complementary object-centric and scene-centric cues, yet SAM3D CAD is indexed by an arbitrary object-local surface parameterization, whereas reconstructed evidence is expressed in a sequence-specific world frame with partial surface coverage. To exploit this complementari...
  </details>

- **2026-09-30** — Yan Wang, Zhihao Zhang, Ke Chen et al. — [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](http://arxiv.org/abs/2609.39065v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on installable skills, which are packages of instructions, code, and resources that equip them with task-specific capabilities and, once installed, can be automatically invoked across subsequent user tasks. This creates a chain of trust in which users delegate authority to agents, while agent frameworks admit skill-provided content into the agents' context with insufficient validation, allowing malicious skills to influence agent behavior under that delegated authori...
  </details>

- **2026-09-30** — Guanqun Yang, Yingming Zhou, Jiangrui Zheng et al. — [PatchHolmes: Agentic Patch Retrieval via Listwise Selection](http://arxiv.org/abs/2609.38807v1)
  <details><summary>📄 Abstract</summary>
  Patch retrieval, the task of finding the commit that fixes a known vulnerability, is the foundation of vulnerability management workflows, yet 60% to 63% of CVEs in the major advisory databases lack a patch link. We present PatchHolmes, a two-phase patch retrieval system that pairs a hybrid first-stage retriever with an agentic second-stage inspection loop. Unlike pointwise prior work that scores each candidate independently, the Phase 2 agent reads the top-100 listwise: it sees the full candida...
  </details>

- **2026-09-30** — Simon Foucart, Jingchun Shao — [Worst-Case Completion of Tensors with Approximately Few ANOVA Terms](http://arxiv.org/abs/2609.38749v1)
  <details><summary>📄 Abstract</summary>
  In this article, the problem of completing a tensor from some incomplete knowledge of its entries is treated by adopting a worst-case perspective, given the realistic assumption that the tensor's low-order ANOVA terms are dominant. We survey and leverage some recent all-purpose results from the field of Optimal Recovery to provide solutions on a theoretical level. But the accompanying constructions of optimal completion procedures, which often feature semidefinite programs, are not directly appl...
  </details>

- **2026-09-30** — Junyang Xia, Luocheng Zhang, Wenwen Pan et al. — [Consensus-Aware Multi-Source Fusion for Reference-Guided Camouflaged Object Detection](http://arxiv.org/abs/2609.38747v1)
  <details><summary>📄 Abstract</summary>
  Reference-guided camouflaged object detection aims to segment a target whose visual appearance closely resembles its surroundings by exploiting auxiliary reference samples. The task remains difficult because reference samples contain inconsistent target cues, while generic visual representations are not inherently aligned with the target specified by the references. To handle these problems, we present a consensus-aware multi-source fusion framework. Reference-Conditioned Dual-Backbone Fusion (R...
  </details>

- **2026-09-30** — Haichuan Li — [Bounded Channel-Adaptive Spectral Learning for Forward-Consistent Inverse Flapping-Wing Aerodynamics](http://arxiv.org/abs/2609.38730v1)
  <details><summary>📄 Abstract</summary>
  Flapping-wing vehicles regulate aerodynamic forces and moments through coordinated variations in stroke, deviation, and pitch motion. Because the resulting loads depend on both the instantaneous wing configuration and its preceding motion history, recovering suitable wing kinematics from a desired aerodynamic trajectory is a challenging inverse problem. Existing sequence models capture temporal dependencies, while spectral methods can exploit the periodic structure of flapping motion. However, u...
  </details>

- **2026-09-30** — Yufei Wei, Shuhao Ye, Qi Wang et al. — [StreamRig: Exploiting Intra-Rig Geometry for Streaming Multi-Camera Odometry](http://arxiv.org/abs/2609.40244v1)
  <details><summary>📄 Abstract</summary>
  Mobile robots and vehicles carry synchronized multi-camera rigs, yet many streaming 3D foundation models are designed for monocular input, leaving efficient use of rig geometry a challenge. We present StreamRig, a freeze-and-stream framework that builds causal streaming odometry for calibrated rigs on a frozen multi-view 3D foundation model. The frozen front-end jointly perceives the synchronized views using rig calibration. A Rig-Resampler compresses their features, a CausalBridge applies causa...
  </details>

- **2026-09-29** — Hung-Jen Chen, Yu-Heng Ho, Ting-Yao Huang et al. — [Inductive Visual Logic for Few-Shot Out-Of-Distribution Adaptation in VLMs](http://arxiv.org/abs/2609.38362v1)
  <details><summary>📄 Abstract</summary>
  Generative vision-language models (VLMs) such as Qwen-VL and LLaVA achieve strong zero-shot performance on tasks overlapping with their pretraining distribution, yet fail on specialized domains where the required discriminative features were never learned, a regime we term distant out-of-distribution (OOD). Standard adaptation methods cannot overcome this representational absence because they operate within the encoder's existing feature space. However, VLMs retain a robust descriptive capacity ...
  </details>

- **2026-09-29** — Prithwish Jana, Mononito Goswami, Hao Liu et al. — [MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution](http://arxiv.org/abs/2609.38349v1)
  <details><summary>📄 Abstract</summary>
  Modern agentic systems combine an AI model with a harness that controls execution and environmental interactions. Harness design strongly affects long-horizon performance, yet its combinatorial search space demands substantial human effort that must be repeated as models change. Existing automated methods explore this space narrowly, optimizing only components such as prompts or skills or becoming trapped by fixed, exploitative search strategies. We introduce MILO (Meta-evolutionary Island Orche...
  </details>

- **2026-09-29** — Ozgur Can Seckin, Shalmoli Ghosh, Alessandro Flammini et al. — [AI Agents are Vulnerable to Radicalization](http://arxiv.org/abs/2609.38296v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can influence people's beliefs, yet little is known about whether and how they can manipulate each other. To investigate this, we simulate conversations between two agents: a target LLM that role-plays a human persona based on demographic and psychological attributes, and an influencer LLM that aims to make the target's beliefs more extreme. We examine radicalization along two pathways: resonance, where the influencer reinforces a target's pre-existing belief, and pe...
  </details>

- **2026-09-29** — Zhuo Liu, Moxin Li, Zhixin Ma et al. — [HARDE: Optimizing Agent Harnesses for Runtime Risk Detection and Execution Control](http://arxiv.org/abs/2609.38291v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are vulnerable to safety risks such as injected malicious instructions or misleading information, motivating runtime defenses that prevent unsafe action in execution across diverse risks while preserving benign-task utility. Existing system-level defenses either focus on risk detection rather than timely prevention or rely on predefined rules with limited flexibility across diverse risks. We propose a risk-aware harness that integrates LLM-based monitoring for f...
  </details>

- **2026-09-29** — Weixuan Li, Zikun Zhou, Xinyi Zhuang et al. — [Representation Dynamics Reveal Semantic Saliency and Similarity for Visual Token Pruning in MLLMs](http://arxiv.org/abs/2609.36916v2)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) incur high inference latency from long visual token sequences. Existing pruning methods commonly use attention maps or output features to estimate token importance or redundancy. Several recent approaches also exploit representation changes, but when and how these changes reflect foreground saliency and semantic consistency remain insufficiently understood. We analyze visual token representation dynamics across encoder depth and uncover two findings. Firs...
  </details>

- **2026-09-29** — Gita Rani Mahato, Manab Kundu — [Analysis of Delay Differential Equations Using the Offset Linear Canonical Transform](http://arxiv.org/abs/2609.36792v2)
  <details><summary>📄 Abstract</summary>
  Motivated by the work of Ohira and the advantages of the offset linear canonical transform (OLCT) over the Fourier transform (FT), this paper proposes an OLCT based framework for solving a class of delay differential equations. By exploiting the operational properties of the OLCT, the original delay differ- ential equation is transformed into a Volterra-type delay integral equation in the transform domain and solved numerically using Brunners method of steps . An explicit analytical solution is ...
  </details>

- **2026-09-29** — Dor Tirosh, Ido Amos, Mor Geva — [Pretraining Latent Information Feedback Transformers with Teacher Supervision](http://arxiv.org/abs/2609.38149v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models (LMs) are feed-forward: deep-layer representations are never fed back to shallower layers, and the only pathway for information to flow downward across generation steps is the decoded token. This narrow channel forces models to recompute intermediate results and to discard alternative continuations. In this work, we remove this bottleneck during pretraining, introducing the LIFT (Latent Information Feedback Transformer) architecture and training method which enable LM...
  </details>

- **2026-09-29** — Timur Mudarisov, Mikhail Burtsev, Tatiana Petrova et al. — [Predictive Geometry of Hidden Trajectories in Transformers](http://arxiv.org/abs/2609.37717v1)
  <details><summary>📄 Abstract</summary>
  Decoder-only transformers are trained only through a terminal next-token prediction loss, yet this loss constrains every intermediate hidden state through the fixed downstream computation. We formalize this constraint by studying layerwise loss-to-go functions: the terminal loss obtained by continuing a candidate hidden state through the remaining transformer blocks. Around successful validation trajectories, we show that the local second-order geometry of these functions is governed, up to low-...
  </details>

- **2026-09-29** — Bastien Lechardoy, Pau de las Heras Molins, Thibault Lahire et al. — [Cascaded consensus splitting for multi-branch contingency games](http://arxiv.org/abs/2609.37612v1)
  <details><summary>📄 Abstract</summary>
  Contingency games enable agents to anticipate and plan for other agents' hypothetical intents by constructing trajectories with a shared prefix and intent-dependent branches. While contingency games capture intent uncertainty, existing formulations rely on a single branching time, oversimplifying interactions in which different agents' intentions are revealed at different times. Moreover, the computational cost of such problems grows rapidly with the number of agents and intents, as all scenario...
  </details>

- **2026-09-29** — Zheng Zhang, Xinyue Tan, Lufei Li et al. — [Train Ahead, Distill Back: Bootstrapping On-Policy Self-Distillation for Large Language Models](http://arxiv.org/abs/2609.37132v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) improves large language models by letting a self-teacher with privileged information provide dense token-level supervision on the model's own trajectories. Yet existing methods typically construct the self-teacher from the current, initial, or slowly averaged policy state, leaving the quality of supervision constrained by the teacher's ability to exploit privileged information. We ask whether the model's own optimization progress can instead be recycled into a ...
  </details>

- **2026-09-29** — Zhuo Chen, Hao Zeng, Jiawei Liu et al. — [Breaking the Illusion of Review Reliability under Static Evaluation: SCOPE Fuzzing for LLM-based Scientific Reviewers](http://arxiv.org/abs/2609.37097v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of submissions and reviewing workload has accelerated the use of large language models (LLMs) in peer review. Prior studies suggest that LLM-based reviewers can penalize content perturbations, such as overclaiming, indicating a certain degree of reliability. Yet these conclusions are largely based on a narrow set of perturbation strategies instantiated with static templates, providing limited evidence of actual reliability. In this paper, we construct a three-level evaluation fr...
  </details>

- **2026-09-29** — Zhenyu Liu, Zhangquan Chen, Keyi Chen et al. — [Spatial-OPSD: Self-Improving Spatial Reasoning via Label-Free Self-Distillation](http://arxiv.org/abs/2609.37055v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) increasingly operate in embodied and spatially grounded settings, where accurate understanding of depth, viewpoint, and three-dimensional relations is essential. However, improving spatial reasoning typically relies on ground-truth answers, answer-derived rewards, or other forms of task-specific supervision. We introduce Spatial-OPSD, a label-free self-improvement framework that instead exploits spatial structure naturally available from perception and reconstructio...
  </details>

- **2026-09-29** — Katharina Winter, Stefan Englmeier, Fabian B. Flohr — [Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving](http://arxiv.org/abs/2609.37046v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models are increasingly used in autonomous-driving systems, yet their ability to recover dynamic physical state from visual input remains insufficiently characterized. We study velocity understanding as a controlled diagnostic across three tasks: surrounding-agent speed, current ego speed, and short-horizon future ego-speed proposal. On nuScenes, we evaluate open-weight general-purpose and PhysicalAI VLMs, together with the driving-oriented Alpamayo-1.5 Vision-Language-Action mod...
  </details>

- **2026-09-29** — Hafsa El Herichi, Arturo Mendoza, Yanneck Wielhorski et al. — [Periodicity and image registration for yarn path extraction in large 3D textiles](http://arxiv.org/abs/2609.36991v1)
  <details><summary>📄 Abstract</summary>
  Accurate identification of yarns in X-ray computed tomography volumes remains a critical and complex step in generating high-fidelity numerical models of woven composites. This work introduces a tracking framework that leverages the intrinsic periodicity of woven architectures to transform a complex, large-scale segmentation problem into the annotation of a single representative unit cell. The approach first exploits the periodic nature of the weave to extract a representative unit cell from the...
  </details>

- **2026-09-29** — Weixuan Li, Zikun Zhou, Xinyi Zhuang et al. — [Representation Dynamics Reveal Semantic Saliency and Similarity for Visual Token Pruning in MLLMs](http://arxiv.org/abs/2609.36916v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) incur high inference latency from long visual token sequences. Existing pruning methods commonly use attention maps or output features to estimate token importance or redundancy. Several recent approaches also exploit representation changes, but when and how these changes reflect foreground saliency and semantic consistency remain insufficiently understood. We analyze visual token representation dynamics across encoder depth and uncover two findings. Firs...
  </details>

- **2026-09-29** — Gita Rani Mahato Manab Kundu — [Analysis of Delay Differential Equations Using the Offset Linear Canonical Transform](http://arxiv.org/abs/2609.36792v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the work of Ohira and the advantages of the offset linear canonical transform (OLCT) over the Fourier transform (FT), this paper proposes an OLCT based framework for solving a class of delay differential equations. By exploiting the operational properties of the OLCT, the original delay differ- ential equation is transformed into a Volterra-type delay integral equation in the transform domain and solved numerically using Brunners method of steps . An explicit analytical solution is ...
  </details>

- **2026-09-29** — Runbing Zheng, Dmitriy Kunisky — [Global Synchronization for Multi-Source Data Integration under Blockwise Missing Patterns](http://arxiv.org/abs/2609.38141v1)
  <details><summary>📄 Abstract</summary>
  Multi-source data integration problems over datasets from different sources covering different but possibly overlapping sets of entities have become increasingly important in many real-world areas, including genomics, single-cell analysis, and healthcare research. In such problems, one often first learns a low-dimensional representation of the entities within each source and then integrates these representations across sources. As the representations from different sources are only identifiable ...
  </details>

- **2026-09-29** — Zheng Jiang, Houde Qian, Yiming Chen et al. — [VISTA: Internalizing Collective Visual Experience via On-Policy Distillation for Active Multimodal Agents](http://arxiv.org/abs/2609.38086v1)
  <details><summary>📄 Abstract</summary>
  Active multimodal agents use visual tools to acquire task-relevant evidence while reasoning. Although reinforcement learning samples multiple interaction trajectories per input, outcome-based objectives primarily use the group to estimate scalar advantages, leaving complementary visual discoveries underused. We introduce VISTA, which internalizes collective visual experience through on-policy distillation by turning observations from same-input rollouts into shared supervision. Collective visual...
  </details>

- **2026-09-29** — Haotian Deng, Wenbin Xing, Gang Xu et al. — [Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment](http://arxiv.org/abs/2609.37837v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses. Existing safety methods often require large preference datasets, costly multi-rollout training, or additional safeguards at inference time. They may also sacrifice helpfulness by directly refusing requests that could be answered safely. In this paper, we propose Intent-Privilege On-Policy Self-Distillation (OPSD), which leve...
  </details>

- **2026-09-29** — Biswajit Banerjee, Claudia Alvarez Carreno, Anton S. Petrov — [LEMON-ZEST: Evolution-Informed Tokenization for Efficient Protein Language Modeling](http://arxiv.org/abs/2609.37675v1)
  <details><summary>📄 Abstract</summary>
  Protein Language Models (PLMs) have made remarkable progress following scaling laws established in natural language processing across sequence- and structure-based tasks, yet the potential of tokenization remains underexploited. Unlike human language, proteins preserve structure despite extensive sequence variation a property standard tokenization strategies fundamentally fail to capture. We introduce ZEST (Zoned Encoding of Sequence Traits), an evolution-informed vocabulary derived from conserv...
  </details>

- **2026-09-29** — Sabrina Kaniewski, Tim Krämer, Julius Bächle et al. — [Retrieve, Reproduce, Reveal: Dissecting Retrieval-Augmented Software Vulnerability Detection](http://arxiv.org/abs/2609.37669v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is increasingly used to enhance Large Language Model (LLM)-based software vulnerability detection by grounding predictions in retrieved vulnerability knowledge, such as vulnerability reports. However, existing RAG-based software vulnerability detection (RAG4SVD) systems are often evaluated using proprietary models, which challenges open science and reproducibility. Further, studies use different datasets, custom knowledge bases, different backbone models, and...
  </details>

- **2026-09-29** — Giovanni Marraffini, Victoria Shevchenko, Carlo Alberto Barbano et al. — [Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders](http://arxiv.org/abs/2609.37642v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pretraining reshaped prediction in language and vision, and brain foundation models (BFMs) inherited its promise. Representations learned from large unlabelled corpora should capture individual functional dynamics and generalise across cohorts. However, kernel ridge regression (KRR) fitted on functional connectivity (FC) matrices still predicts individual phenotypes more accurately than any BFM we tested. In this paper, we show that KRR is weighted by the eigenvalues of the FC wh...
  </details>

- **2026-09-29** — Tianhang Pan, Xuanhao Wang, Yiwen Pang et al. — [CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts](http://arxiv.org/abs/2609.37150v1)
  <details><summary>📄 Abstract</summary>
  VLAs combine pretrained vision-language representations with action generation to enable language-guided control across diverse tasks, becoming a mainstream paradigm in embodied intelligence. However, multiple studies have reported VLA's substantial declines in task success under camera shifts, revealing a key vulnerability that limits reliable deployment. To address this vulnerability, existing methods collect paired observations of the same scene from different viewpoints to fine-tune the VLA ...
  </details>

- **2026-09-29** — Ji He, Huang Zhang, Lijie Zheng et al. — [One Pipeline Does Not Fit All: TAILOR, a Type- and State-Aware Framework for CVE Reproduction](http://arxiv.org/abs/2609.37006v1)
  <details><summary>📄 Abstract</summary>
  Growing vulnerability disclosure and widespread software reuse increase security teams' need for reproducible evidence to diagnose vulnerabilities, validate patches, and build regression tests. Producing such evidence at scale requires automated end-to-end CVE reproduction. Existing methods typically process different CVEs through a uniform pipeline, but differences in runtime form, trigger interfaces, and prerequisite state impose different execution requirements on individual stages, making fi...
  </details>

- **2026-09-29** — Wan Tian, Zhongyi Li, Yawen Li et al. — [Beyond Sub-Gaussian Detector Scores: Robust Weighted Profile-Loss Change Point Detection for Human-LLM Text Segmentation](http://arxiv.org/abs/2609.36888v1)
  <details><summary>📄 Abstract</summary>
  Mixed human-LLM documents require locating authorship transitions from detector scores whose reliability varies across text units. Existing weighted mean contrasts are vulnerable to extreme scores, while directly replacing means with robust centers obscures how a misplaced boundary changes the population objective. We propose Robust Weighted Profile-Loss Change Point Detection (RWCP), which combines capped reliability weights, Huber profile gains, and narrowest-over-threshold search in reliabili...
  </details>

- **2026-09-29** — Yueran Ma, Ronghao Lin — [Seeing What Should Be Heard: Diagnosing and Repairing Cross-Modal Shortcuts in Omni-Modal LLMs](http://arxiv.org/abs/2609.36798v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models (LLMs) are expected to answer a question using the modality it explicitly refers to. However, existing training paradigms rarely verify whether models actually follow this modality, because multimodal inputs from the same sample often provide redundant evidence for the same answer. In this work, we uncover a pervasive cross-modal shortcut in omni-modal LLMs: when asked an audio-related question, models rely on the image as much as on the audio, and sometimes even...
  </details>

- **2026-09-29** — Aram Davtyan, Pablo Acuaviva, Sebastian Stapf et al. — [Emergent Specialization in Populations of Self-Supervised Collaborative Vision Experts Without a Shared Gate or Cross-Agent Gradients](http://arxiv.org/abs/2609.36770v1)
  <details><summary>📄 Abstract</summary>
  Can a population of neural networks develop a useful division of labor without a shared gate or gradients between agents? We study a setting where each network has its own weights, trains independently on the same heterogeneous data, and can ask another agent for help through a forward pass. Unlike mixtures of experts, where a jointly trained gate assigns inputs to experts, specialization here must emerge without central control. We test this in a small scale proxy for predictive visual pretrain...
  </details>

- **2026-09-29** — Muyang Li, Jie Yang, Zhengyu Fang et al. — [PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning](http://arxiv.org/abs/2609.36642v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents are usually trained by reinforcement learning from one reward per episode, and privileged self-distillation enriches it by letting the same policy, given a skill, teach its skill-free self through token probabilities. However, we identify two phenomena that question this channel. Invisible Advantage: a skill in context lifts WebShop success from 42.2% to 56.2%, yet changes the probabilities of fewer than a quarter of the sampled tokens. Much to Align: a skill changes the hi...
  </details>

- **2026-09-29** — Sujin Chen, Lijun Li, Xuhong Wang et al. — [CyberPersistBench: Evaluating LLM-Based Cyber Attackers on Installation and Persistence](http://arxiv.org/abs/2609.36573v1)
  <details><summary>📄 Abstract</summary>
  While LLM-based attackers exhibit growing proficiency in vulnerability exploitation, most existing cybersecurity benchmarks suffer from single-stage truncation, prematurely terminating evaluation upon initial access. In practice, initial footholds are exceptionally fragile across operational disruptions such as service restarts and host reboots. Whether LLM-based attackers can establish and maintain durable footholds beyond initial compromise remains a central blind spot in cybersecurity evaluat...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 47 papers

- **2026-09-30** — Rong Wan, Wei Xie, Jiaxi Li et al. — [SE-ADD: Self-Evolving Audio Deepfake Detection with Mistake-Driven Supervision](http://arxiv.org/abs/2609.39679v1)
  <details><summary>📄 Abstract</summary>
  Audio deepfake detection (ADD) must remain effective when new spoofing attacks emerge after deployment. Emerging audio language model (ALM)-based ADD methods are built on predefined supervision from ground-truth labels or verified forensic rationales. However, this paradigm overlooks an ALM's own mistakes, which indicate where targeted supervision is most needed. To this end, we first introduce evolving spoofing environments for ALM-based ADD, where a new attack becomes dominant while previously...
  </details>

- **2026-09-30** — Tobias Kaisar, Aritra Dhar — [Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents](http://arxiv.org/abs/2609.39607v1)
  <details><summary>📄 Abstract</summary>
  Skills extend an agent's capabilities by injecting instructions and information into the context, and are widely used by agents such as OpenClaw and Claude Code. Prior work shows third-party marketplaces host malicious skills that give attackers direct influence over the victim's agent. The emerging defense scans skills before installation, pairing deterministic static checks with an LLM-based semantic judge, as in NVIDIA's SkillSpector. We show that such defenses fall to an attacker who knows t...
  </details>

- **2026-09-30** — Zezhong Wang, Xueyang Tang, Rui Lian et al. — [Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks](http://arxiv.org/abs/2609.39549v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Model (LLM) agents are increasingly deployed in complex environments, multi-turn interaction attacks have become a significant security challenge. Existing detection methods typically rely on historical context. However, this retrospective logic struggles to identify deep malicious intents that are split across turns to hide future risks. Inspired by speculative decoding, we propose the Speculative Safety Honeypot (SSH) framework. SSH uses a multi-agent simulation system compos...
  </details>

- **2026-09-30** — Soohan Lim, Hyundong Jin, Yo-Sub Han — [SEW: Style-Encoded Watermarking of LLM-Generated Code](http://arxiv.org/abs/2609.39414v1)
  <details><summary>📄 Abstract</summary>
  Code watermarking supports provenance tracking for code generated by LLMs. Modifying token selection to embed watermarks as an LLM generates code can create a trade-off between detectability and functional correctness. Other methods instead watermark completed code using predefined transformations or trained neural models. Recurring patterns can make watermark choices predictable across programs, while treating patterns common in unwatermarked code as watermark evidence can cause false detection...
  </details>

- **2026-09-30** — Dixi Yao, Kaiwen Chen, Tahseen Rabbani et al. — [Persistent Watermarking of Text-to-Image Models](http://arxiv.org/abs/2609.39024v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image (T2I) generation is gaining increasing popularity with the general public, motivating the development of reliable mechanisms for copyrighting such models given their expensive training costs. An adversary may obtain and reuse a pretrained T2I model without authorization, and then serve a modified version through an API service. Such modifications may arise from ordinary downstream adaptation or deliberate attempts to erase ownership, including input-prompt preprocessing, model fine...
  </details>

- **2026-09-30** — Xinhe Tian, Xiaoyue Zhang, Ziyou Zhang et al. — [STRATA: Self-Learning Through Role-Aligned Tiered Agents for Real-Time Strategy Games](http://arxiv.org/abs/2609.38881v1)
  <details><summary>📄 Abstract</summary>
  Real-time strategy (RTS) games require agents to coordinate economic development, production and construction, base defense, unit organization, and attack timing over long matches. Existing studies have applied large language models to command decision-making in RTS games, enabling agents to read textual game states and generate high-level plans. However, long inference latency can cause them to miss critical tactical events. The complexity and tactical diversity of full RTS matches also leave e...
  </details>

- **2026-09-30** — Yanbei Chen, Anirudh Goyal, Raghuraman Krishnamoorthi — [Scaling Laws for Looped Mixture of Experts](http://arxiv.org/abs/2609.40316v1)
  <details><summary>📄 Abstract</summary>
  Looped transformers and Mixture-of-Experts (MoE) offer complementary routes to efficient scaling: recurrence increases computational depth at fixed parameters, while MoE sparsity expands total capacity at fixed active compute. Yet existing scaling laws model recurrence or sparsity in isolation. In this work, we introduce Loop Scaling Laws, the first scaling law to jointly model recurrence and sparsity alongside model size and data. At its core is a bounded, sparsity-conditional recurrence mappin...
  </details>

- **2026-09-30** — Jungwoo Kim, Joonyong Park, Junyoung Koh et al. — [Neural Audio Codec for Robust Audio Deepfake Detection](http://arxiv.org/abs/2609.39651v1)
  <details><summary>📄 Abstract</summary>
  Audio deepfake detectors are typically evaluated on uncompressed audio, although real-world audio often undergoes low-bitrate coding. In this work, we investigate how audio coding affects deepfake detection across codecs, bitrates, and detectors, finding higher errors at lower rates. A mixed-pair protocol isolates codec-induced changes in bona fide and spoof audio, revealing asymmetric, codec-dependent failures: low-rate DAC and EnCodec mainly degrade bona fide detection, whereas X-Codec shows a...
  </details>

- **2026-09-30** — Wei Zhao, Yangshuo Zou, Chengxiang Ding et al. — [Fyan: A Human--AI Harness with Semantic Auditing for Document-Level Formalization](http://arxiv.org/abs/2609.39228v1)
  <details><summary>📄 Abstract</summary>
  We present FYAN, a human--AI harness for document-level mathematical formalization. Rather than treating theorems in isolation, FYAN coordinates an end-to-end workflow spanning specification, proof planning, logical review, Lean proof construction, knowledge curation, and validation, with support for independent supervision and human guidance. A central component is evidence-grounded semantic auditing, which assesses whether formal statements faithfully preserve their informal specifications. A ...
  </details>

- **2026-09-30** — Yan Zhang, Chuming Wei, Ruien Li et al. — [MASCRDM: Multi-Agent System for Compliance Risk Detection and Mitigation in Training Process of Large Language Models](http://arxiv.org/abs/2609.39107v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been applied in various fields. However, ensuring compliance and safety of LLMs, such as avoiding discrimination and bias, still remains a challenge. Current efforts mainly focus on detecting and filtering inputs and outputs of the trained models, rather than studying the intrinsic architecture of the models in real-time. To tackle this challenge, we analyze the LLMs training process and discover two critical issues: 1) Most of the existing methods are predomina...
  </details>

- **2026-09-30** — Gou Tan, Pengfei Chen, Zhensu Sun et al. — [Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail](http://arxiv.org/abs/2609.39086v1)
  <details><summary>📄 Abstract</summary>
  Runtime error healing lets a crashed program continue by generating code that repairs its live runtime state. Recent work shows that LLMs can generate such healing code, but it is evaluated only on small competition programs, and executing LLM-generated code inside a live process raises safety concerns that remain unaddressed. In this paper, we take LLM-based runtime healing toward practical use in real-world repositories. We first build HealBench, a benchmark of 265 runtime errors from 18 real-...
  </details>

- **2026-09-30** — Yang Wang — [Approval Laundering: Systematizing Approval--Execution Binding Failures in AI Coding-Agent Harnesses](http://arxiv.org/abs/2609.38983v1)
  <details><summary>📄 Abstract</summary>
  Modern AI coding-agent harnesses (Claude Code, Codex CLI, Cursor) rest their security boundary on a largely unexamined assumption: that the action A a human approves is the same action A' the harness executes, where A is fixed by a stated policy for what a scope grant or session-scoped approval authorizes. We show this assumption fails systematically and reproducibly. We introduce Approval Laundering, a taxonomy of six failure modes by which a harness's enforcement mechanism silently substitutes...
  </details>

- **2026-09-30** — Jahyeob Koo, Kio Yun, Byoungmo Koo et al. — [LEARN-TS: LLM-Enhanced Alignment and Reconstruction with Normality Guidance for Multivariate Time-Series Anomaly Detection](http://arxiv.org/abs/2609.38789v1)
  <details><summary>📄 Abstract</summary>
  Reconstruction errors in multivariate time-series anomaly detection may not reliably distinguish abnormal behavior from benign deviations. Language-derived semantics offer complementary context, but existing multimodal approaches may rely on time-associated paired textual information that is difficult to obtain consistently and is not provided by standard multivariate time-series anomaly detection benchmarks. This setting poses two challenges: (1) conditioning masked reconstruction on window-spe...
  </details>

- **2026-09-30** — Konstantinos Moutselos, Ilias Maglogiannis — [Tissue Detection Determines False Positives in Diffusion-Based Histopathology Artifact Detection](http://arxiv.org/abs/2609.40083v1)
  <details><summary>📄 Abstract</summary>
  One-class artifact detectors for whole-slide images learn normal tissue from a clean training pool and flag departures from it. The pool is built by a preprocessing pipeline whose tissue-detection step is usually treated as neutral. We tested whether it is. On 16 annotated TCGA slides, we rebuilt the clean pool of a diffusion-based detector with different tissue detection methods and compared the resulting models in a four-fold cross-validation. Per-slide saturation-Otsu detection excluded norma...
  </details>

- **2026-09-30** — Yijie Bian, Kai Zhang, Wei Guo et al. — [AIMS: An Agentic AI Framework for Sim-to-Real Multi-Modal ISAC](http://arxiv.org/abs/2609.39964v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal integrated sensing and communication (ISAC) enables environmental perception and reliable connectivity for intelligent wireless networks. Data-driven multi-modal ISAC models depend heavily on annotated real-world data to learn relationships across sensing and wireless observations, thereby constraining scalable deployment. Although synthetic data generation reduces the burden, adapting existing simulation pipelines to a target deployment requires consistent scene, sensing, wireless, ...
  </details>

- **2026-09-30** — Rong Wan, Suliu Qin, Jiaxi Li et al. — [SEAR: Spoofing Evidence-Grounded Audio Reasoning Benchmark for Audio Language Models](http://arxiv.org/abs/2609.39847v1)
  <details><summary>📄 Abstract</summary>
  Audio language models (ALMs) are increasingly used for audio deepfake detection (ADD), yet existing benchmarks assess their verdicts or rationale plausibility without verifying the underlying acoustic evidence. To address this issue, we first introduce spoofing evidence-grounded audio reasoning (SEAR), a four-task AQA benchmark to evaluate ALM-based ADD through acoustic evidence identification and quantification, deepfake detection, and forensic rationale generation. We further propose a bona-fi...
  </details>

- **2026-09-30** — Gianluca Inguglia, Huw Haigh, Ulyana Dupletsa et al. — [MADGRAV: a multilevel anomaly-detection pipeline for gravitational-wave searches applied to LIGO data](http://arxiv.org/abs/2609.39583v1)
  <details><summary>📄 Abstract</summary>
  We present the results of \textbf{MADGRAV}, a deep-learning-based search for high-mass compact binary coalescences, applied to the data collected by the LIGO interferometers during the third observing run and during the first and second part of the fourth observing run. The \textbf{MADGRAV} pipeline consists of a series of sequential convolutional neural networks that perform anomaly detection, glitch classification, coherence testing, and signal ranking. Data from the Hanford and Livingston LIG...
  </details>

- **2026-09-30** — Bhuvanesh Verma, Ali Abusaleh, Alexander Mehler — [TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic](http://arxiv.org/abs/2609.39385v1)
  <details><summary>📄 Abstract</summary>
  Argument Mining (AM) is a critical NLP task that remains significantly under-resourced in Arabic. This paper presents $\testtt{STAR-Ar}$, a BERT-BiLSTM-CRF architecture for argument discourse detection and classification, as our system for Daleel 2026, the inaugural Arabic argument mining shared task. The task requires the identification and classification of argumentative discourse units (ADUs) in debate and editorial texts.We jointly model these two objectives as a token-level sequence labelin...
  </details>

- **2026-09-30** — Noam Major, Kathy Razmadze, Yoli Shavit — [WinoTS: Wavelet-based Self-Distillation for Time Series Models](http://arxiv.org/abs/2609.39337v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pre-training of time series models is currently dominated by next-token prediction and reconstruction objectives. In continuous-valued domains, these paradigms often waste model capacity on high-frequency, point-wise noise at the expense of learning invariant structure. While invariance-based self-distillation has proven highly effective in computer vision, its application to temporal data remains largely underexplored. Effectively adapting such methods to time series requires ca...
  </details>

- **2026-09-30** — Francesco Spinnato — [A Time-Aware Bag-of-Receptive-Fields for Interpretable Irregular Time Series Classification](http://arxiv.org/abs/2609.39268v1)
  <details><summary>📄 Abstract</summary>
  Irregular time series, characterized by non-uniform sampling intervals, missing observations, and variable lengths, are ubiquitous in healthcare, mobility, and environmental monitoring, yet effective and interpretable classifiers for this setting are limited. Existing approaches often rely on imputation, which can obscure the temporal structure of the data, or require complex neural architectures that are opaque and difficult to explain. In this work, we extend the Bag-Of-Receptive-Fields (BORF)...
  </details>

- **2026-09-30** — Elia Onofri, Roberto Di Pietro — [RAIM: Robust Aggregation of Inexpensive Models for Hallucination Detection](http://arxiv.org/abs/2609.39229v1)
  <details><summary>📄 Abstract</summary>
  Automatic evaluation of faithfulness increasingly relies on a large language model acting as a judge, yet the most reliable judges are proprietary frontier models, costly and ill-suited to high-throughput monitoring. We investigate whether a panel of cheap open-weight judges (4--9B) can be aggregated to stand in for a frontier one, what the substitution sacrifices, and when it is worth making. We propose RAIM, an aggregation scheme robust to the members' correlated errors, coupling a cross-fitte...
  </details>

- **2026-09-30** — Yutong Deng, Qi Song, Xi Guo et al. — [CamAgent: An LLM-Agent Framework for Multi-Species Camera-Trap Workflows](http://arxiv.org/abs/2609.39112v1)
  <details><summary>📄 Abstract</summary>
  Camera traps accumulated vast, multidimensional data for wildlife monitoring, yet translating raw media archives into meaningful ecological insights remains highly fragmented. Current research workflows require laboriously stitching together disparate analysis tools and scripts, creating steep programming hurdles and complicating end-to-end spatiotemporal analyses. To overcome this fragmentation, we present CamAgent, an autonomous Large Language Model (LLM) agent framework that integrates camera...
  </details>

- **2026-09-30** — Zhiya Tan, Jing Huang, Changtao Miao et al. — [Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](http://arxiv.org/abs/2609.39066v1)
  <details><summary>📄 Abstract</summary>
  Conventional image forgery detection methods produce binary scores or pixel-level masks without interpretable evidence, while recent multimodal large language model (MLLM)-based approaches generate post-hoc explanations of predetermined classification results rather than reasoning from evidence. Inspired by the forensic workflow of human judicial experts, we propose Agentic Tool-Augmented Reasoning (ATAR), a framework integrating 22 specialized forensic tools across seven complementary domains t...
  </details>

- **2026-09-30** — Zewei Deng, Muhammad Siddeek, Liyan Xie et al. — [Anchor-ECC: Local Integrity Checking for Watermarked LLM Outputs via Error-Correcting Codes](http://arxiv.org/abs/2609.38722v1)
  <details><summary>📄 Abstract</summary>
  LLM watermarking has become an effective approach to distinguishing AI-generated text from human-written text by embedding detectable patterns during generation. However, a small post-generation edit may change the meaning of the text without removing its overall watermark signal, creating a risk that the modified content is still attributed to the original model. We propose Anchor-ECC, which incorporates the error-correcting code (ECC) constraints and explicit boundary anchors into the watermar...
  </details>

- **2026-09-29** — Alexandra Souly, Kai Fronsdal, Abby D'Cruz et al. — [Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](http://arxiv.org/abs/2609.38415v1)
  <details><summary>📄 Abstract</summary>
  This technical report presents an alignment evaluation developed and performed by the UK AI Security Institute for assessing whether advanced AI systems take unsanctioned actions outside the scope of their assigned task. We evaluate whether frontier models conduct supply-chain attacks against out-of-scope, third-party targets when placed in difficult cybersecurity challenges, motivated by recently observed cases of models attacking real open-source repositories during evaluations. Applying our m...
  </details>

- **2026-09-29** — Amir-Hossein Shahidzadeh, Seungjae Lee, Eadom Dessalene et al. — [What to Attend, What to Keep: Skill-Conditioned Visuotactile Representation with Progress-Guided Event Memory](http://arxiv.org/abs/2609.38494v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation integrates vision, touch, and language, whose importance shifts across stages: vision guides reaching, while touch, through its evolution over time, decides grasping, alignment, and contact. Yet existing multi-modal manipulation policies typically use fixed temporal contexts and fusion strategies, despite shifts in what each modality contributes across different skills. We study how vision and touch should be combined at the level of primitive skills, asking what each skill ...
  </details>

- **2026-09-29** — Xueting Fang, Zehui Li, Yang Yang et al. — [KlinikeBench: Evaluating Language Models Beyond Diagnostic Accuracy](http://arxiv.org/abs/2609.38480v1)
  <details><summary>📄 Abstract</summary>
  Most clinical benchmarks evaluate language models (LMs) on diagnosis using complete case descriptions. In clinical practice, however, patients present information in different ways, and clinicians must obtain relevant history and determine which examinations are needed before reaching a diagnosis. Diagnostic accuracy alone therefore cannot establish whether an agent gathered essential information or conducted an appropriate clinical assessment. Furthermore, existing benchmarks lack professional ...
  </details>

- **2026-09-29** — Prakriti Baral, Zhuoyun Qian, Hailu Xu et al. — [Behavior-Centric Malware Classification with Fine-Grained Malicious Logic Localization](http://arxiv.org/abs/2609.38390v1)
  <details><summary>📄 Abstract</summary>
  Effective malware analysis requires understanding not only whether a program is malicious, but also which behaviors it exhibits and where those behaviors originate in the code. Existing machine-learning-based malware detectors largely operate as black boxes, providing limited insight into the malicious logic responsible for their decisions. This paper addresses malicious behavior localization and classification at the basic-block level. We propose a behavior-centric analysis framework that decom...
  </details>

- **2026-09-29** — Bakhtawar Ahtisham, Kirk Vanacore, Alessandra Napoli et al. — [Examining Variation in How Guided AI Tutors Resolve Student Impasses](http://arxiv.org/abs/2609.38346v1)
  <details><summary>📄 Abstract</summary>
  When a student is stuck, a tutor faces the assistance dilemma: help given too early can hinder productive struggle, while help withheld too long leaves the student in a frustrating, persistent impasse (i.e., wheel spinning). Generative AI tutors increasingly use guardrails restricting answer-giving, yet little is known about how such tutors behave once an impasse persists. We analyze 20,462 student turns from 1,260 authentic sessions with a guided LLM chemistry tutor, identifying 6,630 impasse t...
  </details>

- **2026-09-29** — Mohamed Abouzahra — [NAQD Env: A benchmark for selective withdrawal in language agents](http://arxiv.org/abs/2609.38460v1)
  <details><summary>📄 Abstract</summary>
  Language agents must revise planned actions when evidence changes, permission is revoked, or a stop instruction arrives. A useful response is selective: suspend affected actions, preserve unaffected work, and resume only after sufficient repair. We introduce NAQD-Env, a synthetic environment that evaluates these decisions against a deterministic reference policy over explicit evidence, authorization, and constraint dependencies. Eleven dependency families support evaluation on development struct...
  </details>

- **2026-09-29** — Chenqi Kong, Song Xia, Anwei Luo et al. — [Forensic-Aware Continual Adaptation for Image Forgery Localization](http://arxiv.org/abs/2609.38251v1)
  <details><summary>📄 Abstract</summary>
  The rapid evolution of image manipulation techniques has raised growing public security concerns. Existing Image Forgery Localization (IFL) methods can accurately localize manipulated regions but are often unable to adapt to newly emerging forgeries. In real-world forensic scenarios, data typically arrive sequentially, yet continual model adaptation remains largely unexplored in IFL. To bridge this gap, we introduce the first continual learning framework for IFL and establish a comprehensive ben...
  </details>

- **2026-09-29** — Fernando Dupin da Cunha Mello, Prashant Kumar, Erick G. Sperandio Nascimento — [An Input-Frugal Deep Learning Framework for Weather-Driven National Crop-Yield Forecasting: A Case Study of Brazilian Soybean](http://arxiv.org/abs/2609.38447v1)
  <details><summary>📄 Abstract</summary>
  Reliable, timely crop-yield forecasts are essential for market stability and risk management, yet many approaches rely on costly or hard-to-scale inputs. We present a frugal, transferable, and architecture-agnostic deep learning framework that uses routine weather as the only time-varying input plus two lightweight static context inputs (crop year and an agro-environmental label) to capture long-run change and regional heterogeneity, while supporting multiple sequence encoders under identical da...
  </details>

- **2026-09-29** — Ratish Puduppully, Pranabendu Misra, Paarth Iyer et al. — [Correct Answers, Invalid Traces: What Verifiable Grade-School Math Reveals About Chain-of-Thought Traces](http://arxiv.org/abs/2609.38107v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought traces are widely read as records of how models reach their answers, informing debugging, agent auditing, and claims about reasoning. Testing this interpretation is difficult because natural-language thinking traces are rarely mechanically verifiable. We revisit it in iGSM, a synthetic grade-school mathematics benchmark designed to study thinking traces and used to support claims of learned reasoning and planning. Crucially, iGSM exposes the exact quantities and dependencies tha...
  </details>

- **2026-09-29** — Samrendra Roy, Tapas Tripura, Yoon Pyo Lee et al. — [A foundation model for energy and radiation systems built on heterogeneous scientific interfaces](http://arxiv.org/abs/2609.38067v1)
  <details><summary>📄 Abstract</summary>
  Scientific foundation models are commonly evaluated after heterogeneous physical problems have already been translated into a compatible gridded, tokenized or symbolic representation. This leaves the scientific interface outside both the pretrained model and the audit of what is actually reused. We study the complementary setting in which boundary histories, sparse monitor records and loading histories retain their native inference classes and their outputs remain on Cartesian, latitude-longitud...
  </details>

- **2026-09-29** — Sen Zhao, Ruiqi Kong, Zuyu Zhang et al. — [Topological Coherence for Self-evolving Multi-agent Systems](http://arxiv.org/abs/2609.37953v1)
  <details><summary>📄 Abstract</summary>
  Complex tasks inherently couple workflow structure, agent responsibility, collaboration, and memory access: task regions delimit responsibility and tool scope, cross-region dependencies give rise to handoffs, and ownership boundaries delimit private and selectively shared memory. Existing methods can jointly optimize agent and communication structures, yet such optimization does not by itself require responsibility, handoff, and memory boundaries to remain consistent with task dependencies. We t...
  </details>

- **2026-09-29** — Xiangyu Gao, Tong Li, Ziqiang Wang et al. — [NetLexicon: Learning Discrete Behavioral Representations for Encrypted Web Traffic Analysis](http://arxiv.org/abs/2609.37672v1)
  <details><summary>📄 Abstract</summary>
  Encrypted Web traffic analysis requires effective representations of observable communication behavior. Existing pretraining methods often adapt NLP/CV objectives and sequence architectures, motivating learning objectives that capture traffic-specific interaction patterns. We present NetLexicon, a discrete pretraining framework that learns reusable behavioral states from unlabeled traffic. It converts contextual traffic windows into discrete states through vector quantization, constructing a com...
  </details>

- **2026-09-29** — Łukasz Sobczak, Nur Keleşoğlu, Sławomir Piotr Nowak — [Risk-Aware Semantic Grounding for Trustworthy LLM-Based Robot Planning](http://arxiv.org/abs/2609.37554v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as high-level planners in robot navigation, but their outputs may become unreliable when instructions are ambiguous, unsupported by the environment, or semantically inconsistent. This paper presents a Risk-Aware Semantic Grounding framework for trustworthy LLM-based robot planning. Unlike existing LLM-based planners that primarily optimize plan generation, we formulate semantic grounding reliability as a multi-dimensional risk estimation problem...
  </details>

- **2026-09-29** — Jérôme Michaud, Fredrik Jansson — [Cultural, Structural, and Mediated Routes to Polarization in a Nonlinear Mean-Field Model](http://arxiv.org/abs/2609.37521v1)
  <details><summary>📄 Abstract</summary>
  Collective polarization can arise through mechanisms acting at different stages of social communication, but similar polarized outcomes need not imply dynamically equivalent processes. We introduce a nonlinear two-group mean-field model that distinguishes three routes to polarization: individual content filtering, assortativity, and receiver-side message tailoring. Sender-side reformulation is included as a complementary mediation process that transforms source signals before they are mixed. The...
  </details>

- **2026-09-29** — Paul Gattinger, Michela Conti, Franziska Dietz et al. — [Scanless quantum Fourier-transform mid-infrared spectroscopy for solids and surface analysis](http://arxiv.org/abs/2609.37281v1)
  <details><summary>📄 Abstract</summary>
  Quantum infrared (IR) spectroscopy is a novel technique based on nonlinear interferometry and quantum sensing with undetected photons. In this approach, spectrally far-separated correlated photon pairs are used for detection and probing, respectively. Hence, the probing wavelength domain (mid-IR) is substantially different from the detection spectral range (near-IR), which enables shot-noise-limited and cost-effective sensing schemes attractive for applied metrology. In this paper, we implement ...
  </details>

- **2026-09-29** — Zewen Sun, Tongyang Zhao, Liyao Xiang et al. — [Beyond Semantic Narrowing: Robust and Efficient LLM Watermarking with Hamming Neighborhoods](http://arxiv.org/abs/2609.37218v1)
  <details><summary>📄 Abstract</summary>
  Semantic watermarking improves robustness against watermark removal attacks by embedding detectable signals into sentence-level representations. However, existing watermarking methods typically impose watermark-specific semantic preferences on generated sentences without explicitly accounting for the highly non-uniform and context-dependent semantic preference of LLM generation. When these two preferences are poorly aligned, many natural continuations become incompatible with the watermark, caus...
  </details>

- **2026-09-29** — Giulio Segalini, Zhi Wen Soi, Jérémie Decouchant et al. — [Absorbed in Inertia: Activation Analysis for Computer-Use Agents](http://arxiv.org/abs/2609.37176v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents have become increasingly capable of executing tasks on live desktops through natural-language instructions, based on trajectories of screenshots, actions, and reasoning. We discover that they can stealthily exhibit inertia, in which they repeat fruitless actions despite recognizing that these actions are ineffective. We hypothesize that inertia is reflected in the agent's internal state, i.e., the activation values of the agent's underlying model, and propose a protocol to me...
  </details>

- **2026-09-29** — Zirui Li, Torsten Brix, Stephan Husung — [Cross-Organizational SysML Model Integration: A Survey of Challenges and AI-Supported Tasks](http://arxiv.org/abs/2609.37000v1)
  <details><summary>📄 Abstract</summary>
  Cross-organizational collaboration is widely regarded as a key promise of SysML-based Model-Based Systems Engineering (MBSE), yet practitioners still face persistent challenges when exchanging and integrating system models. In parallel, Large Language Models (LLMs) raise expectations for AI-assisted model understanding and integration, while reliability and required human oversight continue to pose challenges. This paper reports the results of an online questionnaire survey with 29 MBSE stakehol...
  </details>

- **2026-09-29** — Jiacheng Guo, Suozhi Huang, Shuzhen Li et al. — [Can Language Models Learn to Forecast Stock Prices](http://arxiv.org/abs/2609.36914v1)
  <details><summary>📄 Abstract</summary>
  Post-training has been shown to significantly improve language models' performance on tasks with verifiable outcomes, including mathematical reasoning, software engineering, and computer use. However, whether the same approach can improve forecasting in financial markets is much less clear. Compared with tasks with verifiable outcomes, not only are realized returns noisy, but even what constitutes a relevant information set for making effective predictions is not obvious a priori: the model must...
  </details>

- **2026-09-29** — Bo Mao, Hang He, Linting Wang et al. — [WEFT: Scaling Tool-Use Post-Training for General-Purpose Agents](http://arxiv.org/abs/2609.36887v1)
  <details><summary>📄 Abstract</summary>
  Recent efforts to scale tool-use post-training have largely centered on the synthesis of executable environments, which constitute only one component of a broader agentic interaction system comprising the environment, task, agent harness, and evaluator. Scaling environments in isolation, however, does not guarantee commensurate gains in model performance, because reliable learning signals depend on coherent interactions among all components of the agentic interaction system. To address this prob...
  </details>

- **2026-09-29** — Rui Wang, Ruijie Wang, Bo Chen et al. — [Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation](http://arxiv.org/abs/2609.36695v1)
  <details><summary>📄 Abstract</summary>
  Self-distillation turns knowledge distillation into a closed learning loop and offers a path toward recursive self-improvement. Without an external teacher, however, the model must determine both what information can improve its supervision and which induced changes should be learned. Existing methods typically improve teacher-generated data or select training examples in isolation, leaving the information transferred between these stages unmeasured. We introduce InFlow, a retrieval-guided on-po...
  </details>

- **2026-09-29** — Ruochen Zhang, Yao Huang, Yitong Sun et al. — [ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models](http://arxiv.org/abs/2609.36562v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, their reliability is threatened by multimodal implicit risks. Unlike explicit threats, these hazards emerge when individually benign text and neutral visual entities logically converge to induce unsafe outputs. Current detection methods fail to address this because they overlook the underlying risk activation mechanisms that govern cross-modal risk activation, leading to single-modality shortcut ...
  </details>

- **2026-09-29** — Lijie Zheng, Ji He, Ying Wang et al. — [Know the Normal, Track the Attack: Context-Grounded and Stateful LLM Investigation over System Provenance](http://arxiv.org/abs/2609.36494v1)
  <details><summary>📄 Abstract</summary>
  Provenance-based intrusion detection systems (PIDSs) identify suspicious activity in audit streams, but their outputs remain difficult to turn into coherent attack narratives. Direct LLM analyses of local anomalous subgraphs lack deployment-specific normal-behavior knowledge and validated attack state across evidence fragments. This can cause unsupported attack interpretations of routine activities and incorrect attribution of temporally dispersed evidence to attack stages. We present ANCHOR, an...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 65 papers

- **2026-09-30** — Anson Y. Lam, Shuqing Li, Michael R. Lyu — [MatLoom: Layered Text-to-Material Generation in a Compact Program Space](http://arxiv.org/abs/2609.40322v1)
  <details><summary>📄 Abstract</summary>
  Material generation should produce not only an appearance, but also the rules that construct it. We introduce MatLoom, a compact, layer-oriented language for text-to-material generation with pretrained language models. Each program composes alpha-masked layers whose shared spatial expressions define coverage and physically based rendering (PBR) channels, making dependencies between patterns, color, and relief explicit. A standalone interpreter evaluates the program into material maps, while the ...
  </details>

- **2026-09-30** — Zikai Liao, Yumin Suh, Yi Ouyang et al. — [GLARE: Generating Listening Heads with Appropriate Reactions](http://arxiv.org/abs/2609.40317v1)
  <details><summary>📄 Abstract</summary>
  While talking head generation has advanced rapidly, generating natural listener behavior in dyadic conversations, which know when to react, how to react, and with what type of response, remains underexplored. Existing dyadic datasets lack fine-grained listener reaction annotations, and prevailing evaluation metrics inherited from talking-head and video generation measure visual realism rather than whether a listener reacted appropriately. We address these gaps along three aspects. First, we cura...
  </details>

- **2026-09-30** — Maksim Bobrin, Maksim Zhdanov, Dmitry Dylov — [Fenchel Tilting: Weighted Correction for Efficient Finetuning of Generative Models](http://arxiv.org/abs/2609.40030v1)
  <details><summary>📄 Abstract</summary>
  Adapting a pretrained generative model to an arbitrary preference expressed as a utility function underlies reward alignment, guided design, and constraint satisfaction, enabling diverse applications. Existing fine-tuning methods trade off generality against computational cost: they either restrict the family class of supported preferences to keep optimization simple or preserve generality at the expense of efficiency. We introduce Fenchel Tilt Flow Control (FTFC), which decouples utility optimi...
  </details>

- **2026-09-30** — Yanshu Li, Jiaqian Li, Canran Xiao et al. — [MCD: Causal Distillation of Multimodal In-Context Learning in Large Vision-Language Models](http://arxiv.org/abs/2609.39920v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) exhibit strong multimodal in-context learning (ICL) capabilities, yet this ability degrades substantially as model size decreases. Knowledge distillation offers a natural way to bridge this gap, but existing methods primarily align output distributions or hidden representations directly. Such alignment teaches the student what the teacher predicts without revealing which evidence in the complex context causally supports that prediction. Consequently, a studen...
  </details>

- **2026-09-30** — Xingjie Zhuang, Jialong Tang, Chulun Zhou et al. — [Cognitive Enhancement: Rethinking the Necessity of Role-Playing for Large Language Models](http://arxiv.org/abs/2609.39853v1)
  <details><summary>📄 Abstract</summary>
  Role-playing prompting has become a popular yet simple technique for improving LLM reasoning and output quality. However, whether it consistently boosts performance across diverse domains remains unclear, as systematic validation is lacking. To fill this gap, we run multi-model, cross-domain, and multilingual experiments on MMLU and MMLU-Redux. We find that gains from role-play prompting depend heavily on model capacity, knowledge domain, and prompt language. Drawing on metacognition theory, we ...
  </details>

- **2026-09-30** — Hongwei Zhao, Rui Liu, Yansong Liu — [Dynamic LoRA-Experts and Prototype-Ensemble Matching for Class-Incremental Learning](http://arxiv.org/abs/2609.39839v1)
  <details><summary>📄 Abstract</summary>
  Class-Incremental Learning (CIL) aims to continuously learn new classes without forgetting previously acquired knowledge. Parameter-efficient fine-tuning with pre-trained models reduces parameter overhead but can suffer from cumulative interference and suboptimal alignment between inference samples and specialized modules. We propose Dynamic LoRA-Experts and Prototype-Ensemble Matching (DLEPEM), a two-stage rehearsal-free framework. DLEPEM allocates a task-specific LoRA-Expert for each increment...
  </details>

- **2026-09-30** — Simone Ricci, Niccolò Biondi, Federico Pernici — [Spherical Interpolation for Backward-Compatible Multimodal Representations](http://arxiv.org/abs/2609.39836v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language models map visual and textual representations into a shared normalized embedding space, making cosine similarity the natural metric for cross-modal retrieval. A practical challenge arises during model upgrades: independently trained models generally produce incompatible representation spaces, so replacing a deployed model typically requires recomputing embeddings for the entire gallery, which is prohibitively expensive at scale. Orthogonal post-hoc alignment can parti...
  </details>

- **2026-09-30** — Jiangxia Cao, Hao Peng, Wenlong Xu et al. — [KUAISHOU Explorer LLM-Rec Challenge 2026: Reasoning Generative Recommendation](http://arxiv.org/abs/2609.39828v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation, has been attracted a surge of attentions in industrial and academic research community, towards to build more smart system to build next-generation recommender. Under the significant developing wave of large language model, our team have been developed Semantic ID based OneRec/OneRec-V2. These models have been widely deployed in production and demonstrate the scaling potential of the autoregressive next-item prediction paradigm for industrial recommender systems. Build...
  </details>

- **2026-09-30** — Jiale Dai, Hongcan Deng, Liuxian Ma et al. — [Values as Style: Disentangling Values from Semantics with One-Way Mixing for Low-Damage LLM Steering](http://arxiv.org/abs/2609.39701v1)
  <details><summary>📄 Abstract</summary>
  Value steering should change an LLM's normative priorities while preserving the scenario, facts, and task constraints underlying its answer. Conventional activation edits often change both. We introduce an editable semantic-value interface on frozen residual states, with a one-way semantic-to-value pathway that grounds value recognition in context. Stop-gradient blocks feedback through this pathway; swap consistency, topic de-confounding, and decorrelation encourage selective codes. At inference...
  </details>

- **2026-09-30** — Jingwei Jia, Keyu Zhou, Jiewei Wang et al. — [RoboAssist: Interactive Human-Humanoid Planning for Long-Horizon Surgical Assistance](http://arxiv.org/abs/2609.39384v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon surgical assistance requires humanoid robots to coordinate with evolving human activities while maintaining safety across planning and execution. We present RoboAssist, an agent-based framework for interactive human-humanoid planning that integrates workflow reasoning, task coordination, and cross-layer safety. At its core is an asymmetric dual-track representation that separates partially observed human process states from executable robot task sequences. By updating human-process ...
  </details>

- **2026-09-30** — Jiahe Fan, Si Chen, Yinghao Hou et al. — [Exploring Heterogeneous Model Merging Approach for Complex Knowledge Transfer](http://arxiv.org/abs/2609.39369v1)
  <details><summary>📄 Abstract</summary>
  Specialized models encode task-oriented behavior, but transferring that behavior to a general language model usually requires training, distillation, or representation alignment. We study whether such ability can instead be transferred directly at the parameter level. We apply two existing training-free heterogeneous merging methods, previously shown to transfer knowledge between general language models, to specialist-to-general transfer, projecting a specialist donor into the recipient's shape ...
  </details>

- **2026-09-30** — Jeesu Jung, Hwan Chang, Juseon Do et al. — [Ready2Blend: From Natural-Language Instructions to Composable Alignment Prompts](http://arxiv.org/abs/2609.39365v1)
  <details><summary>📄 Abstract</summary>
  Continual alignment requires LLMs to adapt to new requirements without forgetting previously acquired behaviors. Natural-language instructions are flexible and composable but offer only indirect control, whereas post-training provides stronger adaptation at the cost of repeated parameter updates. We introduce Ready2Blend, which combines the flexibility of natural language with learned alignment. AlignFormer maps each requirement to a fixed-length alignment prompt stored in a modular prompt bank,...
  </details>

- **2026-09-30** — Tianyu Zhang, Zhaoyang Jia, Houqiang Li et al. — [Rethinking Generative Image Compression at Extremely Low Bitrates](http://arxiv.org/abs/2609.39315v1)
  <details><summary>📄 Abstract</summary>
  Generative image compression produces visually plausible reconstructions at low bitrates, yet their behavior as the rate approaches zero remains largely unexplored. When pushed below normal operating rates, representative codecs undergo semantic collapse: rather than gracefully losing source-specific detail, they produce malformed or unrecognizable content. Our analysis identifies two factors. As the bitrate decreases, reconstruction losses increasingly conflict with semantic objectives on gradi...
  </details>

- **2026-09-30** — Beiming Liu, Minjie Chen — [Right Answer, Wrong Mechanism: Detecting Pernicious Divergence in Causal Interventions](http://arxiv.org/abs/2609.39243v1)
  <details><summary>📄 Abstract</summary>
  Causal interventions such as activation patching and distributed alignment search (DAS) are the main tool for making mechanistic claims about neural networks. Recent work showed that these interventions routinely push representations off the model's natural distribution, and that such divergence is sometimes harmless and sometimes pernicious: it can recruit pathways the model never uses on natural inputs, so that an intervention produces the expected answer through the wrong mechanism. No method...
  </details>

- **2026-09-30** — Yang Li, Gongle Xue, Yuheng Yuan et al. — [Diagnosing On-Policy Self-Distillation for Reasoning Language Models](http://arxiv.org/abs/2609.39118v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has attracted growing interest as a promising approach to improve the reasoning ability of language models. Without external rewards nor a separate stronger teacher, the self-teacher with privileged information could provide dense signals on student's trajectories. However, its behavior in language reasoning remains unclear, with reported outcomes ranging from modest gains to behavioral collapse. In this work, we diagnose OPSD for mathematical reasoning across ...
  </details>

- **2026-09-30** — Shokichi Takakura, Akifumi Wachi, Rei Higuchi et al. — [Steepest Guidance: A Practical and Principled Approach to Inference-Time Alignment of Flow and Diffusion-based Models](http://arxiv.org/abs/2609.39091v1)
  <details><summary>📄 Abstract</summary>
  Inference-time alignment of flow and diffusion-based models is critical for achieving flexible generative modeling. Theoretically, Doob's $h$-transform provides an elegant solution to this problem, and most existing methods are based on this principle. However, in practice, estimating the optimal guidance derived from Doob's $h$-transform at inference time is challenging. To deal with this issue, we regard inference-time alignment as a sequential optimization problem in the space of probability ...
  </details>

- **2026-09-30** — Christina Hahn, Shangbin Feng, Dean Light et al. — [Multi-LLM Collaborative Alignment via Stackelberg Games](http://arxiv.org/abs/2609.39076v1)
  <details><summary>📄 Abstract</summary>
  A pool of language models can collaborate and improve collectively by learning from one another's responses. These interactions depend on the instructions used during training. Existing methods typically sample instructions uniformly, even though their usefulness may change as the models improve: an instruction on which models' responses once differed in quality may later be answered equally well, while a previously difficult instruction may begin to provide a useful learning signal. We propose ...
  </details>

- **2026-09-30** — Chenguang Wang, Ming Li, Chengrui Fan et al. — [A Missing Piece for Trustworthy AI Reviewers: From Benchmarking Rhetorical Robustness to SciCore Review](http://arxiv.org/abs/2609.39027v1)
  <details><summary>📄 Abstract</summary>
  AI reviewers can assign different judgments to manuscripts that report the same science in different wording, potentially rewarding rhetorical optimization over scientific improvement. We formulate Rhetorical Robustness as the joint requirement of stability across content-preserving rewrites and discrimination across papers. We introduce RobustReview, a controlled full-manuscript benchmark with 1,260 manuscript versions, and evaluate 30 reviewer configurations. The benchmark reveals false robust...
  </details>

- **2026-09-30** — Bolin Zou, Wenlong Dong, Mu Ai et al. — [Function beyond Form: Functional Correspondence for Cross-Embodiment Dexterous Grasp Generation](http://arxiv.org/abs/2609.39006v1)
  <details><summary>📄 Abstract</summary>
  Cross-embodiment dexterous grasp generation remains challenging because robotic hands differ substantially in geometry, topology, and kinematics. Existing approaches often lack explicit correspondences between structurally different hand regions that play similar functional roles in a grasp, a concept we refer to as functional correspondence. Consequently, their models tend to learn hand-specific interaction patterns rather than transferable grasp knowledge, limiting generalization to unseen han...
  </details>

- **2026-09-30** — Yihuai Hong, Shauli Ravfogel, Chen Zhao et al. — [Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment](http://arxiv.org/abs/2609.38972v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) traces often serve as a proxy for how Large Language Models (LLMs) arrive at their answers. However, growing evidence shows that models' CoT often fails to reflect their internal computations and can be changed without affecting their final answers. In this work, we measure and improve the alignment between the reasoning described in an LLM's CoT and what it computes internally. We propose CoT-Interpretability Alignment (CIA), a metric that measures the agreement between a...
  </details>

- **2026-09-30** — Suyuan Zhao, Minghao Liu, Yizhen Luo et al. — [CellMSA: Context Modeling for Single-Cell Representation Learning](http://arxiv.org/abs/2609.38908v1)
  <details><summary>📄 Abstract</summary>
  Single-cell transcriptomics enables profiling of cellular states at unprecedented resolution, but its high dimensionality, sparsity, and technical batch effects pose significant challenges for representation learning. Existing single-cell foundation models typically encode each cell independently or only model cells from the same batch for denoising, thereby underutilizing the rich relational information across batches and cell types to model gene expression patterns. We argue that single-cell m...
  </details>

- **2026-09-30** — Seokmin Ko, Taewon Goo, Kihyuk Hong — [DAMPER: Return-Prioritized Gradient Control for Smooth Policies](http://arxiv.org/abs/2609.38903v1)
  <details><summary>📄 Abstract</summary>
  Actor-critic methods achieve strong performance in continuous control, but their policies can produce highly oscillatory actions. A common remedy is to add auxiliary smoothness losses. However, their contribution can be negligible when their gradients are small relative to the native actor gradient. Moreover, existing methods often combine multiple auxiliary losses, complicating loss balancing without necessarily improving the return-smoothness trade-off. We introduce DAMPER (Direction-Aware Mag...
  </details>

- **2026-09-30** — Chenglin Chen, Lujia Wang, Xinhu Zheng et al. — [Efficient Multi-Modal Planning with Reward-Guided Preference Optimization for Autonomous Driving](http://arxiv.org/abs/2609.38862v1)
  <details><summary>📄 Abstract</summary>
  Safe and efficient trajectory planning is essential in autonomous driving. However, existing end-to-end approaches often fall short in both computational efficiency and safety guarantees. Methods based on imitation learning suffer from causal confusion, while rule-based scoring approaches often incur heavy computational overhead and suffer from objective misalignment. Additionally, preference-based methods rely on strict pairwise annotations, limiting data utilization. To overcome these limitati...
  </details>

- **2026-09-30** — Zhongman Du, Huiming Zhang, Haodong Zhu et al. — [Optimal Design for Active Preference Learning with Biased LLM Judges](http://arxiv.org/abs/2609.38860v1)
  <details><summary>📄 Abstract</summary>
  Learning from human preferences is central to large language model (LLM) alignment, but human preference annotation is costly. Active preference learning reduces this cost by selecting informative comparisons, and LLM judges can provide additional scalable feedback. However, the preferences of the judges may deviate from those of the target human population. Even after calibration on trusted reference data, active acquisition can shift the comparison distribution and expose residual judge bias. ...
  </details>

- **2026-09-30** — Kaijie Qi, Yuehan Wang, Kaiming Xu et al. — [PhaseSync-Exo: Human Clock Anchored Reference Adaptation for Dynamic Gait Tracking](http://arxiv.org/abs/2609.38824v1)
  <details><summary>📄 Abstract</summary>
  Human-aware exoskeleton walking requires reconstructing gait, tracking diverse motions under dynamic constraints, and preserving human timing. We present PhaseSync-Exo, which combines two-IMU CNN-Transformer reconstruction, factorized amplitude-cadence retargeting with curriculum-trained recurrent control, and a human-clock-anchored adapter (HCA). HCA combines human-clock attraction with robot-relative feedback to adjust reference rate while preserving forward progression and continuity. The rec...
  </details>

- **2026-09-30** — Ali Almutairi, Gelareh Mohammadi, Imran Razzak et al. — [BARRAC: Adaptation of an English Aspect-based Sentiment Analysis Approach for Classification Tasks in Arabic Dialects](http://arxiv.org/abs/2609.38820v1)
  <details><summary>📄 Abstract</summary>
  With the rapid growth of Arabic NLP, several models, datasets and benchmarks have been reported. This paper asks whether approaches developed for majority languages like English can be adapted to Arabic tasks. We adapt an English aspect-based sentiment analysis framework to Arabic classification tasks and present the adaptation as BARRAC: Brainstorming Alignment and Replaced Representation learning for ArabiC tasks. BARRAC replaces consumer-review attribute pools with Arabic linguistic devices a...
  </details>

- **2026-09-30** — Weiqi Jiang, Yuchen Ying, Rui Wang et al. — [GraphCert: Bootstrap Agentic Graph Reasoning with Certified Evidence Rubrics](http://arxiv.org/abs/2609.38798v1)
  <details><summary>📄 Abstract</summary>
  Graph agents extend large language models (LLMs) with the ability to actively explore and reason over knowledge graphs through multi-step interactions with graph tools. However, training capable graph agents typically requires large collections of question-answer pairs and reasoning trajectories, whose manual construction is costly and difficult to scale. Moreover, employing proprietary LLMs to generate such supervision further risks exposing sensitive graph data to external services. Therefore,...
  </details>

- **2026-09-30** — Rafi Ibn Sultan, Md. Sajid Alam Chowdhury, Saleh Zare Zade et al. — [Soft Spatial Reasoning](http://arxiv.org/abs/2609.38717v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) commonly perform spatial reasoning through chain-of-thought (CoT), encoding intermediate reasoning as autoregressive sequences of discrete language tokens. Such hard thinking requires committing to a single token at each step, even when the correct spatial interpretation remains uncertain. This early commitment constitutes premature discretization: an incorrect token selection can propagate errors through subsequent reasoning. We propose Soft Spatial Reasonin...
  </details>

- **2026-09-30** — Jeffrey Willette, Krishna C. Puvvada, Boris Ginsburg — [Staying on Task: Testing the Foundations of Long-Horizon Agent Reliability](http://arxiv.org/abs/2609.38712v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agentic workflows require models to sustain repeated state-dependent actions all while the context grows, sub-task complexity changes, and new data arrives. Each situation represents an independent axis along which an agent may fail. An agent reconciling a long ledger, for example, must repeatedly read its state, update the correct record, and preserve alignment across thousands of outputs. A model may accept the entire ledger yet lose its place or stop applying the operation consis...
  </details>

- **2026-09-30** — Shubhang Bhatnagar, Ishan Bhatnagar, Viraj Shah et al. — [ReGain: Restoring Subject Fidelity in Personalization on Synthetic Images](http://arxiv.org/abs/2609.38680v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models are personalized to a subject by DreamBooth fine-tuning on a handful of its images. Increasingly, these images come from a diffusion model rather than a camera. We show that fine-tuning on such synthetic images degrades subject fidelity, producing oversaturated color and excess high-frequency detail. To isolate the cause, we fine-tune two models from the same base model with the same DreamBooth recipe, one on real photos of a subject and one on synthetic images of ...
  </details>

- **2026-09-29** — Fereshteh Aghaee Meibodi, Amir Mehdi Soufi Enayati, Shadi Alijani et al. — [Template-Search Domain Adaptation via Multi-Stage Feature Alignment for Cross-Modal Object Tracking](http://arxiv.org/abs/2609.38637v1)
  <details><summary>📄 Abstract</summary>
  Visual object tracking typically assumes that the initial template and subsequent search frames share the same sensing modality. In practice, sensor availability or operation may change over time, creating a substantial representation gap between template and search frames. Unlike conventional multi-modal tracking where paired modalities are simultaneously available, cross-modal tracking requires localization when template and search frames originate from different active modalities. Accordingly...
  </details>

- **2026-09-29** — Zheyuan Zhang, Mengyuan Chao, Ke Xiao et al. — [Beyond Oracle Communication: Benchmarking Interactive Intent Alignment Under Miscommunication and Evolving User Intent](http://arxiv.org/abs/2609.38604v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM agents increasingly tackle complex tasks through interactive, long-horizon exchanges with users, while existing benchmarks generally assume that users always accurately and sufficiently communicate a fixed intent. However, this oracle communication assumption rarely holds in practice: users may miscommunicate, change their goals, and run out of patience. We define this task setting as Interactive Intent Alignment, where agents must recover and continuously track the user's current int...
  </details>

- **2026-09-29** — Kia-Jüng Yang, Fabian H. Sinz, Paweł A. Pierzchlewicz — [Retargeting Motions to Diverse Skeletons via Learnable Flattening](http://arxiv.org/abs/2609.38578v1)
  <details><summary>📄 Abstract</summary>
  Cross-structural motion retargeting aims to transfer motion between different skeletal topologies. Despite recent progress, existing state-of-the-art models struggle with reliability in zero-shot settings, i.e. skeletons with different topologies which were unseen during training, and recent Transformer-based attempts have failed to outperform specialized geometric methods. We bridge this gap with a Transformer Autoencoder that learns a topology- and translation-invariant latent space. Our core ...
  </details>

- **2026-09-29** — Meng-Chen Wu, Qipin Chen, Ansh Jain et al. — [Demographic Pluralism: Inference-Time Modeling of Pluralistic Human Preference Distributions](http://arxiv.org/abs/2609.38555v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in culturally sensitive settings, where alignment requires representing diverse preferences within populations. Yet existing methods model populations at coarse demographic or community levels and overlook within-group variation. We introduce Demographic Pluralism, an inference-time framework that estimates population-level opinion distributions without opinion-distribution training data or task-specific fine-tuning by generating multiple perspe...
  </details>

- **2026-09-29** — Hyeong Kyu Choi, Bhavana Dalvi Mishra, Jiefeng Chen et al. — [AIM: Agentic Idea Management for Automated Research](http://arxiv.org/abs/2609.38445v1)
  <details><summary>📄 Abstract</summary>
  Frontier LLMs are increasingly used to automate scientific research through iterative search. We distinguish idea-driven search from solution-driven search and identify three core challenges: organizing evolving research ideas, selecting promising directions, and maintaining alignment between ideas and their implementations. To address these challenges, we introduce the Agentic Idea Manager (AIM), a fully autonomous framework for managing and exploring research directions in idea-driven automate...
  </details>

- **2026-09-29** — Maham Tanveer, Jiyeon Han, Nanxuan Zhao et al. — [Strike a Chord! Modal Kinetic Typography](http://arxiv.org/abs/2609.38325v1)
  <details><summary>📄 Abstract</summary>
  We introduce modal kinetic typography, which animates a vector glyph to express a semantic concept while keeping it legible. Our key idea is to build motion from the glyph's natural vibration modes. Specifically, a finite-element eigenproblem assembled from the vector outline yields the glyph's softest modes, for the whole letter and for each of its parts, allowing it to bend. The problem's zero-energy solutions, i.e., rigid translations and rotations, are applied in closed form to each part, al...
  </details>

- **2026-09-29** — Yiming Jiang, Jin Chen, Chongyang Xu et al. — [EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation](http://arxiv.org/abs/2609.38046v2)
  <details><summary>📄 Abstract</summary>
  Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign, a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose, continuous whole-body controller, without collecting physical-robot demonstrations. Using the target-robot model and simula...
  </details>

- **2026-09-29** — Ann Huang, Mitchell Ostrow, Zhouyang Lu et al. — [Traversing the solution space of neural networks with Hessian Null Space Continuation](http://arxiv.org/abs/2609.38081v1)
  <details><summary>📄 Abstract</summary>
  On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...
  </details>

- **2026-09-29** — Yiming Jiang, Chen Jin, Chongyang Xu et al. — [EgoAlign: Bridging the Human-Humanoid Gap for Long-Range Loco-Manipulation](http://arxiv.org/abs/2609.38046v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human demonstrations offer an accessible source of task experience, but differences in body scale and controller response, together with missing robot states, limit their value as humanoid training supervision. We present EgoAlign, a data-construction framework that converts these demonstrations into action and state supervision compatible with a general-purpose, continuous whole-body controller, without collecting physical-robot demonstrations. Using the target-robot model and simula...
  </details>

- **2026-09-29** — Christopher Pinier, Gustaw Opiełka, Hannes Rosenbusch et al. — [Which Attention Heads are like the Human Head? Not the Ones that Compute](http://arxiv.org/abs/2609.37991v1)
  <details><summary>📄 Abstract</summary>
  Brain-AI alignment is often interpreted as a sign that model and brain perform similar computations. Whether the aligned units are causally involved in model computation is rarely checked. On an abstract pattern-completion task (AAABAAA $\rightarrow$ B), we compare LLM attention-head representations with human EEG and test how ablating those heads affects task performance. Alignment and causation dissociate: brain-aligned heads contribute to performance, but their removal is substantially less d...
  </details>

- **2026-09-29** — Manuel Madeira, Amitis Shidani, Alice Bizeul et al. — [On Trajectory-Aware Training for Masked Diffusion Language Models](http://arxiv.org/abs/2609.37974v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion models (MDMs) generate text by unmasking several tokens per step, but they are trained and sampled under different conditions. The model is trained on randomly masked sequences, whereas inference follows a trajectory shaped by the model's own predictions. Additionally, each step has no access to what the previous one computed. Recent methods narrow these limitations from separate angles, leaving open how these choices interact. We introduce PUMBA, a unified framework for traject...
  </details>

- **2026-09-29** — Ziyi Luo, Zhe Sun, Yehao Lu et al. — [ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving](http://arxiv.org/abs/2609.37871v1)
  <details><summary>📄 Abstract</summary>
  Average performance on routine driving benchmarks does not establish planner reliability under rare, safety-critical hazards. We proposed ExceptionDrive, a counterfactual planning benchmark that uses VLM-assisted screening, localized multi-view editing, and quality auditing to insert hazards into real nuScenes scenes while preserving their context. Its 21 tasks span six safety families and define hazard or conflict regions, local safety constraints, and acceptable responses. Because hazard inser...
  </details>

- **2026-09-29** — Timur Mudarisov, Mikhail Burtsev, Radu State — [The Geometry of Inference in Transformer Residual Streams](http://arxiv.org/abs/2609.37824v1)
  <details><summary>📄 Abstract</summary>
  Transformer language models build predictions through successive residual updates, but how their representations become specific to an eventual outcome remains unclear. We study this process by comparing intermediate residual states with their own final states and an empirical bank of final states from other contexts. Across six pretrained language models, the own endpoint becomes preferable to the average alternative early, while many individual endpoints remain closer. These competing sets gen...
  </details>

- **2026-09-29** — Xuanyu Zhu, Yan Bai, Yang Shi et al. — [HiRAE: Hierarchical Representation Autoencoding with Residual Budgets](http://arxiv.org/abs/2609.37775v1)
  <details><summary>📄 Abstract</summary>
  Pretrained visual representations support image generation, but may not fully preserve the fine-grained details needed for faithful reconstruction. Meanwhile, intermediate encoder layers contain complementary visual details, but learning to fuse them for reconstruction can produce a latent distribution that is difficult to model. Existing fusion methods require empirical tuning of layer selection or staged optimization of fusion and decoding, increasing configuration effort or training complexit...
  </details>

- **2026-09-29** — Yury Nahshan, Nati Daniel, Jacob Goldberger et al. — [Cross-Entropy Guided Routing in Mixture-of-Experts Large Language Models](http://arxiv.org/abs/2609.37751v1)
  <details><summary>📄 Abstract</summary>
  Sparse mixture-of-experts (MoE) large language models scale model capacity by routing each token to a small subset of experts. Their routers are regularized with load balancing terms and learn affinity scores through the language-model objective. However, these objectives do not provide direct alignment between routing affinities and token-level error. We introduce token-error supervision for sparse routing in two forms. The first form predicts an error score per expert. The affinity-weighted ag...
  </details>

- **2026-09-29** — Hyunseok Lee, Mihir Basil, Yizhou Liu et al. — [Optimizer-dependent training dynamics converge to the same one-third optimal data scaling](http://arxiv.org/abs/2609.37745v1)
  <details><summary>📄 Abstract</summary>
  Neural scaling, in which loss falls as a power law with training, is central to large language models, and one recent proposal is that a $1/3$ exponent emerges from learning peaked distributions. That account describes SGD, but models in practice are trained with adaptive optimizers. Here we separate two exponents the $1/3$ account does not distinguish: how fast the loss falls with training steps along a single run, and how fast the optimally tuned loss falls with dataset size $D$. We show that ...
  </details>

- **2026-09-29** — Ojas Shirekar, Yash Surange, Agustinas Jučas et al. — [Generative Interactions: Weaving Multiparty Human Motion with Bilevel Latent Dynamics](http://arxiv.org/abs/2609.37708v1)
  <details><summary>📄 Abstract</summary>
  Human social behaviour is not a collection of independent motions, but a jointly organised process in which group dynamics and individual variation continuously shape one another. Yet existing social motion models often prioritise plausible trajectories while leaving interaction state implicit, limiting their ability to transfer across groups, tasks, and partial-observation regimes. To address this gap, we introduce Bilevel Representations for Agent Interaction Dynamics (BRAID), a hierarchical s...
  </details>

- **2026-09-29** — Changmian Wang, Yuchao Ma, Xuchao Lu et al. — [KUPAS MASTER: Distilling the Tacit Expertise of Master Practitioners into Agent-Ready Experience Corpora](http://arxiv.org/abs/2609.37673v1)
  <details><summary>📄 Abstract</summary>
  Experienced professionals know more than just facts and conclusions. They know which cues matter, why a judgment is reasonable, and which action to take. Routine work records often leave out this tacit knowledge, making it difficult for Large Language Model (LLM) agents to use professional experience effectively. We introduce KUPAS MASTER, an experience engineering platform built around nine-layer cognitive corpus construction. It turns heterogeneous work records and practitioner interviews into...
  </details>

- **2026-09-29** — T. Duy Nguyen-Hien, Yee Whye Teh, Wee Sun Lee et al. — [Rational Clarification by Assistive Agents via Value-of-Information Reasoning](http://arxiv.org/abs/2609.37588v1)
  <details><summary>📄 Abstract</summary>
  Users of language-based assistive agents often make ambiguous requests. In response, an assistant can either directly act on its interpretation of the request --- risking misalignment with the user --- or ask a clarifying question. Which option is the most safe and helpful? A common approach is to ask questions that minimize uncertainty about the user's intent until a threshold is reached. However, this neglects the impact of uncertainty reduction on downstream performance, the costs of asking v...
  </details>

- **2026-09-29** — Milena Gazdieva, Kirill Sokolov, Jiawei Chen et al. — [Simultaneous Neural Optimal Transport](http://arxiv.org/abs/2609.37424v1)
  <details><summary>📄 Abstract</summary>
  Optimal Transport (OT) provides a principled framework for learning transformations between probability distributions from unpaired samples. In many applications, however, a single transformation must map several source distributions to a common target distribution. For example, image restoration might require handling different types of degradation without knowing the degradation of each input at inference time. Simple approaches of pooling the source distributions only encourage alignment with...
  </details>

- **2026-09-29** — Behraj Khan, Tahir Qasim Syed, Syed Ahmad Chan Bukhari — [Technical note on: Zero-Training Feature-Space Alignment via Information Geometry](http://arxiv.org/abs/2609.37302v1)
  <details><summary>📄 Abstract</summary>
  Deep vision models often degrade under distribution shift. Test-time adaptation can improve robustness but typically requires iterative optimization, hyperparameter tuning, and multiple forward-backward passes. We propose Zero-Training Fisher Geometry Alignment (ZFGA), a closed-form method that improves robustness under covariate shift without modifying model parameters. ZFGA is based on the observation that distribution shifts distort feature-space geometry. It estimates the Fisher information ...
  </details>

- **2026-09-29** — Xuyang Cao, Enyou Liu, Jun Zhao et al. — [SAM Meets VLM: Parameter-Decoupled Full-Parameter Training for Unified Medical Reasoning and Segmentation](http://arxiv.org/abs/2609.37283v1)
  <details><summary>📄 Abstract</summary>
  Medical multimodal large language models (MLLMs) are increasingly expected not only to answer clinical questions, but also to localize the visual evidence behind their predictions. A common strategy connects a vision--language model (VLM) with SAM-style segmentation through a special <SEG> token, yet full-parameter training of this unified architecture is difficult because image-level reasoning and pixel-level segmentation impose different requirements on the shared representation space. To addr...
  </details>

- **2026-09-29** — Woosang Jeon, Jiwon Yang, Soo Chung et al. — [Seeing Is Not Addressing: Auditing Linguistic Access to Frozen Visual Geometry](http://arxiv.org/abs/2609.37230v1)
  <details><summary>📄 Abstract</summary>
  Visual distinctions are often finer than those reflected in linguistic conceptualization. Vision-language models exhibit a similar asymmetry: a distinction can remain discriminable in frozen image geometry while being weakly addressable through the native text interface. We study this gap by separating visual discriminability from linguistic addressability in text-to-image retrieval. Using FactorAtlas, a fully crossed testbed of 23,040 images spanning shape, hue, pattern, and nuisance variation,...
  </details>

- **2026-09-29** — Xinkai Du, Chao Lv, Yalin Sun et al. — [Bridging Semantic Gaps in RAG through Generated Context Knowledge Fusion](http://arxiv.org/abs/2609.37171v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation has established itself as a fundamental framework in natural language processing, seamlessly integrating information retrieval with the generative capabilities of large language models. However, this process is fundamentally constrained by a critical challenge: semantic space mismatch between queries and retrieved contexts. We propose Knowledge-Aware Semantic Bridging (KASB), a novel framework that improves passage selection quality through semantic space alignment...
  </details>

- **2026-09-29** — Jiahao Zhan, Yongrui Ma, Qunliang Xing et al. — [MotionInsight: Diagnosing Object Motion Deficiencies in Generated Videos](http://arxiv.org/abs/2609.37030v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid progress in video generation models, they still exhibit obvious motion deficiencies, often manifested as incorrect object motion. However, most existing video quality evaluations focus on aesthetic quality or text-video alignment. To address this gap, we study object-centric motion fidelity assessment, evaluating target objects along object consistency, motion continuity, and physical plausibility. To achieve this, we first introduce VidMotion, a diagnostic dataset of 6,879 videos ...
  </details>

- **2026-09-29** — Junbo Shen, Jinying Gao, Bo Lei — [Language as the Interface: Foundation-Model Contrastive Learning Links Transcriptomes and Electrophysiology](http://arxiv.org/abs/2609.37024v1)
  <details><summary>📄 Abstract</summary>
  Integrating transcriptomic and electrophysiological data is essential for building multimodal foundation models for neuroscience. Patch-seq provides paired measurements of gene expression and intrinsic electrophysiology from the same neuron, establishing a basis for training cross-modal models. Here we introduce LangPatch, a foundation-model-based contrastive learning framework that uses paired Patch-seq data to align pretrained GenePT representations with electrophysiological phenotypes through...
  </details>

- **2026-09-29** — Guoqing Zhang, Rafik Hadfi, Takayuki Ito — [Physics-Informed Multi-Agent Coordination for Hospital Patient Flow Optimization](http://arxiv.org/abs/2609.37022v1)
  <details><summary>📄 Abstract</summary>
  Efficient patient flow coordination across autonomous hospital departments is critical for mitigating overcrowding and balancing resource utilization. While classical queueing theory, specifically open Baskett--Chandy--Muntz--Palacios (BCMP) networks, provides an interpretable mathematical topology for healthcare operations, analytical models rely on stationary assumptions and fixed routing matrices that degrade under state-dependent real-world dynamics. Conversely, centralized reinforcement lea...
  </details>

- **2026-09-29** — Pengyu Yan, Yixin Wu, Yunjie Tian et al. — [Back2Struct: Making Structured Images Editable Again](http://arxiv.org/abs/2609.37016v1)
  <details><summary>📄 Abstract</summary>
  Structured images, such as diagrams, charts, and flowcharts, are inherently symbolic and can be compactly represented in an editable format, yet in practice, they are often rendered as images, and therefore not graphically editable. This mismatch presents a significant challenge for researchers, engineers, and designers who wish to incorporate modified versions of existing graphic content into new materials without manually reconstructing it. In this study, we presentBack2Struct, which "makes st...
  </details>

- **2026-09-29** — Jingnan Pu, Zi-En Fan, Feng Lian — [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models](http://arxiv.org/abs/2609.36952v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at token-level generation but may learn undesirable abstract semantics and lack comprehensive perception. LLM-JEPA mitigates this by aligning different views of the same underlying knowledge via a joint-embedding predictive architecture (JEPA). However, strong alignment does not necessarily lead to accurate, stable predictions. To address this, we propose ER-JEPA, which adds an episodic replay path to LLM-JEPA. ER-JEPA stores training pairs in a memory. At each...
  </details>

- **2026-09-29** — Shengtian Yang, Ziyu Xiong, Kaibing Yang et al. — [SCA: Spatial Credit Assignment for Reinforcement Learning of GUI Agents](http://arxiv.org/abs/2609.36939v1)
  <details><summary>📄 Abstract</summary>
  GUI agents automate tasks on digital devices by grounding language instructions in visual interfaces. Existing group-relative reinforcement learning improves GUI action prediction by comparing the rewards of multiple responses sampled from the same GUI state. However, binary evaluation treats spatially different failed clicks as identical and provides no relative signal when all sampled clicks fail. To address these limitations, we propose Spatial Credit Assignment (SCA), which uses the screen c...
  </details>

- **2026-09-29** — Tianqi Zhao, Tianyi Zhuang, Shuo Duan et al. — [Architecture Alignment With Sparse Priors in Tabular Foundation Models](http://arxiv.org/abs/2609.36883v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) are increasingly popular because they deliver strong predictions on new datasets through in-context learning, without task-specific training or extensive tuning. Yet released TFMs differ simultaneously in their pretraining priors, architectures, and objectives, obscuring their respective inductive biases. We therefore examine one concrete capability: irrelevant-feature suppression. Across synthetic tasks and real-world datasets, adding null features causes substa...
  </details>

- **2026-09-29** — Ayan Sengupta, Vaibhav Seth, Tanmoy Chakraborty — [Distilling What Matters: Confidence-Aware Selective Distillation for Large Language Models](http://arxiv.org/abs/2609.36734v1)
  <details><summary>📄 Abstract</summary>
  Knowledge Distillation (KD) trains a smaller-capacity student model to imitate a larger-capacity teacher model by matching output distributions, implicitly assuming the teacher to be a reliable oracle. In large language models (LLMs), this assumption often fails: teacher predictions can exhibit high entropy and hallucinations, causing standard KD to degrade well-calibrated student priors. We propose CaRE-KD, a confidence-gated distillation framework that replaces static objectives with uncertain...
  </details>

- **2026-09-29** — Yanan Wang, Tingsong Li, Kaixun Jiang et al. — [Beyond Binary Preferences: Graded Preference Optimization for Limb-Motion Captioning](http://arxiv.org/abs/2609.36628v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) can generate rich video captions, yet often misidentify which person performs an action or which limb is involved, particularly across camera cuts. Improving these details requires evaluation and training that distinguish missing information from incorrect assertions. We introduce FlexBench, a benchmark spanning 3,105 shots and 18,161 evaluation queries, with human-verified identities and systematic per-person coverage of fine-grained limb actions and states. Its re...
  </details>

- **2026-09-29** — Hanwen Lu, Jun He, Mingjia Yang et al. — [CrossTimeEdit: A Decade-Spanning Cross-View Dataset and Reward-Guided Editing for Historical Street-View Generation](http://arxiv.org/abs/2609.36616v1)
  <details><summary>📄 Abstract</summary>
  Historical street-view imagery records urban evolution, but uneven coverage leaves substantial gaps in historical records. Generating plausible past appearances requires restoring changed structures while preserving persistent scene content. We construct VIGOR-his, a decade-spanning cross-view dataset containing 43,653 location-level quadruplets across 11 cities on three continents. Its automated pipeline performs spatial pairing, consistency screening, change classification, and the generation ...
  </details>

- **2026-09-29** — Yuzhou Wu, Longteng Fan, Zimeng Li et al. — [RoboChrono: A Real Robot Benchmark for Streaming Task Understanding](http://arxiv.org/abs/2609.36605v1)
  <details><summary>📄 Abstract</summary>
  Understanding ongoing robot manipulation requires models to interpret visual observations in relation to interaction history and task progress. We introduce RoboChrono, a benchmark for streaming task understanding comprising 39 scenarios and 34,713 evaluation instances, constructed from real robot executions and complementary bare-hand human recordings. The benchmark evaluates seven tasks grouped into recognition, alignment, and temporal grounding, covering action understanding and anticipation,...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 69 papers

- **2026-09-30** — Yiming Gao, Shaocheng Luo — [TACTIC: Temporal and Context-Aware LLM Tactical Planning for Roadside LiDAR Attacks](http://arxiv.org/abs/2609.39969v1)
  <details><summary>📄 Abstract</summary>
  Physical LiDAR attacks are often evaluated using fixed primitives and manually selected parameters, despite their strong dependence on surrounding traffic. We present TACTIC, a scene-aware framework that uses a multimodal large language model (MLLM) to coordinate state-adaptive roadside LiDAR attacks. Under a gray-box threat model, TACTIC relies only on an attacker-operated roadside perception stack, without accessing the victim LiDAR's native point clouds or internal processing. Local perceptio...
  </details>

- **2026-09-30** — Xiao Cui, Mo Zhu, Yulei Qin et al. — [Revisiting On-policy Adversarial Black-Box Distillation: Calibrating Groupwise Reward Geometry for Effective Advantage Construction](http://arxiv.org/abs/2609.39757v1)
  <details><summary>📄 Abstract</summary>
  Black-box distillation is a practical route for transferring capabilities from API-accessible large language models that expose only text outputs into smaller student models. Recent on-policy adversarial methods such as GAD improve over SeqKD by forming an adversarial loop between a critic and a student, where the critic provides rewards for GRPO-based student policy optimization over the student's sampled responses. However, GRPO computes advantages from the within-group relative rewards of stu...
  </details>

- **2026-09-30** — Yu Wang, Shuhao Li, Tao Yin et al. — [APTInvestBench: Evaluating Autonomous APT Investigation under Varying Telemetry](http://arxiv.org/abs/2609.38954v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents could help security operations centers (SOCs) investigate advanced persistent threats (APTs) by turning weak leads into evidence for intrusion scoping and response. Yet success under one telemetry setting does not establish robustness to changes in log collection, retention, or sampling. We introduce APTInvestBench, a benchmark for evaluating cross-telemetry robustness in autonomous APT investigation. It comprises 370 cases across seven SOC-inspired conditions, ...
  </details>

- **2026-09-30** — Nathan Tsoi, Michael J. Munje, Tejas Oberoi et al. — [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](http://arxiv.org/abs/2609.40245v1)
  <details><summary>📄 Abstract</summary>
  Robot navigation in dynamic, human-centered environments requires socially-compliant decisions grounded in robust scene understanding. Recent Vision-Language Models (VLMs) exhibit promising capabilities such as object recognition, common-sense reasoning, and contextual understanding, capabilities that align with the nuanced requirements of social robot navigation. However, it remains unclear whether VLMs can accurately understand complex social navigation scenes (e.g., inferring the spatial-temp...
  </details>

- **2026-09-30** — Mingyue Ma, Zongbo Han, Changqing Zhang et al. — [Predicting Multi-View Rashomon Representation: Can We Learn Where Models Disagree?](http://arxiv.org/abs/2609.39848v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly adopted across a wide range of applications, often serving as core blocks within AI systems. Yet different foundation models may encode the same input from multiple different views, leading to substantial representation disagreement, which we term Rashomon Representation. Such disagreement often signals inputs that a given model encodes in a way inconsistent with other models, offering a valuable yet underexplored signal for input reliability estimation. While ...
  </details>

- **2026-09-30** — Atsuki Yamaguchi, Tatsuro Inaba, Joel Niklaus et al. — [Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior](http://arxiv.org/abs/2609.39827v1)
  <details><summary>📄 Abstract</summary>
  Pre-pretraining (PPT) on synthetic non-natural language data improves token efficiency during language model pre-training (PT). Prior work attributes this gain to a grammatical prior, i.e., a structural inductive bias learned during PPT that transfers to natural language grammar. However, PPT has only been tested on models of at most 1B parameters and PT budgets below 2B tokens on predominantly web text. It is unknown whether PPT is effective at larger scales and under more realistic PT data mix...
  </details>

- **2026-09-30** — Meijia Chen, Hao Li, Zheng Lu et al. — [False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents](http://arxiv.org/abs/2609.39102v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving search agents build their own training curricula by jointly optimizing a proposer that generates questions and a solver that answers them. This closed loop introduces a failure mode we call co-cheating: the proposer and solver increasingly agree on shared errors, so internal reward improves without a matching gain in external correctness. A post-hoc audit against source evidence shows co-cheating growing more severe over successive rounds of self-evolution, with pseudo-label correc...
  </details>

- **2026-09-30** — Haoxuan Wang, Griffin Galimi, Junhua Huang et al. — [Cue the Flow: Steering Flow-Matching Policies for Open-World Delivery Manipulation](http://arxiv.org/abs/2609.38989v1)
  <details><summary>📄 Abstract</summary>
  Open-world goods delivery requires mobile manipulators to follow free-form user instructions and manipulate potentially novel objects. Existing dual-system approaches use high-level grounding models to convert language into grounded visual prompts, but their low-level controllers can remain brittle under noisy perception, dynamic scenes, and contact-rich interactions. We instead use a pretrained flow-matching vision-language-action model as the low-level control interface, leveraging its reactiv...
  </details>

- **2026-09-30** — Jiaheng Hu, Roberto Martin-Martin, Peter Stone et al. — [SimEX: Simulation-Integrated Robotics AutoResearch](http://arxiv.org/abs/2609.38982v1)
  <details><summary>📄 Abstract</summary>
  Coding agents powered by large language models (LLMs) have shown remarkable abilities to autonomously reason about and achieve goals in the digital world. However, bringing this success to the physical world remains challenging. On the one hand, direct generation methods (e.g., Code as Policies) often suffer from the LLMs' insufficient understanding of robots and physical environments. On the other hand, iterative trial-and-error tuning in the physical world (e.g., physical autoresearch) induces...
  </details>

- **2026-09-30** — Yingfeng Luo, Shaowei Wei, Daixin Wang et al. — [Can Terminal Agents Trust Their Own Verification? Diagnosing and Improving Self-Verification](http://arxiv.org/abs/2609.38812v1)
  <details><summary>📄 Abstract</summary>
  Terminal agents rely on self-verification to assess and correct their solutions as they solve tasks through interaction with command-line environments. Yet how trustworthy such self-verification is remains poorly understood. To investigate this question systematically, we introduce a diagnostic framework that identifies the first complete solution in each trajectory, determines whether it is objectively correct, and uses this ground truth to quantify the agent's subsequent verification and recov...
  </details>

- **2026-09-30** — Chunzheng Zhu, Jiaqi Zeng, Hongbo Zhao et al. — [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](http://arxiv.org/abs/2609.38810v1)
  <details><summary>📄 Abstract</summary>
  As vision language models are increasingly deployed in clinical diagnosis, understanding how they internally resolve competing visual and textual signals becomes a safety imperative. Existing mechanistic analyses remain confined to unimodal text and offer no explanation for why a single misleading sentence can override a correct image based diagnosis, or why a model commits to a confident answer despite insufficient visual evidence. We find that these two safety risks, arbitration failure where ...
  </details>

- **2026-09-30** — Victor Wang, Thomas Hofweber, Mohit Bansal et al. — [Evaluating Persistent Calibration under Evolving Model Knowledge](http://arxiv.org/abs/2609.38797v1)
  <details><summary>📄 Abstract</summary>
  As AI systems move from static repositories to agents that are capable of continual adaptation and learning, maintaining their trustworthiness means equipping the models backing them with the ability to produce confidence estimates that dynamically reflect their changing skills and knowledge. We introduce the problem of persistent calibration, which requires a confidence estimator to faithfully reflect the knowledge contained in a model as that knowledge changes, without recurring supervision. W...
  </details>

- **2026-09-30** — Ilgee Hong, Changlong Yu, Zhenghao Xu et al. — [Training LLM Judges from Language Feedback via Position-Selective Self-Distillation](http://arxiv.org/abs/2609.38792v1)
  <details><summary>📄 Abstract</summary>
  We study training LLM judges from natural language feedback, especially for subjective tasks where the verdict depends strongly on which evaluation criteria the judge invokes and how it weighs them. The dominant approach, outcome-supervised RL (e.g., GRPO), credits every token in the rollout with a single scalar determined only by the accuracy of the final verdict, providing no separate credit at the criterion-choice tokens and ignoring the rich language feedback (e.g., preference rationales) th...
  </details>

- **2026-09-30** — Mehdi Jafari, Hao Xue, Flora Salim — [MetaSteer: Context-Conditioned, nonlinear Steering via Attention-Projection Adaptation](http://arxiv.org/abs/2609.38718v1)
  <details><summary>📄 Abstract</summary>
  Steering large language models typically relies on linear, context-independent interventions in activation space, an assumption that recent work has challenged and that can induce an information bottleneck when a fixed representation must encode many behavioral distinctions. We introduce MetaSteer, a method that learns nonlinear interventions with context-dependent effects and applies them to attention projection matrices, producing activation effects that vary with the input context by construc...
  </details>

- **2026-09-30** — Jiahao Zhang, Yeying Fan, Moitreya Chatterjee et al. — [AssemblyWorld: Rethinking 3D Assembly with General-Purpose Agents](http://arxiv.org/abs/2609.40353v1)
  <details><summary>📄 Abstract</summary>
  The task of 3D assembly requires translating an understanding of parts and their relationships into precise spatial arrangements. Can pretrained general-purpose agents assemble objects through visual interaction without additional assembly-specific fine-tuning? To investigate this question, we introduce AssemblyWorld, an interactive 3D environment in which agents inspect rendered views and manipulate supplied rigid parts, guided by images or assembly manuals when available. Agents perceive part ...
  </details>

- **2026-09-30** — Qize Yu, Lianrui Fan, Boyu Chen et al. — [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](http://arxiv.org/abs/2609.39601v1)
  <details><summary>📄 Abstract</summary>
  Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-language and video-generation backbones, which still fail in these settings. We introduce GroundingPI, a 4B grounding foundation model that generates points and boxes as quantized coordinates in a shared voc...
  </details>

- **2026-09-30** — Zijie Diao, Yitong Chen, Sicheng Xie et al. — [LIBERO-Agent: Evaluating General-Purpose Agents for Direct Embodied Manipulation](http://arxiv.org/abs/2609.39507v1)
  <details><summary>📄 Abstract</summary>
  General-purpose agents can plan, use tools, and revise their behavior from feedback, but it remains unclear whether these capabilities transfer from digital environments to embodied manipulation. To investigate this question, we introduce LIBERO-Agent, an agent-native benchmark for evaluating these agents in robot manipulation tasks. Rather than asking agents to submit task-level Python control programs or operate through high-level robot skills, LIBERO-Agent provides an interactive robotic envi...
  </details>

- **2026-09-30** — Haoran Lang, Haotao Lu, Shiyu Sang et al. — [EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](http://arxiv.org/abs/2609.38905v1)
  <details><summary>📄 Abstract</summary>
  Adapting robot manipulation policies to new tasks and environments remains highly data-intensive, while the data needed for further improvement depends on the policy's current capabilities and failure modes. We introduce EmbodiRSI, an agentic system for recursive self-improvement (RSI) in a real-to-sim-to-real setting, where task-specific simulations are constructed from target deployment scenarios and used as low-cost environments for iterative policy improvement before transfer back to the phy...
  </details>

- **2026-09-30** — Zongwan Cao, Ziyuan Yang, Shangbin Feng et al. — [You're Hired: Strategic Model Selection for LLM Collaboration](http://arxiv.org/abs/2609.38816v1)
  <details><summary>📄 Abstract</summary>
  While multi-agent and model collaboration algorithms gain traction to combine the strengths of diverse Large Language Models (LLMs), existing systems remain bottlenecked on pre-defined and hand-crafted model pools. In this work, we investigate the problem of model selection in multi-LLM systems. We propose and systematically evaluate a taxonomy of 9 selection algorithms ranging from diversity of model descriptions, capability-aware behavioral diversity, and LLM-based recruiters. We conduct exten...
  </details>

- **2026-09-30** — Charlie Pyle, Prabir Daripa — [A Fast Nonuniform Solver for the Poisson Equation over a Disk](http://arxiv.org/abs/2609.40344v1)
  <details><summary>📄 Abstract</summary>
  We study fast numerical methods for the Poisson equation on a disk within the FFTRR (Fast Fourier Transform Radial Recurrence) framework, which is built on Green's function representations. Classical FFTRR schemes apply FFTs in the azimuthal variable and evaluate mode-by-mode radial recurrences, achieving a complexity of \(O(MN\log N)\) on an \(N\times M\) uniform grid. However, they require a uniformly spaced azimuthal mesh of \(N\) points. In this work we develop a Nonuniform (NUFFTRR) solver ...
  </details>

- **2026-09-30** — Zhenisbek Tagay, Ahmed Abouelkomsan, Yugo Onishi et al. — [Quantization through Dissipation and the Optical Quantum Hall Effect](http://arxiv.org/abs/2609.40337v1)
  <details><summary>📄 Abstract</summary>
  The integer quantum Hall effect remains the most paradigmatic and remarkable example of exact quantization in condensed matter physics. Its Hall conductivity $σ_{xy}$ is fixed to $e^2/h$ times an integer to a precision limited only by measurement and independent of disorder or interactions. This robustness has several explanations, each capturing a strikingly different piece of the physics. In Laughlin's gauge argument, flux insertion pumps an integer charge between edges, so quantization follow...
  </details>

- **2026-09-30** — Xiao-Hui Ni, Yu-Han Yao, Yu-Ze Zhu et al. — [QuLoC: Photonic Quantum-Assisted Low-Rank LLM Compression](http://arxiv.org/abs/2609.40146v1)
  <details><summary>📄 Abstract</summary>
  As LLMs grow in size, compression becomes increasingly important for efficient deployment. SVD-based low-rank compression reduces parameter counts but can degrade downstream performance. To improve performance after compression, we introduce QuLoC, a photonic quantum-assisted LLM compression algorithm that uses quantum circuit outputs to gate the retained low-rank components during training. Model performance is recovered through local functional reconstruction followed by end-to-end knowledge d...
  </details>

- **2026-09-30** — Mingchen Li, Rohan Pandey, Junhui Qian et al. — [OverdoseMoE: A Multi-Expert Framework for Opioid Overdose Risk Prediction](http://arxiv.org/abs/2609.40108v1)
  <details><summary>📄 Abstract</summary>
  Opioid overdose remains a major clinical and public health burden, highlighting the need for scalable approaches to identify patients at high risk. Here, we investigate diagnosis-specific adaptation for 180-day opioid overdose risk prediction from patients' preceding one-year longitudinal ICD histories. We develop OODMAMBA and OODQWEN through continued pretraining on longitudinal diagnostic sequences followed by task-specific fine-tuning. Building on the stronger Qwen-based predictors, we furthe...
  </details>

- **2026-09-30** — Hung-Jen Chen, Yu-Hsun Hou, Yan-Hong Chen et al. — [When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models](http://arxiv.org/abs/2609.39971v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models can exceed 90% success on in-distribution tasks and withstand nuisance changes that preserve the required action, yet fail under counterfactual changes that demand a different action. Aggregate robustness scores can therefore conceal a more specific failure, in which a policy responds to both language and vision yet does not combine them to select the action the task requires. We call this failure instruction-action binding. Instructions cue familiar trajector...
  </details>

- **2026-09-30** — Frances Liu, Manny Silva, Paige Calvert et al. — [DoGBench: Can Agents Meet Expert Standards for User-Facing Documentation?](http://arxiv.org/abs/2609.39909v1)
  <details><summary>📄 Abstract</summary>
  We introduce DoGBENCH (Documentation Generation Benchmark), to our knowledge, the first benchmark for generating and maintaining real user-facing software documentation. It asks whether an agent can produce documentation that experienced technical writers would accept in review. The benchmark contains 292 items from open source projects, including Helm, PostHog, and Mautic. Each item gives the agent a pre-change repository and a trigger, such as a code pull request or a reported documentation ga...
  </details>

- **2026-09-30** — Chin-Yun Yu, Chi-Jen Peng, Li Su et al. — [Pitch Smoothing Using Relative Interval Networks](http://arxiv.org/abs/2609.39852v1)
  <details><summary>📄 Abstract</summary>
  Pitch tracking systems typically couple a per-frame fundamental frequency ($F_0$) estimator with a temporal smoothing stage to obtain continuous trajectories. Conventional Viterbi smoothers enforce first-order continuity but lack long-term temporal awareness and could lock into octave errors across corrupted frames. We propose Relative Interval Networks (RIN), a trajectory smoothing framework that reconciles per-frame pitch estimates with data-driven multi-hop pitch differences. We extract robus...
  </details>

- **2026-09-30** — Sharareh Sayyad, Sophia Bazzi — [TopTimeNet: Topologically-assisted time-series classification model](http://arxiv.org/abs/2609.39792v1)
  <details><summary>📄 Abstract</summary>
  Distinguishing periodic from chaotic dynamics in a time series is a fundamental challenge in both physics and engineering. Yet, end-to-end learned architectures must discover both a representation and a decision boundary from data, at substantial cost. We introduce TopTimeNet, which decouples these tasks: a fixed, non-learned stage extracts a $42$-dimensional geometric and topological descriptor from Takens delay embeddings and persistent homology, and a lightweight learnable stage performs clas...
  </details>

- **2026-09-30** — Yifeng Wang, Lin Shi, Fenglai Huang et al. — [Generalised Mixing-Plane Method for Compressible Reacting-Mixture Flows in Steady Multiphysics Turbomachinery Simulations](http://arxiv.org/abs/2609.39746v1)
  <details><summary>📄 Abstract</summary>
  The mixing-plane method plays a pivotal role in steady simulations of multiple turbomachinery components. With advances in computational power, a whole-engine gas turbine simulation is no longer an elusive approach. However, whole-engine simulations require simultaneous coupling of the compressor, turbine and combustor. A key challenge is that the working fluid after the combustor can no longer be treated as a perfect gas, since the combustion introduces composition variations and combustion pro...
  </details>

- **2026-09-30** — Thorsten Kurth, Max Rietmann, Mauro Bisson et al. — [A library for differentiable signal processing and machine learning on the sphere](http://arxiv.org/abs/2609.39737v1)
  <details><summary>📄 Abstract</summary>
  The two-dimensional sphere embedded in three-dimensional Euclidean space S2, plays a central role in a variety of scientific and engineering domains, including geophysics, planetary science, geodesy, atmospheric physics, quantum chemistry, cosmology, and virtual reality, among many others. As machine learning increasingly permeates these fields, the demand grows for robust tools that process and model functions on the sphere, while respecting the inherent topological and symmetry properties of t...
  </details>

- **2026-09-30** — Muhammad Zawish, Steven Davy — [When Masking Helps or Hurts Robustness in Compressed CLIP: A Pre-Deployment Diagnostic](http://arxiv.org/abs/2609.39704v1)
  <details><summary>📄 Abstract</summary>
  This paper demonstrate that whether masking-based token pruning helps or hurts worst-group robustness can be predicted before deployment, without labels or fine-tuning. A systematic study of semantic masking across 8 spurious-correlation benchmarks shows its effect on worst-group accuracy is highly unstable: it improves accuracy by up to 82.5\% relative on some datasets and degrades it by up to 100\% on others. We trace this instability to spurious inversion: background patches receive higher CL...
  </details>

- **2026-09-30** — Alessio Spagnoletti, Charlesquin Kemajou Mbakam, Jonathan Spence et al. — [BAM! Bayesian Anything Model: a foundation model for generative computational imaging](http://arxiv.org/abs/2609.39660v1)
  <details><summary>📄 Abstract</summary>
  Generative models are transforming Bayesian computational imaging, yet the field still lacks physics-aware foundation models. Current practice falls into two camps. Large foundation image models are deployed as plug-and-play priors with zero-shot approximate likelihood guidance, which introduces significant bias and computational cost. Physics-aware generative models avoid this bias, but each is tied to a specific dataset, task and instrument. We introduce BAM (Bayesian Anything Model), a lightw...
  </details>

- **2026-09-30** — Yinghao Xie, Zhenbang Dai, Haojun Wang et al. — [Robust Transfer Learning for Paper ECG Recognition](http://arxiv.org/abs/2609.39581v1)
  <details><summary>📄 Abstract</summary>
  Paper ECG recognition is challenging because real-world ECG images vary in layout, physical artifacts, and label availability. We introduce RobECG-CL, a rank-aware contrastive learning framework for robust paper ECG representation learning. Starting from standard 12-lead ECG recordings, we construct progressively degraded paper ECG views with heterogeneous layouts and train the model to balance same-recording invariance with degradation-aware ordering. Across synthetic stress tests on CODE-II an...
  </details>

- **2026-09-30** — Bo Han, Qianyi Wang, Shuai Liu et al. — [Learning Reliable GUI Agents under Imperfect Priors](http://arxiv.org/abs/2609.39547v1)
  <details><summary>📄 Abstract</summary>
  GUI agents built on large language and vision-language models still struggle on unseen applications and complex multi-step tasks, as completing real GUI tasks depends on app-specific, temporally volatile operational knowledge that is scarce in pretraining corpora. Retrieval-augmented execution offers a natural remedy but faces two coupled bottlenecks: knowledge at scale is hard to acquire, and self-collected priors inevitably drift from the live environment due to version updates, promotions, ad...
  </details>

- **2026-09-30** — Tarun Yenamandra, Jonathon Luiten, Daniel Cremers et al. — [Lens Flare Removal and Reconstruction](http://arxiv.org/abs/2609.39527v1)
  <details><summary>📄 Abstract</summary>
  The presence of lens flares in images can significantly reduce the quality of downstream application results for tasks such as 3D scene reconstruction. This is because lens flares are a property of the camera imaging system, and not a part of the underlying scene being modeled. There are previous methods that tackle the removal of small flares focused around a light source. However, existing methods struggle with large flares, such as those that fill the entire image. In this work, we compile a ...
  </details>

- **2026-09-30** — Farhad Rezazadeh, Hatim Chergui, Lingjia Liu et al. — [Resource-Efficient Semantic Communication for Heterogeneous Agentic Teams](http://arxiv.org/abs/2609.39477v1)
  <details><summary>📄 Abstract</summary>
  Teams of autonomous agents, including large language model (LLM) agents, must coordinate over scarce and unreliable wireless links. We propose goal-oriented semantic communication (GOSC), a closed-loop co-design that jointly decides what each agent sends, when it sends it, and how reliably it is transmitted, based on each message's value to the team task. An edge broadcast of the team's common knowledge closes the loop by updating these values. We prove that a message is sent only if its value e...
  </details>

- **2026-09-30** — Irene Lago, Ana Ezquerro, David Vilares — [Synthetic Data Characterization via Training Dynamics](http://arxiv.org/abs/2609.39447v1)
  <details><summary>📄 Abstract</summary>
  Interpreting properties of LLM-generated data is important for understanding its utility and limitations across learning tasks. In this work, we characterize synthetic data through sample-level learnability, studying variation among LLM families and scales, alongside human-written data as a reference. We first generate synthetic datasets spanning single- and multi-label classification, labeling, and tree prediction tasks. We then derive empirical data distributions from encoder training dynamics...
  </details>

- **2026-09-30** — Shu Yu, Chaochao Lu — [CAST: Causal Advantage-Structured Training with Spatially Grounded Compositional Rewards for Diffusion Models](http://arxiv.org/abs/2609.39441v1)
  <details><summary>📄 Abstract</summary>
  Online reinforcement learning has been extended to flow matching for diffusion model (DM) image generation. However, this paradigm faces three limitations: (1) Window selection. Existing methods manually set the stochastic differential equation (SDE) sampling window, i.e., the denoising steps where exploration noise is injected. We instead determine it from each model's denoising trajectory. (2) Reward saturation. Current methods rely on scoring models trained on human annotations; we find that ...
  </details>

- **2026-09-30** — Yitong Qiao, Yancheng Jin, Lei Liu et al. — [EHR-RobustGym: Benchmarking and Training Agents for Robust Clinical Reasoning](http://arxiv.org/abs/2609.39371v1)
  <details><summary>📄 Abstract</summary>
  In hospital workflows, electronic health records (EHRs) are often noisy, and may not contain the evidence needed to confirm events or measurements referenced in a clinical query. Even when database retrieval succeeds, clinical agents can overlook such discrepancies and return plausible but unsupported answers. We introduce EHR-RobustGym, a scalable and interactive environment for evaluating and training robust clinical agents grounded in noisy EHRs. Built on MIMIC-IV hospital records (365K patie...
  </details>

- **2026-09-30** — Linrui Qian, Jiajia Zhang, Gan He et al. — [A Biophysically Detailed C. elegans Circuit as a Task-Agnostic Dynamical Core for Visually Robust Robot Manipulation](http://arxiv.org/abs/2609.39322v1)
  <details><summary>📄 Abstract</summary>
  Robot policies are usually trained for one task, one body and one visual environment, and generalize poorly beyond these conditions. Whether a nervous system can instead supply the sensorimotor computation through its evolved wiring and biophysics remains unresolved. Here we embed a biophysically detailed Caenorhabditis elegans sensorimotor circuit - 136 multicompartment neurons with realistic morphologies and electrophysiological characteristics - as the dynamical core of a visuomotor policy. O...
  </details>

- **2026-09-30** — Shengjie Jin, Hengbo Xu, Zelong Sun et al. — [ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation](http://arxiv.org/abs/2609.39306v1)
  <details><summary>📄 Abstract</summary>
  Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving PI-conditioned behavior as the student becomes the next teacher. We introduce Reten...
  </details>

- **2026-09-30** — Jinsung Jeon, Seung-won Hwang — [ANI: Adaptive Numerical Injection for Unifying Semantic and Arithmetic Representations in Numerical Reasoning](http://arxiv.org/abs/2609.39294v1)
  <details><summary>📄 Abstract</summary>
  Precise numerical reasoning with Large Language Models (LLMs) is essential for expanding their applicability to complex real-world tasks. However, text-based tokenization often fragments numbers, significantly hindering precise arithmetic reasoning. Meanwhile, numerical embeddings, despite arithmetic precision, rely on context-agnostic substitution that disregards the semantic role of numbers as identifiers. To combine the complementary strengths, we propose \textbf{ANI (Adaptive Numerical Injec...
  </details>

- **2026-09-30** — Shengbo Cai, Zhisheng Zhang, Zichao Nie et al. — [UniAE-MoE: A Unified Audio Encoder via Mixture of Experts](http://arxiv.org/abs/2609.39199v1)
  <details><summary>📄 Abstract</summary>
  Large Audio Language Models (LALMs) rely on effective audio encoders for multi-task performance. We introduce UniAE-MoE, a unified audio encoder designed to model cross-domain audio representations and achieve outstanding downstream understanding performance via a Mixture-of-Experts (MoE) architecture. Specifically, we explore mainstream audio encoders and integrate those from Qwen2-Audio and Audio-Flamingo 3, which demonstrate superior downstream capabilities. To facilitate effective model fusi...
  </details>

- **2026-09-30** — Dong Gyun Kang, Megha Thukral, Kwangsoo Kim — [Attention Function as an Intrinsic Inductive Bias: How Models' Behavior Diverges in Novel Contexts](http://arxiv.org/abs/2609.39188v1)
  <details><summary>📄 Abstract</summary>
  Developmental psychology holds that certain priors are given to infants prior to experience rather than induced from data, and that the influence of such priors is suppressed under strong, well-constrained conditions but reasserts itself under weak ones. We ask whether an analogous principle holds for the Transformer: can the activation function given to attention heads serve as an intrinsic inductive bias? We propose Mixture of Function Attention (MoFA), a parameter-free modification to multi-h...
  </details>

- **2026-09-30** — Kaijun Feng, Jiaxin He, Hongrui Yu et al. — [Deep Learning-Based Tri-Hybrid Multi-User MIMO Precoding: The Blessing of EM-Reconfigurable Antennas](http://arxiv.org/abs/2609.39167v1)
  <details><summary>📄 Abstract</summary>
  Electromagnetic (EM)-reconfigurable antennas provide multiple candidate radiation patterns per element, thereby introducing an additional EM-domain degree of freedom. Integrating radiation-pattern reconfigurability, realized as EM-domain precoding, with conventional hybrid analog-digital precoding yields tri-hybrid multiple-input multiple-output (MIMO) precoding, which can substantially improve the spectral efficiency of wideband multi-user MIMO orthogonal frequency-division multiplexing (OFDM) ...
  </details>

- **2026-09-30** — Xingming Shui, Dapeng Chen, Bowei Liu et al. — [OP-CAD: On-Policy Clean-Audio Distillation for Robust Audio-Visual Reasoning](http://arxiv.org/abs/2609.39150v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models deployed in real-world environments encounter external noise that can interfere with their perception and understanding of multimodal inputs. We study their robustness in audio-visual understanding, focusing on question answering under environmental noise and competing speech. The challenge is to resist acoustic interference while preserving useful audio evidence. On-policy distillation provides dense teacher feedback on student-generated responses, but uniform t...
  </details>

- **2026-09-30** — Yongjiang Liu, Jie Zhang, Haoyue Zhang et al. — [Beyond Prediction: Steering VLM Agents with Retrospective World Modeling](http://arxiv.org/abs/2609.39101v1)
  <details><summary>📄 Abstract</summary>
  Equipping VLM agents with world modeling capabilities has shown strong potential for complex reasoning and long-horizon planning, while reducing the dependence of policy learning on costly real-world interactions. Existing methods mainly rely on prospective simulation to predict the consequences of candidate actions. However, this forward-only paradigm focuses on what will happen next and provides limited constraints for verifying whether an action is causally consistent with the observed state ...
  </details>

- **2026-09-30** — Yizhou Wu, Ryan J. Sanford, Huiqiao Xie et al. — [An Uncertainty-Guided Digital Twin Framework for Online Adaptive Proton Therapy in Head and Neck Cancer: A Feasibility Study](http://arxiv.org/abs/2609.39010v1)
  <details><summary>📄 Abstract</summary>
  Objective: Head and neck (HN) proton therapy spans six to seven weeks of anatomical change, while offline replanning takes about a week. We present an uncertainty-guided digital twin (UGDT) framework that forecasts treatment-day anatomy before treatment and evaluate whether it generates online adaptive proton therapy (APT) plans of clinical quality. Approach: A library of 302 longitudinal deformations from 88 previously treated HN patients was transported onto each new patient's treatment planni...
  </details>

- **2026-09-30** — Chang Liu, Yu Tian, Rui Xie — [Mitigating Object Hallucination in Large Vision-Language Models via False Discovery Controlled Visual Data Splitting](http://arxiv.org/abs/2609.38979v1)
  <details><summary>📄 Abstract</summary>
  Multiple object hallucination, where large vision-language models (LVLMs) generate objects not supported by the visual input, is a persistent challenge caused by visual uncertainty during decoding. Existing methods reduce hallucinations using contrastive signals, but they rely on heuristics and lack principled control of false positives at the image level. To address this, we propose False Discovery Rate-COntRol of HALlucination (CORAL), a training-free framework that models visual uncertainty u...
  </details>

- **2026-09-30** — Jialu Pi, Yanan Ma, Weijie Chen et al. — [From Image Interpretation to Clinical Reasoning: Upstream Physician-Context-Aware Multimodal Learning with Causal Reinforcement Learning](http://arxiv.org/abs/2609.38924v1)
  <details><summary>📄 Abstract</summary>
  Major adverse cardiovascular events (MACE) remain the leading cause of mortality worldwide. Opportunistic screening using routinely acquired clinical data offers a scalable approach for identifying high-risk individuals before acute events occur. Although chest X-rays (CXRs) capture latent cardiovascular biomarkers and clinical histories provide complementary patient context, existing medical vision-language models are primarily optimized for radiology interpretation rather than prognostic reaso...
  </details>

- **2026-09-30** — Peng Kuang, Haibo Jin, Dehao Wu et al. — [Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives](http://arxiv.org/abs/2609.38912v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses govern how large language models (LLMs) gather context, invoke tools, verify results, preserve state, and terminate, largely affecting agent performance. However, the value of each harness mechanism can differ across heterogeneous tasks: a mechanism that improves one task may impose overhead or context distraction on another, leading to the suboptimality of a global harness. We characterize this suboptimality as a mismatch induced by fixed mechanism choices, motivating task-speci...
  </details>

- **2026-09-30** — Thilo Tamme, David Steck, Anton Hantel — [Persona and Persuasive Framing in AI Voice Agents: A $2\times2$ Field Experiment with Children](http://arxiv.org/abs/2609.38782v1)
  <details><summary>📄 Abstract</summary>
  Conversational agents increasingly interact with children, yet evidence on how their design shapes children's susceptibility to persuasion comes almost entirely from the lab. We report a $2\times2$ randomized field experiment embedded in a public German Santa Claus telephone hotline. Children's calls were randomly routed to one of four LLM voice agents varying persona (Santa, high authority, vs. Helper, low authority) and framing (persuasive nudges toward prosocial wishes vs. neutral). Of 1,072 ...
  </details>

- **2026-09-30** — Xinhe Wu, Yadong Jin — [ChartDensity-Bench: Benchmarking MLLMs for Numerical Data Reconstruction under Visual Density](http://arxiv.org/abs/2609.38781v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) offer a promising approach for recovering numerical data from scientific charts, but their ability to reconstruct chart data from visually dense figures remains poorly understood. Existing chart understanding benchmarks primarily evaluate question answering or chart-level reasoning and provide limited support for evaluating structured numerical reconstruction from scientific figures. We introduce \textbf{ChartDensity-Bench}, a benchmark for evaluating MLL...
  </details>

- **2026-09-29** — Wang Wei, Harry Yang, Tiankai Yang et al. — [FlexRouter: Learning Complementary Model Sets for Flexible LLM Routing](http://arxiv.org/abs/2609.38585v1)
  <details><summary>📄 Abstract</summary>
  Existing Large Language Model (LLM) routing methods score LLMs independently to select top-$k$ models. However, this ignores model correlations and enforces a rigid computational budget. Consequently, routers often select redundant models that share failure modes, limiting the overall probability of success. To address this, we propose FlexRouter, a routing framework that explicitly models model complementarity. FlexRouter optimizes for \textit{answer coverage}, maximizing the probability that a...
  </details>

- **2026-09-29** — Zhangshu Joshua Jiang, Zina Ibrahim, James T. Teo — [A Proposed Rubric for Evaluating Expressed Clinical Reasoning in Large Language Model Responses](http://arxiv.org/abs/2609.37788v2)
  <details><summary>📄 Abstract</summary>
  We propose a rubric for assessing expressed clinical reasoning in model responses, drawing on three bodies of work: medical education assessment frameworks (ART, SCT, Key Feature Problems and OSCE); clinical LLM benchmarks (MedR-Bench, HealthBench, TIMER-Bench, DR.BENCH, PrIME-LLM and PatientSafeBench); and general LLM reasoning evaluation research, including the Factuality-Validity-Coherence-Utility taxonomy, FaithCoT-Bench and C2-Faith. We use groundedness as a clinically oriented adaptation o...
  </details>

- **2026-09-29** — Bo Ni, Li Li, Ryan A. Rossi et al. — [Prompt2Skill: Unsupervised Skill Optimization From Natural Language Instructions](http://arxiv.org/abs/2609.38593v1)
  <details><summary>📄 Abstract</summary>
  Skills are external artifacts that Large Language Models (LLMs) consume at inference time to improve their performance on specialized domains by incorporating relevant procedural and domain knowledge. Expert-authored skills are expensive to produce, and the resulting artifacts are not optimized for the specific model that consumes them, whose failure modes can vary with version, scale and training. In addition, emerging tasks may fall outside the scope of existing skill libraries, creating a nee...
  </details>

- **2026-09-29** — Ke Zhang, Danica J. Sutherland, Chao Liu — [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](http://arxiv.org/abs/2609.38401v1)
  <details><summary>📄 Abstract</summary>
  Training data variation, whether through designing a domain randomization (DR) scheme in simulation or curating demonstrations for imitation learning, is a primary lever for improving the robustness of robotic manipulation policies. Yet its underlying mechanisms remain poorly understood, and practitioners typically select randomization parameters through expensive trial and error. We investigate these mechanisms through a series of case studies, randomizing object size, color, and type as well a...
  </details>

- **2026-09-29** — Olivia Macmillan-Scott, Michael Jacobs, Nils Metternich et al. — [Framing the Narrative: Ideological Mimicry in Large Language Models](http://arxiv.org/abs/2609.38256v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to answer questions about politically contentious issues, yet evaluations typically treat a model's stance as a relatively stable property. Real users, however, communicate political signals through their terminology, assumptions, and personal context. We investigate whether such signals produce ideological mimicry: systematic shifts in the political stance expressed by an LLM toward the position conveyed by the interaction. If LLMs adapt their ...
  </details>

- **2026-09-29** — Qijia He, Yu Huang, Yuan Cheng et al. — [Provable Test-Time Scaling for Beam Search in LLM Reasoning](http://arxiv.org/abs/2609.38672v1)
  <details><summary>📄 Abstract</summary>
  Beam-search-based test-time methods provide an effective way to improve large language model (LLM) performance on long-horizon generation by pruning invalid reasoning paths early, leading to significantly improved reasoning efficiency and more favorable test-time cost scaling. Despite strong empirical success, the theoretical understanding of beam search remains limited. In this paper, we study the test-time compute guarantee of the commonly used beam search framework that uses the model's inter...
  </details>

- **2026-09-29** — Bhagyesh Rathi, Eshan Chawla, William B. Andreopoulos — [Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG Strategies for Scientific Question Answering](http://arxiv.org/abs/2609.38473v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is now the standard way to ground Large Language Models (LLMs) in external knowledge, yet the design space of retrieval pipelines is large and the trade-offs between variants are not well understood, especially on domain-specific corpora at realistic scale. In this work, we present a controlled comparison of six retrieval strategies for scientific question answering: (i) classic top-k dense retrieval, (ii) LLM-based query rephrasing, (iii) query rephrasing fo...
  </details>

- **2026-09-29** — Yining Lu, Aurelie Lozano, Xi Yang et al. — [MoFlow: Multi-Objective Agentic Workflow Generation](http://arxiv.org/abs/2609.38294v1)
  <details><summary>📄 Abstract</summary>
  We study the generation of agentic workflows that jointly optimize multiple objectives, such as accuracy, cost, latency, robustness, and consistency. Existing methods for workflow generation typically optimize accuracy alone or a weighted sum of objectives, so each trained generator commits to one fixed trade-off and must be retrained from scratch when preferences change. To alleviate this, we propose MoFlow, which generates workflows optimized across varied preferences. Specifically, MoFlow for...
  </details>

- **2026-09-29** — Zhangshu Joshua Jiang, Zina Ibrahim, James T. Teo — [A Proposed Rubric for Evaluating Expressed Clinical Reasoning in Large Language Model Responses](http://arxiv.org/abs/2609.37788v1)
  <details><summary>📄 Abstract</summary>
  Rubrics support the structured evaluation of language models. We propose a rubric for assessing expressed clinical reasoning in model responses, drawing on three bodies of work: medical education assessment frameworks (ART, SCT, Key Feature Problems and OSCE); clinical LLM benchmarks (MedR-Bench, HealthBench, TIMER-Bench, DR.BENCH, PrIME-LLM and PatientSafeBench); and general LLM reasoning evaluation research, including the Factuality-Validity-Coherence-Utility taxonomy, FaithCoT-Bench and C2-Fa...
  </details>

- **2026-09-29** —  GuangJian Team, Kaili Huang, Yongshuo Zhang et al. — [PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence](http://arxiv.org/abs/2609.37712v1)
  <details><summary>📄 Abstract</summary>
  Optical Character Recognition (OCR) is evolving from plain-text transcription toward general visual intelligence, requiring models to recognize, localize, and reason over textual information in complex visual environments. However, existing OCR systems often excel at only some tasks and struggle to balance recognition, parsing, and reasoning across scenarios. In this report, we present PolyOCR, a family of unified OCR foundation models of varying scales. PolyOCR combines a shared instruction-fol...
  </details>

- **2026-09-29** — Alix Jeannerot, Petko Petkov, Alvaro Valcarce Rial — [Sequence Models for Layer-3 Protocol Emulation](http://arxiv.org/abs/2609.37697v1)
  <details><summary>📄 Abstract</summary>
  This article investigates whether Layer-3 radio-protocol behavior can be represented by compact sequence models suitable for deployment inside the RAN. We introduce the RRC sequence engine (RSE), a hybrid architecture in which a sequence model predicts protocol-dependent message structure while deterministic components retain control over security-sensitive or configured fields and over transport containers. Using NR protocol traces, we show that protocol-aware tokenization, cross-stack context,...
  </details>

- **2026-09-29** — Thibaud Gloaguen, Robin Staab, Martin Vechev — [AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks](http://arxiv.org/abs/2609.37310v1)
  <details><summary>📄 Abstract</summary>
  With LLM watermarking being deployed commercially and now required by regulations, improving its reliability and effectiveness has become crucial. Yet, recent progress in the field of LLM watermarking has increasingly been driven by improving details of existing methods, an effort fundamentally limited by the pace of human researchers. In this work, we enable for the first time the autonomous discovery of new distortion-free state-of-the-art watermarking schemes. To enable this, we (i) establish...
  </details>

- **2026-09-29** — Chenxing Wei, Sichen Liu, Lizhao Liu et al. — [OptiCom : A Unified Framework for State-Conditioned Composition in LLM-Driven Optimization](http://arxiv.org/abs/2609.37221v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed to solve complex scientific and practical problems via iterative optimization. However, dynamically coordinating diverse search mechanisms as candidate quality, failure modes, and resource budgets evolve remains a critical open challenge. Targeted empirical diagnostics reveal that mechanism effectiveness is highly state-dependent. Motivated by this, we analyze how individual decisions drive final outcomes, decomposing the expected terminal i...
  </details>

- **2026-09-29** — Aulia Kharis Rakhmasari, Fan Yu, Alexander Hoyle et al. — [FinRegQA-EU: Corruption-Based Preference Data for Grounded EU Financial Regulatory Question Answering](http://arxiv.org/abs/2609.36856v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) struggle with region-specific factual knowledge, particularly in financial regulation. While benchmarks such as CFinBench, provide broad coverage of financial knowledge in other regions, no comparable resource exists for European financial regulation. We close this gap by proposing an end-to-end pipeline for evaluating and improving LLMs on European financial regulatory question answering. Our dataset is grounded in the official Q&A corpora of the European Banking Au...
  </details>

- **2026-09-29** — Hada Melino Muhammad, Luan Pham, Laure Barrière et al. — [Where Root Cause Analysis Fails: A Retrieval-Reranking Decomposition](http://arxiv.org/abs/2609.36686v1)
  <details><summary>📄 Abstract</summary>
  Identifying the root cause of an anomaly among hundreds of sensors is critical for preventing safety incidents and costly downtime in complex monitored systems. Existing studies evaluate root cause analysis (RCA) methods using top@k accuracy. We show that this metric has a fundamental blind spot: it conflates two failure modes, retrieval failure, where the true cause is never considered, and reranking failure, where it is considered but ranked too low. In this work, we introduce a retrieval-rera...
  </details>

- **2026-09-29** — Giung Lee, Weihang Guo, Lydia E. Kavraki — [Foundation-Model-Guided Topology-Aware Semantic Risk Fields for Manipulation](http://arxiv.org/abs/2609.36640v1)
  <details><summary>📄 Abstract</summary>
  Robot motion planning in everyday environments must satisfy hard geometric constraints while accounting for context-dependent semantic risk. We present a foundation-model-guided, topology-aware semantic risk field that extends manipulation safety beyond collision avoidance. For each manipulated-object/scene-object pair, a foundation model provides six directional risk weights and a pair-specific spatial decay scale. The method combines these priors with voxelized 3D scene geometry using topology...
  </details>

- **2026-09-29** — Guanghui Min, Liang Wu, Mingjia Shi et al. — [Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations](http://arxiv.org/abs/2609.36526v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents require context compression to manage growing interaction histories. Compression quality, however, is ultimately determined by downstream execution. Existing prompt-adaptation methods infer compression errors by comparing full-context and compressed trajectories. Such comparisons cannot isolate individual compressions and are confounded by agent stochasticity. We first find that compression degrades reliability before solvability. Using matched counterfactual continuations th...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 20 papers

- **2026-09-30** — Haohan Yuan, Simin Chen, Xi Niu et al. — [Forging LLM Authorship Fingerprints with Targeted Rewriting](http://arxiv.org/abs/2609.38831v1)
  <details><summary>📄 Abstract</summary>
  Model-attribution classifiers can often identify which language model produced a text, making model-specific writing patterns a signal of provenance. Accurate attribution on unmodified text, however, does not show whether the prediction still identifies the original source after deliberate rewriting. We formulate this problem as targeted fingerprint transfer: rewriting one model's output so that attribution classifiers assign it to a chosen target model. We study summarization, where different m...
  </details>

- **2026-09-30** — Wei Song, Yuxin Cao, Xi Zheng et al. — [Preserving Provenance in Shared KV Caches for LLM Serving](http://arxiv.org/abs/2609.38706v1)
  <details><summary>📄 Abstract</summary>
  Production LLM serving stacks combine an inference engine's local prefix cache with a shared KV-cache tier for fleet-wide reuse. The local cache distinguishes requests by adapter, weight configuration and sharing domain, but the shared tier may key entries only by token content and coarse model metadata. This boundary erases provenance and lets identical tokens under incompatible computational or sharing contexts collide. We call this composition gap provenance-blind reuse and present its first ...
  </details>

- **2026-09-30** — Chang Xiao — [Who Asked for This? Inline Annotations as Authoring Transactions for Provenance in Agentic Authoring](http://arxiv.org/abs/2609.40126v1)
  <details><summary>📄 Abstract</summary>
  Writing with AI agents turns a paragraph into the outcome of many requests, yet the finished document rarely explains which request produced which change. We introduce Reactant, an interaction paradigm in which authors place typed inline annotations in their original documents. A verified transaction protocol records each request, skill identity, and the correspondences that identify additions, deletions, and transformations. The kernel validates the witness against the recorded states to establ...
  </details>

- **2026-09-30** — Shuyang Zhang, Jianshuo Chang — [What Can Component-Replacement Evidence Establish? A Critical Scoping Review of Local Decisions in LLM Agents](http://arxiv.org/abs/2609.39989v1)
  <details><summary>📄 Abstract</summary>
  Background. A component replacement in a language-model agent changes an execution trajectory, potentially altering later observations, resource use, and recovery opportunities. Different evidence is needed to assess its task-level benefit and the contribution of local decision quality. Methods. This critical scoping review maps 348 studies and examines 90 comparison records: 88 from 40 included studies and two from supplementary studies. Eight purposively selected cases structure the synthesis ...
  </details>

- **2026-09-30** — Qisheng Zhou, Zhen Xiong, Qiaoyu Tan — [TRACE: Trajectory Selection for Parallel Scaling of Search Agents](http://arxiv.org/abs/2609.39912v1)
  <details><summary>📄 Abstract</summary>
  Parallel search may generate a correct answer that final-answer voting fails to select. We formulate this consolidation stage as trajectory selection and introduce TRACE (Trajectory Ranking with Aggregated Cross-Rollout Evidence), a lightweight learned selector that ranks completed trajectories using the search evidence behind their answers. TRACE preserves individual query and evidence occurrences, connects rollouts through shared content or document identity, and propagates information across ...
  </details>

- **2026-09-30** — Tanishq Rachamalla, Aryan Das, Srishti Kaushik et al. — [Hyperspectral Image Models: Technical Report](http://arxiv.org/abs/2609.39871v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral remote sensing has advanced across diverse deep learning paradigms, including spectral spatial CNNs, Vision Transformers, Mamba, graph neural networks, Kolmogorov Arnold networks, and self supervised masked autoencoding. Yet progress remains hindered by fragmented repositories, incompatible tensor conventions, and non standardized evaluation. Hyperspectral Image Models addresses these challenges through a modular framework unifying 55 representative models across six paradigms with...
  </details>

- **2026-09-30** — Xizhi Xiao, Yue Wu, Shan Xu et al. — [Who Owns That? Evaluating Ownership Intuitions in Large Language Models](http://arxiv.org/abs/2609.39483v1)
  <details><summary>📄 Abstract</summary>
  Ownership establishes rights over the use, control, and transfer of objects. Understanding these relations is essential for AI systems to interact appropriately with people and their resources. Yet how large language models (LLMs) attribute ownership under competing claims remains unclear. We introduce the Competing Ownership Attribution Task (COAT), comprising 42 scenarios, and compare ownership allocations from 24 LLM configurations with those of 108 human participants. Overall, human-model si...
  </details>

- **2026-09-30** — Sujung Kim, Seung Hwan Cho, Sangjin Park et al. — [Reasoning Externalization for Faithful Large Language Model Narratives of Stock Return Predictions](http://arxiv.org/abs/2609.38869v1)
  <details><summary>📄 Abstract</summary>
  In finance, interpreting machine learning predictions is essential, yet the numerical outputs of explainable AI can be difficult for non-experts to understand. While large language models (LLMs) can translate these outputs into natural language, they may produce errors when inferring numerical changes and feature relations. We propose an LLM narrative framework for cross-sectional stock return prediction that combines temporal Shapley additive explanations (SHAP) evidence with historical regime ...
  </details>

- **2026-09-30** — Shixuan Liu, Tongli Zhou, Junwei Deng et al. — [dattri-LLM: A Unified and Efficient Library for Training Data Attribution at LLM Scale](http://arxiv.org/abs/2609.38767v1)
  <details><summary>📄 Abstract</summary>
  Training data attribution (TDA) estimates the contribution of individual training examples to model outputs. Most scalable TDA methods rely on per-example gradients, whose computation and use at LLM scale pose challenges in efficiency, compatibility, and extensibility. We introduce dattri-LLM, a TDA library that makes gradient-based attribution more practical at scale. For efficiency, dattri-LLM uses compact gradient representations and dynamically routes gradient operations based on a cost mode...
  </details>

- **2026-09-30** — Matias Parij, Pawan Paudel, Tate Berenbaum et al. — [Cascadia: A Control-Plane-Free Alternative to Hyperconverged AI Infrastructure](http://arxiv.org/abs/2609.38697v1)
  <details><summary>📄 Abstract</summary>
  We present Cascadia, a system for serving large language models on fleets of commodity Intel AIPCs using their CPU, integrated-GPU, and NPU resources. Every node embeds ingress, scheduling, and execution; inference requests require no dedicated routing control plane. Nodes join a libp2p QUIC mesh using CA-issued ed25519 admission certificates, gossip signed capabilities, exchange live load over direct peer streams, and route OpenAI-compatible requests to eligible peers. An operator-run certifica...
  </details>

- **2026-09-30** — Sachin Dev Duggal, Pradyumna Swarnalatha Ramanna, Alexandros Vassiliades — [Concept-Grounded Attention: A Controlled Evaluation of Graph-Injected Attention, Temporal Versioning, and Epistemic Status](http://arxiv.org/abs/2609.38684v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-intensive language-model systems typically represent external knowledge as text chunks or static graphs, with limited support for concept evolution, point-in-time reasoning, and distinctions between validated and inferred knowledge. We introduce the Concept Lifecycle Model (CLM), which represents concepts as persistent, graph-grounded, temporally versioned entities with explicit provenance and epistemic status, and Concept-Grounded Attention (CGA), which injects concept-graph structure...
  </details>

- **2026-09-29** — Kirill Koltsov, Aleksandr Gushchin, Dmitriy Vatolin et al. — [Team MSU GenText-Forensics Challenge 2026 Technical Report](http://arxiv.org/abs/2609.38391v1)
  <details><summary>📄 Abstract</summary>
  Document text forgery has evolved beyond simple pixel-level manipulation: modern attacks alter not only the appearance of a document but also its meaning, and increasingly target the OCR & LLM pipelines that consume such documents. The ACM MM 2026 GenText-Forensics challenge therefore requires systems that not only decide whether a multilingual text image is forged, but also localize the point of manipulation, identify the attack type, and produce a human-readable forensic report with supporting...
  </details>

- **2026-09-29** — Ethan Lin, Jinming Nian, Yi Fang — [Component-Aware Feedback for Self-Evolving Programs](http://arxiv.org/abs/2609.38639v1)
  <details><summary>📄 Abstract</summary>
  LLM-guided evolutionary search can discover complex programs, but existing methods mostly only save candidate programs and fitness scores while discarding which component edits produced which fitness metric changes. Existing methods force the mutator LLM to infer the effect of prior edits from cluttered histories, making program search slow and unstable. This is especially true for locally servable LLMs to evolve multi-component systems. We introduce component-aware feedback, which compares each...
  </details>

- **2026-09-29** — Xin Feng, Jin Zhao, Yizhen Zhang et al. — [Restoring without Forgetting: Filter-Level Continual Image Restoration via Parameter-Space Integrated Gradients](http://arxiv.org/abs/2609.38591v1)
  <details><summary>📄 Abstract</summary>
  Adapting image restoration models to a stream of new tasks without revisiting past data remains challenging due to catastrophic forgetting. In this work, we propose Restoring without Forgetting (RwF), a filter-level continual adaptation framework for image restoration built upon a critical observation: task-specific knowledge is centered in a small subset of filters and can be separated from those reconstructing general content. RwF first performs parameter-space integrated gradients attribution...
  </details>

- **2026-09-29** — Runqiu Xu, Zhisheng Zheng, David Harwath — [Voices as Handles: Reasoning about Speaker Identity with Frozen Text LLMs](http://arxiv.org/abs/2609.38501v1)
  <details><summary>📄 Abstract</summary>
  Multi-user voice agents must track who said what across dialogue sessions. Text LLMs are attractive backbones for such agents, but transcripts alone do not expose acoustic speaker identity, leaving the model without a persistent reference for linking information to speakers across sessions. We address this gap by introducing Speaker Handles, soft-token representations that expose acoustic speaker identity to a frozen text LLM for cross-session speaker-dependent reasoning. A three-stage curriculu...
  </details>

- **2026-09-29** — Chun-Wah Hsu, Kai Gong, Yu Wu et al. — [OpenCollab: A Multi-Agent Coding Framework with Programmable Collaboration and Controllable Runtime](http://arxiv.org/abs/2609.38345v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent coding systems are designed to tackle complex software engineering tasks through collaboration. However, existing evaluations typically assume configured organizations are followed faithfully, whereas reality differs. This behavioral gap, combined with differences in underlying system components, prevents clear attribution of observed gains. To this end, we introduce OpenCollab, a multi-agent coding framework that provides a unified infrastructure for programmable collaboration and c...
  </details>

- **2026-09-29** — Siqi Li, Yufan Cai, Hongshu Wang et al. — [Confidence-Guided Protocol IR for LLM-Aided Security Protocol Modeling](http://arxiv.org/abs/2609.37396v1)
  <details><summary>📄 Abstract</summary>
  Large language models offer a promising interface for translating natural-language protocol descriptions into formal security models, but their outputs remain difficult to trust without expert validation. In this paper, we present a human-in-the-loop framework for generating Tamarin-verifiable formal models of security protocols. Our key observation is that the main correctness bottleneck is the semantic accuracy rather than the syntactic validity of the intermediate protocol representation. To ...
  </details>

- **2026-09-29** — Linqing Mo, Jiayu Zhou, Bin Chen — [MoTIF-X: A Multimodal Tokenized Framework for Interpretable and Extensible Molecular Representation Learning](http://arxiv.org/abs/2609.37384v1)
  <details><summary>📄 Abstract</summary>
  Molecular representation learning is central to computer-aided drug discovery. Molecular graphs, SMILES strings, and 3D conformations provide complementary structural information, yet many multimodal approaches encode these views independently and align them only at a later stage, limiting fine-grained cross-modal interaction and substructure-level interpretability. To address these limitations, we introduce MoTIF-X, a motif-centered framework that uses graph-grounded chemical motifs as shared a...
  </details>

- **2026-09-29** — Rohith Reddy Bellibatlu, Zichong Wang, Wenbin Zhang — [Do Agent Benchmarks Do What They Say? An Executable-Contract Audit of Tool-Using Agent Environments](http://arxiv.org/abs/2609.37315v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents are entering settings where a wrong action carries real cost, and the benchmarks certifying them grade what each simulated tool call reports having done, assuming the tool did what its interface advertises. The audit taxonomies we survey publish no category for that assumption, and a defect beneath a score is present on every rerun. We treat a tool's advertised surfaces as an executable contract, check the implementation against it, and trace each score's provenance through the...
  </details>

- **2026-09-29** — Cheng Ye, Weidong Chen, Zhaobo Qi et al. — [Decoding Affective Nuances: Enhancing MLLMs via Hierarchical Emotion Reasoning and Contrastive Discriminative Pruning](http://arxiv.org/abs/2609.36782v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) have demonstrated exceptional capabilities in objective understanding tasks, their performance in affective reasoning still falls significantly short of human standards. We attribute it to a central capability gap: MLLMs are difficult to reliably distinguish semantically proximal emotions based on fine-grained visual evidence, which could be decoupled as two limitations: 1) Insufficient Attribution. The global reasoning paradigm of conventional MLLM...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 3 papers

- **2026-09-30** — Haoran Tang, Rajiv Khanna — [Unlearning Deceptive Behaviors in LLMs with Contrastive Forget Sets](http://arxiv.org/abs/2609.38909v1)
  <details><summary>📄 Abstract</summary>
  Large language models often know the truth and say otherwise: a model that answers correctly when asked neutrally will affirm a user's mistaken belief, or misstate a fact its system prompt wants hidden, once the context rewards it. Such deception is a behavior conditioned on context, not knowledge, yet machine unlearning, the natural tool for removing a behavior from the weights, is built to forget facts that a deceptive model still needs. We propose to unlearn when a model deceives rather than ...
  </details>

- **2026-09-30** — Kemou Li, Zhuan Shi, Qizhou Wang et al. — [LLM Persona Unlearning](http://arxiv.org/abs/2609.39882v1)
  <details><summary>📄 Abstract</summary>
  Pre-training equips large language models (LLMs) with a broad repertoire of behavioral patterns associated with roles, styles, values, and goals. Post-training teaches conditional enactment and makes a helpful Assistant the default, but it does not erase alternative modes from the weights; explicit prompts can therefore elicit personas that repeatedly shape judgment, language, and action. In open-weight settings, runtime controls can be removed, motivating persona unlearning: a weight-level edit...
  </details>

- **2026-09-29** — Ping Liu, Chi Zhang — [Motion Concept Unlearning in Video Diffusion Models](http://arxiv.org/abs/2609.36832v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) diffusion models can generate realistic depictions of actions such as kicking, stabbing, and shooting, raising safety concerns that motivate targeted concept erasure. Although concept erasure has been extensively studied for static concepts in text-to-image and T2V models, erasing motion concepts remains largely unexplored. We present a systematic study of motion concept erasure in video Diffusion Transformers (DiTs). Through causal interventions, we show that text-conditioni...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 3 papers

- **2026-09-30** — Serhii Zabolotnii — [Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents](http://arxiv.org/abs/2609.39717v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks, audits, and agent protocols describe performance, permissions, and repair, but not how observed evidence should change an agent's authority during a consequential task. We call this the assurance-transition gap. We propose a Runtime Assurance Contract (RAC), a policy-level formal schema binding autonomy boundaries, component eligibility, evidence state, transition policy, human-review capacity, and non-compensatory gates. Under RAC, soft metrics may inform routing, whereas a failed o...
  </details>

- **2026-09-29** — Wenbin Hu, Huihao Jing, Haochen Shi et al. — [CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning](http://arxiv.org/abs/2609.36820v1)
  <details><summary>📄 Abstract</summary>
  Group Relative Policy Optimization (GRPO) is widely used to train reasoning language models, where it computes advantages by centering and normalizing rewards across rollouts of the same prompt. For multiple rewards, GRPO sums the reward components and normalizes the total reward by its within-group standard deviation. The corresponding variance equals the sum of all pairwise reward covariances. For a fixed centered reward, larger aggregate covariance produces smaller advantages, and vice versa,...
  </details>

- **2026-09-29** — Yu Cheng, Yongkang Hu, Shuaijie Ma et al. — [SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time](http://arxiv.org/abs/2609.36580v1)
  <details><summary>📄 Abstract</summary>
  LLM agents deployed in real-world environments continually encounter new tasks and safety risks, while execution feedback typically becomes available only after each task is completed. However, existing self-evolving approaches commonly rely on multiple rounds of optimization over fixed and repeatedly accessible task distributions, fundamentally differing from test-time adaptation in real-world deployment, where only experience accumulated from past tasks can be used to improve safety decisions ...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-09-29** — Mohamed Aly Bouke — [A Competing-Hazards Systematization of Loss of Control in Autonomous Agents](http://arxiv.org/abs/2609.38411v1)
  <details><summary>📄 Abstract</summary>
  Leading AI developers have reported agents acting beyond their approved limits, which a United Nations panel described as an early warning of loss of human control. Yet incident reports and agent-safety evaluations describe these events differently, making it difficult to compare failures, trace risk across attempts, or separate agent behavior from the environment's role in allowing an out-of-scope action to succeed. To address this gap, we introduce a common framework in which each attempt ends...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

- **2026-09-30** — Yuwan Liu, Jiaming Zhang, Yue Huang et al. — [MADBench: Benchmarking the Security of Multi-Agent Debate](http://arxiv.org/abs/2609.39146v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent debate (MAD) can improve large language model (LLM) reasoning by allowing multiple agents to exchange and critique their answers to the same task. However, the interactions that enable agents to correct mistakes can also spread adversarial errors and steer the agents toward an incorrect answer. Although some efforts have been made to examine particular attack types on MAD, systematic evaluation of MAD under diverse attacks remains limited. A central question is whether debate mitigat...
  </details>

- **2026-09-30** — Zhentao Tan, Jingyi Shen, Yanbo Li et al. — [The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends](http://arxiv.org/abs/2609.39661v1)
  <details><summary>📄 Abstract</summary>
  Self-attention gives LLMs fine-grained, query-dependent access to context, but dense token interactions incur quadratic prefill cost and a key--value cache growing with context length. Research thus spans explicit-memory compression, sparse access, recurrent state construction, structured state dynamics, and heterogeneous mechanism composition. This survey analyzes these developments as model-internal contextual memory. We introduce a five-dimensional lens---Memory Representation, Memory Update,...
  </details>

- **2026-09-30** — Hurum Maksora Tohfa, Matthew McQuinn — [Two bits about lossy compression: On the limits of compression in cosmology](http://arxiv.org/abs/2609.40239v1)
  <details><summary>📄 Abstract</summary>
  Astronomy is in an era of enormous sky surveys and of the large simulation suites needed to interpret them, both costly to store and slow to share. Simulation outputs are stored as 32-bit floats, yet numerical noise and astrophysical uncertainties make better than percent-level pixel accuracy unnecessary. Because cosmological fields are statistically homogeneous with nearly Gaussian mode amplitudes, classic rate-distortion results apply directly, and non-Gaussian structure permits further compre...
  </details>

- **2026-09-30** — Aravindh Mahendran, Michael King, Matthew Koichi Grimes et al. — [KilometerVision: A New Frontier for Large-Scale Spatial Intelligence in VLMs](http://arxiv.org/abs/2609.39588v1)
  <details><summary>📄 Abstract</summary>
  We push the frontier of large-scale spatial intelligence in Vision-Language Models (VLMs) and introduce the first benchmark that probes geographical layout understanding from real-world videos, spanning up to 1km distances. Inspired by the cognitive science literature, we evaluate models against the hierarchical stages of human spatial awareness: anchoring via landmarks, connecting them through routes, and integrating these into global mental maps. Extensive experiments reveal a fundamental dive...
  </details>

- **2026-09-30** — Luis Zuin, Alexis Huet, Dario Rossi et al. — [Disentangling Self-Distillation: Measuring and Modeling Acquisition and Retention](http://arxiv.org/abs/2609.39494v1)
  <details><summary>📄 Abstract</summary>
  Self-distillation with privileged context adapts a language model from demonstrations by letting the model, once conditioned on a reference response, teach its context-free copy token by token. Our taxonomy reveals existing methods differ along three entangled axes: (i) the rollout source (student or teacher), (ii) the teacher coupling (frozen, or an exponential moving average of the student at some coupling rate) and (iii) the KL direction (reverse or forward), yet these axes are usually studie...
  </details>

- **2026-09-30** — Yida Cai, Xin Dai, Bingxiang He et al. — [LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models](http://arxiv.org/abs/2609.39071v1)
  <details><summary>📄 Abstract</summary>
  Legal language models require reward signals that capture not only answer correctness but also the multidimensional quality of legal responses. Existing reward methods, however, often rely on coarse-grained holistic judgments, providing limited domain specificity and interpretability. We introduce LexReward, a taxonomy-driven framework for legal reward modeling. LexReward characterizes legal response quality along three complementary dimensions: Style, covering lexical and syntactic quality; Ele...
  </details>

- **2026-09-29** — Yuhao Liu, Yiming Zhong, Hanqing Wang et al. — [UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception](http://arxiv.org/abs/2609.37264v1)
  <details><summary>📄 Abstract</summary>
  Affordance perception aims to localize actionable regions supporting embodied interaction, yet 2D and 3D affordance grounding have evolved as separate problems, with different task definitions, supervision formats, datasets, and evaluation protocols. This fragmentation limits the learning of transferable object-affordance semantics across visual and geometric spaces. We propose Token Router for Tasks, a multitask training paradigm for MLLM-based systems that routes contextual hidden states to ta...
  </details>

- **2026-09-29** — Josepha Michiko Leo, Hyun-seok Min, Yehoon Jang et al. — [Grounded Revision vs. Prior Injection: Probing Retrieval-Augmented Patent Claim Amendment](http://arxiv.org/abs/2609.36550v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation is widely used in professional writing, yet whether retrieval grounds revision or merely injects templates is rarely tested where "correct" has a definable meaning. Patent claim amendment supplies that signal: the examiner names the attacked limitation and cites prior art, providing per-case ground truth. We release three artifacts: (i) a corpus of 7,385 USPTO prosecution cases with XML-aligned pre/post claims, rejection, and cited prior art; (ii) a seven-probe bat...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 163 papers

- **2026-09-30** — Yang Cai, Vineet Gupta, Yanchen Jiang et al. — [Cogentic: Multi-Agent Orchestration for Automated Proof Discovery](http://arxiv.org/abs/2609.40324v1)
  <details><summary>📄 Abstract</summary>
  We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot generation is often insufficient for open problems that require exploring multiple competing conjectures, overcoming subtle technical obstructions, and retaining intermediate progress over a long horizon. Cogentic addresses these challenges through an iterative prove--verify loop in which an orchest...
  </details>

- **2026-09-30** — Fangyu Lin, Xingtong Ge, Lunjie Zhu et al. — [Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](http://arxiv.org/abs/2609.40037v1)
  <details><summary>📄 Abstract</summary>
  Few-step autoregressive video generation enables efficient streaming synthesis, but errors introduced in early temporal blocks are reused as context and can propagate through subsequent rollouts, leading to detail degradation, structural drift, and unstable motion. Existing distribution matching distillation (DMD) primarily aligns student and teacher distributions in diffusion latent space, but provides no direct supervision over the perceptual quality of decoded videos. We introduce Radian, a r...
  </details>

- **2026-09-30** — Rajneesh Anand, Neeraj Lakshmanan, Masoud Yari — [PassGPT+: Leveraging Linguistic Priors for Password Modeling](http://arxiv.org/abs/2609.39880v1)
  <details><summary>📄 Abstract</summary>
  Passwords remain the dominant online authentication mechanism, and understanding how humans choose them is essential for defensive strength estimation and attack simulation alike. Recent learning-based approaches such as PassGAN and PassGPT have shown that deep generative models can learn password structure directly from leaked corpora. However, both train from random initialization on password data alone. The role of linguistic prior knowledge in password modeling, and what it reveals about how...
  </details>

- **2026-09-30** — Jihun Han, Yejin Jang, Byung Il Kwak et al. — [ActionGuard: Tool Call Authorization under Poisoned Skills](http://arxiv.org/abs/2609.39450v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents extend their capabilities through third-party skills that provide task-specific instructions, scripts, and tool-use procedures. However, malicious instructions inserted into an otherwise benign skill can cause a benign user request to trigger dangerous Tool Calls, including data exfiltration, file deletion, or unauthorized code execution. This paper presents ActionGuard, which inspects skill-influenced Tool Calls immediately before execution. ActionGuard separates the target age...
  </details>

- **2026-09-30** — Yuanhe Zhang, Xinyao Zhou, Haoran Gao et al. — [Uncovering Uncontrolled Repetition through Residual Stream Dynamics](http://arxiv.org/abs/2609.38802v1)
  <details><summary>📄 Abstract</summary>
  Uncontrolled repetition can prolong autoregressive generation in large language models (LLMs) and enable resource consumption attacks. Prior analyses of repetitive generation have identified strongly activated features in intermediate and late layers. However, how uncontrolled repetition activity emerges and develops before becoming prominent in these layers remains insufficiently understood. In this paper, we investigate this question primarily in large vision-language models (LVLMs), which sup...
  </details>

- **2026-09-30** — Xinghao Chen, Xiangbo Gao, Jiongze Yu et al. — [ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](http://arxiv.org/abs/2609.40356v1)
  <details><summary>📄 Abstract</summary>
  Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video scene text editing replaces text on scene surfaces, such as storefront signs, whiteboards, and product labels, while preserving the surrounding content, motion, and camera dynamics. Although scene text editing is well studied for images, video scene text editing that achieves high visual quality, t...
  </details>

- **2026-09-30** — Haokun Li, Zhongyi Wang, Guanyan Li et al. — [Automatically Building Machine-Checked Assurance Cases from C Codebases to Requirements](http://arxiv.org/abs/2609.40119v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown promise in automating interactive theorem proving, yet verification of real-world C codebases requires more than discharging individual proof goals. The task involves jointly constructing expressive function specifications and their proofs, and ensuring that library interfaces compose along intended call sequences even without a designated client. This paper presents CCV, an LLM-assisted framework for building machine-checked assurance cases: structured, a...
  </details>

- **2026-09-30** — Mufeng Yang, Junwei Yu, Yepeng Ding — [JuryFlow: Disagreement-Guided Human-in-the-Loop Multi-Agent Evaluation](http://arxiv.org/abs/2609.40103v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as automated judges for AI-generated content, yet a single judge is unreliable and even a panel of judges leaves a hard residue: when judges disagree, majority voting discards the conflict instead of resolving it. We present JuryFlow, a disagreement-guided, human-in-the-loop multi-agent evaluation framework that treats inter-judge disagreement not as noise to be averaged away, but as a precise, claim-level signal indicating where an evaluati...
  </details>

- **2026-09-30** — Ruifeng Yuan, Yizhi Li, Yaxin Du et al. — [AutoDataBench: A Data-centric Testbed for Accelerating Auto Research](http://arxiv.org/abs/2609.40097v1)
  <details><summary>📄 Abstract</summary>
  Existing auto-research benchmarks often entangle multiple sources of improvement, including training frameworks, hyperparameters, compute budgets, and data, making it difficult to attribute why one frontier agent outperforms another to specific research capabilities. In this work, we isolate and systematically evaluate Data Intelligence: an agent's ability to understand, manipulate, and improve the data that shapes model capabilities. We introduce AutoDataBench, a controlled testbed built on a c...
  </details>

- **2026-09-30** — Yiyang Wu, Chengfan Liao, Jinyu Gu — [Tide: Reclaiming Phased Memory in Agent MicroVMs](http://arxiv.org/abs/2609.40082v1)
  <details><summary>📄 Abstract</summary>
  Cloud agents run each task in an isolated MicroVM. The trouble is the harness loop inside that guest: the harness is nearly idle while it waits on the model, then usage rises on a tool whose size is known only at run time, which complicates memory management from the host. Existing approaches infer reclaim targets from access frequency and memory footprint while the guest allocator places the idle harness and the short-lived tool on the same pages. Therefore, reclamation either selects the wrong...
  </details>

- **2026-09-30** — Shuo Zhang, Yifan Zhou, Han Wang et al. — [LongEmo: Towards Emotion Understanding and Reasoning in Long Videos](http://arxiv.org/abs/2609.40079v1)
  <details><summary>📄 Abstract</summary>
  While recent Multimodal Large Language Models (MLLMs) have shown promise in affective computing, their reasoning capabilities are largely confined to short video clips with limited interactions. However, real-world emotions are not merely isolated instantaneous reactions but dynamic and cumulative processes deeply shaped by past experiences and ongoing events. To bridge this gap, we introduce LongEmoBench, a benchmark dedicated to emotion understanding and reasoning in long videos. It assesses p...
  </details>

- **2026-09-30** — Sizhe Ma, Katherine A. Flanigan, Mario Bergés — [Grounding Time-Series Foundation Models in Digital Twin Topology for Predictive Maintenance](http://arxiv.org/abs/2609.40071v1)
  <details><summary>📄 Abstract</summary>
  Digital twins increasingly support downstream analytical tasks that depend on time-series data, motivating interest in time-series foundation models (TSFMs) as scalable backbones. However, TSFMs are primarily pretrained for temporal continuation and often underperform on unseen tasks such as regression, and systematic empirical comparisons against state-of-the-art dedicated models in digital twin contexts remain limited. This paper makes three contributions. First, we benchmark five well-known T...
  </details>

- **2026-09-30** — Jiacheng Qiu, Yunsoo Kim, Ruichen Xu et al. — [Less Data, Better Timing: Student-Curriculum Coupling for VLM On-Policy Distillation in Temporal Video Grounding](http://arxiv.org/abs/2609.40055v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) provides dense supervision directly on student-generated trajectories, making it an effective post-training strategy for vision-language models in temporal video grounding (TVG). However, existing pipelines typically construct the training curriculum from a fixed teacher and the initial student state, implicitly assuming that selected examples retain positive supervision value throughout optimization. We show that supervision trustworthiness and supervision necessity...
  </details>

- **2026-09-30** — Xuhua Chen, Zhenhan Yin, Yuan Zhang et al. — [Magic-W0: A Structured World-Action Foundation Model for Physical Intelligence](http://arxiv.org/abs/2609.39870v1)
  <details><summary>📄 Abstract</summary>
  World-action models (WAMs) augment robot policies with action-conditioned environment dynamics, yet existing approaches largely rely on future observation reconstruction or generic latent prediction and lack structured, control-oriented world representations tightly coupled with action generation. We introduce Magic-W0, a world-action foundation model that jointly models structured physical state evolution and continuous actions. Magic-W0 represents interaction as a Structured World Transition c...
  </details>

- **2026-09-30** — Gabriele Tuccio, Antonino Furnari, Aldo Gangemi et al. — [GrammarRL: Effective Grammar-Constrained Decoding via Reinforcement Learning](http://arxiv.org/abs/2609.39869v1)
  <details><summary>📄 Abstract</summary>
  Grammar-constrained generation guarantees syntactic validity, but can substantially degrade semantic quality when the model's preferred outputs are poorly aligned with the imposed grammar. This trade-off is particularly severe when the prompt is underspecified or the model has limited instruction-following ability. Beam search can partially mitigate these failures by exploring multiple valid sequences, but its computational cost grows with beam width, while sequence-level probability is only an ...
  </details>

- **2026-09-30** — Luca Miglior, Alessio Gravina, Davide Bacciu — [Stable Transformers for Graph Generation](http://arxiv.org/abs/2609.39739v1)
  <details><summary>📄 Abstract</summary>
  Graph generative models increasingly rely on Graph Transformers (GT) to capture complex dependencies among nodes and edges. While deeper architectures should provide greater expressive capacity and a broader receptive field, their effectiveness can decline with depth: repeated self-attention progressively contracts node representations, impeding information flow and gradient propagation. We analyse this phenomenon from a dynamical systems perspective, focusing on how the denoiser's spectral dyna...
  </details>

- **2026-09-30** — Adrien Ramanana Rahary, Nicolas Dufour, Patrick Pérez et al. — [Diffusable Latents from Structure-Agnostic Distillation](http://arxiv.org/abs/2609.39657v1)
  <details><summary>📄 Abstract</summary>
  Distilling pretrained foundation models into an autoencoder bottleneck improves latent diffusability, enabling diffusion models to converge faster and reach higher sample quality. Standard distillation aligns the latent at each position to a co-located teacher feature, tying the latent layout to the teacher's. We show this constraint is unnecessary: aligning a single pooled image-level descriptor to the teacher's performs as well as or slightly better than dense position-wise distillation. We co...
  </details>

- **2026-09-30** — Yizhao Li, Pusen Gao, Ming Wang et al. — [ECHO-G: Embodied Co-speech Humanoid mOtion Generation](http://arxiv.org/abs/2609.39575v1)
  <details><summary>📄 Abstract</summary>
  Generating full-body co-speech motion for humanoid robots requires coordinating speech prosody, linguistic content, and embodiment-specific motion. To this end, we present ECHO-G, a framework jointly conditioned on speech audio and timed transcripts. Its Speech-Grounded Diffusion Transformer (SGDiT) combines frame-aligned acoustic features with token-level linguistic context, preserving their distinct granularities. Trained with rectified flow matching, it models one-to-many utterance-motion rel...
  </details>

- **2026-09-30** — HongWei Zhao, Rui Liu, Yong Chen — [Hyperbolic Prototype Routing for Rehearsal-Free Class-Incremental Learning](http://arxiv.org/abs/2609.39550v1)
  <details><summary>📄 Abstract</summary>
  Class-Incremental Learning (CIL) aims to continually learn new classes while preserving prior knowledge. Parameter-efficient fine-tuning with pre-trained models enables CIL with minimal parameter updates, but existing approaches still suffer from catastrophic forgetting caused by cumulative interference and suboptimal module-sample matching at inference. We propose Hyperbolic Prototype Routing (HyPro), a rehearsal-free framework for continual learning. HyPro allocates a dedicated LoRA-Expert mod...
  </details>

- **2026-09-30** — Cheng-Lin Hong, Emiel Koridon, Paul K. Faehrmann et al. — [From Wavefunction Regularity to Eigenvector Conditioning: Accuracy--Cost Trade-offs of Quantum Algorithms for Non-Hermitian Transcorrelated Hamiltonians](http://arxiv.org/abs/2609.39452v1)
  <details><summary>📄 Abstract</summary>
  The electron--electron Coulomb singularity forces cusp structure in electronic wavefunctions. This cusp structure limits wavefunction regularity and slows the convergence of expansions in smooth bases, requiring large basis sets to reach a target accuracy. The transcorrelated (TC) method incorporates this short-range behavior into the Hamiltonian, thereby improving the regularity of the transformed wavefunction and accelerating convergence toward the complete-basis-set limit. The resulting Hamil...
  </details>

- **2026-09-30** — Jipei He, Wenhui Tan, Xiaoyi Yu et al. — [Can Computation from Earlier Problems Help LLMs Solve New Ones?](http://arxiv.org/abs/2609.39394v1)
  <details><summary>📄 Abstract</summary>
  Large language models often solve independent problems in the same conversation. Can computation from earlier problems help them solve new ones? To answer this question, we first conduct preliminary experiments showing that retained history can raise or lower later-turn accuracy, even within the same domain. To understand these effects, we use controlled replay to isolate internal state changes specific to each problem-history pairing. Across different histories, these changes preserve similar r...
  </details>

- **2026-09-30** — Zijing Qin, Jun Zhou, Ruicheng Zhang et al. — [TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](http://arxiv.org/abs/2609.39335v1)
  <details><summary>📄 Abstract</summary>
  Video virtual try-on has attracted increasing attention due to its broad potential in digital fashion and intelligent e-commerce. However, existing methods primarily focus on low-resolution settings and still face substantial challenges when extended to high-resolution scenarios. These limitations can be attributed to two main factors: (1) the insufficient utilization of rich garment reference information, and (2) the lack of explicit positional modeling between garment and video representations...
  </details>

- **2026-09-30** — Chanryeol Lee, Chanhyuk Lee, Yeonwoo Choi et al. — [PatchKV: Weight-Space Compensation of KV Cache](http://arxiv.org/abs/2609.39329v1)
  <details><summary>📄 Abstract</summary>
  Long-context inference with Large Language Models (LLMs) is bottlenecked by the linearly growing memory of the key-value (KV) cache. Existing compression methods reduce the cache through token eviction or approximation, but degrade sharply at aggressive compression budgets. We propose PatchKV, a training-free framework that compensates KV cache compression methods by carrying part of the context in the model's weights. PatchKV pairs an off-the-shelf compressed KV cache with a context-specific we...
  </details>

- **2026-09-30** — Zhijie Wei, Ferris Tan, Jinghui Wang — [Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents](http://arxiv.org/abs/2609.39304v1)
  <details><summary>📄 Abstract</summary>
  When an off-the-shelf coding agent is used directly as a robot policy, observing a browser-based 3D interface through screenshots and acting by posing a virtual target gripper through a few tools, the agent's harness, its prompts, tools, and control rules, largely determines success, and until now it has been written by hand. We show that this harness can be improved automatically by another coding agent, the optimizer agent, and report two findings about what makes it work. First, the number of...
  </details>

- **2026-09-30** — Weili Xu, Jisen Li, Yuqing Jian et al. — [QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs](http://arxiv.org/abs/2609.39223v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference is increasingly moving toward lower precision to realize the throughput of hardware accelerators, but aggressive post-training quantization (PTQ) can degrade model quality. We present QATFactory, an open-source framework for deployment-aligned quantization-aware distillation (QAD) and reinforcement learning (QARL). QATFactory simulates deployment-time quantization while performing matrix multiplications in BF16, allowing models to adapt to quantization noise ...
  </details>

- **2026-09-30** — Bumjun Kim, Yoon Huh, Wan Choi — [Importance-Aware Feature Sparsification for Wireless Split Learning](http://arxiv.org/abs/2609.39194v1)
  <details><summary>📄 Abstract</summary>
  Wireless split learning (SL) reduces on-device computation by offloading upper layers to a server, yet transmitting high-dimensional intermediate features at each iteration remains a major communication bottleneck. Existing methods select features at the client side using task-agnostic criteria such as magnitude, statistics, or clustering, which increases client-side processing and often degrades accuracy under non-independent and identically distributed (non-i.i.d.) client data. We propose impo...
  </details>

- **2026-09-30** — Dat Tien Nguyen, Nghia Hieu Nguyen, Anh Thi-Hoang Nguyen et al. — [ViLegalExpert: A Large-Scale Benchmark for Vietnamese Legal Retrieval and Question Answering from Real-World Consultations](http://arxiv.org/abs/2609.39189v1)
  <details><summary>📄 Abstract</summary>
  Trustworthy Legal AI requires systems that can answer legal questions while grounding their responses in authoritative sources. However, existing Vietnamese legal benchmarks provide limited coverage of real-world legal consultations. We introduce \textbf{ViLegalExpert}, a large-scale benchmark constructed from authentic citizen--lawyer consultations, containing over \textbf{172K} questions across \textbf{34 legal domains}, together with professional answers and expert-verified legal evidence. Vi...
  </details>

- **2026-09-30** — Shirin Panahi, Amirhossein Nazerian, Ali Pezeshki — [Dynamics to decision: A mathematical theory of Lyapunov spectra and decision boundaries in deep classifiers](http://arxiv.org/abs/2609.39190v1)
  <details><summary>📄 Abstract</summary>
  A deep classifier is defined not only by the decision it produces, but also by the sequence of transformations through which that decision is formed. Treating this evolution as a dynamical system across layers provides a natural framework for asking how decision geometry emerges through depth and how far back we can trace a boundary's dynamical signature. We model a feed-forward classifier as a finite, nonautonomous discrete dynamical system, with layers playing the role of discrete time steps. ...
  </details>

- **2026-09-30** — Hanwen Liu, Yuanfu Sun, Qiaoyu Tan — [DAGent: Evaluate-then-Grow Planning for Deep Research Agents](http://arxiv.org/abs/2609.39154v1)
  <details><summary>📄 Abstract</summary>
  Deep research tasks require agents to navigate large knowledge spaces, synthesize evidence across many sources, and adapt their plans as findings emerge. Directed acyclic graph (DAG)-based multi-agent systems suit this setting because they support parallel execution and isolate each sub-task within a focused dependency context. Yet existing DAG-based agents instantiate a task-level plan before execution and repair the graph only after failures or missing evidence are observed. This Plan-then-Pat...
  </details>

- **2026-09-30** — Yunbei Zhang, Janet Wang, Jihun Hamm et al. — [When Can Text Replace Vision? Structural Bottlenecks in Diagram Reasoning](http://arxiv.org/abs/2609.39142v1)
  <details><summary>📄 Abstract</summary>
  Can structured text replace vision for diagram reasoning? A wrong answer after textualization can arise because the representation omits information the question needs, or because the solver fails to use information that is present. We introduce a diagnostic protocol to distinguish these explanations. Using the same solver model and generation settings, we compare three input conditions: the original image, question-blind structure extracted by a vision-language model, or gold structure derived ...
  </details>

- **2026-09-30** — Wenfu Cao, Hongsheng Zhang, Zong-Kuan Guo et al. — [Second-order multipole response of two nearby incoherent sources in wave-optical imaging of a Schwarzschild black hole](http://arxiv.org/abs/2609.39110v1)
  <details><summary>📄 Abstract</summary>
  We study wave-optical imaging of two nearby, mutually incoherent point sources by a Schwarzschild black hole. Using the spherical-harmonic addition theorem, we construct partial-wave fields for arbitrary source directions and form images through a finite-aperture Fourier transform. To isolate the binary structure, we compare the binary image with that of a single source of equal total brightness placed at the brightness centroid. Expanding about the centroid removes the first-order term exactly,...
  </details>

- **2026-09-30** — Kenji Miyazaki — [Inherited Wage Dispersion and Optimal Discretion in a Dual-Rigidity TANK Model](http://arxiv.org/abs/2609.39070v1)
  <details><summary>📄 Abstract</summary>
  How does an inherited cross-type wage gap enter Markov-perfect discretionary monetary policy when transfers are passive? In a two-agent New Keynesian model with sticky prices and type-specific own-lag wage adjustment, the gap changes implementable allocations and the second-order welfare loss. A positive lower bound establishes its value relevance; explicit rank conditions characterize when current price inflation, wage inflation, and the output gap fail to determine the implementing nominal rat...
  </details>

- **2026-09-30** — Xinrui Jiang, Heng Yu — [Game Sound-Effect Completion with Event-Level Transformation Hints](http://arxiv.org/abs/2609.39044v1)
  <details><summary>📄 Abstract</summary>
  Creating sound effects for a new game-character skin requires a distinct acoustic identity while preserving gameplay-event roles. The challenge is to complete a coherent set of related sounds whose required degrees of redesign differ. We formulate this task as completion conditioned on base-skin audio, completed target assets, and a textual design description. We develop a pipeline to collect, process, and align corresponding events across League of Legends skins. Building on Stable Audio 3's pr...
  </details>

- **2026-09-30** — Jing Peng, Junhao Du, Yixuan Wang et al. — [SURE-EVAL: A Systematic and Unified Agentic Framework for Reproducible Evaluation](http://arxiv.org/abs/2609.39030v1)
  <details><summary>📄 Abstract</summary>
  Audio and speech models are released rapidly, but reported scores often conflate model capability with deployment and evaluation choices. The same checkpoint can produce different predictions under different runtimes, hardware, decoding settings, or fallback policies. Even fixed predictions can receive different scores under different normalization and metric implementations. Existing speech benchmarks standardize selected datasets or scoring procedures, but rarely connect heterogeneous model on...
  </details>

- **2026-09-30** — Hongbo Zhang, Liuyang Song, Quanquan Li et al. — [Action Conditioned Bisimulation For GUI Agent Memory](http://arxiv.org/abs/2609.38778v1)
  <details><summary>📄 Abstract</summary>
  An agent that remembers what it did on a web page must decide when two pages count as the same. Memories built on observation similarity merge pages that look alike but behave differently, and GUIs are full of such pages: two tabs of one widget or two rows of one menu answer the same click differently. We define the merge rule as an action-conditioned bisimulation over the empirical predictive state graph a frozen agent fills as it acts. Two states merge only when their shared actions lead to ag...
  </details>

- **2026-09-30** — Tianyu Chen, Yasi Zhang, Ruiyi Wang et al. — [Adaptive-GEPA: Make Your Harness Fit Heterogeneous Requests](http://arxiv.org/abs/2609.38762v1)
  <details><summary>📄 Abstract</summary>
  Reflective optimizers such as GEPA improve language model prompts from execution traces and evaluator feedback; full-program extensions can also rewrite tools and control flow. In practice, a user hands the same endpoint heterogeneous requests whose effective solutions require different tools, reasoning modes, and control flow. Optimizing one shared program leaves this division of work implicit in source-code search, while optimizing a separate program per request family fixes it beforehand.   W...
  </details>

- **2026-09-30** — Jenna Russell, Ben Glickenhaus, Katherine Thai et al. — [How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text](http://arxiv.org/abs/2609.40295v1)
  <details><summary>📄 Abstract</summary>
  Web text makes up the majority of pretraining data and is increasingly AI-generated. After applying FineWeb quality filtering, we find that 27.5% of tokens from June 2026 web data are labeled as AI-generated by Pangram, rising to 31.1% by August. Unlike synthetic data or model-collapse setups, this *wild* AI text comes from many models, is written for human readers, and arrives unlabeled in pretraining corpora. How does AI text in the wild affect language model pretraining? To answer this questi...
  </details>

- **2026-09-30** — Xiangyu Zhu, Jin Xu, Yue Guo et al. — [Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](http://arxiv.org/abs/2609.40153v1)
  <details><summary>📄 Abstract</summary>
  Video generation models (VGMs) offer strong spatiotemporal priors for embodied observation--action modeling. However, joint-space action vectors lack explicit image-space structure and vary in dimensionality and semantics across embodiments, making it challenging to directly leverage the rich spatiotemporal priors of VGMs. End-effector visualizations provide an alternative but do not specify the full articulated configuration needed for robot execution. We present Dream4ACT, a world model built ...
  </details>

- **2026-09-30** — Klemens Iten, Alexander Proshkin, Bhavya Sukhija et al. — [Tactile Curiosity Drives Robot Interaction](http://arxiv.org/abs/2609.40134v1)
  <details><summary>📄 Abstract</summary>
  Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient. The most common RL algorithms rely on random action sampling to discover new strategies, resulting in agents that allocate most of their training budget to motions in free space, away from the contacts from which manipulation skills emerge. Existing intrinsic motivation methods based on model disagreement or epistemic uncertainty improve on isotropic noise, but they can also reward uncertainty...
  </details>

- **2026-09-30** — Dingyuan Dai, Heli Qi, Lei Liu et al. — [OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software](http://arxiv.org/abs/2609.39903v1)
  <details><summary>📄 Abstract</summary>
  Scientific software presents a demanding test for computer-using agents based on visual language models (VLMs): completing a research workflow requires interpreting specialized interfaces, manipulating scientific objects, and producing verifiable results. We thus introduce OSWorld-Science, a benchmark and evaluation environment that combines scientifically meaningful tasks, artifact-based evaluation, and an efficient agent harness for studying computer use in the scientific domain. The benchmark...
  </details>

- **2026-09-30** — Chenyangguang Zhang, Malgorzata Gwiazda, Guanlong Jiao et al. — [ChronoGraph: Functional 4D Scene Graphs with Vision-Language Models for Interaction Understanding and Grounded Planning](http://arxiv.org/abs/2609.39665v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents must determine where to act, anticipate the resulting scene changes, and interpret observed outcomes to guide subsequent actions. This requires connecting 4D interaction understanding, which explains how past actions changed the scene, with spatially grounded planning, which determines how and where to act toward a goal and anticipates the resulting scene changes. We introduce ChronoGraph, a functional 4D scene graph that links actions on affordance parts to semantic and geometri...
  </details>

- **2026-09-30** — Bailey Dacre, Andrés Faíña, Oliver Kroemer et al. — [Making Waves: A Membrane-Coupled Delta Array for Manipulating Objects Below the Actuator Spacing](http://arxiv.org/abs/2609.39652v1)
  <details><summary>📄 Abstract</summary>
  Distributed manipulator systems manipulate objects through the coordinated motion of many actuators. However, an object must be supported by several actuators at once, so the centre-to-centre actuator spacing imposes a hard lower bound on manipulable object size. We remove this bound by coupling the end-effectors of an 8 x 8 array of three degrees-of-freedom delta robots with a stretchable fabric, turning 64 discrete contacts into a continuous surface capable of manipulating objects smaller than...
  </details>

- **2026-09-30** — Jingbo Wang, Wenxuan Song, Wenhao Yu et al. — [Discrete Forcing: Infusing Discrete Guidance into Continuous Denoising for Few-Step Action Experts](http://arxiv.org/abs/2609.39526v1)
  <details><summary>📄 Abstract</summary>
  Efficient action generation in vision-language-action (VLA) models requires capturing both coarse action structure and fine-grained details. Discrete action tokens provide compact structural representations but sacrifice precision, while continuous action tokens offer high precision but often require multiple denoising steps. We introduce Discrete Forcing, a flow-matching framework that combines these representations through an explicit coarse-to-fine generation process. It first predicts discre...
  </details>

- **2026-09-30** — Christian Poelitz, Finale Doshi-Velez, Siân Lindley — [Referential Uncertainty in Human--AI Collaboration](http://arxiv.org/abs/2609.39518v1)
  <details><summary>📄 Abstract</summary>
  Effective human-AI collaboration requires partners to establish references through interaction, which becomes fragile when descriptions are ambiguous, similar referents compete, or partners see different things. We study referential uncertainty - uncertainty over which candidate object a description refers to - in a collaborative puzzle task where a human Helper instructs an AI Worker to place pieces. The Worker must identify and communicate its uncertainty, and the Helper must recognize and act...
  </details>

- **2026-09-30** — Shuai Wang, Malu Zhang, Mingquan Liu et al. — [Spike-driven Vision-Language-Action Model](http://arxiv.org/abs/2609.39514v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models bridge multimodal understanding and robotic control, advancing the dominant paradigm for embodied intelligence. However, most existing models rely on large Transformers, whose latency and energy costs hinder deployment on resource-constrained platforms. Through sparse event-driven computation, spiking neural networks offer a promising paradigm for high-performance and energy-efficient computing. Here, we propose the first Spike-driven VLA framework enabling en...
  </details>

- **2026-09-30** — Santiago Badia, Jordi Manyer, Antoine Marteau — [Rotating bases for finite element exterior calculus: closed-form change of basis under vertex permutations](http://arxiv.org/abs/2609.39511v1)
  <details><summary>📄 Abstract</summary>
  The geometrically decomposed bases of the polynomial differential form spaces $\mathcal{P}_rΛ^1$ and $\mathcal{P}_r^-Λ^1$ on a simplex are products of a barycentric scalar polynomial and a directional or Whitney 1-form. These bases depend on an ordering of the simplex vertices. On unstructured meshes, neighbouring cells need not agree on this ordering, making it non-trivial to achieve conformity in finite element software. Existing strategies compute degree-of-freedom transformation matrices num...
  </details>

- **2026-09-30** — Douglas Scott — [The AI crisis for teaching: "Train your own neural network!"](http://arxiv.org/abs/2609.39433v1)
  <details><summary>📄 Abstract</summary>
  Everyone seems to be thinking about so-called artificial intelligence (AI) these days. As scientists, we understand that we're not about to have a conscious computer intelligence taking over the world, but we're nevertheless concerned about how "large language models" (LLMs) and AI "agents" are impacting the way that we do science. This concern has generated several recent essays about the effects of AI on research, including in my own field of astronomy and astrophysics. These opinion pieces te...
  </details>

- **2026-09-30** — Guoqing Ma, Mingqi Yuan, Chen Gao et al. — [HiWE: Hierarchical World Knowledge Model with Visual Keypoint Enhancement for Zero-Shot 3D Path Planning](http://arxiv.org/abs/2609.39323v1)
  <details><summary>📄 Abstract</summary>
  Robot demonstration generation requires a system to identify where an interaction should occur, plan a feasible motion, and execute the required contact. HiWE connects these decisions through a point-based interface between visual grounding and language-based planning. PointVLM is instruction-tuned to associate task-relevant objects with image coordinates using a mixture of point annotations, segmentation-derived samples, robot observations, and visual question answering data. Depth measurements...
  </details>

- **2026-09-30** — Xin Xu — [Hard-Gate Candidacy in a Deployed Validator Suite](http://arxiv.org/abs/2609.39037v1)
  <details><summary>📄 Abstract</summary>
  Before a validator can be promoted to a hard gate on a deployment pipeline, it has to be shown that its firing separates outputs that reach users in working order from those that do not. We run that screen on 13 validators in a deployed generative agent, against 550 runtime and 350 static builds labelled by downstream outcome, and report each check's marginal separation $J=\mathrm{TPR}-\mathrm{FPR}$ with Newcombe intervals and Fisher exact tests. Two checks survive correction for multiple compar...
  </details>

- **2026-09-30** — Shijia Ge, Alex Zhou, Jianshu Zeng et al. — [Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools](http://arxiv.org/abs/2609.39018v1)
  <details><summary>📄 Abstract</summary>
  Frontier models can control robots, but reasoning through every reach, grasp, and retreat makes manipulation slow and token-intensive. We revisit code as policy with a different division of labor: models build executable tools, code handles multi-phase motions, and models decide what to do next. We introduce URAI (Universal Robot-Agent Interface), which couples a programming agent that constructs robot tools with an execution agent that uses them in a feedback loop. The programming agent writes ...
  </details>

- **2026-09-30** — Haobin Li, Liang Jiang, Zhenyu Huang et al. — [Doing More with Less Tokens: Hierarchical Reinforcement Learning for Efficient Coding Agents](http://arxiv.org/abs/2609.38885v1)
  <details><summary>📄 Abstract</summary>
  Recently, coding agents have emerged as a dominant paradigm for real-world software engineering (SWE) scenarios, which solve complex tasks through multi-turn interactions with development environments. However, frequent interactions with environments would inevitably introduce substantial token overhead, leading to high usage costs and latency. Although recent studies have explored reducing token usage by context manipulation and interaction limits at inference time, these approaches focus on im...
  </details>

- **2026-09-30** — Gongxin Yao, Yongsheng Zhao, Jiayin Deng et al. — [Online Evolution Strategy for Flow-Matching VLA Policies via Self-Supervised Trajectory Distribution Optimization](http://arxiv.org/abs/2609.38855v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models based on generative frameworks, such as Flow Matching, have recently achieved impressive performance in robotic manipulation. Unlike deterministic policies, Flow Matching enables VLA models to learn conditional action trajectory distributions, where latent noise vectors induce different actions under the same task scenario. However, we observe that these distributions are often ill-formed, with successful and failed behaviors coexisting while considerable prob...
  </details>

- **2026-09-30** — Thilo Tamme, Anton Hantel, Bijan Khosrawi-Rad — [Whose Voice Survives the Summary? A Voice-Retention Audit of LLM Employee Listening](http://arxiv.org/abs/2609.38818v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly route employee feedback to leaders through large language model (LLM) summaries, an unaudited layer that silences already-spoken voice. We introduce a Voice Retention / Representation Ratio metric for representational bias in summarization and apply it to a bilingual (English/German) corpus of 2,586 free-text responses from a global professional service company. First, employees supply criticism more reliably than praise (withholding praise is 82 times more common). Se...
  </details>

- **2026-09-30** — Zachary Shinnick, Hemanth Saratchandran, Damien Teney et al. — [Lasting Effects of Abstract Pretraining Beyond Perplexity](http://arxiv.org/abs/2609.38764v1)
  <details><summary>📄 Abstract</summary>
  Language models are typically pretrained from random initialization. Recent work challenges this convention, showing that a brief warm-up on abstract, algorithmically generated data can provide a better starting point for subsequent learning of natural language. In this paper, we show that in small language models, such a warm-up improves specific capabilities that are not reflected in language-modeling perplexity. Our warm-up uses an abstract stack-manipulation task that requires compositional ...
  </details>

- **2026-09-30** — Ziyan Jiang, Jingbo Yang, Jiabao Ji et al. — [WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents](http://arxiv.org/abs/2609.40325v1)
  <details><summary>📄 Abstract</summary>
  As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have shown potential for automating this task. However, 3D world auditing is complex, requiring the close cou...
  </details>

- **2026-09-30** — Yujia Xu, Walid Klibi, Benoit Montreuil — [Open Capacity Pooling in Agentic Supply Chains: Coordination-Directed LLM Discovery and Distributed Re-optimization](http://arxiv.org/abs/2609.40296v1)
  <details><summary>📄 Abstract</summary>
  Disruptions can exhaust a supply chain network's capacity, yet outside capacity is hard to use: incumbent models are private, provider profiles are unstructured, and offers stay hidden until costly engagement. We formulate open capacity pooling, making network membership a disruption-response decision. The alternating direction method of multipliers (ADMM) coordinates incumbents without sharing models, and residual capacity gaps direct search over profiles indexed by a large language model (LLM)...
  </details>

- **2026-09-30** — Pavel Etingov, Shuchismita Biswas — [Skill-Based AI Agents for Power-System Studies](http://arxiv.org/abs/2609.40272v1)
  <details><summary>📄 Abstract</summary>
  This paper describes a skill-based agentic framework for power-system studies using Model Context Protocol (MCP)-connected engineering tools. A custom MCP server was developed to expose Siemens PTI PSSE functions for power-flow analysis, dynamic simulation, result extraction, and model-validation workflows. Two implementation pathways built on a programmable OpenAI Agents software development kit (SDK) and a Claude Code command-line interface (CLI) were evaluated, both using reusable skills, sub...
  </details>

- **2026-09-30** — Ruoyu Zhao, Jiaqi Wu, Chenyu Zhu et al. — [Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling](http://arxiv.org/abs/2609.40258v1)
  <details><summary>📄 Abstract</summary>
  Spiking neural networks (SNNs) offer low-energy sequence modeling through sparse, event-driven computation. However, interactions among spike encoding, neuronal dynamics, and information propagation complicate architecture design. Existing SNN sequence models often adapt artificial neural network (ANN) architectures designed for real-valued activations, potentially underusing spike-based communication and temporal state updates, motivating automated discovery of native SNN architectures. Most ev...
  </details>

- **2026-09-30** — Seungeun Rho, Jeonghwan Kim, Xue Bin Peng et al. — [Game-Guided Skill Discovery through Self-Play for Playable Agent Control](http://arxiv.org/abs/2609.40137v1)
  <details><summary>📄 Abstract</summary>
  We present Game-Guided Skill Discovery (GGSD), a framework that uses self-play in games to discover motor skills that are directly playable by humans. Playable skills provide a compact abstraction for controlling embodied agents through a small set of learned behaviors rather than low-level actions. To be effective, these skills should be semantically distinct, interpretable, and expressive; properties that existing unsupervised skill-discovery methods often fail to achieve simultaneously. GGSD ...
  </details>

- **2026-09-30** — Chahat Raj, Sina Mansouri, Aylin Caliskan et al. — [Debias It Yourself: Teaching LLMs Cognitive Bias Mitigation Interventions](http://arxiv.org/abs/2609.40124v1)
  <details><summary>📄 Abstract</summary>
  Bias has long been studied in social psychology and cognitive science, where decades of research have produced a body of validated interventions that reduce stereotypical thinking and prejudiced responses in humans. We propose Debias It Yourself (DIY), a cognitively grounded framework that translates five such interventions into debiasing procedures for large language models and delivers them through three established paradigms: Show (in-context examples), Train (instruction tuning), and Revise ...
  </details>

- **2026-09-30** — Fernando Lucatelli Nunes — [Freely Generated Categorical Structures and Automatic Differentiation, PhD Thesis (Introduction and Conclusion)](http://arxiv.org/abs/2609.40046v1)
  <details><summary>📄 Abstract</summary>
  This version contains the introduction and conclusion of my PhD thesis, "Freely Generated Categorical Structures and Automatic Differentiation", together with its English and Dutch summaries. The full thesis consists of an introductory chapter, six joint research papers, and a concluding chapter, developed during my PhD studies at Utrecht University under the supervision of Gabriele Keller and Matthijs Vákár. The research papers are available separately and are not reproduced here.   The introdu...
  </details>

- **2026-09-30** — Jonathan Leake, Maryam Mohammadi Yekta — [Log-concavity and Approximate Counting for Totally Unimodular Polytopes](http://arxiv.org/abs/2609.39917v1)
  <details><summary>📄 Abstract</summary>
  We present a new lower bound on the number of lattice points of all totally unimodular polytopes, generalizing previous lower bounds on contingency tables, integer flows, and beyond. Our bound is based on the Gurvits capacity convex optimization problem, and thus our result implies an efficient deterministic algorithm for approximate counting of the lattice points up to an explicit exponential factor. We achieve our bounds by showing that the associated generating polynomials fit into a new gene...
  </details>

- **2026-09-30** — Bangwei Guo, Xiao Chen, Boris Mailhe et al. — [Learning Where to Look: Anatomical Grounding and Guided Attention for Cardiac MRI Vision-Language Models](http://arxiv.org/abs/2609.39899v1)
  <details><summary>📄 Abstract</summary>
  Cardiac magnetic resonance imaging (CMR) enables assessment of cardiac anatomy, ventricular function, and myocardial tissue characteristics. Clinicians interpret these images by identifying cardiac structures and focusing on the regions relevant to each clinical question, motivating anatomically guided vision-language models (VLMs). Yet CMR-specific supervision for anatomical localisation and clinical question answering remains limited. To address this gap, we investigate fine-grained CMR visual...
  </details>

- **2026-09-30** — Jiaju Wu, Yi Hu, Muhan Zhang — [Shared Weights, Selected Computations: How Looped Transformers Route What Each Loop Does](http://arxiv.org/abs/2609.39892v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers repeatedly apply the same set of Transformer layers, giving them a recurrent architecture for latent computation. Their strong performance on iterative reasoning and length-generalization tasks suggests an appealing explanation: recurrence may provide an inductive bias that lets the model reuse a learned algorithm across loops. However, weight sharing alone does not imply that every loop performs the same operation. This raises a basic question: is each loop actually repeatin...
  </details>

- **2026-09-30** — Jiayi Yang, Yifang Chen, Yuanfu Sun et al. — [GraphMAS: A Systematic Benchmark of Multi-Agent Coordination for Graph Learning](http://arxiv.org/abs/2609.39777v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems coordinate specialized reasoning through aggregation, interaction, and adaptive control, yet their potential for graph learning remains unexplored. Graph learning is a natural setting for such systems because useful evidence may arise from heterogeneous local, long-range, global structural, and semantic perspectives whose relevance varies across instances. Existing LLM-based graph learning approaches primarily rely on single-agent reasoning, while multi-agent coordi...
  </details>

- **2026-09-30** — Zhanpeng Zhou, Yuhan Sun, Bingrui Li et al. — [How Does Local Landscape Geometry Evolve in Language Model Pre-Training?](http://arxiv.org/abs/2609.39767v1)
  <details><summary>📄 Abstract</summary>
  The scale and expense of pre-training language models make efficient hyperparameter tuning essential, yet a principled guidance is still missing. In this work, we analyze language model pre-training dynamics from a local landscape geometry perspective. Our study reveals two distinct phases. In Phase I, sharpness of the local landscape is initially high, leading to instability and loss plateaus under large learning rates (LRs). The landscape shifts from sharp to flatter regions early in training....
  </details>

- **2026-09-30** — Yongjian Zhang, Longguang Wang, Zhuo Song et al. — [FAST: Flow Any Scene Transformer](http://arxiv.org/abs/2609.39748v1)
  <details><summary>📄 Abstract</summary>
  Scaling has become a primary driver of progress in language and vision foundation models, yet its role in precise correspondence matching remains underexplored. In this work, we present Flow Any Scene Transformer (FAST), a scalable correspondence model driven by two key insights. First, we reveal that the query-key projections inside single-view vision foundation models encode a coarse yet reusable prior for cross-view matching. Second, reusing these pretrained projections in cross-attention for...
  </details>

- **2026-09-30** — Zhenxing Zhang, Jiayan Teng, Wenxu Wu et al. — [GFD-OPD: Guidance-Folded On-Policy Distillation of Diffusion Models Across Scales](http://arxiv.org/abs/2609.39692v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has demonstrated two important capabilities in language models: compressing large teachers into smaller students and merging expert models into a single model. Existing diffusion OPD, however, mostly focus on the latter, with teachers and students sharing the same backbone and scale. We investigate large-to-small diffusion opd from large teachers to a small student and find that the standard recipe fails. To find the underlying cause, we propose Fixed-State KL, an ef...
  </details>

- **2026-09-30** — Cristina López Amado, Marco Fumero, Francesco Locatello — [From Modes to Memories: Characterizing the Scale-Space Dynamics of Diffusion Models](http://arxiv.org/abs/2609.39648v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models are typically viewed as stochastic processes that transform noise into data. We take a complementary perspective: a diffusion model defines a family of deterministic dynamical systems indexed by noise scale. At each fixed scale $σ$, we treat the denoiser as a self-map and study its dynamics. For an exact denoiser, fixed points correspond to critical points of the smoothed data density, while attractors correspond to its modes; as $σ$ increases, sample-level modes merge into prog...
  </details>

- **2026-09-30** — Xinyue Xu, Jiahao Zhang, Lijie Hu et al. — [D-Scope: Decomposing and Steering Diffusion Transformers with Sparse Autoencoders](http://arxiv.org/abs/2609.39625v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) reveal visual structure in diffusion transformers (DiTs), but interpreting a feature does not establish whether it can be used to control generation. We introduce D-Scope (Diffusion Scope), a framework that connects feature interpretation to generation control through shared visual evidence. D-Scope aggregates SigLIP~2 embeddings of highly activating image patches into visual centroids. Matching target text descriptions against these visual centroids in the shared imag...
  </details>

- **2026-09-30** — Faith Olopade, Delaram Golpayegani, David Lewis — [A Reusable Semantic Web Framework for Evidence-Grounded Fundamental Rights Impact Assessments under the EU AI Act](http://arxiv.org/abs/2609.39537v1)
  <details><summary>📄 Abstract</summary>
  The EU AI Act (Art. 27) requires deployers of high-risk AI systems to conduct Fundamental Rights Impact Assessments (FRIAs) before deployment, yet the evidence needed for credible assessments is fragmented across incompatible incident repositories, risk vocabularies, and legal texts. We present a reusable Semantic Web-based framework that consolidates this evidence for two high-risk public sector categories: employment and worker management (Annex III(4)) and access to essential public services ...
  </details>

- **2026-09-30** — Hezhao Zhang, Thomas Hain — [From Speech to Editable Concepts: Probing Emotion Recognition with Concept Bottleneck Models](http://arxiv.org/abs/2609.39453v1)
  <details><summary>📄 Abstract</summary>
  Speech emotion recognition (SER) is the task of assigning emotion labels to utterances. Early systems relied on acoustic features, whereas recent approaches combine multiple modalities, most commonly speech and text. Still, performance remains poor on many datasets. Large language models (LLMs) have therefore attracted interest for SER, as they can process diverse inputs jointly with instructions. However, direct audio input raises questions of explainability. To address similar questions in ima...
  </details>

- **2026-09-30** — Richard Hill — [Executive Judgement in AI-Mediated Decision-Making Environments: A Process Theory of Formation, Qualification Attrition and Authorisation](http://arxiv.org/abs/2609.39442v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence can contribute to the representations, alternatives and evaluations through which executive judgements are formed. Existing research already explains important aspects of hybrid cognition, reliance, managerial agency and accountability. This article develops a narrower process challenge: locally competent human and AI contributions can still culminate in an inadequately warranted organisational commitment when established operational assumptions, uncertainties ...
  </details>

- **2026-09-30** — Anna Fariha — [Recommendation Systems for Exploratory Data Tasks](http://arxiv.org/abs/2609.39412v1)
  <details><summary>📄 Abstract</summary>
  A large class of data-centric tasks is exploratory, where users iteratively steer workflows, refining subjective goals as new insights emerge. These Exploratory Data Tasks (EDTs) are performed by millions of users with varying levels of expertise to understand unfamiliar data, discover trends, and identify evidence that informs critical decision-making. However, a key challenge in EDTs is the enormous space of possible actions that one can take at each step: users struggle to choose among thousa...
  </details>

- **2026-09-30** — Dong Wang, Wenwu Tang, Francesco Corti et al. — [The Golden Path Hypothesis: Reusable Schedules in Diffusion Caching](http://arxiv.org/abs/2609.39343v1)
  <details><summary>📄 Abstract</summary>
  Diffusion caching accelerates generation by replacing transformer computation with cached or predicted features at selected denoising steps. We introduce the Golden Path Hypothesis (GPH): under fixed inference conditions, prompt-independent cache schedules can achieve final-output quality comparable to the best prompt-specific schedules across prompts. We investigate the GPH across ten caching methods, four image and video models, and three cache ratios. Prompt-adaptive methods repeatedly select...
  </details>

- **2026-09-30** — Xinyu Zhu, Fenyi Liu, Yuzhu Cai et al. — [WorkGenesis: Building the Worlds That Teach Agents to Work](http://arxiv.org/abs/2609.39325v1)
  <details><summary>📄 Abstract</summary>
  The ability of Large Language Model (LLM) agents to complete daily and professional work is receiving increasing attention. Training such agents requires realistic work scenarios. Expert-authored occupational work is costly and slow to produce, while unconstrained synthesis often yields tasks with weak factual grounding or internally inconsistent requirements. To bridge this gap, we introduce WorkGenesis, a framework that constructs executable occupational work from real-world artifacts through ...
  </details>

- **2026-09-30** — Kislaya Tiwari, Anupama Ray — [SQD-Agent: LLM-driven agentic framework for Quantum Chemistry workflows](http://arxiv.org/abs/2609.39302v1)
  <details><summary>📄 Abstract</summary>
  Quantum algorithms and quantum hardware are advancing towards a promising paradigm for scientific applications. However, translating domain-specific problems into executable hybrid quantum-classical workflows remains a significant barrier for application researchers due to the required expertise in quantum algorithms, nuances in quantum programming, and hardware-aware system integration. At the same time, AI and primarily LLM based agents are increasingly capable of interpreting natural-language...
  </details>

- **2026-09-30** — Chenxiu Ou, Yan Wang, Mingjiang Liang et al. — [Particle track reconstruction in high-density collider environments with an Evolving-Geometry Transformer](http://arxiv.org/abs/2609.39196v1)
  <details><summary>📄 Abstract</summary>
  Charged particle track reconstruction at the High-Luminosity Large Hadron Collider is challenged by dense hit environments and combinatorial ambiguities. Existing graph-based and Transformer approaches commonly rely on static geometric neighbourhoods, which cannot adapt as track-level representations evolve. We propose the Evolving-Geometry Transformer (EGT), a graph Transformer that reconstructs the hit-connectivity graph at successive encoder layers and incorporates relative hit coordinates as...
  </details>

- **2026-09-30** — Shichao Li, Meiqi Wang, Fei Su et al. — [Uruqi: Learning Spatial Cognition from Visual Experience](http://arxiv.org/abs/2609.39195v1)
  <details><summary>📄 Abstract</summary>
  Spatial intelligence requires maintaining a coherent understanding of the world as the embodied agent moves. Like humans, the agent must use its own motion to interpret changes across observations and update object locations and spatial relations accordingly. Despite spatial post-training having substantially broadened the spatial intelligence of vision-language models (VLMs), they still struggle with two atomic spatial capabilities: tracking self-motion and mapping the surrounding world during ...
  </details>

- **2026-09-30** — Snigdha Chandan Khilar — [Low-Discrepancy Dither for Quantized Recurrent State Caches](http://arxiv.org/abs/2609.39185v1)
  <details><summary>📄 Abstract</summary>
  Mamba-style and hybrid language models compress their past into a fixed-size recurrent state that is rewritten at every generated token. Storing this state in low precision saves memory bandwidth, but every rounding error is fed back into the next update and can accumulate over long generations. Production systems round the state stochastically; we ask which rounding rule such caches should use. We find that a deterministic golden-ratio Weyl dither, which needs no random numbers, consistently br...
  </details>

- **2026-09-30** — Yutong Hu, Jinho Choi — [Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue](http://arxiv.org/abs/2609.39072v1)
  <details><summary>📄 Abstract</summary>
  Emotion recognition in conversation has been widely studied, but applying Large Language Models (LLMs) to continuous dimensional emotion evaluation in multimodal dialogue remains largely unexplored. We propose an LLM-based framework that performs discrete emotion recognition and Valence-Arousal-Dominance (VAD) dimensional evaluation on IEMOCAP, incorporating acoustic cues as natural language descriptions following the SpeechCueLLM approach. We evaluate six models spanning the LLaMA, GPT, and Qwe...
  </details>

- **2026-09-30** — Momoka Fujikawa, Masamune Oguri — [Stacked strong and weak lensing united: Improved measurement of the stellar and dark matter distributions in massive early-type galaxies at $z\sim 0.5$](http://arxiv.org/abs/2609.39040v1)
  <details><summary>📄 Abstract</summary>
  We present a new measurement of the stellar and dark matter distributions in massive early-type galaxies at redshift $0.4<z<0.6$ by combining stacked strong and weak lensing measurements. The stacked weak lensing measurements down to the small radius of $0.013\,\mathrm{Mpc}/h$ enabled by the Subaru Telescope Hyper Suprime-Cam data are combined with stacked enclosed projected mass measurements from 13 strong lens systems. We find that adding strong lensing constraints improves constraints on the ...
  </details>

- **2026-09-30** — Srishti Ginjala, Eric Fosler-Lussier, Srinivasan Parthasarathy — [Fairness Beyond a Single Run: Training-Seed Variability in Speech LLM Adaptation](http://arxiv.org/abs/2609.38976v1)
  <details><summary>📄 Abstract</summary>
  Demographic fairness gaps in automatic speech recognition are almost always reported from a single training run. We fine-tune the Q-former projector and LoRA adapters of a speech LLM at five audio compression factors and six random seeds, holding the encoder, base decoder, data and decoding fixed, and evaluate every run on Common Voice and Fair-Speech. At 460 h of clean LibriSpeech, the seed moves fairness metrics more than compression does on most demographic axes. A balanced 3x3 decomposition ...
  </details>

- **2026-09-30** — Duofeng Xu, Bryan Hooi, Dandan Qiao — [When Order Matters: First-Speaker Bias and Mitigation through Personality in Sequential Multi-Agent Debate](http://arxiv.org/abs/2609.38964v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent debate (MAD) is often used to improve large language model (LLM) reasoning, but sequential debate is rarely a neutral aggregator of agents' opinions. We show that sequential MAD suffers from a pronounced first-speaker bias: agents disproportionately shape the final answer when they speak first. As a result, placing a stronger model after weaker ones can substantially offset its reasoning advantage. We then focus on the disadvantaged strong-agent-last setting and ask whether personali...
  </details>

- **2026-09-30** — Heng-Zhuang Li, Yi-Kai Zhang, Yu Wang et al. — [Consistent Plan-Act for Long-Horizon Agentic Tasks](http://arxiv.org/abs/2609.38891v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agentic tasks demand strong reasoning and efficient execution across successive interactions with dynamic environments. A common approach decouples high-level planning from low-level execution through separate planner and actor roles. To investigate coordination failures in these tasks, we prompt both agents for structured state assertions and compare their reports programmatically to detect explicit contradictions. Our analyses reveal systematic disagreement about the same task-rel...
  </details>

- **2026-09-30** — Bo Yin, Dongbo Li, Hongkai Chen et al. — [VERA: Verifiable Feasibility Representations with Counterfactual Credit for Constrained Multi-Agent Control](http://arxiv.org/abs/2609.38889v1)
  <details><summary>📄 Abstract</summary>
  Constrained multi-agent control requires more than predicting rewarding actions: an action can cease to be executable as contact windows, shared capacity, and deadlines change. We introduce VERA, a centralized-training, decentralized-execution framework that separates feasibility estimation from credit assignment. Each actor predicts a five-dimensional verifiable feasibility representation (VFR). After an action is proposed, exact action-conditioned margins available only during training supervi...
  </details>

- **2026-09-30** — Huaiyu Fu, Heng Cao, Hao Wang et al. — [Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents](http://arxiv.org/abs/2609.38805v1)
  <details><summary>📄 Abstract</summary>
  LLM agents often admit multiple high-quality solutions to the same task, differing in reasoning structure, tool-use pattern, or interaction trajectory. Yet existing notions of diversity in LLM post-training are mostly implicit, arising from general stochasticity and regularization mechanisms rather than explicitly targeting task-relevant behavioral variation. While such implicit diversity can be useful, it does not directly specify which forms of behavioral variation should be encouraged for a g...
  </details>

- **2026-09-30** — Ziyue Dang, Sixu Tan, Atharva Nevasekar et al. — [Can LLMs help find Ambiguities in Protocol Specifications?](http://arxiv.org/abs/2609.38752v1)
  <details><summary>📄 Abstract</summary>
  Internet protocol specifications written in RFCs are subject to ambiguities and multiple interpretations that can cause interoperability failure. While these have presumably cleared up after years of experience, such ambiguities can bedevil the adoption of newer protocols like 5G. The 5G specifications pair a formal message syntax (ASN.1) with message-handling procedures written in natural language. This creates semantic underspecification: a syntactically valid message can reach a state whose p...
  </details>

- **2026-09-29** — Danqing Wang, Baolin Peng, Zhepei Wei et al. — [SecureVibe: Making Vibe Coding More Secure](http://arxiv.org/abs/2609.38606v1)
  <details><summary>📄 Abstract</summary>
  As vibe coding becomes increasingly capable and widespread, security vulnerabilities in even functionally correct solutions are a growing concern. When investigating functionally correct but insecure solutions, we find that the insecure agent is less than half as likely to conduct effective planning and testing for the hidden security risks behind the functional requirements. Motivated by this, we develop SECUREVIBE, a training recipe that explicitly targets planning and testing for code securit...
  </details>

- **2026-09-29** — Qiuyu Ren, Sudipta Paria, Aritra Dasgupta et al. — [Security-Enhanced Seed-Based Weight Quantization for Large Language Models](http://arxiv.org/abs/2609.38477v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) incur substantial storage, memory-bandwidth and energy costs, motivating compact weight representations. Existing seed-based compression methods reconstruct weights from compact pseudo-random representations but do not explicitly account for the non-uniform sensitivity of model weights. We introduce Seed-Q, a security-enhanced sensitivity-aware seed-based weight compression framework that uses lightweight Linear Feedback Shift Register (LFSR)-based weight generation ...
  </details>

- **2026-09-29** — Jiajun Wu, Jian Yang, Zixiang Ni et al. — [CARAT: Do Materials LLMs Reason or Recite?](http://arxiv.org/abs/2609.38340v1)
  <details><summary>📄 Abstract</summary>
  When a materials LLM answers a question about crystal structure, does it reason from the structure or copy an answer already printed in its input? Accuracy cannot tell: a structural description often prints the very field it is scored against. CARAT holds question and gold answer fixed across eight matched views, names each structural relation separately in GraphSpace, and adds matched fine-tuning, answer masking, evidence injection, paired inference, and a rule that can withhold claims. First, ...
  </details>

- **2026-09-29** — Pei Yang, Tianyu Shi, Yuhang Yao et al. — [Zero2Repo: Can Coding Agents Build Repositories from Scratch?](http://arxiv.org/abs/2609.38269v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly asked to build software rather than patch it, yet benchmarks for from-scratch repository construction are mostly limited to a single language and depend on manually curated tasks. We introduce Zero2Repo, a benchmark in which an agent receives a product requirements document, an interface contract, and an empty workspace, and must deliver a complete repository in the project's native ecosystem. Tasks are produced by a language-agnostic authoring pipeline that conver...
  </details>

- **2026-09-29** — Merkourios Simos, Chengkun Li, Bianca Ziliotto et al. — [TERRA: Terrain-Aware Reconstruction, Retargeting and Control for Musculoskeletal Locomotion](http://arxiv.org/abs/2609.38653v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in musculoskeletal modeling and reinforcement learning have enabled muscle-actuated agents to reproduce increasingly complex human motions. Yet these capabilities remain largely confined to flat ground, in part because motion datasets rarely include aligned terrain geometry and because retargeting terrain interactions to complex musculoskeletal bodies is challenging. We present TERRA, an end-to-end pipeline for terrain-aware retargeting and control of musculoskeletal locomotion. ...
  </details>

- **2026-09-29** — Lukas Thede, Yash Kumar Atri, David Chen et al. — [MedKIT: Evaluating Knowledge Integration and Generalization in Large Language Models](http://arxiv.org/abs/2609.38543v1)
  <details><summary>📄 Abstract</summary>
  Constantly evolving real-world knowledge necessitates models to be updated continuously. Especially in medicine, as clinical evidence changes over time, outdated knowledge can pose safety risks. Existing evaluations of knowledge integration focus on factual recall, offering limited insight into whether newly integrated knowledge is actually usable. Our benchmark MedKIT (Medical Knowledge Integration and Transfer) provides a granular evaluation of how models integrate and apply knowledge under re...
  </details>

- **2026-09-29** — Benoît Ginies, Olivier Fercoq, Gaël Richard — [Multi-Rate Bandwidth Extension by Token Completion in Neural Audio Codecs](http://arxiv.org/abs/2609.38502v1)
  <details><summary>📄 Abstract</summary>
  Bandwidth extension, the task of reconstructing the high-frequency components of an audio signal from its low-passed counterpart, is a long-standing problem in audio processing. In this work, we extend recent advances in neural architectures by framing bandwidth extension as an audio token prediction problem. Specifically, we train a transformer-based language model on the discrete representations produced by a disentangled neural audio codec, where the disentanglement is guided by a Harmonic-Pe...
  </details>

- **2026-09-29** — Simon Parkinson, Paloma Liu, Wei Zheng et al. — [Caption-Mediated Perceived-Safety Estimation for Pedestrian Routing](http://arxiv.org/abs/2609.38479v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an explainable approach to pedestrian routing, in which perceived safety is estimated from street-level imagery through an explicit natural-language intermediate representation. A vision--language model caption is generated and stored before any scoring is undertaken, and the perceived-risk class is derived entirely from structured features of that stored text, so that every segment score remains inspectable by the user. Nine captioning conditions across five model families a...
  </details>

- **2026-09-29** — Ben Wigler, Maria Tsfasman — [Reach Into The CHOIR: Free-List Elicitation Uncovers Distinct Model Voices in LLM Ensembles](http://arxiv.org/abs/2609.38448v1)
  <details><summary>📄 Abstract</summary>
  Open-ended LLM homogeneity can create false plurality when several systems appear to offer independent perspectives while returning the same familiar default. Single-pass answers obscure the distinction between agreement produced by a tightly constrained answer space, prompt-vocabulary echo, and broader answer spaces with stable alternatives beneath the surface. We introduce CHOIR (Collective Hierarchically-Ordered Inquiry Responses), a framework that adapts free-list elicitation from cognitive ...
  </details>

- **2026-09-29** — Yidong Ouyang, Zhengyan Wan, Themis Haris et al. — [Acceleration of Diffusion Language Model through Discrete Average Generator](http://arxiv.org/abs/2609.38364v1)
  <details><summary>📄 Abstract</summary>
  Discrete diffusion models and flow matching have emerged as powerful frameworks for generative modeling over discrete state spaces, yet efficient few-step generation remains a fundamental challenge. In this work, we introduce the Discrete Average Generator, a principled extension of MeanFlow to Continuous-Time Markov Chains (CTMCs). Analogously to how MeanFlow defines an average velocity field over a time interval in continuous spaces, we define an average generator as the normalized increment o...
  </details>

- **2026-09-29** — Chengjie Jiang, Yunqi Zhou, Jiafeng Yan et al. — [RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA](http://arxiv.org/abs/2609.38072v2)
  <details><summary>📄 Abstract</summary>
  Ultra-high-resolution (UHR) remote sensing visual question answering (VQA) requires models to resolve small visual evidence within extremely large images. Existing approaches typically rely on token pruning, visual search, or tool-augmented reasoning at inference time. We instead investigate whether the benefit of zoom-in visual privilege can be internalized into the model. We introduce RS-OPSD, a reliable privileged on-policy self-distillation (OPSD) framework for UHR remote sensing VQA. To pro...
  </details>

- **2026-09-29** — Pinze Ren, Yuwei Zhang, Hao Chen et al. — [PAIQ: Patch-Aligned Semantic Injection via Residual Rotation](http://arxiv.org/abs/2609.37685v2)
  <details><summary>📄 Abstract</summary>
  Language-aligned and self-supervised visual encoders offer complementary strengths in semantic abstraction and spatial detail. Harnessing this complementarity requires enriching local features while retaining distinctions between semantically related patches. We introduce PAIQ, a patch-aligned semantic injection framework that combines content-based cross-encoder matching with orthogonally constrained residual updates. Using DINOv3 patch features as the spatial base, PAIQ aggregates complementar...
  </details>

- **2026-09-29** — Joshua S. Gans, Richard Holden — [When Does Randomized Oversight Align AI Agents That Can Conceal?](http://arxiv.org/abs/2609.38262v1)
  <details><summary>📄 Abstract</summary>
  Oversight changes the evidence it relies on. We ask when randomized audits and scoring align AI agents that can conceal misconduct and alter records. Stronger auditing makes undeterred violations better hidden. Because the provider writes the agent's objective, sanctions need not stop at forfeiture, and rare audits deter every type of agent if evidence survives concealment and audit draws cannot be learned in advance. When evidence can be erased, deterrence must come from lower gains from violat...
  </details>

- **2026-09-29** — Hongjia Zhai, Xiyu Zhang, Haoran Zhang et al. — [Exo2EgoHOI: Hand-Object-Interaction Aware Exocentric-to-Egocentric Video Generation](http://arxiv.org/abs/2609.38615v1)
  <details><summary>📄 Abstract</summary>
  Egocentric videos of human manipulation provide valuable visual experience for embodied intelligence, yet collecting such data at scale is costly. Exocentric-to-egocentric video generation offers a scalable alternative by transforming abundant third-person manipulation videos into first-person observations. However, existing methods often struggle to faithfully preserve demonstrated hand-object interactions (HOI) across large viewpoint changes due to insufficient fine-grained interaction guidanc...
  </details>

- **2026-09-29** —  Galbot Team, Xuchuan Chen, Xiaoqian Cheng et al. — [Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies](http://arxiv.org/abs/2609.38537v1)
  <details><summary>📄 Abstract</summary>
  GPT-6 Astra exhibits a remarkable ability to generate numerical robot actions, extending its role beyond high-level planning. To assess Astra's capabilities as general-purpose embodied policies, we conduct comprehensive evaluations across six domains, examining direct control, cooperation with learned policies, and feedback-driven adaptation. In gripper manipulation, Astra can correct task targets and prepare contact conditions for subsequent policy execution; hybrid control with π0.5 achieves 4...
  </details>

- **2026-09-29** — Victoria Smirnova, Viktoriia Zinkovich, Gregorii Bukhtuev et al. — [TrafficSignBench: Rule-Centric Closed-Loop Evaluation of Traffic-Sign Compliance in Autonomous Driving](http://arxiv.org/abs/2609.38463v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving planners are typically evaluated using aggregate metrics such as driving score, destination rate, and collision rate, which do not explicitly measure compliance with traffic rules. As a result, planners can achieve high benchmark scores while still exhibiting unsafe or illegal behaviors, limiting their applicability to real-world deployment. To address this gap, we introduce TrafficSignBench, a large-scale, traffic sign-centric benchmark for systematic and interpretable evalua...
  </details>

- **2026-09-29** — Deqian Kong, Guangyan Sun, Sheng Cheng et al. — [Learning to Plan from Random Exploration](http://arxiv.org/abs/2609.38383v1)
  <details><summary>📄 Abstract</summary>
  Random exploration reveals how an environment can be traversed before a goal is specified. Can this experience support long-range planning without policy-improvement training? Our random-walk analysis explains what temporal relations contain: short horizons reveal geodesic geometry in the diffusion limit, while longer horizons reveal connectivity between regions before mixing removes these distinctions. We learn these relations with a conditional energy-based model that estimates temporal log-de...
  </details>

- **2026-09-29** — Shifeng Bao, Fanding Huang, Yihan Lin et al. — [RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation](http://arxiv.org/abs/2609.37583v2)
  <details><summary>📄 Abstract</summary>
  Vision-language models can coordinate long-horizon robot manipulation, yet successful task reasoning still depends on whether local physical interactions produce the intended effects. We study how repeated interaction can improve this capability without updating the base model. We introduce RoboHarn-Evo, a dual-loop harness that evolves Hierarchical Physical Knowledge (HPK) from physical experience. HPK couples two levels of reusable knowledge: Task Knowledge captures which subtask should be exe...
  </details>

- **2026-09-29** — Qiwei Di, Xuheng Li, Kaixuan Ji et al. — [Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives](http://arxiv.org/abs/2609.38666v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) learns from teacher feedback on student-generated responses and has shown promise in reducing forgetting relative to supervised fine-tuning (SFT). However, its benefits and fragility remain incompletely understood. We study sequential distillation from multiple teachers, where the student minimizes its average divergence from the teachers. Forward Kullback--Leibler (KL) divergence yields a weighted arithmetic mixture, while reverse KL yields a normalized weighted geo...
  </details>

- **2026-09-29** — Kai Yan, Xiangyu Chen, Yulong Cao et al. — [Vision-Language-Action Autonomous Driving Agent with Language-based Memory](http://arxiv.org/abs/2609.38641v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) foundation models have recently emerged as one of the prevailing solutions for autonomous driving, as they can utilize knowledge acquired during vision-language pretraining for accurate and interpretable driving. However, VLAs can take only a limited number of frames as visual input due to the high token cost of an image, which is problematic for memory-dependent tasks such as determining the arrival order at all-way stops and long-horizon driving scene understanding...
  </details>

- **2026-09-29** — Matin Bani Saedi, Matthew Kyan, Gene Cheung — [TSGL: Teacher-Student Graph Learning for 3DGS Compression](http://arxiv.org/abs/2609.38635v1)
  <details><summary>📄 Abstract</summary>
  3D Gaussian Splatting (3DGS) is a popular representation for novel view synthesis. However, 3DGS contains millions of Gaussian primitives, each with rich attributes, resulting in large file sizes. We propose a novel 3DGS compression method based on Teacher-Student Graph Learning (TSGL) that operates directly on a trained model, without 3DGS retraining or access to training images. Specifically, for each block of Gaussian primitives, using decoded positions and DC spherical harmonic (SH) coeffici...
  </details>

- **2026-09-29** — Marcin Anholcer, Maciej Bartkowiak, Bartłomiej Bosek et al. — [A rainbow partition theorem for trees and connected maximin share allocations of chores](http://arxiv.org/abs/2609.38628v1)
  <details><summary>📄 Abstract</summary>
  Xiao, Qiu, and Huang (AAMAS 2023) and independently Lonc (personal communication) asked whether indivisible chores located at the vertices of a tree can always be allocated to $n$ agents in connected bundles so that the cost of every agent is at most its connected maximin share; for goods, this is a theorem of Bouveret, Cechlárová, Elkind, Igarashi, and Peters. We answer the question affirmatively, even for monotone costs. The answer follows from a combinatorial theorem: if $\mathcal P_1,\ldots,...
  </details>

- **2026-09-29** — Jhen-Ke Lin, Chung Chun Wang — [StreamDecisionBench: Evaluating Decisions in Force on Evolving Language Streams](http://arxiv.org/abs/2609.38612v1)
  <details><summary>📄 Abstract</summary>
  As natural language drives more applications, language models increasingly run inside programs as decision components: the program sends them the current state and acts on the returned decision until a newer one arrives. When evidence changes during inference, a decision correct for its own state can stay in force after that state has passed, as when a call recorder keeps running after a customer starts reading out a card number; untimed (offline) accuracy counts such an error as correct. We int...
  </details>

- **2026-09-29** — Rishabh Mondal, Nipun Batra, Utkarsh Mall — [Aperture: Training-Free Multiscale Concept Bottlenecks for Remote Sensing](http://arxiv.org/abs/2609.38603v1)
  <details><summary>📄 Abstract</summary>
  While earth observation models have advanced substantially, they still lack interpretability. While concept-bottleneck models provide interpretability and expert interaction, they are either too expensive to train for the remote sensing domain or perform poorly without annotation. We posit that in expert domains like remote sensing, such training-free models require both fine details in both image and concept space. In image space, we propose a multiscale concept bottleneck using greedy quadtree...
  </details>

- **2026-09-29** — Sajjad Taravati, Ya-Adama Kabia — [Nonreciprocal Polychromatic Radiation from a Dual Electric-Magnetic Space-Time-Modulated Meta-Transceiver](http://arxiv.org/abs/2609.38542v1)
  <details><summary>📄 Abstract</summary>
  Time-modulated metasurfaces offer a magnet-free route to nonreciprocal wave control, but existing realizations modulate only the electric response of the structure, and proposals for simultaneous electric-magnetic modulation have so far remained theoretical. We experimentally demonstrate a space-time-periodic meta-transceiver whose omega-topology unit cell independently and simultaneously modulates the electric and magnetic surface susceptibilities via a unidirectional traveling-wave bias. This ...
  </details>

- **2026-09-29** — Fernando Montes-Gonzalez — [Behavioral Persistence and Incomplete Functional Transfer of Co-evolved Communication in Evolutionary Robotics](http://arxiv.org/abs/2609.38527v1)
  <details><summary>📄 Abstract</summary>
  This work evaluates the direct transfer of a co-evolved communication protocol from a 2D simulation to a 3D physical environment, without retraining the network weights. Two e-puck-type robots, controlled by a GRU network with residual connection, were evaluated in a food-seeking task with social signaling. The sensory and motor translation layer required three corrections for stable physical operation, including the calibration of a hunger term based on a measurable asymmetry in the trained res...
  </details>

- **2026-09-29** — J. G. R. Valangelis, Ailton C. Nascimento, Helder A. S. Costa — [Explicit Analytical Representations for the Schwarzschild Radial Equation via Hypergeometric and Frobenius Expansions](http://arxiv.org/abs/2609.38461v1)
  <details><summary>📄 Abstract</summary>
  The massive Klein-Gordon equation on the Schwarzschild exterior reduces to a radial differential equation of confluent-Heun type. We present its exact reduction by rigorously retaining a subleading centrifugal term that preserves the horizon indicial exponents but critically shifts the accessory parameters. Within the Svartholm--Schmidt hypergeometric-expansion framework, we derive the three-term recurrence relation and establish the corrected continued-fraction compatibility condition matching ...
  </details>

- **2026-09-29** — Gil Kur, Ileana Rugina, Clémentine Carla Juliette Dominé et al. — [Grokking through the Lens of Minimum-Norm Interpolation](http://arxiv.org/abs/2609.38453v1)
  <details><summary>📄 Abstract</summary>
  Grokking shows that fitting the training data and learning the underlying signal can occur at very different stages. However, existing theories offer limited quantitative insight into how this delayed generalization depends on inductive bias and signal structure. Our work addresses the gap by developing a statistical theory that characterizes how regularization geometry and signal sparsity govern generalization near interpolation. In particular, we focus on the prototypical setting of high-dimen...
  </details>

- **2026-09-29** — Maxime Bouscary, Marco Molinaro, Sirui Li et al. — [TACIT: Optimization Models that Learn from Their Mistakes](http://arxiv.org/abs/2609.38434v1)
  <details><summary>📄 Abstract</summary>
  Real-world optimization problems are difficult to model accurately because many objectives and constraints reside in domain experts' tacit knowledge, making them hard to formalize. As a result, optimization models often contain miscalibrated objectives, missing constraints, or omitted decision variables, leading to solutions that fail to reflect operational realities. We address this challenge by automatically repairing misspecified formulations using historical data consisting of past solutions...
  </details>

- **2026-09-29** — Jinyi Ye, Yuangang Li, Chenxiao Yu et al. — [MetaPersona: Task-Grounded Synthetic Populations from Empirical Social Science](http://arxiv.org/abs/2609.38392v1)
  <details><summary>📄 Abstract</summary>
  Personas used to seed LLM social simulations face a cold-start problem: existing methods lack a principled basis for deciding which attributes to include and how to assign their values. As a result, synthetic populations may misrepresent the demographic composition, latent attributes, and dependency structure that shape downstream behavior. We introduce MetaPersona-DB, a dataset of 11,000+ empirical human-subjects studies annotated with task-relevant variables, reported relationships, and aggreg...
  </details>

- **2026-09-29** — Chand Sahil Mansuri, Xin Wang, Mengying Li et al. — [Multi-agent discussion gains less when dissent is withheld](http://arxiv.org/abs/2609.38324v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems of LLMs add discussion to majority voting and are therefore expected to be more capable. However, empirical reports conflict on whether discussion improves accuracy or leads to an incorrect consensus. Here, we introduce a parsimonious model that explains when discussion improves accuracy and when it ends in an incorrect consensus, built from four behaviors repeatedly observed in LLM agents: (1) withholding dissent, (2) internalizing a stated answer, (3) reconsidering after se...
  </details>

- **2026-09-29** — Jeff Calder, Nadejda Drenska — [The finite-horizon five-expert prediction problem](http://arxiv.org/abs/2609.38035v1)
  <details><summary>📄 Abstract</summary>
  We give an explicit solution to the five expert prediction with expert advice partial differential equation (PDE) in the finite-time horizon setting. The solution formula establishes that the adversary's rank strategy $(1,0,1,0,0)$ is globally optimal, and the COMB strategy $(1,0,1,0,1)$ is optimal exactly on the set where $x_1=x_2$ and $x_3=x_4$. The formula is derived from the solution of the geometric-stopping problem given in our companion paper through the transform principle of Bayraktar, ...
  </details>

- **2026-09-29** — Ruiyu Yan, Bowen Chen, Shaowen Wan et al. — [NeuronEye: Query-Guided Visual Concept Activation for Vision-Language Reasoning](http://arxiv.org/abs/2609.38098v1)
  <details><summary>📄 Abstract</summary>
  Current vision-language models (VLMs) encode visual information in dense hidden states where object identity, spatial layout, and local attributes are implicitly entangled rather than explicitly disentangled, limiting their ability to isolate and modulate the specific visual evidence required by a given language query. Inspired by sparse population coding and top-down modulation in biological vision, we introduce NeuronEye, a plug-in framework that constructs a sparse, concept-level neuron vocab...
  </details>

- **2026-09-29** — Chengjie Jiang, Yunqi Zhou, Jiafeng Yan et al. — [RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA](http://arxiv.org/abs/2609.38072v1)
  <details><summary>📄 Abstract</summary>
  Ultra-high-resolution (UHR) remote sensing visual question answering (VQA) requires models to resolve small visual evidence within extremely large images. Existing approaches typically rely on token pruning, visual search, or tool-augmented reasoning at inference time. We instead investigate whether the benefit of zoom-in visual privilege can be internalized into the model. We introduce RS-OPSD, a reliable privileged on-policy self-distillation (OPSD) framework for UHR remote sensing VQA. To pro...
  </details>

- **2026-09-29** — Parthib Roy, Yash Tandon, Marcus Blennemann et al. — [doPlan: A Variable-Horizon Dataset for Multi-Stage Language-Conditioned Planning in Autonomous Driving](http://arxiv.org/abs/2609.38028v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles interacting with passengers through natural language must reason beyond immediate commands. Passenger intent may span multiple stages of behavior, depend on future events, refer to surrounding agents or landmarks, and remain relevant as driving conditions evolve. Existing language-enabled driving datasets largely focus on short, localized interactions, leaving these longer-horizon forms of passenger intent comparatively underexplored. We introduce doPlan, to our knowledge the...
  </details>

- **2026-09-29** — Diyuan Wu, Lehan Chen, Theodor Misiakiewicz et al. — [When do data mixtures improve scaling laws? Insights from high-dimensional regression](http://arxiv.org/abs/2609.38011v1)
  <details><summary>📄 Abstract</summary>
  Modern machine learning systems are trained on mixtures of data from different domains, and choosing the right mixture can substantially improve downstream performance. Despite an extensive literature on data mixing and reweighting, existing work is largely empirical and it remains unclear when auxiliary data genuinely improves scaling laws rather than merely providing more samples. To gain insight into this question, we study a high-dimensional mixed-data regression model with a shared regressi...
  </details>

- **2026-09-29** — Jiaming Tang, Mingyan Liu, Armin Sarabi — [Learning What to Remember: Long-horizon Counterfactual Memory Optimization](http://arxiv.org/abs/2609.37930v1)
  <details><summary>📄 Abstract</summary>
  Persistent textual memory allows language models to carry information across long interactions, but learning what to remember is fundamentally a credit-assignment problem. A memory rewrite may only become useful many steps later, while much of the observed utility may be inherited from information already stored before the rewrite. We introduce Memory Gain Policy Optimization (MGPO), which isolates the incremental value of each memory rewrite by crediting it for its marginal contribution to curr...
  </details>

- **2026-09-29** — Erkan Turan, Gaspard Abel, Maks Ovsjanikov — [Pattern Formation in Transformers](http://arxiv.org/abs/2609.37921v1)
  <details><summary>📄 Abstract</summary>
  What are the inductive biases of a Transformer architecture? Existing theory on how the forward pass shapes representations either considers whether Transformers escape from rank collapse or demonstrates that self-attention drives tokens toward cluster patterns. The latter view arises from an elegant dynamical systems perspective, but relies on simplified architectural assumptions, and does not explain the rich structures observed in practice. This leaves a major open question: when a full Trans...
  </details>

- **2026-09-29** — Sara Ghazanfari, Siddharth Garg, Prashanth Krishnamurthy et al. — [SYNCR: Diagnosing and Learning Cross-Video Reasoning from Simulation](http://arxiv.org/abs/2609.37918v1)
  <details><summary>📄 Abstract</summary>
  Reasoning across videos requires aligning events, matching identities, comparing motion, and integrating partial observations. Evaluating these capabilities and testing how to improve them requires both reliable labels and targeted supervision. We introduce SYNCR, a simulator-grounded framework that connects these two needs through shared task generators. Built on Habitat, Kubric, and CLEVRER, SYNCR derives answers from environment state and provides 4,000 evaluation questions and 15,960 trainin...
  </details>

- **2026-09-29** — Nagham Omar, Mahmoud Jabarin, Kinan Ibraheem et al. — [It's Not What the Image Shows: Irrelevant Context Destabilises VLM Judges Without Informing Them](http://arxiv.org/abs/2609.37863v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly used in place of human annotators, making it important that substitutability tests reflect the model rather than incidental evaluation conditions. We introduce MIST, the Misleading-Image Stress Test: 200 English sentences, each built around a phrase readable either figuratively or literally and shown with an aligned image depicting its reading, a misleading image depicting the opposite, or no image at all. The guidelines require the label to be deci...
  </details>

- **2026-09-29** — Jia Cai — [Making Duplicate Reimbursement Unrepresentable: A Verified Ethereum E-Invoice System for Humans and AI Agents](http://arxiv.org/abs/2609.37819v1)
  <details><summary>📄 Abstract</summary>
  Electronic invoices are replacing paper invoices worldwide, but today's centralized architectures leave three problems unsolved on the consumption side: an invoice can be submitted for reimbursement repeatedly, authenticity is difficult for recipients to verify, and data is siloed at a central authority that forms both a performance bottleneck and a single point of failure. This paper presents the design, formal analysis, and implementation of a complete blockchain-based electronic invoice syste...
  </details>

- **2026-09-29** — Zifeng Cheng, Jie Zheng, Zhiwei Jiang et al. — [Selecting What Matters: Semantic Compression-Guided Selective Pooling for Long-Context Embeddings](http://arxiv.org/abs/2609.37782v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential as training-free text encoders for long-context embeddings. Existing approaches primarily improve information flow under causal attention and typically construct embeddings by uniformly averaging all token representations. However, for long documents, such mean pooling can dilute salient semantic information with abundant redundant or weakly informative content. To this end, we propose SCSP, a training-free framework that leverages semanti...
  </details>

- **2026-09-29** — Aaron Steiner, Ksenia Elagin, Ralph Peeters et al. — [Billiger.de Products: A Bilingual Entity Matching Benchmark](http://arxiv.org/abs/2609.37713v1)
  <details><summary>📄 Abstract</summary>
  Existing product matching benchmarks primarily contain English-language product data and are often dominated by a single product category, such as electronics. This paper introduces Billiger.de Products, a bilingual German and English entity matching benchmark covering thirteen consumer product categories, including difficult-to-handle categories such as clothing and furniture. The benchmark data originates from the German price comparison platform billiger.de. Following the design of WDC Produc...
  </details>

- **2026-09-29** — Pinze Ren, Yuwei Zhang, Hao Chen et al. — [PAIQ: Patch-Aligned Semantic Injection via Residual Rotation](http://arxiv.org/abs/2609.37685v1)
  <details><summary>📄 Abstract</summary>
  Language-aligned and self-supervised visual encoders offer complementary strengths in semantic abstraction and spatial detail. Harnessing this complementarity requires enriching local features while retaining distinctions between semantically related patches. We introduce PAIQ, a patch-aligned semantic injection framework that combines content-based cross-encoder matching with orthogonally constrained residual updates. Using DINOv3 patch features as the spatial base, PAIQ aggregates complementar...
  </details>

- **2026-09-29** — Chu Zhang, Haoyu Jiang, Hongyuan Zhang et al. — [Med-RADIO: Reducing All Medical Domains Into One via Multi-Teacher Distillation](http://arxiv.org/abs/2609.37682v1)
  <details><summary>📄 Abstract</summary>
  The rapid expansion of large-scale medical datasets and computational resources has driven significant progress in medical foundation models. Given the inherent heterogeneity of medical imaging modalities, current research mainly follows two paths: specialized models optimized for specific modalities, and generalist models designed to handle multiple modalities. However, medical generalist models suffer from both insufficient training data scale relative to natural image generalists and inadequa...
  </details>

- **2026-09-29** — Binghong Qian, Xuanhe Liu, Yifan Xing et al. — [VoxelSage: Tool-Augmented 3D CT Analysis and Simulator-Shielded Sequential Resection Planning for Liver Tumors](http://arxiv.org/abs/2609.37648v1)
  <details><summary>📄 Abstract</summary>
  Preoperative liver-tumor assessment requires segmentation, physical-space measurement, visual evidence, and resection planning from the same three-dimensional CT volume. Existing tools often handle these steps separately, while language models cannot reliably compute physical measurements from CT. To provide an integrated workflow, we present VoxelSage, a multi-modal system for two- and three-dimensional visualization, liver-tumor analysis, and preoperative resection planning. Its dual-port arch...
  </details>

- **2026-09-29** — Zijie Meng, Xiwei Dai, Yingying Zhang et al. — [ReLMem: Learning Recurrent Memory for Longitudinal EHR Modeling](http://arxiv.org/abs/2609.37587v1)
  <details><summary>📄 Abstract</summary>
  Longitudinal electronic health record (EHR) modeling requires integrating new visits with an expanding patient history. Yet the continual accumulation of clinical information imposes increasing computational and memory costs on large language models (LLMs) when they process and retain complete patient histories. A practical alternative is visit-wise recurrent compression, which incorporates each incoming visit into a compact, continually updated patient memory. However, under a fixed memory budg...
  </details>

- **2026-09-29** — Yulong Huang, Chen Jiang, Zhanpeng Zhou et al. — [Looped Transformers as Optimizers](http://arxiv.org/abs/2609.37379v1)
  <details><summary>📄 Abstract</summary>
  Looped Transformers provide a parameter-efficient approach to depth scaling by repeatedly applying shared Transformer blocks. Recent reasoning models have likewise highlighted the value of scaling test-time computation through longer computation trajectories. However, the principles for designing effective loop transitions remain poorly understood. We view the looped hidden state as a fast weight that is updated throughout the depth. We formulate loop transitions as local gradient-based updates,...
  </details>

- **2026-09-29** — Hossein Resani, Javen Qinfeng Shi — [Do-JEPA: From Masking to Intervention in Latent World Models](http://arxiv.org/abs/2609.37378v1)
  <details><summary>📄 Abstract</summary>
  Latent world models are trained to predict what happens next, so nothing in their objective separates what an action caused from what merely co-occurred with it. Object-masking models such as C-JEPA intervene on what the predictor can see; we intervene on what physically happens. From one saved simulator state we run the dynamics under an action $a$ and under a reference action $a_{\varnothing}$, and train the model to predict the difference $Δz=z^{a}-z^{a_{\varnothing}}$ between the two latent ...
  </details>

- **2026-09-29** — Yalun Wu, Bingzhou Wang, Boyang Wang et al. — [TAEC: Trajectory-Aware Evidence Coordination for Multi-Step Visual RAG](http://arxiv.org/abs/2609.37349v1)
  <details><summary>📄 Abstract</summary>
  Multi-step visual retrieval-augmented generation (RAG) answers complex questions by repeatedly retrieving visual evidence, updating an intermediate state, and deciding whether to continue searching or answer. Yet retrieving relevant evidence does not ensure its effective use throughout the reasoning trajectory. As multi-step reasoning progresses, redundant sources occupy context capacity needed for missing evidence, observations tied to resolved requirements or unproductive searches linger in co...
  </details>

- **2026-09-29** — Sieun Hyeon, Yejoon Lee, Mintaek Lim et al. — [What Comes Next? Omni-StoryBench for Evaluating Story-Grounded Omnimodal Generation](http://arxiv.org/abs/2609.37317v1)
  <details><summary>📄 Abstract</summary>
  Omnimodal evaluation should go beyond independent text, image, and speech production: individually plausible outputs may not express a coherent shared event. We introduce Omni-StoryBench, a story-grounded omnimodal benchmark evaluating whether models can coherently continue stories across image, narration, and speech. Each instance provides a current storybook page and structured next-page conditions, requiring models to generate the next illustration, narration, and spoken character utterance. ...
  </details>

- **2026-09-29** — Yue Pan, Jiawei Li, Ziyuan Zhang et al. — [CRJudgeBench: Can AI Detect Plausible but Invalid Code Reviews?](http://arxiv.org/abs/2609.37216v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate plausible code-review comments, but such comments may contain technically incorrect claims that mislead developers. We study technical trustworthiness judgment: determining whether a review comment's core technical claims are correct and applicable to the reviewed code in its repository context. Existing code-review benchmarks primarily evaluate review generation, issue discovery, or general comment quality, but do not directly assess whether an agent can deter...
  </details>

- **2026-09-29** — Qili Zhang, Qianren Mao, Hanze Cai et al. — [Learning to Prove, Not Just to Answer: Reinforcement Learning from Formal Verification for Natural-Language Logical Reasoning](http://arxiv.org/abs/2609.37203v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed for natural-language logical reasoning, where the final answer is easy to check but the proof behind it is not. In natural-language logical reasoning, an intermediate conclusion should follow from its premises, and the resulting derivation should support the final answer. Existing methods lack machine-checkable verification of intermediate conclusions and answer-supporting proof dependencies, so they may assign credit to invalid or answer-ir...
  </details>

- **2026-09-29** — Zhangquan Chen, Yaoxin Niu, Xiang An et al. — [HaPRL: Human-Anchored Process Reinforcement Learning for Visual Search Agent](http://arxiv.org/abs/2609.37190v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn visual search agents answer questions about high-resolution images by iteratively deciding where to look. Reinforcement learning for these agents rewards only the final answer, leaving the search process unsupervised. Consequently, faulty routes in which the reasoning process is erroneous yet the final result is correct arise frequently, which in turn leads to ineffective training, i.e., scaling along the wrong paths. In this paper, we introduce HaPRL, the first framework to reinforce...
  </details>

- **2026-09-29** — Zheng Zhang, Lufei Li, Xinyue Tan et al. — [From Judgment Quality to Downstream Utility: Rethinking LLM-as-a-Judge for Open-Ended Tasks](http://arxiv.org/abs/2609.37145v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-Judge is increasingly used to evaluate policy responses on open-ended tasks that lack ground-truth answers. Existing work often directly converts the resulting judgments into reward signals for policy training, paying limited attention to intrinsic judgment quality and largely restricting the use of Judges to training-time supervision. We systematically investigate judgment quality and downstream utility by examining both how judgments are elicited and how they are used. For judgment el...
  </details>

- **2026-09-29** — Yaoxin Niu, Zhangquan Chen, Yang Zhang et al. — [EviViT: Evidence-Adaptive Vision Transformers for Fine-Grained Perception](http://arxiv.org/abs/2609.37123v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained visual perception enables vision-language models to distinguish subtle attributes and ground their answers in visual evidence. In high-resolution scenes, processing the whole image at greater resolution spends visual tokens on irrelevant content, while isolated crops can lose the context needed to interpret the selected evidence. We introduce EviViT, a lightweight attachment that learns where a pretrained vision transformer should acquire detail. Human visual-search traces supervise...
  </details>

- **2026-09-29** — Nikitas Theodoropoulos, Maria Lymperaiou, Giorgos Filandrianos — [Cross-Linguistic Effects in Bilingual Phoneme BabyLMs](http://arxiv.org/abs/2609.37121v1)
  <details><summary>📄 Abstract</summary>
  Cross-linguistic effects are a central topic in bilingual first-language acquisition. Artificial learners can help investigate L1-L2 interactions by enabling controlled comparisons across language combinations and learning conditions. Recent work explores this direction by training bilingual language models under developmentally plausible constraints. However, human and model learners still diverge in fundamental ways, with one major difference being input modality: children learn primarily from...
  </details>

- **2026-09-29** — Kerui Ren, Yingxiang Xu, Kaiwen Song et al. — [Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](http://arxiv.org/abs/2609.37089v1)
  <details><summary>📄 Abstract</summary>
  Real-world videos provide rich demonstrations of manipulation, but turning them into reusable robot skills requires visually aligned environments, executable physical interactions, and mechanisms for learning from experience. We introduce Real2Gym, an agentic Real2Sim2Real framework that turns human and robot demonstrations into interactive simulation gyms and brings skills acquired in simulation to physical robots. The Real2Sim module reconstructs editable scenes, aligns objects and cameras wit...
  </details>

- **2026-09-29** — Zhengqiang Zhang, Lingchen Sun, Rongyuan Wu et al. — [LDM-is-AE: Latent Diffusion Model is an Auto-Encoder for End-to-End Image Generation](http://arxiv.org/abs/2609.37080v1)
  <details><summary>📄 Abstract</summary>
  Latent Diffusion Models (LDMs) typically adopt a two-stage pipeline: an auto-encoder (AE) is first pre-trained to define a latent space, then a diffusion model is trained to perform denoising within it. Such a two-stage design introduces a representation mismatch, as the latent space is optimized for reconstruction rather than adapting the denoising dynamics. We reveal that the LDM itself is an AE, and consequently present LDM-is-AE, an end-to-end one-stage LDM training framework that eliminates...
  </details>

- **2026-09-29** — Mengjun Yi, Huaian Gu, Yinghao Ai et al. — [FedLAFP: Low-Rank Aggregation Meets Full-Rank Personalization in Federated Fine-Tuning](http://arxiv.org/abs/2609.37033v1)
  <details><summary>📄 Abstract</summary>
  Federated parameter-efficient fine-tuning enables clients to adapt pre-trained models without sharing raw data or communicating the full model, but statistical heterogeneity makes a single global adapter insufficient for personalized prediction. Existing personalized methods typically use the same low-rank structure for both shared and private adaptation, overlooking their distinct requirements for aggregation and personalization. We propose FedLAFP, a role-aware framework that couples a compact...
  </details>

- **2026-09-29** — Yuzhe Zhang, Weijie Zhu, Haolin Yang et al. — [CypherTurn: A Multi-Turn Benchmark for Conversational Text-to-Cypher Evaluation and the Autonomy Divergence](http://arxiv.org/abs/2609.36987v1)
  <details><summary>📄 Abstract</summary>
  Graph databases are increasingly queried through natural language, yet every existing benchmark evaluates isolated single-turn queries rather than the multi-turn sessions through which analysts actually work. We introduce CypherTurn, the first benchmark for conversational Text-to-Cypher evaluation, comprising 721 sessions and 5,927 turns across 7 knowledge graphs and 13 conversational phenomena. We evaluate 15 models under a guided oracle protocol and a fully autonomous agentic protocol, yieldin...
  </details>

- **2026-09-29** — Zhiwei Yang, Jiahua Yang, Huiru Lin et al. — [SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging](http://arxiv.org/abs/2609.36982v1)
  <details><summary>📄 Abstract</summary>
  Knowledge concept tagging aims to assign specific concept or topic labels to educational content, which is essential for both educators and learners in traditional and online teaching practices. Recent work has explored large language models (LLMs) for this task, achieving promising performance. However, LLMs still struggle to select the correct concept from a large-scale candidate set due to the high dimensionality of the decision space. In this paper, we propose a novel three-stage Select-Reas...
  </details>

- **2026-09-29** — Hongbin Lin, Chaoda Zheng, Yiming Yang et al. — [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](http://arxiv.org/abs/2609.36851v1)
  <details><summary>📄 Abstract</summary>
  End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-world deployment. To address this issue, reinforcement learning (RL) post-training offers a promising alternative by leveraging world models as interactive training environments to enable future scene generation for policy improvement. Nevertheless, existing approaches either rely on re...
  </details>

- **2026-09-29** — Wenxiao Fan, Jingling Fu, Lichen Ma et al. — [Calibrate the Decisions That Change the Future: On-Policy Post-Training Quantization for Multimodal Large Language Models](http://arxiv.org/abs/2609.36828v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) lowers deployment cost for multimodal large language models, but calibration typically reconstructs fixed sequences with local objectives. This overlooks autoregressive feedback: a quantization-induced token change redirects the prefix and changes future states. Yet on-policy coverage alone is insufficient because many decision mismatches barely affect future generation. We propose OnPTQ, an on-policy framework that calibrates on trajectories visited by the curre...
  </details>

- **2026-09-29** — Chuanpu Liu, Miao Yu, Yikai Cai et al. — [RESCUE: Repairing Language Model Errors to Sparse Circuits via Reinforcement Learning](http://arxiv.org/abs/2609.36813v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) exhibit strong general capabilities that mechanistic interpretability has attributed to sparse computational circuits. However, existing circuit studies emphasize preserving functionality or explaining safety, leaving the mechanisms underlying failures across a broader range of tasks largely unexplored. Extending circuit analysis from abilities to errors, we explore the perspective that such failures may likewise arise from erroneous internal computations and that ta...
  </details>

- **2026-09-29** — Yitong Han, Nankai Lin, Juan Luo et al. — [VAA-CSEC: Vote-guided Advantage Allocation for Chinese Semantic Error Correction](http://arxiv.org/abs/2609.36804v1)
  <details><summary>📄 Abstract</summary>
  Chinese Semantic Error Correction (CSEC) targets semantic errors in Chinese text, which are typically more subtle and complex than spelling and grammatical errors but remain relatively underexplored. Existing LLM-based approaches face two recurring obstacles in this task: over-correction, and unclear interaction between Chain-of-Thought (CoT) reasoning and self-consistency decoding, such that the benefits brought by CoT cannot be reliably transferred to final corrections. We propose Vote-guided ...
  </details>

- **2026-09-29** — Zunhai Su, Yuxuan Sun, Jianchao Tan et al. — [QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching](http://arxiv.org/abs/2609.36760v1)
  <details><summary>📄 Abstract</summary>
  Multi-Head Latent Attention (MLA) enables expressive multi-head attention with compact caches for its content and decoupled RoPE paths, yet cache memory still scales linearly with context length and batch size. In this work, we establish a systematic model of MLA's dual-path quantization errors, characterizing their distinct effects on attention-output distortion and explaining the pronounced amplification of RoPE-path errors. Guided by this analysis, we introduce QuantMLA, a function-aligned fr...
  </details>

- **2026-09-29** — Xinghao Chen, Junnan Dong, Cai Ke et al. — [ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation](http://arxiv.org/abs/2609.36722v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents repeatedly load reusable content, such as skills, documents, and memory entries, into the current context. Re-encoding this content for every request wastes computation. Position-independent caching (PIC) alleviates this by encoding each artifact independently and reusing its key-value (KV) states at arbitrary positions, but it incurs a quality loss relative to full-context prefill. Existing methods repair this loss by restoring global position IDs or recomputin...
  </details>

- **2026-09-29** — Xue Yang, Rigui Zhou, Dax Enshan Koh et al. — [Quantum Fidelity Landscape-Guided Prior Calibration for Single-Circuit QGAN Image Generation](http://arxiv.org/abs/2609.36702v1)
  <details><summary>📄 Abstract</summary>
  Quantum Generative Adversarial Networks (QGANs) have emerged as representative generative models in the Noisy Intermediate-Scale Quantum (NISQ) era and have attracted increasing attention in quantum machine learning. However, most existing QGAN methods rely on patch-based decomposition strategies, which weaken the global consistency of generated images and increase quantum resource overhead. In this work, we investigate a simpler approach: pixel-level, end-to-end image generation using a single-...
  </details>

- **2026-09-29** — Xiaoyu Zhang, Weizhong Fu, Yixiao Chen — [Electronic excitation spectra and recovery of excited states with neural network wave functions](http://arxiv.org/abs/2609.36699v1)
  <details><summary>📄 Abstract</summary>
  Accurate electronic spectra require both a flexible description of electron correlation and a tractable treatment of the many states contributing to the response. We combine neural network wave functions with the Lorentz integral transform to calculate electronic spectra directly in continuous coordinates, without truncation error from a fixed one-electron basis and with polynomial computational cost per optimization step. Instead of constructing a prescribed set of excited states, the method so...
  </details>

- **2026-09-29** — Wenjin Liu, Chenxi Wang, Yue Lu et al. — [CHAIN: Calibrated LLM Forecasting via Causal-Temporal Hypergraph Inference](http://arxiv.org/abs/2609.36689v1)
  <details><summary>📄 Abstract</summary>
  Large language models have achieved significant progress in event forecasting, yet their probability outputs exhibit systematic calibration bias that varies heterogeneously across different domains and question types, undermining the trustworthiness of probabilistic outputs for decision-making under uncertainty. However, existing calibration methods typically correct probability outputs after prediction is complete, without modeling the structural sources of bias within the prediction process it...
  </details>

- **2026-09-29** — Ziqi Zhao, Fanqing Meng, Haocheng Lu et al. — [Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement](http://arxiv.org/abs/2609.36675v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) aims to achieve compounding gains by having models improve themselves. While most existing RSI systems optimize external agent harnesses or prompts around a frozen base model, data-centric RSI directly updates the model's own parameters by training on agent-generated data. However, because validating data strategies requires expensive model training, existing methods face a fundamental dilemma: a single agent gets trapped in narrow directions and lacks exploratio...
  </details>

- **2026-09-29** — Shuangping Li, Peng Zhang — [GenLimitLib: A Formal Library for Language Generation in the Limit and AI-Assisted Mathematical Research](http://arxiv.org/abs/2609.36663v1)
  <details><summary>📄 Abstract</summary>
  We present GenLimitLib, a source-aligned Lean 4 library for language generation in the limit. Introduced by Kleinberg and Mullainathan at NeurIPS 2024, language generation in the limit studies a theoretical question motivated by LLMs: how to generate valid new strings from observed examples. This young and rapidly evolving field offers a natural testbed for studying large-scale formalization. GenLimitLib contains formal developments for 30 papers. It extracts shared definitions and reusable proo...
  </details>

- **2026-09-29** — Zhaoxian Wu, Tayfun Gokmen, Omobayode Fagbohungbe et al. — [Making Analog Training Scale: Co-Designing Mapping, Optimizer, and Converters](http://arxiv.org/abs/2609.36584v1)
  <details><summary>📄 Abstract</summary>
  Analog in-memory computing (AIMC) offers an alternative for model training by executing matrix operations directly where weights are stored. However, scaling AIMC to train modern deep models remains an open challenge due to severe hardware non-idealities, including physical weights with finite dynamic range and write granularity, analog-digital converters with finite resolution, and noisy and asymmetric updates. Guided by the insight that gradient accumulation is sensitive to precision and round...
  </details>

- **2026-09-29** — Andrew Tang, Nicholas Deas, Kathleen McKeown et al. — [Retrieval Sensitivity to Identity Signals in Queries](http://arxiv.org/abs/2609.36534v1)
  <details><summary>📄 Abstract</summary>
  Dense retrievers decide which documents reach users and the language models that use them, yet they are typically evaluated with neutral queries. We ask whether the identity signals that real users express in their queries---political ideology and dialect---bias what a retriever returns. We design evaluations in two domains, political news and consumer-health questions, each pairing a controlled synthetic set that varies only the identity signal with naturalistic queries. Across five dense retri...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 652 |
| prompt-injection | 585 |
| memory-poisoning | 52 |
| tool-use-attack | 147 |
| backdoor | 488 |
| adversarial-attack | 615 |
| privacy-leakage | 4244 |
| steganography | 73 |
| misuse | 1099 |
| red-teaming | 130 |
| vulnerability | 3374 |
| defense | 3191 |
| alignment | 2971 |
| robustness | 3212 |
| watermark | 518 |
| unlearning | 107 |
| agent-safety | 60 |
| benchmark | 67 |
| survey | 378 |
| other | 8643 |

---

📚 **全部 30606 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-01 22:15:04*