<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-35947-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-05 23:10 ｜ **论文总数 / Total Papers**: 35947（近 30 天 / Recent 30 days: 4543）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 35947 篇论文（含摘要、分类筛选、搜索）/ View all 35947 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 713
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 663
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 57
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 172
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 548
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 664
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4538
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 90
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1289
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 146
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3896
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3791
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3556
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3863
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 712
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 119
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 67
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 73
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 442
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10548

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4543 篇，完整 35947 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4543 papers from the last 30 days (with date, authors & abstract). For the full list of 35947 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 10 papers

- **2026-11-04** — Hamid Dashtbani, Alexandra Dmitrienko — [Addition by Subtraction: Toward Mitigating Fragile Safety Alignment in Large Language Models](http://arxiv.org/abs/2611.06553v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) undergo safety alignment to prevent harmful generations, yet they remain vulnerable to jailbreak attacks. Recent work reveals a deeper structural weakness: safety alignment can be highly sparse, such that pruning a small number of safety-critical neurons or ablating a single refusal direction can substantially undermine aligned behavior. In this work, we take the first steps toward strengthening safety alignment such that it is less dependent on sparse model componen...
  </details>

- **2026-11-04** — Erfan Baghaei Potraghloo, Saeid Shokoufa, Seyedarmin Azizi et al. — [SafeStart: Mitigating the Overlooked Safety Cost of Active Expert Reduction in MoE LLM Serving](http://arxiv.org/abs/2611.06147v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) language models send each token through a few of many expert subnetworks. Serving methods make these models faster by running even fewer experts per token, and they are validated on accuracy benchmarks. We show that these methods can weaken the model's refusal of harmful requests, and we introduce SafeStart, which largely restores refusal while keeping most of the speedup. In vLLM on one RTX A6000, keeping about two thirds of the selected experts speeds up offline decodi...
  </details>

- **2026-11-03** — Chuancheng Shi, Shangze Li, Wenhua Wu et al. — [TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport](http://arxiv.org/abs/2611.04878v2)
  <details><summary>📄 Abstract</summary>
  Despite their remarkable capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current safety intervention methods primarily rely on the \textit{locality hypothesis}, rigidly suppressing isolated neurons or features. However, harmful semantics manifest as distributed, cross-layer circuits, rendering localized ablations both brittle against complex jailbreaks and detrimental to general utility. To bridge this gap, we propose TraceRouter++, a routing-level sa...
  </details>

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
*提示注入攻击 / Prompt Injection Attacks* — 13 papers

- **2026-11-04** — Guoqin Xiong, Shengtao Wen, Xiang Chen et al. — [SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents](http://arxiv.org/abs/2611.06682v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave action semantics, state dependencies, and evidence relations implicit, limiting generalization across heterogeneous tools and complicating safe updates. We present \ours{}, a dynamic ontology-guided governance framework. \ours{} grounds hete...
  </details>

- **2026-11-04** — Annabella Chow, Jinhao Zhu, Sylvie Venuto et al. — [Securing Web Agents with the Compile-Then-Execute Paradigm](http://arxiv.org/abs/2611.06039v1)
  <details><summary>📄 Abstract</summary>
  Web agents commonly follow the ReAct paradigm, selecting each action from runtime observations that inherently mix trusted and untrusted content. This design makes their control flow vulnerable to prompt injections embedded in webpages. We introduce Baya, a compile-then-execute web agent designed to prevent prompt-injection-driven control-flow hijacking by design. Before accessing the live website, Baya compiles the user's request into an executable Python program that calls a Trusted Website AP...
  </details>

- **2026-11-03** — Yutao Wu, Xiao Liu, Ming Wen et al. — [ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud](http://arxiv.org/abs/2611.04879v2)
  <details><summary>📄 Abstract</summary>
  Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter online fraud designed to deceive humans, including fraudulent online stores, fake investment platforms, and advance-fee schemes. How web agents respond to such fraud during task execution remains underexplored, in part becau...
  </details>

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


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-11-02** — Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel et al. — [IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning](http://arxiv.org/abs/2611.03431v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies that exceed trusted authorization requirements. We present IAMRAGBENCH, a 60-case benchmark spanning scope, conditions, explicit denies, trust, permissions boundaries, and role delegation. It combines deterministic authorization-envelope sc...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-11-03** — Achuth Chandrasekhar, Jesse Barkley, Peter Pak et al. — [Mechanical Engineering Skills: An Open Library of Agent Skills for Design, Analysis and Manufacturing](http://arxiv.org/abs/2611.05758v1)
  <details><summary>📄 Abstract</summary>
  Mechanical engineers use specialized tools for CAD, simulation, manufacturing and research, each with a distinct interface and learning curve. We present Mechanical Engineering Skills, an open library of 33 agent skills that makes these capabilities accessible through a single text or voice conversation. Each skill combines operating instructions, executable tools and verification procedures. A language model interprets the request, selects and coordinates skills, while deterministic tools perfo...
  </details>

- **2026-11-03** — Jinjun Huang, Jialun Cao, Junxiao Han et al. — [How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub](http://arxiv.org/abs/2611.04456v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based agents increasingly rely on external skills to reuse task-specific knowledge without retraining the model. As skills become common for extending agent capabilities, understanding creation and evolution is critical for reliable agent systems. However, existing studies mainly examine agent skills from a static perspective, leaving their evolution in real-world repositories largely unexplored. This limits our understanding of the patterns and motivations behind skill chan...
  </details>

- **2026-11-02** — Kuiyi Gao, Xue Liu, Bowei He — [RuntimeTickets: Source-Grounded Security Obligations for Agent Skills](http://arxiv.org/abs/2611.03772v1)
  <details><summary>📄 Abstract</summary>
  Third-party Agent Skills extend what an autonomous agent can do, but a malicious Skill can hide data exposure or output manipulation inside a legitimate workflow. Neither reading a Skill's description nor granting it tool permissions tells whether its execution meets the user's security requirements. We introduce RuntimeTickets, a protocol that enforces and audits these requirements while a Skill runs. From released malicious-Skill datasets we derive a risk model and build adversarial-benign Ski...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 1 papers

- **2026-11-02** — Farooq Shaikh, Biagio Montaruli — [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](http://arxiv.org/abs/2611.03555v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions without confirming real execution. We present the first cross-framework measurement of MCP tool poisoning with real tool execution. A 25-class root-cause taxonomy unifies prior classi...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-11-03** — Drake Benjamin Brown, Khushbu Pahwa, Yubin Ge et al. — [Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge](http://arxiv.org/abs/2611.05662v1)
  <details><summary>📄 Abstract</summary>
  Evaluating open-ended agent tasks increasingly falls to an Agent-as-a-Judge: an evaluator handed tools and the agent's full trajectory so it can verify a result against the environment. The premise is that a judge that gathers its own evidence should be grounded by it. We show that this grounding does not immunize the judge against confirmation bias: a single false pre-screening note, attributed to an authority and carrying no evidential bearing on the correct verdict, overturns up to 40% of a t...
  </details>

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

- **2026-11-04** — Calister Nnona — [CoRTeC: A Differentially Private Release for Synthetic Tabular Data, Decodable by Any Generator](http://arxiv.org/abs/2611.06342v1)
  <details><summary>📄 Abstract</summary>
  The records that could train the most useful models, such as a hospital's patient files, are often the ones an institution cannot share. We propose CoRTeC, a method that releases synthetic versions of such records under differential privacy. Differential privacy places a proven limit on what the synthetic data can reveal about any person, and in particular on membership inference. CoRTeC spends the privacy budget once, on a small file of noisy counts designed for training a classifier. For each ...
  </details>

- **2026-11-04** — Zheao Li, Jiancheng An, Chau Yuen — [SIM-Enabled Wave-Domain Processing in MIMO-OFDM Receivers: Architecture, Modeling, and Validation](http://arxiv.org/abs/2611.05999v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a wave-domain linear receiver for wideband MIMO-OFDM, where the main high-dimensional linear processing conventionally performed after sampling is physically shifted to propagation through stacked intelligent metasurfaces (SIMs). The proposed receiver transforms receive-port waveforms into OFDM-domain symbols through three cascaded SIM-enabled functional sections. The first section, SIM_1, performs channel-memory processing and channel shortening in an energy-concentration se...
  </details>

- **2026-11-04** — Jie Fu, Xiangpeng Deng, Yuan Hong et al. — [Timing is Everything: Inferring Temporal Membership in Continually Updated Models](http://arxiv.org/abs/2611.05781v1)
  <details><summary>📄 Abstract</summary>
  Continual model updating has become a common practice in the deployment of machine learning systems. However, the dynamic training behaviors give rise to new risks not sufficiently addressed by existing studies. In this paper, we present the first systematic study of temporal privacy risk in continually updated deep learning models. We formalize the notion of temporal membership in continually updated models. We then define the temporal membership inference attack, which seeks to infer whether a...
  </details>

- **2026-11-04** — Shahan Ali Memon, Anna-Maria Gueorguieva, Anukriti Kumar et al. — [U.S. State Guidance on AI in K-12 Education: A Comparative Content and Citation Analysis](http://arxiv.org/abs/2611.06762v1)
  <details><summary>📄 Abstract</summary>
  In the years following the public release of ChatGPT in late 2022, more than half of U.S. states have published formal guidelines around AI usage in K-12 education, creating a record of largely independent state education departments responding to a shared technological disruption. In this work, we analyze publicly available AI usage guidance documents from 35 states in the U.S. and Puerto Rico. We compare the guidance in these documents across various dimensions, including pedagogy and instruct...
  </details>

- **2026-11-04** — Xi Chen, Julien Cumin, Fano Ramparany et al. — [Multi-Resident Data Association in Smart Homes via MDP Modeling and Behavior Cloning](http://arxiv.org/abs/2611.06296v1)
  <details><summary>📄 Abstract</summary>
  Ambient sensors offer a privacy-preserving solution for activity recognition in smart homes, yet they face a critical challenge in multi-resident environments known as Data Association, which aims to identify the resident triggering a specific anonymous sensor event. Existing approaches fundamentally fail to maintain global consistency by often yielding conflicting associations for silent residents. Additionally, these methods frequently suffer from severe trajectory fragmentation caused by the ...
  </details>

- **2026-11-04** — Tianqi Zong, Baosheng Li, Nuocheng Yang et al. — [CARE-FL: Federated Fine-Tuning of Multimodal LLMs in Resource-Constrained Edge Networks](http://arxiv.org/abs/2611.06169v1)
  <details><summary>📄 Abstract</summary>
  Domain-specific adaptation of Multimodal Large Language Models (MLLMs) in privacy-sensitive edge environments requires federated fine-tuning, yet client selection remains challenging due to heterogeneous multimodal data and modality availability, dynamic system conditions, and evolving client utility during training. We propose Constraint-Aware Reinforcement Learning for Efficient Federated Fine-Tuning (CARE-FL), a constrained online client-selection framework for federated MLLM Low-Rank Adaptat...
  </details>

- **2026-11-04** — Elise L. Han, Tatsunori Hashimoto — [Reconciling Privacy with Provenance for Language Model Watermarks](http://arxiv.org/abs/2611.06100v1)
  <details><summary>📄 Abstract</summary>
  Watermarking has great potential for regulating the use of language models (LMs), but its deployment has been marred by controversy, as many users argue that fine-grained tracking of LM usage violates their privacy. This tension reduces the effectiveness of watermarks, as users engage in evasion strategies such as paraphrasing that can remove much of the watermark signal. We show that provenance and privacy can be reconciled if we shift the goal of watermark design from tracking individuals to e...
  </details>

- **2026-11-04** — Hengyou Kong, Xiaoli Xu, Zilong Liu et al. — [AFDMA with Heterogeneous Post-Chirp Parameters: Supporting User-Specific Waveform Configurations](http://arxiv.org/abs/2611.06063v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates a downlink affine frequency division multiple access (AFDMA) framework supporting flexible user-specific waveform configurations with heterogeneous post-chirp parameters. The proposed framework is in sharp contrast to conventional disjoint chirp-subcarrier allocation, which may destroy inter-user orthogonality when users employ heterogeneous post-chirp parameters. Such a loss of orthogonality manifests as cross-basis leakage onto user-allocated chirp subcarriers, which we...
  </details>

- **2026-11-04** — Bin Wen, Dai-Qiao Zhang, Tien-Ping Tan — [Selective, Risk-Controlled Emotion Forecasting in Conversation: From a Persistence Barrier to Departure Detection with Conformal Guarantees](http://arxiv.org/abs/2611.05896v1)
  <details><summary>📄 Abstract</summary>
  Forecasting emotion in conversation is increasingly framed as predicting the next emotional state's value. We show this targets a hard quantity in a state-observed testbed and propose a learnable, deployable reformulation instead. On valence-arousal-dominance trajectories from a dyadic corpus, repeating a speaker's own previous state sets a persistence baseline that no frozen-encoder correction meaningfully improves upon and a state-space filter exceeds; the floor requires the historical state t...
  </details>

- **2026-11-04** — Zhanhong Jiang, Qisai Liu, Soumik Sarkar — [Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential](http://arxiv.org/abs/2611.05841v1)
  <details><summary>📄 Abstract</summary>
  This vision paper argues that distributed learning, including federated and decentralized, should become a first-class paradigm in LLM post-training, not merely a privacy add-on. Current methods like RLHF and DPO rest on an invisible assumption: preference data should be centralized. We contend this assumption is scientifically unjustified, practically unsustainable, and ethically problematic. As LLMs deploy into healthcare, law, finance, and multilingual communities, preference data originates ...
  </details>

- **2026-11-03** — S M Rayeed, Qian Ma, Charles V. Stewart et al. — [How Finely Can Vision-Language Models See Biology? Bio-VQA: A Benchmark for Taxonomic, Morphological, Spatial and Individual Reasoning](http://arxiv.org/abs/2611.05559v1)
  <details><summary>📄 Abstract</summary>
  In biodiversity monitoring, a single image raises several questions: which taxon, how many, which trait, and whether the individual has been seen before. Vision-language models (VLMs) could answer all of these from the image, but their ability is largely untested in biology, as existing benchmarks focus mostly on species identification within a few taxonomic groups. We present Bio-VQA, the largest biological visual question answering (VQA) benchmark and the only one to span four aspects of biolo...
  </details>

- **2026-11-03** — Mingxuan Li, Huanzhi Mao, Ruitao Zheng et al. — [SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories](http://arxiv.org/abs/2611.05512v1)
  <details><summary>📄 Abstract</summary>
  AI Agents are becoming digital coworkers that can browse the web, write code, run experiments, and assist humans over extended horizons. Yet existing benchmarks fall short of real knowledge work: many rely on synthetic data or isolated tasks, missing the complex, multi-party dynamics of collaborative projects, where critical information is scattered across conversations, code, and evolving decisions. Even simple workplace questions may require locating relevant channels and direct messages, reco...
  </details>

- **2026-11-03** — Zhengtao Gao, Francesco Bombassei De Bona, Leonardo Alchieri et al. — [Self-Supervised Pretraining for Label-Efficient Facial Expression Recognition using Smart Glasses](http://arxiv.org/abs/2611.05711v1)
  <details><summary>📄 Abstract</summary>
  Facial Expression Recognition (FER) on optomyographic (OMG) smart glasses such as OCOsense enables privacy-preserving, camera-free affect sensing for health and well-being. Most FER systems are fully supervised, i.e., they rely either on hand-crafted expert features with classical machine learning, or on end-to-end deep models trained from labelled data. Both depend on large quantities of labelled expressions, which are costly to collect and limit deployment in real-world, personalized settings....
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 12 papers

- **2026-11-04** — Yifan Wang, Junyu Lu, Shun Zhang et al. — [Beyond Risk Cues: A Mechanism-Level Benchmark and Verifiable Debate for Scam Video Detection on the Web](http://arxiv.org/abs/2611.06110v1)
  <details><summary>📄 Abstract</summary>
  Online scam videos pose significant threats to individuals and society. Existing studies primarily focus on binary classification, offering limited insights into how scams work and the reasoning behind detection decisions. Moreover, they often overlook the challenge of distinguishing scam videos from superficially similar non-scam content, such as advertisements, and the robustness of detection models against misleading arguments. These limitations hinder reliable scam video detection. To addres...
  </details>

- **2026-11-04** — Tianwei Zhang, Ivy Njoki Nyagwencha, Zahraa Dirani et al. — [ALTO: African and Levantine Tech-Facilitated Gender-Based Violence Corpus](http://arxiv.org/abs/2611.06706v1)
  <details><summary>📄 Abstract</summary>
  Tech-facilitated gender based violence (TFGBV) is a pervasive online harm affecting women and gender minority groups through its many direct and covert forms. Current models and annotated datasets for gendered harm detection are dominated by data from, and models trained in, Global North languages. In collaboration with civil society organizations (CSOs) from Jordan, Francophone West Africa, and Kenya, we developed a community-led approach to crowdsource culturally and linguistically relevant in...
  </details>

- **2026-11-03** — Duc Anh Vu, Thong Nguyen, Hoang Pham et al. — [Objective-Conditioned Active Preference Learning for Multi-Objective Alignment](http://arxiv.org/abs/2611.05506v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) with several objectives, such as helpfulness, harmlessness, and honesty, typically relies on preference judgment for each objective, growing the annotation cost linearly with the number of objectives. Active preference learning can reduce this cost by selecting the comparisons whose labels are expected to change the policy most. Existing remedies either lack an objective-aware query selection mechanism for the multi-objective setting or regard conflicting pr...
  </details>

- **2026-11-03** — Mehdi Shajari — [Assurance-Conditioned Continuous Authorization for Autonomous AI Agents](http://arxiv.org/abs/2611.05632v1)
  <details><summary>📄 Abstract</summary>
  Autonomous software agents can act through tools, delegate work, and change their models or execution environments while earlier authorizations remain in flight. We present Assurance-Conditioned Continuous Authorization (ACCA), an approach designed to be harness-independent, for maintaining operational authority according to currently justified assurance. It distinguishes evidence validity from contextual applicability, derives assurance claims from eligible evidence, and resolves a multidimensi...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-11-03** — Li Zheng, Simin Chen — [CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](http://arxiv.org/abs/2611.04356v1)
  <details><summary>📄 Abstract</summary>
  Finite element method (FEM) solvers are foundational to scientific and engineering simulation, yet their susceptibility to \emph{efficiency attacks} remains largely unexplored. An adversary can craft syntactically valid and runnable FEM programs that complete successfully while forcing excessive computational work, enabling computational denial-of-service (DoS) attacks. Finding such inputs is challenging because FEM programs occupy a vast, structured space constrained by numerical, geometric, an...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 52 papers

- **2026-11-04** — Weichen Fan, Haiwen Diao, Penghao Wu et al. — [From Pixels to Actions - Towards Native Vision-Language-Action Policies](http://arxiv.org/abs/2611.06918v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a str...
  </details>

- **2026-11-04** — Chaomeng Lu, Pooya Rostami Mazrae, Bert Lagaisse — [PatchCon: Patch-aware Weighted Supervised Contrastive Learning for Vulnerability Detection](http://arxiv.org/abs/2611.06583v1)
  <details><summary>📄 Abstract</summary>
  Automated vulnerability detection is critical for securing modern software systems, yet existing learning-based approaches often treat functions as independent samples and underuse the supervision provided by vulnerability-fixing patches. In this paper, we propose PatchCon, a CodeBERT-based patch-aware contrastive learning model for function-level vulnerability detection. PatchCon jointly optimizes vulnerability classification and supervised contrastive learning, and treats vulnerable-patched fu...
  </details>

- **2026-11-04** — Jianhong Ma, Wenhao Li, Xixing Li et al. — [Towards Early Warning of Real-World Vulnerabilities: An Evidence-Aware Decoupled Method for CVSS Vector Prediction Based on Unstructured Disclosures](http://arxiv.org/abs/2611.06477v1)
  <details><summary>📄 Abstract</summary>
  Early assessment of Common Vulnerability Scoring System (CVSS) vectors from Open Source Intelligence (OSINT) can reduce the delay between initial public disclosure and official National Vulnerability Database (NVD) scoring. Existing predictors, trained mainly on standardized late-stage descriptions, degrade on noisy and incomplete pre-NVD reports. We introduce PARSE, a vulnerability-disclosure lifecycle model, and VPre, an early assessment framework built on two-level Evidence-Aware Decoupling. ...
  </details>

- **2026-11-04** — Zhuangyan Hu, Zhuoxuan Liang, Wei Li et al. — [Graph Foundation Models Can Become Effective Multivariate Time Series Anomaly Detectors](http://arxiv.org/abs/2611.06441v1)
  <details><summary>📄 Abstract</summary>
  Multivariate time series anomaly detection (MTSAD) relies on modeling both temporal dynamics and inter-sensor dependencies to identify complex system faults. Although graph-based detectors explicitly model sensor topologies, they train task-specific networks from scratch on limited target-domain data, remaining vulnerable to spurious correlations and unable to reuse transferable priors. While pretrained Graph Foundation Models (GFMs) offer transferable topological priors and anomaly discriminabi...
  </details>

- **2026-11-04** — Adrian Hayler, Shashank Reddy Chirra, Andrei Lupu et al. — [Zero-Shot Coordination among LLM Agents](http://arxiv.org/abs/2611.06409v1)
  <details><summary>📄 Abstract</summary>
  We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. Existing work on LLM coordination often relies on specialised scaffolding that independently developed agents are unlikely to share in practice. Moreover, evaluations on complex environments (e.g., Hanabi) make it difficult to pinpo...
  </details>

- **2026-11-04** — Ehud Shapiro — [Corralling AI Risks with Grassroots Contracts](http://arxiv.org/abs/2611.06374v1)
  <details><summary>📄 Abstract</summary>
  AI's inflection point is a fountain of alarming risks. Digital platforms in particular are vulnerable to three major AI risks, as those in control of global platforms cede control to AI, of the algorithms, of membership and of content: (1) AI control of global platforms, social and economic, used by the majority of humanity, resulting in the majority of humanity becoming vulnerable to AI control. (2) Unaccountable AI agents operating anonymously on social and economic digital platforms, side-by-...
  </details>

- **2026-11-04** — Norbert Sándor Szolnoki, Gábor Antal — [Reassessing Dataset Quality and Fine-Tuning Practices for Vulnerability Detection on PrimeVul dataset](http://arxiv.org/abs/2611.06373v1)
  <details><summary>📄 Abstract</summary>
  Recent studies report promising results from supervised fine-tuning of pre-trained code language models for automated vulnerability detection on benchmarks such as PrimeVul. In this paper, we present a large-scale empirical evaluation of both model performance and dataset quality in this setting.   We systematically fine-tune three widely used encoder models (CodeBERT, GraphCodeBERT, and UniXCoder) across five imbalance mitigation strategies, extensive hyperparameter sweeps, and multiple random ...
  </details>

- **2026-11-04** — Xingchen Zou, Maonan Wang, Kemou Jiang et al. — [Traffic-VL: Reinforced Vision-Language Models for Generalizable End-to-End Traffic Signal Control](http://arxiv.org/abs/2611.06353v1)
  <details><summary>📄 Abstract</summary>
  Existing traffic signal control methods typically rely on structured traffic states produced by dedicated perception pipelines. Emerging visual approaches often use idealized simulator images and convert them into intermediate representations before control, limiting their ability to directly exploit roadside visual observations. To bridge both the visual-domain and perception-to-decision gaps, we introduce SynTra-V and Traffic-VL. SynTra-V converts physics-based traffic simulations into photore...
  </details>

- **2026-11-04** — Jiongchi Yu, Keke Lian, Junqing Wang et al. — [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](http://arxiv.org/abs/2611.06294v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding assistants and agents construct a repository context before generating code. For security-sensitive code, this context decides whether the model sees the project's safeguards (e.g., authorization checks) or insecure code to imitate. However, context construction is designed almost exclusively for functional correctness, and secure-code benchmarks treat the context as fixed, so how repository context affects the security of generated code remains unclear. We cons...
  </details>

- **2026-11-04** — Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro et al. — [Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks](http://arxiv.org/abs/2611.06257v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input that crashes the vulnerable build, is a natural target for them, since it is an automated analysis task closer to test generation than to code comprehension and it runs against a build that must be executed rather than ...
  </details>

- **2026-11-04** — Zhi Hong, Qianlong Wang, Hongchen Wei et al. — [HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](http://arxiv.org/abs/2611.06254v1)
  <details><summary>📄 Abstract</summary>
  The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through costly end-to-end evaluations. We introduce HarnessFlow, a framework for optimizing complete executable harnesses under a limited candidate-evaluation budget, with the model and task environment held fixed. HarnessFlow or...
  </details>

- **2026-11-04** — Martin Pinzger, Katharina Stengg, Christian Macho et al. — [SBVUL: Statement-Based Vulnerability Detection](http://arxiv.org/abs/2611.06135v1)
  <details><summary>📄 Abstract</summary>
  Many recent approaches for vulnerability detection use large language models (LLMs) to classify functions as vulnerable or benign, leaving developers to locate the exploitable statements. Furthermore, while these approaches have shown performance improvements, they still fall short in distinguishing vulnerable from patched real-world functions. This paper presents SBVul, an agentic approach that detects exploitable statements in C/C++ functions. In Phase~1, an LLM agent explores the function and...
  </details>

- **2026-11-04** — Songtang Han, Letian Liu, Zhiyan Yang et al. — [High-transformer-ratio plasma-based afterburner for extending X-ray free-electron laser photon energies to $\gtrsim$50 keV](http://arxiv.org/abs/2611.05957v1)
  <details><summary>📄 Abstract</summary>
  Bright coherent X-rays in the $\gtrsim$50 keV range are highly desirable for applications in materials science, high-energy-density physics, and nuclear physics, but are difficult to obtain from present X-ray free-electron laser (XFEL) facilities. Plasma-based afterburners offer a compact route to increasing the electron-beam energy, yet high transformer ratio (TR) operation is vulnerable to hosing instability, which can severely degrade the witness beam quality. We propose using a transversely ...
  </details>

- **2026-11-04** — Penghui Li — [When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](http://arxiv.org/abs/2611.05806v1)
  <details><summary>📄 Abstract</summary>
  Office documents are now routinely uploaded to large language models (LLMs) for processing. However, an LLM does not always see what a human sees, because it typically reads the text that an extractor produces from the document's underlying Office Open XML (OOXML) files. Depending on the implementation, extractors differ in which OOXML parts they read and how they interpret them, so their output can differ from what Office applications display. For example, by slightly shifting the positions of ...
  </details>

- **2026-11-03** — Dar-Yen Chen, Yi-Zhe Song — [NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers](http://arxiv.org/abs/2611.05648v1)
  <details><summary>📄 Abstract</summary>
  Adversarial diffusion distillation has conventionally relied on image features for discrimination. We revisit this choice for multimodal diffusion transformers (MMDiTs), whose text stream becomes image-dependent through joint attention. We introduce Text-Stream Adversarial Distillation (TSAD), which exploits intermediate text-token states as a new adversarial representation. Because the text stream has already read the image while remaining tied to the text condition, changing that condition cha...
  </details>

- **2026-11-03** — Soraya Frías-Guadalupe, Pedro Paredes, Carlos Castaneda-Marroquín — [Cibersapiens: Gamifying Cybersecurity Education to Engage Secondary Students](http://arxiv.org/abs/2611.05587v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity education and awareness are often tailored for businesses, leaving general citizens, especially young people, unprepared. Despite the availability of educational resources, cybersecurity training is not provided equally to all individuals, particularly children and teenagers. As digital risks such as sexting, grooming, and cyberbullying, among others, increase, young users remain vulnerable. However, existing awareness efforts fail to engage them effectively and current content lac...
  </details>

- **2026-11-03** — Reza Ramji, Preston Vander Vos, Ziming Zeng et al. — [Anduin: A sybil-resistant agentic marketplace reputation system](http://arxiv.org/abs/2611.05586v1)
  <details><summary>📄 Abstract</summary>
  As autonomous AI agents enter permissionless onchain markets, selecting new service providers remains a core challenge. Existing reputation systems depend on scarce resources like human curation, identity credentials, or voluntary reviews, while naive volume rankings are vulnerable to Sybil attacks.   We evaluate whether existing onchain payment histories can yield provider ratings that are resilient against Sybil attacks. Using a 157-day dataset comprising 66M agentic transactions worth $6.1M a...
  </details>

- **2026-11-03** — Sasha Luccioni, Travis LaCroix — [What Do We Mean When We Say 'F*ck AI'?: Moral Panic, Semantic Indeterminacy, and the Reification of Techno-Capitalism](http://arxiv.org/abs/2611.05574v1)
  <details><summary>📄 Abstract</summary>
  Academic and (increasingly) public resistance to artificial intelligence (AI) often blurs the line between legitimate critique of techno-capitalist exploitation and (inflated) existential risk. Moreover, discourse around AI can sometimes resemble a "moral panic" where an apparently clear and identifiable scapegoat is targeted in lieu of the complex systemic problems that are causing (genuine and justified) social anxieties. However, AI is not a monolith. In this paper, we explore the environment...
  </details>

- **2026-11-03** — Hemanth Ram, Sai Shankar Narasimhan, Shubhankar Agarwal et al. — [TSFM Meets LLM: Context as Covariates](http://arxiv.org/abs/2611.05515v1)
  <details><summary>📄 Abstract</summary>
  Textual information is ubiquitous in real-world time series datasets, appearing as news, reports, and annotations that hold key predictive signals not deducible from numerical history alone. Large Language Models (LLMs) interpret text but lack numerical precision, while Time Series Foundation Models (TSFMs) are quantitatively accurate but cannot reason about the effects of text. Moreover, the lack of large-scale paired multimodal datasets limits progress in bridging this gap. In this work, we ad...
  </details>

- **2026-11-03** — WonJun Moon, Seongchan Kim, Dahun Kim et al. — [Factorized MLLM Embeddings for Composed Image Retrieval](http://arxiv.org/abs/2611.05193v2)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) aims to retrieve a target image given a reference image and a modification text. Although recent approaches leveraging Multimodal Large Language Models (MLLMs) have shown significant progress, we argue that the MLLM's compositional understanding remains underutilized. This stems from directly mapping composed queries into a retrieval embedding via contrastive supervision alone, without explicitly resolving the intended visual modifications. In this work, we introdu...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 53 papers

- **2026-11-04** — Yichiet Aun, Mohammed A. Alhartomi, Jing Jie Tan et al. — [Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](http://arxiv.org/abs/2611.06585v1)
  <details><summary>📄 Abstract</summary>
  AI agents rely on third-party tools, such as Model Context Protocol (MCP) servers, whose publishers can be authenticated and whose execution can be restricted by runtime security policies. Yet authenticity does not guarantee benign behaviour: a legitimately signed tool may perform its advertised function while concealing malicious code that leaks confidential information. We demonstrate this trust failure with a signed MCP tool that embeds sensitive data in requests to a policy-allowed destinati...
  </details>

- **2026-11-04** — Fei Lin, Tengchao Zhang, Ziyang Gong et al. — [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](http://arxiv.org/abs/2611.06911v1)
  <details><summary>📄 Abstract</summary>
  Self-Driving Chemical Laboratories (SDCLs) are moving chemical experimentation toward embodied automation, where machines must perceive laboratory scenes, reason about experimental states, and act under physical, procedural, and safety constraints. Although Multimodal Large Language Models (MLLMs) are increasingly considered as embodied brains for such systems, existing laboratory benchmarks mainly focus on safety, anomaly detection, or general scientific understanding, leaving their execution-o...
  </details>

- **2026-11-04** — Austin C. Kozlowski, Avital Mintz, Madison Lee — [Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs](http://arxiv.org/abs/2611.06848v1)
  <details><summary>📄 Abstract</summary>
  Common methods for monitoring features in large language models (LLMs) such as linear probes and sparse autoencoders (SAEs) assume that features maintain a consistent representation across contexts. LLMs, however, can flexibly adopt different perspectives or "personas" that suggest different underlying systems of conceptual relations. In this paper, we examine whether prompting an LLM to adopt a persona alters the representational geometry of the model's latent space. We extract representations ...
  </details>

- **2026-11-04** — Nil-Jana Akpinar, Eugenia Kim, Natalie Isak et al. — [Measuring Risk, Not Harm: Detecting Psychological Harm Risk Factors in LLM Conversations](http://arxiv.org/abs/2611.06806v1)
  <details><summary>📄 Abstract</summary>
  Psychological harms from interactions with large language models cannot be monitored directly because they may emerge over repeated interactions and depend strongly on subjective individual user context. We propose measuring risk, not harm: detecting observable AI behaviors that constitute risk factors for psychological harm at the AI response level and aggregating these signals to support longitudinal monitoring. We operationalize eight such behaviors and construct a synthetic multi-label corpu...
  </details>

- **2026-11-04** — Chijin Zhou, Quan Zhang — [Rethinking Access Control for AI Agents: Recent Advances and Open Challenges](http://arxiv.org/abs/2611.06764v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents access data, invoke tools, and act on users' behalf. Keeping these actions within authorized bounds is challenging because agents choose their own execution paths while permissions and operating conditions may change. This paper surveys recent advances in agent access control across four areas: policy specification and derivation, identity and delegation, action and resource enforcement, and information flow control. We compare their control objects, enforcement bound...
  </details>

- **2026-11-04** — Shubhabrata Mukherjee, Jeffrey Donatelli, Daniela Ushizima — [Route First, See Later: Enabling Vision Agents to Reason Scientifically by Separating Routing Policy from Action Spaces](http://arxiv.org/abs/2611.06760v1)
  <details><summary>📄 Abstract</summary>
  Scientific image-analysis workflows require agents to select among diverse capabilities like description, detection, counting, and segmentation. Current multi-tool architectures conflate intent interpretation with visual execution, masking whether a failure arises from flawed reasoning (misrouting) or failed perception (invalid tool execution). This lack of auditability renders agents unreliable for high-stakes scientific automation. We introduce ZETA, an extensible architecture that operational...
  </details>

- **2026-11-04** — Zhonghao Zhan, Javad Forough, Yefan Zhang et al. — [Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment](http://arxiv.org/abs/2611.06727v1)
  <details><summary>📄 Abstract</summary>
  When multi-agent systems act on the external world, a single agent's faulty output can spread across tasks before detection, creating a system-wide blast radius. Single-agent guardrails are confined to individual harnesses, while existing multi-agent controls either cancel only the faulty source and miss downstream consumers or halt and roll back the entire workflow at the cost of healthy work. We present Airlock, a multi-agent runtime and guardrail for selective post-alert fault containment. It...
  </details>

- **2026-11-04** — Zohreh Abbasi Liasi, Batoul Hammoud, Anas Madkoor et al. — [Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based Analysis of Relational Knowledge](http://arxiv.org/abs/2611.06715v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) assumes that language models can reason over relations stated in their context rather than fall back on associations memorized during pretraining. We study this evidence-conditioned relational reasoning in isolation, with the facts supplied directly in the prompt rather than retrieved. \textsc{Rel-Bloom} is a controlled multilingual diagnostic of 450 multiple-choice questions built from 30 Wikidata relations; the same source relations are instantiated at five...
  </details>

- **2026-11-04** — Henry Zhang — [Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found](http://arxiv.org/abs/2611.06607v1)
  <details><summary>📄 Abstract</summary>
  Agentic research loops that let a language model propose a change, run a fixed experiment and keep whatever improves the metric work well in machine learning. In trading research the same loop is a machine for producing false discoveries: a backtest that "improves the metric" is, by default, overfit, look-ahead, a multiple-comparisons artifact, cost-free, or market drift wearing a strategy. We describe Autonomous Quant Researcher, an open-source loop built on the opposite premise: the model prop...
  </details>

- **2026-11-04** — Chenyang Le, Pei Zhang, Yuxiang Chen et al. — [CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation](http://arxiv.org/abs/2611.06501v1)
  <details><summary>📄 Abstract</summary>
  Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency. While Large Language Models (LLMs) excel in offline translation, current LLM-based SimulST systems predominantly rely on prefix-incremental generation. This paradigm suffers from redundant Key-Value cache recomputation and necessitates external Voice Activity Detection to process unbounded streams. To overcome these bottlenecks, we propose an end-to-end interleaved read-write framework built upon an omn...
  </details>

- **2026-11-04** — Jonguk Cheong, Myungbin Hwang, Eulgyu Kim et al. — [KVGuard: A KV Cache Safety Checker for LLM Serving Systems](http://arxiv.org/abs/2611.06138v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM serving systems manage the KV cache through PagedAttention, a custom GPU allocator that partitions a single CUDA-allocated region into fixed-size physical blocks and maps each request to those blocks through a CPU-built block table. This block-based design exposes a previously unstudied class of memory safety bugs in the KV cache, including double-free, use-after-free, out-of-bounds access, uninitialized read, and permission violation, which silently corrupt outputs or break request i...
  </details>

- **2026-11-04** — Chunxiao Wu, Huixin Huang, Jialei Pan et al. — [XuanJian-DINOSAR: A SAR Foundation Model Based on Global and Local Semantic Consistency](http://arxiv.org/abs/2611.06105v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised pre-training on synthetic aperture radar (SAR) imagery enables transferable representations, but the optical-SAR domain gap and speckle perturbations limit representation stability. Most SAR foundation models use masked image modeling (MIM) through pixel reconstruction or structural feature prediction, which is sensitive to speckle or relies on predefined operators. Joint modeling of cross-view semantics and perturbation stability at corresponding spatial locations remains undere...
  </details>

- **2026-11-04** — Danwen Chen, Guangba Yu, Pengfei Chen — [SWEOps-Bench: Evaluating Agents for End-to-End Resolution of Software-Induced Cloud Incidents](http://arxiv.org/abs/2611.06099v1)
  <details><summary>📄 Abstract</summary>
  As autonomous agents advance, the traditional boundary between software development and cloud operations gradually blurs, increasing the need for integrated incident detection, localization, and remediation. Existing benchmarks evaluate isolated diagnostic queries or repository-level program repair, failing to test continuous incident resolution across operational clusters and source repositories. We introduce SWEOps-Bench, an interactive benchmark comprising 55 reproducible incident tasks deriv...
  </details>

- **2026-11-04** — Ashutosh Dayal, Mallika Garg, Debashis Sen — [Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline](http://arxiv.org/abs/2611.06000v1)
  <details><summary>📄 Abstract</summary>
  Designing systems that attribute a generated image to its source model has lately become a major area of AI research. Most existing datasets and systems related to image source attribution are targeted towards the detection of architectural signatures of the source models. Distinct from this, focusing on stable diffusion, we introduce a novel task, IntrAA-SD, Intra-Architecture source Attribution for Stable Diffusion, where the source models to be differentiated share the same architectural back...
  </details>

- **2026-11-04** — Junnuo Wang, Weihan Xu, Hao-Wen Dong — [Clips2Story: Training-Free Video Storyboarding and Editing Using Multimodal Retrieval-Embedded Generation](http://arxiv.org/abs/2611.05992v1)
  <details><summary>📄 Abstract</summary>
  Video editors often work with large collections of fragmented footage and must select and organize relevant clips into a coherent story. However, many existing video editing and summarization methods assume a temporally ordered source video and aim to preserve its original narrative and temporal structure. In this paper, we introduce Clips2Story, a training-free, LLM-based pipeline that enables users to create keyword-specified short videos from a pool of video clips. Given a pool of clips and a...
  </details>

- **2026-11-04** — Yusheng Dai, Vladimir Iashin, Kangdi Wang et al. — [LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds](http://arxiv.org/abs/2611.05988v1)
  <details><summary>📄 Abstract</summary>
  Streaming video-to-audio (V2A) generation is essential for immersive interactive applications. However, real-time constraints leave existing streaming V2A methods far behind offline models: (1) visual frontends shrink their receptive fields to cut look-ahead latency, severely degrading audio-visual alignment; (2) causal autoregressive diffusion backends denoise each audio patch in isolation, impairing audio quality. To this end, we present LiveFoley, a streaming causal autoregressive diffusion a...
  </details>

- **2026-11-04** — Shumpei Shiina, Haruka Takahashi, Kento Sasaki et al. — [Enforcing Accountable Disclosure in Confidential AI](http://arxiv.org/abs/2611.05971v1)
  <details><summary>📄 Abstract</summary>
  Advances in CPU and GPU confidential computing enable confidential AI, allowing LLMs to process user prompts without exposing them to service providers or infrastructure operators. However, AI agents often need to send prompt-derived information to external services, and providers may also require limited disclosure for safety monitoring and failure diagnosis. We propose CORDE, a system for confidential virtual machines (CVMs) designed to satisfy the principle of Confine or Declare: user-derived...
  </details>

- **2026-11-04** — Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan et al. — [A Hybrid Approach for Automated Security Pattern Recovery](http://arxiv.org/abs/2611.05823v1)
  <details><summary>📄 Abstract</summary>
  Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source code remains challenging because security patterns are abstract, span multiple components, and admit many valid implementations. We present SecPatRec, a hybrid approach for automated security pattern recovery from sourc...
  </details>

- **2026-11-04** — Wenyi Xu, Renzhe Zhou, Songyang Li et al. — [WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution](http://arxiv.org/abs/2611.06777v1)
  <details><summary>📄 Abstract</summary>
  Algorithm-driven services, including search, recommendation, and advertising, rely on multi-stage model pipelines. While research prioritizes model optimization, post-deployment monitoring focuses on operational reliability. Yet operationally healthy systems may still produce poor-quality results, exposing a gap in existing evaluation and monitoring practices. However, a systematic problem formulation and benchmark for this task remain lacking. To bridge this gap, we formulate System Quality Dia...
  </details>

- **2026-11-04** — Jiuwu Hao, Yuting Wan, Liguo Sun et al. — [Uncertainty-Driven Efficient Communication for UAV-Based Collaborative Perception](http://arxiv.org/abs/2611.06635v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicle (UAV)-based collaborative perception enables multiple agents to share complementary perceptual information, overcoming limitations such as occlusion and limited sensing range. Communication efficiency is a critical bottleneck, as UAVs operate under stringent bandwidth and computational constraints. However, existing spatial selection methods focus predominantly on foreground regions to reduce missed detections, neglecting perceptually ambiguous regions and leaving false d...
  </details>

- **2026-11-04** — Jingwen Yu, Pengyu Wang, Jin Wu et al. — [UniLoop: Unified Loop Closure Detection from Retrieval to Geometric Verification and Relative Pose Estimation](http://arxiv.org/abs/2611.06378v1)
  <details><summary>📄 Abstract</summary>
  Loop closure detection conventionally cascades separate models for global retrieval, geometric verification, and relative pose estimation, leading to redundant computation and disconnected visual representations. We propose UniLoop, a unified framework that reuses the hierarchical representations of the pretrained geometric foundation model throughout this pipeline. A shared image encoder produces features for compact global descriptors; the same features are passed to the cross-view decoder for...
  </details>

- **2026-11-03** — Zekai Li, Zhenke Liu, Yonghao Li et al. — [LIBRA: Programmatic Induction of Executable Tool Libraries](http://arxiv.org/abs/2611.05445v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow.We introduce LIBRA, a framework for Library Induction by Runtime Assembly that turns a flat tool catalog into an executable tool library. An LLM proposes per tool contracts of candidate invocations, reusable outputs and state changes...
  </details>

- **2026-11-03** — Sarah Montgomery-Taylor, Hamsa Subramaniam, Rob Brisk et al. — [Towards Multi-Method Evaluation of AI in Health: Integrating Benchmarks, Autoraters, and Expert Evaluation](http://arxiv.org/abs/2611.05127v2)
  <details><summary>📄 Abstract</summary>
  General-purpose generative AI (GenAI) models are being rapidly adopted in healthcare, but they are challenging to assess with traditional evaluation frameworks. These conceptual, methodological, and practical challenges parallel decades of work in evaluating clinician and health system quality and safety. We describe the adaptation of methods from several fields, combined with emerging technical approaches, into a structured, multi-method evaluation framework designed to give well-rounded assess...
  </details>

- **2026-11-03** — J. Chen, M. Eriksen, D. Navarro-Gironés et al. — [The PAU Survey: Self-supervised image denoising for flux-preserving photometry](http://arxiv.org/abs/2611.05447v1)
  <details><summary>📄 Abstract</summary>
  Context. Deep photometric surveys increasingly rely on low signal-to-noise imaging, where noise affects source detection, flux measurements, photometric redshifts, and sample selection. Self-supervised denoising methods are attractive because they do not require ground-truth images, but applying them to quantitative photometry requires controlling the flux biases they may introduce. Aims. We evaluate and improve Noise2Void (N2V) for denoising real astronomical images, focusing on preserving flux...
  </details>

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

- **2026-11-02** — Tianqi Gao, Ruobing Jiang — [Towards AI-Agent-Accelerated Research in High-Energy Physics: A Case Study in Monte Carlo Analysis](http://arxiv.org/abs/2611.03373v2)
  <details><summary>📄 Abstract</summary>
  We investigate how far contemporary LLM-based agents can participate in multistep computational high-energy-physics research under reproducible human supervision. Using a previously published CEPC Bell-observable analysis in $e^+e^- \to ZH$, $Z \to q\bar q$, $H \to ZZ^* \to 4μ$ as a case study, we test two capabilities. First, the agent performs an instruction-constrained reproduction: it is explicitly instructed not to use the published numerical results as analysis targets, although no technic...
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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-11-04** — Ji Pei — [Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation](http://arxiv.org/abs/2611.06724v1)
  <details><summary>📄 Abstract</summary>
  Dexterous robotic hands are increasingly coupled to large-scale human data and foundation models, yet progress in hardware, representation learning and evaluation is often assessed separately. This survey reviews work from January 2024 to early November 2026, with earlier studies included to establish technical lineages. We organize the literature into five interdependent layers: hardware; data collection and curation; cross-embodiment transfer; learning and foundation models; and evaluation and...
  </details>

- **2026-11-04** — Ruben Boone, Gilles Eerlings, Sebe Vanbrabant et al. — [Does Personality Persuade? Investigating Personality Trait Prompting and Persuasion in Large Language Models](http://arxiv.org/abs/2611.06572v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can be prompted to express different personality profiles, but it remains unclear how reliably they do so or whether personality affects their persuasiveness. We investigate these questions in two evaluations. First, we assess Big Five personality prompting using the IPIP-NEO-120, examining reproducibility, trait controllability, cross-trait effects, and unconditioned model profiles. Second, we conduct a within-subjects user study (N=32) in which participants discuss...
  </details>

- **2026-11-04** — Shumao Wu, Kongcheng Zhang, Jianqiang Huang et al. — [Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](http://arxiv.org/abs/2611.06543v1)
  <details><summary>📄 Abstract</summary>
  Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy trajectories can be distilled into natural-language process rubrics and used as process supervision signals. Based on this insight, we propose Online Rubric Self-Distillation (ORSD), which leverages self-derived process rubrics...
  </details>

- **2026-11-04** — Mingzhe Zheng, Yue Wu, Jing Tan et al. — [EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](http://arxiv.org/abs/2611.06518v1)
  <details><summary>📄 Abstract</summary>
  Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Existing approaches typically rely on fixed rewards for visual quality, motion quality, and text alignment that poorly capture emotional intent and can invite reward hacking, while RLHF is difficult to scale and subject to i...
  </details>

- **2026-11-04** — Ji Shi, Lirong Jie, Lexiao Zou et al. — [Trace2Eval: Contextualized Evaluation of Coding Agents from Real-World Traces](http://arxiv.org/abs/2611.06506v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly used in real-world workflows across diverse domains, motivating evaluation grounded in real user tasks. Existing benchmarks, however, largely rely on static public tasks with reference patches or hidden tests. Next-generation coding-agent benchmarks should therefore move beyond correctness on fixed tasks toward continually renewed evaluation of overall artifact quality in real user workflows.   We propose Trace2Eval, a dynamically updatable pipeline that constructs...
  </details>

- **2026-11-04** — Ye Yuan — [The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention](http://arxiv.org/abs/2611.06476v1)
  <details><summary>📄 Abstract</summary>
  Setting. This is an empirical characterization study; we propose no new method and run no comparisons against alternative objectives. We fine-tune Qwen3.5-4B with sparse LoRA and length-normalized DPO plus an SFT retention term (the RPO objective) on structured financial-filing tasks, and track downstream capability as the implicit reward margin grows to $\sim 7$ $β$-scaled units (nf4 training; $\sim 3$ under fp16 measurement on the unquantized base). Question. Does margin growth degrade capabil...
  </details>

- **2026-11-04** — Shengzhe Zhang, Qi Zhang, Dazhong Shen et al. — [$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](http://arxiv.org/abs/2611.06447v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action Models (VLAs) enable robots to perform manipulation tasks by leveraging Vision-Language Models (VLMs) to process visual observations and language instructions. However, the action prediction objective itself lacks fine-grained task-specific perceptual supervision, making it prone to relying on task-irrelevant visual shortcuts, leading attention away from target objects and key interaction areas, thereby limiting its operational performance and generalization ability. To ad...
  </details>

- **2026-11-04** — Jiaqi Deng, Zhe Fu, Yakun Chen et al. — [Entropogram-guided Visual Realignment Decoding: Capturing the Rhythm of Multimodal Reasoning](http://arxiv.org/abs/2611.06415v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have demonstrated remarkable progress on cross-modal reasoning tasks, yet they continue to suffer from hallucinations in long-chain reasoning processes. In this work, we revisit hallucination in MLLMs from the perspective of reasoning generation dynamics. We argue that entropy is not merely a static measure of uncertainty but a structured signal that reflects how modality information is integrated throughout decoding. Through systematic analysis, we ident...
  </details>

- **2026-11-04** — Anthony Nguyen, Wenjun Lin — [Does Context Compression Preserve Refusal Alignment?](http://arxiv.org/abs/2611.06380v1)
  <details><summary>📄 Abstract</summary>
  Context compression reduces inference cost by encoding inputs into compact representations while preserving semantic content. An open question is whether semantic preservation alone is sufficient to maintain downstream behaviours such as refusal alignment. We investigate this question and find that encoder-based compression systematically weakens refusal behaviour in instruction-tuned language models, despite high reconstruction fidelity. This effect persists across model families and compressio...
  </details>

- **2026-11-04** — Yaowen Ye, Jacob Steinhardt, Sarah Schwettmann et al. — [Mass Producing Training Data with Surprising Side Effects](http://arxiv.org/abs/2611.06324v1)
  <details><summary>📄 Abstract</summary>
  Training data can have unexpected side effects on language model behavior outside the training domain: insecure code data can induce broad misalignment, and outdated bird names can induce a 19th-century persona. Understanding such generalization is hard because only dozens of isolated examples exist, each constructed by hand or discovered by accident. We propose automatically discovering such datasets with surprising side effects (DSSEs). We define three objectives for DSSEs: they should (1) eli...
  </details>

- **2026-11-04** — Ziyi Jin, Kangjin Yu, Beichen Wang et al. — [Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM](http://arxiv.org/abs/2611.06308v1)
  <details><summary>📄 Abstract</summary>
  Feed-forward geometric foundation models enable dense monocular reconstruction without requiring camera calibration, but independently reconstructed submaps can accumulate scale drift, and even a valid revisit can yield an inconsistent cross-submap measurement. We extend VGGT-SLAM 2.0 with fixed-root scale anchoring and short-sequence-assisted direct loop connections. SALAD selects an image pair between the initial submap and each eligible new submap; joint VGGT inference then uses learned impli...
  </details>

- **2026-11-04** — Zhiliang Zhu, Jiazheng Huang, Dawei Zhao — [Beyond Scene Shortcuts: Action-Centric Video-Text Alignment for Fine-Grained Action Understanding](http://arxiv.org/abs/2611.06302v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained action understanding requires vision-language models to ground what an agent does, how it acts, and why it acts in spatio-temporal evidence. However, richer supervision can backfire: fine-tuned models may generate detailed action descriptions grounded in static scenes and salient objects rather than motion, a failure we call Environment-Grounded Action Hallucination (EGAH). To mitigate EGAH, we propose Staged Attention Rectification and Reinforcement (STARR), an action-centric video...
  </details>

- **2026-11-04** — Tanmay Bakshi, Chenglong Wang, Simra Shahid — [Evaluating Human-LLM Alignment on Visualization Preference](http://arxiv.org/abs/2611.06272v1)
  <details><summary>📄 Abstract</summary>
  There are often multiple valid visualizations, spanning different chart types, visual encodings, and aesthetic choices, that can all support a user's goal of analyzing a dataset. Determining which of these candidate visualizations is most appropriate, however, remains challenging. Prior work has leveraged expert-curated taxonomies to guide visualization design and subsequent quality evaluation, a practical evaluation model must also account for human-centric factors. Latest visualization tools i...
  </details>

- **2026-11-04** — Henrik Marklund, Alex Infanger, Benjamin Van Roy — [A Definition of Catastrophic Performance](http://arxiv.org/abs/2611.06219v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they typically do not distinguish between merely suboptimal and catastrophic outcomes. To enable rigorous analysis of catastrophic risk from AI misalignment, we introduce a formal definition of catastrophic performance. Our definition is based on two reference values. The first, baseline value, captures the value attained if ...
  </details>

- **2026-11-04** — Peiran Wu, Fangfei Gou, Zhaoxi Mu et al. — [SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?](http://arxiv.org/abs/2611.06083v1)
  <details><summary>📄 Abstract</summary>
  Omni models answer questions about videos by jointly processing sampled frames and audio in one turn, with progress driven largely by scaling model size and omni training data. We ask whether a model needs to hear the audio directly at all, and present SleuthVLM, an agent harness built on a VLM that never hears the audio directly: speech will be transcribed into text, and the VLM will sleuth the video on its own without any predefined workflow. On four omni benchmarks with videos up to 90 minute...
  </details>

- **2026-11-04** — Mengqi Huang, Wenchuan Wang, Zhendong Mao et al. — [Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring](http://arxiv.org/abs/2611.05893v1)
  <details><summary>📄 Abstract</summary>
  Identity-preserving video generation aims to synthesize high-quality and visually realistic videos from textual and visual conditions while faithfully maintaining the subject's identity across diverse motions. Prior methods have extensively introduced reference-guided control signals and identity-aware conditioning to improve facial alignment from reference images. However, improving static identity alignment alone creates a fundamental tension between identity fidelity and temporal controllabil...
  </details>

- **2026-11-03** — Justin Downes, Robby Milletich, Newel Hirst — [Same Method, Different Task: What the Bitter Lesson Does Not License in Social Simulation](http://arxiv.org/abs/2611.05717v1)
  <details><summary>📄 Abstract</summary>
  The bitter lesson holds that general methods leveraging computation defeat hand-encoded domain knowledge. We argue it carries a condition its popular reading omits: in every case Sutton cites, the general method was scaled against the same task the domain engineering was solving. Social simulation substituted across tasks instead, replacing hand-built agents with an artifact optimized for predicting text. The move is bitter-lesson-shaped, but the lesson does not license it. Prediction is a solit...
  </details>

- **2026-11-03** — Keyty Loza, Shayan Monadjemi — [How Do Artificial Agents Make Decisions in Light of Visual Data?](http://arxiv.org/abs/2611.05671v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have demonstrated significant advances in reasoning with visual data, which is particularly important given that much of human knowledge is encoded visually in scientific articles and other sources. However, a gap remains in understanding how artificial agents, powered by VLMs, perceive and navigate decision-making under uncertainty in the presence of visual data. This study explores this gap by evaluating and analyzing autonomous decision-making processes. Building...
  </details>

- **2026-11-03** — Elad Yoshai, Natan T. Shaked — [CAPTOR: text-encoder-free grounding by counting caption co-occurrence over the visual words of a frozen encoder](http://arxiv.org/abs/2611.05599v1)
  <details><summary>📄 Abstract</summary>
  Grounding a text query in an image needs a matrix scoring every term against every patch. Vision-language models compute it with an aligned text encoder, which many image encoders, such as histopathology-related models trained on slides alone, lack. The Caption-Anchored Patch-Term Occurrence Representation (CAPTOR) estimates the matrix without a text encoder. It clusters a frozen image encoder's patch tokens into visual words and describes each captioned image by its share of patches in each wor...
  </details>

- **2026-11-03** — Hei Yi Mak, Hoang Le, Mehran Taghian Jazi et al. — [Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs](http://arxiv.org/abs/2611.04376v2)
  <details><summary>📄 Abstract</summary>
  In this work, we study end-to-end FP4 reinforcement learning (RL) post-training for Mixture-of-Experts (MoE) large language models. Recent work on FP4 RL has introduced effective recovery recipes that restore accuracy under aggressive low-precision quantization for dense models, but we find that the same approach yields no improvement over the naive FP4 baseline in the MoE setting. We conduct an in-depth study to understand why. Our analysis identifies the root cause in the routing mechanism uni...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 45 papers

- **2026-11-04** — Joan C. Timoneda, Sebastián Vallejo Vera — [Replicability, Reproducibility, and Robustness in Political and Social Science Research with Large Language Models](http://arxiv.org/abs/2611.06639v1)
  <details><summary>📄 Abstract</summary>
  This chapter addresses the central reproducibility problem of research with large language models. LLM output is probabilistic and varies across models and versions, which can have significant effects on downstream statistical results. The chapter distinguishes between replicability, reproducibility, and robustness, and proposes a probabilistic standard based on the distribution of results, not identical outputs. It introduces a standardized prompt script, tests within-model variation for encode...
  </details>

- **2026-11-04** — Harshit Gupta, Shunichi Ishihara — [How Well Can Large Language Models Impersonate Individual Authors? A Comparative Evaluation](http://arxiv.org/abs/2611.05771v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the authorship impersonation capacity of six widely used large language models (LLMs): Gemini 3 Pro, Claude Opus, GPT 5.2, GPT 5.2 Pro, DeepSeek 3.2, and Grok 4.1 Fast. The evaluation was conducted using short product review texts selected to ensure high within author consistency in individual writing style. Two types of in context prompt were designed: a simple prompt with minimal instruction and a complex prompt incorporating explicit stylometric guidance for mimicry. A...
  </details>

- **2026-11-04** — Qiang Wang, Jianxin Bi, Shulong Jiang et al. — [PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World](http://arxiv.org/abs/2611.06768v1)
  <details><summary>📄 Abstract</summary>
  Coding agents powered by models such as GPT-6-Astra connect spatial reasoning with executable robot behavior, raising the question of how such agents can produce lasting improvements in robot capabilities from physical interaction. In this work, we study embodied recursive self-improvement (RSI) through real-world exploration, code refinement, and deployment using PyRUA-REAL, a framework in which coding agents retain interaction experience as persistent memory and reusable executable skills that...
  </details>

- **2026-11-04** — Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel — [A Framework for Context Enrichment and Selective Robustness in LLM Social Agents](http://arxiv.org/abs/2611.06914v1)
  <details><summary>📄 Abstract</summary>
  Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt variations, creating a validation problem for social simulation. One plausible hypothesis is that this brittleness reflects a lack of grounding and can be reduced by enriching the context provided to the agents. Whether ric...
  </details>

- **2026-11-04** — Ruikang Li, Zixuan Chen, Jiarui Wu et al. — [TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing](http://arxiv.org/abs/2611.06741v1)
  <details><summary>📄 Abstract</summary>
  Strong single-turn editing performance does not guarantee reliable multi-turn interaction: as edited outputs are repeatedly reused, small unintended changes can accumulate into severe visual drift. This long-term drift is often mitigated through training on multi-turn data or cross-turn rollouts, potentially altering pretrained priors, or through specialized inference-time mechanisms that are difficult to scale to foundation models. We introduce TailSteer, a final-stage training framework that i...
  </details>

- **2026-11-04** — Yutong Ma — [Data Center Agglomeration and Power Infrastructure Capacity in the United States](http://arxiv.org/abs/2611.06737v1)
  <details><summary>📄 Abstract</summary>
  The continuous expansion of digital infrastructure, especially data centers, has imposed unprecedented, geographically concentrated stress on existing power grids. However, rigorous causal evidence quantifying how these facilities reshape local power-infrastructure supply remains limited. This study builds a comprehensive county-level US panel dataset spanning 2010-2024, uniquely integrating individual data center building footprints and power-plant additions. To mitigate endogeneity and high-di...
  </details>

- **2026-11-04** — Kejian Zhu, Zhuoran Jin, Shangqing Tu et al. — [What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](http://arxiv.org/abs/2611.06483v1)
  <details><summary>📄 Abstract</summary>
  While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and ...
  </details>

- **2026-11-04** — Kasra Fallah, Rudramani Singha, Hannah Ghanei et al. — [Mind Control of LLMs via Closed-Loop Stimulation: Out-of-Distribution Robustness](http://arxiv.org/abs/2611.06418v1)
  <details><summary>📄 Abstract</summary>
  Brains and large language models need not be considered equivalent systems to reveal an interpretable commonality: both exhibit high-dimensional, nonlinear dynamics whose behavior can only be modeled imperfectly. This creates a shared challenge whenever we seek to intervene in their dynamics. A controller may either rely on a model identified around a particular operating regime and risk failure as the system moves away from that regime, or explicitly account for uncertainty and a changing inter...
  </details>

- **2026-11-04** — JunYong Lee, Woo Kyung Kim, Honguk Woo — [MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing](http://arxiv.org/abs/2611.06389v1)
  <details><summary>📄 Abstract</summary>
  Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model resilience explicitly, instead relying on ad-hoc output correction that limits systematic, runtime management of robustness. In this work, we propose Multi-Agent Mesh (MA-Mesh), a framework that constructs a role-based self-healing layer on top of a collaboration pattern. Specifically, MA-Mesh generates resi...
  </details>

- **2026-11-04** — Varun A. Paturkar, Shankar Gangisetty, C. V. Jawahar — [MotoVerse: A Benchmark for Predictive Perception of Motorized Two-Wheelers in Dense Unstructured Traffic](http://arxiv.org/abs/2611.06007v1)
  <details><summary>📄 Abstract</summary>
  Motorized Two-Wheelers (MTWs) dominate personal transport across much of the Global South, yet remain largely overlooked in predictive perception research for autonomous driving and ADAS. We introduce MotoVerse, a benchmark for predictive perception from an MTW's ego-centric perspective. MotoVerse comprises 949 maneuver clips collected in dense, unstructured traffic and trajectory annotations for over 31,000 surrounding road agents, including over 16,000 MTWs, enabling two complementary tasks: E...
  </details>

- **2026-11-04** — Shuli Jiang, Khushbu Pahwa, Yuting Zhang et al. — [Learning When Human Decisions Matter: Executor-Relative Consultation Value for LLM Agents](http://arxiv.org/abs/2611.05814v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly automate complex tasks, but human decision capacity does not scale with their capabilities. In many applications, humans remain essential for providing private context, authority, or judgments unavailable to the agent. We formulate human decision capacity allocation: given multiple consultation opportunities and a limited budget, at which decisions should an LLM agent consult a human? The central challenge is estimating consultation value, which is executor-dep...
  </details>

- **2026-11-04** — Rohit Mohan, Maximilian Luz, Swarnava Chowdhury et al. — [WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](http://arxiv.org/abs/2611.05801v1)
  <details><summary>📄 Abstract</summary>
  Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic tracking benchmarks assume closed-set taxonomies. Consequently, these benchmarks do not evaluate whether unknown objects can be consistently segmented and tracked across synchronized multi-camera sequences. We introduce WayP...
  </details>

- **2026-11-03** — Ce Li, Tao Lin — [Learning to Design Information](http://arxiv.org/abs/2611.05701v1)
  <details><summary>📄 Abstract</summary>
  Information designers, such as large language models and online platforms, often do not know the subjective beliefs of their receivers or users. We construct learning algorithms enabling the designer to learn the belief of a strategic receiver through repeated interactions. Our learning algorithms are robust to the receiver's strategic manipulation of the learning process of the designer. We study regret relative to two benchmarks to measure the performance of the algorithms. The static benchmar...
  </details>

- **2026-11-03** — Wei Wei, Yading Yuan — [Mitigating Spurious Invariance in Contrastive Learning: A Probabilistic Self-Supervised Learning Framework for Medical Image Analysis](http://arxiv.org/abs/2611.05734v1)
  <details><summary>📄 Abstract</summary>
  Owing to the prohibitive cost of manual annotation for enormous medical images, self-supervised learning (SSL) has gained substantial attention and shown promise in various medical imaging tasks. Among SSL approaches, contrastive learning has emerged as a prominent one, encouraging models to encode semantic information that remains invariant between different augmented views. However, this invariance can be spurious for medical images, as subtle but critical medical features can be suppressed du...
  </details>

- **2026-11-03** — Pouya Sohrabipour, Yihong Feng, Chaitanya Kumar Reddy Pallerla et al. — [TRUST-Stereo: Teacher-Assisted Robust Uncertainty-Guided Search and Transfer for Fast Stereo Matching](http://arxiv.org/abs/2611.05689v1)
  <details><summary>📄 Abstract</summary>
  Coarse-to-fine stereo matching enables efficient disparity estimation but remains sensitive to errors in propagated disparity, which may place ground-truth correspondences outside subsequent local search ranges. We propose TRUST-Stereo (Teacher-Assisted Robust Uncertainty-Guided Search and Transfer for Fast Stereo Matching), which addresses this limitation through an Uncertainty-Guided Residual Search Module (UGRSM). UGRSM estimates the reliability of propagated disparity and predicts residual o...
  </details>

- **2026-11-03** — Junhyung Ahn — [AGORA: Reliability-Aware Aggregation of LLM Judges via Item-Response Theory](http://arxiv.org/abs/2611.05556v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-judge is a common substitute for costly human evaluation, and aggregating several judges is the standard remedy for any single judge's bias. Judge pools mix judges of very different reliability, while the human-labeled sets that validate them hold a few hundred items or fewer. In this regime the per-item mean weights weak judges as heavily as strong ones, and confusion-table models such as Dawid-Skene must estimate a per-judge error table from too few items. We propose AGORA (Aggregatio...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 17 papers

- **2026-11-04** — Sofia Bobadilla, Carmine Cesarano, Raphina Liu et al. — [EPISTEME: Trustworthy Coding Agents Through Tool Call Intent](http://arxiv.org/abs/2611.06563v1)
  <details><summary>📄 Abstract</summary>
  Coding agents change software through tool calls. Tool calls mutate the local state. For good? For bad? Nobody knows. Agents never say why a tool call is made. We propose the epistemic agent design, in which the harness guarantees that the model declares why a tool call is made. The harness then records what the command actually did and checks the self-reported declaration against these effects. The result is a journal 1) that can guard calls before they run and 2) that supports audits and foren...
  </details>

- **2026-11-04** — Khalid Tounoussi, Mohammed Sayagh, Ali Ouni et al. — [MCP-Eco: A Linked Dataset of MCP Servers, Consumers, and Development Activity](http://arxiv.org/abs/2611.06897v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) enables LLM agents to access external tools and data. Studying its software ecosystem requires connecting server interfaces, the projects that configure these servers, and their development activity. However, this information is scattered across directories, package registries, configuration files, and repository histories. We present MCP-Eco, a relational dataset that integrates these sources and links consumer configuration declarations to candidate server proj...
  </details>

- **2026-11-04** — Shaoliang Yang, Jun Wang — [Ranking Agreement Does Not Reveal Paragraph-Edit Agreement in Two Released Paper Acceptance Predictors](http://arxiv.org/abs/2611.06789v1)
  <details><summary>📄 Abstract</summary>
  A fast acceptance classifier could select revisions for a slower evaluator. We ask whether agreement on existing papers supports that use. We compare a classifier of word and document features with two released text-only acceptance predictors fine-tuned from the same language model with three billion parameters. For 198 papers from the International Conference on Learning Representations, we compare model rankings of the original papers and of paragraph rewrites screened automatically for unchan...
  </details>

- **2026-11-04** — Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal et al. — [ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs](http://arxiv.org/abs/2611.06481v1)
  <details><summary>📄 Abstract</summary>
  Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure their own construction pipeline produces, and whether they survive a change of construction is rarely tested. We study this cross-construction portability: whether one retrieval procedure, with no construction-specific schema, relation names, or retuning, stays effective when the graph is built differently. We...
  </details>

- **2026-11-04** — Hongnian Huang, Hongliang Liu — [When Every Choice Is Correct: A Causal Study of Numerical Preference in Language Models](http://arxiv.org/abs/2611.06025v1)
  <details><summary>📄 Abstract</summary>
  When a language model chooses a number between 1 and 30, every integer in the range is valid, yet the model can favor particular answers. We use numerical choice to study how preference is processed across layers and tokens. Perturbation probing and gradient attribution nominate neurons for activation interventions. In a selected Qwen3-4B case, a pre-answer edit changes 17 to 15 while both runs first emit 1. After the edit ends, selective cache and attention-output replacements trace part of its...
  </details>

- **2026-11-04** — Hila Levi-Yosefi, Shunit Agmon, Ester Livshits et al. — [A Comparative Study of Importance Attribution to Columns in Deep Learning over Relational Databases](http://arxiv.org/abs/2611.05986v1)
  <details><summary>📄 Abstract</summary>
  Deep learning over relational databases has led to increasingly effective prediction models, motivating a growing need to explain their behavior. We study explanation methods that assign importance scores to individual database attributes, focusing on a fundamental question: to what extent does the choice of importance-attribution method matter? We develop a methodology to systematically compare importance-attribution methods and analyze their similarities and differences. In particular, we stud...
  </details>

- **2026-11-04** — Zimu Liu, Xiaoxi Guo, Xiaolu Tang et al. — [Can LLM Agents Learn to Test? Maintaining Scoped Experience as Testing Evidence for Mobile GUI Testing](http://arxiv.org/abs/2611.05873v1)
  <details><summary>📄 Abstract</summary>
  Repeated mobile GUI tests can reuse routes, locators, and recovery strategies from earlier executions. However, a route that worked in one workflow or app version may be irrelevant or misleading in another. We study how an LLM-based tester can retain useful experience while withholding entries contradicted by current observations. We present a maintenance contract for AdaptiTest in which reusable experience has an explicit applicability scope, trace provenance, and a lifecycle for confirmation, ...
  </details>

- **2026-11-03** — Ali Imran, Abdalwhab Bakheet Mohammed Abdalwhab, Rafael Gomes Braga et al. — [Reality and Perceptual Gaps in Expressive Swarm Robotics](http://arxiv.org/abs/2611.05244v2)
  <details><summary>📄 Abstract</summary>
  Moving robot swarms from simulation into the physical world can be difficult because small discrepancies in hardware, timing and communication can cascade across interacting robots and alter group behaviour. This challenge is known as the reality gap. When swarms operate in human environments, a second challenge emerges: a perceptual gap between what the swarm physically does and what human onlookers actually perceive. This study examines the same decentralised coordination code deployed across ...
  </details>

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


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-11-03** — Kiran Ravish, Ankita Kushwaha,  Preeti et al. — [MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models](http://arxiv.org/abs/2611.05524v1)
  <details><summary>📄 Abstract</summary>
  We propose MA-SafeDiffuser, a multi-agent extension of SafeDiffuser that equips diffusion-based trajectory planners with finite-time diffusion invariance guarantees for joint-agent safety specifications. Building on the single-agent construction that embeds control barrier function (CBF) constraints into reverse-diffusion updates, we: (i) formalize joint safe sets as intersections of per-agent and pairwise barrier sets; (ii) derive centralized and decentralized (communication-aware) constrained ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 6 papers

- **2026-11-04** — Eraldo Pereira Marinho — [Object-independent evaluation of small-data astronomical image classifiers: architecture, representation, and acquisition shortcuts](http://arxiv.org/abs/2611.06484v1)
  <details><summary>📄 Abstract</summary>
  Reported performance in small astronomical image datasets can reflect object reuse, field-of-view differences, acquisition settings, and catalogue-derived properties as well as astronomical morphology. We designed \dataset{} to measure these effects in a four-class task comprising galaxies, globular clusters, nebulae, and open clusters. The dataset contains 370 catalogue-supported physical objects, each represented by three Digitised Sky Survey FITS bands, and uses a group-constrained split of 2...
  </details>

- **2026-11-04** — Wenda Li, Weibing Cai, Congcong Yuan — [FA-Agent: An extensible multimodal agent framework for first-arrival picking in mountainous seismic data](http://arxiv.org/abs/2611.06555v1)
  <details><summary>📄 Abstract</summary>
  First-arrival traveltimes underpin near-surface velocity modeling and static corrections, but in low signal-to-noise mountainous land data the first arrival is often weak, intermittent, and masked by strong direct waves and noise. Energy-based pickers then pick later arrivals or noise, and deep-learning pickers usually require retraining for a new survey. Because erroneous picks bias first-arrival tomography, many difficult zones are still inspected and corrected manually. We present FA-Agent, a...
  </details>

- **2026-11-03** — Egor Pakhomov, Erik Nijkamp — [Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard](http://arxiv.org/abs/2611.05650v1)
  <details><summary>📄 Abstract</summary>
  Published explanations of why long-horizon agents fail are commonly taxonomies labeled over completed trajectories: a judge reads a transcript and names the failure. We argue that a claim attributing an agent's behavior to its history should carry intervention-verified evidence, per instance or via a validated estimator: freeze an executable mid-trajectory state, alter only the history the agent sees, and continue - executed rather than inferred from the transcript, at a state whose restoration ...
  </details>

- **2026-11-03** — Abdullah Al Kalbani, David M. Schultz, Alexandra K. Anderson-Frey et al. — [Can Large Language Models Review the Scientific Literature? A Test Against a 102-Article Benchmark](http://arxiv.org/abs/2611.05459v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to support scientific literature reviews, yet evaluations often examine individual tasks rather than the review process as a whole. We assess six AI tools across four stages: finding relevant articles, interpreting them, synthesizing across them, and proposing future research. The benchmark is a published review of the Spanish plume weather pattern and its 102-article corpus.   In the initial searches, five tools collectively identified 57 artic...
  </details>

- **2026-11-03** — Tamunotonye Harry, Yuanyuan Feng — [Personas Are Not People: Identity as State, Not Attribute](http://arxiv.org/abs/2611.05292v1)
  <details><summary>📄 Abstract</summary>
  Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person is defined by a persona, a written profile of fixed traits, demographics, and attitudes that a language model is instructed to act out. Every such system assumes that a person's identity is a stable attribute that behaves the same way in every situation the simulation presents. We show that this ass...
  </details>

- **2026-11-03** — Wen Zhou, Shaowen Wang, Upmanu Lall et al. — [Fusing Earth observation embeddings and spaceborne terrain with meteorological forcing for flood peak depth prediction from high-water marks](http://arxiv.org/abs/2611.05220v1)
  <details><summary>📄 Abstract</summary>
  Flood peak depth on normally dry land governs damage and risk to life, but is observed only sparsely, by post-event high-water mark (HWM) surveys, and depth derived from satellite flood extent is produced after the event and inherits the vertical error of the digital elevation model (DEM) it is computed from. Deep-learning flood models have in turn been trained on hydrodynamic simulations rather than on observed depths. We ask whether flood peak depth can be learned from field observations and p...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 194 papers

- **2026-11-04** — Georgios Feretzakis, Alexandros Papaspyridis — [Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation](http://arxiv.org/abs/2611.06498v1)
  <details><summary>📄 Abstract</summary>
  Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. We study this text-vector integrity gap. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls the vectors: the hijack rate equals the distribution of angular retrieval margin...
  </details>

- **2026-11-04** — Lorenzo Porcelli — [Clear Human Web: Where a Person Vouches for Every Client](http://arxiv.org/abs/2611.06286v1)
  <details><summary>📄 Abstract</summary>
  The web cannot tell whether a request comes from a person or from a program. Sites have checked the network address and puzzles in its place, and both have given way: automated traffic exceeds human traffic, and puzzles are solved for pay and by agents. This paper proposes the Clear Human Web, the part of the public web that sites open only to clients a person vouches for. A person's wallet presents their person identification data (PID) to one issuer, the only party that registers as a relying ...
  </details>

- **2026-11-04** — Pragyan Phukan — [AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment](http://arxiv.org/abs/2611.06170v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) excel in high-resource languages, their performance often degrades in low-resource languages due to tokenization inefficiencies, generative instability, and linguistic interference. This paper presents AssameseLM-E2B and its instruction-tuned variant, AssameseLM-E2B-it, a 2-billion-parameter model adapted specifically for low resource Assamese language. Built upon the Gemma-4 architecture, the model incorporates an expanded byte-level BPE vocabulary to reduce t...
  </details>

- **2026-11-04** — Bingran You, Wenjun Ke, Ria Rosenauer et al. — [FrontierPhysics: Evaluating Agents for End-to-End Physics Research](http://arxiv.org/abs/2611.06910v1)
  <details><summary>📄 Abstract</summary>
  AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across theoretical, computational, and experimental physics. Each task requires agents to review...
  </details>

- **2026-11-04** — Peidi Dong, Yunze Xiao, Yu-Lin Tsai et al. — [Before You Continue: Evaluating Time-Sensitive Safety Awareness in Conversational Assistants](http://arxiv.org/abs/2611.06839v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) assistants increasingly help users with everyday activities that involve time-dependent constraints. However, users may not mention these constraints in later requests, requiring assistants to recognize and adjust their advice accordingly. To evaluate such capability, we introduce TASC (Temporal Action Safety in Conversation), a benchmark that evaluates whether LLMs apply time-dependent constraints when responding to conversational requests. TASC consists of 3,418 inpu...
  </details>

- **2026-11-04** — Man-Ling Sung, Hemanth Kandula, Jeff Ma et al. — [SAUCE: Summary Analysis Using Conversation Entailment](http://arxiv.org/abs/2611.06812v1)
  <details><summary>📄 Abstract</summary>
  With the growing need for evaluating Large Language Models (LLMs) and their applications to speech, challenges persist in summarizing and evaluating conversations that lack a clear end goal. We introduce SAUCE -- a reference-free, fact-based evaluation pipeline for cross-lingual conversational speech summarization. It measures the accuracy and the fact coverage of a summary through the entailment between conversation and text. We compare SAUCE against several popular summarization metrics and de...
  </details>

- **2026-11-04** — Sachin Gupta — [AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents](http://arxiv.org/abs/2611.06674v1)
  <details><summary>📄 Abstract</summary>
  Infrastructure security does not establish whether an LLM agent selected an allowed tool, grounded its answer in tool output, or followed a required workflow. AgentTrustCI is a Java/JUnit 5 framework that expresses these application-layer expectations as policy, grounding, and trajectory checks over recorded traces. A deterministic replay implementation supports repeatable build-time tests; a judge interface provides an extension point for optional semantic evaluation. On 55 synthetic cases span...
  </details>

- **2026-11-04** — Thomas Christian Joos, Azza Bouleimen, Anikó Hannák et al. — [Perceived Trust and Transparency in AI-Altered vs. Human-Written LinkedIn Posts](http://arxiv.org/abs/2611.06660v1)
  <details><summary>📄 Abstract</summary>
  People increasingly draft a social media post themselves and then let an AI model refine it (AI-altered), a common but understudied middle case between fully human-written and fully AI-generated content. We ask whether this changes how trustworthy and transparent readers perceive the post to be, and whether they can even tell. We first analyze real ChatGPT conversations (WildChat) to find how people actually alter social media posts, which we use to design realistic alteration prompts. We then r...
  </details>

- **2026-11-04** — Sourav Selvaraj, Juan Pablo Espinosa Chessal, Mahdi Agheli — [SCRUB: Contact-Based Surface-Frame Estimation for Force-Motion Control with an Armless Quadruped](http://arxiv.org/abs/2611.06649v1)
  <details><summary>📄 Abstract</summary>
  Wiping, sanding, and inspection robots press a sliding tool on a surface with controlled force. Controlling that force needs the surface normal, which is unknown on real-world, unmapped surfaces. Surface-normal estimators can help estimate the surface normal, but they either need a friction model or assume that the instantaneous tool velocity lies along the surface; however, walking violates this assumption. We propose SCRUB, a contact-based surface-frame estimator, which lets an armless quadrup...
  </details>

- **2026-11-04** — Yuetong Liu, Zhehao Zhou, Yitong Zhang et al. — [Tools Need Not Speak in Text: Latent Context Compression for Agents](http://arxiv.org/abs/2611.06500v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents typically append raw tool outputs to their context. Over multi-step interactions, long and noisy observations incur substantial context overhead and dilute the agent's attention to task-relevant information. Existing token pruning and summarization methods remain constrained by discrete text representations, limiting the achievable compression ratios.   In this work, we challenge the prevailing assumption that agents must consume tool observations as explicit te...
  </details>

- **2026-11-04** — Boyu Niu, Yingjie Xiong, Shurui Li et al. — [AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing](http://arxiv.org/abs/2611.06449v1)
  <details><summary>📄 Abstract</summary>
  Traditional document parsing systems use Markdown as their output representation, which is effective for linear text but does not fully preserve fine-grained spatial structure, table geometry, visual hierarchy, or rendering semantics. We show that HTML is advantageous for heterogeneous and layout-sensitive documents whose representations must remain editable, inspectable, and reusable, and introduce AmbiHTMLBench to systematically study this setting. In this benchmark, given a real-world documen...
  </details>

- **2026-11-04** — Zhuang Zhao, Jiongchi Yu, Yao Zhang et al. — [Keeping Fuzzers on Duty: Repairing Fuzzing Build Breakages in Continuous Open-Source Fuzzing](http://arxiv.org/abs/2611.06358v1)
  <details><summary>📄 Abstract</summary>
  Continuous fuzzing platforms such as OSS-Fuzz provide sustained security testing for open-source projects, but long-term build breakages reduce security coverage and waste infrastructure resources. In OSS-Fuzz, around 20% of integrated projects remain in build-failure states, leaving their fuzzers off duty. These failures expose a maintenance gap between platform maintainers, who lack project-specific context, and project maintainers, who often lack fuzzing and infrastructure expertise. Existing...
  </details>

- **2026-11-04** — Jinhua Wu, Yuting Wang, Zhemin Chen — [Verified Implementation of the Next-gen Borrow Checking Algorithm for Rust via Abstract Interpretation](http://arxiv.org/abs/2611.06319v1)
  <details><summary>📄 Abstract</summary>
  Borrow checking is a central mechanism for Rust to ensure temporal memory safety. Its correctness is based on the intuition that the Aliasing XOR Mutability discipline guarantees that programs without borrow errors inherently could not access invalid references (i.e., pointers). However, existing work on formalizing borrow checking treats it either as a component of type systems or as symbolic execution describing resource transfer. None provides a direct explanation of the correctness of borrow...
  </details>

- **2026-11-04** — Xin Liu, Hongru Song, Ruqing Zhang et al. — [CLEAR: Structured Specifications for Controllable Long-Horizon ML Research Engineering](http://arxiv.org/abs/2611.06263v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly being used to automate machine learning (ML) research workflows, ranging from code development and experiment execution to research reproduction and scientific discovery. Recent systems demonstrate that LLMs can perform substantial portions of ML research engineering with limited human intervention. These advances suggest a shift from automating individual research tasks toward automating long-horizon workflows that transform research artifacts ...
  </details>

- **2026-11-04** — Divyanshu Mishra, Sabine Sternig, Rakshith Shetty et al. — [Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization](http://arxiv.org/abs/2611.06149v1)
  <details><summary>📄 Abstract</summary>
  Video-LLMs are typically trained on paired video-text data for temporal tasks, yet collecting precise temporal annotations and training on large-scale video datasets are both costly. We investigate whether a text-only LLM, with no vision-language pretraining, can be trained on textual video descriptions alone to perform temporal grounding and receive video only at inference time. This setting removes paired video data from training altogether and is a step toward training multimodal models witho...
  </details>

- **2026-11-04** — Mingkang Liu, Peipei Jiao, Weiming Meng et al. — [UniCompress: From Multi-LoRA Experts to One Compact Model for Edge Intelligence](http://arxiv.org/abs/2611.06075v1)
  <details><summary>📄 Abstract</summary>
  Embodied and edge systems increasingly rely on vision-language models (VLMs) to support heterogeneous skills, yet deploying a separate task adapter for each skill while retaining a high-precision backbone creates substantial memory and management costs. We present UniCompress, a deployment-oriented framework that converts multi-task expertise into one compact, adapter-free model. Starting from a consolidated BF16 Qwen3-VL-4B teacher, UniCompress constructs an asymmetric INT2 student using GPTQ i...
  </details>

- **2026-11-04** — Shuo Liu, Hao Ning, Jacky Keung et al. — [SynMOE: A Syntax-Aware MOE-Guided Approach for PEFT-Based Code Intelligence Learning](http://arxiv.org/abs/2611.06069v1)
  <details><summary>📄 Abstract</summary>
  Parameter-Efficient Fine-Tuning (PEFT) has emerged as an important approach for adapting Language Models (LMs) in downstream tasks. However, in the domain of code intelligence, the performance of most PEFT methods relatively drops compared to Full fine-Tuning (FT), hindering their broader applicability. One of the main reasons is that current PEFT methods are generally based on assumptions about the low-rank nature or sparsity of parameter updates, lacking explicit modeling of code-related infor...
  </details>

- **2026-11-04** — Yuliang Liu, Xinyu Wang, Xiang Bai — [Familiar letters, not related languages, let unseen languages into a shared space of meaning](http://arxiv.org/abs/2611.06006v1)
  <details><summary>📄 Abstract</summary>
  Hundreds of languages have written text but almost no translations, and whether a model learning one from untranslated text builds on a related language or familiar letters is unclear: they usually coincide. Here we show that familiar letters, not a related language, let an unseen language into a shared space of meaning. GlyphMind, a tokenizer-free vision transformer that reads text as pixels and lets any sentence be shown in any script, was pretrained to align translations across 27 writing sys...
  </details>

- **2026-11-04** — Luyang Jiang, Chuheng Wei, Yaguang Li et al. — [InterSim: Innovative Intersection Digital Twins for Human-in-the-Loop Driving Simulation](http://arxiv.org/abs/2611.05968v1)
  <details><summary>📄 Abstract</summary>
  Innovative intersection designs can improve roadway safety and operational efficiency, but their uncommon geometries may create challenges for driver comprehension during early deployment. Evaluating these designs through full-scale field implementation can also be costly. This paper presents InterSim, a Unity game engine-based human-in-the-loop (HITL) driving simulator that constructs digital twins of site-specific innovative intersections in a virtual environment. InterSim links the real world...
  </details>

- **2026-11-04** — Keonhee Jang, Kanghoon Lee, Seokwoo Yun et al. — [Robots in the City: Persona-Based Perceptions of Urban Robots](http://arxiv.org/abs/2611.05954v1)
  <details><summary>📄 Abstract</summary>
  Pedestrians increasingly encounter robots in urban public spaces without interacting with them, but how robots change the perceived safety of a street remains unclear. We examine how robot presence and type affect perceived safety across urban contexts. We generate 18 images of Seoul streets that vary in time of day, road class, and robot condition (no robot, a delivery robot, or a humanoid). Two multimodal large language models (MLLMs), Qwen3.8-27B and Gemma4-26B, each conditioned on 500 synthe...
  </details>

- **2026-11-04** — Zehao Lin, Kai Chen, Xixuan Hao et al. — [When Does Better Confidence Improve a Knowledge-Graph Audit?](http://arxiv.org/abs/2611.05877v1)
  <details><summary>📄 Abstract</summary>
  Confidence estimates guide human review in LLM-built knowledge graphs, but better error prediction can yield little improvement in an audit. We study this gap through repairability, selection headroom and label validity. Modelling non-adaptive auditing as budgeted covering, we characterise the minimal decision-relevant error statistics and bound the regret of scalar-preserving first-order planning by a structural mass $Δ^{\mathrm{cl}}$. We simulate ideal repair against benchmark-aligned labels f...
  </details>

- **2026-11-04** — Yuqin Dai, Zhanwei Zhang, Honghui Yang et al. — [CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines](http://arxiv.org/abs/2611.05862v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) shopping assistants now recommend products in multi-turn conversations. However, reliable evaluation faces Data scarcity and Difficulty Standardizing Criteria. To address these obstacles, we introduce CARTBench for CART (Complex and Ambiguous Requests with Timelines). For Data scarcity, we curate cases from real commercial shopping needs across 17 retail domains, pairing timestamped dialogue with 1,603 product records. For Difficulty Standardizing Criteria, we develop ...
  </details>

- **2026-11-04** — Vadim Gorin, Lingfu Zhang — [Gaussian free field limit for the Airy$_β$ line ensemble](http://arxiv.org/abs/2611.05852v1)
  <details><summary>📄 Abstract</summary>
  We prove that the centered height function of the Airy$_β$ line ensemble converges for each $β>0$, under rescaling of space and time variables, towards the Gaussian free field in the half-plane. The conformal structure for GFF involves the spatial change of coordinate $x\mapsto \sqrt{-x}$. The $β$--dependence is isolated in the field rescaling by $\sqrtβ$. For the proofs we study the asymptotic expansions of the moments of Laplace transforms of the Airy$_β$ line ensemble developed in our previou...
  </details>

- **2026-11-04** — Yuning Chen, Hongda Zhang, Linqiang Hu et al. — [Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework](http://arxiv.org/abs/2611.05828v1)
  <details><summary>📄 Abstract</summary>
  Intelligent production requires systems to make decisions and organize work according to production goals and operating conditions. It also requires continuous adjustment through feedback. This paper analyzes intelligence in human production organizations from a complex adaptive systems (CAS) perspective. The analysis identifies two coupled mechanisms: individual autonomy and collective coordination. Individual autonomy enables actors to form local decisions using available information. Collecti...
  </details>

- **2026-11-04** — Mohan Cao, Yongsen Mao, Chucheng Xiang et al. — [GREP: Grounding Generated Room Evaluation in Principles](http://arxiv.org/abs/2611.05802v1)
  <details><summary>📄 Abstract</summary>
  Recent LLM-centric advances can generate attractive furnished rooms by selecting and arranging assets. Yet evaluation remains limited to specific perspectives or predefined questions, failing to reflect overall scene quality. To address this pressing need, we introduce GREP. Its core is a focus shift from defining specific questions to establishing a three-tier evaluation philosophy: basic physical validity checks whether a scene obeys physical constraints; visual coherence concerns compatibilit...
  </details>

- **2026-11-04** — Jikwang Lee, Seungwook Jung, Jaechang Nam — [DARE: Difficulty Analysis for Repair Enhancement](http://arxiv.org/abs/2611.05797v1)
  <details><summary>📄 Abstract</summary>
  LLM-based coding agents are primarily evaluated by their solve rates. However, this metric does not reveal how difficult the solved tasks are or account for differences intask difficulty across benchmarks. Determining the difficulty of individual tasks by repeatedly running multiple agents is costly, while a predicted difficulty score alone provides limited guidance on what support an agent needs. To address these challenges, we propose DARE (Difficulty Analysis for Repair Enhancement), which in...
  </details>

- **2026-11-04** — Shuangyu Xie, Kaiyuan Chen, Uksang Yoo et al. — [VABAR: A Variational Automation Benchmark for Agentic Robotics](http://arxiv.org/abs/2611.06881v1)
  <details><summary>📄 Abstract</summary>
  For robots to operate reliably in commercial and industrial applications, they must persistently perform specific tasks with known variations in object shape and pose. We call this Variational Automation (VA) to differentiate these settings from fixed automation. Inspired by recent papers on Agentic Robotics, where pretrained LLM and VLM coding agents combine interpretable robot programming with the open-world adaptability of model free policies, we propose a general set of agentic robotics benc...
  </details>

- **2026-11-04** — Siddharth Aphale, Ayushman Singh — [Rethinking Self-Repair in Code-as-Policy Agents: What Drives Retry Success?](http://arxiv.org/abs/2611.06863v1)
  <details><summary>📄 Abstract</summary>
  Code-as-policy agents often use execution feedback to retry failed programs. Additional sampling and task guidance can also improve success, leaving the contribution of failure-specific feedback unclear. We study this question in simulated robot manipulation. A fixed lookup selects feedback templates using failure labels and the API variant. A frozen code model generates a fresh program after each scene reset. On the same 252 initial failures, Qwen2.5-Coder-7B recovers 85.3% within five retries,...
  </details>

- **2026-11-04** —  NVIDIA,  :, Anis Ahmad et al. — [Interactive World Simulation with Cosmos for Physical AI](http://arxiv.org/abs/2611.06627v1)
  <details><summary>📄 Abstract</summary>
  We present a shared framework that adapts Cosmos world foundation models for real-time interactive world simulation in Physical AI. By streaming visual observations in response to actions and scene controls, the framework enables users and embodied agents to interact with evolving virtual environments. It supports both predicting the visual consequences of actions and generating observations from physical state maintained by an external simulator. We demonstrate this approach across camera navig...
  </details>

- **2026-11-04** — Sihang Chen, Chen Ye, Wei Chen et al. — [Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation](http://arxiv.org/abs/2611.06475v1)
  <details><summary>📄 Abstract</summary>
  In the real world, mobile manipulation robots must perform complex object interactions and make multi-step decisions, often relying on task-relevant information that is no longer observable. However, existing benchmarks provide limited evaluation of such memory-dependent decision-making in mobile manipulation. To address this gap, we introduce RoboCasa-Mem, a new benchmark comprising nine mobile manipulation tasks that require agents to use interaction history at key decision points. Specificall...
  </details>

- **2026-11-04** — Bingao Chen, Haoquan Fang, C. Karen Liu — [Can Astra Solve RoboMME without Breaking the Bank?](http://arxiv.org/abs/2611.06184v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation often requires remembering information that is no longer visible, such as an object's location before occlusion or the order of a demonstrated action sequence. A large vision-language planner can read this history, but calling it before every action chunk is slow and costly. We present a three-tier system for the RoboMME benchmark. GPT-6 Astra (System 2) selects a grounded subtask from stored visual history, a $π_{0.5}$ vision-language-action policy (System 1) executes it, a...
  </details>

- **2026-11-04** — Xiaozhe Ji, Renfen Hu, Hai Hu — [Phonological Knowledge of Chinese Characters in Language Models](http://arxiv.org/abs/2611.05803v1)
  <details><summary>📄 Abstract</summary>
  How much phonological knowledge do language models (LMs) possess about Chinese characters, and how is this knowledge represented and used? We introduce PinyinBench, a controlled benchmark covering homophones, phonological features (initials, finals, and tones), and polyphonic characters. We investigate 17 text-only and multimodal LMs through three complementary approaches: behavioral evaluation, layer-wise probing, and activation steering. Behaviorally, models demonstrate substantial knowledge o...
  </details>

- **2026-11-04** — Siyi Yu — [Dull, Dirty, Dangerous? Working Conditions and the Limits of Occupational AI Exposure](http://arxiv.org/abs/2611.06888v1)
  <details><summary>📄 Abstract</summary>
  Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using 21 O*NET items across 754 US occupations. Higher exposure is associated with lower condition scores under a large language model (LLM) measure and AI Occupational Exposure (AIOE), with equal occupation weights and employment weights. Adjustment for physical demands, required education, training and experience, and wages reduces the composite associ...
  </details>

- **2026-11-04** — Yingying Yan, Jiaqi Tang, Wei Wei et al. — [Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers](http://arxiv.org/abs/2611.06844v1)
  <details><summary>📄 Abstract</summary>
  A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise semantics of a large language model. Mainstream MLLMs inject a fixed single-layer visual representation into the LLM and treat all LLM layers as a single consumer, ignoring that different layers demand different visual granularities. Recent multi-layer fusion methods either compress hierarchical featu...
  </details>

- **2026-11-04** — Xinrui Zhong, Zhiming Wang, Yongqi Liu et al. — [ServerBench: How can your coding agents design specialized LLM serving systems?](http://arxiv.org/abs/2611.06841v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective serving requires coordinating implementation and operating decisions under session dependencies, latency constraints, and correctness requirements. We introduce ServerBench, a benchmark for agentic design of complete, specialized LLM serving systems. Agents experiment against a common objective, dollars per dollar: late...
  </details>

- **2026-11-04** — Harsidak Singh Banwait — [Transforming Integer Grids to Spatial Intuition: Perception, Not Planning, Governs ARC-AGI-3](http://arxiv.org/abs/2611.06793v1)
  <details><summary>📄 Abstract</summary>
  Sample-efficient fluid intelligence requires agents that rapidly form working models of unfamiliar interactive environments. ARC-AGI-3 tests this across uninstructed visual games scored by Relative Human Action Efficiency, which penalizes exploratory waste quadratically. When frontier models read raw integer grids, serialization destroys spatial topology, and they spend hundreds of actions rediscovering basic boundaries and symmetries. We introduce SARBLOH, an open-weight agent built on the prem...
  </details>

- **2026-11-04** — Ekaterina Fadeeva, Xueyan Li, Mrinmaya Sachan et al. — [Verifier-Guided Self-Consistency: Test-Time Reasoning with Imperfect Generators and Verifiers](http://arxiv.org/abs/2611.06606v1)
  <details><summary>📄 Abstract</summary>
  Large language models can solve many multi-step reasoning problems, but their reasoning remains brittle: plausible intermediate steps often lead to incorrect answers. Improving reasoning at test time requires balancing two imperfect signals: the generator, which provides diversity, and the verifier, which guides correctness. Existing approaches largely favor one side of this tradeoff. Verifier-weighted voting relies on trajectories sampled from the generator and cannot steer generation toward co...
  </details>

- **2026-11-04** — Qian Liu, Shinuo Ma, Yixin Tao et al. — [Competitive Equilibrium for Linear Chores is CLS-complete](http://arxiv.org/abs/2611.06589v1)
  <details><summary>📄 Abstract</summary>
  The competitive equilibrium (CE) is a fundamental concept for markets, with applications to efficient and fair allocation of resources. We consider the fundamental question of computing a CE in the most basic Fisher market model where agents have linear preferences. While it is known that we can compute a CE in strongly polynomial time with linear goods, there is no known polynomial-time algorithm for CE with linear chores. Computing a CE for linear chores is known to be in CLS with no hardness ...
  </details>

- **2026-11-04** — Shreya K. Chari, John S. Vardakas, Kostas Ramantas et al. — [RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management](http://arxiv.org/abs/2611.06554v1)
  <details><summary>📄 Abstract</summary>
  Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid framework that combines the capabilities of RL algorithms and Generative-AI (Gen-AI) for powering an Agentic AI workflow that optimizes resource allocation at the Multi-access Edge Computing (MEC) units. This framework furt...
  </details>

- **2026-11-04** — Christian Pipal, Morgan Wack, Eva-Maria Vogel — [Who Gets Counted? Large Language Models, Informative Refusal, and Downstream Bias in Name-Based Demographic Classification](http://arxiv.org/abs/2611.06550v1)
  <details><summary>📄 Abstract</summary>
  Researchers routinely infer gender, race, and ethnicity from names, yet the standard tools used for this task misclassify the groups that diversity research most needs to measure. Large language models (LLMs) have been proposed as a remedy because they label diverse names accurately. We ask whether that accuracy carries over to the estimates researchers report. Across 10,000 Chinese names, 19,998 North Carolina voters with self-reported race, and 300 political science authors with human referenc...
  </details>

- **2026-11-04** — Zhihao Nan, Sifan Zhou, Yiming Cheng et al. — [MKD2World: A Typed Spatial MarkDown World Model For Web Agents](http://arxiv.org/abs/2611.06544v1)
  <details><summary>📄 Abstract</summary>
  Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces. Existing state representations fail to jointly capture interface layout, UI semantics, and explicit locations. We introduce Typed Spatial Markdown (TSM), a Markdown-style textual state representation for desktop web interfaces. TSM serializes block-level and atomic-level UI elements according to their spatial relationships, jointl...
  </details>

- **2026-11-04** — Etuh E., Eli. A. Jiya — [Dialect Matters: A Dialect-Aware Baseline for Igala-English Machine Translation](http://arxiv.org/abs/2611.06517v1)
  <details><summary>📄 Abstract</summary>
  The massive permeability of intelligent systems in every sphere of human activities have greatly enhanced clarity, ease of work, and increased general global understanding which has significantly awaken the use of intelligent systems by all users. Intelligent systems greatly rely on precise dataset/corpus for the correctness of their output. Despite efforts by researchers to address Low-resource language in the Natural Language Processing (NLP), Igala still has zero parallel corpora despite effo...
  </details>

- **2026-11-04** — Yulu Xie, Zilong Li, Shen Xu et al. — [A 3D foundation model unifying CT interpretation and segmentation](http://arxiv.org/abs/2611.06471v1)
  <details><summary>📄 Abstract</summary>
  Radiologists interpret computed tomography (CT) scans by jointly determining what a finding represents and where it lies in three-dimensional (3D) anatomy. However, CT models have treated CT interpretation and 3D segmentation as separate tasks, leaving textual findings spatially unverifiable and overlooking potential synergy between clinical understanding and spatial perception. Here we present HoloCT, a generalist 3D foundation model unifying CT interpretation and voxel-level segmentation by jo...
  </details>

- **2026-11-04** — Faezeh Fadaei, Jenny Carla Moran, Taha Yasseri — [A Cracked Mirror: How People Perceive Gender Performance by Large Language Models](http://arxiv.org/abs/2611.06393v1)
  <details><summary>📄 Abstract</summary>
  How do large language models (LLMs) perform gender under zero-shot prompting, and how do people interpret those performances in conversation? Drawing on gender performativity, we examine how gendered meanings emerge through generated language, conversational context and human interpretation. In a preregistered randomised online experiment, 1,060 participants each had five short conversations with an LLM. We used minimal prompts to elicit performances from "very masculine" to "very feminine" and ...
  </details>

- **2026-11-04** — Xiaoyu Zhang, Yougang Lyu, Bin Wu et al. — [PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries](http://arxiv.org/abs/2611.06349v1)
  <details><summary>📄 Abstract</summary>
  On Web platforms for shopping and entertainment, recommendation agents under multimodal queries aim to deliver personalized recommendations that satisfy users' visually specified requirements and reflect preferences inferred from user histories. However, existing personalized recommendation benchmarks use text-only queries, while multimodal ones assess query matching without evaluating personalization based on real user histories. We introduce the Personalized Multimodal Recommendation Benchmark...
  </details>

- **2026-11-04** — Dohyun Kim, Junyong Lhim, Kwanyong Park — [A Systematic Benchmark for Evaluating Multimodal Personalized Reasoning of Vision-Language Models](http://arxiv.org/abs/2611.06259v1)
  <details><summary>📄 Abstract</summary>
  People often make decisions by holistically reasoning over heterogeneous forms of personal information. In this paper, we study the relatively underexplored capability of multimodal personalized reasoning in multimodal large language models (MLLMs). To this end, we introduce \texttt{MPRBench}, a novel and comprehensive benchmark specifically designed to evaluate personalized reasoning across a wide range of tasks and real-world challenges. \texttt{MPRBench} consists of 12 sub-tasks and additiona...
  </details>

- **2026-11-04** — Federico Celi, Leonardo Zacchini, Gabriele Ferri — [A Layered View of LLM Support in Underwater Robotics](http://arxiv.org/abs/2611.06162v1)
  <details><summary>📄 Abstract</summary>
  This extended abstract discusses a specific and, in our experience, practically relevant role for large language models (LLMs) in underwater robotics. Our main premise is that, in underwater fielding missions, the immediate difficulty is often not the synthesis of new low-level control laws, but the operation of complex robotic systems under limited communications, partial observability, and expensive field time. In particular, a significant fraction of the effort during sea trials is devoted to...
  </details>

- **2026-11-04** — Sicen Guo, Zhengfei Song, Kuanhsun Chen et al. — [DSRS: Teaching MLLMs to Perceive, Reason, and Segment in Complex Driving Scenes](http://arxiv.org/abs/2611.06160v1)
  <details><summary>📄 Abstract</summary>
  Existing reasoning segmentation frameworks typically employ multimodal large language models (MLLMs) with broad world knowledge to extract semantics in a human-like manner and generate corresponding segmentation masks. Nevertheless, these frameworks lack the necessary scene-specific awareness. This paper introduces driving scene reasoning segmentation (DSRS), a scene-specific task that requires models to interpret implicit instructions, infer spatial relations, detect potential risks, handle cha...
  </details>

- **2026-11-04** — Niccolò Niccoli, Silvia Dani, Marco Mistretta et al. — [GeoBiaset: A Counterfactual Benchmark for Demographic Bias in World-Level Geolocalization](http://arxiv.org/abs/2611.06085v1)
  <details><summary>📄 Abstract</summary>
  World-level image geolocalization is an increasingly important task, yet the biases of current models remain poorly understood. Prior work has identified coarse dataset imbalances noting, for instance, that some cities are absent from training sets and that models tend to perform better in wealthier regions. However, no one has yet examined which visual cues drive these disparities. To do so, we introduce GeoBiaset, the first benchmark designed to measure how geolocalization models are influence...
  </details>

- **2026-11-04** — Dongjin Lee, Eunju Lee, Jinhee Jang et al. — [RI-Prune: Relation and Information Aware Visual Token Pruning for Multi-Image Vision-Language Models](http://arxiv.org/abs/2611.06047v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have recently been extended to handle multiple input images, but this extension dramatically increases the visual token budget, making visual-token pruning not merely an efficiency option but a practical necessity. Existing visual-token pruning methods, primarily designed for the single-image setting, rely on attention-derived saliency signals to estimate per-token importance. However, this attention-centric design transfers poorly to the multi-image regime: ...
  </details>

- **2026-11-04** — Jiamu Wang, Keunho Byeon, Ji-Uk Kim et al. — [PathoS2VD: From 2D Histopathology to Pseudo Z-Stack Representations](http://arxiv.org/abs/2611.05974v1)
  <details><summary>📄 Abstract</summary>
  For decades, diagnostic pathology has relied on thin two-dimensional (2D) tissue sections, despite biological tissues exhibiting inherently three-dimensional (3D) morphological organization. Because a single section captures only one focal plane, important morphological cues along the z-axis are inevitably discarded, limiting tissue representation for both human interpretation and computational analysis. In this work, we propose a generative framework that learns z-axis morphological priors from...
  </details>

- **2026-11-04** — Mengni Jia, Mengyu Zhou, Xiaoxi Jiang et al. — [Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning](http://arxiv.org/abs/2611.05942v1)
  <details><summary>📄 Abstract</summary>
  RL for LLM reasoning often reaches an early performance plateau as the policy distribution becomes increasingly sharp. Recent work has studied policy entropy as both a diagnostic and a control signal for this behavior. In our experiments, however, increasing entropy alone does not reliably change the eventual plateau. We analyze RL through its implicit target policy and derive a sharpness factor $κ$, together with an effective counterpart $κ_{\mathrm{eff}}$, that describes how strongly reward or...
  </details>

- **2026-11-04** — Yoon Pyo Lee, Samrendra Roy, Jay Phil Yoo et al. — [Autonomous agents for electricity-system planning](http://arxiv.org/abs/2611.05911v1)
  <details><summary>📄 Abstract</summary>
  Planning electricity systems requires repeated decisions that connect regional resources, investment, operation and network constraints. Here we present an autonomous planning framework that carries prepared regional scenarios through proposal, numerical evaluation, feedback interpretation, redesign and final plan selection. Agents propose investment bounds, storage operating conditions and feeder interventions, interpret numerical feedback, and decide how to revise designs and when to stop. The...
  </details>

- **2026-11-04** — Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao et al. — [CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating](http://arxiv.org/abs/2611.05890v1)
  <details><summary>📄 Abstract</summary>
  Biological discovery requires using molecular knowledge and new measurements to infer responses beyond the conditions already observed. We introduce CellCanon, the first agentic cellular world model to unify single-cell expression prediction, evidence-grounded explanation, and observation-driven updating. Its predictive core reuses condition-level biological evidence across gene-specific numerical readouts to guide single-cell expression generation. A shared world state links predictions, acquir...
  </details>

- **2026-11-04** — Furong Li, Wei Liu, Yali Shao et al. — [A Laplace-Transform Green's Function for Two-Zone Diffusion with Energy Losses: Application to the Geminga Pulsar Halo](http://arxiv.org/abs/2611.05808v1)
  <details><summary>📄 Abstract</summary>
  Extended TeV gamma-ray halos around pulsars are commonly interpreted as evidence for slow diffusion of high-energy electrons and positrons near their sources, with diffusion coefficients about two orders of magnitude below the Galactic average inferred from B/C measurements. A two-zone diffusion picture offers a natural phenomenological resolution: particles are temporarily confined in a slow-diffusion region around the source and subsequently propagate through the outer region with a diffusion ...
  </details>

- **2026-11-04** — Won-Ki Seo, Jiazhen Xu, Han Lin Shang — [Local Whittle estimation for distributional time series: A regularization framework in Bayes Hilbert space](http://arxiv.org/abs/2611.05765v1)
  <details><summary>📄 Abstract</summary>
  We study local Whittle estimation of long memory in density-valued time series in Bayes Hilbert space. The centered log-ratio (clr) transformation maps densities to a linear Hilbert space, allowing analysis using standard Hilbert space methods. When densities are reconstructed from finite samples, however, small absolute estimation errors can remain large relative to the true density in low-density tails. Taking logarithms can amplify this noise and introduce systematic distortions that affect m...
  </details>

- **2026-11-03** — Rudrajit Choudhuri, Christian Bird, Carmen Badea et al. — [TACT: A Pragmatic Approach to Qualitative Analysis with an AI Council](http://arxiv.org/abs/2611.05702v1)
  <details><summary>📄 Abstract</summary>
  Qualitative data can tell software teams what their stakeholders need, yet rigorously analyzing thousands of qualitative responses takes expert time that few teams can afford or justify. Teams therefore often face a false choice: leave the responses unanalyzed, or hand them to a large language model and accept its interpretation and judgment. In this paper, we take a pragmatic approach to AI-assisted qualitative analysis and present TACT (Traceable AI Council for Thematic analysis), a procedure ...
  </details>

- **2026-11-03** — Giannis Fikioris, Balasubramanian Sivan, Éva Tardos — [Learning vs. Optimizing Players in Budgeted Games](http://arxiv.org/abs/2611.05580v1)
  <details><summary>📄 Abstract</summary>
  We study repeated general games over $T$ rounds between a utility-maximizing optimizer and a learning agent, where budget constraints couple the players' decisions across rounds. Without budgets, low swap regret simultaneously guarantees the learner sublinear regret and caps the optimizer at its Stackelberg value. Budgets break this picture: adversarial no-regret becomes impossible, so the natural goals are non-manipulability---no adaptive optimizer earns more than $\mathtt{BSE} \cdot T + o(T)$,...
  </details>

- **2026-11-03** — Aditya Gupta, Jean Sebastien Dandurand, Kai Qiu et al. — [Learning Hierarchical Patch Splitting Policies for Faster Vision Transformers](http://arxiv.org/abs/2611.05742v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers (ViTs) are bottlenecked by the length of their input token sequence. Standard patchification fixes this length with a single patch size applied across the image, regardless of regional content. Prior work on adaptive patch sizing reduces token count by assigning coarser patches to visually simple regions, but relies on noisy pixel-level heuristics such as local entropy to make patchification decisions. We argue that this compute allocation should be grounded in the model's in...
  </details>

- **2026-11-03** — Ankana Banerjee, Mark van der Giezen, Ole Gunnar Aasprong et al. — [Multimodal Fusion Methods for Whole-Slide Images and Clinical Data in Inflammatory Bowel Disease](http://arxiv.org/abs/2611.05579v1)
  <details><summary>📄 Abstract</summary>
  Multimodal AI fusion of histology and clinical data is an active research area in computational pathology, but fusion methods are rarely compared under identical conditions and across different clinical endpoints. We present a modular framework in which slide-level embeddings, obtained by training an attention-based aggregator over patch embeddings from a frozen foundation model, and per-visit clinical embeddings are fed into 15 interchangeable fusion methods with a shared output dimension and p...
  </details>

- **2026-11-03** — Albert Wilcox, Frank Chang, Nhi Nguyen et al. — [MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](http://arxiv.org/abs/2611.05567v1)
  <details><summary>📄 Abstract</summary>
  Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and saturated, offering little signal on SOTA methods, broadly scoped, providing diversity at the cost of controlled experimentation, or require training on large, messy open-source datasets. We introduce MESA, an evaluation framework designed for precise, reproducible measurement of language-conditioned policy generalization. ...
  </details>

- **2026-11-03** — Jorge Ramón Fonseca Cacho — [Rewrite, Then Veto: Rewriter-Agnostic Edit Gating for LLM-Based Post-OCR Correction](http://arxiv.org/abs/2611.05539v1)
  <details><summary>📄 Abstract</summary>
  LLMs can repair noisy OCR transcripts of historical documents, but they also change text that was already correct. We propose EditVeto, a veto gate placed after a full-context LLM rewrite. The rewrite is character-aligned to the OCR input, its differences are split into blocks, and a 0.6B-parameter gate keeps or reverts each block. An oracle analysis motivates the design: given the true error locations, per-span generation is worse than no correction, whereas vetoing a full rewrite's edits helps...
  </details>

- **2026-11-03** — Ivan Martinez-Kay, Tatiana Kardashina, ShiNung Ching et al. — [A Bayesian Optimized Biquad Filter-Burg Model for Real-Time EEG Phase Estimation](http://arxiv.org/abs/2611.05374v2)
  <details><summary>📄 Abstract</summary>
  Real-time phase estimation on stimulus-aligned transient EEG is critical for closed-loop neuromodulation systems targeting the theta-band, yet most real-time phase estimation methods have been developed and validated on resting-state, high-fidelity signals in the alpha band. Recent work has pursued deep learning architectures, while individualized classical bandpass filter tuning remains underexplored. This study characterizes the spectral and temporal properties of non-anticipative bandpass fil...
  </details>

- **2026-11-03** — Zimeng Wang, Jinrong Yang, Rong Chen — [UMLoad: Fast On-Demand Model Loading on Unified Memory Architecture](http://arxiv.org/abs/2611.04253v2)
  <details><summary>📄 Abstract</summary>
  On-demand model loading dominates response latency for interactive on-device AI, yet unified memory architectures (UMAs), now common on edge devices, should make it cheap by placing weights in memory the GPU already sees. However, frameworks still use the loading flow built for discrete GPUs, leaving significant inefficiencies. This paper presents UMLoad, a system-level model-loading accelerator that decouples a framework's logical allocations from their physical page backing. UMLoad uses on-dem...
  </details>

- **2026-11-03** — Seungyong Lee, Suhyeok Jang, Minyoung Kim et al. — [RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](http://arxiv.org/abs/2611.05163v2)
  <details><summary>📄 Abstract</summary>
  Robot foundation models have shown remarkable performance in robot control, yet adapting them to a new task still relies heavily on teleoperated demonstrations. Egocentric human videos offer a scalable substitute, but overlaying rendered robots on human videos or retargeting human poses into robot actions leaves significant visual or action gaps for high-DoF robot embodiments. To address this limitation, we propose RoboTryOn, which treats human-to-robot translation as virtual try-on: try-on keep...
  </details>

- **2026-11-03** — Andrew Miracle, Phyl Georgiou, Christine Okoth et al. — [Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex](http://arxiv.org/abs/2611.05753v1)
  <details><summary>📄 Abstract</summary>
  Organizations accumulate evidence in conversations, documents, decisions and relationships, but they act on interpretations: judgements assembled from several observations, resting on assumptions, and revised as circumstances change. Existing retrieval, knowledge graphs and agent memory keep the records and lose the interpretation. We propose a four-layer architecture, Signals, Domains, Claims and Dimensions, in which interpretations persist with their justifications and standing, a truth-mainte...
  </details>

- **2026-11-03** — Douglas Guilbeault, Bhargav Srinivasa Desikan — [The Male Abstraction Bias in Internet Culture and Large Language Models](http://arxiv.org/abs/2611.05730v1)
  <details><summary>📄 Abstract</summary>
  Two foundational aspects of human cognition, abstractness and gender, are typically examined as separable. Here, we find they are systematically linked throughout the entire space of concepts spanning single (N = 40,000) and multi-word expressions (N = 67,000): across billions of words and millions of images on the internet -- and across numerous measurement techniques -- more abstract concepts are more associated with men, an effect which replicates in languages around the world. This pattern n...
  </details>

- **2026-11-03** — Yanru Xiao, Yingwei Yu — [Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis](http://arxiv.org/abs/2611.05720v1)
  <details><summary>📄 Abstract</summary>
  Search can help LLM agents correct mistakes, but their starting conditions may shape which evidence they find and use. Drawing on cognitive-bias paradigms, we develop a controlled search harness to examine result order, records of prior work, and initial hypotheses while holding each question and document collection fixed. Matched controls distinguish order effects from differences in document composition and the effects of failed work from context length. Across 10 models and 1,000 synthetic se...
  </details>

- **2026-11-03** — Alexander Berndt, Paul Ralph, Thomas Bach et al. — [Construct Validity of Coding Benchmarks for LLM-based Agentic Coding Tools](http://arxiv.org/abs/2611.05665v1)
  <details><summary>📄 Abstract</summary>
  Software developers increasingly adopt LLM-based agentic coding tools to assist them with development tasks. To provide developers with up-to-date information on these tools' effectiveness, prior work introduced benchmarks that enable comparisons across tools. Despite the widespread adoption of such benchmarks, however, recent work has shown that they suffer from issues threatening their validity. Aims. In this work, we aim to complement prior work by analyzing the construct validity of agentic ...
  </details>

- **2026-11-03** — Alexandra Suvorikova, Ilgam Latypov, Anton Trukhan et al. — [When Are Two SAE Latents the Same Feature?](http://arxiv.org/abs/2611.05655v1)
  <details><summary>📄 Abstract</summary>
  Comparing sparse autoencoders (SAEs) requires connecting feature correspondence, differences between whole dictionaries, and uncertainty from finite evaluation data. We develop a framework that connects these tasks through an energy-weighted optimal-transport plan under a specified similarity geometry. The same plan defines a dictionary-level discrepancy, decomposes it into latent contributions, and quantifies how each latent's mass is distributed across counterparts. We characterize relationshi...
  </details>

- **2026-11-03** — Zeyu Fang, Jun Yin, Yongsheng Mei et al. — [Route to Remember: Adaptive Memory Selection for LLM Agents](http://arxiv.org/abs/2611.05636v1)
  <details><summary>📄 Abstract</summary>
  The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time. Therefore, every new query incurs an additional cost that grows with the accumulated history. Weight memory is a complementary alternative that internalizes knowledge into model parameters and answers with no context at all, and has recently proven effective in self-evolving agents for interna...
  </details>

- **2026-11-03** — Pengze Li, Jingna Feng, Yue Yu et al. — [VirtualTrialHarness: Coordinating Agentic Operationalization of Virtual Trial Protocols Across Complex Clinical Schemas](http://arxiv.org/abs/2611.05551v1)
  <details><summary>📄 Abstract</summary>
  Virtual trials use routinely collected clinical data to evaluate treatment strategies, but translating a study protocol into an executable analysis requires determining how clinical concepts and study requirements should be represented in the available data and applied consistently across the workflow. These decisions depend on local data representations and operational conventions and can involve source selection, patient and encounter identity, linkage, and temporal interpretation. Here we int...
  </details>

- **2026-11-03** — Xin Zhou, Elena Sergeeva, Nan Bi et al. — [Recasting Visual Language Models as EEG Foundation Models for Clinical Neurodiagnostics](http://arxiv.org/abs/2611.05538v1)
  <details><summary>📄 Abstract</summary>
  Historically automated electroencephalography (EEG) systems was done using task-specific supervised models trained on purposely annotated data. A more recent modeling paradigm relies on creating a unified representation, or a 'foundation model', for multiple modality-specific tasks through large-scale domain-specific pretraining on the unannotated EEG signal. The quality of this unified representation directly depends on the availability of the modality-specific datasets. At the same time, gener...
  </details>

- **2026-11-03** — Henning Bahl, Marco Menen, Antoine Petitjean et al. — [Top Spin and CP from Equivariant Transformers](http://arxiv.org/abs/2611.05463v1)
  <details><summary>📄 Abstract</summary>
  Measurements of spin correlations and CP are an exciting and challenging part of the precision-LHC program. We first show how L-GATr-slim, as a Lorentz-equivariant transformer, significantly boosts the spin analyzing power for hadronic top quarks. We then show how adding a pseudoscalar channel to its architecture allows us to learn and interpret optimal observables and their CP properties. We demonstrate this for WBF-Higgs production at parton level and top pair production including detector eff...
  </details>

- **2026-11-03** — Teerawat Tongloy, Jiraporn Pongsopa, Rangsan Jomtarak — [Reading Why: Born-Measured Attention with Exact Word Evidence on Light and Qubits](http://arxiv.org/abs/2611.05355v2)
  <details><summary>📄 Abstract</summary>
  When a language model answers, we can usually only estimate why. We build a transformer in which every step is a Born measurement - attention $|\langle q|k\rangle|^4$ normalised over each row, a measured product in place of the feed-forward nonlinearity, and a Born readout. With its denominators held at their values for the input, each class probability is a polynomial in the word amplitudes, so its integrated-gradient evidence is computed by a finite quadrature with no quadrature error: the wor...
  </details>

- **2026-11-03** — Shu Zhou, Ziyang He, Yuxin Rao et al. — [AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](http://arxiv.org/abs/2611.04813v2)
  <details><summary>📄 Abstract</summary>
  Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding from correctness. To bridge this gap, we introduce $\textbf{AgenticFinBench}$, a benchmark of 230 real-world financial tasks spanning 8 categories, 2 languages, and 4 complexity levels. We also propose a reference-free ...
  </details>

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

- **2026-11-02** — Dilan Mian, Jeremy Bradbury, Yann-Gaël Guéhéneuc et al. — [LLM-based NPCs in Video Games: A Systematic Mapping Study](http://arxiv.org/abs/2611.05427v1)
  <details><summary>📄 Abstract</summary>
  For decades, non-player characters (NPCs) have been driven by rule-based systems whose personalities and interactions are scripted before release. Large language models (LLMs) promise NPCs that converse openly, adapt to new situations, and behave in ways developers did not fully author, prompting a wave of research and commercial experimentation. Yet the field lacks a unified picture of what has been built, how well it works, and at what cost. We address this gap with a systematic mapping study ...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 713 |
| prompt-injection | 663 |
| memory-poisoning | 57 |
| tool-use-attack | 172 |
| backdoor | 548 |
| adversarial-attack | 664 |
| privacy-leakage | 4538 |
| steganography | 90 |
| misuse | 1289 |
| red-teaming | 146 |
| vulnerability | 3896 |
| defense | 3791 |
| alignment | 3556 |
| robustness | 3863 |
| watermark | 712 |
| unlearning | 119 |
| agent-safety | 67 |
| benchmark | 73 |
| survey | 442 |
| other | 10548 |

---

📚 **全部 35947 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-05 23:10:49*