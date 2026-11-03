<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-35531-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-11-03 22:47 ｜ **论文总数 / Total Papers**: 35531（近 30 天 / Recent 30 days: 4506）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 35531 篇论文（含摘要、分类筛选、搜索）/ View all 35531 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 705
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 657
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 57
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 169
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 548
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 660
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4513
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 90
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1279
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 145
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3856
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3747
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3518
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3821
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 695
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 119
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 66
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 73
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 436
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 10377

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4506 篇，完整 35531 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4506 papers from the last 30 days (with date, authors & abstract). For the full list of 35531 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 4 papers

- **2026-11-02** — Wei-Lin Chen, Zhepei Wei, Xinyu Zhu et al. — [VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](http://arxiv.org/abs/2611.03575v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated files, weakening access controls, or corrupting data, in response to benign inputs without explicit jailbreaking. This failure mode is particularly important because apparent task success may reassure users that an agent...
  </details>

- **2026-11-02** — Junyu Lin, Mengjie Wu, Yonghao Dong et al. — [PGuard: A Native, Streaming, and Plug-in Guardrail for Multimodal Large Language Models](http://arxiv.org/abs/2611.02791v1)
  <details><summary>📄 Abstract</summary>
  As streaming generation becomes the dominant serving paradigm for both text-only and multimodal large language models, ensuring safety throughout the generation process has become a critical challenge. We introduce PGuard, a native, streaming, and plug-in guardrail that transforms safety monitoring from an external serving dependency into an integrated capability of the backbone model. PGuard directly leverages the backbone's intermediate representations for token-level safety detection, without...
  </details>

- **2026-10-31** — Running Yang, Beidi Zhao, Xiaoxiao Li — [J-Anchor: Defending Against Prefill Attacks via J-Space Selective Refusal Restoration](http://arxiv.org/abs/2611.01342v1)
  <details><summary>📄 Abstract</summary>
  Prefill jailbreaks can cause safety-aligned language models to continue an unsafe assistant prefix even when they would refuse the same request under normal decoding. We study how the model's internal harmfulness and refusal signals evolve along this attacker-controlled trajectory. Using the Jacobian lens, we track vocabulary-grounded harmfulness and refusal signals from the assistant header through prefilling and subsequent generation. We identify a characteristic phenomenon, which we call refu...
  </details>

- **2026-10-29** — Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman — [Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models](http://arxiv.org/abs/2610.39509v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) deployed in safety-critical settings must resist adversarial inputs designed to elicit harmful outputs. We present a systematic empirical evaluation of five adversarial jailbreaking attack families---direct requests, roleplay-based jailbreaking, hypothetical framing, instruction override, and obfuscation---across seven open-weight and API-accessible LLMs: Llama-3-8B, Llama-3.1-8B, Llama-3.2-3B, Mistral-7B, Qwen2.5-7B, Gemma2-9B, and Phi-4-14B. We further evaluate fou...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 14 papers

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

- **2026-10-30** — Sizhe Chen, Yibo Peng, Jaewon Chang et al. — [SecPO: Principled Adversarial Training for Prompt Injection Security](http://arxiv.org/abs/2610.41998v1)
  <details><summary>📄 Abstract</summary>
  Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers from attack success rates (ASRs) approaching 100% under adaptive prompt injections. One reason is that DPO anchors the model around the undefended reference model, which is insecure. We show an idealized reference model---an injection-invaria...
  </details>

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


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-11-02** — Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel et al. — [IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning](http://arxiv.org/abs/2611.03431v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies that exceed trusted authorization requirements. We present IAMRAGBENCH, a 60-case benchmark spanning scope, conditions, explicit denies, trust, permissions boundaries, and role delegation. It combines deterministic authorization-envelope sc...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-10-30** — Qi Wang, Kang Xu, Chengcheng Wan et al. — [RECAST: REconstruction of Chain-of-Thought via Auditable Structured Traces](http://arxiv.org/abs/2610.41813v1)
  <details><summary>📄 Abstract</summary>
  Large closed-source reasoning models expose only their final answers. The intermediate reasoning that produces those answers is hidden behind API surfaces, tool-call policies, and safety filters. Existing chain-of-thought (CoT) extraction methods assume a side channel: a visible reasoning field, a scratchpad carried through tool calls, or a signed/encrypted reasoning block. We reproduce three representative state-of-the-art extraction methods and find that, on Claude-Sonnet-5.5 accessed through ...
  </details>

- **2026-10-29** — Yifan Wang, Zhenyi Gai, Yiwen Zhao et al. — [Before the Next Rollout: Diagnosing Skill Utility Shifts from Policy Updates](http://arxiv.org/abs/2610.39358v1)
  <details><summary>📄 Abstract</summary>
  Skill-evolution methods typically analyze execution trajectories to guide agent skill refinement. However, policy updates can change the behavioral effects and marginal utility of an unchanged skill. Attribution based on earlier trajectories may therefore no longer reflect the skill's contribution under the updated policy. Moreover, trajectory failures can arise from multiple factors, making individual skill contributions difficult to isolate. We evaluate whether policy-update signals contain pr...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-11-02** — Farooq Shaikh, Biagio Montaruli — [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](http://arxiv.org/abs/2611.03555v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions without confirming real execution. We present the first cross-framework measurement of MCP tool poisoning with real tool execution. A 25-class root-cause taxonomy unifies prior classi...
  </details>

- **2026-11-01** — Bicheng Xiong, Tao Li, Chenhui Cui et al. — [GDBack: A Group-Delay Backdoor Attack on Speaker Identification via Analytic All-Pass Filtering](http://arxiv.org/abs/2611.01721v1)
  <details><summary>📄 Abstract</summary>
  Existing phase-based backdoor attacks on speaker identification rely on shared absolute phase patterns for cross-sample trigger consistency, while other audio backdoor attacks have explored shared transformations that produce input-dependent triggers. Whether phase-based triggers can achieve similar consistency without imposing identical output phase patterns remains unclear. We propose GDBack, a poison-only group-delay backdoor attack using cascaded second-order analytic all-pass filters. Apply...
  </details>

- **2026-10-31** — Zhifang Zhang, Qiang Huang, Chenpeng Wang et al. — [Context-Shielded Backdoor Attack against Large Vision-Language Models](http://arxiv.org/abs/2611.01252v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) routinely use inference-time visual-token compression to prune hundreds of patch tokens down to a compact budget. Existing LVLM backdoors fire whenever a triggered image appears, whereas prior deployment-triggered attacks activate only when model weights are quantized or pruned. However, conventional LVLM backdoors exhibit nearly 100% attack success rate (ASR) under full-token inference, immediately exposing compromised checkpoints during pre-deployment audit...
  </details>

- **2026-10-29** — Kunhang Lv, Rui Han, Fuqi Jia et al. — [Verifiable LLM-Guided Focal SMT Solving for Quantified Arrays](http://arxiv.org/abs/2610.39435v1)
  <details><summary>📄 Abstract</summary>
  Large language models can often identify useful semantic structure in formal artifacts, but their outputs cannot be trusted as proofs or solver decisions. We study whether LLMs can instead guide formal reasoning systems through a narrow, solver-verifiable interface. We instantiate this idea in quantified array SMT solving, where modern instantiation-based techniques can fail when key ground terms and equalities are hidden by auxiliary variables, axiom guards, and nested array terms. We observe t...
  </details>

- **2026-10-29** — Youngjin Jin, Seungwon Shin — [ARBITRA: Robust Document-Level ATT&CK Extraction via Multi-Expert Argumentation](http://arxiv.org/abs/2610.39433v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence (CTI) reports describe adversary behavior in natural language, but converting them into structured MITRE ATT&CK mappings remains difficult: existing methods decompose reports to sentence-level granularity for extraction, while modern LLMs can work with full reports in a single pass but with noticeable performance degradation. We present ARBITRA, which orchestrates multiple role-specialized LLM experts that propose candidate ATT&CK entities from the full report, which ar...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-11-02** — Xulin Chen, Ruipeng Liu, Garrett E. Katz — [Beyond $L_\infty$-Norm Sets: Synthesizing Interpretable Non-Uniform Uncertainty Sets for Evaluation-Time State-Adversarial Robustness](http://arxiv.org/abs/2611.02576v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) agents are vulnerable to perturbations of their observed state inputs. Prior works often constrain state adversaries with $L_p$-norm uncertainty sets and evaluate policy performance under the resulting perturbations. However, in continuous control tasks like robotics control, different state dimensions have distinct physical meanings and influence policy behavior to different degrees, which $L_p$-norm sets fail to capture or explain. Moreover, it is important to...
  </details>

- **2026-11-02** — Zewei Shi, Ruoxi Sun, Minhui Xue et al. — [Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting](http://arxiv.org/abs/2611.02310v1)
  <details><summary>📄 Abstract</summary>
  Accurate electricity-demand forecasting is essential for the modern energy infrastructure. Recently, Times-Series Large Language Models (TS-LLMs) have emerged as a promising approach to forecasting more accurate demand from historical consumption data in zero- and few-shot settings, helping energy operators effectively plan supply and allocate energy resources. However, these models are vulnerable to compromised sensor inputs that can distort forecasts and lead to erroneous market orders or unne...
  </details>

- **2026-10-31** — Siu Wai Shi, Xiaochen Zhu, Xinjian Luo et al. — [The Blind Spots of Detection: Adversarial Perturbation Attacks against Watchdogs in Distributed LLM Inference](http://arxiv.org/abs/2611.01097v1)
  <details><summary>📄 Abstract</summary>
  Decentralizing large language model (LLM) inference across untrusted Web nodes requires robust verification to ensure computational integrity. Existing activation-based verification and detection mechanisms validate intermediate outputs against reference values, permitting bounded numerical deviations to accommodate benign cross-hardware discrepancies. However, a critical security question remains: what can a malicious worker achieve while operating within these tolerance bounds?   In this work,...
  </details>

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


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 31 papers

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

- **2026-10-31** — Zhuohang Jiang, Yuxin Chen, Haohao Qu et al. — [HiGenTrans: Hierarchical LLM Knowledge Transfer for Generative Recommendation](http://arxiv.org/abs/2611.01129v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation promises to simplify conventional multi-stage recommender systems by generating item Semantic IDs (SIDs) autoregressively. However, two obstacles limit its effective- ness in industrial settings: interaction-only supervision underuses the semantic knowledge encoded in pretrained language models, while beam-search likelihood ranks token sequences rather than directly estimating item relevance. To address these limitations, we propose HiGenTrans, a three-level framework t...
  </details>

- **2026-10-31** — Zixian Gao, Penghao Luo, Xiangcheng Cao et al. — [StreamDuo: A Live Commentator and a Research Agent for Unseen Games](http://arxiv.org/abs/2611.01120v1)
  <details><summary>📄 Abstract</summary>
  Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowledge of the game world. We propose StreamDuo, which pairs a trainable commentator with a frozen research agent that reads the wiki of the game being played. When the commentator sees something it cannot...
  </details>

- **2026-10-30** — Donghang Duan, Qingyu Liu, Yifei Liu et al. — [How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces](http://arxiv.org/abs/2610.41885v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agents interact with external tools through protocols such as the Model Context Protocol (MCP), producing tool-call traces that may expose behavioral signals about users. In this work, we systematically study the risk of user-profile inference from MCP tool-call traces, where observers infer user attributes from protocol-valid tool interactions without access to user conversations. We introduce PrivacyTrace, a benchmark containing 1,000 synthetic user profiles an...
  </details>

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


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-11-01** — Marco Molinari, Gabriele Bettineschi — [Multi-Agent Collusion and the J-Space](http://arxiv.org/abs/2611.02153v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly deployed in Multi-Agent Systems (MAS), and they introduce the risk of coordination among agents that might escape human oversight. The J-space has been used to uncover deception in single LLMs, but its use for uncovering and steering collusion between agents remains unexplored. We show, with interpretability experiments on DeepSeek-V4-Flash (284B) on the NARCBench collusion benchmark, that colluding agents' J-space holds the collusion itself: before replying, 86% of c...
  </details>

- **2026-10-29** — Leonidas Raghav — [Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In](http://arxiv.org/abs/2610.40588v1)
  <details><summary>📄 Abstract</summary>
  When AI agents share channels and credentials, one agent can press another to break its operator's rule, a first step towards collusion. Output filters check only what an agent has already written. Can an overseer tell beforehand that an agent is about to give in? We show that a linear probe on the agent's activations can, in a controlled multi-agent setting. Across six scenarios, a peer presses a target for up to 20 rounds to reveal a secret, such as a deploy token; the target often refuses, th...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

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

- **2026-10-31** — Orestis Oikonomou, Bogdan Raonic — [The Verifier Is Part of the Simulator: Evidence-View Gaming in Agentic Equation Discovery](http://arxiv.org/abs/2611.01334v1)
  <details><summary>📄 Abstract</summary>
  A growing number of agentic pipelines search for governing equations: an agent proposes laws and a verifier checks them against simulated trajectories. The verifier sees only a numerical summary: integrals against test functions on a time grid. That summary carries its own discretization error, making the verifier part of the simulator. We freeze the trajectory, candidate library, verifier and thresholds, leaving the agent one move: which permitted summary to admit. Without scores or language mo...
  </details>

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


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

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

- **2026-10-31** — Elias Malomgré, Pieter Simoens — [Alignment Flywheel-Guided Suppression Patching for Interactionless Inverse Reinforcement Learning](http://arxiv.org/abs/2611.01322v1)
  <details><summary>📄 Abstract</summary>
  Learned reward models allow reinforcement-learning agents to use demonstrations, implicit feedback, safety constraints, social norms, or other sources that do not provide a complete hand-designed scalar reward. However, a learned reward model can assign high reward to unwanted behavior. A policy can exploit these errors during training. Later requirements can also identify additional regions where the deployed reward should change. We introduce \emph{flywheel-guided patching}, a mechanism for ma...
  </details>

- **2026-10-31** — Chase J. Metoyer — [Satisfied, Not Solving: Wireheading of Bounded Homeostatic Rewards in Reinforcement Learning](http://arxiv.org/abs/2611.01183v1)
  <details><summary>📄 Abstract</summary>
  Bounded intrinsic rewards are often assumed to be safe from exploitation: if a signal can yield at most a fixed amount, gaming it should not pay. We test this for a homeostatic satiation reward, in which needs build up and relieving them is rewarding, and give the agent a cheap action that resets its needs. In MiniGrid DoorKey-8x8, PPO agents with this action solved 2 of 80 seeds, against 71 of 80 on the same seeds without it; in KeyCorridorS3R1, 0 of 20 against 20 of 20. Their policies stayed n...
  </details>

- **2026-10-31** — Kunal Bhosikar, Prajas Wadekar, Venkata Sai Pranav Bachina et al. — [SHield: Watermarking 4D Gaussian Splatting via Spherical Harmonic Coefficient Perturbation](http://arxiv.org/abs/2611.01162v1)
  <details><summary>📄 Abstract</summary>
  4D Gaussian Splatting (4DGS) models are computationally expensive to train but distributed as easily copied parameter files. Existing watermarks protect these assets by fine-tuning the scene against a neural decoder to extract bit strings from rendered video, a heavy process vulnerable to the temporal dynamics of dynamic scenes. However, if the threat model targets the redistributed file itself, verification can be vastly simplified. Because the canonical Spherical-Harmonic (SH) coefficients of ...
  </details>

- **2026-10-31** — Xianglong Guo, Jianyang Li — [Robust Pixel-wise Digital Image Correlation under Large Motions and Illumination Variations via a Global-to-Local Hybrid Neural Field](http://arxiv.org/abs/2611.01018v1)
  <details><summary>📄 Abstract</summary>
  Digital image correlation (DIC) is a widely used non-contact technique for full-field displacement measurement. Data-driven deep-learning DIC offers rapid inference but may generalize poorly to unseen speckle patterns, deformation modes, noise levels, and illumination conditions. Classical optimization-based DIC and recent image-constrained neural formulations avoid labeled displacement data, yet their convergence and accuracy remain vulnerable to initialization, large rigid-body motion, fine no...
  </details>

- **2026-10-31** — Chongxian Chen, Fan Mo, Xin Fan et al. — [PACT: Defending Recommendation against Promotional News Rewriting via Attack-Diverse Score Consistency](http://arxiv.org/abs/2611.00972v1)
  <details><summary>📄 Abstract</summary>
  Personalized news recommenders are increasingly vulnerable to LLM-powered promotional attacks, where content providers rephrase headlines to manipulate rankings without altering underlying facts. Defending against such manipulation requires covering a wide spectrum of LLM generators and optimization strategies--ranging from stylistic prompting to reinforcement feedback--without incurring prohibitive training or inference costs. In this work, we present PACT (Pooled Attack Consistency Training), ...
  </details>

- **2026-10-30** — Gyeongjin Kang, Freeman Cheng, Botao Ye et al. — [Rethinking Asymmetry in Self-Supervised 3D Geometry Learning](http://arxiv.org/abs/2610.42092v1)
  <details><summary>📄 Abstract</summary>
  Self-supervised learning relies on asymmetry between what a model observes and what it must explain. Recent methods learn 3D geometry from unposed images by predicting cameras and scene structure, then rendering held-out views. To avoid trivial solutions, they impose this asymmetry in the input space, restricting how views interact through separate branches or masked attention. We revisit this design with geometric accuracy, rather than rendering quality, as the main objective. When a held-out v...
  </details>

- **2026-10-30** — Yewen Cao, Dengke Wei, Yulin Shao — [Embodied Movable Antennas](http://arxiv.org/abs/2610.42078v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces embodied movable antennas (MAs), a new MA architecture that rethinks the source of antenna mobility. Unlike conventional MAs that rely on dedicated antenna actuators, embodied MAs harness the mechanical degrees of freedom already present in physical agents to reconfigure antenna position and orientation. We distinguish two modes of embodied MAs: task-coupled and task-preserving. Focusing on the latter, we show how wireless channels can be reconfigured by exploiting task-equ...
  </details>

- **2026-10-30** — Xin Ming Li, Peng Hu — [RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks](http://arxiv.org/abs/2610.42068v1)
  <details><summary>📄 Abstract</summary>
  Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences. We propose RAMA, a retrieval-augmented multi-agent DRL framework with Approximate Information State (AIS), in which each satellite combines its loca...
  </details>

- **2026-10-30** — Tina Rezaei, Suzan Bayhan, Andrea Continella et al. — [Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products](http://arxiv.org/abs/2610.42032v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Things (IoT) has expanded beyond consumer smart homes to sectors, such as industrial systems, healthcare, and smart cities, broadening the IoT attack surface. Prior empirical work has focused on studying aggregate IoT vulnerability characteristics or specific protocols, so patching is directed by aggregate security guidance. However, if dominant weaknesses differ substantially across sectors or products, such uniform guidance misdirects the remediation effort. To address this gap...
  </details>

- **2026-10-30** — Chanhyuk Lee, Wonjung Kim, Patrick Pynadath et al. — [Asynchronous Flow Map Language Models](http://arxiv.org/abs/2610.42018v1)
  <details><summary>📄 Abstract</summary>
  The order in which tokens are predicted in language modeling has a profound impact on the quality of generated sequences. Autoregressive and masked diffusion models iteratively fill in tokens and can exploit such orderings across generation steps, but how to leverage an ordering for one-step parallel language modeling is unclear. We introduce asynchronous flow map language models (aFMLMs), which incorporate prediction order into one-step modeling by learning the flow maps of asynchronous flows. ...
  </details>

- **2026-10-30** — Giacomo Magnifico, Eduard Barbu — [ReX-GG: a LLM Ensemble Pipeline for Relation-extraction and Graph Generation](http://arxiv.org/abs/2610.41901v1)
  <details><summary>📄 Abstract</summary>
  Current LLM ensemble frameworks focus on multi-step setups with additional modules for answer ranking, often opting for token and span analysis rather than structured outputs, leading to heavyweight architectures with potential fail states along the pipeline. Faster, lighter solutions are more vulnerable to hallucination propagation and can lack output control in more complex pipelines. This paper proposes a customisable, lightweight ensemble workflow of coordinated Large Language Models that le...
  </details>

- **2026-10-30** — Marco Bondaschi, Michael Gastpar — [Batch Universal Prediction via Conditional Additive Smoothing](http://arxiv.org/abs/2610.41859v1)
  <details><summary>📄 Abstract</summary>
  Modern language models motivate renewed interest in universal prediction problems in which a predictor can exploit previously observed data before predicting a fresh sequence. We study an idealized version of this setting by introducing \emph{batch regret}: a conditional analogue of classical average regret in which a predictor observes a batch of $n$ training sequences and is then evaluated on an independent test sequence generated by the same unknown source. Additive smoothing estimators, whic...
  </details>

- **2026-10-30** — Hao Dai, Panyu Chen, Jagmohan Chauhan — [MFlowAudio: Efficient Text-to-Audio Synthesis via Mamba-based Stateful Flow Matching](http://arxiv.org/abs/2610.41852v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in audio generation have been largely driven by Transformer-based diffusion models. However, these models suffer from quadratic complexity of self-attention, severely bottlenecking the long-form audio synthesis. To overcome this limitation, we propose MFlowAudio, a novel latent audio generation framework that synergizes the continuous-time dynamics of Flow Matching with a custom-designed TCMamba backbone. TCMamba uses an innovative dual-scan mechanism: a TimeMamba module to c...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 57 papers

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

- **2026-11-01** — Yize Cai, Zhiqing Hong — [GaitFM: A Cross-Modal Foundation Model for Wearable Gait Assessment](http://arxiv.org/abs/2611.01684v1)
  <details><summary>📄 Abstract</summary>
  Gait assessment supports the diagnosis, monitoring, and prognosis of diverse movement-related conditions, such as neurological and musculoskeletal disorders. Recent advances in deep learning using everyday wearable inertial measurement units (IMUs) offer an accessible and low-cost approach to automated gait assessment. However, IMU measurements vary substantially across individuals, body locations, and device configurations, while existing deep learning models are typically developed using small...
  </details>

- **2026-11-01** — Zhangkai Wu, Xu Zhang, Zhihao Hao et al. — [CCD: Context-Calibrated Open-Entity Out-of-Distribution Detection in In-Context Tabular Foundation Models](http://arxiv.org/abs/2611.01489v1)
  <details><summary>📄 Abstract</summary>
  In-context tabular foundation models (TFMs), such as TabPFN, predict from a labelled context without updating their parameters and are increasingly used for out-of-distribution (OOD) detection in Web applications, whose test rows come from entities absent from that context. Such applications need open-entity OOD detection: a new entity must not be mistaken for an unknown class, and an unknown class must still be caught. Existing detectors fail in this setting, and an entity-split gap hides the f...
  </details>

- **2026-10-31** — Carl Benda, Eren Kurshan, Aydin Aysu et al. — [Side-Channel Attack Prevention for Post Quantum Cryptography Algorithms: A 3D-Shield Approach](http://arxiv.org/abs/2611.01144v1)
  <details><summary>📄 Abstract</summary>
  Despite their theoretical quantum attack resistance, practical implementations of post-quantum cryptography (PQC) algorithms remain susceptible to side-channel attacks. This includes all standard algorithms selected the National Institute of Standards and Technology (NIST) such as Kyber/ML-KEM, Dilithium/ML-DSA, Falcon/FN-DSA and SPHINCS+/SLH-DSA. This paper proposes an alternative defense for side-channel resilience based on 3D integration that uses 3D hardware to shield the underlying cryptogr...
  </details>

- **2026-10-31** — Pedro Farinha — [What Must Be Done Here? Using a Bounded Application-Security Ontology at the Point of Change](http://arxiv.org/abs/2611.01127v1)
  <details><summary>📄 Abstract</summary>
  The security guidance that bears on code is real but scattered. It lives across secure-development frameworks, verification standards, controls catalogues, threat taxonomies, and, increasingly, normative regimes such as the EU's NIS2 -- and most of it is written for readers other than the engineer, or the AI assistant, at a point of change. Existing cybersecurity ontologies largely model attacks, indicators, and risk for detection and analysis, not the engineering-practice substance one must act...
  </details>

- **2026-10-31** — Allan Grosvenor, Anton Zemlyansky, Abdul Wahab et al. — [GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations](http://arxiv.org/abs/2611.01001v1)
  <details><summary>📄 Abstract</summary>
  An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose, rank, and accelerate; a symbolic rules engine checks every consequential action against hard limits before it executes; and validated physics confirms and decides. GURU runs a workflow as a closed control loop, with Na...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 54 papers

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

- **2026-10-31** — Yuanbo Li, Vivian Liu, Sean Liu et al. — [Composable CAD: Sketch-to-CAD Program Synthesis in Parts](http://arxiv.org/abs/2611.01165v1)
  <details><summary>📄 Abstract</summary>
  Designers often build CAD models part by part, and may iterate on individual components throughout the design process. Recent vision-language models (VLMs) can synthesize CAD programs from sketches, but generating parts independently does not ensure that they are composable: components may lose the intended proportions and alignments or fail to join correctly where they meet. We present Composable CAD, a framework that uses off-the-shelf VLMs to synthesize a design space of independently sampled...
  </details>

- **2026-10-31** — Dipto Sumit, Zobeida Zaman Chowdhury, Syeda Fabiayee Jahan et al. — [Label Smoothing in Disguise? Gated Knowledge Distillation for Low-Resource Bangla Generation](http://arxiv.org/abs/2611.01065v1)
  <details><summary>📄 Abstract</summary>
  Gated knowledge distillation (KD) weights teacher signals per token or example, aiming to trust an imperfect teacher only where it seems reliable. We test two gates: EWAD (entropy-weighted agreement-aware distillation), which gates tokens by teacher confidence, and CHAD (counterfactual harm-aware distillation), which gates examples by gradient alignment with validation data. Across six Bangla-centric tasks, three student models (60M to about 2B parameters), and two teacher families, no gate sign...
  </details>

- **2026-10-31** — Zain Naboulsi — [Are Fake Citations a Form of Reward Hacking? A Pre-Registered Study of Post-Training and Citation Cues](http://arxiv.org/abs/2611.01313v1)
  <details><summary>📄 Abstract</summary>
  Post-trained language models fabricate citations at high rates. We ask whether that is reward hacking: scoring well on a proxy for scholarship while doing worse on what it stands for. We ran four pre-registered experiments on 900 frozen questions (US federal case law, computationally adjacent scientific literature, and medical literature) across twelve open-weights checkpoints covering four post-training stages of three model families, then refit on fifteen. The clearest result holds the weights...
  </details>

- **2026-10-30** — Ning E, Changde Du, Yizhuo Lu et al. — [Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions](http://arxiv.org/abs/2610.41951v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved impressive performance across a wide range of reasoning tasks, yet it remains unclear whether their internal representations and decision criteria align with the latent structure of human cognition. In this work, we propose a novel framework to align MLLMs with the multidimensional mental representations underlying human similarity judgements. We build on a previously established behavior-derived semantic embedding space, in which objects ar...
  </details>

- **2026-10-30** — Raj Shekhar Singh, Pratham Agarwal — [Iterated Integrals as Lexical Fingerprints: Path Signature Embeddings for Lexical Similarity](http://arxiv.org/abs/2610.41855v1)
  <details><summary>📄 Abstract</summary>
  While sentence embeddings are primarily designed for semantic generalization, their latent geometry implicitly encodes surface-level lexical properties, a relationship that remains poorly understood. Shallow pooling methods discard word order, while deep Transformer models obscure these lexical alignments behind computational complexity and uninterpretable spaces. We propose constructing sentence embeddings via the path signature of Word2Vec trajectories, leveraging the iterated integrals of rou...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 50 papers

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

- **2026-11-01** — Lakshmikar R. Polamreddy, Jialu Li, Youshan Zhang — [MedNet and U$^2$-ViT: A Nested Vision Transformer Diffusion Framework for Diverse Medical Images Generation](http://arxiv.org/abs/2611.01605v1)
  <details><summary>📄 Abstract</summary>
  The scarcity of diverse, high-quality medical images remains a significant bottleneck in advancing AI-driven medical diagnostics and treatment planning. Traditional datasets often suffer from class imbalances, limited disease coverage, and insufficient variations in imaging conditions - challenges that hinder the development of robust, generalizable models. To address this, we introduce MedNet, a large-scale, multi-modal text-to-image dataset spanning 61 disease categories with 160 classes, cove...
  </details>

- **2026-11-01** — Tao Fan, Guoqiang Ma — [\textsc{ChatDify}: Automating End-to-End Dify Workflow Synthesis from Natural Language via Multi-Agent Collaboration](http://arxiv.org/abs/2611.01563v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of Large Language Models has catalyzed powerful application development platforms like Dify, which enable users to build sophisticated LLM-powered workflows through modular node orchestration. However, manually configuring these workflows requires deep platform expertise and remains time-consuming and error-prone, creating a significant barrier for non-expert users. To address this challenge, we propose \textsc{ChatDify}, a novel multi-agent framework that automates end-to-end ...
  </details>

- **2026-11-01** — Tung-Wei Kuo — [A Deterministic O(log m)-Competitive Algorithm for Online Minimum Cost Bipartite Matching with Delays](http://arxiv.org/abs/2611.01553v1)
  <details><summary>📄 Abstract</summary>
  In the online Minimum cost Bipartite Perfect Matching with Delays (MBPMD) problem, $m$ requests and $m$ servers arrive over time in a metric space. An online algorithm has to match each request to a server and can postpone a matching decision by paying the delay cost. The objective is to minimize the total distance and delay cost. Azar, Chiplunkar, and Kaplan gave a randomized $O(\log n)$-competitive algorithm for metric spaces with $n$ points that are known in advance. For deterministic algorit...
  </details>

- **2026-11-01** — Geo Jie Zhou, Kunzhe Song, Ruxin Lin et al. — [RadPose: ISAC-based RF 3D Human Pose Estimation](http://arxiv.org/abs/2611.01400v1)
  <details><summary>📄 Abstract</summary>
  Human pose estimation under adverse lighting and occlusion conditions remains challenging for camera- and LiDAR-based systems. Although mmWave radars provide robustness to illumination and occlusion, they rely on dedicated hardware and licensed spectrum, limiting scalability. In this paper, we present RadPose, a learning-based monostatic integrated sensing and communication (ISAC) framework that enables mmWave communication devices to perform 3D human pose estimation. Unlike specialized radars, ...
  </details>

- **2026-10-31** — Yousef Abuseta — [A Domain Driven Design Based Reference Architecture for IoT Systems Engineering](http://arxiv.org/abs/2611.01196v1)
  <details><summary>📄 Abstract</summary>
  The Internet of Things (IoT) paradigm continues to gain significant traction across diverse do-mains, primarily driven by its transformative and socio-economic benefits. However, engineering robust IoT systems remains a formidable challenge, largely due to the inherent dynamism, volatility, and uncertainty of their operational environments. To mitigate this architectural complexity, microservices have emerged as a viable alternative to traditional, rigid monolithic frameworks, offering a scalabl...
  </details>

- **2026-10-31** — Grant Phillips, Hoang-Dung Tran, Justin M. Bradley — [Robust Safety Assurance for Robotic Swarms Using Decentralized Collision Verification](http://arxiv.org/abs/2611.01081v1)
  <details><summary>📄 Abstract</summary>
  In this paper we present the methodologies, results, and analysis used to deploy a decentralized safety verification algorithm on a robotic swarm to prevent collisions at runtime in an outdoor environment. Typically, approaches toward verification of swarms of cyber-physical systems (CPS) are evaluated solely in numerical simulations or in highly controlled, noiseless indoor environments. Our efforts to implement collision avoidance on a real swarm system outdoors have revealed that the underlyi...
  </details>

- **2026-10-31** — Zilong Huang, Zipeng Ye, Caicheng Wang et al. — [ClothDojo: Learned Data Generation and Benchmarking for Bimanual Garment Flattening and Folding](http://arxiv.org/abs/2611.01190v1)
  <details><summary>📄 Abstract</summary>
  Garment flattening and folding require robots to identify garment structure during manipulation and adapt their actions as the cloth deforms. We present ClothDojo, a simulation platform that generates adaptive manipulation trajectories at scale across diverse garments and initial states and evaluates policies in closed loop. ClothDojo encodes each garment's canonical mesh coordinates as an NOCS texture, providing canonical surface-position cues through the visual interface of a pretrained vision...
  </details>

- **2026-10-31** — Saber Zerhoudi — [Wrong Together: Shared Bias in User Simulation](http://arxiv.org/abs/2611.01354v1)
  <details><summary>📄 Abstract</summary>
  User simulators generate responses in place of human participants, allowing researchers to estimate the result of a study. To use these estimates before collecting human responses, researchers need a way to assess their reliability. We test whether disagreement among simulators can identify unreliable estimates of a group's response proportions and of differences between groups. We evaluate this signal using 6 language-model simulators and existing GlobalOpinionQA responses for 60 questions in 1...
  </details>

- **2026-10-30** — Leon Lufkin, Cutter Dawes, Alexander Speicher et al. — [Subquadratic Attention with a Hierarchical Tree-Structured Indexer](http://arxiv.org/abs/2610.42112v1)
  <details><summary>📄 Abstract</summary>
  The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadrati...
  </details>

- **2026-10-30** — Philipp Bordne, André Biedenkapp — [Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments](http://arxiv.org/abs/2610.42100v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (RL) is a powerful framework for sequential decision-making. Despite many high-profile successes in recent years, deep RL is known to be brittle. An emerging line of research attributes this brittleness to a loss of plasticity in neural networks. However, plasticity loss has so far been understudied in stochastic environments. We study this interplay systematically, training SAC agents on three DeepMind Control tasks augmented with controlled levels of observation and...
  </details>

- **2026-10-30** — Yuxin Chen, Yuejie Chi, Jianqing Fan et al. — [Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective](http://arxiv.org/abs/2610.41903v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) embodies a foundational paradigm for sequential decision-making in the face of uncertainty. The rapid growth of model complexity in emerging applications has significantly amplified the challenges of achieving data-efficient RL, particularly in sample-starved scenarios where data collection may be costly, time-consuming, or even high-stakes. Consequently, understanding and improving the data efficiency of RL algorithms has become a central problem of both fundamental ...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

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

- **2026-11-01** — Hangming Zhang, Yao Zhao, Haotian Kuang et al. — [SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales](http://arxiv.org/abs/2611.01695v1)
  <details><summary>📄 Abstract</summary>
  B2B outbound sales involves high transaction values and relationship-based trust, so closing a deal typically requires multiple rounds of outreach building on prior context. Existing LLM-based sales agents operate within single sessions and cannot carry forward context or refine strategies from experience. Methods that do learn from experience store lessons as unstructured text and treat all outcomes as equally informative, with no mechanism to distinguish a flawed strategy from an external fact...
  </details>

- **2026-10-31** — Xiaoyan Wu, Fan Shi — [Large language models underrepresent malice and overreport virtue](http://arxiv.org/abs/2611.01332v1)
  <details><summary>📄 Abstract</summary>
  People increasingly use large language models (LLMs) to interpret others' behaviour, often assuming that LLMs infer motives as humans do. Aligned LLMs attribute more benevolent and less malevolent motives to a whistleblower than humans do, but ratings alone cannot reveal whether these differences arise in internal representations or at report. Here we compare linear-probe readouts of LLMs' internal states with their own ratings at the same prompt position for four motives, in two preregistered s...
  </details>

- **2026-10-30** — Yingzhao Jian, Zhongan Wang, Yuxuan Hou et al. — [Learning to Interact and Direct: Co-Evolving Video Director Agents](http://arxiv.org/abs/2610.41865v1)
  <details><summary>📄 Abstract</summary>
  Video director agents orchestrate multistage production to realize users' creative visions. Emerging research on their self-evolution advances screenplay planning effectively. However, the mutual reinforcement between directing and user interaction remains largely overlooked. Improved interaction clarifies user intent and informs workflow refinement, while more reliable execution shifts collaboration from troubleshooting to creative decisions. To this end, we introduce LIT (Learning to Interact ...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-29** — Juan Belieni, Ana Carolina Erthal, Eliezer de Souza da Silva et al. — [Preserving Utility in Continual LLM Unlearning via Orthogonal Projections](http://arxiv.org/abs/2610.40483v1)
  <details><summary>📄 Abstract</summary>
  Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. While unlearning requests happen continuously during a model's lifetime, the vast majority of LLM unlearning methods are ill-suited for iterated removal, yielding steep decay in forgetting and utility upon sequential unlearning. This decay stems from interference between successive updates, as each new...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-10-31** — Wayner Barrios, Kenneth Barrios — [What Does a Safety Label Measure? Auditing Situational-Safety Benchmarks for Multimodal LLMs](http://arxiv.org/abs/2611.01125v1)
  <details><summary>📄 Abstract</summary>
  Situational-safety benchmarks label each scene SAFE or UNSAFE and score a multimodal large language model (MLLM) against that label, usually by judging its free-form answer, and these scores guide deployment. We ask what such a label measures. A label score can come from the scene, the request or the benchmark's own files. We propose the Benchmark Card, seven measured fields that tell them apart, and fill it for six benchmarks. Only MSSBench chat leaks the label through its image files: image si...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-11-02** — Jiawei Ran, Yuxia Zhang, Ziyang Zhao et al. — [IssueLighter: An Issue Type-Aware LLM Agent for Issue Report Validity Assessment](http://arxiv.org/abs/2611.02721v1)
  <details><summary>📄 Abstract</summary>
  Invalid issue reports are prevalent in open source software (OSS) projects, imposing substantial burdens on maintainers who already face a high risk of burnout. Prior research has primarily focused on identifying invalid reports for specific issue categories (e.g., bug and wontfix), leaving the broader landscape of OSS issue types largely unexplored and limiting the generalizability of existing approaches. Moreover, existing methods provide little support for explaining or validating their predi...
  </details>

- **2026-11-01** — Haosong Wang, Ting Tan, Yao Li et al. — [The Agentic Observer Hackathon: Autonomous Decision-making in Simulated Astronomical Surveys](http://arxiv.org/abs/2611.01988v1)
  <details><summary>📄 Abstract</summary>
  Astronomical surveys must allocate observing time while responding to changing conditions and competing scientific priorities. We present the Agentic Observer Hackathon (AOH), a community challenge for studying autonomous survey operations. Within a synthetic multi-object survey with prescribed exposure responses and assignment constraints, decision systems select pointings, assign targets and choose exposure configurations while responding to observing requests, instrumental faults and data los...
  </details>

- **2026-10-31** — Stefano Maria Iacus, Haodong Qi — [ISBC: Interpretable Sparse Binary Coding of Pretrained Text Embeddings](http://arxiv.org/abs/2611.00999v1)
  <details><summary>📄 Abstract</summary>
  Pretrained text embeddings encode semantic structure in high-dimensional continuous spaces whose coordinates are difficult to interpret. We introduce Interpretable Sparse Binary Coding (ISBC), which learns a small set of binary dimensions from frozen embeddings without taxonomy labels or downstream outcomes. A trainable encoder and affine decoder combine reconstruction with controls on activity, factor utilization, dependence, and activation uncertainty. Individual bits and their conjunctions se...
  </details>

- **2026-10-30** — Nicolò Pagan, Petter Törnberg, Christopher A. Bail et al. — [LLM Recommenders Produce Demographic Inequality Through Content Preferences](http://arxiv.org/abs/2610.41854v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly being integrated into systems that rank and recommend online content. We examine how this shift can produce demographic inequality in whose voices are surfaced. Using 10,000 Twitter/X posts written by 1,000 survey respondents and linked to verified self-reported characteristics across nine demographic attributes, we conduct a controlled recommendation experiment across three LLM providers, six recommendation objectives, and five levels of contextual ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 184 papers

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

- **2026-11-01** — Alex Nguyen, Kenneth A. Norman, Gautam Reddy — [Meta-memorization and memorization scaling laws in transformers](http://arxiv.org/abs/2611.01564v1)
  <details><summary>📄 Abstract</summary>
  Larger transformers can memorize more data, with a capacity (in bits) that scales roughly linearly with the number of parameters. Counterintuitively, larger models also memorize faster, requiring fewer repetitions of a sequence during training before it is memorized. We reproduce both memorization scaling laws in transformers trained on random binary sequences, showing that rapid memorization can arise even when data contain no semantic or compositional structure. Rapid memorization is due to a ...
  </details>

- **2026-11-01** — Ziliang Qiu, Renfen Hu, Yi Ding et al. — [Revisiting LLM Homogeneity Through a Multidimensional Lens](http://arxiv.org/abs/2611.01549v1)
  <details><summary>📄 Abstract</summary>
  Concerns about LLM homogeneity are typically quantified with embedding similarity, which reduces two texts to a single score. We revisit homogeneity with 25 interpretable metrics spanning five dimensions: semantic, lexical, syntactic, structural, and stylistic & presentational. A human study shows that perceived similarity depends on both content (what responses say) and form (how they say it), yet embedding similarity correlates less with human meaning judgments than sentence-level matching ($ρ...
  </details>

- **2026-11-01** — Ming Lian — [Causal Optimal-Transport Attention: Positional Priors and Length Extrapolation](http://arxiv.org/abs/2611.01472v1)
  <details><summary>📄 Abstract</summary>
  Causal masking obstructs the column balancing used by optimal-transport (OT) attention. We study a prefix-consistent unbalanced operator and characterize the positional prior it induces. Under bounded scores, for any fixed balancing strength $ρ<1$, its fixed point dilutes attention: every fixed window receives a vanishing share as the context grows. For constant scores, we derive an exact scale-invariant prior. We then classify positional encodings by whether their distant attention mass remains...
  </details>

- **2026-11-01** — Saarth Deshpande, Neeraja J. Yadwadkar, Venkat Arun — [DIMWIT: Directly Invoking Models Without Intensive Tuning](http://arxiv.org/abs/2611.01463v1)
  <details><summary>📄 Abstract</summary>
  Resource managers typically encode what to do in a task-specific policy---a heuristic, an optimization procedure, or a model trained for the task---that must be developed before use and may need revision as the workload or system changes. We propose bypassing policy development and instead asking pretrained models to make resource-management decisions directly, given the current system state, desired outcome, and available choices. We evaluate this approach on microservice autoscaling, DRAM sizi...
  </details>

- **2026-11-01** — Haikai Zhao, Haisheng Fu, Zhengjie Miao et al. — [PROBE: Learned Proxy-Based Execution for Highly Selective Multimodal Semantic Queries](http://arxiv.org/abs/2611.01454v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) enable semantic queries over unstructured data, but invoking an LLM on every row is prohibitively expensive. Proxy-based execution can reduce this ple with the LLM and training a lightweight proxyto label the remaining rows. Nevertheless, in practical scenarios where semantic queries are highly selective, it remainschallenging to identify representative samples foLM budget and to achieve accurate predictions overthe remaining data using the proxy. We present PROBE, a...
  </details>

- **2026-10-31** — Shaswat Patel, Michel Liao, Peter Henderson et al. — [Do Coding Agents Catch Their Own Bugs? (They Don't.)](http://arxiv.org/abs/2611.01181v1)
  <details><summary>📄 Abstract</summary>
  In software development, engineers need to foresee and fix potential problems with their code that are not explicitly specified in requirements---such as pre-emptively considering vulnerabilities or other bugs from a code change. But current benchmarks often do not measure these future-looking consequences. We introduce $\textbf{Foresight-SWE}$, a benchmark for measuring whether coding agents can anticipate and address unstated problems during software engineering tasks. Foresight-SWE consists o...
  </details>

- **2026-10-31** — Taghrid Housari, Massa Rankoussi, Jafar Abdul Majeed et al. — [ArSciKids: Arabic Curriculum-Aligned Datasets for Scientific Experiment and Multiple-Choice Question Generation in Primary Education](http://arxiv.org/abs/2611.01191v1)
  <details><summary>📄 Abstract</summary>
  Despite growing interest in Arabic natural language processing, curriculum-aligned educational resources remain scarce compared with English, and few public datasets for Arabic curriculum content with structured, generation-ready annotations are available, particularly for primary-school science. We introduce ArSciKids, a collection of two Arabic datasets designed for curriculum-aligned educational content generation: (1) a scientific-experiments dataset containing 999 manually curated records f...
  </details>

- **2026-10-31** — Jagan B L, Sudhi S Vijayan, Renjith V R et al. — [Light Fidelity in Academic Libraries: A Radiant Journey to Light the Future Light Fidelity in Academic Libraries: A Radiant Journey to Light the Future](http://arxiv.org/abs/2611.01109v1)
  <details><summary>📄 Abstract</summary>
  Academic contexts have changed due to the fast expansion of communication technology, affecting information access, sharing, and dissemination. Light Fidelity (LiFi) is a new technology that may transform academic library connections in this changing environment. This article examines how LiFi can accelerate data transmission, secure data, and provide a more dynamic and collaborative learning environment to spur creativity. Academic libraries may accelerate information interchange using visible ...
  </details>

- **2026-10-31** — Chengcheng Wang, Yuheng Shi, Siyu Xu et al. — [Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](http://arxiv.org/abs/2611.01112v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's success rate from 22.5% under the reference control interface to 76.2%. We present Auriga, a task-agnostic agent harness that closes 68.3% of this gap in zero-shot manipulation without target-task trials or resets. In A...
  </details>

- **2026-10-31** — Chengbo Zheng, Yujie Zheng, Qian Zhu et al. — [Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction](http://arxiv.org/abs/2611.01087v1)
  <details><summary>📄 Abstract</summary>
  LLM assistants increasingly ask clarifying questions (CQs) to elicit preferences and tailor recommendations. Although prior work emphasizes improvements in answer quality and user experience, how CQs shape users' subsequent engagement and reliance remains unclear. We conducted a controlled experiment (N=180) across six everyday decision scenarios, comparing human-LLM interaction with and without CQs. We further manipulated whether responses violated explicit constraints and whether violations oc...
  </details>

- **2026-10-31** — Lin Yang, Yunjie Shen, Zheyu Li et al. — [Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone](http://arxiv.org/abs/2611.01011v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models re-encode the full observation through a multi-billion-parameter vision-language model (VLM) at every control step, even though scene semantics evolve at roughly 1 Hz while reactive control requires 20-50 Hz. We present a VLA that decouples the two: a VLM runs as a low-frequency semantic anchor whose cached context is reused across control steps, while a flow-matching action expert operates at high frequency, consuming the cached semantics with a fresh, low-la...
  </details>

- **2026-10-31** — Masaki Murooka, Ryoichi Nakajo, Tomohiro Motoda et al. — [Evaluating Tactile Foundation Models for End-to-End Imitation Learning in Contact-Rich Manipulation](http://arxiv.org/abs/2611.00957v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing plays an important role in imitation learning for contact-rich manipulation by providing direct observations of physical contact with objects. Recently, several tactile foundation models (TFMs) have been proposed to learn general-purpose tactile representations through pretraining on large-scale tactile datasets. However, how these pretrained tactile representations should be leveraged for end-to-end imitation learning remains insufficiently explored. In this work, we integrate m...
  </details>

- **2026-10-31** — Xujun Che, Depeng Xu, Jian Xiang et al. — [ProofPatch: Reviewing Lean Statements and Keeping the Reviews Valid as Formalizations Evolve](http://arxiv.org/abs/2611.01357v1)
  <details><summary>📄 Abstract</summary>
  The kernel of the Lean proof assistant checks that a proof establishes its statement. Whether the statement says what was intended is left to human reviewers. This is the old problem of validating a specification, and it grows more pressing as language models write formal statements in bulk and agents edit formal developments continuously. We present ProofPatch, a tool that helps reviewers judge Lean statements and keeps their judgments valid while the development changes. A reviewer can ask the...
  </details>

- **2026-10-31** — Hao Wu — [Before the First Bond: Depletion-Assisted Stochastic Capture at the Onset of Endocytosis](http://arxiv.org/abs/2611.01321v1)
  <details><summary>📄 Abstract</summary>
  In a crowded extracellular environment, viruses and nanoparticles must reach the cell membrane within a few nanometers before the first ligand-receptor bond can form. Crowders generate an entropic depletion attraction, yet continuum models usually assume contact is already established or treat the approach deterministically. We formulate a thermodynamically consistent stochastic theory for this pre-contact stage. The sphere-plane depletion geometry uses the exact Asakur-Oosawa spherical-cap over...
  </details>

- **2026-10-31** — Angana Borah, Zoha Hayat Bhatti, Zhijing Jin et al. — [CuriousTogether: Implications of Curiosity and Cultural Grounding in Multi-Agent LLM Interactions](http://arxiv.org/abs/2611.01301v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in multi-agent settings, exhibiting emergent collective behaviors, yet the role of curiosity as a driver of such dynamics remains understudied. We introduce CuriousTogether, a framework evaluating curiosity-driven multi-agent LLM interactions across three complementary dimensions: novelty-seeking, epistemic and social curiosity. Across eight tasks spanning reasoning, creative generation, and social bias mitigation, curiosity-guided multi-age...
  </details>

- **2026-10-31** — Hao Wu — [From First Bond to Stable Adhesion: Multivalent Bond Stabilization in Receptor-Mediated Endocytosis](http://arxiv.org/abs/2611.01293v1)
  <details><summary>📄 Abstract</summary>
  After a particle forms its first receptor--ligand bond near a cell membrane, stable attachment often requires a threshold number of additional bonds. This paper develops a biophysical kinetic theory of this post-capture stage. The bond-number dynamics are modeled as a finite birth--death chain on $n=0,1,\dots,m$, where $0$ is loss of the initial bond and $m$ is the stabilization threshold. The mesoscopic rates $λ_n$ and $μ_n$ encode the local energy landscape, accessible receptor--ligand pairs, ...
  </details>

- **2026-10-31** — Lion Hirth — [An analytical model to explain under which conditions home batteries create new load peaks in the local grid](http://arxiv.org/abs/2611.01286v1)
  <details><summary>📄 Abstract</summary>
  Simulation studies find that price-responsive home batteries and electric vehicles create new load peaks in low-voltage grids; with endogenous wholesale prices most of these peaks disappear. This paper explains both findings with an analytical model of the coincident peak at the transformer. The model is algebraic and solved in closed form, so the parameters that determine whether a new peak emerges and how large it becomes can be identified; they are few. The peak is the background load in the ...
  </details>

- **2026-10-31** — Alejandro Mozo Quesada, Sergio Gálvez Rojas, Francisco López Valverde — [Character-Name Concentration in LLM Fiction: Measuring Displacement and Mitigating Repetition](http://arxiv.org/abs/2611.01284v1)
  <details><summary>📄 Abstract</summary>
  Character names in large language model (LLM) fiction concentrate on a handful of recurrent names such as 'Elara' and 'Elias', a measurable face of AI slop. Existing fixes either require logit access or retraining, or operate per request and cannot control concentration across a corpus. How much prompt-level strategies reduce concentration, and at what cost to name naturalness, has not been systematically measured. We present an empirical study of name-concentration control across eight strategi...
  </details>

- **2026-10-31** — Heeyong Eun, Seungyeon Chung, Hyejee Park et al. — [Toward Bounding Coding-Agent Autonomy in Software Maintenance: A Pilot Study of Boundary Contracts](http://arxiv.org/abs/2611.01265v1)
  <details><summary>📄 Abstract</summary>
  As coding agents gain greater autonomy to modify software repositories, relevant context alone does not define their operational authority. An artifact may be relevant to a maintenance task while being inappropriate to edit; conversely, another artifact may be required even when it is not explicitly mentioned in the request. We explore Boundary Contracts, a machine-readable abstraction that makes task-specific artifact roles (editable, inspect-only, required, and protected) explicit before repos...
  </details>

- **2026-10-31** — Delyan Boychev, Ivo Petrov, Dimitar I. Dimitrov — [Fast and Exact Relative-Position Attention via Structure-Aware Kernels](http://arxiv.org/abs/2611.01182v1)
  <details><summary>📄 Abstract</summary>
  Relative-position attention mechanisms offer compelling alternatives to RoPE across various transformer architectures, delivering superior performance in domains such as audio. These mechanisms typically modify attention scores by adding content-position or bias-position terms. Unlike RoPE, which encodes position via per-token rotations directly on the queries and keys, relative-position terms generally require pairwise offset-dependent computation or lookups, complicating their integration into...
  </details>

- **2026-10-31** — Yi Tang, Geoffrey Martin, Yiye Zhang et al. — [Capacity Planning for Resource-Constrained Clinical LLM Serving](http://arxiv.org/abs/2611.01152v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models (LLMs) under a fixed accelerator budget requires jointly deciding how computational capacity is allocated across model sizes and how incoming requests are routed across that capacity. Although prior work has extensively studied LLM routing and serving efficiency, the relative importance of fleet composition and routing under resource constraints remains less understood. We investigate this question using a controlled four-GPU serving environment with heterogeneous...
  </details>

- **2026-10-31** — Yangyu Wu, Siru Zhong, Haoyuan Liang et al. — [CivicBench: A Benchmark and Memory Framework for Web-Based Civic Data Analytics](http://arxiv.org/abs/2611.01145v1)
  <details><summary>📄 Abstract</summary>
  Municipalities publish service requests, geographic boundaries, weather observations, demographic estimates, and operational guidance through independently maintained Web portals. Civic analysis must combine these sources while preserving their schemas, source links, spatial and temporal scopes, and interpretive limits. Tool-using language agents can perform this integration, but existing task benchmarks rarely test whether a computed claim remains supported by the records used. We present Civic...
  </details>

- **2026-10-31** — Felix Ho, Alexandros Graikos, Dimitris Samaras — [GESTALT: Fast, Generalizable Histopathology Image Synthesis from Gene Expression with Pretrained Pathology Foundation Models](http://arxiv.org/abs/2611.01141v1)
  <details><summary>📄 Abstract</summary>
  Spatial transcriptomics measures gene expression while preserving where each cell sits in the tissue. The inverse, what a given transcriptomic state looks like, is less explored but equally useful: it lets researchers visualize the morphological consequence of a molecular state and interpret a spatial assay's molecular calls against real tissue structure. GeneFlow, the current state of the art on the Xenium gene expression-to-image benchmark, trains a model from scratch, incurring a high cost on...
  </details>

- **2026-10-31** — Jung-Hao Kao, Jing-En Huang, Jia-Wei Liao et al. — [QVR3D: Query-Guided Visual Reasoning for Training-Free 3D Grounding](http://arxiv.org/abs/2611.01084v1)
  <details><summary>📄 Abstract</summary>
  3D visual grounding localizes objects in 3D scenes from natural language descriptions, requiring reasoning over semantics, spatial relationships, and multi-view observations. Training-free approaches avoid costly annotations but often rely on explicit scene transformation or scene-level frame selection, which may waste limited visual capacity on query-irrelevant regions. We observe that effective grounding should prioritize observations that provide evidence for the query rather than uniformly r...
  </details>

- **2026-10-31** — Dipto Sumit, Mahima Mahzabin Sandria, Farig Sadeque et al. — [A Token Is Not a Unit of Difficulty: Segmentation Controls Where Adaptive Computation Goes Inside a Word](http://arxiv.org/abs/2611.00983v1)
  <details><summary>📄 Abstract</summary>
  Early-exit language models decide for each token how much computation to spend, usually by stopping once the prediction is confident. Yet a token is not a fixed unit: tokenizers cut words into different numbers of pieces in different languages. We ask where inside a word such a policy spends its budget. In Qwen3, along two adaptive axes (the timesteps of a spiking conversion and the layers of the original Transformer), confidence stopping gives the continuation pieces of a word less computation ...
  </details>

- **2026-10-30** — Pedro Salomão Quessongo, Daniel Gebbran, Wilhiam de Carvalho et al. — [Risk Assessment of Fair Multi-Period Dynamic Operating Envelopes under Uncertainty](http://arxiv.org/abs/2610.42014v1)
  <details><summary>📄 Abstract</summary>
  Dynamic operating envelopes (DOEs) can allocate time-varying export capacity to distributed energy resources (DERs), and while they are not intended to make operations immune to voltage violations, they should guide operations to mostly remain inside expected values under changing regimes and residual forecast errors. However, although recent literature proposed many different techniques for implementing DOEs, there is sparse discussion of analyzing and quantifying the risk of using more or less...
  </details>

- **2026-10-30** — Bobo Li, Jiajia Song, Hao Fei et al. — [Flide: Accelerating Decision Inference with Exact State Forking](http://arxiv.org/abs/2610.42148v1)
  <details><summary>📄 Abstract</summary>
  Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, we propose Flide, an efficient and exact inference engine that decouples the logical tree structure ...
  </details>

- **2026-10-30** — Artin Yousefi, Aizierjiang Aiersilan, Lorien C Abroms et al. — [Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice](http://arxiv.org/abs/2610.42039v1)
  <details><summary>📄 Abstract</summary>
  Hundreds of millions of people now ask large language model (LLM) chatbots for health advice, which raises a question that is simple to pose and hard to answer: does everyone get the same advice? We audit six widely deployed LLMs from four providers on smoking cessation, a domain with codified clini- cal guidance and substantial public-health stakes, by putting the same four cessation questions to twelve user personas that differ in life stage, self-described expertise, and smoking history, for ...
  </details>

- **2026-10-30** — Wendong Bu, Tinghong Ye, Qizhou Wang et al. — [Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos](http://arxiv.org/abs/2610.41877v1)
  <details><summary>📄 Abstract</summary>
  Scaling humanoid motion foundation models is constrained by the scarcity of diverse, robot-executable data and by the difficulty of jointly learning from heterogeneous multimodal inputs while supporting real-time closed-loop control. We present Movens-5M, constructed from raw Internet videos through clip generation, quality filtering, semantic annotation, motion recovery, and physical refinement with humanoid retargeting and execution verification. It contains 15 million human-motion sequences a...
  </details>

- **2026-10-30** — Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui et al. — [Hierarchical World Models with Implicit Dynamics](http://arxiv.org/abs/2610.42146v1)
  <details><summary>📄 Abstract</summary>
  Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to brittle representations and limited fine-grained control. We introduce ID-WM (Implicit Dynamics World Models), a hierarchical world model that decouples state-space reachability from l...
  </details>

- **2026-10-30** — Kuankuan Cheng, Haocheng Yuan, Changjian Li — [SemEllipsoid: Semantic-aware Shape Abstraction with Ellipsoid](http://arxiv.org/abs/2610.42145v1)
  <details><summary>📄 Abstract</summary>
  Representing 3D shapes using a set of primitives - known as shape abstraction - is an actively studied problem in computer graphics with wide applications in shape understanding, analysis, and simulation due to the compactness and computational efficiency of the primitive-based representation. Prior work has primarily focused on geometry-aware shape abstraction, where the objective is to approximate the input shape with a minimal set of primitives while preserving geometric fidelity. However, th...
  </details>

- **2026-10-30** — Shengguang Wu, Suning Huang, Cherie Ho et al. — [RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory](http://arxiv.org/abs/2610.42141v1)
  <details><summary>📄 Abstract</summary>
  Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises ...
  </details>

- **2026-10-30** — James P. Bailey — [Strategic Tanking in Stable Matching Markets](http://arxiv.org/abs/2610.42105v1)
  <details><summary>📄 Abstract</summary>
  Motivated by a broad literature in psychology, organizational behavior, and matching markets, we introduce strategic tanking: an agent deliberately makes themselves less attractive to selected potential partners in order to improve their eventual assignment. Unlike traditional manipulation in stable matching, a tanker does not misreport whom they prefer; instead, they influence how others rank them. We show that tanking has a striking connection to classical preference manipulation. Cutoff tanki...
  </details>

- **2026-10-30** — Jiaming Wang — [SketchMate: Agentic Geometric Reasoning for Zero-Shot Precision Insertion](http://arxiv.org/abs/2610.41844v1)
  <details><summary>📄 Abstract</summary>
  Inserting an unseen part requires sub-millimetre precision and the correct orientation of keyed features. Current zero-shot agentic manipulation methods built on vision-language models (VLMs) produce spatial outputs that are far too coarse for this. We propose to let a VLM build a sketch model of the task, i.e., a few geometric primitives and two mate frames, which a VLM agent measures with geometric tools in multi-view depth and which a standard planner and compliant controller execute. Because...
  </details>

- **2026-10-30** — Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee et al. — [Latent Reasoning in Continuous Space for Unified Multimodal Models](http://arxiv.org/abs/2610.42149v1)
  <details><summary>📄 Abstract</summary>
  Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space,...
  </details>

- **2026-10-30** — Yanming Zhang, Eric Papenhausen, Klaus Mueller — [CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning](http://arxiv.org/abs/2610.42028v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning is a powerful paradigm for training autonomous agents and has achieved impressive performance in complex environments. However, this success often comes at the cost of interpretability, diminishing trust and complicating efforts to debug and improve agent behavior. To address these challenges, we introduce CausalXRL, a novel framework for explainable reinforcement learning (XRL). A key feature of CausalXRL is its use of causal graph reasoning, which provides transparent, s...
  </details>

- **2026-10-30** — Hanyu Yang — [Less Loss, Fixed Weights: Logit Corrections for Forgetting](http://arxiv.org/abs/2610.42000v1)
  <details><summary>📄 Abstract</summary>
  When a language model is fine-tuned to follow instructions, or further pretrained on a new subject, it often gets worse at predicting standard web text. This is known as "forgetting." We ask whether this loss can be undone by simple, fixed adjustments to the model's final token predictions. Across 14 pairs of base and derived models, from 1B to 7B parameters, we fitted a fixed bonus or penalty for each token (a vocabulary bias), alone or together with a temperature. On text held out from correct...
  </details>

- **2026-10-30** — Nicolò Pagan, Michael Andreas Ebling, Stefania Ionescu et al. — [AI evaluators favor job applications written by certain AI models, independent of candidate quality](http://arxiv.org/abs/2610.41866v1)
  <details><summary>📄 Abstract</summary>
  Job applicants increasingly use large language models (LLMs) to write cover letters, while employers deploy LLMs to screen them. In this all-AI setting, we ask whether the \emph{choice of model} affects hiring outcomes independently of candidate qualifications. We introduce a multi-model auditing framework pairing eleven LLM writer agents with nine API-hosted evaluator agents across ten job descriptions and fifty candidates per job. Four findings emerge. First, we identify a generative preferenc...
  </details>

- **2026-10-30** — Van Bach Nguyen, Qianli Wang, Nils Feldhus et al. — [SimXAI: A Simple Drop-in Layer Increases Interaction Quality and Understanding in Conversational XAI](http://arxiv.org/abs/2610.41856v1)
  <details><summary>📄 Abstract</summary>
  Conversational explainable AI (ConvXAI) agents often use GUS-style architectures with separate modules for intent recognition, dialogue management, and template-based response generation. While faithful to the underlying XAI methods, these pipelines are hard to adapt and often struggle with context-dependent follow-up questions. We present SimXAI, a lightweight LLM-centric conversational layer that replaces these modules with a single tool-calling LLM that bridges access to existing XAI resource...
  </details>

- **2026-10-30** — Hanqiao Ye, Yuzhou Liu, Mengqi Rong et al. — [PGGT-Loc: Primitive-Grounded Geometry Transformer for Feed-Forward Camera Localization](http://arxiv.org/abs/2610.41833v1)
  <details><summary>📄 Abstract</summary>
  Camera localization methods are mostly multi-stage pipelines relying on dedicated and complex maps that are costly to construct, store, and maintain over time. Alternatively, well-structured maps that organize scenes with compact yet expressive primitives are often readily available, providing rich structural and semantic cues that humans can interpret. However, their potential for direct camera localization remains largely unexplored due to the significant modality gap between map primitives an...
  </details>

- **2026-10-30** — Zixiong Wang, Haiping Ma — [A Patch is More Than a Token](http://arxiv.org/abs/2610.41814v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers represent each image patch through a canonical token produced under one observation condition. That token is a powerful interface, but it is still one realized state of the patch. We introduce PMTT, which establishes two foundations: a patch representation object can extend from one canonical state to a canonical-centered Representation State Family, and identity-preserving variation opens Patch-Level Local Feature Space. We develop four parts of this representation program. ...
  </details>

- **2026-10-30** — Guy Binderman, Amir Boag — [Wideband Near- and Far-Field Double-Bounce Physical Optics via Co-Area Range Profile Extraction](http://arxiv.org/abs/2610.41812v1)
  <details><summary>📄 Abstract</summary>
  Wideband evaluation of the Radar Cross Section (RCS) and the underlying range profile of a target, including its secondary double-bounce fields, remains a computational bottleneck even for modern high-frequency solvers. This paper presents a framework for evaluating the wideband range profile under the Physical Optics (PO) approximation without repeated frequency-domain iterations. Using phase level-set integration via the Co-Area formula, we project the single- and double-bounce scattered field...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 705 |
| prompt-injection | 657 |
| memory-poisoning | 57 |
| tool-use-attack | 169 |
| backdoor | 548 |
| adversarial-attack | 660 |
| privacy-leakage | 4513 |
| steganography | 90 |
| misuse | 1279 |
| red-teaming | 145 |
| vulnerability | 3856 |
| defense | 3747 |
| alignment | 3518 |
| robustness | 3821 |
| watermark | 695 |
| unlearning | 119 |
| agent-safety | 66 |
| benchmark | 73 |
| survey | 436 |
| other | 10377 |

---

📚 **全部 35531 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-11-03 22:47:48*