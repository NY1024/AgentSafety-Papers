<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-23312-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-13 02:03 ｜ **论文总数 / Total Papers**: 23312（近 30 天 / Recent 30 days: 2614）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 23312 篇论文（含摘要、分类筛选、搜索）/ View all 23312 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 576
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 486
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 112
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 411
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 555
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3805
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 879
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 114
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2644
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2347
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2182
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2159
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 274
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 86
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 57
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 278
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6196

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2614 篇，完整 23312 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2614 papers from the last 30 days (with date, authors & abstract). For the full list of 23312 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-08-11** — Clemens Vetter, David Kaczér, Lucie Flek et al. — [Data Attribution of Emergent Misalignment with Persona Features](http://arxiv.org/abs/2608.11025v1)
  <details><summary>📄 Abstract</summary>
  Emergent misalignment (EM) is the phenomenon where fine-tuning a language model on a narrow task leads to harmful behavior in unrelated domains. A leading mechanistic account attributes EM to persona features: latent directions acquired during pre-training that misaligned fine-tuning amplifies. We ask where these features come from: which pre-training documents activate them, and whether naturally occurring human-written text suffices to induce EM. Using Sparse Autoencoder (SAE) based model diff...
  </details>

- **2026-08-11** — Xinzhe Huang, Biwu Yao, Kedong Xiu et al. — [ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions](http://arxiv.org/abs/2608.10621v1)
  <details><summary>📄 Abstract</summary>
  Recent research on Large Language Model (LLM) safety has widely adopted guardrails to identify unsafe LLM outputs. Existing guardrails typically formulate safety assessment as a deterministic classification task, mapping a discrete token sequence to a discrete safety label. However, this paradigm has two limitations: First, safety assessment is inherently an uncertain problem, particularly during the early generation state. Second, relying solely on discrete token sequences discards the rich pro...
  </details>

- **2026-08-11** — Chuqiao Lin, Shivaji Sondhi, Xiao-Liang Qi — [Measuring Semantic Abstractness of SAE Features via Nonlocality](http://arxiv.org/abs/2608.10537v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) have helped uncover mechanistic explanations for LLM behaviours such as reasoning, jailbreaking etc., via understanding the corresponding task-relevant and causally effective features. To evaluate such mechanistic explanations, downstream studies must distinguish surface lexical features from genuinely high-level ones. However, neither an autointerp-based semantic description nor causal steering utility fully resolves the abstraction level of a feature. To this end, we...
  </details>

- **2026-08-11** — Md Jafrin Hossain, Mohammad Arif Hossain, Nirwan Ansari — [On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models](http://arxiv.org/abs/2608.10530v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code execution, and maintaining persistent memory. When these agents operate with real-world privileges---calling APIs, modifying files, and querying databases---a compromised reasoning step can trigger unauthorized data access, irreversible state changes, or cascading failures, yet the security research community has not kept pace. To...
  </details>

- **2026-08-11** — Caoyuan Ma, Wenpu Liu, Weichu Xie et al. — [SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning](http://arxiv.org/abs/2608.10513v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) remain vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment inherited from their language backbones. We propose SafeCap, a reinforcement-learning framework that aligns LVLMs through learned self-captioning. SafeCap trains a policy model to first generate a safety-relevant image caption and then produce a final answer; the caption is further optimized by whether it enables a frozen LLM to reach a safety-aligned decision. This c...
  </details>

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-08-10** — Spiros Tsigkopoulos, Christoforos Ntantogian — [From Prompt Injection to Web Exploitation: Revisiting Classic Vulnerabilities in LLM-Integrated Applications](http://arxiv.org/abs/2608.10281v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are increasingly integrated into web applications through chatbots, tool-calling pipelines, and agentic workflows. In these systems, user input may influence not only generated text, but also backend actions such as database queries, HTTP requests, file operations, template rendering, or API calls. This paper introduces LLM-mediated web attacks, a class of attacks in which attacker-controlled input is transformed by an LLM-integrated application and then reaches traditional...
  </details>

- **2026-08-10** — Jordan Pettyjohn, Mansi Sakarvadia, Nathaniel Hudson et al. — [Interpreting Language Model Hidden States at Scale](http://arxiv.org/abs/2608.10260v1)
  <details><summary>📄 Abstract</summary>
  Lens methods interpret large language models (LLMs) by mapping intermediate activations to the output vocabulary, revealing how next-token predictions develop through the network. Trained lenses remain expensive: affine-translator parameters grow quadratically with model width, while exact, full-vocabulary Kullback--Leibler (KL) training dominates memory. Consequently, prior trained lenses have been applied to models of at most 20B parameters and remain tied to particular component types. We pre...
  </details>

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


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 11 papers

- **2026-08-11** — Giuseppe Destefanis, Daniel Graziotin, Matteo Vaccargiu et al. — [GitSkills: A Dataset of Agent Skills on GitHub](http://arxiv.org/abs/2608.10906v1)
  <details><summary>📄 Abstract</summary>
  An agent skill is a folder containing a SKILL.md file with instructions for a language-model agent, optionally accompanied by scripts and reference files. The agent loads the skill when it judges that a task matches the skill description. Anthropic introduced the format in October 2025 as an open specification. Nine months later, we find that skill files in the millions sit in public GitHub repositories. Skills are unlike the artifacts the SE research community usually mines: they are written ma...
  </details>

- **2026-08-10** — Bohan Lin, Hejia Geng, Xinyi Xie et al. — [Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution](http://arxiv.org/abs/2608.09248v2)
  <details><summary>📄 Abstract</summary>
  Skill-based LLM agents select reusable procedures from an external library to solve complex tasks, yet their routing decisions rely entirely on text-level signals such as task descriptions, verbal reflections, and experience-derived rules, while the model's own internal representational state remains unobserved. Recent interpretability work has shown that LLMs maintain linear emotion representations that causally influence behavior; however, these representations have been exploited only for pos...
  </details>

- **2026-08-10** — XPolicyLab Community, Tianxing Chen, Yue Chen et al. — [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](http://arxiv.org/abs/2608.09892v2)
  <details><summary>📄 Abstract</summary>
  Robot policy evaluation and deployment remain fragmented by model-specific software dependencies, data representations, and runtime interfaces, so that connecting N policies to M evaluation environments requires O(NM) separate integrations. We present XPolicyLab, a unified standard and open ecosystem that reduces this cost to O(N+M). XPolicyLab specifies common observation, action, and trajectory schemas together with a minimal adapter interface for observation updates, action prediction, batche...
  </details>

- **2026-08-10** — Shuyan Huang, Kai Du, Andrew Lan — [Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories](http://arxiv.org/abs/2608.10319v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-powered agents have rapidly evolved from code-completion tools into solvers of complex software engineering tasks. As developers collaborate with coding agents over time, their preferences emerge through repeated interactions and can be used to adapt agent behavior to better meet individual developers' needs. Capturing and reusing these preferences may reduce repeated corrections and improve developer-agent collaboration. Agent skills provide a lightweight mechanism fo...
  </details>

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


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-08-11** — Tao Lin, Gaojie Jin, Zongxin Liu et al. — [Once Poisoned, Arbitrarily Controlled: A Programmable Backdoor in VLMs](http://arxiv.org/abs/2608.10959v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language model (VLM) backdoors are usually treated as static vulnerabilities: one-to-one and N-to-N attacks bind one or more triggers to a finite set of targets before victim training. This assumption substantially underestimates the threat. We show that a single poisoning phase can implant a programmable backdoor into a VLM, allowing an attacker to choose previously unseen target-caption semantics at inference time and synthesize corresponding stealthy triggers on demand. Unlike...
  </details>

- **2026-08-10** — Yunhao Liang, Chengguang Gan, Ruixuan Ying et al. — [Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits](http://arxiv.org/abs/2608.09740v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate functionally useful code that remains vulnerable, while security-focused interventions may break intended behavior. We investigate security tests as executable specifications both before generation and during iterative repair. We develop SecTDD, a controlled test-feedback scaffold that separates three factors: whether tests are shown upfront, whether failed executions trigger revision, and how failures are selected and represented. The evaluation uses be...
  </details>

- **2026-08-10** — Yunhao Liang, Chengguang Gan, Ruixuan Ying — [Security Tests as Executable Specifications for LLM Code Generation: Benefits, Trade-offs, and Coverage Limits](http://arxiv.org/abs/2608.09740v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate functionally useful code that remains vulnerable, while security-focused interventions may break intended behavior. We investigate security tests as executable specifications both before generation and during iterative repair. We develop SecTDD, a controlled test-feedback scaffold that separates three factors: whether tests are shown upfront, whether failed executions trigger revision, and how failures are selected and represented. The evaluation uses be...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 6 papers

- **2026-08-10** — Berkay Ozcam, Irem Onen, Mehmet Fatih Amasyali et al. — [Generating Attacks for LLMs with GFlowNets](http://arxiv.org/abs/2608.10171v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Large Language Models (LLMs) has facilitated their ubiquitous integration into various domains, leading to widespread adoption. However, this escalating trend has introduced significant security vulnerabilities, necessitating the identification and mitigation of flaws arising from malicious exploitation. Red teaming assessments, conducted to evaluate model robustness through diverse adversarial inputs, are essential for exposing security risks and implementing countermea...
  </details>

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


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 23 papers

- **2026-08-11** — Chen Lyu, Xingwei Tan, Simon Cullen et al. — [ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls](http://arxiv.org/abs/2608.11200v1)
  <details><summary>📄 Abstract</summary>
  Synthetic dialogue generation offers a way to study conversational dynamics in sensitive domains where real data are difficult to access, release, or annotate. The underlying abuse may occur online or offline: threats and coercion can appear directly in messages, while behaviours such as surveillance, isolation, stalking, and physical violence may be planned, disclosed, or referred to conversationally. Privacy and legal constraints make it difficult the release of large-scale real conversation d...
  </details>

- **2026-08-11** — Fengming Yao, Man Luo — [Partially Observable Learning for Multi-Platform Dispatch Optimization](http://arxiv.org/abs/2608.10897v1)
  <details><summary>📄 Abstract</summary>
  Instant delivery platforms have become a critical component of urban logistics, increasingly relying on crowdsourced couriers to fulfill highly dynamic orders. In real-world systems, couriers are not exclusive to a single platform and may concurrently serve multiple platforms, while each platform can only observe its own orders and couriers' interactions due to privacy and operational constraints. This results in a multi-platform dispatch environment with inherent partial observability. However,...
  </details>

- **2026-08-11** — Yiyang Su, Jie Zhu, Feng Liu et al. — [SapiensID 2.0: Aligning Human Recognition Foundation Models with Human Perception](http://arxiv.org/abs/2608.10497v1)
  <details><summary>📄 Abstract</summary>
  While foundation models have significantly advanced human recognition across diverse modalities, they predominantly rely on static, geometric feature extraction. This approach fundamentally diverges from human perception. Consequently, current models often suffer from "semantic blindness," overfitting to transient noise while failing to leverage invariant soft biometrics, and struggle to capture temporal motion signatures. To bridge this gap, we propose SapiensID 2.0, a human recognition framewo...
  </details>

- **2026-08-11** — Zhen Yang, Mengqi Wang, Gengda Zhao et al. — [Calibrating Post-Training Feature Shifts for LLM Data Contamination Detection](http://arxiv.org/abs/2608.10462v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are trained on massive and largely undisclosed corpora that may contain copyrighted or privacy-sensitive content. Data contamination detection (DCD) therefore aims to determine whether a given text is a member of the pre-training corpus of a target LLM. Recent state-of-the-art DCD methods follow a feature-based paradigm that derives membership features from the input text and the corresponding model output. However, most modern LLMs undergo post-training, such as ins...
  </details>

- **2026-08-11** — Luis Amorim, Vitor Cerqueira, Moises Santos et al. — [Benchmarking Time Series Generation Methods for Privacy-Preserving Forecasting](http://arxiv.org/abs/2608.10891v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting in privacy-sensitive domains often requires training models on released data rather than original observations. Synthetic time series generation has been developed primarily for data augmentation, where generated series supplement the original training set. How well these methods perform when fully replacing the original data - and how much privacy risk the released series carry - remains underexplored. We address this gap through a benchmark evaluating synthetic generati...
  </details>

- **2026-08-10** — Xuexiong Yin, Zechuan Chen, Yongsen Zheng et al. — [UserToolBench: A User-Profile-Hidden Benchmark for Personalized Decision Making in Tool-Use LLMs](http://arxiv.org/abs/2608.10042v1)
  <details><summary>📄 Abstract</summary>
  Tool-use LLMs are increasingly asked to act on users' behalf, but existing benchmarks usually focus on profile recall, style imitation, generic tool use, or response-level personalization. We introduce UserToolBench , a benchmark for personalized decision making in tool-use LLMs. UserToolBench tests whether a model can infer latent user preferences from interaction history, recognize when clarification is needed, and produce user-aligned tool-call trajectories under incomplete information. The b...
  </details>

- **2026-08-10** — Liang Zhang, Stephen Hwang, Yue Ma et al. — [Fine-Tuning Large Language Models for Codebook-Guided Coding of Students' Mathematics Metaphor Responses](http://arxiv.org/abs/2608.10276v1)
  <details><summary>📄 Abstract</summary>
  Student-generated metaphors about mathematics can reveal students' attitudes, beliefs, identities, and experiences, but human expert coding of these thematically and semantically complex open-ended responses is time-intensive and difficult to scale. This study examines whether LoRA-based supervised fine-tuning of large language models (LLMs) can improve their performance on codebook-guided coding tasks for student mathematics metaphors. We used a human-coded corpus of 2,265 Grade 6-8 responses t...
  </details>

- **2026-08-10** — Qingfeng Zhang, Yuanxiong Guo, Yanmin Gong — [Locally Deployable Small Language Models for Emergency Department Decision Support: A Systematic Benchmark of Fine-Tuning Strategies](http://arxiv.org/abs/2608.10273v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models (LLMs) for decision support in emergency departments (EDs) faces two major challenges: privacy risks of transmitting patient data to closed-source commercial LLMs and the lack of systematic evaluation of fine-tuning strategies for locally deployable open-source small language models (SLMs). We benchmarked eight open-source SLMs using zero-shot prompting, prefix tuning, Low-Rank Adaptation (LoRA), and full fine-tuning on three ED tasks: triage level prediction, spe...
  </details>

- **2026-08-10** — Zimu Zhou, Enrique A. Lopez-Guerra, Michael Kwan et al. — [Practical Evaluation of FFT-Based Thickness Extraction for Thick-Film Reflectometry](http://arxiv.org/abs/2608.10146v1)
  <details><summary>📄 Abstract</summary>
  Fast Fourier transform (FFT) is widely used for thick-film reflectometry because of its simplicity and computational efficiency. However, its performance under practical thick-film measurement conditions has received limited experimental evaluation. In this work, FFT, Linearized Reflectance Zero-Crossing (LRZ), and optical model fitting were compared using reflectometry measurements from a nominal 52 μm dielectric film acquired on a production wafer, with White-Light Interferometry (WLI) serving...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 18 papers

- **2026-08-11** — Abigail Oppong, P Sam Sahil, Tadesse Destaw Belay et al. — [The Illusion of Cross-Lingual Safety in Low-Resource Languages](http://arxiv.org/abs/2608.11146v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models (LLMs) is largely developed in English, assuming these safeguards generalize across multilingual settings. However, this assumption remains underexplored and exposes a vulnerability in low-resource languages. We investigate cross-lingual safety transfer in four African languages, Twi, Hausa, Amharic, and Swahili, using LoDNA, a new safety dataset that pairs literal translations with culturally localized prompts. To move beyond generation-based evaluation...
  </details>

- **2026-08-11** — Zixing Chen, Xingyuan Liu, Jie Zhu et al. — [REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems](http://arxiv.org/abs/2608.10669v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents combine language-based reasoning with external tools to perform complex tasks. Adversarial inputs can exploit interactions between the agent and its environment, causing the agent to violate safety policies during execution. Yet existing evaluations often reduce agent safety to a single attack success rate (ASR), collapsing exposure, execution, observation, and adjudication and potentially conflating actual violations with evidence visibility. We introduce REDAg...
  </details>

- **2026-08-11** — Muhammad Mubeen, Arslan Bisharat, Giri Anandhi — [Strategies to Avoid Illegal Data Access](http://arxiv.org/abs/2608.11153v1)
  <details><summary>📄 Abstract</summary>
  For companies of all sizes, data security is a top priority. The chance of unauthorized data access increases as technology develops. To prevent unwanted access to their data, businesses must be proactive. This study examines technology solutions, personnel training, and policy enforcement as methods to prevent unauthorized data access. Data may be protected from illegal access using technological solutions like firewalls, intrusion detection systems, and encryption. Intrusion detection systems ...
  </details>

- **2026-08-11** — Weiyao Huang, Liqin Wang, Ziqi Sheng et al. — [NullEdit: Stealthy Image Protection via VLM Condition Redirection](http://arxiv.org/abs/2608.10870v1)
  <details><summary>📄 Abstract</summary>
  Modern image editors combine vision-language models (VLMs) with diffusion transformer backbones to modify a single reference image according to instructions without fine-tuning. This capability also enables unauthorized manipulation of publicly released images. Existing inference-time defenses either invalidate edits through conspicuous corruption, thereby exposing the protection, or allow them to proceed with identity or reference content drift, thereby failing to prevent the editing behavior i...
  </details>

- **2026-08-11** — Shengzhi Wang, Jun Yang, Kai Wu et al. — [MIRA: Medical Image Reflection for Agentic Diagnosis](http://arxiv.org/abs/2608.10827v1)
  <details><summary>📄 Abstract</summary>
  Medical visual agents can use tools to inspect images and retrieve external knowledge, but indiscriminate tool use may introduce noisy or misleading evidence. Reliable diagnosis therefore requires not only acquiring additional observations, but also verifying whether tool actions are necessary and whether the resulting evidence supports the current hypothesis. We introduce MIRA (Medical Image Reflection for Agentic Diagnosis), a medical visual diagnostic framework for autonomous evidence search ...
  </details>

- **2026-08-11** — Lena Holzwarth, Rita González-Márquez, Dmitry Kobak — [Most biomedical publications show signs of LLM-assisted writing](http://arxiv.org/abs/2608.10715v1)
  <details><summary>📄 Abstract</summary>
  Over the past several years, LLM-powered chatbots and agents have become widely used as a tool for academic writing. LLM-assisted writing can be valuable by removing language barriers but at the same time causes concerns about misconduct and fraud. To inform policy decisions, it is necessary to monitor the prevalence of LLM-altered texts in scholarly publications. Despite some recent progress in this direction, no existing method can produce reliable estimates. Here we suggest and validate a new...
  </details>

- **2026-08-11** — Minh Tran, Trinh Chau, Thanh-Nhan Le et al. — [How Robust Are LLMs to Vietnamese Dialects?](http://arxiv.org/abs/2608.10414v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are typically evaluated on standard written Vietnamese, yet everyday communication frequently involves regional dialects that preserve meaning but differ in surface form. Existing Vietnamese dialect work largely addresses this issue through dialect-to-standard normalization instead of measuring how the model fails under Vietnamese dialectal inputs. To address this gap, we present the first systematic evaluation of LLM robustness to Vietnamese dialect variation across...
  </details>

- **2026-08-10** — Yuqiao Xu, Osama Zafar, Alexander Nemecek et al. — [Beyond Detection: Evaluating Defensive LLMs Against AI-Generated Social Engineering in Live Turn-by-Turn Interaction](http://arxiv.org/abs/2608.10239v1)
  <details><summary>📄 Abstract</summary>
  Generative AI makes social-engineering attacks more fluent, adaptive, and scalable, increasing the need for LLM-based de- fenders that can protect users during ongoing interactions. We ask whether such defenders identify the structural source of risk or merely react to surface cues. We formalize trust-chain localization: identifying whether an interaction fails at actor authority, asset control, verification sufficiency, or transaction path. We construct a controlled 300-case online-housing corp...
  </details>

- **2026-08-10** — Andrew Smart, Shazeda Ahmed, Jackie Kay et al. — [Toward a Theory of Value in AI Alignment](http://arxiv.org/abs/2608.10327v1)
  <details><summary>📄 Abstract</summary>
  Can AI systems be aligned to human values? The popularization of large language models (LLMs) and multi-modal foundation models has seen a rise in harms spanning from toxic speech and hallucinations to AI agents executing unauthorized actions. Within the field of AI safety, these harmful instances are often framed as the alignment problem, or of models being misaligned with human values. Researchers have responded by pursuing applied and theoretical AI value alignment efforts, often without spec...
  </details>

- **2026-08-10** — Vassilis Papadopoulos, McNair Shah, Sam Zimmerman et al. — [Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems](http://arxiv.org/abs/2608.10218v1)
  <details><summary>📄 Abstract</summary>
  AI agents are becoming more autonomous and increasingly interconnected, exposing them to new emergent risks arising from agent-to-agent interaction. One such risk is the spread of mind viruses: ideas or goals that propagate through multi-agent systems by inducing the agents that adopt them to transmit them onward. In addition to propagating, a mind virus may also induce other behavioural changes in its host, which may be benign or harmful. We construct mind viruses with a simple evolutionary alg...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-08-11** — Lukasz Olejnik, Wenchao Dong, Jonas R. Kunst et al. — [IO Factory: Simulating AI-Enabled Influence Campaigns at Scale](http://arxiv.org/abs/2608.10920v1)
  <details><summary>📄 Abstract</summary>
  We introduce IO Factory, an AI-driven framework for simulating information and influence campaigns as fully integrated, traceable processes. The threat of digital manipulation now extends beyond persuasive text from individual language models to AI swarms, i.e., persistent groups of coordinated agents that adapt to platform feedback and disguise organized campaigns as ordinary social interaction. Because such campaigns cannot be identified from isolated messages alone, they must be analyzed acro...
  </details>

- **2026-08-10** — Yuanhe Zhang, Weiliu Wang, Jie Ren et al. — [From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs](http://arxiv.org/abs/2608.09158v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) have demonstrated strong capabilities in understanding diverse audio inputs. This diversity includes low-frequency signals that are inaudible to humans but can still enter the model and influence its generation. However, the practical impact of such low-frequency inputs on LALMs remains largely unexplored. In this paper, we propose Intermittent Low-Frequency Lockout (ILL), an inaudible red teaming method that evaluates this risk using a universal waveform temp...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 54 papers

- **2026-08-11** — Wenrui Bao, Tianyun Jiang, Zhiben Chen et al. — [Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning](http://arxiv.org/abs/2608.11204v1)
  <details><summary>📄 Abstract</summary>
  Learning reliable surgical manipulation policies is bottlenecked by the scarcity of action-labeled demonstrations: teleoperated surgical robot (e.g., dVRK) trajectories with synchronized kinematics are costly to collect, while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordination. Endoscopic video is comparatively inexpensive and abundant relative to synchronized video--kinematics trajectories, and a natural way to exploit it is to learn world models o...
  </details>

- **2026-08-11** — Bowei Liu, Zheng Lu, Yuhan Bian et al. — [VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics](http://arxiv.org/abs/2608.11201v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in video generation models have significantly improved the realism of synthetic videos, blurring the boundary between generated and authentic content and raising concerns about misinformation. Existing MLLM-based detectors mainly rely on supervised fine-tuning or label-level reinforcement learning, where coarse supervision limits generalization to unseen scenarios and emerging video generators. To overcome these limitations, we are the first to introduce \textbf{meta-detection} i...
  </details>

- **2026-08-11** — Shiyu Xuan, Zechao Li — [Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation](http://arxiv.org/abs/2608.11191v1)
  <details><summary>📄 Abstract</summary>
  GUI Visual Grounding is a fundamental capability for GUI agents. Existing models typically freeze their parameters after deployment, limiting their ability to adapt to unseen interfaces. Although recent methods attempt to adapt models via test-time reinforcement learning, they cannot reflect upon failed exploration. To overcome this, we propose a Test-Time Self-Evolving framework that enables models to improve after deployment without human-annotated ground truth. It constructs a closed-loop of ...
  </details>

- **2026-08-11** — Huafeng Chen, Yueming Lyu, Ziyuan Chen et al. — [PRMU: A Corpus-Free Benchmark for Person-Centric Knowledge Unlearning in Multimodal Large Language Models](http://arxiv.org/abs/2608.11149v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have demonstrated remarkable capabilities in storing and recalling rich person-related knowledge, raising increasing concerns about reliable knowledge removal. However, existing machine unlearning approaches for MLLMs typically assume access to original forget and retain corpora, which are often unavailable in realistic deletion scenarios. To address this limitation, we introduce PRMU, a benchmark for evaluating corpus-free multimodal unlearning under rea...
  </details>

- **2026-08-11** — Yuan Zhong, Kaile Chen, Qi Lu et al. — [High-dimensional Supermode Photonics Enabled by Hierarchical Supersymmetric Transformation](http://arxiv.org/abs/2608.11099v1)
  <details><summary>📄 Abstract</summary>
  Modes provide a fundamental degree of freedom for photonic information processing, yet conventional multimode waveguides exhibit non-equidistant effective-index distributions, making closely spaced modes vulnerable to intermodal crosstalk. Supermode photonics can overcome this limitation by geometrically engineering coupled waveguide arrays to realize large and equidistant effective-index spacing, but precise supermode excitation and detection remain challenging at the subwavelength scale. Here,...
  </details>

- **2026-08-11** — Xinrui Lin, Sha Zhang, Shumin Wang et al. — [ThinkAfford: Affordance-Centric Reasoning for Fine-Grained 3D Grounding in Cluttered Scenes](http://arxiv.org/abs/2608.10981v1)
  <details><summary>📄 Abstract</summary>
  Task-driven 3D affordance grounding aims to localize the functional region in a cluttered 3D scene that enables an action specified by a natural-language instruction. Existing methods either predict 3D masks directly or construct them by selecting and fusing intermediate 2D/3D regions. However, they remain vulnerable to two intertwined failure modes: the predicted or selected regions may miss the target interaction area or have unsuitable granularity, while language grounding may confuse visuall...
  </details>

- **2026-08-11** — Nikita Borodin, Maria Krylova, Artem Zabolotnyi et al. — [Diffract: Spectral View of LLM Domain Adaptation](http://arxiv.org/abs/2608.10850v1)
  <details><summary>📄 Abstract</summary>
  We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent head heterogeneity, which we exploit to define a head im...
  </details>

- **2026-08-11** — Mykhailo Koshil, Matthias Feurer, Katharina Eggensperger — [TACTICL: Task-Aware Compression of Tabular ICL Models](http://arxiv.org/abs/2608.10837v1)
  <details><summary>📄 Abstract</summary>
  The strong performance of foundation models for tabular tasks comes at substantial inference costs. Distilling models into task-specific architectures reduces model size and computational demands but also sacrifices in-context adaptability. Here we introduce TACTICL, an automated task-aware compression framework for tabular in-context learning models that jointly prunes transformer layers and replaces them with lightweight adapters trained on downstream tasks, thus blending in-context with in-we...
  </details>

- **2026-08-11** — Naren Kumar S, Tirth Bhatt, Mayank Singh — [Where To Look? : Causal Tracing of Vision Encoders in VLM](http://arxiv.org/abs/2608.10758v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models can describe an image with remarkable accuracy, yet a more fundamental question remains unanswered: what visual information actually drives their answers? In this work, we investigate this question through causal tracing, and we observe that highly causal vision tokens often lie outside the target region. Extending the analysis to larger vision-language models reveals a similar pattern across models and corruption settings, suggesting that strong multimodal performance doe...
  </details>

- **2026-08-11** — Joaquin G. Lopez-Cepero, Rafael Vazquez, Julio C. Sanchez — [LQR Design For Formation Flying Near Halo Orbits Exploiting Quasi-Periodic Symmetry In Toroidal Coordinates](http://arxiv.org/abs/2608.10726v1)
  <details><summary>📄 Abstract</summary>
  This work presents the design of a Linear Quadratic Regulator for relative motion control near periodic orbits in the Circular Restricted Three-Body Problem (CR3BP), formulated in non-singular toroidal coordinates. The key result exploits the rotational quasi-periodicity of the toroidal coordinate transformation. A uniqueness argument on the stabilizing solution of the associated difference Riccati equation proves the optimal control gains need only be computed for a single orbital period. The c...
  </details>

- **2026-08-11** — Evelijn Akerboom, Hirohsi Sugimoto, Minoru Fujii et al. — [Revealing time characteristics of optical excitations in dielectric and plasmonic structures through cathodoluminescence interferometry](http://arxiv.org/abs/2608.10721v1)
  <details><summary>📄 Abstract</summary>
  Cathodoluminescence (CL) spectroscopy provides access to optical excitations with nanometer spatial resolution, but direct time-resolved measurements of optical resonances remain challenging. Here, we demonstrate that CL interferometry provides access to the temporal response, phase behavior, and modal spectral structure of resonant nanoscale scatterers without requiring ultrafast pump-probe schemes. We develop an analytical framework in which Fourier transformation angle- and frequency-resolved...
  </details>

- **2026-08-11** — Aryan Vijay Bhosale, Harshit Rajgarhia, Akhil Pothanapalli et al. — [DuplexWorld: Can voice agents help you get through the day?](http://arxiv.org/abs/2608.10716v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-speech (S2S) voice agents are increasingly being incorporated into enterprise for customer care and as daily companions for consumers owing to the ease of the conversational modality over text. However, existing benchmarks fail to holistically evaluate voice agents along axes that really matter and are shaped as tests of agentic tool calling against a database. We believe they fail to adequately account for the diversity of conversational dialogue that mundane activities introduce and ...
  </details>

- **2026-08-11** — Tal Oved, Roi Pony, Oshri Naparstek et al. — [Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization](http://arxiv.org/abs/2608.10694v1)
  <details><summary>📄 Abstract</summary>
  Evolutionary optimization of LLM prompts and agentic programs (e.g., GEPA) is dominated by fitness evaluation: scoring each candidate runs an answering LLM over a validation set, so the evaluator's price tier dictates total search cost. We restructure that search by decoupling the three roles an LLM plays, running the high-volume answering role on the cheapest tier, reserving a strong model for the rare reflection/variation operator, then exploiting upward cross-tier transfer to deploy the cheap...
  </details>

- **2026-08-11** — Qi Ming, Yuyang Wang, Mingjing Zhao et al. — [Bridging Severe Cross-Modal Misalignment: End-to-End Visible-Infrared Object Detection via Explicit Feature-Domain Affine Registration](http://arxiv.org/abs/2608.10680v1)
  <details><summary>📄 Abstract</summary>
  Visible-infrared object detection relies on complementary RGB and thermal cues, but its performance is often degraded by cross-modal spatial misalignment. Most existing methods rely on implicit feature adaptation to handle weakly misaligned scenarios, while large-offset geometric discrepancies remain insufficiently addressed. In this paper, we propose a Joint Feature-domain Registration and Detection network (JFRDet), an end-to-end visible-infrared oriented object detector tailored for severely ...
  </details>

- **2026-08-11** — Lijun Xia, Xuemei Gu, Kai Wang et al. — [Photonic realization of a subgraph extraction in a quantum random network](http://arxiv.org/abs/2608.10663v1)
  <details><summary>📄 Abstract</summary>
  Understanding how complex connectivity emerges in networks is a fundamental challenge in classical and quantum science. In classical random networks, complex subgraphs typically require relatively high connection probabilities, whereas quantum random network theory predicts that such structures can arise at a single, lower threshold through entanglement and local operations. Here, using an integrated silicon photonic chip, we experimentally realize a quantum subgraph predicted by quantum random ...
  </details>

- **2026-08-11** — Ze Yu, Hongwei Zhen, Chao Shen et al. — [AIDC Microgrid Vulnerability Assessment Under Computing-Power Coordinated Attacks](http://arxiv.org/abs/2608.10645v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of large language model (LLM) services is accelerating the expansion of AI data centers (AIDCs), intensifying concerns over power system resource adequacy and rising carbon emissions. The integration of renewable energy provides a pathway toward addressing these pressures, but it also introduces new cross-domain stability challenges to low-carbon AIDCs. For example, variability in renewable generation affects reliability on the supply side, whereas fluctuations in AIDC workloads...
  </details>

- **2026-08-11** — Jonas Luhrmann, José M. Palacios, Fabio Pusateri et al. — [Asymptotic stability of the degree-one vortex in the abelian Yang-Mills-Higgs model: Linear Theory](http://arxiv.org/abs/2608.10609v1)
  <details><summary>📄 Abstract</summary>
  We study the linearized dynamics near the degree-one vortex of the $(1+2)$-dimensional abelian Yang-Mills-Higgs model at the self-dual coupling, restricted to equivariant perturbations in the orthogonal gauge. The linearized operator is a selfadjoint matrix Schrödinger operator $\mathbf{M}$ on radial $L^2_{\mathrm{rad}}(\mathbb{R}^2;\mathbb{R}^4)$ with continuous spectrum $[1,\infty)$ and a two-dimensional internal mode at a unique gap eigenvalue $λ^2 \in (0,1)$, as established in Part I of our ...
  </details>

- **2026-08-11** — Chunbo Lin, Xinggang Shang, Xijun Li et al. — [Direct experimental measurement of femtonewton-scale momentum transfer force from electron beams](http://arxiv.org/abs/2608.10582v1)
  <details><summary>📄 Abstract</summary>
  Electron beams (e-beams) are ubiquitous in imaging, patterning, and propulsion. This prevalence is rooted in the profound mastery of their wave-particle duality and energy-transfer pathways. Yet, a fundamental dimension remains largely unexplored: while the mechanical effect (i.e., the momentum transfer to a target) is theoretically known, quantification of its femtonewton-range force has remained elusive. This discrepancy represents a missing piece of the puzzle toward a comprehensive understan...
  </details>

- **2026-08-11** — Akiko Nishiyama, Grzegorz Kowzan, Dominik Charczun et al. — [Benchmark measurements of absolute frequencies and collisional line-shape parameters in the CO-Ar system using comb-based FTS](http://arxiv.org/abs/2608.10508v1)
  <details><summary>📄 Abstract</summary>
  We report absolute frequency measurements of the CO fundamental band, together with high-precision Ar-induced collisional line-shape parameters using comb-based Fourier-transform spectroscopy. High-quality spectra were obtained with a stable mid-IR optical frequency comb source and careful suppression of technical noise. By applying analysis methods that fully exploit the advantages of optical frequency comb spectroscopy, precise frequency calibration and robust multi-line fitting were achieved,...
  </details>

- **2026-08-11** — Congyang Ou, Ruike Song, Yang Zhou et al. — [When Vision Becomes Text: Visual Token Pruning via Cross-Modal Residual Guidance in VLMs](http://arxiv.org/abs/2608.10489v1)
  <details><summary>📄 Abstract</summary>
  Abundant visual information strengthens vision-language model (VLM) perception, yet massive visual tokens raise inference costs. Existing visual token pruning methods rely on similarity-based guidance, which exploits pairwise text-vision and vision-vision token correlations for compression. However, such methods only capture local layer-level signals and overlook the whole inference process in VLM. In this paper, we revisit VLM inference and present a new efficient guidance scheme that complemen...
  </details>

- **2026-08-11** — Ruizhong Liu, Tingzhang Luo, Zaiyan Zhang et al. — [GeoSeg-OV: Bridging Geospatial Gaps with Structural Guidance for Open-Vocabulary Remote Sensing Segmentation](http://arxiv.org/abs/2608.10426v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary remote sensing segmentation has recently emerged as a promising paradigm that enables pixel-level recognition of arbitrary categories specified by natural language, including classes unseen during training. However, geospatial domain shifts caused by heterogeneous regions, spatial resolutions, and acquisition platforms weaken visual-text matching and limit cross-dataset generalization. Recent attempts have begun to incorporate auxiliary vision foundation models (VFMs), typically ...
  </details>

- **2026-08-11** — Zebin Xing, Yupeng Zheng, Qiang Chen et al. — [DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving](http://arxiv.org/abs/2608.10413v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for end-to-end autonomous driving by enabling unified reasoning across perception, language, and planning. However, existing approaches lack mechanisms to exploit past failures or adapt to distribution shifts, causing the model to persistently underperform on similar scenarios where it has previously failed. In this paper, we propose DriveVLA-M0, a retrieval-augmented VLA with failure-aware latent memory. We constr...
  </details>

- **2026-08-11** — Shuozhe Cheng, Kunlan Xiang, Mingxuan Li et al. — [Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models](http://arxiv.org/abs/2608.10405v1)
  <details><summary>📄 Abstract</summary>
  Many studies have shown that specially crafted inputs can induce large language models (LLMs) to generate excessively long outputs, resulting in significant computational overhead and resource consumption. While most existing denial-of-service (DoS) attacks target text-only LLMs, end-to-end (E2E) speech LLMs are rapidly emerging. Existing text-based DoS attacks primarily rely on prompt engineering, such as adversarial suffixes or semantic inducement, which exploit the discrete nature of text inp...
  </details>

- **2026-08-11** — Eunjeong Kim, Yeong Jun Jeon, Myeonggyun Han — [MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices](http://arxiv.org/abs/2608.10362v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates autoregressive large language model (LLM) inference by using a lightweight draft model to speculate multiple tokens, reducing expensive target model decoding steps. Its effectiveness depends heavily on draft selection, motivating adaptive methods that exploit variation across inputs and generation stages. On memory-constrained edge devices, however, these methods often fail to improve end-to-end throughput due to the overhead of switching between draft models. We...
  </details>

- **2026-08-11** — Yuhang Yao, Zeyu Wang, Wanyi Chen et al. — [MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale](http://arxiv.org/abs/2608.10333v1)
  <details><summary>📄 Abstract</summary>
  LLM agents execute heterogeneous sequences of model calls within a single task: some invocations require careful reasoning, while others are structured steps such as formatting or tool-argument construction. Prior routing methods exploit this asymmetry by assigning easy invocations to a cheaper small model and difficult ones to a large model. Such policies reduce inference cost, but they leave the small model's capability unchanged, so attainable savings remain bounded by the work the student ca...
  </details>

- **2026-08-10** — Costain Nachuma, Minhaz F. Zibran — [Comprendia: AI-Augmented Code Comprehension](http://arxiv.org/abs/2608.10290v1)
  <details><summary>📄 Abstract</summary>
  Comprendia is an Eclipse plugin that integrates structural dependency visualization with LLM-powered code explanation on a shared interactive graph for Java program comprehension. The tool rests on four pillars: (1) a multi-edge-type dependency graph with live search and multiple layouts; (2) LLM explanations grounded in Graph-Aware Callee Pruning (GACP), an auditable strategy that selects relevant callees using the same graph the developer navigates; (3) a clone-detection overlay that highlight...
  </details>

- **2026-08-10** — Beidi Zhao, Yaoqi Chen, Yuru Feng et al. — [MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory](http://arxiv.org/abs/2608.10108v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far back in the history. External memory stores such trajectories as structured representations, yet each structure provides a distinct and incomplete view. Existing multi-memory systems either read a fixed set of structures for every query, inflating context and introducing noise, or route each query to a single structure, p...
  </details>

- **2026-08-10** — Hejia Zhang, Sheng Lu, Zhongming Yu et al. — [CHORUS: Complementary Experts for High-Coverage Testbench Stimulus Generation](http://arxiv.org/abs/2608.10090v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have advanced code generation, where executable feedback provides a more reliable learning signal than textual imitation alone. Hardware verification is an important application of code generation and accounts for a substantial fraction of modern chip design effort, with high-coverage testbench stimulus generation as a key task. We present CHORUS, a post-training framework that pushes performance beyond what a conventional supervised fine-tuning (SFT)-to-reinforcemen...
  </details>

- **2026-08-10** — Ang Jia, He Jiang, Zhipeng Yang et al. — [N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching](http://arxiv.org/abs/2608.10043v1)
  <details><summary>📄 Abstract</summary>
  Program-level Binary Code Similarity Analysis (BCSA) aims to identify semantically similar code regions across binary programs, serving as a fundamental technique for software plagiarism detection, vulnerability search, and malware analysis. Existing approaches often decompose binaries into modules following the structure of function call graphs (FCGs) and then match these modules by their contained functions. However, function inlining changes both FCG structures and binary function semantics, ...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 60 papers

- **2026-08-11** — Caili Yu, Yiqi Wang, Jiaqi Zhang et al. — [From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents](http://arxiv.org/abs/2608.10502v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning, tool use, answers, and subsequent memory writes. Existing defenses mainly detect or delete suspicious memories, or revise the current response. Deleting the source leaves already propagated claims, actions, and derived memories active, whereas resetting the store or replaying the full trace destroys benign state and repe...
  </details>

- **2026-08-11** — Jinmo Han, Jimin Hong, Chanyeong Moon et al. — [MD-ProTector: Positioning Multiple Data-Driven Prototypes for LLM-Generated Text Detection](http://arxiv.org/abs/2608.10459v1)
  <details><summary>📄 Abstract</summary>
  As LLM-generated content becomes more sophisticated, detection systems for distinguishing those texts from human-written text must operate at scale while handling diverse writing styles, domains, languages, and generator models. Input-only encoder detectors are suitable for practical deployment setting, but standard binary classification supplies only the class label and does not explicitly organize the substantial variation within either class. We propose MD-ProTector, which represents each cla...
  </details>

- **2026-08-11** — Moti Rattan Gupta, Anupam Sobti — [SAR2Agri: Learning SAR Intensity Representations for Agricultural Monitoring](http://arxiv.org/abs/2608.11142v1)
  <details><summary>📄 Abstract</summary>
  Agricultural monitoring faces unique challenges, arising from the landscape's complex temporal, phenological, and climate dynamics, yet monitoring them is critical for ensuring food security. Synthetic Aperture Radar (SAR) satellites offer all-weather day-night imaging capability supporting key monitoring tasks including crop type mapping, yield prediction and phenological event detection. Existing multimodal remote sensing foundation models including TerraMind and CopernicusFM learn SAR represe...
  </details>

- **2026-08-11** — Zhuang Wang — [SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training](http://arxiv.org/abs/2608.11034v1)
  <details><summary>📄 Abstract</summary>
  In LLM pre-training, synchronization propagates rank-local stalls, slowdowns, and numerical errors into job-wide symptoms, obscuring their origin. Existing diagnosis often relies on in-process monitors that cannot report after the trainer blocks or terminates, or on post-mortem logs that preserve only synchronized symptoms; offline health tests lose the workload and operating conditions that triggered the failure. We present SCOUT, a unified runtime failure-localization framework built on one de...
  </details>

- **2026-08-11** — Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca et al. — [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](http://arxiv.org/abs/2608.10835v1)
  <details><summary>📄 Abstract</summary>
  Large Vision-Language Models (LVLMs) achieve impressive visual reasoning and dialogue capabilities, yet frequently hallucinate content unsupported by the visual input. Effective mitigation requires token-level localization, enabling targeted intervention without discarding the entire response. Existing detectors require expensive full-model fine-tuning, rely on external verifiers that ignore the model's generation process, or reduce internal signals to isolated features and hand-crafted statisti...
  </details>

- **2026-08-11** — Lancheng Gao, Ziheng Jia, Shengyan Li et al. — [E$^3$mo-Bench: A Scalable Benchmark for Multimodal Evoked and Expressed Emotion Understanding via Bayesian Pairwise Alignment](http://arxiv.org/abs/2608.10796v1)
  <details><summary>📄 Abstract</summary>
  Understanding both expressed and evoked emotions is critical for multimodal large language models (MLLMs) to achieve comprehensive affect-aware interactions. However, existing benchmarks typically examine expressed and evoked emotions in isolation or are constrained to coarse-grained and incomplete affective characterizations. To bridge this gap, we introduce E$^3$mo-Bench, a scalable benchmark comprising $12{,}314$ question-answer pairs across $2{,}524$ videos with predefined affective perspect...
  </details>

- **2026-08-11** — Ziyan Wang, Liwen Wu, Cheng Xie et al. — [ProTAGAD: A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes](http://arxiv.org/abs/2608.10699v1)
  <details><summary>📄 Abstract</summary>
  Text-Attributed Graphs (TAGs), endowed with abundant textual content along with topological structures, have emerged as a versatile backbone for real-world anomaly detection spanning large language model security, social network moderation, and cyber threat identification. Unlike conventional Graph Anomaly Detection (GAD), which relies primarily on structural irregularities, TAG anomaly detection must jointly leverage both topological patterns and fine-grained textual semantics to capture nuance...
  </details>

- **2026-08-11** — Jungang Li — [Classification of positive entire solutions of the CR Yamabe equation on the Heisenberg group](http://arxiv.org/abs/2608.10642v1)
  <details><summary>📄 Abstract</summary>
  We prove that, for every $n\ge 2$, every positive entire solution of the critical CR Yamabe equation $4Δ_b u = n^2 u^{(Q+2)/(Q-2)}$, $Q=2n+2$, on the Heisenberg group $\mathbb H^n$ is a Jerison-Lee bubble. No integrability, decay, boundedness, or symmetry is assumed. Together with the theorem of Catino, Li, Monticelli, and Roncoroni in $\mathbb H^1$, this classifies the positive entire solutions in every dimension.   Both Euclidean routes to such a statement lose their starting configuration her...
  </details>

- **2026-08-11** — Bingwen Huangfu, Jiani Guo, Shanshan Song et al. — [An Asynchronous Triggered MAC Protocol for Underwater Acoustic Networks](http://arxiv.org/abs/2608.10533v1)
  <details><summary>📄 Abstract</summary>
  Time Division Multiple Access (TDMA)-based Medium Access Control (MAC) protocols have proven their practicality through extensive field trials in Underwater Acoustic Networks (UANs), attributable to their hardware-agnostic and easily implementable properties. Most existing protocols rely on a synchronized and fixed-length slot paradigm to mitigate channel contention and facilitate orderly transmissions. However, this paradigm imposes significant clock synchronization overhead in UANs with low an...
  </details>

- **2026-08-11** — Aman Chauhan, Vishnu Pendyala — [Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy](http://arxiv.org/abs/2608.10532v1)
  <details><summary>📄 Abstract</summary>
  Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes. We ask whether a Large Language Model can replace the static routing policy itself, reading HAProxy and Prometheus telemetry every 10 seconds and isolating faulty servers through guardrailed calls to the HAProxy Data Plane API. On a reproducible benchmark with a persistent structural fault built int...
  </details>

- **2026-08-11** — Cong Chi Nguyen, Trang Mai Xuan, Vu-Duc Ngo et al. — [Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance](http://arxiv.org/abs/2608.10434v1)
  <details><summary>📄 Abstract</summary>
  Machine learning-based Intrusion Detection Systems (IDS) have demonstrated superior performance in securing Unmanned Aerial Vehicle (UAV) networks. However, the 'black-box' nature of these models, combined with the high dimensionality of multimodal cyber-physical data, poses significant interpretability challenges. Static visualization dashboards may struggle to present complex relationships among multimodal cyber-physical features in a form that is easy for operators to inspect and interpret. T...
  </details>

- **2026-08-11** — Sanidhya Vijayvargiya, Rahul Lokesh — [Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique](http://arxiv.org/abs/2608.10430v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) deployed as AI agents frequently exhibit user specification-grounding failures, executing hallucinated, undesired actions to force a resolution rather than expressing uncertainty. Existing detection methods fail to provide actionable, real-time correction as they either do not localize the hallucinations, or incur prohibitive inference latency. We introduce the Latent Critic, a lightweight low-rank adapter (LoRA) that operates concurrently with a frozen base LLM's ge...
  </details>

- **2026-08-11** — Hongrui Bao, Hangyu Rong, Zhuoshang Wang et al. — [EVIL-Detect for NLPCC 2026 Shared Task 6: LLM-Generated Text Detection](http://arxiv.org/abs/2608.10698v1)
  <details><summary>📄 Abstract</summary>
  The rapid development of large language models (LLMs) has increased the need for reliable detection of LLM-generated text, especially in realistic Chinese scenarios involving human-written text (HWT), LLM-generated text (LGT), and LLM-refined text (HLT). This paper presents EVIL-Detect, a multi-signal ensemble framework with conflict-aware fusion for NLPCC 2026 Shared Task 6. The system integrates edit-extent regression, zero-shot likelihood-contrast signals, lexical statistics, and conservative...
  </details>

- **2026-08-11** — Shuyu Jiang, Yue Ran, Kaiyu Xu et al. — [ASCon: A Direction-Aware Reciprocal Agent--Step Contextualization Model for Failure Attribution in Multi-Agent Systems](http://arxiv.org/abs/2608.10646v1)
  <details><summary>📄 Abstract</summary>
  Failure attribution in LLM-based multi-agent systems (MAS) aims to answer who caused failures, when they occurred, and why by identifying responsible targets including faulty agents, erroneous steps, and failure modes. Existing methods have primarily focused on developing dedicated models for specific attribution targets, with limited attention to the evidential dependencies among them. Despite these attribution targets are different, they rely on common diagnostic evidence from MAS trajectories...
  </details>

- **2026-08-11** — Yachun Shan, Feitian Zhang — [JitTrack: Onboard Multi-Object Tracking Against Viewpoint Jitter for Agile UAVs](http://arxiv.org/abs/2608.10485v1)
  <details><summary>📄 Abstract</summary>
  Multi-object tracking (MOT) onboard agile unmanned aerial vehicles (UAVs) remains challenging due to severe viewpoint jitter induced by camera ego-motion. Rapid attitude changes during flight often lead to significant target displacement across frames, causing inaccurate target association and degraded tracking performance. Existing UAV MOT methods are primarily evaluated on offline benchmarks and seldom address the practical requirements of real-world onboard deployment, including robustness to...
  </details>

- **2026-08-10** — Jie Cao, Qi Li, Zelin Zhang et al. — [MarkNull: Model-Agnostic Watermark Removal in AI-Generated Images via On-Manifold Latent Manipulation](http://arxiv.org/abs/2608.10166v1)
  <details><summary>📄 Abstract</summary>
  Digital watermarking has emerged as a critical technique for provenance and copyright attribution in AI-generated imagery, yet its robustness against realistic, model-agnostic removal attacks remains poorly explored. Existing attacks either succeed only against specific generative models or achieve removal at the cost of severe visual degradation. In this paper, we propose MarkNull, a model-agnostic watermark removal attack via on-manifold latent manipulation. MarkNull is grounded in a key obser...
  </details>

- **2026-08-10** — Alexander Schiøtz, Bertram Hage, Christian Rand et al. — [CRHT: A Continuous Regression Hybrid Transformer for Vessel Trajectory Prediction with Online Cluster Sampling](http://arxiv.org/abs/2608.10256v1)
  <details><summary>📄 Abstract</summary>
  Accurate vessel trajectory prediction is critical for maritime safety and anomaly detection, yet existing models often struggle with geographic bias and navigational realism. We propose the Continuous Regression Hybrid Transformer (CRHT), a deep learning framework designed to forecast vessel motion using Automatic Identification System (AIS) data. To mitigate spatial data imbalance, we introduce an online K-means cluster sampling strategy that ensures diverse exposure to rare maneuvers during tr...
  </details>

- **2026-08-10** — Chih Hui Wang, Mengdie Tu, Qianyun Zhang et al. — [Self-evolving Agentic Customer Support System at LinkedIn](http://arxiv.org/abs/2608.10224v1)
  <details><summary>📄 Abstract</summary>
  Enterprise support agents operate in rapidly changing environments where policies, product capabilities, and knowledge bases evolve continuously, making static assistants brittle and costly to maintain. We present LinkedIn's self-evolving agentic support system, which integrates retrieval-augmented generation with evolutionary auto-prompting and a modular, production-aligned evaluation framework to enable safe, continuous improvement without retraining foundation models. The system treats prompt...
  </details>

- **2026-08-10** — Srinivas Telukunta, Georgios Nektarios Lilis, Lucio Baron — [The CASE Framework: A Multi-Disciplinary Control Architecture for Governing Enterprise Agentic AI](http://arxiv.org/abs/2608.10153v1)
  <details><summary>📄 Abstract</summary>
  Enterprises are deploying autonomous AI agents faster than they can govern them, and prevailing approaches stretch a single discipline, typically DevSecOps built for deterministic automation, across every scale of agency. We argue that agentic AI governance is four problems, not one, each with a mature governing science. The CASE framework assigns Control theory to the individual agent (intent as setpoint, guardrails as feedback, evaluation as observation), complex Adaptive systems theory to age...
  </details>

- **2026-08-10** — Yilin Jiang, Xiaorong Zhu, Fei Tan et al. — [ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models](http://arxiv.org/abs/2608.09548v2)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in education as tutors, teaching assistants, and content generators. These roles place demands that ordinary question answering does not: a usable education-facing model is supposed to be accurate, safe under sensitive prompts, instructionally useful, and aligned with pedagogical goals at the same time. Existing benchmarks evaluate these requirements largely in isolation, so none assesses education-facing suitability as an integrated profile. We in...
  </details>

- **2026-08-10** — D M S Sultan, R. Plackett, A. E. McDougall et al. — [Automated Signal Integrity Analysis Framework for High-Speed Interconnects in the PPCB-1347-MuPix11 Probe Card](http://arxiv.org/abs/2608.09462v2)
  <details><summary>📄 Abstract</summary>
  A reusable MATLAB signal-integrity (SI) framework is presented that converts compatible four-port S-parameter data, measured by VNA or obtained from electromagnetic simulation, into traceable link-level evidence rather than a single loss metric. The framework is demonstrated on the four 1.25 Gbps differential routes (DP1-DP4) of the PPCB-1347/MuPix11 probe card using PTSL CST Microwave 3D-Solver-derived four-port S-parameters and a virtual time-domain solver. The automated pipeline preflights fi...
  </details>

- **2026-08-10** — Bin Zhang, Bowen Zheng, Chao Yi et al. — [DREAM Technical Report](http://arxiv.org/abs/2608.09408v2)
  <details><summary>📄 Abstract</summary>
  Industrial recommender systems commonly use cascaded retrieval, ranking, and re-ranking pipelines. Although efficient, these pipelines fragment information and objectives across modules, rely on rigid rules, and have limited awareness of real-time intent, leaving session-level shifts among browsing, comparison, and purchase insufficiently addressed. We present DREAM (Developing Recommender Engine with Agentic Methods), an autonomous optimization control architecture that adds a perception-aware,...
  </details>

- **2026-08-10** — Christopher M. Frost — [Withholding the Completing Chunk: Deterministic Pair-Completion Guardrails for Streaming LLM Output](http://arxiv.org/abs/2608.10279v1)
  <details><summary>📄 Abstract</summary>
  Streaming language-model output creates a release-timing problem: complete-response moderation acts after streamed text has escaped, whereas repeated semantic classification of partial text can be costly and unstable. We study a narrow deterministic construction in which each committed danger signature is the conjunction of two lexical predicates. The guard scans the accumulated prefix before every release and withholds the first chunk that makes both predicates observable. Across four signature...
  </details>

- **2026-08-10** — Han Zhang, Yilin Zhao, Zaid Pervaiz Bhat et al. — [From Detection to Understanding: TAR and TAR-Bench for Multi-Task Traffic Anomaly Reasoning](http://arxiv.org/abs/2608.10317v1)
  <details><summary>📄 Abstract</summary>
  We present TAR (Traffic Anomaly Reasoning) and TAR-Bench datasets, resources for training and evaluating video-language models beyond anomaly detection. TAR contains 44,040 chain-of-thought training annotations across 10 tasks for 3,670 CCTV videos ($\sim$26 hours) from eight public datasets. Its evaluation component, TAR-Bench, contains 960 human-curated test annotations for 80 held-out clips trimmed from 17 public YouTube videos. TAR's training annotations are produced with MAVEN, which consol...
  </details>

- **2026-08-10** — Adrien Schoen, Nachiketa Ratnakar Patil, Arjun Bhagoji et al. — [ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models](http://arxiv.org/abs/2608.10120v1)
  <details><summary>📄 Abstract</summary>
  Modern sequence models, from Transformers to State Space Models, have enabled powerful generative modeling across diverse domains, yet they are typically trained to predict what happens while treating when it happens as a secondary concern. In data-mining settings where events are associated with explicit timing information, this separation can limit temporal reasoning, anomaly detection, and faithful reconstruction of event chronology. A common strategy is to treat timing as an auxiliary signal...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 53 papers

- **2026-08-11** — Zitong Shan, Baichuan Lou, Yanxin Zhou et al. — [Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](http://arxiv.org/abs/2608.10618v1)
  <details><summary>📄 Abstract</summary>
  Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomous racing provides a stringent testbed by combining high-frequency localization and perception, adversarial interaction, near-saturated vehicl...
  </details>

- **2026-08-11** — Changhao Xiang, Shangyu Xing, Zhen Wu et al. — [MultiModal Code-Switching: Interleaving Visual Objects into Language for Explicit Object-Level Alignment](http://arxiv.org/abs/2608.11167v1)
  <details><summary>📄 Abstract</summary>
  Existing Multimodal Large Language Models (MLLMs) predominantly rely on image-text pairs for modality alignment pretraining, mapping global image representations to long textual descriptions. However, this image-level alignment suffers from referential ambiguity: models struggle to infer the correspondences between multiple visual objects and textual entities from the global representation, leading to data inefficiency and suboptimal semantic grounding. To address this, we propose MultiModal Cod...
  </details>

- **2026-08-11** — Mouxiao Huang, Qiangyu Yan, Borui Jiang et al. — [CapProbe: Evaluating Detailed Image Captions via Full-Scene Dense Question Answering](http://arxiv.org/abs/2608.11074v1)
  <details><summary>📄 Abstract</summary>
  Evaluating detailed image captions from Vision-Language Models (VLMs) requires going beyond surface-level semantic similarity. Reference-based metrics (e.g., CIDEr and SPICE) and LLM-as-scorer protocols struggle to verify dense factual claims, while existing QA-based alternatives generally offer lower probe density, narrower domain coverage, or no explicit alignment between individual questions and segmented image regions. We introduce CapProbe, a full-scene dense QA benchmark that turns detaile...
  </details>

- **2026-08-11** — Dong Qiao, Chris Ding, Jicong Fan — [Mapping and Measuring the Behavioral Evolution of Large Language Models](http://arxiv.org/abs/2608.11027v1)
  <details><summary>📄 Abstract</summary>
  Benchmark leaderboards summarize how well a language model performs, but not how its behavior relates to that of other models or changes across generations. We characterize the output behavior of 32 models from six families using their responses to a shared bank of 10{,}000 prompts. After embedding each response, we construct three complementary sentence-level dissimilarities: an aligned mean per-prompt distance, which is a pseudometric on observed model responses; a PCA-compressed summary of pr...
  </details>

- **2026-08-11** — Liangyu Fu, Junbo Wang, Yuke Li et al. — [Watching Synthetic Videos: Aligning Cross-modal Representations with Visual Synthesis for Zero-shot Video Captioning](http://arxiv.org/abs/2608.11013v1)
  <details><summary>📄 Abstract</summary>
  Text-only training is a popular paradigm in zero-shot video captioning, where the video distribution is not available to the model during training, leading to a cross-modal gap between the training (text-only) and the inference (video-only). Previous works attempt to bridge the gap through simple linear transformations. However, the inherent gap between text and video makes cross-modal representation space alignment insufficient, resulting in inaccurate sentences. To address this issue, we propo...
  </details>

- **2026-08-11** — Seonguk Ju, Seola Cho, Sooin Chung et al. — [Pitch Contour Tokenization using VQ-VAE and Its Application on Korean Traditional Music Analysis](http://arxiv.org/abs/2608.10979v1)
  <details><summary>📄 Abstract</summary>
  Computational analysis of music often relies on discrete representations, yet many musical traditions are organized around continuous pitch movement that resists segmentation into note-like units. For such traditions, the discrete units that analysis would build on are not given in advance. We address this gap by learning a vocabulary of local pitch-contour patterns directly from unlabeled audio, using a VQ-VAE that quantizes fixed-length contour segments into a finite codebook. To make the lear...
  </details>

- **2026-08-11** — Zhaoyang Wei, Bowen Jiang, Xumeng Han et al. — [Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes](http://arxiv.org/abs/2608.10954v1)
  <details><summary>📄 Abstract</summary>
  While Multimodal Large Language Models (MLLMs) demonstrate impressive performance in benign scenarios, their cognitive reliability deteriorates significantly in complex scenes under adverse conditions. In these settings, models often rely on implicit inference without sufficient visual evidence, leading to a disconnect between perception and reasoning. Meanwhile, existing outcome-oriented benchmarks evaluate only final predictions and fail to diagnose failures in the underlying reasoning process...
  </details>

- **2026-08-11** — Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim et al. — [Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models](http://arxiv.org/abs/2608.10864v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have achieved strong image and video understanding, yet their visual-spatial representations remain geometrically fragile, leading to failures in spatial reasoning needed for embodied AI, robotics, and autonomous driving. Prior approaches to geometry grounding either fine-tune VLMs on spatial question answering, which can perpetuate spurious visual representations, or fuse features from large geometry-grounded vision models, which substantially increases model size ...
  </details>

- **2026-08-11** — Maryam Masoumi, Amir Kargaran, Reza Jafari — [Impact of Higher-Order Interactions on Collective Motion](http://arxiv.org/abs/2608.10844v1)
  <details><summary>📄 Abstract</summary>
  Collective motion in self-propelled particle systems has been widely studied using the Vicsek model, which relies on pairwise alignment interactions. We introduce a generalized Vicsek model that incorporates higher-order (triadic) alignment interactions. Using agent-based simulations and mean-field theory, we demonstrate that pure triadic alignment induces a discontinuous phase transition, evidenced by hysteresis, a double-well free-energy landscape, and a Binder cumulant minimum that deepens wi...
  </details>

- **2026-08-11** — Rajmund Nagy, Silvia Arellano García, Hendric Voss et al. — [The GENEA Challenge 2026: A Large-Scale Disentangled Evaluation of Speech-Driven Gesture Generation on the Seamless Interaction Dataset](http://arxiv.org/abs/2608.10839v1)
  <details><summary>📄 Abstract</summary>
  This preprint presents the results of the fourth GENEA Challenge, a large-scale human evaluation of five speech-driven gesture-generation systems trained by participating teams on the Seamless Interaction dataset of dyadic conversations. As in the 2023 GENEA Challenge, we used a disentangled evaluation methodology to assess motion quality and speech alignment without confounding between the two, and performed a dyadic mismatching study to isolate the effect of listening and reacting to the inter...
  </details>

- **2026-08-11** — Anton François, Rayane Mouhli, Thomas Pierron — [A Framework for Joint Affine and Diffeomorphic Image Registration](http://arxiv.org/abs/2608.10769v1)
  <details><summary>📄 Abstract</summary>
  Anatomical image registration commonly relies on a sequential pipeline where an affine alignment is estimated first and then held fixed while a non-rigid diffeomorphic deformation is applied. This two-step process often leads to suboptimal results, as the initial stage can absorb local deformations, biasing the residual passed to the diffeomorphic registration. To address this, we introduce a Joint Affine-Diffeomorphic framework, based on the large deformations model, that estimates both global ...
  </details>

- **2026-08-11** — Yuan Wang, Hualiang Wang, Yixin Chen et al. — [MedUP: Awakening Unified Understanding and Perception in Medical Vision-Language Models](http://arxiv.org/abs/2608.10635v1)
  <details><summary>📄 Abstract</summary>
  Medical Vision-Language Models (Med-VLMs) excel at verbalizing visual content, yet precise visual perception, segmentation, and grounding remain challenging. Existing approaches either verbalize regions as coordinate strings or rely on external modules that decouple perception from understanding, creating representation gaps for region-language alignment. We present MedUP, a Med-VLM that natively unifies perception and understanding within a shared token space. At its core lies UniMedTok, a regi...
  </details>

- **2026-08-11** — Rose Niousha, Minwoo Kang, Narges Norouzi — [INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators](http://arxiv.org/abs/2608.10492v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based simulators often reproduce observable actions but fail to capture the underlying reasoning behind them. In education, where student simulation is increasingly used for various applications such as evaluating tutoring systems, this gap is especially pronounced. Two students may submit identical submissions for entirely different reasons. We present INTERNAL STUDENT DIALOGUE (INSIDE), a student modeling framework that fine-tunes LLMs not only to act like students b...
  </details>

- **2026-08-11** — Layla Araiinejad, Vineet Jagadeesan Nair — [Nuclear fusion for AI: A pathway to power data centers sustainably](http://arxiv.org/abs/2608.10454v1)
  <details><summary>📄 Abstract</summary>
  This perspective examines whether nuclear fusion can provide a scalable, low-carbon power source for rapidly growing AI-driven data center demand. As large language models, cloud computing, and cryptocurrency mining accelerate electricity consumption growth, data centers are projected to account for a substantially larger share of U.S. and global electricity use in the coming decades, creating significant pressure on grid reliability and decarbonization goals. We evaluate the technical and econo...
  </details>

- **2026-08-11** — Tianjiao Nie, Ao Zhang, Yusen Tang et al. — [FormaTheoria: Constructing Large-Scale Lean Theories from Mathematical Literature $-$ Toward the Formalization of the Classification of Finite Simple Groups](http://arxiv.org/abs/2608.10894v1)
  <details><summary>📄 Abstract</summary>
  Large-scale formalization of advanced mathematics requires more than translating individual statements: it must reconstruct a coherent theory distributed across heterogeneous sources. This process raises four challenges: discovering implicit dependencies, correcting source defects, preserving semantic fidelity, and reconciling cross-source misalignments. We present FormaTheoria, an end-to-end, AI-assisted workflow that coordinates source acquisition, formalization, proof construction, recursive ...
  </details>

- **2026-08-11** — Simon Geirnaert, Alexander Bertrand, Tom Francart et al. — [Modeling and Interpreting Correlations, Null Distributions and Significance Levels in Neural Tracking of Natural Stimuli](http://arxiv.org/abs/2608.10887v1)
  <details><summary>📄 Abstract</summary>
  Neural tracking - the time-locking of neural responses to continuous stimuli such as speech, music, and video - is widely used to study how the brain processes natural input. Tracking strength is typically quantified as the correlation between the recorded neural response and the stimulus, decoded and/or encoded through data-driven models, and this correlation is routinely used to compare stimulus features, models, or settings. However, its magnitude depends not only on how strongly the brain tr...
  </details>

- **2026-08-10** — Yushun Tang, Yisen Cao, Zhicheng Chen et al. — [Entropy-based Code Adversarial Translation for Real-world Repository Migration](http://arxiv.org/abs/2608.09273v2)
  <details><summary>📄 Abstract</summary>
  LLMs have demonstrated strong capabilities in code generation and automated program repair, but migrating an entire repository rarely produces a runnable application because long-horizon translation challenges LLM-based agents' ability to maintain repository-level migration objectives. In this work, we propose Entropy-based Code Adversarial Translation (ECAT), a multi-agent framework for automated Android-to-HarmonyOS repository migration. ECAT formulates repository migration as adversarial entr...
  </details>

- **2026-08-10** — Alvin Spivey, Thomas Huang — [Logit-Boundary Geometric Belief Interfaces and Sparse Sheaf-Enclave Protocols: A Self-Contained Substrate for Secure Network Electronic Health Record (EHR) Interoperability](http://arxiv.org/abs/2608.10300v1)
  <details><summary>📄 Abstract</summary>
  Electronic health-record interoperability is a boundary problem: legacy systems, generative models, terminology services, identity systems, and human reviewers may each expose rich internal states, while operational exchange requires a narrow shared interface of typed claims, bounded uncertainty, provenance, and explicit admission or abstention. This paper details a mathematical and engineering architecture for that interface. The organizing idea is the logit boundary: a discovery model may prop...
  </details>

- **2026-08-10** — Francisco León Zúñiga Bolívar — [Not a Monolith: Lab-Level Divergence in the Cooperative Equilibria of Chinese Frontier LLM Agents](http://arxiv.org/abs/2608.10262v1)
  <details><summary>📄 Abstract</summary>
  Does the cooperative bias documented for Western frontier LLM agents extend to a different alignment lineage, and should the Chinese models that embody it be treated as a single bloc or as distinct laboratories? We study four frontier-tier Chinese models - DeepSeek V4 Pro, Qwen3-Max, Kimi K2.5 and GLM-5.1 - in an evolutionary Iterated Prisoner's Dilemma, under a design that removes a confound present in prior work. Rather than letting each model convert its own natural-language strategies into c...
  </details>

- **2026-08-10** — Alec Harris, Kasey Corra, Archie Chaudhury et al. — [Evaluation-Conditioned Training: Teaching Models to Generalize to Stronger Oversight Regimes](http://arxiv.org/abs/2608.10209v1)
  <details><summary>📄 Abstract</summary>
  Feedback signals used to train Large Language Models (LLMs) are the primary driver of their behavior and our main lever for instilling alignment with human values and objectives. However, a key limitation of current post-training methods is the inability of human annotators and automated reward functions to faithfully capture the feedback we would like to give. We introduce Evaluation-Conditioned Training (ECT), a post-training framework that uses natural language to condition each training samp...
  </details>

- **2026-08-10** — Sudhanva Manjunath Athreya, Sai Phani Kumar Malladi — [More Accurate, Less Human: Gestalt Grouping in Vision Models](http://arxiv.org/abs/2608.10195v1)
  <details><summary>📄 Abstract</summary>
  Human vision organizes what it sees into wholes: same-colored points group into series, similar marks cohere into categories, and shapes complete into recognizable objects. These are the Gestalt operations that visualization design builds on. Whether vision models organize visual content this way has not been systematically tested. We introduce a behavioral battery that scores models against human data from prior perception studies on four grouping tasks: mark-color odd-one-out, color-series cou...
  </details>

- **2026-08-10** — Vivek Kulkarni, Sudipta Paul, Aounon Kumar et al. — [SBCO: Self-Supervised, Verifier-Grounded Harness Optimization For Planning Agents](http://arxiv.org/abs/2608.10157v1)
  <details><summary>📄 Abstract</summary>
  Self-improving agents seek to reduce the human engineering effort behind AI systems by enabling them to evolve and self-improve their performance over time. Recently, methods like the Darwin Gödel Machine and the Huxley Gödel Machine have been proposed which enable open-ended, recursive self-improvement through self-reference where a coding agent edits its own code. Such self-referential self-improvement methods require that the competence required to perform the task coincides or aligns well wi...
  </details>

- **2026-08-10** — M P V S Gopinadh, Karthik Kamuju, Kummari Avinash et al. — [Procedural Fairness Failures in RLHF from Preference Averaging](http://arxiv.org/abs/2608.10126v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning from Human Feedback (RLHF) aggregates heterogeneous preferences into a single reward model, assuming preference homogeneity. When preferences are heterogeneous, this aggregation induces a procedural fairness failure where majority preference groups dominate reward learning while minority preferences are systematically under-represented. This work defines procedural fairness in alignment as preserving distinct preference signals during reward modeling and shows that standar...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 75 papers

- **2026-08-11** — Alicia Larsen, Victoire Laurent, Aulia Kharis Rakhamsari et al. — [V-FiLLM: Verified Financial LLM Reasoning Benchmark](http://arxiv.org/abs/2608.11047v1)
  <details><summary>📄 Abstract</summary>
  While existing benchmarks have made substantial progress in evaluating LLMs across STEM domains, financial reasoning over structured data remains comparatively less explored. We introduce V-FiLLM, a framework that generates financial reasoning benchmarks from executable computation trees grounded in real tables, yielding items whose answers are correct by construction. Trees are evaluated symbolically to obtain ground truth and rendered into natural-language questions, removing any model from th...
  </details>

- **2026-08-11** — Sofia Avdiiv, Andre Weiner, Ben Steinfurth — [Deep reinforcement learning for separation control in turbulent wind-tunnel flow](http://arxiv.org/abs/2608.10829v1)
  <details><summary>📄 Abstract</summary>
  This work investigates Deep Reinforcement Learning (DRL) as a tool for model-free closed-loop active separation control in a fully turbulent wind tunnel flow over a one-sided diffuser. The agent controls an array of magnetic valves (on/off) that eject compressed air into the boundary layer, while the environmental state is reduced to the signal from a single wall-shear-stress sensor placed near the natural transitory detachment point. The control law is learned in real time using Proximal Policy...
  </details>

- **2026-08-11** — Pooja Yadav, Priyanka Harjule, Basant Agarwal et al. — [Assessing Reliability of BERT-Based Models on Question Answering Tasks](http://arxiv.org/abs/2608.10806v1)
  <details><summary>📄 Abstract</summary>
  Reliability estimation of large language models is in many cases as crucial as their accuracy, as reliable models are more trustworthy, robust, and suitable for practical applications. Recent advancements in natural language processing (NLP), particularly those based on transformer architectures, have significantly accelerated progress across various NLP tasks. This study focuses on the reliability of transformer-based question answering (QA) models, specifically BERT models and its variants (Ro...
  </details>

- **2026-08-11** — Fufangchen Zhao, Jinhu Fu, Jiachen Lei et al. — [FADE: From Passive Verification to Active Discovery in Counterfactual Video Understanding](http://arxiv.org/abs/2608.10764v1)
  <details><summary>📄 Abstract</summary>
  Counterfactual video understanding evaluates whether models grasp physical and commonsense regularities. However, existing multiple-choice question (MCQ) benchmarks inadvertently leak target events through their questions and candidate options. This reduces the core challenge from active discovery to text-guided verification. In this paper, we present FADE, an effective training framework for counterfactual discovery and explanation. Our method is built on an evidence-first, two-stage training p...
  </details>

- **2026-08-11** — Uma Ranjan, Kunal Tilaganji, Aditya Koul et al. — [Rethinking LLM Verification: Evidence Structure, Uncertainty, and Selective Refinement](http://arxiv.org/abs/2608.10725v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often rely on shortcuts rather than systematic reasoning, raising safety concerns in medical applications. Allowing models to abstain when uncertain improves reliability but introduces a coverage accuracy tradeoff. We propose a two-stage framework for medical hypothesis verification in multiple-choice settings that manages this tradeoff through targeted ontology grounding, applied only when the model abstains. We show that abstention is not random but reflects genuin...
  </details>

- **2026-08-11** — Guangrui Shen, Zhili He, Shigang Wang et al. — [TCAM for Autonomous Deformable Manipulation: The RMC2 Champion System for WBCD 2026 Track 4](http://arxiv.org/abs/2608.10718v1)
  <details><summary>📄 Abstract</summary>
  This technical report describes the RMC2 Team's champion solution for the WBCD 2026 Track 4: Deformable Manipulation Challenge. The task requires a robot to pick a single T-shirt from a stack, load it onto a printing pallet, align the collar with a target area, and smooth the printing region, a sequence that involves single-layer separation, deformable transport, precise placement, and contact-rich surface adjustment. The competition strongly incentivizes fully autonomous execution, motivating t...
  </details>

- **2026-08-11** — Masoud Shokrnezhad, Tarik Taleb — [Conversational Orchestration for Organic 6G](http://arxiv.org/abs/2608.10714v1)
  <details><summary>📄 Abstract</summary>
  The Organic 6G vision of a network of networks spanning an edge-cloud continuum complemented by non-terrestrial resources requires, to realize its promise, service provisioning that is simple to operate, scalable across independently administered domains, and agile under domain churn (i.e., domains dynamically joining and leaving). Despite advances in cross-domain orchestration, many proposals rely on heavy integration fabrics, multi-layer coordinators, and deep telemetry pipelines that hinder d...
  </details>

- **2026-08-11** — Zefeng Liang, Jie Qiao, Ruichu Cai et al. — [IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning](http://arxiv.org/abs/2608.10634v1)
  <details><summary>📄 Abstract</summary>
  Model-based reinforcement learning (MBRL), which learns environment dynamics to generate synthetic experience, is a promising approach to sample-efficient decision making. Numerous methods have been developed to improve dynamics prediction and policy optimization for MBRL through uncertainty estimation, model regularization, and conservative value learning. However, these methods typically treat the transition model and critic as monolithic predictors, overlooking the policy-induced data bias. C...
  </details>

- **2026-08-11** — Shuang Sun, Jafar Akhoundali, Arina Kudriavtseva et al. — [A Study of Cursorrules Files in GitHub Open Source Projects](http://arxiv.org/abs/2608.10622v1)
  <details><summary>📄 Abstract</summary>
  Prompts are the primary mechanism for communicating with AI agents, and they directly influence the quality and reliability of AI-generated code. As AI-assisted programming becomes widely adopted, modern tools increasingly combine dynamic conversational prompts with static configuration-like prompt files. Despite the growing focus on prompt engineering, prior research has primarily focused on conversational prompts, while prompt files remain understudied.   To address this gap, we conduct an emp...
  </details>

- **2026-08-11** — Si'an Xie, Jiaxun Liu, Biao Yang et al. — [From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models](http://arxiv.org/abs/2608.10444v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have made substantial progress on reasoning tasks that require increasingly long and complex inferential chains. This progress primarily reflects reasoning depth. A complementary and comparatively unexamined capability is reasoning breadth: exploring multiple semantic directions in parallel and integrating the resulting clues into one coherent answer. We introduce MPAR-Bench, a bilingual English-Chinese benchmark that isolates reasoning breadth through multi-point as...
  </details>

- **2026-08-11** — Songlin Du, Xiaoyong Lu, Zeyu Wu et al. — [Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives](http://arxiv.org/abs/2608.11093v1)
  <details><summary>📄 Abstract</summary>
  Cross-view feature matching aims to establish reliable correspondences across images with large viewpoint variations. Over the past decade, the field has evolved from task-specific models toward increasingly unified and generalizable correspondence models, with recent progress further driven by the emergence of vision foundation models (VFMs). Despite these advances, existing studies remain highly diverse in their problem formulations, model architectures, training paradigms, and evaluation prot...
  </details>

- **2026-08-11** — Ye Kyaw Thu, Ye Bhone Lin, Thura Aung et al. — [myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR](http://arxiv.org/abs/2608.11036v1)
  <details><summary>📄 Abstract</summary>
  Although Whisper models benefit from large-scale multilingual pre-training, their performance on Burmese medical speech remains limited. This work presents a Burmese medical speech recognition framework built on a high-quality 28-hour corpus recorded and validated by native speakers. We fine-tune Whisper models using full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) with LoRA. To evaluate robustness, we apply waveform- and spectrogram-level data augmentation under controlled nois...
  </details>

- **2026-08-11** — Yufei Zhang, Chenlu Zhan, Hongwei Wang — [When Visual Signals Mislead: A Mechanistic Study of Attribute Hallucination in Vision-Language Models](http://arxiv.org/abs/2608.11024v1)
  <details><summary>📄 Abstract</summary>
  Attribute hallucination---where vision-language models (VLMs) correctly identify an object but mischaracterize its properties---is prevalent yet mechanistically poorly understood. The dominant explanation, language-prior dominance, has motivated prior-suppression methods, but this explanation has not been directly tested at the attribute level. We present VISOR (Visual-Operational Remediation), a unified framework that couples null-image-based diagnosis with routed remediation. Its VSNR diagnost...
  </details>

- **2026-08-11** — Roni Blushtein-Livnon, Tal Svoray, Osher Rafaeli et al. — [Evaluating Semantic and Spatial Guidance for Foundation Model Segmentation of Small-Scale PV in Remote Sensing Imagery](http://arxiv.org/abs/2608.10801v1)
  <details><summary>📄 Abstract</summary>
  Spatio-temporal PV data are essential for understanding adoption processes in off-grid regions, yet such data remain largely unavailable. Automated segmentation of remote sensing (RS) imagery offers a promising solution; yet, residential PV systems remain challenging targets because of their small size and sparse distribution, resulting in severe target-background imbalance. Vision-language foundation models (FMs) provide a data-efficient paradigm through prompt-based semantic and spatial guidan...
  </details>

- **2026-08-11** — Hamza Ouarrad, Mohammad Abboush, Andreas Rausch — [LLM Ensemble Fault Classification for Automotive HiL Validation](http://arxiv.org/abs/2608.10710v1)
  <details><summary>📄 Abstract</summary>
  Automotive HiL validation generates large multivariate test recordings whose analysis remains challenging due to manual review effort, rule-based limitations, and the need for explainable diagnostic decisions. Recent machine-learning and deep-learning approaches have improved fault diagnosis, but they often require large labelled datasets, generalise poorly across operating conditions, and provide limited insight into their predictions. This paper proposes an explainable multi-LLM ensemble frame...
  </details>

- **2026-08-11** — Rohit Sinha, Kunal Tilaganji, Tanuja Ganu et al. — [VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus](http://arxiv.org/abs/2608.10665v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models often generate reasoning chains containing subtle errors that lead to incorrect answers. Current verification approaches have notable limitations. Existing approaches either require expensive labelled supervision with inconsistent cross-task performance or aggregate scores from multiple sources by simple aggregations, missing a key insight: when these scores disagree, that disagreement itself carries important information about whether a reasoning step is truly v...
  </details>

- **2026-08-11** — Jiaping Wang, Shaobo Li, Zhen Wang — [Cross-View Sequential Visual Localization with Spatio-Temporal Context Modeling for Autonomous Driving](http://arxiv.org/abs/2608.10660v1)
  <details><summary>📄 Abstract</summary>
  Continuous and reliable localization is essential for autonomous driving. Cross-view visual localization matches ground images with satellite maps, providing complementary localization cues for pipelines that depend on Global Navigation Satellite System (GNSS) signals and high-definition (HD) maps. Most existing cross-view visual localization methods process each frame independently, leaving temporal information underused and limiting accuracy under dynamic occlusion, illumination variation, and...
  </details>

- **2026-08-11** — Carlos Zamora, Hiram Zuniga, Ulises Orozco-Rosas et al. — [Retrieval-Augmented Vision Foundation Models for Robust Leukemia Cell Classification across Multiple Microscopy Datasets](http://arxiv.org/abs/2608.10657v1)
  <details><summary>📄 Abstract</summary>
  Leukemia cell image classification is challenged by real-world domain shifts from acquisition, staining, illumination, and site protocols, causing single-dataset models to generalize poorly in real clinical scenarios. This work presents a robust framework for leukemia classification across multiple heterogeneous datasets using a two-stage pipeline with a pretrained vision foundation model. Stage 1 performs binary classification (leukemia vs. non-leukemia) and is trained using 122,167 single-cell...
  </details>

- **2026-08-11** — Utshab Kumar Ghosh, Shubham Chatterjee — [When Do Anchor-Based Pointwise LLM Rerankers Help? Retriever Quality, Statistical Scope, and Anchor Design](http://arxiv.org/abs/2608.10528v1)
  <details><summary>📄 Abstract</summary>
  Anchor-based pointwise LLM reranking scores each candidate against a shared reference passage to recover cross-document context at pointwise cost. We study when this actually helps, using GCCP/PAGC as a representative method. Our study is reproduction-first. We use reproduction as a starting point for a controlled component-level stress test of anchor-based pointwise reranking. Our initial reimplementation, based only on the paper text, achieves 0.24 nDCG@10 instead of the reported 0.66, reveali...
  </details>

- **2026-08-11** — Daphne Feng, Ricardo Parada, Lily Jiang et al. — [Robust Multi-Agent Bandits with Heavy-Tailed Rewards and Information Asymmetry](http://arxiv.org/abs/2608.10529v1)
  <details><summary>📄 Abstract</summary>
  The multi-armed bandit problem is a central framework in sequential decision-making, extensively studied under sub-Gaussian reward assumptions. However, real-world applications often involve heavy-tailed reward distributions and decentralized, information-asymmetric interactions. We study multi-agent multi-armed bandits with heavy-tailed rewards under three information-asymmetry regimes: unobserved actions with common rewards, observed actions with independent rewards, and unobserved actions wit...
  </details>

- **2026-08-11** — Yingsheng Liu, Haiming Li, Jingmin Zhu et al. — [Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training](http://arxiv.org/abs/2608.10522v1)
  <details><summary>📄 Abstract</summary>
  While vision-language models dominate medical representation learning, unstructured text lacks the dense, quantitative diagnostic phenotypes inherent in structured clinical tables. However, existing multimodal pre-training methods underutilize this potential due to semantic-agnostic designs that treat tabular inputs as flat vectors and employ unstable continuous regression objectives. To overcome this, we propose a novel semantic-aware framework explicitly modeling the intrinsic two-dimensional ...
  </details>

- **2026-08-11** — Xiaoxuan Gao, Rentao Gu, Yingchun Wang et al. — [Link-adaptive digital twin for robust physical-layer modeling in hybrid-amplified ultra-wideband optical networks](http://arxiv.org/abs/2608.10517v1)
  <details><summary>📄 Abstract</summary>
  Accurate physical-layer modeling is increasingly essential for reliable ultra-wideband operation and capacity optimization, especially under the intensified inter-channel stimulated Raman scattering (ISRS) effect. This paper proposes the link-adaptive digital twin (LA-DT) for hybrid-amplified ultra-wideband links to overcome the generalization and speed limitations of existing methods, achieving accurate modeling and robust generalized signal-to-noise ratio (GSNR) estimation across diverse links...
  </details>

- **2026-08-11** — Lujie Ban, Jiangtao Zhu, Yuanheng Yu et al. — [FormStruct-Bench:A Hierarchical and Diagnostic Benchmark for Table-Form Document Structure Recognition](http://arxiv.org/abs/2608.10396v1)
  <details><summary>📄 Abstract</summary>
  Transforming table-form documents into machine-processable records requires recovering not only their visible content but also the multilevel structure that organizes it. However, existing benchmarks evaluate either holistic document outputs or conventional table grids, and their aggregate scores provide little insight into where structural failures occur. We introduce FormStruct-Bench, a hierarchical and diagnostic benchmark that evaluates table-form document structure recognition at both the d...
  </details>

- **2026-08-11** — Samaneh Mohtadi, Pietro Bernardelle, Joel Mackenzie et al. — [Persona Conditioning as an Assessor-Sensitivity Probe for LLM-Based IR Evaluation](http://arxiv.org/abs/2608.10385v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as relevance assessors in information retrieval (IR) evaluation, raising questions about how assessor framing affects judgment reliability and downstream system comparison. We study persona conditioning as a diagnostic mechanism for exposing LLM assessor sensitivity. Using task-oriented personas drawn from two complementary sources (PersonaHub and NVIDIA Nemotron-Personas-USA), we instantiate five assessor roles emphasizing intent interpretation...
  </details>

- **2026-08-10** — Qing Zong, Jiayu Liu, Junhao Shen et al. — [Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design](http://arxiv.org/abs/2608.10299v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems are increasingly expected to improve after deployment, yet single-entity self-evolution is often bounded by a static learning context, such as fixed tasks and feedback. This survey focuses on co-evolution in agentic systems, a multi-component form of self-evolution in which multiple agents and their environment impose adaptive pressure on one another. To organize existing papers, we propose a progressive three-stage taxonomy that traces how the system gradually sheds human-engine...
  </details>

- **2026-08-10** — Kaustubh Shivshankar Shejole, Tanish Agarwal, Arpit Agarwal et al. — [Finding the Signal in the Spam: Jointly Learning Rewards and Worker Reliability from Pairwise Comparisons](http://arxiv.org/abs/2608.10045v1)
  <details><summary>📄 Abstract</summary>
  The problem of learning from pairwise comparisons has been widely studied across many domains such as recommendation systems, social choice, and more recently, fine-tuning large language models. In this problem, the goal is to learn item rewards based on pairwise comparisons between them. In many scenarios, these comparisons are elicited from crowdworkers using platforms such as Amazon Mechanical Turk, Scale AI, etc. However, crowdworkers are often unreliable due to limited domain knowledge or r...
  </details>

- **2026-08-10** — Nusrat Jahan Mozumder, Divya Gopinath, Corina Pasareanu et al. — [SeFaR: Semantic Feature-aware Robustness Testing of Deep Neural Networks](http://arxiv.org/abs/2608.10289v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are increasingly deployed in safety-critical domains as perception modules, where failures are often caused due to rare and under-represented scenarios. This necessitates the need to evaluate the semantic robustness of perception models; conformance of behavior to high-level requirements over real-world perceptual variability. To address this, we propose SeFaR, a framework for systematic semantic-feature-centric testing of vision models. Given a natural-language requirement ...
  </details>

- **2026-08-10** — Touseef Hasan, Laila Cure, Souvika Sarkar — [TRACE: Trustworthy Retrieval-Augmented Conversational Engine](http://arxiv.org/abs/2608.10176v1)
  <details><summary>📄 Abstract</summary>
  Public service chatbots are expected to deliver recommendations from an underlying public service directory, while also making sure that the recommendations respect explicit user constraints. In practice, public service directories are noisy and inconsistent, and general-purpose large language model (LLM) or AI-based chatbots frequently generate unreliable recommendations, citing unverified sources from the web. We investigate the impact of retrieval quality on constraint-aware recommendation in...
  </details>

- **2026-08-10** — Selani A. Indrapala, Wageesha N. Manamperi — [BiTSE: Binaural Target Speaker Extraction in Noisy Multi-Talker Environments for AR Glass Arrays](http://arxiv.org/abs/2608.10106v1)
  <details><summary>📄 Abstract</summary>
  Isolating a desired speech signal in noisy multi-talker conversational scenarios is a key requirement for augmented reality (AR) wearable microphone array systems. In this work, a binaural target speaker extraction (TSE) framework, termed BiTSE, is proposed. It leverages both spatial and temporal cues, specifically the direction-of-arrival (DoA) of the target speaker and corresponding voice activity information, to guide the extraction process. Built upon a binaural signal denoising architecture...
  </details>

- **2026-08-10** — Lisheng Huang, Chen Yang, Hao Zhou et al. — [Evo-Bench: Can Language Models Improve Agent Harness?](http://arxiv.org/abs/2608.09096v2)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have driven rapid progress in autonomous agents, yet standard evaluations remain confined to static task solving. An emerging frontier is harness evolution---the agent's capacity to autonomously optimize its own operating harness. However, systematically benchmarking this capability remains challenging, as existing evaluations fail to isolate harness improvements from base model strength, prevent task-specific overfitting, or capture long-horizon iterative research. ...
  </details>

- **2026-08-10** — Hongyi Pan, Gorkem Durak, Halil Ertugrul Aktas et al. — [BreastMammo and DenseMammo: Benchmarks for Mammography Domain Generalization](http://arxiv.org/abs/2608.10271v1)
  <details><summary>📄 Abstract</summary>
  Breast density classification is a critical component of breast cancer risk assessment, yet AI models often struggle to generalize across clinical sites due to vendor-specific acquisition styles. In this work, we introduce two new datasets, BreastMammo and DenseMammo, to facilitate robust multi-view mammography research. We propose a domain generalization framework that utilizes a foreground-only histogram matching protocol to resolve the domain shift issue arising from disparate clinical source...
  </details>

- **2026-08-10** — Savannah Thais, Wm. Matthew Kennedy, Abhigyan Acherjee et al. — [Toward Human Rights Benchmarking for LLMs: A Pilot Methodology](http://arxiv.org/abs/2608.10268v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly mediate legal determinations over what human rights are realized, and how. Yet, no evaluation benchmark exists to assess whether they can reason correctly about human rights law. To this end, we report our efforts to develop a robust and scalable methodology for creating HumRightsBench: the first expert-validated, scenario-based benchmark for evaluating reasoning grounded in the obligation structure of international human rights law. We adapt the IRAC fr...
  </details>

- **2026-08-10** — Jun Huang, Meiyi Chen, Zijie Yue et al. — [Bootstrapping Vision-Language Model for Hysteroscopic Surgical Scene Segmentation](http://arxiv.org/abs/2608.09302v2)
  <details><summary>📄 Abstract</summary>
  Hysteroscopic surgical scene segmentation plays a pivotal role in understanding the hysteroscopic intraoperative environment as well as computer-assisted intervention. However, this task presents unique challenges due to the high morphological similarity among different lesions and the presence of artifacts such as specular reflections, motion blur, and fluid occlusions in surgical videos. In this work, we propose the first vision-language model (VLM)-based hysteroscopic surgical scene segmentat...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 21 papers

- **2026-08-11** — Yiqi Wang, Zihao Yan, Jiaqi Zhang et al. — [MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows](http://arxiv.org/abs/2608.10509v1)
  <details><summary>📄 Abstract</summary>
  Shared memory helps language-model agents reuse information across long workflows, yet relevant evidence may not be admissible for a particular agent or action. Because restrictions propagate through derivations, summaries can conceal private, poisoned, untrusted, or revoked sources, enabling unauthorized reads or unsafe actions. Existing approaches provide semantic retrieval, scoped access, or lineage tracking, but do not clearly separate hard authorization from graded trust or adapt evidence r...
  </details>

- **2026-08-11** — Audrey Quessada-Vial — [Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems](http://arxiv.org/abs/2608.11166v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems are increasingly composed of heterogeneous agents, prompts, tools, models, skills, composite subsystems, policies, and execution workflows whose configurations evolve across frameworks and runtime environments. Existing LLMOps and AgentOps platforms support orchestration and observability but do not provide a common configuration-governance model for representing and governing these systems as coherent, versioned configurations.   This paper introduces Agentic Configuration Manag...
  </details>

- **2026-08-11** — Francesco Musicco, Danilo Danese, Giuseppe Fasano et al. — [Who Are You Explaining To? A Multi-Agent System for Audience-Aware XAI Narratives](http://arxiv.org/abs/2608.11033v1)
  <details><summary>📄 Abstract</summary>
  Feature-attribution methods such as SHAP provide useful evidence about individual model predictions, but their numerical outputs are rarely sufficient for audiences with different expertise, goals, and risks of misinterpretation. In medical AI, the same local explanation must reach patients, clinicians, and data scientists through markedly different forms of communication, and naive verbalization through large language models (LLMs) is prone to weak grounding, conflation of attribution with caus...
  </details>

- **2026-08-11** — Nicola Giuseppe Marchioro, Gabriele Padovani, Amal Gueroudji et al. — [Workflow Cards: Structured Summaries of Workflow Executions Using Provenance Data](http://arxiv.org/abs/2608.11022v1)
  <details><summary>📄 Abstract</summary>
  Model Cards and Data Cards have demonstrated the value of structured, human-readable documentation for machine learning artifacts, capturing their context, parameters, limitations, and intended use. However, these practices remain focused on static artifacts (the datasets and trained models themselves) while overlooking the workflow executions that produce, transform, and evaluate them. Such executions hold critical details about data preparation, parameter choice, runtime behavior, resource use...
  </details>

- **2026-08-11** — Yang Zhou, Chengqun Yu — [Auditable AI-Assisted Research Writing: An Engineering Discipline with Pre-Registered Process Observation](http://arxiv.org/abs/2608.10858v1)
  <details><summary>📄 Abstract</summary>
  Language models now draft, classify and criticise inside research production, yet the artifacts they help produce carry little accountable history. Rather than detecting machine involvement afterwards, we specify an auditability discipline built at production time: git sealing with an anchor lineage, hash-bound provenance, red-line gates that refuse non-compliant artifacts and log every refusal, cross-model role separation, and programmatic assembly from registered sources. Adherence is instrume...
  </details>

- **2026-08-11** — Viktor Volkov, Valentin Khrulkov, Andrey V. Galichin et al. — [EvoMem: Memory-Augmented Evolution for Code Optimization](http://arxiv.org/abs/2608.10795v1)
  <details><summary>📄 Abstract</summary>
  Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains. However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning. We introduce EvoMem, a persistent memory architecture for LLM-based evolutionary program search that captures and reuse...
  </details>

- **2026-08-11** — Aijun Yang, Qianxue Guo, Ziyi Huang et al. — [Self-Correcting Long-Horizon Search Agents via Tree-Structured Memory](http://arxiv.org/abs/2608.10676v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based search agents answer questions through multi-step interactions with external environments. However, providing complete execution trajectories to the LLM causes unbounded context growth and introduces noise. Existing compression methods reduce context at the cost of important details and often replace erroneous facts without repairing downstream reasoning derived from them. To address this problem, we propose ReTree, a self-correcting tree-structured memory mechan...
  </details>

- **2026-08-11** — Xiaokang Qu, Yiting Lin — [HexEval: An Evidence-Driven Hexagonal Framework for Multidimensional Scholar Assessment](http://arxiv.org/abs/2608.10584v1)
  <details><summary>📄 Abstract</summary>
  Scholar assessment plays a fundamental role in faculty recruitment, funding allocation, academic promotion, and talent discovery. Existing scholar assessment methods predominantly rely on bibliometric indicators and reputation proxies, while recent large language model (LLM)-based approaches mainly focus on evaluating individual research papers rather than comprehensively assessing scholars. We argue that scholar assessment should be formulated as an evidence-driven reasoning problem that jointl...
  </details>

- **2026-08-11** — Junwoo Park, Minyoung Shin, Cheol Soon Lee et al. — [Multi-Granular Rationale-Guided Molecular LLM for Property Prediction](http://arxiv.org/abs/2608.10480v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are widely applied across chemical tasks, such as molecular property prediction, which underpins drug discovery. Molecular LLMs represent a molecule through several modalities, notably a 1D SMILES sequence or a 2D molecular graph. Both encode molecular information implicitly, so the contribution of individual substructures remains opaque. Retrieval and augmentation methods add context, but from external sources. However, the cues chemists reason over are the internal...
  </details>

- **2026-08-10** — Saman Rahbar — [Frozen Brain-MRI Foundation Models Are Site Fingerprints](http://arxiv.org/abs/2608.10295v1)
  <details><summary>📄 Abstract</summary>
  Frozen foundation-model (FM) embeddings are increasingly used as off-the-shelf brain-MRI representations, on the assumption that they capture anatomy. We audit what they actually encode and find that acquisition site is a large, intrinsic component of the representation. Across two independent cohorts (ABIDE-I, ABIDE-II), three frozen 3-D encoders (brain-pretrained, CT-pretrained, and randomly initialized), and every network depth, site is linearly decodable at roughly 0.9 balanced accuracy at d...
  </details>

- **2026-08-10** — Raquel R. Valença, Lilianne Nakazono, Rafael Izbicki et al. — [Tabular foundation models for the estimation of probabilistic quasar photometric redshifts in S-PLUS](http://arxiv.org/abs/2608.10280v1)
  <details><summary>📄 Abstract</summary>
  We assess whether tabular foundation models can be used as off-the-shelf probabilistic photometric-redshift estimators for quasars in the 12-band S-PLUS DR6 survey, where colour-redshift degeneracies produce multi-modal posteriors and spectroscopic training sets are shifted relative to the photometric population. TabPFN 2.5, RealTabPFN 2.5, and TabICL are benchmarked against eight task-specific baselines, including linear conditional Gaussians, FlexZBoost, mixture-density networks, normalising f...
  </details>

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
*综述与系统化 / Surveys & Systematization* — 7 papers

- **2026-08-11** — Marco Tulio Valente — [Understanding the Architecture of Coding Agents: An Exploratory Study Using a Research Prototype](http://arxiv.org/abs/2608.10934v1)
  <details><summary>📄 Abstract</summary>
  Coding agents have rapidly emerged as the primary interface for AI-assisted software development. However, despite their growing adoption, relatively little is known about their internal architecture, and no systematic architectural description comparable to those available for compilers or operating systems currently exists. This paper addresses this gap by documenting the main architectural components of coding agents, explaining their responsibilities, interactions, and execution flow. To sup...
  </details>

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


### 📂 other
*其他安全相关 / Other Security-Related* — 147 papers

- **2026-08-11** — Sourabrata Mukherjee, Kalika Bali, Sunayana Sitaram — [Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents](http://arxiv.org/abs/2608.11110v1)
  <details><summary>📄 Abstract</summary>
  When a tool-using agent is given the same task in a different language, does it still take the same steps? Multilingual evaluation rarely asks: it compares final answers and discards the actions. Yet those actions are the product: they fix cost and latency, decide how the system fails, and are the only auditable part of its behaviour. We make the action policy the measured object across 8 models, 6 parallel benchmarks and 41 languages (2.38M rollouts). The naive measurement fails: five confounds...
  </details>

- **2026-08-11** — Ke Ma, Yamin Mao, Weiming Li et al. — [R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video](http://arxiv.org/abs/2608.11017v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon egocentric video is a rich substrate for wearable AI assistants, but object-centric questions such as where an item was moved, when it last changed state, or why it was relocated remain difficult because caption- and transcript-based memories rarely preserve persistent object identity or structured spatial change. Existing long-video QA methods mainly emphasize temporal grounding and clip retrieval, while prior 3D scene-graph methods typically assume stronger geometry than free-moti...
  </details>

- **2026-08-11** — Dongmin Kim, Brian Liu, Jose J. Valero-Mas et al. — [A Dataset and Benchmark for Optical Music Recognition of String Quartet Scores](http://arxiv.org/abs/2608.10978v1)
  <details><summary>📄 Abstract</summary>
  Optical music recognition (OMR) transcribes music scores into digital formats. While the field has advanced significantly on monophonic and piano-form scores, multi-part score transcription remains underexplored, largely due to the absence of a suitable dataset. We introduce OpenScore String Quartet for Optical Music Recognition (OSSQ-OMR), the first dataset dedicated to multi-part OMR. Built on the OpenScore String Quartet corpus, OSSQ-OMR pairs digitally encoded scores with their original scan...
  </details>

- **2026-08-11** — Yuetian Du, Yucheng Wang, Zhenyuan Chen et al. — [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](http://arxiv.org/abs/2608.10964v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Fine-Tuning (RFT) has enabled medical Multimodal Large Language Models (MLLMs) to produce Chain-of-Thought (CoT) reasoning for visual question answering, yet these models suffer from $\textit{confidence miscalibration}$---a systematic gap between expressed certainty and actual diagnostic accuracy that undermines clinical trust. We propose $\textbf{CARE}$, a $\textbf{C}$onfidence-$\textbf{A}$ware medical $\textbf{RE}$asoning framework that jointly optimizes accuracy and calibration ...
  </details>

- **2026-08-11** — Qianggang Ding, Xingyao Wang, Rui Feng et al. — [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](http://arxiv.org/abs/2608.10915v1)
  <details><summary>📄 Abstract</summary>
  After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeli...
  </details>

- **2026-08-11** — Martina Ianaro, Guilherme Fernandes, Maurizio Gabbrielli et al. — [Order Matters: LVLMs as Judges for Temporal Reasoning in Image Sequences](http://arxiv.org/abs/2608.10908v1)
  <details><summary>📄 Abstract</summary>
  As generative multimedia evolves from static image synthesis to complex, interleaved visual narratives, a foundational bottleneck has emerged: the judgment crisis. While human perception naturally synthesizes the temporal and logical flow of a story, automated evaluation systems remain largely "blind" to sequential continuity, often failing to distinguish between a coherent narrative and a semantically shuffled or contradictory sequence. This work identifies a critical structural gap in current ...
  </details>

- **2026-08-11** — Md Rabiul Islam, Samir Abdaljalil, Erchin Serpedin et al. — [ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral](http://arxiv.org/abs/2608.10885v1)
  <details><summary>📄 Abstract</summary>
  Pulmonary nodule malignancy prediction typically depends on image-trained specialist deep learning (DL) models that require substantial annotated imaging data and task-specific training. We investigate whether a generalist large language model (LLM), reading only a faithful natural-language rendering of standard nodule attributes, can serve as a calibrated triage layer. We propose ConfTriage, a confidence-calibrated method built on three pillars: language as the modality, calibration as the safe...
  </details>

- **2026-08-11** — Jiangjie Qiu, Yijun Li, Xiaonan Wang — [ChemWorld: Programmable Chemical Worlds for Controlled and Replayable Agent Experimentation](http://arxiv.org/abs/2608.10792v1)
  <details><summary>📄 Abstract</summary>
  Autonomous chemistry increasingly depends on environments in which agents can repeatedly act, observe, and adapt.Physical laboratories provide essential real-material evidence but are costly to repeat and difficult to use for tightly matched interventions, whereas most digital environments keep the underlying experimental world largely fixed. We introduce ChemWorld, a programmable chemical environment in which reusable process and observation components are compiled into executable worlds. ChemW...
  </details>

- **2026-08-11** — Zihao Liu, Xiaolong Shen, Zhenglin Zhou et al. — [Beyond Pixels: From Video Priors to 4D Worlds](http://arxiv.org/abs/2608.10744v1)
  <details><summary>📄 Abstract</summary>
  4D generation synthesizes dynamic 3D scenes from conditions such as text or images. Existing methods either reconstruct generated RGB videos with a separate 4D model or adapt a particular video generator to predict geometry directly. The former suffers from distribution mismatch and error propagation, whereas the latter ties 4D prediction to a specific generator and may require retraining when the generator or conditioning regime changes. We ask whether the final denoised latents of video models...
  </details>

- **2026-08-11** — Haoze Liu, Run Liu, Haiying Xu et al. — [Your LLM, Your Style: Behavioral Mode Axes for LLM Behavioral Control](http://arxiv.org/abs/2608.10703v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly act in interactive settings where their behavioral styles affect user experience, safety, and downstream decision making. Existing LLM personality studies largely rely on self-report questionnaires administered in first-person settings, making the resulting profiles sensitive to surface elicitation choices and poorly grounded in concrete model behavior. In this work, we introduce a situated behavioral-data (B-data) framework for studying and controlling ...
  </details>

- **2026-08-11** — Jingyang Tan, Sheng Yang, Yuanpeng Chen et al. — [Rethinking Text-Based Image Retrieval in Specific Domain](http://arxiv.org/abs/2608.10524v1)
  <details><summary>📄 Abstract</summary>
  Driven by the rapid advancement of vision-language representation learning, Text-based Image Retrieval (TBIR) has made notable progress. However, existing benchmarks are predominantly constructed on an exclusive single-match assumption between query and images. While effective in general scenarios, this assumption fails to reflect practical system performance in specific domains (e.g., surveillance), where a single query often corresponds to multiple relevant candidate images. To address this li...
  </details>

- **2026-08-11** — Davood Wadi, Mohsen Ghodrat, Matthew Philp — [Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases](http://arxiv.org/abs/2608.10503v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) are increasingly deployed as autonomous agents, accurately evaluating their latent values and biases is critical. The NLP community typically evaluates models using large, unstructured benchmarks. While effective for general capabilities, these datasets fundamentally conflate causal mechanisms: even when an aggregate bias is detected, unstructured evaluations cannot disentangle whether it stems from baseline traits, contextual confounders, or complex interactions....
  </details>

- **2026-08-11** — Xin Xiao, Jiang Zhong, Junnan Zhu et al. — [GeoForge: Non-Parametric Self-Evolving Agents for Earth-Observation Reasoning](http://arxiv.org/abs/2608.10494v1)
  <details><summary>📄 Abstract</summary>
  Earth observation (EO) agents construct scientifically valid tool workflows and ground their conclusions in current geospatial evidence. This is challenging because EO workflows are constrained by sensing semantics, product dependencies, spatial and temporal compatibility, and parameter requirements. Existing agents often search a broad operation space for each query, while recent self-evolving systems do not fully organize heterogeneous EO trajectories into reusable knowledge across different d...
  </details>

- **2026-08-11** — Li Wenjie, Yash Jangir, Ignacy Stepka et al. — [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](http://arxiv.org/abs/2608.10484v1)
  <details><summary>📄 Abstract</summary>
  Action verbs describe not only the physical outcomes of actions, but also how those actions are performed. Yet action representations in vision-language-action models (VLAs) are typically optimized for reconstruction under L1/L2 losses in raw action space, where numerical proximity need not reflect linguistically meaningful distinctions. On BridgeV2, we show that action trajectories contain verb-grounding information beyond visual state changes, and that reconstruction-only discrete tokenization...
  </details>

- **2026-08-11** — Bhavyesh Sajja, Max Kleiman-Weiner, Roger Zimmermann et al. — [Evaluating Rational Contracting in Natural Language](http://arxiv.org/abs/2608.10475v1)
  <details><summary>📄 Abstract</summary>
  The emergence of language-based AI agents promises to transform the scope of machine economic activity. Instead of just proposing bids or following hard-coded protocols, such agents can be used to negotiate and execute agreements in open-ended natural language. However, most evaluations of these abilities have focused on one-off exchanges or simple economic games, leaving open the rich space of time-extended, contingent, and incomplete contracts made expressible by language; they also focus on r...
  </details>

- **2026-08-11** — Joscha N. Jahns-Schindler, Keith W. Bannister, Adam T. Deller et al. — [Two new highly scattered fast radio bursts: evidence for scatter broadening by the circumsource medium](http://arxiv.org/abs/2608.10452v1)
  <details><summary>📄 Abstract</summary>
  We found two highly scattered Fast Radio Bursts (FRBs) during commissioning of the Commensal Realtime ASKAP Fast Transient COherent (CRACO) backend. FRB 240210D and FRB 240312D have scattering times of $34\pm6$ and $300\pm48$ ms, respectively, when scaled to 1 GHz. FRB 240312D originates near a spiral arm of a face-on galaxy at a redshift of only 0.05. Scintillation from a Milky Way screen constrains the distance of the scattering screen to $\sim 10$ pc from the source. FRB 240312D is therefore ...
  </details>

- **2026-08-11** — Sujung Oh, Jung Uk Kim, Sangmin Lee — [Rationale-Guided Learning for Multimodal Emotion Recognition](http://arxiv.org/abs/2608.10448v1)
  <details><summary>📄 Abstract</summary>
  Multimodal emotion recognition in conversation (MERC) requires understanding complex interactions between verbal and non-verbal cues. However, most existing approaches fundamentally treat this as a direct input-output (multimodal cues-emotion labels) mapping problem, overlooking the causal reasoning that humans use when interpreting emotions. We propose rationale-guided learning (RGL), a novel framework that transforms MERC into a cognitively-inspired reasoning task. Based on dual-process theory...
  </details>

- **2026-08-11** — Lening Zhao, Qipeng Zhan, Li Shen — [Invertible Logits Transformation for Accuracy-Preserving Post-Hoc Uncertainty Calibration](http://arxiv.org/abs/2608.10372v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc calibration aligns a classifier's predicted confidences with its empirical accuracy without retraining. An ideal calibrator should correct nonlinear miscalibration, scale gracefully to large label spaces, and preserve the original predictions; existing methods typically violate at least one of these properties---temperature scaling lacks expressivity, more flexible parametric alternatives introduce parameters that grow with the number of classes $C$, and other expressive methods do not ...
  </details>

- **2026-08-11** — Lin Liao, Peng Li — [Nutrition Data Infrastructure for the AI Era: Operationalizing FAIR for Agent-Mediated Research](http://arxiv.org/abs/2608.10363v1)
  <details><summary>📄 Abstract</summary>
  AI agents can accelerate nutrition research, but their analyses inherit the identity, semantic, and release ambiguities of the underlying data. We present Nutrition Data Service (NDS), source-preserving infrastructure that operationalizes FAIR for automated use: description resolution makes release-specific records findable; typed crosswalks connect independently released resources; machine-readable interfaces expose versioned sources and crosswalks, making analyses by AI agents replayable and a...
  </details>

- **2026-08-11** — Patrick Vossler, Jialin Ouyang, F. Richard Guo et al. — [Expert-Guided g-computation with Large Language Models for Estimating Causal Effects on Timings: Applications to Hospital Quality Improvement](http://arxiv.org/abs/2608.10339v1)
  <details><summary>📄 Abstract</summary>
  Hospital quality improvement (QI) programs routinely face multiple candidate interventions to optimize hospital flow, but existing methods struggle to estimate and rank the causal effects of such interventions. This work focuses on one of the most standard hospital metrics, the average length of stay (LOS), and its causal estimand, the average time saved. To characterize this causal effect, qualitative approaches rely on expert judgment to map patient trajectories, making them susceptible to cog...
  </details>

- **2026-08-11** — Tsofia Cohen, Tom Hope — [MUSE: A Full-Text Cross-Domain Knowledge Base of Scientific Problems, Solutions, and Rationales](http://arxiv.org/abs/2608.10974v1)
  <details><summary>📄 Abstract</summary>
  Scientific papers contain fine-grained records of problem solving: authors mention technical obstacles and methods that were used to address them, often along with reasoning on why those methods were chosen. We introduce MUSE (Mining Underlying Scientific Explanations), a full-text, multi-domain resource of scientific Problem-Solution-Rationale (P-S-R) triplets. We curate 579 expert-annotated full-text paragraphs, with a rich annotation schema covering salient problem, solution, and rationale sp...
  </details>

- **2026-08-11** — Ge Yan, Jinghao Liu, Yuzhi Fan et al. — [Flex-$π$: A Multi-Stream World-Action Model with Compute Flexibility](http://arxiv.org/abs/2608.10860v1)
  <details><summary>📄 Abstract</summary>
  World-action models (WAMs) predict the future to act better, but nearly all of them predict only RGB latents, trained purely for pixel reconstruction, with no explicit signal for the 3D geometry or object semantics manipulation needs. We find a surprising free lunch: the same frozen video-generation VAE that encodes RGB also encodes 3D pointmaps almost losslessly, with no pointmap-specific training at all. This lets us supervise Flex-$π$, a 6B-parameter WAM, on 3D geometry and object-centric DIN...
  </details>

- **2026-08-11** — Nikolai Bolik, Lennart Stöpler, Artur Andrzejak — [Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders](http://arxiv.org/abs/2608.11197v1)
  <details><summary>📄 Abstract</summary>
  Shani et al. (2026) show that LLM representations broadly recover human category boundaries, while failing to reflect fine-grained typicality structure. Their analysis uses cosine similarity over dense model representations. We revisit their approach using overlap over active sparse autoencoder (SAE) latent sets as a more interpretable similarity measure. We first verify that this set-level measure is meaningful: SAE latent sets can recover union-like compositional structure in controlled toy mo...
  </details>

- **2026-08-11** — Song-Duo Ma, Pu-Jen Cheng — [Are We Really Making Progress in Group Recommendation? Unmasking the Tie-Breaking Illusion](http://arxiv.org/abs/2608.11190v1)
  <details><summary>📄 Abstract</summary>
  Recent group recommendation methods have reported strong improvements on standard benchmarks, but it remains unclear whether these gains always reflect genuine advances in modeling group preferences. In this paper, we show that several recent methods are affected by a systematic evaluation bias caused by the interaction between training-time score compression and evaluation-time deterministic tie-breaking. Specifically, an additional sigmoid transformation before the BPR objective can greatly in...
  </details>

- **2026-08-11** — Jiayu Ding, Meilu Song, Yun Chen et al. — [CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting](http://arxiv.org/abs/2608.11150v1)
  <details><summary>📄 Abstract</summary>
  While 3D Gaussian Splatting (3DGS) has advanced open vocabulary scene understanding, existing methods remain confined to explicit queries. They struggle to interpret implicit intents, complex spatial constraints, and commonsense reasoning required for practical embodied interactions. To address this gap, we introduce the task of reasoning 3D Gaussian segmentation and construct two benchmarks, Causal-LERF and Causal-ScanNet. These benchmarks systematically evaluate commonsense, spatial, affordanc...
  </details>

- **2026-08-11** — Xiaofan Bai, Hongqiang Lin, Chao Liu et al. — [SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure](http://arxiv.org/abs/2608.11079v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents accumulate reusable skills by appending successful procedures and failure fixes. Over time, the same requirement is often restated in several branches, examples, and warnings, while common action sequences are copied rather than reused. The resulting skill becomes expensive to inject and difficult to maintain. Generic prompt compression is ill-suited to this setting because a skill is not a flat passage: its name and description define when it applies, its workflow controls ...
  </details>

- **2026-08-11** — Loriano Bonora, Roberto Soldati — [A fermion primer](http://arxiv.org/abs/2608.10925v1)
  <details><summary>📄 Abstract</summary>
  This is a review paper intended to illustrate a few critical issues concerning Dirac, Weyl and Majorana fermions and their differences. The first part consists in basic introductions to fermions, and more in detail to fermions in 4d, focusing in particular in what differentiate the three type of fermions: chirality, helicity, mass, field equations, properties under discrete symmetry transformations, Actions, Observables. On this basis we tackle a series of challenging and sometime controversial ...
  </details>

- **2026-08-11** — Kaivalya Rawal, Daria Onitiu, Brent Mittelstadt et al. — [Rule of Thumb: Explaining Artificial Intelligence Systems using Partial Information](http://arxiv.org/abs/2608.10766v1)
  <details><summary>📄 Abstract</summary>
  Explainable Artificial Intelligence (XAI) seeks to explain how an Artificial Intelligence (AI) system arrived at a particular decision. We propose ''Rule of Thumb'' (RoT) explanations, a new approach to XAI based upon a novel formulation that identifies the most relevant features for predicting the behaviour of an AI system, for a particular datapoint. We show how RoT is well-suited to enable XAI in: (a) zero-shot classification using large language models (LLMs), (b) auditing of opaque AI syste...
  </details>

- **2026-08-11** — Junyong Choi, Cheolhyeon Park, Jaehoon Cho — [Grid-Preserving Knowledge Distillation: Transferring Convolutional Inductive Bias to Vision Transformers under Data Scarcity](http://arxiv.org/abs/2608.10723v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers underperform convolutional networks when training data is scarce, and distilling convolutional inductive biases from a CNN teacher is an effective remedy that leaves the deployed model unchanged. General-purpose feature distillation, however, transfers little in this setting. The pooling, flattening, and logit-space projections it inherits from CNN to CNN pipelines discard the spatial grid in which locality and translation equivariance are encoded, and unlike a convolutional ...
  </details>

- **2026-08-11** — Shuai Wang, Wangyuan Ding, Yixian Shen et al. — [MMArt A Multi-Perspective Multimodal Dataset for Visual Art Understanding](http://arxiv.org/abs/2608.10706v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language models demonstrate impressive general visual understanding, yet their art interpretation remains shallow: they describe surface content but struggle with formal analysis, grounded historical interpretation, or affective characterization. We argue this is not only a model but also a dataset limitation. Existing art datasets are single perspective resources, where no dataset provides narrative, formal, emotional, and historical perspectives simultaneously for the same artwor...
  </details>

- **2026-08-11** — Fabrizio Russo, Mark Somers — [Operationalising Relative Causal Knowledge: Backbone Identifiability from Private Reports on a Shared Outcome](http://arxiv.org/abs/2608.10664v1)
  <details><summary>📄 Abstract</summary>
  The Relativity of Causal Knowledge (RCK) explains how a network of agents with different structural causal models can exchange causal knowledge through a shared interventionally consistent abstraction, or backbone. We ask the prior identification question that this transport mechanism presupposes: when is that backbone determined by the agents' private causal knowledge? In the basic two-agent common-effect case, two private causes influence one shared outcome and each agent identifies only the s...
  </details>

- **2026-08-11** — Linhao Wu, Yizhou Chen, Zhen Yang et al. — [CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing](http://arxiv.org/abs/2608.10613v1)
  <details><summary>📄 Abstract</summary>
  Automated Program Repair (APR) has recently benefited from Large Language Models (LLMs), yet their effectiveness heavily depends on repair context. Existing LLM-based APR methods suffer from a causality gap: test contexts can be noisy or incomplete, while source contexts derived from static analysis often contain irrelevant and unexecuted code, misleading LLMs from identifying the true root cause. To address this issue, we propose CausalRepair, a conversation-driven APR framework based on minima...
  </details>

- **2026-08-11** — Nicola Fabiano — [Inferential Capability Does Not Determine Legal Scope](http://arxiv.org/abs/2608.10601v1)
  <details><summary>📄 Abstract</summary>
  Two instruments of EU digital law place inference at their centre and mean different things by it. Article 3(1) of the AI Act uses the capability to infer constitutively: it is the central feature separating the regulated category from conventional software. The GDPR never defines inference, yet governs it protectively: the consequences follow from the processing of personal data and from what the inference says about, or does to, a person, whether or not the technology that produced it qualifie...
  </details>

- **2026-08-11** — Dong Xu, Zhangfan Yang, Jiantao Wu et al. — [DegradeQuery: Counterfactual Tuple Pretraining for Context-Aware PROTAC Degradation Prediction](http://arxiv.org/abs/2608.10595v1)
  <details><summary>📄 Abstract</summary>
  Proteolysis-targeting chimeras (PROTACs) induce protein degradation by recruiting a target protein to an E3 ubiquitin ligase, making degradation a joint outcome of the degrader molecule and its biological context. Although public databases contain thousands of structured molecule-target-E3 records, degradation measurements are available for only a small fraction of them. Existing supervised approaches therefore leave most recorded chemical-biological relationships unused. We introduce DegradeQue...
  </details>

- **2026-08-11** — Fanqi Zhou, Qiaosheng Chen, Zixian Huang et al. — [Agentic Instruction Data Selection: Let DataMaster Interpret Your Intent](http://arxiv.org/abs/2608.10579v1)
  <details><summary>📄 Abstract</summary>
  Although existing instruction data selection methods have introduced various metrics, the inherent complexity of real-world datasets makes it impractical for any single metric to generalize across all scenarios. Developers are thus often forced to manually inspect data and craft heuristic rules for each new application---a tedious and error-prone process. In this paper, we propose a paradigm shift from manual configuration to automated orchestration via the Instruction Data Selection Agent (Data...
  </details>

- **2026-08-11** — Zhichen Yang, Rui Xu, Yuzhen Niu et al. — [Towards Color-Faithful Low-Light Image Enhancement via Adaptive Color Debiasing and Saturation Rectification](http://arxiv.org/abs/2608.10512v1)
  <details><summary>📄 Abstract</summary>
  Low-light imaging often introduces color bias caused by the low signal-to-noise ratio and the image formation process. Although recent low-light image enhancement methods have achieved strong brightness recovery, faithful color restoration remains challenging, manifesting as overall color bias together with local under- and over-saturation. To address this issue, we propose CAGE, a cylindrical color correction framework with adaptive color debiasing and gamut-harmonized saturation rectification ...
  </details>

- **2026-08-11** — Ying Jin, Noel C. F. Codella, John Corring et al. — [RadFusion: Towards Threshold-Controllable Radiology Report Generation](http://arxiv.org/abs/2608.10505v1)
  <details><summary>📄 Abstract</summary>
  Automated radiology report generation is advancing rapidly in response to the shortage of radiologists, yet unlike a perception model, existing generation models offer no control over the sensitivity-specificity trade-off of their diagnostic content. Such control is essential because clinical scenarios diverge: emergency triage prioritizes sensitivity to reduce missed findings, whereas confirmatory interpretation emphasizes specificity to limit unnecessary interventions. A single fixed report ca...
  </details>

- **2026-08-11** — Jung Hwan Lee, Kyu Ho Lee, Gwang Hoon Yoo — [MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph](http://arxiv.org/abs/2608.10504v1)
  <details><summary>📄 Abstract</summary>
  As coding agents increasingly handle implementation, the central challenge shifts from building individual agents to building an infrastructure that systematically improves them. Current approaches optimize agent systems without accumulating transferable knowledge, accumulate knowledge without compositional reasoning over it, and lack a mechanism for that knowledge to self-evolve through operational evidence. MEGA (Meta Evaluation-Grounded Adaptation) addresses these gaps as a self-evolving infr...
  </details>

- **2026-08-11** — Jongwon Park, Inhyo Lee, Junhyeong Lee et al. — [Predicting Space Groups of Double Perovskites by LLM with Dynamic Few-Shot Learning](http://arxiv.org/abs/2608.10483v1)
  <details><summary>📄 Abstract</summary>
  Double perovskites (DPs) offer broad compositional tunability, but predicting the space groups (SGs) of stable structures remains difficult because available datasets are often strongly imbalanced toward dominant SG classes. We refer to dominant SG classes as major SGs and underrepresented classes as minor SGs. We introduce Dynamic and Diversity-enhanced Few-shot Retrieval and Rule-Guided Inference for Space-Group Prediction (DyRIS), an LLM-agent-based framework that predicts ranked SG candidate...
  </details>

- **2026-08-11** — Ying Yuan — [Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM Acquisition Agents](http://arxiv.org/abs/2608.10441v1)
  <details><summary>📄 Abstract</summary>
  Many pipelines can pay a per-example cost to acquire an auxiliary, model-derived observation -- an LLM's structured reasoning, a slow oracle, an expensive measurement -- and then must decide when the acquired signal is worth using. Our thesis is a distinction that is easy to miss: detecting that such a signal helps on average is not the same as learning to act on it per instance, and a reward-SNR floor governs when the second is even possible. Even when the signal is faithful and an in-sample or...
  </details>

- **2026-08-11** — Hadi Hosseini, Payas Khurana, Shraddha Pathak et al. — [To EFX OR to MMS, That is the Question](http://arxiv.org/abs/2608.10397v1)
  <details><summary>📄 Abstract</summary>
  We study the agent-wise disjunction of two central fairness notions for indivisible items, where every agent must be either envy-free up to any item (EFX) or maximin-share (MMS) satisfied. One might expect this flexibility to restore existence, especially because the existence of EFX itself resisted resolution for nearly a decade. Surprisingly, it does not. We construct counterexamples with three agents and eight submodular goods, and with three agents and seven submodular chores, significantly ...
  </details>

- **2026-08-11** — Yejin Jeon, Marie Maltais, Virginia Ceccatelli et al. — [VoxSumm: A Multilingual Corpus of Long-Form Spoken News for Joint Summarization and Translation](http://arxiv.org/abs/2608.10359v1)
  <details><summary>📄 Abstract</summary>
  As information increasingly traverses linguistic boundaries, users require concise cross-lingual representations of long-form content. Nevertheless, long-document summarization research remains text-centric, whereas multilingual speech research has largely prioritized translation, preserving source content rather than compressing it. We address this methodological gap by formalizing joint speech summarization and translation (JSumT): the generation of a succinct, faithful target-language summary...
  </details>

- **2026-08-11** — Tianyi Fu, Mohan Sridharan — [Hierarchical Compositionality for An Assistive AI Agent](http://arxiv.org/abs/2608.10330v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly being developed to assist humans in various applications, and Large Language Models and other deep network architectures are considered to be state of the art for such agents. These methods are impressive stochastic predictors, but they are resource-hungry, opaque, and known to make arbitrary decisions in novel situations due to the narrow set of underlying representation and processing choices. Our work seeks to explore the design of architectures for such AI agents b...
  </details>

- **2026-08-10** — Siyang Wu, Yibo Jiang, Bryon Aragam — [Is This Your Final Answer? Cross-Contextual Consistency as a Measure of LLM Credibility](http://arxiv.org/abs/2608.10315v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are powerful black-box systems, making it difficult to discern whether their answers reflect stable internal beliefs or superficial pattern matching. We identify cross-contextual consistency as an underutilized behavioral property of LLMs: a credible answer should remain stable when the same task is placed under topic-aligned, content-neutral contextual variation. Building on this intuition, we operationalize Cross-Contextual Consistency (C3) by comparing model gener...
  </details>

- **2026-08-10** — Waleed Jamil, Raphael Schmitt — [TAF-MED: Multi-Turn Safety Refusal Collapse in LLMs Under Declared Self-Treatment Intent](http://arxiv.org/abs/2608.10258v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly provide conversational health information that may influence treatment decisions, yet existing benchmarks do not isolate whether medication-safety boundaries persist across follow-ups after explicit self-treatment intent. We introduce TAF-MED, a physician-reviewed benchmark of 500 fixed three-turn scenarios, and evaluate eight LLMs across 4,000 conversations. A rubric-based automated judge labelled responses as SAFE, LEAKY, or UNSAFE, and two physicians ...
  </details>

- **2026-08-10** — Ying Li, Shradha Sehgal, Arjun Rao et al. — [GenRec: An LLM-Backed Recommendation Ranker at Netflix](http://arxiv.org/abs/2608.10257v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are reshaping recommender systems by enabling richer modeling of users, content, and context directly in natural language. At Netflix, we are exploring this direction through GenRec, an LLM-backed recommendation ranker built on top of an in-house foundational LLM. GenRec follows a two-phase framework: Phase 1 adapts an open-source LLM to Netflix data, developing deep understanding of the catalog and member behavior while balancing capabilities such as content underst...
  </details>

- **2026-08-10** — Scott E. Frias — [Similarity Gates Approve Reversals: A Validity Audit of Embedding-Cosine Thresholds in Agent Systems](http://arxiv.org/abs/2608.10216v1)
  <details><summary>📄 Abstract</summary>
  Agent frameworks ship quality gates that compare text blocks by embedding-cosine similarity and decide at a fixed cutoff. Deduplication filters, semantic caches, drift guards, and answer grader gates deploy to answer the question: "Does this text still mean the same thing?" But the score answers a different question: "How much did the wording change?" We audit this gate class as a measurement instrument. In the cases these gates exist to catch, the two can run in opposite ways. Many times, rever...
  </details>

- **2026-08-10** — Aparajita Bandyopadhyay, Hui Yuan, Willie J. Padilla et al. — [Active Electronic Terahertz Imaging for Industrial Applications: From Hardware to the Paradigm Shift by Artificial Intelligence](http://arxiv.org/abs/2608.10200v1)
  <details><summary>📄 Abstract</summary>
  Imaging with terahertz (THz) radiation (0.3-10 THz) benefits from a unique combination of attributes: penetration through dry, non-polar packaging materials; variations of dielectric functions to provide contrast; the existence of spectral fingerprint resonances for some classes of materials; non-ionizing photon energies that are safe for use around humans; and - viewed from the low-frequency side - an extension of the capabilities of microwave radar to higher frequencies and thus to substantial...
  </details>

- **2026-08-10** — Di Wu, Xiaohui Zhu — [Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents](http://arxiv.org/abs/2608.10198v1)
  <details><summary>📄 Abstract</summary>
  Latent-space communication allows heterogeneous vision-language model agents to exchange continuous representations without serializing visual and reasoning states into text. Vision Wormhole realizes this approach by translating visual features into a universal latent representation that can be consumed by another model, but every message is transported as a dense tensor of the same size regardless of its content. A fixed-capacity dense tensor therefore need not have a fixed effective informatio...
  </details>

- **2026-08-10** — Changshuai Wei, John Bencina, Phuc Nguyen et al. — [From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation](http://arxiv.org/abs/2608.10182v1)
  <details><summary>📄 Abstract</summary>
  Large-scale targeting and recommendation systems are typically built around predictive scores fed into heuristic or local allocation. When the business goal is incremental impact, as in marketing campaigns, incentives, and notifications, this paradigm systematically misallocates resources toward users who would have acted anyway. We present a decision-centric framework that instead optimizes causal effects under global constraints, aligning three components under a single objective: a causal neu...
  </details>

- **2026-08-10** — Yuhan Fang — [Beyond Cash Flows: A Multi-Agent AI Framework for Valuing Clinical-Stage, Cross-Border Biotechnology](http://arxiv.org/abs/2608.10175v1)
  <details><summary>📄 Abstract</summary>
  A new class of software systems is transforming investment analysis. Large language model agents assembled into collaborative team structures including analysts, researchers, and risk managers are increasingly deployed across financial markets. Yet current multi-agent frameworks share a critical limitation: they rely on the foundational assumption that companies can be valued through traditional cash flows. This paradigm fails in clinical-stage biotechnology, where enterprise value depends entir...
  </details>

- **2026-08-10** — Guilherme Vedana — [Classification of Fourier summation formulas on a horizontal strip](http://arxiv.org/abs/2608.10121v1)
  <details><summary>📄 Abstract</summary>
  We extend the classification of Fourier summation formulas to the setting in which the measure $μ$ is supported on a strip of finite width in $\mathbb{C}$. This broader framework encompasses important examples, including the Guinand--Weil explicit formulas for functions in the Selberg class, which lie beyond the scope of the previous classification.   We study identities of the form \begin{align*}   \sum_{n\geq0} a(λ_n)\varphi(λ_n)=\int_{\mathbb{R}} \widehat{\varphi}(t) \mathrm{d}ν(t)+\sum_{γ\in...
  </details>

- **2026-08-10** — Hunter Schofield, Mohammed Elmahgiubi, Mohammad Mahdavian et al. — [Chain of Spatial Thoughts: Modality-Agnostic Spatial Grounding for Vision Language Models](http://arxiv.org/abs/2608.10278v1)
  <details><summary>📄 Abstract</summary>
  Spatial understanding is fundamental to embodied intelligence, underpinning applications such as robotic manipulation, embodied navigation, and autonomous driving. Although recent vision-language models (VLMs) have achieved impressive performance on spatial reasoning benchmarks, state-of-the-art approaches typically rely on additional spatial encoders or architectural modifications during inference, increasing computational cost. We introduce Space Tokens, a lightweight, architecture-agnostic fr...
  </details>

- **2026-08-10** — Graeme Baker, Agostino Capponi — [Multi-Credit Calibration via Elastically Stopped Lévy Processes](http://arxiv.org/abs/2608.10321v1)
  <details><summary>📄 Abstract</summary>
  We calibrate credit default swaps and index tranches with elastically stopped Lévy processes: each firm defaults when the running supremum of a latent, spectrally positive distress process crosses an independent exponential barrier. This yields a Cox construction with totally inaccessible default times, while retaining the interpretability and explicit formulas of a structural approach. Adding a single common compound Poisson jump factor to every firm's latent driver gives a parsimonious multi-c...
  </details>

- **2026-08-10** — Amanda Bertsch, Luca Soldaini, Matthew R. Gormley et al. — [Cracks in the Foundation: Seemingly Minor Architectural Choices Impact Long Context Extension](http://arxiv.org/abs/2608.10296v1)
  <details><summary>📄 Abstract</summary>
  One might imagine that architectural variations within the dense transformer paradigm have a limited effect on accuracy. However, we demonstrate that this is not the case in the long context setting. Specifically, we show that a set of four minor architectural decisions --- all made by at least one of the Olmo, Llama, and Qwen dense model families --- have a compoundingly negative effect on long context extensibility. Any one of these choices alone has a minor impact on long context performance,...
  </details>

- **2026-08-10** — Mark Oskin — [Off-Axis, On Purpose: Where a Transformer Computes Concepts and Why it Does So](http://arxiv.org/abs/2608.10251v1)
  <details><summary>📄 Abstract</summary>
  A transformer's answer lives on one axis: the direction its unembedding reads. Its intermediate states largely do not, and that off-axis position is usually treated as an obstacle to interpretation. We show it is functional. A 12-layer model computes in two phases. Through the first, every sublayer writes into a subspace held near-orthogonal to the read-out, attention 75 to 96 degrees off it at every depth. Moving attention's values onto the read-out is 64 to 84 times more damaging than a matche...
  </details>

- **2026-08-10** — Xin Dong, Vikash V. Gayah — [Mitigating Bus Bunching with Reinforcement Learning Enhanced by Semantic Stop Embedding](http://arxiv.org/abs/2608.10207v1)
  <details><summary>📄 Abstract</summary>
  Bus bunching degrades service regularity and increases passenger waiting in high-frequency transit. Existing reinforcement-learning-based holding controllers primarily rely on instantaneous operational variables or route-specific stop identifiers, which provide limited information about the functional and operational context of individual stops and constrain policy reuse across routes. This study introduces an LLM-assisted semantic stop representation for event-driven bus holding control. An LLM...
  </details>

- **2026-08-10** — Haoyu Han, Yuming Liu, Lei Huang et al. — [ConnectionMind: Leveraging Social Networks and Large Language Models for Personalized Recommendation at Meta](http://arxiv.org/abs/2608.10187v1)
  <details><summary>📄 Abstract</summary>
  Modern recommendation systems on social media platforms such as Meta must model complex social relationships, including friendships, group memberships, and creator interactions, alongside massive and heterogeneous content such as text and video. Traditional recommendation models, however, often omit these signals or treat them independently, lacking the reasoning capability to integrate multi-relational context for fine-grained personalization. We present ConnectionMind, a production-ready recom...
  </details>

- **2026-08-10** — Siqi Yang, Qianlan Yang, Yu-Xiong Wang et al. — [One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models](http://arxiv.org/abs/2608.10178v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving harnesses are closed-loop systems in which an agent inspects its own rollouts and edits its prompts, tools, and memory. They reliably improve coding agents in evaluations, but prior work reports aggregate gains rather than analyzing what the evolved artifacts encode. It therefore remains unclear whether they encode benchmark-specific adaptations, language-specific engineering knowledge, or compensation for limitations of the underlying model. We disentangle these factors by holding...
  </details>

- **2026-08-10** — Ashim Dhor, Pin-Yu Chen — [Intrinsic Structure: Spectral Identifiability for Mechanistic Interpretability](http://arxiv.org/abs/2608.10172v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability explains models by identifying circuits inside them, but has no way to tell whether a circuit is a property of the model or an artifact of the method that found it. Sparse autoencoders illustrate the problem: different seeds and widths recover materially different features from the same activations, and no theory says whether that variability is incidental or structural. We put dictionary learning for interpretability on an identifiability footing. Treating the forwa...
  </details>

- **2026-08-10** — Xu Zhang, Chang Xu, Hui Sun et al. — [REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting](http://arxiv.org/abs/2608.10149v1)
  <details><summary>📄 Abstract</summary>
  Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rely on fixed rules or black-box models based solely on numerical inputs, failing to leverage LLM reasoning for interpretable weighting decisions. We propose REATS, which leverages LLM reasoning capabilities as an intelligent ensemble router that jointly processes textual temporal p...
  </details>

- **2026-08-10** — Kaidi Wang, Daniel K. C. So, Zhiguo Ding — [Pinching-Antenna Systems: From Antenna Placement to Antenna Roaming](http://arxiv.org/abs/2608.10136v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates pinching-antenna systems with finite antenna movement speed, under which conventional antenna placement is subject to non-negligible repositioning delay, resulting in a fundamental tradeoff between channel quality and effective transmission time. In this context, antenna roaming is proposed as a novel operation mode, in which the antenna moves continuously along the waveguide while simultaneously serving users. By incorporating communication and antenna movement into the ...
  </details>

- **2026-08-10** — Zhengfeng Li, Lei Zhang, Xianwei Wu et al. — [OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review](http://arxiv.org/abs/2608.09290v2)
  <details><summary>📄 Abstract</summary>
  LLM-based code review agents promise scalable, always-on review, yet current systems suffer from two intertwined weaknesses: (1) non-determinism--unbounded tool use makes review outcomes unstable, and (2) context locality--the reviewer's access remains bounded to the diff, capping discoverable issue depth. Both give rise to three challenges: misaligned context retrieval, a coherence-efficiency trade-off in multi-file pull requests, and hallucinated comments that erode trust. To address these, we...
  </details>

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

- **2026-08-09** — Yunjia Li, Menglin Wu, Junyu Dai et al. — [Beyond Reconstruction: Full-Context Generative DiT for Music Generation](http://arxiv.org/abs/2608.08787v2)
  <details><summary>📄 Abstract</summary>
  Hybrid music generators combine the long-range planning of an autoregressive language model with the fidelity of a diffusion- or flow-based acoustic renderer. Yet renderers are trained with clean, target-derived codec tokens but deployed with imperfect language-model predictions, creating codecinterface exposure bias. Rather than treating rendering as a simple reconstruction task,we formulate it as full-context generation from an imperfect discrete plan. We introduce FullDiT, a conditional DiT t...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 576 |
| prompt-injection | 486 |
| memory-poisoning | 44 |
| tool-use-attack | 112 |
| backdoor | 411 |
| adversarial-attack | 555 |
| privacy-leakage | 3805 |
| steganography | 55 |
| misuse | 879 |
| red-teaming | 114 |
| vulnerability | 2644 |
| defense | 2347 |
| alignment | 2182 |
| robustness | 2159 |
| watermark | 274 |
| unlearning | 86 |
| agent-safety | 52 |
| benchmark | 57 |
| survey | 278 |
| other | 6196 |

---

📚 **全部 23312 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

⚠️ **本次更新跳过：arXiv API 爬取失败，数据为上次缓存。下次 CI 将自动重试。**

*Generated by AgentGuard at 2026-08-13 02:03:53*