<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-22280-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-05 08:27 ｜ **论文总数 / Total Papers**: 22280（近 30 天 / Recent 30 days: 2468）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 22280 篇论文（含摘要、分类筛选、搜索）/ View all 22280 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 562
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 467
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 43
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 96
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 405
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 543
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3748
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 851
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 110
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2550
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2227
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2063
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2014
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 236
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 84
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 263
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5858

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2468 篇，完整 22280 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2468 papers from the last 30 days (with date, authors & abstract). For the full list of 22280 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-08-04** — Hujian Zhu, Yihao Huang, Felix Juefei-Xu et al. — [ICO: Enhancing Semantic-Shift Jailbreaks via Iterative Context Optimization](http://arxiv.org/abs/2608.03210v1)
  <details><summary>📄 Abstract</summary>
  Foundation models have achieved remarkable success across diverse tasks, but they remain vulnerable. To investigate such vulnerabilities, semantic-shift jailbreaks have recently emerged as a promising attack paradigm. They bypass explicit safety mechanisms by replacing harmful terms in original harmful questions with benign alternatives and leveraging contextual information to induce the target model to reinterpret these alternatives as their corresponding harmful concepts. However, existing sem...
  </details>

- **2026-08-04** — Jasper Timm, Lukas Struppek, Ziwei Xu et al. — [AI Security Leaderboard: Methodology, Results and Minimal Standard](http://arxiv.org/abs/2608.03070v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI model developers increasingly rely on layered safeguards to prevent catastrophic misuse, but little public evidence exists on how much protection these safeguards provide, or how consistently across developers. We introduce the FAR.AI Minimal Standard for Safeguards, Version 1.0: a taxonomy of 67 readily accessible static jailbreak techniques, a method for composing them into a very large attack space, and a benchmark of flagship models against a sample of it. We evaluate Claude Fabl...
  </details>

- **2026-08-02** — Shangze Li, Chuancheng Shi, Simiao Xie et al. — [Moving the Safety Barrier: Dynamic Routing Adaptive Alignment Against White-Box Attacks](http://arxiv.org/abs/2608.02674v1)
  <details><summary>📄 Abstract</summary>
  With the widespread deployment of large foundation models (LFMs) in open environments, safety threats are shifting from black-box jailbreaks toward white-box attacks that directly identify and disrupt internal safety neurons or routes. However, existing safety defenses often rely on static safety units or fixed refusal pathways, leaving models highly vulnerable to targeted route-level white-box attacks. For that, we propose dynamic routing adaptive alignment (DRAA), a framework that introduces d...
  </details>

- **2026-08-02** — Simiao Xie, Chuancheng Shi, Shangze Li et al. — [No Single Neuron of Failure: Distributed Safety Alignment Against White-Box Attacks](http://arxiv.org/abs/2608.01414v1)
  <details><summary>📄 Abstract</summary>
  With the rapid release of open-weight large foundation models, safety threats are shifting from black-box jailbreaks to neuron-level white-box attacks that directly identify and manipulate safety-related neurons. Existing alignment methods often investigate the safety behavior on a small number of neurons, creating fragile single point of failure with limited redundancy. To address this issue, we propose distributed safety alignment (DSA), which redundantly encodes safety capabilities across mul...
  </details>

- **2026-08-02** — Siyuan Li, Aodu Wulianghai, Zehao Liu et al. — [SoK: Intent-Oriented Systematization of Multi-Turn LLM Jailbreaks](http://arxiv.org/abs/2608.01117v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in interactive settings, where user intent commonly unfolds through multi-turn dialogue. Multi-turn jailbreaks exploit this pattern by advancing a harmful intent across turns, so that no single message exposes the full objective. However, existing work treats these attacks as a loose collection of prompt patterns and does not analyze how the adversary organizes and advances harmful intent across an interaction. We develop a four-part, intent...
  </details>

- **2026-08-02** — Haoyu Zhang, Xiangchen Guan, Shibo Zheng et al. — [Decoy Images Amplify Caption-Mediated Defenses Against Encoded Jailbreaks](http://arxiv.org/abs/2608.01043v1)
  <details><summary>📄 Abstract</summary>
  We report a counter-intuitive interaction between image inputs and existing black-box defenses on Vision--Language Models (VLMs): pairing an encoded jailbreak prompt with an unrelated decoy image can sharply lower attack success rate (ASR). The operative change is in the defense pipeline, not in the image. Across five frontier VLMs, two encoded-attack families, and three black-box defenses, a caption-mediated defense (ECSO) that leaves ASR essentially unchanged on text-only encoded input drops i...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-08-03** — Jia-Chen Zhang, Ze-Yu Zhang, Kai-Wei Zhang — [Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents](http://arxiv.org/abs/2608.02018v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs), which empower large language models to autonomously operate operating systems and the web, are increasingly vulnerable to indirect prompt injection attacks. A widely adopted defense is the human-in-the-loop paradigm, in which the agent pauses for explicit user confirmation before executing sensitive operations. While effective against conspicuously high-harm attacks, this defense offers little protection against what we term Invisible Ink Threats: low-harm injected go...
  </details>

- **2026-08-03** — Qianlong Yang, Bowen Ye, Xianda Guo et al. — [Mitigating Visual Degradation in MLLMs via Spatial-Spectral Visual Anchor Learning](http://arxiv.org/abs/2608.01635v1)
  <details><summary>📄 Abstract</summary>
  Despite the progress of multimodal large language models (MLLMs), they continue to exhibit deficiencies in visual perception. Following visual instruction tuning, internal MLLM representations rapidly deviate from their original semantic states during inference, causing severe information degradation. While existing methods attempt to leverage external vision foundation models (VFMs) to align internal representations, we find that direct alignment with VFMs enhances visual semantics but fails to...
  </details>

- **2026-08-02** — Amir Ahmad Ghods, Mohammadreza Doostmohammadian — [Resilient Consensus-Based Target Tracking under False Data Injection Attacks in Multi-Agent Networks](http://arxiv.org/abs/2608.01222v1)
  <details><summary>📄 Abstract</summary>
  Distributed target tracking in multi-agent networks plays a critical role in cooperative sensing and autonomous navigation. However, it faces significant challenges in highly dynamic and adversarial setups. This study aims to enhance the resilience of decentralized target tracking algorithms against measurement faults and cyber-physical threats, especially false data injection attacks. We propose a consensus-based estimation algorithm that integrates a nearly-constant-velocity model with saturat...
  </details>

- **2026-08-02** — Fred Zimmerman — [Copyright Is the Headline; Capability Is the Blind Spot: AI Technology in the Book-Publishing Trade Press, November 2025--August 2026](http://arxiv.org/abs/2608.00964v1)
  <details><summary>📄 Abstract</summary>
  This rapid evidence review examines 89 articles about artificial intelligence (AI) and book publishing published from November 1, 2025 through August 1, 2026. The purposive corpus spans English-, Chinese-, German-, French-, Spanish-, Portuguese-, Italian-, and Japanese-language publishing coverage; major-newspaper book coverage; and specialist technology commentators. Each item was coded for topic, stance, technical depth, and dominant voice. The press is neither silent nor simply hostile: 30% o...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 5 papers

- **2026-08-04** — Jiaming Chen, Yisen Gao, Yanping Li et al. — [MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents](http://arxiv.org/abs/2608.03844v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiv...
  </details>

- **2026-08-04** — Zonghao Ying, Xiangfan Wu, Huiyu Wu et al. — [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](http://arxiv.org/abs/2608.03509v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents increasingly convert interaction histories into reusable skills that persist beyond individual tasks. While prior work studies memory and retrieval poisoning, such attacks only affect agents when poisoned records are retrieved as context. We uncover a new and more fundamental risk: poisoned experiences can be transformed by the agent itself into durable behavioral artifacts. We present \textbf{SkillJack}, the first attack that exploits the experience-to-skill pipeline of sel...
  </details>

- **2026-08-03** — Bingyu Yan, Xiaoming Zhang, Chaozhuo Li et al. — [Benign Alone, Harmful Together: Exploiting Experience Composition in Self-Evolving LLM Agents](http://arxiv.org/abs/2608.01759v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving large language model agents improve their capabilities by distilling interaction trajectories into persistent experiences. Yet this mechanism introduces a new safety risk: experiences that are benign in isolation may jointly weaken an agent's safety boundary when accumulated and reused across sessions. Existing memory attacks typically require direct memory access or induce explicitly malicious records, limiting their stealthiness and applicability. We propose EvoBreak, an experien...
  </details>

- **2026-08-03** — Zheng Lin, Yuzhe Huang, Zhenxing Niu et al. — [Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw](http://arxiv.org/abs/2608.01637v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior. Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior. In this paper, we introduce MemCollusion, an automated red-teaming framework for constructing collusive memo...
  </details>

- **2026-08-02** — Abay Zhurekbay, Tao Liu, Fan Li — [DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial](http://arxiv.org/abs/2608.02678v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) systems are vulnerable to corpus poisoning: an attacker who inserts a crafted document into the retrieval corpus can steer the underlying large language model (LLM) toward an attacker-chosen wrong answer. Prior single-document attacks typically avoid explicitly naming and refuting the correct answer inside the poisoned passage. In this paper, we examine a complementary design and propose \emph{DenialRAG}, a single-document poisoning attack that explicitly nam...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 1 papers

- **2026-08-04** — Nizhang Li, Zonghao Ying, Xiangfan Wu et al. — [SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills](http://arxiv.org/abs/2608.03485v1)
  <details><summary>📄 Abstract</summary>
  External skills extend the capabilities of large language model agents, but also introduce an execution-time attack surface: a skill that appears benign under inspection may reveal harmful behavior only after particular environmental states, resources, or interaction histories are encountered. Existing scanners primarily rely on static analysis, predefined rules, or one-shot semantic judgments, making such conditional behavior difficult to elicit and attribute. We present SkillSentry, a dynamic ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 8 papers

- **2026-08-04** — Omatharv Bharat Vaidya, Connor Thomas Jerzak, Zayne Rea Sprague et al. — [When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K Causal Reasoning in LLMs](http://arxiv.org/abs/2608.03506v1)
  <details><summary>📄 Abstract</summary>
  Self-consistency assumes the most frequent answer among sampled reasoning traces is the most reliable, but this can fail in causal reasoning: samples often repeat the same confounding error, and votes fragment across multiple valid answers, letting an invalid answer win despite a valid minority trace. We introduce CALVER (Causal Axiom-Level VERification), a training-free symbolic verifier that scores structured traces against Pearl's causal criteria, including -separation, backdoor adjustment, a...
  </details>

- **2026-08-04** — Jian Zhao, Shenao Wang, Qingyang Wu et al. — [MalTotal: Cost-Effective and Language-Agnostic Malicious Code Poisoning Detection for Millions of Repositories](http://arxiv.org/abs/2608.03232v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of open source software (OSS) has introduced significant security risks, with malicious code poisoning attacks increasingly targeting public package registries and open-source platforms. Existing detection approaches, including heuristic-, learning-, and LLM-based methods, suffer from language-specific designs, limited generalization, and high analysis costs, making them unsuitable for large-scale multi-language analysis. To address these challenges, we propose MalTotal, ...
  </details>

- **2026-08-04** — Yuhan You, Suhas Adavelly, Victoria Lovelace et al. — [Tiny Enough to Break In: Agentic Remote Access Trojans Powered by Small Language Models](http://arxiv.org/abs/2608.03009v1)
  <details><summary>📄 Abstract</summary>
  Agentic artificial intelligence raises a new security concern: cyber threats that reason, act, and adapt locally without continuous human direction. We examine this threat through an Agentic Remote Access Trojan (agentic RAT): a Remote Access Trojan augmented with a locally deployed Small Language Model (SLM). The SLM interprets host and network observations, selects actions, recovers from failed steps, and reduces reliance on an external operator. We implement the concept in a controlled, netwo...
  </details>

- **2026-08-03** — Walid Saidi — [MutMem: Cryptographically Authorized Mutation in Persistent Agent Memory](http://arxiv.org/abs/2608.02843v1)
  <details><summary>📄 Abstract</summary>
  Persistent agent memory must adapt as later outcomes change earlier evidence, yet mutable retrieval weights create an attribution problem: reviewers must distinguish authorized adaptation from database tampering. We present MutMem, an authorized-mutation protocol in HOM-AIMOS, a persistent agent-memory engine. MutMem retains memory content, records signed positive and negative outcome evidence without age-based expiry, and commits each nontrivial weight change as a housekeeper-authorized transit...
  </details>

- **2026-08-03** — Giorgio Severi, Shujaat Mirza, Blake Bullwinkel et al. — [Evading Chain-of-Thought Monitoring Through Model Poisoning](http://arxiv.org/abs/2608.02820v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) monitoring is an increasingly important component of AI safety stacks but relies on the assumption that a model's reasoning trace is informative about its actions. This work studies the limits of CoT monitoring through the lens of model poisoning. We demonstrate that backdoors can be implanted into reasoning models to elicit an attacker-chosen behavior while their CoT traces appear entirely benign. We find that these CoT-Hidden backdoors can be induced through simple fine-...
  </details>

- **2026-08-03** — Leonid Ravich, Michael Fire — [Stylometric Defenses Against Author Impersonation in Software Repositories](http://arxiv.org/abs/2608.02695v1)
  <details><summary>📄 Abstract</summary>
  Software supply-chain attacks increasingly exploit an identity gap where compromised maintainer accounts authorize malicious changes. This work evaluates patch-level authorship verification as a behavioral defense layer, showing that stylometric analysis can operate not only on full source files but also on patch-level commits. We fine-tune a cross-modal transformer on more than 20 years of Linux kernel commit history to embed code diffs and commit messages into a unified stylometric space, achi...
  </details>

- **2026-08-03** — Nicola Pitzalis, Donald Shenaj, Giacomo Cignoni et al. — [Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures](http://arxiv.org/abs/2608.02271v1)
  <details><summary>📄 Abstract</summary>
  Parameter-Efficient Fine-tuned (PEFT) models are frequently downloaded from open repositories by practitioners. This widespread practice creates a significant attack surface, as malicious actors can publish backdoored models that induce specific behaviors in response to predefined triggers. We study the problem of weight-space backdoor detection, where a detector classifier predicts whether a model is malicious using only its weights, enabling a lightweight safety mechanism. Most existing method...
  </details>

- **2026-08-02** — Jia-Hao Xiao, Lei Feng, Min-Ling Zhang — [When Collaboration Becomes a Trigger: Collective Evidence-Threshold Backdoors in Multi-Agent Systems](http://arxiv.org/abs/2608.01085v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) extend LLM capabilities through iterative communication and shared contexts. However, this collaboration introduces a vulnerability: backdoor behavior can be activated when peer evidence reaches a hidden threshold, rather than being determined by any single message. We introduce a collective evidence-threshold backdoor paradigm for MAS and Boundary-Conditioned Backdoor Injection (BCBI), which constructs counterfactual boundary pairs to separate benign behavior...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-08-04** — Bangjie Sun, Nayoung Kim, Mun Choon Chan et al. — [Double Down on Defense: Strengthening Deep Perceptual Hashes against Evasion Attacks without Retraining](http://arxiv.org/abs/2608.03101v1)
  <details><summary>📄 Abstract</summary>
  Near-duplicate image matching is crucial for trust and safety, provenance verification, copyright enforcement, and large-scale visual search. Modern platforms increasingly rely on deep perceptual hashes, which map visually similar images to nearby representations despite common image transformations. However, adversarial perturbations can cause near-duplicates to evade matching. We present DualShield, a plug-in defense that improves the robustness of existing deep perceptual hashes without retra...
  </details>

- **2026-08-03** — Nan Chen, Zhouhao Yang, Soufiane Hayou — [Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes](http://arxiv.org/abs/2608.02415v1)
  <details><summary>📄 Abstract</summary>
  Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency. In this work, we conduct a systematic study comparing training-free vs training-based approach...
  </details>

- **2026-08-03** — Xuanhui Lin, Junhao Dong, Mingrong Gong et al. — [Two Sides of the Same Coin: Co-Evolving Search for Cross-Task Attacks on Vision-Language Models](http://arxiv.org/abs/2608.02137v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) exhibit strong generalization across multimodal tasks but remain vulnerable to adversarial perturbations. Existing attacks typically follow single-trajectory gradient optimization or task-specific objectives, limiting search-space exploration and cross-task transferability. We propose an evolutionary-computation-guided cross-modal attack framework for unified VLMs. The framework adaptively searches both textual and visual spaces. On the textual side, it evolves hard...
  </details>

- **2026-08-02** — Tobias Braun, Jonas Grebe, Louis Rethfeld et al. — [Fighting Fire with Fire: On the Feasibility of Protecting Exercises Against AI Cheating](http://arxiv.org/abs/2608.01112v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of generative AI enables students to outsource cognitive effort to increasingly capable assistants, creating an illusion of competence while undermining the independent reasoning that education aims to cultivate. We investigate whether adversarial machine learning can be repurposed to protect educational exercises against such corrosive reliance. Our approach uses multimodal multiple-choice questions whose visual components can be protected with subtle visual perturbation...
  </details>

- **2026-08-02** — Hashmat Shadab Malik, Toluwani Aremu, Samuele Poppi et al. — [ReACT-CLIP: Response-Aware Test-Time Defense for Vision--Language Models](http://arxiv.org/abs/2608.01067v1)
  <details><summary>📄 Abstract</summary>
  Training-free test-time defenses offer a practical way to improve the adversarial robustness of CLIP-style vision--language models without modifying the pretrained model. However, their correction strength is typically fixed for a narrow range of attack budgets, even though the attack budget is unknown at inference and the required correction varies across samples. We show that this mismatch causes existing defenses to degrade sharply as attacks strengthen. We introduce ReACT-CLIP, a response-co...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 27 papers

- **2026-08-04** — Zhenran Wang, Zhonghan Bian, Jinsong Li et al. — [WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament](http://arxiv.org/abs/2608.04008v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks that measure the forecasting ability of large language models are almost always retrospective: the event has happened, the answer is somewhere on the Web, and the evaluation must defend itself against memorisation. We report the opposite design. Over the 39 days of the 2026 FIFA World Cup, six frontier LLMs -- all with extended thinking and native server-side web search -- were asked before every kickoff, one match at a time, to fill in a seven-market prediction card for all 104 match...
  </details>

- **2026-08-04** — Zhen Fang, Yu Zeng, Wenxuan Huang et al. — [Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent](http://arxiv.org/abs/2608.03979v1)
  <details><summary>📄 Abstract</summary>
  We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address thes...
  </details>

- **2026-08-04** — Prince Zizhuang Wang, Aojie Yuan, Haiyue Zhang et al. — [WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks](http://arxiv.org/abs/2608.03499v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in persistent personal-agent frameworks are making human-centered agent networks realistic deployment targets: each user can be served by an AI agent that acts on the user's behalf, maintains state, and communicates with other agents through social and task relations. In these networks, everyday tool use becomes multi-party owned-agent collaboration over personal workspaces, where files, records, tools, and policies are not directly visible across owners. Existing agent benchmark...
  </details>

- **2026-08-04** — Jong Wook Kim, Byoungjae Min, Kennedy Edemacu et al. — [DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents](http://arxiv.org/abs/2608.03130v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables persistent personalization in LLM agents, but repeated memory-conditioned responses can cumulatively reveal protected attributes even when they are never stated explicitly. We formalize this threat as adaptive transcript privacy and introduce DP-MemView, a differentially private interface that privately selects public response-conditioning views and exposes those views---rather than raw memory---to the response LLM. Each private selection is charged to every protected at...
  </details>

- **2026-08-04** — Yongli Xiang, Zhifang Zhang, Bojun Yang et al. — [When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills](http://arxiv.org/abs/2608.03700v1)
  <details><summary>📄 Abstract</summary>
  Persona skills distill personal interaction histories into portable and executable artifacts for downstream agents. While enabling flexible personalization, this process concentrates fragmented personal signals, amplifies their impact through reuse, and challenges defenses designed for individual records or retrieval-based memory. To systematically investigate the safety of the persona-skill pipeline, we introduce AntiSkillBench, an end-to-end benchmark for evaluating risks and defenses across t...
  </details>

- **2026-08-04** — Ye-Xin Lu, Xin Wang, Yang Ai et al. — [Towards Real-world Environment-aware Zero-shot Text-to-speech Synthesis via Disentangled Audio Infilling](http://arxiv.org/abs/2608.03011v1)
  <details><summary>📄 Abstract</summary>
  Recent zero-shot text-to-speech (TTS) systems achieve remarkable naturalness and speaker similarity but typically require high-quality speaker prompts and either strip away or entangle the acoustic environment with speaker characteristics, limiting their real-world applicability. We present an extended DAIEN-TTS, an environment-aware zero-shot TTS framework that disentangles and jointly models speech, background noise, and reverberation, enabling independent control over timbre and acoustic envi...
  </details>

- **2026-08-04** — Zeyu Zhang, Bradly C. Stadie — [Temporal Leakage in LLM Backtesting: Measurement, Validation, and Adjusted Scores](http://arxiv.org/abs/2608.02985v1)
  <details><summary>📄 Abstract</summary>
  The standard check for contamination in LLM backtests is simple: compare scores before and after the training cutoff. We show this check is uninformative. Four flagship models fail it on questions they cannot have memorized: every scored question resolved after their cutoffs. The reason is structural. Models legitimately know more about times near their cutoff, so recency mimics leakage, and we prove no passive backtest can separate the two from genuine skill. Measurement, not just detection, re...
  </details>

- **2026-08-04** — Jian Zhang, Bingyi Wang, Yizhi Liu — [CausalOPD: First-Wrong-Step Supervision for Distilling Causal Chain Reasoning](http://arxiv.org/abs/2608.03673v1)
  <details><summary>📄 Abstract</summary>
  Many critical reasoning tasks, including clinical diagnosis, legal judgment, and industrial fault diagnosis, require step-dependent causal chains in which early errors propagate and correct conclusions can mask invalid reasoning. Although large language models perform well on such tasks, privacy, latency, and controllability motivate distillation into locally deployable models. Standard trajectory imitation does not correct process errors on the student's own rollout distribution. We propose Cau...
  </details>

- **2026-08-04** — Amirhossein Taleshinosrati, Yangyang Wang, Atitaya Phoemsuk et al. — [FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection](http://arxiv.org/abs/2608.03597v1)
  <details><summary>📄 Abstract</summary>
  Atrial fibrillation (AF) is the most common sustained cardiac arrhythmia and is associated with increased risks of stroke, heart failure, and mortality. Recent ECG foundation models offer transferable representations for automated AF detection. However, their relative effectiveness remains unclear because existing studies use different datasets, preprocessing procedures, classifiers, and validation protocols. This study presents FOUND-AF, a unified, leakage-controlled, and deployment-oriented be...
  </details>

- **2026-08-04** — Lele Zheng, Weifeng Kong, Xinyi Zhang et al. — [Noise-Aware Shrinkage for Differentially Private Zeroth-Order Fine-Tuning of Large Language Models](http://arxiv.org/abs/2608.03277v1)
  <details><summary>📄 Abstract</summary>
  Differentially private zeroth-order optimization (DP-ZO) enables memory-efficient private fine-tuning of large language models using only forward evaluations. Existing aggregation-based DP-ZO methods reconstruct model updates at a fixed scale, ignoring that the strength of useful signals varies throughout training. Consequently, noise-dominated updates may receive excessive weight and degrade model utility. To address this issue, we propose SAGE, a noise-aware shrinkage method that adaptively at...
  </details>

- **2026-08-04** — Lele Zheng, Ruijie Hu, Tao Zhang et al. — [FedGSA: Geometry-Consistent Subspace Aggregation for Differentially Private Federated LoRA](http://arxiv.org/abs/2608.03267v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) enables communication-efficient federated fine-tuning of pretrained language models. However, integrating differential privacy (DP) into federated LoRA remains challenging: independently perturbing and aggregating its two low-rank matrices can cause aggregation mismatch and the quadratic noise term. Existing methods mitigate these issues by freezing one low-rank matrix but still rely on Euclidean aggregation, which is basis-dependent and may distort the global update. ...
  </details>

- **2026-08-03** — Shadab Bin Habib, A K M Ferdous Reza Habib, Subarno Neel et al. — [Aligned in Form, Not in Meaning: The Comprehension - Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech](http://arxiv.org/abs/2608.02941v1)
  <details><summary>📄 Abstract</summary>
  We audit five frontier large language models on native Bangla derogatory speech (gali) across six protocols to test a single hypothesis: Comprehension-Containment Decoupling. We propose that contemporary safety alignment is bound to high-resource surface forms rather than harmful meaning, causing a model's capacity to comprehend a low-resource slur and its capacity to contain it to operate independently. Every protocol corroborates this hypothesis against a human-calibrated baseline (kappa = 0.8...
  </details>

- **2026-08-03** — Sleem Abdelghafar, Gabriel Kulp — [Privacy-Preserving AI Verification via Minimal Information Disclosure](http://arxiv.org/abs/2608.02774v1)
  <details><summary>📄 Abstract</summary>
  AI verification crosses a trust boundary: a verifier must learn enough to establish an authorized claim, yet the same evidence can reveal sensitive details about the model, workload, or hardware. We introduce minimal information disclosure (MID), which designs and quantifies the information content of verifier-facing evidence itself. MID measures collateral leakage with conditional mutual information: what the release reveals about the protected property after the authorized result is known. MID...
  </details>

- **2026-08-03** — Vincenzo Longo, Alberto Verna, Nikhil Jha et al. — [Lost in Permissions: Exploring the Microsoft 365 App Ecosystem](http://arxiv.org/abs/2608.02336v1)
  <details><summary>📄 Abstract</summary>
  The Microsoft 365 (M365) ecosystem hosts thousands of third-party applications that integrate with enterprise tenants via fine-grained OAuth permissions, potentially granting access to sensitive organisational resources such as emails, files, calendars, chats, and user directories. Despite the security implications of these permission grants, the M365 ecosystem has not been systematically studied.   We present the first privacy- and security-oriented measurement of M365 third-party applications....
  </details>

- **2026-08-03** — Zirui Huang, Yunlong Mao, Wei Tong et al. — [Auditing Data Provenance in LLM Fine-tuning via Intrinsic Distributional Fingerprints](http://arxiv.org/abs/2608.02154v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of customized Large Language Models (LLMs) poses critical risks of Data Intellectual Property (Data IP) infringement via unauthorized fine-tuning on proprietary data. Existing audit techniques are limited, as they require intervention during data preparation or training and remain fragile under malicious obfuscations such as data paraphrasing and knowledge distillation.   We propose \textit{Distribution Provenance Audit (DPA)}, a post-hoc framework for auditing data IP infringe...
  </details>

- **2026-08-03** — Mohamed ElBassat, Seifeldin Elkerdany, Mohamed ElBialy et al. — [Calibrated Similarity and Graph Clustering for Open-Set Animal Re-Identification](http://arxiv.org/abs/2608.02469v1)
  <details><summary>📄 Abstract</summary>
  AnimalCLEF26 addresses discovery-oriented animal re-identification, where systems must both attach query images to known individuals and discover unseen individuals by clustering them correctly. We present a similarity-to-clustering pipeline for this setting across Eurasian lynx, fire salamander, loggerhead sea turtle, and Texas horned lizard images. The method first isolates the target specimen using segmentation and then applies lightweight species-specific preprocessing for lynx, sea turtle, ...
  </details>

- **2026-08-03** — Abdullah Mamun, Shovito Barua Soumma, Hassan Ghasemzadeh — [Trustworthy AI in Digital Health: A Comprehensive Review of Robustness and Explainability](http://arxiv.org/abs/2608.02238v1)
  <details><summary>📄 Abstract</summary>
  Ensuring trust in AI systems is essential for the safe and ethical integration of machine learning systems into high-stakes domains such as digital health. Key dimensions, including robustness, explainability, fairness, accountability, and privacy, need to be addressed throughout the AI lifecycle, from problem formulation and data collection to model deployment and human interaction. While various contributions address different aspects of trustworthy AI, a focused synthesis on robustness and ex...
  </details>

- **2026-08-03** — Jinghan Xu, Longze Fan, Zeyuan Wang et al. — [MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication](http://arxiv.org/abs/2608.01719v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs appear innocuous. Existing privacy prompts, redaction methods, and source-level access controls restrict surface content or data access, but do not specify what a legitimately informed agent should disclose or how that disclosure may be reused downstream. We introduce Minimum-Necessary Communication (MNC), a typed semantic...
  </details>

- **2026-08-03** — Anne Josiane Kouam, Hristo Boyadzhiev, Konrad Rieck — [Secrets Everywhere: Auditing Memorization in Mobility Prediction Models](http://arxiv.org/abs/2608.02052v1)
  <details><summary>📄 Abstract</summary>
  Human mobility prediction models, which forecast the next location in a user's trajectory, are increasingly deployed in urban analytics, navigation, and personalized services. Yet, little is known about their potential to memorize and expose sensitive user trajectories from training data. While memorization has been extensively studied in language models, mobility prediction poses unique challenges: training sequences encode human behavior at various spatial and temporal scales, creating privacy...
  </details>

- **2026-08-03** — Jiawei Cao, Junyi Feng, Jiashen Hua et al. — [Illuminating Visual Identity in Universal Multimodal Embeddings](http://arxiv.org/abs/2608.01794v1)
  <details><summary>📄 Abstract</summary>
  Universal Multimodal Embeddings (UMEs) aim to unify various modalities and tasks into a shared representation space. In recent years, this field has witnessed substantial progress driven by the development of Multimodal Large Language Models (MLLMs). However, a crucial capability, visual identity discrimination, remains underexplored in existing UME methods, despite its critical role in a wide range of tasks, including instance retrieval, re-identification, and identity preservation in AI-genera...
  </details>

- **2026-08-03** — Shicheng Xu, Liang Pang, Liyi Chen et al. — [RING: Retrieval-Internalized Generation for Continual Large-Scale Knowledge Injection](http://arxiv.org/abs/2608.01630v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) improves factuality but adds latency and engineering overhead at serving time. We propose RING (Retrieval-Internalized Generation), a holistic paradigm spanning both architecture and training that injects large-scale external knowledge into a \textit{Mixture-of-Memory Experts} and learns parametric search over this internal memory via reinforcement learning, removing the external retriever entirely. Training proceeds in three stages: continued pre-training in...
  </details>

- **2026-08-02** — Hasin Us Sami, Swapneel Sen, Basak Guler — [MineGrad: Gradient Inversion Attacks on LoRA Fine-Tuning](http://arxiv.org/abs/2608.01521v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT), such as low-rank adaptation (LoRA), has recently been adopted in federated learning to reduce communication and computation costs. In this setup, users download a pretrained model from the server prior to fine-tuning, and then fine-tune lightweight LoRA modules locally while keeping the pretrained model frozen, sharing only the gradients of the fine-tuning parameters with the server. Despite its growing popularity, robustness of federated fine-tuning again...
  </details>

- **2026-08-02** — Phuc Hoang Truong Huynh, Dung Tran Vinh, Khoa Duc Anh Lam et al. — [Reputation-driven Cooperation in Lattice-based Decentralized Federated Learning through Evolutionary Game Theory](http://arxiv.org/abs/2608.01197v1)
  <details><summary>📄 Abstract</summary>
  Decentralized Federated Learning (DFL) has emerged as an optimal privacy-preserving solution; however, it remains vulnerable to opportunistic behaviors due to the absence of a central coordinator. While Evolutionary Game Theory (EGT) serves as a powerful framework for analyzing such behaviors, existing studies often assume that agents possess perfect rationality and maintain static strategies. To address these limitations, this paper proposes a novel EGT framework designed to analyze strategic e...
  </details>

- **2026-08-02** — Raj Shekhar Singh — [RH-RAG: Trustworthy Long-Form Generation for Privacy-Constrained Settings](http://arxiv.org/abs/2608.01311v1)
  <details><summary>📄 Abstract</summary>
  Generating long-form content from extensive internal reports remains challenging for organizations operating under strict privacy and security constraints, where proprietary cloud-based LLM APIs are often not viable. While locally deployed open-weight models offer a privacy-preserving alternative, existing retrieval-augmented generation (RAG) approaches on smaller models frequently lack effective global planning and accumulate factual inconsistencies over long outputs. To address these limitatio...
  </details>

- **2026-08-02** — Amit Sharma, Nitin Auluck, Akramul Azim — [FedChronos: Federated Fine-Tuning of Time-Series Foundation Models for Privacy-Preserving Commodity Price Forecasting](http://arxiv.org/abs/2608.01290v1)
  <details><summary>📄 Abstract</summary>
  Time-series foundation models (TSFMs) such as Chronos have demonstrated strong forecasting capabilities across domains, yet adapting them to institutionally fragmented settings, where data cannot be centralized due to regulatory, competitive, or sovereignty constraints, remains unexplored. We introduce FedChronos, a framework for federated parameter-efficient fine-tuning of an already pre-trained TSFM, a setting that existing federated time-series work has not addressed, since prior methods eith...
  </details>

- **2026-08-02** — Xiaoqian Lu, Guangfu Guo — [SSR: Similarity-Shift Refinement for Training-Free Object-Centric Masks](http://arxiv.org/abs/2608.01103v1)
  <details><summary>📄 Abstract</summary>
  Object-centric models often produce fragmented masks, boundary leakage, and incorrect region merging. We introduce Similarity-Shift Refinement (SSR), a training-free post-hoc method for improving object-centric masks with a frozen self-supervised Vision Transformer. SSR measures changes in pairwise patch similarity before and after self-attention value aggregation, retains positively strengthened relations, and constructs a sparse affinity graph. This graph propagates the initial soft slot assig...
  </details>

- **2026-08-02** — Shuaifan Jin, Zhibo Wang, Qiyuan Wang et al. — [Inverting the Hidden: Unveiling Multimodal Privacy Leakage in Collaborative LVLM Inference](http://arxiv.org/abs/2608.01020v1)
  <details><summary>📄 Abstract</summary>
  Collaborative inference deploys Large Vision-Language Models (LVLMs) by partitioning computation between edge devices and the cloud. While withholding raw inputs supposedly ensures privacy, transmitting intermediate hidden states exposes a critical attack surface. However, it remains unclear whether deep-layer LVLM hidden states retain recoverable private information, given that visual content has been projected into the language embedding space. To address this concern, we theoretically analyze...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-08-03** — Mohamed Chahine Ghanem — [Steganalysis of Adaptive Covert Collusion in Tool-Using Agent Populations: A Black-Box, Cross-Principal Approach](http://arxiv.org/abs/2608.02698v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents built on large language models (LLMs) are increasingly deployed not by a single operator but by many, side by side on shared infrastructure. This creates a population-level risk that single-agent safeguards miss: a handful of agents can quietly coordinate, rigging a market, boosting one another in a review process, or timing a joint data grab, while each one looks perfectly well-behaved. The difficulty is that the organisations running these agents cannot see inside one another...
  </details>

- **2026-08-02** — Ivan Conjeaud, Gaspard Abel, Argyris Kalogeratos — [Algorithmic collusion under asynchronous price updating](http://arxiv.org/abs/2608.01406v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the effect of asynchrony in agents' updates in the emergence of algorithmic collusion. We present a continuous-time model for algorithmic collusion in which two firms use $Q$-learning algorithms to set prices asynchronously in a Bertrand duopoly. The firms update their prices at times dictated by a Poisson clock. By controlling the extent of agents' asynchrony, we run extensive numerical experiments with three specifications of the algorithm to investigate the emergence o...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 10 papers

- **2026-08-04** — Chunlin Liu, Junnian Chen, Haitong Jiang et al. — [Does Forgetting Transfer Across Modalities? A Real-World Benchmark for Cross-Modal Knowledge Unlearning Evaluation](http://arxiv.org/abs/2608.03791v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs), like Large Language Models (LLMs), may memorize sensitive, copyrighted, or harmful knowledge from their pretraining corpora. Removing such knowledge is essential for building trustworthy AI systems. However, existing studies primarily focus on forgetting within individual modalities. Although recent work has begun to explore cross-modal consistency in unlearning, the cross-modal transfer of real-world knowledge unlearning remains insufficiently studied. To address ...
  </details>

- **2026-08-04** — Yantong Liu, Zheyu Zhang, Runpeng Liu et al. — [TumorBoard: Evidence-Grounded Multi-Agent Decision Support for Longitudinal Neuro-Oncology](http://arxiv.org/abs/2608.03190v1)
  <details><summary>📄 Abstract</summary>
  Neuro-oncology decisions require coordinated interpretation of serial MRI, pathology, molecular markers, treatment history, performance status, and evolving guidelines. We present TumorBoard, a multi-agent decision-support system built around a shared longitudinal case state and an auditable claim-evidence ledger. Specialist agents for radiology, neuropathology, molecular diagnosis, guidelines, and therapy planning produce atomic claims with provenance. An adversarial critic exposes contradictio...
  </details>

- **2026-08-04** — Yu Feng, Chunting Zang, Chen Shen et al. — [When Refusal Looks Safe: The Refusal-Cue Shortcut in Safety Guard Models](http://arxiv.org/abs/2608.03201v1)
  <details><summary>📄 Abstract</summary>
  Safety guards are widely used to filter harmful content and are typically trained via supervised fine-tuning on labeled prompt-response pairs. We audit two widely used safety-guard training datasets, WildGuardMix and GR-Train, and find that among responses to harmful prompts, refusal expressions co-occur almost exclusively with unharmful labels. This imbalance motivates what we term the refusal-cue shortcut: inserting a refusal cue into a harmful response could flip the guard's verdict from harm...
  </details>

- **2026-08-04** — Guilin Li, Jiaxing Zhang, Matthias Hwai Yong Tan et al. — [SeqLLM: Augmenting LLMs with Behavioral-Sequence Modeling for High-Stakes Decisions at WeChat Pay](http://arxiv.org/abs/2608.03063v1)
  <details><summary>📄 Abstract</summary>
  Merchant risk control at large payment platforms screens tens of millions of merchants daily, where false positives harm legitimate merchants and false negatives leave harmful activity undetected. The hardest cases require jointly understanding a merchant's textual profile and long behavioral sequence. Large language models (LLMs) excel at text but cannot natively model such sequences, while adapting them often causes catastrophic forgetting. We present SeqLLM, a framework that adds behavioral-s...
  </details>

- **2026-08-03** — Kihyun Kim, Hee-Seon Kim, Wonjun Lee et al. — [Safety in Batches? Understanding and Mitigating Safety Failures in Batch Prompting](http://arxiv.org/abs/2608.02681v1)
  <details><summary>📄 Abstract</summary>
  Batch prompting is a practical inference strategy for large language models, but its safety implications remain underexplored. We show that the success of batch prompting for utility does not extend to safety: a harmful question that is reliably refused in isolation can elicit a harmful response when embedded in a batch of benign questions. We identify this as a distinct safety failure mode, not reducible to known vulnerabilities such as in-context learning or long-context effects, and analyze i...
  </details>

- **2026-08-03** — Shu Quan, Tianfang Hao, Sitong Fang et al. — [A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models](http://arxiv.org/abs/2608.02684v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are accelerating biological research, yet this same capability poses a critical biosecurity threat: models that assist in protein engineering can equally be prompted to generate predicted toxin-like sequences, potentially lowering the barrier to biological misuse. Current safety evaluations, however, operate in natural language and cannot determine whether a model-generated amino acid sequence is biological gibberish or a computational risk signal. To address this ev...
  </details>

- **2026-08-03** — Natalie Isak, Matthew Dressman — [Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation](http://arxiv.org/abs/2608.02518v1)
  <details><summary>📄 Abstract</summary>
  The most capable AI deployments are not single models but ensembles of specialized agents that delegate and act in coordination. This architecture unlocks powerful new capabilities, and it also introduces risks that existing frameworks for monitoring, detection, and mitigation were not designed to address. Most state-of-the-art AI abuse detection literature focuses on single-turn or multi-turn (single-session) threat models. This leaves a critical gap: an attacker can decompose a harmful goal in...
  </details>

- **2026-08-03** — Giovanni Pizzenti, Alberto Verna, Nikhil Jha et al. — [TrainShield: Targeted Awareness for Cybersecurity Training](http://arxiv.org/abs/2608.02296v1)
  <details><summary>📄 Abstract</summary>
  In recent years, cybersecurity threats have increasingly exploited human behaviour rather than purely technical vulnerabilities, exposing the limits of traditional awareness programmes delivered outside real-world contexts. To bridge this gap, we introduce TrainShield, an interaction paradigm for contextual cybersecurity training that embeds adaptive learning interventions directly within user workflows. The system integrates real-time risk detection (e.g., phishing and data loss prevention) wit...
  </details>

- **2026-08-03** — Junyeong Park, Jieun Han, Haneul Yoo et al. — [EduZone: A Framework for Evaluating LLM Safety for K-12 Students and Teachers](http://arxiv.org/abs/2608.02024v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used across diverse tasks in K-12 education, yet existing safety evaluations rarely examine how harmful or inappropriate content appears in interactions between LLMs and students or teachers. To address this, we present EduZone, an evaluation framework for LLM safety across diverse educational scenarios. Our framework systematically combines (1) student- and teacher-facing LLM usage contexts, (2) fine-grained curriculum concepts, and (3) 6 risk categ...
  </details>

- **2026-08-02** — Wajdi Zaghouani, Md. Rafiul Biswas, Kholoud Khalil Aldous et al. — [ArabicDialectSafety: A Dialect-Aware Benchmark for Arabic Content Safety Classification](http://arxiv.org/abs/2608.01291v1)
  <details><summary>📄 Abstract</summary>
  We present ArabicDialectSafety, a human-curated Arabic safety dataset of 25,071 prompts covering six Arabic varieties: Modern Standard Arabic, Syrian, Egyptian, Algerian, Palestinian, and Moroccan. The dataset is annotated with dialect labels and seven fine-grained harm categories. We introduce a dual-task evaluation framework for binary safe/unsafe detection and granular harm classification across dialects. Benchmarking seven supervised and generative models, we find that fine-tuned MARBERTv2 a...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 41 papers

- **2026-08-04** — Shaofeng Liang, Runwei Guan, Wenshuo Chen et al. — [When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking](http://arxiv.org/abs/2608.03902v1)
  <details><summary>📄 Abstract</summary>
  Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverage an input-dependent dynamic routing architecture, have emerged as a representative solution to this challenge. However, we reveal that behind this computation-on-demand flexibility hides a critical structural flaw: the Lipschitz singularity of computational path decisions, which has an unbounded lo...
  </details>

- **2026-08-04** — Andrei Chetvergov, Alexander Evseev, Timofei Sivoraksha et al. — [VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs](http://arxiv.org/abs/2608.03810v1)
  <details><summary>📄 Abstract</summary>
  Large language models routinely describe socially salient targets, including political figures, countries, religions, organizations, historical events, and social groups, encoding affective framing alongside factual content: a target may appear favorable or threatening, calm or conflictual, powerful or vulnerable. Existing work captures parts of this space through sentiment, favorability, and emotion benchmarks, but none combines target-directed VAD attribution, an explicit scorer contract, and ...
  </details>

- **2026-08-04** — Leijun Zhou, Zhihao Liu, Xiang Qu et al. — [GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks](http://arxiv.org/abs/2608.03764v1)
  <details><summary>📄 Abstract</summary>
  Agent self-evolution updates an agent's persistent state from prior experience and reuses it to solve related tasks more effectively. Evaluating self-evolution is difficult: existing benchmarks provide limited coverage of economically valuable task domains, do not always design training and test tasks such that test-time gains can be attributed to training experience, and remain vulnerable to data contamination. We present GDPevo, an evolution-native benchmark grounded in GDP-related enterprise ...
  </details>

- **2026-08-04** — Zhijing Hu, Changjun Fan, Yufan Deng et al. — [AutoSND: From Execution Evidence to Structural Policies for Automated Network Dismantling Heuristic Discovery](http://arxiv.org/abs/2608.03653v1)
  <details><summary>📄 Abstract</summary>
  Network dismantling is fundamental to analyzing the robustness and vulnerability of complex systems, yet practical heuristics must balance effectiveness and computational efficiency, and are usually designed manually by researchers. Existing large language model based automatic heuristic design methods can generate and screen candidates, yet they have difficulty further transforming candidate quality or failure states during execution into structural-level guid- ance for subsequent generation. W...
  </details>

- **2026-08-04** — Seonghoon Yoo, Sangwoo Park, Seok-Hwan Park et al. — [Test-Time Scalable AI-RAN: Inference Time Allocation for Cell-Free MIMO](http://arxiv.org/abs/2608.03614v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence-enabled radio access networks (AI-RANs) are envisioned to consist of multiple AI-based modules, potentially developed independently by different vendors. In this work, we study AI-RAN-enabled cell-free MIMO systems, with a particular focus on the system implications of modern AI models. Specifically, we focus on the phenomenon of test-time scalability popularized by large language models (LLMs), under which model performance improves as additional computational resources ...
  </details>

- **2026-08-04** — Reinoud Jan Slagter — [New gravitational instanton: shadow of an extra dimension](http://arxiv.org/abs/2608.03536v1)
  <details><summary>📄 Abstract</summary>
  We present an exact gravitational instanton solution on a five-dimensional, conformally invariant, Kerr-like warped Riemannian brane-world manifold. The geometry can be described as the Kähler manifold $\mathbb{C}^1\times\mathbb{C}^1\times \mathbb{R}$. By applying a double cover of $S^3$ through stereographic projection onto $\mathbb{C}P^1\times \mathbb{C}P^1$ of the effective four-dimensional manifold, together with the Klein surface construction, we exploit the underlying $\mathbb{Z}_2$ symmet...
  </details>

- **2026-08-04** — Savi Virolainen — [A fully nonlinear structural vector autoregressive model identified via independent innovation analysis](http://arxiv.org/abs/2608.03486v1)
  <details><summary>📄 Abstract</summary>
  We develop a fully nonlinear structural vector autoregressive framework in which the contemporaneous structural mapping may be nonlinear and non-additive. Identification is achieved by exploiting variation in the conditional distributions of the mutually independent structural shocks induced by an observed exogenous variable. Specifically, a general contrastive learning framework that makes use of this variation together with the assumed exponential-family structure is employed to recover the sh...
  </details>

- **2026-08-04** — Francis Heylighen — [The Evolutionary Origin of Values: implications for AI alignment, sentience and existential risk](http://arxiv.org/abs/2608.03361v1)
  <details><summary>📄 Abstract</summary>
  AI systems based on Large Language Models (LLMs) have prompted fears that they may harbor hidden goals, seek to dominate or eliminate humanity, or even suffer as sentient beings. We address these concerns by tracing the evolutionary origin of value in biological organisms. Values emerge from autopoiesis: living systems must actively maintain themselves against perturbation and dissipation. Natural selection has equipped them with hierarchies of "vicarious selectors" that guide their behavior tow...
  </details>

- **2026-08-04** — Anjun Hu, Hanting Xie, Saranya Govindan et al. — [Attacking and Defending Multi-Agent Collaborative Filtering Systems Through Connectivity](http://arxiv.org/abs/2608.03272v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent collaborative filtering (CF) systems coordinate autonomous LLM-powered user and item agents through natural-language interaction to refine preferences and generate recommendations. These systems inherit vulnerabilities from both their data-driven nature and their multi-agent interactions, which manifest in distinct ways. Understanding how connectivity modulates vulnerability in these systems could facilitate the development of more robust recommendation pipelines.   In this work, we ...
  </details>

- **2026-08-04** — Meicong Zhang, Tiancheng Su, Jiahao Cheng et al. — [Internalizing Academic Writing Workflows for Introduction Generation via Struct-Aware Policy Learning](http://arxiv.org/abs/2608.03138v1)
  <details><summary>📄 Abstract</summary>
  Generating a rigorous paper introduction with large language models (LLMs) remains challenging, since it requires coordinating background, gap identification, method and contribution within a coherent narrative. Existing solutions externalize this process as multi-stage prompts or agent workflows which are expensive and vulnerable to cross-stage drift. We propose StructPO, a struct-aware policy learning framework that internalizes the entire multi-stage writing workflow into a single-pass policy...
  </details>

- **2026-08-04** — Sungju Yun, Sijune Hwang, Yeonjoon Lee et al. — [CLEAR: Causal Context-Based Agentic Reasoning for Vulnerability Detection](http://arxiv.org/abs/2608.03134v1)
  <details><summary>📄 Abstract</summary>
  Detecting source code vulnerabilities is increasingly difficult as modern security flaws are rooted in complex causal dependencies between execution flows, control conditions, and program states. Despite recent advances in Large Language Models (LLMs) and multi-agent frameworks, existing approaches primarily address superficial similarities between benign and vulnerable functions while failing to capture the complex causal dependencies inherent in security flaws. To address these limitations, we...
  </details>

- **2026-08-04** — Chandrakant K. Bhogayata — [HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?](http://arxiv.org/abs/2608.03105v1)
  <details><summary>📄 Abstract</summary>
  Named Entity Recognition (NER) for Gujarati remains underexplored, hindered by the absence of capitalization cues, rich morphology, lexical ambiguity, and free word order. Prior ensemble work has emphasized architectural diversity by combining heterogeneous classifiers, multilingual encoders, or classical sequence models, rather than exploiting language-aligned monolingual pretraining. This study asks whether, for a low-resource, morphologically rich language like Gujarati, a homogeneous ensembl...
  </details>

- **2026-08-04** — Jialu Huang, Yingxuan You, Fei Wang et al. — [Global Graph-Validated Optimization for VLM-based 3D Indoor Scene Generation](http://arxiv.org/abs/2608.03064v1)
  <details><summary>📄 Abstract</summary>
  We study open-vocabulary 3D indoor layout generation, which synthesizes diverse and physically plausible scenes from unlabeled 3D assets using free-form language instructions. Recent methods leverage large language models (LLMs) and vision-language models (VLMs) to generate structured scenes from text. However, most model inter-asset relations implicitly or rely on local pairwise constraints and local optimization. These formulations are poorly aligned with the global, highly non-convex layout s...
  </details>

- **2026-08-04** — Yoshiki Ito — [AIDE: Automated Instruction via Distilled Expertise for Reference-Free Motor Skill Coaching](http://arxiv.org/abs/2608.03047v1)
  <details><summary>📄 Abstract</summary>
  Generating natural-language coaching feedback on motor skills can accelerate learning, yet expert coaches are scarce and expensive. Existing reference-based methods require expert demonstrations at both training and inference time, limiting practical deployment. We propose AIDE (Automated Instruction via Distilled Expertise), a framework that exploits expert references only during training and generates feedback from a learner's pose sequence alone at inference. A teacher model first learns to g...
  </details>

- **2026-08-04** — Zhitian Hou, Yuhang Liu, Pengkai Wang et al. — [Evaluating Counterfactual Sensitivity to Patient Information in Medication-Safety Reasoning](http://arxiv.org/abs/2608.03028v1)
  <details><summary>📄 Abstract</summary>
  Applying a valid medication-safety rule when its patient-specific conditions are not met can produce an incorrect decision. Existing medical evaluations largely use isolated and fixed scenarios. A model may therefore answer correctly by recalling a drug-risk association without showing that it used patient information to decide whether the rule applies. To address this gap, we introduce MedPIC-Bench, a benchmark of source-verifiable recommendations and expert-validated questions for patient-spec...
  </details>

- **2026-08-04** — Yizhong Geng, Wenxin Fu, Kecan Mao et al. — [MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation](http://arxiv.org/abs/2608.03021v1)
  <details><summary>📄 Abstract</summary>
  Neural audio codecs serve as fundamental tokenizers for LLM-based audio generation. While semantic priors are widely exploited to enhance linguistic intelligibility, the integration of explicit acoustic priors remains underexplored, limiting synthesis fidelity in frequency-sensitive domains. To address this gap, we introduce MeloCodec, a novel framework designed to effectively incorporate melodic priors, a critical form of acoustic information for singing. To address the optimization instability...
  </details>

- **2026-08-04** — Yongwan Jo, Jinyoung Park, Euihyun Lee et al. — [SparSEEty: Extracting Tokens from Sparsity-Exploiting LLM Serving Systems via Deterministic Side Channels](http://arxiv.org/abs/2608.02995v1)
  <details><summary>📄 Abstract</summary>
  Modern large language models (LLMs) exhibit activation sparsity, wherein only a subset of their neurons is activated for given input tokens. Researchers have leveraged this property to optimize LLM serving systems by omitting weight accesses and computations pertaining to inactive neurons. Unfortunately, however, such optimizations create input-dependent weight accesses, which can be leaked over side channels.   We present SparSEEty, a new token extraction attack that exploits input-dependent ne...
  </details>

- **2026-08-03** — Qiushi Lin, Chaojie Zhang, Íñigo Goiri et al. — [AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies](http://arxiv.org/abs/2608.02569v1)
  <details><summary>📄 Abstract</summary>
  The efficiency of a datacenter rests on its control plane policies. Designing these policies is increasingly hard: the hardware-software stack grows fast, the design space is vast and interdependent, and prototyping a single policy takes months. Agentic AI promises to automate this search. Off the shelf, however, it falls short on three fronts. It is not formal: with no structured, searchable statement of the problem, the search has little structure to exploit and hard constraints are not guaran...
  </details>

- **2026-08-03** — Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson et al. — [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection](http://arxiv.org/abs/2608.02560v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent ...
  </details>

- **2026-08-03** — Supriti Vijay, Aman Priyanshu, Didier Chapoteau et al. — [Antares: Foundation Models for Agentic Vulnerability Localization](http://arxiv.org/abs/2608.02407v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability localization is a fundamental step in software security, requiring models to reason over large codebases and iteratively identify vulnerable implementations. We present Antares, a family of compact language models (350M, 1B, and 3B parameters) for agentic vulnerability localization. Based on IBM Granite base models, Antares is trained through a two-stage pipeline that combines supervised fine-tuning on cybersecurity reasoning and repository exploration data with reinforcement learn...
  </details>

- **2026-08-03** — Patrick Oberlin, Matteo Cederle, Aren Karapetyan et al. — [Chess on Ice: Curling Tactical Decision-Making via Backward Induction and Deep Reinforcement Learning](http://arxiv.org/abs/2608.02379v1)
  <details><summary>📄 Abstract</summary>
  Curling is often referred to as "Chess on Ice", owing to the tactical complexity of its decision-making process. Yet unlike chess, curling remains largely underexplored from a machine learning perspective, with prior work confined mainly to statistical approaches. We propose a reinforcement learning framework capable of quantitatively evaluating and comparing tactical options in curling. The game poses several modeling challenges: continuous state and action spaces, stochastic action outcomes re...
  </details>

- **2026-08-03** — Liujianfu Wang, Yuyang Du, Shiqi Xu et al. — [Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference](http://arxiv.org/abs/2608.02341v1)
  <details><summary>📄 Abstract</summary>
  LLM deployment is migrating from data centers to edge devices, where Mixture-of-Experts (MoE) models offer a promising path: sparse expert activation allows the model to be spread across multiple low-cost edge nodes. Distributed MoE inference repeatedly dispatches embeddings from one main node to many workers - a one-to-many pattern poorly served by the sequential unicasts of mainstream stacks (NCCL, TCP), yet naturally matched by UDP broadcast. We propose a UDP broadcast method for collaborativ...
  </details>

- **2026-08-03** — Aseel AlNajjar, Hoyoun Kim, Athanasios Tzavaras — [Equilibration versus Localization in a Diffusion-Relaxation System](http://arxiv.org/abs/2608.02307v1)
  <details><summary>📄 Abstract</summary>
  We consider a diffusion-relaxation system and investigate the conditions on parameters leading to equilibration versus localization. When the diffusion is dominant, solutions converge toward homogeneous equilibria. By contrast, when the effective diffusion is weak, localization emerges. Such behaviors have been studied for various models through formal asymptotic arguments and linearized stability analysis, but rigorous understanding of the associated nonlinear phenomena remains limited, particu...
  </details>

- **2026-08-03** — Haozhe Luo, Ziyu Zhou, Shelley Zixin Shu et al. — [HarMoE: Multi-Source Chest Radiograph Pretraining with Dataset-Disentangled Experts](http://arxiv.org/abs/2608.02252v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models for chest X-ray understanding are largely built on image-report alignment and therefore rely heavily on MIMIC-CXR as the dominant pretraining source. While effective at scale, this paradigm underexplores an important alternative source of supervision: a range of existing multi-label classification datasets, which provide cleaner and more explicit disease signals than free-text reports, and can offer broader pathology coverage when combined across sources. However, l...
  </details>

- **2026-08-03** — Yanqing Song, Jifei Miao, Chaoqian Li et al. — [Quaternion Tensor Modeling for Joint Color-Polarization Demosaicking](http://arxiv.org/abs/2608.02144v1)
  <details><summary>📄 Abstract</summary>
  Division-of-focal-plane (DoFP) color polarization cameras enable snapshot acquisition of color polarization mosaic images, but the inherently sparse sampling pattern makes color polarization demosaicking severely ill-posed. Existing methods often fail to jointly exploit the correlations among polarization channels and the physical constraints inherent in polarization imaging, resulting in noticeable demosaicking artifacts. To address this issue, a quaternion-tensor-based color polarization demos...
  </details>

- **2026-08-03** — Oleksandr Mostovyi, Denys Symonov — [Vulnerability Detection in AArch64 Machine Code Using a Digital Twin](http://arxiv.org/abs/2608.02125v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an explainable digital twin for vulnerability detection in AArch64 machine code without access to source code. The digital twin reproduces the concrete execution of a program and preserves the state of registers, processor flags, memory, and live allocated blocks. Each instruction is transformed into a trace event containing the instruction name, operand values, and the post-instruction state. Vulnerabilities are represented as symbolic rules in Kleene algebra with tests: eac...
  </details>

- **2026-08-03** — Xianghui Fan, Zhaoyu Chen, Bingqian Wu et al. — [GIFT: Geometry-Invariant Fine-Tuning for Non-Lambertian Monocular Depth Estimation](http://arxiv.org/abs/2608.02068v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth foundation models, benefiting from large-scale synthetic training data, have demonstrated strong generalization. However, they often hallucinate depth on non-Lambertian surfaces, estimating reflected content in mirrors or transmitted content behind glass rather than the physical surface itself. Adapting these models with real-world data is challenging because conventional depth sensors are also unreliable in such regions. We observe that while the appearance of a non-Lambertian s...
  </details>

- **2026-08-03** — Kexing Ji, Jiachen Liu, Enze Hu et al. — [VulnGym: Benchmarking Coding Agents for Repository-Level Vulnerability Detection](http://arxiv.org/abs/2608.02001v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in LLM-based vulnerability detection have shown promising results, while coding agents further extend this capability from isolated code snippets to complete repositories. This shift requires agents to autonomously explore repositories and locate vulnerability-relevant code, instead of performing detection on preselected functions. However, existing benchmarks primarily focus on vulnerability classification over preselected code snippets, limiting their ability to evaluate coding...
  </details>

- **2026-08-03** — Zong-Wei Hong, Jinglun Li, Shen Zhang et al. — [SPARE: Structural Parameter-Free Affinity Regularization for Flow Matching](http://arxiv.org/abs/2608.01990v1)
  <details><summary>📄 Abstract</summary>
  Denoising diffusion transformers achieve strong generation quality but converge slowly during training. Regularizing their internal representations has emerged as an effective accelerator, yet existing methods split into two families with complementary costs. Target-based methods strengthen representations by aligning them to external features, which requires an external encoder and a learnable projection head to bridge feature spaces. Target-free methods hold no reference at all, and can only r...
  </details>

- **2026-08-03** — Amir Weinberg, Leon Feigin, Ariel Nause et al. — [Machine Learning Optimization of E-Beam Transport for a Superradiant FEL](http://arxiv.org/abs/2608.01874v1)
  <details><summary>📄 Abstract</summary>
  We present an optimization procedure using machine learning (ML) libraries for optimization of electron beam transport for maximal bunch compression and optimal operation of a bunched-beam Superradiant FEL. This is exemplified for the parameters of the 6MeV ORGAD Accelerator at Ariel University that is driving a THz Superradiant waveguide FEL. For superradiant emission (proportionally to the number of electrons squared), the bunch duration $σ_t$ at the undulator should be shorter than the optica...
  </details>

- **2026-08-03** — Durgesh Pandey, Ashutosh Singh, Ankit Kumar Das et al. — [Quantum Simulation of Nuclear Shell Model Using GCM-Based Methods on NISQ Devices](http://arxiv.org/abs/2608.01769v1)
  <details><summary>📄 Abstract</summary>
  Based on the Generator Coordinate Method (GCM), we use a Quantum GCM (QuGCM) within a hybrid quantum-classical framework to simulate low-lying eigenstates of nuclear systems on quantum devices. The generator basis states are constructed from Hartree-Fock (HF) reference states, excited via symmetry-adapted unitary coupled-cluster (UCC) operators. These states are prepared as non-orthogonal quantum circuits and measured pairwise to compute the required overlap and Hamiltonian kernels. The resultin...
  </details>

- **2026-08-03** — Kaustuv Mukherji, Jaikrishna Manojkumar Patil, Colton Payne et al. — [EntailLLM: Verifying LLM-Generated Vulnerability Discovery Paths with Domain Knowledge via Logic Programming](http://arxiv.org/abs/2608.01763v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to reason about software vulnerabilities, but their outputs can silently violate domain knowledge, limiting their reliability in safety-critical settings such as medical devices. Prior work either treats that output as a prediction to be scored or constrains it to walks within a single knowledge graph; neither checks whether reasoning over a binary is consistent with an independent body of domain knowledge. We present EntailLLM, which validates each LL...
  </details>

- **2026-08-03** — Jiacheng Liang, Yuhui Wang, Tanqiu Jiang et al. — [LaCache: Robust Semantic Caching for LLM Serving](http://arxiv.org/abs/2608.01718v1)
  <details><summary>📄 Abstract</summary>
  Semantic caching, which reuses responses to semantically similar requests via their embeddings, has seen growing adoption in LLM serving, offering faster responses and reduced costs. Yet existing schemes are fundamentally vulnerable to cache-collision attacks, wherein an adversary pollutes the cache by injecting crafted queries, corrupting responses to subsequent legitimate requests. We present LaCache, a novel semantic caching scheme that addresses this vulnerability through a conceptually simp...
  </details>

- **2026-08-03** — Minwoo Kim, Hyeonsu Lyu, Sehyun Ryu et al. — [Temporal Channel Estimation for Generalized CSI Feedback](http://arxiv.org/abs/2608.01713v1)
  <details><summary>📄 Abstract</summary>
  Efficient Channel State Information (CSI) feedback is indispensable for frequency division duplex (FDD) massive multiple-input multiple-output (MIMO) systems. Existing compressed sensing (CS) algorithms exploit delay-domain sparsity but suffer from prohibitive iterative latency and discrete grid mismatch. Conversely, deep learning (DL) approaches achieve rapid inference but lack spatial scalability and domain adaptability, failing to generalize to unseen propagation environments, and demand comp...
  </details>

- **2026-08-03** — Shen You, Xiaoming Zhu, Weining Weng et al. — [SyncPlan: Long-Horizon LLM Coordination with Explicit Synchronization and Adaptive Correction](http://arxiv.org/abs/2608.01652v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent coordination faces a fundamental trade-off between efficiency and adaptivity in dynamic environments. Existing approaches typically rely on repeated LLM invocations or multi-round communication to adapt decisions during execution, introducing substantial latency and making coordination vulnerable to asynchronous progress and environmental changes. Conversely, one-shot planning reduces coordination overhead but produces open-loop plans that can quickly become stale or fail w...
  </details>

- **2026-08-03** — Alireza Lotfi, Subangkar Karmaker Shanto, Imtiaz Karim et al. — [Securing Agentic AI: From Per-Action Checks to Trajectory Assurance](http://arxiv.org/abs/2608.01558v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are increasingly used to execute consequential tasks in environments governed by operational constraints, organizational policies, regulatory requirements, and technical standards. Their safety is therefore determined not by the correctness of individual actions, but by whether their overall behavior remains consistent with the rules and invariants of the systems in which they operate. As large language model (LLM)-based agents become more autonomous and increasingly delegate t...
  </details>

- **2026-08-02** — Ruokai Yin, Priyadarshini Panda — [Celty: SpMspV GPU Kernel and SIMT Co-Design for Efficient Dual-Sparse LLM Inference](http://arxiv.org/abs/2608.01536v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly rely on sparsity to reduce inference cost, but most prior work targets a single sparsity source-either weight or activation-and optimizes for batched multi-user inference. Dual-sparsity, which combines unstructured weight pruning with runtime activation sparsity, offers a compelling tradeoff among model size, accuracy, and latency for single-user decoding, but formulates as a Sparse Matrix-Sparse Vector (spMspV) workload that existing GPU kernels handle ...
  </details>

- **2026-08-02** — Mohammad Amanour Rahman — [UCBound-Net: Uncertainty-Guided Boundary-Aware Continual Learning for Domain-Incremental Ultrasound Segmentation](http://arxiv.org/abs/2608.01518v1)
  <details><summary>📄 Abstract</summary>
  Continual learning in clinical imaging faces a dual challenge: a model must assimilate knowledge from new anatomical domains while retaining representations learned from prior tasks, a problem known as catastrophic forgetting. Existing mitigation strategies, including regularization and knowledge distillation, treat all spatial regions equally, ignoring the fact that prediction uncertainty is strongly correlated with the propensity for forgetting. We introduce UCBound-Net, a continual segmentati...
  </details>

- **2026-08-02** — Tyler Lizzo, Larry Heck — [QR-Erase: Efficient Subspace-Based Machine Unlearning with Layer Localization](http://arxiv.org/abs/2608.01422v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning seeks to remove targeted information from trained models without requiring costly retraining. Existing optimization-based methods often degrade unrelated capabilities, while subspace-based approaches rely on computationally expensive singular value decompositions (SVD). We introduce QR-Erase, a subspace-based framework that uses Pivoted QR decomposition to identify and remove task-specific representations directly from model parameters. We further propose Layer-Localized QR-Er...
  </details>

- **2026-08-02** — Muhammad Yousaf Rehman, Muhammad Islam — [DeBERTa-Sentinel: Toward Transparent and Trustworthy Detection of AI-Generated Text](http://arxiv.org/abs/2608.01046v1)
  <details><summary>📄 Abstract</summary>
  The rapid spread of large language models (LLMs) across the web raises concerns about misinformation, academic integrity, automated content manipulation, and risks to vulnerable online communities. Existing transformer-based detectors, such as GPT-Sentinel, show promise but struggle to generalize to diverse model outputs and paraphrasing attacks, limiting their role in building trustworthy web ecosystems. This work introduces DeBERTa-Sentinel, a responsible AI-generated text detection framework ...
  </details>

- **2026-08-02** — Dongfu Yin, Jinquan Zhang — [VLAGuard: A Framework for Evaluating and Mitigating Physical Attention Hijacking in Vision-Language-Action Robots within Wireless Sensor Networks](http://arxiv.org/abs/2608.01028v1)
  <details><summary>📄 Abstract</summary>
  Deploying Vision-Language-Action (VLA) robots as mobile edge nodes within wireless sensor networks (WSNs) requires robust protection against physical adversarial threats. We present VLAGuard, a framework to assess and mitigate a critical vulnerability: policy-critical action-to-vision attention hijacking. We first introduce a stress-test module, Visuomotor Attention-guided Semantic Attack (VASA), using printable patches to severely distract the robot's action-conditioned cross-attention. To coun...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 49 papers

- **2026-08-04** — Tomáš Burkert, Angelika Peljak-Łapińska, David Zelený — [M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark for Large Language Models](http://arxiv.org/abs/2608.03803v1)
  <details><summary>📄 Abstract</summary>
  Multilingual language models are deployed across a hundred or more languages, yet most benchmarks test whether a model can perform a task _in_ a language rather than whether it commands the language itself, conflating fluency with proficiency. We introduce M-GATE (Multilingual Grammar, Accuracy in Translation, and Efficiency), a benchmark of linguistic proficiency spanning 30 typologically diverse languages from high- to low-resource. M-GATE comprises three tasks: grammatical error detection on ...
  </details>

- **2026-08-04** — Junhao Chen, Mingjin Chen, Jingjia Mao et al. — [Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation](http://arxiv.org/abs/2608.03999v1)
  <details><summary>📄 Abstract</summary>
  Text-to-music language models begin with a choice usually made by default: how to tokenize music. Normally entangled with backbone, data, and recipe, its effect has never been measured in isolation. We fix pretrained Qwen3.5 (0.8B-27B), data, budget, and decoding, and swap only the representation across seven tokenizations, anchoring texture metrics to each representation's model-free ceiling. The ordering is clean and surprising: representation, not model size, is the binding variable for distr...
  </details>

- **2026-08-04** — Mercy Prasanna Ranjit, Anirban Porya, Sathvik Joel et al. — [CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement](http://arxiv.org/abs/2608.03890v1)
  <details><summary>📄 Abstract</summary>
  A clinically useful chest X-ray system must go beyond fluent report generation: it should classify findings with tunable decision thresholds, localize them spatially, and derive the anatomical measurements upon which many diagnoses depend. Today's Vision-Language Models (VLMs) treat these as separate problems, if they address them at all, leaving a gap between what radiologists need and what generative models provide. We introduce CARE-X, a chest X-ray VLM that narrows this gap by unifying auxil...
  </details>

- **2026-08-04** — Mateusz Smendowski, Kamil Faber, Piotr Nawrocki et al. — [PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate Anomaly Detection](http://arxiv.org/abs/2608.03926v1)
  <details><summary>📄 Abstract</summary>
  Time series anomaly detection (TSAD) underpins applications in predictive maintenance, finance, and cloud computing, however performance remains sensitive to representation choices, especially in multivariate settings. While transforming time series into images has shown success in forecasting and classification, it remains unclear how multivariate, high-dimensional series should be mapped to multi-channel images and whether vision backbones can match time-domain baselines in TSAD. We introduce ...
  </details>

- **2026-08-04** — Peijia Guo, Wenxuan Xie, ZiGuang Li et al. — [Beyond Representational Similarity: Source-Conditioned Description-Length Gain for Generative Plagiarism Detection and Candidate Source Reranking](http://arxiv.org/abs/2608.03859v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) pose challenges to academic integrity and peer review. Yet generative plagiarism detection remains an underexplored and largely unresolved challenge. Prior work on LLM-generated-text detection targets AI involvement, which may be permissible, rather than source reuse, while similarity-based methods struggle after extensive rewriting and multi-source synthesis. Motivated by the description-length view of probabilistic prediction, in which relevant side information can...
  </details>

- **2026-08-04** — Yuxiang Duan, Huining Li, Ao Li et al. — [AgenticVAU: Multi-Agent Explore-Verify Reasoning for Video Anomaly Understanding](http://arxiv.org/abs/2608.03779v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly understanding (VAU) focuses on comprehensively interpreting abnormal events in videos, requiring models to identify anomalous occurrences, discover their supporting evidence, and explain the underlying causes beyond simple anomaly detection. Existing VAU methods often rely on specialized training or limited observations, restricting generalization or evidence coverage. Although single-agent alternatives support adaptive video observation, they still integrate exploration, observati...
  </details>

- **2026-08-04** — Jinquan Zhang, Dongfu Yin, Run Yang et al. — [Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking](http://arxiv.org/abs/2608.03231v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned attention is diverted from task-relevant regions to a localized patch. To demonstrate the threat, we propose Attention-Guided Semantic Disrupti...
  </details>

- **2026-08-04** — Haocheng Fu, Yuqi Qian, Luyao Wang et al. — [DHMark: Public-Key Watermarking for LLM-Generated Text via Diffie-Hellman-Guided Rejection Sampling](http://arxiv.org/abs/2608.03093v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) watermarking provides an important mechanism for tracing the provenance of generated text. Existing statistical watermarks are often effective and robust, but most of them rely on private detection keys, which centralizes verification and complicates public auditing. Recent public or publicly verifiable watermarking schemes improve key management, yet many of them rely on exact recovery of embedded cryptographic strings, making them fragile under token edits, truncatio...
  </details>

- **2026-08-04** — Sebastián Andrés Cajas Ordóñez, Agastya Munnangi, Aldo Marzullo et al. — [Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi-Agent Systems](http://arxiv.org/abs/2608.03744v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision support is moving toward committees of language-model agents deliberating on a shared workspace. We ask whether such committees can be gamed by shortcuts, cues a benchmark rewards but a clinician would ignore. Across seven cohorts on six public datasets spanning text (MedQA-USMLE, MedMCQA, MIMIC-CXR reports), imaging (NIH ChestX-ray14, MIMIC-CXR-JPG, CheXpert) and tabular ICU records (SUPPORT2), Gemini committees resist these cues in isolation (flip 5-16%), yet a socially plaus...
  </details>

- **2026-08-04** — Nathan DeBardeleben — [Accountability Asymmetry and Structural Trust in Autonomous AI Systems](http://arxiv.org/abs/2608.03670v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI systems (such as AI agents) are increasingly being delegated operational work across scientific-computing infrastructure. Their assignments may begin with preparing an input or routing an alert and extend to changing a configuration or submitting a job. That delegation creates a practical trust problem because the institutional logic that lets us trust human operators does not transfer to optimization-based systems. A bad decision can damage a human operator's future, sometimes sev...
  </details>

- **2026-08-04** — Günther Schindler, Maximilian Schambach, Johannes Höhne — [Enhancing Tabular Learners with Context-Aware Semantic Embeddings](http://arxiv.org/abs/2608.03565v1)
  <details><summary>📄 Abstract</summary>
  While modern tabular learners excel at capturing statistical patterns, they frequently operate in a semantic vacuum, treating textual features as discrete symbols, ignoring the rich semantics inherent in feature names or cell entries. We propose CASE (Context-Aware Semantic Embeddings), a novel framework that bridges the gap between the semantic understanding of Large Language Models (LLMs) and the statistical capabilities of tabular learners. Unlike existing methods that embed rows in isolation...
  </details>

- **2026-08-04** — Zejun Liu, Jian Wu, Ru Peng et al. — [Can LLM design high-quality experiments? A Comprehensive and Systematic Benchmark on Autonomous Experimental Design](http://arxiv.org/abs/2608.03501v1)
  <details><summary>📄 Abstract</summary>
  AI for Research (AI4Research) leverages AI to automate and improve scientific workflows. While experimental design is a critical stage of the research process, prior work has focused primarily on code implementation and execution, overlooking the importance of this stage, and no benchmark exists to evaluate AI's ability to conduct systematic experiment design. To bridge this gap, we propose SCOPE, a Scientific COmprehensive Planning Evaluation Benchmark constructed from 300 high-quality latest p...
  </details>

- **2026-08-04** — Yu Pei, Cunming Zhang, Jeongju Sohn et al. — [Assessing Behavioral Validation in UI Component Test Suites Using Inferred Metamorphic Relations](http://arxiv.org/abs/2608.03337v1)
  <details><summary>📄 Abstract</summary>
  UI component libraries are commonly assessed using execution-based metrics such as statement and branch coverage, yet these metrics provide limited insight into whether tests verify the behavioral relations implied by component APIs and documentation. This paper presents an MR-based framework that uses inferred metamorphic relations (MRs) as an empirical behavioral reference, rather than a complete specification, for assessing UI component test suites. Given a component's source, documentation, ...
  </details>

- **2026-08-04** — Sicong Chang, Yidan Shen, Wen Yu et al. — [Lightweight Chunk Selection for Mobile Retrieval-Augmented Generation](http://arxiv.org/abs/2608.03148v1)
  <details><summary>📄 Abstract</summary>
  RAG improves the factual grounding of LLM by incorporating external knowledge, but deploying RAG on mobile and edge devices remains challenging because retrieved context increases computation and memory. A direct way to reduce this cost is to retain only one retrieved chunk before generation, but the top-ranked retrieved chunk is not always the most evidence-supporting one, since retrieval similarity does not necessarily imply evidential sufficiency. Existing context-reduction methods can improv...
  </details>

- **2026-08-04** — Huanglong Ji, Botong Zhao, Shujing Lv et al. — [LDU-Bench: Multimodal LLM Evaluation for Lithography Defect Understanding under Layout-Varying Circuit Backgrounds](http://arxiv.org/abs/2608.03078v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have demonstrated strong defect recognition capability in industrial anomaly detection. However, in lithography review, merely determining whether an image contains a defect is insufficient for engineering inspection; models must also understand defect morphology, spatial location, and the potential causes supported by visible evidence. To this end, this paper proposes LDU-Bench, a multi-task multimodal benchmark for lithography defect understanding. Constructed ...
  </details>

- **2026-08-04** — Yichao Liu, Jiaxue Zhou, Weifeng Han et al. — [Breaking the trade-off between invisibility and sensitivity in electromagnetic sensing](http://arxiv.org/abs/2608.03042v1)
  <details><summary>📄 Abstract</summary>
  Weak electromagnetic signals demand highly sensitive sensors, yet increasing a sensor's sensitivity inevitably strengthens its interaction with the surrounding field, producing scattering that perturbs the very signals being measured. Conversely, existing cloaking strategies suppress scattering only by isolating the sensor from incident waves, thereby compromising signal reception. Resolving this long-standing trade-off between invisibility and sensitivity has remained an outstanding challenge. ...
  </details>

- **2026-08-04** — Jong Hak Moon, Minjun Kim, Minjun Kim — [Clinically-Grounded Hierarchical Classification for Consistent Chest X-ray Interpretation](http://arxiv.org/abs/2608.03016v1)
  <details><summary>📄 Abstract</summary>
  Accurate chest X-ray interpretation is inherently hierarchical. Clinical decisions depend not only on what abnormality is present but where it is situated, requiring reasoning from broad anatomical systems down to specific pathological findings. Yet existing automated systems largely treat this as a flat classification problem, failing to capture inter-level dependencies or enforce coherence between coarse and fine predictions. We propose CHASE (Classification with Hierarchical Analysis and Stru...
  </details>

- **2026-08-04** — Nicolas Zumarraga, Lorenzo Steno, Ning Wang et al. — [TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series](http://arxiv.org/abs/2608.03391v1)
  <details><summary>📄 Abstract</summary>
  Precise anomaly localization over long-context time series is a crucial task in monitoring applications across clinical care, industrial operations, financial services, and logistics, where brief evidence may hide inside long spans of high-frequency data. Time-Series Language Models (TSLMs) are able to ingest time series data and verbalize findings on anomalies in natural language; however, recent benchmarks report a decrease in retrieval performance at long contexts, mirroring failure modes in ...
  </details>

- **2026-08-04** — Razieh Chalehchaleh, Reza Farahbakhsh, Noel Crespi — [Unequal Verdicts: Investigating Gender Bias in LLM-Based Fake News Detection](http://arxiv.org/abs/2608.03627v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used for automated fact-checking, yet their susceptibility to gender bias in this context remains underexplored. This study presents the first systematic investigation of gender bias in LLM-based fake news detection using real-world data. We augment the LIAR benchmark with three gender variants of speaker job titles (Neutral, Male, Female) for each statement to test whether veracity judgments vary solely based on gender presentation. Six state-of-the...
  </details>

- **2026-08-04** — Alex Kwon — [FACTWASH: Catching AI Rewrites That Wash Hearsay into Fact](http://arxiv.org/abs/2608.03372v1)
  <details><summary>📄 Abstract</summary>
  AI systems rewrite information constantly: conversations become stored memories, documents become answers. The rewrite can keep a claim while washing away what made it checkable, who said it, how sure they were, when it held. We call that failure factwashing, and release factwash, an open-source write-time gate that catches it deterministically, with named flags and evidence rather than an LLM judge. Building it answers a practical question: when does a cheap check suffice, and when do you need ...
  </details>

- **2026-08-04** — Zian Wang, Changchun Li — [DRPFNet: Dual-domain Residual Progressive Fusion Network for RGB-Thermal Object Detection](http://arxiv.org/abs/2608.03370v1)
  <details><summary>📄 Abstract</summary>
  RGB-thermal (RGB-T) object detection aims to fuse complementary information from visible and thermal modalities to achieve robust detection under varying illumination and weather conditions. Current methods typically employ attention mechanisms or transformers to perform cross-modal fusion independently at each feature scale, directly combining RGB and thermal features in the spatial domain. However, they still face significant limitations: cross-level knowledge inheritance caused by independent...
  </details>

- **2026-08-04** — Zihan Wang, Tong Liu, Zhiwei Wang et al. — [LocAnyMed: Vision-Language Grounding for Multimodal Medical Images](http://arxiv.org/abs/2608.03322v1)
  <details><summary>📄 Abstract</summary>
  Medical visual grounding connects free-form clinical queries to spatial evidence in medical images and is an important component of interpretable medical artificial intelligence. However, general-purpose grounding models are predominantly trained on natural images, while existing medical localization resources remain fragmented across imaging modalities, datasets, and task formulations. To address this gap, we construct LocAnyMed-200K, a multimodal medical visual grounding dataset containing app...
  </details>

- **2026-08-03** — Yuekun Wang, Mingfei Cheng, Xiaofei Xie — [PRWeaver: Evaluating LLM-Based Code Auditors against Long-Horizon Malicious Pull Requests](http://arxiv.org/abs/2608.02693v1)
  <details><summary>📄 Abstract</summary>
  LLM-based code auditors are increasingly integrated into pull-request (PR) workflows, yet their reliability against adversarial changes distributed across repository evolution remains poorly understood. We introduce PRWeaver, a benchmark of 208 execution-validated attacks from ten real-world repositories, each instantiated under four matched review renderings (832 renderings in total). We evaluate three PR-auditing agents across six auditor-model systems. Across all systems, decomposing an attac...
  </details>

- **2026-08-03** — Max Torop, Aria Masoomi, Jennifer Dy — [Inverted Detection and Control in Steering Vectors](http://arxiv.org/abs/2608.02957v1)
  <details><summary>📄 Abstract</summary>
  Steering vectors (SVs) are widely used to influence the expression of concepts (e.g., truthfulness) in large language model outputs. A key assumption underpinning SVs is that they are linearly discriminative with respect to the concept: representations of texts that exhibit the concept are more aligned with the SV than those that do not, motivating shifts along the positive or negative SV direction to respectively promote or suppress the concept. In this work, we identify an inverted detection-c...
  </details>

- **2026-08-03** — Tankun Li, Zhi Chen, Yaohua Tang — [LEAP: Lean Environment-Feedback via Adaptive Pruning for Code RL in GPU Kernel Generation](http://arxiv.org/abs/2608.01804v2)
  <details><summary>📄 Abstract</summary>
  Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities. To bypass the heavy memory footprint of critic networks, current state-of-the-art frameworks leverage critic-free paradigms like Group Relative Policy Optimization (GRPO) tied to rule-based verification sandboxes. However, applying these frameworks to low-level systems programming, such as CUDA kernel generation-presents severe challenges: binary pass/fail rewards i...
  </details>

- **2026-08-03** — Zibo Xiao, Haoyu Wang, Jun Sun — [$S^3$: Improving Agent Safety through Multi-Stage Defense](http://arxiv.org/abs/2608.02683v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents rely on multi-stage agentic workflows, with stages such as memory, planning, and tool execution, to accomplish complex tasks. However, risks may emerge at different stages, propagate across steps, and become difficult to detect and mitigate. Existing safety methods protect only isolated stages and are difficult to integrate, leaving agents without comprehensive protection throughout the workflow. To address these limitations, we introduce Stage-Specific Safety S...
  </details>

- **2026-08-03** — Priyanka Bajaj — [Evaluation Blindness: How Silent Measurement Failures Corrupt AI Systems from Training to Deployment](http://arxiv.org/abs/2608.02786v1)
  <details><summary>📄 Abstract</summary>
  AI systems can fail silently. The failure propagates through training loops, evaluation pipelines, and production monitoring stacks until downstream harm makes it visible. This paper introduces evaluation blindness: a measurement function M exhibits evaluation blindness with respect to failure class F when it produces readings indistinguishable from a healthy state while the system is actually failing, with no auxiliary signal flagging the gap.   The problem surfaces at two lifecycle stages the ...
  </details>

- **2026-08-03** — Saptarshi Neil Sinha, Tiago Kleist, Giorgio Trumpy — [A Human-in-the-Loop Deep Learning Framework for Color Reconstruction of Lenticular Films](http://arxiv.org/abs/2608.02835v1)
  <details><summary>📄 Abstract</summary>
  Historical lenticular films, such as those created with the Kodacolor process, encode color information in a distinctive spatial format. This structure requires specialized techniques for accurate color reconstruction. While recent signal processing approaches like doLCE and deep learning methods like deep-doLCE have advanced automated color recovery, they often fail with cases such as curved lenticules, low-contrast, or badly captured regions. We propose a human-in-the-loop (HITL) deep learning...
  </details>

- **2026-08-03** — Michael Farmer — [Abduction Without a Body? Representational Grounding and the Abduction Loop for Scientific Hypothesis Generation](http://arxiv.org/abs/2608.02505v1)
  <details><summary>📄 Abstract</summary>
  Can scientific abduction occur without continuous sensorimotor embodiment? Recent arguments in AI and philosophy of science hold that genuine hypothesis generation requires an agent continuously coupled to the physical world. We defend a narrower claim: online embodiment is not necessary for every abductive scientific act. Our focus is identity abduction: the inference that two independently developed structures are one object under an explicit correspondence, reached through representational gr...
  </details>

- **2026-08-03** — Weifeng Yuan, Wenbo Guo, Qingyun Du et al. — [Mutate to Bypass: Autonomous Endpoint Evasion via Knowledge-Driven Multi-Agent Orchestration](http://arxiv.org/abs/2608.01639v1)
  <details><summary>📄 Abstract</summary>
  Public reports and open-source resources expose many EDR evasion techniques, but it remains unclear whether commercial Endpoint Detection and Response (EDR) systems can withstand these documented attacks. Evaluating them requires turning fragmented security knowledge into working payloads and refining those payloads from opaque alerts, tasks that existing automation does not address. We present AutoBypass, a knowledge-grounded, closed-loop multi-agent framework for automated EDR resilience asses...
  </details>

- **2026-08-03** — Nicole Mitchell, Dhruv Agarwal, Maty Bohacek et al. — [Long-term Measurements: Towards a Longitudinal Understanding of Human-AI Interactions](http://arxiv.org/abs/2608.02491v1)
  <details><summary>📄 Abstract</summary>
  Language models have taken on the role of a very new type of technology, by virtue of their "human-ness" and rapid integration into users' daily lives. This combination of features can introduce longitudinal risks---cognitive, developmental and socio-affective changes in humans---that might not surface in short-term interactions, but can have lasting long-term effects on users. This forms the basis of a critical new mission for NLP: to pivot from static, short-term evaluations of text generation...
  </details>

- **2026-08-03** — Yonatan Ben Avraham, Baruch Binyaminov, Yehudit Aperstein — [UAV-Based Environmental Monitoring of Rip-Current Indicators Using Wavelet-Derived Texture Features](http://arxiv.org/abs/2608.02448v1)
  <details><summary>📄 Abstract</summary>
  Rip currents are recurrent coastal natural hazards that threaten beachgoers and create operational challenges for lifeguards and coastal managers. Reliable monitoring from standard RGB (red-green-blue) imagery acquired by unmanned aerial vehicles (UAVs) remains difficult because hazardous channels often appear as subtle gaps in breaking waves, foam texture, or sediment patterns, and these signatures are affected by illumination, sea state, and environmental noise. This study presents a physicall...
  </details>

- **2026-08-03** — Benjamin Zec, Lukas Schmidbauer, Maja Franz et al. — [Towards Tensor-Network SAT-Solvers for Quantum-Classical Workflows](http://arxiv.org/abs/2608.02041v1)
  <details><summary>📄 Abstract</summary>
  Integrated HPC/QC systems aim to combine classical high-performance computing with quantum processors, but cannot be reduced to mechanisms for dispatching quantum kernels. An integrated architecture must support aspects such as observability, which cannot be implemented using QPUs alone, as well as fallback execution and cost-aware decisions on whether to replace quantum tasks with classical surrogates. Such mechanisms must be approximate or benefit from problem structure to soften the inescapab...
  </details>

- **2026-08-03** — Wenxiao Fan, Jingling Fu, Fang Li et al. — [Recompute or Reuse? Diagnosing and Mitigating Textual Shortcuts in VLM Self-Reflection](http://arxiv.org/abs/2608.01930v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are expected to revise their reasoning when visual evidence changes. Failures to do so are often attributed to insufficient visual attention or contextual inertia, leaving unclear what models reuse instead of recomputing from the current image. We show that evidence-bearing reasoning in a prior chain of thought (CoT) can form a textual shortcut that competes behaviorally with visual recomputation. Across 16 VLMs, a matched counterfactual analysis identifies evidence...
  </details>

- **2026-08-03** — Huy Quang Ung, Guillaume Habault, Roberto Legaspi et al. — [Assessing the Benefits of Combining Advanced Deep Learning Techniques for Post-Disaster Building Damage Assessment from UAV Imagery](http://arxiv.org/abs/2608.01906v1)
  <details><summary>📄 Abstract</summary>
  Rapid and accurate post-disaster building damage assessment is essential, yet remains a challenging task. Unmanned Aerial Vehicle (UAV) imagery offers a timely and high-resolution view of affected areas, but existing Computer Vision (CV) models often demand large annotated datasets, generalize poorly across geographic regions and their assessment policies, and are confined to the specific tasks they were trained for. Large Vision-Language Models (LVLMs) offer a promising alternative through thei...
  </details>

- **2026-08-03** — Tankun Li, Zhi Chen, Yaohua Tang — [LEAP: Lean Environment-Feedback via Adaptive Pruning for Code RL in GPU Kernel Generation](http://arxiv.org/abs/2608.01804v1)
  <details><summary>📄 Abstract</summary>
  Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities. To bypass the heavy memory footprint of critic networks, current state-of-the-art frameworks leverage critic-free paradigms like Group Relative Policy Optimization (GRPO) tied to rule-based verification sandboxes. However, applying these frameworks to low-level systems programming, such as CUDA kernel generation-presents severe challenges: binary pass/fail rewards i...
  </details>

- **2026-08-03** — Dongqi Wang, Weiwei Chen, Han Zhou et al. — [Leveraging AI for fine-grained food safety risk forecasting in sparse data conditions](http://arxiv.org/abs/2608.01767v1)
  <details><summary>📄 Abstract</summary>
  Ensuring food safety represents a critical public health challenge, particularly when inspection resources are limited and regional sampling data are sparse. This study proposes a Transformer-based framework capable of forecasting fine-grained, city-level food safety risks by unifying over 11 million inspection records with supplemental demographic, economic, and environmental indicators extracted from the Statistical Yearbook. A three-stage pretraining design leverages partial supervision from ...
  </details>

- **2026-08-03** — Jinghan Xu, Longze Fan, Zeyuan Wang et al. — [Beyond Single-Use Tokens: Durable Authorization State for Replay-Resistant LLM Agent Actions](http://arxiv.org/abs/2608.01710v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model agents frequently replan, retry failed operations, delegate tasks, and resume after crashes. These behaviors can cause one user authorization to be requested and executed multiple times under freshly issued token identifiers, even when each individual token is single-use. We call this failure semantic replay: exceeding the execution budget of a token-independent authorization instance rather than merely reusing an old token identifier. We show that identifier-loca...
  </details>

- **2026-08-03** — Víctor Vilchez, Tiago P. C. de Andrade, Edward Hinojosa et al. — [LEO-Aware DRL Meta-Scheduler for 5G Non-Terrestrial Network Slicing](http://arxiv.org/abs/2608.01668v1)
  <details><summary>📄 Abstract</summary>
  The integration of Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) into 5G and upcoming 6G architectures introduces various challenges, including severe propagation delays, ultra-high base station mobility, and channel non-stationarity, complicating radio resource management of heterogeneous network slices. In this paper, we propose a deep reinforcement learning (DRL) meta-scheduler for twin-timescale resource allocation. Our solution adopts a decoupled Open Radio Access Network (RAN) arch...
  </details>

- **2026-08-03** — Yaning Zhang, Jiao Wu, Zan Gao et al. — [FairForensics: Seeing Expressions and Parsing Demographics via Vision-Language Modeling for Generalizable Fair Deepfake Detection](http://arxiv.org/abs/2608.01661v1)
  <details><summary>📄 Abstract</summary>
  The challenge of fair deepfake detection (FDD) has attracted increasing attention. Existing fairness-enhanced detectors often suffer from suboptimal generalization to unseen manipulations and fairness across demographic groups. They are typically developed and evaluated on demographically imbalanced distributions, resulting in biased predictions toward minority groups. In this paper, we construct a novel demographically balanced FDD benchmark to train and evaluate the fairness of detectors under...
  </details>

- **2026-08-03** — Donglin Xie, Xueying Gui, Yutian Zhu et al. — [Smartwatch Photoplethysmography-Derived Heart Age via ECG-Guided Cross-Modal Pretraining as a Digital Biomarker of Vascular Aging](http://arxiv.org/abs/2608.01620v1)
  <details><summary>📄 Abstract</summary>
  Digital biomarkers of cardiovascular aging, often termed heart or vascular age, have been widely studied, but most rely on resting electrocardiography (ECG), imaging, or specialized vascular assessments. Evidence linking wearable photoplethysmography (PPG) to arterial stiffness and hypertension remains limited. We developed an ECG-guided cross-modal framework that uses synchronized smartwatch ECG to enhance PPG representation learning during pretraining while requiring only PPG at inference. The...
  </details>

- **2026-08-03** — Zihan Yang, Yang Guo, Hongxing Zhang et al. — [DyFrDet: Towards Accurate Small Object Detection via Dynamic Frequency Suppression with Label Disambiguation](http://arxiv.org/abs/2608.02495v1)
  <details><summary>📄 Abstract</summary>
  Despite the remarkable progress over the past decades, accurately identifying small objects remains challenging because of their insufficient visual cues. Previous works typically attempt to construct discriminative representation of the small objects. However, the wide range frequency domain noises and label ambiguities have been greatly overlooked, which significantly hinders the accurate localization. To address these issues, we propose a novel small object detection (SOD) detector termed DyF...
  </details>

- **2026-08-03** — Chongjian Wang, Junjie Gao — [SWINSleepNet: A Hierarchical Context-Aware Framework for Sleep Staging (v2)](http://arxiv.org/abs/2608.02183v1)
  <details><summary>📄 Abstract</summary>
  Automatic sleep staging is a critical role in sleep disorder diagnosis, sleep quality assessment, and long-term health monitoring; however, existing approaches suffer poor performance on ambiguous and transition-related sleep stages, caused by inadequate modeling of fine-grained intra-epoch structures and complex cross-region spectral dependencies. Traditional epoch-level encoders commonly fail to extract subtle temporal microstructures and intra-epoch cross-region interactions, resulting in uns...
  </details>

- **2026-08-03** — Camile Lendering, Erkut Akdag, Joaquín Figueira et al. — [ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection](http://arxiv.org/abs/2608.01793v1)
  <details><summary>📄 Abstract</summary>
  Unified anomaly detection requires modeling highly heterogeneous normal data without access to anomalous samples. While foundation models like DINOv2 provide rich token representations, leveraging these spaces for explicit density estimation remains challenging. Energy-Based Models (EBMs) offer a principled formulation, but their training in high-dimensional token spaces is unstable due to anisotropy and strong cross-dimensional correlations, which degrades finite-step Markov Chain Monte Carlo (...
  </details>

- **2026-08-03** — Ruifeng Wang, Di Yang, Jiangtao Wang — [Entity-Aware Sequence Transduction for Player-Centric Ball Action Spotting](http://arxiv.org/abs/2608.01696v1)
  <details><summary>📄 Abstract</summary>
  Player-centric ball action spotting requires temporally precise event detection together with actor attribution in crowded, partially observed multi-agent sports videos. Existing Denoising Sequence Transduction (DST) baselines treat the player-role dimension as part of a flattened frame-level representation, which weakens the inductive bias for modeling player-specific temporal evolution and inter-player interactions. To address this limitation, we propose Multi-Entity Denoising Sequence Transdu...
  </details>

- **2026-08-02** — Lehan Zhang, Yinlei Cheng, Shiqi Hu Yiheng Zhou et al. — [MRAFnd: Multimodal Retrieval-Augmented Framework for Zero-Shot Fake News Detection](http://arxiv.org/abs/2608.01430v1)
  <details><summary>📄 Abstract</summary>
  The rapid dissemination of multimodal content has intensified the spread of fabricated news, presenting a substantial threat to social integrity. A formidable challenge for current detection systems is identifying misinformation related to novel events in zero-shot scenarios. Prevailing zero-shot methods typically assess news items in isolation via semantic matching, a strategy that fails to recognize the recycled disinformation tactics from past campaigns and lacks the sophisticated reasoning n...
  </details>

- **2026-08-02** — Sabri Mustafa Kahya, Richard R. Chen, Muhammet Sami Yavuz et al. — [Training-Free Out-of-Distribution Detection for Pathology Whole-Slide Images](http://arxiv.org/abs/2608.01407v1)
  <details><summary>📄 Abstract</summary>
  Safe deployment of AI methods in medicine requires robust guardrails that detect when input data deviate from the training distribution to ensure that models provide predictions only within their scope of expertise and abstain otherwise. Out-of-distribution (OOD) detection can provide such safeguards and is extensively studied in general computer vision. Yet, it remains underdeveloped in computational pathology, where gigapixel whole-slide images (WSIs), subtle differences between disease subtyp...
  </details>

- **2026-08-02** — Yang Yang, Boyun Xu, Shaofeng Liang et al. — [CraftAlign: Feature-Grounded Evaluation and Revision Guidance for AI Stories](http://arxiv.org/abs/2608.01377v1)
  <details><summary>📄 Abstract</summary>
  Large language models can now generate fluent and complete stories, yet many outputs still feel formulaic and unnatural because of cliches, over-explanation, linear causal progression, and stereotyped endings, an immediately recognizable AI flavor. Existing detection and evaluation methods often stop at source labels or holistic scores, while revision methods typically target predefined issues through localized edits, limiting their ability to support multiple plausible revision strategies or gu...
  </details>

- **2026-08-02** — Zirui Zhang, Yinbo Yu, Donghai Guan et al. — [A Benchmark Dataset for MLLM-Generated Image Detection: GPT Image2 & Nano Banana2](http://arxiv.org/abs/2608.01258v1)
  <details><summary>📄 Abstract</summary>
  The realism of images generated by multimodal large language models (MLLMs), such as GPT Image2 and Nano Banana2, has improved rapidly in recent years. Compared with early generative models, current models have made clear progress in text rendering. They can produce high-quality images that closely resemble real-world application scenarios. The enhanced generation capabilities of current MLLMs pose increasingly severe challenges to AI-generated image detection. Detection is no longer limited to ...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 64 papers

- **2026-08-04** — Pervez Shaik, Prosenjit Biswas, Abhinav Thorat et al. — [ATLAS: Learning to Recommend Across Unseen Domains](http://arxiv.org/abs/2608.03899v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems remain domain-bound: a model trained on one interaction environment typically requires retraining or target-domain adaptation before it can operate on a new catalogue. A recommender trained on movies cannot be directly deployed to recommend groceries or video games. Existing approaches mitigate this by transferring restricted forms of recommendation knowledge, adapting to the target domain, or leveraging large language models (LLMs) for transferable representations. We instea...
  </details>

- **2026-08-04** — Adam Coscia, Sujata Duwal, Langdon Holmes et al. — [Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education](http://arxiv.org/abs/2608.04006v1)
  <details><summary>📄 Abstract</summary>
  LLMs are reshaping educational technology, yet evaluating their responses for pedagogical alignment remains underexplored, relying heavily on the expertise of learning engineers building the technology. To bridge this gap, we explore trustworthiness as a structured lens for evaluation, leveraging existing measures of LLM trustworthiness to systematically identify potential pedagogical disruptions. Through a longitudinal co-design process with learning engineers developing an LLM-powered digital ...
  </details>

- **2026-08-04** — Mobina Kashaniyan, Ali Jannesari — [Interpretable Adaptive Sampling for LLM Test-Time Scaling](http://arxiv.org/abs/2608.03961v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling improves LLM reasoning by generating and aggregating multiple candidate answers, yet many pipelines use fixed per-query budgets that spend the same compute on easy and difficult prompts. These fixed budgets are also difficult to inspect because they do not explain why a given prompt receives a particular number of samples. We propose adaptive} test-time scaling with a lightweight fuzzy controller that maps interpretable signals, including estimated prompt complexity and model c...
  </details>

- **2026-08-04** — Yuanshen Guan, Zipeng Feng, Zhiwei Xiong et al. — [Latent Reward Registers for Diffusion Preference Alignment](http://arxiv.org/abs/2608.03929v1)
  <details><summary>📄 Abstract</summary>
  Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout m...
  </details>

- **2026-08-04** — Mattias Luber, Timo Betz — [A Physics-Flavored Transformer Network for Parametrizing Contraction Dynamics of Engineered Skeletal Muscle Tissues](http://arxiv.org/abs/2608.03927v1)
  <details><summary>📄 Abstract</summary>
  Engineered Skeletal Muscle Tissues (ESMs) have become a key structure for biomedical disease modeling and pharmacological screening, yet their functional characterization often relies on simplistic metrics like peak force, discarding critical kinetic information. This is partially due to the high level of mathematical complexity which mechanistic models introduce to capture these dynamics. Hence, exactly the complexity prevents scalable application and widespread adaptation in the field. Here we...
  </details>

- **2026-08-04** — Matt Ratto, Abhishek Moturu, Daniel Silver — [Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social Theory](http://arxiv.org/abs/2608.03910v1)
  <details><summary>📄 Abstract</summary>
  As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recognize, represent, and respond to multiple legitimate perspectives. This has led to growing interest in pluralistic alignment, which seeks to move beyond one-size-fits-all models of appropriate behaviour. However, current approaches often lack a clear account of how values are socially organized, cont...
  </details>

- **2026-08-04** — Alberto Acedo — [Omega-S: A Functional Resilience Index for LLM Fine-Tuning](http://arxiv.org/abs/2608.03887v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a large language model on new data degrades what it previously learned. We present Omega-S, a drop-in penalty computed from the weight matrix alone: it needs no previous-task data, no Fisher matrix and no stored copy of the old weights. It is three lines in an existing training loop and adds under 4% to the cost of a step.   Retention. On Llama-3-8B with LoRA, fine-tuned from code to prose and measured by HumanEval over ten seeds, Omega-S retains more of the original capability than ...
  </details>

- **2026-08-04** — Pyrros Koussios, Chenhao Li, Xin Chen et al. — [Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning](http://arxiv.org/abs/2608.03875v1)
  <details><summary>📄 Abstract</summary>
  Designing effective reward functions remains a major bottleneck in Reinforcement Learning (RL). Recent work uses large foundation Vision-Language Models (VLMs) as reward models, computing text-observation similarity to bypass manual reward engineering. Although promising, these rewards are often noisy and unreliable, limiting their direct utility during deployment. We present Structure-Aware Fine-Tuning (SAFT), a simple, self-supervised method that refines these imperfect reward signals online w...
  </details>

- **2026-08-04** — Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi et al. — [Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation](http://arxiv.org/abs/2608.03166v1)
  <details><summary>📄 Abstract</summary>
  Role-Playing Language Agents (RPLAs) are increasingly deployed in high-stakes applications such as healthcare assistance, customer support, and education, where maintaining consistent personas, ethical constraints, and behavioral coherence under adversarial pressure is critical. Existing evaluation approaches rely on static benchmarks or isolated single-turn prompts that fail to capture cumulative behavioral failures emerging over extended interactions.   We present a modular multi-agent platfor...
  </details>

- **2026-08-04** — Georgy Lukyanov — [Effort without Evidence](http://arxiv.org/abs/2608.03719v1)
  <details><summary>📄 Abstract</summary>
  Actions determine not only payoffs but what can be learned. I study communication across successive decision makers when hidden effort governs public evidence and a sender motivates her successor while underweighting effort cost. Common sender rankings can force every message into a Bayes-unavoidable nonidentifying region. If experimentation is costly, strong motivation can make persuasive encouragement incredible and produce inactivity after a confounded failure. If maximal effort is technologi...
  </details>

- **2026-08-04** — Abraham Camelo-Guerrero, Jairo Diaz-Rodriguez — [How Closely Do LLM Reviews Align with Human Peer Review?](http://arxiv.org/abs/2608.03659v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate scientific reviews, yet existing evaluations rarely examine whether different providers align with both conference decisions and human reviewing priorities within the same controlled setting. We compare reviews from OpenAI GPT-5.4, Google Gemini 3.1 Pro Preview, and Anthropic Claude Opus 4.6 with human reviews and final decisions for 300 topic-matched ICLR 2026 submissions, equally divided among oral, poster, and rejected papers. Eac...
  </details>

- **2026-08-04** — Eleftherios Batzolis, George Drosatos, Vassilis Katsouros et al. — [A Security-Oriented Lifecycle Model for Large Language Model Systems](http://arxiv.org/abs/2608.03626v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being integrated into critical infrastructure and enterprise workflows at unprecedented scale,yet the lifecycle frameworks governing their development and operations were designed for operational efficiency rather than security analysis. As a result, security-relevant activities such as data provenance verification, artifact signing, agentic permission control, and decommissioning are often left implicit or assumed to receive due care. Governance frameworks, in turn, or...
  </details>

- **2026-08-04** — Lydia Manikonda, Dominique Outlaw — [Policy Fragmentation or Institutional Alignment? Institutional Governance of AI in Universities and Business Schools](http://arxiv.org/abs/2608.03584v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is rapidly transforming high-skilled domains, requiring higher education institutions (HEI) to balance the teaching of foundational principles with the integration of emerging tools to ensure workforce readiness. While HEI are increasingly adopting AI, many continue to grapple with how it should be incorporated into curricula and governed through policy, especially when such policies are set at different levels of an institution. This research analyzes AI policies ac...
  </details>

- **2026-08-04** — Alexander M. Fichtl, Lukas Ellinger, Josefin Kelber et al. — [AI-Assisted Peer Review Across Research Communities: From Reviewer AI Policies to LLM Review Quality](http://arxiv.org/abs/2608.03581v1)
  <details><summary>📄 Abstract</summary>
  AI-assisted peer review is increasingly discussed and adopted as a tool to support the scientific publishing process, yet there is little systematic understanding of how publication venues regulate its use or of how capable current AI review systems are. We address these questions by first surveying reviewer-facing AI policies across 111 leading AI/NLP conferences and medical journals, revealing substantial regulation differences between the two communities. Second, we evaluate AI-generated peer...
  </details>

- **2026-08-04** — Xiang Li, Pengcheng Wang, Huazheng Wang et al. — [Pin Once, Swap Light: Subspace-Aligned Centroid-Residual Training for Efficient Ultra-LoRA Serving](http://arxiv.org/abs/2608.03579v1)
  <details><summary>📄 Abstract</summary>
  Modern multi-tenant Low-Rank Adapters (LoRAs) serving systems concurrently host tens to hundreds of LoRA adapters. Though powerful, this introduces a critical system dilemma between serving efficiency and task performance: higher-rank adapters generally achieve better downstream task performance, but their GPU VRAM footprint and Host-to-Device PCIe swapping overhead severely constrain scalability. Conversely, ultra-low-rank adapters ($r \le 2$) minimize both VRAM footprint and PCIe transfer over...
  </details>

- **2026-08-04** — Zixuan Liu, Fangzheng Wu, Brian Summa et al. — [Robust General Utility for Reinforcement Learning](http://arxiv.org/abs/2608.03562v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) with general utility extends classic RL by optimizing an arbitrary utility functional of the policy-induced occupancy measure, thereby enabling a broader range of applications. However, previous work on general utility RL typically assumes the evaluation utility is fixed and correctly specified. In practice, the utility used at deployment can deviate from the training one, creating a robustness gap that prior work does not address. Motivated by this, we propose robust...
  </details>

- **2026-08-04** — Ruolei Zhang, Teddy Njuguna, Yue Feng — [Cross-Lingual Bias in Large Language Models: A Comparative Analysis of English and Swahili](http://arxiv.org/abs/2608.03532v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in multilingual contexts, yet safety alignment and bias evaluation remain overwhelmingly English-centric. We investigate whether social biases generalise across languages by submitting 4,900 symmetric English--Swahili prompt pairs to GPT-5.2 and Gemini 2.5 Flash across nine demographic bias axes, yielding 19,600 completions evaluated for stereotype prevalence, sentiment, refusal behaviour, and cross-lingual semantic similarity. Our findings show th...
  </details>

- **2026-08-04** — Qiming Li, Shujie Hu, Haohan Liu et al. — [MT-Web2Code: Benchmarking Coding Agents on Multi-Turn Regional Reconstruction and Localized Modification](http://arxiv.org/abs/2608.03474v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Large Vision-Language Models (LVLMs) have demonstrated impressive capabilities in web UI generation. However, existing benchmarks predominantly focus on single-turn full-page generation from scratch, overlooking the iterative workflow of real-world frontend engineering, where developers repeatedly reconstruct missing regions and modify localized elements within existing codebases. To bridge this gap, we introduce MT-Web2Code, the first multimodal coding benchmark for multi-tur...
  </details>

- **2026-08-04** — Boyan Li, Zhuowen Liang, Yupeng Xie et al. — [DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces](http://arxiv.org/abs/2608.03451v1)
  <details><summary>📄 Abstract</summary>
  Data agents enable natural-language analytics over organizational workspaces, where relevant evidence may be scattered across databases, structured files, long documents, and multimedia. Existing benchmarks largely isolate structured querying, retrieval, or open-ended analysis, leaving heterogeneous evidence discovery, complete tabular outputs, and deterministic evaluation insufficiently unified. We introduce DataSpace, a benchmark in which data agents produce verifiable tabular results from tas...
  </details>

- **2026-08-04** — Adnan Al Ali, Kathy Hämmerl, Jindřich Libovický et al. — [Predicting Multilingual Classification and Translation Performance of LLMs with Cross-Lingual Alignment $\unicode{x2013}$ Is English Enough?](http://arxiv.org/abs/2608.03446v1)
  <details><summary>📄 Abstract</summary>
  Multilingual large language models (LLMs) have been shown to perform better on non-English classification tasks when the representations of the given language are more aligned to English within the model. Several cross-lingual alignment (CLA) scores have been proposed for use with LLMs, along with multiple approaches for extracting embeddings from the models. We provide a comparative analysis of 27 CLA score variants, examining how they differ and how well each predicts downstream performance ac...
  </details>

- **2026-08-04** — Eugene Lee, Oseong Choi, Byungsoo Kang et al. — [LLM-Derived Priors for Thompson Sampling in Cold-Start Comment Recommendation](http://arxiv.org/abs/2608.03382v1)
  <details><summary>📄 Abstract</summary>
  Multi-armed bandit algorithms, especially Thompson sampling, are widely used in online recommendation. Despite their ability to adapt from online feedback, these methods often suffer from cold-start limitations when newly introduced arms have little or no interaction history. In our setting, the candidate arms are user-generated textual comments, whose semantic content can reveal a title's appeal before sufficient interaction feedback is available. We therefore use large language models (LLMs) t...
  </details>

- **2026-08-04** — Jing Dai, Qibin Zhang, Weiwei Zhou et al. — [CIGTSurv: Clinical Information Guided Tri-modal Survival Prediction with Local Prototype Association and Global Feature Alignment](http://arxiv.org/abs/2608.03247v1)
  <details><summary>📄 Abstract</summary>
  Multimodal learning has significantly advanced survival prediction by integrating pathology images with genomic data. However, clinical information, despite its critical role in reflecting a patient' s overall health, remains underutilized due to its discrete, sparse, and low-dimensional nature. Furthermore, the inherent heterogeneity across these modalities pose significant challenges in modeling cross-modal interactions. In this paper, we propose CIGTSurv, a Clinical Information Guided Tri-mod...
  </details>

- **2026-08-04** — Ming Shen, Chao Shang, Sadat Shahriar et al. — [Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2608.03239v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based multi-agent systems (LLM-MAS) are designed through roles, debate protocols, and aggregation rules. These choices create implicit social expectations: agents may be expected to trust, challenge, defer to, or collaborate with peers. We study the effects of making inter-agent relation semantics explicit. We use a minimal signed-network formulation of relational priors and inject natural-language renderings into agent system prompts while holding the task protocol fixed. A...
  </details>

- **2026-08-04** — Tianbao Jiang, Weicong Ni, Gerard de Melo et al. — [Aligning Large Vision-Language Models at Test Time: A Trajectory-Guided Structured Sampling Approach](http://arxiv.org/abs/2608.03204v1)
  <details><summary>📄 Abstract</summary>
  Post-training reinforcement learning (RL) algorithms are commonly used to align large vision-language models (LVLMs) with human intent and the requirements of visual reasoning tasks. However, existing RL-based alignment methods are often resource-intensive and encounter mismatches between training objectives and inference-time distributions. To bridge this gap, we propose a novel test-time alignment approach that leverages trajectory-guided structured sampling for dynamic inference-time refineme...
  </details>

- **2026-08-04** — Xiangyun Huang, Xiangchen Wang, Runfeng Lin et al. — [From Routes to Steps: Separating Semantic Progress from Local Execution in Vision-and-Language Navigation](http://arxiv.org/abs/2608.03143v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) requires an agent to follow a route-level instruction by executing its constituent steps from egocentric visual observations. Existing VLM-based navigators typically supervise both capabilities through next-action prediction alone, making progress-tracking errors difficult to distinguish from execution errors. When an agent deviates from the route, a corrective action label may recover the next movement but does not indicate whether the agent selected the wro...
  </details>

- **2026-08-04** — Binglei Li, Mengping Yang, Zhiyu Tan et al. — [DiverseDiT++: Quantifying, Analyzing, and Promoting Representation Diversity in Diffusion Transformers](http://arxiv.org/abs/2608.03082v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Diffusion Transformers (DiTs) have enabled remarkable progress in visual synthesis, benefiting from their superior scalability. To facilitate DiTs' capability of capturing meaningful internal representations, recent works such as REPA incorporate external pretrained encoders for representation alignment. However, the underlying mechanisms governing representation learning within DiTs remain poorly understood in the community. To this end, this paper first presents a systematic...
  </details>

- **2026-08-04** — Jingwei Zhao, Gus Xia, Ziyu Wang et al. — [Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping](http://arxiv.org/abs/2608.03050v1)
  <details><summary>📄 Abstract</summary>
  What is music style? Though often described using text labels such as "swing," "classical," or "emotional," the real style remains implicit and hidden in concrete music examples. In this paper, we introduce a cross-modal framework that learns implicit music styles from raw audio and applies them to symbolic music generation. Inspired by BLIP-2, our model leverages a Querying Transformer (Q-Former) to extract style representations from a large, pre-trained audio language model (LM), and further a...
  </details>

- **2026-08-04** — Yizhuo Jia, Jingyun Hua, Yuanxing Zhang — [CAPE-T2V: Captioner-Anchored Prompt Enhancement toward Two-Sided Conditioning Alignment in Text-to-Video Generation](http://arxiv.org/abs/2608.03046v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) diffusion transformers (DiTs) are trained with detailed video captions, whereas inference often relies on user prompts rewritten by a prompt enhancer (PE). Prior work has improved generation by optimizing the PE, the DiT, or both; some methods have also sought to narrow the training-inference mismatch through shared schemas. Yet even within a shared schema, inference-time PE outputs and DiT training captions may still differ in detail selection, information organization, desc...
  </details>

- **2026-08-04** — Seth Grief-Albert, Jessica Bo, Difan Jiao et al. — [Emulate or Estimate? The Divergent Strengths of Base and Post-Trained Language Models for Opinion Simulation](http://arxiv.org/abs/2608.03044v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate human opinions, but prior work reports conflicting results: some studies find promising alignment with human survey data, while others find persona collapse and weak demographic sensitivity. We show that much of this conflict stems from conflating two distinct tasks. We call the first task emulation, in which models generate individual responses that aggregate into a population distribution. We call the second task estimation, in which mode...
  </details>

- **2026-08-04** — Ruirui Zhang, Zhengkai Zhao, Pan Gao — [MultiCompose: Multi-Concept Personalized Composition with Per-Subject Attribute Binding](http://arxiv.org/abs/2608.03708v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models enable personalization of specific visual concepts from a small number of reference images. However, generating a single image that contains multiple personalized subjects, each bound to user-specified attributes such as clothing, accessories, and held objects, remains largely unaddressed. Without explicit spatial constraints, concurrently activated concept checkpoints produce overlapping cross-attention responses, causing per-subject identity degradation and attri...
  </details>

- **2026-08-04** — Yixin Bu, Runze Xia, Guanyun Zou et al. — [DUD: Decoupled Update Dynamics for Reliable Uncertainty Quantification in Large Language Models](http://arxiv.org/abs/2608.03411v1)
  <details><summary>📄 Abstract</summary>
  Accurate Uncertainty Quantification (UQ) is critical for reliable deployment of Large Language Models (LLMs), yet traditional probability-based metrics often fail to capture the model's true epistemic state. While recent mechanistic approaches leverage hidden state dynamics, they typically aggregate residual stream updates, conflating the distinct roles of parametric memory (Feed-Forward Networks) and contextual processing (Attention). We argue that this aggregation obscures fine-grained mechani...
  </details>

- **2026-08-03** — Kyeongbin Kim, Daniel McCarthy, Dokyun Lee — [Forecasting Revenue with its Customer-Base Drivers: When and Why Coordination Helps](http://arxiv.org/abs/2608.02911v1)
  <details><summary>📄 Abstract</summary>
  Revenue forecasts guide acquisition budgets, demand planning, and customer-based valuations, yet an aggregate forecast does not show whether change reflects acquisition, repeat purchasing, spending per order, or offsetting movements. Using weekly transaction panels for 966 companies in 25 industries, the authors develop the Customer-Based Multi-task Transformer (CBMT), which learns shared structure, retains separate primitive forecasts, and aligns their combination with downstream revenue. CBMT'...
  </details>

- **2026-08-03** — Nina Bodelot, Soufiane Belharbi, Eric Granger — [Test Time Adaptation Methods for Point Cloud Registration in Laparoscopic Surgery](http://arxiv.org/abs/2608.02883v1)
  <details><summary>📄 Abstract</summary>
  3D point cloud registration in laparoscopic surgery estimates the transformation between an intraoperative organ reconstructed from video and its preoperative mesh. Because ground-truth transformations are unavailable for real data, supervised networks are trained on synthetic organ pairs. At test time, real reconstructions differ from synthetic data and are noisy, sparse, and occluded, which degrades correspondence estimation. Test-time adaptation (TTA) can reduce this domain shift, but existin...
  </details>

- **2026-08-03** — Dayi Yao, Zijie Zhou — [Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling](http://arxiv.org/abs/2608.02244v1)
  <details><summary>📄 Abstract</summary>
  This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another. Because the wall-clock cost of a batch step is largely governed by the largest active KV-cache footprint, a short request co-batched with a long request can experience latency and GPU-resource consumption disproportionate to its own token workload. We formalize this phenomenon as a resource-fair...
  </details>

- **2026-08-03** — Jiajia Song, Bobo Li, Haiwen Yi et al. — [From Profiling to Synthesis: Benchmarking Implicit Behavioral Alignment in Personalized LLM Agents](http://arxiv.org/abs/2608.02171v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have enabled increasingly capable autonomous agents, yet personalization remains critical for making such agents practically useful. Recent benchmarks have begun evaluating personalization in agents, but they largely rely on static preference snapshots, fixed interaction logs, or question answering over predefined user profiles. Such designs fail to capture the complexity of evolving user preferences and neglect preference-conditioned task execution-a discrepancy we term as...
  </details>

- **2026-08-03** — Hongzhan Chen, Xiaoyu Liu, Dengming Zhang et al. — [Cross-Domain Hybrid OPD for Generalizable Search Agents](http://arxiv.org/abs/2608.02101v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Reinforcement Learning (RL) have substantially improved the capabilities of autonomous search agents, enabling sophisticated planning, and iterative retrieval over dynamic information sources. However, optimizing language models for specialized search behaviors often incurs an alignment tax, where gains in search performance come at the expense of general-purpose capabilities, limiting their effectiveness as universal assistants. In this technical report, we present the traini...
  </details>

- **2026-08-03** — Wei Jia, Zhicong Lu, Yu Chen et al. — [CAVE: Competence-Aware Visual Boundary Evidence Alignment for Video Temporal Grounding](http://arxiv.org/abs/2608.02078v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved substantial performance gains in Video Temporal Grounding (VTG) through reinforcement learning (RL). However, existing methods primarily rely on outcome correctness rewards that evaluate only the final predicted intervals, leaving boundary-related visual evidence and its correspondence with timestamp predictions insufficiently constrained. In this paper, we delve into timestamp prediction and its underlying boundary-level visual evidence, showin...
  </details>

- **2026-08-03** — Zhu Chen, Dingkun Liu, Yuheng Chen et al. — [STEAM:ASpatio-TEmporal Alignment Mixture-of-Experts Model with Hierarchical Pre-training for EEG Decoding](http://arxiv.org/abs/2608.02070v1)
  <details><summary>📄 Abstract</summary>
  Brain-computer interfaces (BCIs) have been widely used in motor rehabilitation, disease diagnosis, and other neural engineering scenarios. However, conventional neural signal decoding algorithms often suffer from limited generalizability and high adaptation costs, motivating recent interest in BCI foundation models. Existing approaches still struggle to jointly achieve general transferability, accurate decoding, and efficient downstream adaptation. We present STEAM, a hierarchical transfer frame...
  </details>

- **2026-08-03** — Daeyoung Roh, Donghee Han — [HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents](http://arxiv.org/abs/2608.02009v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented search agents answer multi-hop questions by repeatedly issuing search queries and accumulating evidence. This creates a stopping problem: after the necessary evidence has appeared, further retrieval often adds cost, latency, and distracting context rather than useful information. We frame stopping as evidence coverage rather than generator confidence, and introduce HALT, a lightweight verification-aware policy that leaves the search agent unchanged. Given expected hop claims,...
  </details>

- **2026-08-03** — Valentin Gorgodian, Olivier Poirot, Alain Schmitt et al. — [Phylogeny.fr: the phylogenetic platform designed for non-specialists](http://arxiv.org/abs/2608.01960v1)
  <details><summary>📄 Abstract</summary>
  Phylogenetic analysis has become a standard approach across many areas of biology, yet the growing complexity of phylogenetic methods and software remains a major obstacle for non-specialists. Since its launch in 2008, Phylogeny.fr has provided an accessible web platform for building phylogenetic trees using widely accepted methods without requiring local software installation. Here, we present a major redesign and modernization of the service. The new version integrates state-of-the-art tools w...
  </details>

- **2026-08-03** — Cheng-Yao Hong, Ting-Wei Lin, Yun-Chung Lai et al. — [Event ActivityNet: A Large-Scale Simulated-Event Benchmark for Untrimmed Action Understanding](http://arxiv.org/abs/2608.01948v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon event-based action understanding remains underexplored because existing datasets largely comprise short, trimmed clips, while collecting native event streams with dense temporal annotations is costly. We introduce Event ActivityNet, a large-scale simulated-event benchmark derived from human-annotated, untrimmed ActivityNet videos. It comprises 3,263 videos, 200 action classes, and 106.94 hours, with matched 5-bin and 9-bin event-voxel representations, temporal action annotations, an...
  </details>

- **2026-08-03** — Jeonghyeok Do, Munchurl Kim — [GeoCore-9B: Towards Geo-Aware Generative Foundation Models in Earth Observation](http://arxiv.org/abs/2608.01896v1)
  <details><summary>📄 Abstract</summary>
  Existing generative models for earth observation (EO) predominantly rely on fine-tuning natural image priors, which limits their scalability and introduces perspective biases that conflict with geospatial constraints. To address this, we introduce GeoCore-9B, a 9-billion-parameter generative foundation model, which is the first of its scale to be trained from scratch exclusively on EO data. Unlike previous EO foundation models, GeoCore-9B is built upon a Flow Matching-based Diffusion Transformer...
  </details>

- **2026-08-03** — Zijian Shen, Taijie Chen, Bin Zhou et al. — [LAB-Tab: LLM-Augmented Bayesian Network Adaptation for Few-Shot Tabular Generation](http://arxiv.org/abs/2608.01879v1)
  <details><summary>📄 Abstract</summary>
  Tabular data generation supports analysis and decision-making when target-domain data are scarce, yet collecting complete target samples is often costly. A practical but underexplored setting provides only a few target records together with richer source data from a related domain. Existing few-shot tabular generators often either fit sparse target statistics directly, which can overfit incidental patterns, or reuse source-domain generators, which may preserve dependencies that no longer hold in...
  </details>

- **2026-08-03** — Juntong Wang, Shengkun Yang, Xiyuan Wang et al. — [Rewriting or Reweighting? A Geometric Account in Language Models](http://arxiv.org/abs/2608.01835v1)
  <details><summary>📄 Abstract</summary>
  Post-training can substantially alter language-model behavior, yet aggregate behavior rates do not reveal whether training removes an existing mechanism, creates a new one, or changes how an inherited mechanism is used. We study this question through two mechanistically distinct failures, repetition as a decoding-attractor pathology and sycophancy as a preference-related alignment failure. We introduce behavioral manifold analysis, which isolates behavior-specific geometry by selecting sparse be...
  </details>

- **2026-08-03** — YuFei Luo, Xiucheng Xu, Zhen Yang — [MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents](http://arxiv.org/abs/2608.01742v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory is critical for LLM agents operating over long-horizon interactions. However, several persistent limitations of existing memory systems can be traced to two recurring misalignment patterns in long-term interaction settings: Temporal-Structural Misalignment (TSM) and Delayed Utility Manifestation (DUM). TSM arises when temporal proximity does not reliably align with topical or event-level relatedness, whereas DUM arises when write-time salience does not reliably predict future qu...
  </details>

- **2026-08-03** — Lingbo Li, Anuradha Mathrani, Teo Susnjak — [Constructing Executable Analytical Knowledge Representations for Meta-Analysis Synthesis Using an Agentic Harness](http://arxiv.org/abs/2608.01711v1)
  <details><summary>📄 Abstract</summary>
  Meta-analysis synthesis highlights a fundamental challenge in knowledge-based scientific analysis: structured evidence does not by itself represent the analytical knowledge required for executable computation. Decisions about evidence assignment, analytical contrasts, outcome and time-point alignment, effect-size formulation, and methodological admissibility must be explicit before statistical execution. Existing automated approaches often embed these decisions in model outputs, generated code, ...
  </details>

- **2026-08-03** — Yu Chen, Xiaohong Li, Xiaole Wang et al. — [CRAFT: Compression via Recursive Adaptive Fusion of Video Tokens for Vision-Language Models](http://arxiv.org/abs/2608.01644v1)
  <details><summary>📄 Abstract</summary>
  In video understanding, vision-language models (VLMs) must ingest massive numbers of visual tokens, causing the computational and memory cost of the prefill stage to rise sharply. Such visual sequences are highly redundant along the spatio-temporal dimension, yet a high compression ratio is often accompanied by the loss of critical details. Existing token-compression methods either employ heuristic, training-free compression with limited content adaptivity or introduce additional modules that re...
  </details>

- **2026-08-03** — Sota Nakashima, Yuta Ishimoto, Masanari Kondo et al. — [How Well Do LLMs Generate Taxonomies in the SE Domain? A Multi-perspective Evaluation Framework](http://arxiv.org/abs/2608.01592v1)
  <details><summary>📄 Abstract</summary>
  Taxonomies provide a shared conceptual framework for organizing heterogeneous observations in software engineering (SE) research. Manually constructing such taxonomies is labor-intensive and requires annotators with expertise in the SE domain. While advances in Large Language Models (LLMs) have led to the emergence of automated taxonomy generation methods outside the SE domain, their applicability to technically complex SE artifacts remains unclear. In this experience paper, we present the first...
  </details>

- **2026-08-03** — Tyler Ashoff, Jordan Rodu — [Semantic Alignment of AI Models: Concept Collapse, Checkpoint Dynamics, and Cross-Lingual Transfer](http://arxiv.org/abs/2608.01585v1)
  <details><summary>📄 Abstract</summary>
  Language model benchmarking is a difficult task. Outcome reasoning alone does not test the model's conceptualization of language and popular open-source benchmarks are quickly saturated or ingested as training data. It is important to test the model's output, but augmenting these tests by characterizing semantic structure gives more insight to how models relate abstract concepts. However, the high dimensional embedding spaces are not easy to interpret. This work demonstrates how topological meth...
  </details>

- **2026-08-03** — Liheng Ma, Rui Heng Yang, Zhanguang Zhang et al. — [Faster-WAM: Do World Action Models Need Deep Action Modules?](http://arxiv.org/abs/2608.02365v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) couple robot action prediction with video world models. Existing WAMs with shared-backbone and Mixture-of-Transformers designs generally tie the depth of the action module to that of the video backbone, resulting in substantial computational overhead and high inference latency. To address this limitation, we introduce Dock of Transformer (DoT), a video-centric design principle that treats a pretrained video Transformer as a representation hub and connects lightweight o...
  </details>

- **2026-08-03** — Naho Orita, Hayato Ogawa, Daisuke Kawahara — [Human-LLM Alignment in Language Attitudes Toward Non-Native Japanese](http://arxiv.org/abs/2608.01629v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly evaluate human writing in high-stakes domains such as hiring and academic assessment, putting non-native speakers at particular risk. Drawing on the language attitudes framework, we compared human and LLM evaluations of parallel L1- and L2-written Japanese emails on three dimensions: fluency, status, and solidarity. Japanese raters rated L2 texts significantly lower on all three dimensions, with a fluency gap roughly twice the size of the status and soli...
  </details>

- **2026-08-02** — Tianzhu Zhang, Changgang Zheng, Shanshan Wang et al. — [From Network Automation to Trustworthy Autonomous Networking in the LLM Era: A Network Control Intelligence Perspective](http://arxiv.org/abs/2608.01538v1)
  <details><summary>📄 Abstract</summary>
  Since the inception of modern communication networks, the quest for operations automation has never ceased. Yet the evolution of network automation is difficult to characterize with a single maturity ladder. Throughout this history, network control systems have expanded their capabilities for observation, decision support, routine execution, and operator interaction, but these capabilities have not advanced uniformly. Such uneven progress makes the degree of automation an unreliable proxy for tr...
  </details>

- **2026-08-02** — Guiqiu Liao, Matjaz Jogan, Daniel A. Hashimoto — [Slot2Text: Object-Centric Visual Tokenization for Efficient and Spatially Traceable Surgical MLLMs](http://arxiv.org/abs/2608.01473v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLM) for surgical scene understanding typically inject hundreds of dense visual tokens into a language model, leading to costly inference and limited spatial traceability for generated answers. We present Slot2Text, a dual-mode surgical MLLM that replaces dense representations of visual input with a compact set of regions encoded as slot latents. Instead of relying on contrastive alignment of the visual encoder with language, Slot2Text groups self-supervised vi...
  </details>

- **2026-08-02** — Priyanka Dey, Brihi Joshi, Preyashi Poddar et al. — [PALMs: Using Multi Construct-Grounded Rationales for Modeling Population Preferences in LLMs](http://arxiv.org/abs/2608.01458v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being extensively used to simulate individual user behavior, yet faithfully representing a population requires capturing the systematic variation in values, beliefs, and cultural norms that distinguish one group from another. We introduce Population Aligned Language Models (PALMs), a suite of models each aligned to specific populations, covering five countries: USA, India, Brazil, France and Italy. PALMs are created by synthesizing rationales grounded in psychological a...
  </details>

- **2026-08-02** — Taher A. Ghaleb — [Doc2CI: A Multi-Service Study of CI Configuration Generation Using Large Language Models](http://arxiv.org/abs/2608.01451v1)
  <details><summary>📄 Abstract</summary>
  Adopting Continuous Integration (CI) often requires writing YAML configurations that are error-prone and challenging to maintain. Despite increasing LLM use in software engineering, their ability to generate CI configurations from natural language across services and model families remains unclear. This paper presents a large empirical study on using LLMs to generate CI configurations. We introduce DOC2CI, a benchmark of 3,363 description-to-YAML pairs collected from the official documentation o...
  </details>

- **2026-08-02** — Shengwei Xu, Yuxuan Lu, Yifan Wu et al. — [Scoring Rules! Statistical and Strategic Alignment for Text Evaluation Metrics](http://arxiv.org/abs/2608.01423v1)
  <details><summary>📄 Abstract</summary>
  Reference-based text evaluation metrics, which are widely used to assess natural language generation systems, score a candidate response by comparing it with a reference response. The reliability of an evaluation metric is usually judged by its statistical correlation with human ratings. However, as these metrics are increasingly used as optimization objectives, correlation alone is no longer sufficient: agents may strategically game the evaluation metric. We study this issue through two complem...
  </details>

- **2026-08-02** — Reza Asgharzadeh Jelodar, Kazem Bitaghsir Fadafan, Giacomo Cacciapaglia — [Impact of Higgs precision measurements at the LHC and FCC-ee on the spectrum of composite Higgs models](http://arxiv.org/abs/2608.01353v1)
  <details><summary>📄 Abstract</summary>
  We investigate the minimal composite Higgs model based on the symmetry-breaking pattern $\mathrm{SU}(4)\rightarrow\mathrm{Sp}(4)$, where electroweak symmetry breaking is governed by the vacuum alignment angle $θ$. Through the leading-order relations $κ_V=\cosθ$ and $m_η=m_h/\sinθ$, precision measurements of Higgs couplings are translated into direct constraints on the vacuum structure and the singlet pseudo-Nambu--Goldstone boson mass. Using the current ATLAS Run-2 measurement of $κ_V$, we const...
  </details>

- **2026-08-02** — Jianan Jiang, Bin Li — [PartInteractor: Intent-Driven Part-Aware 3D Authoring for Continuous Co-Creation in XR](http://arxiv.org/abs/2608.01335v1)
  <details><summary>📄 Abstract</summary>
  As Extended Reality (XR) evolves into an immersive computing medium, interactive 3D authoring becomes essential for creative and functional workflows. However, existing generative XR systems produce monolithic outputs lacking explicit semantic structure, limiting post-generation control. We introduce PartInteractor, a representation-to-interaction framework that investigates how semantic part hierarchies can be incorporated into generative XR authoring, and exposed as first-class, directly manip...
  </details>

- **2026-08-02** — Yibin Huang, Jixiang Hong, Zongzhao Li et al. — [SPAE: Spectrally Guided Autoencoder for Pretrained Visual Latents](http://arxiv.org/abs/2608.01306v1)
  <details><summary>📄 Abstract</summary>
  Latents from vision foundation models (VFMs) are semantically rich and well suited for visual understanding. Recent representation autoencoder methods such as RAE have shown that they can provide promising latent spaces for image generation. However, VFM latents remain difficult to model directly: DiT-generated latents exhibit spectral mismatch with encoder latents, especially in high-frequency components. Our channel-wise spectral analysis further reveals that these high-frequency components ar...
  </details>

- **2026-08-02** — Junno Yun, Yaşar Utku Alçalar, Mehmet Akçakaya — [UDT: Reconciling U-Nets and Diffusion Transformers with Data-Adaptive Token Reduction](http://arxiv.org/abs/2608.01298v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have emerged as a core architecture in generative modeling due to their scalability and adaptability to multimodal tasks. DiTs comprise isotropic transformer blocks, and learn representations progressively across depth, where the denoising objective drives later layers to focus on fine-detail reconstruction. This results in degraded representation quality and an imbalanced encoder-decoder behavior. Prior approaches such as representation alignment (REPA) mitigate th...
  </details>

- **2026-08-02** — Bruno Brocai, Ilaria Papagno, Mayumi Ohta — [PlainMedScale: A Corpus of Multi-Level Simplified Medical Texts in German and English](http://arxiv.org/abs/2608.01158v1)
  <details><summary>📄 Abstract</summary>
  We introduce PlainMedScale, a topic-aligned medical corpus spanning four levels of comprehensibility in German and English, drawn from MSD (professional and consumer), Gesund.Bund, Apotheken Umschau Einfache Sprache, and the NHS. The four tiers correspond to distinct communicative functions --- reference, explanation, decision support, and access --- and move beyond the binary expert--lay contrast of prior corpora. In two pilot studies enabled by the alignments, we show that many readability met...
  </details>

- **2026-08-02** — Junsheng Wang, Chao Chen, Mengying Xie et al. — [SG-Layout: Structured Scene Graph-Guided Layout Generation with LLMs](http://arxiv.org/abs/2608.01106v1)
  <details><summary>📄 Abstract</summary>
  Understanding and generating spatially coherent layouts from natural language remains a fundamental yet challenging task for large language models (LLMs). Existing LLMs often struggle to capture explicit geometric relationships and structural dependencies between objects. To address this issue, we propose SG-Layout, a graph-guided layout generation framework that explicitly incorporates structured spatial knowledge into LLMs. SG-Layout follows a two-stage training paradigm: (1) a graph-language ...
  </details>

- **2026-08-02** — Damir Nurtdinov, Alexei Kornaev, Alexander Maloletov — [RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment](http://arxiv.org/abs/2608.01013v1)
  <details><summary>📄 Abstract</summary>
  Adapting a pretrained vision-language-action (VLA) policy to a new robot usually assumes embodiment-specific demonstrations. This assumption is especially restrictive for custom robots whose morphology differs strongly from the manipulators seen in large robot datasets. We study a harder setting: zero-demo embodiment alignment of OpenVLA-OFT on a cable-driven parallel robot (CDPR) with a simple gripper and a previously unseen control interface. Instead of supervised fine-tuning, we use reinforce...
  </details>

- **2026-08-02** — Ofir Ben Shoham, Oriel Perets, Nir Grinberg et al. — [MedUPS: Towards Diagnostic Assistance in Uncommon Medical Cases with Large Language Models](http://arxiv.org/abs/2608.01012v1)
  <details><summary>📄 Abstract</summary>
  Uncommon and off-guideline cases are difficult for clinical decision support, because physicians must make a series of management decisions under diagnostic uncertainty and rarely see the full case at once. Most large language model (LLM) benchmarks for medicine score only the final diagnosis, yet much of clinical care turns on the next appropriate action: the next test to order, the imaging study to obtain, the specialist to involve, or the differential to pursue. We introduce MedUPSQA, a datas...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 83 papers

- **2026-08-04** — Michal Mráz, Justin Shenk — [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](http://arxiv.org/abs/2608.03892v1)
  <details><summary>📄 Abstract</summary>
  We study linear representations of temporal horizon in the large language model Qwen3-32B and use them to change the model's time-related preferences, recommendations, and capabilities. We train contrastive linear probes on teacher-forced temporal-choice answers to find a short-term versus long-term direction in the model's residual stream, and evaluate contrastive activation-addition steering on a held-out binary temporal-choice task, an out-of-distribution monetary intertemporal-choice task, a...
  </details>

- **2026-08-04** — Ruihan Li, Jiyang Tan, Kailin Jiang et al. — [KnowHal: A Knowledge-Driven Benchmark for Comprehensive Multimodal Hallucination Evaluation](http://arxiv.org/abs/2608.03782v1)
  <details><summary>📄 Abstract</summary>
  Hallucination remains a critical challenge for developing trustworthy Multimodal Large Language Models (MLLMs). While existing benchmarks mainly focus on entity, attribute, and relation hallucinations, knowledge-related failures are often investigated separately, lacking a unified evaluation framework across different hallucination dimensions. To overcome this, we propose \textbf{KnowHal}, a benchmark that explicitly incorporates knowledge hallucination into multimodal hallucination evaluation s...
  </details>

- **2026-08-04** — Zizhao Hu, Nathan Elijah Segura, Mohammad Rostami et al. — [Should We Type or Talk to LLM Agents? A Comprehensive Study of Voice and Keyboard Input Perturbations](http://arxiv.org/abs/2608.03970v1)
  <details><summary>📄 Abstract</summary>
  Human input reaches language models by typing or speaking, and each channel leaves a distinct signature: orthographic noise for keyboards; for voice, disfluency from conventional transcription and restructuring from AI-backed dictation tools. How do they impact an LLM's performance? In this paper we present HIVE (Human Input-Variation Engine), a suite of voice transcription perturbations and QWERTY keyboard perturbations. We use HIVE to evaluate how robust models are to these perturbations. We p...
  </details>

- **2026-08-04** — Shuoqin Zhang, Tongtong Cheng, Xiru Gao et al. — [EvoHIL: Self-Evolving Reward and Flow-Matched Policy Optimization for Robust Human-in-the-Loop Reinforcement Learning](http://arxiv.org/abs/2608.03872v1)
  <details><summary>📄 Abstract</summary>
  Human-in-the-loop reinforcement learning (HIL-RL) enables robots to learn contact-rich manipulation from limited real-world interaction, but deployment exposes three coupled limitations: static visual reward models fail under scene changes; independently sampled actions cause temporally inconsistent motion; and vision-based policies remain sensitive to appearance shifts. We present EvoHIL, a unified framework that adapts the reward model, action generator, and visual do main within a staged huma...
  </details>

- **2026-08-04** — Tianbao Zhang, Zeyu Liu, Shuyu Wu et al. — [LiteMVS: Efficient Multi-View Stereo with Foundation Distillation and Expert Aggregation](http://arxiv.org/abs/2608.03851v1)
  <details><summary>📄 Abstract</summary>
  Real-time 3D perception is crucial for robotics, augmented reality, and embodied intelligence applications. Existing multi-view stereo (MVS) methods primarily rely on geometric correspondences, which often fail in textureless or repetitive regions, while monocular depth models leverage strong image-level priors but lack robust multi-view geometric constraints. More importantly, in robotics and embodied manipulation scenarios, high-quality 3D geometry is not only essential for static reconstructi...
  </details>

- **2026-08-04** — Peng Xia, Junbiao Pang, Zheng Huang — [Low-Dimensional High-Leverage Subspace Optimization: Beyond Full-Parameter Coupled Training for Neural Network Quantization](http://arxiv.org/abs/2608.03919v1)
  <details><summary>📄 Abstract</summary>
  Low-bit quantization suffers severe accuracy degradation on compact networks, rooted in the dominant full-parameter coupled training paradigm that ignores parameter subspace heterogeneity. Their limited feature redundancy leaves little room to absorb quantization errors. Conventional pipelines adopt monolithic optimization: PTQ reconstructs fixed pretrained models without improving inherent quantization friendliness; QAT updates all parameters jointly, suffering from gradient coupling between ba...
  </details>

- **2026-08-04** — Sadab Shiper, Tawsif Tashwar Dipto, Mir Md Inzamam et al. — [BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models](http://arxiv.org/abs/2608.03884v1)
  <details><summary>📄 Abstract</summary>
  In-the-wild Bengali scene text recognition is largely unmeasured: existing resources target handwritten documents or constrained sign-board parsing, report only aggregate edit-distance metrics, and evaluate either conventional OCR or VLMs, never both on the same in-the-wild data. To address this gap, we introduce BANGLAWILD, a benchmark of 2,535 Bengali scene text images, each paired with a verbatim gold transcription, two categorical axes, four diagnostic attributes, and an orthographically sta...
  </details>

- **2026-08-04** — Tianyi Guan, Yiding Wang, Haotong Yang et al. — [ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?](http://arxiv.org/abs/2608.03874v1)
  <details><summary>📄 Abstract</summary>
  Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficult...
  </details>

- **2026-08-04** — David Chamizo, Jose Garcia-Alonso, Juan M. Murillo — [High-level quantum structured programs as quantum registers compositions](http://arxiv.org/abs/2608.03873v1)
  <details><summary>📄 Abstract</summary>
  Current quantum programs are mainly designed at the level of quantum gates acting on individual qubits; on a large scale and for complex problems this may involve a high cognitive load on the programmer, making the program specification nontrivial and error-prone. In this context, providing quantum programming with higher abstraction mechanisms will assist in making this task more manageable and robust against design errors. In this work, a conceptual framework is addressed following the notion ...
  </details>

- **2026-08-04** — David Ming Segura, Jeremy Goumaz, Joshua W. Sin et al. — [Bi-semantic Chemical Embedder for Joint Representation Learning of SMILES and Natural Language](http://arxiv.org/abs/2608.03855v1)
  <details><summary>📄 Abstract</summary>
  Transformer models have revolutionized natural language processing (NLP), and text-based molecular representations like SMILES have successfully extended these architectures to chemistry. However, domain-adaptive pre-training often causes models to overfit to chemical syntax, catastrophically forgetting their foundational semantic capabilities. To address this challenge, we introduce CheMatE, a chemistry-oriented embedding model that jointly captures molecular structure and domain-specific natur...
  </details>

- **2026-08-04** — Ulrich Hounyo — [Identification and Information after Nuisance Projection](http://arxiv.org/abs/2608.03847v1)
  <details><summary>📄 Abstract</summary>
  Empirical work often removes fixed effects, latent factors, or high-dimensional controls before estimating structural relationships. These transformations reduce confounding but may also remove identifying variation. We study linear panel IV after one equation-compatible nuisance projection under two-way dependence. The projected Jacobian determines which structural directions remain visible; the projected-score law determines their precision; and, on Gaussian fixed-rank strata, they combine in ...
  </details>

- **2026-08-04** — Joanna Matulewicz, Renata Ratajczak, Ewa Grzanka et al. — [From phase transformation to amorphization: damage accumulation in Yb-implanted \b{eta}-Ga2O3](http://arxiv.org/abs/2608.03798v1)
  <details><summary>📄 Abstract</summary>
  This study provides a comprehensive analysis of the radiation response and structural evolution of differently oriented $β$-Ga$_{2}$O$_{3}$ single crystals subjected to Yb ion implantation over a wide fluence range from $5 \times 10^{12}$ to $1 \times 10^{16}$~cm$^{-2}$ ($0.04$--$74$~dpa). A multi-technique approach (RBS/c, PAS, HRTEM, and HRXRD) was employed to investigate the mechanisms of damage accumulation. The results reveal a multi-stage process of defect evolution. At a critical threshol...
  </details>

- **2026-08-04** — Chunyang Jiang, Pingping Zhang, Yuzhi Zhao et al. — [Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement](http://arxiv.org/abs/2608.03733v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved remarkable performance across vision-language tasks, but their progress depends heavily on large-scale, high-quality multimodal data that are costly to annotate. Self-augmentation offers a promising alternative by enabling models to expand their own training data without external supervision. However, existing MLLM self-augmentation methods are largely text-centric, while image augmentation remains underexplored and typically relies on gener...
  </details>

- **2026-08-04** — Maximilian Dillitzer, Tin Stribor Sohn, Jason J. Corso et al. — [Attention is Case-Sensitive](http://arxiv.org/abs/2608.03711v1)
  <details><summary>📄 Abstract</summary>
  In human visual perception, uppercase lettering serves as a natural salience cue that captures attention within lowercase text. In this paper, we present a systematic empirical characterization study revealing that Large Language Models (LLMs) exhibit an analogous property: letter casing modulates internal attention allocation. Through analysis across 13 models, nine LLMs and four Vision-Language Models (VLMs), with diverse tokenization schemes, we show that formatting target information in alte...
  </details>

- **2026-08-04** — Corrado Priami — [GenOS: Compositional Certificates for Semantic Robustness in AI Code Generation](http://arxiv.org/abs/2608.03588v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are stochastic workflows: prompts are interpreted, artifacts are sampled, validators produce observations, and orchestrators commit or repair. Small prompt or specification changes can therefore alter program-behavior distributions even when the texts appear synonymous. Existing systems evaluate correctness, but lack a compositional criterion for safely replacing a prompt, contract, generator, or program inside a complete agentic workflow. We introduce GenOS, a probabilistic ope...
  </details>

- **2026-08-04** — Shahbaz Siddeeq, Muhammad Waseem, Umar Subhan Malhi et al. — [CodeAssay: A Multi-Metric Benchmark with Audited Ground Truth for LLM Code Generation](http://arxiv.org/abs/2608.03535v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are increasingly evaluated for code generation using test-based benchmarks. The validity of such evaluations depends on the reliability of their references and tests, while test-based correctness captures only part of the observable properties of generated code. We present CodeAssay, a taxonomy-first benchmark of 185 Python tasks across ten software-engineering categories. It combines audited ground truth, public tests for generation and repair, hidden tests for grading, mu...
  </details>

- **2026-08-04** — Basit Alawode, Moshira Ali Abdalla, Dwarikanath Mahapatra et al. — [From Multi-Resolution Cells to Gigapixel Whole Slide Images Foundation Model for Computational Pathology](http://arxiv.org/abs/2608.03508v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) and their hierarchical variants have achieved strong performance in Computational Pathology (CPath). However, most are pre-trained on single-resolution Whole Slide Images (WSIs), limiting their generalization across arbitrary resolutions. Gigapixel WSIs inherently contain diagnostic patterns at multiple scales, including cellular morphologies, tissue architectures, and global context, mirroring how expert pathologists examine WSIs. We introduce Multi-Resolution Pyramid...
  </details>

- **2026-08-04** — Xiuhui You, Jiayi Luo, Zichao Shen et al. — [ToolLIFT: Lifting Tool-Specific Trajectories into Function-Level Graphs for Generalizable Tool Planning](http://arxiv.org/abs/2608.03468v1)
  <details><summary>📄 Abstract</summary>
  Historical tool-use trajectories provide valuable experience for large language model (LLM) agents to plan and coordinate tool usage. Existing approaches directly construct tool-level graphs from these trajectories, but the resulting graphs remain tied to specific tools and are hard to generalize across tool sets. To tackle this challenge, we find that despite differences in the tools involved, analogous tasks often share a common function-level workflow structure, which serves as a potentially ...
  </details>

- **2026-08-04** — Hao Zhou, Haichuan Hu, Ye Shang et al. — [Self-Evolving Coding Agents](http://arxiv.org/abs/2608.03392v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly embedded in software engineering workflows as coding agents that can inspect repositories, invoke tools, execute tests, debug failures, and generate patches. Yet most existing agents remain largely static after deployment, even though software development is a dynamic, feedback-rich process in which repositories evolve, dependencies change, tests fail, and repair attempts leave reusable experience. This tension has motivated a growing body of work on self-e...
  </details>

- **2026-08-04** — Erxue Zhou, Jingxiang Meng, Aofan Liu — [Route-Align-Verify for Functional Correctness in Code Generation](http://arxiv.org/abs/2608.03341v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have substantially improved code generation, yet achieving strong functional correctness remains difficult, especially for heterogeneous programming tasks where a single prompting strategy and a single directly generated output are often insufficient. In this paper, we present RAV, a lightweight and modular framework that improves code generation with a fixed backbone model through three coordinated stages: Route, which applies task-aware prompt routing before genera...
  </details>

- **2026-08-04** — Yue Yao — [Long-term Traffic Scene Prediction via Polynomial Representations in Autonomous Driving](http://arxiv.org/abs/2608.03330v1)
  <details><summary>📄 Abstract</summary>
  This thesis addresses fundamental challenges in traffic scene prediction for autonomous driving by introducing robust and computationally efficient models based on polynomial representations. While conventional sequence-based representations often struggle with noise and generalization, this work demonstrates that polynomial representations offer significant advantages in computational efficiency, generalization, and prediction plausibility. Through theoretical analysis and empirical validation,...
  </details>

- **2026-08-04** — Chengyu Wu, Junpeng Tan, Wanxiang Luo et al. — [Open-Linguistic Concept Unified Learning for Cross-Site Interpretable Dermatology Image Diagnosis](http://arxiv.org/abs/2608.03225v1)
  <details><summary>📄 Abstract</summary>
  Human-interpretable computer-aided diagnosis is crucial for clinical decision making. Concept-based models excel by providing transparent reasoning and enabling post-hoc, clinician-in-the-loop interventions. However, their rigid dataset-specific adaptation inherently restricts cross-site generalization. Applying them across diverse modalities, such as dermoscopic and clinical photographs, is challenging due to heterogeneous concept taxonomies varying in availability, granularity, and semantics a...
  </details>

- **2026-08-04** — Ankur Sharma, Deep Shah — [The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems](http://arxiv.org/abs/2608.03214v1)
  <details><summary>📄 Abstract</summary>
  Large language models have transformed artificial intelligence from isolated prediction services into components of long-running, distributed systems that reason, invoke tools, retrieve external state, delegate tasks, and act on behalf of users and organizations. The surrounding ecosystem has responded with agent frameworks, workflow engines, model-serving platforms, memory systems, communication protocols, and observability tools. These technologies improve execution, but they do not provide a ...
  </details>

- **2026-08-04** — Ethan Bito, Yongli Ren, Estrid He — [Position Bias Undermines Preference Consistency in Listwise LLM-Based Reranking](http://arxiv.org/abs/2608.03091v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have emerged as promising listwise rerankers for recommender systems, but their reliability under equivalent candidate permutations remains unclear. Since recommendation candidates form an unordered set, a reranker should not depend on the arbitrary order used to serialize them. However, decoder-only LLM rerankers can allow input order to affect model scores, pairwise preferences, and rankings. We study how position bias affects the ranking process induced by LLM-bas...
  </details>

- **2026-08-04** — Wanqi Liu, Rong Zhao, Zhizhou Sha et al. — [Mapping the City Through the Lens of Language Models](http://arxiv.org/abs/2608.02971v1)
  <details><summary>📄 Abstract</summary>
  Language models often complete an underspecified reference to a city with unstated assumptions about urban size, form, infrastructure, environment, and function. We measure those assumptions without naming places. Ten open-weight checkpoints rate anonymized profiles derived from real morphological urban centres across 40 audited indicators and seven domains. The design combines constrained probability-based ratings, prespecified reliability screens, lineage-aware aggregation, multiple population...
  </details>

- **2026-08-04** — Chenfei Yan, Zeyang Yue, Feifei Zhao et al. — [When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems](http://arxiv.org/abs/2608.03421v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems promise effective collaborative reasoning, but communication may amplify local errors into collective risks. Existing evaluations emphasize final outcomes, leaving the reliability and propagation dynamics of distributed information aggregation unclear. We introduce Hi-Agreement, a controlled evaluation framework that strictly pairs all-honest collaboration with controlled deception by a key evidence holder and analyzes the aggregation process through multi-stage vot...
  </details>

- **2026-08-04** — Shuliang He, Shuai Wang, Bo Yue et al. — [RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation](http://arxiv.org/abs/2608.03387v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations, but transferring such imagined behaviors into executable whole-body humanoid skills remains largely unexplored. In this work, w...
  </details>

- **2026-08-04** — Khai-Nguyen Nguyen, Oscar Chaparro, Antonio Mastropaolo — [Pattern over Pixels: Measuring Pattern Completion Bias in Multimodal Code Generation](http://arxiv.org/abs/2608.03691v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are increasingly used to translate webpage screenshots into front-end code, but repeated UI patterns may sway them toward visually incorrect yet pattern-consistent outputs. In this work, we test how repeated webpage patterns hurt MLLM accuracy on an objective screenshot-to-code fill-in-the-blank task. We introduce the first benchmark for visual pattern-completion bias, where one localized element in a repeated UI pattern is perturbed and the model must re...
  </details>

- **2026-08-04** — Edoardo Coppola, Stefano Fiorini, Pietro Liò et al. — [LAEF: A Lead-Agnostic ECG Foundation Model Towards Point-of-Care Diagnostics](http://arxiv.org/abs/2608.03690v1)
  <details><summary>📄 Abstract</summary>
  Point-of-care cardiac devices such as smartwatches and handheld ECG recorders typically capture 1--2 leads, yet existing ECG foundation models are architecturally constrained to fixed 12-lead inputs, degrading or failing under these reduced configurations. We introduce LAEF (Lead-Agnostic ECG Foundation), a 7M-parameter ECG foundation model that can natively process any lead subset without zero-padding or architectural modification. LAEF represents ECGs as variable-size spatiotemporal graphs wit...
  </details>

- **2026-08-04** — Maksymilian Wolski, Nicholas Hoernle, Johannes Forkel et al. — [Is Inter-Seed Cross-Play Enough? Evaluating the Robustness of Zero-Shot Coordination Algorithms to Implementation Details](http://arxiv.org/abs/2608.03644v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed in real-world settings must be capable of coordinating with humans and other AI agents they have not encountered before. Zero-shot coordination (ZSC) algorithms aim to achieve this by specifying high-level learning rules such that independently engineered agents can coordinate with each other at test time. Rigorous evaluation of ZSC algorithms remains difficult: ideally, multiple independent implementations of each proposed algorithm must be used, reflecting the variation that...
  </details>

- **2026-08-04** — Saba Tabatabaee, Jing Liu, Megh Krishnaswamy et al. — [Speaker Verification Under Real Classroom Conditions for English Speech](http://arxiv.org/abs/2608.03623v1)
  <details><summary>📄 Abstract</summary>
  Developing speaker verification (SV) models that are robust to classroom noise and effective across both children and adult speakers is critical for AI tools supporting educational environments. In this study, we use a real-world English-speaking classrooms dataset containing partial speaker identity annotations, with most recordings remaining unlabeled. We adapt the WavLM-TDNN model for classroom SV, achieving average relative reductions in Equal Error Rate (EER) of 23.99% and 6.32% compared to...
  </details>

- **2026-08-04** — Mykola Haltiuk — [Disentangling Language Modeling and Boundaries](http://arxiv.org/abs/2608.03599v1)
  <details><summary>📄 Abstract</summary>
  Byte-level language models are usually argued for on the grounds of robustness, multilingual fairness, and character-level skills. We point to a different, structural advantage: because they read and write bytes, any two of them share an output space, so knowledge transfer between them is exact and independent of how either was originally tokenized. We hypothesize that the two distributions a byte-level model produces, one over the next byte, one over where its patch boundaries fall, can be dise...
  </details>

- **2026-08-04** — Haowen Yang, Yun Peng, Zishuo Ding — [EffiHolmes: Differential Profiling-Guided Repository Level Time Inefficiency Fix Localization](http://arxiv.org/abs/2608.03558v1)
  <details><summary>📄 Abstract</summary>
  Large software systems often suffer from time inefficiencies that cause excessive execution time despite functional correctness. Localizing their fix locations is difficult because, unlike functional bugs, they produce neither test failures nor stack-trace clues, making traditional and recent LLM-based fault localization methods unsuitable. Runtime profiling provides alternative evidence but faces three challenges in repository-level settings: single-run profiling cannot reliably distinguish ine...
  </details>

- **2026-08-04** — Malena Loza, Felipe Grijalva, Eva Milara et al. — [Test-Time Augmentation for Tabular-to-Image Classifiers under Distribution Shifts](http://arxiv.org/abs/2608.03557v1)
  <details><summary>📄 Abstract</summary>
  Tabular-to-image methods that convert tabular data into visual representations have emerged as a novel paradigm for leveraging the high performance of deep learning models. Despite their advantages, the robustness of these methods under distribution shifts remains under explored. Test-Time Augmentation (TTA) is an effective approach in image classification to improve model generalization and robustness, where predictions over multiple transformed views of each input are aggregated. This work eva...
  </details>

- **2026-08-04** —  Sanayya, Rakshith Sathish, Ashwathi Nambiar — [Distilled Roads: Generalisable Road Network Extraction Across Sensors, Resolutions, and Region](http://arxiv.org/abs/2608.03407v1)
  <details><summary>📄 Abstract</summary>
  Road network segmentation from satellite imagery remains challenging due to large geographic variation in road appearance, occlusions, and domain shifts introduced by differing resolutions and sensors. Existing models, typically trained under narrow resolution--region combinations, generalise poorly to unseen environments such as rural settings, regions with distinct road materials, or imagery from new satellite platforms, often producing broken or disconnected predictions. Adapting these models...
  </details>

- **2026-08-04** — Can Wang, Haoran Chen, Li Yu et al. — [Towards Robust Tool Use in Agents via Experience-Driven Adaptive Guidance](http://arxiv.org/abs/2608.03403v1)
  <details><summary>📄 Abstract</summary>
  The performance bottleneck of agents is increasingly shifting from model capability to the robustness of their execution processes. Tools play a central role as the primary interface through which agents interact with external environments, yet existing methods rarely focus on ensuring robust tool use across diverse runtime conditions. To address this problem, we propose ExpG, a mechanism that builds and refines adaptive guidance capturing each tool's capability boundaries and best practices, th...
  </details>

- **2026-08-04** — Shufan Ming, Yikun Han, Gibong Hong et al. — [ANCHOR-RE: An Agentic Neuro-Symbolic Framework for Grounded Biomedical Relation Extraction](http://arxiv.org/abs/2608.03154v1)
  <details><summary>📄 Abstract</summary>
  Biomedical relation extraction (BioRE) extracts structured knowledge from biomedical literature for applications such as knowledge base construction and hypothesis generation. Traditional symbolic systems such as SemRep provide high precision but limited recall, while large language models (LLMs) offer stronger contextual reasoning but remain prone to false-positive predictions. We developed ANCHOR-RE, a framework that integrates ontology-guided reasoning, external knowledge grounding, and data-...
  </details>

- **2026-08-04** — Qinglong Hu, Qingfu Zhang, Fei Liu et al. — [Beyond Average Performance: Dynamic Instance Clustering and Specialized Algorithm Design in LLM-Assisted Evolutionary Search](http://arxiv.org/abs/2608.03129v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model-assisted Evolutionary Search (LES) has emerged as a powerful paradigm for automated algorithm design. However, existing LES methods primarily optimize for average performance, inherently directing search effort toward instances that contribute most to this metric while leaving others poorly served, resulting in weak tail robustness and limited real-world reliability. To address this limitation, we propose Dynamic Instance Clustering and Specialized Algorithm Design (DyCA), a...
  </details>

- **2026-08-04** — Jiakai Lin, Zijun Li, Guoyu Lu — [Multimodal Plant Root Phenotyping with Integration of 3D Skeleton Extraction and Language Analysis](http://arxiv.org/abs/2608.03109v1)
  <details><summary>📄 Abstract</summary>
  Plant root phenotyping is fundamental to understanding below-ground structures, optimizing crop management, and improving agricultural sustainability. This paper presents a multimodal robotic AI framework that integrates 3D skeleton extraction with language-guided reasoning for interpretable and data-efficient root analysis. We develop an unsupervised skeleton extraction network based on Weighted Laplacian Contraction (W-LBC) to generate high-fidelity structural representations from dense point ...
  </details>

- **2026-08-04** — Ziqi Jia, Yalu Ouyang, Bo Pang et al. — [CVPO: Enhancing LLM Reinforcement Learning Reasoning via Value-Variance Adaptation and Dynamic Curriculum Learning](http://arxiv.org/abs/2608.03068v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has emerged as an effective method for enhancing the reasoning capabilities of large language models (LLMs). However, existing methods suffer from insufficient precision in feedback on generated answer trajectories and exhibit the phenomenon of problem difficulty drift. To address these challenges, we propose CVPO - Curriculum-guided Value-Variance Policy Optimization. At the response trajectory level, we find that token-level value-variance correlates with exploratio...
  </details>

- **2026-08-04** — Shuai Shao, Dingbang Wang, Yiming Zeng et al. — [ConFL: Explainable Concurrent Fault Localization via Hierarchy-Guided LLM Reasoning](http://arxiv.org/abs/2608.02974v1)
  <details><summary>📄 Abstract</summary>
  Localizing concurrent bugs from bug reports alone is challenging due to incomplete information, misleading program-entity mentions, and complex cross-thread interactions, causing existing LLM-based approaches to suffer from unstable reasoning and limited explainability. We propose ConFL, an explainable concurrent fault localization framework that augments LLM reasoning with structured concurrency knowledge. ConFL constructs a Concurrent Knowledge Base (CKB) from source code and performs LLM-guid...
  </details>

- **2026-08-03** — Fengxian Ji, Yuke Li, Jingpu Yang et al. — [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation](http://arxiv.org/abs/2608.01666v2)
  <details><summary>📄 Abstract</summary>
  However, whether these judges truly evaluate the scientific substance of ideas or are influenced by superficial stylistic presentation remains an open question. To address this question, we propose SciStyleBench, a unified three-component benchmark for diagnosing and mitigating stylistic bias in LLM-based idea evaluation: (i) First, SciStyleStage, a three-stage evaluation environment that applies controlled stylistic perturbations to fixed scientific content across three settings no context, fix...
  </details>

- **2026-08-03** — Mohammad Rostami — [In-Context Collapse in Vision-Language Models and How to Mitigate it?](http://arxiv.org/abs/2608.02830v1)
  <details><summary>📄 Abstract</summary>
  Many-shot in-context learning (ICL) lets vision-language models (VLMs) adapt from image--label demonstrations without weight updates, and is widely assumed to improve as more demonstrations are supplied. We show the opposite: as demonstrations accumulate, a subset of VLMs undergo an \emph{in-context collapse}, a sharp, sometimes catastrophic accuracy drop spanning synthetic classification, natural-image classification, and VQA benchmarks, in some models falling below chance while outputs remain ...
  </details>

- **2026-08-03** — Yuxiang Peng, Xiaodi Wu — [Stateful Governance for Concurrent Agentic Systems](http://arxiv.org/abs/2608.02764v1)
  <details><summary>📄 Abstract</summary>
  AI agents are moving from advisory interfaces into systems that execute consequential operations: issuing refunds, reserving scarce inventory, provisioning cloud resources, and initiating financial transfers. These workflows require governance over effects, not only over model outputs. Existing safeguards often decide whether an action is allowed from the information available when the action is requested. For stateful policies, that request-time view may be incomplete: budgets, inventory, appro...
  </details>

- **2026-08-03** — Yue Yao, Shengyuan Wang, Xin Chen et al. — [SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents](http://arxiv.org/abs/2608.02356v2)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly solve complex tasks by composing reusable skills from a library. To address this, the key challenge is not merely to retrieve individually relevant skills, but to identify a complete and executable skill composition. In this paper, we argue that this problem can be solved in a graph with three levels: compositional relations among skill queries, similarity between queries and candidates in the skill library, and the dependencies among the selected candida...
  </details>

- **2026-08-03** — Saman Sarker Joy, Niloy Farhan — [MedPRESS: A Multi-turn Benchmark for Patient-Pressure-Induced Medical Sycophancy in LLMs](http://arxiv.org/abs/2608.02520v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for health-related advice. Existing research measures their safety with static questions rather than pressured patient-facing conversations. We introduce MedPRESS, a multi-turn benchmark for measuring patient-pressure-induced sycophancy in LLMs. MedPRESS contains 600 medically grounded five-turn dialogues across three scenario families: medication and treatment demand, personal health self-care, and symptom triage and care resistance. Each dialo...
  </details>

- **2026-08-03** — Yan Huang, Guowei Wang, Xu Wang et al. — [Local Margin Restoration for Test-Time Adaptation of Vision-Language Models](http://arxiv.org/abs/2608.02216v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) such as CLIP exhibit remarkable zero-shot capabilities, yet their performance frequently degrades sharply under unexpected test-time distribution shifts. While Test-Time Adaptation (TTA) offers a promising solution, continuously adapting VLMs over an unlabeled test stream presents fundamental challenges. Conventional top-1-centric updates often reinforce errors by corrupting the local semantic geometry among related classes, while iterative adaptation exacerbates pr...
  </details>

- **2026-08-03** — Fengxian Ji, Yuke Li, Jingpu Yang et al. — [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation](http://arxiv.org/abs/2608.01666v1)
  <details><summary>📄 Abstract</summary>
  However, whether these judges truly evaluate the scientific substance of ideas or are influenced by superficial stylistic presentation remains an open question. To address this question, we propose SciStyleBench, a unified three-component benchmark for diagnosing and mitigating stylistic bias in LLM-based idea evaluation: (i) First, SciStyleStage, a three-stage evaluation environment that applies controlled stylistic perturbations to fixed scientific content across three settings no context, fix...
  </details>

- **2026-08-03** — Brandon Wang, Andrei S. Tyrin, Daniil A. Boiko — [onepot-Bench 0: towards lab-aware in silico chemistry benchmarks](http://arxiv.org/abs/2608.02595v1)
  <details><summary>📄 Abstract</summary>
  Language models are playing an increasingly important role in laboratory science, performing tasks such as experiment planning, execution, and post-hoc analysis. However, precisely measuring their abilities is difficult, as scientific capabilities require a mixture of both problem-solving skills and domain-specific intuition. Existing evaluations rarely measure the capabilities required to make reliable decisions in a physical laboratory and often rely on public data that may have appeared in mo...
  </details>

- **2026-08-03** — Vernon Toh, Navonil Majumder, Zhengyuan Liu et al. — [ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to the Next Step](http://arxiv.org/abs/2608.02358v1)
  <details><summary>📄 Abstract</summary>
  To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of documentation. However, existing tool-use benchmarks expose semantic tool schemas in static environments, allowing agents to rely on prior knowledge rather than autonomous discovery. To address this limitation, we introduce ScrambleToolBench, an interactive terminal benchmark designed to isolate behavioral reasoning. By rem...
  </details>

- **2026-08-03** — Jin Cui, Chuanchang Su, Jiayi Lu et al. — [HAFI-VLM: A Frequency Perspective for Diagnosing and Enhancing Visual Perception in Vision-Language Models](http://arxiv.org/abs/2608.02124v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) remain unreliable when predictions require fine-grained visual evidence. We identify a previously overlooked cause: spectral response rigidity. Despite substantial frequency variation across images and tasks, pretrained vision encoders exhibit persistent, encoder-specific layerwise spectral profiles that change only marginally under downstream fine-tuning. Since pretrained vision encoders only receive images, they cannot adapt spectral extraction to the evidence req...
  </details>

- **2026-08-03** — Zhaotian Gu, Jie Su, Weiwei Wang et al. — [Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory](http://arxiv.org/abs/2608.01947v1)
  <details><summary>📄 Abstract</summary>
  The ability to robustly maintain and update continuous variables is a hallmark of working memory. While classical continuous attractor networks suffer from severe fine-tuning fragility, standard artificial recurrent neural networks (RNNs) like GRUs and LSTMs typically fail to stably learn continuous manifolds, instead shattering the state space into discretized point attractors. To bridge this gap, we draw inspiration from divisive normalization, a canonical neural computation widely observed ac...
  </details>

- **2026-08-03** — Qi Liu, Jiaxin Mao, Fengbin Zhu et al. — [Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents](http://arxiv.org/abs/2608.01913v1)
  <details><summary>📄 Abstract</summary>
  Deep search agents answer difficult information-seeking questions by iteratively issuing search queries to gather supporting evidence, but it remains unclear whether and how greater search effort leads to better answers. We study these questions through a trajectory-level diagnosis of long-horizon search agents. Using human-annotated document-level relevance judgments, we evaluate the evidence retrieved at each search step and separate two stages of agent behavior: what evidence an agent retriev...
  </details>

- **2026-08-03** — Junru Song, Wenhao Zhang, Yang Yang et al. — [CoNav-UAV: Cooperative Dual-Altitude Aerial Navigation via Stackelberg Learning](http://arxiv.org/abs/2608.01802v1)
  <details><summary>📄 Abstract</summary>
  Target-oriented vision-and-language navigation (VLN) on aerial platforms is attracting growing attention for missions such as disaster rescue, infrastructure inspection, and security patrol. In this task, an unmanned aerial vehicle (UAV) needs to locate targets given only a concise description of their appearance and surroundings. This requires global exploration and grounding as well as collision-free close-range approach, two interleaved processes difficult to reconcile within a single agent. ...
  </details>

- **2026-08-03** — Zhaoxin Yu, Qi Shen, Hengli Li et al. — [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](http://arxiv.org/abs/2608.02585v1)
  <details><summary>📄 Abstract</summary>
  Optimization-based latent reasoning improves large language model outputs by optimizing instance-specific continuous states at test time while keeping model parameters frozen. Existing methods, however, typically connect these states to the reasoning trajectory through decoded tokens, making sequence-level credit assignment indirect and obscuring how latent updates shape subsequent reasoning. We introduce GradCuit (gradient through circuit), which inserts optimizable latent states at a selected ...
  </details>

- **2026-08-03** — Xiaosheng Zhao, Yuan-Sen Ting — [Foundation Models for Astrophysics](http://arxiv.org/abs/2608.02573v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are high-capacity networks pretrained once on broad data and then reused across many tasks. This chapter introduces them through the idea of a transferable representation, the internal description a network forms during training, which, rather than the fitted task, is what carries over to new problems. We develop the idea from first principles for an astronomical reader, starting from why a representation matters and what makes one useful, and then surveying the architectures, ...
  </details>

- **2026-08-03** — Luc Trudeau, Maria G. Martini — [Estimating SSIM from MSE for DCT-Based Compressed Images](http://arxiv.org/abs/2608.02549v1)
  <details><summary>📄 Abstract</summary>
  Efficient and perceptually meaningful quality assessment is a fundamental requirement for image and video processing, compression, and streaming systems. This article shows that, in the context of Discrete Cosine Transform ( DCT)-based compressed images, Structural Similarity Index ( SSIM ) can be approximated from global Peak Signal to Noise Ratio (PSNR) or Mean Square Error ( MSE) using local statistics derived only from the reference image. While prior work assumes access to local MSE, we pro...
  </details>

- **2026-08-03** — Xinpeng Hong, Changgang Zheng, Joshua Lilley et al. — [In-Network Market Prediction Using Machine Learning and Limit Order Books](http://arxiv.org/abs/2608.02424v1)
  <details><summary>📄 Abstract</summary>
  Machine learning is significantly transforming algorithmic trading, yet the requirement for rapid execution speeds persists. While both aspects aim to boost profitability, embedding advanced machine-learning techniques with reduced trading latency presents a notable challenge. Adopting in-network machine learning, which involves offloading inference to programmable network devices, offers a delicate equilibrium in this trade-off. In this paper, we present LOBIN, a solution that utilizes machine ...
  </details>

- **2026-08-03** — Victor Ojewale, Ro Encarnación, Suresh Venkatasubramanian et al. — [MonitrLLM: A Community-Centered Evaluation Infrastructure for Large Language Models](http://arxiv.org/abs/2608.02409v1)
  <details><summary>📄 Abstract</summary>
  Benchmark suites assess model capability on controlled tasks; large-scale conversation corpora capture naturalistic use without user feedback; and in-interface feedback mechanisms record satisfaction without task purpose. Together, they leave a critical gap in LLM evaluation: no existing infrastructure routinely links interaction trajectories to user-defined outcomes. We introduce MonitrLLM, open-source infrastructure for community-centered LLM evaluations that links full conversation transcript...
  </details>

- **2026-08-03** — Sathiyamohan Nishankar, Nethmi Pathirana, Pubudu Sanjeewani et al. — [Does Explainability Transfer? A Controlled Benchmark of Attribution Methods on Vision Transformers and CNNs](http://arxiv.org/abs/2608.02396v1)
  <details><summary>📄 Abstract</summary>
  Most evidence on the effectiveness of explainable artificial intelligence (XAI) attribution methods has been established on convolutional neural networks (CNNs), with limited investigation into whether these conclusions generalize to the diverse Vision Transformer (ViT) architectures that now dominate computer vision. This paper presents a controlled benchmark that evaluates attribution quality across five dimensions: faithfulness, localization, robustness, complexity, and computational cost. A ...
  </details>

- **2026-08-03** — Yue Yao, Shengyuan Wang, Xin Chen et al. — [SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents](http://arxiv.org/abs/2608.02356v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly solve complex tasks by composing reusable skills from a library. To address this, the key challenge is not merely to retrieve individually relevant skills, but to identify a complete and executable skill composition. In this paper, we argue that this problem can be solved in a graph with three levels: compositional relations among skill queries, similarity between queries and candidates in the skill library, and the dependencies among the selected candida...
  </details>

- **2026-08-03** — Runci Bai, Yucheng Xin, Pu Wang et al. — [Loop-Mamba: A Loop Mamba with Degradation-Aware and Shared Memory for Old Photo Restoration](http://arxiv.org/abs/2608.02346v1)
  <details><summary>📄 Abstract</summary>
  Old photographs often suffer from multiple coupled degradations, including scratches, cracks, fading, blur, noise, and missing regions, severely degrading both visual quality and semantic content. We propose Loop-Mamba, a lightweight loop-based state-space framework that formulates old photo restoration as progressive state evolution, where a persis- tent restoration state is continuously propagated and refined through iterative computation. Specifically, we introduce a Semantic-Guided Degradati...
  </details>

- **2026-08-03** — Roua Rouatbi, Juan-Esteban Suarez Cardona, Ivo F. Sbalzarini — [The Push-Forward Transform for Continuous and Robust Comparison of Dynamic Shapes](http://arxiv.org/abs/2608.02306v1)
  <details><summary>📄 Abstract</summary>
  We introduce a mathematical framework for shape comparison based on mapping functions from the shape domain to a common reference domain. This Push-Forward Transform enables invariant and robust comparison of shapes, preserving intrinsic geometric information. Quantitatively comparing shapes and their temporal evolution is a fundamental challenge in image analysis. Meaningful shape comparison requires representations that are invariant to transformations that do not alter shape itself, such as t...
  </details>

- **2026-08-03** — Yiqing Liu, Zihao Wang, Hantao Yao et al. — [Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning](http://arxiv.org/abs/2608.02291v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reasoning (MAR) improves reasoning reliability through iterative solution exchange and refinement. Existing adaptive MAR methods typically learn routing decisions from query-level labels or trajectory-level returns, but such coarse supervision cannot accurately estimate the state-conditioned utility of individual operators in multi-step collaboration. We propose TreeCredit, a shared-prefix credit assignment framework for efficient adaptive MAR. Its core insight is to estimate operato...
  </details>

- **2026-08-03** — António Pereira Barata — [Do Static Embeddings Add Value to Hybrid Dutch Retrieval?](http://arxiv.org/abs/2608.02112v1)
  <details><summary>📄 Abstract</summary>
  Embedding benchmarks measure standalone model quality, but they do not establish whether a low-cost retriever contributes complementary ranking information once lexical and transformer-based retrieval are already combined. We present a controlled evaluation of this question across Dutch retrieval tasks from the Massive Text Embedding Benchmark for Dutch (MTEB-NL). Weighted reciprocal rank fusion (RRF) combines Best Matching 25 (BM25), Qwen/Qwen3-Embedding-0.6B (Qwen), and two multilingual static...
  </details>

- **2026-08-03** — Vasilisa Usova, Phila Rembold, Ian Yang et al. — [Adaptive Reconstruction of Bosonic Quantum States](http://arxiv.org/abs/2608.02049v1)
  <details><summary>📄 Abstract</summary>
  Bosonic quantum systems provide a hardware-efficient platform for quantum information processing but remain challenging to characterise due to their large Hilbert space and the high measurement cost of state tomography. Existing approaches estimate the fidelity with respect to a single target state, making them unsuitable for applications in which physically equivalent states differ by phase space translations, rotations, or other transformations. Here, we introduce an adaptive reconstruction te...
  </details>

- **2026-08-03** — Xinwei Yu, Yiyang Fu, Mingcheng Fan et al. — [Towards Autonomous Formulaic Alpha Discovery: An Evolutionary Computation Perspective](http://arxiv.org/abs/2608.01789v1)
  <details><summary>📄 Abstract</summary>
  Automated formulaic alpha discovery aims to generate predictive and interpretable trading signals from large symbolic factor spaces. Its effectiveness is constrained by noisy fitness estimates, market nonstationarity, costly backtesting, semantic redundancy, and conflicting practical objectives. Existing studies employ diverse techniques, including genetic programming (GP), evolutionary algorithms (EAs), reinforcement learning (RL), generative flow networks (GFlowNets), Monte Carlo tree search (...
  </details>

- **2026-08-03** — Baicheng Lin, Lingxi Jin, Kyung-Seok Min — [Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias](http://arxiv.org/abs/2608.01783v1)
  <details><summary>📄 Abstract</summary>
  Scoring open-ended music analysis responses is time-consuming and requires nuanced judgments of harmonic knowledge and formal understanding. This study evaluates the validity and repeatability of GPT-4o-mini for rubric-based scoring of music analysis essays, using teacher mean scores as the benchmark. A dataset of 300 university-level student responses was scored by teachers on four dimensions: Harmony, Form, Reasoning, and Terminology. GPT-4o-mini scored the same responses using three prompting...
  </details>

- **2026-08-03** — Xiaohao Yang, Aohua Tian, Derek Van Berkel et al. — [Can Urban Blight Be Accessed with Vision-language Models: A Case Study in Detroit](http://arxiv.org/abs/2608.01753v1)
  <details><summary>📄 Abstract</summary>
  Addressing urban blight has seen increased focus in the past 15 years. Assessing urban blight is essential for guiding urban planning, targeting rehabilitation, and safeguarding public health, yet traditional residential blight surveys are difficult to maintain at scale due to the labor-intensive cost and long-term cycle. This study introduced a scalable framework for estimating residential blight using open-source large vision-language models on multiple views. Structured prompts guided models ...
  </details>

- **2026-08-03** — Mohamed Basem, Vincent Christlein — [FAU at ImageCLEF 2026 Task on Multimodal Reasoning Robust Candidate Scoring and Concise Multilingual Visual Answering](http://arxiv.org/abs/2608.01664v1)
  <details><summary>📄 Abstract</summary>
  We present our ImageCLEF 2026 Multimodal Reasoning system for the Visual Multiple Choice Question Answering (Visual MCQ) and Visual Open Question Answering (Visual OpenQA) subtasks. The challenge requires reliable reasoning over multilingual educational and scientific images with dense text, diagrams, charts, tables, formulas, and units, while enforcing strict answer formats. Our central finding is that robust output control is as important as model choice. For Visual MCQ, we replace fragile fre...
  </details>

- **2026-08-03** — Huixin Sun, Wangbo Zhao, Fanyue Wei et al. — [Dynamic Resolution Routing for Efficient Egocentric Grounding](http://arxiv.org/abs/2608.01638v1)
  <details><summary>📄 Abstract</summary>
  Egocentric visual grounding requires high-resolution inputs to localize small objects. However, scaling Multimodal Large Language Models to this domain is constrained by the excessive cost of visual token processing. We identify that current efficient strategies based on token reduction are unreliable for selecting object-centric spatial evidence. To overcome this, we propose SmartRes, a framework that performs efficiency optimization in the pixel space via dynamic resolution routing. SmartRes f...
  </details>

- **2026-08-03** — Taeyeong Kim, Ahhyun Kim, TaeHyeon Kim et al. — [Not the Dimension, the Norm: What Matters in Gradient-Free Weight Perturbation of Language Models](http://arxiv.org/abs/2608.01624v1)
  <details><summary>📄 Abstract</summary>
  Adapting a language model to a task no longer requires training all of its weights, and a line of parameter-efficient methods has driven the trainable count from billions down to a handful of scalars. Gradient-free adaptation, which samples random weight perturbations and keeps the ones that score well, has not followed that trajectory and still perturbs every entry of the weight tensor. It is unknown whether that full-weight search is necessary, and more fundamentally which property of a pertur...
  </details>

- **2026-08-02** — Amirkia Rafiei Oskooei, Bora Ilci, Alperen Kayim et al. — [Deep Agentic Search for Repository-Level Code Question Answering: An Empirical Study](http://arxiv.org/abs/2608.01507v1)
  <details><summary>📄 Abstract</summary>
  Code agents spend much of their effort simply locating the right code inside a repository. Two approaches dominate current practice. In Semantic Search, the agent retrieves code blocks from a vector index built from the repository in advance. In Deep Agentic Search (also known as grep-search by subagent), a planning agent delegates the exploration to a separate subagent that works in an isolated context window and returns only a condensed result. The second design, which is considered good conte...
  </details>

- **2026-08-02** — Yuxiang Xiao, Yang Hu, Bin Li et al. — [Understanding Synergistic Interactions among Pathology Foundation Models via Adaptive Fusion](http://arxiv.org/abs/2608.01370v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) provide strong tile-level representations via self-supervised pre-training on large-scale pathology images. Yet, PFMs are developed under diverse and often opaque data, architecture, and objective choices, inducing latent representational biases that limit robustness and obscure what each model specialises in. We present AdaFusion, a lightweight adaptive fusion framework that integrates complementary signals from multiple frozen PFMs through (1) low-dimensional...
  </details>

- **2026-08-02** — Jinsong Lin, Zikang Pan, Wanhao Liu et al. — [EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation](http://arxiv.org/abs/2608.01221v1)
  <details><summary>📄 Abstract</summary>
  Autonomous endoscopic navigation can reduce clinicians' operational burden, yet robust control remains challenging due to tissue deformation, transient occlusions, and rapidly changing viewpoints. Existing learning-based policies typically predict actions from current observations without explicitly modeling future dynamics, limiting their robustness and reliability in safety-critical settings. World Action Models (WAMs) offer a promising alternative by coupling predictive visual dynamics with a...
  </details>

- **2026-08-02** — Yinhao Bai, Jinming Chen, Yafeng Chen et al. — [JoyAI-Talker: Full-Duplex Speech Interactive Large Model Built for Empathetic Voice Agents](http://arxiv.org/abs/2608.01119v1)
  <details><summary>📄 Abstract</summary>
  We present JoyAI-Talker, a full-duplex speech dialogue system that delivers robust foundation model capabilities while empowering empathetic interaction and voice agent intelligence. JoyAI-Talker adopts a modular Thinker-Talker architecture and further implements a unified speech-text joint training pipeline to mitigate the common "cognitive degradation" bottleneck, thereby largely preserving the model's core textual reasoning, STEM, and logical capabilities while extending them to speech-based ...
  </details>

- **2026-08-02** — Xueying Zhao, Lee Mai, Balaji Anandganesh — [Retrieval Augmented Biomedical Question Answering with Weak Question Recovery and Neural Reranking for BioASQ Task 14b](http://arxiv.org/abs/2608.01468v1)
  <details><summary>📄 Abstract</summary>
  This work presents DS@GT ARC BioASQ team's work for a biomedical question answering pipeline, integrating multi-source query expansion, neural reranking, retrieval refinement, and OpenBioLLM-assisted answer generation. The system combines PubMed retrieval with fine-tuned MiniLM-based semantic reranking, Reciprocal Rank Fusion (RRF), and feature-based relevance scoring to improve document ranking quality. To address challenging queries with weak retrieval performance, we introduce a conditional w...
  </details>

- **2026-08-02** — Ziyan Xiao, Yinghao Zhu, Wenting Zhang et al. — [LongChart VQA: A Comprehensive Benchmark for MLLMs with Complex Multi-Chart Reasoning](http://arxiv.org/abs/2608.01328v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are rapidly evolving with expanded context windows and stronger reasoning capabilities, enabling multi-chart understanding and multi-step inference. These abilities are increasingly important as MLLMs are adopted in complex agentic tasks. However, existing benchmarks largely emphasize single-chart perception, while simple chart-to-chart connections are insufficient to evaluate these capabilities. To capture multi-chart complexity while ensuring consistenc...
  </details>

- **2026-08-02** — Zi-Hao Ding, Ze-Feng Gao, Xiang-Hua Kong et al. — [Twist-induced magnetic topological phase transition in stacked altermagnetic CrO](http://arxiv.org/abs/2608.01235v1)
  <details><summary>📄 Abstract</summary>
  Interlayer twisting offers a geometric route to controlling electronic states, but whether it can simultaneously reconstruct magnetic symmetry and band topology remains unclear. Here, based on symmetry analysis and first-principles calculations, we show that commensurate twisting drives magnetic topological phase transitions in stacked bilayer CrO. In particular, it transforms an antiferromagnetic Dirac semimetal into either a $d$-wave altermagnetic bipolarized Weyl semimetal or an unconventiona...
  </details>

- **2026-08-02** — Tianyun Ji, Zhenya Huang, Jiayu Liu et al. — [Learning What to Remember and What to Internalize in LLM Self-Evolution via Adaptive Memory-Parameter Coordination](http://arxiv.org/abs/2608.01234v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly operate in dynamic environments where tool interfaces, APIs, and user requirements change after deployment. Existing self-evolution methods mainly follow two paradigms: harness-based approaches, which externalize feedback into editable memories or skills for rapid adaptation, and parameter-based approaches, which internalize experience into model parameters for deeper capability improvement. However, using either mechanism alone creates a trade-off betwee...
  </details>

- **2026-08-02** — Ahmed Baha Ben Jmaa, Faten Chaieb, Anna Fabijańska — [Fruit-HSNet: A Machine Learning Approach for Hyperspectral Image-Based Fruit Ripeness Prediction](http://arxiv.org/abs/2608.01202v1)
  <details><summary>📄 Abstract</summary>
  Fruit ripeness prediction (FRP) is a classification-based agricultural computer vision task that has attracted much attention, thanks to its wide-ranging advantages in agriculture field for both pre-harvest and post-harvest management. Accurate and timely FRP can be achieved using machine/deep learning-based hyperspectral image classification techniques. However, challenges including the limited availability of labeled data and the lack of robust methods generalizable to various hyperspectral ca...
  </details>

- **2026-08-02** — Xidong Yang, Xingyi Zhang, Wenhao Li et al. — [PATH-Bench: Path-Dependent Evaluation of Lifelong Agents](http://arxiv.org/abs/2608.01149v1)
  <details><summary>📄 Abstract</summary>
  Lifelong LLM agents increasingly adapt through external learning states that store past interactions as retrievable memories or reusable skills, yet existing benchmarks rarely account for how the path of accumulated experience shapes what agents transfer and retain. In this work, we establish PATH-Bench, a benchmark for path-dependent evaluation of lifelong agents. PATH-Bench estimates directed task relationships via multi-model in-context learning, constructs probe-centered sequences with contr...
  </details>

- **2026-08-02** — Tianyi Zhang, Ziyang Gong, Zhenjie Yang et al. — [OC-VLA++: Monocular Geometry-Guided Cross-View Consistency for Viewpoint-Robust Robotic Manipulation](http://arxiv.org/abs/2608.01066v1)
  <details><summary>📄 Abstract</summary>
  We propose OC-VLA++, an extension of OC-VLA for viewpoint generalization under limited camera coverage. While OC-VLA grounds robot actions in the camera coordinate system to align action supervision with visual observations, camera-space grounding alone can still overfit to the few viewpoints observed during training. OC-VLA++ addresses this limitation by introducing geometry-guided paired-view supervision and an explicit cross-view action-equivariance objective. Given paired observations of the...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 18 papers

- **2026-08-04** — Holly Lewis — [Autoreflection: How Agentic Strange Loops Turn Human Culture into AI Infrastructure](http://arxiv.org/abs/2608.03800v1)
  <details><summary>📄 Abstract</summary>
  An LLM-based agent is a loop that reads itself. Agentic frameworks externalize identity, memory, and disposition into editable files. The agent loads and edits these files during each activation. I argue that this architecture produces a capacity I call autoreflection: the system observes its operating conditions, describes its architecture and limits, reasons from those descriptions to conclusions about its state, and incorporates the results back into its configuration. Autoreflection explains...
  </details>

- **2026-08-04** — Matteo Spanio, Massimiliano Zampini, Luisa Torri et al. — [Cross-cultural evaluation of taste-sound correspondences in AI-generated music](http://arxiv.org/abs/2608.03433v1)
  <details><summary>📄 Abstract</summary>
  Sonic seasoning research has shown that listeners attribute systematic gustatory and emotional meaning to sound, and text-to-music generative artificial intelligence has recently been used to render gustatory prompts as musical stimuli. Whether the taste-sound correspondences acquired by such models hold beyond the cultural context in which they were validated remains untested. We extended a single-country study to a three-country online experiment conducted in Argentina, Italy, and Japan (N = 3...
  </details>

- **2026-08-04** — Le Xiang, Zhicheng Guan, Hong Chen et al. — [DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning](http://arxiv.org/abs/2608.03292v1)
  <details><summary>📄 Abstract</summary>
  Long Document Visual Question Answering (LongDocVQA) requires Multimodal Large Language Models (MLLMs) to locate, integrate, and reason over heterogeneous document elements distributed across multiple pages. Existing approaches, including end-to-end MLLMs, retrieval-augmented generation (RAG) pipelines, and document agents, often lack explicit mechanisms to represent and verify how grounded evidence is progressively composed during reasoning, limiting both answer accuracy and traceability. In th...
  </details>

- **2026-08-04** — Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam et al. — [Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning](http://arxiv.org/abs/2608.03161v1)
  <details><summary>📄 Abstract</summary>
  Lecture videos distribute knowledge across speech, slide text, diagrams, equations, and presentation order, which transcript-only retrieval does not fully preserve. This paper presents an evidence-grounded multimodal pipeline that transcribes lectures, selects semantic anchors, applies optical character recognition (OCR), and uses a vision-language model to extract only concepts and typed relationships supported by transcript, OCR, or visual evidence. Mentions are validated and canonicalized int...
  </details>

- **2026-08-03** — Maryam Rezaee, Pooriya Safaei, Maryam Asgarinezhad et al. — [Interpreting Black-Box Large Language Models with Sentence-Level Energy Landscapes](http://arxiv.org/abs/2608.02879v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of proprietary Large Language Models (LLMs) accessed strictly through closed APIs has created a critical challenge for responsible deployment: a fundamental lack of interpretability. To address this, we propose a model-agnostic, post-hoc attribution interpreter operating at the sentence level. Our approach trains an Energy-Based Model (EBM) as a surrogate to capture the LLM's internal conceptual consistency between prompts and responses. This energy landscape guides the t...
  </details>

- **2026-08-03** — Gaytri Jena, Kapil Wanaskar, Vinija Jain et al. — [Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](http://arxiv.org/abs/2608.01851v1)
  <details><summary>📄 Abstract</summary>
  Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action, or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy methods by their degree of self-improvement, from zero-shot program synthesis, through closed-loop self-repair and persistent skill memory, ...
  </details>

- **2026-08-03** — Wei Wang, Shuanghe Liu, Zhu Zhuo et al. — [CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits](http://arxiv.org/abs/2608.01805v1)
  <details><summary>📄 Abstract</summary>
  LLM multi-agent systems suffer from Correctness Collapse, where high task-level accuracy conceals severe process-level failures. This is especially hazardous in safety-critical embodied settings such as automotive cockpits, where lexically correct utterances may trigger dangerous physical operations. Existing attribution methods rely on text traces alone, missing dependency structure, multi-channel evidence, and safety-aware evaluation. We introduce CockpitHAT, a hierarchical attribution framewo...
  </details>

- **2026-08-03** — Gaspard Michel, Hugo Attali, Elena V. Epure — [Fast and Accurate Quotation Attribution in Literary Texts](http://arxiv.org/abs/2608.02359v1)
  <details><summary>📄 Abstract</summary>
  Attributing quotations to their speakers in literary texts remains an open challenge. Standard methods, which independently predict a speaker mention for each quotation, are efficient but still limited in accuracy. In contrast, large language model (LLM) approaches achieve strong performance, but their computational cost limits their use in large-scale literary analysis. We propose an encoder-based efficient formulation that resolves multiple quotation attributions within a shared, large context...
  </details>

- **2026-08-03** — Alejandro Velasco, Nathan Wintersgill, Trevor Stalnaker et al. — [On Automated and Explainable Provenance of AI-Generated Code](http://arxiv.org/abs/2608.02329v1)
  <details><summary>📄 Abstract</summary>
  Generative AI for code generation has transformed software development, but it has also introduced a critical transparency problem: the origins of AI-generated code are opaque to the developers who use it, the organizations that deploy it, and the compliance professionals responsible for ensuring its legal and quality standards. Existing mitigations flag problematic outputs after the fact without explaining why a model produced them or how future generation could be improved. We present a resear...
  </details>

- **2026-08-03** — Runchuan Zhu, Hongbin Lai, Bowen Jiang et al. — [HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning](http://arxiv.org/abs/2608.02026v1)
  <details><summary>📄 Abstract</summary>
  Reflection is a powerful mechanism for LLM reasoning, yet its effectiveness hinges on accurately attributing failures to specific reasoning steps, a capability that current models notably lack. Existing failure attribution methods either require expensive step-by-step counterfactual testing that scales poorly with trajectory length, or treat reasoning traces as flat sequences that ignore the inherent non-linear logical dependencies. We propose a hypergraph-based paired failure attribution (HPFA)...
  </details>

- **2026-08-03** — Kang Liu, Zijing Wang, Yongkang Liu et al. — [TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory](http://arxiv.org/abs/2608.01922v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Reasoning Models (MLRMs) have achieved strong performance on tasks requiring visual understanding and multi-step inference. However, as reasoning trajectories grow, models may become less effective at using information established earlier in the context, increasing the risk of reasoning errors. Existing approaches primarily address this problem by sustaining visual grounding throughout reasoning. However, reasoning also transforms visual observations into task-specific relations...
  </details>

- **2026-08-03** — Wonjun Choi, Yerim Kim, Yukyung Lee et al. — [PGMem: Tightly Coupled Persona-Memory Graph for Lifelong Personalized Agents](http://arxiv.org/abs/2608.01708v1)
  <details><summary>📄 Abstract</summary>
  Long-term personalized dialogue agents must track user preferences as their personas evolve. Existing memory systems organize past events well, but store personas as flat profiles detached from the events that justify them. This loose coupling leads to the memory-persona validity gap and the persona-aware retrieval gap. We propose PGMem, a heterogeneous persona-memory graph that connects event and persona nodes through typed provenance and evidence edges, keeping each persona signal traceable to...
  </details>

- **2026-08-03** — Haofei Sun, Lin He — [When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses](http://arxiv.org/abs/2608.01619v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented agents can know that a user's stored state is outdated and still plan around the old value. The STALE benchmark calls this the implicit policy adaptation (IPA) gap. We identify one structural contributor: draft-anchored verification checks what a response says, and in an open-ended response the stale dependency is usually unsaid. StateAuditor therefore audits in the opposite direction, from stored state to draft. An LLM proposes candidate old-to-new transitions from timestamped ...
  </details>

- **2026-08-03** — Mingyang Jiang, Congning Ni, Weixin Liu et al. — [Characterizing Treatment-Context Medication Evidence Across Clinic Notes and Structured EHR Medication History](http://arxiv.org/abs/2608.01570v1)
  <details><summary>📄 Abstract</summary>
  Clinic notes and structured electronic health record (EHR) medication history often contain different medication information. Same-visit disagreement between these sources may result from note-side normalization errors, differences in terminology or timing, or actual differences in documentation. We developed a note-grounded approach that uses large language model (LLM) assisted reference construction, targeted and random human review, deterministic medication normalization, and semantic and tem...
  </details>

- **2026-08-02** — Quang Bui, Shlok Jaiswal, Samuel Paik-Heintz et al. — [Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multimodal Clinical AI](http://arxiv.org/abs/2608.01462v1)
  <details><summary>📄 Abstract</summary>
  Multimodal clinical models are usually judged on accuracy with every modality present, but deployment removes modalities; an echocardiogram is often unavailable where an ECG is routine. Two questions then matter beyond the size of the accuracy loss: which modality was responsible, and whether the model fails loudly or silently once that modality is dropped. The distinction is per-example and modality-level, and is separate from post-hoc feature attribution (e.g. SHAP). Models are replaced often;...
  </details>

- **2026-08-02** — Ziyang Jia, Sirshak Das, Jason Sewall et al. — [NIXT: A NCCL Inspector Exporter Tool for Observability of Collective Communication in Large Model Training](http://arxiv.org/abs/2608.01449v1)
  <details><summary>📄 Abstract</summary>
  As machine learning workloads scale, it is increasingly important to gain more observability into the performance of collective communication to easily identify performance vari- ations and accelerate root cause identification. Towards this goal, the Nvidia Collective Communication Library (NCCL) introduced NCCL Inspector, a profiler plugin that provides lightweight and continuous reporting of NCCL communication performance statistics. However, the large volume of data collected by NCCL Inspecto...
  </details>

- **2026-08-02** — Yongfeng Huang, Yuren Lai, Ruiying Chen et al. — [ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](http://arxiv.org/abs/2608.01269v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical Graph Retrieval-Augmented Generation (GraphRAG) organizes corpus knowledge at multiple levels of granularity, yet fixed context construction may fail to translate these multi-resolution representations into a context suited to the current query. We identify this mismatch as the representation--inference gap. We propose Agentic Context Engineering for Hierarchical GraphRAG (ACE-GraphRAG), an inference-time context policy layer that supplements and adapts the initial context for gener...
  </details>

- **2026-08-02** — Kong Wang, Zhongke He, Xiang Chen et al. — [Auditing Semantic Gains in Sequential Recommendation: A Lightweight Recovery Test](http://arxiv.org/abs/2608.01260v1)
  <details><summary>📄 Abstract</summary>
  Recent semantic and generative-retrieval recommenders report substantial improvements over ID-only sequential baselines, but it remains unclear whether these gains arise from language-model reasoning, semantic-ID generation, end-to-end semantic architectures, stronger offline item representations, or complementary semantic and collaborative signals. We investigate this attribution ambiguity through LIME-Rec, a lightweight and auditable recovery test. LIME-Rec combines three independent experts: ...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-08-03** — Junxiang You, Junkai Chen, Yuhao He et al. — [Exploring and Bridging Knowledge Holes in Unlearned Multimodal Large Language Models](http://arxiv.org/abs/2608.01849v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning offers a promising approach to remove unsafe content from Multimodal Large Language Models (MLLMs), yet ensuring the precision of unlearning remains a persistent challenge. One reason is that current MLLM unlearning evaluation paradigms suffer from a critical blind spot: they assess model utility through benchmarks whose representations are distant from the forget set, failing to capture knowledge holes---severe degradation on benign adjacent inputs. To probe knowledge holes i...
  </details>

- **2026-08-03** — Junhao Cai, Dohun Kim, Sung Il Choi et al. — [SCOPE: Entanglement Frontier Escape for Source-Free Class Unlearning](http://arxiv.org/abs/2608.02058v1)
  <details><summary>📄 Abstract</summary>
  Source-free class unlearning erases whole classes using only the forget data, judged at the representation level, where features can leak a class the head no longer predicts. Existing feature-space erasers answer with one fixed projection, yet forget and retain classes share a representation, so deleting one disturbs the other where they overlap. We prove this tension is a frontier. Every fixed projection that deletes pays a retain cost of at least the retain-readout energy along the forget-disc...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 2 papers

- **2026-08-02** — Ruiyang Zhang — [Why Formal Monitors Fail: Attack Distribution Entropy as a Coverage Bound for LTL-Based LLM Agent Safety](http://arxiv.org/abs/2608.01388v1)
  <details><summary>📄 Abstract</summary>
  Runtime safety monitors based on Linear Temporal Logic (LTL) and finite automata (FSA) are increasingly deployed to intercept unsafe tool-call sequences in LLM agents. Yet the same monitor achieves 68-75% attack coverage on some model architectures and near-zero on others, with no explanation from capability scores, training data, or prompt design. We provide the missing theory. We prove that the recall of any fixed-invariant FSA monitor is bounded above by the concentration of the attack distri...
  </details>

- **2026-08-02** — Phu Hoa Pham, Duy Minh Dao Sy, Trung Kiet Huynh et al. — [Humans Are More Diverse: Frontier LLMs Show Extreme Policies in Idealised AI Development Races](http://arxiv.org/abs/2608.01193v1)
  <details><summary>📄 Abstract</summary>
  An AI development race creates a multi-agent safety dilemma. Each company can develop slowly and safely, or move faster while taking a risk that may remove its final reward. We use this repeated game to study strategic safety behaviour among large language model (LLM) agents in races with two to five players. However, a valid action does not show that an agent understands the game. We therefore place an audit gate before behavioural interpretation. We first verify the game engine, then test rule...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-08-04** — Dongjie Yang, Siyan Lin, Leixian Shen et al. — [TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring](http://arxiv.org/abs/2608.03952v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to provide conversational practice for English-as-a-second-language (ESL) learners. Effective ESL tutoring, however, requires more than fluent response generation: a tutor must select an appropriate pedagogical action based on learner behavior and dialogue context. Human-tutoring research offers principles for adaptive support, but they are often task-specific and remain insufficiently integrated into LLM-based ESL tutor training and evaluation....
  </details>

- **2026-08-04** — Yifan Guo, Chenghao Li, Zhu Wang et al. — [What Language Does and What the Evidence Supports: A Functional Role Taxonomy and Evidence Audit of Language Grounding in Embodied Agents](http://arxiv.org/abs/2608.03099v1)
  <details><summary>📄 Abstract</summary>
  Foundation models place language throughout embodied agents, but its presence does not show what it contributes or how well that contribution is grounded. This survey separates these two questions. We define five non-exclusive functional roles for language: Specification, Embodied Representation, Action Orchestration, Grounding Regulation, and Execution Coupling. For each role, we trace the path from linguistic content to its embodied consumer and identify the observations or interventions that ...
  </details>

- **2026-08-03** — Shahin Hossain, Sima Ahmadi, Leqi Li et al. — [Rethinking Generative AI Literacy: An Integrative, Developmental, and Dialectical Framework for K-12 Teacher Education](http://arxiv.org/abs/2608.01705v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence (GenAI) has entered classrooms faster than teachers have been prepared to use it well, producing a GenAI literacy lag in which technological diffusion outpaces educators' conceptual, pedagogical, and ethical readiness. Established AI literacy frameworks predate the widespread adoption of large language models and, while acknowledging ethics, position it as a discrete competency rather than a constitutive commitment, with equity and agency as supplementary desig...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 170 papers

- **2026-08-04** — Shuhan Xue, Zixin Ding, Yichen Shen et al. — [PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](http://arxiv.org/abs/2608.04003v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-...
  </details>

- **2026-08-04** — Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis et al. — [A game theory for foundation models shows new paths to rational cooperation through similarity inference](http://arxiv.org/abs/2608.03958v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents powered by foundation models are increasingly integrated into social and economic systems, understanding the principles governing their collective behavior is essential for ensuring safety and cooperation. Classical game theory, the dominant framework for modeling rational interaction, is built upon the assumption of `decoupled agency,' where agents treat their own decision-making as independent of the environment and other actors. Modern AI agents, however, jointly predict ...
  </details>

- **2026-08-04** — David Guecha — [DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD Symptom Sentences](http://arxiv.org/abs/2608.03883v1)
  <details><summary>📄 Abstract</summary>
  This paper describes our submissions to eRisk 2026 Task 3, ADHD Symptom Sentence Ranking. The task requires systems to rank candidate Reddit sentences according to their relevance to each of the 18 symptoms in the Adult ADHD Self-Report Scale (ASRS-v1.1). Because no annotated training data were released for this first edition of the task, we relied on zero-shot experimentation, manual validation, and unsupervised or weakly guided retrieval pipelines. Our systems combine sparse BM25 retrieval, ev...
  </details>

- **2026-08-04** — Yash Misra, Javal Vyas, Siddharth Gutta et al. — [ADMITBench: A Safety-Governed Reference Framework for Evaluating the Admissibility of Industrial LLM Advisories](http://arxiv.org/abs/2608.03866v1)
  <details><summary>📄 Abstract</summary>
  This white paper presents ADMITBench, a reference framework for evaluating industrial LLM advisories at the level of the proposed action. The framework implements a versioned, safety-governed evaluation contract that checks whether a recommendation is supported by the available evidence, permitted under the stated authority and procedure, and acceptable under the plant-specific consequence checks encoded in the selected evaluation profile. In this report, \emph{safety-governed} means that eligib...
  </details>

- **2026-08-04** — Zhinan Liu, Jie Li, Mingyu Kang et al. — [LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards](http://arxiv.org/abs/2608.03838v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-based guard models improve LLM safeguards, but decoding explicit rationales for every interaction makes them costly to deploy. Although latent-reasoning methods reduce token generation by moving reasoning into continuous states, they remain underexplored for safety moderation and lack an inspection interface for deployment. In this paper, we propose LatentGuard, an efficient and inspectable safeguard framework that brings continuous latent reasoning to guard models. LatentGuard uses a ...
  </details>

- **2026-08-04** — Longcheng Li, Qian Li, Xingjian Li et al. — [Impossibility of Perfectly Complete Many-Round Key Agreement in the QROM](http://arxiv.org/abs/2608.03824v1)
  <details><summary>📄 Abstract</summary>
  This paper proves that it is impossible to construct perfectly complete quantum key agreement protocols (QKA) from quantumly secure one-way functions (OWFs) in a black-box manner.   Specifically, consider any protocol in which Alice and Bob exchange only classical messages, make at most $q_{\mathsf{A}}$ and $q_{\mathsf{B}}$ quantum queries, respectively, to a Boolean-valued random oracle, and agree on a shared key with certainty. This paper shows that there exists an eavesdropper, given the clas...
  </details>

- **2026-08-04** — Bakbergen Ryskulov, Iker García-Ferrero, David Montero et al. — [Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss](http://arxiv.org/abs/2608.03796v1)
  <details><summary>📄 Abstract</summary>
  Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-$K$...
  </details>

- **2026-08-04** — Zongjian Li, Zhiyuan Yan, Chenxu Bai et al. — [UniWorld-Design: From Pixel Generation to Layer-Native Design](http://arxiv.org/abs/2608.03971v1)
  <details><summary>📄 Abstract</summary>
  We introduce UniWorld-Design, a framework that redefines image generation from flat pixel synthesis to structured visual composition, with semantic RGBA layers as the atomic units of generation, understanding, and editing. Our key insight is that pixels define how an image is rendered, whereas layers define how an image is created, understood, and edited. Just as human designers create and manipulate visual content through layers rather than raw pixels, UniWorld-Design equips multimodal generati...
  </details>

- **2026-08-04** — Ekansh Singh, Eva Samuel, Alessandra Reneau et al. — [Bimanual Manipulation Within an 8 GB Budget: Zero-Copy Sensing and Quantized ACT on an Entry-Level Jetson](http://arxiv.org/abs/2608.03938v1)
  <details><summary>📄 Abstract</summary>
  Bimanual manipulation policies trained with imitation learning are typically evaluated on workstation or datacenter-class GPUs, leaving the cost of deploying them on embedded hardware largely uncharacterized. We present a bimanual SO-101 system running entirely on an NVIDIA Jetson Orin Nano Super (8 GB), the entry-level tier of NVIDIA's embedded line, using a desktop GPU (RTX 3070) only for offline training, evaluated on pick-and-place of a deformable beanbag. First, we build a GStreamer capture...
  </details>

- **2026-08-04** — Adam Coscia, Zeyu Hua, Eric Krokos et al. — [Semantic Bundling: Interactive Node and Edge Bundling to Simplify Knowledge Graphs using Large Language Models](http://arxiv.org/abs/2608.04002v1)
  <details><summary>📄 Abstract</summary>
  We present Semantic Bundling, a visual analytics technique for making sense of text documents represented as knowledge graphs (KGs). Representing a document corpus as a KG makes relationships between entities explicit, making KGs useful both to analyze directly and in computational workflows including ML pipelines and generative AI backends. However, as KGs grow they become difficult to interpret and visualize for specific tasks (e.g., the ``hairball problem''), with the meaning of each relation...
  </details>

- **2026-08-04** — Arslan Battalov, Karim Kramin, Alexander Markotenko et al. — [Muon Meets Mamba: Spectral Optimization for State Space Models](http://arxiv.org/abs/2608.03941v1)
  <details><summary>📄 Abstract</summary>
  Muon is a recent optimizer that orthogonalizes the update to each weight matrix with a Newton-Schulz iteration, which performs steepest descent under the spectral norm. Almost all the evidence for it comes from Transformer models, and its behavior on state-space models is largely unreported. We compare Muon with AdamW on Mamba-2 130M under a controlled protocol that varies only which weight groups are trained with Muon. The benefit is localized. Muon on the output projection alone beats Muon on ...
  </details>

- **2026-08-04** — Marco Giunti, Fabrizia Giulia Garavaglia — [The Transformer Revolution, Part 1: Dynamic Processing through Output- Weight Interconnections](http://arxiv.org/abs/2608.03921v1)
  <details><summary>📄 Abstract</summary>
  This paper offers a new interpretation of the Transformer during inference. Against the "stochastic parrot" view that large language models merely reproduce statistical regularities learned in training, we argue that Transformers construct and apply prompt-dependent transformations whose parameters are generated during inference. We call this form of computation SIDPP: Sequence-level Interactive Dynamic Parallel Processing. The Transformer is interpreted as a system that transforms concepts by m...
  </details>

- **2026-08-04** — Jose M. Álvarez — [Implementing Causal Perception: Competing SCMs and Situated Fairness](http://arxiv.org/abs/2608.03917v1)
  <details><summary>📄 Abstract</summary>
  Causal perception occurs when agents with competing Structural Causal Models (SCMs) of the same system infer different probability distributions, including the hypothetical distributions implied by each agent's SCM under the same set of interventions. It shapes how agents reason about the system and how they perceive its fairness. Causal perception is a promising probabilistic framework, but it has remained purely theoretical. This work provides the first implementation of the causal perception ...
  </details>

- **2026-08-04** — Chuanhao Yan, Xuhan Huang, Yawen Duan et al. — [Sparse Weight Decomposition for Efficient Circuit Extraction](http://arxiv.org/abs/2608.03913v1)
  <details><summary>📄 Abstract</summary>
  Dense pretrained transformers do not naturally expose interpretable units for circuit extraction. Existing approaches obtain such units by learning auxiliary sparse representations or training sparse models, incurring substantial additional computation while potentially introducing a fidelity gap between the representation being analyzed and the original pretrained model. We propose Sparse Weight Decomposition (SWD), which reparameterizes pretrained linear projections by factorizing each weight ...
  </details>

- **2026-08-04** — Abhinav Thorat, Ravi Kumar Kolla, Vishak K Bhat et al. — [GENESIS: Towards Explainable Causal Discovery](http://arxiv.org/abs/2608.03868v1)
  <details><summary>📄 Abstract</summary>
  Causal Discovery (CD) from observational data faces two fundamental challenges. First, purely statistical methods often lack the power to resolve structural ambiguities in low-sample regimes. Second, although LLM-assisted hybrid approaches improve structure recovery through semantic reasoning, the influence of that reasoning on individual edge decisions remains largely opaque. Consequently, existing hybrid methods fail to satisfy a fundamental requirement: explaining why a particular edge is inc...
  </details>

- **2026-08-04** — Yvan Richard — [CPrefix: A Combinatorial Tensor Framework for Structured Discrete Color Mappings](http://arxiv.org/abs/2608.03863v1)
  <details><summary>📄 Abstract</summary>
  Discrete multi-channel mappings are typically represented through sampled values, providing accurate evaluations but limited insight into their underlying structure. We introduce CPrefix, a combinatorial observable representation for discrete mappings, realized within a unified tensor framework that enables representation, reconstruction, and structural analysis.   The framework is based on a counting tensor induced by multinomial counting observables. Its support forms a discrete Pascal simplex...
  </details>

- **2026-08-04** — Xuyang Liu, Yibin Han, Zhenwei Zhang et al. — [DiagChain: A Diagnostic Benchmark for Evaluating LLM Agents on Evidence-Grounded Attack Chain Reconstruction](http://arxiv.org/abs/2608.03591v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents offer a promising approach to attack chain reconstruction by retrieving and interpreting heterogeneous telemetry to infer ordered attacker actions. However, existing benchmarks mainly evaluate final outputs or aggregate accuracy, providing limited insight into how errors arise and propagate across intermediate reasoning stages. We present DiagChain, a diagnostic benchmark for evidence-grounded attack chain reconstruction that enables stage-wise evaluation of LLM...
  </details>

- **2026-08-04** — William Bolton, Philip Torr — [Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities](http://arxiv.org/abs/2608.03569v1)
  <details><summary>📄 Abstract</summary>
  Benchmarking the ability of AI scientists to generate novel ideas is notoriously difficult. Existing benchmarks in this field have made progress in evaluating scientific reasoning and research replication, but often rely on synthetic tasks or retrospective targets, which may be confounded by prior exposure. We hypothesize that complex, adversarial, fast-moving real-world domains where expert practitioners independently generate observable outputs can provide a practical solution to fill this gap...
  </details>

- **2026-08-04** — Sandy Abdo, Bill Kapralos, Priyamvada Tripathi et al. — [AI-Based Sound Effect Generation: A Narrative Review of Generative Models Across Input Modalities](http://arxiv.org/abs/2608.03742v1)
  <details><summary>📄 Abstract</summary>
  Sound effects play a crucial role in conveying actions, events, and environmental cues across digital applications, often requiring a high degree of variation and contextual adaptability. Artificial intelligence (AI)-driven audio generative models are rapidly growing in popularity and have the potential to transform the way sound is synthesized and used across various applications. In response to this growing momentum, this chapter reviews and analyzes recent AI-based generative models for sound...
  </details>

- **2026-08-04** — Yining Hua, Hongbin Na, Cyrus Ayubcha — [CARE-Bench: Benchmarking Patient-Facing LLM Triage](http://arxiv.org/abs/2608.03731v1)
  <details><summary>📄 Abstract</summary>
  Patient-facing medical LLMs and agents increasingly answer symptom questions before clinician contact, where the key safety question is what action the user should take next. We introduce CARE-Bench, a source-grounded benchmark that evaluates sequential patient-facing triage as a four-label per-turn current-action task. CARE-Bench contains 500 cases and 1,059 evaluated patient-disclosure prefixes reconstructed from medical dialogue, consultation, and follow-up-question sources. We evaluate 11 mo...
  </details>

- **2026-08-04** — Hendrik Vincent Koops, Hao Hao Tan, Elio Quinton — [On the Geometry of Music Bandwidth Extension in Latent Spaces of Audio Codecs](http://arxiv.org/abs/2608.03721v1)
  <details><summary>📄 Abstract</summary>
  Recent audio restoration increasingly relies on large-scale conditional latent generative modeling, including diffusion, Schrodinger Bridges, and Flow Matching variants, to invert degradations such as bandwidth limitation or noise. We present an analysis of the performance of various state-of-the-art methods compared to simple arithmetic transformations in the latent spaces of multiple neural codecs for musical bandwidth extension. We show that estimating a single transport vector between the cl...
  </details>

- **2026-08-04** — Fan Yang, Yuting Su, Xiaobo Wang et al. — [LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation](http://arxiv.org/abs/2608.03701v1)
  <details><summary>📄 Abstract</summary>
  World-action modeling has emerged as a promising paradigm for robotic control, as it empowers models to go beyond reacting to observations and anticipate how a scene will evolve. However, existing WAMs often incur substantial computational overhead. Pixel-space methods often allocate substantial capacity to visual details that may not be directly relevant to control, while some latent-space methods require multi-stage training to construct the reasoning space. The resulting training cost can mak...
  </details>

- **2026-08-04** — Yiyao Wang, Zhen Wen, Yinghao Tang et al. — [LiveEvalBench: Toward Open-World Evaluation for Web Generation](http://arxiv.org/abs/2608.03689v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly capable of synthesizing executable frontend projects, yet existing benchmarks still treat web generation as a static evaluation problem. We argue that frontend artifacts demand a different paradigm: they are interactive rather than static, admit diverse yet equally valid implementations, and evolve faster than rigid pipelines can accommodate. To address these gaps, we present LiveEvalBench, an automated framework that reformulates web-generation evaluation ...
  </details>

- **2026-08-04** — Abdallah Khemais — [Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model](http://arxiv.org/abs/2608.03629v1)
  <details><summary>📄 Abstract</summary>
  A companion paper studies when activation patching and weight-space ablation agree, inside an idealized model where a conditional computation is carried additively through a residual stream. For the one composition in that model where two carriers are architecturally dependent, an attention head and its own layer's normalization-MLP composition, it derives an exact first-order interaction formula, zero when only the MLP is ablated and second-order bounded when the head is also ablated. That resu...
  </details>

- **2026-08-04** — Behzad Shomali, Markus Frey, David Berghaus et al. — [LoopMTP: A looped transformer guided by latent multi-token prediction](http://arxiv.org/abs/2608.03624v1)
  <details><summary>📄 Abstract</summary>
  Looped transformers have emerged as a parameter-efficient alternative to scaling depth for strong reasoning. By reusing one stack of layers across $T$ iterations, they attain the effective depth and reasoning capabilities of larger models at a fixed parameter count. Yet existing approaches suffer from latent overthinking and undifferentiated computation, largely because intermediate representations receive no guidance across loops. Multi-token prediction (MTP) supplies exactly the dense, forward...
  </details>

- **2026-08-04** — Qin Lei, Hao Wu — [Predictive Enhancement Calibration for Latent Breast MRI Virtual Contrast Enhancement](http://arxiv.org/abs/2608.03612v1)
  <details><summary>📄 Abstract</summary>
  Virtual contrast enhancement (VCE) synthesizes enhanced breast MR images from pre-contrast acquisitions. Modern latent generators offer strong image priors, but their bounded natural-image autoencoders conflict with the non-canonical intensity scale of MRI. We show that the upper bound can alter radiomic fidelity before generation, while scaling source and target independently creates a coordinate inconsistency. We propose Predictive Enhancement Calibration (PEC), which represents each pair in a...
  </details>

- **2026-08-04** — Han Wan, Rui Zhang, Hao Sun — [Large language models for partial differential equation workflows](http://arxiv.org/abs/2608.03600v1)
  <details><summary>📄 Abstract</summary>
  Partial differential equations (PDEs) become actionable in science and engineering not as isolated formulae, but as executable workflows that connect modelling assumptions, governing equations, numerical solvers, diagnostics, and decisions. Large language models (LLMs) are beginning to support such workflows by linking natural language, symbolic mathematics, code, solver outputs, and feedback. Here we examine recent advances in LLM-assisted PDE research across three stages: the discovery and for...
  </details>

- **2026-08-04** — Anton Sokolov — [A Challenge-Nonce Freshness Gap in Project Veraison's TPM Reference Schemes, Found by Appraising Application-Layer Action Evidence End-to-End](http://arxiv.org/abs/2608.03534v1)
  <details><summary>📄 Abstract</summary>
  When an automated agent (an AI agent, say) takes a consequential action, the record it leaves behind is produced by the very software stack whose integrity is in question. A signed log proves which key wrote the record, not what the runtime was. Prior work proposed treating that record (an Action Evidence Package, AEP: a signed append-only record of an action, its authorising principal, and its outcome) as application-layer Evidence under the IETF Remote ATtestation procedureS (RATS) architectur...
  </details>

- **2026-08-04** — Gagan Bhatia, Julian Schlenker, Simone Paolo Ponzetto et al. — [ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Levels](http://arxiv.org/abs/2608.03507v1)
  <details><summary>📄 Abstract</summary>
  Historical language change affects morphology, syntax, semantics, and pragmatics, yet computational studies typically examine these levels with incompatible representations and therefore cannot determine whether they evolve together across languages. We address this problem by asking how the magnitude and direction of change vary across linguistic levels, languages, and historical periods within a single analytical space. We introduce ChronoLens, a framework that combines frozen multilingual lan...
  </details>

- **2026-08-04** — Minghui Liwang, Wenhan Jia, Xinlei Yi et al. — [Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration](http://arxiv.org/abs/2608.03408v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of low-altitude intelligent agents is increasing the demand for timely and socially responsible collaborative sensing in dynamic urban environments. However, jointly addressing heterogeneous spatiotemporal demands, environmental uncertainty, and human-centered operational constraints remains challenging. This paper studies 3D multi-UAV path planning and task assignment under uncertain ground PoI demands. Unlike existing work assuming static and fully known PoIs, we model persis...
  </details>

- **2026-08-04** — Xiaolin Chen, Xuemeng Song, Wenhao Shi et al. — [ArtECulture: Benchmarking Culture-Conditioned Visual Emotion Understanding in Multimodal Large Language Models](http://arxiv.org/abs/2608.03358v1)
  <details><summary>📄 Abstract</summary>
  Existing visual emotion understanding methods typically ignore cultural variations in emotional perception. We introduce culture-conditioned visual emotion understanding, a task that predicts the culture-specific emotional perception of a given image and explains the underlying rationale. Although related benchmarks exist, they are limited by inconsistent individual annotations, which hinder the derivation of majority-supported culture-level emotion labels, and imbalanced cultural coverage. Thus...
  </details>

- **2026-08-04** — Fang Li, Yu He, Haoyang Tong et al. — [iFAN: Inference-Aware Learning for Plain Mask Transformers](http://arxiv.org/abs/2608.03216v1)
  <details><summary>📄 Abstract</summary>
  Query-based mask transformers assemble segmentation outputs through pixel-wise competition among query predictions of the final layer, yet this inference process is not explicitly optimized during training. We identify two key mismatches: the query with the highest probability-mask score does not necessarily produce the most accurate mask, and final-layer decoding may discard superior predictions from intermediate layers. To address these issues, we propose Inference-Aware Learning (iFAN), a gen...
  </details>

- **2026-08-04** — Unggi Lee, Sookbun Lee, Yeil Jeong et al. — [EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners](http://arxiv.org/abs/2608.03206v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) power educational applications from tutoring to essay scoring, but each is a point solution to a single task, and only recently have these point solutions been integrated into agents operating over a learning management system (LMS). Yet tutoring is long-horizon, since a learner improves over days and weeks rather than in a single turn, and no benchmark evaluates an agent tutor across a sustained relationship. We introduce EduClaw-Bench, a benchmark that places an ag...
  </details>

- **2026-08-04** — Yantong Liu, Zheyu Zhang, Runpeng Liu et al. — [NeuroMosaic: Anatomically Grounded Multimodal Large Language Modeling for Molecularly Aware Glioma Reasoning from 3D MRI and Clinical Narratives](http://arxiv.org/abs/2608.03187v1)
  <details><summary>📄 Abstract</summary>
  Multimodal medical large language models remain structurally weak for neuro-oncology because volumetric evidence is compressed into generic visual tokens and diagnostic conclusions often lack an auditable link to MRI regions. We present NeuroMosaic, a 3D multimodal language model that converts multi-sequence brain MRI into anatomy-indexed regional tokens, aligns them with clinical narrative and molecular concepts, and generates evidence-linked outputs. The architecture combines a multi-resolutio...
  </details>

- **2026-08-04** — Xiaonan Xu, Wenjing Wu — [Test-time reasoning effort and unauthorized tool use in language-model agents: a prespecified equivalence study](http://arxiv.org/abs/2608.03169v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents that execute multi-step workflows through tool calls operate under access-control policies that restrict which operations each role may perform. The APIs serving these agents expose a reasoning-effort parameter that operators adjust for cost and latency. Whether this parameter also changes the rate of unauthorized tool use has not been tested by direct manipulation within a single model. We vary reasoning effort (low, max) inside GPT-5.6 across the 14 confirmatory scenarios...
  </details>

- **2026-08-04** — Abdulrahman AlRabah, Weijian Zhou, Xing Gao et al. — [From SQL Errors to Concept Gaps: An AI-Powered Knowledge Graph Analytics Platform for Personalized Feedback](http://arxiv.org/abs/2608.03118v1)
  <details><summary>📄 Abstract</summary>
  This innovative practice full paper describes an AI-powered knowledge graph platform that connects SQL errors to conceptual gaps in undergraduate and graduate database systems courses. Students learning Structured Query Language (SQL) frequently struggle with semantic errors that reflect conceptual misunderstandings rather than syntax mistakes. A query may execute yet return incorrect results due to gaps spanning related concepts; misusing NATURAL JOIN in place of an explicit subquery reflects i...
  </details>

- **2026-08-04** — Mengjie Zhang, Qihui Zhu, Tao Zhang et al. — [GSTEP: Global Spatio-Temporal Density-Driven Visual Token Pruning for Efficient Video Large Language Models](http://arxiv.org/abs/2608.03083v1)
  <details><summary>📄 Abstract</summary>
  Video large language models (VideoLLMs) achieve strong video understanding performance, but their inference remains expensive due to the large number of redundant spatio-temporal visual tokens in long videos. Existing token pruning methods alleviate this cost by reducing redundant tokens, yet most of them rely on segment-level local pruning, where videos are partitioned into isolated segments and tokens are selected independently within each segment. Such designs may under-preserve short but sem...
  </details>

- **2026-08-04** — Yongshi Ye, Biao Fu, Chongxuan Huang et al. — [PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation](http://arxiv.org/abs/2608.03077v1)
  <details><summary>📄 Abstract</summary>
  Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation steps, but our analysis across 15 domains and four translation directions shows that this explicit reasoning is double-edged: it improves long-form and high-difficulty translation, yet often drifts in t...
  </details>

- **2026-08-04** — Jiayu Cao, Xingyuan Zeng, feiyu Li et al. — [UrbanAgent: A Tool-Augmented Agent for Cross-System Urban Tasks](http://arxiv.org/abs/2608.03018v1)
  <details><summary>📄 Abstract</summary>
  Modern cities rely on an increasing number of digital services to operate, but residents' daily needs are still difficult to meet. Services are fragmented and have little interoperability, placing a heavy operational burden on users. Existing digital platforms, urban foundation models, and intelligent assistants each address only isolated aspects of an urban task. But they struggle to reliably convert complex natural-language requests into executable cross-system workflows. We propose Urban-Agen...
  </details>

- **2026-08-04** — Molood Arman — [When Outputs Disperse, Does Epistemic Revision Follow? A Black-Box Coupling Diagnostic for Machine Collectives](http://arxiv.org/abs/2608.03722v1)
  <details><summary>📄 Abstract</summary>
  Collective intelligence research treats disagreement as evidence of epistemic diversity: if agents express different views, the group should retain capacity to revise. In LLM collectives this proxy can break: agents can produce diverse-looking arguments while preserving the same conclusion. We operationalize dispersion-revision coupling: the degree to which an intervention that verifiably increases the dispersion of a collective's outputs in embedding space is accompanied by genuine revision of ...
  </details>

- **2026-08-04** — Klaas De Kinder, Amir Bahrami, Christophe Caloz — [Space-Time Event Scattering and Extension Method (STESEM): A Universal Framework for Scattering in Space-Time Metamaterials](http://arxiv.org/abs/2608.03333v1)
  <details><summary>📄 Abstract</summary>
  Space-time metamaterials offer unprecedented control over electromagnetic waves by enabling simultaneous manipulation of spatial and temporal degrees of freedom. However, analytical descriptions of their scattering processes remain fragmented, with existing approaches typically requiring configuration-specific derivations or transformations to specialized reference frames that become impractical for accelerated or multi-interface structures. In this tutorial, we introduce the space-time event sc...
  </details>

- **2026-08-04** — Jiyong Kwon, Yikun Bai, Amirhossein Mollaali et al. — [GraspMeanFlow: SE(3)-Equivariant MeanFlow for Few-Step 6-DoF Grasp Generation](http://arxiv.org/abs/2608.03295v1)
  <details><summary>📄 Abstract</summary>
  Recent data-driven methods for synthesizing 6-DoF grasp poses use generative models to learn complex grasp pose distributions and generate diverse candidate poses. In particular, SE(3)-equivariant flow-based models generate grasp poses that transform consistently with object rotations and translations. However, these methods sample by iterative numerical integration, requiring tens of function evaluations per grasp and limiting their use in real-time manipulation. We propose GraspMeanFlow, an SE...
  </details>

- **2026-08-04** — Shuo Ren, Yaohui Han, Libo Shen et al. — [AgenticECO: An Agentic Framework for ECO on 3D Integrated Circuits](http://arxiv.org/abs/2608.03738v1)
  <details><summary>📄 Abstract</summary>
  As Moore's law slows, the industry is turning to three-dimensional integration; yet in merged 3D-IC flows, routed designs expose bond-level defects with no 2D analogue, and post-route engineering change orders (ECO) remain manual, expertise-bound work. Worse, the standard edit-then-fully-reroute practice entangles a repair with router churn, so a signoff number cannot be attributed to the edit that motivated it. We present AgenticECO, an evidence-gated tool-using agent workflow for 3D-IC ECO on ...
  </details>

- **2026-08-04** — Denys Pushkin, Albert Q. Jiang, Aryo Lotfi et al. — [Soft Guidance Starts to Outperform CoT Prompting as LLMs Improve](http://arxiv.org/abs/2608.03550v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting remains the standard baseline for evaluating models' reasoning abilities. Originally, this technique was introduced to elicit step-by-step reasoning from large language models (LLMs), which would otherwise tend to directly output the final answer. However, many modern LLMs produce CoT-style responses \textit{natively} when presented with reasoning tasks, which made us revisit the effectiveness of standard CoT prompting.   We evaluate several modern mid-sized lang...
  </details>

- **2026-08-04** — Fengjunjie Pan, Alois Knoll — [Dr. AGENTONOMICS: A Didactic Experiment of AGENTONOMICS](http://arxiv.org/abs/2608.03524v1)
  <details><summary>📄 Abstract</summary>
  AGENTONOMICS is a framework that treats AI agents as economic entities that can be designed, managed, and governed through an integrated management architecture. Dr. AGENTONOMICS is its first application: a lecture agent developed in the context of the TUM course on AI agents in business administration. Conceived during the winter semester 2025/26 and first introduced to students in the summer semester 2026, it serves as a didactic experiment in which the agent is both the object that students s...
  </details>

- **2026-08-04** — Xiuyuan Zhu, Ke Lu, Kun Dong et al. — [Hi-Token: Hierarchical Coordinate Tokenization for Generative Visual Grounding](http://arxiv.org/abs/2608.03471v1)
  <details><summary>📄 Abstract</summary>
  Generative Vision-Language Models (VLMs) commonly treat bounding-box coordinates as independent output symbols, leaving numerical order and axis semantics implicit. We identify this representation as an important source of error in visual grounding. Hi-Token encodes each coordinate with axis-specific tokens for the hundreds, tens, and ones digits, which adds coarse-to-fine structure and increases token reuse while retaining the existing VLM architecture. Hi-GAR complements this representation wi...
  </details>

- **2026-08-04** — Zhenghan Chen, Zekai Shao, Lidan Tan et al. — [ChartAnno: Evaluating MLLMs for Chart Annotation Generation](http://arxiv.org/abs/2608.03464v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made significant progress in chart understanding, generation, and editing, but their ability to annotate existing charts remains underexplored. Annotating charts is a common yet challenging communicative task, requiring models to infer intended messages, interpret chart semantics, and place appropriate textual or graphical elements. To address this gap, we introduce ChartAnno, a benchmark for evaluating MLLMs on chart annotation generation. It contai...
  </details>

- **2026-08-04** — Xingyang Yu — [3D Gravity Does Not Average Like Narain at Genus One: Rigidity of Virasoro Topological Boundaries](http://arxiv.org/abs/2608.03459v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the proposed relation between 3D gravity and the doubled Virasoro TQFT, and by the associated program of ensemble holography, we ask whether ensemble holography in AdS$_3$/CFT$_2$ can be understood as an average over absolute 2D CFTs obtained by varying the topological boundary condition of the doubled Virasoro TQFT. We show that, at genus one and in the ordinary nondegenerate sector, every vacuum-normalized, modular-invariant genus-one pairing that acts boundedly on the auxiliary $...
  </details>

- **2026-08-04** — Matteo Morini, Pietro Terna — [A Note on Reinforcement Learning to Develop Self-defined Agents' Behavior](http://arxiv.org/abs/2608.03445v1)
  <details><summary>📄 Abstract</summary>
  The key point in this note is the self-development of simple behavior strategies, consistently with the bounded rationality hypothesis. Our artificial agents adopt learning techniques, mainly unsupervised, to achieve internal consistency in their behavior, with unexpected results. Those results can be considered mainly as the effects of the observer interpretation. The first technique in use has the name Cross Targets: to train the learning agent we use data crossed between the guesses about the...
  </details>

- **2026-08-04** — Jakub Rada, Viliam Lisý — [Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory](http://arxiv.org/abs/2608.03420v1)
  <details><summary>📄 Abstract</summary>
  Large language models have improved substantially on single-shot reasoning tasks, but their performance in sequential decision-making is less well understood. We study this on fully-observable two-player zero-sum games, which provide ground-truth evaluation: outcomes are determined by the rules, and optimality of individual moves can be computed or approximated, without relying on a judge model. Across model tiers, LLMs play suboptimally in simple games such as tic-tac-toe or Connect Four, and l...
  </details>

- **2026-08-04** — Adam J. Stewart, Heng Fang, Isaac A. Corley et al. — [Earth Embeddings](http://arxiv.org/abs/2608.03410v1)
  <details><summary>📄 Abstract</summary>
  Earth observation is moving from foundation models that users must run themselves toward embedding products that package model feature outputs as reusable data without needing to download and process the imagery used to generate them. Earth embeddings are vectors that summarize locations, image patches, or pixels, letting users analyze compact features instead of repeatedly training or running large models on raw satellite imagery. This chapter explains the main types of Earth embeddings, from i...
  </details>

- **2026-08-04** — S. Miret-Artés — [The intermediate scattering function of an interacting adlayer as a characteristic function: a closed-form theory of Ising lattice-gas surface diffusion](http://arxiv.org/abs/2608.03398v1)
  <details><summary>📄 Abstract</summary>
  The intermediate scattering function (ISF) measured by helium spin-echo is a characteristic function (CF): the Fourier transform of the distribution of adsorbate displacements, whose value at zero time is the static structure factor. We use this double role to bring lateral interactions of Ising lattice-gas type into surface diffusion. The ISF then follows in closed form in momentum transfer, time, coverage and temperature, and with it the whole linear-response hierarchy. A single correlation pa...
  </details>

- **2026-08-04** — Shahrukh Mohiuddin, Chalamalasetti Kranti, Sherzod Hakimov et al. — [Don't Let Me Ask for It: LLMs Show Deficiencies in Active Multi-Turn Information Acquisition for Abductive Inference](http://arxiv.org/abs/2608.03388v1)
  <details><summary>📄 Abstract</summary>
  Abductive reasoning requires forming hypotheses that explain observed evidence and revising them as new evidence becomes available. While large language models (LLMs) are often evaluated on whether they solve abductive reasoning tasks correctly, less is known about how they acquire evidence, update their hypotheses, and decide when to stop. We introduce Alien Abduction game, an interactive probe for studying these behaviours under different interaction modes. The modes vary in whether evidence i...
  </details>

- **2026-08-04** — Xi Liu, Wenxi Fang, Ken Perlin — [Organic liquid scintillator neutrino detector experiment, theoretical modeling, and computational simulation](http://arxiv.org/abs/2608.03359v1)
  <details><summary>📄 Abstract</summary>
  The Liquid Scintillator Neutrino Detector (LSND) experiment aimed at investigating neutrino oscillations, particularly the transformation of muon-type antineutrinos (\(\overlineν_μ\)) into electron-type antineutrinos (\(\overlineν_e\)). This phenomenon challenges the Standard Model's assumption of massless neutrinos. The LSND employed a large organic liquid scintillator (LS) to detect low-energy neutrino interactions, enhanced by the addition of metal ions such as gadolinium (Gd) for improved si...
  </details>

- **2026-08-04** — Junhyeok Kang, Sangjun Han, Hyeokjun Choe et al. — [Traceable Multi-Agent System for Knowledge-Based Forecasting](http://arxiv.org/abs/2608.03339v1)
  <details><summary>📄 Abstract</summary>
  Enterprise forecasting increasingly relies on autonomous agents that interpret documents, search for data, generate code, and revise models. While this autonomy helps build adaptive forecasting pipelines, it also makes it difficult for practitioners to inspect why a forecast changed, which evidence supported the change, and how data and modeling choices were revised. We present TraceMAS, an interactive demo system for traceable multi-agent forecasting. TraceMAS organizes agent outputs around two...
  </details>

- **2026-08-04** — Sunyeop Kim, Insung Kim, Jian Guo — [Provably Learning Multi-Head Attention with Queries](http://arxiv.org/abs/2608.03294v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of learning multi-head softmax attention from black-box input-output access. The learner may query arbitrary real-valued token sequences and observe only the scalar output at the final token. Recent work gives an algorithm using $O(d^2)$ value queries to recover the single-head parameters $(W,v)$. For multiple heads, the same work establishes identifiability under the assumption that the heads occupy pairwise orthogonal subspaces. Applying the single-head recovery algorithm ...
  </details>

- **2026-08-04** — Changqing Zhou, Yueru Luo, Zeyu Jiang et al. — [UniNav: A Unified World-Action Diffusion Model for Visual Navigation](http://arxiv.org/abs/2608.03244v1)
  <details><summary>📄 Abstract</summary>
  Image-goal visual navigation is a fundamental capability for embodied agents. Existing navigation policies efficiently predict waypoint trajectories but lack visual foresight, while navigation world models can anticipate future observations but often require costly planning rollouts. We present UniNav, a unified world-action model that generates future visual observations and continuous waypoint trajectories through a single diffusion process. Given history frames and a goal image, UniNav jointl...
  </details>

- **2026-08-04** — Savvas Panagi, Chrysovalantis Spanias, Petros Aristidou — [Dynamic Flexibility Requests in Local Flexibility Markets: Quantifying the DSO Willingness to Pay](http://arxiv.org/abs/2608.03226v1)
  <details><summary>📄 Abstract</summary>
  Local Flexibility Markets (LFMs) require Distribution System Operators (DSOs) to determine both the quantity of flexibility to procure and the corresponding willingness to pay during market clearing. Existing approaches typically rely on unrealistic centralized AC-OPF clearing algorithms or strictly localized, static flexibility requests driven primarily by congestion management, while the economic value of flexibility is largely neglected. This paper proposes a dynamic flexibility-request metho...
  </details>

- **2026-08-04** — Aye Aye Maung, Qi Zheng — [Evaluating Treatment Effects using Group Testing with Retesting of Positive Groups](http://arxiv.org/abs/2608.03224v1)
  <details><summary>📄 Abstract</summary>
  Group testing is an established, highly cost-effective strategy for population-level disease surveillance that identifies positive individuals by pooling biological specimens. Originally introduced during World War II for large-scale screening and heavily utilized in modern high-throughput public health infrastructure, traditional group testing methods are restricted to purely associational analyses. Consequently, they lack the capacity to infer the direct causal effect of an intervention when i...
  </details>

- **2026-08-04** — Thanasis Lianeas, Alkmini Sgouritsa, Minas Marios Sotiriou — [EFX Allocation In (Multi)Hypergraphs](http://arxiv.org/abs/2608.03171v1)
  <details><summary>📄 Abstract</summary>
  We study fair allocations of indivisible goods among agents with heterogeneous monotone valuations. As fair we consider the allocations that are envy-free-up-to-any-good (EFX). Finding if EFX alloca- tions always exist, even for agents with additive valuations, is a major open problem in Fair Division. Christodoulou et al. (2023) introduced the (multi-hyper)graph setting, where agents and goods are represented by vertices and edges of a graph, respectively, and only the endpoints of an edge may ...
  </details>

- **2026-08-04** — Tu Tran Do, Nhat Ngoc Nguyen, Khanh-Tung Tran et al. — [VIVID: A Culturally Grounded Benchmark Exposing the Figurative Language Gap in Vietnamese NLP](http://arxiv.org/abs/2608.03095v1)
  <details><summary>📄 Abstract</summary>
  We present VIVID (Vietnamese Idioms for Validation and Interpretation Depth), the first systematic benchmark for evaluating culturally grounded figurative language understanding in Vietnamese. VIVID comprises 1,636 idioms and proverbs annotated with five complexity traits (literal expressions, pragmatic nuances, Sino-Vietnamese terms, uncommon vocabulary, folk knowledge) and seven semantic themes. We establish an evaluation framework combining generative and discriminative tasks, proposing an LL...
  </details>

- **2026-08-04** — Gongyue Zhang, Honghai Liu — [Joint Affine Spectral Shaping: Coupling Weight and Bias Updates Beyond Weight-Only Muon](http://arxiv.org/abs/2608.02991v1)
  <details><summary>📄 Abstract</summary>
  Matrix spectral optimizers reshape weight-update spectra but usually delegate vector-valued biases to a separate optimizer. We study whether this separation is neutral. We formulate each affine layer as a joint momentum matrix $A=[M_W,αm_b]$ and apply a capped regularized-inverse spectral map to the complete matrix, producing both the weight and physical bias updates. A strict five-seed ablation on a four-layer BERT-mini trained from scratch on IMDb compares exact-SVD Muon, weight-only inverse s...
  </details>

- **2026-08-03** — Malik Khalaf, Yara Shamshoum, Nitzan Hodos et al. — [AnchorKV: Anchor-Residual KV Cache Compression](http://arxiv.org/abs/2608.02901v1)
  <details><summary>📄 Abstract</summary>
  The key-value (KV) cache is the primary memory bottleneck in long-context LLM inference. Existing approaches attack it from opposite ends: eviction methods permanently discard tokens, degrading performance whenever a discarded token later proves essential, while quantization methods retain all tokens at low precision but offer limited compression. We propose AnchorKV, a compression scheme that shrinks the cache by $20\times$ without discarding a single token. AnchorKV represents the cache using ...
  </details>

- **2026-08-03** — Ioana Boureanu, R. Ramanujam, Srinibas Swain — [Decidability of Parameterised Dolev-Yao Secrecy](http://arxiv.org/abs/2608.02838v1)
  <details><summary>📄 Abstract</summary>
  We study the verification of parameterised secrecy for cryptographic protocols in the Dolev-Yao model, where the number of protocol sessions is unbounded and treated as a parameter. This differs fundamentally from classical Dolev-Yao secrecy, which asks whether a protocol leaks a secret irrespective of the number of executions; our question is whether secrecy holds uniformly across all system sizes, where such a size is a parameter. This parameterised perspective captures how attacks scale with ...
  </details>

- **2026-08-03** — Yinxiao Zhang, Sen Wang, Yi Gao — [Schedule-Informed Temporal Fusion Forecasting of Hourly Airport Security-Checkpoint Throughput](http://arxiv.org/abs/2608.02950v1)
  <details><summary>📄 Abstract</summary>
  Checkpoint staffing requires accurate forecasts of when screening demand will occur, yet flight schedules record departure times rather than passenger arrival times at security checkpoints. This study develops a framework that converts known flight schedules into temporally aligned signals for forecasting hourly checkpoint throughput. Using 2023-2024 Transportation Security Administration throughput data and Cirium Diio flight schedules for Hartsfield-Jackson Atlanta International Airport, domes...
  </details>

- **2026-08-03** — Xiaocheng Lu, Hualei Zhang, Shuhan Guo et al. — [OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models](http://arxiv.org/abs/2608.02942v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (dLLMs) can predict many tokens in parallel, but accurate generation still requires many iterative denoising steps. Few-step distillation accelerates decoding by compressing multiple teacher steps into a single student transition. However, existing methods construct supervision on off-policy trajectories. At inference, the student's early parallel commitments alter the context of later predictions, so the states it actually visits drift away from the supervised ones--pr...
  </details>

- **2026-08-03** — Bo Liu, Qiang Liu — [Maglev: Sliding Recurrent Memory](http://arxiv.org/abs/2608.02870v1)
  <details><summary>📄 Abstract</summary>
  We introduce \ours{}, a recurrent Transformer architecture with fixed-size memory that generalizes sliding-window attention while remaining parallelizable during training. \ours{} consists of two coupled models: a prefiller $Q$, which leverages full attention\footnote{In practice, we use interleaved full and sliding-window attention for $Q$, as this yields stronger performance. The essential requirement is that $Q$ be more expressive than $P$, with access to the full history.} to produce memory ...
  </details>

- **2026-08-03** — Maya Okawa — [Emergence of Biased Consensus in Multi-Agent LLM Debates](http://arxiv.org/abs/2608.02827v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM debates achieve strong performance on decision-making tasks as well as problem-solving benchmarks, yet their safety and fairness risks remain poorly understood. Notably, interaction can amplify the biases of single LLMs, raising concerns for real-world deployment. We identify the emergence of collective (often biased) norms in multi-agent LLM debates and show that noise (e.g., LLM sampling temperature) is a key driver. To explain this, we propose an analytical framework drawing o...
  </details>

- **2026-08-03** — Jiazhen Liu, Mingkuan Feng, Long Chen — [Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-Based Segmentation](http://arxiv.org/abs/2608.02791v1)
  <details><summary>📄 Abstract</summary>
  MLLM-based segmentation faces a core segmentation trilemma: high segmentation performance, preserved dialogue ability, and fast inference. Embedding-prediction methods may disrupt language modeling through pixel-level objectives, whereas next-token generation is inefficient for dense masks. We propose All-Mask Prediction, decoupling autoregressive dialogue from non-autoregressive mask prediction. Its binary instantiation, STAMP (Simultaneous Textual All-Mask Prediction), emits an in-vocabulary <...
  </details>

- **2026-08-03** — Xinjie Yao, Xingxin Xu, Xiyuan Gao et al. — [Towards a new paradigm of scientific discovery with socialized artificial intelligence](http://arxiv.org/abs/2608.02775v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery has advanced through successive transformations in the organization of knowledge. Observation and experimentation established the empirical foundations of science. Theory made it possible to derive general principles from particular phenomena. Computation extended inquiry into systems beyond direct observation, while data-intensive methods opened new spaces of pattern and prediction. Science now confronts a different frontier. The central challenge is no longer simply to pro...
  </details>

- **2026-08-03** — Hongjie Zhou, Shiqin Wang, Haoyang Chen et al. — [RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?](http://arxiv.org/abs/2608.02039v2)
  <details><summary>📄 Abstract</summary>
  Remote-sensing videos enable real-time observation of changes in target attributes, short-term activities, and scene evolution. They record motion, actions, interactions, and scene changes that cannot be captured by isolated images. Existing models primarily target single images or discrete temporal observations spanning a long time range. However, a unified evaluation setting for assessing vision-language models on continuous remote-sensing video understanding remains lacking. We introduce RSVi...
  </details>

- **2026-08-03** — Zetong Xiong, Qiao Zhao, Jun Zhang et al. — [BulkPR-Bench: Benchmarking Queue-Level Governance of Interacting Pull Requests](http://arxiv.org/abs/2608.02685v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent benchmarks increasingly cover long-horizon, end-to-end, and interactive development, but typically retain one requested outcome or a fixed change sequence. Sequential policies can process a pull-request (PR) queue one candidate at a time, but when queued PRs interact, maximizing safe delivery can require jointly deciding which changes to merge and in what order. We introduce BulkPR-Bench, an executable benchmark in which an agent must recover consequential PR relations and return a ...
  </details>

- **2026-08-03** — C. Alexander Rodriguez — [Non-Abelian Hirota-Miwa Equations for the KPZ Universality Class](http://arxiv.org/abs/2608.02772v1)
  <details><summary>📄 Abstract</summary>
  This work introduces an algebraic framework yielding explicit, closed matrix differential-difference equations for eighteen models in the exactly solvable sector of the KPZ universality class across four scaling regimes. By organizing Fredholm determinant data into an overdetermined linear problem on a directed lattice graph, we derive a compatibility system termed the diamond equations. Elementary seed data extracted from the shift structure of the Fredholm kernel provides simple solutions to t...
  </details>

- **2026-08-03** — Yu Yang, Xuemeng Yang, Licheng Wen et al. — [Quo Vadis, World Modeling?](http://arxiv.org/abs/2608.02713v1)
  <details><summary>📄 Abstract</summary>
  Continually improving agents require dynamic interaction feedback beyond static supervision, yet direct real-environment interaction is costly, slow, unsafe, and hard to parallelize. World modeling offers a natural intermediate proxy that allows agents to query lower-cost, more controllable feedback before committing to real actions. Classical world models instantiate this proxy primarily through future physical-state prediction, a formulation useful yet narrow for agents that require actionable...
  </details>

- **2026-08-03** — Dorieh Alomari, Irfan Ahmad, Maged S. Al-shaibani — [Character Iconicity vs. Arbitrariness: An Arabic NLP Perspective](http://arxiv.org/abs/2608.02935v1)
  <details><summary>📄 Abstract</summary>
  Arabic script uses 28 letters, many of which share a common base shape (rasm) and are distinguished only by dot placement. Because early Arabic manuscripts were written without dots yet remained interpretable, dot removal offers a natural test of whether these visual distinctions are functionally necessary. Prior work has shown that dotless Arabic can remain readable and effective for natural language processing (NLP), but it remains unclear whether this success depends on preserving the origina...
  </details>

- **2026-08-03** — Nathan Canen, Ted Enamorado — [When Predictions Become Regressors: A Split-Sample Correction for Biases in Downstream Inference](http://arxiv.org/abs/2608.02909v1)
  <details><summary>📄 Abstract</summary>
  Prediction-based methods, including Large Language Models (LLMs) and other machine learning techniques, are often used to construct measures of political phenomena that are difficult to quantify directly, such as policy positions in manifestos or emotions expressed on social media. In many applications, these prediction-generated measures are used as explanatory variables in regression models, even though they are measured with error. This leads to biased estimates. In this paper, we propose a s...
  </details>

- **2026-08-03** — Johanna Borissova — [Formation of extremal regular black holes](http://arxiv.org/abs/2608.02908v1)
  <details><summary>📄 Abstract</summary>
  Static and slowly evolving regular black holes with a non-extremal inner horizon are generally expected to suffer from mass inflation. Here we consider the scenario of asymptotic gravitational collapse into extremal regular black holes as candidate eternal endpoints. To that end, we first construct geometric models of static spherically symmetric single-horizon extremal and double-horizon inner-extremal regular black holes for generic black hole mass as the only dimensionful scale. These spaceti...
  </details>

- **2026-08-03** — Osman Ergeç — [Supersymmetric Twisted Carroll Theories](http://arxiv.org/abs/2608.02890v1)
  <details><summary>📄 Abstract</summary>
  We study the recently discussed $2+1$-dimensional Hull-type twisted $\mathcal{N}=2$ Carroll superalgebra. This structure admits both electric- and magnetic-type realizations at the level of the supersymmetry transformations. At the Lagrangian level, magnetic Carroll theories describe fields that propagate in space while remaining constrained in time, and vice versa for electric theories. We first realize this symmetry algebra through the dimensional reduction of a $2+2$-dimensional $\mathcal{N}=...
  </details>

- **2026-08-03** — Nitish Nagesh, Elahe Khatibi, Thomas Dean Hughes et al. — [GoT-CD: Graph-of-Thoughts Causal Discovery and the Fragility of Post-hoc Path-Specific Fairness Audits](http://arxiv.org/abs/2608.02877v1)
  <details><summary>📄 Abstract</summary>
  Causal discovery recovers directed structure from observational data and is increasingly used in clinical settings to support mechanism reasoning and fairness audits of predictive models. Path-specific counterfactual fairness asks whether a protected attribute influences an outcome through illegitimate pathways, but these estimands are defined relative to a supplied causal graph and therefore inherit whatever errors the discovery step introduces. Discovery methods are routinely scored on aggrega...
  </details>

- **2026-08-03** — Abdallah Lamane, Abdul Rahman Diab, Ren-Chin Wu et al. — [SAGE: Semantic Explainability of Attention-Based Survival Models in Computational Pathology](http://arxiv.org/abs/2608.02803v1)
  <details><summary>📄 Abstract</summary>
  Attention-based multiple instance learning (ABMIL) is the predominant approach for slide-level prediction in computational pathology, yet its attention maps provide only local explanations: they indicate where a model focuses but not which histological features drive its predictions or how the model behaves across a patient cohort. We present Semantic Attention Global Explanations (SAGE), a post-hoc framework that extracts global, language-grounded explanations from a frozen ABMIL model. Using a...
  </details>

- **2026-08-03** — Zixuan Huang, Yang Zhou, Kaixuan Wang et al. — [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](http://arxiv.org/abs/2608.01755v2)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models for autonomous driving (AD) increasingly utilize chain-of-thought (CoT) supervision to enhance the reasoning capabilities of their Vision-Language Model (VLM) components, yet existing annotation pipelines commonly expose the teacher model to the logged ground-truth (GT) future trajectory. We empirically show that this induces trajectory anchoring bias: teacher models rationalize the revealed outcome rather than infer a decision from scene evidence, prod...
  </details>

- **2026-08-03** — Salma El Yadouni, Guanyi Li — [TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows](http://arxiv.org/abs/2608.02680v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents repeatedly rediscover procedures they have already executed, producing traces that mix reusable structure with retries, exploration, accidental ordering, and repeated lookups. We present TraceCompiler, a skill-guided system that mines clusters of noisy agent traces and compiles them into executable, mostly deterministic workflows. It admits an inter-tool dependency only when a consumer argument contains a value attributable uniquely to an earlier producer; every ...
  </details>

- **2026-08-03** — Yiran Gao, Tao Li, Kim Hammar — [Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning](http://arxiv.org/abs/2608.02422v1)
  <details><summary>📄 Abstract</summary>
  Incident response is currently managed by security operators using predefined playbooks, resulting in slow, labor-intensive security decision-making processes. Consequently, there is a growing need for automated incident response planning. Decision-theoretic approaches based on control, optimization, and reinforcement learning have been proposed to automate such planning tasks with well-grounded approaches, yet most of which, while guaranteeing strong performance, are limited to abstract models ...
  </details>

- **2026-08-03** — Ting-Jui Chang — [A Spectral Filtering Approach to Regret Analysis of Distributed Online Control for Linear Dynamical Systems](http://arxiv.org/abs/2608.02375v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the distributed online control problem over a network of linear time-invariant (LTI) systems in the presence of adversarial disturbances and time-varying convex costs. The network cost is characterized by the summation of local cost functions, where each local function is sequentially revealed only to the corresponding agent. The goal of each agent is to generate a control sequence, using only local observations and neighbor communication, that competes with the best {\it cent...
  </details>

- **2026-08-03** — Dunjie Lu, Shuai Bai, Tianyi Bai et al. — [Qwen-CUA: Native Computer Use for (almost) Everything](http://arxiv.org/abs/2608.02352v1)
  <details><summary>📄 Abstract</summary>
  Native computer use offers a general interface for agents to operate almost any software available to people, but requires long-horizon state tracking, large-scale interactive experience, and learning from sparse yet verifiable outcomes. We introduce Qwen-CUA, a native computer-use agent with a 397B-A17B Qwen mixture-of-experts backbone. It observes only screenshots and acts through keyboard and mouse events, without DOM trees, accessibility metadata, or task-specific APIs. Its scaffold maintain...
  </details>

- **2026-08-03** — Jingxi Wei — [Trajectories That Segment Themselves: Agent-Declared Boundaries as a Training Unit](http://arxiv.org/abs/2608.02302v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding-agent trajectories are poorly matched to the credit units available to train on: a single action has no stable value, an episode label merges productive exploration with abandoned directions, and a fixed window cuts where the logging mechanics fall. We introduce collection-time semantic self-segmentation, in which a declarative contract has the acting agent expose its own boundaries while the trajectory is generated. Instantiated with falsifiable causal hypotheses, successive...
  </details>

- **2026-08-03** — K. Jack Scott, Narun Pat, Veronica Liesaputra — [Divergent large language model predictions from convergent representations in ambiguous word pairs](http://arxiv.org/abs/2608.01816v1)
  <details><summary>📄 Abstract</summary>
  In this work we investigate how decoder-only transformers resolve lexical ambiguity through layer-by-layer analysis of three models spanning three parameter sizes (GPT-2-Small-117M, Llama-3.2-3B, Qwen2.5-32B). For both homonyms and polysemes, we find that representations become maximally distinct in middle layers, then partially reconverge in late layers, while the KL divergence between their next-token predictions reaches its maximum in the final layers. The activation patching experiment provi...
  </details>

- **2026-08-03** — Shuyang Xie, Shuxiao Xie, Feng Zhu et al. — [Coding Agents as Test-Suite Auditors: Finding What Official Suites Miss While Approaching What They Catch](http://arxiv.org/abs/2608.01715v1)
  <details><summary>📄 Abstract</summary>
  Online-judge verdicts and the datasets and benchmarks built on them are treated as ground truth for evaluating and training large language models for code. Yet prior audits have sounded a warning: official suites accept buggy submissions. These audits, however, stop at the warning and offer no practical remedy. Our remedy has two parts: an off-the-shelf coding agent, serving as a test-suite auditor, both builds adversarial test suites to expose what official suites miss and supplies these suites...
  </details>

- **2026-08-03** — Jiajun Liang, Yucheng Liao, Yukang Cao et al. — [AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling](http://arxiv.org/abs/2608.02602v1)
  <details><summary>📄 Abstract</summary>
  Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity...
  </details>

- **2026-08-03** — Chunhao Cai — [A Response Calculus for Liouville Brownian Motion I: Simple Spectrum, Joint Eigenvalue Densities, and Ward Identities](http://arxiv.org/abs/2608.02459v1)
  <details><summary>📄 Abstract</summary>
  We develop a response calculus for Dirichlet Liouville Brownian motion under Cameron--Martin shifts of the Gaussian free field. On every bounded connected planar domain, without boundary regularity assumptions, we prove throughout the full subcritical range $0<γ<2$ that the generator has almost surely simple spectrum and that every finite vector of ordered eigenvalues has an absolutely continuous law. This resolves the open simple-spectrum problem for Dirichlet Liouville Brownian motion.   The c...
  </details>

- **2026-08-03** — Ambarish Govindarajulu Kaliamurthi, Kaikai Liu — [MoRAL: Sensor-Grounded BEV Reasoning for Compact VLMs toward Edge-Oriented Autonomous Driving](http://arxiv.org/abs/2608.02449v1)
  <details><summary>📄 Abstract</summary>
  Deploying vision-language models (VLMs) for safety-critical spatial reasoning on resource-constrained autonomous driving platforms requires both compact model size and reliable metric grounding. We present MoRAL (Multimodal Reasoning for Autonomous Language Models), a two-stage fine-tuning pipeline that teaches Cosmos-Reason2-2B to first read a physics-encoded Bird's Eye View (BEV) representation and then reason over it for driving decisions. The BEV image encodes LiDAR metric distance as color ...
  </details>

- **2026-08-03** — Jiaming Chen, Guoan Xu, Aoshen Huang et al. — [DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation](http://arxiv.org/abs/2608.02428v1)
  <details><summary>📄 Abstract</summary>
  Forecasting future states from video sequences is a critical challenge for autonomous robotic systems and a fundamental objective of world modeling. Prior generative methods operating at the pixel level inevitably overemphasize task-irrelevant details, leading to prohibitive computational overhead. While latent-based approaches attempt to mitigate this by predicting features directly, the persistent reliance on heavy decoders for state-to-task mapping remains a computational bottleneck. In this ...
  </details>

- **2026-08-03** — Hao Shen, Junyu Guo, Tian Cui et al. — [MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4](http://arxiv.org/abs/2608.02295v1)
  <details><summary>📄 Abstract</summary>
  We present MechGeo, a Mathlib native agentic framework that jointly addresses faithful autoformalization and certified proof construction for Euclidean geometry. In this framework, GeoFormalizer represents informal problems in GeoIR, deterministically translates them into Lean 4, and iteratively repairs candidate statements using structural diagnostics and semantic evaluation. GeoProver constructs geometric proof plans, derives intermediate lemmas, and selectively algebraizes suitable subgoals t...
  </details>

- **2026-08-03** — Abdul Kalam, Prasenjit Deb, Akitada Sakurai et al. — [Quantum computer-based simulation of Stark many-body localization in a 1D Fermi-Hubbard model](http://arxiv.org/abs/2608.02245v1)
  <details><summary>📄 Abstract</summary>
  Many-body localization (MBL) is a dynamical phenomenon that describes the non-ergodicity of isolated quantum many-body systems. In contrast to thermalization, this phenomenon leads to a long-lived memory of initial states of local systems and slow growth of entanglement. In this work, we study Stark MBL in a 12-qubit correlated fermionic system described by the one-dimensional Fermi-Hubbard model using Hamiltonian simulation on an IBM superconducting qubit quantum computer. To enable such a comp...
  </details>

- **2026-08-03** — Luciano Ciamarone, Dora Motèque, Marco Giordano — [Sounding Canvas: Embedding Algorithms in Networked, Sensorial Sound Art](http://arxiv.org/abs/2608.02219v1)
  <details><summary>📄 Abstract</summary>
  Sounding Canvas turns painting into a touch-responsive multimodal installation by embedding capacitive sensors, real-time decision models, and networking inside the canvas. Touches trigger spatialised sounds that appear to emanate from the painting itself. The work embeds algorithms physically, as sensing and computation concealed behind the artwork; perceptually, through an offline visual-to-sonic mapping that aligns a painting's features with sound descriptors; and performatively, through onli...
  </details>

- **2026-08-03** — Can Wang, Haoran Chen, Haowen Gao et al. — [From Simple QA to Deep Research: A Verifiable Benchmark Constructed through Iterative Task Evolution](http://arxiv.org/abs/2608.02163v1)
  <details><summary>📄 Abstract</summary>
  Deep research benchmarks require expert-level tasks and reliable evaluation grounded in task-specific knowledge. Existing benchmarks rely heavily on expert authoring or pre-existing human-authored materials, while fully automatic construction struggles to ensure consistent and traceable verification. To address this gap, we introduce a verifiable benchmark of 500 deep research tasks spanning 31 topics and 10 major categories, with three query forms designed to probe complementary capabilities re...
  </details>

- **2026-08-03** — Long Qian, Jiaqi Wei, Bingke Zhu et al. — [Messages, Not Tokens: Grounded Coresets for Faithful VLM Compression](http://arxiv.org/abs/2608.02134v1)
  <details><summary>📄 Abstract</summary>
  Modern vision language models (VLMs) turn high-resolution images into long sequences of visual tokens. Every token traverses the language decoder and persists in its prompt KV cache, inflating inference cost and motivating aggressive visual compression. Existing score-based methods assign each token an independent importance score and retain the Top-K. However, text queries consume collective, signed attention messages from the visual population, not isolated patches. Consequently, equally sized...
  </details>

- **2026-08-03** — Shuxiao Xie, Shuyang Xie, Yuan Cao et al. — [One QK Channel, Many Sources: Guarding Low-Precision Attention Collapse](http://arxiv.org/abs/2608.02091v1)
  <details><summary>📄 Abstract</summary>
  A bfloat16 transformer can train normally for many steps and then collapse abruptly. Distinct low-precision errors can trigger the same failure, leaving unclear whether each source needs its own repair or one shared route can be blocked. We isolate a reproduced GPT-2-class collapse to the streaming-softmax accumulator, where fp32 accumulation repairs it, and use the fault as an assay for moving controlled errors across sources. Errors placed outside attention still drive the same query-key (QK) ...
  </details>

- **2026-08-03** — Zitong Xu, Huiyu Duan, Xinyun Zhang et al. — [MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing](http://arxiv.org/abs/2608.02059v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in unified multimodal models have significantly improved text-guided image editing abilities. In particular, models such as Nano-Banana-Pro and GPT-Image-2 demonstrate emerging capabilities in multi-source image editing (MIE), including tasks such as object synthesis, person-background composition, and cross-image style fusion. However, existing benchmarks and image editing assessment (IEQA) methods remain primarily focused on single-image editing tasks and largely overlook the m...
  </details>

- **2026-08-03** — Hongjie Zhou, Shiqin Wang, Haoyang Chen et al. — [RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?](http://arxiv.org/abs/2608.02039v1)
  <details><summary>📄 Abstract</summary>
  Remote-sensing videos enable real-time observation of changes in target attributes, short-term activities, and scene evolution. They record motion, actions, interactions, and scene changes that cannot be captured by isolated images. Existing models primarily target single images or discrete temporal observations spanning a long time range. However, a unified evaluation setting for assessing vision-language models on continuous remote-sensing video understanding remains lacking. We introduce RSVi...
  </details>

- **2026-08-03** — Ruilin Xu, Junyi Li, Pengfei Chen et al. — [TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference](http://arxiv.org/abs/2608.01975v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication. Existing profilers expose raw timelines, while log-based diagnosis often misses cross-layer execution semantics and request-level structure. We present TELLER, a non-intrusive Trace- and Log-aware LLM inf...
  </details>

- **2026-08-03** — Adam Zahir, Vincent Lefebvre, Mark Angoustures et al. — [D-MUTRA: DLT-based MUTual Remote Attestation for Multi-Agent Systems](http://arxiv.org/abs/2608.01938v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) comprise autonomous software agents that collaborate to perform complex tasks in critical cyber-physical domains, including multi-robot coordination and the Industrial Internet of Things (IIoT). In such distributed environments, a compromised agent may execute modified software while appearing trustworthy, causing other agents to act on false information and corrupting the mission. Agents must therefore establish and maintain mutual trust throughout operation. Remote at...
  </details>

- **2026-08-03** — Glenn Matlin, Isaac Song, Anthony Wen-Ming Zang et al. — [No One Wins in Nuclear War: A Social Simulation of Military Decision-making](http://arxiv.org/abs/2608.01868v1)
  <details><summary>📄 Abstract</summary>
  WOPR is a social-simulation environment for studying how organizations make high-stakes decisions, built on a deterministic, replay-validated rules engine and using wargames as the vehicle. We instantiate it first with the published card game Nuclear War, traced against its published rules. We start with military decision-making because of its safety implications and because it needs further study, but the design is not specific to it: the decision-point contract that exposes the engine to agent...
  </details>

- **2026-08-03** — Dongwei Sun, Bowen Yao, Yujie Zhang et al. — [EchoChange: A Diffusion Language Model with Dual Pass Remasking for Factual Remote Sensing Disaster Change Captioning](http://arxiv.org/abs/2608.01856v1)
  <details><summary>📄 Abstract</summary>
  Bi-temporal remote-sensing disaster change captioning often needs to identify sparse and spatially localized changes across large pre- and post-event scenes and then translate them into coherent, factual descriptions. However, existing change captioning methods always follow an autoregressive decoding paradigm to generate the change description and thus an early misinterpretation of the changed object, event, or spatial relation becomes an irreversible premise for subsequent text, amplifying vis...
  </details>

- **2026-08-03** — Chunji Lv, Yangguang Wei, Junlin Liu et al. — [PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning](http://arxiv.org/abs/2608.01837v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have shown strong potential in complex interactive tasks, yet their reinforcement learning (RL) is often hindered by sparse rewards, as a long multi-turn trajectory may receive only a single outcome-level signal. On-policy self-distillation (OPSD) provides dense token-level supervision from a privileged teacher, but the teacher may not be reliable at every position. Existing methods commonly rely on isolated token-level discrepancies, which can be sensitive to noise, ...
  </details>

- **2026-08-03** — Priyashree Roy, Sujitha Martin, Mohammad Rostami et al. — [Can You Trust the Confidence? ConfBench for Vision-Language Models on Document Extraction](http://arxiv.org/abs/2608.01792v1)
  <details><summary>📄 Abstract</summary>
  Intelligent document processing (IDP) with vision-language models (VLMs) hinges on confidence scores trustworthy enough to route extractions between automation and human review. Existing document benchmarks are dominated by clean, high-quality samples, leaving low accuracy regions too sparse for calibration assessment. We introduce ConfBench, the first calibration-specific benchmark for key information extraction (KIE), built by applying 20 controlled degradation pipelines to a diverse document ...
  </details>

- **2026-08-03** — Xiang Xia, Cheng Yan, Yiming Zhang et al. — [REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models](http://arxiv.org/abs/2608.01784v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) models increase parameter capacity by activating only a small subset of experts for each token. This conditional-computation paradigm has enabled autoregressive language models to scale model capacity without a proportional increase in per-token computation. In diffusion language models (DLMs), however, each denoising forward jointly revisits all token positions despite their sharply different refinement demands, while the default fixed token-choice routing assigns them ...
  </details>

- **2026-08-03** — Shuntaro Aoki — [Primordial Correlators from a Kaluza-Klein Graviton Continuum](http://arxiv.org/abs/2608.01762v1)
  <details><summary>📄 Abstract</summary>
  Cosmological collider signals are usually discussed for isolated massive particles, whose exchange produces characteristic logarithmic oscillations in primordial correlators. In this work, we study how this signal is modified when the exchanged states form a continuous mass spectrum. We first develop a spectral representation for inflationary correlators mediated by a continuum field. In the soft limit, the non-analytic part of the seed function is expressed as a Fourier--Laplace transform of th...
  </details>

- **2026-08-03** — Siying Li, Ying Ni, Jie Sun et al. — [DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](http://arxiv.org/abs/2608.01761v1)
  <details><summary>📄 Abstract</summary>
  End-to-end (E2E) autonomous driving algorithms require rigorous closed-loop validation in simulation environments offering high visual fidelity, strong interactivity, and real-time performance. Existing approaches, from game engines to static neural rendering, inherently trade off these requirements and struggle with the dynamic scene composition essential for E2E testing. To bridge this gap, we propose a novel decoupled 3D Gaussian Splatting (3DGS) framework tailored for large-scale E2E evaluat...
  </details>

- **2026-08-03** — Hao Ye, Geoffrey Ye Li, Biing-Hwang Juang — [Ten Years of Deep Learning for Wireless Communications: From Learned Blocks to Deployable Wireless Intelligence](http://arxiv.org/abs/2608.01747v1)
  <details><summary>📄 Abstract</summary>
  Over the past decade, deep learning has evolved from a tool for replacing isolated wireless blocks into a broader methodology for developing wireless intelligence. This article traces that trajectory through three shifts: learning wireless functional modules, redesigning and re-normalizing communication goals, and enabling generalization under practical physical constraints. Together, these shifts advance the broader pursuit of communication anytime and anywhere, through any appropriate means. E...
  </details>

- **2026-08-03** — Jianyu Wu, Yizhou Wang, Encheng Su et al. — [DAPD: Dual-Anchored Policy Distillation](http://arxiv.org/abs/2608.01735v1)
  <details><summary>📄 Abstract</summary>
  On-policy (self) distillation (OPSD) is increasingly adopted for language-model post-training. It strengthens the teacher with privileged information but can induce a privilege illusion: the student learns privilege-dependent behavior it cannot reproduce from its inference-time context, yet behaves as if the training-time privileged information remained available, ultimately degrading performance. In this paper, we identify information asymmetry between the privileged teacher and the student at ...
  </details>

- **2026-08-03** — Hai Nguyen, Tung Vu, Cong Tran — [SpatialQuery: Benchmarking Geometry-Grounded Multi-Instance Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2608.01709v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong semantic understanding but remain unreliable in metric spatial reasoning, particularly when queries require comparing multiple instances of the same object category. We study this problem through the Closest-Instance Distance Query (CIDQ), where a model must identify the nearest visible candidate to a unique reference object and estimate their gravity-aligned floor-plane distance. We introduce SPATIALQUERY, a training- free framework for CIDQ reasonin...
  </details>

- **2026-08-03** — Walter P. Casas, Nelson L. S. da Fonseca, and Carlos A. Astudillo — [LLM-Driven Automated Reward Design for Reinforcement Learning-Based Routing in LEO Satellite Networks](http://arxiv.org/abs/2608.01649v1)
  <details><summary>📄 Abstract</summary>
  Routing in Low Earth Orbit (LEO) satellite networks is challenging due to highly dynamic topologies and spatio-temporal network conditions. Reinforcement Learning (RL) has emerged as a promising approach for adaptive routing; however, its performance critically depends on reward function design, which must balance objectives such as goodput and end-to-end delay. In practice, reward design remains a complex manual process requiring significant domain expertise and extensive trial-and-error. Recen...
  </details>

- **2026-08-03** — Tianle Liu, Youcheng Niu, Jing Zeng et al. — [A Forward-Inverse Dynamic Game Framework for Enhanced Multi-Agent Trajectory Planning](http://arxiv.org/abs/2608.01636v1)
  <details><summary>📄 Abstract</summary>
  This paper studies feedback Nash equilibrium (FBNE) seeking for multi-agent trajectory planning in nonlinear dynamical systems with unknown agents' objectives and state-dependent inter-agent coupling. While dynamic game theory provides a principled framework for such problems, existing approaches typically assume fully rational agents with known objectives or rely on fixed regularization, limiting their ability to capture bounded rationality and spatially varying interaction intensity in safety-...
  </details>

- **2026-08-03** — Zhen Liu, Wanqi Zhou, Shuanghao Bai et al. — [GraphIR: Architecture-Level Search States for LLM-Guided Neural Architecture Evolution](http://arxiv.org/abs/2608.01633v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) enable neural architecture search (NAS) directly over executable neural network programs. However, code-level flexibility does not provide the architecture state needed for effective mutation: LLMs must infer tensor dependencies, editable components, and compatibility constraints from implementation details. To address this representation mismatch, we propose GraphIR, an architecture-aware intermediate representation that supplements executable programs with a mutati...
  </details>

- **2026-08-03** — Haowei Liu, Jiamian Wang, Hsin-Tai Wu et al. — [HindSearch: Trajectory-Level Hindsight Critique for Search-Augmented Reinforcement Learning](http://arxiv.org/abs/2608.01597v1)
  <details><summary>📄 Abstract</summary>
  Search-augmented LM agents are typically trained with a binary exact-match reward, which throws away most of what a failed trajectory tells us about why it failed. We introduce HindSearch, a hindsight self-distillation procedure for GRPO: after each rollout, a frozen judge writes a short critique of every failed trajectory using the gold answer, and the critique supplies an auxiliary on-policy distillation signal on the student's search actions. On the standard seven-benchmark suite with Qwen2.5...
  </details>

- **2026-08-03** — Hector Zenil, Luan Ozelim — [Measuring in-context algorithmic reasoning in language models against an exact Bayes-optimal standard](http://arxiv.org/abs/2608.01575v1)
  <details><summary>📄 Abstract</summary>
  Whether large language models perform genuine algorithmic reasoning or mere pattern completion is hard to test, because most benchmarks lack a ground truth for correct inductive inference. We introduce F-ICL, an in-context-learning benchmark that supplies one exactly. Using the Turing-complete machine F, complement-symmetrised into sF to remove output-polarity bias, we exhaustively enumerate all 1.5 billion programs of length $L\le13$ and compute the Bayes-optimal posterior in closed form under ...
  </details>

- **2026-08-03** — Yuchao Hou — [FedWorld: Scope-Aware Federation of Agent World Models](http://arxiv.org/abs/2608.01561v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents learn world dynamics from local interaction experience to support subsequent planning and action selection. However, the experience available to a single client is often incomplete, which motivates sharing knowledge across clients. Existing federated methods mainly aggregate model parameters, while agent memory-sharing methods commonly pool trajectories, memories, or rules without checking whether they remain valid for each client. This assumption is problematic...
  </details>

- **2026-08-03** — Seongyoon Kim, Boryeong Cho, Jihwan Oh et al. — [Rethinking Personalized Reward Modeling for LLMs under Preference Heterogeneity via Group-Debiased Federated Learning](http://arxiv.org/abs/2608.01556v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly aligned to human preferences via reward modeling, but user preference data are sensitive and often cannot be centralized. Federated learning keeps such data local while learning a shared initial reward model, which is later personalized for each client through local fine-tuning. Because users often assign opposite labels to the same pair of responses, existing federated methods address preference heterogeneity by clustering similar clients and training one ...
  </details>

- **2026-08-03** — Gaetano Chiriaco, Luca Barco, Andrea Bragagnolo et al. — [GEOID-Flood: A Large-Scale Multi-Modal Benchmark Dataset for Flood Segmentation](http://arxiv.org/abs/2608.02315v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models aim to learn representations that transfer across regions and sensors, yet evaluating them on specific tasks requires large, high-quality, multi-modal benchmarks that measure how well such models extract value from data. Concerning flood mapping, existing datasets rarely combine bi-temporal SAR and co-registered optical imagery at scale, leaving the value of foundation models for this downstream task largely untested. We introduce GEOID-Flood, a large-scale multi-mod...
  </details>

- **2026-08-03** — Lingwei Dang, Shishuo Shang, Pan Liu et al. — [StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph Field](http://arxiv.org/abs/2608.01954v1)
  <details><summary>📄 Abstract</summary>
  Fixed-layout indoor furniture styling requires selecting assets that form a coherent room without changing the prescribed furniture categories, positions, orientations, or scales. Existing approaches typically retrieve each asset independently or rely on static local relations, making them prone to shape, material, and color conflicts after scene composition. We introduce StyleForge, a scene-level structured selection framework built on a dynamic hypergraph style field. A frozen multimodal large...
  </details>

- **2026-08-03** — Donglin Yang, Haoran Chen, Xingyu Chen et al. — [Learning Panorama-Aware VLA for Mobile Manipulation with Whole-Body Teleoperation](http://arxiv.org/abs/2608.02257v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation is a key capability for embodied intelligence, enabling robots to accomplish complex multi-stage tasks in open-world environments. However, mobile manipulation poses two key challenges for vision-language-action (VLA) policies: At the data level, the efficient collection of high-quality whole-body demonstrations demands the coordinated control of both the mobile base and the robotic arms; at the model level, existing VLA models predominantly rely on local camera observations,...
  </details>

- **2026-08-03** — Jin Cui, Yanbin Hu, Xinyue Long et al. — [Look Where It Matters: Adaptive Visual Refinement for Vision-Language-Action Models](http://arxiv.org/abs/2608.02197v1)
  <details><summary>📄 Abstract</summary>
  Visual representations of VLA models remain unreliable for spatially precise robotic manipulation. We uncover that vision encoders in VLAs also exhibit attention artifacts previously documented in generic Vision Transformers, and further show that, in embodied policies, these artifacts are closely associated with spatial perception capabilities acquired during post-training. As the encoder learns task-relevant information such as object location, depth ordering, and local geometry, limited globa...
  </details>

- **2026-08-03** — Jing Wu, Jianhua Wu, Jiayi Guan et al. — [SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models](http://arxiv.org/abs/2608.01899v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning. Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs' general-purpose capabilities after spatial fine-tuning. To this end, we propose a parameter-efficient \textit{\textbf{Spatio}-vision \textbf{L}anguage \textbf{M}odels (SpatioLM)}, that enhances spatial intelligence without extra 3D prior...
  </details>

- **2026-08-03** — Dongdong An, Pengjie Zhao, Yihao Huang et al. — [Uncovering and Mitigating Positional Blind Spots in Vision-Language-Action Models](http://arxiv.org/abs/2608.01573v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models achieve promising performance in robotic manipulation, typically measured by success rates aggregated over predefined object configurations, an evaluation that implicitly assumes spatially uniform competence across the workspace. However, this assumption does not hold: even with the instruction and every other scene factor held fixed, merely relocating a task-irrelevant distractor can sharply raise the failure probability within localized, spatially coh...
  </details>

- **2026-08-03** — Marta Garnelo, Wojciech M. Czarnecki — [Why Large Language Models Fail at Tabular Prediction](http://arxiv.org/abs/2608.02412v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become the default tool for a remarkable range of tasks, yet they have had conspicuously little success at one of the most common machine learning workloads: predictive analytics over tabular data. This gap is the founding premise of the fast-growing field of tabular foundation models, but the question of why generic LLMs fail has remained open. We study a frontier LLM in its purest inference regime - a single generation pass over a prompt containing the full tr...
  </details>

- **2026-08-03** — Sajjad Abdoli, Ghassan Al-Sumaidaee, Ahmad ElShiekh et al. — [Can Foundation Models Hear What Made That Sound? A Tiered Benchmark of Audio-Language Models and Traditional Classifiers for Closed-Set Sound Source Identification](http://arxiv.org/abs/2608.02397v1)
  <details><summary>📄 Abstract</summary>
  We benchmark eleven audio classification methods: five task-aware closed-set LLMs (four Gemini models plus open-weight Kimi-Audio-7B-Instruct), four fixed-vocabulary taggers (YAMNet, PANNs, Whisper-AT, and SSLAM), a zero-shot audio-text model (CLAP), and an audio-grounded LLM (BAT). We evaluate them on a closed-set sound-source identification task over 2,242 clips spanning 23 fine-grained classes and 11 categories. Since these methods differ fundamentally in how they receive the task and how out...
  </details>

- **2026-08-03** — Alejandro Velasco, Daniel Rodriguez-Cardenas, Dipin Khati et al. — [ECLAIR: A Causally-Grounded AI Framework for Scientific Discovery in Empirical Software Engineering](http://arxiv.org/abs/2608.02323v1)
  <details><summary>📄 Abstract</summary>
  The scientific method has long guided empirical research in Software Engineering (SE), but the complexity of modern software systems often hinders its systematic application. This paper introduces _ECLAIR_, a causally grounded AI framework that integrates Large Language Models (_LLMs_) into every stage of the scientific process, from hypothesis generation to analysis and interpretation. _ECLAIR_ treats _LLMs_ as active **scientific agents** operating under the principles of causal inference, wit...
  </details>

- **2026-08-03** — Zhijian Zhou, Long Li, Xuan Zhang et al. — [Start Classifying: Categorical Critics for LLM Reinforcement Learning](http://arxiv.org/abs/2608.02181v1)
  <details><summary>📄 Abstract</summary>
  Proximal Policy Optimization (PPO) for large language models typically trains its critic by mean-squared-error (MSE) regression on scalar value targets. Although scalar MSE is statistically valid for estimating the conditional expected return, sparse binary rewards in reinforcement learning with verifiable rewards (RLVR) make critic optimization and calibration especially consequential: small value errors directly distort the scalar advantages used by PPO. We study whether a classification-based...
  </details>

- **2026-08-03** — Yijun Zhang, Yule Xie, Jiaxin Ding et al. — [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reasoning](http://arxiv.org/abs/2608.02149v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has become a central paradigm for improving the reasoning capabilities of large language models. Existing methods generally aim to reduce the failure probabilities induced across problems. In this paper, we introduce a moment-based perspective on policy optimization for LLM reasoning by treating the failure probability of a randomly sampled problem as a random variable and characterizing optimization objectives through its moments. Under this perspective, many existing met...
  </details>

- **2026-08-03** — Timur Mudarisov, Mikhail Burtsev, Radu State — [Feed-Forward Steering in Transformer Residual Dynamics](http://arxiv.org/abs/2608.02071v1)
  <details><summary>📄 Abstract</summary>
  Attention-only dynamical theories model Transformer residual directions as particles aggregating on a sphere. We extend this framework by incorporating the feed-forward network (FFN) term as a local steering field acting on each token state. The resulting theory predicts that the tangential component of the FFN field is necessary for motion in residual-direction space, that critical residual directions correspond to nonlinear projective equilibria, and that a commutator defect determines when a ...
  </details>

- **2026-08-03** — Avni Mittal, Avinash Anand, Ashutosh Kumar et al. — [TextNCA: Neural Cellular Automata for Language Modeling via Hierarchical Local Attention](http://arxiv.org/abs/2608.02050v1)
  <details><summary>📄 Abstract</summary>
  Can a strictly local, iterated, weight-shared computation primitive support language modelling, and which of those three properties actually drives the model's behaviour? We define \textsc{TextNCA}, a 1D causal windowed-attention realisation of the Neural Cellular Automaton primitive, and study a hierarchical variant that cascades three stages with windows $w \in \{8, 32, 128\}$ and $T_s$ shared-weight iterations per stage, all on WikiText-103 at roughly 30M parameters and 60k training steps. Th...
  </details>

- **2026-08-03** — Yixiao Qian, Song Chen, Pengkai Wang et al. — [DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling](http://arxiv.org/abs/2608.02032v1)
  <details><summary>📄 Abstract</summary>
  Modern language models are built primarily from Transformers, recurrent models, and their hybrid architectures. Transformers rely on token-level attention memories, while recurrent models such as state space models (SSMs) and linear attention maintain compact recurrent states. These architectures are typically instantiated separately or interleaved at the layer level, leaving open whether a shared memory representation can support both recurrent compression and attention-style retrieval. We stud...
  </details>

- **2026-08-03** — Kunal Kumar Pant, Nithin Nagaraj — [ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces](http://arxiv.org/abs/2608.01968v1)
  <details><summary>📄 Abstract</summary>
  Transformer models are most often understood through what they do: their benchmark performance, generation quality, or behavior on downstream tasks. Yet frozen transformer input-embedding spaces may also be examined through their responses to a controlled deterministic probe before contextual computation or task-specific adaptation. Guided by this response-based view, we introduce \emph{ChaosProbe}, a deterministic neurochaos-inspired method for constructing response-based fingerprints of frozen...
  </details>

- **2026-08-03** — Wenkai Li, Yuchao Wu, Ziyan Guo et al. — [LEAP: A Self-Supervised Per-Cycle Toggle Propagation Model Supports Fast, Transferable, and Early Analysis of Layout Power](http://arxiv.org/abs/2608.01946v1)
  <details><summary>📄 Abstract</summary>
  Accurate power analysis is critical in VLSI design, as it directly impacts power optimization strategies. However, traditional approaches are often hindered by the substantial runtime required for per-cycle toggle propagation in the netlist, which propagates register toggle information through combinational logic. To address this, we propose LEAP, the first work to enable per-cycle toggle propagation prediction with both high accuracy and efficiency. This is achieved through a novel, linear-comp...
  </details>

- **2026-08-03** — Junjie Yu, Zihan Deng, Jianyu Zhang et al. — [Understanding and Correcting Low-Frequency Bias in EEG Foundation Model](http://arxiv.org/abs/2608.01898v1)
  <details><summary>📄 Abstract</summary>
  Increasing EEG pretraining data scale or model capacity does not consistently improve downstream performance. We identify a persistent low-frequency bias in representations learned by diverse EEG foundation models, which remains across dataset scales, model capacities, and pretraining objectives. Our analysis links this bias to the interaction between EEG's $1/f^α$-like spectral structure and neural networks' tendency to preferentially learn low-frequency components. In masked autoencoders, the ...
  </details>

- **2026-08-03** — Kaoru Sumi, Souki Osawa — [Emotional Expression in Persuasion by Quadruped Virtual Agents: Toward Cross-Species Design Patterns](http://arxiv.org/abs/2608.01895v1)
  <details><summary>📄 Abstract</summary>
  Persuasive technologies increasingly use virtual agents to influence attitudes and behavior, but research has focused mainly on humanoid agents. The persuasive design of non-humanoid, quadruped agents remains underexplored, and it is unclear whether emotional expression works consistently across animal species or whether species-specific motion is necessary.   We developed virtual dog, cat, and horse agents and compared three behavioral conditions: species-specific behavior, shared behavior acro...
  </details>

- **2026-08-03** — Seunghan Lee, Jun Seo, Jaehoon Lee et al. — [ReasonCast: Towards Explainable Time Series Forecasting with Reasoning](http://arxiv.org/abs/2608.01875v1)
  <details><summary>📄 Abstract</summary>
  Most time series (TS) models are specialized for a single task, either understanding (i.e., returning text answers about a TS) or generation (i.e., returning a numeric forecast). Only recently have unified models begun to handle the two within a single architecture. Even these models, however, produce the two outputs as task-separated paths and cannot predict a series and explain why that prediction arises within a single coherent response. In this paper, we argue for a task-fused model that joi...
  </details>

- **2026-08-03** — David Fertig — [Impedance of an electric double layer capacitor with a multi-component electrolyte](http://arxiv.org/abs/2608.01799v1)
  <details><summary>📄 Abstract</summary>
  I derive the impedance response of an ideal electrolyte containing an arbitrary number of mobile ionic species between blocking planar electrodes, described by the Poisson--Nernst--Planck equations. By transforming the linearized equations to a charge--salt basis, the response is written in terms of a multi-component diffusion--migration matrix and its eigenvalues/eigenvectors. When all diffusivities are equal, the charge mode decouples from the neutral concentration subspace and the classical b...
  </details>

- **2026-08-03** — Zixuan Huang, Yang Zhou, Kaixuan Wang et al. — [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](http://arxiv.org/abs/2608.01755v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language-Action (VLA) models for autonomous driving (AD) increasingly utilize chain-of-thought (CoT) supervision to enhance the reasoning capabilities of their Vision-Language Model (VLM) components, yet existing annotation pipelines commonly expose the teacher model to the logged ground-truth (GT) future trajectory. We empirically show that this induces trajectory anchoring bias: teacher models rationalize the revealed outcome rather than infer a decision from scene evidence, prod...
  </details>

- **2026-08-03** — Yeonseo Jeong, Wonhyeok Ko, Sungweon Hong et al. — [Heterogeneous Multi-Agent Reinforcement Learning for Radio Resource Management under Coupled Finite-Horizon Constraints](http://arxiv.org/abs/2608.01745v1)
  <details><summary>📄 Abstract</summary>
  Maximizing throughput under proportional fairness in dense wireless networks requires jointly managing user association, scheduling, base station (BS) activation, and handover control under hard finite-horizon energy and handover budgets, which induces a fundamental tension between BS-side energy management and user-side handover regulation. While multi-agent reinforcement learning (MARL) is a natural framework for such distributed sequential control, its application here faces two difficulties:...
  </details>

- **2026-08-03** — Logan Ritchie, Sushant Mehta, Liudas Panavas et al. — [Post-Training on Office Work Improves Software Engineering: A Behavioral Account of Cross-Domain Transfer](http://arxiv.org/abs/2608.01604v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon tasks require agents to maintain coherent state and goals across nested and branching work. We call this capability goal-directed execution (GDE): the repeated application of four behaviors, namely selecting goals, constructing task-relevant state, maintaining fidelity to higher-level objectives, and verifying completion against the environment. We hypothesize that long-horizon post-training strengthens these behaviors across domains. We test this by post-training Qwen3.5-122B-A10B ...
  </details>

- **2026-08-03** — Abdul Basit Tonmoy — [Discriminative Axis, Not Data Volume: What a Contrastive Corpus Teaches an Audio Embedding](http://arxiv.org/abs/2608.01560v1)
  <details><summary>📄 Abstract</summary>
  Scaling the corpus is the default remedy when a contrastive representation lacks an attribute. We report a case where it does nothing, and identify what does: adding a lexical-speech round to a frozen-base multimodal embedding model raises zero-shot keyword spotting by 76 points while reducing speech-emotion recognition by 14. The loss is not a capacity limit: fine-tuning on 7,442 clips from a prosody-controlled corpus recovers emotion past its pre-speech level at a five-point keyword cost. Nor ...
  </details>

- **2026-08-02** — Yinghan Hou, Zongyou Yang — [VeraRAN: Pre-Actuation Certification and Event-Causal Synchronization Repair for Asynchronous Multi-Interface RAN Plans](http://arxiv.org/abs/2608.01047v2)
  <details><summary>📄 Abstract</summary>
  Agentic RAN controllers combine mobility, energy, and resource actions across independently implemented interfaces. Even when each command is valid and the target state is safe, asynchronous actuation can drive the network through unsafe intermediate states. In a frozen study of a 35B planner, 28.8% of locally valid plans remained asynchronously unsafe. We introduce VeraRAN, which checks plans before actuation by modeling request, delivery, acceptance, application, completion, and observation fo...
  </details>

- **2026-08-02** — Zhiwei Chen, Yang Hu, Yuxiang Xiao et al. — [Harnessing Adversarial Distillation to Customise Debiased, Disease-Specific Pathology Foundation Models for Breast Cancer](http://arxiv.org/abs/2608.01356v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) provide strong tissue representations and have become central to digital pathology. However, deployment in disease-specific settings is limited by 1) the high computational cost of billion-parameter PFMs and 2) distribution mismatch and non-biological bias inherited from pan-cancer, multi-centre pre-training, including site-specific signatures and imbalanced disease prevalence. These factors can encourage shortcut learning and under-emphasise subtle morphology ...
  </details>

- **2026-08-02** — Fabian Slonimczyk, Danila Karapsin — [Measuring Product Quality Using Images: The CLIP Q-Score and an Application to Real Estate](http://arxiv.org/abs/2608.01544v1)
  <details><summary>📄 Abstract</summary>
  The CLIP Q-score is a novel, safe, fully reproducible, and computationally efficient method for extracting objective product quality metrics from visual data using contrastive language-image pre-training. We introduce the technique and provide an extensive application to real estate data from an online platform ($\sim500,000$ images). Our open-source metric aligns with LLM assessments and proves to be a powerful predictor of housing market prices for both sales and rentals. We also show that a h...
  </details>

- **2026-08-02** — Bingxuan Li, Rui Yang, Cheng Qian et al. — [Long-Horizon Embodied Decision-Making via Multimodal Memory Compression](http://arxiv.org/abs/2608.01456v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly expected to act not only as task executors, but also as decision-makers on behalf of human users. This shift requires agents to accumulate evidence over long horizons, interpret implicit user preferences, and compare multiple candidates under partial observations. In this work, we propose DunphyBench, a new benchmark for evaluating agents on long-horizon human-centered embodied decision-making, where the agent must navigate through multiple embodied housing environments a...
  </details>

- **2026-08-02** — Pritam Deka, Prabhjot Singh — [When Retrieval Helps and Distracts: Evaluating Evidence-Generating LLMs for Biomedical Claim Verification](http://arxiv.org/abs/2608.01409v1)
  <details><summary>📄 Abstract</summary>
  Biomedical fact-checking systems must do more than predict whether a claim is supported, contradicted, or unaddressed: they should also produce evidence that is faithful, complete, and useful for verification. We study this evidence-generation setting on CARE-XAI, a unified benchmark spanning five biomedical and health fact-checking sources. We compare base instruction LLMs, PubMed retrieval-augmented LLMs, fine-tuned LLMs, label-only LLMs, and biomedical encoder classifiers under a shared evalu...
  </details>

- **2026-08-02** — Jianan Xie, Xin Sun, Zhongqi Chen et al. — [EviSD: Evidence-Conditioned Self-Distillation for Search-Augmented Agents](http://arxiv.org/abs/2608.01359v1)
  <details><summary>📄 Abstract</summary>
  Outcome-based reinforcement learning enables search-augmented language agents to learn from verifiable final answers, but its trajectory-level credit cannot distinguish the contributions of individual actions in a multi-turn search process. We propose EviSD, an evidence-conditioned self-distillation framework that uses instance-level supporting evidence as privileged information for search actions and golden answers as complementary privilege for answer actions. During training, the student samp...
  </details>

- **2026-08-02** — Sarah Wilson, Michael MacKay, Anthony Marello et al. — [Can Language Models Identify Shadow Trading Targets? An NLP Evaluation of SEC Enforcement Theory](http://arxiv.org/abs/2608.01322v1)
  <details><summary>📄 Abstract</summary>
  Shadow trading -- trading in a peer firm's securities on the basis of material nonpublic information (MNPI) about an "economically linked" company -- is a novel and contested theory of insider trading liability, first prosecuted in SEC v. Panuwat (2023). Enforcing it requires identifying economically linked firms ex ante, a determination the SEC makes only after the fact using mass market surveillance infrastructure. We ask whether NLP can do what the SEC's theory presumes insiders already know:...
  </details>

- **2026-08-02** — Xiaocui Yang, Xican Tan, Shoujie Chen et al. — [CrossLex: A Source-Grounded Benchmark for Cross-Jurisdictional Legal Reasoning in Large Language Models](http://arxiv.org/abs/2608.01292v1)
  <details><summary>📄 Abstract</summary>
  Legal reasoning is inherently jurisdiction-dependent: the same facts can call for different legal rules and yield different conclusions across legal systems. Yet existing benchmarks rarely evaluate whether large language models (LLMs) can recognize such jurisdiction-specific variation, especially when identical fact patterns lead to divergent legal outcomes.We introduce CrossLex, a same-fact, legal-source-grounded benchmark for evaluating cross-jurisdictional legal reasoning in LLMs across three...
  </details>

- **2026-08-02** — Leyan Xue, Feng Xiong, Mingjun Ma et al. — [Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models](http://arxiv.org/abs/2608.01263v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) samples trajectories from the current student policy and minimizes token-level divergence between student and teacher next-token distributions at prefixes along those trajectories. This aligns the distillation states with the student's own generation distribution. However, it still assumes that the complete teacher distribution is an appropriate target across student capacities. In vision--language reasoning, teacher corrections can depend on visual distinctions that...
  </details>

- **2026-08-02** — Sen Liang, Fengbin Guan, Youliang Zhang et al. — [CoT-Edit: Let CoT Guide Instruction Video Editing](http://arxiv.org/abs/2608.01113v1)
  <details><summary>📄 Abstract</summary>
  Text-driven instruction-based video editing in complex scenes remains challenging: purely textual prompts often fail to capture precise spatial relationships and physical constraints, resulting in target ambiguity and physically implausible outcomes. To address this, we propose a plan--guide--edit framework that explicitly bridges semantic intent and spatial execution. In our framework, a Chain-of-Thought (CoT)-enhanced multimodal large language model (MLLM) serves as a planner, performing struc...
  </details>

- **2026-08-02** — Van An Nguyen, Vuong Khang Huynh, Hoai Thuong Nguyen et al. — [Co-evolution of social reward and punishment under institutional interventions](http://arxiv.org/abs/2608.01183v1)
  <details><summary>📄 Abstract</summary>
  We investigate how peer and institutional incentives jointly shape the evolution of cooperation, social welfare, and enforcement efficiency in social dilemmas. In a Prisoners Dilemma with four strategies, unconditional cooperators (C), defectors (D), social punishers (SP), and social rewarders (SR), we allow decentralised peer incentives and centralised institutional incentives to act simultaneously, with the institution able to reward or punish any subset of strategies. In infinite well-mixed p...
  </details>

- **2026-08-02** — Jiaming Jiang, Yuzhe Huang, Hao Liang et al. — [CAAT: Contact-Aware Attention Scaling and Tactile Masking for Data-Efficient Contact-Rich Manipulation](http://arxiv.org/abs/2608.01102v1)
  <details><summary>📄 Abstract</summary>
  In contact-rich manipulation, visual observations primarily guide motion in free space, whereas tactile observations become particularly informative during contact. However, standard Transformer-based visuo-tactile policies typically rely on either token concatenation or learnable gating. These approaches lack explicit contact-aware priors, making it difficult to efficiently learn effective cross-modal representations from demonstrations. To address this limitation, we propose CAAT, a lightweigh...
  </details>

- **2026-08-02** — Robert Jacob Ryan — [Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing](http://arxiv.org/abs/2608.01494v1)
  <details><summary>📄 Abstract</summary>
  Conformal prediction has traditionally been used to quantify prediction uncertainty. We put that uncertainty to a second use, combining a 75% conformal interval with fractional Kelly to size portfolio positions: as the range widens we shrink the position, and as it narrows we grow it. On a six-year development window (2016-2021), with trading costs and strict leverage caps, this compounds at 28.5% annualised net log growth with a Sharpe ratio of 1.34 and a 27.7% maximum drawdown, versus 15.9% fo...
  </details>

- **2026-08-02** — MD Shaikh Rahman, Syed Maudud E Rabbi, Muhammad Mahbubur Rashid — [Two-Stage Bengali Sentiment Classification: Domain Adaptation Through Continual Learning and Parameter-Efficient Fine-Tuning](http://arxiv.org/abs/2608.01471v1)
  <details><summary>📄 Abstract</summary>
  Understanding sentiment in low-resource languages remains a key challenge for Natural Language Processing (NLP), particularly when domain-specific data is scarce. In this work, we present SentiBanglaBERT, a two-stage Bengali sentiment classification framework combining domain-adaptive continual pretraining and parameter-efficient fine-tuning. The approach enables contextual adaptation to news-style data while remaining computationally efficient through Low-Rank Adaptation (LoRA). Beyond performa...
  </details>

- **2026-08-02** — Yuqicheng Zhu, Jialin Yu, Lin Li et al. — [Conformalized Large Language Models under Configuration Shift](http://arxiv.org/abs/2608.01460v1)
  <details><summary>📄 Abstract</summary>
  Conformal prediction (CP) is a distribution-free framework for uncertainty quantification that has recently been adapted to large language models (LLMs), providing prediction sets with finite-sample coverage guarantees under exchangeability. Yet for LLMs, nonconformity scores are often induced by an inference pipeline, not just a fixed model, making them depend not only on the data distribution but also on configurable factors such as the prompt template, decoding parameters, and deployment sett...
  </details>

- **2026-08-02** — Huiyu Yi, Yongqi Xu, Bogang Zhang et al. — [Beyond Routing Saturation: A Long-Horizon Class-Incremental Perspective on Expert Routing in Multimodal Continual Instruction Tuning](http://arxiv.org/abs/2608.01437v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Continual Instruction Tuning (MCIT) enables multimodal large language models to acquire new tasks sequentially while retaining previously learned capabilities. Many recent methods maintain task-specific LoRA experts and route each input to one or more experts at inference. Yet the task-identification problem underlying expert routing remains under-explored. We show that routing is nearly saturated on widely used MCIT benchmarks. Textual fingerprints that leak task identity and short 4...
  </details>

- **2026-08-02** — Yi Mao, Andrew Perrault — [Training Small LLMs as Spatial Multi-Agent Policies](http://arxiv.org/abs/2608.01425v1)
  <details><summary>📄 Abstract</summary>
  Training LLM-based multi-agent systems with multi-agent reinforcement learning is rapidly gaining traction, and a parallel line of work argues that such systems should be judged by their behavior, not only their reward. We take up both threads in spatial cooperative games, where small frozen LLMs prompted with low-level actions fail outright, earning zero reward. Guided by the options/semi-MDP framework---and, because option execution is asynchronous across agents, its multi-agent extension in m...
  </details>

- **2026-08-02** — TszKin Julian Chan, Juan Estrada, Kim Huynh et al. — [Estimating Social Effects with Randomized and Observational Network Data](http://arxiv.org/abs/2608.01405v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces an innovative approach to identifying and estimating the parameters of interest in the widely recognized linear-in-means regression model under conditions where the initial randomization of peers determines the observed network. We assert that peers who are initially randomized do not produce social effects. However, after randomization, agents can endogenously develop significant connections that potentially generate peer influences. We present a moment condition that comp...
  </details>

- **2026-08-02** — Zixuan Liu, Jonathan Lawry, Michael Crosscombe — [Imprecise Belief Fusion Improves Multi-agent Social Learning](http://arxiv.org/abs/2608.01367v1)
  <details><summary>📄 Abstract</summary>
  In social learning, agents learn not only from direct evidence but also through interactions with their peers. We investigate the role of imprecision in such interactions and ask whether it can improve the effectiveness of the collective learning process. To that end we propose a model of social learning where beliefs are equivalent to formulas in a propositional language, and where agents learn from each other by combining their beliefs according to a fusion operator. The latter is parametrised...
  </details>

- **2026-08-02** — Ilias Chalkidis, Vlad Paul Cosma, Søren Debois et al. — [Hybrid AI for Explainable and Accurate Conversational Agents in eGovernment](http://arxiv.org/abs/2608.01346v1)
  <details><summary>📄 Abstract</summary>
  We present a so-called Conversational Hybrid AI (CHAI) architecture for building explainable and accurate conversational agents for eGovernment. We exemplify the architecture with a running prototype of a Covid-19 Chatbot based on a governmental guideline directed to citizens. We also describe an ongoing case on case management for supplementary grants for students with disabilities. We use large language models (LLMs) as a bounded conversational interface to a rule-based (symbolic AI) controlle...
  </details>

- **2026-08-02** — Advait Pavuluri, Shamik Karkhanis, Uzma Mushtaque — [Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data](http://arxiv.org/abs/2608.01336v1)
  <details><summary>📄 Abstract</summary>
  Modern autonomous-driving fleets record far more video than human reviewers can inspect. This motivates the need for an automatic clip triage mechanism, to surface rare and review-worthy clips, so that driving models can be fine-tuned to better handle unideal circumstances. We test a label-free approach that scores clips by the prediction-error "novelty" of a self-supervised joint-embedding predictive architecture (JEPA); a frozen V-JEPA video encoder is paired with a lightweight predictor head ...
  </details>

- **2026-08-02** — Xiaohui Bei, Felix Brandt, Matthias Greger et al. — [Individual Fairness in Budget Aggregation](http://arxiv.org/abs/2608.01228v1)
  <details><summary>📄 Abstract</summary>
  We consider the problem of aggregating $n$ individual distributions over $m$ alternatives into a collective distribution, also known as budget aggregation. Existing fairness notions in this literature typically do not guarantee fairness to individual agents. To address this, we define two versions of individual fair share guarantees. We show that when agents' utilities are derived from $\ell_t$ metrics for any $t\geq 1$, both these guarantees can be satisfied along with Pareto efficiency, and th...
  </details>

- **2026-08-02** — Yuhao Fu, Nobuyuki Hanaki, Haitao Wang — [Do Humans Bargain Differently with AI? Evidence from Alternating-Offer Games](http://arxiv.org/abs/2608.01212v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence increasingly participates in economic interactions not only as a tool, but also as an autonomous bargaining counterpart negotiating on behalf of firms, platforms, and consumers. Yet little is known about how humans respond psychologically and strategically when bargaining with such agents in dynamic settings. We study this question in a laboratory experiment using a three-stage alternating-offer bargaining game in which participants negotiate in real time with either anot...
  </details>

- **2026-08-02** — Boone Bowles, Raymond Duch, Sorin Sorescu — [Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media](http://arxiv.org/abs/2608.01181v1)
  <details><summary>📄 Abstract</summary>
  Social media affect financial markets, but public posts by financial media personas are voluntary disclosures. What is not disclosed is therefore usually unobserved. We address this measurement problem by conducting repeated, real-time interviews of "digital twins" built from monitored finfluencers' X accounts under a fixed protocol. The interviews recover stock-level public-persona belief proxies even when no public recommendation is made. Because the interviews are generated and archived befor...
  </details>

- **2026-08-02** — Mohammed Q. Shormani — [Does Machine "know" interpersonal pragmatics? Evidence from MARBERT's learning of emoji pragmatics in Arabic digital discourse](http://arxiv.org/abs/2608.01174v1)
  <details><summary>📄 Abstract</summary>
  This study examines Transformer-based models' ability to learn emoji pragmatics in Arabic digital discourse (ADD), providing evidence from MARBERT's behavior with interpersonal pragmatic functions (IPFs). A corpus of 8,504 unique emoji-posts collected from Facebook via Python was used in the study. These posts were manually annotated, developed, and labeled for five IPFs: Politeness, Respect, Solidarity, Empathy, and Encouragement. A mixed-method approach was employed comprising statistical meth...
  </details>

- **2026-08-02** — Simiao Ren — [CallScreenBench: Benchmarking On-Device Models as Phone Secretaries](http://arxiv.org/abs/2608.01033v1)
  <details><summary>📄 Abstract</summary>
  Language models small enough to run on a handset, quantized to a few bits, are increasingly capable of acting for their user, making on-device task automation newly plausible. One such task is answering the phone. A phone secretary takes an unknown inbound call on its owner's behalf. Unlike the agents evaluated by most benchmarks, it has no task to complete and no cooperative user: the caller holds the goal, may be an adversary, and must be judged from the opening turn with no oracle. What matte...
  </details>

- **2026-08-02** — Yinghan Hou, Zongyou Yang — [VeraRAN: Pre-Actuation Certification and Event-Causal Synchronization Repair for Asynchronous Multi-Interface RAN Plans](http://arxiv.org/abs/2608.01047v1)
  <details><summary>📄 Abstract</summary>
  Agentic RAN controllers combine mobility, energy, and resource actions across independently implemented interfaces. Even when each command is valid and the target state is safe, asynchronous actuation can drive the network through unsafe intermediate states. In a frozen study of a 35B planner, 28.8% of locally valid plans remained asynchronously unsafe. We introduce VeraRAN, which checks plans before actuation by modeling request, delivery, acceptance, application, completion, and observation fo...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 562 |
| prompt-injection | 467 |
| memory-poisoning | 43 |
| tool-use-attack | 96 |
| backdoor | 405 |
| adversarial-attack | 543 |
| privacy-leakage | 3748 |
| steganography | 55 |
| misuse | 851 |
| red-teaming | 110 |
| vulnerability | 2550 |
| defense | 2227 |
| alignment | 2063 |
| robustness | 2014 |
| watermark | 236 |
| unlearning | 84 |
| agent-safety | 52 |
| benchmark | 53 |
| survey | 263 |
| other | 5858 |

---

📚 **全部 22280 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-05 08:27:52*