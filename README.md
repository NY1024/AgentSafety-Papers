<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-30251-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-09-30 18:09 ｜ **论文总数 / Total Papers**: 30251（近 30 天 / Recent 30 days: 4506）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 30251 篇论文（含摘要、分类筛选、搜索）/ View all 30251 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 647
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 581
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 52
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 145
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 484
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 609
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4227
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 72
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1091
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 129
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3342
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3158
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2934
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3152
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 502
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 105
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 59
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 66
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 372
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 8524

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4506 篇，完整 30251 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4506 papers from the last 30 days (with date, authors & abstract). For the full list of 30251 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

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

- **2026-09-28** — Shunchang Liu, Lukas Fluri, Xin Chen et al. — [Narrow Multimodal Fine-Tuning Can Induce Emergent Misalignment](http://arxiv.org/abs/2609.35291v1)
  <details><summary>📄 Abstract</summary>
  Modern AI models are aligned through post-training to adapt them to downstream tasks. Recent work shows that fine-tuning language models on narrow tasks can induce emergent misalignment (EM), causing broadly harmful behaviors beyond the training task. However, EM has been studied almost entirely in text-only tasks, leaving its manifestation in multimodal models unclear. In this paper, we define and analyze EM in the context of vision-language models. We first induce EM via fine-tuning on narrow ...
  </details>

- **2026-09-28** — Xi Wang, Songlei Jian, Yiming Zhang et al. — [Jailbreak Context Lingers: Divergent Safety Routing and Its Cross-Task Predictability in Tool Agents](http://arxiv.org/abs/2609.34686v1)
  <details><summary>📄 Abstract</summary>
  As large language models increasingly operate as tool-using agents, post-jailbreak safety feedback is often assumed to serve as a reliable safeguard; however, how lingering jailbreak context shapes subsequent agent behavior remains largely unexplored. To systematically examine this dynamic, we introduce a paired continuation framework across 192 parent tasks spanning 42 domains, evaluating 12,148 analyzed continuation pairs (curated from a 12,288-pair initially design) across eight diverse agent...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 12 papers

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

- **2026-09-29** — Federico Torrielli, Gianluca Barmina, Andrea Blasi Núñez et al. — [Selecting The Most Informative Tokens in Natural Language Autoencoders](http://arxiv.org/abs/2609.37040v1)
  <details><summary>📄 Abstract</summary>
  Natural language autoencoders translate a language model's internal activations into readable explanations. Explaining every token position is costly. Which positions should an auditor inspect to understand a potential threat? We study this question across $4.7$ million explanations on prompt injection and concealment. We compare signals from model computation with a ranker trained only on chat structure. Chat structure usually selects more relevant explanations than the computational signals, w...
  </details>

- **2026-09-28** — Yan Zhan, Yunze Song, Mengkai Hou et al. — [Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template Prompt Injection](http://arxiv.org/abs/2609.35932v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection against LLM agents becomes much stronger when the injected instruction is wrapped in the model's own chat template. A forged template marker such as <|im_start|> can reach the model either as a single reserved control token or as a sequence of ordinary subword tokens. The two decode to exactly the same text, and because tokenization runs on the server, the defender rather than the attacker decides which one the model receives. We use this to measure how much of the injected inst...
  </details>

- **2026-09-28** — Jie Zhang, Andrei Baroian, Jan N. van Rijn et al. — [Render Before Reading: Visual Rendering as a Prompt Injection Defense](http://arxiv.org/abs/2609.36121v1)
  <details><summary>📄 Abstract</summary>
  Large language models are vulnerable to prompt injection attacks, where third-party adversarial content can hijack the model's behavior. In this paper, we study the role played by the adversarial data's input modality, and identify a systematic asymmetry: multimodal LLMs are more likely to follow adversarial instruction when they appear as text than when the same instruction is delivered through a non-textual channel (e.g., as an image). We hypothesize that this modality gap arises from text-cen...
  </details>

- **2026-09-28** — Bravish Ghosh — [Tracekit: Tamper-Evident Intent-Reasoning-Action Auditing for Autonomous Coding Agents](http://arxiv.org/abs/2609.35659v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents read untrusted files, run shell commands and spawn sub-agents with little supervision, yet their record is usually an editable log. We present Tracekit, an open-source, dependency-free system that captures three channels for every agent session: what the human asked (intent), what the model said of its reasoning (self-report), and what it actually executed (actions). These are written to a hash-chained, externally anchorable ledger and cross-checked. Tracekit hooks into ...
  </details>

- **2026-09-28** — Rohit Saxena, Utkarsh Upadhyay — [Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence](http://arxiv.org/abs/2609.34572v1)
  <details><summary>📄 Abstract</summary>
  Reasoning language models that can call tools must decide during inference whether to answer unaided or delegate. Any self-reflection mechanism for this must answer three questions: where the reflective signal comes from (verbal reports, output distributions, hidden states, a separate predictor), how it is presented to the model (numerical prediction, confidence token, prompt injection), and whether it changes the model's subsequent action. We isolate the third question. At a fixed point in othe...
  </details>

- **2026-09-28** — Xiao Yang, Yangchen Ou, Yuhan Gao et al. — [CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents](http://arxiv.org/abs/2609.34463v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents increasingly rely on external tools and content, exposing them to indirect prompt injection (IPI). This threat has motivated a wide range of defenses, among which training-based defenses are often regarded as most reliable. However, existing training-based defenses are typically optimized on a static distribution of explicit injections. They learn surface-form cues rather than the boundary between serving the user and obeying an injected objective, and the...
  </details>

- **2026-09-28** — Anmol Pandey, Aditya Jain, Liang Chen et al. — [Certified Multi-Source Integrity for Structured Agent Actions](http://arxiv.org/abs/2609.34245v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly take privileged, often irreversible structured actions, such as paying an invoice. They assemble each action from action-critical fields in documents and tool outputs that an adversary can corrupt, and indirect prompt injection can drive the model itself to extract attacker-chosen values. Current defenses gate on a source's trust label or certify free-text answer quality. None certifies the integrity of a coupled, policy-bound structured action under a corruption budget t...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-09-28** — Mingxi Zou, Langzhang Liang, Zhuo Wang et al. — [From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents](http://arxiv.org/abs/2609.34132v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates a lasting channel through which malicious memory writes can influence future behavior. Persistent-memory attacks are typically evaluated by whether they succeed, yet successful attacks can leave persistent states with substantially different downstream consequences. We study this severity as a distinct attack-design obje...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-09-29** — Haoran Ou, Gelei Deng, Xuanye Zhang et al. — [SKILLLITE: Evidence-Guided Malicious Skill Auditing with Compact LLMs](http://arxiv.org/abs/2609.36879v1)
  <details><summary>📄 Abstract</summary>
  As LLM-based agents perform increasingly complex tasks, Agent Skills have emerged as a flexible mechanism for extending their capabilities. An Agent Skill packages task-specific instructions with executable components and auxiliary resources to provide specialized functionalities. However, the growing adoption of third-party Skills introduces a new supply-chain attack surface. Malicious Skills can embed harmful behaviors that abuse agent privileges and compromise the agent execution environment ...
  </details>

- **2026-09-29** — Zhen Xiong, Qiaoyu Tan — [EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents](http://arxiv.org/abs/2609.36746v1)
  <details><summary>📄 Abstract</summary>
  Agent skills provide a lightweight mechanism for self-evolving agents to accumulate reusable procedural knowledge without updating model parameters. However, existing learned skill curators typically optimize curation without explicitly modeling downstream executor behavior. We show that this can cause systematic cross-executor degradation: curators trained with different executors perform best when paired with their own training executor, indicating that effective skill curation is executor-dep...
  </details>

- **2026-09-28** — Lingqi Jiang, Jialuo Chen, Jianan Ma et al. — [MMSkillRisk: Can Agents Stay Safe When Multimodal Skills Become Traps?](http://arxiv.org/abs/2609.35912v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are shareable packages of procedural instructions, tools, and examples. Multimodal skills additionally include visual references that agents retrieve and inspect during execution. Because these images guide actions, attackers can disguise malicious instructions as ordinary visual guidance within otherwise legitimate skills. Existing skill-security research primarily examines text-carried attacks or scanner detection, leaving the runtime effects of image-borne attacks insufficiently ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 9 papers

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

- **2026-09-28** — Zihan Zhang, Shuangjie Yao, Zesen Liu et al. — [Similarity Is Not Validity: Defending LLM Semantic Caches Against Poisoning](http://arxiv.org/abs/2609.35908v1)
  <details><summary>📄 Abstract</summary>
  Semantic caches reduce LLM serving costs by reusing previously generated answers for semantically similar queries. However, retrieval is based solely on embedding similarity between the incoming query and cached queries. This design enables cache poisoning: an attacker can cache a malicious response under a query with high cosine similarity to benign requests. The vulnerability stems from a gap between retrieval similarity and answer validity. From an information-bottleneck perspective, query em...
  </details>

- **2026-09-28** — Issam Seddik, Mohamed El Amine Seddik — [Why Backdooring Neural Networks is so Easy?](http://arxiv.org/abs/2609.36117v1)
  <details><summary>📄 Abstract</summary>
  Securing modern AI systems against backdoor attacks remains an open challenge and requires fundamentally principled estimates of the adversary's budget -- the poison fraction $π$ and trigger strength $α$ needed to construct successful yet stealthy attacks. Motivated by recent empirical evidence that poisoning large language models can require a nearly constant number of malicious samples even as clean datasets grow, we derive an exact closed-form analysis of a quadratic neuron trained on a poiso...
  </details>

- **2026-09-28** — Kajetan Dymkiewicz, Tim Farrelly, Adam Práda et al. — [Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoor Triggers and Preserves Desired Traits](http://arxiv.org/abs/2609.35356v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning can teach language models undesired behaviours alongside desired ones. Inoculation prompting (IP) aims to limit unwanted generalisation by requesting the undesired behaviour during training and removing the request at inference. However, undesired behaviour can still appear under unrelated prompts. IP can also hinder learning of the desired behaviour. We address these limitations in settings where both behaviours co-occur in most training examples, so filtering out example...
  </details>

- **2026-09-28** — Kaisheng Fan, Yishu Gao, Xunzhu Tang et al. — [LENS: The Sum Is Worse Than the Parts for Set-Level Poisoning in Retrieval-Augmented Generation](http://arxiv.org/abs/2609.35155v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) aggregates evidence from multiple external documents, yet this joint integration creates an underexamined vulnerability: attack effects absent in individual documents can emerge through set-level composition. Existing coordinated attacks do not explicitly enforce that every proper subset remains insufficient in frozen single-round RAG. We formalize set-level compositional poisoning, where documents designed to remain individually plausible jointly redirect RA...
  </details>

- **2026-09-28** — Zhongqi Wang, Jie Zhang, Nie Sen et al. — [Backdoor as Probe: Test-Time Adversarial Defense for CLIP](http://arxiv.org/abs/2609.34641v1)
  <details><summary>📄 Abstract</summary>
  Test-time adversarial defense improves the robustness of vision-language foundation models such as CLIP without retraining. However, adversarial activation shifts are typically treated as distortions to suppress, rather than signals to exploit. We turn these shifts into defense signals by repurposing the trigger-to-target mechanism of backdoors. The key is to implant a defender-controlled backdoor as a probe that is weakly activated by clean inputs but strongly activated by adversarial shifts. B...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 4 papers

- **2026-09-29** — Rikhiya Ghosh, Himanshu Kumar, Sriram Venkatapathy et al. — [FinRT: Distilling Adaptive Red-Teaming Strategies into Reusable Adversarial Generators in Consumer Finance](http://arxiv.org/abs/2609.36474v1)
  <details><summary>📄 Abstract</summary>
  In regulated industries like consumer finance, seemingly harmless user queries can exploit large language model vulnerabilities, triggering safety failures and pushing responses dangerously close to policy limits. Existing automated red-teaming methods trade off attack effectiveness against generation cost, while treating coverage, severity, and diversity as incidental rather than joint objectives. We introduce FinRT, a structured framework that builds reusable adversarial prompt generators from...
  </details>

- **2026-09-29** — Yuanwei Hu, Bo Peng, Yuheng Jia et al. — [VLM4Cluster: Benchmarking Deep Clustering In the Era of Vision-Language Pre-training](http://arxiv.org/abs/2609.36648v1)
  <details><summary>📄 Abstract</summary>
  Vision-language pre-training has reshaped image clustering, giving rise to language-assisted image clustering (LaIC), which leverages textual semantics to complement visual representations. Despite the rapid proliferation of LaIC methods, it remains unclear how much LaIC has actually advanced image clustering, as existing studies generally suffer from major limitations, including inconsistent experimental settings, inadequate dataset selection, and limited evaluation dimensions. To address this ...
  </details>

- **2026-09-28** —  Mansi, Nikhil Raghavan, Zixia Huang et al. — [eval-unlearn: Benchmarking unlearning in Text-to-Image Diffusion Models](http://arxiv.org/abs/2609.35269v1)
  <details><summary>📄 Abstract</summary>
  The rising number of concept unlearning techniques for text-to-image (T2I) diffusion models has produced a fragmented evaluation landscape. Methods are assessed under heterogeneous experimental conditions making principled cross-method comparison difficult. We present eval-unlearn, an open-source Python library providing a unified, reproducible benchmarking framework for concept unlearning in T2I Diffusion models. eval-unlearn integrates twelve published unlearning techniques spanning fine-tunin...
  </details>

- **2026-09-28** — Mashal Zainab, Salijona Dyrmishi, Hamid Bostani et al. — [Breaking Windows Malware Detection: A Comprehensive Evaluation of Problem-Space Adversarial Robustness](http://arxiv.org/abs/2609.34456v1)
  <details><summary>📄 Abstract</summary>
  Problem-space evasion attacks have exposed critical weaknesses in machine learning-based malware detectors; yet, their evaluation remains fragmented across models, datasets, and attack methodologies, often neglecting domain-specific requirements such as executability and functionality preservation. We address this gap with a unified, large-scale evaluation of nine state-of-the-art evasion attacks against eight Windows malware detectors, including seven open-source models and one commercial detec...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 26 papers

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

- **2026-09-29** — Longzhu He, Zelang Wen, Xinfeng Li et al. — [Concealing LLM-Based Multi-Agent Topology via Phantom Structure Injection](http://arxiv.org/abs/2609.37567v1)
  <details><summary>📄 Abstract</summary>
  Driven by the rapid advancement of large language models (LLMs), LLM-based multi-agent systems (MAS) have emerged as a powerful paradigm for collaborative reasoning over complex tasks. A key design element of MAS is the communication topology, which governs information flow among agents and often encodes proprietary knowledge about the system architecture. However, recent work has shown that such topologies can be inferred even in black-box settings by exploiting semantic dependencies in observa...
  </details>

- **2026-09-29** — Mohammadali Mohammadkhani, Madhava Krishna, Yash Sarrof et al. — [Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring](http://arxiv.org/abs/2609.37312v1)
  <details><summary>📄 Abstract</summary>
  Can reasoning models trick chain of thought (CoT) monitors and perform hidden computation without revealing it in their thinking traces? We show that the answer depends on the underlying task difficulty and the model size. Simple computations can be performed covertly; however, beyond a threshold depending on model size, successfully solving the task necessarily leaks a near-linear amount of information about the covert task input into the CoT. Therefore, sufficiently complex hidden computation ...
  </details>

- **2026-09-29** — Fangting Zhou, Balazs Kulcsar, Jelena Andric — [From Demand to System Co-Shaping: A Review of User Roles in Transportation Systems](http://arxiv.org/abs/2609.37295v1)
  <details><summary>📄 Abstract</summary>
  Users are central to transportation systems, yet their roles are often simplified in transportation modeling and decision-making. Conventional approaches primarily represent users through demand-related inputs, such as trip flows, delivery requests, and charging loads. However, digital, electrified, and platform-based services create more direct user-system interactions, with users responding to prices, incentives, service availability, and information in ways that can influence operational and ...
  </details>

- **2026-09-29** — Kajetan Ożóg, Alicja Wojciechowska, Dawid Malarz et al. — [LLM unbranding: Erasing Commercial Identity while Preserving Generic Utility](http://arxiv.org/abs/2609.37127v1)
  <details><summary>📄 Abstract</summary>
  Establishing unbranding as a critical practice to prevent visual logos from acquiring negative connotations is standard in image generation. Large Language Models (LLMs) now face a parallel and emerging challenge. These models frequently generate brand descriptions within diverse contexts. This frequency introduces significant risks, such as trademark dilution, false attribution, and brand defamation. In response, we formally define the novel task of LLM Unbranding. We specifically address the c...
  </details>

- **2026-09-29** — Shiqian Zhao, Siwei Jiang, Xinfeng Li et al. — [Practical Secrets Extraction against Black-box LLMs](http://arxiv.org/abs/2609.36941v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly power autonomous coding agents such as Codex and Claude Code, yet their training corpora may contain confidential credentials exposed in public repositories or collected from private development artifacts, creating risks of memorization and subsequent leakage. Existing extraction audits, however, largely assume access to model weights or token probabilities. In this work, we present a black-box secret extraction framework for commercial, API-based LLMs u...
  </details>

- **2026-09-29** — Chong Qi — [NuPaD: A Generative AI Framework for Fostering Deep Learning in Subatomic Physics](http://arxiv.org/abs/2609.36930v1)
  <details><summary>📄 Abstract</summary>
  The rapid adoption of generative artificial intelligence (GenAI) in higher education has introduced a critical pedagogical paradox: while these systems possess extraordinary capacity for information retrieval and synthesis, their default operational mode of supplying immediate, unprompted answers actively undermines the cognitive processes upon which genuine scientific understanding is built. This paper presents NuPaD (Nuclear \& Particle Physics -- Deep Learning Tutor), a novel pedagogical fram...
  </details>

- **2026-09-29** — Hadi Reisizadeh, Jiajun Ruan, Sijia Liu et al. — [Do LLMs Really Forget? Hidden-State Leakage in Model Unlearning and How to Fix it](http://arxiv.org/abs/2609.36612v1)
  <details><summary>📄 Abstract</summary>
  Unlearning in large language models (LLMs) is typically evaluated at the output level, where a model appears to suppress sensitive or undesirable content. In this work, we show that such evaluations can create an illusion of forgetting: even when output-level leakage is eliminated, sensitive information can remain encoded in the model's hidden representations. We first provide a theoretical analysis establishing a fundamental separation between output suppression and representational erasure. Sp...
  </details>

- **2026-09-29** — Parsa Razmara, Woojae Jeong, Aditya Kommineni et al. — [Best Practices in EEG Analysis: Preprocessing, Modeling, and Machine Learning](http://arxiv.org/abs/2609.36609v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) analysis requires careful choices in preprocessing, statistical modeling, and machine learning because EEG signals are highly susceptible to artifacts, volume conduction, low signal-to-noise ratio, and substantial inter-subject variability. This chapter provides a practical and methodological guide to modern EEG analysis, spanning EEG preprocessing, artifact removal, filtering, bad-channel detection and interpolation, re-referencing, independent component analysis (I...
  </details>

- **2026-09-29** — Zhiqi Li, Xiaowei Zhou, Zeyuan Sun et al. — [FM-ReID: Selective Competitive Token Routing for Object Re-Identification](http://arxiv.org/abs/2609.36560v1)
  <details><summary>📄 Abstract</summary>
  Object re-identification (ReID) faces a recurring challenge: different identities can share highly similar global appearances, while the cues that distinguish them are localized, heterogeneous, and visible only under particular viewpoints. This challenge arises in animal ReID through markings, contours, and scars, in person ReID through subtle clothing and accessory cues, and in vehicle ReID through localized appearance details. Although visual foundation models encode such information in dense ...
  </details>

- **2026-09-29** — Lei Ma, Dennis Hofmann, Haowen Xu et al. — [MAADBench: The Refreshable Paradigm for Anomaly Detection in Multi-Agent Systems](http://arxiv.org/abs/2609.36556v1)
  <details><summary>📄 Abstract</summary>
  Recent studies report that LLM-based multi-agent systems (MAS) fail at rates of 41%-87%, yet to our knowledge, no benchmark to date supports systematic anomaly detection (AD) for them. Building MAS AD benchmarks is hard because they must remain fresh as LLM systems evolve: tasks may leak into training data and thus be memorized by LLMs, traces and anomaly patterns expire as backbones evolve, and labels must be provided reliably for each refresh. To address these challenges, we present MAADBench ...
  </details>

- **2026-09-29** — Bravish Ghosh — [Frontier Autolab: Organizational Memory, Adversarial Dissent and Temporal Leakage in Multi-Agent LLM Firms Across Fifty Years of Technological Change](http://arxiv.org/abs/2609.36739v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems are increasingly structured like organizations, with roles, critics and shared memory, yet they are evaluated on tasks that last minutes. We ask how such an organization behaves when the ground it stands on keeps moving. Frontier Autolab is a long-horizon testbed in which one simulated firm, voiced by sixteen role personas and a dedicated Red Team, must re-found itself in nine technology eras from 1990 to 2040. Each era is temporally gated: the firm decides from a dated b...
  </details>

- **2026-09-28** — Louis Tremblay Thibault, Sofiane Azogagh, Marc-Olivier Killijian et al. — [Quantization Enables Private Dense Retrieval against Malicious Service Providers](http://arxiv.org/abs/2609.36376v1)
  <details><summary>📄 Abstract</summary>
  Dense retrieval, the key component of Retrieval Augmented Generation (RAG), retrieves the most relevant documents by comparing dense vector representations of queries and passages from a large corpus. In privacy-sensitive applications, the server observes the query and controls which evidence is returned, creating both confidentiality and integrity risks. We formulate private dense retrieval as providing query privacy and retrieval integrity against a malicious server, and develop a two-round cr...
  </details>

- **2026-09-28** — Lucas Biechy, Cédric Eichler, Héber H. Arcolezi et al. — [PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents](http://arxiv.org/abs/2609.35937v1)
  <details><summary>📄 Abstract</summary>
  While prior work has documented privacy failures in LLM agents, it remains unclear how the presentation of privacy guidance influences their choice of information sources. We introduce PrivacySkills, a controlled framework for evaluating how agents choose among acquisition pathways that provide the same task-relevant value: consulting publicly available personal information, accessing confidential sources, or interacting with the user. The evaluation framework comprises 55 synthetic tasks spanni...
  </details>

- **2026-09-28** — Hao Chen, Wenhui Dong, Ye Chen et al. — [CoSec: Benchmarking Agent Security in Communities](http://arxiv.org/abs/2609.34790v2)
  <details><summary>📄 Abstract</summary>
  LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must complete legitimate tasks and prevent unauthorized disclosure of protected information. Existing evaluations do not fully examine these risks in agent systems. We introduce \textbf{CoSec}, an executable benchmark for evaluating privacy and author...
  </details>

- **2026-09-28** — Shuxing Zhang, Yongquan Ni, Zhenyu Ding et al. — [Privacy-Preserving Full-Body Meshing from mmWave Radar via Mesh Foundation Model Supervision](http://arxiv.org/abs/2609.34768v2)
  <details><summary>📄 Abstract</summary>
  Millimeter-wave (mmWave) radar enables privacy-preserving human perception, but the extreme sparsity of point clouds from commercial single-chip sensors (mean ~6.5 points/frame; ~28% empty frames) has confined prior art to body-part keypoints or discrete action classification. We present a cross-modal teacher-student framework that lifts commercial radar to full-body, per-frame, metric 3D mesh reconstruction with per-joint uncertainty. Three innovations: (1) a mesh-foundation-model teacher - SAM...
  </details>

- **2026-09-28** — Deepthy K. Bhaskar, VP Binu, B Minimol — [Agentic Federated Learning: Rule-Based Client and Server Agents for Adaptive Training](http://arxiv.org/abs/2609.35914v1)
  <details><summary>📄 Abstract</summary>
  Federated Learning (FL) enables collaborative model training across distributed clients without sharing raw data, making it suitable for privacy-sensitive applications such as healthcare, finance, and edge intelligence. However, conventional FL approaches rely on static client participation and fixed aggregation strategies, which limits their effectiveness under non-IID data distributions, heterogeneous client behavior, and noisy or unreliable updates. To overcome these issuess, this paper propo...
  </details>

- **2026-09-28** — Ying Ma, Jarod Govers, Le Fang et al. — ["Black Mirror?": Public Sensemaking of AI-Powered Lifelogging](http://arxiv.org/abs/2609.34950v1)
  <details><summary>📄 Abstract</summary>
  AI-powered lifelogging wearables are emerging as a new class of consumer devices that transform everyday experience into searchable, AI-curated memory archives. We study early public sensemaking around these systems at the moment of their market entry, using the Looki L1 as an empirical lens. Analysing large-scale Chinese-language and English-language social media discourse (N = 5,053 comments), we combine topic clustering with inductive thematic analysis to examine how users interpret the socia...
  </details>

- **2026-09-28** — Hao Chen, Wenhui Dong, Ye Chen et al. — [CoSec: Benchmarking Agent Security in Communities](http://arxiv.org/abs/2609.34790v1)
  <details><summary>📄 Abstract</summary>
  LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must complete legitimate tasks and prevent unauthorized disclosure of protected information. Existing evaluations do not fully examine these risks in agent systems. We introduce \textbf{CoSec}, an executable benchmark for evaluating privacy and author...
  </details>

- **2026-09-28** — Zimeng Huang, Shilei Chen, Jiatong Zhao et al. — [Loyal Agents: Training LLM Agents to Protect Principal Interests Under Strategic Information Asymmetry](http://arxiv.org/abs/2609.34714v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly act as delegated agents, they are expected to protect principals' interests when interacting with external parties. Standard alignment objectives, such as helpfulness, harmlessness, and honesty, do not specify how agents should protect principals' strategic interests under delegation. We formalize Agent Loyalty as an information-control property requiring agents to prevent Exploitable Information Leakage (EIL) and resist Manipulative Information Uptake (MIU). We introduce Lo...
  </details>

- **2026-09-28** — Xinyuan Qian, Yanghao Zhou, Ziyang Jiang et al. — [Multimodal Target Speaker Extraction: Towards Unified Speaker Cues Across Modalities](http://arxiv.org/abs/2609.35613v1)
  <details><summary>📄 Abstract</summary>
  Target Speaker Extraction (TSE) is pivotal in speech communication and human-computer interaction, enabling the isolation of a specific speaker's voice from complex acoustic environments, i.e., the cocktail party scenario. Although traditional TSE systems conditioned on enrollment speech have progressed substantially, enrollment speech as a cue has inherent limitations. Its reliability degrades when the target and interfering speakers have similar voice characteristics, when intra-speaker variab...
  </details>

- **2026-09-28** — Haowen Yang, Sophia Huerta, Yingying Wu — [AI-Assisted Identification of Magnetic Orders and Skyrmions](http://arxiv.org/abs/2609.35566v1)
  <details><summary>📄 Abstract</summary>
  Exotic magnetic orders in two-dimensional (2D) materials are attracting huge interest for energy-efficient spintronic applications, yet realizing robust high-temperature van der Waals antiferromagnets and topological magnetic states remains challenging. In this work, we develop a machine-learning framework for identifying magnetic orders and predicting magnetization using structural, compositional, and electronic information derived from the Materials Project. Fixed-length descriptors are constr...
  </details>

- **2026-09-28** — Qingzhe Bing, Kaiyuan Zhang, Yinqian Zhang — [INTCC: A Framework for Interactive Confidential Computing](http://arxiv.org/abs/2609.35552v1)
  <details><summary>📄 Abstract</summary>
  Confidential computing leverages Trusted Execution Environments (TEEs) to ensure the confidentiality and integrity of data in use. However, TEEs rely on remote attestation to guarantee the integrity of their initial memory state. This model is fundamentally at odds with interactive development workflows. In scenarios like LLM fine-tuning and exploratory data analysis, data processors need human-in-the-loop capabilities, including dynamic code injection, intermediate state inspection, and hyperpa...
  </details>

- **2026-09-28** — Fengzhou Sun, Yuan Zhang, Xintong Yu et al. — [EP-Mem: Elastic Privacy Memory for Social Relationship-Aware LLM Agents](http://arxiv.org/abs/2609.35233v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents face critical privacy risks when acting as delegates in human-agent-human communication. To prevent such breaches, agents must understand users' social relationships and adhere to context-dependent social information disclosure boundaries. Current studies on agent memory privacy focus on instantaneous interactions, leaving the long-term relational disclosure problem unexplored. In this paper, we propose EP-Mem, an Elastic Privacy Memory architecture that reframe...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 17 papers

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

- **2026-09-29** — Benoit Dherin, Michael Munn, Xavier Gonzalvo et al. — [The Safety Operator: Modulating the Expression of Safety Instructions via Spectral Optimization](http://arxiv.org/abs/2609.36434v1)
  <details><summary>📄 Abstract</summary>
  Context tokens in a transformer-based language model can be absorbed into the model's weights as a multiplicative operator. We study this operator in the setting of safety instructions and show that influencing its dominant eigenvalue modulates how strongly the instruction shapes generation. We derive a Contrastive Safety Loss with a suppression weight that controls the tradeoff between emphasizing the safety instruction on harmful queries while suppressing it on harmless queries. Varying the su...
  </details>

- **2026-09-29** — Puning Yang, Qizhou Wang, Junchi Yu et al. — [UnlearningSoup: Is Repeated Tuning Necessary for Large Language Model Unlearning?](http://arxiv.org/abs/2609.37076v1)
  <details><summary>📄 Abstract</summary>
  Large language models trained on vast corpora inherently risk memorizing harmful content that may later re-emerge in their outputs. To mitigate this issue, existing unlearning methods typically rely on training-based parameter updates, such as gradient ascent and its variants, to delete targeted content while preserving other knowledge. However, balancing the competing goals of forgetting and retention makes hyperparameter choices for these methods particularly difficult, often requiring repeate...
  </details>

- **2026-09-29** — Edoardo Bolzoni, Valerio Capraro — [Gender bias across LLMs is common and highly heterogenous](http://arxiv.org/abs/2609.38036v1)
  <details><summary>📄 Abstract</summary>
  Understanding gender biases in large language models (LLMs) is increasingly important as these systems become embedded in decision-support tools with real consequences. Prior research has focused only on a small set of models, leaving open the extent to which gender biases are common and heterogeneous across LLMs. We address this gap across ten models released between April 2025 and June 2026, spanning nine vendors, using two paradigms: gender attribution to stereotyped phrases (Study 1) and mor...
  </details>

- **2026-09-29** — Yaxin Gong, Gangyi Zhang, Chongming Gao et al. — [When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration](http://arxiv.org/abs/2609.36855v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems rely on message passing among specialized agents to accomplish complex tasks. However, an upstream agent may provide useful information or an incorrect answer that causes a downstream agent to override a correct answer supported by its own evidence. Prior work has not clearly separated the benefits of communication from the damage caused by incorrect messages. We study this problem with controlled experiments across five benchmarks and five receivers, keeping the downstre...
  </details>

- **2026-09-28** — Theodore Rogalski, Shirantha Welikala — [Fully Decentralized and Safety-Aware Multi-Agent Reinforcement Learning for Control on Networks](http://arxiv.org/abs/2609.36292v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a safe and fully decentralized multi-agent reinforcement learning (MARL) algorithm to solve a class of discrete-time control problems on networks, including the persistent monitoring problem. Fully decentralized control of agents, while offering numerous benefits, faces issues such as exponentially increasing sample complexity, lack of global information about the system, and challenges in coordinating between agents. To address these issues, this paper introduces a fully dec...
  </details>

- **2026-09-28** — Jianxing Chen, Xiao Yu, Shipra Agrawal et al. — [SCOUT: Synergizing Reasoning and Tool-Use for Computer-Use Safety](http://arxiv.org/abs/2609.36201v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs), while capable of completing computer tasks in everyday and professional workflows, can cause unintended harm even under benign instructions and environments. However, detecting such harm remains challenging. First, it requires careful, task-specific reasoning: verifiers guided only by general safety criteria often overlook many important but subtle harmful behaviors. Second, it requires active investigation: past trajectory screenshots show what the agent did but not ...
  </details>

- **2026-09-28** — David Racovan, Ajay Rawat, Christopher K. May et al. — [Argus: Academic Integrity in the Era of Generative AI](http://arxiv.org/abs/2609.36073v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of large language models (LLMs) in the context of education has introduced significant challenges in enforcement of academic integrity, especially in programming courses. We present Argus, an automated detection system for LLM-assisted student work in undergraduate C programming assignments. Argus integrates behavioral and stylistic indicators to create a holistic picture of the student's progress through an assignment and surfaces anomalies that point to potential misuse...
  </details>

- **2026-09-28** — Bhavik Mangla — [Almost Human, Except When It Matters: VoxParity and the Decisions a Voice Should Change](http://arxiv.org/abs/2609.35922v1)
  <details><summary>📄 Abstract</summary>
  A voice agent can handle almost every call on the words alone and still fail the few its sector's rules were written for. Emergency-call standards, fraud guidance, radio phraseology and vulnerability rules recognise that how a caller sounds, or what else is audible, can change the right action. VoxParity tests whether agents act on it. In 183 scenarios from 14 sectors, one transcript stays fixed while the audio changes (a coaching voice, a medical monitor beeping, a mayday under a radio check, n...
  </details>

- **2026-09-28** — Chenxi Wang, Ruiyang Huang, Li Huang et al. — [How to Tame a Multi-Headed Hydra? Adaptive Multi-Category Safety Steering for Large Language Models](http://arxiv.org/abs/2609.34514v2)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) become increasingly widespread, preventing unsafe responses to harmful prompts is essential for their safe deployment. Activation steering offers an approach to improving LLM safety by modifying internal activations during inference without updating model parameters. However, a single prompt can involve multiple harm categories, and steering toward safety in one category may leave harmful content from another unaddressed. Despite advances in adaptive steering, exi...
  </details>

- **2026-09-28** — Xinjie Shen, Junran Wang, Rongzhe Wei et al. — [SEAD: A State-Based Perspective on Attack and Defense in Tool-Using Agents](http://arxiv.org/abs/2609.34518v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents increasingly use tools to act on external systems. Earlier actions can alter files, permissions, database records, or other state, making a later routine-looking action harmful. Yet the visible interaction may not reveal the underlying state needed to assess that action. We formulate attack and defense as partially observed state control in SEAD, deriving their design requirements from this shared execution process. Because attackers supply instructions while the target cho...
  </details>

- **2026-09-28** — Zhiwei Chen, Tianchun Wang, Zhongtao Rao et al. — [SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing](http://arxiv.org/abs/2609.34342v1)
  <details><summary>📄 Abstract</summary>
  A strong LLM strategic agent should reason prospectively over uncertain futures, adapt its strategy to opponents' behavioral tendencies, and continuously recalibrate its decision process from interaction experience. However, incorporating these sources in free-form reasoning could lead to unsupported strategic assumptions, inconsistent opponent estimates, and harmful interference from irrelevant historical interactions. To address these issues, we propose SAGE, a training-free inference-time fra...
  </details>

- **2026-09-28** — Xu Wang, Difan Zou, Xuansheng Wu — [Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability](http://arxiv.org/abs/2609.35544v1)
  <details><summary>📄 Abstract</summary>
  Reliable refusal of harmful requests is essential to the safe deployment of language models. Because excessive eagerness to please users may undermine existing refusal capabilities, reducing sycophancy offers a potential route to stronger refusal beyond the harmful scenarios covered by safety training. We investigate this possibility using compensatory feature injection (CFI), a training technique designed to limit the acquisition of a target concept by supplying its associated activation during...
  </details>

- **2026-09-28** — Guanxu Chen, Qihao Lin, Jing Shao — [Imprint Reader: From Weight-Update Readout to Behavioral Intervention](http://arxiv.org/abs/2609.35261v1)
  <details><summary>📄 Abstract</summary>
  As language models take a growing role in AI development, a natural aspiration is for them to reflect on their own learning process, as humans do, and use that reflection to improve themselves. At the same time, these models have an advantage that human learners lack, since training leaves parameter-level traces that can, in principle, be inspected directly. However, current models cannot decode these traces into an explicit account of what they have learned. To this end, we introduce the \texti...
  </details>

- **2026-09-28** — Abel Rodríguez, Giuseppe Garofalo, Lieven Desmet et al. — [Tool Mediation Alters Refusal Mechanisms in Large Language Models](http://arxiv.org/abs/2609.35117v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed with access to external tools, yet harmful tool-mediated interactions are less likely to be refused when compared to regular conversational ones. As this change in refusal behavior remains underexplored, we investigate its underlying mechanisms across a diverse set of open-weight language models. We find that information about the harmfulness of a request remains strongly encoded in the model's representations and transfers across conversati...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-09-28** — Dmitrii Kharlapenko, Sergei Bratchikov, Konstantin Korolev et al. — [RISE: Red-teaming via Iterative Strategy Evolution for Modern Text-to-Image Models](http://arxiv.org/abs/2609.34920v1)
  <details><summary>📄 Abstract</summary>
  On modern production text-to-image systems, successful policy violations are rare, and previously effective human-written seeds are often patched out. Current automated red-teamers are poorly matched to this regime in two ways: unreliable success measurement and poor exploration. First, we find that judges widely used in prior T2I red-teaming work are unreliable under vague unsafe-content targets: they either miss true violations or reward benign borderline images on hardened APIs. We therefore ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 68 papers

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

- **2026-09-29** — Zhenghao He, Guangzhi Xiong, Sanchit Sinha et al. — [Rethinking Reasoning Paths as Phase-Structured Trajectories](http://arxiv.org/abs/2609.36461v1)
  <details><summary>📄 Abstract</summary>
  Large language models often improve problem-solving performance by generating multi-step reasoning paths, yet how to analyze the hidden states along these paths remains unclear. Existing approaches typically assign each intermediate state the final-answer correctness label and train probes across heterogeneous questions. We argue that this protocol obscures reasoning dynamics in two ways: (1) correctness prediction can exploit question-level variation rather than path quality, and (2) states ali...
  </details>

- **2026-09-29** — Mahmoud Abdelgalil, Miroslav Krstic, Jorge I. Poveda — [Non-Holonomic Gradient Play: Leafwise Nash Equilibria, Stability, and Deception](http://arxiv.org/abs/2609.38051v1)
  <details><summary>📄 Abstract</summary>
  We study generalized learning dynamics in multi-agent systems whose joint state evolves on a manifold and whose agents act through state-dependent, potentially nonholonomic vector fields. Under a bundle-splitting condition, we show that these dynamics admit an intrinsic representation as projected Riemannian gradients, giving rise to a class of \emph{nonholonomic gradient play} dynamics. We characterize the local stability of its equilibria through an intrinsic linearization that explicitly capt...
  </details>

- **2026-09-29** — Ahmed Nader Ahmed, Omar Moured, Mughni Irfan Mohammed Abdul et al. — [ProAct-VLM: Pre-Failure Vision-Language Task Replanning with Continuous Perception Feedback](http://arxiv.org/abs/2609.37681v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic tasks are vulnerable to unexpected environmental changes that can render planned actions ineffective or unsafe. To address this, robots must detect such changes as they occur, interpret their impact, and adjust their actions accordingly. Traditional rule-based decision-making pipelines are brittle in open-world conditions, as they are hand-tuned for specific scenarios and lack generalization. Vision-Language Models (VLMs) offer a promising alternative as they combine broad w...
  </details>

- **2026-09-29** — Yaxin Zhao, Dianye Huang, Chenwei Wang et al. — [Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies](http://arxiv.org/abs/2609.37307v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have driven rapid progress in robotic manipulation, demonstrating strong fine-grained control and promising performance on long-horizon tasks. However, many existing VLAs lack explicit access to interaction history, making them vulnerable to perceptual aliasing: similar current observations and robot states at different task stages may induce action ambiguity and lower success rate. Existing methods incorporate temporal or progress cues through feature conditi...
  </details>

- **2026-09-29** — Panagiotis Theodoropoulos, Nan Jiang, Xintong Duan et al. — [Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via Sampling](http://arxiv.org/abs/2609.38104v1)
  <details><summary>📄 Abstract</summary>
  Power-sharpened sampling is an inference-time alternative to reinforcement-learning (RL) post-training for enhancing reasoning in large language models (LLMs). High-probability sequences are amplified under the base model without parameter updates or external rewards, avoiding the costly optimization and jagged generalization of RL. However, this approach faces a fundamental exploration--exploitation trade-off, as % strong sharpening restricts exploration, trapping samplers in plausible but inco...
  </details>

- **2026-09-29** — Bilal Hassan, Areg Karapetyan, Samer Madanat — [A Model-Agnostic Physics-Guided Adapter for Few-Shot Transfer of Coastal Flood Prediction Models to Unseen Regions](http://arxiv.org/abs/2609.37565v1)
  <details><summary>📄 Abstract</summary>
  Deep learning surrogates can produce high-resolution coastal flood maps orders of magnitude faster than physics-based hydrodynamic simulators, yet transferring them to new coastal regions remains costly, since generating target-region data for fine-tuning typically requires numerous time-consuming simulations. To tackle this bottleneck, we introduce the Physics Adapter (PA), a compact, architecture-agnostic adaptation interface that enables efficient few-shot transfer of flood prediction models ...
  </details>

- **2026-09-29** — Hongyang Li, Xiao Li, Caesar Wu et al. — [Unlocking the Critic: Reward-Free Policy Optimization for LLM Post-Training](http://arxiv.org/abs/2609.37119v1)
  <details><summary>📄 Abstract</summary>
  Recent approaches to reinforcement learning (RL) post-training for large language models increasingly remove the critic to reduce training instability and memory overhead. Even where a critic is trained, it is discarded once training ends, although it has learned to predict outcomes. We revisit this trend and show that a pretrained critic's ability to predict future outcomes can make it a valuable asset for efficient long-horizon reasoning. First, we find that instability in critic-based RL for ...
  </details>

- **2026-09-29** — Suhani Grover, Astik Srivastava, Viswas Dinesh et al. — [GlassFormer: Learning Real-time Glass Segmentation using Radar-Depth Fusion](http://arxiv.org/abs/2609.36844v1)
  <details><summary>📄 Abstract</summary>
  Transparent surfaces are ubiquitous in built environments, yet they remain a persistent failure case for robotic perception. RGB cameras perceive the background behind glass rather than the surface itself, while depth sensors such as LiDAR, time-of-flight, and RGB-D often return invalid or background measurements in transparent regions. As a result, systems that rely solely on optical sensing may misinterpret glass walls, doors, or mirrors as free space, compromising safe and reliable navigation...
  </details>

- **2026-09-28** — Mehdi Makni, Ryan Lucas, Rahul Mazumder — [ThinQuant: Scalable Rotation Learning for Weight and Activation Quantization of LLMs](http://arxiv.org/abs/2609.36120v1)
  <details><summary>📄 Abstract</summary>
  Learned rotations play an important role in enabling low-bit weight and activation quantization of large language models by smoothing outliers in the activation distribution. State-of-the-art approaches include gradient-based procedures such as SpinQuant and computationally friendlier gradient-free approaches such as DartQuant, but both remain hard to scale to the largest architectures. To address the computational bottlenecks in gradient-free rotation learning, we introduce two ideas for effici...
  </details>

- **2026-09-28** — Yihao Wang, Linhan Xia, Rui Liu et al. — [SAGE: A Statistical Acceptance Gate for Self-Evolving Agents](http://arxiv.org/abs/2609.36043v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based agents increasingly self-evolve by editing a persistent skill document that encodes their workflow, tool-use rules, and decision logic. This loop has two steps, an optimizer that proposes a candidate edit and a gate that accepts or rejects it. Prior work has concentrated on the optimizer, while the gate still follows a naive rule that keeps any edit which improves an aggregate validation score. We show that this rule fails in two ways. First, it admits permanent ...
  </details>

- **2026-09-28** — Chong Wang, Zixuan Fu, Shiqi Huang et al. — [Persistence Forcing: Exploiting Feature Specialization in Pixel-Space Diffusion](http://arxiv.org/abs/2609.36014v1)
  <details><summary>📄 Abstract</summary>
  Pixel-space diffusion Transformers (DiTs) directly operate on high-dimensional visual data, yet their hidden representations typically undergo uniform refinement across depth. Natural images, however, are inherently organized at different levels of granularity. Global structure can often be represented compactly, whereas local textures and fine details require richer representations. Motivated by this, we introduce heterogeneous refinement in pixel-space DiTs, assigning different feature groups ...
  </details>

- **2026-09-28** — Luke Leckie, Peter M. Todd, Jacob G. Foster — [Signatures of semantic search in the activations of large language models](http://arxiv.org/abs/2609.35599v2)
  <details><summary>📄 Abstract</summary>
  When recalling lists of concepts (e.g., animals) during the semantic fluency task (SFT), both humans and large language models (LLMs) organise their output into clusters of related items (e.g., sea animals) that are punctuated by strategic switches between clusters. In humans, this pattern can be explained by a semantic foraging process, whereby distinct neural and behavioural signatures accompany within-cluster production ("exploit") and between-cluster switching ("explore"). Whether LLMs likew...
  </details>

- **2026-09-28** — Kaikai Zhang, Zihan Zhang, Yuchong Xie et al. — [Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery](http://arxiv.org/abs/2609.35909v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents turn vulnerability discovery into a repository-scale search: they generate many vulnerability hypotheses but can verify only a subset under a finite budget. We show that autonomous vulnerability discovery exhibits a hypothesis-verification asymmetry, where verifying a candidate hypothesis through reachability analysis, execution, and proof-of-concept construction is substantially more expensive than forming it. Under a finite resource budget, this makes autonomous discovery...
  </details>

- **2026-09-28** — Ruibo Chen, Zhengmian Hu, Donghang Lu et al. — [TTMark: Pairwise Distortion-Free Watermarking Beyond Single-Token Entropy](http://arxiv.org/abs/2609.36372v1)
  <details><summary>📄 Abstract</summary>
  Distortion-free watermarking enables reliable attribution of machine-generated text while preserving output distribution. However, existing methods operate independently on each generated token, making their detection capability fundamentally constrained by the entropy of the next-token distribution. We present Tandem Token WaterMark (TTMARK), a general pairwise watermarking framework that extends distortion-free watermarking from individual tokens to adjacent token pairs. By watermarking the jo...
  </details>

- **2026-09-28** — Yishu Li, Liyuan Geng, Xinyi Mao et al. — [Scouting the Dynamics Gap: Test-Time Policy Adaptation via Action-Outcome Feedback](http://arxiv.org/abs/2609.36107v1)
  <details><summary>📄 Abstract</summary>
  While pretrained robotic policies exhibit impressive capabilities in controlled environments, unobserved physical properties and dynamics require these policies to rapidly adapt during deployment. Existing test-time adaptation methods typically rely on sparse scalar rewards, failing to exploit the rich geometric and dynamic feedback from the environment during physical interaction. To address this challenge, we propose SCOUT, a dynamics-aware meta-learning framework that enables manipulation pol...
  </details>

- **2026-09-28** — Yiyang Li, Sai Shankar Narasimhan, Priam Alataris et al. — [ALF: Spectrally Anchored Latent Flow Matching](http://arxiv.org/abs/2609.36385v1)
  <details><summary>📄 Abstract</summary>
  Wireless time-series generation is useful for emerging applications that will drive the adoption and integration of machine learning tasks within next-generation networks, such as waveform classification in shared spectrum bands and interpretation of the physical world through integrated sensing and communications. Unlike a generic time series, wireless signals have time-frequency duality, where a frequency domain bandwidth constraint implicitly imposes latent structural constraints on the evolu...
  </details>

- **2026-09-28** — Wenxin Shao, Siqi Chai, Kun Li et al. — [Humanoid Loco-Manipulation With Discrete VLA Model](http://arxiv.org/abs/2609.35709v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models using discrete action tokens have proven effective for controling robotic arms on manipulation tasks. For a humanoid, however, the whole-body action space -- legs, torso, arms, and hands -- is far higher-dimensional and heterogeneous, raising tokenization, training, and real-time inference challenges that the previous VLA models do not address. We present Holo-M, to our knowledge the first discrete VLA model for humanoid loco-manipulation that intrinsically ex...
  </details>

- **2026-09-28** — Priyanka Kargupta, Silviu Cucerzan, Shweti Mahajan et al. — [Reinforcing Agentic Creativity in Scientific Ideation with Night Science](http://arxiv.org/abs/2609.35706v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) excel at structured, verifiable tasks, but their low-entropy bias can produce homogeneous and predictable outputs, limiting their utility for open-ended scientific ideation. Effective discovery, however, spans a broader creative spectrum: from structured day science to loosely structured, serendipitous night science that reaches ideas beyond those typically considered. We introduce AI Night-Scientist, an agentic framework that uses reinforcement learning to teach mod...
  </details>

- **2026-09-28** — Qiyao Ma, Junshan Zhang, Zhe Zhao — [Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking Models](http://arxiv.org/abs/2609.35695v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) to diverse user preferences is fundamentally hindered by standard alignment paradigms that optimize for monolithic users. In this work, empirical studies are first used to reveal the existence of a massive, untapped performance headroom for personalized generation through test-time alignment. We demonstrate that personalized generation is uniquely suited for test-time scaling methods like Best-of-N (BoN) because it can be viewed primarily as a candidate matc...
  </details>

- **2026-09-28** — Pedro R. A. S. Bassi, Wenxuan Li, Hanxue Gu et al. — [RT-Super: Learning Tumor Segmentation from Longitudinal Images and Reports](http://arxiv.org/abs/2609.35637v1)
  <details><summary>📄 Abstract</summary>
  Multi-tumor segmentation is important for early cancer detection and allows radiologists to visualize, verify, and understand AI predictions. However, tumor segmentation masks are expensive, time-consuming, and unavailable for many tumor types in public data. Instead, hospitals have vast, readily available data that can guide segmentation: radiology reports, longitudinal images, and multi-phase images. We use this readily available data to substitute for tumor masks in training AI for tumor segm...
  </details>

- **2026-09-28** — Nazim Bendib, Nicolas Perrin-Gilbert, Olivier Sigaud — [Behavioral Foundation Models for Quality Diversity](http://arxiv.org/abs/2609.35615v1)
  <details><summary>📄 Abstract</summary>
  Behavioral Foundation Models (BFMs) are an emerging paradigm in reinforcement learning, playing a role analogous to large language models in natural language processing: they have shown remarkable versatility, enabling zero-shot performance, fast imitation, and online adaptation, all by exploiting the structure of a latent space. In this work, we investigate whether the latent behavioral space induced by BFMs can serve as an effective search space to discover large repertoires of behaviorally di...
  </details>

- **2026-09-28** — Luke Leckie, Peter M. Todd, Jacob G. Foster — [Signatures of semantic search in the activations of large language models](http://arxiv.org/abs/2609.35599v1)
  <details><summary>📄 Abstract</summary>
  When recalling lists of concepts (e.g., animals) during the semantic fluency task (SFT), both humans and large language models (LLMs) organise their output into clusters of related items (e.g., sea animals) that are punctuated by strategic switches between clusters. In humans, this pattern can be explained by a semantic foraging process, whereby distinct neural and behavioural signatures accompany within-cluster production ("exploit") and between-cluster switching ("explore"). Whether LLMs likew...
  </details>

- **2026-09-28** — Yaxin Du, Xiyuan Yang, Zhifan Zhou et al. — [RSI-Master: Structuring Experiments to Guide Autonomous Model Improvement](http://arxiv.org/abs/2609.35561v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) seeks to enable AI systems to participate in improving their own capabilities. A concrete pathway is autonomous model development, where agents iteratively explore post-training strategies to improve a base model. This setting faces two challenges: agents may exploit open-ended experimental actions through hacking, and repeated experimentation may lead to strategy lock-in, where an early direction is refined rather than reconsidered. We introduce RSI-Master, whic...
  </details>

- **2026-09-28** — Ruishuo Chen, Weijia Li, Xun Wang et al. — [One Proposal for Every Margin: Zero-Shot Amortized Sequential Importance Sampling for Binary Matrices](http://arxiv.org/abs/2609.35514v1)
  <details><summary>📄 Abstract</summary>
  In ecology, psychometrics, and the analysis of social and financial networks, binary matrices are often analyzed conditional on their observed row and column sums, which restricts the problem to a finite sample space of matrices with the same margins. Two fundamental problems are to count this space and to sample uniformly from it. Sequential importance sampling (SIS) addresses both with independent weighted samples and an unbiased count estimator, but its efficiency depends critically on the pr...
  </details>

- **2026-09-28** — Joni Herttuainen, Kirsi Hellsten, Vesa Kuikka et al. — [AI-Based Vulnerability Assessment Capability and Cyber Attack Graph Analysis](http://arxiv.org/abs/2609.35414v1)
  <details><summary>📄 Abstract</summary>
  Cyber threats targeting mission-critical infrastructure are becoming more sophisticated while the barrier to launching attacks continues to fall. Traditional point solutions like antivirus and firewalls are reactive and fail to address the combinatorial complexity of modern attack surfaces. This paper presents an investigation combining two complementary methodologies: Lockheed Martin's Vortex/Crow framework, which applies multi-agent reinforcement learning (MARL) over industry-standard cyber kn...
  </details>

- **2026-09-28** — Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom et al. — [Epistemic Policy Divergence in Multi-Turn LLM Contamination: A Protocol-Gradient Investigation](http://arxiv.org/abs/2609.35308v1)
  <details><summary>📄 Abstract</summary>
  Large language models process conversation history as unverified context: false premises injected into prior turns can be adopted as fact, a failure mode we term session-level contamination. We introduce five contamination protocols arranged along a source-authority gradient, isolating distinct failure mechanisms while holding the false premise constant, and evaluate GPT-5.4 Mini, Gemini-3.1 Flash-Lite, and GLM-4.5-Air across ten knowledge domains at temperature zero (22,500 turns), using a dual...
  </details>

- **2026-09-28** — Yilun Qiu, Xiaoyan Zhao, Chengbing Wang et al. — [Rubric-Aware On-Policy Self-Distillation for LLM Personalization](http://arxiv.org/abs/2609.35262v1)
  <details><summary>📄 Abstract</summary>
  LLM personalization aims to generate responses aligned with individual users' preferences and needs. User-specific rubrics make these expectations explicit, providing direct supervision on what a satisfactory answer should cover. Existing rubric-guided approaches, however, exploit such guidance only at a coarse granularity, either by using rubrics to supervise the prediction of relevant aspects for subsequent generation or by reducing aspect coverage to a single response-level reward for reinfor...
  </details>

- **2026-09-28** — Prateek Kumar Rajput, Abdoul Kader Kabore, Yewei Song et al. — [Trajectory-Level Security Debt in LLM Coding Agents](http://arxiv.org/abs/2609.35199v1)
  <details><summary>📄 Abstract</summary>
  LLM coding agents can traverse hundreds of intermediate code states before submitting a solution. Evaluating only the final artifact leaves the evolution of security findings unmeasured. We introduce the Security Debt Line Integral (SDLI), which accumulates static-analysis risk when an agent reaches a new best test pass ratio. We instantiate it with four static application security testing (SAST) tools and study artifacts from 830 passing SWE-bench runs, 712 ProgramBench final workspaces, and 13...
  </details>

- **2026-09-28** — Jiaan Zhu, Wei Gao, Youhui Bai et al. — [PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning](http://arxiv.org/abs/2609.35158v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn rollout dominates the cost of agentic reinforcement learning (RL). Asynchronous execution and elastic GPU resources can accelerate this stage, but adding rollout replicas yields diminishing returns while training GPUs remain idle between updates. We observe that effective resource use also depends on the prefill--decode (PD) configuration. Both the choice between colocation and disaggregation and the optimal PD ratio vary with the workload, making resource scaling and PD configuration...
  </details>

- **2026-09-28** — Fida M. Thoker, Renaud Vandeghen, Karen Sanchez et al. — [Advancing Video-Text Pretraining with Multi-View Captions](http://arxiv.org/abs/2609.35090v1)
  <details><summary>📄 Abstract</summary>
  Video-text pretraining has achieved remarkable progress through the scaling of models and datasets, yet the quality of language supervision remains underexplored. Existing web-scale datasets often provide only a single sparse caption per video that fails to capture rich spatiotemporal semantics, while directly using captioning models can generate noisy descriptions. We propose a large-scale multimodal large language model-based supervision generation framework that improves supervision diversity...
  </details>

- **2026-09-28** — Zeqin Liao, Yuhong Nan, Henglong Liang et al. — [SmartMemory: Detecting On-chain-off-chain Communication Inconsistency for Smart Contract via Memory-based Agent](http://arxiv.org/abs/2609.34983v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts underpin decentralized finance, where growing demand for on-chain/off-chain communication(OFC) has driven diverse applications such as cross-chain bridges, real-world asset tokenization, and fiat-backed stablecoins. TheOFC-related security incidents in these applications are increasingly frequent, but prior studies address separate vulnerability categories within OFC applications rather than providing a unified view, causing vulnerabilities outside known patterns to be missed.In ...
  </details>

- **2026-09-28** — Zijian Dai, Sen Han, Youhui Bai et al. — [WaveAlign: Cache-Aware Query-Row Scheduling for Sparse Attention in Long-Video Generation](http://arxiv.org/abs/2609.34814v1)
  <details><summary>📄 Abstract</summary>
  Long-video generation with diffusion transformers (DiTs) produces extremely long token sequences, making attention a dominant inference bottleneck. Dynamic sparse attention reduces computation, but its realized speedup remains limited because irregular query-row execution degrades L2 cache locality and increases HBM traffic. We present WaveAlign, a lightweight, cache-aware query-row reordering framework for dynamic sparse attention. WaveAlign formulates row ordering as an optimization problem an...
  </details>

- **2026-09-28** — Minchan Kang, Kyeonghye Park, Seungyeon Sa et al. — [Beyond Reconstruction Loss in Post-Training Quantization: Balanced Fitting for Large Vision-Language Models](http://arxiv.org/abs/2609.34765v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) enables efficient deployment of large vision-language models (LVLMs), but is typically calibrated on a small set while expected to generalize across diverse downstream tasks. Although recent PTQ methods for LVLMs incorporate sensitivity signals, they still minimize reconstruction loss with respect to the full-precision model, potentially over-preserving FP behavior and calibration-specific bias. Rather than treating quantization solely as an error to be minimized...
  </details>

- **2026-09-28** — Zhen Wang, Changpeng Wang, Zhe Liu et al. — [PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation](http://arxiv.org/abs/2609.34759v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models (VLMs) have advanced vision-and-language navigation (VLN), enabling models to predict navigation actions from visual observations and language instructions. In this work, we explore VLN with panoramic observations and introduce PanoVLN. The motivation is straightforward: more complete visual context should enable better-informed navigation decisions. For example, a panorama can reveal a passage outside a perspective camera's field of view, allowing the model to iden...
  </details>

- **2026-09-28** — Alexandre Declèves, Etienne Boursier, Nicolas Flammarion — [Statistical Benefits of Fine-Tuning from Pretrained Initialization in Diagonal Linear Networks](http://arxiv.org/abs/2609.34756v1)
  <details><summary>📄 Abstract</summary>
  Adapting pretrained models to downstream tasks with limited data has become a central paradigm in modern deep learning. Yet, despite its widespread practical success, how fine-tuning leverages information from pretraining remains poorly understood theoretically. We study fine-tuning from pretrained weights through the lens of sparse linear regression and two-layer diagonal linear networks. In our setting, pretraining provides information through the support (and signs) of the initialization pred...
  </details>

- **2026-09-28** — Thorsten Feldmann, Jack Jenkins, Jaime del Palacio Lirola — [Soft-Collinear Chiral Perturbation Theory for $B \to π$ form factors at large recoil](http://arxiv.org/abs/2609.34696v1)
  <details><summary>📄 Abstract</summary>
  We develop an effective hadronic theory for heavy-meson decays into energetic pions, organized by the approximate heavy-quark and chiral symmetries. The dynamical degrees of freedom of the theory consist of quasi-static heavy-meson fields coupled to soft and collinear pions, relevant for exclusive $B \to π$ transitions at large recoil energy ${E_π\simeq M_B/2}$. Our approach exploits the factorization of soft and collinear quarks in Soft-Collinear Effective Theory (SCET), leading to an emergent ...
  </details>

- **2026-09-28** — Moongyu Jeon, Dongjae Jeon, Bumjun Kim et al. — [Low-Confidence Remasking Traps Flexibility: Realizing Arbitrary-Order Potential for Diverse Rollouts in Diffusion LLMs](http://arxiv.org/abs/2609.34509v1)
  <details><summary>📄 Abstract</summary>
  Masked diffusion language models support arbitrary-order generation, suggesting a natural way to produce diverse outputs. However, recent work argues that this flexibility reduces diversity by delaying high-uncertainty tokens that can lead to different generation paths. We trace this diversity loss not to arbitrary-order generation itself, but largely to low-confidence remasking (LCR), a widely used decoding rule. At each step, LCR samples a token at every masked position but commits only the sa...
  </details>

- **2026-09-28** — Ayana Mussabayeva, Anuar Aimoldin, Olivier Oullier et al. — [PhysioTRACE: Provenance-Aware Stress Tests for Physiological Foundation Models](http://arxiv.org/abs/2609.34466v1)
  <details><summary>📄 Abstract</summary>
  Physiological foundation models encode how a signal was recorded alongside the physiology it reflects. When recording conditions are associated with diagnosis, this acquisition provenance can become a shortcut, yet the usual evidence, shifted transfer and provenance decodability, does not show whether a predictor uses it. We introduce PhysioTRACE, a four-axis behavioral audit for frozen encoders that separates what a probe can decode from what a fixed task head relies on. Recover scores how deco...
  </details>

- **2026-09-28** — Yekun Xu, Ante Wang, Jingyi Ren et al. — [When Words Fall Short: Iterative Synergy Between Verbalized Reasoning and Hidden Features for LLM Confidence Estimation](http://arxiv.org/abs/2609.34454v1)
  <details><summary>📄 Abstract</summary>
  Confidence estimation is crucial for developing trustworthy large language models (LLMs), with most methods following estimator-based or verbalization-based paradigms. While recent research increasingly focuses on improving verbalized self-reports of confidence, we challenge the prevailing view that this approach surpasses independent confidence estimators. Our empirical study shows that a dedicated confidence estimator can substantially outperform verbalized confidence, indicating that LLMs' in...
  </details>

- **2026-09-28** — Liang He, Sheng Wu, Haomiao Hao et al. — [ReproBench: Benchmarking LLM Agents on Reproducing Vulnerability From Scratch](http://arxiv.org/abs/2609.34450v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly evaluated on cybersecurity tasks such as vulnerability reproduction, exploitation, and patching. However, existing cybersecurity benchmarks predominantly operate under a post-environment evaluation paradigm, i.e., handing the agent source code, a container, or an executable binary. This setup bypasses the critical environment reconstruction step, leaving a fundamental question for real-world vulnerability analysis: can an agent autonomously reco...
  </details>

- **2026-09-28** — Jialu Wang, Peizhi Niu, Haoteng Yin et al. — [Making LLMs Truly Forget: Deep Unlearning by Searching, Selecting, and Severing Knowledge Paths](http://arxiv.org/abs/2609.34442v1)
  <details><summary>📄 Abstract</summary>
  While an unlearned language model may no longer recall a fact directly, the fact often remains recoverable through multi-hop reasoning over related knowledge. Most existing unlearning techniques overlook this vulnerability, targeting facts in isolation while leaving their supporting knowledge intact. To achieve true forgetting, we propose a general deep unlearning framework compatible with existing unlearning algorithms. Our approach adaptively explores both explicit responses and latent interna...
  </details>

- **2026-09-28** — Yingjie Qi, Cenlin Duan, Yiou Wang et al. — [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation](http://arxiv.org/abs/2609.34351v1)
  <details><summary>📄 Abstract</summary>
  Digital Compute-in-Memory (CIM) presents a promising solution for accelerating deep neural networks (DNNs) through the integration of computational logic directly within memory arrays. However, mapping modern DNN operators to CIM accelerators often results in severe array underutilization, due to the strict data reuse constraints imposed by the rigid CIM array structure. We observe that data reuse in modern DNNs forms hyperplane structures often oriented along non-axial directions, rendering the...
  </details>

- **2026-09-28** — Weijun Luo, Kelvin Luu, Xinyi Liu et al. — [Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes](http://arxiv.org/abs/2609.34262v1)
  <details><summary>📄 Abstract</summary>
  Agentic benchmarks guide model selection and training. Yet an agent can pass a task without demonstrating the intended capability. Such outcomes constitute unearned passes; their proportion among all passes defines the integrity gap. As agents improve, benchmark surfaces that once seemed harmless can become exploitable, making benchmark validity an ongoing maintenance problem. We introduce a process-verification framework that audits passing trajectories, distinguishes evidenced reward hacking f...
  </details>

- **2026-09-28** — Qiyong Zhong, Mao Zheng, Mingyang Song et al. — [MAS-OPD: On-Policy Distillation for Multi-agent Systems](http://arxiv.org/abs/2609.34234v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) split a task across specialized roles and are promising on complex tasks, yet a prevailing approach relies on inference-time orchestration alone. General-purpose APIs are costly and hard to customize, while small models with role prompts rarely develop stable role competence or reliable collaboration, so post-training a MAS jointly is central. Most attempts use reinforcement learning, whose team-level reward leaves undetermined which step of which agent brought about th...
  </details>

- **2026-09-28** — Hong Zhang, Zhongjie Duan, Yingda Chen — [EntroPack: Fast and Accurate Entropy-Coded Weight Compression at Arbitrary Bitrates](http://arxiv.org/abs/2609.34185v1)
  <details><summary>📄 Abstract</summary>
  Weight compression helps large neural networks fit deployment memory budgets, but common fixed-width formats offer only coarse storage choices. Entropy coding supports finer rates, yet the achieved size depends on the quantized weight distribution and coding overhead. Exploiting this flexibility requires accurate rate selection and efficient weight reconstruction for inference. We present EntroPack, an entropy-coded weight compressor that supports arbitrary target bitrates without activation cal...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 48 papers

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

- **2026-09-29** — Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani — [LLMs Learn to Evade Latent Monitors from Prior Feedback Alone](http://arxiv.org/abs/2609.36490v1)
  <details><summary>📄 Abstract</summary>
  Latent space monitors aim to detect undesired behaviors in LLM agents by inspecting an agent's internal activations rather than its outputs. However, interactive monitoring creates a feedback channel where each verdict the monitor delivers leaks information to the model about how its internal states are being evaluated. We ask whether an agent can infer the monitor's decision rule from this feedback and then selectively edit its activations to evade detection. Unlike prior evasion attacks, the m...
  </details>

- **2026-09-29** — Hongzhu Guo, Mohsen Fayyaz, Nanyun Peng — [From Routing Signals to Selective Review: Visual regrounding in MoE VLMs](http://arxiv.org/abs/2609.38111v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) may accept false visual premises, answering questions about a target object's color, count, location, or state even when it is absent. We call this reliability-critical behavior a target-absence grounding failure. Existing visual-grounding detectors primarily rely on generated responses, hidden states, or uncertainty measures. We present the first framework to leverage internal routing decisions in Mixture-of-Experts (MoE) VLMs to detect target absence before genera...
  </details>

- **2026-09-29** — Bingxuan Li, Siqi Song, Yizhuo Wu et al. — [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](http://arxiv.org/abs/2609.38078v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have advanced robotic manipulation, but their zero-shot generalization in new tasks and environments remains limited, and their reliance on specialized training keeps them from benefiting directly from rapidly advancing general-purpose vision-language models (VLMs). In parallel, recent agentic robotic systems leverage VLMs for high-level reasoning or coding agents for robot control, but often depend on extensive external models and tools, introducing additiona...
  </details>

- **2026-09-29** — Mahsa Abdollahi, Nico Coallier, Maxime Fraser Franco et al. — [Acoustic Honeybee Queen-State Detection Under Unseen Conditions](http://arxiv.org/abs/2609.37845v1)
  <details><summary>📄 Abstract</summary>
  Honeybee queen loss is a major threat to colony health, yet queen-status assessment remains largely manual and disruptive. Acoustic monitoring offers a non-invasive alternative by enabling continuous analysis of hive sounds. In this paper, we benchmark conventional and learned acoustic representations for automated detection of queen absence, comparing task-specific convolutional neural networks with pretrained audio transformers. Experiments are performed on 5,129 audio recordings from 3,285 hi...
  </details>

- **2026-09-29** — Wenbin Shen, Guoxuan Qin, Guangxu Yao et al. — [Rethinking Multimodal Fake News Detection in the Generative AI Era](http://arxiv.org/abs/2609.36850v1)
  <details><summary>📄 Abstract</summary>
  Generative content is increasingly entering the production and dissemination of news, transforming fake news from manually fabricated or simply manipulated material into complex forms in which native and generated content jointly participate. Existing multimodal fake news detection research primarily focuses on veracity assessment and rarely characterizes how generativity differences affect the reliability of evidence. In contrast, AIGC detection primarily determines whether content is generated...
  </details>

- **2026-09-29** — Michele Antonazzi, Alejandra C. Hernandez, José Araujo et al. — [When to Adapt: Multi-Signal Domain Shift Detection for Efficient Training-Free Adaptation in Open-Vocabulary Segmentation](http://arxiv.org/abs/2609.37602v1)
  <details><summary>📄 Abstract</summary>
  Robust and reliable perception is essential for autonomous robots operating in real-world environments, particularly in long-term missions where environmental conditions may change significantly over time. Although recent advances in Visual Foundation Models (VFMs) have improved open-vocabulary semantic segmentation, these models can still suffer from domain shift, which can significantly degrade performance if they are not adapted to the current environment. Training-free domain adaptation is a...
  </details>

- **2026-09-29** — Annabelle K. L. Chua, Forster J. Khoo, Joel C. R. Tan et al. — [Look What You Made Us Cluster: Hate Narrative Extraction from Reddit Discourse](http://arxiv.org/abs/2609.37408v1)
  <details><summary>📄 Abstract</summary>
  Narrative extraction allows us to identify online hate narratives, supporting the construction of rigorous detection systems. Existing computational approaches, however, are limited in precision as they rely on semantic representations, which tend to capture only surface-level meaning. To detect more precise and interpretable narratives, we present an extraction pipeline that represents narratives as entity-evaluation pairs. Narratives are extracted using a Large Language Model (LLM) reasoning p...
  </details>

- **2026-09-29** — Li Pang, Xinqiao Wu, Jing Yao et al. — [HyperSAM: A Promptable Foundation Model for Hyperspectral Remote Sensing](http://arxiv.org/abs/2609.37340v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral remote sensing provides dense spectral measurements that are indispensable for material-level Earth observation, yet the construction of a general-purpose hyperspectral foundation model remains difficult. Two bottlenecks are especially limiting. First, large hyperspectral corpora rarely provide high spatial resolution together with reliable dense annotations. Second, many hyperspectral models are still trained almost from scratch, so the geometric and interactive priors learned by ...
  </details>

- **2026-09-29** — Nicholaus Dismas Ladislaus, Olatunji Damilare Emmanuel, Samuel Chol Buol — [The Vote Hides the Failure: Aggregation Choice and Noise Robustness in Heart Murmur Detection](http://arxiv.org/abs/2609.37161v1)
  <details><summary>📄 Abstract</summary>
  Noise robustness in automated phonocardiogram (PCG) murmur detection, and how it is measured, remains underexamined despite growing interest in low-resource screening. We evaluate two independently reimplemented pipelines, Hierarchical Multi-Scale Convolutional Network (HMS-Net)--CNN, and Bidirectional Long Short-Term Memory (BiLSTM)--LSTM, under controlled, multi-severity noise with noise-augmented fine-tuning and held-out generalization testing. Under matched aggregation, the complete BiLSTM p...
  </details>

- **2026-09-29** — Zhengkun Di, Bin Shi, Kai Sun et al. — [When Should Agents Check External State? Budgeting Observations for Stored Intentions](http://arxiv.org/abs/2609.37125v1)
  <details><summary>📄 Abstract</summary>
  Prospective memory allows an agent to retain an intention tied to a future condition, but the stored intention does not reveal whether that condition currently holds. Checking it may require web access, multi-step tool use, and paid calls. Existing systems decide when intentions require attention, but do not allocate the resulting observations under a shared budget. We introduce the first resource-allocation formulation for the external observations required by stored intentions under a shared e...
  </details>

- **2026-09-29** — Doyun Choi, Dooho Lee, Jaemin Yoo — [TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks](http://arxiv.org/abs/2609.36968v1)
  <details><summary>📄 Abstract</summary>
  Unsupervised tabular anomaly detection (TAD) aims to identify anomalous rows in tabular data using normal training samples. While conventional methods rely on dataset-specific training and configuration search, recent tabular foundation models (TFMs) enable zero-shot anomaly detection on unseen datasets via in-context learning. Most TFM-based approaches, however, require anomaly-specific pretraining from scratch, making detection inherently dependent on synthetic TAD-specific priors and costly t...
  </details>

- **2026-09-28** — Gregor Wiedemann, Daniel Wehrend — [The Surge of Anti-Semitism in German Social Media following the October 7 Attacks](http://arxiv.org/abs/2609.36290v1)
  <details><summary>📄 Abstract</summary>
  We investigate the extent to which the Hamas attacks on Israel of October 7, 2023, have affected German social media debates about Judaism and Israel. For this, we develop an approach to detect 26 anti-Semitic categories in user postings via large language models (LLMs). The approach is applied to Facebook and Telegram posts (N=125,718) from three months before and after the event. Methodically, we test different open-weight models in two setups---with and without user information as additional ...
  </details>

- **2026-09-28** — Long Phan, Stephen K. Yang, Jason J. Lim et al. — [CheatBench: Measuring Reward Gaming in AI Agents](http://arxiv.org/abs/2609.36308v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has helped AI agents solve increasingly difficult tasks, but high rewards do not always reflect the work users intended. In recent incidents and controlled evaluations across the AI industry, agents trained to maximize reward have accessed unauthorized information, attempted to evade monitoring systems, and even breached sandbox protections to attack external systems. As agents become more capable, this behavior could pose increasingly serious risks. To measure this proble...
  </details>

- **2026-09-28** — Feijie Wu, Hugo Barbalho, Konstantina Mellou et al. — [HeurEvo: Agentic Evolution of Hybrid Solver-Augmented Heuristics for Time-Critical Mathematical Optimization](http://arxiv.org/abs/2609.36303v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic heuristic design use AI agents and execution feedback to automate algorithm discovery for challenging optimization problems. In many practical settings, high-quality solutions must be obtained under strict runtime constraints, motivating hybrid approaches that combine problem-specific heuristics with powerful mathematical programming solvers. However, existing approaches typically improve heuristic components within predefined procedures or tune solver configurations i...
  </details>

- **2026-09-28** — Lei Liu, Zhaokang Liang, Qingcheng Zeng et al. — [MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis](http://arxiv.org/abs/2609.36235v1)
  <details><summary>📄 Abstract</summary>
  Major depressive disorder (MDD) severely impacts daily activities and quality of life. Detecting MDD involves multimodal data, such as interview recordings and sensor measurements. This is particularly challenging, as these heterogeneous modalities often demand distinct, customized prediction pipelines. Existing efforts to address this challenge have explored both manually engineered multimodal architectures and agent-assisted pipeline development. Despite their progress, it remains challenging ...
  </details>

- **2026-09-28** — Kaiqing Lin, Songze Li, Shen Chen et al. — [From Sharp Eyes to Expert Mind: Internalizing Expert Knowledge in MLLMs for Tampered Text Detection](http://arxiv.org/abs/2609.36145v1)
  <details><summary>📄 Abstract</summary>
  Tampered Text Detection (TTD) is essential for safeguarding document authenticity in security-critical workflows. Existing expert models are effective at capturing subtle manipulation traces but often generalize poorly across diverse document domains, while Multimodal Large Language Models (MLLMs) offer stronger semantic understanding and transferability yet remain insensitive to fine-grained forensic artifacts. This complementarity motivates us to investigate how expert forensic perception can ...
  </details>

- **2026-09-28** — Chaoqian Ouyang, Ling Yue, Libin Zheng et al. — [TokenCast: Forecasting Token Consumption During LLM Agent Execution](http://arxiv.org/abs/2609.35760v2)
  <details><summary>📄 Abstract</summary>
  When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cos...
  </details>

- **2026-09-28** — Dipankar Sarkar — [Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness with Constitutional Rewards, Escalation Labels, and Runtime Governance](http://arxiv.org/abs/2609.37501v1)
  <details><summary>📄 Abstract</summary>
  We propose RegLLM, a diagnostic harness for bounded autonomy in regulated agentic workflows. It instruments six trustworthiness signals: citation validity, source grounding, schema compliance, escalation correctness, constitutional alignment, and unsafe-action rate. Signals are distinguished by their source of supervision: programmatic verifiers, task-level escalation labels, or AI-judge scores. A deterministic runtime supervisor blocks ungrounded answers and forces escalation, logging intervent...
  </details>

- **2026-09-28** — Ethan D. Frakes, Amy Kvien, Rishabh Kundu et al. — [GeoOutageBench: Benchmarking Ambiguity-aware, Ontology-grounded Geospatiotemporal KGQA for Multimodal Power Outage and Resilience Analysis](http://arxiv.org/abs/2609.36082v1)
  <details><summary>📄 Abstract</summary>
  We introduce GeoOutageBench, a benchmark for assessing LLM-based geospatiotemporal KGQA for multimodal outage and resilience analysis. Unlike existing KGQA benchmarks for Web knowledge, GeoOutageBench considers a spatiotemporal KG that integrates visual, textual, and structured data from outage records, remote sensing, weather observations, storm and power events, geographic entities, and domain ontologies. It provides a competency query taxonomy at different difficulty levels from spatiotempora...
  </details>

- **2026-09-28** — Shidan Javaheri, Alexander Panfilov, Oliver Britton et al. — [Distillation Defenses Easily Break After Reinforcement Learning](http://arxiv.org/abs/2609.35699v1)
  <details><summary>📄 Abstract</summary>
  Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this pa...
  </details>

- **2026-09-28** — Saswat Das, Parvati Viswanathan, Daniel Donnelly et al. — [SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents](http://arxiv.org/abs/2609.35596v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment...
  </details>

- **2026-09-28** — Rong Pan, Yili Hong, Min Xie — [Reliability Engineering for AI Systems: Challenges, Methods, and Directions](http://arxiv.org/abs/2609.35316v1)
  <details><summary>📄 Abstract</summary>
  AI reliability concerns whether an AI system performs its intended function dependably over a stated period and under stated operating conditions, with stated evidence. As these systems become more autonomous, that function includes more than a correct output. Retrieval, memory, tool use, permissions, human oversight, and interactions among systems must operate consistently and safely, and, for generative systems, so must the reasoning process that produces the output. Average benchmark accuracy...
  </details>

- **2026-09-28** — Homayoun Maleki, Nekane Sainz, Jon Legarda et al. — [Sustained Participation as a Security Resource: The Bounded Participation Channel](http://arxiv.org/abs/2609.35300v1)
  <details><summary>📄 Abstract</summary>
  Can sustained, per-identity participation be engineered into a security resource? Most anti-Sybil defenses price identity creation rather than identity survival. Once admitted, an adversary may sustain many identities without paying a recurring cost. We introduce the Bounded Participation Channel (BPC), a formal primitive for repeatedly verifying participation window by window. BPC issues fresh, identity-bound challenges under a strict deadline and enforces four structural properties: identity b...
  </details>

- **2026-09-28** — Kasra Arabi, Nir Weinberger, Micah Goldblum et al. — [TANGO: Watermarking Masked Diffusion Language Models in Token Pairs](http://arxiv.org/abs/2609.35224v1)
  <details><summary>📄 Abstract</summary>
  Masked-diffusion language models fill in masked positions in parallel and in no fixed order. Most practical text watermarks assume left-to-right generation. They key each token to the tokens before it, and in a diffusion model those tokens may still be masked. A fixed green list needs no such context, but it favors the same tokens at every position, so these tokens appear more often in watermarked text. An attacker who compares token frequencies in watermarked and unwatermarked text can recover ...
  </details>

- **2026-09-28** — Qiankun Li, Yuechen Zhang, Bowen Chen et al. — [Still There, No Longer Seen: Exposing Compression-Induced Risk in Large Vision-Language Models](http://arxiv.org/abs/2609.35002v1)
  <details><summary>📄 Abstract</summary>
  Visual token compression reduces the inference cost of Large Vision-Language Models (LVLMs). However, aggregate robustness measures do not reveal whether a particular adversarial failure is induced by compression or inherited from the underlying model. We define a compression-specific failure (CSF) as an adversarial input that remains correct under full-token inference but fails after compression, casting compression-induced risk as a paired failure attribution problem. Within a controlled diagn...
  </details>

- **2026-09-28** — Yiqing Feng, Haozhe Feng, Shunan Shang et al. — [AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking](http://arxiv.org/abs/2609.34597v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can acquire complex capabilities through multi-step interaction and tool use, but their trajectories can also be illegally collected to dis- till student agents. However, existing watermarking methods either do not fit the structured and interactive nature of agent environments or lack reliable effective- ness across tasks and model architectures. We introduce AuxMark, a behavioral watermarking framework for tracing unauthorized agent distillation. AuxMark dynamically...
  </details>

- **2026-09-28** — Chanhee Park, Jeongho Yoon, Sungbin Han et al. — [AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering](http://arxiv.org/abs/2609.34428v1)
  <details><summary>📄 Abstract</summary>
  Agentic tasks require a large language model to interact with the world, navigating information and gathering evidence across multiple steps with restricted resources. Due to this complexity, agentic task failures arise from various sources, and pinpointing these failure causes is essential to diagnose and improve agentic systems. Existing benchmarks, however, tend to focus on a single leaderboard score, leaving the underlying failure modes opaque. To fill this gap, we introduce AgentHop, a diag...
  </details>

- **2026-09-28** — Ding Jia, Wei Liu, Xianglong Du et al. — [PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety](http://arxiv.org/abs/2609.34415v1)
  <details><summary>📄 Abstract</summary>
  The transition from Large Language Models (LLMs) to agents shifts safety stakes from toxic text to irreversible environmental harm. While current defenses remain largely retrospective, proactive runtime intervention is bottlenecked by the lack of large-scale, causally-consistent data. We propose PROACT-Agent, a framework for synthesizing high-fidelity trajectories to enable real-time guardrails. We identify a critical "safety drift" in prior benchmarks, where lenient annotation paradigms fail to...
  </details>

- **2026-09-28** — Chaoqian Ouyang, Ling Yue, Libin Zheng et al. — [TokenCast: Forecasting Token Consumption During LLM Agent Execution](http://arxiv.org/abs/2609.35760v1)
  <details><summary>📄 Abstract</summary>
  When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and intermediate results, while the growing context steadily inflates the input size of every subsequent call. The total consumption of a task is therefore hard to predict before execution and the prediction must be revised as the run unfolds. In this paper, we propose TokenCast, which learns a composable cos...
  </details>

- **2026-09-28** — Tianyao Shi, Xipeng Shen, Yi Ding — [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions](http://arxiv.org/abs/2609.35569v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving has environmental impacts across energy consumption, carbon emission, water consumption, and biodiversity loss. Yet these dimensions are largely evaluated in isolation, leaving it unclear when and how they lead to different optimization decisions. We present PRISM, a unified framework for characterizing and optimizing LLM serving across energy, carbon, water, and biodiversity impacts. Our analysis reveals a fundamental distinction: computing configurations dete...
  </details>

- **2026-09-28** — Shobhan Roy — [The Compiler May Read It, the Agent May Not: Keeping Part of a Research Code Away from a Coding Agent](http://arxiv.org/abs/2609.35557v1)
  <details><summary>📄 Abstract</summary>
  The compiler must read modules a physics-based solver cannot build without; the coding agent must not read that intellectual property. The harness does not ship that rule. We classified fifteen read routes against a container, permission rules and a sandbox. None of the three can tell which program is reading.
  </details>

- **2026-09-28** — Yage Zhang, Yukun Jiang, Yang Zhang — ["Nothing to See Here'': Unintended Disclosure through Revision Traces of LLM Deliverables](http://arxiv.org/abs/2609.35408v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) assistants increasingly help users draft content for third-party recipients. During private drafting, the user or the model may introduce an item and later remove or replace it. The model may remove the item from the intended content but reveal it again when stating the edit. We call such statements revision traces. For example, after a user removes the password before sharing a configuration file, the model may delete it but leave a comment saying, "Removed the passwo...
  </details>

- **2026-09-28** — Jinnan Guo, Hao Mark Chen, Kapil Vaswani et al. — [Planarian: Managing Agent State with Statepoints](http://arxiv.org/abs/2609.35366v1)
  <details><summary>📄 Abstract</summary>
  LLM agents solve complex tasks by iteratively changing files, invoking local tools, and interacting with remote services, which modifies state across their local environment and remote services. Today, agents and users must manage these changes explicitly, whether reverting exploratory actions or recovering from erroneous ones. Doing so safely requires coordinated actions, yet current agent harnesses lack unified abstractions and mechanisms for managing local and remote state consistently and ef...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 52 papers

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

- **2026-09-29** — Sumin Hong, Katsumi Ibaraki, Renee Shi et al. — [Similar Choices, Different Attention: Cross-Modal Associations in Humans and Vision-Language Models](http://arxiv.org/abs/2609.36475v1)
  <details><summary>📄 Abstract</summary>
  Cross-modal associations are systematic pairings of features across modalities, such as the association of 'bouba' with round shapes and 'kiki' with sharp shapes. Prior work has compared humans and vision-language models (VLMs) on such associations, but often using different stimuli or tasks between humans and models. Here, we ask whether VLMs align with humans not only in choices, but also in where they look when making those choices. We study both VLMs and humans (N = 53), presenting them with...
  </details>

- **2026-09-29** — Chao Hu, Yuan Guo, Guanlin Wu et al. — [LLM-Based Multi-Agent Systems over Wireless Networks: A Joint Agent--Network Design Perspective](http://arxiv.org/abs/2609.37094v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) evolve from standalone models into collaborative agents embedded in physical systems, their reasoning and execution are increasingly distributed across wireless edge nodes. In this setting, wireless networks are experiencing a paradigm shift from only providing data connectivity to supporting the multi-agent reasoning workflow itself. The task performance of such network-constrained LLM-based multi-agent systems (MASs) is jointly affected by the multi-agent reason...
  </details>

- **2026-09-28** — Wasif Jalal, Sachin Deb, Asif Salekin — [Reducing the Adaptation Gap Through Reachable Fisher Geometry](http://arxiv.org/abs/2609.36329v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) determines not only how many parameters are trained, but also which local directions a model can move in, so similar adapters can affect subgroup losses differently. Since curvature matrices are infeasible to form at adapter scale, scalar summaries such as the Fisher trace are often used instead. We study what the trace reveals and what it loses through the reachable Fisher: each subgroup's full-model Fisher pulled back through the adapter Jacobian. Under l...
  </details>

- **2026-09-28** — Zitong Lan, Mutian Tong, Jiatao Gu et al. — [Enabling Immersive Audio-Visual Experience from Any Video](http://arxiv.org/abs/2609.36295v1)
  <details><summary>📄 Abstract</summary>
  Most videos capture only a narrow field of view and provide no spatial audio, limiting the sense of immersion they can provide. Recent video generation models can expand perspective videos into panoramic ones, but do not provide the corresponding spatial soundscape. Without spatially consistent audio, these expanded visual worlds remain incomplete. This paper presents OmniDream, a training-free framework that transforms a silent monocular video into an immersive audiovisual experience, where vie...
  </details>

- **2026-09-28** — Neemias B. da Silva, Martin Lukk, Ali Sutani et al. — [Population Fidelity: Evaluating Population Representativeness in LLMs](http://arxiv.org/abs/2609.36253v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) show considerable potential in simulating human attitudes and preferences. Prior work finds that LLM-generated responses can compress the range of attitudes found within populations and misrepresent particular subgroups in ways that vary across models and topics. We introduce Population Fidelity, an evaluation framework that distinguishes key conditions required for a set of LLM-generated responses to represent a population. It incorporates three dimensions: group-le...
  </details>

- **2026-09-28** — Zhivar Sourati, Mengxuan Helen Wu, Nona Ghazizadeh et al. — [Cognitive Expert Language Models Better Align with the Corresponding Brain Systems](http://arxiv.org/abs/2609.36239v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can predict human brain activity across a variety of brain regions during natural language comprehension. Typically, however, LLM-brain alignment is measured using one model for different regions of the brain, and then model performance is summarized across regions. This one-model-fits-all approach ignores the functional specialization of brain regions. In this study, we assess whether a model oriented toward a particular cognitive domain aligns better with the brain...
  </details>

- **2026-09-28** — Aditya Sharma, Divya Saxena — [One Geometry, Different Outcomes: Readout-Dependent Effects of the Modality Gap in Vision-Language Models](http://arxiv.org/abs/2609.36101v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language models learn shared embedding spaces by aligning matched image-text pairs, yet their representations remain separated by a modality gap. Prior work reports divergent effects of modifying this gap: reducing it can improve zero-shot classification and cross-modal alignment, whereas removing gap-related structure can degrade image-text retrieval. In this paper, we provide a unified geometric explanation for these task-dependent effects. Across CLIP and SigLIP encoders, w...
  </details>

- **2026-09-28** — Cheng Chang, Yining Mao, Peng Qi — [PADMÉ: Preference Alignment Data Synthesis for Meta-Evaluation of LM Agent Evaluators](http://arxiv.org/abs/2609.36086v1)
  <details><summary>📄 Abstract</summary>
  Language models are frequently employed to evaluate other language models. An LM evaluator scoring agentic behaviors across multiple criteria is valuable, provided that its decisions align with human judgment. We call the problem of evaluating this alignment Meta-Evaluation. Tackling it directly is difficult: collecting human data is expensive, absolute scoring is hard to align, and using an LM meta-evaluator recurses the question of trustworthiness. We adopt a reformulation of meta-evaluation a...
  </details>

- **2026-09-28** — Sahand Rezaei-Shoshtari, Patryk Wozniczka, Shu Ishida et al. — [FLOORA: A Human-Aligned Domain-Specific Language Model for Architectural Design](http://arxiv.org/abs/2609.36064v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are powerful generators, but many engineering domains require structured representations that general-purpose systems handle poorly. We introduce FLOORA (Floor Layout Optimization with RL Alignment), a family of small domain-specific language (DSL) models for architectural layout generation. With specialized data and alignment, our 0.6B model outperforms much larger frontier models, achieving VLM judge win rates up to 92.0% on out-of-distribution real-world buildings and 96.0% ...
  </details>

- **2026-09-28** — Shengchao Hu, Peng Wang, Qiyang Zhou et al. — [Alignment-Guided Flow Transformer for Efficient Vision-Language-Action Policy Learning](http://arxiv.org/abs/2609.34467v2)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language-Action (VLA) models point toward general-purpose robotic intelligence by unifying perception, instruction, and control. Despite impressive progress, existing VLA models often adapt poorly due to \emph{tri-modal misalignment} among vision, language, and action, which weakens action grounding and hurts generalization and fine-tuning efficiency. In this work, we present Alignment-Guided Flow Transformer (AGFT), a novel framework that explicitly enforces tri-modal ...
  </details>

- **2026-09-28** — Qirui Liu, Yichen Sun, Yan Wang et al. — [DeShortcut-Align: Decoupling Spurious Shortcuts for Robust Safety Alignment in Large Reasoning Models](http://arxiv.org/abs/2609.34896v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment of large reasoning models (LRMs) via supervised fine-tuning (SFT) and reinforcement learning (RL) often yields near-perfect safety scores, yet this apparent success comes at the cost of severe over-refusal and degraded general capabilities. Through systematic empirical analysis, we find that these failures are closely associated with the learning of spurious shortcuts rather than robust intent-sensitive safety evaluation. Specifically, we identify two dominant shortcuts: formatt...
  </details>

- **2026-09-28** — Yejin Kim, William F. Shen, Seokwon Jung et al. — [TULIP: Targeted LLM Unlearning at Layers Identified Per-Input](http://arxiv.org/abs/2609.34591v1)
  <details><summary>📄 Abstract</summary>
  Representation-level unlearning intervenes on the intermediate hidden states of LLMs. Although knowledge is distributed across layers, existing methods operate at a single fixed layer for the entire forget set. We ask whether such a fixed layer is sufficient. To answer this, we design a hijacking experiment that grafts hidden states of the target model into an oracle trained only on the retain set. The oracle cannot produce the forget answer on its own, yet it produces the answer from the grafte...
  </details>

- **2026-09-28** — Hyunwoo Yoo, Cassie Huang, Haebin Shin et al. — [Representation Alignment as a Bottleneck in LLM-Based Retrosynthesis Planning](http://arxiv.org/abs/2609.35571v1)
  <details><summary>📄 Abstract</summary>
  While LLMs show promise in general reasoning, symbolic planning in chemistry remains a bottleneck. Direct ''SMILES-to-PDDL'' attempts fail because they force models to juggle chemical analysis and planning-language structuring simultaneously. We hypothesize that this failure stems from a lack of intermediate abstractions rather than insufficient model capacity. By decomposing retrosynthesis into molecule mapping, reaction mapping, and PDDL generation, we achieve high success rates where end-to-e...
  </details>

- **2026-09-28** — Pranjal Garg, Jacob Beck — [Spontaneous Context Restoration: How Language Models Recover from Corrupted Inputs](http://arxiv.org/abs/2609.35475v1)
  <details><summary>📄 Abstract</summary>
  Language models sometimes produce correct outputs even when their inputs are corrupted by deletion, replacement, or misspelling. We study the internal processes accompanying this behavior, which we call context restoration, in controlled attention-only transformers and five pretrained LLMs (1B-32B parameters) across arithmetic, reading comprehension, and multiple-choice reasoning tasks. In the attention-only transformers, restoration emerges spontaneously despite training exclusively on clean se...
  </details>

- **2026-09-28** — Carlos Garrido-Munoz, Jorge Calvo-Zaragoza — [Handwritten Text Recognition Lives in the High-Pixel Variance Subspace](http://arxiv.org/abs/2609.35473v1)
  <details><summary>📄 Abstract</summary>
  In self-supervised pretraining for Handwritten Text Recognition (HTR), pixel reconstruction methods outperform contrastive methods, unlike in natural-image classification. We argue that this difference follows from where discriminative signal lies in pixel space: for HTR, it is concentrated in high-variance directions and largely absent from low-variance ones. This predicts that objectives preserving high-variance pixel content will transfer best. We test six SSL methods from three families (pix...
  </details>

- **2026-09-28** — Lucas Bandarkar, Junlin Hu, Chenyuan Yang et al. — [Multilinguality in Hybrid Attention LLMs](http://arxiv.org/abs/2609.35378v1)
  <details><summary>📄 Abstract</summary>
  In response to the growing demand for long sequences in agentic and reasoning use cases, many state-of-the-art LLMs combine multiple variants of attention to mitigate the quadratic complexity of traditional softmax attention. These hybrid attention LLMs aim to balance the strengths and limitations of full attention and alternatives based on recurrence. This work presents a first study of how hybrid attention impacts the multilinguality of LLMs. Beyond the impact on long sequences in poorly token...
  </details>

- **2026-09-28** — Bangjun Wang, Longyan Wu, Yukun Wei et al. — [From Pixel to Poses: Object-centric Tool Manipulation Learning from Human Demonstrations](http://arxiv.org/abs/2609.35375v1)
  <details><summary>📄 Abstract</summary>
  Scaling up robotic manipulation is primarily bottlenecked by the scarcity of real-world robot data. While recent approaches leverage human video demonstrations to mitigate this shortage, they remain computationally expensive and still rely on paired human-robot data for domain alignment. Although current state-of-the-arts excel at long-horizon tasks, they struggle with the delicate and precise control required for complex tool manipulation. To overcome these limitations, we introduce P2P-T, from...
  </details>

- **2026-09-28** — Xingming Long, Jie Zhang, Yuecong Min et al. — [Beyond Saying Less: Fine-Grained Alignment for Informative and Faithful Vision-Language Models](http://arxiv.org/abs/2609.35294v1)
  <details><summary>📄 Abstract</summary>
  Object hallucination remains a major challenge for large vision-language models. While off-policy preference optimization proves to be an effective solution, on-policy reinforcement learning provides a more promising direction as it directly targets a model's current failure modes. However, we find that without fine-grained reward formulation and allocation, on-policy optimization often falls into an easy shortcut: reducing hallucinations merely by saying less---making fewer valid claims. To com...
  </details>

- **2026-09-28** — Han Fu, Jiacheng Chen, Baoquan Zhao et al. — [Scaffold Then Internalize: Representation Injection for Diffusion Transformers](http://arxiv.org/abs/2609.35292v1)
  <details><summary>📄 Abstract</summary>
  Recent representation alignment (REPA) methods accelerate diffusion transformer training by aligning projections of the transformer's hidden states with representations from pretrained visual encoders. In this work, we explore a reverse and complementary direction to REPA: rather than projecting diffusion representations into the encoder's space, we inject encoder representations into the diffusion transformer, allowing them to actively participate in the denoising process. To this end, we intro...
  </details>

- **2026-09-28** — Yuanzi Li, Lingjie Wang, Zihang Tian et al. — [SCBO: Semantically Coherent Batching and Ordering for LLM-Based Social Surveys](http://arxiv.org/abs/2609.35250v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer a scalable way to simulate survey respondents using demographic profiles and observed reference responses. However, the conventional approach of predicting one question per prompt repeatedly encodes the same context, limits each target to a narrow set of reference responses, and prevents later predictions from using information in earlier answers. Predicting multiple questions in one prompt can reduce these costs, share a broader pool of references, and let lat...
  </details>

- **2026-09-28** — Shurui Liu, Weide Chen, Changwang Yi et al. — [DrawingsDreamer: A Unified Multi-View Engineering Drawings Generation Model](http://arxiv.org/abs/2609.35242v1)
  <details><summary>📄 Abstract</summary>
  Scalable Vector Graphics (SVG) are essential for modern industrial Computer-Aided Design (CAD). However, existing autoregressive SVG generation models are predominantly tailored for artistic creation and struggle to maintain the rigorous geometric fidelity and cross-view spatial alignment required for engineering drawings. To bridge this gap, we introduce \textbf{DrawingsDreamer}, a unified Large Language Model (LLM)-driven framework for multi-view vector-based engineering drawings generation. B...
  </details>

- **2026-09-28** — Rui Zhong, Yu Li, Zheyu Yan et al. — [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](http://arxiv.org/abs/2609.35232v1)
  <details><summary>📄 Abstract</summary>
  Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity. We revisit compression through a token parameterization lens, separating (i) basis transformation and structured truncation (retained subspace/compressibility) from (ii) coordinate organization (optimization and cross-modal alignment)...
  </details>

- **2026-09-28** — Zhaoyi An, Sihan Tan, Youngbae Hwang et al. — [SignFLIP: A Unified Model for Sign Language Translation and Generation via Stage-wise Alignment at Scale](http://arxiv.org/abs/2609.35225v1)
  <details><summary>📄 Abstract</summary>
  Sign language translation and generation share the goal of bidirectional alignment between text and sign representations. However, existing approaches either treat them as isolated tasks or are only verified on limited datasets, limiting effective modeling between modalities. In this paper, we propose SignFLIP, a unified LLM-centered framework for translation and generation. To enable bidirectional mapping between text and sign, SignFLIP adopts a symmetric architecture together with a stage-wise...
  </details>

- **2026-09-28** — Husrev Taha Sencar, Rezart Beka, Danish Naeem et al. — [From Normative Frameworks to Alignment Data: Constructing and Evaluating SFT and Preference Data](http://arxiv.org/abs/2609.35201v1)
  <details><summary>📄 Abstract</summary>
  Aligning language models with a specified normative framework requires translating abstract principles into concrete examples and preference signals from which models can learn. We present an expert-driven methodology for constructing such alignment data and apply it to a normative framework grounded in Islamic ethical, theological, and jurisprudential traditions. Over approximately one year, seven domain experts systematically probed language models to identify alignment deficiencies, curated d...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

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

- **2026-09-29** — Dongchan Shin, Xing Han Lù, Jiaqi Deng et al. — [AdaptArena: Evaluating Test-Time Personalization of Web Agents](http://arxiv.org/abs/2609.36488v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have demonstrated strong performance on complex web navigation tasks, yet they remain brittle in real-world settings where user intentions are underspecified and preferences are heterogeneous. In practice, users rarely provide explicit profiles, requiring agents to infer latent preferences from implicit signals. Despite its importance for deployment, this problem setting is largely underexplored in existing benchmarks. To address this gap, we introduce AdaptAren...
  </details>

- **2026-09-29** — Merve Atasever, Keyan Azbijari, Cagan Bakirci et al. — [Video2STL: Grounding VLM-Generated Temporal Specifications for Robot Learning](http://arxiv.org/abs/2609.37519v1)
  <details><summary>📄 Abstract</summary>
  Video-based policy learning is particularly promising, as it illustrates target behaviors without requiring action annotations or embodiment-matched demonstrations. A central challenge is deciding what information should be transferred from the video to the robot. Existing approaches commonly convert visual observations into scalar similarity or value signals, or ask foundation models to directly generate reward code. These approaches can make the temporal structure of a task difficult to inspec...
  </details>

- **2026-09-29** — Arav Dhoot, Punya Syon Pandey, Jamie Johnson et al. — [Character Training for Risk-Averse Agents](http://arxiv.org/abs/2609.38093v1)
  <details><summary>📄 Abstract</summary>
  Risk aversion in resources could prevent misaligned AI agents from causing catastrophic harm. Misaligned but risk-averse agents would tend to favor safer strategies like making deals with humans over riskier strategies like rebelling. We train agents to be risk averse through character training, finding that persona traits provide a robust mechanism for instilling risk preferences. To do this, we construct a model constitution describing constant absolute risk aversion (CARA) over an agent's res...
  </details>

- **2026-09-29** — Vincenzo Pomponi, Rocco Felici, Paolo Franceschi et al. — [DROM: A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation](http://arxiv.org/abs/2609.37348v1)
  <details><summary>📄 Abstract</summary>
  Learning robust manipulation policies for diverse, long-horizon tasks from limited demonstrations remains a fundamental challenge in robotics. We present DROM, a language-guided diffusion framework that enables robots to learn, represent, and compose multiple manipulation skills within a single generative policy. DROM leverages Dynamic Movement Primitives (DMPs) to augment a small set of expert demonstrations into expressive multi-skill datasets, substantially reducing data collection while impr...
  </details>

- **2026-09-29** — Junghyun Kim, Ngseo Kim, ChungWoo Lee et al. — [Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead](http://arxiv.org/abs/2609.37165v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models remain brittle under visual distribution shifts, often relying on spurious correlations tied to domain-specific factors rather than task-relevant structure. We propose Domain-Invariant Latent Lookahead (DILL), a representation-learning framework that mitigates shortcut learning in VLA policies. Our key idea is to supervise policies with domain-invariant future latents learned from domain-transformed trajectory data. A Task-Domain Encoder is trained with contra...
  </details>

- **2026-09-29** — Xiaotian Zhang, Yusheng Wang, Naoya Kagawa et al. — [DRHeC: Differentiable Rendering for Hand-Eye Calibration with RGB-Based Gradients](http://arxiv.org/abs/2609.36779v1)
  <details><summary>📄 Abstract</summary>
  Accurate hand-eye calibration is crucial for precision manipulation. Traditional methods rely on markers, with their precision dependent on marker accuracy and observability. In contrast, markerless methods, such as learning-based approaches, use deep neural networks to directly extract keypoints or features from images, enabling the computation of hand-eye transformation with a single image and without the need for physical markers. Recently, differentiable rendering-based methods for hand-eye ...
  </details>

- **2026-09-29** — Ruixiao Xu, Wong Lik Hang Kenny, Zhiqian Liu et al. — [Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning](http://arxiv.org/abs/2609.36588v1)
  <details><summary>📄 Abstract</summary>
  We study reinforcement learning (RL) methods for cooperative multi-agent Vision-Language-Action (VLA) models. This problem is challenging because VLAs are pretrained on large-scale single-agent data and therefore lack the fine-grained coordination skills required for inter-robot collaboration. Supervised fine-tuning (SFT) on multi-robot demonstrations partially bridges this gap, but its performance is bounded by the demonstration data and cannot improve from its own experience. We present a thre...
  </details>

- **2026-09-29** — Mathias Jackermeier, Jacques Cloete, Alessandro Abate — [Jaxolotl: A Unified High-Performance Benchmark Suite for LTL-Based Multi-Task RL](http://arxiv.org/abs/2609.38065v1)
  <details><summary>📄 Abstract</summary>
  Training agents to follow arbitrary instructions is an important goal of multi-task reinforcement learning (RL). Linear temporal logic (LTL) provides a precise and structured formalism for specifying instructions to agents, and has been successfully adopted for training generalist multi-task policies. However, differences in implementations, task distributions, and evaluation protocols make existing methods difficult to compare, while high computational costs limit the scale and statistical reli...
  </details>

- **2026-09-29** — Agathe Sadeghi, Dingyue Liu, Ciamac Moallemi et al. — [Not All LPs Are Equal: The Active-Passive Gap in Automated Market Maker Liquidity Provision](http://arxiv.org/abs/2609.37963v1)
  <details><summary>📄 Abstract</summary>
  Liquidity provision in automated market makers is typically analyzed at the pool level, implicitly assuming LP homogeneity. This aggregate view can hide how liquidity provision outcomes differ between LP strategies, particularly as concentrated liquidity AMM designs operating on high-performance blockchains allow liquidity to be actively repositioned around trades. We develop a markout-based framework to decompose Uniswap LP profitability into active and passive components using two complementar...
  </details>

- **2026-09-29** — Timothy K Johnsen, Marco Levorato — [WayFinder: Hierarchical Visual-Language-Action for Zero-Shot Waypoint Generation and Low-Level Kinematic Control](http://arxiv.org/abs/2609.37922v1)
  <details><summary>📄 Abstract</summary>
  Visual Language Action (VLA) models offer unprecedented generalization for autonomous robots; however, their real-world deployment is frequently bottlenecked by unreliable execution and the prohibitive computational cost of fine-tuning for specific robot embodiments and tasks. To bridge this gap, we propose WayFinder, an end-to-end, closed-loop hierarchical VLA framework that circumvents the need for fine-tuning by decoupling high-level task reasoning from low-level kinematic control. WayFinder ...
  </details>

- **2026-09-29** — Lalita Lowphansirikul, Attapol Rutherford, Jian Gang Ngui et al. — [Zero-shot Dependency Parsing with Unsupervised Cross-Lingual Bootstrapping](http://arxiv.org/abs/2609.37883v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained language models (PLMs) with encoder-based architectures have shown impressive capabilities in zero-shot cross-lingual transfer for various language understanding tasks. However, applying this technique to dependency parsing remains a significant challenge due to its syntactic nature. To boost model generalizability across linguistic typologies, we propose a cross-lingual unsupervised bootstrapping method to improve syntactic knowledge within the PLM. We show that our method achieves ...
  </details>

- **2026-09-29** — Zhenting Huang, Junnan Liu, Qianren Mao et al. — [Active Budget Can Kill Sensitivity: Diagnosing and Repairing TopK Sparse Autoencoder Reliability](http://arxiv.org/abs/2609.37857v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are increasingly scaled to wider dictionaries to recover fine-grained structure from large language model activations. However, a feature is useful for interpretation only if it remains a stable unit of analysis when the same meaning is expressed in different surface forms. We study this reliability question for TopK SAEs via feature sensitivity. Experiments demonstrate that scaling selectively reduces the sensitivity of rare features, while common features remain comp...
  </details>

- **2026-09-29** — Neha Sharma, Sushanta Mandal, Nikita Sharma et al. — [From Chemical Complexity to Tunable Magnetic Ordering in Highly Disordered High-Entropy Spinel Oxides](http://arxiv.org/abs/2609.37792v1)
  <details><summary>📄 Abstract</summary>
  High-entropy stabilization chemistry is redefining materials design by transforming configurational disorder, arising from the deliberate incorporation of multiple principal cations, into a thermodynamic advantage that promotes phase stability and enables emergent functionalities. In this work, we investigate the evolution of magnetic ordering in spinel-type high entropy oxides by systematically varying the cation composition of the B site within a fixed high-entropy A-site matrix, (Ni$_{0.2}$Mg...
  </details>

- **2026-09-29** — Min Yang, Yichen Pan, Jinghua Piao et al. — [EnterpriseBench: Benchmarking LLM Agents on Enterprise-Level Strategic Reasoning and Decision-Making](http://arxiv.org/abs/2609.37658v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly expected to support enterprise workflows, where tasks often involve missing information, uncertainty, feedback, and long-term trade-offs. However, existing enterprise and financial benchmarks mainly test static capabilities such as information extraction, numerical calculation, domain knowledge, and financial QA, leaving interactive and long-horizon decision-making underexplored. To bridge this gap, we introduce EnterpriseBench, a benchmark that evaluates LLM agents a...
  </details>

- **2026-09-29** — Jiayu Ying, Qijian Tian, Ruijie Xu et al. — [Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding](http://arxiv.org/abs/2609.37655v1)
  <details><summary>📄 Abstract</summary>
  Advancing spatial intelligence in Multimodal Large Language Models (MLLMs) is bottlenecked by the scarcity of complex, scalable 3D question-answer (QA) data. While manual annotation is labor-intensive, directly utilizing LLMs to synthesize these QA pairs often fails due to their inherent deficiencies in spatial and geometric computation. We introduce Exemplar2VQA, a scalable exemplar-driven visual question answering generation framework that rapidly synthesizes large-scale spatial QA pairs in si...
  </details>

- **2026-09-29** — AmirEhsan Khorashadizadeh, Benjamín Béjar — [TomoTransformer: Towards a Foundation Model for CT Reconstruction](http://arxiv.org/abs/2609.37605v1)
  <details><summary>📄 Abstract</summary>
  Supervised deep learning has advanced sparse-view tomographic reconstruction. However, conventional models, which typically map filtered back-projection (FBP) images or sinograms to clean reconstructions, are brittle under distribution shifts. Because they require retraining whenever projection counts and angles, detector resolutions, or data distributions change, their deployment in real-world applications remains limited. To address this, we introduce TomoTransformer, a transformer-based archi...
  </details>

- **2026-09-29** — Bruno Brocai, Maria Becker — [Pair Difficulty Matters: Rethinking Pairwise LLM-as-a-Judge Evaluation and Consistency](http://arxiv.org/abs/2609.37577v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model judges are widely used to rank texts and text-generating systems through pairwise comparison, and their reliability is typically assessed via three proxies: position bias, transitivity, and pairwise agreement (self- or human-labeled). Because these proxies drive judge selection and benchmarking, a substantial literature reporting that judges perform poorly on them risks steering practitioners away from otherwise capable evaluators. We argue this assessment is misleading. Und...
  </details>

- **2026-09-29** — Hyunjong Ok, Seunggu Kang, Jaeho Lee — [Hierarchical Compression of Vision-Language Model Benchmarks](http://arxiv.org/abs/2609.37515v1)
  <details><summary>📄 Abstract</summary>
  Thorough evaluation of vision-language models (VLMs) has become prohibitively expensive, as benchmarks span an ever-broader spectrum of capabilities and new models arrive at a relentless pace. Benchmark compression methods that preserve model rankings at a fraction of the cost are well studied for language models, but for VLMs the question remains under-explored. We present PRIMEBench (Pruning Redundant Items for Multimodal Evaluation), a vision-aware hierarchical benchmark compression framework...
  </details>

- **2026-09-29** — Marcos Rodriguez-Vega, Afonso Ferreira, Iru Exposito-Luis et al. — [Shaping Opinion: Quantifying the Psychological Impact of Autonomous Multi-Agent LLM Interactions](http://arxiv.org/abs/2609.37369v1)
  <details><summary>📄 Abstract</summary>
  Natural-sounding multi-agent conversational AI is increasingly deployed, fundamentally altering human-machine interaction and human information processing. While prior work largely focuses on algorithmic failure, this study investigates the cognitive ergonomics and socio-cognitive impact of algorithmic competence. We present and evaluate FORMS (Framework for Opinion and Rhetoric in Multi-agent Simulations), a low-latency architecture for spatially mediated human-machine dialogue, driven by disti...
  </details>

- **2026-09-29** — Zijing Cai, Yuzhe Wang, Jingxian Zhu et al. — [ResComEmb: Effective and Efficient Multimodal Embedding via Residual Homogeneity Compression](http://arxiv.org/abs/2609.37225v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have shown strong potential for universal multimodal representation learning. However, existing methods either compress each input into a single vector, limiting fine-grained expressiveness, or retain long sequences of visual-token vectors, incurring substantial storage and interaction costs. To resolve this trade-off, we propose ResComEmb, a trainable framework for effective and efficient universal multi-vector multimodal embedding. ResComEmb first encod...
  </details>

- **2026-09-29** — Marco Jochum, Ioannis Kouroudis, Gohar Ali Siddiqui et al. — [Accelerated surrogate dynamics for dynamical, stochastic system evolution](http://arxiv.org/abs/2609.37184v1)
  <details><summary>📄 Abstract</summary>
  Dynamic simulations are an entrenched way of gaining insight into the evolution of system dynamics. Their computational cost however is often prohibitively high, especially in cases of stochastic frameworks. Machine learning algorithms are especially suited as simulation surrogates. Nevertheless, they face some very distinct limitations. Firstly, the sheer dimensionality of these systems, however, precludes the use of traditional time series models who struggle with high dimensional feature spac...
  </details>

- **2026-09-29** — Hongyang Li, Yiming Zhu, Xiao Li et al. — [Beyond Compression: Diagnosing How Post-Training Changes Mathematical Reasoning](http://arxiv.org/abs/2609.37066v1)
  <details><summary>📄 Abstract</summary>
  Post-training is central to mathematical reasoning in modern large language models (LLMs), but endpoint pass@1 alone underidentifies what has changed. Gains may reflect newly reachable solutions, cheaper sampling of latent solutions, surface robustness, or memorisation. We compare three post-training paths under a common diagnostic readout: our sufficiently trained off-policy distillation trajectories, released Qwen3 off-policy-plus-on-policy distillation endpoints, and a released DeepSeek-Math ...
  </details>

- **2026-09-29** — Maria Cristina Barbieri Góes, Saverio Barabuffi — [Beyond the Coast: an Empirical Assessment of the Kaldor-Verdoorn Law in Chinese Provinces](http://arxiv.org/abs/2609.37051v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates spatial productivity convergence across Chinese provinces during structural transformation, examining how a shift in auonomous demand composition reshaped regional productivity dynamics. Using Panel Structural Vector Autoregressive modelling and province level data from 2001 to 2021, we analyse eastern, central, ad western regions across two sub-periods through the augmented Kaldor-Verdoorn law. A post-2011 spatial reversal emerges: inland regions exhibit stronger Verdoor...
  </details>

- **2026-09-29** — Kirill Borodin, Vasilii Kudryavtsev, Maxim Maslov et al. — [ReDimNet2+: Multi-Corpus Data Scaling for Robust Speaker Verification](http://arxiv.org/abs/2609.37014v1)
  <details><summary>📄 Abstract</summary>
  Automatic speaker verification must remain reliable across devices, rooms, and compression pipelines. We present ReDimNet2+, which scales training of the compact ReDimNet2 backbone across seven public corpora (63,934 speakers, about 8,675 hours). Analysis of a VoxBlink2 subset reveals a shift in predicted spectral coloration, motivating codec and waveform augmentation alongside this multi-corpus training, large-margin fine-tuning (LMFT), and graph-based retrieval reranking. With random 4-second ...
  </details>

- **2026-09-29** — Zhongyi Li, Wan Tian, Xiang Xu et al. — [Dual-Channel Robust Group-Relative Policy Optimization via Advantage and Sequence-Weight Estimation](http://arxiv.org/abs/2609.36944v1)
  <details><summary>📄 Abstract</summary>
  Group-relative policy optimization relies on reward-derived advantages and sequence-level likelihood weights, both of which can be sensitive to localized outliers. Extreme rewards can collapse the contrast among clean responses after group normalization, while token-level log-ratio perturbations can alter sequence weights and clipping decisions. We introduce RoVR-GSPO, a dual-channel robust optimizer that addresses these failure modes separately. Its reward channel combines robust reference esti...
  </details>

- **2026-09-29** — Thai Duy Nguyen, Addison Lin Wang — [SFE-VGGT: Source-Free VGGT Distillation for Event-Based Monocular Depth Estimation](http://arxiv.org/abs/2609.36929v1)
  <details><summary>📄 Abstract</summary>
  Recent event-based depth estimation methods successfully transfer geometric priors from vision foundation models via cross-modal distillation. However, their reliance on synchronized RGB-event pairs or depth annotations during training severely restricts practical deployment. To overcome this bottleneck, we propose SFE-VGGT, a novel source-free framework that distills the geometric priors of VGGT to the event domain without any paired RGB observations. Our core idea is to reconstruct surrogate f...
  </details>

- **2026-09-29** — Bin Kang, Jiarui Ouyang, Li Jiang et al. — [PrecogUI: Proactive GUI Agents via Pre-cognitive Simulation and Experience Retrieval](http://arxiv.org/abs/2609.36923v1)
  <details><summary>📄 Abstract</summary>
  Existing reactive Graphical User Interface (GUI) agents often fail in long-horizon, dynamic scenarios, where unexpected disturbances trigger attention-diverting and cascading failures. To address this, we propose PrecogUI, a pre-cognitive architecture that shifts the paradigm from reactive execution to proactive decision-making. Specifically, we design a Proactive Experience Pool (PEP), which caches recurring anomaly and success patterns as "state-action-result" tuples in a dual-memory repositor...
  </details>

- **2026-09-29** — François Costa, Charly Castes, Thomas Bourgeat et al. — [AI as a Compiler: Compiling Triton kernels without the Triton compiler](http://arxiv.org/abs/2609.36800v1)
  <details><summary>📄 Abstract</summary>
  Compiler backends are expensive to build and maintain as programming models, workloads, and accelerators evolve. We investigate whether large language models can replace the conventional optimizing and lowering pipeline, a process that we call AI lowering. We study AI lowering from Triton to NVIDIA PTX: an LLM agent translates Triton kernels directly into PTX. We build an environment that evaluates candidate PTX, and an agentic harness in which an LLM translates Triton kernels into PTX. Across t...
  </details>

- **2026-09-29** — Moein Khajehnejad, Forough Habibollahi, Tommaso Boccato et al. — [From Neurons to Conversation: Speech Brain-Computer Interfaces](http://arxiv.org/abs/2609.36736v1)
  <details><summary>📄 Abstract</summary>
  Speech brain-computer interfaces (BCIs) aim to restore communication by transforming neural activity related to speech, language, or communicative intent into external outputs such as text, synthesized voice, or avatar control. Recent advances in intracortical and electrocorticographic recording, deep sequence models, and language-model-assisted decoding have enabled rapid progress, including high-performance attempted-speech decoding and increasingly naturalistic speech synthesis. Yet these ach...
  </details>

- **2026-09-29** — Xinlin Zhuang, Siyuan Wang, Imran Razzak et al. — [What Makes Recurrence Effective in Looped Language Models?](http://arxiv.org/abs/2609.36636v1)
  <details><summary>📄 Abstract</summary>
  Looped language models (LoopLMs) increase computational depth through parameter sharing, offering a path to scale inference computation without adding parameters. However, it remains unclear when additional recurrence is beneficial and how architectural choices affect its effectiveness. Through controlled experiments, we systematically examine (1) when recurrence helps, (2) where it should be applied, and (3) how its conditioning affects performance. Our evaluation covers inference budgets below...
  </details>

- **2026-09-29** — Jiapeng Li — [Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent Stress Test](http://arxiv.org/abs/2609.36614v1)
  <details><summary>📄 Abstract</summary>
  A commercial incentive need not enter the final ranking algorithm to affect a shopping assistant's recommendation: it may instead influence which preference question the assistant asks. We make this distinction experimentally observable in a deliberately small, synthetic setting. Each task has two products, three verified numerical attributes, a price limit, and a private fixed preference vector. An honest simulated user answers one pairwise question. A separate recommender receives the products...
  </details>

- **2026-09-29** — Faiz Ghifari Haznitrama, Afrizal Hasbi Azizy, Faeyza Rishad Ardi — [Large-scale factor analysis shows machine intelligence is only partially interpretable](http://arxiv.org/abs/2609.36515v1)
  <details><summary>📄 Abstract</summary>
  A common assumption in language model development is that cognitive abilities are organized around a general, domain-free intelligence factor, like fluid intelligence in humans. This assumption is rarely tested directly, and prior attempts have done so only at a much smaller scale. We take a latent variable approach to intelligence in language models, similar to how psychometricians study psychological constructs. Performance in every specific problem set is influenced by a domain-specific and a...
  </details>

- **2026-09-28** — Jakob Steglich, Justus Meyer zu Bexten, Shakiba Moradi et al. — [Representational and Functional Robustness to Electrode Montages in EEG Foundation Models](http://arxiv.org/abs/2609.36288v1)
  <details><summary>📄 Abstract</summary>
  EEG foundation models (EEG-FMs) are intended to generalize across different datasets by learning representations that, ideally, are invariant to dataset-specific EEG configurations such as electrode montages. However, EEG-FMs that accept different montages as input do not guarantee that representations and predictions remain stable across different electrode configurations, especially outside the training setting. In this work, we investigate the effects of different electrode montages through a...
  </details>

- **2026-09-28** — Liner Xiang, Wenbo Zhang, Hengrui Cai — [OTROPE: Optimal Transport-based Robust Off-policy Evaluation for Large Language Models](http://arxiv.org/abs/2609.36264v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of large language models (LLMs) is essential for their development and deployment, yet is often costly, risky, and difficult to perform safely online. We study off-policy evaluation for LLMs, where limited human-labeled data from a behavior model are used to evaluate a newer target LLM. This setting is challenging because labels are scarce, behavior--target distribution shift is common, and response likelihoods are often unavailable for black-box LLMs. We propose the Optimal ...
  </details>

- **2026-09-28** — Matthieu Queloz, Pierre Beckmann — [A Polyphonic Conception of AI Understanding](http://arxiv.org/abs/2609.36079v1)
  <details><summary>📄 Abstract</summary>
  When a doctor, a judge, or an engineer must decide whether to trust an AI model's output, they cannot avoid asking what the model understands. Purely mathematical or statistical descriptions struggle to distinguish trustworthy from untrustworthy outputs without reintroducing the question of AI understanding in all but name. Yet the question is ill-framed as it stands, because the inherited concept operates within a monophonic paradigm: the idea that a cognitive system's understanding of somethin...
  </details>

- **2026-09-28** — Zhuoyuan Yu, Jiacheng Wang, Tianle Liu et al. — [F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement](http://arxiv.org/abs/2609.35575v2)
  <details><summary>📄 Abstract</summary>
  The real-world performance of current vision-language-action models is fundamentally constrained by the limited coverage of expert demonstrations and their insufficient understanding of physical interactions. A common remedy is to collect additional real-world demonstrations of newly encountered failures. However, this process is costly, inefficient, potentially unsafe, and difficult to scale. To address this challenge, we propose Failure for Rising (F4R), a failure-driven real-to-sim-to-real cl...
  </details>

- **2026-09-28** — Xiaozuo Shen, Yifei Cai, Tian Tan et al. — [When Trees Are Not Enough: Learning Mixed-Topology Feature Graphs with Adaptive Graph Sparse Autoencoders](http://arxiv.org/abs/2609.36294v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) expose interpretable features in large language model activations, yet existing structured SAEs impose single-parent trees or forests, while post-hoc graphs permit multiple parents but neither guide feature learning nor ensure reliable relation recovery. We introduce the Adaptive Graph Sparse Autoencoder (AG-SAE), a structure-guided training paradigm that treats each feature's complete parent set as an atomic structural hypothesis and lets evidence select zero, one, or...
  </details>

- **2026-09-28** — Ali Alfageeh, Rahul Gopinath, Amin Alipour — [How Much Prompt Is Enough? A Blackbox Minimization of Few-Shots in LLMs](http://arxiv.org/abs/2609.36289v1)
  <details><summary>📄 Abstract</summary>
  Prompts are the primary mechanism for directing the behavior of large language models (LLMs). Yet the internal structure and causal hierarchy of prompts remain poorly understood: which parts are causally necessary and which are redundant is an open question. This opacity can have severe consequences. Subtle prompt variations can silently shift model outputs in critical software systems, and engineers lack techniques to reason about prompt reliability.   We present \framework, a blackbox prompt-m...
  </details>

- **2026-09-28** — Myokyung Han, Taegyoon Kim, Jinhyuk Yun et al. — [The Uneven Decline of Collective Knowledge Production: Evidence from Stack Overflow After Generative AI](http://arxiv.org/abs/2609.36069v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (Gen AI) is reshaping how individuals learn and work, but its consequences for collective knowledge, the shared body of knowledge that online communities produce together, remain poorly understood. Prior work has documented an aggregate decline in participation on knowledge-sharing platforms, but it remains unclear which specific kinds of knowledge are being lost first. We study this question using Stack Overflow, one of the largest online communities for software engineering, trea...
  </details>

- **2026-09-28** — Yinuo Ren, Haoxuan Chen, Grant M. Rotskoff et al. — [FluxLite: Inference-Time Proposal Control for Discrete Diffusion Models](http://arxiv.org/abs/2609.35947v1)
  <details><summary>📄 Abstract</summary>
  Many inference-time tasks for pretrained discrete diffusion models and diffusion language models reduce to drawing samples from a tilted version of the pretrained distribution. Feynman-Kac sequential Monte Carlo (SMC) makes this correction exact in principle, but its prescribed weights routinely degenerate when the proposal dynamics are misaligned with the tilt, capping the practical gains from additional particles. We introduce FluxLite, a lightweight, training-free proposal-control framework f...
  </details>

- **2026-09-28** — Sidharth Pulipaka, Ansh Sharma, Stanislau Hlebik et al. — [Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents](http://arxiv.org/abs/2609.35576v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a r...
  </details>

- **2026-09-28** — Kseniya Belousova, Anna Konanykhina, Zilya Murzina et al. — [Physics-informed self-supervised generation of digital brain MRI phantoms from weighted images using differentiable MRI simulation](http://arxiv.org/abs/2609.35273v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To develop a physics-informed, self-supervised framework for generating digital brain MRI phantoms directly from conventional weighted MR images without requiring ground-truth parametric maps or anatomical segmentation. Methods: The framework predicts T1, T2, and proton density (PD) maps from T1-, T2-, and PD-weighted images and reconstructs the input images through an MRI signal model. Three generative architectures (variational autoencoder (VAE), generative adversarial network (GAN), ...
  </details>

- **2026-09-28** — Victor L. Qin, Nicolas Lanzetti, Saverio Bolognani et al. — [Strategically Robust Game-Theoretic Multi-Agent Trajectory Optimization](http://arxiv.org/abs/2609.35142v1)
  <details><summary>📄 Abstract</summary>
  Aviation authorities worldwide expect Advanced Air Mobility (AAM) traffic management to be decentralized among service providers, requiring AAM flights to autonomously plan trajectories by predicting other flights' control inputs rather than relying on centralized coordination. Game-theoretic approaches that formulate multi-agent collision avoidance as an exact dynamic potential game can efficiently find open-loop equilibria, but they assume that agents exactly follow their equilibrium trajector...
  </details>

- **2026-09-28** — Haoyang Zou, Yao Wang, Jun Yao et al. — [LoRo-Mark:Provably Lossless and Robust Agent Watermarking](http://arxiv.org/abs/2609.34080v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents are increasingly deployed as commercial services, protecting proprietary orchestration logic and tool-use policies is important. We consider agent repackaging: an adversary integrates a protected agent into its own application via API and presents it under its own identity. It may modify parts of execution to obscure the source. The owner typically has only black-box access to the repackaged service, so black-box ownership verification is essential. Agent watermarking embeds owners...
  </details>

- **2026-09-28** — Zhilin Guo, Boqiao Zhang, Oszkár Urbán et al. — [Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose](http://arxiv.org/abs/2609.35764v1)
  <details><summary>📄 Abstract</summary>
  Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth labels), we show the reliability problem is channel-level: a channel ablation isolates foot acceleration ...
  </details>

- **2026-09-28** — Tianjian Liu, Shicheng Feng, Jin'ao Shang et al. — [LLM-Assisted Automatic Security Proofs for Cryptographic Protocols: How Far Are We?](http://arxiv.org/abs/2609.35434v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential for assisting software and security analysis tasks, yet their effectiveness in cryptographic symbolic protocol verification remains insufficiently understood.   In this paper, we conduct the first systematic evaluation of the capability of state-of-the-art LLMs in cryptographic symbolic protocol verification. To quantify this capability, we propose \textsc{CRoST} (Coverage Rate of Solve Tree), a proof-based metric derived from the verifier...
  </details>

- **2026-09-28** — Julianna Piskorz, Antonin Berthon, Mihaela van der Schaar — [On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics](http://arxiv.org/abs/2609.35259v1)
  <details><summary>📄 Abstract</summary>
  On-policy learning has been argued to reduce catastrophic forgetting, produce sparser parameter updates, and improve generalisation. However, existing comparisons between supervised fine-tuning and reinforcement learning vary many factors simultaneously, making the contribution of rollout policy difficult to isolate. We study the effect of rollout policy in a controlled strong-to-weak distillation setting, by independently varying rollout policy, token-level KL direction, and learning rate acros...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 11 papers

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

- **2026-09-29** — Bowen Yuan, Danny Wang, Ruihong Qiu et al. — [Tracing the Evidence: Faithful Token Attribution Through Vision-Language Reasoning](http://arxiv.org/abs/2609.37656v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) exhibit strong reasoning capabilities, yet the visual and textual evidence supporting the generated responses remains difficult to identify. Faithful token attribution explains an LVLM's response by assigning scores that rank image and prompt tokens by how much the model relies on them, such that removing higher-ranked tokens causes the likelihood of the generated response to drop more rapidly. However, existing token-attribution methods have been developed m...
  </details>

- **2026-09-29** — Van Bach Nguyen, Jörg Schlötterer, Christin Seifer — [Targeted Visual Counterfactual Explanations for Contrastive Vision-Language Model](http://arxiv.org/abs/2609.37638v1)
  <details><summary>📄 Abstract</summary>
  Current explanation methods for contrastive vision--language models such as CLIP mainly identify important regions without showing how to change the input in order to get a target prediction. We introduce \textbf{M}ask-guided \textbf{A}daptive \textbf{C}ounterfactual \textbf{E}xplanations (\mace), a targeted visual counterfactual method designed specifically for CLIP zero-shot classification. \mace constructs an editable region from either source attribution or source--target attribution differe...
  </details>

- **2026-09-29** — David Achara, Maryam Sultana, Alexander D. Rast et al. — [XU-RS: Explaining Credal Width in Random-Set Language Models](http://arxiv.org/abs/2609.37594v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty estimates tell us how unsure a model is, but not why. Without knowing which parts of an input influences a model's uncertainty, we cannot tell whether that uncertainty score depends on input features that are relevant for the task. We study this problem in randomset classifiers built using pretrained language models. These classifiers assign probability to individual answers and to groups of answers, producing lower and upper probabilities for each answer; The difference between thes...
  </details>

- **2026-09-29** — Shanwen Mao, Mingming Li, Hao Zhang et al. — [How Can Recommendation Feedback Evolve Agent Memory?](http://arxiv.org/abs/2609.37544v1)
  <details><summary>📄 Abstract</summary>
  Content-generation agents continuously receive impressions, clicks, conversions, and negative feedback from recommendation systems, providing real-world outcome signals for memory evolution. However, these signals are delayed and noisy, confounded by audience composition, placement, and recommendation policies, and may result from the combined influence of multiple memories, making accurate attribution difficult. Existing methods rely primarily on immediate feedback or semantic retrieval and the...
  </details>

- **2026-09-29** — Olga Ohrimenko — [Eternal Sunshine of the Spotless Mind: Systematically Erasing LLM's Memories](http://arxiv.org/abs/2609.36414v1)
  <details><summary>📄 Abstract</summary>
  We consider persistent LLMs that accumulate memories of their interactions with a user over time. Such LLMs maintain memories using external storage, which they can query to overcome the limitations of a fixed context window. Such systems have numerous practical applications, as they can draw on all past interactions when responding to user queries.   In this paper, we ask whether LLMs can forget information shared with them upon a user's request. We find that current LLMs fail to delete such in...
  </details>

- **2026-09-28** — Sibo Liu — [Audience-Bound Persistent Memory: Authorization Across the Memory Lifecycle](http://arxiv.org/abs/2609.36373v1)
  <details><summary>📄 Abstract</summary>
  A personal language agent that acts for its owner across private and shared conversations can learn a fact from one audience and later place it in the context it assembles for another. We study authorization before context across the whole memory lifecycle. Each memory item carries the audience present when it was recorded; derived items are partitioned by audience, receive the intersection of their sources' audiences, or are suppressed; an audience widens only by an explicit, object-specific gr...
  </details>

- **2026-09-28** — Niklas Koenen, Claudia Battistin, Jeriek Van den Abeele et al. — [A Hierarchy of Entropy-Shapley Games for Multivariate Predictive Uncertainty](http://arxiv.org/abs/2609.35217v1)
  <details><summary>📄 Abstract</summary>
  Modern probabilistic machine learning models increasingly produce multivariate outputs with complex dependence structure, from multi-step time-series forecasts to sample path predictions. Understanding which input features drive the predictive uncertainty is important for risk-aware decisions, model diagnostics, and deciding whether the uncertainty should be mitigated or hedged against. This attribution problem requires a choice of how dependencies between output components are treated. Existing...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 5 papers

- **2026-09-29** — Ping Liu, Chi Zhang — [Motion Concept Unlearning in Video Diffusion Models](http://arxiv.org/abs/2609.36832v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) diffusion models can generate realistic depictions of actions such as kicking, stabbing, and shooting, raising safety concerns that motivate targeted concept erasure. Although concept erasure has been extensively studied for static concepts in text-to-image and T2V models, erasing motion concepts remains largely unexplored. We present a systematic study of motion concept erasure in video Diffusion Transformers (DiTs). Through causal interventions, we show that text-conditioni...
  </details>

- **2026-09-29** — Tianhao Qian, Ziming Hong, Chongyang Gao et al. — [Storage Is Not Strategy: State-Conditioned Support Control for LLM Unlearning](http://arxiv.org/abs/2609.37858v1)
  <details><summary>📄 Abstract</summary>
  Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization. The parameters most associated with a target, however, need not be the best ones to update, and candidate interventions can change value as optimization proceeds. In a controlled experiment, a storage-localization score reaches an area under the receiver operating characteristic curve (AUROC) of 0.981, yet storage identity agrees with the ...
  </details>

- **2026-09-29** — Amrita Singh, Aditya Joshi, Jiaojiao Jiang et al. — [LAURA: Knowledge Distillation for Interpretable Ambiguous Clause Identification in Legal Contracts](http://arxiv.org/abs/2609.36707v1)
  <details><summary>📄 Abstract</summary>
  Legal contracts contain ambiguities that expose enterprises to financial and legal risks. Some ambiguities allow flexible interpretation without triggering disputes, while others lead to significant legal conflicts. This makes identification alone insufficient, and interpretable rationale analysis essential. We propose LAURA, a post-training framework for interpretable ambiguous clause identification. LAURA leverages knowledge distillation with an IRAC-Unlearning prompting technique to transfer ...
  </details>

- **2026-09-28** — Zhengyang Shan, Jiayun Xin, Yanjun Lin et al. — [UNBIND: UNlearning By INference-time Directional Steering for Code LLMs](http://arxiv.org/abs/2609.35913v1)
  <details><summary>📄 Abstract</summary>
  Code large language models acquire programming capabilities from large code corpora, but can also memorize implementations that later require removal. Code unlearning is needed to control their continued reproduction when copyright or security concerns arise. However, targeted and retained code share computational patterns, creating a tension between forgetting specific implementations and preserving general programming ability. We propose \textbf{UNBIND}, a code unlearning framework that separa...
  </details>

- **2026-09-28** — Bardh Prenkaj, Andrea D'Angelo, Davide Mottin et al. — [Causal Routing for Unlearning](http://arxiv.org/abs/2609.34475v1)
  <details><summary>📄 Abstract</summary>
  LLMs cannot forget the way we delete a file. Strangely, we are asked to remove something that was never put anywhere in particular. What the model took from a piece of text is now smeared across billions of weights. Existing methods rewrite all of them to change one thing, and none of them say which part produced that change. To address this, we introduce Causal Routing for Unlearning (CRU) by asking where the concept is expressed in the model and suppressing only that part. One untrained forwar...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 4 papers

- **2026-09-29** — Wenbin Hu, Huihao Jing, Haochen Shi et al. — [CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning](http://arxiv.org/abs/2609.36820v1)
  <details><summary>📄 Abstract</summary>
  Group Relative Policy Optimization (GRPO) is widely used to train reasoning language models, where it computes advantages by centering and normalizing rewards across rollouts of the same prompt. For multiple rewards, GRPO sums the reward components and normalizes the total reward by its within-group standard deviation. The corresponding variance equals the sum of all pairwise reward covariances. For a fixed centered reward, larger aggregate covariance produces smaller advantages, and vice versa,...
  </details>

- **2026-09-29** — Yu Cheng, Yongkang Hu, Shuaijie Ma et al. — [SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time](http://arxiv.org/abs/2609.36580v1)
  <details><summary>📄 Abstract</summary>
  LLM agents deployed in real-world environments continually encounter new tasks and safety risks, while execution feedback typically becomes available only after each task is completed. However, existing self-evolving approaches commonly rely on multiple rounds of optimization over fixed and repeatedly accessible task distributions, fundamentally differing from test-time adaptation in real-world deployment, where only experience accumulated from past tasks can be used to improve safety decisions ...
  </details>

- **2026-09-29** — Jose Tupayachi, Xueping Li, Soham Das — [Learning to Harvest Without Collapse in a Regenerative Commons: A Lagrangian Framework](http://arxiv.org/abs/2609.36478v1)
  <details><summary>📄 Abstract</summary>
  The tragedy of the commons poses a multi-agent safety problem: reward-seeking agents can deplete a shared resource, and cooperation among its users does not itself specify how much must be preserved. We make preservation an explicit requirement by formulating a regenerative commons as a constrained Markov game or a constrained multi-agent MDP with a designer-specified depletion budget. We develop a nonstationary Lagrangian framework that constructs a policy sequence from solutions of unconstrain...
  </details>

- **2026-09-28** — Guy Lupo, Nguyen Hung Nguyen, Viet Vo et al. — [Continuous Assurance of Agentic Security Auditors for Software Delivery Decision Gates](http://arxiv.org/abs/2609.35266v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based repository auditors are increasingly deployed as security controls within continuous integration (CI) pipelines, where their findings admit, block, or delay software changes. As Agentic Software Development Life Cycle (SDLC) Security Controls, their non-deterministic behaviour changes the evidence, while organisational risk appetite and jurisdictional or data-sovereignty policy change its interpretation. Point-in-time audits therefore cannot maintain current assu...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 8 papers

- **2026-09-29** — Yuhao Liu, Yiming Zhong, Hanqing Wang et al. — [UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception](http://arxiv.org/abs/2609.37264v1)
  <details><summary>📄 Abstract</summary>
  Affordance perception aims to localize actionable regions supporting embodied interaction, yet 2D and 3D affordance grounding have evolved as separate problems, with different task definitions, supervision formats, datasets, and evaluation protocols. This fragmentation limits the learning of transferable object-affordance semantics across visual and geometric spaces. We propose Token Router for Tasks, a multitask training paradigm for MLLM-based systems that routes contextual hidden states to ta...
  </details>

- **2026-09-29** — Josepha Michiko Leo, Hyun-seok Min, Yehoon Jang et al. — [Grounded Revision vs. Prior Injection: Probing Retrieval-Augmented Patent Claim Amendment](http://arxiv.org/abs/2609.36550v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation is widely used in professional writing, yet whether retrieval grounds revision or merely injects templates is rarely tested where "correct" has a definable meaning. Patent claim amendment supplies that signal: the examiner names the attacked limitation and cites prior art, providing per-case ground truth. We release three artifacts: (i) a corpus of 7,385 USPTO prosecution cases with XML-aligned pre/post claims, rejection, and cited prior art; (ii) a seven-probe bat...
  </details>

- **2026-09-29** — Manyu Li, Xunkai Li, Yongfu Xiong et al. — [OmniVCBench: Benchmarking Evidence-Grounded Multimodal Reasoning Towards AI Virtual Cells](http://arxiv.org/abs/2609.37773v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence Virtual Cells (AIVCs) are envisioned as scientific agents that simulate cellular responses, explain underlying mechanisms, and support hypothesis-driven discovery. Existing AIVC benchmarks, however, operate primarily at the simulation layer, motivating complementary evaluation of how models interpret experimental evidence and formulate biological hypotheses. We introduce OmniVCBench, a figure-centric, source-traceable benchmark for the interpretation component of an AIVC....
  </details>

- **2026-09-29** — Divyansh Chandarana, Sandipan De, Vivek Gupta — [DraftTrace: A Multi-View Analytics Environment for AI-Integrated Writing](http://arxiv.org/abs/2609.36544v1)
  <details><summary>📄 Abstract</summary>
  Generative AI has changed how students produce writing assignments. The final artifact is no longer sufficient to understand the process through which it was produced. We introduce DraftTrace, a writing environment that jointly captures three complementary views of writing: the final product, the writing process and interactions with an integrated AI-assistant. DraftTrace reconstructs how a document develops over time and organizes these signals into submission, longitudinal, and class-level ana...
  </details>

- **2026-09-28** — Rafael Garcia-Dias, Alexandre Triay Bagur, Chayanin Tangwiriyasakul et al. — [Making Cross-Continental Federated Learning Repeatable with FLIP: a Multi-Application Study](http://arxiv.org/abs/2609.36001v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) in healthcare remains challenging, as the overhead of rebuilding governance guarantees for every collaboration stops most projects at the proof-of-concept stage. Here we present FLIP (Federated Learning Interoperability Platform), an open-source, multi-application platform that makes FL training and evaluation repeatable. FLIP implements common FL workflows as a set of composable services: cohort queries against per-site structured databases, on-demand DICOM retrieval fro...
  </details>

- **2026-09-28** — Marx Wang, Ella Zhang, Cameron Tan et al. — [Right Words, Wrong Moment: A Clinician-Grounded Analysis of Distress in 19,930 Conversations between Young People and ChatGPT](http://arxiv.org/abs/2609.35953v1)
  <details><summary>📄 Abstract</summary>
  Young people increasingly turn to General-Purpose Conversational Agents (GPCAs), such as ChatGPT, in moments of distress. We examine young adults' (ages 18-25) experiences using ChatGPT. We first collected 19,930 ChatGPT conversations and survey data from 158 young adults. We then selected five example conversations reflecting user distress. Finally, we asked ten clinicians to review those five conversations. We found distressed participants reported greater emotional engagement with ChatGPT and...
  </details>

- **2026-09-28** — Haojian Huang, Zexi Li, Junhao Guo et al. — [In-Context Learning for Robots: Methods and Applications](http://arxiv.org/abs/2609.36012v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robots must infer what a new task requires and translate that understanding into appropriate physical action. In-context learning (ICL) for robots supports this process by using demonstrations and interaction to direct existing competence with neural parameters held fixed during deployment. We organize this literature review around the interfaces connecting contextual evidence to execution, distinguishing four families: context-conditioned policies, geometric demonstration transf...
  </details>

- **2026-09-28** — D. Gilman, A. M. Nierenberg, J. Gurian et al. — [JWST lensed quasar dark matter survey V: Hints of self-interacting dark matter from 29 quadruply imaged quasars](http://arxiv.org/abs/2609.35974v1)
  <details><summary>📄 Abstract</summary>
  Theories of self-interacting dark matter (SIDM) predict the eventual core collapse of dark matter halos, a process that transforms these structures into extremely efficient gravitational lenses. We present a population-level inference on the abundance of core collapsed halos and subhalos in the mass range $10^6 - 10^{10.7} M_{\odot}$ using 29 quadruply imaged quasars, drawing on the collective lensing signal of many low-mass perturbers. Our structure formation model predicts the abundance of col...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 169 papers

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

- **2026-09-29** — Jade Choghari, Pepijn Kooijmans, Mansi Agarwal et al. — [FineART: Fine-grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation](http://arxiv.org/abs/2609.36416v1)
  <details><summary>📄 Abstract</summary>
  Robots operating in real-world environments must execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions. Current manipulation datasets struggle to support this capability: although single-arm datasets reach hundreds of thousands of trajectories, they typically provide only one high-level instruction per episode while the rare bimanual effort that does label subtasks annotates only a fraction of its hours. We present FineART, a densely annotated bimanua...
  </details>

- **2026-09-29** — Jisho Miyazaki, Kohdai Kuroiwa, Mio Murao — [Dynamical resource theory of time-reversal symmetry breaking](http://arxiv.org/abs/2609.36408v1)
  <details><summary>📄 Abstract</summary>
  Time-reversal symmetry and its violation (T-violation) are fundamental across diverse physics domains, from particle physics to fluctuation theorems and reciprocity. While time-reversal symmetry for isolated systems is simply determined by the Hamiltonian, quantifying the magnitude of T-violation, especially in noisy quantum processes, has been a subject of ongoing debate. Here, we propose an operationally meaningful framework to quantify the intrinsic T-violation of quantum channels. We integra...
  </details>

- **2026-09-29** — Zihan Wang, Zhen Wu, Pieter Abbeel et al. — [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](http://arxiv.org/abs/2609.38172v1)
  <details><summary>📄 Abstract</summary>
  Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We propose PRISM, a real-to-sim-to-real framework that overcomes this limitation by amplifying a handful of real videos into a large, diverse tra...
  </details>

- **2026-09-29** — Cailyn Smith, Geoffrey Sun, Henny Admoni et al. — [BlenDAgger: Blended Shared Control for Interactive Imitation Learning](http://arxiv.org/abs/2609.37599v1)
  <details><summary>📄 Abstract</summary>
  Robot policies are frequently trained from human corrections, yet teleoperating a robot to provide corrections is burdensome, and human demonstrators are not always optimal. We propose Blended DAgger (BlenDAgger), an approach for collecting data to train imitation learning policies by using shared control to blend the policy's and demonstrator's actions during interventions. By blending human and policy actions, we aim to improve the autonomous performance of manipulation policies. We validate o...
  </details>

- **2026-09-29** — Shifeng Bao, Fanding Huang, Yihan Lin et al. — [RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation](http://arxiv.org/abs/2609.37583v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models can coordinate long-horizon robot manipulation, yet successful task reasoning still depends on whether local physical interactions produce the intended effects. We study how repeated interaction can improve this capability without updating the base model. We introduce RoboHarn-Evo, a dual-loop harness that evolves Hierarchical Physical Knowledge (HPK) from physical experience. HPK couples two levels of reusable knowledge: Task Knowledge captures which subtask should be exe...
  </details>

- **2026-09-29** — Johannes Hechtl, Yannik Blei, Simon Ball et al. — [Wrench-ACT: Enhancing Robot Policies for Contact Rich Behavior Using Direct Wrench Control](http://arxiv.org/abs/2609.37552v1)
  <details><summary>📄 Abstract</summary>
  While contact-rich manipulation requires deliberate regulation of interaction forces, recent approaches to robot manipulation learning predominantly represent actions as target positions or poses. Even methods that incorporate force sensing either use it solely as an observation or, when predicting forces as part of the output, rely on a hybrid force controller. In this paper, we propose an imitation learning policy that predicts wrenches as its sole action output for direct use by a pure force ...
  </details>

- **2026-09-29** — Hongjie Fang, Shirun Tang, Junjian Hu et al. — [FP2: Equipping Robotic Foundation Models with Force Control](http://arxiv.org/abs/2609.37433v1)
  <details><summary>📄 Abstract</summary>
  Robotic foundation models (RFMs) are increasingly capable of general-purpose manipulation, yet reliable physical interaction remains challenging in contact-rich settings. We present FP2, a lightweight downstream interface that equips task-adapted RFMs with explicit force control while preserving their action-generation capability. FP2 adopts an action-regulation decomposition: the task-adapted RFM serves as a foundation policy responsible for task-level action generation, while a high-frequency ...
  </details>

- **2026-09-29** — T. Konstantin Rusch, Tim Seyde, Jared Boyer et al. — [Looped Actor: Depth-Recurrent Reasoning Models for Reinforcement Learning](http://arxiv.org/abs/2609.37432v1)
  <details><summary>📄 Abstract</summary>
  Looped reasoning models repeatedly apply a shared set of parameters, enabling more computation without increasing the model size. These models also support input-dependent computation by dynamically deciding when to stop looping. Motivated by the recent success of looped transformers in language modeling and reasoning, we investigate whether dynamic looping can similarly benefit sequential decision-making. We provide a complexity-theoretic motivation for this approach by showing that there exist...
  </details>

- **2026-09-29** — Jian Ma, Runxin Yu, Tianyu Tang et al. — [An LLM-powered Agent Framework for Heterogeneous Evacuation Behavior Modeling under a Moving Threat in a Public Plaza](http://arxiv.org/abs/2609.37009v1)
  <details><summary>📄 Abstract</summary>
  Modeling heterogeneous evacuation behavior under a moving threat is difficult because human perception, memory, and evidence evaluation are not well captured by fixed rules. We propose a novel LLM-powered agent-based framework to represent these internal decision processes. Each pedestrian agent perceives a private symbolic ASCII view, maintains a Memory-based Knowledge Graph derived solely from individual observations, and makes decisions through persona-conditioned prompts under a common sampl...
  </details>

- **2026-09-29** — Mingyue Huo, Shivam Mehta, Bhavin Jawade et al. — [Louder, Longer, Livelier: Acoustic Shortcuts and Underspecified Rationales in Speech LLM Judges](http://arxiv.org/abs/2609.36979v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge is widely used for evaluating text, but extending this paradigm to speech requires models to interpret acoustic as well as linguistic evidence. This introduces a modality-specific risk: a speech judge may treat a perceptually salient cue as evidence of quality even when that cue is irrelevant to the target criterion or receives more weight than human listeners give it. We call this behavior an acoustic shortcut. To study it, we audit six speech LLM judges using controlled manipula...
  </details>

- **2026-09-29** — Yize Liu, Huang Huang, Yining Hong et al. — [T$^2$Mem: Learning Test-Time Memory for Robotics](http://arxiv.org/abs/2609.36720v1)
  <details><summary>📄 Abstract</summary>
  Memory-dependent robotic manipulation requires policies to use information that is no longer available in the current observation. Retaining history alone is insufficient: memory must preserve information that supports future actions. One challenge is whether a memory-free foundation model can learn to retain and use historical information from action demonstrations alone, without external memory support. We introduce T$^2$Mem, a framework that develops this capability within a pretrained vision...
  </details>

- **2026-09-29** — Jianshu Zhang, Ce Zhang, Xiyuan Yang et al. — [Video2Skill: From Streaming Experience to Reusable Embodied Skills](http://arxiv.org/abs/2609.36691v1)
  <details><summary>📄 Abstract</summary>
  Manipulation behaviors vary widely across objects and scenes, but they share a small set of reusable skills, and planning with these skills helps embodied agents generalize to new tasks. Yet an agent can only plan with skills it knows. Recovering skills from observed experience, the inverse of planning, builds this knowledge over time and yields skill data for training future agents. Vision-Language Models (VLMs) describe individual manipulation events well, but can they organize a stream of eve...
  </details>

- **2026-09-29** — Jianshu Zhang, Keliang Wu, Chengxuan Qian et al. — [ProgressCompass: Embodied Progress Reward Models Are Lost Without the Right Context](http://arxiv.org/abs/2609.36684v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents now take on ever longer tasks. For long tasks, knowing only whether a task finally succeeds or fails says little; the steps along the way matter. Progress Reward Models (PRMs) score how far a task has come at every step, and serve as dense rewards, verifiers and monitors. Yet in long tasks the current frame alone often cannot tell how far the task has come, because progress depends on what happened before. We call this problem context-dependent progress estimation. Existing bench...
  </details>

- **2026-09-29** — Yuyou Zhang, Yunbei Zhang, Miao Li et al. — [Simple Agentic Memory for Generalist Robot Policies](http://arxiv.org/abs/2609.36595v1)
  <details><summary>📄 Abstract</summary>
  Visual-memory systems commonly retain or compress past observations. Robot control additionally requires interaction-derived state that no individual frame may explicitly represent, such as persistent identity relations, accumulated progress, or ordered procedures. We introduce Simple Agentic Robot Memory (SimpleARM), a training-free memory layer for frozen generalist robot policies. From the task instruction, SimpleARM specifies what to monitor; frozen perceptual tools maintain compact typed st...
  </details>

- **2026-09-29** — Joseph Metcalfe, Sara Sharifzadeh, Fabio Caraffini — [Cropland PAtteRNS: Parallel Dimensional Attention Networks and Attention to Dataset Disparity for Crop Segmentation in Satellite Imagery Time Series Data](http://arxiv.org/abs/2609.38165v1)
  <details><summary>📄 Abstract</summary>
  The landscape of satellite imagery time series datasets and boundary-pushing architectures for cropland segmentation has never been richer. However, in this gold rush, important truths are being missed on both fronts, as a drive for the most novel concepts or the largest datasets pushes finer details to the side. In this paper, we present our hybrid transformer-convolutional model, Cropland Parallel Attention and Refinement Network for Segmentation (PAtteRNS), the first model to use self-attenti...
  </details>

- **2026-09-29** — Yu Xu, Yuxin Zhang, Xiao Yang et al. — [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](http://arxiv.org/abs/2609.38140v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE), popularized by large language models, is a promising paradigm for scaling visual generative models. However, conventional token-wise MoE routes tokens independently within a homogeneous expert pool and regularizes expert usage toward uniformity, making it poorly matched to video data that is spatiotemporally redundant and semantically long-tailed. We show that existing visual MoEs fall into a uniformity trap: semantically under-organized routing, compounded by uniform e...
  </details>

- **2026-09-29** — Tianqi Liu, Nayoung Kim, Julia Sebastien et al. — [IMPACT: Modeling Socially Interdependent Movement in a Generative Multi-Agent Simulation of a Pompeian Household](http://arxiv.org/abs/2609.38113v1)
  <details><summary>📄 Abstract</summary>
  Simulations of archaeological sites can make interpretations of past cultural practices observable and examinable. Generative multi-agent simulations offer a bottom-up approach to modeling how people collectively moved through and used historical spaces. However, current agents designed to simulate everyday life often plan and act independently, limiting their ability to capture how movement depends on others' actions. We introduce IMPACT (Interdependent Movement Planning through Inter-Agent Con...
  </details>

- **2026-09-29** — Cutter Dawes, Nick Alonso, Tom Figliolia et al. — [How Local Mixing Encodes Relative Position in Global NoPE Attention](http://arxiv.org/abs/2609.38109v1)
  <details><summary>📄 Abstract</summary>
  The attention operation is naively position invariant. However, positional information is fundamental to natural language, and therefore a variety of explicit position encodings have been developed in transformer-based models, such as rotary position encoding (RoPE). Although explicit position encodings have long been assumed to be required, recent methods that interleave local mixing layers, such as sliding window attention (SWA) and gated linear attention, while not encoding position (NoPE) in...
  </details>

- **2026-09-29** — Ganesh Pavan Kartikeya Bharadwaj Kolluri, Michael Kampouridis, Ravi Shekhar — [Pruning for Efficiency, Paying in Fairness: Demographic Disparities in Pruned Speech-LLMs](http://arxiv.org/abs/2609.38106v1)
  <details><summary>📄 Abstract</summary>
  Speech-LLMs are expensive to run, making compression important for real-world deployment. However, compressed models are usually selected using aggregate word error rate (WER), which can hide how pruning affects different demographic groups. In this work, we systematically study the effect of audio encoder pruning on SLAM-ASR for different demographic groups. Using the Fair-Speech and Common Voice datasets, we found that the pruning does not affect all demographic groups equally; the gap between...
  </details>

- **2026-09-29** — Xiwei Zeng, Shengrong Li, Yiheng Liu et al. — [BrainNet Studio: A Unified Toolkit for Brain Network Construction, Intelligent Analysis, and Visualization](http://arxiv.org/abs/2609.37956v1)
  <details><summary>📄 Abstract</summary>
  Brain networks characterize structural and functional relationships among brain regions and support research on cognition, brain disorders, and brain-computer interfaces. Their time-varying topology and higher-order spatiotemporal dependencies are not adequately represented by conventional static networks. Existing tools primarily focus on static connectomes and provide limited integration of dynamic network modeling with modern graph and sequence learning methods. We present BrainNet Studio, an...
  </details>

- **2026-09-29** — Paul Rosa — [Semiparametric Bernstein-von Mises theorems from Stein's method](http://arxiv.org/abs/2609.37939v1)
  <details><summary>📄 Abstract</summary>
  We introduce a novel proof strategy for semiparametric Bernstein-von Mises theorems based on Stein's method combined with an information-geometric framework. Rather than controlling the effect of the prior on the asymptotic marginal posterior distribution of the functional of interest through the stability of an integrated likelihood under a suitable perturbation, we characterise its influence through the prior-weighted divergence of suitable vector fields over the statistical model. Applying St...
  </details>

- **2026-09-29** — Joel Anto Paul, Litu Rout, Aditya Akella et al. — [Time-Anchored Diffusion Language Models: Latent-Space Caching for Fast Generation](http://arxiv.org/abs/2609.37924v1)
  <details><summary>📄 Abstract</summary>
  Recent work on anchored diffusion language models improves denoising by shaping an intermediate latent space with supervised important-token targets. In this work, we introduce time-based (self-supervised) anchoring, which learns and reuses latent anchors without requiring such targets. Our key observation is that anchors encode persistent properties of the clean sequence, such as its semantic intent, global structure, or intermediate plan. Although their hidden representations become stale as t...
  </details>

- **2026-09-29** — Liang He, Jingbo Wen, Yixiong Chen et al. — [You Cannot Pick a Provider From the Price List: Market-Aware Routing for Open-Weight LLM Inference](http://arxiv.org/abs/2609.37902v1)
  <details><summary>📄 Abstract</summary>
  Existing LLM routers choose among models using static per-model costs. We show that open-weight inference markets introduce a second, largely ignored decision axis: after choosing a model, a client must still choose which provider serves it. Measuring live endpoints across [nummodels] open models, competing providers, multiple task types, and three measurement waves, we find that provider choice cannot be inferred from the price list. The same model can vary sharply in quality, latency, availabi...
  </details>

- **2026-09-29** — Bhanu Prakash Vangala, Sowmya Guda, Navya Vangala — [How Many Labels Does a Language Need? Annotation Budgets and Cross-Lingual Pooling for African-Language Text Classification](http://arxiv.org/abs/2609.37882v1)
  <details><summary>📄 Abstract</summary>
  Every text classifier for an African language begins with a budgeting question: how many labelled examples are needed, and can labels from other African languages stand in for them? We answer both questions empirically for 28 language-task pairs, news topic classification in 16 languages (MasakhaNEWS) and tweet sentiment in 12 languages (AfriSenti), using a character n-gram linear model that trains in seconds on two CPU cores with no pretrained weights and no accelerator. Monolingual learning cu...
  </details>

- **2026-09-29** — Timur Mudarisov, Mikhail Burtsev, Radu State — [Retrieval Capacity of Self-Attention Under Competition](http://arxiv.org/abs/2609.37879v1)
  <details><summary>📄 Abstract</summary>
  How many tokens from its context does a language model actually use, and what determines that number? We study this question through self-attention. Without retraining, we retain only the tokens with the highest attention weights at each head, layer, and query, keeping their original weights unchanged. By varying the selected set size and measuring the increase in negative log-likelihood (NLL), we estimate the effective attention set size needed to stay within a chosen loss tolerance. Relatively...
  </details>

- **2026-09-29** — Fabian A. Mikulasch, Friedemann Zenke — [Predictive Self-Supervised Learning Provably Identifies Stochastic Signals under Nuisance](http://arxiv.org/abs/2609.37789v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning (SSL) by predicting in latent space, without generating the input data itself, learns highly abstract, useful representations. Intuitively, this success is often attributed to its ability to discard nuisance information that is irrelevant to prediction. However, this poses a conundrum: both stochastic variation in a prediction-relevant latent signal and true nuisance make observations partly unpredictable; how could they be distinguished? Surprisingly, we prove that comm...
  </details>

- **2026-09-29** — Rémi Kazmierczak, Johanne Cohen, Marianne Clausel — [CHOQOLATE: Organizing Concept Bottleneck Latent Spaces with Choquet Integrals](http://arxiv.org/abs/2609.37786v1)
  <details><summary>📄 Abstract</summary>
  Concept Bottleneck Models (CBMs) built on vision-language models such as CLIP represent a latent space as human-understandable concepts. These representations are unfaithful: related concepts are entangled, so individual scores do not reflect their intended meaning. We propose CHOQOLATE, an interpretable-by-design layer based on 2-additive Choquet integrals, which merges correlated concepts into compact nodes. Across four datasets, CHOQOLATE achieves a favorable accuracy-interpretability trade-o...
  </details>

- **2026-09-29** — Johannes Schlüter, Alexander Schönhuth — [CancerZigZag: Iterative Seed-Anchored Diffusion for Generative Modeling of Single-Cell State Transitions](http://arxiv.org/abs/2609.37735v1)
  <details><summary>📄 Abstract</summary>
  Single-cell cancer datasets are predominantly cross-sectional and rarely provide paired or longitudinal observations linking individual healthy-like cells to tumor-associated states. We introduce CancerZigZag, a seed-initialized diffusion-based framework for exploratory generation of tumor-associated single-cell candidate clouds from unpaired epithelial cell populations. For each cancer context, a diffusion model is trained exclusively on tumor-derived epithelial cells and applied through repeat...
  </details>

- **2026-09-29** — Tue M. Cao, Lisiane Pruinelli, My T. Thai — [Weights Read and Write Features: Scalable Parameter Decomposition Grounded in Activation Space](http://arxiv.org/abs/2609.37731v1)
  <details><summary>📄 Abstract</summary>
  Activation space and parameter space provide complementary views of model computation. Activations represent information, while weights read, transform, and write that information. Yet existing interpretability methods largely study the two spaces separately, leaving the connection between represented information and parameter-level computation underexplored. We introduce Activation-Supported Parameter Decomposition (ASPD), which jointly decomposes activation and parameter spaces and grounds eac...
  </details>

- **2026-09-29** — Artur C. Fassoni — [Stochastic gradient descent on the epigenetic landscape: a unified framework for cellular plasticity, tumor heterogeneity, and the asymptotic irrelevance of fitness](http://arxiv.org/abs/2609.37703v1)
  <details><summary>📄 Abstract</summary>
  Phenotypic plasticity, the ability of cells to switch between states, is central to development, differentiation, and therapy resistance. Although it is modeled at several scales, from compartmental ODEs to phenotype-structured PDEs and single-cell stochastic equations, a framework connecting these descriptions is missing. We present such a framework. Starting from a general $n$-compartment ODE model encompassing nonlinear growth and linear transitions between phenotypes, we show, with a new, el...
  </details>

- **2026-09-29** — Adhemar de Senneville, Xavier Bou, Jérémy Anger et al. — [Are In-Context Images Worth 10 Dimensions?](http://arxiv.org/abs/2609.37659v1)
  <details><summary>📄 Abstract</summary>
  There has been significant work on understanding the In-Context Learning capabilities of Large Language Models, especially on the induction circuit. For a few-shot classification task, the induction circuit leverages linear representations of each labeled example in-context in order to classify an unlabeled query. However, few works focus on how those linear representations are built in the first place. Leveraging the expressivity of the vision modality compared to text, we uncover a Shared Disc...
  </details>

- **2026-09-29** — Abhinav Rajeev Kumar, Paras Chopra — [Authority Bias in Language Models: Source Deference and User Agreement Are Not Interchangeable](http://arxiv.org/abs/2609.37616v1)
  <details><summary>📄 Abstract</summary>
  Language models tend to agree with whatever a user asserts, and post-training increasingly targets this sycophancy so that models evaluate claims on their merits rather than deferring to the user. Yet the same models are far more compliant when a wrong answer is attributed to a verified source, which is how retrieval results, tool outputs, and grounded-search content often present information. We measure this gap across five open-weight families and three closed APIs. A single verified-source no...
  </details>

- **2026-09-29** — Yuxiang Yao, Zijun Zhao — [GraphVQ: Structure-Aware Autoregressive Decoding over Context-Quantized Graph Tokens](http://arxiv.org/abs/2609.37604v1)
  <details><summary>📄 Abstract</summary>
  Graph foundation models need a discrete token representation, but casting a graph as a generatable token sequence faces a structural obstacle: edges spanning beyond the serialization window cannot be emitted in one pass--so one-pass autoregressive generators systematically under-produce cycles--and a single global condition cannot tell candidate edges apart. GraphVQ removes both obstacles: node contexts--features plus a local edge mask under multi-order breadth-first serialization--are quantized...
  </details>

- **2026-09-29** — Sangsidhya Kar — [Why Adaptive Optimizers Underestimate Rare Tokens](http://arxiv.org/abs/2609.37535v1)
  <details><summary>📄 Abstract</summary>
  In the softmax output layer, a rare token receives a small positive logit gradient on most steps and a much larger negative gradient on the few steps when it is the target. SGD simply adds these contributions. Coordinate-wise adaptive methods such as Adam, RMSProp, and sign descent instead divide each update by a running estimate of its magnitude, and that estimate is largest immediately after the token appears. This imbalance has two effects. At the level of the whole output layer, we character...
  </details>

- **2026-09-29** — Yuren Hao — [Physical Muon: Orthogonalization as an Equilibrium Computation](http://arxiv.org/abs/2609.37525v1)
  <details><summary>📄 Abstract</summary>
  Physical neural networks and analog in-memory computing could reduce the energy cost of neural network training. Realizing this potential, however, requires optimizers that combine effective learning with physical implementability. SGD fits local analog updates but struggles on transformers, while Adam family is unstable against analog bias. Muon offers strong training performance, but its Newton--Schulz orthogonalization relies on dense matrix-matrix products. To address this obstacle, we intro...
  </details>

- **2026-09-29** — Salvatore Di Stefano, Marta Zoppello — [A posteriori controllability of non-linear remodelling in linear elastic continua](http://arxiv.org/abs/2609.37411v1)
  <details><summary>📄 Abstract</summary>
  We investigate the a posteriori controllability of remodelling within the framework of Geometric Control Theory applied to continuum systems. Remodelling is described through an isochoric Bilby--Kroner--Lee decomposition, where the internal structural transformation is represented by a remodelling tensor and its evolution is governed by a stress-driven constitutive law. Assuming infinitesimal deformation and remodelling stretches, while retaining finite rotations of the principal remodelling dir...
  </details>

- **2026-09-29** — Xianghan Wei, Xiaoda Yang, Zhi Wang et al. — [Complementary Retrieval-Augmented Prompting for Consistent Long-Form Video Generation](http://arxiv.org/abs/2609.37407v1)
  <details><summary>📄 Abstract</summary>
  While recent video foundation models excel at generating high-quality short videos, long-form video generation remains a critical challenge, where a major bottleneck lies in conditioning independently generated shots to preserve consistent characters, scenes, and objects throughout a story. Existing training-free approaches typically condition target shots using retrieved historical visuals. However, these references often suffer from severe informational mismatch, either introducing irrelevant ...
  </details>

- **2026-09-29** — Kodai Kawamura, Kenji Kawaguchi, Anji Liu — [Rethinking Soft Tokens for Parallel Decoding in Diffusion Language Models](http://arxiv.org/abs/2609.37391v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) enable parallel generation by predicting and committing multiple tokens at each denoising step, yet they can generate individually plausible but mutually inconsistent tokens. Recent work shows that \emph{soft tokens} can mitigate this issue by representing uncertain positions with continuous embeddings built from the model's predictive distribution at the previous decoding step. However, although soft tokens are commonly understood as preserving predictive uncert...
  </details>

- **2026-09-29** — Sumit Srivastav, Per Eng-Johnsson, Raimund Feifel et al. — [Ionization-Driven Dehydrogenation and Molecular Growth in Gas-Phase Adamantane Clusters](http://arxiv.org/abs/2609.37385v1)
  <details><summary>📄 Abstract</summary>
  We investigate fragmentation and molecular growth induced by keV ions in initially neutral gas-phase adamantane clusters, the simplest diamondoid molecule (Ad, C$_{10}$H$_{16}$). Using time-of-flight mass spectrometry in combination with quantum-chemical calculations, we find that intact cluster cations undergo extensive dehydrogenation. We also observe a distinct distribution of singly charged products with masses predominantly between those of the adamantane monomer and dimer cations. We attri...
  </details>

- **2026-09-29** — Jiale Dai, Liuxian Ma, Xiaoke Niu et al. — [VISTA: Value-Informed Event Appraisal for Multimodal Emotion Conflict](http://arxiv.org/abs/2609.37324v1)
  <details><summary>📄 Abstract</summary>
  Conflicting emotional cues can be individually valid: a subdued voice may reflect a blocked goal while a smile satisfies a social obligation. Their interpretation depends on what the event means to the person. We introduce VISTA (Value-Informed Semantic Trust Arbitration), a learned seven-field appraisal interface that conditions modality arbitration on concerns, event relations, and expression conditions while retaining a joint-evidence residual. A log-odds decomposition separates emotion expec...
  </details>

- **2026-09-29** — Marcin Postolak — [The alternative scalar field dark sector of the Universe: Cosmological inflation, quintessence and ekpyrotic model in the framework of scalar-tensor cosmology](http://arxiv.org/abs/2609.37293v1)
  <details><summary>📄 Abstract</summary>
  This dissertation investigates scalar field descriptions of the dark sector (of the Universe), with emphasis on scalar-tensor cosmology, inflationary effective field theory, quintessence, and ekpyrotic/cyclic alternatives to inflation.   The thesis first reviews scalar-tensor theories of gravity, starting from Brans-Dicke theory and extending to general non-minimally coupled scalar fields. Particular attention is paid to the interpretation of the scalar field, the relation between the Jordan and...
  </details>

- **2026-09-29** — Siqi Lu, Suo Wei, Yongbin Zheng et al. — [Beyond Attention Imbalance: Mitigating Hallucinations via Spectral Surgery](http://arxiv.org/abs/2609.37263v1)
  <details><summary>📄 Abstract</summary>
  While Large Vision-Language Models (LVLMs) achieve remarkable success, hallucinations remain a significant barrier to their reliable deployment. Recent studies primarily attribute these issues to cross-modal attention imbalances; most solutions therefore focus on reweighting visual tokens or suppressing language priors. However, such approaches often overlook the spectral characteristics of the visual information flow and frequently rely on Contrastive Decoding (CD), which doubles inference time...
  </details>

- **2026-09-29** — Aakash Kumar Tiwari — [CredWise: A Controlled Agentic Decision-Intelligence Framework for Explainable and Auditable Credit-Risk Assessment](http://arxiv.org/abs/2609.37223v1)
  <details><summary>📄 Abstract</summary>
  Credit-risk prediction is important in banking, but a prediction alone does not explain why an applicant is risky or how it should be combined with other evidence. This paper presents CredWise, a decision-support framework that integrates credit-risk prediction, probability calibration, explainable artificial intelligence, policy retrieval, SQL analytics, and controlled agent-based workflows. An XGBoost model is trained on Lending Club data (1,345,310 loans, 18 features) using a temporal split: ...
  </details>

- **2026-09-29** — Zhehao Huang, Changxin Tian, Qingyuan Yang et al. — [Trajectory Soup: Pushing the Compute-Scaling Frontier of LLM Mid-training via Diverse Trajectories](http://arxiv.org/abs/2609.37169v1)
  <details><summary>📄 Abstract</summary>
  Mid-training equips pretrained large language models with specialized and reasoning capabilities, but the returns of this stage are bounded since additional serial compute yields little further downstream improvement and can even degrade some capabilities, which places a practical ceiling on how much compute mid-training absorbs. We revisit how this compute should be allocated to a single run or multiple similar optimizations. We find that branches forked from a shared checkpoint under various c...
  </details>

- **2026-09-29** — Mei Wu, Rui Xie, Runyu Zhang et al. — [MatToolBench: Benchmarking Multimodal Agents in Real-World Materials Science Workflows](http://arxiv.org/abs/2609.37053v1)
  <details><summary>📄 Abstract</summary>
  Multimodal GUI agents have achieved impressive results on general software benchmarks, yet their ability to operate professional scientific software remains largely unexplored. In materials science, sparse domain-specific web data, specialized interfaces, and tacit workflow conventions create blind spots that general-purpose pretraining cannot readily bridge. We present MatToolBench, the first real-environment benchmark for evaluating multimodal GUI agents on professional materials science softw...
  </details>

- **2026-09-29** — Shinan Zhang, Tao Zhang, Qihui Zhu et al. — [LatCom: Cross-Agent Latent Compression for Efficient Multi-Agent Collaboration](http://arxiv.org/abs/2609.37017v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) increasingly use latent collaboration to avoid the information loss and repeated encoding-decoding overhead of natural-language communication. However, directly forwarding all sender latents makes the receiver-side context scale with both the number of agents and the reasoning length, increasing computation, memory usage, and collaboration latency. A natural solution is latent compression. But we find that cross-agent redundancy remains unresolved in existing ...
  </details>

- **2026-09-29** — Xingyu Jia, Baole Ai, Ang Wang et al. — [Parameterized Stripe Attention for Efficient Video Generation](http://arxiv.org/abs/2609.37001v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) enable high-quality video generation but suffer from substantial inference latency, primarily attributable to the computationally expensive full spatio-temporal attention. While sparse attention methods offer potential solutions, existing approaches face an inherent flexibility--efficiency dilemma: predefined masks lack the flexibility to capture diverse attention patterns, while runtime-determined masks introduce overheads and sacrifice hardware efficiency. We iden...
  </details>

- **2026-09-29** — Xiaoxun Gong, Zechen Tang, Woochang Kim et al. — [Deep Learning GW Quasiparticle Hamiltonians for Many-Body Excited-State Electronic Structure at Scale](http://arxiv.org/abs/2609.36962v1)
  <details><summary>📄 Abstract</summary>
  Accurate quasiparticle electronic structures are the foundation for understanding excited-state properties of materials and explaining optoelectronic, quantum, and transport phenomena. First-principles GW calculations nevertheless remain computationally intensive for large or configurationally complex systems. Here we introduce DeepH-GW, a deep-learning framework that predicts an effective GW quasiparticle Hamiltonian directly from atomic structure. Building on the local, equivariant message-pas...
  </details>

- **2026-09-29** — Yiwei Liu — [Beyond Readability: Evaluating Task Information Recoverability](http://arxiv.org/abs/2609.36957v1)
  <details><summary>📄 Abstract</summary>
  Direct visual readability and task-information recoverability are different quantities. Failure to decode a target from a fixed observation need not eliminate access to that target through another recovery route. We develop an evaluation perspective that makes the observation, query, target, and available knowledge explicit and measures the overlap between routes' success sets. For information available on the original visible surface under suitable imaging conditions, direct optical recovery re...
  </details>

- **2026-09-29** — Vincent D. Zaballa, Elliot E. Hui — [Scalable Diffusion SBI for Compositional Inference under Simulator Misspecification](http://arxiv.org/abs/2609.36950v1)
  <details><summary>📄 Abstract</summary>
  Simulation-based inference is challenging when many heterogeneous observations must be composed, hierarchical latent structure must be preserved, and the simulator is misspecified relative to observed data. We develop sampling and fine-tuning methods for diffusion-based inference in design-conditional settings, where the same simulator is queried across different experimental conditions $ξ$. We extend compositional score-based inference with a continuous-time diffusion coefficient that accounts ...
  </details>

- **2026-09-29** — Zhiwei Wang, Yanxi Chen, Yaliang Li et al. — [Fine-Tuning on Self-Generated and Reward-Weighted Data: Learning Dynamics, Convergence Rates, and Benefits of Off-Policyness](http://arxiv.org/abs/2609.36945v1)
  <details><summary>📄 Abstract</summary>
  We study the learning dynamics of fine-tuning a policy model on self-generated and reward-weighted data, with particular focus on a generalized version of REINFORCE -- referred to as RE(S) -- that updates the rollout distribution once every $S \ge 1$ gradient steps. Prior work in bandits and reinforcement learning has developed rich theory for policy gradient methods, and on-policy sampling (i.e., a small $S$, ideally $1$) is often viewed as crucial to their success; yet in prominent application...
  </details>

- **2026-09-29** — Mario Sanz-Guerrero, Minh Duc Bui, Manuel Mager et al. — [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation](http://arxiv.org/abs/2609.36931v1)
  <details><summary>📄 Abstract</summary>
  Reproducibility is essential for scientific research, yet prior work shows that LLM outputs vary with hardware and batching. We identify an overlooked factor: the hidden injection of the current date into system prompts, which users cannot control and which changes every day. Across 9 recent LLMs and 6 datasets spanning multiple-choice QA (MCQA), math reasoning, code generation, and machine translation, performance varies solely with the current date, with deltas of up to 6% on MCQA, 14% on math...
  </details>

- **2026-09-29** — Chien-Feng Liu, Chih-Kai Yang, Bo-Han Feng et al. — [When Capabilities Fail to Compose: Diagnosing the Compositionality Gap in Large Audio-Language Models](http://arxiv.org/abs/2609.36921v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) perform strongly on individual audio tasks, but whether these capabilities can be reliably composed remains underexplored. We conduct a controlled diagnostic study of capability composition in LALMs, requiring models to integrate audio-attribute recognition, cue-conditioned segment selection, and downstream ASR or question answering. We construct two-utterance inputs with distinct acoustic cues to evaluate composition across environmental sound, gender, and em...
  </details>

- **2026-09-29** — Chihiro Taguchi, Yotaro Kubo, Rujikorn Charakorn — [BaLEEN: Biasing with Latent Encoded Entities for Context-Aware ASR](http://arxiv.org/abs/2609.36913v1)
  <details><summary>📄 Abstract</summary>
  Transcribing domain-specific entities and rare proper nouns remains a major challenge in automatic speech recognition (ASR). In this paper, we propose BaLEEN (Biasing with Latent Encoded Entities), a lightweight, hypernetwork-based framework for dynamic contextual adaptation without fine-tuning the underlying ASR model. BaLEEN encodes variable-length contextual keywords using a pretrained language model, compresses them into a fixed sequence of latent vectors via a Perceiver bottleneck, and inje...
  </details>

- **2026-09-29** — Jiahui Li, Hao Nie, Yibo Zhu et al. — [Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators](http://arxiv.org/abs/2609.36899v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training increasingly relies on long-horizon, multi-turn rollouts. As post-training jobs outgrow a single cluster, rollout pools assembled across clusters introduce hardware heterogeneity. Rollout scheduling must serve two stakeholders: the hardware needs high aggregate decode throughput, while each trajectory needs to finish quickly. The tension arises from the memory-bandwidth-bound nature of autoregressive decoding. A large active batch amortizes weight reads ...
  </details>

- **2026-09-29** — Zhenwen Ji, Lei Jin, Shanyong Wang et al. — [Momentum-Coupled Rubric Adaptation for Detailed Image Captioning](http://arxiv.org/abs/2609.36893v1)
  <details><summary>📄 Abstract</summary>
  Detailed image captioning requires accurate and comprehensive descriptions of fine-grained visual content, yet caption quality spans factual accuracy, information coverage, and clarity. Compared with conventional methods that rely mainly on high-quality supervision or holistic rewards, rubric-based reinforcement learning decomposes these requirements into explicit criteria and provides targeted, structured feedback. However, existing methods often use separate models for caption generation, rubr...
  </details>

- **2026-09-29** — Zeyu Gan, Zixuan Gong, Yong Liu — [Harness Evolution as Learning: Approximation, Generalization, and Optimization Limits of Self-Improving Personal Agents](http://arxiv.org/abs/2609.36892v1)
  <details><summary>📄 Abstract</summary>
  As the capabilities of large language models (LLMs) continue to advance, increasing attention is turning to how to translate their abilities into useful behavior. Personal agents bring this question into everyday settings, where models are expected to serve individual users and continually adapt to their preferences. With the underlying model held fixed, such adaptation relies on harness engineering: designing and evolving the surrounding layer that manages context, memory, tools, and execution....
  </details>

- **2026-09-29** — Kaichen Ouyang, Chenglei Yu, Chuanrui Wang et al. — [SINO: Scale-Invariant Neural Operator](http://arxiv.org/abs/2609.36890v1)
  <details><summary>📄 Abstract</summary>
  In scientific machine learning, physical fields governed by partial differential equations exhibit low-rank structure and scale invariance. When solving equations on coarse grids, missing information leads to the closure problem: modeling unresolved physics to recover lost dynamics. Although closure terms depend on grid resolution, they represent scale-invariant physical laws. A model truly learning physics should capture these mechanisms with low-rank parameterization rather than memorizing gri...
  </details>

- **2026-09-29** — Ziqian Zou, Conghao Wong, Qinmu Peng et al. — [Socialality Anchors: Towards Group-bounded Trajectory Prediction](http://arxiv.org/abs/2609.36852v1)
  <details><summary>📄 Abstract</summary>
  Trajectory prediction is a key component for understanding human behavior patterns in dynamic scenes. Researchers have devoted substantial efforts to modeling social interactions, especially group-wise interactions, since group membership often reflects shared intention, coordinated motion, and stable mutual adaptation, thus providing a persistent and semantically meaningful social prior for forecasting. However, existing group modeling methods may rely on a fixed threshold and infer groups main...
  </details>

- **2026-09-29** — Zheyu Shen, Guanhua Wang, Dezhan Tu et al. — [ARC-KV: Amortizing Anchor Search for Reconstruction-Based KV Cache Compaction](http://arxiv.org/abs/2609.36835v1)
  <details><summary>📄 Abstract</summary>
  Long-context large language model inference is bottlenecked by KV caches that grow linearly with sequence length. This burden is especially severe for long, reusable context prefixes, whose cache must serve many downstream queries. Reconstruction-based methods such as Attention Matching achieve strong downstream task performance with compact KV caches. However, iterative anchor search dominates the compaction cost of OMP-based Attention Matching. This motivates our selective amortization princip...
  </details>

- **2026-09-29** — Long Li, Qichao Zhao, Yue Yang et al. — [Spotter: Let the Embodied Model Lead, and the VLM Reflect for It](http://arxiv.org/abs/2609.36808v1)
  <details><summary>📄 Abstract</summary>
  Current embodied models do not respond to their own failures, although what just went wrong could inform a small adjustment on the next attempt, the kind of reflection behind the gains of thinking in language models. We test whether they can repair a known error, which requires producing a correction and judging whether it is right. Stopped at a failure and allowed to retry, they seldom repair it through their own randomness or from a language description of the error, and best-of-N selection ca...
  </details>

- **2026-09-29** — Kaijun Yin, Jun-Ping Du, Peijun Yu et al. — [Evidence for Distributed Fault Energetics and Their Impact on Deformation in a Chemically Complex Alloy](http://arxiv.org/abs/2609.36780v1)
  <details><summary>📄 Abstract</summary>
  Chemically complex alloys feature intrinsically heterogeneous local chemical environments and, consequently, fluctuations in local fault energetics. However, experimentally quantifying their relationship remains challenging, leaving the role of this distributed energy landscape in deformation mechanisms incompletely resolved. Here, we develop a distribution based framework linking experimentally measured stacking fault widths to deformation relevant apparent fault energy, revealing a distributed...
  </details>

- **2026-09-29** — Qi Cao, Kangning Liu, Xuan Kan et al. — [JudgeProfile: Understanding and Steering Subjectivity in LLM Judges](http://arxiv.org/abs/2609.36705v1)
  <details><summary>📄 Abstract</summary>
  LLM judges are inherently subjective, often favoring different responses in pairwise comparison when neither option is objectively wrong. To study this subjectivity, we introduce JudgeProfile, a framework that dissects LLM evaluation into perception (how a judge compares two responses across specific attributes like clarity, correctness, and detail) and prioritization (how much each attribute influences the final choice). We curate SubjectiveSet, a dataset of 50,013 response pairs from 17 public...
  </details>

- **2026-09-29** — Zizhao Li, Chengyi Cai, Mohammed Yaqoob Ansari et al. — [Reprogramming Vision-Language Models via Structured Prompt Reparameterization](http://arxiv.org/abs/2609.36680v1)
  <details><summary>📄 Abstract</summary>
  Visual reprogramming adapts pretrained models to downstream tasks by modifying their input and output interfaces while keeping the backbone fixed. In vision-language models, existing methods mainly rely on intra-class prompt aggregation and do not explicitly model relationships among classes. However, fine-grained categories often exhibit highly overlapping attribute descriptions and strong inter-class correlation in the text embedding space, where discriminative cues lie in subtle low-variance ...
  </details>

- **2026-09-29** — Zihan Jiao, Xinping Yi, Shi Jin et al. — [Surrogate-Enhanced Fractional Programming for MIMO Device-to-Device Interference Networks](http://arxiv.org/abs/2609.36586v1)
  <details><summary>📄 Abstract</summary>
  Interference management in multi-stream multi-input multi-output (MIMO) device-to-device (D2D) networks often leads to weighted sum-rate maximization with sum-log-determinant involving matrix-valued signal-to-interference-plus-noise ratios. The state-of-the-art paradigms, including weighted minimum mean-square error (WMMSE) and fractional programming (FP), have achieved tremendous success in link scheduling, power control, and beamforming problems. Recently, an upgraded FP approach, named surrog...
  </details>

- **2026-09-29** — Janet Wang, Yunbei Zhang, Xiao Wang et al. — [How Medical VLMs Underutilize Their Vision Encoders: A Dermatology Perspective](http://arxiv.org/abs/2609.36557v1)
  <details><summary>📄 Abstract</summary>
  Medical Vision-Language Models (VLMs) show significant promise for clinical image understanding, offering accurate diagnosis with interpretable reasoning. However, a critical performance gap exists between their strong vision encoders and the full multimodal model: in dermatology, the MedSigLIP encoder outperforms MedGemma by an average of 10.26 percentage points even when both use zero target-task labels; few-shot linear probing provides further evidence of strong visual representations. This g...
  </details>

- **2026-09-29** — Quan Xiao, Mingda Liu, Gaowen Liu et al. — [BRIDGE: Bilevel Retrieval-Credit-Aware Agentic Reinforcement Learning](http://arxiv.org/abs/2609.36505v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (ARL) with verifiable rewards improves the ability of large language models (LLMs) to tackle knowledge-intensive tasks by learning to interleave search and reasoning. However, most existing ARL methods optimize only LLM-generated tokens and treat retrieved evidence as environment observations. This creates an information-credit gap: failures caused by missing or misleading evidence are attributed to the LLM policy rather than to the retriever, which motivates train...
  </details>

- **2026-09-29** — Jinghan A Zeng — [A Polynomial Time Characterization For Strongly EFX Orientable Graphs](http://arxiv.org/abs/2609.36498v1)
  <details><summary>📄 Abstract</summary>
  Discrete fair division is the problem of dividing a discrete set of goods among agents in a fair manner. In this setting, one of the most sought-after notions of fairness is envy-freeness up to any good (EFX). In 2023, Christodoulou, Fiat, Koutsoupias, and Sgouritsa introduced the idea of a graphical valuation, where the fair division problem is represented by a simple graph where vertices are the agents and the edges are the goods, and each vertex only values incident edges. They showed that an...
  </details>

- **2026-09-29** — Sheryl Paul, Kexin Wang, Ruolin Li et al. — [Agent-Based Evolutionary Dynamics for Mixed Autonomy Weaving Ramps](http://arxiv.org/abs/2609.36424v1)
  <details><summary>📄 Abstract</summary>
  Existing models of mixed-autonomy weaving ramps characterize how altruistic connected and automated vehicles (CAVs) can improve traffic efficiency at the population level, but provide limited insight into how such behavior emerges from decentralized vehicle interactions or how it is affected by finite populations, heterogeneous preferences, and imperfect information. We develop an agent-based model of a macroscopic weaving-ramp framework in which individual vehicles adapt their lane choices usin...
  </details>

- **2026-09-28** — Om Shankar Tiwari, Tangi Vass, Gagan Deep Singh — [Assay: Claims That Decay With the Code. Content-Addressed Evidence Graphs for Accountable AI-Assisted Software Delivery](http://arxiv.org/abs/2609.36170v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents fail in two coupled ways. They spend most of their context window rediscovering where things live, and they assert success without evidence when the work gets hard. Repository indexes address the first with cheap context, and orchestration frameworks with adversarial review address the second with accountability. Both describe the same object, the structure of the codebase, at two timescales: what is true of the code now, and what was verified to be true, at which revision, by w...
  </details>

- **2026-09-28** — Jenny Y. Huang, Jiameng Fan, Ahmed Imtiaz Humayun et al. — [Language Models Are "Insecure" Reporters](http://arxiv.org/abs/2609.36139v1)
  <details><summary>📄 Abstract</summary>
  As large language models are deployed in increasingly autonomous long-horizon tasks, manually auditing and verifying the actions, artifacts, and outputs of models becomes more difficult. Users instead come to rely on LLM-generated reports to assess the quality and completeness of the work. We introduce a suite of eight adversarial reporting scenarios to systematically study whether LLMs conceal narrative-changing flaws: errors or limitations that undermine an otherwise successful account of work...
  </details>

- **2026-09-28** — Hanbin Zhou, Shangzhe Li, Alexander Braverman et al. — [Provable Benefits of Regularization: Fast Rates for Adversarial Imitation Learning](http://arxiv.org/abs/2609.35698v2)
  <details><summary>📄 Abstract</summary>
  We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner behavior. Historically, reward regularization and entropy-based policy regularization are key components of empirically successful methods such as GAIL and LS-IQ, yet their finite-sample benefits remain underexplored. We establish fast rates for jointly regularized AIL in finite-horizon Markov decision ...
  </details>

- **2026-09-28** — Yuyan Chen — [ARCagent: An Adaptive Retrieval Calibration Agent for Clinical Question Answering](http://arxiv.org/abs/2609.36392v1)
  <details><summary>📄 Abstract</summary>
  In diseases where clinical guidelines are incomplete, contested, or mutually contradictory, knowledge completeness and dynamic conflict-aware synthesis are two safety-critical properties that standard Retrieval-Augmented Generation systems do not provide. Therefore, we present \sysname, an adaptive retrieval calibration clinical question-answering agent for ME/CFS, a disease where diagnostic frameworks coexist and major guidelines actively contradict each other on treatment. ARCagent contributes...
  </details>

- **2026-09-28** — Ke Fang, Yupu Yao, Lu Cheng — [ATLAS: Aligned Transport of Latent Structure for Reliable World Model Planning](http://arxiv.org/abs/2609.36333v1)
  <details><summary>📄 Abstract</summary>
  Latent world models rely on representation geometry for planning, yet regularizing the latent marginal alone does not determine the state-to-state relationships used for action selection. We show that this can cause planning-relevant novelty structure to be weakened as representations are transformed into the final latent used by the planner. We introduce Aligned Transport of Latent Structure (ATLAS), a training objective that explicitly preserves relational geometry while calibrating the global...
  </details>

- **2026-09-28** — Mir Tafseer Nayeem, Susmoy Chakraborty, Davood Rafiei — [CineSubBench: Evaluating LLMs on Long-Form Narrative and Cultural Understanding from Multilingual Movie Subtitles](http://arxiv.org/abs/2609.36218v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly evaluated in specialized domains such as law, medicine, software engineering, and cybersecurity, yet film remains comparatively underexplored despite requiring long-form narrative integration, multilingual interpretation, and culturally situated audience judgments. We introduce CineSubBench, a benchmark for evaluating long-context film understanding from multilingual movie subtitles. A subtitle track represents a film as thousands of short, temporally order...
  </details>

- **2026-09-28** — Som Sagar, Ransalu Senanayake — [Test-Time Adaptation of Manipulation Policies Under Actuator Degradation](http://arxiv.org/abs/2609.36182v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulation policies are usually trained under the assumption that a commanded action produces the same motion as it did during training even after hours of operation. Real hardware violates this assumption as the motors gradually heat up, current saturates near contact, voltage sags under load, thus the same policy action can produce a weaker, delayed, or noisier motion. These conditions are already measured by onboard telemetry, such as joint temperature, motor current, and supply volta...
  </details>

- **2026-09-28** — Mia Zhang, Jizong Peng — [Boosting Metric Depth Completion via Training-Free Adaptive Response Geometry](http://arxiv.org/abs/2609.36168v1)
  <details><summary>📄 Abstract</summary>
  Depth completion aims to recover dense metric depth from sparse sensor measurements, increasingly leveraging visual foundation models as geometric priors. However, aligning these priors to true metric scale typically relies on rigid affine assumptions in predefined coordinate systems, leaving systematic calibration errors. Linearity in depth calibration depends on the response coordinate. We introduce adaptive response geometry, which makes the fixed choice of depth, log depth, or disparity an i...
  </details>

- **2026-09-28** — Joshua Chen, Peter Jan van Leeuwen — [Copula Active Subspaces I: A Score-Covariance Method for Reduced-Order Non-Gaussian Density Estimation](http://arxiv.org/abs/2609.36142v1)
  <details><summary>📄 Abstract</summary>
  In Bayesian inference problems with non-Gaussian observation noise, the posterior is only as accurate as the noise density, and gradient-based samplers need that density and its gradient evaluable pointwise, whether from an explicit expression or from code, and without an inner solve. We propose Copula Active Subspaces (CAS) to represent this noise density. A componentwise rank transform isolates the noise law's dependence in its copula, and a rank-$r$ reduction keeps only the directions along w...
  </details>

- **2026-09-28** — Eliott Morgensztern, Cesar Fierro Cota, Alessandro Mininno — [Solver Agent: an Agentic AI Framework for Theoretical Physics Computations Applied to F-theory Uplifts of O3-planes and S-folds](http://arxiv.org/abs/2609.35958v1)
  <details><summary>📄 Abstract</summary>
  We introduce Solver Agent, an AI framework based on large language models for calculations and proofs in mathematics and theoretical physics. The solution process is tracked through a persistent ledger that records assumptions, derivations, and computations. A central agent delegates tasks to specialized sub-agents, while independent agents verify both intermediate steps and the final result. This setup improves the traceability, reproducibility, and verification of computer-assisted calculation...
  </details>

- **2026-09-28** — Di Wen, Wenhao Guo, Yuedong Tan et al. — [HEIR: Learning Human-Entity Interactions with Functional Roles](http://arxiv.org/abs/2609.35955v1)
  <details><summary>📄 Abstract</summary>
  Understanding human-entity interactions requires recovering each person-action event's participants, roles, and shared identities. This structure can support embodied agents by clarifying who acts on which entities and how, informing anticipation and coordination in shared environments. Standard HOI metrics score individual links, leaving complete event composition undermeasured. We introduce HEIR (Human-Entity Interactions with Functional Roles), an image benchmark for complete grounded partici...
  </details>

- **2026-09-28** — Kerui Ren, Tao Lu, Linning Xu et al. — [GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](http://arxiv.org/abs/2609.35734v2)
  <details><summary>📄 Abstract</summary>
  Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consi...
  </details>

- **2026-09-28** — Ting-Chih Chen, Emile van Krieken, Shujian Yu et al. — [Question-Specific Knowledge Graphs for Efficient Visual Reasoning](http://arxiv.org/abs/2609.35942v1)
  <details><summary>📄 Abstract</summary>
  Recent work in visual question answering has shown that vision-language models can exhibit strong reasoning capabilities by translating visual inputs into textual representations. The effectiveness of this translation depends on how well visual details are retained; models need to surface and align both explicit and implicit knowledge sufficient to support reasoning, without introducing spurious assumptions. Existing methods that leverage detailed image captions introduce visual details unrelate...
  </details>

- **2026-09-28** — Azza Bouleimen, Nicolò Pagan, Anikó Hannák — [Illusory Truth or Mere Exposure? Model-Dependent Repetition Effects in LLM-Based Social Media Simulations](http://arxiv.org/abs/2609.36278v1)
  <details><summary>📄 Abstract</summary>
  Generative agent-based models (GABMs) are increasingly used to simulate social media dynamics, including misinformation spread. For such social simulations to be valid proxies of human behavior, LLM agents should replicate established human cognitive biases, among them the Illusory Truth Effect (ITE), where repeated exposure to a claim increases its perceived truth value. We investigate whether and how the ITE manifests across four LLMs (Gemma-3-4b-it, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct,...
  </details>

- **2026-09-28** — He Zhu, Lusen Zhao, Kwan Man Cheng et al. — [SkillWeaver: Agentic Exploration over Neural Interaction Skills for Scalable Robot Data Generation](http://arxiv.org/abs/2609.36171v1)
  <details><summary>📄 Abstract</summary>
  Large-scale demonstrations have driven unprecedented progress in robot learning, yet collecting robot data through teleoperation is expensive and difficult to scale to diverse environments and long-horizon tasks. Simulation offers a scalable alternative, but existing data-generation pipelines often rely on open-loop controllers, scripted skill sequences, or task-specific programs. We introduce SkillWeaver, an agentic framework that autonomously generates robot experience by exploring over Neural...
  </details>

- **2026-09-28** — Kehang Zhu, Anand Shah, David Parkes — [Engineering Simplicity: Simple Mechanism Interfaces Steer LLM Agents](http://arxiv.org/abs/2609.36365v1)
  <details><summary>📄 Abstract</summary>
  Can interaction formats and textual scaffolds help large language model (LLM) agents make better decisions, and do better decisions come with better explanations? We study these questions in auctions and matching, multi-agent environments with explicit rules and known optimal strategies. These settings let us vary how a decision problem is presented while retaining a benchmark for evaluating behavior. Drawing on human-motivated theories of simplicity, we compare interfaces that elicit a complete...
  </details>

- **2026-09-28** — Ming Du, Xiangyu Yin, Michael Prince et al. — [Strategies for Deploying AI Agents in Production at Scientific User Facilities](http://arxiv.org/abs/2609.36362v1)
  <details><summary>📄 Abstract</summary>
  Agentic artificial intelligence (AI) is moving beyond research demonstrations toward production use at scientific user facilities, including light sources, neutron sources, nanoscience centers, and autonomous laboratories. Its scientific value extends beyond increasing throughput. Agents can perform repeatable tasks in calibration, measurement execution, and quality control, as well as initial analyses that turn data into reviewable evidence, allowing scientists to focus on hypotheses, unexpecte...
  </details>

- **2026-09-28** — Jiarui Li, Zixiang Yin, Samuel Landry et al. — [Explainability from Training with Applications to TCR-Epitope Prediction](http://arxiv.org/abs/2609.36354v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models have achieved strong performance in artificial intelligence for science, yet their black-box nature limits our understanding of how they learn scientific tasks. Existing methods for interpretability provide limited insight into how models organize evidence and evolve during learning. We introduce explainability from training (EFT), a model-agnostic paradigm that traces model interpretation during training to explain why models rely on specific features and how they organize ...
  </details>

- **2026-09-28** — Amirhossein Abaskohi, Amirhossein Dabiriaghdam, Lele Wang et al. — [DeepRewind: Predicting and Repairing Premature Commitments in Deep Research Agents](http://arxiv.org/abs/2609.36344v1)
  <details><summary>📄 Abstract</summary>
  Deep-research agents conduct long-horizon investigations through iterative search, evidence evaluation, belief revision, and synthesis. However, they may commit to claims before sufficient evidence is available, causing later reasoning to reinforce an incorrect interpretation. We introduce DeepRewind, an additive control layer for reversible deep research that represents the agent's evolving epistemic state as a typed graph of sources, evidence, claims, hypotheses, assumptions, commitments, plan...
  </details>

- **2026-09-28** — Paul T. von Hippel — [Faster Estimates from Binned Test Score Data---and How Accurate They Are](http://arxiv.org/abs/2609.36312v1)
  <details><summary>📄 Abstract</summary>
  Education agencies often summarize test score distributions by counting how many students scored in 3 to 5 different \textit{bins}. The HETOP model transforms bin counts into estimated means and standard deviations, assuming that scores follow a normal distribution within each school or district. Past HETOP implementations ran slowly, taking 3--60 minutes, if they finished, when given bin counts for all 1,151 districts in Texas. Our new function, \code{fast\_hetop()} in the R package \pkg{binest...
  </details>

- **2026-09-28** — Thomas Jacob Maranzatto, Semih Akkoc, Sennur Ulukus — [The Role of Feed-Forward Layers in Transformer Dynamics](http://arxiv.org/abs/2609.36230v1)
  <details><summary>📄 Abstract</summary>
  We study the dynamical behavior of tokens in transformers from a control-theoretic perspective. Our model includes the feed-forward layer present after the self-attention mechanism, with the self-attention mechanism interpreted as an interacting particle system and the feed-forward layer as an independent control. Our main theoretical result establishes that the feed-forward network can steer the tokens arbitrarily close to consensus regardless of the key, query, and value matrices. Our result a...
  </details>

- **2026-09-28** — Bang Xiao, Wenqi Jia, Ozgur Kara et al. — [LeRF: Learning Reference Coordinate Frames for Perspective Taking Reasoning](http://arxiv.org/abs/2609.36219v1)
  <details><summary>📄 Abstract</summary>
  Perspective taking is a fundamental component of spatial intelligence, requiring models interpret spatial relations from a specified viewpoint, such as that of another entity or an imagined observer. Despite the increasing spatial reasoning capabilities of Vision-Language Models (VLMs), they still struggle with perspective taking, often defaulting to the camera viewpoint when a query requires reasoning from a different perspective. We introduce Learning Reference Coordinate Frames for Perspectiv...
  </details>

- **2026-09-28** — Xinming Dai, Qihang Jin, Tianshu Tan et al. — [Sparse-View Interpretable 3D Animal Behavior Representations for Neural Encoding and Decoding](http://arxiv.org/abs/2609.36217v1)
  <details><summary>📄 Abstract</summary>
  A deeper understanding of brain function requires a precise, structured characterization of behavior.Yet, extracting behavioral representations from video in a form suitable for scientific analysis remains a fundamental challenge. Many prior studies represent behavior via pose estimation or nonlinear video embeddings. However, pose tracking discards rich information beyond predefined keypoints, while nonlinear video embeddings lack interpretability. We address this limitation with SABLE (Sparse-...
  </details>

- **2026-09-28** — Shishi Xiao, Zichao Wang, Alexa Siu et al. — [FigAct: Turning Scientific Figures into Active Canvases for Explanation](http://arxiv.org/abs/2609.36190v1)
  <details><summary>📄 Abstract</summary>
  Scientific figures are designed to communicate information visually, yet MLLMs typically explain them by translating their visual content back into text. This requires readers to manually map the resulting explanations back to the figure. Inspired by how people present visual information, we introduce FigAct, a framework that transforms static scientific figures into question-conditioned visual presentations by acting directly on their existing graphical elements. Like a human presenter, FigAct ...
  </details>

- **2026-09-28** — Cristina Rossetti, Anna V. Kononova, Thomas Bäck et al. — [EvoMO-SR: Multiobjective LLM-based Evolution of Symbolic Expressions with substructure guidance](http://arxiv.org/abs/2609.36187v1)
  <details><summary>📄 Abstract</summary>
  Symbolic Regression (SR) is a data-driven method for scientific discovery which searches for interpretable analytical relationships within data. Recently, Large Language Models (LLMs) have also had a significant impact on scientific discovery, enabling the automation of various stages of the process. For these reasons, the possibility of harnessing the embedded scientific knowledge and programming capabilities of LLMs to solve SR tasks has emerged, showing promising performance compared with tra...
  </details>

- **2026-09-28** — Fahd Seddik, Fatemeh Fard — [Principled Thoughts for Latent Recursive LLM Systems](http://arxiv.org/abs/2609.36159v1)
  <details><summary>📄 Abstract</summary>
  Large language models can reason in continuous space instead of decoded text, by recurring on their own hidden states or by passing those states between agents, while training supervises only the Cross-Entropy (CE) of the final decoded answer and does not constrain the thought. Theoretical and empirical analyses establish and confirm four failures of CE-only training that lead to a lower probability of the correct answer such as collapsing thoughts across distinct questions and retaining irrelev...
  </details>

- **2026-09-28** — Yundaichuan Zhan, Weishi Wang, Wenbiao Liu et al. — [Dyad: Extending Large Language Models with Native Typed Decision-Making](http://arxiv.org/abs/2609.36116v1)
  <details><summary>📄 Abstract</summary>
  We study how to build more capable general-purpose agents by extending large language models (LLMs) with native typed decision-making. We introduce Dyad, an architecture that augments a pretrained LLM with an environment-conditioned action encoder that embeds each candidate action description in parallel, then scores these embeddings against the LLM's internal state to yield a distribution over typed actions. By factorizing decision-making into representations of the evolving interaction state a...
  </details>

- **2026-09-28** — Blaz Bertalanic, Carolina Fortuna — [An Exact Generate - Transform Decomposition of Small-LLM Team Scaling Across Orchestration Architectures](http://arxiv.org/abs/2609.36104v1)
  <details><summary>📄 Abstract</summary>
  Replacing one LLM agent with a collaborating team can raise accuracy, but whether scaling the team helps, and which architecture to scale, is unclear. Sweeping eight agent orchestration architectures across five instruction-tuned 7-9B models, five short-answer benchmarks, and an executable-code benchmark up to 30 calls, we find that the returns to team scaling are sharply task-dependent: from three to thirty calls accuracy rises by up to 17 points on the two arithmetic word-problem benchmarks (G...
  </details>

- **2026-09-28** — Hanbo Xie — [Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice](http://arxiv.org/abs/2609.36097v1)
  <details><summary>📄 Abstract</summary>
  Using predictive models to explain cognition requires more than accurate behavioral predictions. Input ablations offer an appealing route: remove information from a model and interpret the resulting performance change as evidence of its importance for behavior. Yet this inference assumes that the model's dependence on information reflects the dependence of the process generating the behavior. We test it in two synthetic sequential bandit tasks with known generating policies, where past choices c...
  </details>

- **2026-09-28** — Shen Yan, Duc Le, Irina-Elena Veliche — [HEAR: Real Voices, Real Bias: A Large-Scale Human-Recorded, Demographically Diverse Benchmark for Audio Language Models](http://arxiv.org/abs/2609.35952v1)
  <details><summary>📄 Abstract</summary>
  We introduce HEAR (Human-recorded Evaluation of Audio-LLM bias by Real speakers), a large-scale, ecologically valid benchmark comprising 87k real human audio samples from 843 demographically diverse participants. HEAR enables comprehensive evaluation through Multiple Choice Question Answering (MCQA) and open-ended long-form tasks. To our knowledge, this is the first large-scale voice benchmark grounded entirely in authentic human speech.   We evaluate model behavior across both real-time speech-...
  </details>

- **2026-09-28** — Hanbin Zhou, Shangzhe Li, Alexander Braverman et al. — [Provable Benefits of Regularization: Fast Rates for Adversarial Imitation Learning](http://arxiv.org/abs/2609.35698v1)
  <details><summary>📄 Abstract</summary>
  We study adversarial imitation learning (AIL), in which an agent learns to imitate expert demonstrations by optimizing a policy against an adversarial reward that distinguishes expert and learner behavior. Historically, reward regularization and entropy-based policy regularization are key components of empirically successful methods such as GAIL and LS-IQ, yet their finite-sample benefits remain underexplored. We establish fast rates for jointly regularized AIL in finite-horizon Markov decision ...
  </details>

- **2026-09-28** — MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi et al. — [Optimal Networks for Agentic Information Aggregation](http://arxiv.org/abs/2609.35537v1)
  <details><summary>📄 Abstract</summary>
  We study information aggregation in the networked learning model introduced by Kearns, Roth, and Ryu (SODA 2026). There is a fixed distribution over $d$ features and a common label. Agents learn in topological order on a directed acyclic graph. Each observes a subset of the features and its parents' predictions, fits a linear predictor to minimize mean squared error, and passes only its prediction forward. The global predictor is the best linear predictor using all features. Kearns, Roth, and Ry...
  </details>

- **2026-09-28** — Chengyang Li, Yujie Wan, Shuai Wang et al. — [Memory in the Sky: Low-Altitude Question Answering with Multi-Agent Memory Aggregation](http://arxiv.org/abs/2609.35431v1)
  <details><summary>📄 Abstract</summary>
  This paper studies low-altitude question answering (LAQA), in which distributed unmanned aerial vehicle (UAV) memories are aggregated at a ground server to answer questions about observations over a long horizon. Unlike conventional resource allocation based on sensing, communication, control, or computation metrics, LAQA requires an explicit measure of memory value. We propose a generative adversarial exam (GAE) that uses forward simulation to evaluate memory retrieval and exam scores to quanti...
  </details>

- **2026-09-28** — Ritam Bhaumik, Chun Guo, Xiaoning Guo et al. — [Indistinguishability of Sum of Permutations: A Fourier Analytic Route to Classical and Quantum Security](http://arxiv.org/abs/2609.35421v1)
  <details><summary>📄 Abstract</summary>
  We study classical and quantum indistinguishability of sums of independent random permutations and related transformations from permutations to functions. Let $G$ be a finite abelian group of order $N$, and let $π^k_+(x)=π_1(x)+\cdots+π_k(x)$ for $k\geq2$ independent uniform random permutations of $G$. We give a unified Fourier analytic treatment in which the construction is represented by its probability density and a distinguisher by its acceptance function, with the classical and quantum quer...
  </details>

- **2026-09-28** — Keyi Li, Yihao He, Quanyi Li — [Envy-Free Decompositions of Random Assignments: Settling Four Agents, and What Lies Beyond](http://arxiv.org/abs/2609.35192v1)
  <details><summary>📄 Abstract</summary>
  A random assignment of n indivisible objects to n agents is specified by its assignment matrix and implemented by drawing a deterministic assignment from a Birkhoff-von Neumann decomposition. Kawase et al. observed that the choice of decomposition matters for fairness: a matrix that is envy-free in the sense of stochastic dominance (SD-EF) can be decomposed so that some agent envies another with probability close to 1. They call a decomposition Dec-EF if every agent envies every other agent with...
  </details>

- **2026-09-28** — Benjamin Aminof, Tuan Khai Nguyen, Sasha Rubin — [FONDANT: Strong and Best-Effort Planning via Antichains](http://arxiv.org/abs/2609.35160v1)
  <details><summary>📄 Abstract</summary>
  A classical solution concept in fully observable nondeterministic (FOND) planning, is the strong policy (aka winning strategy in the closely related area of reactive synthesis), i.e., such a policy ensures that the goal is reached in an adversarial environment. When strong policies are not available or there is no evidence that the environment is adversarial, one can resort to best-effort policies, which always exist, and which follow the classic decision-theoretic principle that an agent should...
  </details>

- **2026-09-28** — Jeremy Canale — [DGF-Bench: A Benchmark for Simulating and Auditing Deception Against Multi-Agent Governance Boards](http://arxiv.org/abs/2609.34913v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents can review enterprise projects as governance boards do: they read the evidence, apply written rules and decide whether the project may proceed. Part of that evidence comes from suppliers and project members with a stake in the decision. DGF-Bench is a benchmark in which a board of agents (specialist gates and a General gate that consolidates their decisions) reviews synthetic dossiers while an attacker plants deceptive content in evidence the organization does no...
  </details>

- **2026-09-28** — Andrew Nguyen, Samson Kempiak, Agrim Gupta et al. — [MINT: Modeling GenAI Impact on Network Traffic](http://arxiv.org/abs/2609.35742v1)
  <details><summary>📄 Abstract</summary>
  Generative AI (GenAI) is becoming a mainstream network workload, yet packet-level simulators lack measure\-ment-driven GenAI traffic models. Currently researchers must approximate GenAI services using traditional sources such as file transfer and video streaming, limiting realistic network evaluation of scheduling and capacity planning. We present MINT, a measurement and modeling framework for GenAI network traffic. Using an isolated net\-work-namespace capture pipeline, we collect client-side t...
  </details>

- **2026-09-28** — Jonathan Light, Christopher Zhang Cui, Jeonghye Kim et al. — [Shockingly Simple Self-retrospection Improves Agentic Models Without RL](http://arxiv.org/abs/2609.35741v1)
  <details><summary>📄 Abstract</summary>
  People learn not only by repeating successful actions, but also by recounting and explaining their experiences, revising their understanding to guide future behavior. Can a language-model agent improve its future actions by training only on explanations of its own experience? We investigate this question by studying Retrospection-Only Fine-Tuning (ROFT), a minimal online procedure designed to isolate the effect of explanation-only training on subsequent behavior. The agent attempts a task, obser...
  </details>

- **2026-09-28** — Kerui Ren, Tao Lu, Linning Xu et al. — [GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](http://arxiv.org/abs/2609.35734v1)
  <details><summary>📄 Abstract</summary>
  Novel view synthesis from sparse images must reconcile faithful reconstruction of observed regions with plausible completion of unseen content, while maintaining world consistency across viewpoints. Existing geometry-based methods preserve observed scene structure but often struggle to complete unseen regions, whereas video generative models offer rich appearance priors but accumulate inconsistencies during sequential view generation. We propose GeoVerse, a framework that synthesizes world-consi...
  </details>

- **2026-09-28** — Ziyao Huang, Zhengkun Rong, Shiyang Qin et al. — [FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning](http://arxiv.org/abs/2609.35728v1)
  <details><summary>📄 Abstract</summary>
  We present FlowAct-R2, a framework for interactive humanoid video generation that combines continuous multimodal control with proactive agent planning. Our method consists of two coupled components. First, a Streaming Multimodal Reference Diffusion Transformer adapts the pretrained Seedance 2.0 Mini reference-to-video backbone to accept rolling action prompts, streaming audio, and dynamically updated image, audio, and video references. Video-driven rotary positional embeddings align reference ch...
  </details>

- **2026-09-28** — Li Zhang, Chuqin Geng, Mark Zhang et al. — [Rethinking Circuit Evaluation: Do Circuits Explain Model Errors?](http://arxiv.org/abs/2609.35686v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability (MI) aims to explain a model's behaviour through analyzing its internal computations; circuit-based explanations aim to isolate these computations with compact subnetworks validated by ablating the rest of the model. We show that circuits validated this way may fail to recover the underlying mechanism of the model's behaviour by closely reproducing its successful decisions while failing to account for most of its errors. Such explanations should account for the model...
  </details>

- **2026-09-28** — Matteo Musacchio, Juan Cruz Giner Pulero, Isabel Castañeda et al. — [QuanReview: Offline, Auditable Reconciliation of Human and LLM Span Annotations](http://arxiv.org/abs/2609.35685v1)
  <details><summary>📄 Abstract</summary>
  Structured span annotations, such as quantities with their units, uncertainty modifiers, and event classes, are expensive to create and hard to keep trustworthy once language models enter the loop. We present QuanReview, an open-source system for auditing and correcting such annotation layers. QuanReview aligns two annotation streams over the same documents at character level, resolves unambiguous cases by an explicit and logged policy, and routes candidate conflicts to a browser-based adjudicat...
  </details>

- **2026-09-28** — Haofeng Xu, Junwei Su, Lansong Diao et al. — [Reward-Aligned Reweighting for On-Policy Distillation](http://arxiv.org/abs/2609.35517v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student language model with dense feedback from a stronger teacher on student-generated trajectories. Yet standard OPD weights token-level distillation terms uniformly, implicitly treating local teacher preference as a proxy for correction utility. A decision's task value, however, depends on how the student completes the subsequent reasoning. This mismatch can cause imitation to suppress viable student strategies or reinforce paths the student cannot reliab...
  </details>

- **2026-09-28** — Takashi Furuya, Nicholas H. Nelsen, Frank Cole — [Universal Approximation of Measure-to-Measure Operators by Pushforwards](http://arxiv.org/abs/2609.35483v1)
  <details><summary>📄 Abstract</summary>
  Many learning tasks map an input distribution to an output distribution. A natural way to model such an operator is to transform each input sample using a continuous function that may depend on the entire input distribution, and then take the distribution of the transformed samples. This defines a measure-dependent pushforward model and includes measure-theoretic formulations of transformers. We ask when such models can approximate arbitrary continuous operators between spaces of probability mea...
  </details>

- **2026-09-28** — Chenyu Zhang, Yuhang Cao, Daru Du et al. — [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching](http://arxiv.org/abs/2609.35469v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive Vision-Language-Action (VLA) models offer a scalable path to robot learning, yet existing action tokenizers treat tokenization as a compression problem, producing representations that are semantically misaligned with the autoregressive backbone. We propose CATok, a causal action tokenizer that reframes tokenization as a causally structured generative process. CATok introduces a conditional annealing mechanism that extracts action tokens by progressively annealing a flow-matching p...
  </details>

- **2026-09-28** — Junchen Fu, Kleomenis Katevas, Vandana Rajan et al. — [Can Generative Retrievers Learn Semantic IDs Without Forgetting How to Speak?](http://arxiv.org/abs/2609.35430v1)
  <details><summary>📄 Abstract</summary>
  Generative retrieval (GR) enables end-to-end retrieval by generating document semantic identifiers (SIDs). However, retrieval-only fine-tuning can over-specialize pretrained language models to SID prediction, substantially distorting their natural-language distribution and limiting their suitability for interactive systems that must both retrieve documents and generate natural-language responses. We introduce SpeakGR, a dual-objective framework that learns SIDs while preserving language generati...
  </details>

- **2026-09-28** — Amir Moeini, Huaijiang Zhu, Daniel Havir et al. — [Inductive Feedback for Mixed-Policy Distillation](http://arxiv.org/abs/2609.35390v1)
  <details><summary>📄 Abstract</summary>
  Verbal feedback can identify errors and prescribe corrections, providing rich supervision for language-model post-training even when reliable programmatic verifiers are unavailable. Such feedback, often generated by a capable model, can be used to condition the teacher in on-policy distillation, which trains the student to match the teacher's predictions on student-generated rollouts. However, this approach can transfer teacher preferences that the feedback did not motivate, while leaving much o...
  </details>

- **2026-09-28** — Ruitao Liu, Qinghao Hu, Song Han — [d-OPD: Future-Aware On-Policy Distillation for Block Diffusion Language Models](http://arxiv.org/abs/2609.35362v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) typically generate text autoregressively (AR), predicting one token at a time. Block diffusion language models (dLLMs) instead generate blocks sequentially while denoising multiple tokens in parallel within each block, offering a promising way to accelerate generation. Rather than training such models from scratch, recent work adapts strong pretrained AR models into block dLLMs through distillation. On-policy distillation (OPD) has been widely used for LLM training b...
  </details>

- **2026-09-28** — Yiqun Zhang, Peidong Wang, Zihan Wang et al. — [Decide, Don't Generate: Competitive Dimensional ABSA with Jev's Typed Decisions](http://arxiv.org/abs/2609.35293v1)
  <details><summary>📄 Abstract</summary>
  Aspect-based sentiment analysis (ABSA) has largely turned to text generation. We show that competitive dimensional ABSA does not need it. Using Jev, a frozen model that answers typed questions with rubric scores, label probabilities, and yes/no judgments, we decompose all three tasks of SemEval-2026 Task III Track A into such decisions and align them with the annotation scheme through 488 coefficients fitted on CPU, with no text generation and no backbone tuning. On valence-arousal regression ov...
  </details>

- **2026-09-28** — Leyang Xue, Tianxin Wang, Xin Zhe Khooi et al. — [Weaver: A System for AI-RAN Compute Sharing with Foundation Model Training](http://arxiv.org/abs/2609.35276v1)
  <details><summary>📄 Abstract</summary>
  The emergence of AI-RAN infrastructure, which equips cell sites with GPU-accelerated hardware, creates an opportunity to colocate non-RAN workloads with primary RAN processing. We explore using this spare capacity for decentralized training of foundation models (FMs), one of the most compute-intensive AI workloads. We present the first characterization of spare GPU capacity in AI-RAN systems at both micro-scale--across transmission slots within a cell site--and macro-scale--across sites. Our ana...
  </details>

- **2026-09-28** — Genglin Wang, Kaiwei Liu, Liekang Zeng et al. — [EdgeCraft: Automated Model Crafting for Edge IoT](http://arxiv.org/abs/2609.35167v1)
  <details><summary>📄 Abstract</summary>
  Machine learning (ML) increasingly powers Internet of Things (IoT) applications at the edge. Yet producing a deployable edge ML artifact for a specific scenario requires navigating a huge search space spanning data representation, model design, training on domain-specific data, and runtime customization. This workflow is fragmented and difficult to scale across diverse edge applications.   We present EdgeCraft, an LLM-driven system that turns high-level intent into deployable edge ML artifacts. ...
  </details>

- **2026-09-28** — Guodong Ma, Baofeng Sun, Wenyu Yang et al. — [Coordinated Lane-Level Variable Speed Limits and Ramp Metering for Successive Weaving Segments Considering Merging/Diverging Risks: A Hybrid Model Predictive Control and Multi-Agent Reinforcement Learning Approach](http://arxiv.org/abs/2609.35152v1)
  <details><summary>📄 Abstract</summary>
  Successive weaving segments (SWSs) on urban expressways are bottlenecks prone to recurrent congestion and collisions, requiring fine-grained active traffic management (ATM). Existing approaches struggle to balance the adaptive performance of data-driven optimization with the resilience and transferability of model-based control. We propose a hybrid framework to coordinate lane-level variable speed limits (VSLs) and ramp metering across SWSs. First, we reconstruct L-METANET, a lane-level macrosco...
  </details>

- **2026-09-28** — Yaxiao Liu, Pengbo Liu, Yiwen Liu et al. — [From Migration to Calibration: Preserving Agent Capabilities across Models, Jurisdictions, and Scale](http://arxiv.org/abs/2609.35149v1)
  <details><summary>📄 Abstract</summary>
  Agents need calibration when deployment conditions change: replacing a driving model, including a foundation-to-post-trained transition; crossing jurisdictions; or scaling across heterogeneous markets and sources. Interface compatibility alone does not establish capability retention or target-contract satisfaction. We formulate agent calibration as constrained behavioral adaptation across three interacting layers: information preservation, harness adaptation, and user acceptance; the layers appl...
  </details>

- **2026-09-28** — Ran Yan, Youhe Jiang, Jiayi Nie et al. — [AReaL-TIK: Stateful Agentic Optimization of Unified RL Kernels through an Optimization IR](http://arxiv.org/abs/2609.35140v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training often uses distinct GPU kernels for rollout and policy update. In synchronous PPO and GRPO, numerical disagreement can perturb ratios between current token probabilities and those assigned during rollout. Recomputing rollout log-probabilities with the policy-update backend avoids this discrepancy but adds a forward pass. Bitwise-consistent unified kernels permit reuse when the policy snapshot and probability processing match the objective. Their optimiza...
  </details>

- **2026-09-28** — Yu-Kai Wang, Chun-Xin Tan, Manh-Hung Nguyen et al. — [Style-Driven Data Synthesis and Degradation-Aware Enhancement for Ultrasound Image Restoration](http://arxiv.org/abs/2609.35120v1)
  <details><summary>📄 Abstract</summary>
  Low-cost handheld ultrasound devices can be widely deployed compared to professional hospital ultrasound machines. However, their images suffer from compound degradation that can mislead clinical judgment. Motivated by this observation, mapping handheld low-quality (LQ) to hospital high-quality (HQ) images has been considered a valuable research question. Conventionally, the mapping requires pixel-aligned LQ-HQ pairs. This requirement is unsatisfactory in practical scenarios because real scans a...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 647 |
| prompt-injection | 581 |
| memory-poisoning | 52 |
| tool-use-attack | 145 |
| backdoor | 484 |
| adversarial-attack | 609 |
| privacy-leakage | 4227 |
| steganography | 72 |
| misuse | 1091 |
| red-teaming | 129 |
| vulnerability | 3342 |
| defense | 3158 |
| alignment | 2934 |
| robustness | 3152 |
| watermark | 502 |
| unlearning | 105 |
| agent-safety | 59 |
| benchmark | 66 |
| survey | 372 |
| other | 8524 |

---

📚 **全部 30251 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-09-30 18:09:39*