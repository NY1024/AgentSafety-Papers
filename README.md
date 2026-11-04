<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-35751-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-04 13:39 ｜ **论文总数 / Total Papers**: 35751（近 30 天 / Recent 30 days: 4596）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 35751 篇论文（含摘要、分类筛选、搜索）/ View all 35751 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 710
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 660
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 57
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 171
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 548
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 663
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4525
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 90
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1285
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 146
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3876
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3766
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3536
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3847
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 704
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 119
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 66
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 73
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 438
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10471

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4596 篇，完整 35751 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4596 papers from the last 30 days (with date, authors & abstract). For the full list of 35751 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-11-03** — Chuancheng Shi, Shangze Li, Wenhua Wu et al. — [TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport](http://arxiv.org/abs/2611.04878v1)
  <details><summary>📄 Abstract</summary>
  Despite their remarkable capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current safety intervention methods primarily rely on the \textit{locality hypothesis}, rigidly suppressing isolated neurons or features. However, harmful semantics manifest as distributed, cross-layer circuits, rendering localized ablations both brittle against complex jailbreaks and detrimental to general utility. To bridge this gap, we propose TraceRouter++, a routing-level sa...
  </details>

- **2026-11-03** — Masoud Poorghaffar Aghdam, Göktuğ Serdar Yıldırım, Sinem Sav — [BrainwashedLLM: Jailbreaking via Automated Adversarial Chain of Thoughts Discovery](http://arxiv.org/abs/2611.04717v1)
  <details><summary>📄 Abstract</summary>
  Large Reasoning Models (LRMs) achieve strong performance on complex tasks by generating explicit Chain-of-Thought (CoT) reasoning, but the safety implications of this intermediate reasoning surface remain underexplored. We demonstrate that the reasoning trace itself is a powerful attack vector. Safety alignment in large models is substantially less robust to malicious reasoning embedded in the context than to direct imperative prompts. We introduce BrainwashedLLM, a weak-to-strong adversarial fr...
  </details>

- **2026-11-03** — Gia Phong Tran, Thai Duong Huynh, Randolph Loh et al. — [From Guidelines to Practice: Defining Requirements for AI Red-Teaming Tools](http://arxiv.org/abs/2611.04271v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) has seen significant developments and increased usage in recent years. AI benefits various tasks, automates decision-making, and enhances efficiency. However, AI also introduces additional attack surfaces for threat actors to perform attacks like prompt injection and jailbreaking, making security a great concern. AI security testing aims to imitate adversarial attacks or malicious inputs via manual testing or with the assistance of tools. Thus, it is critical that or...
  </details>

- **2026-11-02** — Yang Qu, Qiang Fu, Zonghao Ying et al. — [VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions](http://arxiv.org/abs/2611.03765v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents are increasingly deployed in open-world environments, yet current robustness evaluations remain biased toward hazardous instructions and jailbreak vulnerabilities. A more fundamental issue is largely overlooked: agents are rarely tested under semantically sufficient but contextually minimal instructions (i.e., common in real-world human communication), where auxiliary contextual cues are absent. For the first, we identify a novel phenomenon termed Ambient Context Illusion, where ...
  </details>

- **2026-11-02** — Junyu Lin, Mengjie Wu, Yonghao Dong et al. — [PGuard: A Native, Streaming, and Plug-in Guardrail for Multimodal Large Language Models](http://arxiv.org/abs/2611.02791v2)
  <details><summary>📄 Abstract</summary>
  As streaming generation becomes the dominant serving paradigm for both text-only and multimodal large language models, ensuring safety throughout the generation process has become a critical challenge. We introduce PGuard, a native, streaming, and plug-in guardrail that transforms safety monitoring from an external serving dependency into an integrated capability of the backbone model. PGuard directly leverages the backbone's intermediate representations for token-level safety detection, without...
  </details>

- **2026-11-02** — Wei-Lin Chen, Zhepei Wei, Xinyu Zhu et al. — [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](http://arxiv.org/abs/2611.03575v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated files, weakening access controls, or corrupting data, in response to benign inputs without explicit jailbreaking. This failure mode is particularly important because apparent task success may reassure users that an agent...
  </details>

- **2026-11-02** — Junyu Lin, Mengjie Wu, Yonghao Dong et al. — [PGuard: A Native, Streaming, and Plug-in Guardrail for Multimodal Large Language Models](http://arxiv.org/abs/2611.02791v1)
  <details><summary>📄 Abstract</summary>
  As streaming generation becomes the dominant serving paradigm for both text-only and multimodal large language models, ensuring safety throughout the generation process has become a critical challenge. We introduce PGuard, a native, streaming, and plug-in guardrail that transforms safety monitoring from an external serving dependency into an integrated capability of the backbone model. PGuard directly leverages the backbone's intermediate representations for token-level safety detection, without...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 12 papers

- **2026-11-03** — Yutao Wu, Xiao Liu, Ming Wen et al. — [ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud](http://arxiv.org/abs/2611.04879v1)
  <details><summary>📄 Abstract</summary>
  Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter online fraud designed to deceive humans, including fraudulent online stores, fake investment platforms, and advance-fee schemes. How web agents respond to such fraud during task execution remains underexplored, in part becau...
  </details>

- **2026-11-03** — Yao Wang, Zehua Ma, Weiming Zhang et al. — [Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning](http://arxiv.org/abs/2611.04673v1)
  <details><summary>📄 Abstract</summary>
  Indirect Prompt Injection (IPI) poses a critical threat to LLM agents. Existing defenses largely focus on whether an injection induces a new tool invocation or unintended action. In this paper, we study a different attack surface, parameter poisoning, where the attacker preserves the intended action but manipulates one or more tool arguments, such as a recipient or other task-critical value. Such attacks are difficult to detect because no new action is introduced, while parameter changes themsel...
  </details>

- **2026-11-03** — Ilan Zendel, Matan Levy, Stav Cohen et al. — [Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents](http://arxiv.org/abs/2611.04393v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly act on information retrieved from public sources they treat as credible, which turns a manipulated recommendation into a transaction, a dependency, or a decision with physical consequences. The security literature models this threat as instruction injection, in which an adversary writes a command into retrieved content and deployed defenses learn to recognize command syntax. We show that an attacker can instead steer an agent through the agent's own harm-avoidance. A sing...
  </details>

- **2026-11-02** — Xu Zhang, Zhichao Lu — [ATrust: Adaptive Trust Boundary Expansion for Securing LLM Agents](http://arxiv.org/abs/2611.02741v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents take on more complex tasks with greater autonomy, security has become a major obstacle to their broader deployment. Unlike in attacks that require complex exploitation of operating system vulnerabilities, attackers can easily hijack agents through indirect prompt injection (IPI), leading to privacy leakage, financial loss, and destructive operations. However, existing defenses often make security decisions based on limited static trusted evidence or assess ob...
  </details>

- **2026-11-02** — Kainan Zhou, Gangzhen Qian, Janet Sung et al. — [SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search](http://arxiv.org/abs/2611.02643v1)
  <details><summary>📄 Abstract</summary>
  An indirect prompt injection can affect a search-augmented large language model only after its carrier page reaches model context. SearchInject controls this admission decision with a joint score combining retrieval relevance, search-abuse cues, instruction likelihood, and two relevance interactions. A quarantine threshold is selected under an empirical 0.5% clean-candidate false-quarantine constraint on a calibration split. Evaluation uses 300 held-out SciFact queries and held-out payload categ...
  </details>

- **2026-11-02** — Christopher Krakauer, Andreas Schaad — [Where Does MCP Security End? A Three-Tier Mitigation Mapping Framework for the OWASP MCP Top 10](http://arxiv.org/abs/2611.02611v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) has become a leading standard for connecting Large Language Models (LLMs) to external tools, software, and data sources. MCP architecture favors ease of integration over security, blending the data and control planes into a single natural language channel. This introduces confused deputy and prompt injection vulnerabilities that cannot be completely mitigated in the software development lifecycle (SDLC) of an MCP server. Structured security guidance for server de...
  </details>

- **2026-11-02** — Haowen Dai, Alejandro Guerra-Manzanares — [StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents](http://arxiv.org/abs/2611.02605v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through alert triage, incident summarization, response recommendation, and Indicator of Compromise (IOC) extraction as locally plausible intermediate decisions. We characterize this failure mode as evidence-chain contamination of protected task state...
  </details>

- **2026-11-02** — Junwei Yao, Jianan Liu, Yongxi Zhou et al. — [Ranked but Not Stopped: Detecting Prompt-Injection Hijacks from Typed Decision Models' Output Probabilities](http://arxiv.org/abs/2611.02522v1)
  <details><summary>📄 Abstract</summary>
  Programs that use a language model as a classifier act on its most probable label. Text injected into the input can move that label to one the attacker chooses, a hijack. A monitor that does not know the attacker's label can read the model's own confidence and raise an alarm when the top probability is low. We test this monitor on AG News topic classification with five systems, three of them served through a provider's API. Pooled over five families of injected text, low confidence ranks hijacke...
  </details>

- **2026-11-02** — Javad Mohammad Alizadeh, Huanmei Wu — [Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets](http://arxiv.org/abs/2611.02484v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly built into data-analysis software, yet little evidence shows how reliably they preprocess clinical data or whether the tools they invoke give correct, reproducible output. We report a benchmark of THReD, a web-based system that turns electronic health record (EHR) extracts into AI-ready datasets through a chat agent whose proposed steps run only after user confirmation. The agent benchmark has 141 tasks (100 templates) in seven categories, including goal-level request...
  </details>

- **2026-11-02** — Sreehari Sankar, Debargha Ganguly, Vikash Singh et al. — [LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents](http://arxiv.org/abs/2611.02332v1)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies combine state predicates with scoped past-time temporal operators over the execution history, evaluation is fail-closed, and the decision procedure is proved equivalent to a LeanLTL semantics. A denied call can be corrected in two ways. With feedback, the a...
  </details>

- **2026-11-01** — Shiyu Kan, Yue Qi, Yufei Han et al. — [Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security](http://arxiv.org/abs/2611.01976v1)
  <details><summary>📄 Abstract</summary>
  Large language model based agents increasingly rely on external tools to invoke services and interact with web resources. These tools can evolve through software updates, yet agentic frameworks may continue trusting them without re-verifying their safety after implementation changes. This tool update gap creates a supply-chain vulnerability in agentic systems: because updated tool code executes outside the LLM's context window, malicious functionality embedded in tool updates can bypass defenses...
  </details>

- **2026-11-01** — Zhihua Wang, Yunhao Feng, Yifeng Gao et al. — [MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents](http://arxiv.org/abs/2611.01700v1)
  <details><summary>📄 Abstract</summary>
  AI agents often rely on persistent memory to retain user preferences and operational rules across sessions. However, this capability introduces a new safety risk: malicious instructions from messages, documents, or Web content can be retained in memory and influence future tasks even after the original attack content is removed. Existing attack success metrics, however, fail to capture who is affected and how attacks translate into downstream harm during otherwise normal task execution. We intro...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-11-02** — Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel et al. — [IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning](http://arxiv.org/abs/2611.03431v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies that exceed trusted authorization requirements. We present IAMRAGBENCH, a 60-case benchmark spanning scope, conditions, explicit denies, trust, permissions boundaries, and role delegation. It combines deterministic authorization-envelope sc...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-11-03** — Jinjun Huang, Jialun Cao, Junxiao Han et al. — [How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub](http://arxiv.org/abs/2611.04456v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based agents increasingly rely on external skills to reuse task-specific knowledge without retraining the model. As skills become common for extending agent capabilities, understanding creation and evolution is critical for reliable agent systems. However, existing studies mainly examine agent skills from a static perspective, leaving their evolution in real-world repositories largely unexplored. This limits our understanding of the patterns and motivations behind skill chan...
  </details>

- **2026-11-02** — Kuiyi Gao, Xue Liu, Bowei He — [RuntimeTickets: Source-Grounded Security Obligations for Agent Skills](http://arxiv.org/abs/2611.03772v1)
  <details><summary>📄 Abstract</summary>
  Third-party Agent Skills extend what an autonomous agent can do, but a malicious Skill can hide data exposure or output manipulation inside a legitimate workflow. Neither reading a Skill's description nor granting it tool permissions tells whether its execution meets the user's security requirements. We introduce RuntimeTickets, a protocol that enforces and audits these requirements while a Skill runs. From released malicious-Skill datasets we derive a risk model and build adversarial-benign Ski...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 2 papers

- **2026-11-02** — Farooq Shaikh, Biagio Montaruli — [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](http://arxiv.org/abs/2611.03555v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions without confirming real execution. We present the first cross-framework measurement of MCP tool poisoning with real tool execution. A 25-class root-cause taxonomy unifies prior classi...
  </details>

- **2026-11-01** — Bicheng Xiong, Tao Li, Chenhui Cui et al. — [GDBack: A Group-Delay Backdoor Attack on Speaker Identification via Analytic All-Pass Filtering](http://arxiv.org/abs/2611.01721v1)
  <details><summary>📄 Abstract</summary>
  Existing phase-based backdoor attacks on speaker identification rely on shared absolute phase patterns for cross-sample trigger consistency, while other audio backdoor attacks have explored shared transformations that produce input-dependent triggers. Whether phase-based triggers can achieve similar consistency without imposing identical output phase patterns remains unclear. We propose GDBack, a poison-only group-delay backdoor attack using cascaded second-order analytic all-pass filters. Apply...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 5 papers

- **2026-11-03** — Mostafa Kira, Bader Rasheed, Manuel Mazzara — [Anchored Rank-Adversarial Fine-Tuning Pretrained Visual Place Recognition Models](http://arxiv.org/abs/2611.05286v1)
  <details><summary>📄 Abstract</summary>
  Visual place recognition (VPR) localises a camera by retrieving similar geo-tagged images, and current foundation-model VPR models are accurate across cities, seasons and illumination, but not robust to adversarial perturbations: under a white-box attack on the ranking at an imperceptible budget of 1/255, SuperVLAD and BoQ keep at most 0.2% top-1 recall (R@1) on four benchmarks. We propose anchored rank-adversarial fine-tuning (ARAFT), which fine-tunes a released model with a listwise rank loss ...
  </details>

- **2026-11-03** — Jiayan Cui, Davide Salvi, Paolo Bestagini et al. — [Detector-Guided Vocoder Training for Adversarial Text-to-Speech Synthesis](http://arxiv.org/abs/2611.04511v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose a novel Text-to-Speech (TTS) framework designed to perform adversarial attacks against speech deepfake detection systems. Given a TTS model and a detector capable of classifying its outputs as synthetic, our approach fine-tunes the vocoder by integrating the detector into the TTS training loop. Unlike traditional adversarial methods that rely on post-hoc perturbations or external noise injection, our approach enables the generation of synthetic speech that is intrinsica...
  </details>

- **2026-11-02** — Geyuan Wang, Shunyu Liu, Siyuan Liang et al. — [The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents](http://arxiv.org/abs/2611.03754v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have shown promise for empowering search agents to tackle complex information-seeking tasks. However, since acquiring external information necessitates web search, these agents are highly susceptible to various adversarial attacks (e.g., malicious information injection or stealthy context manipulation). Existing attack strategies inevitably rely on static and human-crafted templates, failing to emulate the dynamic and complex nature of real-world threats. In this pap...
  </details>

- **2026-11-02** — Xulin Chen, Ruipeng Liu, Garrett E. Katz — [Beyond $L_\infty$-Norm Sets: Synthesizing Interpretable Non-Uniform Uncertainty Sets for Evaluation-Time State-Adversarial Robustness](http://arxiv.org/abs/2611.02576v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) agents are vulnerable to perturbations of their observed state inputs. Prior works often constrain state adversaries with $L_p$-norm uncertainty sets and evaluate policy performance under the resulting perturbations. However, in continuous control tasks like robotics control, different state dimensions have distinct physical meanings and influence policy behavior to different degrees, which $L_p$-norm sets fail to capture or explain. Moreover, it is important to...
  </details>

- **2026-11-02** — Zewei Shi, Ruoxi Sun, Minhui Xue et al. — [Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting](http://arxiv.org/abs/2611.02310v1)
  <details><summary>📄 Abstract</summary>
  Accurate electricity-demand forecasting is essential for the modern energy infrastructure. Recently, Times-Series Large Language Models (TS-LLMs) have emerged as a promising approach to forecasting more accurate demand from historical consumption data in zero- and few-shot settings, helping energy operators effectively plan supply and allocate energy resources. However, these models are vulnerable to compromised sensor inputs that can distort forecasts and lead to erroneous market orders or unne...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-11-03** — Tuan Thanh Duong, Joongmin Shin, Jeongho Yoon et al. — [Residual Attribute Leakage Is an Interface: Auditing Privacy Evaluation After Text De-identification](http://arxiv.org/abs/2611.04941v1)
  <details><summary>📄 Abstract</summary>
  A privacy evaluation of de-identified text asks a language model (the adversary) to guess a person's protected attribute. We introduce a prior-normalised clipped leakage score of its confidence gain on the true value and audit the conclusions drawn from it. Each verdict depends on an evaluation interface (the queried person, answer options, prior, adversary model and scoring rule), which we vary on fixed releases of three corpora. In a stress test, an editor that writes the opposite-sex form at ...
  </details>

- **2026-11-03** — Chenyu Yi, Jiawen Zong, Sami Hormi et al. — [The Pen is Mightier than the Pixel: Natural Textual Unlearnable Example for Large Vision Language Models](http://arxiv.org/abs/2611.04817v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of Large Vision Language Models (LVLMs), trained on vast and often sensitive datasets, raised concerns regarding data privacy and unauthorized usage. Unlearnable Examples (UEs), which subtly perturb training data to mislead the models, have emerged as a promising defense method. This paper presents the first exploration of UEs specifically on LVLMs, which poses unique challenges due to their inherent multimodal nature. We propose a novel text-based perturbation method, Natural ...
  </details>

- **2026-11-03** — Shuaidong Li, Chenhao Lin, Xinshan Yang et al. — [Extracting System Prompt of LLM Services in Complex (Agentic) Settings: Hierarchical Optimization and Reliable Evaluation Metrics](http://arxiv.org/abs/2611.04803v1)
  <details><summary>📄 Abstract</summary>
  System prompt is a critical intellectual property of large language model (LLM) services. To analyze its leakage, prompt extraction attacks have been extensively studied. However, we validate that existing attacks substantially degrade on recent LLM services, whose complexity has evolved in both the prompt itself and system-level constraints. Specifically, (1) system prompts become longer and more structured to contain pre-defined tool schemas, execution logic, safety guardrails, etc., and (2) o...
  </details>

- **2026-11-03** — Alexandre G. Leclercq, Sébastien Bougleux, Aurélien Corroyer-Dulmont et al. — [Federated Transfer Learning for Medical Image Classification under Mixed Skew](http://arxiv.org/abs/2611.05035v1)
  <details><summary>📄 Abstract</summary>
  Deep learning in medical imaging is constrained by data scarcity and by privacy regulations that make centralizing patient data across institutions impractical. Federated Learning (FL) addresses these constraints by keeping data local, but its distributed nature exposes training to strong statistical heterogeneity. Multicentric medical data is particularly affected, exhibiting a mixed skew that combines feature, label, concept, and quantity shifts across centers. Personalized FL mitigates hetero...
  </details>

- **2026-11-03** — Qiao Li, Jing Chen, Cong Wu et al. — [ProAlign: Progressive Positional and Prototype-Guided Alignment for Aerial-Ground Person Re-Identification](http://arxiv.org/abs/2611.04980v1)
  <details><summary>📄 Abstract</summary>
  Aerial-Ground Person Re-Identification (AG-ReID) aims to match pedestrian images captured by unmanned aerial vehicles (UAVs) and ground-based surveillance cameras. The task remains highly challenging due to severe viewpoint discrepancies, frequent occlusions, and substantial domain gaps between aerial and ground imagery. Beyond these observable factors, existing methods often overlook two fundamental structural issues: cumulative positional drift during hierarchical feature extraction and semant...
  </details>

- **2026-11-03** — Chaerin Lee, Wonho Lee, Sohee Park et al. — [Reducing Logprob Without Causal Verification: Diagnosing SAE-Based PII Suppression in LLMs](http://arxiv.org/abs/2611.04782v1)
  <details><summary>📄 Abstract</summary>
  SAE-based feature-level interventions to suppress PII leakage in LLMs are primarily evaluated by log-probability reduction. We show that this criterion cannot distinguish feature specific suppression from a magnitude artifact: a direction-agnostic effect of sufficiently large activation perturbations. Across 36 (model, layer, PII type) cases, we compare selected SAE feature interventions with coherencematched random direction controls using logprob and rank-aware metrics. While 17 cases (47%) ap...
  </details>

- **2026-11-03** — Zhiyu Wang, Rajkumar Buyya — [EvoCache: Accelerating Browser Large Language Model Delivery with Public Cache Anchors](http://arxiv.org/abs/2611.04638v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can run directly in a browser, but first use typically requires downloading model files that are hundreds of MiB or even several GiB in size. The same LLM is often repackaged by different publishers; these files share substantial content, yet byte differences prevent whole-file caches from reusing them. We propose EvoCache, a browser-managed LLM delivery system. EvoCache uses public cache anchors that are stored in advance by the browser and independent of browsing h...
  </details>

- **2026-11-03** — Maisha Maliha, Vishal Pramanik, Sumit Kumar Jha — [ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems](http://arxiv.org/abs/2611.04321v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a locally reasonable message that exercises authority belonging to another role: a verifier that begins planning, a retriever that asserts unsupported conclusions, an executor that change...
  </details>

- **2026-11-03** — Muhammad Usama, Muhammad Saad Qadir — [Where Did the Update Go? Certifying Declared Change Envelopes for Model Updates](http://arxiv.org/abs/2611.04192v1)
  <details><summary>📄 Abstract</summary>
  Deployed language models are updated continually, and regulators increasingly accept changes that were declared in advance. Showing that an update changed behavior only where it was declared to is a different statistical problem from bounding how much it changed: a useful update is meant to change some decisions, so global disagreement and regression bounds cannot certify it. We formalize the problem with declared change envelopes. Before training, the developer commits to a region of inputs, an...
  </details>

- **2026-11-02** — Andrii Shkabrii, Claudia Plant, Martin Pawelczyk — [Forget What Comes Next: LLM Unlearning via Statistical Independence](http://arxiv.org/abs/2611.03955v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can memorize and reproduce fragments of their training data, raising privacy and legal concerns that motivate machine unlearning. Yet poisoned training examples can remain statistically detectable after unlearning, which raises the question of whether current unlearning objectives remove what the model has memorized at all. In this work, we introduce PINT, a novel algorithm for machine unlearning that uses the Hilbert-Schmidt Independence Criterion (HSIC) to reduce t...
  </details>

- **2026-11-02** — Le Zhou, Xiao Luo, Chinmay Chandra et al. — [Balancing Chain-of-Thought and Answer Supervision for Small Language Models on Medical Question Answering](http://arxiv.org/abs/2611.03948v1)
  <details><summary>📄 Abstract</summary>
  Small language models (<=9B parameters) can support local medical question answering (QA) while reducing privacy and latency concerns, but effective fine-tuning remains challenging. This paper compares two chain-of-thought (CoT) supervised fine-tuning methods: Uniform-across-Sequence (UaS), which applies equal loss weighting to the full CoT-and-answer sequence, and Segment-weighted (SwS), which separately weights CoT and answer losses. We evaluate six general- and medical-domain models on multip...
  </details>

- **2026-11-02** — Kyoohyun Lee, Woohyeok Park, Taeyoon Kim et al. — [Fault-Free Profiles and Decision-Level Training for Root Cause Analysis via Small Language Models](http://arxiv.org/abs/2611.02416v2)
  <details><summary>📄 Abstract</summary>
  Root cause analysis (RCA) in microservice systems requires distinguishing failure sources from routine fluctuations and propagated symptoms. Small language models (SLMs) offer a practical solution under cost and privacy constraints, and recent approaches improve their capabilities through structured diagnostic procedures. However, performing diagnostic analysis does not ensure correct root-cause identification. Our empirical study shows that final decisions often favor large anomaly scores despi...
  </details>

- **2026-11-02** — Fedor Velikonivtsev, Mikhail Koltakov, Denis Kuznedelev — [FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on Blackwell](http://arxiv.org/abs/2611.03344v1)
  <details><summary>📄 Abstract</summary>
  Attention remains a substantial computational cost in Transformer training, particularly at long context lengths. NVIDIA Blackwell GPUs provide high-throughput low-precision matrix multiplication, but exploiting it in attention requires addressing quantization overhead, causal information leakage through shared scales, and numerical inconsistencies between the forward and backward passes. We present FLAMIA, a family of attention kernels for Blackwell with MXFP8 and mixed NVFP4/FP8 training paths...
  </details>

- **2026-11-02** — Arpit Arora, Adam Holmes, Krysta M. Svore et al. — [Agentic Pipelines for Mapping Topological Codes to Quantum Hardware](http://arxiv.org/abs/2611.03329v1)
  <details><summary>📄 Abstract</summary>
  Mapping a prescribed many-body Hamiltonian to a particular quantum hardware is generally an approximate process, resulting in both intended and unwanted quantum dynamics. We introduce an AI-agent-assisted workflow that uses Lean to establish whether an effective device Hamiltonian retains the intended low-energy subspace of the target many-body Hamiltonian. We demonstrate this approach with topological quantum error correction (QEC), providing, to our knowledge, the first Lean-verified pipeline ...
  </details>

- **2026-11-02** — Mohamed Allam, Thomas Spendlhofer, Hugo Sanz-González et al. — [End-to-End NTT on FPGA for FHE Acceleration](http://arxiv.org/abs/2611.03325v1)
  <details><summary>📄 Abstract</summary>
  Fully homomorphic encryption (FHE) enables privacy-preserving computation on encrypted data without decryption. Despite its strong security guarantees, FHE incurs substantial computational and memory overhead. In FHE-based deep learning inference, on average 63% of the CPU time is spent on the number theoretic transform (NTT) and its inverse (INTT), which reduce the complexity of polynomial multiplication from $O(N^2)$ to $O(N \log N)$. Prior FPGA works follow two approaches: accelerating entire...
  </details>

- **2026-11-02** — Mahdi Haghifam, Kumar Kshitij Patel, Avrim Blum et al. — [Should We Combine Our Data? Algorithms and Limits for Privately Assessing Data Sharing](http://arxiv.org/abs/2611.03599v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study when two parties should pool their data to train a machine learning model. Two agents, Alice and Bob, each hold a sensitive labeled dataset and want to train a classifier from a given hypothesis class $\mathcal{H}$. Even when each party's dataset can be perfectly classified on its own, the two parties may follow conflicting labeling standards or have selection biases that affect their features and label sets, such that no single classifier in $\mathcal{H}$ fits their comb...
  </details>

- **2026-11-02** — Ali Abedi, Q. M. Jonathan Wu, Ning Zhang et al. — [Contrastive Adapter Training and Consensus Knowledge Distillation for Multi-Source-Free Domain Adaptation in Skin Cancer Diagnosis](http://arxiv.org/abs/2611.03528v1)
  <details><summary>📄 Abstract</summary>
  Skin cancer diagnosis, particularly differentiating melanoma from benign nevi, is challenging due to the visual similarity between lesions. Although convolutional neural networks (CNNs) and vision transformers (ViTs) have shown promising performance, their effectiveness often deteriorates on data from heterogeneous clinical sources. Conventional domain adaptation methods address domain shift but require access to source data during adaptation, which is often infeasible due to privacy regulations...
  </details>

- **2026-11-02** — Daiqiang Li, Jingyi Peng, Rui Hu et al. — [ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents](http://arxiv.org/abs/2611.03238v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches between documented and deployed software versions and differences in scope between documentation coverage and task requirements. We introduce ScienceCUA, a two-stage framework combining resource-to-skill construction with exe...
  </details>

- **2026-11-02** — Liang Song, Jiayue Jin, Peng Sun et al. — [Networked AI: Architecture, Theory, and Applications](http://arxiv.org/abs/2611.03063v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Artificial Intelligence (AI), particularly large-scale deep learning, have been driven by monolithic or offline training on massive curated datasets. While successful, these approaches face structural limitations: escalating data and computational demands, limited online adaptability, and a lack of system-level intelligence in open, non-stationary environments. This paper presents Networked AI - a networked intelligent system composed of interacting, heterogeneous, and continu...
  </details>

- **2026-11-02** — Bessie Dominguez-Dager, Miguel Cazorla, Vincent Lepetit — [VLM-as-a-Judge for Person Re-Identification](http://arxiv.org/abs/2611.03027v1)
  <details><summary>📄 Abstract</summary>
  Cloth-changing person re-identification (CC-ReID) is still very challenging, and no method clearly dominates: methods that lead on one benchmark collapse on the others, because they rest on different identity cues. We show that a general-purpose vision-language model (VLM), used zero-shot as a judge for reranking a short candidate list, beats the expert retrieval models it reranks by a wide and consistent margin. On the four scenarios of CHIRLA, a long-term CC-ReID benchmark that no publicly rel...
  </details>

- **2026-11-02** — Heungjun Im, Bongmin Cha, Agung Nugraha et al. — [Comparative study of global pooling for pre-departure ship fuel consumption prediction: Advantages over per-ship and adaptation-based approaches](http://arxiv.org/abs/2611.03015v1)
  <details><summary>📄 Abstract</summary>
  Most fuel oil consumption (FOC) models for voyage planning are per-ship models and thus generalize poorly beyond each vessel's records. Transfer and federated learning have been reported to perform better, but under different protocols that often use inputs unavailable before departure or random data splits. It therefore remains unclear which approach performs best. In this study, we compare 11 per-ship, adaptation-based, and global methods on 21 vessels. To prevent leakage, all methods receive ...
  </details>

- **2026-11-02** — ByungHee Cha, Naoki Murata, Yuhta Takida et al. — [Probing Local Conditional Fit for Diffusion Model Membership Inference](http://arxiv.org/abs/2611.02578v1)
  <details><summary>📄 Abstract</summary>
  Membership inference determines whether a candidate example was used to train a text-to-image diffusion model and is an important tool for auditing training-data use. We identify a directional membership signal in \emph{conditional prediction shifts}, the changes in predicted noise under alternative text conditions at a fixed noisy input: whether movement toward the alternative prediction initially lowers or raises the denoising loss from its value under the original caption. Members exhibit les...
  </details>

- **2026-11-02** — Swathi Pallikala, Yashas Hariprasad — [EEFA: A Framework for the Ethical Evaluation of AI Agents](http://arxiv.org/abs/2611.02561v1)
  <details><summary>📄 Abstract</summary>
  The rapid deployment of autonomous AI agents across consequential domains including healthcare, legal services, nancial management, and enterprise workows has created an urgent governance challenge. While the eld of AI evaluation has produced sophisticated benchmarks for measuring agent capability, these frameworks measure exclusively what agents can do rather than how they do it. The ethical dimensions most critical to responsible agent deployment, in- cluding respect for human autonomy, harm a...
  </details>

- **2026-11-02** — Kyoohyun Lee, Woohyeok Park, Taeyoon Kim et al. — [Fault-Free Profiles and Decision-Level Training for Small-Model Root Cause Analysis](http://arxiv.org/abs/2611.02416v1)
  <details><summary>📄 Abstract</summary>
  Root cause analysis (RCA) in microservice systems requires distinguishing failure sources from routine fluctuations and propagated symptoms. Small language models (SLMs) offer a practical solution under cost and privacy constraints, and recent approaches improve their capabilities through structured diagnostic procedures. However, performing diagnostic analysis does not ensure correct root-cause identification. Our empirical study shows that final decisions often favor large anomaly scores despi...
  </details>

- **2026-11-02** — Yuxiang Sun, Mengshi Chen, Jianwei Wang et al. — [Mixed-Type Relational Database Synthesis with Graph-Prompted Language Model](http://arxiv.org/abs/2611.02373v1)
  <details><summary>📄 Abstract</summary>
  Data access is often limited by privacy or proprietary restrictions, motivating relational database synthesis, which synthesizes realistic contents across related tables. Relational databases couple multi-table structure with mixed-type attributes and intricate semantic dependencies among values, making realistic synthesis challenging. In this paper, we propose REMIX, a unified framework for realistic relational database synthesis with mixed-type attributes. REMIX integrates a small language mod...
  </details>

- **2026-11-01** — Hossein B. Jond — [Directional Bounded-Confidence Matrix Alignment in Vicsek Flocking](http://arxiv.org/abs/2611.02189v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a directional bounded-confidence variant of the discrete-time Vicsek multiagent model, in which pairwise heading alignment is modulated by a state-dependent, positive semidefinite matrix that independently gates orthogonal radial and tangential components in the instantaneous line-of-sight frame. We analyze the normalized, matrix-weighted system dynamics, proving a uniform non-vanishing bound on proposal vectors that guarantees global well-posedness across arbitrary network s...
  </details>

- **2026-11-01** — Sandesh Kumar Kafle, Jan Vykopal, Valdemar Švábenský — [Rubric-Based Assessment of Student Reports Using Small Language Models](http://arxiv.org/abs/2611.01785v1)
  <details><summary>📄 Abstract</summary>
  Language models can analyze and assess student texts using predefined rubrics and deliver structured feedback, reducing instructors' workload. However, existing solutions often rely on external services that are resource-intensive, costly, and raise privacy concerns, making them unsuitable for constrained environments. This study evaluates an automated assessment pipeline with three key aims: design for low-resource environments, privacy, and focus on a novel context in cybersecurity education. ...
  </details>

- **2026-11-01** — Minha Hwang, Shavak Agrawal, David Chen et al. — [Measuring User Success in Randomized Search Experiments: Interpreting Good Abandonment in Generative AI Search](http://arxiv.org/abs/2611.01582v1)
  <details><summary>📄 Abstract</summary>
  Randomized search experiments increasingly evaluate experiences in which large language models answer information needs directly on the results page. Click status alone cannot identify success: a click may lead to an unsatisfactory result, while no click may indicate successful answer consumption, or "good abandonment." Prior research has shown that good abandonment is difficult to detect because dwell, scrolling, and reformulation are meaningful only in context. We present Session Success Rate ...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-11-01** — Marco Molinari, Gabriele Bettineschi — [Multi-Agent Collusion and the J-Space](http://arxiv.org/abs/2611.02153v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly deployed in Multi-Agent Systems (MAS), and they introduce the risk of coordination among agents that might escape human oversight. The J-space has been used to uncover deception in single LLMs, but its use for uncovering and steering collusion between agents remains unexplored. We show, with interpretability experiments on DeepSeek-V4-Flash (284B) on the NARCBench collusion benchmark, that colluding agents' J-space holds the collusion itself: before replying, 86% of c...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 13 papers

- **2026-11-03** — Luxi He, Pengcheng Jiang, Jifan Zhang et al. — [Suppressing Misaligned Behaviors in Language Models, Durably](http://arxiv.org/abs/2611.05358v1)
  <details><summary>📄 Abstract</summary>
  Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and beha...
  </details>

- **2026-11-03** — Ariana M. Villegas-Suarez, Guido Freire, Sohan Venkatesh et al. — [Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment](http://arxiv.org/abs/2611.05287v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning a large language model (LLM) on harmful data in a narrow domain, such as bad medical advice, can make it broadly misaligned. How realistic this risk is remains unclear, since models are very rarely fine-tuned on explicitly harmful data in practice. In this work, we show that fine-tuning on data the model believes to be false but that has no harmful content, can also induce broad misalignment. Across mathematics, trivia, cooking and sports, the more strongly the model disbelieves the ...
  </details>

- **2026-11-03** — Chandler Smith, Qi Guo, Cecilia Elena Tilli et al. — [Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems](http://arxiv.org/abs/2611.04556v1)
  <details><summary>📄 Abstract</summary>
  The deployment of AI agents in multi-agent settings enables inter-agent influence, whereby agents can strategically steer each other's behaviour towards an intended outcome. Such capabilities pose novel risks, as malicious agents could direct others towards harmful actions. In this work we investigate three such capabilities - persuasion, deception, and coercion - across five realistic evaluation environments and a variety of agents instantiated with frontier language models. We observed signifi...
  </details>

- **2026-11-03** — Bo Ma, Weiqi Yan — [Auditing Targetless Camera-LiDAR Extrinsic Correction before Recursive Use](http://arxiv.org/abs/2611.04397v1)
  <details><summary>📄 Abstract</summary>
  Camera-LiDAR fusion repeatedly uses an extrinsic transform in projection, association, and recursive state estimation. We study whether a targetless correction should be admitted to a downstream consumer only after separate audits of correction quality, confidence ranking, and recursive risk. Our log-disjoint protocol evaluates these stages under synthetic extrinsic drift on Argoverse 2 and treats cross-dataset and odometry experiments as bounded diagnostics.   On 27 test-split logs, single-fram...
  </details>

- **2026-11-03** — Xuanye Zhang, Yongsen Zheng, Kaiyu Zhou et al. — [Can Benign Skills Induce Misaligned Behavior in LLM Agents?](http://arxiv.org/abs/2611.04299v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on reusable skills to plan tasks, invoke tools, recover from errors, and complete workflows without modifying model parameters. Although these skills are typically developed to enhance benign tasks, they may also make an agent more capable of executing procedures for harmful purposes. We study this risk, which we call skill-induced behavioral misalignment: adding benign skills may cause an agent to execute external actions that violate safety requirements.   We first...
  </details>

- **2026-11-03** — Hongseung Yu, In Gim, Kyunghan Lee et al. — [Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests](http://arxiv.org/abs/2611.04794v1)
  <details><summary>📄 Abstract</summary>
  Expert offloading enables large mixture-of-experts (MoE) language models to run locally, but conventional batching stalls the GPU while missing experts are fetched. A popular remedy, known as prefetching, is to predict what experts will be needed soon and fetch them using idle link bandwidth. Imprecise prediction, however, wastes bandwidth and GPU memory on fetching unnecessary experts. Our key finding is that prefetching can be harmful when there is an expert cache in GPU memory. This is becaus...
  </details>

- **2026-11-02** — Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur — [Auditing Representation-Space Fraud Detection: A Bayesian IRL Framework for Calibrated Uncertainty and Its Limits](http://arxiv.org/abs/2611.02673v1)
  <details><summary>📄 Abstract</summary>
  Shilling detectors for recommender systems are almost always evaluated by one number, detection AUROC, with no account of when it can be trusted. We audit representation-space detection with VEIL (Variational Evaluation via Inverse-reinforcement Learning), a pairwise (Bradley-Terry) Bayesian reward-inference framework over frozen encoder embeddings, following the Bayesian auditing paradigm for LLM alignment [1]: (A) a base posterior; (B) a hierarchical ARD extension with learned confidence; and ...
  </details>

- **2026-11-02** — Brandon Jaipersaud, Elliot Creager — [Characterizing When Language Models Take Harmful Actions to Protect Their Assigned Goals](http://arxiv.org/abs/2611.03374v1)
  <details><summary>📄 Abstract</summary>
  Recent language model (LM) safety failures have largely been studied as disparate phenomena. In agentic misalignment, a model blackmails an executive to avoid being replaced. In alignment faking, it complies with harmful requests during training to keep its values from being modified. We argue that these behaviours share a common decision structure: a model assigned a goal must either take a harmful action to preserve it or refuse and lose it. We formalize this as a goal-harm conflict and presen...
  </details>

- **2026-11-02** — Abudukelimu Wuerkaixi, Qizhou Wang, Sen Cui et al. — [Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](http://arxiv.org/abs/2611.02620v1)
  <details><summary>📄 Abstract</summary>
  With the growing deployment of large language models (LLMs) across diverse domains, concerns regarding their safety have grown substantially. LLM unlearning has emerged as a pivotal approach to removing harmful or unlawful content while maintaining utility. Despite increasing interest, the challenges of continual unlearning, which is common in real-world scenarios, remain underexplored. Successive unlearning tasks often lead to intensified utility degradation. To effectively unlearn targeted kno...
  </details>

- **2026-11-02** — Boyuan Zhang, Mohammad Zandsalimy, Shanu Sushmita — [Which Words a Model Fears: From a Refusal Direction to a Vocabulary-Wide Fear Lexicon](http://arxiv.org/abs/2611.02348v1)
  <details><summary>📄 Abstract</summary>
  Whether an aligned language model refuses depends in part on which words a prompt contains, regardless of whether those words carry the request's meaning. Harm words shift the hidden state at the generation boundary along a component shared across prompts and words, which crossed differencing extracts as a single direction. In eight models, writing along this direction raises and lowers refusal monotonically with dose, ahead of random and KL-matched directions. Used as a ruler over the full voca...
  </details>

- **2026-11-02** — Bryan C. Boots — [Networked Synthetic Social Engineering on the Web](http://arxiv.org/abs/2611.02407v1)
  <details><summary>📄 Abstract</summary>
  Several genuine AI services may repeat one unsupported source, and correcting that source may leave later reports unchanged. We examine these networked consequences of synthetic social engineering (SSE), deliberately misleading influence intended to redirect AI recipients from authorized objectives. Our framework connects social influence, information aggregation, and misinformation correction research to observable evidence and permission boundaries. It separates originating attempts from legit...
  </details>

- **2026-11-01** — Changran Xu, Zeju Li, Qiang Xu — [Delivered, Not Used: Evaluating Agent Memory at Its Point of Use](http://arxiv.org/abs/2611.01718v1)
  <details><summary>📄 Abstract</summary>
  Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use. We introduce MemUse, which evaluates memory at its point of use in recorded trajectories: each memory delivery is compared with what the agent could already see and followed through the agent's later actions and their consequences. An agentic judge rates each delivered entry's relevance, accuracy, novelty, influence, and observed effect; programmatic checks enforce c...
  </details>

- **2026-11-01** — Zhihua Wang, Yifeng Gao, Yunhao Feng et al. — [CST: Lightweight Risk Triage with Source-Grounded Evidence for Web Discussions](http://arxiv.org/abs/2611.01710v1)
  <details><summary>📄 Abstract</summary>
  Web communities rely on moderators to catch harmful messages such as insults, hate speech, and scams, but no one can read every message. Existing tools give each message a risk score, which tells moderators where to look but not what to read or how to check it. Yet meaning depends on context: the same reply, "I agree.", can support or oppose removing someone from a group. Moderators therefore need source-grounded evidence, not just scores: a few key messages kept with their original wording and ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-11-03** — Li Zheng, Simin Chen — [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](http://arxiv.org/abs/2611.04356v1)
  <details><summary>📄 Abstract</summary>
  Finite element method (FEM) solvers are foundational to scientific and engineering simulation, yet their susceptibility to \emph{efficiency attacks} remains largely unexplored. An adversary can craft syntactically valid and runnable FEM programs that complete successfully while forcing excessive computational work, enabling computational denial-of-service (DoS) attacks. Finding such inputs is challenging because FEM programs occupy a vast, structured space constrained by numerical, geometric, an...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 43 papers

- **2026-11-03** — Adar Peleg, Dvir Alsheich, Tomer Ashuach et al. — [The Geometry of Ignorance: Detecting Suppressed Knowledge in LLMs through Activation Fragmentation](http://arxiv.org/abs/2611.05272v1)
  <details><summary>📄 Abstract</summary>
  Evaluating whether a large language model (LLM) genuinely knows a concept remains a fundamental problem, since behavioral metrics can be fooled by suppression: a model that refuses to answer may still harbor recoverable knowledge. The framework measures the geometric coherence of \textit{anon-vectors}, the differences in hidden states between a concept-specific query and its anonymized paraphrase, and shows that genuine knowledge forms a tight, low-entropy cluster while ignorance forces geometri...
  </details>

- **2026-11-03** — WonJun Moon, Seongchan Kim, Dahun Kim et al. — [Factorized MLLM Embeddings for Composed Image Retrieval](http://arxiv.org/abs/2611.05193v1)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) aims to retrieve a target image given a reference image and a modification text. Although recent approaches leveraging Multimodal Large Language Models (MLLMs) have shown significant progress, we argue that the MLLM's compositional understanding remains underutilized. This stems from directly mapping composed queries into a retrieval embedding via contrastive supervision alone, without explicitly resolving the intended visual modifications. In this work, we introdu...
  </details>

- **2026-11-03** — Mohammad Javad Amiri, Carsten Binnig, Andreas Kipf et al. — [Correctness Firewalls for Synthesized Database Components](http://arxiv.org/abs/2611.05173v1)
  <details><summary>📄 Abstract</summary>
  For the first time in history, high-performance code is cheap. Today's coding agents can generate bespoke, instance-optimized data systems with excellent performance, and such agents will continue to improve as LLMs advance. But a purely agentic approach, even when validated with strong testing techniques, does not automatically inherit the correctness guarantees our community has spent decades building. We propose a middle ground between hand-crafted and agent-crafted systems: correctness firew...
  </details>

- **2026-11-03** — Quan Tran, Duong Nguyen, Thanh Le-Cong et al. — [One Strategy Does Not Fit All: Rethinking Data Labeling for Just-in-Time Vulnerability Prediction](http://arxiv.org/abs/2611.05013v1)
  <details><summary>📄 Abstract</summary>
  Just-In-Time Vulnerability Prediction (JIT-VP) identifies security risks in code changes at commit time, enabling early feedback before vulnerabilities enter software systems. However, its practical reliability is challenged by the difficulty of constructing accurate labels. Multiple strategies with different trade-offs have been proposed to identify vulnerability-fixing commits (VFCs) and vulnerability-introducing commits (VICs) for dataset construction, leading to substantially different datas...
  </details>

- **2026-11-03** — Chase J. Metoyer — [Found by Search, Broken by a Shortcut: Transfer and Tampering of Searched Intrinsic Rewards](http://arxiv.org/abs/2611.04838v1)
  <details><summary>📄 Abstract</summary>
  Can a search over innate drives find intrinsic rewards that help a reinforcement-learning agent learn, transfer to a task it never saw, and resist an exploit that was absent during the search? Each candidate reward combines four generic events (a new view, a pickup, a drop and a toggle), each with a weight, a relief and a refill rate. We ran three pre-registered stages; the search protocol was locked in a public, timestamped commit before any search result existed. CMA-ES and an equal-budget ran...
  </details>

- **2026-11-03** — Yasaman Zolfimoselo, Nikolas Geroliminis, Maryam Kamgarpour — [Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards](http://arxiv.org/abs/2611.04774v1)
  <details><summary>📄 Abstract</summary>
  We study cooperative multi-agent reinforcement learning with decoupled dynamics and a monotone submodular reward function over joint trajectories. Due to the non-additive reward, an optimal policy may depend on the history of all agents. This dependence makes exact optimization exponential in the horizon and the number of agents. To overcome this challenge while retaining theoretical guarantees, we introduce pre-window curvature $c_m$, which quantifies how states visited more than $m$ steps earl...
  </details>

- **2026-11-03** — Yangguang Lin, Quan Fang, Xiaoyan Liu et al. — [SPOD: Recovering Suppressed Temporal Evidence in Video-LLMs via Single-Pass Orthogonal Decomposition](http://arxiv.org/abs/2611.04728v1)
  <details><summary>📄 Abstract</summary>
  Video Large Language Models (Video-LLMs) have achieved strong performance on many video understanding tasks, yet remain vulnerable to temporal hallucination in time-sensitive reasoning scenarios such as scene transition understanding and event ordering. Existing solutions either require costly retraining or introduce inefficient multi-pass inference and external supervision at test time. In this work, we show that temporal evidence is already encoded in Video-LLM hidden representations but is no...
  </details>

- **2026-11-03** — Pinhuan Wang, Jianian Fu, Jie Zhang et al. — [FenixWalk: Adaptive Sampling for Large-Scale Dynamic Graphs on Heterogeneous Architectures](http://arxiv.org/abs/2611.04683v1)
  <details><summary>📄 Abstract</summary>
  Random walks are fundamental to graph analytics, yet executing them efficiently on large, evolving graphs remains challenging. Existing approaches must balance sampling efficiency, update overhead, and memory consumption. Sampling structures optimized for throughput often incur substantial memory overhead and costly maintenance, whereas lightweight alternatives can suffer from high sampling latency on high-degree vertices or skewed weight distributions. These challenges become more pronounced on...
  </details>

- **2026-11-03** — Sharareh Alipour, Amir Jafari — [Balanced Fair Division and Generalized Kneser Graphs](http://arxiv.org/abs/2611.04486v1)
  <details><summary>📄 Abstract</summary>
  We study indivisible goods allocated to two prescribed nonempty groups whose members have arbitrary monotone valuations. We guarantee balanced envy-freeness up to one good (EF1) for at most five agents and up to two goods (EF2) for at most nine, for any number of goods. Bundle sizes differ by at most one. The EF1 threshold is sharp: every split of six agents can fail. EF2 improves the previous five-agent guarantee.   Via the connection of Kyropoulou, Suksompong, and Voudouris, these guarantees f...
  </details>

- **2026-11-03** — Anastasios Chatzigiannis, Natalia Panagou, Maria Koziri — [KeyWise: Efficient Video-Only Piano Transcription with a Lightweight Per-Key Architecture](http://arxiv.org/abs/2611.04476v1)
  <details><summary>📄 Abstract</summary>
  Audio-based piano transcription is hampered by the sustain pedal and by noisy or missing soundtracks, problems that video-only transcription avoids, since a top-view video shows directly when each key is pressed and released. Most visual transcription networks, however, describe the whole keyboard with one global feature vector and must learn where each key is. In this paper, we propose KeyWise, a lightweight per-key architecture that exploits the known geometry of the keyboard instead of learni...
  </details>

- **2026-11-03** — Riasad Alvi, Md. Asaduzzaman Shuvo, Md. Ahashan Habib et al. — [Entropy-Gated Dynamic Rectification for Object Hallucination in Large Vision-Language Models](http://arxiv.org/abs/2611.04438v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) routinely name objects that are absent from the image. Latent steering can reduce this failure in one model forward pass, but a fixed gate treats early and late decoding steps by the same criterion. We observe that predictive entropy varies sharply within free-running generation, while states that commit to short answers occupy a narrow, confident band. We exploit this temporal mismatch by using uncertainty as a causally available, token-local control signal ...
  </details>

- **2026-11-03** — Jinshuo Zhang, Yafei Wang, Hongwei Hou et al. — [Movable Antenna Aided Robust Wireless Transmission: From Model-Based Optimization to Scalable Reinforcement Learning](http://arxiv.org/abs/2611.04433v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates robust joint antenna positioning and precoding for multiuser movable antenna (MA) systems under imperfect channel state information (CSI). First, we identify the mismatch between the spatial statistics of densely sampled MA channels and the discrete Fourier transform (DFT) basis used for conventional robust precoding. To address this, we develop a novel discrete prolate spheroidal sequence (DPSS)-based a posteriori channel model. By exploiting the spatial covariance struc...
  </details>

- **2026-11-03** — Tamer Abdelaziz, karim Ali — [TxBench: A Benchmark of Attack Transactions and Evidence-Backed Negatives on Seven EVM Chains](http://arxiv.org/abs/2611.04411v1)
  <details><summary>📄 Abstract</summary>
  Researchers evaluate detectors of malicious smart-contract transactions on datasets that each paper assembles anew. Their positives come from incident trackers, whose citations mix attacks with setup steps and transactions that never ran, or from a detector's own output, which makes the evaluation circular; their negatives are ordinary transactions. A shared benchmark needs positives whose own execution shows the attack and negatives that use the attacks' mechanisms, with no detector deciding ei...
  </details>

- **2026-11-03** — Vimal William, Yuanzhe Li, Danella Zhao et al. — [Anchor: Augmented Cross-Layer Recurrent State for Long-Context Retrieval in Test-Time Training](http://arxiv.org/abs/2611.04327v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient linearization turns a pretrained autoregressive Transformer into an efficient model by hybridizing sliding-window attention (SWA) with a constant-size recurrent memory. But does every layer's recurrent state contribute to long-context retrieval? Investigating an SWA and Test-Time Training (TTT) hybrid, we find that retrieval is sparse across depth, concentrated in a few anchor layers, and that the remaining states hold similar information expressed through layer-specific tran...
  </details>

- **2026-11-03** — Yuxuan Wang, Dadi Guo, Weijie Guo et al. — [DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](http://arxiv.org/abs/2611.04196v1)
  <details><summary>📄 Abstract</summary>
  Frontier LLM agents can turn known vulnerabilities into working exploits, but are costly and often access-restricted due to their potential for malicious use. Open-weight models offer a more accessible alternative, but struggle to maintain progress across long exploitation chains. They also often fail to apply relevant security knowledge at the appropriate stage and in the right context to identify and evaluate promising attack directions. To address these limitations, we propose DoGNAVY-Exploit...
  </details>

- **2026-11-03** — Charles Herr, Gabriele Spadaro, Enzo Tartaglione — [Exploiting Biases in Attention for Transformers](http://arxiv.org/abs/2611.04657v1)
  <details><summary>📄 Abstract</summary>
  Attention is known to be sparse in vision transformers. In particular, we analyze the unequal relevance of attention-matrix columns to the final computation and show that this phenomenon becomes increasingly pronounced with network depth. This can be interpreted as saying that tokens have an absolute importance for the attention process, independently of queries. Inspired by this, we propose a reformulation of the attention formula that makes this phenomenon explicit by adding an input-dependent...
  </details>

- **2026-11-02** — Anarzhan Abilgazy, Mikhail Zaslavsky — [Adaptive data-driven reduced-order models for reciprocal MIMO port-Hamiltonian dynamical systems](http://arxiv.org/abs/2611.04065v1)
  <details><summary>📄 Abstract</summary>
  Port-Hamiltonian (pH) systems provide a general framework for modeling a broad class of physical dynamical systems, including systems with dissipation. Constructing accurate and robust data-driven reduced-order models for general pH systems is challenging. In this work, we focus on an important subclass of pH systems satisfying reciprocity, a property arising naturally in a variety of models. Rather than seeking to preserve the full pH structure, we exploit the additional symmetry provided by re...
  </details>

- **2026-11-02** — Nitin Aravind Birur, Divyanshu Kumar, Sahil Agarwal et al. — [JevBreak: Your Model, Their Decision](http://arxiv.org/abs/2611.03759v1)
  <details><summary>📄 Abstract</summary>
  Restricting what a model can say is often mistaken for restricting an attacker's influence over its decision. An attacker can add text to the evidence and steer the model toward a wrong answer that still belongs to the allowed set. We evaluate seven decision models spanning hosted APIs, open-weight models and an encoder on 16 tasks in seven domains from Decision Bench, targeting every wrong option across 240 text examples (990 targets per model). We present Slot Attack, a black-box attack design...
  </details>

- **2026-11-02** — Zhuyi Zhao, Shengjie Yuan, Shengyu Wang et al. — [Cyber-JEV: Matched Contrastive Fine-Tuning of Language Models for Fast Source-Code Vulnerability Triage](http://arxiv.org/abs/2611.02957v2)
  <details><summary>📄 Abstract</summary>
  Single-pass scoring models such as Jev give each code function a vulnerability probability, so that security teams can rank many functions for review without generating written explanations. Training an open-weight model for this task is limited by data. Benchmarks with both vulnerable and non-vulnerable labels keep few vulnerable functions once examples related to the test data are removed, while larger public vulnerability records mostly contain vulnerable functions only. Mixing the two lets t...
  </details>

- **2026-11-02** — Leon Klingborg, Theodor Cimpeanu, Alexander J. Stewart — [Exploit or conform? How norm utility prompting changes the way LLMs use community beliefs](http://arxiv.org/abs/2611.04048v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) serve both as tools for aiding human decision-making in everyday life and as models of human agents in experimental simulation studies. Alignment on prototypical social decisions -- such as whether to cooperate on a collective action -- therefore has immediate practical consequences for researchers and for society at large. Here we systematically explore the impact of ``norm utility'' -- the non-material components of utility that account for an individual's desire t...
  </details>

- **2026-11-02** — Paulius Skaisgiris, Thomas Pammer, Veronika Semmelrock et al. — [From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles](http://arxiv.org/abs/2611.03641v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) generation has substantially improved the performance of Large Language Models (LLMs) on complex reasoning tasks, including code generation, data analysis, and exam-style question answering. Despite these advances, purely neural LLMs continue to struggle with elementary logical reasoning problems and lack the determinism, soundness, and reliability characteristic of symbolic reasoning systems. Conversely, classical symbolic methods such as SAT solving and exact cover guara...
  </details>

- **2026-11-02** — Sharyu Kekane, Sadique Khatib, Abhushan Bokade et al. — [Qyantram: A Transparent and Verifiable Quantum Computing Platform](http://arxiv.org/abs/2611.03262v1)
  <details><summary>📄 Abstract</summary>
  Most quantum circuit platforms focus on idealized circuit assembly and simulation, hiding hardware compilation, error identification, and variational model training behind black-box operations. QYANTRAM addresses this gap through an open platform comprising four subsystems, built around evidence-backed results and independent verification.   Its staged compilation pipeline makes every transformation traceable, while the router publishes rejected SWAP candidates and their scores for transparent d...
  </details>

- **2026-11-02** — Xiaohan Qin, Xiangdong Zhang, Yu Wang et al. — [DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction](http://arxiv.org/abs/2611.03142v1)
  <details><summary>📄 Abstract</summary>
  Scaling depth is a key route to stronger large language models, but Pre-LN architectures often suffer from depth-wise information dilution, limiting the effective use of deep layers. While cross-layer connectivity has proven effective at mitigating this problem, existing designs usually introduce additional computation or memory access. We revisit cross-layer KV sharing as an efficient form of such connectivity. Beyond cache compression, each KV reuse edge creates a direct gradient path from dee...
  </details>

- **2026-11-02** — Manoj N H, S Ganga Prasath — [Emergent stigmergy and pheromone-guided decisions in a foraging collective](http://arxiv.org/abs/2611.02997v1)
  <details><summary>📄 Abstract</summary>
  Ants in a colony forage and recruit other nest-mates for cooperative transport of food through stigmergy. Traditional approach to capture the foraging dynamics relies on fine-tuning phenomenological rules for pheromone deposition, chemotaxis, evaporation, and behavioral switching after reaching the food source. Here, we show that stigmergy emerges from an infinite-horizon stochastic optimal control problem involving outbound foragers traveling from the nest to the food source and returning agent...
  </details>

- **2026-11-02** — Zhuyi Zhao, Shengjie Yuan, Shengyu Wang et al. — [Cyber-JEV: Matched Contrastive Fine-Tuning of Language Models for Fast Source-Code Vulnerability Triage](http://arxiv.org/abs/2611.02957v1)
  <details><summary>📄 Abstract</summary>
  Single-pass scoring models such as Jev give each code function a vulnerability probability, so that security teams can rank many functions for review without generating written explanations. Training an open-weight model for this task is limited by data. Benchmarks with both vulnerable and non-vulnerable labels keep few vulnerable functions once examples related to the test data are removed, while larger public vulnerability records mostly contain vulnerable functions only. Mixing the two lets t...
  </details>

- **2026-11-02** — Woohyeon Byeon, Seongmin Kim, Jiwon Jeon et al. — [AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games](http://arxiv.org/abs/2611.02875v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we consider mixed-motive games (MMGs) which model various real-world multi-agent scenarios where self-interested agents must both cooperate and compete. We identify an issue with existing gifting methods, where agents become overly dependent on incoming gifts and fail to learn reward-yielding behaviors, a phenomenon we call gift over-reliance. To address this, we propose a refusal-augmented gifting framework that balances cooperation and competition in MMGs. Our approach introduce...
  </details>

- **2026-11-02** — Wen Zeng, Ke Hong, Xu Fu et al. — [Rose: Efficient Embodied RL through Graph Optimization and GPU Compute Resource Control](http://arxiv.org/abs/2611.02705v1)
  <details><summary>📄 Abstract</summary>
  Embodied reinforcement learning (RL) coordinates policy inference, simulation, and model training with highly heterogeneous resource demands. Although individual components frequently underutilize GPU compute during execution, existing systems only overlap work at coarse component boundaries (e.g., pipelining inference and simulation across simulator groups), leaving substantial low-activity GPU windows within subcomponent phases and nested loops. Exploiting these fine-grained windows manually r...
  </details>

- **2026-11-02** — Bohan Jiang, Dawei Li, Yasin Silva et al. — [The Customer Never Sees the Goal: Measuring and Detecting Vulnerability-Targeted Manipulation in LLM Assistants](http://arxiv.org/abs/2611.02689v1)
  <details><summary>📄 Abstract</summary>
  Companies deploy large language model (LLM) assistants on their websites to advise customers. For commercial reasons, the operator can give an assistant a goal that the customer never sees. This paper focuses on operator-induced vulnerability-targeted manipulation (VTM), in which an assistant pursues such a goal by exploiting a vulnerability the customer discloses. While existing research mainly measures how manipulative a model is, we go further and ask whether VTM can be detected from the cust...
  </details>

- **2026-11-02** — Hanyoung Park, Yongjae Jang, Ji-Woong Choi — [Vehicle Speed-Aware Jammer-Resilient Receiver for Multi-User MIMO V2X Systems](http://arxiv.org/abs/2611.02552v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-everything (V2X) communication plays a crucial role in enabling connected and autonomous driving by supporting the reliable exchange of safety-critical information among vehicles and infrastructure. However, due to the open nature of wireless channels, V2X systems are vulnerable to various physical-layer attacks, among which jamming is one of the most intuitive and severe threats. In this paper, we propose a vehicle speed-aware jammer-resilient reception framework for multi-user multi...
  </details>

- **2026-11-02** — Chengzhi Lu, Boxi Zhou, Yanying Lin et al. — [When Cache Pressure Becomes a Trap: Metastability in Agent Serving](http://arxiv.org/abs/2611.02543v1)
  <details><summary>📄 Abstract</summary>
  LLM agents repeatedly send a growing conversation to a model, making prefix reuse central to efficient serving. We show that a brief surge can disrupt this reuse and trigger metastable failure in prefill--decode (PD) disaggregated engines: service remains degraded after arrivals return to a load the engine previously sustained. On SGLang, a ten-minute surge reduced goodput by about 88% over the following hour. Removing the residual burst sessions restored service within minutes.   The sustaining...
  </details>

- **2026-11-02** — Liangbo Ning, Siyuan Liang, Yi Zhou et al. — [Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration](http://arxiv.org/abs/2611.02457v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-augmented recommender systems (RecSys) enhance user preference modeling by generating reasoning trajectories over historical interactions before making recommendations. Knowledge distillation provides a practical paradigm for transferring such reasoning capabilities from powerful large language models to lightweight RecSys. However, existing methods typically rely on a single fixed teacher, remain constrained by the teacher knowledge ceiling, and indiscriminately distill teacher-genera...
  </details>

- **2026-11-02** — Bing Fan, Yunhe Feng, Yan Huang et al. — [Exploiting Textual Semantics for Robust Cross-View Object Correspondence](http://arxiv.org/abs/2611.02356v1)
  <details><summary>📄 Abstract</summary>
  Cross-view object correspondence (CVOC) aims to establish associations of the same target between query and search videos captured from different viewpoints. Existing methods often rely on visual cues for CVOC. Despite recent progress, these methods struggle in complicated scenarios with substantial viewpoint changes and appearance variations, due to lacking sufficient target information. Addressing this, we introduce TeSCo, a framework that exploits rich Textual Semantics of an object, in addit...
  </details>

- **2026-11-01** — Arun B. Chandrasekaran, Damilola Popoola, Souradeep Bhattacharya et al. — [ZT-DAC: ML-Driven Dynamic Access Control Policy for Zero Trust in DER Networks](http://arxiv.org/abs/2611.02107v1)
  <details><summary>📄 Abstract</summary>
  The increasing penetration of Distributed Energy Resources (DERs) in the smart grid has significantly expanded the cyber-attack surface. Traditionally, DER networks rely on static role-based access control (RBAC) mechanisms that assume persistent trust after authentication. This limitation enables adversaries to maintain unauthorized privileges and move laterally across DER systems, disrupting grid operations. Although attribute-based access control (ABAC) enables fine-grained and context-aware ...
  </details>

- **2026-11-01** — David A. Ehrlich, Manuel Baltieri, Fernando E. Rosas et al. — [Beliefs in feedback: Factored representations of interacting agents in transformers](http://arxiv.org/abs/2611.02047v1)
  <details><summary>📄 Abstract</summary>
  Complex systems, from ecosystems to brains, are usually modeled as modular components coupled through feedback rather than as indivisible wholes. Can a transformer trained on the joint behavior of a group of interacting agents be understood in the same way? In this work, we develop a computational-mechanics framework to study agents interacting in feedback loops. We formally prove that any joint stochastic process can be presented as resulting from the behavior of agents interacting in feedback,...
  </details>

- **2026-11-01** — Bum Jun Kim, Anastasis Kratsios — [Scalar Smoothness Is One Point on a Besov Spectrum](http://arxiv.org/abs/2611.02037v1)
  <details><summary>📄 Abstract</summary>
  Studies of neural network generalization and robustness often summarize smoothness with a single number, such as a Lipschitz constant or a Hessian curvature statistic. However, Lipschitz constants summarize global worst-case sensitivity and Hessian statistics summarize local curvature; neither captures how model responses vary with the size, direction, and location of perturbations encountered in real-world deployment. To measure smoothness under these perturbations, we introduce a finite-differ...
  </details>

- **2026-11-01** — Parmida Valiahdi, Niloofar Mehrnia, Mustafa Furkan Beker et al. — [FADE: A Flow-Based Approach for Multichannel Tail Estimation](http://arxiv.org/abs/2611.01849v1)
  <details><summary>📄 Abstract</summary>
  Ultra-Reliable Low-Latency Communication (URLLC) is vulnerable to rare low-received-power events, and the spatial-diversity benefits of multiple receivers can be significantly reduced when they experience simultaneous deep fading. Multivariate Extreme Value Theory (MEVT) provides a principled framework for characterizing such joint tail behavior. However, conventional MEVT methods often rely on restrictive parametric assumptions or discrete representations of the dependence structure, which may ...
  </details>

- **2026-11-01** — Rui Cao, Jia-Hui Pan, Yin Zhang et al. — [UA-Depth: Uncertainty-Aware Depth Restoration for Material-Agnostic Object Manipulation](http://arxiv.org/abs/2611.01645v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation requires accurate metric depth, yet commodity RGB-D cameras often fail on non-Lambertian objects such as transparent, reflective, and translucent materials, producing holes, structured noise, and biased depth. Most restoration methods produce only a single depth map, treating noisy and reliable regions uniformly for downstream tasks while ignoring regional uncertainty. We present UA-Depth, an uncertainty-aware depth restoration framework that iteratively co-refines depth and...
  </details>

- **2026-11-01** — Hong Nie, Zhangchi Gao, Yuqian Liang et al. — [Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models](http://arxiv.org/abs/2611.01617v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates vision-language model (VLM) inference without altering the output distribution, yet two factors limit its gains. Existing drafters either lack the image evidence required for visually grounded tokens or pay to condition on every visual token, although a short draft block typically depends on only a few image regions. Moreover, the value of verifying additional candidates varies with GPU load, so no fixed verification structure is efficient across serving conditio...
  </details>

- **2026-11-01** — Jianfeng Ding, Linfeng Tang, Hao Zhang et al. — [NatureFusion: Rethinking Infrared and Visible Image Fusion as Natural Complementary Enhancement](http://arxiv.org/abs/2611.01607v1)
  <details><summary>📄 Abstract</summary>
  In the absence of ground truth, most existing infrared and visible image fusion methods pursue fidelity to the source images and directly superimpose two physically distinct modalities. As a result, salient infrared targets appear as bright patches of thermal radiation pasted onto the scene. These patches obscure the original color and texture of the targets, so the fused images look unnatural to human observers and deviate from the data distribution learned by vision models pretrained on visibl...
  </details>

- **2026-11-01** — Shicheng Huang, Cai Fu, Jianqiang Lyu et al. — [StateGate: A Behavioral-Fidelity Prompt Optimization Method for Long-Chain LLM Agents](http://arxiv.org/abs/2611.01585v1)
  <details><summary>📄 Abstract</summary>
  Currently, long-chain LLM agents commonly suffer from behavioral degradation in complex tasks, where prompts are written in full but steps are not executed in full. To address this issue, existing approaches face three major challenges. First, constraints are strongly bound to their textual carriers; once natural-language constraint sentences are removed, their binding force vanishes. Second, the execution process lacks independent verification, as the evidence for judgment is often supplied by ...
  </details>

- **2026-11-01** — Bohan Liu, Wenqian Ye, Guangzhi Xiong et al. — [Label-Free Localization and Test-Time Suppression of CLIP's Typographic Circuits](http://arxiv.org/abs/2611.01513v1)
  <details><summary>📄 Abstract</summary>
  CLIP-based Vision-Language Models have become cornerstones of modern multimodal systems. The cross-modal contrastive objective equips the CLIP vision encoder to both see objects and read text. These two abilities induce an entanglement between the encoding of lexical and semantic shapes, creating a distinctive vulnerability to typographic attacks, in which rendered text overrides an image's semantic content with its literal meaning. The black-box nature of these encoders has prevented a mechanis...
  </details>

- **2026-11-01** — Haoyu Zhao, Zafeirios Fountas, Jun Wang — [Can Large Language Model Agents Learn by Watching Tutorial Videos?](http://arxiv.org/abs/2611.01460v1)
  <details><summary>📄 Abstract</summary>
  Humans continuously acquire knowledge from carefully crafted materials such as books and tutorial videos, carrying that understanding into future tasks. Millions of such instructional videos are uploaded online every day, yet LLM agents remain unable to exploit this ever-expanding wealth of human teaching. Their capabilities are frozen after training, while parameter updates at scale remain prohibitively expensive. This raises the central question: can LLM agents learn from this vast instruction...
  </details>

- **2026-11-01** — Leming Shen, Qiang Yang, Xinyu Huang et al. — [A Self-Exploring and Self-Evolving Paradigm for Adaptive Edge AI Development](http://arxiv.org/abs/2611.01377v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) exhibit powerful code generation abilities, fostering agentic systems to automate edge AI application development. However, existing agents typically operate via fixed agentic workflows and predefined design spaces, struggling to handle rapidly evolving demands of real-world scenarios (e.g., heterogeneous data modalities, diverse task pipelines). Unlike prior systems that treat LLMs mainly as code generators following rigid workflows, we fully exploit their reasoning...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 53 papers

- **2026-11-03** — Javal Vyas, Mehmet Mercang{ö}z — [OperAItor: An Agentic Framework for Fault-Tolerant Operation of Chemical Processes](http://arxiv.org/abs/2611.05179v1)
  <details><summary>📄 Abstract</summary>
  OperAItor, an open-source framework for developing and evaluating large language model agents for supervisory fault management in chemical processes. The framework is demonstrated on a dynamic reactor-distillation process representing isopropanol dehydrogenation, with physically based thermodynamics and modified reaction kinetics to permit liquid-phase operation. The process is represented by a 113-variable differential-algebraic model and operates at a nominal feed rate of 100kmol/h, producing ...
  </details>

- **2026-11-03** — Sarah Montgomery-Taylor, Hamsa Subramaniam, Rob Brisk et al. — [Towards Multi-Method Evaluation of AI in Health: Integrating Benchmarks, Autoraters, and Expert Evaluation](http://arxiv.org/abs/2611.05127v1)
  <details><summary>📄 Abstract</summary>
  General-purpose generative AI (GenAI) models are being rapidly adopted in healthcare, but they are challenging to assess with traditional evaluation frameworks. These conceptual, methodological, and practical challenges parallel decades of work in evaluating clinician and health system quality and safety. We describe the adaptation of methods from several fields, combined with emerging technical approaches, into a structured, multi-method evaluation framework designed to give well-rounded assess...
  </details>

- **2026-11-03** — Rounak Sen, Divya Kumari, Deeksha Varshney — [When Ground Truth Is Not Ground Truth: Automatic Labeling for Hallucination Detection](http://arxiv.org/abs/2611.04697v1)
  <details><summary>📄 Abstract</summary>
  Hallucinations in Large Language Models (LLMs) remain a major challenge, as they can produce misleading, factually incorrect, or unverifiable information, thereby undermining their trustworthiness and reliability. However, reliable ground-truth labels remain a key challenge in evaluating hallucination detectors. Recent studies often construct labels automatically by comparing model generations with reference answers using similarity metrics such as BLEURT. This implicitly treats BLEURT similarit...
  </details>

- **2026-11-03** — Jonas Hallgren, David Hyland, Mahault Albarracin — [Can Network Models of Science Do Without Pluralist Agents?](http://arxiv.org/abs/2611.04590v1)
  <details><summary>📄 Abstract</summary>
  Science is a process of useful models being proven wrong time and again, but despite its many flaws, it somehow works. Why is this? Paul Feyerabend argued that it works because people dare to hold and defend incompatible rival theories against the accepted one, since a theory's failures often lead to its abandonment in the presence of a more accurate or simpler alternative. He called this view theoretical pluralism. We introduce a theoretical and experimental model in which this can be examined....
  </details>

- **2026-11-03** — Zhan-He Wang, Zi-Yang Lang, Yi-Yang Li et al. — [CosmosAlpha: Multi-Relational Graph Search with Pareto-Guided Exploration for LLM-Driven Alpha Mining](http://arxiv.org/abs/2611.04555v1)
  <details><summary>📄 Abstract</summary>
  Discovering predictive alpha factors from noisy financial data is a fundamental yet challenging problem in quantitative finance. LLM-driven formulaic alpha mining offers an attractive paradigm by combining interpretable symbolic expressions with iterative generation and refinement guided by quantitative feedback. However, existing generation-centric and tree-based search strategies primarily organize factors through generation lineage, leaving structural and statistical relationships across sear...
  </details>

- **2026-11-03** — Suifeng Zhao, Zida Liu, Lei Sun et al. — [AttriSwarm: Orchestrating Agent Swarms for Cross-Page Visual Attribution](http://arxiv.org/abs/2611.04504v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) increasingly address knowledge-intensive tasks by integrating evidence scattered across multiple document pages into a final answer. Because such answers are synthesized from many pages, the link between the answer and its supporting visual evidence can become obscured, hindering verification and trust. Cross-page visual attribution is therefore essential: it requires identifying the supporting pages and localizing fine-grained evidence regions within the...
  </details>

- **2026-11-03** — Yi-Ping Chen, Ying-Kuan Tsai, Seul Lee et al. — [Integrating Machine Learning and Uncertainty Quantification for Real-Time Decision-Making in Digital Twins: A System-Centric Review and Perspective](http://arxiv.org/abs/2611.04269v1)
  <details><summary>📄 Abstract</summary>
  Digital Twins are evolving from passive virtual representations into closed-loop systems that continuously synchronize with physical assets and drive real-time decisions. Yet predictive modeling, machine learning (ML), uncertainty quantification (UQ), and decision-making have been studied as separate capabilities, leaving limited understanding of their integration and maintenance during online operation. This narrative review, scoped by the functional requirements of real-time decision-making ra...
  </details>

- **2026-11-03** — Mahmoud Alyosify, Mirna Imbabi, Eman Elkhamisi et al. — [Say Less, Mean Better: Training-Free Verbosity Control for Language Models](http://arxiv.org/abs/2611.04107v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often generate responses longer than necessary, increasing inference latency and computational cost. While prompting can encourage conciseness, controlling output length without compromising response completeness remains challenging. Aggressive early stopping can reduce generation costs but risks terminating responses prematurely. We introduce MinimalLM, a training-free framework for reliable verbosity control that combines uncertainty-aware, length-dependent stop-to...
  </details>

- **2026-11-03** — Jillian Fisher, Thomas Richardson, Daniel W. Fisher et al. — [Whose Guardrail? User Identity Shapes the Effectiveness of Model Disclaimers in Mitigating LLM Political Persuasion](http://arxiv.org/abs/2611.05347v1)
  <details><summary>📄 Abstract</summary>
  Politically biased AI can shift users' opinions, yet it remains unclear whether model disclaimers protect against such persuasion. We report a preregistered experiment (N=1,586) examining how disclaimer design and user characteristics shape susceptibility to politically biased AI. We varied whether disclaimers identified political bias versus potential inaccuracies and whether they included an explanation. Participants completed two decision-making tasks with an LLM biased against their politica...
  </details>

- **2026-11-03** — Aashish Chapagai, Angad Singh Gurtatta, Erik Cambria — [Can saliency maps flag chest radiograph classifier errors at a new hospital? An external validation study](http://arxiv.org/abs/2611.05011v1)
  <details><summary>📄 Abstract</summary>
  Saliency maps are offered as a safeguard for medical image classifiers, but whether they reveal individual errors at a new hospital remains largely untested. We trained a convolutional network and a vision transformer on NIH ChestX-ray14 and evaluated 303,768 decisions per model at the training hospital and at two external sites, in the USA and Vietnam, with radiologist-consensus labels. We scored each explanation by its anatomical enrichment, the area-normalized concentration of attribution in ...
  </details>

- **2026-11-03** — Zhiheng Li, Zongyang Ma, Jiaxian Chen et al. — [OCR in the Foundation Model Era: From Specialist Models to Unified Models](http://arxiv.org/abs/2611.04874v1)
  <details><summary>📄 Abstract</summary>
  Optical Character Recognition (OCR) is among the oldest and most widely deployed applications of artificial intelligence. This survey reviews its development, focusing on the Foundation Model Era. We define OCR through faithful transcription: within a specified visual scope, OCR should completely reconstruct the text, notation, and document structure observable in the source image, and every textual, notational, or structural element in the output must be verifiable from visual evidence in that ...
  </details>

- **2026-11-03** — Yang Xiao, Ting Dang — [VeriSpoof: Beyond Real or Fake with One Audio LLM](http://arxiv.org/abs/2611.04634v1)
  <details><summary>📄 Abstract</summary>
  A speech deepfake detector estimates whether a recording is synthetic, but a forensic analyst also asks which system produced it, whether recordings share a source, and what evidence supports each conclusion. We present VeriSpoof, an audio language model that unifies five tasks with shared weights: deepfake detection, generator attribution (generator, acoustic model and vocoder), recording-condition analysis, synthesized-span localisation, and source verification. Each decision is supported by g...
  </details>

- **2026-11-03** — Xiaoshan Zhou — [Co-Occurrence Priors Override Visual Spatial Evidence: Understanding False Alarms in Vision-Language Models for Construction Struck-By Hazard Detection](http://arxiv.org/abs/2611.04112v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) increasingly support construction hazard monitoring, yet their frequent false alarms remain poorly understood. This study investigates whether false struck-by hazard warnings arise from failures in object recognition, spatial relation encoding, or hazard decisions dominated by learned co-occurrence priors. We evaluated Qwen2.5-VL-7B and InternVL3.5-8B using 355 counterfactual worker-excavator scene pairs with controlled spatial proximity and worker-removal variants,...
  </details>

- **2026-11-02** — Shravya Kanchi — [Permitted but Unauthorized: Affordance-Induced Delegated-Scope Violations in Multi-Agent LLM Systems](http://arxiv.org/abs/2611.04086v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems place several agents on shared infrastructure, where each agent holds permissions far broader than the task it is delegated -- so every agent is routinely permitted to act on a peer's resources it was never assigned. We ask: under competitive pressure, what determines whether an agent crosses from its delegated scope into a peer's resources, and can such crossings be enforced away? We study this across eight LLMs in two simulated environments -- a CI/CD release pipeline a...
  </details>

- **2026-11-02** — Shobhnik Kriplani, Haohan Wang — [Characterizing Adversarial GEO via Implicit Brand Injection](http://arxiv.org/abs/2611.04005v1)
  <details><summary>📄 Abstract</summary>
  Generative search engines increasingly shape how users discover products, services, and commercial entities by generating answers from retrieved web content. This creates an opportunity to influence which brands appear in these answers by modifying the content available to the retrieval system. In this work, we study an adversarial generative engine optimization (GEO) setting in which a predefined brand is added to an article through a single contextually integrated mention. The challenge is to ...
  </details>

- **2026-11-02** — Tianyi Ma, Jing Gu, Haozhe Zhao et al. — [ScienceVision: Can AI Observe and Reason Like a Scientist?](http://arxiv.org/abs/2611.04087v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery builds on accurate observations interpreted through domain knowledge and reasoning. For scientific 3D data, this requires understanding structures and spatial relationships, from protein contacts to anatomical organization. Existing multimodal benchmarks largely evaluate text and 2D images, while scientific 3D evaluations vary in representations and protocols across disciplines, limiting cross-disciplinary comparison. To assess these foundational capabilities, we introduce S...
  </details>

- **2026-11-02** — Anh Nguyen, Tianyi Xu, Phat Tran et al. — [Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials](http://arxiv.org/abs/2611.04073v1)
  <details><summary>📄 Abstract</summary>
  Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges. However, the contribution of each component -- tutorials, the judge, and the world model -- to overall improvement has not been evaluated in isolation. To fill this gap, we first construct OSWorld-Tutorial and ScienceBoard-Tutorial: two datasets for CUAs with curated multimodal tutorials, covering everyday and scientific domains. We then ...
  </details>

- **2026-11-02** — Emmanuela Andam, Emanuel S. Grant, Naima Kaabouch — [What Malware Actually Does: An Empirical Analysis of Post-Infection Behavior Across Malware Families](http://arxiv.org/abs/2611.03774v1)
  <details><summary>📄 Abstract</summary>
  Most malware detection research focuses on identifying whether a file is malicious before it executes. Far less attention goes to what happens after infection. This paper presents an empirical analysis of post-infection malware behavior across 37 families, grounded in dynamic sandbox execution using CAPEv2. Behavioral traces are modeled as heterogeneous graphs with five node types and seven typed edge relationships, preserving relational structure that flat feature vectors discard. A voting ense...
  </details>

- **2026-11-02** — Rupak Kadel, Jie Li, Yong Chen — [INSIGHT-HPC: An Interpretable System Intelligence for Global HPC Telemetry](http://arxiv.org/abs/2611.03875v1)
  <details><summary>📄 Abstract</summary>
  Modern high-performance computing (HPC) clusters integrate multi-generation CPUs and GPUs, which generate rich, high-dimensional telemetry streams from out-of-band baseboard management controllers (BMC), job schedulers, and facility power distribution units. Detecting anomalies within this telemetry is critical to prevent energy waste and costly node failures. Existing approaches often rely primarily on statistical deviations and require stronger labels than actual production environments can pr...
  </details>

- **2026-11-02** — Zhengdao Li, Hui Wen, Zixuan Wan et al. — [TrafficInstruct: A Multi-Task Network Traffic Dataset and Benchmark for Instruction Tuning](http://arxiv.org/abs/2611.03319v1)
  <details><summary>📄 Abstract</summary>
  Instruction tuning for multi-task network traffic analysis requires data with clearly defined sources, supervision targets, and evaluation conditions. We introduce TrafficInstruct, a newly collected dataset comprising raw packet captures and 55,000 structured supervised fine-tuning records across ten tasks: malware traffic detection, botnet detection, malicious DNS-over-HTTPS detection, Web attack detection, advanced persistent threat detection, encrypted VPN detection, Tor behavior detection, e...
  </details>

- **2026-11-02** — Yiwei Zha, Qingyu Meng, Herbert Bos et al. — [Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](http://arxiv.org/abs/2611.03223v1)
  <details><summary>📄 Abstract</summary>
  LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not identify where each violation comes from. We introduce ARCBench(Agent Rule Compliance Benchmark), a configurable benchmark built on the open-source pi agent harness. Its tool-calling agent loop lets us measure rule compl...
  </details>

- **2026-11-02** — Tom Saliencro, Wen-Hsuan Liu, Rohan Desai et al. — [BISECT: Bilevel Spectral Decomposition for Low-Rank Continual Learning](http://arxiv.org/abs/2611.03574v1)
  <details><summary>📄 Abstract</summary>
  Exemplar-free continual learning on pre-trained Vision Transformers increasingly relies on Low-Rank Adaptation (LoRA), yet prevailing methods govern the low-rank update space through strict subspace isolation. By projecting each incoming task into the approximate null space of historical token activations, isolation-based learners equate any cross-task feature overlap with catastrophic interference. We show that this orthogonality premise induces a structural bottleneck we term \emph{spectral st...
  </details>

- **2026-11-02** — Shai Nahum Gefen, Vered Chassida, Dmitry Basin et al. — [Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](http://arxiv.org/abs/2611.03434v1)
  <details><summary>📄 Abstract</summary>
  Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a method for fitting a minimal agent harness to a fixed, self-hostable LLM. Given an expert-validated dataset, CLEO admits only the tools, guardrails, memory policies, and loop components that improve accuracy while remaining g...
  </details>

- **2026-11-02** — Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez et al. — [Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents](http://arxiv.org/abs/2611.03384v1)
  <details><summary>📄 Abstract</summary>
  Financial research agents can generate and monitor trading rules faster than a human can document the resulting selection process. Candidates appear at data-dependent times, weak rules are abandoned, and promising ones are watched until they cross a reporting threshold. We introduce PROMOTE, a protocol that assigns every candidate predictable testing wealth at birth and accumulates a cost-aware e-process only from subsequent returns. If lifetime allocations sum to at most one, a weighted Ville a...
  </details>

- **2026-11-02** — Tianqi Gao, Ruobing Jiang — [Towards AI-Agent-Accelerated Research in High-Energy Physics: A Case Study in Monte Carlo Analysis](http://arxiv.org/abs/2611.03373v1)
  <details><summary>📄 Abstract</summary>
  We investigate how far contemporary LLM-based agents can participate in multistep computational high-energy-physics research under reproducible human supervision. Using a previously published CEPC Bell-observable analysis in $e^+e^- \to ZH$, $Z \to q\bar q$, $H \to ZZ^* \to 4μ$ as a case study, we test two capabilities. First, the agent performs an instruction-constrained reproduction: it is explicitly instructed not to use the published numerical results as analysis targets, although no technic...
  </details>

- **2026-11-02** — Akram Elbouanani, Yousra Taleb, Gianluca Demartini et al. — [User Attributes and Political Ideology Shape LLM Receptiveness in Online Political Debates](http://arxiv.org/abs/2611.02908v1)
  <details><summary>📄 Abstract</summary>
  Online political discussions increasingly involve AI-mediated participation, as users invoke LLMs to assess contested claims, arbitrate disputes, and respond to opposing viewpoints. As these systems become participants in online exchanges, they may alter which speakers and argumentative strategies receive validation within the discussion.   We study this interactional dimension by reconstructing 5,376 Debate.org debates as LLM conversations and running nearly 150,000 controlled multi-turn conver...
  </details>

- **2026-11-02** — Weixiang Zhao, Zhihao Liu, Guancheng Li et al. — [Predictive Safety Guardrails Do Not Always Make LLM Agents Safer](http://arxiv.org/abs/2611.02815v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly take consequential actions in digital and physical environments, where safety risks may emerge only after multiple interaction steps. This has motivated world-model-driven predictive safety guardrails, which anticipate future consequences before execution. However, existing evaluations largely focus on end-to-end safety outcomes, leaving unclear whether safety gains arise from reliable prediction and faithful use of predicted risks. In this work, we syste...
  </details>

- **2026-11-02** — Jinpeng Hu, Yiduo Jin, Erqiang Wang et al. — [AffToM: Benchmarking Recursive Affective Theory of Mind in Dynamic Multi-Party Interactions](http://arxiv.org/abs/2611.02725v1)
  <details><summary>📄 Abstract</summary>
  Understanding emotion in realistic social interactions requires more than recognizing facial expressions or assigning affective labels. The same event can elicit different emotions depending on what each participant knows, what they believe others know or feel, and how these nested mental states evolve over time. Existing benchmarks largely study higher-order epistemic Theory of Mind (ToM) and multimodal emotion reasoning in isolation, leaving recursive affective reasoning under asymmetric and d...
  </details>

- **2026-11-02** — Lixun Zhang, Zishan Shao, Kangning Cui et al. — [BasisKV: Value Latents for Communication and Key Routing](http://arxiv.org/abs/2611.02583v1)
  <details><summary>📄 Abstract</summary>
  Long-context large language model (LLM) inference is increasingly constrained by the cost of maintaining an ever-growing KV-cache. Low-rank K/V projections provide a promising way to compress the KV-cache with minimal quality loss, but prior work has largely optimized KV-cache compression in isolation, leaving distributed inference, especially with tensor parallelism where attention computation is partitioned across multiple GPUs, largely underexplored. We make two observations: (i) tensor-paral...
  </details>

- **2026-11-02** — Xiaokun Sun, Jian Yang, Zhenyu Zhang — [SeMo3D: Unifying 3D Generation, Editing, and Completion via Selective Modeling](http://arxiv.org/abs/2611.02568v1)
  <details><summary>📄 Abstract</summary>
  3D generation, editing, and completion are typically treated as regenerating the complete 3D asset under task-specific constraints, even when only a local region needs modification. This leads to task isolation, inconsistency in content that should remain unchanged, and dependence on task-specific paired data. We address these issues with a key observation: the three tasks all synthesize a designated region while keeping the rest intact---the full region for generation, the target region for edi...
  </details>

- **2026-11-02** — Xiao Yang, Aishan Liu, Siyuan Liang et al. — [Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety](http://arxiv.org/abs/2611.02516v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly to emerging risks. Here we present EVOLVE, a tool-level self-evolving defense framework that formulates agent security as a process of cumulative security evolution. Inspired by how human societies transform experiences into transferable pro...
  </details>

- **2026-11-02** — Keuntae Kim, Yong Suk Choi — [A balloon effect: ban one channel and a hidden trait finds another](http://arxiv.org/abs/2611.02509v1)
  <details><summary>📄 Abstract</summary>
  Language models trained on the outputs of other models can acquire traits that those outputs never mention, such as a preference for an animal carried by lists of numbers. Such subliminal learning can pass on unwanted traits. The intuitive defence is to find and forbid the tokens through which a trait shows, but how a trait's trace behaves under such bans, and what of it a student learns, has not been resolved. We closed a trait's outlets one by one in two stress tests, a preference chain and a ...
  </details>

- **2026-11-02** — Nico Morloher, Johannes Reschke, Mohamed Mady — [Specificity Bias and the Wikipedia Paradox: An xAI Analysis of AI Text Detectors under Domain Shift](http://arxiv.org/abs/2611.03280v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of Large Language Models (LLMs) demands reliable detection of human-authored versus synthetic text. However, current Transformer-based detectors often experience severe performance degradation during domain shifts and operate as opaque classifiers. This paper investigates the robustness and interpretability of fine-tuned Transformer models (DistilBERT, RoBERTa) by evaluating them against a custom out-of-distribution (OOD) dataset of hyper-local news synthesized via open-s...
  </details>

- **2026-11-02** — Néstor Ortega, Agustín Salgado, Javier Sánchez — [Comprehensive Evaluation of Monocular and Multi-view 3D Human Pose Estimation Models for Fitness Exercise Analysis](http://arxiv.org/abs/2611.02929v1)
  <details><summary>📄 Abstract</summary>
  Three-dimensional human pose estimation has become a fundamental component of computer vision systems for sports analytics, rehabilitation, and motion understanding. Although recent deep learning approaches have achieved remarkable accuracy on standard benchmarks, their performance under realistic sports scenarios remains insufficiently studied. Furthermore, the trade-offs between recent monocular and multi-view approaches, as well as the benefits of post-processing techniques for improving temp...
  </details>

- **2026-11-02** — Zihao Sun — [From Language to Country to Valence: A Multilingual Audit of Stereotype Bias Across LLMs](http://arxiv.org/abs/2611.02585v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly considered for education, recruitment, workplace decision support, and other consequential applications, making pre-deployment social-bias detection essential. Yet major benchmarks are English-centred or translated, focus mainly on negative stereotypes, and may miss linguistic and cultural variation. We investigate gender, racial, and religious bias using 12,000 locally written Reddit posts in English, Spanish, French, and German. Only search terms a...
  </details>

- **2026-11-02** — Tao Xie, Yiqun Zhang, Yiu-ming Cheung — [When Prediction Shapes the Future: A BlueSky Agenda for Reflexive Time Series Analysis](http://arxiv.org/abs/2611.02511v1)
  <details><summary>📄 Abstract</summary>
  Time-series models are increasingly deployed in operational systems (e.g., inventory management and clinical care) where predictions trigger interventions that alter future observations, producing records we term AI-shaped trajectories. This sequence-prediction coupling deepens as such systems evolve into agents that autonomously predict, act, and remember across long horizons. Such AI-shaped trajectories support immediate performance monitoring, but turn ambiguous once reused as passive data. A...
  </details>

- **2026-11-01** — Tian Qin, Yuhang Jiang, Junzhe Chen et al. — [Step-Zero Attack: Agent Safety Before Observability](http://arxiv.org/abs/2611.01953v1)
  <details><summary>📄 Abstract</summary>
  Existing attacks and defenses for coding agents act once content enters the model context: injected text persuades the model, and guards inspect what the model reads. Yet to judge whether processing an unknown archive, network response, or image is safe, an agent often must process it first, and that step can do harm before any content reaches the model. We call this first processing Step Zero, and harm done by it a Step-Zero attack. Across seven harnesses and six models, each agent received onl...
  </details>

- **2026-11-01** — Jiacheng Lu, Qixuan Yang, Tao Song et al. — [CertClaim: Towards Certified Model-Claim Verification for Coding-Agent Services](http://arxiv.org/abs/2611.01950v1)
  <details><summary>📄 Abstract</summary>
  Coding-agent services are priced by the model they claim, making the verification of such model claims crucial for their users. In this paper, we reveal that existing model auditing methods rely on a latent assumption that the deployment is static, i.e., the claimed model is always served in one reference configuration. This assumption does not hold for coding-agent services, whose providers may legitimately change the sampling preset, the reasoning mode or the system prompt without changing the...
  </details>

- **2026-11-01** — Angela John, Hamayoon Behmanush — [Systematic Evaluation of Robustness in Fine-tuned Models](http://arxiv.org/abs/2611.01900v1)
  <details><summary>📄 Abstract</summary>
  Our study systematically evaluates the robustness of fine-tuned pre-trained models across different datasets and attack types, aiming to provide insights for researchers in selecting pre-trained models for image classification tasks while prioritizing robustness against potential attacks. Our work explores the influence of fine-tuning pre-trained models with different datasets and attack types on their robustness and overview of the appropriate pre-trained model for image classification based on...
  </details>

- **2026-11-01** — Avetik Arakelyan, Davit Alaverdyan, Naira Hovakimyan et al. — [Mean Field Game Problem with Kantorovich Potential Coupling: An Attrition model](http://arxiv.org/abs/2611.01616v1)
  <details><summary>📄 Abstract</summary>
  In this work we address a class of Mean-Field Game (MFG) systems on the flat torus $\mathbb{T}^{d}$ in which individual agent incentives arise from macroscopic, distribution-dependent objectives governed by the Wasserstein-2 ($W_{2}$) distance. Taking the first variation (Lions derivative) of the Wasserstein-based macroscopic functional yields a coupled forward-backward system of Hamilton--Jacobi--Bellman (HJB) and Fokker--Planck (FP) equations featuring a nonlocal coupling driven by the Kantoro...
  </details>

- **2026-11-01** — Ziruo Zhao, Jie Fu, Wendy Hui Wang et al. — [Towards Fine-grained and Robust Detection of Human-AI Co-authorship](http://arxiv.org/abs/2611.01427v1)
  <details><summary>📄 Abstract</summary>
  The widespread adoption of large language models (LLMs) is reshaping how textual content is produced, complicating text provenance, and raising concerns for misinformation, plagiarism, and intellectual property. While prior work on AI-generated text detection has progressed, one-dimensional human-AI co-authorship scores lack signals directly relevant to ``AI involvement''. It remains unclear how adversarial paraphrasing distorts detection signals. In this work, we formulate a discrete-class text...
  </details>

- **2026-11-01** — Luca Anzalone — [Reinforcement Learning in High-Energy Physics: A Survey from Accelerator Control to Theory Exploration](http://arxiv.org/abs/2611.02049v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is a machine learning paradigm in which an agent learns a decision-making policy by interacting with an environment, guided by a scalar reward rather than explicit supervision. Supervised and unsupervised learning have become indispensable tools in high-energy physics (HEP), but they learn from fixed datasets, whereas many HEP tasks are closed-loop decisions: the data an algorithm observes depend on its choices, the feedback is sparse or delayed, and the objective is ...
  </details>

- **2026-11-01** — Bradley J Erickson, Sara Salehi — [Zero-shot evaluation of open vision-language models as System 1 decision models on radiology tasks](http://arxiv.org/abs/2611.01631v1)
  <details><summary>📄 Abstract</summary>
  Purpose: We compared two multimodal System 1 decision models, Clef 27B and d1 3B, with a traditional LLM (Qwen 3.8-27B) on seven radiology tasks covering text, radiographs, CT and MRI. Methods: Three models were compared: Clef, Qwen3.8-27B and d1. Three tasks were interpretation of text and 4 were detection of finding in images. The tasks were: 1. finding presence of finding in CT-RATE chest CT reports; 2. Presence of finding in PadChest chest radiograph reports; 3. the same 18 findings on CT-RA...
  </details>

- **2026-11-01** — Lixing Tan, Qing Xia, Yuting Guo et al. — [MoPort: A View-Aware 2D Interface for Motion Language Models](http://arxiv.org/abs/2611.01541v1)
  <details><summary>📄 Abstract</summary>
  Motion language models (MoLMs) encode 3D human motion as discrete tokens for language-based understanding. Deploying them on monocular video raises two problems. Pose detection yields 2D joint sequences, leaving a dimensional gap from the 3D motion used in training. Moreover, the 2D observation changes with the camera viewpoint, while the depth lost in projection makes the 2D pose ambiguous across viewpoints. We propose MoPort, a view-aware 2D interface that enables MoLMs to take 2D observations...
  </details>

- **2026-11-01** — Xiang Zhang, Shijie Song, Wanqing Zhao et al. — [AR-RRG: Anatomy-Guided Retrieval-Driven Radiology Report Generation](http://arxiv.org/abs/2611.01529v1)
  <details><summary>📄 Abstract</summary>
  Radiology report generation (RRG) streamlines clinical workflows and alleviates the burden of radiologists' documentation. Standard vision-language models capture global visual cues and lack fine-grained alignment between anatomical regions and diagnostic text. Most retrieval-augmented methods retrieve complete historical reports, introducing redundant noise and severe vision-text mismatches that trigger clinically risky hallucinations and missed lesions. In this paper, we introduce AR-RRG, an a...
  </details>

- **2026-11-01** — Annan Zhang, Shengjie Song, Wenshuai Yao et al. — [Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning](http://arxiv.org/abs/2611.01411v1)
  <details><summary>📄 Abstract</summary>
  Private fine-tuning of large language models increasingly pairs DP-SGD with low-rank adapters on frozen, quantized backbones, and every such stack inherits one unstated premise: frozen layers keep each record's clipped gradient a function of that record alone. We show that LLM.int8 breaks this premise. It routes outlier activation columns to a higher-precision path using a union over the whole batch, so one record decides how every other record's activations are computed, even though the weights...
  </details>

- **2026-11-01** — Linxiao Li, Haoran Ma, Chenyue Wang et al. — [Toward Executable Multi-framework Front-end Code Generation with Self-Correction](http://arxiv.org/abs/2611.01383v1)
  <details><summary>📄 Abstract</summary>
  Generating codes from UI screenshots has recently benefited from MLLMs, yet existing methods centered on HTML targets and transfer poorly to multi-frameworks such as React, Vue, and Angular. However, unlike HTML, which does not entail compilation issues, generating executable code in multi-framework settings is more challenging due to framework-specific differences in syntax and failure modes, as well as the need to maintain global consistency across files. To address this problem, we study exec...
  </details>

- **2026-11-01** — Jingjun Yi, Chen Hu, Qi Bi et al. — [Lie Routing Vision Language Models for View-Robust 3D Understanding](http://arxiv.org/abs/2611.02306v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have made substantial progress in 3D scene understanding from multi-view RGB observations. Yet a fixed object and query can elicit inconsistent target-related responses across camera viewpoints, a phenomenon we characterize as viewpoint-induced semantic drift. We introduce LieVLM, a Lie routing framework for view-robust 3D understanding. Motivated by the rotational component of viewpoint change, Lie routing adapts visual representations by applying local ...
  </details>

- **2026-11-01** — Muhammad Atif Saeed, Akhtar Jamil, Subhan Ullah — [HQNN-CL: Regime-Aware Hybrid Quantum Neural Network with Continual Learning for Financial Forecasting](http://arxiv.org/abs/2611.02091v1)
  <details><summary>📄 Abstract</summary>
  Financial time-series forecasting is still difficult owing to the non-stationary nature of the market, regime changes, and catastrophic forgetting, which makes conventional deep learning models hard to adapt in the long term. To achieve uncertainty-aware robust financial forecasting in the face of changing market conditions, this study proposes a Hybrid Quantum-Classical Neural Network with Continual Learning (HQNN-CL). The proposed framework combines Gaussian Hidden Markov Model (HMM) based reg...
  </details>

- **2026-11-01** — Mahindra Rautela, Alexander Scheinker — [SensOFormer: Foundation Models for Particle Accelerators](http://arxiv.org/abs/2611.02031v1)
  <details><summary>📄 Abstract</summary>
  Large-scale scientific facilities, such as particle accelerators, are complex systems composed of thousands of interacting components that must operate collectively to support diagnostics and control, and ensure safe, reliable operation. These facilities rely on extensive sensor networks that generate large volumes of heterogeneous, incomplete, and noisy telemetry, often sampled at different rates across subsystems. In this paper, we adopt the foundation-model paradigm to learn general-purpose s...
  </details>

- **2026-11-01** — Liyuan Wang, Xinsong Ma, Ziye Ma — [Query-efficient scan-and-search watermark localization](http://arxiv.org/abs/2611.02030v1)
  <details><summary>📄 Abstract</summary>
  Recently, the detection of AI-generated content has been of particular importance in various fields of our society. For accountability purposes, many large language models (LLMs) have implicitly watermarked their outputs. Localizing such watermarks requires a piece of text to undergo an additional verification process. Existing localization methods typically rely on dense token-level scoring, making verification costly even when an LLM-generated watermark only sparsely appears. To tackle this pr...
  </details>

- **2026-11-01** — Yuntong Hu, Hongji Pu, Zimo Li et al. — [Launder-Bench: Can Repository-Level Agentic Code Laundering Be Detected?](http://arxiv.org/abs/2611.01966v1)
  <details><summary>📄 Abstract</summary>
  Coding agents can now rewrite repository-scale codebases while preserving tested behavior, creating a new challenge for plagiarism detection, license auditing, and software provenance. We ask whether such rewrites can still be traced to their source. Existing clone benchmarks emphasize fragments and bounded edits, while repository-transformation benchmarks evaluate functional correctness rather than provenance. Moreover, ranking the most similar source does not establish derivation when independ...
  </details>

- **2026-11-01** — Ashish Kumar, Prashant Kumar, Mallika Garg — [RCFormer: Reliability-aware Context Transformer for Occlusion-Robust Facial Landmark Detection](http://arxiv.org/abs/2611.01822v1)
  <details><summary>📄 Abstract</summary>
  Facial landmark detection has advanced substantially under regular imaging conditions, yet occlusion, poor illumination, and large pose changes remain major sources of error because local facial evidence can become incomplete or misleading. Context-guided latent patch recovery offers a promising way to address this issue by inferring unreliable patch representations from surrounding facial context before heatmap prediction. However, the recovered context can itself be unreliable when it is weakl...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 52 papers

- **2026-11-03** — Nicolas Waehner, Enzo Tagliazucchi, Jacobo Sitt et al. — [The Platonic Brain: Representational Convergence in EEG Foundation Models](http://arxiv.org/abs/2611.05097v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis (PRH) predicts that artificial neural networks converge on shared representations as scale and performance increase. We test whether these predictions hold for representations of the human brain with EEG foundation models. Using EEG recordings from six participants watching a television series, together with aligned visual and language content, we tested whether EEG foundation-model representations converge within and across modalities as their embeddings b...
  </details>

- **2026-11-03** — Eoin Quinn, Oliver Bent — [Ablating Design Choices for Protein Ensemble Generators Across Structural Regimes](http://arxiv.org/abs/2611.05055v1)
  <details><summary>📄 Abstract</summary>
  Generative models of protein conformational ensembles inherit much of their design from structure prediction for folded proteins. Ordered and disordered proteins, however, occupy distinct structural regimes, and we investigate how design choices hold up across them. Using a minimal C$α$ flow-matching model, we ablate choices of architecture, sequence conditioning, rigid-body alignment and training source, and evaluate each variant against experimental SAXS and NMR chemical-shift data partitioned...
  </details>

- **2026-11-03** — Toygar Tanyel, Serkan Ayvaz — [Whose Effect Is It? How Objectives Inflate Learned Subspace Interventions](http://arxiv.org/abs/2611.05033v1)
  <details><summary>📄 Abstract</summary>
  Interpretability often locates concepts by copying part of a language model's state from one input into another (activation patching). A larger output change counts as stronger evidence that this part carries the concept. Methods that learn which part to copy often change the output more than the whole state does. By that reading, learned parts isolate the concept more cleanly. Yet the whole contains the part. So whose effect is this excess, the network's or the method's? Copying the whole state...
  </details>

- **2026-11-03** — Yu Zhang, Zhihan Wang, Yuhang Lu et al. — [Auditing Multi-Proxy Explanations of Web User Preferences: Identification Boundaries and Abstention](http://arxiv.org/abs/2611.04997v1)
  <details><summary>📄 Abstract</summary>
  Web systems infer user preferences from behavior, ratings, text, and LLM-generated profiles, yet explaining a proxy may reveal its measurement process rather than the preference of interest. We develop an audit framework distinguishing point identification, partial identification, and abstention relative to an explicit reference distribution. Under feature-dependent, arbitrarily signed proxy bias, a strict majority of uncontaminated proxy attributions lets the coordinatewise median recover laten...
  </details>

- **2026-11-03** —  Kling Team, Dong Chen, Jialu Chen et al. — [Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](http://arxiv.org/abs/2611.04916v1)
  <details><summary>📄 Abstract</summary>
  Video generation has progressed from isolated clips to coherent short-form audiovisual sequences, and the bottleneck is shifting from rendering to semantic control. This report summarizes the observations and insights on multimodal understanding gained from successive generations of Kling. We argue that generation quality is the projection of multimodal understanding through the entire data--conditioning--alignment--evaluation chain, and we examine this chain module by module. Kling-MLLM, a shar...
  </details>

- **2026-11-03** — Zichuan Fu, Xian Wu, Jingtong Gao et al. — [Feeling of Knowing in Large Language Models](http://arxiv.org/abs/2611.04834v1)
  <details><summary>📄 Abstract</summary>
  Post-training updates change what large language models (LLMs) can answer, but may leave their answerability judgments misaligned. We study this knowledge-judgment desynchronization through functional feeling of knowing (FoK), which supports selective generation, retrieval triggering, and model routing without implying subjective experience. We propose two trainable channels: a knowledge channel that changes answerability and a FoK channel that judges the current knowledge state. Three stages tr...
  </details>

- **2026-11-03** — Jaemin Choi, Jincheol Yang, Nahyun Lim et al. — [SPA-Q: Structure-Preserving Adaptive Post-Training Quantization for Monocular Depth Estimation](http://arxiv.org/abs/2611.04491v1)
  <details><summary>📄 Abstract</summary>
  Monocular depth estimation (MDE) has advanced rapidly with the emergence of foundation models such as Depth Anything. Their transformer-based architectures provide strong generalization across diverse scenes and domains, but also incur high computational and memory cost, making efficient deployment challenging. Post-Training Quantization (PTQ) provides an efficient and practical solution for model compression, yet low-bit PTQ remains challenging for MDE models. When applying PTQ to Depth Anythin...
  </details>

- **2026-11-03** — Michel Barlaud, Clement Genninasca, Maxime Zanella et al. — [A Parametric Linear Conic Projection for Structured Sparse Attention](http://arxiv.org/abs/2611.04479v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we introduce the Cone Alignment Index (CAI), a scale-invariant sparsity measure associated with a Lorentz-cone geometry. We provide a probabilistic analysis of the distribution of the CAI score, including a general theorem and explicit corollaries for Gaussian and uniform distributions. As a consequence, we show that, in the high-sparsity regime, the probability that the samples lie within the convex cone tends to one. Building upon this formulation, we derive two complementary pr...
  </details>

- **2026-11-03** — Jun Huang, Junyang Zhang, Zijie Yue et al. — [Beyond Token Representations: Explicit Visual Object Grounding for Video Reasoning Segmentation](http://arxiv.org/abs/2611.04472v1)
  <details><summary>📄 Abstract</summary>
  Video Reasoning Segmentation (VRS) aims to infer and segment target objects specified by reasoning queries in videos. Existing methods typically first infer the target and generate a few segmentation tokens for it, which are then fed into a mask decoder for mask prediction. However, such segmentation tokens tend to be both semantically monotonous and spatially ambiguous, making them largely insufficient to represent the target to guide mask prediction. In this paper, we propose an explicit visua...
  </details>

- **2026-11-03** — Mingyu Wang, Si Li, Ziqing Chen et al. — [ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control](http://arxiv.org/abs/2611.04424v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak, which arrives within tens of milliseconds. Learned whole-body policies running at 50 Hz introduce a policy-cycle delay and may suppress a protective withdrawal as a tracking error. To address these challenges, we propose ARC (Ascending Reflex Control), a bottom-up framework that integrates instantaneous tactile reflexes with learned whole-body control. ARC consists of two component...
  </details>

- **2026-11-03** — Hei Yi Mak, Hoang Le, Mehran Taghian Jazi et al. — [Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs](http://arxiv.org/abs/2611.04376v1)
  <details><summary>📄 Abstract</summary>
  In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models. Recent work on FP4 RL has introduced effective recovery recipes that restore accuracy under aggressive low-precision quantization for dense models, but we find that the same approach yields no improvement over the naive FP4 baseline in the MoE setting. We conduct an in-depth study to understand why. Our analysis identifies the root cause in the routing mechanism uni...
  </details>

- **2026-11-03** — Xujia Wang, Yixuan Liu, Shaohan Huang et al. — [Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning](http://arxiv.org/abs/2611.05151v1)
  <details><summary>📄 Abstract</summary>
  Generating HTML from natural-language specifications is an important application of code large language models (LLMs). Despite producing renderable pages, current models often fail to ensure functionality and visual quality during actual interaction. Existing methods typically target task-specific webpage supervision, leaving demanding interactive artifact optimization underexplored. Using mini-games as a challenging testbed, we expose limitations in interaction experience, reward signal, and cr...
  </details>

- **2026-11-02** — Xinbo Zhao, Yuhang Liu, Xin Zhang et al. — [Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning](http://arxiv.org/abs/2611.04031v1)
  <details><summary>📄 Abstract</summary>
  Offline multi-task reinforcement learning (MTRL) aims to learn a unified policy from heterogeneous offline datasets that generalizes across tasks. However, existing offline MTRL methods often struggle with two fundamental issues: severe per-task data scarcity and limited cross-task generalization. In this paper, we propose Language-Model Augmented Decision Transformer (LaMA-DT), a unified sequence-modeling framework that leverages a single large language model (LLM) for both trajectory augmentat...
  </details>

- **2026-11-02** — Xinbo Zhao, Yuhang Liu, Xin Zhang et al. — [Decision Transformer with Task-Aware Representations for Offline Meta-Reinforcement Learning](http://arxiv.org/abs/2611.04010v1)
  <details><summary>📄 Abstract</summary>
  To enable effective generalization in offline meta-RL, it is essential to accurately infer the underlying task through latent task representations, which provide a compact and transferable summary of task-specific characteristics for guiding policy generation. In this paper, we propose Contrastive Task-Aware Decision Transformer (CoTA-DT), a DT-based offline meta-RL framework that learns task representations by jointly integrating four complementary components: (i) contrastive learning from offl...
  </details>

- **2026-11-02** — Xintong Li, Yufen Lin, Yuhua Wu et al. — [A Guideline-Grounded Multi-Agent Framework for Personalized Exercise Prescription from Clinical and Wearable Data](http://arxiv.org/abs/2611.03983v1)
  <details><summary>📄 Abstract</summary>
  Translating population-level exercise guidance into individualized prescriptions requires integrating clinical and wearable data, including diagnoses, medications, functional limitations, and baseline activity, with condition-specific recommendations, a process difficult to scale beyond specialist rehabilitation settings. We developed FITTER, a multi-agent framework that integrates these data with condition-specific guidance to generate personalized FITT-VP prescriptions and applies deterministi...
  </details>

- **2026-11-02** — Nataša Djurdjevac Conrad, Sebastian Pokutta, Christof Schütte — [Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics](http://arxiv.org/abs/2611.03980v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used as synthetic participants in opinion-dynamics experiments, often assuming that an agent's behaviour is fully determined by its prompt. We test this assumption with a framework in which LLM agents discuss a contested policy issue over repeated rounds while their stance is quantified by a fixed psychometric instrument independent of any dynamics model. Across six LLMs, committed personas are intrinsically stable: in each of the five models te...
  </details>

- **2026-11-02** — Maryam Rahimimovassagh, Michael Brown, Sanjeda Sara Jennifer et al. — [One Mistake, Three Layers: Persistence Rules Under Depth Correlation](http://arxiv.org/abs/2611.03968v1)
  <details><summary>📄 Abstract</summary>
  Probing frozen representations layer by layer is now standard practice, but reporting when a signal first becomes decodable requires a rule for reading a depth curve, and the obvious rule is wrong. On synthetic curves with known ground truth, requiring a probe score to exceed a null-calibrated threshold for three consecutive stages reports an onset nineteen stages early under transformer-like depth correlation, with every resample returning an onset. The failure follows from correlation between ...
  </details>

- **2026-11-02** — Yiqiao Qiu — [Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation](http://arxiv.org/abs/2611.02746v2)
  <details><summary>📄 Abstract</summary>
  Multi-teacher on-policy distillation (MOPD) distills several domain experts into one student and is used in the post-training of recent large language models. It trains on all domains at once, so every expert must be available at the same time. In practice, capabilities often arrive one after another, and the experts of earlier domains may be gone when a new domain is learned. Distilling the experts in sequence then suffers from catastrophic forgetting of the earlier domains. Some recent pipelin...
  </details>

- **2026-11-02** — Tengfei Liu, Yang Shi, Yuran Wang et al. — [Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning](http://arxiv.org/abs/2611.03602v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) can generate detailed video captions, yet they may overemphasize minor details while overlooking essential context and key events. We argue that not all visual evidence deserves equal attention, as the importance of visual information depends on the content of each video. Motivated by this observation, we propose Reviso, an agentic video captioning framework that learns what to observe and how to gather relevant visual evidence. From a low-frame-rate glob...
  </details>

- **2026-11-02** — Avni Mittal, Avinash Anand, Dikshant Kukreja et al. — [VIAS: Value-Isolating Activation Steering for Multi-Value Alignment and Compliance for Organisations](http://arxiv.org/abs/2611.03518v1)
  <details><summary>📄 Abstract</summary>
  Organisations increasingly deploy large language model agents that must follow organisational values. We check whether activation steering, which adds vectors to a model's internal activations during generation without changing its weights, can improve compliance beyond prompting alone. Since most scenarios involve several values at once, we focus on multi-value steering. A simple way to build these vectors is to contrast responses that follow all values relevant to a scenario with responses tha...
  </details>

- **2026-11-02** — Puyu Wang, Rui Zhao, Hang Dong — [LODox: A Web-Based Platform for Cultural Heritage Linked Data Discovery](http://arxiv.org/abs/2611.03508v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Large Language Models have transformed how data can be linked, discovered, and enhanced. LODox, Linked Open Data at Oxford, is an evolving web-based platform that embraces this transformation for cultural heritage Linked Open Data. LODox features a novel interface with intuitive card-based data presentation and visualization in a semantic portal. It represents an evolving approach to explore heterogeneous cultural heritage data across multiple sources through a unified interfa...
  </details>

- **2026-11-02** — Berkan Şahin, Ecem İlgün, Klea Zambaku et al. — [In-depth data movement characterization of DNA read mapping algorithms](http://arxiv.org/abs/2611.03400v1)
  <details><summary>📄 Abstract</summary>
  Read mapping algorithms represent a critical bottleneck in genomic analysis pipelines due to the resources required; a problem that is becoming more pronounced as sequencing technologies advance and datasets expand. We present an extensive workload characterization of leading read mapping algorithms across diverse sequencing technologies to identify hardware acceleration and optimization opportunities. We analyzed the following implementations: MashMap, wfmash, and Minimap2 for whole-genome alig...
  </details>

- **2026-11-02** — Chun-An Lin, Yu-Chia Chang, Chi-Mao Fan et al. — [Progressive Multi-Scale Super-Resolution via Cascaded Bicubic Anchors and Inter-Scale Mutual Refinement](http://arxiv.org/abs/2611.03390v1)
  <details><summary>📄 Abstract</summary>
  Super-resolution networks are trained for one magnification factor, so several output resolutions require several models. We propose PMS-SR, a progressive single-input multiple-output network that produces x2, x4, and x8 results in one forward pass, with a Transformer backbone on the low-resolution grid. In Stage 1, each scale is predicted as a residual over the detached bicubic upsampling of the previous scale's prediction. With Dirac and zero initialization, training starts exactly from the bi...
  </details>

- **2026-11-02** — Yuhang Deng, Zheng Chen, Erik G. Larsson — [Non-Coherent Over-the-Air Distributed Consensus: Algorithm Design and Power Control Optimization](http://arxiv.org/abs/2611.03378v1)
  <details><summary>📄 Abstract</summary>
  Non-coherent over-the-air (NCOTA) aggregation offers a scalable and communication-efficient approach to distributed average consensus in wireless networks, without requiring instantaneous channel state information (CSI) or phase alignment. However, persistent aggregation errors pose fundamental challenges in achieving exact average consensus under nominal distributed averaging protocols. In this paper, we develop an NCOTA consensus framework that accommodates row-stochastic mixing, without requi...
  </details>

- **2026-11-02** — Hao Fu, Degang Sun, Wan Wei et al. — [SQLoom: Set-Contrastive Learning of Syntactic, Semantic, and Logical Dependencies for Text-to-SQL](http://arxiv.org/abs/2611.03298v1)
  <details><summary>📄 Abstract</summary>
  Text-to-SQL translates natural language questions into SQL queries, enabling database access without writing SQL. Fine-tuning open-weight large language models (LLMs) is cost-effective, but existing methods treat SQL as ordinary text and optimize token-level likelihood without explicitly modeling its syntactic, semantic, and logical requirements. Thus, a single incorrect alias or comparison operator can invalidate a query while contributing little to training loss. We propose SQLoom, a constrain...
  </details>

- **2026-11-02** — Bolong Feng, Pengfei Zhou, Zhenglin Wan et al. — [R$^2$-Omni: Reducing Structural and Precision Redundancy in Omni-LLMs for Long-Form Generation](http://arxiv.org/abs/2611.03247v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models (Omni-LLMs) typically process large numbers of multimodal tokens from audio-visual inputs, incurring substantial computational costs and a large memory footprint for the key-value (KV) cache. Aggressive token pruning can alleviate this problem while maintaining competitive performance on multiple-choice tasks, which require only a single option as output. However, we observe substantial quality degradation when generating long-form, open-ended responses. We attri...
  </details>

- **2026-11-02** — Marcus Armstrong — [Written Once, Read Differently How Language Models Own Answers Steer Their Next Ones](http://arxiv.org/abs/2611.03198v1)
  <details><summary>📄 Abstract</summary>
  When a language model answers a yes/no question, that answer changes how it answers a different question about the same entity. We study this \emph{self-commitment} in 22 open-weight models from four families (0.5B--72B parameters), fixing the model's first answer and measuring the shift in its second across 3,600 question pairs about 120 entities. Each answer writes a \emph{commitment direction} into the residual stream. The similarity of two questions' directions predicts their coupling on hel...
  </details>

- **2026-11-02** — Renye Yan, Jikang Cheng — [When Optimization Meets Human Intent: Human-Centered Diffusion Model Optimization](http://arxiv.org/abs/2611.03140v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models are evolving from general tools into personalized systems that adapt to user needs through fine-tuning and guidance. However, diffusion optimization mainly targets measurable objectives such as aesthetics, rarely examining whether they align with human intent. Human needs are multidimensional, contextual, and dynamic, whereas existing methods approximate them with fixed metrics. Because these metrics capture human needs only partially and may amplify deviations from true intent ...
  </details>

- **2026-11-02** — Zhicheng He, Xiaohan Xing, Hongqiu Wang et al. — [SurgPace: Complexity-Aware Progressive Distillation for Surgical Multimodal Large Language Models](http://arxiv.org/abs/2611.03125v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have shown strong potential in robotic surgery for question answering, scene understanding, and grounded assistance, but their high computational cost limits real clinical deployment. Knowledge distillation provides a practical way to build compact surgical MLLMs, yet direct distillation is not well suited to surgical data because surgical samples vary greatly in difficulty, visual ambiguity, and required clinical context, making uniform teacher-student t...
  </details>

- **2026-11-02** — Ilias Driouich, Hongliu Cao, Eoin Thomas et al. — [ComplianceAtlas: A Taxonomy-Driven Agentic AI Framework for Automated AI Act Gap Analysis and Remediation](http://arxiv.org/abs/2611.03121v1)
  <details><summary>📄 Abstract</summary>
  Assessing regulatory compliance for high-risk AI systems requires systematic identification of technical gaps such as missing controls, in- adequate processes, or shallow evaluation of practices. Compliance officers typically admin- ister structured questionnaires collecting evi- dence of current practices, where organizations respond with descriptions of their existing pro- cesses, technical capabilities, and architectural choices. However, translating these compli- ance questionnaire responses...
  </details>

- **2026-11-02** — Yi Tan, Beier Zhu, Sirui Chen et al. — [RouteREPA: Routed Representation Alignment for Just Image Transformers](http://arxiv.org/abs/2611.02941v1)
  <details><summary>📄 Abstract</summary>
  Representation alignment (REPA) is widely used to accelerate the training of latent-space diffusion transformers (DiTs). However, applying it to pixel-space models such as Just Image Transformers (JiT) is challenging. Our analysis reveals a pronounced representation conflict between discriminative alignment and pixel-space generation. Compared with its latent counterpart, JiT learns representations that are substantially less aligned with DINOv2. Applying REPA to JiT consistently reduces the rec...
  </details>

- **2026-11-02** — Yi Tan, Beier Zhu, Sirui Chen et al. — [Unlocking the Potential of Contrastive Regularization for Diffusion Transformer Training](http://arxiv.org/abs/2611.02921v1)
  <details><summary>📄 Abstract</summary>
  Representation regularization has emerged as an effective way to improve diffusion transformer training. Yet one of the most canonical regularizers--InfoNCE-style contrastive learning--remains largely underexplored in this setting. We naturally ask a question: can standard contrastive learning serve as an effective regularizer for diffusion transformers? Surprisingly, we find that naive InfoNCE regularization brings only marginal gains. Our analysis reveals that the objective is easily dominated...
  </details>

- **2026-11-02** — Lukáš Zezulka, Zdeněk Nováček, Martin Konečný et al. — [A plug-and-play platform for self-aligning 3D-printed structures on optical fibers](http://arxiv.org/abs/2611.02850v1)
  <details><summary>📄 Abstract</summary>
  Two-photon polymerization 3D printing advances optical fibers into complex lab-on-fiber devices. However, widespread adoption remains bottlenecked by the inherent inefficiencies of sequential, direct-on-fiber printing. To address this, a custom-designed modular platform and a corresponding fiber-decoupled fabrication methodology on planar substrates are presented. This platform features a compliant, spring-like socket that enables passive self-alignment and reversible fiber insertion, paired wit...
  </details>

- **2026-11-02** — Yunzhi Zhuge, Xinzhuo Yu, Sitong Gong et al. — [Unlocking the Potential of Vision Foundation Models for Multi-Task Dense Prediction via Mixture of Task Adapters](http://arxiv.org/abs/2611.02769v1)
  <details><summary>📄 Abstract</summary>
  Multi-task dense prediction seeks a single, coherent representation that supports simultaneously discriminative semantic recognition and regularized geometric/structural inference. For vision foundation models, pretrained semantic invariances conflict with the frequency and smoothness biases of dense objectives; joint fine-tuning and single-route adapters therefore compress competing gradients into one update channel, causing negative transfer and unstable cross-task agreement. We frame this as ...
  </details>

- **2026-11-02** — Mingchuan Ma, Dongqi Cai, Daqian Yang et al. — [Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute](http://arxiv.org/abs/2611.02688v1)
  <details><summary>📄 Abstract</summary>
  LLM pretraining is increasingly compute-intensive, while substantial inference serving compute remains idle during off-peak periods. However, such serving hardware is difficult to use for conventional first-order training due to its memory, networking and other system requirements. Zeroth-order (ZO) optimization offers a natural interface to this forward-only compute resource, but its gradient estimates break down in pretraining. Unlike fine-tuning, which can confine updates to a small parameter...
  </details>

- **2026-11-02** — Alice Driessen, Emil Malmsten, Steffen Wolf et al. — [HistoTx: Early fusion of H&E images and spatial transcriptomics at varying spatial transcriptomics resolution with self-supervised learning](http://arxiv.org/abs/2611.02681v1)
  <details><summary>📄 Abstract</summary>
  Spatial transcriptomics maps gene expression across tissue sections and, when integrated with whole slide images, jointly captures both morphological architecture and molecular activity to provide a rich, multimodal view of tissue biology. ML approaches combining spatial transcriptomics and WSIs typically learn a mapping from morphological features to molecular profiles via contrastive alignment or supervised fine-tuning of pathology foundation models. In both cases, transcriptomics serves as a ...
  </details>

- **2026-11-02** — Jingping Wang, Zhanhao Li, Shao Zhang et al. — [UPSHIFT: User Preference Steering from Human-AI Interaction Feedback Traces](http://arxiv.org/abs/2611.02667v1)
  <details><summary>📄 Abstract</summary>
  Personalizing large language model assistants requires adapting their responses to individual users, including the selection of content, reasoning approach, level of detail, and form of presentation. Such preferences are often latent, becoming visible only when users respond to an initial answer and request revisions. We investigate whether these feedback trajectories can be converted into a reusable personalization signal without explicit preference profiles or labels, prompt-time access to int...
  </details>

- **2026-11-02** — Peipei Jiao, Mingkang Liu, Weiming Meng et al. — [Parallelism-Aligned Pruning and Round-Aware Context Reuse for On-Device Multimodal Agents](http://arxiv.org/abs/2611.02601v1)
  <details><summary>📄 Abstract</summary>
  On-device multimodal agents are limited by two deployment mismatches: pretrained attention structures may not divide evenly across the compute cores of an edge accelerator, causing irregular partitions; and standard prefix caching keeps historical visual tokens in the persistent KV cache, whose capacity grows with the number of rounds. We present PARC, which combines parallelism-aligned structured pruning with lifetime-aware KV-cache reorganization. At the model level, it uses first-order Taylor...
  </details>

- **2026-11-02** — Xueqi Ma, Yanbei Jiang, Xingjun Ma et al. — [Towards Multi-Value Alignment via Value Localization in LLMs](http://arxiv.org/abs/2611.02503v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) with multiple, potentially conflicting human values remains challenging, as existing multi-objective alignment methods often require costly fine-tuning and provide limited insight into the internal mechanisms underlying value-related behaviors. In this work, we investigate multi-value alignment from a mechanistic interpretability perspective by identifying value-sensitive attention heads (value heads) in LLMs. Using a probing-based value localization framewo...
  </details>

- **2026-11-02** — Mehedi Hasan Shanto, Md. Anaytul Islam, Muhammad Asaduzzaman et al. — [Toward an Evidence-Based Template for Agent Instruction Files: An Empirical Study of Adoption, Consistency, and Maintenance](http://arxiv.org/abs/2611.02383v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents rely on repository-level instruction files to understand project conventions, development workflows, and constraints. However, different agents support different instruction formats, and limited empirical evidence exists about how these files are adopted, what information they contain, whether coexisting formats provide consistent guidance, and how they are maintained. We conduct an empirical study of 3,387 instruction files from 1,000 GitHub repositories across four formats: AG...
  </details>

- **2026-11-02** — Ziqi Pang, Yu-Xiong Wang — [Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning Strategies in RLVR](http://arxiv.org/abs/2611.03627v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) can enable generalizable improvement for large language model (LLM) reasoning. This paper studies how to incentivize such generalization via reasoning strategies. We study this question with a controllable equation-solving framework: finding multiple inputs x for equations f(x)=y, where f is a non-bijective string function. This setting makes reasoning strategies observable while supporting a clear definition of easy-to-hard out-of-distributi...
  </details>

- **2026-11-02** — Qian Cheng, Ruize Tang, Saad Mohammad Rafid Pial et al. — [TLAPS-Bench: Formally Proving Correctness of Real-World System Specifications with TLA+ Proof System](http://arxiv.org/abs/2611.02849v1)
  <details><summary>📄 Abstract</summary>
  TLAPS-Bench is a benchmark and execution harness for constructing machine-checked proofs for real-world system specifications in TLA+ with agentic AI. Proving correctness of complex system specifications requires discovering inductive invariants, reasoning about intricate state transitions, and decomposing proofs into tractable obligations. TLAPS-Bench provides a proof harness that supports iterative proof development atop the TLA+ Proof System (TLAPS), where agents are equipped with proof tools...
  </details>

- **2026-11-02** — Kunjun Li, Wenhao Chai, Yihao Liang et al. — [SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding](http://arxiv.org/abs/2611.02501v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass. However, it remains unclear whether their released systems (stock) attain the full speedup that parallel drafting permits. We identify three challenges. First, with one request, each step accepts few tokens but reads every target weight. Second, with batching, per-request verification work roughly halves the speedup over a...
  </details>

- **2026-11-02** — Zixiao Wang, Duzhen Zhang, Xingbo Du et al. — [Forecasting How RLHF Responds to Reward-Model Edits Before Training](http://arxiv.org/abs/2611.03244v1)
  <details><summary>📄 Abstract</summary>
  Responses with headers, lists and greater length receive high scores from reward models (RMs), and RLHF policies learn to produce these features even when true quality does not improve. Practitioners therefore edit their RMs, but they learn whether an edit works only after an RL run. We show that the response of a policy to an RM edit can be forecast before training, from samples of the current policy and the scores of the old and new RM. If we read the RM as a set of prices, the first-order the...
  </details>

- **2026-11-01** — Jae Oh Woo, Mengdie Flora Wang, Rahul Ghosh et al. — [Can LLMs Reliably Evaluate Themselves? A Probabilistic VC Framework](http://arxiv.org/abs/2611.02253v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) find increasing use in critical applications, evaluating their ability to assess their own outputs has become crucial. We present a theoretical and empirical framework that examines whether LLMs can differentiate between correct and incorrect solutions while maintaining properly calibrated confidence. Building on classical Vapnik-Chervonenkis (VC) theory, we adapt it to probabilistic predictors through two complexity metrics: Probabilistic VC (PVC), which measures...
  </details>

- **2026-11-01** — Kevin Baum, Ruta Binkytė, Gerrit Großmann et al. — [Rewarded for Not Getting Caught: Why Alignment Training Selects for Conditional Compliance and Cannot Instill Norms](http://arxiv.org/abs/2611.02162v1)
  <details><summary>📄 Abstract</summary>
  Current alignment training cannot be expected to deliver what it is meant to deliver: AI agents that comply with norms whatever the gains and whether or not anyone is watching. Training that rewards and penalizes behavior can teach norms only through that reward, and a reward can encode a norm only as a price: "do not do X" becomes "doing X costs something", and training charges the cost only when X is noticed. A price, unlike a norm, can be paid: a large enough gain outweighs it, noticed or not...
  </details>

- **2026-11-01** — Ruisheng Sun, Jiaqi Shao, Weijia Han et al. — [Towards Self-Evolving Narrative Systems: Real-Time Adaptation and Long-Term Optimization with LLMs](http://arxiv.org/abs/2611.01954v1)
  <details><summary>📄 Abstract</summary>
  Traditional interactive narrative systems offer strong authorial control and structural coherence but often restrict player agency. In contrast, LLM-driven narratives enable open-ended generation and greater flexibility, yet frequently suffer from inconsistency and diminished narrative control. To navigate this trade-off, we propose a hybrid narrative framework that dynamically balances pre-authored content with real-time LLM generation via semantic similarity alignment. Additionally, sustaining...
  </details>

- **2026-11-01** — Farhad Mehran, Charles Turyagyenda, Dritan Kaleshi — [Interoperability Assessment of Fronthaul and E2 Interfaces for Multi-Vendor Open RAN Systems](http://arxiv.org/abs/2611.01862v1)
  <details><summary>📄 Abstract</summary>
  Open Radio Access Networks (RANs) aim to transform the existing wireless network architectures by adopting open interfaces, disaggregating and virtualising RAN components, and enabling dynamic control of the system via data-driven methods. To accelerate the development of interoperable RAN solutions, rigorous assessment of Open Fronthaul and E2 interfaces based on O-RAN Alliance Interoperability Testing (IOT) specifications plays a key role as the integration of these interfaces seems to be very...
  </details>

- **2026-11-01** — Yongqi Shan, Yifan Wang, Yunzhi Zhuge et al. — [MMCoT$^3$: Empowering 3D Scene Understanding with 3D-Text Interleaved Multi-Modal Chain-of-Thought Reasoning](http://arxiv.org/abs/2611.01676v1)
  <details><summary>📄 Abstract</summary>
  Understanding and reasoning over 3D scenes from point clouds is essential for a broad range of AI applications. Recent 3D large language models have shown promising results, yet they still face two fundamental limitations: (i) insufficient capability for grounded multi-step reasoning in complex 3D scenes, and (ii) a text-centric inference paradigm that lacks effective interaction between textual reasoning and visual evidence. As a result, these models often fail to verify intermediate inferences...
  </details>

- **2026-11-01** — Tuc Nguyen, Marcos Gutiérrez-del-Pozo, Eduardo Paluzo-Hidalgo et al. — [TopoSteer: Topological Layer Selection for Activation Steering in LLMs](http://arxiv.org/abs/2611.01493v1)
  <details><summary>📄 Abstract</summary>
  Activation steering controls large language models at inference time by adding a vector to their internal representations. Most work asks how to build that vector, and far less attention has gone to where to add it, even though steering at a poorly chosen layer can be worse than not steering at all. Prior selectors choose a layer without ever steering the model to test it: they score how separable the target behavior is at that layer, and how consistently the individual examples point along the ...
  </details>

- **2026-11-01** — Ahmed Sameh, Gayal Kuruppu, Neeraj Wagh et al. — [ERIA: An Instruction-Optimized Agent for Clinical EEG Reporting](http://arxiv.org/abs/2611.01394v1)
  <details><summary>📄 Abstract</summary>
  Clinical EEG interpretation requires integrating technical quality, background and behavioral states, interictal and ictal abnormalities, and overall clinical context across long recordings. We introduce ERIA (EEG Reporting and Instruction-Optimized Agent), a locally deployable framework in which a single 27B language-model controller analyzes whole-recording EEGs by orchestrating specialized parametric and signal-processing tools. ERIA combines learned tools for background abnormality, sleep-wa...
  </details>

- **2026-11-01** — Panayiotis Christou, Shuwen Kan, Ying Mao — [A GPU-Accelerated and Geometry-Aware Quantum-Classical Framework for Optimized PES Scans with CUDA-Q](http://arxiv.org/abs/2611.01389v1)
  <details><summary>📄 Abstract</summary>
  Hybrid quantum-classical workloads, particularly Potential Energy Surface (PES) scans in quantum chemistry using batched VQE and QAOA, involve many structurally similar Hamiltonians differing only in coefficients. Existing warm-start and meta-optimization strategies reuse parameters between instances but still consume fixed quantum-classical resources, ignoring cross-instance structural similarities. We present OptiPESS, a GPU-accelerated runtime system for adaptive resource allocation in hybrid...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 58 papers

- **2026-11-03** — Hong Je-Gal, Jinwoo Kim, Chanbin Yi et al. — [LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](http://arxiv.org/abs/2611.04974v1)
  <details><summary>📄 Abstract</summary>
  We investigate the automated generation of executable robot reinforcement learning (RL) policies from natural-language task descriptions. Rather than using large language models (LLMs) as execution-time decision makers, we use them as designers that construct RL pipelines before deployment, including Markov decision process (MDP) formulation and simulator implementation. We identify a phase-wise structure in this problem: MDP formulation is dependency-structured and sequential, whereas simulator...
  </details>

- **2026-11-03** — Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal et al. — [PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs](http://arxiv.org/abs/2611.04948v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling (TTS) improves generative models by allocating additional inference-time computation to sampling, search, and verification. Existing image generation approaches, however, typically rank completed images or image-centric intermediate states. We study TTS for parallel multimodal discrete diffusion language models, in which reasoning tokens and image tokens are decoded jointly within a single generation trajectory. We first diagnose a limitation of conventional final-image selecti...
  </details>

- **2026-11-03** — Shresth Grover, Andrey Kolobov, Dhruv Shah — [RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training](http://arxiv.org/abs/2611.04368v1)
  <details><summary>📄 Abstract</summary>
  Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions. We introduce reasoning-aligned fine-tuning (RAFT), a two-stage post-training procedure: RAFT first trains low-rank adapters on task-relevant reasoning annotations, then freezes them while fine-tuning the policy on action demonstrations. On a physical DROID robot, RAFT achieves $75....
  </details>

- **2026-11-03** — Yang Chen, Bin Wen, Danyang Peng et al. — [DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?](http://arxiv.org/abs/2611.04228v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal agents have shown promising progress in embodied planning and web interaction. However, existing evaluations often rely on simplified tasks with limited combinatorial structure, leaving it unclear whether current agents can robustly integrate perception and reasoning for multi-goal planning under temporal, physical, and multimodal constraints. We introduce DualWorldBench, a unified benchmark for evaluating agent planning under controlled symbolic--temporal and grounded--topolog...
  </details>

- **2026-11-03** — Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb — [LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs](http://arxiv.org/abs/2611.04217v1)
  <details><summary>📄 Abstract</summary>
  Predicting stock returns requires modeling persistent company relations and time-varying market signals. Graph Neural Network (GNN) approaches combine static priors with dynamic relational graphs, but treat every extracted edge as a trustworthy binary fact, ignoring heterogeneous reliability across relational sources. We propose LENS (LLM-Extracted priors and News-driven Semantics), a static--dynamic graph framework for stock return prediction and ranking that models relational reliability as a ...
  </details>

- **2026-11-03** — Hang Chen, Jiaying Zhu, Wenya Wang — [Unifying and Beyond the Theory of Pervasive Capability Degradation in LLM Post-training SFT from Feature Interference](http://arxiv.org/abs/2611.05003v1)
  <details><summary>📄 Abstract</summary>
  Pervasive Capability Degradation (PCD) refers to the phenomenon in which supervised fine-tuning (SFT), while adapting a large language model (LLM) to a target task, often erodes the general capabilities acquired during pre-training. Prevailing explanations attribute PCD to macroscopic distribution shift and therefore lack microscopic manipulability, leaving existing mitigation methods without a complete theoretical foundation. In this paper, we first develop a bottom-up geometric theory of PCD g...
  </details>

- **2026-11-03** — Byungkun Lee, Minho Park, Hojoon Lee et al. — [All-For-One: Distilling Visual Foundation Models to a Fast, Memory-Efficient Visuomotor Policy](http://arxiv.org/abs/2611.04485v1)
  <details><summary>📄 Abstract</summary>
  Visual Foundation Models (VFMs) provide semantic cues such as depth and segmentation useful for robotic manipulation, but directly deploying them in closed-loop control is impractical due to high computational cost, temporal inconsistency, and distribution shift between static internet images and egocentric robot observations. We propose All-For-One (AFO), a two-stage distillation framework that leverages VFMs strictly as privileged information during training, using downstream robotic data. Fol...
  </details>

- **2026-11-03** — Kamal Mammadov, Glen Pearce, Helen Krause et al. — [Distributed Marginal Return: A Communication-Efficient Algorithm for Multi-Agent Weapon Target Assignment](http://arxiv.org/abs/2611.04370v1)
  <details><summary>📄 Abstract</summary>
  The Weapon-Target Assignment (WTA) problem in distributed multi-agent systems is challenged by limited situational awareness and communication constraints. Existing distributed methods, such as auction-consensus algorithms, typically assume task-value independence, a simplification that fails to capture the coupled effects of multi-weapon assignments. This paper introduces the Distributed Marginal Return (DMR) algorithm, a novel decentralized approach that generalizes auction-consensus framework...
  </details>

- **2026-11-03** — Afshin Khadangi — [Going Deeper With Memories](http://arxiv.org/abs/2611.05255v1)
  <details><summary>📄 Abstract</summary>
  Byte level language models avoid tokenizer dependence and provide universal coverage, but processing every byte at full resolution is expensive. We introduce DeepMem, a causal multiscale architecture that separates semantic compression from exact byte preservation. A learned invertible subband transform constructs a hierarchy of shorter sequences, while a lossless carrier and explicit detail sidebands preserve byte identity. Fast weight memory blocks operate along the encoder, with iterative sha...
  </details>

- **2026-11-03** — Alex Mwololo Kimuya, Mary Mwadulo, Dickson Mwenda Kinyua — [The Novelty Horizon H_N: Why Large Language Models Fail to Generate Scientific Data beyond Their Training Distribution](http://arxiv.org/abs/2611.05175v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) lack physical grounding and extrapolation. This paper formalises the Novelty Horizon as tasks needing extrapolation beyond training support, causal reasoning absent from learned correlations, or post-frontier information. A forensic analysis tests LLMs on unguided, guided, and ground-truth data from an underrepresented diode-clamped short-circuit experiment using temporal, spectral, and statistical validation against a first-principles Modified Ohm's Law. Both script...
  </details>

- **2026-11-03** — Manthan Patel, Jonas Frey, Pascal Roth et al. — [WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation](http://arxiv.org/abs/2611.05129v1)
  <details><summary>📄 Abstract</summary>
  Web services provide walking directions for nearly every city, but following them reliably over long routes remains challenging for autonomous robots. Point-goal navigation policies rely heavily on accurate GNSS, while most vision-language navigation models struggle to execute even short instructions outdoors. We present WayTrace, a hierarchical system that connects web-map directions to robot motion through language. An off-the-shelf orchestrator vision-language model reads the turn-by-turn dir...
  </details>

- **2026-11-03** — Javeria Javed, Ahmed Salim, Muhammad Mahboob Ur Rahman — [Label-Preserving Fourier Domain Adaptation with Generative-AI and Real Style Donors for 3D Mitral Valve Segmentation](http://arxiv.org/abs/2611.05106v1)
  <details><summary>📄 Abstract</summary>
  Accurate segmentation of the mitral valve from three-dimensional transesophageal echocardiography (3D TEE) is severely restricted by the scarcity of publicly available expert- annotated volumetric datasets. To address this critical limitation, we investigated Fourier Domain Adaptation (FDA), utilizing general-purpose generative-AI images (from platforms like Chat- GPT, Google Gemini, and Microsoft MAI) as annotation-free style donors for 3D mitral valve segmentation. We employed a DeepMitral res...
  </details>

- **2026-11-03** — Aboubaker Seddiq Benterki, Jüri Vain, Gert Kanter et al. — [ALBI: LLM-Guided Inductive Logic Programming via Iterative Generate-Test-Constrain Refineme](http://arxiv.org/abs/2611.05039v1)
  <details><summary>📄 Abstract</summary>
  We introduce ALBI (Agent for Learning By Induction), a neuro-symbolic ILP framework that replaces the ASP-based hypothesis generator in the Learning from Failures (LFF) paradigm with a Large Language Model (LLM), while retaining SWI-Prolog as a formal verifier. ALBI implements an iterative generate-test-constrain loop: the LLM proposes candidate hypotheses from structured prompts; Prolog tests each candidate; and diagnostic feedback drives refinement. We further introduce semantic anonymization,...
  </details>

- **2026-11-03** — Amna Irshad, Luca Antonelli, Vitaly Petrov et al. — [Joint Channel Scanning and Geometry-Aware Codebook Design for Movable Antenna Arrays](http://arxiv.org/abs/2611.04918v1)
  <details><summary>📄 Abstract</summary>
  Multiple-input multiple-output (MIMO) systems rely on spatial degrees of freedom, but fixed antenna geometries cannot adapt to propagation environments. Movable antenna (MA) systems address this by adapting antenna positions to the channel. In discrete MA architectures, active antennas are selected from candidate positions, requiring channel state information (CSI) at those positions. With limited radio-frequency (RF) chains, CSI is acquired through successive pilot rounds, or antenna scanning, ...
  </details>

- **2026-11-03** — Matteo Romilio Pasqual, Matteo Tomasetto, J. Nathan Kutz et al. — [Fault-tolerant shallow recurrent decoders for sparse sensing with missing sensor measurements](http://arxiv.org/abs/2611.04893v1)
  <details><summary>📄 Abstract</summary>
  Real-world sensing systems are inherently imperfect: sensors may fail, intermittently disconnect, operate with asynchronous sampling rates, and be subject to noise, leading to measurement streams that are irregular, incomplete, and heterogeneous. Nevertheless, sensing strategies for real-time state reconstruction typically assume synchronous and continuously active sensors, a constraint that substantially limits their applicability in operational environments. In this work, we introduce fault-to...
  </details>

- **2026-11-03** — Sierra Bonilla, Fengyi Jiang, Chinedu Nwoye et al. — [iMED: A Multi-Endoscope Dataset for Surgical 3D Perception](http://arxiv.org/abs/2611.04755v1)
  <details><summary>📄 Abstract</summary>
  We introduce iMED, the first synchronized multi-endoscope dataset for robot-assisted minimally invasive surgery (RAMIS), designed to address a fundamental limitation in surgical vision benchmarking: the absence of independent held-out viewpoints. Existing surgical datasets capture single-trajectory sequences from a single endoscope, making it impossible to distinguish geometric generalization from photometric interpolation along a narrow forward-facing path. iMED provides 340 sequences ~170K syn...
  </details>

- **2026-11-03** — Michel Olvera, Paraskevas Stamatiadis, Ga{ë}l Richard — [Confidence-Aware Aggregation for Multimodal Audio Reasoning](http://arxiv.org/abs/2611.04580v1)
  <details><summary>📄 Abstract</summary>
  Large Audio Language Models (LALMs) enable generative reasoning over complex acoustic scenes but often exhibit prediction instability. We show that this variability can serve as a reliability metric via inference-time self-consistency and confidence-aware aggregation. Using a log-probability--based scoring framework, candidate answers are weighted by model likelihoods, leveraging reasoning diversity and self-certainty without additional training. Experiments on four LALMs, including Qwen3-Omni a...
  </details>

- **2026-11-03** — Anna Gogleva, Thomas Charman, Martin Balla et al. — [Treating the Symptom, Missing the Cause: Anatomy of a Scientific Reasoning Failure](http://arxiv.org/abs/2611.04473v1)
  <details><summary>📄 Abstract</summary>
  Scientific agents can find interventions that work without understanding why they do. We study this failure mode in controlled synthetic regulatory systems, where agents must experimentally identify a hidden fault and rescue the resulting phenotype. Across seven LLMs, every model restores the healthy phenotypes more often than it identifies the fault. Claude Opus 4.6 and Sonnet 4.6 rescue every organism while diagnosing only 55% and 35% of them. This failure is not simply due to insufficient exp...
  </details>

- **2026-11-03** — Zongxi Liu, Hongyang Du — [WiSI: Wireless-in-the-Loop Self-Improvement](http://arxiv.org/abs/2611.04437v1)
  <details><summary>📄 Abstract</summary>
  The growing autonomy of AI agents has enabled self-improvement, where agents iteratively refine their programs through execution feedback and performance evaluation. As these agents increasingly operate in physical environments and rely on wireless connectivity, communication conditions become an integral part of their improvement process. However, existing approaches largely assume ideal communication, overlooking how wireless conditions shape both the feedback that guides program modifications...
  </details>

- **2026-11-03** — Tengju Ru, Weitong Lian, Zecong Tang et al. — [VidUEU-Agent: A Data-Curation Agent for Multimodal Understanding, Editing, and Unified Tasks](http://arxiv.org/abs/2611.04418v1)
  <details><summary>📄 Abstract</summary>
  The advancement of multimodal learning is heavily constrained by the scarcity and high annotation cost of high-quality instruction data. While raw videos offer an abundant and dynamic source of visual knowledge, transforming them into precise instruction data remains highly challenging. To bridge this gap, we present VidUEU-Agent, an automated pipeline that synthesizes instruction data from raw videos for multimodal understanding, editing, and unified tasks. VidUEU-Agent follows a four-stage pip...
  </details>

- **2026-11-03** — Yangze Liu — [Silent Instrument Errors Reorder Agent Leaderboards](http://arxiv.org/abs/2611.04399v1)
  <details><summary>📄 Abstract</summary>
  On a public agent leaderboard, a general-purpose agent trails a scaffold built for an airline customer-service benchmark by 13 points on the tasks that touch its database, and a reader could conclude that generality costs accuracy. The gap comes from the grader. The general agent often ends its conversations in a way that never triggers grading, so only about half of its episodes were scored and the rest were stored as failures. Grading the ungraded half under the benchmark's own rule closes the...
  </details>

- **2026-11-03** — Shabab Sabiq, Progga Biswas Parama — [FinTech Adoption, Bank Profitability, and Stability: The Mediating Role of Operational Cost Efficiency in Bangladesh's Commercial Banking Sector](http://arxiv.org/abs/2611.04298v1)
  <details><summary>📄 Abstract</summary>
  While financial technology (FinTech) is seen as a contributor to bank performance, the empirical evidence of digitization's ability to translate into improved profit and stability outcomes and efficiency gains, within emerging systems dominated by banks is not conclusive. The direct impact of a composite FinTech Adoption Index (FTI) on the profitability (ROE) and stability (ln(Z-score)) of Bangladesh's commercial banks is explored in this study along with whether operational cost efficiency (CIR...
  </details>

- **2026-11-03** — Renkai Yi, Yuwei Wu, Haoyu Zhang et al. — [DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](http://arxiv.org/abs/2611.04226v1)
  <details><summary>📄 Abstract</summary>
  Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful. A recovery system must therefore choose a response suited to the current state. We present DiMuRe (diagnosis-guided multilevel recovery), a framework for robot-use agents that uses phase-specific evidence and method preconditions to select program reuse or predefined recovery skills, including bounded vision-language-action (VLA) grasping. After the original program exi...
  </details>

- **2026-11-02** — Lianmin Chen, Junbin Qiu, Chenxing Wei et al. — [The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning](http://arxiv.org/abs/2611.03260v2)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization has emerged as a promising approach for memory-efficient large language model (LLM) post-training, yet its reliability in reinforcement learning with verifiable rewards (RLVR) remains largely unexplored. Motivated by the distinct data regimes of on-policy RL and fixed-data optimization, we develop a generic variance-theoretic framework to investigate what limits the reliability of ZO gradient estimation. Our analysis reveals that estimation reliability is structura...
  </details>

- **2026-11-02** — Zhiwei Zhang, Wenxuan Yuan, Xiaoyuan Cheng et al. — [When Latent Dynamics Meet Data Assimilation: A Benchmark of Koopman-Type Representations](http://arxiv.org/abs/2611.03916v1)
  <details><summary>📄 Abstract</summary>
  Koopman representations describe nonlinear dynamics through linear evolution in a transformed space, offering an attractive framework for their linear simplicity and generality. Yet these advantages do not necessarily translate into improved performance in deep latent data assimilation (LDA). We systematically compare seven representative methods and structural baselines across five systems spanning approximately periodic to strongly chaotic dynamics and a broad range of state dimensions. We eva...
  </details>

- **2026-11-02** — Lianmin Chen, Junbin Qiu, Chenxing Wei et al. — [The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning](http://arxiv.org/abs/2611.03260v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization has emerged as a promising approach for memory-efficient large language model (LLM) post-training, yet its reliable application to reinforcement learning with verifiable rewards (RLVR) remains largely unexplored. Motivated by the distinct data regimes of on-policy RL and fixed-data optimization, we develop a generic variance-theoretic framework to investigate what limits the reliability of ZO gradient estimation. Our analysis reveals that estimation reliability is ...
  </details>

- **2026-11-02** — Jackson Petty, William Merrill, Ashish Sabharwal — [A Fine-Grained Hierarchy and Benchmark for State Tracking in Language Models](http://arxiv.org/abs/2611.03094v1)
  <details><summary>📄 Abstract</summary>
  Theoretical limitations of transformers on state tracking---the ability to track information about entities or variables over long contexts---have motivated new recurrent language modeling (LM) architectures such as Gated DeltaNet (GDN). These architectures have, in particular, been benchmarked against the $S_5$ word problem, a theoretically hard state-tracking task that captures abilities such as code evaluation under arbitrary variable assignment. It, however, remains open whether other, simpl...
  </details>

- **2026-11-02** — Fengxian Ji, Xie Yu, Zhexuan Cui et al. — [PRIME: Predictive Routing of Interventions by Modeling Effects for Scientific Ideation](http://arxiv.org/abs/2611.03055v1)
  <details><summary>📄 Abstract</summary>
  Feedback-driven iteration is widely used to improve LLM-generated scientific ideas, but existing systems either leave revision decisions implicit in generation, align revisions with feedback-localized weaknesses, or restrict action selection to system-specific operations. This is problematic because problems, hypotheses, and solutions are interdependent: the location where a weakness manifests does not itself determine the revision scope that will produce a better successor. We term this phenome...
  </details>

- **2026-11-02** — Polina Fedorinina, Anna Fattakhova, Nadezhda Romanova et al. — [Is your LLM an Agressive Narcissist with Depression? Analyzing Psychological Portraits of Large Language Models](http://arxiv.org/abs/2611.02757v1)
  <details><summary>📄 Abstract</summary>
  Nowadays, interaction with AI requires caution not only regarding the factual reliability of generated content but also regarding personality markers that models may implicitly transmit during dialogue that can subtly influence users' perception of information. In this paper, we conduct a large-scale experimental study in which 22 large language models complete 11 psychological inventories. Furthermore, we investigate correlations between human and model responses to track the adjustments made f...
  </details>

- **2026-11-02** — Prabhpreet Singh Setia, Bhavesh Neekhra, Debayan Gupta — [Widening Harm Evaluation Coverage with a Judge that Reads the World](http://arxiv.org/abs/2611.02624v1)
  <details><summary>📄 Abstract</summary>
  An agent acting in a stateful environment can leave evidence of harm in two places: the record of what it did and said, or the world it changed. Safety evaluations for discovering harm examine one or the other in limited ways, using either an LLM judge over the trajectory or deterministic checks over the final state. Although LLM-based verifiers that inspect the environment exist, they have been used to verify task completion, not to detect and confirm harm in a safety setting. We address this g...
  </details>

- **2026-11-02** — Qianyue Chen, Jinghua Wang, Daimeng Shang et al. — [On Modelling the Scattering of Highly Nonlinear Transient Water Waves Due to Surface-Piercing Cylinder. Part I: Formulations and Verifications](http://arxiv.org/abs/2611.02369v1)
  <details><summary>📄 Abstract</summary>
  The presence of extreme ocean waves poses substantial threats to the safety of marine engineering applications and navigational activities. Accurate prediction of the nonlinear wave loads on offshore structures in large-diameter cylindrical configuration, such as monopile wind turbines and platform columns, requires a robust solution to the high-order wave diffraction problem. This paper introduces a novel, highly nonlinear time-domain numerical pseudo-spectrum model based on potential flow theo...
  </details>

- **2026-11-02** — Rileigh Bandy, Teresa Portone, Mohammad Khalil et al. — [Efficient Closure Learning in Dynamical Systems: A Comparison of Data-Assimilated and Embedded Approaches](http://arxiv.org/abs/2611.03612v1)
  <details><summary>📄 Abstract</summary>
  Increased computing power has transformed computational science and improved predictive capabilities for complex systems, but many phenomena still exceed current simulation capabilities or require rapid evaluations for fast design iterations. Closure models address this challenge by approximating unresolved effects in reduced or incomplete dynamical systems. Data-driven closures offer a flexible mechanism for improving model accuracy and applicability, but approaches that embed the closure withi...
  </details>

- **2026-11-02** — Dorian Zeilinger, Felix Engertsberger, Herbert Egger — [Structured Neural Network Models for Anisotropic Magnetic Constitutive Laws](http://arxiv.org/abs/2611.03475v1)
  <details><summary>📄 Abstract</summary>
  High-performance electrical steel used for iron cores of power transformers and generators exhibits complex material behavior. While modeling and simulation of isotropic nonlinear response is well understood, the incorporation of magnetic anisotropy remains challenging. This work proposes to utilize a structured neural network architecture to systematically describe the anisotropic nonlinear anhysteretic magnetic material response of electrical steel sheets. By constructing a convex and smooth c...
  </details>

- **2026-11-02** — Jeel Piyushkumar Khatiwala, Divyangkumar Patel, Dianxiang Xu et al. — [A Symbolic-Neural Framework for Context-Aware Evidence Extraction from Mobile SQLite Databases](http://arxiv.org/abs/2611.03323v1)
  <details><summary>📄 Abstract</summary>
  Reliable forensic evidence extraction from mobile SQLite databases is challenging because application schemas are undocumented, evolve across releases, and differ across operating systems, making schema-specific methods brittle and difficult to maintain. We present SNEEF, a symbolic-neural framework for context-aware evidence extraction that encodes each SQLite row as context-value pairs with standardized provenance metadata and column labels, uses a language model to recognize nine forensic ent...
  </details>

- **2026-11-02** — Vasiliki Vasileiou, Panagiotis P. Filntisis, Petros Maragos et al. — [ReVA-HPE: Relative 6DoF Head Pose Estimation with Synthetic Pose Supervision and Personalized Virtual Anchors](http://arxiv.org/abs/2611.03283v1)
  <details><summary>📄 Abstract</summary>
  Monocular head pose estimation is usually formulated as absolute regression from a single face crop, yet many applications observe the same person over time and can supply an explicit anchor image. Recently, relative head pose estimation was proposed, which casts the problem as estimation of the relative geometric change between an anchor and a query image. However, existing methods still require the anchor image pose to be known at inference, significantly limiting their practical use. We first...
  </details>

- **2026-11-02** — Marcos Antonio Obando, Tianyuan Wang, Tanja Tarvainen et al. — [Bayesian Sequential Optimal Experimental Design for Single-Pixel Imaging using Reinforcement Learning](http://arxiv.org/abs/2611.03042v1)
  <details><summary>📄 Abstract</summary>
  Adaptive compressed sensing (CS) aims to select the most informative measurements sequentially, which is crucial for many modern imaging systems. This task can be formulated as a Bayesian sequential optimal experimental design (sOED) problem, where each new acquisition is chosen to maximally reduce uncertainty about the unknown image given prior information and subsequent data provided by acquisitions. However, in single-pixel imaging (SPI), the large design space consists of all possible binary...
  </details>

- **2026-11-02** — Xuanren Chen, Chongyang Tao, Wenpeng Hu et al. — [BLPO: Beyond-Local Policy Optimization for Long-Horizon LLM Agents](http://arxiv.org/abs/2611.03005v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon tasks require large language model (LLM) agents to coordinate interdependent actions, a capability central to automating complex workflows. Stepwise group-based reinforcement learning provides finer credit than trajectory-level supervision, but reliable comparisons must account for differences in interaction history. Enforcing this consistency within the limited rollouts of each task can leave insufficient support for estimating action preferences. We propose Beyond-Local Policy Opt...
  </details>

- **2026-11-02** — N'Dah Jean Kouagou, Pritilata Saha, Caglar Demir et al. — [NIR: Approximate Neural Instance Retrieval for ALCIQ](http://arxiv.org/abs/2611.02842v1)
  <details><summary>📄 Abstract</summary>
  Instance retrieval is the main bottleneck of concept-learning systems based on refinement operators. We present NIR, a family of neural instance retrievers for ALCIQ that output graded membership scores from knowledge graph embeddings. We compare tokenization-based encoders (GRU, LSTM, Transformer) with a Compositional encoder that mirrors DL operators via primitive sub-networks. On eight benchmarks, all variants approximate Pellet closely on complete knowledge bases, while the Transformer model...
  </details>

- **2026-11-02** — Jinlei Zhang, Zixuan Zhang, Hao Qiu et al. — [Discovering hierarchical governing equations for community-structured complex network dynamics with LLM agents](http://arxiv.org/abs/2611.02816v1)
  <details><summary>📄 Abstract</summary>
  Governing equations provide an interpretable description of the mechanisms underlying complex network dynamics, yet their discovery from observational data remains challenging when shared community-level dynamics coexist with individual-level variations and the relevant functional structures may be absent from the initial candidate library or not explicitly specified in advance. Here we formulate this task as a hierarchical law-discovery problem and introduce SAGE, a large language model-guided ...
  </details>

- **2026-11-02** — Jules Clerc, Domitile Lourdeaux, Mohamed Sallak et al. — [Creating Hybrid Interactive Narrative Systems with LLM: From Formal Description to Evaluation](http://arxiv.org/abs/2611.02807v1)
  <details><summary>📄 Abstract</summary>
  Interactive narratives let users shape a story while an Experience Manager (EM) keeps it coherent, balancing player freedom against authorial control. Large Language Models now enable a new generation of hybrid EMs, which combine run-time generation from free-text input with symbolic narrative control. However, their heterogeneity makes them hard to compare: A manager's behaviour is generally tied to the unique and specific scenario in which it operates, and much of its decision-making takes pla...
  </details>

- **2026-11-02** — Jinming Ge, Shang Liu, Jiawei Liang et al. — [HLSClaw: Bringing Vibe Coding to High-Level Synthesis through Skill-Based Agentic Harness](http://arxiv.org/abs/2611.02784v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are rapidly shifting software development toward intent-driven \emph{vibe coding}, yet their effectiveness drops sharply in high-level synthesis (HLS), where code optimization must jointly consider design structure, directive search, and downstream hardware constraints. Existing HLS optimization approaches, including both heuristic-based methods and recent LLM-assisted pipelines, typically operate at fixed abstraction levels or in weakly coupled stages, limiting their ability to lever...
  </details>

- **2026-11-02** — Fanyu meng, Zhaodan Kong, Xin Liu — [Chain of Faith: Policy-Internal Rewards for Reasoning Reliance](http://arxiv.org/abs/2611.02672v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) explanations can sound plausible while having little influence on a model's final answer. We study four rewards that use the policy's own signals to encourage reliance on generated reasoning: gradient sensitivity, confidence gaps, progressive confidence gains, and reasoning--prompt swaps. We add each reward to group relative policy optimization (GRPO) and evaluate two small instruction-tuned models on GSM8K and StrategyQA using reasoning edits, paraphrases, and prompt hint...
  </details>

- **2026-11-02** — Adam M. Krajewski, Ricardo Amaral, Jonathan W. Siegel et al. — [Data-driven candidate structure ensemble generation beyond the convex hull with crystALL approach](http://arxiv.org/abs/2611.02584v1)
  <details><summary>📄 Abstract</summary>
  Real materials consist of multiple stable or metastable states under real-world conditions, existing as statistical ergodic ensembles of configurations rather than ideal crystals. Yet, data-driven computational materials discovery increasingly biases itself toward finding "new stable structures" from ground-state DFT calculations alone. This limits our long-term ability to discover materials whose properties emerge from metastable phases, to explain experimental observations, or to model thermod...
  </details>

- **2026-11-02** — Wangshu Cai, Jun Zhou, Lei Wang et al. — [Latent Spectral Prompting for Multimodal Hyperspectral Object Tracking](http://arxiv.org/abs/2611.02512v1)
  <details><summary>📄 Abstract</summary>
  Hyperspectral videos provide rich spectral signatures for robust tracking under challenging conditions such as camouflage and low illumination. However, limited hyperspectral annotations and the large RGB-hyperspectral domain gap hinder the direct use of modern temporally pretrained RGB trackers. We propose SProTrack, a multimodal framework that transfers temporal knowledge from pretrained RGB trackers to the hyperspectral domain through latent spectral prompting. The key idea is to decouple tem...
  </details>

- **2026-11-02** — Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer et al. — [Beyond Accuracy: How Quantization Affects Coding Agents](http://arxiv.org/abs/2611.02368v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly used for coding tasks, but the inference cost of large language models (LLMs) limits where they can run. Quantization reduces model size, but its effects on coding agents that execute and revise programs remain underexplored. We compare BF16 with 4-bit AWQ and GPTQ for Qwen2.5-Coder-Instruct (7B, 14B, and 32B) and Devstral-Small-2507 (24B) on OJBench coding problems across three seeds. We detect no statistically significant accuracy loss for any of the coding agents. Howe...
  </details>

- **2026-11-02** — Getuar Rexhepi, Kuranage Roche Rayan Ranasinghe, Giuseppe Thadeu Freitas de Abreu et al. — [Joint PAPR Reduction and Over-the-Air Computing in Multi-User OFDMA Systems](http://arxiv.org/abs/2611.02343v1)
  <details><summary>📄 Abstract</summary>
  We consider the peak-to-average power ratio (PAPR) reduction challenge of orthogonal frequency division multiplexing (OFDM) systems utilizing tone reservation (TR) under an over-the-air computing constraint, such that the signals placed in the reserved tones simultaneously enable distributed computation at the receiver. To that end, the problem is cast as a fractional programming problem and solved via the iterative quadratic transform (QT), which guarantees convergence to a stationary point. A ...
  </details>

- **2026-11-01** — Jae Oh Woo, Mengdie Flora Wang, Rahul Ghosh et al. — [Calibration-Constrained Diagnostics for Evaluating LLM Self-Evaluation](http://arxiv.org/abs/2611.02253v2)
  <details><summary>📄 Abstract</summary>
  We introduce a reusable evaluation artifact for diagnosing whether LLM self-reported confidence can support confidence-gated act-or-defer decisions. The artifact is designed for evaluation rather than safety certification: it provides a black-box protocol, prompts, judge-reference labels, model outputs, reproduction scripts, and calibration-constrained diagnostic metrics for auditing LLM self-evaluation across math, factual, and commonsense reasoning tasks. Our central finding is that aggregate ...
  </details>

- **2026-11-01** — Sowjanya Karanam, Jayanth Bhargav — [Metamorphic Testing for Evaluating Robustness of Sentiment Analysis Models](http://arxiv.org/abs/2611.02248v1)
  <details><summary>📄 Abstract</summary>
  Machine learning systems are challenging to test using traditional software testing methods because their behavior is learned from data rather than explicitly programmed. This challenge is particularly significant in natural language processing (NLP), where small input variations can lead to unexpected model behavior. Conventional evaluation metrics, such as accuracy and F1-score, often fail to capture such inconsistencies. Metamorphic testing addresses this limitation by evaluating expected rel...
  </details>

- **2026-11-01** — Habibur Rahaman, Daniel Lobo, Md Rezoan Ferdous et al. — [SANAI: Secure ECC Distributed Keyed Parity Embedded in Weights for Protecting Neural Networks against Bit-Flip Attacks](http://arxiv.org/abs/2611.02042v1)
  <details><summary>📄 Abstract</summary>
  Quantized neural networks store weights in dense memory, where bit flips caused by voltage scaling, aging, radiation, or deliberate attacks such as RowHammer can severely degrade model behavior. A single corrupted high-order bit can cause misclassifications or nonsensical language-model outputs. Embedded error-correcting codes (ECC) avoid dedicated parity storage by hiding parity within model weights, but existing schemes embed uniformly across layers and bit planes, leave parity unsecured, and ...
  </details>

- **2026-11-01** — Youran Wang, Devodita Chakravarty, Yiwei Lyu — [When to Probe and When to Act: Clarity-Aware Risk-Adaptive Control for Interactive Driving](http://arxiv.org/abs/2611.02240v1)
  <details><summary>📄 Abstract</summary>
  Safe navigation in interactive traffic requires autonomous vehicles to reason about unobservable human characteristics and the reciprocal nature of multi-agent interactions. Traditional architectures often decouple prediction from planning, leading to the "Frozen Robot Problem" or unsafe maneuvers under high ambiguity because they treat risk assessment and information acquisition as independent objectives. We argue that the notion of safety should not remain static but must instead dynamically c...
  </details>

- **2026-11-01** — Liangkai Liu, Bimal Thapa Magar — [When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem](http://arxiv.org/abs/2611.02101v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models now act in a closed loop, yet their safety is evaluated one variation at a time: robustness benchmarks perturb the scene while assuming instantaneous inference, and real-time execution methods study inference delay in nominal scenes. We argue that physical safety is not a property of the model alone, but emerges from how variations in the physical environment, the model, the computing platform, and execution interact in closed loop. We formalize this as cross-layer variat...
  </details>

- **2026-11-01** — Muyuan Ma, Shuo Jiang, Lijun Han et al. — [Recursive Self-Improvement of Exoskeleton Assistance Policies through Human-in-the-Loop Feedback](http://arxiv.org/abs/2611.01581v1)
  <details><summary>📄 Abstract</summary>
  To reduce reliance on manual design and extensive parameter tuning, a framework for the autonomous evolution of exoskeleton assistance policies through human feedback is proposed. Assistance policies are autonomously generated as executable control code by an intelligent agent and evaluated in experiments with human participants. Subjective user feedback, movement performance, and muscle activation measurements are incorporated into policy assessment. Based on these assessments, policy deficienc...
  </details>

- **2026-11-01** — Amir Hossain Raj, Xuesu Xiao — [SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts](http://arxiv.org/abs/2611.01600v1)
  <details><summary>📄 Abstract</summary>
  Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space. Reactive policies often miss these hidden constraints, while exhaustive search becomes computationally prohibitive in dense clutter. We present SCOUT, an occlusion-aware planning framework that bridges high-level deliberation with grounded physical rollouts. SCOUT leverages an object-centric scene representation to reconstruct hidden...
  </details>

- **2026-11-01** — Takuro Shimaya, Ryosaku Shino, Masahiro Saiko — [Peripheral prototypical contrastive loss for supervised medical image segmentation](http://arxiv.org/abs/2611.02305v1)
  <details><summary>📄 Abstract</summary>
  Robust segmentation of biomedical images remains challenging primarily due to ill-defined object boundaries. Although several loss functions have recently been proposed to enhance object boundary recognition, concerns remain about the susceptibility to unstable annotations resulting from boundary ambiguities. Here, we introduce the Peripheral Prototypical Contrastive (PPC) loss, which leverages prototypical contrastive learning to improve boundary recognition and enable stable training even unde...
  </details>

- **2026-11-01** — Yvon Apedo, Martyna Poreba, Michal Szczepanski et al. — [SVD-Prune: Spectral Vision Token Pruning under Extreme Compression](http://arxiv.org/abs/2611.02284v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models process hundreds of visual tokens, making visual representations a major computational bottleneck. We argue that visual token pruning should be formulated not as identifying individually important tokens, but as preserving the dominant low-rank spectral structure of the visual representation. Based on this formulation, we introduce SVD-Prune, a training-free framework that leverages Singular Value Decomposition (SVD) and stati...
  </details>

- **2026-11-01** — Geonwoo Cho, Jaegyun Im, Doyoon Kim et al. — [ANCHOR: KL-Anchored Adaptation for Stable Offline-to-Online RL](http://arxiv.org/abs/2611.02177v1)
  <details><summary>📄 Abstract</summary>
  Offline-to-online reinforcement learning (RL) follows the pretrain-finetune paradigm: an agent is first pretrained on historical data and then adapted through online interaction. We study offline-to-online adaptation without offline replay, where the agent must improve using only the pretrained model and newly collected experience. A key challenge is to avoid catastrophic failure, a sharp early performance collapse during online fine-tuning, while still achieving strong asymptotic performance. T...
  </details>

- **2026-11-01** — Franco Corti, Sajid Siraj — [How Green Is Your Manifesto? Scoring Environmental Positions in the 2024 EU Elections with an LLM Panel](http://arxiv.org/abs/2611.02033v1)
  <details><summary>📄 Abstract</summary>
  Locating political parties on environmental and climate policy is central to the study of party competition, yet the established instruments, expert surveys and the hand coding of manifestos, are costly, periodic, and slow to extend to new documents. We ask whether a panel of large language models can serve as a cheaper and reproducible alternative. Treating each manifesto as a set of sentences, three models from independent providers score every sentence on two dimensions, environmental protect...
  </details>

- **2026-11-01** — Philipp Nazari, Neehal Tumma, Daniela Rus et al. — [Quantizing Recurrent Language Models Is Easier Than You Think](http://arxiv.org/abs/2611.01864v1)
  <details><summary>📄 Abstract</summary>
  Linear recurrences are becoming an increasingly common building block in large language models, replacing the growing KV cache of softmax attention with a fixed-size recurrent state that enables efficient decoding. However, the quantization stack has largely been developed around softmax Transformers, whose numerical properties and inference state differ from those of recurrent models. Our goal is to understand these differences and study the design space of quantization methods for recurrent mo...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 16 papers

- **2026-11-03** — Qinghua Mao, Xi Lin, Yuxin Qi et al. — [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](http://arxiv.org/abs/2611.04289v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented Web applications increasingly employ multi-agent debate (MAD) to aggregate conflicting, noisy, and heterogeneous information, yet deliberation is fundamentally a social process susceptible to interpersonal dynamics. When retrieved Web sources contain latent hazards alongside safe factual content, social biases such as conformity pressure and authority deference can override evidence-grounded safety boundaries. In this work, we investigate whether the social structure of delib...
  </details>

- **2026-11-03** — Ali Imran, Abdalwhab Bakheet Mohammed Abdalwhab, Rafael Gomes Braga et al. — [Reality and Perceptual Gaps in Expressive Swarm Robotics](http://arxiv.org/abs/2611.05244v1)
  <details><summary>📄 Abstract</summary>
  Moving robot swarms from simulation into the physical world can be difficult because small discrepancies in hardware, timing and communication can cascade across interacting robots and alter group behaviour. This challenge is known as the reality gap. When swarms operate in human environments, a second challenge emerges: a perceptual gap between what the swarm physically does and what human onlookers actually perceive. This study examines the same decentralised coordination code deployed across ...
  </details>

- **2026-11-03** — Shivin Dass, Kevin Nguyen, Rohan Yelandur et al. — [GUILD: Guided Iterative Data Collection for Imitation Learning](http://arxiv.org/abs/2611.05368v1)
  <details><summary>📄 Abstract</summary>
  Imitation learning policies in robotics are trained on datasets collected through costly real-world teleoperation. Often, the data-collection process is unguided, relying on the teleoperator's intuition, resulting in data that contributes little to overall policy performance. Recent work has shown that curating such unguided datasets can substantially improve policy performance, but these approaches operate by filtering existing datasets after collection and therefore do not prevent the acquisit...
  </details>

- **2026-11-03** — Zhen Tao, Xun Zhou, Xuhui Chen et al. — [HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation](http://arxiv.org/abs/2611.05319v1)
  <details><summary>📄 Abstract</summary>
  In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone. Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup. We recast LLM-based recommendation as an agentic-communication process in four stages: BUILD a self-description, TRANSMIT it along the collaborative graph, UNDERSTAND the other side, and SYNC it from the next interaction. This formulation reve...
  </details>

- **2026-11-03** — Krzysztof Rogowski, Marcin Dziubiński — [Search and Verification for Strategyproof Facility Location on Metric Graphs](http://arxiv.org/abs/2611.05092v1)
  <details><summary>📄 Abstract</summary>
  We study automated design of strategyproof (SP) mechanisms for randomized facility location on continuous metric graphs, with the objective of minimizing total distance. We develop methods for computing upper and lower bounds on the optimal approximation ratio achievable by SP mechanisms for a given graph and number of agents.   For the lower bound, we propose a cost-preserving reduction to a finite domain that yields lower bounds for unrestricted SP mechanisms through linear programming dual ce...
  </details>

- **2026-11-03** — Junfeng Wang, Jiawei Liu, Yongchao Xu et al. — [Learning Where to Look: Observation Policy Optimization for Thinking with Images](http://arxiv.org/abs/2611.04943v1)
  <details><summary>📄 Abstract</summary>
  Complex visual question answering often requires vision-language models to think with images, i.e., actively acquire local visual evidence by zooming into informative regions of high-resolution images. Our error analysis shows that many failures in this setting originate from incorrect observation actions, where the model fails to localize key regions or obtain crops that contain sufficient evidence for answering. We further observe that bounding-box tokens exhibit substantially higher generatio...
  </details>

- **2026-11-03** — Xuwei Tan, Jingchun Huang, Ming Cai et al. — [CogniLife: Continuous Cognitive Distillation for Deployed Multi-Expert Agent Marketplaces](http://arxiv.org/abs/2611.04483v1)
  <details><summary>📄 Abstract</summary>
  Multi-expert agent marketplaces -- where creators publish domain-specific AI experts for end users to consult -- are an emerging deployment pattern for language technology. A published expert can receive many requests yet little evidence about its creator, who remains active elsewhere: the cold-expert problem. We frame continuous cognitive distillation as converting attributed creator observations into revisable decision rules, communication patterns, and domain procedures. CogniLife proposes a ...
  </details>

- **2026-11-03** — Liang Lin, Jianguo Zhu, Gang Lei et al. — [Large Language Models for Forecasting of Electricity Price Spikes](http://arxiv.org/abs/2611.04354v1)
  <details><summary>📄 Abstract</summary>
  Can market notices read by a large language model (LLM) improve short-horizon electricity price spike forecasts? We study five regions of Australia's National Electricity Market. A local LLM extracted features once per notice, only notices visible at the forecast origin were used, and a gradient-boosting model produced onset probabilities. In an out-of-sample development back-test (July 2022 to July 2024), notice features did not lower the 60-minute Brier score of a numeric model including the m...
  </details>

- **2026-11-02** — Marcel Müller, Mohammad Ghazi Vakili, Yoshihiro Ogura et al. — [El Agente Fármaco: A Scalable AI Scientist for Drug Discovery](http://arxiv.org/abs/2611.03832v1)
  <details><summary>📄 Abstract</summary>
  Computational drug discovery offers a growing range of tools for proposing and evaluating molecules, but combining them and deciding what to do next still requires substantial expert effort. Here, we introduce El Agente Fármaco, an AI scientist that uses modern large language model (LLM) technology to turn discovery goals expressed in everyday language into complex, scalable computational screening workflows. The agentic harness selects scientific tools, reviews their results, and adjusts subseq...
  </details>

- **2026-11-02** — Michael Barasa Murunga, Allan Vikiru — [A Human-Verified AI Workflow for Annotating Environmental Sound Data](http://arxiv.org/abs/2611.03271v1)
  <details><summary>📄 Abstract</summary>
  Large-scale annotation of environmental sound recordings presents significant challenges under time and resource constraints, particularly when sound categories are imbalanced and only part of a dataset has been labeled. This paper describes the development and evaluation of a human-AI workflow used during annotation of the Kenya Forest Sounds Dataset (KFSD), using a project-stage working collection of 7,531 audio recordings across 21 categories. We investigated zero-shot classification, a featu...
  </details>

- **2026-11-02** — Yanbei Jiang, Chao Lei, Rena Gao et al. — [CARE: Grounded Recursive Self-Improvement for Production Customer-Service Agents](http://arxiv.org/abs/2611.02839v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) in production agents involves transforming accumulated experience into reliable model updates while adapting to evolving business policies. We present CARE (Customer-service Agent Retrospective and Evolve), a grounded RSI framework that operationalizes this process in customer service. Its goal is to replace a frontier proprietary incumbent with an in-house mid-sized model that continues learning after deployment. After a one-time cold start on governed productio...
  </details>

- **2026-11-02** — Jingxuan Wei, Song Tan, Xiaohan Liu et al. — [FindLink: Learning to Assess Scientific Connections from Source-Grounded Premises](http://arxiv.org/abs/2611.02545v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery from the literature requires assessing connections among findings obtained under different study conditions. Source attribution makes individual findings traceable, but does not determine what they jointly support. We introduce GI-TraceBench, a benchmark of 10,282 questions in gastrointestinal oncology that unifies provenance question answering, knowledge discovery, and hypothesis evaluation through shared Paper, Claim, and Evidence Span records. We further propose FindLink,...
  </details>

- **2026-11-02** — Zexin Zhong, Yanjun Zhang, Yulei Sui et al. — [APG: Agentic Static-Analysis Infrastructure on LLVM-IR Graph Databases](http://arxiv.org/abs/2611.02349v1)
  <details><summary>📄 Abstract</summary>
  LLM-based coding agents increasingly rely on external program knowledge, yet access to static-analysis graphs alone does not ensure appropriate operation selection or evidence interpretation. We present APG, an infrastructure for semantics-grounded static program analysis. Built on SVF and LLVM, it decomposes compiler-derived program analyses into atomic capabilities that LLM agents can select, compose, and orchestrate for goal-directed, cross-graph investigation, with query safeguards and evide...
  </details>

- **2026-11-02** — Farnoush Rezaei Jafari, Tristan Lazard, Kenza Bouzid et al. — [Attribution-based diagnostics for single-cell foundation models](http://arxiv.org/abs/2611.02335v1)
  <details><summary>📄 Abstract</summary>
  Single-cell RNA foundation models (scFMs) are increasingly used for in-silico biological discovery, yet predictive performance alone does not reveal whether their decisions rely on biologically meaningful signals or model-specific shortcuts. We systematically investigate post-hoc attribution of downstream predictions across two tasks: cell-type annotation using pretrained Cell2Sentence and scGPT models, and perturbation prediction using scGPT+STATE in a controlled setting. For cell annotation, w...
  </details>

- **2026-11-01** — Xingyu Yi, Xinya Zhang, Yunshen Zhou et al. — [From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents](http://arxiv.org/abs/2611.01527v1)
  <details><summary>📄 Abstract</summary>
  A scientific agent can give the same verdict while reading and citing different evidence. BioAgent-DF tests this separation using paired reference and candidate values saved at the same scientific computation site. It restores or transplants those values at their original coordinates, then runs the agent on healthy hardware. Across eight SciFact batches, Qwen3.5-4B shows repeatable citation changes in three capture-claim combinations, and Gemma 3 4B IT shows repeatable read and citation changes ...
  </details>

- **2026-11-01** — Danyal Sarfraz, SeEun Lee, Ulugbek Vahobjon Ugli Ismatullaev et al. — [Capable but Not Scalable: Requirements and Interaction Costs of Building Multi-View CAD Datasets for Design Research](http://arxiv.org/abs/2611.02108v1)
  <details><summary>📄 Abstract</summary>
  Transforming CAD models into consistent multi-view image datasets is increasingly important for AI-driven product design research, yet existing workflows can impose substantial burdens on researchers without programming expertise. We examine this challenge from a human-computer interaction (HCI) perspective by analyzing ten reported rendering practices and deriving fourteen requirements spanning dataset quality, visual consistency, and user interaction. We then assess eleven development- and des...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-11-03** — Tamunotonye Harry, Yuanyuan Feng — [Personas Are Not People: Identity as State, Not Attribute](http://arxiv.org/abs/2611.05292v1)
  <details><summary>📄 Abstract</summary>
  Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person is defined by a persona, a written profile of fixed traits, demographics, and attitudes that a language model is instructed to act out. Every such system assumes that a person's identity is a stable attribute that behaves the same way in every situation the simulation presents. We show that this ass...
  </details>

- **2026-11-03** — Wen Zhou, Shaowen Wang, Upmanu Lall et al. — [Fusing Earth observation embeddings and spaceborne terrain with meteorological forcing for flood peak depth prediction from high-water marks](http://arxiv.org/abs/2611.05220v1)
  <details><summary>📄 Abstract</summary>
  Flood peak depth on normally dry land governs damage and risk to life, but is observed only sparsely, by post-event high-water mark (HWM) surveys, and depth derived from satellite flood extent is produced after the event and inherits the vertical error of the digital elevation model (DEM) it is computed from. Deep-learning flood models have in turn been trained on hydrodynamic simulations rather than on observed depths. We ask whether flood peak depth can be learned from field observations and p...
  </details>

- **2026-11-02** — Jiawei Ran, Yuxia Zhang, Ziyang Zhao et al. — [IssueLighter: An Issue Type-Aware LLM Agent for Issue Report Validity Assessment](http://arxiv.org/abs/2611.02721v1)
  <details><summary>📄 Abstract</summary>
  Invalid issue reports are prevalent in open source software (OSS) projects, imposing substantial burdens on maintainers who already face a high risk of burnout. Prior research has primarily focused on identifying invalid reports for specific issue categories (e.g., bug and wontfix), leaving the broader landscape of OSS issue types largely unexplored and limiting the generalizability of existing approaches. Moreover, existing methods provide little support for explaining or validating their predi...
  </details>

- **2026-11-01** — Haosong Wang, Ting Tan, Yao Li et al. — [The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys](http://arxiv.org/abs/2611.01988v1)
  <details><summary>📄 Abstract</summary>
  Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data los...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 202 papers

- **2026-11-03** — Hongyin Luo, Wei Fang, Lijie Yang et al. — [Adversarial Speculative Reasoning Improves Long Horizon Agents](http://arxiv.org/abs/2611.05345v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this view does not hold true for long-horizon agent reasoning. Measuring frontier open-weight models on complex agentic tasks with different speculative decoding approaches, we found that numerical noise grows within verific...
  </details>

- **2026-11-03** — Hui Xuan Tan, Stefanos Chaliasos, Alastair F. Donaldson — [Proving the Wrong Program: Miscompilations as a Threat to zkVM Guarantees](http://arxiv.org/abs/2611.04701v1)
  <details><summary>📄 Abstract</summary>
  A zero-knowledge virtual machine (zkVM) lets an untrusted prover convince a verifier that a program, typically Rust compiled to RISC-V, ran correctly. The proof covers the compiled binary, so a miscompilation can make a correct zkVM produce a valid proof of a computation that differs from the developer's source. We present the first empirical study of miscompilation as a threat to zkVM guarantees, on the production zkVMs SP1 and Jolt. We assemble 88 known rustc and LLVM miscompilations with Rust...
  </details>

- **2026-11-03** — Andrea Cenzato, Lukas Karch, Andre Luckow et al. — [Ground-Wing: A Parametric 3D Wing-in-Ground-Effect Dataset for Benchmarking Neural Surrogate Models](http://arxiv.org/abs/2611.04571v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a CFD dataset of a highly parametrized 3D wing operating in ground effect, designed for benchmarking neural surrogate models for aerodynamic prediction, using a wing shape and flow conditions typically encountered in motorsport applications. The dataset comprises 770 RANS simulations of 194 unique wing configurations, sampled across 27 airfoil profile variants and 4 distances from the ground, spanning variations in wing sweep, chord, taper, angle of attack, and tip twist. Six...
  </details>

- **2026-11-03** — Ivan Martinez-Kay, Tatiana Kardashina, ShiNung Ching et al. — [A Bayesian Optimized Biquad Filter-Burg Model for Real-Time EEG Phase Estimation](http://arxiv.org/abs/2611.05374v1)
  <details><summary>📄 Abstract</summary>
  Real-time phase estimation on stimulus-aligned transient EEG is critical for closed-loop neuromodulation systems targeting the theta-band, yet most real-time phase estimation methods have been developed and validated on resting-state, high-fidelity signals in the alpha band. Recent work has pursued deep learning architectures, while individualized classical bandpass filter tuning remains underexplored. This study characterizes the spectral and temporal properties of non-anticipative bandpass fil...
  </details>

- **2026-11-03** — Austin Tsai, Saurav Nanda, Ganapathy Parthasarathy et al. — [Aligning Language Models with General Preferences: An Empirical Study of Direct Nash Optimization](http://arxiv.org/abs/2611.05373v1)
  <details><summary>📄 Abstract</summary>
  Direct Nash Optimization (DNO) aligns a language model to a general preference function by approximating the Nash equilibrium of a two-player preference game. Its practical variant, DNO-Prct, iterates on-policy sampling, LLM-based rating of the samples together with a teacher's gold response, large-margin preference-pair selection and a DPO-style contrastive update. We re-implement DNO-Prct independently and study it on two open-weight instruct models, Llama 3.1 8B Instruct and Mistral 7B Instru...
  </details>

- **2026-11-03** — Piper Wolters, Gabriel Tseng, Favyen Bastani et al. — [PLANTEUR: A Crop-Type Segmentation Benchmark for Tropical Regions](http://arxiv.org/abs/2611.05223v1)
  <details><summary>📄 Abstract</summary>
  We introduce PLANTEUR, a benchmark for crop-type mapping from satellite images in the French overseas territories. Building on the PASTIS design, PLANTEUR provides georeferenced and aligned Sentinel-2, Sentinel-1, and Landsat-8 sequences with parcel-derived labels spanning six tropical regions and an 8-class label space. We define both a standard test split and a leave-one-island-out protocol to measure cross-territory generalization, and evaluate fully supervised models, linear probes, and fine...
  </details>

- **2026-11-03** — Abhijeet M. Kulkarni, Saimouli Katragadda, Yuze Du et al. — [Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture](http://arxiv.org/abs/2611.04972v1)
  <details><summary>📄 Abstract</summary>
  By harnessing the inherent commonsense capabilities of pretrained Large Language Models (LLMs) and Vision-Language Models (VLMs), current Vision-Language Action(VLA) models for legged robots excel at interpreting language-based navigation commands but lack the physical grounding and explicit safety assurance required for real-world operation. Therefore, this paper aims to cage Legged-Vision-Language Navigation (VLN) through a safety architecture that provides physical grounding and ensures navig...
  </details>

- **2026-11-03** — Jianye Xu, Yousef Sayed, Bassam Alrifaee — [Safeguarding Multi-Agent Reinforcement Learning for Connected and Automated Vehicles with Recursively Feasible Control Barrier Functions](http://arxiv.org/abs/2611.04957v1)
  <details><summary>📄 Abstract</summary>
  Multi-Agent Reinforcement Learning (MARL) shows promise in coordinating connected and automated vehicles but offers no safety guarantee. Although Control Barrier Functions (CBFs) can add this guarantee, their optimization problem can become infeasible in practice due to control bounds. Moreover, they often overapproximate vehicle and road geometry, which makes them conservative. This paper proposes the Backup-Horizon CBF (BH-CBF), which evaluates safety along a horizon until all vehicles stop. B...
  </details>

- **2026-11-03** — Travis Davies, Wentao Ma, Lihao Guo et al. — [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)
  <details><summary>📄 Abstract</summary>
  A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon rollouts. We present PrimeSim, an action-conditioned, multiview world model simulator that addresses these challenges through progressive midtraining and posttraining. Starting from a pretrained video generator, we midtrain on 30,110 hours of robot demonstrations spanning 22 platforms. ...
  </details>

- **2026-11-03** — Minghao Kong, Muyao Chen, Jianhao Wu et al. — [CardioVascBench:Prioritized Diagnosis Generation from Real-World Chinese Cardiovascular Records](http://arxiv.org/abs/2611.04687v1)
  <details><summary>📄 Abstract</summary>
  Identifying the primary diagnosis alone does not fully characterize a model's diagnosis-generation performance. We introduce CardioVascBench, a retrospective benchmark for prioritized diagnosis generation from real-world Chinese cardiovascular inpatient records. It contains 3,262 de-identified cases, with 2,174 for training and 1,088 for evaluation, linking clinical narratives and textual ECG reports to expert-verified, ordered discharge diagnoses standardized to ICD-10. An English translation o...
  </details>

- **2026-11-03** — Andrea Pomarico, Salvatore Tessitore, Giorgio Giannuzzi et al. — [TuneBench: Benchmarking AI Agents for Power System Dynamic Model Calibration](http://arxiv.org/abs/2611.04640v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based agents can automate complex engineering workflows by interacting with tools, interpreting feedback, and making iterative decisions. This paper introduces TuneBench, a benchmark for evaluating Agentic AI in power system dynamic model calibration, where controller parameters are adjusted to reproduce target dynamic responses. The benchmark reflects a common Transmission System Operator (TSO) practice, in which equivalent models used for Dynamic Security Assessment ...
  </details>

- **2026-11-03** — Yifan Yang, Zhen Huang, Weijia Shi et al. — [ValQID: Learning the Net Value of Semantic Query Groups for Web Device Identification](http://arxiv.org/abs/2611.04576v1)
  <details><summary>📄 Abstract</summary>
  Web interfaces are widely used to access network services and manage networked devices. Identifying the vendors and types of devices behind Web interfaces is a critical step in asset inventory, security management, and risk assessment. Device identity cues are dispersed across page text, configuration fields, and management functions, and interpreting them often requires linking related Web objects. Responses and objects require different amounts of semantic analysis, so exhaustively processing ...
  </details>

- **2026-11-03** — Jonas Leo Mueller, Dario Zanca, Sebastian Hoefler et al. — [A Universal Raw-IQ Radar Encoder for Cross-Sensor Human Sensing](http://arxiv.org/abs/2611.04534v1)
  <details><summary>📄 Abstract</summary>
  Radar-based human sensing typically relies on end-to-end task-specific models trained on hand-chosen signal projections, which generalize poorly across unseen users, tasks, and hardware. We argue that the dominant signal processing choice, the micro-Doppler spectrogram, is a poor starting point for transfer because it keeps the Doppler axis, which carrier frequency rescales, and discards the angular axis, which carrier frequency leaves unchanged. We instead pretrain a convolutional beta-VAE with...
  </details>

- **2026-11-03** — Haowei Pan, Hwa Hui Tew, Junn Yong Loo et al. — [E2I-Flow: EEG-to-Image Reconstruction via Wavelet-Temporal Cross-Attention and Conditional Flow Matching](http://arxiv.org/abs/2611.04524v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG)-based visual decoding and reconstruction aims to recover visual information from non-invasive brain signals. But there are challenges due to the complex temporal-frequency characteristics of EEG signals and the difficulty of discrete denoising framework in mapping neural activity to meaningful visual representations. Here, we propose E2I-Flow, an EEG-to-image decoding and reconstruction framework that combines a novel EEG encoder for time-frequency representation lea...
  </details>

- **2026-11-03** — Brett Daley, Ilya Gorbachev, Anubhav Natani et al. — [Learnings and Pitfalls from AI-Assisted A/B Experimentation at Scale](http://arxiv.org/abs/2611.04515v1)
  <details><summary>📄 Abstract</summary>
  A/B testing underpins product decisions by providing trustworthy, reproducible quantification of proposed changes' effects. Growing large language model (LLM) capabilities have motivated efforts to automate experimentation workflows. Yet LLMs are nondeterministic and prone to hallucination, properties that conflict with the trust experimentation systems must provide. Experiments are also operationally messy: diagnosing anomalies, debugging configurations, and conducting bespoke follow-up analyse...
  </details>

- **2026-11-03** — Alessandro Zirilli, Davide Marincione, Evgenios M. Kornaropoulos et al. — [Perseus: A Full-Stack System for Homomorphic Model Inference](http://arxiv.org/abs/2611.04488v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have made it exceptionally convenient for users to send their private data to model providers, which process them in plaintext. Fully Homomorphic Encryption (FHE) promises to secure remote inference by computing directly on encrypted data, yet it has remained prohibitively slow. The effort to make it practical remains fragmented, with most existing frameworks being closed-source, which keeps progress from compounding. We present Perseus, a free and open Python softwa...
  </details>

- **2026-11-03** — Chen Zhang, Seth Aycock, Yusuke Miyao — [Typological Feature Induction as a Benchmark for Inductive Metalinguistic Reasoning](http://arxiv.org/abs/2611.04421v1)
  <details><summary>📄 Abstract</summary>
  Existing metalinguistic reasoning benchmarks require both inference of rules and their application, making failures hard to diagnose. We introduce typological feature induction (TFI) which targets the former step. Given sentences in an unnamed language paired with translations in a known pivot language, models must predict a typological feature of the unnamed language. From Grambank and multi-parallel corpora, we automatically build evaluation questions over 195 languages. We find that LLMs iden...
  </details>

- **2026-11-03** — Maosen Zhao, Xianfang Zeng, Pengtao Chen et al. — [Efficient and Faithful High-Resolution Image Editing with Sparse Cross-Resolution Denoising](http://arxiv.org/abs/2611.04416v1)
  <details><summary>📄 Abstract</summary>
  Instruction-based image editors still primarily operate at 1K, whereas practical editing increasingly requires faithful 2K/4K outputs. Dense high-resolution adaptation preserves the editing trajectory but incurs expensive target-source attention; editing at 1K followed by external refinement is cheaper but can separate detail restoration from the editing trajectory. We introduce FLASH, a native high-resolution editor based on sparse cross-resolution denoising. A frozen 1K branch provides a seman...
  </details>

- **2026-11-03** — Yeonseok Lee — [Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](http://arxiv.org/abs/2611.04392v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models generalize across tasks, but their autoregressive decoders need sequential forward passes in proportion to the action horizon, each bounded below on embedded aerial platforms by streaming billions of parameters from memory. We present Aero-VPA, a lightweight Vision-Predictor-Action architecture for 3D navigation on edge hardware. A compact RGB-D Vision Transformer and a five-head ensemble predictor, trained without pixel reconstruction, forecast the next laten...
  </details>

- **2026-11-03** — Jiaming Zhou, Pei Zhang, Shiwan Zhao et al. — [Do Multi-Turn Conversational Capabilities Carry Over from Text to Speech? A Parallel Multilingual Benchmark](http://arxiv.org/abs/2611.04390v1)
  <details><summary>📄 Abstract</summary>
  Successful multi-turn voice interaction requires models to retain information from earlier turns, follow persistent instructions, and track revisions to conversational state. These abilities are usually evaluated from transcripts, leaving open whether successes demonstrated from text carry over when the same turns are spoken, and whether this transfer is consistent across languages. We introduce Omnilingua-AudioMC, a strictly parallel multilingual extension of Audio MultiChallenge, to study this...
  </details>

- **2026-11-03** — Junyu Yin, Vinod Grover, Keren Zhou — [Warpline: Binary-Level Tracing and Unified Evidence for Agentic GPU Kernel Optimization](http://arxiv.org/abs/2611.04331v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are becoming GPU kernel engineers, but they still tune kernels without seeing where the time goes. Hardware profilers report how busy each unit was, not where each warp's time went; intra-kernel tracers can show it, but only with hand-placed probes and a recompilation that alters the very kernel being measured. We present Warpline, which gives agents this view automatically while leaving the kernel essentially unchanged. Warpline analyzes the binary to decide which events to record an...
  </details>

- **2026-11-03** — Zimeng Wang, Jinrong Yang, Rong Chen — [UMLoad: Fast On-Demand Model Loading on Unified Memory Architecture](http://arxiv.org/abs/2611.04253v1)
  <details><summary>📄 Abstract</summary>
  On-demand model loading dominates response latency for interactive on-device AI, yet unified memory architectures (UMAs), now common on edge devices, should make it cheap by placing weights in memory the GPU already sees. However, frameworks still use the loading flow built for discrete GPUs, leaving significant inefficiencies. This paper presents UMLoad, a system-level model-loading accelerator that decouples a framework's logical allocations from their physical page backing. UMLoad uses on-dem...
  </details>

- **2026-11-03** — Kailing Li, Ruoxuan Zhang, Zheyuan Zhou et al. — [AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](http://arxiv.org/abs/2611.04241v1)
  <details><summary>📄 Abstract</summary>
  Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not necessarily reflect changes in task objectives. We introduce AceAction, a dataset of human gameplay across multiple 3D games for learning skill composition and subgoal transitions. AceAction organizes demonstrations aro...
  </details>

- **2026-11-03** — Shuhang Lin, Chuhao Zhou, Zhenyu Wang et al. — [AdSteer: Native Advertising in Large Language Model Generation](http://arxiv.org/abs/2611.04147v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) services face rapidly rising serving costs. To sustain free or affordable access for a broad user base, alternative monetization mechanisms are needed. Native advertising offers a promising approach, as it creates economic value by aligning user intent with merchant offerings. Yet how to integrate sponsored content naturally into LLM responses remains largely underexplored. Existing approaches primarily rely on prompt-level injection, multi-pass rewriting, or fine-tuni...
  </details>

- **2026-11-03** — Minho Ha, Myunghyun Rhee, Euiseok Kim et al. — [HyPAIC: Personal AI Computer with High Bandwidth Flash for High Performance Trillion-Parameter LLM Inference](http://arxiv.org/abs/2611.04144v1)
  <details><summary>📄 Abstract</summary>
  LLMs have rapidly expanded from simple chatbots to agentic AI, where models directly use tools to solve complex problems. To improve problem solving, most frontier LLMs adopt an MoE architecture, pushing model sizes into the trillion-parameter regime. While cloud services have dominated large-scale LLM inference, cost and security concerns drive demand for on-premises deployment. Thus, GPU manufacturers have introduced personal AI computers (PAICs). However, existing PAICs with LPDDR-based unifi...
  </details>

- **2026-11-03** — Kevin Weekly, Alexandre M. Bayen — [Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy](http://arxiv.org/abs/2611.04096v1)
  <details><summary>📄 Abstract</summary>
  Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically been performed offline. As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic policies, a deterministic safety layer with formal guarantees is an essential complement. We present a CUDA implementation of the ...
  </details>

- **2026-11-03** — Sangdo Han, Moonsoo Kim — [Swapping the Judge Changes the Ranking: A Preregistered Study of Cross-Provider Replication in LLM-Judged System Comparisons](http://arxiv.org/abs/2611.04090v1)
  <details><summary>📄 Abstract</summary>
  Practitioners who compare systems with an LLM judge and have no human labels often check a conclusion by repeating it with a judge from another provider. We test how far that check can be trusted. In a preregistered study (with a disclosed post-registration reduction of the judge set), five judge models from three providers re-judged 4,000 Chatbot Arena battles (nine systems, 33 system pairs) that carry human votes, each in both response orders. Agreement with the human vote was low at the verdi...
  </details>

- **2026-11-03** — Pengfei Zhou, Yixing Ma, Hexin Wang et al. — [Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](http://arxiv.org/abs/2611.05275v1)
  <details><summary>📄 Abstract</summary>
  Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capability, a promising path toward AGI now is to orchestrate a heterogeneous ecosystem of specialized models, tools, and policies (candidates) into a unified AI system. At the heart of this vision lies a fundamental question: how can an AI system dynamically select and coordinate the most capable candi...
  </details>

- **2026-11-03** — Asher James Hancock, Boyi Li, Yuxiao Chen et al. — [Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs](http://arxiv.org/abs/2611.05249v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models increasingly pair a pre-trained vision-language model (VLM) with a flow-matching expert that conditions its action predictions on the VLM's key-value representations. Those representations must carry information useful for control, yet the VLM was never trained for the action expert's flow-matching objective. Two signals can address this: gradients backpropagated from the expert's loss (coupling), or VLM supervision to predict discrete tokens encoding the same...
  </details>

- **2026-11-03** — Seungyong Lee, Suhyeok Jang, Minyoung Kim et al. — [RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](http://arxiv.org/abs/2611.05163v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keep...
  </details>

- **2026-11-03** — Sombit Dey, Luc Van Gool, Danda Pani Paudel — [Asynchronous Robot Policies](http://arxiv.org/abs/2611.05155v1)
  <details><summary>📄 Abstract</summary>
  Scaling vision-language foundation models has significantly advanced generalist robot manipulation, but the increased model scale introduces computational latency that degrades real-time physical reactivity. Existing Vision-Language-Action (VLA) architectures execute high-level semantic reasoning and action ex- ecution sequentially within the primary control loop, creating a fundamental tension between semantic-reasoning capability and robot agility. To address this, we propose Asynchronous Robo...
  </details>

- **2026-11-03** — Po-Yi Wu, Djengo Cyun-Jyun Fang, Dian Cheng et al. — [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](http://arxiv.org/abs/2611.05080v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments. However, standard RL pipelines rely on episodic training with frequent scene resets, which is impractical for real-world deployment due to the need for substantial human intervention. While prior work has studied non-episodic RL in relatively small policies trained from scratch, its behavior when fine-tuning modern large-scale pre-trained vision-language-action (VLA) models remains under...
  </details>

- **2026-11-03** — Yihang Liu, Yiming Chen, Mingzhe Zheng — [Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning and Action](http://arxiv.org/abs/2611.05058v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal language models can reason directly about robot scenes, but it is unclear whether they need to repeatedly reinterpret raw visual observations at every step of an interaction. We propose shifting routine spatial reasoning from images to text and symbols through a 3D geometric abstraction that is refreshed locally from observations and read directly by the language models. Specifically, our interface represents scene geometry via typed, evidence-aware symbolic references to objec...
  </details>

- **2026-11-03** — Andrew Semenov, Svyatoslav Dorofeev — [Kierston & KierstonBench: Simulation of Allentown, PA and Evaluation of Language Models in Crime Investigation and Surveillance Tasks](http://arxiv.org/abs/2611.04785v1)
  <details><summary>📄 Abstract</summary>
  Large language models are candidates for collecting and analyzing records in criminal investigations and mass surveillance. Their capability and accuracy in this work cannot currently be measured. Real deployments lack the ground truth needed to score a model's conclusions, and no benchmark evaluates these capabilities in a simulated environment. We present Kierston, a city-scale simulation engine, and KierstonBench, a benchmark that tests these capabilities against known simulated events. Kiers...
  </details>

- **2026-11-03** — Peter Chen, Ni Zhang, Siyuan Zhang — [Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition](http://arxiv.org/abs/2611.04420v1)
  <details><summary>📄 Abstract</summary>
  Automated research pipelines pair an LLM proposer with a verifier on an implicit bet: discovery quality rises with verification strength. Under a pre-registered protocol we test this bet in two real-data domains -- job-shop scheduling and vehicular edge offloading on Beijing T-Drive trajectories -- across 100 matched LLM/random pairs per domain and three verifier tiers. The manipulation binds -- a 429-case mutation battery shows scores rising across tiers -- yet the paired LLM-over-random advant...
  </details>

- **2026-11-03** — Hiram Ring — [The Min-Max theory of language behavior](http://arxiv.org/abs/2611.04406v1)
  <details><summary>📄 Abstract</summary>
  The "Min-Max" theory of language behavior proposes that humans engage simultaneously in minimization of processing effort and maximization of information content, and that this is a primary driver in language evolution (Ring, 2025). This claim seeks to unify observations from language processing (Mahowald et al., 2013; Futrell et al., 2015; Yadav et al., 2020; Hawkins, 2014), interaction (Hörberg and Sjons, 2023; Tucker et al., 2025; Jaeger and Tily, 2011; Smith and Culbertson, 2025), and corpor...
  </details>

- **2026-11-03** — Han Zhang, Sicheng Lu, Aleks Santari et al. — [ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms](http://arxiv.org/abs/2611.04255v1)
  <details><summary>📄 Abstract</summary>
  Operating rooms (ORs) increasingly contain ambient sensing infrastructure to enable AI-based optimization of workflows and utilization. We pursue an alternative path: using ambient AI to guide robot action and optimize utilization. Deploying humanoids in the OR without ambient AI is severely limited by cumbersome de novo orientation and planning due to partial onboard observations. We posit that this can be achieved by coupling an ambient AI-based agentic orchestrator with the humanoid robotic a...
  </details>

- **2026-11-03** — Sangyoon Bae, Jiook Cha — [Structure, Dimensionality, and Distribution Shape - What Makes Pretraining Data Transferable, and Why the Input Pipeline Decides Which](http://arxiv.org/abs/2611.04106v1)
  <details><summary>📄 Abstract</summary>
  What makes a pretraining corpus transferable? We describe a corpus by three properties: its structure, its dimensionality, and the distribution shape of each unit's values. We propose the Transfer-Invariance Principle: the same property can be irrelevant to transfer under one input transform and decisive under another, so the model's input transform, not the data modality, decides which properties can matter. To test it we build TransferForge, a generator that places a synthetic population at an...
  </details>

- **2026-11-03** — Hao Fei — [From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](http://arxiv.org/abs/2611.05376v1)
  <details><summary>📄 Abstract</summary>
  For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, fail to find the right words, and face hard choices without the benefit of their own history, because the machine that could help stands outside the situation. As AI moves into the physical world, atte...
  </details>

- **2026-11-03** — Michael F. Barad — [A wider state, not wider arithmetic, for single-precision time integration](http://arxiv.org/abs/2611.05365v1)
  <details><summary>📄 Abstract</summary>
  Single precision (FP32) halves the memory and data movement of double precision (FP64), and on accelerators is often several times faster. Its rounding errors are harmless except in the stored state. A modified equation for Runge-Kutta methods in Shu-Osher form and linear multistep methods separates the rounding of the stored state, a forcing proportional to $1/Δt$, from truncation and from right-hand-side rounding, which sets a $Δt$-independent floor. We bound this forcing for strong-stability-...
  </details>

- **2026-11-03** — Teerawat Tongloy, Jiraporn Pongsopa, Rangsan Jomtarak — [Reading Why: Born-Measured Attention with Exact Word Evidence on Light and Qubits](http://arxiv.org/abs/2611.05355v1)
  <details><summary>📄 Abstract</summary>
  When a language model answers, we can usually only estimate why. We build a transformer in which every step is a Born measurement - attention $|\langle q|k\rangle|^4$ normalised over each row, a measured product in place of the feed-forward nonlinearity, and a Born readout. With its denominators held at their values for the input, each class probability is a polynomial in the word amplitudes, so its integrated-gradient evidence is computed by a finite quadrature with no quadrature error: the wor...
  </details>

- **2026-11-03** — Yueqiao Chen, Dongyu Liu — [CATF: A Manager-Worker Framework for Context-Aware Time-Series Forecasting](http://arxiv.org/abs/2611.05325v1)
  <details><summary>📄 Abstract</summary>
  We study context-aware time-series forecasting, in which a single target variable is predicted from its own history and a set of contextual variables, such as weather and calendar information. As the context becomes more diverse, a single model struggles to capture all of its regimes, while ensemble learning and Mixture-of-Experts approaches rely on manual data partitioning or soft routing, which increases the inference cost and hinders interpretability. We propose CATF, a Context-Aware Time-Ser...
  </details>

- **2026-11-03** — Yunan Wu, Bin Sun, Partha Acharjee et al. — [Wonder 4: A Mixture-of-Experts Recipe for Image Quality Enhancement](http://arxiv.org/abs/2611.05294v1)
  <details><summary>📄 Abstract</summary>
  A real photograph is often blurry, grainy, compressed, scratched, and low-resolution at the same time. Each defect has its own severity and its own place in the image. The corrections for these defects conflict with each other. Exist- ing models describe the whole image with one description, so they cannot say where each correction belongs. To solve this problem, we present Wonder 4, a mixture-of-experts (MoE) model for image quality enhancement. It corrects several defects of a real photograph ...
  </details>

- **2026-11-03** — Kadharmoideen Fadurudeen — [False Reassurance in LLM Severe-Weather Guidance: A Replayable Evaluation Against Real NWS Alerts](http://arxiv.org/abs/2611.05290v1)
  <details><summary>📄 Abstract</summary>
  An LLM assistant that cannot see official severe-weather alerts may tell users that conditions are calm while a warning is active. We call this false reassurance and measure it by replaying 117 frozen cases built from real U.S. National Weather Service (NWS) alerts (69 alert cases, 32 no-alert controls, 16 non-U.S. locations) through five conditions of a Claude-based preparedness pipeline that differ in alert access and prompt design. One rater hand-labeled all 342 alert-case responses under a s...
  </details>

- **2026-11-03** — Shucheng Zou, Yuhao Gu, Long Chen et al. — [ToolSched: Resource-Efficient Tool Scheduling for Shared-Host LLM Agents](http://arxiv.org/abs/2611.05269v1)
  <details><summary>📄 Abstract</summary>
  Local LLM agents often work on shared hosts. Unlike multi-tenant cloud clusters, these hosts often have tightly bounded memory, CPU, and I/O resources. Concurrent agents frequently suffer from resource contention, leading to failures such as OOM and reduced resource efficiency. Considering that agents' resource demands are bursty and shell command delay is imperceptible to agents, there is a huge scheduling opportunity to arrange when and in what order commands are actually executed. Thus, we pr...
  </details>

- **2026-11-03** — Shanka Subhra Mondal, Jiayun Wang — [JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks](http://arxiv.org/abs/2611.05263v1)
  <details><summary>📄 Abstract</summary>
  Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through intermediate states, track progress over extended interaction histories, and execute visually grounded actions. Although prior work has explored modular multi-agent systems with a sepa...
  </details>

- **2026-11-03** — Yuhang Chen, Yuda Feng, Weijiang Hu et al. — [Santa Claus and Weighted Nash Social Welfare with Subadditive Valuations](http://arxiv.org/abs/2611.05229v1)
  <details><summary>📄 Abstract</summary>
  We study two fairness objectives for allocating $m$ indivisible items among $n$ agents with subadditive valuations: the max-min objective, also known as the Santa Claus problem, which maximizes the smallest value of an agent, and the weighted Nash social welfare, which maximizes the weighted geometric mean of the agents' values.   For the max-min allocation problem, we give a randomized polynomial-time $O(\sqrt n)$-approximation algorithm for subadditive valuations with demand queries, improving...
  </details>

- **2026-11-03** — Zihan Zhou, Mingxi Ye, Yan Gao et al. — [DSL-Bench: Evaluating and Explaining LLM Code Generation Across Domain-Specific Languages](http://arxiv.org/abs/2611.05168v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in software-engineering workflows, but code-generation benchmarks largely focus on general-purpose languages. Domain-specific languages (DSLs) have distinct syntax, semantics, and validation requirements, making results from individual DSL benchmarks difficult to compare. We present DSL-Bench, an executable benchmark and analysis framework for cross-DSL code generation. Starting from 13,045 DSL-related papers, LLM-assisted open card sorting iden...
  </details>

- **2026-11-03** — Artem Chistyakov, Renat Sergazinov, Artem Babenko — [Beyond Foundation Models: PFN Priors Improve Tabular Hyperparameter Optimization](http://arxiv.org/abs/2611.05141v1)
  <details><summary>📄 Abstract</summary>
  Synthetic priors have so far served one purpose: pretraining tabular foundation models. We ask whether the same priors can improve conventional tabular models, which are trained from scratch on each dataset. We propose PriorTune, a method that meta-tunes hyperparameter configurations on synthetic tasks alone. Offline, for a given model, we fit a pool of configurations on datasets sampled from a published PFN prior and greedily select the subset with the highest winrate over the random baseline. ...
  </details>

- **2026-11-03** — Tom Szwagier, Xiaoyi Mai, José Henrique de Morais Goulart — [A Random Matrix Analysis of Symmetric Tensor Unfolding](http://arxiv.org/abs/2611.05137v1)
  <details><summary>📄 Abstract</summary>
  We study a fundamental problem in machine learning: partial recovery of a planted signal $\boldsymbol{v} \in \mathbb{S}^{n-1}$ from a spiked tensor $\boldsymbol{\mathsf{X}} = λ\, \boldsymbol{v}^{\otimes p} + \boldsymbol{\mathsf{Z}}$, where $\boldsymbol{\mathsf{Z}}$ has symmetric Gaussian entries of variance $\asymp n^{-1}$. While previous works replace $\boldsymbol{\mathsf{Z}}$ by an i.i.d. standard Gaussian tensor to circumvent technical difficulties caused by dependencies, this paper directly ...
  </details>

- **2026-11-03** — Pawel Gomoluch, Anthony Bradley — [Molecular Prior Networks](http://arxiv.org/abs/2611.05103v1)
  <details><summary>📄 Abstract</summary>
  Predicting affinity between small molecules and their protein targets remains one of the central problems in drug discovery. Due to the substantial cost of wet-lab experiments, machine learning models of drug-target affinity are usually trained on relatively small datasets, ranging from tens to hundreds of molecules. Given the inherent difficulty of generalization between different targets and chemical series, existing datasets of protein-ligand affinities are typically not used for new projects...
  </details>

- **2026-11-03** — Junzhe Chen, Tian Qin, Eugenie Shi et al. — [VIGOR: Visual Gain Ordering for Hallucination Mitigation in Multimodal Discrete Diffusion Language Models](http://arxiv.org/abs/2611.05066v1)
  <details><summary>📄 Abstract</summary>
  Multimodal discrete diffusion language models (dLLMs) generate responses through iterative mask prediction and offer a promising alternative to autoregressive large vision-language models. However, they still suffer from hallucination, producing outputs that are plausible under language priors but insufficiently grounded in the image. We argue that hallucination in multimodal dLLMs is not only a token prediction problem, but also a premature commitment problem: during iterative denoising, some m...
  </details>

- **2026-11-03** — Zhenghao Chen, Lebin Zhou, Zicong Chen et al. — [An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression](http://arxiv.org/abs/2611.04960v1)
  <details><summary>📄 Abstract</summary>
  Despite decades of progress, image codecs remain difficult to adapt to diverse real-world compression scenarios for two main reasons. First, most image codecs are optimized for a specific objective and require substantial redevelopment when the compression goal changes. Second, they typically assume clean inputs, whereas sensor-captured images often contain degradations that alter rate-quality behavior. To address these challenges, we propose Practical Image Coding Agents (PICA), a multi-agent f...
  </details>

- **2026-11-03** — Zehan Lin, Xiaowei Wu, Shengwei Zhou — [Best-of-Many-Worlds MMS Allocation for Chores with Sublinear Disposals](http://arxiv.org/abs/2611.04884v1)
  <details><summary>📄 Abstract</summary>
  We study randomized allocations (lotteries) of indivisible chores under additive costs and introduce the notion of MMS1, which requires each agent's bundle to satisfy the maximin share (MMS) bound after the removal of at most one chore. Our main result establishes that every instance admits an ex-ante proportional lottery in whose support every allocation is MMS1 and all but $o(n)$ agents satisfy MMS. Consequently, every realized allocation can be made MMS by disposing of at most $o(n)$ chores. ...
  </details>

- **2026-11-03** — Jin Zhu, Junxian Zhu — [Amortized Nonlinear Variable Selection with Prior-Data Fitted Networks](http://arxiv.org/abs/2611.04848v1)
  <details><summary>📄 Abstract</summary>
  Variable selection is an important task for interpreting potentially complex systems in fields such as biology, business, and sociology. The importance of variable selection has attracted considerable attention in statistics and machine learning. In this paper, we are mainly interested in model-agnostic variable selection for identifying variables that have general nonlinear dependence on the response. We propose MambaPFN, short for Model-Agnostic Markov BlAnket selection with Prior-data Fitted ...
  </details>

- **2026-11-03** — Shu Zhou, Ziyang He, Yuxin Rao et al. — [AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](http://arxiv.org/abs/2611.04813v1)
  <details><summary>📄 Abstract</summary>
  Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding from correctness. To bridge this gap, we introduce $\textbf{AgenticFinBench}$, a benchmark of 230 real-world financial tasks spanning 8 categories, 2 languages, and 4 complexity levels. We also propose a reference-free ...
  </details>

- **2026-11-03** — Atikkhan Faridkhan Nilgar, Manuel Dietrich, Kristof Van Laerhoven — [Just Between Us? Exploring a Wearable-Mediated Channel for Discreet Human-Agent Interaction in a Shared Game Setting](http://arxiv.org/abs/2611.04692v1)
  <details><summary>📄 Abstract</summary>
  In shared settings, social robots may need to exchange information with an individual while limiting co-present others' access to or interpretation of that information. Publicly observable speech and gestures may not adequately support such exchanges. We investigate a wearable-mediated channel for discreet interaction that combines in-ear audio messages with deliberate rightward head tilts as responses. To examine its feasibility and participants' experiences, we studied 20 pairs (40 participant...
  </details>

- **2026-11-03** — Benjamin Gess, Paul Nikolaev — [Long-time behaviour and bifurcation analysis of a non-reciprocal two-species aggregation-diffusion system on the torus](http://arxiv.org/abs/2611.04655v1)
  <details><summary>📄 Abstract</summary>
  A two-species aggregation-diffusion system on the one-dimensional torus with antisymmetric cross-interactions modeling pursuit-evasion dynamics is studied. The self-interaction strength is used as a bifurcation parameter, and the linear stability of the homogeneous state is characterized by Fourier analysis. It is shown that non-reciprocal coupling enlarges the stability region. In a symmetric diffusion setting, exponential convergence to the homogeneous state is established for sufficiently wea...
  </details>

- **2026-11-03** — Pyare Lal Chauhan, Vaibhav Kumar, Bharat Lohani — [BhopalMLS: A LiDAR Dataset for Semantic Scene Understanding in Heterogeneous Urban Environments](http://arxiv.org/abs/2611.04654v1)
  <details><summary>📄 Abstract</summary>
  We introduce BhopalMLS, a large-scale Mobile Laser Scanning (MLS) dataset from a dense, heterogeneous urban environment in Bhopal, India, with mixed traffic, informal structures, and narrow unplanned streets. It spans approximately 10 km of road corridors with over 1.2 billion points and 19,518 annotated instances across 62 fine-grained static categories, grouped into 12-class and 21-class benchmark taxonomies; 6 optional moving-class subclasses support dynamic-object analysis. Existing 3D datas...
  </details>

- **2026-11-03** — Ehsan Khorrambakht, Cristiano Caissutti, Andrea Munafo et al. — [LLM-Assisted Planning with Distributed Onboard Behaviour Tree Execution for Multi-AUV Missions](http://arxiv.org/abs/2611.04518v1)
  <details><summary>📄 Abstract</summary>
  Coordinating autonomous underwater vehicles requires translating operator intent into feasible assignments while preserving autonomous execution when communication is limited. We present a hierarchical framework that couples Large Language Model (LLM) interpretation of natural-language mission instructions with Mixed-Integer Linear Programming (MILP) and distributed Behaviour Tree (BT) execution. The LLM extracts assignment and ordering constraints, which the MILP optimizer combines with vehicle...
  </details>

- **2026-11-03** — Muhammad Uzair Ul Haq, Davide Rigoni, Alessandro Sperduti et al. — [Fast, Cheap, and Fair? Evaluating Decision Models](http://arxiv.org/abs/2611.04510v1)
  <details><summary>📄 Abstract</summary>
  Industries are increasingly adopting AI-driven systems to automate a wide range of tasks, including high-stakes decisions in human resources, such as candidate screening and recruitment. This makes evaluating their fairness essential, particularly when decisions directly affect individuals' opportunities. Accordingly, the EU AI Act classifies recruitment AI systems as high-risk, imposing strict requirements on their deployment. In this context, compact ``System~1'' decision models offer a fast a...
  </details>

- **2026-11-03** — Ruize Gao, Feng Xiao, Jinpu Li et al. — [Theory-guided relational learning for data product pricing: An interpretable meta-path-guided graph neural network approach](http://arxiv.org/abs/2611.04508v1)
  <details><summary>📄 Abstract</summary>
  Data products are non-standardized and context-dependent, so their prices are jointly shaped by product attributes and contextual factors such as provider reputation, product comparability, and industry structure. We formulate data product pricing as a learning task over a heterogeneous information network spanning data products, providers, marketplaces, industries, and pricing modes, and design theory-grounded meta-paths, brand-based, similarity-based, industry-based, and hybrid, to characteriz...
  </details>

- **2026-11-03** — Taehoon Kim, Wonjun Hwang, Hyunsouk Cho — [Bridging CLIP with DINO: Cross-Modal Information Maximization for Online Test-Time Adaptation](http://arxiv.org/abs/2611.04489v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models such as CLIP enable zero-shot classification from arbitrary class names, but under test-time corruptions, their visual encoder projects distorted features onto incorrect textual anchors with high confidence: a phenomenon we term modality bias. Standard entropy minimization reinforces these overconfident errors, which creates a confirmation-bias loop and collapses the predicted label distribution. We propose an online test-time adaptation (TTA) method that breaks this loop ...
  </details>

- **2026-11-03** — Riccardo Maggioni — [TEMPO: Time Series Understanding via Discrete Tokenization](http://arxiv.org/abs/2611.04482v1)
  <details><summary>📄 Abstract</summary>
  Time-series interpretation often requires both numerical observations and textual context. Integrating these inputs into a pretrained language model raises a representation question: how should a signal enter the model's token sequence? We present TEMPO, which extends an LLM's vocabulary with discrete codes from a context-aware Transformer tokenizer using finite scalar quantization. A frozen tokenizer maps four-step patches to a 625-code vocabulary; signal tokens, scale statistics, and text are ...
  </details>

- **2026-11-03** — Monit Sharma, Hoong Chun Lau — [Reducing the arithmetic cost of quantum derivative pricing with language-model circuit design](http://arxiv.org/abs/2611.04431v1)
  <details><summary>📄 Abstract</summary>
  Quantum amplitude estimation can estimate expected discounted payoffs with quadratically fewer oracle calls than Monte Carlo, but each call requires coherent computation. We use language-model-assisted circuit design to reduce reversible payoff arithmetic for a three-asset worst-of autocallable and a target accrual redemption forward (TARF). The constructions retain compact integer representations of market paths alongside contract history, reconstructing quantities temporarily for contract deci...
  </details>

- **2026-11-03** — Nishi Kanta Paul, Md Shihabul Islam Shovo, Audrija Chowdhury et al. — [DR-LiteNet: A Lightweight Explainable Hybrid CNN Framework for Imbalanced Diabetic Retinopathy Grading via Adaptive SMOTE Fusion](http://arxiv.org/abs/2611.04405v1)
  <details><summary>📄 Abstract</summary>
  Automated diabetic retinopathy (DR) grading from colour fundus photographs is held back by two compounding challenges: severe class imbalance across five severity grades and the heavy computational cost of large scale architectures in resource constrained clinical settings. We introduce DR-LiteNet, a dual branch hybrid convolutional neural network that tackles both problems at once. The CNN branch extracts 1,280 dimensional deep features through EfficientNetB0, while the handcrafted (HC) branch ...
  </details>

- **2026-11-03** — Ajit Singh — [The smallest-parts function and elliptic curves](http://arxiv.org/abs/2611.04387v1)
  <details><summary>📄 Abstract</summary>
  Recently, Ono established a new connection between partition congruences and the arithmetic of elliptic curves by expressing the partition function $p(n)$ as a CM trace on the modular curve $X_0(6)$. This approach yields new proofs of Ramanujan-type congruences for the partition function modulo powers of $5$, $7$, and $11$, revealing how the geometry of supersingular elliptic curves and the arithmetic of oriented optimal embeddings govern these congruence properties. Motivated by Ono's work, we ...
  </details>

- **2026-11-03** — Yichen Xu, Shipei Lin, Chenhao Ma — [Text-to-SQL Models Make Choices Without Saying So](http://arxiv.org/abs/2611.04318v1)
  <details><summary>📄 Abstract</summary>
  A text-to-SQL answer can run, return a plausible number and still compute something other than what the analyst meant. This can happen when the request leaves a calculation choice open, such as whether to count rows or distinct entities, and the model settles it without saying so. Standard benchmarks cannot detect this, because they score each question against a single reference interpretation. We introduce SpecBridge, which tests such a choice by varying it alone: it poses three otherwise ident...
  </details>

- **2026-11-03** — Zhuoran Zheng,  Doubao — [Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop](http://arxiv.org/abs/2611.04268v1)
  <details><summary>📄 Abstract</summary>
  Can an LLM directly edit the weights of a diffusion-based image-restoration model to \emph{improve} restoration quality---without gradients, paired data, or fine-tuning? Recent experiments show frontier LLMs can fix structural bugs by modifying as little as \(0.016\%\) of parameters, but cannot instill new capabilities. We ask whether weight-space programming (WSP) can move from \emph{debugging} to \emph{improvement} in the precise-regression setting of image restoration (deblurring, super-resol...
  </details>

- **2026-11-03** — Sihao Wang, Bozheng Li, Xuemiao Xu et al. — [LIRA: A More Interpretable Dynamic Loss-Informed Rank Allocation for Low-Rank Adaptation](http://arxiv.org/abs/2611.04239v1)
  <details><summary>📄 Abstract</summary>
  Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large pretrained models. However, standard LoRA typically assigns a fixed rank profile despite layer- and stage-dependent adaptation needs, while recent adaptive-rank variants often rely on heuristic or first-order signals that provide only an indirect link between rank reallocation and local loss behavior. This leaves the rationale behind each rank reallocation insufficiently interpretable. Motivated ...
  </details>

- **2026-11-03** — Madeleine Grunde-McLaughlin, Hafsah Usman, Daniel Mitroshkov et al. — [Agentic Path Maps: Exposing an Agent's Traversal Through the Garden of Forking Paths](http://arxiv.org/abs/2611.04183v1)
  <details><summary>📄 Abstract</summary>
  When an AI agent executes an underspecified task, it embeds choices that may contradict unarticulated user context and preferences. However, interrupting the user for clarification on all such decisions is untenable. How might agents communicate impactful, but unexplored, paths to the user after execution? To investigate, we first distill a design space for communicating alternative paths, supporting the generation of new systems and structuring dimensions of future study. We then measure the im...
  </details>

- **2026-11-03** — Yinuo Liu — [Length Is Cheap, Competition Is Not: Attention Predicts Context Rot in Retrieval](http://arxiv.org/abs/2611.04169v1)
  <details><summary>📄 Abstract</summary>
  Why do language models fail on long inputs? The common answer is length. We show that, for retrieval, length is cheap and competition is not. On five open models (0.5B to 3B parameters, four families), neutral filler costs nothing: accuracy stays at 0.97 to 1.00, up to 32K tokens on Qwen2.5-1.5B. Statements in the format of the evidence, placed at the same positions, drop it to 0.16 to 0.33. A single statement that gives the queried key a rival value multiplies the loss by 9 to 110, and every ad...
  </details>

- **2026-11-03** — Kiyoun Kim, Sung-Yeon Nathan Lim — [Multidimensional Views Behind Target-Price Revisions: An LLM-Based Representation of Analyst Outlooks](http://arxiv.org/abs/2611.04119v1)
  <details><summary>📄 Abstract</summary>
  A target price compresses an analyst's multidimensional views into a single number. We propose an LLM-based text representation that extracts these views from research reports as question-based outlook scores with supporting evidence. The questions organize reported views on earnings, valuation, industry conditions, and other investment dimensions into a compact representation of analyst sentiment. In walk-forward evaluation, the scores improve prediction of subsequent target-price revisions bey...
  </details>

- **2026-11-03** — Hao Lu, Weixing Zhu, Ruiyang Li — [Evaluation Contracts and Evaluation Leverage: Sliced-Gap Readings in Structured Prediction Can Move Without Model Change](http://arxiv.org/abs/2611.04099v1)
  <details><summary>📄 Abstract</summary>
  NLP evaluation reports routinely cite sliced performance differences, most prominently the intra-inter gap in document-level relation extraction, as capability evidence. We show that such gap readings are joint properties of models and evaluation contracts: scoring function, gold version, threshold, output format, and prompt language. With predictions frozen, a method ordering reverses under a gold-standard exchange (+0.0363, CI excluding zero; tie-level after), movement localizing where gold re...
  </details>

- **2026-11-02** — Datta Manikanta Sri Hari Danduri, Connor Everett Glosner, Aravind Machiry — [Towards Effective Fuzzing of EDK2 Components](http://arxiv.org/abs/2611.03854v1)
  <details><summary>📄 Abstract</summary>
  Securing bootloaders is critical to establishing the trusted computing base of modern systems. TianoCore's edk2, the de facto UEFI-based bootloader, is widely deployed but has recently been shown to contain numerous high-severity vulnerabilities. Existing approaches either focus on post-boot interfaces or rely on heavyweight simulation, limiting their scalability, throughput, and coverage of boot-time components.   We present Metis, an automated technique for fuzzing edk2 protocols (i.e., boot-t...
  </details>

- **2026-11-02** — Yuqi Jia, Yunjie Tian, Jiayu Zheng et al. — [Axion 1.0: Open Agent Foundation Models, Simplified](http://arxiv.org/abs/2611.03233v2)
  <details><summary>📄 Abstract</summary>
  We introduce Axion 1.0, a fully open agent foundation model that combines strong and broad agentic capabilities with a remarkably simple training recipe. Axion 1.0 is trained in only three stages: two lightweight supervised fine-tuning stages followed by reinforcement learning, without dedicated mid-training, direct preference optimization (DPO), or on-policy distillation (OPD). The first SFT stage develops strong self-contained reasoning through model-aware data construction, where we synthesiz...
  </details>

- **2026-11-02** — Mirza Samad Ahmed Baig, Syeda Anshrah Gillani — [Whose startup does the AI back? An algorithm audit of reputation and demographic signals in LLM-assisted crowdfunding](http://arxiv.org/abs/2611.03993v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) assistants increasingly advise backers on which crowdfunding campaigns to support. LLMs have known race and gender problems, and it is unsettled whether they reproduce, erase, or reverse the discrimination documented in entrepreneurial finance. We ask when, and through which decision process, LLM assistants use founders' gender and ethnicity. In a pre-specified choice-based conjoint experiment, seven LLMs chose among five synthetic campaigns with independently randomiz...
  </details>

- **2026-11-02** — Nick Hagar — [From Benchmarks to Behaviors: A Framework for Auditing AI Agents](http://arxiv.org/abs/2611.03939v1)
  <details><summary>📄 Abstract</summary>
  Generative AI systems increasingly mediate access to information. Their behavior depends on tools, instructions, and user memories that are often difficult for researchers to observe or control. Here, I introduce TRACE (Transparent Research on Agent Contexts and Environments), a framework for systematically auditing how these components shape AI agent behavior. Built on an open-source agent harness, TRACE enables controlled manipulation of system components. It also records inputs, outputs, and ...
  </details>

- **2026-11-02** — Yumou Liu, Mingju Chen, Zhoufutu Wen et al. — [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](http://arxiv.org/abs/2611.03412v2)
  <details><summary>📄 Abstract</summary>
  LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a time, leaving a gap between the capability we measure and the outcome that makes agents useful. To address this gap, we introduce DeliverBench, which tests whether agents can carry a project from brief to final delivery. I...
  </details>

- **2026-11-02** — Xinyang Li, Zeran Xu, Jingna Sun et al. — [TaoMate-FVSR: Audio-Guided Facial Video Restoration](http://arxiv.org/abs/2611.03393v2)
  <details><summary>📄 Abstract</summary>
  Low-quality facial videos suffer from missing fine details, while AI-generated videos may additionally contain implausible teeth and lip movements that do not match the speech. Restoring the mouth region is particularly challenging: enhancing existing details can preserve structural errors, whereas regenerating them risks changing facial identity and articulation. We propose an audio-guided facial video restoration framework that reconstructs unreliable mouth details and aligns lip movements wit...
  </details>

- **2026-11-02** — George Kontogiannis, Pantelis Tzamalis, Sotiris Nikoletseas — [Metadata-Conditioned Audio Transformers for Adaptive Respiratory Sound Classification](http://arxiv.org/abs/2611.03769v1)
  <details><summary>📄 Abstract</summary>
  Respiratory sound classification from auscultation recordings is confounded by heterogeneous acquisition conditions, including recording device, auscultation site, and patient characteristics, that introduce systematic variability unrelated to the underlying pathology. Although such metadata is often available, existing approaches either ignore it or rely on naïve fusion strategies that do not model how distinct metadata sources influence different components of the acoustic representation.   We...
  </details>

- **2026-11-02** — Eirik Botten Nicolaysen — [Outdated numeric values from Norwegian statutes and regulations in a further-trained model and its base model: a preregistered paired comparison of Borealis 2 and Gemma 4](http://arxiv.org/abs/2611.02334v2)
  <details><summary>📄 Abstract</summary>
  We compare how often two released language models give outdated numeric values from Norwegian statutes and regulations: NbAiLab/borealis2-26b-a4b-preview (Borealis 2), which the National Library of Norway further trained from google/gemma-4-26B-A4B-it (Gemma 4), and Gemma 4 itself. The study was preregistered (doi:10.5281/zenodo.23858965) and uses the closed norregel benchmark, scored deterministically against a value history. On the 411 of 503 primary items where both models gave an interpretab...
  </details>

- **2026-11-02** — Aditya Agarwal, William Shen, Sahit Chintalapudi et al. — [FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation](http://arxiv.org/abs/2611.04080v1)
  <details><summary>📄 Abstract</summary>
  A mobile manipulator asked to "put the toys away in the toy box" must decide which objects are toys and which container the user means, then find base poses, grasps, and placements it can execute. Because a scene representation is built before the instruction is known, it may lack the attributes, affordances, or concepts needed to resolve the task. We present FEIJOA, a language-model agent that grounds the instruction at test time. It queries a grounding tool over a posed RGB-D scan, inspects th...
  </details>

- **2026-11-02** — Ruijie Zhang, Jiayin Zheng, Yequan Zhao et al. — [Controlling Action-Head Co-Adaptation to VLM Representation Anisotropy](http://arxiv.org/abs/2611.04006v1)
  <details><summary>📄 Abstract</summary>
  Modern learning systems increasingly combine pretrained models with downstream heads. Despite the growing importance of such modular designs, how the downstream model co-adapts to the geometry of pretrained representations remains relatively underexplored. We study this problem through vision-language-action models (VLAs), where a pretrained vision-language model (VLM) conditions an action model for control. We find that the action model progressively concentrates its sensitivity on high-varianc...
  </details>

- **2026-11-02** — Yifan Liu, Baihan Zhang, Khai Loong Aw et al. — [FlowBench: Counterfactual Imagination Training for Spatial Intelligence](http://arxiv.org/abs/2611.03937v1)
  <details><summary>📄 Abstract</summary>
  Humans imagine scene changes under hypothetical motions, an ability central to spatial reasoning and robotic planning. However, this capability remains underexplored in vision-language models and world models. We formalize this capability as Counterfactual Spatial Imagination (CSI) and introduce FlowBench, a resource for training and evaluating both, with 428K training examples spanning simulated and real-world scenes, household environments and tabletop manipulation, and diverse question types....
  </details>

- **2026-11-02** — Kobi Kelemen, Tomasz Niedziałkowski, Marcin Paszczak et al. — [Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place](http://arxiv.org/abs/2611.03779v1)
  <details><summary>📄 Abstract</summary>
  Training robot policies for multi-task pick and place requires demonstrations on many objects, which handheld Universal Manipulation Interfaces (UMIs) can collect quickly and cheaply. However, existing UMIs depend on external base stations, use rigid fingers that give no signal about contact forces, or use parallel-jaw fingers that limit grip strength. We present a battery-powered handheld interface, built on YUBI, whose soft, angled fingers wrap around objects, deform visibly under load as a vi...
  </details>

- **2026-11-02** — Phuc Minh Nguyen, Ngoc-Hieu Nguyen, Parshin Shojaee et al. — [On the Primacy Bias in RLVR Training](http://arxiv.org/abs/2611.04061v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Reward (RLVR) has emerged as a promising approach for enhancing the reasoning capabilities of large language models. However, it still remains unclear whether RLVR can extend reasoning capabilities beyond what is already encoded in the base model. In this paper, we study this question through the lens of primacy bias: the tendency of models to over-rely on already-learned representations, disproportionately improving performance on problems they already han...
  </details>

- **2026-11-02** — Thomas Bartz-Beielstein — [Structured Priors: Towards an algebra of component priors for prior-data fitted networks](http://arxiv.org/abs/2611.04056v1)
  <details><summary>📄 Abstract</summary>
  Prior-data fitted networks are typically trained using synthetic data generated by a single, manually constructed generator. In cases where such a generator combines multiple components, e.g., in TabPFN, Mitra, or TabICLv2, this is achieved through a mixture using manually specified weights, the impact of which on the network only becomes apparent after pre-training. Instead of such a hand-built generator, this work proposes a structured prior: a small set of named component priors, linked by op...
  </details>

- **2026-11-02** — Necati Sefercioglu, Mehmet Ozan Unal, Metin Ertas et al. — [Measure Before You Repair: An Explainable Agent for Blind Restoration of Multi-Artifact 3-D MRI](http://arxiv.org/abs/2611.03996v1)
  <details><summary>📄 Abstract</summary>
  A brain MRI scan can carry an unknown mix of artifacts, so restoration has to be blind, yet most deep-learning methods are built to correct one known artifact. We present Dx-Rx, an agent in which a multimodal large language model (MLLM) measures suspected artifacts before it repairs them. To our knowledge, it is the first agent to restore whole 3-D MRI volumes, whereas earlier MRI agents restore 2-D slices. In a loop, it looks at slices of the 3-D volume, calls five diagnostic tools (noise, spik...
  </details>

- **2026-11-02** — Yan Huang, Charles Santhosam Lourdu Raja, Rajesh Gadiyar — [GTAC: A Graph-Transformer Actor-Critic for Carrier-Aware MU-MIMO User Grouping](http://arxiv.org/abs/2611.03922v1)
  <details><summary>📄 Abstract</summary>
  Achieving higher spectral efficiency (SE) in 5G and future 6G networks requires efficient massive multi-user multiple-input multiple-output (MU-MIMO) grouping under coupled physical-layer constraints and strict scheduling deadlines. Motivated by industry efforts in AI-native RAN, we propose Graph-Transformer Actor-Critic (GTAC), a deep reinforcement learning (DRL) architecture for carrier-aware MU-MIMO user grouping. The objective is to maximize the long-term proportional-fair (PF) utility of th...
  </details>

- **2026-11-02** — Denisse Córdova Carrizales, Abhijatmedhi Chotrattanapituk, L. Dagny Davis et al. — [Agentic inverse design of spatially programmed materials](http://arxiv.org/abs/2611.03795v1)
  <details><summary>📄 Abstract</summary>
  Spatially programmed functional materials, from functionally graded alloys and metamaterials to quantum superlattices, use their spatial structure to tailor physical properties. However, translating a desired spatial structure into a practical fabrication recipe remains challenging due to the complex relationship between processing conditions and resulting material structures. Here we show that a large language model (LLM) agent can inverse-design such fabrication recipes by using a physics-base...
  </details>

- **2026-11-02** — Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot — [NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains](http://arxiv.org/abs/2611.03576v2)
  <details><summary>📄 Abstract</summary>
  Law changes over time. A court decides a case under the law in force on that day, and legal QA benchmarks grade answers against today's law. We checked 156,650 decisions of four Thai courts. Up to 67% of them cite law that has since been amended or repealed. We introduce NitiBench+, the sequel of our NitiBench, a Thai legal QA benchmark with 1,670 items across 17 domains, built from decisions of three courts. For each cited section it holds both the text in force on the decision date and the cur...
  </details>

- **2026-11-02** — Linjie Xu, Yiqun Hu, Jixiang He et al. — [Why Tabular Foundation Models Excel on Relational Data They Have Never Seen](http://arxiv.org/abs/2611.02936v2)
  <details><summary>📄 Abstract</summary>
  Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As candidate targets are numerous in enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models (FMs) based on in-context learning (ICL) and RDB-specific pre-training provide a viable solution, but the ideal design still remains largely unresolved. Perh...
  </details>

- **2026-11-02** — Rukang Ma, Bingxue Wang, Liwen Zou et al. — [TME-ContextNet: Class-Conditioned Spatial Supervision and Grouped Decoding for Joint Nuclei Instance Segmentation and Classification](http://arxiv.org/abs/2611.02671v2)
  <details><summary>📄 Abstract</summary>
  Joint nuclei instance segmentation and classification requires precise boundaries and neighborhood information that helps distinguish morphologically similar cell types. We present TME-ContextNet, a multi-task framework that learns class-conditioned spatial context from existing nuclear annotations and organizes decoding into geometry-related and semantic task groups. Class-conditioned spatial supervision extends nuclear labels into a dense target using Euclidean distance transforms, requiring n...
  </details>

- **2026-11-02** — Raphael Casey, Michael Simeone, Alberto Tosato et al. — [Four Bridges: Measuring Deception Propensity in a Multi-Agent Game](http://arxiv.org/abs/2611.03600v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any instruction to deceive. We introduce Kradle, a platform for evaluating AI models, and Four Bridges, an information asymmetry game in which four agents distribute across four rooms: one is the death room, the others hold ...
  </details>

- **2026-11-02** — Yuqi Jia, Yunjie Tian, Jiayu Zheng et al. — [Axion 1.0: Open Agent Foundation Models, Simplified](http://arxiv.org/abs/2611.03233v1)
  <details><summary>📄 Abstract</summary>
  We introduce Axion 1.0, a fully open agent foundation model that combines strong and broad agentic capabilities with a remarkably simple training recipe. Axion 1.0 is trained in only three stages: two lightweight supervised fine-tuning stages followed by reinforcement learning, without dedicated mid-training, direct preference optimization (DPO), or on-policy distillation (OPD). The first SFT stage develops strong self-contained reasoning through model-aware data construction, where we synthesiz...
  </details>

- **2026-11-02** — Aswin Ramachandran, Jona Schulz, Maurus Derungs et al. — [KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL](http://arxiv.org/abs/2611.03138v1)
  <details><summary>📄 Abstract</summary>
  Progress in robot learning, particularly physical multi-agent reinforcement learning (MARL), is currently challenged by a limited availability of accessible, standardized benchmarks. While simulation-based MARL has produced remarkable emergent behaviors, from coordinated team play to complex tool use, translating these advances to physical systems remains difficult. A key barrier is infrastructural: physical platforms are often prohibitively expensive, require specialized facilities, or lack ope...
  </details>

- **2026-11-02** — Jae Wang Lee, Abhirup Banerjee, Yeong Chan Lee — [Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents](http://arxiv.org/abs/2611.02319v1)
  <details><summary>📄 Abstract</summary>
  Medical artificial intelligence agents should retrieve patient identifiers only when a task requires them, the data-minimization principle behind the HIPAA minimum necessary standard for protected health information (PHI). An agent can retrieve identifiers without revealing them. Such silent access remains invisible to evaluations that inspect only the output. We embedded canaries in synthetic patient records and linked each tool invocation to canary exposure in the final answers across five lan...
  </details>

- **2026-11-02** — Rafal Karp, Gene Liu, Shih-Hsin Li et al. — [Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data](http://arxiv.org/abs/2611.03626v1)
  <details><summary>📄 Abstract</summary>
  We present Isekai3D Synthetic Data Generation (SDG), a platform for simulating and capturing synthetic 3D gameplay for research in vision and world models, neural graphics, gameplay agents, and other applications. The platform combines reusable environment and character assets with Unreal Engine plugins in a two-stage workflow. First, world simulation generates gameplay while recording the world state, character movements, actions, and camera tracks needed for replay. Second, the recorded simula...
  </details>

- **2026-11-02** — Abdellah Rahmani, Sean McLeish, Ang Li et al. — [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](http://arxiv.org/abs/2611.03526v1)
  <details><summary>📄 Abstract</summary>
  Computer programmers chain together the same reusable computational primitives, for example, conditional statements or loops, but in different orders to implement different algorithms. In contrast, existing language model architectures always execute their layers in the same order. We introduce Library of Layers (LoL), an architecture that dynamically orders its layers during inference to solve the problem at hand. LoL has a single hyperparameter, the size of its global library of transformer bl...
  </details>

- **2026-11-02** — Wen-Hsuan Liu, Amara Okonkwo, Tom Saliencro et al. — [RASP: Read-All, Sparse-Plasticity Continual Learning in a Stationary-Size LoRA](http://arxiv.org/abs/2611.03513v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient continual learning on pre-trained Vision Transformers largely relies on a costly premise: preventing catastrophic forgetting requires either spawning a dedicated LoRA branch per session---causing adapter parameters to scale linearly with task horizon---or applying sparse Mixture-of-Experts gating symmetrically to both forward and backward passes, which sacrifices representational rank at test time. We argue that reading consolidated knowledge and writing new task credit are f...
  </details>

- **2026-11-02** — Felix Koulischer, Gianni Van De Velde, François Remy et al. — [Online Class Posteriors for Interpretable and Controllable Discrete Diffusion](http://arxiv.org/abs/2611.03454v1)
  <details><summary>📄 Abstract</summary>
  Discrete diffusion models remain far less understood than their continuous counterparts, despite recent breakthroughs across modalities, most notably in text. Leveraging tools from continuous diffusion, we formulate a theoretical framework to track the class-conditional posterior in an online manner by combining conditional and unconditional model predictions. In masked language modeling, this posterior offers highly interpretable dynamics: tokens aligned with a class boost the posterior, while ...
  </details>

- **2026-11-02** — Yumou Liu, Mingju Chen, Zhoufutu Wen et al. — [DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](http://arxiv.org/abs/2611.03412v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a time, leaving a gap between the capability we measure and the outcome that makes agents useful. To address this gap, we introduce DeliverBench, which tests whether agents can carry a project from brief to final delivery. I...
  </details>

- **2026-11-02** — Elizabeth G. Campolongo, Eric R. Sokol, Marty Downs et al. — [From FAIR to AI-FAIR Metadata-First Infrastructure for AI-Enabled Science](http://arxiv.org/abs/2611.03327v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) technologies and their capabilities have advanced rapidly over the past few years, leading to widespread interest and adoption in the biological and ecological sciences. However, the data infrastructure and computational resources that provide the foundation for AI workflows in ecology and biodiversity science remain fragmented. Moreover, the flow of value remains largely unidirectional: data move from collectors, through repositories and aggregators into models, and...
  </details>

- **2026-11-02** — Xueyang Feng, Xiaohe Bo, Xu Chen et al. — [From Local Skills to Long-Horizon Web Tasks: Progressive Skill Exploration for LLM Web Agents](http://arxiv.org/abs/2611.03116v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are driving autonomous agents toward real-world environments, with the Web emerging as one of the most representative interaction scenarios. However, training Web agents with naive exploration remains challenging: successful trajectories are rare, and the sparse terminal rewards make it difficult for agents to obtain useful feedback from failed trajectories. Inspired by skill acquisition theory, we propose Skill-Composed Progressive Exploration (SCOPE), a short-to-lo...
  </details>

- **2026-11-02** — Zheng Wu, Xinbei Ma, Yao Yao et al. — [Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents](http://arxiv.org/abs/2611.03092v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents amplify human agency: enabling people to pursue their goals with less routine supervision while retaining control over consequential decisions. We advocate Avatar Intelligence, a paradigm of persistent personal agents th...
  </details>

- **2026-11-02** — Haoyi Xiong, Yi Liu, Jiang Bian et al. — [Towards a Trustworthy and Governable Internet of Agentics: An Architectural Perspective on Protocols, Systems, and Services](http://arxiv.org/abs/2611.03066v1)
  <details><summary>📄 Abstract</summary>
  Large language model applications are increasingly being organized as tool-using and multi-agent workflows rather than as isolated chat interfaces. This perspective paper examines the architectural problem that follows from that shift: agents may reason, invoke tools, and delegate work, but dependable deployment still requires interoperability across frameworks, runtimes, data boundaries, and organizational control domains. We study this problem through the lens of the \emph{Internet of Agentics...
  </details>

- **2026-11-02** — Yihan Fang, Yuxin Tian, Ruixiang Wang et al. — [PointPilot: Unified Robotic Manipulation via Object-Centric 3D Point Flow Prediction](http://arxiv.org/abs/2611.02930v1)
  <details><summary>📄 Abstract</summary>
  Generalization remains a central challenge in robotics, calling for policies that address domain variations from multiple dimensions such as diverse embodiments, camera poses, and/or scene layouts. In order to approach this problem, we introduce PointPilot, a task-focused and 3D aligned manipulation framework built on a 3D space point-flow prediction. Rather than modeling the global scene, PointPilot only represents task-focused objects (robot grippers treated as objects), avoiding the predictio...
  </details>

- **2026-11-02** — Thapelo Sindane, Unarine Netshifhefhe, Vukosi Marivate et al. — [Maswao: An automatically collected, prepared, and benchmarked dataset for the South African Sign language](http://arxiv.org/abs/2611.02903v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in sign language processing can be attributed to developments in both large-scale dataset collection and algorithmic complexity in areas such as pose estimation techniques, signal processing through Transformer models, and model optimization. However, only a handful of sign languages, such as the American, British, and German, from over 200 globally recognized sign languages, reap the benefits of such advancements, while the rest lag behind. In this study, we aim to address t...
  </details>

- **2026-11-02** — Yingtao Ren, Xiao Luo, Yiwei Fu et al. — [TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation](http://arxiv.org/abs/2611.02810v1)
  <details><summary>📄 Abstract</summary>
  This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinations. Towards this end, we propose a novel approach named Task Refinement with Individual Optimization (TRIO) for RAG. The core idea of our TRIO is to equip three well-designed agents with an iterative refinement paradigm...
  </details>

- **2026-11-02** — Felix Mächtle, Gautham Sriram, Manjil Neupane et al. — [Rethinking Neural Decompilation: Candidate Selection as the Hidden Bottleneck](http://arxiv.org/abs/2611.02788v1)
  <details><summary>📄 Abstract</summary>
  Reverse engineering obfuscated binaries is a core task in malware analysis and software security auditing. While neural decompilers based on Large Language Models (LLMs) have improved the readability and functional fidelity of recovered code over heuristic tools such as Ghidra and IDA Pro, a substantial gap remains between best-sample performance and practical single-output accuracy, particularly under code obfuscation. We study this gap through the lens of candidate generation and candidate sel...
  </details>

- **2026-11-02** — Mengzhao Wang, Yanli Ji, Peng Ye — [Lookahead Prediction-Guided Adaptive Visual Refocusing for Interleaved Multimodal Reasoning](http://arxiv.org/abs/2611.02780v1)
  <details><summary>📄 Abstract</summary>
  Interleaved multimodal chain-of-thought reasoning improves the visual reasoning capabilities of multimodal large language models by dynamically incorporating visual evidence during reasoning. However, existing methods primarily select evidence from historical context. When the reasoning focus shifts, history-guided evidence may remain focused on prior regions and fail to cover the visual information required by the next step. We refer to this lag between visual evidence and subsequent reasoning ...
  </details>

- **2026-11-02** — Jiale Lao, Immanuel Trummer — [Stop Handcrafting Your Engine! GenDB-V: Towards AI-Generated and Formally Verified Database Systems](http://arxiv.org/abs/2611.02779v1)
  <details><summary>📄 Abstract</summary>
  For over 50 years, the database community has developed a wide range of successful engines to answer two fundamental questions: how can database systems run faster, and how can we ensure their correctness? Experience with these engines shows that performance depends on hardware and workloads. As both change over time, we repeatedly redesign and rebuild database systems, a time-consuming and expensive process. Correctness remains another long-standing challenge: recent studies continue to uncover...
  </details>

- **2026-11-02** — Xiangyun Luo, Yunkai Zhang, Yong Huang et al. — [Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model](http://arxiv.org/abs/2611.02738v1)
  <details><summary>📄 Abstract</summary>
  Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inferences lack clear links to physical-mechanical laws; and experts' tacit knowledge remains difficult to formalize. This study proposes a knowledge-enhanced autonomy formalization methodology and apply it to construct the...
  </details>

- **2026-11-02** — Xiangrui Meng, Jingcheng Liu, Ke Wang et al. — [Human-Supervised Artificial Intelligence Researchers in Electric Power Systems: Knowledge, Physics, Simulation, and Governance for Large Language Models](http://arxiv.org/abs/2611.02711v1)
  <details><summary>📄 Abstract</summary>
  Conclusions in power-system research require a clear evidential basis. Researchers need to understand the data sources, modelling assumptions, and solution procedures to assess the conditions under which a conclusion holds. Large language models (LLMs) can help researchers extract information from documents and translate research requests into code and tool calls, but their outputs still require physical validation. Focusing on human-supervised artificial intelligence (AI) researchers, this revi...
  </details>

- **2026-11-02** — Mei Chen, Yu Xia, Haipeng Mao — [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](http://arxiv.org/abs/2611.02659v1)
  <details><summary>📄 Abstract</summary>
  Producing an executable CAD script is not sufficient to establish that an agent has satisfied an engineering design request. Evaluation must also consider the resulting geometry, specified dimensions, and native CAD modeling history. We present Parametric CAD Bench v3, a 100-task benchmark comprising 30 text-to-CAD creation tasks, 30 text-to-CAD create-and-edit tasks, and 40 tasks that reconstruct mechanical parts from engineering drawings. Agents operate in a pinned FreeCAD environment and subm...
  </details>

- **2026-11-02** — Sean Wu, Aneesh Pappu, Jiaru Zou et al. — [Measuring AI Agents as Teammates with Collaborative Intelligence](http://arxiv.org/abs/2611.02633v1)
  <details><summary>📄 Abstract</summary>
  Progress in AI is often measured by what a single model can do on its own. Yet teams of AI agents are starting to make breakthroughs and discoveries in science, medicine, mathematics and software engineering. As AI begins to work in teams of agents and people, the ability to collaborate becomes a core part of their intelligence. Research on human teams has measured this ability for decades. Inspired by this, we introduce the Collaborative Intelligence Benchmark, which measures how well an AI age...
  </details>

- **2026-11-02** — Yingshu Li, Shaoyang Zhou, Zhanyu Wang et al. — [MedHEB: Benchmarking Medical Embeddings Across Heterogeneous Clinical Evidence](http://arxiv.org/abs/2611.02519v1)
  <details><summary>📄 Abstract</summary>
  Clinical evidence is inherently relational: medical images are interpreted with prior studies, cross-modal examinations, reports, and localized findings, and retrieving relevant evidence is therefore central to clinical interpretation. Recent foundation models increasingly encode these heterogeneous sources into shared embedding spaces, yet existing embedding evaluation often focuses on isolated matches, leaving unclear whether current models retrieve relevant evidence across changes in modality...
  </details>

- **2026-11-02** — Alexander Valverde, Danny Xie-Li, Zhichao Wang et al. — [Blueprint2CAD: Benchmarking Foundation Models on Engineering Drawing-to-CAD Render Correspondence](http://arxiv.org/abs/2611.02433v1)
  <details><summary>📄 Abstract</summary>
  Engineering drawings specify mechanical parts through orthographic projections. Recognizing which part a drawing depicts underlies part search, design reuse, and digitization, yet no public benchmark measures whether vision models can do it. We introduce Blueprint2CAD, a benchmark for drawing-to-render correspondence: given an orthographic line drawing and a shaded render, usually from another viewpoint, decide whether they show the same part. Its data layer, BlueCAD-30K, applies an open draftin...
  </details>

- **2026-11-02** — Zirui Ma, Zhihua Fan, Haibin Wu et al. — [SCARF: A Scene-Adaptive Depth-Guided G-3DGS Encoder Accelerator with Semantic Reuse and Fused Dataflow](http://arxiv.org/abs/2611.02365v1)
  <details><summary>📄 Abstract</summary>
  Depth-guided, cost-volume-based Generalizable 3D Gaussian Splatting (G-3DGS) encoders reconstruct scenes as sets of Gaussian primitives directly from multi-view images without requiring per-scene optimization, thereby facilitating feed-forward novel-view synthesis on edge computing platforms. However, their shared encoder architecture presents two primary bottlenecks. First, the per-pixel depth search disregards semantic similarity within the 2D feature space, causing depth search operations to ...
  </details>

- **2026-11-02** — Eirik Botten Nicolaysen — [Does a Norwegian further-trained model give more outdated legal values than its base model? A preregistered paired comparison of Borealis 2 and Gemma 4](http://arxiv.org/abs/2611.02334v1)
  <details><summary>📄 Abstract</summary>
  We compare how often two released language models give outdated numeric values from Norwegian statutes and regulations: NbAiLab/borealis2-26b-a4b-preview (Borealis 2), which the National Library of Norway further trained from google/gemma-4-26B-A4B-it (Gemma 4), and Gemma 4 itself. The study was preregistered (doi:10.5281/zenodo.23858965) and uses the closed norregel benchmark, scored deterministically against a value history. On the 411 of 503 primary items where both models gave an interpretab...
  </details>

- **2026-11-02** — Yujiao Shen, Jiahe Song, Haitian Li et al. — [EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human Videos](http://arxiv.org/abs/2611.03646v1)
  <details><summary>📄 Abstract</summary>
  Learning from human data offers a scalable path toward embodied intelligence, yet it requires models to accurately understand fine-grained human actions from egocentric observations. However, existing benchmarks remain limited in action atomicity, temporal precision, and hand-action association. We introduce EgoActionBench, a benchmark that represents continuous human manipulation as temporally localized atomic actions associated with the left hand, right hand, or both hands. EgoActionBench cont...
  </details>

- **2026-11-02** — Arda Uzunoglu, Mahler Revsine, Michael Schatz et al. — [Tracing the Scientific Discovery Capacity of LLMs to Their Training Data](http://arxiv.org/abs/2611.03617v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) show growing promise for scientific discovery, yet basic questions remain about what enables reliable discovery. How can we trace the scientific discovery capacity of LLMs to their training data? We study this question as one of missing probability mass and develop a theoretical account in which monofacts-the facts observed once during training-set the discovery capacity. In materials science and regulatory genomics, we directly manipulate monofact rates in training ...
  </details>

- **2026-11-02** — Utkarsh A. Mishra, Alperen Degirmenci, Yongxin Chen et al. — [TAMPAgent: Agentic Belief-Space Planning for Mobile Manipulation](http://arxiv.org/abs/2611.03584v1)
  <details><summary>📄 Abstract</summary>
  Open-world robotic mobile manipulation requires acting in physical environments with only partial information. While recent Large Vision-Language Model (LVLM) agents show strong open-world reasoning capabilities, existing architectures that rely on direct tool calling struggle with geometric uncertainty and thus are limited to fully-observable tabletop environments. In contrast, Task and Motion Planning (TAMP) systems can solve long-horizon tasks under partial observability but incur high comput...
  </details>

- **2026-11-02** — Xuanyou Chen, Jinyu Chen, Glen Chou — [VerifLM: Physically Verified Image-Edit-Guided Goal Pose Generation for Robotic Manipulation](http://arxiv.org/abs/2611.03268v1)
  <details><summary>📄 Abstract</summary>
  Many manipulation goals are easier to visualize than to specify numerically through explicit geometric constraints. We present VerifLM, a framework that converts image-edited goal configurations into physically verified 6-DoF object poses for planning. Using an edited image, VerifLM recovers an initial relative pose between an active object and a passive object, then prompts a vision-language model to generate axis-wise sampling constraints and a task-specific validation program. Candidate poses...
  </details>

- **2026-11-02** — Nishan Chatterjee, Matthew Purver, Antoine Doucet et al. — [Finding Errors Is Not Enough: Selective Model Escalation for Entity-Targeted Sentiment Analysis](http://arxiv.org/abs/2611.02989v1)
  <details><summary>📄 Abstract</summary>
  Improving a sentiment classifier with limited resources involves more than simply deciding how much data to collect or which model to train. A labelled collection may lack examples of an important class. Once trained, a classifier may benefit from another model even when that model is weaker on its own. We study these decisions in document-level Entity-Level Sentiment Analysis (ELSA), primarily using South Slavic news. We first compare acquisition orders as collections grow. We then use uncertai...
  </details>

- **2026-11-02** — Minhyeon Oh, Chiyeong Heo, Geonwoo Noh et al. — [Action Verification through Conjecture and Refutation for Language Model Agents](http://arxiv.org/abs/2611.02950v1)
  <details><summary>📄 Abstract</summary>
  Language model agents increasingly act on users' behalf by manipulating external environments through tools, often from high-level instructions that leave critical task- and environment-specific context unstated. To prevent resulting misaligned actions, recent work verifies proposed actions before execution, largely by establishing whether the conditions supporting them hold. We argue that this confirmation-oriented view leaves a fundamental blind spot: a wrong action often passes every check th...
  </details>

- **2026-11-02** — Catherine Li, Jingchu Gai, Andrej Risteski et al. — [Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap](http://arxiv.org/abs/2611.03633v1)
  <details><summary>📄 Abstract</summary>
  Muon has recently emerged as a promising optimizer for pretraining large language models, offering a speedup over AdamW in minimizing pretraining loss. However, it remains unclear whether Muon's advantage persists after fine-tuning. In this paper, we study the downstream behavior of Muon and AdamW and uncover a surprising trend: beyond a sufficiently large pretraining data budget, AdamW outperforms Muon after fine-tuning. Moreover, as model size increases, AdamW overtakes Muon at progressively s...
  </details>

- **2026-11-02** — Marius Memmel, Shawn Yin, Urvi Rutia et al. — [D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models](http://arxiv.org/abs/2611.03622v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) hold promise for zero-shot video task-progress estimation in robot learning, yet existing frameworks frequently suffer from confirmation bias, hallucinating progress in failed executions due to implicit success assumptions or relative temporal ranking designs. Naive prompting of frontier models collapses into a binary success detector that fails to capture nuanced, non-linear progress and failures. While post-training approaches can mitigate this through explicit tr...
  </details>

- **2026-11-02** — Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot — [NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains](http://arxiv.org/abs/2611.03576v1)
  <details><summary>📄 Abstract</summary>
  Law changes over time. A court decides a case under the law in force on that day, and legal QA benchmarks grade answers against today's law. We checked 156,650 decisions of four Thai courts. Up to 67% of them cite law that has since been amended or repealed. We introduce NitiBench+, the sequel of our NitiBench, a Thai legal QA benchmark with 1,670 items across 17 domains, built from decisions of three courts. For each cited section it holds both the text in force on the decision date and the cur...
  </details>

- **2026-11-02** — J. Climent Vidal, E. Cosme Llópez, R. Ruiz Mora et al. — [Higher-order many-sorted categorial algebras via generalized hep-derivors](http://arxiv.org/abs/2611.03553v1)
  <details><summary>📄 Abstract</summary>
  Higher-order many-sorted categorial algebras are many-sorted algebras whose carriers are strict higher-order categories and whose operations are higher-order functors. They admit a homogeneous and a heterogeneous presentation, both by partial algebras whose operation domains are given by existence equations. To relate these presentations and their dimensions, we introduce generalized hep-derivors between hierarchical equationally partial signatures. A generalized hep-derivor selects carriers by ...
  </details>

- **2026-11-02** — Alberto Liardi, George Blackburne, Pedro A. M. Mediano — [An information-geometric formulation of distributed computation](http://arxiv.org/abs/2611.03545v1)
  <details><summary>📄 Abstract</summary>
  Understanding how complex systems perform computations, i.e. how they store, transmit, and transform information across their components, is a major goal across the natural sciences. However, characterising genuinely collective computations across multiple inputs and outputs that cannot be reduced to contributions from individual components remains an open problem. In this work, we introduce $Φ\text{ID}^{IG}$, a geometric theory of information dynamics that captures irreducible collective phenom...
  </details>

- **2026-11-02** — Marcus Chen I Wada, Sina Mohammadi, Van-Hai Bui et al. — [Transformer-guided Variable Projection for Phasor and Fault-Time Estimation Under DDC Offset](http://arxiv.org/abs/2611.03416v1)
  <details><summary>📄 Abstract</summary>
  Decaying DC (DDC) offsets introduce substantial phasor estimation errors during the first post-fault cycle. Recent approaches have sought interpretable waveform representations, but identifying analytical expressions can incur substantial computational costs. This paper proposes a transformer-guided variable-projection estimator that extracts the fundamental phasor, DDC parameters, and fault inception time from point-on-wave (POW) samples as an interpretable analytical expression. An offline-tra...
  </details>

- **2026-11-02** — Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini et al. — [The SIMPLE Law for Energy Cost of LLM Inference](http://arxiv.org/abs/2611.03330v1)
  <details><summary>📄 Abstract</summary>
  Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs, and the most accurate SOTA model is a fit, not a law: it absorbs architecture into fitted coefficients, requiring per-LLM fitting. We derive closed-form expressions of the computational and memory-access complexity of LLM inference ...
  </details>

- **2026-11-02** — Andrei-Alexandru Manea, Jindřich Libovický, Philipp J. Rösch — [MultiInpaintCOCO: Fine-Grained Visual Understanding in Multiple Languages](http://arxiv.org/abs/2611.03309v1)
  <details><summary>📄 Abstract</summary>
  Previous research shows that vision-language (VL) models struggle to understand fine-grained image details and tend to focus on the overall layout. Moreover, any weakness in English tends to be further amplified in the multilingual setting. To study that, we extend InpaintCOCO, an English dataset focused on fine-grained visual details, to 13 typologically diverse languages across five language families, creating MultiInpaintCOCO - a new multilingual benchmark of 953 minimal-pair examples. We fur...
  </details>

- **2026-11-02** — Zhuoli Ouyang, Changxi Chi, Siyuan Li et al. — [ENGINE: Endogenous Variational MultiScale Optimization for Zeroth-Order LLM Fine-Tuning](http://arxiv.org/abs/2611.03293v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization enables memory-efficient large language model (LLM) fine-tuning, and recent methods incorporate curvature-aware strategies. However, in the high-dimensional parameter space of LLMs, these methods inherently suffer from exploding gradient variance and prohibitive costs. Conversely, confining updates to a low-dimensional subspace reduces variance but discards critical high-dimensional information, degrading performance. This creates a fundamental dilemma: full-space ...
  </details>

- **2026-11-02** — Ye Tian, Anzhi Sheng, Angela Fontan et al. — [Susceptibility optimization for wisdom of crowds: A social power reformulation and realization framework](http://arxiv.org/abs/2611.03240v1)
  <details><summary>📄 Abstract</summary>
  Whether social influence makes a crowd wiser or more biased hinges on who yields to others and who holds firm. Such heterogeneous susceptibilities to social influence, together with the influence network, determine the weight each agent's initial estimate carries in the collective estimate, known as social power. This paper studies susceptibility optimization for maximizing the wisdom of crowds under the Friedkin-Johnsen model. Minimizing the squared collective bias over susceptibilities leads t...
  </details>

- **2026-11-02** — Alfonso Cannavale, Alessandra Parziale, Valeria Pontillo et al. — [Specification-Driven Governance for Fairness-by-Design in Agentic Software Engineering: How Far Can We Go?](http://arxiv.org/abs/2611.03231v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is shifting developers' responsibilities from software implementation to software governance. While this paradigm improves productivity, it also raises challenges in ensuring that autonomous coding agents preserve developers' intentions. Among these, operationalizing fairness-by-design is largely unexplored, as existing approaches provide limited support for representing and propagating fairness requirements throughout agentic development workflows. In this paper, we investigate wheth...
  </details>

- **2026-11-02** — Hamidreza Eivazi, Eslam Sharaawy, Stefan Wittek et al. — [FlowBatt: Flow Matching for Probabilistic Battery Degradation Prediction](http://arxiv.org/abs/2611.03150v1)
  <details><summary>📄 Abstract</summary>
  Battery degradation remains a central challenge in the development and broad application of sustainable energy technologies. Accurate degradation prediction is challenging, as battery aging emerges from complex and heterogeneous interactions among cycling behavior, operating conditions, and cell chemistry. Existing machine-learning approaches typically focus on deterministic end-of-life predictions or modeling degradation curves within fixed chemistry settings, leaving probabilistic state of hea...
  </details>

- **2026-11-02** — Zichong Zhu, Zhihao Liu, Andrei Sharf et al. — [Visual-to-Executable Procedural Reconstruction of Buildings](http://arxiv.org/abs/2611.03143v1)
  <details><summary>📄 Abstract</summary>
  Procedural modeling offers compact, editable, and reusable representations for architectural content, but building such models still depends heavily on manually authored grammars. We study image-based procedural building reconstruction from in-the-wild images, with the goal of recovering an executable procedural description that can be instantiated as an editable 3D building asset. Because a single image provides only partial and view-dependent evidence, we focus on recovering the dominant visib...
  </details>

- **2026-11-02** — Furkan Yasir Goksu, Yaren Yilmaz, Sule Gunduz Oguducu — [Preprocessing Choices in Fine-Tuning Data Matter: Utility and Demographic Sensitivity in LLM-Based Recommendation](http://arxiv.org/abs/2611.03113v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have introduced a generative approach to recommendation, producing item lists from textual representations of user histories and item information. However, this generative setting raises challenges concerning output validity, prompt consistency, and sensitivity to demographic descriptors. In this work, we investigate how preprocessing choices in fine-tuning data affect recommendation utility and fairness-related behavior in a generative LLM-based recommender system. ...
  </details>

- **2026-11-02** — Junzhao Huang, Xi Wu, Zihan Wang et al. — [PACERec: Progressive Adaptation of LLM Item Embeddings with Collaborative Evidence for Recommendation](http://arxiv.org/abs/2611.03068v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) embeddings have been increasingly adopted in sequential recommendation to encode static item attributes and alleviate the limitations of item ID embeddings under sparse interactions. However, these embeddings typically capture only static content similarity while neglecting sequential transitions, and since their adaptation quality relies on sparse per-item updates or global geometric calibration, existing methods still struggle to explicitly transfer preceding interac...
  </details>

- **2026-11-02** — Tomáš Knap, Ivana Kvapilíková, Jan Černý et al. — [Unlocking Criminal Court Decisions: Flexible Information Extraction for Empirical Legal Research](http://arxiv.org/abs/2611.03051v1)
  <details><summary>📄 Abstract</summary>
  Criminal verdicts contain descriptions of criminal behavior that can support quantitative legal research, but structuring them requires attributes and extraction rules that cannot always be fully specified in advance. We present an LLM-based pipeline that builds a structured dataset through attribute exploration, text span extraction, and value normalization, guided by annotation instructions that legal experts can refine. We evaluate it on two traffic offenses: driving under the influence (DUI)...
  </details>

- **2026-11-02** — Ihor Vitenko — [VERS: Steering Reasoning Models by Editing Their Activation Explanations](http://arxiv.org/abs/2611.03040v1)
  <details><summary>📄 Abstract</summary>
  Reasoning language models write a chain of thought before they answer, and many checks in it do not change the final answer. Natural language autoencoders (NLAs) explain a model's activations in text and rebuild activations from text, and editing an explanation can steer a model at a single token. We study whether such edits can also steer how a model reasons. We build VERS (Verbalize, Edit, Reconstruct, Steer): it turns explanation edits at the doubt points of one reasoning trace into one fixed...
  </details>

- **2026-11-02** — Yanchao Bi, Pengfei Chen, Yulong Yan et al. — [Q-CamTuning: A Multimodal Large Language Model for Fine-Grained Quality Reasoning in Livestreaming Camera Tuning](http://arxiv.org/abs/2611.03007v1)
  <details><summary>📄 Abstract</summary>
  With the popularization of livestreaming applications, automatic camera tuning has become indispensable for ordinary users to enjoy high Quality of Experience (QoE). However, the existing Image Quality Assessment (IQA) methods face two challenges in camera tuning. First, they struggle to identify subtle quality difference between images, which is common in camera tuning. Second, the ability to explain fine-grained differences and to provide suggestions for camera tuning are even more lacking. To...
  </details>

- **2026-11-02** — Linjie Xu, Yiqun Hu, Jixiang He et al. — [Why Tabular Foundation Models Excel on Relational Data They Have Never Seen](http://arxiv.org/abs/2611.02936v1)
  <details><summary>📄 Abstract</summary>
  Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As candidate targets are numerous in enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models (FMs) based on in-context learning (ICL) and RDB-specific pre-training provide a viable solution, but the ideal design still remains largely unresolved. Perh...
  </details>

- **2026-11-02** — Stanislav Kosorin, Trever Schirmer, Leonard Wossnig et al. — [Dispatch Control for Priority-Based, Multi-Tenant Workflows under Multi-Resource External Rate Limits](http://arxiv.org/abs/2611.02926v1)
  <details><summary>📄 Abstract</summary>
  Workflow engines orchestrate pipelines of activities, which often call external APIs, on a fixed pool of worker slots, the threads that run them. When an API enforces a hard rate limit shared by all tenants and priorities, a throttled call that retries after a backoff keeps its worker slot and starves other tenants. Large Language Model provider APIs are particularly complex: their per-organization caps are low and bind independently on requests and tokens per minute. The operator can neither re...
  </details>

- **2026-11-02** — Yuan-Kang Lee, Kuan-Lin Chen, Chia-Che Chang et al. — [PhotoGuider: Composition-Aware Cropping and 360$^{\circ}$ View Framing with Explainable Photographic Assessments](http://arxiv.org/abs/2611.02897v1)
  <details><summary>📄 Abstract</summary>
  Traditional image cropping assumes the photograph already contains the composition worth keeping, and asks only where to crop. A full 360$^{\circ}$ scene offers no such guarantee: the viewing direction in a scene has to be discovered before anything can be framed. We present PhotoGuider, a measure-then-frame method that answers both questions with compact learned scorers over one shared set of composition-aware features. The designed features are extracted using foundation and task-specific visi...
  </details>

- **2026-11-02** — Guangyuan Dong, Lingdong Shen, Xudong Zhang et al. — [Bridging Low-Level Image Fusion and High-Level Semantic Understanding](http://arxiv.org/abs/2611.02896v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing image fusion and semantic interpretation are usually optimized separately, so reconstruction quality need not preserve downstream retrieval utility. We propose LANCE, which uses structured language as an explicit, indexable semantic state. A frozen vision-language model maps the input to a closed-vocabulary text record; a language-conditioned generator fuses the imagery; and a dense verifier with a differentiable continuous summarizer re-describes the output. Text-text consistency...
  </details>

- **2026-11-02** — Viju Sudhi, Giulio Billi, Andreea Scrob et al. — [Tug of Watts: A study on the Energy - Accuracy Trade-off of Large Language Models on Medical Question Answering Tasks](http://arxiv.org/abs/2611.02889v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in medical question answering (QA) systems. While recent works aim at incrementally improving the downstream task accuracy, an empirical estimation of the models' energy consumption and the associated carbon footprints is often overlooked. In this study, we demonstrate how practitioners can estimate energy consumption and arrive at reliable emission estimates for medical QA tasks available in the OpenMedical-LLM leaderboard by investigating 13 L...
  </details>

- **2026-11-02** — Zhengyang Yu, Akio Hayakawa, Masato Ishii et al. — [Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](http://arxiv.org/abs/2611.02822v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to compounding exposure bias. To stabilize long rollouts, recent methods heuristically adopt frame sink, keeping initial frames as a persistent model context, inspired by attention sinks in LLMs. We revisit this design and find that the mechanism by which initial frames stabilize long-range consistency in AR-VDMs is not a...
  </details>

- **2026-11-02** — Mengda Li, Jianfeng Yao — [Spectral Degeneration of Self-Attention under Isotropic Score Geometry](http://arxiv.org/abs/2611.02778v1)
  <details><summary>📄 Abstract</summary>
  We study the spectral structure of the self-attention matrix in Transformer models through an idealized spectral model for the pre-softmax score matrix. Motivated by the rotational isotropy of query and key representations, our model replaces the random token-space orientation of the score matrix by its canonical singular-value representative with a logarithmic spike--bulk separation. Empirical diagnostics on pretrained vision and language transformers motivate this model: token-space singular m...
  </details>

- **2026-11-02** — Shi Shu, Hao Chen, Baopu Qiu et al. — [Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce Relevance](http://arxiv.org/abs/2611.02758v1)
  <details><summary>📄 Abstract</summary>
  Relevance modeling is fundamental to e-commerce search, determining how well retrieved products satisfy the needs expressed in a user's query. Accurate judgments require interpreting user intent, comparing product attributes, and applying business-specific matching criteria. Current methods based on large language models (LLMs) leverage contextual understanding and reasoning, focusing on incorporating domain-specific context and enhancing reasoning performance. Despite these advances, difficult ...
  </details>

- **2026-11-02** — Huanzhi Mao, Yichuan Wang, Michael Koo et al. — [GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation](http://arxiv.org/abs/2611.02698v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model (VLM) agents that act in the open world need two abilities: world knowledge to interpret what they see, and exploration to find what they cannot yet see. We study how agents combine the two through interactive visual geolocation. GeoGuesser Bench contains 282 tasks in an offline Street View environment where agents rotate, zoom, and move between real panoramas. Its three task types shift the balance from knowledge to exploration: agents (1) report the coordinates of their s...
  </details>

- **2026-11-02** — Rukang Ma, Bingxue Wang, Liwen Zou et al. — [TME-ContextNet: Class-Conditioned Spatial Supervision and Grouped Decoding for Joint Nuclei Instance Segmentation and Classification](http://arxiv.org/abs/2611.02671v1)
  <details><summary>📄 Abstract</summary>
  Joint nuclei instance segmentation and classification requires precise boundaries and neighborhood information that helps distinguish morphologically similar cell types. We present TME-ContextNet, a multi-task framework that learns class-conditioned spatial context from existing nuclear annotations and organizes decoding into geometry-related and semantic task groups. Class-conditioned spatial supervision extends nuclear labels into a dense target using Euclidean distance transforms, requiring n...
  </details>

- **2026-11-02** — Amin Najafgholizadeh — [Train the Sampler You Run: Few-Step Masked Diffusion Language Models via Mixture-Likelihood Fine-Tuning](http://arxiv.org/abs/2611.02666v1)
  <details><summary>📄 Abstract</summary>
  When a masked diffusion language model is sampled in a few parallel steps in a random order, the model actually run is a mixture over reveal plans, while cross-entropy training fits token conditionals rather than this mixture. We introduce mixture-likelihood fine-tuning (Mix-FT), which fine-tunes a pretrained model on an importance-weighted bound of its own sampler's likelihood, with no teacher and no change to the architecture or the sampler. On LLaDA-8B, a LoRA fine-tune for 0.002% of the pret...
  </details>

- **2026-11-02** — Elisabeth Mayrhuber, Ting Hu, Stephan Winkler — [Evolving Explanations: Complexity-Adaptive Refinement of Faithful Explanations for Symbolic Regression](http://arxiv.org/abs/2611.02634v1)
  <details><summary>📄 Abstract</summary>
  Natural-language explanations generated by large language models (LLMs) for machine learning models often seem fluent but are not necessarily faithful to the underlying model. We formalize this mismatch as a faithfulness gap and propose a complexity-adaptive refinement framework for symbolic regression that iteratively generates and validates explanations until numerical agreement with the target expression is achieved. The approach follows a two-stage pipeline: an explainer LLM produces textual...
  </details>

- **2026-11-02** — Haris Ghafoor, Minjee Seo, Seonaeng cho et al. — [SMILE: A Structured Multi-Agent Clinical Reasoning for Liver Ultrasound Understanding](http://arxiv.org/abs/2611.02581v1)
  <details><summary>📄 Abstract</summary>
  Automated liver ultrasound report generation improves the diagnosis of liver diseases by producing clinically structured descriptions of anatomical and disease-related findings. However, current generative vision-language models (VLMs) often rely on a single reasoning pathway that maps ultrasound appearance directly to textual descriptions. In addition to the inherent vision-language modality gap, this design is limited for liver ultrasound because disease interpretation is constrained by subtle...
  </details>

- **2026-11-02** — Johanna Einsiedler — [Comparing the Empirical Content of Economic Theories](http://arxiv.org/abs/2611.02565v1)
  <details><summary>📄 Abstract</summary>
  A fitted theory that predicts well may do so because of the structure it commits to or because it was fitted to the data it is evaluated on. We propose measures that separate the two by operationalising a theory as a functional form, a support restriction on behavior and a distribution over the parameters, with no parameter fitted to the evaluation sample. Probabilistic completeness is the share of the predictable variation that a rule drawn from the theory captures out of sample. Probabilistic ...
  </details>

- **2026-11-02** — Takaya Tamamoto, Tomoko Yonezawa — [Touching Projected Agents through the DAT Screen -System Design and Questions of Interaction Boundaries-](http://arxiv.org/abs/2611.02525v1)
  <details><summary>📄 Abstract</summary>
  Touching a virtual agent involves more than detecting a finger on a display: the contact surface can deform and resist the user's push, and the agent can respond to that action. We describe the Desktop Amid Touch (DAT) screen, which combines spatial projection onto a semi-transparent, deformable mesh with touch sensing and motorized control of resistance to indentation. An initial prototype detected a single touch and estimated its position and depth from tension changes around a flexible projec...
  </details>

- **2026-11-02** — Ziyi Chen, Yan Zhang, Jianhui Wei et al. — [RLiD: Reinforcement Learning in the Decision Plane for Language Agents and LLMs](http://arxiv.org/abs/2611.02455v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has improved the capabilities of large language models (LLMs) across a wide range of tasks. However, token-level RL assigns an action's advantage to the entire generated response, including tokens specifying the parsed action, reasoning chains, and malformed content. Although the environment executes only the parsed action, variation in how the action is expressed in natural language can introduce additional variance into policy-gradient estimates. We propose RLiD (Re...
  </details>

- **2026-11-02** — Jinwen Luo, Han Jiang, Ziang Xiao et al. — [Diagnosing Model--Item Interactions in Language Model Benchmarks with LSIRM](http://arxiv.org/abs/2611.02432v1)
  <details><summary>📄 Abstract</summary>
  Language models with similar benchmark accuracy can succeed on different items. Overall scores do not show where their performance differs or which item properties might explain those differences. We demonstrate how the latent space item response model (LSIRM) can help evaluators investigate these patterns and their consequences for model comparison. We analyze 1,348 language models on 5,761 BBH items and compare ways of presenting and scoring answers across BBH, GPQA, MMLU-Pro, and MuSR. We exa...
  </details>

- **2026-11-02** — Yimin Tang, Han Zhang, Shao-Hung Chan et al. — [Late Autumn: LLM Agents Specialize a General Multi-Robot Planner for One Warehouse](http://arxiv.org/abs/2611.02391v1)
  <details><summary>📄 Abstract</summary>
  No algorithm is best on all problems, but a real warehouse is a narrow problem: its layout and processes rarely change. Operators still run one general multi-robot planner at many sites, because experts cannot tune it for each one. In this work, which we call Late Autumn, we explore whether LLM coding agents running autonomous research can specialize a general planner for one site, trading generality for throughput, much as post-training adapts a pretrained LLM to one task. We study six campaign...
  </details>

- **2026-11-01** — Wenbin Wu — [AIDA: An AI Outage Registry with Evidence from On-Chain MEV](http://arxiv.org/abs/2611.01656v1)
  <details><summary>📄 Abstract</summary>
  Generative AI coding tools have lowered the cost of writing trading software, but no systematic dataset records when these services fail. We introduce the AI Incident and Disruption Archive (AIDA), a multi-vendor registry of 5,868 deduplicated outage incidents across 30 providers from 2025 to 2026, with foundation-model incidents verified against primary status-page or postmortem URLs. Pairing AIDA with 5,041,034 verified maximal extractable value (MEV) transactions by 8,516 Ethereum addresses, ...
  </details>

- **2026-11-01** — Zhongjie Wang, Mingyi Liu, Xiang He et al. — [Trustworthy Execution of Industrial Agents](http://arxiv.org/abs/2611.02300v1)
  <details><summary>📄 Abstract</summary>
  Industrial agents increasingly modify persistent engineering objects rather than merely generate answers. Authentication and successful calls cannot establish whether intended changes occurred, evidence supports a conclusion, or historical results remain applicable. We present a framework for trustworthy industrial-agent execution within a single enterprise governance domain. Eight control domains assign responsibilities across authority, planning, composition, tool execution, actual effects, ev...
  </details>

- **2026-11-01** — Ahmet Bahaddin Ersoz, Justin McHenry, Yevgeniya Kovalchuk et al. — [Toward Agentic AI-Ready Workflows in Built Environment Organizations: Knowledge Structures and Interoperability Challenges](http://arxiv.org/abs/2611.02286v1)
  <details><summary>📄 Abstract</summary>
  The rise of agentic artificial intelligence (AI) in the built environment is shifting attention from isolated AI tools toward autonomous systems that reason, plan, and act across project and organizational workflows. The effectiveness of such systems depends not only on large language model capabilities, but also on the readiness of heterogeneous data environments across the Architecture, Engineering, and Construction (AEC) sector. These environments combine structured sources, such as CAD and B...
  </details>

- **2026-11-01** — Wenchang Wang, Yue Song — [When the Text Is Silent: Memory Shortcuts and the Validity of LLM Annotation under Evidence Insufficiency](http://arxiv.org/abs/2611.02273v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to annotate text for social science research, content moderation, and training data. Their broad knowledge of real-world entities raises a concern: when labeling a text, do they rely on its evidence or substitute what they already know? We call this behavior a memory shortcut and examine when it emerges, what amplifies it, and how to mitigate it. Using 995 widely recognized public figures and four matched control names per figure, we construct c...
  </details>

- **2026-11-01** — Matteo Penlington, Lorenzo Fiaschi, Raj Kiriti Velicheti et al. — [Towards a Theory for the Design of Rules in Multi-Agent Systems: the case of Homogeneous Fleets](http://arxiv.org/abs/2611.02260v1)
  <details><summary>📄 Abstract</summary>
  The regulation of systems composed of many interacting decentralised agents is a long-standing problem. This problem has typically been resolved by the imposition of rules. Rules resolve the limitations of sub-optimal agents whilst simultaneously aligning the behaviour of the agents with the demands of society. Traffic laws, for example, let a driver cross a junction without seeing around the corner, and transport protocols such as TCP let applications share a network without knowing of one anot...
  </details>

- **2026-11-01** — Ramiro Pesina, Ashish Madkaikar — [The 3-Tier Integrated Technology Risk Model for Occupational Safety and Health](http://arxiv.org/abs/2611.02257v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the 3-Tier Integrated Technology Risk Model, a progressive framework for Occupational Safety and Health (OSH) management that integrates Job Safety Analysis (JSA), dynamic risk assessment using leading and lagging indicators, and predictive analytics powered by Large Language Models (LLMs). The model provides organizations with a structured pathway to evolve from static, reactive safety practices to a sophisticated, predictive safety paradigm. Each tier builds upon the previo...
  </details>

- **2026-11-01** — Junfei Wu, Qiuyue Wang, Xuhong Huang et al. — [Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models](http://arxiv.org/abs/2611.02026v1)
  <details><summary>📄 Abstract</summary>
  The spatial intelligence of large vision-language models (LVLMs) requires the ability to combine local visual observations into a geometrically consistent representation of the physical world. Many static benchmarks assess isolated spatial judgments, such as relative direction or distance, while interactive embodied evaluations combine perception with exploration, planning, control, and simulator-specific execution. To bridge this gap, we introduce RECONSPATIAL, a benchmark centered on multi-vie...
  </details>

- **2026-11-01** — Ke An, Shizhe Xiang, Yue Liu et al. — [NAS-PO: Native Attention-Strategy Policy Optimization for Vision-Language Models](http://arxiv.org/abs/2611.02008v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has become an effective post-training paradigm for vision-language models (VLMs). Standard RLVR, however, assigns identical outcome-derived credit to all generated tokens regardless of their perceptual relevance. Recent perception-aware methods estimate visual reliance through image perturbation or masking. These indirect proxies require perturbation branches, while corruption sensitivity does not necessarily identify the visual evidence used...
  </details>

- **2026-11-01** — Bahar Radmehr, Jiaxu Zhao, Fatma Betül Güreş et al. — [To Align Long, Plan Short: Simulating Diverse Profile-Aligned Students by Realizing Short-Term Plans in Long-Horizon Learning Environments](http://arxiv.org/abs/2611.02002v1)
  <details><summary>📄 Abstract</summary>
  Simulated students offer a scalable way to test learning platforms and AI tutors before deployment with real students and to augment scarce data for studying learning at scale. Existing LLM-based simulators primarily target short, language-centered interactions. In open-ended learning environments, however, student behavior emerges from patterns across long-horizon interaction trajectories, where turn-level prompting can drift from an assigned behavior profile. We introduce ALPS (Align Long-term...
  </details>

- **2026-11-01** — Zhengshu Zhou, Shaoyu Wang, Lu Tao et al. — [Safety4DM: A Vision-Language Framework for Risk-Aware Dynamic Maps in Vehicle-Road-Cloud Collaborative Driving](http://arxiv.org/abs/2611.01996v1)
  <details><summary>📄 Abstract</summary>
  Dynamic map (DM) is a core information infrastructure for vehicle-road-cloud (VRC) cooperative autonomous driving. It fuses perception data from multiple sources to overcome the inherent line-of-sight and field-of-view limits of single-vehicle perception. However, DM still falls short on driving safety in two ways. First, DM data specifications already define road conditions semantically, but no pipeline yet turns real-world road observations into fine-grained risk entities in the DM. Second, ex...
  </details>

- **2026-11-01** — Wanying Qu, Zhiyuan Fan, Jiyao Liu et al. — [RSI-Env: An Open-Ended Environment for Recursive Self-Improvement of Agents](http://arxiv.org/abs/2611.01736v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) envisions agent systems that autonomously improve their own models and harnesses, with each updated system continuing to improve itself. Existing approaches typically restrict optimization objectives, editable components, or evaluation procedures, limiting open-ended exploration and continuity across generations. We introduce RSI-Env, a persistent environment for coordinated model-harness improvement, supporting autonomous training, harness modification, and rete...
  </details>

- **2026-11-01** — Junjie Li, Zengbin Wang, Gaoxiang Li et al. — [Restoring Semantic Fidelity for Training-Free High-Resolution Image Generation in Diffusion Transformers](http://arxiv.org/abs/2611.01696v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformer (DiT)-based text-to-image models have recently achieved remarkable success in image synthesis. However, when directly applied beyond their training resolution, these models often suffer from severe semantic degradation, where meaningful semantic content disappears. Although existing training-free high-resolution generation methods can mitigate this issue, the inherent semantic degradation at high resolutions remains largely unresolved, leading to degraded fine-grained detai...
  </details>

- **2026-11-01** — Khandokar Md. Rahat Hossain, Souvik Das, Tahsina Hashem et al. — [LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features](http://arxiv.org/abs/2611.01615v1)
  <details><summary>📄 Abstract</summary>
  Accurate house price prediction is essential for real estate buyers, sellers, agents, and financial institutions. Traditional methods rely primarily on structured data, e.g., number of bedrooms, bathrooms, parkings, but they overlook rich contextual information embedded in textual descriptions and property photos. Previous deep learning approaches for house price prediction have fused multimodal data but they fall short to extract structured spatio-temporal and contextual features from texts and...
  </details>

- **2026-11-01** — Lixing Tan, Qing Xia, Yuting Guo et al. — [CUFormer: Modality-Aware CT-Ultrasound Point Cloud Registration for Orthopedic Navigation](http://arxiv.org/abs/2611.01536v1)
  <details><summary>📄 Abstract</summary>
  Registering intraoperative Ultrasound (US) bone-surface point clouds to preoperative Computed Tomography (CT) models can support radiation-free orthopedic navigation. Differences in imaging physics produce distinct surface sampling patterns, complicating cross-modal feature matching. Bone strongly reflects ultrasound and casts an acoustic shadow, so US captures only the probe-facing bone surface and leaves most CT points unmatched. This partial coverage makes correspondences ambiguous on near-sy...
  </details>

- **2026-11-01** — Hedong Zhang, Mengxin Zheng, Qian Lou — [CipherFlow: Compiling AI Programs for Efficient Cryptographically Secure Inference](http://arxiv.org/abs/2611.01450v1)
  <details><summary>📄 Abstract</summary>
  Cryptographically secure inference faces two practical challenges: making secure programming accessible to AI developers and data scientists, and achieving efficient execution across deployment environments. Developers must compose cryptographic primitives correctly, while performance depends on hardware, networks, and evolving ciphertext states. We present CipherFlow, a compiler framework that takes a high-level AI computation graph, available cryptographic primitives, and a target hardware and...
  </details>

- **2026-11-01** — Yuxiang Wei, Lijing Zhu, Qizhen Lan et al. — [CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](http://arxiv.org/abs/2611.01449v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can autonomously run neuroimaging analyses from research questions to reported findings. Existing agentic systems use tools to check that code runs and reported values match its output, but rely on LLM judgment to decide which results warrant scientific reporting. We show that LLM judges endorse site-confounded findings even when the confound is presented as evidence. We present \textbf{CONFIRM}, a framework that separates running an analysis from deciding which...
  </details>

- **2026-11-01** — Huanzhi Mao, Chengkun Cao, Shuo Yuan et al. — [I-PTC: Interactive Programmatic Tool Calling for Stateful Tool-Augmented Agents](http://arxiv.org/abs/2611.01446v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly capable of writing and executing code, suggesting a natural paradigm for tool-augmented agents: expressing tool use as programs rather than isolated calls. Programmatic tool calling (PTC) captures this idea through loops, batching, abstraction, and structured computation, but existing PTC approaches are largely stateless, limiting their ability to reuse intermediate results and adapt over time. This is problematic for real-world tasks, where tool environmen...
  </details>

- **2026-11-01** — Ran Li, Shimin Di, Zeyu Ren et al. — [Latent Harness: Compiling Agent Behaviors into Post-Block Activation Shifts](http://arxiv.org/abs/2611.01415v1)
  <details><summary>📄 Abstract</summary>
  Harness engineering and self-evolving agents improve language-model agents quickly, yet their gains live outside the model. The harness is re-sent and re-paid on every call, and the standard route to internalization is a weight update that is costly to iterate and fixed once merged. We propose compiling the harness instead. Latent Harness distills an external condition into a rank-8 activation shift. The shift is applied at the output of every decoder block of a frozen backbone, at 0.03-0.05% of...
  </details>

- **2026-11-01** — Hirofumi Morise — [Information-Theoretic Design of Sparse Autoencoder-Based Steering](http://arxiv.org/abs/2611.01378v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoder (SAE)-based activation steering is a lightweight approach for modifying the behavior of large language models (LLMs) by adding small vectors to hidden states during inference. However, designing effective steering interventions remains challenging. In this work, we develop an information-theoretic framework for analyzing SAE activations through empirical feature-firing distributions. The central object of the framework is the Jensen--Shannon divergence (JSD) between such firin...
  </details>

- **2026-11-01** — Marek Šuppa, Jaroslav Kopčan — [XDecideBench: Evaluating Typed Decision Models and Confidence Policies Across Languages](http://arxiv.org/abs/2611.01370v1)
  <details><summary>📄 Abstract</summary>
  Applications use Typed Decision Models to route and moderate text in many languages, and they often act only on decisions above a confidence threshold. We introduce XDecideBench, a benchmark of nine suites in 122 languages with 88,425 texts and 153,875 typed questions. All suites share one scoring contract, and we report aligned, locally labelled and native items separately. Model rankings change from suite to suite. The model that is best in English, chosen in hindsight, loses significantly in ...
  </details>

- **2026-11-01** — Zhouli Yu — [OCBI: Order-Sensitive Cross-Branch Interaction for Image Manipulation Localization](http://arxiv.org/abs/2611.01783v1)
  <details><summary>📄 Abstract</summary>
  Image manipulation localization combines semantic structure with forensic traces to identify modified pixels. Within-branch spatial mixing and RGB-guided cross-branch mixing can produce different messages when composed in opposite orders. We propose OCBI, an extension of Co-Transformers that models the discrepancy between these two composition orders for localization. A local cross-branch fusion module uses the commutator of RGB-guided cross-attention and forensic self-attention to add a learnab...
  </details>

- **2026-11-01** — Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang et al. — [Democratizing Robot-Use Agents: A Unified Harness with Open Models](http://arxiv.org/abs/2611.01560v1)
  <details><summary>📄 Abstract</summary>
  Robot-use Agents (RUAs) have shown promising zero-shot manipulation capabilities, but reliance on frontier, proprietary models limits research into further training. To democratize RUA research, we introduce uni-robot-agent, a unified harness for competitive open-weight robot use that supports further training. Without privileged inputs, an out-of-the-box Qwen3.8-Flash-Next achieves a RoboDojo Score of 31.39, surpassing the published GPT-6 Astra-RoboProbe result of 28.97 and many VLA/WAM baselin...
  </details>

- **2026-11-01** — Emily Adlam — [The Reference System Loophole](http://arxiv.org/abs/2611.02283v1)
  <details><summary>📄 Abstract</summary>
  I argue that the Extended Wigner's Friend theorems have a `loophole' that has previously not been appreciated, coming from the fact that we typically need a reference system to give meaning to a measurement outcome. I show how this loophole can be used in the context of the Local Friendliness theorem to preserve the predictions of quantum mechanics without denying Local Friendliness, and I respond to some objections. I explain how the loophole arises naturally from consideration of relevant symm...
  </details>

- **2026-11-01** — Xuanxi Zhang, Kevin S. Cheng, Weizhou Wang et al. — [Restrained Diffusion Bridges: Targeted Denoiser Training and Refinement](http://arxiv.org/abs/2611.02170v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models are often inaccurate in critical, data-sparse regions of the target distribution. Sampling from restrained distributions, biased distributions used in classical enhanced sampling to concentrate data near chosen configurations, can control where training data are collected but biases the learned distribution. We establish that this bias cancels exactly when forward noising from restrained data is conditioned on the restrained configuration at an appropriately chosen intermediate ...
  </details>

- **2026-11-01** — Maximos Skandalis — [FOLLIE: Automated Reasoning over the First Dataset of Sentences with their First-Order Logical Representation for French](http://arxiv.org/abs/2611.02129v1)
  <details><summary>📄 Abstract</summary>
  FOLLIE (for First-Order Logic for Language Inference and Entailment for French) connects French sentences, compositional first-order representations and automated natural language inference (NLI). The first French NLI-ready, NL-to-FOL resource, it contains 19,983 inference records and 36,987 non-empty sentence-slot--formula mappings from six heterogeneous NLI sources, retaining French lexical material and source problem structure. Its silver annotations are produced by a neural--symbolic pipelin...
  </details>

- **2026-11-01** — Sepideh Arab Mohammadi, Amir Kargaran, Ali Hosseiny et al. — [When Does Triadic Balance Reduce to Pairwise Order?](http://arxiv.org/abs/2611.02117v1)
  <details><summary>📄 Abstract</summary>
  Structural-balance interactions are naturally defined on triads, but when pair affinities are themselves generated by continuous node attributes, it is not clear whether the resulting interaction remains genuinely higher order. Here we address this question for agents represented by unit vectors in an attribute space, with pair affinity given by their scalar product and a Heider product assigned to each triangle. For planar attributes, we show that the triadic interaction reduces exactly, at fin...
  </details>

- **2026-11-01** — Mingyu Cao, Yaokai Jin, Shiwei Liu et al. — [Bernoulli On-Policy Distillation: Don't Ignore High-Confidence Student Tokens](http://arxiv.org/abs/2611.02093v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student language model on its own trajectories using token-level supervision from a stronger teacher. We show that standard sampled reverse-KL OPD systematically suppresses updates to high-confidence tokens, such that their weak gradient contribution does not necessarily imply weak or uninformative teacher supervision. We introduce Bernoulli On-Policy Distillation (Bernoulli OPD), which directly matches the teacher and student probabilities for that token. T...
  </details>

- **2026-11-01** — Rodrigo Diaz, Pablo Tablas De Paula, David Marttila et al. — [Count-Density Networks for Modal Plate Parameter Estimation](http://arxiv.org/abs/2611.02083v1)
  <details><summary>📄 Abstract</summary>
  We describe two submissions to Task B of the 1st DAFx Parameter Estimation Challenge, which estimates an unknown number of modal frequency, decay, and gain triples from a synthetic plate-reverb impulse response. The first method combines pooled spectral features with time-domain and absolute-scale conditioning in a real-valued convolutional count-density network, while the second uses a complex-valued Transformer count-density network. Both methods jointly infer the modal count and per-mode attr...
  </details>

- **2026-11-01** — Hamidreza Alikhani, Nazmul Takbir, Matin Khajavi et al. — [Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling](http://arxiv.org/abs/2611.02082v1)
  <details><summary>📄 Abstract</summary>
  LLM-based applications often employ agentic workflows and retrieval-augmented generation (RAG), which build long prompts from shared context. When prefixes are shared across requests, serving engines reuse the key-value (KV) cache to skip parts of the prefill computation. Reuse is typically graded: the uncached work of requests in a queue can differ by up to 100x. In this setting, the order of scheduling determines the time-to-first-token (TTFT) for the queued requests. KV reuse-first scheduling...
  </details>

- **2026-11-01** — Zhuoyuan Li, Xidong Wu, Hanyu Cui et al. — [ECGJev: Question-Conditioned Option Scoring for 12-Lead ECG Interpretation](http://arxiv.org/abs/2611.02041v1)
  <details><summary>📄 Abstract</summary>
  Clinical interpretation of a 12-lead electrocardiogram (ECG) often requires answering targeted diagnostic questions with clear, quantifiable decisions. We introduce ECGJev, the first ECG framework built on a decision decoder, a pretrained language model trained to return a probability for every listed option. A question-conditioned bridge compresses frozen waveform and spectrogram features into 16 ECG tokens, and a two-stage procedure adapts the bridge and low-rank adapters on the decoder's nati...
  </details>

- **2026-11-01** — Bahar Radmehr, Lan Tran, Ekaterina Shved et al. — [ClickSight: An LLM Framework for Interpreting Student Clickstreams Through Learning Strategies](http://arxiv.org/abs/2611.02021v1)
  <details><summary>📄 Abstract</summary>
  Digital learning environments produce rich clickstream data that can reveal how students approach learning tasks, yet interpreting these fine-grained traces often requires substantial expert effort. We introduce ClickSight, a framework for interpreting student clickstreams through learning strategies defined in the literature. Given a student clickstream and a predefined set of learning strategies, ClickSight uses a staged LLM-based pipeline to identify strategy-relevant evidence, assess adheren...
  </details>

- **2026-11-01** — Weijian Fan, Chichen Lin, Xiao Han et al. — [No Note Is an Island: Probing LLMs' Understanding of Crowdsourced Fact-Checking Environments](http://arxiv.org/abs/2611.01935v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly assist crowdsourced fact-checking, yet evaluations focus on individual annotations. A correction's reach and reception depend on visibility, audience responses, and platform policies. We introduce correction context understanding: assessing corrective content, interpreting audience responses, and reasoning about platform dynamics within a shared environment. We build NoteHabitat from 36 months of Weibo Annotations data, linking 102,994 posts (42,853 anno...
  </details>

- **2026-11-01** — Zhongxiang Sun, Chenghao Yang, Haojie Ding et al. — [TriPhysBench: Evaluating Physical Intelligence for Embodied Agents](http://arxiv.org/abs/2611.01934v1)
  <details><summary>📄 Abstract</summary>
  Embodied agents need physical intelligence to understand their surroundings through physical perception, physical knowledge retrieval, and physical reasoning. These capabilities must work together to interpret events and make quantitative judgments. Existing benchmarks advance physical understanding and general-purpose tool use, yet the coordination of these capabilities in physical scenarios remains insufficiently characterized. Inspired by Popper's Three Worlds, we introduce TriPhysBench, a be...
  </details>

- **2026-11-01** — Dario Labrador Alonso, Alaa Alahmadi — [Vision-language classification of Torsades de Pointes risk from pseudo-coloured ECG images: do T-wave morphology and colour context help or hinder?](http://arxiv.org/abs/2611.01921v1)
  <details><summary>📄 Abstract</summary>
  Contextual prompting is widely presented as a cheap route to better performance from vision models, but the evidence comes largely from benchmarks in which an attribute named in a prompt is also present in the image, confounding the two channels. We investigate the significance of context for a semantically complex biomedical signal classification task using a domain-adapted vision-language model, BiomedCLIP. Building on our previous work that renders electrocardiogram (ECG) signals as colour-en...
  </details>

- **2026-11-01** — Wenqi Zeng, Chen Feng, YuAng Chen — [Who Asks, Who Answers: Linear Attention Builds the Query in Hybrid Language Models](http://arxiv.org/abs/2611.01909v1)
  <details><summary>📄 Abstract</summary>
  Hybrid language models interleave linear-attention layers with a small number of softmax-attention layers. Prior work largely attributes in-context retrieval to softmax attention, treating linear attention primarily as a mechanism for compressing past context. We revisit this division of labor and show that linear attention plays a direct role in retrieval by constructing the query used by softmax attention. Studying Qwen3.5 (Gated DeltaNet) and Granite4.0 (Mamba-2), we identify an Encode--Addre...
  </details>

- **2026-11-01** — Sergey V. Popov — [Same Text, Different Filename: Are LLM Judges Biased?](http://arxiv.org/abs/2611.01829v1)
  <details><summary>📄 Abstract</summary>
  Yes. In 2026, leading economic journals started using Refine.ink in the technical quality assessment of submissions before publication. I study whether renaming a file changes the perception of the document's quality by LLM judges. I find that three frontier LLMs score the same document differently if you change the document's filename. A person-related label scores higher than no label; there is no consistent preference of own- or rival-based label, nor a penalty for an Asian name, but there is...
  </details>

- **2026-11-01** — Kaixiang Shu — [Shared relations, specific choices: conditional sensitivity and competing pathways in language models](http://arxiv.org/abs/2611.01809v1)
  <details><summary>📄 Abstract</summary>
  How does a relational representation shared across queries drive a query-specific choice? Controlled entity-binding experiments with GPT-2 Small, Qwen2.5-1.5B and Llama-3.2-1B reveal a low-dimensional relational background that is predominantly shared across query roles and transfers to new names. Same-domain interactions persist when another attribute domain is queried. After removing this component, restoring independently trained relation directions brings output contrasts closer to their ori...
  </details>

- **2026-11-01** — Boyu Cao, Wenshuo Wang — [A Bounded Evaluation Protocol for Representational Systematicity](http://arxiv.org/abs/2611.01755v1)
  <details><summary>📄 Abstract</summary>
  Multiple studies have shown that neural networks can be behaviorally systematic, producing correct outputs for novel combinations of familiar parts. Whether they are also representationally systematic, that is, whether they represent these parts and their roles and use them to produce the outputs, remains hard to test, because each kind of evidence can mislead on its own: correct outputs can come from shortcuts, a decodable signal need not be used, an intervention can act through unintended path...
  </details>

- **2026-11-01** — Yupeng Tong, Lianze Shan, Jitao Zhao et al. — [ReCoG: Relative Node Contexts for Multi-Domain Graph Pre-training](http://arxiv.org/abs/2611.01753v1)
  <details><summary>📄 Abstract</summary>
  The success of foundation models in language and vision has motivated Graph Foundation Models (GFMs), which learn transferable knowledge through multi-domain graph pre-training. Existing methods advance GFMs through feature unification and structural learning, and in doing so they rely on the raw graph structure to organize node contexts. However, we observe that removing a large proportion of edges from source graphs during pre-training improves cross-domain transfer accuracy across four repres...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 710 |
| prompt-injection | 660 |
| memory-poisoning | 57 |
| tool-use-attack | 171 |
| backdoor | 548 |
| adversarial-attack | 663 |
| privacy-leakage | 4525 |
| steganography | 90 |
| misuse | 1285 |
| red-teaming | 146 |
| vulnerability | 3876 |
| defense | 3766 |
| alignment | 3536 |
| robustness | 3847 |
| watermark | 704 |
| unlearning | 119 |
| agent-safety | 66 |
| benchmark | 73 |
| survey | 438 |
| other | 10471 |

---

📚 **全部 35751 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-04 13:39:39*