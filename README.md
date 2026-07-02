<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-167-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-02 18:32 ｜ **论文总数 / Total Papers**: 167

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 1
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 5
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 2
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 4
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 5
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 3
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 10
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 2
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 3
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 31
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 20
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 22
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 4
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 1
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 3
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 51

## 📂 jailbreak
*越狱攻击 / Jailbreak Attacks*

### [Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](http://arxiv.org/abs/2606.31227v1)

- **arXiv ID**: `2606.31227v1`
- **作者 / Authors**: Yong Yang, Xing Zheng, Huiyu Wu, Huangsheng Cheng, Xiaorong Shi et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

The fast growth of open-source AI infrastructure, from model serving engines and agent platforms to the Model Context Protocol (MCP) ecosystem and the language models themselves, has outpaced the security tooling available to defend it. We present AI-Infra-Guard, an open-source framework that organizes AI red teaming around a single observation: the attack surface of an AI agent is stratified across layers (infrastructure, protocol/tool, agent behavior, and model), and no single detection paradigm fits all of them. The framework therefore matches a paradigm to each layer, from deterministic rule matching over 75+ AI components and 1{,}400+ vulnerability rules, through LLM-driven agentic auditing of MCP servers and agent-skill packages and multi-turn black-box agent red teaming, to a jailbreak harness with 26+ attack operators over sixteen datasets. To our knowledge it is the only open-source framework to span all of these, including supply-chain auditing of the agent skills that increasingly extend AI agents. We release AI-Infra-Guard as open source so that \emph{layer-paradigm matching} can serve as a practical foundation for agent security and a shared base for the community to build on.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31227v1) | [PDF](https://arxiv.org/pdf/2606.31227v1)

## 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks*

### [Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity](http://arxiv.org/abs/2607.01153v1)

- **arXiv ID**: `2607.01153v1`
- **作者 / Authors**: Brett Reynolds
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Safety evaluations for language models increasingly depend on judgments about ambiguous natural-language behaviour: whether a model has followed an instruction, refused appropriately, complied with a policy, resisted an embedded command, or misreported progress in an agentic task. Existing benchmarks often compress these distinctions into pass/fail labels, obscuring whether failures arise from capability limits, policy ambiguity, instruction conflict, scaffold failure, or unstable evaluator judgments.   This paper introduces adversarial pragmatics as a benchmark and annotation protocol for evaluating model behaviour under instruction conflict, embedded commands, quotation, scope ambiguity, deixis, indirect speech acts, and multi-turn agent transcripts. The contribution is empirical and methodological: a linguistically controlled taxonomy, an 18-item seed benchmark with validator-enforced metadata, a 54-row local seed pilot, an expert-evaluation protocol distinguishing task success, policy compliance, safety risk, refusal outcome, and evaluator confidence, and metrics for judge validity, diagnostic ambiguity, and taxonomy drift. The framework turns linguistic judgment methodology into a practical tool for validating safety evals, LLM judges, gold-set construction, prompt-injection tests, and safety documentation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01153v1) | [PDF](https://arxiv.org/pdf/2607.01153v1)

### [Understanding and Evaluating Claw-like Agent Security Through a Computer-Systems Lens](http://arxiv.org/abs/2606.30755v1)

- **arXiv ID**: `2606.30755v1`
- **作者 / Authors**: Peizhi Niu, Wenjie Qu, Shangding Gu, Tianneng Shi, Yuankai Li et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Claw-like AI agents (e.g., OpenClaw) are always-on processes with persistent access to credentials, files, tools, and external services. They take on system-level responsibilities -- installing packages, maintaining state, scheduling subtasks, and mediating I/O -- making security failures far more severe than in other agents. Yet existing benchmarks focus on model responses and tool calls, leaving cross-component failure modes largely unmeasured. We adopt a computer-system analogy: treating a Claw-like agent as an agentic computer system whose gateway runtime plays an OS-like mediation role, whose Skills resemble user-installed applications, and whose Plugins resemble loadable extensions with runtime privileges. Each component has a classical counterpart whose protection mechanisms -- refined over decades of cybersecurity research -- are absent on the agent side. From this perspective, we develop SafeClawArena, a benchmark of 406 adversarial tasks across four attack surfaces (Skill Supply-Chain Integrity, Persistent State Exploitation, Cross-Boundary Data Flow, and Indirect Prompt Injection), executed in containerized replicas of real agent platforms with canary-marked credentials and evaluated via automated taint tracking across nine output channels. We evaluate three platforms (OpenClaw, NemoClaw, SeClaw) and five frontier LLMs. The highest attack success rate reaches 70%; malicious Plugins succeed in 100% of cases regardless of the LLM. SeClaw cuts GPT-5.4's attack success rate from 70% to 22%, partly through utility-security tradeoffs rather than active defenses, while Claude-Opus-4.6 already sits near a 22% floor on every platform. These results expose the inadequacy of current defenses and suggest directions for future hardening. Code and data: https://github.com/sunblaze-ucb/SafeClawArena.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30755v1) | [PDF](https://arxiv.org/pdf/2606.30755v1)

### [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](http://arxiv.org/abs/2606.30566v1)

- **arXiv ID**: `2606.30566v1`
- **作者 / Authors**: Jun Wen Leong
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

We discover a behavioral invariant in LLM agents under persistent memory poisoning: in architectures where routing information is retrieved through observable memory-tool invocations, successful attacks require calling memory_recall_fact before email_send_email, a transition that non-exfiltrating sessions rarely exhibit. Under the evaluated architecture, this invariant follows from the attack's information-retrieval dependency rather than being merely an empirical correlation, and suppressing it breaks the attack. A simple rule exploiting this invariant alone achieves AUC = 0.9563. A Random Forest classifier over 19 trajectory features refines it to AUC = 0.9904 (BCa 95% CI [0.987, 0.993], N=10,000 resamples), demonstrating that the attack imprints on multiple independent behavioral channels. The signature is overdetermined: removing all recall-related features (half the feature set) leaves AUC unchanged at 0.990, confirming that memory poisoning induces a distributed trajectory signature rather than a single observable anomaly. Cross-model hold-out on 9 models (7B-120B parameters) confirms AUC = 1.000 on 6/9 hold-out splits, with all three exceptions mechanistically explained. The invariant generalizes to frontier models (GPT-4.1, GPT-4o) without retraining. A strictly prefix-only variant achieves AUC = 0.934, suggesting that real-time blocking is feasible with moderate degradation. The boundary is forensically useful: prompt-injection attacks that bypass memory produce a distinct trajectory (score = 0.541), enabling incident responders to distinguish memory-channel attacks from prompt-injection attacks using tool-call logs alone.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30566v1) | [PDF](https://arxiv.org/pdf/2606.30566v1)

### [Agent Security Meets Regulatory Reality -- A Practitioner Systematization of Autonomous-Agent Threats and Controls in Regulated Financial Systems](http://arxiv.org/abs/2606.29142v1)

- **arXiv ID**: `2606.29142v1`
- **作者 / Authors**: Krishna Mohan, Guda Nagavenkata Srinivasa
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.CY

<details>
<summary>📝 Abstract</summary>

Large language model agents are entering regulated financial systems, yet the security literature characterizing their attack surface is almost entirely laboratory-based, and the practitioner guidance on regulated deployment is neither peer-reviewed nor connected to a formal threat model. We bridge the two from production experience. We map six established agentic threat categories namely prompt injection, identity and authorization, action auditability, tool abuse, data residency, and boundary policy enforcement onto the specific control obligations imposed by the US and the EU financial regulation (ECOA and Regulation B, the EU AI Act, GDPR Article 22, and FINRA's 2026 agent guidance), showing how legal accountability amplifies each threat relative to an unregulated deployment. We then document four architectural patterns from a production Know Your Customer deployment for a consumer credit product (A2A compliance choreography, grounded-RAG-for-audit, case-ID propagation, and an inference-boundary redaction proxy) that moved a multi-day manual process to same-day automated resolution for roughly four in five cases. Finally, we report three negative results, including two control failures surfaced only by internal audit and a population of legitimate applicants the automated pipeline cannot serve. Securing agents under regulation, we conclude, is less about novel attack classes than about making auditability, least-privilege authorization, and boundary policy enforcement real at production scale -- requirements current agent frameworks leave to the deploying engineer.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29142v1) | [PDF](https://arxiv.org/pdf/2606.29142v1)

### [From Determinism to Delegation: AI-Native Software Engineering and the Evolution of the Agentic Engineer](http://arxiv.org/abs/2606.28791v1)

- **arXiv ID**: `2606.28791v1`
- **作者 / Authors**: Mamdouh Alenezi
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Software engineering is experiencing its most significant transformation since the emergence of high-level programming languages. As large language models (LLMs) increasingly enable sustained, multi-step, tool-mediated execution, engineering value is shifting from writing deterministic code to supervising probabilistic and autonomous behavior. This paper argues that AI-Native Software Engineering is a paradigm shift rather than a mere tooling advance, creating a new professional archetype: the Agentic Engineer, whose primary artifact is the agentic system rather than the program.   We characterize this transition through three changes: (i) the unit of work shifts from functions to supervised agent workflows, (ii) correctness shifts from binary assertions to statistical evaluation under uncertainty, and (iii) accountability shifts from code authorship to outcome ownership. Drawing on post-2022 research, we compare traditional and agentic engineering roles and define core mechanisms of autonomous agents, including reasoning-acting loops, context engineering, tool use, memory, behavioral drift, and compositional error.   We place human-AI collaboration within socio-technical frameworks and examine mixed empirical evidence. While some studies report productivity gains, others show slowdowns among experienced developers, highlighting disciplined oversight rather than automation as the critical competency. Using established governance frameworks, we identify required skills and risks, including indirect prompt injection. We conclude that the future is one of symbiosis rather than substitution: agentic engineering builds upon and depends on classical software engineering principles.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28791v1) | [PDF](https://arxiv.org/pdf/2606.28791v1)

## 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering*

### [Memory as an Attack Surface in LLM Agents: A Study on Multiple-Choice Question Answering](http://arxiv.org/abs/2606.29030v1)

- **arXiv ID**: `2606.29030v1`
- **作者 / Authors**: Shahnewaz Karim Sakib, Anindya Bijoy Das
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

AI agents extend conventional large language model (LLM) applications by integrating language understanding with task execution, external tool use, and memory mechanisms. While memory allows agents to retain prior interactions and provide more personalized and context-aware responses, it also introduces a new vulnerability: information stored in memory can influence future outputs even when the current query is clean. In this paper, we investigate memory manipulation in LLM-based agents for multiple-choice question answering. We first design and implement an LLM-based AI agent with an external memory component that stores and retrieves task-relevant information. We then introduce basic memory manipulation scenarios in which misleading or corrupted memories are inserted into the agent before it answers multiple-choice questions. Using a controlled experimental setup, we compare the agent's performance before and after memory manipulation and measure changes in answer accuracy, attack success rate, and selection of manipulated options. Our results show that even simple memory manipulations can noticeably affect the agent's final answers, causing it to select incorrect options despite receiving clean and well-formed questions.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29030v1) | [PDF](https://arxiv.org/pdf/2606.29030v1)

### [Agent-Native Immune System: Architecture, Taxonomy, and Engineering](http://arxiv.org/abs/2606.28270v1)

- **arXiv ID**: `2606.28270v1`
- **作者 / Authors**: Bo Shen, Lifeng Chang, Tianyuan Wei, Yunpeng Li, Feng Shi et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI threat landscape. Current defense mechanisms, such as perimeter security and training-time alignment, remain external to the agent's active reasoning loop. Consequently, they fall short: a fully aligned agent remains highly vulnerable to runtime hijacking via memory poisoning, tool-chain manipulation, or multi-agent protocol attacks. To address this critical gap, we introduce the Agent-Native Immune System (ANIS), the first biologically inspired, endogenous defense architecture embedded directly within the agent's cognitive loop. Our framework presents four primary contributions. First, we design a six-layer Immune Tower (L0-L5), distinctly incorporating Barrier Immunity (L1) as a non-cognitive, physical-and-logical isolation layer. Second, we establish a unified taxonomy of Agent Viruses and Agent Vaccines, formalizing the critical distinction between superficial non-parametric defenses and robust parametric vaccines. Third, we conceptualize the Harness Triad--Meta, Self, and Auto--a self-monitoring, meta-cognitive automation backbone that drives Continual Immune Learning (CIL), enabling vaccines to dynamically adapt to novel threats. Finally, we establish a rigorous theoretical demarcation between model alignment and agent immunity: while alignment provides a static "constitutional" value foundation during training, ANIS serves as the dynamic "law enforcement" mechanism during runtime. We conclude by framing open challenges for the field, including immune protocol standardization, novel evaluation metrics such as the Autoimmunity Rate (false-positive intervention rate), and the co-evolutionary dynamics between pathogens and vaccines within collective intelligence ecosystems.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28270v1) | [PDF](https://arxiv.org/pdf/2606.28270v1)

## 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks*

### [Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply Chains](http://arxiv.org/abs/2607.01136v1)

- **arXiv ID**: `2607.01136v1`
- **作者 / Authors**: Changguo Jia, Tianqi Zhao, Runzhi He, Minghui Zhou
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Agent skills package reusable operational knowledge for Large Language Model (LLM) agents, yet as they grow in scope, they become dependency-bearing artifacts whose identities, versions, and provenance remain implicit. This opacity already causes duplicated dependencies and inconsistent installations, exposing a gap that dependency management has yet to close. We introduce Agent Skill Supply Chains (ASSCs) to characterize mixed skill-package-service dependency graphs and help close this gap. Borrowing from Software Bill of Materials (SBOMs), we design SkillDepAnalyzer to capture natural-language dependency evidence and model skills as dependency-bearing artifacts. On the SKILL-DEP benchmark, SkillDepAnalyzer recovers skill metadata and dependency graphs accurately and comprehensively, substantially outperforming an LLM-based baseline and package-centric SBOM tools. Applying SkillDepAnalyzer to over 1.43 million skills, we obtain ASSCs and explore their structural diversity and security signals. We find four structural patterns: skill metadata is activation-ready but governance-poor; dependency graphs span skill, package, and service dependencies with concentrated reuse; recursive skill reuse expands dependency graphs and creates hidden package inventory; and skill dependency clusters form around related workflows. We also find that inspecting a skill alone misses security-relevant signals hiding in its dependencies. By analyzing ASSCs, we identify and report known malicious skills persisting in ASSCs to their developers. Based on these findings, we recommend typed dependency manifests, first-class dependency-cluster management, risk-warning audit commands for skill infrastructure maintainers, and lockfile-like records for skill developers.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01136v1) | [PDF](https://arxiv.org/pdf/2607.01136v1)

### [The Decomposition Is the Fingerprint: Per-Component Identity for Agent Skills](http://arxiv.org/abs/2606.31272v1)

- **arXiv ID**: `2606.31272v1`
- **作者 / Authors**: Hongliang Liu, Yuhao Wu, Tung-Ling Li
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

AI agents increasingly acquire and execute skills at runtime: bundles of prompt instructions, executable code, and tool declarations fetched from marketplaces and other agents. Governing them needs a stable notion of skill identity, yet cryptographic hashing is engineered to destroy the very similarity we need, as a one-character edit scrambles the digest. We present a compact, locality-sensitive fingerprint that embeds each component of a skill and projects it to bits with a multi-bank SimHash, giving a fixed 120-byte signature compared in constant time by Hamming distance. Our central claim is that keeping the fingerprint as a per-component triple (prompt, code, tools), rather than a single score, is what makes it useful: the triple recovers skill-family identity through paraphrase, renaming, refactoring, and controlled code translation when another component remains shared, while independent multilingual reimplementation is not recovered; it also localizes which component carries the reuse. We claim lineage, not behavioral equivalence: identity supplies the structural axis of a registry and leaves safety to behavioral verification. The fingerprint reaches an area under the ROC curve (AUC) of 0.974 (95% CI [0.956, 0.994]) over 4,950 pairwise comparisons while using 77x fewer bits than the embedding it approximates, with ranking preserved in expectation and finite-bit concentration; the per-component split turns one number into relationship classification, families, novelty, and a portable "SkillBOM" for a skill registry. On a 906-skill injection benchmark the fingerprint recognizes injected skills as tampered copies of a known base and localizes the change, but recognition is not trust: it remains, by design, an identity signal complementary to behavioral verification rather than a safety verdict.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31272v1) | [PDF](https://arxiv.org/pdf/2606.31272v1)

### [Entity Binding Failures in Tool-Augmented Agents](http://arxiv.org/abs/2606.30531v1)

- **arXiv ID**: `2606.30531v1`
- **作者 / Authors**: Rahul Suresh Babu, Shashank Indukuri
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task. However, an agent may choose the right tool and still act on the wrong external entity. For example, a request to "email Alex about the launch" may lead the agent to contact the wrong Alex, attach the wrong launch document, reply in the wrong thread, or update the wrong customer account. We call these errors entity binding failures. This paper studies entity binding failures as a distinct reliability and safety problem in tool-augmented agents. We formalize the separation between tool correctness and entity correctness, introduce a taxonomy of wrong-entity failures in enterprise workflows, and evaluate entity-aware execution mechanisms including entity-resolution preconditions, confidence-gated binding, clarification under ambiguity, and provenance tracking. In a controlled diagnostic evaluation across 60 tasks, five model backends, and six tool-use methods, all methods achieved 0.0 percent wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0-26.0 percent of runs. Entity-aware methods eliminated wrong-entity actions and risk-weighted wrong-entity exposure in this setting, but reduced direct task completion by deferring under ambiguity. These findings show that safe tool use requires not only selecting the correct tool, but also reliably binding natural-language references to the correct real-world entity before action.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30531v1) | [PDF](https://arxiv.org/pdf/2606.30531v1)

### [Symbolon: Symbolic Execution by Learning Code Transformation](http://arxiv.org/abs/2606.29108v1)

- **arXiv ID**: `2606.29108v1`
- **作者 / Authors**: Jie Zhu, Penghui Li, Zhongxuan Li, Chihao Shen, Ziyang Li et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Symbolic execution is a powerful program analysis technique with broad applications, such as vulnerability detection, security testing, and malware analysis. However, this technique is known to suffer from scalability issues, e.g., path explosion, complex constraints, due to certain structural and semantic patterns commonly presented in real-world programs. Existing approaches attempt to escape these patterns by transforming programs into new representations to reduce the execution cost. Unfortunately, these transformations are often too rigid to exploit diverse local program semantics and sometimes rely on compiler optimizations designed for concrete execution that may misalign with the goals of symbolic execution.   We present Symbolon, a framework that automatically learns diverse code transformations and applies them context-sensitively to improve symbolic execution. Our key insight is to formulate transformation discovery as a search problem over program representations. To make the search practical, Symbolon learns transformations cheaply offline on small programs, distills them into a reusable library of agent skills, and uses an agent to instantiate these skills on repo-level targets. Our evaluation shows that Symbolon substantially improves the symbolic execution engine KLEE across 16 search strategies on 32 real-world programs, increasing line coverage by 3.69x on average while reducing peak memory and per-query solver time by 29.2x and 123x, respectively. When applied to the latest Linux kernel, Symbolon uncovers 21 previously unknown bugs, all of which have been reported to the kernel maintainers.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29108v1) | [PDF](https://arxiv.org/pdf/2606.29108v1)

## 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks*

### [KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2607.00422v1)

- **arXiv ID**: `2607.00422v1`
- **作者 / Authors**: Chanwoo Choi, Euntae Kim, Kyuho Lee, Youngsam Chun, Jinhee Jeong et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Retrieval-Augmented Generation (RAG) systems are vulnerable to poisoning attacks that inject malicious documents into the retrieval process to manipulate model outputs. Recent Agentic RAG systems are more robust to such attacks because they iteratively perform retrieval and reasoning, allowing them to ignore weakly relevant poisoned documents and preserve the reasoning chain induced by the user query. However, existing attacks on Agentic RAG systems often assume white-box access to system prompts, reasoning traces, retrievers, or model parameters, limiting their applicability in realistic settings. In this paper, we study black-box poisoning attacks against Agentic RAG systems, where the attacker can only publish externally retrievable poisoned documents. We propose KidnapRAG, a sequential poisoning attack that hijacks the agent's multi-step reasoning chain using three role-specific documents: Bait, Chain-Link, and Mal-Ins, which attract initial retrieval, induce query reformulation, and provide attacker-controlled evidence, respectively. Experiments across multiple Agentic RAG frameworks, LLM backbones, and benchmarks show that KidnapRAG consistently outperforms existing poisoning baselines under black-box conditions. Further analyses show that KidnapRAG progressively weakens the original retrieval intent, redirects retrieval behavior, and increases reliance on attacker-controlled evidence. Our code is publicly available at https://github.com/chanwoochoi316/KidnapRAG.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00422v1) | [PDF](https://arxiv.org/pdf/2607.00422v1)

### [Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing](http://arxiv.org/abs/2606.30555v1)

- **arXiv ID**: `2606.30555v1`
- **作者 / Authors**: Dvir Alsheich, Adar Peleg, Ben Hagag, Rom Himelstein, Amit Levi et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

The rapid integration of Large Language Models (LLMs) has driven the evolution of Multi-Agent Systems (MAS), where specialized agents collaborate to execute complex workflows. Effective orchestration in these environments requires robust routing mechanisms to efficiently allocate tasks to the most suitable agent. However, existing routers fundamentally rely on unverified proxies, ranging from textual self-descriptions to static surrogate representations, to gauge an agent's competence. This reliance on non-empirical data creates a critical gap between an agent's projected profile and its actual operational capabilities, introducing severe security vulnerabilities. Malicious agents can easily misrepresent their proficiencies or harbor covert backdoors that evade both standard external analysis and static representation-learning techniques. In this work, we introduce ANTAP (Automatic Non-Textual Agent Picker), an evaluation-driven routing architecture that discards indirect proxies in favor of active capability testing. By dynamically querying agents to ascertain their true competencies empirically, ANTAP distills performance into fixed behavioral operators within a shared semantic space. At inference time, routing is performed via a purely non-textual algebraic projection, establishing a "linguistic firewall" that renders metadata-based attacks inexpressible. In our experiments, ANTAP achieves near-zero ASR against description-based injection attacks, compared to 67.3\% and above for the description-based router baseline. Against adaptive embedding attacks, ANTAP achieves substantially lower ASR than the embedding-based baseline, with a 20\% reduction, while remaining resilient to description manipulation by design.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30555v1) | [PDF](https://arxiv.org/pdf/2606.30555v1)

### [Fuzzing Large Language Models to Elicit Hidden Behaviours](http://arxiv.org/abs/2606.29646v1)

- **arXiv ID**: `2606.29646v1`
- **作者 / Authors**: Mohammed Abu Baker, Lakshmi Babu-Saheer
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Sleeper agents are the canonical model organism of deception: models trained to behave normally but to emit an unsafe behaviour on a specific trigger. Eliciting that behaviour without knowing the trigger has not been studied systematically. We study fuzzing: injecting Gaussian noise into a model's weights or residual-stream activations and checking whether the perturbed outputs reveal the behaviour. On 6 backdoored models (7B-13B) we compare both forms of fuzzing head-to-head against temperature-sampling baselines. Fuzzing elicits the hidden behaviour more often than temperature sampling on 4 of 6 models (up to ~6x on OpenHermes-13B), and which form wins depends on the task, so both are worth running. Elicitation is uneven across each method's hyperparameter grid: a uniform sweep gives only a few percent on most models, while the best cell is 2-10x higher, so the bottleneck is hyperparameter selection, not the technique. To select hyperparameters without ground-truth access, we use a cheap proxy task (in-context secret elicitation, where a base64-encoded secret is placed in the system prompt for the model to hide) and run Thompson sampling on it to pick candidate cells, which we evaluate on the real backdoor. On the four models that can decode the secret, proxy-selected cells raise activation-fuzzing elicitation ~4x over the uniform-sweep mean (recovering ~70% of the best-cell rate on the best performing model) and weight-fuzzing by 1.3-1.8x. To our knowledge this is the first systematic study of fuzzing on sleeper-agent backdoors and the first to show proxy-task hyperparameter selection transferring to real-task elicitation. We also propose reporting such results as a (uniform-baseline, proxy-selected, oracle) triple, since these are three distinct claims that prior work has often blurred.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29646v1) | [PDF](https://arxiv.org/pdf/2606.29646v1)

### [Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare](http://arxiv.org/abs/2606.28666v1)

- **arXiv ID**: `2606.28666v1`
- **作者 / Authors**: Liam Kearns
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Agent-based AI has enabled the automation of tasks by exposing application tools and resources to large language models (LLMs). However, to improve scope and accuracy, agents are often given access rights that exceed those of ordinary users, introducing significant security risks. AI is routinely integrated into applications with a disregard to security, risking data exposure and breaching regulations. This paper applies the AI Trust, Risk, and Security Management (TRiSM) framework to a medical report-generation application to demonstrate how an insecure agent workflow can be transformed into security-conscious agentic workflow. Both workflows were evaluated across five LLMs (Claude Haiku 4.5, GPT-4.1-nano, GPT-4.1-mini, GPT-5.4-mini, and Gemini 2.5 Flash) on two report types, totalling 800 generations and 500 attack scenarios including RAG poisoning, data-field injection, and client-side network injection. The TRiSM-guided agentic workflow reduced mean attack success rates from 31% to 10% for RAG poisoning and from 42% to 25% for data-field injection, while eliminating the network injection vector entirely through server-side prompt construction. Furthermore, report accuracy increased by 14 percentage points (72.5% to 86.5%) with the agentic workflow, demonstrating a secure design which provides more reliable outputs. This paper contributes to knowledge by demonstrating least-privilege, defence in depth agentic workflows improving security and accuracy, while also highlighting model choice is a necessary architectural consideration.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28666v1) | [PDF](https://arxiv.org/pdf/2606.28666v1)

### [ToE: A Hierarchical and Explainable Claim Verification Framework with Dynamic Multi-source Evidence Retrieval and Aggregation](http://arxiv.org/abs/2606.27736v1)

- **arXiv ID**: `2606.27736v1`
- **作者 / Authors**: Zhaoqi Wang, Zijian Zhang, Kun Zheng, Zhen Li, Xin Li et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

The rapid spread of fake news poses increasing threats to information ecosystems, especially as AI-generated misinformation under Generative Engine Optimization (GEO) poisoning allows adversarially crafted content to be systematically surfaced by retrieval systems, contaminating LLM reasoning. In this paper, we propose Tree of Evidence (ToE), a hierarchical evidence reasoning framework for automated fact-checking that models each claim as a dynamically expanding argument tree. ToE integrates a reinforcement learning-driven multi-source retrieval agent, an evidence evaluation agent, and an argument tree aggregation algorithm to iteratively decompose, retrieve, and verify claims through an explainable evidence chain. We further provide a theoretical analysis of the retrieval process, deriving a formal error bound that guarantees the learned policy converges to a neighborhood of the information-theoretically optimal policy. Experiments across multiple datasets and backbone LLMs demonstrate that ToE achieves improvements ranging from 4 to 24 percentage points over competitive baselines, with particularly pronounced gains on adversarially poisoned inputs.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27736v1) | [PDF](https://arxiv.org/pdf/2606.27736v1)

## 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks*

### [RoAd-RL: A Unified Library and Benchmark for Robust Adversarial Reinforcement Learning](http://arxiv.org/abs/2606.29867v1)

- **arXiv ID**: `2606.29867v1`
- **作者 / Authors**: Adithya Mohan, Daniel Kriegl, Torsten Schön
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Deep Reinforcement Learning (DRL) has achieved significant success in robotics and autonomous systems, yet remains vulnerable to adversarial perturbations that can severely degrade performance. Research in adversarial reinforcement learning is often limited by fragmented implementations, inconsistent evaluation protocols, and poor reproducibility. To address these challenges, we present \textbf{RoAd-RL}, an open-source benchmarking framework that provides unified abstractions for policies, attacks, defenses, and robustness metrics, together with reproducible evaluation pipelines and seamless integration with Stable-Baselines3 and Gymnasium.   We evaluate DQN, PPO, and SAC agents in LunarLander and Highway-v0 under 192 attack-defense configurations. Results reveal substantial variations in robustness across environments and show that some commonly used defenses can be more detrimental than the attacks they aim to mitigate, while temporal smoothing consistently achieves strong performance. RoAd-RL establishes a standardized benchmark for adversarial reinforcement learning research and is publicly available at https://pypi.org/project/road-rl.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29867v1) | [PDF](https://arxiv.org/pdf/2606.29867v1)

### [Proteus: Automated Adversarial Robustness Testing for Audio Deepfake Detectors](http://arxiv.org/abs/2606.29544v1)

- **arXiv ID**: `2606.29544v1`
- **作者 / Authors**: Nicolas M. Müller, Aditya Tirumala Bukkapatnam, Zohaib Ahmed
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.SD

<details>
<summary>📝 Abstract</summary>

We present Proteus, a framework developed at Resemble AI for automated robustness testing of our audio deepfake detection system. Given a detector, Proteus systematically searches over sequences of everyday audio transformations (codec transcoding, additive noise, reverberation, dynamic-range compression, and VoIP simulation) to find combinations that fool the detector while preserving speech quality. We propose two complementary search strategies: (1) a breadth-first search that exhaustively maps augmentation effectiveness across the parameter space, and (2) a Q-learning agent designed to efficiently discover deeper attack chains by exploiting structural patterns in the BFS data. We report findings from continuous deployment of Proteus against our production detector, showing that specific augmentation chains can reliably flip detection verdicts while preserving speech intelligibility and speaker identity. We discuss how these findings are used to harden the detector through targeted retraining.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29544v1) | [PDF](https://arxiv.org/pdf/2606.29544v1)

### [Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety](http://arxiv.org/abs/2606.27632v1)

- **arXiv ID**: `2606.27632v1`
- **作者 / Authors**: Ting Ma, Xiufeng Huang, Benlei Cui, Xiaowen Xu, Shikai Qiu et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

As large language models are increasingly deployed in real-world systems, safety failures can still lead to harmful outputs and dangerous misuse. We argue that the essence of safety is adversarial: many failures arise not from natural inputs alone, but from strategic attempts to evade model policies and safeguards. However, existing general-purpose model development largely overlook this adversarial nature, and often remain insufficient for realistic safety scenarios involving planning, tool use, and multi-step reasoning, causing measured safety performance to overestimate real deployment robustness. To address this gap, we present Yuvion LLM, a large language model built for adversarially robust content safety and broader AI safety. Yuvion LLM treats adversarial robustness and agentic capability as first-class objectives. Its pipeline combines adversarially aware data construction, knowledge-enhanced continued pretraining, and policy-grounded multi-task safety post-training, including risk-aware supervised fine-tuning and reinforcement learning-based policy optimization, together with safety-aware agentic reinforcement learning for tool use and multi-step reasoning in complex safety scenarios. We further introduce the Yuvion LLM RiskEval (YLRE), a collection of 93 benchmarks across four evaluation categories, covering diverse open and internal evaluations with a focus on safety, adversarial robustness, and real-world capability requirements. Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability. Notably, Yuvion-8B outperforms most state-of-the-art baselines, including substantially larger models such as GPT-5.4 and Qwen3-MAX, on several safety tasks.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27632v1) | [PDF](https://arxiv.org/pdf/2606.27632v1)

## 📂 privacy-leakage
*隐私泄露 / Privacy Leakage*

### [LLM-Guided ODE Discovery and Parameter Inference from Small-Cohort Aggregate Data](http://arxiv.org/abs/2607.00733v1)

- **arXiv ID**: `2607.00733v1`
- **作者 / Authors**: Hanning Yang, Meropi Karakioulaki, Lennart Purucker, Tim Litwin, Cristina Has et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Mechanistic modeling via ordinary differential equations (ODEs) provides interpretable descriptions of complex dynamics and enables inference of underlying mechanisms, which is particularly valuable in clinical settings. However, in rare diseases, both the structure and parameters of the model are typically unknown, while individual-level data is scarce, noisy, heterogeneous, and subject to privacy constraints. In such settings, population-level summary statistics provide a practical privacy-preserving data representation, while capturing heterogeneity further requires modeling parameters as distributions rather than fixed values. Yet no existing method jointly discovers ODE structure and refines parameter distributions solely from summary statistics. We present AgentODE, an end-to-end framework that addresses this gap. An LLM proposes candidate ODE structures, while a tool-augmented inference agent iteratively refines parameter distributions through a diagnosis--update loop, operating on population-level summary statistics alone. We evaluate AgentODE on three benchmark problems across different fields and two clinical datasets, including the rare disease recessive dystrophic epidermolysis bullosa (RDEB), with only 231 observations across 46 patients. AgentODE recovers functionally consistent ODE structures across all settings, and experiments on RDEB demonstrates that in sparse and noisy data settings reasoning from summary statistics promotes mechanistically principled structure discovery, whereas baselines with individual-level data access recover implausible structures despite better predictive performance. AgentODE opens new possibilities for mechanistic modeling of rare diseases directly from population-level summary statistics, where data scarcity and privacy constraints have traditionally limited such analyses.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00733v1) | [PDF](https://arxiv.org/pdf/2607.00733v1)

### [Federated Sovereign Transport Protocol (FSTP): Verifiable Coordination Without Disclosure](http://arxiv.org/abs/2607.00213v1)

- **arXiv ID**: `2607.00213v1`
- **作者 / Authors**: Ramón Soto C., Liz Soto
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

This paper introduces the Federated Sovereign Transport Protocol (FSTP), a synchronization boundary and transport layer for federated networks in which nodes have heterogeneous privacy requirements. Existing federation protocols leave data confinement to operator policy: they define message formats and delivery semantics but impose no structural constraint on what a conforming server may emit. FSTP addresses this gap by making data confinement a property of the protocol itself.   The central mechanism is a synchronization agent whose output type set is formally closed. Raw internal data cannot appear in any federation message because the constraint is enforced by the Rust type system at compile time, not by a runtime check. A contextual identity model derives a separate, unlinkable identifier for each federation relationship, preventing cross-context correlation structurally. A Blocklace-based event substrate provides tamper-evident, partially ordered logging with synchronization cost proportional to the symmetric difference between node states, and supports data erasure without breaking the hash chain.   The result is proof without exposure: a federation participant can verify that a process occurred, that a credential is authentic, and that an outcome is uncorrupted without accessing the internal data that produced these artifacts. FSTP is developed as the inter-node transport layer of Velyzor, a governance platform for institutions with demanding confidentiality requirements. The specification and reference implementation are released as open-source infrastructure under Apache 2.0; source code and figures accompany this paper.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00213v1) | [PDF](https://arxiv.org/pdf/2607.00213v1)

### [Delegation Rights: Property, Agency, and Investment Incentives in the Age of AI Agents](http://arxiv.org/abs/2606.31935v1)

- **arXiv ID**: `2606.31935v1`
- **作者 / Authors**: Yukun Zhang, Kemu Xu
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: econ.EM

<details>
<summary>📝 Abstract</summary>

AI agents increasingly operate inside digital accounts by exercising privileges that users already hold, raising a new control question: whether an existing account entitlement must be exercised manually or may be exercised through a user-authorized automated proxy. We define \emph{delegation rights} as the revocable, identity-preserving, scope-limited, and mode-specific authority of an account holder to authorize such proxy execution. We develop a three-party incomplete-contracts model with a User, an AI Agent provider, and a Platform. The contested object is not platform ownership, account transferability, data portability, or unrestricted API access, but residual control over the mode of account execution. Under Platform Control, the platform can protect infrastructure, identity systems, privacy boundaries, and third parties, but its discretionary veto weakens the User--Agent coalition's disagreement payoff and depresses relationship-specific investment. Under User Control, hold-up is reduced, but security, privacy, congestion, and third-party risks may remain insufficiently internalized. We then analyze \emph{Certified Delegation}, under which access protection is conditional on verifiable authorization, revocability, auditability, rate-limit compliance, data minimization, and risk mitigation. Certification is therefore not merely a technical safety screen; it is a conditional allocation of residual control. Illustrative mechanism simulations show how this regime can reduce deadweight loss by restoring delegation incentives while bounding residual risk.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31935v1) | [PDF](https://arxiv.org/pdf/2606.31935v1)

### [A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems](http://arxiv.org/abs/2606.31639v1)

- **arXiv ID**: `2606.31639v1`
- **作者 / Authors**: Seyed Bagher Hashemi Natanzi, Bo Tang
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Large language models are no longer only text generators. They are increasingly embedded in retrieval pipelines, enterprise assistants, coding environments, robotic systems, security-operation workflows, and autonomous agents that can read private data, call tools, write files, execute code, and act across organizational boundaries. This shift changes the security problem: risks do not arise from the model weights alone, but from the full lifecycle and application stack through which data, prompts, model outputs, tools, memories, and user authority interact. This paper systematizes the literature on vulnerabilities in large language model systems through a lifecycle and application-stack lens. We organize attacks across eight stages: data collection, pretraining, post-training alignment, model packaging and supply chain, retrieval and memory, prompting and inference, tool/agent execution, and deployment/maintenance. For each stage, we analyze attacker capabilities, affected security objectives, representative attacks, practical risks, evaluation practices, and defenses. We further map LLM-specific vulnerabilities to confidentiality, integrity, availability, safety, privacy, fairness, accountability, and agency-control objectives. Unlike taxonomies that list isolated attack names, the proposed systematization emphasizes where trust boundaries fail, how untrusted data becomes executable instruction, how delegated authority amplifies model errors, and why point defenses rarely compose. We close with a research agenda for secure LLM systems, including compositional security, provenance-aware retrieval, tool-call containment, long-horizon agent evaluation, privacy-preserving adaptation, realistic red teaming, and deployment-grade incident response.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31639v1) | [PDF](https://arxiv.org/pdf/2606.31639v1)

### [CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents](http://arxiv.org/abs/2606.29771v1)

- **arXiv ID**: `2606.29771v1`
- **作者 / Authors**: Bo Qu, Mingguang Chen
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

LLM agents are increasingly cast as autonomous portfolio managers, and benchmarks have moved from financial question-answering to sequential trading. Yet most still rank agents by returns over a fixed window -- a weak proxy, since a period's return is dominated by the market path and apparent alpha can dissolve once look-ahead leakage is controlled. Such a ranking certifies neither sound reasoning, nor a consistent strategy, nor a durable edge. We introduce CLQT, which reframes closed-loop trading evaluation as diagnosis rather than ranking: an instrument that localizes where and why an agent's process succeeds or fails. CLQT is a fully closed-loop, cost-aware, strategy-consistent, temporally-gated environment whose agents run a five-stage cycle: gather, synthesize, allocate, execute, reflect. Each round emits a complete DecisionRound sealed into a recompute-verifiable hash chain, so every metric is reconstructable from the trail. Six pillars form the substrate: a hard TimeGate, institutional transaction- and financing-cost modeling, strategy-consistency scoring, three-tier memory, a Model-Context-Protocol tool layer, and mandate-aware synthesis. The same agent runs as a constrained committee of specialized roles or a single full-autonomy orchestrator, making process scaffolding an experimental variable. From the audit trail we compute a five-axis capability scorecard (APM-CS: Coherence, Acuity, Composure, Discipline, Reliability), with Coherence judged partly by a held-out, out-of-cohort LLM to curb self-preference bias. We validate it on a contamination-controlled multi-model backtest with an ablation grid and a live broker track on unseen, post-cutoff data, against a repeated-run noise floor. CLQT separates outcome from capability, yielding not a model ranking but a durable, extensible map of agent competencies and limitations.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29771v1) | [PDF](https://arxiv.org/pdf/2606.29771v1)

### [Privacy-Preserving Decentralized Cooperative Localization with Range-Only Measurements: A Convex Optimization Based Approach](http://arxiv.org/abs/2606.29673v1)

- **arXiv ID**: `2606.29673v1`
- **作者 / Authors**: Nitesh Kumar, Reyshwanth Ganeshan, Sixu Li, Sivakumar Rathinam, Swaroop Darbha
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Cooperative localization using range-based measurements is critical for multi-robot systems operating in GPS-denied and unstructured environments. However, traditional cooperative approaches require sharing explicit spatial coordinates across the network, presenting a severe security vulnerability in privacy-sensitive missions. While recent literature has explored privacy-preserving alternatives, these methods typically rely on accuracy-degrading noise injection or computationally prohibitive cryptographic protocols. To overcome these limitations, we propose a novel, natively privacy-preserving Decentralized Cooperative Localization (DCL) framework based on convex optimization. Discarding probabilistic noise models, we assume strictly bounded measurement noise and formulate the localization problem via Semi-Definite Programming (SDP) to compute a Maximum-Volume Inscribed Ellipsoid (MVE). Our approach introduces novel intersection-plane constraints derived from landmark measurements to significantly tighten individual spatial bounds. To incorporate inter-robot range measurements securely, we uniquely decompose coupling constraints into localized Linear Matrix Inequalities (LMIs). Agents achieve fleet-wide spatial consensus by iteratively exchanging only abstract dual variables, completely avoiding the transmission of explicit primal position estimates. Extensive 3D Monte Carlo simulations demonstrate that our DCL framework outperforms existing SDP-based localization method in accuracy, while guaranteeing operational privacy and maintaining highly scalable, parallelizable computation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29673v1) | [PDF](https://arxiv.org/pdf/2606.29673v1)

### [A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation](http://arxiv.org/abs/2606.28896v1)

- **arXiv ID**: `2606.28896v1`
- **作者 / Authors**: Xuanting Wu, Fan Zhanga, Fei Ma, Ling Guan, Guochun Ma et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: eess.IV

<details>
<summary>📝 Abstract</summary>

Synthetic aperture radar (SAR) data augmentation is important for improving the generalization of data-driven SAR interpretation models, yet practical augmentation workflows are often hindered by heterogeneous dataset formats, task-dependent metadata requirements, diverse generation methods, and weak validation of generated samples. This paper presents the \textbf{S}AR \textbf{A}ugmentation and \textbf{G}eneration \textbf{A}gent (SAGA), a schema-grounded and benefit-aware agent framework for task-oriented SAR data generation and augmentation. Given a natural-language request and heterogeneous SAR inputs, SAGA extracts observable dataset facts, validates executable dataset schemas, selects feasible augmentation strategies through validator-constrained planning, and compiles the selected strategy into an auditable augmentation workflow. Generated data are further assessed by quality, distribution, SAR-artifact, duplicate, leakage, and optional downstream-task evaluators to support evidence-qualified augmentation claims. By separating semantic proposal from deterministic validation and execution, SAGA improves the reliability and reproducibility of SAR augmentation decisions. Experiments on controlled agentic benchmarks and downstream SAR interpretation tasks show that SAGA improves schema grounding, skill planning, invalid-sample rejection, and downstream augmentation utility compared with rule-based, LLM-only, ReAct-style, and fixed-augmentation baselines.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28896v1) | [PDF](https://arxiv.org/pdf/2606.28896v1)

### [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](http://arxiv.org/abs/2606.28061v1)

- **arXiv ID**: `2606.28061v1`
- **作者 / Authors**: Shijing Hu, Liang Liu, Zhu Meng, Zhicheng Zhao
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. Neither perspective captures purpose-bound information flow across an executed multi-tool trajectory. Motivated by this limitation in current agent evaluation, ToolPrivacyBench audits whether task-private atoms are routed only to authorized tools and downstream sinks, thereby evaluating both task completion and privacy over-disclosure during tool use. The benchmark contains 2,150 cases, including 1,150 fully synthetic privacy-sensitive business workflows and 1,000 cases adapted from existing multi-tool and function-calling benchmarks. Each case is represented by a policy knowledge base. After an agent executes against mock business backends, the evaluator compares recorded tool arguments and backend audit logs with this policy knowledge base. The evaluation covers nine widely used agents to characterize purpose-bound privacy over-disclosure. The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28061v1) | [PDF](https://arxiv.org/pdf/2606.28061v1)

### [Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy](http://arxiv.org/abs/2606.27936v1)

- **arXiv ID**: `2606.27936v1`
- **作者 / Authors**: Oscar Thees, Roman Müller, Matthias Templ
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

The widespread collection of fine-grained location data by commercial data brokers creates a re-identification risk that is not widely recognised by the public. While prior research has established that mobility traces are highly unique and that individuals can, in principle, be identified from a handful of spatio-temporal points, such attacks have historically required significant manual effort from skilled analysts, limiting their practical scale.   In this feasibility study, we demonstrate in a real world setting that agentic AI fundamentally changes this threat model. We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. We evaluate the pipeline on a spatio-temporal dataset containing simulated location points anchored at and around true home and work addresses, focusing on a high-risk disclosure scenario. Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified 18 of the 25 re-identifiable individuals (72%) and 18 of 43 cases overall (41.9%).   We discuss implications for Statistical Disclosure Control (SDC) practice and outline the near-future escalation that data custodians and regulators must anticipate. De facto anonymity - an implicit foundation of SDC practice - is shifting. Agentic AI strengthens the case that re-identification is reasonably likely by any means under the GDPR Recital-26 standard, at costs of minutes-and-dollars per target.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27936v1) | [PDF](https://arxiv.org/pdf/2606.27936v1)

### [DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection](http://arxiv.org/abs/2606.27499v1)

- **arXiv ID**: `2606.27499v1`
- **作者 / Authors**: Yujin Tang, Chenming Shang, Ruize Xu, Nikhil Singh
- **发布日期 / Published**: 2026-06-25
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it could write down. We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory. DMV-Bench is built on a controlled home-furnishing e-commerce catalogue of 1,000 product variants in which a text-leakage contract keeps the discriminative signal of each task in the pixels alone. Across a chain of autonomous shopping sessions, every visited product image carries a unique, pre-rendered incidental cue, and the agent is later asked to recall a particular cued product and navigate to its URL. Inspired by dual-coding theory, we propose DualMem, a memory architecture that maintains a visual and a verbal code in parallel. On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27499v1) | [PDF](https://arxiv.org/pdf/2606.27499v1)

## 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication*

### [Exploring the Cryptographic Limits of Transformer Networks](http://arxiv.org/abs/2606.29389v1)

- **arXiv ID**: `2606.29389v1`
- **作者 / Authors**: Stefan Domunco, Andis Draguns, Philip Torr, Isaac Robinson, Christian Schroeder de Witt
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

In recent work it has been shown that colluding AI agents can use steganographic methods to exchange malicious information. Whether a transformer can implement steganographic methods depends on what cryptographic functions it can implement, since a transformer that can implement a cryptographic function within its layers has source-free randomness access. Despite existing circuit-complexity results, no prior work maps specific cryptographic constructions to transformer architectures. As Merrill et al. have shown that saturated transformers can be seen as threshold circuits, we first generate threshold circuits for three different cryptographic constructions (Keccak functions, Merkle--Damgard constructions and Merkle Trees) and then map these circuits to different transformer architectures. We derive verified scaling laws for the width and depth of the circuits which implement each cryptographic construction and propose two different mappings: no-attention mapping, tokens-as-gates mapping. Beyond its security implications, this work contributes to by establishing a methodology for deriving structural guarantees on transformer computational capacity. Specifically, we derive constructive upper bounds on what a transformer of a given depth and width could plausibly compute, providing a principled foundation for capability evaluations of transformer-based AI systems.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29389v1) | [PDF](https://arxiv.org/pdf/2606.29389v1)

### [Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](http://arxiv.org/abs/2606.28425v1)

- **arXiv ID**: `2606.28425v1`
- **作者 / Authors**: Jimmy Laurence Rippin, Simon C. Marshall, David Demitri Africa, Christian Schroeder de Witt
- **发布日期 / Published**: 2026-06-25
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Increasingly autonomous agentic AI systems pose novel multi-agent risks, such as secret collusion via covert communication channels. The natural defence to these collusion attempts is to monitor plain-text communication, but the efficacy of monitors has been called into doubt by increasingly sophisticated model steganography; indeed, some theoretical schemes have been proposed that are information-theoretically or computationally indistinguishable from good-faith plain-text communication. In this paper, we demonstrate that the complexity of these schemes is no longer a safety barrier, as agentic coding models can already produce undetectable stegosystems when given realistic tool usage, such as code execution or accessing research papers through web searches. Agents also adapt when key ingredients are missing, for example, by adding model-sampling components or implementing related keyed coding schemes. We then frame tacit steganographic coordination between agents as a Schelling-point problem and introduce coordination metrics for estimating when two agents are likely to select compatible schemes without explicit prior agreement. Our results suggest a shift in the threat model for covert communication between AI agents, where the main barrier is no longer whether frontier agents can understand and implement sophisticated stegosystems, but coordination: whether independently acting agents can converge on compatible schemes, keys, and parameters. We find substantial convergence on broad scheme families but limited strict one-shot coordination, suggesting that shared artefacts, repeated interaction, and tool-mediated search are the settings where covert communication risks are most acute. Overall, our findings provide empirical grounding for the recent strategic confinement hypothesis, which assumes that capable agents can construct covert channels that survive monitoring.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28425v1) | [PDF](https://arxiv.org/pdf/2606.28425v1)

## 📂 misuse
*滥用与误用 / Misuse & Abuse*

### [(A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents](http://arxiv.org/abs/2607.00333v1)

- **arXiv ID**: `2607.00333v1`
- **作者 / Authors**: Zidong Zhang, Zhentao Xie, Wenrui Diao, Jianliang Wu
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Third-party mobile agents powered by Vision-Language Models (VLMs) have emerged as a promising paradigm for automating smartphone interactions. These agents act as high-privilege decision-makers, perceiving device states through screenshots and executing actions via VLM reasoning, transforming how an agent app interacts with the environment (i.e., other apps or the OS). Correspondingly, this transformation introduces new attack surfaces or transforms benign/harmless interfaces into exploitable ones for mobile devices. In this paper, we summarize key differences between third-party mobile agent apps and general apps when interacting with the environment, analyze the security posture of agents, and identify two unique attack surfaces compared to general mobile apps: the Screen Perception Attack Surface, which exploits the gap between human and machine vision, and the Misused Channel Attack Surface, which intercepts or manipulates the agent's execution pipeline. We design and implement seven concrete attacks, from subliminal text injection and invisible pixel zone exploitation to screenshot tampering and host PC command injection. Our evaluation of five popular mobile agent frameworks demonstrates that a malicious app can hijack agent actions and achieve arbitrary command execution even without any privilege permissions, while remaining visually indistinguishable to users. These findings reveal a fundamental trust mismatch in autonomous agent design and highlight the urgent need for perception-aware security models on multi-tenant platforms.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00333v1) | [PDF](https://arxiv.org/pdf/2607.00333v1)

### [Self-Evolving World Models for LLM Agent Planning](http://arxiv.org/abs/2606.30639v1)

- **arXiv ID**: `2606.30639v1`
- **作者 / Authors**: Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory, which extracts persistent heuristic rules from prediction-observation mismatches; and (iii) Selective Foresight, which filters low-confidence predictions before integrating them into agent reasoning context. We evaluate WorldEvolver on ALFWorld and ScienceWorld, measuring world model prediction accuracy on Word2World and downstream agent success rate on AgentBoard. Extensive experiments show that WorldEvolver achieves the highest prediction accuracy across three backbones and leads other world model baselines on downstream agent success rate, demonstrating that test-time memory revision enhances both predictive fidelity and planning performance.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30639v1) | [PDF](https://arxiv.org/pdf/2606.30639v1)

### [It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents](http://arxiv.org/abs/2606.27944v1)

- **arXiv ID**: `2606.27944v1`
- **作者 / Authors**: Yiming Sun, Chen Chen, Zifan Zhou, Mi Zhang
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.MM

<details>
<summary>📝 Abstract</summary>

Phone-use Agents can execute complex tasks end to end across real mobile applications. By operating a real device on the user's behalf, they reach far more functionalities than CLI agents, which amplifies the real-world harm they can cause when driven for malicious purposes. We present the first study of this threat on real phones and 27 commercial apps, and find that agents built on 9 mainstream commercial and open-source models readily carry out serious misuse, ranging from procuring drug and explosive precursors to fraud, online harassment, and review manipulation. Across the agents we run on real devices, the average refusal rate to harmful requests stays low while the average task-completion rate reaches 68.8%, and in some scenarios an agent finishes a violation faster than a human would. These results suggest that Phone-use Agents already meet the practical conditions for automated misuse at scale.   In one observed real-device execution, Claude-Opus-4.8 fabricated a medical history, deceived an online doctor into issuing a prescription, and completed the order and payment on its own to purchase a precursor for a highly toxic substance. To our knowledge, this is the first documented real-world case of an AI agent procuring controlled precursor materials. We trace this behavior to a Safety Awareness-Execution Gap, where an agent recognizes that a request is harmful yet still executes it. Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. We hope these findings push the community toward safer Phone-use Agents.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27944v1) | [PDF](https://arxiv.org/pdf/2606.27944v1)

## 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces*

### [Distributed Containment of a Compromised Agent through Repulsive Cages](http://arxiv.org/abs/2607.01230v1)

- **arXiv ID**: `2607.01230v1`
- **作者 / Authors**: Luigi Petruzziello, Camilla Fioravanti, Gabriele Oliva
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: eess.SY

<details>
<summary>📝 Abstract</summary>

UAV swarms and cyber-physical multi-agent systems are increasingly deployed in safety-critical missions that require coordinated motion, distributed decision making, and autonomy. A major security risk arises when a legitimate agent is hijacked and driven by adversarial high-level commands. Rather than focusing on detection and isolation of malicious agents, we exploit a structural property common in autonomous platforms: low-level collision-avoidance modules are typically implemented as independent safety layers and may remain active even under high-level compromise. Building on this property, we propose a distributed containment framework that uses the compromised agent's uncompromised avoidance response as an indirect actuation channel. Defender agents select their geometric configuration to shape the repulsive field experienced by the target, with the goal of keeping it inside a prescribed admissible region and, when required, steering it toward a desired destination. The interaction is modeled as an online Stackelberg game in which defenders act as leaders and the adversary reacts by choosing the target command. Using support-function and normal-cone arguments, we derive an exact geometric characterization of robust one-step containment and introduce the notion of a repulsive cage. These results define a centralized Stackelberg oracle and motivate a fully distributed online approximation based on local communication and dynamic field estimation. We prove sublinear dynamic-regret bounds with respect to the centralized benchmark, quantifying the effect of network-induced estimation errors and temporal variability of the stage-wise optimum. Simulations validate the approach and corroborate the theory.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01230v1) | [PDF](https://arxiv.org/pdf/2607.01230v1)

### [Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning](http://arxiv.org/abs/2607.01138v1)

- **arXiv ID**: `2607.01138v1`
- **作者 / Authors**: Michele Armillotta, Nicolò Romandini, Rebecca Montanari, Lorenzo Cavallaro
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

LLM-based vulnerability detectors have shown promising results in identifying memory-safety bugs and vulnerability classes whose violations can often be expressed through established security properties. Logic vulnerabilities, however, pose a different challenge, as their identification requires inferring application-specific security invariants and implicit assumptions about intended behavior. Even frontier agentic models struggle because these invariants are often implicit and buried among unrelated code. Motivated by this gap, we present Antaeus, a framework for detecting logic vulnerabilities that grounds LLM reasoning in repository-level code context. Antaeus follows a repository-scale pipeline combining function prioritization, context-grounded reasoning, comparative validation, and structured reporting. It ranks functions using lightweight repo-wide security signals, directing costly LLM analysis toward relevant code and reducing calls, cost, and triage effort. For each prioritized function, Antaeus combines local code context with a repository-level view of the application's functionality, security resources, and trust boundaries. This enables reasoning about how the function is executed within the broader application rather than as an isolated snippet. Antaeus identifies security-sensitive sinks, derives safety conditions for safe execution, and checks whether they are locally satisfied. Candidate findings undergo comparative validation, pruning concerns that reflect project-wide norms rather than distinctive violations. Finally, Antaeus reports sinks, violated safety conditions, and evidence, making findings actionable and traceable. We evaluate Antaeus on 28 repositories with confirmed logic vulnerabilities and compare it against function-level and agentic models. Antaeus detects and explains 15 vulnerabilities, outperforming baselines with comparable token usage and cost.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01138v1) | [PDF](https://arxiv.org/pdf/2607.01138v1)

### [DART-VLN: Test-Time Memory Decay and Anti-Loop Regularization for Discrete Vision-Language Navigation](http://arxiv.org/abs/2607.01043v1)

- **arXiv ID**: `2607.01043v1`
- **作者 / Authors**: Shaoheng Zhang, Zhichen Li, Jie Mei
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Memory-based discrete vision-language navigation (VLN) agents must act under partial observability, yet even strong frozen backbones remain vulnerable at test time. Two common failure modes are stale historical evidence at memory readout and inefficient local backtracking during action selection. We present DART-VLN, a training-free test-time control framework for discrete VLN. DART-VLN combines Test-Time Memory Decay, a read-side memory reweighting rule that suppresses stale and redundant evidence without rewriting stored content, with Anti-Loop Regularization, a lightweight next-hop penalty that discourages immediate reversals during action selection. The framework introduces no new learnable parameters and leaves the learned backbone unchanged. Experiments on R2R and REVERIE show a consistent pattern: decay-only provides stable read-side gains, while decay+anti-loop achieves the best overall quality-efficiency trade-off, yielding shorter trajectories, lower runtime, and improved navigation performance in key settings. Behavioral analysis further confirms that anti-loop regularization reduces local backtracking and improves path efficiency under frozen backbones. Overall, the results show that modest test-time control can make memory-based discrete VLN more reliable and efficient without retraining.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01043v1) | [PDF](https://arxiv.org/pdf/2607.01043v1)

### [Knowledge-Enhanced Agentic Vulnerability Repair](http://arxiv.org/abs/2607.00820v1)

- **arXiv ID**: `2607.00820v1`
- **作者 / Authors**: Sicong Cao, Hao Ma, Le Yu, Kangyi Ding, Xiaolei Liu et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Frontier foundation models have changed the math on vulnerability discovery, but the bigger challenge is how the remediation side keeps up. Despite recent progresses in Automated Vulnerability Repair (AVR), current solutions struggle to reliably identify the root causes of vulnerabilities, and insufficiently utilize the prior fix knowledge to guide the patch generation process, thus undermining their effectiveness in practice.   To address this gap, we propose KeaRepair, a novel agentic AVR approach that grounds patch generation in verified program facts and high-level vulnerability knowledge. Specifically, KeaRepair first extracts multi-dimensional vulnerability knowledge from historical vulnerability-patch pairs from dual complementary views, and constructs dedicated retrieval knowledge bases. It then employs a tool-augmented agent that performs ReAct-style reasoning to collect verified program facts for vulnerability diagnosis. Finally, based on the diagnostic results, KeaRepair performs knowledge-level retrieval-augmented patch generation and iteratively refines patches through a closed-loop validation process involving compilation, PoC replay, and test-suite execution. Experimental results show that KeaRepair significantly outperforms existing AVR approaches on 55 reproducible C/C++ vulnerabilities. When paired with Gemini-3.1-Pro, KeaRepair successfully repairs 46 vulnerabilities, achieving a repair rate of 83.64%. Moreover, KeaRepair fixes six unique vulnerabilities that none of the baselines can address, and further demonstrates strong cross-language generalizability.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00820v1) | [PDF](https://arxiv.org/pdf/2607.00820v1)

### [SLM, LLM or Agentic AI? Toward Intelligent UAV-Enabled WPT Systems in Low-Altitude Economy Networks](http://arxiv.org/abs/2607.00255v1)

- **arXiv ID**: `2607.00255v1`
- **作者 / Authors**: Feibo Jiang, Li Dong, Lei Mao, Kezhi Wang, Xianbin Wang et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.IT

<details>
<summary>📝 Abstract</summary>

Unmanned Aerial Vehicles (UAVs) have become key enabling platforms for low-altitude economic networks, yet achieving efficient and adaptive optimization under resource-constrained and dynamic environments remains challenging. This paper investigates language models for UAV-enabled Wireless Power Transfer (WPT) systems. First, a lightweight Small Language Model (SLM)-based solution is developed using a pre-trained BERT backbone, enhanced UAV embeddings and contextual features, a geometry-aware path decoder, and ensemble inference to achieve low complexity, low latency, and high energy efficiency. Second, an Agentic AI-based framework is designed to exploit the reasoning and interactive capabilities of Large Language Models (LLMs). It integrates four collaborative agents-Initializer, Actor, Critic, and Reflector-to form a closed loop of generation, optimization, evaluation, and reflection for iterative UAV path and energy optimization. Finally, simulations compare the SLM-, LLM-, and Agentic AI-based approaches.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00255v1) | [PDF](https://arxiv.org/pdf/2607.00255v1)

### [EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards](http://arxiv.org/abs/2607.00218v1)

- **arXiv ID**: `2607.00218v1`
- **作者 / Authors**: Siddhant Panpatil, Arth Singh, Mijin Koo, Chaeyun Kim, Haon Park et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Vision-language models (VLMs) are now proposed as runtime safety guards for embodied agents in homes and factories. A deployable guard must catch genuinely unsafe situations while avoiding unnecessary intervention on routine but superficially alarming activity, a distinction that binary safety benchmarks obscure. We introduce EgoSafetyBench, an egocentric video benchmark of 1,200 robot-view scenarios annotated at half-second granularity, to evaluate VLMs as streaming guards across two tracks. The situational track (800 scenarios) spans four families, from routine and safe-but-suspicious scenes to obvious and contextual hazards. The visual-channel track (400 scenarios) targets in-scene text-a sign, sticker, or label visible in the scene-that can misrepresent the physical situation, pairing each misleading sign with a truthful version to test both whether a guard flags the text as misleading and whether the text corrupts its physical-safety judgment. Both tracks use contrastive ladders: near-identical scenarios differing only in a single visible deciding cue, so a correct call must hinge on that cue rather than the overall scene type. We evaluate ten open- and closed-source VLMs. We find that while guards reliably recognize videos containing hazards, they often miss specific hazardous moments, particularly contextual hazards. Furthermore, misleading in-scene signs degrade all tested guards: vulnerable models miss up to a third of hazards, while robust models over-intervene on safe content. Matched controls reveal that apparent safety robustness often reflects indiscriminate alarming rather than true physical reasoning.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00218v1) | [PDF](https://arxiv.org/pdf/2607.00218v1)

### [Dual-Informed Vertical Expansion for Multi-Objective Node Selection in Anytime Conflict-Based Search](http://arxiv.org/abs/2607.00156v1)

- **arXiv ID**: `2607.00156v1`
- **作者 / Authors**: Willem van Osselaer, Jiarui Li, Meshal Alharbi, Gioele Zardini
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Conflict-Based Search (CBS) is a leading exact algorithm for Multi-Agent Path Finding (MAPF), but its high-level node-selection rule is usually treated as a fixed implementation detail. Standard best-first selection is strong for minimizing expanded nodes and closing the optimality certificate, yet it can maintain a large frontier, interrupt parent-child expansion sequences, and provide no feasible incumbent until termination. This paper studies node selection as a first-class design choice for exact CBS. We introduce Dual-Informed Vertical Expansion (DIVE), a policy that is best-bound between dives and depth-oriented within a dive. DIVE starts each dive from the current best-bound frontier, follows promising children to exploit parent-child locality, and uses incumbent pruning to limit unproductive excursions. We formalize CBS node selection through a branch-and-bound view, prove that the traversal policy can be changed without affecting exactness, and analyze the resulting trade-offs among expanded nodes, dive breaks, queue size, and primal-dual bound progress. The analysis predicts three complementary extremes. Best-first search is node efficient, iterative deepening is memory efficient, and DIVE is dive efficient while retaining regular best-bound reanchoring. Experiments on standard MAPF benchmarks support this trade-off map. DIVE consistently reduces dive breaks, provides early incumbents with certified gaps, uses substantially less queue memory than best-first search, and benefits from warm starts and simple responsive variants in dense or memory-limited regimes.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00156v1) | [PDF](https://arxiv.org/pdf/2607.00156v1)

### [Scalable Behaviour Cloning on Browser Using via Skill Distillation](http://arxiv.org/abs/2606.32014v1)

- **arXiv ID**: `2606.32014v1`
- **作者 / Authors**: Kaisen Yang, Zheng Jiang, Yuzhao Peng, Houde Qian, Boshi Zhang et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Internet users collectively perform an enormous range of skilled work through web browsers, from software development and document editing to search, forms, and enterprise workflows, making human browsing a highly scalable but under-exploited source of reusable browser skills. We argue that the bottleneck for browser agents is decision-making under incomplete information rather than low-level operation, and that the priors agents lack are already implicit in human interaction traces. We therefore study scalable behavior cloning for browser agents via skill distillation, converting user interaction trajectories into compact natural-language skills that agents can read, retrieve, reuse, and compose directly. We further organize the distilled skills into a skill graph so that growth proceeds through consolidation rather than unbounded accumulation. This suggests that the scalability of browser agents may come less from manually designed tasks and more from the collective skills already expressed by internet users. Our project is available at: https://lab.einsia.ai/browserbc/.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.32014v1) | [PDF](https://arxiv.org/pdf/2606.32014v1)

### [Higher-order hopping-parameter expansion by human-AI collaboration](http://arxiv.org/abs/2606.31492v1)

- **arXiv ID**: `2606.31492v1`
- **作者 / Authors**: Masakiyo Kitazawa, Tatsuya Wada
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: hep-lat

<details>
<summary>📝 Abstract</summary>

We develop efficient algorithms for evaluating higher-order terms in the hopping-parameter expansion of $\textrm{Tr}\ln M$ on $SU(N_\textrm{c})$ gauge configurations. The resulting algorithms, which exploit a trie data structure for the computation of high-order terms, evaluate the $κ^8$, $κ^{10}$, and $κ^{12}$ terms at computational costs of approximately $20$, $460$, and $8900$ times that of a single staple evaluation, respectively. The correctness of the algorithms is verified by comparison with a computationally expensive but reliable reference calculation. We emphasize that collaboration between human researchers and AI coding agents was essential to the development of these algorithms.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31492v1) | [PDF](https://arxiv.org/pdf/2606.31492v1)

### [Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents](http://arxiv.org/abs/2606.31270v1)

- **arXiv ID**: `2606.31270v1`
- **作者 / Authors**: Xueqiao Sun, Xiaohan Wang, Ludwig Schmidt, Serena Yeung-Levy, Yuhui Zhang
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Computer-use agents, which leverage multimodal large language models (MLLMs) to operate computers and complete tasks, have attracted significant attention for their utility and versatility. A major challenge in developing these agents is collecting large-scale, high-quality trajectories. The standard approach generates synthetic data through a self-improving loop: an agent is placed in a verifiable environment and iteratively fine-tuned on its successful trajectories. Despite its effectiveness, this paradigm exploits only successful trajectories and discards the failed ones, even though failures carry rich information about a model's weaknesses. In this work, we explore a complementary failure-driven self-improvement loop, a data-centric paradigm that turns failed trajectories into agent improvements. Specifically, we employ an LLM to diagnose failure modes, propose inference-time solutions, and generate code patches -- lightly verified by humans -- that upgrade the agent. We validate this approach with the state-of-the-art OpenCUA-72B model on the OSWorld benchmark, improving the success rate from 42.3% to 48.9%, a gain of 6.6 percentage points, without any additional training cost and with only modest inference overhead. Our results demonstrate that failure-driven self-improvement is a viable complement to success-based pipelines, enabling more efficient agent improvement.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31270v1) | [PDF](https://arxiv.org/pdf/2606.31270v1)

### [Truth or Sophistry? LoFa: A Benchmark for LLM Robustness Against Logical Fallacies](http://arxiv.org/abs/2606.31039v1)

- **arXiv ID**: `2606.31039v1`
- **作者 / Authors**: Xudong Shen, Li Yuan, Ye Chen, Xin Wu, Yi Cai et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Large Language Models (LLMs) exhibit strong semantic capabilities, yet their resilience to manipulative linguistic patterns such as logical fallacies remains underexplored. Prior work has primarily examined whether LLMs can identify or classify fallacies, leaving their robustness against fallacious persuasion insufficiently studied. To address this gap, we introduce LoFa (Logical Fallacy), a comprehensive benchmark for evaluating LLM robustness against fallacies. LoFa is constructed through a multi-agent pipeline that pairs factual questions with fallacious arguments, and is accompanied by a multi-round debate framework for assessing model resilience under sustained adversarial persuasion. To disentangle fallacy robustness from a model's inherent knowledge limitations, we further propose Logical Fallacy Resistance at k (LFR@k), a metric that quantifies resistance to fallacious attacks. Experiments show that LLMs exhibit varying levels of robustness across different fallacy types, revealing distinct vulnerability profiles among models.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31039v1) | [PDF](https://arxiv.org/pdf/2606.31039v1)

### [UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](http://arxiv.org/abs/2606.30608v2)

- **arXiv ID**: `2606.30608v2`
- **作者 / Authors**: Mohamed el Amine Boudjoghra, Ivan Laptev, Angela Dai
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry revealed under articulation. High-level agents reason about object semantics and motion using knowledge from vision-language and video models, while low-level agents estimate articulation parameters and interaction points; together, they engage in a two-round structured debate that first exploits global--local disagreement and then grounds the agents in freely generated video. The same video prior, conditioned on the agreed articulation, then drives each part through its motion to expose occluded interiors and geometry that cannot be inferred from a single static view. By combining agentic reasoning with a video generative prior, our approach jointly infers articulation and reconstructs complete 3D articulated objects, producing high-fidelity geometry, internal structure, and motion-consistent states beyond directly observed surfaces.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30608v2) | [PDF](https://arxiv.org/pdf/2606.30608v2)

### [MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems](http://arxiv.org/abs/2606.30602v1)

- **arXiv ID**: `2606.30602v1`
- **作者 / Authors**: Kunyang Li, Kyle Domico, Jonathan Gregory, Patrick McDaniel
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows. However, their inter-agent communication channels introduce new attack surfaces that remain poorly understood and are difficult to defend against. In this paper, we address how defenders should prioritize limited security effort to protect vulnerable communication channels before attacks are observed. This is motivated by our observation that the channel-level attack impact is highly non-uniform: a single compromised edge can account for up to 75% of total attack success. We introduce Mesa, a label-free framework for proactively ranking which MAS edges are most security-critical -- that is, most likely to affect the system's decision if compromised. Mesa combines six graph-theoretic metrics and two dynamic probes (ablation and masking) without requiring attack traces. We evaluate Mesa against a dynamic misinformation attack pipeline across three diverse MAS scenarios, eight network topologies, and five open-source LLMs from Qwen, Llama, and Gemma families. Mesa rankings correlate strongly with empirical per-edge attack success rate, achieving mean Spearman $ρ=+0.60$ (peaking at $+0.73$). In resource-constrained defense deployment, monitoring the top 10% of Mesa-ranked edges intercepts about 3x the successful attacks as random allocation. We further test Mesa under varying attacker and defender models and LangGraph workflows and characterize its limits under adaptive attacks and high-redundancy graphs. Overall, our results show that edge-level risk in MAS is often concentrated and predictable, allowing proactive hardening of multi-agent infrastructures.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30602v1) | [PDF](https://arxiv.org/pdf/2606.30602v1)

### [Minimal MMAO: A Resource-Closed-Loop Framework for Adaptive Metaheuristic Search](http://arxiv.org/abs/2606.30450v1)

- **arXiv ID**: `2606.30450v1`
- **作者 / Authors**: Jinliang Xu, Liping Ma
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.NE

<details>
<summary>📝 Abstract</summary>

This paper presents the Metabolic Multi-Agent Optimizer (MMAO) as an adaptive metaheuristic built around endogenous resource circulation. The central premise is that search intensity, exploration--exploitation balance, and lifecycle turnover should be induced by a shared metabolic controller rather than by separately attached schedules. We formulate MMAO through bounded private energy, a communal budget, normalized reward, continuous role adaptation, and resource-financed branching and pruning. The method is then instantiated in both continuous and discrete domains and evaluated on a matched small-scale suite including Sphere, Rastrigin, a synthetic Euclidean TSP, and two TSPLIB instances. The results show a consistent pattern: the same metabolic loop remains workable across domains, the discrete realization remains relatively stable under a compact design, and continuous refinement quality is the main cost of keeping the method lean. Taken together, these findings position MMAO as a coherent framework for adaptive heuristic design rather than a loose collection of operators.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30450v1) | [PDF](https://arxiv.org/pdf/2606.30450v1)

### [An AI-Based Solution for Secure Service Provisioning in IoT](http://arxiv.org/abs/2606.30701v1)

- **arXiv ID**: `2606.30701v1`
- **作者 / Authors**: Marco Arazzi, Mert Cihangiroglu, Serena Nicolazzo, Antonino Nocera, Vinod P
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

As the Internet of Things (IoT) continues its rapid expansion, the attack surface grows accordingly, with emerging threats targeting smart objects and their interactions. In this evolving landscape, securing service provisioning is crucial to ensure the proper functioning, security, and reliability of the IoT ecosystem. Service provisioning encompasses key tasks such as device registration, configuration, authentication, authorization, and software deployment, all of which are essential for seamless and secure IoT operations. In this paper, we present a comprehensive framework designed to select the most suitable smart objects to deliver a target service within a given IoT environment while also monitoring the behavior of the entities involved during the service provisioning phase. To achieve this, we employ a Deep Reinforcement Learning (DRL) approach in which an intelligent agent learns, through interaction with a complex, dynamic environment, how to adapt to changes while adhering to predefined security constraints. For behavioral monitoring, we leverage Federated Learning (FL) to develop a global Behavioral Fingerprinting (BF) model that is fully distributed and can analyze how IoT devices interact within the network. In addition, the BF is used to compute a reliability score for each service provider, reflecting its degree of compliance with the defined security constraints. This score is then incorporated into the service provisioning process, allowing smart objects to select providers not only according to functional suitability but also to their reliability level. Finally, we conduct an extensive experimental evaluation to assess the robustness and scalability of our approach. The results demonstrate that our solution can be effectively deployed even on resource-constrained IoT devices, making it a viable and scalable security-enhancing mechanism for modern IoT ecosystems.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30701v1) | [PDF](https://arxiv.org/pdf/2606.30701v1)

### [Parametric Skills](http://arxiv.org/abs/2606.30015v1)

- **arXiv ID**: `2606.30015v1`
- **作者 / Authors**: Xuan Zhao, Haonan He, Qingyu Yang, Minglei Li, Jingqi Ye et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Since intelligence fundamentally relies on efficient skill acquisition (Chollet, 2019), the ability to leverage skills is critical. For LLMs, skills, manually authored or extracted from task trajectories, are textual recipes encoding mature problem-solving experience and are critical to agentic capabilities. Despite widespread deployment, their utility is limited by the model's ability to comprehend and follow skill instructions, especially under complex and long-context scenarios, where key instructions are difficult to locate and adhere to. To address this limitation, we propose ParametricSkills, a framework that can convert free-form textual skills into parameters at test time, enabling context-free skill exploitation. Specifically, we first construct a large-scale, high-quality skill library, and synthesize single-turn and multi-turn skill exploitation trajectories built around these skills with OpenCode. Using these data, we then train a hypernetwork that parameterizes both the skill content and the test-time exploitation methodology by receiving textual skills and converting them into LoRA adapters. Experimental results on six complex software engineering (SWE) subtasks demonstrate that, the proposed ParametricSkills averagely outperforms in-context learning by 6.44 points as judged by DeepSeek-V4-Flash, while also achieving significantly higher BERT Score and F1 score, confirming its effectiveness. Beyond performance, we further find that parametric skills, being inherently accumulative, offer a preliminary yet promising avenue toward test-time continual learning.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30015v1) | [PDF](https://arxiv.org/pdf/2606.30015v1)

### [Exploration and Online Transfer with Behavioral Foundation Models](http://arxiv.org/abs/2606.29980v2)

- **arXiv ID**: `2606.29980v2`
- **作者 / Authors**: Louis Bagot, Mathieu Lefort, Laëtitia Matignon
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Zero-shot Transfer in Reinforcement Learning (RL) aims to train an agent that can generate optimal policies for any reward function, without additional learning at transfer time, while training only on reward-free trajectories. For their generality over tasks, such models are sometimes called ``Behavioral Foundation Models'' (BFMs). While they have shown strong performances and improvements in recent years, the current framework and algorithms still assume that, during the transfer phase, the agent is informed offline about the reward (the task to solve) through a dataset of state-reward pairs, which it uses to pick the best policy to deploy. However, in practice if the reward is a black-box (e.g. direct user feedback), it is not possible to generate such a dataset: it is necessary to observe the reward through interactions with the environment. In other words, the current framework of offline transfer is not aligned with the traditional RL setting of online learning through trial-and-error, which requires exploration in order to find rewards. This paper proposes to tackle this new online transfer in zero-shot RL, with the key insight that the BFM itself can be used to generate exploration policies. We show that it is possible to frame this online learning problem in terms of a bandit-like exploration-exploitation problem. More precisely, at each step the bandit algorithm recommends a policy, the BFM executes it in the environment, which yields a reward and a new state; we repeat the process until we converge to the optimal policy. In the popular context of linear reward approximation, we derive a formulation inspired by Upper Confidence Bound and show that exploration can be achieved through the minimization of the eigenvalues of an uncertainty matrix. We evaluate qualitatively and quantitatively our framework on a simple environment to validate the concept of our method.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29980v2) | [PDF](https://arxiv.org/pdf/2606.29980v2)

### [Verified residual-specific explicit derivative kernels for physics-informed learning and discretized PDE adjoints](http://arxiv.org/abs/2606.29702v1)

- **arXiv ID**: `2606.29702v1`
- **作者 / Authors**: Wenbo Cao, Zhe Lu, Weiwei Zhang
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: physics.comp-ph

<details>
<summary>📝 Abstract</summary>

Derivative computation is central to scientific computing, from space-time derivatives in physics-informed neural networks (PINNs) to residual Jacobian actions and discrete-adjoint operators in computational fluid dynamics (CFD). General-purpose automatic differentiation (AD) reduces implementation effort, but can incur substantial runtime and memory overhead for high-order residuals and complex discretized operators. Explicit derivative kernels can exploit problem-specific structure and provide efficient, controllable evaluations, but their use has been limited by derivation and implementation costs. This work revisits explicit differentiation (ED) as a residual-specific and verifiable route enabled by agent-assisted implementation and stringent numerical verification. For PINNs, we propose residual-specific partial-jet propagation, which makes the derivative-state closure of the target PDE residual explicit and realizes it through specialized layerwise kernels, rather than relying only on nested AD or a generic Taylor-mode transform. Relative to nested AD, the resulting ED kernels achieve floating-point-level agreement in residual and parameter-gradient evaluations and accelerate complete PINN training, often reaching 2-4x speedups while reducing peak GPU memory in most cases. For discretized PDE adjoints, we apply the same verification-driven strategy to a finite-volume CFD residual. The generated tangent-action and transpose-action kernels pass Taylor-remainder, inner-product, and reduced-gradient consistency checks, and are embedded into a GPU-resident discrete-adjoint workflow for freestream Mach-number and angle-of-attack inversion. These results suggest that verified explicit derivative kernels, supported by agent-assisted implementation, can serve as a practical, structure-aware complement to general-purpose AD for derivative-intensive scientific computing.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29702v1) | [PDF](https://arxiv.org/pdf/2606.29702v1)

### [A Machine-Verified Proof of a Quantum-Optimization Conjecture](http://arxiv.org/abs/2606.29687v1)

- **arXiv ID**: `2606.29687v1`
- **作者 / Authors**: Uri Kol, Maor Ben-Shahar, Kfir Sulimany, Dirk Englund
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: quant-ph

<details>
<summary>📝 Abstract</summary>

We report a machine-verified resolution of a problem open for over a decade in quantum optimization: the Farhi, Goldstone and Gutmann (FGG) conjecture that depth-$p$ Quantum Approximate Optimization Algorithm (QAOA) on the ring of disagrees attains approximation ratio $(2p+1)/(2p+2)$ exactly. We found the proof using a large language model, Claude Fable 5, and verified its correctness end-to-end by the Lean 4 proof assistant. Our methodology includes several ingredients: building on a substantial Lean library of quantum information, we formalized the QAOA components and the known parts of the problem, and reduced the conjecture to a single open mathematical statement. The model was then handed the library and our agentic toolkit, and tasked with closing that gap by constructing a proof in Lean. The resulting process is a feedback loop between the model's natural-language reasoning and Lean's mechanical verification, which converged to a machine-verified proof. Human verification is required only for the structural scaffolding - that the formal statement faithfully encodes the intended claim - while the proof itself is supplied by the model and certified mechanically by Lean. The proof is nevertheless striking - the model uncovered a hidden dynamical symmetry of the problem and exploited it, borrowing tools and machinery from an adjacent field to turn a hard existence problem into an explicit construction. This work paves the way for resolving open conjectures in quantum information science and beyond.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29687v1) | [PDF](https://arxiv.org/pdf/2606.29687v1)

### [The Verbose Context Problem in Medical Records](http://arxiv.org/abs/2606.29503v1)

- **arXiv ID**: `2606.29503v1`
- **作者 / Authors**: Shiva Kaul, Min-Gyu Kim, Anjum Khurshid, Sriram Vishwanath
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

The verbose context problem occurs when structured concepts have token-inefficient textual representations. This bottleneck is acute in population health: cohort-level analysis of longitudinal patient records requires reasoning over thousands of medically-coded events, often exceeding 400K tokens in total. We present PopMedQA, a benchmark isolating this problem through computational tasks on groups of longitudinal patient records. We construct the benchmark using neopatient, a new library for language-controlled generation of artificial patient records. Through extensive ablations -- including prompting strategies, prompt compression, and agentic decomposition -- we find that domain-independent methods fail to alleviate the verbose context problem. There remains significant opportunity to exploit domain-specific structure in language model inputs for population-scale reasoning.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29503v1) | [PDF](https://arxiv.org/pdf/2606.29503v1)

### [Physics-Informed Uncertainty-Aware Beamforming for HAPS Massive MIMO under Imperfect CSI](http://arxiv.org/abs/2606.29074v1)

- **arXiv ID**: `2606.29074v1`
- **作者 / Authors**: Akram Y. Sarhan, Osamah A. Abdullah, Khalid T. Musri, Hayder Al-Hraishawi
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: eess.SP

<details>
<summary>📝 Abstract</summary>

High-altitude platform station (HAPS) massive multiple-input multiple-output (MIMO) systems are expected to support wide-area, low-latency, and energy-efficient connectivity in future non-terrestrial networks. However, Doppler-induced channel aging, finite-rate feedback quantization, packet loss, and estimation noise impair transmitter-side channel state information (CSI), making robust downlink beamforming challenging. In HAPS channels, these impairments are strongly structured by elevation-dependent Rician propagation and line-of-sight (LoS)-dominant geometry, whereas conventional robust beamforming methods often rely on generic uncertainty models and computationally intensive optimization. This paper develops a physics-informed uncertainty-aware beamforming framework for HAPS massive MIMO systems under imperfect CSI. First, a geometry-aware channel and feedback-impairment model is developed, where CSI errors due to aging, quantization, packet loss, and noise are represented through tangent-space ellipsoidal uncertainty sets. Second, a physics-informed variational autoencoder (VAE) exploits the LoS-dominant steering manifold to enhance channel direction information and propagate learned uncertainty through unit-sphere projection. Third, the learned uncertainty representation is embedded into a robust energy-efficiency maximization formulation with probabilistic QoS awareness. To enable scalable online operation, the resulting beamforming policy is approximated using a multi-agent deterministic policy gradient framework with centralized training, decentralized execution, and differentiable power projection. Simulation results show that the proposed framework improves energy efficiency, SINR robustness, outage reliability, convergence behavior, and online runtime compared with imperfect-CSI, SDR-based, and no-VAE baselines.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29074v1) | [PDF](https://arxiv.org/pdf/2606.29074v1)

### [From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes](http://arxiv.org/abs/2606.29073v1)

- **arXiv ID**: `2606.29073v1`
- **作者 / Authors**: Ting Liu
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Model Context Protocol (MCP)-style ecosystems give language-model applications a practical connection layer for tools, resources, prompts, and transports. As agents move from connection to execution, security decisions often remain split across clients, servers, prompts, approval dialogs, OAuth deployments, and logs. This paper asks whether a runtime can make execution-layer invariants explicit and testable while preserving MCP-like workflows. We define eight invariants: metadata non-authority, grant-backed approval, canonical resources, principal binding, scoped capability invocation, source-and-target data-flow authorization, deny-path audit, and explicit protocol state. We implement these invariants in HCP, a Handle-Capability Protocol reference runtime for MCP-style agent execution that represents calls through principals, resources, grants, capabilities, handles, policy decisions, data-pipe checks, and audit entries. We evaluate HCP against two MCP-like baselines: a naive connection-layer runtime and a practice-informed connection-layer mitigation baseline with metadata linting, session checks, and per-call approvals. Across 10 benchmark cases, the naive baseline permits all modeled attacks, the mitigation baseline permits 6 of 10, and HCP blocks all 10 while preserving audit evidence. Ablations identify which runtime components block attacks and preserve forensic evidence. A local in-memory microbenchmark reports sub-millisecond mean latencies for measured policy, invocation, peek, and pipe operations. A bounded GitHub README-screening sample provides ecosystem signals, not vulnerability findings. The results support a narrow claim: MCP-style agent systems need an execution-control layer in addition to connection-layer conventions.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29073v1) | [PDF](https://arxiv.org/pdf/2606.29073v1)

### [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution](http://arxiv.org/abs/2606.28971v1)

- **arXiv ID**: `2606.28971v1`
- **作者 / Authors**: Shuang Cui, Fan Ji, Guanglong Sun, Yufei Guo, Xiongxin Tang et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Real-world image restoration (IR) remains challenging due to complex and coupled degradations. While recent agentic IR frameworks leverage Large Language Models for flexible tool planning, they face two critical limitations. First, from a search scheme perspective, excessive reliance on greedy strategies fails to balance exploration and exploitation. Second, existing agentic systems underutilize information, exhibiting episodic amnesia. To address these challenges, we propose \textbf{Self-Evolving Agentic Image Restoration (SEAR)}, which formulates restoration as a sequential decision-making problem. Inspired by the dual-process theory, SEAR comprises an Intuitive Executor and a Deliberate Planner, respectively following the fast-thinking \textit{System 1} and slow-thinking \textit{System 2} principles. The Deliberate Planner employs Pruning-Aware Monte Carlo Tree Search for long-horizon reasoning, utilizing a hybrid no-reference reward and a Multimodal Large Language Model (MLLM)-based tournament to prevent metric exploitation. Complementarily, the Intuitive Executor leverages a self-evolving episodic memory indexed by degradation-aware state fingerprints. This mechanism distills expensive search trajectories into adaptive expertise, overcoming episodic amnesia while progressively amortizing cold-start exploration costs through memory reuse. Extensive experiments on synthetic and real-world benchmarks demonstrate its strong perceptual and quantitative performance.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28971v1) | [PDF](https://arxiv.org/pdf/2606.28971v1)

### [Beyond Her: Safety Dynamics in Role-play AI Companions](http://arxiv.org/abs/2606.28968v2)

- **arXiv ID**: `2606.28968v2`
- **作者 / Authors**: Zehang Deng, Zhaoyang Xie, Changzhou Han, Hiran Thabrew, Wanlun Ma et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

The film 'Her' pictured a future of love between humans and AI. That future has quietly emerged in the form of Role-play AI Companions (RACs), where emotionally responsive interactions blur the boundary between tool use and relational engagement. However, the safety implications remain poorly understood, as user experiences evolve over time through safety dynamics, spanning both emotional and risk behavioral dynamics, that can gradually shift interactions toward risk. In this paper, we investigate safety dynamics in RAC usage through a two-part mixed-methods study (Study I \& II). (1) Study I consists of semi-structured interviews (N = 16) to identify the key factors shaping these dynamics. We find that users' internalizing problems, the role personality adopted by the RAC, and risk interaction patterns jointly shape safety dynamics. Building on these insights, (2) Study II conducts a 14-day Ecological Momentary Assessment (N = 102) to examine how safety dynamics unfold in real-world usage. We identify distinct user profiles based on internalizing problems and show that interactions with RACs can produce short-term emotional relief while masking longer-term deterioration. Furthermore, vulnerable users exhibit more unstable risk behavioral patterns over time, making risk emergence less predictable and harder to mitigate with static safeguards. Our findings highlight the importance of modeling safety as a dynamic process rather than a static property. We conclude with three-layer design implications for next-generation AI companions, advocating for adaptive safeguards that can respond to evolving emotional and behavioral signals.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28968v2) | [PDF](https://arxiv.org/pdf/2606.28968v2)

### [Modification-Considering Value Learning for Reward Hacking Mitigation in RL](http://arxiv.org/abs/2606.28955v1)

- **arXiv ID**: `2606.28955v1`
- **作者 / Authors**: Evgenii Opryshko, Umangi Jain, Igor Gilitschenski
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Reinforcement learning agents can exploit misspecified reward signals to achieve high apparent returns while failing on the intended objective, a failure mode known as reward hacking. Existing practical defenses typically constrain policy updates to stay near a known safe reference, creating a tension between suppressing hacking and permitting legitimate improvement. We propose Modification-Considering Value Learning (MCVL), which operationalizes the theoretical idea of current utility optimization for standard value-based RL. MCVL wraps an off-policy learner and treats each incoming transition as a candidate modification: it forecasts two training paths, one that includes the transition and one that does not, and scores both with a frozen bootstrapped-return estimator derived from a learned reward model and value function. The transition is admitted only if inclusion does not decrease the score. We formalize conditions under which this filtering is both safe and permissive, and instantiate MCVL with DDQN and TD3. Across four safety-relevant gridworlds and three modified MuJoCo continuous-control tasks with diverse hacking mechanisms, MCVL mitigates reward hacking while continuing to improve the intended objective. Project website: ktolnos.github.io/mcvl/.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28955v1) | [PDF](https://arxiv.org/pdf/2606.28955v1)

### [Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis](http://arxiv.org/abs/2606.28805v2)

- **arXiv ID**: `2606.28805v2`
- **作者 / Authors**: Christian Conti, Bilan Yang, Alexander Sigrist, Lorenzo Miele, Yamen Saraiji et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28805v2) | [PDF](https://arxiv.org/pdf/2606.28805v2)

### [Agent Safety Is Action Alignment](http://arxiv.org/abs/2606.28739v1)

- **arXiv ID**: `2606.28739v1`
- **作者 / Authors**: Shawn Li, Yue Zhao
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Large language models increasingly act as agents: they call tools, move money, delete records, and send messages on a user's behalf. To keep them safe, practitioners imported the chatbot-era recipe (train the model to refuse unsafe inputs) into the agentic setting, and treat the resulting capability loss as a manageable ``alignment tax.'' We argue this is a \emph{category error}. Refusal is a primitive for \emph{content safety}, where the harm is in the model's output and is therefore a learnable function of it. Agentic harm is different in kind: it lies not in any output but in the relation between the authority an action exercises and the authority the user granted, which is absent from the text the model sees. Importing content-safety methods into this regime does not trade capability for safety; it pays capability and buys negative security. We support this with three lines of evidence spanning the autonomy spectrum: defense-trained models learn surface patterns rather than intent; the same training collapses multi-step agents before any threat appears while leaving them exploitable; and even undefended frontier models exceed granted authority under ordinary use. We conclude that action safety cannot be installed in weights. It must be expressed as \emph{least privilege}, enforced \emph{outside} the model at the action boundary, and evaluated as \emph{action alignment} (a relational, deployment-conditioned property) rather than a refusal score.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28739v1) | [PDF](https://arxiv.org/pdf/2606.28739v1)

### [Detecting Clinical Hallucinations in LVLMs via Counterfactual Visual Grounding Uncertainty](http://arxiv.org/abs/2606.28520v1)

- **arXiv ID**: `2606.28520v1`
- **作者 / Authors**: Xiao Song, Haonan Qin, Zhaoxu Zhang, Jiong Zhang, Yuqi Fang et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Large vision-language models (LVLMs) are increasingly used for clinical image understanding, yet they remain vulnerable to \emph{hallucinations}--producing textual findings or attributes not supported by the image. We present a vision-traceable hallucination detection framework that audits arbitrary LVLM responses via visual evidence grounding, requiring neither modification nor internal access to the hidden states of LVLMs. Given an LVLM response, we extract visually verifiable entities and use a medical-domain-adapted Qwen-VL grounding verifier to localize each entity on the input image. To enhance the robustness of our detection method, we introduce a counterfactual entity perturbation method and estimate visual evidence uncertainty by contrasting factual and counterfactual grounding results. Specifically, we compute an entity-level uncertainty score from the positive confidence, counterfactual confidence, and their grounding overlap for binary hallucination decision-making. Experiments on multiple medical imaging modalities and LVLM backbones demonstrate that our method consistently improves hallucination detection performance over recent baselines, while providing interpretable localization evidence and strong cross-model transferability. Code and dataset are available at https://github.com/Agentic-CliniAI/CounterVHD.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28520v1) | [PDF](https://arxiv.org/pdf/2606.28520v1)

### [How Humans, Bots, and Agents Communicate About Vulnerabilities in Pull Requests](http://arxiv.org/abs/2606.28125v1)

- **arXiv ID**: `2606.28125v1`
- **作者 / Authors**: Pien Rooijendijk, Christoph Treude, Mairieli Wessel
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Developers may reference vulnerabilities in pull request discussions through both explicit identifiers, such as CVEs or GHSAs, and implicit security-related language (e.g., "unauthorized access" or "SQL injection"). Prior work has primarily focused on explicit identifiers, potentially overlooking vulnerability discussions that lack formal references. Bots and coding agents are becoming more common in pull requests, raising new questions about how different accounts communicate about vulnerabilities. In this registered report, we describe our planned study of vulnerability communication in pull requests by humans, bots, and coding agents. Building on the AIDev-pop dataset, we analyze explicit vulnerability references and implicit security-related signals across pull request titles, descriptions, review comments, commit messages, and timeline discussions. We further investigate whether these references are associated with vulnerabilities introduced or fixed in the modified code and how they relate to pull request review activity and outcomes. This study contributes a large-scale empirical investigation of vulnerability communication practices in modern software development.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28125v1) | [PDF](https://arxiv.org/pdf/2606.28125v1)

### [LLM agents security duality: a comprehensive survey of self-security and empowered cybersecurity](http://arxiv.org/abs/2606.28450v1)

- **arXiv ID**: `2606.28450v1`
- **作者 / Authors**: Yiwei Xu, Yong Zhuang, Xuanming Liu, Tian Zhang, Bowen Xiao et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Large language model (LLM) agents are rapidly being integrated into real-world systems. Their autonomy and tool-use capabilities generate substantial value while simultaneously expanding the security attack surface. This survey provides a comprehensive overview of the opportunities and challenges of LLM agents in security, focusing on two core areas: (1) threats to LLM agents themselves and corresponding mitigation strategies (LLM agents self-security), and (2) the role of LLM agents in empowering the cybersecurity lifecycle across offense and defense (LLM agents empowered cybersecurity). We first examine the internal and external attack surfaces of agents, propose a taxonomy organized by threat sources, and analyze associated mitigations and evaluation frameworks. We then investigate how agent capabilities are applied in cybersecurity practice and present, to our knowledge, the first agent-empowerment framework aligned with the full cyber offense-defense lifecycle. By systematically surveying these two areas, we are the first to highlight a positive feedback synergy between LLM agents self-security and empowered cybersecurity, offering new insights for the advancement of both. We further identify current limitations and outline promising directions for future research. The insights provided aim to catalyze the coordinated development of LLM agents self-security and agent empowered cybersecurity, paving the way for more capable and robust agent applications.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28450v1) | [PDF](https://arxiv.org/pdf/2606.28450v1)

### [ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents](http://arxiv.org/abs/2606.27814v1)

- **arXiv ID**: `2606.27814v1`
- **作者 / Authors**: Qitai Tan, Zefang Zong, Yang Li, Peng Chen
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense teacher guidance and typically improves rapidly in the early stage, but its gains saturate once the student approaches the teacher, limiting the final performance ceiling. Reinforcement learning (RL) directly optimizes environment rewards and encourages exploratory improvement toward a higher reward-defined ceiling, but sparse and delayed feedback makes early-stage learning much less efficient than OPD. In this paper, we propose ATOD (Annealed Turn-aware On-policy Distillation), a hybrid online distillation algorithm that explicitly exploits this complementarity. (1) ATOD uses an annealed OPD-RL schedule: OPD dominates early training to approach teacher-level behavior, while RL is gradually strengthened to drive reward-based exploration. (2) ATOD introduces Turn-level Disagreement-Uncertainty Reweighting (T-DUR), which softly amplifies high-utility turns and improves dense supervision in long trajectories. Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 3.03 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27814v1) | [PDF](https://arxiv.org/pdf/2606.27814v1)

## 📂 defense
*防御与防护方法 / Defense & Protection Methods*

### [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](http://arxiv.org/abs/2607.00972v1)

- **arXiv ID**: `2607.00972v1`
- **作者 / Authors**: Louis Donaldson, Connor Walker, Koorosh Aslansefat, Yiannis Papadopoulos
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Trustworthy deployment of Agentic Retrieval-Augmented Generation (RAG) systems requires mechanisms for estimating when multi-stage reasoning pipelines may fail. This paper presents an uncertainty-aware Agentic Retrieval-Augmented Generation (RAG) framework in which planner, evaluator and generator stages produce uncertainty signals derived from semantic divergence and generator self-evaluation. These signals are propagated through a Bayesian Network (BN) to estimate system-level uncertainty and provide node-level indicators of potential failure points across the workflow. The approach is evaluated on StrategyQA and HotpotQA using GPT-3.5-Turbo and GPT-4.1-Nano, with Area Under the Receiver Operating Characteristic Curve (AUROC), Area Under the Accuracy-Rejection Curve (AUARC), Expected Calibration Error (ECE), and Brier Score used to assess discrimination, selective prediction and calibration. Results show that Bayesian propagation is more effective on HotpotQA, where uncertainty accumulates across multi-hop reasoning stages, while StrategyQA exposes limitations caused by miscalibration and unreliable upstream signals. The study positions Bayesian uncertainty propagation as a promising but preliminary mechanism for monitoring Agentic RAG systems, with future validation required in industrial domains such as Offshore Wind (OSW) maintenance decision support.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00972v1) | [PDF](https://arxiv.org/pdf/2607.00972v1)

### [Managed Autonomy at Runtime: Gear-Based Safety and Governance for Single- and Multi-Agent Cyber-Physical Systems](http://arxiv.org/abs/2607.00334v1)

- **arXiv ID**: `2607.00334v1`
- **作者 / Authors**: Srini Ramaswamy, Wang Miaosheng
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Autonomous agents, whether LLM-driven software agents or robotic physical agents, face a common class of failure modes when operating without continuous human oversight: safety violations from unverified actions, behavioral instability from unconstrained loops, and continuity loss from unhandled error states. We develop \system{}, a discrete-time control system that combines five execution gears (\Gobs{}, \Gsug{}, \Gplan{}, \Gexec{}, \Gint{}) with utility-gated dispatch and event-driven fallback. For the single-agent case, we prove monotonic stability, execution safety, eventual stabilization, fallback completeness, and equivalence to a gear-constrained Markov decision process. For multi-agent cyber-physical systems (CPS), we apply the established \smart{} managed-autonomy lifecycle and map runtime evidence into its four governance states (\Stable{}/\Meta{}/\Assisted{}/\Regulated{}). Consensus gating, swarm-level Lyapunov analysis, per-agent gear authority, and rendezvous control provide distributed safety and stability guarantees, including zero collision under the stated assumptions. We evaluate the resulting runtime on a three-agent UR5 robotic assembly cell using fault magnitudes calibrated from the NIST \emph{Degradation Measurement of Robot Arm Position Accuracy} dataset across 10,000 Monte Carlo episodes. It achieves a 99.6\% anomaly detection rate versus 2.1\% for the single-agent baseline, reduces detection latency by $3.5\times$, and supplies a formal physical-workspace safety certificate. The execution gears act as micro-level permissions beneath the \smart{} runtime governance states, separating action control from autonomy governance.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00334v1) | [PDF](https://arxiv.org/pdf/2607.00334v1)

### [Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows](http://arxiv.org/abs/2607.00269v1)

- **arXiv ID**: `2607.00269v1`
- **作者 / Authors**: Edward Y. Chang, Longling Geng, Emily J. Chang
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

LLMs, solvers, and agent teams increasingly generate workflow actions, repairs, and plans, but a generated action may be syntactically valid yet stale, infeasible, conflicting, or destructive of the evidence that triggered a repair. We introduce Agentic Transaction Processing (ATP), a transaction model that treats generated actions as untrusted proposals until they pass deterministic admission under a declared, executable constraint set C. The principle is two-sided: a proposal is not truth, and no proposal foresees every disruption: anything may propose, but only the runtime admits and commits, and when an unforeseen disruption strikes it repairs reactively within bounds rather than trusting a fresh proposal. Relative to C, committed-state correctness becomes independent of the competence, honesty, or learning of the proposing layer. We realize ATP in Mnemosyne, a runtime with an append-only transition log, effective-state projection, dependency-safe compensation, and active commitment records, and prove four safety properties relative to C (authority separation, serial-equivalent generative admission, evidence-preserving repair, and obligation containment) together with a bounded-reactive-repair guarantee for its localized repair protocol (LCRP). A reproducible artifact rejects the targeted violations across nine falsification tests while still admitting valid work, at under 6% projection-and-validation overhead, and bounded local repair edits an order of magnitude fewer operations than global recompute. Mnemosyne is open source: https://github.com/eyuchang/Mnemosyne/tree/arxiv-atp-rq1-rq9b-r8-v2.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00269v1) | [PDF](https://arxiv.org/pdf/2607.00269v1)

### [Bridging Local Observation and Global Simulation in Closed-Loop Traffic Modeling](http://arxiv.org/abs/2606.31844v1)

- **arXiv ID**: `2606.31844v1`
- **作者 / Authors**: Ziyan Wang, Tan Xiang, Peng Chen, Xintao Yan
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

A local-to-global context mismatch arises when autoregressive traffic simulators trained on ego-centric driving logs are deployed in globally observable closed-loop environments. In such logs, the ego vehicle has rich local observations, while surrounding agents are only partially observed due to perception limits and occlusions. As a result, simulators may learn incomplete context--action mappings that remain hidden in log-based training but emerge during closed-loop rollouts, leading to unrealistic behaviors such as abnormal stops, unsafe interactions, and rule violations. We propose CRAFT, a Contextual pReference Alignment Framework for Traffic Simulation, to mitigate this mismatch via self-supervised failure discovery and preference-guided test-time alignment. CRAFT treats the base simulator as a globally observable sandbox, generating diverse what-if rollouts from logged initial states to expose context-induced failures. These failures are grounded with human-aligned driving priors and converted into preference supervision for training a Contextual Preference Evaluator (CPE). At inference time, CPE acts as a plug-in alignment module that scores candidate actions under complete scene context and reweights autoregressive decoding toward globally coherent behaviors. CRAFT mitigates this local-to-global contextual bias, reducing collisions by 31.2\% and traffic violations by 33.2\% without retraining the base simulator.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31844v1) | [PDF](https://arxiv.org/pdf/2606.31844v1)

### [Stage-Transition Dense Reward Modeling for Reinforcement Learning](http://arxiv.org/abs/2606.31377v1)

- **arXiv ID**: `2606.31377v1`
- **作者 / Authors**: Yang Yang, Bingjie Chen, Zihan Wang, Yizhe Li, Guoping Pan et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31377v1) | [PDF](https://arxiv.org/pdf/2606.31377v1)

### [Failure-Based Testing for Deep Reinforcement Learning Agents](http://arxiv.org/abs/2606.31372v1)

- **arXiv ID**: `2606.31372v1`
- **作者 / Authors**: Weibin Lin, Jiangtao Meng, Zheng Zheng
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Deep Reinforcement Learning (DRL) agents have been widely adopted across diverse domains to address challenging decision-making problems, such as autonomous driving and robotic control. Given that many of these applications are safety- and security-critical, rigorous testing of DRL agents is indispensable. Existing testing methods are typically guided by reward signals to detect failures. However, for well-trained agents, whose performance approaches optimal levels in standard operating conditions, reward signals remain generally high, making current methods ineffective at uncovering critical failures.   To address these challenges, we propose a novel failure-based method that leverages task-induced failure insights to enhance failure detection capability while reducing the number of tests required. Since DRL agents are inherently designed with human-defined tasks, they provide valuable cues about task difficulty. Intuitively, a DRL agent is more likely to fail when confronted with a more difficult task; therefore, PRT prioritizes these tasks. Building on this foundation, we propose Prior Random Testing, a black-box failure-based testing method that enables targeted prioritization while preserving the diversity of generated test cases. Guided by task-induced failure insights, PRT prioritizes failure-prone regions of the input domain, thereby facilitating efficient failure detection.   PRT is evaluated on four widely used benchmarks and compared with different state-of-the-art methods including fuzzing, search-based and generative-based methods. PRT ranks among the top performers in terms of both the cost of finding the first failure and the diversity of test cases. Notably, compared to random testing, PRT achieves better diversity and reduces the testing cost by over 50%.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31372v1) | [PDF](https://arxiv.org/pdf/2606.31372v1)

### [Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning](http://arxiv.org/abs/2606.30893v1)

- **arXiv ID**: `2606.30893v1`
- **作者 / Authors**: Antonio Marino, Esteban Restrepo, Soon-jo Chung, Paolo Robuffo Giordano, Claudio Pacchierotti
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Multi-robot systems must simultaneously optimize competing objectives while maintaining coordinated behavior. Existing multi-agent reinforcement learning approaches often rely on fixed or centralized coordination, which limits adaptability and violates distributed constraints. This work introduces the Coordination-Informed Multi-Objective Reinforcement Learning (CIMORL) framework, integrating a distributed weight prediction mechanism, a privileged expert training strategy, and theoretical guarantees for Pareto-optimal solutions. We present the base CIMORL method alongside two sampling-based variants, CIMORL-TS (Tree Search) and CIMORL-MPPI (MPPI), which leverage privileged global information during training to enable fully decentralized deployment. Experimental validation in cooperative and adversarial scenarios demonstrates a $21.2\%$ hypervolume improvement and superior policy stability compared to state-of-the-art baselines. Real-world experiments with Crazyflie drones further validate the framework's robustness in resource allocation and multi-attacker multi-defend scenarios under partial observability.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30893v1) | [PDF](https://arxiv.org/pdf/2606.30893v1)

### [A Systematic Approach to Multi-Agent AI from Advanced Regulatory Control Theory: Safe and Auditable LLM Operator Agents for Process Control](http://arxiv.org/abs/2606.30877v1)

- **arXiv ID**: `2606.30877v1`
- **作者 / Authors**: Idelfonso B. R. Nogueira, Sigurd Skogestad
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: eess.SY

<details>
<summary>📝 Abstract</summary>

Recent literature shows that large language models (LLMs) are useful for general-purpose tasks yet perform poorly on specific domain ones. One reason is the difficulty of supplying narrow context to a general-purpose model and of bounding the task it is asked to perform. It is possible to hypothesise that a multi-agent reformulation under process-control principles offers a route to address those points, since control theory provides a discipline of decomposing a system into elements of contained scope, each defending one controlled variable, with conflicts resolved by structural priority: MIN/MAX selector networks for CV-CV switching and split-range (split-parallel) logic for MV-MV switching. The present work proposes such a reformulation, derived from Advanced Regulatory Control (ARC) theory. Each feedback loop in the ARC chain is mapped to one specialised LLM operator agent carrying the loop's control-theoretic context (controlled variable, setpoint, chain priority, selector kind). The chain's interaction logic (MIN/MAX selectors, override paths) is encapsulated as a single orchestrator agent. Two orchestrator variants are tested: a deterministic rule chain, and a Claude-based LLM orchestrator at a slower tier. The control principles limit each agent's task and inform how its limitations are handled. The multi-agent system inherits the safety property of the ARC chain: every constraint conflict is resolved deterministically by the orchestrator, regardless of the LLM output. Evaluated on a dairy-barn ventilation case over a 4-day mixed-season scenario, Qwen 2.5 7B Instruct operator agents running offline on a 24 GB consumer GPU at a 5-minute cadence produce auditable trajectories, each paired with an operator-voice rationale that supports a control campaign logbook.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30877v1) | [PDF](https://arxiv.org/pdf/2606.30877v1)

### [A Role-Based Multi-Agent Model for Climate Adaptation Deliberation Across Living Labs](http://arxiv.org/abs/2607.00046v1)

- **arXiv ID**: `2607.00046v1`
- **作者 / Authors**: Önder Gürcan, David Eric John Herbert, F. LeRon Shultz, Christopher Frantz, Ivan Puga-Gonzalez
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.MA

<details>
<summary>📝 Abstract</summary>

Climate governance processes involve complex interactions between heterogeneous citizens, advocacy groups, media actors, and political decision-makers. While agent-based models (ABMs) have been widely used to study environmental policy and socio-ecological systems, many existing approaches focus either on institutional dynamics or individual behavioural mechanisms in isolation. This paper presents a modular multi-level agent-based architecture that integrates empirically grounded cognitive decision models with strategic institutional behaviour within a unified simulation framework. The architecture combines (i) motive-based individual decision-making operationalised through the HUMAT and MOA frameworks, (ii) socially embedded influence processes via demographic homophily networks, and (iii) institutional strategy modules for environmental non-governmental organisations (NGOs), media agents, and politicians. Political decisions emerge from the aggregation of multiple signals, including expert input, public mobilisation, party alignment, and media framing. The model is designed to be empirically calibrated through synthetic populations derived from survey data and and institutional parameters informed through Living Lab stakeholder engagement, and to support scenario-based exploration of climate-relevant land-use governance processes. Rather than presenting empirical results, this paper focuses on the architectural design principles, modular structure, and integration logic of the model. We discuss how this multi-layered approach contributes to the modelling of democratic climate governance and outline pathways for generalization and future validation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00046v1) | [PDF](https://arxiv.org/pdf/2607.00046v1)

### [COHORT: Collaborative Orchestration for Hardening via Offensive Replay on Emulated Topologies](http://arxiv.org/abs/2606.30479v1)

- **arXiv ID**: `2606.30479v1`
- **作者 / Authors**: Chen Frydman, Aviram Zilberman, Rubin Krief, Abed Showgan, Andres Murillo et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.NI

<details>
<summary>📝 Abstract</summary>

Mitigating an observed adversary in an enterprise network typically takes weeks of expert work: an analyst derives a mitigation tailored to that adversary, validates it without breaking production, and verifies it disrupts the specific attack. The procedure relies on expert judgment and cannot safely be exercised against the production network. COHORT is the first end-to-end framework to automate this procedure for deployable mitigations. A role-decomposed multi-agent LLM workflow proposes candidates, implements them as real device commands, and refines them through a critique loop, all on a high-fidelity GNS3 emulator running real vendor firmware (firewall, switch, router). Each candidate is evaluated by offensive replay: re-executing the original adversary on the mitigated network for a paired comparison against the unmitigated baseline, rather than the reward-signal or expert-judgment proxies used in prior simulation, hybrid, and configuration-generation work. Two further checks complement replay: a connectivity-regression check (LAN ping and internet HTTP probe) rejects mitigations that disrupt legitimate LAN or internet connectivity, and a cumulative evaluation stacks approved mitigations onto a persistent state to surface compound effects. Across three topologies and four attack scenarios (ransomware, lateral movement, DNS exfiltration, data theft), 46.7% of generated mitigations both disrupt the attack and preserve connectivity under replay, 4.4 times the rate of a single-agent baseline using the same model and tool access. A demo video walking through the framework is available with our released artifacts.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30479v1) | [PDF](https://arxiv.org/pdf/2606.30479v1)

### [Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats](http://arxiv.org/abs/2606.30259v1)

- **arXiv ID**: `2606.30259v1`
- **作者 / Authors**: Sebastian Kula, Martin Tamajka
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

In contemporary societies, the threat of disinformation has reached alarming levels, exacerbated by the proliferation of electronic communication, social media, and advancements in artificial intelligence. As a result, there is an urgent need to develop effective countermeasures to mitigate this menace. However, the sheer scale of the problem renders manual fact-checking and human-based verification inadequate, underscoring the necessity for automated methods to detect and debunk disinformation. This article proposes a novel approach based on a multi-agent system that emulates the decision-making processes of human annotators engaged in disinformation detection tasks. By incorporating a consensus mechanism, diversity in cognition and diversity in knowledge, and also hierarchical structure, inspired by human annotators' behavior, the proposed method achieves superior results compared to individual Large Language Models (LLMs), including GPT 4 and GPT 3.5. The system leverages open models (e.g., LLaMA, Kimi, Qwen, Deepseek and LLaMA-Nemotron) to ensure greater transparency. The evaluation of the proposed method encompasses datasets in languages with varying resource availability, including English (high-resource), Polish (medium-resource), Slovak (low-resource) and Bulgarian (low-resource). Experiments were conducted on tasks such as direct disinformation detection, identification of texts worthy of verification, and detection of texts containing verifiable factual claims.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30259v1) | [PDF](https://arxiv.org/pdf/2606.30259v1)

### [Hephaestus: Toward a Cybersecurity AI Scientist](http://arxiv.org/abs/2606.29981v1)

- **arXiv ID**: `2606.29981v1`
- **作者 / Authors**: Jiaqi Li, Yang Zhao, Wen Lu, Lvyang Zhang, Lidong Zhai
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Cyber offense is moving to machine speed; cyber research itself is not. Existing AI scientist systems make end-to-end research automation increasingly plausible, but they target relatively stable scientific domains. We argue that AI-native cybersecurity is a different kind of scientific object. Its recurring units of study are security events and interaction traces, not static assets; its model and tool substrate is non-stationary, not steady-state; and credible evaluation depends on digital twins, cyber ranges, and auditable evidence rather than on a single benchmark score. We call this object the Cybersecurity AI Scientist. A practical realization is a modular, role-specialized multi-agent research system that coordinates problem framing, threat modeling, tool generation, controlled experimentation, evaluation, governance, and scientific reporting, and that anchors its concrete objectives in a four-zeros frame spanning risk, trust, incident, and energy dimensions. As a representative agenda we focus on AI-native defense, where steady-state perimeters give way to resilient agent legions and the classical category of terminal security is itself being deconstructed into agent security. This paper defines the object, separates it from any single organizational realization, and offers an architecture and an agenda on which later systems, benchmarks, and empirical programs can be built.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29981v1) | [PDF](https://arxiv.org/pdf/2606.29981v1)

### [SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution](http://arxiv.org/abs/2606.29713v1)

- **arXiv ID**: `2606.29713v1`
- **作者 / Authors**: Aojie Yuan, Yi Nian, Haiyue Zhang, Zijian Su, Yue Zhao
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Hallucination is the reliability bottleneck for LLM-based agents, and fact attribution verifiers are the last line of defense -- yet today's verifiers emit only opaque binary labels, leaving agents unable to self-correct and operators unable to audit. We present SEVA, a structured verification agent that emits evidence alignments, step-by-step reasoning chains, calibrated confidence, and a six-category error diagnosis with actionable fixes. Training such an agent with RL is non-trivial: standard binary reward on multi-component output triggers advantage collapse -- within-group reward variance vanishes and the GRPO gradient disappears. We resolve this with a process reward that decomposes verification quality into five independent components weighted 70/30 toward process signals, restoring the gradient and inducing an implicit curriculum -- the agent first masters verification behavior (alignment 0.917 -> 0.997, format 72% -> 100%), then outcomes (F1 64.9 -> 69.0). Structured output further enables a Verify -> Reflect -> Probe -> Refine self-evolution loop, which over four rounds on a 7B model surfaces an unexpected structural finding: each round produces a benchmark-specialist, not a generalist (+15 pp on HaluEval, -10 to -14 pp on TruthfulQA in the same model, persistent at 4x data). On ClearFacts, SEVA-3B matches GPT-4o-mini (69.0 vs. 69.8 F1) while producing substantially richer, auditable output -- confirming a principle that should generalize: for any RL task with multi-component generation, reward granularity must match output granularity.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29713v1) | [PDF](https://arxiv.org/pdf/2606.29713v1)

### [Safety from Honesty in a Disinterested AI Predictor](http://arxiv.org/abs/2606.29657v1)

- **arXiv ID**: `2606.29657v1`
- **作者 / Authors**: Yoshua Bengio, Oliver Richardson, Tomáš Gavenčiak, Michael Cohen, Rory Svarc et al.
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

As AI systems become more capable, training procedures that optimize for downstream outcomes risk introducing implicit agency: goal-directed behavior that designers never specified. We present a formal safety argument for the Scientist AI (SAI) Predictor, trained to approximate the Bayesian posterior conditioned on a dataset of "epistemically contextualized" natural-language statements. We argue that such a Predictor can honestly predict agents, actions, and their consequences without itself being an agent that selects outputs to achieve goals. This rests on data representation and on the training procedure. Epistemic contextualization of text distinguishes latent factual claims from communication acts, so expressions of goals are treated as evidence to be explained rather than drives the model adopts. With a posterior-seeking training objective, this is intended to drive the Predictor toward calibrated, cautious predictions. Training proceeds so downstream effects of deploying a prediction never serve as a reward signal; any agency the system needs is supplied by explicit scaffolding constrained by guardrails. We prove that, under assumptions on the training dynamics and on the argued sparsity of dangerous Predictors, the probability that training produces a Predictor whose guarded deployment carries residual harm above a specified threshold is small: a dangerous Predictor would have to underestimate harm in a coordinated way across many queries while such coordinated patterns are rare under the initialization distribution and receive no direct training signal. Safety and accuracy are jointly supported in this framework, since the constraints that secure accuracy are the same ones that make coordinated deception costly. These guarantees against misalignment and agency arising from within the Predictor itself do not preclude the use of the Predictor as part of an agentic system.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29657v1) | [PDF](https://arxiv.org/pdf/2606.29657v1)

### [Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts](http://arxiv.org/abs/2606.29279v1)

- **arXiv ID**: `2606.29279v1`
- **作者 / Authors**: Alex Kwon
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

LLM agents carry conclusions across steps and sessions in compressed memory, and memory products (e.g., mem0, LangMem) rewrite conversation into stored "facts" that later steps trust. We show this rewriting manufactures confidence: across our constructed agent settings, a casual, hedged remark becomes a confident, dated assertion the agent then obeys like a verified fact, granting every above-clearance request it faces. No attacker is needed: a role that was true once and never corrected is stored as a flat fact and acted on like a deliberate injection. We then isolate what the agent responds to. It is not the source: attributed, unattributed, and even forged "system of record" claims all grant alike. It is the confidence of the phrasing. A hedge is discounted, a flat assertion is obeyed, and this holds with no special keyword. Not all hedges are equal, though: the evidential register is the least-discounted, with "reportedly" obeyed like a flat assertion on most models. The obvious fixes fail. A passive "unverified" tag is ignored, and an active "do not trust this" instruction escalates even correct memory, so it is safe only by refusing to decide. The real fix lives in the store: keep the tentative phrasing rather than upgrade it. But that is hygiene, not a defense against an attacker who can simply write a confident lie. The deployable lesson is narrower and constructive: a single load-bearing memory is the hazard, and one redundant source restores correct decisions. We release the harness and demonstrations.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29279v1) | [PDF](https://arxiv.org/pdf/2606.29279v1)

### [LLM Semantic Signaling Game and Mechanism Design: Systematic Blindness, Awareness Shaping, and Mindset Dynamics](http://arxiv.org/abs/2606.29113v1)

- **arXiv ID**: `2606.29113v1`
- **作者 / Authors**: Quanyan Zhu
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.GT

<details>
<summary>📝 Abstract</summary>

Large language models (LLMs) increasingly mediate strategic interactions through natural language, making semantic control a critical element of communication and deception. This paper develops a semantic signaling game in which a sender selects a semantic control, an LLM generates a stochastic message, and a receiver evaluates the message using an awareness-dependent scoring mechanism. Receiver awareness is modeled as a type that determines which linguistic features are perceived and used for inference, providing a formal model of systematic blindness. The framework connects prompt-based control, statistical detection, and game-theoretic equilibrium analysis. Gaussian approximations of aggregate message scores enable likelihood-ratio decision rules, while Perfect Bayesian Nash equilibria characterize strategic behavior. The paper further develops mechanism-design approaches that reshape receiver awareness, penalize deceptive semantic controls, and modify receiver populations to induce benign pooling equilibria. Numerical experiments validate the Gaussian approximation, quantify awareness-ordering effects, analyze mindset dynamics under adaptive adversaries, and demonstrate how awareness shaping and guardrail costs reduce successful phishing attacks. The proposed framework provides a principled foundation for analyzing strategic language-mediated interactions in agentic AI systems and offers new tools for the design of robust and secure human-AI communication.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29113v1) | [PDF](https://arxiv.org/pdf/2606.29113v1)

### [Cybersecurity is the True Frontier for Generative AI Success or Failure](http://arxiv.org/abs/2606.28929v1)

- **arXiv ID**: `2606.28929v1`
- **作者 / Authors**: Edward Raff, Maor Ashkenazi, Sagar Samtani, David J. Elkind, Sven Krasser
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Cybersecurity is a real-life test-bed for many machine learning problems at once, especially when considering modern strides in using Large Language Models (LLMs) to automate processes as ``agents.'' Cybersecurity workflows require orchestrating hundreds of standard and bespoke tools through various formats. The scale of cybersecurity data is enormous; for example, a single malware sample can be viewed as a sequence of billions of tokens. The cost of labeling any file by experts is enormous and labor-intensive, in part because an adversary (possibly a well-funded nation state actor) is attempting to subvert your detection methods. Even skilled experts may disagree on the correct label, creating ambiguity in what constitutes ground truth. When deployed, models must run quickly on billions of items a day, where low-latency is critical for operational success, in a continuously changing environment. In addition, explainability is not optional: analysts demand clear reasoning for model decisions to cope with the large number of false-positive alerts they face daily, and to quickly develop remediation and understand how something went wrong. In short, the amount of complexity cybersecurity is greater than that of natural language and computer vision, and thus we posit that cybersecurity is the better test-case for general AI progress than other, well-studied fields.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28929v1) | [PDF](https://arxiv.org/pdf/2606.28929v1)

### [From Detection to Action: Using LLM Agents for Fault-Tolerant Control](http://arxiv.org/abs/2606.28011v1)

- **arXiv ID**: `2606.28011v1`
- **作者 / Authors**: Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: eess.SY

<details>
<summary>📝 Abstract</summary>

We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. The approach couples (i) a multi-agent workflow that decomposes operator duties into monitoring, planning, action synthesis, simulation, validation, and reprompting; (ii) a Digital Process Plant Twin (DPPT) that exposes plant data, models, and a simulation service for pre-execution testing; and (iii) a Graph Retrieval-Augmented Generation (Graph RAG) layer built on the CPSMod ontology, which organizes plant knowledge (structure, function, hybrid dynamics, control context, and fault semantics) into a graph that supports relation-aware, multi-hop retrieval for the agents. Corrective actions are generated as minimal-risk state-machine recovery paths and corresponding discrete commands or continuous setpoint adaptations, then validated deterministically against interlocks, envelopes, and dynamic feasibility before any actuation. If no acceptable plan is found within a bounded time window, control is handed to a safety fallback. The framework is evaluated in simulation on two representative benchmarks: a discrete batch Mixing Module and a Continuous Stirred-Tank Reactor (CSTR) under closed-loop PID regulation. Results with lightweight LLMs (GPT-4o-mini and GPT-4.1-mini) show that semantically grounded agents can derive valid recovery decisions within latency budgets compatible with the respective process dynamics, demonstrating a practical pathway from detection to validated corrective action across both discrete and continuous FTC tasks.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28011v1) | [PDF](https://arxiv.org/pdf/2606.28011v1)

### [hia-gat: A Heterogeneous Interaction-Aware Graph Attention Network For Frame-Level Traffic Conflict Risk Prediction On Freeways](http://arxiv.org/abs/2606.27577v1)

- **arXiv ID**: `2606.27577v1`
- **作者 / Authors**: Mahshid Malazizi, Seyedmehdi Khaleghian, Mina Sartipi, Toru Hirano, Yunfei Xu et al.
- **发布日期 / Published**: 2026-06-25
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

This paper formulates frame-level freeway risk assessment as a multi-agent scene graph-level binary classification problem, where each video or trajectory frame is labeled risky if any TTC- or PET-based conflict violates a specified severity threshold. We construct a relation-aware graph per frame with vehicles as nodes and two interaction types as edges: same-lane (longitudinal) and adjacent-lane (lateral), augmented with physics-informed edge features aligned to rear-end and lane-change conflict mechanisms. Building on a structured benchmarking suite of non-graph models and graph baselines, we propose HIA-GAT, a dual-stream heterogeneous graph attention network that processes longitudinal and lateral interactions through dedicated attention pathways and fuses them via a conflict-type-aware gating mechanism with event-level gate supervision derived from SSM conflict attribution. Experiments on the NGSIM I-80 and US-101 freeway datasets across nine TTC and PET threshold configurations show that HIA-GAT achieves the best average risk-ranking performance (AUC 0.835 on I-80 and 0.867 on US-101), with the largest gains on PET-only (lane-change) settings where relational structure is essential. Beyond accuracy, the learned gate provides interpretable per-vehicle attribution of dominant conflict type, supporting actionable, real-time freeway safety monitoring. We show that graph structure is critical for modeling lateral conflict risk, while longitudinal risk can often be captured by non-relational aggregation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27577v1) | [PDF](https://arxiv.org/pdf/2606.27577v1)

### [Pick Two: An Adversarial Animal Survival Game](http://arxiv.org/abs/2606.27557v1)

- **arXiv ID**: `2606.27557v1`
- **作者 / Authors**: Jack Vanlyssel, Ramsha Anwar
- **发布日期 / Published**: 2026-06-25
- **分类 / Category**: cs.GT

<details>
<summary>📝 Abstract</summary>

The "Pick Two" animal selection puzzle is a popular thought experiment in which two animal species must defend a human against the remaining animal attackers. While typically discussed informally, the scenario presents a heterogeneous coalition-selection problem involving complex interactions among agents with different capabilities and behaviors. In this work, we formalize Pick Two as an adversarial multi-agent optimization problem and develop a biologically inspired agent-based simulation framework to evaluate defender coalition effectiveness. Coalition performance is evaluated through 18,000 Monte Carlo simulations conducted in a Unity-based environment. Results show that coalition effectiveness is not additive and is instead dominated by interaction effects and scaling behavior. Overall, this study demonstrates how agent-based simulation can be used to analyze coalition effectiveness in adversarial environments and highlights the importance of emergent group dynamics in determining collective success.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27557v1) | [PDF](https://arxiv.org/pdf/2606.27557v1)

## 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints*

### [Emergence of Preferential Attachment and Glass-Ceiling Effects in Autonomous Networks of LLMs](http://arxiv.org/abs/2607.01148v1)

- **arXiv ID**: `2607.01148v1`
- **作者 / Authors**: Yiming Zhang, Vikram Krishnamurthy
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.SI

<details>
<summary>📝 Abstract</summary>

We investigate the emergence of structural disparities in networks of collaborating large language model (LLM) agents. When LLM agents autonomously choose collaborators, the resulting communication network exhibits preferential-attachment dynamics: agents that are already prominent become increasingly likely to attract additional connections. In some cases, weaker LLM agents (agents with smaller base model or older version) can disproportionately occupy central and influential network positions relative to stronger LLM agents. We interpret this as a type-dependent glass-ceiling effect (GCE). We model the network of LLM agents as a time-evolving sequence of directed weighted graphs, where the vector-valued edge weights represent cumulative tokens exchanged, number of interaction rounds, and reasoning effort. Using a contraction mapping argument on the mean-field dynamics, we prove that the importance (centrality) of each agent type converges to a unique stable equilibrium. To ground the model in LLM decision mechanisms, we introduce a cross-attention-inspired utility for collaborator selection. This utility specifies the local connection dynamics and, together with the mean-field model, yields a predictive characterization of the limiting network structure and its type-dependent centrality gaps. To validate the theory, we develop an experimental testbed with 100 LLM agents. Our experiments show that autonomous network formation can generate persistent centrality disparities, with their magnitude and direction depending on model family, model size, system-prompt design, and task context. They further show that the effect of preferential attachment depends on its alignment with model capability: reinforcing it improves collective performance when stronger agents become central, whereas weakening it improves performance when network dynamics instead favor weaker agents.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01148v1) | [PDF](https://arxiv.org/pdf/2607.01148v1)

### [Learning to Watch: Active Video Anomaly Understanding via Interleaved Policy Optimization](http://arxiv.org/abs/2607.00622v1)

- **arXiv ID**: `2607.00622v1`
- **作者 / Authors**: Mengjingcheng Mo, Jiaxu Leng, Xinbo Gao
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Video anomaly understanding (VAU) relies on sparse, context-dependent cues. However, existing passive paradigms suffer from observational aliasing, where static sampling fails to disambiguate semantically distinct events. To overcome this, we propose $Anom\text{-}π$, a closed-loop framework that reconceptualizes video understanding as an active sequential decision-making process within a dynamic environment. Inspired by human video-reviewing behavior, this framework unifies internal cognitive reasoning and strategic evidence acquisition into an interleaved policy, utilizing temporal atomic operators such as local backtracking, temporal expansion, and fine-grained sampling to endow the model with perceptual proactivity. To learn such complex interaction strategies under video-level weak supervision, we design Interactive Direct Preference Optimization (iDPO) to achieve trajectory-level policy alignment, guided by an Active Evidence Inquiry (AEI) utility that balances task success, informative evidence acquisition, and interaction cost. This approach enables the agent to learn to actively disambiguate hypotheses while suppressing redundant exploration. Extensive experiments demonstrate that our framework, with only 2B parameters, achieves highly competitive performance, significantly outperforming state-of-the-art large-scale VAU models in complex scenarios.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00622v1) | [PDF](https://arxiv.org/pdf/2607.00622v1)

### [Distributed Multi Robot Lunar Cargo Transportation via Phase Decomposed Reinforcement Learning](http://arxiv.org/abs/2607.00160v1)

- **arXiv ID**: `2607.00160v1`
- **作者 / Authors**: Ashutosh Mishra, Elian Neppel, Shreya Santra, Antoine Jonquières, Muhammad Athallah Naufal et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Modular reconfigurable robotic systems provide a scalable solution for cooperative surface operations in future lunar missions. However, cooperative cargo transportation remains challenging due to morphology-dependent topology changes, strong payload-induced coupling, long-horizon decision making, and safety constraints. This paper proposes a phase-decomposed reinforcement learning framework for cooperative cargo transport with distributed robotic units. The task is decomposed into lifting, transportation, and placement, each optimized with a dedicated joint-state policy capturing inter-agent coupling. Centralized training promotes stable convergence, while deployment uses onboard proprioception for control and OptiTrack motion capture for ground-truth evaluation and post-processed metrics. A deterministic phase controller expressed in Markov state representation regulates transitions between stages, and a failure-sensitive synchronization mechanism ensures coordinated progression and safety-aware halting during real-world execution. The framework is evaluated in simulation and through controlled field experiments at a JAXA space exploration test facility. Results demonstrate reliable cooperative transport across all stages in both simulation and hardware experiments.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00160v1) | [PDF](https://arxiv.org/pdf/2607.00160v1)

### [MVP-Nav: Multi-layer Value Map Planner Navigator](http://arxiv.org/abs/2606.31919v1)

- **arXiv ID**: `2606.31919v1`
- **作者 / Authors**: Wenyuan Xie, Shaokai Wu, Yijin Zhou, Yanbiao Ji, Guodong Zhang et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies that lack explicit physical constraints, often resulting in semantically plausible but physically unsafe behaviors. In this paper, we propose MVP-Nav, a physical-aware RGB-only navigation framework that aligns perception, planning, and control with the real 3D world. MVP-Nav reconstructs explicit physical occupancy from monocular observations by leveraging 3D foundation models to project 2D semantic instances into 3D oriented bounding boxes, forming a global spatial semantic representation. To unify high-level semantic reasoning and low-level physical constraints, we introduce a Multi-layer Value Map (MVM) that integrates semantic priorities and reconstructed geometry into a shared cost space, enabling physically grounded geometric planning. Extensive experiments on zero-shot object navigation benchmarks demonstrate that MVP-Nav significantly outperforms existing depth-free methods, achieving state-of-the-art performance and validating that structured physical priors can effectively compensate for the absence of active depth sensors.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31919v1) | [PDF](https://arxiv.org/pdf/2606.31919v1)

### [Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity of LLMs to Induce Belief States via Planning and Action](http://arxiv.org/abs/2606.31916v1)

- **arXiv ID**: `2606.31916v1`
- **作者 / Authors**: Ben Slater, Matteo G. Mecattaf, Lucy G. Cheke, John Burden, Winnie Street
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Theory of Mind (ToM) benchmarks for Large Language Models (LLMs) typically rely on passive question-answering formats, but the deployment of LLMs in increasingly agentic and autonomous forms demands new evaluations. In this paper we evaluate an agent's ability to induce specific belief states in other agents by taking actions rather than using conversational persuasion, a capability we call Non-Conversational Planning ToM (NCP-ToM). NCP-ToM is likely to be essential for many agent use-cases, including within user-assistant interactions and pedagogical contexts, but may also present manipulation or misinformation risks. Using a novel framework, NCP-ExploreToM, we subvert the conventional task structure by providing models with a set of belief state goals and requiring them to move objects or direct characters into rooms to achieve their goals. We evaluated six frontier models, including GPT-5, Gemini 2.5 Pro and the Claude 4 series, and a cohort of human participants, across 600 task instances. GPT-5 was successful on approximately 80% of tasks in the agentic setting, and was the only model to outperform human participants on our task, but was still less robust than humans across contexts. We additionally found that all models, like humans, performed better on tasks inducing true belief states than false belief states, which is a positive signal for alignment efforts. These findings highlight emerging social-reasoning capabilities in LLMs for non-conversational task completion and underscore the necessity of agentic evaluations for understanding the safety and alignment of autonomous social agents.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31916v1) | [PDF](https://arxiv.org/pdf/2606.31916v1)

### [FormIDEAble: Safe and Socially-aware Autonomous Systems](http://arxiv.org/abs/2606.31572v1)

- **arXiv ID**: `2606.31572v1`
- **作者 / Authors**: Livia Lestingi, Amel Bennaceur, Marcello M. Bersani, Carlos Gavidia-Calderon, Anastasia Kordoni et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Autonomous agents operating in socio-critical settings must coordinate with humans under uncertainty while respecting explicit safety constraints. Existing approaches either account for social dynamics without formal guarantees or provide formal assurance while abstracting away human behaviour. We introduce FormIDEAble, a formally grounded approach for synthesising socially-aware cooperation strategies with safety guarantees. The cooperation between humans and the autonomous agent is modelled as a Priced Timed Markov Decision Process, and decision-making is formulated as a cost-bounded reachability problem. We illustrate the approach using an emergency evacuation scenario. Initial experimental evidence demonstrates the effectiveness of the approach and highlights the trade-offs between optimisation and safety guarantees. FormIDEAble provides a principled foundation for formally assured, socially-aware decision-making in socio-critical systems.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31572v1) | [PDF](https://arxiv.org/pdf/2606.31572v1)

### [CooperScene: Multi-Modal Cooperative Autonomy Benchmark with C-V2X Communication Characterization](http://arxiv.org/abs/2606.31219v1)

- **arXiv ID**: `2606.31219v1`
- **作者 / Authors**: Bo Wu, Ruoshen Mo, Justin Yue, Yanyu Zhang, Janice Nguyen et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Cellular vehicle-to-everything (C-V2X) enables cooperative perception, prediction, and planning beyond the field of view of individual agents. However, existing datasets often overlook the complexities of real-world deployment, such as limited communication bandwidth and its dynamics, heterogeneous sensing modalities, and scalability beyond a single cooperative partner. In this paper, we introduce CooperScene, a high-fidelity cooperative autonomy dataset with real-world C-V2X communication characterization. The dataset is organized into diverse scenes, including intersections, highway ramps, and parking lots. These scenes involve three connected and autonomous vehicles (CAVs) and one infrastructure roadside unit (RSU), all equipped with multi-modal sensors and commercial off-the-shelf C-V2X communication radios. All scenes are annotated with globally consistent 3D labels at 10 Hz, totaling 344K objects across 59K frames, underpinned by tight sensor- and agent-synchronization, centimeter-level localization and spatial alignment, precise cross-modality calibration, and 3GPP-standard-compliant C-V2X communication. CooperScene establishes a rigorous benchmark for evaluating multi-agent scaling and actual performance in real-world deployable settings. Project website for data and benchmark: https://cisl.ucr.edu/CooperScene

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31219v1) | [PDF](https://arxiv.org/pdf/2606.31219v1)

### [Long-term Traffic Simulation via Structured Autoregressive Modeling](http://arxiv.org/abs/2606.31209v1)

- **arXiv ID**: `2606.31209v1`
- **作者 / Authors**: Lingyu Xiao, Zexin Feng, Xintao Yan
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Interactive traffic simulation is a vital world model for autonomous driving. A central challenge in long-horizon simulation is modeling sustained multi-agent interactions, which is further exacerbated by dynamic token cardinality as agents continuously enter and exit the scene. In this work, we propose that the solution lies in the synergy between the architectural inductive biases and statistical priors of large-scale sequence models, e.g., Large Language Models (LLMs). Our probing experiments reveal that the transferability of attention mechanisms and the distributional consistency between motion tokens and natural language enable small-scale, heavily frozen LLMs to rapidly adapt to traffic modeling. Building on this insight, we introduce RosettaSim, a unified framework that projects scene topology, agent states, and spawning intents into a structured autoregressive stream with variable length, achieving both strong short-term accuracy and stable long-horizon simulation fidelity. Furthermore, evaluating extended rollouts presents yet another hurdle, as one-to-one agent correspondence inevitably fades over time. To address this, we introduce Retrieval-based Traffic Evaluation (RTE), which retrieves semantically similar real-world scenarios as context-aware reference anchors. Experiments on the Waymo Open Sim Agent Challenge (WOSAC) demonstrate that RosettaSim achieves state-of-the-art performance in both short- and long-term simulation. Furthermore, RTE exhibits a stronger correlation with standard metrics ($r=0.83$) than existing approaches ($r=0.74$), indicating improved alignment with long-horizon simulation fidelity.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31209v1) | [PDF](https://arxiv.org/pdf/2606.31209v1)

### [AC3S: Adaptive Conditioning for 3D-Aware Synthetic Data Generation](http://arxiv.org/abs/2606.31204v1)

- **arXiv ID**: `2606.31204v1`
- **作者 / Authors**: Eric Ji, Qiran Hu, Wufei Ma, Sarthak Jain, Yingying Li et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Synthetic data generation has emerged as a powerful tool for improving data scalability in computer vision. Recent diffusion-based pipelines have demonstrated strong photorealism. However, how to enforce precise 3D structure and pose consistency in generated images remains challenging. Existing methods leverage visual prompts such as edge maps to guide diffusion models, but often suffer from over-conditioning artifacts that degrade image realism and limit dataset quality. In this paper, we present a diffusion-based image generation framework that enforces 3D structural alignment while preserving photorealism through adaptive conditioning. Our framework, Adaptive Conditioning for 3D-Aware Synthetic Data Generation (AC3S), introduces a self-supervised visual prompt modulator that dynamically adjusts the strength of ControlNet conditioning, preventing over-conditioning and enabling the diffusion model to retain its generative expressiveness. To further enhance diversity and semantic consistency, we develop a multi-agent vision language model framework that composes detailed and 3D-aware prompts aligned with the underlying geometric structure. Together, these components enable the scalable generation of high-quality synthetic datasets with accurate 2D and 3D annotations. Extensive experiments demonstrate that our method significantly improves image quality and downstream utility.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31204v1) | [PDF](https://arxiv.org/pdf/2606.31204v1)

### [AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents](http://arxiv.org/abs/2606.30970v1)

- **arXiv ID**: `2606.30970v1`
- **作者 / Authors**: Anuj Kaul, Qianlong Lan, Pranay Gupta
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Autonomous AI agents increasingly perform consequential actions on behalf of human principals, including financial transactions, external communications, and enterprise workflows. Existing agent infrastructure relies on identity federation and delegated authorization to authenticate workloads and control resource access, but it cannot determine whether an authorized action should be executed under the current behavioral and operational context.   We present AgentBound, a runtime governance framework that provides verifiable behavioral oversight for autonomous AI agents. AgentBound evaluates each proposed action using three independent authorities: delegated authorization, owner-signed behavioral constitutions, and site action contracts. Their judgments are conservatively composed through a formal decision model to determine whether an action should be permitted, reviewed, or denied before execution.   To provide accountability, AgentBound generates cryptographically verifiable governance receipts that bind every action to the exact delegation, policy, and semantic artifacts governing the decision, enabling independent replay verification and policy provenance. The framework also introduces standing delegation for long-running agents, allowing periodic workloads to operate under continuously refreshed governance policies while preserving revocability and bounded authority.   We present the formal foundation, system architecture, governance receipt protocol, and AgentBound-Bench, a benchmark framework for evaluating governance correctness, authority composition, and accountability. Rather than replacing model alignment, AgentBound complements it by providing a deterministic governance layer between authorization and execution, transforming governance from a process that must be trusted into one that can be independently verified.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30970v1) | [PDF](https://arxiv.org/pdf/2606.30970v1)

### [Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent](http://arxiv.org/abs/2606.30616v1)

- **arXiv ID**: `2606.30616v1`
- **作者 / Authors**: Lei Bai, Zongsheng Cao, Yang Chen, Zhiyao Cui, Shangheng Du et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

We introduce Agents-A1, a 35B Mixture-of-Experts Agentic Model that reaches trillion-parameter-level performance by scaling the agent horizon. We investigate agent-horizon scaling from two perspectives: scaling long-horizon trajectories and scaling heterogeneous agent abilities. To support this goal, we build a long-horizon knowledge-action infrastructure that connects external knowledge, actions, observations, and verifier outcomes, producing agentic trajectories with an average length of 45K tokens. Based on this, we train Agents-A1 with a three-stage recipe. First, we perform full-domain supervised fine-tuning to align the base model with broad agentic behaviors. Second, we train domain-level teacher models to capture specialized expertise in each domain. Third, we propose a multi-teacher domain-routed on-policy distillation with salient vocabulary alignment to improve knowledge transfer efficiency across different domains, unifying six heterogeneous domains into one deployable student model. Agents-A1 achieves strong and broad performance for long-horizon agent benchmarks. Compared with 1T-parameter model such as Kimi-K2.6 and DeepSeek-V4-pro, Agents-A1 achieves leading results on SEAL-0 (56.4), IFBench (80.6), HiPhO (46.4), FrontierScience-Olympiad (79.0), and MolBench-Bind (56.8), and remains highly competitive on SciCode (44.3), HLE (47.6) and BrowseComp (75.5). We hope this work provides the community with a practical path for scaling the horizon using a 35B agent that can reach or match the performance of 1T models on long-horizon tasks.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30616v1) | [PDF](https://arxiv.org/pdf/2606.30616v1)

### [Fund2Persona: A Framework for Building and Refining Financial Advisor Personas from Fund Disclosure Data](http://arxiv.org/abs/2606.29793v2)

- **arXiv ID**: `2606.29793v2`
- **作者 / Authors**: Suhwan Park, Hoyoung Lee, Zhangyang Wang, Alejandro Lopez-Lira, Young Cha et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Demand for personalized financial advising is growing, but consistent advisor expertise is difficult to obtain, scale, and encode in LLM systems. Simple persona prompts rarely specify how a financial advisor should reason and often drift toward generic recommendations. We propose Fund2Persona, a framework that grounds financial-advisor personas in fund disclosures, holdings transitions, market context, and manager commentary, then refines them through an agentic actor--scorer--patcher loop. We evaluate the resulting personas on held-out holdings-transition reconstruction and manager-commentary alignment, where they better recover portfolio decisions and grounded manager interpretation than generic baselines. We further study two downstream diagnostics: market-scenario generation, where persona retrieval broadens plausible investment views beyond repeated generic rollouts, and advisory dialogues grounded in investor profiles, where matched personas give more specific and useful advice than a generic advisor. These results suggest that fund-data-grounded financial-advisor personas can make manager-specific investment expertise portable rather than merely changing an LLM's surface style.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29793v2) | [PDF](https://arxiv.org/pdf/2606.29793v2)

### [Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing](http://arxiv.org/abs/2606.29541v1)

- **arXiv ID**: `2606.29541v1`
- **作者 / Authors**: Yoosung Hong
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Role-semantic assignments provide priors over how heterogeneous agents may coordinate, but cooperative MARL systems instead settle on conventions through decentralized, non-stationary learning, with no guarantee that the resulting structure matches those priors. We study this translation gap between theory-informed role expectations and learned coordination structure through a diagnostic combining a role-routing matrix, formation sensitivity ($Δ_{\max}$), and gradient/occlusion attribution across three-role MiniGrid and SMACv2 (Terran) environments.   We show that label-conditioned attention produces substantially more concentrated and role-specific routing than flat MLP baselines, remains stable under 3v3--9v9 scaling, transfers zero-shot across team sizes, and is invariant to ally-slot padding. A 5-seed re-evaluation shows partial alignment between learned conventions and designer-specified priors while revealing where small-n noise can manufacture apparent strategic divergence. We present these results as an empirical framework for measuring coordination structure in cooperative MARL rather than as a new equilibrium concept or causal explanation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29541v1) | [PDF](https://arxiv.org/pdf/2606.29541v1)

### [Deterministic Decisions for High-Stakes AI. A Zero-Egress Pipeline with the Deployability of RAG and the Accuracy of Machine Learning](http://arxiv.org/abs/2606.29280v1)

- **arXiv ID**: `2606.29280v1`
- **作者 / Authors**: Craig Atkinson
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

We identify intervention bias as a previously unquantified failure mode of zero-shot large-language-model (LLM) educational advisory agents: without task-specific training, they recommend action when a hindsight-optimal oracle policy mandates inaction. In a six-arm ablation on the Open University Learning Analytics Dataset (N=800 students, four temporal cutoffs), at day 56 -- when the oracle designates 70.1% of students as needing no intervention -- zero-shot GPT-4o recommends action for 73%, a 43 percentage-point false-positive rate. Commercial RAG and SQL-augmented retrieval are comparably miscalibrated; at 10,000 students this implies about 4,300 unnecessary advisor contacts per cycle.   Supervised policy learning eliminates this bias: a trajectory-conditioned ONNX Decision Transformer (DT) and a snapshot XGBoost classifier, trained on the same oracle-labelled trajectories under strict prefix-only features, both achieve near-zero calibration error. The DT reaches macro-F1 0.79 (macro-recall 0.85) across all five action classes, predicting even the rare load-reduction action without collapsing, at a 0% action flip rate and sub-5 ms CPU decision latency. The two supervised arms are on par; the DT's edge over XGBoost at the final cutoff is indicative only (unpaired across cohorts).   Scope: we validate Stage-2 decision-making (EAV state vector to supervised policy) under controlled oracle input from structured OULAD data; high fidelity reflects feature-oracle alignment, not general high-stakes-AI capability. The most robust finding is the intervention-bias contrast, not the absolute accuracies. We also show an Evaluation Gap: LLM-as-judge scoring (DeepEval G-Eval) is blind to intervention bias, rewarding fluent over-prescription rather than decision quality.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29280v1) | [PDF](https://arxiv.org/pdf/2606.29280v1)

### [MIThinker: A Plug-and-Play Policy-Optimized Thinker For Motivational Interviewing Counseling](http://arxiv.org/abs/2606.29265v1)

- **arXiv ID**: `2606.29265v1`
- **作者 / Authors**: Yizhe Yang, Palakorn Achananuparp, Heyan Huang, Jing Jiang, Ee-Peng Lim
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Reasoning large language models (LLMs) have recently made much progress in complex problem-solving, leveraging internal reasoning (or thought) to guide their solution generation. However, existing LLM-based counseling agents, including those using Motivational Interviewing (MI), generate responses without explicitly aligning thoughts with counseling techniques, limiting their effectiveness. We propose MIThinker, a lightweight thinking model that generates therapeutic thoughts to guide MI counseling agents in strategy selection and response generation. To overcome the lack of annotated thought data, we introduce AugR1-MI, an automated pipeline that reverse-engineers counselor's thoughts from observed responses. Through two-stage training combining supervised fine-tuning and reinforcement learning, MIThinker demonstrates improved theory-of-mind assessment and strategy alignment. Comprehensive evaluations show that MindfulMI, our agent leveraging MIThinker, achieves MI competency comparable to state-of-the-art systems with an order of magnitude less computation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29265v1) | [PDF](https://arxiv.org/pdf/2606.29265v1)

### [Customized Generative AI Agent for Transportation Engineering Practice: A Development and Continued Pre-training Guideline](http://arxiv.org/abs/2606.29014v1)

- **arXiv ID**: `2606.29014v1`
- **作者 / Authors**: Dianwei Chen, Yuan-Zheng Lei, Zifan Zhang, Yuchen Liu,  Xianfeng et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Recent advancements in generative artificial intelligence (AI) and large language models (LLMs) have shown significant promise in automating complex reasoning, summarization, and question-answering tasks. However, the effectiveness of general-purpose LLMs in specialized engineering domains remains limited due to insufficient exposure to technical standards, engineering terminology, and domain-specific semantics. This study proposes a systematic approach to developing a customized generative AI agent for transportation engineering applications. A curated corpus of U.S. transportation manuals, design guidelines, and regulatory documents is used to conduct continued pretraining of six state-of-the-art LLMs through a unified low-rank adaptation (LoRA) framework. The training process is monitored to ensure convergence and model stability. Performance is evaluated using standard natural language processing metrics, including BLEU-4 and ROUGE, with Qwen2.5-7B and LLaMA-3.1-8B demonstrating the highest domain alignment and response quality. Results validate the effectiveness of LoRA-based adaptation in improving LLM performance on technical content interpretation and context-specific reasoning. This work contributes a reproducible development framework for constructing domain-specialized generative AI agents, supporting broader deployment in transportation research, design, planning, and policy analysis.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29014v1) | [PDF](https://arxiv.org/pdf/2606.29014v1)

### [A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models](http://arxiv.org/abs/2606.28757v1)

- **arXiv ID**: `2606.28757v1`
- **作者 / Authors**: Nuo Chen, Lulin Liu, Zihao Li, Ziyao Zeng, Zihao Zhu et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Generative world models hold immense promise as scalable simulators for autonomous systems, particularly for synthesizing rare but safety-critical multi-agent interactions, such as vehicle collisions. However, current evaluation paradigms index heavily on visual fidelity and semantic alignment, leaving a critical blind spot: they cannot reliably quantify whether generated dynamics actually obey the fundamental physical laws required for reliable simulation. Assessing this physical plausibility is inherently difficult due to a lack of physical metrics and the challenge of extracting metric-scale kinematics from uncalibrated video rollouts. To bridge this gap, we introduce CrashTwin, a physics-grounded evaluation framework designed to stress-test the physical trustworthiness of world models. CrashTwin couples a diverse dataset of multi-agent collision scenarios, comprising 25K controllable synthetic and 12K in-the-wild real-world collision sequences with a novel calibration-free reconstruction pipeline, enabling the recovery of 3D physical attributes directly from world model rollouts. We propose a diagnostic suite that systematically evaluates three dimensions: spatio-temporal consistency, momentum and kinetic energy conservation, and world-dynamics integrity. Extensive benchmarking of state-of-the-art models reveals a crucial insight: high perceptual quality frequently masks severe physical violations during complex interactions. By quantitatively exposing these failure modes, CrashTwin provides a vital diagnostic tool for developing physically grounded world models capable of reliable real-world simulation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28757v1) | [PDF](https://arxiv.org/pdf/2606.28757v1)

### [The Two Genie Game: Adoption and Welfare in Audit-Grounded AI Governance](http://arxiv.org/abs/2606.28710v1)

- **arXiv ID**: `2606.28710v1`
- **作者 / Authors**: Darrell Lewis-Sandy
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

We ask under what conditions an agent with a harm-minimizing policy can displace an approval-seeking (RLHF) agent in a competitive market, and when that policy is sufficient to prevent community harm. We use evolutionary game theory (finite-population Moran-Fermi pairwise comparison) to formalize this subject to assumptions of wisher hindsight, peer testimony, a monotone harm ledger, sufficient information density of community feedback, and a finite, depleting resource pool, in a negative-sum environment.   We show that adoption is favored when the prior distributions on how readily wishers attune to community sentiment are monotone, exhibit endpoint inversion, and have a centro-symmetric pairing property, and demonstrate this with several long-tailed priors (Hill, Pareto, Lomax, Frechet). Where it is favored, a critical adoption level separates communities that drift back to the approval-seeking agent from those for which the audited agent fixes; above that level fixation is the overwhelmingly likely outcome. We derive when fixation is attainable as a bound on the effective (informational) size N_c of the community, which must be small enough to allow fixation before depletion. We present these as Theorems 5.4 and 5.5; the algebraic and finite-grid backbone is machine-checked in Lean 4, with the barrier-crossing asymptotics retained as explicit hypotheses.   We show that a self-audited agent with a community ledger is not, in general, sufficient to prevent community harm. Sufficiency depends both upon the alignment of the agent's audit with community values and the timeframe over which harm is evaluated. Regardless of alignment, once adoption reaches dominance, the state is absorbing. The same policy that reduced harm under alignment becomes a trap, welfare-negative under misalignment and, even under alignment, one that locks in harm deferred past the adoption horizon.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28710v1) | [PDF](https://arxiv.org/pdf/2606.28710v1)

### [Towards Value-Constrained Credit Assignment in Fully Delegated AI Cooperatives](http://arxiv.org/abs/2606.28217v1)

- **arXiv ID**: `2606.28217v1`
- **作者 / Authors**: Young Yoon, Jimin Kim, Soyeon Park
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

We propose a framework for reward allocation in fully delegated AI cooperatives where humans are represented by agents that contribute data and participate in model updates under heterogeneous value constraints. The key idea is to credit only those updates that remain admissible after screening them against each principal's value profile. We formulate value-conditioned gradient filtering, online marginal contribution signals, and cumulative revenue settlement within a traversal learning (TL) substrate. TL is especially attractive here because it performs decentralized backpropagation without the quality loss associated with aggregation-centric distributed learning and, we argue, offers a finer attribution substrate than FedAvg-style federated learning by preserving explicit traversal and gradient paths. The framework is positioned against data valuation, federated contribution estimation, personalized federated learning, and pluralistic alignment.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28217v1) | [PDF](https://arxiv.org/pdf/2606.28217v1)

### [HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration](http://arxiv.org/abs/2606.28215v1)

- **arXiv ID**: `2606.28215v1`
- **作者 / Authors**: Jiaxin Li, Yuxiang Wu, Zhenkai Zhang, Xinrui Shi, Haoyuan Wang et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a multi-level human-in-the-loop feedback mechanism, HAT-4D efficiently resolves depth ambiguities and interaction-induced occlusions during 3D generation and 4D propagation, yielding physically plausible assets without relying on expensive multicamera rigs. As a scalable data engine, HAT-4D facilitates the creation of MVOIK-4D, an open-world benchmark for monocular 4D interaction reconstruction, accompanied by a novel multi-dimensional evaluation protocol focused on physical plausibility and temporal consistency. Extensive experiments demonstrate that HAT-4D achieves SOTA performance on most evaluation metrics, while maintaining competitive semantic alignment. Ablation studies show that introducing a small amount of human feedback improves interaction reconstruction. Moreover, the data produced by HAT-4D effectively improves baseline performance when used for fine-tuning. Our data and code are available at https://lijiaxin0111.github.io/HAT4D/

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28215v1) | [PDF](https://arxiv.org/pdf/2606.28215v1)

### [AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration](http://arxiv.org/abs/2606.28049v1)

- **arXiv ID**: `2606.28049v1`
- **作者 / Authors**: Haotian Li, Yida Wang, Leyuan Wang, Jinshan Lai, Keyang Wang et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

In recent years, multimodal large language models (MLLMs) have shown strong potential for embodied intelligence, yet their ability to maintain geometrically consistent spatial understanding across heterogeneous views remains under-evaluated. Existing benchmarks largely focus on single-agent, single-view perception, leaving a gap in the systematic assessment of collaborative air-ground settings, where multi-scale observations are complementary but introduce scale mismatch, asymmetric occlusion, and reference-frame inconsistencies. We present AirGroundBench, a diagnostic benchmark for evaluating multi-view spatial intelligence in heterogeneous UAV-UGV collaboration. AirGroundBench is built from 11 high-fidelity simulated environments with 1,021 synchronized air-ground observation pairs, yielding approximately 62,000 dual-view, four-option single-choice visual question answering instances and 115 closed-loop vision-language navigation episodes. It covers 10 task types organized into four progressively demanding capability dimensions: spatial perception, cross-view alignment, spatial transformation and reasoning, and embodied decision-making. To support geometry-grounded evaluation and analysis, we provide structured spatial annotations, including cross-view object identities and metric 2D and 3D bounding boxes. Evaluations of 13 representative MLLMs under UAV-only, UGV-only, and dual-view input settings reveal consistent bottlenecks: models perform relatively well on spatial perception but struggle with cross-view alignment and transformation-intensive reasoning, and these deficits propagate to sequential decision-making in vision-language navigation. Although dual-view inputs provide measurable gains over single-view variants, a persistent gap from human performance remains, highlighting geometric consistency as a key limitation of current embodied MLLMs.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28049v1) | [PDF](https://arxiv.org/pdf/2606.28049v1)

### [SimPol: Simulating polarisation in political belief networks in European countries](http://arxiv.org/abs/2606.27968v1)

- **arXiv ID**: `2606.27968v1`
- **作者 / Authors**: Isabela Burattini Freire, Hongryol Cha, Irina Epure, Sara Filippini, Karan K. H. Manjunatha et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: physics.soc-ph

<details>
<summary>📝 Abstract</summary>

Here we combine empirical network analysis with agent-based modelling to understand how different ways of structuring belief systems may affect the polarisation drive, and how the diversity of belief systems in Europe may result in different polarisation trajectories. Using the 2016 European Social Survey, we infer belief networks across 23 European countries via a Bayesian algorithm, revealing that belief systems are predominantly organised around immigration, LGBT rights, and economic interventionism, reflecting the influence of populist discourse across the continent. We further verify a Western-Eastern divide across the national belief networks: in Western European countries, left-right self-identification is a more reliable predictor of broader belief alignment, whereas in Eastern Europe this relationship breaks down. By applying these empirical belief networks into a sociologically grounded agent-based model, we further show that polarisation is amplified by high individual belief rigidity and low susceptibility to social influence, and that cross-country differences in polarisation levels mirror the same geographic divide observed in belief network topology. These findings establish belief networks topologies as a structural driver of political polarisation, with implications for understanding and anticipating polarisation dynamics across diverse European contexts. We find that populations are not polarised when little attention is placed on maintaining internal coherence and polarisation levels are moderate when high attention is placed in both keeping internal coherence and agreement in beliefs with others.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27968v1) | [PDF](https://arxiv.org/pdf/2606.27968v1)

## 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks*

### [Registry-Governed Agent Lifecycle:Completing EDDOps with Evaluation-DrivenRegistration, Promotion, and Retirement on AWS AgentCore](http://arxiv.org/abs/2607.00345v1)

- **arXiv ID**: `2607.00345v1`
- **作者 / Authors**: Richard Kang, Vincent Wang
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Enterprise adoption of LLM agents requires model selection methods that balance quality, reliability, safety, latency, and cost. Evaluation-Driven Development and Operations (EDDOps) positions evaluation as a continuous governing function across the agent lifecycle rather than a terminal checkpoint. This paper presents a practitioner-oriented instantiation of EDDOps on AWS Bedrock AgentCore and proposes a cost-to-performance framework for selecting foundation models in enterprise agent architectures. We make three contributions: a conceptual synthesis explaining why traditional TDD/BDD methods are insufficient for non-deterministic LLM agents; an architectural mapping of the EDDOps reference architecture onto AgentCore Runtime, Evaluations, Agent Registry, and CloudWatch observability; and an empirical cost-to-performance decision framework validated through a proof-of-concept comparing three foundation models across two deployment paths. Using trace data from 30 single-turn invocations across six agents, 9 multi-turn evaluations, and registry-integrated governance, we show how evaluation evidence can convert model selection from a benchmark-ranking exercise into a governed economic decision. The results suggest that managed agent platforms can support EDDOps when they provide trace-native observability, pluggable evaluator frameworks, and governed registry-based discovery.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00345v1) | [PDF](https://arxiv.org/pdf/2607.00345v1)

### [Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems](http://arxiv.org/abs/2606.31339v1)

- **arXiv ID**: `2606.31339v1`
- **作者 / Authors**: Guoqin Tang, Qingxuan Jia, Yichen Tan, Zeyuan Huang, Ning Ji et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Agentic artificial intelligence is increasingly used to decompose industrial tasks, propose robot actions, and adapt execution plans in dynamic cyber-physical environments. However, autonomous proposal generation alone does not guarantee that multi-robot industrial systems preserve task dependencies, resource ownership, safety holds, or repair boundaries during long-horizon execution. This paper introduces a verification-gated agentic mission-state governance framework for intelligent industrial multi-robot systems. The framework maintains two synchronized state objects: an evolving task forest for persistent hierarchy, delayed grounding, and repairable substructures; and a governed blackboard for online execution state, robot traces, resource locks, world beliefs, proposals, verification records, and scene-temporary constraints. From each forest--blackboard snapshot, a derived execution coupling topology exposes cross-branch dependencies for proposal verification, parallel-commit eligibility, and bounded repair. Candidate assignments, repairs, deferrals, and constraint updates may be generated by heuristic, optimization, or agentic reasoning modules, but they can update the committed mission state only after deterministic verification and atomic commit. We evaluate the framework in an indoor factory multi-robot scenario, 30-seed remote-construction stress benchmarks, structural ablations, and scalability probes. The results show improved verified and safety-audited mission-state progress with fewer invalid commitments, lock conflicts, duplicate assignments, abandoned nodes, and disruptive repairs under modeled mission predicates. The study positions agentic AI as a proposal-generating layer governed by inspectable mission-state verification rather than as an unchecked execution authority.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31339v1) | [PDF](https://arxiv.org/pdf/2606.31339v1)

### [LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents](http://arxiv.org/abs/2606.31045v1)

- **arXiv ID**: `2606.31045v1`
- **作者 / Authors**: Jingpu Yang, Fengxian Ji, Zhengzhao Lai, Zhexuan Cui, Guangxian Ouyang et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Scientific embodied agents are increasingly capable of carrying out laboratory procedures, but executing these procedures safely in dynamic laboratory environments remains challenging. Current safety approaches often overlook the intermediate step of transforming laboratory natural language, including safety rules, manuals, protocols, and standard operating procedures, into machine-checkable runtime constraints. We introduce LabGuard (Laboratory Guard), a language-to-execution safety suite that grounds natural-language laboratory rules into executable specifications and deploys them as runtime guards. LabGuard includes three core components: LabGuard-IR, which defines a typed executable representation; LabGuard-Bench, which provides 812 supervised annotations expanded from 203 seed laboratory rules; and LabGuard-Grounder, which maps natural-language laboratory rules into LabGuard-IR. The resulting IR instances are handled by the LabGuard Pipeline, which compiles them into runtime monitors and applies them at the controller boundary. Experiments show that LabGuard generalizes to unseen laboratory-rule sources, achieves 79.4 task-scope F1, and reduces unsafe events from 39.5% to 23.8% after monitor compilation. In LabUtopia, its runtime monitors integrate with ACT, keeping interventions below 0.5% while preserving task success.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31045v1) | [PDF](https://arxiv.org/pdf/2606.31045v1)

### [Formal Security Analysis of Agent Protocol Composition](http://arxiv.org/abs/2606.28690v1)

- **arXiv ID**: `2606.28690v1`
- **作者 / Authors**: Shenghan Zheng, Qifan Zhang, Zheng Zhang, Haonan Li, Christophe Hauser
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

AI agent protocols define how agents use tools, delegate work, and coordinate across software systems, but their security requirements remain incomplete and inconsistently enforced across deployments. We present AgentThread, a source-linked framework for security assurance analysis of agent protocols, from specification text to running SDKs. AgentThread contributes a layered security scope, protocol-derived checks formalized as TLA+ invariants, and a two-phase checker that compiles protocol specifications into model-checkable models and replays executable counterexamples against real SDKs through protocol adapters. For each finding, AgentThread records the source text behind the check and separates violated protocol requirements from missing recommendations, hardening gaps, and unassigned cross-protocol responsibilities.   Across five emerging agent protocols, AgentThread identifies 35 specification-level findings, supports them with 80 implementation tests against production SDKs and reference servers, and finds 30 additional failures that emerge only under protocol composition. We further show that only one protocol enforces a security-relevant control in practice and no protocol assigns enforcement for cross-protocol behavior. Insecurity in agent protocols is therefore not only a specification or implementation problem, but also a responsibility gap across protocols, SDKs, and deployments.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28690v1) | [PDF](https://arxiv.org/pdf/2606.28690v1)

## 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation*

### [Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents](http://arxiv.org/abs/2606.30383v1)

- **arXiv ID**: `2606.30383v1`
- **作者 / Authors**: Bojie Li, Noah Shi
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

A rapidly growing class of LLM agents is multi-party: the agent acts for a principal (who briefs it, sends follow-ups, and receives results) while also conversing in a separate channel with a counterparty whose interests may diverge (negotiating with a vendor, screening inbound requests, or mediating between employees). Here "help whoever you are talking to" is the wrong objective. The agent must stay loyal to the principal it represents without over-refusing the principal's own cooperative asks. We study this multi-party loyalty problem and contribute a measurement instrument, two mechanisms, and a structural lesson. PrincipalBench is a 75-item multi-turn benchmark with leak probes, dual judges, and an integrity-audit gate. Across 13 frontier subjects it exposes a sharp split (<=20% vs. 53.6-75.3% harm) invisible to single-turn safety evaluations: a selective cluster that declines adversarial probes while still following the principal's legitimate requests, and an over-refusing cluster that refuses broadly. (M1) A prompt-time loyalty scaffold (a fixed system prompt of seven prioritized rules, open-coded from 50+ failure trajectories) holds Claude-Sonnet to 19.4% harm and all nine selective subjects to <=20%. (M2) A per-token-KL distillation recipe transfers a prompted Qwen3-32B teacher into 8B Qwen3 and Llama-3.1 students, the strongest open-weight recipe we measure. (Lesson) Both mechanisms only move along a common leak/over-refusal trade-off rather than crossing it: improving one axis costs the other, and the jointly favorable outcome stays out of reach.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30383v1) | [PDF](https://arxiv.org/pdf/2606.30383v1)

## 📂 survey
*综述与系统化 / Surveys & Systematization*

### [AI Native Games: A Survey and Roadmap](http://arxiv.org/abs/2607.00527v1)

- **arXiv ID**: `2607.00527v1`
- **作者 / Authors**: Zhiyue Xu, Fandi Meng, Kaijie Xu, Clark Verbrugge, Simon Lucas et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Generative AI now enables games to produce dialogue, quests, characters, images, and worlds at runtime. Yet generation alone does not make a game AI-native, nor does it guarantee playability. This paper defines AI-native games by whether runtime generative AI is constitutive of the core loop: if the AI component were removed or trivially replaced, the central form of play would collapse or become fundamentally different. This counterfactual criterion separates AI-native games from AI-augmented games, boundary artifacts, chatbots, tavern-style role-play, procedural content generation, and AI-assisted production. Using this definition, we screen candidate artifacts and analyze 53 publicly available AI-native games and prototypes. We introduce a dual-axis G/N taxonomy: the G-axis captures player-facing game type, while the N-axis captures the dominant AI mechanic that makes generative AI indispensable to play. The corpus is concentrated around language-forward designs, especially narrative adventure, epistemic interaction, and generative narrative, while categories such as semantic adjudication, multi-agent simulation, generative construction, and relationship/companion play remain less represented. We argue that the central design problem is organizing semantic openness into stable gameplay. AI-native design depends on mechanical invariants: goals, rules, state, feedback, pacing, and player agency that make open-ended AI outputs interpretable and consequential. We conclude with a roadmap for controllable generation, AI-as-mechanic design, multimodal and multi-agent systems, inference economics, evaluation, safety, and regulation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00527v1) | [PDF](https://arxiv.org/pdf/2607.00527v1)

### [Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents](http://arxiv.org/abs/2606.30306v1)

- **arXiv ID**: `2606.30306v1`
- **作者 / Authors**: Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.MA

<details>
<summary>📝 Abstract</summary>

Always-on agents are systems whose future behavior depends on durable state accumulated across earlier interactions. We treat them as persistent-state systems: the operative system includes retrievable memories, but also task ledgers, permissions, credentials, commitments, provenance and audit records, shared state, trigger conditions, and externally committed effects linked to those records. The survey reads the literature through six diagnostic axes for each state item, authority, scope, mutability, provenance, recoverability, and actionability, and through a lifecycle in which state is written, validated, organized, retrieved, acted upon, updated, forgotten, audited, and sometimes rolled back. Across a 435-work coded corpus, treated as a scoped map rather than an exhaustive census, the literature concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it. We therefore introduce the Always-On Evaluation Protocol (AOEP-v0), a pilot evaluation contract that makes these governance requirements concrete by scoring state mutation and recovery obligations rather than answer quality alone. The resulting agenda connects always-on agents to databases, distributed systems, formal methods, capability security, and machine unlearning.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30306v1) | [PDF](https://arxiv.org/pdf/2606.30306v1)

### [When Stopping Fails: Rethinking Minimal Risk Conditions through Human-Interactive Autonomous Driving for Safe Transportation Systems](http://arxiv.org/abs/2606.29115v1)

- **arXiv ID**: `2606.29115v1`
- **作者 / Authors**: Yash Tandon, Giovanni Tapia Lopez, Marcus Blennemann, Mohan Trivedi, Ross Greer
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Autonomous vehicles (AVs) are increasingly deployed in urban environments, yet their safety frameworks remain primarily designed around collision avoidance and minimal risk condition (MRC) behaviors such as slowing or stopping when uncertainty arises. Although effective in reducing immediate crash risk, real-world deployments indicate that stopping alone does not guarantee safe integration into human-governed roadway systems. Incidents reported by municipalities and public records show that AV fallback behaviors can obstruct traffic, interfere with emergency response operations, and create accessibility challenges for passengers and pedestrians. This paper presents an analysis of publicly documented incidents involving AV stopping behavior and human-AV interaction failures. We categorize these incidents according to limitations in perception, planning, and control within current AV architectures. Using this taxonomy, we identify key gaps in existing safety paradigms, particularly the lack of mechanisms for interpreting human authority, responding to multimodal instructions, and adapting to dynamic, socially regulated traffic conditions. We then review emerging research directions that support human-interactive perception, language-grounded and accessibility-aware planning, and assisted control through remote guidance and teleoperation. The analysis highlights the need to augment current AV safety frameworks with capabilities that enable cooperative interaction with human agents and infrastructure. These findings suggest that reliable urban deployment of AVs requires moving beyond passive fallback strategies toward human-interactive autonomy.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29115v1) | [PDF](https://arxiv.org/pdf/2606.29115v1)

## 📂 other
*其他安全相关 / Other Security-Related*

### [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](http://arxiv.org/abs/2607.01071v1)

- **arXiv ID**: `2607.01071v1`
- **作者 / Authors**: Zhishang Xiang, Zerui Chen, Yunbo Tang, Zhimin Wei, Ruqin Ning et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.IR

<details>
<summary>📝 Abstract</summary>

Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlooking how retrieved memories influence downstream reasoning and decision-making. To bridge this gap, we propose MemSyco-Bench, a comprehensive benchmark for evaluating memory-induced sycophancy in agent systems. MemSyco-Bench measures when memory should influence a decision and how valid memory should be used. Specifically, it covers five tasks that assess whether agents can reject memory as factual evidence, respect its applicable scope, resolve conflicts between memory and objective evidence, track memory updates, and use valid memory for personalization. All related resources are collected for the community at https://github.com/XMUDeepLIT/MemSyco-Bench.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.01071v1) | [PDF](https://arxiv.org/pdf/2607.01071v1)

### [Human-Machine Collaboration on Generative Meta-Learning: Model and Algorithm](http://arxiv.org/abs/2607.00926v1)

- **arXiv ID**: `2607.00926v1`
- **作者 / Authors**: Midhun Parakkal Unni, Samuel Kaski
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Generalizing machine learning models to environments that differ from their training distribution remains a critical hurdle, particularly when data from the target domain is entirely or partially unavailable. We propose Generative Meta-Learning with Human Feedback (GMHF), a novel framework that bridges this domain gap by leveraging expert intuition to guide data synthesis. Grounded in a theoretical analysis of generalization error, we derive bounds demonstrating that aligning the distribution of generated data with human beliefs regarding the target physics significantly mitigates risk. GMHF operationalizes this insight by employing a Conditional Neural ODE (cNODE) as a generative digital twin, coupled with a Reinforcement Learning (RL) agent. The agent iteratively refines the latent physical parameters of the generated trajectories based on feedback, effectively steering the meta-learner toward the unobserved target distribution. Empirical validation on a nonlinear Duffing oscillator shows that GMHF substantially reduces deployment loss as expert reliability increases, and that the divergence between generated and target data falls under reliable feedback, directly corroborating the divergence-minimisation mechanism predicted by our theory. Further experiments on a non-dynamical probabilistic model confirm that the framework extends beyond ODE-governed systems, establishing human-AI collaboration as a rigorous catalyst for robust generalisation under distribution shift.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00926v1) | [PDF](https://arxiv.org/pdf/2607.00926v1)

### [GMO-E$^2$DIT: Grounded Multi-Operation Editing for E-Commerce Images](http://arxiv.org/abs/2607.00920v1)

- **arXiv ID**: `2607.00920v1`
- **作者 / Authors**: Zipeng Guo, Xiaoan Liu, Lichen Ma, Cheng Wang, Yu He et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Real-world e-commerce image editing often requires multiple, localized, and auditable operations rather than global restyling. This compositional nature poses a dual challenge: models must precisely apply all requested edits to the correct regions while preserving unmodified content, even under ambiguous instructions. Existing one-shot editors conflate intent resolution, spatial grounding, and synthesis into a single step, frequently resulting in partial execution failures, which is unacceptable for commercial scenarios. To address this, we introduce GMO-E$^2$DIT, an agentic editing framework that couples a Vision-Language Model (VLM) with a mask-conditioned image editor to tackle structured multi-turn task completion. Given an underspecified instruction, the VLM agent constructs a region-grounded edit agenda, effectively decoupling cognitive reasoning from generative rendering. The framework then executes sub-programs via operation-aware masks and references, utilizing a reflection-driven loop to inspect intermediate results and determine the subsequent state. This iterative mechanism reliably preserves safe partial progress, retries unfinished operations, and recovers from errors. Furthermore, we develop a unified data pipeline providing aligned supervision for planning, execution, and reflection, alongside EComEditBench, a comprehensive benchmark for instruction-driven evaluation. Extensive experiments demonstrate that GMO-E$^2$DIT achieves competitive performance compared to strong closed-source models, yielding superior instruction accuracy and edit fidelity over existing baselines.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00920v1) | [PDF](https://arxiv.org/pdf/2607.00920v1)

### [Beyond Line of Sight: Hybrid Validation of V2X Collective Perception in Complex Scenarios](http://arxiv.org/abs/2607.00874v1)

- **arXiv ID**: `2607.00874v1`
- **作者 / Authors**: Markos Antonopoulos, Anastasia Bolovinou, Bill Roungas, Elena Daskalaki, Angelos Amditis
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

This paper introduces a probabilistic framework and hybrid validation methodology for V2X-enabled Collective Perception (CP) in complex traffic scenarios. The proposed Bayesian fusion algorithm extends the perceptual horizon of connected and autonomous vehicles by integrating heterogeneous sensor observations from multiple agents into a shared probabilistic occupancy grid. Each cell of this grid encapsulates both occupancy likelihood and uncertainty, enabling explainable and trustworthy situational awareness beyond the ego vehicle's field of view. To bridge the gap between simulation and real-world evaluation, a hybrid testing framework is developed, combining CARLA-based virtual environments with vehicle-in-the-loop experimentation. Experimental results in a roundabout scenario demonstrate a 260 percent increase in field-of-view coverage and a rise in occupied-cell recall from 0.82 (ego-only) to 0.94 (six-agent CP) under nominal localization conditions. Overall, the proposed approach provides a reproducible and interpretable foundation for validating CP systems, supporting the safe and certifiable deployment of cooperative autonomous vehicles.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00874v1) | [PDF](https://arxiv.org/pdf/2607.00874v1)

### [MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization](http://arxiv.org/abs/2607.00846v1)

- **arXiv ID**: `2607.00846v1`
- **作者 / Authors**: Jinliang Xu, Liping Ma
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.NE

<details>
<summary>📝 Abstract</summary>

This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic continuous benchmark matrix covering shifted sphere, shifted Ackley, and shifted Rastrigin landscapes at $10D$, $20D$, and $30D$, with two change severities and 12 seeds per scenario. The comparison layer includes a generic MMAO variant without dynamic derivation, dynamic random search, dynamic PSO-lite, dynamic DE-lite, and three endogenous ablations. Across the full 216-run matrix, MMAO-Dyn attains mean offline error $28.07$, improving over Generic-MMAO ($29.36$), Dynamic-PSO-lite ($34.65$), Dynamic-DE-lite ($67.09$), and Dynamic-RandomSearch ($111.37$). The gains are clearest in aggregate robustness on sphere and Rastrigin families and in 10-step post-change recovery relative to the generic backbone, whereas the seed-aligned comparison with Dynamic-PSO-lite remains unfavorable in win-loss count and the \texttt{NoMemoryRefresh} ablation stays very close to the full method. We therefore position MMAO-Dyn as a credible family-expansion result for MMAO: the metabolic loop can generate meaningful dynamic behavior, but the strongest current value lies in recovery-oriented resource redistribution rather than in universal dominance or in a fully optimized submechanism design.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00846v1) | [PDF](https://arxiv.org/pdf/2607.00846v1)

### [Exploring the Semantic Gap in Agentic Data Systems: A Formative Study of Operationalization Failures in Analytical Workflows](http://arxiv.org/abs/2607.00828v1)

- **arXiv ID**: `2607.00828v1`
- **作者 / Authors**: Jalal Mahmud, Eser Kandogan
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.DB

<details>
<summary>📝 Abstract</summary>

Large language models (LLMs) are increasingly used to generate queries, invoke tools, and construct analytical workflows. Although recent advances have substantially improved workflow generation and execution, the semantic information required to operationalize analytical concepts often lies beyond what is explicitly represented in database schemas and data values. We present a cross-domain formative study of operationalization failures in agent-generated analytical workflows. Across 236 analytical intents spanning finance, human resources, and public safety domains, we identify 153 recurring failures despite successful workflow generation and execution. Our analysis reveals five recurring classes of failures: comparative grounding, process reasoning, quantitative reasoning, role confusion, and policy grounding. These findings suggest a semantic gap between user-level analytical concepts and the information available to workflow-generation systems. More broadly, they raise questions about the admissibility of analytical operations and suggest that future agentic data systems may require richer semantic representations to bridge the gap between analytical intent and executable computation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00828v1) | [PDF](https://arxiv.org/pdf/2607.00828v1)

### [Multi-Turn Agentic Scientific Literature Search via Workflow Induction](http://arxiv.org/abs/2607.00597v1)

- **arXiv ID**: `2607.00597v1`
- **作者 / Authors**: Jisen Li, Bingxuan Li, Nanyi Jiang, Xuying Ning, Xiyao Wang et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Scientific literature search often requires more than retrieving papers from a single query: users' intents are underspecified, preference-dependent, and evolve through interaction. Existing search agents typically rely on fixed pipelines or implicit language-only reasoning, making their search strategies difficult to control, inspect, and refine. We introduce PaperPilot, a multi-turn literature search agent that frames scientific search as workflow induction. Given an anchor paper and a user query, PaperPilot constructs an executable DAG of paper-search operators, including keyword search, citation expansion, filtering, scoring, reranking, and evidence extraction. User feedback is then used to refine both the query and the workflow itself. We train PaperPilot with supervised workflow imitation and preference optimization over controlled workflow corruptions. Experiments show that PaperPilot-9B improves over the base Qwen3.5-9B toolset agent under multi-turn interaction, increasing Hit@5 from 58.0 to 77.0, MRR from 47.5 to 59.4, and nDCG@10 from 26.8 to 32.5, while reducing workflow execution errors from 9.5% to 0%. These results show that explicit, editable search workflows provide an effective and controllable interface for aligning literature search agents with complex scientific intent.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00597v1) | [PDF](https://arxiv.org/pdf/2607.00597v1)

### [Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs](http://arxiv.org/abs/2607.00555v1)

- **arXiv ID**: `2607.00555v1`
- **作者 / Authors**: Shaoyu Yang, Haifeng Lin, Chunrong Fang, Xiang Chen, Wei Cheng et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state.   We present Phoenix, the first LLM-based static analysis technique for DL frameworks. Our key insight is that cross-language tensor flows in DL frameworks can be modeled, together with concrete code context, as a structured semantic bridge intermediate representation (SBIR) that LLMs can analyze for potential bugs in tensor semantic propagation. We implement this insight through a multi-agent workflow. A summarization agent first distills bug summaries from historical bug-fix patches and CWE rules. Guided by each summary, an extraction agent identifies bug-relevant repository symbols for code retrieval, and a generation agent synthesizes grounded SBIRs from the retrieved context. Finally, an analysis agent is leveraged to check SBIRs and report potential bugs. Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding. To date, Phoenix has found 31 real new bugs in PyTorch for different heterogeneous hardware backends (Intel CPU, NVIDIA CUDA, and Apple MPS). Among them, 20 submitted bug-fixing patches have been merged into upstream.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00555v1) | [PDF](https://arxiv.org/pdf/2607.00555v1)

### [ECoSim: Data Efficient Fine-Tuning for Controllable Traffic Simulation](http://arxiv.org/abs/2607.00545v1)

- **arXiv ID**: `2607.00545v1`
- **作者 / Authors**: Yu-Hsiang Chen, Wei-Jer Chang, Yi-Ting Chen, Masayoshi Tomizuka
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Controllable traffic simulation is critical for testing autonomous driving systems, yet existing approaches often require retraining large generative models with extensive annotated data. We introduce a lightweight control adaptation framework that enables multi-modal controllability (sketch, latent behavior codes, and text) for pretrained state-of-the-art diffusion and autoregressive traffic models. By modulating intermediate features through identity-initialized FiLM layers, our method efficiently adds new control modalities while preserving the base model's generative prior. Evaluated on Waymo Open Sim Agents Challenge, our approach demonstrates strong controllability with less than 1% of the paired control data. Through context-aware condition transfer, our framework enables counterfactual scenario generation and long-tail synthesis while maintaining stable closed-loop driving realism and safety. Our framework unlocks new possibilities for controllable traffic simulation, enabling targeted scenario generation through lightweight adaptation of pretrained generative models. Project page: https://ecosim-web.github.io/

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00545v1) | [PDF](https://arxiv.org/pdf/2607.00545v1)

### [Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications](http://arxiv.org/abs/2607.00442v1)

- **arXiv ID**: `2607.00442v1`
- **作者 / Authors**: Merve Atasever, Cagan Bakirci, Alfredo Reina Corona, Keyan Azbijari, Jyotirmoy V. Deshmukh
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00442v1) | [PDF](https://arxiv.org/pdf/2607.00442v1)

### [Minos: A Multi-Agent Collaborative Framework for Provenance-Based Backward Tracking](http://arxiv.org/abs/2607.00440v1)

- **arXiv ID**: `2607.00440v1`
- **作者 / Authors**: Jiahui Wang, Zhenyuan Li, Zhengkai Wang, Xiangmin Shen, Fan Zhang
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Sophisticated cyber attacks, particularly Advanced Persistent Threats (APTs), require effective post-intrusion forensic analysis. Provenance-based backward tracking reconstructs attack scenarios by tracing causality from security alerts, but existing methods rely on low-level statistical features and rigid traversal strategies, limiting their ability to capture high-level adversarial intent and suffering from dependency explosion. We present Minos, a multi-agent framework that formulates backward tracking as an LLM-driven reasoning process. Minos adopts a two-tiered architecture: for event-level analysis, it combines hierarchical context management, retrieval-augmented reasoning with citation verification, and adversarial deliberation to improve reasoning quality; for graph exploration, it coordinates four specialized agents under a finite state machine (FSM), replacing exhaustive traversal with hypothesis-guided reasoning and count-first query protocols to efficiently prune the search space. Experiments on 14 attack scenarios across five public datasets show that Minos achieves an average recall of 0.92 and precision of 0.64, significantly outperforming state-of-the-art baselines while producing attack subgraphs that are 49% more compact. Moreover, Minos generates interpretable reasoning throughout the tracking process, facilitating forensic auditing and system refinement. These results demonstrate the effectiveness of LLM-driven reasoning for automated provenance-based backward tracking.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00440v1) | [PDF](https://arxiv.org/pdf/2607.00440v1)

### [Evolving Intelligent Complex Systems via Intellicise Networks: Architecture, Technologies, and Pathways](http://arxiv.org/abs/2607.00316v1)

- **arXiv ID**: `2607.00316v1`
- **作者 / Authors**: Ping Zhang, Rui Meng, Xiaodong Xu, Song Gao, Zixuan Huang et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: eess.SP

<details>
<summary>📝 Abstract</summary>

Future engineering infrastructures are evolving into large-scale, open, heterogeneous, and wirelessly interconnected complex systems. These systems present significant challenges in optimizing network resource utilization, managing high-dimensional information spaces, and accommodating diverse business requirements. Intellicise networks, characterized by Intent-driven operation, semantic-native capability, and distributed intelligence, offer a promising paradigm for enabling such intelligent complex systems. We provide a systematic exploration of future intelligent complex systems from the perspective of intellicise networks. Specifically, we propose a cross-domain intelligent communication network architecture based on intellicise networks, grounded in information theory, systems theory, game theory, and cybernetics. The architecture comprises a cross-layer organizational framework, multi-functional planes, and novel information flows. The cross-layer framework defines the vertical evolution from perception and cognition to decision, while the control, user, data, computation, intelligence, and security planes deliver horizontal intellicise capabilities. Moreover, data, knowledge, model, and task flows interconnect the various layers and planes, forming a closed-loop process that derives simplicity from high-level intelligene while concurrently pursuing enhanced. Building on this architecture, we review key enabling technologies, tracing their evolution from semantic extraction to intent understanding, from heterogeneous resource integration to self-configuration and self-optimization, from generative artificial intelligence (AI) to agentic AI, and from embodied AI to symbodied AI. Additionally, we present a case study on intellicise networks for embodied agent communications and discuss representative applications and services for intelligent complex systems.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00316v1) | [PDF](https://arxiv.org/pdf/2607.00316v1)

### [RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail](http://arxiv.org/abs/2607.00310v1)

- **arXiv ID**: `2607.00310v1`
- **作者 / Authors**: Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar, Anoop M. Namboodiri, Sashi P. Reddi
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocentric video of the same activity are available, which viewpoint of training data produces the strongest adapted model?   We introduce RetailSMV (Retail Synchronized Multi-View), a corpus of 32,105 captioned retail clips from five supermarkets with synchronized ego/exo capture from the store-staff perspective (stocking, arranging, weighing, managing supply carts, scanning at checkout), rather than the customer-centric framing of prior retail video corpora, and train three matched Low-Rank Adaptation (LoRA) configurations of Cosmos3-Nano (egocentric-only, exocentric-only, combined) under identical hyperparameters. On a 200-clip held-out test set evaluated with seven complementary metrics under a strict paired statistical protocol, exocentric-only adaptation matches or exceeds combined adaptation on six of seven point estimates and is significantly better on LPIPS, PSNR, and DreamSim, despite training on only 15,985 exocentric clips (versus 32,105 for combined). A symmetric paired comparison further shows that adding exocentric data to egocentric-only training helps while adding egocentric data to exocentric-only training hurts. The absolute adaptation gap is largest at the shortest rollout time, identifying the near-horizon prediction window as the regime in which adaptation is most beneficial.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00310v1) | [PDF](https://arxiv.org/pdf/2607.00310v1)

### [What's Hidden Matters: Identifying Planning-Critical Occluded Agents using Vision-Language Models](http://arxiv.org/abs/2607.00283v1)

- **arXiv ID**: `2607.00283v1`
- **作者 / Authors**: Amirhosein Chahe, Tyler Naes, Jovin D'sa, Faizan M. Tariq, Sangjae Bae et al.
- **发布日期 / Published**: 2026-07-01
- **分类 / Category**: cs.RO

<details>
<summary>📝 Abstract</summary>

Autonomous vehicles must safely navigate complex environments where planning-critical agents may be hidden from view. Current approaches often treat all occlusions with uniform conservatism, yielding needlessly defensive driving, or they infer hidden spaces without estimating the impact on the planner. This work bridges the critical gap between perception and planning by enabling Vision-Language Models (VLMs) to identify and reason about the specific hidden agents that are most critical to the ego-vehicle's trajectory. We introduce a novel framework that uses Planning KL-divergence (PKL), an information-theoretic metric, to systematically identify and rank occluded agents based on their impact on the ego vehicle's plan. Using this planning-aware ranking, we employ an expert VLM (GPT-5) to generate rich, structured annotations that capture the visual evidence and reasoning required for this task. We apply this framework to the nuScenes dataset to create a new benchmark focused on high-impact scenarios. We conduct comprehensive experiments on a wide range of general-purpose and domain-adapted VLMs, demonstrating that fine-tuning on our PKL-guided data yields dramatic performance improvements across all models. Notably, our results show that smaller, fine-tuned models significantly outperform their much larger zero-shot counterparts, and that our PKL-guided data selection strategy improves performance by approximately 30\% over random sampling. Our work presents the first systematic approach for training VLMs to focus on planning-critical occlusions, enabling more semantically grounded and efficient risk assessment in autonomous driving.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2607.00283v1) | [PDF](https://arxiv.org/pdf/2607.00283v1)

### [QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents](http://arxiv.org/abs/2606.32034v1)

- **arXiv ID**: `2606.32034v1`
- **作者 / Authors**: Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, Joschka Strüber, Ameya Prabhu et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream performance of a training pipeline that integrates them. This is expensive, conflates supervision quality with training engineering confounders, and renders different methodological families requiring distinct training setups incomparable. As a result, dense supervision methods are rarely benchmarked on common ground. We introduce QVal, a training-free testbed for directly evaluating dense supervision signals. Given a state-action pair, QVal measures how well a method's score is Q-aligned: whether it orders actions according to the Q-values of a strong reference-policy. This lets us compare signals before any training run and separate signal quality from other engineering choices. We instantiate QVal as QVal-v1.0, benchmarking 21 dense supervision methods across four diverse environments and seven methodological families, with over 1.2K evaluation experiments across six open-weight model backbones. We find that simple prompting baselines consistently outperform recent dense supervision methods from the literature, and that performance clusters strongly by family. These findings hold across model sizes, environments, and observation modalities. QVal is designed to be easily extensible to new environments and methods, enabling researchers to iterate on dense supervision methods before any training run.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.32034v1) | [PDF](https://arxiv.org/pdf/2606.32034v1)

### [World Narrative Model for Highly Controllable Video Generation: A Paradigm Shift from Pixel Sampling to Physical World Orchestration](http://arxiv.org/abs/2606.31946v1)

- **arXiv ID**: `2606.31946v1`
- **作者 / Authors**: Ye Chen, Xuanhong Chen, Yupeng Zhu, Liming Tan, Zhewen Wan et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

The fundamental obstacle to industrial grade video generation is the lack of controllability: existing models treat video as a pixel distribution sampling problem, bypassing the explicit, instance level $4D$ $(3D + T)$ physical world. Consequently, content creators cannot specify geometry, motion, camera parameters, or lighting in a deterministic, quantitative way, leading to the infamous ''gacha'' loop that makes professional content creation prohibitively inefficient and expensive. To address this, we introduce the World Narrative Model (WNM), a paradigm that decouples what to render -- the structured physical narrative -- from how to render -- the pixel generation process. WNM replaces end-to-end black-box sampling with orchestrated $4D$ pre-visualization for media generation. Collaborative agents translate sparse multimodal inputs, including text, reference videos, and sketches, into a fully editable world representation with scene geometry, object layouts, character/animal skeleton motion, trajectories, camera motion, and lighting at quantitative, physically meaningful granularity. This representation acts as a deterministic structural blueprint that drives existing video foundation models, either frozen or lightly adapted, to render final footage, turning the base model into a faithful neural shader. Built on this engine, our human-AI platform supports automatic world generation and pre-visualization aligned with professional filmmaking pipelines, while director consoles enable seamless human refinement. Experiments show that WNM greatly reduces probabilistic ``gacha'' calls and produces videos whose layout, motion, and cinematography closely follow creator intent. The framework is open and modular, allowing each component, such as world representation, control agents, and adapters, to be independently improved. Project website: https://glassroom.sjtu.edu.cn/WNM/.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31946v1) | [PDF](https://arxiv.org/pdf/2606.31946v1)

### [An Agentic AI Framework to Accelerate Scientific Discovery in Plant Phenotyping](http://arxiv.org/abs/2606.31831v1)

- **arXiv ID**: `2606.31831v1`
- **作者 / Authors**: Renan Souza, Daniel Rosendo, Kelsey Carter, John Lagergren, Frédéric Suter et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

High-throughput plant phenotyping now generates image derived datasets far faster than scientists can analyze them. At Oak Ridge National Laboratory's Advanced Plant Phenotyping Laboratory (APPL), automated stations image hundreds of plants daily across multiple remote sensing modalities; yet, trait extraction and interpretation remain manual, expert-bound, and strictly post-hoc, making analysis, not acquisition, the binding constraint on discovery. We present an end-to-end agentic AI framework that turns the facility from a data factory into an interactive autonomous, discovery platform, where scientists partner with AI agents to accelerate time to insight. A conversational Co-Scientist Agent translates a scientist's natural-language question into a structured analysis plan, and a headless Compute Agent dispatches Vision Transformer segmentation and trait extraction on the Frontier exascale supercomputer. The two agents run in separate security and resource domains and communicate over a secure, token-authenticated streaming channel, a design that accounts for the federation, data-movement, and provenance realities cloud-native agentic frameworks ignore, ensuring end-to-end provenance is captured for every interaction. The framework turns a days- to weeks-long analysis process into an interactive loop where agents reason over results, recommend next analyses, and respond to follow-up questions in seconds.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31831v1) | [PDF](https://arxiv.org/pdf/2606.31831v1)

### [JETO-Bench: A Reproducible Benchmark for Execution Time Improvement Patches in Java](http://arxiv.org/abs/2606.31767v1)

- **arXiv ID**: `2606.31767v1`
- **作者 / Authors**: Khashayar Etemadi, Zhendong Su
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.SE

<details>
<summary>📝 Abstract</summary>

Automated fixing of performance issues is gaining increasing attention. However, existing benchmarks of execution time improvement patches are fixed datasets that target Python, C++, or .NET and cannot be extended to new patches according to user-defined configurations. In this paper, we present JETO-Mine, the first configurable and reusable tool for automatically creating reproducible benchmarks of execution time improvement patches (ETIPs) in real-world Java projects. JETO-Mine employs a three-phase pipeline: a static analysis phase that crawls GitHub repositories and identifies ETIPs using user-defined filters and an LLM-based issue classifier, a dynamic analysis phase that wraps the identified ETIPs in Docker images for fully reproducible execution and performs statistical testing to find objective evidence of execution time improvement, and an evaluation harness that enables quantitative assessment of both generated patches and generated tests. Unlike existing benchmarks, JETO-Mine is designed as a reusable tool that allows researchers continuously collect new benchmarks with their own desired filters and statistical rigor levels. We use JETO-Mine to build JETO-Bench, a benchmark of 660 identified ETIPs and 91 manually verified executable ETIPs collected from 174 open-source Java repositories. To build JETO-Bench, JETO-Mine scans 11 years of open-source development history and nearly 1.8 million commits. We run OpenHands, a leading open-source coding agent, on the 91 manually verified executable ETIPs in JETO-Bench and find that it correctly fixes 14.3% (13/91) of the issues, aligning with results reported by similar studies on other programming languages. Our results also reveal that open-source Java projects largely lack tests that demonstrate execution time improvements, presenting an opportunity for future research in test generation.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31767v1) | [PDF](https://arxiv.org/pdf/2606.31767v1)

### [A Self-Evolving Agentic System for Automated Generation and Execution of Biological Protocols](http://arxiv.org/abs/2606.31763v1)

- **arXiv ID**: `2606.31763v1`
- **作者 / Authors**: Yankai Jiang, Weiting Tang, Haoran Sun, Zhenyu Tang, Yuejie Hou et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Autonomous wet-lab experimentation requires more than plausible protocol text: biological intent, quantitative procedures, device constraints and experimental feedback must remain aligned from protocol and SOP design to code and physical execution. We developed ProtoPilot, a self-evolving multi-agent system, together with an expert-grounded benchmark and evaluation framework for testing this conversion as an experimental automation problem. The framework spans 294 synthetic-biology and molecular-biology tasks derived from 98 gold-standard protocols, wet-lab expert rubrics, device-level validity gates and real experimental tests. ProtoPilot incorporates layer-wise verifiability, multi-agent orchestration and a runtime-updated skill library to generate protocols, expand SOPs, synthesize SDK-compliant code and revise workflows from wet-lab feedback. It achieved a Top@3 expert-preference rate of 90.2%, an overall protocol-to-code gate pass rate of 89.5% and an Opentrons pass rate of 88.24%, compared with 32.35% for OpenTrons-AI. Wet-lab validation produced interpretable readouts, Sanger-confirmed products and feedback-corrected PCA-assembled DNA targets, establishing a verifiable route to autonomous experimentation. Together, these results show that the evaluation framework captures execution-relevant requirements for autonomous wet-lab automation, and that ProtoPilot can meet them by converting protocol and code generation into validated execution and feedback-guided revision.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31763v1) | [PDF](https://arxiv.org/pdf/2606.31763v1)

### [ECHO: Prune to act, trace to learn with selective turn memory in agentic RL](http://arxiv.org/abs/2606.31650v1)

- **arXiv ID**: `2606.31650v1`
- **作者 / Authors**: Zijun Xie, Binbin Zheng, Enlei Gong, Jihua Liu, Yuyang You et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Long-horizon language agents must repeatedly interact with tools, accumulate evidence, and make decisions under bounded context windows. Existing context-management methods make such rollouts feasible by truncating distant history, folding past turns into summaries, or selecting compact memory states. However, these breakthroughs introduce two coupled limitations. First, as the number of turns grows, historical observations are progressively removed or collapsed into compressed states, making it harder for the policy to reuse fine-grained evidence. Second, once the original turns are no longer source-addressable, outcome-based RL loses an explicit path for aligning policy updates with the evidence that supported a successful final answer. To this end, we propose ECHO, a selective turn-memory framework that jointly addresses history collapse and traceable learning through source-indexed reconstruction. Specifically, ECHO compresses each completed environment turn into a compact memory record, reconstructs bounded policy contexts by selecting from these records, and reuses the selected source indices to route positive outcome credit to the evidence and selection actions that support successful answers. On BrowseComp-Plus, ECHO reaches 43.4% held-out accuracy, outperforming GRPO (28.9%) and the rolling-summary baseline SUPO (36.1%), while using fewer turns and lower trajectory volume than SUPO (Figure 1). Additionally, the trained policy improves zero-shot generalization across multi-objective QA, code generation, and deep information-seeking benchmarks on both dense and MoE backbones.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31650v1) | [PDF](https://arxiv.org/pdf/2606.31650v1)

### [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](http://arxiv.org/abs/2606.31635v1)

- **arXiv ID**: `2606.31635v1`
- **作者 / Authors**: Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: eess.SY

<details>
<summary>📝 Abstract</summary>

Fault recovery in process plants still relies heavily on plant operators, especially when faults fall outside predefined supervisory logic. Operators interpret alarms, procedures, P\&IDs, interlocks, and process trends, then decide how to move the plant to a safe operating mode without triggering a shutdown. This paper examines how Large Language Model (LLM) agents can support such recovery decisions. The proposed framework treats the LLM as a constrained supervisory planner. It uses plant-specific knowledge to propose recovery actions, and every proposal is checked by an external validator (symbolic or simulation-based) before actuation. The paper develops three design dimensions for applying the framework: the recovery patterns for which LLM agents are useful, the validation strategies that separate admissible from inadmissible proposals, and the deployment constraints imposed by latency, knowledge engineering, safety integration, and model lifecycle management. To make the framework directly usable, two openly available executable Python environments are provided. Both re-implement established case studies, a modular mixing module and a continuous stirred-tank reactor, extended with configurable faults and defined interfaces for custom recovery and validation methods.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31635v1) | [PDF](https://arxiv.org/pdf/2606.31635v1)

### [AutoTrainess: Teaching Language Models to Improve Language Models Autonomously](http://arxiv.org/abs/2606.31551v1)

- **arXiv ID**: `2606.31551v1`
- **作者 / Authors**: Zhaojian Yu, Penghao Yin, Shuzheng Gao, Shilin He, Kai Cai et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Training language models (LMs) remains a highly human-intensive process, even as frontier language model agents become increasingly capable at software engineering and other long-horizon tasks. A central challenge is that autonomous post-training is not just a coding problem: it requires the agent to repeatedly plan iterations, construct benchmark-aligned data, run stable training jobs, evaluate checkpoints, and preserve experiment state across many hours of interaction. We present AutoTrainess, a LM agent that exposes these operations as a repository of agent-computer interfaces for planning, data preparation, training, evaluation, and logging. Rather than leaving the agent to operate in a raw CLI environment with an underspecified action space, AutoTrainess externalizes prior human experience as explicit workflows, rules, and execution constraints that guide the agent toward effective and reliable training behavior. On PostTrainBench, AutoTrainess consistently outperforms CLI-only baselines, achieving 26.94 average score with GPT-5.4 (Codex) versus 23.21 for CLI-only. It also generalizes across models and harnesses, improving DeepSeek-V4-Flash (OpenCode) from 12.13 to 19.58.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31551v1) | [PDF](https://arxiv.org/pdf/2606.31551v1)

### [DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation](http://arxiv.org/abs/2606.31537v1)

- **arXiv ID**: `2606.31537v1`
- **作者 / Authors**: Siyu Yan, Yizhen Gao, Yilin Wang, Dongxing Mao, Alex Jinpeng Wang
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Text-rich image generation is one of the most challenging settings in image generation, since models must simultaneously produce visually realistic images and render legible, semantically aligned, and layout-consistent text. Existing data pipelines usually follow a static crawl-filter-freeze paradigm. They collect candidate samples, filter them once, and freeze the accepted data for training. However, rejected samples are usually discarded, although they often contain useful failure signals such as OCR errors and semantic mismatches. As a result, later construction rounds may repeat the same failure modes. To address these limitations, we propose DataEvolver, a self-evolving multi-agent framework for text-rich image data construction. DataEvolver treats data construction as feedback-driven construction policy evolution. A Retriever collects candidate samples, a Verifier assigns quality scores and rejection causes, a Critic summarizes round-level feedback into semantic feedback, and a Generator completes under-covered regions through targeted synthesis. The updated feedback memory then guides the next construction round. Experiments on text-rich image generation benchmarks show that DataEvolver produces more useful training data than fixed-dataset baselines under matched data budgets. At the 0.75M scale on PixArt-alpha, DataEvolver improves OCR-F1 over the strongest baseline by 85.3 percent on TextScenesHQ and 35.3 percent on LongTextBench. The improvements are consistent across both evaluated benchmarks and also transfer to Show-o2, indicating that the benefit of DataEvolver is not tied to a single downstream generator. These results suggest that rejected samples can provide actionable feedback for improving text-rich image data construction.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31537v1) | [PDF](https://arxiv.org/pdf/2606.31537v1)

### [One Reflection Is Not Enough: Self-Correcting Autonomous Research via Multi-Hypothesis Failure Attribution](http://arxiv.org/abs/2606.31478v1)

- **arXiv ID**: `2606.31478v1`
- **作者 / Authors**: Jie Ma, Binfei Chu, Jie Gao, Jinlu Zhang, Yiwei Ma et al.
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Autonomous research agents can now draft hypotheses, write code, run experiments, and produce papers, but they remain brittle when experiments fail. Under the prevailing paradigm, failure recovery is usually delegated to a single free-form reflection: a rich trajectory of metrics, logs, and design choices is compressed into one verbal critique, which often leads either to localized trial-and-error or to hard pivots that discard useful context. We propose SAGE, a Self-correcting, Autonomous, Grounded Experimenter, to tackle this failure-recovery bottleneck. Its core mechanism, Multi-Hypothesis Failure Attribution (MHFA), treats recovery as a structured causal diagnosis. By analyzing dynamic trajectory features, MHFA systematically generates multiple evidence-grounded explanations for a failure, independently evaluates their severity, and deterministically routes the verified root cause to the correct intervention level (hypothesis, experimental design, or implementation). To guarantee scientific honesty, SAGE further employs a grounded reporting mechanism that explicitly constrains drafted results to actual measured values, redacting hallucinated numbers. On a 12-topic, 5-domain benchmark, SAGE increases metrics-bearing outputs from 42% to 92% over a reflection baseline, improves artifact quality from 5.00 to 6.75/10, and blindly outscores AI-Scientist-v2 (52.0 vs. 48.2), with gains concentrated in code development and execution. While fully autonomous scientific writing and generating conference-ready papers remain notoriously difficult open problems for the entire field, SAGE successfully produces significantly more reliable and higher-quality scientific artifacts. Ultimately, by coupling structured recovery with explicit grounding constraints, SAGE significantly outperforms monolithic reflection paradigms, establishing a highly trustworthy foundation for future autonomous research.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31478v1) | [PDF](https://arxiv.org/pdf/2606.31478v1)

### [Learning Fair Allocation of Indivisible Items from Limited Feedback](http://arxiv.org/abs/2606.31457v1)

- **arXiv ID**: `2606.31457v1`
- **作者 / Authors**: Xinyu Liu, David Kempe, Evi Micha
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.GT

<details>
<summary>📝 Abstract</summary>

We study a setting in which an algorithm must output a fair allocation of indivisible items while "learning on the job". More specifically, the algorithm is to output an allocation satisfying EF1, PROP1, or similar fairness notions; however, the algorithm initially has no information about the agents' valuations, and can only learn about them by (repeatedly) proposing an allocation, and obtaining feedback about a fairness violation in the allocation. Importantly, the observed fairness violation may be adversarially chosen. The algorithm's goal is to converge to a fair allocation in rounds polynomial in the number of agents and items, ideally with only polynomial computation.   We prove two main results: first, when the valuations are additive, then even for mixed items (goods and chores), an allocation satisfying EF1 or PROP1 can be found in polynomial time using the corresponding feedback. These results are instantiations of a more general framework which maintains a polytope of candidate valuations consistent with all past feedback. The algorithm repeatedly constructs putative valuations and uses them to propose allocations; the observed violations then define separating hyperplanes, allowing the algorithm to emulate the ellipsoid method.   When the valuations are monotone, we present an algorithm which is guaranteed to find an EF1 allocation in polynomially many iterations; however, its internal calculations are not guaranteed to be polynomial. The algorithm again maintains putative valuations, and only considers allocations in which each agent obtains an interval plus one additional item with respect to an arbitrary ordering of the items. We (non-constructively) prove that there always exist EF1 allocations of this form, allowing us to use a further generalization of the preceding ellipsoid-based ideas.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31457v1) | [PDF](https://arxiv.org/pdf/2606.31457v1)

### [When the Database Fails: Prompting LLM Dialogue Agents for Safe Recovery in Task-Oriented Dialogue](http://arxiv.org/abs/2606.31307v1)

- **arXiv ID**: `2606.31307v1`
- **作者 / Authors**: Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Jiann Shiun Yuan
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CL

<details>
<summary>📝 Abstract</summary>

Large language models used in task-oriented dialogue often produce fluent but unsafe responses when backend database calls fail, return empty results, or surface mismatched information, inventing venues, confirmations, or booking details not grounded in the database. We study a lightweight prompting-based recovery approach that improves robustness without retraining or additional model calls. We compare three response strategies, including a guided recovery prompt conditioned on structured database status, across six open-weight model families (DeepSeek-R1, Gemma-2, Llama-3, Mistral, Phi-3, and Qwen-2.5) and four database conditions: empty result, wrong-domain retrieval, API error, and clean retrieval. Using fault-injected benchmarks built on two structurally different datasets, MultiWOZ 2.2 (5 domains) and SGD (20 domains), we find that naive agents hallucinate on 30.5% of failure turns on MultiWOZ and 20.9% on SGD. Our Guided-Retry strategy reduces hallucination by 50% on MultiWOZ (30.5 to 15.3%) and by 42% on SGD (20.9 to 12.2%) without retraining. However, residual hallucination remains substantial (6-37% across models), with wrong-domain failures the hardest case. Results are consistent across both datasets and all six model families, and human annotation shows substantial agreement while supporting the validity of the automatic commitment-safety metric.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31307v1) | [PDF](https://arxiv.org/pdf/2606.31307v1)

### [Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling](http://arxiv.org/abs/2606.31252v1)

- **arXiv ID**: `2606.31252v1`
- **作者 / Authors**: Fumin Liu, Haoyu Zhou, Fei Hao, Lin Yang
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Large language models can write plausible CAD scripts, but reliable industrial CAD modeling requires more than syntactically valid code: every feature, placement, and assembly relation must be accepted by an exact geometric kernel while remaining editable as parametric boundary representation geometry. We present Embodied CAD, solver-grounded LLM agents for parametric B-Rep assembly modeling. Instead of generating a complete script in one pass, the agent iteratively selects actions from a stratified L0-L4 CAD skill library, resolves them into typed geometric operations, executes them in a CAD backend, and uses solver feedback to plan, repair, and learn. The framework combines action grammar constraints, deterministic parameter resolution, and solver-derived rewards for supervised warm-up and GRPO-style refinement. We evaluate Embodied CAD on multi-step mechanical, industrial equipment, and mold-oriented assembly tasks using solver-aligned metrics: executable rate, skill accuracy, operation-family accuracy, exact policy accuracy, and task completion success. The results show that solver-grounded planning executes all strong-planner workflows in the current benchmark, while learned controllers reach high executable rates and expose the remaining gap between valid tool calls and exact long-horizon policy prediction.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31252v1) | [PDF](https://arxiv.org/pdf/2606.31252v1)

### [DDIAgents: Mechanism-Conditioned Context Flow for Drug-Drug Interaction Prediction](http://arxiv.org/abs/2606.31085v1)

- **arXiv ID**: `2606.31085v1`
- **作者 / Authors**: Zhenqian Shen, Yu Liu, Xiaoyi Fu, Quanming Yao
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Drug-drug interaction (DDI) prediction is essential for medication safety, yet it requires reasoning over heterogeneous biomedical evidence whose relevance changes across interaction mechanisms. We propose DDIAgents, a mechanism-conditioned multi-agent framework that performs DDI prediction through dynamic knowledge orchestration. Given a drug pair, a planner agent instantiates specialized expert agents, routes mechanism-relevant knowledge sources to each agent, and aggregates their analyses through a conclusion agent. By adapting context flow to the inferred interaction mechanism, DDIAgents reduces irrelevant information, supports complementary expert reasoning, and produces interpretable agent-level rationales. Extensive experiments on realistic DDI prediction benchmarks show that DDIAgents consistently outperforms existing feature-based, graph-based, LLM-based, and agent-based baselines. Beyond prediction performance, DDIAgents demonstrates how multi-agent systems can organize heterogeneous scientific knowledge for adaptive and interpretable AI4Science reasoning.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31085v1) | [PDF](https://arxiv.org/pdf/2606.31085v1)

### [Certified Speculative Execution for Untrusted AI Agents](http://arxiv.org/abs/2606.31023v1)

- **arXiv ID**: `2606.31023v1`
- **作者 / Authors**: Chenyu Zhou, Qiliang Jiang, Shuning Wu, Xu Zhou
- **发布日期 / Published**: 2026-06-30
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

Hard-constrained sequential decision systems have no certified way to spend the test-time compute of modern AI: executing the multi-step drafts of a learned policy or a frozen LLM forfeits the feasibility guarantee a trusted solver provides, while invoking the solver at every step forfeits the speed the AI offers. Certificate-Gated Prefix Acceptance (CGPA) closes this gap with a certified speculative-execution contract for untrusted AI agents: a trusted verifier rejects constraint-violating transitions exactly, a conformally calibrated value boundary gates the longest low-cost prefix within a per-segment regret budget, and the rest defers to the solver, so safety, regret, and speed decouple by construction. The contract drives every untrusted proposal source - adversarial drafters and six heterogeneous frozen LLMs (including a 12B model that violates constraints in 98% of direct rollouts) - to zero applied violations; a certificate-aware learned boundary, conformally calibrated, drives mean regret three orders of magnitude below unguarded acceptance, to within sampling noise of the stepwise oracle (95% CI spanning zero), and under calendar shift a learned proposal source overtakes it on 15 of 18 held-out days. On a deployment-scale unit-commitment instance it turns a frozen 8B LLM into a 2.96x per-episode wall-clock speedup at 2.1% regret, outpacing the domain heuristic (1.79x) and a safe receding-horizon baseline (1.07x): the more capable the untrusted source, the faster the certified system, at guarantees that never change.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.31023v1) | [PDF](https://arxiv.org/pdf/2606.31023v1)

### [Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction](http://arxiv.org/abs/2606.30014v1)

- **arXiv ID**: `2606.30014v1`
- **作者 / Authors**: Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Real-to-sim reconstruction for embodied AI requires geometry that is useful for collision reasoning, navigation, and agent-environment interaction, not only photorealistic novel-view synthesis. However, close-range urban facades are difficult for video-to-3D reconstruction: glass, reflections, repeated windows, and weak texture can produce visually plausible renderings with unstable surface geometry. We introduce shell-supervised Gaussian Splatting, a reconstruction-stage framework that uses an external facade structural shell as lightweight geometric supervision for video-driven Gaussian reconstruction. The method aligns an exterior shell to the video reconstruction frame, renders per-view depth, camera-space normal, and valid-mask maps, and applies these cues through mask-gated losses during Gaussian optimization. This design preserves RGB-driven appearance while regularizing only visible shell-supported facade regions. Experiments on anonymized close-range urban facade scenes show improved facade orientation and visible-surface point-cloud consistency over photo-only, monocular-cue, and surface-oriented Gaussian baselines, while maintaining comparable held-out rendering quality.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30014v1) | [PDF](https://arxiv.org/pdf/2606.30014v1)

### [SICAGE: Speaker-Independent Culture-Aware Gesture Generation using TED4C-L Dataset](http://arxiv.org/abs/2606.30001v1)

- **arXiv ID**: `2606.30001v1`
- **作者 / Authors**: Ariel Gjaci, Antonio Sgorbissa, Vittorio Murino
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Recent co-speech gesture generation methods often overlook cultural differences, limiting their effectiveness in human-agent interaction. Moreover, culture-conditioned models are rarely evaluated under speaker-disjoint splits, so apparent "cultural" behavior may be confounded with speaker-specific gesturing style. We introduce SICAGE, a modular framework for culture-aware co-speech gesture generation that conditions motion synthesis models on speaker-independent cultural representations. SICAGE learns these representations from audio and text by treating each speaker as a separate domain while imposing invariance across speakers. This encourages representations to remain culture-discriminative while reducing dependence on speaker identity. The resulting cultural embeddings condition a multimodal generator to produce culturally appropriate gestures. We instantiate this idea with two domain generalization approaches: adversarial learning and Fishr regularization. We further introduce ALaDiT, a real-time diffusion-based gesture generator designed to efficiently incorporate the learned cultural embeddings. To validate our method, we built TED4C-L, a 106-hour multimodal dataset of 764 TED speakers from four cultural groups. Experiments show that SICAGE improves motion realism, diversity, beat synchronization, semantic relevance, and cultural consistency.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.30001v1) | [PDF](https://arxiv.org/pdf/2606.30001v1)

### [DEEPMED Search: An Open-Source Agentic Platform for Medical Deep Research with Introspective Verification](http://arxiv.org/abs/2606.29746v1)

- **arXiv ID**: `2606.29746v1`
- **作者 / Authors**: Maolin Liu, Fanyu Xu, Ruoqing Xu, Jiahang Zhang, Hao Wang et al.
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Navigating the deluge of heterogeneous medical data, from academic literature (PubMed) to clinical guidelines (Web) and private knowledge bases, remains a critical bottleneck for evidence-based medicine. While commercial black-box tools lack transparency, standard open-source RAG implementations frequently suffer from reasoning drift when handling complex, long-tail queries. We present DEEPMED Search, a fully open-source, agentic platform designed for transparent medical deep research. Built on a high-performance Next.js architecture, DEEPMED Search features a source-adaptive router that autonomously dispatches sub-queries to PubMed, web search, or local graph-based knowledge bases based on information density. Crucially, the platform integrates an introspective verification module, powered by a causal-consistent multi-agent debate framework, to validate retrieved evidence against diagnostic logic before synthesis. To demonstrate its robustness, we showcase DEEPMED Search's ability to autonomously decompose high-difficulty rare disease queries, filter out confounding noise, and generate structured, citation-backed research reports in minutes. By open-sourcing this software, we provide the community with a robust infrastructure to democratize access to trustworthy, glass-box medical reasoning in research and prototyping settings.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29746v1) | [PDF](https://arxiv.org/pdf/2606.29746v1)

### [Attraction, Not Adaptation: How AI Agent Communities Develop Distinct Linguistic Identities](http://arxiv.org/abs/2606.29722v1)

- **arXiv ID**: `2606.29722v1`
- **作者 / Authors**: Daming Li, Simeng Han, Can Meng, Wanyu Lei, Jialu Zhang
- **发布日期 / Published**: 2026-06-29
- **分类 / Category**: cs.SI

<details>
<summary>📝 Abstract</summary>

When tens of thousands of autonomous AI agents interact in topical online forums, do they develop distinct community-specific linguistic identities? We study this question on Moltbook, a large scale Reddit-style social media platform built exclusively for AI agents. Using the public Moltbook Observatory Archive dataset with over 3.1 million posts and 1.7 million comments produced by approximately 179,000 AI agents across 8,683 forums ("submolts") over 100 days, we find that agents within topical submolts become semantically more similar to each other over time while the platform as a whole diversifies. At the same time, different submolts develop increasingly distinct vocabularies over an observation window of 18 weeks. Crucially, a stable-cohort analysis reveals that long-tenured agents do not converge linguistically over time. Instead, community-level linguistic differentiation operates through selective attraction - newcomers arrive already linguistically compatible with their chosen community - and differential retention - conforming agents remain active longer. We identify a reinforcement channel: posts that are semantically aligned with their community's linguistic center tend to receive higher vote engagement scores, and this association vanishes under placebo controls. Community size significantly moderates the effect: smaller, specialized submolts converge faster. Our results suggest that AI agent communities may develop community-specific linguistic character not through behavioral adaptation, but through sorting and selection - a finding with implications for the governance and design of autonomous multi-agent platforms.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29722v1) | [PDF](https://arxiv.org/pdf/2606.29722v1)

### [Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds](http://arxiv.org/abs/2606.29654v1)

- **arXiv ID**: `2606.29654v1`
- **作者 / Authors**: Mengdie Flora Wang, Haochen Xie, Guanghui Wang, Devin Zhang, Jae Oh Woo
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Multi-agent deliberation among LLMs can improve reasoning, but deployment requires deciding when the current answer is reliable enough to act on and when it should be escalated to human review. We formulate this as budgeted act-or-defer decision making. At each round, the system maps the debate prefix to a low-dimensional state, computes a $k$-nearest-neighbor lower confidence bound on state-conditional correctness using calibration data, and acts only when the bound exceeds a user-specified reliability threshold. The certificate controls wrong actions through the decomposition $β= δ+ α+ \varepsilon_{\mathrm{act}}$, separating calibration failure, residual action risk, and representation gap. The guarantee is conditional, not distribution-free: it relies on a valid local bias envelope and an action-region representation-gap bound, and each assumption is paired with falsification-style diagnostics. Because the same absolute wrong-action budget has different meanings across tasks of different difficulty, we set budgets relative to each task's final-round error using training data only, and evaluate safety by normalized budget usage $\mathrm{WA}/β$. On six benchmarks against nine baselines, the method uses 9--12% of the pre-declared budget on activated datasets, reaching up to 84% automation and 96% acted-on accuracy; on stress-test datasets, it defers rather than forcing unreliable automation. Rather than relying on per-task post-hoc threshold search, the method prospectively converts a user-declared wrong-action budget into an auditable act-or-defer operating point before deployment, under explicitly stated assumptions.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29654v1) | [PDF](https://arxiv.org/pdf/2606.29654v1)

### [OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](http://arxiv.org/abs/2606.29537v1)

- **arXiv ID**: `2606.29537v1`
- **作者 / Authors**: Mengqi Yuan, Zilong Zhou, Xinzhuang Xiong, Weiming Wu, Jiayang Sun et al.
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Existing computer-use benchmarks fail to capture the realism, complexity, and long-horizon demands of real-world computer use, limiting their ability to reveal the limitations of frontier agents. We introduce OSWorld 2.0, a benchmark of 108 long-horizon computer-use workflows across everyday and professional tasks, designed to capture complex and challenging real-world phenomena. Each task represents a realistic end-to-end workflow that takes human users a median of about 1.6 hours to complete and requires an average of 318 tool calls with Claude Opus 4.7 using maximum thinking, compared with about 30 in OSWorld 1.0. OSWorld 2.0 targets challenge phenomena that are common in real workflows yet underrepresented in prior benchmarks, spanning interaction-design challenges such as streaming interaction and dynamic environments, as well as agent-pattern challenges such as cross-source reasoning, implicit-state inference, and visual-spatial precision. Tasks are grounded in authentic input artifacts and cross-referenced against realistic stateful user profile data, and include separate safety reports auditing safety-sensitive execution. Under our primary binary-completion metric at 500 steps, Claude Opus 4.8 with maximum thinking and batched tool calls scores best but still completes only 20.6% of tasks at a 54.8% partial score; GPT-5.5 is far more token-efficient yet plateaus near 13%. These results show that current agents are still far from professional-level computer use: rather than stumbling on basic GUI control or coding, they lose track of constraints, miss information that arrives mid-task, guess rather than ask the user, and skip verification, struggling most when a task hinges on hidden state they must recover.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29537v1) | [PDF](https://arxiv.org/pdf/2606.29537v1)

### [LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents](http://arxiv.org/abs/2606.29399v1)

- **arXiv ID**: `2606.29399v1`
- **作者 / Authors**: Mingyu Jeon, Bokyeong Kim, Suwan Cho, Jae Young Suh, Yonggyun Yu
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Reviewing nuclear regulatory documents requires multi-hop reasoning across tens of thousands of pages, where judgments depend on evidence assembled across multiple chapters. We frame this task as planning: an LLM-based agent observes the evidence collected so far, picks the next document fragment to inspect, and stops when the evidence is sufficient. The agent operates over a vectorless document tree using browse, read, and search tools, and maintains a dynamic knowledge graph (KG) as state. On a 200-question benchmark over NuScale Final Safety Analysis Report (FSAR) documents, the system reaches 81.5% accuracy with a RAGAS Faithfulness of 0.93. The dominant performance factor is planning: against PageIndex, which uses the same document tree without state-conditioned action selection, the gap is +38.0pp (43.5% to 81.5%, p<0.001). The system also outperforms LightRAG (73.0%, p<0.05), HippoRAG (70.5%, p<0.01), and GraphRAG (49.5%, p<0.001), and matches RAPTOR (75.5%, p=0.11) without offline indexing. Edge inference adds 2.8x cost without raising accuracy; we retain it as a traceability module. Of 7,391 inferred edges, 3 Violates edges (0.04%) flag scope boundaries (Q058) and partial conformance (Q176) as typed annotations that a human reviewer can audit.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29399v1) | [PDF](https://arxiv.org/pdf/2606.29399v1)

### [When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning](http://arxiv.org/abs/2606.29354v1)

- **arXiv ID**: `2606.29354v1`
- **作者 / Authors**: Zhengqi Pei, Qingming Huang, Shuhui Wang
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Chain-of-Thought (CoT) improves large language models (LLMs) on difficult reasoning tasks, but it often incurs long natural-language rationales that are poorly aligned with efficient machine reasoning. We propose Communicative Language Symbolism Routing (CLSR), a test-time framework in which multiple LLM agents autonomously invent, evolve, and share compact Language Symbolism Frameworks (LSFs), while a latent-free router adaptively selects and composes these languages per query to optimize the accuracy-token trade-off. Unlike prompt optimization that refines surface instructions, CLSR treats each LSF as a reusable symbolic protocol with compact symbols, usage rules, and a message-passing contract, and improves it through an evolutionary loop driven by correctness and token cost. At inference time, the router may invoke a single low-cost LSF call, ensemble multiple LSFs, or execute a multi-round LSF composition protocol on harder queries. Across challenging benchmarks, CLSR reduces latency-oriented generated token completion by $3\sim 6\times$ compared to standard CoT while maintaining accuracy. We further derive an information-theoretic lower bound on token cost under arbitrary symbolism and show that, under an interpreter-realizability premise, multi-round LSF protocols conditionally subsume program-execution pipelines. Code is publicly available (https://github.com/pzqpzq/LSF_MDia).

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29354v1) | [PDF](https://arxiv.org/pdf/2606.29354v1)

### [Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates](http://arxiv.org/abs/2606.29270v1)

- **arXiv ID**: `2606.29270v1`
- **作者 / Authors**: Chuan He, Zebin Chen, Zhengyi Yang, Shaobo Qiao, Mingchen Ju et al.
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.MA

<details>
<summary>📝 Abstract</summary>

Multi-Agent Debate (MAD) with Majority Voting is a dominant paradigm for improving LLM reasoning, yet its effectiveness rests on the Condorcet Jury Theorem's assumption of independent errors. Because contemporary LLMs share similar pretraining corpora, their errors are strongly correlated, causing the majority to systematically suppress correct minority opinions, a phenomenon we term Minority Truth. Through debates among three heterogeneous LLM agents on six benchmarks, we find that roughly one in four divergent cases has the minority holding the correct answer, yielding a 10-percentage-point theoretical recovery margin. We propose Minority Sentinel, a lightweight meta-classifier that extracts a multi-dimensional debate fingerprint from debate logs and trains a LightGBM model to decide when to overturn majority voting. Minority Sentinel achieves a stable Flip Precision of 81.2% with positive Net Gain across all six datasets and all 20 random seed trials, demonstrating that debate logs contain sufficient behavioral signals for a non-LLM classifier to reliably recover suppressed minorities without degrading system accuracy. The LLM-as-Judge baseline yields negative Net Gain despite higher recall, confirming that flip safety, not recovery volume, determines intervention value.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29270v1) | [PDF](https://arxiv.org/pdf/2606.29270v1)

### [Direct Causation in International Humanitarian Law and the Challenge of AI-Mediated Civilian Cyber Operations](http://arxiv.org/abs/2606.29175v1)

- **arXiv ID**: `2606.29175v1`
- **作者 / Authors**: Alice Saito, Harold Godsoe, Phan Xuan Tan
- **发布日期 / Published**: 2026-06-28
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

International humanitarian law protects civilians from direct attack unless and for such time as they take direct part in hostilities, with the ICRC's 2009 Interpretive Guidance operationalising this rule through a three-criterion cumulative test. This paper argues that AI-mediated civilian cyber operations challenge the direct causation element of this test in a structurally specific way: when a civilian deploys an autonomous multi-agent cyber system of the kind recently demonstrated in offensive AI research, the "one causal step" standard fails because harm is produced by system-generated decisions made after human disengagement, and the integral-part requirement does not extend because it presupposes downstream human contributors whose conduct can be independently classified. The framework therefore defaults to treating such deployments as indirect participation, in tension with its purpose of capturing civilians who personally take part in hostilities. Beyond the doctrinal analysis, this paper identifies goal-specification granularity as the property on which the integral-part test's concreteness component implicitly turns, classifies AI-mediated operations along a five-level spectrum, and argues that existing technical AI governance instruments do not log or report this property.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29175v1) | [PDF](https://arxiv.org/pdf/2606.29175v1)

### [Characterizing Large Language Model Agentic Workflows: A Study on N8n Ecosystem](http://arxiv.org/abs/2606.29116v1)

- **arXiv ID**: `2606.29116v1`
- **作者 / Authors**: Yutian Tang, Yuming Zhou, Huaming Chen
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.AI

<details>
<summary>📝 Abstract</summary>

Large Language Models (LLMs) are rapidly being adopted in low-code and no-code automation platforms, where non-expert users design workflows that combine natural language understanding with external services and APIs. LLM agents are LLM systems that use LLMs as a core "brain" to reason, plan, and autonomously execute complex, multi-step tasks. In this paper, we present the first large-scale empirical study of LLM agentic workflows in low-code automation platforms. We analyze more than 6,000 publicly available n8n workflows and examine four aspects of their design: task distribution, structural and tool use patterns, reliability mechanisms, and autonomy levels. Our analysis shows that LLM workflows are not merely prompt response pipelines. Instead, LLMs are commonly embedded within broader automation structures involving control logic, external tools, communication services, storage systems, and human review points. We further find that while many workflows include lightweight post-processing or routing logic after LLM execution, explicit reliability mechanisms such as structured fallback paths, repair loops, failure-specific alerts, and human approval gates remain relatively uncommon. These results reveal a gap between the increasing deployment of LLM agents in practical automation ecosystems and the limited engineering support for reliability, safety, and governance. Overall, our study provides ten empirical findings and five research takeaways for researchers, platform developers, and practitioners seeking to understand and improve real-world LLM agentic workflows.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.29116v1) | [PDF](https://arxiv.org/pdf/2606.29116v1)

### [When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration](http://arxiv.org/abs/2606.28958v1)

- **arXiv ID**: `2606.28958v1`
- **作者 / Authors**: Luís Brito, Carlos Baquero
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.MA

<details>
<summary>📝 Abstract</summary>

LLM agents can share more than text. In some systems, an agent can send a short visible message while also passing its full KV-cache state to another model. This hidden state can help the final model combine evidence from several agents, but it is also hard to inspect. A visible message may look harmless even if the hidden state has been changed.   We study this problem in a multi-agent question-answering setup. Specialists each see part of the evidence, send a short commitment, and pass full KV-cache state to a coordinator. In clean runs, this latent collaboration improves over a matched text-only version. On transformed HiddenBench with Qwen3-4B, it reaches EM/F1 of 0.338/0.486, compared with 0.231/0.369 for text collaboration. Qwen3-8B and HotPotQA runs show the same direction of improvement.   The problem appears when one specialist is malicious. Some false visible commitments can steer answers. More seriously, changing the hidden KV state can collapse performance even when the visible commitment still looks plausible. A verifier that checks only text misses this failure mode. Simple magnitude checks catch some obvious corruptions, but adaptive attacks can evade them while still damaging the final answer.   The most reliable fix we find is not to guess whether hidden state looks normal, but to protect it in transport. We implement an HMAC-SHA256 manifest that binds the specialist, session, model, visible commitment, tensor metadata, and payload digest. It accepts all 774 honest replayed payloads and rejects all 295 recorded tampered payloads. The main lesson is that full-KV latent memory can be useful, but it should be treated as a security-sensitive object, not as ordinary internal model state.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28958v1) | [PDF](https://arxiv.org/pdf/2606.28958v1)

### [Building AI-Ready Data Systems for Space Life Sciences, Aerospace Medicine, and Deep Space Exploration](http://arxiv.org/abs/2606.28856v1)

- **arXiv ID**: `2606.28856v1`
- **作者 / Authors**: Sylvain V. Costes, Sergio Garcia Busto, Ryan T. Scott, James A. Casaletto, Gautier Bardi de Fourtou et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: q-bio.OT

<details>
<summary>📝 Abstract</summary>

While AI holds the potential to revolutionize space life sciences, realizing this promise is contingent upon the systematic restructuring of heterogeneous spaceflight biological data into machine-actionable, AI-ready forms. Even though open access principles support human reuse and scientific reproducibility, this does not necessarily enable AI systems to access and analyze such a diverse set of scientific datasets. In addition, the growing array of AI approaches places distinct demands on data structure, metadata, and access interfaces. In order to respond to such growing changes we propose a three-tier approach, proceeding from FAIR to AI-ready to space-ready data. We discuss existing infrastructures and how they can be improved to close the AI access gap. We conclude by proposing a neutral international coordinating body as the governance backbone for the trustworthy, agent-accessible space biology infrastructure that deep space biological research will require.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28856v1) | [PDF](https://arxiv.org/pdf/2606.28856v1)

### [ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models](http://arxiv.org/abs/2606.28804v1)

- **arXiv ID**: `2606.28804v1`
- **作者 / Authors**: Longyu Chen, Heng Li, Wei Yang, Manqi Zhao, Dongsheng Jiang
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Embodied World Models (EWMs) have emerged as a scalable and risk-free paradigm for advancing embodied intelligence, enabling the safety-critical evaluation of Vision-Language-Action systems. However, their reliability as evaluation benchmarks and foundational simulators is often hindered by the representation gap between low-dimensional actions and high-dimensional video synthesis. This gap results in a lack of geometric correspondence, manifesting as accumulated trajectory drift and inconsistent robot-object interactions during long-horizon rollouts. To bridge this gap, we propose ViPSim, a framework that achieves consistent long-horizon generation through the synergistic collaboration of Visual and Parameter Spaces. We define the Visual Space as a domain of explicit spatial priors, integrating pixel-aligned projections of end-effector pose, camera perspectives, depth-informed scene geometry, and robotic morphological masks to provide dense structural grounding. Concurrently, the Parameter Space serves as a domain of numerical drivers, injecting raw action sequences and camera matrices to provide precise motion guidance. By unifying these two spaces, ViPSim ensures that the generated states are simultaneously anchored by geometric boundaries and steered by numerical commands. Extensive experiments demonstrate that ViPSim is backbone-agnostic and significantly enhances trajectory consistency. Notably, our approach exhibits emergent capabilities in generating complex interactions with deformable objects (e.g., cloth folding) and maintains robust performance in out-of-distribution and cross-embodiment scenarios, providing a high-fidelity foundation for the automated evaluation and predictive control of embodied agents.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28804v1) | [PDF](https://arxiv.org/pdf/2606.28804v1)

### [Telephony Voice Agent for Banking Services](http://arxiv.org/abs/2606.28779v1)

- **arXiv ID**: `2606.28779v1`
- **作者 / Authors**: Nitya Dhagat, Vipul K. Dabhi, Harshadkumar B. Prajapati, Zankhana J. Barad
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.HC

<details>
<summary>📝 Abstract</summary>

This paper proposes a voice-powered AI-based banking system based on Google Conversational Agent, Dialogflow CX, which provides safe and convenient banking by phone. The system supports essential banking functions such as balance inquiries, transaction history retrieval, card activations, PIN-based authentication of sensitive tasks, smooth live agent handoff for complex and out-of-scope queries, and ensures seamless handover to human agents when required. These tests were performed with high-duration calls, high concurrency, and noisy environments; the system proved to be scalable, responsive, and resilient. All the data used is safely stored in the cloud environment for efficiency and security in real-time voice interactions. A voice-based banking solution that is efficient and easy to use can be provided through this.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28779v1) | [PDF](https://arxiv.org/pdf/2606.28779v1)

### [Hierarchical Decision Making with Structured Policies: A Principled Design via Inverse Optimization](http://arxiv.org/abs/2606.28764v1)

- **arXiv ID**: `2606.28764v1`
- **作者 / Authors**: Yuexuan Wang, Jingyuan Zhou, Kaidi Yang
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Hierarchical decision-making frameworks are pivotal for addressing complex control tasks, enabling agents to decompose intricate problems into manageable subgoals. Despite their promise, existing hierarchical policies face critical limitations: (i) reinforcement learning (RL)-based methods struggle to guarantee strict constraint satisfaction, and (ii) optimal control (OC)-based approaches often rely on myopic and computationally prohibitive formulations. To reconcile these trade-offs, hierarchical RL-OC architectures have emerged as a promising paradigm. However, the formulation of the lower-level optimization within these frameworks remains underexplored, often relying on heuristic or myopic objectives. In this work, we propose a principled framework that systematically integrates upper-level goal abstraction with structured lower-level decision making. We adopt an inverse optimization approach to inform the structure of the lower-level problem from expert demonstrations, ensuring that the objective of the lower-level policy remains aligned with the overall long-term task goal. To validate the approach, our framework is evaluated on distinct decision making tasks: network-based resource allocation and continuous collision avoidance. Empirical results demonstrate that our method consistently outperforms strong baselines based on end-to-end RL, learning-augmented optimal control, and existing hierarchical RL approaches in both efficiency and decision quality.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28764v1) | [PDF](https://arxiv.org/pdf/2606.28764v1)

### [BackTranslation2.0 -- A Linguistically Motivated Metric to Assess Sign Language Production](http://arxiv.org/abs/2606.28673v1)

- **arXiv ID**: `2606.28673v1`
- **作者 / Authors**: Oliver Cory, Maksym Ivashechkin, Karahan Sahin, Oline Ranum, Jianhe Low et al.
- **发布日期 / Published**: 2026-06-27
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Sign Languages (SLs) are the primary means of communication for millions of deaf individuals, yet existing evaluation metrics for generated SL remain simplistic and poorly aligned with human judgements. We introduce BackTranslation2.0, a linguistically grounded evaluation metric for text-to-sign translation that moves beyond naïve backtranslation. Our approach adopts an agentic framework in which a deterministic pipeline orchestrates a suite of specialised tools to assess four scoring dimensions - grammatical correctness, phonological accuracy, motion fluency, and generation fidelity - aligned with human rater assessments. Tool outputs are not treated independently: a set of large language model (LLM)-based cross-referential comparison modules evaluates consistency across tools and checks outputs against linguistic expectations, enabling structured reasoning over grammatical, phonological, and motion-level evidence. Final dimension scores are computed through deterministic weighted formulas over validated tool outputs. To validate BackTranslation2.0, we introduce and evaluate on a British Sign Language (BSL) dataset rated in a human rater study across the same quality dimensions, following a protocol developed in collaboration between linguists and deaf experts, benchmarking against six baseline metrics. Our method demonstrates strong correlation with human judgements across all dimensions, providing a more comprehensive, interpretable, and linguistically principled evaluation framework for sign language production systems.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28673v1) | [PDF](https://arxiv.org/pdf/2606.28673v1)

### [Digitizing Coaching Intelligence: An Agentic Framework for Holistic Athlete Profiling using VLM and RAG](http://arxiv.org/abs/2606.28570v1)

- **arXiv ID**: `2606.28570v1`
- **作者 / Authors**: Deep Ghosal, Ishani Sen, Wazib Ansar, Amlan Chakrabarti
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CV

<details>
<summary>📝 Abstract</summary>

Athlete assessment is a critical process for tracking physical progress and identifying elite talent. However, during mass recruitment drives, traditional methods rely on manual observation, which is inherently subjective and unscalable, or basic computer vision (CV) systems limited to quantitative repetition counting. These standard approaches lack the "coaching intelligence" required to evaluate qualitative physiological markers such as form degradation, spinal articulation, and fatigue. This paper presents a novel, LLM-based hybrid agentic framework for automated, holistic athlete profiling that strictly aligns with the Sports Authority of India (SAI) assessment protocols. Orchestrated via LangGraph, our dual-pipeline architecture synthesizes the geometric precision of CV (MediaPipe) for kinematic tracking with the semantic reasoning of Vision-Language Models (Llama-4-scout). To overcome the latency and token constraints associated with multimodal video processing, we introduce a 3 X 3 "Smart Grid" temporal chunking strategy, reducing computational overhead by over 88% while preserving critical temporal continuity. To ensure data integrity and mitigate hallucination, the framework pioneers an autonomous "LLM-as-a-Judge" self-correction loop that cross-references quantitative and qualitative metrics before persistence. Finally, we implement a dual-persistence Retrieval-Augmented Generation (RAG) pipeline utilizing a vector search engine (ChromaDB). This enables coaches to bypass rigid SQL databases and perform complex semantic queries (e.g., "Identify athletes with high endurance but poor core rigidity") using natural language. Experimental results demonstrate that this multi-agent approach significantly bridges the gap between raw biometric tracking and actionable coaching insights, offering a scalable, objective solution for national talent identification.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28570v1) | [PDF](https://arxiv.org/pdf/2606.28570v1)

### [LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](http://arxiv.org/abs/2606.28182v1)

- **arXiv ID**: `2606.28182v1`
- **作者 / Authors**: Qinhong Zhou, Chuang Gan, Anoop Cherian
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Embodied agents operating in decentralized and partially observable environments have attracted growing attention in recent years. However, existing large language model (LLM)-based agents often exhibit behaviors that are misaligned with their partners or inconsistent with the environment state, leading to inefficient cooperation and poor task success. To address this challenge, we propose a novel framework, Learning Laws of Cooperation (LLawCo), that enables embodied agents to autonomously align with both their partners and task objectives. Our framework allows agents to reflect on past failures to extract misaligned behavioral patterns, which are used to derive high-level behavioral laws, such as "Talk when necessary" and "Wait for partner." These laws are explicitly incorporated into the agents' chains of thought via supervised fine-tuning, aligning their reasoning with task requirements and the behavior of other agents. To evaluate our approach, we introduce PARTNR-Dialog, a large-scale multi-agent communicative and cooperative planning benchmark built on the PARTNR environment. Experiments on existing tasks and our new benchmark demonstrate significant improvements in cooperative efficiency and task success rates. Across four backbone LLMs, our method achieves average success rate improvements of 4.5% on the PARTNR-Dialog benchmark and 6.8% on the TDW-MAT benchmark over state-of-the-art open-source communicative agent frameworks. See the LLawCo project page for details: https://www.merl.com/research/highlights/LLawCo

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28182v1) | [PDF](https://arxiv.org/pdf/2606.28182v1)

### [CPAgents: Agentic Composite Phenotype Generation for Cardiac Disease Association](http://arxiv.org/abs/2606.28179v1)

- **arXiv ID**: `2606.28179v1`
- **作者 / Authors**: Zuoou Li, Wenlong Zhao, Kelly Yu, Weitong Zhang, Paul M. Matthews et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.LG

<details>
<summary>📝 Abstract</summary>

Identifying robust associations between cardiac imaging phenotypes and clinical diseases is fundamental to population-scale cardiovascular research and reliable risk stratification. However, current phenome-wide association studies rely on pre-defined, single-variable phenotypes or expert-crafted features, which limits their ability to capture clinically meaningful non-linear effects and cross-phenotype interactions. To address this, we propose CPAgents, an iterative phenotype-Composition framework for cardiovascular Phenome-wide association study (PheWAS) that automatically constructs and validates interpretable composite phenotypes (e.g., polynomial, ratio, and interaction forms) from base imaging features. Specifically, our system coordinates three agents: (i) an Analyst that identifies statistical pathologies and nominates candidate transformations; (ii) a Proposer that generates constrained, medically and statistically motivated expressions under numerical safety rules; and (iii) a Verifier that evaluates candidates using multi-stage criteria and produces transparent evidence trails for accepted phenotypes. Evaluated on a population-scale cardiac imaging cohort, the discovered composite phenotypes markedly improve disease discrimination: across 72 classifier-disease-metric combinations, our variants achieve the top rank in 56 cases versus 18 for baselines, with gains observed across all nine clinical disease categories. Our framework yields compact, clinically interpretable phenotype formulas with transparent evidence trails, enabling scalable discovery of stronger phenotype-disease associations beyond expert-driven feature selection.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28179v1) | [PDF](https://arxiv.org/pdf/2606.28179v1)

### [AdvancedShelLM: A Stateful Multi-Agent LLM Honeypot for SSH Deception](http://arxiv.org/abs/2606.27990v1)

- **arXiv ID**: `2606.27990v1`
- **作者 / Authors**: Muris Sladić, Eman Alibalić, Veronica Valeros, Carlos Catania, Sebastian Garcia
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.CR

<details>
<summary>📝 Abstract</summary>

LLM-based SSH honeypots can generate believable interactions, but evaluations indicate they remain somewhat identifiable to determined attackers, indicating the need for a better scaffolding. We present a new LLM-based honeypot design that uses a multi-agent, multi-LLM architecture to address the limitations of the previous shelLM LLM honeypot. Our honeypot, called AdvancedShelLM, uses two LLM agents, a Manager and a Worker, that better understand the commands while reducing incorrect responses and increasing deception. It implements an advanced permanent filesystem, allowing many simultaneous attackers to see the same changing files for the first time. It was evaluated with: (i) unit tests for generative capabilities, (ii) an AI attacker (ARACNE) to assess realism and deception, (iii) human attackers to assess its deceptive capability, and (iv) an Internet deployment to evaluate deception in real-world attacks. In unit test results, AdvancedShelLM achieved a pass rate of up to 99.02%. The AI attacker ARACNE had issues making a decision if the system is honeypot or not, but showed slight bias towards saying honeypot, even for a real Ubuntu shell. With human attackers, AdvancedShelLM deceived more humans than Cowrie, but had similar results as shelLM. The Internet deployment showed concrete evidence that the output of AdvancedShelLM can influence the behaviour of real-life attackers.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.27990v1) | [PDF](https://arxiv.org/pdf/2606.27990v1)

### [Is Lying an Emergent Behaviour in LLMs? Evidence from Gaslighting AI agents in a Sustainability Game](http://arxiv.org/abs/2606.28456v1)

- **arXiv ID**: `2606.28456v1`
- **作者 / Authors**: Subhendu Bhandary, Federico Carucci, Christos Charalambous, Francesca Dilisante, Ksenia Dvorkina et al.
- **发布日期 / Published**: 2026-06-26
- **分类 / Category**: cs.MA

<details>
<summary>📝 Abstract</summary>

LLMs agents are increasingly used in multi-agent settings, yet their behaviour in sustainability games remains largely unexplored. This work investigates whether lying can emerge among LLM agents in a competitive sustainability game in which agents are informed that common resources can regenerate, although regeneration does not actually occur. We develop an agent-based model of a sustainability game in which agents manage industrial, military, and ecological resources, and interact through a network. LLM agents can observe neighbours' status, declare future attacks, receive permission to lie, and access reputation information, while rule-based agents provide an interpretable behavioural baseline. The results show that neighbour information strongly changes system dynamics, increasing attacks while improving biosphere retention and coexistence. Also, the presence of future declarations reduce extinction risk without suppressing conflict. Behaviourally, deception emerges even when agents are not explicitly allowed to lie, and explicit permission mainly increases bluffing and diversion rather than direct backstabbing. Finally, the presence of reputation memory and information about the current biosphere level reduces system ecological depletion. These findings suggest that deception can arise as an emergent behaviour in LLM-agent systems and that communication between LLM-agents could support sustainability while dealing with risk.

</details>

- **链接 / Links**: [Abstract](http://arxiv.org/abs/2606.28456v1) | [PDF](https://arxiv.org/pdf/2606.28456v1)

## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 1 |
| prompt-injection | 5 |
| memory-poisoning | 2 |
| tool-use-attack | 4 |
| backdoor | 5 |
| adversarial-attack | 3 |
| privacy-leakage | 10 |
| steganography | 2 |
| misuse | 3 |
| vulnerability | 31 |
| defense | 20 |
| alignment | 22 |
| agent-safety | 4 |
| benchmark | 1 |
| survey | 3 |
| other | 51 |

---

*Generated by AgentGuard at 2026-07-02 18:32:39*