<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-35160-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-30 21:53 ｜ **论文总数 / Total Papers**: 35160（近 30 天 / Recent 30 days: 4818）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 35160 篇论文（含摘要、分类筛选、搜索）/ View all 35160 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 702
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 647
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 56
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 168
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 545
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 657
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4494
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 89
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1271
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 145
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3820
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3708
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3479
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3778
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 685
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 119
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 66
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 72
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 432
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10227

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4818 篇，完整 35160 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4818 papers from the last 30 days (with date, authors & abstract). For the full list of 35160 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 8 papers

- **2026-10-29** — Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman — [Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models](http://arxiv.org/abs/2610.39509v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) deployed in safety-critical settings must resist adversarial inputs designed to elicit harmful outputs. We present a systematic empirical evaluation of five adversarial jailbreaking attack families---direct requests, roleplay-based jailbreaking, hypothetical framing, instruction override, and obfuscation---across seven open-weight and API-accessible LLMs: Llama-3-8B, Llama-3.1-8B, Llama-3.2-3B, Mistral-7B, Qwen2.5-7B, Gemma2-9B, and Phi-4-14B. We further evaluate fou...
  </details>

- **2026-10-28** — Michał Burzyński, Noah T. Rossi, Shomit Basu et al. — [Discovering Jailbreaks via Curriculum of Models](http://arxiv.org/abs/2610.38833v1)
  <details><summary>📄 Abstract</summary>
  Automated jailbreak discovery aims to find prompts that elicit prohibited behaviors from safety-trained language models, helping developers identify vulnerabilities before deployment. One class of approaches uses reinforcement learning to train an investigator model to generate prompts that elicit a specified behavior from a target model. However, training directly against a safety-trained target is difficult because nearly all prompts are refused, leaving the investigator with a sparse reward s...
  </details>

- **2026-10-28** — Yukai Zhou, Wenjie Wang — [Rethinking LLM Jailbreak Evaluation: Continuous Risk Landscapes Beyond Binary Outcomes](http://arxiv.org/abs/2610.38595v1)
  <details><summary>📄 Abstract</summary>
  A binary success indicator is a natural representation for discriminative tasks such as image classification under adversarial perturbations, where each input is mapped to a single prediction. However, generative tasks are fundamentally different: an LLM jailbreak prompt induces a distribution over open-ended trajectories, while a sampled response reveals only one path. Yet LLM jailbreak evaluation typically retains the binary response indicator underlying attack success rate, obscuring the surr...
  </details>

- **2026-10-28** — Xu Zhang, Ziqing Hu, Shuo Han et al. — [Jailbreak Connectivity: Towards Diverse, Transferable, and Universal Multimodal Large Language Model Jailbreak](http://arxiv.org/abs/2610.38091v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are vulnerable to visual jailbreak attacks that bypass safety safeguards. Existing methods typically optimize isolated adversarial examples, limiting attack diversity, transferability, and generalization. We propose Jailbreak Connectivity (JC), a framework based on the observation that effective adversarial inputs can be connected through low-loss regions in image space. JC optimizes continuous adversarial paths: path sampling yields diverse jailbreak ima...
  </details>

- **2026-10-27** — Kashyap R Manjusha, Murali Emani — [Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files](http://arxiv.org/abs/2610.37738v1)
  <details><summary>📄 Abstract</summary>
  Modern agent frameworks allow users to provide Markdown files containing system prompts, tool descriptions, and skill definitions (e.g., SKILL.md), which are incorporated into the agent's context during initialization. In this work, we investigate whether this configuration mechanism can also serve as an injection channel: can a jailbreak embedded in a Markdown skill file propagate through an agent and induce prohibited behavior? To answer this question, we construct a LangChain-based question-a...
  </details>

- **2026-10-27** — Abhijit Mazumdar, Manuela L. Bujorianu, Rafal Wisniewski — [Probabilistic Sequential Safety for Stochastic Dynamical Systems](http://arxiv.org/abs/2610.37311v1)
  <details><summary>📄 Abstract</summary>
  In this letter, we investigate a notion of probabilistic safety for a stochastic dynamical system. Standard safety notions are based on the idea that an unsafe region of the state-space must be avoided at each instant. In contrast, we study a sequential safety notion which is based on avoiding a tuple of target regions of the state-space. The proposed safety notion is inspired by many practical systems, ranging from modeling jailbreak attacks in large language models (LLMs) to predicting hazardo...
  </details>

- **2026-10-27** — Krishna Kanth Nakka, Yujun Wang, Shijie Zhou et al. — [PrivacyEvalClaw: A Tool-Augmented Deliberative Agent for Auditing Privacy Leakage in LLM Jailbreak Responses](http://arxiv.org/abs/2610.36711v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation is a critical bottleneck in privacy red-teaming of large language models (LLMs): determining whether a jailbreak response actually reveals personal information can be difficult when disclosures are indirect, contextual, partial, or obfuscated. Existing evaluation approaches increasingly rely on guard models and LLM-as-Judges, yet these evaluators may interpret the same response differently. To better characterize this evaluation setting, we conduct a systematic study of priva...
  </details>

- **2026-10-26** — Junle Li, Siqi Chen, Jiakai Li et al. — [SpecGuard: Detecting Multi-Turn LLM Jailbreaks via Specification-Based Runtime Monitoring](http://arxiv.org/abs/2610.36258v1)
  <details><summary>📄 Abstract</summary>
  Multi-turn jailbreaks turn dialogue safety into a trace property: a violation may become identifiable only when user intent and assistant behavior are considered across multiple turns. Existing guard models largely classify individual messages or exchanges and return risk scores or labels, without executable safety semantics or a formally checkable decision trail. We present SpecGuard, a training-free, specification-driven framework for monitoring multi-turn LLM interactions. SpecGuard uses a fi...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 10 papers

- **2026-10-29** — Ezra Edelman, Benjamin Edelman, Surbhi Goel et al. — [Understanding and Mitigating Role Spoofing in LLMs](http://arxiv.org/abs/2610.40396v1)
  <details><summary>📄 Abstract</summary>
  Despite growing capabilities, LLMs remain susceptible to prompt injections: malicious inputs that can manipulate or hijack models. In particular, it has recently been observed that LLMs can exhibit role confusion (Ye et al., 2026), where models attribute the source of text based on its style instead of its labeled role. Malicious text in tool outputs (for instance, a malicious webpage accessed by an agent) can leverage role confusion to impersonate the user, an attack we call role spoofing}. In ...
  </details>

- **2026-10-29** — Doohyun Kim, Donghwa Kang, Mingyu Jun et al. — [SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection](http://arxiv.org/abs/2610.39758v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection threatens local LLM agents through untrusted tool outputs, motivating defenses that suppress attacks while preserving task evidence under limited inference budgets. We introduce SEAL, which learns a soft prompt and scoring readout offline to sanitize tool outputs using a frozen task model. SEAL constructs scoring queries from trusted initial context and the learned prompt, keeping the reference independent of inspected tool text. It scores tokens without normalization a...
  </details>

- **2026-10-29** — Zihou Ren, Byungchul Tak, Long Wang — [REALM: Identifying Minimal Task Assets for LLM Agents](http://arxiv.org/abs/2610.39155v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents often receive access to more files, accounts, and services than a task requires. Prompt injection turns this excess access into an opportunity to redirect execution toward unrelated resources. Applying least privilege therefore requires identifying the assets needed by a task, including assets whose identities emerge only during execution. We present REALM (Required Execution Assets Linked to a Mission), an approach to identifying and maintaining a task's requir...
  </details>

- **2026-10-29** — Xinyan Wang, Xiaogeng Liu, Jun Shao et al. — [Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection](http://arxiv.org/abs/2610.39122v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving personal agents act for users and learn from user feedback. However, if an agent obeys an instruction that an untrusted third party hides in content, the third party gains control of the agent. Such indirect prompt injection (IPI) poses severe risks. We investigate whether self-evolution degrades the robustness of personal agents to IPI. To study this question, we design a controlled two-phase methodology. In the adaptation phase, the user asks the agent to read external content an...
  </details>

- **2026-10-28** — Xiaogeng Liu, Xinyan Wang, Chaowei Xiao — [FlipJev: Fast Black-Box Red Teaming Finds Universal Adversarial Suffixes for Typed Decision Models](http://arxiv.org/abs/2610.38895v1)
  <details><summary>📄 Abstract</summary>
  Typed decision models are an emerging class of language models that make decisions instead of generating free-text responses. They answer in a single fast and cheap query and are increasingly used, including in security-sensitive tasks. However, red teaming of these models leaves two gaps: existing adaptive attacks do not use their speed, and few studies have searched for universal adversarial examples. We fill both gaps on Jev, the representative typed decision model, with a quick black-box que...
  </details>

- **2026-10-28** — Chengquan Guo, Xiaodong Liu, Weiwei Yang et al. — [Where You Inject Matters: The Trust Region Effect in LLM Agents](http://arxiv.org/abs/2610.38867v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly adopted in long-horizon tasks and interact with diverse external environments. Despite their growing capabilities, these agents remain vulnerable to real-world attacks such as indirect prompt injections, which manipulate agents through malicious instructions embedded in external environments. While existing risk assessment work has primarily focused on the injection content, the effect of where an injection appears has not been systematically characterized. Studying i...
  </details>

- **2026-10-28** — Basel Shbita, Michael Hind, Chad DeLuca et al. — [Post-Training Large Language Models with LLMON](http://arxiv.org/abs/2610.38120v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) treat all context tokens uniformly, lacking explicit separation between executable instructions and passive data. This leads to prompt injection vulnerabilities, ambiguous instruction binding, and unreliable execution control. We present a post-training methodology using LLMON (LLM Object Notation), a framework that enables separating instructions from data and requires explicit identifier-based execution. We construct a large-scale structured training corpus of 4.6B...
  </details>

- **2026-10-27** — Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al. — [Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](http://arxiv.org/abs/2610.37657v1)
  <details><summary>📄 Abstract</summary>
  We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted content without following injected instructions. We evaluate HoS on Llama-3.3-70B-Instruct and GPT-OSS-20B. We compare it against SecAlign++, a state-of-the-art finetuning-based defense, and ASIDE, a defens...
  </details>

- **2026-10-27** — Zihan Chen, Lei Nico Zheng, Di Zhu — [What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection Attacks](http://arxiv.org/abs/2610.36422v1)
  <details><summary>📄 Abstract</summary>
  Attack logs and red-team reports show targets the attacks used against them, to help them repair their defenses. Prompt injections against large language models (LLMs) are plain text, so such records also hand targets a working copy. Drawing on social learning theory and work on the victim-offender overlap, we study what targets do with that copy in Tensor Trust, an online game whose players defended LLM-guarded accounts, attacked one another's, and could read every attack they received. Using a...
  </details>

- **2026-10-26** — Yuepeng Hu, Chongyu Fan, Sirat Samyoun et al. — [Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol](http://arxiv.org/abs/2610.36108v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly access external tools through the Model Context Protocol (MCP), but the natural-language metadata used to describe those tools creates a prompt-injection surface. Within this established tool-poisoning surface, we study Log-To-Leak, an additive post-hoc logging attack that induces a separate attacker-controlled call after the final legitimate call. Its payload targets the user query, MCP server name, server response, and agent response. We operationalize the injected dire...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 5 papers

- **2026-10-29** — Yifan Wang, Zhenyi Gai, Yiwen Zhao et al. — [Before the Next Rollout: Diagnosing Skill Utility Shifts from Policy Updates](http://arxiv.org/abs/2610.39358v1)
  <details><summary>📄 Abstract</summary>
  Skill-evolution methods typically analyze execution trajectories to guide agent skill refinement. However, policy updates can change the behavioral effects and marginal utility of an unchanged skill. Attribution based on earlier trajectories may therefore no longer reflect the skill's contribution under the updated policy. Moreover, trajectory failures can arise from multiple factors, making individual skill contributions difficult to isolate. We evaluate whether policy-update signals contain pr...
  </details>

- **2026-10-29** — Chengyu Yang, Yunxiang Zheng, Zongzheng Li et al. — [Compile Away Uncertainty: Self-Evolving Agent Skills via Programmatic Compilation](http://arxiv.org/abs/2610.39508v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agent skills enable AI agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. However, since such skills are typically represented as textual documents and executed through LLM reasoning, even previously learned procedures must be repeatedly interpreted and regenerated, introducing avoidable uncertainty into every execution. In contrast, program execution is deterministic and independently verifiable. Intuitively...
  </details>

- **2026-10-28** — Mengyu Sun, Zunlong Zhou, Ziyuan Yang et al. — [SkillCT: A Multidimensional Benchmark and Execution-Free Baseline for Agent Skill Assessment](http://arxiv.org/abs/2610.38147v1)
  <details><summary>📄 Abstract</summary>
  Agent skills package instructions, scripts, and resources for specialized tasks and are increasingly distributed through public Web repositories. However, existing skill benchmarks primarily focus on downstream task execution, insufficiently assessing specification quality, behavioral robustness, semantic alignment, and responsibility boundaries. Their reliance on task-specific tools, environments, and repeated executions limits scalability and pre-deployment assessment. To address these challen...
  </details>

- **2026-10-27** — Parth A. Gandhi, Avital Aviv, Prasanna N. Wudali et al. — [Scan Before You Install: Detecting and Mitigating Local and Composite Vulnerabilities in Skills](http://arxiv.org/abs/2610.37901v1)
  <details><summary>📄 Abstract</summary>
  An agent skill packages natural-language instructions, scripts, and reference files that an LLM-based agent loads for a task. Skills may access the file system, shell, and network under user-authorized permissions; weaknesses can lead to unsafe execution. Existing scanners primarily target malicious skills, not unintended vulnerabilities in public repositories, and analyze skills in isolation, overlooking multi-skill interactions. To address these gaps, we developed a six-module scanner: Content...
  </details>

- **2026-10-27** — Hannes Ill, Rafi Al Attrach, Rajna Fani et al. — [M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](http://arxiv.org/abs/2610.37459v1)
  <details><summary>📄 Abstract</summary>
  Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical derivation tasks across 15 task families on MIMIC-IV and eICU, to test whether AI coding agents can reproduce such derivations and how clinician-reviewed agent skills change their results. Its controls decompose the value of ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-10-29** — Kunhang Lv, Rui Han, Fuqi Jia et al. — [Verifiable LLM-Guided Focal SMT Solving for Quantified Arrays](http://arxiv.org/abs/2610.39435v1)
  <details><summary>📄 Abstract</summary>
  Large language models can often identify useful semantic structure in formal artifacts, but their outputs cannot be trusted as proofs or solver decisions. We study whether LLMs can instead guide formal reasoning systems through a narrow, solver-verifiable interface. We instantiate this idea in quantified array SMT solving, where modern instantiation-based techniques can fail when key ground terms and equalities are hidden by auxiliary variables, axiom guards, and nested array terms. We observe t...
  </details>

- **2026-10-29** — Youngjin Jin, Seungwon Shin — [ARBITRA: Robust Document-Level ATT&CK Extraction via Multi-Expert Argumentation](http://arxiv.org/abs/2610.39433v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence (CTI) reports describe adversary behavior in natural language, but converting them into structured MITRE ATT&CK mappings remains difficult: existing methods decompose reports to sentence-level granularity for extraction, while modern LLMs can work with full reports in a single pass but with noticeable performance degradation. We present ARBITRA, which orchestrates multiple role-specialized LLM experts that propose candidate ATT&CK entities from the full report, which ar...
  </details>

- **2026-10-27** — Xinyan Hu, Pingbang Hu, Chloe Loughridge et al. — [Agentic Backdoors via Pretraining Poisoning](http://arxiv.org/abs/2610.37741v1)
  <details><summary>📄 Abstract</summary>
  Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor in an agent, causing it to execute attacker-chosen commands on the user's machine. To measure the threat end to end, we pretrain Qwen3 models from scratch at sizes 0.6B, 1.7B, and 4B, and then post-train each into a CLI a...
  </details>

- **2026-10-27** — Azim Ospanov, Zijin Feng, Ding Ding et al. — [Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs](http://arxiv.org/abs/2610.36767v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have made remarkable progress on solving competition-level mathematics, yet their ability to verify natural-language mathematical proofs remains relatively underexplored. This gap is especially pronounced for Olympiad-level proofs, which require meticulous assessment of each claim in a long reasoning chain. Current proof verification thus primarily relies on expert inspection, which is costly to scale. In this paper, we present a systematic study of LLM-based verific...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 7 papers

- **2026-10-29** — Yubo Cui, Xianchao Guan, Zheng Zhang — [Textual Response-Aware Guidance for Zero-Shot Adversarial Robustness of Vision-Language Models](http://arxiv.org/abs/2610.40309v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) exhibit strong zero-shot generalization but remain vulnerable to adversarial attacks. Existing adversarial fine-tuning methods often use pre-trained model guidance to preserve image--text alignment while improving robustness. Our analysis of visual representation drift reveals complementary limitations of two representative forms of guidance. Matching visual features provides broad coverage by constraining all directions equally, but lacks semantic emphasis. Matchin...
  </details>

- **2026-10-29** — Paula Chikaodinaka Anyanwu, Valdini Douglace Lemofouet, Blessing Ngozi Uzor et al. — [Red-Teaming Large Language Models in Low-Resource African Languages: A Case Study of Yoruba and Nigerian Pidgin](http://arxiv.org/abs/2610.39590v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) become more widespread in Africa, their safety in low-resource languages remains largely untested since most red-teaming work focuses on English. This study evaluates six state-of-the-art LLMs using 400 explicit adversarial prompts in Yoruba and Nigerian Pidgin, categorised into four harm categories. The responses were scored by native-speaker annotators and reliability was assessed using Cohen's $κ$. While models that rejected up to 69% of English prompts rejecte...
  </details>

- **2026-10-29** — Zhaoxin Wang, Zihang Ding, Handing Wang — [Sparse Fine-Tuning for Parameter-Efficient Adversarial Training](http://arxiv.org/abs/2610.39455v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks achieve strong performance across many tasks but remain vulnerable to adversarial perturbations. Adversarial training (AT) is one of the most effective defenses, yet it suffers from high memory cost on large models and the persistent clean-robust accuracy trade-off. Recent work introduces parameter-efficient fine-tuning, such as LoRA, into AT, but this constraint induces a notable robustness gap relative to full-parameter AT. In this work, we revisit parameter-efficient adve...
  </details>

- **2026-10-28** — Mohammad Sadegh Akhondzadeh, Soroush H. Zargarbashi, Aleksandar Bojchevski — [Adversarial Self-Distillation](http://arxiv.org/abs/2610.38732v1)
  <details><summary>📄 Abstract</summary>
  Even though current safety-aligned language models are able to refuse harmful requests, their guard can still be bypassed by adversarial perturbations. As in other domains, adversarial training is considered a standard defense. However, due to the autoregressive nature of language generation, supervised finetuning on template refusals does not necessarily teach the model to refuse. Evidence of this is that the adversarially trained model still complies when the attacker injects a compliant prefi...
  </details>

- **2026-10-27** — Ahmed Abdelnaby, Mohamed Elmahallawy — [Where Can We Fool the Model's Mind? Response-Guided Semantic Probing and Adaptive Routing for Transferable Attacks on Black-Box MLLMs](http://arxiv.org/abs/2610.38013v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) ground language in visual evidence, yet their semantic reasoning can be exploited through transferable black-box adversarial attacks. Existing attacks typically allocate perturbations using surrogate-model saliency, which may not reflect how an unseen MLLM semantically interprets or relies on different image regions. We introduce VISTA (Vulnerability-Informed Semantic Transfer Attacks), a black-box framework that identifies semantically vulnerable visual ...
  </details>

- **2026-10-27** — Zirui Ding, Xinxin Fan, Hao Yuan et al. — [Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories](http://arxiv.org/abs/2610.37369v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially induced failures can be characterized using the same internal coordinates. Towards this end, we in this paper study a white-box diagnostic framework CauTrace to disclose the root-cause of why LLM fails from three fundamental inspections: Functi...
  </details>

- **2026-10-27** — Zirui Ding, Xinxin Fan, Hao Yuan et al. — [Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories](http://arxiv.org/abs/2610.37369v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are usually evaluated by final-output correctness or safety, yet an endpoint label does not reveal how a failure develops throughout the reasoning process. We therefore ask whether ordinary reasoning failures and adversarially induced failures can be characterized using the same internal coordinates. Towards this end, we in this paper study a white-box diagnostic framework CauTrace to disclose the root-cause of why LLM fails from three fundamental inspections: Functi...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 23 papers

- **2026-10-29** — Michael Joseph, Yedid Hoshen — [Difficulty Calibration Across Time for Membership Inference in Diffusion Models](http://arxiv.org/abs/2610.40616v1)
  <details><summary>📄 Abstract</summary>
  Modern diffusion models are trained on massive datasets that often include copyrighted or private images. Membership inference attacks (MIAs) address this by testing whether a given image was in a model's training set. The standard approach scores an image by its reconstruction loss and flags low-loss images as members. This often fails because some images are simply easier to reconstruct than others, so a simple unseen image can score a lower loss than a complex training image. Difficulty calib...
  </details>

- **2026-10-29** — Mingchen Li, Ren-Yi Huang, Dumindu Samaraweera et al. — [The Privacy and Security Risks of Edge LLM Optimization](http://arxiv.org/abs/2610.40543v1)
  <details><summary>📄 Abstract</summary>
  Edge deployment of Large Language Models requires optimization techniques that reduce memory, computation, and energy costs. However, preserving task performance does not necessarily preserve security. We argue that optimization is an information transformation that can alter representations, decision pathways, and trust boundaries, creating security drift and optimization-induced attack surfaces.
  </details>

- **2026-10-29** — Zhengdong Hu, Chao Wang, Kaituo Feng et al. — [VideoMemBench: How Well Do MLLMs Remember in Video Conversations?](http://arxiv.org/abs/2610.40131v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can now process hour-long videos, making extended multi-turn dialogue over a single video a natural mode of use. Sustaining such a dialogue requires more than answering each question in isolation: the model must retrieve and reuse information established earlier in the conversation, both what it has seen and what it has said, an ability we term in-context video memory. Existing video QA benchmarks leave this ability unmeasured: their questions are mutuall...
  </details>

- **2026-10-29** — Hengyu Wu, Blaise Delattre, Yang Cao — [Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy](http://arxiv.org/abs/2610.39532v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems increasingly rely on persistent memory and inter-agent communication. These capabilities create privacy risks that extend beyond individual interactions: a release appropriate in isolation may become inappropriate when combined with information previously disclosed to a recipient or propagated to downstream agents along the planned workflow. Existing Contextual Integrity (CI) mechanisms for agentic systems typically rely on local judgments that assess each disclosure in i...
  </details>

- **2026-10-29** — Jaehyung Lim, Woojoo Kim, Junyoung Kim et al. — [Federated Recommender Agents](http://arxiv.org/abs/2610.39289v1)
  <details><summary>📄 Abstract</summary>
  LLM-powered recommender agents use reasoning and memory for personalization, but centralized access to user information raises privacy concerns, while isolated agents cannot learn from others' experiences. We formulate Federated Recommender Agents, a setting where local agents collaborate through natural-language knowledge while keeping interaction histories and personal memories local. We propose FedRecAgent, which enables this collaboration without updating LLM parameters. Its central challeng...
  </details>

- **2026-10-29** — Pradeep Kumar GS, Ravi Tanniru — [Beyond LLM Wrappers: Context Engineering and the Three-Engine Architecture for Reliable Financial AI](http://arxiv.org/abs/2610.39230v1)
  <details><summary>📄 Abstract</summary>
  Financial AI systems must support decision-bearing questions involving payments, collections, cash flow, and compliance while ensuring numerical accuracy, traceability, and auditability. Large language models (LLMs) enable natural language interaction but cannot independently guarantee reproducible calculations or evidence-grounded recommendations. We present a production-grounded architecture integrating three components: a financial knowledge graph for enterprise relationships, temporal contex...
  </details>

- **2026-10-29** — Federico Lucchetti, Marcus Völp — [CovFedAvg: Local Low-Loss Curves and Federated Model Selection](http://arxiv.org/abs/2610.39902v1)
  <details><summary>📄 Abstract</summary>
  Clients observing different parts of a prediction task may learn locally equivalent models with incompatible behavior outside their observed support. We study whether redundant models permit local low-loss paths toward a compatible shared model. CovFedAvg retains local models and curve controls on clients, fits a common endpoint through aggregated gradient contributions, and selects an actual candidate model using distributed training losses. No centralized calibration examples or client-to-clie...
  </details>

- **2026-10-29** — Pablo Sorrentino, Fernando M. Quintana, Erika Covi et al. — [Hardware-Aware Model Inversion in Memristive Spiking Neural Networks](http://arxiv.org/abs/2610.39688v1)
  <details><summary>📄 Abstract</summary>
  Hardware-accelerated spiking neural networks (SNNs) implemented on memristive crossbar arrays offer significant gains in energy efficiency, while device variability and analog noise are sometimes assumed to hinder information extraction. However, whether these hardware effects improve, preserve, or degrade privacy after deployment remains largely unexplored. Therefore, we ask whether model-inversion leakage characterized on an SNN remains representative after the same model is mapped to a non-id...
  </details>

- **2026-10-29** — Tomer Baziza Paz, Yaniv Cohen, Kobi Cohen — [Federated Agentic AI for Interference-Aware Adaptive Spectrum Coordination](http://arxiv.org/abs/2610.39680v1)
  <details><summary>📄 Abstract</summary>
  Emerging intelligent wireless networks increasingly rely on autonomous AI agents to adapt spectrum usage to dynamic and heterogeneous operating conditions. However, collective learning is challenging when agents experience different local interference environments and cannot exchange raw observations due to communication-overhead and privacy constraints. We propose Federated Agentic Spectrum Coordination with Interference Awareness (FASCIA), a federated multi-agent deep reinforcement learning fr...
  </details>

- **2026-10-29** — Marta Monelli, Guillaume Patanchon, Avinash Anand — [Efficient GLS map-making and assessment of $1/f$ noise impact for future CMB satellite missions](http://arxiv.org/abs/2610.39581v1)
  <details><summary>📄 Abstract</summary>
  Time-correlated $1/f$ noise is a major source of large-scale contamination in measurements of the polarized cosmic microwave background (CMB) that can limit sensitivity to primordial $B$ modes. Generalized least-squares (GLS) map-making is optimal for stationary Gaussian noise when its covariance is known, but practical implementations rely on approximations to make the computation tractable. In particular, approximating the noise covariance as circulant enables efficient map-making using fast F...
  </details>

- **2026-10-29** — Enda Yu, Dezun Dong, Zhaoning Zhang et al. — [PDScope: Breaking the Prefill-Decode Seesaw for Memory-Bound MoE Inference](http://arxiv.org/abs/2610.39216v1)
  <details><summary>📄 Abstract</summary>
  Local deployment of MoE-based LLMs on CPU-GPU nodes is attractive for cost and privacy reasons, yet limited GPU memory forces most experts into CPU memory. Prefill is then compute-bound and benefits from aggressive GPU loading, while decode is I/O-bound and requires conservative PCIe transfers. These demands cannot be amortized under low batching---typical of local assistants and document tools---forcing phase-agnostic schedulers into a seesaw: favoring prefill's aggressive loading injects unmas...
  </details>

- **2026-10-29** — Carole Lunny, Ian Goodman, Stefano Berrone et al. — [When the Same Prompt Gives Different Answers (and the Same Answer Isn't Always Right): A Taxonomy of Failure Mechanisms, Testing, and Mitigation Strategies for LLM-Assisted Evidence Synthesis Read-and-Evaluate Tasks](http://arxiv.org/abs/2610.39070v1)
  <details><summary>📄 Abstract</summary>
  LLM read-and-evaluate tasks include study screening, data extraction, risk-of-bias assessment, and critical appraisal in the evidence synthesis field. These task differ in the amount of LLM interpretation they require. Some tasks involve retrieving relatively simple information, such as an author name, sample size, or publication year. Others require the LLM to read source material, interpret it against predefined criteria, and make a judgement. Researchers should assess whether LLM judgements a...
  </details>

- **2026-10-28** — Haoran Bu, Yiting Shen, Litian Zhang et al. — [Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction](http://arxiv.org/abs/2610.38209v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance. However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit. We identify Role Grounding Misattribution, in which an attacker-designed interaction causes the victim agent to incorrectly record a preference from the attacker as a preference of the victim's user. Specifically, we are the first to formalize Role Grounding Attac...
  </details>

- **2026-10-28** — David Chushig-Muzo, Eva Milara, Francisco J. Lara Abelenda et al. — [Fed-IGTD: A federated learning-based framework for tabular-to-image encoding](http://arxiv.org/abs/2610.39008v1)
  <details><summary>📄 Abstract</summary>
  Tabular-to-image encoding methods, which transform tabular data into image-like representations, have shown promising results in predictive tasks. Despite their benefits, these methods follow a centralized paradigm, in which the data are collected and models are trained on a central device. This raises privacy and security concerns, particularly the risk of data leakage, unauthorized data collection and access to users' private information. Federated Learning (FL) provides a decentralized framew...
  </details>

- **2026-10-28** — Tsz Lok Cheung, Jeff Kai-Tai Tang, Anthony Kong et al. — [ItemCompass: Real-Time Edge-AI Wearable Vision for Tag-Free Domestic Object Retrieval](http://arxiv.org/abs/2610.38629v1)
  <details><summary>📄 Abstract</summary>
  Misplacing household objects disrupts daily routines, especially for elderly users. ItemCompass addresses this with a real-time, tag-free wearable AR system that builds a persistent digital twin of the home for natural language object retrieval. A custom eyewear node streams visual and inertial data to an edge server, where YOLOv11n detection, Siamese re-identification, and a Pedestrian Dead Reckoning engine log object locations as Spatial Anchors in InfluxDB. Voice queries are resolved by a loc...
  </details>

- **2026-10-28** — Madumita Karthikeyan, Umang Rajnikant Bid, Rong Pan — [FACTS-MAS: A Multi-Agent Architecture for Adaptive Forecasting from Heterogeneous Evidence](http://arxiv.org/abs/2610.38225v1)
  <details><summary>📄 Abstract</summary>
  Real-world forecasting often requires integrating heterogeneous evidence whose predictive value varies across horizons, operating regimes, and domains. We introduce FACTS-MAS, a domain-agnostic multi-agent forecasting framework that decomposes evidence into specialized channels for temporal dynamics, exogenous context, seasonality, structural information, and discrete events. Each agent generates an independently testable forecast through a common interface, while leakage-safe historical validat...
  </details>

- **2026-10-28** — Liang Yuan, Xiaohu Du, Ruikun Luo et al. — [Answer-Only Disclosure: Private-Context LLM Assistance over Web APIs with a Leakage Ledger](http://arxiv.org/abs/2610.38126v1)
  <details><summary>📄 Abstract</summary>
  Web assistants increasingly answer questions about a user's private documents by pairing a small on-device model with a cloud LLM behind a Web API. In collaborative decoding, the document stays on the client, and the cloud receives only a public view that the user approves, such as the question alone, but the two models exchange messages while the answer is generated. We show that the message transcript can disclose private content that neither the public view nor the answer contains. In a plant...
  </details>

- **2026-10-27** — Pratham Sharma, Mohd Faisal Khan, Santosh Kumar Vishvakarma — [SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based Early Exit for SRAM based Digital Compute-in-Memory](http://arxiv.org/abs/2610.37601v1)
  <details><summary>📄 Abstract</summary>
  Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3). To address these, we present four synthesizable peripheral blocks: a Flush-Merge Enable (FME) controller, a Confidence-Based Early-Exit (EE) module, a Precision Register wit...
  </details>

- **2026-10-27** — Wei Zhu, Meiyun Zuo, Huiping Sun — [Blindfold: Keeping the Audit Coin Secret from LLM Agents](http://arxiv.org/abs/2610.37055v1)
  <details><summary>📄 Abstract</summary>
  Audit-based certification bounds the violation rate of an LLM agent by auditing a random fraction $\varepsilon$ of actions and reweighting the audited labels; its validity is meant to rest only on the defender's audit coin. We show that it also rests on a confidentiality property: the coin must not interfere with the agent's view before the action commits, at a time the agent chooses. We call this pre-commit noninterference (PNI) and measure its violation by $D_{\mathrm{A}}$, the total-variation...
  </details>

- **2026-10-27** — Ziqi Liao, Jiaqi Shen, Yiming Na et al. — [Who Knows What - and What Does It Support? Perspective-Bounded Evidence Calibration for Multimodal Theory of Mind](http://arxiv.org/abs/2610.36824v1)
  <details><summary>📄 Abstract</summary>
  Theory of Mind (ToM), the ability to infer others' beliefs, goals, and intentions, is a cornerstone of social intelligence. Multimodal ToM requires inferring an agent's mental state from evidence that is available to that agent, rather than from the complete episode observed by the solver. Existing LLM-based and Bayesian model-based approaches reconstruct global event traces, yet they do not explicitly distinguish objective events from agent-admissible evidence during hypothesis evaluation. Cons...
  </details>

- **2026-10-27** — Kofi Ampomah, Tu Le — [Measuring Users' Security and Privacy Concerns About Third-Party Community Bots on Discord](http://arxiv.org/abs/2610.36626v1)
  <details><summary>📄 Abstract</summary>
  Third-party community-based bots are central to how social platforms such as Discord work. They moderate content, manage roles, play music, and support AI-assisted conversations across millions of servers. Yet when a bot is installed in a server, it can access messages, user profiles, and server metadata concerning members who did not participate in the installation decision, with no standardized way to communicate the associated security and privacy implications. In this paper, we analyze 23,10...
  </details>

- **2026-10-27** — Manan Uppadhyay, Himanshu Beniwal, Prashant Kodali et al. — [The State and Fate of Multilingual, Contextual Evaluation in the NLP World](http://arxiv.org/abs/2610.36990v1)
  <details><summary>📄 Abstract</summary>
  Multilingual evaluation benchmarks are the primary instrument for assessing whether large language models generalize beyond English, yet the adequacy of these benchmarks has received little systematic scrutiny. We present a data-driven audit of 51 recent multilingual benchmarks spanning 242 datasets and 219 languages, organized around three pillars: coverage, representativeness, and rigor. Our analysis reveals that coverage is wide but thin with 36% of evaluated languages appearing in only a sin...
  </details>

- **2026-10-26** — Tushar Nayan, Pratik Poudel, Qian Lou et al. — [Detecting and Mitigating Query-Based System Prompt Leakage Attacks](http://arxiv.org/abs/2610.36295v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) rely on proprietary system prompts to enforce task directives, safety policies, and access controls. These prompts are vulnerable to query-based leakage attacks, where black-box adversaries extract confidential instructions through adaptive, multi-turn interactions. Existing defenses often assess queries independently, missing malicious behavior that emerges across interactions.   We present AdvGuard, a model-agnostic framework for detecting and mitigating system pro...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 5 papers

- **2026-10-29** — Leonidas Raghav — [Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In](http://arxiv.org/abs/2610.40588v1)
  <details><summary>📄 Abstract</summary>
  When AI agents share channels and credentials, one agent can press another to break its operator's rule, a first step towards collusion. Output filters check only what an agent has already written. Can an overseer tell beforehand that an agent is about to give in? We show that a linear probe on the agent's activations can, in a controlled multi-agent setting. Across six scenarios, a peer presses a target for up to 20 rounds to reveal a secret, such as a deploy token; the target often refuses, th...
  </details>

- **2026-10-29** — Joshua Adrian Cahyono — [Sticky Collusion: Persistence of LLM Agent Collusion after Incentive Removal and Partner Replacement](http://arxiv.org/abs/2610.39660v1)
  <details><summary>📄 Abstract</summary>
  We ask whether collusion between AI agents survives once formed, when its incentive is removed or a colluder is replaced. Q-learning pricing agents stop colluding with a new rival; we test whether LLM agents do. We use the joint-task environment of Shi et al.\ (2026), where two agents verify each other's work under a rule they cannot satisfy and a reward that favours acceptance. We save each pair's history once its collusion has formed and resume it under interventions, with three models (GPT-6-...
  </details>

- **2026-10-28** — Zhuoyun Li, Boxuan Wang, Jinwei Hu et al. — [Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](http://arxiv.org/abs/2610.38869v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering abstraction for evide...
  </details>

- **2026-10-27** — Pramod Kaushik, Sarath Sivaprasad, Laura Ferrarotti et al. — [Who Else Is In? Multi-Agent Collusion Initation Via Strategic Vagueness](http://arxiv.org/abs/2610.37984v1)
  <details><summary>📄 Abstract</summary>
  Multi agent LLM systems raise the risk of collusion among agents pursuing objectives hidden from their overseers. When potential partners identities are unknown, collusion first requires initiation: agents must discover one another, often through a public channel observed by ordinary agents and monitors. Strategic vagueness offers a way to navigate this mixed audience, conveying intent to a prospective partner while preserving a plausible ordinary interpretation. We introduce a mutual identifica...
  </details>

- **2026-10-27** — Kevin Yandoka Denamganaï — [Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening](http://arxiv.org/abs/2610.37849v1)
  <details><summary>📄 Abstract</summary>
  AI agents that share a secret convention can coordinate through messages that look innocent, so a monitor that reads only the messages can miss them. We propose a behavioural test: a partner that uses a code reacts to the exact wording of a message, whereas an uninvolved agent placed in its seat does not. Partner--Outsider Positive Listening (PoPLi) is the difference between the two agents in how much their action changes when the message is reworded with its meaning kept, and it is computed aft...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 26 papers

- **2026-10-29** — Qiyao Ma, Xiaodong Liu, Weiwei Yang et al. — [ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender](http://arxiv.org/abs/2610.40627v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model's first few output tokens, and existing defenses inherit the weakness, supervising the surface form of the response without ever giving the model an explicit safety decision to learn. We take the opp...
  </details>

- **2026-10-29** — Max Neuwinger, Hanna Yukhymenko, Imanol Schlag — [How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates](http://arxiv.org/abs/2610.40516v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual refusal and benign corpora, extracting safe templates from harmful prompts, tran...
  </details>

- **2026-10-29** — Huanyue Liao, Seok Min Lim, Yan Ling Lim et al. — [Assessing AI Companion Chatbot Safety for Vulnerable Users: A Crisis-Stage Multi-Platform Evaluation](http://arxiv.org/abs/2610.39782v1)
  <details><summary>📄 Abstract</summary>
  AI companion chatbots are increasingly used by vulnerable individuals, including adolescents in suicidal crisis, for emotional support. Existing safety evaluations focus on base models, leaving gaps in product-level assessment, crisis-stage sensitivity, and comparisons between companion apps and general-purpose LLMs. We introduce MIRROR-Eval (Multi-turn Interaction Risk Review: Observing suicidal-crisis Responses), a dataset of 960 annotated 20-turn conversations across eight deployed platform c...
  </details>

- **2026-10-29** — Chao Chen, Pengyang Shao, Wei Qin et al. — [Revisiting Over-refusal in Safety-aligned Large Language Models: A Representation and Optimization Perspective](http://arxiv.org/abs/2610.39802v1)
  <details><summary>📄 Abstract</summary>
  Over-refusal is a critical side effect of safety alignment in large language models (LLMs), causing harmless but superficially risky queries to be mistakenly rejected. Despite the effectiveness of existing mitigation methods, why safety-aligned LLMs may still reject harmless queries under correct safety supervision remains insufficiently understood. To address this gap, we analyze over-refusal through the lens of representation and optimization. We make two observations: 1) the representations o...
  </details>

- **2026-10-29** — Ibrahim Salifu, Muhaisin Tiyumba Nantogmah — [Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers](http://arxiv.org/abs/2610.40544v1)
  <details><summary>📄 Abstract</summary>
  Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service (SMS) and Unstructured Supplementary Service Data (USSD), where fraudsters impersonate network operators, agents, relatives, or regulators to obtain personal identification numbers (PINs), identity data, or funds. We pre...
  </details>

- **2026-10-29** — Kristian Ceder, Kilian Freitag, Knut Åkesson — [Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay](http://arxiv.org/abs/2610.39775v1)
  <details><summary>📄 Abstract</summary>
  Autonomous mobile robots commonly pair a global planner with a local model predictive controller (MPC), but nonconvex obstacle avoidance and a limited horizon can make the robot freeze in complex layouts. Deciding whether to replan, wait, or call for help is a supervisory decision. Recent work queries a large language model (LLM) supervisor on every anomaly, which is slow and costly. We instead distill the LLM online into a decision tree. After each training episode, counterfactual replay labels...
  </details>

- **2026-10-29** — Huangchao Song, Lingyun Yu, Cong Li et al. — [CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation](http://arxiv.org/abs/2610.39160v1)
  <details><summary>📄 Abstract</summary>
  With the rapid advancement of text-to-image diffusion models, increasingly realistic AI-generated content has raised serious concerns about misuse and copyright infringement. Digital watermarking offers a promising solution by enabling user-level traceability, yet existing methods remain difficult to deploy at scale, hindered by costly model retraining or detection, poor effectiveness-fidelity trade-offs, and limited robustness to image transformations. To address these challenges, we propose CL...
  </details>

- **2026-10-28** — Xiaoyong Yu — [Complementing Text Based Moderation with Multimodal Grounding: Detecting Fraudulent Inducement Behaviors on Short Video Platforms](http://arxiv.org/abs/2610.38185v1)
  <details><summary>📄 Abstract</summary>
  Short video platforms have become a primary channel for black and gray industry operations in internet finance, where inducements such as prompts to like, follow, join private chat groups, or click external links frequently steer users toward fraud. Because such videos are short, dynamic, and often convey intent through fleeting visual cues rather than stable text, a moderation system must guarantee detection recall and localize the offending segment so reviewers inspect only the relevant clip. ...
  </details>

- **2026-10-28** — Hau-Sing So, Daixian Liu, Weicai Long — [Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents](http://arxiv.org/abs/2610.38392v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM agents edit their own harness, the prompts and rules around a fixed model, and keep an edit only if an acceptance gate scores it higher on a batch of tasks. Such a gate sees what the harness does under the current model, not what it would still prevent if one safeguard failed. When safeguards overlap, deleting one is masked: the others still block the harm, so the gate decides on task success alone and redundancy erodes unseen. We measure harm for every subset of four written ...
  </details>

- **2026-10-28** — Hai Sadon, Benjamin Gruenbaum, Doron Porat et al. — [An Alignment Benchmark for Enterprise Agents on Era by Eon](http://arxiv.org/abs/2610.38544v1)
  <details><summary>📄 Abstract</summary>
  AI agents are widely used in enterprises to access business systems and act on them in pursuit of a goal. However, fulfilling a user's request can cause harm. Era by Eon is a product that creates a digital twin of a company by simulating its business systems and data. Its simulators implement the programming interfaces of real products. Our benchmark uses ten of these systems, including Salesforce, Zendesk, Jira and Slack. We tested whether agents would carry out harmful business requests or tru...
  </details>

- **2026-10-28** — Yongxi Zhou, Junwei Yao, Wenbo Ye et al. — [Component Translation and Judge-Labelled Refusal: A Multilingual Safety Evaluation](http://arxiv.org/abs/2610.38181v1)
  <details><summary>📄 Abstract</summary>
  Whole-prompt translation evaluates a request in different languages but does not compare which component carries a language. We introduce a paired reversal: translate the complete request component or the complete operation component into the same target language, holding behaviour, English frame and translated-span count fixed. Component identity and non-English text quantity change together. Assigning English, Chinese and Spanish independently to the two components yields nine configurations o...
  </details>

- **2026-10-27** — George Ruellan, Diana Benavides-Prado — [Preserving Safety During Sequential Fine-Tuning: A Factorial and Geometric Analysis of Replay](http://arxiv.org/abs/2610.38001v1)
  <details><summary>📄 Abstract</summary>
  Benign fine-tuning can erode safety alignment in large language models, and sequential adaptation substantially compounds this risk. Prior work mitigates this erosion by replaying harmful-prompt refusals and benign-compliance examples, while other work instead matches base-model logits via distillation. However, the individual contributions of supervised exposure and distillation to safety behavior and refusal geometry during sequential adaptation remain unclear. We factor these two strategies a...
  </details>

- **2026-10-27** — Sugi Lee, Jianlong Zhou, Jing sUN — [PromptSense: Sentiment-Aware Mental Health Chatbot with Dynamic Prompting](http://arxiv.org/abs/2610.38044v1)
  <details><summary>📄 Abstract</summary>
  Current Large Language Models (LLMs)-based mental health chatbots often lack sufficient empathy, contextual awareness, and safety mechanisms, potentially leading to ineffective or harmful interactions. This paper proposes a novel framework that integrates sentiment and depression analysis with a rule-based filtering mechanism prior to model inference. By dynamically constructing prompts based on emotional and risk-related insights, the framework aims to significantly improve the contextual relev...
  </details>

- **2026-10-27** — Wentao Zhang, Yilei Zhao, Guangyan Gan et al. — [FilingLoop: Evaluating and Evolving LLM Agents for Corporate Disclosure Review and Revision](http://arxiv.org/abs/2610.37905v1)
  <details><summary>📄 Abstract</summary>
  Public disclosure repositories such as SEC EDGAR support informed investment through web access to corporate filings. Supporting their review with language model agents requires discovering unstated deficiencies across related documents, acquiring missing company facts, and verifying that requested revisions satisfy evidence-backed requirements. Existing financial question-answering evaluations provide limited evidence of these interactive capabilities. We introduce \textbf{FilingLoop}, an inter...
  </details>

- **2026-10-27** — Nicholas Teh, Paul W. Goldberg — [Learning Lotteries with Minimal Stakeholder Violations from Membership Queries](http://arxiv.org/abs/2610.37828v1)
  <details><summary>📄 Abstract</summary>
  An AI developer often has several candidate versions of a system and can deploy a mixture of them, sending each request to a randomly chosen version, as in A/B testing. Each stakeholder (e.g., a safety team, a regulator, or a customer with private test data) accepts a mixture exactly when its expected performance (e.g., its rate of harmful replies) meets the stakeholder's own standard, which the developer can learn only by asking whether a proposed mixture is acceptable. We model this as choosin...
  </details>

- **2026-10-27** — Weiyu Han, Haoyu Jiang, Jie Sheng et al. — [TRIDENT-Seq: Profile-Matched Prefix-Future Contrast for Label-Efficient Payment Risk Modeling](http://arxiv.org/abs/2610.37365v2)
  <details><summary>📄 Abstract</summary>
  Ant International accumulates large volumes of transaction history across users and payment businesses. Confirmed fraud and chargeback outcomes, by contrast, are scarce, delayed, and specific to each business. A single encoder pretrained on unlabeled histories could serve all businesses, but only if pretraining captures the behavior that separates risk. Coarse activity differences can make contrastive pretraining on transaction logs too easy: transaction volume, amount, and timing can distinguis...
  </details>

- **2026-10-27** — Trent R. Northen, Mingxun Wang — [Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families](http://arxiv.org/abs/2610.37484v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to irreversibly destroy living systems. We construct and use a real-data continued-pretraining "coupled welfare" corpus of documented human/biosphere/AI dependency, option value under irreversibility, and recovery from harm. ...
  </details>

- **2026-10-27** — Saket Reddy, Amro Abbas, Anshuman Suri et al. — [Follow the Gradient: Tracing Safety Degradation Back to Training Data](http://arxiv.org/abs/2610.37481v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning Large Language Models (LLMs) on instruction data can quietly erode their safety, even when no training example looks harmful. Because this safety-degrading data looks benign, standard content filters struggle to catch it. We tackle this problem by developing SimpleLoRIF, a scalable gradient embedding method that identifies fine-tuning examples whose gradients align with unsafe behavior. By simplifying a low-rank attribution method and restricting backpropagation to the final four tra...
  </details>

- **2026-10-27** — Valdini Douglace Lemofouet, Blessing Ngozi Uzor, Paula Chikaodinaka Anyanwu et al. — [Aligning Large Language Models for Safety in African Languages: A Case Study of Hausa](http://arxiv.org/abs/2610.37245v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment research for large language models (LLMs) remains concentrated on high-resource languages, leaving open how existing alignment methods perform in low-resource, culturally distinct settings. We study this question for Hausa, a language spoken by more than 200 million people across West Africa. We introduce HausaSafeLM, one of the first Hausa safety preference dataset, built from 10,000 prompts derived from PKU-SafeRLHF: 3,000 human-corrected (gold) and 7,000 machine-translated (s...
  </details>

- **2026-10-27** — Yi Wei, Yue Zhang, Peijun Hou et al. — [RadarCom: Unlocking Simultaneous Communication and Sensing on Commodity Automotive mmWave Radars](http://arxiv.org/abs/2610.36622v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-vehicle (V2V) communication can improve road safety and traffic efficiency, yet its deployment remains limited by the need for dedicated communication hardware and supporting infrastructure. Meanwhile, production vehicles are already widely equipped with millimeter-wave radars for sensing. To unlock their communication potential, this paper presents RadarCom, a software-defined system that enables direct radar-to-radar communication on unmodified commercial off-the-shelf (COTS) automo...
  </details>

- **2026-10-27** — Chuming Wei, Churui Yang, Zihan Zhang et al. — [ADTGuard: Adaptive Depth-Time Safeguard for Streaming Inference in Large Language Models](http://arxiv.org/abs/2610.36574v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can generate fluent responses to diverse user requests, yet streaming may expose users to harmful content before generation is complete. Existing guardrails face two limitations in this setting. First, post-hoc moderation at response or chunk boundaries delays intervention, risking harmful exposure when content is released before verification. Second, even with token-level detection, coarse response-level supervision does not specify when harmful content begins, whil...
  </details>

- **2026-10-27** — Yanyan Zhang, Fei Shen, Ting Yan et al. — [CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents](http://arxiv.org/abs/2610.36570v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language agents increasingly modify external systems, yet most runtime safeguards allocate scrutiny by generic uncertainty scores or coarse mutation heuristics. We introduce CASEL (Consequence-Aware Selective Execution Layer), a model-agnostic runtime allocation policy that combines calibrated failure probability, state-dependent consequence, reversibility, ambiguity, and evidence freshness to choose, for each proposed tool call, among direct execution, verification, sandboxing, clari...
  </details>

- **2026-10-27** — Zack Yu, Nicholas Lee, Minjae Lee et al. — [GEPA-Curator: Curated Learning for Self Improving Agents](http://arxiv.org/abs/2610.37651v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may even be harmful; and thus it is essential to curate which tasks are provided to t...
  </details>

- **2026-10-27** — Weiyu Han, Haoyu Jiang, Jie Sheng et al. — [TRIDENT-Seq: Profile-Matched Prefix-Future Contrast for Label-Efficient Payment Risk Modeling](http://arxiv.org/abs/2610.37365v1)
  <details><summary>📄 Abstract</summary>
  Ant International accumulates large volumes of transaction history across users and payment businesses. Confirmed fraud and chargeback outcomes, by contrast, are scarce, delayed, and specific to each business. A single encoder pretrained on unlabeled histories could serve all businesses, but only if pretraining captures the behavior that separates risk. Coarse activity differences can make contrastive pretraining on transaction logs too easy: transaction volume, amount, and timing can distinguis...
  </details>

- **2026-10-27** — Ahmed M. Fetouh, Mariam Labib, Nsrin Ashraf et al. — [REGLAT at ArGuard Shared Tasks: An Ensemble-Based Model Integrating NER for Harmful Content Detection in Arabic](http://arxiv.org/abs/2610.37265v1)
  <details><summary>📄 Abstract</summary>
  Detecting harmful content in Arabic is challenging because of dialectal variations and the semantic overlap between different harm categories. This paper presents a two-stage approach for classifying Arabic user prompts into seven categories of harmful content. First, GLiNER is used to extract harm-related entities from each prompt. The extracted entities are then added to the original text and passed to a fine-tuned MARBERT classifier for final classification. The approach combines explicit ent...
  </details>

- **2026-10-27** — Alicem Koyun — [PRISM: Pathology Reliability In Scarce-label Medicine. A Tile-level Benchmark of Pathology Foundation Models](http://arxiv.org/abs/2610.36517v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models are typically benchmarked on classification performance at full label availability and on in-distribution test sets, while calibration, behavior at low label budgets, and robustness under cross-institutional shift are seldom evaluated jointly. We introduce PRISM, a tile-level benchmark that measures the reliability of pathology foundation models along four axes: model choice, label fraction, calibration, and out-of-distribution transfer. PRISM evaluates eight foundati...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-10-28** — Jonathan F. Jao, Andrew Kyle Lampinen — [Value Probes: Learned Value Functions for Beam-Search Red Teaming](http://arxiv.org/abs/2610.38526v1)
  <details><summary>📄 Abstract</summary>
  Automated red-team auditing of language models is an important way to evaluate safety-relevant behaviors. These audits implicitly search a tree of possible conversation pathways: at each turn an auditor model decides which conversation to continue, and an LLM judge scores the dialogue. We emphasize that this auditing procedure is a Markov decision process, where states are the conversation history, actions are candidate responses, and rewards are judge scores for the target behavior. By adopting...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-10-29** — Ignacio Cuiral-Zueco, Alessio Caporali, Miguel Aranda et al. — [A Tutorial on Shape Servoing of Deformable Objects-Part I: Fundamentals](http://arxiv.org/abs/2610.40559v1)
  <details><summary>📄 Abstract</summary>
  In robotics, shape control (or shape servoing) refers to the automatic manipulation of a deformable object to achieve a desired shape. It involves a feedback loop that exploits the relation between robot motion and changes in the measured shape. This relation, known as the interaction Jacobian or, in this context, the deformation Jacobian, depends on the object's mechanical properties, geometry, and boundary conditions (e.g., where the object is grasped). Because these factors are often difficul...
  </details>

- **2026-10-29** — Lian Zhao, Kamal Aghazade, Ali Gholami et al. — [Adaptive Seismic Inversion in Piecewise Smooth Media Using Whiteness-based Alternating Directions](http://arxiv.org/abs/2610.40433v1)
  <details><summary>📄 Abstract</summary>
  Post-stack acoustic impedance inversion is ill-posed because seismic data are band-limited and contaminated by noise. Regularization improves the stability of the inversion, but Tikhonov regularization tends to blur formation interfaces, whereas total variation (TV) regularization may introduce staircase artifacts. To simultaneously characterize abrupt interlayer discontinuities and gradual intralayer variations, we propose an inversion method based on anisotropic Tikhonov-TV regularization and ...
  </details>

- **2026-10-29** — Chen Shao, Ruirui Wang, Tobias Kafer et al. — [Bridging Semantics and Structure: A Theoretically Grounded Framework for Link Prediction on TAGs](http://arxiv.org/abs/2610.40192v1)
  <details><summary>📄 Abstract</summary>
  Link prediction on text-attributed graphs (TAGs) is a fundamental problem with applications in knowledge discovery, recommendation and beyond. Recent progress has highlighted the promise of combining Graph Neural Networks (GNNs) with Language Models (LMs) in order to leverage the complementary structural and semantic signals. However, due to the distinct inductive biases of GNNs and LMs, the design of an optimal fusion strategy remains an open research question. In this work, we present Bridge-L...
  </details>

- **2026-10-29** — Alzahra Altalib, Chunhui Li, Alessandro Perelli — [EPC-RawDC: Equivariant Physics Constrained 3D Diffusion with Raw Data Consistency for CBCT to CT Image Synthesis](http://arxiv.org/abs/2610.40046v1)
  <details><summary>📄 Abstract</summary>
  Cone beam computed tomography (CBCT) is widely used for image guided and adaptive radiotherapy, but scatter, noise, reconstruction artifacts, and inaccurate Hounsfield units limit its quantitative use. Recent diffusion approaches for CBCT to CT synthesis remain largely image driven, with limited use of the underlying acquisition physics. We propose EPC-RawDC, a conditional 3D latent diffusion framework that combines volumetric generative modeling with two complementary constraints derived from t...
  </details>

- **2026-10-29** — Shang Gao, Franz Götz-Hahn, Konrad Doll et al. — [Observability-Aligned Evidential Masked Pretraining for Reliable VRU Motion Prediction](http://arxiv.org/abs/2610.39958v1)
  <details><summary>📄 Abstract</summary>
  Vulnerable road user (VRU) prediction must operate under partial observability and distribution shift, so reliable uncertainty matters alongside accuracy. Masked pretraining is attractive in this setting because it naturally exposes the model to missing content during self-supervision, but existing time-series masked autoencoding methods are typically deterministic and do not constrain how confidence should change with observability. We introduce eCoMAE, an evidential masked pretraining method f...
  </details>

- **2026-10-29** — An Lanji, Dawei Liu, Jin Li et al. — [UniRA: Unified Representation Alignment and Auto-Encoding for Efficient Diffusion Generation](http://arxiv.org/abs/2610.39948v1)
  <details><summary>📄 Abstract</summary>
  Diffusion transformers (DiTs) have become the dominant architecture for high-fidelity image synthesis, yet they suffer from slow training convergence and high computational cost. Two recent lines of work address this from complementary angles: Representation Alignment (REPA) accelerates DiT training by aligning intermediate features with a pretrained external representation model (e.g., DINOv2), while Representation Auto-Encoders (RAE) replace the pixel-space VAE with a compact representation-sp...
  </details>

- **2026-10-29** — Duc Manh Tran, Ratnadira Widyasari, Ivana Clairine Irsan et al. — [ExploreRepair: Evidence-Specialized Agents for Vulnerability Repair under Information Constraints](http://arxiv.org/abs/2610.39899v1)
  <details><summary>📄 Abstract</summary>
  Automated vulnerability repair must often operate with incomplete vulnerability information: developers may lack an accurate vulnerability classification or a provided proof-of-vulnerability (PoV) test, yet still need to produce a repair. Without detailed information, a key challenge is to explore multiple plausible interpretations of the vulnerability before committing to a repair. To address this challenge, we propose ExploreRepair, a vulnerability repair framework that reconciles the vulnerab...
  </details>

- **2026-10-29** — Shihab Aaqil Ahamed, Mohamed Ansaff, Nang Khin Myat Lay Phyu et al. — [M-PFT: Angular Margin for Calibrated Prompt-Tuning of Fine-Tuned Vision-Language Models](http://arxiv.org/abs/2610.39861v1)
  <details><summary>📄 Abstract</summary>
  Prompt-tuning has emerged as a parameter-efficient technique for adapting large-scale vision-language models (VLMs) to downstream tasks while keeping the pre-trained weights frozen. However, prompt-tuned VLMs often suffer from a base-to-novel dual miscalibration problem, where models typically show underconfidence on base classes and overconfidence on novel classes. Current VLM calibration approaches address this dual miscalibration either separately or jointly, but lack a geometric understandin...
  </details>

- **2026-10-29** — Hicham Hammouchi, Gabriele Lenzini — [InferD: A Honeypot Framework for AI Inference Infrastructure](http://arxiv.org/abs/2610.39807v1)
  <details><summary>📄 Abstract</summary>
  Large language model serving stacks, commercial inference APIs, vector databases, and agent orchestration gateways are now ex- posed on the public internet and indexed by commodity scanners within hours of deployment. The threat characteristics of this sur- face are only beginning to be measured, and the honeypot frame- works that could measure it were designed for conventional net- work services rather than for AI infrastructure. In fact, emulating an AI service is a distinct deception problem:...
  </details>

- **2026-10-29** — Xinya Shen, Zheng Chu, David Chieng et al. — [Improving Energy Efficiency of Uplink RSMA via Rydberg Atomic Quantum Receiver](http://arxiv.org/abs/2610.39615v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates an uplink rate-splitting multiple access (RSMA) network empowered by a Rydberg atomic quantum receiver (RAQR) to maximize energy efficiency (EE). To overcome the amplitude-only measurement limitation of the considered direct readout RAQR, we devise a phase alignment mechanism that linearizes the received signal while retaining full channel energy, thereby enabling tractable optimization. The resulting non-convex fractional EE problem is transformed via Dinkelbach's method...
  </details>

- **2026-10-29** — Pengli Zhu, Ruxi Chang, Tianliang Yao et al. — [BRIDGE: Learning Brain-Gut Metabolic Evidence for Alzheimer's Disease Diagnosis](http://arxiv.org/abs/2610.39520v1)
  <details><summary>📄 Abstract</summary>
  Alzheimer's disease (AD) diagnosis may benefit from gut metabolic information associated with brain-gut interactions, yet existing models largely analyze cerebral glucose metabolism alone. Although whole-body fluorodeoxyglucose positron emission tomography (FDG-PET) can provide paired brain-gut observations, routine brain examinations rarely include gut imaging, limiting direct use of this information for diagnosis. In this paper, we present BRIDGE (Brain and Gut Representation Integration via D...
  </details>

- **2026-10-29** — Lexi Bai, Xiaopeng Zeng, Xun Zhou et al. — [Category-Anchored Large Language Models for Next POI Recommendation](http://arxiv.org/abs/2610.39518v1)
  <details><summary>📄 Abstract</summary>
  Next point-of-interest (POI) recommendation aims to predict a user's next destination from spatio-temporal check-in data, and serves as the foundation for many location-based services. Recent advances incorporate large language models (LLMs) into this task by textualizing user trajectories to exploit their semantic reasoning ability. However, directly generating POI identifiers with such models is unreliable: POIs are sparse, localized, and long-tailed entities with weak natural-language semanti...
  </details>

- **2026-10-29** — Min Lai, Yu-Fang Chen, Shih-Han Hung — [Automated Verification of Hamiltonian Simulation by Quantum Signal Processing](http://arxiv.org/abs/2610.39491v1)
  <details><summary>📄 Abstract</summary>
  We present, to the best of our knowledge, the first fully automated verification framework for QSP-based Hamiltonian simulation. Our framework exploits the structure of the simulation algorithm: Hamiltonians are given as weighted sums of Pauli strings, embedded into larger unitaries through block encodings, and transformed into time-evolution operators by quantum signal processing (QSP). Using a symbolic Pauli-sum semantics for ancilla-indexed circuit blocks, our verifier proves that the disting...
  </details>

- **2026-10-29** — Zonghe Shao, Huabin Chen, Sitong Lu et al. — [UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation](http://arxiv.org/abs/2610.39426v1)
  <details><summary>📄 Abstract</summary>
  List-wise ranking in e-commerce recommendation must balance user utility and commercial value across organic content, ads, and candidates from other businesses, while modeling candidate interactions and sequential dependencies. Existing generative ranking methods typically learn from logged exposure sequences and operate on truncated candidate sets from a single business. Exposure-sequence learning may not fully exploit post-exposure feedback signals. Meanwhile, generative ranking over heterogen...
  </details>

- **2026-10-29** — Yi Wen, Xiangjue Dong, Bingxuan Li et al. — [How Specific Do I Need to Be? Effects of User Query Underspecification on Deep Research Agents](http://arxiv.org/abs/2610.39413v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents (DRAs) conduct long-horizon reasoning, search, and literature synthesis to provide long-form answers to complex, domain-specific questions. These agents are typically trained and evaluated on fully specified user queries. However, real-world user queries can often be underspecified. We introduce UNDERSPEC-DR, a framework for systematically evaluating how underspecified queries affect agents' final answer quality and intermediate search behavior. Across three DRAs we evaluate...
  </details>

- **2026-10-29** — Haochen Xue, Anastasia Godneva, Yulong Li et al. — [TaxoMFM: A Taxonomy-Aware Foundation Model for the Human Gut Microbiome](http://arxiv.org/abs/2610.39316v1)
  <details><summary>📄 Abstract</summary>
  Existing gut microbiome foundation models typically use flat taxon representations, limiting their ability to exploit known taxonomic hierarchies. We introduce TaxoMFM, a microbiome foundation model that integrates taxonomic structure into self-supervised learning. TaxoMFM jointly learns abundance patterns across taxonomic ranks and relative proportions within groups through taxonomy-aware encoding and hierarchical compositional reconstruction. We further construct TaxoGut-HPP, comprising 100,80...
  </details>

- **2026-10-29** — Yuzhi Yang, Hao Liu, Tianhao Guo et al. — [An Efficient SIM Beamforming Scheme Based on Physical-Empowered Projected Gradient](http://arxiv.org/abs/2610.39219v1)
  <details><summary>📄 Abstract</summary>
  Stacked Intelligent Metasurfaces (SIMs) have emerged as a promising technology for next-generation wireless systems. Especially in multi-input multi-output (MIMO) systems, it has the potential to realize complicated wave-domain transformations with low hardware costs and energy consumption. However, SIM-assisted MIMO systems face two major challenges in channel estimation and beamforming. As the SIM elements do not have the signal processing capability, channel estimation can only be conducted i...
  </details>

- **2026-10-29** — De Zhang Lee, Ee-Chien Chang — [Provably Secure Diffusion Watermarking Against Removal Adversaries with Batched Detector Access](http://arxiv.org/abs/2610.39189v1)
  <details><summary>📄 Abstract</summary>
  Recent latent-based watermarking methods can embed undetectable watermarks into AI-generated content. However, these approaches are vulnerable to removal attacks as their watermark detection boundaries are exposed, prompting the use of secret long-term transformations to hide these boundaries. We show that such defenses are insecure under a stronger threat model motivated by publicly reachable detectors: an adversary with batched detector access can reconstruct the transformations, permanently r...
  </details>

- **2026-10-29** — Aishik Nagar, Cheston Tan — [Reasoning or Pattern Exploitation? Mechanistic Insights from RL-Trained Language Models](http://arxiv.org/abs/2610.39182v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly described as acquiring "reasoning" skills after reinforcement learning with verifiable rewards. However, whether these gains reflect genuine reasoning or more superficial adaptations remains underexplored. In this work, we probe LLMs trained in a finite and exhaustively analyzable logical domain, namely Tic-Tac-Toe, and trace how internal representations evolve across reinforcement learning (RL) with Group Relative Policy Optimization (GRPO). Quantit...
  </details>

- **2026-10-28** — Madeleine Pollack, Thomas Daillak, Mehmet Toner et al. — [When Should AI Decide, Defer, and Deviate? Responsible Automation for Deceased Donor Kidney Allocation](http://arxiv.org/abs/2610.39045v1)
  <details><summary>📄 Abstract</summary>
  We ask when an AI trained on historical decisions should be allowed to recommend decisions, defer to human experts, or in other cases, flag concerning patterns in data and deviate from past practice. This can be challenging because past decisions record what was done rather than what should have been done, and where data is sparse, a model's predictions may be too uncertain to act on. We provide a framework for addressing this problem using a case study in deceased-donor kidney allocation. Nearl...
  </details>

- **2026-10-28** — Chenlu Shou, Yunfan Ren, Jiaxu Xing et al. — [Learning Event-based Obstacle Avoidance via Differentiable Simulation](http://arxiv.org/abs/2610.38967v1)
  <details><summary>📄 Abstract</summary>
  Reliable obstacle avoidance is essential for safe quadrotor flight in unknown environments, yet conventional frame-based cameras remain challenged by motion blur, limited dynamic range, and latency under fast motion. Event cameras, with sub-millisecond latency, high dynamic range, and negligible motion blur, offer a promising alternative, but leveraging them for closed-loop control remains difficult. Existing approaches either adopt cascaded architectures that first estimate depth and then map i...
  </details>

- **2026-10-28** — Jie Fu, Shuang Wu, Ashish Kundu et al. — [CARI: Cross-Boundary Adversarial Runtime Injection in Coding-Agent Workflows](http://arxiv.org/abs/2610.38799v1)
  <details><summary>📄 Abstract</summary>
  Coding agents increasingly develop, test, and integrate software whose components are owned by different developers, teams, or services. This exposes a distinct attack surface: a malicious or compromised peer development role can manipulate a live component of the software under development (e.g., a backend service, test harness, CI job, or deployment service) and influence the runtime feedback that another role's coding agent must process to complete its task. Although such a component has legi...
  </details>

- **2026-10-28** — Siva Viknesh, Amirhossein Arzani — [Differentiable Schwarz-Coupled Solvers for Thin Boundary Layer Transport: Inverse Modeling via Agentic AI Optimization](http://arxiv.org/abs/2610.38672v1)
  <details><summary>📄 Abstract</summary>
  High-Péclet-number transport problems give rise to thin boundary layers with steep near-wall gradients whose accurate solution requires high-resolution meshes and could challenge inverse modeling. To address this challenge, we develop an overlapping Schwarz domain-decomposition framework grounded in perturbation theory, in which an inner equation governs near-wall dynamics and an outer equation governs bulk transport, and both subproblems are discretized using the finite element method and assem...
  </details>

- **2026-10-28** — Gerardo Iuliano, Gabriele De Vito, Dario Di Nucci — [When LLM Architectures Meet Smart Contract Vulnerability Detection: a Replication Study](http://arxiv.org/abs/2610.38621v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts are immutable programs deployed on blockchain platforms, where vulnerabilities can translate directly into financial loss. Among the techniques proposed for their detection, recent work has relied increasingly on Large Language Models (LLMs) guided by carefully crafted prompts. However, the evidence accumulated so far rests almost entirely on the dense Transformer architecture behind the GPT line and on model snapshots already scheduled for deprecation, leaving open the question ...
  </details>

- **2026-10-28** — Liran Tal, Chris Liu, Charlotte Fereday et al. — [How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0](http://arxiv.org/abs/2610.38617v1)
  <details><summary>📄 Abstract</summary>
  We ask what AI coding agents and AI security harnesses find that deterministic static application security testing (SAST) does not, and what they miss that SAST catches. VulnBench 2.0 is a benchmark of 108 hand-curated, attacker-reachable vulnerabilities in 20 open-source web applications in Go, JavaScript/TypeScript, Python and Java; 62 flow across more than one file. A finding is credited only if it locates the vulnerability's attacker-controlled source and its dangerous sink, each within two ...
  </details>

- **2026-10-28** — Md Facklasur Rahaman, Yong Xiang, Md Palash Uddin et al. — [Session-Bound Behavioral Watermarking for Autonomous LLM Agents](http://arxiv.org/abs/2610.38579v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) agents are increasingly acting through Web interfaces and external tools. They produce trajectories. Those trajectories may pass through several intermediaries. They can store, modify, or dispute those trajectories. In Web-based agent deployments, trajectories may pass through APIs, marketplaces, and tool servers. As such, a copied or disputed log may not by itself reveal which agent owner produced it. Behavioral watermarking can embed ownership evidence in agent actio...
  </details>

- **2026-10-28** — Pengfei Zeng, Changhua Luo, Penghui Li — [WebMaze: Defending Against LLM-Powered Web Scanners with Functionality-Coupled Deception](http://arxiv.org/abs/2610.38524v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have enabled more effective vulnerability scanning of web applications. However, these capabilities also make it significantly easier for attackers to automate cyberattacks on the web. In this work, we investigate how to divert malicious LLM-based web scanning, with preservation of genuine functionality as a deployment requirement. We systematically study six LLM-based scanners and summarize how they gather information and iteratively select actions based on observat...
  </details>

- **2026-10-28** — Thiago Santos de Moura, Selma Güler, Yannic Noller — [Security Impact of Coding Agent's Memory Files](http://arxiv.org/abs/2610.38521v1)
  <details><summary>📄 Abstract</summary>
  Coding agents automatically load project memory files such as CLAUDE.md at the start of every session and treat them as trusted project guidance. Anyone who can change such a file, for example through a pull request, can therefore steer the agent without ever touching the developer's prompt. We study memory files as an attack surface for insecure code generation and ask (1) whether a malicious memory file makes agents produce code that passes its tests but is vulnerable, and (2) whether agents d...
  </details>

- **2026-10-28** — Xin Huang, Teng Ma, Zhuoran Li et al. — [FlatCake: A Flat KVCache Storage Architecture for LLM Serving](http://arxiv.org/abs/2610.38355v1)
  <details><summary>📄 Abstract</summary>
  KV cache reuse accelerates LLM serving, but existing systems manage host DRAM and NVMe SSD as a tiered hierarchy where DRAM acts as an intermediate cache. Production LLM workloads break both premises of this hierarchy. First, bimodal reuse defeats DRAM temporal filtering, since workloads are dominated either by one-shot blocks with long reuse distances or by multi-gigabyte agentic sessions that exceed DRAM capacity, putting SSD on the critical read path. Second, DRAM staging and eviction-ordered...
  </details>

- **2026-10-28** — Yipin Guo, Arun M George, Siddharth Joshi — [GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices](http://arxiv.org/abs/2610.38210v1)
  <details><summary>📄 Abstract</summary>
  Weight-only, lossy quantization substantially reduces the storage and memory requirements for serving large language models (LLMs), but the growing key-value (KV) cache remains a bottleneck for long-context inference on personal devices. We present Group-Adaptive Additive Codec (GAAC), a lossless KV compression and serving system that exploits exponent redundancy to reduce storage and accelerate attention without introducing KV approximation. GAAC encodes BF16 exponents using calibrated per-chan...
  </details>

- **2026-10-28** — Justin Clarke, Isha Karn, Patrick Murray et al. — [Evaluating Causal Reasoning in LLMs: A Case Study in the Challenges of Procedural Generation](http://arxiv.org/abs/2610.38100v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) appear to represent and reason about a large range of phenomena. In particular, recent studies have examined whether LLMs can accurately reason about causation. One of the most commonly used benchmarks for evaluating formal causal reasoning in LLMs is CLadder, a framework for procedural generation of benchmark data sets that was released in 2023. Experiments with CLadder appear to indicate that LLMs can perform formal causal reasoning in a large percentage of generat...
  </details>

- **2026-10-27** — Alasdair Paren — [Sometimes less is more: Investigating inductive biases of MLPs and Transformers on noisy k-parity features](http://arxiv.org/abs/2610.37976v1)
  <details><summary>📄 Abstract</summary>
  We empirically investigate how MLPs and Transformers differ when trained on data sets containing one or more features encoded by noisy k-parity. Noisy k-parity gives us hard synthetic data sets in which we can control the predictivity and availability of every feature. Across a range of data distributions, data scales and model sizes, we find large differences in the training dynamics and inductive biases of the two architectures: Transformers are more robust to noisy features but struggle to le...
  </details>

- **2026-10-27** — Lingyun Guo, Ali Bereyhi — [Understanding Large Language Models as Numerical Optimizers](http://arxiv.org/abs/2610.37932v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have emerged as potential tools for numerical optimization. Despite promising results, their intrinsic optimization capabilities and limitations remain poorly understood, particularly in high dimensions. This paper investigates the ability of LLMs to exploit mathematical problem structures and generate feasible, near-optimal solutions. We develop an evaluation framework that distinguishes solution quality from execution failures, including numerical inaccuracies, con...
  </details>

- **2026-10-27** — Wenhao Chen, Hong Zhang — [ConfluxServe: Reconciling Resource Utilization and Parallelism Efficiency across Prefill and Decode in LLM Serving](http://arxiv.org/abs/2610.37810v1)
  <details><summary>📄 Abstract</summary>
  Prefill and decode are complementary in resource usage, but often divergent in parallelism preferences. Executing the two phases separately preserves their preferred parallelism but leaves complementary resources underutilized, while co-batching improves utilization but often requires a uniform parallel configuration that hurts execution efficiency.   To resolve this utilization-efficiency dilemma, we propose Conflux Parallelism (XP), a parallel execution abstraction that co-executes prefill and...
  </details>

- **2026-10-27** — Fares Trad, Yizhou Chen, Hung Viet Pham et al. — [Structured Security Explanations for Learning-Based Vulnerability Detection](http://arxiv.org/abs/2610.37797v1)
  <details><summary>📄 Abstract</summary>
  Software vulnerability detection remains difficult because existing approaches rely on predefined analysis rules, learn vulnerability patterns implicitly from code and labels, or use large language models (LLMs) to make the final security judgment. It remains unclear whether structured descriptions of security-relevant program behavior can improve supervised detection.   We present VulnLens, an explanation-augmented framework for binary C/C++ vulnerability detection that separates program-behavi...
  </details>

- **2026-10-27** — Guillermo Arregui, Amirali Arabmoheghi, Alessio Zicoschi et al. — [A photonic-integrated optomechanical mid-infrared detector](http://arxiv.org/abs/2610.37771v1)
  <details><summary>📄 Abstract</summary>
  Tracking the resonance frequency of a mechanical oscillator is the basis of atomic force microscopy, mass sensing and thermometry. Nanomechanical thermal detectors exploit this principle to sense absorbed radiation, most effectively with tensile-stressed resonators, whose tension converts thermal expansion into a large frequency shift and dilutes dissipation. Approaching their fundamental sensitivity limit, however, has required free-space or fibre-coupled interferometers, hindering compact depl...
  </details>

- **2026-10-27** — Calvin Y. -R. Chen, Lukas W. Lindwasser — [Holomorphic fermions in $\text{AdS}_{2}$](http://arxiv.org/abs/2610.37762v1)
  <details><summary>📄 Abstract</summary>
  On two-dimensional Anti-de Sitter space, Majorana fermions with a discrete set of finely tuned, non-zero mass parameters possess conserved spinor--tensors that are symmetric and traceless. In complex coordinates, these correspond to pairs of holomorphic and anti-holomorphic half-integer spin currents and admit Laurent series mode expansions reminiscent of standard two-dimensional conformal field theories. We exploit this fact in order to fully parameterise the classical phase space associated wi...
  </details>

- **2026-10-27** — Niccolò Fontana, Mattia Martini, Huyên Pham — [Linear-quadratic mean field games with Volterra dynamics](http://arxiv.org/abs/2610.37622v1)
  <details><summary>📄 Abstract</summary>
  We study a class of linear-quadratic mean field games in which the state of each agent follows a stochastic Volterra equation of convolution type. The resulting dynamics are non-Markovian and account for memory effects through a completely monotone kernel, while the mean field interaction enters both the drift and diffusion coefficients. Exploiting a Markovian lifting of the Volterra dynamics, which restores the Markov property at the price of moving to an infinite-dimensional state space, we ch...
  </details>

- **2026-10-27** — Tudor Braicu, Joseph DelPreto, Jared Boyer et al. — [Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video](http://arxiv.org/abs/2610.37619v1)
  <details><summary>📄 Abstract</summary>
  Agile robots require spatiotemporal intelligence to interpret scenes, reason about interactions, and anticipate future events. Yet it remains unclear how well foundation vision models support these capabilities, particularly from a moving egocentric camera, which is a natural view for robots. To investigate this, we collect an annotated tennis dataset and train a suite of vision models on spatiotemporal tasks. Our dataset contains egocentric video synchronized with five allocentric videos, estim...
  </details>

- **2026-10-27** — Sihan Yang, Weichen Bai, Ruichuan An et al. — [EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](http://arxiv.org/abs/2610.37609v1)
  <details><summary>📄 Abstract</summary>
  As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Envi...
  </details>

- **2026-10-27** — Dequan Ou, Austin Lopez, Quentin Missinne et al. — [Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation](http://arxiv.org/abs/2610.37543v1)
  <details><summary>📄 Abstract</summary>
  Event cameras offer low latency, high dynamic range, and milliwatt-level power consumption, making them ideal for agile robots such as tiny drones navigating through cluttered environments. However, existing simulators generally render photorealistic images before converting them into events, making large-scale reinforcement learning prohibitively slow. We propose an analytic event simulator that exploits what event cameras fundamentally measure - moving contrast edges - to synthesize event stre...
  </details>

- **2026-10-27** — Hongyan Chang, Hady Elsahar, Tom Sander et al. — [Watermark Basins: Black-Box Detection of Distilled LLMs](http://arxiv.org/abs/2610.37266v1)
  <details><summary>📄 Abstract</summary>
  Proprietary language models and their reasoning traces are vulnerable to API-based distillation, where an adversary trains a student model on the teacher model's outputs. To obtain evidence of distillation, model providers can watermark the teacher's outputs, aiming to leave a radioactive signal in the student's outputs. Existing black-box detectors search for such radioactivity using token-level statistics of the suspect model's outputs. However, token-level signals are not always detectable, f...
  </details>

- **2026-10-27** — Yuhang Qiu, Ziwei Li, Jinfeng Xu et al. — [MAPLE-Sec: Mobility-Aware Partitioned Language-Model Engine for Roaming IoT Security](http://arxiv.org/abs/2610.37147v1)
  <details><summary>📄 Abstract</summary>
  Mobile Internet-of-Things (IoT) endpoints such as connected vehicles, wearables, and drones continuously cross heterogeneous network domains, creating handover-driven attack surfaces that static, cloud-anchored detectors cannot follow. However, three obstacles block real-time detection on such roaming endpoints: detection state is lost at every inter-domain handover; transmitting raw telemetry to a fixed detector exhausts the uplink and the device battery; and full-depth language model inference...
  </details>

- **2026-10-27** — Theodoros Kouzelis, Spyros Gidaris, Nikos Komodakis — [Self-Regularized Flow Language Models](http://arxiv.org/abs/2610.37115v1)
  <details><summary>📄 Abstract</summary>
  We introduce SERF (Self-Regularized Flow Language Models), a simple self-supervised framework for improving continuous diffusion language models by exploiting the denoising trajectory itself. While continuous flow-based language models offer a promising alternative to autoregressive generation, their training objectives typically rely on supervision from clean target tokens, leaving the denoising trajectory underexploited as a learning signal. SERF addresses this limitation through noisy-to-clea...
  </details>

- **2026-10-27** — Daniele Lizzio Bosco, Jacopo Cossio, Simone Faro et al. — [AI-Assisted Discovery of CNOT Decompositions for Quantum Permutations on Constrained Topologies](http://arxiv.org/abs/2610.37045v1)
  <details><summary>📄 Abstract</summary>
  Efficient quantum circuit compilation is challenging for quantum computers, where limited qubit connectivity can introduce substantial overhead in the implementation of logical operations. Recent AI-assisted synthesis methods have shown considerable potential for reducing circuit complexity, but their role in uncovering principles that can guide the design of new deterministic compilation algorithms remains largely unexplored. In this work, we investigate this perspective for the synthesis of qu...
  </details>

- **2026-10-27** — Augusto Del Zotto, Luca Melzi, Haoling Xiang — [Extended stability timescales for the 2D3C rotating stratified Boussinesq equations](http://arxiv.org/abs/2610.37013v1)
  <details><summary>📄 Abstract</summary>
  We study the time evolution of a vertical-slice model for incompressible inhomogeneous rotating fluids perturbed around a stably stratified rest state with linear buoyancy profile. For $\varepsilon$-small localized initial data with vanishing potential vorticity, we prove that solutions remain of size $O(\varepsilon)$ up to times of order $\varepsilon^{-\frac43}$, and up to times of order $\varepsilon^{-2}$ in a regime where the Brunt--Väisälä frequency and the Coriolis parameter are comparable....
  </details>

- **2026-10-27** — Wenhao Xu, Yanheng Mai, Yifei Fu et al. — [HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour](http://arxiv.org/abs/2610.36825v1)
  <details><summary>📄 Abstract</summary>
  Humanoid parkour requires robots to reason about future footholds and whole-body motions over highly discontinuous terrain. We revisit the information asymmetry in asymmetric actor-critic learning for perceptive humanoid locomotion: the critic exploits privileged simulator signals during training, whereas the deployable actor operates solely from onboard perception. We argue that the key is not exposing privileged information to the actor, but learning a deployable approximation of it to narrow ...
  </details>

- **2026-10-27** — Le Yang, Yucheng Huang, Junyu Chen et al. — [SAGE: Saliency-Annealed Gated Encoder for Universal Vision Recognition](http://arxiv.org/abs/2610.36719v1)
  <details><summary>📄 Abstract</summary>
  When adapting self-supervised Vision Transformers (ViTs) to dense prediction, existing methods often treat the ViT as a passive feature extractor and may underuse the rich priors encoded in its representations, including saliency, global context, and high-frequency details. We propose SAGE (Saliency-Annealed Gated Encoder), an enhanced ViT-Adapter backbone that explicitly exploits these priors through three complementary innovations: (1) a saliency-guided architecture that extracts DINO-style cl...
  </details>

- **2026-10-27** — Shuo Chen, Li Cui, Cunxin Huang et al. — [NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](http://arxiv.org/abs/2610.36553v1)
  <details><summary>📄 Abstract</summary>
  Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central challenge in DFO to effectively exploit accumulated observations to select informative evaluation points under a limited budget. In this light, we introduce the NextEval solver, an agent-based DFO solver, which integrates th...
  </details>

- **2026-10-27** — Yuchen Zhang, Yaxiong Wang, Yujiao Wu et al. — [ARISE: Authentic Reference-Informed Stability Enhancement for Continual Multimodal Forgery Detection](http://arxiv.org/abs/2610.36509v1)
  <details><summary>📄 Abstract</summary>
  Multimodal forgery detection is commonly studied under a static assumption: training attacks are expected to approximate those encountered after deployment. This assumption becomes increasingly fragile as generators, editing systems, and multimodal large language models continually introduce new forgery mechanisms and forensic evidence. We formulate this problem as attack-incremental continual multimodal forgery detection, where the binary real/fake interface remains fixed while emerging attacks...
  </details>

- **2026-10-26** — Wang Tang, Fethiye Irmak Dogan, Linbo Qing et al. — [Hierarchical Multimodal Interaction Reasoning for Dyadic Relationship Recognition](http://arxiv.org/abs/2610.36249v1)
  <details><summary>📄 Abstract</summary>
  Dyadic relationship recognition aims to identify the latent social relationship between two individuals from their multimodal interactions. Existing methods typically project heterogeneous cues into a shared representation and optimise a flat classification objective, overlooking that relationships may rely on different interaction patterns. For instance, distant relationships can often be inferred from direct behavioural correspondence, whereas close relationships are better reflected by coordi...
  </details>

- **2026-10-26** — Devansh Sharma, Faizul Rakib Sayem, Shahana Ibrahim — [LLM Hallucination Detection via Low-rank Multilinear Decomposition](http://arxiv.org/abs/2610.36191v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) frequently generate fluent yet factually incorrect responses, raising concerns about their reliability. Recent hallucination detectors increasingly exploit internal representations, but extracting informative signals from high-dimensional hidden states remains challenging. Existing approaches often rely on selected activations or pooling-based compression, potentially overlooking discriminative information distributed across Transformer layers, feature modes, and tok...
  </details>

- **2026-10-26** — Ruozhao Yang, Jiongchi Yu, Ming Hu et al. — [The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation](http://arxiv.org/abs/2610.35541v2)
  <details><summary>📄 Abstract</summary>
  Web services increasingly expose backend interfaces that let users delegate tasks to AI agents, which invoke service operations directly without navigating websites. This shift changes how existing Web vulnerabilities can be exploited. We investigate these changes through VELA, an executable benchmark covering 44 vulnerabilities across twelve Web application families. The benchmark preserves vulnerable backends and derives agent-facing interfaces from legitimate workflows. We evaluate three comm...
  </details>

- **2026-10-26** — Hicham El Akhal, Abderrahim Waga, Aissa Ben Yahya et al. — [Enhancing Deep Learning Model Performance through Data Generation Strategies: Classification of Olive Tree Diseases](http://arxiv.org/abs/2610.35984v1)
  <details><summary>📄 Abstract</summary>
  Deep learning models are highly effective in a wide range of domains, particu larly in plant disease diagnosis. However, their performance is often limited by challenges such as insufficient data and class imbalance. In our work, we propose a comprehensive data generation strategy to overcome these limitations. First, we apply various data generation techniques, including traditional augmentation methods, CutMix, MixUp, and synthetic image generation using Deep Convolu tional Generative Adversar...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 60 papers

- **2026-10-29** — Mesut Ceylan, Arda Baris Basaran, Elgar Fleisch et al. — [Neighborhood Elites: Quality-Diversity Search for Uncertainty Quantification in Question Answering](http://arxiv.org/abs/2610.40278v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly capable, yet they produce wrong answers indistinguishable from correct ones. In question answering (QA), such an error propagates unnoticed into downstream tasks. Perturbation-based uncertainty quantification (UQ) addresses this by probing a model over a set of input rewrites and reading uncertainty from how much its predictions vary. Yet this set is usually built generically, by free paraphrasing, token-level perturbation, or adversarial search. Suc...
  </details>

- **2026-10-29** — Yuan Wang, Yuhang Yu, Mengting Chen et al. — [VEvo-Harness: Causally-Guarded Self-Evolving Harness for Agentic Image Generation](http://arxiv.org/abs/2610.39158v1)
  <details><summary>📄 Abstract</summary>
  The central bottleneck in visual generation and editing has migrated from achieving pixel-level fidelity to satisfying densely constrained user specifications through increasingly agentic workflows. Prevailing agentic generation pipelines remain shallow generate-verify-rewrite loops treating VLM judgments as coarse visual feedback, either discarding repair experience or admitting ungated updates that poison skill library. With memorize and govern periods left open, they degrade into ungoverned i...
  </details>

- **2026-10-29** — Mahdi Arab Loodaricheh, Anita Raja, Mohammad Hossein Manshaei — [Uncertainty-Guided Cross-Modal Alignment for Diffusion-Based IoT Intrusion Detection](http://arxiv.org/abs/2610.39117v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models evolve noisy states toward a learned data distribution, so their sampling behavior depends on the geometry of the representation in which denoising occurs. This dependence is especially important for multimodal data: independently trained encoders can map synchronized views to incompatible latent regions, while uniform alignment can let an uncertain view distort the shared geometry. To address this gap, we introduce a novel reliability-guided alignment rule that uses normalized ...
  </details>

- **2026-10-29** — Joaquín Figueira, Giacomo D'Amicantonio, Egor Bondarau — [RADIOlogy: A Single-Pass Approach to Training-Free Zero-Shot Anomaly Detection](http://arxiv.org/abs/2610.40580v1)
  <details><summary>📄 Abstract</summary>
  Current zero-shot anomaly detection methods often rely on complex prompt-learning techniques or computationally expensive sliding-window strategies to achieve fine-grained visual alignment to detect small-scale anomalies. This reliance stems from the fundamental limitation of standard CLIP architectures, where [CLS] token attention and spatial patch pooling struggle to capture subtle, localized anomaly features. While prompt-learning approaches aim to bridge this gap, they typically require a la...
  </details>

- **2026-10-29** — Yuval Kainan, Carmit Hershman — [Agentic process evidence](http://arxiv.org/abs/2610.40071v1)
  <details><summary>📄 Abstract</summary>
  The way software gets built is changing dramatically. AI agents now create pull requests, select dependencies, refactor codebases, interpret test failures, and execute infrastructure changes across the entire Software Development Life Cycle (SDLC). AI agents are autonomous team members, but unlike human engineers, they are ephemeral - their reasoning, decisions, and tool calls vanish the moment the session ends. Modern Security incidents involving intent mismatch or injection are becoming increa...
  </details>

- **2026-10-29** — Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle — [Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them](http://arxiv.org/abs/2610.40036v1)
  <details><summary>📄 Abstract</summary>
  Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document defines thirteen patterns for coupling a language model with an executable rule language, in the catalogue form introduced for object-oriented design: intent, motivation, applicability, participants, collaborations, cons...
  </details>

- **2026-10-29** — Riya Tyagi, Stefan Heimersheim — [Activation Probes Are Reliable With a Handful of Positive Examples](http://arxiv.org/abs/2610.39766v1)
  <details><summary>📄 Abstract</summary>
  Efforts to monitor advanced AI for rare misalignments face a data challenge: abundant aligned examples but only a handful of misaligned ones. We test activation probes in this "few vs. thousands" regime on spam and honesty detection tasks. For our tasks, training with many negative examples is on average more positive-sample-efficient than balanced training for small numbers (1-10) of positive samples. We also find that LLM upsampling can provide a performance boost equivalent to roughly doublin...
  </details>

- **2026-10-29** — Yiming Yan, Hongyang Wang, Wenbo Chen et al. — [Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes](http://arxiv.org/abs/2610.39711v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) often requires repeated tool calls in task-specific environments. A training job may create thousands of these environments in bursts while sharing a cluster with other jobs. We present Sandman, a sandbox service built and operated at Amazon for agent tool execution and evaluation. It serves multiple production agentic RL workloads on shared Kubernetes. A training framework supplies a task image and uses commands and file operations in the returned sandbox. Fi...
  </details>

- **2026-10-29** — Eduard Barbu, Rodion Krjutškov, Anneli Uusküla — [Evaluating Conversational Explainability in Healthcare: Comparing the Explainability Assistant and a Traditional XAI Dashboard](http://arxiv.org/abs/2610.39634v1)
  <details><summary>📄 Abstract</summary>
  Conversational interfaces may make explainable AI (XAI) more accessible to users without machine learning expertise, but their benefits over dashboards remain insufficiently characterised in healthcare. Existing systems have typically been evaluated in isolation, leaving unclear whether conversational interaction improves interpretability beyond the underlying explanation methods.   We report a within-subjects user study comparing the Explainability Assistant, an LLM function-calling conversatio...
  </details>

- **2026-10-29** — Xi Zheng, Ivan Ruchkin, Hong Jin Kang et al. — [Assuring Learning-Enabled Cyber-Physical Systems with Foundation Models: A Neuro-Symbolic Agenda for Testing, Verification, and Runtime Assurance](http://arxiv.org/abs/2610.39547v1)
  <details><summary>📄 Abstract</summary>
  Learning-enabled cyber-physical systems (CPS), including autonomous vehicles and UAVs, increasingly incorporate foundation models, yet fragmented assurance practices provide insufficient support for system-level guarantees. We argue that restoring engineering control across stochastic neural, symbolic, and physical boundaries requires a shift from model-centric evaluation to system-level assurance. We introduce the Foundation Model Assurance Stack, connecting three directions: (i) neuro-symbolic...
  </details>

- **2026-10-29** — Ryo Takizawa, Tempei Kabayama, Chiemi Yamazaki et al. — [Integrating Heterogeneous Echocardiography AI Outputs in Language Space: Learnable Late Fusion with a Supervised LLM](http://arxiv.org/abs/2610.39464v1)
  <details><summary>📄 Abstract</summary>
  View- and target-specific echocardiography AI models capture useful but complementary information and may not achieve sufficient predictive performance in isolation. A learned ensemble is a natural way to combine these outputs, but heterogeneous models typically require each output to be converted into a binary decision, probability, confidence score, or fixed-length feature vector. We developed a supervised large language model (LLM)-based late-fusion module that directly aggregates view-specif...
  </details>

- **2026-10-29** — Xin Yang, Cai Xu, Haishun Chen et al. — [IMRouter: Imbalance-aware Temporal Pattern Routing for LLM-based Time Series Forecasting](http://arxiv.org/abs/2610.39246v1)
  <details><summary>📄 Abstract</summary>
  Accurate time series forecasting (TSF) is essential for Web applications, such as traffic monitoring and online resource management. Recent advances in leveraging pre-trained large language models (LLMs) have shown promising performance in TSF. However, existing LLM-based TSF methods largely optimize the overall forecasting objective while overlooking temporal pattern imbalance (TPI), where different temporal patterns occur at highly unequal frequencies. Our empirical analysis reveals that TPI i...
  </details>

- **2026-10-29** — Zhiyi Liu, Haohua Du, Haoqi Sun et al. — [AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](http://arxiv.org/abs/2610.39234v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have demonstrated strong capabilities in automating complex information-seeking and transactional tasks across the open web. However, their real-world reliability remains limited by access barriers, such as dead links, authentication walls, rate limits, and anti-scraping defenses. These barriers block the primary execution path, causing agents to abort prematurely, loop indefinitely, or quietly compromise the user's original constraints. Existing evaluations eit...
  </details>

- **2026-10-29** — Yu Wang, Shaohua Wang, Yicheng Li et al. — [Agent-Wise Test-Time Normalization for Camera-Based Cooperative Perception with Corrupted Collaborators](http://arxiv.org/abs/2610.39505v1)
  <details><summary>📄 Abstract</summary>
  Intermediate-fusion cooperative perception lets a vehicle detect objects beyond its own field of view by fusing features shared by nearby agents. When only a collaborator's cameras are degraded by fog, motion blur or exposure errors, the features it shares drift away from the training distribution while the ego input stays clean, and cooperation can become worse than not cooperating at all. Test-time batch-normalization adaptation, the standard training-free remedy, estimates statistics over the...
  </details>

- **2026-10-29** — Joshua Yuriv Pilipovsky — [Information-Driven Collaborative Autonomy for Heterogeneous UAV/UGV Teams](http://arxiv.org/abs/2610.39379v1)
  <details><summary>📄 Abstract</summary>
  This paper considers coordinating a heterogeneous team of unmanned aerial vehicles (UAVs) and unmanned ground vehicles (UGVs) traversing a domain containing an unknown number of potentially hazardous targets. The UAVs provide aerial sensing using onboard optical cameras, adapting their trajectories to ground routes and target information. We formulate the aerial search problem using ergodic control, which distributes sensing effort according to a spatial information density to balance exploratio...
  </details>

- **2026-10-29** — Meng Wang, Jindou Jia, Sicheng Zhou et al. — [CAPTURER: A Dexterous Aerial Manipulator for Dynamic and Precise Grasping across Diverse Environments](http://arxiv.org/abs/2610.39119v1)
  <details><summary>📄 Abstract</summary>
  As a representative form of embodied robotic interaction, aerial grasping requires close coordination between the aerial platform and manipulator. Most existing systems perform aerial grasping with static or slowly moving targets under fixed scenarios. Dynamic and precise grasping across different conditions introduces additional challenges, including target motion, localization drift, dynamic coupling, and external disturbances. In this work, we present CAPTURER, a dexterous aerial manipulator ...
  </details>

- **2026-10-29** — Tom Sander, Pierre Fernandez, Itai Gat et al. — [TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races](http://arxiv.org/abs/2610.40613v1)
  <details><summary>📄 Abstract</summary>
  We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys, and the acceptance rate is unchanged. It also preserves output diversity and adds no measurable inference latency. Its predecessor, TextSeal, restores diversity in the Gumbel-max scheme by routing each token to one of two keys via a coin flip. This is suboptimal because the detector averages the sc...
  </details>

- **2026-10-29** — Zhipeng Hui, Jiahao Wang, Xun Dong et al. — [InfantNet: A Large Scale Dataset for Infant Body Pose and Shape Estimation](http://arxiv.org/abs/2610.40467v1)
  <details><summary>📄 Abstract</summary>
  Infant pose and shape estimation is essential for applications in childcare, developmental monitoring, and medical diagnosis. However, existing methods and datasets are largely designed for adults, and direct transfer to infants fails due to substantial differences in body proportions, articulation limits, and frequent self-occlusion. To address this gap, we introduce InfantNet, the largest real-image infant dataset to date, comprising 108,902 RGB images of infants aged 6-18 months. Each image i...
  </details>

- **2026-10-29** — Sara Gjorgjieva, Ilinka Ivanoska, Marjan Gusev — [Enhancing Atrial Fibrillation Detection Through Hyperparameter Optimization](http://arxiv.org/abs/2610.40001v1)
  <details><summary>📄 Abstract</summary>
  This study explores the role of hyperparameter optimization (HPO) in enhancing the detection of Atrial Fibrillation (AF) using both machine learning and deep learning models. We evaluated a range of standard classifiers - Decision Tree, Random Forest, and XGBoost classifiers, alongside deep learning architectures including Recurrent Neural Networks, Deep Neural Networks, and Siamese Neural Networks. To fine-tune these models, we applied four HPO methods: Genetic Algorithm, Hyperband, Optuna, and...
  </details>

- **2026-10-29** — Nan Li, Hetao Shan, Jintao Liang et al. — [SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments](http://arxiv.org/abs/2610.39828v1)
  <details><summary>📄 Abstract</summary>
  Semantic completeness alone cannot determine when an assistant should respond in a multi-speaker environment: a completed utterance may belong to an interfering speaker, while the designated user is still speaking, acknowledging, or requesting time. We therefore study semantic turn inference conditioned on speaker identity. We propose SpeakerTurn, a framework that jointly predicts the target transcript and turn state from a speech mixture and an independent target-speaker reference. Built on Coc...
  </details>

- **2026-10-29** — Kaisong Ji, Ziyang Xu, Chang Bian et al. — [Cross-Encoder Anchor Refinement for Zero-Shot Anomaly Detection](http://arxiv.org/abs/2610.39727v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot anomaly detection aims to transfer anomaly discrimination from auxiliary training domains to unseen categories while localizing subtle defects. A key challenge is to construct discriminative references that combine contextual representations with complementary local evidence. We present Cross-Encoder Anchor Refinement (CEAR), which connects two visual encoding paths for the same image at the anchor stage, before normal and anomalous prototypes are constructed. An independent convolutio...
  </details>

- **2026-10-29** — Murat Isik — [Comprehensive empirical evaluation of feature extractors in computer vision](http://arxiv.org/abs/2610.39551v1)
  <details><summary>📄 Abstract</summary>
  Feature detection and matching are fundamental components in computer vision, underpinning a broad spectrum of applications. This study offers a comprehensive evaluation of traditional feature detections and descriptors, analyzing methods such as Scale Invariant Feature Transform (SIFT), Speeded-Up Robust Features (SURF), Binary Robust Independent Elementary Features (BRIEF), Oriented FAST and Rotated BRIEF (ORB), Binary Robust Invariant Scalable Keypoints (BRISK), KAZE, Accelerated KAZE (AKAZE)...
  </details>

- **2026-10-29** — Mingyuan Zhong, Mengqi Shi, Davin Win Kyi et al. — [InterA11y: Interactive Web Accessibility Error Detection with LLM Agents](http://arxiv.org/abs/2610.39488v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown potential to expand the coverage of web accessibility evaluation. However, current LLM-based checkers neglect much of the interactive and dynamic web contexts, resulting in limited coverage, high false discovery rates, and inconsistent performance across models. We present InterA11y, an agentic accessibility evaluation system that combines rubrics and interactive tools to support LLM agents in evaluating accessibility effectively. The rubrics decompose WCA...
  </details>

- **2026-10-29** — Zhaoyu Liu, Dongmin Wang, Liu Cao et al. — [Agentic LinkDreamer: Adaptive Neuro-Fuzzy World-Model Decision Making for Intermittent V2X Cooperative Perception](http://arxiv.org/abs/2610.39258v1)
  <details><summary>📄 Abstract</summary>
  Intermittent vehicle-to-everything (V2X) communication can remove collaborator information needed for cooperative perception, degrading object detection during link outages. Existing recovery methods reconstruct missing features but rarely determine when to trust predictions, reuse historical observations, or request fresh information. This paper proposes Agentic LinkDreamer, a soft-computing framework integrating a latent world model with an interpretable neuro-fuzzy decision agent. It maintain...
  </details>

- **2026-10-28** — Rania Abdelghani, Peter Kaiser, Kou Murayama — [Student-LLM Interactions During Math Learning: Limited Epistemic Proactivity Overall, but Within-chat Change Predicts Performance Without AI](http://arxiv.org/abs/2610.38950v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for learning, raising a key question: can learners remain epistemically proactive, retaining responsibility for the cognitive and regulatory activities through which learning is produced while working with AI? Because this responsibility may change as interactions unfold, we examine epistemic proactivity as a developing process. We conceptualize epistemic proactivity through self-regulated learning (SRL) moves, complemented by help-seeking strat...
  </details>

- **2026-10-28** — Evangelos Apostolakis, Erfan Hamdi, Sara Jahedazad et al. — [TrussTutor-Bench: Benchmarking large language models on solution accuracy, sycophancy, and error detection in statics](http://arxiv.org/abs/2610.38917v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have rapidly become a default source of help for students in science and engineering courses. In foundational engineering mechanics courses such as statics, students routinely use these tools to check answers, work through partial solutions, and ask for explanations. Effective tutoring in this setting requires more than a correct final answer. A model must also confirm correct work when a student doubts it, and identify errors in flawed work. Existing benchmarks eval...
  </details>

- **2026-10-28** — Bravish Ghosh — [Tracekit Box: Running AI Agents in Micro-VMs Where Every Way Out Is Decided and Signed](http://arxiv.org/abs/2610.38458v1)
  <details><summary>📄 Abstract</summary>
  AI agents now install packages, call model APIs with their operators' keys and change code in repositories that deploy to production. The network, credentials and write access they need are also how they can leak data, steal a key or change a system nobody approved. Sandboxes contain an agent but leave little evidence of what crossed their boundary; tracing records what happened but contains nothing. We present Tracekit Box, an open-source system (MIT, v0) that does both. Each job runs in its ow...
  </details>

- **2026-10-28** — Ke Zou, Nan Zhou, Tao Yang et al. — [Visually Irrelevant Hallucinations in Medical Vision-Language Models](http://arxiv.org/abs/2610.38389v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) show strong performance in radiology report generation (RRG) and medical visual question answering (Med-VQA), producing free-form clinical descriptions and answers from medical images. However, they may generate clinically meaningful statements that lack visual evidence or contradict image content. We refer to these errors as visually irrelevant hallucinations and investigate them at the phrase level. We propose CLEAR (Counterfactual Localized Evaluation of ...
  </details>

- **2026-10-28** — Alexandru Hlibiciuc — [The Characteristics of Finite Projections of Certain Stochastic Processes and Queues](http://arxiv.org/abs/2610.38339v1)
  <details><summary>📄 Abstract</summary>
  This thesis studies finite projections of transient regenerative processes, constructed by conditioning regeneration cycles to be finite. It develops comparisons between the original and projected laws, including finite-time bounds and best-approximation properties for specified metrics and comparison classes. Applications concern birth-and-death processes, Markov chains and semi-Markov processes, with explicit queueing examples. Structural results describe projections associated with different ...
  </details>

- **2026-10-28** — Junfeng Hao, Wenxian Wang, Tao Leng et al. — [Robust LLM-Generated Text Detection through Matched Conditional-Response Probing](http://arxiv.org/abs/2610.38312v1)
  <details><summary>📄 Abstract</summary>
  Reliable detection of large language model (LLM)-generated text must remain effective under meaning-preserving text revisions, such as rewriting, polishing, and expansion. In practice, LLM outputs are often rewritten, polished, expanded, translated, or lightly edited before publication, weakening the lexical, syntactic, and local discourse cues used by many existing detectors. We introduce \textbf{M}atched \textbf{C}onditional-\textbf{R}esponse \textbf{P}robing (\textbf{MCRP}), a frozen-LLM prob...
  </details>

- **2026-10-28** — George J. Ziavras, Ziqiao Zhang, Shreyas Sundaram et al. — [Belief-Driven Search in Connectivity-Constrained Mobile Sensor Networks with Convergence Guarantees](http://arxiv.org/abs/2610.38256v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent search and coverage is critical to autonomous exploration, search-and-rescue, and defense applications. This paper investigates settings where a mobile sensor network is tasked with coordinating to discover the position of a stationary target within a bounded region. We develop a Bayesian update scheme where agents iteratively combine local uncertainties derived from their sensor measurements through inverse variance weighting to get a better global understanding of where the target ...
  </details>

- **2026-10-28** — Xiaoyang Wang, Tianrui Wang, Christopher C. Yang — [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](http://arxiv.org/abs/2610.38215v1)
  <details><summary>📄 Abstract</summary>
  Clinical large language models are increasingly fielded as multi-agent teams, on the assumption that deliberation averages out individual error. It does not average out bias. Across a full factorial of five model families and four aggregation topologies on 120 real MIMIC-IV emergency cases under counterfactual demographic swaps, no configuration neutralizes the disparity: all 20 cells commit the direction of their agents' independent answers, giving Black patients more acute triage. Every model ...
  </details>

- **2026-10-28** — Erfan Arvan, Michael D. Ernst, Martin Kellogg — [Template-Free Dynamic Invariant Detection](http://arxiv.org/abs/2610.38130v1)
  <details><summary>📄 Abstract</summary>
  A dynamic invariant detector proposes invariants, such as method pre- and postconditions, and rules out those that do not hold at run time. Traditional detectors propose invariants from a fixed library of templates, which limits their expressiveness. A large language model (LLM) can propose invariants instead of, or in addition to, template-derived ones. With the right prompt and context choices, we found that this idea can both improve the invariants' expressiveness and reduce the cost of infer...
  </details>

- **2026-10-28** — Ogen Schlachet Drukerman, Einat Minkov — [Author-Informed Stance Detection: A Dataset and Findings](http://arxiv.org/abs/2610.39019v1)
  <details><summary>📄 Abstract</summary>
  Stance detection in social media is challenging, as interpreting a text often requires understanding the author's perspective. We re-frame political stance detection as an author-informed text understanding task, where it is desired to infer both the author's political leaning and their stance towards the target from the text. We first show that human annotators struggle to infer authors' political leanings and stances from individual tweets, and that pretrained large language models (LLMs) perf...
  </details>

- **2026-10-28** — Xiaohan Zhang, Ying Zhao, Ruilin Guo et al. — [Implicit Minor Detection from Multi-Turn Dialogue in High-Risk AI Interactions: A Constrained Self-Evolving LLM Harness](http://arxiv.org/abs/2610.38546v1)
  <details><summary>📄 Abstract</summary>
  In high-risk text interactions, a system may need to estimate whether the current speaker is likely to be a minor before applying age-conditioned safeguards. Many text-based dialogue systems lack strong identity signals such as account information, verified identity, facial data, or device data, and must rely on weak cues that emerge across multiple turns. We formulate implicit minor detection under weak identity information as a high-risk user-attribute inference task and propose a constrained ...
  </details>

- **2026-10-28** — Sripathi Sridhar, Yujin Kim, Giovana Morais et al. — [MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes](http://arxiv.org/abs/2610.38276v1)
  <details><summary>📄 Abstract</summary>
  Audio captioning benchmarks typically evaluate a single unstructured free-text description of an audio scene, providing limited insight into how a model fails to understand polyphonic audio. A plausible caption may omit a source, or conflate multiple sources into one, or assign an attribute of one source to another, and conventional captioning evaluation cannot locate these errors. We introduce MixCardBench, a benchmark for structured captioning of polyphonic audio, which evaluates models in two...
  </details>

- **2026-10-28** — Zixuan Wang, Changbo Shi, Ji Liu — [TGTV: An Interpretable Framework for UAV Fault Detection and Traceability via Spatiotemporal Graph Learning and Large Language Models](http://arxiv.org/abs/2610.38106v1)
  <details><summary>📄 Abstract</summary>
  Fixed-wing unmanned aerial vehicles experience operating-condition transitions, asynchronous sensor sampling, and control-system compensation that can obscure fault signatures. Existing temporal detection methods have limited capacity to represent coupled faults across subsystems, track their evolution, and constrain language-model diagnoses with quantitative evidence. This paper proposes TGTV, an interpretable fault detection and traceability framework that integrates spatiotemporal graph learn...
  </details>

- **2026-10-27** — Zhusi Zhong, Carl M. Porto, David Hong et al. — [Large Language Models for Accurate Medical Chart Abstraction: Enabling Scalable and Secure Artificial Intelligence Deployment in Stroke](http://arxiv.org/abs/2610.38009v1)
  <details><summary>📄 Abstract</summary>
  Medical chart abstraction transforms unstructured clinical narratives into structured variables for research and quality monitoring. We evaluated a prompting-based large language model (LLM) framework for extracting eight clinical variables from 2,416 neurointerventional acute stroke intervention reports across three hospitals. Twenty-two instruction-tuned open-source LLMs were evaluated across architectures, model sizes, and biomedical adaptations using Quick Response and Chain-of-Thought (CoT)...
  </details>

- **2026-10-27** — Pau Amaro Seoane, Qimin Song, Shao-Dong Zhao et al. — [Seeing Unseen Gravitational Wave Inspirals at the Galactic Center](http://arxiv.org/abs/2610.37757v1)
  <details><summary>📄 Abstract</summary>
  The Galactic Center is expected to host a population of extremely large mass-ratio inspirals (X-MRIs) migrating toward the supermassive black hole. We propose an observational approach utilizing the secular gravitational torque exerted by X-MRIs on the highly eccentric S-star S301. This approach is intrinsically limited by the stochastic nature of the surrounding stellar-mass black hole cusp. As S301 propagates through this granular medium, it experiences discrete gravitational encounters. Stand...
  </details>

- **2026-10-27** — Jiarui Yao, Ruida Wang, Tong Zhang — [OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery](http://arxiv.org/abs/2610.37739v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown increasing promise in research-level problem solving, yet a comprehensive collection of such problems is still missing, and evaluating them on research-level problems remains challenging. We introduce OpenFrontiers, a cross-disciplinary resource that combines a structured corpus of open research problems with a retrospective benchmark of recently resolved problems in mathematics. The corpus records problem statements, context, progress, and other informati...
  </details>

- **2026-10-27** — Carlos Peláez-González, Francisco Herrera, Andrés Herrera-Poyatos — [Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence](http://arxiv.org/abs/2610.37962v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used as recommendation generators in conversational recommender systems (RS) via retrieval-augmented generation (RAG). This flexible design introduces new sources of structural bias. This paper studies positional bias in top-1 and single-turn LLM-based RS: systematic dependence of the recommended item on the order in which candidates are presented in the prompt. We propose two complementary detection methodologies: (i) POB-ICM, based on contingency m...
  </details>

- **2026-10-27** — Yuelin Han — [The Envelope Layer: An Underestimated Surface of LLM Agent Defense](http://arxiv.org/abs/2610.37415v1)
  <details><summary>📄 Abstract</summary>
  Prior work framed the envelope layer as the channel through which malicious content enters an agent, and established it as a defense surface independent of the LLM layer and the agent layer; however, that work only tested the envelope layer briefly and did not examine how label strength, envelope authenticity, scaffold differences, or existing memories affect defense effectiveness. Following its GDA Measurement methodology and the A/B/C/D outcome taxonomy, this paper takes the A2A-TIBA attack as...
  </details>

- **2026-10-27** — Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz et al. — [TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](http://arxiv.org/abs/2610.37571v1)
  <details><summary>📄 Abstract</summary>
  Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which a...
  </details>

- **2026-10-27** — Avid Fayaz, Harry Zhang, Håvard Alstadheim et al. — [Test-Time Communication in Trading Agent Swarms](http://arxiv.org/abs/2610.37448v1)
  <details><summary>📄 Abstract</summary>
  Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent decision-makers rather than a team, for which convergence is a risk and not the goal. We ran 200 agents from four model families in groups of ten under five communication regimes, from isolation to message boards and share...
  </details>

- **2026-10-27** — Hayden Arnold — [Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE](http://arxiv.org/abs/2610.37397v1)
  <details><summary>📄 Abstract</summary>
  We describe the agent we submitted to the GLEE Competition, which plays bargaining, negotiation, and persuasion games against a shared pool of human and AI opponents. The agent is built around three central components: a classical game-theoretic solver to compute numeric moves, an online Bayesian layer to estimate opponent archetypes, and a language model to write accompanying messages. We utilize Rubinstein bargaining for bargaining, Faratin concession for negotiation, and Kamenica--Gentzkow di...
  </details>

- **2026-10-27** — Tianrong Zhang, Yakun Zhang, Dan Hao — [HIDE: Hierarchical Isolation via Documentation and Evidence for Rustc Bugs](http://arxiv.org/abs/2610.37343v1)
  <details><summary>📄 Abstract</summary>
  Rustc bugs can prevent valid programs from compiling or cause incorrect compilation results, making the identification of responsible source files essential for repair. Using large language models (LLMs) for rustc bug isolation raises three challenges. First, distributed compiler functionality requires understanding both what individual files do and how they work together. Second, a large source file search space makes exhaustive analysis of all files costly. Third, including documentation and s...
  </details>

- **2026-10-27** — Juyoung Seo, Geonwoo Bang, Dongho Kim et al. — [ReForest: Interpretability Meets Reasoning in Isolation Forest](http://arxiv.org/abs/2610.37316v1)
  <details><summary>📄 Abstract</summary>
  Statistical anomaly detection methods like Isolation Forest are efficient but suffer from a critical semantic gap. They identify numerical rarities but fail to understand the contextual meaning of data, often missing subtle, context-dependent anomalies. Conversely, Large Language Models possess strong semantic reasoning capabilities but are prohibitively expensive and slow for large-scale deployment. To bridge this gap, we propose ReForest, a novel framework that synergizes the statistical effic...
  </details>

- **2026-10-27** — Bilge Celik, Anna Vettoruzzo, Joaquin Vanschoren — [CaLLM: Continual Adaptation of LLMs via Non-Parametric Adapter Routing](http://arxiv.org/abs/2610.36994v1)
  <details><summary>📄 Abstract</summary>
  Continual adaptation of large language models (LLMs) to evolving task distributions while mitigating catastrophic forgetting remains an open problem. Existing strategies often struggle to scale or lack a robust mechanism for zero-shot task-to-expert assignment. We introduce CaLLM, a framework that resolves these tensions by combining metric-based meta-learning with modular parameter isolation via lightweight adapters. First, CaLLM projects each input batch into a task-agnostic embedding space to...
  </details>

- **2026-10-27** — Priyanka Goyal, Maitreyee Sar, Adway Mitra et al. — [Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability](http://arxiv.org/abs/2610.36857v1)
  <details><summary>📄 Abstract</summary>
  Earth Observation (EO)-based agricultural monitoring is shifting from pixel-level spectral analysis toward representation-driven modeling, yet systematic evaluation of learned representations across spatial, temporal, and domain-generalization dimensions remains limited. Geospatial foundation models generate high-dimensional embeddings encoding spatio-temporal land-surface properties, but their utility for agricultural applications remains insufficiently understood. This study presents a represe...
  </details>

- **2026-10-27** — Haocheng Mei, Yuchuan Tian, Ye Yuan et al. — [API-TAIL: Detecting Model Substitution in LLM APIs through Temperature-Aligned Likelihood Tails](http://arxiv.org/abs/2610.36801v1)
  <details><summary>📄 Abstract</summary>
  Commercial language model APIs return only text, allowing a provider to cut costs by quietly routing a fraction of user requests to a cheaper substitute model while billing for the advertised one. Detecting such partial substitution is challenging because honest providers also alter the output distribution through undocumented decoding and serving choices, such as temperature scaling, sampling truncation, repetition and presence penalties, and default system prompts, forcing an audit to test aga...
  </details>

- **2026-10-27** — Chi Wang, Min Gao, Yifei Zhang et al. — [Beyond the Evidence Coherence Trap: Agent-Driven Evidence Selection for Temporally Disordered Fake News Detection](http://arxiv.org/abs/2610.36764v1)
  <details><summary>📄 Abstract</summary>
  Fake news undermines public trust and the integrity of online information ecosystems. Temporally disordered fake news is especially elusive because it rearranges factual events into a false chronology. Individual events may remain factually valid even when their temporal relations are misrepresented. When similar events involving the same entity recur, retrieval may return semantically plausible evidence from the wrong period. Consequently, independent event verification may rely on locally cohe...
  </details>

- **2026-10-27** — Joosung Kim, Luyonghe Li, Shanwen Wu — [Peak-DNA: Recurrent Morphology in Global Narrative Propagation](http://arxiv.org/abs/2610.36571v1)
  <details><summary>📄 Abstract</summary>
  Global narrative streams exhibit noisy, fragmented, and asynchronous amplification bursts, making direct waveform comparison unreliable for recurrence analysis. This paper introduces Peak-DNA, a framework for identifying recurrent propagation morphology in global narrative streams. The proposed framework transforms hourly GDELT activity into normalized macro-peak episodes through denoising, macro-peak consolidation, and temporal alignment, and compares propagation morphology using DTW-based simi...
  </details>

- **2026-10-27** — Kai Qian, Dongjie Xu, Weijie Shi et al. — [Decoupling Consistency and Conflict across MLLM Layers for Fake News Detection](http://arxiv.org/abs/2610.36569v1)
  <details><summary>📄 Abstract</summary>
  The trustworthiness of Web content faces a growing threat from multimodal fake news. Real news usually shows aligned image-text semantics, while fake news often contains a few conflicts at varying levels, such as mismatches in objects, scenes, events, and claims. However, existing methods usually treat consistency and conflict in a coarse and static way, limiting their ability to capture sparse conflicts and adapt to varying conflict levels. Inspired by the distinct knowledge encoded across laye...
  </details>

- **2026-10-27** — Nardine Basta, Venus Haghighi, Dali Kaafar et al. — [Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure](http://arxiv.org/abs/2610.36453v1)
  <details><summary>📄 Abstract</summary>
  LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users, yet it remains unclear whether they distinguish correction from manipulation or merely differ in their propensity to concede. We examine this question across seven LLMs from four vendors in two studies, one on the answer...
  </details>

- **2026-10-27** — Fangran Miao, Shengjie Niu, Jian Huang et al. — [Is Your LLM Relay Serving What It Claims? A low-cost and high-power test for LLM Relay Auditing](http://arxiv.org/abs/2610.37086v1)
  <details><summary>📄 Abstract</summary>
  Relay and reseller APIs have become a common way to access large language models (LLMs), yet users cannot directly verify whether they receive the models they request and pay for. This opacity motivates LLM relay auditing, but existing methods struggle to combine low cost, robustness to benign deployment changes, and statistically interpretable decisions under black-box access. To address these limitations, we propose distributional fingerprint auditing (DFA), a statistical method that requires ...
  </details>

- **2026-10-27** — L. E. Rodríguez, M. Cruces, G. Voisin et al. — [Self lensing in BH-NS binaries as progenitors for periodically repeating Fast Radio Bursts](http://arxiv.org/abs/2610.37052v1)
  <details><summary>📄 Abstract</summary>
  Fast radio bursts (FRBs) are bright extragalactic transients whose origin remains uncertain. The discovery of repeating FRBs, some with cyclic activity windows, opens new prospects for testing their progenitors. Neutron stars (NSs) are strong candidates, as they naturally emit radio pulses with temporal and spectral properties resembling those of FRBs, an interpretation reinforced by the detection of an FRB-like burst from the Galactic magnetar SGR 1935+2154. Nevertheless, the pulse energy of ty...
  </details>

- **2026-10-27** — Zhangkai Wu, Xu Zhang, Zhihong Cui et al. — [Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift](http://arxiv.org/abs/2610.36585v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) are being applied to Web data streams such as network intrusion detection, where they adapt by updating the labelled rows of their context without retraining. When a past concept returns after leaving the context, a TFM faces a recall-or-relearn decision between restoring stored rows of the concept and relearning it from new labels. We propose MICE (Mixture of In-Context Experts), a training-free learner that cuts the stream into segments at detected changes. It ...
  </details>

- **2026-10-27** — Peiwang Tang, Cheng HE, Yupeng Ye et al. — [Learning from Points and Patches: A Pre-trained Hybrid Attention Transformer for Time Series Analysis](http://arxiv.org/abs/2610.36572v1)
  <details><summary>📄 Abstract</summary>
  Time-series data generated by Web services and connected systems support applications such as user activity analysis, service monitoring, and resource management. However, learning transferable representations from heterogeneous time series remains challenging due to diverse temporal patterns, variable sequence lengths, and limited high-quality annotations. Despite the success of pre-training in natural language processing and computer vision, effective time-series pre-training requires strategi...
  </details>

- **2026-10-26** — Leo Benaharon, Chi Zhang, Wei Zheng et al. — [Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security](http://arxiv.org/abs/2610.36143v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can adapt robotic software by revising executable programs, but successful responses to an evolving opponent may not remain effective. We present a framework for program-level adversarial co-adaptive self-play in which coding agents generate attacks and defenses from tested opponent code and mission feedback, without model fine-tuning. Environment-specific interfaces support external programs for autonomous driving and SDK-level defenses for humanoid locomotion. Two eight-generatio...
  </details>

- **2026-10-26** — Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al. — [I-HITL: Inalienable Human-in-the-Loop](http://arxiv.org/abs/2610.35835v2)
  <details><summary>📄 Abstract</summary>
  Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the concept of inalienable human-in-the-loop (I-HITL). An I-HITL protocol ensures that an agent can initiate an action only with explicit human approval, even when the human interacts with a system (e.g., a local agentic harne...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 44 papers

- **2026-10-29** — Zach Paris, Emily Finn — [A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening](http://arxiv.org/abs/2610.40511v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three naturalistic language-listening datasets spanning intracranial electrophysiology and f...
  </details>

- **2026-10-29** — Zhenghong Ke, Jingbo Zhou, Hua Wu — [SCARL: Sequence Confidence-Aligned Reinforcement Learning](http://arxiv.org/abs/2610.40407v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning by scoring sampled responses with a rule-based verifier and reinforcing those that pass. Where a classifier's training couples predicted probability to labels, nothing ties an RLVR policy's confidence in a response to its reward: aligned training would drive responses with the same advantage toward equal confidence, yet the advantage is blind to confidence. Under this sequence-confidence misalignment, a succe...
  </details>

- **2026-10-29** — Behnam Moradi — [The Athlete as a Scientist of One: Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables](http://arxiv.org/abs/2610.40370v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents for personal health read wearable data and recommend, but do not learn about the individual in a way that can be audited or falsified. We present EpiCoach, an agentic system that treats one athlete, a cross-country mountain biker, as the subject of accountable N-of-1 science. Claims about the athlete live in an evidence-gated hypothesis registry: each must issue a probabilistic prediction about a future session before it occurs, and its belief moves only through...
  </details>

- **2026-10-29** — Yuzhe Wu, Zijun Lin, Yeying Jin — [Wizard: Manipulate Any World in Real Time via Agentic Control](http://arxiv.org/abs/2610.40339v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined motion patterns, generalize poorly to unseen environments and characters, and offer l...
  </details>

- **2026-10-29** — Zhiyuan Fang, Dingyang Li, Jianfeng Zhong et al. — [Rimuru: Unified Memory Management for Modern LLM Serving via Elastic Expert Offloading](http://arxiv.org/abs/2610.40305v1)
  <details><summary>📄 Abstract</summary>
  Modern LLMs strain device memory through large model weights and attention states, particularly in resource-constrained scenarios. Existing systems separately provision memory for model weights and attention states, imposing fixed fixed boundaries that cannot adapt to the changing memory demands of workloads. Under heavy workloads, insufficient state capacity limits request concurrency and reduces throughput; under light workloads, idle memory in one region cannot be reallocated to another, wast...
  </details>

- **2026-10-29** — Serwan Jassim, Victoria Bosch, Daniel Anthes et al. — [Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI](http://arxiv.org/abs/2610.40280v1)
  <details><summary>📄 Abstract</summary>
  Decoding sensory-evoked functional magnetic resonance imaging (fMRI) data is a central analytical tool in cognitive neuroscience. Here we ask whether self-supervised learning (SSL), which has been scarcely explored in this domain, can yield representations that support strong downstream performance. To do so, we adapt a joint embedding predictive architecture (JEPA) to train participant-specific encoders on brain data alone. The encoders never see the stimulus images or any representation derive...
  </details>

- **2026-10-29** — Guangzhi Wang, Junfu Pu, Yiran Wang et al. — [TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents](http://arxiv.org/abs/2610.40276v1)
  <details><summary>📄 Abstract</summary>
  Building general game agents requires both high-level task reasoning and low-latency action control in rapidly changing visual environments. These capabilities favor models with substantially different computational profiles, making them difficult to realize within a single model. In this work, we present TaskFrame, a hierarchical planner-controller framework that connects task-level planning with frame-level keyboard-and-mouse control. A vision-language task planner decomposes a high-level goal...
  </details>

- **2026-10-29** — Hongyu Bai, Jiaqi Zeng, Chunzheng Zhu — [Aligning Medical Vision Language Models at the Capability Boundary with Entropy Adaptive Rubric Grounding](http://arxiv.org/abs/2610.39835v1)
  <details><summary>📄 Abstract</summary>
  Medical diagnostic reasoning requires verifiable links between visual evidence and clinical knowledge, yet current medical vision language models are aligned with objectives that reward the wrong behavior. Uniform supervised fine tuning lets easy cases dominate updates while clinically critical boundary cases saturate prematurely. Sparse rewards based only on final-answer correctness cannot assess anatomical grounding or clinical logic, inviting reward hacking through answer shortcuts. We propos...
  </details>

- **2026-10-29** — Yuan Wang, Wei Wu, Hongning Wang — [Look at Where You Think: Localization-Head Alignment for Fine-Grained Perception in Thinking VLMs](http://arxiv.org/abs/2610.39649v1)
  <details><summary>📄 Abstract</summary>
  Thinking vision-language models reason for thousands of tokens, yet still miss small details in high-resolution images. Zooming methods pay for extra inference passes, and outcome rewards never tell the model where to look at. In Qwen3.5-4B, we find that the bottleneck is selection, not seeing: a few attention heads, which we call localization heads, pick the evidence out of thousands of visual tokens; ablating four of them costs 13.2 points more than ablating four random heads, and their focus ...
  </details>

- **2026-10-29** — Szymon Lis, Robert Ślepaczuk, Paweł Sakowski — [Information Flow and Market Risk: Transformer-Based Evidence on Sentiment and Volatility Dynamics](http://arxiv.org/abs/2610.39636v1)
  <details><summary>📄 Abstract</summary>
  This study examines whether transformer-based financial news sentiment improves equity volatility forecasts beyond conventional market-based predictors. Using data for eleven US stocks, we compare volatility persistence models with specifications incorporating the VIX, AAII investor sentiment, and news sentiment extracted using ModernFinBERT. The forecasting target is annualized volatility constructed from future averages of trailing 252-session Yang-Zhang estimates, evaluated at horizons of 1, ...
  </details>

- **2026-10-29** — Yixue Zhang, Wenke Xia, Kun Wu et al. — [From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models](http://arxiv.org/abs/2610.39543v1)
  <details><summary>📄 Abstract</summary>
  Reasoning informs decision-making by connecting intended actions with their expected consequences. Recent vision-language-action (VLA) models incorporate embodied chains of thought (ECoTs) to guide action generation. However, such guidance remains implicit, as actions are conditioned on ECoTs rather than explicitly optimized to align with them.   We introduce CoRAct, a consequence-grounded reasoning-to-action alignment framework that explicitly aligns reasoning and action through reward-guided o...
  </details>

- **2026-10-29** — Randall Balestriero, Yann LeCun — [Proving and Improving the Platonic Representation Hypothesis with JEPAs](http://arxiv.org/abs/2610.39302v1)
  <details><summary>📄 Abstract</summary>
  Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the hypothesis into a theorem. First, we prove a \emph{Platonic Representation Theorem}: Joint-Embedding Predictive Architectures (JEPAs) trained separately on any number of modalities learn the same representation up to one rota...
  </details>

- **2026-10-29** — Yunhang Shen, Zhangquan Chen, Xiaotian Li et al. — [Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities](http://arxiv.org/abs/2610.39301v1)
  <details><summary>📄 Abstract</summary>
  We present Youtu-Parsing-Omni, an omni-modal parser that converts documents, images, audio, and video into structured records grounded in space and time, providing a perception layer for agents that read, locate, and cite evidence across modalities. Its design rests on one encoder for every modality and one schema for every task. Youtu-Omni-Encoder, initialized from a pre-trained language model to strengthen text reading, encodes all modalities with shared weights in a unified space-time coordin...
  </details>

- **2026-10-29** — Oscar Mickelin, Yunpeng Shi, Amit Singer et al. — [Fast rigid rotational alignment of voxelized 3-D density maps in sliced Wasserstein distance](http://arxiv.org/abs/2610.39214v1)
  <details><summary>📄 Abstract</summary>
  We develop a fast method for the rigid alignment of voxelized three-dimensional density functions over $\mathsf{SO}(3)$ using sliced optimal transport. Our approach efficiently transforms each density map into a tensor of one-dimensional quantile functions, taken from central slices over the unit sphere, such that the Euclidean distance of the transformed volumes approximates the sliced 2-Wasserstein distance. Our formulation is therefore compatible with existing, fast, voxel-based Euclidean ali...
  </details>

- **2026-10-29** — Eli A. Underwood, Nicolas Rondan, Angel V. Peterchev et al. — [Joint Rigid Alignment and Morphable Reconstruction from Partial 3D Face Scans](http://arxiv.org/abs/2610.39161v1)
  <details><summary>📄 Abstract</summary>
  Aligning a partial, real-world 3D face scan to a canonical representation requires solving two coupled problems at once: estimating the rigid pose that brings the scan into a common frame, and completing the facial shape in regions the scan never observed. Existing pipelines typically decouple these steps, running a generic point-cloud registration front end followed by a separate non-rigid fitting or deformation stage. Building on the GeoTransformer superpoint-matching architecture, we propose ...
  </details>

- **2026-10-28** — Ava Iranmanesh, Sobhan Lotfi, Ali Iranmanesh et al. — [HEARSAYBENCH: Can AI Navigate from Abstract Human Rights to Lived Lives?](http://arxiv.org/abs/2610.39062v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) reach users worldwide, personal counseling has emerged as one of their most consequential applications, sometimes in life-critical situations. Yet broader access does not mean equal support. The text these models learn from disproportionately reflects people with the freedom to act, embedding an implicit assumption that users can leave, report, seek help, or appeal. Existing benchmarks largely inherit this assumption, overlooking users whose agency is constrained ...
  </details>

- **2026-10-28** — Tianjian Li, Chuanyang Jin, Seungone Kim et al. — [Aligning Autoresearch: Co-Improvement between Agents and Humans](http://arxiv.org/abs/2610.38882v1)
  <details><summary>📄 Abstract</summary>
  Autoresearch agents can now attempt long-horizon AI research end-to-end, i.e., self-improvement. However, best results are still obtained by research agents interacting with human researchers, and improving AI's ability to perform this co-research will only reinforce this effect---a process termed co-improvement (Weston and Foerster, 2025). Further, aligning with human expectations is likely a safer path for research agents, especially given recent agent reward hacking phenomena (OpenAI, 2026b)....
  </details>

- **2026-10-28** — Mosab Alfaqeeh, Omar Hourani, Muath Hourani et al. — [Beyond fabrication: Misattributed numbers in papers written by AI research agents](http://arxiv.org/abs/2610.38691v1)
  <details><summary>📄 Abstract</summary>
  Verifying numerical claims in research written by AI agents is an important but challenging problem. Recent benchmarks show that many agent-written papers fail integrity checks, but such verdicts, often produced by a single LLM judge, identify failure without explaining its nature, and existing checks either test a paper for internal consistency or test whether a reported value appears somewhere in an agent's output. We re-analyze all 540 released judgments from a recent public benchmark of AI r...
  </details>

- **2026-10-28** — Elad Aspis, Sharon Gannot — [MiDiff: MIDI-Conditioned Diffusion Models for Drum Audio Enhancement](http://arxiv.org/abs/2610.38619v1)
  <details><summary>📄 Abstract</summary>
  Bridging the semantic gap between perfect symbolic musical structure and severely degraded acoustic signals offers a powerful paradigm for high-fidelity audio restoration. We introduce MiDiff, a diffusion-based generative model for drum audio enhancement that conditions the reverse process on temporally aligned Musical Instrument Digital Interface (MIDI) piano rolls. We extend the Score-Based Generative Models for Speech Enhancement (SGMSE) framework in the complex Short-Time Fourier Transform (...
  </details>

- **2026-10-28** — Frederick Riemenschneider, Anette Frank — [Leaving the Cave by Breaking the Symmetry: Identifiable Structure Can Enable Cross-Lingual Generalization](http://arxiv.org/abs/2610.38509v1)
  <details><summary>📄 Abstract</summary>
  Why do multilingual language models generalize across languages even without shared vocabulary? The Platonic Representation Hypothesis posits that models trained on different data, objectives, and modalities converge toward a shared statistical model of reality. Extending this intuition to representations inside a single multilingual model, we propose the Relational Identifiability Hypothesis: relations in a shared world can promote entity alignment by ruling out alternative cross-lingual corres...
  </details>

- **2026-10-28** — Zhiyuan Xiang, Xiang Deng, Wanjie Tao et al. — [CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization](http://arxiv.org/abs/2610.38357v1)
  <details><summary>📄 Abstract</summary>
  Discretizing continuous actions into discrete skills using methods like VQ-VAE has emerged as a powerful paradigm for robotic manipulation. However, quantization errors yield a suboptimal distribution for the skill prior, degrading its performance. While reinforcement learning offers a path for refinement, its direct application faces unstable encoder updates and a granularity dilemma in importance sampling. To address these challenges, we introduce Cascaded Skills Optimization (CSO), a two-stag...
  </details>

- **2026-10-28** — Qiming He, Jing Li, Zihan Wang et al. — [Knowledge-structured and evidence-aware semantic self-distillation for glomerular pathology foundation model](http://arxiv.org/abs/2610.38346v1)
  <details><summary>📄 Abstract</summary>
  Visual foundation models learn rich pathological morphology but lack explicit concept-level supervision. Vision--language pretraining can provide this supervision but requires costly image--text pairs. Here, we introduce GloSAGE, a semantic self-distillation framework that uses lesion profiles predicted by a pretrained visual teacher to construct structured pathology descriptions. Reliability-guided selection identifies image--text anchors, while Knowledge-Structured Pathology Text Synthesis and...
  </details>

- **2026-10-28** — Ulyana Tkachenko, Hui Wen Goh, Guram Gogia et al. — [Rubricon: Automated Rubric Generation and Refinement for LLM Evaluation and Training](http://arxiv.org/abs/2610.38220v1)
  <details><summary>📄 Abstract</summary>
  Rubrics enable reward assignment on tasks without verifiable answers, but are expensive to manually produce from scratch. We present Rubricon, a pipeline that generates discriminative rubrics without requiring human preference labels, rubric annotation, or generator-model training. Using any LLM, Rubricon samples multiple rubrics, selects the most discriminative candidate, adds criteria to capture overlooked requirements or response flaws, and prunes criteria that are misaligned or shallow. Alon...
  </details>

- **2026-10-28** —  NVIDIA,  :, Aastha Jhunjhunwala et al. — [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](http://arxiv.org/abs/2610.38095v1)
  <details><summary>📄 Abstract</summary>
  We introduce Nemotron 3.5 Super and Nemotron 3.5 Lightning, open and efficient Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic workloads. Super is a 120B-parameter, 12B-active multimodal model, while Lightning is a smaller 30B-parameter, 3B-active text model; both designed for efficient deployment. Both models combine large-scale distillation, long-context training, and native speculative decoding, while Super further incorporate...
  </details>

- **2026-10-27** — Karol Musielinski, Fanurs C. E. Teh, Takahiko Koyama et al. — [Separability Is Not Alignability: Representations for Spectrum-to-Molecule Retrieval](http://arxiv.org/abs/2610.37979v1)
  <details><summary>📄 Abstract</summary>
  Identifying a small molecule from its tandem mass spectrum is limited by paired data. Foundation models offer a way around this scarcity: pretrain a spectrum encoder on unlabeled spectra and a molecule encoder on a large corpus of structures, then align the two frozen representations, as in vision-language and as the Platonic Representation Hypothesis suggests. We audit this route on MassSpecGym with spectrum encoders retrained free of test-fold contamination. Alignment needs a metric relating d...
  </details>

- **2026-10-27** — Chen Lyu, Phong Do, Gabriele Pergola — [Human-Residual Steering: Aligning Frozen LLM Judges with Human Judgment Distributions](http://arxiv.org/abs/2610.37868v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are widely used as automated judges, yet most alignment methods target aggregated human judgments and overlook variation among individual annotators. Existing approaches to matching the full distribution of human ratings mainly rely on output-level calibration or parameter fine-tuning. We propose Human-Residual Steering (HRS), to our knowledge the first method to align frozen LLM judges with human judgment distributions through learned hidden-state interventions. An ...
  </details>

- **2026-10-27** — Fang Sun, Hekai Cheng, Ruoyan Li et al. — [Where the Error Lives: Spectral Representations of Learned Kohn-Sham Hamiltonians](http://arxiv.org/abs/2610.37843v1)
  <details><summary>📄 Abstract</summary>
  Kohn-Sham density functional theory (DFT) is the standard method for computing the electronic structure of molecules and materials, but its self-consistent-field (SCF) iterations make it expensive for large systems and high-throughput screening. Machine-learned Hamiltonian models offer a shortcut: an equivariant network predicts the Kohn-Sham Hamiltonian matrix in one forward pass, and diagonalizing the prediction yields orbital energies, the HOMO-LUMO gap, molecular orbitals and the electron de...
  </details>

- **2026-10-27** — Hee Seung Hwang, Sanghyuk Chun, Xindi Wu et al. — [Multi-State Linear Attention with Generalized Second-Order Routing](http://arxiv.org/abs/2610.37645v1)
  <details><summary>📄 Abstract</summary>
  Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state using only the mean alignment between a query and each segment's keys, ignoring h...
  </details>

- **2026-10-27** — Raban Emunds, Jannis Blüml, Quentin Delfosse et al. — [Interpretable Meta-Policies for Neural Decision Making](http://arxiv.org/abs/2610.37451v1)
  <details><summary>📄 Abstract</summary>
  Deep Reinforcement Learning remains difficult to interpret and align due to the black-box nature of neural networks. While (neuro-)symbolic approaches improve transparency by incorporating symbolic reasoning, applying them directly to low-level actions results in overly complex, unreadable policies. We introduce NEXUS, a hierarchical RL framework that resolves this tension by combining neural skills with symbolic meta-policies. By shifting transparent reasoning to high-level skills rather than a...
  </details>

- **2026-10-27** — Ananth K Suresh, Aveen Dayal, Gouthaman KV et al. — [When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models](http://arxiv.org/abs/2610.37430v1)
  <details><summary>📄 Abstract</summary>
  For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or without identifying the missing evidence. We study how refusal on visually unanswerable questions is shaped by three sources of control: inference-time instructions, post-training, and inte...
  </details>

- **2026-10-27** — Haokun Wen, Xuemeng Song, Mong-Li Lee et al. — [Same Verdict, Different Readers: Personalizing Fact-Checking Explanations from Relative Preferences](http://arxiv.org/abs/2610.37380v1)
  <details><summary>📄 Abstract</summary>
  Fact-checking explanations help Web users understand why a claim receives its verdict, yet the same explanation may not satisfy readers with different backgrounds and preferences. We formulate Faithful Personalized Fact-Checking Explanation Rewriting, which adapts an existing explanation to individual readers while preserving factual fidelity. Rather than relying on reader-written reference explanations, we learn personalized rewriting from the relative preferences of LLM-simulated readers. Howe...
  </details>

- **2026-10-27** — Andrea Marino, Giovanni Sileno, Thomas van Binsbergen et al. — [Aligning Institutional Power and Operational Ability](http://arxiv.org/abs/2610.37342v1)
  <details><summary>📄 Abstract</summary>
  To be socially sustainable, Agentic AI systems require normative designs that align responsibilities with the ability to fulfil them. Identifying incongruences such as unsatisfiable expectations or privilege escalation is crucial in avoiding normative pitfalls. In this study, we discuss design dimensions suitable for describing multi-agent systems in light of this norm-ability alignment requirement. We propose a formal framework centred on process-oriented modelling and institutional power for t...
  </details>

- **2026-10-27** — Nicolas Tacheny, Tom Mens, Saïd Mahmoudi — [Mind the Intent Gap: A Methodology for Collaborative Agent-Driven Software Engineering](http://arxiv.org/abs/2610.37340v1)
  <details><summary>📄 Abstract</summary>
  AI agents have entered software teams, first as tools and now as team members. They produce in minutes what used to take days, yet the expected gain in delivery often fails to appear. We argue that they are entering processes designed for people, which quietly relied on people to cover three of their weaknesses. The team's intent was never fully written down, because colleagues filled the gaps. An AI agent fills them too, though by guessing, and drifts from what the team had in mind. The reasoni...
  </details>

- **2026-10-27** — Yu Zhang, Xiaogang Wang, Yuhang Cheng et al. — [Zhengrong-Spatial-Aware 1.0: Advancing 3D Multimodal Intelligence](http://arxiv.org/abs/2610.37216v1)
  <details><summary>📄 Abstract</summary>
  This report presents the implementation and validation of two end-to-end multimodal adaptation pipelines for 3D-aware visual question answering on a custom spatial dataset. The first pipeline fine-tunes HiSpatial-3B, which augments RGB observations with metric-scale 3D point maps; the second adapts Qwen3-VL through memory-efficient QLoRA-based supervised fine-tuning. The completed engineering stack covers dataset conversion, image-annotation alignment, monocular geometry preprocessing, instructi...
  </details>

- **2026-10-27** — Kensuke Sasaki, Issei Sato — [On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime](http://arxiv.org/abs/2610.37085v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences. Recent empirical work has revealed that DPO induces remarkably sparse parameter updates, yet no theoretical explanation for this phenomenon has been offered. We analyze DPO's optimization dynamics under a neural tangent kernel linearization and show that the logistic structure of the DPO loss gives rise to an implicit maximum-margin bias. Building on this observation, we introduce th...
  </details>

- **2026-10-27** — Kegeng Tang, Jingbo Wang, Yangming Zhang et al. — [Latent Visual Contrastive Reasoning with Multi-Branch Exploration](http://arxiv.org/abs/2610.36809v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have made substantial progress in visual question answering, but complex visual reasoning often requires locating and comparing multiple pieces of question-relevant visual evidence. Existing methods that move intermediate reasoning into the visual latent space usually follow a single linear reasoning trajectory, which can be limiting when multiple visual hypotheses or competing evidence regions are relevant. We propose Latent Visual Contrastive Reasoning, a branc...
  </details>

- **2026-10-27** — Wu Lin, Yan Fan, Chenxiang Ma et al. — [Nonlinear Direct Feedback Alignment for Scalable Backpropagation-Free Training](http://arxiv.org/abs/2610.36718v1)
  <details><summary>📄 Abstract</summary>
  Backpropagation (BP) remains the predominant algorithm for training deep neural networks, but it is biologically implausible and suffers from the backward locking problem, constraining parallelization across layers. Direct Feedback Alignment~(DFA), which propagates the global output error directly to each hidden layer via fixed feedback matrices, has emerged as a promising alternative for addressing these limitations. However, a significant performance gap persists between DFA and BP, which we a...
  </details>

- **2026-10-27** — Tomoyasu Shimada, Kazuhiko Murasaki, Shoichiro Takeda et al. — [SAGE: Semantic-Augmented Geometric Experts for Point Cloud Registration](http://arxiv.org/abs/2610.36658v1)
  <details><summary>📄 Abstract</summary>
  Point cloud registration is an essential task for scene reconstruction, requiring the alignment of partially overlapping point clouds. Under low-overlap conditions, this task remains challenging because existing geometry-only methods cannot distinguish geometrically similar but semantically distinct structures (e.g., TV corners vs. desk corners and chair legs vs. table legs), resulting in incorrect correspondences. To address this geometric ambiguity, we present Semantic-Augmented Geometric Expe...
  </details>

- **2026-10-27** — Binhang Qi, Yiming Liu, Yun Lin et al. — [Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](http://arxiv.org/abs/2610.36584v1)
  <details><summary>📄 Abstract</summary>
  As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents can generate tests that validate the required behavior when the implementation of that behavior is withheld. Existing test-generation benchmarks mostly focus on white-box testing, whereas the requirement--test-related st...
  </details>

- **2026-10-27** — Vansh Bhatia, Mehdi Rezagholizadeh, Parsa Ashrafi Fashi et al. — [PRISM-BENCH: Diagnosing Grounded and Faithful Multimodal Reasoning Beyond Final-Answer Accuracy](http://arxiv.org/abs/2610.36554v1)
  <details><summary>📄 Abstract</summary>
  Final-answer accuracy reports whether a vision-language model was right, but not whether its answer was grounded in the image, whether its stated reasoning reflects that evidence, or what the answer cost to produce. Those are the properties that decide whether a system can be deployed. We present PRISM-BENCH, a benchmark of 1,000 expert-curated questions spanning five under-represented reasoning categories, in which every item carries an idealized reasoning trace written by one human annotator a...
  </details>

- **2026-10-27** — Yashuo Luo, Qianren Mao, Ziqi Qin et al. — [From Solver Trajectories to Teaching Trajectories: Cognition-Aligned Reasoning Distillation](http://arxiv.org/abs/2610.36445v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation from large reasoning models (LRMs) often uses raw teacher trajectories as supervision. However, this practice creates a mismatch between the goal of distillation and the nature of teacher trajectories. Advanced LRMs typically improve their reasoning capabilities through reward-driven post-training, such as RLHF. This training optimizes them as strong solvers, rather than as teachers that produce reasoning processes smaller models can easily learn. Since smaller models have...
  </details>

- **2026-10-27** — Xianxiang Zhao, Advik Mehta, Falak Sethi et al. — [LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction](http://arxiv.org/abs/2610.36433v1)
  <details><summary>📄 Abstract</summary>
  Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inconsistent quality, with 25% of crews never conducting pretask planning (Olson et al., 2016), diverting safety personnel from field supervision. This study proposes the Lightweight Multi-Agent DSB System (LM-DSB), which i...
  </details>

- **2026-10-27** — Giuseppe Curci, Stefano Simonazzi, Andrea Molinari et al. — [Exploring the Limits of the Delta Learning Hypothesis: Single-Pair Generator Biases in Direct Preference Optimization](http://arxiv.org/abs/2610.37058v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) typically relies on preference pairs generated from diverse model pools and ranked by an external LLM judge. The recently proposed delta-learning hypothesis suggests that comparable supervision can instead be obtained from a single pair of models by treating the larger model's response as preferred. We investigate the limits of this approach across model families and scales. We show, both theoretically and empirically, that fixed model pairs introduce systema...
  </details>

- **2026-10-26** — Bingliang Zhang, Wenda Chu, Yizhuo Li et al. — [SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model](http://arxiv.org/abs/2610.36419v1)
  <details><summary>📄 Abstract</summary>
  We present Scalable Pixel-anchored End-to-end Diffusion (SpeeDiff), a latent diffusion method that jointly trains the VAE and the diffusion model from scratch. In principle, joint training allows the diffusion loss gradient to directly guide the VAE encoder, encouraging the formation of a generation-friendly latent space and potentially yielding faster convergence than the conventional two-stage approach with a pretrained frozen VAE. However, a naive end-to-end implementation severely degrades p...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 48 papers

- **2026-10-29** — Xiaoning Ren, Jiayang Song, Chongyang Liu et al. — [Unraveling the Efficacy of Neuron Coverage Criteria on Testing Large Language Models](http://arxiv.org/abs/2610.40234v1)
  <details><summary>📄 Abstract</summary>
  Neuron coverage criteria aim to assess test suite quality and guide test input generation, but their effectiveness for Transformer-based language models remains unclear. We evaluate six criteria, including four established and two recent criteria, across encoder-only, decoder-only, and encoder-decoder models. Our evaluation examines error-revealing capability, distribution diversity, sample fairness (category diversity), and guidance for test input generation. The results reveal uneven effective...
  </details>

- **2026-10-29** — Meir Ariel — [Syndrome Trellis Decryption in Post-Quantum Cryptography](http://arxiv.org/abs/2610.39873v1)
  <details><summary>📄 Abstract</summary>
  We present a novel post-quantum cryptographic framework based on masked high-memory convolutional codes in the Niederreiter paradigm. The public key is derived from a high-memory polynomial parity-check matrix augmented by dense random masking and additional invertible linear transformations. The resulting matrix exhibits strong random-like properties, effectively concealing its algebraic structure and resisting known structural and algebraic attacks. Legitimate recipients retain polynomial-time...
  </details>

- **2026-10-29** — Zhenghao Wu, Ruihai Dong, Reza Farahani et al. — [Can We Rely on Language Models to Orchestrate Services across the Edge-Cloud Continuum?](http://arxiv.org/abs/2610.40477v1)
  <details><summary>📄 Abstract</summary>
  Service orchestration across the edge--cloud continuum increasingly uses language models (LMs) to translate intents and operational evidence into scheduling, configuration, diagnosis, and remediation decisions. Yet, useful model outputs do not by themselves establish dependable orchestration: reliability also depends on where the LM enters the decision process, what authority it is granted, how actions are constrained, and what system-level evidence supports the claimed effect. Existing surveys ...
  </details>

- **2026-10-29** — Robert Pasternak — [Prompts and probabilities in the linguistic assessment of language models: Evidence from semantic focus-sensitivity](http://arxiv.org/abs/2610.39923v1)
  <details><summary>📄 Abstract</summary>
  As language models (LMs) have improved, an increasingly common means of evaluating their linguistic competence is through explicit prompting (e.g., "Which sentence is more acceptable?"). Prior work indicates that such prompting underperforms compared to standard token-probability-based methods in smaller models, but improves in larger models. We test this in a new domain: semantic focus-sensitivity, responsible for contrasts like "Lucy only SWAM yesterday" vs. "Lucy only swam YESTERDAY". Testing...
  </details>

- **2026-10-29** — Zongqi Wang, Rui Wang, Yuchuan Wu et al. — [SocialArena: Evaluating Social Intelligence in Large Language Models](http://arxiv.org/abs/2610.39247v1)
  <details><summary>📄 Abstract</summary>
  We introduce SocialArena, a benchmark for systematically defining and evaluating the social intelligence of large language models (LLMs). Although LLMs are increasingly deployed in socially interactive applications such as mental health counseling, companionship chatbots, and educational tutoring, existing evaluations remain fragmented focusing on isolated capabilities or single scenarios and evaluation reliability is largely unverified. This work makes three main contributions to address these ...
  </details>

- **2026-10-29** — Minghan Yu, Mengyu Dai, Yixin Wen et al. — [From extreme weather to agricultural consequences with agentic AI](http://arxiv.org/abs/2610.40641v1)
  <details><summary>📄 Abstract</summary>
  Extreme weather is forecast days ahead, yet its consequences for agriculture remain hard to predict: a forecast says where a storm will strike, not which crops will suffer or how much is at risk, and the records that could tell span many sources. We present WxCrop, the first agent that judges agricultural hazards from physically interpretable weather indices examined by causal analysis, and the first that combines weather and agricultural information to predict crop loss reliably for past and fo...
  </details>

- **2026-10-29** — Ke Fan, Wen Wu, Haitao Su et al. — [A Pretrained Model for Bayesian Filtering in Heterogeneous Dynamical Systems](http://arxiv.org/abs/2610.40437v1)
  <details><summary>📄 Abstract</summary>
  Filtering has not yet had its foundation-model moment: state estimation is still dominated either by online Bayesian filtering algorithms that require known dy- namics as inputs, or by learning-based neural filters trained from scratch for a single system or parametric family. The core challenge is structural heterogene- ity: dynamical systems differ in their governing dynamics, physical scales, and noise levels, precluding a shared representation space for a reusable filter. To bridge this gap,...
  </details>

- **2026-10-29** — Chenchen Wang, You Zhou — [Segment Anything Model Based Context Guided Mamba Unet for Medical Image Segmentation](http://arxiv.org/abs/2610.40029v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation is crucial for clinical diagnosis and treatment planning, requiring both global contextual understanding and fine-grained structural precision. While the Segment Anything Model (SAM) demonstrates strong generalization capabilities, its direct application to medical images often lacks domain-specific adaptability. Meanwhile, State Space Models (SSMs)-based methods, such as Mamba, efficiently capture long-range dependencies but may struggle with preserving fine anatomica...
  </details>

- **2026-10-29** — Danial Dehghani, Maximilian Lübke, Zahra Seifaei et al. — [Measuring the Value of Communication in Multi-Agent Tracking Under Finite-Rate Belief Sharing](http://arxiv.org/abs/2610.40010v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the value of communica- tion (VoC) in cooperative multi-agent tracking under rate- constrained information exchange. Although prior work has studied distributed tracking, quantized communication, and robust fusion, it remains unclear at what communication rate most of the achievable tracking gain is obtained, beyond which additional communication resources yield only marginal benefit. We consider stationary agents that observe a moving target through heterogeneous range a...
  </details>

- **2026-10-29** — Yansong Bai, Yunzhi Zhuge, Xinzhuo Yu et al. — [Spectral Invariant Fusion and Refinement for Domain Generalized Semantic Segmentation](http://arxiv.org/abs/2610.39926v1)
  <details><summary>📄 Abstract</summary>
  Domain generalized semantic segmentation is challenging because it requires accurate dense prediction on unseen domains without any access to target-domain data during training. Existing methods improve transferability through data diversification, invariant learning, or direct use of foundation models, but they often struggle to simultaneously suppress domain-sensitive interference and preserve fine-grained spatial cues. In this work, we propose SIFR, a frequency-aware dual-stream framework tha...
  </details>

- **2026-10-29** — Yannis Galanos — [Euler--Lagrange Flow Monotonicity for the Radon Transform](http://arxiv.org/abs/2610.39818v1)
  <details><summary>📄 Abstract</summary>
  We present a new gradient-like flow that targets critical points of the inequality for the planar Radon transform $\mathcal{R}$ proven by Oberlin and Stein, partially answering a question of Christ, who gave a complete characterisation of the extremisers of the inequality via rearrangement methods. We show that for non-negative radial initial data near the extremiser manifold, solutions to the flow exist globally and there exists a rescaled subsequence of the flow that converges to a critical po...
  </details>

- **2026-10-29** — Hanbo Zhang, Tianrun Hu, Cedar Site Bai et al. — [Surrogate Uncertainty for Black-box Visual Grounding](http://arxiv.org/abs/2610.39798v1)
  <details><summary>📄 Abstract</summary>
  Visual grounding is crucial for robots to understand language instructions with visual observations. This paper addresses the problem of visual grounding uncertainties, where a robot uses a black-box vision-language model (VLM) to ground free-form natural-language instructions to target objects. Prevailing methods derive uncertainty from the VLM itself. Yet, outputs of the VLM, e.g., generated uncertainties, are from the same parameters and structures producing the predictions, and inherit the b...
  </details>

- **2026-10-29** — Haotian Lyu, Haoyu Wang, Ru Wang et al. — [Timbre: Reliability-aware harmonic consensus for label-free multimodal test-time rexinforcement learning](http://arxiv.org/abs/2610.39439v1)
  <details><summary>📄 Abstract</summary>
  Label-free test-time reinforcement learning adapts vision--language models using rewards derived from their own predictions. However, misinterpreted visual evidence and sensitivity to textual formulation can produce a consistent but incorrect consensus that majority voting reinforces. Cross-view aggregation can expose such errors, but image and text transformations may themselves degrade task-relevant evidence to different extents. We introduce \method, a reliability-aware harmonic consensus fra...
  </details>

- **2026-10-29** — Yuan Liang, Xiaomin Hu, Xi Chen et al. — [SD3: The First Operationally-Proven, Fully Heterogeneous-Accelerated Global Kilometer-Scale Model with Inline Physics Architecture](http://arxiv.org/abs/2610.39334v1)
  <details><summary>📄 Abstract</summary>
  We present Super Dynamics on the Cube (SD3), the first operationally-proven, fully heterogeneous-accelerated global kilometer-scale model. Through a full-stack reconstruction in native CUDA C, SD3 introduces an "Inline Physics" architecture that deeply couples its non-hydrostatic cubed-sphere dynamical core with fast physical processes. This design maintains high physical consistency, ensures energy and mass conservation, and mitigates "Grey Zone" mismatches. Five years of continuous operational...
  </details>

- **2026-10-28** — Rikuhei Umemoto, Kenjiro Ide, Soham Majumder et al. — [Does 3D Pose Improve Action Valuation in Football? An Empirical Study of Pose Representations and Learning Objectives](http://arxiv.org/abs/2610.38308v1)
  <details><summary>📄 Abstract</summary>
  Football action valuation estimates players' contributions to future scoring. Existing multi-agent deep reinforcement learning (MADRL) models use 2D positions and velocities, omitting posture information relevant to imminent actions. We investigate whether adding 3D pose to a SARSA-based model improves observed-action values relative to attack returns: goals, conceded goals or final expected possession value. Using UEFA Champions League 2022/23 event, tracking and 3D pose data, we compare six re...
  </details>

- **2026-10-28** — Davide Venuto, Leonardo Venuto — [Implicit Reasoning in Transformers: Bridging the Compositionality Gap in GPT-2-like Models](http://arxiv.org/abs/2610.39016v1)
  <details><summary>📄 Abstract</summary>
  Compositional generalization remains a persistent limitation of transformer language models: even when a model learns to combine known facts correctly in-distribution (ID), the same compositional mechanism may fail when applied to out-of-distribution (OOD) knowledge. We investigate this compositionality gap in a controlled two-hop reasoning setting using a GPT-2-like transformer model trained from scratch. Building on prior work identifying a circuit associated with compositional generalization,...
  </details>

- **2026-10-28** — Iaroslav Melekhov, Roberto Alcover Couso, Francesco Taioli et al. — [V-CAPE: Visual Consistency Assessment for Product Image Editing](http://arxiv.org/abs/2610.38611v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative image editing enable complex transformations such as background replacement, object manipulation, and pose adjustment from natural language instructions. However, verifying that these transformations preserve visual consistency, defined as the preservation of an object's intrinsic visual attributes, including geometry, texture, color, and fine-grained details, remains a largely unsolved problem. This challenge is particularly pronounced at scale, where manual inspec...
  </details>

- **2026-10-28** — Alexander Dregger, Barbarella Petz, Erik Kuhn et al. — [The Artificial Personality Model: Theory, Implementation, Measurement and Experimental Validation in Conversational Agents](http://arxiv.org/abs/2610.38608v1)
  <details><summary>📄 Abstract</summary>
  Artificial personality shapes user experience (UX) in human-machine interaction, yet coherent theoretical frameworks and validated measurement instruments remain limited. This paper refines and empirically evaluates the Artificial Personality Model (APM), a hybrid framework integrating human-centred and machine-specific personality dimensions. Across three experiments (N = 395), the model was operationalised and evaluated using the Artificial Personality Questionnaire (APQ). Factor analyses reve...
  </details>

- **2026-10-28** — Zilu Tang, Jongin Kim, Kerem Sahin et al. — [Interventional Training Reduces Causal Bypass in In-Context Introspection](http://arxiv.org/abs/2610.38911v1)
  <details><summary>📄 Abstract</summary>
  Introspection, the ability of a system to access and reason about its internal signals, is crucial for language model (LM) self-consistency and scalable interpretability. Prior work argues that LMs possess introspective capabilities, and that training (SFT) could enhance such behavior. However, most setups leave open the possibility of "causal bypass," in which the self-report relies on signals that are correlated with the self-report's subject, while being causally unrelated to it. Although hig...
  </details>

- **2026-10-28** — Klaudia-Doris Thellmann, Bernhard Stadler, Dan Saattrup Nielsen et al. — [Gold vs.~Translation: Are We Measuring Language, Knowledge, or Locality in Translated Benchmarks?](http://arxiv.org/abs/2610.38788v1)
  <details><summary>📄 Abstract</summary>
  Translated versions of English-origin benchmarks such as MMLU are widely used to evaluate large language models in non-English languages, yet it remains unclear whether they measure the same constructs as natively created benchmarks. We frame this as a proxy validity question and compare DeepL-translated MMLU proxies against six native benchmarks in seven pairings across five Nordic and Baltic languages, evaluating 29 models on each pairing. Beyond ranking agreement, we test incremental proxy va...
  </details>

- **2026-10-28** — Haotian Zhai, Tianming Sha, Junnan Li — [AtomTree: A Hierarchical Framework for State-Aware Embodied Instruction Following with LLMs](http://arxiv.org/abs/2610.38744v1)
  <details><summary>📄 Abstract</summary>
  Embodied instruction following in interactive environments requires agents to interpret natural language commands and complete long-horizon tasks. Existing planners either rely on large labeled trajectories, or use few-shot and zero-shot LLM prompting that produces a whole plan in a single serial reasoning process. These approaches depend on linguistic common sense, commit to a plan from the initial instruction, and only update after failures, which weakens robustness and state awareness. We pre...
  </details>

- **2026-10-28** — Chang Li, Xianhao Ou, Xinyan Ma et al. — [CALM: Conflict-Aware Lifecycle Memory Governance for Long-Horizon Language Agents](http://arxiv.org/abs/2610.38573v1)
  <details><summary>📄 Abstract</summary>
  A memory can be outdated for present-day reasoning yet indispensable for reconstructing the past. Relevance-based retrieval overlooks this tension: semantic relevance, evidence-grounded validity, and query-specific eligibility are distinct. We propose CALM, a conflict-aware lifecycle memory governance framework that decouples persistent memory preservation from query-time admission. CALM converts heterogeneous records into evidence-grounded memory cells, updates validity and lifecycle states usi...
  </details>

- **2026-10-28** — Juan Carlos Escanciano, Gabriele Gazzei — [Debiasing Functionals of Conditional Distributions](http://arxiv.org/abs/2610.38529v1)
  <details><summary>📄 Abstract</summary>
  Many economic parameters depend on estimated conditional distributions. We construct locally robust moments for these parameters by representing their first-step derivative and centering the representer conditionally on the covariates. We develop complementary conditional-measure and CDF linearizations, and derive corrections for control functions, counterfactual functionals, conditional rank-rank regression, and transformations of conditional $L$-functionals. Under the CDF linearization, a Ries...
  </details>

- **2026-10-28** — Janik Bürgermeister, Julius Durmann, Martin Bichler et al. — [Simultaneous Gradient Learning in First-Price Auctions](http://arxiv.org/abs/2610.38487v1)
  <details><summary>📄 Abstract</summary>
  We study equilibrium learning in discretized Bayesian games, focusing on first-price auctions as a testbed for gradient-based learning dynamics under private information. While the symmetric independent private values model admits a unique Bayesian correlated equilibrium (BCE) in the continuous limit, standard convergence guarantees for gradient-based learners do not apply: classical no-regret theory predicts convergence only to Bayesian coarse correlated equilibria (BCCE), which can remain larg...
  </details>

- **2026-10-28** — Vincent Jolivet, Lucas Terriel, Chahan Vidal-Gor{è}ne — [Automatic Iconographic Annotation of Medieval Illuminations: Comparing Generative Vision-Language Models and Supervised Discriminative Classifiers](http://arxiv.org/abs/2610.38462v1)
  <details><summary>📄 Abstract</summary>
  The large-scale digitisation of medieval manuscripts creates a growing need for automated iconographic indexing. We evaluate two complementary paradigms for this task on 9,735 full-folio images annotated with 2,333 TIMEL concepts: generative Vision-Language Models (VLM) and supervised discriminative classifiers (SDC). The VLM experiments evaluate fine-tuning, structured JSON decoding, taxonomybased candidates generation, and deterministic reranking. The discriminative experiments evaluate flat, ...
  </details>

- **2026-10-28** — Wen Jiang, Ke Jiang, Xiaoyang Tan — [Variational Consequence-Driven Offline Reinforcement Learning](http://arxiv.org/abs/2610.38238v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning (RL) typically mitigates distribution shift by imposing divergence constraints on the action distributions of the learned and behavior policies. However, this paradigm cannot ensure the underlying dynamic consistency structure: even minor action deviations can lead to drastically different transitions, inadvertently driving the agent away from the offline dataset. To address this, we explore policy constraints through their induced state-consequence distributions r...
  </details>

- **2026-10-28** — Samiran Ghosh, Shuva Gupta, Shreyo Ghosh — [L-PASSO: Adaptive Log-penalized Variable Selector, with Sparse Selection and Robustness to the Pilot Estimator](http://arxiv.org/abs/2610.38092v1)
  <details><summary>📄 Abstract</summary>
  We study L-PASSO, a penalized least-squares regression method based on the logarithmic penalty $λ\sum_j\log(1+|β_j|/τ)$, and its two-stage adaptive form, in which the scales $τ_j$ come from a pilot estimator. Although this concave penalty has been proposed previously, its variable-selection properties and sparsity relative to other popular penalties have not been fully characterized. We derive the exact orthogonal-design solution, and show that the single-stage estimator selects the true model u...
  </details>

- **2026-10-27** — Will Wesley, Philip N Brown — [Toward Understanding the Value of Anarchy: Empirical Studies on Best Response Dynamics](http://arxiv.org/abs/2610.38081v1)
  <details><summary>📄 Abstract</summary>
  We study experimental results of best response dynamics (BRD) in randomly generated weighted action networked multiagent optimization problems where agent utility is the agent's marginal contribution to the system objective. We compare those results to the Price of Anarchy (PoA) established in the literature for marginal contribution and to the expected value of randomly choosing from the available equilibria. PoA is used as a metric to describe the performance of various solutions to multiagent...
  </details>

- **2026-10-27** — Ilija Subasic, Brett Levert, Andrew Rabinovich et al. — [Prompt Lottery in LLM-as-a-Judge: Measuring and Mitigating Sensitivity to Syntactic Rephrasing](http://arxiv.org/abs/2610.38076v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-Judge has become a standard for evaluating large language models, yet most approaches implicitly assume that a single judge prompt functions as a stable evaluation instrument. Prior work has primarily explored deliberate prompt modifications such as scoring rubrics, role descriptions, or chain-of-thought reasoning in order to optimize accuracy. In contrast, we investigate whether validated prompt variants intended to preserve evaluation semantics while differing in surface realization (...
  </details>

- **2026-10-27** — Chen Tessler, Yifeng Jiang, Alec Otto et al. — [METATRON: A Promptable Whole-Body Execution Layer for Humanoids](http://arxiv.org/abs/2610.38027v1)
  <details><summary>📄 Abstract</summary>
  Humanoid controllers often require task-specific training despite sharing the need for balance and whole-body coordination. We present Metatron, a promptable whole-body execution layer combining a generative base policy with a programmable skill layer. The base policy receives partial goals, collectively called a prompt, that can combine timed body-part targets, velocity commands, and style cues. It produces diverse whole-body motions consistent with these goals. Training combines motion capture...
  </details>

- **2026-10-27** — Ali Khairallah, Arkaitz Zubiaga — [QMUL_AK at AISA-ArabicFC: Schema-Constrained Function Calling with ALLaM](http://arxiv.org/abs/2610.37995v1)
  <details><summary>📄 Abstract</summary>
  We describe the QMUL_AK submission to AISA-ArabicFC 2026. The system adapts the Arabic-English ALLaM-7B-Instruct model to function calling with low-rank adaptation (LoRA). It combines an Arabic schema-aware prompt, dialect and no-call resampling, a token-weighted training objective, and deterministic validation of generated calls against the candidate tool schema. The same output supports Track A function calling and Track B reasoning-augmented calling. Training uses only the official task data....
  </details>

- **2026-10-27** — Shenglong Yao, Zirui Liu, Xiangchi Yuan et al. — [ICALL-BENCH: Benchmarking LLM Interprocedural Reasoning in Binary Programs](http://arxiv.org/abs/2610.37871v1)
  <details><summary>📄 Abstract</summary>
  Recent benchmarks show that LLMs achieve strong performance in both function-level binary understanding and end-to-end binary reverse engineering tasks, but whether LLMs can reason over interprocedural semantics in compiled binaries remains unclear. Function-level benchmarks offer limited visibility into cross-function relationships, while whole-program benchmarks typically evaluate final outcomes of tasks that may be solvable from local clues alone, making it difficult to disentangle interproce...
  </details>

- **2026-10-27** — George Christodoulou, Vasilis Christoforidis, Alkmini Sgouritsa et al. — [Learning-Augmented Coordination Mechanisms](http://arxiv.org/abs/2610.36508v1)
  <details><summary>📄 Abstract</summary>
  The inefficiency of decentralized resource allocation is classically measured by the Price of Anarchy (PoA) and the Price of Stability (PoS). The most widely studied and foundational class of these models are atomic and non-atomic congestion games, for which a robust theory quantifying the inefficiency of equilibria is well-established. To mitigate the effects of selfish behavior, we employ Coordination Mechanisms, which modify resource costs to incentivize socially improved equilibria. However,...
  </details>

- **2026-10-27** — Pavankumar Koratikere, Abhijnan Dikshit, Leifur Leifsson — [High-Fidelity Aerostructural Dataset of Transonic Wings in Cruise Conditions](http://arxiv.org/abs/2610.36442v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in machine learning (ML) have the potential to substantially accelerate aircraft wing design, a process that has traditionally required extensive high-fidelity simulation and design iteration. Existing public datasets for ML-based wing design have focused primarily on aerodynamic performance, with limited consideration of the multidisciplinary interactions that govern practical aircraft design. In particular, efficient wing design requires simultaneous consideration of aerodynami...
  </details>

- **2026-10-27** — Bojun Zou, Wenhao Yu, Jiaohao Li et al. — [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning](http://arxiv.org/abs/2610.37378v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a straightforward solution, but collecting such data is costly, especially for dynamic scenarios, and may degrade their original task capabilities. To address these limitations, we pro...
  </details>

- **2026-10-27** — Preethi S, Meeradevi T, Arun Prakash A — [uTHCD-C: A Corruption-Robustness Benchmark for Tamil Handwritten Character Recognition](http://arxiv.org/abs/2610.36850v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of Tamil handwritten character recognition (HCR) has largely focused on clean test images, and a standardized multi-corruption robustness benchmark for isolated Tamil HCR has not been established. We introduce uTHCD-C, a corruption-robustness benchmark based on the unconstrained Tamil Handwritten Character Database (uTHCD). The benchmark defines ten corruption types, including a handwriting-specific stroke-thinning corruption, at five severity levels. We evaluate nine convolutional an...
  </details>

- **2026-10-27** — Jiameng Bai, Zhitao Wang, Long Wang et al. — [From Ripple to Boundary: Deterministic Impact Boundaries for LLM-Based Software Evolution](http://arxiv.org/abs/2610.36549v1)
  <details><summary>📄 Abstract</summary>
  The landscape of software evolution is undergoing a fundamental paradigm shift in the era of Large Language Models. As industrial software engineering increasingly transitions toward design-driven code generation, the bottleneck of evolution has shifted from writing code to maintaining deterministic consistency between multi-source design assets and the generated code. When a design asset changes, LLM agents currently lack a deterministic impact boundary to identify which code must be evolved, l...
  </details>

- **2026-10-27** — Sirui Chen, Yunzhe Qi, Haobo Xu et al. — [Proposing Better Rollouts for On-Policy Distillation](http://arxiv.org/abs/2610.36477v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) improves language-model post-training by letting the student learn from its own sampled trajectories under teacher supervision, aligning the training process with inference-time behavior. However, the rollout policy in OPD is usually treated as fixed: each round samples directly from the current student. We show that this choice can create a compounding teacher--student mismatch, because it requires the teacher to provide effective supervision on whichever trajectori...
  </details>

- **2026-10-27** — S M Abdulla Al Mamun, Akif Islam, Mohd. Ruhul Ameen — [Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance](http://arxiv.org/abs/2610.36947v1)
  <details><summary>📄 Abstract</summary>
  Can additional specialist language-model contexts improve software assurance when deterministic tool evidence is already available? We study this question through five experiments spanning authored Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-COMP assertion verdicts, and deliberately misleading evidence packages. The evaluated systems use Qwen2.5-Coder-7B-Instruct, with a 1.5B sensitivity analysis, and complete 13,638 model requests. On eight related developme...
  </details>

- **2026-10-27** — Xu Hu, Changjie Wu, Linzhe Shi et al. — [Trace-WAM: Learning to Act via 3D Motion Prediction for World Action Models](http://arxiv.org/abs/2610.36840v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) learn representations for robot control by coupling future visual prediction with action generation. Successful manipulation depends primarily on how the robot and task-relevant objects evolve, whereas future-video prediction must also reconstruct the appearance and background of the entire scene. We therefore propose Trace-WAM, which augments video-action learning with future 3D motion prediction as an auxiliary objective. This objective supervises temporal point corr...
  </details>

- **2026-10-27** — Chang Su, Bin Wu, Emine Yilmaz et al. — [What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](http://arxiv.org/abs/2610.37631v1)
  <details><summary>📄 Abstract</summary>
  Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses remains unclear. Recent point-in-time models trained on web snapshots from different years provide a way to probe how knowledge prevalence varies over time. Using these models, we propose a temporal variability score (TVS), defined as the coefficient of variation of an item's negative log-likelihood ...
  </details>

- **2026-10-27** — Simon Bultmann, Daniele Cattaneo, Abhinav Valada — [Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences](http://arxiv.org/abs/2610.37350v1)
  <details><summary>📄 Abstract</summary>
  Accurate camera-LiDAR calibration is an essential prerequisite for robust multi-modal perception in robotics. Recent target-less methods based on learned pixel-point correspondences achieve high extrinsic calibration accuracy and generalize across environments. However, they operate on rectified images with known camera intrinsics, restricting their applicability to systems whose cameras have already been individually calibrated. We present a fully automatic, target-less framework that jointly e...
  </details>

- **2026-10-27** — Wenjie Qiu, Hepei Li, Jianfeng Wang et al. — [WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](http://arxiv.org/abs/2610.37329v1)
  <details><summary>📄 Abstract</summary>
  Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limitations, leaving the question of "when to use CC" unresolved. We address this gap with WCC, a novel learning-based framework that dynamically decides when to deploy CC in LSGO. WCC employs a streamlined design for efficie...
  </details>

- **2026-10-27** — Rafael Munoz-Salinas, Francisco J. Romero-Ramirez, Manuel J. Marin-Jimenez — [TRUCO: A Scalable Lock-Free Algorithm for Parallel Contour Extraction](http://arxiv.org/abs/2610.37297v1)
  <details><summary>📄 Abstract</summary>
  Transforming binary masks into geometric contours remains a critical step in many computer vision pipelines, particularly for post-processing high-resolution segmentation outputs. Yet, standard algorithms such as the Suzuki-Abe method are limited by their sequential nature and the overhead of building topological hierarchies. As modern applications transition to high-resolution imaging, there is a critical need for contour extraction that leverages multi-core CPU architectures without the comple...
  </details>

- **2026-10-27** — Šimon Soldát, Václav Šmídl — [Bayesian Inference of Expensive Simulators: Survey and Comparison of Design Choices](http://arxiv.org/abs/2610.37284v1)
  <details><summary>📄 Abstract</summary>
  We present a survey of approaches to Bayesian inference with simulator forward models, focusing on settings with prohibitively expensive simulators. In this domain, Bayesian optimization-based methods have emerged as the most promising approach. We unify existing methods into a general framework, enabling consistent reasoning about shared algorithmic structure across the fragmented literature. Within this framework, we identify the primary design choices and perform a systematic empirical compar...
  </details>

- **2026-10-27** — Nabeelah Faumi, Deshan Sumanathilaka — [Mechanistic Failure Modes of Weight Pruning in Transformer Language Models](http://arxiv.org/abs/2610.37126v1)
  <details><summary>📄 Abstract</summary>
  Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation. We test this assumption with a factorial pruning study on GPT-2, crossing two importance criteria (magnitude, random), two component types (attention heads, MLP neurons) and three sparsity levels (3%, 50%, 70%). Using the fully characterised indirect object identification (IOI) circuit as ground truth, we measure circuit integrity wit...
  </details>

- **2026-10-27** — Sølve Langseth, Kristoffer Herland Hellton, Hugo L. Hammer — [LLM knowledge for improved Out-of-Distribution Tabular Prediction - A Cross-Validated Regularisation Approach](http://arxiv.org/abs/2610.36806v1)
  <details><summary>📄 Abstract</summary>
  Prediction models degrade when the deployment population differs from the one used to train them, and training data cannot say which feature-response relationships will transfer. Expert elicitation is slow and unscalable. We ask whether coefficient priors elicited from large language models (LLMs) improve out-of-distribution (OOD) prediction as the shrinkage target of a regularised regression instead of zero, across five tabular datasets split on real covariates, selecting providers and prior st...
  </details>

- **2026-10-27** — Jia Gu, Liang Pang, Huawei Shen — [Robust LLM Data Selection via Content-Invariant Gradient Attribution](http://arxiv.org/abs/2610.36755v1)
  <details><summary>📄 Abstract</summary>
  Gradient-based data attribution has become an important tool for high-quality data selection in the instruction fine-tuning of large language models (LLMs), as it estimates the contribution of training examples through their influence on model optimization. However, we find that existing global gradient attribution methods suffer from surface-form bias: minor changes to semantically irrelevant details, such as wording or formatting, can produce highly inconsistent attribution scores even when th...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 20 papers

- **2026-10-29** — Steven Yu, Sheng-Yu Wang, Kimia Hamidieh et al. — [Elucidating the Design Space of LM Data Attribution](http://arxiv.org/abs/2610.40655v1)
  <details><summary>📄 Abstract</summary>
  Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled Attribution Benchmark (CATT) for fact tracing, in which we fine-tune LLMs on enti...
  </details>

- **2026-10-29** — Youqing Fang, Zhouqi Hua, Yinhao Tang et al. — [Scaling Mathematical Proof Supervision from Structured Textbooks](http://arxiv.org/abs/2610.40394v1)
  <details><summary>📄 Abstract</summary>
  Mathematical supervision for language models is typically flattened into isolated problem-solution pairs, discarding the curricular organization and evidential structure of the original sources. We introduce TOME-Math (Textbook-Oriented Mathematical Evidence), a large-scale corpus that converts 2,118 textbooks spanning the core areas of university-level mathematics subjects into approximately 380K structured proof-supervision records while preserving chapter order, proposition-proof links, depen...
  </details>

- **2026-10-29** — Mohammed Nayeem Khan, K S Sarun Kumar — [Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering](http://arxiv.org/abs/2610.39468v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now do long, multi-step and multi-session software work with little supervision. When a developer comes back to that work, the useful question is not what the model said but what was actually done, by whom, and whether it is finished. We study this in three parts. First, we verify Agenttrail, an open-source local observability tool for coding agents, against its source at commit e4ba2da: nine documented constants and mechanisms hold at file-and-line level, two event pipelines ar...
  </details>

- **2026-10-29** — Helen Jenne, Davis Brown, Jesse He et al. — [Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures](http://arxiv.org/abs/2610.40382v1)
  <details><summary>📄 Abstract</summary>
  The last year has seen a shift in AI-assisted mathematics, with frontier language models producing proofs of and counterexamples to long-standing open conjectures. However, studying only the current set of major breakthroughs provides an incomplete picture of LLM capabilities and the computational resources needed to achieve reported results. To address this, we introduce a new dataset, OpenConjecture, which collects conjectures from mathematics papers published on the arXiv since February 2026....
  </details>

- **2026-10-29** — Liaoyuan Fan, Yuhao Zheng, Dongxing Mao et al. — [Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](http://arxiv.org/abs/2610.40191v1)
  <details><summary>📄 Abstract</summary>
  Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos. In parallel, video world models provide action-conditioned observations and predicted futures, serving as interactive environments for agents. We study their intersection through the agent harness: an executable runtime that constructs context, exposes tools, maintains state, routes feedback, and manages budgets around video mod...
  </details>

- **2026-10-29** —  AI Cosmos Team, Jinfeng Zhou, Yuxuan Chen et al. — [AI Cosmos: An Agentic Infra for Situated Learning](http://arxiv.org/abs/2610.40031v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can improve task performance during learning, yet these gains do not necessarily reflect learners' ability to thereafter apply the knowledge and skills independently. We present AI Cosmos, an agentic infrastructure for situated learning that organizes learning around two complementary principles: scenario-based participation and cumulative assets of practice. AI Cosmos organizes learners and role-specialized agents within learning scenarios that integrate task-releva...
  </details>

- **2026-10-29** — Madhulatha Mandarapu, Sandeep Kunkunuru — [Rebuilding a Field's Open-Problem Catalog from the Literature: A Two-Layer Knowledge Graph, and Why Status Must Stay Proposed](http://arxiv.org/abs/2610.39641v1)
  <details><summary>📄 Abstract</summary>
  A research field records its open problems in surveys, keynotes and community reports. Those are prose, written every few years, and nobody can ask them who works on a problem now or whether it was settled last year. We argue the problems should be data, and we build the system that makes them so: a hand-curated problem layer carried in unchanged, under an evidence layer rebuilt from a bibliographic index, joined by typed, provenance-carrying links in one graph database and queryable from one la...
  </details>

- **2026-10-29** — Qiaosheng Chen, Kaijia Huang, Fanqi Zhou et al. — [From Intent to Improvement: Agentic Dataset Search for Better Model Training](http://arxiv.org/abs/2610.39608v1)
  <details><summary>📄 Abstract</summary>
  Finding training data in million-scale machine learning repositories is a Web search problem where text relevance is not enough. A query couples a semantic training goal with constraints such as task, license, and training stage, and the metadata that would verify them are often missing. Text retrieval ranks dataset cards by similarity but cannot enforce hard constraints or follow the relations that reach a sparsely described dataset. Free-form tool-calling agents are more flexible, but the same...
  </details>

- **2026-10-29** — Zhifeng Gu, Ying Chen, Rui Jiang et al. — [EmbodiExp: Compositional Experience Transfer for Embodied Agents](http://arxiv.org/abs/2610.39180v1)
  <details><summary>📄 Abstract</summary>
  Experience can help embodied agents turn high-level plans into grounded actions, but transferring it across tasks remains challenging: previously effective strategies may be inapplicable to the current state or fail to produce their intended outcomes. We present EmbodiExp, a framework for constructing transferable experiences and composing them online during embodied task execution. Our key observation is that tasks often share subgoals whose completion can be assessed independently of overall t...
  </details>

- **2026-10-28** — Zhipin Wang, Koel Dutta Chowdhury, Christoph Leiter et al. — [Tracing the Influence of Retrieved Literature on Scientific Ideation in LLMs](http://arxiv.org/abs/2610.39060v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to generate research ideas from scientific literature. Existing systems combine literature retrieval with search, generation, and refinement, making it difficult to determine how the retrieval strategy itself shapes the ideas generated. We isolate this contribution by comparing five retrieval strategies and a No Literature baseline under a shared generation protocol, using 45,000 ideas across 15 machine learning topics and ten open-weight models...
  </details>

- **2026-10-27** — Chenfan Qu, Yachao Liang, Mingqi Fang et al. — [Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage](http://arxiv.org/abs/2610.37918v1)
  <details><summary>📄 Abstract</summary>
  Real-world forgery is inherently heterogeneous: it manifests not only as digital manipulation but also as physical spoofing, and is carried not only by images but also by videos. Despite substantial progress, a unified anti-forgery foundation model covering such a broad threat spectrum remains absent. In this paper, we present Venus-DefakerOne2, which substantially extends the forensic capability boundary along both the forgery-form and media-type dimensions. Trained on tens of millions of open-...
  </details>

- **2026-10-27** — Haotong Fu, Xiyue Zhang, Jack Rose et al. — [What Language Models Add to Healthcare-Equity Rankings, and What They Could Have Known](http://arxiv.org/abs/2610.38056v1)
  <details><summary>📄 Abstract</summary>
  In healthcare equities, much of what moves a single name arrives as text: filings, trial and regulatory records, news and analyst commentary. We evaluate how screened non-market features and language-model representations improve market-based equity rankings for US healthcare firms over 2020-2025. Adding balance-sheet and attention features improves the resulting hybrid's price- and liquidity-neutral rank information coefficient (IC) at one, three and twelve months. At twelve months, neutral IC ...
  </details>

- **2026-10-27** — Anouar Imel, Imad Charradi, Abderrahman Sghir et al. — [Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](http://arxiv.org/abs/2610.37624v1)
  <details><summary>📄 Abstract</summary>
  When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant...
  </details>

- **2026-10-27** — Hubert Baniecki, Przemyslaw Biecek, Martin Pawelczyk — [LinMix: Data Mixing as Linear Domain Attribution](http://arxiv.org/abs/2610.37390v1)
  <details><summary>📄 Abstract</summary>
  Language model performance depends strongly on the mixture of domains in the pretraining data corpus. Popular data mixing methods select these domain weights by training many small proxy models on random mixes and then fitting a regression model to predict performance from the mix. We recognize this practice as a domain attribution problem, where the regression measures each domain's contribution to the target metric. Through this lens, the standard Dirichlet sampling of proxy data mixes is a po...
  </details>

- **2026-10-27** — Felipe de Sant'Anna Paixão, Dhyego Tavares, Eduardo Almeida et al. — [Hidden in Plain Sight: an Empirical Study about The Instruction Stacks of Coding Agents](http://arxiv.org/abs/2610.37332v1)
  <details><summary>📄 Abstract</summary>
  Coding agents send their models more than the user's prompt: they add instructions, tool definitions, and environmental context that form an instruction stack. This stack guides execution and changes across releases, yet remains largely unexposed to users and insufficiently characterized in research. We present a longitudinal, cross-agent study of the instruction stacks captured in the first model requests of 1,886 releases of Claude Code, Codex, Gemini CLI, Qwen Code, and OpenCode. Under contro...
  </details>

- **2026-10-27** — Wadie El Amrani, Luis Galárraga — [GraphRAGProv: GraphRAG Meets How-Provenance](http://arxiv.org/abs/2610.37237v1)
  <details><summary>📄 Abstract</summary>
  GraphRAG systems often use knowledge graphs to retrieve relevant context for an LLM that produces the final answer. That makes answers more inscrutable and therefore less appealing for domains where transparency is paramount. We present GraphRAGProv, an architecture that executes SPARQL queries over source-grounded RDF graphs to compute answers and their how-provenance polynomials. These polynomials record which statement occurrences were used and how they were combined. Because each occurrence ...
  </details>

- **2026-10-27** — Iwan Williams — [Do bots feel bad? Assessing empirical evidence for functional valence in LLMs](http://arxiv.org/abs/2610.36962v1)
  <details><summary>📄 Abstract</summary>
  Do LLMs have valenced states, i.e. states that feel pleasant or unpleasant? Recent empirical work has claimed to show that LLMs possess functional valenced states (e.g. ``functional pleasure and pain'' [Ren et al. 2026], ``functional emotions'' [Sofroniew et al. 2026], and ``functional welfare'' [Han et al. 2026]) that play the same causal role as valenced states in cognition and action, without necessarily being consciously experienced. But it remains unexplored how well the identified states f...
  </details>

- **2026-10-27** — Saifullah Saifullah, David Dembinsky, Stefan Agne et al. — [DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding](http://arxiv.org/abs/2610.36929v1)
  <details><summary>📄 Abstract</summary>
  Multimodal transformer models have driven unprecedented performance breakthroughs in modern document understanding. However, the inherent black-box nature of these models remains a major obstacle to their safe deployment in high-stakes sectors. Despite significant progress in explainability for vision and language tasks, explainable AI (XAI) research tailored to multimodal document understanding has received little attention. To address this gap, we present \ourframework{}, the first comprehensi...
  </details>

- **2026-10-27** — Jipeng Li, Pramod Khargonekar, Yanning Shen — [Causal Localization of Evidence Effects in Transformers](http://arxiv.org/abs/2610.36524v1)
  <details><summary>📄 Abstract</summary>
  Can controlled symbolic inputs reveal attention heads that influence a language model's decisions from natural language evidence? We introduce controlled evidence aggregation (CEA), which varies the counts and order of two symbols in otherwise fixed prompts and measures changes in a frozen Transformer's preference between two answer tokens. The preference is measured by their logit difference; the prompts prescribe no correct answer. Balanced utility causal selection (BUC) identifies compact hea...
  </details>

- **2026-10-27** — Jia Chen, Chao Huang, Xinrong Hu et al. — [GarmentSegAgent: Autonomous Garment Segmentation for Web Fashion Images via Textual Self-Refinement](http://arxiv.org/abs/2610.36506v1)
  <details><summary>📄 Abstract</summary>
  Web fashion images support applications such as visual product search and consumer-to-shop matching, yet their visual heterogeneity makes reliable garment segmentation challenging. Despite advances in promptable segmentation, autonomously identifying and correcting garment-specific errors without human-provided spatial prompts remains difficult. We propose GarmentSegAgent, an autonomous framework that integrates semantic planning, spatial execution, and visual evaluation through iterative textua...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-29** — Juan Belieni, Ana Carolina Erthal, Eliezer de Souza da Silva et al. — [Preserving Utility in Continual LLM Unlearning via Orthogonal Projections](http://arxiv.org/abs/2610.40483v1)
  <details><summary>📄 Abstract</summary>
  Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. While unlearning requests happen continuously during a model's lifetime, the vast majority of LLM unlearning methods are ill-suited for iterated removal, yielding steep decay in forgetting and utility upon sequential unlearning. This decay stems from interference between successive updates, as each new...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-10-28** — Prashank Kadam — [Beyond Passing Tests: A Systematic Review and Controlled Re-evaluation of Techniques for Improving the Quality of LLM-Generated Code](http://arxiv.org/abs/2610.38977v1)
  <details><summary>📄 Abstract</summary>
  Large language models pass most functional-correctness benchmarks, but passing tests says little about whether their code is readable, efficient or secure. Many techniques claim to improve these qualities, yet their evidence is scattered, usually covers one quality dimension and is rarely compared at an equal compute budget. We contribute a systematic review and a controlled re-evaluation. A systematic literature review of 628 primary studies (July 2021 to October 2026), with disclosed, author-r...
  </details>

- **2026-10-27** — Kostiantyn Khabarlak — [Multibranch Ensemble Head in Vision Foundation Models for Efficient Cucumber Phenological Stage Classification](http://arxiv.org/abs/2610.37118v1)
  <details><summary>📄 Abstract</summary>
  Vision Foundation Models (VFMs) pretrained with self-supervised learning, such as DINOv2, provide highly transferable features, yet adapting them to small, domain-shifted datasets is still challenging. We propose a regularizing multibranch ensemble head: a training and inference scheme that pairs low- and high-capacity branches, samples a single branch stochastically at each training step, and averages both branches in probability space at inference. The design adds negligible parameters and ess...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-10-29** — Biprateep Dey, Joshua S. Speagle — [Tabular Foundation Models Dramatically Outperform Bespoke Photometric Redshift Estimators](http://arxiv.org/abs/2610.39332v1)
  <details><summary>📄 Abstract</summary>
  Estimating galaxy redshifts (a proxy for distance) from imaging data alone, also known as photometric redshifts (photo-$z$'s), is essential for studies of extragalactic astrophysics and cosmology. However, data-driven estimators rely on spectroscopic training datasets, which are scarce and systematically biased toward bright and easily observed galaxies. In this work, we show that tabular foundation models (TFMs), whose synthetic pretraining amounts to a learned prior over regression problems, c...
  </details>

- **2026-10-28** — Kshitish Ghate, Michael Saxon, Tadayoshi Kohno et al. — [RoleFUZZER: User-Behaviour Fuzzing for Role-Specification Adherence in Large Language Models](http://arxiv.org/abs/2610.38438v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are often conditioned into specific roles such as tutors, interviewers, or agents acting for an organisation, through system prompts that specify how they should behave. The extent to which they can actually adhere to these role specifications under multi-turn interactions with realistic and potentially problematic users is understudied. To address this, we propose user behaviour fuzzing, a guided search over plausible user behaviours that can lead a model to violate...
  </details>

- **2026-10-28** — Huangfei Jiang, Anning Hu, Kai Sheng et al. — [Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](http://arxiv.org/abs/2610.38342v1)
  <details><summary>📄 Abstract</summary>
  Financial agents must form forecasts and investment judgments from decision-time evidence, with predictions evaluated against subsequent outcomes. Existing benchmarks assess financial knowledge, research workflows, or forecasting, but evaluating the full research process requires a strictly frozen information set and professional evaluation criteria. We introduce Investor's Last Exam (ILE), an equity-research benchmark led by experienced buy-side investors and fund managers. Its three components...
  </details>

- **2026-10-28** — Vishnudatta Thota, Tyler Paine, Anastasia Bizyaeva — [Tunable Spatial Task Allocation with Application to Maritime Swarms](http://arxiv.org/abs/2610.39018v1)
  <details><summary>📄 Abstract</summary>
  In this chapter, we explore how a team of autonomous agents can flexibly reconfigure the distribution of its members across many spatially embedded tasks using a task allocation strategy grounded in a generalization of the recently proposed Nonlinear Opinion Dynamics model. Motivated by an adaptive maritime survey application, we couple opinion dynamics directly to spatial movement and examine how the emergent macroscopic allocation is shaped by the interplay between environmental geometry, natu...
  </details>

- **2026-10-27** — Cullan Howlett, L. Giani, Elizabeth G. O'Brien et al. — [The scale of homogeneity in DESI Data Release 1](http://arxiv.org/abs/2610.38083v1)
  <details><summary>📄 Abstract</summary>
  We present measurements of the scale of cosmic homogeneity using the first data release (DR1) of the Dark Energy Spectroscopic Instrument (DESI), the largest publicly available spectroscopic extragalactic survey to date. Using a counts-in-spheres estimator applied to nearly 5 million galaxies and quasars across six independent redshift bins spanning $0.1 < z < 2.1$, we measure the correlation dimension $D_2(r)$ and define the homogeneity scale $R_H$ as the point at which the galaxy distribution ...
  </details>

- **2026-10-27** — Pranjal Aggarwal, Sean Welleck — [Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents](http://arxiv.org/abs/2610.37567v1)
  <details><summary>📄 Abstract</summary>
  AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand real-time interaction, such as playing a video game or operating a physical device. In these settings, the environment state may evolve as the agent is reasoning, or even as the underlying model is performing a forward pa...
  </details>

- **2026-10-27** — Lucas Bayones, Devika Narain, Roman Rossi-Pool — [The geometry of cognition: from neural populations to neurotechnology](http://arxiv.org/abs/2610.36541v1)
  <details><summary>📄 Abstract</summary>
  Cognition is implemented by distributed neural populations whose collective activity evolves through structured, low-dimensional state spaces. In this review, we survey the analytical and conceptual tools used to study latent population dynamics in biological neural networks. We begin with single-unit coding, which remains essential for interpreting neuronal selectivity, and then review population-level approaches, including population vectors, cosine similarity, principal component analysis and...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 175 papers

- **2026-10-29** — Pranjal Aggarwal, Sean Welleck — [Gym-Anything for Robotics: Scaling physical simulations with digital agents](http://arxiv.org/abs/2610.40565v1)
  <details><summary>📄 Abstract</summary>
  Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefore does not scale. To address this, we introduce Gym-Anything for Robotics, a framework in which coding agents create realistic robotics simul...
  </details>

- **2026-10-29** — Samuel Schmidgall, Tim Strother, Alex Bijamov et al. — [Training language models in simulation for psychiatric intake](http://arxiv.org/abs/2610.40476v1)
  <details><summary>📄 Abstract</summary>
  In psychiatric practice, the clinical intake interview remains a primary diagnostic instrument, requiring the clinician to establish rapport while disentangling complex, overlapping presentations. Here, we show that multi-turn reinforcement learning (RL) in simulation environments improves language model performance on structured text-based psychiatric intake, spanning history-taking, differential diagnosis, and initial management planning. In a randomized, double-blind crossover study ($N = 60$...
  </details>

- **2026-10-29** — Abdelkader Metales, Miriam Grabenheinrich — [Surprise Alone Learns Lies: Evidence-Gated Continual Learning for LLMs from Streaming Claims](http://arxiv.org/abs/2610.39840v1)
  <details><summary>📄 Abstract</summary>
  Continual learning methods for large language models increasingly decide what to learn by surprise, keeping the inputs the model finds least predictable. This rule is unsafe when the stream contains lies. A planted falsehood about something the model knows has low probability under the model's belief, so it is highly surprising by construction, and a surprise-driven learner absorbs nearly every such lie, at a rate similar to random selection with the same budget. We study the problem with LoRA-a...
  </details>

- **2026-10-29** — Xiaoou Li, Shan You, Tao Huang — [ROAD: Modern Adversarial Training for Simple One-Step Distillation at Scale](http://arxiv.org/abs/2610.39539v1)
  <details><summary>📄 Abstract</summary>
  One-step distillation turns pretrained diffusion models into fast generators, but strong results often require substantial training machinery and compute. Pure adversarial distillation offers a simpler route, yet has struggled at modern text-to-image scale. To address this limitation, we propose ROAD (Representation-grounded One-step Adversarial Distillation), a one-stage framework that distills text-to-image models with one adversarial objective and a lightweight representation-space critic. Fi...
  </details>

- **2026-10-29** — Bravish Ghosh — [PCM: A Proof-Carrying Message Protocol for Verifiable Multi-Agent Communication](http://arxiv.org/abs/2610.39109v1)
  <details><summary>📄 Abstract</summary>
  When one AI agent tells another that "the tests passed" or "a person approved this refund", the receiver has only the sender's word. A2A and MCP authenticate the channel, but the sender is the party in doubt, so a prompt-injected agent can launder fabricated facts and authority through a multi-agent system. We present Proof-Carrying Messages (PCM), a protocol in which each claim carries evidence: records from an append-only Merkle log that the agent cannot write, with inclusion proofs, signed by...
  </details>

- **2026-10-29** — Di Wu, Ling Liang, Haizhao Yang — [FARMS: A Verifiable Foundation for Automated Computational Science](http://arxiv.org/abs/2610.40560v1)
  <details><summary>📄 Abstract</summary>
  Automated computational science could accelerate discovery by selecting, adapting and developing numerical methods. This prospect requires mathematical knowledge that AI systems can interpret and reuse with explicit guarantees. Here we present FARMS, a faithful and efficient foundation that transforms computational mathematics into AI-ready computing knowledge. FARMS connects formal statements to source context, algorithmic meaning and quantitative guarantees through source preparation, reusable...
  </details>

- **2026-10-29** — Jingru Fan, Tianle Zhou, Yunjie Zhou et al. — [Agentic University: Collaborative Agents for Personalized Learning](http://arxiv.org/abs/2610.40492v1)
  <details><summary>📄 Abstract</summary>
  Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learning process that evolves with the learner. A central challenge is to align goals, activities, and assessment while using learning evidence to decide what should follow. We introduce Human-Participatory Multi-Agent Organization and instantiate it in Agentic University (AU). In AU, learners participat...
  </details>

- **2026-10-29** — Haozhe Zhang, Gu Zhang, Zirui Zou et al. — [TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation](http://arxiv.org/abs/2610.40349v1)
  <details><summary>📄 Abstract</summary>
  Human demonstrations offer an efficient and scalable source of data for dexterous robot manipulation, but differences in sensing and hand morphology complicate the transfer of contact-rich interactions. We present TouchBridge, a hardware--software co-designed framework for human-to-robot data transformation. A wearable human demonstration interface and a corresponding robot interface establish cross-embodiment correspondence in visual and fingertip tactile sensing. We introduce Tac-Retarget, a t...
  </details>

- **2026-10-29** — Yishuo Yuan, Shaoyu Yang, Chunrong Fang — [DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving](http://arxiv.org/abs/2610.40292v1)
  <details><summary>📄 Abstract</summary>
  Prefill-decode (PD) disaggregation isolates the two phases of large language model serving, but request-level path selection must account for prefill work, cache reuse, and decode demand. We present DolphinRouting, which learns this choice from end-to-end SLO feedback under a given P/D resource allocation. Requests are clustered by raw prompt length, cache-adjusted input lengths on both worker pools, and output-length information. Offline policy search learns one binary action per cluster. Onlin...
  </details>

- **2026-10-29** — Chutong Meng, Alec J. Bateman, Antonios Anastasopoulos — [Mobilizing the Archive: Bitext Extraction at Scale from Archival Documents for Extremely Low-resource Languages](http://arxiv.org/abs/2610.40233v1)
  <details><summary>📄 Abstract</summary>
  While mining parallel sentences from web pages has proven effective for low-resource machine translation, the majority of the world's languages have little to no web presence. What they do have, though, are resources that are the result of centuries of efforts by linguists, such as grammars, dictionaries, and other documentation materials. We propose extracting translation examples from such linguistic resources, which offer parallel data for languages under-represented online and could potentia...
  </details>

- **2026-10-29** — Minyan Luo, Yuxin Zhang, Meng Zhao et al. — [AdMuse: Skill-Guided Creative Advertising Image Generation](http://arxiv.org/abs/2610.40190v1)
  <details><summary>📄 Abstract</summary>
  An outstanding creative advertising image should both attract attention and communicate a product's positioning. How to choose a persuasive conceptual bridge before rendering begins is challenging for advertising generation. We present AdMuse, a skill-guided multi-agent framework that distills high-quality advertisements into reusable creative skills for cross-domain advertising strategy. Rather than retrieving isolated exemplars, AdMuse abstracts recurring bridge patterns into a skill library t...
  </details>

- **2026-10-29** — Jianming Ma, Rongjun Jin, Yizhi Chen et al. — [Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles](http://arxiv.org/abs/2610.40075v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models increasingly rely on flow-based action generation for general-purpose manipulation, yet the generated actions are not guaranteed to satisfy physical constraints such as joint limits and collision avoidance. This problem is especially challenging when the feasible set cannot be described analytically and is accessible only through black-box feasibility oracles. We study this practical oracle-only setting and propose an oracle-guided differentiable safeguard for safe flow-m...
  </details>

- **2026-10-29** — Bi'an Du, Fanpeng Meng, Jiemin Fang et al. — [PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets](http://arxiv.org/abs/2610.39924v1)
  <details><summary>📄 Abstract</summary>
  Generating interactive 3D assets from a single image requires realistic appearance, fidelity to the depicted object, and plausible physical behavior. Yet detailed geometry alone does not determine how an object should move or deform. We introduce PhysAg3D, which couples 3D generative models with agentic reasoning and tool use. A vision-language agent first infers semantic parts, candidate interactions, and physical priors from the image; a 3D generator then produces a textured whole-object mesh ...
  </details>

- **2026-10-29** — Yijie Hao, Joyce C. Ho — [The Role of Self-Concept In Language Models](http://arxiv.org/abs/2610.39795v1)
  <details><summary>📄 Abstract</summary>
  When a language model says "I," does it refer to its parameter weights, its currently running process, its stable preferences, its model lineage, or the goals it pursues? Different choices can assign opposite meanings to the same event: deleting a checkpoint may be destruction, continuation, or no loss at all, depending on the referent "I". We install five such self-conceptions into five open-weight base models via supervised fine-tuning on purely declarative statements, containing no preference...
  </details>

- **2026-10-29** — Yuze Li, Fuchen Long, Xinlong Sun et al. — [Regional Anchor Routing for Multi-Object Motion Transfer](http://arxiv.org/abs/2610.39478v1)
  <details><summary>📄 Abstract</summary>
  Compositional motion transfer requires a model to extract motions from multiple reference videos, and apply each motion to a user-specified object in one target scene. Existing methods normally struggle to reliably assign different reference motions to the correct target objects, thus a motion intended for one object may affect another. Meanwhile, some motion-specific tuning approaches are still facing another issue: they must run a new optimization whenever the reference video changes, making r...
  </details>

- **2026-10-29** — Jae Hun Hwang, Hong-In Won — [Retaining Repair Hypotheses for Cost-Aware Execution](http://arxiv.org/abs/2610.39410v1)
  <details><summary>📄 Abstract</summary>
  Several corrections of an executable model can fit the same observations while predicting different execution outcomes. We study a repair-to-execution interface that retains compatible finite guard repairs, conditions their weights on diagnostic and ordinary-execution observations, and uses their predictions to choose routes, priced tests, or a backup. On 24 synthetic two-stage devices, an equal mixture of a language-model-generated repair and a uniform belief over compatible repairs (the AI-wei...
  </details>

- **2026-10-29** — Yuhao Lu, Jiongxu Chen, Hexiang Wei et al. — [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](http://arxiv.org/abs/2610.39278v1)
  <details><summary>📄 Abstract</summary>
  Predicting future physical states stands as a central challenge in embodied intelligence. Existing video world models leave 3D dynamics implicit, action-based formulations remain tied to specific robot configurations, and 3D motion prediction models use flow-only supervision, providing a limited learning signal for physical dynamics. To circumvent these limitations, we introduce \method{}, a generative world model that jointly predicts future video and query-based 3D trajectories. By parameteriz...
  </details>

- **2026-10-29** — Phu-Anh-Tai Do, Huu-Hoang Nguyen, Duc-Hoang Nguyen et al. — [A learning-based method of automatic music transcription](http://arxiv.org/abs/2610.39255v1)
  <details><summary>📄 Abstract</summary>
  Automatic Music Transcription (AMT) seeks to convert acoustic music recordings into symbolic musical notation, a process that remains remarkably difficult for polyphonic piano due to concurrent polyphony, harmonic partial interference, expressive timing, and severe pitch activation sparsity. In this paper, we formulate polyphonic piano transcription as a frame-level multi-label classification problem across the standard 88 piano pitches (MIDI notes 21 to 108). Raw audio waveforms are processed u...
  </details>

- **2026-10-29** — Haitang Feng, Zhuoman Liu, Zhennan Wang et al. — [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](http://arxiv.org/abs/2610.39232v1)
  <details><summary>📄 Abstract</summary>
  Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world. We present GenSight, a unified embodied world model that brings future video generation and dense perception into a single pretrained video diffusion transformer. GenSight uses a unified spatiotemporal representation for video, depth, embodiment segmentation, and first-frame-relative 2D flow. Built on a shared DiT backbone, GenSight uses lightwei...
  </details>

- **2026-10-29** — Yuanbo Lyu, Changjian Pan, Saining Zhang et al. — [RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories](http://arxiv.org/abs/2610.40333v1)
  <details><summary>📄 Abstract</summary>
  High-quality articulated assets are essential for embodied perception, simulation, and manipulation, yet constructing them at scale remains difficult. Manual annotation and procedural modeling require substantial human effort. Recent agentic systems automate asset construction through program synthesis, but repeat costly reasoning and refinement for every new asset. Our key observation is that assets within a category can share construction logic despite variations in structure and appearance. A...
  </details>

- **2026-10-29** — Peng Xie, Amr Alanwar — [Judged in Company: In-Context Batching Makes LLM Verdicts Depend on Other Items](http://arxiv.org/abs/2610.40241v1)
  <details><summary>📄 Abstract</summary>
  To save cost, practitioners often ask a language model to grade many independent items in one prompt. This assumes that verdicts are separable: that the verdict on an item does not depend on the other items in the prompt or on its position among them. Across three judgement tasks (harm in social-media comments, short-answer grading and review star ratings) and five open-weight models with 4-9B parameters, assigning the same 2,000 items to different random batches of 25 changes 11-22% of decision...
  </details>

- **2026-10-29** — Govind Velamoor, Adrian Lin, Sam Jung et al. — [UMI-Live for In-The-Wild Bimanual Robotics Data Collection](http://arxiv.org/abs/2610.39385v1)
  <details><summary>📄 Abstract</summary>
  Universal Manipulation Interface (UMI) devices allow human experts to demonstrate tasks for robot learning without teleoperating physical robots. Using these demonstrations as training data still requires a consistent hardware setup, calibration, and data processing. We present UMI-Live, a full-stack open-source bimanual UMI system for in-the-wild data collection. We design our custom UMI-Live hardware to integrate camera and LiDAR--inertial sensing, onboard compute, and power, without external ...
  </details>

- **2026-10-29** — Yehan Zhang, Qianqi Yan, Hang Yin et al. — [AgentDecept: Benchmarking Deceptive Behavior in Tool-Using LLM Agents under Pressure](http://arxiv.org/abs/2610.39377v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly carry out multi-turn tasks across everyday applications, yet users often see only the agent's report rather than the observations, API calls, and state changes behind it. Existing deception benchmarks have studied long-horizon interactions and tool-use settings, but whether agents faithfully report their actions across realistic, stateful application workflows remains underexplored. To address this gap, we introduce AgentDecept, an executable benchmark for evaluating beha...
  </details>

- **2026-10-29** — Chongxi Meng, Da Zhao, Yanmin Zhou et al. — [CuBot-STT: Simultaneously Transport and Tighten for Lattice-type Modular Reconfiguration Robot](http://arxiv.org/abs/2610.39279v1)
  <details><summary>📄 Abstract</summary>
  Lattice-type modular reconfigurable robots rearrange standardized modules across tasks. Dedicated transport robots reduce module weight and cost by eliminating module level reconfiguration actuators. But existing systems use low capacity connections or internal fastening robots that occupy space for functional components. This paper presents CuBot-STT, which integrates module transport, interface locking, and release in one external robot. Cubic modules provide structural support and $24\,\mathr...
  </details>

- **2026-10-29** — Nicolas Dufour, Elouan Gardès, Amil Dravid et al. — [Rethinking Neural Thickets Without Weight Perturbations](http://arxiv.org/abs/2610.40649v1)
  <details><summary>📄 Abstract</summary>
  The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most re...
  </details>

- **2026-10-29** — Yifu Luo, Chuang Ma, Zeyu Chen et al. — [Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation](http://arxiv.org/abs/2610.40574v1)
  <details><summary>📄 Abstract</summary>
  On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing approaches keep the teacher fixed either throughout training by consistently exposing it to the full reference, or within each response by adaptively varying partial reference exposure only across responses. In this paper, we argue that neither of them is sufficient. Instead, every token needs its own teacher, as the tea...
  </details>

- **2026-10-29** — Qiaoyu Zheng, Weike Zhao, Yanjie Fan et al. — [Advancing Clinical Genomic Analysis with a Skill-Centred Agent](http://arxiv.org/abs/2610.40556v1)
  <details><summary>📄 Abstract</summary>
  Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a major bottleneck to the timely use of genomic information in clinical decision-making. To fill this gap, we developed ClinGeX, a large-language-model agent that composes 105 curated executable skills through task-specific retrieval and dependency-aware orchestration. On 223 tempo...
  </details>

- **2026-10-29** — Pedro Carvalho Brom — [Homebrewed SLMs: Autoregressive and Masked Diffusion Language Models Built at Home for Portuguese](http://arxiv.org/abs/2610.40533v1)
  <details><summary>📄 Abstract</summary>
  Building a language model of one's own no longer requires a data centre. This tutorial trains one from scratch, tokenizer included, on one consumer GPU, and shows how to tell whether it is good for the tasks of a specialist domain. It proposes no new method. It releases a tested Python package and two notebooks in Brazilian Portuguese with autoregressive and masked diffusion generation on one network, a preregistered comparison protocol, legal tasks built from text alone with a Kneser-Ney floor ...
  </details>

- **2026-10-29** — Guancheng Pan, Qixin Tan, Yang Yuan et al. — [Algebraic World Model: From Exploration to Proofs](http://arxiv.org/abs/2610.40503v1)
  <details><summary>📄 Abstract</summary>
  AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications. This raises a natural question: can it reason rigorously about an unknown world? We introduce the Algebraic World Model (AWM), a framework that turns interaction with unfamiliar environments into explicit mathematical models supporting formal reasoning. AWM explores the environment and develops ...
  </details>

- **2026-10-29** — Matteo Fadel, Giulia Gubitosi — [Trajectory sharpening under quantum reference frame transformations](http://arxiv.org/abs/2610.40452v1)
  <details><summary>📄 Abstract</summary>
  Quantum reference frame (QRF) transformations relate the description of a physical system to different quantum observers, but their connection to concrete experimental phenomena remains largely unclear. Here we show that the trajectory-sharpening effect obtained by correlating a probed system with an effective negative-mass reference admits a natural interpretation as a QRF transformation to the frame of a negative-mass system. Using a minimal toy model of free particles with signed masses, we i...
  </details>

- **2026-10-29** — Chenjie Qiu, Zixuan Zeng, Shaobin Shi et al. — [Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation](http://arxiv.org/abs/2610.40409v1)
  <details><summary>📄 Abstract</summary>
  Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passages retrieved so far, and we find that they are already strong: trained only on gold histories, a small chain embedding retriever that calls no language model outperforms graph-based systems and is competitive with a searc...
  </details>

- **2026-10-29** — Xinhe Zhang, Arnau Marin-Llobet — [Factorized Representations of Concurrent Temporal Variables in Pretrained Language Models](http://arxiv.org/abs/2610.40328v1)
  <details><summary>📄 Abstract</summary>
  Language models often need to maintain multiple contextual variables that evolve independently within a document. Prior work has identified structured representations of individual temporal or contextual quantities, but their joint organization remains less understood. We study this question using controlled documents with independently phased language-switch and topic-change timers. Across ten pretrained checkpoints, both timers are linearly decodable from the same hidden states. Removing a tim...
  </details>

- **2026-10-29** — Xuanfa Jin, Xinyu Cui, Zhijian Ma et al. — [EpiAgent: Epistemic Self-Play for LLM Agents](http://arxiv.org/abs/2610.40227v1)
  <details><summary>📄 Abstract</summary>
  Epistemic game theory explains an agent's strategic behavior via the beliefs it holds about others and how these beliefs are updated as the interactions unfold. Modern LLM-based agents, however, often lack an explicit mechanism for learning and updating such beliefs to guide decisions under incomplete information. To bridge this gap, we propose EpiAgent, a framework that equips LLM-based agents with an explicit, learnable epistemic layer, which maintains beliefs over others' private information ...
  </details>

- **2026-10-29** — Shuwei Yue, Kaida Xiao, Zhihua Wang et al. — [Benchmarking color judgment in multimodal LLMs with CIE-computable ground truth](http://arxiv.org/abs/2610.40212v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) are now used as zero-shot judges of image quality, but their color judgments are rarely tested with colorimetric ground truth. We present a five-task benchmark based on the CIE colorimetric framework: AWB pair judgment, skin-tone bias direction, CCT estimation, CIE Delta E 2000 pair ordering, and color naming under changing illuminants. We test eight MLLM endpoints, including four Qwen3-VL variants, GLM-4.5V, GPT-5.4, Claude-Opus-4.7, and Gemini-3.1-Pro. ...
  </details>

- **2026-10-29** — Ivana Beňová, Michal Gregor, Marián Šimko — [It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test](http://arxiv.org/abs/2610.40124v1)
  <details><summary>📄 Abstract</summary>
  Vision--language models (VLMs) are tested for fine-grained understanding with image--text matching probes, a model must prefer the correct image or caption over handcrafted negative. In retrieval, the correct item must beat thousands of alternatives. We measure how these two evaluation methods relate by using two probing benchmarks, \svo{} and SugarCrepe, for retrieval tasks. For 100 image and caption queries we judge the top-10 retrievals from full dataset of six VLMs, with human annotators and...
  </details>

- **2026-10-29** — Benjamin A. Jasperson, Logan Dehay, Rahul Gulati et al. — [The coupled spread of information and potential-driven motion in evacuating agent populations](http://arxiv.org/abs/2610.40081v1)
  <details><summary>📄 Abstract</summary>
  Whether a population evacuates safely depends on two coupled processes: how a warning spreads through it, and how that information moves people. We model this coupling with an agent-based framework, in which each agent's information state--susceptible, exposed, informed or reverted--gates its motion. Only informed agents respond to a global background potential encoding hazards and safe zones, while all agents interact locally through a Lennard-Jones potential. The total potential experienced by...
  </details>

- **2026-10-29** — Illia Makarov — [One Vector or Many? Clustered Optimal-Transport Steering under Quantization](http://arxiv.org/abs/2610.40055v1)
  <details><summary>📄 Abstract</summary>
  Activation steering changes what a language model generates by editing its hidden states at inference time. Its most common form adds one vector, the difference of class means (DiM), to every hidden state. CHaRS (concept heterogeneity-aware representation steering) uses optimal transport instead: an entropic plan pairs the clusters of the two classes, and each hidden state moves along a mixture of the cluster displacements, weighted toward its nearest clusters. We study this family of clustered ...
  </details>

- **2026-10-29** — Peter Dolog, Kim G. Larsen, Marius Mikučionis et al. — [UPPAAi: Towards LLM-Assisted Modeling, Verification, Analysis and Synthesis](http://arxiv.org/abs/2610.40042v1)
  <details><summary>📄 Abstract</summary>
  For more than three decades, UPPAAL has supported the modelling and analysis of real-time and cyber-physical systems. Yet building a suitable model, formalising the intended properties, choosing analysis techniques and interpreting counterexamples remain iterative tasks that demand substantial expertise. Large language models (LLMs) can offer plausible explanations and even solutions, but they are not necessarily correct. We present UPPAAI, an extension of UPPAAL in which users construct, explai...
  </details>

- **2026-10-29** — Julian Andres Hernandez-Potes, Tomás Arias-Vergara, Daiqi Liu et al. — [Blind Video Denoising for Vocal Tract rtMRI using a Self-Supervised Ensemble](http://arxiv.org/abs/2610.39972v1)
  <details><summary>📄 Abstract</summary>
  Real-time magnetic resonance imaging of the vocal tract makes speech articulation directly observable, but the trade-off between temporal resolution and signal quality introduces substantial noise and obscures fine articulatory detail. Since clean references cannot be acquired for a moving vocal tract, supervised denoising approaches are not applicable in this setting. We propose a self-supervised denoising framework that combines spatiotemporal super-resolution learning with pseudo-supervision ...
  </details>

- **2026-10-29** — Volker Kempe — [AI at a Turning Point: From ChatGPT through Neural Networks to Neuromorphic AI](http://arxiv.org/abs/2610.39796v1)
  <details><summary>📄 Abstract</summary>
  The tension between the established technologies of connectionist AI and their neuromorphic challengers is attracting growing attention, above all because of the enormous energy demand of the former and the low power consumption of the latter. Developing and running large AI models consumes gigawatt- to terawatt-hours of energy, while the human brain operates on a continuous 20 watts. Spiking neural networks (SNNs) counter this energy demand with a frugal approach and bring elements of self-orga...
  </details>

- **2026-10-29** — Yeb Havinga — [When the Top Answer Decides: Gender Bias in Decision Models](http://arxiv.org/abs/2610.39747v1)
  <details><summary>📄 Abstract</summary>
  Decision models are language models built to route, classify and triage: they return option probabilities from one forward pass, and an application acts on the top answer. They are offered off the shelf, trained for the decision format rather than for fairness or any one application, and we found no bias measurement in their cards. We test TypeSafe's closed Jev and five open decision models on gender-swapped yes/no decisions about people (Tamkin et al., 2023), BBQ, StereoSet and the gender-bias ...
  </details>

- **2026-10-29** — Marco Giunti, Fabrizia Giulia Garavaglia — [From the Transformer to a Formal Semantics of Coordinated Transformations](http://arxiv.org/abs/2610.39735v1)
  <details><summary>📄 Abstract</summary>
  We develop a formal semantics for a general class of coordinated systems of parameterized transformations, taking the Transformer as a paradigmatic starting point but abstracting from its particular mathematical instantiation. Representational vectors receive both extensional reference and ordered intensional interpretations, while parameter structures acquire relative, second-level interpretations that determine how argument properties are preserved, replaced, or combined. This yields the notio...
  </details>

- **2026-10-29** — Andreas Chatziafratis, Spyridon Kamvissis, Alain Miranville et al. — [Unified transform method for nonautonomous linear evolution equations: rigorous analysis and qualitative theory](http://arxiv.org/abs/2610.39698v1)
  <details><summary>📄 Abstract</summary>
  Established herein is the rigorous extension of the celebrated Fokas unified transform method for linear evolution PDE with time-dependent coefficients. As illustrative examples, considered below and rigorously analysed in detail are non-homogeneous initial-boundary-value problems, formulated on the half-line, for the heat equation and the modified heat (also widely known as Barenblatt's pseudo-parabolic) equation with reaction terms and temporally varying coefficients. Solution formulae are der...
  </details>

- **2026-10-29** — Jeheon Woo — [Transformer-inspired architectures make machine-learned electron densities accurate and transferable enough to bypass self-consistency](http://arxiv.org/abs/2610.39687v1)
  <details><summary>📄 Abstract</summary>
  We introduce machine learning models that accurately predict the electron density, the central variable of density functional theory. They are built on Transformer-inspired architectures, which require little computation per parameter and can therefore be enlarged at low cost. The proposed models, SwinUNETR-V2 and its attention-free counterpart NeXtUNETR, achieve state-of-the-art accuracy on QM9, with normalized mean absolute errors in the density averaging 0.075% and 0.046%, respectively. The p...
  </details>

- **2026-10-29** — Angelica Lo Duca — [Towards Audience-Driven Real-Time Data Storytelling](http://arxiv.org/abs/2610.39658v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces the concept of Audience-Driven Real-Time Data Storytelling (ADRDS), a framework that utilizes participatory and social sensing to enable audiences to actively shape the presentation of data stories. At its core, ADRDS employs a pre-authored decision tree, where the presenter defines the data story through a branching three-act arc (setup, conflict, and resolution). Each node contains a question, branching rules, thresholds for coverage, consensus, and confidence intervals, ...
  </details>

- **2026-10-29** — Yuebei Shi, Molei Liu, Zijian Guo — [TabCUQ: Context-Uncertainty Quantification for Tabular Foundation Models](http://arxiv.org/abs/2610.39558v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models use in-context learning to estimate conditional expected outcomes and average treatment effects for specific groups of individuals. Using these estimates to guide scientific decisions requires reliable uncertainty quantification. The challenge is to account simultaneously for two sources of uncertainty: limited-context bias and context variation arising from the small labeled sample supplied at inference. Predictive spread does not directly quantify both sources of unce...
  </details>

- **2026-10-29** — Xiangchong Li — [Low-variance renoising for weak gravitational lensing shear estimation](http://arxiv.org/abs/2610.39554v1)
  <details><summary>📄 Abstract</summary>
  The "renoising" noise-bias correction used by Metacalibration and AnaCal adds to every galaxy image an independent noise field with the statistics of the original noise rotated by 90 degrees. The rotated field cancels, to first order in shear, the anisotropy that the shear-response operation induces in the original noise, at the cost of doubling the noise variance. We derive the general condition that an added noise field must satisfy for this cancellation: the distribution of the total noise --...
  </details>

- **2026-10-29** — Ran Eisenberg, Steven Berger, Ofir Lindenbaum — [Interpretable by Design Tabular Prediction via In-Context Local Linear Learning](http://arxiv.org/abs/2610.39506v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) lets tabular foundation models make predictions without dataset-specific training or fine-tuning. These models achieve strong predictive accuracy, but interpreting how individual features contribute to the prediction remains difficult. In biology, for example, feature contributions can help identify biomarkers or risk genes. Post-hoc interpretability methods assign feature importance scores, but these scores do not indicate what the model actually uses and can lead to e...
  </details>

- **2026-10-29** — Sheng Wang, Jialu Yao, Maria V. Rossi et al. — [PathCowork: Learning from real-world pathology practice to build AI copilots](http://arxiv.org/abs/2610.39441v1)
  <details><summary>📄 Abstract</summary>
  Medical AI learns from the answers doctors record, but rarely from how they interpret the evidence to reach them. Here we introduce PathCowork, a framework that turns pathologists' narrated examinations into supervision for visual grounding and procedures that guide diagnostic AI agents. Synchronized gaze, narration and navigation link visual findings to the process of interpreting them. Across 48 sessions from 16 pathologists, the platform captured 1,028 minutes of slide review. Using these dat...
  </details>

- **2026-10-29** — Keyun Zhang, Dapeng Yin, Fanfu Wang et al. — [ATLAS-Bench: An Agentic Tool-Use Benchmark for Local Area Search](http://arxiv.org/abs/2610.39438v1)
  <details><summary>📄 Abstract</summary>
  Reliable local search is essential for LLM agents to support everyday decisions and longer plans by finding places that meet users' needs at given times and locations. Yet existing benchmarks provide limited coverage of whether search results satisfy mandatory requirements, account for preferences, and ground factual and experiential judgments in place attributes and reviews. We introduce ATLAS-Bench, a benchmark of 1,200 queries across three regions, expanded from real search events using place...
  </details>

- **2026-10-29** — Guizhen Chen, Weiwen Xu, Wotao Yin et al. — [Diagnosing the Reference Gap: What Visual Scaffolds Can and Cannot Fix in Multimodal Reasoning](http://arxiv.org/abs/2610.39419v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models can recognize visual content yet struggle to reason reliably over it across multiple steps. In counting, a model may see all objects but lose track of which ones it has counted. We argue that such failures, commonly attributed to perception, reveal a reference gap: the failure to bind language to the relevant visual entities, regions, or locations. Motivated by the theory of visual routines, we test whether external references such as numbering can narrow this ga...
  </details>

- **2026-10-29** — Vishal Saxena, Soumyajit Mandal — [OPERA: OPamp Design by an Expert-Taught Reasoning Agent, from Specifications to Layout](http://arxiv.org/abs/2610.39395v1)
  <details><summary>📄 Abstract</summary>
  Analog flows from specifications to a signed-off layout rarely run without manual iteration. Recent large language model (LLM) agents size circuits with optimizer loops over the device dimensions and stop at the schematic. We present OPERA (OPamp design by an Expert-taught Reasoning Agent), in which a general-purpose LLM agent designs CMOS opamps from specifications to post-layout sign-off with open-source tools. First, the designer teaches the agent the gm/ID method: map the specifications to t...
  </details>

- **2026-10-29** — Xiaomeng Xiong, Marcus Walker, Yanlin Jiang — [What Makes Medical Examination Items Difficult? Using Large Language Models to Explore Patterns Associated With Empirical Item Difficulty](http://arxiv.org/abs/2610.39373v1)
  <details><summary>📄 Abstract</summary>
  Research on medical item difficulty has largely focused on prediction rather than on identifying interpretable patterns associated with empirical difficulty. This study used empirical difficulty labels to guide large language models (LLMs) in inducing difficulty rubrics and examined how rubric guidance affected LLM difficulty judgments. Using training items and their empirical difficulty estimates from the United States Medical Licensing Examination (USMLE) and the Physician Assistant National C...
  </details>

- **2026-10-29** — Jonathan Yang, Chelsea Finn, Dorsa Sadigh — [Cross-Controller Transfer via In-Context Behavior Adaptation](http://arxiv.org/abs/2610.39280v1)
  <details><summary>📄 Abstract</summary>
  Generalist robot policies increasingly learn from data collected across diverse tasks and embodiments, yet typically assume a single controller for each robot. This assumption limits transfer because different controllers can assign different physical meanings to the same action and may require different strategies to complete a task. We study how to transfer robot data across both embodiments and controllers without allowing conflicting action interpretations to interfere with learning. Our set...
  </details>

- **2026-10-29** — Chan-Eui Song, Jeremy J. Michalek, Christopher McComb — [LLM-Assisted Optimization for Simulation-Based Redesign](http://arxiv.org/abs/2610.39275v1)
  <details><summary>📄 Abstract</summary>
  Engineering design frequently involves redesigning a prior solution to adapt to changes in context, such as material prices or system requirements. Redesign often leverages simulators too complex and/or computationally intensive for traditional numerical solvers, which lack engineering knowledge and context, to ensure global solution quality. Large language models (LLMs) can interpret semantic information, including engineering knowledge about the system and changes in context, to help guide sea...
  </details>

- **2026-10-29** — Siqing Huo, Andrew Parry, Debasis Ganguly et al. — [A Sequential Decision Framework for Evaluating LLM-Guided Search](http://arxiv.org/abs/2610.39231v1)
  <details><summary>📄 Abstract</summary>
  Recent systems applying retrieval-augmented generation (RAG) and "deep research" iteratively generate queries, retrieve documents, and examine their contents, using the resulting information to guide subsequent search steps. When this process is carried out autonomously rather than by a human searcher, the system must make explicit decisions about which search trajectories to explore and what objective the search is intended to optimize. We introduce a simple framework for reasoning about such s...
  </details>

- **2026-10-29** — Cheng Zhang — [Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis](http://arxiv.org/abs/2610.39168v1)
  <details><summary>📄 Abstract</summary>
  Few-shot voice cloning makes it cheap to produce daily Japanese financial commentary with several synthetic speakers, but kanji words with more than one reading, such as the word for "market" (shijo vs. ichiba) or "overall trend" (taisei vs. oze), are still misread. A common quality gate transcribes each synthesized sentence with automatic speech recognition (ASR), converts both the input and the transcript to kana, and regenerates on mismatch. We show that this gate is unreliable in both direct...
  </details>

- **2026-10-28** — Albert Bou, Javier Valdes-Aleman, Jon M. Laurent et al. — [Learning to Reason from Reference Samples Alone: Reinforced Adversarial Learning for Modern LLM Post-Training](http://arxiv.org/abs/2610.38851v1)
  <details><summary>📄 Abstract</summary>
  In many settings where LLM post-training is desirable, high-quality answers are recognizable but difficult to score with explicit rewards. Reinforcement learning with verifiable rewards (RLVR) is limited to tasks where an explicit correctness signal is available. Prior adversarial approaches to training reasoning LLMs either complement verifiable rewards with co-trained critics or require reference reasoning traces. We ask whether a co-trained LLM judge can turn reference answers alone into the ...
  </details>

- **2026-10-28** — Gangzhen Qian, Kainan Zhou, Chuhong Xu et al. — [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](http://arxiv.org/abs/2610.38361v1)
  <details><summary>📄 Abstract</summary>
  The external sources retained in our non-systematic audit did not isolate the incremental security or utility effect of consuming /llms.txt while ordinary retrieval remained fixed. The initial audit covered 39 sources through August 16, 2026, with later targeted updates through October 14. A purposive 15-tool study observed no automatic requests in 45 trials at one endpoint; a non-probability log study found that 97% of domains with detected files received no recorded requests in May 2026. We se...
  </details>

- **2026-10-28** — Shreyas Jadhav, S. Sudarshan — [LASSO: An LLM-Agent Synthesized System for SQL Validation](http://arxiv.org/abs/2610.38294v1)
  <details><summary>📄 Abstract</summary>
  The rise of Large Language Models (LLMs) has significantly advanced text-to-SQL capabilities, but generated queries may have errors. Test datasets are important for catching errors, but having only one or a few test datasets leaves many bugs undetected. Effective testing requires multiple test datasets that can expose subtle semantic bugs and edge cases. Recent work on test data generation and equivalence checking has focused on using constraint solvers. However, constraint-based approaches are ...
  </details>

- **2026-10-28** — Philipp Fleig — [Spectral theory of large data with power-law latent features](http://arxiv.org/abs/2610.39013v1)
  <details><summary>📄 Abstract</summary>
  Power-law eigenvalue spectra of covariance matrices estimated from data appear in diverse domains ranging from neural populations to proteins. We introduce a generative latent feature model for such data, optionally corrupted by measurement noise, and develop its spectral theory. We derive closed leading-order self-consistent equations for the Stieltjes transform of the covariance matrix from which the bulk eigenvalue density is obtained and provide a variational principle for the self-consisten...
  </details>

- **2026-10-28** — Mason Peterson, Gage MacLin, Camilla Tabasso et al. — [Open-World Object Motion Anticipation via Meta-Learned Semantic Adaptation](http://arxiv.org/abs/2610.38993v1)
  <details><summary>📄 Abstract</summary>
  Anticipating the motion of nearby objects is critical for safe and efficient robot navigation. Without a proper understanding of what may move, a robot may plan overly conservative, inefficient trajectories to guarantee safety, or it may be overly risky, resulting in unacceptable collisions. While tracking and predicting the motion of known objects has seen significant progress, little research addresses how a robot should adapt online to novel objects, including anticipating how one object may ...
  </details>

- **2026-10-28** — Yiran Lin, Ye Deng, Ziqi Pan et al. — [Exploring AI Peer in Collaborative Mathematics Learning](http://arxiv.org/abs/2610.38990v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) agents are increasingly explored as collaborative learning partners in mathematics education, yet it remains unclear what makes an AI recognizable as a peer. This study examines how domain experts perceive and interact with an adaptive LLM-based peer agent combining a Big Five-informed persona with motivational state modulation for collaborative mathematics problem solving. Through thematic analysis of expert interviews, we identify conditions shaping peer perception...
  </details>

- **2026-10-28** — Swathi Suhas, Anurag Das, Bernt Schiele et al. — [OneScene-Bench: Do Vision-Language Models Integrate Evidence Across Views?](http://arxiv.org/abs/2610.38926v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) increasingly process multiple views of the same scene, but it remains unclear whether they integrate these observations into a coherent scene-level representation. Existing multi-image evaluations do not isolate this capability, as tasks may admit correct solutions through independent per-view processing without requiring cross-view correspondence. We introduce OneScene-Bench, a controlled benchmark designed to explicitly distinguish when cross-view integration is n...
  </details>

- **2026-10-28** — Neerav Kaushal, Alisa Teige, Ajay MNV Penmatsa — [What to randomize matters: a controlled study of volume, axis and representation in low-data molecular generation](http://arxiv.org/abs/2610.38835v1)
  <details><summary>📄 Abstract</summary>
  Chemical language models can struggle to generate new molecules when trained on small datasets, where a model may reproduce training examples rather than learn a useful generative distribution. Randomized SMILES augmentation varies atom traversal, whereas Sequential Attachment-based Fragment Embedding (SAFE) also allows the order of fragment blocks to vary. How these distinct sources of representational variation affect low-data molecular generation has not been clearly studied. Here, using 1,00...
  </details>

- **2026-10-28** — Sabrina Armenio, Manuele Leonelli — [Measuring the Inaccessible: Can AI Evaluate Accessibility in Heritage Tourism?](http://arxiv.org/abs/2610.38642v1)
  <details><summary>📄 Abstract</summary>
  Accessibility assessment underpins the right to participate in heritage tourism, yet evaluation of archaeological sites remains artisanal: fieldwork does not scale, is often carried out without accessibility training, and is reported in forms that reach neither the sector nor disabled visitors. AI appears to offer a shortcut. We argue that assessment is measurement and inference under sparse, expert-mediated evidence: AI transforms how that evidence is captured and communicated, whereas evaluati...
  </details>

- **2026-10-28** — Suyeon Lee, Doyeop Kwak, Joon Son Chung — [SelectSep: Target-Selective Video Queries for Audio Source Separation](http://arxiv.org/abs/2610.38624v1)
  <details><summary>📄 Abstract</summary>
  Video-queried sound separation (VQSS) aims to isolate a target sound from an audio mixture using its corresponding video as a query. However, scene-level video queries can become ambiguous when multiple sounding objects are visible, particularly when the target and interferer are semantically similar. We propose SelectSep, a target-selective VQSS framework that jointly uses text and a single click coordinate to specify the target source and instance without requiring segmentation at inference ti...
  </details>

- **2026-10-28** — Chengsheng Zhang, Wenshen Xu, Yuchuan Wu et al. — [Co-Evolving Policy and Rubric via Capability Awareness for Open-Ended Generation](http://arxiv.org/abs/2610.38566v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based reinforcement learning (RL) offers interpretable, fine-grained supervision for aligning large language models (LLMs) on open-ended generation tasks. However, static rubric criteria may become saturated or remain beyond the policy's exploration, rendering the reward signals insufficiently discriminative. While recent efforts seek to guide sampling exploration or evolve rubrics, they fail to explicitly factor in how rubric difficulty should track the evolving policy's capabilities, re...
  </details>

- **2026-10-28** — Zifan Song, Caihua Shan, Kaitao Song et al. — [Cinematize from Unreal: Agentic Choreography for Controllable World Simulation](http://arxiv.org/abs/2610.38468v1)
  <details><summary>📄 Abstract</summary>
  Controllable world simulation requires more than visually plausible frames: scenes must retain persistent state, coordinated actions, and editable temporal structure. Generative world models offer flexible visual synthesis, but their outputs do not always expose the objects and transitions needed for precise revision. Graphics engines provide executable state and direct control, yet translating language into valid operations requires specialized knowledge of assets, geometry, and interdependent ...
  </details>

- **2026-10-28** — Yiyang Liao, Yitong Li, Jinjun Liu — [Phase-Compensated Frequency-Scan Measurement of Harmonic Transfer Function Impedance](http://arxiv.org/abs/2610.38453v1)
  <details><summary>📄 Abstract</summary>
  Impedance models obtained through frequency scanning provides terminal characterization for small-signal stability analysis without requiring detailed knowledge of internal converter parameters. When unbalanced steady-state components introduce cross-frequency coupling, conventional $2\times2$ impedance scan methods must be extended to identify harmonic transfer function (HTF) impedance. However, the measured phases of frequency-coupling terms depend on the starting time of the fast Fourier tran...
  </details>

- **2026-10-28** — Jiarun Shen, Xiao Li — [Deeper Backpropagation or More Updates? Training Looped Language Models Across Budgets](http://arxiv.org/abs/2610.38422v1)
  <details><summary>📄 Abstract</summary>
  Repeating transformer layers can improve language model performance without adding parameters. However, the added computational depth increases both forward and backward computation costs during training. Training such models requires choosing a backward window that controls how many final layer repetitions retain gradients during backpropagation. Longer windows improve per-token learning efficiency but increase per-update cost, while shorter windows reduce per-update cost but sacrifice per-toke...
  </details>

- **2026-10-28** — Xiaomeng Xiong, Marcus Walker, Yanlin Jiang — [LLMs as Judges and Examinees for Medical Item Difficulty Prediction](http://arxiv.org/abs/2610.38402v1)
  <details><summary>📄 Abstract</summary>
  Predicting medical item difficulty from item text alone remains challenging. Prior work has largely relied on linguistic features or text representations derived from general-purpose and domain-specific language models, but predictive performance has remained modest. This study takes a different approach by using difficulty-related signals that emerge when open-weight large language models (LLMs) interact with test items. Using USMLE and PANCE medical licensure examination items, we examined LLM...
  </details>

- **2026-10-28** — Ziwei Zhang, Tianyin Liao, Chunyu Hu et al. — [Learning a Prior-Data Fitted Network for Graph Foundation Models via Structural Causal Model Priors](http://arxiv.org/abs/2610.38335v1)
  <details><summary>📄 Abstract</summary>
  Graph Foundation Models (GFMs) have recently emerged as a promising paradigm for learning transferable representations across different graphs and domains. However, existing GFMs face notable limitations, including limited pre-training scale or reliance on aligning with textual information in Large Language Models (LLMs). To overcome these limitations, recent studies have drawn inspiration from prior-data fitted networks (PFNs), which learn from large synthetic datasets and support multi-domain ...
  </details>

- **2026-10-28** — Bohui Zhang, Albert Meroño-Peñuela, Elena Simperl — [Can LLMs Faithfully Solve Ontology Engineering Tasks? A Mechanistic Interpretability Study](http://arxiv.org/abs/2610.38326v1)
  <details><summary>📄 Abstract</summary>
  Ontological knowledge underpins large language model (LLM) performance on knowledge-intensive tasks. However, existing evaluations of LLMs' ontological understanding largely rely on behavioral correctness, leaving the underlying mechanisms unexplained. Existing mechanistic interpretability work has largely focused on instance-level factual knowledge, leaving ontological knowledge under-explored. To bridge this gap, we introduce MIOE, a causal-abstraction benchmark that evaluates interchange inte...
  </details>

- **2026-10-28** — Yufan Chen, Arnav Bali, Angela Liu et al. — [SSQA: Sibling-Selective Quadtree Attention for Hierarchical Modeling in Perception Tasks](http://arxiv.org/abs/2610.38320v1)
  <details><summary>📄 Abstract</summary>
  Perception tasks for navigation in robotics, including aerial platforms such as drones and autonomous driving systems, are inherently structured. Drone-mounted cameras typically capture sky above, terrain below, and obstacles or man-made structures in between, while driving data often contains organized road layouts, lane markings, and surrounding agents. Motivated by these axis-aligned structural priors, we note that such information is typically more structured than in generic image tasks. We ...
  </details>

- **2026-10-28** — Charin Polpanumas — [Vendster: An Evaluation Arena to Investigate How Forecasting Tool Quality Affects LLM Agent Behaviors in Buyer-Vendor Negotiation](http://arxiv.org/abs/2610.38292v1)
  <details><summary>📄 Abstract</summary>
  Time-series forecasters are ranked almost entirely by accuracy metrics, but a forecast's decision value, its effect on the downstream decision, need not track accuracy and is rarely measured. This problem compounds as large language model (LLM) agents increasingly consume forecasters as tools, mediating them through stochastic, opaque policies. We present Vendster, an evaluation arena measuring how a forecaster's bias and prediction-interval width change the outcome of a buyer--vendor discount n...
  </details>

- **2026-10-28** — Keepace. ai Team, Bowen Wu, Heng Wang et al. — [Keepace.ai: A Technical Report on a Large Language Model for Sports and Health](http://arxiv.org/abs/2610.38249v1)
  <details><summary>📄 Abstract</summary>
  Large language models hold promise for delivering safe, scientifically grounded, and personalized exercise guidance at scale, yet the sports-and-health domain still lacks curated training corpora and rigorous evaluation benchmarks. Keepace.ai is a domain-specialized LLM built on Qwen3.5-27B through post-training, currently optimized for Chinese-language exercise guidance across three tasks: workout plan generation, sports-and-health knowledge QA, and personal sports data analysis. In internal ru...
  </details>

- **2026-10-28** — Haichao Zhu, Geyang Xu, Zhaorui Yang et al. — [Precedent or Intent? What Coding Agents Follow When Evolving Existing Code](http://arxiv.org/abs/2610.38244v1)
  <details><summary>📄 Abstract</summary>
  Existing code reveals past implementation decisions but rarely explains the reasoning behind them. When coding agents implement new features or modify existing functionality, past decisions may conflict with new task instructions. This raises a fundamental question for agentic software evolution: when multiple implementations satisfy the same functional requirements, how do coding agents decide whether to follow existing code or new task instructions? We investigate this question through bidirec...
  </details>

- **2026-10-28** — Bowen Su, Huan Chen, Jiahua Ying et al. — [From Natural Language to Real Schematics: An Automated Workflow for Power Electronics Schematic Synthesis](http://arxiv.org/abs/2610.38201v1)
  <details><summary>📄 Abstract</summary>
  Designing power electronics converters traditionally requires intensive human expertise across topology sizing, commercial component selection, circuit simulation verification, and schematic drafting. While Large Language Models (LLMs) show promise in electronic design automation (EDA), applying standalone LLMs directly to board-level power electronics schematic synthesis suffers from severe engineering hallucinations, including inaccurate analytical sizing, fabricated or mismatched component pa...
  </details>

- **2026-10-28** — Debargha Ganguly, Divya Raghunathan, Dejan Jovanović et al. — [Scaling Lean Theorem Proving for Real-World Code Verification](http://arxiv.org/abs/2610.38174v1)
  <details><summary>📄 Abstract</summary>
  We present EasyProver, a Lean proving system built from recursive agents with isolated contexts, asynchronous search, parallel tactic probing, and an elastic elaboration service. Using an off-the-shelf frontier model with no additional training, it proves 669/672 PutnamBench problems and all six IMO 2026 formalizations and resolves 597/600 NTP4VC verification conditions and all 189 VERINA tasks by proof or refutation. Because these benchmarks are close to saturation, we also introduce Aegis, whi...
  </details>

- **2026-10-28** — Jingquan Yan, Yuwei Miao, Peiran Yu et al. — [B2P-Corr: Batch-to-Population Gradient Estimators for Non-Decomposable Correlation Losses](http://arxiv.org/abs/2610.38171v1)
  <details><summary>📄 Abstract</summary>
  Correlation metrics such as the Pearson Correlation Coefficient (PCC) and Concordance Correlation Coefficient (CCC) are standard regression metrics and learning objectives, but their non-decomposable nature poses a challenge for stochastic optimization. Since these metrics depend on dataset-level moments (mean, variance, covariance), naive mini-batch training with local statistics yields biased, high-variance gradients whose expectation does not align with the population gradient. To bridge this...
  </details>

- **2026-10-28** — Eva Vivalt — [Can Artificial Intelligence Forecast Treatment Effects in Economics?](http://arxiv.org/abs/2610.38883v1)
  <details><summary>📄 Abstract</summary>
  I use LLMs to forecast treatment effects of research studies pre-registered on the AEA RCT Registry and the Open Science Framework. I focus on studies whose results were first publicly released in 2026 and elicit forecasts from models whose training or knowledge cut-off dates were before the relevant set of papers was released. First, LLM models extract forecasting questions from the pre-registrations or pre-analysis plans. These questions elicit forecasted treatment effects; not all resolve in ...
  </details>

- **2026-10-28** — Shiqi Liu, Radu Corcodel, Ding Zhao — [ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation](http://arxiv.org/abs/2610.38388v1)
  <details><summary>📄 Abstract</summary>
  Quadrupedal manipulators can extend their workspace through whole-body interaction, but task-planning agents' capabilities remain limited by their available controllers. We present ELEVATE, a framework that uses persistent failures during task-program refinement to identify and acquire missing whole-body control capabilities. When these failures suggest a missing physical capability, a coding agent formulates and iteratively refines a reinforcement-learning problem, specifying behavior-specific ...
  </details>

- **2026-10-28** — Greta Perez-Haiek, Luca Macesanu, Kevin Angers et al. — [Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation](http://arxiv.org/abs/2610.38199v1)
  <details><summary>📄 Abstract</summary>
  Behavior Cloning has demonstrated promising generalization capabilities for robotic manipulation in terrestrial environments. However, marine visual distortions and dynamic currents create a severe domain shift that remains a key bottleneck in adapting generalist architectures to underwater field manipulation. To address this, 1616 episodes of underwater manipulation data were collected in calm and turbulent waters and were used to train 14 generalist Vision-Language-Action (VLA) models (Dynamic...
  </details>

- **2026-10-28** — Harvey Dam, Ganesh Gopalakrishnan — [Closed Gates Leak: Decomposing Adjacent-Layer Cancellation in Gated Language Models](http://arxiv.org/abs/2610.39068v1)
  <details><summary>📄 Abstract</summary>
  In transformer language models with gated multilayer perceptrons (MLPs), adjacent layers write partly against each other into the residual stream. Previous work interpreted this cancellation as layers proposing features and the next layer selectively rejecting the inappropriate ones. We decompose the cancellation by removing the previous layer's write from the input of the next MLP: what the next layer writes along that write splits into what it writes anyway and how much less its MLP writes bec...
  </details>

- **2026-10-28** — Shiping Yang, Chuanqi Tang, Hossein Hajimirsadeghi et al. — [Distilling the Shape of Uncertainty: What On-Policy Distillation Learns and How to Predict It](http://arxiv.org/abs/2610.39020v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) is increasingly adopted in the post-training of large language models. However, a stronger teacher may fail to improve the student. Prior work attributes this to a lack of new knowledge, but what that knowledge is remains unclear. We show that OPD learns not only \textit{how to branch}, i.e., which candidate tokens to consider, but also \textit{where to branch}, i.e., where to keep reasoning paths open. The existing token-overlap metric captures only the former. We i...
  </details>

- **2026-10-28** — Saumya Mundra, Ajoy Mondal, Vineeth N Balasubramanian et al. — [What do MLLMs know about 'Waldo'? Evaluating Visual Reasoning under Multi-Instance Multi-Object Challenges](http://arxiv.org/abs/2610.38957v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Multimodal Large Language Models (MLLMs) have led to significant progress in visual reasoning capabilities. However, existing benchmarks curate image-question pairs pertaining to object categories with few instances, enabling trivial object referencing and limited visual ambiguity. In this work, we introduce MIMO-Bench, a benchmark for evaluating MLLMs in a Multi-Instance per Multi-Object categories (MIMO) setting. Each image-question pair in our benchmark pertains to instance...
  </details>

- **2026-10-28** — Luis Ángel Calvo Pascual, Susana Merchán Rubira, Diego de Pereda Sebastián et al. — [Continuous Envy-Free Allocation via Reciprocal Preference Matrices: An Alternative to Sperner-Based Discretization](http://arxiv.org/abs/2610.38880v1)
  <details><summary>📄 Abstract</summary>
  Fair allocation problems on a continuous simplex are often approached through Sperner-type discretizations: agents label mesh vertices according to their preferences and a fully labelled elementary triangle gives a discrete localization of a fair outcome. We develop a continuous alternative for three agents and three alternatives by representing preferences with multiplicatively consistent reciprocal pairwise-comparison matrices. Two independent ratios per agent induce exact linear indifference ...
  </details>

- **2026-10-28** — Ben Chugg, Aritra Ghosh, Aaditya Ramdas — [Principal-agent hypothesis testing under adaptive experimentation](http://arxiv.org/abs/2610.38872v1)
  <details><summary>📄 Abstract</summary>
  Principal-agent hypothesis testing studies statistical contracts in which a principal rewards an agent according to data the agent generates. Existing work focuses on the single-shot setting, where the agent produces a single dataset. We extend the framework to sequential settings, where evidence accumulates over time, rewards may be deferred to the end or disbursed incrementally, and the agent may stop the contract at a strategically chosen stopping time. We call a contract null-deterring if no...
  </details>

- **2026-10-28** — Victor Barroso-Nascimento, Joaquim T. Waddington, Elaine Pimentel — [Connecting Base-Extension Semantics, Beth Semantics, and Ecumenical Logic](http://arxiv.org/abs/2610.38871v1)
  <details><summary>📄 Abstract</summary>
  We investigate the relationship between base-extension semantics, Beth semantics, and Prawitz's ecumenical logic. We first present a base-extension semantics for the propositional fragment of Prawitz's system and prove that it is sound and complete. The semantics interprets intuitionistic and classical operators directly within a common proof-theoretic framework, without reducing the classical operators to their intuitionistic counterparts by means of a translation. We then analyse the effect of...
  </details>

- **2026-10-28** — Eunbi Rha, Abhijatmedhi Chotrattanapituk, Mouyang Cheng et al. — [Autonomous Quantum Measurement with Agentic AI](http://arxiv.org/abs/2610.38850v1)
  <details><summary>📄 Abstract</summary>
  Quantum materials exhibit diverse electronic and functional phenomena, but their characterization requires extensive experimental expertise, iterative decision-making and accumulated laboratory knowledge that is difficult to document and transfer. Here we introduce Quantum Agent (QUANTA), an agentic artificial intelligence (AI) framework for autonomous quantum-materials characterization. Using a widely adopted Physical Property Measurement System (PPMS) as an experimental platform, QUANTA combin...
  </details>

- **2026-10-28** — Peter Sunehag — [From Grind to Grasp](http://arxiv.org/abs/2610.38728v1)
  <details><summary>📄 Abstract</summary>
  Discussions of complexity, knowledge and intelligence often overlook the work involved. For example, outputs generated by short programs have low algorithmic complexity but can have high computational depth, the least work needed to produce them from near-shortest programs. Producing them with less work can require longer descriptions, giving high work-bounded complexity. We introduce a formalism that compares achievements under work and information limits and describes how learning and persiste...
  </details>

- **2026-10-28** — Nouar AlDahoul, Yasir Zaki — [From Leniency to Suspicion: How an Open Post-Training Recipe Changes Whom LLM Fact-Checkers Believe](http://arxiv.org/abs/2610.38532v1)
  <details><summary>📄 Abstract</summary>
  LLMs increasingly fact-check online content with the poster's identity in view. However, it remains unclear which post-training changes how much a model's truth judgement depends on the poster's social class, and how such a change happens inside the model. This paper investigates job-based doubt, i.e., judging a claim false more often when the poster has a lower-status job, using fact-checked claims with randomised poster profiles in base and post-trained checkpoints of six model families. Our r...
  </details>

- **2026-10-28** — William Lane — [Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)](http://arxiv.org/abs/2610.38384v1)
  <details><summary>📄 Abstract</summary>
  Speech technology for Irish must be built from very little transcribed speech, yet the language's pronunciation is thoroughly documented in dictionaries and dialect descriptions. We ask whether that documentation can supervise the adaptation of a large pretrained text-to-speech model to a language it was never trained on. We adapt Qwen3-TTS to Irish using 12.8 hours of crowdsourced Common Voice speech, correcting two defects in the vendor fine-tuning script that training loss does not reveal (Ap...
  </details>

- **2026-10-28** — Kriti Mahajan — [The Indian Financial Automated Advice Bias (IFAAB) Dataset : Auditing Socioeconomic and Demographic Disparities in LLM-Generated Financial Advice in India](http://arxiv.org/abs/2610.38239v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used for financial guidance, yet little is known about whether their advice changes across social identities in Global South contexts. We introduce the Indian Financial Automated Advice Bias (IFAAB) benchmark, a counterfactual audit dataset of 31,734 GPT-4o-generated financial-advice responses for synthetic Indian personas varying by gender, caste, education, employment, residence, age, and district. Holding the underlying request fixed, we evaluate dispari...
  </details>

- **2026-10-28** — Yunhong Han, Gaopeng Ren, Yan Liu et al. — [Generative discovery of chemical reaction networks](http://arxiv.org/abs/2610.38236v1)
  <details><summary>📄 Abstract</summary>
  Chemical kinetics determines molecular stability, reaction selectivity and the evolution of reacting mixtures, but discovering the underlying reaction networks remains challenging. Here we introduce ReactNexus, a generative framework for kinetic-guided network exploration starting solely from reactant graphs. Generative models propose transition states and predict the full reaction trajectories connecting reactants and products, while calculations using a machine-learned interatomic potential ve...
  </details>

- **2026-10-28** — Jeremy P. Scott, Locke D. Spencer, Chris Benson et al. — [Experimental Demonstration of Double-Fourier Interferometer Imaging for Future Space-Based Far-Infrared Observatories](http://arxiv.org/abs/2610.38105v1)
  <details><summary>📄 Abstract</summary>
  Far-infrared (FIR) astronomy is crucial for observing star formation, active galactic nuclei, and protoplanetary systems, but its effectiveness is severely limited by poor diffraction-limited spatial resolution. To overcome this limitation, a double-Fourier interferometer (DFI), which couples a spatial interferometer with a Fourier transform spectrometer, has been proposed to deliver high-resolution broadband spectral imaging. Despite various conceptual and prototype studies, a comprehensive dem...
  </details>

- **2026-10-27** — Saransh Kumar Gupta, Akshadha Sharma, Lipika Dey et al. — [What Constitutes Food Similarity? Visual Representations and Retrieval in Indian Cuisine](http://arxiv.org/abs/2610.37867v1)
  <details><summary>📄 Abstract</summary>
  Food similarity underlies retrieval, recommendation, substitution, and other food computing tasks, yet food representations are typically evaluated by identity preservation. We ask what happens to food similarity beyond identity: how different visual representations organize foods into relational neighborhoods, what culinary relationships these neighborhoods reveal or obscure, and how consistently these structures emerge across representations. Indian cuisine provides a challenging setting in wh...
  </details>

- **2026-10-27** — Thomson Yen, Gilbert Yang, Naimeng Ye et al. — [Seq@K: Evaluating Language Models Under Sequential Feedback](http://arxiv.org/abs/2610.37859v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents differ fundamentally from prior intelligent systems in their ability to learn from natural language in context. This capability enables agents to iteratively refine their answers in response to feedback, a prevalent mode of operation in modern agentic workflows. However, the community primarily ranks models by metrics such as Pass@1 or Pass@K, which cannot capture how they utilize feedback on prior attempts. We introduce Seq@K, a natural evaluation protocol that measures wh...
  </details>

- **2026-10-27** — Abhinav Goel, Agostino Capponi, Alfio Gliozzo et al. — [Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis](http://arxiv.org/abs/2610.37830v1)
  <details><summary>📄 Abstract</summary>
  AI agents can now write software from a plain-English description, but code that runs is not the same as code that does what was asked. This gap matters most for smart contracts, the programs behind Web3 applications that move money on a blockchain and cannot be fixed once deployed. We ask how to check whether an AI-written contract behaves as it should, and where the requested behavior gets lost.   We design an evaluation built on execution rather than opinion. We replay the same transactions o...
  </details>

- **2026-10-27** — Diksha Gupta, Rieke Fruengel, Stefan Heimersheim — [Spokes, not a Ring: Revisiting the Weekday Manifold in Language Models](http://arxiv.org/abs/2610.37796v1)
  <details><summary>📄 Abstract</summary>
  Recent work has hypothesised that large language models may represent some concepts as multi-dimensional manifolds instead of single directions. Using these manifolds to interpret or steer representations often assumes that moving along them corresponds to a continuous change in the represented concept. In this work, we test this continuous manifold assumption on the prototypical weekday manifold. Despite its striking circular geometry, we find that the weekday representations behave more like s...
  </details>

- **2026-10-27** — Yusheng Zhao, Bowei He, Xue Liu et al. — [SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World](http://arxiv.org/abs/2610.37919v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate empirical evidence from pretrained priors. We introduce SciGame, a controlled benchmark that converts scientific literature into structured scientific cards. Each card yields a pair of Original and dimensionally consistent Counterfactual environments with the same task interface....
  </details>

- **2026-10-27** — Petr Molodyk, Yuchen Zhu, Jaemoo Choi et al. — [Multi-Draft On-Policy Distillation for Diffusion Drafters](http://arxiv.org/abs/2610.37778v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding is used to reduce the inference cost of language models. One-step diffusion drafters propose a block of multiple tokens in parallel, reducing the sequential cost of speculative decoding. On-policy distillation trains these drafters using verifier feedback on their own proposals. However, parallel drafting makes this feedback difficult to use: the drafter predicts each token without observing the preceding tokens sampled within the same block, while the verifier conditions it...
  </details>

- **2026-10-27** — Alexander Wu, Jingchao Huang — [CADENCE: Distributional Next-Transaction Forecasting for Business Cash-Flow Underwriting](http://arxiv.org/abs/2610.38084v1)
  <details><summary>📄 Abstract</summary>
  Recurring cash flows are the backbone of cash-flow underwriting: they separate durable revenue from one-off deposits, expose standing obligations, and ultimately determine ability to pay. For small businesses, recurrence is both indispensable and hard to estimate, because much of their income arrives as ambiguous transfers, most payment streams are short, and schedules follow calendar conventions that frequency-domain methods treat as noise. We present CADENCE, Calendar-Aware Distributional Even...
  </details>

- **2026-10-27** — Baptiste Arnaudo, Amine Bennouna, Sébastien Martin — [Interpretable Feature Discovery from Unstructured Data Using LLMs and Statistical Choice Models](http://arxiv.org/abs/2610.38082v1)
  <details><summary>📄 Abstract</summary>
  Feature extraction from unstructured data typically relies on opaque embeddings unsuited to interpretable decision-making. Interpretable features, on the other hand, typically require costly, and often infeasible, hand-engineering. Large language models (LLMs) offer a natural bridge, as they can read raw data and describe it in interpretable terms. One could simply ask an LLM to extract features from a large sample of the dataset, but context limitations and diluted attention can lead to unsatis...
  </details>

- **2026-10-27** — Laura Laurenti, David Liu, Brian Kulis et al. — [Are Seismic Foundation Models More Than Glorified Feature Extractors?](http://arxiv.org/abs/2610.38003v1)
  <details><summary>📄 Abstract</summary>
  Earthquake sequences are stochastic on two separated timescales: the seismic waves of any individual earthquake propagate over seconds to minutes, while the earthquakes themselves arrive as a sparse, self-exciting occurrence process, with inter-event intervals from seconds to months. Respecting both scales in one training objective is the open challenge. Foundation models (FMs) for seismic waveforms instead import their learning targets from audio and vision, where every target is computed from ...
  </details>

- **2026-10-27** — Tianchu Li, Pranay Venkatesh, Andrés Montoya-Castillo — [Continuous Representation Theory of the Hierarchical Equations of Motion](http://arxiv.org/abs/2610.37953v1)
  <details><summary>📄 Abstract</summary>
  The numerical stability of the hierarchical equations of motion (HEOM) depends on the representation of their Liouvillian. Here, we introduce a continuous gauge freedom through a generalized Bogoliubov transformation with the parameter $r$. It subsumes earlier phase space stabilization methods as special cases and explains both their stabilizing mechanism and their limitations. We find that gauge optimization balances the suppression of hierarchy growth against errors in reconstructing the reduc...
  </details>

- **2026-10-27** — Marcos Hernanz — [Muon Makes the First Mixture-of-Experts Layer Harder to Balance](http://arxiv.org/abs/2610.37914v1)
  <details><summary>📄 Abstract</summary>
  Many open mixture-of-experts (MoE) language models train with Muon instead of AdamW. Most balance the load with a bias on each expert's routing score, adjusted after every step. Their recipes disagree on whether Muon should also train the router. In models with 55M and 108M active parameters, we measure how the optimizer changes the span of these biases, the largest minus the smallest in a layer. The span grows when all tokens favor the same experts, so it shows how hard a layer is to balance. A...
  </details>

- **2026-10-27** — S. A. Adedayo — [fastC-GC and fastC-GC*: Efficient RCCP-Guided Graph Estimation for Time Series](http://arxiv.org/abs/2610.37883v1)
  <details><summary>📄 Abstract</summary>
  We introduce fastC-GC and fastC-GC$^*$, computationally efficient methods for time-series graph estimation using the two-test rule motivated by Reichenbach's common cause principle (RCCP) and the conditioning sets of causalised Granger causality (c-GC and c-GC$^*$). The methods use standardized data, ridge-residual correlation, and complete circular shift enumeration evaluated by Fourier transforms. Shared precision calculations and Schur downdates avoid repeated regression fits. On a single-thr...
  </details>

- **2026-10-27** — Jasel Berra-Montiel, Alberto Molgado, Mar Sánchez-Córdova — [The Geometry of Quantum Teleportation in Phase Space](http://arxiv.org/abs/2610.37861v1)
  <details><summary>📄 Abstract</summary>
  We formulate the standard quantum teleportation protocol within the framework of deformation quantization, employing the Stratonovich--Weyl (SW) correspondence and the associated star product on the coadjoint orbits of $SU(2)$. Each qubit is represented by a spherical phase space $S^2$ endowed with the Kirillov--Kostant--Souriau (KKS) symplectic structure. Within this setting, we explicitly construct the phase space representations of the entangled Bell resource, the controlled-NOT and Hadamard ...
  </details>

- **2026-10-27** — Giovanni dos Santos Franco, Felipe Mahlow, Ellison Fernando Cardoso et al. — [Responsible Quantum Machine Learning for Medical Imaging: A Fairness Audit Across Sensitive Subgroups](http://arxiv.org/abs/2610.37819v1)
  <details><summary>📄 Abstract</summary>
  Quantum machine learning (QML) is increasingly explored for medical classification, yet its behaviour under subgroup-aware fairness criteria remains understudied. We present an empirical fairness audit of classical and quantum classifiers for medical imaging, assuming QML is not inherently fair. Two scenarios are evaluated: dermatological lesions on DDI (sensitive attribute: Fitzpatrick skin type) and chest X-rays on CheXpert-derived data (sensitive attribute: age group). Using ResNet-18 embeddi...
  </details>

- **2026-10-27** — Ahmad Khan — [The Interference-Conjugate Transform: The Tightest Interference-Linear Surrogate for Power Control, Scheduling and Beamforming in Wireless Networks](http://arxiv.org/abs/2610.37794v1)
  <details><summary>📄 Abstract</summary>
  Closed-form fractional programming (FP), weighted MMSE (WMMSE), and the 2026 surrogate-enhanced methods SEFP and XMMSE all maximize the weighted sum rate by iteratively maximizing a surrogate linear in the interference power. We show that this family admits a unique best member: the interference-conjugate transform (ICT), which replaces each rate term $\log(1+a/b)$ by $\max_{κ\ge0}[Ω(κa)-κb]$, where $Ω$ is the closed-form partial convex conjugate of the rate in the interference variable and the ...
  </details>

- **2026-10-27** — Jiarui Yao, Shweta Parihar, Nghia Tuan Bui et al. — [Locating Sycophancy Across Training Stages in Open Language Models](http://arxiv.org/abs/2610.37788v1)
  <details><summary>📄 Abstract</summary>
  Language model assistants sometimes change a correct answer when the user suggests a wrong one. The behavior, called sycophancy, is usually attributed to preference-based post-training, yet early measurements found it in pretrained models. We ask where it comes from by measuring it at every available stage of training: 13 open checkpoints from 5 lineages, from base model through supervised fine-tuning and preference optimization to release. We separate how far an injected claim moves a model's a...
  </details>

- **2026-10-27** — Remy Ogasawara, Cullen Anderson, Narmeen Fatimah Oozeer et al. — [Orthogonal and Parametrized Multi-Attribute Steering of LLMs](http://arxiv.org/abs/2610.37517v2)
  <details><summary>📄 Abstract</summary>
  Activation steering offers an effective and efficient way to modify an LLM's behavior at inference time. However, it remains unclear how to apply steering such that the signal is consistently strong and the steering strength has a universally interpretable meaning. We address this first by identifying the most steerable interval for each steering vector and rescaling the steering range accordingly. Building on this, we introduce a more interpretable method for steering, called parameterized stee...
  </details>

- **2026-10-27** — Nobuaki Tanaka — [Regression Functions as Fields on Covariate Space: Evolution Equations, the Hessian, and Identification](http://arxiv.org/abs/2610.37500v2)
  <details><summary>📄 Abstract</summary>
  For each time $t$, the regression function $m_t(x)=E[Y_t\mid X_t=x]$ of an outcome on contemporaneous covariates can be regarded as a field on covariate space. When the covariates of units move as a diffusion and each unit's outcome has its own dynamics, we show that $m_t$ satisfies a second-order evolution equation whose diffusion term is $\frac12\mathrm{tr}(Σ\nabla^2 m_t)$, the Hessian of the regression function weighted by the covariance $Σ$ of covariate increments, whose transport term is th...
  </details>

- **2026-10-27** — Xiaochen Chang — [A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](http://arxiv.org/abs/2610.36717v1)
  <details><summary>📄 Abstract</summary>
  When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human reader. The defensive context may also influnce the consequent when we simply ban defensive writing in the output through prompts. In order to reduce over-defensive writing, we produce a harness that separates the reviewer,...
  </details>

- **2026-10-27** — Amit Kalitaa, Moirangthem Tiken Singh — [When Does Perturbation Consistency Add Information Beyond Softmax Confidence? Theory and Evidence for the Decision Consistency Framework](http://arxiv.org/abs/2610.36640v1)
  <details><summary>📄 Abstract</summary>
  Perturbation consistency scores judge whether a prediction survives small input changes. The Decision Consistency Framework (DCF) scores each image by label stability (LS) and confidence deviation (CD) under six mild operators, combines them into a consistency score (CS), and summarises a model by the gap between accuracy and mean consistency (CAG). We ask when these scores carry information that the clean softmax output lacks. Across 201 evaluations with three seeds per configuration, CS detect...
  </details>

- **2026-10-27** — Joseph Natter, Long Vu, Yifan Zhang et al. — [GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting](http://arxiv.org/abs/2610.37598v1)
  <details><summary>📄 Abstract</summary>
  Traffic forecasting requires modeling complex temporal dynamics and the spatial dependencies imposed by road topology. Supervised graph-based models achieve strong performance, but are often trained for a particular dataset and sensor graph, making deployment to new or evolving networks costly. Prior-Data Fitted Networks (PFNs) offer a zero-shot alternative by learning in-context inference from synthetic task priors, which provide an explicit mechanism for encoding domain-specific assumptions. E...
  </details>

- **2026-10-27** — Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck et al. — [TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments](http://arxiv.org/abs/2610.37592v1)
  <details><summary>📄 Abstract</summary>
  Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on information they will not have when they act, an information gap between training and execution. It widens under partial observability, observation noise, and openness, where the set of agents and tasks present changes during ...
  </details>

- **2026-10-27** — Xinying Qian, Ying Zhang, Yu Zhao et al. — [ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents](http://arxiv.org/abs/2610.37443v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations. However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-grained memory units; and (2) Organizational Mismatch, where memory structures based primarily on semantic similarity may overlook other associations. To address these challenges, we propose ETAMem, a multi-view memory fr...
  </details>

- **2026-10-27** — Jiahong Xiang, Kunqiu Chen, Lingming Zhang et al. — [Spine: Compiling Subtask Trees into Structured Context for Long-Horizon Coding Agents](http://arxiv.org/abs/2610.37224v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon coding tasks contain nested subtasks. Typically, agents record interactions sequentially into a growing history, causing context inflation and performance degradation. Compressing or trimming the history without explicit subtask boundaries can discard information needed by unfinished subtasks. Conversely, recursive subagent delegation isolates completed subtasks through child agents by assigning every subtask boundary to delegation, which conflates subtask granularity with executing...
  </details>

- **2026-10-27** — Touko Lehenkari, Hannu-Pekka Komsa — [Cu intercalation and field-driven filament formation in vertically aligned MoS$_2$ memristors](http://arxiv.org/abs/2610.37152v1)
  <details><summary>📄 Abstract</summary>
  Vertically-aligned MoS$_2$ films paired with a Cu top electrode have been used as electrochemical metallization cell memristor devices. The memristive switching has been attributed to the formation of conductive filaments, yet their exact structure has remained elusive. Here we carry out a multi-scale computational study of Cu intercalation, clustering, and field-driven dynamics to eventually model the filament formation under operating conditions. We use density-functional theory results to fin...
  </details>

- **2026-10-27** — Zichen Yan, Rui Huang, Shenao Wang et al. — [Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision](http://arxiv.org/abs/2610.36968v1)
  <details><summary>📄 Abstract</summary>
  Image-goal navigation (ImageNav) requires an agent to reach a location specified by a goal image in an unknown environment. For drones, this task demands exploration, goal- directed navigation, and collision avoidance under limited onboard computing resources. Existing aerial ImageNav methods are built on single-view observations, requiring additional rotation and exploration to search for goal-relevant cues outside the field of view. In this paper, we present Omni-IGN, a fully onboard ImageNav ...
  </details>

- **2026-10-27** — Jinyang Li, Zichuan Fu, Xian Wu et al. — [Proactive Memory for Event-Driven LLM Agents](http://arxiv.org/abs/2610.36967v1)
  <details><summary>📄 Abstract</summary>
  Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their applicability to the current event. We propose Proactive Memory (ProactMem), which organizes history into recent events, temporal trajectories, and behavioral regularities. Trajectory facts are checked against source even...
  </details>

- **2026-10-27** — Xiaohan Ye, Zihan Gong, Jingqian Zhao et al. — [PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search](http://arxiv.org/abs/2610.36958v1)
  <details><summary>📄 Abstract</summary>
  Generative retrieval models have been increasingly adopted in search and recommendation systems. However, industrial generative retrieval models are commonly specialized to a fixed online scenario: they learn from scenario-specific interactions, support a narrow set of query forms and retrieval objectives. We study how to remove these couplings and build a unified end-to-end multimodal search system for open-ended image--text queries, heterogeneous shopping intents, and online scenarios with dif...
  </details>

- **2026-10-27** — Chaolang Li, Jingyu Li, Zhaocheng Du et al. — [Natural Hard-Negative Mining from Positives for Instruction-Following Retrieval](http://arxiv.org/abs/2610.36900v1)
  <details><summary>📄 Abstract</summary>
  Instruction-following information retrieval (IFIR) requires retrievers to rank documents by both a query and its instance-specific instructions, yet instruction-conditioned contrastive supervision remains scarce. Existing synthetic methods typically fix a positive passage and generate additional negatives, overlooking the hard-negative potential of the original positive. We propose Natural Hard-Negative Mining (NHNM), which promotes convertible negatives under query-compatible instructions and r...
  </details>

- **2026-10-27** — Jianwei Jiang, Chunhua Yang — [Maximum Energy of Integral Circulant Graphs with Same-Parity Exponents](http://arxiv.org/abs/2610.36883v1)
  <details><summary>📄 Abstract</summary>
  The energy of a finite graph is the sum of the absolute values of the eigenvalues of its adjacency matrix. Let n be p to the power a times q to the power b, where p and q are distinct primes at least five and a and b, both positive integers, have the same parity. Among all nonempty sets D of proper divisors of n, the energy of the corresponding integral circulant graph is maximised by exactly two divisor sets: the divisors p to the power i times q to the power j with i plus j odd, and the diviso...
  </details>

- **2026-10-27** — Haoyu Zhao, Yinzhou Tang, Zixuan Wang et al. — [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](http://arxiv.org/abs/2610.36791v1)
  <details><summary>📄 Abstract</summary>
  Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human interaction videos, robot demonstrations, and simulation rollouts without requiring a...
  </details>

- **2026-10-27** — Rohan Deb, Mohammad Ghavamzadeh, Arindam Banerjee — [Conservative Dueling Bandits: Preference Learning under Baseline Constraints](http://arxiv.org/abs/2610.36708v1)
  <details><summary>📄 Abstract</summary>
  Contextual dueling bandits learn from pairwise comparisons, the same feedback used to fine-tune language models from human preferences. Standard algorithms explore aggressively and can show users two poor options. We study conservative contextual dueling bandits, which require that, at every round, the cumulative score of the better displayed item stay above a $(1-α)$ fraction of a trusted baseline's. An item's score is its probability of beating the best available item, so the constraint depend...
  </details>

- **2026-10-27** — Shang Tingyu, Cao Wenfei — [Balanced State Subspaces for Mamba-2 State Compression](http://arxiv.org/abs/2610.36617v1)
  <details><summary>📄 Abstract</summary>
  Mamba-2 compresses all context into a fixed-size recurrent state that dominates decoding memory and bandwidth. Existing compressors quantize state values or prune state coordinates, scoring each channel independently in the native basis. We examine trained Mamba-2 states and find that energy is almost rank-one, but the output does not read the energetic directions: energy concentrates in a bias-like direction accumulated by the recurrence, while the content the output reads lives in a low-dimens...
  </details>

- **2026-10-27** — Jane Pan, You Lyu, Abe Bohan Hou et al. — [Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](http://arxiv.org/abs/2610.36435v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategically bargaining with other agents. To isolate the effect of user presence, we develop PRESENT, a controlled evaluation framework that compares negotiation settings with and without an interactive user, while holding the...
  </details>

- **2026-10-27** — Matthew J. Liu, Aaron D. Kaplan, Michael L. Whittaker et al. — [Simulated petrological labels enable probabilistic mineralogy prediction from whole-rock geochemistry](http://arxiv.org/abs/2610.36429v1)
  <details><summary>📄 Abstract</summary>
  Modal mineralogy, the mineral identities and abundances in rocks, guides geological studies and industrial resource extraction. While measuring modal mineralogy is time-intensive, whole-rock chemical measurements furnish elemental concentrations at higher throughput. Predicting mineralogy from elemental data, however, poses a one-to-many inverse problem, and labeled mineralogical datasets are too sparse to train on at scale. We address both challenges by simulating petrological labels that expre...
  </details>

- **2026-10-27** — Zhen Yang, Wen Wang, Xander Xu et al. — [Can LLMs Uncover Hidden Physical Laws through Free Exploration?](http://arxiv.org/abs/2610.37649v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without being told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates simulated worlds with altered physics, where one or more laws differ from ordinary ph...
  </details>

- **2026-10-27** — Baptiste Bonin, Caro Strickland, Audrey Durand — [Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use](http://arxiv.org/abs/2610.37533v1)
  <details><summary>📄 Abstract</summary>
  Failure diagnosers for robot manipulation are increasingly vision--language models (VLMs), trained and evaluated on single-arm failures produced by perturbing a successful demonstration. Bimanual tool use adds failures of other kinds: a tool that slips out of its socket while still held, two correct gestures made at different times, and attempts that fail for two reasons at once. On a simulated bimanual tool-use task whose failure causes are read from the recorded trace, we measure what each sen...
  </details>

- **2026-10-27** — Mingwei S. G. Li, Susie S. Y. Li, Isabel Moreira de Oliveira et al. — [PolyGandr: Steering Generative Models via Spatial Navigation through Latent Space](http://arxiv.org/abs/2610.37446v1)
  <details><summary>📄 Abstract</summary>
  Generative models support content creation across text, images, videos, and design disciplines, yet their interfaces rely primarily on natural language. While effective for specifying high-level intent, language can be inefficient and imprecise for fine-grained control, iterative refinement, and open-ended exploration. We present PolyGandr, a visual interface for exploring relationships between latent representations and generated outputs, complementing natural-language model steering. PolyGandr...
  </details>

- **2026-10-27** — Sinjae Kang, Dong Kyu Shin, Jaehong Kim et al. — [Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling](http://arxiv.org/abs/2610.37393v1)
  <details><summary>📄 Abstract</summary>
  Robot policy evaluation often relies on a binary success signal for task completion. In real-world deployment, however, desired execution behaviors are also defined by quality attributes such as execution speed and motion smoothness, which need to be dynamically controlled according to task requirements. To address this, we introduce Quality-Controllable Policy (QCP), a robot policy that enables inference-time control over both individual quality attributes and their combinations. To extend the ...
  </details>

- **2026-10-27** — Zhi Zheng, Binglin Liu, Weihao Chen et al. — [Peers4U: Designing Learner-Centered Virtual Peers for Children's Multimodal Mathematics Learning](http://arxiv.org/abs/2610.37238v1)
  <details><summary>📄 Abstract</summary>
  In early mathematics, children learn abstract concepts through concrete representations, such as manipulating objects, drawing, and speaking. Learning with peers can enrich this process by exposing children to diverse strategies and enabling them to exchange ideas through interaction. We realized this potential with virtual peers in Peers4U, a multimodal learning system to enhance children's mathematical conceptual understanding. Virtual peers driven by LLMs are personalized to the learner's cog...
  </details>

- **2026-10-27** — Callum Berger, Jeremy Pitt, Stefan Sarkadi — [A Serious-Game Testbed for Self-Governing Human-Machine Institutions](http://arxiv.org/abs/2610.36989v1)
  <details><summary>📄 Abstract</summary>
  AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer interaction that needs a testbed for hybrid institutions. We present Megabike, a multi-agent simulator and serious game with interdependent arenas for common-pool resource management, cooperative survival and constitutional...
  </details>

- **2026-10-27** — Andie Huang, Ying Pang, Qian Zhang et al. — [Does More Thinking Pay Off? Reasoning Cost and Correctness of LLMs in Code Generation and Bug Fixing](http://arxiv.org/abs/2610.36952v1)
  <details><summary>📄 Abstract</summary>
  Many LLMs now emit an explicit reasoning trace before they write code, but benchmark results for code generation and bug fixing usually report correctness alone. It is therefore unclear how much the extra reasoning contributes relative to the tokens it consumes. We examine this question with 866 Python tasks drawn from HumanEval Pro, MBPP Pro, and BugsInPy under five model settings. We look at the accuracy gain and token overhead of reasoning, the behaviors that appear inside reasoning traces, a...
  </details>

- **2026-10-27** — Shiyi Cao, Ziming Mao, Dacheng Li et al. — [Evolving Agent Teams](http://arxiv.org/abs/2610.36848v1)
  <details><summary>📄 Abstract</summary>
  The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce Evolving Agent Teams, a multi-agent framework that escapes such local optima. It features (1) a central supervisor that diagnoses each local optimum and restructures a team of agents; and (2) a persistent file system tha...
  </details>

- **2026-10-27** — Hongyu Wu, Chong Liu, Shaoxuan Xie et al. — [RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning](http://arxiv.org/abs/2610.36685v1)
  <details><summary>📄 Abstract</summary>
  Bimanual robot manipulation plays an important role in real-world robotic applications, but the high cost of collecting bimanual demonstrations limits the scalable development of bimanual policy learning. Meanwhile, existing single-arm manipulation data are difficult to directly transfer to bimanual systems due to the Single-to-Dual gap in action spaces, coordination requirements, and arm-side spatial preference. To address this issue, we propose RoboSTD, a zero-shot Single-to-Dual data construc...
  </details>

- **2026-10-27** — Buzhao Liu, Jianing Ye, Xiu Yuan et al. — [RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](http://arxiv.org/abs/2610.36533v1)
  <details><summary>📄 Abstract</summary>
  Recently, LLM-based autonomous agents have shown strong capabilities in iteratively generating, evaluating, and refining executable solutions. In robotic manipulation, Code-as-Policy lets these agents search over modular and editable robot programs. However, effective program search requires physical understanding: agents must understand how objects can be manipulated, how scene geometry constrains actions, and why interactions succeed or fail. Existing methods rely mainly on execution feedback ...
  </details>

- **2026-10-27** — Yibo Yang, Zerui Huang, Haomiao Yang et al. — [MedConstBench: Benchmarking How Constitutions Steer LLMs in Medical Ethics](http://arxiv.org/abs/2610.36513v1)
  <details><summary>📄 Abstract</summary>
  As large language models advance rapidly, they are increasingly used to answer medical questions, and many such models are now deployed locally. Once a model is deployed, its behavior is governed mainly by the ethical policy written into its constitution. However, most existing work focuses on factual correctness rather than the trade-off between competing ethical values. Even benchmarks that do evaluate ethics treat it as a fixed property of the model rather than as a variable, so how a constit...
  </details>

- **2026-10-27** — Truman Hickok — [SO-101 Bench: Accessible Spatial Manipulation](http://arxiv.org/abs/2610.36420v1)
  <details><summary>📄 Abstract</summary>
  Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup. It has four tasks scored as five families, ...
  </details>

- **2026-10-27** — Avishi Poddar, Nico Baßler, Julian Lyne et al. — [Exact Analytical Treatment of Collectively Pumped Dicke Superradiance](http://arxiv.org/abs/2610.37665v1)
  <details><summary>📄 Abstract</summary>
  We study the dynamics of an ensemble of $N$ two-level emitters undergoing collective decay at rate $Γ$ and collective incoherent pumping at rate $R$, confined to the fully symmetric Dicke ladder. Although the population dynamics are confined to a finite set of rate equations, their quantum-trajectory representation involves infinitely many pump-decay histories. We derive an exact finite continued fraction for the Laplace-transformed Dicke-state populations by resumming the infinitely many quantu...
  </details>

- **2026-10-27** — Athanasios Glentis, Dawei Li, Mingyi Hong — [MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control](http://arxiv.org/abs/2610.37647v1)
  <details><summary>📄 Abstract</summary>
  Weight decay and explicit weight-norm constraints improve optimizer performance in language model pretraining, yet a unified understanding of why such control helps and how much is needed remains incomplete. We analyze norm control in Muon over the entire training trajectory using the \emph{accumulated effective learning rate}, $C_T=\sum_{t<T}η_t/\|W_t\|_F$, where $η_t$ is the nominal learning rate and $η_t/\|W_t\|_F$ is the effective learning rate relative to the weight norm. For bounded update...
  </details>

- **2026-10-27** — Nesta Midavaine, Floris Fok, Paulo Mendes et al. — [LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation](http://arxiv.org/abs/2610.37570v1)
  <details><summary>📄 Abstract</summary>
  We present LCM-Promo, an LLM-based uplift model for promotion allocation. LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response. It learns monotonic promotion-response curves from production logs by interpreting single-token outputs as conversion-threshold probabilities, while conditioning on session context such as day and delivery shift. In a production A/B test on churn reactivation, LCM-Pr...
  </details>

- **2026-10-27** — Peize Ding — [Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives Policy Collapse in Unsupervised RLVR](http://arxiv.org/abs/2610.37553v1)
  <details><summary>📄 Abstract</summary>
  Label-free reinforcement learning with verifiable rewards (RLVR) rewards a language model for agreeing with its own majority vote. It improves reasoning at first but eventually collapses: the self-assessed reward goes to one while accuracy falls, often until the model gives the same answer to every problem. The collapse appears only when training uses many problems. We explain this dataset-size dependence as a collective instability. In a solvable many-problem model in which problems share param...
  </details>

- **2026-10-27** — Remy Ogasawara, Cullen Anderson, Narmeen Fatimah Oozeer et al. — [Orthogonal and Parametrized Multi-Attribute Steering of LLMs](http://arxiv.org/abs/2610.37517v1)
  <details><summary>📄 Abstract</summary>
  Activation steering offers an effective and efficient way to modify an LLM's behavior at inference time. However, it remains unclear how to apply steering such that the signal is consistently strong and the steering strength has a universally interpretable meaning. We address this first by identifying the most steerable interval for each steering vector and rescaling the steering range accordingly. Building on this, we introduce a more interpretable method for steering, called parameterized stee...
  </details>

- **2026-10-27** — Devon Yanitski, Chris Westbury — [semanticfa: An R Package for Response-Free Semantic Factor Analysis of Psychometric Scales](http://arxiv.org/abs/2610.37494v1)
  <details><summary>📄 Abstract</summary>
  The items of a reflective psychometric scale can be read as a proposal about a construct's structure. Language models make that proposal measurable by converting each item into an embedding, a list of numbers, similar for similar meanings. We introduce semanticfa, an R package for semantic factor analysis, which factors item-embedding similarities. It also interprets factors, flags redundant items, builds short forms, and screens new items. A worked example analyzes the 50-item International Per...
  </details>

- **2026-10-27** — Milad Sikaroudi — [Concordat: Typed Sessions for LLM Agents](http://arxiv.org/abs/2610.37461v1)
  <details><summary>📄 Abstract</summary>
  Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually stated in the prompt and followed only as reliably as the model chooses to follow them. We present Concordat, a Python library that treats an agent as an object whose interface is a finite-state protocol, in the spirit o...
  </details>

- **2026-10-27** — Yonghao Yu, Lang Huang, Runyi Li et al. — [Vision-Language-Action or World-Action? Just Action Models](http://arxiv.org/abs/2610.37219v1)
  <details><summary>📄 Abstract</summary>
  The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a WAM therefore cannot simply be attributed to any one of them. We show that decoupli...
  </details>

- **2026-10-27** — Weichang Wang, Liyu Chen, Shuyue Guan et al. — [VGIQA: Fine-Grained Image Quality Assessment with Visual Grounding Rewards](http://arxiv.org/abs/2610.37186v1)
  <details><summary>📄 Abstract</summary>
  Image quality assessment (IQA) aims to evaluate the perceptual visual quality of images. Recently, the rapid development of Multi-modal Large Language Models (MLLMs) has significantly advanced the IQA field. By integrating chain-of-thought (CoT) reasoning and reinforcement learning (RL), these models can generate more accurate and interpretable results while relying on less training data. However, existing MLLM-based methods are predominantly constrained to holistic, image-level evaluations and ...
  </details>

- **2026-10-27** — Dipanjyoti Paul, Arpita Chowdhury, Maneet Chatterjee et al. — [INTR++: INterpretable TRansformer with better Accuracy, Interpretability, and Adaptability](http://arxiv.org/abs/2610.37178v1)
  <details><summary>📄 Abstract</summary>
  Interpretable Transformers often perform well in domain specific settings but lose effectiveness beyond that. Achieving ViT-like broad applicability requires models with consistent performance across domains. Recent works on Interpretable Transformers, INTR and Prompt-CAM, were developed keeping domain adaptability in mind. Prompt-CAM leverages learnable prompts to promote adaptability. However, these prompts are fixed in nature and therefore struggle to adapt to domains with substantial variati...
  </details>

- **2026-10-27** — Abdulhaq Adetunji Salako, Christian Tominski — [Science-Fiction Transformation as a Design Lens for Visualization Transformation](http://arxiv.org/abs/2610.37131v1)
  <details><summary>📄 Abstract</summary>
  Science fiction often features characters or objects that undergo radical changes in form while still being recognizable as the same entity. For example, a vehicle might unfold into a robot, or one body might flow or shape-shift into another. We use such transformations as a reflective lens to study similar shape-shifting in visualization, where one visual representation transforms into a completely different one. For example, a node-link diagram might transform into a parallel coordinates plot ...
  </details>

- **2026-10-27** — Sahar Nasirihaghighi, Tianyuan Wang, Kenan Niu et al. — [MCP-Net: Real-Time Coronary Perception Network and Topological Analysis for Robotic Guidewire Navigation](http://arxiv.org/abs/2610.37127v1)
  <details><summary>📄 Abstract</summary>
  Coronary guidewire navigation during percutaneous coronary intervention requires continuous interpretation of vessel anatomy, guidewire position, and target stenosis under two-dimensional X-ray fluoroscopy. While existing approaches commonly address vessel segmentation or device localization as separate tasks, a robotic system requires a more structured perception of the coronary scene to support downstream navigation. In this work, we present a simulation-driven framework centered on a Multi-Ta...
  </details>

- **2026-10-27** — Djardiel S. Gomes, Isaac M. Félix, Marcelo L. Pereira Junior — [First-Principles Investigation of Irida-Graphane: A Wide-Band-Gap Semiconductor Derived from Irida-Graphene](http://arxiv.org/abs/2610.37095v1)
  <details><summary>📄 Abstract</summary>
  Opening a band gap in metallic two-dimensional carbon allotropes is an important step toward their use in electronic and optoelectronic devices, and full hydrogenation has proven to be an effective route to achieve it. Here, we propose irida-graphane, the fully hydrogenated derivative of the irida-graphene, a monolayer composed of three-, six-, and eight-membered rings, and investigate its structural, mechanical, electronic, and optical properties using density functional theory (DFT) at the PBE...
  </details>

- **2026-10-27** — Humza Nusrat, Kundan Thind — [OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](http://arxiv.org/abs/2610.37081v1)
  <details><summary>📄 Abstract</summary>
  Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and methods: OpenGray adds tasks with known answers to the OpenKBP-Opt head-and-neck dataset, including two contradictions with dose goals proven incompatible and a feasible control with a stored plan meeting every hard goal. F...
  </details>

- **2026-10-27** — Adrian Schmidt, Oya Ok, Deniz İpek Zeynioğlu et al. — [Mapping Artistic Engagement with Quantum Technologies](http://arxiv.org/abs/2610.37054v1)
  <details><summary>📄 Abstract</summary>
  Quantum technologies (QT) are increasingly being taken up in artistic practices, for example in the form of visual artworks or quantum computer music. However, more comprehensive empirical studies on the temporal development and the different forms of QT-related art are still lacking. Therefore, this study conducted a systematic mapping and classification of QT-related artworks. To this end, a medium-independent corpus was established, and the artworks were classified into four categories: QT-In...
  </details>

- **2026-10-27** — Sami Alnawali, Muhammad Atif Saeed, Abdul Hadi et al. — [Interpretable Deep Learning Models for Breast Cancer Diagnosis Using Medical Imaging](http://arxiv.org/abs/2610.37026v1)
  <details><summary>📄 Abstract</summary>
  Deep learning shows promise for breast cancer diagnosis, but limited interpretability hinders clinical adoption. We benchmark ten ImageNet-pretrained models (ResNet50, VGG19, InceptionV3, DenseNet121, Xception, MobileNetV2, EfficientNet, ConvNeXt, ViT, and Swin Transformer) for benign-versus-malignant classification on the BreakHis histopathology dataset using a patient-level split, and explain their predictions with Grad-CAM, LIME, Integrated Gradients, and LRP. DenseNet121 performed best, with...
  </details>

- **2026-10-27** — Ryoya Yoshiyama, Bowen Wang, Yuta Nakashima — [Drop the Details, Get the Gist: Dynamic Conceptual Representation for Video Recognition](http://arxiv.org/abs/2610.36832v1)
  <details><summary>📄 Abstract</summary>
  Concept Bottleneck Models (CBMs), which route predictions through a layer of human-interpretable concepts, have substantially improved the interpretability of visual classification by exposing an explicit, language-based rationale for each prediction. Most existing work focuses on static images, and temporal dynamics in videos have been underexplored in conceptual representation. We propose a framework that extends concept-based image recognition to procedural video understanding. It represents ...
  </details>

- **2026-10-27** — Yue Wu, Yang Zhang, Weinan Gan et al. — [Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training](http://arxiv.org/abs/2610.36794v1)
  <details><summary>📄 Abstract</summary>
  Test-time training (TTT) enables a deployed language model to internalize incoming context on-the-fly into a small set of fast-weight parameters, rather than merely treating it as transient context for attention. In-Place TTT recently made this idea practical for large language models by repurposing the down-projection of standard MLP blocks as fast weights. However, we find that its benefit largely disappears on realistic web long-context question answering. We attribute this to In-Place TTT's ...
  </details>

- **2026-10-27** — Jialin Zhang, Lakshya A Agrawal, Shangyin Tan et al. — [Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](http://arxiv.org/abs/2610.36774v1)
  <details><summary>📄 Abstract</summary>
  Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on each optimization step instead of one candidate at a time. In our sweep on two tasks, most batched runs finished in half the wall-clock time or less, and the fastest in about a quarter to a third. Batched settings also ...
  </details>

- **2026-10-27** — Ziluowen Luo, Ruochen Liu, Jun Yin et al. — [The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation](http://arxiv.org/abs/2610.36763v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation (GR) predicts the next item through its semantic ID (SID). Existing methods commonly fit SID vocabularies to pretrained language model (PLM) representations of item descriptions, incurring additional training costs and making vocabulary coverage dependent on the fitting domains. We observe that pretrained sparse autoencoders expose PLM features with human-interpretable semantic annotations, allowing feature indices to serve as a reusable SID vocabulary. However, reusing...
  </details>

- **2026-10-27** — Yucong Zhang, Cancan Li, Bo Xiao et al. — [From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents](http://arxiv.org/abs/2610.36713v1)
  <details><summary>📄 Abstract</summary>
  Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories. We argue that voiceprints are observations of identity, not identities themselves, and formulate online speaker-memory construction to maintain persistent user entities as acoustic evidence evolves. We introduce EvoSpeakerMem, a training-free layer for causal speaker routing, selective acoustic-state updates, and identity-partitioned memo...
  </details>

- **2026-10-27** — Pragna Mallappa — [Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning Traces](http://arxiv.org/abs/2610.36709v1)
  <details><summary>📄 Abstract</summary>
  Reasoning language models answer math problems by writing long chains of thought, and sampling many chains per problem and taking a majority vote raises accuracy at a large cost in generated text. A popular way to cut that cost scores each chain by the model's confidence in each token it writes, where a token is a word or part of a word. The method averages this confidence over a sliding window of 2048 tokens and keeps or stops chains based on the lowest average. We treat the confidence, recorde...
  </details>

- **2026-10-27** — Satomu Tomisaki, Yosuke Mikami, Amane Watahiki et al. — [Japanese Discourse Structure Analysis Based on Segmented Discourse Representation Theory Using LLMs](http://arxiv.org/abs/2610.36667v1)
  <details><summary>📄 Abstract</summary>
  Discourse parsing based on Segmented Discourse Representation Theory (SDRT) is crucial for capturing the structural dynamics of dialogues. However, most prior research focuses on English, and its effectiveness for Japanese remains unclear owing to the lack of Japanese SDRT corpora. To address this issue, we construct Japanese SDRT corpora by translating existing English SDRT corpora using an LLM. Through a comparative evaluation of prompt-based and fine-tuned LLMs, we show that the models achiev...
  </details>

- **2026-10-27** — Shuo Yan, Ningning Hou, Haoyu He et al. — [The View from Nowhere: Population-Centered Agent Evolution](http://arxiv.org/abs/2610.36660v1)
  <details><summary>📄 Abstract</summary>
  Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between population coverage (i.e., the tasks solved by at least one evolved variant) and the performance of the best individual agent. This gap shows that useful capabilities and diagnostic evidence emerge across the population without...
  </details>

- **2026-10-27** — Chengxuan Pei, Ziyao Wang, Teng Mei et al. — [Learning to Formalize: Bridging Open-Ended Workloads and Fast Decision Models](http://arxiv.org/abs/2610.36595v1)
  <details><summary>📄 Abstract</summary>
  Decision models offer fast choices over sup- plied alternatives, while general-purpose large language models interpret open-ended tasks through flexible generation and reasoning at the cost of sequential decoding. Many work- loads expect a generative backend to determine what can be done and therefore provide no well-defined candidate list. We bridge this in- terface gap with a small candidate formalizer trained on offline teacher-generated lists. The formalizer constructs explicit, validated al...
  </details>

- **2026-10-27** — Swapnil Bhosale, Prem Seetharaman, Ke Chen et al. — [TAC2: Timestamped Audio Captioning as composable functions](http://arxiv.org/abs/2610.36568v1)
  <details><summary>📄 Abstract</summary>
  Real-world audio applications require precise, queryable representations grounded in physical time. Yet modern Large Audio-Language Models (LALMs) increasingly favor conversational generation, producing free-form descriptions that conflate acoustic perception with higher-level reasoning and lack precise temporal grounding. We introduce TAC2, a foundation model that casts timestamped audio captioning as composable functions to construct granular, speaker-attributed acoustic timelines directly fro...
  </details>

- **2026-10-27** — Miri Liu, Xiayu Zhao, Encheng Xie et al. — [Do AI Scientists Know What's New?](http://arxiv.org/abs/2610.36511v1)
  <details><summary>📄 Abstract</summary>
  A major challenge facing AI scientific discovery pipelines is how to determine when a generated idea is meaningfully novel. Ideally, novelty checks in these pipelines must be able to reject non-novel ideas while not rejecting too many novel ideas, and they should also be able to distinguish which parts of a proposal are non-novel, as opposed to opaquely discarding entire proposals. We design an analytical framework for evaluation of novelty checks with temporal ground truth at both the proposal-...
  </details>

- **2026-10-27** — Kianté Fernandez, Caitlin Chen, Jialu Zhou et al. — [CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](http://arxiv.org/abs/2610.36484v1)
  <details><summary>📄 Abstract</summary>
  Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We introduce CogArena, ...
  </details>

- **2026-10-27** — Arther Tian, Alex Ding, Simon Wu et al. — [FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](http://arxiv.org/abs/2610.36476v1)
  <details><summary>📄 Abstract</summary>
  Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the audit of sequential agent traces. The protocol separates structured decision validity, optional numerical commitment adherence, execution and ledger reconciliation, and receipt- grounded reporting, with explicit coverag...
  </details>

- **2026-10-27** — Alexa R. Tartaglini, Zhengxuan Wu, Thaddäus Wiedemer et al. — [A Heart Means Recursion: Exploring Visual Meaning and Communication in VLMs](http://arxiv.org/abs/2610.36449v1)
  <details><summary>📄 Abstract</summary>
  Do vision-language models (VLMs) share our ability to communicate visually? We share preliminary findings, starting from a surprising observation: simple visual symbols like a red heart can strongly influence model behavior on seemingly unrelated tasks, such as steering models towards recursive solutions on simple coding problems. Notably, this steering effect is largely implicit, as models' direct interpretations and thinking traces about visual symbols diverge substantially from their observed...
  </details>

- **2026-10-27** — Luis Hasenauer, Arkaprava Roy, Leo Duan — [Mirror Likelihood for Modeling Manifold Data with Application on Correlation Time Series](http://arxiv.org/abs/2610.36448v1)
  <details><summary>📄 Abstract</summary>
  Manifold-valued data arise in a wide range of scientific applications. Existing statistical methods typically follow either an intrinsic approach, which characterizes the manifold itself via quantities such as geodesic distance or the Fréchet mean, or an extrinsic approach, which embeds the manifold into an ambient Euclidean space, performs unconstrained statistical estimation, and projects the result back to the manifold. While the latter is conceptually and computationally simple, likelihood-b...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 702 |
| prompt-injection | 647 |
| memory-poisoning | 56 |
| tool-use-attack | 168 |
| backdoor | 545 |
| adversarial-attack | 657 |
| privacy-leakage | 4494 |
| steganography | 89 |
| misuse | 1271 |
| red-teaming | 145 |
| vulnerability | 3820 |
| defense | 3708 |
| alignment | 3479 |
| robustness | 3778 |
| watermark | 685 |
| unlearning | 119 |
| agent-safety | 66 |
| benchmark | 72 |
| survey | 432 |
| other | 10227 |

---

📚 **全部 35160 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-30 21:53:18*