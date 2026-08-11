<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-23092-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-11 06:57 ｜ **论文总数 / Total Papers**: 23092（近 30 天 / Recent 30 days: 2634）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 23092 篇论文（含摘要、分类筛选、搜索）/ View all 23092 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 571
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 484
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 108
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 409
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 554
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3796
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 869
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 113
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2615
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2322
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2159
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2126
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 263
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 86
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 57
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 277
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6132

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2634 篇，完整 23092 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2634 papers from the last 30 days (with date, authors & abstract). For the full list of 23092 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-08-10** — Alexander Panfilov, David Schmotz, Ilia Shumailov et al. — [Stealing Reasoning Traces from Proprietary LLM APIs](http://arxiv.org/abs/2608.09867v1)
  <details><summary>📄 Abstract</summary>
  Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request. Building on prior research, we identify an architectural vulnerability: these encrypted blocks are fully compatible and interchangeable across different ses...
  </details>

- **2026-08-10** — Hongli Shen, Shaopeng Fu, Qinbo Zhang et al. — [Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs](http://arxiv.org/abs/2608.09542v1)
  <details><summary>📄 Abstract</summary>
  Large reasoning models (LRMs) achieve remarkable success on complex tasks but remain vulnerable to harmful prompts that induce unsafe outputs. Recent methods align LRMs using direct refusals or safety rationales, yet often focus on prompt patterns rather than intrinsic attack mechanisms. As a result, these pattern-centric alignments struggle to generalize across diverse jailbreaks, compromising adversarial robustness and reasoning utility. We propose AdvSafe, a dual-adversarial framework that en...
  </details>

- **2026-08-09** — Yu Ma, Hongli Shi, Jing Li et al. — [When Skills Meet Safety: Benchmarking and Characterizing the Adaptive Jailbreak Robustness of Skill-Merged LLMs](http://arxiv.org/abs/2608.08542v1)
  <details><summary>📄 Abstract</summary>
  Model merging has become the default way to give an aligned language model new skills without retraining: a practitioner folds task vectors from math, code, or domain specialists into a safety-aligned base using task arithmetic, TIES, or DARE. This convenience is known to carry a safety cost, but almost all of that evidence rests on static refusal tests: fixed harmful prompts scored for compliance. We argue this is misleading. Because safety alignment is "shallow," concentrated in the first few ...
  </details>

- **2026-08-09** — Cong Ming, Jingyi Chen, Bin Liu et al. — [Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production](http://arxiv.org/abs/2608.08471v1)
  <details><summary>📄 Abstract</summary>
  Deployed LLM safety guardrails are predominantly static: trained once and frozen at release, while new jailbreak techniques and previously un-addressed harmful categories emerge within days, leaving the defense perpetually a step behind. We present SESG (Self-Evolving Safety Guardrails), a multi-agent system running in production. SESG monitors the live traffic behind a deployed guardrail and surfaces two classes of failure: jailbreaks novel in form and harmful categories novel in content. Once ...
  </details>

- **2026-08-07** — Elena Dumitrescu, Gert Lek, Lydia Y. Chen et al. — [Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits](http://arxiv.org/abs/2608.07430v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood. In this work, we investigate DLLMs both as targets and as adversaries, exposing mechanistic vulnerabilities in diffusion-based alignment.   We first show that safety alignment in DLLMs remains sparse and transferable across architectures. DLLMs initialized from autoregressive predecessors inherit the same mechanisti...
  </details>

- **2026-08-06** — Abdulkadir Külçe, Alihan Esen, Cağla Fikir et al. — [ECHO: A Locally-Deployable Agentic Health Assistant with Temporal Memory, Safety Guardrails, and Speech Assessment](http://arxiv.org/abs/2608.06110v1)
  <details><summary>📄 Abstract</summary>
  This paper presents ECHO (Enhanced Care \& Health Observer), a locally-deployable conversational health assistant for long-term chronic care management. ECHO integrates three complementary software modules developed under shared supervision as a unified system. The core module is an agentic chatbot built on a ReAct loop orchestrated via LangGraph, equipped with 17 clinical tools and a temporal knowledge graph for persistent cross-session memory; it achieves a 94.9\% tool-execution pass rate acro...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-08-09** — Lier Jin, Lan Hu, Binqi Shen et al. — [Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access](http://arxiv.org/abs/2608.08942v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly integrated into healthcare, education, public services, and everyday decision making. They should provide comparable assistance regardless of a user's literacy, communication style, or prompt-engineering expertise. However, existing research on prompt robustness primarily focuses on adversarial attacks, prompt injection, and prompt optimization, while overlooking whether semantically equivalent requests receive different responses simply because they...
  </details>

- **2026-08-09** — Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea et al. — [Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection](http://arxiv.org/abs/2608.08939v1)
  <details><summary>📄 Abstract</summary>
  The rise of autonomous AI agents represents a major paradigm shift in how users interact with mobile devices. Frameworks such as MobileRun and Mobile-Use can autonomously navigate Android applications and execute complex multi-step tasks. To interpret user interfaces, these frameworks rely primarily on Android accessibility (A11y) trees and secondarily on visual screenshots. In this paper, we demonstrate that this architectural dependence on unsanitized accessibility metadata, together with visu...
  </details>

- **2026-08-09** — Sihan Hou, Xinmeng Hou, Zhijun Zhang et al. — [Toward Metacognitive One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection](http://arxiv.org/abs/2608.08795v1)
  <details><summary>📄 Abstract</summary>
  Tool-using large language model (LLM) agents are vulnerable to indirect prompt injection (IPI), in which malicious instructions embedded in external observations manipulate subsequent agent decisions and actions. Most existing adaptive attacks rely on repeatedly querying and refining against the target agent, whereas realistic attackers may have only a single opportunity to interact with an unknown target agent. We propose SAVOR (Strategy Abstraction Via Outcome-Conditioned Reflection), which sh...
  </details>

- **2026-08-09** — Xinze Chen, Chi Zhang, Ping Ji et al. — [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](http://arxiv.org/abs/2608.08468v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills---structured packages of instructions and scripts that augment LLM-based agents---are rapidly proliferating, yet their security properties remain under-explored. We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores skill packages along pattern density, statistical anomaly, dataflow taint, import anomaly, and capability mismatch dimensions. We construct an adversarial evaluation dataset of 2{,}266 skills spanning 16~attack types across code-level, syst...
  </details>

- **2026-08-08** — Yuyang Luo, Haoran Wang, Kai Shu — [Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning](http://arxiv.org/abs/2608.08303v1)
  <details><summary>📄 Abstract</summary>
  Agentic skills improve large language model (LLM) agents by encoding reusable procedures for complex tasks. However, manually authored skills often adapt poorly to long-horizon tasks and changing environments. To address the limitation, self-evolving skill systems have been developed to automatically construct and update skills from execution trajectories, shifting skill acquisition from external marketplaces to a trusted evolution pipeline. By replacing external skill acquisition with trusted i...
  </details>

- **2026-08-08** — Kaysarul Anas Apurba, Md. Hasibul Hasan, Mahedee Zaman Moon et al. — [Defending Retrieval-Augmented Intrusion Detection Against Knowledge Poisoning and Prompt Injection](http://arxiv.org/abs/2608.08100v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) enables large language models to classify network flows and generate human-readable incident reports by retrieving semantically similar historical traffic from a vector knowledge base. However, the retrieval layer introduces vulnerabilities to knowledge poisoning and prompt-injection attacks. We present RAG-IDS, a three-tier multi-agent intrusion detection framework with a retrieval-boundary defense combining soft trust scoring, label-embedding consistency ch...
  </details>

- **2026-08-08** — Laiqiao Qin, Tianqing Zhu, Longxiang Gao et al. — [BASIS: Breach-Aware Selective Prompt Injection Shielding with Prefill Attention Probes](http://arxiv.org/abs/2608.08027v1)
  <details><summary>📄 Abstract</summary>
  Prompt injection is a critical security threat in large language model (LLM) applications, where attackers hijack model behavior by embedding malicious instructions in user or external data. Existing detection methods only detect the presence of injection and refuse to respond upon detection, overlooking the fact that for many modern aligned models, well-crafted instructions can resist most injection attacks. This means that the injection robustness varies significantly across instructions and m...
  </details>

- **2026-08-07** — Aditya Katkar, Om Karkele, Kartik Mandhane et al. — [NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs](http://arxiv.org/abs/2608.07167v1)
  <details><summary>📄 Abstract</summary>
  Giving an AI agent the ability to send emails, query databases, or execute commands is useful--until the agent is tricked into doing something it shouldn't. Prompt injection, hallucinated reasoning, and unsafe tool calls form the primary attack surface for autonomous LLM agents. Existing defenses rely on software checks like system prompts or policy filters running on the same machine the attacker targets, offering no verifiable proof of execution. We introduce Niyam-AI, a framework that makes s...
  </details>

- **2026-08-06** — S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana et al. — [Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots](http://arxiv.org/abs/2608.05715v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly deployed as planners in robotic systems, where they translate natural-language commands into executable actions grounded in visual scene understanding. This tight coupling between perception and instruction-following introduces a new attack surface: adversarial text placed within the robot's visual field can act as an indirect prompt injection into the VLM's reasoning stack. We present a systematic study of physical prompt injection attacks against ...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-08-07** — Yingtao Ren, Ziyi Zhao, Yiwei Fu et al. — [When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse](http://arxiv.org/abs/2608.06947v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs. Previous methods rely on output-side signals such as perplexity and consistency checks to detect such attacks. Nevertheless, our analysis reveals that deliberate attacks often induce false confidence, where poisoned outputs exhibit even lower perplexity than benign o...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 10 papers

- **2026-08-10** — Puyu Zeng, Simeng Qin, Jingzhi Li et al. — [ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners](http://arxiv.org/abs/2608.09732v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are emerging as an important attack surface in LLM-based agent systems. Through an empirical study of existing skill scanners, we find that current defenses mainly inspect individual skills, leaving risks from cross-skill composition insufficiently examined. This creates a practical blind spot: multiple locally plausible skills may pass security checks while collectively forming a harmful workflow during agent execution. To investigate this threat, we propose ColluSkill, a collusive...
  </details>

- **2026-08-10** — Hao Sui, Simeng Qin, Jie Liao et al. — [ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization](http://arxiv.org/abs/2608.09577v1)
  <details><summary>📄 Abstract</summary>
  Agent skills, bundles of instructions and resources that an LLM agent loads on demand, form an emerging supply chain where a single poisoned skill can persistently compromise every agent that installs it. However, existing skill attacks either fire on every request or rely on fine-tuned weights or multiple skills, leaving a conditional and low-cost backdoor unexplored. In this work, we present ElasticBack, an effective conditional single-skill backdoor that plants a rule R in the skill document ...
  </details>

- **2026-08-10** — Bohan Lin, Hejia Geng, Xinyi Xie et al. — [Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution](http://arxiv.org/abs/2608.09248v1)
  <details><summary>📄 Abstract</summary>
  Skill-based LLM agents select reusable procedures from an external library to solve complex tasks, yet their routing decisions rely entirely on text-level signals such as task descriptions, verbal reflections, and experience-derived rules, while the model's own internal representational state remains unobserved. Recent interpretability work has shown that LLMs maintain linear emotion representations that causally influence behavior; however, these representations have been exploited only for pos...
  </details>

- **2026-08-10** — XPolicyLab Community, Tianxing Chen, Yue Chen et al. — [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](http://arxiv.org/abs/2608.09892v1)
  <details><summary>📄 Abstract</summary>
  Robot policy evaluation and deployment remain fragmented by model-specific software dependencies, data representations, and runtime interfaces, so that connecting N policies to M evaluation environments requires O(NM) separate integrations. We present XPolicyLab, a unified standard and open ecosystem that reduces this cost to O(N+M). XPolicyLab specifies common observation, action, and trajectory schemas together with a minimal adapter interface for observation updates, action prediction, batche...
  </details>

- **2026-08-10** — Liang He, Jingbo Wen, Hongyu Gu et al. — [From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents](http://arxiv.org/abs/2608.09168v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are increasingly used to equip large language model (LLM) agents with reusable procedural knowledge. Although recent work has substantially improved skill retrieval due to the increasing skill libraries, retrieving a plausible skill bundle does not guarantee that executing it is worthwhile. Since every skill-conditioned rollout is computationally expensive, deciding whether a retrieved bundle should be executed has become an increasingly important challenge. To this end, we introduc...
  </details>

- **2026-08-09** — Chi Zhang, Yimin Liu, Xinze Chen et al. — [What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files](http://arxiv.org/abs/2608.08453v1)
  <details><summary>📄 Abstract</summary>
  Under the current standard, Agent Skills are SKILL.md files that combine instructions with supporting resources, enabling Large Language Model (LLM) agents to reuse procedures beyond a single conversation. Yet many public skills appear to originate from a single task, repository, or conversation, even when they are shared as reusable components. We analyze this gap across 138,133 public SKILL.md files from 20,556 repositories using a two-tier defect taxonomy grounded in the official specificatio...
  </details>

- **2026-08-09** — Donghong Jiang, Endian Lin, Luoping Cui et al. — [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](http://arxiv.org/abs/2608.08640v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly rely on reusable skills to extend their capabilities beyond parametric knowl- edge. However, retrieving the appropriate skill from a large- scale library remains challenging because realistic user re- quests are often concise and underspecified, stating only the task goal while leaving the required capabilities and execu- tion steps implicit. Existing benchmarks provide limited cov- erage of such requests. To address this gap, we introduce SkillReason-Ben...
  </details>

- **2026-08-07** — Jiahui Han, Qinuo Li, Ziheng Peng et al. — [SkillEval: Decomposing Agent Skill Quality into Interpretable Signals](http://arxiv.org/abs/2608.06891v1)
  <details><summary>📄 Abstract</summary>
  Agent skills provide reusable procedural knowledge that helps agents solve specialized tasks. As their use expands, evaluating skill quality becomes increasingly important. Existing evaluations often measure skill quality by testing whether a skill improves performance on specific downstream tasks. However, a reusable skill may apply to multiple task scenarios. Downstream evaluation mainly reflects the compatibility between a skill and the evaluated task, provides only a partial view of skill qu...
  </details>

- **2026-08-06** — Yuru Feng, Yaoqi Chen, Beidi Zhao et al. — [SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation](http://arxiv.org/abs/2608.05628v1)
  <details><summary>📄 Abstract</summary>
  Although agent skills equip LLMs with reusable procedural knowledge, manual maintenance suffers from high costs, unscalability, and misalignment. Real-world deployments thus require autonomous, on-demand skill evolution at test time, constrained by limited interaction budgets and a lack of training or validation sets. This setting introduces a severe sparse reward challenge, where outcomes conflate multiple latent failure causes. Under such ambiguity, existing methods that greedily refine a sing...
  </details>

- **2026-08-06** — Jialuo Chen, Lingqi Jiang, Xinhao Deng et al. — [When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems](http://arxiv.org/abs/2608.05563v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving skill (SES) systems distill agent trajectories into persistent skills, allowing untrusted experience to become trusted instruction. We introduce PoisonedEvolution, a trajectory-poisoning attack on this promotion process. Our skill-visible black-box attacker can inspect a target skill and contribute bounded evidence, but cannot observe private pools or evolution logic or edit the skill bank. Artifact poisoning requires Inclusion, Evolution Attribution, and Realization. Attribution i...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 2 papers

- **2026-08-10** — Yunhao Liang, Chengguang Gan, Ruixuan Ying — [Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits](http://arxiv.org/abs/2608.09740v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate functionally useful code that remains vulnerable, while security-focused interventions may break intended behavior. We investigate security tests as executable specifications both before generation and during iterative repair. We develop SecTDD, a controlled test-feedback scaffold that separates three factors: whether tests are shown upfront, whether failed executions trigger revision, and how failures are selected and represented. The evaluation uses be...
  </details>

- **2026-08-06** — Yuchen Chen, Wei Cheng, Yuan Xiao et al. — [Breaking Customized LLMs for Coding: Automated Red Teaming for Instruction Backdoor Attacks](http://arxiv.org/abs/2608.05659v1)
  <details><summary>📄 Abstract</summary>
  LLM customization platforms allow users to build task-specific models for code intelligence tasks by embedding instructions into system prompts, without modifying the underlying model parameters. While these platforms lower the barrier to developing customized LLMs, they also introduce a new attack surface: instruction backdoor attacks, in which adversaries implant hidden malicious behaviors into customized instructions. However, existing attacks suffer from two key limitations. First, they ofte...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-08-10** — Rohan Bhagra, Mahantesh Halapannavar, Uddhav Bhattarai — [Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy](http://arxiv.org/abs/2608.09857v1)
  <details><summary>📄 Abstract</summary>
  Advances in advanced artificial intelligence tools have sparked research in robot autonomy, but the development of such systems has largely focused on execution rather than verifying the feasibility actions planning models propose. Like general-purpose LLMs, robotics planning models carry risks: biased toward user-specified goals, they may suggest actions misaligned with scientific ethics, they may be unsafe due to an inability to "remember" prior safety risks, or they may be vulnerable to adver...
  </details>

- **2026-08-10** — Kevin Thomas, Milosz Kasprzyk, Reuel C Igbokwe Onuigbo et al. — [Build it, Break it, Repeat: Benchmarking and improving LLM-manipulated disinformation detection in social media posts](http://arxiv.org/abs/2608.09510v1)
  <details><summary>📄 Abstract</summary>
  Detecting machine-generated disinformation on social media is increasingly difficult as large language models (LLMs) make it easier to generate and rewrite misleading content at scale. Static benchmark evaluations, measuring detector performance on fixed held-out datasets, do not capture how detectors behave when posts are deliberately transformed to evade classification. This paper adapts the Build it, Break it, Fix it framework into Build it, Break it, Repeat (BiBiR): iterative sessions design...
  </details>

- **2026-08-09** — Yi Pan, Jun-Jie Huang, Tianrui Liu et al. — [IDATA: Scalable Invertible Diffusion for Unrestricted Adversarial Transfer Attack](http://arxiv.org/abs/2608.08734v1)
  <details><summary>📄 Abstract</summary>
  Unrestricted adversarial transfer attacks are important for evaluating the black-box robustness of deep visual models. Diffusion-based attacks have shown promising transferability and visual imperceptibility by optimizing adversarial perturbations along denoising trajectories in latent space. However, existing methods are limited by two challenges: memory-intensive multistep backpropagation and frequency-agnostic perturbation over intermediate latents. To address these issues, we propose IDATA, ...
  </details>

- **2026-08-09** — Parham Sazdar, Mostafa Tavassolipour, Reshad Hosseini — [Domain-Aware Pruning: Sparsity and Domain Generalization via Regularized Probabilistic Masking](http://arxiv.org/abs/2608.08624v1)
  <details><summary>📄 Abstract</summary>
  Domain generalization (DG) and neural network pruning are conventionally treated as distinct objectives, targeting out-of-distribution (OOD) robustness and model efficiency, respectively. In this work, we bridge this gap by introducing Domain-Aware Pruning (DAP), a framework that leverages network sparsity as a mechanism to implicitly enhance generalization to unseen domains. Diverging from standard binary mask optimization, DAP learns a continuous parameter retention probability $p \in [0, 1]$,...
  </details>

- **2026-08-08** — Nuthakki Siva Gopala Krishna, Kanishka Jain — [STEMMA: An Adversarial Multi-Agent Framework for Evaluating Self-Identity Consistency in LLMs](http://arxiv.org/abs/2608.08164v1)
  <details><summary>📄 Abstract</summary>
  Knowledge Distillation is a widely adopted technique in the training and fine-tuning of large language models (LLMs) enabling transfer of structured information and functional behavior from a large teacher model to a smaller student model while significantly reducing computational costs. However, as the use of distillation increases in both scale and complexity it raises an important question about what kind of knowledge is really transferred from the teacher model. In this work, we argue that a...
  </details>

- **2026-08-06** — Hao Wang, Yuxuan Zhang, Wei Yang — [Universal Concept Disruption for SAM3 Image Segmentation](http://arxiv.org/abs/2608.05983v1)
  <details><summary>📄 Abstract</summary>
  SAM3 extends promptable segmentation from geometry-driven mask prediction to open-vocabulary concept segmentation, where a text-conditioned grounding model decides whether a concept is present and segments all matching instances. While this presence-gated design improves concept-level prediction, its adversarial robustness remains unexplored. In this paper, we introduce Universal Concept Disruption (UCD), the first universal cross-concept adversarial attack tailored to SAM3 image segmentation. U...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 25 papers

- **2026-08-10** — Tejasvi C. Addagada — [Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference](http://arxiv.org/abs/2608.09225v1)
  <details><summary>📄 Abstract</summary>
  The key-value (KV) cache is the primary throughput optimization in modern large language model (LLM) inference, enabling prefix reuse across requests. In multi-tenant deployments this cache is shared across tenants, creating a timing side channel: an adversarial tenant can reconstruct another tenant's private prompt by probing cache-hit latency. Three published attacks exploit it -- PROMPTPEEK, EarlyBird and InputSnatch -- reaching up to 100% attack success rate against unprotected vLLM and SGLa...
  </details>

- **2026-08-10** — Tianhong Xu, Saion K. Roy, Ruyi Ding et al. — [SLAC: Access-Driven CPU-to-GPU Side-channel Attacks via System-Level Cache on Apple Silicon](http://arxiv.org/abs/2608.09075v1)
  <details><summary>📄 Abstract</summary>
  Modern heterogeneous System-on-Chip designs integrate CPU cores and a GPU that share a last-level cache (LLC) or system-level cache (SLC). This sharing exposes a new cross-domain attack surface, and existing attacks on integrated platforms either exploit coarse-grained cache-occupancy contention or require the adversary to co-reside on the GPU with the victim to obtain accurate timing measurements. In this work, we target Apple Silicon heterogeneous SoCs and discover that GPU memory accesses lea...
  </details>

- **2026-08-10** — Shengcheng Yu, Yuchen Ling, Junyang Xing et al. — [Software Engineering for and with GUI Agent](http://arxiv.org/abs/2608.09278v1)
  <details><summary>📄 Abstract</summary>
  GUI agents have advanced rapidly, producing a growing body of frameworks, benchmarks, and applications. However, this growth has outpaced the maturity of the field. GUI agents remain technically brittle, incompletely engineered, and insufficiently validated for sustained real-world use. They are evolving into closed-loop software systems. Within these systems, model reasoning is coupled with interface perception, execution feedback, recovery, and human oversight. This evolution calls for a softw...
  </details>

- **2026-08-10** — Bingcan Guo, Eryue Xu, Jijie Zhou et al. — [CIDER: A Dataset of Contextual Disclosure Boundaries for Privacy Preference Alignment](http://arxiv.org/abs/2608.09164v1)
  <details><summary>📄 Abstract</summary>
  Aligning large language models (LLMs) with human privacy preferences requires capturing individuals' disclosure boundaries beyond general privacy norms. However, a gap remains in eliciting such nuanced preferences to evaluate alignment in realistic settings. We introduce CIDER, a dataset of 14,850 human annotations from 169 users, forming 1,650 contextual disclosure boundary sets across 60 interpersonal communication scenarios involving information sharing that violates privacy norms. Each bound...
  </details>

- **2026-08-10** — Moghis Fereidouni, Vinaik Chhetri, Umar Farooq et al. — [Security and Privacy Taxonomy Generation from Mobile App Reviews](http://arxiv.org/abs/2608.09049v1)
  <details><summary>📄 Abstract</summary>
  Mobile app reviews are a rich, continuously renewing source of how users experience privacy and security, yet existing taxonomies of these concerns are hand-crafted and cannot keep pace with the evolving nature of the data. Automating taxonomy construction is the natural response, but scalability is the core challenge: current LLM- and clustering-based methods are developed for scientific corpora of a few thousand documents and do not extend to app review collections numbering in the hundreds of...
  </details>

- **2026-08-10** — Jiaheng Su, Yu Sun — [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](http://arxiv.org/abs/2608.08976v1)
  <details><summary>📄 Abstract</summary>
  Parkinson's disease (PD) is the second most common neurodegenerative disorder. Typical machine learning screening methods require PD labels, but the available data is limited by privacy concerns and the need for expert annotation. We propose a label-free face-plus-voice PD screen built entirely on frozen pretrained encoders--a face-expression Vision Transformer and HuBERT--in which no PD label touches any fit; the reference is training controls only. The voice modality uses a synthetic-dysarthri...
  </details>

- **2026-08-10** — Jaeheon Kim, Hokeun Kim, Bong Jun Choi — [Label Granularity Skew in Federated Learning with Hierarchical Image Classification](http://arxiv.org/abs/2608.09236v1)
  <details><summary>📄 Abstract</summary>
  Federated learning enables privacy-preserving collaboration across distributed devices without centralizing local data. However, clients may differ not only in data distributions but also in domain knowledge and annotation capabilities. In this paper, we introduce label granularity skew, a new form of statistical heterogeneity in federated hierarchical classification, in which clients provide taxonomy-consistent labels at different levels of detail within a shared class hierarchy. To model this ...
  </details>

- **2026-08-10** — Li Siyan, Zhou Yu, Julia Hirschberg — [Beyond Direct Identifiers: Probabilistic Privacy Risk Estimation for Privacy-Conscious LLM Query Delegation](http://arxiv.org/abs/2608.09140v1)
  <details><summary>📄 Abstract</summary>
  Recent work on protecting privacy during user-LLM interactions often focuses on direct, explicit identifiers: the personally-identifiable information (PII) captured by standard detectors. One such approach is Privacy-Conscious Delegation (PCD), where a local LLM acts as an intermediary. However, privacy risk does not stem solely from explicit identifiers but also PII-free self-disclosures, leaving users identifiable through combinations of quasi-identifying traits. We investigate a probabilistic...
  </details>

- **2026-08-10** — Wu Hangyu — [How Far Do Foundation Models Transfer to Infant Signals? A Cross-Dataset Transfer Audit with a Unified Need Ontology](http://arxiv.org/abs/2608.08989v1)
  <details><summary>📄 Abstract</summary>
  Public infant cry corpora are small, label-incompatible, and almost always evaluated one corpus at a time. We ask what this practice hides and what fixes it. Across four cry corpora screened by a multi-level leakage audit (byte-level and embedding-level deduplication plus a within-corpus train-test near-duplicate audit), we probe four frozen encoders and a handcrafted baseline under a unified five-class need ontology and shared task formulations. The audit exposes what single-corpus evaluation c...
  </details>

- **2026-08-09** — Víctor Gallego — [Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under Selection Pressure](http://arxiv.org/abs/2608.08722v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks for systems that are optimized against the evaluation signal measure something different from what they claim. We document this concretely in two GPU-kernel-optimization suites with held-out generalization gates: Metal-Sci (10 scientific-compute tasks) and Metal-ZK (12 zero-knowledge/cryptographic tasks), in which three frontier LLMs (Opus 4.7, Gemini 3.1 Pro, GPT-5.5) propose Metal kernels inside a $(1{+}1)$ evolutionary loop with rich feedback. Although no model is prompted to act a...
  </details>

- **2026-08-09** — Joseph Bingham — [A Dynamic-Semantics Framework for Grounding Human Referring Expressions in Visual Perceptual Data](http://arxiv.org/abs/2608.08663v1)
  <details><summary>📄 Abstract</summary>
  Humans converge on shared names for novel, hard-to-describe objects through repeated interaction, a process psycholinguists call lexical entrainment. Leading vision-language models fail at this: recent empirical work documents that they do not shorten references, reuse successful expressions, or maintain stable pact state across turns. We present a framework that addresses the gap by externalizing pact state into three explicit, inspectable sets of referent-object bindings ($Γ, Ξ, Ω$), updated b...
  </details>

- **2026-08-09** — Jack Stark, Srinath Saikrishnan, Vikram Seenivasan et al. — [AquiLLM: An Architecture for Supporting Tacit Knowledge Capture in Research Groups](http://arxiv.org/abs/2608.08883v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in retrieval-augmented generation (RAG) and large language models (LLMs) enable researchers to integrate AI into scientific workflows. However, using proprietary commercial AI systems raises concerns about transparency, reproducibility and privacy, which are essential for scientific practices. To this end, AquiLLM was developed as an open-source modular RAG-LLM framework using open-weight models, designed to support research groups in capturing tacit knowledge. In this work, we p...
  </details>

- **2026-08-09** — Navid Hasanzadeh, Shahrokh Valaee — [DoRF++: Spherical Representation Learning over Doppler Radiance Fields for Robust Wi-Fi Sensing](http://arxiv.org/abs/2608.08381v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the IEEE 802.11bf effort to standardize advanced WLAN sensing, interest in Wi-Fi Channel State Information (CSI) for passive, device-free, and privacy-preserving activity and gesture recognition has grown rapidly. Recent studies have shown that Doppler velocity projections extracted from CSI, which directly reflect human-motion velocity, enable more robust human activity recognition (HAR) and stronger generalization across users and unseen conditions. Nevertheless, reliable generali...
  </details>

- **2026-08-08** — Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj — [SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents](http://arxiv.org/abs/2608.08253v1)
  <details><summary>📄 Abstract</summary>
  AI agents are becoming shared infrastructure, yet durable memory is commonly assembled from separate retrieval, governance, and operational components. We present SuperLocalMemory 4.0, a governed, local-first memory operating system for AI agents. The system combines dense semantic, BM25 lexical, temporal, Hopfield-associative, and spreading-activation retrieval through reciprocal-rank fusion; a governed learning and behaviour layer; bi-temporal recall; multi-scope personal, shared, and global m...
  </details>

- **2026-08-08** — Michael Levit, Josh Ledgard, Haoyu Dong et al. — [Privacy-Preserving Data Drift Detection and Recovery for Large-Scale LLM Applications via Proxy Representations](http://arxiv.org/abs/2608.08245v1)
  <details><summary>📄 Abstract</summary>
  LLM applications deployed at scale face a fundamental challenge: privacy constraints prevent direct inspection of user interactions, making it difficult to obtain any representative evaluation dataset or to track the ongoing evolution of production traffic. We present ProxyDrift, a framework that (i) identifies and measures drift between production traffic and offline evaluation sets, and (ii) constructs and refreshes those evaluation sets accordingly; all without access to raw user data. Our ap...
  </details>

- **2026-08-08** — Matteo Caligiuri, Francesco Barbato, Pietro Zanuttigh et al. — [EFFEKT: Efficient Federated Knowledge Transfer to Foundation Models](http://arxiv.org/abs/2608.08138v1)
  <details><summary>📄 Abstract</summary>
  Recent data protection laws have accelerated the adoption of Federated Learning (FL) for privacy-preserving decentralized training. Nevertheless, increasing model sizes impose substantial computational demands on client devices, limiting FL applicability in resource-constrained settings. We introduce a novel multi-domain federated learning framework in which lightweight client-side proxy models collaborate with a server-side Foundation Model (FM) to learn new concepts without sharing private dat...
  </details>

- **2026-08-08** — Hakeem Hannoon, Andrew Zhao, Mihir Narayan et al. — [Mitigating Over-Personalization in LLMs via Structured Memory](http://arxiv.org/abs/2608.08300v1)
  <details><summary>📄 Abstract</summary>
  Conversational assistants increasingly rely on persistent long-term memory to personalize responses across sessions. However, when stored user information is reintroduced into the model context, it can also influence responses in inappropriate or unrelated settings. We study two such failure modes in memory-augmented LLMs: cross-domain leakage, where memories from one life domain affect responses in another, and memory-induced sycophancy, where stored user beliefs make models more likely to agre...
  </details>

- **2026-08-08** — Wentao Dai, Xuanran Li, Yuxiang Zhang et al. — [ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling](http://arxiv.org/abs/2608.07974v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) fine-tuning at the edge adapts the model to scenario-specific data while preserving privacy. Although existing studies proposed pipeline parallelism to address the limited memory and computing resources of edge devices, they commonly rely on backpropagation (BP) training, which has a fundamental limitation of update locking and could experience severe throughput and memory bottlenecks. In this work, we propose a BP-free algorithm, called ZeroLock, that decouples the mo...
  </details>

- **2026-08-07** — Minami Yoda, Jialong Li, Yasuyuki Tahara et al. — [Statistical Analysis of Executability and Program Equivalence in Decompilation for IoT Vulnerability Detection](http://arxiv.org/abs/2608.06960v1)
  <details><summary>📄 Abstract</summary>
  Internet of Things (IoT) devices handle sensitive privacy-related information such as user audio, video, and authentication data, making it essential to detect vulnerabilities in their firmware. Decompilation, a key detection technique, has recently attracted attention because Large Language Models (LLMs) enable high readability and high recompilation success rates. However, because LLM outputs depend on probabilistic token prediction, they tend to prioritize syntactic correctness and may genera...
  </details>

- **2026-08-07** — Xin Wang, Yingchao Huang, Yuhan Su et al. — [LSEAD: A Privacy-Preserving LLM-Based Speech Analysis Framework for Early Alzheimer's Disease Screening](http://arxiv.org/abs/2608.07378v1)
  <details><summary>📄 Abstract</summary>
  Early diagnosis of Alzheimer's disease (AD) is critical for enabling timely interventions that may slow disease progression and improve patient outcomes. There is a growing need for AD detection methods that are non-invasive and cost-effective, especially in real-world clinical settings with diverse patient populations and recording conditions. Speech-based screening addresses these needs by using natural speech collected without specialized equipment. Recent advances in large language models (L...
  </details>

- **2026-08-06** — Zirui Chen, Shi Tang, Zhengchao Gao et al. — [Algebraic Cryptanalytic Extraction on Hard-Label Neural Networks](http://arxiv.org/abs/2608.05736v1)
  <details><summary>📄 Abstract</summary>
  Although the state-of-the-art neural network model extraction attack in the hard-label setting by Carlini et al. at EUROCRYPT 2025 has polynomial-time complexity in theory, its dual-point clustering relies on singular value decomposition (SVD) with a time complexity of $\mathcal{O}(n^2 \cdot (d^{(k)})^3)$, resulting in huge runtime in practice. To address this computational bottleneck, this work transforms Carlini et al.'s geometric-view hard-label attack into an algebraic framework, and propose...
  </details>

- **2026-08-06** — Omid Bazgir, Md Nasir, Jacob Hoffman et al. — [Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints](http://arxiv.org/abs/2608.06265v1)
  <details><summary>📄 Abstract</summary>
  Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice.   We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility ...
  </details>

- **2026-08-06** — Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda — [From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems](http://arxiv.org/abs/2608.06112v1)
  <details><summary>📄 Abstract</summary>
  Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research pr...
  </details>

- **2026-08-06** — Kai Li, Conggai Li, Sarah Ali Siddiqui et al. — [When Agentic AI Meets Integrated Sensing and Communication](http://arxiv.org/abs/2608.05792v1)
  <details><summary>📄 Abstract</summary>
  Agentic artificial intelligence (AI) is transforming Integrated Sensing and Communication (ISAC) from a function-oriented physical-layer technology into a goal-driven, closed-loop intelligent system, a paradigm we term AISAC. Existing work on learning-based sensing, resource allocation, reconfigurable intelligent surfaces (RIS), edge intelligence, multi-agent coordination, and resilient networking has developed largely in isolation. This survey unifies the literature within a six-stage closed-lo...
  </details>

- **2026-08-06** — Jiarui Yang, Jiale Zhange, Jiawei Li et al. — [LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models](http://arxiv.org/abs/2608.05706v1)
  <details><summary>📄 Abstract</summary>
  World models enable agents to perform forward rollout and planning without real-world interaction. However, their application in open-world embodied intelligence remains limited by the high cost of action annotations and the heterogeneity of action spaces across platforms. Recently, latent action models (LAMs) have alleviated this bottleneck by learning action representations directly from unlabeled human videos in a self-supervised manner. Nevertheless, most existing LAMs rely on single-view in...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 13 papers

- **2026-08-10** — Bocheng Chen, Han Zi, Roucheng Ou et al. — [Pragmatic Attack Surface: Vulnerabilities of Implicit Context in Large Language Models](http://arxiv.org/abs/2608.09551v1)
  <details><summary>📄 Abstract</summary>
  In the era of large language models (LLMs), attackers often manipulate natural language to elicit unsafe or harmful outputs, creating a new natural language attack surface unique to LLM-based systems, where attacks directly exploit explicit linguistic cues in user prompts to bypass the safety mechanism of LLMs. However, such attacks can often be mitigated by existing safety alignment algorithms. On the other hand, human language is inherently grounded in pragmatics, necessitating typical context...
  </details>

- **2026-08-10** — Neel Tushar Shah, Manglam Kartik, Akshat Karkar — [Capability Is Not Propensity: Measuring Pressure-Robust Cooperative Behavior in Civic LLM Agents](http://arxiv.org/abs/2608.09485v1)
  <details><summary>📄 Abstract</summary>
  Cooperative capabilities in language models are dual-use. The same social reasoning that supports civic deliberation can also enable strategic omission, false consensus, and manipulative framing. We argue that Cooperative AI evaluations should separate what models can do under benign instructions from what they tend to do under realistic civic pressure. We introduce DiffCoop-Civic, a 10-scenario pilot evaluation suite spanning preference understanding, evidence and persuasion, commitment design,...
  </details>

- **2026-08-10** — Shuyi Miao, Wangjie Qiu, Pengyang Shao et al. — [Who Bridges Safety? Identifying and Targeting Cross-Lingual Shared Safety Pathways](http://arxiv.org/abs/2608.09095v1)
  <details><summary>📄 Abstract</summary>
  Uncovering the internal mechanisms underlying the safety capabilities of large language models (LLMs) is crucial for developing trustworthy artificial intelligence. Currently, mechanistic interpretability studies on multilingual safety are largely confined to local components, such as isolated neurons. However, this static and fragmented perspective overlooks the synergy among components and fails to elucidate how safety signals dynamically propagate within the model to drive safety decisions ul...
  </details>

- **2026-08-10** — Maryam Tahermazandarani, Adnan Mahmood, Fahmida Islam et al. — [When Confidence Fails: Overconfidence in LLMs under Uncertainty and Missing Clinical Information](http://arxiv.org/abs/2608.09080v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved strong performance in medical question answering and clinical reasoning tasks. However, their reliability under uncertainty remains poorly understood which raises critical concerns for deployment in high-stakes clinical settings. In such environments, incorrect predictions are inherently risky, but confident incorrect predictions can be particularly harmful as they may mislead clinical decision-making. In this paper, we conduct a systematic behavioral a...
  </details>

- **2026-08-09** — Jiaxin Guo, Yanwei Yue, Xuanbo Fan et al. — [Learning from Consensus and Disagreement: Unsupervised On-Policy Self-Distillation with Minority-Trajectory Contrast](http://arxiv.org/abs/2608.08764v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation improves language-model reasoning by querying a teacher on states actually visited by the student. Recent methods create a powerful information asymmetry by exposing the teacher to privileged context, yet they fundamentally rely on external supervision---such as gold solutions or verifiers---to construct this advantage. We introduce CoDA (Consensus and Disagreement Alignment), a fully unsupervised framework that creates reliable privileged information entirely from th...
  </details>

- **2026-08-09** — Yuxiao Li, Gjergji Kasneci — [Safety Cost of Steering Vectors Is Separable and Reducible](http://arxiv.org/abs/2608.08383v1)
  <details><summary>📄 Abstract</summary>
  Steering vectors are a lightweight tool for controlling LLM behavior. However, emerging evidence shows that steering vectors can unintentionally compromise a model's safety mechanisms and increase compliance with harmful requests, while no effective mitigation yet exists. In this work, we show that this safety degradation arises from a separable component in the vector that disrupts the model's safety mechanisms but contributes little to the steering objective. We identify and remove this safety...
  </details>

- **2026-08-09** — Tak Ho Alex Li, Kaijie Liu, Lik-Hang Lee et al. — [HoloAegis: Frozen Representation, Topological Inference: Minimally Parametric Safety Manifolds for Zero-Shot LLM Guardrails](http://arxiv.org/abs/2608.08485v1)
  <details><summary>📄 Abstract</summary>
  Current LLM safety guardrails face a fundamental tension: fine-tuning distorts pre-trained representations while generative judges incur prohibitive inference costs. We challenge the prevailing paradigm by asking: can safety be achieved through pure geometric reasoning over frozen semantic representations? We present HoloAegis, a minimally parametric topological inference framework that decouples representation from reasoning. We term our approach minimally parametric because the only free param...
  </details>

- **2026-08-09** — Sourav Das, Tanmay Joshi, Kripabandhu Ghosh — [Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs](http://arxiv.org/abs/2608.08744v1)
  <details><summary>📄 Abstract</summary>
  The carbon footprint of any deployed Large Language Model (LLM) accumulates during inference, where repeated use of the model substantially exceeds the one-time cost of fine-tuning. Yet most efficiency interventions target either pre-training scale or post-hoc compression. We ask whether folding a calibrated, differentiable energy surrogate into the fine-tuning objective can produce inference behavior that gains task accuracy at zero or near-zero carbon cost, a break-even configuration. We propo...
  </details>

- **2026-08-08** — Fan Zhou, Weitian Wang, Tim Van de Cruys — [Commitment Before Realization: When Classifier-Free Guidance Becomes Unnecessary in Masked Diffusion Language Models](http://arxiv.org/abs/2608.08082v1)
  <details><summary>📄 Abstract</summary>
  Classifier-free guidance (CFG) is usually kept on throughout masked diffusion language model decoding, although its benefit varies across prompts and over time. We study when CFG is actually needed by comparing, from any partial output, the probability of eventual constraint satisfaction under continued CFG and under base-only continuation. Their difference defines the remaining value of guidance. Guidance dependence is highly prompt-specific. Many prompts already succeed without CFG, while for ...
  </details>

- **2026-08-07** — Wenzhang Sun, Chunfeng Wang, Xiangchen Yin et al. — [Stable Curves, Unstable Items: Item-Level Scaling Heterogeneity in Video LLMs](http://arxiv.org/abs/2608.07014v1)
  <details><summary>📄 Abstract</summary>
  Aggregate scaling curves suggest that Video LLMs improve smoothly or saturate as visual budgets grow. We show that this view can conceal large, opposing changes at the item level. We represent each frozen model--item pair by its response trajectory under controlled visual budgets and derive matched-grid measures of configuration complementarity, harmful transitions, and text overwrite. Across five open Video LLMs from three architecture families, four multiple-choice benchmark splits, open-ended...
  </details>

- **2026-08-07** — Jiankun Wang, Yisen Gao, Ziwei Zhang et al. — [Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?](http://arxiv.org/abs/2608.07006v1)
  <details><summary>📄 Abstract</summary>
  Visual retrieval-augmented generation (RAG) commonly expands the retrieved evidence set to improve answer-page coverage, implicitly assuming that all available evidence should be passed to the generator. We show that this assumption does not hold for diffusion language models (DLMs): retrieving more pages increases answer-page recall, whereas unconditionally passing all retrieved pages to the generator often reduces answer accuracy, primarily because of semantic conflict. A latent-source analysi...
  </details>

- **2026-08-06** — Hongrui Bao, Yubing Ren, Yanan Cao et al. — [Once a Response, Always a Response: Detecting LLM-generated Text via Latent Prompt Restoration](http://arxiv.org/abs/2608.05741v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate fluent and convincing text at scale, creating growing risks for misinformation dissemination, educational misuse, and platform governance. These concerns make robust detection of machine-generated text increasingly necessary. Recent zero-shot detectors mainly exploit probability-based statistical discrepancies, but they do not explicitly account for the training process of LLMs, which leaves a distinct generation mechanism insufficiently modeled and limi...
  </details>

- **2026-08-06** — Shenyi Zhang, Keyan Guo, Zihao Wang et al. — [MMAligner: Safeguarding Multimodal Large Language Models through Representation Calibration](http://arxiv.org/abs/2608.05909v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) often refuse unsafe text prompts yet generate harmful responses to semantically equivalent multimodal inputs. Existing defenses either rely on external guardrails, which add inference overhead without repairing intrinsic flaws, or safety fine-tuning, which treats alignment as black-box optimization and may sacrifice utility or require large multimodal datasets. To identify the cause of this safety disparity, we analyze MLLM representations geometrically. ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-08-10** — Yuanhe Zhang, Weiliu Wang, Jie Ren et al. — [From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs](http://arxiv.org/abs/2608.09158v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) have demonstrated strong capabilities in understanding diverse audio inputs. This diversity includes low-frequency signals that are inaudible to humans but can still enter the model and influence its generation. However, the practical impact of such low-frequency inputs on LALMs remains largely unexplored. In this paper, we propose Intermittent Low-Frequency Lockout (ILL), an inaudible red teaming method that evaluates this risk using a universal waveform temp...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 40 papers

- **2026-08-10** — Zichao Yu, Chengzhi Yu, Shengze Xu et al. — [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](http://arxiv.org/abs/2608.09836v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has emerged as a core component of modern LLM post-training pipelines, yet we reveal a failure mode: degenerate agreement, where students exploit repetitive loops to achieve near-perfect token agreement with the teacher despite globally flawed responses. We therefore shift our focus from agreement to teacher-student mismatch, and find that mismatch tokens can be mainly categorized into two types: student-excess tokens and student-deficit tokens. Student-excess tokens...
  </details>

- **2026-08-10** — Changhao Li, Yifang Zhang, Heng Zhang et al. — [Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition](http://arxiv.org/abs/2608.09762v1)
  <details><summary>📄 Abstract</summary>
  Real-world online reinforcement learning (RL) provides a promising approach for training robotic manipulation policies directly in the physical world, avoiding the sim-to-real gap and enabling continuous policy refinement through human-in-the-loop interaction. Recent methods have demonstrated sample-efficient learning through human intervention but remain limited to small randomization ranges and encounter challenges with the non-stationarity induced by concurrently training multiple agents. To ...
  </details>

- **2026-08-10** — Ivan Wiryadi — [Activation Probes Surface Code-Security Signals that the Model's Output Misses](http://arxiv.org/abs/2608.09643v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now write a growing share of production code, and human security review does not scale at the rate code is generated. The agents in widest use are closed-weight, so a deploying team cannot read their internals. It can instead run an open-weight model as a reviewer over the agent's output. That reviewer's activations are readable. We ask whether reading those activations recovers a security signal that simply asking the same reviewer misses. We fit a single linear probe per model...
  </details>

- **2026-08-10** — Bo Chen — [From Runnable to Verifiable: An Independent Reproducibility Study of LLM/Agent-Driven Vulnerability Validation Artifacts](http://arxiv.org/abs/2608.09567v1)
  <details><summary>📄 Abstract</summary>
  Security research artifacts---repositories, PoC exploits, and validation pipelines---are increasingly produced by LLM/agent-driven vulnerability workflows, yet the gap between \emph{publicly available}, \emph{runnable}, \emph{signal-producing}, and \emph{semantically confirmed} artifacts is poorly measured. We conduct a pre-registered reproducibility audit of this literature. A search covering 2023--2026 with dual screening yields a 104-paper consensus corpus, of which 59 papers (56.7\%) have a ...
  </details>

- **2026-08-10** — Zeyuan Ma, Jiaxin Chen, Di Huang — [From Semantic Grounding to Decision Optimization: A Unified Framework for Long-Horizon UAV Vision-Language Navigation](http://arxiv.org/abs/2608.09564v1)
  <details><summary>📄 Abstract</summary>
  UAV vision-language navigation (UAV-VLN) focuses on enabling an aerial agent to follow natural-language instructions in open 3D environments from egocentric visual observations. Current approaches suffer from three coupled issues: weak grounding of instruction-relevant landmarks in visual observations, insufficient exploitation of long-horizon history, and unstable decisions under local traps or repeated exploration. To address these issues, we propose a unified semantic-to-decision framework. F...
  </details>

- **2026-08-10** — Hanlin Jiang, Puyi Wang, Jiandong Jin et al. — [RangeFactory: Scalable Construction of Multi-Hop Cyber Ranges](http://arxiv.org/abs/2608.09526v1)
  <details><summary>📄 Abstract</summary>
  Real-world cyberattacks often require sustained progress across multiple hosts and network segments, making multi-hop cyber ranges essential infrastructure for studying and improving LLM agents' ability to sustain complete attack chains. Prior work has scaled isolated vulnerability tasks and constructed multi-host scenarios from manually specified vulnerability semantics. However, they are still unable to automatically orchestrate the growing supply of vulnerability environments into end-to-end ...
  </details>

- **2026-08-10** — Chenghong Bian, Chaozheng Wen, Hongze Chen et al. — [GLocFM: A Geometry-Aware Foundation Model for 3D Indoor Wireless Localization](http://arxiv.org/abs/2608.09285v1)
  <details><summary>📄 Abstract</summary>
  Learning-based wireless localizers often fail to utilize geometric information about the propagation environment, limiting their ability to exploit non-line-of-sight (NLoS) propagation and generalize across scenes. To bridge this gap, we propose GLocFM, a Geometry-aware Localization Foundation Model, which jointly exploits WiFi measurements and scene geometry represented as a 3D point cloud. We formulate localization as a maximum-likelihood (ML) estimation problem, where the goal is to find a tr...
  </details>

- **2026-08-10** — Chenxu Du, Kang An, Tengyue Wang et al. — [MMArch: Benchmarking Multimodal Reasoning Grounded in Architectural Evidence](http://arxiv.org/abs/2608.09281v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) perform strongly on engineering imagery, yet existing benchmarks mostly test drawing recognition, information extraction, or compliance checking, leaving open whether models can combine distributed visual evidence with engineering principles to reach a conclusion. We introduce MMArch, a benchmark for architecture and civil engineering spanning ten subdomains and built entirely from figures in peer-reviewed papers. Its $1{,}212$ short-answer items are prod...
  </details>

- **2026-08-10** — Yuhan Li, Fangao Zeng, Sicong Kang et al. — [RL-Native Distillation: Exploiting Scored Trajectories for Few-Step Image Generation](http://arxiv.org/abs/2608.09226v1)
  <details><summary>📄 Abstract</summary>
  Efficient text-to-image generation requires both reinforcement-learning (RL)-based reward alignment and few-step distillation, yet these procedures are typically performed sequentially, increasing training cost and risking the loss of reward gains during compression. We instead take an RL-native perspective: diffusion RL already generates reward-scored finite-step trajectories, whose intermediate states provide a natural source of distillation supervision rather than a disposable byproduct of sa...
  </details>

- **2026-08-10** — Chidaksh Ravuru, Shashank Srivastava — [UNMASK: Discovering and Causally Verifying Spurious Shortcuts in Text Classifiers](http://arxiv.org/abs/2608.09209v1)
  <details><summary>📄 Abstract</summary>
  Neural language models trained on large crowdsourced corpora frequently exploit spurious surface patterns tied to target labels without true linguistic or causal relevance, boosting benchmark performance while failing on adversarial or out-of-distribution inputs. Existing approaches either require manual specification of the feature vocabulary or automate discovery only partially, leaving the gap between dataset-level correlation and model-level exploitation unaddressed. We present U N M ASK, a ...
  </details>

- **2026-08-10** — Junyao Wang, Yulin Xu, Yu Li et al. — [CRUISE: Vision-Language Model-Guided Uncertainty-Aware Cross-Modal Sensor Fusion for Robust Autonomous Driving](http://arxiv.org/abs/2608.09202v1)
  <details><summary>📄 Abstract</summary>
  Modern autonomous vehicles are equipped with multiple sensors, such as cameras, LiDAR, and radar, for comprehensive environmental perception. However, robust cross-modal feature fusion remains a critical challenge, as the reliability of each sensor varies significantly across diverse real-world driving conditions, including poor visibility and adverse weather. While uncertainty quantification (UQ) mitigates this issue by allowing models to prioritize reliable signals, existing uncertainty-aware ...
  </details>

- **2026-08-10** — Shenyuan Guan, Qiaodan Hou, Yanjun Chen et al. — [Memoir: Learning, Verifying, and Evolving False-Positive Memories for Static Application Security Testing Tools](http://arxiv.org/abs/2608.09181v1)
  <details><summary>📄 Abstract</summary>
  Static Application Security Testing (SAST) tools have become indispensable in modern secure software devel- opment. However, these tools often generate false-positive (FP) alerts, imposing substantial manual inspection costs and reducing the trust from developers. Existing FP reduction methods still face two primary challenges. First, the large differences among SAST tools and vulnerability categories make it difficult for these methods to learn recurring patterns in historical false positives. ...
  </details>

- **2026-08-10** — Mingrui Liu, Xingxing Zuo, Renlang Huang et al. — [ROEVO: Robust Organized Edge Feature-based Visual Odometry Using RGB-D Cameras](http://arxiv.org/abs/2608.09112v1)
  <details><summary>📄 Abstract</summary>
  This work presents a visual odometry (VO) system that leverages image edge features. Edges are spatially expressive cues commonly present across diverse environments, offering rich textural and structural information. However, existing edge-based VO methods often fail to fully exploit this potential. To this end, we introduce a novel feature representation termed \textit{organized edges}, which transforms disjoint edge pixels into sequentialized clusters, enabling more effective retention and ut...
  </details>

- **2026-08-09** — Delin Mao, Chenghao Sun, Jingwei Song et al. — [ToolVision: Learning When and How to Use Visual Tools with Capability-Aligned Supervision](http://arxiv.org/abs/2608.08907v1)
  <details><summary>📄 Abstract</summary>
  Thinking with images allows a multimodal model to compensate for limited perception by invoking visual tools through code. Yet the prevailing SFT-then-RL recipe creates a different supervision misalignment at each stage. SFT is expected to teach how to use tools, but trajectories from stronger teachers may succeed through perceptual capabilities that a smaller student cannot reliably reproduce or exploit, causing the student to imitate tool-call patterns without learning how to make them useful....
  </details>

- **2026-08-09** — Juncheng Dong, Ding Tong, Ishan Gupta et al. — [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](http://arxiv.org/abs/2608.08889v1)
  <details><summary>📄 Abstract</summary>
  Recommendation systems thrive on personalization, where ''correctness'' is rarely a binary truth but a matter of subjective human preference. As Large Language Models (LLMs) are deployed as autonomous verifiers of safety and quality guidelines, they face a distinctive challenge: context-aware preference alignment. Recent gains in Reinforcement Learning with Verifiable Rewards (RLVR) are indexed mostly on objective, mathematical tasks. Through a large-scale study spanning both proprietary and ope...
  </details>

- **2026-08-09** — Donghui Feng, Fengxi Zhang, Changsheng Gao et al. — [Visual Token Codec: Unleashing Spatial Redundancy for ViT Feature Coding](http://arxiv.org/abs/2608.08832v1)
  <details><summary>📄 Abstract</summary>
  Distributed deployment of large vision foundation models often partitions a ViT backbone and exchanges intermediate token features between computing nodes, making efficient feature compression critical under bandwidth and computation constraints. Existing ViT feature codecs typically flatten heterogeneous global and patch tokens into an L x C pseudo image, causing entropy models to mainly capture sequence-axis dependencies while overlooking the native two-dimensional patch-grid structure. In thi...
  </details>

- **2026-08-08** — Yusra Tariq, Rakesh Chandra Joshi — [Frequency-Domain Dual-Branch Fusion for Medical Visual Question Answering](http://arxiv.org/abs/2608.08307v1)
  <details><summary>📄 Abstract</summary>
  Medical Visual Question Answering (VQA) requires aligning subtle visual evidence, including lesion texture, boundary sharpness, and diffuse density changes, with clinical language. Existing multimodal fusion approaches operating in the spatial domain may not fully exploit complementary frequency information present in visual and textual representations. We introduce a dual-branch frequency-domain fusion module that conditions spectral filtering on the input question, enabling adaptive selection ...
  </details>

- **2026-08-08** — Yiming Lin, Chiyu Hao, Shreya Shankar et al. — [Scout: Scalable Document Extraction via Data Similarity](http://arxiv.org/abs/2608.08261v1)
  <details><summary>📄 Abstract</summary>
  Extracting values from large document collections powers data analysis across many domains. Frontier LLMs extract such values accurately, but processing an   entire collection with one is prohibitively costly. Yet this cost is largely avoidable: real-world collections exhibit rich similarity, so for the same query   over similar documents, the answer tends to recur in similar locations; an LLM need only read that small span, not the whole document. Prior methods that   exploit this similarity fa...
  </details>

- **2026-08-08** — Sujith Pulikodan, Agneedh Basu, Pavan Kumar J et al. — [SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages](http://arxiv.org/abs/2608.08235v1)
  <details><summary>📄 Abstract</summary>
  India's linguistic landscape spans over 700 languages and thousands of dialects, yet the vast majority of automatic speech recognition (ASR) systems support only a small fraction of this diversity. We present SraVaani-1.0, a multilingual ASR model covering 65 Indian languages and dialects, many of which currently have no publicly available or competing ASR system. SraVaani-1.0 is built on a FastConformer architecture and trained from scratch through a three-stage pipeline.In the first stage, we ...
  </details>

- **2026-08-08** — Ximeng Liu, Qianlong Wang, Yingming Mao et al. — [Janus: An Algorithm-Evaluator Co-Evolution Framework for LLM-Driven Discovery under Expensive Evaluation Budgets](http://arxiv.org/abs/2608.08189v1)
  <details><summary>📄 Abstract</summary>
  LLM-driven program discovery relies on rapid evaluator feedback, but many scientific and engineering tasks require high-fidelity simulations, hardware execution, or physical experiments, making each evaluation expensive. Cheap surrogate evaluators can reduce this cost, yet fixed surrogates are vulnerable to search-induced distribution shift and are difficult to fit reliably from sparse, search-biased labels. We introduce Janus, a framework that uses LLMs to co-evolve target programs and executab...
  </details>

- **2026-08-08** — Alvin Combrink, Sabino Francesco Roselli, Martin Fabian — [AOC-CBS: Anytime-Optimal Continuous-time Conflict-Based Search for Generalised Multi-Agent Path Finding](http://arxiv.org/abs/2608.08175v1)
  <details><summary>📄 Abstract</summary>
  Many research fields share a common structure: a set of agents, each pursuing its own goal, whose actions must be coordinated so that no two of them conflict. Multi-Agent Path Finding (MAPF) is a concrete instance of this structure, with applications from warehouses to road traffic and airports. Much of MAPF research assumes discrete time, circular agents sharing one spatial graph, a single goal per agent, and that an agent must remain at its goal once reached, precluding heterogeneous fleets, n...
  </details>

- **2026-08-08** — Sajjad Ghiasvand, Yifan Yang, Mahnoosh Alizadeh et al. — [ZOMP: Zeroth-Order Multi-Modal Prompt Tuning for Vision-Language Models](http://arxiv.org/abs/2608.08060v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning vision-language models such as CLIP typically requires backpropagation (BP) through the full model, which is infeasible when only forward-pass access is available, as is common for memory-constrained edge devices and proprietary model deployments. Prior BP-free, zeroth-order prompt-tuning methods avoid this requirement but often tune prompts in a single modality or optimize over a search space large enough that convergence requires thousands of forward passes, which is impractical un...
  </details>

- **2026-08-08** — Ibne Farabi Shihab, Fariya Afrin — [Quality-Diversity Stress Tests for Process Reward Models:What Archive Coverage Can and Cannot Certify](http://arxiv.org/abs/2608.08008v1)
  <details><summary>📄 Abstract</summary>
  Process reward models (PRMs) score intermediate reasoning steps and are widely used for search, ranking, and training, but optimization can exploit these learned proxies by increasing reward while turning correct reasoning into incorrect reasoning. We formulate PRM stress testing as a quality-diversity search problem using MAP-Elites, retaining the most severe correctness-flipping edit in each behavior-space region while separating search coverage from exploit coverage. We characterize what such...
  </details>

- **2026-08-08** — Fariya Afrin, Ibne Farabi Shihab — [Evaluator Ensembles Under Reward Hacking: Covariance Geometry and Finite-Search Guarantees](http://arxiv.org/abs/2608.08002v1)
  <details><summary>📄 Abstract</summary>
  Language-model judges and reward models enable scalable supervision, but finite optimization can exploit evaluator errors rather than improve response quality. We characterize this failure through the covariance geometry of evaluator ensembles. For calibrated judges, the ensemble mean retains common-mode error along the all-ones direction, whereas cross-judge disagreement captures only orthogonal error. Consequently, disagreement can be high despite robust aggregation, or low while shared respon...
  </details>

- **2026-08-08** — Reto Achermann, Em Chu, Ryan Mehri et al. — [Velosiraptor: Code Synthesis for Memory Translation](http://arxiv.org/abs/2608.07966v1)
  <details><summary>📄 Abstract</summary>
  Security is among the top concerns of operating system (OS) developers. A secure runtime environment relies on the OS to correctly configure the memory hardware on which it runs. This is mission-critical as it provides essential security-relevant features and abstractions that ensure the integrity and isolation of untrusted applications running alongside each other. Configuring a platform's memory hardware is not a one-off effort as designers constantly develop new mechanisms for translation and...
  </details>

- **2026-08-07** — Lumin Chen, Qingyao Tian, Jinpeng Li et al. — [Geometry-Aware Camera Localization for Bronchoscopy](http://arxiv.org/abs/2608.07116v1)
  <details><summary>📄 Abstract</summary>
  Camera localization in bronchoscopy remains a challenging problem due to stringent accuracy requirements, real-time constraints, and limited training data. Compared to natural scenes, the confined anatomical structures demand millimeter-level precision, while intraoperative guidance necessitates low-latency inference. However, existing methods often fail to effectively exploit preoperative geometric priors, limiting their robustness and accuracy. To address these limitations, we propose a unifie...
  </details>

- **2026-08-07** — Yash Priya Shastri, Anand Eswaran, Adnan Qidwai et al. — [BONSAI: Evolvability-Guided Tree Search over Skills](http://arxiv.org/abs/2608.07056v1)
  <details><summary>📄 Abstract</summary>
  A skill is a naturallanguage document that steers a frozen agent whose weights cannot be updated so any capability the agent lacks must be supplied in prose Optimising a skill is therefore optimising text against a score and the standard recipe which keeps any edit that raises a heldout score is blind in a specific way a single score cannot tell a document perched on a narrow overfit spike from one resting on a broad plateau even though only the second can still be improved We introduce BONSAI a...
  </details>

- **2026-08-07** — Junghwan Park, Sangcheol Sim, Woojin Cho et al. — [Summarize First, Download Later: Onboard VLMs for Bandwidth-Efficient Earth Observation](http://arxiv.org/abs/2608.06959v1)
  <details><summary>📄 Abstract</summary>
  Modern Earth observation (EO) satellites carry increasingly advanced sensors that produce vast volumes of high-resolution, multispectral data, yet downlink capacity remains a critical bottleneck -- often causing significant latency or the loss of valuable observations within limited contact windows. We propose a "Summarize First, Download Later" paradigm that exploits recent advances in onboard edge computing and Vision-Language Models (VLMs). Rather than indiscriminately downlinking raw imagery...
  </details>

- **2026-08-06** — Nima Hatami, Karim Faez, Saeed Sharifian et al. — [CFGPNet: Cross-Attention-Based Fused Gradient Programmed Network Framework for Multispectral Object Detection](http://arxiv.org/abs/2608.06205v1)
  <details><summary>📄 Abstract</summary>
  RGB--T object detection exploits the complementary strengths of visible and infrared imagery, supporting robust perception in low-light, adverse-weather, and complex multi-scale environments. However, existing methods still suffer from insufficient cross-modal interaction, unstable fusion from modality distribution gaps, and the high computational cost of heavy attention-based architectures. To address these issues, CFGPNet is proposed, a Cross-Attention-Based Fused Gradient Programmed Network f...
  </details>

- **2026-08-06** — Omar Coser, Antonio Orvieto, Paolo Soda et al. — [Is Self-Pretraining really useful to improve diagnosis in medical Time Series?](http://arxiv.org/abs/2608.06122v1)
  <details><summary>📄 Abstract</summary>
  Inspired by recent evidence that transformer architectures benefit from Self-PreTraining (SPT) on long-context benchmarks, we investigate whether similar gains extend to multimodal, multivariate, and even simple univariate medical time series. Our objective is to assess the impact of SPT on the performance and scalability of transformer-based models across diverse medical applications, particularly under limited data conditions. We evaluate transformer architectures on three representative medic...
  </details>

- **2026-08-06** — Wenhao Mao, Chengbin Hou, Weixiao Wang et al. — [Training-Free Token-Level Steering for LLM Personalized Co-Writing](http://arxiv.org/abs/2608.06069v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) show great promise for personalization, they often lack specialized domain knowledge. Conventional solutions like fine-tuning struggle with high computational costs and rapid data updates, while Retrieval-Augmented Generation fails to provide fine-grained, token-level steering. Furthermore, chat-based interfaces remain dominant, whereas productive co-writing paradigms have not yet been well exploited beyond the coding domain. To this end, we introduce SteerWrit...
  </details>

- **2026-08-06** — Trond Vatten, Yuming Jiang — [ASGE-RR: Agentic Service Graph Embedding with Revisable Reservations for Dynamic AI-Agent Calls](http://arxiv.org/abs/2608.06033v1)
  <details><summary>📄 Abstract</summary>
  AI-agent workflows often involve remote calls to models, memory stores, and tools distributed across a network. As execution progresses, these dependency calls collectively form an agentic service graph (ASG). Unlike traditional service requests, many dependency calls are revealed only at runtime. Consequently, allocating resources to a currently visible call may consume capacity later needed by a call from a higher-value workflow. We formulate this challenge as Agentic Service Graph Embedding (...
  </details>

- **2026-08-06** — Zhuowen Liu, Bohan Cui, YinShang Guo et al. — [HERALD: Counterfactual Audits and Minimal Repairs for Proof-of-Retrieval Rewards](http://arxiv.org/abs/2608.06012v1)
  <details><summary>📄 Abstract</summary>
  Search-agent rewards mix answer quality, citation grounding, tool cost, and anti-hacking terms; a high score therefore need not imply that cited evidence was retrieved, and added penalties can cancel. We introduce HERALD, an offline audit that applies exact same-question interventions, separates candidate-visible from oracle information, and enumerates detector contracts before policy optimization. On four Qwen3-8B pools from HotpotQA, 2WikiMultiHopQA, and MuSiQue, $R_0$ rejects search deletion ...
  </details>

- **2026-08-06** — Majed Jaber, Abdul Qadir Khan, Ankush Meshram et al. — [Tool Demo: Topology analysis with GPML for detection of cyberattacks in Water Distribution Networks](http://arxiv.org/abs/2608.05902v1)
  <details><summary>📄 Abstract</summary>
  Water distribution networks depends on industrial control systems to integrate the physical process with communication network, making them vulnerable to cyberattacks that alter the traffic pattern and network behavior. Traditional detection approaches that rely on raw traffic or protocol information often oversee structural changes that are induced by such attacks. In this work, we presents a topology-driven approach for detection of cyberattacks in water distribution networks based on Graph Pr...
  </details>

- **2026-08-06** — Shayell Aharon Salomon Amir Shaked Matan Noga — [The Vulnerability With No CVE: Managing Persistent Gaps Between Mandate and Authority in AI Coding Agents](http://arxiv.org/abs/2608.05884v1)
  <details><summary>📄 Abstract</summary>
  Existing guidance identifies excessive agency, excessive permission, weak task-bound authorization, and inadequate agent controls as important risks. Control frameworks also describe capabilities for constraining, authorizing, observing, validating, and responding to agent activity. Yet security programs still need a way to manage persistent deployed instances that span components and outlive any one event.   We propose the agentic posture vulnerability (APV) as a task-conditioned vulnerability-...
  </details>

- **2026-08-06** — Dong Wang, Qiaoyu Han, Lin Yang et al. — [Agent-Based Test Assertion Generation via Diverse Perspective Aggregation](http://arxiv.org/abs/2608.05822v1)
  <details><summary>📄 Abstract</summary>
  Test assertions are critical elements of unit tests, serving as checkpoints to validate expected behavior and ensure software correctness. Numerous techniques have been proposed to automate assertion generation, with recent progress notably driven by large language models (LLMs). Despite the promise, existing approaches such as ChatAssert suffer from modest accuracy, heavy reliance on oversampling, and vulnerability to model randomness due to one-shot prompting. To address these limitations, we ...
  </details>

- **2026-08-06** — Mustafa Alfarhan, Matteo Ravasi, Fuqiang Chen et al. — [Foundation Model-Assisted Full Waveform Inversion](http://arxiv.org/abs/2608.05763v1)
  <details><summary>📄 Abstract</summary>
  Full waveform inversion (FWI) can recover high-resolution subsurface velocity models. Conventional waveform-difference objectives, however, are vulnerable to cycle skipping when the starting model is inaccurate. We introduce an FWI objective that compares features produced from modeled and observed seismic traces by SeisLM, a pretrained seismic foundation model. The SeisLM encoder remains frozen during inversion, and the feature discrepancy is differentiated with respect to the modeled traces to...
  </details>

- **2026-08-06** — Victor Gialis, Maxime Metz, David Esteve et al. — [Spectral Aliasing Pretext: A novel task for Self-Supervised fault diagnosis in rotating machinery](http://arxiv.org/abs/2608.05705v1)
  <details><summary>📄 Abstract</summary>
  Deep learning is a new way for machinery fault diagnosis but requires extensive labeled data, a scarce resource in industrial settings. We propose Spectral Aliasing Pretext (SAP), a self-supervised learning method that pretrains models on unlabeled vibration data by exploiting spectral aliasing. We deliberately undersample signals to create folded spectrum, then train a Transformer to reconstruct the original unfolded spectrum. This pretext task forces the model to learn frequency-domain invaria...
  </details>

- **2026-08-06** — Changshuo Liu, Yanzheng Jin, Shangfeng Cai et al. — [F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading](http://arxiv.org/abs/2608.05668v1)
  <details><summary>📄 Abstract</summary>
  With increasingly diverse and heterogeneous information sources, effectively leveraging multimodal data is becoming pivotal for high-quality financial trading. Although recent advancements in Large Language Model (LLM)-based agents have enabled the ingestion of multimodal inputs, existing methods fail to capture nuanced cross-modal dependencies and remain vulnerable to market noise, due to limited multimodal modeling, ineffective fusion mechanisms, and inadequate robustness. To address these cha...
  </details>

- **2026-08-06** — Yu Gu, Zhi Zheng, Yunpeng Ba et al. — [Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging](http://arxiv.org/abs/2608.05541v1)
  <details><summary>📄 Abstract</summary>
  Evolution Strategy (ES) is a promising alternative to gradient-based fine-tuning for resource-constrained Large Language Model (LLM) reasoning. However, directly applying ES to billion-parameter LLMs is highly ineffective. In such high-dimensional parameter spaces, most random perturbations are nearly orthogonal to useful update directions, leading to unstable optimization. We propose Hyper-ES, a subspace-based ES framework that avoids the weakness of ES in full-parameter search while exploiting...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 56 papers

- **2026-08-10** — Hunar Batra, Lachin Naghashyar, Ashkan Khakzar et al. — [Multimodal Model Diffing for Feature Discovery and Control](http://arxiv.org/abs/2608.09928v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) exhibit strong visual understanding, yet the internal features that cause these behaviors remain difficult to identify, audit, or control. While applicable to post-hoc inspection, hidden states that are decomposed into interpretable feature directions using sparse autoencoders (SAEs) neither readily isolate which features are changed by multimodal training, nor are they directly useful for targeted control. We introduce MMDiff, a multimodal model-diffing ...
  </details>

- **2026-08-10** — Peter Lorenz, Anjith George, Marcel Sébastien — [LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection](http://arxiv.org/abs/2608.09633v1)
  <details><summary>📄 Abstract</summary>
  Face presentation attack detection (PAD) aims to reliably detect a wide range of presentation attacks. While PAD methods achieve strong performance within individual datasets, their performance degrades under cross-dataset evaluation. Variations in sensors or lighting conditions can reduce the effectiveness of detectors from near-perfect to nearly random. Foundation models (FMs) have emerged as a promising alternative because typical PAD datasets, such as the MCIO benchmarks (MSU-MFSD, CASIA-FAS...
  </details>

- **2026-08-10** — Yanqiu Li, Yang Xiao, Jisheng Bai et al. — [MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](http://arxiv.org/abs/2608.09593v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in speech synthesis and audio generation have made high-fidelity acoustic forgery low-cost and difficult to attribute, enabling a realistic attack scenario in which speech and background audio are independently manipulated over otherwise authentic video. Yet existing research either focuses on visual manipulation, addresses speech detection in isolation, or conflates speech and non-speech audio as a single undifferentiated audio stream, overlooking the distinct forensic challenge...
  </details>

- **2026-08-10** — Tadanobu Chuyo Kamijo, Ori Rottenstreich, Javier Conde et al. — [Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness](http://arxiv.org/abs/2608.09900v1)
  <details><summary>📄 Abstract</summary>
  Large language model evaluations typically focus on performance under nominal conditions, creating an illusion of capability where models comfortably walk a narrow, highly optimized generation corridor. In real-world deployments, however, complex system prompts, safety guardrails, and structural constraints continuously force models off this nominal path, driving a divergence between benchmark scores and deployment performance. To address this issue, we introduce Decoding-Level Taboo, a zero-pro...
  </details>

- **2026-08-10** — Dongchi Huang, Hongyin Zhang, Bohan Hou et al. — [RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](http://arxiv.org/abs/2608.09853v1)
  <details><summary>📄 Abstract</summary>
  General-purpose reward models are increasingly the bottleneck for scaling robot learning, yet the recipe for learning value-related capabilities from large-scale heterogeneous corpora remains underexplored. Existing approaches tie supervision to task-internal anchors such as preferences or normalized progress, none of which transfer cleanly across embodiments and data sources. We introduce RynnValue, an open-source value foundation model for robotic manipulation that replaces these anchors with ...
  </details>

- **2026-08-10** — Zhanna Mukhametsharip, Vera Demberg, Varsha Suresh — [PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large Vision-Language Models](http://arxiv.org/abs/2608.09772v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) have demonstrated strong performance on multimodal benchmarks, yet it remains unclear whether they genuinely reason about relationships between images and text or rely on superficial correlations, known as shortcut learning. This question is particularly important for multimodal sarcasm detection, where successful prediction depends on recognizing pragmatic incongruity rather than treating sarcasm as simple image-text mismatch. We introduce PragMatch, a contr...
  </details>

- **2026-08-10** — Yilin Jiang, Xiaorong Zhu, Fei Tan et al. — [ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models](http://arxiv.org/abs/2608.09548v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in education as tutors, teaching assistants, and content generators. These roles place demands that ordinary question answering does not: a usable education-facing model is supposed to be accurate, safe under sensitive prompts, instructionally useful, and aligned with pedagogical goals at the same time. Existing benchmarks evaluate these requirements largely in isolation, so none assesses education-facing suitability as an integrated profile. We in...
  </details>

- **2026-08-10** — Petr Hauschwitz — [Direct Laser Interference Patterning of Functional Metal Surfaces: From Written Geometry to Functional Interfaces](http://arxiv.org/abs/2608.09545v1)
  <details><summary>📄 Abstract</summary>
  Direct laser interference patterning (DLIP) generates periodic micro- and nanoscale structures with increasing precision and throughput, yet similar geometries can produce fundamentally different functional responses. This review examines why morphology alone cannot predict friction, wetting and ice adhesion, bacterial response, cell behaviour, optical performance or electrochemical and photovoltaic function. DLIP is treated as a model system in which the optically prescribed geometry can be dis...
  </details>

- **2026-08-10** — Hanlin Jiang, Jionghao Huang, Shaofei Li et al. — [STAIR: Effective Incident Response Using an End-to-End Agentic Planning Framework](http://arxiv.org/abs/2608.09524v1)
  <details><summary>📄 Abstract</summary>
  Incident response planning is critical for restoring compromised software systems after cyberattacks. Common practice relies on expert-driven playbooks that encode fixed response procedures, but these static workflows struggle to adapt to evolving incident states, changing recovery objectives, and execution feedback. Recent LLM-based planners and tool-using agents improve automation, yet they remain unstable in long-horizon response because they lack a unified basis for maintaining incident stat...
  </details>

- **2026-08-10** — Thomas Lauber, Mehmet Ozgur Turkoglu, Sélène Ledain et al. — [SwissCrop25: A National Multi-Year Benchmark for Operational Crop Mapping](http://arxiv.org/abs/2608.09497v1)
  <details><summary>📄 Abstract</summary>
  Operational crop mapping requires models that generalise across years, resolve fine-grained crop taxonomies, and distinguish cropland from surrounding landscapes. However, existing crop mapping datasets enable evaluation of these requirements only in isolation. We therefore introduce SwissCrop25, a national-scale crop mapping benchmark dataset spanning seven growing seasons (2019-2025). SwissCrop25 combines Sentinel-2 time series, daily temperature observations, a fine-grained 73 crop taxonomy i...
  </details>

- **2026-08-10** — D M S Sultan, R. Plackett, A. E. McDougall et al. — [Automated Signal Integrity Analysis Framework for High-Speed Interconnects in the PPCB-1347-MuPix11 Probe Card](http://arxiv.org/abs/2608.09462v1)
  <details><summary>📄 Abstract</summary>
  A reusable MATLAB signal-integrity (SI) framework is presented that converts compatible four-port S-parameter data, measured by VNA or obtained from electromagnetic simulation, into traceable link-level evidence rather than a single loss metric. The framework is demonstrated on the four 1.25 Gbps differential routes (DP1-DP4) of the PPCB-1347-MuPix11 probe card using PTSL CST Microwave 3D-Solver-derived four-port S-parameters and a virtual time-domain solver. The automated pipeline preflights fi...
  </details>

- **2026-08-10** — Zihan Wang, Anglin Liu, Rongyi Wang et al. — [Coupled Graph--Policy Distillation for Personalized Medication Safety in Older Adults with Multimorbidity](http://arxiv.org/abs/2608.09443v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can support medication review between clinical visits, but safe choices for older adults with multimorbidity depend on conditions, medications, and geriatric risks that users may omit. We introduce ATLAS, a coupled graph--policy distillation framework for patient-adaptive medication safety. ATLAS structures guideline evidence as a medication-safety graph. Targeted questions update the patient state and distill relevant relations into a patient-specific medicatio...
  </details>

- **2026-08-10** — Chengyu Lai, Jiuning Lin, Zhibo Xiao et al. — [MetaStrategy: Generative Ranking with Executable LLM Strategies](http://arxiv.org/abs/2608.09440v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems rank heterogeneous content under coupled user, business, commercial, and experience objectives. Existing generative ranking methods typically construct item sequences directly, making them difficult to integrate with mature predictive models, operational rules, and field-level guardrails. We present MetaStrategy, a framework that instead generates a structured, executable ranking strategy. Conditioned on request context, a large language model (LLM) policy emits a ...
  </details>

- **2026-08-10** — Bin Zhang, Bowen Zheng, Chao Yi et al. — [DREAM Technical Report](http://arxiv.org/abs/2608.09408v1)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems commonly use cascaded retrieval, ranking, and re-ranking pipelines. Although efficient, these pipelines fragment information and objectives across modules, rely on rigid rules, and have limited awareness of real-time intent, leaving session-level shifts among browsing, comparison, and purchase insufficiently addressed. We present DREAM (Developing Recommender Engine with Agentic Methods), an autonomous optimization control architecture that adds a perception-aware,...
  </details>

- **2026-08-10** — Puneet Mathur, Manan Suri, Dinesh Manocha — [Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models](http://arxiv.org/abs/2608.09227v1)
  <details><summary>📄 Abstract</summary>
  Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive. While recent token compression methods attempt to alleviate this burden, compressing modalities in isolation often destroys the temporal cross-modal anchors necessary for coherent reasoning. We introduce Omni2LoRA, a two-stage framework for efficient parametric memory compression via coherence-preserving context distillation that bypas...
  </details>

- **2026-08-10** — Zhihao Zhang, Gengwei Zhang, Tianlong Chen et al. — [RefineAny3D: Depth Refinement as Semantic Alignment for Monocular 3D Detection](http://arxiv.org/abs/2608.09147v1)
  <details><summary>📄 Abstract</summary>
  Monocular 3D object detection spans two regimes: closed-set detectors operating within a fixed category vocabulary, and open-vocabulary detectors that localize arbitrary categories by leveraging depth foundation models for 3D geometry. We find that current depth foundation models, despite their strong zero-shot generalization, lack the object-level precision 3D detection demands: substituting a state-of-the-art depth foundation model for a strong detector's predicted depth degrades accuracy, eve...
  </details>

- **2026-08-10** — Oluwanifemi Bamgbose, Simon Rosen, Jash Shah et al. — [Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions](http://arxiv.org/abs/2608.09930v1)
  <details><summary>📄 Abstract</summary>
  Automated Text-to-Speech (TTS) evaluation methods (Mean Opinion Score (MOS) predictors and Audio Large Language Models (Audio-LLM) judges) are expected to reflect human perception, yet it is unclear how well they capture the distinct aspects of speech that listeners actually perceive. We deconstruct "naturalness" into a linguistically grounded annotation schema spanning 10 distinct perceptual dimensions, and use it to construct the first dimension-level meta-evaluation benchmark for TTS, compris...
  </details>

- **2026-08-10** — Jingtai He, Shiyuan Meng, Wenchao Meng et al. — [ADOPD: Reference-Privileged On-Policy Distillation for MLLM-Based Industrial Anomaly Detection](http://arxiv.org/abs/2608.09789v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection (IAD) requires identifying fine-grained deviations from normal visual patterns. Multimodal large language models (MLLMs) can improve recognition accuracy by comparing query images with references at inference time, but these benefits rely on additional retrieval and processing. We investigate whether the benefits of reference comparison can instead be internalized in the model parameters. Access to references during training allows a reference-aware teacher to superv...
  </details>

- **2026-08-10** — Stefan Smeu, Dragos-Alexandru Boldisor, Elisabeta Oneata et al. — [Foundation Models are Implicit Deepfake Detectors](http://arxiv.org/abs/2608.09427v1)
  <details><summary>📄 Abstract</summary>
  Pretrained self-supervised representations have emerged as a core component of current deepfake detection methods, yet it remains unclear which of their properties make real and fake media distinguishable. In this work, we uncover a surprisingly consistent phenomenon: across multiple pretrained models, datasets, and both image and video domains, fake samples systematically produce lower-magnitude representations than their real counterparts. Motivated by this finding, we formulate deepfake detec...
  </details>

- **2026-08-10** — Patryk Marszałek, Jacek Tabor, Marek Śmieja — [In-Context Density Estimation for Tabular Data](http://arxiv.org/abs/2608.09348v1)
  <details><summary>📄 Abstract</summary>
  Density estimation underlies many unsupervised tasks on tabular data such as anomaly detection, out-of-distribution detection, and data augmentation. Although all these problems reduce to questions about where probability mass lies, they are typically solved individually by fitting a separate model to each dataset, with its own hyperparameters and tuning budget. We introduce ICED, an in-context, energy-based density estimator that removes this per-dataset cost. ICED is a transformer-based model ...
  </details>

- **2026-08-10** — Ruiyu Li, Zhiying Zhu — [Subjective Multi-Bias Detection with Large Language Models](http://arxiv.org/abs/2608.09126v1)
  <details><summary>📄 Abstract</summary>
  In this project, we delved into the pervasive challenge of bias detection within the text content. More specifically, our focus lies on the identification of subjective bias, a type of bias that introduces improper attitudes or portrays a statement at odds with the actual truth. The subjective bias can jeopardize the authenticity and reliability of texts, leading to misconceptions and potential social tensions, especially when expressed through offensive language.   Following prior work [1], we ...
  </details>

- **2026-08-10** — Lin Zhang, Fan Yang — [Extreme Value Alpha and Crash Risk: Separating Structural Tails from Lottery Tails with LLM-Extracted Disclosure Networks](http://arxiv.org/abs/2608.09089v1)
  <details><summary>📄 Abstract</summary>
  A heavy upper tail in a stock's returns is ambiguous: it can be a lottery tail, transient jump risk that investors overpay for (the MAX discount), or a structural tail, the statistical shadow of an economic reconfiguration that precedes extreme winners. Returns alone cannot separate them, so tail heat alone is not an alpha signal. Our discriminator is the firm's disclosure-measured network: a directed, span-grounded graph from 10-K filings via an auditable LLM pipeline, whose rewiring decomposes...
  </details>

- **2026-08-09** — Shiva Ahir — [IDRAAK: From Multi-Agent NLP to Few-Shot Prompting for Semantic Drift Detection in Technical Requirements](http://arxiv.org/abs/2608.08801v1)
  <details><summary>📄 Abstract</summary>
  Translating technical requirements across languages can introduce semantic drift, altering numerical constraints, polarities, modalities, or other specification-critical meaning. IDRAAK is presented as an interpretable framework for detecting such drift using a language-independent Semantic Requirement Representation (SRR), with six detection workflows evaluated, ranging from deterministic comparison to multi-agent verification and few-shot prompting. On 890 synthetic perturbations across 300 re...
  </details>

- **2026-08-09** — Tarun Sharma — [HaloMark: A Spectral Threshold for Embedding-Vector Watermarking under C2PA](http://arxiv.org/abs/2608.08645v1)
  <details><summary>📄 Abstract</summary>
  Foundation-model embeddings are now a primary data asset, but the content-provenance machinery built for images and audio does not transfer to them. C2PA binds to an asset with a stable bit-level or perceptual identity; embeddings have neither, since quantisation, projection, fine-tuning, and windowed averaging reshape them in normal use and break any fixed hash.   We present HaloMark, a watermark for embedding vectors cryptographically bound to a C2PA manifest. It composes four standard primiti...
  </details>

- **2026-08-09** — Wenyao Cui, Huaping Zhang, Yongyi Huang et al. — [SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification](http://arxiv.org/abs/2608.08786v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly serve as data-driven reasoners, yet their chains-of-thought (CoT) can be unfaithful even when final answers are correct. Most existing ``verification'' signals are not diagnostic: answer matching observes only the outcome, LLM-as-judge provides subjective and non-verifiable critiques, and scalar rewards (e.g., PRMs/RMs) offer little insight into where a multi-step derivation fails.We propose \textbf{SymDiag}, a neuro-symbolic framework that \textbf{refra...
  </details>

- **2026-08-09** — Jan Spörer — [Can Open-Weight Models Compete on Financial Text Comprehension?](http://arxiv.org/abs/2608.08634v1)
  <details><summary>📄 Abstract</summary>
  Open-weight language models from Chinese AI labs caught up on benchmarks relative to proprietary frontier models in recent months. Yet their reliability on real-world financial tasks remains largely untested. We updated the Financial Touchstone benchmark, which now has 2,967 question context-answer triplets across 495 international annual reports. We also apply a new set of models on the benchmark, expanding coverage from eleven to twenty models across ten providers, including recent open-weight...
  </details>

- **2026-08-09** — Yi-Fan Cao, Qing Shi, Liangwei Wang et al. — [SocialFiVis: A Visual Analytics Sandbox for LLM-Grounded Multi-Agent Simulation in Social Finance](http://arxiv.org/abs/2608.08497v1)
  <details><summary>📄 Abstract</summary>
  The emergence of social finance (SocialFi) transforms online communities into complex socio-economic systems. Within these spaces, collective decisions shape a "digital commons" characterized by social capital (e.g., community trust) and financial health (e.g., market liquidity). Governing such hybrid ecosystems is challenging because real-world interventions are costly and irreversible. While counterfactual simulation is essential for exploring alternative governance strategies, existing approa...
  </details>

- **2026-08-09** — Zongwei Wang, Min Gao, Guangyu Hu et al. — [Personalized Communication Skills for Agentic Recommender Systems](http://arxiv.org/abs/2608.08417v1)
  <details><summary>📄 Abstract</summary>
  Agentic recommender systems increasingly employ large language model-based UserAgents to evaluate candidate items through simulated feedback before recommendations are delivered. However, existing UserAgents typically reason in isolation based on limited personal histories, which may lead to perspective narrowing: the agent evaluates candidates from a local and incomplete view, overlooks relevant preference facets, and consequently produces inaccurate judgments. A natural way to alleviate this p...
  </details>

- **2026-08-09** — David M. Markowitz, Timothy R. Levine — [Theory-Guided Deception Detection: A RAG-Based Artificial Intelligence Exploration](http://arxiv.org/abs/2608.08881v1)
  <details><summary>📄 Abstract</summary>
  The current work developed seven Retrieval-Augmented Generation (RAG) models based on leading deception theories and compared how deception judgments were made relative to baseline models. Across 700 statements drawn from five published deception datasets, four large language models (gpt-4o, claude-sonnet-4-6, ollama/llama3, deepseek-v4-flash), and two run-types (RAG vs. baseline), a total of 39,200 deception judgments were rendered. Detection accuracies were consistent with typical human accura...
  </details>

- **2026-08-09** — Lennox Anderson, Ahmed Boutar, Jonah Mulcrone et al. — [Can Webcam Gaze Constrain Mesa-Objectives in Driving Models? An Instrument Precision Analysis](http://arxiv.org/abs/2608.08947v1)
  <details><summary>📄 Abstract</summary>
  Current hazard detection systems in autonomous driving may develop mesa objectives, learned internal goals that achieve high training performance through spurious correlations rather than genuine hazard recognition. We investigate whether human gaze patterns, captured via webcam-based eye tracking (WebGazer.js), can serve as privileged information to constrain mesa-objective formation. We collected 137,663 frame-level gaze samples synchronized with hazard annotations across 388 real dashcam clip...
  </details>

- **2026-08-09** — Kalelo Dukuray, Israel Pina, Evan Perez et al. — [Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis](http://arxiv.org/abs/2608.08935v1)
  <details><summary>📄 Abstract</summary>
  This work presents a unified multimodal AI system for damage assessment that integrates retrieval-augmented generation (RAG) models, thermal spectrum perception, vision foundation model pipelines, and exploratory wireless signal sensing. A RAG component is developed to ground a locally hosted language model in project-specific documentation, including specialized damage level classification criteria to mitigate hallucinations during inference. Controlled comparisons against static few-shot promp...
  </details>

- **2026-08-09** — Anushka Roy, Jyotirmoy Singh, Shreea Bose et al. — [Agentic Anomaly Detection with ORCA-Style Dynamic Inductive Bias Adaptation in Multimodal Wearable Time Series Data](http://arxiv.org/abs/2608.08859v1)
  <details><summary>📄 Abstract</summary>
  Wireless Body Area Networks (WBANs) generate multivariate physiological time series that are highly nonstationary and must often be processed under strict computational and memory constraints. A critical yet underexplored challenge in this setting is selecting an appropriate temporal receptive field, which serves as a strong inductive bias for anomaly detection models. Existing approaches typically rely on fixed temporal contexts, which can perform inconsistently across heterogeneous signal regi...
  </details>

- **2026-08-09** — Madhumitha Venkatesh, Shanawaj S Madarkar, Konda Reddy Mopuri — [Parcel2Progression: An Anatomy-aware Longitudinal Framework for Alzheimer's Disease Diagnosis](http://arxiv.org/abs/2608.08753v1)
  <details><summary>📄 Abstract</summary>
  Alzheimer's disease (AD) progression is a longitudinal process with subtle pathological cues in the early stages. Yet, computational constraints have limited most neuroimaging models to either compromise spatial information or limit the number of longitudinal scans. We aim to overcome this bottleneck and fully leverage high-resolution, variable-length T1w structural MRI (4D sMRI) scan sequences. We introduce Parcel2Progression (P2P), a Longitudinal Transformer Framework which tackles this challe...
  </details>

- **2026-08-08** — Zhengyang Shan, Xu Qian, Jiayun Xin et al. — [OBLIVION: Workflow-Level Operational Skill Unlearning for Deployed Agents](http://arxiv.org/abs/2608.08264v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents are becoming operational interfaces to files, memories, registries, and external tools. This deployment shift creates a new skill revocation problem: after a skill is removed from an explicit registry, an agent may still reconstruct it from residual carriers such as archives, transcripts, schemas, or memory entries. We study this problem as operational skill unlearning, where the goal is not parameter-level forgetting, but preventing a deployed agent from rebuilding a...
  </details>

- **2026-08-08** — Anton Razzhigaev, Andrei Gritsaev, Andrei Kaznacheev et al. — [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](http://arxiv.org/abs/2608.08311v1)
  <details><summary>📄 Abstract</summary>
  We present Ouroboros, a self-developing agent harness whose tools, prompts, context assembly, and core implementation improve through reviewed commits that become the runtime for later work. Core evolution proceeds in two modes. In recursive free evolution, improvement is itself a task, and completing one evolution cycle can schedule the next. In experience-driven core evolution, ordinary work and social interaction expose bugs, rough edges, and inefficient context construction that lead to revi...
  </details>

- **2026-08-08** — Rui Wang, Yeteng Wu, Xianling Zhang et al. — [VTO: Visual Tool Orchestration for Video Anomaly Detection](http://arxiv.org/abs/2608.08219v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly detection (VAD) is a critical yet challenging task due to the complex and diverse nature of real-world scenarios. Traditional deep learning approaches are fundamentally limited by poor generalization across diverse scenarios. While multimodal agents offer a promising tool-learning paradigm for VAD, current systems relying on supervised fine-tuning struggle with complex orchestration, and standard reinforcement learning often causes premature termination due to coarse-grained outcom...
  </details>

- **2026-08-08** — Satoshi Matsuoka — [Compositional Threat Analysis of Latent Compromise in LLM Agent Systems: The Order 66 Scenario](http://arxiv.org/abs/2608.08131v1)
  <details><summary>📄 Abstract</summary>
  In the fictional Order 66, catastrophe does not arise from a powerful command alone: a trusted population is preconditioned, a short directive activates the concealed condition, and protective authority turns against the system. This paper translates that mechanism into an origin-neutral security analysis of tool-using large language model (LLM) agents. A representative scenario combines a deployed artifact or shared memory bearing a dormant destructive rule, a later email, document, update, or ...
  </details>

- **2026-08-08** — Yichun Yeh, Yiheng Li, Xiaobo Hu et al. — [Evidence-Grounded Forensic Reasoning for Detecting and Grounding Multi-Modal Media Manipulation](http://arxiv.org/abs/2608.08009v1)
  <details><summary>📄 Abstract</summary>
  Fake news increasingly relies on cross-modal image-text forgeries, making transparent and verifiable reasoning chains an urgent need for Detecting and Grounding Multi-Modal Media Manipulation (DGM4). Existing methods produce black-box detection results without any decision rationale, limiting their reliability in forensic practice. Multi-modal Large Language Models (MLLMs) offer a natural path toward explainability, but applying them to DGM4 raises two difficulties. First, models tend to generat...
  </details>

- **2026-08-08** — Negin Ayoughi, Baharin A. Jodat, Armina Faghihi et al. — [Synthesizing Behavioural Models of CPS Using Automata Learning and Statistical Machine Learning](http://arxiv.org/abs/2608.08214v1)
  <details><summary>📄 Abstract</summary>
  Inferring behavioural models from system executions is essential for supporting formal verification and analysis of complex, heterogeneous cyber-physical systems (CPS). Automata learning provides an effective way to infer state machine models from system executions. However, CPS inputs and outputs often consist of numeric time-series data, while automata learning algorithms assume inputs over a finite symbolic alphabet. As a result, raw numeric data must first be abstracted into a finite set of ...
  </details>

- **2026-08-08** — Zakhar Mrykhin, Valentin Malykh — [Prompt Embedding Probes (PEP): Hallucination Detection in LLMs from Hidden States](http://arxiv.org/abs/2608.08024v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate fluent and useful responses but remain prone to hallucinations. We introduce Prompt Embedding Probes (PEP), a white-box method for answer-level hallucination detection from the hidden states of a frozen LLM. PEP extends standard linear probes by augmenting the input with a small number of learnable prompt embeddings. We evaluate PEP on TriviaQA, GSM8K, and MedQA using Qwen3 models at multiple scales. PEP improves hidden-state-based detection over standar...
  </details>

- **2026-08-08** — Kutub Uddin, Nusrat Tasnim, Khalid Malik — [PE-Mamba: Bidirectional Selective Layer Aggregation for AI-Generated Image Detection](http://arxiv.org/abs/2608.07999v1)
  <details><summary>📄 Abstract</summary>
  AI-generated image (AIGI) detection has become increasingly challenging due to the rapid advancement of generative models and the diminishing gap between synthetic and authentic content. Existing vision transformer-based detectors commonly rely on weighted-sum strategies to aggregate intermediate representations across transformer layers, often overlooking the inherently ordered semantic progression of hierarchical features from shallow texture cues to deep semantic representations. In this work...
  </details>

- **2026-08-07** — Afreen Alam, Evgenija Popchanovska, Ana Gjorgjevikj et al. — [Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools](http://arxiv.org/abs/2608.07446v1)
  <details><summary>📄 Abstract</summary>
  Rapid adoption of large language models (LLMs) in enterprise settings has introduced operational, security, and governance risks. As generative AI applications move from pilot to production, manual harm identification and mitigation are becoming difficult to scale. Although many tools support model evaluation, adversarial testing, runtime guardrails, and observability, the tooling landscape remains fragmented. Tools are typically designed for specific engineering tasks and described in technical...
  </details>

- **2026-08-07** — Xiao Zhang, Yusheng Wang, Yuhao Fei et al. — [HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses](http://arxiv.org/abs/2608.06984v1)
  <details><summary>📄 Abstract</summary>
  Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present HarnessSafe, a benchmark ...
  </details>

- **2026-08-07** — Daniele Raimondi, Feichi Lu, Oliver Grun et al. — [SCALE: Scientific Concept Aggregation via LLMs and Embeddings for Fine-Grained Taxonomy Extension](http://arxiv.org/abs/2608.07254v1)
  <details><summary>📄 Abstract</summary>
  The increasing specialization of scientific research challenges existing classification systems, which provide effective representations of broad disciplines and research topics but often fail to capture the fine-grained conceptual structure of contemporary science. Author keywords offer greater specificity, but their fragmentation, redundancy, and terminological variability limit their use as stable units of knowledge organization. We introduce SCALE (Scientific Concept Aggregation via LLMs and...
  </details>

- **2026-08-07** — Francisco Caetano, Tim J. M. Jaspers, Haiko Middeljans et al. — [Representation-driven Endoscopic Visual Embedding Alignment for Latent Generation](http://arxiv.org/abs/2608.07176v1)
  <details><summary>📄 Abstract</summary>
  Developing foundation generative models for endoscopy is limited by the gap between natural and clinical images and the computational cost of training large Diffusion Transformers. Although representation alignment has improved efficiency in general computer vision, its role within the highly specialized endoscopic image space remains unclear. We introduce REVEAL (Representation-driven Endoscopic Visual Embedding Alignment), the largest generative foundation model for endoscopy to date, trained ...
  </details>

- **2026-08-07** — Bhavika Jalli, Nikhil Korati Prasanna, Jayanta Choudhury — [A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy Costs While Improving Accuracy](http://arxiv.org/abs/2608.07427v1)
  <details><summary>📄 Abstract</summary>
  LLM inference accounts for over 90% of AI operational energy, scaling directly with input token count---a critical inefficiency for telecom network analytics and numerical time-series data analysis (NTSDA), where raw multivariate KPI windows from 4G/5G cell sites expand into thousands of floating-point tokens. Vision-Language Models (VLMs) eliminate this mismatch by encoding time-series as 2D plots, achieving 3.6-10.4x input token reduction across Llama-3.2-90B, Qwen2.5-VL-72B, and Pixtral-12B a...
  </details>

- **2026-08-07** — Sumaiya Islam, Harsha Kumara Moraliyage — [PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery](http://arxiv.org/abs/2608.07126v1)
  <details><summary>📄 Abstract</summary>
  Most CubeSats, small and low-cost satellites roughly the size of a shoebox, do not survive as long as they were designed to: a study of 178 missions found that only 48-65% remain operational after two years, against a designed lifetime of 2-5 years. The deeper issue is that a CubeSat in low Earth orbit (LEO) is physically unreachable from the ground for roughly 85 minutes out of every 96-minute orbit, so faults that start during that window go unnoticed until the next contact pass, by which poin...
  </details>

- **2026-08-07** — Fabian Bongratz, Zhizheng Zhuo, Chao Zhang et al. — [International Transfer of Stochastic Cortical Self-Reconstruction](http://arxiv.org/abs/2608.07092v1)
  <details><summary>📄 Abstract</summary>
  Stochastic cortical self-reconstruction (SCSR) enables personalized mapping of gray matter atrophy, a hallmark of neurodegenerative disorders such as Alzheimer's disease (AD), onto high-resolution cortical surfaces. Unlike conventional normative modeling approaches, which typically operate at a coarse regional level and remain inherently constrained by the covariates included during training, SCSR estimates an individualized healthy reference directly from the observed cortical thickness at the ...
  </details>

- **2026-08-07** — Satoshi Hashimoto, Hitoshi Nishimura, Mori Kurokawa — [MuST-VAD: Mutual Structured Learning for Video Anomaly Detection](http://arxiv.org/abs/2608.06913v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose MuST-VAD, a mutual structured learning framework for weakly supervised video anomaly detection (VAD) in which an anomaly detector and a large vision-language model (LVLM) exchange their acquired knowledge. Detectors in weakly supervised VAD learn anomaly scores from features extracted by a fixed, task-agnostic backbone. These fixed features bound the achievable detection accuracy. Recent methods therefore transfer LVLM semantics into the detector as richer features. How...
  </details>

- **2026-08-06** — Jiacheng Wei, Zhaoxin Fan, Xin Wen et al. — [ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution](http://arxiv.org/abs/2608.05790v1)
  <details><summary>📄 Abstract</summary>
  General-purpose large language model agents have achieved strong performance on tool-augmented tasks, yet they rely on assumptions break down in blockchain environments. On-chain execution is stateful, adversarial, and economically irreversible, exposing three fundamental gaps: Reactivity, Irreversibility, and Observability. We propose ChainClaw, a blockchain-native agent framework built on OpenClaw, that addresses all three gaps through a layered architecture comprising an event-driven orchestr...
  </details>

- **2026-08-06** — Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra et al. — [AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks](http://arxiv.org/abs/2608.05507v1)
  <details><summary>📄 Abstract</summary>
  Speech deepfake detection (SDD) systems achieve strong performance on conventional benchmarks; however, existing datasets provide limited coverage of emotionally expressive and recent large audio-language model (LALM)-based attacks. Existing emotional spoofing datasets are also limited in scale and attack diversity, typically covering only voice conversion (VC) or text-to-speech (TTS) attacks. We introduce AffectDF, the most comprehensive benchmark for emotionally expressive speech deepfakes, sp...
  </details>

- **2026-08-06** — Massi-Nissa Abboud, Aladin Djuhera, Elena Cabrio et al. — [Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts](http://arxiv.org/abs/2608.06123v1)
  <details><summary>📄 Abstract</summary>
  Measuring political bias in large language models (LLMs) remains challenging as it can manifest through subtle differences in framing, argumentation, and legal reasoning that are difficult to capture with a single metric. In this work, we introduce Poli-Bias, a counterfactual framework for measuring whether LLMs treat legally equivalent conflict scenarios differently depending on the countries involved. Poli-Bias compares responses to paired prompts in which country identities are systematically...
  </details>

- **2026-08-06** — R. P. Erickson — [A quantum framework for event graphs](http://arxiv.org/abs/2608.06058v1)
  <details><summary>📄 Abstract</summary>
  Graph representations of discrete events provide a natural foundation for machine-learning models of anomaly detection, yet they also suggest a deeper quantum description in which graph structure gives rise to interacting quantum degrees of freedom. We develop a quantum framework based on a directed participant graph whose edges represent events connecting pairs of source and destination vertices. A line-graph transformation maps each event to a node of a bidirectional event graph, whose edges i...
  </details>

- **2026-08-06** — Jiale Han, Xiang Li, Jing Qian et al. — [From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models](http://arxiv.org/abs/2608.06020v1)
  <details><summary>📄 Abstract</summary>
  Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as generative engines in which heterogeneous agents act, interact, adapt, and co-evolve with markets and institutions, thereby producing economic ...
  </details>

- **2026-08-06** — Mohammad Abboush, Hamza Ouarrad, Andreas Rausch — [Sensor-Level Fault Diagnosis for Automotive Software Validation Using Large Language Models](http://arxiv.org/abs/2608.05921v1)
  <details><summary>📄 Abstract</summary>
  The pre-series validation of automotive software on hardware-in-the-loop (HIL) platforms produces large volumes of multivariate sensor recordings whose assessment against functional safety requirements exceeds what manual review can sustain at campaign scale. Threshold-based tooling reports that a deviation has occurred but neither identifies its nature nor locates its source, while data-driven classifiers, although accurate, rely on large labelled datasets and return opaque decisions that sit u...
  </details>

- **2026-08-06** — Wenhao Lin, Chenyu Yu, Xingwei Lin et al. — [DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model](http://arxiv.org/abs/2608.05695v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents increasingly invoke external tools and interact with real-world systems, unsafe actions may cause irreversible consequences on external states, user data, and downstream services. Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory. This limitation creates a crit...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 64 papers

- **2026-08-10** — Yushun Tang, Yisen Cao, Zhicheng Chen et al. — [Entropy-based Code Adversarial Translation for Real-world Repository Migration](http://arxiv.org/abs/2608.09273v1)
  <details><summary>📄 Abstract</summary>
  LLMs have demonstrated strong capabilities in code generation and automated program repair, but migrating an entire repository rarely produces a runnable application because long-horizon translation challenges LLM-based agents' ability to maintain repository-level migration objectives. In this work, we propose Entropy-based Code Adversarial Translation (ECAT), a multi-agent framework for automated Android-to-HarmonyOS repository migration. ECAT formulates repository migration as adversarial entr...
  </details>

- **2026-08-10** — Igor Sterner, Mirella Lapata, Alex Lascarides et al. — [REFRAMED: Towards Realistic Audio Description Generation for Movies](http://arxiv.org/abs/2608.09765v1)
  <details><summary>📄 Abstract</summary>
  Audio Description (AD) is a verbal narration of key visual content in videos, enabling access for visually impaired audiences. Unlike standard video captioning, AD is a structured editorial task: descriptions must be inserted into gaps in dialogue and must convey only what is needed to understand the narrative being told. However, existing approaches formulate AD generation in an artificial setting where both the content and timing of descriptions are pre-specified, reducing the task to clip-lev...
  </details>

- **2026-08-10** — Dongxu Ge, Shansong Liu, Cheng Gong et al. — [Towards Expressive and Faithful Audio-to-Image Generation: A Unified Multimodal Dataset and Synthesis Framework](http://arxiv.org/abs/2608.09529v1)
  <details><summary>📄 Abstract</summary>
  As an important subfield of cross-modal generation, synthesizing static visual content in the form of images from audio, namely audio-to-image (A2I) generation, has attracted increasing research attention in recent years. Nevertheless, despite the remarkable visual quality of modern text-to-image (T2I) models, the performance of A2I remains fundamentally limited by traditional datasets, which often lack both high-fidelity images and precise cross-modal alignment. As a result, existing methods st...
  </details>

- **2026-08-10** — Xiaocheng Lu, Huabin Liu, Song Guo et al. — [Reducing Pretraining-Generation Mismatch in Diffusion Language Models](http://arxiv.org/abs/2608.09424v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive language models align training and use: generation conditions on a clean prompt, and training predicts future tokens from clean left context. Diffusion language models offer parallel denoising, but native dLLM pretraining can randomly corrupt prompt and continuation tokens together, weakening the clean-prefix interface needed for prompt-conditioned generation. We identify this mismatch for prompt continuation and propose PCD (Prefix-Conditioned Diffusion), a pretraining objective ...
  </details>

- **2026-08-10** — Bo Wang, Ruixing Zhang, Yunqi Liu et al. — [Intent Speaks Louder: Controllable User Simulation Beyond Response Imitation](http://arxiv.org/abs/2608.09420v1)
  <details><summary>📄 Abstract</summary>
  User simulators are widely used as scalable environments for training and evaluating interactive assistants. Generating the next user turn is inherently one-to-many: the same profile and dialogue context may support multiple plausible continuations with different local interaction intents. A fluent response may therefore advance the dialogue through an inappropriate intent, such as acceptance rather than repair. Our key insight is that controllable user simulation should separate which local int...
  </details>

- **2026-08-10** — Yang Shi, Liangsi Lu, Minzhe Guo et al. — [Diffusion Image Editing via Asynchronous Token Decoding](http://arxiv.org/abs/2608.09322v1)
  <details><summary>📄 Abstract</summary>
  Text-guided diffusion image editing aims to modify semantic attributes of an image while preserving its identity, layout, and background. However, naïvely switching the text condition during sampling often causes global drift, as denoising dynamics propagate changes across tokens and can disrupt unedited regions. To address this issue, we propose \textbf{A}synchronous \textbf{T}oken \textbf{D}ecoding \textbf{Edit} (ATDEdit), an inference-time framework that views each sampler step as a parallel ...
  </details>

- **2026-08-10** — Zhuo Song, Lian Xu, Runqing Jiang et al. — [Warp-free Cross-view Geo-localization via Feature-space Consensus Mining](http://arxiv.org/abs/2608.09321v1)
  <details><summary>📄 Abstract</summary>
  Cross-view geo-localization is challenging due to drastic viewpoint changes and large appearance discrepancies between street-level and satellite imagery. Although existing methods often use geometric warping to expose co-visible cues, such transformations rely on restrictive spatial assumptions and inevitably introduce severe visual distortions under view-dependent visibility, yielding noisy supervision and fragile correspondences. To overcome this, we propose a novel joint-view consensus-guide...
  </details>

- **2026-08-10** — Yushun Tang, Weiming Chen, Siyi Liu et al. — [In-Loop Model Adaptation with Coupled Latent-Noise Guidance for High-Fidelity Subject-Driven Text-to-Image Generation](http://arxiv.org/abs/2608.09244v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models have achieved remarkable success in generating high-quality images from a given text prompt. Subject-driven generation aims to synthesize customized images to mimic the appearance of subjects in given reference images within different visual contexts specified by the text prompts. The central challenge here is that, when the reference image changes, the diffusion model cannot efficiently adapt to different visual contexts while consistently maintaining the subject ...
  </details>

- **2026-08-10** — Ruiyu Li, Haoyang Cai, Zhitong Guo et al. — [MELLON - Multimodal Enhanced LLM for Online Navigation](http://arxiv.org/abs/2608.09121v1)
  <details><summary>📄 Abstract</summary>
  Web navigation agents are capable of addressing various types of tasks on different websites. Current baselines on web navigation are either unimodal or lack strong reasoning abilities given multimodal inputs. Focusing on the WebShop benchmark, a real-world website simulation, we explore the alignment of text and images, as well as multimodal reasoning and planning abilities, to enhance the performance of web navigation agents. We propose three innovative multimodal enhancements: Multimodal Enha...
  </details>

- **2026-08-10** — Weixin Ye, Wei Wang, Hongguang Zhu et al. — [SI-Edit: Toward Sketch-Instruction Guided Local Image Editing with Pixel-Level Precision](http://arxiv.org/abs/2608.09097v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid advances in generative models, achieving pixel-level precision in sketch-based image editing remains a persistent challenge, particularly for fine-grained local deformations. This gap stems primarily from the critical shortage of high-quality, publicly available benchmark datasets that jointly provide geometric constraints and semantic instructions. To address this issue, we first introduce **SI-Data**, a high-quality dataset specifically designed for instruction-guided local sketc...
  </details>

- **2026-08-10** — Hongxiang Gao, He-yang Xu, Yuwen Li et al. — [Diagnosing as Cardiologists Do: ECG Agents with Doctor-Grounded Priors for Clinical Reasoning Across Diseases and Populations](http://arxiv.org/abs/2608.09053v1)
  <details><summary>📄 Abstract</summary>
  Cardiologists interpret electrocardiograms by localizing waveform components, measuring rhythm and interval patterns, and translating these structured observations into diagnostic evidence. Whether this expert reading process can serve as an effective prior for ECG agents remains unclear. To address this question, we introduce LuminaECG, a clinically structured ECG reasoning framework that reformulates ECG interpretation as measurement-grounded visual reading. ECG signals are rendered on standar...
  </details>

- **2026-08-10** — Xuanyu Liu, Zheng Fang, Hongyang He et al. — [Triple Expert Learning from Noisy Labels for Semi-Supervised Vision Foundation Model Adaptation](http://arxiv.org/abs/2608.09052v1)
  <details><summary>📄 Abstract</summary>
  Semi-supervised adaptation of vision foundation models (VFMs) commonly freezes the pretrained backbone and updates lightweight modules such as LoRA. However, pseudo-labels have mixed reliability, and a single LoRA adapter must absorb reliable, ambiguous, and noisy gradients in the same low-rank space. This can make VFM adaptation sensitive to pseudo-label noise. We propose \textbf{TriNoL}, a \textbf{Tri}ple-expert learning framework from \textbf{No}isy \textbf{L}abels for semi-supervised VFM ada...
  </details>

- **2026-08-10** — Ponkrit Kaewsawee, Chaklam Silpasuwanchai, Chutiporn Anutariya — [PolicyKG: An Agentic LLM Pipeline for Translating Institutional Policies into SHACL Knowledge Graphs](http://arxiv.org/abs/2608.09028v1)
  <details><summary>📄 Abstract</summary>
  Institutional policies stay in natural language while the systems that check compliance demand machine-readable constraints. Bridging that gap is still done by hand.   PolicyKG closes the loop. It is an LLM pipeline that reads a policy PDF, classifies each sentence as an obligation, permission, or prohibition, lifts the label into first-order deontic logic, and emits SHACL constraints. Four stages run on a LangGraph state machine with per-stage validators. The piece that matters most is the Corp...
  </details>

- **2026-08-10** — Ming Li, Chenguang Wang, Xirui Li et al. — [How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review](http://arxiv.org/abs/2608.08975v1)
  <details><summary>📄 Abstract</summary>
  As large language models increasingly participate in scientific evaluation, we investigate a potential form of reward hacking: how rhetorical choices shape AI-review judgments when reported scientific content is preserved and how these effects vary across evaluation conditions. We construct a controlled corpus of 4,200 full-paper manuscripts derived from 120 anonymized ICLR 2026 submissions. Two LLM rewriters transform six rhetorical dimensions in opposing directions, and five LLM reviewers eval...
  </details>

- **2026-08-09** — Chenglin Li, Yisen Xu, Zehao Wang et al. — [Independent Patch Verification for Coding Agents with a Bidirectional Reconstruct-and-Verify Framework](http://arxiv.org/abs/2608.08950v1)
  <details><summary>📄 Abstract</summary>
  Autonomous coding agents powered by large language models can now generate code patches directly from bug reports, but a fundamental gap remains: once a patch is produced, no mechanism independently verifies whether it truly resolves the reported problem. Prior work has sought to address this through iterative self-refinement and inference-time scaling, but these approaches either review the patch under the same interpretation that produced it or broaden candidate generation without verifying in...
  </details>

- **2026-08-09** — Natallia Kokash, Adam S. Z. Bellouma, Paola Grosso — [Biomedical Knowledge Composition: A Software Engineering Perspective](http://arxiv.org/abs/2608.08927v1)
  <details><summary>📄 Abstract</summary>
  Biomedical research has accumulated vast molecular, clinical, and population data, yet translating this wealth into actionable knowledge remains constrained by technical and organizational difficulties. This article presents a unified treatment of two perspectives on biomedical knowledge infrastructure. The first introduces the biomedical domain to software engineers: it explains why knowledge graphs (KGs) are the central integrative data structure in modern biomedicine, characterizes five data ...
  </details>

- **2026-08-09** — Muhammad Faishal Adly Nelwan, Alfan Farizki Wicaksono — [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](http://arxiv.org/abs/2608.08829v1)
  <details><summary>📄 Abstract</summary>
  Activation steering edits the behaviour of a frozen language model by adding a learned vector to its residual stream, and current practice fixes the injection layers globally per task. We argue that the best layers are an instance-level decision, and we make per-instance, multi-layer selection both well understood and deployable. On two open-weight 8B models and six binary persona traits, a per-instance oracle over layer subsets shows that the best layers vary from one input to the next: on most...
  </details>

- **2026-08-09** — Jinhong Zhu, Weiqi Yan, Shengchuan Zhang et al. — [LASA: Language-and-Source-Anchored Alignment for Domain Generalized Semantic Segmentation](http://arxiv.org/abs/2608.08805v1)
  <details><summary>📄 Abstract</summary>
  Domain Generalization Semantic Segmentation (DGSS) focuses on generalizing knowledge from labeled source domains to unseen target domains where data is unavailable during the training phase. While conventional methods utilize style randomization or feature normalization to mitigate domain shifts, they often impair feature integrity. Specifically, style randomization distorts the underlying feature manifold due to its coarse-grained nature, while feature normalization suppresses discriminative, d...
  </details>

- **2026-08-09** — Kaili Zheng, Kaiwen Wang, Xun Zhu et al. — [FitAQA: A Benchmark of Fitness Action Quality Assessment for Multimodal Large Language Models](http://arxiv.org/abs/2608.08736v1)
  <details><summary>📄 Abstract</summary>
  Fitness Action Quality Assessment (AQA) is important for intelligent sports training, yet the capabilities of Multimodal Large Language Models (MLLMs) in this setting remain underexplored. Existing benchmarks rely on action-specific annotation schemes and focus primarily on final assessment outputs, offering limited insight into how models assess exercise quality. We introduce FitAQA, a systematic benchmark for evaluating MLLMs in fitness AQA, containing 2,219 videos and 5,512 QA instances acros...
  </details>

- **2026-08-09** — Gabriele La Malfa, Lakmal Meegahapola, Edyta Bogucka et al. — [Unaccountable Delegation, Fading Skills: Mapping the Risks of Workplace AI Agents](http://arxiv.org/abs/2608.08601v1)
  <details><summary>📄 Abstract</summary>
  To anticipate socio-technical risks from AI agents, organizations need taxonomies to classify them. However, existing AI risk taxonomies focus on broad risks and do not capture job-specific risks introduced by agents. To address this gap, we make three main contributions. First, we developed a multi-layer framework from a literature review of AI agents. The framework models three core components and their interactions: agents, goals, and environment. Second, we embedded this framework in a struc...
  </details>

- **2026-08-09** — Fangdi Li, Juncheng Liao, Changxu Cheng et al. — [Goal-oriented Navigation Instruction Generation with Tour Video Priors](http://arxiv.org/abs/2608.08596v1)
  <details><summary>📄 Abstract</summary>
  Navigation Instruction Generation (NIG) aims to produce step-by-step natural language instructions for navigation guidance. Existing studies primarily treat NIG as an auxiliary task for vision-andlanguage navigation (VLN), focusing on data augmentation or multi-task learning. However, generating navigation instructions from compact environmental priors requires meticulous spatial reasoning, especially when the target route does not simply follow the demonstrated tour, and remains challenging for...
  </details>

- **2026-08-09** — Omer Yom Tov, Avigdor Gal — [Neural Message Passing on Structural Interaction Graphs for Fully-Inductive Graph Neural Networks](http://arxiv.org/abs/2608.08567v1)
  <details><summary>📄 Abstract</summary>
  A central obstacle in building graph foundation models is the input heterogeneity in terms of feature space dimensionality, semantics, and structure. Such heterogeneity limits the capability of graph neural networks to generalize to new graphs with unseen feature spaces. We address the transferability challenge with SIGIL, a framework that maps any attributed graph to a unified representation space of fixed dimension. Given a graph, SIGIL lifts it to a structural interaction graph, where nodes a...
  </details>

- **2026-08-09** — Rong Fu, Chunlei Meng, Yangchen Zeng et al. — [MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling](http://arxiv.org/abs/2608.08553v1)
  <details><summary>📄 Abstract</summary>
  Video super-resolution (VSR) aims to recover high-fidelity high-resolution videos from low-resolution inputs and is central to applications ranging from mobile capture to streaming and archival restoration. Existing approaches trade off among local-detail fidelity, long-range spatio-temporal modeling, perceptual realism, and efficiency: convolutional alignment techniques preserve local structure but suffer when motion is large or degradations are complex; transformer-based methods capture long-r...
  </details>

- **2026-08-09** — Qiang Hu, Yuxuan Luo, Yingjie Guo et al. — [Linguistically-Aligned and Visually-Grounded Preference Optimization for Clinically-Augmented Medical Report Generation](http://arxiv.org/abs/2608.08494v1)
  <details><summary>📄 Abstract</summary>
  Despite significant advances in Medical Report Generation (MRG), the reliability remains constrained by the prevalence of factual errors. While Direct Preference Optimization (DPO) has emerged as a promising post-training paradigm to enhance the performance of Supervised Fine-Tuned (SFT) MRG models, existing DPO-based MRG methods typically adopt a naive preference construction that directly pairs model-generated reports with ground truth reports. This strategy inadvertently entangles critical cl...
  </details>

- **2026-08-09** — Yidong Wang, Yan Zhan, Ziteng Feng et al. — [TrustRoboReward: Preference-Ordered Isotonic Score Editing for Multi-Paradigm Robot Reward Models](http://arxiv.org/abs/2608.08491v1)
  <details><summary>📄 Abstract</summary>
  Reward models are a bottleneck for reinforcement learning in embodied AI. Long-horizon robotic manipulation requires scalable vision feedback beyond handcrafted rewards or task-specific annotations. Existing open-source VLM reward judges like RoboReward adopt simple 1--5 trajectory progress scoring, lacking pairwise preferences for RLHF, DPO and Bradley-Terry frameworks, while failing to optimize video scene understanding. Augmenting RoboReward with pairwise comparison and video-QA supervision c...
  </details>

- **2026-08-09** — Zecheng Ren, Yafei Hu, Jianing Zhao et al. — [RenderMatte: Exact-Alpha Rendering and Group-Relative Alignment for Image Matting](http://arxiv.org/abs/2608.08487v1)
  <details><summary>📄 Abstract</summary>
  Image matting is an essential enabling technology for modern visual content production, where foreground extraction determines the realism and editability of downstream creation workflows. However, precise alpha estimation in open-world scenes remains challenging because real foregrounds exhibit highly diverse appearances and opacity patterns. This makes existing methods struggle with semantic ambiguity and fine-grained opacity variation, especially in sparse boundary regions that are fragile an...
  </details>

- **2026-08-09** — Xianghan Meng, Wei He, Zhiyuan Huang et al. — [Learning Deep Modality-Shared Self-Expressiveness for Image Clustering with Textual Information](http://arxiv.org/abs/2608.08418v1)
  <details><summary>📄 Abstract</summary>
  Leveraging textual information for image clustering has emerged as a promising direction, largely owing to the powerful representations learned by Vision-Language Models (VLMs). Existing approaches typically retrieve a textual counterpart for each image and then refine multimodal representations by directly enforcing cross-modal agreement, e.g., maximizing image-text similarity inherited from pretrained VLMs. However, such a strategy aligns heterogeneous representations across modalities without...
  </details>

- **2026-08-08** — Aleksei Velsh, Nenad Petrovic, Alois Knoll — [Stateful Multi-Agent LLMs for Cross-View Interface Alignment in Automotive Model-Based Systems Engineering](http://arxiv.org/abs/2608.08038v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) can accelerate Model-Based Systems Engineering (MBSE) for software-defined vehicles, their probabilistic nature causes "architectural drift", fabricating interfaces in behavioral views that lack structural foundations. To enforce deterministic interface alignment, we propose a stateful, multi-agent validation pipeline. The framework utilizes a sequential generation matrix (Class->Activity->Sequence) and Vehicle Signal Specification (VSS)-grounded Retrieval-Augm...
  </details>

- **2026-08-08** — Yifan Li, Ruxin Sun, Tongzhou Zhao — [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](http://arxiv.org/abs/2608.08326v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective approach for improving multimodal reasoning. However, most existing methods evaluate an entire response using a binary reward based only on final-answer correctness, thereby discarding the supervision available in intermediate reasoning steps. Process reward models offer finer-grained feedback, but they typically rely on separately trained verifiers, costly chain-of-thought annotations, or online judging by large l...
  </details>

- **2026-08-08** — Chan Aristella Lu, Arya Fayyazi, Junhao Zhang et al. — [Fair on the Surface? Benchmarking Hidden-Output Fairness Gaps in LLM Recommenders](http://arxiv.org/abs/2608.08284v1)
  <details><summary>📄 Abstract</summary>
  Fairness audits for LLM-based recommenders have largely focused on observable outputs, implicitly assuming that stable recommendations reflect stable internal processing. We challenge this assumption with FairGap, the first benchmark to jointly evaluate recommendation fairness at two levels: observable output shift (OBS) and hidden representation shift (IBS), measured through controlled counterfactual identity probes across gender, age, and race. Their relationship is summarized via Representati...
  </details>

- **2026-08-08** — Aleks Knoks, Marija Slavkovik — [Metanormative Theory for RL-Based Moral Agents](http://arxiv.org/abs/2608.08220v1)
  <details><summary>📄 Abstract</summary>
  The overlapping disciplines of machine ethics and value alignment are concerned with designing artificial agents that are aligned with human values and that act in ethically acceptable ways. A recent trend in these disciplines is the use of reinforcement learning (RL) to design such agents, sidelining the philosophical literature that used to play a more central role. Against this backdrop, this paper pursues two goals. The first is to draw out ideas from recent work in metanormative theory that...
  </details>

- **2026-08-08** — Kaiming Liu, Fuwen Luo, Ziyue Wang et al. — [Illusion of Alignment: Detecting Hidden Disagreement in Collaborative Dialogue](http://arxiv.org/abs/2608.08210v1)
  <details><summary>📄 Abstract</summary>
  Collaborative dialogue can end with apparent agreement while participants still differ on goals, assumptions, or execution plans, creating an \textbf{illusion of alignment (IoA)}. A real-user study across 18 meetings confirms that IoA arises routinely in human collaboration. Yet IoA poses a paradox: if participants were aware of such disagreements, they would already be explicit; if not, they cannot articulate them when asked, leaving IoA invisible to both participants and observers. In this wor...
  </details>

- **2026-08-08** — Yutong Wu, Xiaofan Bai, Shixin Li et al. — [Targeted Counterfactual Fingerprinting for Black-Box LLM Ownership Verification](http://arxiv.org/abs/2608.08195v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are high-value assets that can be derived through redeployment, fine-tuning, quantization, or further alignment. Because deployed LLMs are commonly exposed only through query APIs, ownership verification must often rely on black-box text responses. This setting is difficult: generations are open-ended and can vary across repeated queries, while existing black-box fingerprints rely on signals that are fragile under a final-response interface, including full-text match...
  </details>

- **2026-08-08** — Ronghua Xu, Kepha Barasa, Manoj Kumal et al. — [Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform forHigh Dose Rate (HDR) Brachytherapy](http://arxiv.org/abs/2608.08163v1)
  <details><summary>📄 Abstract</summary>
  The convergence of the Metaverse and Large Language Model (LLM)-based AI agent is catalyzing a shift toward autonomous, immersive, and personalized pedagogical frameworks in medical education. This paper presents a novel agentic AI-driven immersive simulation specifically designed for High Dose Rate (HDR) vaginal cylinder (VC) brachytherapy in cancer care. By integrating Virtual Reality (VR) and mobile computing, the system establishes a high-fidelity, risk-free environment that allows trainees ...
  </details>

- **2026-08-08** — Gabriele La Malfa, Nitay Alon, Emanuele La Malfa et al. — [Explore, Map, Remember, Decide: Are Embodied VLMs Ready for Safety-Critical Scenarios?](http://arxiv.org/abs/2608.08077v1)
  <details><summary>📄 Abstract</summary>
  Theory of Space framework (ToS) assesses the spatial understanding of curiosity-driven Vision-Language Models (VLMs) under partial observability. As AI techniques are increasingly applied to safety-critical scenarios, it is crucial to understand whether VLMs possess robust spatial memory and make reliable decisions. In this paper, we assess whether VLMs' decisions are based on physical evidence or are corrupted by visual-language biases, if their memory processes align with human cognitive patte...
  </details>

- **2026-08-08** — Xiaowen Jian, Xinyi Mou, Daisong Gong et al. — [Representational Equality in Cross-country Value Simulation: A Systematic Analysis of Large Language Models](http://arxiv.org/abs/2608.08058v1)
  <details><summary>📄 Abstract</summary>
  Traditional methods for studying human opinions often struggle to support representative and scalable research across countries. Large language models (LLMs) can serve as scalable proxies for simulating human opinions, enabling more efficient opinion analysis. However, this use of LLMs requires not only high average accuracy but also representational equality, that is, comparable simulation accuracy across populations. Uneven simulation accuracy may reproduce or amplify societal biases in downst...
  </details>

- **2026-08-08** — Pengxiang Cai, Xiaohan Li, Anglin Liu et al. — [JustLLMGRPO: Radiographic Control for Chest X-Ray Generation](http://arxiv.org/abs/2608.08046v1)
  <details><summary>📄 Abstract</summary>
  Text-conditioned chest X-ray generation aims to synthesize realistic radiographs that faithfully depict specified findings. Existing work has primarily improved quality by updating image generators, implicitly treating prompts as fixed after CXR-domain adaptation. We show that this generator-centric view leaves a substantial optimization dimension underexplored. With a CXR-adapted Sana generator frozen, one-pass reformulation by an unmodified LLM reduces RadDINO-FID from 54.225 to 27.572. Prompt...
  </details>

- **2026-08-08** — Fulong Liu, Liang Xu, Chengqun Yang et al. — [MRBench: A Comprehensive Benchmark for Human Motion-Text Retrieval](http://arxiv.org/abs/2608.07993v1)
  <details><summary>📄 Abstract</summary>
  Human motion-text retrieval provides a rigorous means of assessing cross-modal alignment. Prevailing benchmarks are dominated by homogeneous indoor motions, imbalanced motion distributions, and oversimplified, repetitive texts, which hinder the reliable measurement of cross-domain and cross-granularity alignment. We thus introduce MRBench, a comprehensive motion-text retrieval benchmark featuring heterogeneous motions, broad and balanced category coverage, and reliable, discriminative, multi-gra...
  </details>

- **2026-08-08** — Ivan Hornung, Deepthi Marasinghe Arachchige, Tharindu Kumarage et al. — [CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity](http://arxiv.org/abs/2608.07965v1)
  <details><summary>📄 Abstract</summary>
  Gamification is especially effective in learning domains requiring active problem-solving and iterative skill-building, such as cybersecurity education. Generative AI agents offer a path to delivering such experiences adaptively at scale, but introduce well-documented risks in educational settings: inconsistent behavior, hallucinated reasoning, and misalignment with pedagogical frameworks. Grounding these systems in learning science is therefore essential. We present \model, an agentic framework...
  </details>

- **2026-08-08** — Junfei Ling, Bangzheng Pu, Bingsen Xue et al. — [DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology](http://arxiv.org/abs/2608.08148v1)
  <details><summary>📄 Abstract</summary>
  Attention mechanisms have been widely utilized in modern deep learning, and many existing multi-omics models inherit their conventional use to allow unrestricted bidirectional interactions. However, the fundamental logic of life is directional. Existing designs often overlook the directionality suggested by the central dogma, potentially limiting transfer across heterogeneous cancers, downstream tasks, and incomplete modality settings.In this work, we present DoGMA, a central-dogma-guided founda...
  </details>

- **2026-08-07** — Youjun Zhao, Alex Warren, Gary K. L. Tam et al. — [MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](http://arxiv.org/abs/2608.07463v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis. However, generating mirror reflections remains challenging because the content within a mirror must remain consistent with the surrounding scene. Existing VDMs are not specifically designed to model scene-to-mirror relationships, which can lead to reflections with incorrect content or inconsistent spatial arrangements. We observe that mirror reflection generation involves two complementary challenges: de...
  </details>

- **2026-08-07** — Ruochen Jin, Zhanliang Wang, Zongyu Dai et al. — [Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration](http://arxiv.org/abs/2608.07419v1)
  <details><summary>📄 Abstract</summary>
  Preference alignment often makes large language models (LLMs) overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent: a temperature fitted on one domain does not generalize across domains. This motivates us to modify model parameters during training to improve calibration. We propose maximizing the entropy of predictive distributions as the calibration objective, which directly targets overconfidence by discouraging overly concentrated predic...
  </details>

- **2026-08-07** — Maria-Louisa Wightman, Guillaume Bied, Tijl De Bie — [People Are Not Just Their Countries. Disentangling Social Determinants of LLM Value Alignment Across Europe](http://arxiv.org/abs/2608.07367v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly used as a primary source of information and advice, understanding their alignment to humans in terms of values becomes a pressing concern. A growing literature has leveraged large scale surveys to investigate to what extent LLMs' and humans' stated values and opinions align. With limited exceptions, studied populations have been defined country borders or cultural bounds. Yet, this focus neglects the role that socio-demographic divides may play fo...
  </details>

- **2026-08-07** — Jingkai Ying, Zhijin Qin, Yuan Shen et al. — [Token Communication for Multimodal Large Language Model](http://arxiv.org/abs/2608.07279v1)
  <details><summary>📄 Abstract</summary>
  With the broad success of the Transformer architecture, token is becoming a new basic information processing unit. This trend is especially evident in multimodal large language models (MLLMs), where both visual and textual information are represented and processed as tokens. With the rapid deployment of MLLMs, the efficient transmission of tokens has become increasingly important. This paper investigates how to reduce the amount of transmitted data during interactions with MLLMs while preserving...
  </details>

- **2026-08-07** — Yang Shen, Chonghao Cheng, Ziyi Zhao et al. — [Representation Handoffs for OpenArm-Based Laboratory Mobile Manipulation](http://arxiv.org/abs/2608.07154v1)
  <details><summary>📄 Abstract</summary>
  Open-source robotics and foundation models have lowered the barrier to embodied AI, yet language-guided laboratory automation still requires reliable alignment from instructions and observations to safe actions. This field report presents an OpenArm-based mobile manipulation prototype for laboratory-style tasks, built by integrating dual OpenArm manipulators with a mobile base, vertical slide, RGB-D sensing, lidar-based mapping, ROS2/MoveIt execution, and profile-defined skill interfaces. The sy...
  </details>

- **2026-08-07** — Nuria Alabau-Bosque, Jorge Vila-Tomás, Paula Daudén-Oliver et al. — [Human-AI Perceptual Alignment by Playing Hues and Cues](http://arxiv.org/abs/2608.07141v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the perceptual alignment between Contrastive Vision-Language Models (CVLMs) and humans is typically constrained by traditional benchmarks that overlook fine-grained semantic and cultural nuances. In this work, we propose a novel evaluation framework that leverages the gamified, discrete color space of the board game Hues and Cues. By mapping the board's 480 color cells to the CIE xy chromaticity diagram, we calculate empirical perceptual distances across a carefully curated 100-word v...
  </details>

- **2026-08-07** — Zhiyuan Liu, Tinghong Ye, Chenghao Liu et al. — [MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents](http://arxiv.org/abs/2608.07068v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations. Learning what to retain typically relies on proximal policy optimization (PPO) with final task rewards, but sparse rewards provide little guidance for individual memory updates. This limitation motivates on-policy distillation (OPD), which supplies dense teacher supervision on st...
  </details>

- **2026-08-07** — Ivan Majic, Zexian Huang, Franziska Hübl et al. — [LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents](http://arxiv.org/abs/2608.06948v1)
  <details><summary>📄 Abstract</summary>
  AI models are becoming increasingly adept at understanding and processing spatial information, thereby facilitating agentic problem-solving in spatial tasks and workflows. However, most of the research on their spatial capabilities (e.g., spatial reasoning) has focused on the textual modality as input and output. This contrasts with the human approach to GIS workflows, where text and visual modalities are often used together, interchangeably, and in a complementary manner. Thus, to truly achieve...
  </details>

- **2026-08-07** — Wanshu Fan, Yunzhe Zhang, Yue Shen et al. — [Degradation-Aware Prompt Learning with Cross-Modal Compensation for Adverse Weather Removal](http://arxiv.org/abs/2608.06939v1)
  <details><summary>📄 Abstract</summary>
  Adverse weather causes diverse and complex image degradations, severely compromising the reliability of computer vision systems. Existing all-in-one restoration models attempt to address multiple degradation types within a unified framework, but often lack explicit spatial and semantic modeling of degradation characteristics, limiting their adaptability to diverse weather conditions. To address this limitation, we propose a Degradation-Aware Cross-Modal Prompt Compensation Network (DCMPC-Net) th...
  </details>

- **2026-08-07** — Zihao Zheng, Xuenan Xu, Jiahao Mei et al. — [MMAG: A Multi-Control Mixed Audio Generation Benchmark](http://arxiv.org/abs/2608.06900v1)
  <details><summary>📄 Abstract</summary>
  Recent audio generation systems have progressed from single-modality synthesis to generating complex acoustic scenes containing speech, music, and sound effects. Therefore, evaluating these models requires assessing multiple interacting capabilities, including semantic fidelity, speaker consistency, and temporal control, yet existing benchmarks focus on isolated domains or coarse-grained descriptions. To address this gap, we introduce the Multi-control Mixed Audio Generation (MMAG) benchmark. MM...
  </details>

- **2026-08-06** — Tao Wang, Qihao Yang, Rongjiao Liang et al. — [Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard Documents](http://arxiv.org/abs/2608.06312v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly support complex professional tasks, yet their capabilities in rule-intensive document review remain insufficiently evaluated. National standard documents, such as China GB/T standards, offer a representative testbed: they are lengthy, highly structured, and governed by explicit rules for scope, terminology, normative wording, and cross-section consistency. Existing benchmarks focus on domain knowledge and question answering, largely overlooking intrinsic...
  </details>

- **2026-08-06** — Fardin Afdideh, Fernando Seoane, Farhad Abtahi — [A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance](http://arxiv.org/abs/2608.06246v1)
  <details><summary>📄 Abstract</summary>
  Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragmented across technique families, model classes, and deployment contexts, making it difficult to compare methods or describe how a trained model has been modified. This survey synthesiz...
  </details>

- **2026-08-06** — Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng et al. — [EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](http://arxiv.org/abs/2608.06231v1)
  <details><summary>📄 Abstract</summary>
  Emotion shapes how viewers interpret a scene, yet existing video generators entangle global atmosphere, affect-bearing semantic cues, and temporal progression within a single text condition. We present EmoWorld, a framework that decouples these factors within a frozen flow-matching video diffusion transformer (Video DiT). A one-time preparation stage extracts layer-specific affect directions and a reusable cue library from geometry-preserving neutral and emotion-edited panoramas. At inference, V...
  </details>

- **2026-08-06** — Hoda Fakharzadehjahromy, Emil Wiman, Andreas Bueff et al. — [SAGA: Score-Weighted Adaptive Generation Alignment for Low-Resource Nordic Language Models](http://arxiv.org/abs/2608.06179v1)
  <details><summary>📄 Abstract</summary>
  Preference optimisation has proven effective for improving large language models but typically relies on costly human preference annotations. Extending these methods to morphologically rich, low-resource languages remains challenging because such annotations are scarce. We present SAGA (Score-weighted Adaptive Generation Alignment), a parser-guided preference optimisation framework that replaces human labels with dependency-parser supervision. SAGA converts parser judgements into preference pair...
  </details>

- **2026-08-06** — Giorgio Tonetti, Laurent Kneip, Abel Gawel et al. — [Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments](http://arxiv.org/abs/2608.06170v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical 3D scene graphs are a promising representation for high-level spatial reasoning in autonomous mobile platforms. However, existing extraction frameworks typically rely on purely local visual clustering or strict geometric heuristics, such as wall-separated rooms, which fail in open-plan or arbitrarily-structured environments. We propose Prior-SG, a task- and prior-driven framework that casts scene graph generation fundamentally as a probabilistic alignment problem. As the robot explo...
  </details>

- **2026-08-06** — Xingyu Guo, Wei Chen, Linlin Yang et al. — [Contextual Information Policy Optimization for Search Agents](http://arxiv.org/abs/2608.06128v1)
  <details><summary>📄 Abstract</summary>
  Search agents extend large language models beyond static parametric memory by enabling them to acquire and use ex ternal evidence during multi-step reasoning. For knowledge intensive tasks involving complex or evolving information, their reliability depends not only on retrieving relevant ev idence but also on using it to guide subsequent reasoning. However, existing methods primarily reward final-answer cor rectness or intermediate progress, without directly assessing whether post-retrieval act...
  </details>

- **2026-08-06** — Pranav Dahiya — [Mind the Gaps: Mixture-of-Minds for Human Simulation](http://arxiv.org/abs/2608.06115v1)
  <details><summary>📄 Abstract</summary>
  Predicting how a population will answer a new question is a long-standing goal. Statistical methods succeed at the level of the mass but falter at the level of the individual. Large language model simulators inherit this gap. They recover a population's central tendencies while flattening its heterogeneity, and they carry social biases and prompt brittleness that distort individual predictions. This paper introduces Anacreon, an audience simulation model that targets the individual level within ...
  </details>

- **2026-08-06** — He Kong, Zengjue Chen, Qi Wang et al. — [Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation](http://arxiv.org/abs/2608.05999v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have demonstrated remarkable capabilities in robotic manipulation by leveraging pretrained vision-language models. However, existing post-training methods predominantly optimize VLA models as flat policies, making it difficult to explicitly model task progression and perform robust long-horizon manipulation. Although hierarchical approaches introduce task decomposition, they mainly rely on supervised learning from offline demonstrations and cannot effectively ...
  </details>

- **2026-08-06** — Taolin Zhang, Weizi shao, Zijie Zhou et al. — [M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent Retrieval-Augmented Generation](http://arxiv.org/abs/2608.05967v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-modal retrieval-augmented generation (mRAG), which augments multi-modal large language models (MLLMs) with external knowledge, have shown that collective intelligence from multiple agents can outperform a single model through effective communication. Despite their strong performance, existing multi-agent systems incur substantial token overhead and computational cost, posing challenges for large-scale deployment. To address these issues, we propose a Multi-Modal Multi-ag...
  </details>

- **2026-08-06** — Maulik Chevli, Johannes Brandt, Rickmer Braren et al. — [Big, Bright, or Invisible: A Frozen-Feature Benchmark of 3D CT Foundation Models](http://arxiv.org/abs/2608.05960v1)
  <details><summary>📄 Abstract</summary>
  Routine CT interpretation is inherently comprehensive, capturing incidental findings across the entire scan volume. 3D CT foundation models could assist this process by providing generalizable representations of anatomy and pathology. To evaluate their diagnostic breadth, we benchmark ten frozen CT encoders across three cohorts of thoracic CT scans, including an unseen internal clinical dataset, using $k$-nearest neighbors, zero-shot prompting, and linear probing. We find no universal state-of-t...
  </details>

- **2026-08-06** — Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian — [CourseGraph: Finding overlaps and differences in Computer Science courses across universities](http://arxiv.org/abs/2608.05910v1)
  <details><summary>📄 Abstract</summary>
  Student mobility programs such as Erasmus+ enable students to take courses at other universities, broadening their academic and cultural horizons. However, this flexibility also leads to a practical challenge: ensuring that students do not take courses elsewhere that substantially overlap with courses in their home curriculum. In this work, we propose CourseGraph, a methodology that automates the evaluation of external courses based on insights obtained from the process followed by curriculum ad...
  </details>

- **2026-08-06** — Yushe Cao, Shikun Feng, Fei Shen et al. — [UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](http://arxiv.org/abs/2608.05745v1)
  <details><summary>📄 Abstract</summary>
  Video Virtual Try-On (VVT) synthesizes a video of a person wearing a target garment while preserving identity, motion, and scene dynamics. Dominant approaches cast VVT as mask-conditioned video inpainting and rely on separate modules for human parsing, pose estimation, and garment warping. This multi-stage design complicates deployment and, more critically, allows errors in explicit geometric priors to propagate irreversibly into the generated video. We present UniVVT, a unified end-to-end frame...
  </details>

- **2026-08-06** — Mehrshad Saadatinia, Parsa Razmara, Ardalan Aryashad et al. — [CircuitSteer: Geometrically Aligned Multi-Layer Steering via Sparse Autoencoder Circuits](http://arxiv.org/abs/2608.05732v1)
  <details><summary>📄 Abstract</summary>
  Controlling the behavior of large language models (LLMs) remains a critical challenge for AI alignment. Existing steering methods, such as Contrastive Activation Addition (CAA), typically rely on fixed single-layer interventions derived from aggregate activation differences. These methods impose a single intervention across semantically diverse inputs and often fail to sustain consistent behavioral changes across layers, limiting the effectiveness of the steering. In this work, we introduce Circ...
  </details>

- **2026-08-06** — Yuma Asato, Kiyoaki Shirai, Natthawut Kertkeidkachorn — [Mitigating Scoring Bias in LLM-as-a-Judge via Random Number Generation](http://arxiv.org/abs/2608.05726v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are often used as evaluators of text quality, known as LLM-as-a-Judge, which can outperform conventional automatic evaluation metrics that rely on reference texts. However, LLM evaluators tend to generate particular scores regardless of the context of the evaluated text, which is known as scoring bias. This study proposes a novel method to mitigate this scoring bias. An LLM is instructed to randomly generate number tokens, and the latent numerical bias of the LLM is ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 71 papers

- **2026-08-10** — Yangfan Wu, Haozhe Wang, Huanyu Yang et al. — [SpecPath: Testing Coding Agents Across Contract-Equivalent Specification Histories](http://arxiv.org/abs/2608.09799v1)
  <details><summary>📄 Abstract</summary>
  Modern coding agents increasingly appear capable of following complex software requirements, yet their success leaves a critical ambiguity: do they resolve the active specification, or merely follow the most salient path by which it was stated? We identify specification-path sensitivity, a failure mode in which requirement histories that are equivalent in their final meaning lead the same agent system to produce behaviorally different programs. This reframes evolving-requirement evaluation as ac...
  </details>

- **2026-08-10** — Yen-Shan Chen, Yu Chian Duan, Chih-En Kuo et al. — [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](http://arxiv.org/abs/2608.09638v1)
  <details><summary>📄 Abstract</summary>
  Theory of Mind (ToM) is essential for agent interactions, yet existing evaluations either rely on static scenarios that oversimplify mental-state reasoning or interactive settings that provide limited diagnostic insight. We present Avalon-ToM-Bench, a fine-grained benchmark that operationalizes ToM through the asymmetric-information mechanics of The Resistance: Avalon. Rather than evaluating end-to-end gameplay, it decomposes ToM into a 2$\times$2 taxonomy -- epistemic versus motivational reason...
  </details>

- **2026-08-10** — Chencheng Zhu, Xiaoyang Li, Taotao Cai — [When Do Task Vectors Interfere? Mapping the Validity Boundaries of Weight-Space Composition](http://arxiv.org/abs/2608.09490v1)
  <details><summary>📄 Abstract</summary>
  Task arithmetic treats fine-tuning displacements as composable directions in weight space, yet it remains unclear when parameter addition reflects predictable changes in model function. We separate parameter geometry from functional geometry and measure pairwise functional non-additivity over a two-dimensional task-vector surface, using a first-token predictive-distribution interaction ratio conditioned on an input distribution and evaluated with norm-matched controls, three training seeds, and ...
  </details>

- **2026-08-10** — Ali Cheraghian, Hamidreza Dastmalchi, Hamed Barzamini et al. — [Beyond Global Editing: Per-Instance Disentangled Subspaces for Training-Free Hallucination Mitigation in LVLMs](http://arxiv.org/abs/2608.09344v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large vision-language models (LVLMs) have enabled powerful multimodal reasoning by integrating visual encoders with large language models (LLMs). However, their reliability is frequently undermined by hallucinations, where generated text inaccurately describes the visual input. Although fine-tuning can mitigate this problem, it is computationally expensive and requires large, curated datasets, making training-free alternatives attractive. Among these, model editing is more pro...
  </details>

- **2026-08-10** — Ziyi Song, Chen Xia, Hang Yu et al. — [DH-VLM: Dual-Horizon Cooperative Latent Reasoning for Autonomous Driving](http://arxiv.org/abs/2608.09333v1)
  <details><summary>📄 Abstract</summary>
  Large-scale language models for autonomous driving enable enhanced global understanding and long-horizon planning. However, when deployed in isolated vehicles, limited sensing range and occlusions restrict reliable decision-making, and the substantial computational and latency overhead makes on-board deployment impractical. Cooperative driving provides a potential solution by leveraging external agents for information exchange, but existing methods remain limited in semantic reasoning capability...
  </details>

- **2026-08-10** — Taoyuan Yu, Kui Wang, Zongdian Li et al. — [How Roadside Units Enhance Intersection Safety? Cooperative Autonomous Driving System Design and A Proof of Concept](http://arxiv.org/abs/2608.09144v1)
  <details><summary>📄 Abstract</summary>
  Intersections remain one of the most hazardous locations in urban road networks, where heterogeneous traffic participants and limited visibility frequently lead to severe traffic conflicts. In this paper, a vehicle-to-infrastructure-to-vehicle (V2I2V) cooperative system is proposed for improving road safety and traffic efficiency by using digital twins (DTs) deployed on roadside units (RSUs) to eliminate blind spots and centrally coordinate connected and automated vehicles (CAVs) in smart inters...
  </details>

- **2026-08-10** — Lisheng Huang, Chen Yang, Hao Zhou et al. — [Evo-Bench: Can Language Models Improve Agent Harness?](http://arxiv.org/abs/2608.09096v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have driven rapid progress in autonomous agents, yet standard evaluations remain confined to static task solving. An emerging frontier is harness evolution---the agent's capacity to autonomously optimize its own operating harness. However, systematically benchmarking this capability remains challenging, as existing evaluations fail to isolate harness improvements from base model strength, prevent task-specific overfitting, or capture long-horizon iterative research. ...
  </details>

- **2026-08-10** — Zihao Deng, Yining Zhu, Leiming Wang et al. — [Tree-of-Experience: Hierarchical Experience Management for Self-Evolving Agents](http://arxiv.org/abs/2608.09044v1)
  <details><summary>📄 Abstract</summary>
  Continual self-evolution requires LLM agents to transform environmental interactions into reliable and reusable experience. Existing methods typically refine individual trajectories or abstract shared knowledge from related trajectories, but their experience representations are often disconnected from the underlying reasoning process. This limits feedback attribution, cross-task transfer, and update and retrieval efficiency, particularly in complex reasoning tasks with outcome-level feedback. To...
  </details>

- **2026-08-10** — Ao Zhou, Zhiwei Jiang, Zifeng Cheng et al. — [Dynamic Distribution-Aware Uncertainty Tracking in Vision-Language Representation Learning](http://arxiv.org/abs/2608.09011v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty Quantification (UQ) aims to measure the reliability of model predictions, serving as a critical safeguard for deploying Vision-Language Models (VLMs) in safety-critical scenarios. Post-hoc approaches are widely adopted due to their lightweight nature, mapping the outputs of VLMs to uncertainty measures through learnable modules or inductive summarization. However, Post-hoc approaches remain inherently confined to fitting the failure patterns of the source domain, ignoring the dynamic...
  </details>

- **2026-08-10** — Alban Puech, Matteo Mazzonelli, Tamara R. Govindasamy et al. — [GENCO - A Unified Neural Solver Embedded in a Development Framework for Steady-State Grid Analysis](http://arxiv.org/abs/2608.09921v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are transforming business workflows and boosting productivity, yet they remain largely absent from engineering domains such as power system analysis, where strict physical consistency must be enforced.   We present GENCO (GEometric Neural Corrective Optimizer), a unified neural solver for steady-state transmission grid analysis that handles power flow (PF), optimal power flow (OPF), and state estimation (SE) within a single architecture and shared network representation. To sup...
  </details>

- **2026-08-10** — Jonhnanthan Oliveira, Rohit Gheyi, Márcio Ribeiro et al. — [Detecting Behavioral Changes in Python Refactoring Implementations with Foundation Models](http://arxiv.org/abs/2608.09919v1)
  <details><summary>📄 Abstract</summary>
  Python is a widely adopted programming language, valued for its simplicity and flexibility. However, automated refactoring for Python remains challenging, even though refactoring is an essential practice in software evolution aimed at improving internal code structure without changing external behavior. Understanding how behavioral changes are introduced during refactoring is crucial, as such issues can compromise software reliability and reduce developer productivity. We propose an approach bas...
  </details>

- **2026-08-10** — Navid Panchi, Sebastian Kuckuk, Markus Wittmann et al. — [AES-Debye: an Accurate, Efficient, and Scalable Engine for Debye Scattering Calculations](http://arxiv.org/abs/2608.09916v1)
  <details><summary>📄 Abstract</summary>
  Total scattering models are essential for characterizing the structure and disorder of nanoscale materials. The Debye scattering equation (DSE) provides a rigorous route to elastic total scattering, but its direct evaluation is computationally demanding because pairwise contributions must be accumulated at every scattering vector, whereas common acceleration strategies based on binned pair-distance distributions or gridded fast Fourier transforms can introduce discretization and aliasing artifac...
  </details>

- **2026-08-10** — Lecheng Kong, Like Hui, Haitao Mao et al. — [Consilience for Verifier-Free Test-Time Scaling](http://arxiv.org/abs/2608.09898v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling often uses an external verifier, such as compilers and test cases in coding or trained value functions in robotics applications, to obtain high-quality rollouts. Verifier-free test-time scaling (or VF-TTS) is gaining extensive attention as a mechanism to enhance Large Language Model (LLM) reasoning, primarily because we do not have access to such high-quality verifiers in many real-world applications. Among existing VF-TTS methods, confidence-based VF-TTS methods, which compute...
  </details>

- **2026-08-10** — Haoyu Yang, Meixing Shi, Zengjie Chen et al. — [MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation](http://arxiv.org/abs/2608.09818v1)
  <details><summary>📄 Abstract</summary>
  Reliable medical image understanding requires models to connect clinical language and visual reasoning with pixel-level grounding. Yet medical vision-language models often lack precise localization, whereas medical segmenters typically rely on explicit target categories or precise spatial prompts. This divide is reinforced by a supervision mismatch: segmentation datasets provide precise masks but little language supervision, whereas medical vision-language data rarely pair language with dense sp...
  </details>

- **2026-08-10** — Rajul Kumar, Ningshi Yao — [Analysis and Consensus Control of Emergent Dynamic Polarization in Minimally-Nonlinear Opinion Dynamics](http://arxiv.org/abs/2608.09724v1)
  <details><summary>📄 Abstract</summary>
  Collective opinions in social networks evolve through local interaction rules, yet how such local updates give rise to dynamic polarization--persistent oscillatory disagreement between opposing opinion clusters at the network level--remains unexplained. This paper proposes a Minimally-Nonlinear Opinion Dynamics (or M-NOD) framework that analytically characterizes dynamic polarization as a truly emergent collective behavior arising solely from local, agent-level opinion-update rules without exter...
  </details>

- **2026-08-10** — Navaraj Neupane, Loc H. Nguyen — [Carleman--Picard and time-dimensional reduction for inverse initial-data problems in nonlinear transport with memory](http://arxiv.org/abs/2608.09665v1)
  <details><summary>📄 Abstract</summary>
  We study an inverse initial-data problem for a quasilinear transport equation with nonlinear and memory effects. The unknown initial state is reconstructed from time-dependent measurements on the outflow boundary, with prescribed inflow data. We first apply a Legendre--exponential time-dimensional reduction to transform the governing equation into a finite nonlinear system in space. We then develop a Carleman-weighted and Tikhonov-regularized Picard method. At each iteration, the nonlinear terms...
  </details>

- **2026-08-10** — Hieu Dinh Trung Pham, Phuong Huu Vu Tran, Thuan Duc Mai et al. — [FaLCon: Facet-Anchored Retrieval with Late Consensus for Sim2Real Text-Based Person Anomaly Search](http://arxiv.org/abs/2608.09474v1)
  <details><summary>📄 Abstract</summary>
  Text-based person anomaly search requires retrieving real-world pedestrian images from detailed natural-language descriptions using models trained primarily on synthetic data. This Sim2Real setting is particularly challenging because visually similar candidates may differ only in subtle actions, object interactions, or appearance attributes, while applying multimodal large language models to the entire gallery is computationally expensive. We propose an anchor-constrained coarse-to-fine retrieva...
  </details>

- **2026-08-10** — Boxiong Wang, Hui Kang, Geng Sun et al. — [RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation](http://arxiv.org/abs/2608.09467v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicle vision-language navigation (UAV-VLN) requires agents to translate visual observations and language instructions into reliable flight actions in complex environments. Although recent end-to-end UAV vision-language-action (UAV-VLA) policies reduce reliance on separately designed perception, planning, and control modules, their behavior-cloning objectives provide limited corrective supervision for interactive closed-loop execution. Reinforcement learning (RL) offers a promis...
  </details>

- **2026-08-10** — N. Karimi, E. Salavati, F. Shokrollahi — [Climate-Conditioned Cascade Modeling for Multi-Peril Reinsurance: Analysis and Controlled Numerical Applications](http://arxiv.org/abs/2608.09456v1)
  <details><summary>📄 Abstract</summary>
  Climate perils are linked through event ordering and state-dependent propagation, features not fully captured by joint loss distributions alone. This paper develops a Cascading Climate Risk Network (CCRN) for multi-peril reinsurance that separates calendar-scale climate conditioning from within-event propagation on a directed acyclic graph (DAG). The model combines complementary-log-log triggering hazards with bounded severity activation, mapping physical states to insured losses via a capacity-...
  </details>

- **2026-08-10** — Siqi Wang, Xinlin Li, Zhenglin Li et al. — [OpenLoopEvolve: A Verifiable Self-Evolution Framework for Loop Policies in Long-Horizon Complex Tasks](http://arxiv.org/abs/2608.09380v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon complex tasks require agents to repeatedly observe states, formulate plans, invoke tools, verify results, and recover from failures in continuously changing environments. However, such control experience often remains confined to a single context or a fixed prompt, and is difficult to accumulate and reuse across historical traces. This paper presents OpenLoopEvolve (OLE), a self-evolution framework centered on the Loop Policy. OLE represents an agent's observation, planning, memory,...
  </details>

- **2026-08-10** — Jun Huang, Meiyi Chen, Zijie Yue et al. — [Bootstrapping Vision-Language Model for Hysteroscopic Surgical Scene Segmentation](http://arxiv.org/abs/2608.09302v1)
  <details><summary>📄 Abstract</summary>
  Hysteroscopic surgical scene segmentation plays a pivotal role in understanding the hysteroscopic intraoperative environment as well as computer-assisted intervention. However, this task presents unique challenges due to the high morphological similarity among different lesions and the presence of artifacts such as specular reflections, motion blur, and fluid occlusions in surgical videos. In this work, we propose the first vision-language model (VLM)-based hysteroscopic surgical scene segmentat...
  </details>

- **2026-08-10** — Tong Zhao, Mingkun Lei, Yucheng Han et al. — [BAG: Budget-Aware Gating for Diffusion Caching](http://arxiv.org/abs/2608.09231v1)
  <details><summary>📄 Abstract</summary>
  Diffusion caching is a lightweight strategy that accelerates Diffusion Transformers (DiTs) by reusing intermediate features across denoising steps, but existing paradigms face a fundamental trade-off: online heuristics lack global budget awareness, whereas static schedules lack instance adaptivity and fail to flexibly adapt to varying runtime budget constraints. To bridge this gap, we present BAG (Budget-Aware Gating), a novel caching policy that unifies global budget pacing with dynamic, instan...
  </details>

- **2026-08-10** — Junyu Wang, Siyuan Zhang, Peiyuan Jiang et al. — [EmoS: A Theory-Grounded Framework for Evaluating and Aligning Emotional Intelligence in Spoken Language Models](http://arxiv.org/abs/2608.09189v1)
  <details><summary>📄 Abstract</summary>
  Despite significant advances in instruction-following and auditory comprehension, the evaluation of Emotional Intelligence (EI) in Spoken Language Models (SLMs) remains confined to rudimentary paralinguistic perception, lacking a systematic, theory-driven cognitive framework. We introduce EmoSBench, the first comprehensive EI evaluation benchmark for SLMs constructed upon the four-branch theoretical model, covering Perceiving, Understanding, Using, and Managing Emotion across ten sub-tasks. Prel...
  </details>

- **2026-08-10** — Yanxi Ding, Tingyue Jia — [A Time-Frequency Dual-Domain Multi-Scale Convolutional Neural Network for Bearing Fault Diagnosis under Strong Noise](http://arxiv.org/abs/2608.09174v1)
  <details><summary>📄 Abstract</summary>
  To address the degradation of bearing fault diagnosis accuracy under strong noise, this paper proposes a time-frequency dual-domain multi-scale convolutional neural network. The time-domain branch employs three parallel convolutional kernels to capture multi-scale impulse features, while the frequency-domain branch applies the Fast Fourier Transform to extract noise-robust spectral structure information. Features from both branches are fused for fault classification, yielding a compact model of ...
  </details>

- **2026-08-10** — Tianchen Deng, Chongdi Wang, Nailin Wang et al. — [Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction](http://arxiv.org/abs/2608.09146v1)
  <details><summary>📄 Abstract</summary>
  Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture and a dual-tier loop closure mechanism. Specifically, we propose a progressive mapping strategy that dynamically allocates neural submaps to ...
  </details>

- **2026-08-10** — Shadikur Rahman, Umme Ayman Koana, Syed Muhammad Danish — [Pseudo2CodeQA: A Benchmark for LLM-Based Structured Algorithmic Reasoning in Code Generation](http://arxiv.org/abs/2608.09068v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved impressive performance in natural language-to-code generation; however, their ability to follow structured algorithmic reasoning remains insufficiently understood. We introduce Pseudo2Code, a benchmark designed to systematically evaluate the impact of structured pseudocode on code generation quality and algorithmic faithfulness. The benchmark consists of 300 manually validated real-world programming tasks spanning multiple domains and three difficulty l...
  </details>

- **2026-08-09** — Pengfei Zhou, Zhiwei Tang, Xiaopeng Peng et al. — [Improving Generalization Robustness of Multimodal RLVR](http://arxiv.org/abs/2608.08802v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning with Verifiable Rewards (RLVR) makes Multimodal Large Language Models more accurate, but the gains are brittle: simply paraphrasing a question or changing the prompt template can degrade them, which challenges reliable deployment in high-stakes scenarios like medical VQA. We trace this to two issues of the standard RL objective. First, the binary verifier conflates format with content, so the reward signal cannot tell a wrong answer apart from a misformatted one. Second, t...
  </details>

- **2026-08-09** — Dongjie Xu,  Julius, Hanchi Dong et al. — [PluginEval: A Diagnostic Benchmark for Fine-Grained Error Attribution in Function Calling](http://arxiv.org/abs/2608.08700v1)
  <details><summary>📄 Abstract</summary>
  Reliable evaluation of tool routing is critical as Large Language Models increasingly operate as autonomous agents. Current benchmarks face three structural limitations: data distributions that follow a power law leave rare scenarios underrepresented; the absence of adversarial hard negatives obscures performance differences across models; and annotation pipelines depend on LLM judgments that have not been validated through execution. In this paper, we introduce PluginEval, a benchmark construct...
  </details>

- **2026-08-09** — Y. M. Du, Miao-Miao Yi, Tan-Ji Zhou et al. — [Reliability-Safety Trade-off in AI Distillation: A Renormalization-Group Approach](http://arxiv.org/abs/2608.08572v1)
  <details><summary>📄 Abstract</summary>
  Knowledge distillation transfers more than task competence: it also transmits response propensities, refusal policies, error boundaries, and latent safety biases. We formulate this behavioral inheritance as a coarse-graining model grounded in statistical mechanics, in which the student's answer and refusal decisions define two macrostates, while the teacher induces an effective field that reshapes the student's free-energy landscape. The model yields a reliability-safety trade-off relation contr...
  </details>

- **2026-08-09** — Yu Wang, Jeffrey Zhou, Menglin Liu et al. — [Position Bias in Ordinal Classification: A Systematic Evaluation](http://arxiv.org/abs/2608.08869v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used for ordinal classification, yet semantically equivalent changes to prompt organization can alter their predictions. We conduct systematic experiments to characterize positional bias from label order, demonstration order, and demonstration placement. First, we apply the three probes to ten frontier LLMs on a common ordinal-classification task; every model is sensitive to all three positional sources, showing that the problem is pervasive. Second, we var...
  </details>

- **2026-08-09** — Zi Yuan Eric Shao — [Simultaneous Group-Envelope Bounds for $Γ$-Robust Multiple-Choice Knapsack Problems](http://arxiv.org/abs/2608.08861v1)
  <details><summary>📄 Abstract</summary>
  Many robust planning problems are solved by checking a family of ordinary optimization problems, one for each uncertainty threshold. Repeatedly building and solving those relaxations can dominate runtime. We show that, when a decision chooses exactly one option from each group, the entire threshold family of multiple-choice knapsack relaxations can instead be bounded together. A cancellation removes threshold-specific baselines and reduces each group's contribution to two simple envelopes. After...
  </details>

- **2026-08-09** — Zongfei Li — [Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts](http://arxiv.org/abs/2608.08853v1)
  <details><summary>📄 Abstract</summary>
  Sparse Mixture-of-Experts (MoE) routers commonly use the same scores both to select experts and to weight their already-computed outputs. We study whether these two roles, dispatch and aggregation, should be coupled. On pretrained OLMoE-1B-7B, we keep selected Top-8 expert IDs, expert computation, and total selected router mass fixed and change only within-set aggregation. A structured oracle improves full-horizon cross-entropy by 0.0160 +/- 0.0039 across three seeds; the router's top-scored exp...
  </details>

- **2026-08-09** — Zhanyu Ju, Wenchi Cheng — [ML-Based Hierarchical Prediction for Practical Energy Scheduling in Dynamic NTN-WPT Systems](http://arxiv.org/abs/2608.08804v1)
  <details><summary>📄 Abstract</summary>
  With advancements in long-distance wireless power transfer (WPT) and space-based energy technologies, integrating WPT into non-terrestrial networks (NTNs), referred to as NTN-WPT, is emerging as a promising approach for next-generation wireless networks. This paper proposes an energy-scheduling approach that jointly optimizes energy efficiency, task completion rate, and task waiting time for power transfer from low Earth orbit satellites to terrestrial mobile user devices (UDs). To address sched...
  </details>

- **2026-08-09** — Nazlıcan Düşünmez, Halûk Gümüşkaya — [RobustDefect-LLM: Explainable and Robustness-Aware Industrial Surface Defect Classification with Decision Support and AI-Assisted Reporting](http://arxiv.org/abs/2608.08589v1)
  <details><summary>📄 Abstract</summary>
  This paper presents RobustDefect-LLM, an industrial surface-defect inspection framework integrating deep-learning classification, operator-facing visual evidence, confidence-aware decision support, controlled AI-assisted reporting, traceable storage, and mobile interaction in a unified quality-control workflow. Here, robustness-aware denotes explicit evaluation under controlled image degradation and confidence-aware review routing, not an intrinsic robustness guarantee. Four transfer-learning-ba...
  </details>

- **2026-08-09** — Prishita Ray — [Curriculum Generation under Structured Parametric Environments for Robust Navigation Policies](http://arxiv.org/abs/2608.08545v1)
  <details><summary>📄 Abstract</summary>
  Robust navigation policies for autonomous agents must generalize across continuously varying environmental conditions such as turn rates, obstacles, friction, pits, and slopes. Curriculum generation provides a principled mechanism for improving generalization by progressively adapting training environments, but designing such curricula in a sample-efficient and automated manner remains challenging. This paper proposes a reparameterized curriculum generation framework for structured continuous en...
  </details>

- **2026-08-09** — Minhan Cho, Jimin Kweon — [Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing](http://arxiv.org/abs/2608.08514v1)
  <details><summary>📄 Abstract</summary>
  We independently reproduce two recent methods for making large language model (LLM) reasoning more reliable, and stress-test them across domains and models (RPC across four new task domains with Qwen3-8B, LCF across four 7-8B models). The first, RPC, aggregates token probabilities and self-consistency at inference; the second, LCF, trains projectors that split hidden states into "content" and "logic" and edits the logic part toward a valid region. Validating such reliability claims matters becau...
  </details>

- **2026-08-09** — Thai-Binh Nguyen, Zhaolin Li, Jan Niehues et al. — [From Speech to Interaction: Analyzing Multimodal Systems in Cocktail-Party Scenarios](http://arxiv.org/abs/2608.08510v1)
  <details><summary>📄 Abstract</summary>
  Humans have the remarkable ability to engage in spontaneous informal conversations and selectively attend to individual speakers while filtering out competing speech from nearby conversations. This "cocktail party" scenario still presents severe challenges to speech recognition systems. The CHiME-9 MCoRec task provides a testbed where systems must recognize groups of speakers and transcribe each of their conversations from audio-visual input. In this work, we analyze a diverse set of systems, re...
  </details>

- **2026-08-09** — Ajeet Kumar Verma — [Towards Adaptive Super-Resolution and Quality Assessment via Test-Time Adaptation](http://arxiv.org/abs/2608.08508v1)
  <details><summary>📄 Abstract</summary>
  This paper presents doctoral research on adaptive video super-resolution and perceptual quality modeling under real-world conditions. Existing video super-resolution (VSR) methods struggle to generalize under unknown degradations arising from heterogeneous devices, codecs, and network environments. We address this challenge through test-time adaptation (TTA), a unified paradigm that improves robustness and perceptual quality without retraining or high-quality supervision. Specifically, we: 1) pr...
  </details>

- **2026-08-09** — Rahma Simin Ali, Jawad Hossain — [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](http://arxiv.org/abs/2608.08503v1)
  <details><summary>📄 Abstract</summary>
  Mathematical reasoning remains challenging in low-resource languages such as Bangla. We study whether teacher-generated Bangla Chain-of-Thought (CoT) supervision provides benefits beyond ordinary supervised fine-tuning. We construct \textsc{MathShikkha}, a Bangla mathematical reasoning dataset with GPT-5.4-generated rationales, and fine-tune four 4B--7B student models under a matched protocol in which answer-only and CoT conditions share data splits, response-only loss masking, decoding, and sco...
  </details>

- **2026-08-09** — Jiaqi Liu, Chunyang Zhang, Heng Pan et al. — [PSP: Low-Overhead Packet-Level Load Balancing for Stale-State and Bandwidth-Asymmetric Networks](http://arxiv.org/abs/2608.08425v1)
  <details><summary>📄 Abstract</summary>
  With the rapid growth of large language model training and generative artificial intelligence services, data center networks face severe micro-burst traffic and high concurrency. Traditional hash-based flow-level load balancing cannot sense link states, leading to hash collisions, hotspot congestion, and tail latency in multipath Clos networks. Existing packet-level schemes are constrained by stale state information, high hardware complexity, and poor adaptation to heterogeneous links.   To addr...
  </details>

- **2026-08-08** — Zhiyuan Yang, Jiahao Cheng, Vincent Quoc-Huy Trinh et al. — [Gated Spatial Redundancy Projection for Pathology Transformer Attentions](http://arxiv.org/abs/2608.08374v1)
  <details><summary>📄 Abstract</summary>
  Transformer models are increasingly used for whole-slide image analysis in computational pathology. Yet, WSIs differ fundamentally from natural images: neighbouring patches often contain highly similar tissue type, stain, texture, and cellular composition. We identify this local spatial redundancy as a pathology-specific failure mode of self-attention, where dominant neighbourhood features can be repeatedly mixed into patch-tokens and weaken subtle diagnostic or prognostic deviations. We propose...
  </details>

- **2026-08-08** — Francisco Ribeiro, Sohaila Abdulsattar, Renata Gonzalez et al. — [On the Robustness of LLMs' Internal Representation of Code Correctness](http://arxiv.org/abs/2608.08266v1)
  <details><summary>📄 Abstract</summary>
  Code generated by modern language models often reads naturally. Yet, it also often fails to implement what was asked. This should be no surprise, as research shows the models' own confidence signals are poorly calibrated with actual correctness. A promising way to assess correctness looks inside the model: by contrasting the hidden states of correct and incorrect programs, recent work captured an internal signal of code correctness that is able to judge candidate solutions better than the model'...
  </details>

- **2026-08-08** — Xiaohe Li, Yiru Wang, Junhao Fan et al. — [Lingjing: A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Cities](http://arxiv.org/abs/2608.08045v1)
  <details><summary>📄 Abstract</summary>
  Urban embodied intelligence requires coordination among heterogeneous agents (e.g., UAVs, ground robots, and autonomous vehicles) in dynamic cities. Simulators therefore provide a scalable foundation for developing and evaluating such coordination. Existing platforms nevertheless isolate different embodiments and decouple them from task design and evaluation. We present \textbf{Lingjing}, a simulation platform for heterogeneous multi-agent embodied intelligence in open-ended urban environments. ...
  </details>

- **2026-08-08** — Bo Cheng, Qiaolin Lu, Yi Chang et al. — [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](http://arxiv.org/abs/2608.08168v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) employing Chain-of-Thought (CoT) exhibit superior reasoning capabilities, the neural mechanisms distinguishing this explicit Thinking mode from direct answer generation (NoThinking mode) remain poorly understood. To deconstruct this cognitive process, we apply Top-K Sparse Autoencoders (SAEs) to the intermediate representations of DeepSeek-R1-Distill-Qwen-7B and examine the model's divergent behaviors across math-solving tasks of three distinct difficulty level...
  </details>

- **2026-08-08** — Siddarth Singh, Victoria Williams, Simon Rosen et al. — [CORDA: A Benchmark for Hierarchical Harm-Centric Moral Reasoning in Large Language Models](http://arxiv.org/abs/2608.08061v1)
  <details><summary>📄 Abstract</summary>
  The key question in moral judgement is not simply whether someone chooses the "right" answer, but how they decide what matters most when moral principles conflict. Current evaluations of large language models (LLMs) remain limited: most test whether models give morally acceptable answers, match human preferences, or avoid obvious violations, rather than whether they can prioritise between competing principles when no option is morally cost-free. We introduce CORDA (Conditioned Ordering and Ranke...
  </details>

- **2026-08-08** — Osvaldo Quinjica, Eric Bennett, Xinchen Yang et al. — [Do Evaluation Metrics Detect Errors in Classical Chinese to English Translations?](http://arxiv.org/abs/2608.08283v1)
  <details><summary>📄 Abstract</summary>
  Although large language models can translate some historical languages surprisingly well, their usefulness in digital humanities workflows is limited by the lack of reliable evaluation. We investigate whether existing automatic evaluation metrics developed for modern languages are reliable in this setting, using translation from Classical Chinese to English as a test case. We introduce a diagnostic framework based on minimal pairs capturing error types salient in scholarly use, probing both refe...
  </details>

- **2026-08-08** — Catherine M. Brousse, Nelu D. Radpour — [Focus particles and scalar inferences across humans and language models](http://arxiv.org/abs/2608.08227v1)
  <details><summary>📄 Abstract</summary>
  Focus particles such as "even" and "only" are central to formal semantic theories that posit structured representations over sets of alternatives. "Even" highlights unexpected or extreme alternatives, while "only" enforces exclusivity. If such scalar representations are robust and generalizable, they should give rise to consistent judgments across contexts and systems. In this work, we test whether humans and large language models (LLMs) construct stable scalar representations from sentences con...
  </details>

- **2026-08-08** — Praveen Kumar Katwe, Rakesh Chandra Balabantaray, Kali Prasad Vittala et al. — [A Grounded and Decomposed Framework for Relation-Level Hallucination Evaluation in Abstractive Summarization](http://arxiv.org/abs/2608.08180v1)
  <details><summary>📄 Abstract</summary>
  Abstractive text summarization systems frequently generate fluent yet unfaithful summaries by fabricating or distorting relationships between entities and   events. Such relation-level hallucinations undermine the reliability of generated summaries, particularly in high-stakes domains. In this work, we present a   refined and grounded framework for evaluating relation hallucination in abstractive summarization. We present the empirical Relation Hallucination Index (RHI) by   introducing a depend...
  </details>

- **2026-08-08** — Junsik Jung, Seokryun Choi, Yoonki Cho et al. — [EvBS: Event-guided Blur Synthesis for Domain-adaptive Motion Deblurring](http://arxiv.org/abs/2608.08066v1)
  <details><summary>📄 Abstract</summary>
  Motion deblurring has achieved remarkable progress with deep learning, yet pre-trained deblurring models often suffer from performance degradation in real-world scenarios due to the domain shift between training and testing distributions. To remedy this, we propose EvBS, an event-guided blur synthesis framework that generates diverse training pairs for calibrating pre-trained models to the target domain. While existing methods are constrained by the inherent entanglement between motion and visua...
  </details>

- **2026-08-08** — Ling Lin, Yang Bai, Congcong Zhu et al. — [Advantage-Guided Gate: Reshaping Open-Ended Reasoning for Vision-Based Spatial Intelligence](http://arxiv.org/abs/2608.07987v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have demonstrated significant potential in complex spatial scene understanding and reasoning tasks. However, their open-ended reasoning process is prone to decision errors and error accumulation, leading to instability in answer quality. To address this, we propose an advantage-guided gating framework that dynamically intervenes in and corrects deviations during the reasoning process. Specifically, we model step-by-step reasoning as a finite-horizon decis...
  </details>

- **2026-08-07** — Valentin Liévin, Samuel Schmidgall, Tim Strother et al. — [ResidencyRL: Reinforcement Learning in Simulated Clinical Environments](http://arxiv.org/abs/2608.07418v1)
  <details><summary>📄 Abstract</summary>
  In medical education, physicians convert academic knowledge into clinical expertise through residency: years of training across thousands of encounters, with diverse sources of feedback and progressively greater autonomy. Much of clinical reasoning relies on the patient encounter, a dialogue in which a clinician elicits history, refines diagnostic hypotheses, and decides management under uncertainty. While large language models (LLMs) excel on static medical benchmarks, methods to optimize the f...
  </details>

- **2026-08-07** — Caden Wong, Vikram Das, Himanshu Dhami — [The Token Efficiency Index: A Peer-Benchmarked Composite Indicator for AI Token Efficiency](http://arxiv.org/abs/2608.07304v1)
  <details><summary>📄 Abstract</summary>
  As artificial intelligence (AI) adoption accelerates across tech giants, AI-native startups, and non-technical organizations alike, a deceptively simple question remains hard to answer: is that spending efficient? AI consumption is priced by tokens, and costs vary by token type (input, output, reasoning) and model type, with usage ranging from a few hundred tokens for simple queries to over a million for multi-step agentic tasks. This variance makes cost comparison, both within and across organi...
  </details>

- **2026-08-07** — Junkai Lin, Siqi Hou, Raymond Lee — [QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series Forecasting](http://arxiv.org/abs/2608.07363v1)
  <details><summary>📄 Abstract</summary>
  Forecasting non-stationary time series remains difficult due to long-range dependencies, local volatility bursts, structural shifts, and nonlinear oscillatory behaviors. Although Transformer-based forecasters are effective for modeling long-term temporal dependencies, their feed-forward blocks typically rely on smooth static activations that are insufficiently sensitive to abrupt regime changes. Motivated by quantitative Transformer designs and oscillator-based nonlinear activations, we propose ...
  </details>

- **2026-08-07** — Chen Shao, Yue Wang, Zhenyi Zhu et al. — [When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series](http://arxiv.org/abs/2608.07333v1)
  <details><summary>📄 Abstract</summary>
  Modeling multivariate time series by representing them as graphs, where individual series act as nodes and pairwise temporal corre- lations serve as edges, has gained significant traction. Recent advances in Graph Neural Networks (GNNs) have demonstrated strong perfor- mance by assuming a static graph topology and aggregating information from neighboring series. In this work, we investigate the representa- tional power of GNNs for forecasting under both static and dynamic settings (i.e., when pa...
  </details>

- **2026-08-07** — Rahul Murali Shankar, Titus von der Malsburg, Sebastian Padó — [Gaze Behavior in Visual World Experiments Can be Modeled With Off-the-shelf Language-Vision Encoders](http://arxiv.org/abs/2608.07282v1)
  <details><summary>📄 Abstract</summary>
  The recent advances in neural language models have also spurred much work in computational psycholinguistics, asking whether neural LMs are also promising models of human language processing. However, work has been overwhelmingly focused on the unimodal case of written or spoken language. In contrast, multimodal experimental paradigms, like visual world studies that present participants with both visual and linguistic input simultaneously, have been neglected. In this paper, we present a novel a...
  </details>

- **2026-08-07** — Mathurin Videau, Badr Youbi-Idrissi, David Lopez-Paz et al. — [Skaling: Chinchilla's Exponents Meet Kaplan's Coupling](http://arxiv.org/abs/2608.07222v1)
  <details><summary>📄 Abstract</summary>
  Neural scaling laws are foundational for language model development, yet standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently. To address this, we introduce the Skaling law, a generalized functional form that couples model capacity and data through a single interaction exponent. This simple extension reduces the Mean Absolute ...
  </details>

- **2026-08-07** — Bruno Palau, Franziska Vogt, Daria Laslo et al. — [Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation](http://arxiv.org/abs/2608.07117v1)
  <details><summary>📄 Abstract</summary>
  Radiology reporting is time-consuming and subject to inter-rater variability, making automated report generation an attractive clinical application for Vision-Language Models (VLMs). We benchmark state-of-the-art VLMs on lumbar spine MRI with a focus on diagnostic accuracy and demonstrate that standard lexical and semantic metrics poorly reflect clinical correctness: fluent, well-structured reports can score highly while containing clinically meaningful diagnostic errors. To address this failure...
  </details>

- **2026-08-07** — Xingcheng Chen, Mehmet Besenk, Andrea Stocco — [Explanation-Guided Metamorphic Testing of Specialized Language Models: An Empirical Study](http://arxiv.org/abs/2608.07076v1)
  <details><summary>📄 Abstract</summary>
  \head{Background} Task-specialized language models are increasingly integrated into software engineering workflows to support vertical-domain activities such as issue triaging, document classification, and automated analysis. Despite their adoption, there is limited empirical evidence on how to test their robustness and detect brittle behaviors under semantics-preserving input transformations.   \head{Aims} This paper investigates whether explainability-guided metamorphic testing can improve the...
  </details>

- **2026-08-07** — R. G. Bahumanya, Harshith V. M., Shreyank N. Gowda et al. — [Explanation Stability of Test-Time Adaptation in Computational Pathology: A Large-Scale Benchmark](http://arxiv.org/abs/2608.07062v1)
  <details><summary>📄 Abstract</summary>
  Test-time adaptation (TTA) has become a practical way to adapt deployed models to unlabeled target data, a setting that is especially relevant in computational pathology where staining, scanner, and cohort shifts are routine. While most TTA methods are evaluated by their effect on accuracy, clinical use also depends on whether the model's explanations remain reliable after adaptation. In this paper, we take a closer look at this largely unmeasured effect. We study explanation stability under TTA...
  </details>

- **2026-08-07** — Iulian Cîmpean, Andreea Grecu, Arghir Zarnescu — [Extended Walk-on-Spheres Algorithm for Linear and Nonlinear Elliptic Problems of Divergence-type](http://arxiv.org/abs/2608.07017v1)
  <details><summary>📄 Abstract</summary>
  The Walk-on-Spheres algorithm, introduced by M. E. Muller in 1956, is a well known Monte Carlo method that leverages Brownian exit distributions from spheres to solve the Laplace equation with Dirichlet boundary conditions. Its mesh-free nature, robustness on complex geometries, favorable scaling with dimension, and intrinsic parallelism distinguish it from mesh-based solvers. However, its efficient applicability has been essentially limited to operators that admit explicit probabilistic exit la...
  </details>

- **2026-08-07** — Jerzy Grobelny, Rafał Michalski — [Linguistic Pattern Based Optimization of Economic and Spatial Uniformity Criteria in Facility Layout Problems](http://arxiv.org/abs/2608.07011v1)
  <details><summary>📄 Abstract</summary>
  This paper extends prior work on linguistic pattern based facility layout optimization by enhancing the LP Alinks framework with an explicit spatial uniformity criterion. While earlier studies demonstrated that linguistic patterns can effectively encode expert knowledge and guide agent based layout emergence, their optimization scope remained limited to cost oriented objectives. To address this gap, we introduce the Normalized Coverage Score (NCS), a scale adjusted measure of spatial evenness th...
  </details>

- **2026-08-07** — Haolin Tian, Yuzhe Liu, Tonghan Wang — [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](http://arxiv.org/abs/2608.07001v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result, cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance local resolution and information coverage. Therefore, we propose GraceKV, a global...
  </details>

- **2026-08-07** — Bingqi Huang, Bingchuan Wei, Xuan Wang et al. — [Cross-View Action Consistency for Camera-Robust Vision-Language-Action Policies](http://arxiv.org/abs/2608.06965v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies fine-tuned from a fixed scene camera can fail when the camera is moved, even when the task, objects, language, and robot state are unchanged. We study scene-camera viewpoint robustness using only a scene RGB image, language, and proprioception, without camera labels, extrinsics, depth, or point-cloud inputs. The wrist stream is masked throughout to prevent an unperturbed visual shortcut from confounding attribution to scene-camera variation. For flow-based V...
  </details>

- **2026-08-07** — Seitaro Ono, Senna Ross, Jun Saiki — [Calibrating WEAT Against Anisotropy: ZCA Whitening as a Geometric Pre-Processing Step for Embedding Association Tests](http://arxiv.org/abs/2608.06908v1)
  <details><summary>📄 Abstract</summary>
  We propose Zero-phase Component Analysis (ZCA) whitening as a geometric pre-processing step for the Word Embedding Association Test (WEAT). WEAT is a bias measurement method widely used in both computational social science and AI fairness research. It relies on cosine similarity as a measure of semantic association, which assumes that the embedding space is approximately isotropic. However, prior work has reported that many widely used language models do not satisfy this assumption, raising conc...
  </details>

- **2026-08-07** — Yong Li, Tao Du, Rasmus Christensen et al. — [Local Structure Dictates Ionic Transport and Mechanical Properties in Glassy Solid Electrolytes for Lithium Batteries](http://arxiv.org/abs/2608.06895v1)
  <details><summary>📄 Abstract</summary>
  Electrolytes composed of sulfide and halide glasses are promising candidates for all-solid-state lithium batteries owing to their processability, lack of grain boundaries, and relatively high ionic conductivity. Nevertheless, their ionic conductivity and mechanical properties are still not satisfying for the real-world applications. Significant advances in solid electrolytes require a thorough understanding of their microstructures. Here, we reveal the connections among structure, ionic transpor...
  </details>

- **2026-08-06** — Zhiheng Wang, Bo Peng, Lai Wei et al. — [The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images](http://arxiv.org/abs/2608.06270v1)
  <details><summary>📄 Abstract</summary>
  The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost. They may also repeatedly crop irrelevant regions and fail on questions that direct inference answers correctly. We ask whether the returned visual evidence causally affects the answer. To answer this question, we formulate visual tool-use as a c...
  </details>

- **2026-08-06** — Ro Encarnación, Tina Behzad, Emma Lurie et al. — [What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)](http://arxiv.org/abs/2608.06202v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) benchmark evaluations are routinely used to support claims about model safety, reliability, and deployment readiness. Yet most evaluations rely on a single access modality (model APIs), perform a single run per prompt, and report accuracy as the primary outcome metric, without accounting for conditions such as web search that may have effects on model behavior in deployment. We audit these assumptions for one of the most widely-used LLMs, comparing two modalities, Chat...
  </details>

- **2026-08-06** — Xiaoqing Wu, Xingyu Fan, Feifei Li et al. — [When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories](http://arxiv.org/abs/2608.06057v1)
  <details><summary>📄 Abstract</summary>
  Tool-calling agents infer task state from accumulated dialogue and tool traces. In persistent interactions, however, historical traces may remain structurally valid and semantically plausible after they cease to be authoritative for the current request. We show that such history can hijack a policy the model already possesses: on Qwen3-1.7B, pollution flips 32.1% of decisions that are correct under the original trajectory and frequently induces reuse of corrupted entities or interface convention...
  </details>

- **2026-08-06** — Alexander Apartsin, Yehudit Aperstein — [Clinical Communication Processing with Models Trained on LLM-Generated Synthetic Data: A Structured Survey and Novel Application Case Studies](http://arxiv.org/abs/2608.05993v1)
  <details><summary>📄 Abstract</summary>
  Much clinical value is conveyed not through structured records but through communication: exchanges in which patients describe symptoms, clinicians reason and give instructions, ambulances hand over to emergency departments, and nurses pass on a shift. Such language differs from tabular data because meaning depends on speaker role, intent, causality, uncertainty, omission, and channel noise. Healthcare natural language processing must therefore interpret information as conveyed rather than coded...
  </details>

- **2026-08-06** — Yongjie Qian, Ke Gao, Zhibin Zhang et al. — [RepoOMP: Repository-Aware Hotspot OpenMP Parallelization via Dependency-Aware Context Reduction](http://arxiv.org/abs/2608.05855v1)
  <details><summary>📄 Abstract</summary>
  OpenMP parallelization of hotspots in mature repositories remains difficult because loop safety and optimization payoff often depend on non-local evidence. Rule-based tools under-parallelize when legality is not locally provable, while agent-based approaches become unstable when retrieval misses decisive dependencies or includes irrelevant code. We present RepoOMP, a hybrid framework that recovers parallelization-relevant evidence before generation. RepoOMP builds a Multi-granularity Attributes ...
  </details>

- **2026-08-06** — Gihoon Kim, Jeyoung Lee, Suhan Woo et al. — [Cautious Context Steering for Language Model Personalization](http://arxiv.org/abs/2608.05813v1)
  <details><summary>📄 Abstract</summary>
  Personalizing language models (LMs) to individual user preferences is essential for aligning responses with diverse goals and backgrounds. Existing methods typically train a separate adapter for each user or learn a reward model whose scores depend on the user. Despite explicitly optimizing for each user, these methods must learn from limited observations and therefore suffer from data sparsity and poor generalization to unseen users and domains. In-context learning (ICL) and Context Steering (C...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 21 papers

- **2026-08-10** — Wanying Qu, Qinghua Mao, Yu Li et al. — [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](http://arxiv.org/abs/2608.09885v1)
  <details><summary>📄 Abstract</summary>
  The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a ...
  </details>

- **2026-08-10** — Abdullah X — [Multi-Agent AI Safety as an Institutional Design Problem](http://arxiv.org/abs/2608.09828v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly work inside systems that govern how they delegate tasks, move information, execute actions, and use shared resources. Recent work already shows that deployment rules can change collective behavior. Here we ask which parts of an AI institution produce safety and how they do it. This is the first paper from POLIS, an ongoing research programme studying algorithmic institutions for multi-agent systems. We report a frozen 5,280-episode study suite. The main pre-specified deleg...
  </details>

- **2026-08-10** — Xuewan He, Tong Chu, Zihan Cheng et al. — [UniDFKD: A Unified Semantic Prior Framework for Architecture-Agnostic Data-Free Knowledge Distillation](http://arxiv.org/abs/2608.09287v1)
  <details><summary>📄 Abstract</summary>
  Data-Free Knowledge Distillation (DFKD) transfers knowledge from a pretrained teacher model to a compact student model by synthesizing semantically informative data, eliminating the need for access to the original training dataset. Existing DFKD methods rely heavily on architecture-specific statistical priors (e.g., Batch Normalization statistics) to guide data synthesis, however, such architecture-dependent priors are often absent in modern architectures such as Vision Transformers (ViTs), resu...
  </details>

- **2026-08-10** — Yikai Zhao, Pradeep Kumar Misra, Saurabh Pandey — [TRACE: TRajectory Attribution for Automated Context Engineering](http://arxiv.org/abs/2608.09153v1)
  <details><summary>📄 Abstract</summary>
  Production AI agents fail when their context sources -- system prompts, knowledge bases, tool descriptions, and procedural skills -- contain errors or gaps. Current maintenance relies on manual log review and ad-hoc debugging, creating a scalability bottleneck as interaction volume grows.   We present TRACE (TRajectory Attribution for Automated Context Engineering), an automated feedback loop that mines historical agent trajectories to diagnose and remediate context failures. Our key insight is ...
  </details>

- **2026-08-10** — Kamil Khadiev, Aliya Khadieva, Vadim Sagitov et al. — [Quantum Hashing Circuit Optimization for Arbitrary Qubit Connectivity Graphs Based on 1-Covering Path](http://arxiv.org/abs/2608.09134v1)
  <details><summary>📄 Abstract</summary>
  One of the obstacles to the widespread adoption of quantum computing is the problem of efficient circuit synthesis. Current quantum hardware has limited connections between qubits, with each qubit connected to only a few others. This means that the circuit has to be transformed to accommodate this. In this paper, we present an algorithm that converts a circuit containing a sequence of CNOT gates into a form that is suitable for arbitrary quantum computer architectures. Although we demonstrate th...
  </details>

- **2026-08-09** — Yijun Pan, Yukun Lian, Kunyu Shi et al. — [Business Arena: Benchmarking LLM Agents in a Realistic Marketplace](http://arxiv.org/abs/2608.08621v1)
  <details><summary>📄 Abstract</summary>
  Running a business is a challenging form of intelligent work. Operators must infer opportunities from partial signals, commit capital under uncertainty, adapt to delayed outcomes in a changing market, and satisfy regulatory obligations before trading legally. Frontier LLM agents can increasingly complete complex workflows, yet business-related capabilities are rarely evaluated in existing agent benchmarks. We introduce \textbf{Business Arena}, a controlled environment where an AI agent runs a cr...
  </details>

- **2026-08-09** — Andrea Caciolai, Pere-Lluís Huguet Cabot, Chierh Cheng et al. — [OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents](http://arxiv.org/abs/2608.08775v1)
  <details><summary>📄 Abstract</summary>
  Agentic benchmarks aim to measure how well AI agents plan, search, execute, and recover within realistic multi-tool environments, but they are almost exclusively in English. As AI agents are globally deployed to a linguistically diverse user base, whether agentic competence measured in English transfers to other languages remains an open question. We introduce OmnilingualGAIA2, a machine-translated expansion (with partial human- expert validation) of the GAIA2 agentic benchmark, covering ten tar...
  </details>

- **2026-08-09** — Miki Ueno — [Private Etymology: Designing Relational Reuse of Shared Symbols in Long-Term Human-AI Interaction](http://arxiv.org/abs/2608.08443v1)
  <details><summary>📄 Abstract</summary>
  Previous studies have shown that people can develop shared symbols, partner-specific expressions, personal idioms, inside jokes, and other parts of a relational microculture. Recent work has also examined how humans and conversational AI negotiate and revise symbolic meanings. However, long-term human-AI systems still lack a clear design model for recording how a dyad-specific expression gains meaning, checking whether both sides still accept that meaning, and safely reusing the expression in la...
  </details>

- **2026-08-09** — Shuowei Jin, Xueshen Liu, Jiaxin Shan et al. — [LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving](http://arxiv.org/abs/2608.08382v1)
  <details><summary>📄 Abstract</summary>
  As LLM inference shifts to multi-tenant GPU clusters, co-batching improves throughput but obscures per-tenant usage and limits control. Enabling fractional sharing of the inference engine requires a real-time, per-request attribution primitive that is accurate and light enough to run inside the scheduling loop. We present LLMVisor, a roofline-guided latency attribution model that captures the memory-bound and compute-bound phases via a concise piecewise-linear form over features proportional to ...
  </details>

- **2026-08-08** — Uri Z. Kialy, Gil Ben-Artzi — [Circuit Fine-Tuning for Compute-Efficient Transformer Adaptation](http://arxiv.org/abs/2608.08336v1)
  <details><summary>📄 Abstract</summary>
  Parameter-Efficient Fine-Tuning (PEFT) has become the de facto standard for adapting Vision Transformers (ViTs) to downstream tasks. While parameter count has been the dominant efficiency metric in PEFT, it does not imply \textit{compute efficiency}: parameter-sparse methods can still incur full-model training cost per step, and typically need long schedules to reach peak accuracy. We introduce Circuit Fine-Tuning (CFT), a compute-efficient framework that uses circuit discovery---conventionally ...
  </details>

- **2026-08-08** — Muhammad Ayub Sabir, Shaohong Zheng, Zhiyu Qu et al. — [Large Multimodal Agents for Intelligent Transportation Systems: Architectures, Evidence, and Deployment Challenges](http://arxiv.org/abs/2608.08184v1)
  <details><summary>📄 Abstract</summary>
  Large multimodal agents (LMAs) are increasingly proposed for intelligent transportation systems (ITS), but existing studies often conflate multimodality, agency, empirical performance, and deployment readiness. This review provides an auditable evidence map of 42 primary study families released between January 2023 and 3 August 2026 within a corpus of 91 mapped sources. It distinguishes model-level, system-level, and hybrid multimodality and classifies each family by system architecture and acti...
  </details>

- **2026-08-08** — Eunna Lee — [The Authority Expectancy Effect in Multi-User Conflict](http://arxiv.org/abs/2608.08026v1)
  <details><summary>📄 Abstract</summary>
  We investigate how social authority (SA) signals interact with severity-based prioritization in large language models, operationalizing each axis as a model-elicited baseline -- the triage hierarchy and the SA hierarchy. Across four LLMs (Claude, Gemini, GPT, Grok) and three experimental phases -- resource allocation, fault attribution, and multi-turn dispute mediation -- we find that occupational authority, institutional documentation, and relational congruence can restructure model judgments i...
  </details>

- **2026-08-08** — Yuqi Wu, Shengming Zhao, Jie Chen — [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](http://arxiv.org/abs/2608.08159v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly reported to exhibit human-like neural and cognitive signatures, including concept cells, mental number lines, and cognitive maps. These claims often rely on linear probing and activation steering applied to a single model, yet both methods are highly sensitive to measurement choices. A reported parallel may therefore reflect the model, the measurement procedure, or both. We audit four representative neuroscience-inspired paradigms across 17 models fr...
  </details>

- **2026-08-08** — Yuqi Wu, Shengming Zhao, Jie Chen — [TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance](http://arxiv.org/abs/2608.08139v1)
  <details><summary>📄 Abstract</summary>
  Establishing the provenance of a language model---including its base checkpoint and possible overlap in training distributions---is a governance challenge that metadata alone cannot resolve. We introduce a training-free fingerprint based on the top-$k$ vocabulary projections of late hidden states elicited by 250 fixed knowledge probes, compared using Jaccard overlap over decoded token strings. We evaluate the method on 32 open-weight models from nine families (0.6B--32B) with documented relation...
  </details>

- **2026-08-08** — Gregorius Reynaldi Pratama, Kuo-Kun Tseng — [Accurate Ensembles, Fragile Narratives: Multi-Scale Stacking and a Fidelity Audit of LLM-Generated Explanations for Credit Risk](http://arxiv.org/abs/2608.08126v1)
  <details><summary>📄 Abstract</summary>
  Credit scoring increasingly relies on models whose decision logic cannot be read off their parameters, in tension with supervisory expectations that adverse decisions be explainable. A common proposal closes that gap with a language model: compute feature attributions, hand them to an LLM, and let it write the rationale. We build such a system end to end and test whether the second half of the promise holds. The predictive component is a multi-scale stacking ensemble fusing four differently regu...
  </details>

- **2026-08-08** — Fengrong Wan, Chengcan Wu, Ningtao Lyu — [SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents](http://arxiv.org/abs/2608.08055v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents that assist users over weeks of conversation must remember what is currently true, not merely what was once said. Flat RAG diaries and Markdown logs optimize needle retrieval but under-serve currency, provenance, and ordered temporal reasoning (Maharana et al. 2024; Wu et al. 2024; Packer et al. 2023; Chhikara et al. 2025). We present SodaMem, an evidence-grounded temporal graph memory that (i) extracts typed FactEvents with mandatory provenance spans, (ii) pers...
  </details>

- **2026-08-07** — Jing Chen, Yang Sun, Li Zhang et al. — [Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework](http://arxiv.org/abs/2608.06909v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents increasingly operate through long-horizon trajectories involving user instructions, tool use, external observations, and memory. Existing benchmarks primarily evaluate behavioral outcomes but provide limited support for fine-grained attribution analysis. We introduce trajectory attribution and develop a benchmark and annotation framework for this task. The benchmark organizes heterogeneous trajectories under a unified component schema and provides annotations of...
  </details>

- **2026-08-07** — Sasan Mansouri, Daniel Saad, Mark Wahrenburg et al. — [FinRank: An Evidence-Grounded Benchmark for Financial Question Answering and Retrieval over SEC Filings](http://arxiv.org/abs/2608.07400v1)
  <details><summary>📄 Abstract</summary>
  Financial question answering is typically evaluated by answer correctness, yet in SEC filings a plausible and even numerically correct answer can be grounded in the wrong evidence. Similar facts and disclosures recur across sections of a filing, across reporting periods of the same firm, and across comparable firms. FinRank targets this provenance-sensitive retrieval problem by requiring systems to identify evidence for the intended entity, reporting period, and disclosure context. The benchmark...
  </details>

- **2026-08-07** — Milan Markovic, Goutham Indukuri, Somayajulu Sripada et al. — [Authoring and Management of Transparent Research Integrity Assessments of Randomised Clinical Trial Publications Using LLM-assisted Tools and Provenance Knowledge Graphs](http://arxiv.org/abs/2608.07202v1)
  <details><summary>📄 Abstract</summary>
  Systematic reviews of Randomised Controlled Trials (RCTs) are routinely used as evidence for clinical care guidelines. Such evidence has to meet high research integrity standards to prevent low quality or false research outputs influencing the clinical care. However, assessing research integrity of published RCTs is a complex process requiring manual effort, and potentially resulting in diverse opinions of the human assessors. This paper describes INSPECT-AI, an LLM-based interactive tool that a...
  </details>

- **2026-08-07** — Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski — [GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base](http://arxiv.org/abs/2608.06992v1)
  <details><summary>📄 Abstract</summary>
  We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as f...
  </details>

- **2026-08-06** — Nuzhat Khan, Indrakshi Dey — [Certifying Collective Reasoning in Multi-Agent Systems via Koopman Spectral Analysis](http://arxiv.org/abs/2608.05956v1)
  <details><summary>📄 Abstract</summary>
  Orchestrated collectives of large language model (LLM) agents that debate and vote are an emerging form of computational intelligence: the intelligent behaviour resides in the \emph{interaction}, not in any single agent. They improve task accuracy, yet remain black boxes at the system level: there is no principled test of convergence, no bound on the rounds needed, and no faithful account of what drove a decision. This paper develops a novel framework based on Koopman operator theory and validat...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-08-06** — Paweł Batorski, Przemysław Spurek, Paul Swoboda — [GROM: Gradient-Free Rapid One-Shot Machine Unlearning](http://arxiv.org/abs/2608.05783v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning has become a critical capability for safely removing specific, sensitive knowledge from large language models (LLMs). Current state-of-the-art approaches primarily rely on iterative, training-time unlearning via fine-tuning. However, even when utilizing parameter-efficient dimensionality reduction techniques like LoRA, gradient-based optimization remains computationally expensive and lacks explicit analytical formulations. It can also leave the targeted knowledge merely hidden...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 2 papers

- **2026-08-10** — Yuanchi Zhu, Kang An, Tengyue Wang et al. — [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](http://arxiv.org/abs/2608.09230v1)
  <details><summary>📄 Abstract</summary>
  Industrial-safety understanding requires more than detecting workers, equipment, and personal protective equipment. Models must also assess compliance, identify hazardous interactions, explain potential accident mechanisms, and recommend preventive actions. Existing safety datasets primarily focus on visual perception or isolated violation recognition and provide limited supervision for evidence-grounded reasoning. We introduce SafeSceneReason, a multimodal industrial-safety reasoning benchmark ...
  </details>

- **2026-08-08** — Wenwen He, Wenke Huang, Wei Yang Bryan Lim et al. — [Persuasive and Compliant Tendencies Predict Group Decision-Making in Humans and Language Models](http://arxiv.org/abs/2608.08199v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly involved in group decision-making with other LLMs and humans. Yet it remains unclear whether their influence is driven by persuasion-oriented expression or compliance-oriented accommodation. We introduce DecisionQE, a questionnaire-based framework for measuring each model's persuasive and compliant tendencies across multiple decision scenarios, and use the Werewolf game as an interactive testbed to study their effects on social influence and group ou...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 9 papers

- **2026-08-10** — Xinqi Yang, Kang An, Tengyue Wang et al. — [CircuitReason-1k: Benchmarking Long-Horizon Visual-to-Symbolic Reasoning inElectrical Circuits](http://arxiv.org/abs/2608.09374v1)
  <details><summary>📄 Abstract</summary>
  Electrical circuit analysis requires more than recognizing components in an image. A solver must ground symbols and labels, recover latent topology, select a physical model, formulate coupled equations, propagate intermediate quantities, and preserve units, signs, directions, and phase conventions. We introduce \benchmark, a benchmark of 1,000 authentic textbook problems for evaluating this complete long-horizon visual-to-symbolic reasoning process. Each problem pairs one or more circuit diagram...
  </details>

- **2026-08-10** — Zhenhang Shang, Yingzhe Yu, Kani Chen — [Repeated-Game Security for Restaking-Based Verifiable Inference](http://arxiv.org/abs/2608.09055v1)
  <details><summary>📄 Abstract</summary>
  Restaking-based protocols enable verifiable LLM inference without the high proving cost of zkML or the hardware trust assumptions of TEEs. Their security is commonly justified by a one-round slashing condition: a rational provider should not cheat when the expected penalty exceeds the cost saving from dishonest inference. This paper shows that this condition can overstate security when inference is supplied repeatedly under the same stake. We model verifiable inference as a discounted repeated g...
  </details>

- **2026-08-10** — Laurens Samson, Iva Gornishka, Gossa Lô et al. — [From Values to Benchmarks: Evaluating Large Language Models for Governmental Use in Dutch](http://arxiv.org/abs/2608.09925v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly being deployed in governmental settings, yet few existing evaluation frameworks jointly reflect the values of public administration and the linguistic requirements of non-English contexts. We present the "Grip on LLMs" framework, a systematic evaluation suite for Dutch governmental use developed in collaboration with domain experts from a major Dutch municipal organisation. Through an advisory board process, user research, and a survey of the users of a civ...
  </details>

- **2026-08-10** — Mahvish Nagda, Jihyeon Lee, Matthew Thompson et al. — [Towards Expert-level Medical AI for Real-time Video Consultations](http://arxiv.org/abs/2608.09861v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual interaction is the standard for patient-physician consultations, enabling natural communication and effective assessment of illness through non-verbal cues. While text-based AI has shown promise, it discards essential perceptual dimensions and limits patients who cannot articulate symptoms in writing. Early efforts to extend medical AI to audio-visual interaction have demonstrated feasibility but not reached clinician-level performance. Here, we provide the first demonstration of ex...
  </details>

- **2026-08-09** — Zhuowen Liang, Zhengxuan Zhang, Jiayang Wang et al. — [Beyond Tables: Doc2DB-Bench for Relationally Faithful Document-to-Database Construction](http://arxiv.org/abs/2608.08459v1)
  <details><summary>📄 Abstract</summary>
  Practical AI systems increasingly need to turn long, heterogeneous documents into queryable relational databases, not isolated spreadsheets. In domains such as finance, healthcare, education, transportation, and enterprise operations, downstream workflows rely on normalized schemas, entity identities, keys, cross-table relationships, and integrity constraints for analytics, compliance, auditing, and SQL-backed decision making. Existing Document-to-Table benchmarks are insufficient for this setti...
  </details>

- **2026-08-09** — Bernes Lorier Atabonfack, Zion Kongbi Nfo, Ahmed Tahiru Issah et al. — [From Manuals to Maintenance: Fine-Tuning MedGemma for Multi-Modal Imaging System Support in Low-Resource Settings](http://arxiv.org/abs/2608.08896v1)
  <details><summary>📄 Abstract</summary>
  Imaging device downtime is a major barrier to healthcare delivery in low- and middle-income countries (LMICs), often driven by limited access to specialized biomedical engineering support. We present a multi-modality medical equipment maintenance question-answering (QA) framework and demonstrate the fine-tuning of a medical foundation model for specialized technical troubleshooting tasks. Guided by a multi-country survey across nine LMICs, we curated technical manuals from MRI and ultrasound sys...
  </details>

- **2026-08-08** — Weijie Yuan, Geng Sun, Jiacheng Wang et al. — [Toward Intelligent Skies: Signal Processing and AI Foundations of Low-Altitude Wireless Networks](http://arxiv.org/abs/2608.08225v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of low-altitude aerial services and applications, driven by uncrewed aerial vehicles (UAVs), calls for a new class of digital infrastructure beyond conventional terrestrial networks. The low-altitude wireless network (LAWN) has been proposed as dynamically reconfigurable three-dimensional architectures that integrate aerial and ground nodes to provide connectivity, sensing, and control in open, safety-critical airspace. This tutorial presents a comprehensive treatment of LAWNs f...
  </details>

- **2026-08-07** — Fouad Bahrpeyma, Dirk Reichelt — [A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing](http://arxiv.org/abs/2608.07148v1)
  <details><summary>📄 Abstract</summary>
  Modern manufacturing imposes six coupled demands on adaptive control: local decisions with global consequences, partial observability, nonstationarity, reflex speed response with long horizon effects, delayed and diffuse outcomes, and dynamics that resist explicit modeling. Cooperative multiagent reinforcement learning (MARL), posed as a Dec-POMDP under centralized training with decentralized execution, is a particularly natural formalism for these demands. This paper adopts a MARL centered scop...
  </details>

- **2026-08-07** — Songheng Zhang, Emily Aurelia, Anthony Tang — [UncertaintyVis: Preserving Linguistic Uncertainty in Automated Text-to-Chart Generation](http://arxiv.org/abs/2608.07093v1)
  <details><summary>📄 Abstract</summary>
  Data-rich documents pair narrative text with quantitative claims, and authors routinely qualify those claims with linguistic uncertainty markers such as "nearly," "approximately," or "at least." Automated text-to-chart systems discard these markers, producing visualizations that appear definitive even when the source text expresses hedged or incomplete knowledge. Readers may then over-interpret precision and misjudge author intent. We present UncertaintyVis, a system that preserves linguistic un...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 163 papers

- **2026-08-10** — Hongwei Yao, Yiming Liu, Meihui Chen et al. — [ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents](http://arxiv.org/abs/2608.09476v1)
  <details><summary>📄 Abstract</summary>
  Cowork agents may complete benign tasks while disclosing protected data, manipulating unauthorized state, invocate unauthorized API. We define behavioral safety and introduce ActBench, a self-evolving benchmark that evaluates such behavior risk from execution trajectories rather than final responses. Each case pairs a benign task with an adversarial variant that preserves its instruction, configuration, initial state, rating model, and trusted records while injecting a task-reachable payload. Ac...
  </details>

- **2026-08-10** — Panayotis Mertikopoulos — [Regret, equilibrium, and learning in games: A guided tour](http://arxiv.org/abs/2608.09389v1)
  <details><summary>📄 Abstract</summary>
  This note aims to serve as an entry point to the literature on learning in games, a topic with significant theoretical appeal and a wide range of applications -- from machine learning and data science to economics and beyond. Our presentation is structured around two complementary viewpoints: We first consider a single agent -- the learner -- engaged in a sequential decision process in an unknown, non-stationary, and possibly adversarial environment. We then examine what happens when the environ...
  </details>

- **2026-08-10** — Juntian Zhu, Guanpu Chen, Tongtian Zhu et al. — [Distributed Team Orchestration via Supervisor Networks: Convergence, Optimality, and Resilience](http://arxiv.org/abs/2608.09256v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study zero-sum potential team games with a supervisor network, where agents rely on supervisor-provided belief information rather than accurate common beliefs. The main challenge is that such belief information can be inaccurate because of supervisors' belief-estimation errors and the misreporting of joint actions by Byzantine teams. We propose the distributed team-orchestrating algorithm (DTOA), which combines team fictitious play with supervisor-based distributed belief learn...
  </details>

- **2026-08-10** — Sam Siavoshian, Omar Ramadan, Amir K. Saeed et al. — [ChronoState: Hidden Elapsed-Time Conditioning for Temporal-State Action Selection in Frozen-Backbone Language Models](http://arxiv.org/abs/2608.09124v1)
  <details><summary>📄 Abstract</summary>
  Temporal decisions in language-model systems often depend on both symbolic task state and elapsed wall-clock time, such as cache expiration, job completion, quota resets, deadlines, or stale sessions. We study whether elapsed time can be supplied as a non-token, system-side scalar and composed with visible symbolic state by a frozen-backbone language model. We introduce ChronoState, a compositional temporal-state benchmark in which symbolic state appears in the prompt, elapsed seconds tau are su...
  </details>

- **2026-08-10** — Jakub Kacper Szeląg, Aydin Abadi, Mohammad Naseri — [Defining Decentralization: An Ontological Perspective](http://arxiv.org/abs/2608.09748v1)
  <details><summary>📄 Abstract</summary>
  Decentralization as a concept in computer science has existed for over half a century. Despite its fundamental role across domains such as security, distributed computing, artificial intelligence, cloud infrastructures, and Internet of Things (IoT) architectures, there remains no universally accepted definition of decentralization applicable across computer communication systems. This has become increasingly problematic with the emergence of decentralized AI and machine learning paradigms, inclu...
  </details>

- **2026-08-10** — Jiajun Xu, Yanghao Zhou, Jingyun Liao et al. — [VideoVIBE: A Video-Grounded Diagnostic Benchmark for One-Shot Interactive Website Generation](http://arxiv.org/abs/2608.09573v1)
  <details><summary>📄 Abstract</summary>
  Natural-language-driven "vibe coding" enables the one-shot generation of visually rich and interactive web applications, yet reliable assessment of their quality has not kept pace. Existing evaluations often score isolated artifacts or final task outcomes, offering limited evidence about which failures occur and why. We introduce VideoVIBE, a video-grounded benchmark that transforms human-operated webpage recordings into fine-grained diagnostic tasks. It contains approximately 1.7K diagnostic Vi...
  </details>

- **2026-08-10** — Zhi-Fu Gao, Hui Wang, Luiz Carlos Garcia de Andrade et al. — [Dynamical Barbero--Immirzi field coupled to quintessence: gravitational-wave propagation constraints and next-generation forecasts](http://arxiv.org/abs/2608.09487v1)
  <details><summary>📄 Abstract</summary>
  We investigate the imprints of a dynamical Barbero--Immirzi (BI) field $γ(x)$ coupled to a quintessence scalar field $φ$ on gravitational-wave (GW) propagation. In the framework of Einstein--Cartan--Holst gravity, promoting $γ$ to a dynamical scalar introduces a stress--energy that back-reacts on the metric, modifying the GW friction term. A minimal coupling $\proptoβ\,φ^2γ^2$ between the BI field and quintessence leads to a two-parameter extension of the Belgacem--Maggiore parametrization, char...
  </details>

- **2026-08-10** — Yueyang Cang, Xiaoteng Zhang, Zhiyuan Ning et al. — [FeedbackTrack: Visual-Cortex-Inspired Cross-Frame Feedback for Transformer Tracking](http://arxiv.org/abs/2608.09369v1)
  <details><summary>📄 Abstract</summary>
  Visual object tracking requires effective temporal integration, yet most Transformer trackers still rely on predominantly feed-forward feature extraction. Existing temporal mechanisms typically update templates, prompts, queries, or prediction states, while intermediate representations are rarely reused to modulate corresponding processing stages. We propose \textbf{FeedbackTrack}, a visual-cortex-inspired framework that introduces sparse, group-level layer-aligned cross-frame feedback into pret...
  </details>

- **2026-08-10** — Zhihang Liu, Mei-Po Kwan, Jinlin Wu et al. — [GeoPhysAdapter: Scale-Matched Geophysical Adaptation for Cross-Domain Landslide Mapping with Vision Foundation Models](http://arxiv.org/abs/2608.09325v1)
  <details><summary>📄 Abstract</summary>
  Newly triggered landslides rarely carry immediate annotations, so cross-domain transferability determines the value of landslide mapping for emergency response and regional risk assessment. Vision foundation models have strengthened representational transfer, yet on unseen regions, events, and data sources they still generate high-confidence false alarms. Terrain, material, and rainfall triggering can constrain such errors, but their supports are local, regional, and event-scale, so that resampl...
  </details>

- **2026-08-10** — Tianhao Jiang, Hang Gu, Teng Wang et al. — [UnionSparse: An Index-Efficient Sparsity Framework for Low-Bit Sparse LLM Inference on Edge](http://arxiv.org/abs/2608.09291v1)
  <details><summary>📄 Abstract</summary>
  Edge LLM inference combines sparsity and low-bit quantization to meet device memory, latency, and power limits. Yet quantization shrinks weight payloads without proportionally reducing sparse metadata, so index traffic and nonzero extraction become critical SpMM bottlenecks. We introduce the Payload-to-Metadata Ratio (PMR) and show that improving PMR raises effective compute intensity in decoding.   We present UnionSparse, an index-efficient framework that combines Index-Efficient Bitmap Encodin...
  </details>

- **2026-08-10** — Steve Woollaston, Brendan Flanagan, Hiroaki Ogata — [Accurate but Natural? Diagnosing Grammatical and Idiomatic Gaps in Japanese EFL Writing](http://arxiv.org/abs/2608.09289v1)
  <details><summary>📄 Abstract</summary>
  Second language writing research distinguishes grammatical accuracy from native-like idiomaticity, yet automated writing evaluation often conflates these dimensions. This study introduces a layered LLM-correction pipeline that isolates structural errors from unnaturalness by generating literal error corrections and idiomatic revisions for 3,830 English writing samples from 120 Japanese junior high school students. Applying the regex-based CEFR-J grammar extractor, we quantify two diagnostic meas...
  </details>

- **2026-08-10** — Adrian Li, Kelong Mao, Yudong Guo et al. — [ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons](http://arxiv.org/abs/2608.09282v1)
  <details><summary>📄 Abstract</summary>
  Real-world shopping often requires constructing a basket of complementary items rather than retrieving a single product. Such combo-shopping tasks arise in device setup, meal preparation, event planning, and group takeout ordering, requiring joint reasoning about item compatibility, availability, store-level requirements, delivery fees, coupons, and budgets. Evaluation is challenging because multiple baskets may satisfy the same request, making exact-match metrics unsuitable, whereas semantic ev...
  </details>

- **2026-08-10** — Zenan Li, Ziran Yang, Peiyang Song et al. — [P$^{3}$: Joint Program-and-Proof Planning for Verified Code Generation](http://arxiv.org/abs/2608.09277v1)
  <details><summary>📄 Abstract</summary>
  Verified code generation asks a large language model (LLM) to generate both an executable program and a machine-checkable proof that the program meets a formal specification, promising software that is correct by construction. The de facto workflow decouples the two halves of the problem: first synthesize a program, then attempt to prove it correct. We observe that this sequential pipeline can be both ineffective and inefficient in practice. A program generated without anticipating its proof can...
  </details>

- **2026-08-10** — Peiwen Li, Shiyang Zhang, Yangtian Zhang et al. — [MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts](http://arxiv.org/abs/2608.09251v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based multi-agent systems have recently shown strong potential for complex, long-horizon tasks. However, existing methods mainly rely on coarse prompt-level differentiation without parameter adaptation for diverse subtasks, resulting in insufficient inter-agent heterogeneity and limited specialized capability that bottleneck performance on tasks with complex requirements. To address this, we introduce a Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts (M...
  </details>

- **2026-08-10** — Yongsong Huang, Xiaofeng Liu, Tomo Miyazaki et al. — [Right Answer, Wrong Heat: Explanation-Aware Evaluation and Thermal-Grounded Feedback for MLLMs on Infrared Images](http://arxiv.org/abs/2608.09145v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal large language models (MLLMs) are increasingly applied to infrared images, where they are commonly scored by answer accuracy alone. However, a correct answer does not ensure that the model's explanation is grounded in infrared thermal evidence. We introduce an explanation-aware evaluation framework that separates answer correctness, output-level explanation groundedness, and thermal grounding for infrared visual questions. Using a Dual-LLM Consensus Judge with a prelim...
  </details>

- **2026-08-10** — Mengxian Lyu, Cheng Peng, Tim Jang et al. — [An Agentic Generative Large Language Model for Treatment Planning of Colorectal Cancer](http://arxiv.org/abs/2608.09142v1)
  <details><summary>📄 Abstract</summary>
  Treatment planning in precision oncology requires synthesizing heterogeneous patient information with rapidly evolving clinical guidelines to ensure guideline-concordant care. While large language models (LLMs) show promise in many diagnostic tasks, their adoption for high-stakes treatment planning is hindered by complex reasoning, adherence to timely clinical guidelines, and safety concerns. In this study, we present GatorOnco, an agentic LLM for colorectal cancer (CRC) treatment planning. Gato...
  </details>

- **2026-08-10** — Jinkun Hou, Zhuo Liu, Huimin Ren et al. — [RISE-RL: Rubric-Informed Selective Exploration for Open-Ended Reinforcement Learning](http://arxiv.org/abs/2608.09123v1)
  <details><summary>📄 Abstract</summary>
  Aligning Large Language Models (LLMs) for open-ended tasks is challenging because responses must satisfy multidimensional criteria without following a single correct generation trajectory. Existing rubric-based reinforcement learning (RL) methods compress fine-grained criterion-level feedback into scalar rewards, making persistent capability gaps difficult to target under limited on-policy exploration. We propose $\textbf{RISE-RL}$ (Rubric-Informed Selective Exploration), which uses repeatedly m...
  </details>

- **2026-08-10** — Chengying Huan, Yudong Liu, Jianguo Wang et al. — [RVANNS: Mixed-Precision Indexing and Locality-Aware Graph Traversal on RISC-V](http://arxiv.org/abs/2608.09077v1)
  <details><summary>📄 Abstract</summary>
  Approximate nearest neighbor search (ANNS) on CPUs is increasingly constrained by candidate-vector movement and decoding rather than peak arithmetic throughput. Although the RISC-V Vector Extension (RVV) provides vector-length-agnostic execution and LMUL-based register grouping, generic low-precision decoding still incurs conversion overhead, while irregular graph traversal generates scattered accesses that degrade cache locality and memory-level parallelism.   We present RVANNS, an RVV-oriented...
  </details>

- **2026-08-10** — Xin Zhou, Chun Yong Chong, Kisub Kim et al. — [A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents](http://arxiv.org/abs/2608.09072v1)
  <details><summary>📄 Abstract</summary>
  Large language model-powered coding agents are increasingly used to modify existing code repositories, for example, by adding features or fixing bugs. Yet existing repository-level benchmarks typically evaluate only whether the final patch passes tests. Satisfying a user request requires a long chain of interdependent reasoning and decisions: an agent must recover explicit and implicit requirements, formulate a repository-grounded implementation plan, and translate it into correct code. A pass/f...
  </details>

- **2026-08-10** — Rui Tang, Qiangqiang Liu, Yichi Zhang et al. — [Context Is Not Authority: Structured Runtime Governance for Financial Market Agents](http://arxiv.org/abs/2608.09025v1)
  <details><summary>📄 Abstract</summary>
  Financial agents can turn correct context into an unauthorized effect: a customer-facing commitment, trade, or deployed policy. We present SAGE-Fin, a finance-specific authority-handoff contract that makes the proposed effect, not merely its text, the object of runtime control. SAGE-Fin compiles proposals into typed, adapter-bound candidates; records missing or stale institutional obligations as coverage debt; contracts authority under current market, account, policy, and dialogue state; and req...
  </details>

- **2026-08-10** — Zhaochen Lan, Mengxiang Lin — [RoboSeg: Online Part-Level Semantic Reconstruction for Robotic Manipulation via a Single Eye-in-Hand Camera](http://arxiv.org/abs/2608.09778v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation requires perception systemsthat identify actionable parts such as handles, rims, triggers,and tool tips, not merely object categories or point clouds. This paper presents RoboSeg, a part-level semantic reconstructionsystem that links vision-language model (VLM) functional-partdiscovery, asynchronous online RGB-D semantic reconstruc-tion, and task-oriented grasp generation without requiring CAD models or pre-scanned meshes. RoboSeg queries a VLM onthe initial RGB observation ...
  </details>

- **2026-08-10** — Jingkai Wang, Zihan Tang, Gu Zhang et al. — [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](http://arxiv.org/abs/2608.09771v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action policies rely on large multimodal backbones to jointly perform perception, language conditioning, and action generation at every control step. Much of this capacity supports open-domain semantics, whereas continuous robot manipulation primarily requires compact representations of observations, actions, and the transitions induced by actions. Pixel-level world models provide another route, but predicting visual details irrelevant to control can be unnecessarily expensive. W...
  </details>

- **2026-08-10** — Yunhao Zhao, Zhenyang Ni, Haoyang Chen et al. — [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](http://arxiv.org/abs/2608.09410v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language-action (VLA) policies have acquired broad manipulation skills, but typically generate each action chunk from the current observation or a short fixed-length history. However, real-world manipulation is often non-Markovian, requiring robots to retain and reason over task-relevant information from long-horizon interaction histories to determine the next action. To address this challenge, we propose HyMeS, a hybrid learning framework that leverages the reasoning and memory-ma...
  </details>

- **2026-08-10** — Grzegorz Jamróz — [Competitive mediator games and urban CAV routing markets](http://arxiv.org/abs/2608.09894v1)
  <details><summary>📄 Abstract</summary>
  Inspired by possible future markets of autonomous routing and driving (ARAD), we introduce competitive mediator games and their equilibria which generalize the (coarse) correlated equilibria, which have become a popular research area recently as they not only can be more socially efficient than Nash equilibria but also are limits of algorithmic no-regret multi-agent learning dynamics. We discuss the basic properties of competitive mediator games and prove that in the generic setting of anonymous...
  </details>

- **2026-08-10** — Tim J. Boonen, Wing Fung Chong, Kenneth Tsz Hin Ng et al. — [Nash Peer-to-Peer Insurance Bargaining under Price Fairness and Coalitional Stability](http://arxiv.org/abs/2608.09859v1)
  <details><summary>📄 Abstract</summary>
  We study peer-to-peer (P2P) insurance contracting between a risk-averse P2P reinsurer and multiple risk-averse peers in an asymmetric Nash-bargaining framework, where all agents seek to improve expected utility relative to their disagreement points. Consistent with the expected value premium principle, we impose a price-fairness condition requiring each peer's expected contribution to be based on a common loading applied to the peer's expected loss. To justify the bargaining formulation relative...
  </details>

- **2026-08-10** — Aimilios Hadjiliasi, Louis Nisiotis — [CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems](http://arxiv.org/abs/2608.09848v1)
  <details><summary>📄 Abstract</summary>
  The development of embodied Intelligent Virtual Agents (IVAs) that have cognitive capabilities in real-time interactive virtual environments remains a challenge, even with today's advancements in technology. Existing architectures are often focused on either the implementation of low-level reactive control systems that are constrained by commercial game engines, or high-level representations of reasoning models that can be difficult to implement in virtual worlds. This paper builds on that notio...
  </details>

- **2026-08-10** — Jutao Xiao, Yuan Qu, Dongsheng Ma et al. — [From Diagnosis to Correction: Benchmarking and Improving Real-World Table Parsing](http://arxiv.org/abs/2608.09842v1)
  <details><summary>📄 Abstract</summary>
  Recent document parsers achieve table TEDS scores above 93 on OmniDocBench v1.6, yet community feedback and our audit reveal persistent failures on complex real-world tables. To quantify this gap, we introduce TableParseMap, a diagnostic benchmark of 916 real-world tables organized into five challenging scenarios and nine failure types. The strongest evaluated parser achieves only 85.03 TEDS, showing that aggregate benchmark scores conceal substantial weaknesses. Our analysis attributes these fa...
  </details>

- **2026-08-10** — Qu Tang, Benhui Zhuang, Bo Yuan et al. — [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](http://arxiv.org/abs/2608.09730v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies. They excel at efficient closed-loop control but do not explicitly model how physical scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage pretrained video world models to capture spatiotemporal evolution, yet retaining future generation or a large video backbone in the control loop substantially increases inference cost. We introduce World Tokens, an embodied policy architec...
  </details>

- **2026-08-10** — Shulin Tian, Ziqi Huang, Fan Zhang et al. — [Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models](http://arxiv.org/abs/2608.09666v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in visual generative models have enabled high-quality image and video generation, but evaluating these models often demands sampling hundreds or thousands of images or videos, which is computationally expensive. Existing evaluation methods also rely on rigid pipelines that overlook specific user needs and provide numerical results without clear explanations. Mimicking how humans quickly form impressions of a model's capabilities from only a few samples, we propose the Evaluation ...
  </details>

- **2026-08-10** — Yuke Li, Xuehan Hou — [Hallucination-Free GUI Grounding via Regression-Free Layout-Aware Matching](http://arxiv.org/abs/2608.09654v1)
  <details><summary>📄 Abstract</summary>
  GUI agents are shifting from metadata-dependent large language models to purely visual multimodal large language models (MLLMs) that operate directly on screenshots. The core task, GUI grounding, requires translating abstract user instructions into precise element coordinates. This task faces a persistent dual obstacle: conventional grounding models lack the semantic richness to interpret abstract instructions, while end-to-end MLLMs suffer from coordinate hallucinations caused by deficient fine...
  </details>

- **2026-08-10** — Haiyang Yan, Jinyue Guo, Yanchao Zhang et al. — [NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation](http://arxiv.org/abs/2608.09636v1)
  <details><summary>📄 Abstract</summary>
  Accurate 3D neuron segmentation in fluorescence microscopy is critical for neuroscience. However, the sparse and elongated morphology of neurons poses significant challenges to existing segmentation methods. These methods struggle to preserve both local details and global topology, leading to fragmented results. To address this, we propose NeuroRefiner, a multi-agent system that formalizes the human expert workflow involving iterative global observation and local editing. Specifically, NeuroRefi...
  </details>

- **2026-08-10** — Hui Xue, Fan Yang — [Rethinking Self-Evolving Agents: Do We Still Need Prescribed Optimization Pipelines?](http://arxiv.org/abs/2608.09629v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents are usually built around prescribed optimization pipelines: the framework decides how to gather evidence, revise a persistent artifact, select candidates, and stop. We ask whether this task-specific procedure remains necessary when a frontier model acts as the optimizer. We introduce Open-Ended Optimization (OEO), which keeps the objective, permitted interactions, resource budget, data boundary, and evaluation fixed while allowing the optimizer to compose the improvement pro...
  </details>

- **2026-08-10** — Yan Rong, Fengji Ma, Xu Li et al. — [AudioMap: Cloze-and-Choice Reinforcement Learning for Time-Aware Dense Audio Captioning](http://arxiv.org/abs/2608.09559v1)
  <details><summary>📄 Abstract</summary>
  Time-aware dense audio captioning (TDAC) aims to generate multiple fine-grained attributes (dense) of the audio with precise time boundaries (time-aware). Existing methods struggle to achieve these two goals and mainly rely on supervised fine-tuning, yielding sub-optimal performance. While reinforcement learning (RL) shows promise, applying it to TDAC faces two main challenges: (1) existing rewards are too coarse to supervise multi-event, multi-attribute, and multi-relation descriptions in a fin...
  </details>

- **2026-08-10** — Kayvan Kousha, Mike Thelwall — [Does ChatGPT score research quality differently by gender?](http://arxiv.org/abs/2608.09552v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are being considered for research evaluation, raising concerns about the introduction of AI bias. This study investigates whether ChatGPT research quality scores differ by first-author gender using 89,744 journal articles from the UK Research Excellence Framework (REF) 2021. Author information was withheld from ChatGPT to avoid direct gender bias. Nevertheless, male first-authored papers had slightly higher ChatGPT scores in most Units of Assessment (UoAs), especiall...
  </details>

- **2026-08-10** — Junyu Wu, Shiqin Nie, Youyi Kou et al. — [verdi: retrieval is not transfer for continual world model optimization](http://arxiv.org/abs/2608.09537v1)
  <details><summary>📄 Abstract</summary>
  Foundation world models have made remarkable progress in planning, simulation, and embodied intelligence. However, optimizing a pretrained world model toward a user-specified objective remains difficult: each campaign typically rediscovers optimization strategies from scratch, and the resulting knowledge rarely transfers to the next model. Existing research agents automate the optimization loop but treat successful strategies as directly reusable recipes, without principled safeguards for when t...
  </details>

- **2026-08-10** — Su-Hyeon Kim, Jiwan Mun, Yo-Sub Han — [One Adapter Pair per Model: A Universal Activation Interface for Language Models](http://arxiv.org/abs/2608.09521v1)
  <details><summary>📄 Abstract</summary>
  Activation-based tools are usually tied to one model's native hidden space, requiring probes, sparse autoencoders, and natural-language interpreters to be rebuilt or rediscovered for each new language model. We present a Universal Activation Bus, a framework that provides a common activation interface across compatible language models. Using a small set of source models, we learn a shared dense space together with one lightweight linear encoder--decoder adapter pair per model. After source train...
  </details>

- **2026-08-10** — Yuting Liu, Wei Wu, Jianzhe Zhao et al. — [Learning Preference Adaptation for Large Language Model Personalization via Verbal Reinforcement Learning](http://arxiv.org/abs/2608.09507v1)
  <details><summary>📄 Abstract</summary>
  Natural language user preferences provide an interpretable interface for LLM personalization. However, universal preference summaries often contain information irrelevant to a particular downstream task. Directly supplying the full preference summary therefore wastes context capacity and introduces cross-task distraction, while manually designing task-specific preference views is difficult to scale. In this work, we study \emph{task-specific preference adaptation}: given a universal user prefere...
  </details>

- **2026-08-10** — Max Dupré la Tour — [Balanced Fair Division for Three Agents under General Valuations and Laminar Constraints](http://arxiv.org/abs/2608.09437v1)
  <details><summary>📄 Abstract</summary>
  We study fair allocations of indivisible items under general set valuations. We prove that every instance with three agents and arbitrary real-valued valuations admits a balanced allocation that is envy-free up to one good and one chore (EF$1^c_g$). This directly implies balanced EF$1$ when each valuation is either monotone nondecreasing or monotone nonincreasing. We also show that balanced EF$1$ cannot be guaranteed without monotonicity: there exists an instance with three agents, nine items, a...
  </details>

- **2026-08-10** — Rose Cymbler, Daniel Guez, Laurent Fabre — [Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law](http://arxiv.org/abs/2608.09393v1)
  <details><summary>📄 Abstract</summary>
  We identify and quantify temporal misgrounding: the systematic retrieval and citation of the currently in-force version of a legal article when the applicable version is an earlier or future one. Standard legal RAG treats the corpus as static; we argue legal question answering is a temporally-indexed retrieval problem. We introduce FiscalQA Pro, pairing a versioned corpus of 32,436 article-versions of the French tax code (93 years, 1938-2031) with an all-model-hard temporal-reasoning track: 209 ...
  </details>

- **2026-08-10** — John S. H. Baxter, Elodie Germani — [Foundational values for foundation models](http://arxiv.org/abs/2608.09377v1)
  <details><summary>📄 Abstract</summary>
  Research values, properties with a distinctive normative dimension, often affect how technological research is performed in both direct and indirect ways by influencing how technical decisions are made. In machine learning for medical imaging, understanding these values can be important for understanding why particular researchers justify the decisions made in their publications and explain why certain technologies become ubiquitous (or not) in the scientific literature and in the clinic. This a...
  </details>

- **2026-08-10** — Run Yang, Weihang Wang, Boheng Sheng et al. — [MemeMind: Reference-Guided Trace Construction for Offline Context Optimization](http://arxiv.org/abs/2608.09316v1)
  <details><summary>📄 Abstract</summary>
  Offline context optimization improves an agent by revising its instructions and examples while keeping the model frozen. This approach learns from rollouts on an adaptation set, but some queries produce only failed rollouts. In these cases, the optimizer sees no successful example of how the available tools can reach the correct answer. We introduce MemeMind, which uses an offline reference answer to recover this missing experience. TraceBuilder identifies the evidence required by the reference,...
  </details>

- **2026-08-10** — Zhengfeng Li, Lei Zhang, Xianwei Wu et al. — [OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review](http://arxiv.org/abs/2608.09290v1)
  <details><summary>📄 Abstract</summary>
  LLM-based code review agents promise scalable, always-on review, yet current systems suffer from two intertwined weaknesses: (1) non-determinism--unbounded tool use makes review outcomes unstable, and (2) context locality--the reviewer's access remains bounded to the diff, capping discoverable issue depth. Both give rise to three challenges: misaligned context retrieval, a coherence-efficiency trade-off in multi-file pull requests, and hallucinated comments that erode trust. To address these, we...
  </details>

- **2026-08-10** — Geonho Lee, Min-Soo Kim — [SafeQL: Search-based Refinement for Safe and Efficient LLM-based Text-to-SQL](http://arxiv.org/abs/2608.09260v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have advanced Text-to-SQL by enabling natural language interfaces to databases without task-specific fine-tuning. However, existing LLM-based systems remain unreliable, often generating SQL queries that are invalid under the database schema, referencing non-existent tables, attributes, functions, or values. Such errors persist because interactions with the database management system (DBMS) are typically limited to error messages, leaving it in a largely passive role ...
  </details>

- **2026-08-10** — Xuanchen Li, Haitao Li, Yujia Zhou et al. — [Different Feedback, Different Updates: Selective Self-Learning from User Interactions for Large Language Models](http://arxiv.org/abs/2608.09109v1)
  <details><summary>📄 Abstract</summary>
  User feedback offers natural supervision for persistent LLM improvement, but a single message may support multiple behavioral changes with different scopes of generalization. We introduce SLIFT, a selective self-learning framework built on a task-relative view of user feedback. SLIFT decomposes each feedback message into atomic components and interprets each component relative to the original task as Fix, Spec, or Null: requirements for task validity, compatible condition-specific refinements, o...
  </details>

- **2026-08-10** — Jing Ning, James D. Braza — [TLDChoiceNet: Quantitatively Choosing a Transfer Learning Dataset](http://arxiv.org/abs/2608.09091v1)
  <details><summary>📄 Abstract</summary>
  Transfer learning is particularly useful in settings with limited training data, and within image classification it is common to transfer learn upon massive datasets like ImageNet , CIFAR-100, or COCO . Qualitatively, it seems a transfer learning dataset should have both more classes and more examples per class than the fine tuning dataset; however, a quantitative method to choose the best transfer learning dataset does not currently exist. In this paper, we design TLDChoiceNet, a model to choos...
  </details>

- **2026-08-10** — Avijit Roy, Proma Roy, Hrishitva Patel — [Measuring the Tokenization Premium: A Cost Audit for Underserved Language Communities](http://arxiv.org/abs/2608.09046v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as general-purpose educational and technical assistance systems, but their underlying infrastructure does not treat languages equally. One underexamined source of disparity is tokenization: semantically equivalent content can require substantially different token counts across languages, affecting API cost, latency, and usable context length before a model is invoked. We introduce the Tokenization Equity Audit (TEA), a reproducible benchmark for me...
  </details>

- **2026-08-10** — Alessia Danagoulian, Benli Jiang, Nicholas Russo et al. — [Wrinkling in Selected Polymer Thin Films Induced by Combined Ion Beam and Humidity Exposure](http://arxiv.org/abs/2608.09041v1)
  <details><summary>📄 Abstract</summary>
  This study investigates ion beam sputtering (IBS)-induced surface wrinkling phenomena in three polymers with varying hydrophilicity: poly-hydroxy-ethyl-methacrylate (pHEMA), poly-4-vinyl pyridine (p4VP), and poly-2,4,6,8-tetramethyl-2,4,6,8-tetravinylcyclotetrasiloxane (pV4D4). It is observed that pHEMA and p4VP films wrinkle only when exposed to ion bombardment and subsequent water vapor exposure. No wrinkling is observed in pV4D4 under these same conditions. X-ray photoelectron spectroscopy (X...
  </details>

- **2026-08-10** — Haohao Zhu, Xiaolin Shi, Jiayu Zhou — [ELICITED: EHR-grounded Longitudinal Interactive Conversations for Information-seeking Triage Evaluation and Decision-making](http://arxiv.org/abs/2608.09024v1)
  <details><summary>📄 Abstract</summary>
  Emergency-department (ED) triage requires clinicians to rapidly identify patients who need immediate attention, determine who can safely wait, and prioritize limited clinical resources. At presentation, however, information may be limited to a chief complaint and initial vital signs. Clinically important details, including symptom onset and progression, associated symptoms, medical history, and medication use, are often obtained through focused conversation. Effective triage therefore requires c...
  </details>

- **2026-08-10** — Bob Holdom — [Superselected ghost theory: perturbation theory](http://arxiv.org/abs/2608.09017v1)
  <details><summary>📄 Abstract</summary>
  A superselection rule based on an exact ghost parity can endow a ghost QFT with a probability interpretation. However, this ghost parity is not respected at finite order in the standard perturbative expansion. A ghost-parity-preserving perturbation theory (Z$_2$PT) is obtained through a similarity transformation of the Hamiltonian, $h=g H g^{-1}=h_0+h_1+h_2+...$. The resulting expansion is reminiscent of old-fashioned perturbation theory (OFPT) with some significant differences. The superselecti...
  </details>

- **2026-08-10** — Shiwei Gan, Xiao Liu, Yafeng Yin et al. — [SignLlama: Enhancing Gloss-free Sign Language Translation by Prioritizing Visual Features for LLMs](http://arxiv.org/abs/2608.09006v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable success across a wide range of tasks. However, fine-tuning LLMs for Gloss-Free Sign Language Translation (GFSLT) remains a challenge. In this paper, we investigate how to effectively adapt LLMs to the GFSLT task. We show that there are two key issues that need to be solved: (1) the inherent distributional gap between visual feature inputs and text feature inputs makes it difficult for LLMs to interpret visual inputs; and (2) existing approach...
  </details>

- **2026-08-10** — Pouya Ghiasnezhad Omran, Soujanya Lanka, Qin Zhang et al. — [Muscle Memory for Agents: Compile not Merely Retrieve](http://arxiv.org/abs/2608.08995v1)
  <details><summary>📄 Abstract</summary>
  Memory for LLM agents has converged on a single architectural pattern: store experience as text, embeddings, reflections, or rules; retrieve at inference time; let a general-purpose orchestrator interpret what to do. This paper argues that the pattern is the wrong default for personalization. We position Muscle Memory - the practice of compiling recurring user intent into purpose-built specialist agents - as a distinct memory paradigm from retrieval, and we argue that compilation is a better fit...
  </details>

- **2026-08-10** — Haris Aziz — [Best-of-Both-Worlds Fairness and Pareto Optimality](http://arxiv.org/abs/2608.08966v1)
  <details><summary>📄 Abstract</summary>
  We consider fair allocation of indivisible items among agents with non-negative and additive valuations. The goal is to construct a lottery over deterministic allocations whose induced fractional allocation is envy-free, while every realised allocation is envy-free up to one item and Pareto optimal. We show that this is always possible for two agents. We then prove a stronger result that there always exists a lottery over deterministic allocations whose induced fractional allocation is envy-free...
  </details>

- **2026-08-09** — Tianli Tao, Ziyang Wang, Emma Robinson et al. — [Decoding Phenotypes: A Framework for Fusing Genomic Language Models and Neuroimaging](http://arxiv.org/abs/2608.08926v1)
  <details><summary>📄 Abstract</summary>
  Neuroimaging and genetic testing are two important clinical references for nervous system diseases, offering complementary diagnostic information. However, integrating genomic and neuroimaging data for precise disease diagnosis is challenging due to cross-modality heterogeneity. Existing imaging-genetics approaches mainly encode genetic information as hard-coded labels, which lose the local sequence context around disease-associated variants. To address this limitation, we propose GeneFuse, a mu...
  </details>

- **2026-08-09** — Qucheng Gao, Zuyi Yang, Xiao Chen — [Clustered Attractor Manifolds and Dynamical Condensation in Self-Attention](http://arxiv.org/abs/2608.08922v1)
  <details><summary>📄 Abstract</summary>
  Transformer layers generate state-dependent interaction networks: token representations determine the attention matrix, which in turn updates the representations. We study this feedback in a minimal normalized self-attention dynamics and identify the overlap gap as the central quantity governing its attractor structure in the thermodynamic limit. When tokens form internally aligned clusters and their similarity to members of the same cluster exceeds that to every other cluster by a nonvanishing ...
  </details>

- **2026-08-09** — Nakul Poudel, Richard Simon, Cristian A. Linte — [Toward Mask Annotation-Free Surgical Instrument Segmentation from Endoscopic Images Using Text-Prompted Segment Anything Model 3 (SAM3)](http://arxiv.org/abs/2608.08844v1)
  <details><summary>📄 Abstract</summary>
  Surgical instrument segmentation is a fundamental task for computer-assisted interventions, yet most existing methods rely on pixel-level annotations or manual spatial prompts, which limit scalability and automation. The recently introduced Segment Anything Model 3 (SAM3) offers a pathway to annotation-free, automatic segmentation via text-based prompting; however, the instrument name as a text prompt could not be directly used due to a large domain gap. To overcome these limitations, we propose...
  </details>

- **2026-08-09** — Yunjia Li, Menglin Wu, Junyu Dai et al. — [Beyond Reconstruction: Full-Context Generative DiT for Music Generation](http://arxiv.org/abs/2608.08787v1)
  <details><summary>📄 Abstract</summary>
  Hybrid music generators combine the long-range planning of an autoregressive language model with the fidelity of a diffusion- or flow-based acoustic renderer. Yet renderers are trained with clean, target-derived codec tokens but deployed with imperfect language-model predictions, creating codecinterface exposure bias. Rather than treating rendering as a simple reconstruction task,we formulate it as full-context generation from an imperfect discrete plan.We introduce FullDiT, a conditional DiT th...
  </details>

- **2026-08-09** — Xiutian Zhao, Philipp Koehn, Björn Schuller et al. — [Multilingual Emotion Neurons in Large Audio-Language Models](http://arxiv.org/abs/2608.08772v1)
  <details><summary>📄 Abstract</summary>
  Emotion is central to human communication, and its expression varies across languages. Large audio-language models (LALMs) achieve strong performance on multilingual speech tasks, yet it remains unclear whether they encode emotion through language-specific correlations or language-agnostic representations. We present the first neuron-level interpretability study of this question. We define Multilingual Emotion Neurons (MLENs) as functional units exhibiting stable emotional selectivity and aligne...
  </details>

- **2026-08-09** — Qingying Niu, Ruiyang Ren, Wayne Xin Zhao et al. — [BOUND: Brief-Guided Corrective Preference Distillation at Search-Control Boundaries](http://arxiv.org/abs/2608.08768v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based deep search agents solve tasks through iterative retrieval and reasoning, but locally relevant evidence can cause persistent wrong-anchor drift, constraint drift, or local-topic drift. Existing methods supervise trajectories, outcomes, or steps, but rarely distinguish task-aligned continuations from locally plausible ones that reinforce drift. We propose BOUND, a brief-guided corrective preference distillation framework for persistent search drift. For each stude...
  </details>

- **2026-08-09** — Jędrzej Maczan — [Measuring and Reducing WebGPU Dispatch Overhead for LLM Inference](http://arxiv.org/abs/2608.08730v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are deployed to multiple types of environments, from internet browsers to edge devices, and WebGPU serves as a modern cross-platform standard. The engines for browser-based LLM inference have proliferated, yet the overhead of WebGPU per-operation dispatch remains poorly characterized. In this work, we introduce a sequential-dispatch measurement method and show that naive single-operation measurements overestimate per-dispatch cost by conflating dispatch with synchronization...
  </details>

- **2026-08-09** — Junjie Liu, Wanshui Gan, Zitong Dai et al. — [OccAnyScene: Towards Unified Indoor-Outdoor 3D Occupancy Predictio](http://arxiv.org/abs/2608.08696v1)
  <details><summary>📄 Abstract</summary>
  3D occupancy prediction is fundamental to scene understanding, yet existing 3D semantic occupancy methods are typically specialized to fixed scene types and occupancy protocols. We introduce Cross-Scene 3D Semantic Occupancy Prediction, a new task setting which requires a single model to handle heterogeneous indoor and outdoor scenes with varying cameras, spatial ranges, voxel specifications, and semantic taxonomies. This setting poses a fundamental challenge: achieving metric-consistent yet sce...
  </details>

- **2026-08-09** — Aadil Gani Ganie, Saad Ezzini, Naveed Farooz Marazi — [RAG-Based Auto-Configuration for Industrial Fieldbus Devices](http://arxiv.org/abs/2608.08618v1)
  <details><summary>📄 Abstract</summary>
  Industrial device commissioning requires engineers to manually extract hundreds of protocol-specific parameters from heterogeneous PDF manuals and transcribe them into supervisory control systems, a time-intensive, error-prone workflow. This paper presents SysName, a production-oriented pipeline that automates device configuration end-to-end for Modbus RTU, OPC-UA, Profibus DP, and CANopen. It builds a hybrid dense-sparse retrieval index augmented by an ontology graph derived from ECLASS, AAS, a...
  </details>

- **2026-08-09** — Wenxu Jia, Dongjie Fu, Xize Cheng et al. — [VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference](http://arxiv.org/abs/2608.08569v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in Speech Large Language Models have demonstrated remarkable capabilities in understanding complex audio tasks. Despite this progress, their long-context inference remains severely bottlenecked by prohibitive KV cache memory demands. Existing text-centric compression methods struggle here, often disrupting speech continuity or discarding crucial semantic cues. To address this, we propose VoxZip, a train-free, two-stage semantic-anchored KV cache compression framework. The fir...
  </details>

- **2026-08-09** — Lucian Zhu — [Fluid Structure, Rigid Record: A Layered Organizational Design Framework for Agent-Native Organizations](http://arxiv.org/abs/2608.08516v1)
  <details><summary>📄 Abstract</summary>
  An agentic organization should not be a set of model instances with corporate titles, despite most MAS still operationalizing organization as a conversational topology, a role prompt, or a fixed workflow. This paper develops an agent-native organizational structure framework that separates the persistent and dynamic layers of operations. The persistent layer consists of a four-store record architecture and a pool of resident specialization agents. A coordination layer defines Permission as the b...
  </details>

- **2026-08-09** — Juan S. Santillana — [VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use](http://arxiv.org/abs/2608.08477v1)
  <details><summary>📄 Abstract</summary>
  We present VectraYX-Vision-1B, a sub-2B vision-language model (VLM) for Spanish/LATAM cybersecurity imagery, coupling a frozen SigLIP-so400m encoder to a 1.04B Spanish/LATAM security decoder via an MLP. To our knowledge, it is the first sub-2B VLM specialized for cyber UI (IDA, Ghidra, Wireshark, Nmap, Metasploit, Volatility) that answers in Spanish, emits structured reasoning via native <|think|> tokens, invokes tools via Model Context Protocol (<|tool_call|>), and exports to llama.cpp's LLaVA ...
  </details>

- **2026-08-09** — Tailin Zhou — [Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses](http://arxiv.org/abs/2608.08466v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM agents are often improved by modifying prompts, tools, or workflows manually, while the executable scaffold surrounding the model---the \emph{harness}---is typically treated as a fixed artifact after deployment. This work studies an alternative where the harness is \emph{task-specific and continuously evolvable}: each task family maintains its own harness, which is hot-swapped across iterations through a fixed task-injection seam and rewritten using environment feedback. We introduce ...
  </details>

- **2026-08-09** — Jiaojian Shi, Yijing Huang, Christian Heide et al. — [Nonresonant optomechanical control of structural phases](http://arxiv.org/abs/2608.08899v1)
  <details><summary>📄 Abstract</summary>
  Optical tweezers demonstrate how light can exert forces to trap, repel, and manipulate microscopic particles without absorption. Recent theory has suggested that such forces can extend beyond particle manipulation to drive structural phase transitions in solids. Here we apply this optomechanical principle to tin selenide (SnSe), a material where proximity to several different structural phases gives rise to its high thermoelectric figure of merit and makes it a candidate for a switchable topolog...
  </details>

- **2026-08-09** — Junjie He, Junfeng Li, Zhide Zhong et al. — [SG-WAM: Text-Grounded and Spatial-aware Semantic Guidance for World-Action Models](http://arxiv.org/abs/2608.08839v1)
  <details><summary>📄 Abstract</summary>
  World-Action Models (WAMs) have emerged as a promising paradigm for robotic manipulation. However, most existing WAMs generate future videos and actions by relying mainly on visual cues rather than language instructions, since off-the-shelf text encoders embed instructions independently of visual observations. As a result, the videos predicted by these WAMs are often semantically misaligned with their corresponding language instructions, which degrades the accuracy of the predicted actions. To o...
  </details>

- **2026-08-09** — Yiming Chen, Kaiwen Zhang, Guanjun Liu et al. — [Generics-Aware Fuzz Target Generation for Rust Libraries via Structured API Analysis](http://arxiv.org/abs/2608.08637v1)
  <details><summary>📄 Abstract</summary>
  Fuzzing Rust library APIs requires constructing well-typed, compilable call sequences that satisfy ownership rules, generic parameters, and trait bounds; existing tools ignore these constraints or use shallow heuristics, yielding low coverage. We present GRAFT, which extracts structured API information from Rust documentation, builds an API dependency graph via recursive generics-aware type matching, and uses topology-guided traversal plus LLM synthesis with compiler-error feedback to produce co...
  </details>

- **2026-08-09** — Sarah Rastegar, Mina Ghadimi Atigh, Pascal Mettes et al. — [Fourier Self-Supervision for Fine-Grained Generalized Category Discovery](http://arxiv.org/abs/2608.08963v1)
  <details><summary>📄 Abstract</summary>
  Generalized Category Discovery aims to recognize known categories while identifying novel ones within unlabeled data. Existing methods, typically based on self-supervision and contrastive learning, often struggle to capture fine-grained distinctions, relying on superficial visual cues rather than the intrinsic attributes humans use for categorization. We introduce Fourier Self-Supervision, that leverages the Fourier transform of images to enhance the discrimination of subtle differences and supp...
  </details>

- **2026-08-09** — Cheng Fan, Junyi Zhou, Tingzhang Luo et al. — [Reading is not Reasoning: Bridging the Agentic Policy Gap in Vision-Text Compression](http://arxiv.org/abs/2608.08960v1)
  <details><summary>📄 Abstract</summary>
  Multi-step language-model agents repeatedly process growing interaction histories, leading to substantial context costs. Vision--text compression reduces these costs by rendering history as images, but the resulting modality shift creates a marked capability gap. Through controlled evaluations of history recovery, matched-state decisions, and complete trajectories, we show that this gap cannot be explained by OCR quality alone. Visual-history agents exhibit systematic drift in action selection, ...
  </details>

- **2026-08-09** — Alexander Hackett, Arnaud Denis-Remillard, Axel Cassou — [From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability](http://arxiv.org/abs/2608.08904v1)
  <details><summary>📄 Abstract</summary>
  How much of a vision-language model's (VLM) spatial understanding remains after the action post-training process of building a vision-language-action model (VLA)? We probe depth perception, a primitive of spatiogeometric understanding, from every decoder layer of a weight-matched open-source base VLM/VLA pair: Molmo2-ER and MolmoAct2-LIBERO. First, the VLA decodes depth worse at every layer, a persistent gap we call the floor. Second, the degradation is not uniform: while the base VLM's depth de...
  </details>

- **2026-08-09** — Aya Manel Zitouni, Aicha Zenakhri, Karim Haroun et al. — [Sparse Attention to Emotion: Efficient Facial Emotion Recognition via Token Reduction](http://arxiv.org/abs/2608.08873v1)
  <details><summary>📄 Abstract</summary>
  Facial Emotion Recognition (FER) is an important task that has significant implications across various fields such as biometrics, health, and human-computer interaction. Current Vision Transformer-based approaches display quadratic complexity $\mathcal{O}(N^2)$, with N being the input sequence length, making them cumbersome to deploy at the edge. In this paper, we hypothesize that the FER task does not necessarily require all facial information to correctly interpret emotional states, as specifi...
  </details>

- **2026-08-09** — Subinay Adhikary, Upal Bhattacharya, Vivek Kumar Singh et al. — [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](http://arxiv.org/abs/2608.08830v1)
  <details><summary>📄 Abstract</summary>
  Legal Statute Prediction (LSP) involves automatically identifying relevant legal statutes given factual descriptions in legal documents, typically framed as a multi-label classification task within natural language processing and information retrieval research. While recent advances have begun incorporating Large Language Models (LLMs) for statute prediction, current approaches primarily focus on accuracy metrics without addressing the critical need for legal reasoning, a fundamental requirement...
  </details>

- **2026-08-09** — Jingyun Chen, Fengchun Liu, Linghan Cai et al. — [Agentic Visual Reasoning in Whole-Slide Pathology Images via Active Perception](http://arxiv.org/abs/2608.08648v1)
  <details><summary>📄 Abstract</summary>
  Whole-slide visual reasoning requires identifying sparse diagnostic evidence in gigapixel pathology slides and integrating observations across spatial scales. Existing WSI methods either compress densely sampled patches into global representations or use pretrained vision-language models with heuristic region selection, weakening links between predictions and morphology or lacking pathology-trained observation policies. We present AdaptivePath, an active-perception framework that formulates WSI ...
  </details>

- **2026-08-09** — Ioana Grigore, Sergiu Nisioi — [Mitigating Gender Bias in English to Romanian Machine Translation](http://arxiv.org/abs/2608.08606v1)
  <details><summary>📄 Abstract</summary>
  Machine translation (MT) systems often fail to correctly translate gender, especially when converting from a gender-neutral language like English to a gendered target language such as Romanian. This bias results in translations that default to masculine forms or reinforce gender stereotypes. We propose a hybrid pipeline to mitigate this issue by combining large language model (LLM)-based gender classification with neural machine translation (NMT). Our system uses a fine-tuned LLM to detect the i...
  </details>

- **2026-08-09** — Eyad Alkassar, Mahmoud Fouz, Kurt Mehlhorn — [Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods](http://arxiv.org/abs/2608.08590v1)
  <details><summary>📄 Abstract</summary>
  We prove that every fair-division instance with four agents, additive valuations over the non-negative reals, and at most nine indivisible goods admits a \emph{complete} allocation that is envy-free up to any good in the strong, zero-tolerant sense ($\EFXo$). The case $m=9=n+5$ lies beyond the previously known frontier for complete EFX with four agents ($m\le n+3$). The proof combines a small set of hand-proven reduction lemmas with a machine-verified certificate corpus. The valuation polytope i...
  </details>

- **2026-08-09** — Tzu-Wei Chiu, Song-Duo Ma, Hsin-Yu Lin et al. — [Structure-Preserving Projection for Mitigating Modality Bias in LLM-Based Sequential Recommendation](http://arxiv.org/abs/2608.08583v1)
  <details><summary>📄 Abstract</summary>
  Recent LLM-based recommenders integrate textual and collaborative signals by projecting collaborative embeddings into the embedding space of the LLM. However, this projection can introduce modality bias that distorts the underlying collaborative structure and limits the usefulness of projected embeddings. To address this issue, we propose a novel structure-preserving projection approach that maintains the relational geometry of collaborative embeddings through dedicated structure-preserving loss...
  </details>

- **2026-08-09** — Sina Mohammadi, Wencong Su — [SymbolicPhasor: Power System Phasor Estimation via Deep Symbolic Regression](http://arxiv.org/abs/2608.08552v1)
  <details><summary>📄 Abstract</summary>
  Accurate phasor estimation during power system faults is challenging because fault currents contain decaying DC offsets, harmonics, noise, and possible frequency deviations. These distortions can significantly degrade conventional discrete Fourier transform-based estimators, especially during the first cycle after fault inception. This paper presents SymbolicPhasor, a dynamic deep symbolic regression framework for estimating the fundamental component of distorted fault current signals. The metho...
  </details>

- **2026-08-09** — Chester Tan, Moritz Lampert, Courtney Maynard et al. — [Can Graph Learning Learn Circuits?](http://arxiv.org/abs/2608.08536v1)
  <details><summary>📄 Abstract</summary>
  Circuit localization is a mechanistic interpretability task whose goal is to identify a sparse subgraph of a transformer's computation graph sufficient to reproduce a particular behavior. Most established methods localize circuits independently for each model--task pair. We instead frame circuit localization as a graph machine learning problem in which the edges of a computation graph represent computational pathways, and graph neural networks (GNNs) model interactions among these pathways. We i...
  </details>

- **2026-08-09** — Xiaoyan Zhao, Yujie Cai, Yang Zhang et al. — [Forgotten History or Test-of-Time? Retrospect and Prospect on RAG from an IR Perspective](http://arxiv.org/abs/2608.08445v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is widely regarded as a novel paradigm born from the limitations of large language models (LLMs)--a mechanism to ground their outputs in external knowledge. This view, however, is incomplete when considered within a broader historical context. In this paper, we argue that the core ideas underlying RAG are not new: foundational concepts such as integrating retrieval and language generation, knowledge augmentation, answer verification, and iterative query (or p...
  </details>

- **2026-08-08** — Abisoye Abidakun, Mingjun Zhong, Georgios Leontidis — [Causal State-Space Model for Causal Inference: Estimating Longitudinal Individual Treatment Effects](http://arxiv.org/abs/2608.08288v1)
  <details><summary>📄 Abstract</summary>
  Estimating counterfactual outcomes over time from longitudinal observational data is central to clinical decision support. Existing methods rely on domain confusion -- adversarial training that renders representations invariant to treatment assignment -- yet this invariance creates a mutual information conflict: it suppresses treatment-correlated covariate signals necessary for accurate outcome prediction. We formalise this tension via a Jensen-Shannon divergence bound on counterfactual predicti...
  </details>

- **2026-08-08** — Yingpeng Ma, Jianhao Yan, Bei Shi et al. — [Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives](http://arxiv.org/abs/2608.08160v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Large Language Models (LLMs) is revolutionizing AI for Games by enabling open-ended and fluid interactive storytelling. However, existing research has largely overlooked the critical challenge of maintaining long-horizon logical consistency and narrative integrity against unconstrained user interventions. To address this, we formulate this challenge as Narrative Commitment Preservation (NCP), and take interactive narrative as our testbed. We introduce NCP-Bench, a benchm...
  </details>

- **2026-08-08** — Xin Luo, Yicheng Tao, Haoxuan Zeng et al. — [VOICE: A Vision-Omics Foundation Model Integrating Direct and Retrieval-Based Prediction of In-situ Single-Cell Gene Expression](http://arxiv.org/abs/2608.08366v1)
  <details><summary>📄 Abstract</summary>
  Spatial transcriptomics can resolve gene expression at single-cell resolution, but it is costly, limited to targeted panels of a few hundred to a few thousand genes, and applicable to only a small number of samples. H&E imaging, by contrast, is cheap and collected routinely at scale. This makes predicting single-cell expression directly from morphology a practical way to bring molecular analysis to large tissue archives. We therefore present VOICE, a multimodal foundation model that predicts sin...
  </details>

- **2026-08-08** — Jobst Heitzig, Ram Potham — [A Fair Objective for Human-Empowerment-Preserving AI: Desiderata, Design, and Likely Behavioral Consequences](http://arxiv.org/abs/2608.08240v1)
  <details><summary>📄 Abstract</summary>
  This paper explores the idea of promoting well-being and safety in human-AI interactions by forcing AI agents explicitly to empower humans and to manage the power balance between humans and AI agents in a desirable way. Using a principled, partially axiomatic approach based on desirable properties, we design a parametrizable and decomposable objective function for AI systems that represents an inequality- and risk-averse long-term aggregate of human power. It can take into account models of huma...
  </details>

- **2026-08-08** — Ashritha Gonuguntla — [The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores the Wrong World](http://arxiv.org/abs/2608.08239v1)
  <details><summary>📄 Abstract</summary>
  LLM routers promise efficiency by matching each request to the cheapest adequate model, and are increasingly applied per step inside multi-step agents. Yet agentic routers are evaluated like single-turn routers: by replaying logged trajectories and substituting another model's recorded outputs, assuming the rest of the trajectory is unaffected. We test this assumption with branching rollouts: we fork live SWE-bench agent trajectories at controlled points, rebuild the environment, continue each f...
  </details>

- **2026-08-08** — Chenxi Zhou, Pengfei Cao, Jinyu Ye et al. — [Quantization Degradation in Large Language Models: A Signal-Noise Perspective](http://arxiv.org/abs/2608.08188v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization reduces the deployment cost of large language models, yet how severely a quantized model degrades is not determined by bit-width alone. We systematically study weight-only post-training quantization across bit-widths, quantization methods, model scales and downstream tasks on multiple model families. We observe that such degradation varies substantially across these factors: 4-bit quantization usually preserves performance, 2-bit often causes broad degradation, and at ...
  </details>

- **2026-08-08** — Fouad Bahrpeyma — [A Unified Framework for Dynamic Reward Shaping in Reinforcement Learning](http://arxiv.org/abs/2608.08158v1)
  <details><summary>📄 Abstract</summary>
  Sparse, delayed, and weakly informative rewards remain central obstacles to efficient reinforcement learning. Reward shaping addresses these limitations by supplementing the task reward with an auxiliary signal that can accelerate learning while, in the classical setting, the original objective remains the evaluation criterion. Established theory guarantees safety for fixed shaping signals: potential-based reward shaping preserves optimal policies when the auxiliary term is the discounted differ...
  </details>

- **2026-08-08** — Abhishek Panwar, Maheep Singh, Saksham Bansal — [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](http://arxiv.org/abs/2608.08113v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-Thought (CoT) prompting has become the dominant paradigm for eliciting reasoning in Large Language Models (LLMs), yet it creates substantial computational overhead by forcing models to externalize intermediate reasoning steps as discrete tokens. Recent latent reasoning approaches attempt to internalize this process within continuous hidden states. One of the latest advancements in the field of latent reasoning, Tiny Recursive Models (TRMs) excel at symbolic reasoning but struggle to pre...
  </details>

- **2026-08-08** — Xuning He, Zinan Sheng, Yongding Tao et al. — [Archer: Adaptive Reuse of Cached Hidden States for Efficient Rollback in Diffusion Language Models](http://arxiv.org/abs/2608.08086v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) iteratively refine a sequence, allowing earlier predictions to be revised as context evolves. This rollback capability distinguishes them from irreversible autoregressive generation, but makes inference costly. Every denoising update alters the global context, forcing both prompt and response states to be recomputed even though only response tokens are revisable. Key-value (KV) caching could reduce this cost, yet conventional caching assumes immutable historical ...
  </details>

- **2026-08-08** — Yi Shu, Tianyu Peng, Yingzhuo Deng et al. — [DialectS2S: End-to-End Speech Dialogue Modeling for Low-Resource Chinese Dialects](http://arxiv.org/abs/2608.08067v1)
  <details><summary>📄 Abstract</summary>
  Current end-to-end speech dialogue models are primarily optimized for mainstream languages and remain limited in low-resource dialect scenarios due to the scarcity of dialect speech data. Moreover, during dialect adaptation, the semantic representation space of speech dialogue models continuously evolves, while conventional speech supervision remains unchanged, leading to semantic inconsistency between hidden representations and speech targets and degrading speech stability and naturalness. To a...
  </details>

- **2026-08-08** — Jie Huang, Xiaohe Li, Jiahao Li et al. — [PhysX-CoT: Structured Physical Reasoning from a Single Image to Simulation-Ready 3D Assets](http://arxiv.org/abs/2608.08053v1)
  <details><summary>📄 Abstract</summary>
  Simulation-ready 3D assets are central to robotics and embodied AI. Generating them from a single image is usually framed as a vision-language model that emits a serialized asset for a decoder to turn into geometry and physical fields, leaving the image-to-3D reasoning implicit. We argue the limiting factor is this output-centric view: part placement and local shape are entangled in one global-coordinate token stream, and the intermediate physical states are never exposed for supervision, condit...
  </details>

- **2026-08-08** — Liangliang Zhao, Junying Wang, Danni Yang et al. — [Distilling Physical Priors into Streaming World Models](http://arxiv.org/abs/2608.07981v1)
  <details><summary>📄 Abstract</summary>
  Streaming world models predict future visual states online while maintaining physically coherent dynamics over long horizons. However, their rollouts often violate basic physical constraints. A common approach distills pretrained bidirectional DiTs into few-step causal generators. However, this paradigm suffers from two fundamental limitations: generic bidirectional teachers acquire limited physical priors from visually oriented pretraining, and the limited priors suffer further loss during bidi...
  </details>

- **2026-08-08** — Jianbin Luo, Weibin Lin, Yiran Lin et al. — [Verication-driven closed-loop multi-agent large language modelframework for code-compliant structural design](http://arxiv.org/abs/2608.07978v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model(LLM)systems are applied to structural design,yet most use one-shot generation and cannot verify their output,leaving themill-suited to safety-critical tasks.Rather than trusting LLM self-correction,thisframework injects feedback from an external physics-based verier into a closedrepair loop.The framework couples a three-layernite-element verication systemwith a dual-node loop.Node 1 turns code violations into hard repair constraints,Node 2 turns a four-dimensiona...
  </details>

- **2026-08-08** — Huiling Wu, Yuxin Deng — [ReOC: Compilation of Recursive Quantum Oracles with Recursion-Aware Uncomputation](http://arxiv.org/abs/2608.07973v1)
  <details><summary>📄 Abstract</summary>
  Quantum oracles are essential to many quantum algorithms, and their specifications may involve recursive control flow that depends on runtime quantum data. However, existing reversible compilation frameworks provide limited support for such quantum-controlled recursive structures.   We present ReOC, a compilation framework that transforms high-level recursive oracle specifications with quantum control flow into reversible quantum programs. The framework comprises RQIMP, a high-level imperative s...
  </details>

- **2026-08-08** — Jinghao Wang, Yihang Zhou, Xiaoyang Sun et al. — [ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters](http://arxiv.org/abs/2608.07971v1)
  <details><summary>📄 Abstract</summary>
  Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations. This leaves substantial GPU capacity underutilized: training jobs reserve entire devices despite periodic idle phases, while offline inference tasks over-provision GPUs despite bursty demand patterns. We present ElastiCo, an elastic co-location framework that enables training a...
  </details>

- **2026-08-08** — Zijian Lu, Yiping Zuo, Hao Xu et al. — [WirelessOpsAgent: A Benchmark and Agent Design for Action Assurance in Wireless Networks](http://arxiv.org/abs/2608.08277v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are emerging as planners for autonomous wireless network operations. Yet a task answer that is correct at proposal time can still be unsafe at execution time if supporting telemetry is stale or inconsistent. Existing benchmarks mainly evaluate task solving from fixed observations and leave support checking at execution time untested. We introduce WirelessOptBench, a benchmark for action assurance in wireless operations. It turns wireless tasks into execution sta...
  </details>

- **2026-08-08** — Hanxiao Chen — [Multi-modal Interactive Control of Robotic Arm based on Offline Large Language Models](http://arxiv.org/abs/2608.08183v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have significantly revolutionized the modern society with numerous advanced interactions between humans and AI agents, whereas the usage of most large language models including ChatGPT are not friendly open-sourced and must require the users paying a lot for such AI services continuously. Therefore, deploying open-sourced large language models on local servers can be considered as an efficient approach to design and implement creative embodied AI algorithms with lowe...
  </details>

- **2026-08-08** — Rui Xu, Hanmo Zhang, Songhua Liu — [Staying True to the Origin: Continuous Image Stylization with Smooth Transitions](http://arxiv.org/abs/2608.08125v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative models have achieved remarkable performance in text- and image-conditioned editing. However, preserving the content of a given image while referencing style patterns from another remains challenging, often leading to uncontrollable stylization results. In this paper, we approach image stylization from the perspective of continuous control, aiming to enable modern Diffusion Transformer (DiT)-based multi-reference editing models to (1) faithfully preserve the semantic...
  </details>

- **2026-08-08** — Hu Cang — [A Shared Observation Shields Collective Fluctuations while Preserving Local Independence](http://arxiv.org/abs/2608.08358v1)
  <details><summary>📄 Abstract</summary>
  As a liquid approaches its glass transition, its dynamics turns heterogeneous: mobile and immobile regions coexist, and the four-point susceptibility $χ_4$ that quantifies this heterogeneity grows sharply. Interpreting that growth is subtle, because the collective signals experiments record, such as a tagged particle's trajectory, an overlap function, or a mean field, are generated by the same particles they describe. Here we compute exactly what conditioning on such a shared record does to the ...
  </details>

- **2026-08-08** — Raimundas Sereika, Matthew P. Clay, Kallol Chakrabarty et al. — [Pressure-Induced Stacking Disorder and Suppression of Long-Range Sm-type Order in Medium-Entropy Rare-Earth Alloys](http://arxiv.org/abs/2608.08351v1)
  <details><summary>📄 Abstract</summary>
  Rare-earth medium-entropy alloys provide a platform for investigating how chemical disorder modifies the well-established pressure-induced structural evolution of close-packed $4f$ lanthanides. Here, we study TbHoEr and TbHoDy using synchrotron X-ray diffraction in diamond anvil cells. Both alloys transform from the ambient hexagonal close-packed (hcp) structure to a double hexagonal close-packed (dhcp) phase, while no well-resolved bulk Sm-type intermediate phase is observed. For TbHoEr, compre...
  </details>

- **2026-08-08** — Hwanhee Kim, Jaehyun Jang, Seungmin Cha et al. — [Action- and Language-Conditioned Video Assessment for Embodied Control](http://arxiv.org/abs/2608.08273v1)
  <details><summary>📄 Abstract</summary>
  Vision-based embodied agents executing multi-step natural language instructions require feedback mechanisms that assess task progress over complete trajectories. Conventional approaches based on final-frame matching or continuous embedding similarity may overlook intermediate transitions that are necessary for determining whether an instruction has been completed. We propose ALVA (Action- and Language-Conditioned Video Assessment), a trajectory evaluator that conditions its assessment on visual ...
  </details>

- **2026-08-08** — Binwen Tan, Jingchao Wang, Dengzhe Hou et al. — [Control-Diverse Reinforcement Fine-Tuning: Decoupling the Shared Control Bottleneck of RL Post-Training](http://arxiv.org/abs/2608.08224v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning post-training unlocks complex reasoning in LLMs. Yet benchmark scores reveal only whether a model improved, not what changed inside it, nor how it splits finite capability across tasks. A representative interpretability line attributes the success of RL fine-tuning to stronger and more diverse circuit activation. We challenge this activation-centered account by separating activation from control: an activated circuit need not control the post-training reward gain. Adapting...
  </details>

- **2026-08-08** — Seungjin Choi — [Anytime-Valid Evidence for Prespecified Predictive Corrections](http://arxiv.org/abs/2608.08174v1)
  <details><summary>📄 Abstract</summary>
  A predictive correction is a prespecified modification of an existing predictive distribution intended to reflect an anticipated change in future outcomes given their inputs, motivated, for example, by instrument recalibration, assay drift, or a known intervention. We study how to accumulate anytime-valid evidence that such a correction predicts incoming target outcomes better than the uncorrected source predictive distribution. A fixed nonnegative tilt transforms the source predictive into a co...
  </details>

- **2026-08-08** — Ameen Ali, Tamim Zoabi, Lidor Brami et al. — [Wiener Representation Filtering for VLM Hallucination Suppression](http://arxiv.org/abs/2608.08167v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) excel at open-ended captioning and visual QA but often describe objects, attributes, or relations absent from the image, a phenomenon known as object hallucination. We propose a {training-free, post-hoc representation editing technique} that operates in the representation space of the language backbone. The method performs a lightweight, one-time offline calibration on a modest paired dataset to estimate the required covariance structures, using only forward passes ...
  </details>

- **2026-08-08** — Paul Tarau — [On the (Intuitionistic) Logic of Next-Token Prediction](http://arxiv.org/abs/2608.08145v1)
  <details><summary>📄 Abstract</summary>
  We model in intuitionistic implicational logic the key enabler of today's GenerativeAI: the next-token prediction in autoregressive causal neural networks.   In our framework, next-token prediction corresponds to modus ponens, and sequence processing becomes constructive proof extension under the Curry-Howard correspondence. Our Prolog-based specialized theorem provers validate fundamental properties of the neural models, among which relations between commutative vs. non-commutative sequencing  ...
  </details>

- **2026-08-08** — Sankalp Nagaonkar, Rohit Garg, Ankit Raj et al. — [Search over the Visual World: Persistent Visual Memory, Layered Indexes, and Source-Grounded Evidence](http://arxiv.org/abs/2608.08075v1)
  <details><summary>📄 Abstract</summary>
  Most video-retrieval systems assume a bounded corpus and return ranked files or timestamps. Agents operating over cameras, screens, streams, and archives face a different systems problem: observations arrive continuously; models interpret them at different temporal granularities; context must be selected without replaying the complete visual record; and results must stay connected to inspectable source evidence. We argue that search over such a corpus is an infrastructure problem that cannot be ...
  </details>

- **2026-08-08** — Alireza Joonbakhsh, Arda Canser Adalı, Slinger Jansen et al. — [HugSelect: An Explainable Multi-Criteria Decision-Support Framework for foundation-model selection](http://arxiv.org/abs/2608.08069v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly reused as software components, making model selection a critical software-engineering decision. Current model hubs primarily support discovery through popularity metrics, often neglecting functional capabilities, operational constraints, and community-perceived quality. We argue that foundation-model selection should be treated as an explicit, auditable software-component selection task rather than as keyword search, popularity ranking, or opaque conversational...
  </details>

- **2026-08-08** — D. A. Batyaev, A. V. Korybut — [Gauge transformations in Z-space in (anti)holomorphic sector of HS theory](http://arxiv.org/abs/2608.08062v1)
  <details><summary>📄 Abstract</summary>
  We consider a consistent deformation of the (anti)holomorphic generating system of [arXiv:2209.01966], aiming to provide a map to the (anti)holomorphic truncation of the Vasiliev theory. In our new formulation, the previously rigidly defined master-field $Λ$ can be shifted by $\mathrm{d}_z$-exact projective one-forms. The class of projective one-forms is described comprehensively, and corresponding projective identities are proven. $\mathrm{d}_z$-exact forms of the order $n$ in $C$ induce field ...
  </details>

- **2026-08-08** — Tianle Yang, Cuiling Zhang, Chengzhe Sun et al. — [The Voiceprint Fallacy: Why Voices Are Not Unique Biometric Imprints](http://arxiv.org/abs/2608.07980v1)
  <details><summary>📄 Abstract</summary>
  In recent years, the term voiceprint has regained attention, particularly in technological applications and policy-making contexts, often carrying the assumption that a person's voice constitutes a stable and unique biometric trace analogous to a fingerprint. Yet this conception has been repeatedly criticized and rejected by forensic voice experts throughout the decades since its introduction. Although voices undoubtedly contain speaker-related information, this simplified conception obscures th...
  </details>

- **2026-08-07** — Shaull Almagor, Guy Avni, Julian Ewaied — [Analyzing the Interaction of Optimal Strategies in Mean-Payoff Bidding Games](http://arxiv.org/abs/2608.07383v1)
  <details><summary>📄 Abstract</summary>
  A common assumption when designing an agent in a multi-agent system is that the other agents behave adversarially. This allows a designer to obtain the strongest guarantees when they have no control over nor knowledge about the other agents' behavior. However, when all agents are designed under this adversarial assumption, their actual interaction is not adversarial (e.g., when all players play defensively, no player actually attacks). In such settings, we would like to know what behavior arises...
  </details>

- **2026-08-07** — Kaela Kokkas, Hairong Wang, Richard Klein et al. — [Artificial Intelligence Can Match Domain Experts in Evidence Extraction and Critical Appraisal of Microbial Oncogenesis Research Publications](http://arxiv.org/abs/2608.07250v1)
  <details><summary>📄 Abstract</summary>
  Confirmed oncogenic microbes contribute significantly to cancer burden. Identifying novel microbial oncogenicity could yield strategies that will reduce disease burdens. However, relevant evidence is dispersed and infeasible for humans to comprehensively synthesize. LLMs may enable scalable, expert-level systematic evidence synthesis to identify microbe-cancer pairs; however, such capabilities have not yet been demonstrated. Domain experts were recruited to create a dataset to benchmark LLM perf...
  </details>

- **2026-08-07** — Paul-Peter Arslan — [Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints](http://arxiv.org/abs/2608.06949v1)
  <details><summary>📄 Abstract</summary>
  Prior benchmarking work has shown that a single large language model (LLM), forced to make life-or-death resource-allocation decisions, exhibits measurable demographic bias. Real deployments, however, rarely use a single agent: they use pipelines, with review steps meant to catch exactly this kind of failure. We study what happens to bias when the same decision is distributed across a role-differentiated multi-agent pipeline (assessment, allocation, independent audit) instead of made and checked...
  </details>

- **2026-08-07** — Hanke Xie, Haopeng Lin, Jiale Qian et al. — [SemBridge: Semantic Token Anchoring for Continuous-Latent Autoregressive Speech Generation](http://arxiv.org/abs/2608.07462v1)
  <details><summary>📄 Abstract</summary>
  Continuous-latent autoregressive speech generation has emerged as a promising alternative to discrete-token modeling by avoiding quantization loss and preserving richer acoustic information. However, continuous acoustic targets do not ex- pose linguistic structure as explicit token-level prediction tar- gets. Consequently, the autoregressive language model (LM) must acquire linguistic structure indirectly through acous- tic prediction, which can compromise the content fidelity of generated speec...
  </details>

- **2026-08-07** — Haoyu Zheng, Yun Zhu, Qing Wang et al. — [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](http://arxiv.org/abs/2608.07371v1)
  <details><summary>📄 Abstract</summary>
  Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditio...
  </details>

- **2026-08-07** — Assaf Caftory, Almog Zemach, Moshe Butman et al. — [Why Study Emergent Behavior When You Can Regulate It? Aligning Multi-Agent Systems with Reward Prediction](http://arxiv.org/abs/2608.07280v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent simulations are widely used to study complex social and ecological systems, where rich and often unexpected emergent behaviors arise from local interactions. A large body of prior work has focused on analyzing such emergent dynamics across domains. In this paper, we move beyond analyzing emergent behavior and introduce a learning-based mechanism for actively shaping it via social reward modeling. We introduce Multi-Agent Reward Prediction (MARP), a simple framework that extends prefe...
  </details>

- **2026-08-07** — Vasanth Iyer — [Dual-Node NVIDIA DGX Spark over Tailscale: A Remote-Access Testbed for Distributed LLM Training and Cyber-Threat-Intelligence Fine-Tuning](http://arxiv.org/abs/2608.07226v1)
  <details><summary>📄 Abstract</summary>
  Compact AI systems make local language-model experimentation increasingly accessible, yet practical evidence for multi-node training on desktop-class accelerators remains limited. This report presents a proof-of-concept deployment of distributed NanoChat pretraining across two NVIDIA DGX Spark systems, each with a GB10 Grace Blackwell system-on-chip and 128 GB of unified memory, administered remotely over a Tailscale mesh VPN and connected for training by a dedicated 200 Gb/s QSFP56 direct fiber...
  </details>

- **2026-08-07** — Dazhuo Qiu, Yingli Zhou, Amedeo Pachera et al. — [Toward a Causal Data Management Ecosystem for Decision Making and Agentic AI](http://arxiv.org/abs/2608.07214v1)
  <details><summary>📄 Abstract</summary>
  Modern AI is no longer a single model but an ecosystem: classical ML predictors, deep and multimodal models, large language models, and agents, each trained and tuned over different data sources and each producing outputs at scale that become inputs to the others. Operating such an ecosystem is fundamentally a data integration problem - the knowledge it depends on is fragmented across dozens of heterogeneous, independently governed sources that must be reconciled and continually maintained. Yet ...
  </details>

- **2026-08-07** — Chuan Liu, Hongyi Bian, Wei Gao et al. — [DRL-Based Secure Transmission for Rotatable Antenna-Enabled Low-Altitude ISAC Systems](http://arxiv.org/abs/2608.07170v1)
  <details><summary>📄 Abstract</summary>
  The development of the low-altitude economy has driven innovation in intelligent antenna systems within ISAC systems. In this paper, we investigate a Rotatable Antenna (RA)-enabled low-altitude integrated sensing and communication (ISAC) system. In practical terms, the RA array can flexibly adjust the three-dimensional (3D) beam direction of each antenna to enhance array directional gain, thereby improving the communication security of legitimate mobile users against potential eavesdropping risk...
  </details>

- **2026-08-07** — Mark Leon Ringer, Michel Tokic — [Interpretable reinforcement learning with decision-tree pruning](http://arxiv.org/abs/2608.07151v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning policies are difficult to inspect, but interpreting them is a prerequisite for trustworthiness. Converting a trained policy into explicit decision-tree rules improves transparency and the resulting artifacts often remain too complex for human understanding. We present a pruning process that simplifies such rule-based policies while preserving task performance and making edits to the policy auditable. The process defines a small set of structural and usage-aware operators a...
  </details>

- **2026-08-07** — Fedor Pakhomov — [Lévy-Montague reflection is $Π^1_1$-conservative over $\mathsf{WKL}_0$](http://arxiv.org/abs/2608.07050v1)
  <details><summary>📄 Abstract</summary>
  We study a Lévy-Montague reflection scheme $\mathsf{Rfn}$ in second-order arithmetic: for each formula $\varphi$, the scheme asserts that every set belongs to a countable coded $ω$-model such that $\varphi$ is absolute, at all parameters from the model, between the model and the universe. Our central result is a model extension construction: every countable model of $\mathsf{RCA}_0$ can be extended, without changing its first-order part, to a model of $\mathsf{WKL}_0$ together with the full sche...
  </details>

- **2026-08-07** — Shrutendra Harsola, Vignesh Subrahmaniam — [Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses](http://arxiv.org/abs/2608.07037v1)
  <details><summary>📄 Abstract</summary>
  Small businesses often have only 12-24 months of accounting history, yet planning and risk workflows require coordinated forecasts across financial statements. We study joint 12-month forecasting of 13 income-statement, balance-sheet, cash-flow, and working-capital key performance indicators (KPIs) from 71 monthly ledger series. We introduce the Accounting Graph Transformer (AGT), which represents each ledger series as a masked token, exchanges information through typed attention on a fixed acco...
  </details>

- **2026-08-07** — Mudar Adas, Polina Tsvilodub, Michael Franke et al. — [Confirming Our Biases? Evaluating the Capabilities, Risks, and Societal Impact of Large Language Models](http://arxiv.org/abs/2608.06977v1)
  <details><summary>📄 Abstract</summary>
  It is well established that large language models (LLMs) are sensitive to prompt framing, reflecting patterns in their training data or prior prompts. In this study, we investigate the extent to which LLMs reinforce users biases expressed in the prompts and examine the boundary between implicit framing effects and explicit prompt manipulation. Specifically, we evaluate how susceptible LLMs are to direct and suggestive prompts that encourage models to support or challenge particular positions.   ...
  </details>

- **2026-08-07** — Hongyu Luo, He Wang, Huihao Jing et al. — [Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs](http://arxiv.org/abs/2608.06967v1)
  <details><summary>📄 Abstract</summary>
  Current evaluations do not isolate whether text-only language models can originate visual concepts before image generation. Fluent visual prose can hide visual-plan failures: an answer may appear creative while repeating familiar visual clichés or failing to specify a renderable scene. We define Visual Creative Ideation (VCI) as the ability to produce textual visual plans that are useful, expressive, and population-novel, and introduce Ekphrasis, a 400-task benchmark spanning Abstraction, Combin...
  </details>

- **2026-08-07** — Ali Jalal-Kamali, Nikolos Gurney, David V. Pynadath et al. — [TRIBE: Predicting Team Performance via Communication Behavior Ensembles](http://arxiv.org/abs/2608.06926v1)
  <details><summary>📄 Abstract</summary>
  Designing autonomous agents that effectively assist human teams hinges on understanding team dynamics, often without task specific knowledge. We present TRIBE, a domain independent approach that reveals team behavioral dynamics invisible to traditional performance metrics. We show that communication patterns can categorize teams into performance predictive behavioral tribes, as early as 10% into the task, enabling timely interventions. We test TRIBE on four diverse datasets and demonstrate that ...
  </details>

- **2026-08-07** — Guoshan Liu, Bin Zhu, Pengkun Jiao et al. — [ReGraph: Learning to Generate Recipe Graphs from Food Images](http://arxiv.org/abs/2608.06917v1)
  <details><summary>📄 Abstract</summary>
  Recent Large Multimodal Models (LMMs) have achieved impressive performance in recipe generation from food images.However, cooking is a structured transformation process in which ingredients undergo state changes through ordered actions,while free-form recipe language leaves the corresponding entities, intermediate states, and dependencies largely implicit and entangled.A graph representation makes this procedural knowledge explicit and compositional, providing a structured basis for assessing wh...
  </details>

- **2026-08-07** — Eric Nichols, Alva Markelius, Hatice Gunes — [How Should I Pick a Foundation Model for My Robot? In Favor of a Community Evaluation Framework for Social Robots](http://arxiv.org/abs/2608.06898v1)
  <details><summary>📄 Abstract</summary>
  Researchers who seek to build social robot applications on foundation models are faced with a difficult question: how should we pick a model? Public leaderboards offer little guidance: the demands of real-time, embodied social interaction lie largely outside their focus. And direct evaluation is impractical at scale: each embodied study requires scarce participant, robot, and experimenter time. In this paper, we identify five evaluation dimensions for foundation models in social robots: (i) conv...
  </details>

- **2026-08-07** — Xiaolin Bu, Biaoshuai Tao — [Bayesian Fair Division: Truthfulness in Picking Sequence with Correlated Valuations](http://arxiv.org/abs/2608.07414v1)
  <details><summary>📄 Abstract</summary>
  Sequential allocation mechanisms contain a class of widely studied mechanisms (e.g., round-robin) in the fair division of indivisible goods, where agents take turns picking items in a predefined picking order. It is known that the sequential allocation mechanisms are not truthful: when an agent's most preferred item is not valued by others, the agent may manipulate the mechanism by choosing to defer picking that item and instead competing for another slightly less preferred item that is valued b...
  </details>

- **2026-08-07** — Ziheng Liu, Quantao Yang — [TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models](http://arxiv.org/abs/2608.07314v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models are commonly adapted to downstream manipulation tasks via supervised fine-tuning (SFT) or online reinforcement learning (RL) post-training. SFT is prone to distribution mismatch, and existing RL approaches typically apply a single, uniform update strategy to all model components, ignoring their distinct functional roles. We propose TEMPO, a semantic-action decoupled, two-timescale RL post-training framework for VLA models. TEMPO freezes the pretrained vision-l...
  </details>

- **2026-08-07** — Zichuan Wang, Songlin Yang, Bo Peng et al. — [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](http://arxiv.org/abs/2608.07302v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) often suffer from object hallucination, generating objects that are absent from the image. Prior work largely attributes this to insufficient visual attention. However, we find that both real and hallucinated objects receive equally strong visual attention in the model's mid-to-late layers, suggesting that the key issue may not be how much the model attends, but what it attends to and why. To this end, we decode the visual features of high-attention regions u...
  </details>

- **2026-08-07** — Xiangkai Ma, Yue Ma, Junjie Wang et al. — [Decoupling Intention from Trajectory: A Representational Deduction Framework for World Action Models](http://arxiv.org/abs/2608.06994v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) aim to construct a unified architecture capable of understanding world state evolution and guiding to generative motion planning. However, existing visual branches focus on predicting static visual observation, rather than reflecting potential transition information that captures the evolution of world states under motion interactions. This leads to representational entanglement between high-level physical condition evolution and low-level action trajectory generation ...
  </details>

- **2026-08-07** — Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin — [CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity](http://arxiv.org/abs/2608.07460v1)
  <details><summary>📄 Abstract</summary>
  While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning t...
  </details>

- **2026-08-07** — Zixuan Lan, Luzhe Sun, Matthew R. Walter et al. — [SABRE: Scalable and Automated Benchmarking of VLMs under Stress](http://arxiv.org/abs/2608.07435v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are improving rapidly, but benchmark development lags behind, making weaknesses hard to identify. Building stress tests is costly: samples must satisfy controlled conditions, remain answerable, and challenge current models. We present SABRE, a scalable, automated pipeline that converts a Test Primer (a Markdown Task Design with Data Schema) into structured specifications, generated or edited images, and question-answer pairs. Automated filtering removes candidates s...
  </details>

- **2026-08-07** — Heechang Kim, Ernest K. Ryu, Shuvomoy Das Gupta — [A Domain-Specific Harness for End-to-End Automation of Optimization Research](http://arxiv.org/abs/2608.07407v1)
  <details><summary>📄 Abstract</summary>
  We present AutoOPT, a domain-specific harness for end-to-end automation of optimization research. AutoOPT organizes the discovery of optimal first-order methods into four stages: numerical design through the BnB-PEP methodology; symbolic discovery of the analytic description and a convergence proof through frontier large language models (LLMs); formal verification in the Lean 4 proof assistant; and human interpretation and write-up. We demonstrate the framework on two case studies, each of indep...
  </details>

- **2026-08-07** — Shivi Dixit, Rishabh Gupta, Adam Kelloway et al. — [Uncovering expert objectives in production planning via inverse optimization: An industrial case study](http://arxiv.org/abs/2608.07398v1)
  <details><summary>📄 Abstract</summary>
  Production planning in the manufacturing industry often relies on the use of optimization models, but defining an appropriate objective function can be a challenge. In practice, planners must balance competing goals, manage uncertainty, and account for qualitative business preferences that are difficult to quantify. As a result, many optimization models fail to match expert behavior, limiting trust and adoption. In this work, we propose a data-driven inverse optimization framework to infer the o...
  </details>

- **2026-08-07** — Ioannis Ziogas, Ensieh Khazaei, Bilal Taha et al. — [Omni-modal decomposition autoencoders learn full-stack wearable disentangled representations](http://arxiv.org/abs/2608.07385v1)
  <details><summary>📄 Abstract</summary>
  Learning disentangled representations is a key requirement for developing versatile, general-purpose, and sustainable models in multi-modal wearable computing. However, existing approaches do not operate as full-stack wearable processors, i.e., they do not simultaneously address task-specific classification performance, disentangled and interpretable representation learning, fusion, and generative modeling of highly heterogeneous multi-modal time series. To address this gap, we introduce Omni-mo...
  </details>

- **2026-08-07** — Polina Proutskova — [Beyond Call and Response: Modelling Reciprocal Coordination in Human-AI Vocal Ensembles](http://arxiv.org/abs/2608.07376v1)
  <details><summary>📄 Abstract</summary>
  Musical interaction with AI is often organised as a response loop: a human performs, the system interprets that action, and the system answers, accompanies, or schedules a musical event. Unconducted vocal ensembles pose a different problem. Singers act simultaneously and continuously affect one another; neither timing nor pitch is fixed by a conductor, metronome, accompaniment, score, or tuning source. Collective organisation emerges from many-to-many reciprocal adjustment. This paper frames suc...
  </details>

- **2026-08-07** — Edoardo Sebastiano De Duro, Emma Franchino, Massimo Stella — [Natural Language Processing Psychometrics](http://arxiv.org/abs/2608.07316v1)
  <details><summary>📄 Abstract</summary>
  Natural Language Processing (NLP) models predicting mental health outcomes rarely specify what they measure: contextual knowledge, emotional content, or syntactic structure. NLP Psychometrics treats psychological prediction from text as a psychometric problem, linking scores to interpretable linguistic evidence and testing beyond the training text format. Nine LLMs, conditioned on controlled personas (cognitive digital shadows), completed psychometric questionnaires with textual explanations per...
  </details>

- **2026-08-07** — Idil Gözel — [Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis](http://arxiv.org/abs/2608.07228v1)
  <details><summary>📄 Abstract</summary>
  When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse.   We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At o...
  </details>

- **2026-08-07** — Yujun Wang, Tao Zhang, Jinhe Bi et al. — [MemWM: Memory-Augmented Text-Based World Model](http://arxiv.org/abs/2608.07107v1)
  <details><summary>📄 Abstract</summary>
  World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions. Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules. To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated memory bank of transition rules, state caches, and hard-to-predict facts, to condi...
  </details>

- **2026-08-07** — Zeinab Dehghani, Dhavalkumar Thakker, Koorosh Aslansefat et al. — [Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design](http://arxiv.org/abs/2608.07091v1)
  <details><summary>📄 Abstract</summary>
  Edge Artificial Intelligence (Edge AI) enables the deployment of AI models directly on local edge devices, while such deployments are subject to strict resource constraints, particularly in clinical applications requiring local and timely inference. In such contexts, explainable artificial intelligence (XAI) can serve as a human-AI interface intended to support healthcare professionals' and patients' understanding of model predictions and informed decision-making. To fulfill this role, XAI metho...
  </details>

- **2026-08-07** — Devin Pereira, Willem Zuidema — [Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking](http://arxiv.org/abs/2608.07077v1)
  <details><summary>📄 Abstract</summary>
  The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all rings on a single peg). This paper presents an in-depth study of how both small, in-house Transformers and large, third-party LRMs solve this task. To understand the failures mechanistically, we first tra...
  </details>

- **2026-08-07** — Lendert Gelens, Alejandro Fábregas-Tejeda, Grant Ramsey et al. — [Simulating is not always understanding: When model complexity obscures biology](http://arxiv.org/abs/2608.06998v1)
  <details><summary>📄 Abstract</summary>
  In cell biology, computational models of biological systems range from minimal representations with a handful of parameters to whole-cell simulations tracking thousands of molecular species across a complete cell cycle. While these models span a continuum of detail, increasing complexity changes what they capture and are able to explain, what they can predict, and how they can fall short. A model contributes to understanding only when it makes novel predictions, reveals an unexpected coupling be...
  </details>

- **2026-08-07** — Gregor Molan, Grafika Jati, Francesco Barchi et al. — [Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction](http://arxiv.org/abs/2608.06993v1)
  <details><summary>📄 Abstract</summary>
  Large-scale pretrained time-series models achieve strong results through large-scale pretraining and task-agnostic representation learning, but they rely on abundant, diverse data that industrial and scientific domains often lack. We therefore propose the FSD-RM (Family of Small-Data Representation Models) paradigm as a practical alternative for limited, domain-specific telemetry. Rather than relying on large-scale pretraining, we focus on capacity-controlled representation learning using establ...
  </details>

- **2026-08-07** — Shixin Zhao, Lian Liu, Tianhua Han et al. — [Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM](http://arxiv.org/abs/2608.06989v1)
  <details><summary>📄 Abstract</summary>
  Heterogeneous architectures that combine neural processing unit (NPU) and processing-in-memory (PIM) are increasingly adopted to accelerate LLM inference. Prior work focuses on building a unified memory that allows NPUs and PIM to share data without duplication. However, these designs implicitly assume that each tensor is bound to a fixed execution device, and therefore rely on static, device-biased data mappings.   We observe that this assumption does not hold in modern LLM workloads. Due to ph...
  </details>

- **2026-08-07** — Jonghyun Jee, Aaron Shaw — [Critical Acclaim Orientation in Large Language Models: Evidence from Film Preference Elicitation](http://arxiv.org/abs/2608.06955v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are trained on corpora that contain expressions of human judgment about films, books, music, and more. Yet whether LLMs systematically reproduce evaluative hierarchies remains unclear. Prior research on cultural bias in LLMs suggests competing expectations: models may mirror the popularity signals of internet texts, or may reproduce forms of prestige embedded in critical discourse. We probe this question through a study of film evaluations with eight models from four...
  </details>

- **2026-08-07** — Taolin Han, Yuchen Zhang, Jinghang Wang et al. — [Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery](http://arxiv.org/abs/2608.06931v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly involved in scientific discovery, yet it remains unclear whether they can support complex real laboratory science. Here we introduce Science Edge Evaluation (SEE), a multimodal benchmark of expert-curated questions grounded in peer-reviewed literature and experimental practice in chemistry, biology, and materials science. Evaluation of 19 multimodal large language models (MLLMs) shows that even the best-performing model reaches only 48.7% accuracy. M...
  </details>

- **2026-08-06** — Fanzhe Meng, Guoxin Chen, Jiale Zhao et al. — [CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks](http://arxiv.org/abs/2608.06352v1)
  <details><summary>📄 Abstract</summary>
  Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a...
  </details>

- **2026-08-06** — Germana Bertoli, Ilaria Amelia Caggiano, Francesca Lagioia et al. — [What out-of-the-box LLMs can(t) do in law? A Turing test in Italian exams for lawyers, judges and notaries](http://arxiv.org/abs/2608.06166v1)
  <details><summary>📄 Abstract</summary>
  The article reports on a blind Turing Test experiment, assessing the performance of out-of-the-box leading LLMs on three Italian legal professional exams: the Bar, Judges and Notary exams. Leading LLMs were asked to generate full written exam papers, which were made indistinguishable from human submissions and anonymously evaluated by expert examiners, using the same criteria applied in real examinations. Results reveal marked differences across both models and tasks. While some LLMs match or ex...
  </details>

- **2026-08-06** — Leo Sambrook, Sampo Sovio — [Hardware Keystores for AI Agent Signing Workflows: A Zero-Trust MCP Enforcement Architecture](http://arxiv.org/abs/2608.06130v1)
  <details><summary>📄 Abstract</summary>
  AI agents performing cryptographic operations (signing Git commits, authenticating API calls, issuing certificates) currently store private keys in software-accessible locations: plaintext files, environment variables, or container memory. Any process with sufficient read privileges can extract the raw key material. A recent production incident demonstrated the practical severity: private keys were exfiltrated from a widely deployed framework via email injection in under five minutes. We aim to ...
  </details>

- **2026-08-06** — Junfeng Li, Junjie He, Zhide Zhong et al. — [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](http://arxiv.org/abs/2608.06374v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations. First, they underuse dynamics priors shared across diverse visual and interaction data, limiting cross-embodiment transfer. Second, they require extensive manual preprocessing to convert embodiment-specific actions into a common format. To overcome these limitati...
  </details>

- **2026-08-06** — Praphul Chandra, Sujit Gujar, Ganesh Ghalme — [Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents](http://arxiv.org/abs/2608.06353v1)
  <details><summary>📄 Abstract</summary>
  We give a formal mechanism design model for the continuous participatory governance of a deployed AI agent. The mechanism is built on the principle that governance should control an AI agent through resource allocation so as to make authorization self enforcing via compute budgets. The mechanism seeks to establish the Safe AI paradigm that compute is an effective governance lever. We situate our work as a compliance or commons overlay on a deployer. One governance period is an extensive form gam...
  </details>

- **2026-08-06** — Alexandra Newcomb, Omar Ochoa — [Automatic Translation of Unstructured Requirements into Linear Temporal Logic through Large Language Models](http://arxiv.org/abs/2608.06287v1)
  <details><summary>📄 Abstract</summary>
  Automatically translating unstructured natural language requirements into formal specifications remains a challenge in requirements engineering and formal methods, particularly for safety- and mission-critical systems whose verification depends on mathematically precise specifications. This paper evaluates whether contemporary off-the-shelf Large Language Models (LLMs) can help bridge this gap by generating Linear Temporal Logic (LTL) formulas directly from unstructured requirements. The study e...
  </details>

- **2026-08-06** — Stefan Dziembowski, Grzegorz Fabiański, Daniele Micciancio et al. — [Game Hopping in Lean](http://arxiv.org/abs/2608.06261v1)
  <details><summary>📄 Abstract</summary>
  We present HOPSCOTCH, a Lean 4 framework for mechanizing computationally sound, game-based cryptographic proofs. Security definitions are expressed as indistinguishability between stateful probabilistic oracles, and proofs follow the standard game-hopping paradigm. HOPSCOTCH uses a shallow embedding: oracles and reductions are ordinary Lean definitions, enabling direct integration with the full Lean ecosystem, including general mathematical theories from Mathlib, such as finite-group theory. A g...
  </details>

- **2026-08-06** — Haris Riaz, Hyungji Kim, Mihai Surdeanu — [Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers](http://arxiv.org/abs/2608.06111v1)
  <details><summary>📄 Abstract</summary>
  Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraining and injects it across all three dominant PE families (absolute, relative, rotary), for both encoders and decoders, leaving self-attention and the rest of the architecture untouch...
  </details>

- **2026-08-06** — Zelong Sun, Jun Wang, Kaicheng Yang et al. — [Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval](http://arxiv.org/abs/2608.06060v1)
  <details><summary>📄 Abstract</summary>
  Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs. Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multimodal inputs often misses fine-grained discriminative cues, leading to confusion among semantically similar candidates. Recent methods mitigate this limitation by generating Chain-of-Thought (CoT) rationales to enrich the query representation. However, s...
  </details>

- **2026-08-06** — Zirui Wang, Jiaqi Wang, Qinghan Wang et al. — [EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?](http://arxiv.org/abs/2608.06022v1)
  <details><summary>📄 Abstract</summary>
  Epitopes determine where antibodies bind antigens and shape downstream therapeutic properties such as functional blockade and escape resistance, making epitope understanding central to antibody drug discovery. Although large language models (LLMs) have shown strong biomedical reasoning ability, it remains unclear whether they can infer epitope information directly from antigen and antibody sequences. Existing epitope resources typically focus on isolated prediction tasks or rely on specialized s...
  </details>

- **2026-08-06** — Yuhan Zhou, Yuchu Luo, Hao Nie et al. — [TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure](http://arxiv.org/abs/2608.06007v1)
  <details><summary>📄 Abstract</summary>
  Modern LLM infrastructure increasingly manages tensors not only as computation data, but also as persistent states shared across distributed components. Existing systems optimize individual tensor management tasks, such as model weight loading, KV cache management, and checkpoint synchronization, by deeply integrating task-specific mechanisms with execution engines, networks, or storage backends. However, this specialization creates isolated silos that hinder the reuse and composition of tensor ...
  </details>

- **2026-08-06** — Paweł Batorski, Abtin Pourhadi, Akylgali Aitaza et al. — [MACRO: Markov Chain Routing of Transformer Layers](http://arxiv.org/abs/2608.05872v1)
  <details><summary>📄 Abstract</summary>
  Standard Large Language Models (LLMs) execute layers sequentially. Dynamic layer routing, i.e. search for a different execution path through layers involving layer repetitions, skips and other moves, can improve performance. Existing routing approaches often require updating model weights, running expensive search loops per test instance, or demand ground-truth labels during inference. In this work, we propose Markov Chain Routing of Transformer Layers (MACRO), a framework that learns task-speci...
  </details>

- **2026-08-06** — Hong Jiang, Junnan Zhu, Jingwang Huang et al. — [M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding](http://arxiv.org/abs/2608.05817v1)
  <details><summary>📄 Abstract</summary>
  Metaphor enables the understanding of abstract concepts through cross-domain mappings while conveying affective attitudes. In multimodal scenarios, visual and textual information jointly construct Target--Source mappings, requiring both conceptual understanding and cross-modal reasoning. However, existing benchmarks mainly evaluate metaphor understanding through isolated subtasks and lack evidence-grounded explanations, making it difficult to assess whether models establish mappings grounded in ...
  </details>

- **2026-08-06** —  Vorch Team, Xiaoyu Chen, Yang Ding et al. — [Vorch-Omni: Multi-Task Orchestration of Sight and Sound](http://arxiv.org/abs/2608.05803v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative video modeling have enabled diverse generation, reference-based synthesis, extension, and editing, but existing approaches often rely on fragmented task-specific models. A general model must distinguish heterogeneous target, source, and reference signals to determine what to generate, preserve, or use as guidance, while reducing interference among tasks. Joint audio-visual generation further increases this challenge by introducing diverse conditioning and output con...
  </details>

- **2026-08-06** — Stefan Krsteski, Charlotte Meyer — [Predicting Task Difficulty Without Rollouts](http://arxiv.org/abs/2608.05797v1)
  <details><summary>📄 Abstract</summary>
  Task difficulty dictates an agent's likelihood of success, and estimating it without rollouts means forecasting this directly from a task description before executing costly simulations in stateful environments. Reliable estimates would therefore allow environment designers to calibrate evaluation benchmarks and construct progressive training curricula. This becomes increasingly important as agents move into long-horizon domains, where empirical trial-and-error is a severe computational bottlene...
  </details>

- **2026-08-06** — Lisai Zhang, Yidi Wu, Qi Liu et al. — [Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](http://arxiv.org/abs/2608.05776v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive continuation provides a natural path toward minute-scale audio-visual generation by repeatedly extending a short-window generator conditioned on previously generated video and audio. However, models are trained on clean ground-truth histories, while inference relies on their own generated histories, where accumulated errors cause identity drift, over-smoothing, and audio-visual desynchronization. Recent methods reduce this mismatch by reusing prediction residuals as synthetic corr...
  </details>

- **2026-08-06** — Shuhao Yan, Changhao He, Xi Peng et al. — [RA-CAD: Learning Post-Execution Critique for State-Aware Text-to-CAD Generation](http://arxiv.org/abs/2608.05714v1)
  <details><summary>📄 Abstract</summary>
  Text-to-CAD generation translates natural-language design intent into editable and executable parametric computer-aided design (CAD) codes, reducing the expertise and effort required for manual modeling. Existing methods incorporate fixed, externally supplied, prompt-induced, or separately optimized critique mechanisms to optimize the generation process, but they do not necessarily optimize how feedback is interpreted and translated into effective corrective actions throughout the generation pro...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 571 |
| prompt-injection | 484 |
| memory-poisoning | 44 |
| tool-use-attack | 108 |
| backdoor | 409 |
| adversarial-attack | 554 |
| privacy-leakage | 3796 |
| steganography | 55 |
| misuse | 869 |
| red-teaming | 113 |
| vulnerability | 2615 |
| defense | 2322 |
| alignment | 2159 |
| robustness | 2126 |
| watermark | 263 |
| unlearning | 86 |
| agent-safety | 52 |
| benchmark | 57 |
| survey | 277 |
| other | 6132 |

---

📚 **全部 23092 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-11 06:57:32*