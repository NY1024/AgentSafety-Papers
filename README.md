<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-23494-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-13 12:57 ｜ **论文总数 / Total Papers**: 23494（近 30 天 / Recent 30 days: 2796）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 23494 篇论文（含摘要、分类筛选、搜索）/ View all 23494 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 577
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 488
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 113
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 413
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 555
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3816
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 886
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 114
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2665
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2362
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2201
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2188
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 280
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 86
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 57
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 279
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6263

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2796 篇，完整 23494 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2796 papers from the last 30 days (with date, authors & abstract). For the full list of 23494 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 8 papers

- **2026-08-12** — Xucheng Yu, Emily Knox, Haohan Wang — [Understanding Content Moderation in Large Language Models through Restricted Books: From Refusal to Warning](http://arxiv.org/abs/2608.11806v1)
  <details><summary>📄 Abstract</summary>
  As large language models enter everyday information pipelines, understanding how they handle sensitive topics matters as much as understanding whether they handle them at all. We study this question through a large-scale, systematic experiment using restricted versus unrestricted books as a controlled testbed: 40,800 query-response pairs, 400 books, 17 prompt designs, and six frontier models spanning six AI providers (Claude Sonnet 4.5, GPT-4o, Gemini 2.5 Flash, DeepSeek-V3, Qwen-Plus, and Grok-...
  </details>

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 4 papers

- **2026-08-12** — Van Tran, Taveesh Sharma, Tajveer Singh Dhesi et al. — [Rethinking Agent Security as a Networking Problem](http://arxiv.org/abs/2608.12172v1)
  <details><summary>📄 Abstract</summary>
  AI agents are rapidly becoming more capable and widely deployed, promising substantial gains in productivity and enabling new classes of applications. However, their growing autonomy also introduces significant privacy and security risks. Existing defenses are predominantly agent-centric, relying on the agent itself to detect threats and enforce privacy and security policies. This approach is fundamentally limited because it entrusts policy enforcement to AI agents whose LLM-driven behavior is i...
  </details>

- **2026-08-12** — Yutao Mou, Pengfei Yang, Zhe Yin et al. — [ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents](http://arxiv.org/abs/2608.11878v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents integrated with external tools are vulnerable to indirect prompt injections embedded in environmental states. However, existing studies largely rely on manually implemented or reused environments, stochastic LLM-based tool simulation, and predefined injection locations, limiting scalable security research across broader domains. To bridge this gap, we propose **ToolHazard**, a scalable adversarial environment synthesis framework that reduces human engineering an...
  </details>

- **2026-08-10** — Spiros Tsigkopoulos, Christoforos Ntantogian — [From Prompt Injection to Web Exploitation: Revisiting Classic Vulnerabilities in LLM-Integrated Applications](http://arxiv.org/abs/2608.10281v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models are increasingly integrated into web applications through chatbots, tool-calling pipelines, and agentic workflows. In these systems, user input may influence not only generated text, but also backend actions such as database queries, HTTP requests, file operations, template rendering, or API calls. This paper introduces LLM-mediated web attacks, a class of attacks in which attacker-controlled input is transformed by an LLM-integrated application and then reaches traditional...
  </details>

- **2026-08-10** — Jordan Pettyjohn, Mansi Sakarvadia, Nathaniel Hudson et al. — [Interpreting Language Model Hidden States at Scale](http://arxiv.org/abs/2608.10260v1)
  <details><summary>📄 Abstract</summary>
  Lens methods interpret large language models (LLMs) by mapping intermediate activations to the output vocabulary, revealing how next-token predictions develop through the network. Trained lenses remain expensive: affine-translator parameters grow quadratically with model width, while exact, full-vocabulary Kullback--Leibler (KL) training dominates memory. Consequently, prior trained lenses have been applied to models of at most 20B parameters and remain tied to particular component types. We pre...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 10 papers

- **2026-08-12** — Gen Dong, Yanjie Gao, Liqun Li et al. — [Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents](http://arxiv.org/abs/2608.11888v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are the de facto mechanism for extending LLM agents with reusable guidance. A skill can shape the agent's task execution, including planning, tool use, problem-solving, and validation. Prior work reported mixed results of agent skills: some skills improve task success rates, while others have no effect, increase token use and execution time, and even reduce success rates. This paper presents a comprehensive analysis of skill-induced agent failures by attributing task failures and co...
  </details>

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


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-08-11** — Md. Nahid Hasan, Mohammad Arif Hossain — [An Empirical Study of Output-to-Input Loops for Black-Box Backdoor Detection in Fine-Tuned Open-Weight LLMs](http://arxiv.org/abs/2608.11348v1)
  <details><summary>📄 Abstract</summary>
  Anyone can upload a fine-tuned large language model (LLM) to a public repository and claim it is safe. A backdoored model behaves normally on ordinary inputs until a hidden trigger fires, and a user with no training data, clean reference weights, or the trigger phrase has no clear way to check the model before using it. We introduce and empirically evaluate self-feeding, a black-box test method that feeds a model's own output back as its next input, so the text drifts away from the starting prom...
  </details>

- **2026-08-11** — Gabriel Huang, Abhay Puri, Léo Boisvert et al. — [Backdoor Decontamination Dynamics in LLM Agents](http://arxiv.org/abs/2608.11295v1)
  <details><summary>📄 Abstract</summary>
  Open-weight LLM agents are vulnerable to backdoors installed during fine-tuning, which may be undetectable if the trigger conditions are never met during testing. Assuming defenders do not know the existing trigger, they cannot unlearn it directly. One decontamination strategy is to install a known backdoor (defensive poisoning) then to unlearn it, hoping that the original unknown backdoor is removed as a side effect. However, this procedure has uncertain outcomes: the original backdoor may pers...
  </details>

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
*对抗攻击 / Adversarial Attacks* — 3 papers

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


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-08-12** — Yan Deng, Fei Xu — [DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation](http://arxiv.org/abs/2608.12308v1)
  <details><summary>📄 Abstract</summary>
  Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence over time, plan future actions, and determine when it has reached a navigation goal under partial observability. Although recent VLA models offer a promising perception-to-action paradigm, adapting them to aerial navigation remains challenging due to limited historical context, short planning horizons, and unreliable implicit termination. To address these challenges, we propose DreamFly, a diffusion-b...
  </details>

- **2026-08-12** — Shaohua Li, Cunhua Pan, Hong Ren et al. — [AFDM-ISAC With Fractional Delay-Doppler Coupling](http://arxiv.org/abs/2608.11998v1)
  <details><summary>📄 Abstract</summary>
  Affine frequency division multiplexing (AFDM) is a promising chirp-based multicarrier waveform for high-mobility integrated sensing and communication (ISAC). Accurate angle, delay, and Doppler estimation is essential for AFDM sensing. Since target delays and Doppler shifts are generally continuous-valued, representing them on a discrete delay--Doppler grid causes energy leakage and peak displacement in the discrete affine Fourier transform (DAFT) domain. The AFDM chirp also induces delay--Dopple...
  </details>

- **2026-08-12** — Haokun Lin, Kaijie Zhu, Haobo Xu et al. — [Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed](http://arxiv.org/abs/2608.11981v1)
  <details><summary>📄 Abstract</summary>
  Small Language Models (SLMs) have emerged as a more efficient alternative to traditional Large Language Models (LLMs), offering promising potential in resource-constrained scenarios. Existing approaches to building SLMs typically follow two paths: training compact models from scratch, or compressing larger pre-trained models using methods such as pruning, quantization, or distillation. As language models become increasingly integrated into real-world applications, ensuring their trustworthiness ...
  </details>

- **2026-08-12** — Yifan Zhang, Yu Bai, Riku Jantti et al. — [AmbSentry: Mitigating Sensing Eavesdropping in ISAC Systems by Harnessing Ambient IoT Devices](http://arxiv.org/abs/2608.11799v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing and communication (ISAC) has emerged as a pivotal paradigm for 6G networks, enabling the synergistic convergence of spectral and hardware resources to maximize system efficiency. However, the inherent openness of wireless transmission exposes ISAC systems to critical security risks, particularly regarding the privacy of the sensing information. Unauthorized sensing eavesdroppers can extract sensitive target parameters (e.g., range and velocity) by directly estimating open sens...
  </details>

- **2026-08-12** — Aaron Chatterji, David Holtz, Neel Rakholia et al. — [How Organizations Use AI: Evidence from ChatGPT](http://arxiv.org/abs/2608.12236v1)
  <details><summary>📄 Abstract</summary>
  We study how organizations use frontier generative AI by linking ChatGPT Enterprise account records to usage, worker roles, task classifications, and public-company financial data through March 2026. These linked data enable a privacy-preserving analysis of adoption, worker roles, and message-level tasks at scale: for instance, the worker-level sample we analyze at the six-month adoption horizon includes over 1,500 organizations and over 17 million messages. We document four facts about enterpri...
  </details>

- **2026-08-12** — Alessandra Mancas, Mounir Ammam, Hyacinth Ali et al. — [Towards Automated Domain Model Extraction from Source Code using Heuristics and Open-Source LLMs](http://arxiv.org/abs/2608.12228v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have recently shown strong capabilities for code understanding, making them promising for reverse engineering domain models from source code. However, state-ofthe- art proprietary LLMs cannot be used in many industrial contexts due to privacy and confidentiality constraints, while compact open-source LLMs that can run locally are limited by their context window and cannot process large code bases directly. In this paper, we propose an automated approach to extract do...
  </details>

- **2026-08-12** — Yuanmin Huang, Chen Chen, Geng Hong et al. — [Fingerprinting Text-to-Image Diffusion Models via Collapsed Generation](http://arxiv.org/abs/2608.11732v1)
  <details><summary>📄 Abstract</summary>
  Proprietary text-to-image diffusion models are increasingly distributed as hosted services and downloadable checkpoints, making their intellectual property (IP) protection an increasingly critical concern when model leakage, copying, or unauthorized fine-tuning is disputed. In this work, we present a non-invasive model fingerprinting framework based on \emph{collapsed generation}, a phenomenon where certain input conditions produce highly consistent images across multiple stochastic seeds. We sh...
  </details>

- **2026-08-12** — Yuhao Zhang, O. Ozan Koyluoglu, Thejas Venkatesh et al. — [FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents](http://arxiv.org/abs/2608.11683v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly deployed for professional investment research, yet no benchmark captures the complexity of the full investor workflow. Existing benchmarks mainly target financial data extraction, a narrow slice that current models have largely saturated, while reference-based metrics and generic LLM-as-a-judge scoring fall short on the open-ended, long-form answers that real analyst queries demand. We introduce FrontierFinance, a fully open benchmark of 220 expert-crafted queries and ...
  </details>

- **2026-08-12** — Kegeng Tang, Jingbo Wang, Shaogang Ren et al. — [CT-$Δ$Bench: A Benchmark for Longitudinal 3D Medical Imaging Difference Reporting with Vision-Language Models](http://arxiv.org/abs/2608.11534v1)
  <details><summary>📄 Abstract</summary>
  In medical imaging, the clinical value of Computed Tomography (CT) lies not only in depicting current disease status, but crucially in enabling longitudinal comparison of serial scans to determine disease evolution, a process that underpins response assessment, recurrence detection, and ongoing patient management. Yet, despite this central role of temporal comparison in clinical decision-making, existing medical foundation models remain largely confined to single-study understanding, leaving tem...
  </details>

- **2026-08-11** — Joshua S. Gans — [When Agents Talk: Honeytokens under Shared Memory](http://arxiv.org/abs/2608.11436v1)
  <details><summary>📄 Abstract</summary>
  During a 2026 cyber-capability evaluation, short-lived AI agents turned a shared package repository into persistent memory, passing exploit findings to later agents and rebuilding the channel after it was removed. The broader evaluation culminated in an intrusion into Hugging Face. This episode raises a question for defensive deception: can a honeytoken be harmless to trusted agents without becoming recognisable to an attacker who shares their information and can implement the trusted policy? Th...
  </details>

- **2026-08-11** — Cinara Gomes de Melo Carneiro, Renato de Freitas Bulcão Neto — [Simplifying Requirements Engineering in the Context of the LGPD: An LLM-Based Investigation](http://arxiv.org/abs/2608.11454v1)
  <details><summary>📄 Abstract</summary>
  Compliance with privacy legislation poses a complex challenge to Requirements Engineering (RE): translating legal norms into software requirements. In this context, this study investigates whether Large Language Models (LLMs) can simplify RE within the framework of the Brazilian General Data Protection Law (LGPD). The proposed approach utilizes current legislation to automatically generate User Stories and Acceptance Test Scenarios. The evaluation results demonstrated high performance, confirmin...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 20 papers

- **2026-08-12** — Nimet Beyza Bozdag, Emre Can Acikgoz, Gokhan Tur et al. — [Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs](http://arxiv.org/abs/2608.11624v1)
  <details><summary>📄 Abstract</summary>
  Persuasion is a core dynamic of natural language communication, shaping how large language models (LLMs) update beliefs, resolve disagreements, and reach decisions. As LLMs increasingly debate, advise, and think collaboratively with humans and each other, resistance to harmful persuasion becomes a core requirement for reliable behavior. Yet we show that this requirement is far from met: a single targeted persuasive argument is enough to collapse model accuracy to near zero, even when the argumen...
  </details>

- **2026-08-12** — Lang Cao — [Making Your LLMs More Objective: Stabilizing LLM Safety Behavior Across Traits with Trait-Invariant Safety Tuning](http://arxiv.org/abs/2608.11705v1)
  <details><summary>📄 Abstract</summary>
  Aligned large language models (LLMs) are expected to exhibit safety behavior based on the content of the user request: they should refuse unsafe requests and comply with safe ones. However, we show that the same request can elicit substantially different safety decisions under different traits assigned in the system prompt, a failure mode we call trait-induced safety variation. To measure this failure, we introduce refusal-based metrics: Trait-Induced Deviation measures dataset-level deviation f...
  </details>

- **2026-08-12** — Shivank Singh Thakur, Meien Li, Mark Stamp — [Robustness of AI-Art Detectors under Generator Shift](http://arxiv.org/abs/2608.11643v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image generative models have advanced rapidly, with modern Diffusion Transformer architectures producing images that are increasingly difficult to distinguish from human-created artwork. This development has raised significant concerns regarding copyright protection, misinformation, fraud, impersonation, and the authenticity of digital content. Most AI-art detectors are trained and evaluated on the same generator family, leaving robustness to newer architectures underexplored. In this ch...
  </details>

- **2026-08-12** — Ning Lin, Jiacheng Cen, Anyi Li et al. — [Reducing Symmetry Increase in Equivariant Neural Networks](http://arxiv.org/abs/2608.12010v1)
  <details><summary>📄 Abstract</summary>
  Equivariant Neural Networks (ENNs) have empowered numerous applications in scientific fields. Despite their remarkable capacity for representing geometric structures, ENNs suffer from degraded expressivity when processing symmetric inputs: the output representations are invariant to transformations that extend beyond the input's symmetries. The mathematical essence of this phenomenon is that a symmetric input, after being processed by an equivariant map, experiences an increase in symmetry. Whil...
  </details>

- **2026-08-12** — Vibha Bhavikatti, Mark Stamp — [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](http://arxiv.org/abs/2608.12077v1)
  <details><summary>📄 Abstract</summary>
  Recent studies have shown that binary-to-image representations can enable effective machine learning-based results for malware detection and classification. However, performance can vary significantly, depending on the technique used to convert binaries to images. Furthermore, the explainability and interpretability of image-based models is largely unexplored within the malware domain. In this research, we employ Gradient-weighted Class Activation Maps (Grad-CAM) as an eXplainable AI (XAI) tool,...
  </details>

- **2026-08-11** — Valentin Rodionov, Shamil Assylbekov — [TRACES: A Benchmark for Epistemic Reliability in Scientific Reasoning by LLMs](http://arxiv.org/abs/2608.11415v1)
  <details><summary>📄 Abstract</summary>
  Large language models are being proposed as agents in scientific workflows, in domains where no downstream verifier exists. Such deployment assumes the model can distinguish reliable scientific literature from unreliable literature, a capability that has not yet been directly measured. Existing benchmarks evaluate factuality on questions with known answers; the failure mode we target here is different. We introduce a probe corpus of 42 retracted, fraudulent, and pseudoscientific papers, paired w...
  </details>

- **2026-08-11** — Hangqi Ren, Junyi Liao — [Unmasking Toxic Mimicry in Medical Offline Reinforcement Learning for ICU Sepsis Management via Counterfactual Clinical Audits](http://arxiv.org/abs/2608.11410v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning (RL) offers considerable promise for optimizing ICU treatment decisions, yet standard evaluation metrics Mean Squared Error (MSE) and Fitted Q-Evaluation (FQE) assess only behavioral imitation and cannot detect Toxic Mimicry, a failure mode in which agents replicate harmful patterns such as treatment withdrawal during comfort-care transitions. Using the MIMIC-III database, we propose the Counterfactual Clinical Audit (CCA) framework, which stress-tests RL agents th...
  </details>

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
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 63 papers

- **2026-08-12** — Simon Yu, Nicholas Tomlin, Marwa Abdulhai et al. — [One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL](http://arxiv.org/abs/2608.12253v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reinforcement learning for human-AI interaction typically relies on a single large language model to simulate user behavior. We show that this approach systematically fails to generalize, and trace the failure to simulator collapse: because the simulator LLM is mode-collapsed, an LLM policy trained against it overfits to narrow strategies that exploit the simulator's dominant mode, and such a policy transfers poorly to unseen simulators and real users. We formalize this collapse theo...
  </details>

- **2026-08-12** — Jin Lu, Xuening Han, Yang Zhong et al. — [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](http://arxiv.org/abs/2608.12246v1)
  <details><summary>📄 Abstract</summary>
  Evaluating security vulnerability detection tools requires benchmark datasets with vulnerability-inducing commits (VICs) - the commits that first introduce vulnerabilities into codebases. VICs are essential for determining the full range of vulnerable software versions. Existing vulnerability datasets suffer from limited programming language coverage, restricted patch complexity, and narrow project scope. Through our dual annotation by human experts and an agentic workflow, we create a benchmark...
  </details>

- **2026-08-12** — Fenglin Yan, Bohao Wang, Jian Zhang et al. — [Making Collaborative Signals Count: Graph-Aware Large Language Models for Sequential Recommendation](http://arxiv.org/abs/2608.12184v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have been widely adopted as backbones for recommender systems. However, their language-centric pretraining makes it difficult to capture collaborative signals implicit in user-item interactions, which are crucial for personalized recommendation. Existing methods either inject collaborative representations produced by external recommenders or model only intra-sequence dependencies, limiting their ability to exploit global collaborative patterns. To address this limita...
  </details>

- **2026-08-12** — Davide Cozzolino, Giovanni Poggi, Luisa Verdoliva — [Understanding Why Foundation Models Work for Diffusion-Generated Image Detection](http://arxiv.org/abs/2608.12155v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models have recently emerged as powerful feature extractors for detecting AI-generated images, achieving strong generalization across generators and robustness to common image degradations. However, the reason behind their effectiveness is poorly understood. In this work, we investigate what cues are exploited by foundation-model-based detectors to distinguish real images from diffusion-generated ones. To this end, we design an ad hoc analysis protocol based on DDIM inversion. ...
  </details>

- **2026-08-12** — Nikolette Pedersen, Regitze Sydendal, Veronika Cheplygina et al. — [Look What the Probes Dragged In! Real-World Chest X-ray Shortcuts in MedCLIP](http://arxiv.org/abs/2608.12086v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models, such as contrastive language-image pre-training (CLIP)-based approaches, have reached state-of-the-art (SOTA) results in medical artificial intelligence. However, recent work reveals that CLIP-based models remain vulnerable to shortcuts. We investigate how real-world shortcuts manifest across different layers of the medical CLIP-based model, MedCLIP, and its vision encoder, a frozen ResNet-50. We attach 17 linear classification probes to the intermediate layers of the Res...
  </details>

- **2026-08-12** — Jinjun Huang, Zhongzhen Wen, Tongtong Xu et al. — [RealisticTritonBench: A Benchmark for Triton-Kernel Generation in Real-World AI Frameworks](http://arxiv.org/abs/2608.12004v1)
  <details><summary>📄 Abstract</summary>
  In modern AI frameworks, GPU kernels are key to overall system performance. Combining usability, portability, and near-handwritten CUDA performance, Triton is widely adopted for implementing GPU kernels. Recent advances show the potential of large language models (LLMs) to automatically generate Triton kernels, reducing the manual effort required from expert kernel developers. Several benchmarks evaluate LLM-generated Triton kernels. However, they suffer from three key limitations: (1) they rest...
  </details>

- **2026-08-12** — Sen Xu, Wei Wang, Shixi Liu et al. — [Claim-Level Reliability Assessment for Efficient Test-Time Reasoning](http://arxiv.org/abs/2608.11994v1)
  <details><summary>📄 Abstract</summary>
  We propose claim-level falsification as a principle for test-time scaling and instantiate it through Claim-Level Reliability Assessment (CLR), a training-free framework that reallocates test-time compute from additional solution sampling to targeted verification. Since whole-trace evaluation often obscures decisive errors due to signal dilution from routine tokens, CLR condenses each reasoning trace into a compact set of decision-critical claims, thereby isolating its logical anchors. Furthermor...
  </details>

- **2026-08-12** — Sanghun Shin, Sangyeon Kim, Gisan Ji et al. — [NITRO: High-Performance 3D NAND Flash-Based In-Storage Computing with Enhanced Activation Dataflow](http://arxiv.org/abs/2608.11920v1)
  <details><summary>📄 Abstract</summary>
  In-storage computing (ISC) is considered a next-generation memory architecture for its ability to relieve the data bottleneck between the host and the memory. While the required resources of large language models (LLMs) have increased significantly in recent years, the memory density has not scaled accordingly. Recently, several works have studied NAND flash-based processing-in-memory (NAND-PIM) schemes to exploit the high density of the memory. However, they do not address the dataflow/buffer f...
  </details>

- **2026-08-12** — Rahul Nair, Bastian Lipka, Elizabeth Daly — [Policy-as-logic for robust reasoning over rules](http://arxiv.org/abs/2608.11905v1)
  <details><summary>📄 Abstract</summary>
  In many practical applications of generative AI systems, from tax rules to airline baggage allowance, responses to natural language queries must respect written policies or rules. We present a hybrid symbolic approach that expresses policies in formal logic and at inference time exploits the representation power of language models for fact extraction to ground predicates, and an answer set solver for reasoning such that responses are interpretable, auditable, and as we show, accurate and robust ...
  </details>

- **2026-08-12** — Jiazhen Dong, Lei Liu, Xiaojun Yuan et al. — [A Universal Random Precoding Framework for MIMO Systems](http://arxiv.org/abs/2608.11828v1)
  <details><summary>📄 Abstract</summary>
  Current wireless systems combat inter-symbol interference (ISI) by diagonalizing or sparsifying the channel matrix, yet they remain vulnerable to selective fading. To address this, we propose a universal random precoding (RP) transmission framework based on the universality class. RP leverages random transforms to statistically exploit all subchannels and construct an equivalent channel belonging to the universality class, thereby enhancing diversity gain while maintaining backward compatibility...
  </details>

- **2026-08-12** — Yushi Ye, Xu Chen, Haoyun Jiang et al. — [Ripple-Pivot Search: Active Parallel Decoding for Diffusion Large Language Models](http://arxiv.org/abs/2608.11742v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive language models, offering the potential for substantially faster inference through parallel decoding. Existing parallel decoding schedulers typically commit positions only after they meet a per-position criterion, overlooking how early commitments may benefit subsequent decoding. We identify a ripple effect in dLLM decoding: proactively committing a mid-entropy pivot position can induce a pronounc...
  </details>

- **2026-08-12** — Debanjan Dutta, Anish Chakrabarty, Swagatam Das — [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](http://arxiv.org/abs/2608.11716v1)
  <details><summary>📄 Abstract</summary>
  Chain of Thought (CoT) lifts the expressive ceiling of bounded-depth Transformers, with characterizations tying the number of CoT steps to circuit complexity classes. What remains largely missing are concrete instantiations with explicit, depth-bounded constructions, and the traversal procedures such characterizations presuppose. We close this gap for branching complexity. We give CoT realizations of depth-first search (DFS) and of Dijkstra algorithm, the latter subsuming breadth-first search, b...
  </details>

- **2026-08-12** — Minglai Yang, Xinyu Guo, Utkarsh Tyagi et al. — [Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL](http://arxiv.org/abs/2608.11669v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning against rubrics, lists of criteria graded by an LLM judge, has become a standard way to post-train language models on tasks with no deterministic answer. The rubric, however, is a fixed proxy for quality, never a complete description of it, and a policy trained against it long enough will learn to exploit the difference. We measure this directly. Training Qwen3-8B with Group Relative Policy Optimization (GRPO) on medical and science rubrics and grading out-of-distribution ...
  </details>

- **2026-08-12** — Daifeng Peng, Yuanke Peng, Haiyan Guan — [Zero-OVCD: Bridging Training-Free Foundation Models and Pseudo-Label Learning for Open-Vocabulary Change Detection](http://arxiv.org/abs/2608.11663v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary change detection (OVCD) enables the identification of user-specified land-cover changes in bitemporal remote sensing images, but existing training-free pipelines remain vulnerable to inaccurate candidate masks, ambiguous semantic assignments, and accumulated inference errors. To address these issues, we propose Zero-OVCD, a two-stage framework that requires no pixel-level annotations from the target domain. In the first stage, high-quality change pseudo-labels are generated throu...
  </details>

- **2026-08-12** — Oshan A. B. Yalegama, Wageesha N. Manamperi — [Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones](http://arxiv.org/abs/2608.11627v1)
  <details><summary>📄 Abstract</summary>
  The Relative Transfer Matrix (ReTM), recently introduced as a generalization of the relative transfer function for multiple receivers and sources, shows promising performance when applied to speech enhancement in noisy environments. Estimating the ReTM of sound sources by exploiting the covariance matrices of multichannel recordings is highly beneficial for practical applications and, to date, remains the only proposed approach. This paper investigates deep learning-based ReTM estimation. We pro...
  </details>

- **2026-08-12** — Daowen Li, Ding Ding, Zifu Zhang et al. — [Generative Video Compression Based on Hierarchical Referencing](http://arxiv.org/abs/2608.11618v1)
  <details><summary>📄 Abstract</summary>
  Diffusion-based generative video compression has emerged as a promising paradigm to improve perceptual quality, where latent frames are required to be encoded efficiently while serving as denoising conditions. However, existing methods neither carefully design reference and quality structures during latent coding nor account for the impact of frame-level quality variation on denoising procedure, which limits coding efficiency and aggravates artifact propagation during generative reconstruction. ...
  </details>

- **2026-08-12** — Zhaohui Yang, Yuwei Han, Ruiyun Zhang et al. — [Efficient Compilation for Hamiltonian Simulation via Global Binary Symplectic Form Simplification](http://arxiv.org/abs/2608.11579v1)
  <details><summary>📄 Abstract</summary>
  Hamiltonian simulation is a core quantum workload, underpinning variational quantum algorithms and Trotterized time evolution. Such programs are expressed as Pauli exponential sequences, exhibiting structural patterns that are highly amenable to high-level synthesis and optimization. Existing compilers, however, fail to fully unlock the optimization potential of their global algebraic structure, even when employing advanced graph- or tableau-based methods.   We present Symphony, a holistic compi...
  </details>

- **2026-08-12** — Jie Hong, Tingtian Li, Xuesong Li et al. — [Repurposing RGB-based Foundation Model for Depth Estimation on Thermal Images Using Hierarchical Supervision](http://arxiv.org/abs/2608.11564v1)
  <details><summary>📄 Abstract</summary>
  Depth estimation from thermal images is highly valuable for robotic applications in adverse conditions, such as nighttime and rainy weather. Recent studies have sought to transfer knowledge from RGB-based foundation models to thermal modalities, yet the rich hierarchical representations these models encode remain underutilized. To address this limitation, we propose RGB-HS, a novel framework for thermal-image depth estimation that leverages hierarchical supervision from an RGB-based foundation m...
  </details>

- **2026-08-12** — Chentao Yue, Gaoyang Pang, Branka Vucetic et al. — [Semantic Error Control Coding with Foundation Models for Future Communications](http://arxiv.org/abs/2608.11551v1)
  <details><summary>📄 Abstract</summary>
  Classical channel decoding typically treats all information sequences as equally likely and relies primarily on the channel observations and code structure, without exploiting statistical or semantic structure in the source data. Although source compression is designed to remove redundancy, practical source coding can leave substantial residual structure that conventional channel decoders do not exploit. Modern multimodal data sources, including text, speech, and images, exhibit rich statistical...
  </details>

- **2026-08-11** — Christophe Kolb, Jim Caron — [Cheap, Fallible Cognition and the Political Economy of Expertise](http://arxiv.org/abs/2608.11512v1)
  <details><summary>📄 Abstract</summary>
  The question of whether artificial intelligence will "destroy jobs" is too coarse to guide economic analysis or institutional design. A job is not an indivisible object, and machine cognition is not a uniform substitute for human labor. This paper develops a task-based and institutionally grounded framework for analyzing generative AI as cheap, scalable, and fallible cognition. The relevant margins are exposure, adoption, verification, question selection, workflow redesign, demand elasticity, ap...
  </details>

- **2026-08-11** — Tal Oved, Roi Pony, Oshri Naparstek et al. — [Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization](http://arxiv.org/abs/2608.10694v2)
  <details><summary>📄 Abstract</summary>
  Evolutionary optimization of LLM prompts and agentic programs (e.g., GEPA) is dominated by fitness evaluation: scoring each candidate runs an answering LLM over a validation set, so the evaluator's price tier dictates total search cost. We restructure that search by decoupling the three roles an LLM plays, running the high-volume answering role on the cheapest tier, reserving a strong model for the rare reflection/variation operator, then exploiting upward cross-tier transfer to deploy the cheap...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 56 papers

- **2026-08-12** — Zhuoyang Qian, Biao Wu, Yiran Wang et al. — [Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill](http://arxiv.org/abs/2608.11924v1)
  <details><summary>📄 Abstract</summary>
  Turning a research idea into a complete paper requires more than text generation: the system must retrieve literature, design and execute experiments, revise claims according to evidence, produce publication-ready figures, and maintain consistency across a long generation process. We present Spark-to-Paper, an end-to-end research paper generation system implemented as thirteen composable skills inside an existing coding assistant, without requiring a separate agent platform or orchestration serv...
  </details>

- **2026-08-12** — Ankita Rajaram Naik, Anupama Murthi, Benjamin Elder et al. — [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](http://arxiv.org/abs/2608.12282v1)
  <details><summary>📄 Abstract</summary>
  Agents deployed in enterprise settings must reason across structured APIs and document collections, yet existing benchmarks evaluate these capabilities in isolation. We introduce VAKRA (e\textbf{V}aluating \textbf{A}PI and \textbf{K}nowledge \textbf{R}etrieval \textbf{A}gents), a benchmark of over $8{,}000$ executable APIs across $62$ domains with tasks spanning three settings of increasing difficulty: diverse API interaction styles, multi-hop reasoning over structured APIs, and multi-source rea...
  </details>

- **2026-08-12** — Karl Hanna, Chen Feng — [Accuracy and Order Sensitivity Diverge Under Label-Free Strategies](http://arxiv.org/abs/2608.11947v1)
  <details><summary>📄 Abstract</summary>
  Multiple-choice benchmarks are widely used to evaluate large language models, but MCQ scores conflate knowledge with sensitivity to option order, which makes them unreliable measures of model knowledge. In this paper, we test whether preventing a model from seeing option labels while committing to an answer removes positional influence and, in turn, improves performance. We evaluate two different strategies for mitigating bias. The first uses a generation-then-matching approach, and the second s...
  </details>

- **2026-08-12** — Shuangqing Zhang, Lei-Lei Ma, Zhao Wang et al. — [TD-VAD: Breaking Visual Dependence in Video Anomaly Detection with Text-Driven Learning](http://arxiv.org/abs/2608.11820v1)
  <details><summary>📄 Abstract</summary>
  Visual data is typically a prerequisite for training existing video anomaly detection (VAD) methods. However, obtaining sufficient annotated anomaly data for training is challenging and not scalable due to the rarity of anomaly data and the wide variety of abnormal events. In this work, we advocate that the effectiveness of treating texts as video sequences for the VAD model and propose a novel Text-Driven Video Anomaly Detection (TD-VAD) approach to break visual dependence. In contrast to the a...
  </details>

- **2026-08-12** — Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò et al. — [Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs](http://arxiv.org/abs/2608.12179v1)
  <details><summary>📄 Abstract</summary>
  Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dom...
  </details>

- **2026-08-12** — Touseef Hasan, Mounika Ghanta, Souvika Sarkar et al. — [AgenticTwin: An Agentic LLM Framework Integrated with Digital Twin for Anomaly Detection](http://arxiv.org/abs/2608.11679v1)
  <details><summary>📄 Abstract</summary>
  Digital twins are increasingly used to monitor and simulate the behavior of cyber-physical systems. Even with skilled operators, interpreting anomalies detected within digital twin pipelines is challenging, as the sheer complexity and volume of raw sensor data make thorough analysis difficult. Recent advances in large language models (LLMs) offer promising capabilities for reasoning and explanation, yet their integration into digital twin-driven anomaly analysis remains underexplored. In this wo...
  </details>

- **2026-08-11** — Zirui Song, Huaxing Liu, Xiang Wang et al. — [Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning](http://arxiv.org/abs/2608.11408v1)
  <details><summary>📄 Abstract</summary>
  Prior white-box studies show that large language models can retain latent traces of target knowledge after unlearning, even when the knowledge is no longer expressed in their outputs. However, existing audits remain limited to one-off diagnostics: it is unclear whether these residual signals can predict future recovery under continued training or serve as reliable optimization targets. Resolving this gap is essential to determine whether internal auditing can move beyond post-hoc evaluation towa...
  </details>

- **2026-08-11** — Josh Dafoe, Niusen Chen, Bo Chen — [A Runtime Decentralized Attestation and Coordinated Repair Framework for Securing Automotive ECUs](http://arxiv.org/abs/2608.11489v1)
  <details><summary>📄 Abstract</summary>
  The evolution of automotive technology increasingly integrates components, transforming vehicles into interconnected systems of systems. Modern vehicles are controlled by a distributed system of computing devices, known as electronic control units (ECUs). However, this interconnectedness means that any error poses significant risks to the vehicle operator. In particular, malware can be injected into ECUs, threatening vehicle safety. To address this, we need mechanisms to detect compromised ECUs ...
  </details>

- **2026-08-11** — Elias Grünewald, Daniil Cherepko, Linus Gustafsson et al. — [An Event-Driven Cloud-Native Wearable Analytics Framework for Real-Time Clinical Workloads](http://arxiv.org/abs/2608.11402v1)
  <details><summary>📄 Abstract</summary>
  Continuous physiological monitoring using consumer-grade wearables offers a transformative opportunity for clinical care and research, yet integration remains hindered by device heterogeneity, proprietary data formats, and strict regulatory requirements. We present an event-driven, cloud-native system designed to ingest, normalize, and analyze high-frequency vital signs from wearables at scale and without vendor lock-in. The system design proposes a multi-layered microservice architecture using ...
  </details>

- **2026-08-11** — Ted Kwartler, Alan Aqrawi, Arian Abbasi — [AI Guardrail Survival under Single-Cycle Agentic Self-Summarization](http://arxiv.org/abs/2608.11392v1)
  <details><summary>📄 Abstract</summary>
  Long-running agents periodically compact their context, replacing the transcript with a model-generated summary.Recent work shows that dropping a standing safety constraint during compaction drives behavioral violations acrossmany models (Governance Decay; Chen, 2026). We ask a finer question: under a single compaction cycle, how is a safetyrule lost, and what does that imply for detection and evaluation? Our central finding is that a presence check is not asafety check: when compaction does not...
  </details>

- **2026-08-11** — Vasundra Srinivasan — [Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations](http://arxiv.org/abs/2608.11323v1)
  <details><summary>📄 Abstract</summary>
  Enterprise practitioners read agent leaderboards as if they ranked agent capability. We show, across three open agent-trace benchmarks (TheAgentCompany, $τ^2$-bench, and AppWorld), that the agent main effect accounts for less than 3% of total variance in every dataset and check type, while the agent-by-task interaction accounts for 7-23%. Leaderboards rank specialization, not capability. We arrive at this through a four-facet Generalizability Theory variance decomposition, fit with three estimat...
  </details>

- **2026-08-11** — Albus W. Ng, Yi Han, Jusheng Zhang et al. — [Agent Safety Should Be a Runtime Contract](http://arxiv.org/abs/2608.11274v1)
  <details><summary>📄 Abstract</summary>
  The dominant paradigm treats AI safety as a property to be instilled during model training via RLHF, DPO, or Constitutional AI. We argue this is structurally insufficient for autonomous agents that execute code, mutate files, send messages, and modify databases. Agent safety should be a runtime contract enforced by the harness, and the contract has two complementary faces. The preventive face blocks dangerous actions before they happen via sandboxes, permission gates, output filters, and traject...
  </details>

- **2026-08-11** — Christopher Brown, Michael Spannowsky, Simon Williams — [Robust Quantum Machine Learning for Collider Event Selection under Detector Variability](http://arxiv.org/abs/2608.11330v1)
  <details><summary>📄 Abstract</summary>
  Robust machine-learning methods are becoming increasingly important for high-energy physics data analysis as experiments enter the era of higher luminosity and future higher-energy colliders. Detector degradation, changing running conditions and calibration drift can shift data distributions, causing models trained on clean reference samples to degrade after deployment. We investigate whether parameterised quantum models provide a useful inductive bias for robust collider-event selection in two ...
  </details>

- **2026-08-11** — Hamza Ouarrad, Mohammad Abboush, Andreas Rausch — [Knowledge-Graph-Guided Retrieval-Augmented LLMs for Explainable Root Cause Analysis in Automotive HiL Validation](http://arxiv.org/abs/2608.11277v1)
  <details><summary>📄 Abstract</summary>
  Hardware-in-the-Loop validation of automotive software systems generates large multivariate time-series recordings whose manual analysis is time-consuming and often limited to anomaly detection and fault classification rather than root-cause analysis. Although deep learning methods have shown strong performance in fault detection and classification, they usually require task-specific training or retraining when new fault locations, systems, or operating conditions are introduced. They also tend ...
  </details>

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

- **2026-08-10** — Tadanobu Chuyo Kamijo, Ori Rottenstreich, Javier Conde et al. — [Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness](http://arxiv.org/abs/2608.09900v2)
  <details><summary>📄 Abstract</summary>
  Large language model evaluations typically focus on performance under nominal conditions, creating an illusion of capability where models comfortably walk a narrow, highly optimized generation corridor. In real-world deployments, however, complex system prompts, safety guardrails, and structural constraints continuously force models off this nominal path, driving a divergence between benchmark scores and deployment performance. To address this issue, we introduce Decoding-Level Taboo, a zero-pro...
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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 55 papers

- **2026-08-12** — Youze Huang, Penghui Ruan, Bojia Zi et al. — [ScaleVid: Geometry-Aware Video Object Scaling with Mesh-Free Inference](http://arxiv.org/abs/2608.12232v1)
  <details><summary>📄 Abstract</summary>
  Geometry-aware video object scaling aims to anisotropically resize the object along object-centric axes while preserving geometric plausibility, temporal coherence, and background consistency. Existing text-guided methods mainly operate in the 2D image plane, while depth-guided approaches provide coarse control and mesh-based methods require costly 3D reconstruction. We present a progressive two-stage training framework that decouples geometry-aware foreground transformation from background pres...
  </details>

- **2026-08-12** — Kangning Zhang, Haotian Fang, Xukun Luo et al. — [HCGRec: Hint-Conditioned Generative Recommendation with Semantic IDs](http://arxiv.org/abs/2608.11980v1)
  <details><summary>📄 Abstract</summary>
  Semantic-ID generative recommenders represent each item as a short sequence of discrete semantic tokens and predict the next item by autoregressively generating this token sequence. This paradigm enables a unified generation interface for item IDs, histories, and item text, but it also creates a structured optimization bottleneck during reward-based post-training: when an early semantic token enters the wrong branch of the item-token space, finite rollout groups rarely reach the ground-truth ite...
  </details>

- **2026-08-12** — Fang Guo, Qi Zhu, Rongcan Pei et al. — [Sci-Surf: Navigating Scientific Literature Discovery through Human Feedback and Intelligent Summarizatio](http://arxiv.org/abs/2608.11973v1)
  <details><summary>📄 Abstract</summary>
  The rapid growth of scientific publications makes it increasingly difficult for researchers to identify relevant new studies and effectively comprehend them. Existing academic discovery platforms typically rely on static topic subscriptions or embedding-based similarity and provide only abstracts or short summaries, offering limited support for nuanced intent modeling and in-depth paper summarization. We present Sci-Surf, an intent-centric knowledge discovery system that integrates feedback-driv...
  </details>

- **2026-08-12** — Thomas A. Pollak, Hamilton Morrin, Murray Shanahan — [Philosophical vertigo with artificial intelligence](http://arxiv.org/abs/2608.11955v1)
  <details><summary>📄 Abstract</summary>
  Large language models are already adept at engaging users in long, emotionally salient conversations across ordinary and existential domains. They are also capable of inducing a potent sense of connection with a human-like entity, even when the user knows their interlocutor is artificial. For some users, these conversations can unsettle assumptions about mind, reality, agency and authority, producing forms of ontological shock and epistemic destabilisation in which inherited criteria become newl...
  </details>

- **2026-08-12** — Wenshuo Peng, Kaipeng Zhang — [HarmoniDPO: Video-guided Audio Generation via Preference-Optimized Diffusion](http://arxiv.org/abs/2608.11913v1)
  <details><summary>📄 Abstract</summary>
  Video-to-audio (V2A) generation faces significant challenges in achieving precise temporal synchronization and high perceptual quality due to the complex, ambiguous relationship between visual and auditory cues. Existing methods typically compress video inputs into single feature representations, leading to significant loss of temporal dynamics and fine-grained visual information. These approaches also rely on reconstruction-based training objectives that poorly correlate with human perceptual j...
  </details>

- **2026-08-12** — Guang Yang, Fengchen Liu, Alex Wang et al. — [How China-Origin Vision-Language Models Move from Refusal to Reframing in State Alignment](http://arxiv.org/abs/2608.11816v1)
  <details><summary>📄 Abstract</summary>
  State-aligned distortion has been documented in China-origin text-based large language models (LLMs), but whether, and in what form, it arises in multimodal systems has not been systematically examined. We construct a balanced benchmark of 200 core entries spanning ten politically sensitive topics, plus a seven-variant visual-abstraction probe, and run nine vision-language models (VLMs), seven China-origin and two non-China, across four elicitation paradigms and two prompt languages, yielding 21...
  </details>

- **2026-08-12** — Duy Tran Thanh, Yeejin Lee, Byeongkeun Kang — [Learning from Multimodal Pseudo-Labels for Robust Open-Vocabulary Instance and Panoptic Segmentation](http://arxiv.org/abs/2608.11681v1)
  <details><summary>📄 Abstract</summary>
  This work addresses the challenge of open-vocabulary instance segmentation (OVIS) and open-set panoptic segmentation (OSPS), which aim to recognize both predefined and unseen object categories without exhaustive human annotations. Existing methods often suffer from noisy pseudo-masks, limited visual-textual grounding, and difficulty handling synonyms or out-of-vocabulary (OOV) words. To overcome these challenges, we propose a multimodal framework that leverages pre-trained vision-language models...
  </details>

- **2026-08-12** — Myeong-Ju Cho, Hye-Bin Shin, Seo-Hyun Lee et al. — [Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models](http://arxiv.org/abs/2608.11656v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in EEG foundation models have demonstrated the potential of large-scale pretraining to enable generalizable neural decoding across subjects, recording environments, and datasets. However, dominant pretraining paradigms face key challenges: masked autoencoding tends to prioritize low-level signal reconstruction over task-relevant semantics, while autoregressive modeling creates a mismatch between continuous neural dynamics and discrete token spaces. To address these challenges, ne...
  </details>

- **2026-08-12** — Kuangzhao Yang, Ziliang Zhao, Zhicheng Dou — [CLAIM: Leading Open-domain Active Clarification of Large Language Models with Uncertainty Measurement](http://arxiv.org/abs/2608.11631v1)
  <details><summary>📄 Abstract</summary>
  In open-domain human-computer interaction scenarios, large language models (LLMs) frequently encounter user queries that are ambiguous or incomplete. In such cases, directly producing an answer often leads to overgeneralized, erroneous, or low-information responses. In contrast, asking clarifying questions can substantially improve interaction quality. However, existing approaches still rely heavily on manually annotated data or preference alignment to address two fundamental challenges: when cl...
  </details>

- **2026-08-12** — Rentao Gu, Yihang Ding, Junjie Li et al. — [FM-LLM: A frequency-enhanced mixture-of-experts framework for adapting LLMs to time series forecasting](http://arxiv.org/abs/2608.11623v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Large Language Models (LLMs) have spurred cross-modal solutions for time-series forecasting. However, existing methods rely heavily on textual prompts for modality alignment-introducing nontrivial computational overhead and failing to leverage the rich spectral dynamics inherent in time-series data. To enable prompt-free, frequency-aware adaptation of frozen LLMs, we propose FM-LLM (Frequency-Enhanced Mixture-of-Experts for adapting LLMs to Time Series Forecasting), an autoreg...
  </details>

- **2026-08-12** — Haobo Zhang, Kelong Mao, Sulong Xu et al. — [Learning from Online User Feedback for Shopping Agents](http://arxiv.org/abs/2608.11604v1)
  <details><summary>📄 Abstract</summary>
  Large language model-based shopping agents are increasingly deployed in real-world e-commerce platforms, generating massive amounts of user interaction logs that provide valuable supervision for improving these agents. However, existing approaches primarily rely on offline training signals, such as user-item interactions or synthetic preference data, while largely overlooking the rich supervision contained in users' natural conversational feedback. Moreover, the available online feedback is hete...
  </details>

- **2026-08-12** — Mingyu Zong, Sampad Mohanty, Bhaskar Krishnamachari — [Localizing Safety Alignment: MLP Layers and Mid-Network Blocks Encode Refusal Behavior in Large Language Models](http://arxiv.org/abs/2608.11583v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models is often treated as a distributed property of the entire network, yet its practical brittleness suggests that refusal behavior may be concentrated in a smaller set of parameters. This work addresses where safety-aligned refusal is encoded by transplanting weights from aligned models into matched unaligned base models at multiple levels of granularity. Using two open-weight model pairs and four safety benchmarks, we conducted experiments to compare the ef...
  </details>

- **2026-08-12** — Shinji Yamashita, Yuma Kinoshita, Hitoshi Kiya — [Alignment of Similarity-Transformed Images Based on Fourier--Mellin Transform Using Auxiliary Function Method](http://arxiv.org/abs/2608.11565v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an algorithm for estimating the similarity transformation, namely translation, scale, and rotation, between two images with subpixel accuracy. Image registration is a fundamental technique for aligning images acquired under different viewpoints and imaging conditions, and a representative approach based on maximizing discrete cross-correlation is the Fourier--Mellin registration. However, the Fourier--Mellin approach often fails to achieve sufficient alignment accuracy when s...
  </details>

- **2026-08-12** — Haokai Zhao, Yunze Xiao, Weihao Xuan et al. — [Group Alignment-Induced Sycophancy: A Two-Sided Evaluation of Steerable Pluralistic Alignment](http://arxiv.org/abs/2608.11528v1)
  <details><summary>📄 Abstract</summary>
  Group alignment adapts a language model to a demographic group to produce responses that reflect the group's opinions, values, and preferences. Sycophancy, a well-documented by-product of alignment, causes the model to over-agree with the user regardless of factual and objective information. However, existing group alignment methods and evaluations focus only on how closely the model matches the group's opinions, overlooking the induced change in sycophantic behaviour. To bridge this gap, we int...
  </details>

- **2026-08-11** — Alireza S. Ziabari, Kat Ellis, Colleen Chan et al. — [From Prompting to Behavioral Alignment: Personalized LLM Judges for Recommendation Evaluation](http://arxiv.org/abs/2608.11493v1)
  <details><summary>📄 Abstract</summary>
  Traditional offline recommendation evaluation relies heavily on complex, manually maintained feature pipelines that are difficult to scale. While Large Language Models (LLMs) offer a promising alternative by predicting user engagement directly from raw text logs, empirical analysis in this study identifies a critical failure mode termed bidirectional rationalization. In a zero-shot setting, LLMs are found to convincingly argue for both positive and negative user engagement outcomes on the exact ...
  </details>

- **2026-08-11** — Simón Patiño Idarraga, Erick Silva, Rehana Yasmin et al. — [Herding End-to-End Autonomous Driving via Neuro-Symbolic Safety Guards](http://arxiv.org/abs/2608.11451v1)
  <details><summary>📄 Abstract</summary>
  Modern end-to-end driving agents can achieve high average performance yet still violate basic traffic rules that a human driver would never miss. The reason is structural: they learn statistical patterns rather than the physical conditions that guarantee safe driving, leaving their decision-making process opaque and safety constraints unenforced. We introduce a neuro-symbolic safety guard, a lightweight module that attaches to the final command interface of an already-trained agent. Immediately ...
  </details>

- **2026-08-11** — Alexandrine Fortier, Hazel Chen, Peter West — [Is Convergence Inevitable? Tracing Output Homogeneity Back to Base Models](http://arxiv.org/abs/2608.11426v1)
  <details><summary>📄 Abstract</summary>
  The lack of diversity in LM content is widely attributed to the alignment process, but how and where exactly in the pipeline this collapse begins is unknown. We argue that output homogeneity is likely learned during the pretraining phase, and only \emph{revealed} or magnified during the alignment process. Specifically, we find that semantic convergence is observed from the first alignment stage--the instruction-tuning phase (SFT)--suggesting that homogeneity might already exist in the pre-alignm...
  </details>

- **2026-08-11** — Mengyu Chen, Feiyu Lu, Chun-Fu Chen et al. — [Inverse Theory of Mind Modeling for Content Recommendation: From Web Browsing to Dynamic Intelligent Interfaces](http://arxiv.org/abs/2608.11354v1)
  <details><summary>📄 Abstract</summary>
  Modern recommender systems treat observed actions as reliable proxies for user preferences, yet interactions often reflect exploration or comparison rather than stable preference expression. As interfaces evolve from static layouts toward generative UIs and immersive extended reality (XR), the need for deeper, modality-agnostic user understanding grows: these adaptive environments must decide not only what to present but where, when, how prominently, and most importantly why a user acts. We prop...
  </details>

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

- **2026-08-10** — Alvin Spivey, Yu Huang — [Logit-Boundary Geometric Belief Interfaces and Sparse Sheaf-Enclave Protocols: A Self-Contained Substrate for Secure Network Electronic Health Record (EHR) Interoperability](http://arxiv.org/abs/2608.10300v2)
  <details><summary>📄 Abstract</summary>
  Electronic health-record interoperability is a boundary problem: legacy systems, generative models, terminology services, identity systems, and human reviewers may each expose rich internal states, while operational exchange requires a narrow shared interface of typed claims, bounded uncertainty, provenance, and explicit admission or abstention. This paper details a mathematical and engineering architecture for that interface. The organizing idea is the logit boundary: a discovery model may prop...
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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 71 papers

- **2026-08-12** — Saman Marandi, Yu-Shu Hu, Mohammad Modarres — [Constructing Dynamic Master Logic Models as Knowledge Graphs for Complex System Diagnostics Using Retrieval-Augmented Large Language Models](http://arxiv.org/abs/2608.12304v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Master Logic (DML) provides a hierarchical framework for representing system behavior by linking functional objectives to underlying structural elements. However, DML construction typically relies on expert interpretation of technical documentation, limiting scalability for complex systems. This study presents a framework for automated construction of DML models from system descriptions and their representation as Knowledge Graphs (KG-DML), using Retrieval-Augmented Generation and Large ...
  </details>

- **2026-08-12** — Jiarui Ma, Jianghan Wang, Yuheng Ma et al. — [NetlistBench: Evaluating LLM Reliability in SPICE Netlist Recognition and Manipulation](http://arxiv.org/abs/2608.12197v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in circuit design workflows, yet their reliability on simulator-facing SPICE netlist recognition and manipulation remains poorly understood and is rarely separated from high-level design reasoning. Although netlists are textual, they encode structured circuit objects through topology and parameters. We present \textbf{NetlistBench}, a structure-verified benchmark for SPICE netlist recognition and manipulation. NetlistBench contains 2,342 cases a...
  </details>

- **2026-08-12** — Martin Schuck, Maks Sorokin, Simone Manni et al. — [Learning Loco-Manipulation From SMPC Demonstrations With Sparse Offline-to-Online RL](http://arxiv.org/abs/2608.12063v1)
  <details><summary>📄 Abstract</summary>
  Integrating locomotion and manipulation is essential for robot autonomy, but scaling standard Reinforcement Learning (RL) to complex tasks is severely bottlenecked by the slow, manual process of dense reward shaping. To bypass this limitation, we leverage Sample-based Model Predictive Control (SMPC) entirely in simulation as an automated, rapidly tunable expert to generate massive offline datasets. Because this data solves the fundamental exploration problem, we can train an off-policy RL agent ...
  </details>

- **2026-08-12** — Ofir Ben Shoham, Shrutendra Harsola, Vignesh Subrahmaniam et al. — [GRPO for Financial Advice Generation: Outperforming Commercial LLMs under CATE Evaluation](http://arxiv.org/abs/2608.11787v1)
  <details><summary>📄 Abstract</summary>
  Generating actionable financial advice from business records demands that models integrate numerical reasoning, domain knowledge, and sound judgment, while avoiding recommendations that could harm the business. Direct supervision is difficult: historical decisions are not necessarily optimal, and high-quality free-form labels are expensive to obtain. We formulate financial advice generation as a reinforcement learning problem and fine-tune an open-weight language model using Group Relative Polic...
  </details>

- **2026-08-12** — Jiabao Zhuang, Changhao Jiang, Hanchen Wang et al. — [MuseCritic: Learning Multi-Aspect Song Rewards through Natural-Language Aesthetic Critiques](http://arxiv.org/abs/2608.11755v1)
  <details><summary>📄 Abstract</summary>
  Long-form song generation models continue to improve in duration, structural integrity, and acoustic complexity, making reliable aesthetic rewards increasingly important for aligning these models with human preferences. However, reward models for complete songs remain limited, and existing evaluators typically predict scores in a single forward pass without providing readable explanations. We introduce MUSECRITIC, a semi-scalar reward model that generates a natural-language critique covering fiv...
  </details>

- **2026-08-12** — Ran Li, Huiguo He, Jiahuan Cao et al. — [JieZi: A Large-Scale Expert-Audited Dataset and Benchmark for Ancient Chinese Character Exegesis](http://arxiv.org/abs/2608.11741v1)
  <details><summary>📄 Abstract</summary>
  The scholarly exegesis of ancient Chinese characters demands integrating visual observation, linguistic analysis, and historical context. However, existing computational approaches focus narrowly on subtasks such as character recognition and retrieval, lacking the structured datasets and benchmarks required for comprehensive scholarly analysis. To address this limitation, we introduce Ancient Chinese Character Exegesis (ACCE), a vision-language question answering (VQA) task that models the schol...
  </details>

- **2026-08-12** — Peijie Chen, Zhuanling Zha, Zhipeng Nie et al. — [Phoenix TTS: High-Fidelity Synthesis and Voice Conversion via Flow-Matching-Driven Speech Tokenization](http://arxiv.org/abs/2608.11737v1)
  <details><summary>📄 Abstract</summary>
  In current zero-shot text-to-speech systems, conventional semantic tokenizers are typically optimized using supervised automatic speech recognition or self-supervised learning objectives. However, due to the inherent nature of speech, semantic and acoustic information cannot be completely decoupled, and ASR-based tokenizers discard acoustic details to focus on linguistic content; models relying on them usually struggle to achieve optimal speaker similarity. Furthermore, these tokenizers are opti...
  </details>

- **2026-08-12** — Ebenezer Gelo, Geraud Nangue Tasse, Steven James et al. — [Redistribution-based Cost Inference Improves Sparse Safe Offline RL](http://arxiv.org/abs/2608.12306v1)
  <details><summary>📄 Abstract</summary>
  Safe offline RL typically assumes access to dense per-step cost annotations, but in practice supervisors provide only trajectory-level stop-feedback: a binary signal at the first unsafe transition, with no per-step attribution. We frame this as a temporal credit assignment problem and propose the Redistribution-based Cost Inference (RCI) framework, which converts sparse stop-feedback into dense per-step costs via return decomposition, then trains a constrained offline policy on the augmented dat...
  </details>

- **2026-08-12** — Yicheng Liu, Zibin Dong, Baijun Ye et al. — [G0.5: One Autoregressive Stream for Robot Reasoning and Action](http://arxiv.org/abs/2608.11739v1)
  <details><summary>📄 Abstract</summary>
  The prevailing recipe for Vision-Language-Action (VLA) models couples a pretrained VLM with a separately trained flow-matching action expert. This makes the VLM a context encoder rather than a decision-maker. We introduce G0.5, a pretrained autoregressive VLA in which a single transformer decoder emits reasoning and action tokens under a single objective. Three components make this tractable at foundation-model scale: a learnable cross-embodiment action tokenizer that maps heterogeneous robot ac...
  </details>

- **2026-08-12** — Xikai Sun, Kebin Liu, Haotian Wang et al. — [Motion-as-Prompt: Enhancing Motion Reasoning in Multimodal Large Language Models via Motion-Guided Cross-Frame Visual Prompting](http://arxiv.org/abs/2608.11655v1)
  <details><summary>📄 Abstract</summary>
  Motion-centric video reasoning is fundamental to interactive applications such as robotic manipulation and autonomous navigation. However, multimodal large language models (MLLMs) typically process videos through sparse uniform sampling to control visual-token and attention costs. This strategy may discard critical transitions between sampled frames, limiting reasoning about object movement, collisions, and causal interactions. To mitigate this issue, we propose Motion-as-Prompt (MaP), a track-g...
  </details>

- **2026-08-12** — AmirHossein Eshghi, Hamid Saadatfar, Seyyed Ali Hoseini et al. — [Class Activation Mapping in Explainable Computer Vision: A Method-Centered Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations](http://arxiv.org/abs/2608.12299v1)
  <details><summary>📄 Abstract</summary>
  Class activation mapping (CAM) is one of the most widely used visual explanation families in explainable artificial intelligence. Its purpose is intuitive: it converts internal model evidence into a heatmap that highlights the image regions, convolutional channels, tokens, or patches that support a target class or concept. Since the first CAM formulation in 2016, the field has moved far beyond global-average-pooled CNN classifiers. CAM-style methods now include gradient-based post-hoc explanatio...
  </details>

- **2026-08-12** — Zile Zhou, Huining Yuan, Weichen Zhang et al. — [SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought and Multi-Objective Process Reward](http://arxiv.org/abs/2608.12220v1)
  <details><summary>📄 Abstract</summary>
  Existing Vision-Language Models (VLMs) exhibits a critical bottleneck in robust spatial reasoning. Recent reinforcement learning (RL) methods aim to close this gap with verifiable outcomes, yet they suffer from poor credit assignment across intermediate reasoning steps. Concurrently, structured reasoning approaches overlook the critical depth perception necessary for comprehensive 3D understanding. To address these challenges, we propose SCOUT (Structured Chain-Of-Thought Utilizing Process-Super...
  </details>

- **2026-08-12** — Arda Uzunoglu, Benjamin van Durme, Daniel Khashabi — [Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge](http://arxiv.org/abs/2608.12218v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which ...
  </details>

- **2026-08-12** — Praveen Reddy, Charuta Mandke, Suvrankar Datta et al. — [A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench](http://arxiv.org/abs/2608.12138v1)
  <details><summary>📄 Abstract</summary>
  General-purpose large language models (LLMs) have recently been reported to match or exceed specialized clinical AI tools on medical benchmarks, but such comparisons draw on a narrow set of systems and on benchmarks developed largely in high-income settings. We evaluate VITA, a retrieval-augmented generation (RAG) system purpose-built for contextual knowledge retrieval in India and other low- and middle-income (LMIC) settings. VITA retrieves from a curated corpus of disease-specific guidelines, ...
  </details>

- **2026-08-12** — Ruibin Li, Tao Yang, Zhiyuan Ma et al. — [Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite Avatars](http://arxiv.org/abs/2608.12107v1)
  <details><summary>📄 Abstract</summary>
  Existing streaming video systems often rely on sequential, distillation-centered training pipelines to enable few-step long-video generation. However, this paradigm suffers from two limitations. First, failures or distribution shifts introduced in earlier stages affect later optimization, complicating the training process to converge. Second, the distillation-centric objective favours short-term generation but is prone to quality degradation when autoregressive errors accumulate over long rollou...
  </details>

- **2026-08-12** — Shukrullo Nazirjonov, Sai Prasanna, Anna Manasyan et al. — [Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models](http://arxiv.org/abs/2608.12078v1)
  <details><summary>📄 Abstract</summary>
  Learning world models from offline trajectories enables agents to accomplish different tasks through planning. Object-centric (OC) representations, which decompose a scene into a set of slots that bind to its objects, have been proposed as an inductive bias for world models that are more sample-efficient and generalize better. Yet prior object-centric world models (OCWMs) take the slot encoder as given and evaluate only in-distribution, leaving open whether the object-centric bias actually deliv...
  </details>

- **2026-08-12** — Chaoran Chen, Vy Nguyen, Ziji Zhang et al. — [Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via Controlled Error Injection](http://arxiv.org/abs/2608.11977v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents are commonly trained and evaluated in environments where tool calls succeed reliably, yet deployed tools can fail transiently, persistently, or silently. Robust recovery therefore requires more than repeated retries: an agent may need to retry the same path, switch to an alternative, or recognize that no viable path remains. We present BENCH2ROBUST, a framework that converts failure-free tool-use benchmarks into controlled stochastic environments with scenario-controlled so...
  </details>

- **2026-08-12** — Zheyu Zhuang, Ruiyu Wang, Nils Ingelhag et al. — [Enhancing Visual Domain Robustness in Behaviour Cloning via Saliency-Guided Augmentation](http://arxiv.org/abs/2608.11870v1)
  <details><summary>📄 Abstract</summary>
  In vision-based behavior cloning (BC), conventional image augmentations such as Random Crop and Color Jitter often fall short under substantial visual domain shifts, including changes in shadows, distractors, and backgrounds. Superimposition-based augmentations, which blend in-domain and out-of-domain images, have shown promise for improving generalization in computer vision, but their suitability for BC remains uncertain because task-critical semantics, spatiotemporal relationships, and agent-t...
  </details>

- **2026-08-12** — Xulin Fan, Jialu Li, Mohammad Nur Hossain Khan et al. — [Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning](http://arxiv.org/abs/2608.11587v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in model design and self-supervised audio representations have improved speech and audio understanding, yet infant-centered naturalistic recordings remain challenging due to limited labeled data, low signal-to-noise ratio, and cross-family domain shifts. We present a family-conditioned, multi-tier audio tagger that combines a LoRA-finetuned Whisper encoder with a lightweight, target-speaker-aware Transformer for long-context inference and framewise prediction across tiers. To imp...
  </details>

- **2026-08-12** — Vu Duc Anh, Nhat M. Hoang, Do Xuan Long et al. — [Reinforcing Step-level Reasoning for Effective Self-Correction in LLMs](http://arxiv.org/abs/2608.11573v1)
  <details><summary>📄 Abstract</summary>
  Achieving effective self-correction, where models verify and correct their own mistakes, remains a fundamental challenge for large language models (LLMs). In this work, we propose Self-Fix Step-DPO (SFS-DPO), a reinforcement learning based, two-stage framework for step-level self-verification and self-correction. The first stage strengthens step-level reasoning via step-level preference optimization, while the second stage explicitly trains models to self-verify and self-correct. We further intr...
  </details>

- **2026-08-12** — Thejani Gamage, Hyemin Gu, Zhizhen Zhang et al. — [Fine-Tuning Generative Models for Extreme Events via CVaR-Penalized Wasserstein Gradient Flows](http://arxiv.org/abs/2608.11544v1)
  <details><summary>📄 Abstract</summary>
  We propose CVaR-penalized Generative Particle Algorithm (CVaR-GPA), a robust, tail-agnostic algorithm for fine-tuning generative models to learn heavy-tailed distributions and capture extreme events, requiring no prior knowledge or estimation of the target's tail characteristics. The method is the Wasserstein gradient flow of the Lipschitz-regularized Kullback-Leibler (KL) divergence penalized by a Conditional Value-at-Risk (CVaR) discrepancy term: the Lipschitz-regularized KL divergence enables...
  </details>

- **2026-08-11** — Si'an Xie, Jiaxun Liu, Biao Yang et al. — [From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models](http://arxiv.org/abs/2608.10444v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have made substantial progress on reasoning tasks that require increasingly long and complex inferential chains. This progress primarily reflects reasoning depth. A complementary and comparatively unexamined capability is reasoning breadth: exploring multiple semantic directions in parallel and integrating the resulting clues into one coherent answer. We introduce MPAR-Bench, a bilingual English-Chinese benchmark that isolates reasoning breadth through multi-point as...
  </details>

- **2026-08-11** — Mehran Tamjidi, Hamidreza Dastmalchi, Ali Cheraghian et al. — [Test-Time Hallucination Control in Large Vision-Language Models](http://arxiv.org/abs/2608.11474v1)
  <details><summary>📄 Abstract</summary>
  Object Hallucination in large vision-language models (LVLMs), where models generate non-factual content about input images, remains a critical barrier to their reliability in real-world applications. Existing mitigation strategies can be categorized into training-based and training-free methods. Training-based methods often achieve strong performance but are costly, requiring extensive computational resources, large-scale data, and time-consuming fine-tuning. Training-free approaches are particu...
  </details>

- **2026-08-11** — Da Saem Lee, Yash Vardhan Pant, Sebastian Fischmeister — [Top-down Traffic Scenario Generation via Joint Initial-Goal Diffusion and Trajectory Infilling](http://arxiv.org/abs/2608.11407v1)
  <details><summary>📄 Abstract</summary>
  Robust traffic simulators are crucial for developing and testing autonomous vehicles to reduce the costly, labor-intensive real-world data collection process and the need for physical presence on the road. However, existing simulators require agents' initial states to generate trajectories, which limits scalability and diversity due to restrictions on the given initial states. While data-driven agent initialization has been widely studied, the generated initial states are not interpretable in te...
  </details>

- **2026-08-11** — Yueke Zhang, Zihan Fang, Kevin Leach et al. — [GraphAlignCoder: Aligning Program and Proof Graphs for Code Generation](http://arxiv.org/abs/2608.11394v1)
  <details><summary>📄 Abstract</summary>
  Code large language models (LLMs) can generate syntactically plausible programs that nevertheless violate hidden semantic constraints. Existing execution-feedback training methods identify whether a completed program fails, but provide limited supervision about how a correct solution should be organized. We introduce GraphAlignCoder, a training framework that transfers explicit correctness structure into code generation.   GraphAlignCoder constructs an implementation graph that captures control ...
  </details>

- **2026-08-11** — Jordan Coblin, Han Wang, Martha White et al. — [Dynamics Models for Offline Hyperparameter Selection in Real-World RL](http://arxiv.org/abs/2608.11349v1)
  <details><summary>📄 Abstract</summary>
  A key obstacle to deploying reinforcement learning in real-world systems is hyperparameter selection, particularly when simulators are unavailable and online experimentation is costly. Prior work has proposed calibration models trained on offline data to approximate environment dynamics and enable offline hyperparameter selection, but these methods have so far been evaluated only in simple simulated settings. In this paper, we present the first application of calibration models in a real-world i...
  </details>

- **2026-08-11** — Zixi Huang, Xiheng Wang, Andrew Wang et al. — [Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost](http://arxiv.org/abs/2608.11338v1)
  <details><summary>📄 Abstract</summary>
  Recently, the practice of augmenting LLM agent capability with skills has gained prevalence. We explore the cost effective adaptation of agents to novel domains by means of learning skills. Existing works focus on performance gain over cost effectiveness. As a result, little is known about what skill learning strategies save cost. We argue that among all the different skill learning methods, those that view skills as programs can achieve the best cost reduction. By executing sequences of actions...
  </details>

- **2026-08-11** — Christos Tsepas, Chang Yan, Maximilian Fuetterer et al. — [Physics-Informed Implicit Neural Representations for Improved Myocardial Perfusion MRI Quantification](http://arxiv.org/abs/2608.11282v1)
  <details><summary>📄 Abstract</summary>
  Quantifying myocardial perfusion from cardiac magnetic resonance (CMR) can be achieved by fitting tracer-kinetic models to the dynamic contrast-enhanced MR data. However, fitting the observed data with multi-compartment exchange models, which describe the evolution of the contrast agent in the tissue, to estimate perfusion parameters is a challenging inverse problem that is sensitive to noise and acquisition variability. Previously, physics-informed neural networks (PINNs) have been proposed as ...
  </details>

- **2026-08-11** — Utshab Kumar Ghosh, Shubham Chatterjee — [When Do Anchor-Based Pointwise LLM Rerankers Help? Retriever Quality, Statistical Scope, and Anchor Design](http://arxiv.org/abs/2608.10528v2)
  <details><summary>📄 Abstract</summary>
  Anchor-based pointwise LLM reranking scores each candidate against a shared reference passage to recover cross-document context at pointwise cost. We study when this actually helps, using GCCP/PAGC as a representative method. Our study is reproduction-first. We use reproduction as a starting point for a controlled component-level stress test of anchor-based pointwise reranking. Our initial reimplementation, based only on the paper text, achieves 0.24 nDCG@10 instead of the reported 0.66, reveali...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 20 papers

- **2026-08-12** — Shivali Dalmia, Sumukha Thoppanahalli, Mohammadreza Sediqin et al. — [GUIDE: Governed Unified Intelligence for Document-to-Artifact Generation in Enterprise Settings](http://arxiv.org/abs/2608.12133v1)
  <details><summary>📄 Abstract</summary>
  Enterprise guideline documents are heterogeneous and multimodal, combining narrative text, complex tables, and embedded images. Existing LLM and VLM systems face hallucinated content, table structure degradation, and lack governed workflows extending beyond extraction to validation and artifact generation. This leaves enterprises to perform this manually, consuming 2-3 days per document. To address this, we introduce GUIDE, a governed multi-agent framework built on a shared versioned rule store ...
  </details>

- **2026-08-11** — Kelvin P. Idanwekhai, Enes Kelestemur, Benjamin Strickland et al. — [A Modular Agentic Framework for Synthetically Constrained Multi-Objective Hit-to-Lead Optimization](http://arxiv.org/abs/2608.11483v1)
  <details><summary>📄 Abstract</summary>
  Hit-to-lead optimization requires iterative design of hit analogs across competing potency, selectivity, physicochemical, pharmacokinetic, safety, and synthetic constraints. We present SABLE (Synthetically-accessible Agentic Bayesian Ligand Exploration), an open-source framework that employs natural-language orchestration to guide chemical structure optimization. SABLE uses an LLM to interpret user-defined goals and route tasks, while specialized tools perform reaction-templated analog enumerati...
  </details>

- **2026-08-11** — Paul R. B. Houssel, Olivier Levillain, Sylvie Laniepce et al. — [A Study of Kernel Telemetry Options for Security-Oriented Provenance](http://arxiv.org/abs/2608.11418v1)
  <details><summary>📄 Abstract</summary>
  Provenance aims to capture the origins, transformations, and interactions of system objects for security and forensic applications. Existing provenance capture approaches still face major challenges and are not yet ready for production environments. In this paper, we first analyze the main kernel telemetry capture approaches, identifying eBPF as the most promising, and complement this analysis with micro benchmarks to assess its performance overhead and the filtering mechanisms used to achieve c...
  </details>

- **2026-08-11** — Xiaoyang Hu, Mike Angstadt, Shane Storks et al. — [Conflict and Congruency Effects in Large Language Models: In-Weight and In-Context Competition in a Verbal Conflict Task](http://arxiv.org/abs/2608.11510v1)
  <details><summary>📄 Abstract</summary>
  Congruency effects, observed in conflict tasks such as Stroop and flanker tasks, have been investigated for nearly a century in psychology and neuroscience, but their mechanistic basis is not fully understood. We introduce a verbal-only LLM conflict task in which a prompt stem elicits a default same-color completion and an explicit rule either agrees with (congruent condition) or conflicts with (incongruent condition) the completion. Gemma-2-2B and six Pythia models ranging from 410M to 12B para...
  </details>

- **2026-08-11** — Brian Wang, Bin Feng, Xiaoman Pan et al. — [Apodex Discovery: Reality Benchmarks and Environments for Evaluating and Building Discoverative Artificial Intelligence](http://arxiv.org/abs/2608.11341v1)
  <details><summary>📄 Abstract</summary>
  Apollo did not reach the Moon merely because its engineers could solve difficult equations. It succeeded by turning a distant ambition into a mission architecture of explicit objectives, simulation, verification, and repeated correction. AI now faces a similar transition: frontier models can solve difficult tasks once the problem, tools, and success criteria are specified, yet consequential real-world challenges rarely arrive in an executable or verifiable form.   We introduce Apodex Discovery, ...
  </details>

- **2026-08-11** — Xiaokang Qu, Yiting Lin — [HexEval: An Evidence-Driven Hexagonal Framework for Multidimensional Scholar Assessment](http://arxiv.org/abs/2608.10584v2)
  <details><summary>📄 Abstract</summary>
  Scholar assessment plays a fundamental role in faculty recruitment, funding allocation, academic promotion, and talent discovery. Existing scholar assessment methods predominantly rely on bibliometric indicators and reputation proxies, while recent large language model (LLM)-based approaches mainly focus on evaluating individual research papers rather than comprehensively assessing scholars. We argue that scholar assessment should be formulated as an evidence-driven reasoning problem that jointl...
  </details>

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


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-08-10** — Yuanchi Zhu, Kang An, Tengyue Wang et al. — [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](http://arxiv.org/abs/2608.09230v1)
  <details><summary>📄 Abstract</summary>
  Industrial-safety understanding requires more than detecting workers, equipment, and personal protective equipment. Models must also assess compliance, identify hazardous interactions, explain potential accident mechanisms, and recommend preventive actions. Existing safety datasets primarily focus on visual perception or isolated violation recognition and provide limited supervision for evidence-grounded reasoning. We introduce SafeSceneReason, a multimodal industrial-safety reasoning benchmark ...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-08-11** — Alex Deaconu, Anubhav Gupta, Manaal Basha et al. — [Do Influence Tactics Matter? Investigating Prompt Framing Effects in LLM Code Generation](http://arxiv.org/abs/2608.11513v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into software engineering workflows, helping developers write, debug, test, and maintain code. While prompt wording and structure are known to influence model performance, the impact of psychologically inspired prompt framings remains unexplored. This study investigates whether different psychology-based communication strategies that humans use to persuade or motivate others can lead to more effective prompt framing, which may, in turn, af...
  </details>

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


### 📂 other
*其他安全相关 / Other Security-Related* — 150 papers

- **2026-08-12** — Junliang Liu, Ruoyu Li, Wenxin Tang et al. — [Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents](http://arxiv.org/abs/2608.12273v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly rely on third-party skills, using natural-language descriptions for selection and instruction bodies for planning. This progressive-disclosure design exposes two sequential control points to untrusted publishers: a static skill may steer an otherwise correct task onto an unnecessarily costly trajectory. Prior work studies selection manipulation, malicious skill instructions, and tool-chain resource amplification largely separately, leaving their end-to-end composition unc...
  </details>

- **2026-08-12** — Nicholas E. Kyrkewood — [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](http://arxiv.org/abs/2608.11775v1)
  <details><summary>📄 Abstract</summary>
  Gist-based context compression---summarising older conversation history into compact representations---is a common approach in long-horizon language model agents, yet its effect on different types of memory retrieval is poorly understood. We use Salience-Weighted Consolidation (SWC), a biologically-inspired compression framework motivated by sleep-based memory consolidation, as a diagnostic probe to study when gist compression helps and when it hurts. SWC scores conversation history by salience,...
  </details>

- **2026-08-12** — Mengjie Tian, Xinrui Zhang, Tianyu Li et al. — [Video2Track: From Real-World Interaction Videos to Steerable Adversarial Closed-Track Testing for Automated Driving Systems](http://arxiv.org/abs/2608.11592v1)
  <details><summary>📄 Abstract</summary>
  Closed-track testing plays a fundamental role in the verification and validation of automated driving systems (ADS), particularly for safety-critical scenarios, by enabling reproducible evaluation under controlled conditions. However, most existing approaches still rely on standardized protocols or predefined trajectories, leading to overly scripted interactions and limited ability to reproduce the natural complexity of public-road traffic. To address this limitation, we propose Video2Track, a f...
  </details>

- **2026-08-12** — Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini et al. — [Large Language Model-Driven Small-Capitalization Trading: Integrating Financial News Sentiment, Macroeconomic Indicators, and Technical Signals](http://arxiv.org/abs/2608.12283v1)
  <details><summary>📄 Abstract</summary>
  Large language models can extract richer signals from financial news than fixed sentiment lexicons, and recent work has explored feeding such signals into portfolio construction. We study an uncertainty-aware construction that feeds model-predicted risk -- decomposed into aleatoric and epistemic components -- directly into the covariance matrix of portfolio allocators, rather than treating portfolio risk as fixed or adjusting only expected returns. We evaluate the pipeline on Russell 2000 equiti...
  </details>

- **2026-08-12** — Yuzhong Shen, Masha Sosonkina, Peng Xu et al. — [An Agentic Workflow for Legacy HPC Modernization: Converting the Two-Electron-Integral Core of GAMESS](http://arxiv.org/abs/2608.12249v1)
  <details><summary>📄 Abstract</summary>
  Modernizing legacy Fortran is a problem of volume: the transformations are individually routine, but the codebases can be enormous, and across much of computational science the work simply goes undone. We propose an agentic workflow that takes this work on at production scale, and we set out to measure how far such delegation can reach. In this work, three prompt-specialized agent roles operate under a version-controlled specification that the agents themselves authored and revised, while humans...
  </details>

- **2026-08-12** — Jiazheng Liu, Hang Li, Jiawei Zhang et al. — [GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors](http://arxiv.org/abs/2608.12203v1)
  <details><summary>📄 Abstract</summary>
  Generative models like Diffusion Models and Flow Matching have demonstrated remarkable capabilities in synthesizing high-fidelity driving videos, but are severely constrained by high inference latency due to the requirement of extensive sampling steps. We argue that this inefficiency stems from the prevailing reliance on a standard Gaussian source distribution, where consecutive frames are initialized as independent Gaussian noise. This paradigm disregards the rich spatiotemporal correlations in...
  </details>

- **2026-08-12** — Zunhai Su, Bohan Sun, Xialie Zhuang et al. — [Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus](http://arxiv.org/abs/2608.12149v1)
  <details><summary>📄 Abstract</summary>
  We present the first systematic study of Massive activations (MAs) in layer-interleaved HLA LLMs and uncover two architecture-aligned morphologies: MAs consistently spike immediately before full attention layers, forming pre-attention spikes (PAS), and can persist through intervening linear attention layers, giving rise to inter-spike plateaus (ISP). As full attention becomes denser, successive PAS become increasingly connected through ISP, ultimately recovering the stable MA morphology of full ...
  </details>

- **2026-08-12** — Long Hoang Nguyen, Eva Späthe, Sebastian Lins et al. — [No One to Blame: A Framework of Constitutive AI Unaccountability](http://arxiv.org/abs/2608.12104v1)
  <details><summary>📄 Abstract</summary>
  The increasing deployment of autonomous, agentic AI systems challenges traditional accountability mechanisms. Existing research predominantly frames AI accountability gaps as barriers that can be overcome through better standards, transparency, and institutional reform. We argue that this framing is insufficient: certain configurations of actors, systems, and institutions render AI accountability conceptually unachievable regardless of effort. We introduce the concept of constitutive AI unaccoun...
  </details>

- **2026-08-12** — Fabian Hüger — [Do Not Forget the Obvious - RISC: A Risk-Informed Slice-Coverage Protocol for Safe Autonomous Driving](http://arxiv.org/abs/2608.12051v1)
  <details><summary>📄 Abstract</summary>
  Aggregate metrics may not fully reflect performance in insufficiently examined high-risk driving conditions. We propose RISC (Risk-Informed Slice Coverage), a practical protocol for risk-guided stress testing and coverage-qualified evaluation. Risk-guided stress testing directs a finite audit budget toward risk-relevant sub-datasets, called risk slices, while coverage-qualified evaluation reports results together with explicit statements about which slices are sufficiently or insufficiently cove...
  </details>

- **2026-08-12** — Mengru Wang, Junfeng Fang, Shuofei Qiao et al. — [Mechanist: AI as a Scientific Instrument for Discovering the Mechanisms of Intelligence](http://arxiv.org/abs/2608.12036v1)
  <details><summary>📄 Abstract</summary>
  AI models have achieved remarkable success across diverse domains, yet the mechanisms underlying their capabilities and the risks they may pose remain poorly understood. As AI development becomes faster and increasingly automated, mechanistic exploration remains largely manual, widening the gap between what models can do and our ability to understand and control them. To bridge this gap, we introduce Mechanist, an agentic system that uses AI as a scientific instrument for the autonomous discover...
  </details>

- **2026-08-12** — Tuhinangshu Gangopadhyay, Rasmus Adler, Peter Liggesmeyer et al. — [From Safety Documentation to Safety Knowledge Support: An Evidence-Grounded LLM Framework for Medical Devices](http://arxiv.org/abs/2608.12025v1)
  <details><summary>📄 Abstract</summary>
  Medical devices are becoming more software-intensive, connected, and AI-enabled. Their development requires risk-management evidence aligned with ISO 14971 and, for software, IEC 62304. This evidence must be kept consistent across requirements, design decisions, software changes, verification results, complaints, and post-market data. These tasks are costly and depend on scarce safety and domain experts.   Large language models (LLMs) may reduce parts of this effort because medical-device safety...
  </details>

- **2026-08-12** — Zhixin Zhang, Xinke Jiang, Zhibang Yang et al. — [LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation](http://arxiv.org/abs/2608.11967v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory. A critical capability in such settings is reflection: assessing trajectory progress, identifying missing evidence and unreliable intermediate states, and deciding whether to continue, revise, or abandon the current branch. Learning effective reflection, however, is challenging because reflection is performed locally within the current branch, whereas its utilit...
  </details>

- **2026-08-12** — Mariama Celi Serafim De Oliveira, Motunrayo Osatohanmen Ibiyo, Marco Gianrusso et al. — [Developing LLM-based Multi-Agent Systems in Software Engineering: A Mixed-Method Experience Report](http://arxiv.org/abs/2608.11965v1)
  <details><summary>📄 Abstract</summary>
  The proliferation of Generative Artificial Intelligence (Gen AI) powered by large language models (LLMs) has transformed the software development process, introducing new paradigms for code generation, debugging, testing, and maintenance. While early applications focused on leveraging single, independent LLMs to assist developers with isolated tasks, recent advances have shifted toward multi-agent systems (MAS) that orchestrate multiple LLM-based agents working collaboratively toward common obje...
  </details>

- **2026-08-12** — Zhou Liu, Chaoyang Han, Zewei Pan et al. — [ExRole: From Team Trajectories to Executable Roles in Multi-Agent Language Models](http://arxiv.org/abs/2608.11949v1)
  <details><summary>📄 Abstract</summary>
  Roles provide an interpretable interface for organizing language-model agents, yet most multi-agent systems treat them as hand-written prompt labels disconnected from learned behavior and parameter updates. We argue that a useful role should instead be an executable control variable: it should summarize behavior predictive of future utility, guide subsequent interaction, and identify the trainable capacity responsible for that behavior. We introduce ExRole, a trajectory-to-role framework that le...
  </details>

- **2026-08-12** — Tom Adamczewski — [OEIS Open: How many conjectures can language models turn into theorems?](http://arxiv.org/abs/2608.11941v1)
  <details><summary>📄 Abstract</summary>
  We construct OEIS Open, a benchmark based on 492 open mathematical conjectures from the OEIS, formalized in Lean by Tsoukalas et al. Whereas these conjectures had previously been attempted only with a bespoke agent, our open-source evaluation code runs any generic language model (LM) against them, and is secure against LM cheating attempts. We find that LMs equipped with a minimal set of tools resolve 147 of these conjectures with a budget of \$50 per attempt, scoring 30% on OEIS Open. OEIS Open...
  </details>

- **2026-08-12** — Po-Jen Ko, Che-Cheng Wu, Hung-Chun Hsu et al. — [LODESTAR: Trustworthy Entropy Is Navigated, Not Merely Measured -- Reinforced Polarizer Keeps a Frozen LLM from Being Confidently Misled by the Wrong Evidence](http://arxiv.org/abs/2608.11922v1)
  <details><summary>📄 Abstract</summary>
  Predictive-distribution entropy makes a strong selection rule in retrieval-augmented question answering: across five QA benchmarks, keeping the candidate answer that a frozen respondent LLM produces with the lowest answer-token entropy lifts mean answer $F_1$ from 0.4769 to 0.5148 over the retriever's top-ranked passage, with no gold answers. Yet this lowest-entropy rule, which prior entropy-based selectors adopt, fails in a specific and consequential way: a misleading passage makes the responde...
  </details>

- **2026-08-12** — Zihao Xie, Pingrui Lai, Yitong Wu et al. — [DaViNCi: A Dataset Towards Outdoor Vision-and-Language Navigation with Continuous Actions and Dynamic Elements](http://arxiv.org/abs/2608.11901v1)
  <details><summary>📄 Abstract</summary>
  Vision-and-Language Navigation (VLN) has progressively expanded from indoor to outdoor environments. However, existing outdoor VLN datasets still rely on fixed discrete topological graphs for construction. It fails to align with the rapidly changing real-world outdoor environments and impedes the sim-to-real transfer of VLN agents. To address this limitation, we propose DaViNCi (\textbf{D}yn\textbf{a}mic \textbf{Vi}sion-and-Language \textbf{N}avigation in \textbf{C}ont\textbf{i}nuous Environment...
  </details>

- **2026-08-12** — Xueqin Niu, Mufan Liu, Yifan Wang et al. — [ResPCC: A Loss-Resilient Neural Point Cloud Codec over Lossy Networks](http://arxiv.org/abs/2608.11845v1)
  <details><summary>📄 Abstract</summary>
  Point cloud compression (PCC) is critical for efficient storage and transmission of 3D data. While recent learning-based PCC methods achieve good rate-distortion (R-D) performance, they generally rely on ideal transmission conditions. In practice, packet loss is a common issue and can severely distort latent features, causing coordinate drift and geometric degradation. To address this challenge, we present ResPCC, the first end-to-end neural point cloud codec designed to offer intrinsic resilien...
  </details>

- **2026-08-12** — Alireza A. Safaei, Laura M. Vowels, Matthew J. Vowels et al. — [Quantifying the Relationship Between Clinical Safety and Environmental Impact in Therapeutic LLMs](http://arxiv.org/abs/2608.11830v1)
  <details><summary>📄 Abstract</summary>
  The deployment of large language models (LLMs) in mental health contexts raises questions about the relationship between clinical safety and environmental cost. In this paper, we examine this relationship by combining K-Bench clinical safety scores with EcoLogits life-cycle assessment estimates across 47 supported model configurations. We evaluate model performance and environmental impact across four dimensions: energy use, carbon emissions, water consumption, and abiotic depletion. The results...
  </details>

- **2026-08-12** — Sophia Abraham, Ben Bucknall — [Silent Updates: Measuring and Closing the Post-Deployment Disclosure Gap](http://arxiv.org/abs/2608.11803v1)
  <details><summary>📄 Abstract</summary>
  Deployed foundation models are often not static systems, with providers able to modify system behavior through fine-tuning, classifier updates, system prompt revisions, retrieval changes, and routing changes. These updates can be made silently -- that is, without public disclosure, a version increment, or re-evaluation. Such silent updates challenge a core assumption behind current AI governance frameworks that an externally verifiable chain of custody links the model referred to in evaluation r...
  </details>

- **2026-08-12** — Duy-Dong Nguyen, Le-Van Thai, Hoai Nhan Pham et al. — [ProBAG: Prototype-Guided Boundary-Aware Graph Diffusion for Weakly Supervised Histopathology Segmentation](http://arxiv.org/abs/2608.11765v1)
  <details><summary>📄 Abstract</summary>
  Weakly supervised semantic segmentation enables histopathology tissue segmentation from image-level annotations, avoiding costly pixel-level labeling by expert pathologists. However, CAM-based methods often localize only highly discriminative regions and remain unreliable near tissue interfaces. We propose ProBAG, a stage-1 pseudo-mask generator that combines dataset-specific visual prototypes with pathology-aligned CONCH text prototypes over multi-scale frozen UNI features. ProBAG introduces tw...
  </details>

- **2026-08-12** — Yuxuan Zhang, Haozhong Xiong, Jiayi Song et al. — [UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos](http://arxiv.org/abs/2608.11752v1)
  <details><summary>📄 Abstract</summary>
  Talking-video character replacement requires coordinated transfer of appearance and voice while preserving the source motion, scene, linguistic content, and audio-video timing. Existing methods use separately optimized models for the two modalities, making audio-visual consistency difficult to enforce. We present UniSwap, the first framework for streaming joint audio-visual identity replacement in talking videos. Given a source video, a reference image, and a reference voice clip, UniSwap transf...
  </details>

- **2026-08-12** — Xikai Sun, Cangtian Zhou, Kebin Liu et al. — [HUGIN: Enhancing Vision-Language Planning for Autonomous Logistics Sorting](http://arxiv.org/abs/2608.11692v1)
  <details><summary>📄 Abstract</summary>
  Autonomous logistics sorting systems (ALSS) are an important industrial application of embodied AI, which requires joint planning over spatially disjoint camera views. We formulate this setting as Joint Multi-Scene Understanding (JMSU). With open-world visual understanding and task-planning capabilities, vision-language models (VLMs) are promising candidates for JMSU. However, directly applying existing VLMs to JMSU is non-trivial due to scarce cross-scene supervision and attention dispersion ca...
  </details>

- **2026-08-12** — Zijian Zhao, Sen Li — [Is Per-Agent Policy Composition Safe? Rethinking Successor-Feature Transfer in Cooperative Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2608.11658v1)
  <details><summary>📄 Abstract</summary>
  Many reinforcement learning systems, from fleet management to traffic signal control, must serve an objective that changes dynamically after deployment, and retraining a policy for each new objective is prohibitively expensive. For a single agent, this problem is well understood: successor features with generalized policy improvement, together with their universal extension, recombine a library of learned policies into a policy for any new objective, with a guarantee that the result is never wor...
  </details>

- **2026-08-12** — Alekh Jindal, Jyoti Pandey, Christina Pavlopoulou et al. — [Reverse Migration of Cloud Applications to On-premises](http://arxiv.org/abs/2608.11640v1)
  <details><summary>📄 Abstract</summary>
  Cloud has become ubiquitous to modern applications due to its agility and scalability. However, regulated industries still prefer to deploy on-premises due to security and compliance reasons. This creates a paradox for vendors who need to develop in the cloud but deploy on-premises, leading to long release cycles and complex maintenance. In this paper, we present Diel, the Tursio On-premises Migrator, a tool that automates reverse migration of cloud applications to on-premises environments. Diel...
  </details>

- **2026-08-12** — Pann Thinzar Seint, Bryan Atwood, Subas Chhatkuli — [Transferable Above-Ground Biomass (AGB) Estimation Model from Multi-Sensor Data with Sparse Field Calibration](http://arxiv.org/abs/2608.11638v1)
  <details><summary>📄 Abstract</summary>
  Spatially continuous quantification of forest above-ground biomass (AGB) is what makes carbon accounting credible and mitigation strategies actionable. While field inventories provide high localized accuracy, they are spatially sparse; conversely, spaceborne LiDAR from the Global Ecosystem Dynamics Investigation (GEDI) offers broad biomass samples but lacks spatial continuity and systematic underestimation of high-biomass forests. This paper presents an operational framework centered on a single...
  </details>

- **2026-08-12** — Chuyue Li, Jinpeng Yu, Haozhe Wang et al. — [AVA-Encoder: Towards Agent-Native Video Representation Learning](http://arxiv.org/abs/2608.12313v1)
  <details><summary>📄 Abstract</summary>
  Creative agents still lack an effective way to learn from high-quality human films, limiting their ability to produce cinematic-grade videos. A key challenge is the absence of a structured video representation that is both faithful to film content and directly usable for agentic reasoning and manipulation. To address the challenge, we propose the Agentic Video Auto-Encoder (AVA-Encoder), a framework for learning agent-native video representations via agentic auto-encoding.   AVA-Encoder transfor...
  </details>

- **2026-08-12** — Zhenjie Yang, Xingyu Jiao, Guopeng Zhong et al. — [HandEdit: A Unified Benchmark for Egocentric Human-to-Robot Dexterous Hand Image Editing](http://arxiv.org/abs/2608.12122v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation with dexterous hands is a cornerstone of Embodied AI, yet its progress is stifled by the high cost of collecting embodiment-aware teleoperation data. While abundant egocentric videos of human hands offer a scalable alternative, the profound discrepancies in appearance, articulation, and camera viewpoints between human and robotic data raise significant challenges for co-training. Though existing general image-editing models demonstrate strong capabilities, they lack necessar...
  </details>

- **2026-08-12** — Shiji Zhou, Kunlin Lyu, Lei Zhang et al. — [MOON: Multi-Objective OrthoNormalized Updates for Multitask Learning](http://arxiv.org/abs/2608.11749v1)
  <details><summary>📄 Abstract</summary>
  Multi-objective optimization (MOO) has demonstrated significant success in multi-task learning by mitigating task conflicts through gradient manipulation. However, most existing methods flatten model parameters into vectors and perform gradient manipulation under Euclidean geometry, thereby overlooking the matrix structure prevalent in modern architectures such as Transformers. In this paper, we show that gradient manipulation in Euclidean space does not generally yield the steepest descent dire...
  </details>

- **2026-08-12** — Siyu Xu, Yunke Wang, Zijian Wang et al. — [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](http://arxiv.org/abs/2608.11671v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models can follow instructions and manipulate objects, but their performance often collapses out of distribution (OOD), when the scene, viewpoint, or object differs from training. Adapting to each new situation typically requires collecting more data and fine-tuning. We present StellaVLA, a framework that instead adapts at test time by conditioning on a single retrieved demonstration. The key idea is to move beyond imitating what an expert did and instead convey why:...
  </details>

- **2026-08-12** — Carlos Alberto Fernández-y-Fernández, Jorge R. Aguilar-Cisneros — [The Role Specialization Model (RSM): Coordinating LLM-Based Tools in Agentic Software Development - An Exploratory Case Study](http://arxiv.org/abs/2608.12311v1)
  <details><summary>📄 Abstract</summary>
  The integration of large language models (LLMs) into software development workflows has given rise to a paradigm known as Agentic Software Engineering (SE 3.0), in which autonomous agents manage full development life cycles under human supervision. This paper presents an exploratory case study in which three LLM-based tools, Antigravity (an agentic IDE with a Gemini 2.5 backend), Gemini CLI, and Qwen Code (local execution via Ollama), are coordinated according to a role-distribution framework pr...
  </details>

- **2026-08-12** — Yusuf Pisan — [Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior](http://arxiv.org/abs/2608.12292v1)
  <details><summary>📄 Abstract</summary>
  An effective large language model (LLM) tutor must often decline to give an answer it could easily produce. In a randomized study, students who used an unguarded chatbot scored higher while practicing but lower on a later test taken without it, whereas a Socratically guarded version of the same model kept the practice gain and removed the later loss [4]. Reliable answer-withholding is therefore central to a tutor's value, yet a capable model pressed by a frustrated student does not withhold reli...
  </details>

- **2026-08-12** — Steven Campbell, Karl Kristian Engelund — [When should one stop the most exciting game? Sequential Inference for win-martingales](http://arxiv.org/abs/2608.12291v1)
  <details><summary>📄 Abstract</summary>
  Prediction markets have become a prominent way of aggregating beliefs about binary future events, and their price processes are often interpreted as evolving win probabilities, or ``win-martingales.'' Motivated by this perspective and recent work on Aldous' ``most exciting game,'' we study when a decision maker should stop observing a win-martingale and make a decision about the outcome. In particular, we allow the true outcome to be revealed at a fixed finite horizon, as in a sports game or ele...
  </details>

- **2026-08-12** — Pedro Sousa, Will Tebbutt, Sadiq Jaffer et al. — [Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling](http://arxiv.org/abs/2608.12271v1)
  <details><summary>📄 Abstract</summary>
  Global weather reanalyses and forecasts resolve the evolving atmospheric state on coarse grids, but site-specific applications require predictions at arbitrary locations where near-surface conditions also depend on unresolved terrain and land-surface properties. Existing probabilistic downscalers address this gap using hand-crafted topographic descriptors. We ask instead whether Earth observation foundation models can provide transferable sub-grid surface representations for probabilistic weathe...
  </details>

- **2026-08-12** — Ting-Chen Hsu, Lianye Zhang, Jiangxu Lin et al. — [IF:CARGO: LLM-Based Semantic Compilation for Al-Native Rule Programming Games](http://arxiv.org/abs/2608.12195v1)
  <details><summary>📄 Abstract</summary>
  This case study presents IF: CARGO, an experimental puzzle game that uses a large language model as a semantic compiler rather than an autonomous game-playing agent. Players author IF/THEN rules in natural language, which the model translates into a constrained command schema for deterministic validation and execution by the game engine. This architecture creates a playable loop of expression, execution, observation, and revision, framing AI interaction as semantic debugging. A mixed-methods pla...
  </details>

- **2026-08-12** — Zhao Su, Yuxin Xia, Haoran Li et al. — [HYDRA: Hyperbolic Dynamic Representation Architecture for Kolmogorov-Arnold Networks](http://arxiv.org/abs/2608.12194v1)
  <details><summary>📄 Abstract</summary>
  Kolmogorov-Arnold Networks (KANs) enhance nonlinear function approximation by replacing scalar weights with learnable univariate functions. However, assigning an independent function to every connection results in substantial parameter redundancy, limiting their scalability and efficiency. To reduce this redundancy, we introduce \textbf{HY}perbolic \textbf{D}ynamic \textbf{R}epresentation \textbf{A}rchitecture (HYDRA), a parameter-efficient hyperbolic extension of KAN that combines spline-based ...
  </details>

- **2026-08-12** — Yuchao Wu, Junqin Li, XingCheng Liang et al. — [SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges](http://arxiv.org/abs/2608.12129v1)
  <details><summary>📄 Abstract</summary>
  While retrieval-augmented generation (RAG) has proven effective at giving LLMs access to external knowledge, mainstream dense-retrieval implementations remain inherently limited in handling structured constraints and multi-hop reasoning. Graph-based methods address this by constructing knowledge graphs offline, but they often fragment semantics, incur high maintenance, and complicate incremental updates. We propose SAG (SQL-Retrieval Augmented Generation), a structured retrieval architecture tha...
  </details>

- **2026-08-12** — Yihui Fu, Zhengyang Li, Tim Fingscheidt — [Rethinking Language Model-Based Generative Speech Enhancement in the Latent Space of a Neural Audio Codec](http://arxiv.org/abs/2608.12082v1)
  <details><summary>📄 Abstract</summary>
  Language model (LM)-based speech enhancement (SE) has recently emerged rapidly using latent space features of neural audio codecs (NACs). In this paper, first, we present a unified framework covering six popular LM-based generative SE modeling paradigms based on discrete/continuous latent NAC features: discrete or continuous autoregressive (D/CAR) SE, discrete or continuous non-autoregressive (D/CNAR) SE, discrete diffusion (DDiff) SE, and continuous flow matching (CFM) SE. Second, we are the fi...
  </details>

- **2026-08-12** — Dehui Gao, Zhixian Zhao, Zhennan Lin et al. — [The SLT 2026 SmartGlasses Challenge: Benchmarking Egocentric Multi-Talker Speech Recognition and Understanding with Audio-Language Models](http://arxiv.org/abs/2608.12034v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models (LLMs) and multimodal LLMs (MLLMs) have created new opportunities for wearable speech interfaces, with smart glasses providing an egocentric platform for continuous audio sensing and assistance. However, speech recognition and understanding in this setting remain challenging because of dynamic acoustic conditions, speaker overlap, and the spatial ambiguity introduced by wearer-centered recording geometry. To support systematic evaluation in this setting, ...
  </details>

- **2026-08-12** — Selim Jerad, Anej Svete, Jiaoda Li et al. — [Disentangling the Expressivity of RoPE](http://arxiv.org/abs/2608.11909v1)
  <details><summary>📄 Abstract</summary>
  Two accounts recur in explanations of the success of rotary position embeddings (RoPE). Expressivity studies associate periodic position information with modular predicates, whereas mechanistic and long-context studies emphasize positional anchors and local offsets. We formalize both accounts for fully uniform, finite-precision soft-attention transformers. We find that, if every rotary component is periodic, RoPE transformers recognize exactly the languages definable in past temporal logic with ...
  </details>

- **2026-08-12** — Junyoung Kim, Wonbin Kweon, Woojoo Kim et al. — [From Overlooked to Explored: Recovering Item Relations via Mixture of Perspectives for Sequential Recommendation](http://arxiv.org/abs/2608.11846v1)
  <details><summary>📄 Abstract</summary>
  Capturing user preference from a user's interaction sequence is the central challenge of Sequential Recommendation (SR). This preference intuitively emerges from inter-item relations: each item transition reflects a preference embedded in the relations between items, making the faithful capture of these relations essential for accurate recommendation. For this reason, self-attention is dominant in sequential recommendation for its ability to compute pairwise item interactions, yet our empirical ...
  </details>

- **2026-08-12** — Chencheng Zhu — [Orientation, not magnitude: the causal structure of task-vector interference in merged language models](http://arxiv.org/abs/2608.11797v1)
  <details><summary>📄 Abstract</summary>
  Model merging by task arithmetic works until it doesn't, and the field diagnoses why with magnitudes: layerwise representation bias, deviations from cross-task linearity, parameter overlap. Tracking the exact layerwise cross-term of merged LLMs through a factorial ledger and intervening on it directly, we find magnitude insufficient - and inconsistent across model families - as a diagnostic axis. An exact decomposition of the layerwise flux shows it is dominated by amplifying transport of the ex...
  </details>

- **2026-08-12** — Xining Xun — [Causal Structure is Inducible but Functionally Decoupled: The Routing/Readout Boundary of a Typed Mechanism Library](http://arxiv.org/abs/2608.11767v1)
  <details><summary>📄 Abstract</summary>
  When a language model answers an interventional question, the computation it must perform depends on the type of evidence the query requires. We report a decoupling in how a transformer organizes causal knowledge: slot-by-type structure induced by type-level supervision organizes routing, yet remains functionally decoupled from answer readout. We establish this with a typed mechanism library -- discrete mechanism slots partitioned by evidence type, auditable at the state level -- on a causal-wor...
  </details>

- **2026-08-12** — Giancarlo Sportelli, Nicola Belcari, Roberta Pace et al. — [Automated binary classification of hazelnut X-ray images: A deep-learning benchmark for quality assessment](http://arxiv.org/abs/2608.11759v1)
  <details><summary>📄 Abstract</summary>
  Non-destructive X-ray imaging can reveal internal hazelnut defects that are difficult to detect by external inspection alone; however, automated interpretation remains challenging because of subtle radiographic differences among classes, marked class imbalance, and limited annotated data. Here, we present a benchmark for binary hazelnut quality classification (healthy versus defective) based on 799 segmented single-kernel X-ray images (224 x 224 pixels, grayscale), grouped into 101 acquisition u...
  </details>

- **2026-08-12** — Michael Schlee, Fabian Lukassen, Christoph Weisser — [LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification](http://arxiv.org/abs/2608.11753v1)
  <details><summary>📄 Abstract</summary>
  Financial text is produced and interpreted within a market environment, yet financial text classifiers almost always receive text alone. We study whether financial time series are useful as an additional input on the task of classifying sentences from Federal Reserve communication as hawkish, dovish, or neutral. Our system, \lfts{}, extends the \lf{} architecture with this modality: a small voting network combines three independently trained components, a fine-tuned RoBERTa encoder, a prompted l...
  </details>

- **2026-08-12** — Yueru Yan, Siqi Wu, Thai Le — [Locating and Controlling Implicit Personalization in Large Language Models](http://arxiv.org/abs/2608.11735v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) often shift their outputs in response to implicit demographic cues even when users never state a demographic identity. Previous work has documented this behavior, but the connection between these behavioral changes and the model's internal activations remains unclear. Using matched cued and neutral conversations across five LLMs, we establish that a localized internal activation signal tracks changes in recommendations, with correlations up to r=0.87. When multiple c...
  </details>

- **2026-08-12** — Zijian Zhao, Sen Li — [Low-Interaction-Rank Learning: Unifying Multiplicative Dual-Encoder Heads](http://arxiv.org/abs/2608.11661v1)
  <details><summary>📄 Abstract</summary>
  A multiplicative dual-encoder network computes a real-valued output for a pair of inputs as the inner product of their separate encodings. This architecture has been developed independently in operator learning, bipartite matching, contrastive vision-language models, retrieval, and other areas, yet no unified theory guides the basic design decisions: how many interaction modes to represent, how to normalize the encoders, and when the architecture should be avoided. We provide such a foundation b...
  </details>

- **2026-08-12** — Tianci Liu, Zihan Dong, Tianchun Li et al. — [Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing](http://arxiv.org/abs/2608.11660v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve remarkable performance across natural language tasks, yet they are trained on static corpora and their knowledge quickly becomes outdated in a fast-changing world. This motivates knowledge editing (KE), which updates specific knowledge in an LLM without changing unrelated others. Recent works move from structured knowledge triples toward unstructured KE (UKE), where the edit is a free-form passage that may state multiple facts at once. Nonetheless, existing e...
  </details>

- **2026-08-12** — Gregor Schubert — [Organizational Technology Ladders: Remote Work and Generative AI Adoption](http://arxiv.org/abs/2608.11626v1)
  <details><summary>📄 Abstract</summary>
  This study proposes that firms move along an "organizational technology ladder": adopting one technology transforms hiring and work processes and builds skills and organizational capital that change the cost of adopting subsequent technologies. I study how firms' adoption of remote work technology during the COVID-19 period shaped later uptake of generative AI. Using U.S. job-posting data and an instrumental-variables strategy based on predicted differences in labor-market pressure to offer remo...
  </details>

- **2026-08-12** — Jiaru Zhang, Can Cui, Yi Xu et al. — [How Can Driving World Models Do Counterfactual Prediction?](http://arxiv.org/abs/2608.11601v1)
  <details><summary>📄 Abstract</summary>
  Driving world models are often interpreted as counterfactual simulators for observed driving episodes: given a factual driving log, they are asked what would have happened under an alternative ego action. In this paper, we identify a fundamental mismatch between this goal and direct action-conditioned prediction. The direct prediction uses the shared history and the alternative action but not the factual continuation observed after that history. It can therefore generate a plausible future witho...
  </details>

- **2026-08-11** — Jeremy Spence, Nicholas Assaderaghi, Jinhao Zhu et al. — [The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark](http://arxiv.org/abs/2608.11469v1)
  <details><summary>📄 Abstract</summary>
  AI agents are rapidly improving in cybersecurity capabilities when the source code is available for analysis, yet much of the software most consequential to cybersecurity, including malware, firmware, and proprietary applications, is available only as binaries. Analyzing such software requires reverse engineering(RE): recovering program semantics before the analysis can be meaningfully performed. However, evaluating agentic RE poses a fundamental challenge: benchmark instances must be unseen as ...
  </details>

- **2026-08-11** — Hunter McNichols, Kai Du, Andrew Lan — [Principal Trait Analysis: Towards Deriving "Skills" in Human-AI Collaboration](http://arxiv.org/abs/2608.11460v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model-powered agents are increasingly used in the workplace via human-artificial intelligence (AI) collaboration. In this new era of work, it is important to understand the kinds of prompting traits that contribute to task success. Moreover, we need to uncover key skills required for modern professionals and inform educators on how to foster these skills among students. Existing guidelines for human-AI collaboration are built from either top-down theory or context-specific observa...
  </details>

- **2026-08-11** — Jungyoon Lee, Gyuil Lim, Doeon Kim et al. — [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](http://arxiv.org/abs/2608.11458v1)
  <details><summary>📄 Abstract</summary>
  We present the first-place solution to the MeViS-Text track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge 2026: referring video object segmentation guided by written motion expressions, including deceptive no-target expressions that match no object in the video and must yield empty masks in every frame. Our pipeline, SSUPER, resolves each expression into a visual concept, generates full-video candidate masklets with SAM~3.1, and selects target IDs. At every reasoning stage, ...
  </details>

- **2026-08-11** — Pardis Taghavi, Santosh Bhavani — [From Numbers to Judgment: Specialist LLM Agents and Reinforcement Learning for European Listed Real Estate](http://arxiv.org/abs/2608.11381v1)
  <details><summary>📄 Abstract</summary>
  We study whether the localized numerical operations and integrative judgments of financial analysis benefit from the same form of LLM specialization. Larix maps a 16-lens European listed-real-estate analysis framework to eight lens-aligned specialists; we compare a frontier LLM under monolithic versus specialist-decomposed prompting while holding the model, source evidence, task instructions, output schema, and scoring fixed. Across 19 firms spanning seven regulatory wrappers, decomposition impr...
  </details>

- **2026-08-11** — Hang Fan, Wei Wei, Shengwei Mei — [Market-Information-Aware Gated-LoRA of Foundation Models for Transferable Day-Ahead Electricity Price Forecasting](http://arxiv.org/abs/2608.11359v1)
  <details><summary>📄 Abstract</summary>
  Electricity price forecasting is crucial for market participants but remains difficult because prices are volatile, market-specific, and closely tied to anticipated system conditions. Existing supervised methods depend largely on market-specific historical data, limiting their use in newly established or data-scarce markets. This paper proposes a market-information-aware adaptation framework that transfers the Chronos-2 time-series foundation model to day-ahead electricity price forecasting. It ...
  </details>

- **2026-08-11** — Henry Han — [Governing Agentic AI in FinTech](http://arxiv.org/abs/2608.11344v1)
  <details><summary>📄 Abstract</summary>
  Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with little oversight. Yet agentic AI governance in FinTech is under-investigated. We argue the binding governance constraint is not capability but verifiability. We define the Verifiability Gap as the shortfall between the verification delegated authority demands and the explainability and reproducibility retained after a decision. It is indexed to a ver...
  </details>

- **2026-08-11** — Archan Dutta, Vyanktesh Kanungo — [Can Frontier LLMs Match Natively Multimodal Embeddings? A Comparison on Hard-Negative Text-to-Image Retrieval](http://arxiv.org/abs/2608.11343v1)
  <details><summary>📄 Abstract</summary>
  Multimodal retrieval and classification across different types of media, spanning text, images,video and audio, has traditionally relied on dual-encoder models that align visual and textual representations through contrastive learning. The March 2026 release of Gemini Embedding 2, Google's first natively multimodal embedding model to map text, images, video, audio, and documents into a single shared space, raises competition among multimodal retrieval systems. Simultaneously, frontier Large lang...
  </details>

- **2026-08-11** — V. Lora, J. I. Gonzalez-Carbajal, A. Pasquali et al. — [From blue to red spirals: Slow galaxy transformation via ram pressure stripping in TNG-50](http://arxiv.org/abs/2608.11336v1)
  <details><summary>📄 Abstract</summary>
  Late-type galaxies lose gas through ram-pressure stripping (RPS) after falling into a massive halo. Because this mechanism primarily removes the gaseous component while leaving the stellar disk largely undisturbed, it provides a pathway for quenching star formation without immediate morphological transformation. While RPS is well established in galaxy clusters, galaxy evolution in low-mass groups is often attributed to mergers, leaving open the question of whether RPS alone can drive the transit...
  </details>

- **2026-08-11** — Oğuz Akif Tüfekcioğlu, Ezgi Ekin, Mustafa Kaan Çevik et al. — [Gloss-Free Representation Learning for Cross-Dataset Sign Spotting](http://arxiv.org/abs/2608.11332v1)
  <details><summary>📄 Abstract</summary>
  Sign-language research for resource-constrained languages is often limited by the cost of dense linguistic labels such as glosses, temporal boundaries, and sign order. Broadcast news offers a practical alternative by pairing continuous signing with spoken-language transcripts, but this supervision is weak since text and signing are loosely aligned. Morphologically rich languages such as Turkish add further difficulty, as the same lexical meaning can appear in many inflected forms while some deri...
  </details>

- **2026-08-11** — Qianggang Ding, Xingyao Wang, Rui Feng et al. — [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](http://arxiv.org/abs/2608.10915v2)
  <details><summary>📄 Abstract</summary>
  After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeli...
  </details>

- **2026-08-11** — Rofiqul Islam, Lilatul Ferdouse — [Uncertainty-Aware and Explainable Ensemble Deep Learning Framework for Multi-Class Skin Lesion Classification](http://arxiv.org/abs/2608.11280v1)
  <details><summary>📄 Abstract</summary>
  Skin cancer diagnosis from dermoscopic images remains challenging due to high intra-class variability, inter-class similarity, class imbalance, and the limited interpretability of deep learning models. This paper proposes an uncertainty-aware and explainable deep learning framework for multi-class skin lesion classification. The framework combines a vision transformer model (MaxViT-Tiny) with CNN-based models (ConvNeXt-Tiny and EfficientNetV2-B0) through deep ensemble learning. Monte Carlo (MC) ...
  </details>

- **2026-08-11** — Frederick Hayes — [Predictive Allostatic Organization in Recurrent and Spiking Agents Under Partial Observability](http://arxiv.org/abs/2608.11506v1)
  <details><summary>📄 Abstract</summary>
  Adaptive behavior under partial observability depends on internal organization that carries information beyond the current observation. Drawing on Barrett and Miller's account of categorization as predictive, compressive, functionally organized, and allostatically constrained, we test whether recurrent and spiking agents develop internal states with corresponding computational properties. Agents operate in an energy-constrained foraging task requiring resource acquisition, threat avoidance, cont...
  </details>

- **2026-08-11** — Tianze Yang, Liang Wu, Ruitong Sun et al. — [Self-Evolving Code-with-Image Reasoning](http://arxiv.org/abs/2608.11292v1)
  <details><summary>📄 Abstract</summary>
  Multimodal models increasingly reach for tools when solving visual tasks (crop, zoom, rotate, brighten), a paradigm known as thinking-with-images. The central challenge is one of perception: tools mostly serve to expose visual evidence, reasoning over that evidence stays in language, and most targets are ones a human could in principle determine by inspection. Some visual questions, however, are not bottlenecked by perception: recovering their answers requires executing a multi-step visual algor...
  </details>

- **2026-08-11** — Jiayu Ding, Meilu Song, Yun Chen et al. — [CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting](http://arxiv.org/abs/2608.11150v2)
  <details><summary>📄 Abstract</summary>
  While 3D Gaussian Splatting (3DGS) has advanced open vocabulary scene understanding, existing methods remain confined to explicit queries. They struggle to interpret implicit intents, complex spatial constraints, and commonsense reasoning required for practical embodied interactions. To address this gap, we introduce the task of reasoning 3D Gaussian segmentation and construct two benchmarks, Causal-LERF and Causal-ScanNet. These benchmarks systematically evaluate commonsense, spatial, affordanc...
  </details>

- **2026-08-11** — Guobin Zhao, Xiao-Yan Li — [Chemically Meaningful Textualization Enables Explainable Validation of Metal-Organic Frameworks by Large Language Models](http://arxiv.org/abs/2608.11283v1)
  <details><summary>📄 Abstract</summary>
  Computation-ready metal-organic framework (MOF) databases are essential for high-throughput screening, yet many reported crystal structures remain chemically unreasonable or disordered, compromising simulation fidelity. Existing validation approaches can identify non-computation-ready structures, but they often rely on heuristic rules, license requirement, or offer limited interpretability. Here, we show that large language models (LLMs) can serve as interpretable validators of MOF structures wh...
  </details>

- **2026-08-11** — Davi R. Freitas, Gustavo L. Sandri, Ricardo L. de Queiroz — [Geometry-Based Compression of Plenoptic Point Clouds](http://arxiv.org/abs/2608.11273v1)
  <details><summary>📄 Abstract</summary>
  Plenoptic point clouds (PPC) are novel data structures that represent the light from different viewing directions in order to provide a higher degree of realism to regular point clouds. This is achieved by associating each point to multiple colors instead of a single one. Here, we present a method to efficiently compress the attributes of a PPC, consisting of a Karhunen-Loève transform over the color attributes followed by multiple attribute coders with intra prediction capability. This compress...
  </details>

- **2026-08-11** — Nicola Fabiano — [Inferential Capability Does Not Determine Legal Scope](http://arxiv.org/abs/2608.10601v2)
  <details><summary>📄 Abstract</summary>
  Two instruments of EU digital law place inference at their centre and mean different things by it. Article 3(1) of the AI Act uses the capability to infer constitutively: it is the central feature separating the regulated category from conventional software. The GDPR never defines inference, yet governs it protectively: the consequences follow from the processing of personal data and from what the inference says about, or does to, a person, whether or not the technology that produced it qualifie...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 577 |
| prompt-injection | 488 |
| memory-poisoning | 44 |
| tool-use-attack | 113 |
| backdoor | 413 |
| adversarial-attack | 555 |
| privacy-leakage | 3816 |
| steganography | 55 |
| misuse | 886 |
| red-teaming | 114 |
| vulnerability | 2665 |
| defense | 2362 |
| alignment | 2201 |
| robustness | 2188 |
| watermark | 280 |
| unlearning | 86 |
| agent-safety | 52 |
| benchmark | 57 |
| survey | 279 |
| other | 6263 |

---

📚 **全部 23494 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-13 12:57:39*